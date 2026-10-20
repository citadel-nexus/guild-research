<!--
# File: .bits/srs/SRS-CN-RESEARCH-BUILD-001.md
# Stage: 04_HYPOTHESIZE
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: package.json, .github/workflows/build-provenance.yml
# EnumType: Doc
# EnumEdges: DEPENDS_ON package.json; DEPENDS_ON .github/workflows/build-provenance.yml
# DAG Node: none
# Intent: Restore reproducible Research build gates before provenance can be produced.
-->

# Research Guild reproducible build repair

SRS: SRS-CN-RESEARCH-BUILD-001
Dispatch: DISP-BUILD-research
Status: in_progress
Seat: BITS-CODEGEN; mode: staging
Guildmaster: Scholar; owner: @citadel-nexus/guild-research
CKS gate: B+/75; CAPS minimum: B+; CKS/CAPS/CK: pending

## Intent

Repair the existing TypeScript scaffold so reproducible installation, static
checks, real tests and compilation can precede digest-bound build attestation.
The operator explicitly authorizes this follow-up to governance PR #17, on a
new branch and a separate PR. Preserve the merged scaffold-expression fixes.

## Scope and acceptance

1. Record the operator directive and this registered dispatch.
2. Start from current main; preserve merged governance and other contributors' work.
3. Identify the existing SDK's legitimate package source; never replace it with
   a stub, guessed implementation, optional dependency or permissive type shim.
4. Generate a genuine npm lockfile from dependency metadata and verify npm ci.
5. Configure strict TypeScript checking, including tsc --noEmit.
6. Configure ESLint for the existing TypeScript source.
7. Run meaningful tests with a pinned supported Node runtime. No tests may be
   deleted, weakened or skipped merely to pass. No production connections in tests.
8. Align CI, provenance, release and Docker toolchains; preserve CodeQL and
   secret scanning. Retain correct GitHub expression syntax for registry login.
9. Archive and attest actual compiled output after successful checks; retain the
   main-only signer, strict verification and no-artifact-on-build-failure policy.
10. Document setup, evidence, blockers, rollback and the three-type memory payload.

Required final evidence: npm ci, npm run lint, npm run typecheck, npm test,
npm run build, plus governance/workflow checks. Dependency/network/tool failures
must be reported as blockers, never turned into success or bypassed with shims.

## Bounds

No production, deployment, direct push, GitHub settings changes, secrets changes,
private-stack modifications, registry publication or live NATS connections.
Workflow definitions may be repaired; do not invoke their publishing jobs here.
Existing runtime behavior is preserved. Existing package dependencies remain
required. The queued Living World dispatch is not activated by this work.
