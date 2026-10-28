# Verification ladder and release gate

## Use the cheapest valid check first

1. **Static review:** target facts, imports, ownership, resources, descriptor and registration consistency.
2. **Pure unit tests:** algorithms, permissions/validation boundaries where isolated, cooldown math, state transitions, schema transforms and transaction policy.
3. **Framework tests:** use an existing compatible plugin mock harness or loader GameTest setup when supported. Verify task names with `tasks --all`; do not invent tasks.
4. **Module build:** compile Java and Kotlin and run configured checks; inspect exact failures.
5. **Artifact inspection:** production task, descriptor expansion, dependency inclusion and absence of unwanted files.
6. **Clean runtime:** install the packaged artifact in a disposable exact-version server/client with the actual dependency set.
7. **Compatibility matrix and load:** run advertised targets, representative workloads and integration combinations.

Mock-based plugin tests do not prove real chunk behavior, packet transport, mapping correctness, Folia ownership or client rendering. An integrated client server does not prove a dedicated server avoids client-only linkage. A passing build does not prove correct entrypoint metadata.

## Runtime regression checklist

### All projects
- Cold startup and clean shutdown; actionable required-dependency failure.
- Happy path and invalid input, permission denied, missing state, full inventory, timeout/failure.
- Duplicate input, rapid repeated actions and late callbacks.
- Logout/reconnect, death/respawn, dimension/world change and world unload.
- Persistence after restart, corrupt/missing optional data, old-schema fixtures.
- Resource/config reload only if advertised; no duplicate tasks/listeners.
- Missing optional integration and intended integration versions.
- Logs without unexpected warnings, stack traces or secret leakage.

### Plugins
- Correct command/permission declaration, console behavior, registration and tab completion.
- Event cancellation interoperability and GUI transfer variants.
- No async world/inventory access, task leaks, invalid late callbacks or stale player references.
- Spigot runtime test if Spigot support is claimed; Folia runtime/ownership tests if Folia is claimed.

### Mods
- Dedicated-server boot and separate client boot for shared mods.
- Client connects to server; initial sync, tracking changes, late join, respawn and reconnect.
- Registry IDs, recipes, loot, models, language files and generated data load.
- Side separation: no client-class initialization in common/server paths.
- Mixin application and conflicts; serialization round trips and old-save migration.
- Available rendering backends when custom renderer support is claimed.

## Evidence table

For each executed check record command/scenario, exact target build, result, important output and limitation. Use “not run,” “blocked by dependency resolution,” “not available in this environment,” or “manual steps provided” honestly.

Do not install a game/server, download untrusted executables, accept EULA or deploy without authorization. Do not run a clean task that removes user-owned generated artifacts without checking ownership. Preserve a dirty worktree; do not reset, stash or commit automatically.

## Release artifact gate

- Correct platform/game-family artifact name and version.
- Java runtime and Kotlin/library requirements documented.
- Descriptor, entrypoint, dependencies, permissions and API version match implementation.
- No broad unsupported MC range, no development JAR, no bundled API/server classes.
- No debug commands, tokens, personal data, test worlds or temporary logging.
- Stable IDs and config keys preserved, migrations tested on copies.
- Changelog distinguishes bug fixes, behavior changes and performance claims.
- Installation, backups, migration and rollback steps are reproducible.

## Performance evidence gate

A correctness test is not a benchmark. State workload, warmup, samples, profiler and absolute/relative results. Compare the same features enabled. If change removes a feature or reduces update frequency, label it a tradeoff and request approval.

## Skill-suite validation versus product validation

Checking this library's Markdown links, YAML frontmatter and helper scripts proves packaging integrity only. It does not prove a generated mod/plugin compiles or an AI follows the instructions. Agent scenario evaluation is described in the package's `evals/scenarios.md`; run it explicitly before claiming model-level validation.
