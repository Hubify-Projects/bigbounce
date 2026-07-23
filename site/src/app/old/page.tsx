import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Legacy site archive — BigBounce",
  description:
    "Archived first-generation static site for the BigBounce research program, preserved as-is for provenance.",
};

// NOTE: this page must NOT redirect to /old/index.html — with cleanUrls enabled
// the host 308s /old/index.html back to /old, which made the old redirect() an
// infinite loop (2026-07-22 site audit, lane C). Render a lander instead.
export default function OldSiteArchivePage() {
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Legacy archive
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          First-generation site, preserved as-is
        </h1>
        <p className="subtitle">
          This is the original static site for the research program, kept
          unmodified for provenance. Numbers and versions on archived pages
          reflect the state of the program when they were written — the current
          site is always the source of truth.
        </p>
      </div>
      <p style={{ marginTop: 20 }}>
        <a href="/old/index.html">Enter the legacy archive &rarr;</a>
      </p>
      <p style={{ marginTop: 8 }}>
        <a href="/">&larr; Back to the current site</a>
      </p>
    </>
  );
}
