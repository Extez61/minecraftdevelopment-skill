# NeoForge tooling, metadata, event buses and Kotlin

## Tooling

Start from the official Mod Generator/MDK for the exact game/NeoForge version. Choose ModDevGradle or NeoGradle intentionally; preserve an existing project choice. A build example for one plugin cannot be copied piecemeal into the other's DSL.

Read wrapper, Gradle plugin, Java toolchain, run configurations, source sets, dependency handling and distribution tasks. Keep Minecraft/NeoForge versions aligned. Resolve actual versions; do not derive every new loader coordinate from a guessed game-version formula.

Use the correct game Java baseline: 21 for 1.21.x, 25 for 26.1+. Confirm build plugin/Gradle/Kotlin compatibility. Keep the Gradle daemon JDK, compiler target and runtime distinct. Use official generated/patched sources for API verification.

## Descriptor and entrypoint

Inspect the target's `META-INF/neoforge.mods.toml` schema, language loader, loader range, mod ID/version, dependencies and side/order declarations. Preserve resource expansion and manifest/version conventions from the matching template. Do not paste legacy `mods.toml`/Forge metadata without checking the NeoForge target.

The entrypoint's mod ID must match declared identity and registrations. Use the supported `@Mod` constructor/injection form for the exact loader; do not assume one constructor signature spans every patch. Keep static initializers free of premature registry access and client-only linkage.

Validate required dependencies clearly. Isolate optional integrations behind safe loading boundaries; a dependency flag does not make an absent class available. Do not hide a required integration failure with empty defaults.

## Two event buses, version-sensitive registration

NeoForge exposes a game bus and a per-mod bus. Setup/registration/lifecycle events and gameplay events may use different buses and threading guarantees. Read event interfaces and exact-version docs rather than guessing by event name.

The versioned 1.21.1 events page itself distinguishes behavior for older loader builds (`21.1.0–21.1.180`) from later builds. Therefore “Minecraft 1.21.1” alone is not sufficient for all event-subscriber details. Inspect the actual NeoForge artifact and match annotation/registration semantics.

For explicit listeners, attach to the correct bus exactly once. For subscriber annotations, verify static requirements, environment filtering, bus selection/automatic routing and loader-version behavior. Do not register the same class manually and automatically unless intentionally handling distinct subscriptions.

Many lifecycle events run in parallel. Use the documented enqueue/deferred-work facility when non-thread-safe setup must occur on the proper thread. Event priority does not make parallel lifecycle mutation safe. For gameplay events check cancellation/results and actual thread, not merely “it's the game bus.”

## Kotlin paths

Support Kotlin without assuming a Java-shaped loader can instantiate every Kotlin declaration. Choose one verified strategy:
1. target-supported Kotlin language provider and matching runtime libraries;
2. a loader-compatible Java or Kotlin class bootstrap with Kotlin internals and intentional runtime library distribution.

Kotlin for Forge offers variants/branches that can support NeoForge; verify target file metadata and actual coordinates. Do not use a Forge variant in NeoForge or a 1.21.1 provider release as proof of 26.2 support. Other providers need the same exact-version checks.

Descriptor `modLoader`, loader dependency/range and provider installation must agree. Installing a library JAR that lacks the required language provider is not equivalent to installing a matching provider. Do not switch language loaders in metadata as an error-suppression trick.

For annotation-discovered static handlers, inspect compiled JVM methods. Companion methods may need static bridges; explicit listener registration is often clearer. Use small Java glue for Mixins or reflection-sensitive entrypoints if it is the simpler reliable option.

## Lifecycle validation

Test correct registration, no duplicate listener invocation, required dependency failure, absent optional integration, dedicated-server startup and client startup. Test integrated server stop/start because process-lifetime singleton state can otherwise leak between worlds.

Sources: [NeoForge getting started](https://docs.neoforged.net/docs/gettingstarted/), [1.21.1 events](https://docs.neoforged.net/docs/1.21.1/concepts/events/), [KotlinForForge](https://github.com/thedarkcolour/KotlinForForge).
