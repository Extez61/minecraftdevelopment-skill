# Small architecture, explicit gameplay state

## Default shape

Start with a bootstrap/entrypoint, feature-focused code, and a small pure domain core only where it improves tests. Do not create `Manager`, `Service`, `Factory`, `Repository`, `Controller` and `Facade` for every noun. Separate a repository when real persistence is involved; do not wrap a single map behind five interfaces.

Prefer constructor injection of a few real collaborators to mutable global singleton access. Keep resource ownership clear. A plugin/mod entrypoint coordinates lifecycle, not every gameplay algorithm. Preserve existing conventions unless the current structure directly prevents the requested correction.

## State machines

Represent phases explicitly when behavior depends on them: lobby → countdown → running → ending → closed. Keep legal transitions centralized and observable. One authoritative phase is safer than independent `started`, `ending`, `canJoin` and `isLobby` flags that drift apart.

A transition should check current state, apply invariants, create/cancel owned resources and handle failure. Repeated stop/close should be idempotent when appropriate. Delayed callbacks must carry an instance/generation token and reject stale ownership.

For cooldowns, choose simulation ticks or monotonic elapsed time based on the existing contract. Wall-clock time can jump; tick time slows under server lag. Do not silently switch clocks in an optimization. Persist absolute expiry only when the feature should survive restart, with explicit clock assumptions.

## Arenas and multiplayer sessions

Keep per-arena ownership of players, teams, spectators, mobs, projectiles, timers, temporary items, scoreboards and chat audiences. Clean up on quit, kick, death, match completion, map failure and disable. Check cross-arena visibility/combat/chat and global broadcasts.

Avoid a task per player for a concern that is naturally one match loop. Do not replace every task with one giant universal tick system either. Choose the smallest owner-aligned schedule. A phase change should invalidate countdown/reward callbacks so old rounds cannot affect new matches.

Copy and unload temporary worlds safely. Validate ownership before deleting generated folders. Never clone an actively written world as if it were a consistent backup. Require explicit authorization for destructive cleanup and operate only on known owned test directories.

## Machines, inventories and crafting

Keep recipes/data separate from execution state. Validate inputs once at a defined boundary and recheck before a transaction commits if state can change. Simulate insertion/extraction correctly; do not mutate during a simulation query. Distinguish server inventory state, persistent storage and client display sync.

Do not run expensive recipe scans for every block entity every tick. Use dirty flags/cache invalidation when correct, bounded lookup/indexing if measured, and preserve recipe precedence and dynamic datapack reload behavior. Reload invalidates recipe/registry-derived caches.

## Combat and progression

Preserve event cancellation and modifiers from other mods/plugins. Check source, attacker, target, projectile owner, team, game phase and invulnerability semantics. Guard against recursively triggering your own damage handler. Do not apply damage and award kills twice across duplicate callbacks.

Use idempotent reward identifiers where retries/duplicate events matter. Track XP/perks/quests by stable identity, clean player sessions, and preserve save format. Do not turn an atomic reward transaction into disconnected fire-and-forget writes.

## Multi-loader and cross-version layout

Only introduce a shared module when more than one actual target is required or tests justify it. Share pure rules, small immutable data and algorithms. Keep registration, loader lifecycle, client rendering, network registration, components/attachments, capability bridges and runtime descriptors in platform modules.

Do not expose Fabric/NeoForge/Bukkit types through a “common” API meant to be platform-neutral. Avoid loading one platform's classes from another platform artifact. Build and inspect each distribution separately. If using an existing multi-loader toolchain, preserve its conventions instead of inventing a replacement.

Port semantics, not imports: a Bukkit event is not necessarily equivalent to a Fabric callback or NeoForge event. Document cancellation, logical side, timing and permission differences per adapter. A single common event bus is not automatically warranted.
