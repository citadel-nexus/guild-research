// File: tests/health.test.mjs
// Stage: 08_TEST
// SRS: SRS-CN-RESEARCH-BUILD-001
// CAPS: pending
// CK: pending
// Dispatch: DISP-BUILD-research
// Seat: BITS-CODEGEN
// Owner: Citadel Nexus Inc.
// Created: 2026-10-20
// Depends: src/routes/health.ts, package.json
// EnumType: Test
// EnumEdges: DEPENDS_ON src/routes/health.ts; DEPENDS_ON package.json
// DAG Node: none
// Intent: Verify the existing public health response without production or event-bus connections.

import assert from 'node:assert/strict';
import { test } from 'node:test';
import { healthCheck } from '../src/routes/health.ts';

test('health reports the public Research identity and scaffold status', () => {
  const result = healthCheck();
  assert.equal(result.guild, 'research');
  assert.equal(result.status, 'healthy');
  assert.equal(result.version, '0.1.0');
  assert.deepEqual(Object.keys(result).sort(),
    ['guild', 'nats_prefix', 'status', 'timestamp', 'version']);
});

test('health generates a fresh UTC timestamp for each request', (context) => {
  context.mock.timers.enable({ apis: ['Date'], now: Date.UTC(2026, 0, 1) });
  assert.equal(healthCheck().timestamp, '2026-01-01T00:00:00.000Z');
  context.mock.timers.tick(1250);
  assert.equal(healthCheck().timestamp, '2026-01-01T00:00:01.250Z');
});

test('callers cannot mutate subsequent health responses', () => {
  const first = healthCheck();
  first.status = 'changed by caller';
  assert.equal(healthCheck().status, 'healthy');
  assert.notEqual(first, healthCheck());
});
