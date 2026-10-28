# Fabric rendering, Mixins and narrow vanilla integration

## Prefer a supported hook

Search exact Fabric API events, extension points, resource/data-driven mechanisms and the target source before using a Mixin. A Mixin is appropriate for a real missing hook, not as a default architecture. Document the vanilla method, behavior being changed, expected invocation frequency and compatibility risk.

Prefer a narrowly scoped injection or value modification preserving unrelated code. Avoid `@Overwrite` when a narrower supported mechanism works. Redirects can conflict with other mods; consider the available MixinExtras mechanisms only if supported by the resolved runtime and semantically correct.

## Verify the target precisely

Inspect the exact target class and bytecode/source for the selected game version and mapping namespace. Confirm method descriptor, overload, injection point, invocation owner, return type, locals and side. An ordinal is fragile when surrounding instructions change; prefer a stable semantic anchor when available.

Keep match requirements meaningful. Do not set injection `require=0` merely to hide a broken mandatory hook. Optional compatibility injections may legitimately tolerate absence, but gate them explicitly and test both combinations. A failing core injection should produce an actionable error rather than silently disable functionality.

Package the mixin config and referenced classes, and register it in metadata. Check remapping rules for the era, refmap behavior where applicable, and client-only mixin lists. Do not add `remap=false` just because a symbol cannot be resolved without understanding the namespace.

## Access widening and class tweaking

Use the supported target-version mechanism only for necessary visibility/finality changes. Avoid widening a whole class surface unnecessarily. Verify descriptor/resource registration and production transformation, not just IDE compilation.

Fabric 26.2 introduces enum-extension support through the newer Loader/Loom tooling according to its release article. This is not a reason to add enum extensions to an older project. Prefer a registry/data-driven alternative if it avoids invasive changes and satisfies the feature.

## Kotlin Mixins

Kotlin compiles properties, companions, default arguments and objects to JVM members that may not match intuition. Verify generated fields/method descriptors and static semantics. A small Java Mixin calling a Kotlin-owned pure helper is often simpler than debugging synthetic Kotlin members. Do not add runtime allocations or suspending work inside injected hot methods.

## Rendering boundaries across the interval

- 1.21.2 introduced entity render-state changes; extract needed values according to the target contract instead of passing mutable entities everywhere.
- 1.21.4 changes item model definitions; code-only fixes may not repair missing resources.
- 1.21.5/1.21.6 change HUD/render APIs; an old callback may be removed or have wrong ordering semantics.
- 1.21.9 changes rendering/resource-reload organization; inspect extraction/submission lifecycle.
- 26.1 changes naming/build assumptions.
- 26.2 changes GPU/render abstractions and moves GUI/HUD APIs. Fabric's article illustrates screen setting through the `gui` object rather than the older direct call, but exact target signatures must still be verified.

Do not keep one giant renderer file with scattered version checks if separate real target modules are clearer. Do not create modules for hypothetical targets either.

## Backend-neutral GPU usage

26.2 includes OpenGL and experimental Vulkan backend support per the release article. Use game-supported GPU/pipeline abstractions rather than raw OpenGL-specific calls for new portable code. Manage buffers/textures/passes with explicit lifecycle and cleanup. Respect render/extraction phases and resource reload.

Reuse immutable render resources where valid, but invalidate them on reload/context changes. Avoid per-frame shader/pipeline compilation, synchronous filesystem access or unnecessary buffer recreation. Do not assume an object is safe to retain forever just because its ID is stable.

Test available advertised backends and combinations with common renderer mods only when those combinations are in scope. If Vulkan was not tested, say so. A compile pass does not prove correct shader bindings, render ordering, transparency or backend compatibility.

## Mixin/performance release gate

Check startup mixin logs, behavior before/after, conflict cases, target-version production artifact and hot-path allocation/cost if relevant. Record unsupported combinations. Do not suppress global errors or disable another mod to claim a universal fix.

Sources: [Fabric porting](https://docs.fabricmc.net/develop/porting), [26.2 article](https://fabricmc.net/2026/06/15/262.html), [Sponge Mixin documentation](https://github.com/SpongePowered/Mixin/wiki) as a lookup entrypoint; verify exact resolved Mixin/MixinExtras version before using features.
