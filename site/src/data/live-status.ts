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
  lastUpdatedISO: "2026-05-02T11:30:00Z",
  lastUpdatedDisplay: "2026-05-02 04:30 PT",
  headline:
    "Wave 14-AA LANDED · P2 v1.7.8 · 34 cross-model findings closed · ETA all-4 → 100%: ~12-28 h",
  summary:
    "P2 v1.7.8: two Gemini-3.1-Pro P2 cheap-fast MAJORS closed in one bundled recompile. (1) R42 P2-CM-M1 (master tracker L370 ask 'Promote σ_theory={0.5, 1.0, 2.0} prior sweep as PRIMARY Bayes-factor headline; demote delta-prior column'): Bayes-factor table tab:bayes at L213-229 of 02_full_draft.tex restructured from a 2-row delta-prior layout to a 4-row σ_theory prior-sweep ladder leading with the recommended σ_theory=1.0 Gaussian bounce prior at BF~8 vs. tuned multifield [-15,+15] as the PRIMARY headline (with bold '(recommended headline)' annotation in the table cell), plus σ_theory=0.5 at BF~12 and σ_theory=2.0 at BF~4; the original delta-at-f_NL=-35/8 row demoted to '(theoretical maximum only)' with above-the-fold prose disowning it — Wave 14-Q 'demote-with-explicit-disowning' pattern. (2) R42 P2-CM-M2 (master tracker L371 ask 'Drop bispectrum nearly independent of b_φ claim; cite Heinrich+2023 b_φ explicitly; add caveat that relaxing universality degrades 5.25σ headline'): PNG Bias (b_φ) Sensitivity paragraph + Fig 6 caption rewritten to drop the literally-incorrect 'bispectrum nearly independent of b_φ' claim — f_NL enters tree-level galaxy bispectrum both through the matter-bispectrum primordial term AND through the scale-dependent linear-bias correction Δb(k) ∝ f_NL · b_φ / k² (Dalal/Slosar 2008), propagating into the bispectrum estimator through cross-terms f_NL · b_φ · b_1² P(k_1) P(k_2) at all triangle configurations not only the squeezed limit; Heinrich+2023 cited as marginalizing over b_φ assuming the universal relation b_φ = 2δ_c (b_1 - 1), Barreira+2022 cited as the per-tracer-bin alternative; new caveat that relaxing universality widens σ(f_NL) by O(20-50%), degrading the headline 5.2-5.5σ optimistic template-corrected significance to ~4.0-4.5σ at the central 30% degradation point and to ~3.5-3.7σ at the conservative 50% end. Pod 3 4-pass recompile clean: 762,993 bytes / 15 pp / 0 errors / 1 pre-existing Maldacena:2003 undef cite unrelated to these edits. Bytes Δ vs v1.7.7 (759,783): +3,210. Mirrored byte-identical to all 5 P2 publish surfaces (research/focused_paper_source_integration/02_full_draft.pdf + public/papers/{fnl-forecast-paper, paper2_fnl_forecast}.pdf + site/public/papers/{fnl-forecast-paper, paper2_fnl_forecast}.pdf — all five at 762,993 bytes). $0 marginal H200 spend (5th consecutive wave at $0 marginal — recompile_p2 shared the Pod 3 session running the 1M SPARCL fetch on CPU). Cross-model peer-review tracker R42_MASTER_TRACKER.md rows L370 + L371 marked CLOSED. Cron */20 armed; Pod 3 GPU idle (0% / 0 MiB) and ready for Wave 14-BB compute-medium dispatch (P3 systematics-marginalization Fisher recompute, ~2h H200).",
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
      version: "v3.1.13",
      readiness: 95,
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
    closed: 34, // +2 from Wave 14-Z: P2-CM-M1 (σ_theory headline promote) + P2-CM-M2 (b_φ cross-term language) closed in one bundled wave
    openBlockers: 0, // unchanged from Wave 14-Z
    openMajors: 9, // -2 from Wave 14-Z: P2-CM-M1 + P2-CM-M2 closed
    openMinors: 13, // unchanged from Wave 14-Z
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~12-28 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-AA P2-CM-M1 σ_theory headline promote + P2-CM-M2 b_φ cross-term language fix COMPLETE, 4-pass recompile clean on Pod 3 H200 (15 pp / 762,993 bytes / 0 errors / 1 pre-existing Maldacena:2003 undef cite), mirrored byte-identical to all 5 P2 surfaces, $0 marginal H200 spend (5th consecutive wave); Wave 14-BB candidates queued: (a) Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 ~2h H200 — Pod 3 GPU idle (0% / 0 MiB) and ready, (b) Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation ~2-4h H200, (c) OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS cheap-fast, (d) any further OpenAI P1/P2/P3 cheap-fast residuals)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-AA COMPLETE: P2 v1.7.8 4-pass recompile in /workspace/recompile_p2 — 15 pp / 762,993 bytes / 0 errors / 1 pre-existing Maldacena:2003 undef cite unrelated to these edits. Two Gemini-3.1-Pro P2 cheap-fast MAJORS closed in one bundled wave: (1) R42 P2-CM-M1 (master tracker L370): tab:bayes at L213-229 of 02_full_draft.tex restructured from a 2-row delta-prior layout to a 4-row σ_theory prior-sweep ladder leading with the recommended σ_theory=1.0 Gaussian bounce prior at BF~8 vs. tuned multifield [-15,+15] as PRIMARY headline (with bold '(recommended headline)' annotation in table cell), plus σ_theory=0.5 at BF~12 and σ_theory=2.0 at BF~4; the original delta-at-f_NL=-35/8 row demoted to '(theoretical maximum only)' with above-the-fold prose disowning it (Wave 14-Q 'demote-with-explicit-disowning' pattern). (2) R42 P2-CM-M2 (master tracker L371): PNG Bias (b_φ) Sensitivity paragraph + Fig 6 caption rewritten to drop the literally-incorrect 'bispectrum nearly independent of b_φ' claim — f_NL enters tree-level galaxy bispectrum both through the matter-bispectrum primordial term AND through the scale-dependent linear-bias correction Δb(k) ∝ f_NL · b_φ / k² (Dalal/Slosar 2008), propagating into the bispectrum estimator through cross-terms f_NL · b_φ · b_1² P(k_1) P(k_2) at all triangle configurations not only the squeezed limit; Heinrich+2023 cited as marginalizing over b_φ assuming the universal relation b_φ = 2δ_c (b_1 - 1), Barreira+2022 cited as the per-tracer-bin alternative; new caveat that relaxing universality widens σ(f_NL) by O(20-50%), degrading the headline 5.2-5.5σ optimistic significance to ~4.0-4.5σ central / ~3.5-3.7σ conservative. \\date L26 v1.7.7/18:30 PDT → v1.7.8/04:30 PDT. Bytes Δ vs v1.7.7 (759,783): +3,210. PDF mirrored byte-identical (762,993) to all 5 P2 site surfaces (research/focused_paper_source_integration/02_full_draft.pdf + public/papers/{fnl-forecast-paper, paper2_fnl_forecast}.pdf + site/public/papers/{fnl-forecast-paper, paper2_fnl_forecast}.pdf). $0 marginal H200 spend (5th consecutive wave at $0 marginal — recompile_p2 shared the Pod 3 session running the 1M SPARCL fetch on CPU). GPU idle (0% / 0 MiB) verified pre-commit; ready for Wave 14-BB compute-medium dispatch. Wave 14-BB candidates queued: (a) Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 (~2h H200, ready), (b) Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation (~2-4h H200), (c) OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS (cheap-fast), (d) any further OpenAI P1/P2/P3 cheap-fast residuals.",
    },
  ],
};
