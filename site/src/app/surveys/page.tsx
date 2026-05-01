import { surveys } from"@/data/surveys";
import { Badge } from"@/components/ui/badge";
import { Button } from"@/components/ui/button";
import { MathText } from"@/components/MathText";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import Link from"next/link";
import type { Metadata } from"next";

export const metadata: Metadata = {
  title:"Surveys",
  description:
"All astronomical surveys processed by the BigBounce anomaly detection pipeline.",
};

const qcVariantMap: Record<
"pass" |"caution" |"fail" |"needs-expansion",
  { variant:"default" |"secondary" |"destructive" |"outline"; label: string }
> = {
  pass: { variant:"default", label:"QC PASS" },
  caution: { variant:"outline", label:"QC CAUTION" },
  fail: { variant:"destructive", label:"QC FAIL" },
"needs-expansion": { variant:"outline", label:"NEEDS EXPANSION" },
};

export default function SurveysIndexPage() {
  const totalSources = surveys.reduce((sum, s) => {
    const n = parseFloat(s.sources.replace(/[^\d.]/g,""));
    const mult = s.sources.includes("M") ? 1e6 : s.sources.includes("K") ? 1e3 : 1;
    return sum + n * mult;
  }, 0);
  const totalAnomalies = surveys.reduce((sum, s) => sum + s.anomalies, 0);
  const passCount = surveys.filter((survey) => survey.qcStatus === "pass").length;

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
          Every astronomical survey processed by our AI anomaly detection
          pipeline. Each survey page shows its anomalies, figures, paper
          connections, and follow-up tasks.
        </p>
        <div className="insight-strip">
          <div className="insight">
            <div className="insight-label">Sources scored</div>
            <div className="insight-value">{(totalSources / 1e6).toFixed(1)}M</div>
          </div>
          <div className="insight">
            <div className="insight-label">Retained anomalies</div>
            <div className="insight-value">{totalAnomalies.toLocaleString()}</div>
          </div>
          <div className="insight">
            <div className="insight-label">QC pass</div>
            <div className="insight-value">{passCount}/{surveys.length}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Coverage</div>
            <div className="insight-value">8 surveys</div>
          </div>
        </div>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>All Surveys</h2>
        <div className="grid gap-4 md:grid-cols-2">
          {surveys.map((survey) => {
            const qc = qcVariantMap[survey.qcStatus];
            const wavelength = survey.wavelength.split(" ")[0].replace(/[(),]/g, "");
            return (
              <Card
                key={survey.slug}
                className={`index-card flex flex-col ${survey.qcStatus === "pass" ? "index-card-primary" : ""}`}
              >
                <CardHeader className="pb-3">
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <div className="card-kicker">{survey.pipeline}</div>
                      <CardTitle
                        className="mt-1 text-base"
                        style={{ fontFamily:"var(--font-mono-stack)" }}
                      >
                        {survey.name}
                      </CardTitle>
                    </div>
                    <Badge variant={qc.variant}>{qc.label}</Badge>
                  </div>
                  <CardDescription className="font-mono text-sm leading-relaxed">
                    {survey.sources} &rarr;{""}
                    {survey.anomalies.toLocaleString()} anomalies (
                    {survey.anomalyRate})
                  </CardDescription>
                </CardHeader>
                <CardContent className="flex-1">
                  <p className="text-sm text-muted-foreground">
                    <MathText>{survey.description.slice(0, 180)}</MathText>
                    {survey.description.length > 180 ?"…" :""}
                  </p>
                  <div className="chip-row mt-3 text-xs">
                    <Badge variant="outline">
                      {wavelength}
                    </Badge>
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
    </>
  );
}
