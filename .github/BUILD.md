<!--
# File: .github/BUILD.md
# Stage: 06_PLAN
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: package.json, .nvmrc, tsconfig.json, .github/PROVENANCE.md, .bits/queue/DISP-BUILD-research.md
# EnumType: Doc
# EnumEdges: DEPENDS_ON package.json; DEPENDS_ON .nvmrc; DEPENDS_ON tsconfig.json; DEPENDS_ON .github/PROVENANCE.md; DEPENDS_ON .bits/queue/DISP-BUILD-research.md
# DAG Node: none
# Intent: Document reproducible build recovery and distinguish offline checks from a successful clean build.
-->

# Research build setup and recovery

Use Node **24.13.0** (`nvm use`) and npm **11.6.2**, matching `.nvmrc`,
`package.json` engines and CI. Docker uses the same Node release. TypeScript,
ESLint and their parser/plugin versions are explicitly declared. The runtime
still requires the real `@citadel-guilds/sdk` and `nats` packages.

## Current blocker

This staging sandbox has no cached SDK, NATS or Node type definitions and does
not support internet package installation. Offline lockfile generation fails
with `ENOTCACHED` for `@citadel-guilds/sdk`. The SDK's legitimate package registry
must be confirmed by its owner; an earlier attempt to attach the SDK repository
was rejected by public/private repository isolation. This does not prove that
the SDK is unpublished. No registry mapping or credential has been invented.

**No lockfile is supplied until the real dependency graph can be resolved.**
`npm ci` therefore remains blocked. Do not treat the other local checks as proof
of a clean install. A fake SDK, ambient module shim or source-only artifact would
hide the failure and is not an acceptable build repair.

## Finish dependency locking in an authorized environment

Confirm the SDK package source and access through the existing organization
package process. Do not put credentials in source control or paste them into
issues. With that registry available:

```bash
nvm use
node --version  # v24.13.0
npm --version   # 11.6.2
npm install --package-lock-only --ignore-scripts --no-audit --no-fund
npm ci
npm run lint
npm run typecheck
npm test
npm run build
```

Review the generated lockfile's resolved sources/integrity hashes and SDK origin.
Include `package-lock.json` and its CGRF sidecar in the same build-repair dispatch,
then rerun the full gate sequence from a clean install. Do not hand-edit transitive
metadata or generate a lockfile from only a subset of required dependencies.
The commands above describe the remaining dependency-enabled work; they have not
succeeded in this sandbox.

## Local checks and output

- `npm run lint`: recommended ESLint/TypeScript rules for source, tests and config.
- `npm run typecheck`: `tsc --noEmit` with strict checking of all `src/**/*.ts`.
- `npm test`: Node's built-in test runner (no previously existing Vitest tests
  were removed). Tests exercise the existing health response and actual cleanup
  command without contacting the SDK, NATS or production. Coverage thresholds are
  80% for lines/branches/functions of loaded source; health.ts is currently the
  only exercised runtime module. This is not whole-application coverage.
- `npm run build`: remove stale `dist/`, then compile; `noEmitOnError` prevents
  partial output from a failing compiler.
- `python -m unittest discover -s .bits/checks -p 'test_*.py' -v`: governance and
  workflow policy checks. Requires Python 3.11+ and PyYAML 6.0.3.

Node executes TypeScript source for local development/tests using its native
type stripping. This does not typecheck source; `npm run typecheck` remains a
separate mandatory gate. `npm run dev` starts the real SDK and must only be run
with an explicitly authorized staging configuration; it was not run here.

The local lint check uses links to preinstalled sandbox ESLint/TypeScript tools
at the declared versions because npm installation is blocked. Those links are
ignored and are not distributed. Typecheck/build failures still expose the
missing actual dependency/type packages.

## CI and signed output

CI, release and provenance jobs run installation, lint, typecheck, tests and build.
Security scanning retains CodeQL and TruffleHog/private-import checks. GHCR login
uses GitHub expressions; this fix was already merged and is regression-tested.
No publishing workflow is invoked by local validation.

The provenance workflow requires nonempty `dist/index.js` and archives only
`package.json`, `package-lock.json` and compiled `dist/`. It attests the digest of
that exact archive, then verifies the signed bundle before uploading it. Missing
build prerequisites or compiler errors prevent the archive/signing job. PRs have
no signing permissions; signing remains limited to successful trusted main runs.

Follow [PROVENANCE.md](PROVENANCE.md) to verify an actual signed artifact after a
successful GitHub build. No real compiled artifact or live attestation was produced
locally. Administrator protection/permission activation remains separate.

## Rollback

Use a reviewed revert on the build-repair PR. Preserve the original governance
and ownership changes and the merged scaffold-expression fixes. Do not disable
checks or publish previous/stale output to work around dependency failures.
