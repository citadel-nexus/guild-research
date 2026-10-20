<!--
# File: .bits/context.md
# Stage: 11_COMMIT
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
# Intent: Record active build-repair scope and confirmed guild ownership.
-->

# Current staging context

- Active SRS: `SRS-CN-RESEARCH-BUILD-001`.
- Dispatch: `DISP-BUILD-research`, status `in_progress`.
- Seat: BITS-CODEGEN. Mode: staging. Date: 2026-10-20.
- Authorization: authenticated operator directive recorded verbatim in the dispatch.
- Confirmed owner: `@citadel-nexus/guild-research`; Scholar automation App:
  `scholar-research-guildmaster` (operator-confirmed through Datadog team links).
- Deliverable: one separate build-repair PR; no external settings changes.
- CKS gate: B+/75; CAPS minimum: B+; CKS, CAPS and CK: pending.

The operator authorized ten staging build-repair steps after governance PR #17.
See the build dispatch for exact scope and commands. Preserve the Living World
queue, code-owner rules, signing trust boundary, CodeQL and secret scanning.

Repair npm dependency locking, TypeScript, ESLint, test tooling and CI. Record
unresolved dependency access as a blocker. No fabricated package metadata,
weakened tests, production connections, publishing or settings changes.
