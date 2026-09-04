import { readFile } from "node:fs/promises";
import path from "node:path";
import type { Metadata } from "next";
import Link from "next/link";
import { LegacyExplorerClient } from "./LegacyExplorerClient";

export const metadata: Metadata = {
  title: "Anomaly Explorer",
  description:
    "Interactive review of 2,145 SNR-filtered DESI DR1 spectral anomalies — table view, sky map, side-panel inspection, and AI/human commentary tracks.",
};

const REPO_ROOT = path.resolve(/* turbopackIgnore: true */ process.cwd(), "..");

async function loadExplorer(): Promise<{
  style: string;
  body: string;
  script: string;
}> {
  const file = path.join(REPO_ROOT, "anomaly-explorer.html");
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

export default async function AnomalyExplorerPage() {
  const { style, body, script } = await loadExplorer();

  return (
    <>
      <p className="mono mb-3 text-xs uppercase tracking-wider text-muted-foreground">
        <Link href="/explore" className="hover:text-foreground">
          ← Explore
        </Link>
      </p>
      <div className="legacy-explorer-root" suppressHydrationWarning>
        <style dangerouslySetInnerHTML={{ __html: style }} suppressHydrationWarning />
        <style
          dangerouslySetInnerHTML={{ __html: ANOMALY_EXPLORER_OVERRIDES }}
          suppressHydrationWarning
        />
        <LegacyExplorerClient body={body} script={script} />
      </div>
    </>
  );
}

const ANOMALY_EXPLORER_OVERRIDES = `
.legacy-explorer-root .container {
  max-width: none !important;
  padding: 0 !important;
  margin: 0 !important;
}
.legacy-explorer-root table { border-color: var(--border) !important; }
.legacy-explorer-root th, .legacy-explorer-root td { border-color: var(--border) !important; }
.legacy-explorer-root .filter-bar,
.legacy-explorer-root .side-panel,
.legacy-explorer-root .ai-comment {
  background: color-mix(in srgb, var(--surface) 88%, var(--bg)) !important;
  border-color: var(--border) !important;
  border-radius: var(--radius) !important;
}
.legacy-explorer-root input,
.legacy-explorer-root select,
.legacy-explorer-root textarea {
  background: var(--surface) !important;
  color: var(--text) !important;
  border-color: var(--border) !important;
  border-radius: 6px !important;
}
.legacy-explorer-root a { color: var(--accent) !important; }
.legacy-explorer-root .anomaly-row:hover { background: color-mix(in srgb, var(--accent) 8%, var(--surface)) !important; }
`;
