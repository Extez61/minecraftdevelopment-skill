"""Static server-operation guardrails; not live server tests."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
OPS=ROOT/'skills/minecraft-server-operations'
class OperationsTests(unittest.TestCase):
 def test_skill_registered(self):
  self.assertTrue(OPS.is_dir())
  self.assertEqual(len(list((ROOT/'skills').glob('*/SKILL.md'))),6)
  for skill in (ROOT/'skills').glob('*/SKILL.md'):
   self.assertNotIn('extez061',skill.read_text())
 def test_reference_set(self):
  self.assertEqual({p.stem for p in (OPS/'references').glob('*.md')},{'configuration','performance','player-management','lifecycle','backup-recovery','security-observability','sources','command-runbooks'})
 def test_config_preservation(self):
  s=(OPS/'references/configuration.md').read_text()
  for text in ('bukkit.yml','spigot.yml','paper-world-defaults.yml','overrides','hopper.disable-move-event','restart-required','not universally equivalent'):
   self.assertIn(text,s)
 def test_no_live_action_authorization(self):
  s=(OPS/'SKILL.md').read_text()
  self.assertIn('not permission to execute console commands',s)
  self.assertIn('Do not run broad server commands',s)
  self.assertIn('No production command runner',s)
 def test_backup_and_security_guards(self):
  s=(OPS/'references/backup-recovery.md').read_text()
  self.assertIn('save-all flush alone does not atomically snapshot',s)
  self.assertIn('NEW isolated directory',s)
  self.assertIn('live SQLite copy may miss WAL',s)
  s=(OPS/'references/security-observability.md').read_text()
  self.assertIn('NOT a firewall replacement',s)
  self.assertIn('not evidence of native Bedrock support',s)
 def test_routes_readme_and_templates(self):
  self.assertIn('minecraft-server-operations',(ROOT/'README.md').read_text())
  self.assertIn('minecraft-server-operations',(ROOT/'skills/minecraft-development/AI-INDEX.md').read_text())
  self.assertTrue((ROOT/'templates/server-change-plan.md').is_file())
  self.assertTrue((ROOT/'templates/server-incident-report.md').is_file())
