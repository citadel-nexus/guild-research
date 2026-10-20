<!--
# File: AGENTS.md
# Stage: 04_HYPOTHESIZE
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: .bits/queue/DISP-BUILD-research.md
# EnumType: ConfigDoc
# EnumEdges: DEPENDS_ON .bits/queue/DISP-BUILD-research.md
# DAG Node: none
# Intent: Apply the operator-authorized build-repair scope while retaining staging boundaries.
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

The operator has now authorized `SRS-CN-RESEARCH-BUILD-001` /
`DISP-BUILD-research` for the ten staging build-repair steps. Read its spec and
dispatch for the active scope. Governance-only restrictions below describe the
prior bootstrap and do not prohibit this explicitly authorized build repair.

Read this file, `CLAUDE.md`, `.bits/context.md`, `.bits/srs_registry.yml`, the
selected SRS, the dispatch, then its Memory Brief. Preserve unrelated dispatches.

## Repository conventions and boundaries

- Scholar (GitLab `scholar`) is guildmaster. Datadog team: `guild-research`.
- Use existing TypeScript/npm conventions. Do not introduce a backend stack.
- The governance SRS covered ownership and provenance. The active build SRS
  permits lockfile/toolchain/configuration, tests, CI and build documentation
  repairs. Preserve runtime semantics; do not activate Living World work.
- Use one branch and PR for this SRS. Include SRS and dispatch in commit footers.
- No production, deployment, publishing, direct pushes, GitHub settings changes,
  secrets, private-stack access, memory API writes or signing-key generation.
- Preserve CodeQL, secret scanning and existing publishing boundaries when
  repairing CI/release definitions. Do not execute publishing or deployment jobs.
  Preserve the unrelated Living World SRS.
- CODEOWNERS uses the operator-confirmed team `@citadel-nexus/guild-research`.
  Scholar's automation identity is the `scholar-research-guildmaster` GitHub App.
  Apps cannot be code owners; retain team review and existing protection rules.
- New files carry CGRF metadata; grades and CK remain `pending`.
- Preserve GitHub's discoverable `.github/` paths and this repo's root doc layout.
  CKET stages here are logical classifications, not extra directory prefixes:
  root governance/verification docs and CODEOWNERS = `06_PLAN`; AGENTS, CLAUDE
  and SRS specs = `04_HYPOTHESIZE`; `.bits/` operational records, tests and
  `.github/workflows/` = `11_COMMIT`. This repo-specific mapping supersedes the
  mirror-only physical-directory convention. For build repair, root build configs
  and Docker use `11_COMMIT`, tests use `08_TEST`, and documentation uses
  `06_PLAN`; these are logical classifications preserving conventional paths.
- JSON memory records have a sibling `.cgrf.yaml` descriptor. Record every touched
  file and its edges in the dispatch memory payload; no direct memory ingestion.

## Validation and reporting

Run the smoke block in the dispatch after each phase. Report application test,
lint and build failures separately from governance checks; never label an
unbuilt artifact as verified. The active build dispatch repairs the scaffold prerequisites. If dependencies
cannot be resolved, record the blocker and retain the failed build gate; do not
create fake lockfiles, SDK replacements or ambient module shims.

The PR must use the repository template and explain motivation, changes, test
evidence, limitations and administrator activation steps. No runtime modules are
added by this SRS, so SAKE/module coverage requirements are not applicable.

## Glossary

SRS: scoped specification. Dispatch: authorized task record. CGRF: file metadata.
CKET: lifecycle classification. Scholar: Research guildmaster. Guildmasters group:
cross-guild escalation authority; its GitHub identity is not yet confirmed.
