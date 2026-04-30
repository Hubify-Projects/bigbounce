import { surveys } from "@/data/surveys";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Surveys",
  description:
    "All astronomical surveys processed by the BigBounce anomaly detection pipeline.",
};

const qcVariantMap: Record<
  "pass" | "caution" | "fail" | "needs-expansion",
  { variant: "default" | "secondary" | "destructive" | "outline"; label: string }
> = {
  pass: { variant: "default", label: "QC PASS" },
  caution: { variant: "outline", label: "QC CAUTION" },
  fail: { variant: "destructive", label: "QC FAIL" },
  "needs-expansion": { variant: "outline", label: "NEEDS EXPANSION" },
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
          {surveys.length} Surveys &middot; {(totalSources / 1e6).toFixed(1)}M
          Sources &middot; {totalAnomalies.toLocaleString()} Anomalies
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          Survey Hub
        </h1>
        <p className="subtitle">
          Every astronomical survey processed by our AI anomaly detection
          pipeline. Each survey page shows its anomalies, figures, paper
          connections, and follow-up tasks.
        </p>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>All Surveys</h2>
        <div className="grid gap-4 md:grid-cols-2">
          {surveys.map((survey) => {
            const qc = qcVariantMap[survey.qcStatus];
            return (
              <Card key={survey.slug} className="flex flex-col">
                <CardHeader className="pb-3">
                  <div className="flex items-start justify-between gap-3">
                    <CardTitle
                      className="text-base"
                      style={{ fontFamily: "var(--font-serif)" }}
                    >
                      {survey.name}
                    </CardTitle>
                    <Badge variant={qc.variant}>{qc.label}</Badge>
                  </div>
                  <CardDescription className="font-mono text-sm">
                    {survey.sources} &rarr;{" "}
                    {survey.anomalies.toLocaleString()} anomalies (
                    {survey.anomalyRate})
                  </CardDescription>
                </CardHeader>
                <CardContent className="flex-1">
                  <p className="text-sm text-muted-foreground">
                    {survey.description.slice(0, 180)}
                    {survey.description.length > 180 ? "…" : ""}
                  </p>
                  <div className="mt-3 flex flex-wrap gap-2 text-xs">
                    <Badge variant="outline">
                      {survey.wavelength.split(" ")[0]}
                    </Badge>
                    {survey.paperRefs.slice(0, 2).map((ref) => (
                      <Badge key={ref} variant="secondary">
                        {ref.split(" — ")[0]}
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
