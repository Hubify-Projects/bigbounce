import { surveys } from "@/data/surveys";
import { predictions } from "@/data/predictions";
import { papers } from "@/data/papers";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import Link from "next/link";

const totalAnomalies = surveys.reduce((s, sv) => s + sv.anomalies, 0);
const qcPassCount = surveys.filter((s) => s.qcStatus === "pass").length;

const predStatusVariant: Record<
  "green" | "blue" | "amber" | "red" | "purple",
  "default" | "secondary" | "destructive" | "outline"
> = {
  green: "default",
  blue: "secondary",
  amber: "outline",
  red: "destructive",
  purple: "secondary",
};

const paperStatusVariant: Record<
  "green" | "blue" | "amber" | "red",
  "default" | "secondary" | "destructive" | "outline"
> = {
  green: "default",
  blue: "secondary",
  amber: "outline",
  red: "destructive",
};

const surveyQcVariant: Record<
  "pass" | "caution" | "fail" | "needs-expansion",
  { variant: "default" | "secondary" | "destructive" | "outline"; label: string }
> = {
  pass: { variant: "default", label: "PASS" },
  caution: { variant: "outline", label: "CAUTION" },
  fail: { variant: "destructive", label: "FAIL" },
  "needs-expansion": { variant: "outline", label: "EXPAND" },
};

const stats: Array<{ value: string; label: string; tone: string }> = [
  { value: "4", label: "Papers", tone: "text-emerald-600 dark:text-emerald-400" },
  {
    value: `${surveys.length}`,
    label: "Surveys",
    tone: "text-blue-600 dark:text-blue-400",
  },
  {
    value: "37.3M+",
    label: "Sources Scored",
    tone: "text-emerald-600 dark:text-emerald-400",
  },
  {
    value: `${(totalAnomalies / 1000).toFixed(0)}K+`,
    label: "Anomalies",
    tone: "text-emerald-600 dark:text-emerald-400",
  },
  {
    value: "424K+",
    label: "MCMC Samples",
    tone: "text-emerald-600 dark:text-emerald-400",
  },
  {
    value: `${qcPassCount}/${surveys.length}`,
    label: "QC Pass",
    tone:
      qcPassCount === surveys.length
        ? "text-emerald-600 dark:text-emerald-400"
        : "text-amber-600 dark:text-amber-400",
  },
  {
    value: "4",
    label: "Predictions",
    tone: "text-blue-600 dark:text-blue-400",
  },
  {
    value: "50",
    label: "Queued Experiments",
    tone: "text-amber-600 dark:text-amber-400",
  },
];

const exploreLinks: Array<{
  href: string;
  external?: boolean;
  title: string;
  description: string;
}> = [
  {
    href: "/explained",
    title: "Explainer",
    description: "Non-technical guide",
  },
  {
    href: "/glossary",
    title: "Glossary",
    description: "Key terms & equations",
  },
  {
    href: "/timeline",
    title: "Timeline",
    description: "Cosmic history → 2028",
  },
  {
    href: "/speculations",
    title: "Speculations",
    description: "Future research paths",
  },
  {
    href: "https://github.com/Hubify-Projects/bigbounce",
    external: true,
    title: "GitHub",
    description: "Source code & data",
  },
  {
    href: "mailto:houston@hubify.com",
    external: true,
    title: "Contact",
    description: "houston@hubify.com",
  },
];

