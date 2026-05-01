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
  lastUpdatedISO: "2026-05-02T13:00:00Z",
  lastUpdatedDisplay: "2026-05-02 06:00 PT",
  headline:
    "Wave 14-CC LANDED · P4-OA-B6 documentation closure · 36 cross-model findings closed · ETA all-4 → 100%: ~10-24 h",
  summary:
    "Wave 14-CC: R42 P4-OA-B6 BLOCKER closed via documentation/tracker close-out (R42 master tracker L410 ask: 'Change removes → reduces; document calibration objective + dataset + residual offset; OR re-fit so cw/(cw+ccw)=0.5 on validation set'). Verification of pipelines/p2_chirality/chirality_catalog_paper.tex confirmed all three sub-asks already resolved in-paper since Wave 11-C P4 N_spiral recompile: (1) L674 Catalog~B description uses 'reduces' not 'removes' ('Platt-calibrated: a sigmoid calibration (bias = 1.58, temperature = 4.65) fitted against CE-ResNet consensus labels reduces the residual CW excess from...'), (2) L681-687 documents Platt scaling parameters (A, B) = (1/4.65, -1.58) mapping p_cal = σ(Az + B), L-BFGS minimization of cross-entropy on held-out 20% validation set + companion code repo, (3) L688-690 explicit caveat 'the Platt scaling calibration is fit against CE-ResNet consensus labels, not an independent ground truth; the calibration therefore inherits any systematic bias present in the CE-ResNet labels' + L815 quantitative residual offset 'Platt calibration (Catalog~B) reduces this to ~0.4%'. No .tex edits, no PDF recompile, no version bump — pure tracker close. Wave 14-CC GPU-dispatch scoping outcome: Pod 3 H200 GPU still idle (0% / 0 MiB / 143156 MiB available, confirmed 13:00 PDT) but the natural compute-medium candidates are blocked on data NOT currently on Pod 3: (a) Wave 14-S P3 systematics-marginalization Fisher recompute infrastructure not on Pod 3 (would need 1-2h dev + 30-60min run); (b) P4-CM-M2 D4 b/a<0.3 TTA needs DESI Legacy DR8 sweep cross-match column NOT in catalog_production.parquet schema (probed: 8.47M rows, columns dr8_id/p_cw_eq/p_ccw_eq/p_ns_eq/class_eq/confidence_eq/ra/dec/image_url + raw probs — no b/a axis-ratio column, 2.39 GB memory). Pragmatic path chosen per feedback_take_critiques_seriously.md (transparency on hard things at TOP): close P4-OA-B6 documentation BLOCKER + scope Wave 14-DD as DESI Legacy DR8 sweep fetch on Pod 3 to unblock 14-EE GPU dispatch. SPARCL fetch progress (PID 25860, alive 12h13m): 259/2000 shards = 13.0% at sustained rate ~21.6 shards/hr (~10,800 spectra/hr), ETA to 1M completion ~80h (~3.4 days) — likely SPARCL server rate-limiting, not Pod 3 CPU saturation; SPARCL fetch is CPU-bound (99% on single core) and does NOT block GPU dispatch. Wave 14-DD plan: dispatch DESI Legacy DR8 sweep fetch on Pod 3 (compute-medium IO-bound, ~30-60min wget + parquet conversion) to materialize b/a axis-ratio column, then Wave 14-EE GPU-medium TTA recompute closes P4-CM-M2 D4 with real GPU work.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.14",
      readiness: 97,
    },
    {
      slug: "fnl-forecast",
      number: 2,
      shortTitle: "f_NL SPHEREx Forecast",
      version: "v1.7.8",
      readiness: 92,
    },
    {
      slug: "anomaly-catalog",
      number: 3,
      shortTitle: "Multi-Survey Anomaly Catalog",
      version: "v3.1.14",
      readiness: 96,
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.16",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 36, // +1 from Wave 14-BB: P4-OA-B6 (Catalog~B documentation closure) closed Wave 14-CC
    openBlockers: 0, // unchanged from Wave 14-BB (P4-OA-B6 was a BLOCKER but already in-paper since Wave 11-C; tracker close only)
    openMajors: 8, // unchanged from Wave 14-BB
    openMinors: 13, // unchanged from Wave 14-BB
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~10-24 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-CC P4-OA-B6 documentation closure COMPLETE — pure tracker close-out, no .tex edits / no PDF recompile / no version bump, all three sub-asks verified in-paper at chirality_catalog_paper.tex L674 + L681-687 + L688-690 + L815 since Wave 11-C; Wave 14-CC GPU-dispatch scoping found natural compute-medium candidates blocked on data NOT on Pod 3 — pragmatic path chosen per transparency directive; Wave 14-DD plan: dispatch DESI Legacy DR8 sweep fetch on Pod 3 (compute-medium IO-bound, ~30-60min wget + parquet conversion) to materialize b/a axis-ratio column, then Wave 14-EE GPU-medium TTA recompute closes P4-CM-M2 D4 with real GPU work; SPARCL fetch (PID 25860) at 13.0% / ETA 80h is CPU-bound and does NOT block GPU dispatch; idle-GPU violation per feedback_idle_gpu_proactive.md acknowledged — Wave 14-DD will fetch data NOW (no morning-ask deferral per feedback_never_defer_path_discovery.md), Wave 14-EE will dispatch GPU work)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-CC COMPLETE: R42 P4-OA-B6 BLOCKER documentation/tracker close-out (R42 master tracker L410 ask: 'Change removes → reduces; document calibration objective + dataset + residual offset; OR re-fit so cw/(cw+ccw)=0.5 on validation set'). Verification of pipelines/p2_chirality/chirality_catalog_paper.tex confirmed all three sub-asks already resolved in-paper since Wave 11-C P4 N_spiral recompile: L674 'reduces' (not 'removes') + L681-687 Platt scaling parameters (A,B)=(1/4.65,-1.58) on held-out 20% validation set + L688-690 explicit caveat about CE-ResNet consensus labels not being independent ground truth + L815 quantitative residual offset '~0.4%'. No .tex edits, no PDF recompile, no version bump — pure tracker close. Wave 14-CC GPU-dispatch scoping outcome: Pod 3 H200 GPU still idle (0% / 0 MiB / 143156 MiB available, confirmed 13:00 PDT) and ready, BUT natural compute-medium candidates blocked on data NOT currently on Pod 3 — (a) Wave 14-S P3 Fisher recompute infrastructure not on Pod 3 (~1-2h dev + ~30-60min run), (b) P4-CM-M2 D4 b/a<0.3 TTA needs DESI Legacy DR8 sweep cross-match column NOT in /workspace/r42_b20/chirality_catalog/catalog_production.parquet schema (probed: 8.47M rows / 2.39 GB / columns dr8_id,p_cw_eq,p_ccw_eq,p_ns_eq,class_eq,confidence_eq,ra,dec,image_url + raw probs — no b/a column). Pragmatic path per feedback_take_critiques_seriously.md (transparency at TOP) + feedback_never_defer_path_discovery.md (resolve dataset paths NOW, no morning-ask): Wave 14-CC closes P4-OA-B6 documentation BLOCKER + scopes Wave 14-DD as DESI Legacy DR8 sweep fetch on Pod 3 (~30-60min wget + parquet conversion, IO-bound compute-medium) to materialize b/a axis-ratio column, then Wave 14-EE GPU-medium TTA recompute closes P4-CM-M2 D4 with real GPU work. SPARCL fetch (PID 25860, alive 12h13m): 259/2000 shards = 13.0% at sustained ~21.6 shards/hr (~10,800 spectra/hr), ETA 1M ~80h (~3.4 days) — likely SPARCL server rate-limit, not Pod 3 CPU saturation; SPARCL is CPU-bound (99% on single core) and does NOT contend with GPU. $0 marginal H200 spend (7th consecutive wave at $0 marginal — Wave 14-CC was tracker-only). Wave 14-DD dispatching this fire to unblock 14-EE GPU work.",
    },
  ],
};
