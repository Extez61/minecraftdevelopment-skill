"""Offline mod metadata tests; no installation/downloading code."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('mods_inspector',ROOT/'skills/minecraft-development/scripts/inspect_mods.py')
mods=importlib.util.module_from_spec(spec);spec.loader.exec_module(mods)

class ModListTests(unittest.TestCase):
    def setUp(self):self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
    def tearDown(self):self.temp.cleanup()
    def jar(self,name,entries):
        p=self.root/name
        with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED) as z:
            for k,v in entries.items():z.writestr(k,json.dumps(v) if isinstance(v,dict) else v)
        return p
    def fabric(self,name,ident,**kw):return self.jar(name,{'fabric.mod.json':{'schemaVersion':1,'id':ident,'version':'1.0.0',**kw}})
    def test_fabric_dependencies_and_side(self):
        self.fabric('a.jar','a',environment='client',depends={'lib':'>=2','minecraft':'1.21.1'},jars=[{'file':'nested/lib.jar'}])
        r=mods.inventory(self.root,'server')
        self.assertEqual(r['jars'][0]['embedded_jars_not_inspected'],['nested/lib.jar'])
        self.assertEqual(r['required_ids_not_observed'][0]['id'],'lib')
        self.assertEqual(r['side_mismatch_candidates'][0]['id'],'a')
    def test_alias_satisfies_observed_identity_only(self):
        self.fabric('a.jar','a',depends={'alias':'>=100'})
        self.fabric('b.jar','b',provides=['alias'])
        r=mods.inventory(self.root)
        self.assertEqual(r['required_ids_not_observed'],[])
        self.assertEqual(r['jars'][0]['dependencies'][0]['constraint'],'>=100')
        self.assertTrue(any('version resolver' in x for x in r['limits']))
    def test_duplicate_ids(self):
        self.fabric('a.jar','same');self.fabric('b.jar','same')
        self.assertEqual(mods.inventory(self.root)['duplicate_ids_across_files']['same'],['a.jar','b.jar'])
    def test_conflict_is_candidate(self):
        self.fabric('a.jar','a',breaks={'b':'<1'});self.fabric('b.jar','b')
        r=mods.inventory(self.root);self.assertIn('not evaluated',r['declared_conflict_candidates'][0]['status'])
    def test_neoforge_multimod_and_manifest_version(self):
        text='''modLoader="javafml"
loaderVersion="[1,)"
[[mods]]
modId="first"
version="${file.jarVersion}"
[[mods]]
modId="second"
version="2.0"
[[dependencies.first]]
modId="lib"
type="required"
versionRange="[1,2)"
side="CLIENT"
'''
        self.jar('neo.jar',{'META-INF/neoforge.mods.toml':text,'META-INF/MANIFEST.MF':'Manifest-Version: 1.0\nImplementation-Version: 3.0\n'})
        r=mods.inventory(self.root,'server');self.assertEqual(len(r['jars'][0]['mods']),2)
        self.assertEqual(r['jars'][0]['mods'][0]['version'],'3.0')
        self.assertEqual(r['required_ids_not_observed'],[])
        self.assertEqual(r['jars'][0]['mods'][0]['environment'],'not-proven-by-descriptor')
    def test_legacy_optional_not_required(self):
        text='''[[mods]]
modId="legacy"
version="1"
[[dependencies.legacy]]
modId="lib"
mandatory=false
'''
        self.jar('old.jar',{'META-INF/mods.toml':text})
        self.assertEqual(mods.inventory(self.root)['required_ids_not_observed'],[])
    def test_jarjar_is_not_recursively_executed(self):
        self.jar('a.jar',{'fabric.mod.json':{'id':'a','version':'1'},'META-INF/jarjar/metadata.json':{'jars':[{'path':'META-INF/jarjar/lib.jar'}]}})
        self.assertEqual(mods.inventory(self.root)['jars'][0]['embedded_jars_not_inspected'],['META-INF/jarjar/lib.jar'])
    def test_malformed_jar_reported_others_continue(self):
        (self.root/'bad.jar').write_bytes(b'notzip');self.fabric('ok.jar','ok')
        r=mods.inventory(self.root);self.assertEqual(len(r['errors']),1);self.assertEqual(len(r['jars']),1)
    def test_duplicate_metadata_refused(self):
        p=self.root/'dup.jar'
        with zipfile.ZipFile(p,'w') as z:
            z.writestr('fabric.mod.json','{}');z.writestr('fabric.mod.json','{}')
        self.assertEqual(len(mods.inventory(self.root)['errors']),1)
    def test_compression_limit(self):
        self.fabric('large.jar','large',description='a'*200000)
        self.assertEqual(len(mods.inventory(self.root)['errors']),1)
    def test_unknown_and_plugin_signals(self):
        self.jar('plugin.jar',{'plugin.yml':'name: Test\n'});self.jar('unknown.jar',{'something.txt':'x'})
        r=mods.inventory(self.root)
        self.assertIn('bukkit-or-paper-plugin:not-a-loader-mod',r['jars'][0]['format_signals'])
        self.assertTrue(r['jars'][1]['warnings'])
    def test_mrpack_no_download(self):
        p=self.jar('pack.mrpack',{'modrinth.index.json':{'formatVersion':1,'game':'minecraft','name':'Test','dependencies':{'minecraft':'1.21.1','fabric-loader':'x'},'files':[{'path':'mods/a.jar','env':{'server':'unsupported'},'hashes':{'sha1':'abc','sha512':'def'},'downloads':['https://private.invalid/token=SECRET']} ]}})
        r=mods.inventory(p);self.assertEqual(r['pack']['format'],'modrinth-index')
        self.assertNotIn('SECRET',json.dumps(r));self.assertEqual(r['pack']['file_references'][0]['download_count'],1)
    def test_curseforge_ids_unresolved(self):
        p=self.root/'manifest.json';p.write_text(json.dumps({'minecraft':{'version':'1.21.1','modLoaders':[{'id':'neoforge-x'}]},'files':[{'projectID':1,'fileID':2,'required':True}]}))
        r=mods.inventory(p);self.assertEqual(r['pack']['file_references'][0]['project_id'],1)
        self.assertIn('not resolved',r['pack']['warning'])
    def test_plain_list_preserved_not_inferred(self):
        p=self.root/'mods.txt';p.write_text('Example Mod 999\nMystery\n')
        r=mods.inventory(p);self.assertEqual(r['rows'],['Example Mod 999','Mystery']);self.assertEqual(r['format'],'unverified-text-list')
    def test_csv_preserved(self):
        p=self.root/'mods.csv';p.write_text('name,version\na,1\n')
        self.assertEqual(mods.inventory(p)['rows'][1],['a','1'])
    def test_readonly_no_extraction(self):
        p=self.fabric('safe.jar','safe');before=p.read_bytes(),p.stat().st_mtime_ns
        self.jar('odd.jar',{'../ESCAPED':'x','fabric.mod.json':{'id':'odd','version':'1'}})
        mods.inventory(self.root)
        self.assertEqual(before,(p.read_bytes(),p.stat().st_mtime_ns));self.assertFalse((self.root.parent/'ESCAPED').exists())
    def test_symlink_input_refused(self):
        p=self.fabric('a.jar','a');s=self.root/'link.jar';s.symlink_to(p)
        with self.assertRaises(ValueError):mods.inventory(s)
    def test_limit_and_unknown_json(self):
        self.fabric('a.jar','a');self.fabric('b.jar','b')
        with self.assertRaises(ValueError):mods.inventory(self.root,max_files=1)
        p=self.root/'other.json';p.write_text('{}')
        with self.assertRaises(ValueError):mods.inventory(p)
    def test_mixed_descriptors_not_false_duplicate(self):
        p=self.jar('multi.jar',{'fabric.mod.json':{'id':'same','version':'1'},'META-INF/neoforge.mods.toml':'[[mods]]\nmodId="same"\nversion="1"'})
        self.assertEqual(mods.inventory(p)['duplicate_ids_across_files'],{})

if __name__=='__main__':unittest.main()
