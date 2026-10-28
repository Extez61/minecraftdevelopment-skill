# Performance engineering without feature loss

## Diagnose the actual bottleneck

Distinguish server tick time (MSPT), tick rate (TPS), client frame time/FPS, GC pauses, packet throughput, disk waits and network round-trip latency. “Lag” is not a diagnosis. At a nominal 20 TPS the total tick budget is 50 ms; that is not your feature's private allowance. TPS capped at 20 can conceal significant remaining headroom or occasional bad tails.

Use a representative reproduction: game/server build, JDK, heap, CPUs, worlds, view/simulation distances, players, entity/block-entity counts, mod/plugin set, seed and warmup. Record p50/p95/p99 tick/frame time when available, not only averages. Separate cold chunk generation from steady-state loaded chunks.

Use a sampling profiler such as spark for supported server environments, JFR for JVM CPU/allocation/locks/GC, heap tools for retained-object analysis, and appropriate client profilers for rendering. Obtain consent before uploading profiles or heap dumps: they can contain sensitive world/player/plugin data. A profiler page or command is version-dependent; inspect installed tooling rather than fabricating a command.

## Optimization loop

1. Establish a baseline and one hypothesis.
2. Locate a hot path with a profile or narrow instrumented measurement.
3. Estimate call frequency × per-call cost, including allocation and downstream effects.
4. Choose the least complex change that addresses the dominant cost.
5. Run behavior equivalence and regression tests.
6. Re-measure the same workload with warmup and repeated samples.
7. Report absolute values, relative improvement, variance and limits. Keep the change only if the evidence supports it.

Do not report a percentage from invented data. JMH can validate pure calculations; it does not simulate chunk ownership, event dispatch, network backpressure or game ticks. Avoid `System.nanoTime()` spam in every callback; aggregate or sample deliberately.

## High-value patterns

### Remove unnecessary work without changing semantics

Prefer correctly invalidated event-driven updates over unconditional polling. Update a scoreboard slot, menu field or sync payload when its underlying value changes. Track dirty state and flush at a bounded interval if the feature permits that latency. Verify external changes and reload paths trigger invalidation too.

Guard hot listeners early by cheap checks: world/arena membership, action type, item presence and relevant state. Cache a stable ownership index if maintaining it is cheaper and reliable. Do not compare full lore strings or parse JSON every move event.

### Bound work

Use a per-tick budget for large migrations/builds, with cancellation and progress. Bound both item count and time when cost varies. Do not force a whole-world entity scan or block traversal into one tick. Never silently skip required work to stay under budget; defer it according to a documented deadline, or report overload.

Keep database/HTTP concurrency below sensible pool/service limits; bound queues and define overload behavior. More threads can reduce throughput through contention. Virtual threads do not make world APIs safe and do not remove external-service capacity limits.

### Avoid accidental chunk loads

Read only loaded/relevant chunks when feature semantics allow. If loading/generating is required, use the supported target API and lifecycle, with bounded concurrency and cancellation. Track/release chunk tickets. A location lookup, block access, teleport or nearby query may trigger expensive behavior; inspect semantics.

### Reduce repeated queries

Prefer per-world/per-arena/per-chunk indices for a measured query bottleneck. Define update points and cleanup for spawn, remove, transfer, unload and reload. An index that returns stale state is not an improvement.

For nearby checks, squared distance can avoid square roots when mathematically equivalent. Check world/dimension identity first and avoid overflow or coordinate mistakes. Do not shrink the search radius or cap targets without user approval.

### Memory and GC

Do not retain `Player`, `World`, entity, block entity, renderer or event instances in long-lived static structures. UUID keys still leak if never removed. Bound caches by size/lifecycle and use immutable snapshots. Examine retained references rather than blaming “Java GC” generically.

Avoid ephemeral large collections, repeated component parsing, per-tick reflection, and unnecessary serialization in proven hotspots. Pooling mutable objects can add aliasing bugs and complexity; do not pool by default. Resource keys and immutable configs can often be reused safely, whereas mutable stacks cannot be shared blindly.

### Networking

Send only to affected/tracking clients, and send deltas when protocol semantics allow. Batch within an acceptable delay and limit payload sizes. Avoid a per-player full-state packet every tick for unchanged values. Always send a correct initial state and recovery resync; an optimization that works only for already-connected players is incomplete.

### Client rendering

Track frame-time tails and GPU resource lifetime. Avoid blocking resource loads, per-frame shader compilation, recreating buffers without need and raw backend assumptions. Follow exact-version extraction/submission rules. Do not access changing world objects from a render stage that expects immutable captured state.

## Do not optimize like this

- Disable validation, anti-duplication or permission checks.
- Drop inventory updates/saves or change event cancellation ordering.
- Increase cooldowns, reduce mob counts or simulation ranges without calling it a behavior change.
- Move Bukkit/Minecraft state mutation onto workers.
- Add a giant cache with no bounds or invalidation.
- Replace every loop with parallel streams/coroutines.
- Recommend random JVM flags, massive heaps or a thread pool as a universal fix.
- Claim “zero lag,” “O(1)” for a compound operation, or a percentage with no measurement.

## Benchmark report

State hypothesis, workload, baseline, changed build, metrics, repetitions, behavior tests, tradeoffs and remaining bottlenecks. Use `templates/performance-report.md`. “No reliable measurement available; this is a plausible reduction in repeated work” is better than fabricated certainty.
