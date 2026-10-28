# Research notes and source coverage

Research checked **2026-10-28** against official/project-maintainer sources. The complete annotated ledger is [the shared source index](skills/minecraft-development/references/sources.md).

## What was researched

- Claude Code skill discovery, directory layout, frontmatter and supporting-file guidance.
- Fabric release changes at 1.21/1.21.1, 1.21.2/3, 1.21.4, 1.21.5, 1.21.6/7/8, 1.21.9/10, 1.21.11, 26.1 and 26.2.
- Fabric's Java 25/non-remapping boundary, API renames, Kotlin mapping migration limitation and typed networking.
- Paper dependency/version format, descriptor/API baseline, mapping/reobfuscation eras and Folia ownership.
- Bukkit scheduler restrictions and inventory transaction Javadoc.
- NeoForge event buses/parallel lifecycle, patch-sensitive event registration, components, attachments, capabilities, payload threads and the vanilla 26.2 primer.
- Fabric Language Kotlin and Kotlin for Forge provider/runtime integration. No universal adapter/compiler version was inferred.

## Deliberate safeguards

Current documentation is often newer than the requested target. The skill instructs the coding agent to inspect exact resolved sources and compile the touched module. A link or a successful metadata range is not compatibility evidence. One binary is not promised for this entire scope.

The package contains **procedures, engineering constraints and version-aware reference material**, not a copied encyclopedia or a prevalidated SDK. Version-sensitive code snippets are intentionally limited; a large collection of uncompiled pseudo-universal APIs would make the agent less reliable, not more knowledgeable.

## Evidence levels

1. Official dated release notes for known migration boundaries.
2. Official versioned docs for version-scoped concepts and semantics.
3. Project-maintainer READMEs for Kotlin adapters/providers.
4. Exact resolved artifacts/source/Javadocs at implementation time for signatures.
5. Actual compile/runtime/migration/performance tests for product claims.

This packaging task provides levels 1–3 research and a workflow requiring levels 4–5 before claims. It does not claim to have executed a complete four-platform, every-version runtime matrix.

## Licensing and attribution

Guidance is original synthesis. Upstream links remain attributed in the source index; upstream code, game assets, server binaries, full documentation and third-party skills are not vendored. Check upstream licenses when adapting actual code. Unobfuscated Minecraft does not imply permission to redistribute the game or call it open source.

## Multi-tool update

Official Claude Code setup/skills, OpenCode V1/V2 install/skills, Cursor skills, Copilot skill locations/surface support, Codex skills, Gemini CLI skills and JetBrains AI Assistant project rules were additionally checked on 2026-10-28. The new installation guide separates native support from manual adapters, and application installation from local skill copying. Commands describe current upstream methods, not end-to-end installations executed here. See the added client sources in the shared source index.

## Link-first installation and API/mod-list update

The user clarified that “install from a link” means installing the skill library, not the Claude Code application. Root INSTALL.md now defines that agent workflow, using existing authorized Git access, native plugin installation or normal file copying. No Python install/download helpers are included.

API-domain coverage was reviewed against the official platform indexes and expanded with transfer/resource/config/registry/UI playbooks and maintained optional integration lookup points. Mod Menu, runtime mod enumeration, offline Fabric/NeoForge metadata and Modrinth pack formats were checked. Exact dependency/API/runtime compatibility is still verified at implementation time; no all-APIs/all-versions guarantee is made.

The offline inspector preserves raw constraints and labels unresolved dependencies/conflicts as candidates. It does not execute JARs, recursively resolve nested libraries, download mods, call CurseForge APIs, evaluate every version expression or certify runtime compatibility. Project IDs in exports and unstructured text remain unverified evidence.

## Anti-cheat and companion update

Reviewed upstream READMEs and the Caveman voice SKILL.md on 2026-10-28: Caveman, Superpowers, Matt Pocock skills, Context7, Grim/GrimAPI and legacy NoCheatPlus. These are documentation observations, not executed integrations. Current README examples can differ from an installed release; exact-version verification remains mandatory. No upstream token-saving metric is adopted as this package's result. No skill/CLI/proxy/hook or anti-cheat runtime was installed.

## GitHub README / Claude plugin packaging

Reviewed official Claude Code setup, plugin manifest/marketplace references, VS Code extension and OpenCode V1 documentation on 2026-10-28. Added a root-source marketplace and minimal hook-free plugin manifest. npm application commands are not a published npm distribution of this suite. JSON/path checks do not replace claude plugin validate or a live install; neither was run here.

## Server operations expansion

Added a sixth skill with seven on-demand operations references after reviewing official Paper config/properties/world settings, profiling/update/Java pages; spark commands; Velocity security; LuckPerms usage; and NeoForge server install docs. See the new operations source ledger for exact URLs and evidence limits. Fabric server-install extraction failed twice and no newly verified install command is asserted. No live server/player action or performance/restore experiment was performed.

## Updated operations adaptation and permission engineering

Adapted the practical scope of the user-referenced minecraft-server-ops into the existing sixth skill, retaining reviewed current config/profile/backup/player/security guidance rather than copying legacy presets/hot-reload assumptions. Added safe operational command planning and a shared permission-engineering reference after reviewing official Paper classic descriptor/1.21.1 API, LuckPerms API/usage, Fabric Permissions API maintainer usage and NeoForge 1.21.1 upstream sources. No Notion skill page was modified. Exact retrieval limits are recorded in the shared source ledger.

## Owned closed-source plugin protection

Reviewed Guardsquare ProGuard usage/Kotlin metadata, Zelix advertised protection features and Paper descriptor contracts. Added an on-demand defensive IP-protection workflow and conservative configuration/checklist fragments. No obfuscator or decompiler was executed, and no product/JVM compatibility, benchmark or AI-resistance guarantee is asserted.
