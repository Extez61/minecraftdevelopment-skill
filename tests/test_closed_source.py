"""Static protection guidance checks, not a tested obfuscator configuration."""
from pathlib import Path
import unittest
R=Path(__file__).resolve().parents[1]
P=R/'skills/minecraft-development/references/closed-source-protection.md'
class ClosedSourceTests(unittest.TestCase):
 def test_routes(self):
  for name in ('minecraft-development','minecraft-paper','minecraft-bukkit'):
   self.assertIn('closed-source-protection.md',(R/'skills'/name/'SKILL.md').read_text())
 def test_limits_and_performance(self):
  s=P.read_text()
  for x in ('cannot be made permanently secret','no free/zero-overhead protection claim'.capitalize(),'p95/p99','Do not add prompt-injection','No obfuscator','Do not upload closed-source'):
   self.assertIn(x,s)
 def test_compatibility_contracts(self):
  s=P.read_text()
  for x in ('keepnames','plugin.yml','kotlin.Metadata','permission nodes','mapping files','Java 25','final output','JIT'):
   self.assertIn(x,s)
 def test_conservative_template(self):
  s=(R/'templates/closed-source-proguard.pro').read_text()
  self.assertIn('-dontshrink',s);self.assertIn('-dontoptimize',s)
  self.assertIn('-keep class com.example.plugin.ExamplePlugin',s)
  self.assertNotIn('\n-ignorewarnings',s)
  self.assertNotIn('\n-dontwarn',s)
  self.assertTrue((R/'templates/closed-source-release-checklist.md').is_file())
