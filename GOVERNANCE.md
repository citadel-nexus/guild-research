<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        GOVERNANCE.md
# Stage:       06_PLAN
# SRS:         SRS-CN-RESEARCH-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-research
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .github/BRANCH_PROTECTION.md, .github/PROVENANCE.md
# EnumType:    Doc
# EnumEdges:   DEPENDS_ON .github/BRANCH_PROTECTION.md; DEPENDS_ON .github/PROVENANCE.md
# DAG Node:    none
# Intent:      Define Research stewardship, review authority and cross-guild escalation.
# ───────────────────────────────────────────────────────────────
-->

# Research Guild governance

Owner: **Citadel Nexus Inc.** Guildmaster: **Scholar** (GitLab user `scholar`).
Datadog team handle: **`guild-research`**.

## Charter

The Research Guild owns the **knowledge and world graph**, the **research corpus**,
and the **research flywheel**: sourcing, assessing, synthesizing and refining
knowledge through evidence and feedback. It maintains public Research contracts,
provenance, quality criteria and documentation. Public artifacts must not expose
private corpus contents, credentials or tenant data.

## Decisions and approval

Contributors propose changes through an SRS-linked PR with motivation, evidence,
test results and rollback. Scholar is accountable for scope, priorities and
acceptance, and approves changes or explicitly delegates review to a Research
lead. At least one non-author code-owner approval and all required checks are
needed before merging. Authors do not approve their own changes. New commits
invalidate prior approvals; all review conversations must be resolved.

Changes to this charter, ownership, workflows, provenance policy or branch
protections require Scholar's explicit approval and a recorded guildmasters-group
review. GitHub's one-owner review rule alone does not enforce the additional
human review; reviewers must record it in the PR before merge. Do not weaken
checks or use an administrator bypass to handle a failing build.

Consult SDK maintainers on public SDK interface changes without replacing guild
approval. Cross-guild contracts and contested decisions go to the guildmasters
group before acceptance. Record the decision and rationale in the PR.

## Escalation

Raise unresolved ownership, evidence-quality, cross-guild or policy disputes in
the PR and request Scholar's decision. If Scholar is unavailable, conflicted, or
the dispute remains unresolved, escalate to the **guildmasters group** via the
organization's established review channel. Record the group's decision and the
responsible reviewer in the PR. Hold the merge until that decision is recorded;
there is no implied emergency bypass. No unverified GitHub group handle is used.

## GitHub ownership mapping

GitLab `scholar` and Datadog `guild-research` are not verified GitHub identities.
CODEOWNERS names Scholar and uses the repository's existing
`@citadel-nexus/guild-research-leads` team as the enforceable owner. An administrator
must confirm that this team exists, is visible, has explicit write access, and
includes Scholar's verified GitHub account. Until confirmed, automated review
routing cannot be claimed as active. If direct individual ownership is required,
replace the owner with the verified account in a reviewed follow-up change.

See [branch protection](.github/BRANCH_PROTECTION.md) for admin activation and
[signed provenance](.github/PROVENANCE.md) for consumer verification.

## Accountability and rollback

Scholar owns governance and provenance policy. Repository administrators enable
GitHub enforcement; merging files alone does not enable protection. Research
maintainers own build reproducibility and investigate verification failures.
Rollback uses a reviewed revert with the same approvals and checks. Suspect
artifacts must not be consumed; rebuild from a reviewed commit after remediation.
No production or deployment authority is granted by this charter.
