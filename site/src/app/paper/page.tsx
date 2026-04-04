import { papers } from "@/data/papers";
import { Badge } from "@/components/Cards/Badge";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Papers",
  description: "Research papers from the BigBounce spin-torsion cosmology program.",
};

export default function PaperPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Papers &middot; {papers.length} Papers
        </p>
        <h1>Papers</h1>
        <p className="subtitle">
          Published and in-progress research papers. Click any paper for full details,
          connected surveys, predictions tested, and remaining work.
        </p>
      </div>

      <hr />

      <section className="section">
        <h2>Paper Listing</h2>
        {papers.map((paper) => (
          <Link
            key={paper.slug}
            href={`/papers/${paper.slug}`}
            style={{ textDecoration: "none", color: "inherit", display: "block" }}
          >
            <div className="card" style={{ marginBottom: 16, cursor: "pointer" }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 8 }}>
                <h3 style={{ margin: 0, fontSize: 15 }}>
                  Paper {paper.number}
                </h3>
                <Badge variant={paper.statusVariant}>{paper.status}</Badge>
              </div>
              <p style={{ margin: "0 0 8px", fontSize: 14, fontWeight: 600, color: "var(--text)" }}>
                {paper.title}
              </p>

              {/* Readiness bar */}
              <div style={{ margin: "8px 0", background: "var(--border)", borderRadius: 4, height: 6, overflow: "hidden" }}>
                <div
                  style={{
                    height: "100%",
                    width: `${paper.readiness}%`,
                    background: paper.readiness === 100 ? "#22c55e" : paper.readiness >= 90 ? "#3b82f6" : "#f59e0b",
                    borderRadius: 4,
                  }}
                />
              </div>

              <p style={{ margin: "0 0 8px", fontSize: 13, color: "var(--text-secondary)" }}>
                {paper.description.slice(0, 200)}...
              </p>
              <div style={{ display: "flex", gap: 12, fontSize: 12, fontFamily: "var(--font-mono-stack)", color: "var(--text-muted)" }}>
                <span>{paper.version}</span>
                <span>{paper.pages} pages</span>
                <span>{paper.refs} refs</span>
                <span>Target: {paper.target}</span>
                {paper.remainingWork.length > 0 && (
                  <span style={{ color: "#f59e0b" }}>{paper.remainingWork.length} tasks remaining</span>
                )}
              </div>
            </div>
          </Link>
        ))}
      </section>
    </>
  );
}
