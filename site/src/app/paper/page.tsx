import { Badge } from "@/components/Cards/Badge";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Papers",
  description: "Research papers from the BigBounce spin-torsion cosmology program.",
};

const papers = [
  {
    number: 1,
    title: "Spin-Torsion Cosmology: Structural Barriers, Falsifiable Predictions, and the Bounce-Inflation Landscape",
    version: "v2.2.0",
    pages: "~24",
    refs: "63+",
    status: "99% Ready" as const,
    statusVariant: "green" as const,
    target: "Physical Review D",
    description: "14 ECH structural barriers, ALP birefringence prediction (β = 0.27°), f_NL = -35/8, bounce model discrimination table, 424K+ MCMC samples.",
  },
  {
    number: 2,
    title: "f_NL = -35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation",
    version: "v1.3.0",
    pages: "~12",
    refs: "30+",
    status: "Submission-Ready" as const,
    statusVariant: "green" as const,
    target: "Physical Review Letters",
    description: "Parameter-free f_NL prediction, normalization audit (92% confidence), Fisher forecast for SPHEREx, template mismatch quantification.",
  },
  {
    number: 3,
    title: "Multi-Survey Anomaly Catalog: 328K Anomalies from 33.5M Sources Across 8 Surveys",
    version: "v0.5",
    pages: "~18",
    refs: "TBD",
    status: "Draft (~95%)" as const,
    statusVariant: "blue" as const,
    target: "ApJS",
    description: "8 surveys, 328K anomalies, 6.1% f_NL improvement, SPHEREx 4.38σ forecast, taxonomy, cross-survey validation.",
  },
  {
    number: 4,
    title: "Galaxy Chirality at Scale: 8.47M Galaxies Classified, Dipole 0.43σ Null",
    version: "v0.8",
    pages: "~11",
    refs: "TBD",
    status: "Draft (~85%)" as const,
    statusVariant: "blue" as const,
    target: "MNRAS",
    description: "Largest bias-audited chirality catalog (40x prior work). 93.7% accuracy, 8/8 bias tests. Definitively refutes Shamir 3% parity claim.",
  },
];

export default function PaperPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Papers &middot; 4 Papers
        </p>
        <h1>Papers</h1>
        <p className="subtitle">
          Published and in-progress research papers from the BigBounce program.
        </p>
      </div>

      <hr />

      <section className="section">
        <h2>Paper Listing</h2>
        {papers.map((paper) => (
          <div key={paper.number} className="card" style={{ marginBottom: 16 }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 8 }}>
              <h3 style={{ margin: 0, fontSize: 15 }}>
                Paper {paper.number}
              </h3>
              <Badge variant={paper.statusVariant}>{paper.status}</Badge>
            </div>
            <p style={{ margin: "0 0 8px", fontSize: 14, fontWeight: 600, color: "var(--text)" }}>
              {paper.title}
            </p>
            <p style={{ margin: "0 0 8px", fontSize: 13, color: "var(--text-secondary)" }}>
              {paper.description}
            </p>
            <div style={{ display: "flex", gap: 12, fontSize: 12, fontFamily: "var(--font-mono-stack)", color: "var(--text-muted)" }}>
              <span>{paper.version}</span>
              <span>{paper.pages} pages</span>
              <span>{paper.refs} refs</span>
              <span>Target: {paper.target}</span>
            </div>
          </div>
        ))}
      </section>
    </>
  );
}
