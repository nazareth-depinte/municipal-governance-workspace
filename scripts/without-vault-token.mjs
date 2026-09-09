import { spawnSync } from 'node:child_process';

// The deployment process gets the resolved Cloudflare credential, never the vault token.
const env = { ...process.env };
for (const key of Object.keys(env)) if (key.startsWith('OP_')) delete env[key];
const [command, ...args] = process.argv.slice(2);
if (!command) process.exit(1);
const result = spawnSync(command, args, { env, stdio: 'inherit', shell: false });
if (result.error) console.error('Could not start the requested command.');
process.exit(result.status ?? 1);
