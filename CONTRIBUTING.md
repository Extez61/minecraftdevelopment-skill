# Contributing

Keep changes focused, version-specific and behavior-preserving. Read AI-START-HERE.md for routing; do not preload every guide.

- Keep six sibling skills and their relative references intact.
- Use English for skill/reference content. Keep installation guidance in README.md and the agent-facing INSTALL.md; avoid duplicate setup documents.
- Verify platform APIs using authoritative sources for the exact release. Record uncertainty instead of guessing.
- Keep source attribution, creator extez061 and repository metadata consistent.
- Add regression tests for changed Python behavior; distinguish static checks from live game/model tests.
- Never commit player data, credentials, server worlds, binaries or raw private logs.

From the repository root, using Python 3.11+:

```bash
python tools/validate_pack.py
python -m unittest discover -s tests
python tools/release_check.py
```

The release check excludes local Python cache directories but distributions must not include them. Before a release update MANIFEST.json hashes to match every distributed file, then run `python tools/release_check.py --verify-manifest`. Do not claim a platform/provider integration was tested unless it was actually run.

Discuss license/redistribution terms with the repository owner before distributing third-party code. Third-party projects linked in the guides are not bundled dependencies.
