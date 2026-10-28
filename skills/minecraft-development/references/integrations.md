# Optional API integrations — verified entrypoints, narrow adapters

These are integration playbooks and upstream lookup points, **not bundled libraries, pinned versions or precompiled adapters**. Resolve actual Minecraft/platform/library compatibility before implementation. Add only the integration requested or already used in the repository. Prefer public APIs over commands, reflection and scraping another plugin's data files.

## Common integration contract

1. Establish required versus optional dependency and exact supported API range.
2. Add a compile-time API scope and intentional runtime requirement; do not shade the host plugin/mod/API blindly.
3. Isolate optional classes behind a loader-safe boundary. Check installed identity and compatible version before loading that boundary.
4. Verify callback threads, mutable-object ownership, cancellation, resource lifetime and reload semantics.
5. Preserve legitimate behavior when absent; required dependency failure must be explicit. Avoid silent empty/default profiles or free purchases.
6. Test absent, supported, incompatible and mid-operation failure states as relevant. Report untested combinations.

## Permissions: LuckPerms

Use the maintained [LuckPerms developer API](https://luckperms.net/wiki/Developer-API), not a historical GitHub revision's old package/version. Obtain the API through the documented provider/service mechanism at the correct lifecycle. Understand cached/loaded user data, contexts and effective permissions; do not assume a group name is a complete permission check.

Callbacks/events may be asynchronous. Return to the owner before touching Bukkit/Minecraft objects. Do not force a blocking user load on the tick thread or retain user/player contexts forever. Keep changes and save/recalculation behavior explicit; a metadata read need not rewrite permissions.

## Economy/services: Vault API

[VaultAPI](https://github.com/MilkBowl/VaultAPI) is a service/API bridge; its presence does not imply an economy provider is available or that every method is thread-safe. Resolve the actual registered service and inspect its contract. Validate response/failure and currency semantics.

For purchases preserve rounding, affordability, inventory capacity and compensation policy. Do not claim a database transaction atomically includes another plugin's balance change. Test provider missing, withdrawal failure, full inventory, disconnect and repeated input. Do not install Vault automatically on a Fabric/NeoForge mod as if it were a loader API.

## Text/placeholder integrations

Use [PlaceholderAPI integration guidance](https://wiki.placeholderapi.com/developers/using-placeholderapi/) when requested. Confirm expansion registration/lifetime, plugin absence, playerless context and callback thread. Avoid slow synchronous DB/HTTP in a frequently expanded placeholder. Cache only if privacy, session and invalidation are correct.

Treat placeholder output as untrusted text at the next boundary. Do not pass player-controlled expansion results directly into privileged MiniMessage/click-to-run templates or commands. Be explicit about intended trusted operator formatting versus user data.

Adventure on Paper is not automatically available in every other runtime. [Adventure's modded platform guide](https://docs.papermc.io/adventure/platform/modded/) documents separate platform/version integration, including old/new Loom eras. Do not add its shared-platform artifact to a single-loader project unless actually needed.

## Protection/regions/world editing

Use [WorldGuard's developer API](https://worldguard.enginehub.org/en/latest/developer/) for region/flag policy and matching WorldEdit types where required. Verify the actor, world, region query, bypass/context and flag combination semantics; “inside a region” is not synonymous with “may build.” Respect another plugin's event cancellation.

Do not mutate worlds asynchronously or bypass ownership because a protection query succeeded. Large edits still need budget, cancellation and verified platform APIs. World editing/deletion is not authorized by merely installing this skill. Test overlapping regions, boundary positions, no-player/console context and optional integration absence.

## Protocol/packets

[ProtocolLib](https://github.com/dmulloy2/ProtocolLib) and [PacketEvents](https://docs.packetevents.com/) are alternative protocol integration choices, not libraries to install together by default. Inspect exact server/client protocol support, packet direction/phase, callback thread, wrapper lifetime and per-version fields.

Use public high-level APIs when sufficient. Packet cancellation/transformation can affect other plugins and anti-cheat; preserve legitimate traffic, bound work and validate server authority. Do not retain reusable packet/event wrappers into delayed tasks without a documented copy. Never advertise all protocols because a listener registered.

## Mod list/configuration UI

[Mod Menu](https://github.com/TerraformersMC/ModMenu) offers a Fabric mod list and API for config-screen integration. The maintainer README documents implementing `ModMenuApi`, a `modmenu` entrypoint and a config screen factory; inspect the exact target's types/signatures. This is client UI, not a required dedicated-server dependency or loader dependency resolver.

[Cloth Config](https://shedaniel.gitbook.io/cloth-config/) builds configuration screens; it is not synonymous with Fabric's loader, a universal storage format or an authoritative server configuration sync. Keep screen classes client-side. Respect parent-screen navigation, validation, cancel/save behavior and runtime optional dependencies. Check loader variant and game version; do not copy unrelated old “Cloth API” modules.

For NeoForge use the target loader's own mod-list/config screen extension where available; verify exact hook and constructor. Do not import Fabric Mod Menu classes into NeoForge. See [mod list workflow](modlists-compatibility.md).

## Recipe viewers: JEI, EMI and requested alternatives

Use [JEI's maintainer wiki](https://github.com/mezz/JustEnoughItems/wiki) or [EMI's maintainer wiki](https://github.com/emilyploszaj/emi/wiki) for the requested viewer/version. Other viewers, such as REI, require their own official exact-target documentation rather than pretending these APIs are interchangeable.

Separate client recipe display from authoritative server recipes. Register categories, displays, catalysts/input/output and transfer handlers according to the chosen API, without changing server crafting behavior. Test tags/components, dynamic reload, missing viewer and full/partial inventory transfer. Do not implement a viewer button that grants server output without validation.

Keep optional viewer/client classes out of server load paths. Avoid duplicated recipes from multiple registration mechanisms. A rendered recipe is not proof its server serializer, ingredients or transaction works.

## Multi-loader abstractions

[Architectury metadata/platform APIs](https://docs.architectury.dev/api/platform/mod/) can unify some operations in an existing multi-loader project. They do not erase loader lifecycle, capability/transfer, renderer, event or version differences. Do not introduce Architectury for a single optional mod-presence check when the native loader API suffices.

## Unknown/custom APIs

For any requested API not listed here, inspect its official maintained source, license, exact supported target/version, lifecycle, thread model, build/runtime dependencies and public contract. Add a small isolated integration and tests rather than inventing methods. Explicitly state what is unverified. This extension procedure is the support path for the open-ended ecosystem; it is not an “all APIs already implemented” claim.
