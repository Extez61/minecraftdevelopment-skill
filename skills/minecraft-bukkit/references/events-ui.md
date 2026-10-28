# Bukkit events, commands, GUIs and item identity

## Event contracts

Inspect exact Javadoc/source for priority, cancellation and threading. `MONITOR` is observational. `ignoreCancelled=true` is not universally correct: it changes whether the feature sees cancelled actions. Choose it according to behavior and interoperability.

Do not assume every event is synchronous. Async chat/pre-login-style contexts need explicit thread handling; do not touch world/player state just because an event has a player-like identifier. Do not retain event objects into delayed callbacks; capture validated values or re-resolve state on the owner.

For interaction events check action, hand, item, block/entity and feature state; some interactions occur twice or expose separate use results. For damage, death and rewards inspect event chains and recursion. Preserve protection-plugin cancellation and game-phase gates.

Avoid heavy operations in move, damage, interact and inventory callbacks. A block-coordinate filter can be a good optimization only if the feature does not care about within-block movement/rotation. Do not silently change precision.

## Command safety

Validate console versus player, permission, argument count/type, target existence, bounds and feature lifecycle. Error messages should be actionable and avoid leaking hidden player/admin information. Do not perform blocking remote lookups for every tab-completion request.

Keep command parsing separate from domain logic only to the extent it improves clarity/testability. Do not introduce a large command framework for a two-subcommand plugin unless already used. Never interpolate command arguments into shell commands or SQL.

## GUI transaction model

Use a known holder/session to identify the menu. A title is a display string and can collide. Distinguish the top inventory, player inventory, raw slot numbers, local indices and outside clicks.

Handle all relevant transfer routes:
- ordinary left/right click;
- shift-click from either inventory;
- hotbar/number-key swap and offhand;
- double-click collection;
- drag events over protected and unprotected slots;
- cursor state, dropping and outside clicks;
- creative-mode actions if supported;
- closing/disconnect during delayed work.

Read `InventoryClickEvent` restrictions. Inventory open/close and transaction-sensitive mutations are not universally safe inside the same event. Cancel when required and schedule a next-tick operation where the Javadoc prescribes it, then revalidate the session before applying. Do not call inventory refresh blindly on every click as a substitute for correct transaction logic.

For purchases validate balance, price, stock, capacity and item identity on the server. Consume/award under an explicit transaction policy and handle failures. Make duplicate button input idempotent or safely rejected. A title/lore match or hidden client button is not authority.

## Item metadata

Use stable namespaced PDC keys where the baseline supports them, with explicit type and schema checks. Use the proper item-meta copy/commit pattern; modifying detached metadata without setting it back does not necessarily change the stack.

Avoid mutable shared `ItemStack` templates. Clone before per-player customization; verify split/merge, crafting, anvil, grindstone, drop, death and restart behavior as applicable. Do not force raw NBT or Paper-specific data components into a portable implementation when stable API suffices.

## Player state

Use UUIDs for durable identity and cleanup transient maps. Do not use display names, current online entity IDs or `Player` object identity as persistent keys. Model game phases/cooldowns explicitly and invalidate old delayed callbacks on session/phase changes.

Source: [InventoryClickEvent Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/InventoryClickEvent.html). Current online Javadocs may show a newer game version; verify the project's resolved API before adopting specific methods.
