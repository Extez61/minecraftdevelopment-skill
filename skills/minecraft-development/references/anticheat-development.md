# Anti-cheat development and legitimate compatibility

Skill creator: extez061

## Scope and target contract

Use for developing defensive anti-cheat features or integrating legitimate plugins/mods with protections on systems the user owns or is authorized to maintain. Do not provide stealth bypasses, client spoofing, concealment or production evasion. Keep protection enabled by default. A legitimate gameplay mechanic needs a documented compatibility path, not a permanent blanket exemption.

Establish exact server and client versions, protocol translation, Java, loader, anti-cheat product/build/API, packet-library version, proxy topology and platform scheduler. Minecraft 1.21.1–26.2 scope does not imply each anti-cheat supports every release or Fabric/NeoForge/Paper/Bukkit combination. A client requirement, server support claim and API availability are separate facts. Record unknown compatibility instead of inferring it from a repository title.

## Integration lookup

- [Grim](https://github.com/GrimAnticheat/Grim) links its official [GrimAPI](https://github.com/GrimAnticheat/GrimAPI). Resolve a matching artifact/build and inspect exact API source. The reviewed current README illustrates typed event channels in API 1.3+ and legacy registrations; do not transplant either style into another resolved version. Preserve incoming cancellation state unless an explicitly approved policy changes it. Do not copy examples that cancel all flags or un-cancel based on free-form text. Determine callback thread from that exact implementation: async anti-cheat is not a license to access Bukkit worlds from packet threads.
- [NoCheatPlus](https://github.com/NoCheatPlus/NoCheatPlus) and its linked [API documentation](https://github.com/NoCheatPlus/Docs/wiki/API) are legacy lookup references, NOT evidence of 26.2 support. Identify the deployed fork/maintainer/build before using modern examples or exemptions. Do not choose an abandoned artifact merely because its name matches.
- For other products, including proprietary ones, use the actual vendor's versioned developer documentation and license. Do not invent events, Maven coordinates or exemption methods. Prefer public integration surfaces over reflection/internal check mutation.
- PacketEvents/ProtocolLib supply packet infrastructure, not an anti-cheat verdict. Load only the correct dependency and verify protocol coverage; follow [integration playbooks](integrations.md). Fabric and NeoForge packet hooks are loader-specific, not Bukkit listeners.

This package does not bundle anti-cheat code, proprietary SDKs, working compiled adapters or pretested settings. API lookup support is not proof that a product runs on the selected server.

## Owner-thread and lifecycle architecture

Separate bounded packet parsing/snapshots, pure calculations, owner-thread world decisions and audited enforcement. Verify order guarantees for each connection; do not use a global parallel stream over live players. Queue immutable identity/session/generation data, not pooled packet wrappers or mutable player/world objects. Return owner-thread changes through the platform scheduler; on Folia use the appropriate entity/region owner, not a universal main-thread assumption.

Reject delayed results after logout, reconnect, teleport, respawn, world change or shutdown. Register optional integration only after its runtime dependency is ready. Isolate classes so the server can boot without optional anti-cheat libraries. Unregister listeners, cancel work and clear bounded state on disable; define reload support explicitly. Kotlin coroutines must have an owned cancelled scope and cannot bypass game-thread rules.

## Movement and legitimate mechanics

Model the actual protocol/game release and known server-authorized state. Consider velocity/knockback, teleports and confirmations, vehicles, fluids, climbable blocks, collisions, effects/attributes, gliding, flight permissions, world borders, portals, chunk transitions and custom mobility. Distinguish tick time, monotonic elapsed time, RTT/jitter and server stalls; do not use wall-clock jumps as a cheating signal. Packet count alone is not a trustworthy timer verdict.

An integration that launches/dashes/teleports players should use normal server-authoritative APIs and the product's documented scoped compatibility mechanism if available. Bind any approved exemption to identity, specific mechanic/check, narrow duration and cleanup; audit and expire it even on failure. Never expose a client-triggered exemption endpoint or disable all checks to solve one false positive. No generic exemption API signature is assumed here.

Translation layers and Bedrock bridges can change observable semantics. Verify the exact supported integration and policy. Do not classify bridge clients as cheating or promise equal check coverage when upstream intentionally exempts them.

## Combat and interaction checks

Use server-known participants, dimensions, permissions, line of sight, target validity and the applicable reach/attack/attribute semantics. Entity positions are temporal observations; account for justified interpolation/latency only with a bounded version-correct design. Do not store unbounded player history. Validate block placement/breaking and inventory actions against actual world/menu state. Avoid a universal hard-coded numeric threshold copied from another game release.

Separate a check observation, suspicion/confidence accumulation, cancellation/setback and punishment. Define repeated-input behavior and idempotence so retries cannot duplicate penalties or rewards. Do not equate one anomalous packet or one timing sample with a proven cheat. Establish decays, tolerances and the evidence required for each action in the user's approved policy. Keep severity and units explicit.

## False-positive handling and rollout

Start new uncertain checks in observation mode on an authorized staging server. Build legitimate-mechanics regression fixtures before enforcement. Record minimal structured observations: check/build, protocol, server timing, reason, relevant mechanic/session and measured values. Redact private identifiers where possible and restrict staff access. Bound log rate/retention; do not dump packet payloads, IPs or player inventories into shared reports by default.

Review representative flagged and unflagged samples with labels; retain denominators and distinguish precision, missed detections and false-positive rate. Do not claim statistical accuracy from synthetic tests or unlabelled production flags. Policy changes need review, rollback and clear communication; do not silently change ban thresholds during a performance refactor.

## Performance without weakening protection

Set per-player and global bounds for queued work, history, parsing and logging. Use cheap early validation before expensive checks; avoid blocking I/O, HTTP/database calls, stack traces, allocations and repeated metadata resolution in a packet hot path. Cache only stable versioned facts with explicit invalidation. Profile CPU, allocation/GC, queue depth, p95/p99 check latency and tick impact under a stated workload.

When overloaded, apply an explicit reviewed backpressure policy; do not silently drop evidence then assert checks ran. Never reduce detection coverage, remove checks, broaden exemptions or suppress alerts merely to report lower CPU. Compare the same workload/check configuration before and after; re-run false-positive and detection fixtures as well as performance tests.

## Verification matrix

Test each claimed server/client/product/API tuple, with and without optional integration, and on dedicated server where applicable. Include normal movement/combat, each custom mechanic, permission changes, packet fragmentation/invalid bounds, loss/jitter/stalls, reconnect, death/respawn, teleport/world switch, vehicles, translation/bridge behavior, disable/re-enable and concurrent users. Use authorized local synthetic fixtures for invalid input, not live evasion clients or public-server testing.

Prove functional invariants and legitimate-play false-positive regressions; compile/artifact checks alone are insufficient. Preserve a minimal replay/fixture when lawful, isolate protocol fixtures from personal data and verify deterministic ordering. If runtime or an anti-cheat license is unavailable, state the gap. Handoff: supported tuples actually tested, unchanged enforcement policy, commands/results, measured costs, unresolved compatibility and rollback. Never label this guide universally anti-cheat compatible.
