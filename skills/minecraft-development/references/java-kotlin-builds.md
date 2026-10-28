# Java, Kotlin, Gradle and distributable artifacts

## Contents
1. Repository and build discipline
2. Java rules
3. Kotlin rules
4. Platform runtime strategies
5. Mixed-language interop
6. Artifact verification

## 1. Repository and build discipline

Use the existing wrapper (`./gradlew` or `gradlew.bat`) and DSL. Inspect wrapper URL, checksum policy and build instructions. Do not download/run arbitrary remote scripts or silently regenerate the wrapper with an arbitrary system Gradle. Preserve an existing Maven project for a narrow fix; use the matching official Gradle template for a new project unless the user chooses otherwise.

Read `settings.gradle(.kts)`, module builds, properties, version catalogs and dependency locks before editing. Do not print all Gradle properties if they may contain credentials. Keep plugin repositories and dependency repositories distinct; avoid `mavenLocal()` or catch-all repositories without a concrete reason. Prefer trusted official repositories, content filters and existing dependency verification.

Pin released coordinates and tool versions after resolution. A dynamic version or snapshot shown in a tutorial is not a tested release lock. For snapshots, record the actual resolved artifact/build and checksums when reproducibility matters. Do not change every dependency because one method is missing.

Choose Gradle, build plugin, JDK, Kotlin compiler, game, loader and API **as a compatible set**. Avoid “always latest” wrapper commands in an established repository. The official Fabric article's recommended versions are dated examples; recheck before scaffolding and do not impose them on older targets.

## 2. Java rules

- Set the toolchain explicitly for the target; use `--release` where needed to constrain standard-library APIs and bytecode.
- Prefer final fields, immutable records for simple values, narrow visibility and explicit ownership.
- Use sealed types only where a closed set genuinely improves a domain model.
- Avoid parallel streams, mutable static world state, reflection in hot paths and hidden blocking in constructors.
- Keep Minecraft/framework types out of pure domain logic when a real testing or multi-platform boundary benefits.
- Treat exceptions as errors with context; do not swallow persistence failures or catch every `Throwable`.

Use try-with-resources for resources your code actually owns. A platform-owned stream or executor may have different lifecycle rules; check before closing it. Do not allocate a thread per player or block entity.

## 3. Kotlin rules

Kotlin source (`src/main/kotlin`) and Gradle Kotlin DSL (`build.gradle.kts`) are independent choices. A Java plugin can use Kotlin DSL; a Kotlin mod can use Groovy DSL. Do not infer the game source language from the build filename.

### Nullability and JVM boundaries

Java platform types are not guaranteed non-null. Validate lookups, registry resolution, commands, world/player presence and optional integrations at the correct boundary. Use `requireNotNull` only for a startup invariant with a precise error; prefer graceful absence handling for runtime disconnects. Do not scatter `!!` to silence uncertainty.

Kotlin `List` is read-only through that reference, not necessarily deeply immutable. Copy nested mutable state when sending snapshots across threads. `data class.copy()` is shallow. Never reuse a mutable `ItemStack`, collection, NBT object or component payload across owners without the API's required copy semantics.

Keep equality/hash contracts stable: a mutable data class used as a map key can become unreachable after mutation. UUID/resource keys and immutable IDs are safer long-lived keys.

### Lifecycle and coroutines

Coroutines are optional, not the default solution to every async need. Preserve an existing correct executor/future approach for a narrow task.

If coroutines are justified:
- Own a scope with a cancellable job under plugin/server/client lifecycle, not `GlobalScope`.
- Distinguish CPU (`Default`) from blocking I/O (`IO` or a deliberately bounded dispatcher).
- **Neither dispatcher is a Minecraft main thread or a Folia region dispatcher.** Bridge through a verified platform scheduler before touching live state.
- Bound queues and concurrency. A scope can still launch unbounded work and exhaust a database pool.
- Propagate cancellation; rethrow `CancellationException`. Avoid a broad `runCatching`/`catch` that turns cancellation into success.
- Validate session/generation and owner after every suspension before applying a result.
- Cancel owned work on stop/disable, with a bounded flush policy for important writes.
- Do not call `runBlocking` on the tick/render thread. Do not block shutdown waiting for work that itself needs the stopped game thread.

### Performance and readability

Use ordinary loops in profiled hot paths when they reduce allocations clearly. `asSequence()` is not always faster; lambdas, boxing and intermediate collections have context-dependent cost. An inline/value class can box at generics or reflection boundaries. Do not rewrite readable Kotlin into obscure low-level code without measurement.

