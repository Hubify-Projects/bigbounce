import { papers, getPaperBySlug } from "@/data/papers";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import {
  Tabs,
  TabsList,
  TabsTrigger,
  TabsContent,
} from "@/components/ui/tabs";
import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";

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
  if (!paper) return { title: "Not Found" };
  return {
    title: `Paper ${paper.number}`,
    description: paper.title,
  };
}

const statusVariantMap: Record<
  string,
  "default" | "secondary" | "destructive" | "outline"
> = {
  green: "default",
  blue: "secondary",
  amber: "outline",
  red: "destructive",
};

function readinessColor(pct: number) {
  if (pct === 100) return "bg-emerald-500";
  if (pct >= 90) return "bg-blue-500";
  return "bg-amber-500";
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
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link
            href="/paper"
            style={{ color: "var(--text-muted)", textDecoration: "none" }}
          >
            Papers
          </Link>{" "}
          &rarr; Paper {paper.number}
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          Paper {paper.number}
        </h1>
        <p className="subtitle" style={{ fontFamily: "var(--font-serif)" }}>
          {paper.title}
        </p>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <Badge variant={statusVariantMap[paper.statusVariant]}>
            {paper.status}
          </Badge>
          <Badge variant="outline">{paper.version}</Badge>
          <Badge variant="outline">{paper.pages} pages</Badge>
          <Badge variant="outline">{paper.refs} refs</Badge>
          <Badge variant="outline">Target: {paper.target}</Badge>
        </div>
      </div>

      <div className="my-6 flex items-center gap-3">
        <div className="h-2 flex-1 overflow-hidden rounded-full bg-border">
          <div
            className={`h-full transition-[width] duration-300 ${readinessColor(paper.readiness)}`}
            style={{ width: `${paper.readiness}%` }}
          />
        </div>
        <span className="text-xs font-mono text-muted-foreground">
          {paper.readiness}% ready
        </span>
      </div>

      <p className="text-[15px] leading-relaxed text-muted-foreground">
        {paper.description}
      </p>

      <Separator className="my-8" />

      <Tabs defaultValue="results" className="w-full">
        <TabsList>
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
          <Card>
            <CardHeader>
              <CardTitle>Key Results</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="list-disc space-y-2 pl-5 text-sm leading-relaxed text-muted-foreground">
                {paper.keyResults.map((r, i) => (
                  <li key={i}>{r}</li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="surveys" className="pt-4">
          {paper.surveys.length > 0 ? (
            <div className="grid gap-2 md:grid-cols-2">
              {paper.surveys.map((s) => (
                <Card key={s}>
                  <CardContent className="p-4 text-sm">{s}</CardContent>
                </Card>
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
          <div className="flex flex-wrap gap-2">
            {paper.predictions.map((p) => (
              <Badge key={p} variant="secondary" className="text-xs">
                {p}
              </Badge>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="figures" className="pt-4">
          {paper.figures.length > 0 ? (
            <div className="flex flex-wrap gap-2">
              {paper.figures.map((f) => (
                <Badge key={f} variant="outline" className="text-xs">
                  {f}
                </Badge>
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
            <div className="space-y-1 rounded-lg border bg-card">
              {paper.remainingWork.map((task, i) => (
                <div
                  key={i}
                  className="flex items-center gap-3 border-b px-4 py-3 text-sm last:border-b-0"
                >
                  <span
                    className={`h-2 w-2 shrink-0 rounded-full ${task.startsWith("TIER 1") ? "bg-red-500" : "bg-amber-500"}`}
                  />
                  <span className="text-muted-foreground">{task}</span>
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
