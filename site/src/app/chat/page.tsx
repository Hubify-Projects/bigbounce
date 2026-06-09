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

      <div
        id="astro-full-chat"
        style={{
          marginTop: 24,
          minHeight: 520,
          border: "1px solid var(--border)",
          borderRadius: "var(--radius)",
          background: "var(--surface)",
        }}
      />
    </>
  );
}
