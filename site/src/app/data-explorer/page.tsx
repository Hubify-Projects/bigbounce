import { readFile } from "node:fs/promises";
import path from "node:path";
import type { Metadata } from "next";

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
    <div className="data-explorer-root">
      <style dangerouslySetInnerHTML={{ __html: style }} />
      <div dangerouslySetInnerHTML={{ __html: body }} />
      <script dangerouslySetInnerHTML={{ __html: script }} />
    </div>
  );
}
