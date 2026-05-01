import { papers } from"@/data/papers";
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
  title:"Papers",
  description:
"Research papers from the BigBounce spin-torsion cosmology program.",
};

const statusVariantMap: Record<
  string,
"default" |"secondary" |"destructive" |"outline"
> = {
  green:"default",
  blue:"secondary",
  amber:"outline",
  red:"destructive",
};

function readinessColor(pct: number) {
  if (pct === 100) return"progress-fill-success";
  if (pct >= 90) return"progress-fill-near";
  return"progress-fill-caution";
}

export default function PaperPage() {
  const averageReadiness = Math.round(
    papers.reduce((sum, paper) => sum + paper.readiness, 0) / papers.length,
  );
  const submissionReady = papers.filter((paper) => paper.readiness >= 95).length;

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Papers &middot; {papers.length} Papers
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Papers
        </h1>
        <p className="subtitle">
          Published and in-progress research papers. Click any paper for full
          details, connected surveys, predictions tested, and remaining work.
        </p>
        <div className="insight-strip">
          <div className="insight">
            <div className="insight-label">Program papers</div>
            <div className="insight-value">{papers.length}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Average readiness</div>
            <div className="insight-value">{averageReadiness}%</div>
          </div>
          <div className="insight">
            <div className="insight-label">Near submission</div>
            <div className="insight-value">{submissionReady}</div>
          </div>
          <div className="insight">
            <div className="insight-label">Target journals</div>
            <div className="insight-value">PRD / PRL / ApJS</div>
          </div>
        </div>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>Paper Listing</h2>
        <div className="flex flex-col gap-4">
          {papers.map((paper) => (
            <Card
              key={paper.slug}
              className={`index-card ${paper.readiness === 100 ? "index-card-primary" : ""}`}
            >
              <CardHeader className="pb-3">
                <div className="flex items-start justify-between gap-4">
                  <div>
                    <CardDescription className="text-xs uppercase tracking-wider">
                      Paper {paper.number} &middot; {paper.version}
                    </CardDescription>
                    <CardTitle
                      className="mt-1 text-base"
                      style={{ fontFamily:"var(--font-mono-stack)" }}
                    >
                      <MathText>{paper.title}</MathText>
                    </CardTitle>
                  </div>
                  <Badge variant={statusVariantMap[paper.statusVariant]}>
                    {paper.status}
                  </Badge>
                </div>
              </CardHeader>
              <CardContent>
                <div className="mb-3 flex items-center gap-3">
                  <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-border">
                    <div
                      className={`h-full rounded-full ${readinessColor(paper.readiness)}`}
                      style={{ width: `${paper.readiness}%` }}
                    />
                  </div>
                  <span className="text-xs font-mono text-muted-foreground">
                    {paper.readiness}%
                  </span>
                </div>
                <p className="text-sm text-muted-foreground">
                  <MathText>{paper.description}</MathText>
                </p>
                <div className="mt-3 flex flex-wrap gap-3 text-xs font-mono text-muted-foreground">
                  <span>{paper.pages} pages</span>
                  <span>{paper.refs} refs</span>
                  <span>Target: {paper.target}</span>
                  {paper.remainingWork.length > 0 && (
                    <span className="tone-caution">
                      {paper.remainingWork.length} tasks remaining
                    </span>
                  )}
                </div>
              </CardContent>
              <CardFooter>
                <Button asChild size="sm" variant="outline">
                  <Link href={`/papers/${paper.slug}`}>Open paper &rarr;</Link>
                </Button>
              </CardFooter>
            </Card>
          ))}
        </div>
      </section>
    </>
  );
}
