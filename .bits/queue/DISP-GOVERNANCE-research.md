<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/queue/DISP-GOVERNANCE-research.md
# Stage:       11_COMMIT
# SRS:         SRS-CN-RESEARCH-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-research
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .bits/srs/SRS-CN-RESEARCH-GOVERNANCE-001.md
# EnumType:    ConfigDoc
# EnumEdges:   DEPENDS_ON .bits/srs/SRS-CN-RESEARCH-GOVERNANCE-001.md
# DAG Node:    none
# Intent:      Record the operator directive and bounded staging tasks as a local dispatch.
# ───────────────────────────────────────────────────────────────
-->

# DISP-GOVERNANCE-research

- srs: SRS-CN-RESEARCH-GOVERNANCE-001
- guild: research
- champion: Scholar
- seat: BITS-CODEGEN
- mode: staging
- branch: bits/SRS-CN-RESEARCH-GOVERNANCE-001-provenance
- status: in_progress
- brief: .bits/srs/SRS-CN-RESEARCH-GOVERNANCE-001.md
- authorization_source: authenticated operator directive in this Bits coding session
- operator: Dmitry Richard, mr.nobody@citadel-nexus.com
- authorization_date: 2026-10-20

## Authorization

> Directive: "create those". This authorizes creating the missing governance
> records for this work, including the missing AGENTS.md.
>
> Create AGENTS.md, plus any other missing prerequisites (CLAUDE.md,
> .bits/context.md, registry, queue), following the conventions of the sibling
> guild repos. Then create a local SRS registry entry and SRS document
> SRS-CN-RESEARCH-GOVERNANCE-001 ("Research Guild ownership governance and signed
> build provenance"), and a dispatch DISP-GOVERNANCE-research with status
> in_progress. Record this directive as the dispatch's authorization source.
>
> SRS scope: CODEOWNERS, GOVERNANCE.md, branch-protection/ruleset documentation
> or config, and a CI workflow for SLSA provenance attestations, artifact signing
> and verification docs, all as described in my first message.
>
> Bounds: one branch and PR for this SRS only. No production, deploy, push to main,
> changes to GitHub settings, or secrets.

This creates a local authorization record only; it does not assert external VCC
registration, blueprint approval, or production authorization.

## Task table

| Phase | Task | Gate |
|---|---|---|
| A | Bootstrap local governance prerequisites and register this SRS | Required records present; existing SRS preserved |
| B | Guild ownership, charter and administrator protection guide | Owner and policy checks pass |
| C | Build/sign/verify workflow, smoke checks, memory and report | Governance smoke checks pass |

## Smoke test

Prerequisite: Python 3.11+ and PyYAML 6.0.3 (CI installs the pinned parser).

```bash
python -m unittest discover -s .bits/checks -p 'test_*.py' -v
```

A successful exit is PASS. Failure is FAIL; stop the phase and report the failing
assertion. Before all checks exist, the phase A/B gate uses the corresponding
`BootstrapTests` / `OwnershipTests` test class. Run existing `npm run lint`,
`npm test`, `npm run build` as baseline diagnostics and report known scaffold
failures separately; these do not waive the provenance build gate.

## Memory Brief

The source conversation requested governance/provenance sessions for guildmasters.
This task identifies Scholar, Research's graph/corpus/flywheel scope and Datadog
team `guild-research`. Existing Research ownership uses the GitHub team
`citadel-nexus/guild-research-leads`; its membership has not been verified. The
unrelated Living World dispatch remains queued. No external memory recall or
VCC lookup was performed. No injected issue Memory Brief was supplied.
