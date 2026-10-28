# API coverage map and lookup discipline

## Scope and honesty

This is a **broad API-domain catalog and implementation playbook**, not an embedded SDK, every method signature, or proof all APIs exist on every 1.21.1–26.2 target. The ecosystems change independently; no finite skill can truthfully guarantee “every API.” Use this catalog to avoid major omissions, then verify the exact resolved artifact/source for the task. Do not install every listed library into every project.

Coverage labels:
- **Guide:** this suite includes a concrete lifecycle/design/validation procedure.
- **Lookup:** a maintained upstream entrypoint is provided; exact implementation still requires target research.
- **Conditional:** available only on particular versions/platforms/dependencies.
- **Out of default scope:** use only if explicitly requested, never silently substitute it for one of the four target platforms.

## Shared API domains — guide coverage

| Domain | Questions and invariants | Local guide |
| --- | --- | --- |
| Build/runtime/mappings | Exact game/loader/API, Java/Kotlin ABI, runtime libraries, production artifact | [Java/Kotlin builds](java-kotlin-builds.md), [version policy](version-policy.md) |
| Lifecycle/events/commands | Registration owner, callback thread, result/cancellation, sender and permissions | Actual platform skill + [behavior preservation](behavior-preservation.md) |
| Entity/block/item state | Stable IDs, copy semantics, lifetime, dirty marking and server authority | Actual platform content/API guide + [advanced systems](mod-feature-playbooks.md) |
| Networks and protocols | Direction, phase, bounded codecs, initial/delta sync, tracking, validation | Actual mod networking guide + [trust boundaries](trust-boundaries.md) |
| Persistence/config | PDC/components/attachments/saved data versus repositories; migration and reload | [Concurrency/persistence](concurrency-persistence.md), [migration](migration.md) |
| UI/inventories/input | Transaction ownership, transfer variants, menu identity, side separation | Actual platform UI/menu guide |
| Worldgen/recipes/loot/tags | Dynamic/static registry, data schema, merging, deterministic behavior | [Advanced systems](mod-feature-playbooks.md) |
| AI/attributes/combat/effects | Goal priority, modifier identity, cancellation, duplication and cleanup | [Advanced systems](mod-feature-playbooks.md) |
| Rendering/resources | Versioned pipelines, extraction/submission, models, reload, backend/GPU lifetime | Fabric rendering / NeoForge rendering guide |
| Performance/testing | Measured workload, preserved behavior, integration/old-save/runtime evidence | [Performance](performance.md), [testing](testing-release.md) |
| Installed mods/plugin lists | Offline metadata versus runtime discovery versus successfully enabled content | [Mod lists](modlists-compatibility.md) |
| External integrations | Optional classloading, exact dependency, cross-service boundaries | [Integrations](integrations.md) |

## Fabric: Loader and game API are separate

**Loader (guide + lookup):** mod/container metadata, all-mods enumeration, optional mod presence, entrypoints/language adapters, environment, version metadata, mapping resolution, nested JAR discovery. Use the public loader API, not internal implementation classes. A loader presence check does not verify another mod's API version or permit eager class linkage.

**Fabric API (guide + conditional lookup):** lifecycle/tick events, command registration, interaction/entity/item/block callbacks, networking and payload types, resource loading/reload, data generation, item/block registrations and creative tabs, object attachments, rendering/HUD/world render hooks, particles/sounds, screen/keybinding APIs, biome/dimension modification hooks, recipes/loot/tags, resource conditions and compatibility hooks. Module names and symbols can change, especially at 26.1.

**Transfer (guide + lookup):** item/fluid storage views and transactional transfer; simulation/commit/rollback and sided context require correct semantics. Do not treat a transaction as permission for cross-thread mutation. Fabric's transfer documentation also points to a separate TechReborn Energy API; energy integration is not automatically the same universal built-in API as item/fluid transfer.

**Mixin/access tools (guide + conditional):** Mixin/MixinExtras, access widening/class tweaking, target descriptors, optional gates, conflict testing and production transformations. Use supported public hooks first. Newer enum/class-tweaker features cannot be assumed on older Loader/Loom.

