# Exact-version policy and compatibility boundaries

## Contents
1. Support contract
2. Toolchain and mapping eras
3. Intermediate release boundaries
4. How to verify a symbol
5. Multi-version release policy

## 1. Support contract

The requested research interval is Minecraft Java **1.21.1 through 26.2 inclusive**. Version names changed: **26.2 is not 1.26.2**. Do not compare versions as floating-point numbers, lexicographic strings, or “second dot component only.” Keep an ordered explicit list of tested targets; read the platform's version parser/range semantics before declaring metadata.

Not every loader, mod dependency, integration or server distribution necessarily publishes an artifact for every Minecraft patch. Minecraft release availability and platform support are separate facts. Resolve actual artifact metadata instead of manufacturing a dependency string. Snapshots/pre-releases are out of the default compatibility promise.

“Supported scope” means the skill can guide investigation across the interval. It does not imply one binary, one source tree, one mapping namespace, one JDK, or full runtime verification across the interval.

## 2. Toolchain and mapping eras

| Era | Game Java baseline | Fabric naming/build concern | Plugin/NeoForge concern |
| --- | --- | --- | --- |
| 1.21.1–1.21.11 | Java 21 | Obfuscated game; Yarn or Mojang mappings according to project; use matching remapping Loom | Exact API/loader and build plugin matter; do not use 26.x build coordinates |
| 26.1, 26.1.1, 26.1.2 | Java 25 | Unobfuscated game; official naming; new non-remapping Loom workflow | Paper no longer supports the old reobfuscation path; NeoForge toolchain/template must match |
| 26.2 | Java 25 | Non-remapping workflow plus substantial rendering/registration changes | Resolve matching platform artifacts; do not silently use 26.3 examples |

Java requirements come from official Fabric/NeoForge setup and release guidance; do not extrapolate Java 21 to all future Minecraft versions. The Gradle daemon JDK, compiler toolchain, Java `--release`, Kotlin `jvmTarget`, API dependency bytecode, and server/client runtime are **different settings**. A JDK 25 daemon may compile a Java 21-compatible library, but it does not make 26.x API references safe on 1.21.1.

For Kotlin, verify the exact Kotlin compiler supports the intended JVM target and is compatible with the selected Gradle version. Do not set `jvmTarget=25` with an older compiler that does not support it. A lower bytecode target can be valid on a newer runtime if verified, but the runtime's game API baseline still applies.

### Fabric 26.1 boundary

The official 26.1 article instructs migration from remapping Loom plugin IDs to `net.fabricmc.fabric-loom`, from `modImplementation`/`modCompileOnly`-style configurations to ordinary `implementation`/`compileOnly`, and from `remapJar` to `jar`. Apply these changes **only** to the correct era. Keep legacy remapping for older target modules that require it.

Fabric API also renamed symbols to align with official names; for example, the release article describes `ItemGroupEvents` becoming `CreativeModeTabEvents`. A mappings migration does not solve every API migration. Loom's mapping migration does not support Kotlin source according to the Fabric mappings guide; use the documented Kotlin-capable migration tooling or review Kotlin changes manually.

### Paper 26.1 boundary

Paper's project setup documents old API coordinates as `{VERSION}-R0.1-SNAPSHOT` through 1.21.11 and new coordinates in the form `{VERSION}.build.<build>-<status>` from 26.1. Resolve and pin an actual build for releases. A documented dynamic example is discovery guidance, not a reproducibility strategy. Do not invent `26.2-R0.1-SNAPSHOT` for Paper.

`paperweight-userdev` documents that reobfuscation to old Spigot runtime mappings does not work for 26.1+. Keep NMS use isolated and exact-version tested; unobfuscated names do not stabilize internal APIs.

## 3. Intermediate release boundaries

Use the following as **research triggers**, not interchangeable API recipes. Exact signatures still require target-version source inspection.

