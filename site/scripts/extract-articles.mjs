import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, "..", "..");
const SRC = path.join(REPO_ROOT, "articles.html");
const OUT = path.resolve(__dirname, "..", "src", "data", "articles.ts");

const html = readFileSync(SRC, "utf-8");

const decode = (s) =>
  s
    .replace(/<[^>]+>/g, "")
    .replace(/&mdash;/g, "—")
    .replace(/&ndash;/g, "–")
    .replace(/&middot;/g, "·")
    .replace(/&amp;/g, "&")
    .replace(/&nbsp;/g, " ")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&sigma;/g, "σ")
    .replace(/\\\(/g, "")
    .replace(/\\\)/g, "")
    .replace(/\\,/g, " ")
    .replace(/\\;/g, " ")
    .replace(/\$([^$]+)\$/g, "$1")
    .replace(/\\mathrm\{([^}]+)\}/g, "$1")
    .replace(/f_\{NL\}/g, "f_NL")
    .replace(/\\rho_\{crit\}/g, "ρ_crit")
    .replace(/\\rho_\{Pl\}/g, "ρ_Pl")
    .replace(/\\approx/g, "≈")
    .replace(/\\sigma/g, "σ")
    .replace(/\s+/g, " ")
    .trim();

const cardRe =
  /<div class="card"[^>]*>[\s\S]*?<p class="text-xs sans"[^>]*>([\s\S]*?)<\/p>[\s\S]*?<h3[^>]*><a href="articles\/([^"]+)\.html">([\s\S]*?)<\/a><\/h3>[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>[\s\S]*?<\/div>\s*<\/div>/g;

const articles = [];
let m;
while ((m = cardRe.exec(html)) !== null) {
  const meta = decode(m[1]);
  const slug = m[2];
  const title = decode(m[3]);
  const summary = decode(m[4]);
  // Split meta on bullet (·) — first segment is type, second is category
  const parts = meta
    .split(/[·•]/)
    .map((s) => s.trim())
    .filter(Boolean)
    .filter((s) => s.toUpperCase() !== "NEW");
  const isNew = /\bNEW\b/i.test(meta);
  articles.push({
    slug,
    title,
    summary,
    type: parts[0] || "",
    category: parts.slice(1).join(" · ") || "",
    isNew,
  });
}

console.log(`Parsed ${articles.length} articles.`);

const ts = `// AUTO-GENERATED from /articles.html — do not edit by hand.
// Regenerate with: cd site && node scripts/extract-articles.mjs

export interface Article {
  slug: string;
  title: string;
  summary: string;
  type: string;
  category: string;
  isNew: boolean;
}

export const articles: Article[] = ${JSON.stringify(articles, null, 2)};
`;

writeFileSync(OUT, ts);
console.log(`Wrote ${OUT}`);
