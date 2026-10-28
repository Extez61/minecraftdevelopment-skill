# Fabric bootstrap, build eras and Kotlin

## Establish the project from evidence

Use the official Fabric template generator or example repository branch for the exact game version. For an existing repository preserve its source organization, DSL and integration strategy. Confirm optional choices: client-only/common/server-only, split client source sets, Kotlin, datagen and tests.

Read the complete build relationship: settings/plugin management, wrapper, version catalog, properties, source sets, Loom configuration, dependency scopes, Java/Kotlin targets and resource expansion. Pin a known compatible set rather than collecting newest version numbers independently.

## Descriptor consistency

`fabric.mod.json` is a contract. Check `schemaVersion`, ID, version, environment, entrypoints, mixins, access declarations, dependencies and provided/conflicting mods where used. Keep `id` stable and legal. The Java package and display name are not the registry namespace by accident; establish intentional identity.

Declare runtime requirements actually used. Compile-time access to Fabric API or Kotlin classes does not prove those libraries exist in a user's instance. Do not mark a required dependency optional simply to bypass a load error. Match dependency range semantics to Fabric Loader; do not use Maven range syntax where it does not belong.

Common `main`, `client` and server-specific entrypoints have different purposes. Do not register a client renderer in a shared initializer, or initialize shared gameplay only in an integrated client. Only use the dedicated-server entrypoint for genuinely dedicated-only behavior; shared server logic must also work in integrated servers.

## 1.21.x remapping era

Select mappings from the actual project. Yarn names in one version are not Mojang names in another. Match Loom's mod-aware dependency configurations and remapping/jar-in-jar rules for the chosen release. Inspect the produced mod JAR and runtime dependencies; ordinary shading of mods can break metadata/loader discovery.

Do not delete mapping/remapping configuration because a newer article says it is unnecessary. That instruction applies to unobfuscated releases, not the old target. Do not add Parchment or a different namespace merely to match a copied snippet.

## 26.1–26.2 unobfuscated era

Fabric's 26.1 release guidance identifies `net.fabricmc.fabric-loom` as the non-remapping plugin and switches old mod dependency scopes to standard scopes and `remapJar` to `jar`. Use the exact-version official template to confirm the current arrangement. Verify publication and nested dependency behavior rather than assuming old task names still exist.

Fabric's 26.2 article recommended Loom 1.17, Gradle 9.5.1 and Loader 0.19.3 **at publication time**. These are historical source facts, not an instruction to force those versions in every repository. Recheck compatibility/security fixes and lock the resolved release set.

Unobfuscation does not remove API changes, side constraints, Mixins, binary compatibility issues or licensing obligations. Do not describe Minecraft as open source merely because names are readable.

## Kotlin path

Use the generator's Kotlin option or inspect Fabric Language Kotlin's README. Configure the Kotlin Gradle plugin, JVM target/toolchain and a matching Fabric Language Kotlin dependency deliberately. If the entrypoint uses `adapter: "kotlin"`, declare its runtime dependency in the descriptor.

The adapter supports Kotlin entrypoint forms, including objects, as documented. Do not transfer that assumption to Bukkit's `JavaPlugin` loader. Keep client Kotlin objects out of common static initialization; class references in singleton properties can trigger early loading.

Avoid bundling duplicate stdlib/coroutines libraries already provided by the selected adapter without understanding runtime resolution. Match `implementation` versus older `modImplementation` to the Loom era. A dependency version shown in the current README may not match a 1.21.1 project.

For mapping migration, Fabric explicitly notes Loom migration does not support Kotlin; its documented alternative tool supports Kotlin. Review generated names, references, mixin targets and code semantics after tooling runs. Never call a find/replace across Yarn names a verified migration.

## Bootstrap validation

Check that:
- version placeholders are expanded in the packaged descriptor;
- exact entrypoint classes exist and implement the expected interface or supported adapter form;
- source sets enforce client/server separation;
- mixin JSON and access declarations point to real packaged files;
- generated resources are included once;
- runtime dependencies are installed/nested correctly;
- dedicated server and client both reach startup where advertised.

Do not publish a development or sources JAR. Do not accept an EULA, download a runtime or install the artifact into a live instance without authorization.
