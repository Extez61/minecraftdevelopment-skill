# Token efficiency without correctness shortcuts

Skill creator: extez061

## Always-on compact contract

Read the core router, one relevant platform router, and only the references needed for the current task. Keep detailed guides available on disk instead of pasting them into CLAUDE.md, AGENTS.md, every prompt, or every platform file. The platform router should point to the core; do not read the same unchanged file twice in one active context.

Token economy is a resource policy, not permission to weaken tests, skip API verification, change gameplay, reduce compatibility, or hide uncertainty. No fixed savings percentage or unchanged model quality is guaranteed. Do not silently change model, reasoning effort, provider, context limits, or routing to save cost.

## Retrieval ladder

1. Use facts already established in the active task. Recheck only when evidence changed or a consequential uncertainty remains.
2. Discover filenames/modules with a bounded file listing. Exclude generated build output, caches, dependency trees, worlds and secrets.
3. Search exact relevant symbols or errors using scoped search. Read a small surrounding range, then callers/resources/tests if needed. Never treat a truncated result as a full search.
4. Read the complete affected function or lifecycle when a local excerpt cannot establish behavior. Follow dependency and threading boundaries, not an arbitrary token ceiling.
5. For version-sensitive APIs, inspect the exact resolved source/Javadoc or matching official documentation. Fetch one focused question, not a complete documentation site. Reuse verified version/signature facts until dependencies change.
6. Expand scope on unresolved evidence: multiple call paths, side effects, data migrations, security, race conditions or ambiguous protocol semantics. Stop retrieval when the required evidence is sufficient; do not cycle through equivalent searches.

## Tool output and build costs

- Save noisy compiler/test output locally; return command, exit status, test counts, decisive failure lines and an accessible log location. Preserve the full log for investigation. Do not report PASS from an empty/truncated summary or a pipeline whose exit status came from a filter.
- Group independent read-only inspections. Keep dependent edits/builds ordered. Prefer an existing deterministic tool over regenerating a script every time; review scripts before running them.
- Test the touched unit/module first. Then run the necessary integration, artifact and runtime gates for the change. A packet, scheduler, mapping or packaging change may require more than unit tests.
- Use incremental builds and an already-running approved Gradle daemon where appropriate. Do not repeatedly clean, refresh dependencies, resolve every release or restart servers without cause. Never alter toolchain flags to conceal an error.
- Avoid duplicating generated code or full diffs in chat. Persist required code in files; report the relevant change and tests. Do not replace runnable source with ellipses to shorten output.

## Small task-local fact sheet

Keep only: target versions/language/mappings; behavior invariants; changed files; verified API signatures with evidence; commands/results; unresolved blockers and next action. Store no secrets. A tiny fix needs no permanent planning document. Before a context handoff, preserve exact paths, units, negations, constraints and test failures; distinguish observed facts from assumptions. Reopen original evidence if a summary cannot support a risky decision.

## Responses and companion compression

Use the user's language. Answer with outcome, necessary evidence, risks and next step; omit repeated plans, narrating routine calls and decorative tables. For tiny changes, a few lines suffice. Keep code, commands, API names, diagnostics, paths, version numbers, units, negations and safety conditions exact. Full clear sentences win whenever compression creates ambiguity.

Caveman support affects presentation, not code semantics or source comments. Optional proxies, hooks, cloud compression, telemetry, keep-warm requests or model routing are separate products/features: never enable them just because the voice skill is present. See [companion skills](companion-skills.md).

## Measurement and stop rule

Use actual client usage counters when available. Compare like-for-like task, model, cache state, verification scope, wall time, output artifacts and correctness; do not substitute word count for exact tokens. Report not measured when counters are absent. A smaller prompt that causes repeated failures is not an improvement. Stop when acceptance criteria and required verification pass; do not invent extra work to fill the context.

## User-visible brevity

Keep ordinary completion messages to outcome, essential evidence and next action/risk. Omit internal tool choices, unsolicited “X instead of Y” comparisons and long notes. Do not add explanatory prose to source comments/README merely to describe your work. Preserve existing meaningful comments and required documentation. Expand only when the user asks or a consequential decision needs explanation; never omit a failed check or safety constraint.
