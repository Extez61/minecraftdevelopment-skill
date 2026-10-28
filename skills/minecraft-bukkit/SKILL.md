---
name: minecraft-bukkit
description: "Create, debug, optimize, review and port Bukkit/Spigot-compatible Minecraft plugins in Java or Kotlin from 1.21.1 through 26.2. Use for plugin.yml, JavaPlugin, portable commands/listeners, permissions, BukkitScheduler, PDC, inventories and safe async persistence. Avoid Paper-only linkage and unverified version ranges."
---

# Bukkit / Spigot Plugin Development

**Skill creator: extez061**

For shared topic lookup, use the [AI file map](../minecraft-development/AI-INDEX.md); do not load unrelated platform guides.

Read `../minecraft-development/SKILL.md`. Treat Bukkit as an API family and Spigot as a concrete runtime/API distribution; do not invent a maintained official “Bukkit server download” for every game version. Identify the real runtime the user will deploy.

## Discover the target

Read the exact Bukkit/Spigot API dependency, runtime version/build, wrapper, Java/Kotlin target, descriptor, entrypoint, commands/listeners, storage and integration APIs. A classic `plugin.yml` can belong to a Paper project too; the intended deployment contract decides the skill.

Determine the minimum API and actual supported server matrix. Do not assume Paper APIs, Adventure conveniences, async chunk APIs or region schedulers exist on Spigot because they appeared in a search result.

For API-domain/integration lookup, read `../minecraft-development/references/api-catalog.md` and `../minecraft-development/references/integrations.md` as needed. For mod/plugin lists, modpack dependency triage or mod-list/config-screen UI, read `../minecraft-development/references/modlists-compatibility.md`.

## Reference router

| Work | Read |
| --- | --- |
| Build, plugin.yml, Kotlin entrypoint, registration | [Bootstrap/portability](references/bootstrap-portability.md) |
| Events, commands, inventory transactions and item identity | [Events/UI](references/events-ui.md) |
| Scheduling, storage, lifecycle and performance | [Lifecycle/storage](references/lifecycle-storage.md) |
| Cross-version compatibility and verification | [Validation](references/validation.md) |

For changes read shared behavior-preservation; for Kotlin/builds read shared Java/Kotlin guide; for optimization read shared performance.

## Core rules

1. Depend on the intended minimum Bukkit/Spigot API and avoid Paper-only classes in the portable artifact.
2. Declare and register commands, permissions and listeners coherently. Validate command sender type and execution permissions.
3. Keep most Bukkit API work on the main server thread. Async workers operate on independent immutable data only.
4. Keep a task/resource owner and cleanup for quit, death, match end, world unload and plugin disable as applicable.
5. Use PDC/metadata APIs supported by the baseline; do not use lore or a display name as an authorization marker.
6. Respect event priority, cancellation/result semantics and inventory event restrictions.
7. Avoid NMS/CraftBukkit unless truly necessary and version-isolated; public API first.
8. Use an instantiable Kotlin `JavaPlugin` class, not `object`; ship required runtime libraries intentionally.
9. Prefer restart over hot reload for code changes. Do not prescribe PlugMan or `/reload` to avoid understanding lifecycle bugs.
10. Do not claim Folia support for a Bukkit-scheduler implementation or rely on Paper runtime tests to prove Spigot support.

## Delivery

Provide the smallest working change, coherent descriptor/resources, exact build artifact, actual tests and explicit compatibility limitations. Preserve user configuration, command behavior, event interoperability and durable data. Do not replace features with placeholders to simplify a port.

Sources: [Spigot Javadocs](https://hub.spigotmc.org/javadocs/spigot/), [BukkitScheduler](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scheduler/BukkitScheduler.html), [InventoryClickEvent](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/InventoryClickEvent.html).

## Anti-cheat and lean companion workflows

For defensive anti-cheat checks or legitimate gameplay compatibility, read [anti-cheat engineering](../minecraft-development/references/anticheat-development.md); verify this exact platform/product tuple. Apply the core lean context contract; do not preload unrelated platform/reference files. For optional Caveman or other workflow composition, read [companion skills](../minecraft-development/references/companion-skills.md) only when needed.

For node declaration, command/action guards, defaults or permission providers, open [permission engineering](../minecraft-development/references/permissions-authorization.md) only when needed. Match the actual platform/API version and preserve existing access behavior.

For owned closed-source plugin obfuscation, reflection/descriptor keep rules and performance-preserving distribution, read [artifact protection](../minecraft-development/references/closed-source-protection.md) only when requested. No AI-proof or unmeasured zero-overhead claims.
