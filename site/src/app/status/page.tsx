import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
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
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Research Status",
  description:
    "Master status page: papers, pipelines, MCMC chains, compute pods, and discoveries.",
};

const stats: Array<{ value: string; label: string; tone: string }> = [
  { value: "4", label: "Papers", tone: "text-emerald-600 dark:text-emerald-400" },
  {
    value: "424K+",
    label: "MCMC Samples (3 frozen datasets)",
    tone: "text-emerald-600 dark:text-emerald-400",
  },
  {
    value: "37.3M+",
    label: "Sources Scored (8 Surveys)",
    tone: "text-emerald-600 dark:text-emerald-400",
  },
  {
    value: "319K+",
    label: "Anomalies Found",
    tone: "text-emerald-600 dark:text-emerald-400",
  },
  { value: "6", label: "AI Pipelines", tone: "text-blue-600 dark:text-blue-400" },
  {
    value: "14",
    label: "Computation Scripts",
    tone: "text-blue-600 dark:text-blue-400",
  },
  {
    value: "6",
    label: "Bounce Channels",
    tone: "text-amber-600 dark:text-amber-400",
  },
];

export default function StatusPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Last Updated: May 1, 2026 · 02:55 PDT
        </p>
        <h1 style={{ fontFamily: "var(--font-serif)", fontWeight: 600 }}>
          Research Program Status
        </h1>
        <p className="subtitle">
          Comprehensive source of truth for the entire BigBounce spin-torsion
          cosmology research program.
        </p>
      </div>

      <Card className="mt-6 border-l-4 border-l-emerald-500">
        <CardHeader>
          <div className="flex items-baseline justify-between gap-2 flex-wrap">
            <CardTitle className="text-sm font-bold uppercase tracking-wider text-emerald-700 dark:text-emerald-400">
              R42 4-LLM Adversarial Peer Review · Closure Sprint
            </CardTitle>
            <CardDescription className="font-mono text-xs">
              Updated 2026-05-01 02:55 PDT
            </CardDescription>
          </div>
        </CardHeader>
        <CardContent className="space-y-3 text-sm">
          <div className="flex items-center gap-3">
            <strong>23 of 23 BLOCKERs CLOSED</strong>
            <span className="text-muted-foreground">100%</span>
            <div className="h-2 w-56 overflow-hidden rounded bg-muted">
              <div className="h-full bg-emerald-500" style={{ width: "100%" }} />
            </div>
          </div>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Paper</TableHead>
                <TableHead>Version</TableHead>
                <TableHead>R42 Status</TableHead>
                <TableHead>Open Items</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow>
                <TableCell><strong>P1</strong> Spin-Torsion</TableCell>
                <TableCell className="font-mono">v2.2.0</TableCell>
                <TableCell><Badge className="bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">CLOSED</Badge></TableCell>
                <TableCell>—</TableCell>
              </TableRow>
              <TableRow>
                <TableCell><strong>P2</strong> f<sub>NL</sub> Forecast</TableCell>
                <TableCell className="font-mono">v1.7.5</TableCell>
                <TableCell><Badge className="bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">CLOSED</Badge></TableCell>
                <TableCell>—</TableCell>
              </TableRow>
              <TableRow>
                <TableCell><strong>P3</strong> Anomaly Catalog</TableCell>
                <TableCell className="font-mono">v3.1.5</TableCell>
                <TableCell><Badge className="bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">CLOSED</Badge></TableCell>
                <TableCell>—</TableCell>
              </TableRow>
              <TableRow>
                <TableCell><strong>P4</strong> Chirality Catalog</TableCell>
                <TableCell className="font-mono">v1.0.5</TableCell>
                <TableCell><Badge className="bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">CLOSED</Badge></TableCell>
                <TableCell>—</TableCell>
              </TableRow>
            </TableBody>
          </Table>
          <div className="space-y-1 text-muted-foreground">
            <p><strong className="text-foreground">B20 result:</strong> 240,919 GZ1 galaxies cross-matched (95.45%). Three-class accuracy on independent GZ1 = <strong>58.71%</strong>; spiral-only CW vs CCW = <strong>69.91%</strong> on 117,205 spirals.</p>
            <p><strong className="text-foreground">B21 result:</strong> Of 53,862 NOT_SPIRAL galaxies in raw classification, <strong>51,694 (95.97%)</strong> stayed NOT_SPIRAL after equivariance averaging; CW/CCW leakage balanced (1,066 vs 1,102, Δ=0.07%).</p>
            <p><strong className="text-foreground">Pod:</strong> <code className="font-mono text-xs">regular_green_pig-migration</code> @ 38.80.152.148:33089 · cross-match completed in 73 s.</p>
            <p><strong className="text-foreground">B23:</strong> All five HuggingFace artifacts are <strong className="text-emerald-700 dark:text-emerald-400">PUBLIC</strong>:{" "}
              <a className="underline" href="https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog" target="_blank" rel="noopener noreferrer"><code>galaxy-chirality-catalog</code></a> (8.47M predictions),{" "}
              <a className="underline" href="https://huggingface.co/bamfai/galaxy-chirality-v2" target="_blank" rel="noopener noreferrer"><code>galaxy-chirality-v2</code></a> (ViT-Small model),{" "}
              <a className="underline" href="https://huggingface.co/bamfai/desi-spectral-anomaly-detector" target="_blank" rel="noopener noreferrer"><code>desi-spectral-anomaly-detector</code></a> (BigAE),{" "}
              <a className="underline" href="https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog" target="_blank" rel="noopener noreferrer"><code>bigbounce-anomaly-catalog</code></a> (319K anomalies),{" "}
              <a className="underline" href="https://huggingface.co/datasets/bamfai/bigbounce-mcmc" target="_blank" rel="noopener noreferrer"><code>bigbounce-mcmc</code></a> (424K MCMC samples).</p>
            <p><strong className="text-emerald-700 dark:text-emerald-400">BUNDLE READY-TO-SEND. All 23 R42 BLOCKERs CLOSED.</strong> Next phase on pod: 5-seed BigAE ensemble + second-level AE (16D) on the 100K DESI OOD set — produces ensemble error bars on B10 and a ranked ultra-rare anomaly catalog for Paper 3 §X. ~2–3 h wall.</p>
          </div>
        </CardContent>
      </Card>

      <div className="mt-6 grid grid-cols-2 gap-3 md:grid-cols-4">
        {stats.map((stat) => (
          <Card key={stat.label}>
            <CardContent className="p-4">
              <div
                className={`font-mono text-2xl font-bold ${stat.tone}`}
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
        <h2>1. Research Papers</h2>
        <Card>
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Paper</TableHead>
                  <TableHead>Title</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead>Pages</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <TableRow>
                  <TableCell className="font-semibold">Paper 1</TableCell>
                  <TableCell>
                    Spin-Torsion Framework: 14 Barriers, Falsifiable Predictions
                  </TableCell>
                  <TableCell>
                    <Badge variant="default">99% Ready</Badge>
                  </TableCell>
                  <TableCell className="font-mono">~24</TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">Paper 2</TableCell>
                  <TableCell>
                    f<sub>NL</sub> = -35/8 Forecast: SPHEREx Discrimination
                  </TableCell>
                  <TableCell>
                    <Badge variant="default">Submission-Ready</Badge>
                  </TableCell>
                  <TableCell className="font-mono">~12</TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">Paper 3</TableCell>
                  <TableCell>
                    Multi-Survey Anomaly Catalog: 319K from 37.3M Sources
                  </TableCell>
                  <TableCell>
                    <Badge variant="secondary">Draft (~95%)</Badge>
                  </TableCell>
                  <TableCell className="font-mono">~18</TableCell>
                </TableRow>
                <TableRow>
                  <TableCell className="font-semibold">Paper 4</TableCell>
                  <TableCell>
                    Galaxy Chirality at Scale: 8.47M Galaxies
                  </TableCell>
                  <TableCell>
                    <Badge variant="secondary">Draft (~85%)</Badge>
                  </TableCell>
                  <TableCell className="font-mono">~11</TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
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
          <Card className="border-l-4 border-l-emerald-500">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily: "var(--font-serif)" }}
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

          <Card className="border-l-4 border-l-amber-500">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily: "var(--font-serif)" }}
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
                program has not yet run a free-w<sub>0</sub>–w<sub>a</sub>{" "}
                MCMC. External DESI DR2 (Adame et al.) reports 2.8–4.2σ for
                w-crossing depending on dataset combination. (Earlier in-house
                claim P(quintom-B) = 98.6% from 50.9K samples was a fire #21
                bookkeeping confabulation, corrected fire #25.)
              </p>
            </CardContent>
          </Card>

          <Card className="border-l-4 border-l-blue-500">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily: "var(--font-serif)" }}
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

          <Card className="border-l-4 border-l-emerald-500">
            <CardHeader className="pb-2">
              <CardTitle
                className="text-base"
                style={{ fontFamily: "var(--font-serif)" }}
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
