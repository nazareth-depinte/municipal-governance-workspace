import fs from 'node:fs';
import path from 'node:path';
import { briefingSources } from '../../../lib/content-routes';
export const prerender = true;
export function getStaticPaths() { return briefingSources.map(file => ({params: {file}})); }
export function GET({ params }: {params: {file?: string}}) {
  if (!params.file || !briefingSources.includes(params.file)) return new Response('Not found', {status:404});
  const source = path.resolve('../evidence/2026-09-06-digitale-dienstverlening', params.file);
  return new Response(fs.readFileSync(source), {headers: {'Content-Type': params.file.endsWith('.json') ? 'application/json' : 'text/plain; charset=utf-8'}});
}
