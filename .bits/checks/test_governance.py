# ─── CGRF Header ───────────────────────────────────────────────
# File:        .bits/checks/test_governance.py
# Stage:       11_COMMIT
# SRS:         SRS-CN-RESEARCH-GOVERNANCE-001
# CAPS:        pending
# CK:          pending
# Dispatch:    DISP-GOVERNANCE-research
# Seat:        BITS-CODEGEN
# Owner:       Citadel Nexus Inc.
# Created:     2026-10-20
# Depends:     .github/workflows/build-provenance.yml, .github/CODEOWNERS, .bits/srs_registry.yml
# EnumType:    Test
# EnumEdges:   DEPENDS_ON .github/workflows/build-provenance.yml; DEPENDS_ON .github/CODEOWNERS; DEPENDS_ON .bits/srs_registry.yml
# DAG Node:    none
# Intent:      Check owner coverage and prevent PR or cross-run artifact signing regressions.
# ───────────────────────────────────────────────────────────────

"""Validate governance prerequisites and the signing workflow's trust boundary."""

from pathlib import Path
import os
import subprocess
import tarfile
import tempfile
from typing import Any, cast
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
SRS = "SRS-CN-RESEARCH-GOVERNANCE-001"
DISPATCH = "DISP-GOVERNANCE-research"


def load_workflow() -> dict[str, Any]:
    """Load workflow keys without YAML 1.1 boolean coercion of `on`."""
    return cast(dict[str, Any], yaml.load(
        (ROOT / ".github/workflows/build-provenance.yml").read_text(),
        Loader=yaml.BaseLoader,
    ))


class BootstrapTests(unittest.TestCase):
    """Check that the local authorization is complete and prior scope survives."""

    def test_required_records(self) -> None:
        """Require all local authorization records and an explicit operator source."""
        for name in ("AGENTS.md", "CLAUDE.md", ".bits/context.md",
                     ".bits/srs_registry.yml", f".bits/srs/{SRS}.md",
                     f".bits/queue/{DISPATCH}.md"):
            self.assertTrue((ROOT / name).is_file(), name)
        dispatch = (ROOT / f".bits/queue/{DISPATCH}.md").read_text()
        self.assertIn("status: in_progress", dispatch)
        self.assertIn("authenticated operator directive", dispatch)
        self.assertIn('"create those"', dispatch)

    def test_registry_preserves_existing_srs(self) -> None:
        """Require the new dispatch while preserving the Living World registration."""
        registry = yaml.safe_load((ROOT / ".bits/srs_registry.yml").read_text())
        self.assertEqual(registry[SRS]["dispatch"], DISPATCH)
        self.assertEqual(registry[SRS]["ck"], "pending")
        self.assertIn("SRS-CN-RESEARCH-LIVINGWORLD-001", registry)


class OwnershipTests(unittest.TestCase):
    """Check ownership coverage and required administrator settings."""

    def test_guild_review_cannot_be_overridden_by_path(self) -> None:
        """Require a single all-path Research owner, including workflows."""
        owners = (ROOT / ".github/CODEOWNERS").read_text()
        rules = [line.split() for line in owners.splitlines()
                 if line.strip() and not line.startswith("#")]
        self.assertEqual(rules, [["*", "@citadel-nexus/guild-research-leads"]])
        self.assertIn("Guildmaster: Scholar", owners)

    def test_admin_requirements_match_pr_jobs(self) -> None:
        """Require documented owner, signature and actual PR check requirements."""
        guide = (ROOT / ".github/BRANCH_PROTECTION.md").read_text()
        for text in ("Code-owner review", "Signed commits", "`build`",
                     "`Governance checks`", "`Build artifact`", "Bypass list"):
            self.assertIn(text, guide)
        jobs = load_workflow()["jobs"]
        self.assertEqual(jobs["governance"]["name"], "Governance checks")
        self.assertEqual(jobs["build"]["name"], "Build artifact")


