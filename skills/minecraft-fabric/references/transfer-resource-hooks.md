# Fabric transfer, reload, conditions and optional extension hooks

## Item/fluid transfer transactions

Use the target Fabric Transfer API's storage/views and transaction contract for the actual item/fluid integration. A storage lookup, a mod-owned inventory, a component container and a vanilla slot view can have different ownership/copy semantics. Verify exact supported types and sided context.

Separate discovery from execution. When querying neighbors, avoid chunk generation and stale storage references; invalidate on neighbor/state/unload changes or use documented lookup patterns. Cache only for a measured repeated lookup and a well-defined lifetime.

A transaction should either commit the intended transfer or leave the simulated/aborted state unchanged. Test partial insert/extract, zero capacity, invalid quantities, remainders, combined inventories, a changing neighbor and exceptions/early returns. A try-with-resources transaction scope does not automatically mean “always commit”; call the correct commit only when the complete operation succeeds.

Do not combine a Fabric transaction with a separate database/economy service and claim distributed atomicity. Do not mutate inventories outside the supported transaction when rollback is expected. Keep gameplay storage access on the owning thread; transactional APIs are not general concurrent containers.

Fabric item/fluid transfer and an external energy API are distinct choices. Inspect the intended energy provider, units and simulation contract; do not invent a standard built-in Fabric energy interface or silently convert energy units across integrations.

## Resource reload and data conditions

Identify client resources versus server data. Use the exact target's reload registration, prepare/apply stages and ordering dependencies. The 1.21.9 resource loader rework is a known boundary; do not keep removed identifiable-listener assumptions in newer targets.

Parse independently where permitted, validate completely, then swap immutable resolved state at the correct stage. Invalidate recipes/tags/registry/model-derived caches deliberately. Never perform an expensive directory scan or JSON parse per tick. Retaining a recipe/registry lookup past reload can be incorrect even when an ID string is stable.

Use supported resource-condition mechanisms only when needed to make optional content depend on a mod/config/context. Confirm condition registration and datagen schema for the target. A condition hiding data is not permission to reference an absent class from shared Java/Kotlin code.

## Networking, menus and event extensions

Use native events/lookup hooks before Mixins. Establish phase, logical side, result propagation and callback thread. A callback returning PASS rather than consuming can be essential for other mods. Do not centralize all integrations into an invented global event bus.

For optional mod entrypoints, load them through a safe loader boundary only when the provider is present and compatible. Do not instantiate every integration during static startup. Type references in common code can link before a later presence check.

## Client UI, particles, sounds and rendering

Register client screen/keybinding/render/audio features on client paths. Distinguish server-driven particle/sound events from purely local effects; do not execute gameplay twice. Input edge/held semantics should preserve the requested cadence and use validated server requests.

Do not load textures/fonts/shaders synchronously per frame or retain invalid GPU objects after reload. A modern rendering event or method name is not guaranteed on 1.21.1. Check the matching release source and production transforms.

## Acceptance gate

Verify transaction abort/commit, runtime absence of optional providers, resource reload ordering, dedicated-server boot, late join/sync and data-pack overrides. Source: [Fabric Transfer overview](https://wiki.fabricmc.net/tutorial:transfer-api), exact Fabric API sources and dated release articles in the shared source index.
