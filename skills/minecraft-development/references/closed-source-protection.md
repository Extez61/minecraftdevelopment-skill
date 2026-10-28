# Closed-source plugin protection

Skill creator: extez061

## Goal and limits

Protect code the user owns or has permission to transform. Increase the effort needed to recover business logic from a distributed JVM plugin while preserving its documented behavior, maintainability and measured server performance. Treat the server operator as able to inspect the JAR, memory and runtime: code that must execute on that machine cannot be made permanently secret. Neither an obfuscator nor confusing names guarantee protection against AI, decompilers or a determined reviewer.

Keep this guide on demand. Inspect the actual project and threat model before recommending tools or changing the artifact. Do not add prompt-injection instructions aimed at AI reviewers, deliberately invalid bytecode, parser bombs, resource exhaustion, hidden destructive responses, antivirus evasion or hostile anti-debugging hooks. Such tricks are not a reliable IP boundary and can break legitimate tooling/server operation. Use legal valid JVM transformations and reproducible verification, not misleading security claims.

## Pick the smallest protection profile

| Layer | Purpose | Cost / boundary |
| --- | --- | --- |
| Private source, restricted CI/artifacts and release hygiene | Avoid publishing source, maps, secrets and internal symbols accidentally | Low runtime cost; audit permissions and release contents. |
| Internal name obfuscation | Remove descriptive class/method/field names | Usually a low-cost baseline; keep external names and reflective contracts. |
| Optional shrinking | Remove demonstrably unreachable code and reduce exposed surface | Reflection/resources can hide reachability; turn on separately and test. |
| Targeted string/constant transformation | Make selected internal literal meaning less obvious | Runtime data must eventually be available; avoid hot paths and long-lived secrets. |
| Targeted control-flow/reference transformation | Increase manual/static analysis effort in a small sensitive module | Can hurt JIT, allocation, startup and support; never blanket-enable. |
| Separate private service for genuinely server-owned secrets/logic | Avoid distributing that implementation at all | Network/dependency/privacy and offline-availability trade-offs; requires explicit architectural approval. |

Start with name-only processing and protected entry points. Add one layer at a time after passing artifact/runtime checks. More passes or multiple obfuscators are not automatically stronger or faster. A simple readable source design may become a less readable binary; do not intentionally sabotage maintainable source or remove tests to confuse analysis.

## Exact toolchain gate

Record game/server/API, Java bytecode/runtime, Kotlin compiler/runtime, Gradle/shading/remapping and obfuscator exact version/license. ProGuard is one baseline option for shrinking/name obfuscation; advanced control-flow/string/reference features depend on the actual selected product. The Zelix feature documentation describes those capabilities, but this library bundles no commercial product/license and makes no claim a particular edition supports the user's class-file version.

Confirm the tool understands the exact class-file level and Kotlin metadata before running it. Java 21 and Java 25 bytecode are distinct; support for Java 21 is not proof of Java 25 support. Inspect the tool's current supported versions and test the resolved artifact. Supply exact server/platform libraries as library inputs rather than embedding/transforming the server runtime. Keep Java module/library inputs consistent with the selected JDK; do not guess a pre-Java-9 rt.jar path.

## Preserve all external roots

Build a keep/contract inventory before obfuscation:

- plugin.yml main class and its loader-required constructor/lifecycle, plus Paper-specific loader/bootstrap entry points if actually used.
- Public API/SPI types and methods consumed by other plugins, including JVM descriptors, generic signatures and relevant annotations. A library consumer is not visible to the plugin's local shrinker.
- Event/command registrations, reflective constructors, annotation-discovered listeners, serializers, ORM/config adapters, dependency injection, Kotlin reflection and generated serialization code.
- Services named in META-INF/services, class names in resource files, resource paths relative to packages, native/JNI method contracts and dynamic class lookups.
- Persisted/configured type names, stable IDs, command names/aliases, permission nodes, localization keys, network/resource identifiers and stored schemas.

Do not assume a command's permission node or saved ID should be obfuscated because it is a string. Those are operator/user interoperability contracts. Dotted Java package names, permission names and world IDs are different namespaces.

Keep the main class name stable as the simplest policy. If adapting resource class names instead, target only verified fields/files and inspect the resulting descriptor; do not apply blind text replacement across every YAML/JSON file. A matching string rewrite does not prove a class was retained. ProGuard keepnames preserves a name only if the class survives shrinking; it is not a replacement for keep at external roots.

## Kotlin and reflection

Decide whether kotlin-reflect, Jackson Kotlin, serializers, coroutines, public Kotlin APIs, default constructors/parameters, companion access, enum names or annotation discovery need metadata. Consult exact obfuscator Kotlin support. Guardsquare documents explicit keep/adaptation for kotlin.Metadata where reflection/library consumers require it; stripping all metadata as a protection shortcut can break runtime behavior.

Generated bridge/synthetic methods, suspend state machines and inline/reified APIs require target compilation and runtime tests. Do not transform/shade another plugin's runtime, indiscriminately relocate kotlin packages or aggressively minimize reflective libraries merely because source-level tests pass. Keep the chosen Kotlin runtime distribution strategy intact.

## Selective higher-cost layers

Use clear threat-driven criteria rather than a long list of tricks:

