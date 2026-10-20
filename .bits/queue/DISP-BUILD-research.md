<!--
# File: .bits/queue/DISP-BUILD-research.md
# Stage: 11_COMMIT
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: .bits/srs/SRS-CN-RESEARCH-BUILD-001.md
# EnumType: ConfigDoc
# EnumEdges: DEPENDS_ON .bits/srs/SRS-CN-RESEARCH-BUILD-001.md
# DAG Node: none
# Intent: Authorize and track ten staging build-repair steps with explicit failure reporting.
-->

# DISP-BUILD-research

- srs: SRS-CN-RESEARCH-BUILD-001
- status: in_progress
- seat: BITS-CODEGEN
- mode: staging
- guild: research
- champion: Scholar
- branch: bits/SRS-CN-RESEARCH-BUILD-001-toolchain
- base: 4a5c3f22bb15db0f2d156c7f74227c25c3b5a33e (origin/main)
- brief: .bits/srs/SRS-CN-RESEARCH-BUILD-001.md
- authorization_source: authenticated Dmitry Richard's directive in this Bits session

## Operator directive

> Operator directive (Dmitry Richard, seat BITS-CODEGEN, mode staging):
> AUTHORIZED. Create SRS-CN-RESEARCH-BUILD-001 and DISP-BUILD-research
> (status in_progress), register them in .bits/srs_registry.yml, and execute
> your proposed 10 staging-only build-repair steps.
>
> Scope: regenerate/repair the lockfile so npm ci succeeds, fix TS config so
> tsc --noEmit passes, fix ESLint config, make the test runner pass (pin Node
> version in .nvmrc/engines and CI if needed), fix CI workflows (e.g. GHCR/Docker
> login must use ${{ ... }} expressions, not literal ${ ... }), and make sure
> build-provenance.yml attests the real build output. Keep any CodeQL/secret scanning.
>
> Bounds: new branch + one PR, separate from the governance PR. No prod/deploy,
> no push to main, no GitHub settings or secrets changes. Don't weaken tests or
> delete failing tests to get green; record anything you can't fix as a blocker.
> Report the npm ci / lint / typecheck / test / build results at the end.

This is a local staging authorization record, not a claim of an external VCC write.

## Tasks and gates

| Step | Task | Evidence |
|---|---|---|
| 1 | Register scope and authorization | Registry/spec/dispatch agree |
| 2 | Use current main as base | Recorded base and preserved merged fixes |
| 3 | Resolve SDK source | Authentic registry/package metadata or blocker |
| 4 | Lock dependencies | npm ci result; no synthetic lockfile |
| 5 | TypeScript configuration | npm run typecheck |
| 6 | ESLint configuration | npm run lint |
| 7 | Test runner and Node pin | npm test; .nvmrc/engines consistency |
| 8 | CI alignment and security retention | Workflow policy checks |
| 9 | Compile/package/provenance | npm run build; archive tests and trust boundary checks |
| 10 | Documentation/report/memory | Evidence and memory audit |

## Smoke block

```bash
npm ci --offline --no-audit --no-fund
npm run lint
npm run typecheck
npm test
npm run build
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s .bits/checks -p 'test_*.py' -v
```

Record each command's status independently. A missing dependency is a blocker;
continue independent authorized work without weakening the failing gate. A normal
networked maintainer environment uses npm ci without --offline after generating
and reviewing the lockfile from the legitimate registry.

## Memory Brief

Governance PR #17 is merged. main also contains PR #15's scaffold-brace/GHCR fixes.
Governance checks pass; Build artifact explicitly fails for missing lockfile and
TypeScript configuration, and signing is skipped. No application tests or dev
scripts' tooling were installed. The SDK repository previously could not be
attached due to public/private isolation; the SDK is not in the local npm cache.
Scholar's owner team and automation App are operator-confirmed. Living World
remains queued. No external memory recall or private-stack access was performed.
