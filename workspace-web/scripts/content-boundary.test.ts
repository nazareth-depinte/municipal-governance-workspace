import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const generated = JSON.parse(fs.readFileSync(path.join(webRoot, "src/generated/pages.json"), "utf8")) as { sourcePath: string }[];
const forbidden = [".env", "node_modules", "repos/", "case-data/", "unredacted/", "investigations/", "attachments/", "exports/"];

test("public projection excludes protected and nested paths", () => {
  for (const page of generated) {
    for (const marker of forbidden) assert.equal(page.sourcePath.includes(marker), false, `${page.sourcePath} contains ${marker}`);
  }
});

test("architecture and authority are always present", () => {
  const paths = new Set(generated.map((page) => page.sourcePath));
  assert.ok(paths.has("docs/architecture/GOVERNANCE-ARCHITECTURE.md"));
  assert.ok(paths.has("AUTHORITY.md"));
});
