import { surveys, getSurveyBySlug } from "@/data/surveys";
import { Badge } from "@/components/Cards/Badge";
import { DiscoveryCard } from "@/components/Cards/DiscoveryCard";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";

export function generateStaticParams() {
  return surveys.map((s) => ({ slug: s.slug }));
}

export function generateMetadata({ params }: { params: { slug: string } }): Metadata {
  const survey = getSurveyBySlug(params.slug);
  if (!survey) return { title: "Not Found" };
  return {
    title: survey.name,
    description: `${survey.name}: ${survey.sources} scored, ${survey.anomalies.toLocaleString()} anomalies found.`,
  };
}

const qcColors = {
  pass: { bg: "#dcfce7", color: "#166534", label: "QC PASS" },
  caution: { bg: "#fef3c7", color: "#92400e", label: "QC CAUTION" },
  fail: { bg: "#fee2e2", color: "#991b1b", label: "QC FAIL" },
  "needs-expansion": { bg: "#fef3c7", color: "#92400e", label: "NEEDS EXPANSION" },
};

export default function SurveyPage({ params }: { params: { slug: string } }) {
  const survey = getSurveyBySlug(params.slug);
  if (!survey) notFound();

  const qc = qcColors[survey.qcStatus];

  return (
    <>
      {/* Hero */}
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link href="/surveys" style={{ color: "var(--text-muted)", textDecoration: "none" }}>
            Surveys
          </Link>{" "}
          &rarr; {survey.shortName}
        </p>
        <h1>{survey.name}</h1>
        <p className="subtitle">{survey.description}</p>
        <div className="meta">
          <span style={{ padding: "4px 12px", borderRadius: 12, fontSize: 12, fontWeight: 700, background: qc.bg, color: qc.color }}>
            {qc.label}
          </span>
          <span className="badge badge-accent">{survey.sources}</span>
          <span className="badge badge-accent">{survey.anomalies.toLocaleString()} anomalies ({survey.anomalyRate})</span>
          <span className="badge badge-neutral">{survey.wavelength}</span>
        </div>
      </div>

      {/* QC Note */}
      <div className="card" style={{ borderLeft: `3px solid ${qc.color}`, marginBottom: 24 }}>
        <p style={{ margin: 0, fontSize: 13 }}>
          <strong>QC Status:</strong> {survey.qcNote}
        </p>
      </div>

      <hr />

      {/* Key Findings */}
      <section className="section">
        <h2>Key Findings</h2>
        <ul style={{ paddingLeft: 20, fontSize: 14, color: "var(--text-secondary)", lineHeight: 1.8 }}>
          {survey.keyFindings.map((finding, i) => (
            <li key={i}>{finding}</li>
          ))}
        </ul>
      </section>

      {/* Top Anomalies */}
      {survey.topAnomalies.length > 0 && (
        <section className="section">
          <h2>Top Anomalies</h2>
          <table>
            <thead>
              <tr>
                <th>Rank</th>
                <th>RA</th>
                <th>Dec</th>
                <th>Score</th>
                <th>Type</th>
              </tr>
            </thead>
            <tbody>
              {survey.topAnomalies.map((a) => (
                <tr key={a.rank}>
                  <td>#{a.rank}</td>
                  <td>{a.ra.toFixed(1)}°</td>
                  <td>{a.dec.toFixed(1)}°</td>
                  <td>{a.score.toFixed(2)}</td>
                  <td>{a.type || "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      {/* Pipeline Details */}
      <section className="section">
        <h2>Pipeline Details</h2>
        <table>
          <tbody>
            <tr><td style={{ fontWeight: 600 }}>Pipeline</td><td>{survey.pipeline}</td></tr>
            <tr><td style={{ fontWeight: 600 }}>Wavelength</td><td>{survey.wavelength}</td></tr>
            <tr><td style={{ fontWeight: 600 }}>Cost</td><td>{survey.cost}</td></tr>
            <tr><td style={{ fontWeight: 600 }}>Runtime</td><td>{survey.runtime}</td></tr>
          </tbody>
        </table>
      </section>

      {/* Paper Connections */}
      <section className="section">
        <h2>Paper Connections</h2>
        {survey.paperRefs.map((ref) => (
          <div key={ref} className="card" style={{ padding: "12px 16px", marginBottom: 8 }}>
            <span style={{ fontSize: 14 }}>{ref}</span>
          </div>
        ))}
      </section>

      {/* Cross-Links */}
      <section className="section">
        <h2>Connected Entities</h2>
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          {survey.connections.map((conn) => (
            <Link key={conn.href} href={conn.href}>
              <span className="badge badge-blue" style={{ cursor: "pointer", fontSize: 13, padding: "4px 12px" }}>
                {conn.label} &rarr;
              </span>
            </Link>
          ))}
        </div>
      </section>

      {/* Follow-Up Tasks */}
      <section className="section">
        <h2>Follow-Up Tasks ({survey.followUpTasks.length})</h2>
        <div style={{ fontSize: 14, color: "var(--text-secondary)" }}>
          {survey.followUpTasks.map((task, i) => (
            <div
              key={i}
              style={{
                padding: "10px 14px",
                borderBottom: "1px solid var(--border)",
                display: "flex",
                alignItems: "center",
                gap: 10,
              }}
            >
              <span style={{ width: 8, height: 8, borderRadius: "50%", background: "#f59e0b", flexShrink: 0 }} />
              {task}
            </div>
          ))}
        </div>
      </section>

      {/* Figures */}
      {survey.figures.length > 0 && (
        <section className="section">
          <h2>Related Figures</h2>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
            {survey.figures.map((fig) => (
              <span key={fig} className="badge badge-neutral" style={{ fontSize: 12 }}>
                {fig}
              </span>
            ))}
          </div>
        </section>
      )}
    </>
  );
}
