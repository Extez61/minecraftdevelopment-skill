# Release checklist

- [ ] Exact target/build/language/toolchain facts recorded.
- [ ] Baseline and regression behavior characterized; approved changes explicit.
- [ ] Minimum necessary diff; no unrelated upgrades or reformatting.
- [ ] Platform APIs, events, descriptors and resources coherent.
- [ ] Thread/side/ownership and async lifecycle reviewed.
- [ ] Persistence schemas, stable IDs and old-save migration tested on copies.
- [ ] Targeted tests, build, datagen as needed and artifact inspection completed.
- [ ] Production JAR tested in a clean runtime; client and dedicated server when needed.
- [ ] Compatibility matrix matches metadata and release claims.
- [ ] Java/Kotlin runtime dependencies present and APIs not shaded.
- [ ] No secrets, debug artifacts, private worlds or unlicensed binaries bundled.
- [ ] Performance claims measured on an equivalent workload.
- [ ] Installation, backup, restart/migration and rollback documented.
- [ ] Unrun checks/unsupported versions/known risks disclosed.