**Lookup entrypoints:** [Fabric developer docs](https://docs.fabricmc.net/develop/), [Loader API source](https://github.com/FabricMC/fabric-loader/blob/master/src/main/java/net/fabricmc/loader/api/FabricLoader.java), [metadata specification](https://docs.fabricmc.net/develop/loader/fabric-mod-json), [transfer overview](https://wiki.fabricmc.net/tutorial:transfer-api), [attachments](https://docs.fabricmc.net/develop/data-attachments).

## Paper: public extensions and internal server code are separate

**Guide coverage:** classic/Paper-specific lifecycle and descriptors, command/event/lifecycle APIs, Bukkit versus ownership-aware scheduling, inventories/menus, PDC and item data, Adventure/components/MiniMessage, entities/world/chunks/teleportation, recipes, configuration, plugin services/messaging and optional integrations.

**Conditional lookup:** Paper registries and registry modification, modern dialog/UI APIs, experimental/data-component APIs, version-specific entity APIs, async chunk/teleport facilities and their completion/ownership rules. Do not assume an API introduced later exists on 1.21.1. The dialog API is an example of a later 1.21.x surface, not a portable baseline feature.

**Internal code:** paperweight/NMS/CraftBukkit access is exact-version internal integration, not a stable API. 26.1+ unobfuscation and coordinate/reobfuscation changes do not make internals version-neutral.

**Folia:** explicit separate concurrency target; entity/region/global/async scheduling and cross-region coordination need audited code and real tests. Do not add its support flag because a public method is present.

**Lookup entrypoints:** [Paper API groups](https://docs.papermc.io/paper/dev/api/), [Paper development](https://docs.papermc.io/paper/dev/), [Folia support](https://docs.papermc.io/paper/dev/folia-support), [userdev](https://docs.papermc.io/paper/dev/userdev/).

## Bukkit/Spigot: portable baseline

**Guide coverage:** JavaPlugin lifecycle, plugin.yml, commands/tab completion, permissions/services, event priority/cancellation/results, scheduler, entities/worlds/chunks, inventory/item metadata/PDC, recipes, configuration, scoreboards/boss bars and plugin messaging where supported.

**Lookup/version gate:** exact overloads and enum/material/entity values, server-specific library loading, text APIs, custom resource-pack/client features and any newer descriptor semantics. Do not turn a Paper convenience into a portable Bukkit requirement. A Bukkit API interface and a concrete server build are different compatibility facts.

**Out of portable scope:** Paper/Folia-only linkage or broad NMS access without isolated actual target support. Proxies such as Velocity/BungeeCord are separate runtimes and require an explicitly requested adapter.

**Lookup:** [Spigot Javadocs](https://hub.spigotmc.org/javadocs/spigot/). Current online Javadocs may be newer than the target; use the resolved artifact for availability.

## NeoForge: APIs by responsibility

**Guide coverage:** entrypoint/metadata/tooling, mod/game buses and parallel lifecycle, deferred registries/holders, blocks/items/entities/attributes, components, attachments, saved data, item/fluid/energy capabilities and invalidation, payloads/codecs/distribution, server menus/client screens, resources/datagen, client renderer registration and old-save migration.

**Conditional lookup:** config specification/sync/reload, conditions/recipes/loot modifiers, biome/worldgen/dimension hooks, registry/datapack bootstrap, tags, inter-mod communications/extensions, ingredient/recipe serialization, model/geometry hooks, client events, GameTests, access transformers/Mixins and the built-in mods screen/config-screen extension. Exact event names, bus routing, constructors and available helper APIs vary by loader patch.

**Semantic traps:** capability discovery is not persistence; attachments are not item components; saved data does not automatically sync; `getData` can allocate; simulation must not mutate; lifecycle events can be parallel; main-thread payload defaults/overrides must match the chosen registrar.

**Lookup:** [NeoForge docs](https://docs.neoforged.net/), [1.21.1 docs](https://docs.neoforged.net/docs/1.21.1/), [26.2 vanilla primer](https://docs.neoforged.net/primer/docs/26.2/). A vanilla primer is not verification of a NeoForge hook.

## API use acceptance gate

For each used API, identify platform/module and exact version, dependency scope/runtime availability, symbol/signature, side, thread, lifecycle, error/cancellation behavior, experimental status and test evidence. For integrations include absence/wrong-version tests. For a required undocumented/internal hook, state the risk and consider a narrower supported alternative.

Do not answer a missing-method error by adding random libraries, suppressing linkage failures, changing metadata to force load or dropping behavior. Update this coverage map when a genuinely new supported domain is added; do not claim a lookup link equals a compiled integration.
