# Performance change report

## Hypothesis and invariant
What repeated cost is being reduced? What behavior must remain equivalent?

## Reproduction
Commit/artifact, game/platform/JDK, hardware/heap, worlds/entities/players, mod/plugin set, seed/settings, warmup.

## Measurements
| Metric | Baseline | Changed | Repetitions/variance | Notes |
| --- | --- | --- | --- | --- |
| Tick/frame p50/p95/p99 | | | | |
| CPU/allocation/GC | | | | |
| Network/storage cost | | | | |

Do not fill with invented numbers. Separate client FPS, server MSPT/TPS and RTT.

## Change
Files, algorithm/caching/invalidation/budget details, complexity added and alternatives rejected.

## Equivalence tests
Event semantics, timing/radius, ordering/RNG, save/network state, lifecycle and external integrations.

## Outcome
Measured improvement/regression, tradeoffs, untested cases, and whether the change should be retained.
