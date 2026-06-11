import { readFile } from "node:fs/promises";
import path from "node:path";
import type { Metadata } from "next";
import { DataExplorerClient } from "./DataExplorerClient";

export const metadata: Metadata = {
  title: "Data Explorer",
  description:
    "Interactive dashboard for the BigBounce MCMC chains, anomaly catalog, chirality catalog, and observational datasets.",
};

const REPO_ROOT = path.resolve(/* turbopackIgnore: true */ process.cwd(), "..");

async function loadExplorer(): Promise<{
  style: string;
  body: string;
  script: string;
}> {
  const file = path.join(REPO_ROOT, "data-explorer.html");
  const html = await readFile(file, "utf-8");

  const styleMatch = html.match(/<style>([\s\S]*?)<\/style>/);
  const mainMatch = html.match(/<main>([\s\S]*?)<\/main>/);
  // Find first inline <script> after </main> (the datasets+logic block)
  const afterMain = mainMatch ? html.slice((mainMatch.index ?? 0) + mainMatch[0].length) : "";
  const scriptMatch = afterMain.match(/<script>([\s\S]*?)<\/script>/);

  return {
    style: styleMatch?.[1] ?? "",
    body: mainMatch?.[1] ?? "",
    script: scriptMatch?.[1] ?? "",
  };
}

export default async function DataExplorerPage() {
  const { style, body, script } = await loadExplorer();

  return (
    <div className="data-explorer-root" suppressHydrationWarning>
      <style dangerouslySetInnerHTML={{ __html: style }} suppressHydrationWarning />
      <style
        dangerouslySetInnerHTML={{ __html: DATA_EXPLORER_OVERRIDES }}
        suppressHydrationWarning
      />
      <DataExplorerClient body={body} script={script} />
    </div>
  );
}

const DATA_EXPLORER_OVERRIDES = `
/* Bound the explorer + dataset tab rail to the viewport: the legacy mobile
   breakpoint turns .de-sidebar into a horizontal nowrap rail, which must
   scroll inside its own box rather than widening the page. */
.data-explorer-root,
.data-explorer-root .explorer,
.data-explorer-root .de-sidebar,
.data-explorer-root .main-panel {
  max-width: 100%;
  min-width: 0;
}
.data-explorer-root .de-sidebar { background: var(--surface-2) !important; }
.data-explorer-root .de-sidebar-group .dot.green,
.data-explorer-root .de-sidebar-group .dot.blue,
.data-explorer-root .de-sidebar-group .dot.purple { background: var(--accent) !important; }
.data-explorer-root .de-sidebar-group .dot.orange { background: var(--warn) !important; }
.data-explorer-root .de-sidebar-item {
  color: var(--text-secondary) !important;
  border: 1px solid transparent !important;
}
.data-explorer-root .de-sidebar-item:hover {
  background: color-mix(in srgb, var(--surface) 78%, var(--bg)) !important;
}
.data-explorer-root .de-sidebar-item.active {
  background: color-mix(in srgb, var(--accent) 12%, var(--surface)) !important;
  color: var(--accent) !important;
  border-color: color-mix(in srgb, var(--accent) 28%, transparent) !important;
}
.data-explorer-root .de-sidebar-badge,
.data-explorer-root .de-sidebar-badge.frozen,
.data-explorer-root .de-sidebar-badge.active-badge,
.data-explorer-root .de-sidebar-badge.ref,
.data-explorer-root .status-badge,
.data-explorer-root .status-badge.frozen,
.data-explorer-root .status-badge.active-badge,
.data-explorer-root .status-badge.ref {
  background: color-mix(in srgb, var(--surface) 86%, var(--bg)) !important;
  color: var(--accent) !important;
  border: 1px solid color-mix(in srgb, var(--accent) 28%, transparent) !important;
}
.data-explorer-root .main-panel {
  padding-left: clamp(22px, 3vw, 42px) !important;
  padding-right: clamp(22px, 3vw, 42px) !important;
}
.data-explorer-root .table-wrap,
.data-explorer-root .controls-bar .btn,
.data-explorer-root .search-bar {
  border-color: var(--border) !important;
  background-color: color-mix(in srgb, var(--surface) 88%, var(--bg)) !important;
  border-radius: var(--radius) !important;
}
`;
