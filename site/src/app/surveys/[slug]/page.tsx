import { surveys, getSurveyBySlug } from"@/data/surveys";
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
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from"@/components/ui/table";
import { Alert, AlertTitle, AlertDescription } from"@/components/ui/alert";
import Link from"next/link";
import { notFound } from"next/navigation";
import type { Metadata } from"next";
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle2,
  ClipboardList,
  Database,
  Gauge,
  Link2,
  RadioTower,
  Telescope,
} from"lucide-react";

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
  if (!survey) return { title:"Not Found" };
  return {
    title: survey.name,
    description: `${survey.name}: ${survey.sources} scored, ${survey.anomalies.toLocaleString()} anomalies found.`,
  };
}

const qcVariantMap: Record<
"pass" |"caution" |"fail" |"needs-expansion",
  {
    variant:"default" |"secondary" |"destructive" |"outline";
    label: string;
    border: string;
  }
> = {
  pass: {
    variant:"default",
    label:"QC PASS",
    border:"border-tone-success",
  },
  caution: {
    variant:"outline",
    label:"QC CAUTION",
    border:"border-tone-caution",
  },
  fail: {
    variant:"destructive",
    label:"QC FAIL",
    border:"border-tone-danger",
  },
"needs-expansion": {
    variant:"outline",
    label:"NEEDS EXPANSION",
    border:"border-tone-caution",
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
  const relatedSurveyLinks = survey.connections.filter((conn) =>
    conn.href.startsWith("/surveys/"),
  );
  const externalProgramLinks = survey.connections.filter(
    (conn) => !conn.href.startsWith("/surveys/"),
  );

  return (
    <>
      <div className="survey-detail-hero">
        <div className="hero">
          <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link
            href="/surveys"
            style={{ color:"var(--text-muted)", textDecoration:"none" }}
          >
            Surveys
          </Link>{""}
          &rarr; {survey.shortName}
          </p>
          <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
            {survey.name}
          </h1>
          <p className="subtitle"><MathText>{survey.description}</MathText></p>
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

        <Card className={`survey-status-card border-l-4 ${qc.border}`}>
          <div className="card-kicker">Readiness</div>
          <div className="survey-status-title">
            <Badge variant={qc.variant}>{qc.label}</Badge>
            <span>{survey.shortName}</span>
          </div>
          <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
            <MathText>{survey.qcNote}</MathText>
          </p>
          <div className="survey-status-grid">
            <div>
              <span>Cost</span>
              <strong>{survey.cost}</strong>
            </div>
            <div>
              <span>Runtime</span>
              <strong>{survey.runtime}</strong>
            </div>
          </div>
        </Card>
      </div>

      <div className="survey-stat-strip">
        <div className="survey-stat">
          <Database aria-hidden="true" />
          <span>Sources</span>
          <strong>{survey.sources}</strong>
        </div>
        <div className="survey-stat">
          <Telescope aria-hidden="true" />
          <span>Anomalies</span>
          <strong>{survey.anomalies.toLocaleString()}</strong>
        </div>
        <div className="survey-stat">
          <Gauge aria-hidden="true" />
          <span>Rate</span>
          <strong>{survey.anomalyRate}</strong>
        </div>
        <div className="survey-stat">
          <RadioTower aria-hidden="true" />
          <span>Band</span>
          <strong>{survey.wavelength.split(" ")[0]}</strong>
        </div>
      </div>

      <Separator className="my-8" />

      <div className="survey-detail-grid">
        <section className="survey-main-column">
          <Card>
            <CardHeader>
              <CardTitle className="survey-section-title">
                <CheckCircle2 aria-hidden="true" />
                Key Findings
              </CardTitle>
              <CardDescription>
                Results that define how this survey should be used in the paper set.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <ul className="survey-finding-list">
                {survey.keyFindings.map((finding, i) => (
                  <li key={i}>
                    <span>{String(i + 1).padStart(2,"0")}</span>
                    <MathText>{finding}</MathText>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="survey-section-title">
                <Database aria-hidden="true" />
                Pipeline
              </CardTitle>
            </CardHeader>
            <CardContent className="p-0">
              <Table>
                <TableBody>
                  <TableRow>
                    <TableCell className="w-36 font-medium">Model</TableCell>
                    <TableCell className="text-muted-foreground">
                      <MathText>{survey.pipeline}</MathText>
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

          <Card>
            <CardHeader>
              <CardTitle className="survey-section-title">
                <Telescope aria-hidden="true" />
                Top Anomalies
              </CardTitle>
            </CardHeader>
            <CardContent className={survey.topAnomalies.length > 0 ? "p-0" : ""}>
              {survey.topAnomalies.length > 0 ? (
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
                          {a.ra.toFixed(1)}deg
                        </TableCell>
                        <TableCell className="font-mono">
                          {a.dec.toFixed(1)}deg
                        </TableCell>
                        <TableCell className="font-mono">
                          {a.score.toFixed(2)}
                        </TableCell>
                        <TableCell className="text-muted-foreground">
                          {a.type ||"—"}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              ) : (
                <Alert>
                  <AlertTitle>No top anomalies surfaced yet</AlertTitle>
                  <AlertDescription>
                    This survey is still being processed or its top-N list has not
                    been published.
                  </AlertDescription>
                </Alert>
              )}
            </CardContent>
          </Card>
        </section>

        <aside className="survey-side-column">
          <Card>
            <CardHeader>
              <CardTitle className="survey-section-title">
                <ClipboardList aria-hidden="true" />
                Follow-Up Queue
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="survey-task-list">
                {survey.followUpTasks.map((task, i) => (
                  <div key={i} className="survey-task">
                    <span>{i + 1}</span>
                    <MathText>{task}</MathText>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="survey-section-title">
                <Link2 aria-hidden="true" />
                Paper Links
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="survey-pill-list">
                {survey.paperRefs.map((ref) => (
                  <Badge key={ref} variant="secondary">
                    {ref}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>

          {relatedSurveyLinks.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="survey-section-title">
                  <RadioTower aria-hidden="true" />
                  Related Surveys
                </CardTitle>
              </CardHeader>
              <CardContent className="survey-link-stack">
                {relatedSurveyLinks.map((conn) => (
                  <Button key={conn.href} asChild variant="outline" size="sm">
                    <Link href={conn.href}>
                      {conn.label}
                      <ArrowRight aria-hidden="true" />
                    </Link>
                  </Button>
                ))}
              </CardContent>
            </Card>
          )}

          {externalProgramLinks.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="survey-section-title">
                  <Gauge aria-hidden="true" />
                  Program Connections
                </CardTitle>
              </CardHeader>
              <CardContent className="survey-link-stack">
                {externalProgramLinks.map((conn) => (
                  <Button key={conn.href} asChild variant="secondary" size="sm">
                    <Link href={conn.href}>
                      {conn.label}
                      <ArrowRight aria-hidden="true" />
                    </Link>
                  </Button>
                ))}
              </CardContent>
            </Card>
          )}

          {survey.figures.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="survey-section-title">
                  <Telescope aria-hidden="true" />
                  Figures
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="survey-pill-list">
                  {survey.figures.map((fig) => (
                    <Badge key={fig} variant="outline" className="text-xs">
                      {fig}
                    </Badge>
                  ))}
                </div>
              </CardContent>
              <CardFooter>
                <Button asChild variant="outline" size="sm">
                  <Link href="/figures">Open figures</Link>
                </Button>
              </CardFooter>
            </Card>
          )}
        </aside>
      </div>

      <div className="mt-8 flex gap-2">
        <Button asChild variant="outline" size="sm">
          <Link href="/surveys">
            <ArrowLeft aria-hidden="true" />
            All surveys
          </Link>
        </Button>
      </div>
    </>
  );
}
