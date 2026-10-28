# Mod/plugin compatibility report

## Target and provenance
MC/loader/server/Java/exact build, side, source of list, observation date; offline versus runtime evidence.

## Inventory
| Source/archive | ID and aliases | Declared/resolved version | Loader/side evidence | Dependencies | Confidence |
| --- | --- | --- | --- | --- | --- |

## Confirmed blockers
Only target-matched dependency/resolution/runtime failures with evidence; not guesses from filenames.

## Candidates and unresolved facts
Version expressions not evaluated, nested dependencies not inspected, export IDs not resolved, client/server differences, optional integration/classloading, mixin/render/registry issues requiring source/runtime checks.

## Smallest safe actions
Explain why, expected behavior/data impact, required authorization, backups and reversible steps. No automatic deletion/download or production-world experiment.

## Verification
Exact runtime/artifacts and scenarios actually executed; unrun checks stated. Include startup/connect, feature behavior, old-save restart and profiling only as relevant.

## Rollback
Restore original artifacts/config/save copy as needed; downgrading a JAR alone does not undo converted world data.
