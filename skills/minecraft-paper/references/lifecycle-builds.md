# Paper build, descriptors, lifecycle and commands

## Dependency setup

Use the Paper repository and exact compatible API dependency as `compileOnly`, not an embedded server library. Preserve the project's Gradle DSL. Paper changed its artifact version format at 26.1: legacy `MC-R0.1-SNAPSHOT` and modern `MC.build.<build>-<status>` are distinct eras. Resolve a real published coordinate rather than substituting a guessed string.

Use Java 21 for the 1.21.x game line and Java 25 for the 26.1+ game baseline, with compatible Gradle/Kotlin tooling. Do not set Kotlin bytecode or Java release targets inconsistently. For Kotlin runtime distribution, read the shared build guide. Inspect the final shaded/loaded library arrangement and test a clean server without your IDE dependencies.

## Choose a plugin model deliberately

Classic Bukkit-style `plugin.yml` supports ordinary Paper plugins and the conventional `JavaPlugin` lifecycle. `paper-plugin.yml` enables Paper-specific loading/bootstrap features with different rules. They are not interchangeable descriptors, and adding both without design can create confusing ownership/registration behavior.

Do not migrate to the Paper plugin model for a trivial feature. If the project already uses it, preserve its bootstrap/loader architecture and consult matching docs. Do not assume classic descriptor `commands` registration works identically in every Paper-specific model.

For classic descriptors keep name, main, version, API version, commands, aliases, permissions, required/soft dependencies and load order coherent. Quote `api-version` as a string. It is an API baseline/load gate, not a declaration that your plugin supports every later server.

Paper docs allow patch-level `api-version` from 1.20.5 onward. Set the minimum actually required, not the newest number for marketing. Do not extrapolate Paper's descriptor/versioning rules to a Spigot target without checking Spigot.

## Lifecycle

Keep field initializers/constructors lightweight. Do not access a fully running world, services or online player state before the lifecycle permits it. Use `onLoad` only for tasks that belong there; use `onEnable` to validate required configuration/dependencies, build collaborators and register runtime components in an intentional order.

A required initialization failure should disable/fail clearly, not leave partially registered commands/tasks operating with null state. On disable stop accepting work, cancel owned timers, invalidate async callbacks, persist required snapshots and close owned resources safely. Handle partial startup where only some resources were created.

No static plugin singleton should outlive its actual lifecycle or retain a previous classloader. Prefer passing the plugin/scheduler dependency narrowly rather than global access everywhere. Do not allocate a pool/thread for each player or listener.

## Commands

Choose the command mechanism already used: classic executor/tab completer or a verified Paper command/lifecycle API. Match target-version availability and descriptor model.

For classic commands check `getCommand` registration at startup and fail with an actionable message if a declared required command is absent. Do not silently skip registration and report success. Keep permission nodes and usage text synchronized with code.

Validate sender type, argument count, ranges and current state. Enforce permission in execution, not only completion. Tab completion must not leak restricted player/world/administrative information. Avoid expensive disk/DB calls on every completion.

For Brigadier-style commands use the documented target registration point and sender abstraction; do not copy a newer API method into 1.21.1. Preserve aliases, messages and console behavior during migration.

## Optional integrations and services

Required dependencies should have explicit metadata and fail startup clearly if absent. Soft dependency/order declarations help loading but do not guarantee runtime classes are safe to eagerly link. Isolate optional integration classes behind a loader-safe boundary and verify compatible versions/service availability.

For economy/permissions/placeholder APIs follow their contract and lifecycle. Keep implementation classes off shared eager initialization paths. Do not shade another plugin's API/runtime by default. Test optional dependency absent, present, wrong version and disabled unexpectedly where relevant.

## Resources and configuration

Load defaults without overwriting operator changes. Validate config into an immutable snapshot with clear errors. For feature-specific reload, validate all new values before swapping; preserve the old snapshot if invalid. Keep tasks/listeners single-registered and update derived caches intentionally.

Do not read the config file in every event or rebuild components on every scoreboard refresh. Cache validated values with a documented reload boundary, not an unbounded or permanently stale cache.
