# Behavior contract — use only for a substantial change

## Requested change
State the problem and measurable success criteria.

## Target facts
MC/platform/API/loader/build, Java/Kotlin, mappings, physical/logical side, production artifact.

## Baseline evidence
Reproduction, current result, expected result, existing tests and pre-existing failures.

## Invariants
- Public commands/permissions/messages/config:
- Event/results and ordering:
- Gameplay values/timing/RNG boundaries:
- IDs/persistence/schema/units:
- Protocol/authority and sync:
- Lifecycle/resource ownership:
- Integration behavior:

## Approved semantic differences
None unless explicitly approved; list intentional bug/security corrections.

## Smallest implementation plan
For each step, name the change and verification. Avoid speculative future work.

## Regression scenarios
Happy path, invalid/duplicate input, disconnect/reconnect, old-save restart, shutdown and integrations as relevant.

## Evidence and limits
Commands/scenarios actually executed, exact builds, results, unrun checks and rollback.
