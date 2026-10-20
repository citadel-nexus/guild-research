<!--
# File: CLAUDE.md
# Stage: 04_HYPOTHESIZE
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: AGENTS.md
# EnumType: Doc
# EnumEdges: DEPENDS_ON AGENTS.md
# DAG Node: none
# Intent: Direct IDE seats to the active build-repair dispatch and its dependency limitations.
-->

# Research Guild seat context

The guild owns the knowledge and world graph, research corpus, and research
flywheel. Scholar (GitLab `scholar`) is guildmaster; `guild-research` is the
Datadog team handle. Legal owner: Citadel Nexus Inc.

Read `AGENTS.md` and `.bits/context.md` before work. The active follow-up is
`SRS-CN-RESEARCH-BUILD-001` / `DISP-BUILD-research`; governance PR #17 is merged. Only local staging
records are authorized; external VCC state has not been checked or changed.

The repo already contains a TypeScript scaffold and GitHub CI/release workflows.
The operator authorized staging application build repairs, tests and CI
configuration. Production, deployment and private-stack repairs remain excluded.
The referenced `guild-sdk` sibling could not be inspected because the sandbox
refused to combine public and private repositories. These records follow this
repository's observable conventions; sibling alignment remains unverified.

See `GOVERNANCE.md` for decision rules, `.github/BRANCH_PROTECTION.md` for admin
activation, and `.github/PROVENANCE.md` for artifact verification.
