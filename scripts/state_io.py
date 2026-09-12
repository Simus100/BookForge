#!/usr/bin/env python3
"""Validate and atomically save a candidate state. Manuscript revisions must already exist."""
import argparse
import json
import os
from pathlib import Path
import tempfile
from validate_state import read_json, validate, safe_path


def atomic_write(path, data):
    path = Path(path)
    fd, name = tempfile.mkstemp(prefix='.'+path.name+'.', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def transition_errors(old, new):
    errors = []
    if old['project']['id'] != new['project']['id']:
        errors.append('Project ID mismatch')
    # Immutable history records: new versions are new records, never silent in-place edits.
    for group in ('files', 'decisions'):
        lookup = {x['id']: x for x in new[group]}
        for item in old[group]:
            if lookup.get(item['id']) != item:
                errors.append(f'Cannot delete or rewrite historical {group} record {item["id"]}')
    facts = {x['id']:x for x in new['facts']}
    for f in old['facts']:
        if f['status'] == 'proposed':
            continue
        replacement = facts.get(f['id'])
        if replacement is None:
            errors.append('Cannot delete canonical history: '+f['id'])
        elif replacement != f:
            permitted = dict(f, status='superseded')
            if replacement != permitted or f['status'] != 'approved':
                errors.append('Canonical change requires a new superseding fact: '+f['id'])
    chapters = {x['id']:x for x in new['chapters']}
    for c in old['chapters']:
        if c['id'] not in chapters:
            errors.append('Preserve chapter history; use discarded status: '+c['id'])
        if c['status'] != 'accepted':
            continue
        n = chapters.get(c['id'])
        if n is None or n['status'] != 'accepted':
            errors.append('Accepted chapter cannot be removed/demoted: '+c['id'])
        elif n != c and (n['accepted_ref'] == c['accepted_ref'] or not n['accepted_ref']):
            errors.append('Changed accepted chapter needs a new acceptance reference: '+c['id'])
    promises = {x['id']:x for x in new['promises']}
    for promise in old['promises']:
        n = promises.get(promise['id'])
        if n is None or n['statement'] != promise['statement'] or n['opened_in'] != promise['opened_in']:
            errors.append('Preserve promise identity and origin; close or supersede explicitly: '+promise['id'])
    return errors


def save(candidate, target, root, expected_revision):
    target = Path(target).resolve()
    root = Path(root).resolve()
    if not target.is_relative_to(root):
        raise ValueError('State must be inside project root')
    if not target.parent.is_dir():
        raise ValueError('Destination directory must already exist')
    lock = target.with_name(target.name+'.lock')
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        os.close(fd)
        old = read_json(target) if target.exists() else None
        current = old['revision'] if old else 0
        if current != expected_revision or candidate['revision'] != current+1:
            raise ValueError('Revision conflict; reload current state')
        if old:
            old_report = validate(old, root)
            if not old_report['valid']:
                raise ValueError('Existing state invalid: '+'; '.join(old_report['errors']))
        report = validate(candidate, root)
        if not report['valid']:
            raise ValueError('; '.join(report['errors']))
        if candidate['migration']['status'] != 'clear':
            raise ValueError('Migration review required before activation')
        if old:
            errors = transition_errors(old, candidate)
            if errors:
                raise ValueError('; '.join(errors))
        # Reject collisions between state control files and the manuscript manifest.
        protected = {target, lock, target.with_name(target.name+'.bak')}
        for f in candidate['files']:
            if safe_path(root, f['path']) in protected:
                raise ValueError('Manifest cannot reference state control files')
        payload = (json.dumps(candidate, ensure_ascii=False, indent=2)+'\n').encode()
        if old:
            atomic_write(target.with_name(target.name+'.bak'), target.read_bytes())
        atomic_write(target, payload)
        return report
    finally:
        lock.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('candidate')
    ap.add_argument('target')
    ap.add_argument('--root', required=True)
    ap.add_argument('--expected-revision', required=True, type=int)
    args = ap.parse_args()
    try:
        candidate = read_json(args.candidate)
        report = validate(candidate, args.root)
        if not report['valid']:
            raise ValueError('; '.join(report['errors']))
        report = save(candidate, args.target, args.root, args.expected_revision)
        print(json.dumps({'saved': True, 'revision': candidate['revision'], 'validation': report}, ensure_ascii=False))
    except (OSError, ValueError, KeyError) as e:
        print(json.dumps({'saved': False, 'error': str(e)}, ensure_ascii=False))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
