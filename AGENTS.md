<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        AGENTS.md
# Stage:       04_HYPOTHESIZE
# SRS:         SRS-CN-RESEARCH-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-research
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/queue/DISP-GOVERNANCE-research.md
# EnumType:    ConfigDoc
# EnumEdges:   DEPENDS_ON .bits/queue/DISP-GOVERNANCE-research.md
# DAG Node:    none
# Intent:      Constrain the authorized Research governance bootstrap to staging.
# ───────────────────────────────────────────────────────────────
-->

# Research Guild agent guidance

This repository is `citadel-nexus/guild-research`, a public Research Guild
scaffold, not `cnwb-mirror`. Owner: Citadel Nexus Inc. Seat: BITS-CODEGEN.

## Authorized staging bootstrap

The authenticated operator Dmitry Richard (mr.nobody@citadel-nexus.com)
authorized creating missing governance prerequisites in this session with the
directive “create those”. The authorization is recorded in
`.bits/queue/DISP-GOVERNANCE-research.md`; its SRS is
`SRS-CN-RESEARCH-GOVERNANCE-001`. This is local staging authorization, not a
claim that a VCC database record was created or verified. No blueprint is
claimed. Future work needs its own ready/in-progress dispatch.

Read this file, `CLAUDE.md`, `.bits/context.md`, `.bits/srs_registry.yml`, the
selected SRS, the dispatch, then its Memory Brief. Preserve unrelated dispatches.

## Repository conventions and boundaries

- Scholar (GitLab `scholar`) is guildmaster. Datadog team: `guild-research`.
- Use existing TypeScript/npm conventions. Do not introduce a backend stack.
- This SRS changes governance, ownership, workflow configuration and verification
  documentation only. Do not modify service code or repair the application scaffold.
- Use one branch and PR for this SRS. Include SRS and dispatch in commit footers.
- No production, deployment, publishing, direct pushes, GitHub settings changes,
  secrets, private-stack access, memory API writes or signing-key generation.
- Preserve existing CI/release workflows and the unrelated Living World SRS.
- CODEOWNERS must use verified GitHub identities; GitLab and Datadog identities
  do not establish GitHub membership. Retain the existing Research leads team
  until an administrator confirms Scholar's GitHub identity and write access.
- New files carry CGRF metadata; grades and CK remain `pending`.
- Preserve GitHub's discoverable `.github/` paths and this repo's root doc layout.
  CKET stages here are logical classifications, not extra directory prefixes:
  root governance/verification docs and CODEOWNERS = `06_PLAN`; AGENTS, CLAUDE
  and SRS specs = `04_HYPOTHESIZE`; `.bits/` operational records, tests and
  `.github/workflows/` = `11_COMMIT`. This repo-specific mapping supersedes the
  mirror-only physical-directory convention for this bootstrap.
- JSON memory records have a sibling `.cgrf.yaml` descriptor. Record every touched
  file and its edges in the dispatch memory payload; no direct memory ingestion.

## Validation and reporting

Run the smoke block in the dispatch after each phase. Report application test,
lint and build failures separately from governance checks; never label an
unbuilt artifact as verified. The existing scaffold lacks its npm lockfile,
TypeScript/ESLint configuration and development tool declarations. An application
repair dispatch is required before build provenance can run successfully.

The PR must use the repository template and explain motivation, changes, test
evidence, limitations and administrator activation steps. No runtime modules are
added by this SRS, so SAKE/module coverage requirements are not applicable.

## Glossary

SRS: scoped specification. Dispatch: authorized task record. CGRF: file metadata.
CKET: lifecycle classification. Scholar: Research guildmaster. Guildmasters group:
cross-guild escalation authority; its GitHub identity is not yet confirmed.
