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
  lastUpdatedDisplay: "2026-05-01 16:35 PT",
  headline:
    "Wave 14-G LANDED — P4 v1.0.12 (OpenAI M-2 dipole-sidedness convention + OpenAI M-3 rotation-augmentation conceptual fix; OpenAI M-8 / Gemini m-2 hemisphere-LEE max-stat documented as already closed via Wave 12 N_MC=10,000); 8 cross-model findings closed across 6 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch runs",
  summary:
    "Wave 14-G closes two more cheap-fast OpenAI/GPT-5 P4 findings (M-2 + M-3) and documents the de facto closure of OpenAI M-8 / Gemini m-2 (no .tex edit needed — §sec:hemisphere already cites the Wave 12 v4 GPU N_MC=10,000 max-stat null with p_LEE = 9.999e-5 at the 1/10001 floor, superseding the original Bonferroni LEE correction). OpenAI M-2 (dipole-sidedness convention): §sec:dipole \"Simple dipole\" paragraph at L893 rewritten so the 0.43σ amplitude significance is explicitly tagged one-tailed p = 0.33 (equivalently two-tailed p = 0.67, since the dipole-amplitude statistic is positive-definite and we test the alternative \"amplitude > random isotropic\"); the one-tailed convention is the natural one for amplitude-only tests, applied consistently to multipole-null and hemisphere p-values reported elsewhere in the section. OpenAI M-3 (rotation-augmentation conceptual fix): §III.B Augmentations paragraph at L373 rewritten to correct the conceptual claim that random in-plane rotation \"does not preserve the CW/CCW label under large rotations\" — in fact in-plane rotation about the line-of-sight is chirality-preserving by construction (a clockwise-trailing spiral remains clockwise-trailing after any rotation; only mirror reflection flips CW↔CCW), and the residual orientation-correlated asymmetry that survives the augmentation arises from the classifier's rotation-non-equivariance under spatially-varying PSF and pixel-grid structure, not from rotated CW/CCW labels being mismatched; the optional D_4-TTA extension noted in §sec:tta is now flagged as the natural averaging path for that classifier-side residual; fix removes an internal inconsistency between §III.B and §III.C/§sec:tta. P4 .tex bumped v1.0.11 → v1.0.12, date 16:10 PDT → 16:35 PDT, recompiled clean on Pod 3 (pdflatex × 2 in /workspace/recompile_p4/, 25.79 MB / 18 pp / 0 undef refs, page count unchanged because both edits flow within existing column blocks), mirrored to pipelines/p2_chirality/ + public/papers/. Eight cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G) now closed across six cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window — exactly the cheap-fast text-edit while compute runs discipline feedback_more_not_less.md + feedback_default_hardest_path.md codify. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~1h43m elapsed at this commit, 35 shards / 72 MB written, sustained throughput ~170 spectra/min — correcting downward the Wave 14-F header read of \"275 spectra/min\" which was an arithmetic over-read against a single-shard window; at the actual sustained rate the 1M ETA is ~98 hours, so the 100K sub-sample short-circuit (~10 hours at the same throughput) is now the strongly recommended operational call.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.5",
      readiness: 92,
    },
    {
      slug: "fnl-forecast",
      number: 2,
      shortTitle: "f_NL SPHEREx Forecast",
      version: "v1.7.6",
      readiness: 90,
    },
    {
      slug: "anomaly-catalog",
      number: 3,
      shortTitle: "Multi-Survey Anomaly Catalog",
      version: "v3.1.8",
      readiness: 91,
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.12",
      readiness: 96,
    },
  ],
  blockerTally: {
    closed: 14, // 14 cross-model BLOCKERs closed across Waves 11-14 (Wave 14-G closes M-2/M-3 MAJORs + documents M-8/m-2 closure, not BLOCKERs)
    openBlockers: 4, // remaining cross-model BLOCKERs (P3-OA-M1 1M Jaccard pending fetch / sub-sample short-circuit)
    openMajors: 21, // -3 from Wave 14-G: OpenAI P4 M-2 (sidedness) + OpenAI P4 M-3 (rotation aug) + OpenAI P4 M-8 (Bonferroni → empirical max-stat, documented as already closed)
    openMinors: 23, // -1 from Wave 14-G: Gemini P4 m-2 (Bonferroni → empirical max-stat, documented as already closed alongside OpenAI M-8)
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~48-72 h at current Wave-cadence (3-5 cross-model findings / day on cheap-fast queue + 1 compute-heavy / day on Pod 3 H200; Wave 14-B 1M Jaccard fetch now ~98 h on the corrected ~170 spectra/min sustained throughput, 100K sub-sample short-circuit (~10 h) is now the strongly recommended operational call)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~1h43m elapsed, 35 shards / 72 MB written, sustained throughput ~170 spectra/min — correcting downward the Wave 14-F header read of \"275 spectra/min\" which was an arithmetic over-read; at the actual sustained rate the 1M ETA is ~98 h, 100K sub-sample short-circuit (~10 h) is now the strongly recommended operational call)",
    },
  ],
};
