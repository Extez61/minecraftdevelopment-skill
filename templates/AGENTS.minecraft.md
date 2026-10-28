# Minecraft agent routing — merge selectively into AGENTS.md

Do not replace existing repository instructions. This fragment assumes the six skill folders are in `.agents/skills/`; adjust that prefix to the actual installed location, such as `.opencode/skills/`, before use.

For Minecraft work, read `.agents/skills/minecraft-development/SKILL.md`, then the matching platform skill:
- Fabric: `.agents/skills/minecraft-fabric/SKILL.md`
- Paper: `.agents/skills/minecraft-paper/SKILL.md`
- Bukkit/Spigot: `.agents/skills/minecraft-bukkit/SKILL.md`
- NeoForge: `.agents/skills/minecraft-neoforge/SKILL.md`

Load only the relevant referenced files. Inspect exact versions, Java/Kotlin, mappings, build/side and existing behavior before editing. Preserve stable IDs, saved data, commands, permissions, timing and configuration. Prefer the smallest correct patch and measured optimizations. Do not invent APIs or test evidence. Keep state on its owning thread. Do not deploy, delete worlds, upload private data, change permissions or start additional agents without authorization.

If file access is unavailable, ask for the needed source rather than pretending to have read it. The selected model and client must support the required tools; installing this library does not grant them.

For fast lookup, open `minecraft-development/AI-INDEX.md` relative to the actual installed skills root. Use its topic table instead of reading the entire library; retain the core contract and required verification.

For server configuration/optimization, player management, backup/restore or maintenance, select the sibling `minecraft-server-operations/SKILL.md` and only its relevant references. Do not interpret a review request as authorization for live console actions, punishment, downtime or destructive data edits.

Keep user-facing replies short: outcome, essential result/risk, next action only. Omit process diaries and unsolicited implementation comparisons. Never hide failed tests, pending approval/restart or data/security consequences.
