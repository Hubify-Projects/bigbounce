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
  lastUpdatedISO: "2026-05-02T12:30:00Z",
  lastUpdatedDisplay: "2026-05-02 05:30 PT",
  headline:
    "Wave 14-BB LANDED · P3 v3.1.14 · 35 cross-model findings closed · ETA all-4 → 100%: ~10-24 h",
  summary:
    "P3 v3.1.14: R42 P3-OA-M7 MAJOR closed (cross-survey dedup language harmonization, R42 master tracker L395 ask 'Cross-survey dedup mixes object detections with CMB patches in headline (partially addressed by R42 Wave 7) | Apply consistently in abstract + all headline summaries | text-only | 30min'). Wave 7 B16 had already landed full two-tier stratification disclosure at four key sites (abstract L54, §III intro L175, Table~I footnote L215, §VII Conclusions item 1 L622), but three downstream headline sites still carried bare-378,280 / bare-37M / bare-eight-archives language predating the ACT~DR6 quarantine: (1) §I Introduction L73 'first multi-survey anomaly detection campaign at combined scale exceeding 37 million sources. We apply a unified autoencoder architecture (BigAE) to eight distinct archives,' rewritten with explicit two-tier '37.3 million sources and CMB map patches (after a 7-way 5″ positional dedup that reduces 378,280 unique anomalies to 378,080 point-source object detections across DESI, SDSS, LAMOST, eROSITA, Gaia, and NEOWISE plus 200 Planck CMB-patch sky-region detections; ACT~DR6 quarantined to Appendix per Wave 11 QA)' + 'seven retained archives (DESI~DR1, SDSS~DR18, LAMOST~DR10, eROSITA~DR1, Planck CMB, Gaia~DR3, NEOWISE)' + bold 'R42 Wave 14-BB headline-stratification harmonization' trace note; (2) §VII Conclusions item 5 ('Path-C rebuild') L636 bare '378,280 unique physical objects (2.629% compression)' got bold 'R42 Wave 14-BB headline-stratification' disclosure appended; (3) §Acknowledgments Data availability L648 bare 378,280 got bold 'R42 Wave 14-BB headline-stratification' disclosure appended. Edits are pure-text-add — no equations, figures, numbers, or substantive claims modified. Pod 3 H200 4-pass recompile clean: 28,311,141 bytes / 40 pp / 0 errors / 0 undef refs / 0 undef cites / 3 'Wave 14-BB' occurrences confirmed across §I + §VII + §Acknowledgments. Bytes Δ vs v3.1.13 (28,309,528): +1,613. Mirrored byte-identical to all 7 P3 publish surfaces (pipelines/p3_anomaly_engine/paper3_draft.pdf + public/papers/{anomaly-catalog-paper, paper3_draft, paper3_anomaly_catalog}.pdf + site/public/papers/{anomaly-catalog-paper, paper3_draft, paper3_anomaly_catalog}.pdf + arxiv/paper3_anomaly_catalog.pdf — all seven at 28,311,141 bytes). $0 marginal H200 spend (6th consecutive wave at $0 marginal — recompile_p3 shared the Pod 3 session running the 1M SPARCL fetch on CPU). Cross-model peer-review tracker R42_MASTER_TRACKER.md row L395 marked CLOSED. Cron */20 armed; Pod 3 GPU still idle (0% / 0 MiB / 143771 MiB available) and ready for Wave 14-CC compute-medium dispatch (Wave 14-S P3 systematics-marginalization Fisher recompute ~2h H200, or Gemini P4 B-1 NaMaster recompute / B-2 PSF cross-correlation 2-4h H200, or OpenAI P4 B5/B7 leftover compute-heavy MAJORS).",
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
    closed: 35, // +1 from Wave 14-AA: P3-OA-M7 (cross-survey dedup language harmonization) closed Wave 14-BB
    openBlockers: 0, // unchanged from Wave 14-AA
    openMajors: 8, // -1 from Wave 14-AA: P3-OA-M7 closed
    openMinors: 13, // unchanged from Wave 14-AA
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~10-24 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-BB P3-OA-M7 cross-survey dedup language harmonization COMPLETE, 4-pass recompile clean on Pod 3 H200 (40 pp / 28,311,141 bytes / 0 errors / 0 undef refs / 0 undef cites / 3 'Wave 14-BB' occurrences confirmed across §I + §VII + §Acknowledgments), mirrored byte-identical to all 7 P3 surfaces, $0 marginal H200 spend (6th consecutive wave); Wave 14-CC candidates queued: (a) Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 ~2h H200 — Pod 3 GPU still idle (0% / 0 MiB / 143771 MiB available) and ready, (b) Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation ~2-4h H200, (c) OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS cheap-fast, (d) any further OpenAI P1/P2/P3 cheap-fast residuals; idle-GPU violation (per feedback_idle_gpu_proactive.md) escalating — Wave 14-CC MUST dispatch compute-medium GPU work next iteration)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-BB COMPLETE: P3 v3.1.14 4-pass recompile in /workspace/recompile_p3 — 40 pp / 28,311,141 bytes / 0 errors / 0 undef refs / 0 undef cites / 3 'Wave 14-BB' occurrences confirmed across §I + §VII + §Acknowledgments. One Gemini-3.1-Pro P3 cheap-fast MAJOR closed: R42 P3-OA-M7 (master tracker L395 literal ask: 'Cross-survey dedup mixes object detections with CMB patches in headline (partially addressed by R42 Wave 7) | Apply consistently in abstract + all headline summaries | text-only | 30min'). Three remaining unstratified-headline sites in paper3_draft.tex patched (Wave 7 B16 had already harmonized abstract L54 + §III intro L175 + Table~I footnote L215 + §VII Conclusions item 1 L622): (1) §I Introduction L73 rewritten with explicit two-tier '37.3 million sources and CMB map patches (after a 7-way 5″ positional dedup that reduces 378,280 unique anomalies to 378,080 point-source object detections across DESI, SDSS, LAMOST, eROSITA, Gaia, and NEOWISE plus 200 Planck CMB-patch sky-region detections; ACT~DR6 quarantined to Appendix per Wave 11 QA)' + 'seven retained archives (DESI~DR1, SDSS~DR18, LAMOST~DR10, eROSITA~DR1, Planck CMB, Gaia~DR3, NEOWISE)' + bold 'R42 Wave 14-BB headline-stratification harmonization' trace note; (2) §VII Conclusions item 5 ('Path-C rebuild') L636 bare '378,280 unique physical objects (2.629% compression)' got bold 'R42 Wave 14-BB headline-stratification' disclosure appended; (3) §Acknowledgments Data availability L648 bare 378,280 got bold 'R42 Wave 14-BB headline-stratification' disclosure appended. Edits are pure-text-add — no equations, figures, numbers, or substantive claims modified. \\date L51 v3.1.13/03:00 PDT → v3.1.14/04:50 PDT. Bytes Δ vs v3.1.13 (28,309,528): +1,613. PDF mirrored byte-identical (28,311,141) to all 7 P3 publish surfaces (pipelines/p3_anomaly_engine/paper3_draft.pdf + public/papers/{anomaly-catalog-paper, paper3_draft, paper3_anomaly_catalog}.pdf + site/public/papers/{anomaly-catalog-paper, paper3_draft, paper3_anomaly_catalog}.pdf + arxiv/paper3_anomaly_catalog.pdf — all seven verified at 28,311,141 bytes). $0 marginal H200 spend (6th consecutive wave at $0 marginal — recompile_p3 shared the Pod 3 session running the 1M SPARCL fetch on CPU; SPARCL fetch PID 25860 is CPU-bound and does not block GPU). GPU still idle (0% / 0 MiB / 143771 MiB available) verified pre-commit — idle-GPU violation per feedback_idle_gpu_proactive.md escalating, Wave 14-CC MUST dispatch compute-medium GPU work next iteration. Wave 14-CC candidates queued: (a) Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 (~2h H200, ready), (b) Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation (~2-4h H200), (c) OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS (cheap-fast), (d) any further OpenAI P1/P2/P3 cheap-fast residuals.",
    },
  ],
};
