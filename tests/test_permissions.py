"""Static permission guidance tests; not platform compilation or provider runtime tests."""
from pathlib import Path
import unittest
R=Path(__file__).resolve().parents[1]
P=R/'skills/minecraft-development/references/permissions-authorization.md'
class PermissionGuidanceTests(unittest.TestCase):
 def test_platform_routes(self):
  for name in ('minecraft-development','minecraft-bukkit','minecraft-paper','minecraft-fabric','minecraft-neoforge','minecraft-server-operations'):
   self.assertIn('permissions-authorization.md',(R/'skills'/name/'SKILL.md').read_text())
 def test_enforcement_and_policy(self):
  s=P.read_text()
  for x in ('isPermissionSet','hasPermission','not automatically create a parent/child','Denied actions must have no side effects','Java guard fragment','Kotlin equivalent fragment','Do not substitute','paper-plugin.yml'):
   self.assertIn(x,s)
 def test_mod_and_provider_boundaries(self):
  s=P.read_text()
  for x in ('not built-in Fabric API','NOT a tested 26.2 selection','PermissionGatherEvent.Nodes','QueryOptions','explicit denial','modifyUser','does NOT make all Bukkit'):
   self.assertIn(x,s)
 def test_ops_adaptation_and_command_safety(self):
  s=(R/'skills/minecraft-server-operations/SKILL.md').read_text()
  self.assertIn('Updated operations workflow',s)
  s=(R/'skills/minecraft-server-operations/references/command-runbooks.md').read_text()
  for x in ('not permission to execute','Retries are not always safe','pending restart'):
   self.assertIn(x,s)
  self.assertTrue((R/'templates/permission-contract.md').is_file())
