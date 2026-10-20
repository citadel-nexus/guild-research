<!--
# File: .bits/out/DISP-BUILD-research/report.md
# Stage: 11_COMMIT
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: .bits/checks/test_build.py, .github/BUILD.md, .bits/out/DISP-BUILD-research/memory.json
# EnumType: Doc
# EnumEdges: DEPENDS_ON .bits/checks/test_build.py; DEPENDS_ON .github/BUILD.md; DEPENDS_ON .bits/out/DISP-BUILD-research/memory.json
# DAG Node: none
# Intent: Report completed staging repairs and unresolved clean-install/compiler blockers without claiming success.
-->

# Build-repair staging report

## §1 SUMMARY

Status: PARTIAL — configuration/tests are implemented; real dependency resolution
and clean installation still block full typecheck, compilation and attestation.
Dispatch: DISP-BUILD-research
Seat: BITS-CODEGEN; mode: staging
SRS: SRS-CN-RESEARCH-BUILD-001
Branch: bits/SRS-CN-RESEARCH-BUILD-001-toolchain
Base: 4a5c3f22bb15db0f2d156c7f74227c25c3b5a33e (main after governance/scaffold fixes)
Tasks: 6/10 complete, 2 partial, 2 blocked
Tests: 21/21 pass (5 Node application/cleanup tests, 16 Python policy checks)
Required command gates: 3/6 pass; npm ci, typecheck and build remain blocked.
CKS Gate: B+/75; CKS: pending; CAPS: pending; CK: pending
Commits: resolve with `git log --oneline 4a5c3f22bb15db0f2d156c7f74227c25c3b5a33e..HEAD`.

## §2 TASK RESULTS

| Step | Status | Result | Verify |
|---|---|---|---|
| 1 Register dispatch | PASS | Explicit operator directive and in_progress registry | Python BuildRepairTests |
| 2 Current base | PASS | Separate branch starts from latest main; GHCR fix retained | git merge-base HEAD origin/main |
| 3 SDK source | BLOCKED | Required SDK absent from npm cache; legitimate registry unanswered | npm install --package-lock-only --ignore-scripts --offline --no-audit --no-fund |
| 4 Lockfile/install | BLOCKED | No trustworthy full dependency graph; no fabricated lockfile | npm ci --offline --no-audit --no-fund |
| 5 TypeScript | PARTIAL | Strict NodeNext config, noEmitOnError and noEmit gate added; actual dependency types missing | npm run typecheck |
| 6 ESLint | PASS, qualified | Recommended rules pass using installed sandbox tools at declared versions | npm run lint |
| 7 Tests/Node | PASS | Node 24.13.0/npm 11.6.2 pin; 5 actual behavior tests | npm test |
| 8 CI | PASS locally | Runtime/gates aligned; CodeQL and secret scans retained | Python BuildRepairTests |
| 9 Build/provenance | PARTIAL | Archive includes compiled output and lockfile; build cannot complete | npm run build; Python ProvenanceTests |
| 10 Documentation | PASS | Build recovery guide, report and memory evidence recorded | JSON memory validation and metadata audit |

