import path from 'node:path';

export const movedBriefings: Record<string, string> = {
  'docs/architecture/DEMO-GEMEENTETEAM.md': 'demo-gemeenteteam',
  'evidence/2026-09-07-cloudflare-en-europese-hosting/BRIEFING.md': 'cloudflare-en-europese-hosting',
  'evidence/2026-09-06-digitale-dienstverlening/BRIEFING-WEBSITEPROBLEMEN.md': 'websiteproblemen',
  'evidence/2026-09-07-ai-piloot/BRIEFING.md': 'ai-piloot',
};

export const briefingSources = ['website-controles.json', 'prestatie-hermeting.json', 'audit_public.py', 'diensteninventaris.csv', 'bronmanifest.json'];

export function hrefFor(sourcePath: string): string {
  if (movedBriefings[sourcePath]) return `/briefings/${movedBriefings[sourcePath]}/`;
  if (sourcePath.startsWith('briefings/')) return `/briefings/${path.posix.basename(sourcePath, '.md')}/`;
  if (sourcePath === 'projects/README.md') return '/projects/';
  if (sourcePath.startsWith('projects/')) return `/projects/${path.posix.basename(sourcePath, '.md')}/`;
  if (sourcePath === 'docs/architecture/GOVERNANCE-ARCHITECTURE.md') return '/architecture/';
  if (sourcePath === 'AUTHORITY.md') return '/authority/';
  return `/knowledge/${sourcePath.replace(/\.md$/, '').replace(/\/README$/, '')}/`;
}

// Resolve document-relative references without exposing arbitrary workspace files.
export function briefingLink(href: string, sourcePath: string): string {
  if (/^(?:[a-z][a-z\d+.-]*:|\/|#)/i.test(href)) return href;
  const [file, fragment] = href.split('#');
  const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(sourcePath), file));
  if (resolved.endsWith('.md')) return hrefFor(resolved) + (fragment ? `#${fragment}` : '');
  if (resolved.startsWith('evidence/2026-09-06-digitale-dienstverlening/') && briefingSources.includes(path.posix.basename(resolved))) return `/briefings/bronnen/${path.posix.basename(resolved)}`;
  return href;
}
