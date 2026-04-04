import { predictions } from "@/data/predictions";
import { Badge } from "@/components/Cards/Badge";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Predictions",
  description: "Testable predictions from the bounce cosmology portfolio.",
};

export default function PredictionsIndexPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Bounce Cosmology Portfolio &middot; {predictions.length} Channels
        </p>
        <h1>Predictions</h1>
        <p className="subtitle">
          Each prediction is a distinct observational channel for testing bounce
          cosmology against inflation. Click any to see connected surveys, papers, and next steps.
        </p>
      </div>

      <hr />

      <section className="section">
        <h2>Observational Channels</h2>
        {predictions.map((pred) => (
          <Link
            key={pred.slug}
            href={`/predictions/${pred.slug}`}
            style={{ textDecoration: "none", color: "inherit", display: "block" }}
          >
            <div className="card" style={{ marginBottom: 12, cursor: "pointer" }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 6 }}>
                <h3 style={{ margin: 0, fontSize: 16 }}>{pred.name}</h3>
                <Badge variant={pred.statusVariant}>{pred.status}</Badge>
              </div>
              <div style={{ fontSize: 18, fontWeight: 700, fontFamily: "var(--font-mono-stack)", marginBottom: 6 }}>
                {pred.value}
              </div>
              <p style={{ margin: "0 0 8px", fontSize: 13, color: "var(--text-secondary)" }}>
                {pred.description.slice(0, 180)}...
              </p>
              <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                <span className="badge badge-neutral">{pred.bestModel}</span>
                <span className="badge badge-accent">{pred.experiment}</span>
                <span className="badge badge-neutral">{pred.nextSteps.length} next steps</span>
              </div>
            </div>
          </Link>
        ))}
      </section>
    </>
  );
}
