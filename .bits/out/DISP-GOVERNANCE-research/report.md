<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/out/DISP-GOVERNANCE-research/report.md
# Stage:       11_COMMIT
# SRS:         SRS-CN-RESEARCH-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-research
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/checks/test_governance.py, .bits/out/DISP-GOVERNANCE-research/memory.json
# EnumType:    Doc
# EnumEdges:   DEPENDS_ON .bits/checks/test_governance.py; DEPENDS_ON .bits/out/DISP-GOVERNANCE-research/memory.json
# DAG Node:    none
# Intent:      Record implementation evidence and separate pending GitHub activation from local completion.
# ───────────────────────────────────────────────────────────────
-->

# Governance bootstrap report

## §1 SUMMARY

Status: PARTIAL (implementation complete; application build and GitHub activation pending)
Dispatch: DISP-GOVERNANCE-research
Seat: BITS-CODEGEN
SRS: SRS-CN-RESEARCH-GOVERNANCE-001
Branch: bits/SRS-CN-RESEARCH-GOVERNANCE-001-provenance
Tasks: 3/3 implementation tasks
Smoke: 10/10 governance checks
CKS Gate: B+/75; CKS: pending; CAPS: pending; CK: pending
Commits: resolve with `git log --format='%h %s' c42f10f967314ff97715c8efced4c4d7da434674..HEAD`;
the PR report records the final SHA without embedding a self-referential commit hash here.

## §2 TASK RESULTS

### Task A — Bootstrap prerequisites

Status: PASS
Output: Local operator-authorized dispatch and registered SRS, preserving prior work.
Verify: `python .bits/checks/test_governance.py BootstrapTests -v`
Files: AGENTS.md, CLAUDE.md, .bits/context.md, .bits/srs_registry.yml,
.bits/srs/SRS-CN-RESEARCH-GOVERNANCE-001.md, .bits/queue/DISP-GOVERNANCE-research.md
CKET: 04_HYPOTHESIZE, 11_COMMIT (logical mapping in AGENTS.md)

### Task B — Ownership and approval policy

Status: PASS (identities operator-confirmed; admin enforcement pending)
Output: Scholar named as guildmaster, all paths assigned to the confirmed owner
team `@citadel-nexus/guild-research`, with `scholar-research-guildmaster` recorded
as Scholar's automation App and expected actor. Identity confirmation is complete;
charter and administrator-owned default-branch requirements remain in effect.
Verify: `python .bits/checks/test_governance.py OwnershipTests -v`
Files: GOVERNANCE.md, .github/CODEOWNERS, .github/BRANCH_PROTECTION.md
CKET: 06_PLAN

### Task C — Build provenance and verification

Status: PASS (local checks only; no live signed artifact)
Output: PR builds have read-only privileges. Only successful main builds reach an
isolated job that creates and verifies a signed SLSA provenance v1 attestation.
Verify: `python .bits/checks/test_governance.py ProvenanceTests -v`
Files: .github/workflows/build-provenance.yml, .github/PROVENANCE.md,
.bits/checks/test_governance.py and this dispatch's report/memory records
CKET: 11_COMMIT, 06_PLAN

## §3 SMOKE TEST RESULTS

Run `python -m unittest discover -s .bits/checks -p 'test_*.py' -v`.
Expected and actual: all 10 checks pass. No smoke failures. The suite was rerun
after applying the operator-confirmed owner team and automation identity.

| Check | Expected and actual | Result |
|---|---|---|
| Required records | Local authorization and records present | PASS |
| Registry | Existing SRS preserved; new dispatch registered | PASS |
| Owner coverage | Single Research rule covers all paths | PASS |
| Admin policy | Named review/signature/check requirements match PR jobs | PASS |
| Archive command | Missing output rejected; fixture compiled output archived | PASS |
| Build sequence | Install, lint, test and compile required before archive | PASS |
| Permissions | Build jobs read-only; signing isolated | PASS |
| Signing condition | 40 event/ref/repo combinations match trusted-main policy | PASS |
| Artifact continuity | Current-run archive only; attested path matches uploaded file | PASS |
| Verification | Digest, repo, workflow and ref checked before distribution | PASS |

