<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/srs/SRS-CN-RESEARCH-GOVERNANCE-001.md
# Stage:       04_HYPOTHESIZE
# SRS:         SRS-CN-RESEARCH-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-research
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     GOVERNANCE.md, .github/workflows/build-provenance.yml
# EnumType:    Doc
# EnumEdges:   DEPENDS_ON GOVERNANCE.md; DEPENDS_ON .github/workflows/build-provenance.yml
# DAG Node:    none
# Intent:      Specify reviewable ownership and digest-bound provenance for Research artifacts.
# ───────────────────────────────────────────────────────────────
-->

# Research Guild ownership governance and signed build provenance

- SRS: SRS-CN-RESEARCH-GOVERNANCE-001
- Dispatch: DISP-GOVERNANCE-research
- Status: in_progress; mode: staging
- Guildmaster: Scholar (GitLab `scholar`); Datadog team: `guild-research`
- CKS gate: B+/75; CAPS minimum: B+; CKS/CAPS/CK: pending

## Intent and scope

Make Research ownership, decisions and escalation explicit, and allow consumers
to verify the origin and integrity of compiled build artifacts. The guild owns
the knowledge and world graph, research corpus and research flywheel.

Bootstrap the missing agent/seat context and local dispatch records. Configure
CODEOWNERS, a guild charter, and documented default-branch requirements. There
is no existing repository-settings reconciler, so settings are documented for
an administrator instead of adding an inert policy file.

## Acceptance

1. CODEOWNERS names Scholar and routes every path to the operator-confirmed
   `@citadel-nexus/guild-research` team; no path silently overrides guild review.
   Record `scholar-research-guildmaster` as Scholar's automation App, not a code owner.
2. Governance defines decisions, approval and escalation to the guildmasters group.
3. Admin instructions cover required owner reviews, signed commits, named required
   status checks, bypass restrictions and activation order on default branch `main`.
4. PRs build with read-only permissions. Only same-repository `main` runs can sign.
   The signer is isolated from execution of repository build scripts.
5. A successful npm build is archived and receives a signed SLSA provenance v1
   attestation via GitHub's keyless Sigstore integration. Upload the exact archive
   and bundle; do not deploy or publish a package/container.
6. Verification binds artifact digest, repository, workflow, source ref and source
   commit, and rejects tampering. Do not claim a certified SLSA level.
7. Smoke checks, report and three-type memory payload reflect actual evidence.

## Limits and rollout

Application repair is outside this SRS. A missing lockfile/toolchain is a hard
build failure, not a reason to substitute source archives or empty artifacts.
No live signing is possible in the local sandbox. Activate protections only after
checking owner-team access and obtaining successful checks on GitHub. No settings
are changed here. Existing npm/container publication remains unattested by this
new archive workflow and requires separate scope if needed.
