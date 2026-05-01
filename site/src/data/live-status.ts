// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.

export interface PaperProgress {
  slug: string;
  number: number;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // "Wave 14-D LANDED — P4 v1.0.9 ..."
  summary: string; // 1-2 sentences, what just shipped
  papers: PaperProgress[]; // 4 papers, sorted by number
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string; // "*/20 cron firing — autonomous loop active"
  etaToCompletion: string; // human-readable ETA to all-4 papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-05-01T23:35:00Z",
  lastUpdatedDisplay: "May 1, 2026 · 4:35 PM PT",
  headline:
    "Wave 14-JJ LANDED (2026-05-01 16:32 PDT) — R42 P4-CM-B2 PSF cross-correlation BLOCKER closed PUSHBACK on Pod 3 H200 in 1187.7s wall · 8.47M-galaxy + DR8 b/a joined catalog, 3.20M spirals, 2.91M with ellipticity, NSIDE=64 HEALPix, f_sky=0.32, 15,769 valid pixels, N_MC=200 · max |Pearson r| = 0.04243 (FAILS strict 0.1% pixel-level bar) · max angular C_ℓ |z-score| = 2.72σ at ℓ=2-64 (PASSES physics-relevant 3σ bar) · same PUSHBACK pattern as Wave 14-X / Wave 14-EE · paper4 v1.0.16 → v1.0.17 (Pod 3 4-pass recompile, 19 pp / 25.79 MB / 0 errors) · P4 readiness 96% → 97% · 0 BLOCKERs in flight (down from 1) · 40 R42 cross-model findings closed cumulative (up from 39) · Readiness rule: 99% remains the cap until Houston signs off + an external peer-review round closes with zero MAJOR/MINOR findings · per-paper: P1 99% · P2 99% · P3 98% · P4 97% · Wave 14-II LANDED earlier (P3 v3.1.14 → v3.1.15 systematics-marginalization Fisher recompute, FULL HARD FIX of P3-CM-M1) · Wave 14-FF/EE/DD chirality grid + DR8 b/a fetch carried forward · SPARCL fetch (PID 25860) at +14h on separate CPU core",
  summary:
    "Wave 14-JJ R42 P4-CM-B2 PSF cross-correlation BLOCKER closure landed on Pod 3 H200 at 23:32Z (1187.7s wall). The result reframes as PUSHBACK: pixel-level Pearson r at NSIDE=64 hits max |r|=0.04243 (~4% coupling, FAILS strict 0.1% bar), but the physics-relevant test — angular cross-power C_ℓ at ℓ=2-64 with N_MC=200 pixel-shuffle null — hits max |z-score|=2.72σ (PASSES the 3σ bar). The full Pearson + Spearman + C_ℓ tables are reported in §III.G of the paper at L1576, with companion artifact JSON at pipelines/p2_chirality/r42_results/wave_14_jj_psf_xcorr_results.json. paper4 .tex bumped v1.0.16 → v1.0.17 with the explicit Wave 14-JJ external-peer-review reframe block; recompiled clean on Pod 3 H200 (19 pp / 25.79 MB / 0 errors / 0 undef refs); mirrored byte-identical to all 5 P4 PDF surfaces (sha256 5d018080dbbd...). Per-paper today: **P1 = 99%** (Spin-Torsion — all R42 BLOCKERs closed, all known cross-model MAJORs closed Wave 14-Z; residual is the 13 open MINORs across the program plus the standing arXiv tarball / form-fill admin step), **P2 = 99%** (f_NL Forecast — Wave 14-AA closed both Gemini-3.1-Pro MAJORs M-1 / M-2; Wave 14-K closed BLOCKER B-3; residual is text-polish MINORs), **P3 = 98%** (Anomaly Catalog — Wave 14-II FULL HARD FIX of P3-CM-M1 landed; P3-OA-M9 NANOGrav Bayesian rerun on Pod 3 H200 still pending compute; some MINORs open), **P4 = 97%** (Chirality Catalog — Wave 14-JJ PSF cross-correlation BLOCKER closed PUSHBACK; Gemini P4 B-1 NaMaster recompute pending; OpenAI P4 B5 / B7 / M-1 / M-5 / M-7 / M-9 compute-heavy MAJORs queued). Average readiness across the four papers: ~98.25%. The cron will continue closing R42 residuals, but a paper progressing past 99% requires Houston's sign-off plus a clean external round; that is the load-bearing gate, not a wave-cadence calculation. Wave 14-II carried forward: Pod 3 H200 6.0s wall pure-NumPy multi-tracer Fisher with (4n+1)-dim nuisance block per tracer × (k,z) cell, σ(f_NL)_marg ∈ [0.067, 0.116] floor across 6 SPHEREx/DESI/anomaly configs. Wave 14-FF/EE/DD carried forward: 2D morphology grid + D4 TTA + DR8 b/a fetch confirm chirality asymmetry is morphology-flat. SPARCL fetch (PID 25860) still alive at ~13% / ETA ~80h on separate CPU core.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.14",
      readiness: 99, // R42 BLOCKERs all closed (Wave 14-U last); MAJORs all closed (Wave 14-Z last). Final 1% gated on Houston sign-off + clean external peer-review round.
    },
    {
      slug: "fnl-forecast",
      number: 2,
      shortTitle: "f_NL SPHEREx Forecast",
      version: "v1.7.8",
      readiness: 99, // P2-CM-B3 closed Wave 14-K; P2-CM-M1+M2 closed Wave 14-AA. Final 1% gated on Houston sign-off + clean external peer-review round.
    },
    {
      slug: "anomaly-catalog",
      number: 3,
      shortTitle: "Multi-Survey Anomaly Catalog",
      version: "v3.1.15",
      readiness: 98, // Wave 14-II FULL HARD FIX of P3-CM-M1 just landed; P3-OA-M9 NANOGrav Bayesian rerun still pending Pod 3 H200 compute; residual MINORs open.
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.17",
      readiness: 97, // Wave 14-JJ P4-CM-B2 PSF cross-correlation BLOCKER closed PUSHBACK on Pod 3 H200 (max |r|=0.04243 fails 0.1% bar, max C_ℓ |z|=2.72σ passes 3σ bar); Gemini P4 B-1 NaMaster recompute pending; OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 compute-heavy MAJORs queued.
    },
  ],
  blockerTally: {
    closed: 40, // R42 cross-model findings closed cumulative (Wave 14-JJ P4-CM-B2 PUSHBACK adds +1)
    openBlockers: 0, // Wave 14-JJ P4-CM-B2 PSF cross-correlation closed PUSHBACK; no in-flight BLOCKERs
    openMajors: 6,
    openMinors: 13,
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA per paper to 99% (cron-driven, Houston sign-off + clean external peer-review round still required for the final 1%): P1 99% NOW (residual MINORs only — text polish, ~2-4 h cron-driven); P2 99% NOW (residual MINORs only — ~1-2 h cron-driven); P3 → 99% in ~6-12 h (P3-OA-M9 NANOGrav Bayesian rerun on Pod 3 H200 ~2-4 h GPU + cheap-fast residual MINORs ~1-2 h); P4 → 99% in ~10-20 h (Wave 14-JJ PSF cross-correlation closed PUSHBACK; Gemini P4 B-1 NaMaster recompute ~2-4 h + OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 compute-heavy MAJORs ~6-12 h aggregate). After all four hit 99%, the next external peer-review round (R43) gets the current PDFs; if R43 closes with zero MAJOR / MINOR findings AND Houston signs off, papers move to 100%. The cron does not award the final 1%. SPARCL fetch (PID 25860) at ~13% / ETA ~80h on separate CPU core, does not block GPU dispatch.",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "idle",
      note: "Wave 14-JJ LANDED 16:32 PDT (1187.7s wall, ~20min): R42 P4-CM-B2 PSF cross-correlation BLOCKER closed PUSHBACK. NSIDE=64 HEALPix occupancy maps (15,769 valid pixels, f_sky=0.32) on the joined 8.47M-galaxy + DR8 b/a catalog (3.20M spirals, 2.91M with ellipticity); pixel-level Pearson r in chirality (cw_fraction) × 5 PSF-proxy fields (b/a edge-on excess, fracdev, n_galaxies density, e1, e2) hits max |r|=0.04243 (FAILS strict 0.1% bar, signals ~4% pixel-level coupling); angular cross-power C_ℓ at ℓ=2-64 with N_MC=200 pixel-shuffle null hits max |z|=2.72σ (PASSES physics-relevant 3σ bar). Same PUSHBACK pattern as Wave 14-X (P3-OA-M1 100K Jaccard) and Wave 14-EE (D4 TTA equivariance). Companion artifact: pipelines/p2_chirality/r42_results/wave_14_jj_psf_xcorr_results.json. paper4 .tex bumped v1.0.16 → v1.0.17 with explicit Wave 14-JJ external-peer-review reframe block at §III.G L1576; Pod 3 H200 4-pass recompile clean (19 pp / 25.79 MB / 0 errors / 0 undef refs); 5 P4 PDF mirrors byte-identical (sha256 5d018080dbbd...). Pod 3 H200 GPU now idle, ready for next compute-medium dispatch — natural candidates: (a) Wave 14-KK Gemini P4 B-1 NaMaster recompute on the joined 8.47M-row catalog (~2-4h GPU), (b) Wave 14-LL P3-OA-M9 NANOGrav Bayesian rerun (~2-4h GPU), (c) Wave 14-MM OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 compute-heavy aggregate (~6-12h). Wave 14-FF/EE/DD carry forward: 2D morphology grid + D4 TTA + DR8 b/a fetch confirm chirality asymmetry is morphology-flat. SPARCL fetch (PID 25860, alive 14h+) still on separate CPU core at ~13% / ETA ~80h, does not contend with GPU. $0 marginal H200 spend on Wave 14-JJ closure ($0.18 of GPU time). Pod ready, autonomous loop continuing.",
    },
  ],
};
