import { surveys, getSurveyBySlug } from "@/data/surveys";
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
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";

export function generateStaticParams() {
  return surveys.map((s) => ({ slug: s.slug }));
}

type PageParams = Promise<{ slug: string }>;

export async function generateMetadata({
  params,
}: {
  params: PageParams;
}): Promise<Metadata> {
  const { slug } = await params;
  const survey = getSurveyBySlug(slug);
  if (!survey) return { title: "Not Found" };
  return {
    title: survey.name,
    description: `${survey.name}: ${survey.sources} scored, ${survey.anomalies.toLocaleString()} anomalies found.`,
  };
}

const qcVariantMap: Record<
  "pass" | "caution" | "fail" | "needs-expansion",
  {
    variant: "default" | "secondary" | "destructive" | "outline";
    label: string;
    border: string;
  }
> = {
  pass: {
    variant: "default",
    label: "QC PASS",
    border: "border-l-emerald-500",
  },
  caution: {
    variant: "outline",
    label: "QC CAUTION",
    border: "border-l-amber-500",
  },
  fail: {
    variant: "destructive",
    label: "QC FAIL",
    border: "border-l-red-500",
  },
  "needs-expansion": {
    variant: "outline",
    label: "NEEDS EXPANSION",
    border: "border-l-amber-500",
  },
};

export default async function SurveyPage({
  params,
}: {
  params: PageParams;
}) {
  const { slug } = await params;
  const survey = getSurveyBySlug(slug);
  if (!survey) notFound();

  const qc = qcVariantMap[survey.qcStatus];

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link
            href="/surveys"
            style={{ color: "var(--text-muted)", textDecoration: "none" }}
          >
            Surveys
          </Link>{" "}
          &rarr; {survey.shortName}
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          {survey.name}
        </h1>
        <p className="subtitle">{survey.description}</p>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <Badge variant={qc.variant}>{qc.label}</Badge>
          <Badge variant="secondary" className="font-mono">
            {survey.sources}
          </Badge>
          <Badge variant="secondary" className="font-mono">
            {survey.anomalies.toLocaleString()} anomalies ({survey.anomalyRate})
          </Badge>
          <Badge variant="outline">{survey.wavelength}</Badge>
        </div>
      </div>

      <Card className={`mt-6 border-l-4 ${qc.border}`}>
        <CardHeader>
          <CardTitle className="text-sm">QC Status</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">{survey.qcNote}</p>
        </CardContent>
      </Card>

      <Separator className="my-8" />

      <Tabs defaultValue="findings" className="w-full">
        <TabsList>
          <TabsTrigger value="findings">Key Findings</TabsTrigger>
          <TabsTrigger value="anomalies">
            Top Anomalies ({survey.topAnomalies.length})
          </TabsTrigger>
          <TabsTrigger value="pipeline">Pipeline</TabsTrigger>
          <TabsTrigger value="papers">Papers</TabsTrigger>
          <TabsTrigger value="connections">Connections</TabsTrigger>
          <TabsTrigger value="tasks">
            Tasks ({survey.followUpTasks.length})
          </TabsTrigger>
          {survey.figures.length > 0 && (
            <TabsTrigger value="figures">Figures</TabsTrigger>
          )}
        </TabsList>

        <TabsContent value="findings" className="pt-4">
          <Card>
            <CardHeader>
              <CardTitle>Key Findings</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="list-disc space-y-2 pl-5 text-sm leading-relaxed text-muted-foreground">
                {survey.keyFindings.map((finding, i) => (
                  <li key={i}>{finding}</li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="anomalies" className="pt-4">
          {survey.topAnomalies.length > 0 ? (
            <Card>
              <CardContent className="p-0">
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead>Rank</TableHead>
                      <TableHead>RA</TableHead>
                      <TableHead>Dec</TableHead>
                      <TableHead>Score</TableHead>
                      <TableHead>Type</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {survey.topAnomalies.map((a) => (
                      <TableRow key={a.rank}>
                        <TableCell className="font-mono">#{a.rank}</TableCell>
                        <TableCell className="font-mono">
                          {a.ra.toFixed(1)}°
                        </TableCell>
                        <TableCell className="font-mono">
                          {a.dec.toFixed(1)}°
                        </TableCell>
                        <TableCell className="font-mono">
                          {a.score.toFixed(2)}
                        </TableCell>
                        <TableCell className="text-muted-foreground">
                          {a.type || "—"}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </CardContent>
            </Card>
          ) : (
            <Alert>
              <AlertTitle>No top anomalies surfaced yet</AlertTitle>
              <AlertDescription>
                This survey is still being processed or its top-N list has not
                been published.
              </AlertDescription>
            </Alert>
          )}
        </TabsContent>

        <TabsContent value="pipeline" className="pt-4">
          <Card>
            <CardContent className="p-0">
              <Table>
                <TableBody>
                  <TableRow>
                    <TableCell className="w-32 font-medium">Pipeline</TableCell>
                    <TableCell className="text-muted-foreground">
                      {survey.pipeline}
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">Wavelength</TableCell>
                    <TableCell className="text-muted-foreground">
                      {survey.wavelength}
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">Cost</TableCell>
                    <TableCell className="font-mono text-muted-foreground">
                      {survey.cost}
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">Runtime</TableCell>
                    <TableCell className="font-mono text-muted-foreground">
                      {survey.runtime}
                    </TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="papers" className="pt-4">
          <div className="grid gap-2 md:grid-cols-2">
            {survey.paperRefs.map((ref) => (
              <Card key={ref}>
                <CardContent className="p-4 text-sm">{ref}</CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="connections" className="pt-4">
          {survey.connections.length > 0 ? (
            <div className="flex flex-wrap gap-2">
              {survey.connections.map((conn) => (
                <Button
                  key={conn.href}
                  asChild
                  variant="secondary"
                  size="sm"
                >
                  <Link href={conn.href}>{conn.label} &rarr;</Link>
                </Button>
              ))}
            </div>
          ) : (
            <Alert>
              <AlertTitle>No cross-links registered</AlertTitle>
              <AlertDescription>
                Connections to predictions, papers, and other surveys will
                populate as the catalog grows.
              </AlertDescription>
            </Alert>
          )}
        </TabsContent>

        <TabsContent value="tasks" className="pt-4">
          <div className="space-y-1 rounded-lg border bg-card">
            {survey.followUpTasks.map((task, i) => (
              <div
                key={i}
                className="flex items-center gap-3 border-b px-4 py-3 text-sm last:border-b-0"
              >
                <span className="h-2 w-2 shrink-0 rounded-full bg-amber-500" />
                <span className="text-muted-foreground">{task}</span>
              </div>
            ))}
          </div>
        </TabsContent>

        {survey.figures.length > 0 && (
          <TabsContent value="figures" className="pt-4">
            <div className="flex flex-wrap gap-2">
              {survey.figures.map((fig) => (
                <Badge key={fig} variant="outline" className="text-xs">
                  {fig}
                </Badge>
              ))}
            </div>
          </TabsContent>
        )}
      </Tabs>

      <div className="mt-8 flex gap-2">
        <Button asChild variant="outline" size="sm">
          <Link href="/surveys">&larr; All surveys</Link>
        </Button>
      </div>
    </>
  );
}
