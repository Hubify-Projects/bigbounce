import { cp, mkdir, readdir, readFile, rm, stat, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const repoRoot = path.dirname(siteRoot);
const oldRoot = path.join(siteRoot, "public", "old");

const htmlFiles = [
  "404.html",
  "activity.html",
  "admin.html",
  "animations.html",
  "anomaly-explorer.html",
  "articles.html",
  "arxiv-preview.html",
  "bigbounce-md.html",
  "chat.html",
  "contributions.html",
  "data-comparison.html",
  "data-explorer.html",
  "datasets.html",
  "explained.html",
  "figures.html",
  "findings.html",
  "galaxy-explorer.html",
  "galaxy-zoo.html",
  "glossary.html",
  "index.html",
  "infrastructure.html",
  "interactive-data.html",
  "mathematics.html",
  "methodology-anomaly.html",
  "methodology.html",
  "paper.html",
  "projects.html",
  "review.html",
  "sitemap.html",
  "sources.html",
  "speculations.html",
  "ssot.html",
  "status.html",
  "team.html",
  "timeline.html",
  "versions.html",
  "view-pdf.html",
  "visualize.html",
];

const supportFiles = ["style.css", "styles.css", "nav.js", "search.js", "gate.js"];
const legacyDirs = [
  "articles",
  "astro",
  "assets",
  "review",
  "versions",
  "wiki",
  path.join("research", "project_master_dossier"),
  "paper",
];

function rewriteLegacyHtml(html) {
  return html
    .replace(/(["'(])public\//g, "$1/")
    .replace(/(["'])\/astro\//g, "$1astro/")
    .replace(/https:\/\/bigbounce\.hubify\.app\/public\//g, "https://bigbounce.hubify.app/");
}

async function exists(file) {
  try {
    await stat(file);
    return true;
  } catch {
    return false;
  }
}

async function copyIfExists(from, to) {
  if (!(await exists(from))) return;
  await mkdir(path.dirname(to), { recursive: true });
  await cp(from, to, { recursive: true, force: true });
}

await rm(oldRoot, { recursive: true, force: true });
await mkdir(oldRoot, { recursive: true });

for (const file of htmlFiles) {
  const source = path.join(repoRoot, file);
  if (!(await exists(source))) continue;
  const html = await readFile(source, "utf8");
  await writeFile(path.join(oldRoot, file), rewriteLegacyHtml(html));
}

for (const file of supportFiles) {
  await copyIfExists(path.join(repoRoot, file), path.join(oldRoot, file));
}

for (const dir of legacyDirs) {
  await copyIfExists(path.join(repoRoot, dir), path.join(oldRoot, dir));
}

const publicRoot = path.join(repoRoot, "public");
const sitePublicRoot = path.join(siteRoot, "public");
if (await exists(publicRoot)) {
  for (const item of await readdir(publicRoot)) {
    await copyIfExists(path.join(publicRoot, item), path.join(sitePublicRoot, item));
  }
}

console.log(`Copied legacy static site to ${path.relative(repoRoot, oldRoot)}`);
