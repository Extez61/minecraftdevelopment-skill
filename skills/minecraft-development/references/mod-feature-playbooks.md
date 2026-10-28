# Advanced mod feature playbooks

Use with the actual Fabric or NeoForge skill. These are investigation/implementation checklists, not interchangeable loader APIs. Verify exact target source for names and signatures. Keep optional features out of a project until requested.

## World generation, biomes, dimensions and structures

Establish whether the requested change is data-driven, a supported loader biome/worldgen hook, or a genuinely custom codec/type implementation. Prefer data definitions and supported modification hooks when they satisfy the feature; avoid replacing a complete world generator for one ore or placed feature.

Inspect dynamic registry/bootstrap contexts, feature/placed-feature/biome/structure IDs, dimension type versus level-stem identity, tags and relevant codecs. Register code-backed types at the correct lifecycle, and provide data in the target schema. Do not mutate frozen registries or retain reload-sensitive registry objects indefinitely.

Distinguish configured behavior from placement, biome selection and structure-set rules. Validate distributions statistically or with deterministic seed-based scenarios where appropriate; a single successful spawn does not prove correct density. Do not change random-number consumption casually during an optimization, because it can alter generated worlds.

Generation may use worker threads and constrained world-generation views. Do not assume arbitrary server/world access is valid from a generator callback. Avoid blocking I/O, static mutable generation state and global caches keyed only by coordinates without dimension/seed/lifecycle context. Use APIs and structures documented for that generation stage.

Worldgen changes normally affect newly generated chunks, not already-generated terrain. Explain chunk-boundary discontinuities and compatibility with existing saves. Never promise a rollback by downgrading the JAR after newer data has been written. Test on copied worlds with fixed seeds and separate fresh/existing-chunk scenarios. Do not silently regenerate or delete player terrain.

Profile generation separately from steady-state ticking. Replacing expensive computation with a cache requires correct keys, deterministic results, memory bounds and thread safety; a cross-world stale result can corrupt generation. Respect data-pack/other-mod merging and do not replace whole biome/tag definitions unnecessarily.

## Recipes, loot, tags and data-driven enchantments

Use target-version serializers/codecs, data providers and reload integration. Stable recipe/type/serializer IDs matter independently. Preserve recipe precedence, matching semantics, remainders, conditions and tags when porting.

For a custom machine, keep ingredient matching and output creation pure where possible, then execute the authoritative consumption/production transaction on the owner. Test empty inputs, partial stacks, damaged/components-bearing items, multiple valid recipes, full output, remainder containers and reload while a recipe is active. Simulated insertion/extraction must not mutate.

For loot, distinguish tables, conditions, functions and modifiers/hooks. Preserve other mods' additions and avoid replacing an entire vanilla table when a narrow supported change exists. Check server-side authority and random distribution; test duplicate trigger paths and entity/block context.

For enchantments/effects with data-driven definitions, use appropriate registry/data mechanics for the exact release. Do not port an old hard-coded singleton enum/list pattern just because it compiled in another version. Keep execution hooks and visual tooltip/model data coherent; test reload, old saved items and mutually interacting effects.

Tags are semantic sets that may merge across packs. Use tags when the behavior should extend to compatible modded content. Do not replace tags wholesale or hardcode vanilla-only classes if interoperability is part of the requirement. On reload invalidate recipe/tag-derived caches at a documented boundary.

## Entities, attributes, AI and pathfinding

Identify spawn rules, entity type, attributes, tracked state, save data, goals/brain/sensors and client renderer. Keep each under the target loader's correct registration/lifecycle. Do not assume Fabric and NeoForge attribute registration share event names.

AI changes must preserve priority, interruption, target validity, ownership, team/attack rules and navigation capabilities. Avoid expensive full-radius/entity/path searches every tick without profiling. Cache/reuse only when targets, dimensions, obstacles and lifecycle changes invalidate correctly. A capped target list, reduced awareness radius or slower reaction cadence changes behavior and requires approval.

Keep pathfinding/gameplay on supported threads/APIs. Do not send live level/entity objects into arbitrary parallel streams to “speed up AI.” A pure off-thread planning calculation can use a valid immutable snapshot, but authoritative application must recheck world state and ownership.

Test natural and command spawn, despawn/removal, unloaded chunks, save/reload, dimension changes, owner logout, death, unusual target types and other AI-mod combinations in scope. Avoid static references to removed entities or client renderers.

## Attributes, effects, damage and projectiles

Use stable identities for modifiers according to target APIs. Decide whether a modifier is transient, equipment-driven, saved or recomputed; avoid applying a second copy every tick or leaving it after unequip/death.

Preserve damage source/type semantics, armor/resistance interaction, cancellation, invulnerability windows, knockback, projectile ownership and kill attribution. Re-entering vanilla damage from an event can recurse or award twice. Use a narrowly defined guard/transition rather than globally disabling events.

Separate visual prediction from server-authoritative damage/rewards. Test both logical sides, simultaneous hits, removed projectiles, friendly fire, protected targets, death/respawn and save/reload where relevant. Do not treat a client packet's proposed damage or target as authority.

## Configurable features without config bloat

Expose values when operators/users actually need them or the project already has a matching config contract. Do not turn every implementation detail into a configuration key. Validate ranges, units, interdependent options and changed defaults clearly.

Choose whether a setting is client-local, server-authoritative, synced for display, restart-required or reloadable. Never let a client-local value control authoritative loot/damage/range. Use an immutable validated snapshot and a deliberate reload application point. Avoid a config watcher thread that mutates gameplay objects directly.

## Compatibility review

Check data-pack overrides, optional integration classloading, registry identity, item components, loot/recipe merging, event cancellation, Mixins and resource reload. Test the smallest dependency set as well as intended integrations. A workaround that disables another mod's feature is not behavior-preserving unless explicitly approved.

Read the shared version policy and source index before exact API work. When a feature requires an undocumented hook or unstable internal API, state the risk, identify the exact verified target and consider a simpler supported alternative.
