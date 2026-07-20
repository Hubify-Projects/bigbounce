import { Badge } from"@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
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
import type { Metadata } from"next";
import Link from"next/link";
import { getLivePapers, getRunningPods, displayVersion, type LivePaperState } from "@/lib/livePapers";
import { SurveyQcTable } from "@/components/Cards/SurveyQcTable";

export const metadata: Metadata = {
  title:"Research Status",
  description:
"Master status page: papers, pipelines, MCMC chains, compute pods, and discoveries.",
};

const PAPER_DISPLAY_NAMES: Record<string, { number: string; tagline: string }> = {
  "paper-1a": { number: "P1A", tagline: "ECH channel-level closure + perturbation transparency" },
  "paper-1b": { number: "P1B", tagline: "MCMC companion + tension survey" },
  "paper-2": { number: "P2", tagline: "f_NL = -35/16 forecast (SPHEREx)" },
  "paper-3": { number: "P3", tagline: "Multi-survey anomaly catalogue" },
  "paper-4": { number: "P4", tagline: "Galaxy chirality at 8.47M scale" },
  "paper-5": { number: "P5", tagline: "DESI environmental chirality" },
};

function statusBadgeVariant(state: LivePaperState): "default" | "secondary" | "outline" {
  if (state.openBlockers > 0) return "outline";
  if (state.openMajors > 0) return "secondary";
  return "default";
}

function statusLabel(state: LivePaperState): string {
  if (state.openBlockers > 0) return `${state.openBlockers} BLOCKER${state.openBlockers === 1 ? "" : "s"}`;
  if (state.openMajors > 0) return `${state.openMajors} MAJOR${state.openMajors === 1 ? "" : "s"}`;
  if (state.openMinors > 0) return `${state.openMinors} MINOR${state.openMinors === 1 ? "" : "s"}`;
  return "no recorded open findings";
}

const stats: Array<{ value: string; label: string }> = [
  { value:"6", label:"Papers (P1A, P1B, P2–P5)" },
  {
    value:"424K+",
    label:"MCMC Samples (309,189 frozen · 3rd chain accumulating)",
  },
  {
    value:"37.3M+",
    label:"Sources Scored (8 Surveys)",
  },
  {
    value:"378K+",
    label:"Anomalies Found",
  },
  { value:"8.47M", label:"Galaxy Chirality Labels" },
  { value:"6", label:"AI Pipelines" },
  { value:"6", label:"Bounce Channels" },
];

// Status is statically rendered, so use one stable build timestamp for every
// pod row instead of calling an impure clock during React render.
const BUILD_NOW = Date.now();

export const dynamic = "force-static";

