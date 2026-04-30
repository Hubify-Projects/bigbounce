import { predictions, getPredictionBySlug } from "@/data/predictions";
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
  return predictions.map((p) => ({ slug: p.slug }));
}

type PageParams = Promise<{ slug: string }>;

export async function generateMetadata({
  params,
}: {
  params: PageParams;
}): Promise<Metadata> {
  const { slug } = await params;
  const pred = getPredictionBySlug(slug);
  if (!pred) return { title: "Not Found" };
  return {
    title: pred.name,
    description: `${pred.name}: ${pred.value}. ${pred.status}.`,
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
  purple: "secondary",
};

export default async function PredictionPage({
  params,
}: {
  params: PageParams;
}) {
  const { slug } = await params;
  const pred = getPredictionBySlug(slug);
  if (!pred) notFound();

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link
            href="/predictions"
            style={{ color: "var(--text-muted)", textDecoration: "none" }}
          >
            Predictions
          </Link>{" "}
          &rarr; {pred.name}
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          {pred.name}
        </h1>
        <p className="subtitle">{pred.description}</p>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <Badge variant={statusVariantMap[pred.statusVariant]}>
            {pred.status}
          </Badge>
          <Badge variant="secondary" className="font-mono">
            {pred.value}
          </Badge>
          <Badge variant="outline">{pred.bestModel}</Badge>
          <Badge variant="outline">{pred.experiment}</Badge>
        </div>
      </div>

      <Card className="mt-6 border-l-4 border-l-blue-500">
        <CardHeader>
          <CardTitle className="text-sm">Current Constraint</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            {pred.currentConstraint}
          </p>
        </CardContent>
      </Card>

      <Separator className="my-8" />

      <Tabs defaultValue="results" className="w-full">
        <TabsList>
          <TabsTrigger value="results">Key Results</TabsTrigger>
          <TabsTrigger value="surveys">Surveys</TabsTrigger>
          <TabsTrigger value="papers">Papers</TabsTrigger>
          <TabsTrigger value="timeline">Timeline</TabsTrigger>
          <TabsTrigger value="next">
            Next Steps ({pred.nextSteps.length})
          </TabsTrigger>
        </TabsList>

        <TabsContent value="results" className="pt-4">
          <Card>
            <CardHeader>
              <CardTitle>Key Results</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="list-disc space-y-2 pl-5 text-sm leading-relaxed text-muted-foreground">
                {pred.keyResults.map((r, i) => (
                  <li key={i}>{r}</li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="surveys" className="pt-4">
          {pred.surveys.length > 0 ? (
            <div className="grid gap-2 md:grid-cols-2">
              {pred.surveys.map((s) => (
                <Card key={s}>
                  <CardContent className="p-4 text-sm">{s}</CardContent>
                </Card>
              ))}
            </div>
          ) : (
            <Alert>
              <AlertTitle>No survey datasets attached</AlertTitle>
              <AlertDescription>
                This prediction is currently in theoretical or external-data
                territory.
              </AlertDescription>
            </Alert>
          )}
        </TabsContent>

        <TabsContent value="papers" className="pt-4">
          <div className="grid gap-2 md:grid-cols-2">
            {pred.papers.map((p) => (
              <Card key={p}>
                <CardContent className="p-4 text-sm">{p}</CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="timeline" className="pt-4">
          <Card>
            <CardContent className="p-6 text-sm text-muted-foreground">
              {pred.timeline}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="next" className="pt-4">
          <div className="space-y-1 rounded-lg border bg-card">
            {pred.nextSteps.map((step, i) => (
              <div
                key={i}
                className="flex items-center gap-3 border-b px-4 py-3 text-sm last:border-b-0"
              >
                <span className="h-2 w-2 shrink-0 rounded-full bg-amber-500" />
                <span className="text-muted-foreground">{step}</span>
              </div>
            ))}
          </div>
        </TabsContent>
      </Tabs>

      <div className="mt-8 flex gap-2">
        <Button asChild variant="outline" size="sm">
          <Link href="/predictions">&larr; All predictions</Link>
        </Button>
      </div>
    </>
  );
}
