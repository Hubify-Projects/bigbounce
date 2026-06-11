import { surveys } from"@/data/surveys";
import { predictions } from"@/data/predictions";
import { papers } from"@/data/papers";
import { liveStatus } from"@/data/live-status";
import { Badge } from"@/components/ui/badge";
import { Button } from"@/components/ui/button";
import { LiveStatus } from"@/components/Shell/LiveStatus";
import { LivePapersDashboard } from"@/components/Cards/LivePapersDashboard";
import { SurveyQcTable } from"@/components/Cards/SurveyQcTable";
import { PublicationPathCompact } from"@/components/PublicationPath";
import { MathText } from"@/components/MathText";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import { AlertTriangle, ArrowRight, Database, FileText, Orbit } from"lucide-react";
import Link from"next/link";

const totalAnomalies = surveys.reduce((s, sv) => s + sv.anomalies, 0);
const qcPassCount = surveys.filter((s) => s.qcStatus ==="pass").length;

const predStatusVariant: Record<
"green" |"blue" |"amber" |"red" |"purple",
"default" |"secondary" |"destructive" |"outline"
> = {
  green:"default",
  blue:"secondary",
  amber:"outline",
  red:"destructive",
  purple:"secondary",
};

const paperStatusVariant: Record<
"green" |"blue" |"amber" |"red",
"default" |"secondary" |"destructive" |"outline"
> = {
  green:"default",
  blue:"secondary",
  amber:"outline",
  red:"destructive",
};

const stats: Array<{ value: string; label: string; tone?: string }> = [
  { value: `${papers.length}`, label:"Papers" },
  { value: `${surveys.length}`, label:"Surveys" },
  { value:"37.3M+", label:"Sources Scored" },
  {
    value: `${(totalAnomalies / 1000).toFixed(0)}K+`,
    label:"Anomalies",
  },
  { value:"424K+", label:"MCMC Samples" },
  {
    value: `${qcPassCount}/${surveys.length}`,
    label:"QC Pass",
    tone:
      qcPassCount === surveys.length
        ? undefined
        :"tone-caution",
  },
  { value:"4", label:"Predictions" },
  {
    value:"50",
    label:"Queued",
    tone:"tone-caution",
  },
];

const exploreLinks: Array<{
  href: string;
  external?: boolean;
  title: string;
  description: string;
}> = [
  {
    href:"/explained",
    title:"Explainer",
    description:"Non-technical guide",
  },
  {
    href:"/glossary",
    title:"Glossary",
    description:"Key terms & equations",
  },
  {
    href:"/timeline",
    title:"Timeline",
    description:"Cosmic history → 2028",
  },
  {
    href:"/speculations",
    title:"Speculations",
    description:"Future research paths",
  },
  {
    href:"https://github.com/Hubify-Projects/bigbounce",
    external: true,
    title:"GitHub",
    description:"Source code & data",
  },
  {
    href:"mailto:houston@hubify.com",
    external: true,
    title:"Contact",
    description:"houston@hubify.com",
  },
];

