import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import stylometry as st
from validate_state import read_json, validate
from state_io import save
from migrate_state import migrate
from render_state import render


class StylometryTests(unittest.TestCase):
    def test_quoted_sentence_boundaries(self):
        self.assertEqual(len(st.split_sentences('«Parti.» «Torno.»')), 2)

    def test_abbreviation_and_decimal(self):
        self.assertEqual(len(st.split_sentences('Il dott. Rossi paga 3.14 euro. Torna.')), 2)

    def test_apostrophe_invariance(self):
        a = st.analyze('L’acqua dell’isola.')
        b = st.analyze("L'acqua dell'isola.")
        self.assertEqual(a['metrics'], b['metrics'])

    def test_unicode_composition(self):
        self.assertEqual(st.tokenize_words('caffe\u0300'), st.tokenize_words('caffè'))

    def test_dash_dialogue(self):
        self.assertEqual(st.analyze('— Vieni con me.\n— Resto qui.')['metrics']['dialogue_ratio'], 1)

    def test_long_dialogue(self):
        self.assertEqual(st.analyze('«'+'parola '*1000+'»')['metrics']['dialogue_ratio'], 1)

    def test_nested_quotes_no_double_count(self):
        self.assertEqual(st.analyze('«Disse “vieni qui”, poi uscì.»')['metrics']['dialogue_ratio'], 1)

    def test_dash_closing_attribution(self):
        self.assertLess(st.analyze('— Vieni qui — disse Marco.')['metrics']['dialogue_ratio'], 1)

    def test_repeated_dialogue_in_all_thirds(self):
        text=('«Va bene.» '+'pietra '*60+'.\n')*3
        thirds = st.analyze(text)['pip_hints']['dialogo_per_terzo']
        self.assertTrue(all(0 < x <= 1 for x in thirds), thirds)

    def test_nominal_diagnosis_unavailable(self):
        self.assertIsNone(st.analyze('Partì. Corse. Dormì.')['metrics']['nominal_sentence_ratio'])

    def test_no_translation_diagnosis(self):
        self.assertIsNone(st.analyze('Via. Ora. Corri.')['italian_register']['anglo_translated_flag'])

    def test_mattr_vs_naive(self):
        words = ['a','b','a','c','d','e']*25
        expected=sum(len(set(words[i:i+100]))/100 for i in range(len(words)-99))/(len(words)-99)
        self.assertAlmostEqual(st.mattr(words),expected)

    def test_vocabulary_stability_repeated_windows(self):
        base=' '.join('word'+str(i) for i in range(200))
        a=st.analyze((base+' ')*2);b=st.analyze((base+' ')*10)
        self.assertEqual(a['styledna_quantitative_suggestion']['VOCABULARY_RICHNESS'], b['styledna_quantitative_suggestion']['VOCABULARY_RICHNESS'])

    def test_short_sample_vr_unavailable(self):
        self.assertIsNone(st.analyze('Una frase breve.')['styledna_quantitative_suggestion']['VOCABULARY_RICHNESS'])

    def test_empty_and_unsupported(self):
        for text,lang in [('', 'it'),('...', 'it'),('A sentence.', 'en')]:
            with self.assertRaises(ValueError):st.analyze(text,lang)

    def test_cli_language_rejected(self):
        p=subprocess.run([sys.executable,str(ROOT/'scripts/stylometry.py'),str(ROOT/'references/carta.md'),'--lang','en'],capture_output=True)
        self.assertNotEqual(p.returncode,0)

    def test_cli_text_and_json(self):
        for args in ([],['--json']):
            p=subprocess.run([sys.executable,str(ROOT/'scripts/stylometry.py'),str(ROOT/'references/carta.md'),*args],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr)
            if args:self.assertEqual(json.loads(p.stdout)['analyzer_version'],'7.7.0')


class StateTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        self.s=read_json(ROOT/'examples/minimal/bookforge_state.json')
        self.s['project']['id']='test-project'
        self.target=self.root/'bookforge_state.json'

    def tearDown(self):self.tmp.cleanup()

    def chapter(self):
        self.s['volumes']=[{'id':'v1','title':'One'}]
        (self.root/'chapter.md').write_text('Una scena approvata.\n')
        self.s['files']=[{'id':'file1','path':'chapter.md','sha256':hashlib.sha256((self.root/'chapter.md').read_bytes()).hexdigest(),'role':'chapter','required_for_resume':True}]
        self.s['chapters']=[{'id':'c1','volume_id':'v1','number':1,'title':'Uno','status':'accepted','summary':'Una scena.','file_id':'file1','accepted_ref':'author-message-1'}]

    def test_empty_template_valid(self):self.assertTrue(validate(self.s,self.root)['valid'])

    def test_accepted_missing_file(self):
        self.chapter();(self.root/'chapter.md').unlink()
        self.assertFalse(validate(self.s,self.root)['valid'])

    def test_hash_change(self):
        self.chapter();(self.root/'chapter.md').write_text('Alterato')
        self.assertFalse(validate(self.s,self.root)['valid'])

    def test_accepted_needs_acceptance(self):
        self.chapter();self.s['chapters'][0]['accepted_ref']=None
        self.assertFalse(validate(self.s,self.root)['valid'])

    def test_no_root_declares_partial_validation(self):
        report=validate(self.s)
        self.assertFalse(report['files_checked']);self.assertTrue(report['warnings'])

    def test_traversal_and_symlink(self):
        self.chapter()
        for path in ('../outside','/tmp/outside','C:\\outside'):
            self.s['files'][0]['path']=path
            self.assertFalse(validate(self.s,self.root)['valid'])
        with tempfile.TemporaryDirectory() as elsewhere:
            (self.root/'escape').symlink_to(elsewhere,target_is_directory=True)
            self.s['files'][0]['path']='escape/file.md'
            self.assertFalse(validate(self.s,self.root)['valid'])

    def test_duplicate_ids_and_volume_numbers(self):
        self.chapter();self.s['chapters'].append(copy.deepcopy(self.s['chapters'][0]))
        self.assertFalse(validate(self.s,self.root)['valid'])

    def test_cursor_cross_chapter(self):
        self.chapter();self.s['scenes']=[{'id':'s1','chapter_id':'c1','status':'draft','summary':''}]
        self.s['resume_cursor']['scene_id']='s1'
        self.assertFalse(validate(self.s,self.root)['valid'])

    def test_fact_unknown_knower(self):
        self.s['facts']=[self.fact()];self.s['facts'][0]['known_by']=['ghost']
        self.assertFalse(validate(self.s,self.root)['valid'])

    def fact(self):
        return {'id':'f1','kind':'canon','status':'approved','statement':'The key is red.','source':'author note','source_chapter_id':None,'known_by':[],'reader_knows':False,'approval':'author-1','supersedes':None}

    def test_valid_amendment_and_cycle(self):
        f=self.fact();f['status']='superseded';g=dict(f,id='f2',status='approved',statement='The key is blue.',supersedes='f1',approval='author-2')
        self.s['facts']=[f,g]
        self.assertTrue(validate(self.s,self.root)['valid'])
        f['supersedes']='f2';g['status']='superseded'
        self.assertFalse(validate(self.s,self.root)['valid'])

    def test_promises_resolution_reference(self):
        self.s['promises']=[{'id':'p1','statement':'Who did it?','status':'fulfilled','opened_in':None,'resolved_in':'missing','decision':None}]
        self.assertFalse(validate(self.s,self.root)['valid'])

    def test_duplicate_json_keys_rejected(self):
        p=self.root/'bad.json';p.write_text('{"revision":0,"revision":1}')
        with self.assertRaises(ValueError):read_json(p)

    def test_invalid_types_and_axes(self):
        self.s['revision']=True
        self.assertFalse(validate(self.s)['valid'])
        self.s['revision']=0;self.s['styledna']['axes']['SL']=11
        self.assertFalse(validate(self.s)['valid'])

    def test_save_backup_and_stale_revision(self):
        self.s['revision']=1;save(self.s,self.target,self.root,0)
        next_state=copy.deepcopy(self.s);next_state['revision']=2
        save(next_state,self.target,self.root,1)
        self.assertEqual(read_json(str(self.target)+'.bak')['revision'],1)
        with self.assertRaises(ValueError):save(next_state,self.target,self.root,1)
        self.assertEqual(read_json(self.target)['revision'],2)

    def test_interrupted_commit_preserves_previous(self):
        self.s['revision']=1;save(self.s,self.target,self.root,0)
        next_state=copy.deepcopy(self.s);next_state['revision']=2
        original=os.replace
        def fail_current(src,dst):
            if Path(dst)==self.target:raise OSError('simulated interruption')
            return original(src,dst)
        with patch('state_io.os.replace',side_effect=fail_current):
            with self.assertRaises(OSError):save(next_state,self.target,self.root,1)
        self.assertEqual(read_json(self.target)['revision'],1)
        self.assertEqual(read_json(str(self.target)+'.bak')['revision'],1)
        self.assertFalse(Path(str(self.target)+'.lock').exists())

    def test_cross_project_rejected(self):
        self.s['revision']=1;save(self.s,self.target,self.root,0)
        new=copy.deepcopy(self.s);new['revision']=2;new['project']['id']='another'
        with self.assertRaises(ValueError):save(new,self.target,self.root,1)

    def test_canonical_rewrite_rejected(self):
        self.s['facts']=[self.fact()];self.s['revision']=1;save(self.s,self.target,self.root,0)
        new=copy.deepcopy(self.s);new['revision']=2;new['facts'][0]['statement']='Changed silently'
        with self.assertRaises(ValueError):save(new,self.target,self.root,1)

    def test_accepted_demotion_rejected(self):
        self.chapter();self.s['revision']=1;save(self.s,self.target,self.root,0)
        new=copy.deepcopy(self.s);new['revision']=2;new['chapters'][0]['status']='draft'
        with self.assertRaises(ValueError):save(new,self.target,self.root,1)

    def test_lock_refuses_second_writer(self):
        lock=Path(str(self.target)+'.lock');lock.write_text('other writer')
        self.s['revision']=1
        with self.assertRaises(FileExistsError):save(self.s,self.target,self.root,0)
        self.assertTrue(lock.exists())

    def test_open_promise_cannot_disappear(self):
        self.s['promises']=[{'id':'p1','statement':'Find the key','status':'open','opened_in':None,'resolved_in':None,'decision':None}]
        self.s['revision']=1;save(self.s,self.target,self.root,0)
        new=copy.deepcopy(self.s);new['revision']=2;new['promises']=[]
        with self.assertRaises(ValueError):save(new,self.target,self.root,1)

    def test_migration_preserves_source_and_blocks_activation(self):
        old={'bookforge_version':'7.6','project_meta':{'title':'Legacy'},'custom':{'unknown':['keep']},'continuity_bible_condensed':{'canon_facts_or_didactic':['fact']}}
        original=copy.deepcopy(old);new=migrate(old,'legacy-book')
        self.assertEqual(old,original);self.assertEqual(new['legacy_payload'],original)
        self.assertEqual(new['facts'][0]['status'],'proposed')
        new['revision']=1
        with self.assertRaises(ValueError):save(new,self.target,self.root,0)

    def test_migration_cli_never_overwrites(self):
        source=self.root/'old.json';source.write_text(json.dumps({'bookforge_version':'7.6'}));before=source.read_bytes()
        p=subprocess.run([sys.executable,str(ROOT/'scripts/migrate_state.py'),str(source),'--output',str(source),'--project-id','old-book'],capture_output=True)
        self.assertNotEqual(p.returncode,0);self.assertEqual(source.read_bytes(),before)

    def test_markdown_render_retains_every_field(self):
        result=render(self.s)
        for key in self.s:self.assertIn('## '+key+'\n',result)
        self.assertIn('GENERATED VIEW',result)


if __name__=='__main__':unittest.main()
