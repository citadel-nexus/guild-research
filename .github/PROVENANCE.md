<!--
# File: .github/PROVENANCE.md
# Stage: 06_PLAN
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: .github/workflows/build-provenance.yml, .github/BUILD.md
# EnumType: Doc
# EnumEdges: DEPENDS_ON .github/workflows/build-provenance.yml; DEPENDS_ON .github/BUILD.md
# DAG Node: none
# Intent: Verify signed archives that include compiled output and its dependency lockfile.
-->

# Signed Research build provenance

`Build provenance` builds with `npm ci`, lint, typechecking, tests and TypeScript compilation.
It archives `dist/`, `package.json` and `package-lock.json` as `research-build-<full-commit-sha>.tar.gz`.
The archive is compiled output, not a deployable image or dependency bundle;
consumers must supply runtime dependencies separately. Missing build inputs or
an empty/missing `dist/index.js` fail the build. No source-only fallback is used.

PRs receive a read-only build check and an unsigned, short-lived CI artifact.
Only successful same-repository runs on `refs/heads/main` (push or manual) reach
the separate `Attest artifact` job. That job downloads the current run's archive
without checking out or executing repository code. Only it receives OIDC and
attestation write permissions. It does not publish to npm, a registry or a release.

`actions/attest-build-provenance` produces a SLSA provenance v1 statement and
Sigstore keyless signature using GitHub Actions OIDC identity. The signed statement
binds the archive's SHA-256 digest to its source and build identity. This is artifact
signing via a signed attestation, not a separate raw-file signature or a managed
long-lived key. Public repository attestations use Sigstore's public transparency
infrastructure; do not place sensitive data in public artifacts or metadata.
No certified SLSA level is claimed by this workflow alone.

The job verifies the result before uploading `signed-research-build-<sha>`, which
contains the exact archive and `provenance.sigstore.json`. Download and retain
both: Actions artifacts expire after 30 days (unsigned build intermediates: 14).
See [BUILD.md](BUILD.md) for the dependency-locking blocker and repair evidence.
No live attestation exists until the scaffold prerequisites are repaired and a
trusted main run completes. Existing npm and container outputs are not covered.

## Verify before extracting or consuming

Use a current GitHub CLI with `gh attestation verify` and the policy flags below.
Select a successful run of `.github/workflows/build-provenance.yml` on `main` and
independently obtain the expected full commit SHA from the reviewed merge. Do
not trust an artifact filename as evidence of the approved source commit.

```bash
# Replace these with the trusted workflow run ID and reviewed full commit SHA.
RUN_ID='<trusted-successful-main-run-id>'
EXPECTED_SHA='<reviewed-full-commit-sha>'
REPO='citadel-nexus/guild-research'

gh run view "$RUN_ID" --repo "$REPO" \
  --json conclusion,event,headBranch,headSha,workflowName
# Confirm success, push/workflow_dispatch, main, expected SHA and Build provenance.
gh run download "$RUN_ID" --repo "$REPO" \
  --name "signed-research-build-$EXPECTED_SHA" --dir verified-build

gh attestation verify "verified-build/research-build-$EXPECTED_SHA.tar.gz" \
  --bundle verified-build/provenance.sigstore.json \
  --repo "$REPO" \
  --signer-workflow citadel-nexus/guild-research/.github/workflows/build-provenance.yml \
  --source-ref refs/heads/main \
  --source-digest "$EXPECTED_SHA" \
  --predicate-type https://slsa.dev/provenance/v1 \
  --deny-self-hosted-runners
```

A zero exit status is required. Verification checks the artifact digest, signature,
certificate identity and trust chain as well as the repository, workflow, source
ref and source commit policy. Bundle verification may still fetch trust material;
it is not a promise of offline operation. Omit `--bundle` to fetch matching
attestations from GitHub instead. Merely finding an attestation, printing a
checksum or successfully downloading an archive is not verification.

## Negative verification check

After a successful verification, change a copy of the archive and verify that it
fails with the same trusted bundle and policy. Never modify the retained original.

```bash
cp "verified-build/research-build-$EXPECTED_SHA.tar.gz" verified-build/tampered.tar.gz
printf '\nintentional-tamper\n' >> verified-build/tampered.tar.gz
if gh attestation verify verified-build/tampered.tar.gz \
  --bundle verified-build/provenance.sigstore.json \
  --repo "$REPO" \
  --signer-workflow citadel-nexus/guild-research/.github/workflows/build-provenance.yml \
  --source-ref refs/heads/main \
  --source-digest "$EXPECTED_SHA" \
  --predicate-type https://slsa.dev/provenance/v1 \
  --deny-self-hosted-runners; then
  echo 'FAIL: modified artifact accepted'
  exit 1
else
  echo 'PASS: modified artifact rejected (inspect output for digest mismatch)'
fi
```

Run the positive check first: authentication, network, or trust-root failures are
not evidence that digest enforcement works. Also reject a mismatched expected
source SHA, another workflow identity, a missing bundle or an unsigned PR artifact.

If verification fails, stop consumption and escalate to Scholar. Retain the run
ID and error; rebuild from a reviewed commit after fixing the cause. Do not use
identity-relaxing flags or silently trust a different ref. See
[branch protection](BRANCH_PROTECTION.md) for administrator prerequisites.
