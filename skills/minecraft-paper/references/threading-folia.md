# Paper threading, asynchronous work and explicit Folia support

## Conventional Paper

Assume world/entity/player/inventory/scoreboard operations belong on the server thread unless the exact API documents otherwise. Some events are asynchronous; inspect their contract instead of treating every listener as main-thread. Do not make event dispatch synchronous by blocking an async event on the tick thread without considering deadlocks.

Use async work for independent blocking I/O or heavy pure computation. Capture immutable IDs/values on the owner, do the independent work, schedule an owner-thread continuation, then validate lifecycle/session before applying. Re-resolve live players/worlds only on the correct thread.

Do not call `.get()`/`.join()` on a future that needs the game thread. Do not assume `thenAccept`, coroutine `IO` or a scheduler callback in another API has the right ownership. A plugin disabled during I/O must not receive a late mutating completion.

## Scheduling semantics

Ticks are simulation units, not a wall-clock guarantee. Preserve whether a cooldown should slow with server TPS or expire after real elapsed time. Use monotonic timing for in-process elapsed durations; persistent real-time expiry needs an explicit wall-clock design.

Store handles when cancellation matters. Cancel per-match/entity tasks when ownership ends, not only on plugin disable. Prefer a feature/match-owned loop when appropriate, but do not create a global mega-scheduler for unrelated concerns without evidence.

Avoid synchronous chunk load/generation in hot callbacks. Async chunk APIs, where available, still require attention to completion thread, lifecycle, cancellation and ticket cleanup. An async load does not make subsequent arbitrary block mutations thread-safe.

## Folia is a distinct concurrency target

Folia divides ticking into region ownership. It is not “Paper with a faster main thread.” Do not claim support merely because your plugin avoids explicit async work.

| Work | Owner/scheduler concept |
| --- | --- |
| A moving player's/entity's state | Entity scheduler, including retirement handling |
| Blocks at a fixed location | Region scheduler for that location |
| Global non-region task | Global region scheduler |
| Independent I/O/computation | Async scheduler/owned executor |

Entity scheduling follows the entity when it moves; location scheduling does not. Global scheduling does not grant access to arbitrary region-owned entities/blocks. Cross-region multi-entity operations require careful message-passing/coordination and validated APIs; do not hold locks while synchronously waiting for another region.

Audit every direct access, including reads, collection iteration, events, commands, teleportation, inventory updates and libraries. A concurrent map does not protect region-owned values. Global static game state can race when two regions call your code simultaneously.

Use supported asynchronous teleport/lifecycle APIs only after verifying target signatures and outcomes. Handle entity retirement/disconnect and callbacks that may never run if the entity is gone. Release operation resources on all completion paths.

## Scheduler abstraction: only when justified

If explicitly supporting conventional Paper and Folia, a small owner-aware execution interface can isolate scheduling. Do not provide a fake `runSync` that maps all work to the global scheduler. Methods should express ownership, such as entity-bound, location-bound and independent work, without hiding invalid assumptions.

Do not add a platform abstraction if only ordinary Paper is required. State Folia is unsupported rather than shipping a misleading flag. If supporting it, include `folia-supported: true` only after the actual audit and tests.

## Storage and shutdown

Use bounded repository work and per-profile ordering/session tokens. Save snapshots rather than traversing live inventories asynchronously. On disable stop input, invalidate callbacks, snapshot where allowed, and drain important writes under a bounded policy. Avoid waiting forever for an owner thread that has stopped.

Kotlin scopes must be lifecycle-owned and cancellation-aware. `GlobalScope`, `runBlocking` on a tick thread, and IO-dispatcher world access are prohibited shortcuts.

## Verification

Test independent players/entities in different regions, cross-region interaction, teleport during a queued operation, disconnect/retirement, world unload and disable during work. Concurrency bugs often do not reproduce with one stationary player. Passing conventional Paper tests is not Folia verification.

Source: [Supporting Paper and Folia](https://docs.papermc.io/paper/dev/folia-support), [Paper API guides](https://docs.papermc.io/paper/dev/api/). Confirm the exact resolved scheduler API before writing code.
