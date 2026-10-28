# Client and model portability

The engineering instructions apply independently of the underlying model. Tool names, skill discovery, permissions and invocation belong to the **client**, not to a model family. Match the actual installed client/version and do not assume Claude Code slash commands work elsewhere.

| Client | Common native project location | Usage note |
| --- | --- | --- |
| Claude Code | `.claude/skills` | Native skill invocation/selector |
| OpenCode | `.opencode/skills` | Ask to load the exact skill ID through the skill tool; V1/V2 installation and configuration differ |
| Cursor | `.cursor/skills` or `.agents/skills` | Confirm discovered skills and workspace/remote scope |
| Copilot agent mode | `.github/skills` or `.agents/skills` | IDE/extension/surface support varies |
| Codex | `.agents/skills` | Supported `/skills`/skill mention workflow |
| Gemini CLI | `.gemini/skills` or `.agents/skills` | Check skill listing/reload and current precedence |
| JetBrains AI Assistant/other clients | A short project-rule/manual router | Not an automatic native skill import claim |

Install all six siblings together. Avoid duplicate IDs across global/project/compatibility folders. Personal local files may not exist in a remote/cloud workspace. Do not silently copy instructions or source to a remote service.

Use the actual client's read/edit/shell tools while preserving the same intent: inspect facts, protect behavior, edit minimally, verify and report. If a tool is unavailable, say so and ask for the required file or provide a proposed step. Never simulate an executed build, benchmark or repository read.

For small-context models, load core + one platform + the needed reference rather than the full library. Keep a concise task fact sheet and work in verifiable steps. Do not weaken validation, thread ownership or data-preservation rules to accommodate the model.

No adapter grants tool permissions, changes authentication, installs applications, enables remote uploads or authorizes extra agents. Install only through the native client or reviewed folder copying when explicitly requested. No Python installation helper is supplied.

Sources: [Claude skills](https://code.claude.com/docs/en/skills), [OpenCode skills](https://opencode.ai/docs/skills), [OpenCode V2 skills](https://opencode.ai/v2/docs/skills), [Cursor](https://cursor.com/docs/context/skills), [Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills), [Codex](https://developers.openai.com/codex/skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/), [JetBrains rules](https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html).
