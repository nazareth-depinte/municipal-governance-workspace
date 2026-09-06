import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import fg from "fast-glob";
import matter from "gray-matter";
import yaml from "yaml";

const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const root = path.resolve(webRoot, "..");
const include = ["README.md", "MAP.md", "AUTHORITY.md", "RIGHTS.md", "constitutional/**/*.md", "competences/**/*.md", "decisions/**/*.md", "evidence/**/*.md", "participation/**/*.md", "standards/**/*.md", "docs/architecture/**/*.md"];
const forbidden = ["**/.env*", "**/node_modules/**", "repos/**", "**/case-data/**", "**/unredacted/**", "**/investigations/**", "**/attachments/**", "**/exports/**"];

const pages = fg.sync(include, { cwd: root, onlyFiles: true, ignore: forbidden }).map((sourcePath) => {
  const raw = fs.readFileSync(path.join(root, sourcePath), "utf8");
  const parsed = matter(raw);
  const heading = /^#\s+(.+)$/m.exec(parsed.content)?.[1];
  const title = String(parsed.data.title ?? heading ?? path.basename(sourcePath, ".md"));
  const description = parsed.content.split("\n").map((line) => line.trim()).find((line) => line && !line.startsWith("#") && !line.startsWith("|") && !line.startsWith("```") ) ?? "";
  const section = sourcePath.includes("/") ? sourcePath.split("/")[0] : "spine";
  return { title, description, sourcePath, section, body: parsed.content, status: String(parsed.data.status ?? "active") };
});

const registry = yaml.parse(fs.readFileSync(path.join(root, "repos/_registry.yml"), "utf8"));
const out = path.join(webRoot, "src/generated");
fs.mkdirSync(out, { recursive: true });
fs.writeFileSync(path.join(out, "pages.json"), JSON.stringify(pages, null, 2));
fs.writeFileSync(path.join(out, "registry.json"), JSON.stringify(registry.repositories, null, 2));
console.log(`Collected ${pages.length} public pages and ${registry.repositories.length} repositories.`);

