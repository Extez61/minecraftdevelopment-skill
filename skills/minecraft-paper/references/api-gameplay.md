# Paper public API, gameplay, metadata, UI and persistence

## Events and interoperability

Keep event priority and `ignoreCancelled` deliberate. Follow the actual event's cancellation/result semantics; some events expose separate use results. Monitoring priority is for observation, not state mutation. Do not uncancel another plugin's protection check casually.

Use early cheap guards in high-frequency move/interact/damage events. Avoid full scans, config I/O, regex/component parsing or repeated reflection per event. Do not skip all move events unless movement crossed a block boundary if the feature needs sub-block precision or rotation; that is a semantic decision.

Check source/target, hand, action, world/arena and phase. Avoid duplicate item grants for multiple hands or recursively triggered damage. Coordinate death/respawn, spectator and quit cleanup. Define whether a reward belongs to the final accepted event or a separate authoritative transition.

## Persistent Data Container and item components

Prefer supported PDC for plugin-owned namespaced metadata; do not use names/lore or raw NMS tags as identity. Keep key names and types stable. Validate types and missing values. Copy/modify item metadata through documented APIs and avoid sharing mutable stacks.

PDC access conveniences differ by version. Inspect the exact API for item stacks, item meta, entities and block state containers. A PDC write on a block state snapshot may require the documented update/commit step; merely changing a detached object is not always persistent.

Paper's data component API has version-specific and potentially experimental surfaces. Prefer stable high-level item APIs when they meet the need. Do not assume every modern component method exists on 1.21.1 or is Bukkit/Spigot portable. Keep experimental APIs isolated with explicit target support.

Do not serialize arbitrary runtime objects into PDC. Store a small versioned schema or stable reference to authoritative storage where appropriate. Test stack split/merge, anvil/crafting behavior, transfer, death/drop and restart.

## Inventory menus

Use an owned holder/session identity, not an inventory title comparison alone. Distinguish raw slot indices, view slots and player inventory. Treat click and drag events according to the documented transaction timing. Certain inventory open/close operations should be deferred to a safe next-tick action per the API; follow exact docs.

Cover shift-click from both inventories, hotbar/number-key swaps, offhand swap, double-click collection, drag distribution, cursor contents, outside clicks and creative mode. Cancellation alone is not a complete design. Recheck a delayed callback still refers to the same player/menu/session.

Never grant a purchase based only on client button/lore text. Validate price, balance, stock, capacity, permission and session immediately before server-side mutation. Define rollback if item grant or economy operation fails; do not claim multi-plugin exactly-once guarantees without a protocol.

## Adventure and messages

Use Adventure components/MiniMessage as already adopted in the project. Separate trusted administrator formatting templates from untrusted player-provided text. Use unparsed/text insertion for user values so they cannot inject click events or commands.

Do not parse a static template per player per tick; prepare immutable components where valid and substitute dynamic values safely. Preserve localization, placeholders and permissions. Do not add a text library to a Spigot-compatible module if its runtime is not distributed intentionally.

## Scoreboards, boss bars and effects

Update only changed state when semantics allow. Scope recipients by match/team/visibility. Remove viewers and temporary objectives on ownership end. Do not overwrite another plugin's scoreboard or global team state without a defined integration strategy.

Limit particles/sounds to relevant audiences and settings, preserving requested behavior. A lower visual frequency is a tradeoff, not a free equivalent optimization. Avoid adding cosmetic broadcasts to every arena by default.

## World and entity operations

Check loaded chunk/valid entity/world ownership before actions. Large block edits should be budgeted and cancellable with explicit completion; preserve ordering, physics and neighbor updates where relevant. Skipping physics indiscriminately changes gameplay and world consistency.

For map instances, verify copied world integrity, ownership, unload/save policy and deletion safety. Avoid retaining `World`/`Chunk`/entity references beyond unload. UUIDs still require cleanup and live re-resolution.

## Persistent profiles/config

Use the shared repository and transaction guidance. On join, distinguish loading from loaded and failed; a default profile must not overwrite durable data. On quit snapshot safely, keep required pending writes tracked and reject stale rejoin callbacks. For economy/progression preserve precision, ordering, and idempotent reward behavior.

Use feature-specific validated config reload only when implemented; code deployment normally requires restart. Do not recommend hot plugin unloading as a substitute for lifecycle correctness.
