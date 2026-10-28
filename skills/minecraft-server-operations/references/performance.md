# Measured server optimization

Skill creator: extez061

## Diagnose the right bottleneck

Distinguish client FPS, network latency/loss, join/chunk stalls and server tick lag. TPS is capped at the intended tick rate and can hide reduced headroom. At the normal 20 ticks/second target, the nominal budget is 50 ms/tick; use p50/p95/p99 MSPT and stall durations, not only an average or an unsupported universal target. Record population, loaded/ticking chunks/entities, exploration, farms, mod/plugin builds, hardware/container limits and measurement window.

Observe per-thread CPU, throttling/steal time, heap/GC, process RSS/native memory, disk latency/free space, network and relevant database latency. Low overall CPU does not rule out a saturated tick/region thread. A full heap can be normal until collection; RSS is not identical to heap, and allocating all physical memory to -Xmx can starve native buffers, the OS and other services.

## Profiling

Use the exact installed spark/host profiler and verify commands/help/permissions. Profile while the actual problem occurs. Official spark documentation includes `/spark profiler start --timeout <seconds>`, `/spark profiler stop` and `/spark profiler info`; choose an agreed bounded duration, not an endless capture. In console omit the leading slash as appropriate. Availability, bundled versions and options vary by server build.

Start with CPU evidence. Use allocation/GC/thread captures when the symptom warrants them; more detailed captures have costs. Report recording settings and overhead. Do not run heap dumps, forced GC or heavy all-thread profiling casually on production. Reports may upload operational metadata; obtain the appropriate approval and review exposure before sharing a profiler URL. Preserve raw logs and real command exit/results, not a filtered PASS summary.

Read the hot path and its callers before assigning blame. Inclusive time is not automatically self-time; a top-level plugin frame may contain world I/O or other plugin work. Correlate GC and storage stalls with tick spikes. Use the shared code-performance guide only when an actual code change is needed.

## Workload-specific actions

- Exploration: profile chunk generation, loading/sending and storage. Optional pregeneration is a scheduled, bounded I/O/CPU/disk task with a defined world border/radius, estimate, monitoring and cancellation; it does not eliminate all runtime load.
- Entities: identify loaded counts, pathfinding, villagers/POI and plugin AI. Fix leaks or repeated searches before changing spawn/activation behavior.
- Hoppers/redstone: identify real concentrations and event listeners. Optimize code safely; changes to event delivery, update order or throughput are gameplay changes, not invisible wins.
- Plugins/mods: reproduce and isolate on a staging copy. Removing content mods may erase persistent registries/items; never binary-search a production world with content mods removed.
- Databases: inspect batching, connection pools, indexes and blocking calls. Bound queues and preserve consistency/transactions. Never move live world access async to reduce MSPT.
- Proxy/network: distinguish authentication, compression, throughput and packet parsing costs. Do not weaken authentication, drop legitimate traffic or relax anti-cheat as a performance fix.

## JVM and host policy

Match the exact runtime requirements: Paper's reviewed table uses Java 21 for 1.20–1.21.11 and Java 25 for 26.1+; verify loader/modpack and launcher requirements separately. Use the actual service/container Java executable, not merely the interactive shell version.

Begin with supported defaults and a justified heap budget that includes OS/native/container headroom. Measure GC before choosing G1/ZGC or additional flags; collector suitability depends on runtime/hardware/workload. Do not paste old experimental Aikar-style flag bundles across Java versions, force Xms=Xmx universally, prescribe a universal maximum heap, or assume more RAM fixes tick-thread CPU. Validate supported flags and startup errors. Record command line, limits, baseline and rollback without leaking secrets.

For containers/panels, inspect effective CPU quota/cpuset and memory limit; a host RAM label may differ from available memory. Do not change system/kernel/network/firewall settings without explicit scope and a recovery channel. Avoid swap thrashing and overcommit; distinguish Java OOM, native allocation failure and container OOM-kill from logs/host evidence.

## Experiment and acceptance

State hypothesis, one coherent change, protected mechanics, identical workload and metrics. Repeat enough to distinguish normal variance; report duration/sample limitations. Test access, economy, saves, farms/redstone, custom mechanics and anti-cheat interactions as relevant. Reject faster results obtained by silently disabling functionality. Provide before/after and rollback, or clearly label a recommendation unmeasured. No zero-lag, fixed player capacity or percentage gain without evidence.