| Target family | Known migration hotspot to examine | Primary reading |
| --- | --- | --- |
| 1.21.1 baseline | Data-driven enchantments, components, registry-aware serialization, singular data-pack paths | Fabric 1.21/1.21.1 article; versioned NeoForge 1.21.1 docs |
| 1.21.2–1.21.3 | Entity render states; block/item settings and registry keys; result semantics; recipes | Fabric 1.21.2/1.21.3 article |
| 1.21.4 | New item model definition files under `assets/<namespace>/items/`; model pipeline changes | Fabric 1.21.4 article |
| 1.21.5 | NBT getters and missing-value handling; HUD API and GameTest changes | Fabric 1.21.5 article |
| 1.21.6–1.21.8 | Block entity serialization views; rendering and HUD rewrites; datagen changes | Fabric 1.21.6/7/8 article |
| 1.21.9–1.21.10 | Resource Loader API v1; renderer extraction/submission; key input changes | Fabric 1.21.9/10 article |
| 1.21.11 | Game-rule identifiers/registration; environment attributes; final obfuscated line | Fabric 1.21.11 article |
| 26.1 and hotfixes | Java 25, unobfuscation, Fabric API names/build changes; recipe/item changes | Fabric 26.1 article; corresponding NeoForge primer |
| 26.2 | GPU backend abstractions, GUI/HUD movement, resource-key-based datagen/registry restructuring | Fabric 26.2 article; NeoForge 26.2 vanilla migration primer |

Yarn-specific terminology in old articles may differ from Mojang-mapped NeoForge or later Fabric names. For example, a historical NBT “view” concept and its target-version class name should not be assumed identical. Read generated source.

26.2 adds an experimental Vulkan backend alongside OpenGL according to Fabric's release article. Raw OpenGL assumptions are not backend-neutral. New renderer code should use supported game abstractions, with explicit runtime tests on available backends.

## 4. How to verify a symbol

1. Resolve the build dependency; inspect `dependencies`/`dependencyInsight` for the relevant configuration when needed.
2. Open its source/Javadoc or target-version generated sources.
3. Confirm fully qualified class, method parameters/return, generics, side, event bus, threading, lifecycle, deprecation and experimental status.
4. Check one matching official example if the semantics remain unclear.
5. Compile a minimal use in the actual module. Do not add a sample dependency merely to make an unrelated symbol appear.
6. If online evidence conflicts, prefer exact resolved source and matching release docs; record the discrepancy.

Current documentation often defaults to a newer version. A header saying “26.2” and prose saying “26.1” may reflect shared guidance or stale text. Do not resolve the conflict by silently substituting the newest API. A search excerpt is a lead, not enough proof for a complicated signature.

## 5. Multi-version release policy

Separate source compatibility, binary compatibility, save compatibility, network compatibility and metadata acceptance. Passing one does not prove the others.

- Prefer one exact target until the user actually needs a wider range.
- For public-API-only plugins, compile against the intended minimum API, avoid newer symbols, and runtime-test representative boundaries and every advertised target as feasible.
- For mods and NMS, prefer separate version-family artifacts/modules where APIs diverge; do not hide a broad catch/reflection soup in one JAR.
- For a 1.21.1 + 26.2 product, consider a pure Java-21-compatible domain module and platform/version adapters compiled with their own toolchains. Add this architecture only if multi-target distribution is required.
- Name release artifacts unambiguously by platform and game family. Declare only verified version ranges and required runtime dependencies.
- Report unknown or untested combinations explicitly. Never change a metadata interval to make an incompatible JAR load.

Sources: [Fabric 26.1](https://fabricmc.net/2026/03/14/261.html), [Fabric mappings](https://docs.fabricmc.net/develop/porting/mappings), [Fabric 26.2](https://fabricmc.net/2026/06/15/262.html), [Paper setup](https://docs.papermc.io/paper/dev/project-setup/), [Paper userdev](https://docs.papermc.io/paper/dev/userdev/), and the dated release links in [sources.md](sources.md).