class ProvenanceTests(unittest.TestCase):
    """Check privileges, artifact continuity and verification constraints."""

    def test_archive_rejects_missing_output_and_packs_compiled_files(self) -> None:
        """Exercise the actual archive command with missing output and a fixture."""
        steps = load_workflow()["jobs"]["build"]["steps"]
        command = next(step["run"] for step in steps if step.get("name") == "Archive compiled output")
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            env = {**os.environ, "ARTIFACT_NAME": "fixture.tar.gz"}
            (folder / "package.json").write_text('{"name":"archive-test-fixture"}')
            missing = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                     cwd=folder, env=env, capture_output=True)
            self.assertNotEqual(missing.returncode, 0)
            self.assertFalse((folder / "artifact/fixture.tar.gz").exists())
            (folder / "dist").mkdir()
            (folder / "dist/index.js").write_text("// synthetic archive test fixture\n")
            built = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                   cwd=folder, env=env, capture_output=True)
            self.assertEqual(built.returncode, 0, built.stderr.decode())
            with tarfile.open(folder / "artifact/fixture.tar.gz") as archive:
                self.assertEqual(set(archive.getnames()), {"package.json", "dist", "dist/index.js"})

    def test_pr_jobs_have_no_signing_permissions(self) -> None:
        """Prevent signing privileges from leaking into repository build execution."""
        workflow = load_workflow()
        self.assertEqual(workflow["permissions"], {"contents": "read"})
        for job_id in ("build", "governance"):
            self.assertNotIn("permissions", workflow["jobs"][job_id])
        signer = workflow["jobs"]["attest"]
        self.assertEqual(signer["permissions"], {
            "contents": "read", "id-token": "write", "attestations": "write"})
        actions = [step.get("uses", "") for step in signer["steps"]]
        self.assertFalse(any("checkout" in action for action in actions))
        self.assertFalse(any("npm " in step.get("run", "") for step in signer["steps"]))

    def test_signer_rejects_untrusted_events_and_refs(self) -> None:
        """Exercise the workflow condition for trusted and adversarial event contexts."""
        workflow = load_workflow()
        self.assertEqual(set(workflow["on"]), {"push", "pull_request", "workflow_dispatch"})
        self.assertEqual(workflow["on"]["push"]["branches"], ["main"])
        self.assertEqual(workflow["on"]["pull_request"]["branches"], ["main"])
        condition = workflow["jobs"]["attest"]["if"]
        # A constrained expression evaluator: only comparisons, boolean operators,
        # constants and named context fields are accepted; never eval repo input.
        import ast
        import itertools
        expression = ast.parse(condition.replace("&&", " and ").replace("||", " or ").strip(), mode="eval")

        def evaluate(node: ast.AST, context: dict[str, str]) -> object:
            if isinstance(node, ast.Expression):
                return evaluate(node.body, context)
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                return node.value
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                self.assertEqual(node.value.id, "github")
                return context[node.attr]
            if isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
                return evaluate(node.left, context) == evaluate(node.comparators[0], context)
            if isinstance(node, ast.BoolOp) and isinstance(node.op, (ast.And, ast.Or)):
                values = [bool(evaluate(value, context)) for value in node.values]
                return all(values) if isinstance(node.op, ast.And) else any(values)
            self.fail(f"Unsupported workflow condition: {ast.dump(node)}")

        for repo, ref, event in itertools.product(
            ("citadel-nexus/guild-research", "fork/guild-research"),
            ("refs/heads/main", "refs/heads/feature", "refs/pull/1/merge", "refs/tags/v1.0.0"),
            ("push", "workflow_dispatch", "pull_request", "pull_request_target", "workflow_run"),
        ):
            with self.subTest(repo=repo, ref=ref, event=event):
                actual = evaluate(expression, {"repository": repo, "ref": ref, "event_name": event})
                expected = (repo == "citadel-nexus/guild-research" and ref == "refs/heads/main"
                            and event in ("push", "workflow_dispatch"))
                self.assertEqual(actual, expected)

    def test_signer_uses_only_current_run_artifact(self) -> None:
        """Prevent artifact substitution from another workflow run or repository."""
        jobs = load_workflow()["jobs"]
        self.assertEqual(set(jobs["attest"]["needs"]), {"governance", "build"})
        upload = next(step for step in jobs["build"]["steps"]
                      if step.get("uses", "").startswith("actions/upload-artifact@"))
        download = jobs["attest"]["steps"][0]
        self.assertTrue(download["uses"].startswith("actions/download-artifact@"))
        self.assertEqual(set(download["with"]), {"name", "path"})
        self.assertEqual(download["with"]["name"], upload["with"]["name"])
        self.assertEqual(upload["with"]["if-no-files-found"], "error")
        attest = next(step for step in jobs["attest"]["steps"] if step.get("id") == "provenance")
        self.assertTrue(attest["uses"].startswith("actions/attest-build-provenance@"))
        self.assertEqual(attest["with"]["subject-path"], "signed/" + upload["with"]["path"].split("/", 1)[1])

    def test_compilation_is_required_before_archive(self) -> None:
        """Reject source-only or empty artifacts and build failures hidden by fallback."""
        steps = load_workflow()["jobs"]["build"]["steps"]
        commands = [step["run"] for step in steps if "run" in step]
        self.assertEqual(commands[1:5], ["npm ci", "npm run lint", "npm test", "npm run build"])
        self.assertIn("package-lock.json", commands[0])
        self.assertIn("test -s dist/index.js", commands[5])
        self.assertIn('tar -czf "artifact/$ARTIFACT_NAME" package.json dist', commands[5])
        self.assertFalse(any("continue-on-error" in step for step in steps))

    def test_verification_binds_identity_ref_and_digest(self) -> None:
        """Require strict verification before signed artifact distribution."""
        steps = load_workflow()["jobs"]["attest"]["steps"]
        verify_index = next(i for i, step in enumerate(steps) if "gh attestation verify" in step.get("run", ""))
        verify = steps[verify_index]["run"]
        for flag in ("--bundle signed/provenance.sigstore.json",
                     "--repo citadel-nexus/guild-research",
                     "--signer-workflow citadel-nexus/guild-research/.github/workflows/build-provenance.yml",
                     "--source-ref refs/heads/main", '--source-digest "$SOURCE_SHA"',
                     "--predicate-type https://slsa.dev/provenance/v1", "--deny-self-hosted-runners"):
            self.assertIn(flag, verify)
        upload = steps[verify_index + 1]
        self.assertTrue(upload["uses"].startswith("actions/upload-artifact@"))
        self.assertIn("signed/provenance.sigstore.json", upload["with"]["path"])


if __name__ == "__main__":
    unittest.main()
