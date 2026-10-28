# Minecraft Development Skills

> One skill suite. Build, optimize, and manage Minecraft.

**v1.0.0 · By extez061 · Java & Kotlin · Minecraft Java 1.21.1–26.2**

AI skills for **Fabric, Paper, Bukkit/Spigot, NeoForge and server operations**.

## Install with Git + Claude Code

No Python is required to install or use the skills. Git obtains the repository; Claude Code loads its plugin. **Private repository:** your GitHub/Git account needs access. Never put a token in the URL.

```bash
git clone https://github.com/Extez61/minecraftdevelopment-skill.git
cd minecraftdevelopment-skill
claude plugin marketplace add .
claude plugin install minecraft-development@extez061-skills
```

Or inside Claude Code, once the repository files are on GitHub and Git access is configured:

```text
/plugin marketplace add Extez61/minecraftdevelopment-skill
/plugin install minecraft-development@extez061-skills
```

Confirm the scope/installation in the plugin UI if prompted, then reload/restart the client if needed. Private access and enterprise marketplace policies still apply. Use the repository, not a raw README URL. Package files must be present in GitHub before remote installation works.

### Use a skill

```text
/minecraft-development:minecraft-paper
Inspect this project and fix the issue while preserving existing behavior.
```

| Skill | Purpose |
| --- | --- |
| minecraft-development | Shared Java/Kotlin engineering and version policy |
| minecraft-fabric | Fabric mods |
| minecraft-paper | Paper plugins |
| minecraft-bukkit | Bukkit/Spigot plugins |
| minecraft-neoforge | NeoForge mods |
| minecraft-server-operations | Configuration, profiling, players, permissions and backups |

All plugin invocations use `/minecraft-development:<skill-name>`.

## OpenCode and direct folder installation

Clone or extract this repository. Copy all six directories inside `skills/` into the existing project's destination:

| Client | Project destination |
| --- | --- |
| Claude Code, without the plugin | .claude/skills/ |
| OpenCode | .opencode/skills/ |
| Cursor | .cursor/skills/ |
| GitHub Copilot, supported surfaces | .github/skills/ |
| Codex | .agents/skills/ |
| Gemini CLI | .gemini/skills/ |

Use your file manager or the agent's normal file tools. Copy the folders with their references/scripts; do not flatten them or copy only SKILL.md. Review and back up differing existing folders before replacing anything. Do not install duplicate plugin/direct copies.

Restart/reload your client as needed. With direct copying, Claude uses `/minecraft-paper`; in OpenCode ask: “Load minecraft-development and minecraft-fabric, then inspect this project.” Claude `/plugin` commands are **not** OpenCode commands. See [other clients](docs/OTHER-TOOLS.md) for discovery limitations and manual adapters.

## Install the AI application only if needed

These npm commands install the applications, NOT this skill library. Review current official requirements and select the application/major version you actually need.

```bash
# Claude Code (Node.js 22+ for this npm method)
npm install -g @anthropic-ai/claude-code

# OpenCode V1
npm install -g opencode-ai
```

Claude Code's native installation is also available upstream. OpenCode V2 has a different install path; do not install both major lines over each other. Provider authentication/billing is separate. [Claude setup](https://code.claude.com/docs/en/setup) · [OpenCode V2 docs](https://opencode.ai/v2/docs).

### Visual Studio Code

Install the official Claude Code extension from Extensions or, with `code` on your PATH:

```bash
code --install-extension anthropic.claude-code
```

Use `/plugins` in the Claude panel to manage plugins, or use the CLI in the terminal. The extension does not put `claude` on your terminal PATH. VS Code and Visual Studio are different products; this command is for VS Code. Other editors can use the standalone CLI or [manual adapter](docs/OTHER-TOOLS.md).

## What's included

- Version-specific development, networking, threading, persistence and migration guides.
- Behavior preservation, measured optimization, tests and short, practical replies.
- Permission nodes/defaults, action guards, LuckPerms and mod permission APIs.
- Owned closed-source plugin protection: keep rules, Kotlin/reflection safety and measured obfuscation trade-offs.
- Defensive anti-cheat, mod-list/API integration and optional companion-skill guidance.
- Server YAML/properties, spark/TPS/MSPT, Java/GC, players, OP/deop, maintenance, backups and proxy/RCON safety.
- On-demand AI navigation: [start here](AI-START-HERE.md), then the installed [file map](skills/minecraft-development/AI-INDEX.md).

## Repository layout

```text
.claude-plugin/   Claude plugin and marketplace metadata
.github/         Developer validation workflow
skills/          Six skills and on-demand references
docs/           Setup, clients and publishing
templates/      Optional project/task fragments
examples/       Java/Kotlin examples
tests/          Optional developer tests
evals/          Manual AI scenarios
tools/          Optional developer validation (not installers)
```

Optional read-only inspection tools and developer tests use Python; skill installation does not. See [validation](QA.md) if developing this repository.

## Notes

This is an instruction library, not a Minecraft mod/plugin JAR or universal compatibility layer. Exact API/game versions still require verification. Live game/client/provider tests and token savings are not claimed. No hooks, telemetry, automatic punishment or extra agents are configured.

[Agent installation](INSTALL.md) · [Publishing](docs/PUBLISHING.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Research](RESEARCH.md)

Sources: [Claude setup](https://code.claude.com/docs/en/setup), [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [VS Code](https://code.claude.com/docs/en/vs-code), [OpenCode V1](https://opencode.ai/docs).
