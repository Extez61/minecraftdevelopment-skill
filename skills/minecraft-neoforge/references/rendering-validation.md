# NeoForge rendering, datagen, version ports and verification

## Client rendering

Use the exact target's client registration events and renderer architecture. Entity/block entity renderers, models, shaders and GUI hooks change across the requested interval. Do not paste a Fabric rendering callback into NeoForge or use an old renderer signature because class names look similar.

Respect extraction versus submission/drawing stages where present. Snapshot values under the supported contract; avoid unsafe direct reads of changing world state in stages that consume render state. Own GPU resources and invalidate/rebuild them on appropriate reload/context changes.

26.2's vanilla migration primer describes major changes to GPU bind groups/pipelines, render passes, render types, GUI/HUD organization and registry keys. It is a **vanilla migration guide**, not proof that a particular NeoForge hook exists. Use it to locate changes, then inspect the actual loader build.

For backend-neutral code, use supported game GPU abstractions rather than raw OpenGL assumptions. Test available advertised backends and resource reload; report when Vulkan or compatibility with renderer mods is not tested.

## Datagen and resources

Use target-compatible providers for blockstates/models, item definitions, loot, recipes, tags and language. Inspect generated outputs and include them in the production resources intentionally. Avoid manually editing generated files or shipping duplicate definitions from two source roots.

Check paths and pack metadata by target, not only JSON syntax. For 1.21.4+ item definitions differ from old model-only setups. For 26.2 registry-key/tag-provider changes, follow matching examples instead of applying blind search/replace.

Regenerate on migration and review deleted/renamed IDs carefully. A successful generation task does not prove every resource reference resolves at runtime. Load resources/data packs and exercise actual recipes/models.

## Migration review

For 1.21.1 → 26.2, inventory:
- Java 21 → 25 toolchain/runtime and Kotlin compatibility;
- Gradle/NeoForge plugin and MDK changes;
- event bus/subscriber/parallel setup semantics;
- registry constructors/keys/holders and stable identity;
- component/attachment/capability persistence and sync;
- menu opening and network protocol;
- NBT/serialization views and old-save migration;
- datagen, item models, loot/recipe/tag formats;
- render states, GUI/HUD APIs and GPU lifecycle;
- optional integrations, access transformations and Mixins.

Do not mix a version port with feature removal. Preserve IDs and configs unless there is an explicit migration. Build after small coherent groups; verify semantic changes even if a name migration tool compiles.

## Performance review

Profile block entity tickers, recipe lookup, capability queries, neighbor scans, chunk loads, payload frequency, datagen/startup if relevant, render allocation and retained level/player state. Cache only when invalidation is correct; use supported capability caching rather than retaining stale handlers.

Budget large work without dropping required operations. Dirty flags must cover external inventory edits and reloads. Do not lower machine speed, skip recipes or drop output as a “performance optimization.” Preserve simulation/execute semantics and test partial transfer/rollback.

## Verification ladder

Use unit tests for pure rules, codecs/schema transforms and state transitions. Use an existing loader-supported GameTest setup when available and verify actual task names. Run datagen and compile both Java/Kotlin; inspect production JAR descriptor, classes, client separation, generated resources, access/mixin files and runtime Kotlin/provider dependencies.

Launch a clean dedicated server and separate client with the packaged mod. Test connect, content registration, interaction, menu sync, late join, death/respawn, dimension travel, old-save copy, restart, resource reload and graceful shutdown. Test optional dependency absent/present and declared client/server requirements.

A unit test cannot prove loader discovery or renderer correctness. An integrated run cannot prove dedicated-server classloading. A current-version online doc may not describe the selected loader patch.

## Troubleshooting

- Registry/deferred access failure: inspect initialization order and early dereference, not just null handling.
- Event not firing: inspect exact event bus, side, static/discovery requirements and duplicate registration.
- Language provider missing: inspect correct loader variant, descriptor and installed provider, not only stdlib presence.
- Lost state: inspect dirty marking, codec/default behavior, clone/death rules and correct authoritative holder.
- Duplication: inspect server authority, repeated events/packets, simulation mutation and transaction ownership.
- Server crash from client class: inspect common static initialization and subscriber classloading.

Report exact version/build, artifact, executed checks, untested matrix and remaining migration risks. Do not advertise every intermediate version based on two endpoint builds.

Source: [26.2 vanilla migration primer](https://docs.neoforged.net/primer/docs/26.2/) and versioned NeoForge documentation.
