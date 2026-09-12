#!/usr/bin/env python3
"""Render every field of a structurally valid state to a derived Markdown view."""
import argparse
import json
from pathlib import Path
from validate_state import read_json, validate
from state_io import atomic_write


def render(state):
    report = validate(state)
    if not report['valid']:
        raise ValueError('; '.join(report['errors']))
    parts = ['<!-- GENERATED VIEW — edit the JSON, not this file. -->',
             '# BookForge · stato del progetto',
             'Vista derivata. La generazione non verifica file né coerenza semantica.']
    for key, value in state.items():
        body = json.dumps(value, ensure_ascii=False, indent=2)
        # A fence longer than any run in the user content prevents accidental closure.
        import re
        fence = '`' * max(3, max((len(x) for x in re.findall(r'`+',body)), default=0)+1)
        parts.append(f'## {key}\n\n{fence}json\n{body}\n{fence}')
    return '\n\n'.join(parts)+'\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('state')
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    try:
        if Path(args.state).resolve() == Path(args.output).resolve():
            raise ValueError('Output must differ from canonical JSON')
        atomic_write(args.output, render(read_json(args.state)).encode())
    except (ValueError, OSError) as e:
        print(str(e))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
