# Fabric content, registries, storage and resource data

## Registries and identity

Use stable lower-case namespaced IDs; register once in a deterministic appropriate initialization phase. Initialize related registrations in an intentional order without relying on accidental class initialization. Confirm whether a registry is static, dynamic/data-driven or reloadable and which thread/lifecycle it permits.

When constructors/settings require a registry/resource key in a target release, supply the key at the documented point. Do not paste pre-1.21.2 settings patterns into later versions without checking. Avoid reading a deferred/dynamic registry entry before it exists.

Preserve identifiers across updates. Removing/renaming a block, item, entity or component can orphan world data. A display-name change is not a reason to change the registry ID. If an ID truly must change, plan supported remapping/data migration and old-save tests.

For 26.2, examine separate vanilla ID/key collections (`BlockIds`, `BlockItemIds`, `ItemIds`) and resource-key-based datagen. The official article describes removal of `valueLookupBuilder`; do not patch that missing method with an invented replacement. Regenerate from target-version provider examples.

## Blocks and block entities

Keep block state properties small and purposeful: each independent property multiplies possible states. Use a block entity for richer state when appropriate, not dozens of booleans in block states. Register the block item intentionally if players need an inventory representation.

A ticker should be absent or return early when no work is needed. Separate client effects from server-authoritative processing. Mark dirty/save state when persistent data changes according to exact API semantics; sync only necessary client state. Do not serialize a full block entity every tick to update one progress value.

When a block is removed/replaced, preserve expected inventory drops, comparator updates and cleanup. Test chunk unload/reload and block replacement during processing. A cached recipe or neighbor reference must invalidate when recipes reload or neighbors change.

## Items and components

Use the platform's supported item data component model rather than transplanting pre-component raw item NBT patterns. Distinguish default component values, stack-specific overrides and removal semantics. Use immutable component values or the required replacement/copy pattern; mutating a shared object can bypass dirty/sync/equality expectations.

Give custom persisted/synchronized values the proper codec(s), bounds and stable schema. Do not use display name/lore as authority. Item identity, tooltip rendering and server gameplay checks are different concerns. Check stack copying, splitting, combining, crafting, recipe remainders, dropping and saving.

For item models, 1.21.4 introduced definitions under `assets/<namespace>/items/` in addition to model geometry references. A working texture or legacy predicate alone may not be enough. Inspect generated files and runtime resource errors.

## Entities and synchronization

Register type, attributes, spawn/data rules and client renderer separately according to version requirements. Keep server AI/physics and client visuals distinct. Use supported tracked data for small entity state where appropriate; use payloads for custom interactions when required. Avoid sending the same state redundantly through multiple mechanisms.

Test natural spawn, command spawn, save/reload, dimension transfer, tracking range, late client join, death/removal and despawn. An entity ID is connection/world-local and not a durable UUID. Do not retain entity instances across unload.

## Persistence choices

Use the exact-version supported saved-state/attachment/component APIs. Fabric attachment APIs are not interchangeable with NeoForge attachments. Confirm sync/copy-on-death support by release rather than assuming one universal capability.

For block entity persistence, examine the 1.21.5 NBT getter changes and the 1.21.6 serialization view transition in the target namespace. Preserve defaults deliberately; an optional getter returning empty is not the same as a legitimate saved zero. Test missing/malformed values and old saves.

Level-level data needs a lifecycle-owned save mechanism. Do not store all worlds in one unkeyed static map. Mark dirty at the right mutation boundary, and do not call full disk saves per tick or from a worker holding live game objects.

## Datagen and reload

Use target-version datagen providers for recipes, loot, tags, models, blockstates and language where appropriate. Do not hand-edit generated outputs if the source provider will overwrite them. Keep generated output reproducible and review unexpected deletions or registry-key changes.

Validate pack metadata and version-specific singular/plural paths. Do not assume a path that worked in an old tutorial is still correct. Tags merge by semantics; replacing a tag can remove other mods' content. Namespace all resources, avoid accidental override of vanilla IDs, and state intentional overrides.

Data/resource reload can invalidate recipes, tags, models, baked objects and caches. Parse/prepare on appropriate stages, then apply atomically under the documented reload contract. Do not run a filesystem scan or parse a data pack inside each gameplay event.

## Commands and interactions

Use the documented command registration callback for the target API and Brigadier where appropriate. Enforce server permissions and sender context; guard client-only commands separately. Do not confuse a client command with a privileged server operation.

Interactions may fire for multiple hands, sides or phases. Define whether a result passes, consumes, succeeds or fails on each side; preserve existing semantics during ports. Avoid a blanket “return success” that prevents other mods from handling an interaction or consumes an item twice.

Sources: dated Fabric release articles in the shared source index; [Fabric developer docs](https://docs.fabricmc.net/develop/); exact resolved target sources.
