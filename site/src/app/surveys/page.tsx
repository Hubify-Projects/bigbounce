import { surveys } from"@/data/surveys";
import { Badge } from"@/components/ui/badge";
import { Button } from"@/components/ui/button";
import { MathText } from"@/components/MathText";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import Link from"next/link";
import type { Metadata } from"next";
import { Activity, Database, Gauge, Telescope } from"lucide-react";

export const metadata: Metadata = {
  title:"Surveys",
  description:
"All astronomical surveys processed by the BigBounce anomaly detection pipeline.",
};

const qcVariantMap: Record<
"pass" |"caution" |"fail" |"needs-expansion",
  {
    variant:"default" |"secondary" |"destructive" |"outline";
    label: string;
  }
> = {
  pass: { variant:"default", label:"QC PASS" },
  caution: { variant:"outline", label:"QC CAUTION" },
  fail: { variant:"destructive", label:"QC FAIL" },
"needs-expansion": { variant:"outline", label:"NEEDS EXPANSION" },
};

function sourceCountValue(sources: string) {
  const n = parseFloat(sources.replace(/[^\d.]/g,""));
  const mult = sources.includes("M") ? 1e6 : sources.includes("K") ? 1e3 : 1;
  return n * mult;
}

export default function SurveysIndexPage() {
  const totalSources = surveys.reduce((sum, s) => sum + sourceCountValue(s.sources), 0);
  const totalAnomalies = surveys.reduce((sum, s) => sum + s.anomalies, 0);
  const passCount = surveys.filter((survey) => survey.qcStatus === "pass").length;
  const groupedSurveys = [
    { title:"Publication-grade", items: surveys.filter((s) => s.qcStatus === "pass") },
    { title:"Use with caveats", items: surveys.filter((s) => s.qcStatus === "caution" || s.qcStatus === "needs-expansion") },
    { title:"Quarantined", items: surveys.filter((s) => s.qcStatus === "fail") },
  ].filter((group) => group.items.length > 0);
  const sortedSurveys = [...surveys].sort(
    (a, b) => sourceCountValue(b.sources) - sourceCountValue(a.sources),
  );

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          {surveys.length} Surveys &middot; {(totalSources / 1e6).toFixed(1)}M
          Sources &middot; {totalAnomalies.toLocaleString()} Anomalies
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Survey Hub
        </h1>
        <p className="subtitle">
          Every astronomical survey processed by the anomaly-detection program,
          organized by publication readiness so catalog-grade results do not sit
          beside quarantined diagnostics without context.
        </p>
        <div className="insight-strip">
          <div className="insight">
            <Database aria-hidden="true" className="insight-icon" />
            <div className="insight-label">Sources scored</div>
            <div className="insight-value">{(totalSources / 1e6).toFixed(1)}M</div>
          </div>
          <div className="insight">
            <Activity aria-hidden="true" className="insight-icon" />
            <div className="insight-label">Retained anomalies</div>
            <div className="insight-value">{totalAnomalies.toLocaleString()}</div>
          </div>
          <div className="insight">
            <Gauge aria-hidden="true" className="insight-icon" />
            <div className="insight-label">QC pass</div>
            <div className="insight-value">{passCount}/{surveys.length}</div>
          </div>
          <div className="insight">
            <Telescope aria-hidden="true" className="insight-icon" />
            <div className="insight-label">Coverage</div>
            <div className="insight-value">8 surveys</div>
          </div>
        </div>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <div className="survey-ledger">
          <div>
            <h2>Survey Readiness</h2>
            <p className="subtitle">
              The cards separate headline catalog inputs from cautionary
              baselines and quarantined experiments.
            </p>
          </div>
          <div className="survey-mini-table">
            {sortedSurveys.map((survey) => {
              const qc = qcVariantMap[survey.qcStatus];
              return (
                <Link
                  key={survey.slug}
                  href={`/surveys/${survey.slug}`}
                  className="survey-mini-row"
                >
                  <span>{survey.shortName}</span>
                  <span>{survey.sources}</span>
                  <Badge variant={qc.variant}>{qc.label}</Badge>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {groupedSurveys.map((group) => (
        <section key={group.title} className="section">
          <div className="section-heading-row">
            <h2>{group.title}</h2>
            <Badge variant="outline">{group.items.length} survey{group.items.length === 1 ? "" : "s"}</Badge>
          </div>
          <div className="survey-card-grid">
          {group.items.map((survey) => {
            const qc = qcVariantMap[survey.qcStatus];
            const wavelength = survey.wavelength.split(" ")[0].replace(/[(),]/g, "");
            return (
              <Card
                key={survey.slug}
                className={`survey-card index-card flex flex-col ${survey.qcStatus === "pass" ? "index-card-primary" : ""}`}
              >
                <CardHeader className="pb-3">
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <div className="card-kicker">{survey.shortName} · {wavelength}</div>
                      <CardTitle
                        className="mt-1 text-base"
                        style={{ fontFamily:"var(--font-mono-stack)" }}
                      >
                        {survey.name}
                      </CardTitle>
                    </div>
                    <Badge variant={qc.variant}>{qc.label}</Badge>
                  </div>
                </CardHeader>
                <CardContent className="flex-1">
                  <div className="survey-metrics">
                    <div>
                      <span>Sources</span>
                      <strong>{survey.sources}</strong>
                    </div>
                    <div>
                      <span>Anomalies</span>
                      <strong>{survey.anomalies.toLocaleString()}</strong>
                    </div>
                    <div>
                      <span>Rate</span>
                      <strong>{survey.anomalyRate}</strong>
                    </div>
                  </div>
                  <p className="text-sm text-muted-foreground">
                    <MathText>{survey.description.slice(0, 180)}</MathText>
                    {survey.description.length > 180 ?"…" :""}
                  </p>
                  <div className="chip-row mt-3 text-xs">
                    {survey.paperRefs.slice(0, 2).map((ref) => (
                      <Badge key={ref} variant="secondary">
                        {ref.split(" —")[0]}
                      </Badge>
                    ))}
                    <Badge variant="outline">
                      {survey.followUpTasks.length} tasks
                    </Badge>
                  </div>
                </CardContent>
                <CardFooter className="pt-0">
                  <Button asChild size="sm" variant="outline">
                    <Link href={`/surveys/${survey.slug}`}>
                      Open survey &rarr;
                    </Link>
                  </Button>
                </CardFooter>
              </Card>
            );
          })}
          </div>
        </section>
      ))}
    </>
  );
}
