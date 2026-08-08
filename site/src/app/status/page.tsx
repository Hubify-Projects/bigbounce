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
import { getPaperBySlug } from "@/data/papers";
import { readinessBreakdown, readinessBreakdownNote, publishingPhase, type GateOwner } from "@/data/readinessBreakdown";
import { SurveyQcTable } from "@/components/Cards/SurveyQcTable";

export const metadata: Metadata = {
  title:"Research Status",
  description:
"Current research-program, artifact, and editorial status for BigBounce.",
};

// Taglines are the plain-English purpose label from data/papers.ts (directive
// Q3) — never hand-write a second copy here. Role prefixes carried over from
// the previous hardcoded strings (P3's "Integrated Supporting Data Release",
// P5's "Standalone AJ companion") are preserved in front of the plain label.
function taglineFor(slug: string, rolePrefix?: string): string {
  const plainTitle = getPaperBySlug(slug)?.plainTitle ?? "";
  return rolePrefix ? `${rolePrefix} · ${plainTitle}` : plainTitle;
}

const PAPER_DISPLAY_NAMES: Record<string, { number: string; tagline: string }> = {
  "paper-1a": { number: "P1A", tagline: taglineFor("paper-1a") },
  "paper-1b": { number: "P1B", tagline: taglineFor("paper-1b") },
  "paper-2": { number: "P2", tagline: taglineFor("paper-2") },
  "paper-3": { number: "P3", tagline: taglineFor("paper-3", "Integrated Supporting Data Release") },
  "paper-4": { number: "P4", tagline: taglineFor("paper-4") },
  "paper-5": { number: "P5", tagline: taglineFor("paper-5", "Standalone AJ companion") },
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
  { value:"3", label:"Question-first research programs" },
  {
    value:"P2",
    label:"Lead bounce-theory result" ,
  },
  {
    value:"P4",
    label:"Lead galaxy-chirality result",
  },
  {
    value:"P3",
    label:"Integrated DESI Public-ID Recovery release",
  },
  { value:"P5", label:"Standalone AJ chirality companion" },
  { value:"Legacy", label:"Survey-pipeline records preserved as archive evidence" },
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
  const renderedAt = new Date(BUILD_NOW).toLocaleString("en-US", {
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
          cosmology research program. The three research questions lead; artifact
          versions and review evidence below document their supporting work.
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
              {renderedAt} · {livePapers.length} versioned artifacts tracked
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
                <TableHead>Artifact</TableHead>
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
            Readiness follows <strong>directive P</strong> (2026-07-23): the headline % is
            package and review evidence, not a scientific endorsement, standalone-submission
            decision, journal acceptance, or proof that every tracked artifact is a flagship.
            P3 is an integrated Supporting Data Release; P5 is the standalone AJ companion.
          </p>
        </CardContent>
      </Card>

      {/* Readiness breakdown — Houston 2026-07-23: one clear publication-readiness
          number per paper, decomposed into named gates with explicit owners so it
          is obvious what KIND of work remains (none of it is science/compute). */}
      <Card className="mt-6">
        <CardContent className="pt-6">
          <h2 className="mb-1 font-mono text-lg font-semibold" style={{ fontFamily: "var(--font-mono-stack)" }}>
            What &ldquo;ready&rdquo; means — five gates per paper (directive P)
          </h2>
          <p className="mb-4 text-sm text-muted-foreground">{readinessBreakdownNote}</p>
          <div className="space-y-5">
            {readinessBreakdown.map((p) => (
              <div key={p.code}>
                <div className="mb-1 flex items-baseline gap-3">
                  <span className="font-mono font-bold" style={{ fontFamily: "var(--font-mono-stack)" }}>{p.code}</span>
                  <span className="text-sm text-muted-foreground">publication readiness (evidence-capped): <strong>{p.publicationReadiness}%</strong></span>
                </div>
                <div className="grid gap-x-6 gap-y-1 text-xs md:grid-cols-2">
                  {p.gates.map((g) => (
                    <div key={g.dimension} className="flex items-baseline gap-2">
                      <span className="whitespace-nowrap font-mono" style={{ fontFamily: "var(--font-mono-stack)" }}>
                        {g.score}% <span className="text-muted-foreground">(×{g.weight})</span>
                      </span>
                      <span className="whitespace-nowrap font-semibold">{g.dimension}</span>
                      <span className="whitespace-nowrap uppercase tracking-wide" style={{ color: ({ done: "var(--success)", agent: "var(--text-secondary)", houston: "var(--warn)", external: "var(--text-muted)" } as Record<GateOwner, string>)[g.owner] }}>
                        {g.owner === "done" ? "complete" : `owner: ${g.owner}`}
                      </span>
                      <span className="text-muted-foreground">{g.status}</span>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
          <h3 className="mb-1 mt-6 font-mono text-base font-semibold" style={{ fontFamily: "var(--font-mono-stack)" }}>
            Publishing phase — next steps, NOT part of the readiness score
          </h3>
          <div className="space-y-1 text-xs">
            {publishingPhase.map((s) => (
              <div key={s.step} className="flex items-baseline gap-2">
                <span className="whitespace-nowrap font-semibold">{s.step}</span>
                <span className="whitespace-nowrap uppercase tracking-wide" style={{ color: ({ done: "var(--success)", agent: "var(--text-secondary)", houston: "var(--warn)", external: "var(--text-muted)" } as Record<GateOwner, string>)[s.owner] }}>
                  owner: {s.owner}
                </span>
                <span className="text-muted-foreground">{s.status}</span>
              </div>
            ))}
          </div>
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
        <h2>Research programs and artifacts</h2>
        <p className="text-sm text-muted-foreground">
          The live artifact table above preserves version and review evidence. The
          portfolio is organized around three question-first programs; P3 is an
          integrated Supporting Data Release rather than a standalone anomaly
          flagship. Current PDFs and artifact detail live at{" "}
          <a href="/paper" className="underline">
            /paper
          </a>
          .
        </p>
      </section>

      <section className="section">
        <h2>Predictions and boundaries</h2>
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
                    f<sub>NL</sub> = -35/16 (stated P2 assumptions)
                  </TableCell>
                  <TableCell>
                    <Badge variant="secondary">P2 lead result</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">
                    Quintom bounce-DE
                  </TableCell>
                  <TableCell>Quintom bounce</TableCell>
                  <TableCell className="font-mono">w(z) crosses -1</TableCell>
                  <TableCell>
                    <Badge variant="outline">theoretical program; no in-house free-w0–wa result</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">NANOGrav GW</TableCell>
                  <TableCell>Matter bounce</TableCell>
                  <TableCell className="font-mono">
                    γ = 3.0 vs 2.567 ± 0.382
                  </TableCell>
                  <TableCell>
                    <Badge variant="default">legacy consistency comparison; not a detection</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">PBH dark matter</TableCell>
                  <TableCell>Asymmetric matter bounce</TableCell>
                  <TableCell className="font-mono">Asteroid-mass PBHs</TableCell>
                  <TableCell>
                    <Badge variant="outline">theoretical possibility</Badge>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </section>

      <section className="section">
        <h2>Legacy survey-pipeline records</h2>
        <p className="mb-4 text-sm text-muted-foreground">
          These are preserved methodology and archive records. Their historic candidate counts
          are superseded as current portfolio results; no survey result here proves a bounce.
        </p>
        {/* Single-sourced from data/surveys.ts via SurveyQcTable — never
            hardcode QC verdicts here (previously contradicted /surveys). */}
        <SurveyQcTable />
      </section>

      <section className="section">
        <h2>Program evidence and boundaries</h2>
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
                P2 presents the matter-contraction prediction f_NL = -2.1875 under
                its stated assumptions. A future measurement may test that prediction;
                it is not a present observational detection of a bounce.
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
                This legacy model-comparison note reports a compatible simplified slope
                comparison. It is neither a bounce detection nor a basis for selecting a
                publication flagship.
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
                P3 · Integrated Supporting Data Release · 181 TARGETIDs recovered
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                P3 preserves 181 public DESI DR1 TARGETIDs from a frozen
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