Avoid eager singleton initialization that touches registries, clients or server worlds too early. An `object` persists for a classloader lifetime, not automatically for a single world session.

## 4. Platform runtime strategies

| Platform | Kotlin runtime/entrypoint policy |
| --- | --- |
| Fabric | Use a matching Fabric Language Kotlin release when adopting its language adapter. Configure `adapter: kotlin` and declare the metadata dependency when needed. Match dependency configurations to the Loom era. Do not bundle conflicting duplicate stdlib/coroutines copies blindly. |
| Paper/Bukkit | The server does not inherently supply your chosen Kotlin runtime. Choose a verified shading strategy or supported dependency loading mechanism. The `JavaPlugin` entrypoint should be an instantiable class, not a Kotlin singleton `object`. |
| NeoForge | Choose a target-version-supported Kotlin language provider/library strategy; confirm loader coordinates and descriptor. A provider release for 1.21.1 does not automatically support 26.2. A Java bootstrap with Kotlin internals is also possible when runtime libraries are intentionally provided. |

Fabric Language Kotlin's own README documents adapter syntax and bundled libraries. Match the Kotlin Gradle plugin and runtime set; do not copy the latest README version into a historical target without verification.

Kotlin for Forge has separate version lines and loader variants; despite its name, some variants support NeoForge. Verify its matching branch/file metadata and target NeoForge requirements. Do not add a Forge-only artifact to a NeoForge project or hardcode `modLoader="kotlinforforge"` while omitting the provider.

For plugins, document whether consumers need a separate runtime dependency. Shade ordinary implementation libraries only when appropriate. Do not shade Minecraft, Bukkit, Spigot, Paper, Fabric Loader/API, or NeoForge. Do not mechanically relocate `kotlin.*`: metadata, reflection, public signatures and integrations need testing. Preserve required service descriptors and reflection/serializer resources when shading; minimization can remove reflectively reached classes.

## 5. Mixed-language interop

Keep Java/Kotlin compiler targets consistent and inspect task dependencies in mixed source sets. Avoid a circular compile-order dependency between generated Java and Kotlin processors.

Use `@JvmStatic`, `@JvmField`, `@JvmOverloads` or `@JvmName` deliberately at real Java/loader boundaries, not globally. Framework reflection may need a static JVM method, not an instance method on a companion. Kotlin default constructor arguments are not a universal replacement for a framework-required constructor. Prefer explicit registration when annotation/static discovery is unclear.

Mixins are often safer as small Java classes even in Kotlin-heavy projects: verify generated JVM members, companion placement, synthetic methods and constructor behavior before writing Kotlin Mixins. Do not insist on one language for technical glue at the cost of reliability.

When using serialization/compiler plugins, match plugin versions and verify generated artifacts. Do not introduce KSP/kapt merely for a small data object. Test public extension APIs from Java when compatibility matters.

## 6. Artifact verification

1. Build the correct distribution task for the actual platform/version, not a guessed `remapJar`/`reobfJar` task.
2. Inspect `build/libs` (or Maven output) and identify development, sources, plain, shaded and production artifacts.
3. Inspect JAR entries and descriptor expansion; reject literal unresolved `${version}` placeholders.
4. Confirm entrypoint names, mod/plugin IDs, mixin config, access wideners/class tweakers, generated data and service files exist where needed.
5. Confirm no server/API classes, secrets, logs, world saves or credentials were bundled.
6. Inspect dependency/runtime inclusion and duplicate files; validate licenses and notices as applicable.
7. Test installation from the packaged production JAR in a clean target runtime, not only an IDE launch.

Useful commands after reviewing the repository: `./gradlew tasks --all`, `./gradlew :module:test`, `./gradlew :module:build`, `jar tf <artifact>`, `javap -verbose <class>`. Do not claim these ran unless they actually did.

Sources: [Fabric Kotlin](https://github.com/FabricMC/fabric-language-kotlin), [Kotlin for Forge](https://github.com/thedarkcolour/KotlinForForge), [Kotlin JVM Gradle](https://kotlinlang.org/docs/gradle-configure-project.html), [Paper setup](https://docs.papermc.io/paper/dev/project-setup/).

## Optional closed-source protection

For owner-authorized protected artifacts, use [closed-source protection](closed-source-protection.md). Keep runtime entry points, reflection/Kotlin metadata and final-artifact tests intact; do not insert unverified transforms into an existing shade/remap/sign pipeline.
