# Bukkit/Spigot bootstrap, descriptor and portability

## Build dependency

Resolve the actual published Bukkit/Spigot API and repository for the target. Use `compileOnly`/provided semantics; never shade the server API or a server JAR. Preserve the repository's DSL/build system. A Paper artifact coordinate is not a Spigot coordinate, especially around 26.x version-format changes.

Use exact Java/runtime requirements and compatible Kotlin tooling. The game baseline is Java 21 for 1.21.x and Java 25 from 26.1; confirm the chosen server distribution's requirements separately. Inspect transitive dependency bytecode if targeting a lower plugin bytecode baseline.

For NMS development, do not fetch random server JARs from third-party mirrors. Use lawful official tooling/documented sources with authorization, and preserve licenses. If public API satisfies the feature, avoid internal server dependencies entirely.

## Classic descriptor

In `src/main/resources/plugin.yml`, verify:
- `name`, expanded `version`, fully qualified `main` and intended `api-version`;
- commands, aliases, description and usage matching executors;
- permission nodes, defaults and children matching code;
- required/optional dependencies and load order as actually needed;
- intentional library loading only if supported and tested.

Check exact Spigot version handling for patch-level/new-number API versions; Paper documentation is not conclusive for another server's parser. Do not omit `api-version` just to hide legacy warnings, or set it below the actual required API to force loading.

Do not add `paper-plugin.yml` to a portable artifact as a cosmetic upgrade. Paper-specific bootstrappers/loaders and command lifecycle APIs are separate platform choices.

## Kotlin entrypoint and libraries

The plugin main class must be instantiable by the plugin loader and extend `JavaPlugin`. Use a normal Kotlin `class`, not `object`; do not implement a custom singleton bootstrap unless there is a verified reason. Avoid accessing the server in constructor/field initialization.

Choose a runtime strategy for stdlib and any optional coroutines/serialization libraries: a compatible shading configuration or a verified server library loading feature. Test a clean runtime with only declared dependencies. Compilation success in IntelliJ does not establish distribution correctness.

Do not indiscriminately relocate Kotlin packages or minimize reflective libraries; inspect metadata/service resources and public Java/Kotlin consumers. Use explicit static bridges when reflection/annotation discovery actually requires them.

## Registration

Register listeners exactly once through the platform API. Check command existence and fail clearly at startup when a required descriptor command is missing. Keep executor/completer instances scoped and injected with only needed collaborators.

Use defensive sender handling and explicit permissions. Tab completion is a UX layer, not access control. Keep aliases, argument validation and console behavior stable across refactors. Register service integrations only after checking required dependencies safely.

## Portable boundary

Do not import/link `io.papermc.paper.*`, Paper-only methods on Bukkit types, Paper-provided Adventure convenience methods or Folia scheduler APIs in the portable core without an isolated, independently tested adapter.

A runtime `if (isPaper)` does not automatically prevent classloading of Paper-referencing field/method signatures. Put optional implementation classes behind a safe loading boundary and avoid referencing them eagerly. Add this complexity only if a real optional Paper enhancement is requested.

For text use the baseline API or intentionally provided cross-platform library. Do not assume Adventure/MiniMessage is on every Spigot classpath. Avoid bundling another plugin's runtime to make a missing dependency disappear.
