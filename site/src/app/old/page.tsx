import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Old BigBounce Site",
  description: "Legacy static BigBounce site archive.",
};

export default function OldSiteRedirectPage() {
  return (
    <main className="container">
      <meta httpEquiv="refresh" content="0; url=/old/index.html" />
      <div className="hero">
        <p className="text-xs sans">Legacy Archive</p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          Old BigBounce Site
        </h1>
        <p className="subtitle">
          Redirecting to the archived static site.
        </p>
        <p>
          <a href="/old/index.html">Open the old site archive</a>
        </p>
      </div>
    </main>
  );
}
