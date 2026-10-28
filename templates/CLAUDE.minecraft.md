# Minecraft repository guidance — merge selectively

This is an optional fragment, not a replacement for existing repository instructions.

- Load `minecraft-development` plus the actual Fabric/Paper/Bukkit/NeoForge skill before platform work.
- Inspect the repository first. Record exact game/platform/dependency, Java/Kotlin, mappings, side and artifact.
- Read relevant references only; do not load every platform or every research file on a small task.
- Preserve behavior, stable IDs, saved data, commands, permissions and configuration unless a change is explicitly requested.
- Prefer the smallest correct patch; avoid unrelated refactors, dependency upgrades and speculative abstractions.
- Verify uncertain/versioned APIs from exact sources; never invent signatures or a universal compatibility range.
- Keep game state on its owning thread. Coroutines and concurrent maps do not make world objects safe.
- Use the repository wrapper and actual production task; keep Java/Kotlin targets/runtime libraries coherent.
- Run the cheapest relevant tests and report what actually ran. Measure before performance claims.
- Do not deploy, accept EULA, erase worlds, reset the worktree, upload private artifacts or introduce hooks without authorization.
- Do not spawn subagents unless the user or governing instructions explicitly allow them.

## Repository facts — fill from evidence

- Minecraft exact version:
- Platform and exact API/loader/server build:
- Language and build DSL:
- Java daemon/compiler/bytecode/runtime:
- Kotlin compiler/runtime/provider, if any:
- Mappings/naming and physical/logical side:
- Build/test/datagen tasks:
- Production artifact:
- Actually tested compatibility matrix:

For fast lookup, open `minecraft-development/AI-INDEX.md` relative to the actual installed skills root. Use its topic table instead of reading the entire library; retain the core contract and required verification.

For server configuration/optimization, player management, backup/restore or maintenance, select the sibling `minecraft-server-operations/SKILL.md` and only its relevant references. Do not interpret a review request as authorization for live console actions, punishment, downtime or destructive data edits.

Keep user-facing replies short: outcome, essential result/risk, next action only. Omit process diaries and unsolicited implementation comparisons. Never hide failed tests, pending approval/restart or data/security consequences.
