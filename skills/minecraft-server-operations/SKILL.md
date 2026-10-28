---
name: minecraft-server-operations
description: "Administer, configure, optimize, troubleshoot and maintain Minecraft Java servers from 1.21.1 through 26.2: Paper/Bukkit/Spigot and Fabric/NeoForge; bukkit.yml, spigot.yml, server.properties, Paper per-world settings, spark profiling, Java/GC, player permissions and moderation, backups/restores, updates, proxies, RCON and incident response. Preserve gameplay, saves and security; verify exact server/build settings."
---

# Minecraft Server Operations

Read the [core contract](../minecraft-development/SKILL.md) once. Use the [AI lookup map](../minecraft-development/AI-INDEX.md) to avoid unrelated reading. This is an operations guide, not permission to execute console commands, restart production, punish players, change access/security or accept an EULA. Observe the user's exact authorized scope; propose consequential live actions for approval when not already explicit.

## Establish the target

Identify exact Minecraft/server/loader/modpack versions, Java executable, launch script/service/container/panel, memory/CPU limits, storage free space, worlds/dimensions, online population and workload, recent changes, installed plugins/mods, proxy/bridge topology, backup status and acceptable downtime. Read relevant redacted files before asking questions the evidence answers. Never collect an RCON password or panel token in chat.

Determine whether this is offline config review, staging or live production. Distinguish a restart/reload, a filesystem edit and an executable console action. Do not run broad server commands simply to inventory files. Do not copy Paper YAML into Fabric/NeoForge; load the development platform skill only if source/build work is involved.

## Find the needed guide

| Task | Read |
| --- | --- |
| bukkit.yml / spigot.yml / Paper YAML / properties and inheritance | [Configuration](references/configuration.md) |
| Lag/TPS/MSPT, spark, CPU, memory, GC, chunks/entities | [Performance](references/performance.md) |
| OP/deop, whitelist, roles, LuckPerms, moderation, player data and economy | [Players](references/player-management.md) |
| Setup, plugins/mods, maintenance, updates and platform migration | [Lifecycle](references/lifecycle.md) |
| Consistent backups, restore, corruption and disaster recovery | [Backups](references/backup-recovery.md) |
| Proxy/forwarding, RCON, network access, monitoring and incidents | [Security/operations](references/security-observability.md) |
| Console/admin command planning or safe remote/scheduled actions | [Command runbooks](references/command-runbooks.md) |
| Implement plugin/mod permission nodes, action guards or provider integrations | [Permission engineering](../minecraft-development/references/permissions-authorization.md) |
| Official references and evidence limits | [Sources](references/sources.md) |

For legitimate anti-cheat interactions read [anti-cheat engineering](../minecraft-development/references/anticheat-development.md). For modpack/dependency triage read [mod lists](../minecraft-development/references/modlists-compatibility.md). Keep full library loading off the hot path.

## Execute the smallest reversible plan

1. Capture baseline: problem, time window, effective settings, logs/metrics and protected gameplay/security invariants.
2. Back up affected files and state; verify a viable restore point. For live data use a consistent backup process, not a random copy of open region/database files.
3. State exact file/key/current value/proposed value/scope/version evidence, expected effect, gameplay cost, restart requirement and rollback. Do not invent keys, defaults or a universal performance preset.
4. Change one coherent cause at a time. Preserve comments/encoding and unrelated keys; validate syntax and target schema. Permission, punishment, destructive world changes, firewall and downtime actions require the appropriate authorization.
5. Test under comparable load and representative farms, redstone, entities, custom plugins/mods and legitimate player actions. Restart only through the correct approved supervisor; do not use /reload or PlugMan as a general safety shortcut.
6. Verify effective values, startup logs, player access, saving and monitoring. Restore if behavior or security regresses. Report measured results and gaps; never promise zero lag or unlimited players.

## Scope boundaries

Support operational workflows for the four development ecosystems, not every third-party panel/fork/API. Purpur, Folia, hybrid servers, Velocity, bridges, hosts and proprietary plugins require their exact upstream version/support checks. Do not claim NeoForge works with Bukkit plugins. Bedrock Dedicated Server, proxy development, host DDoS mitigation and managed-panel APIs require dedicated sources; Java RCON instructions do not prove Bedrock support. No production command runner, panel automation or automated player punishment is bundled.

## Updated operations workflow

Keep the practical diagnose → plan → back up → approved change → verify flow: exact server/build and logs first, versioned config inheritance, bounded spark evidence, consistent restore points, player-role checks and controlled maintenance. Use the dedicated guides rather than a generic ready-made settings bundle. Avoid automatic PlugMan reloads, copied JVM flag packs, relaxed anti-cheat thresholds, mandatory plugin lists and assumed Bedrock RCON. These require target-specific justification, not legacy defaults.

## User-visible handoff

Follow the core concise-output rule. Report the result, any pending restart/approval and only essential safety or verification gaps. Do not publish the internal configuration ledger, command inventory or “X instead of Y” comparison unless requested or needed for an informed decision. Keep operator escalation, player punishment, downtime and data-loss warnings explicit.
