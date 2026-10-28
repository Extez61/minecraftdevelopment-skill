---
name: minecraft-fabric
description: "Build, debug, review, optimize or port Fabric mods in Java or Kotlin for Minecraft 1.21.1 through 26.2. Use for fabric.mod.json, Loom, Fabric API, entrypoints, registries, components, payload networking, rendering, datagen, Mixins, dedicated-server crashes and Yarn-to-official naming migrations. Not for Bukkit or NeoForge APIs."
---

# Fabric Mod Development

**Skill creator: extez061**

For shared topic lookup, use the [AI file map](../minecraft-development/AI-INDEX.md); do not load unrelated platform guides.

Read `../minecraft-development/SKILL.md`, then load only the shared references and Fabric references relevant to the task. Do not assume a Fabric mod is client-only; establish physical and logical sides explicitly.

## Required facts

Inspect `fabric.mod.json`, `settings.gradle(.kts)`, build files, properties, source sets, mixin configurations, access wideners/class tweakers, generated resources and tests. Record exact Minecraft, Loader, Fabric API, Loom, mappings, JDK, Kotlin compiler/runtime, environment and output task.

Determine whether the project uses old remapping Loom or the unobfuscated 26.1+ workflow. Do not paste modern configuration names into a 1.21.1 project or retain old remapping tasks blindly in 26.2.

For worldgen, biomes/dimensions, recipes/loot, entity AI, attributes or effects, also read `../minecraft-development/references/mod-feature-playbooks.md`.

For API-domain/integration lookup, read `../minecraft-development/references/api-catalog.md` and `../minecraft-development/references/integrations.md` as needed. For mod/plugin lists, modpack dependency triage or mod-list/config-screen UI, read `../minecraft-development/references/modlists-compatibility.md`.

## Reference router

| Work | Read |
| --- | --- |
| Transfer/resource conditions/reload and optional extension hooks | [Additional API playbooks](references/transfer-resource-hooks.md) |
| Project setup, Java/Kotlin, entrypoints, build eras | [Bootstrap/builds](references/bootstrap-builds.md) |
| Registries, blocks/items/entities, storage, data/resources | [Content/data](references/content-data.md) |
| Packets, menus, client/server sync, side safety | [Networking/sides](references/networking-sides.md) |
| Renderers, Mixins, access changes, version porting | [Rendering/Mixins](references/rendering-mixins.md) |
| Review, test and troubleshoot | [Validation](references/validation.md) |

For version changes also read the shared version policy and migration procedure. For optimization read shared performance and behavior-preservation references before editing.

## Non-negotiable Fabric rules

1. Prefer a documented Fabric API event/extension point over a Mixin when it covers the actual behavior.
2. Keep client classes and client-only initialization out of common/server classloading paths. Runtime `if` checks are not always enough to prevent linkage.
3. Register content at the right lifecycle point and preserve stable namespaced IDs. Do not call registration “fixed” by changing IDs in a save-sensitive project.
4. Separate persistent data from sync state. Saving a component or attachment does not universally imply network synchronization.
5. Treat the server as authoritative for gameplay. Validate every C2S action on the server even if the UI already checked it.
6. Match codec, registration, direction, connection phase and handling semantics to the exact Fabric API version.
7. Do not touch game state from arbitrary executors/coroutines; verify callback thread guarantees and hand off only when needed.
8. Use Java or Kotlin according to the project; configure Fabric Language Kotlin intentionally when using its adapter.
9. Compile and inspect the **production** artifact; IDE success alone does not prove remapping, nesting or metadata correctness.
10. Never promise one mod JAR spans 1.21.1–26.2 without real evidence; these families include significant API/build changes.

## Workflow

1. Identify a minimal reproducible scenario and the affected logical side.
2. Inspect exact API/source and current registration/resource graph.
3. Make the smallest coherent change to code, descriptor, resources and tests.
4. Run targeted checks, datagen if touched, and the correct build task.
5. Test dedicated server plus client/connection when the feature is common, not just single-player.
6. Review Mixins, state ownership, serialization, late join and cleanup; report precise gaps.

## Stop conditions

Pause and ask a focused question if the platform/side/version cannot be derived and changes the design. If a method or mapping is unverified, identify the unknown rather than inventing an API. If the only way to implement the request appears to require invasive vanilla replacement, explain supported alternatives and conflict risk first.

Sources: [Fabric developer docs](https://docs.fabricmc.net/develop/), [26.1](https://fabricmc.net/2026/03/14/261.html), [26.2](https://fabricmc.net/2026/06/15/262.html), [Fabric Language Kotlin](https://github.com/FabricMC/fabric-language-kotlin).

## Anti-cheat and lean companion workflows

For defensive anti-cheat checks or legitimate gameplay compatibility, read [anti-cheat engineering](../minecraft-development/references/anticheat-development.md); verify this exact platform/product tuple. Apply the core lean context contract; do not preload unrelated platform/reference files. For optional Caveman or other workflow composition, read [companion skills](../minecraft-development/references/companion-skills.md) only when needed.

For node declaration, command/action guards, defaults or permission providers, open [permission engineering](../minecraft-development/references/permissions-authorization.md) only when needed. Match the actual platform/API version and preserve existing access behavior.
