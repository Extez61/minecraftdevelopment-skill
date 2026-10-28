# Small language examples, not platform scaffolds

`java/SessionGate.java` and `kotlin/SessionGate.kt` illustrate the same session-generation pattern. All methods are **owner-thread confined**; these classes are intentionally not advertised as concurrent collections or full schedulers. Keep each instance scoped to a plugin/server lifecycle. Do not share it across platforms/threads without redesign.

On the owner thread call `open(UUID)` when a new session begins. Capture the returned primitive token with immutable request data. A worker never calls this gate. Back on the owner thread, before applying a result call `isCurrent(UUID, token)`; reject stale callbacks. Call `close` on quit and `clear` on stop. Also validate running state, live player/world and permission as appropriate; a token alone does not authorize mutation.

The monotonically increasing token avoids reconnect ABA and is not reset by `clear`. Overflow fails explicitly instead of silently reusing a token. These are pure JVM examples with no Minecraft dependency; they do not supply platform scheduling, durability or runtime registration.

The [Java test harness](../tests/SessionGateJavaTest.java) harness exercises reconnect, close, clear and independent-player behavior if a Java compiler/runtime is available. A [Kotlin test harness](../tests/SessionGateKotlinTest.kt) is also included. QA.md records whether the environment actually compiled/ran them. No version-specific Minecraft build templates are presented as prevalidated projects.
