import { defineConfig } from "astro/config";
import { movedBriefings } from "./src/lib/content-routes";

export default defineConfig({
  output: "static",
  redirects: Object.fromEntries(Object.entries(movedBriefings).map(([source, slug]) => [`/knowledge/${source.replace(/\.md$/, "")}/`, `/briefings/${slug}/`])),
  trailingSlash: "always",
  build: { inlineStylesheets: "auto" },
  devToolbar: { enabled: false }
});