Additional evidence: all 10 shell steps pass `bash -n`. Mutation experiments
rejected PR-level write permissions, a removed main-ref restriction, and an
injected cross-run artifact ID. Archive exercise uses synthetic fixture bytes;
it is not an application build. Live positive/tamper verification commands are
in .github/PROVENANCE.md and have not run against a real attestation.

Baseline diagnostics (outside the phase smoke gate):

| Command | Actual / cause | Applied fix and next verification |
|---|---|---|
| `npm run lint` | FAIL: missing ESLint configuration | None: outside scope; application repair dispatch, rerun command |
| `npm test` | FAIL: Vitest unavailable | None: outside scope; declare/install tooling, rerun command |
| `npm run build` | FAIL: TypeScript compiler unavailable | None: outside scope; repair toolchain/configuration, rerun command |
| `mypy --strict .bits/checks/test_governance.py` | BLOCKED: missing PyYAML type stubs | No network install attempted; install types-PyYAML in a suitable validation environment and rerun |

No pytest/runtime-module coverage claim is made: this SRS adds documentation,
configuration and unittest-based workflow checks, not a runtime module. Python
unittest and PyYAML 6.0.3 were used locally. Actionlint is unavailable; YAML,
workflow policy and shell syntax were checked instead. External action execution,
GitHub review routing, settings enforcement and Sigstore signing remain untested.

## §4 MEMORY INGEST

Type A count: 15
Type B count: 22
Type C count: 4
IOO compliance: true
DKG orphans: 0
Payload: .bits/out/DISP-GOVERNANCE-research/memory.json
Verify: `python -m json.tool .bits/out/DISP-GOVERNANCE-research/memory.json > /dev/null`
No external memory write was performed. No post-merge ingestion workflow is added
or claimed; ingestion must use the authorized dispatch flow.

## §5 CKET FILING

Logical stages preserve GitHub and root-doc discovery paths (AGENTS.md):

- 06_PLAN: GOVERNANCE.md, .github/CODEOWNERS, .github/BRANCH_PROTECTION.md,
  .github/PROVENANCE.md
- 04_HYPOTHESIZE: AGENTS.md, CLAUDE.md,
  .bits/srs/SRS-CN-RESEARCH-GOVERNANCE-001.md
- 11_COMMIT: .bits/context.md, .bits/srs_registry.yml, dispatch, smoke checks,
  report, memory payload/descriptor, .github/workflows/build-provenance.yml
- 13_SAVE: none

CGRF headers: all new files, with a sibling descriptor for JSON.
REFLEX check: deferred to the authorized private-side post-merge process; not run.

## §6 GOVERNANCE

Entity: Citadel Nexus Inc. (Delaware C-Corporation)
License posture: existing license unchanged; no relicensing authorized by this SRS.
Hard-NO scan: no prohibited paths changed.
Secret scan: no prohibited secret prefixes in the changed files.
Stripe mode: not applicable; no checkout or payment code touched.
Grades and CK: pending. External VCC state: not read or changed.
Sibling conventions: guild-sdk attachment was refused by repository isolation;
local repository conventions were used. No cross-repository reads occurred.

## §7 NEXT ACTIONS

Blockers: application scaffold lacks lockfile/config/toolchain; owner-team access
and ruleset/Actions permissions need administrator activation. Identity confirmation
is complete; a trusted GitHub run is required for live attestation verification.
Handoffs requested: administrator steps in .github/BRANCH_PROTECTION.md; no private
seat handoff created because no private-stack work was performed.
Suggested next dispatch: application build-scaffold repair (operator to assign ID).
Bugs filed: none; no issue target was supplied and provider tools are read-only.
PR publication: use the Bits Create or Update PR button after reviewing this change.
Requested labels: bits:codegen, srs:srs-cn-research-governance-001,
dispatch:disp-governance-research, verified:static-only. Labels are not applied here.
