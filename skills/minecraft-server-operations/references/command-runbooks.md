# Operational command runbooks

Skill creator: extez061

## Read-only first, authorized execution second

Identify the target instance, exact version/platform, authenticated identity, console/RCON/panel context and user-authorized scope. Commands shown here are categories/templates to verify using the actual server help; this file is not permission to execute them. Console commonly omits the slash used in chat. Vanilla, Bukkit, plugins, mod loaders and proxy consoles have different command trees. Do not promise vanilla commands for plugin-only features.

| Need | Lookup / workflow | Boundary |
| --- | --- | --- |
| Connected players and basic status | list / installed platform diagnostics | Do not publish player identifiers; TCP reachability is not game health. |
| Access and staff | whitelist add/remove/list, op/deop; LuckPerms roles | Exact identity, least privilege and explicit scope; see player-management.md. |
| Moderation | kick, ban/pardon; installed plugin mute/temporary policies | Preview players/reason/duration; no bulk or autonomous punishment. |
| Player support | teleport, inventory/economy repair using supported tools | Verify world/session/authority and save/data rollback; no automatic item grants. |
| World rules | difficulty, gamerule, time/weather using target syntax | Gameplay changes require owner intent; enumerate actual rules instead of inventing names. |
| Maintenance notice | say or supported localized broadcast | Review message/audience; do not send unsolicited broadcasts. |
| Profiling | installed spark help and bounded recording | Approval for report uploads, overhead/privacy and real performance evidence. |
| Save/backup | version-supported save workflow with databases | save-all/flush is not a transactionally complete backup; follow backup-recovery.md. |
| Stop/restart | graceful stop via actual supervisor | Explicit downtime scope, verified save and rollback; no generic hot reload. |

## Remote and scheduled actions

Use the host's established secure SSH/panel/RCON tooling; no credentials in chat/commands/git. Prefer a read-only dry-run preview for scheduled maintenance and exact allowlisted actions for automation. Escape/validate all identifiers and input according to the actual tool; never splice player/log text into shell or console strings. Bound execution time, output, retry count and concurrency.

Retries are not always safe: a repeated give/payment/teleport/ban can change state twice or override a newer decision. Use an operation ID/idempotent design where possible and verify before replay. One server's success must not be applied to another instance by a stale connection. Record minimal private audit evidence and report only the user-relevant outcome.

A generic terminal runner, panel API integration, multi-server orchestration or Java RCON client must be separately implemented and tested if requested. Do not claim these exist merely because this guide mentions them; do not claim native Bedrock RCON support. Do not deploy a cron/service job merely to document it.

## Minimal response

State what completed and the required next action or risk, if any. Keep full command transcripts private and available for investigation; omit irrelevant substitutions, architecture notes and routine command narration. Never hide a failed permission change, pending restart, partial execution or possible data loss.
