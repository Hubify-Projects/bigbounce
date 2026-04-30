import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, "..", "..");
const FIGURES_HTML = path.join(REPO_ROOT, "figures.html");
const OUT_PATH = path.resolve(__dirname, "..", "src", "data", "figures.ts");

const html = readFileSync(FIGURES_HTML, "utf-8");

const SECTION_RE = /<h2>([^<]+(?:<[^>]+>[^<]*<\/[^>]+>[^<]*)*?)<span class="section-count">/g;
const ITEM_RE =
  /<div class="gallery-item">[\s\S]*?<img src="([^"]+)" alt="([^"]*)"[^>]*>[\s\S]*?<div class="gallery-item-number">([^<]+)<\/div>[\s\S]*?<div class="gallery-item-title">([\s\S]*?)<\/div>[\s\S]*?<p class="gallery-desc">([\s\S]*?)<\/p>(?:[\s\S]*?<span class="gallery-source">([\s\S]*?)<\/span>)?[\s\S]*?<\/div>\s*<\/div>/g;

function decodeText(s) {
  return s
    .replace(/<[^>]+>/g, "")
    .replace(/&mdash;/g, "—")
    .replace(/&ndash;/g, "–")
    .replace(/&minus;/g, "−")
    .replace(/&plusmn;/g, "±")
    .replace(/&times;/g, "×")
    .replace(/&sigma;/g, "σ")
    .replace(/&alpha;/g, "α")
    .replace(/&beta;/g, "β")
    .replace(/&gamma;/g, "γ")
    .replace(/&Delta;/g, "Δ")
    .replace(/&Omega;/g, "Ω")
    .replace(/&omega;/g, "ω")
    .replace(/&Lambda;/g, "Λ")
    .replace(/&lambda;/g, "λ")
    .replace(/&rho;/g, "ρ")
    .replace(/&pi;/g, "π")
    .replace(/&ell;/g, "ℓ")
    .replace(/&hellip;/g, "…")
    .replace(/&middot;/g, "·")
    .replace(/&isin;/g, "∈")
    .replace(/&asymp;/g, "≈")
    .replace(/&ge;/g, "≥")
    .replace(/&le;/g, "≤")
    .replace(/&ldquo;/g, "“")
    .replace(/&rdquo;/g, "”")
    .replace(/&lsquo;/g, "‘")
    .replace(/&rsquo;/g, "’")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/\\\(/g, "")
    .replace(/\\\)/g, "")
    .replace(/\$([^$]+)\$/g, "$1")
    .replace(/\\mathrm\{([^}]+)\}/g, "$1")
    .replace(/\\hat\{R\}/g, "R̂")
    .replace(/\\Upsilon/g, "Υ")
    .replace(/\\sigma/g, "σ")
    .replace(/\\rho/g, "ρ")
    .replace(/\\Omega/g, "Ω")
    .replace(/\\Delta/g, "Δ")
    .replace(/\\beta/g, "β")
    .replace(/\\gamma/g, "γ")
    .replace(/\\alpha/g, "α")
    .replace(/\\Lambda/g, "Λ")
    .replace(/\\ell/g, "ℓ")
    .replace(/\\to/g, "→")
    .replace(/\\rightarrow/g, "→")
    .replace(/\\sim/g, "~")
    .replace(/\\cdot/g, "·")
    .replace(/\\approx/g, "≈")
    .replace(/\\text\{([^}]+)\}/g, "$1")
    .replace(/\\mathcal\{([^}]+)\}/g, "$1")
    .replace(/\\;/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

const allSections = [];
let lastIndex = 0;
const sectionStarts = [];
const sectionRegex = /<h2>([\s\S]*?)<span class="section-count">([^<]+)<\/span>[\s\S]*?<\/h2>([\s\S]*?)(?=<h2>|<\/main>)/g;
let match;
while ((match = sectionRegex.exec(html)) !== null) {
  const sectionTitle = decodeText(match[1]);
  const sectionCount = decodeText(match[2]);
  const sectionBody = match[3];
  const items = [];
  let im;
  ITEM_RE.lastIndex = 0;
  while ((im = ITEM_RE.exec(sectionBody)) !== null) {
    const rawSrc = im[1];
    const src = rawSrc.startsWith("http") || rawSrc.startsWith("/") ? rawSrc : `/${rawSrc}`;
    items.push({
      src,
      alt: im[2],
      number: decodeText(im[3]),
      title: decodeText(im[4]),
      desc: decodeText(im[5]),
      source: decodeText(im[6] || ""),
    });
  }
  allSections.push({ title: sectionTitle, count: sectionCount, items });
}

const totalItems = allSections.reduce((s, sec) => s + sec.items.length, 0);
console.log(`Parsed ${allSections.length} sections, ${totalItems} figures.`);

const ts = `// AUTO-GENERATED from /figures.html — do not edit by hand.
// Regenerate with: cd site && node scripts/extract-figures.mjs

export interface Figure {
  src: string;
  alt: string;
  number: string;
  title: string;
  desc: string;
  source: string;
}

export interface FigureSection {
  title: string;
  count: string;
  items: Figure[];
}

export const figureSections: FigureSection[] = ${JSON.stringify(allSections, null, 2)};

export const allFigures: Figure[] = figureSections.flatMap((s) => s.items);
`;

writeFileSync(OUT_PATH, ts);
console.log(`Wrote ${OUT_PATH}`);