Python checks: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s .bits/checks -p 'test_*.py' -v`.
Per-file scope and CKET stage assignments are recorded in the Type A memory vectors.
No existing failing test was removed or skipped. No runtime service code changed.

## §3 SMOKE TEST RESULTS

| Command | Expected | Actual | Result |
|---|---|---|---|
| npm install --package-lock-only --ignore-scripts --offline --no-audit --no-fund | Resolve real dependency graph | ENOTCACHED for @citadel-guilds/sdk | BLOCKED |
| npm ci --offline --no-audit --no-fund | Clean install | EUSAGE: lockfile absent | BLOCKED |
| npm run lint | Zero lint errors | Zero errors with preinstalled linked ESLint/TS tools | PASS, qualified |
| npm run typecheck | tsc --noEmit succeeds | TS2688: @types/node unavailable | BLOCKED |
| npm test | Nonempty suite passes with coverage gates | 5/5 pass; no skips; health.ts 100% lines/branches/functions | PASS |
| npm run build | Fresh compiled dist output | Missing Node types, NATS and SDK; no dist emitted | BLOCKED |
| Python unittest discovery | All policy checks pass | 16/16 pass | PASS |
| bash -n on workflow run steps | Valid shell syntax | 23/23 valid | PASS |
| test ! -e dist | Failed build leaves no output | No dist exists | PASS |

The initial lint failure was an unqualified URL global in the new build test.
Applied fix: import URL explicitly from node:url. `npm run lint` now passes.

Dependency failures are unresolved: required packages are not cached, and this
sandbox cannot perform internet package installation. Offline generation never
produced a lockfile. An operator question requests the authentic SDK package source.
No SDK/NATS replacement, optional dependency or ambient module shim was introduced.
Run the documented dependency-enabled recovery in .github/BUILD.md, then repeat
all gates; dependency correctness and real SDK API compatibility are unverified.

The sandbox's actual ESLint 9.16.0, parser/plugin 8.18.0 and TypeScript 5.7.3 were
linked into ignored node_modules for partial validation. This is not npm ci evidence.
Tests run on actual Node v24.13.0/npm 11.6.2. Health coverage does not measure
unloaded SDK/NATS modules; no whole-application coverage claim is made.

Strict mypy checking of both Python policy-test modules is also blocked by
missing types-PyYAML stubs (two import-untyped diagnostics); no ignore rule was
added. Actionlint is unavailable; workflow YAML, policy and shell checks passed.

Archive tests use explicit fixtures, not a claimed application artifact. Live
GitHub Actions, Docker builds, package publication and Sigstore verification were
not run. TypeScript noEmitOnError remains enabled; a failed build emits no artifact.

## §4 MEMORY INGEST

Type A count: 31; Type B count: 62; Type C count: 4.
IOO compliance: true; DKG orphans: 0
Payload: .bits/out/DISP-BUILD-research/memory.json
Verify: `python -m json.tool .bits/out/DISP-BUILD-research/memory.json > /dev/null`.
No external memory API write is performed. Actual event timestamps are recorded;
CK/CAPS/CKS remain pending. No dispatch-completed event is claimed.

## §5 CKET FILING

04_HYPOTHESIZE: agent/seat context and build SRS.
06_PLAN: README, build/verification/protection guides.
08_TEST: Node health and build cleanup tests.
11_COMMIT: build configuration, workflows, Docker, operational tests and records.
These are logical stages preserving conventional repo paths under AGENTS.md.
New files have CGRF metadata; JSON and .nvmrc use sidecars to retain valid syntax.
REFLEX: deferred to authorized private-side processing, not executed here.

## §6 GOVERNANCE

Entity: Citadel Nexus Inc. (Delaware C-Corporation).
License: unchanged; no relicensing is part of this SRS.
Hard-NO changed-path scan: no prohibited paths modified.
Secrets: no prohibited secret prefixes in changed files; no credentials changed.
Stripe: not applicable; no payment code changes.
Security: CodeQL and TruffleHog/private-import checks preserved.
Owner team: @citadel-nexus/guild-research.
Scholar automation identity: scholar-research-guildmaster GitHub App.
No production, deployment, direct push or GitHub settings changes performed.

## §7 NEXT ACTIONS

Blockers: authentic SDK registry/package access and uncached dependencies. Resolve
these in an authorized environment, generate/review the real lockfile and its
CGRF sidecar, then rerun install/lint/typecheck/test/build before claiming completion.
A green GitHub build is required before live positive/tamper attestation checks.
Administrator branch/Actions activation remains separate from this staging PR.
Handoff: operator/package maintainer to provide the public SDK source; no private
stack edits or additional repository attachment attempted.
Suggested next dispatch: finish this in_progress build dispatch after access is available.
Bugs filed: none; provider tools are read-only.
Requested labels: bits:codegen, srs:srs-cn-research-build-001,
dispatch:disp-build-research, verified:manual-review (not applied here).
