import { papers, getPaperBySlug } from "@/data/papers";
import { Badge } from "@/components/Cards/Badge";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";

export function generateStaticParams() {
  return papers.map((p) => ({ slug: p.slug }));
}

export function generateMetadata({ params }: { params: { slug: string } }): Metadata {
  const paper = getPaperBySlug(params.slug);
  if (!paper) return { title: "Not Found" };
  return {
    title: `Paper ${paper.number}`,
    description: paper.title,
  };
}

export default function PaperDetailPage({ params }: { params: { slug: string } }) {
  const paper = getPaperBySlug(params.slug);
  if (!paper) notFound();

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link href="/paper" style={{ color: "var(--text-muted)", textDecoration: "none" }}>
            Papers
          </Link>{" "}
          &rarr; Paper {paper.number}
        </p>
        <h1>Paper {paper.number}</h1>
        <p className="subtitle">{paper.title}</p>
        <div className="meta">
          <Badge variant={paper.statusVariant}>{paper.status}</Badge>
          <span className="badge badge-accent">{paper.version}</span>
          <span className="badge badge-neutral">{paper.pages} pages</span>
          <span className="badge badge-neutral">{paper.refs} refs</span>
          <span className="badge badge-neutral">Target: {paper.target}</span>
        </div>
      </div>

      {/* Readiness bar */}
      <div style={{ margin: "16px 0 24px", background: "var(--border)", borderRadius: 4, height: 8, overflow: "hidden" }}>
        <div
          style={{
            height: "100%",
            width: `${paper.readiness}%`,
            background: paper.readiness === 100 ? "#22c55e" : paper.readiness >= 90 ? "#3b82f6" : "#f59e0b",
            borderRadius: 4,
            transition: "width 0.3s",
          }}
        />
      </div>

      <p style={{ fontSize: 14, color: "var(--text-secondary)" }}>{paper.description}</p>

      <hr />

      <section className="section">
        <h2>Key Results</h2>
        <ul style={{ paddingLeft: 20, fontSize: 14, color: "var(--text-secondary)", lineHeight: 1.8 }}>
          {paper.keyResults.map((r, i) => (
            <li key={i}>{r}</li>
          ))}
        </ul>
      </section>

      {paper.surveys.length > 0 && (
        <section className="section">
          <h2>Connected Surveys</h2>
          {paper.surveys.map((s) => (
            <div key={s} className="card" style={{ padding: "10px 16px", marginBottom: 8 }}>
              <span style={{ fontSize: 14 }}>{s}</span>
            </div>
          ))}
        </section>
      )}

      <section className="section">
        <h2>Predictions Tested</h2>
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          {paper.predictions.map((p) => (
            <span key={p} className="badge badge-blue" style={{ fontSize: 13, padding: "4px 12px" }}>
              {p}
            </span>
          ))}
        </div>
      </section>

      {paper.figures.length > 0 && (
        <section className="section">
          <h2>Figures</h2>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
            {paper.figures.map((f) => (
              <span key={f} className="badge badge-neutral" style={{ fontSize: 12 }}>
                {f}
              </span>
            ))}
          </div>
        </section>
      )}

      {paper.remainingWork.length > 0 && (
        <section className="section">
          <h2>Remaining Work ({paper.remainingWork.length})</h2>
          {paper.remainingWork.map((task, i) => (
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
              <span style={{ width: 8, height: 8, borderRadius: "50%", background: task.startsWith("TIER 1") ? "#ef4444" : "#f59e0b", flexShrink: 0 }} />
              {task}
            </div>
          ))}
        </section>
      )}
    </>
  );
}
