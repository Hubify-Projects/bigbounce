import { predictions, getPredictionBySlug } from "@/data/predictions";
import { Badge } from "@/components/Cards/Badge";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";

export function generateStaticParams() {
  return predictions.map((p) => ({ slug: p.slug }));
}

export function generateMetadata({ params }: { params: { slug: string } }): Metadata {
  const pred = getPredictionBySlug(params.slug);
  if (!pred) return { title: "Not Found" };
  return {
    title: pred.name,
    description: `${pred.name}: ${pred.value}. ${pred.status}.`,
  };
}

export default function PredictionPage({ params }: { params: { slug: string } }) {
  const pred = getPredictionBySlug(params.slug);
  if (!pred) notFound();

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link href="/predictions" style={{ color: "var(--text-muted)", textDecoration: "none" }}>
            Predictions
          </Link>{" "}
          &rarr; {pred.name}
        </p>
        <h1>{pred.name}</h1>
        <p className="subtitle">{pred.description}</p>
        <div className="meta">
          <Badge variant={pred.statusVariant}>{pred.status}</Badge>
          <span className="badge badge-accent">{pred.value}</span>
          <span className="badge badge-neutral">{pred.bestModel}</span>
          <span className="badge badge-neutral">{pred.experiment}</span>
        </div>
      </div>

      {/* Current Constraint */}
      <div className="card" style={{ borderLeft: "3px solid #3b82f6", marginBottom: 24 }}>
        <h4 style={{ margin: "0 0 6px", fontSize: 14 }}>Current Constraint</h4>
        <p style={{ margin: 0, fontSize: 13, color: "var(--text-secondary)" }}>
          {pred.currentConstraint}
        </p>
      </div>

      <hr />

      {/* Key Results */}
      <section className="section">
        <h2>Key Results</h2>
        <ul style={{ paddingLeft: 20, fontSize: 14, color: "var(--text-secondary)", lineHeight: 1.8 }}>
          {pred.keyResults.map((result, i) => (
            <li key={i}>{result}</li>
          ))}
        </ul>
      </section>

      {/* Connected Surveys */}
      {pred.surveys.length > 0 && (
        <section className="section">
          <h2>Connected Surveys</h2>
          {pred.surveys.map((survey) => (
            <div key={survey} className="card" style={{ padding: "10px 16px", marginBottom: 8 }}>
              <span style={{ fontSize: 14 }}>{survey}</span>
            </div>
          ))}
        </section>
      )}

      {/* Paper Connections */}
      <section className="section">
        <h2>Paper Connections</h2>
        {pred.papers.map((paper) => (
          <div key={paper} className="card" style={{ padding: "10px 16px", marginBottom: 8 }}>
            <span style={{ fontSize: 14 }}>{paper}</span>
          </div>
        ))}
      </section>

      {/* Timeline */}
      <section className="section">
        <h2>Timeline</h2>
        <p style={{ fontSize: 14, color: "var(--text-secondary)" }}>{pred.timeline}</p>
      </section>

      {/* Next Steps */}
      <section className="section">
        <h2>Next Steps ({pred.nextSteps.length})</h2>
        {pred.nextSteps.map((step, i) => (
          <div
            key={i}
            style={{
              padding: "10px 14px",
              borderBottom: "1px solid var(--border)",
              fontSize: 14,
              color: "var(--text-secondary)",
              display: "flex",
              alignItems: "center",
              gap: 10,
            }}
          >
            <span style={{ width: 8, height: 8, borderRadius: "50%", background: "#f59e0b", flexShrink: 0 }} />
            {step}
          </div>
        ))}
      </section>
    </>
  );
}
