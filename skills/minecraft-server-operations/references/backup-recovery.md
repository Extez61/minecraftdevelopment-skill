# Consistent backups and recovery

Skill creator: extez061

## Define the recovery contract

Agree on recovery point objective (acceptable data loss), recovery time objective, downtime, retention, encryption, access and off-host copies. A successful archive job is not proof of a restorable backup. Identify all worlds/dimensions, playerdata, plugin/mod JARs/config/state, permission/economy/claims databases, datapacks, launcher/runtime versions, proxy state and required secrets. Store secrets separately with restricted access; do not expose them in a public backup/repo.

Prefer a graceful shutdown plus verified database backup for a simple consistent snapshot when downtime is allowed. With an online server, use the target implementation's documented flush/save/pause procedure AND coordinate external databases/plugins. save-all flush alone does not atomically snapshot every file or external database; save-off alone is not a backup. Any temporary save pause requires a bounded operation, failure-safe resumption and verification. Do not emit a one-line cron archive of changing region files and call it transactionally consistent.

Use supported database snapshots/dumps and filesystem snapshot coordination where appropriate. A live SQLite copy may miss WAL state; follow the database's supported backup API/procedure rather than copying only the primary file. Remote economy/permission data needs a consistent recovery point alongside worlds to avoid duplication or entitlement drift.

## Backup procedure

1. Inventory paths, database boundaries, sizes, free space, exact builds and expected service ownership. Check exclusions so worlds/dimensions/plugin data are not accidentally omitted.
2. Plan and approve downtime or coordinated online snapshot; notify players as required. Verify an existing rollback point before experiments.
3. Quiesce/stop through the correct supervisor and verify completion, or execute the reviewed consistent snapshot process. Do not race a running writer.
4. Write backups outside the live world/server tree where possible; avoid recursively archiving previous backups. Record timestamp, versions, file manifest/checksums and consistency method. Encryption/hashes serve different purposes.
5. Confirm archive integrity, database restoreability, expected contents and free space. Copy to controlled off-host storage under the approved privacy policy.
6. Resume normal saving/service, check logs and monitor. Alert on failed/late jobs, not just process crashes. Rotate only verified backup sets according to policy; never delete the last known good restore point automatically.

## Restore drill

Restore into a NEW isolated directory/server first, on compatible exact binaries. Block production webhooks, payments, cross-server messaging and database writes from the test copy; do not accidentally connect staging to production storage. Use private network/ports and approved authentication settings, not an exposed offline-mode server.

Verify world/dimension loading, inventories/ender chests, permissions, claims, balances, plugins/mods and registry content. Test representative login and save/restart; compare critical counts/transactions with the stated snapshot point. Record actual restore duration and uncovered dependencies. A checksum match proves file integrity, not gameplay correctness.

For approved production recovery: stop writers, preserve incident evidence/current state, restore the mutually consistent set, verify ownership/paths/config and start through the supervisor. Reconcile transactions after the restore point; do not replay payments or rewards blindly. Communicate the real data-loss window and monitor closely.

## Corruption and incidents

Do not run world repair, delete region/player files or reset a world on the only copy. Preserve original bytes and logs, diagnose the affected scope and use version-compatible tooling on copies with explicit consent. Partial region/player/plugin restores can create duplication or dangling references; define reconciliation before applying them. Never promise that switching compression or disabling saves repairs corruption.
