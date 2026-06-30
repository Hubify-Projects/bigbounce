import { papers } from"@/data/papers";
import { getLivePapers } from"@/lib/livePapers";
import { PublicationPathCompact } from"@/components/PublicationPath";
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
import { Download, FileText } from"lucide-react";
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

export default async function PaperPage() {
  // SINGLE SOURCE OF TRUTH: readiness comes from Convex (listAllPaperStates via
  // getLivePapers), the SAME source the home dashboard reads — never from static
  // papers.ts — so home and /paper can never show conflicting readiness again.
  const live = await getLivePapers();
  const liveReadiness = new Map(live.map((p) => [p.slug, p.readinessComputed]));
  const livePapers = papers.map((p) => ({
    ...p,
    readiness: liveReadiness.get(p.slug) ?? p.readiness,
  }));
  const averageReadiness = Math.round(
    livePapers.reduce((sum, paper) => sum + paper.readiness, 0) / livePapers.length,
  );
  const submissionReady = livePapers.filter((paper) => paper.readiness >= 95).length;

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
          Pre-print research papers ready for arXiv submission. Click any paper
          for full details, connected surveys, predictions tested, and remaining work.
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
          {livePapers.map((paper) => (
            <Card
              key={paper.slug}
              className={`index-card overflow-hidden ${paper.readiness === 100 ? "index-card-primary" : ""}`}
            >
              <CardHeader className="pb-3">
                <div className="flex flex-wrap items-start justify-between gap-3">
                  <div className="min-w-0 flex-1">
                    <CardDescription className="text-xs uppercase tracking-wider">
                      Paper {paper.number} &middot; {paper.version} &middot; {paper.target}
                    </CardDescription>
                    <CardTitle
                      className="mt-1 text-base break-words"
                      style={{ fontFamily:"var(--font-mono-stack)" }}
                    >
                      <MathText>{paper.title}</MathText>
                    </CardTitle>
                  </div>
                  <Badge
                    variant={statusVariantMap[paper.statusVariant]}
                    className="shrink-0 whitespace-nowrap font-mono"
                  >
                    {paper.readiness}%
                  </Badge>
                </div>
              </CardHeader>
              <CardContent>
                <p className="mb-3 text-sm text-muted-foreground leading-relaxed">
                  <MathText>{paper.tldr}</MathText>
                </p>
                <div className="mb-3 flex items-center gap-3">
                  <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-border">
                    <div
                      className={`h-full rounded-full ${readinessColor(paper.readiness)}`}
                      style={{ width: `${paper.readiness}%` }}
                    />
                  </div>
                  <span className="text-xs font-mono text-muted-foreground shrink-0">
                    {paper.pages} pp &middot; {paper.refs} refs
                  </span>
                </div>
                <PublicationPathCompact paper={paper} />
                {paper.remainingWork.length > 0 && (
                  <div className="mt-3">
                    <div className="text-xs font-mono uppercase tracking-wider text-muted-foreground mb-2">
                      What&apos;s left
                    </div>
                    <ul className="space-y-1.5 text-sm text-muted-foreground">
                      {paper.remainingWork.map((task, i) => (
                        <li key={i} className="flex gap-2 break-words">
                          <span className="text-muted-foreground/60 shrink-0">&bull;</span>
                          <span><MathText>{task}</MathText></span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </CardContent>
              <CardFooter className="flex flex-wrap gap-2">
                {(() => {
                  const pdf = paper.artifacts.find(
                    (a) =>
                      a.kind === "primary" &&
                      a.href.toLowerCase().endsWith(".pdf"),
                  );
                  const dl = paper.artifacts.find(
                    (a) => a.download && a.href.toLowerCase().endsWith(".pdf"),
                  );
                  return (
                    <>
                      {pdf && (
                        <Button asChild size="sm">
                          <a
                            href={pdf.href}
                            target="_blank"
                            rel="noopener noreferrer"
                          >
                            <FileText size={14} />
                            Read PDF
                          </a>
                        </Button>
                      )}
                      {dl && (
                        <Button asChild size="sm" variant="outline">
                          <a href={dl.href} download>
                            <Download size={14} />
                            Download
                          </a>
                        </Button>
                      )}
                      <Button asChild size="sm" variant="outline">
                        <Link href={`/papers/${paper.slug}`}>
                          Details &rarr;
                        </Link>
                      </Button>
                    </>
                  );
                })()}
              </CardFooter>
            </Card>
          ))}
        </div>
      </section>
    </>
  );
}
