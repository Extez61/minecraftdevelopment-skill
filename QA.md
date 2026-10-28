# Release validation — 1.0.0

## Completed locally

- 73 Python unit/static tests passed for read-only project/mod inspection, metadata handling, navigation, permission/operations/output guidance, Git/native installation contracts, release hygiene and manifest tampering.
- All six skill frontmatters, local Markdown links, fences, JSON and Python syntax passed validation. Each skill router remains below 500 lines.
- Git/native plugin instructions and manual six-folder destinations are documented; Python installation/download/application helpers and their dependent tests were removed.
- The Java SessionGate example/test previously compiled with the JDK 25 compiler using --release 21 and ran successfully. The source is unchanged; this is not a Minecraft runtime test.
- Final ZIP checks include exact file hashes/sizes, empty-file/generated-output/symlink/case-collision checks and isolated Git staging of all files including hidden metadata.

## Python is optional for users

No Python is needed to clone, commit, push, install or use the skills. The remaining Python code is optional read-only analysis and repository-development validation. The developer tests require Python 3.11+. CI runs those checks after push; no hosted CI run has happened here.

## Evidence limits

No live Minecraft server, permission provider, anti-cheat, player action, RCON session, restore drill, performance benchmark, model-behavior evaluation or authenticated GitHub installation was run. Kotlin compilation was not performed. Claude Code is not installed here, so official plugin validation/discovery remains a client acceptance check. No GitHub push, tag, release, npm package or license grant was created by packaging.

Removed installer/download test results are not claimed for this distribution. Git obtains the private repository using the user's existing authorized connection; native Claude plugin management or reviewed folder copying performs installation. A bare link grants no access or execution permission.

## Optional developer checks

From the repository root, using Python 3.11+:

```bash
python tools/validate_pack.py
python -m unittest discover -s tests
python tools/release_check.py --verify-manifest
```

Update MANIFEST.json hashes whenever distributed files change. Local test logs and temporary staging folders are not distributed. Manual eval scenarios have not been executed as agent tests.

## Closed-source protection addition

Four static tests cover routing, stated protection limits/performance requirements, external-contract preservation and a conservative ProGuard fragment. No obfuscator, transformed plugin, commercial tool or decompiler benchmark was executed. The template is not a tested ready-to-run configuration. Python installation remains removed; initial publication version remains 1.0.0.
