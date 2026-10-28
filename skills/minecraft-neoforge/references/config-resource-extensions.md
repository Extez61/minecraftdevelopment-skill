# NeoForge configuration, resources and extension API playbooks

Use the exact target documentation/source for names, events and schemas. This file closes common domain gaps; it is not a universal implementation for every loader patch.

## Configuration and config-screen extension

Distinguish client-local options, common settings, server-authoritative gameplay values and fields synchronized for display. Use the target's documented configuration specification/registration and lifecycle. Validate bounds, units and interdependent settings; do not let client-local config control authoritative damage/loot.

For reloadable settings, prepare a validated snapshot and apply at the correct lifecycle/thread boundary; invalidate derived caches deliberately. Some options require restart or world reload. Do not claim arbitrary registry/content registration can be hot-reloaded because a config value changed.

A config screen and config persistence/sync are different systems. For the built-in mods UI, use the target-supported config-screen extension/factory and safe physical-client initialization. Preserve parent navigation, save/cancel and unavailable-option feedback. Optional Cloth Config integration is a screen implementation choice, not a mandatory server dependency.

## Conditions, recipes, ingredients and loot

Use supported target resource-condition mechanisms and serializers/codecs. Distinguish code-registered type/serializer identity from data-driven definitions loaded through registries/data packs. Do not hide an absent code class only with a JSON condition.

For custom ingredient/recipe behavior, test components/tags, matching precedence, stack copying/remainders and dynamic reload. For loot modifiers/conditions/functions, preserve other mods' additions and use the correct context; avoid replacing whole tables unless intentional.

Recipe viewer display is client integration, not server authority. A transfer handler should request a valid operation and never mint output based on the UI's data alone. Test missing viewer, full inventory, partial transfer and repeated input.

## Worldgen, biome and datapack extensions

Prefer supported data-driven registry/bootstrap and biome modification hooks for the requested feature. Verify lifecycle and frozen-registry rules. Distinguish new terrain generation from existing chunks; do not promise changes to already-generated worlds without explicit migration work.

Keep generation deterministic where expected and obey stage-specific thread/world access. Use codecs/holders/keys from the selected version rather than copying a Fabric/Yarn example. Test fresh/copied existing saves and datagen/runtime resource resolution.

## Inter-mod communication and extension registration

Use documented native extension mechanisms only when there is a real cooperating mod/API. Validate provider availability, supported API/format, processing lifecycle and callback thread. Keep optional types out of eager common initialization. Do not introduce a custom plugin system or reflection scanner for one optional integration.

Capabilities expose behavior; attachments/components/saved data retain state; messages communicate state. Do not collapse them into one general “integration manager” that hides ownership and persistence. Explicit narrow adapters are easier to test.

## Access transformers and Mixins

Use supported public hooks first. If access transformation or a Mixin is necessary, verify exact source/descriptor/side, package its declaration correctly, keep scope minimal and test production transforms/conflicts. Unobfuscated names are not a compatibility guarantee.

Do not suppress failed required transformations or set a zero match requirement to hide broken functionality. Optional transforms require explicit provider/version gates and an absence test. Kotlin synthetic/static members should be inspected at the JVM boundary; small Java glue may be simpler.

## Acceptance gate

Verify configuration defaults/reload, config-screen client-only loading, data-pack overrides, codecs and stable IDs, old-save restart, optional integration absence, dedicated server/client startup and production artifact contents. Start from [NeoForge documentation](https://docs.neoforged.net/) and select the actual game/loader version; current latest docs and the vanilla 26.2 primer are not interchangeable loader API guarantees.
