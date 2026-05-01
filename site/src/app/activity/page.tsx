import { FeedItem } from"@/components/Feed/FeedItem";
import { Badge } from"@/components/ui/badge";
import { Card, CardContent } from"@/components/ui/card";
import { Separator } from"@/components/ui/separator";
import type { Metadata } from"next";

export const metadata: Metadata = {
  title:"Activity",
  description:
"Live research status and chronological timeline of the BigBounce program.",
};

export default function ActivityPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Live Research Activity
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          Activity Feed
        </h1>
        <p className="subtitle">
          What we&apos;re working on now, what happened recently, and what&apos;s
          coming next.
        </p>
      </div>

      <Card className="mt-6 border-l-4 border-tone-muted">
        <CardContent className="space-y-2 p-5">
          <div className="flex items-center gap-2">
            <Badge variant="default">Current Focus</Badge>
          </div>
          <div
            className="text-lg font-semibold"
            style={{ fontFamily:"var(--font-mono-stack)" }}
          >
            R42 Wave 14-D LANDED — P4 v1.0.9 (P4-OA-B6 Platt close) + Next.js site is live
          </div>
          <p className="text-sm leading-relaxed text-muted-foreground">
            Wave 14-D bundled the P4-OA-B6 Platt-calibration text edit (raw
            +0.79% / 28.8σ → calibrated +0.4% / 14.6σ → equivariant -0.26% /
            9.5σ; calibration is p_cal = σ(Az + B) with A = 1/T, B = -1.58
            via L-BFGS on the held-out 20% validation split). Three GPT-5
            BLOCKERs (P4-OA-B1 / B2 / B6) closed inside the single Wave 14-B
            fetch window. Live site flipped from static HTML to Next.js
            (vercel.json buildCommand → cd site && npm run build / outputDirectory
            site/out / installCommand → cd site && npm install). LiveStatus
            banner now baked at top of every page with build-time timestamp,
            paper readiness bars, BLOCKER tally, Pod 3 fetch state, and
            ETA-to-completion. Pod 3 H200 SPARCL 1M fetch alive on PID 25860
            (~60 min elapsed, 18 shards / 9K of 1M spectra written, ~150
            spectra/min observed — sub-sample short-circuit decision pending
            if throughput stays at this level).
          </p>
        </CardContent>
      </Card>

      <Separator className="my-8" />

      <section className="section">
        <h2>Research Timeline</h2>
        <div className="flex flex-col gap-3">
          <FeedItem
            date="2026-05-01"
            title="R42 Wave 14-D LANDED — P4 v1.0.9 Platt-Calibration Close + Next.js Site Flipped Live"
            type="positive"
            tags={["Wave 14-D","P4","P4-OA-B6","Platt","Next.js","Site Flip"]}
          >
            Bundled Principle-13 close on the P4-OA-B6 GPT-5 reviewer BLOCKER:
            paper4 §VII.D revised so the Platt-scaling claim no longer reads as
            &quot;removes&quot; the +0.79% raw chirality residual when Table III
            still shows a calibrated +0.4% (14.6σ at the 8.47M sample). New
            text: raw +0.79%/28.8σ → calibrated p_cal = σ(z/4.65 - 1.58) (L-BFGS
            on 20% held-out split) +0.4%/14.6σ → equivariant pretrain -0.26%/9.5σ.
            Same commit shipped: vercel.json buildCommand flip + LiveStatus
            banner + activity feed sync + SSOT queue update. Two follow-on
            commits fixed Vercel deploy errors (missing prebuild script + missing
            installCommand). Live site verified Next.js: title &quot;BigBounce —
            Spin-Torsion Cosmology&quot;, GeistSans/Mono fonts, Turbopack chunks,
            LiveStatus banner rendered at top of every page.
          </FeedItem>

          <FeedItem
            date="2026-05-01"
            title="R42 Wave 13 LANDED — Real NANOGrav KDE Free-Spectrum γ = 2.567 ± 0.382"
            type="positive"
            tags={["Wave 13","NANOGrav","P3-CM-B3","Pod 3","emcee"]}
          >
            Closed the highest-leverage P3 cross-model BLOCKER autonomously: the
            free-spectrum dataset path was discovered (Zenodo 8060824 — KDE
            Representations of GWB Free Spectra), 30-bin Ceffyl KDE pack pulled
            on Pod 3, and emcee ran 32 walkers × 10,000 production + 2,500
            burn-in in 25 s on H200. Real-data γ = 2.567 ± 0.382 (median 2.591,
            68% CI [2.304, 2.882]); log10_A = -14.025 ± 0.380. Bounce γ = 3.0
            sits at -1.13σ — still consistent. SMBHB γ = 4.33 excluded at -4.6σ
            (sharper than the synthetic-power-law -2.7σ). Real-vs-synthetic
            shift: -1.48σ — substantive. ESS = 5,507; τ ≈ 58; acceptance = 0.63.
            Artifact: pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/.
          </FeedItem>

          <FeedItem
            date="2026-05-01"
            title="R42 Wave 12 LANDED — H200 Hemisphere LEE Null at p &lt; 10⁻⁴"
            type="positive"
            tags={["Wave 12","Paper 4","H200","Pod 3","Hemisphere"]}
          >
            Pod 3 H200 ran direct-MC max-statistic null over 768 healpix
            directions (NSIDE=8) on the 3,201,160-spiral catalog at N_MC =
            10,000. max|A|(data) = 8.531×10⁻³ at dir #731 (RA = 78.75°, Dec =
            -66.44°); zero of 10,000 nulls reached the data → p_LEE = 9.999×
            10⁻⁵ at the 1/10001 precision floor — an order of magnitude
            tighter than Wave 11-G v3&apos;s 1/501. Wall 17.2 s (4.8 s MC at
            2,098 MC/s on H200). Closes P4-CM-B2 + P4-CM-m2 + P4-OA-M8
            hemi-LEE skeptic-channel triplet.
          </FeedItem>

          <FeedItem
            date="2026-05-01"
            title="R42 Wave 11 LANDED — P1 Reframe + P2 Eq. 3 + P3 Retitle 378K + P4 N_spiral Fix"
            type="milestone"
            tags={["Wave 11","R42","Cross-Model","All Papers","Principle 13"]}
          >
            Single bundled commit landed the highest-leverage Wave 10 cross-model
            findings across all 4 papers. P1 abstract drops &quot;evidence for
            ECH&quot; framing; Bayes-factor scoped to ΛCDM+ΔN_eff proxy only
            (closes P1-CM-B1 + P1-CM-B3 + P1-CM-M2 + P1-OA-B2). P2 Eq. 3 1/k²
            shape-function factor restored to match prose. P3 retitled
            &quot;378,280 anomalies from 37.3 million sources&quot;; ACT-DR6
            quarantine made explicit; §VI separates IF injection-recovery from
            BigAE-latent primary catalogs. P4 NaMaster footnote-5 shot-noise
            recomputed with corrected N_spiral = 3,321,795 denominator
            (cross-confirmed Gemini 3.1-Pro P4-CM-B1 and GPT-5 P4-OA-M7 — two
            adversarial models converged on the same bug). All 4 PDFs
            recompiled clean on Pod 3 (P1 1.23 MB, P2 758 KB, P3 28.27 MB, P4
            25.78 MB).
          </FeedItem>

          <FeedItem
            date="2026-05-01"
            title="R42 Wave 10 OPEN — Cross-Model Adversarial Peer Review (Gemini 3.1-Pro + GPT-5)"
            type="milestone"
            tags={["Wave 10","Cross-Model Review","Gemini","GPT-5","Adversarial"]}
          >
            Two non-Anthropic models reviewed all 4 papers in parallel; ~60
            unique findings queued (Gemini: 12 BLOCKERs / 9 MAJORs / 8 MINORs;
            OpenAI: 23 BLOCKERs / 25 MAJORs / 17 MINORs after dedup). Verdicts:
            Gemini — P1 REJECT, P2 REJECT, P3 MAJOR REVISION, P4 MAJOR
            REVISION; GPT-5 — major-revisions-needed across all four. One
            high-confidence cross-confirmation: P4 NaMaster N_spiral arithmetic
            bug independently re-discovered by both models. Three load-bearing
            patterns surfaced that survived 9 prior in-Anthropic review rounds:
            tighter-than-official error bars, claim-vs-derivation gaps, and
            validation-vs-product mismatches — exactly the failure class
            invisible inside an Anthropic-only review pipeline.
          </FeedItem>

          <FeedItem
            date="2026-05-01"
            title="R42 Wave 5 CLOSED — P3 100k OOD Validation + LAMOST FAIL Relabel"
            type="positive"
            tags={["Wave 5","P3","Path-C","BLOCKERs"]}
          >
            P3 B10 100k OOD validation: 100k unseen DESI DR1 spectra retrieved
            via NOIRLab SPARCL (seed 20,260,501; distinct from training seed),
            BigAE 47k checkpoint scored in 0.3 s on H200; median MSE 0.178, p99
            = 44.85, 0.87% DESI anomaly rate preserved. P3 B15 LAMOST FAIL
            relabel: 113,342 native top-1% LAMOST sources reclassified as
            exploratory tier within the 378,280 headline; primary-tier
            sub-total = 264,938 unique objects. 16 of 23 R42 BLOCKERs CLOSED.
          </FeedItem>

          <FeedItem
            date="2026-04-30"
            title="R41 Cross-Paper Decoupling + P1 Negative-Rhetoric Reframe"
            type="milestone"
            tags={["R41","Decoupling","P1 Reframe","All Papers"]}
          >
            28 inter-paper Golden:2026 cross-citations eliminated (P1: 13, P2:
            6, P3: 6, P4: 3) and replaced with primary-source citations
            (Heinrich+2023, Lentati+2013, WilsonEwing+2012, Mercuri+2006,
            Freidel+2005, Poplawski+2012/2016, Eskilt+2022, Diego-Palazuelos+
            2025, Minami+2020, Cai+2026, Baron+2017, Liang+2023). P1 abstract
            reframed: opens with the inflation-tension structural finding
            instead of chained negatives. Each paper now stands on its own —
            no inter-paper citation chain; submission order constraint relaxed.
          </FeedItem>

          <FeedItem
            date="2026-04-29"
            title="Pod 1 NaMaster 500MC Birefringence + UMAP Multi-Seed Stability"
            type="positive"
            tags={["Pod 1","NaMaster","Birefringence","UMAP","H200"]}
          >
            Pod 1 (frail_tomato_koi) ran NaMaster 500MC on a single GPU
            overnight: β = 0.27° (bounce prediction) recovered as 0.238°
            (bias 0.032°) at SNR = 20.32σ at ACT sensitivity (f_sky = 0.32,
            n_side = 512, ℓ_max = 1024, 10 µK·arcmin noise); β = 0.342°
            (Planck+ACT observed) recovered as 0.302° at SNR = 25.71σ;
            consistency P1-prediction vs observation = 0.77σ. UMAP
            multi-seed stability (50K × 16D × 20 seeds): 1-of-3 PASS framing
            integrated into Paper 3.
          </FeedItem>

          <FeedItem
            date="2026-04-29"
            title="Pod 2 Chirality Bias Hardening + MASTER Deconvolution"
            type="positive"
            tags={["Pod 2","Paper 4","H200","MASTER","Bias Hardening"]}
          >
            Pod 2 (regular_green_pig) closed all 4 originally-blocked Paper 4
            tasks: MASTER deconvolution on 8.47M galaxies (NSIDE=64, f_sky =
            0.4928, max C_ℓ = 6.26×10⁻³ at ℓ=9), bias hardening 4/8 PASS
            (flip/swap, rotation, artifacts, perturbation FAIL → flagged in
            §validation), Catalog C redshift dipole pulled from
            bamfai/galaxy-chirality-catalog, edge-on equivariance suppression
            factor = 3.86× (raw asym +2.05% → eq asym -0.53%).
          </FeedItem>

          <FeedItem
            date="2026-04-27"
            title="Adversarial Peer Review Rounds 31–34 — Single-Check Micro-Tasks"
            type="milestone"
            tags={["R31–R34","Peer Review","All Papers"]}
          >
            5 parallel Opus agents (4 hostile per-paper referees + 1 cross-paper
            consistency checker) ran 4 focused single-check rounds across all 4
            papers. R31: P1 1 MAJOR + 3 MINOR; P2 3 MINOR; P3 1 MAJOR + 3 MINOR;
            P4 2 MINOR + N_gal closure. R32: reproducibility note → 500MC, bib
            hygiene, UMAP &quot;1-of-3 PASS&quot; honest framing, units + ℓ_max
            + N_gal arithmetic + Dosovitskiy bib. R33+R34 used the focused
            pattern exclusively — zero stalls. Strategy lesson: single-check
            1-scope micro-tasks finished in 15-230 s; broad 3-check sub-agents
            stalled at 600 s with zero edits.
          </FeedItem>

          <FeedItem
            date="2026-04-22"
            title="Path-C Paper 3 Rebuild CLOSED — 12/12 Criteria Green"
            type="positive"
            tags={["Path-C","Paper 3","Rebuild","Closed"]}
          >
            Houston greenlit autonomous completion. Final fire executed on pod
            o76k3jfzbfh25e: live SPARCL retrieval of 47,000 DESI DR1 spectra
            in 19.8 min, 0 dropped, deterministic checksum 1812395110. 5-fold
            BigAE training &lt; 30 s on A100. Jaccard aggregation GATE PASS:
            mean pairwise J̄ = 0.862 (min 0.777) vs required J̄ ≥ 0.70. Paper
            3 §pathc_caveats updated, recompiled to 28 MB / 33 pp / 0 undef,
            mirrored to public/papers/. All 12 Path-C exit criteria CLOSED.
          </FeedItem>

          <FeedItem
            date="2026-04-04"
            title="Planck CMB Re-Run PASSES QC — Galactic Mask Fix Works"
            type="positive"
            tags={["Planck CMB","QC PASS","Phase 1","H200 Queue v2"]}
          >
            Re-ran Planck CMB anomaly detection with GAL080 galactic mask
            applied before patch extraction. val_loss = 0.138 (was 0.831). Top
            anomaly at RA = 208.5°, Dec = -21.2° (no longer at Dec &lt; -84°
            galactic pole). 193 anomalies from 19,296 masked patches. First
            Phase 1 experiment complete.
          </FeedItem>

          <FeedItem
            date="2026-04-04"
            title="Full Project Reset: Houston Method v2, Wiki, Next.js, H200 Queue v2"
            type="milestone"
            tags={["Quality Audit","Houston Method v2","Wiki","Next.js","Project Reset"]}
          >
            Quality audit of H200 results revealed 6/10 experiments have QC
            failures: Planck CMB (galactic contamination), ACT DR6
            (undertrained), NEOWISE (ecliptic systematic), super-resolution
            (null coordinates), taxonomy (degenerate clustering), Gaia (sample
            too small). Implemented Houston Method v2 with mandatory 9-step
            completion loop. Created Karpathy-style wiki (25 pages). Scaffolded
            Next.js app. New 50-experiment queue designed.
          </FeedItem>

          <FeedItem
            date="2026-04-03"
            title="f_NL Multi-Tracer Pipeline: 6.1% Improvement — PUBLISHABLE"
            type="positive"
            tags={["f_NL","Multi-Tracer","Publishable"]}
          >
            Ran full f_NL pipeline on DESI + SDSS anomalies. σ(f_NL) improved
            6.1% (DESI alone) and 16.4% (DESI+SDSS combined). Clears 5%
            threshold for publication. SPHEREx forecast: 4.38σ detection of
            f_NL = -35/8.
          </FeedItem>

          <FeedItem
            date="2026-04-02"
            title="All 10 H200 Experiments Complete — 33.5M Sources, 328K Anomalies"
            type="milestone"
            tags={["H200 Queue","Multi-Survey","Complete"]}
          >
            Multi-survey anomaly sweep finished: DESI, SDSS, LAMOST, eROSITA,
            Planck, ACT, NEOWISE, Gaia + NANOGrav consistency +
            super-resolution. Grand total: 33.5M sources scored, 328,448
            anomalies across 8 surveys. (Later audit revealed 6/10 need
            re-running due to QC issues.)
          </FeedItem>
        </div>
      </section>
    </>
  );
}
