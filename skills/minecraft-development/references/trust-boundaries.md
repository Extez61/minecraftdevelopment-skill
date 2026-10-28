# Trust boundaries and abuse-resistant gameplay

Treat clients, command arguments, item text, packets, external service responses and operator-provided configuration as inputs requiring appropriate validation. A client keybind, menu button or visually disabled widget is not authorization.

## Server-authoritative actions

For every client-to-server request validate identity from the authenticated connection; do not trust a claimed UUID. Validate direction, protocol phase/version, payload bounds, player alive/connected state, dimension, distance, ownership, permission, inventory/session identity, cooldown and current game state. Revalidate critical conditions on the owning thread immediately before mutation.

Never accept a client's proposed reward, price, damage, arbitrary block entity inventory, teleport destination or serialized object as authoritative. Derive effects server-side. Reject impossible or stale requests without crashing the server. Rate-limit abuse with bounded per-connection state and cleanup; avoid a global lock that becomes a new denial-of-service bottleneck.

## Bounded codecs and parsing

Bound strings, arrays, nested containers, item counts, coordinates and packet size before expensive allocation. Validate counts/ranges after decoding too. Use the platform's typed payload/codec system for the target version. Do not deserialize arbitrary Java objects or polymorphic types supplied by players. Do not decompress unbounded payloads or trust a declared length.

Network-thread handlers must not block on external I/O or execute heavy unbounded work. Keep decoding small; send expensive independent work to an appropriately bounded executor and apply results through a validated owner-thread handoff.

## Commands and text

Check permission in the actual execution path, not only tab completion. Validate console/player-specific access. Parse arguments explicitly and reject negative, non-finite, overflowing or out-of-range values when invalid. Do not use player-controlled strings as shell commands, SQL syntax, file paths or format templates.

For Adventure/MiniMessage, insert untrusted player text as an unparsed/text component or a deliberately restricted resolver. Do not let a player name or chat message introduce click-to-run commands or privileged styling. Preserve intended admin formatting separately from user input.

## Inventory and economy

Identify a custom menu by an owned holder/session, not just a title. Handle drag, shift transfer, number-key swap, offhand, double-click collection, cursor state, creative behavior and stale close callbacks. Recheck session and item identity before granting rewards. Do not trust lore as an authority marker; use supported stable metadata.

Treat purchases, item consumption and rewards as state transitions with explicit failure handling. Test full inventory, disconnect, retries and duplicate input. Audit money rounding and overflow. Reject replayed operations where a repeated packet could mint items or currency.

## Files, services and operational safety

Keep generated/exported paths inside an authorized root; normalize and check containment, and consider symlinks where relevant. Never recursively delete a path derived from a world name or player input without explicit validation, ownership and authorization.

Use parameterized SQL, TLS and timeouts for external services. Keep secrets out of source, JARs, logs and generated reports. Do not upload logs, profiles, source or worlds without authorization. Back up config/saves before migrations; never disable authentication, permissions or security requirements to make development convenient.

## Compatibility and failure behavior

A missing optional integration should disable only the dependent feature, not crash classloading. A required dependency should fail startup with a clear actionable message. Do not swallow a dependency error and run with corrupt defaults. Keep class references to optional libraries behind a verified load boundary; merely checking “plugin installed” after class initialization is too late.
