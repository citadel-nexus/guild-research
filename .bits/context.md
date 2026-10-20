<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/context.md
# Stage:       11_COMMIT
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
# Intent:      Record the active staging scope and known build prerequisites.
# ───────────────────────────────────────────────────────────────
-->

# Current staging context

- Active SRS: `SRS-CN-RESEARCH-GOVERNANCE-001`.
- Dispatch: `DISP-GOVERNANCE-research`, status `in_progress`.
- Seat: BITS-CODEGEN. Mode: staging. Date: 2026-10-20.
- Authorization: authenticated operator directive recorded verbatim in the dispatch.
- Deliverable: one reviewable governance/provenance PR; no external settings changes.
- CKS gate: B+/75; CAPS minimum: B+; CKS, CAPS and CK: pending.

Do create missing prerequisites, record ownership and approval rules, document
branch protection, and add a build/attestation workflow with consumer verification.
Do preserve the existing Living World registry entry and queued dispatch.
Do not change application code, existing CI/release behavior, production, secrets,
or external governance databases. Do not infer GitHub identities from GitLab.

Known prerequisite gaps: no npm lockfile, no TypeScript or ESLint config, no
Vitest/TypeScript development dependencies. These need a separate application
repair dispatch. Do not disable failing build requirements to manufacture evidence.
