#!/usr/bin/env python3
"""Create a review-only 7.7 candidate from a 7.6 JSON; never overwrite the source or infer acceptance."""
import argparse
import copy
import json
from pathlib import Path
import re
from validate_state import read_json, validate

ROOT = Path(__file__).resolve().parents[1]


def migrate(old, project_id):
    if not isinstance(old, dict) or str(old.get('bookforge_version','')) not in ('7.6','7.6.1'):
        raise ValueError('Supported source versions: 7.6 / 7.6.1')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}', project_id):
        raise ValueError('Invalid project ID')
    state = read_json(ROOT/'examples/minimal/bookforge_state.json')
    state['project']['id'] = project_id
    meta = old.get('project_meta', {})
    state['project'].update(title=str(meta.get('title','')), language=str(meta.get('language','it')))
    kind = old.get('continuity_bible_condensed', {}).get('project_type')
    if kind in ('fiction','non-fiction','other'):
        state['project']['type'] = kind
    state['legacy_payload'] = copy.deepcopy(old)
    notes = ['Legacy payload preserved verbatim as JSON values; inspect before activation.',
             'Map manuscript/voice/archive files and hashes; no file availability inferred.',
             'Legacy approvals and canonical assertions require review; none inferred.']
    state['migration'] = {'status':'review_required', 'notes':notes}
    volume_id = 'v1'
    state['volumes'] = [{'id':volume_id,'title':'Legacy volume '+str(meta.get('volume',''))}]
    summaries = old.get('chapters_summary', {})
    for i, item in enumerate(old.get('index_planned', []), 1):
        raw = str(item.get('chapter', i))
        summary = summaries.get('recenti', {}).get(raw, summaries.get('vecchi', {}).get(raw, ''))
        number = item.get('chapter', i)
        if type(number) is not int or number < 1:
            number = i
        state['chapters'].append({'id':f'v1-c{i:03}', 'volume_id':volume_id, 'number':number,
            'title':str(item.get('title','')), 'status':'revised' if item.get('status')=='completato' else 'planned',
            'summary':str(summary), 'file_id':None, 'accepted_ref':None})
    vector = old.get('styledna', {}).get('vector','')
    for key, value in re.findall(r'\b(SL|SC|RV|VR|RL|FD|ST|SD|DW|ET|SUB|AP):\s*(\d+)\b', str(vector)):
        if 1 <= int(value) <= 10:
            state['styledna']['axes'][key] = int(value)
    state['styledna']['profile'] = str(old.get('styledna',{}).get('profile',''))
    state['styledna']['note'] = str(old.get('styledna',{}).get('vector_note',''))
    voice = old.get('voice_fingerprint', {})
    for dest, origin in [('golden_samples','golden_samples'),('idiolect','idiolect'),('baseline','stylometry_baseline')]:
        if origin in voice:
            state['voice_fingerprint'][dest] = copy.deepcopy(voice[origin])
    state['narrative_state'] = {'legacy_nst':copy.deepcopy(old.get('narrative_state_tracker',{})),
                              'strategic_board':copy.deepcopy(old.get('strategic_board',{}))}
    for i, fact in enumerate(old.get('continuity_bible_condensed', {}).get('canon_facts_or_didactic', []), 1):
        state['facts'].append({'id':f'legacy-f{i:03}', 'kind':'canon', 'status':'proposed',
            'statement':fact if isinstance(fact,str) else json.dumps(fact,ensure_ascii=False),
            'source':'Legacy JSON: requires source verification', 'source_chapter_id':None,
            'known_by':[], 'reader_knows':False, 'approval':None, 'supersedes':None})
    state['resume_cursor']['next_action'] = 'Review migration, restore file manifest and cursor from legacy_payload'
    report = validate(state)
    if not report['valid']:
        raise ValueError('Cannot migrate without resolving ambiguous structure: '+'; '.join(report['errors']))
    return state


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source')
    ap.add_argument('--output', required=True)
    ap.add_argument('--project-id', required=True)
    args = ap.parse_args()
    try:
        state = migrate(read_json(args.source), args.project_id)
        with Path(args.output).open('x', encoding='utf-8') as out:
            json.dump(state, out, ensure_ascii=False, indent=2)
            out.write('\n')
        print(json.dumps({'created':args.output, 'status':'review_required', 'notes':state['migration']['notes']}))
    except (OSError, ValueError, TypeError, AttributeError) as e:
        print(json.dumps({'error':str(e)}))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
