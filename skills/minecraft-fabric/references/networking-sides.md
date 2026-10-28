# Fabric side safety, payloads and synchronized UI

## Physical and logical sides

A physical client can contain both a logical client and an integrated logical server. A dedicated server cannot resolve client rendering classes. An `environment` metadata field is not a substitute for safe code organization.

Use client source sets/entrypoints and load boundaries for rendering, screens, keybindings and client-only integrations. Avoid client classes in common field types, static initializers, method references or eager Kotlin singleton properties. A guarded call can still fail when the enclosing class is verified/initialized.

Server-authoritative gameplay belongs to the logical server. Client-side effects can be predictive/visual, but persistent rewards, inventories and damage must not be independently executed on both sides.

## Payload implementation workflow

1. Define a small typed payload with a stable namespaced identity and bounded fields.
2. Define a matching codec in common code safe on both physical environments.
3. Register the payload type for the correct connection phase and direction on the sides that need to encode/decode it.
4. Register server handlers in common/server-safe code and client handlers in the client entrypoint.
5. Check whether the peer supports optional payloads before sending when appropriate.
6. Use verified callback threading; avoid redundant or incorrect scheduling. Hand off when the actual API requires it.
7. Validate, mutate server state, then send minimal authoritative results to affected/tracking clients.

The 1.21.1 Yarn-era and 26.2 official-name APIs have different type/method names. Current Fabric docs demonstrate `CustomPacketPayload`, `StreamCodec` and `PayloadTypeRegistry.clientboundPlay/serverboundPlay`; do not paste those names into every old Yarn project. Inspect exact source and imports.

## C2S validation

Derive identity from the network context. Validate player/world, direction, phase, permission, distance, entity/block identity, open menu/session, current recipe/action, cooldown and bounds. Revalidate after any async/suspending work. A client “I clicked recipe 500” is a request, not authority to grant arbitrary output.

Do not let a packet load arbitrary chunks, decode unbounded stacks, traverse enormous areas or allocate based on an unchecked count. Keep network handlers short; never run blocking HTTP/DB work on the network event loop. Use bounded independent work and owner-thread application if such work is necessary.

## Initial sync, deltas and tracking

Define initial state on login/open/tracking and deltas after change. Late join, dimension transfer, entity removal and reconnect must not leave stale state. Use tracking audiences for world/entity-local effects rather than all players.

Do not assume persistence automatically syncs to the client. Separate saved fields from visual fields and document which needs authoritative synchronization. Avoid maintaining conflicting copies in tracked data, menu sync and custom packets unless each has a distinct purpose.

A delta-only protocol needs a resync path. Sequence/generation IDs may help discard stale UI/entity messages when ownership changes. Do not use a network entity ID as a persistent key.

## Menus, screens and input

Keep authoritative inventory/container logic server-side, visual screen state client-side. Verify slot indices, stack movement, quick move/shift-click and close/disconnect. Client button IDs require server-side validation against the active container/session.

Keybindings request an action through a validated route; they do not directly mutate server-only state. Avoid sending a packet on every rendered frame for a held key when an edge/change-driven protocol can preserve semantics. Rate-limit without breaking legitimate input behavior.

For Kotlin callbacks, verify nullability and ownership after suspension. An integrated server test can hide side/thread bugs; always include a real dedicated-server boot for shared mods.

## Error diagnosis

- Unknown payload: inspect type registration, direction, phase and both client/server artifacts.
- Decode failure: compare exact codec field order/types/bounds and protocol versions.
- Client-only `NoClassDefFoundError` on server: inspect common static references and adapter classloading.
- Desync after late join: inspect initial state/tracking lifecycle, not only delta sending.
- Duplicate rewards: inspect both-side execution, duplicate input and transaction ownership.

Source: [Fabric networking](https://docs.fabricmc.net/develop/networking). Always select the documentation/source version matching the project.
