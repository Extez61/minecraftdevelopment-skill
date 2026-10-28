# Paper compatibility, NMS, profiling and release

## API boundary

Paper-only code can use documented Paper extensions. A Bukkit/Spigot-compatible release must not eagerly reference those extensions; use a real isolated optional adapter only when required and tested. Paper's ability to load many Bukkit plugins does not prove Paper plugins run on Spigot.

Compile a portable public-API plugin against its intended minimum API, then runtime-test actual advertised targets. Method availability, material/entity constants, components and descriptor semantics can vary within 1.21.x. Do not hardcode a universal “1.21 = everything” branch.

## NMS and paperweight

Use public APIs first. If NMS is essential, scope it to exact game/build families and inspect generated sources. `paperweight-userdev` supplies a matching dev bundle and target-specific tooling; it is not a broad compatibility guarantee. Do not add a separate Paper API dependency redundantly when the chosen dev bundle already includes it.

Paper's docs distinguish the 1.20.5–1.21.11 mapping era from 26.1+. In the older era, production mappings/manifest assumptions matter. In 26.1+ the old Spigot reobfuscation route is unsupported because the game is unobfuscated. Do not depend on `reobfJar` for 26.2 just because an old tutorial did.

Do not use CraftBukkit package-version string parsing as a universal version detector. Do not catch linkage errors everywhere to “support all versions.” A small explicit adapter selected at startup is clearer when multiple real families are required. If an unsupported version is detected, fail the dependent feature clearly.

## Performance review

Inspect hot listeners, scheduled loops, full-world/nearby scans, chunk loading, repeated message parsing, inventory refreshes, sync I/O, database pool contention and retained players/worlds. Use spark/JFR where available. Keep the workload and features identical before/after.

A plugin can be CPU-light but cause GC pressure, excessive packets or synchronous disk waits. Measure the relevant layer. Do not remove permission checks, cancel protection integration or reduce game radius/timing and call that an optimization.

## Test ladder

Use pure unit tests for state transitions and repository policies; an existing compatible mock server harness for registration/event-level checks; then a clean Paper runtime from the production JAR. A mock harness cannot prove NMS, mapping behavior, packet semantics or Folia concurrency.

Check startup, commands/console/permissions, event interoperability, menu transfer variants, optional dependencies, join/quit/reconnect, death/respawn, world unload, persistence restart, config failure and disable with I/O in flight. If broad support is promised, include the actual target matrix and exact builds.

## Troubleshooting by cause

- `UnsupportedClassVersionError`: compare runtime JVM and artifact bytecode, including shaded dependencies.
- `NoClassDefFoundError` for Kotlin: inspect runtime distribution/shading/loading and entrypoint references.
- Missing command: inspect descriptor model, declared name and registration; do not silently skip.
- NMS `NoSuchMethodError`: compare exact runtime/API/dev bundle and mapping era.
- Async access exception: find the earliest callback leaving owner context; do not disable the safety check.
- Persistent data disappears: inspect snapshot/commit semantics, key/type stability and save lifecycle.
- “Fixed by reload”: investigate stale tasks/listeners/cache state; restart cleanly to characterize.

## Release gate

Identify the correct packaged artifact, inspect expanded metadata, avoid bundled APIs, document Java/Kotlin runtime requirements and keep actual supported version ranges. Include migration/backups/rollback if data changes. Mark untested Spigot/Folia/version combinations explicitly.

Sources: [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/), [paperweight-userdev](https://docs.papermc.io/paper/dev/userdev/), [plugin.yml](https://docs.papermc.io/paper/dev/plugin-yml/).
