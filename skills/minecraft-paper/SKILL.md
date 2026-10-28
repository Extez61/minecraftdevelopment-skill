---
name: minecraft-paper
description: "Develop, debug, optimize, review or migrate Paper plugins in Java or Kotlin for Minecraft 1.21.1 through 26.2. Use for JavaPlugin, plugin.yml/paper-plugin.yml, lifecycle, Adventure, PDC/data components, commands, inventories, async persistence, paperweight and explicitly scoped Folia support. Preserve behavior and verify exact-version APIs."
---

# Paper Plugin Development

**Skill creator: extez061**

For shared topic lookup, use the [AI file map](../minecraft-development/AI-INDEX.md); do not load unrelated platform guides.

Read `../minecraft-development/SKILL.md`. Determine whether the target is Paper only, Bukkit/Spigot compatible, or explicitly Folia compatible. Do not assume one implies the others. Classic `plugin.yml` is valid for many Paper plugins; Paper-specific plugin loading is a separate choice.

## Inspect first

Record exact Minecraft/Paper build, API coordinate, JDK/runtime target, Java/Kotlin, build DSL, descriptors, plugin entrypoint, listeners/commands, dependencies/integrations, persistence and existing tests. Read lifecycle and task ownership before changing stateful code.

For API-domain/integration lookup, read `../minecraft-development/references/api-catalog.md` and `../minecraft-development/references/integrations.md` as needed. For mod/plugin lists, modpack dependency triage or mod-list/config-screen UI, read `../minecraft-development/references/modlists-compatibility.md`.

## Reference router

| Work | Read |
| --- | --- |
| Registries/dialogs/plugin messaging/resource packs and extended public APIs | [Additional API playbooks](references/extended-public-api.md) |
| Build, descriptors, bootstrap, commands, integrations | [Lifecycle/builds](references/lifecycle-builds.md) |
| Scheduler/thread ownership, async I/O, optional Folia | [Threading/Folia](references/threading-folia.md) |
| PDC, components, inventories, text, gameplay and storage | [API/gameplay](references/api-gameplay.md) |
| Compatibility, NMS, performance and release checks | [Compatibility/validation](references/compatibility-validation.md) |

Read shared behavior-preservation before modifying code; read shared Java/Kotlin/build guidance for runtime libraries and packaging; read shared profiling before optimization.

## Hard rules

1. Prefer Paper public APIs over NMS/reflection for Paper-only projects.
2. Compile against the intended API baseline; do not shade the Paper/server API.
3. Never mutate live server state from an arbitrary async callback/coroutine.
4. Register commands/listeners exactly once and keep descriptor/permission/config declarations coherent.
5. Preserve event priority, cancellation and existing plugin interoperability. Do not modify state in a monitoring-only handler.
6. Keep long-lived identity by UUID/stable key, with cleanup; do not retain stale players/worlds/events.
7. Treat every scheduled task and external resource as lifecycle-owned.
8. For Kotlin use an instantiable `JavaPlugin` class and an intentional runtime dependency strategy.
9. Never set `folia-supported: true` until scheduling, shared state and runtime behavior are actually audited/tested.
10. Do not recommend `/reload` or hot unload as a normal deployment or debugging loop.

## Implement and prove

Capture current behavior and regression risks; use a small patch, targeted tests, production artifact inspection and a clean exact-version server run. Verify permissions, console usage, join/quit/death, configuration failure, shutdown and persistence. Report untested versions and performance honestly.

Sources: [Paper developer docs](https://docs.papermc.io/paper/dev/), [project setup](https://docs.papermc.io/paper/dev/project-setup/), [Folia support](https://docs.papermc.io/paper/dev/folia-support).

## Anti-cheat and lean companion workflows

For defensive anti-cheat checks or legitimate gameplay compatibility, read [anti-cheat engineering](../minecraft-development/references/anticheat-development.md); verify this exact platform/product tuple. Apply the core lean context contract; do not preload unrelated platform/reference files. For optional Caveman or other workflow composition, read [companion skills](../minecraft-development/references/companion-skills.md) only when needed.

For node declaration, command/action guards, defaults or permission providers, open [permission engineering](../minecraft-development/references/permissions-authorization.md) only when needed. Match the actual platform/API version and preserve existing access behavior.

For owned closed-source plugin obfuscation, reflection/descriptor keep rules and performance-preserving distribution, read [artifact protection](../minecraft-development/references/closed-source-protection.md) only when requested. No AI-proof or unmeasured zero-overhead claims.