export default async function StatusPage() {
  const [livePapers, runningPods] = await Promise.all([
    getLivePapers(),
    getRunningPods(),
  ]);
  const isLive = livePapers.length > 0 && livePapers[0].source === "convex";
  // Display in PT so the date doesn't read one day ahead for PT-anchored audience
  const renderedAt = new Date().toLocaleString("en-US", {
    timeZone: "America/Los_Angeles",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  }) + " PT";

  const totalOpenBlockers = livePapers.reduce((s, p) => s + p.openBlockers, 0);
  const totalOpenMajors = livePapers.reduce((s, p) => s + p.openMajors, 0);
  const noMajorFindingCount = livePapers.filter(
    (p) => p.openBlockers === 0 && p.openMajors === 0,
  ).length;
  const totalReadiness =
    livePapers.length > 0
      ? Math.round(livePapers.reduce((s, p) => s + p.readinessComputed, 0) / livePapers.length)
      : 0;

  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Rendered at build · {renderedAt} ·{" "}
          {isLive ? (
            <span className="tone-success">live data</span>
          ) : (
            <span className="text-muted-foreground">static fallback</span>
          )}
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Research Program Status
        </h1>
        <p className="subtitle">
          Comprehensive source of truth for the entire BigBounce spin-torsion
          cosmology research program. Paper versions, readiness, and open
          findings counts are updated on every build.
        </p>
      </div>

      <Card className="mt-6">
        <CardHeader>
          <div className="flex items-baseline justify-between gap-2 flex-wrap">
            <CardTitle className="font-mono text-xs font-semibold uppercase tracking-wider" style={{ color: "var(--text-tertiary)" }}>
              <span className="tone-success" aria-hidden="true">● </span>
              Live portfolio status
            </CardTitle>
            <CardDescription className="font-mono text-xs">
              {renderedAt} · {livePapers.length} papers tracked
            </CardDescription>
          </div>
        </CardHeader>
        <CardContent className="space-y-3 text-sm">
          <div className="flex items-center gap-4 flex-wrap">
            <span>
              <strong>{noMajorFindingCount}</strong>/{livePapers.length} with no recorded open BLOCKER/MAJOR
            </span>
            <span className="text-muted-foreground">avg readiness {totalReadiness}%</span>
            <span className="text-muted-foreground">
              {totalOpenBlockers} open BLOCKER{totalOpenBlockers === 1 ? "" : "s"}
            </span>
            <span className="text-muted-foreground">
              {totalOpenMajors} open MAJOR{totalOpenMajors === 1 ? "" : "s"}
            </span>
            <div className="h-2 w-56 overflow-hidden rounded bg-muted">
              <div
                className="h-full progress-fill-success"
                style={{ width: `${Math.min(totalReadiness, 100)}%` }}
              />
            </div>
          </div>
          <div className="status-table-scroll">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Paper</TableHead>
                <TableHead>Version</TableHead>
                <TableHead>Readiness</TableHead>
                <TableHead>Open findings</TableHead>
                <TableHead>Last update</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {livePapers.map((p) => {
                const meta = PAPER_DISPLAY_NAMES[p.slug] ?? {
                  number: p.number,
                  tagline: p.shortTitle,
                };
                return (
                  <TableRow key={p.slug}>
                    <TableCell>
                      <Link
                        href={`/papers/${p.slug}`}
                        className="font-semibold underline-offset-4 hover:underline"
                      >
                        {meta.number}
                      </Link>{" "}
                      <span className="text-muted-foreground">{meta.tagline}</span>
                    </TableCell>
                    <TableCell className="whitespace-nowrap font-mono">{displayVersion(p.currentVersion)}</TableCell>
                    <TableCell className="whitespace-nowrap font-mono">
                      {p.readinessComputed}%
                      <span className="live-papers-bar" aria-hidden="true">
                        <span
                          style={{
                            width: `${p.readinessComputed}%`,
                            background:
                              p.readinessComputed >= 95
                                ? "var(--success)"
                                : p.readinessComputed >= 85
                                  ? "var(--text-secondary)"
                                  : "var(--warn)",
                          }}
                        />
                      </span>
                    </TableCell>
                    <TableCell>
                      <Badge variant={statusBadgeVariant(p)}>{statusLabel(p)}</Badge>
                    </TableCell>
                    <TableCell className="whitespace-nowrap font-mono text-xs text-muted-foreground">
                      {p.lastUpdated ?? "—"}
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
          </div>
          <p className="text-xs text-muted-foreground">
            All six papers remain <strong>IN REVISION</strong>. Zero recorded open findings is
            an inventory state, not proof of scientific closure or publication readiness.
            Readiness values are evidence caps: P1B v1B.0.108 and P4 v1.0.244 have closure
            changes that have not yet been re-reviewed. Remaining gates include independent
            human scientific review, venue-specific checks, and immutable archive/DOI work.
            Automated-model ACCEPT labels are review evidence, not journal acceptance.
          </p>
        </CardContent>
      </Card>

      <div className="mt-6 grid grid-cols-2 gap-3 md:grid-cols-4">
        {stats.map((stat) => (
          <Card key={stat.label}>
            <CardContent className="p-4">
              <div
                className="font-mono text-2xl font-bold"
                style={{ fontFamily:"var(--font-mono-stack)" }}
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
        <h2>Active Compute</h2>
        {runningPods.length === 0 ? (
          <div className="compute-idle">
            <span className="compute-idle-dot" aria-hidden="true" />
            <div>
              <p className="compute-idle-title">0 pods running · $0/hr</p>
              <p className="compute-idle-note">
                All compute jobs idle. Job history + cost accounting live in
                the live research log.
              </p>
            </div>
          </div>
        ) : (
          runningPods.map((pod) => {
            const hoursUp = Math.max(0, (BUILD_NOW - pod.startedAt) / 3.6e6);
            return (
              <Card key={pod.podId} style={{ marginBottom: 12 }}>
                <CardHeader>
                  <CardTitle className="flex flex-wrap items-center gap-2 text-sm">
                    <Badge>{pod.gpu}</Badge>
                    <span className="font-mono">{pod.name}</span>
                    <Badge variant="outline" className="font-mono text-[10px]">
                      {pod.podId}
                    </Badge>
                    <span
                      className="font-mono text-xs text-muted-foreground"
                      style={{ marginLeft: "auto" }}
                    >
                      ${pod.hourlyCostUsd.toFixed(2)}/hr · up{" "}
                      {hoursUp.toFixed(1)}h · ~$
                      {(pod.totalCostUsd + hoursUp * pod.hourlyCostUsd).toFixed(2)}{" "}
                      total
                    </span>
                  </CardTitle>
                  <CardDescription>{pod.purpose}</CardDescription>
                </CardHeader>
                {pod.jobs && pod.jobs.length > 0 && (
                  <CardContent className="p-0">
                    <Table>
                      <TableHeader>
                        <TableRow>
                          <TableHead>Job</TableHead>
                          <TableHead>Paper</TableHead>
                          <TableHead>Status</TableHead>
                          <TableHead>ETA</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {pod.jobs.map((job) => (
                          <TableRow key={job.tmuxSession}>
                            <TableCell className="font-mono text-xs">
                              {job.name}
                            </TableCell>
                            <TableCell className="font-mono text-xs">
                              {job.paper}
                            </TableCell>
                            <TableCell>
                              <Badge
                                variant={
                                  job.status === "running"
                                    ? "default"
                                    : job.status === "done"
                                      ? "secondary"
                                      : "outline"
                                }
                                className="font-mono text-[10px]"
                              >
                                {job.status}
                              </Badge>
                            </TableCell>
                            <TableCell className="text-xs text-muted-foreground">
                              {job.etaNote}
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </CardContent>
                )}
              </Card>
            );
          })
        )}
      </section>

      <section className="section">
        <h2>Paper Portfolio</h2>
        <p className="text-sm text-muted-foreground">
          The live paper table above is the canonical source of truth.
          Per-paper detail and current PDF mirrors live at{" "}
          <a href="/paper" className="underline">
            /paper
          </a>
          .
        </p>
      </section>

      <section className="section">
        <h2>Bounce Channels &amp; Predictions</h2>
        <Card>
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Channel</TableHead>
                  <TableHead>Best Model</TableHead>
                  <TableHead>Prediction</TableHead>
                  <TableHead>Status</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <TableRow>
                  <TableCell className="font-semibold">
                    Galaxy bispectrum f<sub>NL</sub>
                  </TableCell>
                  <TableCell>Matter bounce</TableCell>
                  <TableCell className="font-mono">
                    f<sub>NL</sub> = -35/16 (parameter-free)
                  </TableCell>
                  <TableCell>
                    <Badge variant="secondary">FLAGSHIP</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">
                    Quintom bounce-DE
                  </TableCell>
                  <TableCell>Quintom bounce</TableCell>
                  <TableCell className="font-mono">w(z) crosses -1</TableCell>
                  <TableCell>
                    <Badge variant="outline">DESI DR2 chain: w_pivot = -0.952 ± 0.019 (+2.5σ from -1)</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">NANOGrav GW</TableCell>
                  <TableCell>Matter bounce</TableCell>
                  <TableCell className="font-mono">
                    γ = 3.0 vs 2.567 ± 0.382
                  </TableCell>
                  <TableCell>
                    <Badge variant="default">+1.13σ consistent</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">PBH dark matter</TableCell>
                  <TableCell>Asymmetric matter bounce</TableCell>
                  <TableCell className="font-mono">Asteroid-mass PBHs</TableCell>
                  <TableCell>
                    <Badge variant="outline">Viable</Badge>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </section>

      <section className="section">
        <h2>Completed Surveys (8 total)</h2>
        {/* Single-sourced from data/surveys.ts via SurveyQcTable — never
            hardcode QC verdicts here (previously contradicted /surveys). */}
        <SurveyQcTable />
      </section>

      <section className="section">
        <h2>Key Discoveries</h2>
        <div className="grid md:grid-cols-2 gap-x-10">
          <div className="flat-item-list">
            <div className="py-4">
              <p className="font-semibold font-mono text-sm mb-0.5">
                f_NL = -35/16 Mechanism Independence
              </p>
              <p className="font-mono text-[11px] text-muted-foreground mb-2">
                Paper 2 · quintom_fnl_verification.py
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Verified across 3 bounce models: f_NL = -2.1875 is parameter-free
                and mechanism-independent. SPHEREx (~2028) will measure to σ ~
                0.7-2.
              </p>
            </div>
            <div className="py-4">
              <p className="font-semibold font-mono text-sm mb-0.5">
                NANOGrav Consistency
              </p>
              <p className="font-mono text-[11px] text-muted-foreground mb-2">
                nanograv real-KDE free-spectrum re-fit (Zenodo chains, emcee)
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Matter bounce γ = 3.0 vs NANOGrav real-KDE free-spectrum 2.567 ± 0.382 (+1.13σ consistent); SMBHB γ = 4.33 excluded at +4.61σ. Savage-Dickey decisively favors the bounce slope.
              </p>
            </div>
          </div>
          <div className="flat-item-list">
            <div className="py-4">
              <p className="font-semibold font-mono text-sm mb-0.5">
                Quintom w-Crossing — Theoretical Only
              </p>
              <p className="font-mono text-[11px] text-muted-foreground mb-2">
                Paper 1A model-discrimination table · zero free-w0–wa samples in our chains
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Whether w(z) crosses -1 is a quintom-bounce signature, but our
                program has not yet run a free-w<sub>0</sub>–w<sub>a</sub>{" "}
                MCMC. External DESI DR2 (Adame et al.) reports 2.8–4.2σ for
                w-crossing depending on dataset combination. (An earlier
                in-house claim of P(quintom-B) = 98.6% was traced to a
                bookkeeping error in an automated run and retracted.)
              </p>
            </div>
            <div className="py-4">
              <p className="font-semibold font-mono text-sm mb-0.5">
                Public-ID Recovery of a Historical DESI DR1 Anomaly List
              </p>
              <p className="font-mono text-[11px] text-muted-foreground mb-2">
                Paper 3 (v3.2.0-r10) · 181 TARGETIDs recovered · archive-recovery product
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Paper 3 recovers 181 public DESI DR1 TARGETIDs from a frozen
                historical anomaly list (170 high-coordinate-consistency core + 11
                lower-confidence) — an archive-recovery / provenance product,
                explicitly not a purity, novelty, or detection claim. The
                exploratory autoencoder pipeline that produced the candidate list
                is browsable separately.
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