1. Keep packet handlers, tick loops, pathfinding, inventory/transaction logic and public integration adapters in a low-overhead profile. Do not add reflective dispatch or decrypt a literal for every event.
2. If a licensed tool supports it, trial flow/reference transformations on a small infrequently executed proprietary calculation or policy module. Exclude lifecycle/reflection/serialization boundaries until proven compatible.
3. Apply literal protection only to non-contract internal strings where it meaningfully reduces static understanding. Decrypting/caching once trades CPU for memory exposure; measure lifetime and allocation. Never claim an embedded key or decrypted runtime string remains secret from the operator.
4. Treat per-customer watermark/build markers as traceability, not access control. Minimize personal data, secure the customer/build association and use an explicit support/privacy policy. Do not phone home or collect machine identifiers without approval.
5. Keep critical secrets, private signing keys and authoritative entitlements off the distributed JAR where the design permits. Offline verification can use a public verification key and a bounded signed claim, but the local check remains patchable. Do not invent cryptography or disguise embedded secrets as encryption.

Do not implement VM/interpreter layers, custom native loaders or widespread invokedynamic indirection by default. They add compatibility/operational cost and require a specific justified design, not a promise of AI resistance. Do not stack transforms blindly or use reflection everywhere to confuse decompilers.

## Build pipeline and release provenance

Determine the actual artifact chain: compilation, resource processing, shading/relocation, platform remapping/reobfuscation where required, protection and signing. There is no universal order across Paper/Fabric/NeoForge release eras. Class names consumed by a later remapper must remain intelligible to that stage, and later byte changes invalidate earlier signatures. Preserve required notices/licenses; inspect services/resources at the final output, not an intermediate JAR.

Give each stage an unambiguous input/output. Keep development and distribution artifacts separate so a deploy task cannot accidentally choose the unprotected development JAR. Pin the exact tool/config and retain input/output hashes and a build ID. Do not include mapping files, sources JARs, raw source paths, local secrets or CI tokens in the customer release. Map retention is essential for support; keep it access-controlled per release. If transformations randomize output, record the supported seed/settings or acknowledge the reproducibility limits.

The optional template in the package is a conservative ProGuard fragment, not a turnkey Gradle plugin or tested server build. Resolve the actual inputs/libraries/outputs and all dynamic roots before applying it. Never add ignorewarnings or blanket dontwarn to hide an unresolved dependency.

## Licensing and tamper handling

Follow the owner's explicit distribution terms and third-party licenses. Obfuscation does not remove copyleft/notice obligations, grant redistribution rights or prove ownership. A checksum/integrity test whose expected value ships in the same JAR is patchable. For authenticity, verify signed release metadata using an appropriate trust distribution scheme; a trusted signature does not prove the code is safe.

An approved license flow must have bounded timeouts, rate limits, caching/expiry and a clearly documented outage/grace policy. Do not put network licensing on the tick/packet thread. Request only necessary data, keep secrets out of logs and respect offline usage contracts. On invalid entitlement, reject the relevant protected feature/startup in a documented non-destructive way; never delete worlds, corrupt files, ban players, leak data, kill unrelated processes or covertly download/execute code.

## Performance and functional acceptance

Use the same hardware/runtime, dependencies, workload and enabled features before/after. Measure artifact size, cold/warm startup, class loading, heap/RSS, allocations/GC, p95/p99 MSPT and relevant handler latency. JIT inlining/code size and exception paths matter; name-only changes and flow/dispatch changes need different budgets. Set acceptable regressions with the owner and remove/reduce a layer if it exceeds them. No free/zero-overhead protection claim.

Test the FINAL protected artifact on each actually supported tuple: enable/disable, commands/aliases/permissions, reflective events, integrations absent/present, save/restart, persisted data, serializers/Kotlin reflection, scheduled work, concurrent players and shutdown cleanup. Add a deliberate exception to verify private mapping/retrace support. Run JVM bytecode verification where appropriate, and inspect descriptor/API/service contracts.

For a protection assessment, use authorized local decompilers/bytecode inspection to compare recoverable structure before/after, under a stated time budget. Measure observed analysis effort, not a fictional AI-proof score or a universal delay. Do not upload closed-source JARs/source/maps to online decompilers or third-party AI providers without authorization. A single failed decompiler says nothing definitive about other tools. Document gaps and stop at the approved performance/maintenance budget.

Keep the user-facing summary short: profile applied, protected compatibility boundaries, test evidence and necessary risks. Do not fill the handoff with a catalogue of misleading “anti-AI” tricks.

## Reviewed sources

- [ProGuard usage](https://www.guardsquare.com/manual/configuration/usage): keep versus keepnames, shrinking/optimization, attributes and targeted resource adaptation.
- [ProGuard Kotlin](https://www.guardsquare.com/manual/languages/kotlin): metadata preservation/adaptation for reflection and libraries.
- [Zelix features](https://www.zelix.com/klassmaster/features.html): advertised flow/string/reference/constant transformations; not evidence of a tested configuration or current JVM compatibility.
- [Paper plugin.yml](https://docs.papermc.io/paper/dev/plugin-yml/): main class, commands and permission resource contracts; a current example version is not a requested-target validation.

Reviewed 2026-10-28. No obfuscator, commercial license, transformed plugin or decompiler benchmark was executed while authoring this guide.
