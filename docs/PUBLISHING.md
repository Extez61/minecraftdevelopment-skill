# Publish to GitHub

Repository: https://github.com/Extez61/minecraftdevelopment-skill (private).

## Prepare

Extract the ZIP and open the inner `minecraftdevelopment-skill` directory. README.md, skills/, tools/ and hidden .claude-plugin/ must be at the repository root, not inside a second nested folder. Include .github/, .gitignore and .gitattributes too.

Use Git and an account with repository write access. Authenticate with your existing credential manager, GitHub CLI or SSH setup. If GitHub CLI is installed, `gh auth login` provides its own browser flow; no credentials belong in these files. HTTPS GitHub push does not use your account password. Do not paste a token into the remote URL.

The package does not select a distribution license for the owner. Choose appropriate license terms before making it public or permitting redistribution; no MIT/Apache grant is assumed merely because source files are available.

## First push to the empty repository

Run from the extracted directory, after checking `git status` and file contents. These commands initialize local history and publish it when YOU execute them:

```bash
git init
git branch -M main
git remote add origin https://github.com/Extez61/minecraftdevelopment-skill.git
git add .
git status --short
git diff --cached --stat
git commit -m "Add Minecraft development and server operations skill suite"
git push -u origin main
```

Python is not required to initialize, commit, push or install skills. Optional developer checks require Python 3.11+ and are documented in QA.md; CI runs them after push. Stop if a check you run fails. If Git requests a commit identity, configure your chosen name and GitHub no-reply email locally; never guess or publish your private identity.

If origin already exists, inspect `git remote -v` first. Only if you intend to change it:

```bash
git remote set-url origin https://github.com/Extez61/minecraftdevelopment-skill.git
```

Do not run `git init`/branch rename blindly inside an unrelated repository. If the remote is no longer empty or rejects the push, fetch and inspect both histories before merging. Do not force-push, reset or discard existing work as a workaround.

## Install from a private repository

Users and agents need authorized Git access. A public browser fetch does not authenticate this private repository.

```bash
git clone https://github.com/Extez61/minecraftdevelopment-skill.git
cd minecraftdevelopment-skill
```

Then use either the local Claude marketplace or manual six-folder copy documented in README.md. A remote `/plugin marketplace add Extez61/minecraftdevelopment-skill` also requires the client's Git authentication and repository access; a bare link does not grant it. Account permissions and enterprise marketplace policies can still block installation.

## Release checks

Keep plugin version/changelog and release manifest aligned. CI runs on Python 3.11 and 3.13 after push; adding the workflow is not evidence it has already run. Before claiming Claude plugin validation, run `claude plugin validate .` on an installed current CLI and test discovery/installation. This authoring environment did not have that CLI. No push is performed by the package or these instructions themselves.

## First release version

The initial plugin/package version is 1.0.0. A source push does not automatically create a GitHub Release or tag. If you want a version tag after reviewing and pushing the release commit, explicitly run `git tag v1.0.0` and `git push origin v1.0.0`. Creating a GitHub Release is a separate optional action. Do not recreate/overwrite an existing tag.
