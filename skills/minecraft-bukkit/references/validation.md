# Bukkit/Spigot compatibility and validation

## Compatibility is empirical

Compile against the intended minimum API and runtime-test actual Spigot builds. Test on Paper additionally if promised; do not substitute a Paper-only run for Spigot validation. `plugin.yml` acceptance, successful classloading, API availability and correct gameplay are separate gates.

Prefer public APIs. If NMS/CraftBukkit is unavoidable, isolate by exact supported version and inspect matching source/build tooling. Do not parse old package prefixes as a universal 26.x detector or use broad reflection/catch blocks to pretend unsupported methods exist.

Keep a minimal tested matrix for actual release commitments. For a requested broad range, define separate artifacts/adapters when needed and label untested combinations. Do not claim all 1.21.1–26.2 versions merely because a descriptor uses an old API version.

## Build and artifact checks

Run relevant tests and build through the repository wrapper. Inspect the final JAR for expanded `plugin.yml`, main class, required Kotlin/implementation libraries and service resources. Ensure Bukkit/Spigot/Paper classes and server binaries were not bundled.

A clean target server should load the packaged artifact with only documented dependencies. Check startup failure messages for missing required dependencies and degraded behavior for absent optional dependencies.

## Functional checks

Test all commands/aliases from player and console; denied permissions and tab visibility; intended cancellation with another protection/integration plugin; menu transfer routes; profile join/load/quit/reconnect races; persistence across restart; death/respawn; world unload; disable with work in flight; invalid config and supported config reload.

For gameplay plugins verify per-arena isolation, timers, cleanup, temporary entity ownership and reward idempotency. For item plugins verify metadata across stack operations and server restart. For performance changes run the same workload and invariants before and after.

## Truthful evidence

A mock harness can test some registration/events but not actual NMS, packets, chunk loading, classloader differences or network clients. List exact commands/builds and mark unrun checks. Never state a plugin is Folia-safe because it passed a single-threaded mock test.

Do not recommend `/reload`, hot unloading, unsafe async access or disabling runtime checks as the release path. Provide restart instructions, backups and migration/rollback steps when data is affected.
