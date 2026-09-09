export function deploymentEnvironment(config) {
  if (config.schemaVersion !== 1) throw Error('Unsupported deployment configuration version.');
  const { cloudflare, onePassword } = config;
  const reference = /^op:\/\/[^/\r\n]+\/[^/\r\n]+\/[^\r\n]+$/;
  if (!reference.test(onePassword.cloudflareApiTokenRef ?? '')) throw Error('Configure a 1Password reference in config/deployment.json, never a raw Cloudflare token.');
  if (onePassword.cloudflareAccessEmailsRef != null && !reference.test(onePassword.cloudflareAccessEmailsRef)) throw Error('The Access allowlist must be a 1Password reference.');
  for (const key of ['accountId', 'zoneId']) if (!/^[a-f0-9]{32}$/i.test(cloudflare[key] ?? '')) throw Error(`Invalid Cloudflare ${key} in config/deployment.json.`);
  if (!/^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+net$/.test(cloudflare.hostname ?? '')) throw Error('Invalid test hostname in config/deployment.json.');
  const domains = cloudflare.accessEmailDomains ?? [];
  if (!Array.isArray(domains) || !domains.every(domain => typeof domain === 'string' && /^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}$/.test(domain))) throw Error('Invalid Access email domain.');
  return {
    CLOUDFLARE_API_TOKEN: onePassword.cloudflareApiTokenRef,
    CLOUDFLARE_ACCOUNT_ID: cloudflare.accountId,
    CLOUDFLARE_ZONE_ID: cloudflare.zoneId,
    CLOUDFLARE_HOSTNAME: cloudflare.hostname,
    CLOUDFLARE_ACCESS_EMAIL_DOMAINS: domains.join(','),
    ...(onePassword.cloudflareAccessEmailsRef ? { CLOUDFLARE_ACCESS_EMAILS: onePassword.cloudflareAccessEmailsRef } : {}),
  };
}
