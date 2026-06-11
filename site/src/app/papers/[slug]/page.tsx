import { papers, getPaperBySlug } from"@/data/papers";
import {
  getLivePapers,
  getNotablesForPaper,
  getFiguresForPaper,
} from"@/lib/livePapers";
import { sortedReviewRounds, type PaperId } from"@/data/reviewTimeline";
import { PaperFigureGallery } from"./PaperFigureGallery";
import { Badge } from"@/components/ui/badge";
import { Button } from"@/components/ui/button";
import { MathText } from"@/components/MathText";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
} from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import {
  Tabs,
  TabsList,
  TabsTrigger,
  TabsContent,
} from"@/components/ui/tabs";
import { Alert, AlertTitle, AlertDescription } from"@/components/ui/alert";
import { ExternalReviewPanel } from"@/components/ExternalReviewPanel";
import { PublicationPath } from"@/components/PublicationPath";
import { Download, ExternalLink, FileText } from"lucide-react";
import Link from"next/link";
import { notFound } from"next/navigation";
import type { Metadata } from"next";

export function generateStaticParams() {
  return papers.map((p) => ({ slug: p.slug }));
}

type PageParams = Promise<{ slug: string }>;

export async function generateMetadata({
  params,
}: {
  params: PageParams;
}): Promise<Metadata> {
  const { slug } = await params;
  const paper = getPaperBySlug(slug);
  if (!paper) return { title:"Not Found" };
  return {
    title: `Paper ${paper.number}`,
    description: paper.title,
  };
}

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

