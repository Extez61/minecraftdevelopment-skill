# Bukkit scheduling, persistence, shutdown and performance

## Main-thread rule

BukkitScheduler's Javadoc explicitly warns that asynchronous tasks should not access Bukkit API. Use conservative owner-thread access unless the exact API documents an exception. Keep worker code limited to copied primitive/immutable data and independent services.

Pattern: on main thread capture UUID/request/config snapshot and session generation; worker does bounded I/O/computation; main-thread callback checks plugin enabled, current session/player/world and request relevance; apply state. Do not pass a live inventory, event, entity or location that may be mutated concurrently.

`CompletableFuture` completion does not imply the Bukkit thread. Coroutines `Dispatchers.IO`/`Default` do not imply it either. Avoid blocking waits on the main thread, async scheduler misuse and “thread-safe maps” that still hold unsafe game objects.

## Tasks and timing

Own task handles at the relevant feature/session. Cancel countdowns when a match ends and old callbacks when a new round begins. Cancel/rescope entity-related tasks on removal/quit; invalidate delayed work after world unload.

Ticks and wall-clock seconds are not interchangeable under lag. Preserve the feature's clock contract. Use a monotonic source for elapsed in-process timing where appropriate; only use persistent absolute timestamps when offline expiry is intentional.

A single match loop may be simpler than one repeating task per player, but centralizing unrelated tasks into a custom scheduler often adds unnecessary complexity. Profile actual callback frequency and cost before restructuring.

## Configuration

Validate and cache values at a defined boundary. Do not read YAML from disk during every event. Preserve user keys/defaults and migrate explicitly. A safe feature reload parses a complete new config, validates it, then swaps a snapshot; do not partially apply invalid settings.

Do not overwrite operator config on enable. Keep defaults and documentation coherent. A missing required field should produce a clear startup/config error rather than a later null dereference or silent data loss.

## Persistent profiles and transactions

Use bounded I/O and explicit load state. On reconnect reject an old session's load result; do not let a default profile overwrite data before loading completes. Preserve write ordering per key to avoid stale saves winning.

Use prepared statements, transactions, timeouts and a reasonable connection pool where a database is justified. A flat file can be simpler for small settings; it is not automatically suitable for high-write concurrent economy profiles. Choose the smallest system satisfying durability, not a fashionable storage stack.

Do not serialize live game objects on workers. Capture snapshots on the owner and serialize supported stable data. Persist IDs/schema/units explicitly. Handle failed writes, retries, duplicate rewards and shutdown acknowledgments honestly.

## Shutdown

Stop input, cancel owned tasks/scopes, invalidate callbacks, snapshot critical state and drain owned persistence within a bounded policy. Close owned executors/pools/watchers and clear player/world references. Partial startup must also clean up safely.

Avoid waiting for a worker that will call back to the stopped main thread. Avoid fire-and-forget saves reported as successful durability. Explain unfinished writes and recovery to operators without secrets.

## Optimization

Profile hot listeners, repeated scans, sync I/O, message/JSON parsing, scoreboards, chunk loads and allocation. Cache only where invalidation is correct and benefits are measured. Do not reduce scan radius, skip targets, change cooldown intervals or remove checks and call it preservation.

Folia is outside this scheduler model. Do not set a compatibility flag or route entity work to a global scheduler. Use the separate Paper/Folia reference only if Folia becomes an explicit independently tested target.

Source: [BukkitScheduler Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scheduler/BukkitScheduler.html).
