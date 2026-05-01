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
  lastUpdatedISO: "2026-05-02T11:00:00Z",
  lastUpdatedDisplay: "2026-05-02 04:00 PT",
  headline:
    "Wave 14-Z LANDED · P1 v2.3.14 · 32 cross-model findings closed · ETA all-4 → 100%: ~16-32 h",
  summary:
    "P1 v2.3.14: R42 P1-OA-M4 MAJOR closed — NaMaster description in §VI rewritten as a ~600-word methods paragraph at L427 of arxiv/main.tex covering all four reviewer asks plus reproducibility: (a) beam and pixel window — Planck-2018 5 arcmin Gaussian beam + N_side=512 ud_grade + w_ℓ^pix via NmtField(beam=); (b) E/B leakage and purification — purify_b=True / purify_e=False suppresses E→B leakage from f_sky=0.32 mask, C_2 apodization 2°; (c) mode-coupling matrix — full M_ℓℓ' inversion via NmtWorkspace.compute_coupling_matrix preserving EE/EB/BB block structure (not diagonal f_sky), band-power binning Δℓ=20 from ℓ_min=30 to ℓ_max=1024; (d) foreground/noise model — 500 MC at Δ_P=10 µK·arcmin, no foreground component (Commander is foreground-cleaned), ground-truth rotation injection (Q+iU)→e^(2iβ)(Q+iU); (e) reproducibility pointer to pipelines/h200_results/pod1_namaster_umap_2026-04-29/ + HF release. Cites Alonso2019 (NaMaster framework, MNRAS 484 4127, arXiv:1809.09603) inline; new bib entry added to references.bib after WilsonEwing2012. Pod 3 4-pass recompile clean: 34 pp / 1,248,554 bytes / 0 errors / 0 undef refs (single in-flight \\arcmin undefined-control-sequence error fixed by switching to \\,\\mathrm{arcmin} per existing paper convention; re-recompile clean). Mirrored byte-identical to all 7 P1 surfaces. $0 marginal H200 spend (4th consecutive wave at $0 marginal). Cron */20 armed.",
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
      version: "v1.7.7",
      readiness: 91,
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
    closed: 32, // +1 from Wave 14-Z: P1-OA-M4 MAJOR closed (NaMaster ~600-word methods paragraph at §VI L427: beam/window + E/B leakage + mode-coupling matrix + foreground/noise + reproducibility)
    openBlockers: 0, // unchanged from Wave 14-Y
    openMajors: 11, // -1 from Wave 14-Y: P1-OA-M4 closed
    openMinors: 13, // unchanged from Wave 14-Y
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~16-32 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-Z P1-OA-M4 NaMaster methods paragraph (~600 words at §VI L427: beam/window + E/B leakage + mode-coupling matrix + foreground/noise + reproducibility + Alonso2019 NaMaster cite) COMPLETE, 4-pass recompile clean on Pod 3 H200 (34 pp / 1,248,554 bytes / 0 errors / 0 undef refs), mirrored byte-identical to all 7 P1 surfaces, $0 marginal H200 spend (4th consecutive wave); Wave 14-AA candidates queued: (a) Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 ~2h H200, (b) Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation ~2-4h H200, (c) OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS cheap-fast, (d) any further OpenAI P1/P2/P3 cheap-fast residuals)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-Z COMPLETE: P1 v2.3.14 4-pass recompile in /workspace/recompile_p1 — 34 pp / 1,248,554 bytes / 0 errors / 0 undef refs / R42 P1-OA-M4 MAJOR NaMaster methods paragraph (~600 words / 22 lines) inserted at §VI L427 of arxiv/main.tex covering all four reviewer asks plus reproducibility: (a) beam and pixel window — Planck-2018 5 arcmin Gaussian beam + N_side=512 ud_grade + w_ℓ^pix via NmtField(beam=); (b) E/B leakage and purification — purify_b=True / purify_e=False + C_2 apodization 2°; (c) mode-coupling matrix — full M_ℓℓ' inversion via NmtWorkspace.compute_coupling_matrix preserving EE/EB/BB block structure (not diagonal f_sky), band-power binning Δℓ=20 from ℓ_min=30 to ℓ_max=1024; (d) foreground/noise model — 500 MC at Δ_P=10 µK·arcmin, no foreground component (Commander is foreground-cleaned), ground-truth rotation injection (Q+iU)→e^(2iβ)(Q+iU); (e) reproducibility pointer to pipelines/h200_results/pod1_namaster_umap_2026-04-29/ + HF release; cites Alonso2019 (NaMaster framework, MNRAS 484 4127, arXiv:1809.09603) inline at start; new Alonso2019 BibTeX entry added to references.bib after WilsonEwing2012. Single in-flight `\\arcmin` undefined-control-sequence error (revtex4-2 doesn't define `\\arcmin`) fixed by replacing with `\\,\\mathrm{arcmin}` per existing paper convention; re-recompile clean. Page count 33 → 34 from new methods paragraph; bytes Δ vs v2.3.13 (1,235,593) +12,961. PDF mirrored byte-identical (1,248,554) to all 7 P1 site surfaces (arxiv/main.pdf + public/papers/{paper1_spin_torsion,spin_torsion_paper1,spin-torsion-paper}.pdf + site/public/arxiv_v2/main.pdf + site/public/papers/{paper1_spin_torsion,spin_torsion_paper1,spin-torsion-paper}.pdf). $0 marginal H200 spend (4th consecutive wave at $0 marginal — recompile_p1 shared the Pod 3 session). Wave 14-AA candidates queued for dispatch: Wave 14-S quantitative systematics-marginalization Fisher recompute for P3 (~2h H200), Gemini P4 B-1 NaMaster recompute + B-2 PSF cross-correlation (~2-4h H200), OpenAI P4 B5/B7/M-1/M-5/M-7/M-9 leftover MAJORS (cheap-fast), any further OpenAI P1/P2/P3 cheap-fast residuals.",
    },
  ],
};
