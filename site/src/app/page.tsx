import { surveys } from "@/data/surveys";
import { predictions } from "@/data/predictions";
import { papers } from "@/data/papers";
import { StatCard } from "@/components/Cards/StatCard";
import { Badge } from "@/components/Cards/Badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import Link from "next/link";

const totalAnomalies = surveys.reduce((s, sv) => s + sv.anomalies, 0);
const qcPassCount = surveys.filter((s) => s.qcStatus === "pass").length;

export default function HomePage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Program &middot; Updated April 2026
        </p>
        <h1>Spin-Torsion Cosmology</h1>
        <p className="subtitle">
          Proving bounce cosmology beats inflation through systematic AI-powered
          archival mining and precision cosmological tests. 4 papers, 8 surveys,
          33.5M sources scored.
        </p>
      </div>

      {/* Stats grid */}
      <div className="grid grid-4" style={{ margin: "20px 0 32px" }}>
        <StatCard value="4" label="Papers" />
        <StatCard value={`${surveys.length}`} label="Surveys" color="blue" />
        <StatCard value="33.5M+" label="Sources Scored" />
        <StatCard value={`${(totalAnomalies / 1000).toFixed(0)}K+`} label="Anomalies" />
        <StatCard value="475K+" label="MCMC Samples" />
        <StatCard value={`${qcPassCount}/${surveys.length}`} label="QC Pass" color={qcPassCount === surveys.length ? "green" : "amber"} />
        <StatCard value="4" label="Predictions" color="blue" />
        <StatCard value="50" label="Queued Experiments" color="amber" />
      </div>

      <hr />

      {/* Predictions — the science */}
      <section className="section">
        <h2>
          <Link href="/predictions" style={{ textDecoration: "none", color: "inherit" }}>
            Testable Predictions &rarr;
          </Link>
        </h2>
        <div className="grid grid-2">
          {predictions.map((pred) => (
            <Link key={pred.slug} href={`/predictions/${pred.slug}`} style={{ textDecoration: "none", color: "inherit" }}>
              <div className="card" style={{ cursor: "pointer", height: "100%" }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                  <h3 style={{ margin: 0, fontSize: 14 }}>{pred.name}</h3>
                  <Badge variant={pred.statusVariant}>{pred.status}</Badge>
                </div>
                <div style={{ fontSize: 20, fontWeight: 700, fontFamily: "var(--font-mono-stack)", marginBottom: 6, color: "var(--text)" }}>
                  {pred.value}
                </div>
                <p style={{ margin: 0, fontSize: 12, color: "var(--text-tertiary)" }}>
                  {pred.bestModel} &middot; {pred.experiment}
                </p>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Surveys — the data */}
      <section className="section">
        <h2>
          <Link href="/surveys" style={{ textDecoration: "none", color: "inherit" }}>
            Survey Results &rarr;
          </Link>
        </h2>
        <table>
          <thead>
            <tr>
              <th>Survey</th>
              <th>Sources</th>
              <th>Anomalies</th>
              <th>QC</th>
            </tr>
          </thead>
          <tbody>
            {surveys.map((survey) => (
              <tr key={survey.slug}>
                <td>
                  <Link href={`/surveys/${survey.slug}`} style={{ fontWeight: 600 }}>
                    {survey.name}
                  </Link>
                </td>
                <td>{survey.sources}</td>
                <td>{survey.anomalies.toLocaleString()} ({survey.anomalyRate})</td>
                <td>
                  <Badge variant={survey.qcStatus === "pass" ? "green" : survey.qcStatus === "caution" ? "amber" : "red"}>
                    {survey.qcStatus === "pass" ? "PASS" : survey.qcStatus === "caution" ? "CAUTION" : survey.qcStatus === "fail" ? "FAIL" : "EXPAND"}
                  </Badge>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      {/* Papers — the output */}
      <section className="section">
        <h2>
          <Link href="/paper" style={{ textDecoration: "none", color: "inherit" }}>
            Research Papers &rarr;
          </Link>
        </h2>
        {papers.map((paper) => (
          <Link key={paper.slug} href={`/papers/${paper.slug}`} style={{ textDecoration: "none", color: "inherit", display: "block" }}>
            <div style={{ display: "flex", alignItems: "center", gap: 12, padding: "10px 0", borderBottom: "1px solid var(--border)", cursor: "pointer" }}>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 14, fontWeight: 600 }}>Paper {paper.number}</div>
                <div style={{ fontSize: 12, color: "var(--text-tertiary)" }}>
                  {paper.title.slice(0, 80)}...
                </div>
              </div>
              <div style={{ width: 80, background: "var(--border)", borderRadius: 4, height: 6, overflow: "hidden" }}>
                <div style={{ height: "100%", width: `${paper.readiness}%`, background: paper.readiness === 100 ? "#22c55e" : "#3b82f6", borderRadius: 4 }} />
              </div>
              <Badge variant={paper.statusVariant}>{paper.readiness}%</Badge>
            </div>
          </Link>
        ))}
      </section>

      {/* Current Focus — shadcn smoke test */}
      <section className="section">
        <h2>Current Focus</h2>
        <Card className="border-l-4 border-l-[#1e40af]">
          <CardHeader>
            <CardTitle className="text-[11px] uppercase tracking-wider font-bold text-[#1e40af]">
              H200 Queue v2 — Phase 2 Running
            </CardTitle>
            <CardDescription className="text-sm">
              5/6 Phase 1 re-runs QC PASS (Planck, ACT, NEOWISE, Gaia, Taxonomy).
              Phase 2 validation in progress. 50 total experiments across 10 phases.
              Auto-backup every 20min. Est. ~$1,768 total.
            </CardDescription>
          </CardHeader>
          <CardFooter className="flex gap-2 flex-wrap pt-0">
            <Button asChild size="sm" variant="outline">
              <Link href="/activity">Activity Feed &rarr;</Link>
            </Button>
            <Button asChild size="sm" variant="outline">
              <Link href="/status">Full Status &rarr;</Link>
            </Button>
          </CardFooter>
        </Card>
      </section>

      {/* Quick links */}
      <section className="section">
        <h2>Explore</h2>
        <div className="grid grid-3">
          <Link href="/explained" style={{ textDecoration: "none", color: "inherit" }}>
            <div className="card" style={{ cursor: "pointer", textAlign: "center" }}>
              <h3 style={{ margin: "0 0 4px" }}>Explainer</h3>
              <p style={{ margin: 0, fontSize: 12, color: "var(--text-tertiary)" }}>Non-technical guide</p>
            </div>
          </Link>
          <Link href="/glossary" style={{ textDecoration: "none", color: "inherit" }}>
            <div className="card" style={{ cursor: "pointer", textAlign: "center" }}>
              <h3 style={{ margin: "0 0 4px" }}>Glossary</h3>
              <p style={{ margin: 0, fontSize: 12, color: "var(--text-tertiary)" }}>Key terms &amp; equations</p>
            </div>
          </Link>
          <Link href="/timeline" style={{ textDecoration: "none", color: "inherit" }}>
            <div className="card" style={{ cursor: "pointer", textAlign: "center" }}>
              <h3 style={{ margin: "0 0 4px" }}>Timeline</h3>
              <p style={{ margin: 0, fontSize: 12, color: "var(--text-tertiary)" }}>Cosmic history &rarr; 2028</p>
            </div>
          </Link>
          <Link href="/speculations" style={{ textDecoration: "none", color: "inherit" }}>
            <div className="card" style={{ cursor: "pointer", textAlign: "center" }}>
              <h3 style={{ margin: "0 0 4px" }}>Speculations</h3>
              <p style={{ margin: 0, fontSize: 12, color: "var(--text-tertiary)" }}>Future research paths</p>
            </div>
          </Link>
          <a href="https://github.com/Hubify-Projects/bigbounce" target="_blank" rel="noopener" style={{ textDecoration: "none", color: "inherit" }}>
            <div className="card" style={{ cursor: "pointer", textAlign: "center" }}>
              <h3 style={{ margin: "0 0 4px" }}>GitHub</h3>
              <p style={{ margin: 0, fontSize: 12, color: "var(--text-tertiary)" }}>Source code &amp; data</p>
            </div>
          </a>
          <a href="mailto:houston@hubify.com" style={{ textDecoration: "none", color: "inherit" }}>
            <div className="card" style={{ cursor: "pointer", textAlign: "center" }}>
              <h3 style={{ margin: "0 0 4px" }}>Contact</h3>
              <p style={{ margin: 0, fontSize: 12, color: "var(--text-tertiary)" }}>houston@hubify.com</p>
            </div>
          </a>
        </div>
      </section>
    </>
  );
}
