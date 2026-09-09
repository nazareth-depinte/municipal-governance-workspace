import fs from 'node:fs';
import { parseEnv } from 'node:util';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { deploymentEnvironment } from './deployment-config.mjs';

// Never source .env as shell code or print its values.
const envFile = fileURLToPath(new URL('../.env', import.meta.url));
let settings = {};
try { settings = parseEnv(fs.readFileSync(envFile, 'utf8')); }
catch (error) {
  if (error.code !== 'ENOENT') { console.error('Cannot read the local .env file.'); process.exit(1); }
}
const args = process.argv.slice(2);
let shared;
try {
  shared = deploymentEnvironment(JSON.parse(fs.readFileSync(new URL('../config/deployment.json', import.meta.url), 'utf8')));
} catch {
  console.error('Invalid shared deployment configuration. Check config/deployment.json; no secrets were retrieved.');
  process.exit(1);
}
if (args[0] === 'status') {
  console.log(`OP_SERVICE_ACCOUNT_TOKEN (.env): ${settings.OP_SERVICE_ACCOUNT_TOKEN?.trim() ? 'configured' : 'missing'}`);
  console.log('Shared Cloudflare configuration and token reference: valid (config/deployment.json)');
  console.log(`Access allowlist reference: ${shared.CLOUDFLARE_ACCESS_EMAILS ? 'configured' : 'missing'}`);
  process.exit(settings.OP_SERVICE_ACCOUNT_TOKEN?.trim() ? 0 : 1);
}
if (args[0] !== '--' || !args[1]) {
  console.error('Usage: node scripts/with-1password.mjs status | -- <command> [arguments]');
  process.exit(1);
}
if (!settings.OP_SERVICE_ACCOUNT_TOKEN?.trim()) {
  console.error('Set OP_SERVICE_ACCOUNT_TOKEN in the workspace .env first. No secrets were retrieved.');
  process.exit(1);
}
const env = { ...process.env };
// Service-account-only authentication: do not inherit Connect or desktop credentials.
for (const key of Object.keys(env)) if (key.startsWith('OP_') || key.startsWith('CLOUDFLARE_')) delete env[key];
env.OP_SERVICE_ACCOUNT_TOKEN = settings.OP_SERVICE_ACCOUNT_TOKEN;
env.OP_BIOMETRIC_UNLOCK_ENABLED = 'false';
Object.assign(env, shared);
const result = spawnSync('op', ['run', '--', process.execPath, fileURLToPath(new URL('./without-vault-token.mjs', import.meta.url)), ...args.slice(1)], { env, stdio: 'inherit', shell: false });
if (result.error) console.error('Could not start 1Password CLI. Install op and try again.');
process.exit(result.status ?? 1);
