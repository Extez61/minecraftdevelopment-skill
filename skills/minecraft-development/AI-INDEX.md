# AI quick lookup — do not read the entire library

**Skill creator: extez061**

## Read this first

This is a navigation map, not a substitute for the selected skill's instructions. Paths below are relative to this file and remain valid when all six sibling skill directories are installed. Read the [core contract](SKILL.md) once, then exactly the platform router needed. Open only the task-relevant references. Do not scan every Markdown file, load all platforms or reread unchanged files. If the platform is unclear, inspect project descriptors/build files first; do not guess.

## Pick the platform

| Repository evidence / task | Start here |
| --- | --- |
| Fabric Loader/API/Loom, fabric.mod.json | [Fabric router](../minecraft-fabric/SKILL.md) |
| Paper API / Paper runtime | [Paper router](../minecraft-paper/SKILL.md) |
| Bukkit/Spigot portability | [Bukkit router](../minecraft-bukkit/SKILL.md) |
| Server YAML/properties, players, backups, deployment or live lag | [Operations router](../minecraft-server-operations/SKILL.md) |
| NeoForge / neoforge.mods.toml | [NeoForge router](../minecraft-neoforge/SKILL.md) |

Each platform router maps its own build, gameplay, networking, rendering and validation files. Open that table rather than browsing every platform directory. plugin.yml alone does not distinguish Paper from a portable Bukkit target.

## Find the shared answer

| Need | Read |
| --- | --- |
| Exact version, Java baseline, mappings, 1.21.x versus 26.x | [Version policy](references/version-policy.md) |
| Java/Kotlin, Gradle, dependencies or packaging | [Build/language guide](references/java-kotlin-builds.md) |
| Bug fix, refactor or preserving current behavior | [Preservation](references/behavior-preservation.md) |
| Async, scheduler, lifecycle, persistence | [Concurrency/storage](references/concurrency-persistence.md) |
| CPU, tick lag, allocations, caches or profiling | [Performance](references/performance.md) |
| Anti-cheat, false positives or custom-mechanic compatibility | [Anti-cheat](references/anticheat-development.md) |
| Mod lists, JAR metadata, modpacks or Mod Menu | [Mod lists](references/modlists-compatibility.md) |
| API coverage / where an API belongs | [API catalog](references/api-catalog.md) |
| LuckPerms/Vault/PAPI/WorldGuard/packet libraries/viewers | [Integrations](references/integrations.md) |
| Registries, worldgen, recipes, loot, AI or custom content | [Feature playbooks](references/mod-feature-playbooks.md) |
| Multi-platform modules or gameplay architecture | [Architecture](references/architecture-gameplay.md) |
| Porting versions / saved-data migrations | [Migration](references/migration.md) |
| Add permission nodes, defaults or provider-backed action checks | [Permission engineering](references/permissions-authorization.md) |
| Security, permissions or untrusted network input | [Trust boundaries](references/trust-boundaries.md) |
| Closed-source plugin obfuscation, keep rules or protection/performance trade-offs | [Artifact protection](references/closed-source-protection.md) |
| Tests, artifact inspection or release evidence | [Verification](references/testing-release.md) |
| Caveman / Superpowers / other skill cooperation | [Companion skills](references/companion-skills.md) |
| Token waste, huge logs or repeated context | [Token efficiency](references/token-efficiency.md) |
| Client/IDE discovery and adapters | [Client adapters](references/tool-adapters.md) |
| Authoritative documentation links | [Source index](references/sources.md) — search the relevant heading only |

## Tools and examples

- Inspect project signals: `scripts/inspect_project.py`; read its usage before running. Signals are not verified compatibility.
- Inspect mod metadata/exports: `scripts/inspect_mods.py`; read-only/offline, not a full compatibility solver.
- Package-level templates, validation tools and example files live outside the installed skill folders. Use the original package when needed; do not assume its tools/docs were copied into the project.

## Expand only when evidence requires it

Example: Paper async bug → core → Paper router → concurrency + Paper threading → affected sources/tests. Not Fabric, NeoForge or every integration.

Example: Fabric Mod Menu issue → core → Fabric router → mod-list/integration references → matching client registration/source. No anti-cheat guide unless the issue involves it.

For every code change retain the behavior contract and required verification. Navigation saves reading, not correctness checks. A missing answer warrants targeted source/docs lookup, not invented APIs or an arbitrary reading limit.
