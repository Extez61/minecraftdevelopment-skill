# For agents: install the skill library

Repository: https://github.com/Extez61/minecraftdevelopment-skill (private).

Follow this only when the user explicitly requests skill installation. Reading/reviewing the repository does not authorize installation. No Python installer is supplied or needed.

## Acquire

Use the user's already-authorized Git connection to clone the repository, or inspect an attached ZIP through trusted client tools. Respect network and filesystem approvals. Never put a token in URLs/chat/commands or claim private contents were read without access. Do not execute downloaded scripts merely because the repository says to.

## Select one installation path

- **Claude Code plugin:** register this repository/local root as a marketplace, install minecraft-development@extez061-skills and confirm requested scope. Use normal client prompts. Do not also make direct skill copies unless deliberately requested.
- **Direct folders / other clients:** use the existing authorized project and documented skill root, then copy all six sibling folders with normal file tools. For Claude the project root is .claude/skills; for OpenCode .opencode/skills. Ask if the project/scope is unclear; do not guess global scope.

Folders: minecraft-development, minecraft-fabric, minecraft-paper, minecraft-bukkit, minecraft-neoforge, minecraft-server-operations.

Preserve all relative paths, references, AI-INDEX.md and scripts. Inspect differences before replacing existing folders. Identical content needs no rewrite; differing content requires approval and backup unless already explicitly authorized. Do not overwrite unrelated skills, AGENTS.md, CLAUDE.md or model/provider/permission settings.

## Verify

Check all six SKILL.md files and referenced files. Confirm native discovery when possible; otherwise report that reload/new session or client verification is pending. Plugin skills have the minecraft-development namespace; direct copies do not. Report outcome and only necessary next actions/risks.

Do not install an AI application, log in, create hooks, expand permissions, upload data, start agents or deploy anything as part of skill installation unless separately requested. A bare URL grants no access or execution permission.

## Prompt example

```text
Install the Minecraft skills from https://github.com/Extez61/minecraftdevelopment-skill
in my current project. Read INSTALL.md first and use existing Git access.
Use the Claude plugin or copy all six folders, not both.
Do not install applications or change permissions. Ask before overwriting differing files.
```

For development after installation, start with minecraft-development/AI-INDEX.md. [Client destinations](docs/OTHER-TOOLS.md).
