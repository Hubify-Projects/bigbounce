import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Astro Chat",
  description:
    "Astro — the AI research assistant for the BigBounce spin-torsion cosmology research program. Ask anything about the papers, results, methodology, or science.",
};

export default function ChatPage() {
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          AI research assistant
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          astro
        </h1>
        <p className="subtitle">
          Ask anything about spin-torsion cosmology, the 6-paper portfolio,
          MCMC verification, anomaly surveys, the chirality catalog, or the
          14 structural barriers. Astro grounds answers in the published research.
        </p>
      </div>

      {/* Honest offline state (2026-07-22 audit): the chat backend is not
          deployed with this static site, so the previous live-input mount was
          dead UI. Re-enable the #astro-full-chat mount + layout script only
          together with a working /api/chat backend. */}
      <div
        style={{
          marginTop: 24,
          padding: "32px 28px",
          border: "1px solid var(--border)",
          borderRadius: "var(--radius)",
          background: "var(--surface)",
        }}
      >
        <p style={{ margin: 0, fontWeight: 600 }}>
          Astro is temporarily offline.
        </p>
        <p style={{ marginTop: 8, color: "var(--text-secondary)" }}>
          The chat backend is not deployed with this static release. Every
          answer Astro would give is grounded in the published materials, which
          are all here: start with the{" "}
          <a href="/explained">plain-language explainer</a>, the{" "}
          <a href="/papers">six papers</a>, or the{" "}
          <a href="/reviews">open review record</a>. Questions are welcome at{" "}
          <a href="mailto:houston@hubify.com">houston@hubify.com</a>.
        </p>
      </div>
    </>
  );
}
