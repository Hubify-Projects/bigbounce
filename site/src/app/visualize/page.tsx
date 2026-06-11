import { readFile } from "node:fs/promises";
import path from "node:path";
import type { Metadata } from "next";
import { LegacyVisualizeClient } from "./LegacyVisualizeClient";

export const metadata: Metadata = {
  title: "Visualize the Bounce",
  description:
    "Interactive dark-mode cosmic simulation tracing parent universe → ECH bounce → reheating → CMB → SPHEREx 2028.",
};

const REPO_ROOT = path.resolve(/* turbopackIgnore: true */ process.cwd(), "..");

async function loadVisualize(): Promise<{
  style: string;
  body: string;
  script: string;
}> {
  const file = path.join(REPO_ROOT, "visualize.html");
  const html = await readFile(file, "utf-8");

  const styleMatch = html.match(/<style>([\s\S]*?)<\/style>/);

  const bodyOpenIdx = html.indexOf("<body>");
  const bodyCloseIdx = html.indexOf("</body>");
  const bodyInner =
    bodyOpenIdx >= 0 && bodyCloseIdx > bodyOpenIdx
      ? html.slice(bodyOpenIdx + "<body>".length, bodyCloseIdx)
      : "";

  const inlineScriptMatch = bodyInner.match(/<script>([\s\S]*?)<\/script>/);
  const scriptStart = inlineScriptMatch?.index ?? bodyInner.length;
  const bodyContent = bodyInner.slice(0, scriptStart);

  return {
    style: styleMatch?.[1] ?? "",
    body: bodyContent,
    script: inlineScriptMatch?.[1] ?? "",
  };
}

export default async function VisualizePage() {
  const { style, body, script } = await loadVisualize();

  return (
    <div className="legacy-visualize-root" suppressHydrationWarning>
      <style dangerouslySetInnerHTML={{ __html: style }} suppressHydrationWarning />
      <style
        dangerouslySetInnerHTML={{ __html: LEGACY_VISUALIZE_OVERRIDES }}
        suppressHydrationWarning
      />
      <a href="/" className="visualize-escape-hatch" aria-label="Back to overview">
        ← back to BigBounce
      </a>
      <LegacyVisualizeClient body={body} script={script} />
    </div>
  );
}

const LEGACY_VISUALIZE_OVERRIDES = `
/* The legacy visualize.html ships its own body { overflow: hidden } and
   position:fixed sidebar, which fights the shell layout. Counteract that
   so the BigBounce sidebar + topbar remain reachable. */
html, body { overflow: auto !important; height: auto !important; }
.legacy-visualize-root .container,
.legacy-visualize-root .wide-container {
  max-width: none !important;
  padding: 0 !important;
  margin: 0 !important;
}
.legacy-visualize-root canvas {
  border-radius: var(--radius) !important;
  border: 1px solid var(--border) !important;
  /* fixed left:0/right:0 + 1px borders = 2px viewport bleed without border-box */
  box-sizing: border-box !important;
  max-width: 100vw !important;
}
.legacy-visualize-root button {
  background: var(--surface) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
}
.legacy-visualize-root button:hover {
  background: color-mix(in srgb, var(--accent) 12%, var(--surface)) !important;
  border-color: var(--accent) !important;
}
.legacy-visualize-root a { color: var(--accent) !important; }
.visualize-escape-hatch {
  position: fixed;
  top: 12px;
  right: 12px;
  z-index: 10000;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: 8px;
  font-family: var(--font-mono-stack);
  font-size: 12px;
  font-weight: 600;
  text-decoration: none;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.18);
}
.visualize-escape-hatch:hover {
  background: color-mix(in srgb, var(--accent) 12%, var(--surface));
  border-color: var(--accent);
}
`;
