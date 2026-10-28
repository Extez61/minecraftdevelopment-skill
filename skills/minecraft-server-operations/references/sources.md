# Operations sources and verification ledger

Skill creator: extez061

Reviewed official/maintainer material on 2026-10-28. These live pages can describe a different release from the user's server; inspect exact generated configs and release/source documentation before editing. No live game server, RCON command, panel, player moderation, restore, profiler session or performance experiment was executed while authoring these guides.

| Source | Verified documentation topic |
| --- | --- |
| [Paper configuration layout](https://docs.papermc.io/paper/reference/configuration/) | Global/default/per-world layout and inheritance; actual dimension paths must be discovered. |
| [Bukkit config](https://docs.papermc.io/paper/reference/bukkit-configuration/) | Spawn/timing/autosave settings and possible Paper overrides. |
| [Spigot config](https://docs.papermc.io/paper/reference/spigot-configuration/) | Activation/tracking and per-world distance defaults; gameplay consequences. |
| [Paper world config](https://docs.papermc.io/paper/reference/world-configuration/) | Autosave/spawning overrides, hopper event suppression and redstone behavior changes. |
| [server.properties](https://docs.papermc.io/paper/reference/server-properties/) | Auth/network/RCON/whitelist and distance properties; target schema still required. |
| [Paper getting started](https://docs.papermc.io/paper/getting-started/) | Java version table and official server launch/download guidance. |
| [Paper updates](https://docs.papermc.io/paper/updating/) | Backups and deliberate plugin/server update workflow. |
| [Paper profiling](https://docs.papermc.io/paper/profiling/) | Profile while the issue occurs; spark entry point. |
| [spark commands](https://spark.lucko.me/docs/Command-Usage) | Bounded profiler commands/options and diagnostic surfaces. |
| [Velocity security](https://docs.papermc.io/velocity/security/) | Firewall/forwarding secret/tunnel boundaries. |
| [LuckPerms usage](https://luckperms.net/wiki/Usage) | Permission/groups/inheritance/contexts and command/editor concepts. |
| [NeoForge server installation](https://docs.neoforged.net/user/docs/server/) | Installer, generated launch scripts and user_jvm_args.txt. |

The Fabric player server-installation page could not be retrieved in fast or comprehensive extraction during this update. Therefore no newly checked Fabric installer command or pinned launcher version is claimed. Use the actual Fabric release/installer instructions and existing platform source index when executing setup. Do not replace failed research with guessed commands.

Backup consistency, least privilege, measurement and rollback procedures are engineering guidance; they are not a platform SDK or a claim every host/panel has identical features. Proprietary panels, forks, bridges and storage backends require their own exact authoritative sources.