export default async function PaperDetailPage({
  params,
}: {
  params: PageParams;
}) {
  const { slug } = await params;
  const paper = getPaperBySlug(slug);
  if (!paper) notFound();

  // Single source of truth for paper-level numeric state: Convex via getLivePapers.
  // The static papers.ts retains descriptive content (title, tldr, path,
  // figures, artifacts) but readiness + version + lastUpdated come from Convex so
  // they can never drift relative to the homepage dashboard.
  const [liveStates, notables, figures] = await Promise.all([
    getLivePapers(),
    getNotablesForPaper(slug),
    getFiguresForPaper(slug),
  ]);
  // Review history — single-sourced from data/reviewTimeline.ts (same source
  // as /reviews) so the per-paper list can never go stale relative to the
  // timeline. Previously a separate Convex externalReviews table drifted.
  const SLUG_TO_PAPER_ID: Record<string, PaperId> = {
    "paper-1a": "P1A",
    "paper-1b": "P1B",
    "paper-2": "P2",
    "paper-3": "P3",
    "paper-4": "P4",
    "paper-5": "P5",
  };
  const paperId = SLUG_TO_PAPER_ID[slug];
  const paperRounds = paperId
    ? sortedReviewRounds().filter((r) => r.papers.includes(paperId))
    : [];
  const recentRounds = paperRounds.slice(0, 6);
  const inPaperFigures = figures.filter((f) => (f.status ?? "in-paper") === "in-paper");
  const candidateFigures = figures.filter((f) => f.status === "candidate");
  const live = liveStates.find((p) => p.slug === slug);
  const readiness = live?.readinessComputed ?? paper.readiness;
  const version = live?.currentVersion ?? paper.version;
  const lastUpdated = live?.lastUpdated ?? paper.lastUpdated;
  const liveStatus = live?.status ?? null;
  const openSummary = live
    ? `${live.openBlockers}B/${live.openMajors}M/${live.openMinors}m/${live.openCaveats}C open`
    : null;
  const liveSource = live?.source ?? "static-fallback";

  const staticVariant = paper.statusVariant;
  function statusLabel(s: string | null): string {
    switch (s) {
      case "active-drive-to-100":
        return "active";
      case "paused-houston-external":
        return "paused (houston review)";
      case "submitted-arxiv":
        return "submitted to arXiv";
      case "in-revision":
        return "in revision";
      case "accepted":
        return "accepted";
      default:
        return staticVariant === "green"
          ? "ready"
          : staticVariant === "blue"
            ? "active"
            : staticVariant === "amber"
              ? "draft"
              : "blocked";
    }
  }

  const livePdfHref = live?.sitePdfPath ?? null;
  // Canonical focus bullets + novelty tier from Convex (Gap #4 + Gap #2).
  // Falls back to empty array when running on the static path so the page
  // still renders. Houston picks the novelty tier per-paper via the
  // papers:setNovelty mutation — null means "not yet assigned".
  const focusAreas = live?.focusAreas ?? [];
  const novelty = live?.novelty ?? null;
  const pdfArtifactRaw = paper.artifacts.find(
    (a) => a.kind === "primary" && a.href.toLowerCase().endsWith(".pdf"),
  );
  const downloadArtifactRaw = paper.artifacts.find(
    (a) => a.download && a.href.toLowerCase().endsWith(".pdf"),
  );
  // Override static artifact hrefs with live Convex sitePdfPath (versioned, CDN-fresh URL)
  const pdfArtifact = pdfArtifactRaw && livePdfHref
    ? { ...pdfArtifactRaw, href: livePdfHref }
    : pdfArtifactRaw;
  const downloadArtifact = downloadArtifactRaw && livePdfHref
    ? { ...downloadArtifactRaw, href: livePdfHref }
    : downloadArtifactRaw;
  const supplementaryArtifacts = paper.artifacts.filter(
    (a) => a !== pdfArtifactRaw && a !== downloadArtifactRaw,
  );

  return (
    <>
      <div className="paper-detail-hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link
            href="/paper"
            style={{ color:"var(--text-muted)", textDecoration:"none" }}
          >
            Papers
          </Link>{""}
          &rarr; Paper {paper.number}
        </p>
        <div className="paper-detail-grid grid gap-5 lg:grid-cols-[minmax(0,1fr)_360px]">
          <div className="paper-detail-copy">
            <div className="paper-detail-kicker flex flex-wrap gap-2">
              <span>Paper {paper.number}</span>
              <span>{paper.preprintId}</span>
              <span>{paper.pages} pages</span>
              <span>{paper.refs} refs</span>
              <span>Target: {paper.target}</span>
            </div>
            <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
              Paper {paper.number}
            </h1>
            <p className="subtitle"><MathText>{paper.title}</MathText></p>
            <div className="mt-4 flex flex-wrap items-center gap-2">
              <Badge variant={statusVariantMap[paper.statusVariant]}>
                {readiness}% · {statusLabel(liveStatus)}
              </Badge>
              <Badge variant="outline">{version}</Badge>
              {liveSource === "convex" && (
                <Badge
                  variant="outline"
                  title="readiness + version live from Convex (computed from open findings + caveats)"
                  style={{
                    borderColor: "color-mix(in srgb, var(--success) 45%, transparent)",
                    color: "var(--success)",
                  }}
                >
                  ● live
                </Badge>
              )}
              {openSummary && (
                <Badge
                  variant="outline"
                  title="Open: BLOCKERs / MAJORs / minors / Caveats"
                >
                  {openSummary}
                </Badge>
              )}
            </div>
            <p style={{ marginTop: 14, fontSize: "0.92rem", color: "var(--text-muted)", lineHeight: 1.55 }}>
              {paper.tldr}
            </p>
            {(pdfArtifact || downloadArtifact) && (
              <div className="mt-4 flex flex-wrap gap-2">
                {pdfArtifact && (
                  <Button asChild size="default">
                    <a
                      href={pdfArtifact.href}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <FileText size={16} />
                      Read PDF
                    </a>
                  </Button>
                )}
                {downloadArtifact && (
                  <Button asChild size="default" variant="outline">
                    <a href={downloadArtifact.href} download>
                      <Download size={16} />
                      Download PDF
                    </a>
                  </Button>
                )}
              </div>
            )}
          </div>
          <Card className="paper-artifact-card">
            <CardHeader>
              <CardTitle className="text-sm">Paper Artifacts</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="paper-artifact-meta">
                <span>{paper.pdfMeta}</span>
                <span>{paper.target}</span>
              </div>
              <div className="paper-artifact-actions flex flex-wrap gap-2">
                {pdfArtifact && (
                  <Button asChild size="sm">
                    <a
                      href={pdfArtifact.href}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <FileText size={14} />
                      {pdfArtifact.label}
                    </a>
                  </Button>
                )}
                {downloadArtifact && (
                  <Button asChild size="sm" variant="outline">
                    <a href={downloadArtifact.href} download>
                      <Download size={14} />
                      {downloadArtifact.label}
                    </a>
                  </Button>
                )}
                {supplementaryArtifacts.map((artifact) => (
                  <Button
                    key={`${artifact.href}-${artifact.label}`}
                    asChild
                    size="sm"
                    variant="outline"
                  >
                    <a
                      href={artifact.href}
                      target={artifact.external ? "_blank" : undefined}
                      rel={artifact.external ? "noopener noreferrer" : undefined}
                      download={artifact.download ? true : undefined}
                    >
                      {artifact.label}
                      {artifact.external && <ExternalLink size={12} />}
                    </a>
                  </Button>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      <div className="paper-readiness grid gap-2">
        <div className="paper-readiness-head flex items-baseline justify-between gap-3">
          <span>
            Readiness
            {liveSource === "convex" && (
              <span
                style={{
                  marginLeft: 8,
                  fontSize: "0.7rem",
                  color: "var(--success)",
                  fontFamily: "var(--font-mono-stack)",
                }}
                title="computed from open findings + caveats; live from Convex"
              >
                ● live
              </span>
            )}
          </span>
          <strong>{readiness}%</strong>
        </div>
        <div className="paper-readiness-track h-2.5 overflow-hidden rounded-full bg-border">
          <div
            className={`paper-readiness-fill ${readinessColor(readiness)}`}
            style={{ width: `${readiness}%` }}
          />
        </div>
        {openSummary && (
          <p
            style={{
              margin: 0,
              fontSize: "0.72rem",
              color: "var(--text-muted)",
              fontFamily: "var(--font-mono-stack)",
            }}
            title="Open findings (B=BLOCKER, M=MAJOR, m=minor) + open §pathc_caveats items (C)"
          >
            {openSummary} · {lastUpdated ?? "no date"}
          </p>
        )}
      </div>

      <Card className="paper-summary-card">
        <CardContent>
          <p className="paper-summary"><MathText>{paper.description}</MathText></p>
        </CardContent>
      </Card>

      <Card className="paper-summary-card" style={{ marginTop: 16 }}>
        <CardHeader>
          <CardTitle className="text-sm font-mono" style={{ textTransform: "uppercase", letterSpacing: "0.06em", color: "var(--text-muted)" }}>
            Path to publication
          </CardTitle>
        </CardHeader>
        <CardContent>
          <PublicationPath stages={paper.path} />
        </CardContent>
      </Card>

      {focusAreas.length > 0 && (
        <Card className="paper-summary-card" style={{ marginTop: 16 }}>
          <CardHeader>
            <CardTitle
              className="text-sm font-mono"
              style={{
                textTransform: "uppercase",
                letterSpacing: "0.06em",
                color: "var(--text-muted)",
              }}
            >
              Focus areas
              {novelty && (
                <span
                  title="Novelty tier per /never-claim-n4 (N1 incremental · N2 substantive · N3 first-of-kind). N4 reserved for paradigm-shifting work awarded by the field."
                  style={{
                    marginLeft: 10,
                    padding: "2px 7px",
                    fontSize: "0.65rem",
                    border: "1px solid var(--border)",
                    borderRadius: 4,
                    color: "var(--text-muted)",
                    letterSpacing: "0.04em",
                  }}
                >
                  Novelty: {novelty}
                </span>
              )}
            </CardTitle>
          </CardHeader>
          <CardContent>
            <ul style={{ margin: 0, paddingLeft: 20, fontSize: "0.88rem", lineHeight: 1.6 }}>
              {focusAreas.map((item) => (
                <li key={item}><MathText>{item}</MathText></li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}

      {notables.length > 0 && (
        <Card className="paper-summary-card" style={{ marginTop: 16 }}>
          <CardHeader>
            <CardTitle
              className="text-sm font-mono"
              style={{
                textTransform: "uppercase",
                letterSpacing: "0.06em",
                color: "var(--text-muted)",
              }}
            >
              Notable contributions
            </CardTitle>
          </CardHeader>
          <CardContent>
            <ul style={{ margin: 0, paddingLeft: 20, fontSize: "0.88rem", lineHeight: 1.6 }}>
              {notables.map((n) => (
                <li key={n.ordinal}><MathText>{n.bullet}</MathText></li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}

      {recentRounds.length > 0 && (
        <Card className="paper-summary-card" style={{ marginTop: 16 }}>
          <CardHeader>
            <CardTitle
              className="text-sm font-mono"
              style={{
                textTransform: "uppercase",
                letterSpacing: "0.06em",
                color: "var(--text-muted)",
              }}
            >
              Review history ({paperRounds.length} rounds)
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid gap-0" style={{ fontSize: "0.82rem" }}>
              {recentRounds.map((r, i) => (
                <div
                  key={r.id}
                  style={{
                    display: "grid",
                    gridTemplateColumns: "90px minmax(0,1fr)",
                    gap: 10,
                    padding: "8px 0",
                    borderTop: i === 0 ? "none" : "1px solid var(--border)",
                    alignItems: "baseline",
                  }}
                >
                  <span
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      color: "var(--text-muted)",
                      fontSize: "0.75rem",
                    }}
                  >
                    {r.dateISO}
                  </span>
                  <span style={{ minWidth: 0 }}>
                    <span
                      style={{
                        fontFamily: "var(--font-mono-stack)",
                        fontSize: "0.72rem",
                        color:
                          r.kind === "external-browser"
                            ? "var(--accent)"
                            : "var(--text-tertiary)",
                        letterSpacing: "0.04em",
                      }}
                    >
                      {r.id}
                    </span>
                    <span
                      style={{
                        marginLeft: 8,
                        color: "var(--text-secondary)",
                        lineHeight: 1.5,
                      }}
                    >
                      {r.title}
                    </span>
                  </span>
                </div>
              ))}
            </div>
            <p style={{ margin: "10px 0 0 0", fontSize: "0.78rem" }}>
              <Link
                href={`/reviews?papers=${paperId}`}
                style={{ color: "var(--accent-link)" }}
              >
                Full review timeline for Paper {paper.number} →
              </Link>
            </p>
          </CardContent>
        </Card>
      )}

      {(() => {
        const texArtifact = paper.artifacts.find((a) => a.label?.toLowerCase().includes("latex"));
        const texPath = texArtifact?.href.replace(/^https:\/\/github\.com\/[^/]+\/[^/]+\/blob\/[^/]+\//, "") ?? "";
        const pdfArtRaw = paper.artifacts.find((a) => a.kind === "primary" && a.href.toLowerCase().endsWith(".pdf"));
        const pdfArt = pdfArtRaw && livePdfHref ? { ...pdfArtRaw, href: livePdfHref } : pdfArtRaw;
        if (!pdfArt) return null;
        return (
          <ExternalReviewPanel
            paperNumber={paper.number}
            paperTitle={paper.title}
            paperVersion={version}
            paperPath={texPath || "(see GitHub LaTeX source artifact)"}
            pdfHref={pdfArt.href}
            pdfMeta={paper.pdfMeta}
            focusAreas={focusAreas}
          />
        );
      })()}

      <Separator className="my-8" />

      <Tabs defaultValue="results" className="paper-tabs w-full">
        <TabsList className="flex-wrap">
          <TabsTrigger value="results">Key Results</TabsTrigger>
          <TabsTrigger value="surveys">Surveys</TabsTrigger>
          <TabsTrigger value="predictions">Predictions</TabsTrigger>
          <TabsTrigger value="figures">Figures</TabsTrigger>
          {paper.remainingWork.length > 0 && (
            <TabsTrigger value="todo">
              Remaining ({paper.remainingWork.length})
            </TabsTrigger>
          )}
        </TabsList>

        <TabsContent value="results" className="pt-4">
          <Card className="paper-tab-panel">
            <CardHeader>
              <CardTitle>Key Results</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="paper-result-list grid gap-0">
                {paper.keyResults.map((r, i) => (
                  <li key={i} className="grid grid-cols-[34px_minmax(0,1fr)] gap-3">
                    <span className="font-mono text-xs text-muted-foreground">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    <span>
                      <MathText>{r}</MathText>
                    </span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="surveys" className="pt-4">
          {paper.surveys.length > 0 ? (
            <div className="paper-chip-grid">
              {paper.surveys.map((s) => (
                <div key={s} className="paper-chip-card">
                  <MathText>{s}</MathText>
                </div>
              ))}
            </div>
          ) : (
            <Alert>
              <AlertTitle>No surveys connected</AlertTitle>
              <AlertDescription>
                This paper does not draw on a specific survey dataset.
              </AlertDescription>
            </Alert>
          )}
        </TabsContent>

        <TabsContent value="predictions" className="pt-4">
          <div className="paper-chip-grid">
            {paper.predictions.map((p) => (
              <div key={p} className="paper-chip-card">
                <MathText>{p}</MathText>
              </div>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="figures" className="pt-4">
          {figures.length > 0 ? (
            <PaperFigureGallery
              inPaper={inPaperFigures}
              candidates={candidateFigures}
              paperNumber={paper.number}
            />
          ) : paper.figures.length > 0 ? (
            <div className="paper-chip-grid">
              {paper.figures.map((f) => (
                <div key={f} className="paper-chip-card">
                  <MathText>{f}</MathText>
                </div>
              ))}
            </div>
          ) : (
            <Alert>
              <AlertTitle>No figures registered yet</AlertTitle>
              <AlertDescription>
                Figures will populate as the paper draft is finalized.
              </AlertDescription>
            </Alert>
          )}
        </TabsContent>

        {paper.remainingWork.length > 0 && (
          <TabsContent value="todo" className="pt-4">
            <div className="paper-task-list">
              {paper.remainingWork.map((task, i) => (
                <div
                  key={i}
                  className="paper-task-item"
                >
                  <span
                    className={`h-2 w-2 shrink-0 rounded-full ${task.startsWith("TIER 1") ?"dot-tone-danger" :"dot-tone-caution"}`}
                  />
                  <span><MathText>{task}</MathText></span>
                </div>
              ))}
            </div>
          </TabsContent>
        )}
      </Tabs>

      <div className="mt-8 flex gap-2">
        <Button asChild variant="outline" size="sm">
          <Link href="/paper">&larr; All papers</Link>
        </Button>
      </div>
    </>
  );
}
