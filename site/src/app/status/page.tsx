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
import { getLivePapers, type LivePaperState } from "@/lib/livePapers";

export const metadata: Metadata = {
  title:"Research Status",
  description:
"Master status page: papers, pipelines, MCMC chains, compute pods, and discoveries.",
};

const PAPER_DISPLAY_NAMES: Record<string, { number: string; tagline: string }> = {
  "paper-1a": { number: "P1A", tagline: "Spin-torsion ECH no-go framework" },
  "paper-1b": { number: "P1B", tagline: "MCMC companion + tension survey" },
  "paper-2": { number: "P2", tagline: "f_NL = -35/8 forecast (SPHEREx)" },
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
  return "clean";
}

const stats: Array<{ value: string; label: string }> = [
  { value:"6", label:"Papers (P1A, P1B, P2–P5)" },
  {
    value:"424K+",
    label:"MCMC Samples (3 frozen datasets)",
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

export const dynamic = "force-static";

export default async function StatusPage() {
  const livePapers = await getLivePapers();
  const isLive = livePapers.length > 0 && livePapers[0].source === "convex";
  const renderedAt = new Date().toISOString().slice(0, 16).replace("T", " ") + " UTC";

  const totalOpenBlockers = livePapers.reduce((s, p) => s + p.openBlockers, 0);
  const totalOpenMajors = livePapers.reduce((s, p) => s + p.openMajors, 0);
  const cleanCount = livePapers.filter(
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
            <span className="tone-success">live Convex data</span>
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
          findings counts come from Convex on every build.
        </p>
      </div>

      <Card className="mt-6 border-l-4 border-tone-success">
        <CardHeader>
          <div className="flex items-baseline justify-between gap-2 flex-wrap">
            <CardTitle className="text-sm font-bold uppercase tracking-wider tone-success">
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
              <strong>{cleanCount}</strong>/{livePapers.length} papers clean
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
                      <strong>{meta.number}</strong>{" "}
                      <span className="text-muted-foreground">{meta.tagline}</span>
                    </TableCell>
                    <TableCell className="font-mono">{p.currentVersion ?? "—"}</TableCell>
                    <TableCell className="font-mono">{p.readinessComputed}%</TableCell>
                    <TableCell>
                      <Badge variant={statusBadgeVariant(p)}>{statusLabel(p)}</Badge>
                    </TableCell>
                    <TableCell className="font-mono text-xs text-muted-foreground">
                      {p.lastUpdated ?? "—"}
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
          <p className="text-xs text-muted-foreground">
            Self-claim readiness ceiling is 95% pre-sign-off and 99% once a
            clean cross-vendor R-round + Houston sign-off close together. The
            final 1% is never awarded by the cron — only by Houston.
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
        <h2>1. Bounce Cosmology Portfolio</h2>
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
        <h2>2. Bounce Cosmology Portfolio</h2>
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
                    f<sub>NL</sub> = -35/8 (parameter-free)
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
                    <Badge variant="outline">Theoretical (no in-house MCMC yet)</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">NANOGrav GW</TableCell>
                  <TableCell>Matter bounce</TableCell>
                  <TableCell className="font-mono">
                    γ = 3.0 vs 3.20 ± 0.42
                  </TableCell>
                  <TableCell>
                    <Badge variant="default">0.48σ consistent</Badge>
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
        <h2>3. Completed Surveys (8 total)</h2>
        <Card>
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Survey</TableHead>
                  <TableHead>Sources</TableHead>
                  <TableHead>Anomalies</TableHead>
                  <TableHead>QC Status</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <TableRow>
                  <TableCell className="font-semibold">DESI DR1</TableCell>
                  <TableCell>22.5M spectra</TableCell>
                  <TableCell className="font-mono">195,829 (0.87%)</TableCell>
                  <TableCell>
                    <Badge variant="default">PASS</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">SDSS DR18</TableCell>
                  <TableCell>2.3M spectra</TableCell>
                  <TableCell className="font-mono">77,905 (3.4%)</TableCell>
                  <TableCell>
                    <Badge variant="outline">Caution: domain shift</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">LAMOST DR10</TableCell>
                  <TableCell>11.4M spectra</TableCell>
                  <TableCell className="font-mono">44,075 (0.39%)</TableCell>
                  <TableCell>
                    <Badge variant="outline">Caution: blue-excess bias</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">eROSITA DR1</TableCell>
                  <TableCell>930K X-ray</TableCell>
                  <TableCell className="font-mono">298 (0.03%, BigAE top-cut)</TableCell>
                  <TableCell>
                    <Badge variant="default">PASS</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">Planck CMB</TableCell>
                  <TableCell>20K patches</TableCell>
                  <TableCell className="font-mono">200</TableCell>
                  <TableCell>
                    <Badge variant="destructive">FAIL: galactic contamination</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">ACT DR6</TableCell>
                  <TableCell>20K patches</TableCell>
                  <TableCell className="font-mono">200</TableCell>
                  <TableCell>
                    <Badge variant="destructive">FAIL: undertrained</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">NEOWISE</TableCell>
                  <TableCell>43.5K sources</TableCell>
                  <TableCell className="font-mono">436</TableCell>
                  <TableCell>
                    <Badge variant="destructive">FAIL: ecliptic systematic</Badge>
                  </TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">Gaia DR3</TableCell>
                  <TableCell>50K variables</TableCell>
                  <TableCell className="font-mono">500</TableCell>
                  <TableCell>
                    <Badge variant="outline">Needs 10x expansion</Badge>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </section>

      <section className="section">
        <h2>4. Key Discoveries</h2>
        <div className="grid gap-3 md:grid-cols-2">
          <Card className="border-l-4 border-tone-success">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily:"var(--font-mono-stack)" }}
              >
                f_NL = -35/8 Mechanism Independence
              </CardTitle>
              <CardDescription className="font-mono text-[11px]">
                Paper 2 · quintom_fnl_verification.py
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Verified across 3 bounce models: f_NL = -4.375 is parameter-free
                and mechanism-independent. SPHEREx (~2028) will measure to σ ~
                0.7-2.
              </p>
            </CardContent>
          </Card>

          <Card className="border-l-4 border-tone-caution">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily:"var(--font-mono-stack)" }}
              >
                Quintom w-Crossing — Theoretical Only
              </CardTitle>
              <CardDescription className="font-mono text-[11px]">
                Paper 1 §VII.H · zero free-w0–wa samples in our chains
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Whether w(z) crosses -1 is a quintom-bounce signature, but our
                program has not yet run a free-w<sub>0</sub>–w<sub>a</sub>{""}
                MCMC. External DESI DR2 (Adame et al.) reports 2.8–4.2σ for
                w-crossing depending on dataset combination. (Earlier in-house
                claim P(quintom-B) = 98.6% from 50.9K samples was a fire #21
                bookkeeping confabulation, corrected fire #25.)
              </p>
            </CardContent>
          </Card>

          <Card className="border-l-4 border-tone-muted">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily:"var(--font-mono-stack)" }}
              >
                NANOGrav Consistency
              </CardTitle>
              <CardDescription className="font-mono text-[11px]">
                nanograv_model_comparison.py · v2b Fisher recompute
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Matter bounce γ = 3.0 vs NANOGrav 3.20 ± 0.42 (0.48σ). Bayesian:
                bounce preferred 5.6:1 over SMBH.
              </p>
            </CardContent>
          </Card>

          <Card className="border-l-4 border-tone-success">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily:"var(--font-mono-stack)" }}
              >
                319,443 Anomalies Across 8 Surveys
              </CardTitle>
              <CardDescription className="font-mono text-[11px]">
                Pipeline B · 37.3M sources · Paper 3 Table 1 canonical totals
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm leading-relaxed text-muted-foreground">
                First multi-survey AI anomaly sweep. 6.1% f_NL improvement via
                latent-space multi-tracer. SPHEREx 4.38σ forecast.
              </p>
            </CardContent>
          </Card>
        </div>
      </section>
    </>
  );
}