export default function HomePage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Research Program &middot; Updated April 2026
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          Spin-Torsion Cosmology
        </h1>
        <p className="subtitle">
          Proving bounce cosmology beats inflation through systematic AI-powered
          archival mining and precision cosmological tests. 4 papers, 8 surveys,
          37.3M sources scored.
        </p>
      </div>

      <div className="mt-6 grid grid-cols-2 gap-3 md:grid-cols-4">
        {stats.map((stat) => (
          <Card key={stat.label}>
            <CardContent className="p-4">
              <div
                className={`text-2xl font-bold ${stat.tone}`}
                style={{ fontFamily: "var(--font-serif)" }}
              >
                {stat.value}
              </div>
              <div className="mt-1 text-xs uppercase tracking-wider text-muted-foreground">
                {stat.label}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>
          <Link
            href="/predictions"
            className="no-underline text-foreground hover:text-muted-foreground"
          >
            Testable Predictions &rarr;
          </Link>
        </h2>
        <div className="grid gap-3 md:grid-cols-2">
          {predictions.map((pred) => (
            <Card
              key={pred.slug}
              className="flex flex-col transition-colors hover:bg-accent/40"
            >
              <Link
                href={`/predictions/${pred.slug}`}
                className="flex h-full flex-col no-underline text-foreground"
              >
                <CardHeader className="pb-2">
                  <div className="flex items-start justify-between gap-3">
                    <CardTitle
                      className="text-sm"
                      style={{ fontFamily: "var(--font-serif)" }}
                    >
                      {pred.name}
                    </CardTitle>
                    <Badge variant={predStatusVariant[pred.statusVariant]}>
                      {pred.status}
                    </Badge>
                  </div>
                </CardHeader>
                <CardContent className="flex-1">
                  <div className="font-mono text-xl font-bold">
                    {pred.value}
                  </div>
                  <p className="mt-2 text-xs text-muted-foreground">
                    {pred.bestModel} &middot; {pred.experiment}
                  </p>
                </CardContent>
              </Link>
            </Card>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>
          <Link
            href="/surveys"
            className="no-underline text-foreground hover:text-muted-foreground"
          >
            Survey Results &rarr;
          </Link>
        </h2>
        <Card>
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Survey</TableHead>
                  <TableHead>Sources</TableHead>
                  <TableHead>Anomalies</TableHead>
                  <TableHead>QC</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {surveys.map((survey) => {
                  const qc = surveyQcVariant[survey.qcStatus];
                  return (
                    <TableRow key={survey.slug}>
                      <TableCell>
                        <Link
                          href={`/surveys/${survey.slug}`}
                          className="font-semibold underline-offset-4 hover:underline"
                        >
                          {survey.name}
                        </Link>
                      </TableCell>
                      <TableCell className="text-muted-foreground">
                        {survey.sources}
                      </TableCell>
                      <TableCell className="font-mono text-muted-foreground">
                        {survey.anomalies.toLocaleString()} ({survey.anomalyRate}
                        )
                      </TableCell>
                      <TableCell>
                        <Badge variant={qc.variant}>{qc.label}</Badge>
                      </TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </section>

      <section className="section">
        <h2>
          <Link
            href="/paper"
            className="no-underline text-foreground hover:text-muted-foreground"
          >
            Research Papers &rarr;
          </Link>
        </h2>
        <div className="space-y-1 rounded-lg border bg-card">
          {papers.map((paper) => (
            <Link
              key={paper.slug}
              href={`/papers/${paper.slug}`}
              className="flex items-center gap-4 border-b px-4 py-3 last:border-b-0 hover:bg-accent/40"
            >
              <div className="flex-1">
                <div className="text-sm font-semibold">
                  Paper {paper.number}
                </div>
                <div className="text-xs text-muted-foreground">
                  {paper.title.slice(0, 80)}…
                </div>
              </div>
              <div className="hidden h-1.5 w-20 overflow-hidden rounded-full bg-border md:block">
                <div
                  className={`h-full rounded-full ${
                    paper.readiness === 100
                      ? "bg-emerald-500"
                      : paper.readiness >= 90
                        ? "bg-blue-500"
                        : "bg-amber-500"
                  }`}
                  style={{ width: `${paper.readiness}%` }}
                />
              </div>
              <Badge variant={paperStatusVariant[paper.statusVariant]}>
                {paper.readiness}%
              </Badge>
            </Link>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Current Focus</h2>
        <Card className="border-l-4 border-l-blue-500">
          <CardHeader>
            <CardTitle
              className="text-base"
              style={{ fontFamily: "var(--font-serif)" }}
            >
              H200 Queue v2 — Phase 2 Running
            </CardTitle>
            <CardDescription>
              5/6 Phase 1 re-runs QC PASS (Planck, ACT, NEOWISE, Gaia,
              Taxonomy). Phase 2 validation in progress. 50 total experiments
              across 10 phases. Auto-backup every 20min. Est. ~$1,768 total.
            </CardDescription>
          </CardHeader>
          <CardFooter className="flex flex-wrap gap-2 pt-0">
            <Button asChild size="sm" variant="outline">
              <Link href="/activity">Activity Feed &rarr;</Link>
            </Button>
            <Button asChild size="sm" variant="outline">
              <Link href="/status">Full Status &rarr;</Link>
            </Button>
          </CardFooter>
        </Card>
      </section>

      <section className="section">
        <h2>Explore</h2>
        <div className="grid gap-3 md:grid-cols-3">
          {exploreLinks.map((link) =>
            link.external ? (
              <a
                key={link.href}
                href={link.href}
                target={link.href.startsWith("http") ? "_blank" : undefined}
                rel={link.href.startsWith("http") ? "noopener" : undefined}
                className="no-underline text-foreground"
              >
                <Card className="text-center transition-colors hover:bg-accent/40">
                  <CardContent className="p-4">
                    <div
                      className="text-base font-semibold"
                      style={{ fontFamily: "var(--font-serif)" }}
                    >
                      {link.title}
                    </div>
                    <p className="mt-1 text-xs text-muted-foreground">
                      {link.description}
                    </p>
                  </CardContent>
                </Card>
              </a>
            ) : (
              <Link
                key={link.href}
                href={link.href}
                className="no-underline text-foreground"
              >
                <Card className="text-center transition-colors hover:bg-accent/40">
                  <CardContent className="p-4">
                    <div
                      className="text-base font-semibold"
                      style={{ fontFamily: "var(--font-serif)" }}
                    >
                      {link.title}
                    </div>
                    <p className="mt-1 text-xs text-muted-foreground">
                      {link.description}
                    </p>
                  </CardContent>
                </Card>
              </Link>
            ),
          )}
        </div>
      </section>
    </>
  );
}
