# Permission implementation and authorization

Skill creator: extez061

## Pick the permission system, not just a node string

Read the exact platform, command model, game/API/provider version and existing access contract. Distinguish defining permission metadata, checking effective access, granting persistent roles and authorizing one action. A node in a file does not secure an event, GUI button, packet, service method or alternate command entry point. Enforce on the authoritative server at every externally reachable mutation boundary. Permission is necessary but may not be sufficient: validate ownership, target, world, current session, limits and transaction state too.

Use stable lower-case namespaced nodes, for example `exampleplugin.command.status`, `exampleplugin.command.reload`, `exampleplugin.manage.others` and narrowly scoped bypass nodes only when required. Do not silently rename existing nodes or change defaults. Separate self versus other-player actions and ordinary versus administration capabilities. Grant no wildcard, OP or administrative node automatically. A third-party prefix, scoreboard team, display name or client-supplied rank is not authoritative permission evidence.

## Bukkit / Spigot / classic Paper descriptor

For the classic `plugin.yml` model, declare nodes, explicit defaults and intentional child relationships. Synchronize command declarations with code and resources. `true`, `false`, `op`, `notop` have different meanings; use least-privilege defaults appropriate to the existing policy. A dotted name does not automatically create a parent/child grant. Wildcard-looking names are not a portable automatic wildcard implementation; declare intended children or verify provider semantics. Adding `default: true` to an administrative parent can unexpectedly grant all declared children.

Minimal descriptor fragment (merge into the existing classic descriptor; not a complete plugin):

```yaml
commands:
  examplestatus:
    description: Show allowed status information
    permission: exampleplugin.command.status
permissions:
  exampleplugin.command.status:
    description: View non-sensitive status
    default: true
  exampleplugin.command.reload:
    description: Reload this plugin's supported configuration
    default: op
  exampleplugin.admin:
    description: Administrative features
    default: op
    children:
      exampleplugin.command.reload: true
```

These defaults are an example policy, not permission to change a deployed server. If administration must require explicit assignment even for OP, use an approved `false` default and account for provider/plugin OP behavior. Inspect exact generated resources in the final JAR. `paper-plugin.yml` and Paper command lifecycle registration are a different model: do not paste classic `commands` into them and assume registration. Verify that model's actual permission metadata and registration APIs.

Check `sender.hasPermission("exampleplugin.command.reload")` or the target platform's actual equivalent before the action. Do not substitute `isPermissionSet`: it asks about an override, not whether effective access is granted. Do not use `isOp` as a replacement for a narrow capability node. Respect console, command blocks, proxied senders and player-only constraints intentionally; never cast every sender to Player.

Java guard fragment, inside an existing authorized command/action handler:

```java
if (!sender.hasPermission("exampleplugin.command.reload")) {
    sender.sendMessage("You do not have permission.");
    return true;
}
// Continue with validated arguments and the supported reload transaction.
```

Kotlin equivalent fragment:

```kotlin
if (!sender.hasPermission("exampleplugin.command.reload")) {
    sender.sendMessage("You do not have permission.")
    return true
}
// Continue with validated arguments and the supported reload transaction.
```

These illustrate classic boolean command handlers; use the correct return contract in other APIs. Do not replace a plugin's Adventure/localization system solely for this example. Tab completion and command-tree visibility improve UX but do not secure GUI/packet/service paths. Avoid leaking restricted targets in suggestions.

For temporary `PermissionAttachment` grants, track the attachment/owner/session, exact lifetime and removal on expiry/quit/disable. They are runtime grants, not durable rank storage. Avoid repeated attachment creation or permission recalculation per tick; verify default/negative/child/provider interactions and target thread ownership. Do not delete another plugin's attachments.

## Fabric

Vanilla operator permission levels and Brigadier requirements are not automatically named-node provider permissions. Use exact-version command APIs for the project's mappings; do not guess a Yarn/Mojang/26.x method from a different release.

