# Version and platform migration procedure

## 1. Establish the baseline

Record source commit/worktree state, exact source and destination targets, API/loader/build tool, Java/Kotlin compiler, mappings, production artifact, dependencies and known working behavior. Build the existing project if possible before changing it. If baseline already fails, separate pre-existing failures from migration failures.

Back up representative saves/configuration and document rollback. Do not open the only original save in a newer version. A newer game may rewrite data in ways the old version cannot read; downgrading a JAR is not a world rollback.

## 2. Inventory migration surfaces

Inspect entrypoints and descriptors; registries/resource IDs; components, NBT, saved data and attachments; payload codecs/direction; command tree; event subscriptions/cancellation; renderers/models/shaders; data/resource packs; mixins/access widening; optional integrations; datagen; build plugins and distribution tasks.

For Kotlin include entrypoint adapters, language provider, stdlib/coroutines, Java interop, Mixins and the mapping tool's Kotlin support. A Java-only migration task cannot be assumed to rewrite Kotlin correctly.

## 3. Plan by meaningful boundaries

Use the release-family table in `version-policy.md`. For a large 1.21.1 → 26.2 jump, read intermediate migration notes to understand semantic changes, but do not create and ship a separate artifact for every patch without need. Decide whether staged compilations help isolate changes or a direct port with grouped commits is cheaper.

Keep categories separate where practical:
1. compatible build/toolchain setup;
2. mappings/names and descriptor changes;
3. API/lifecycle changes;
4. data/resources/codec migrations;
5. rendering/client work;
6. runtime regression and performance verification.

Do not combine a feature redesign with a version port. Preserve gameplay values and public contracts unless a platform restriction requires an explicitly approved change.

## 4. Mappings are not APIs

A name migration can map `Identifier` to a corresponding official-name type in a given context; it does not guarantee unchanged constructors, codecs, registry rules or result semantics. Confirm each changed signature. Unobfuscated source is readable, not a stability guarantee and not an open-source license grant.

For Fabric 26.1+ update build model/configurations and API renames as documented. For Paper 26.1+ remove unsupported legacy reobfuscation assumptions. For NeoForge, use destination-version MDK/Gradle tooling and descriptor semantics; do not mix an old Forge event package into a new NeoForge mod.

## 5. Data and protocol migration

Version persistent schemas explicitly. Write narrow, tested transformations that handle missing fields, malformed values and repeated application safely. Keep stable IDs unless the change demands a registered migration/remap. Test old save → new code → save → restart, and account for old backups.

For network protocols, align registration, direction, phase, codecs and compatible versions on both ends. Fail cleanly for unsupported clients. Do not label a protocol “compatible” merely because a handshake accepts it. Test a late-joining client and resync after dimension changes.

## 6. Resource migration

Regenerate using destination-version providers and inspect the diff. JSON validity is insufficient: paths, identifiers, registry references, model schema, tags, recipes, loot and pack metadata must match the target. Keep generated outputs reproducible and distinguish generated/source directories.

For 1.21.4+ inspect item model definitions; for 1.21.5+ inspect NBT missing-value behavior; for 1.21.6+ inspect block entity serialization views; for 26.2 inspect resource-key-based datagen, GUI/HUD changes and renderer backend abstractions. Verify exact names in the target's mappings.

## 7. Validate and release

Compile both language sources, run unit/regression tests, run datagen, inspect production JARs, launch dedicated server and client where relevant, load an old-save copy, test integrations and compare performance. If one stage cannot run, state that explicitly and provide reproduction commands.

Do not broaden version ranges until the actual matrix supports them. Give operators exact artifact selection, Java/runtime dependencies, backup steps, migration caveats and rollback instructions. A server-plugin target and a client mod target require different release guidance.
