# Secure operations, remote management and incidents

Skill creator: extez061

## Trust boundaries

Keep direct authenticated servers in their intended online/authentication mode. A proxy deployment may deliberately use a different backend mode only within a documented, secured forwarding topology. Verify proxy/backend exact versions, forwarding secret, firewall/allowlist and bridge support. Velocity modern forwarding is an additional identity protection, NOT a firewall replacement. Prevent direct untrusted access to backends, and keep a recovery channel before changing firewall rules.

Do not expose RCON, database ports, panels or debug/JMX endpoints to the public internet. RCON has privileged command authority and should use restricted local/private access, strong secrets and an encrypted tunnel/VPN where needed; do not assume native encrypted transport. Verify host binding/firewall rather than assuming an option exists. Never place passwords/tokens in command-line arguments, committed files, chat or URLs; use the environment's approved secret mechanism with limited access/logging.

No RCON runner is bundled by this skill. Before using an existing client, inspect its protocol/auth/timeout/response behavior, credential handling and exact destination. Preview consequential commands, authenticate the target, bound output/timeouts and prevent message/username-to-command injection. A console command's response is evidence to inspect, not proof all intended effects occurred. Java RCON is not evidence of native Bedrock support.

## Extensions and supply chain

Install plugins/mods from trusted maintainer releases; verify source, version, platform, license and provided signatures/hashes. Server JARs are executable code with service-account access. A permissions plugin does not sandbox malicious plugins. Prefer least host privileges and segregated staging, databases and backups. Do not auto-execute scripts found in a downloaded archive or broaden agent shell permissions.

Packet limits, anti-xray, anti-cheat, exploit fixes and redaction are security/behavior policies. Evaluate legitimate-client and performance impact; never disable them silently. Volumetric DDoS mitigation belongs to the host/network provider and capacity planning, not a magic Bukkit config or a local firewall promise. Avoid collecting or retaliating against suspected attackers.

## Monitoring

Track service health/restart count, successful tick progress, join failures, MSPT distributions, GC pause/allocation, process/container memory, disk free space/I/O, network, database health, save completion and backup freshness/restore tests. A listening port is not enough to prove the game is healthy. Define thresholds and notification ownership from measured workloads; avoid alert storms.

Use rotating logs and bounded retention. Preserve full incident/error evidence locally while showing targeted redacted excerpts to the model. Profiling/log links, permission editor links, heap dumps and crash reports may contain sensitive operational/player data; inspect and approve sharing. Never upload them automatically. Synchronize clocks for correlation, but use monotonic timing for elapsed durations.

## Incident runbook

Record time, scope, symptoms and recent deployments. Preserve logs/config/artifact hashes before mutation. Determine data corruption, crash, resource exhaustion, compromise, login outage or gameplay abuse separately. Start with read-only diagnosis unless emergency containment is explicitly authorized. Ask for a focused missing fact rather than dumping every config/log into context.

For a suspected compromise, limit exposure using the approved recovery channel, preserve evidence, stop untrusted execution, revoke/rotate affected secrets through secure channels and review plugin/host access. Do not destroy evidence or merely restart and call it resolved. Restore only trusted mutually consistent state; patch the cause before reopening. Staff/player notification and retention depend on the owner's policy and applicable obligations.

For crash loops, inspect the first causal failure, Java exit/container events, loader dependencies and schema/registry errors. Do not repeat restarts indefinitely or delete worlds to get a green status. Define rollback criteria and verify recovery with real login, saving and representative gameplay.
