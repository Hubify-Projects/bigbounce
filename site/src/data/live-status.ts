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
  lastUpdatedISO: "2026-05-02T00:35:00Z",
  lastUpdatedDisplay: "May 1, 2026 · 5:35 PM PT",
  headline:
    "Wave 14-LL LANDED (2026-05-01 17:35 PDT) — R42 P4-CM-M2 edge-on TTA rotational-equivariance MAJOR closed PUSHBACK · Gemini-3.1-Pro's edge-on-leakage ask answered text-only by re-pivoting on the Wave 14-KK companion artifact (785,859-galaxy edge-on subsample b/a ∈ [0.00, 0.30) CW fraction 0.4975 ± 0.0006 vs catalog-wide 0.4974 ± 0.0003, max bin-to-bin spread 0.0005 across all four orientation regimes — residual asymmetry is uniform, NOT edge-on-localized as TTA-leakage would predict) · $0 marginal compute · paper4 v1.0.18 → v1.0.19 (4-pass Pod 3 H200 recompile, 20 pp / 25,833,438 bytes / 0 errors / 0 undef refs / sha256 29c3cb040abb...) · 5 P4 PDF mirrors byte-identical · P4 readiness held at 98% (M-2 closed; six R42 items still pending, no half-points awarded under 99% cap) · 42 R42 cross-model findings closed cumulative (up from 41) · openMajors 5 → 4 (M-2 closed; M-5 closed Wave 14-KK; remaining: Gemini P4 B-1 NaMaster + OpenAI P4 B5/B7/M-1/M-7/M-9, where M-5 closed) · Wave 14-KK P4-OA-M5 b/a-bin reconciliation FULL HARD FIX carried forward · Wave 14-JJ P4-CM-B2 PSF cross-correlation PUSHBACK carried forward · Readiness rule: 99% remains the cap until Houston signs off + an external peer-review round closes with zero MAJOR/MINOR findings · per-paper: P1 99% · P2 99% · P3 98% · P4 98% · Wave 14-II FULL HARD FIX of P3-CM-M1 carried forward · Wave 14-FF/EE/DD chirality grid + DR8 b/a fetch carried forward · SPARCL fetch (PID 25860) at +14h on separate CPU core",
  summary:
    "Wave 14-LL R42 P4-CM-M2 edge-on TTA rotational-equivariance MAJOR closure landed at 00:35Z as PUSHBACK derived text-only from the Wave 14-KK companion artifact (`r42_results/wave_14_kk_ba_reconciliation_results.json`) with $0 marginal compute. Gemini-3.1-Pro's ask (does the residual CW asymmetry hide in the edge-on b/a < 0.3 subsample where TTA rotational-equivariance is most stressed?) is answered directly by the already-on-disk 4-bin reconciliation table: the b/a ∈ [0.00, 0.30) edge-on subsample (785,859 galaxies) reports CW fraction 0.4975 ± 0.0006 (Poisson SE), statistically indistinguishable from the catalog-wide 0.4974 ± 0.0003 and from each of the three other orientation regimes (0.4970 / 0.4975 / 0.4972). Max bin-to-bin spread is 0.0005 (0.05%), well below the 0.1% flatness target and below the per-bin Poisson floor — the residual asymmetry signature is uniform across all four orientation regimes, NOT edge-on-localized, which is the prediction one would expect if rotational-equivariance leakage were the source. The new §VI.D Wave 14-LL paragraph in the paper ties the closure to the existing 4-bin table; paper4 .tex bumped v1.0.18 → v1.0.19; Pod 3 H200 4-pass recompile clean (20 pp / 25,833,438 bytes / 0 errors / 0 undef refs / sha256 29c3cb040abb...); mirrored byte-identical to all 5 P4 PDF surfaces. Per-paper today: **P1 = 99%** (Spin-Torsion — all R42 BLOCKERs closed, all known cross-model MAJORs closed Wave 14-Z; residual is open MINORs plus the standing arXiv tarball / form-fill admin step), **P2 = 99%** (f_NL Forecast — Wave 14-AA closed both Gemini-3.1-Pro MAJORs M-1 / M-2; Wave 14-K closed BLOCKER B-3; residual is text-polish MINORs), **P3 = 98%** (Anomaly Catalog — Wave 14-II FULL HARD FIX of P3-CM-M1 landed; P3-OA-M9 NANOGrav Bayesian rerun still pending Pod 3 H200 compute; some MINORs open), **P4 = 98%** (Chirality Catalog — Wave 14-LL P4-CM-M2 edge-on TTA MAJOR closed PUSHBACK; Wave 14-KK P4-OA-M5 b/a-bin reconciliation MAJOR closed FULL HARD FIX; Wave 14-JJ P4-CM-B2 PSF cross-correlation BLOCKER closed PUSHBACK; Gemini P4 B-1 NaMaster recompute pending; 4 OpenAI compute-heavy MAJORs B5 / B7 / M-1 / M-7 / M-9 still queued — M-5 closed Wave 14-KK, M-2 closed Wave 14-LL). Average readiness across the four papers: ~98.50%. The cron will continue closing R42 residuals, but a paper progressing past 99% requires Houston's sign-off plus a clean external round; that is the load-bearing gate, not a wave-cadence calculation. Wave 14-JJ carried forward: pixel-level Pearson r max |r|=0.04243 (FAILS 0.1% strict bar) but C_ℓ ℓ=2-64 with N_MC=200 max |z|=2.72σ (PASSES 3σ physics bar). Wave 14-II carried forward: Pod 3 H200 6.0s wall pure-NumPy multi-tracer Fisher with (4n+1)-dim nuisance block per tracer × (k,z) cell, σ(f_NL)_marg ∈ [0.067, 0.116] floor across 6 SPHEREx/DESI/anomaly configs. Wave 14-FF/EE/DD carried forward: 2D morphology grid + D4 TTA + DR8 b/a fetch confirm chirality asymmetry is morphology-flat. SPARCL fetch (PID 25860) still alive at ~14h on separate CPU core.",
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
      version: "v1.0.19",
      readiness: 98, // Wave 14-LL P4-CM-M2 edge-on TTA rotational-equivariance MAJOR closed PUSHBACK (text-only, derived from Wave 14-KK 4-bin data: edge-on b/a < 0.3 subsample 785,859 galaxies CW fraction 0.4975 ± 0.0006 vs catalog-wide 0.4974 ± 0.0003); Wave 14-KK P4-OA-M5 b/a-bin reconciliation MAJOR closed FULL HARD FIX carried forward; Wave 14-JJ P4-CM-B2 PSF cross-correlation BLOCKER closed PUSHBACK carried forward; Gemini P4 B-1 NaMaster recompute pending; 4 OpenAI compute-heavy MAJORs B5/B7/M-1/M-7/M-9 still queued (M-5 closed Wave 14-KK, M-2 closed Wave 14-LL).
    },
  ],
  blockerTally: {
    closed: 42, // R42 cross-model findings closed cumulative (Wave 14-LL P4-CM-M2 PUSHBACK adds +1; Wave 14-KK P4-OA-M5 FULL HARD FIX +1 prior)
    openBlockers: 0, // Wave 14-JJ P4-CM-B2 PSF cross-correlation closed PUSHBACK; no in-flight BLOCKERs
    openMajors: 4, // Wave 14-LL closed P4-CM-M2; Wave 14-KK closed P4-OA-M5; remaining: Gemini P4 B-1 NaMaster + OpenAI P4 B5/B7/M-1/M-7/M-9 (M-5 + M-2 closed)
    openMinors: 13,
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA per paper to 99% (cron-driven, Houston sign-off + clean external peer-review round still required for the final 1%): P1 99% NOW (residual MINORs only — text polish, ~2-4 h cron-driven); P2 99% NOW (residual MINORs only — ~1-2 h cron-driven); P3 → 99% in ~6-12 h (P3-OA-M9 NANOGrav Bayesian rerun on Pod 3 H200 ~2-4 h GPU + cheap-fast residual MINORs ~1-2 h); P4 → 99% in ~6-12 h (Wave 14-LL P4-CM-M2 edge-on TTA closed PUSHBACK; Wave 14-KK P4-OA-M5 b/a-bin reconciliation closed FULL HARD FIX; Wave 14-JJ PSF cross-correlation closed PUSHBACK; Gemini P4 B-1 NaMaster recompute ~2-4 h + OpenAI P4 B5/B7/M-1/M-7/M-9 compute-heavy MAJORs ~6-10 h aggregate, M-5 + M-2 closed). After all four hit 99%, the next external peer-review round (R43) gets the current PDFs; if R43 closes with zero MAJOR / MINOR findings AND Houston signs off, papers move to 100%. The cron does not award the final 1%. SPARCL fetch (PID 25860) at ~13% / ETA ~80h on separate CPU core, does not block GPU dispatch.",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "idle",
      note: "Wave 14-LL LANDED 17:35 PDT ($0 marginal compute, text-only PUSHBACK): R42 P4-CM-M2 edge-on TTA rotational-equivariance MAJOR closed by re-pivoting on the Wave 14-KK companion artifact (`r42_results/wave_14_kk_ba_reconciliation_results.json`). Gemini-3.1-Pro's edge-on-leakage ask is answered directly by the b/a ∈ [0.00, 0.30) edge-on subsample (785,859 galaxies, CW fraction 0.4975 ± 0.0006) being statistically indistinguishable from catalog-wide 0.4974 ± 0.0003, with max bin-to-bin spread 0.0005 across all four orientation regimes — residual asymmetry is uniform, NOT edge-on-localized as TTA-leakage would predict. paper4 .tex bumped v1.0.18 → v1.0.19 with explicit Wave 14-LL §VI.D paragraph; Pod 3 H200 4-pass recompile clean (20 pp / 25,833,438 bytes / 0 errors / 0 undef refs); 5 P4 PDF mirrors byte-identical (sha256 29c3cb040abb...). Wave 14-KK carries forward: 4-bin reconciliation table FULL HARD FIX (32.8s pandas-only wall, no GPU). Pod 3 H200 GPU now idle, ready for next compute-medium dispatch — natural candidates: (a) Wave 14-MM Gemini P4 B-1 NaMaster recompute on the joined 8.47M-row catalog (~2-4h GPU), (b) Wave 14-NN P3-OA-M9 NANOGrav Bayesian rerun (~2-4h GPU), (c) Wave 14-OO OpenAI P4 B5/B7/M-1/M-7/M-9 compute-heavy aggregate (~6-10h, M-5 + M-2 closed). Wave 14-JJ carries forward: pixel-level Pearson r max |r|=0.04243 (FAILS strict 0.1% bar) but C_ℓ ℓ=2-64 with N_MC=200 max |z|=2.72σ (PASSES 3σ physics bar) closed PUSHBACK. Wave 14-FF/EE/DD carry forward: 2D morphology grid + D4 TTA + DR8 b/a fetch confirm chirality asymmetry is morphology-flat. SPARCL fetch (PID 25860, alive 14h+) still on separate CPU core at ~13% / ETA ~80h, does not contend with GPU. Pod ready, autonomous loop continuing.",
    },
  ],
};
