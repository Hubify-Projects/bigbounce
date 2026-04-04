import { surveys } from "@/data/surveys";
import { Badge } from "@/components/Cards/Badge";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Surveys",
  description: "All astronomical surveys processed by the BigBounce anomaly detection pipeline.",
};

const qcBadge = {
  pass: { variant: "green" as const, label: "QC PASS" },
  caution: { variant: "amber" as const, label: "QC CAUTION" },
  fail: { variant: "red" as const, label: "QC FAIL" },
  "needs-expansion": { variant: "amber" as const, label: "NEEDS EXPANSION" },
};

export default function SurveysIndexPage() {
  const totalSources = surveys.reduce((sum, s) => {
    const n = parseFloat(s.sources.replace(/[^\d.]/g, ""));
    const mult = s.sources.includes("M") ? 1e6 : s.sources.includes("K") ? 1e3 : 1;
    return sum + n * mult;
  }, 0);
  const totalAnomalies = surveys.reduce((sum, s) => sum + s.anomalies, 0);

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          {surveys.length} Surveys &middot; {(totalSources / 1e6).toFixed(1)}M Sources &middot;{" "}
          {totalAnomalies.toLocaleString()} Anomalies
        </p>
        <h1>Survey Hub</h1>
        <p className="subtitle">
          Every astronomical survey processed by our AI anomaly detection pipeline.
          Each survey page shows its anomalies, figures, data, paper connections, and follow-up tasks.
        </p>
      </div>

      <hr />

      <section className="section">
        <h2>All Surveys</h2>
        {surveys.map((survey) => {
          const badge = qcBadge[survey.qcStatus];
          return (
            <Link
              key={survey.slug}
              href={`/surveys/${survey.slug}`}
              style={{ textDecoration: "none", color: "inherit", display: "block" }}
            >
              <div className="card" style={{ marginBottom: 12, cursor: "pointer" }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
                  <div>
                    <h3 style={{ margin: "0 0 4px", fontSize: 16 }}>{survey.name}</h3>
                    <div style={{ fontSize: 13, color: "var(--text-secondary)", marginBottom: 6 }}>
                      {survey.sources} &rarr; {survey.anomalies.toLocaleString()} anomalies ({survey.anomalyRate})
                    </div>
                  </div>
                  <Badge variant={badge.variant}>{badge.label}</Badge>
                </div>
                <p style={{ margin: "0 0 8px", fontSize: 13, color: "var(--text-tertiary)" }}>
                  {survey.description.slice(0, 150)}...
                </p>
                <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                  <span className="badge badge-neutral">{survey.wavelength.split(" ")[0]}</span>
                  {survey.paperRefs.slice(0, 2).map((ref) => (
                    <span key={ref} className="badge badge-accent">{ref.split(" — ")[0]}</span>
                  ))}
                  <span className="badge badge-neutral">{survey.followUpTasks.length} tasks pending</span>
                </div>
              </div>
            </Link>
          );
        })}
      </section>
    </>
  );
}
