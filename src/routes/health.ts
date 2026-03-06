export function healthCheck() {
  return {
    guild: 'research',
    status: 'healthy',
    version: '0.1.0',
    nats_prefix: 'citadel.research.*',
    timestamp: new Date().toISOString(),
  };
}
