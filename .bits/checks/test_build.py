# File: .bits/checks/test_build.py
# Stage: 11_COMMIT
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: package.json, tsconfig.json, .nvmrc, .github/workflows/ci.yml, .github/workflows/release.yml, .github/workflows/security-scan.yml, .github/workflows/build-provenance.yml
# EnumType: Test
# EnumEdges: DEPENDS_ON package.json; DEPENDS_ON tsconfig.json; DEPENDS_ON .nvmrc; DEPENDS_ON .github/workflows/ci.yml; DEPENDS_ON .github/workflows/release.yml; DEPENDS_ON .github/workflows/security-scan.yml; DEPENDS_ON .github/workflows/build-provenance.yml
# DAG Node: none
# Intent: Keep strict build checks, pinned runtimes, real dependencies and security scans mandatory.

"""Check the staging build gates without contacting registries or production."""

import json
from pathlib import Path
import unittest
from typing import Any, cast

import yaml

ROOT = Path(__file__).resolve().parents[2]


def workflow(name: str) -> dict[str, Any]:
    """Read workflow conditions without coercing the on key into a boolean."""
    return cast(dict[str, Any], yaml.load(
        (ROOT / f".github/workflows/{name}.yml").read_text(), Loader=yaml.BaseLoader))


class BuildRepairTests(unittest.TestCase):
    """Protect reproducibility, scanner retention and output safety."""

    def test_node_pin_is_used_by_all_build_surfaces(self) -> None:
        """Require CI, release, provenance, CodeQL and Docker to use the pinned runtime."""
        version = (ROOT / ".nvmrc").read_text().strip()
        package = json.loads((ROOT / "package.json").read_text())
        self.assertEqual(package["engines"]["node"], version)
        self.assertEqual(package["packageManager"], "npm@" + package["engines"]["npm"])
        for name in ("ci", "release", "build-provenance", "security-scan"):
            with self.subTest(workflow=name):
                setup = [step for job in workflow(name)["jobs"].values() for step in job["steps"]
                         if step.get("uses", "").startswith("actions/setup-node@")]
                self.assertTrue(setup)
                for step in setup:
                    self.assertEqual(step["with"]["node-version-file"], ".nvmrc")
                    self.assertNotIn("node-version", step["with"])
        images = [line.split()[1] for line in (ROOT / "docker/Dockerfile").read_text().splitlines()
                  if line.startswith("FROM ")]
        self.assertEqual(images, [f"node:{version}-alpine"] * 2)

    def test_typescript_cannot_emit_on_errors(self) -> None:
        """Require all source files and real dependency types without permissive shims."""
        config = json.loads((ROOT / "tsconfig.json").read_text())
        self.assertEqual(config["include"], ["src/**/*.ts"])
        options = config["compilerOptions"]
        self.assertIs(options["strict"], True)
        self.assertIs(options["noEmitOnError"], True)
        self.assertIs(options["skipLibCheck"], False)
        self.assertEqual(options["outDir"], "dist")
        self.assertNotIn("paths", options)

    def test_all_build_jobs_require_lint_types_tests_and_compilation(self) -> None:
        """Require every build surface to run all gates without continuing on failures."""
        for name, job in (("ci", "build"), ("release", "release"), ("build-provenance", "build")):
            with self.subTest(workflow=name):
                steps = workflow(name)["jobs"][job]["steps"]
                commands = [step["run"] for step in steps if "run" in step]
                required = ["npm ci", "npm run lint", "npm run typecheck", "npm test", "npm run build"]
                positions = [commands.index(command) for command in required]
                self.assertEqual(positions, sorted(positions))
                self.assertFalse(any("continue-on-error" in step for step in steps))

    def test_security_scanners_are_retained(self) -> None:
        """Require CodeQL init/analyze and secret scanning with private-import checks."""
        jobs = workflow("security-scan")["jobs"]
        actions = [step.get("uses", "") for step in jobs["codeql"]["steps"]]
        for action in ("init", "analyze"):
            self.assertTrue(any(value.startswith(f"github/codeql-action/{action}@") for value in actions))
        secret_steps = jobs["secret-scan"]["steps"]
        self.assertTrue(any(step.get("uses", "").startswith("trufflesecurity/trufflehog@") for step in secret_steps))
        self.assertTrue(any(step.get("name") == "Check private imports" for step in secret_steps))
        self.assertFalse(any("continue-on-error" in step for job in jobs.values() for step in job["steps"]))

    def test_registry_login_uses_github_expressions(self) -> None:
        """Prevent literal expressions from reaching GHCR login."""
        steps = workflow("ci")["jobs"]["docker"]["steps"]
        login = next(step for step in steps if step.get("uses", "").startswith("docker/login-action@"))
        self.assertEqual(login["with"]["username"], "${{ github.actor }}")
        self.assertEqual(login["with"]["password"], "${{ secrets.GITHUB_TOKEN }}")

    def test_dispatch_is_registered_and_sdk_remains_required(self) -> None:
        """Retain real SDK/NATS dependencies and the explicit build-repair authorization."""
        registry = yaml.safe_load((ROOT / ".bits/srs_registry.yml").read_text())
        self.assertEqual(registry["SRS-CN-RESEARCH-BUILD-001"]["dispatch"], "DISP-BUILD-research")
        package = json.loads((ROOT / "package.json").read_text())
        self.assertIn("@citadel-guilds/sdk", package["dependencies"])
        self.assertIn("nats", package["dependencies"])
        self.assertNotIn("optionalDependencies", package)
        self.assertEqual(package["scripts"]["typecheck"], "tsc --noEmit")
        self.assertTrue(package["scripts"]["build"].startswith("npm run clean && "))
        self.assertNotIn("passWithNoTests", package["scripts"]["test"])


if __name__ == "__main__":
    unittest.main()
