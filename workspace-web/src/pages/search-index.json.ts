import pages from "../generated/pages.json";
export const prerender = true;
import { hrefFor } from "../lib/content-routes";
export function GET(){ return new Response(JSON.stringify(pages.map((p)=>({...p, body: undefined, href: hrefFor(p.sourcePath)}))),{headers:{"Content-Type":"application/json"}}); }
