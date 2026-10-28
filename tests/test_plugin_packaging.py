"""Static manifests only; not official CLI validation or live installation."""
from pathlib import Path
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
class PluginPackagingTests(unittest.TestCase):
 def test_minimal_manifest(self):
  p=json.loads((ROOT/'.claude-plugin/plugin.json').read_text())
  self.assertEqual(p['name'],'minecraft-development')
  self.assertEqual(p['author'],{'name':'extez061'})
  self.assertFalse(set(p)&{'hooks','mcpServers','agents','settings'})
 def test_marketplace_root_and_name(self):
  m=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
  self.assertEqual(m['name'],'minecraftdevelopment-skill')
  self.assertEqual(m['plugins'][0]['source'],'./')
  self.assertEqual(m['plugins'][0]['name'],'minecraft-development')
  self.assertEqual(len(list((ROOT/'skills').glob('*/SKILL.md'))),6)
 def test_readme_install_distinctions(self):
  s=(ROOT/'README.md').read_text()
  for phrase in ('Extez61/minecraftdevelopment-skill','must be present in GitHub','/minecraft-development:minecraft-paper','anthropic.claude-code','not** OpenCode','Visual Studio are different'):
   self.assertIn(phrase,s)
