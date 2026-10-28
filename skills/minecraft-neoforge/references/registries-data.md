# NeoForge registration, components, attachments and capabilities

## Deferred registration

Use the exact target's supported deferred registration and holder types. Attach registration to the appropriate lifecycle/bus and preserve stable namespaced IDs. A holder is not a license to call `.get()` during arbitrary static initialization. Access entries when registration/lifecycle guarantees they exist.

Keep creative tab entries, block items, attributes, menus, recipes, serializers and entity/block entity types coherently registered. Do not register the same object twice under accidental IDs or suppress duplicate registry errors.

Static versus dynamic registries have different lifecycles. Data-driven registries and reloadable content should use appropriate data/bootstrap contexts, not late writes to frozen registries. Do not hold registry lookups or entries across a reload/lifecycle where they may become invalid.

## Choose the data mechanism by responsibility

| Mechanism | Primary responsibility | Do not assume |
| --- | --- | --- |
| Item data components | Structured item stack values with codec/network semantics | Old item NBT or attachments are interchangeable |
| Data attachments | Extra state associated with supported holders | Persistence implies sync or death-copy behavior |
| Capabilities | Discover/expose behavior or handlers through a stable interface | A storage format or general-purpose helper lookup |
| Block entity serialization | Save owned block entity fields | Automatic client updates for every field |
| Saved data | Level/world-scoped persistent structures | A static global map is equivalent |
| Payloads/menu sync | Client/server communication | Durable storage or authority from the client |

Keep state in one authoritative owner, expose it through capabilities as needed, and sync the necessary projection. Avoid four independent copies that drift.

## Item components

Versioned 1.21.1 docs describe `DataComponentType` with persistent `Codec` and network `StreamCodec` options. Verify the builder and codec types in the exact target. Model values immutably or replace them through the supported update API; mutating a shared component object can break equality/caching and sync assumptions.

Test missing/default component values, malformed persisted data, copy/split/merge, recipe use and network round trips. Declare intentional non-persistent/non-synchronized fields explicitly. Do not assume a default network codec is optimal or safe for unbounded structures.

Data attachments for item stacks were superseded by vanilla components according to NeoForge's docs. Do not copy an old attachment tutorial onto modern item stacks.

## Attachments

Define holder applicability, default factory, serialization, copy-on-death/clone behavior and sync policy. Do not share one mutable default object among different holders. Reading with “get or create” may allocate/change state; do not call it indiscriminately in hot render/query paths when an absence check is needed.

The 1.21.1 documentation requires explicit attention to synchronization and notes death-copy behavior. Newer docs add synchronization facilities that should not be assumed present in old builds. Inspect exact APIs, tracking behavior and privacy/audience rules.

If a player dies or changes dimension, decide whether each field resets, persists, copies or re-syncs. Avoid double-copying fields already handled by an API flag. Mark holders dirty as required after mutations, particularly chunk/block-owned state. Test save/reload and old-schema defaults.

## Capabilities and handler contracts

Use capabilities to expose behavior across blocks/entities/items through the actual target API. For 1.21.1, documented standard handlers include items, fluids and energy. Do not transplant old Forge `LazyOptional` assumptions into NeoForge code without verifying the current model.

Respect side/context arguments, lifecycle and invalidation. A cached capability/handler can become stale after a neighbor/block/state changes or chunk unloads. Use the supported cache/invalidation mechanism when justified by repeated queries, not a permanent reference map.

Implement simulation semantics correctly: simulate must not mutate. Validate slot indices, quantities, limits, remainder/returned-stack rules and ownership. Test partial acceptance, full inventory, zero/negative invalid inputs, sided access and repeated simulation before a real transaction. Mutable handler views should not allow bypassing dirty marking or synchronization.

Capabilities do not serialize your implementation automatically. Save the authoritative state through an appropriate mechanism and expose a controlled interface. Do not create a capability for a simple local calculation that needs no dynamic extensibility.

## Block entities and saved data

Keep ticks cheap and server/client work separated. Persist actual owned fields; call the correct dirty/changed method after mutation. Send client update data only as needed. Keep fields such as GUI progress distinct from inventory authority and save structure.

Newer game lines change block entity serialization APIs; 1.21.6 introduces view abstractions described in migration notes, with names depending on mappings. Use the NeoForge target source instead of guessing Yarn-derived names.

For level data, handle level/server lifecycle, schema migration and save flags. Avoid duplicate global data per dimension unless intentional, and do not use a process static singleton as a durable storage system. Never edit the only save copy during migration experiments.

Sources: [1.21.1 components](https://docs.neoforged.net/docs/1.21.1/items/datacomponents/), [attachments](https://docs.neoforged.net/docs/1.21.1/datastorage/attachments/), [capabilities](https://docs.neoforged.net/docs/1.21.1/inventories/capabilities/).
