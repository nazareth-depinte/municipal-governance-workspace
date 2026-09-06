import pages from "../generated/pages.json";
export const prerender = true;
export function GET(){ return new Response(JSON.stringify(pages.map((p)=>({...p, body: undefined, href: p.sourcePath === "docs/architecture/GOVERNANCE-ARCHITECTURE.md" ? "/architecture/" : p.sourcePath === "AUTHORITY.md" ? "/authority/" : "/knowledge/"}))),{headers:{"Content-Type":"application/json"}}); }

