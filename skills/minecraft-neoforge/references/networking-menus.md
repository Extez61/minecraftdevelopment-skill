# NeoForge payloads, physical/logical sides and menus

## Side separation

A physical client includes a logical client and may host an integrated logical server. A dedicated server cannot link client-only Minecraft/rendering classes. Use supported client initialization/subscription boundaries and source organization; do not hide a client class behind a late `if` after it is already eagerly loaded.

Register shared gameplay safely for both dedicated and integrated servers. Keep rendering, screens, key mapping and client-only integrations out of common static fields, method signatures or Kotlin object initialization paths that cause linkage.

## Payload registration and handler semantics

The 1.21.1 docs use `RegisterPayloadHandlersEvent`, `PayloadRegistrar`, typed `CustomPacketPayload` and `StreamCodec`. Register on the event's correct bus, choose direction/phase/protocol version, define bounded codecs and verify both peers understand the payload.

The versioned 1.21.1 payload page documents **main-thread handling by default**, with `executesOn(HandlerThread.NETWORK)` for network-thread handlers and `enqueueWork` for handing work to the game thread. Do not repeat the generic outdated assumption that every NeoForge handler starts on the network thread. Inspect the actual selected target and registrar configuration.

Conversely, main-thread default is not a license to block with HTTP/DB or heavy computation. Network-thread handling must not access live gameplay state or block the Netty event loop. Capture/decode bounded data, perform only appropriate short work, and use a bounded executor for expensive independent work with a validated owner-thread continuation.

Registration configuration methods can return a modified/new registrar rather than mutating the old instance; use the documented chaining/assignment pattern. Confirm exact-version source before relying on an example.

## Payload design

Keep IDs stable and codecs explicit. Enforce maximum string/collection/nesting/byte sizes; validate value ranges, finite numbers and unknown IDs. Match field order/type on both ends and decide how incompatible protocols fail.

Derive sender from context. Validate dimension, distance, ownership, current menu/session, permission, cooldown and current world/recipe state before applying. Do not let clients submit arbitrary NBT/items/reward amounts as authority. Revalidate after async work or scheduling delays.

Use the correct packet distribution audience: tracking players, a single player, relevant dimension or another intentional scope. Avoid global broadcasts for local state and unchanged full-state packets each tick. Define initial sync, late join and a resync path when deltas are used.

## Menus and screens

Register the menu type and client screen according to the target lifecycle. Server menu code owns inventory/transactions; screen code draws and sends requests. Keep client-only screens off server classpaths.

Validate opening data, block position/entity identity, distance and `stillValid`-style semantics as implemented by the actual API. Menu IDs and button IDs must be checked against the live server container/session. Test shift-transfer slot boundaries, remainders, full inventory, cursor and close/disconnect.

Small progress integers may fit an existing menu data mechanism, but inspect bit width/sign/precision and target contract. Do not silently truncate a large energy value or leak private state. Use custom payloads only when the existing sync cannot correctly carry the needed state.

Do not duplicate authoritative inventory state in a client attachment and trust it on purchase. Client visuals may be stale; server checks must be definitive. Reject replayed/stale input rather than relying on a disabled button.

## Entity/attachment synchronization

Saving data and syncing data are separate responsibilities. Test spawn/tracking, late join, dimension changes, death/clone, removal and reconnect. On supported newer attachment APIs, verify actual sync audience and copy policy rather than assuming all viewers receive every field.

Distinguish network entity IDs from durable UUIDs. Capture session/generation for async results and clear server/client caches at their real lifecycle end.

## Kotlin-specific pitfalls

A `suspend` handler is not automatically compatible with a Java functional interface; register an explicit supported callback and own the coroutine scope if needed. Do not suspend while holding game objects/locks across ownership changes. `Dispatchers.IO` does not return to a Minecraft owner thread after a DB call without an explicit verified dispatcher/bridge.

Sources: [1.21.1 networking](https://docs.neoforged.net/docs/1.21.1/networking/), [1.21.1 payloads](https://docs.neoforged.net/docs/1.21.1/networking/payload/). Recheck newer targets independently.
