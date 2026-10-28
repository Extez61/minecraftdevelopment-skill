---
name: minecraft-neoforge
description: "Build, debug, review, optimize or migrate NeoForge mods in Java or Kotlin for Minecraft 1.21.1 through 26.2. Use for neoforge.mods.toml, ModDevGradle/NeoGradle, @Mod, mod/game event buses, DeferredRegister, components, attachments, capabilities, menus, payloads, datagen and client renderers. Do not substitute Forge or Fabric APIs."
---

# NeoForge Mod Development

For shared topic lookup, use the [AI file map](../minecraft-development/AI-INDEX.md); do not load unrelated platform guides.

Read `../minecraft-development/SKILL.md`. NeoForge is its own loader/API target; old Forge snippets are not authoritative for a NeoForge project. Confirm exact versions, including patch-level loader API changes within a Minecraft line.

## Inspect first

Read wrapper, build/plugin versions, properties/catalogs, `META-INF/neoforge.mods.toml`, `@Mod` entrypoint, registry classes, event registrations, access declarations, mixins, networking, client sources, datagen and tests. Record ModDevGradle vs NeoGradle, Java/Kotlin, mappings/naming, runtime dependencies and target side.

For worldgen, biomes/dimensions, recipes/loot, entity AI, attributes or effects, also read `../minecraft-development/references/mod-feature-playbooks.md`.

For API-domain/integration lookup, read `../minecraft-development/references/api-catalog.md` and `../minecraft-development/references/integrations.md` as needed. For mod/plugin lists, modpack dependency triage or mod-list/config-screen UI, read `../minecraft-development/references/modlists-compatibility.md`.

## Reference router

| Work | Read |
| --- | --- |
| Config/mods UI/resource conditions/loot and extension hooks | [Additional API playbooks](references/config-resource-extensions.md) |
| Build, descriptor, entrypoint, event buses, Kotlin | [Bootstrap/events](references/bootstrap-events.md) |
| Content, deferred registration, components, storage, capabilities | [Registries/data](references/registries-data.md) |
| Payloads, menus, side separation and authoritative gameplay | [Networking/menus](references/networking-menus.md) |
| Rendering, datagen, migrations, tests and performance | [Rendering/validation](references/rendering-validation.md) |

Also read shared version policy, behavior preservation, Java/Kotlin builds and relevant concurrency/performance/migration references. Load selectively.

## NeoForge invariants

1. Register each event on its actual bus for the exact loader version. Do not assume every setup event runs on the game thread.
2. Use deferred registration/holders according to the target lifecycle. Do not eagerly dereference entries before registration.
3. Keep physical client-only classes off dedicated-server load paths.
4. Distinguish components, attachments, capabilities and saved data; they solve different problems.
5. Explicitly design persistence, dirty marking, synchronization and player death/clone behavior.
6. Register typed payloads with correct direction/phase/version/thread semantics; validate C2S requests.
7. Use a supported target-specific Kotlin provider/runtime strategy, not a Forge-only artifact by name similarity.
8. Do not bypass failed registry/codec validation with broad exception suppression.
9. Preserve stable IDs and old-save contracts; test on copies.
10. Build and test the production artifact on a dedicated server/client where applicable; one IDE integrated run is insufficient.

## Execution

Establish baseline → inspect target source/official versioned docs → make a surgical change → compile/test/datagen as needed → inspect production JAR → runtime check and old-save regression → report exact evidence and unresolved compatibility.

Sources: [NeoForge docs](https://docs.neoforged.net/), [1.21.1 docs](https://docs.neoforged.net/docs/1.21.1/), [26.2 vanilla migration primer](https://docs.neoforged.net/primer/docs/26.2/).

## Anti-cheat and lean companion workflows

For defensive anti-cheat checks or legitimate gameplay compatibility, read [anti-cheat engineering](../minecraft-development/references/anticheat-development.md); verify this exact platform/product tuple. Apply the core lean context contract; do not preload unrelated platform/reference files. For optional Caveman or other workflow composition, read [companion skills](../minecraft-development/references/companion-skills.md) only when needed.

For node declaration, command/action guards, defaults or permission providers, open [permission engineering](../minecraft-development/references/permissions-authorization.md) only when needed. Match the actual platform/API version and preserve existing access behavior.
