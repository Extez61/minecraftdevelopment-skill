# Mod lists, loader inventories, modpack compatibility and in-game mod menus

## Distinguish four different requests

1. **Offline inventory:** what metadata is declared by JARs/list files currently on disk?
2. **Runtime inventory:** what the actual loader/plugin manager discovered, loaded or enabled?
3. **Compatibility analysis:** do exact versions, sides, dependency constraints, integrations and behavior work together?
4. **Mod-list UI/integration:** how the mod appears in a client mods screen or supplies a configuration screen?

These are not interchangeable. Ask only when the intent materially changes the work; otherwise use the user's file/context to route correctly. A filename, a modpack manifest and a successfully enabled runtime component are different evidence levels.

## Accept and normalize evidence

Useful inputs: a plain mod list, CSV, mods directory, Fabric/NeoForge metadata, launcher export, `modrinth.index.json`/`.mrpack`, CurseForge `manifest.json`, runtime mod dump, crash report or sanitized startup log. Do not require source code just to inventory installed mods.

Record Minecraft/loader/build, Java, physical side, launcher/server distribution and exact list provenance/time. Preserve unknown values. Prefer stable mod IDs plus versions over display names or filenames. Never infer loader/side solely from a popular mod's name: projects can ship different variants and compatibility changes.

Use `scripts/inspect_mods.py <mods-directory-or-list>` for a bounded offline inventory. It requires Python 3.11+ for standard-library TOML parsing, unlike the simpler Python 3.10+ package tools. It never executes/extracts JARs, downloads missing files, edits mods/config or starts Minecraft.

Examples from an installed core skill's directory:

```bash
python scripts/inspect_mods.py "/path/to/instance/mods" --side server
python scripts/inspect_mods.py "/path/to/export.mrpack"
python scripts/inspect_mods.py "/path/to/manifest.json"
python scripts/inspect_mods.py "/path/to/mod-list.txt"
```

The tool scans only immediate JARs in a chosen directory, caps files/read sizes, parses Fabric and NeoForge/legacy Forge TOML metadata, records dependency kinds/sides/raw version expressions, aliases and nested-JAR references. It recognizes plugin/Quilt descriptors but does not pretend to resolve those ecosystems. It records errors instead of executing suspicious JARs. It is not a malware scanner or sandbox.

Modrinth indexes preserve game/loader dependencies, hashes and environment declarations without downloading URLs or verifying the referenced files. CurseForge export IDs remain unresolved until an authorized lookup. Text/CSV rows remain unverified text, not guessed mod/version identities. Check private content before sharing any list/log/report.

## Dependency analysis procedure

Build an evidence table with archive/source, mod ID/aliases, declared/resolved version, platform, environment, required/optional/recommended dependency constraints, incompatible/discouraged declarations, nested references and confidence.

Separate built-in game/Java/loader requirements from installable mods. Evaluate loader-specific version semantics with its real parser or exact documented rules; Maven ranges and Fabric predicates are not universally interchangeable. Preserve unsupported expressions as unresolved, not compatible.

Account for multiple mod IDs in one JAR, multiple-format JARs, provided aliases and embedded dependencies. A dependency not seen among top-level files may be bundled or loader-provided. The helper therefore says **not observed**, not “definitely missing.” Its conflict flags are candidates because raw version predicates are not evaluated. Do not delete nested libraries or install duplicates automatically.

Check duplicates by actual ID/selected version and loader selection semantics, not filename similarity. A client-only Fabric environment on a requested dedicated server is a useful mismatch signal, not authorization to delete it. For NeoForge, a dependency `side` describes the dependency's applicability, not proof the entire owning mod is client-only/server-only.

Check required versus optional dependencies correctly. An absent optional integration should not be treated as a guaranteed crash. An installed incompatible version can matter even when presence is optional. Cyclic load ordering and early optional class linkage need source/runtime investigation beyond a plain list.

## Runtime mod/plugin listing

Fabric's public `FabricLoader` API offers `getAllMods`, `getModContainer` and `isModLoaded`; inspect exact target types/version metadata before using them. Do not use implementation packages or command-line argument dumps that can leak secrets.

NeoForge's maintained loader source exposes `ModList` APIs including `getMods`, `isLoaded` and container lookup; exact availability, initialization stage and meaning must match the target. A discovered sorted mod list is not by itself proof every mod completed initialization. Do not copy a Forge package name into NeoForge.

For Bukkit/Paper use the actual public plugin manager/description and enabled-state APIs for the resolved target, with appropriate permissions. Mods and plugins are not the same loading system. Do not advertise a client mod inventory from a vanilla protocol connection unless an explicit supported handshake supplies it; absence of a report is not proof no mods exist.

Expose administrative inventory endpoints/commands only with authorization and redaction. Versions can be sensitive operational data. Do not upload players' lists or logs automatically. Keep list generation event-driven/on-demand rather than dumping all metadata every tick.

## Compatibility triage

1. Verify exact game/loader/Java line and intended side.
2. Resolve identity/required dependency and explicit incompatibility candidates.
3. Compare client/server manifests and connection protocol requirements; not all mods need both sides, but new content/network expectations often do.
4. Inspect first meaningful loader error/root exception and relevant mixin/registry/codec conflicts.
5. Identify library/runtime/renderer/worldgen/inventory/protection integration groups without assuming every member conflicts.
6. Reproduce on a disposable copy with a minimal relevant set and controlled additions. Back up saves/config before removing content mods; never binary-search by opening the only world with missing registry content.
7. Test functionality, persistence, connect/reconnect/reload and performance on the actual set.

Do not claim a notorious mod-pair conflict from memory as current fact. Require a matching maintainer issue/release note/reproduction and exact versions. Do not “optimize a modpack” by deleting features, silently disabling security or inventing incompatible pairs. Suggestions should identify evidence, expected behavior impact and reversible steps.

## In-game mod list and config screen support

For Fabric Mod Menu, implement the documented optional client integration and metadata: identity/display name/version, description/authors/license/contact/logo where relevant, language entries and a parent-respecting config screen factory. Check actual API signatures. Keep optional client classes safely isolated so a server without Mod Menu still boots.

For NeoForge, provide correct `neoforge.mods.toml` metadata and use its target-version mod screen/config-screen hook where available. Match loader lifecycle; do not reference screen classes from shared static fields. Cloth Config is an optional screen builder, not a requirement for every config UI.

Test mod-list display, localization, long names/descriptions, missing logo fallback, config open/save/cancel/back navigation, optional dependency absence and dedicated-server boot. Do not turn mod-list support into an invasive custom launcher or a new permission system without request.

## Report format

Use `templates/mod-compatibility-report.md` from the distribution for substantial reports, or a concise equivalent: target/provenance → confirmed inventory → confirmed blockers → candidates/unresolved → smallest safe actions → tests/rollback. Distinguish “declared,” “observed,” “loaded,” “enabled,” and “runtime tested.” No automatic downloads, deletions or universal compatibility verdicts.

Sources: [Fabric metadata](https://docs.fabricmc.net/develop/loader/fabric-mod-json), [Fabric Loader public source](https://github.com/FabricMC/fabric-loader/blob/master/src/main/java/net/fabricmc/loader/api/FabricLoader.java), [NeoForge metadata](https://docs.neoforged.net/docs/gettingstarted/modfiles), [NeoForge loader ModList source](https://github.com/neoforged/FancyModLoader/blob/main/loader/src/main/java/net/neoforged/fml/ModList.java), [Modrinth format](https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack), [Mod Menu](https://github.com/TerraformersMC/ModMenu).
