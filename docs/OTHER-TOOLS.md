# Other IDEs, coding clients and models — lightweight adapters

Keep the same six skill folders. **The client loads instructions; the model name alone does not provide a skill system.** An IDE, an AI extension and its chosen model are separate layers. This guide adds small interoperability support, not a guarantee of identical behavior across clients.

## Native skill locations verified in official docs

| Client | Repository copy target | Personal target | How to verify/use |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills` | `~/.claude/skills` | Native skill selector/slash invocation |
| OpenCode | `.opencode/skills` | `~/.config/opencode/skills` | Ask the agent to load by exact skill ID; inspect skill-tool access |
| Cursor Agent | `.cursor/skills` or `.agents/skills` | `~/.cursor/skills` or `~/.agents/skills` | Inspect discovered skills/Agent settings; explicitly request relevant skill |
| GitHub Copilot agent mode | `.github/skills` or `.agents/skills` | `~/.copilot/skills` or `~/.agents/skills`, where supported | Verify extension/surface feature support and actual skill attachment |
| OpenAI Codex CLI/IDE extension | `.agents/skills` | `~/.agents/skills` | `/skills` or `$` skill mention in supported clients |
| Gemini CLI | `.gemini/skills` or `.agents/skills` | `~/.gemini/skills` or `~/.agents/skills` | `/skills list`, `/skills reload`, then explicit task request |

Compatibility directories and scope/precedence vary. Avoid duplicates; do not assume every client reads every directory above. Copilot feature availability depends on IDE/extension/surface versions. Local personal folders are not automatically uploaded to a cloud/remote coding environment; install or commit project skills where the actual agent runs, with authorization.

Clone/extract the repository, then copy all six directories under skills/ into the selected client's destination using your file manager or the agent's normal file tools. Preserve each folder's name, references and scripts. Do not copy only SKILL.md or flatten the library. Review existing differences and back up approved replacements; do not overwrite root project instructions/settings or install duplicate skill IDs. No Python setup step is needed.

Sources: [Cursor skills](https://cursor.com/docs/context/skills), [Copilot skill locations](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/add-skills), [Copilot surface support](https://docs.github.com/en/copilot/concepts/customizations/agent-skills), [Codex skills](https://developers.openai.com/codex/skills), [Gemini CLI skills](https://geminicli.com/docs/cli/skills/).

## VS Code and JetBrains

VS Code itself does not load these as an autonomous coding agent. If using Copilot, follow Copilot's skill support; if using a terminal Claude Code/OpenCode session, follow that client's paths. For remote SSH, devcontainers and WSL, install where the agent executes and check file visibility/permissions.

For IntelliJ IDEA and other JetBrains IDEs, distinguish Copilot agent mode from JetBrains AI Assistant and other plugins. Copilot support depends on its current feature matrix. For JetBrains AI Assistant, use a **small router rule**, not the entire reference library as an always-on rule:

1. Copy all six folders into `.agents/skills` for a stable repository reference location.
2. Open Settings → Tools → AI Assistant → Rules, create a project rule, and merge the content from `templates/jetbrains-minecraft-rule.md`.
3. Select the rule's applicability in the IDE (manual/model decision/file patterns as appropriate), and confirm it is attached.
4. Ask the assistant to open the core and actual platform `SKILL.md`, then only the needed references.

The rule approach is a **manual adapter**, not a claim JetBrains AI Assistant natively imports this suite as skills. If the assistant cannot read referenced files, attach their text. Do not rename `SKILL.md` to `.mdc` and claim automatic Cursor rule conversion; native skill directories are preferable where supported.

Source: [JetBrains project rules](https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html).

## Other models, web chat and unverified clients

For Claude, GPT, Gemini, local models or another coding extension without confirmed native skill support:

1. Keep/attach the six-folder library in a location the client can access.
2. Provide the core `SKILL.md` plus the actual platform `SKILL.md`.
3. Attach only references required by the current task. Preserve relative paths if the client can read files; otherwise include their text.
4. Supply exact Minecraft/platform/language/build/side facts and a small task.
5. Ask for source verification, minimal edits, protected invariants and actual test evidence.

Use `templates/manual-model-prompt.md` for a portable starting prompt. Models without file/shell tools can review or propose changes but cannot truthfully claim to have inspected the repository, compiled a plugin or run Minecraft. A directory path written in a chat message does not grant file access.

Small-context models should load the core, one platform and one task reference at a time. Keep a compact fact sheet as the conversation grows; do not paste 26,000 words into every request. Weaker models may need smaller patches and a human diff review. Skill instructions improve guidance but do not create API knowledge, permissions or verified compatibility by themselves.

## Common cross-client safety contract

- No automatic deployment, destructive commands, subagent creation or permissive settings changes.
- Secrets stay in the client's/provider's secure mechanisms, not in repository instructions.
- Existing project instructions and the user's request take precedence over this reusable guidance.
- Always load the real files; do not claim to use a skill based only on its name/description.
- Record what was actually inspected/tested; do not equate discovery with implementation correctness.
