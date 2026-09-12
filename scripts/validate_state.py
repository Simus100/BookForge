#!/usr/bin/env python3
"""Structural and file-integrity validator for the bundled state schema. No semantic certification."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

SCHEMA_PATH = Path(__file__).resolve().parents[1] / 'schemas/bookforge_state.schema.json'


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('Invalid JSON number: '+x)))


def schema_errors(value, schema, path='$'):
    """Implements exactly the keywords used by our bundled schema, not a general JSON Schema engine."""
    errors = []
    types = schema.get('type', [])
    if isinstance(types, str):
        types = [types]
    checks = {'object': lambda v: isinstance(v, dict), 'array': lambda v: isinstance(v, list),
              'string': lambda v: isinstance(v, str), 'integer': lambda v: type(v) is int,
              'boolean': lambda v: type(v) is bool, 'null': lambda v: v is None}
    if types and not any(checks[t](value) for t in types):
        return [f'{path}: expected {types}']
    if 'const' in schema and value != schema['const']:
        errors.append(f'{path}: expected {schema["const"]}')
    if 'enum' in schema and value not in schema['enum']:
        errors.append(f'{path}: invalid enum')
    if isinstance(value, dict):
        for key in schema.get('required', []):
            if key not in value:
                errors.append(f'{path}.{key}: required')
        props = schema.get('properties', {})
        for key, item in value.items():
            if key in props:
                errors.extend(schema_errors(item, props[key], f'{path}.{key}'))
            elif schema.get('additionalProperties') is False:
                errors.append(f'{path}.{key}: unknown field')
    if isinstance(value, list):
        for i, item in enumerate(value):
            errors.extend(schema_errors(item, schema.get('items', {}), f'{path}[{i}]'))
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0):
            errors.append(f'{path}: empty string')
        if 'pattern' in schema and re.fullmatch(schema['pattern'], value) is None:
            errors.append(f'{path}: invalid pattern')
    if type(value) is int:
        if value < schema.get('minimum', value) or value > schema.get('maximum', value):
            errors.append(f'{path}: out of range')
    return errors


def safe_path(root, relative):
    p = PurePosixPath(relative)
    if not relative or p.is_absolute() or '..' in p.parts or '\\' in relative or ':' in relative:
        raise ValueError('Unsafe project path: ' + relative)
    result = (Path(root) / relative).resolve()
    if not result.is_relative_to(Path(root).resolve()):
        raise ValueError('Path escapes project root: ' + relative)
    return result


def validate(state, root=None):
    errors = schema_errors(state, read_json(SCHEMA_PATH))
    warnings = []
    if errors:
        return {'valid': False, 'errors': errors, 'warnings': warnings, 'files_checked': False, 'semantic_check': 'not_performed'}
    indexes = {}
    for group in ('volumes', 'chapters', 'scenes', 'characters', 'files', 'facts', 'promises', 'decisions'):
        indexes[group] = {x['id']: x for x in state[group]}
        if len(indexes[group]) != len(state[group]):
            errors.append(f'{group}: duplicate ID')
    def ref(value, group, where):
        if value is not None and value not in indexes[group]:
            errors.append(f'{where}: missing {group} reference {value}')
    seen_numbers, seen_paths = set(), set()
    for c in state['chapters']:
        ref(c['volume_id'], 'volumes', c['id'])
        ref(c['file_id'], 'files', c['id'])
        key = (c['volume_id'], c['number'])
        if key in seen_numbers:
            errors.append(f'{c["id"]}: duplicate chapter number within volume')
        seen_numbers.add(key)
        if c['status'] == 'accepted' and (not c['summary'].strip() or not c['file_id'] or not c['accepted_ref']):
            errors.append(f'{c["id"]}: accepted chapter needs summary, file and acceptance reference')
        if c['file_id'] in indexes['files']:
            f = indexes['files'][c['file_id']]
            if f['role'] != 'chapter':
                errors.append(f'{c["id"]}: manuscript must reference a chapter file')
            if c['status'] == 'accepted' and not f['required_for_resume']:
                errors.append(f'{c["id"]}: accepted manuscript must be required for resume')
    for s in state['scenes']:
        ref(s['chapter_id'], 'chapters', s['id'])
    cursor = state['resume_cursor']
    for key, group in [('volume_id','volumes'), ('chapter_id','chapters'), ('scene_id','scenes')]:
        ref(cursor[key], group, 'resume_cursor')
    chapter = indexes['chapters'].get(cursor['chapter_id'])
    scene = indexes['scenes'].get(cursor['scene_id'])
    if chapter and chapter['volume_id'] != cursor['volume_id']:
        errors.append('resume_cursor: chapter/volume mismatch')
    if scene and scene['chapter_id'] != cursor['chapter_id']:
        errors.append('resume_cursor: scene/chapter mismatch')
    replacements = {}
    for fact in state['facts']:
        ref(fact['source_chapter_id'], 'chapters', fact['id'])
        for char in fact['known_by']:
            ref(char, 'characters', fact['id'])
        ref(fact['supersedes'], 'facts', fact['id'])
        if fact['status'] in ('approved','superseded') and (not fact['approval'] or not fact['source'].strip()):
            errors.append(f'{fact["id"]}: approved facts require approval and source')
        if fact['supersedes']:
            old = indexes['facts'].get(fact['supersedes'])
            if fact['supersedes'] in replacements:
                errors.append(f'{fact["id"]}: multiple replacements of same fact')
            replacements[fact['supersedes']] = fact['id']
            if old and (old['status'] != 'superseded' or fact['status'] not in ('approved','superseded')):
                errors.append(f'{fact["id"]}: invalid amendment status')
        visited, current = set(), fact
        while current:
            if current['id'] in visited:
                errors.append(f'{fact["id"]}: amendment cycle')
                break
            visited.add(current['id'])
            current = indexes['facts'].get(current['supersedes'])
    for fact in state['facts']:
        if fact['status'] == 'superseded' and fact['id'] not in replacements:
            errors.append(f'{fact["id"]}: missing replacement')
    for promise in state['promises']:
        ref(promise['opened_in'], 'chapters', promise['id'])
        ref(promise['resolved_in'], 'chapters', promise['id'])
        if promise['status'] == 'fulfilled' and not promise['resolved_in']:
            errors.append(f'{promise["id"]}: fulfilled promise needs resolution chapter')
        if promise['status'] in ('deferred','dropped') and not promise['decision']:
            errors.append(f'{promise["id"]}: changed promise needs decision')
    for f in state['files']:
        try:
            target = safe_path(root or '.', f['path'])
            normalized = target.as_posix()
            if normalized in seen_paths:
                errors.append(f'{f["id"]}: duplicate file path')
            seen_paths.add(normalized)
            if root is not None:
                if not target.is_file():
                    (errors if f['required_for_resume'] else warnings).append(f'{f["id"]}: file unavailable')
                elif hashlib.sha256(target.read_bytes()).hexdigest() != f['sha256']:
                    errors.append(f'{f["id"]}: hash mismatch')
        except (ValueError, OSError) as e:
            errors.append(str(e))
    if root is None:
        warnings.append('File availability and hashes NOT checked: provide --root')
    if state['migration']['status'] == 'review_required':
        warnings.append('Migration needs author review before activation')
    return {'valid': not errors, 'errors': errors, 'warnings': warnings,
            'files_checked': root is not None, 'semantic_check': 'not_performed'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('state')
    ap.add_argument('--root', help='Project folder for file/hash verification')
    args = ap.parse_args()
    try:
        report = validate(read_json(args.state), args.root)
    except (OSError, ValueError) as e:
        report = {'valid': False, 'errors': [str(e)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['valid'] else 1)


if __name__ == '__main__':
    main()