The maintained [fabric-permissions-api](https://github.com/lucko/fabric-permissions-api) is a separate API, not built-in Fabric API or a permission manager. Its [usage guide](https://github.com/lucko/fabric-permissions-api/blob/master/USAGE.md) documents `Permissions.check` and `Permissions.require`, explicit boolean/level fallback policies and asynchronous offline UUID checks. A compatible provider is needed for administrator-configured nodes. Choose whether the dependency is required/included or genuinely optional; preserve metadata and loader-safe class boundaries. Do not shade a manager into a mod to obtain permission checks.

The reviewed version matrix lists 0.3.1 for 1.21.1-or-earlier and 0.7.0 for 26.1, and explicitly changes `modImplementation` to `implementation` at 26.1. These are observed upstream entries, NOT a tested 26.2 selection; verify current coordinates, mappings and artifact compatibility. Upstream snippets mix version-era naming: compile against the actual resolved source rather than copying them verbatim.

Choose a deliberate fallback when no provider answers: a narrow operator requirement or explicit denial for sensitive capabilities, not unconditional allow. Do not convert an explicit denial to a fallback grant. Check command requirements and execution entry points; validate gameplay packet permissions server-side. Offline future results must not block server/tick/packet threads with join/get; return to the correct owner and revalidate current session/context before a game mutation.

## NeoForge

For NeoForge 1.21.1, reviewed upstream source exposes typed `PermissionNode`, `PermissionAPI.getPermission` / `getOfflinePermission`, and registration through `PermissionGatherEvent.Nodes`. Reuse the registered node instance, define type/default resolver and dynamic context intentionally, register on the exact documented event bus/lifecycle, and verify the active permission handler. The source rejects unregistered nodes. Do not query before handler initialization or assume node name hierarchy/wildcards automatically work.

Node APIs and initialization can change: inspect exact target source for 26.x, not legacy Forge `PreInit` examples. A typed permission result is not always a boolean. Server-side command/action guards must use the resolved API and appropriate fallback. Do not replace the server's active handler merely to add one node. Avoid blocking offline/provider queries or calling game APIs from provider callbacks without a documented thread contract.

## LuckPerms integration and persistent changes

For ordinary Bukkit/Paper feature checks, prefer the existing platform's effective hasPermission path; a direct LuckPerms API dependency is unnecessary unless the feature genuinely needs provider-specific data/context/mutation. If it does, resolve a matching API as compile-only/provided, obtain the available service/provider at the right lifecycle and isolate optional classes. LuckPermsProvider access can fail when the API is unavailable. Test absent/incompatible/disabled provider behavior.

Use the cached permission data with QueryOptions for the correct world/server/context. Offline users are not guaranteed loaded; load asynchronously when needed, with bounded work and error handling. Do not treat a raw node list, group name, primary group or prefix as the effective permission result. Preserve true/false/undefined semantics and intentional fallback; an explicit deny is not a reason to use a more permissive path.

For authorized persistent grants/revocations, use documented node/user mutation plus saving, or the matching modifyUser lifecycle; setting an in-memory value alone is not a confirmed durable update. Account for temporary expiry, contexts, inheritance and multi-server messaging. Do not grant a broader parent to repair one missing node. Report success only after the relevant operation completes; preserve existing memberships and unrelated nodes.

LuckPerms documents thread-safe API operations and asynchronous events. That does NOT make all Bukkit/NeoForge/Fabric world/player calls safe from those callbacks, nor does it prove every other provider has the same guarantees. Schedule actual game changes to the platform owner and revalidate authority/session after delays. Do not cache permission decisions indefinitely; provider cached data already handles much of the work. Any custom cache needs context/identity/expiry/invalidation and denial/revocation tests.

## Required tests and handoff

Test non-OP and OP, explicit allow and deny, unset/default, child/parent relationships, alternate entry points, console/player restrictions, relevant world/server contexts, temporary expiry, provider absent, reconnect, permission revoked during async work, restart persistence for grants, and optional dependency classloading. Denied actions must have no side effects. Include both Java/Kotlin build/resource checks for the actual project, not merely a YAML parse.

Expose a short permission-node table in user documentation when a feature needs it: node, purpose, default and scope. Do not emit a long access-control essay after every edit. Keep detailed evidence in the appropriate existing logs/tests; show important failures and pending approvals clearly. Examples here are guidance fragments, not compiled platform adapters or a live permission-system test.
