import { papers, getPaperBySlug } from"@/data/papers";
import { Badge } from"@/components/ui/badge";
import { Button } from"@/components/ui/button";
import { MathText } from"@/components/MathText";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
} from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import {
  Tabs,
  TabsList,
  TabsTrigger,
  TabsContent,
} from"@/components/ui/tabs";
import { Alert, AlertTitle, AlertDescription } from"@/components/ui/alert";
import { ExternalReviewPanel } from"@/components/ExternalReviewPanel";
import { Download, ExternalLink, FileText } from"lucide-react";
import Link from"next/link";
import { notFound } from"next/navigation";
import type { Metadata } from"next";

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
  if (!paper) return { title:"Not Found" };
  return {
    title: `Paper ${paper.number}`,
    description: paper.title,
  };
}

const statusVariantMap: Record<
  string,
"default" |"secondary" |"destructive" |"outline"
> = {
  green:"default",
  blue:"secondary",
  amber:"outline",
  red:"destructive",
};

function readinessColor(pct: number) {
  if (pct === 100) return"progress-fill-success";
  if (pct >= 90) return"progress-fill-near";
  return"progress-fill-caution";
}

export default async function PaperDetailPage({
  params,
}: {
  params: PageParams;
}) {
  const { slug } = await params;
  const paper = getPaperBySlug(slug);
  if (!paper) notFound();

  const pdfArtifact = paper.artifacts.find(
    (a) => a.kind === "primary" && a.href.toLowerCase().endsWith(".pdf"),
  );
  const downloadArtifact = paper.artifacts.find(
    (a) => a.download && a.href.toLowerCase().endsWith(".pdf"),
  );
  const supplementaryArtifacts = paper.artifacts.filter(
    (a) => a !== pdfArtifact && a !== downloadArtifact,
  );

  return (
    <>
      <div className="paper-detail-hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          <Link
            href="/paper"
            style={{ color:"var(--text-muted)", textDecoration:"none" }}
          >
            Papers
          </Link>{""}
          &rarr; Paper {paper.number}
        </p>
        <div className="paper-detail-grid grid gap-5 lg:grid-cols-[minmax(0,1fr)_360px]">
          <div className="paper-detail-copy">
            <div className="paper-detail-kicker flex flex-wrap gap-2">
              <span>Paper {paper.number}</span>
              <span>{paper.preprintId}</span>
            </div>
            <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
              Paper {paper.number}
            </h1>
            <p className="subtitle"><MathText>{paper.title}</MathText></p>
            <div className="mt-4 flex flex-wrap items-center gap-2">
              <Badge variant={statusVariantMap[paper.statusVariant]}>
                {paper.readiness}% · {paper.statusVariant === "green" ? "ready" : paper.statusVariant === "blue" ? "active" : paper.statusVariant === "amber" ? "draft" : "blocked"}
              </Badge>
              <Badge variant="outline">{paper.version}</Badge>
              <Badge variant="outline">{paper.pages} pages</Badge>
              <Badge variant="outline">{paper.refs} refs</Badge>
              <Badge variant="outline">Target: {paper.target}</Badge>
            </div>
            <p style={{ marginTop: 14, fontSize: "0.92rem", color: "var(--text-muted)", lineHeight: 1.55 }}>
              {paper.tldr}
            </p>
            {(pdfArtifact || downloadArtifact) && (
              <div className="mt-4 flex flex-wrap gap-2">
                {pdfArtifact && (
                  <Button asChild size="default">
                    <a
                      href={pdfArtifact.href}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <FileText size={16} />
                      Read PDF
                    </a>
                  </Button>
                )}
                {downloadArtifact && (
                  <Button asChild size="default" variant="outline">
                    <a href={downloadArtifact.href} download>
                      <Download size={16} />
                      Download PDF
                    </a>
                  </Button>
                )}
              </div>
            )}
          </div>
          <Card className="paper-artifact-card">
            <CardHeader>
              <CardTitle className="text-sm">Paper Artifacts</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="paper-artifact-meta">
                <span>{paper.pdfMeta}</span>
                <span>{paper.target}</span>
              </div>
              <div className="paper-artifact-actions flex flex-wrap gap-2">
                {pdfArtifact && (
                  <Button asChild size="sm">
                    <a
                      href={pdfArtifact.href}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <FileText size={14} />
                      {pdfArtifact.label}
                    </a>
                  </Button>
                )}
                {downloadArtifact && (
                  <Button asChild size="sm" variant="outline">
                    <a href={downloadArtifact.href} download>
                      <Download size={14} />
                      {downloadArtifact.label}
                    </a>
                  </Button>
                )}
                {supplementaryArtifacts.map((artifact) => (
                  <Button
                    key={`${artifact.href}-${artifact.label}`}
                    asChild
                    size="sm"
                    variant="outline"
                  >
                    <a
                      href={artifact.href}
                      target={artifact.external ? "_blank" : undefined}
                      rel={artifact.external ? "noopener noreferrer" : undefined}
                      download={artifact.download ? true : undefined}
                    >
                      {artifact.label}
                      {artifact.external && <ExternalLink size={12} />}
                    </a>
                  </Button>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      <div className="paper-readiness grid gap-2">
        <div className="paper-readiness-head flex items-baseline justify-between gap-3">
          <span>Readiness</span>
          <strong>{paper.readiness}%</strong>
        </div>
        <div className="paper-readiness-track h-2.5 overflow-hidden rounded-full bg-border">
          <div
            className={`paper-readiness-fill ${readinessColor(paper.readiness)}`}
            style={{ width: `${paper.readiness}%` }}
          />
        </div>
      </div>

      <Card className="paper-summary-card">
        <CardContent>
          <p className="paper-summary"><MathText>{paper.description}</MathText></p>
        </CardContent>
      </Card>

      {paper.blockingItems && paper.blockingItems.length > 0 && (
        <Card className="paper-summary-card" style={{ marginTop: 16 }}>
          <CardHeader>
            <CardTitle className="text-sm font-mono" style={{ textTransform: "uppercase", letterSpacing: "0.06em", color: "var(--text-muted)" }}>
              What&apos;s gating 100%
            </CardTitle>
          </CardHeader>
          <CardContent>
            <ul style={{ margin: 0, paddingLeft: 20, fontSize: "0.88rem", lineHeight: 1.6 }}>
              {paper.blockingItems.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}

      {(() => {
        const texArtifact = paper.artifacts.find((a) => a.label?.toLowerCase().includes("latex"));
        const texPath = texArtifact?.href.replace(/^https:\/\/github\.com\/[^/]+\/[^/]+\/blob\/[^/]+\//, "") ?? "";
        const pdfArt = paper.artifacts.find((a) => a.kind === "primary" && a.href.toLowerCase().endsWith(".pdf"));
        const focus: Record<string, string[]> = {
          "paper-1a": [
            "14-barrier no-go structure (Sec. III + Appendix)",
            "ALP birefringence β=0.27° prediction vs Eskilt 0.342°±0.094° observed",
            "Perturbation-transparency theorem in §IV.D",
            "Mercuri-Capozziello phase-space-vs-loop framing at §II.C.1 (post-R23)",
          ],
          "paper-1b": [
            "309,189 MCMC posterior samples across 2 converged dataset combinations (176,240 full-tension + 132,949 Planck+BAO+SN)",
            "ΔNeff ≈ 0 result and H_0 = 67.68 ΛCDM-consistent",
            "NaMaster pseudo-C_ℓ pipeline 500 MC recovery at SNR=20.32σ",
            "Spectator-ALP carved-out regime (f_a ~ M_Pl, m ~ H_0) — explicit parameter-restriction where Ω_φ ≪ Ω_crit holds",
          ],
          "paper-2": [
            "f_NL = -35/8 = -4.375 parameter-free bounce prediction",
            "Heinrich+2023 σ(f_NL)=0.7 externalization vs own Fisher",
            "Detection significance 3-5σ post-systematic-budget",
            "DBI category-error closure at §IV (post-R22 Gemini)",
          ],
          "paper-3": [
            "378,280 anomalies headline (=378,080 + 200) across 7 surveys",
            "7-way 5″ positional FoF dedup arithmetic (10,213 = 637 + 9,576)",
            "Fisher-positivity caveats in §6 — canonical 1σ envelope σ(f_NL) ∈ [3.92, 8.98] under 1/σ² = F_0 + c·α² (NOT the retracted symmetric ±2.37 form)",
            "σ(f_NL)=8.14 central at empirical α=0.19 jackknife (jk dispersion 0.65) at <1σ from null",
            "v3.1.64 conclusions retracted-Fisher-form text fix — §sec:conclusion now matches §sec:fnl canonical envelope framing",
            "NANOGrav 15-yr γ = 2.567 ± 0.382 (real-KDE Zenodo emcee fit); matter-bounce γ=3.0 at +1.13σ; SMBHB γ=4.33 at +4.61σ",
          ],
          "paper-4": [
            "Subsample-mask −0.12σ MASTER-deconvolved load-bearing null",
            "v1.0.139 joint nuisance-marginalized fit: interpretation (i) at 1.7% f_CW formally excluded at ~18σ under block-bootstrap σ (NSIDE=8 super-pixels, N_boot=1000) — naive WLS gave 264σ, but residual is spatially coherent",
            "Canonical-mask +3.64σ three-interpretation closure (interpretation (ii) coherent depth/morphology systematic favored by 5+ anchors)",
            "ℓ=2 cross-spectrum r=−0.65 σ=−2.89 vs pixel-density proxy",
            "MASTER-decoupled monopole-only null × 500 (88% unexplained by monopole-only leakage)",
            "Shamir 2020 vs 2022 split with arXiv IDs (post-R22 Perplexity BL-1)",
          ],
          "paper-5": [
            "V-Web env_finder Phase 1 MVP cosmic-web classification on 14.6M DESI spectro galaxies",
            "Per-environment cw_fraction: void/wall/filament/cluster (range 1.7pp dominated by counting statistics)",
            "Phase 2 sensitivity sweep (10/25/50 Mpc/h × 128³/256³/512³)",
            "Tempel+2018 cross-validation status",
            "EFT bound on parity-violating coupling: Chern-Simons modified GR sense (Alexander–Yunes 2009) + photon-graviton parity sector (Lue–Wang–Kamionkowski 1999) — citations in §VII",
            "Shot-noise residual diagnostic: skewness +0.044, excess kurtosis consistent with pure-shot-noise null (post-GEM-M3 closure)",
          ],
        };
        if (!pdfArt) return null;
        return (
          <ExternalReviewPanel
            paperNumber={paper.number}
            paperTitle={paper.title}
            paperVersion={paper.version}
            paperPath={texPath || "(see GitHub LaTeX source artifact)"}
            pdfHref={pdfArt.href}
            pdfMeta={paper.pdfMeta}
            focusAreas={focus[paper.slug] ?? []}
          />
        );
      })()}

      <details
        style={{
          marginTop: 8,
          marginBottom: 16,
          padding: "12px 14px",
          border: "1px solid var(--border)",
          borderRadius: 8,
          fontSize: "0.85rem",
        }}
      >
        <summary
          style={{
            cursor: "pointer",
            fontFamily: "var(--font-mono-stack)",
            color: "var(--text-muted)",
            fontSize: "0.78rem",
            letterSpacing: "0.06em",
            textTransform: "uppercase",
          }}
        >
          full closure log (versions, R-rounds, audit trail)
        </summary>
        <p style={{ marginTop: 12, color: "var(--text-muted)", lineHeight: 1.6, whiteSpace: "pre-wrap" }}>
          {paper.status}
        </p>
      </details>

      <Separator className="my-8" />

      <Tabs defaultValue="results" className="paper-tabs w-full">
        <TabsList className="flex-wrap">
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
          <Card className="paper-tab-panel">
            <CardHeader>
              <CardTitle>Key Results</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="paper-result-list grid gap-0">
                {paper.keyResults.map((r, i) => (
                  <li key={i} className="grid grid-cols-[34px_minmax(0,1fr)] gap-3">
                    <span className="font-mono text-xs text-muted-foreground">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    <span>
                      <MathText>{r}</MathText>
                    </span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="surveys" className="pt-4">
          {paper.surveys.length > 0 ? (
            <div className="paper-chip-grid">
              {paper.surveys.map((s) => (
                <div key={s} className="paper-chip-card">
                  <MathText>{s}</MathText>
                </div>
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
          <div className="paper-chip-grid">
            {paper.predictions.map((p) => (
              <div key={p} className="paper-chip-card">
                <MathText>{p}</MathText>
              </div>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="figures" className="pt-4">
          {paper.figures.length > 0 ? (
            <div className="paper-chip-grid">
              {paper.figures.map((f) => (
                <div key={f} className="paper-chip-card">
                  <MathText>{f}</MathText>
                </div>
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
            <div className="paper-task-list">
              {paper.remainingWork.map((task, i) => (
                <div
                  key={i}
                  className="paper-task-item"
                >
                  <span
                    className={`h-2 w-2 shrink-0 rounded-full ${task.startsWith("TIER 1") ?"dot-tone-danger" :"dot-tone-caution"}`}
                  />
                  <span><MathText>{task}</MathText></span>
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
