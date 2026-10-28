# Setup, maintenance, updates and deployment

Skill creator: extez061

## Provisioning

Use official release/installer sources, exact game/build/loader/modpack versions and documented Java requirements. Verify hashes/signatures where supplied. Do not fetch arbitrary mirrored server JARs, upload credentials or accept license/EULA terms for the owner automatically. Record the service working directory, account, paths, world ownership, listening ports, supervisor and backup location. Use a non-privileged dedicated service identity where the host supports it.

Paper/Spigot plugins and Fabric/NeoForge mods are different ecosystems; do not promise hybrid compatibility. Choose a server implementation for required semantics, not merely the highest benchmark. Paper/Purpur/Folia switches require exact plugin/platform validation; Folia needs region-aware support. Existing launcher/build scripts take precedence over a generic `java -jar server.jar` guess.

NeoForge's reviewed install flow uses its installer with --installServer and generated run.sh/run.bat plus user_jvm_args.txt; match the exact release and do not replace the generated argument-file launch chain with a guessed single-JAR command. Fabric server launcher, Loader, Minecraft and Fabric API dependencies must match the actual selected releases. A client modpack is not automatically a server pack; verify dedicated-server side requirements before removing or adding mods.

## Change management

Inventory current JAR versions/hashes, configs/data dependencies, permissions, datapacks/resource packs, worlds, launch args and database schema. Stage one coherent update with rollback artifacts and a maintenance window. Review upstream release notes, compatibility/license and migrations. Test login, permissions, economy, gameplay, cross-world/proxy transfers, save/restart and shutdown before production. Do not automatically chase latest snapshots or update every dependency during an unrelated fix.

Plugin dependency metadata and ordering are not the same as runtime compatibility. Keep only one intended version of a plugin/mod, but do not delete suspicious duplicates without ownership review. A missing dependency or client-only class error requires exact metadata/source diagnosis, not random JAR removal. Use the mod-list guide for evidence; metadata alone is not a passed boot test.

## Restart/reload policy

Prefer the documented graceful stop/start through the actual supervisor (systemd, container, panel or shell). Announce an approved maintenance window and ensure save/shutdown completion. Avoid a shell loop that starts a second process or ignores a failing startup. Set restart backoff and alerting; do not create an infinite crash loop. A forced kill is a last resort for a genuinely stuck process, with data-loss risk and specific authorization.

Do not use Bukkit /reload, PlugMan or arbitrary classloader hot reload as a general update strategy. It can leak tasks/listeners/classloaders and corrupt state; only a product's explicitly supported narrow reload procedure applies, after verifying its restrictions. Datapack/resource reload and plugin reload are different actions. A config edit marked restart-required remains pending until the restart occurs.

## Updates, migrations and recovery

Back up a consistent complete state before changing a server/game/loader version. Test restore on an isolated copy. World upgrades can be one-way; an old binary cannot safely open an upgraded world simply because it starts. Roll back the binary AND corresponding worlds, plugin/mod data and database snapshot, or follow a verified migration/reconciliation procedure. Never downgrade the only copy.

Document datapack/resource-pack formats, mod registry and dimension IDs, enabled features, config schema and plugin storage migrations. Do not remove content mods/dimensions or regenerate chunks on the production save to troubleshoot. Preserve region/player/POI/entity relationships. Large edits, pruning and regeneration need mapped bounds, backups, dry-run preview, explicit approval and staging validation.

Host/panel/container changes require the provider's exact supported interfaces. Avoid embedding secrets in launch commands, git, images, screenshots or logs. Never add a generic auto-update job without version pinning, health checks, maintenance coordination and rollback. Automation must be intentionally requested; this skill alone installs no service or scheduled task.
