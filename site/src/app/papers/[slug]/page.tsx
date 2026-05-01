import { papers, getPaperBySlug } from"@/data/papers";
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

function ArtifactLink({
  artifact,
}: {
  artifact: {
    label: string;
    href: string;
    kind: "primary" | "secondary";
    external?: boolean;
    download?: boolean;
  };
}) {
  const button = (
    <Button
      variant={artifact.kind === "primary" ? "default" : "outline"}
      size="sm"
      asChild
    >
      <a
        href={artifact.href}
        target={artifact.external ? "_blank" : undefined}
        rel={artifact.external ? "noopener noreferrer" : undefined}
        download={artifact.download ? true : undefined}
      >
        {artifact.label} {artifact.external ? "↗" : ""}
      </a>
    </Button>
  );

  return button;
}

export default async function PaperDetailPage({
  params,
}: {
  params: PageParams;
}) {
  const { slug } = await params;
  const paper = getPaperBySlug(slug);
  if (!paper) notFound();

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
            </div>
            <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
              Paper {paper.number}
            </h1>
            <p className="subtitle"><MathText>{paper.title}</MathText></p>
            <div className="mt-4 flex flex-wrap items-center gap-2">
              <Badge variant={statusVariantMap[paper.statusVariant]}>
                {paper.status}
              </Badge>
              <Badge variant="outline">{paper.version}</Badge>
              <Badge variant="outline">{paper.pages} pages</Badge>
              <Badge variant="outline">{paper.refs} refs</Badge>
              <Badge variant="outline">Target: {paper.target}</Badge>
            </div>
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
                {paper.artifacts.map((artifact) => (
                  <ArtifactLink key={`${artifact.href}-${artifact.label}`} artifact={artifact} />
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      <div className="paper-readiness grid gap-2">
        <div className="paper-readiness-head flex items-baseline justify-between gap-3">
          <span>Readiness</span>
          <strong>{paper.readiness}%</strong>
        </div>
        <div className="paper-readiness-track h-2.5 overflow-hidden rounded-full bg-border">
          <div
            className={`paper-readiness-fill ${readinessColor(paper.readiness)}`}
            style={{ width: `${paper.readiness}%` }}
          />
        </div>
      </div>

      <Card className="paper-summary-card">
        <CardContent>
          <p className="paper-summary"><MathText>{paper.description}</MathText></p>
        </CardContent>
      </Card>

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
          {paper.figures.length > 0 ? (
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
