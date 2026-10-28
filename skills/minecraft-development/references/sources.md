# Source index and verification scope

## Quick navigation

[Contents](#contents) · [CC1 — Claude Code skills](#cc1--claude-code-skills) · [F1 — Fabric 1.21 / 1.21.1](#f1--fabric-121--1211) · [F2 — Fabric 1.21.2 / 1.21.3](#f2--fabric-1212--1213) · [F3 — Fabric 1.21.4](#f3--fabric-1214) · [F4 — Fabric 1.21.5](#f4--fabric-1215) · [F5 — Fabric 1.21.6 / 1.21.7 / 1.21.8](#f5--fabric-1216--1217--1218) · [F6 — Fabric 1.21.9 / 1.21.10](#f6--fabric-1219--12110) · [F7 — Fabric 1.21.11](#f7--fabric-12111) · [F8 — Fabric 26.1](#f8--fabric-261) · [F9 — Fabric 26.2](#f9--fabric-262) · [F10 — Fabric porting guide](#f10--fabric-porting-guide) · [F11 — Fabric mapping migration](#f11--fabric-mapping-migration) · [F12 — Fabric networking](#f12--fabric-networking) · [F13 — Fabric setup](#f13--fabric-setup) · [F14 — Fabric project creation](#f14--fabric-project-creation) · [F15 — Fabric template generator](#f15--fabric-template-generator) · [F16 — Fabric Language Kotlin](#f16--fabric-language-kotlin) · [P1 — Paper project setup](#p1--paper-project-setup) · [P2 — Paper userdev](#p2--paper-userdev) · [P3 — Paper plugin.yml](#p3--paper-pluginyml) · [P4 — Paper/Folia support](#p4--paperfolia-support) · [P5 — Paper API index](#p5--paper-api-index) · [B1 — BukkitScheduler Javadoc](#b1--bukkitscheduler-javadoc) · [B2 — InventoryClickEvent Javadoc](#b2--inventoryclickevent-javadoc) · [N1 — NeoForge getting started](#n1--neoforge-getting-started) · [N2 — NeoForge 1.21.1 events](#n2--neoforge-1211-events) · [N3 — NeoForge 1.21.1 components](#n3--neoforge-1211-components) · [N4 — NeoForge 1.21.1 attachments](#n4--neoforge-1211-attachments) · [N5 — NeoForge newer attachments](#n5--neoforge-newer-attachments) · [N6 — NeoForge 1.21.1 capabilities](#n6--neoforge-1211-capabilities) · [N7 — NeoForge 1.21.1 networking](#n7--neoforge-1211-networking) · [N8 — NeoForge 1.21.1 payload registration](#n8--neoforge-1211-payload-registration) · [N9 — Minecraft 26.2 vanilla migration primer](#n9--minecraft-262-vanilla-migration-primer) · [N10 — NeoForge mod files](#n10--neoforge-mod-files) · [K1 — Kotlin for Forge project](#k1--kotlin-for-forge-project) · [K2 — Kotlin for Forge 5.x README](#k2--kotlin-for-forge-5x-readme) · [Additional lookup entrypoints (not independently audited here)](#additional-lookup-entrypoints-not-independently-audited-here) · [Evidence conflicts and limitations](#evidence-conflicts-and-limitations) · [Client interoperability update — checked 2026-10-28](#client-interoperability-update--checked-2026-10-28) · [Link/API/mod-list update — checked 2026-10-28](#linkapimod-list-update--checked-2026-10-28) · [Companion and anti-cheat lookup sources](#companion-and-anti-cheat-lookup-sources) · [Permission implementation sources — reviewed 2026-10-28](#permission-implementation-sources--reviewed-2026-10-28)


## Contents
- CC1: Claude Code installation and skill structure
- F1–F16: Fabric release boundaries, build/mappings, networking and Kotlin
- P1–P5: Paper build, descriptor, mapping eras and Folia
- B1–B2: Bukkit scheduling and inventory contracts
- N1–N10: NeoForge lifecycle, data, networking and 26.2 migration
- K1–K2: Kotlin provider project/branch references
- Additional lookup entrypoints
- Evidence conflicts and limitations

Research check: **2026-10-28**. Links are upstream sources, not vendored documentation.

Use exact resolved target sources for signatures. “Retrieved excerpt” is narrower evidence than full-page/API validation. Dated release posts describe the release at publication; they are not current dependency locks.

## CC1 — Claude Code skills
[Claude Code skills](https://code.claude.com/docs/en/skills)
Installation paths, SKILL.md frontmatter, supporting files, progressive loading. Loaded official docs.

## F1 — Fabric 1.21 / 1.21.1
[Fabric 1.21 / 1.21.1](https://fabricmc.net/2024/05/31/121.html)
Baseline: enchantments, identifiers, paths, teleportation, rendering. Downloaded full article.

## F2 — Fabric 1.21.2 / 1.21.3
[Fabric 1.21.2 / 1.21.3](https://fabricmc.net/2024/10/14/1212.html)
Entity render state, settings and registry requirements, result/recipe changes. Downloaded full article.

## F3 — Fabric 1.21.4
[Fabric 1.21.4](https://fabricmc.net/2024/12/02/1214.html)
Item definition files and model changes. Downloaded and inspected relevant section.

## F4 — Fabric 1.21.5
[Fabric 1.21.5](https://fabricmc.net/2025/03/24/1215.html)
NBT missing/type getters and HUD/GameTest changes. Downloaded and inspected NBT section.

## F5 — Fabric 1.21.6 / 1.21.7 / 1.21.8
[Fabric 1.21.6 / 1.21.7 / 1.21.8](https://fabricmc.net/2025/06/15/1216.html)
Serialization views, rendering/HUD and datagen changes. Downloaded and inspected relevant sections.

## F6 — Fabric 1.21.9 / 1.21.10
[Fabric 1.21.9 / 1.21.10](https://fabricmc.net/2025/09/23/1219.html)
Resource Loader v1, key input and renderer changes. Downloaded and inspected sections.

## F7 — Fabric 1.21.11
[Fabric 1.21.11](https://fabricmc.net/2025/12/05/12111.html)
Final obfuscated line, game rules, environment attributes and migration context. Downloaded full article.

## F8 — Fabric 26.1
[Fabric 26.1](https://fabricmc.net/2026/03/14/261.html)
Java 25, non-remapping Loom, configuration/task changes and API renames. Downloaded and inspected relevant sections.

## F9 — Fabric 26.2
[Fabric 26.2](https://fabricmc.net/2026/06/15/262.html)
GPU backend, registry keys/datagen, GUI/HUD changes and dated tooling recommendations. Loaded full official article.

## F10 — Fabric porting guide
[Fabric porting guide](https://docs.fabricmc.net/develop/porting)
26.1 to 26.2 procedure and links; loaded relevant content.

## F11 — Fabric mapping migration
[Fabric mapping migration](https://docs.fabricmc.net/develop/porting/mappings)
Yarn to official naming, Kotlin migration-tool distinction. Retrieved official search excerpts.

## F12 — Fabric networking
[Fabric networking](https://docs.fabricmc.net/develop/networking)
Typed payload registration, audience/tracking, server validation; loaded relevant content.

## F13 — Fabric setup
[Fabric setup](https://docs.fabricmc.net/develop/getting-started/setting-up)
Java 25 setup baseline; retrieved official search excerpt. Header/prose differ in version emphasis.

## F14 — Fabric project creation
[Fabric project creation](https://docs.fabricmc.net/develop/getting-started/creating-a-project)
Generator/example and version selection; retrieved official search excerpt.

## F15 — Fabric template generator
[Fabric template generator](https://fabricmc.net/develop/template/)
Target version, Kotlin source, Kotlin DSL, datagen/client separation options. Retrieved official search excerpt.

## F16 — Fabric Language Kotlin
[Fabric Language Kotlin](https://github.com/FabricMC/fabric-language-kotlin)
Adapter, dependency metadata and bundled libraries. Retrieved project README excerpts; latest version is intentionally not copied as a universal pin.

## P1 — Paper project setup
[Paper project setup](https://docs.papermc.io/paper/dev/project-setup/)
Official repository, dependency scopes, old/new artifact version format and toolchain. Loaded relevant content; current examples may be newer than 26.2.

## P2 — Paper userdev
[Paper userdev](https://docs.papermc.io/paper/dev/userdev/)
Mapping-era distinctions and no reobfuscation from 26.1. Loaded relevant content.

## P3 — Paper plugin.yml
[Paper plugin.yml](https://docs.papermc.io/paper/dev/plugin-yml/)
Descriptor semantics and patch-level API baseline. Retrieved official search excerpt.

## P4 — Paper/Folia support
[Paper/Folia support](https://docs.papermc.io/paper/dev/folia-support)
Region/entity/global/async ownership and support-flag warning. Retrieved official search excerpt.

## P5 — Paper API index
[Paper API index](https://docs.papermc.io/paper/dev/api/)
PDC, components, lifecycle, commands and API navigation. Retrieved official search excerpt.

## B1 — BukkitScheduler Javadoc
[BukkitScheduler Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scheduler/BukkitScheduler.html)
Async API warning and synchronous scheduling; loaded relevant content. Current Javadoc may be newer than target.

## B2 — InventoryClickEvent Javadoc
[InventoryClickEvent Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/InventoryClickEvent.html)
Transaction restrictions, delayed open/close guidance and overwritten slot mutations. Retrieved official Javadoc excerpt.

## N1 — NeoForge getting started
[NeoForge getting started](https://docs.neoforged.net/docs/gettingstarted/)
Java 25, ModDevGradle/NeoGradle generator and source locations. Downloaded official page.

## N2 — NeoForge 1.21.1 events
[NeoForge 1.21.1 events](https://docs.neoforged.net/docs/1.21.1/concepts/events/)
Game/mod buses, parallel lifecycle and patch-sensitive subscriber behavior. Loaded relevant content.

## N3 — NeoForge 1.21.1 components
[NeoForge 1.21.1 components](https://docs.neoforged.net/docs/1.21.1/items/datacomponents/)
Persistent/network codecs and component value model. Retrieved official excerpt.

## N4 — NeoForge 1.21.1 attachments
[NeoForge 1.21.1 attachments](https://docs.neoforged.net/docs/1.21.1/datastorage/attachments/)
Persistence, death copy and item component distinction. Retrieved official excerpt.

## N5 — NeoForge newer attachments
[NeoForge newer attachments](https://docs.neoforged.net/docs/datastorage/attachments)
Newer synchronization facilities; version contrast only, not backported to 1.21.1. Retrieved official excerpt.

## N6 — NeoForge 1.21.1 capabilities
[NeoForge 1.21.1 capabilities](https://docs.neoforged.net/docs/1.21.1/inventories/capabilities/)
Handler APIs, caches and dynamic behavior. Retrieved official excerpt.

## N7 — NeoForge 1.21.1 networking
[NeoForge 1.21.1 networking](https://docs.neoforged.net/docs/1.21.1/networking/)
Payload overview. Retrieved official excerpt.

## N8 — NeoForge 1.21.1 payload registration
[NeoForge 1.21.1 payload registration](https://docs.neoforged.net/docs/1.21.1/networking/payload/)
Registration, main-thread default, network override and enqueueWork. Loaded relevant content.

## N9 — Minecraft 26.2 vanilla migration primer
[Minecraft 26.2 vanilla migration primer](https://docs.neoforged.net/primer/docs/26.2/)
Rendering/GPU changes, registry keys/tag providers, GUI/HUD and vanilla migrations. Loaded relevant content; not a NeoForge-hook guarantee.

## N10 — NeoForge mod files
[NeoForge mod files](https://docs.neoforged.net/docs/gettingstarted/modfiles)
Descriptor/build properties; retrieved official excerpt. Some examples lag the page version.

## K1 — Kotlin for Forge project
[Kotlin for Forge project](https://github.com/thedarkcolour/KotlinForForge)
Language provider/runtime strategy; project/variant verification required.

## K2 — Kotlin for Forge 5.x README
[Kotlin for Forge 5.x README](https://github.com/thedarkcolour/KotlinForForge/blob/5.x/README.md)
Downloaded branch README via raw URL; NeoForge skeleton/variant and language provider instructions. Do not apply this old branch universally to 26.2.

## Additional lookup entrypoints (not independently audited here)
- [Kotlin JVM/Gradle reference](https://kotlinlang.org/docs/gradle-configure-project.html)
- [Sponge Mixin wiki](https://github.com/SpongePowered/Mixin/wiki)
- [Fabric developer documentation](https://docs.fabricmc.net/develop/)
- [Spigot Javadocs index](https://hub.spigotmc.org/javadocs/spigot/)
- [NeoForge documentation](https://docs.neoforged.net/)

## Evidence conflicts and limitations
- Search results included third-party tutorials with over-broad Java/version claims. Those claims were not adopted over official target guidance.
- Current Paper pages show 26.3 examples. This suite uses their version-format/era rules but does not silently target 26.3.
- Some Fabric docs are headed 26.2 while setup prose mentions 26.1, and porting prose may retain snapshot language. Dated official release posts and exact generated sources should resolve target-specific questions.
- NeoForge current general docs can default to 26.1; the 26.2 primer describes vanilla changes. Verify actual 26.2 NeoForge artifacts and APIs separately.
- Kotlin provider documentation is branch-specific and current runtime versions move. Verify loader variant and game support at implementation time; no universal version number is pinned.
- Official online Spigot Javadocs can describe a newer API. Use the resolved target artifact for availability checks.
- Engineering guidance on ownership, bounded queues, testing and simple design is original synthesis, not copied official text or an independently benchmarked result.
- No generated Minecraft project was compiled or run in this packaging task. See root QA.md for actual local checks.


## Client interoperability update — checked 2026-10-28

- [Claude Code application setup](https://code.claude.com/docs/en/setup): loaded official setup content, including native/package-manager/npm methods and current Node requirement.
- [OpenCode V1 introduction/install](https://opencode.ai/docs): retrieved official install excerpt, distinct V1 package and V2 collision warning.
- [OpenCode V2 introduction/install](https://opencode.ai/v2/docs): loaded official npm/native-platform/provider connection guidance; Windows package-manager restriction retained.
- [OpenCode V1 skills](https://opencode.ai/docs/skills): loaded official paths, tool loading and permission/discovery guidance.
- [OpenCode V2 skills](https://opencode.ai/v2/docs/skills): loaded official frontmatter, ID/discovery/loading guidance; does not assume V1 config syntax works for V2.
- [Cursor skills](https://cursor.com/docs/context/skills): retrieved official native/compatibility directory and remote scope excerpts.
- [Copilot adding skills](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/add-skills): retrieved official native and compatible path excerpt.
- [Copilot skill concepts/surfaces](https://docs.github.com/en/copilot/concepts/customizations/agent-skills): retrieved official feature/surface and IDE-version qualifications.
- [Codex skills](https://developers.openai.com/codex/skills): loaded official page (redirected to current learning docs), `.agents/skills`, local scopes and invocation guidance.
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/): loaded official native/alias locations, listing/reload and install guidance.
- [JetBrains AI Assistant rules](https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html): loaded official rule directory/applicability/attachment guidance; used as a manual adapter, not native skill discovery.


## Link/API/mod-list update — checked 2026-10-28

- [Fabric mod metadata](https://docs.fabricmc.net/develop/loader/fabric-mod-json): loaded environment, nested JAR and dependency semantics; no universal SemVer resolver is implemented by the offline helper.
- [Fabric Loader public API source](https://github.com/FabricMC/fabric-loader/blob/master/src/main/java/net/fabricmc/loader/api/FabricLoader.java): retrieved method-level metadata/list/presence excerpts; exact target source still required.
- [NeoForge mod files](https://docs.neoforged.net/docs/gettingstarted/modfiles): loaded descriptor/dependency kind, side, order and version fields; current examples can lag page target.
- [NeoForge loader ModList source](https://github.com/neoforged/FancyModLoader/blob/main/loader/src/main/java/net/neoforged/fml/ModList.java): downloaded maintained source through raw URL, inspected list/presence/container methods; not every historical build audited.
- [Modrinth mrpack specification](https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack): loaded archive/index/hash/environment/dependency fields; helper does not download referenced content.
- [Paper API index](https://docs.papermc.io/paper/dev/api/): checked API groups; individual target symbols still require resolution/compilation.
- [Fabric Transfer overview](https://wiki.fabricmc.net/tutorial:transfer-api): downloaded maintainer documentation; distinguishes item/fluid transactions from separate energy integration.
- [LuckPerms developer API](https://luckperms.net/wiki/Developer-API): retrieved maintained API entrypoint/version/thread-related excerpts; old revision search results were not used as current API pins.
- [VaultAPI](https://github.com/MilkBowl/VaultAPI), [PlaceholderAPI](https://wiki.placeholderapi.com/developers/using-placeholderapi/), [WorldGuard](https://worldguard.enginehub.org/en/latest/developer/), [ProtocolLib](https://github.com/dmulloy2/ProtocolLib), [PacketEvents](https://docs.packetevents.com/): downloaded official/project entrypoint pages to verify integration lookup destinations; not a full signature or version-matrix audit.
- [Mod Menu](https://github.com/TerraformersMC/ModMenu): downloaded maintainer README and inspected modmenu entrypoint/API/config factory guidance.
- [Cloth Config](https://shedaniel.gitbook.io/cloth-config/), [JEI wiki](https://github.com/mezz/JustEnoughItems/wiki), [EMI wiki](https://github.com/emilyploszaj/emi/wiki): downloaded maintained lookup entrypoints; no compiled target-specific adapter included.
- [Architectury mod metadata](https://docs.architectury.dev/api/platform/mod/): downloaded metadata/platform lookup guidance; optional toolchain, not imposed on single-loader projects.
- [Adventure modded platform](https://docs.papermc.io/adventure/platform/modded/): retrieved project-maintainer platform/era guidance; not a guarantee that Paper's runtime dependencies exist on every modded server.

Remote GitHub link installation is an original bounded helper and agent workflow. No actual public repository/release was created or fetched in its tests. Synthetic archive tests do not establish that a placeholder URL exists. No full CurseForge API client, loader dependency solver, malware detector or every-API SDK is claimed.

## Companion and anti-cheat lookup sources

Reviewed 2026-10-28; live sources may change. Documentation-level interoperability only; no source code vendored.

- [Caveman](https://github.com/JuliusBrussee/caveman) and [voice skill](https://raw.githubusercontent.com/JuliusBrussee/caveman/main/skills/caveman/SKILL.md): exact payload/clarity and voice-versus-proxy boundaries.
- [Superpowers](https://github.com/obra/superpowers): named debugging, TDD and verification workflows; no automatic lifecycle/subagent authorization.
- [Matt Pocock skills](https://github.com/mattpocock/skills): TDD and user-invoked versus model-invoked boundaries.
- [Context7](https://github.com/upstash/context7): focused library resolution/documentation tools, not a Minecraft library or skill.
- [Grim](https://github.com/GrimAnticheat/Grim), [GrimAPI](https://github.com/GrimAnticheat/GrimAPI): official integration lookup; versioned event/lifecycle differences.
- [NoCheatPlus](https://github.com/NoCheatPlus/NoCheatPlus): legacy API lookup; NOT proof of current target support.

## Permission implementation sources — reviewed 2026-10-28

- [Paper classic plugin.yml](https://docs.papermc.io/paper/dev/plugin-yml/): permission defaults/children and command permission metadata.
- [Paper 1.21.1 Permissible](https://jd.papermc.io/paper/1.21.1/org/bukkit/permissions/Permissible.html): hasPermission versus isPermissionSet, attachment lifecycle; not cross-version proof.
- [LuckPerms API](https://luckperms.net/wiki/Developer-API) and [usage](https://luckperms.net/wiki/Developer-API-Usage): lifecycle, cached context-aware checks, asynchronous loading/events and saved mutations. Upstream examples still need target compilation and safe game-thread adaptation.
- [Fabric Permissions API](https://github.com/lucko/fabric-permissions-api) and [usage](https://github.com/lucko/fabric-permissions-api/blob/master/USAGE.md): separate permission-provider API, fallbacks/offline futures and version/build transition; matrix does not establish 26.2 support.
- [NeoForge 1.21.1 PermissionAPI source](https://raw.githubusercontent.com/neoforged/NeoForge/1.21.1/src/main/java/net/neoforged/neoforge/server/permission/PermissionAPI.java) and [gather event source](https://raw.githubusercontent.com/neoforged/NeoForge/1.21.1/src/main/java/net/neoforged/neoforge/server/permission/events/PermissionGatherEvent.java): registered typed-node checks and registration, not proof of newer signatures.

The separate Paper-specific plugin overview could not be retrieved in this update; no new Paper-plugin-model permission schema is claimed from that page. Classic metadata is deliberately not assumed interchangeable. No permission provider runtime or platform snippet was compiled/executed during authoring.

## Closed-source artifact protection

Reviewed 2026-10-28: [ProGuard usage](https://www.guardsquare.com/manual/configuration/usage), [Kotlin metadata](https://www.guardsquare.com/manual/languages/kotlin), [Zelix feature descriptions](https://www.zelix.com/klassmaster/features.html), and [Paper descriptor](https://docs.papermc.io/paper/dev/plugin-yml/). Guidance only: no obfuscator execution, proprietary tool/SDK, exact class-file support verification or reverse-analysis benchmark was performed.
