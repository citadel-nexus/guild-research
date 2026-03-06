import  connect, StringCodec  from 'nats';

const sc = StringCodec();

export async function startListener() {
  const nc = await connect( servers: process.env.NATS_URL );
  const sub = nc.subscribe('citadel.research.>');
  console.log(`[research] Listening on citadel.research.*`);
  for await (const msg of sub) {
    const data = sc.decode(msg.data);
    console.log(`[research] $msg.subject: $data`);
    // Route to handlers based on msg.subject
  }
}
