// File: tests/build.test.mjs
// Stage: 08_TEST
// SRS: SRS-CN-RESEARCH-BUILD-001
// CAPS: pending
// CK: pending
// Dispatch: DISP-BUILD-research
// Seat: BITS-CODEGEN
// Owner: Citadel Nexus Inc.
// Created: 2026-10-20
// Depends: package.json
// EnumType: Test
// EnumEdges: DEPENDS_ON package.json
// DAG Node: none
// Intent: Prevent stale output from surviving a clean build while preserving source files.

import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, existsSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { URL } from 'node:url';
import { test } from 'node:test';

const manifest = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8'));

test('clean removes stale compiled files and preserves source inputs', (context) => {
  const directory = mkdtempSync(join(tmpdir(), 'research-build-'));
  context.after(() => rmSync(directory, { recursive: true, force: true }));
  mkdirSync(join(directory, 'dist'));
  mkdirSync(join(directory, 'src'));
  writeFileSync(join(directory, 'dist/index.js'), '// stale fixture');
  writeFileSync(join(directory, 'src/index.ts'), '// source fixture');
  const result = spawnSync(manifest.scripts.clean, { cwd: directory, shell: true, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  assert.equal(existsSync(join(directory, 'dist')), false);
  assert.equal(readFileSync(join(directory, 'src/index.ts'), 'utf8'), '// source fixture');
});

test('clean succeeds when no previous build exists', (context) => {
  const directory = mkdtempSync(join(tmpdir(), 'research-build-'));
  context.after(() => rmSync(directory, { recursive: true, force: true }));
  const result = spawnSync(manifest.scripts.clean, { cwd: directory, shell: true, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  assert.equal(existsSync(join(directory, 'dist')), false);
});
