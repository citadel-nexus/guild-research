import  GuildClient  from '@citadel-guilds/sdk';

const guild = new GuildClient({
  name: 'research',
  natsPrefix: 'citadel.research',
  port: 8200,
});

guild.start();
