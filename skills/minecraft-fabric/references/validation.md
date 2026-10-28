# Fabric validation and troubleshooting

## Minimum evidence

Inspect actual tasks, then run relevant unit tests, datagen when resources changed and the correct distribution task. State the actual command; a proposed command is not execution evidence. Verify the production JAR's descriptor, classes, mixin configuration, runtime dependencies and generated resource paths.

For a shared mod, launch a dedicated server without client classes and a separate client with the packaged artifact. Connect, open the feature, save, restart and reconnect. For a client-only mod, verify the declared environment and required rendering/input behavior. For a server-only mod, verify whether vanilla clients are actually supported by its content/network choices.

## Regressions to include

- Required dependency missing, optional dependency absent/present.
- Registry ID stability and old-save loading on a copy.
- Recipes, loot, tags, models, textures and language fallback.
- Initial and delta sync; late join, tracking, dimension changes, disconnect/reconnect.
- Inventory quick move, crafting remainder, full storage and duplicate requests.
- Resource/data reload and cache invalidation where advertised.
- Integrated server stop/start within one client process.
- Client/server thread ownership; stale callbacks after logout/world unload.
- Mixin success and expected behavior in a production artifact, not only a dev launch.

## Diagnose errors by layer

**Dependency resolution:** check repositories, exact coordinates, compatible Loom/Gradle/JDK set and offline/cache state. Do not refresh everything repeatedly or copy a newer project's coordinates.

**Mapping error:** verify namespace, target era and source names. On 26.1+, check non-remapping configuration and Fabric API renames; on 1.21.x preserve required remapping.

**Loader/entrypoint failure:** check expanded descriptor, class name, Kotlin adapter/runtime, environment and constructor/entrypoint form.

**Mixin error:** inspect earliest cause, target descriptor, actual matching instructions, mapping/remapping and loaded mod combinations. Do not hide an essential failed injection.

**Resource error:** check exact versioned paths/schema, identifiers, generated resource inclusion and pack metadata. JSON parsing success is not semantic validity.

**Desync/duplication:** check logical sides, authority, protocol registration, callback thread and session validation before adding random delays.

**Lag:** follow the shared profiling loop. Identify server vs client and generation vs steady state; do not assume Mixins are automatically faster than API events.

## Reporting

List exact MC/Loader/Fabric API/Loom/JDK/Kotlin/mappings and distribution artifact, then checks actually run. Mark unavailable checks. Never claim a single tested 1.21.1 mod supports every patch through 26.2.
