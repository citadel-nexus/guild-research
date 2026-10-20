<!--
# ─── CGRF Header ───────────────────────────────────────────────
# File:        .github/BRANCH_PROTECTION.md
# Stage:       06_PLAN
# SRS:         SRS-CN-RESEARCH-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-research
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .github/CODEOWNERS, .github/workflows/build-provenance.yml
# EnumType:    Doc
# EnumEdges:   DEPENDS_ON .github/CODEOWNERS; DEPENDS_ON .github/workflows/build-provenance.yml
# DAG Node:    none
# Intent:      Specify administrator-owned enforcement without pretending repository files apply settings.
# ───────────────────────────────────────────────────────────────
-->

# Default-branch protection requirements

Default branch: `main` (confirmed from GitHub repository metadata on 2026-10-20).
This repository has no settings-app or ruleset reconciler. This is an administrator
configuration specification, **not an applied rule**. Recheck the default branch
before activation; update workflow filters and verification policy if it changes.

## Required configuration

Create an **active branch ruleset** targeting the default branch (`~DEFAULT_BRANCH`)
in GitHub Settings → Rules → Rulesets, or equivalent branch protection:

| Requirement | Value |
|---|---|
| Pull request before merge | Required; at least 1 approving review |
| Code-owner review | Required |
| Stale approvals | Dismiss after new commits |
| Most recent reviewable push | Require approval by someone other than its author |
| Review conversations | Require resolution |
| Signed commits | Required; commits must show GitHub Verified signatures |
| Status checks | Required, including branches up to date before merge |
| Required check contexts | `build`, `Governance checks`, `Build artifact` |
| Expected status-check source | GitHub Actions; verify the actual contexts after first runs |
| Expected guildmaster automation actor | `scholar-research-guildmaster` GitHub App (operator-confirmed) |
| Force pushes and branch deletion | Block |
| Bypass list | Empty; apply to administrators as well |

`build` is the existing CI build job. `Governance checks` and `Build artifact`
are PR jobs in `Build provenance`. Do **not** require `Attest artifact`: it runs
only after changes reach trusted `main`, and is deliberately skipped on PRs.
Do not require `docker` or scheduled-only scan jobs on PRs. The existing default
branch CI and release workflows are unchanged by this work.

## Administrator activation order

1. Ensure the confirmed owner team `@citadel-nexus/guild-research` is visible and
   has explicit repository write access; review CODEOWNERS validation in GitHub.
   The operator has confirmed the team and `scholar-research-guildmaster` App
   through the Datadog team links; no further Scholar identity confirmation is
   required. The App is the expected guildmaster automation actor, not a code
   owner or the source of the GitHub Actions checks listed above. Do not add it
   to the bypass list. Record the guildmasters approval required by the charter.
2. Have an application-scaffold dispatch supply the missing lockfile, dev tools
   and TypeScript/ESLint configuration. Existing CI already runs `npm ci`; the
   new build also refuses to proceed without a lockfile. Do not mark missing
   builds successful or disable their checks to bootstrap governance.
3. Enable GitHub Actions and permit the actions used by the new workflow. Allow
   job-scoped `id-token: write` and `attestations: write` on trusted main runs.
   Keep the repository's default token read-only. Confirm artifact attestations
   are available for this repository/plan (this repository is public).
4. Run a PR and inspect the exact check contexts and app identity. Obtain passing
   checks before selecting them as required. The normal repair PR review process
   must remain in effect until the new rule can be activated.
5. Enable the ruleset above. Confirm contributors and automation use commits that
   GitHub recognizes as signed. Local signing alone is not evidence of GitHub's
   Verified status. Check the chosen merge method also produces acceptable signed
   commits. No signing key or token is created by this change.
6. After merge and a successful trusted build, verify the signed archive using
   PROVENANCE.md. Confirm a PR cannot run the signing job. Test that an unsigned
   commit or PR without owner approval cannot update `main` through GitHub's
   normal UI/validation, without changing production or bypassing the rule.

This session does not change GitHub settings, team memberships or permissions.
A successful archive attestation covers only that archive; it does not retrofit
signing onto existing npm publishing or container builds.

## Limits and recovery

GitHub accepts any listed code owner; keep one Research owner rule to prevent a
narrow SDK rule from removing guild review. Extra Scholar/guildmasters approvals
are human requirements until an administrator configures an additional enforceable
review policy. Required check names should remain stable and not be duplicated.

If settings or workflow changes prevent merging, escalate to Scholar and the
guildmasters group. Resolve the underlying check/identity problem through a
reviewed change. Do not silently relax the protected-branch requirements.
