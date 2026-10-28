# Thread ownership, persistence and lifecycle

## Thread boundary pattern

Use **capture → compute/I/O → validate → apply**, with immutable snapshots at the boundary:

1. On the owning game thread, validate the request and capture only primitive/immutable data, UUIDs and a session generation.
2. Submit bounded I/O/CPU work to an owned executor or scope. Do not retain event instances or live world/player/inventory references for worker use.
3. Complete with explicit success/failure. Preserve per-key ordering or an optimistic concurrency version where writes can race.
4. Schedule application onto the correct owner. Recheck plugin/server running state, player/session, dimension/world, permissions and request relevance.
5. Apply atomically to the extent the platform permits. Discard stale results without discarding a durable write acknowledgment silently.

A `ConcurrentHashMap` protects selected map operations, not the game objects stored in it and not a multi-step business transaction. An atomic integer cannot make an inventory exchange atomic. `CompletableFuture.thenAccept` may run on the completing thread; an explicit executor/scheduler is required at the game boundary.

## Platform ownership

- Conventional Bukkit/Spigot/Paper: assume gameplay API access belongs on the server thread unless exact documentation explicitly permits otherwise.
- Folia: use entity ownership for moving entities, region ownership for location-bound state, global scheduling for global tasks, async scheduling for independent work. Global does not mean permission to access arbitrary regions.
- Fabric/NeoForge: distinguish physical environment from logical side. Use the documented server/client executor and event/payload handler semantics for the exact API.
- Client rendering: obey the renderer's thread/phase and lifecycle; worker-safe extraction data is not permission to mutate game state during drawing.

Do not create an async loop around a synchronous chunk/world API. Do not perform external HTTP, blocking JDBC, filesystem scans, sleeps or `.join()`/`.get()` waits in a hot tick or render callback. Tiny platform-mandated synchronous config reads during controlled startup differ from unbounded runtime disk work; assess cost and lifecycle rather than inventing a universal ban.

## Persistence model

Choose the simplest storage that matches durability and workload:
- small operator-editable settings: validated platform config;
- item/entity metadata: supported PDC, components or attachments for the platform;
- level-level mod state: supported saved-data API;
- durable profiles/economy across sessions: a repository with explicit transaction semantics;
- cross-server state: only introduce distributed storage when required.

Store UUIDs and stable namespaced IDs, not display names or ordinal enum positions. Keep schema versions, units and precision explicit. For currency use the integration's established semantics; where designing anew, prefer integer smallest units or deliberate decimals, not accidental floating-point rounding.

Never reset malformed data to an empty “successful” state without reporting and a recovery policy. Preserve a corrupt copy for diagnosis when safe. Missing new optional fields may use documented defaults; malformed critical inventory/economy state should fail safely.

## Safe saves

For standalone files, write a temporary sibling, close/flush according to durability needs, then use an atomic replacement if supported; keep backup/recovery behavior explicit. Atomic rename alone is not a complete power-loss durability guarantee. For SQLite, consider its concurrency/locking behavior and transaction scope instead of assuming a large pool improves throughput.

For JDBC use parameterized statements, bounded pools, timeouts and transactions. Never build SQL by concatenating player input. Save snapshots, not live world objects. Bound pending write memory; choose batching/coalescing only if intermediate writes are not required events.

Protect against stale overwrites: serialize operations per profile/key, use row versions/compare-and-set, or define a transaction strategy. “Last completion wins” is usually wrong when an older write finishes after a newer one. Idempotency keys can protect legitimate retry behavior, especially rewards and externally triggered operations.

Do not claim exactly-once across a database, player inventory and external economy service without a real protocol. Describe crash windows and compensation. A transaction in one database cannot atomically commit another plugin's in-memory balance.

## Load/quit/reconnect races

Capture a session token on join. If a player disconnects and reconnects before an old load finishes, reject application to the new session. Decide whether actions are blocked until load succeeds; never allow a default zero profile to overwrite an existing one during an incomplete load.

On quit, snapshot on the owner, submit the save, clean transient UI/task state, and retain durable save tracking until completion. Avoid duplicate rewards or disconnect exploits. Define retries and user/operator reporting on failure.

## Reload and shutdown

Do not promise safe `/reload`, PlugMan reload or loader hot swapping. Prefer a restart for code changes; implement a feature-specific configuration reload only when designed and tested.

For config reload: parse and validate a complete new snapshot, then swap it at a safe point. Do not partially mutate live settings. Preserve the old valid config on failure. Invalidate derived caches deliberately; prevent duplicate listeners/tasks.

For shutdown: stop accepting new work; invalidate session callbacks; cancel timers/scopes; snapshot required state; drain important queued writes under a bounded policy; close owned resources in dependency order. Avoid scheduling essential game-thread work after the server/plugin stops. Log unfinished writes and recovery details without credentials.

World unloading invalidates world-owned references and tasks. Integrated server stop/start in one client process is a real lifecycle boundary: clear per-server static state rather than assuming process exit. Resources such as GPU buffers, file watchers, sockets, database pools and executors need explicit owners and terminal cleanup.
