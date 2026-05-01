import { readFile } from "node:fs/promises";
import path from "node:path";
import type { Metadata } from "next";
import { LegacyExplorerClient } from "./LegacyExplorerClient";

export const metadata: Metadata = {
  title: "Galaxy Chirality Explorer",
  description:
    "Interactive exploration of the 8.47M-galaxy DESI Legacy DR8 chirality catalog (CW / CCW / NOT_SPIRAL classification, hemispheric statistics, look-elsewhere null).",
};

const REPO_ROOT = path.resolve(/* turbopackIgnore: true */ process.cwd(), "..");

async function loadExplorer(): Promise<{
  style: string;
  body: string;
  script: string;
}> {
  const file = path.join(REPO_ROOT, "galaxy-explorer.html");
  const html = await readFile(file, "utf-8");

  const styleMatch = html.match(/<style>([\s\S]*?)<\/style>/);
  const mainMatch = html.match(/<main[^>]*>([\s\S]*?)<\/main>/);
  const afterMain = mainMatch ? html.slice((mainMatch.index ?? 0) + mainMatch[0].length) : "";
  const scriptMatch = afterMain.match(/<script>([\s\S]*?)<\/script>/);

  return {
    style: styleMatch?.[1] ?? "",
    body: mainMatch?.[1] ?? "",
    script: scriptMatch?.[1] ?? "",
  };
}

export default async function GalaxyExplorerPage() {
  const { style, body, script } = await loadExplorer();

  return (
    <div className="legacy-explorer-root" suppressHydrationWarning>
      <style dangerouslySetInnerHTML={{ __html: style }} suppressHydrationWarning />
      <style
        dangerouslySetInnerHTML={{ __html: LEGACY_EXPLORER_OVERRIDES }}
        suppressHydrationWarning
      />
      <LegacyExplorerClient body={body} script={script} />
    </div>
  );
}

const LEGACY_EXPLORER_OVERRIDES = `
.legacy-explorer-root .wide-container,
.legacy-explorer-root .container {
  max-width: none !important;
  padding: 0 !important;
  margin: 0 !important;
}
.legacy-explorer-root .gx-stat,
.legacy-explorer-root .gx-filters,
.legacy-explorer-root table,
.legacy-explorer-root .gx-pagination button {
  border-color: var(--border) !important;
}
.legacy-explorer-root .gx-filters {
  background: color-mix(in srgb, var(--surface) 88%, var(--bg)) !important;
  border-radius: var(--radius) !important;
}
.legacy-explorer-root .gx-filter-group select,
.legacy-explorer-root .gx-filter-group input {
  background: var(--surface) !important;
  color: var(--text) !important;
  border-radius: 6px !important;
}
.legacy-explorer-root a { color: var(--accent) !important; }
`;
