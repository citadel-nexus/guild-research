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

The operator confirmed these identities through the Datadog `guild-research`
team links under the existing SRS and dispatch:

- Guildmaster code owner: [@citadel-nexus/guild-research](https://github.com/orgs/citadel-nexus/teams/guild-research).
- Scholar's automation identity: the [scholar-research-guildmaster GitHub App](https://github.com/apps/scholar-research-guildmaster).

CODEOWNERS assigns every path to the confirmed team. GitHub Apps cannot be code
owners; Scholar's App performs automation and does not replace team code-owner
approval. Identity confirmation is complete. Administrators must still ensure
the team is visible, has explicit repository write access, and that protection
rules are active. The App receives no branch-protection bypass from this policy.

See [branch protection](.github/BRANCH_PROTECTION.md) for admin activation and
[signed provenance](.github/PROVENANCE.md) for consumer verification.

## Accountability and rollback

Scholar owns governance and provenance policy. Repository administrators enable
GitHub enforcement; merging files alone does not enable protection. Research
maintainers own build reproducibility and investigate verification failures.
Rollback uses a reviewed revert with the same approvals and checks. Suspect
artifacts must not be consumed; rebuild from a reviewed commit after remediation.
No production or deployment authority is granted by this charter.
