# Behavior preservation and surgical change protocol

## Baseline before editing

Record only relevant contracts, not an exhaustive design document. For a one-line fix, a test and a sentence may be enough. For stateful features, use `templates/behavior-contract.md` from the package.

| Surface | Preserve or explicitly migrate |
| --- | --- |
| Commands | names, aliases, argument forms, permission nodes, console handling, completion visibility |
| Gameplay | damage/reward amounts, ordering, cooldown clock, range boundaries, random distribution, phase transitions |
| Events | firing frequency, priority, cancellation/result propagation, other-mod/plugin interoperability |
| Data | stable resource IDs, schema versions, PDC/component keys, units, precision, UUID identity |
| Configuration | keys, defaults, validation, comments where meaningful, migration and reload behavior |
| Network | direction, discriminator/identifier, codec bounds, sequence and resync behavior |
| Lifecycle | startup failures, load order, quit/death/dimension changes, world unload and shutdown cleanup |
| Integrations | optional dependency absence, service registration and permission/economy behavior |

Distinguish “observable contract” from accidental implementation detail. Do not preserve an exploit as a feature; document the intentional correction and test the legitimate case too.

## Bug-fix workflow

1. Capture exact version, stack trace with root cause, reproduction, expected and observed behavior.
2. Narrow the first incorrect state transition rather than suppressing its later exception.
3. Add a failing regression test or a repeatable runtime scenario before the fix where practical.
4. Change the earliest appropriate boundary, keeping permission, side and lifecycle validation intact.
5. Repeat the reproduction and adjacent negative cases; verify persistence/restart if touched.
6. Remove temporary diagnostic noise and review only your changes.

A null check is correct if absence is legitimate. It is not a substitute for understanding why registration failed. Disabling the listener, returning success without doing work, or replacing lost data with defaults is not a safe bug fix.

## Refactoring workflow

Keep behavior fixes and structural changes separate unless inseparable. Preserve serialization shape and constructor/entrypoint requirements. Keep public JVM signatures when integrations compile against them; Kotlin default arguments do not automatically preserve Java call sites.

Use small steps: extract a pure calculation; establish tests; replace duplicated logic; compile; then remove only newly orphaned code. Do not reformat the repository or redesign a public API in a private helper refactor. Reconcile the requested scope with each changed line.

## Optimization equivalence checklist

- Does event-driven replacement observe every transition formerly polled, including external modification and chunk reload?
- Does batching preserve ordering, atomicity and maximum latency?
- Does caching invalidate on configuration/resource reload, logout, dimension/world change and external writes?
- Does using squared distance preserve an inclusive radius comparison and the same coordinate system?
- Does changing iteration order change RNG consumption, tie-breaking, reward ordering or deterministic output?
- Does deduplicating updates preserve required side effects and downstream events?
- Does async execution preserve per-player write ordering and prevent stale completion?
- Does a lower update frequency change gameplay timing? If yes, get approval rather than calling it behavior-preserving.
- Does using a set remove multiplicity that mattered? Does a cheaper collection alter iteration guarantees?
- Does a save queue acknowledge durability too early? Are failed writes surfaced and retained?

Use explicit numerical equivalence rules for floating-point calculations and money. A slightly different calculation order can change boundary outcomes; characterize thresholds, overflow, negative values and zero denominators.

## State-machine invariants

For a match, craft, transaction or machine operation, establish:
1. one authoritative owner;
2. legal states and transitions;
3. preconditions and postconditions;
4. idempotency or rejection of duplicate input;
5. rollback/compensation for multi-step failures;
6. cleanup after each terminal state.

Test repeated quit/join, duplicate packets, death during an async load, world unload while a task is queued, reload during a menu session, and disable during persistence. Use generation/session tokens when an old completion could otherwise affect a new session.

## Definition of done

A change is complete when the requested behavior is implemented, relevant old behavior remains covered, the artifact is correct, and gaps are honestly stated. More classes, more documentation and more patterns do not increase correctness by themselves. Stop expanding once success criteria are met.
