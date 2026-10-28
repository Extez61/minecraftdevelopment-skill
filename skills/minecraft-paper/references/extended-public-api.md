# Paper extended public API lookup playbooks

These are version-qualified procedures, not declarations that each API exists on the full 1.21.1–26.2 interval. Start with the [official API index](https://docs.papermc.io/paper/dev/api/) and the project's resolved source/Javadoc. Do not introduce an experimental/new API when a stable baseline API meets the request.

## Registries and lifecycle-managed registration

Determine whether a registry supports the requested read/modification and at which lifecycle point. Use supported public registration events/builders for the exact target; do not mutate frozen registries late or replace internals through reflection casually.

Keep stable keys, data-pack precedence and user overrides. Existing worlds/items can reference entries across updates; metadata/key changes need migration reasoning. Do not assume a lifecycle hook runs at the same time as classic onEnable. Bootstrap code must not access a fully running world prematurely.

## Dialogs, resource packs and client-facing UI

Modern dialog APIs are a later-version feature; do not import them into a minimum 1.21.1 module without an isolated actual compatibility strategy. Check available client/server feature support and callback identity, permission and lifecycle.

Resource-pack push/accept/decline/failure behavior is separate from custom protocol/plugin state. Respect user/server policy and documented events. Do not claim a resource pack installs arbitrary Java client mods. A custom font/model reference requires matching actual resources and correct versioned formats.

All UI input is a request. Validate current menu/dialog session, sender, ownership, state, range and permissions on the server. Handle disconnect/close/timeout and repeated response. Use an inventory/chat fallback only if the product requires one; avoid unnecessary universal UI abstractions.

## Plugin messaging and proxy/backend boundaries

Plugin messaging is not the same as a custom Fabric/NeoForge payload API or a private authenticated RPC channel. Verify transport, plugin-channel registration, payload bounds, forwarding assumptions and actual proxy support.

A player/client-reachable channel cannot be trusted to grant admin actions, currency or cross-server identity without a real authentication/authorization protocol. Do not confuse proxy configuration with proof a message is legitimate. Keep protocol encoding/versioning explicit and reject malformed/oversized messages.

Velocity/BungeeCord code belongs in a separate explicitly requested runtime module. Do not run its listeners inside a Paper JavaPlugin or advertise broad proxy compatibility from a backend-only implementation.

## Recipes, particles and entity/chunk APIs

Use supported recipe APIs and stable namespaced keys. Preserve ingredient semantics, recipe remainders and user data-pack overrides. Test a reload/restart and avoid registering duplicate recipes/listeners every config refresh.

Spawn particles/sounds only for intended recipients and locations. Audience reduction is valid only when it preserves behavior. Do not reduce a requested effect's density/range or timing without calling it a tradeoff.

For teleport/chunk APIs check asynchronous completion threads, failure outcomes, tickets, cancellation and entity/world lifetime. Do not `.join()` on the tick thread or mutate world data in the wrong completion context. Folia needs actual owner-aware handling independently.

## Testing

Compile against the actual intended baseline, inspect packaging, and runtime-test registration, optional older-version absence, input validation, disconnect and shutdown. A Javadoc index entry is only a lookup lead, not a compiled API integration.