export default function HomePage() {
  return (
    <>
      <LiveStatus />
      <section className="page-hero">
        <div className="hero-copy">
          <p className="eyebrow" style={{ marginBottom: 10 }}>
            Research Program / Updated {liveStatus.lastUpdatedDisplay}
          </p>
          <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 650 }}>
            Spin-Torsion Cosmology
          </h1>
          <p className="subtitle">
            A live research dossier testing bounce cosmology against inflation
            through archival survey mining, falsifiable signatures, and
            paper-ready evidence trails.
          </p>
          <div className="mt-5 flex flex-wrap gap-2">
            <Button asChild>
              <Link href="/paper">
                Open papers <ArrowRight size={15} />
              </Link>
            </Button>
            <Button asChild variant="outline">
              <Link href="/status">Research status</Link>
            </Button>
          </div>
        </div>
        <div className="hero-panel">
          <div className="hero-panel-header">
            <span>observational ledger</span>
            <Badge variant="accent">
              {papers.length} papers ·{" "}
              {Math.round(
                papers.reduce((s, p) => s + p.readiness, 0) / papers.length,
              )}
              % avg · awaiting Houston sign-off
            </Badge>
          </div>
          <div className="hero-panel-body">
            <div className="signal-row">
              <span>Survey sources scored</span>
              <span className="signal-value">37.3M</span>
            </div>
            <div className="signal-row">
              <span>Catalog anomalies retained</span>
              <span className="signal-value">378K</span>
            </div>
            <div className="signal-row">
              <span>MCMC posterior samples</span>
              <span className="signal-value">424K+</span>
            </div>
            <div className="signal-row">
              <span>Public research artifacts</span>
              <span className="signal-value">7 HF</span>
            </div>
          </div>
        </div>
      </section>

      <div style={{ marginBottom: 24 }}>
        <LivePapersDashboard />
      </div>

      {liveStatus.needsHouston.length > 0 && (
        <section className="section needs-houston" aria-label="Needs Houston">
          <header className="needs-houston-head">
            <AlertTriangle size={14} aria-hidden="true" />
            <span className="needs-houston-kicker">Needs Houston</span>
            <span className="needs-houston-count">
              {liveStatus.needsHouston.length} truly-blocked
              {liveStatus.needsHouston.length === 1 ? " item" : " items"} —
              agents cannot proceed without you
            </span>
          </header>
          <p className="needs-houston-intro">
            Everything else on the site is autonomous and driven by agents.
            This block lists only items that require Houston-only authority:
            personal sign-off, API/SSH credentials, arXiv endorsement, or
            something physical only you can provide.
          </p>
          <ul className="needs-houston-list">
            {liveStatus.needsHouston.map((item) => (
              <li key={item.title}>
                <div className="needs-houston-item-head">
                  <span className="needs-houston-title">{item.title}</span>
                  {item.blockedPaper && (
                    <Badge variant="outline" className="text-xs">
                      gates {item.blockedPaper}
                    </Badge>
                  )}
                </div>
                <p className="needs-houston-line">
                  <span>Why blocked</span>
                  {item.why}
                </p>
                <p className="needs-houston-line">
                  <span>Ask</span>
                  {item.ask}
                </p>
              </li>
            ))}
          </ul>
        </section>
      )}

      <div className="metric-grid">
        {stats.map((stat) => (
          <div className="metric-card" key={stat.label}>
              <div
                className={`metric-value ${stat.tone ??""}`.trim()}
              >
                {stat.value}
              </div>
              <div className="metric-label">{stat.label}</div>
          </div>
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
                    <CardTitle className="flex items-center gap-2 text-sm font-mono">
                      <Orbit size={15} />
                      <MathText>{pred.name}</MathText>
                    </CardTitle>
                    <Badge variant={predStatusVariant[pred.statusVariant]}>
                      {pred.status}
                    </Badge>
                  </div>
                </CardHeader>
                <CardContent className="flex-1">
                  <div className="big-value">
                    <MathText>{pred.value}</MathText>
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
        {/* Single-sourced from data/surveys.ts via SurveyQcTable (shared with /status). */}
        <SurveyQcTable />
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
        <div className="paper-ledger">
          {papers.map((paper) => (
            <Link
              key={paper.slug}
              href={`/papers/${paper.slug}`}
              className="paper-ledger-item"
            >
              <div className="paper-ledger-badge-row">
                <Badge
                  variant={paperStatusVariant[paper.statusVariant]}
                  className="paper-ledger-badge"
                >
                  {paper.readiness}% · {paper.statusVariant === "green"
                    ? "ready"
                    : paper.statusVariant === "blue"
                      ? "active"
                      : paper.statusVariant === "amber"
                        ? "draft"
                        : "blocked"}
                </Badge>
              </div>
              <div className="paper-ledger-main">
                <div className="paper-ledger-kicker">
                  <FileText aria-hidden="true" />
                  <span>Paper {paper.number}</span>
                  <span>{paper.version}</span>
                </div>
                <div className="paper-ledger-title">
                  <MathText>{paper.title}</MathText>
                </div>
                <p
                  style={{
                    fontSize: "0.82rem",
                    color: "var(--text-muted)",
                    margin: "8px 0 8px 0",
                    lineHeight: 1.5,
                  }}
                >
                  {paper.tldr}
                </p>
                <div style={{ marginBottom: 6 }}>
                  <PublicationPathCompact paper={paper} />
                </div>
                <div className="paper-ledger-meta">
                  <span>{paper.target}</span>
                  <span>{paper.pages} pages</span>
                  <span>{paper.refs} refs</span>
                </div>
              </div>
              <div className="paper-ledger-status">
                <div className="paper-ledger-progress">
                  <div
                    className={`paper-ledger-fill ${
                      paper.readiness === 100
                        ?"is-complete"
                        : paper.readiness >= 90
                          ?"is-near"
                          :"is-draft"
                    }`}
                    style={{ width: `${paper.readiness}%` }}
                  />
                </div>
                <span className="paper-ledger-percent">
                  {paper.readiness}%
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Current Focus</h2>
        <Card className="border-l-4 border-l-[var(--accent)]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base font-mono">
              <Database size={16} />
              {liveStatus.headline}
            </CardTitle>
            <CardDescription>
              {liveStatus.summary}
            </CardDescription>
          </CardHeader>
          <CardContent className="pt-0">
            <p className="text-xs uppercase tracking-wide text-muted-foreground mb-2">
              Currently running
            </p>
            <ul className="text-sm space-y-1 list-disc pl-5">
              {liveStatus.currentlyRunning.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </CardContent>
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
                target={link.href.startsWith("http") ?"_blank" : undefined}
                rel={link.href.startsWith("http") ?"noopener" : undefined}
                className="no-underline text-foreground"
              >
                <Card className="text-center transition-colors hover:bg-accent/40">
                  <CardContent className="p-4">
                    <div
                      className="font-mono text-base font-semibold"
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
                      className="font-mono text-base font-semibold"
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
