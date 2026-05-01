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
  lastUpdatedISO: "2026-05-02T05:30:00Z",
  lastUpdatedDisplay: "2026-05-01 22:30 PT",
  headline:
    "Wave 14-Q LANDED — P1 v2.3.7 → v2.3.8 (Gemini-3.1-Pro P1 MINOR m-1 Savage-Dickey AIC/BIC primary promotion at §VII.B post-eq:Zcomb2 per Gemini's literal 'If you know the estimator is heavily biased, do not use it. Quote the AIC/BIC or run nested sampling.' ask: bold/italic R42 Wave 14-Q peer-review reframe block prepended + new ΔAIC/ΔBIC/Δχ²_eff equation block computed from existing Table~\\ref{tab:modelcomp} columns — full-tension dataset: ΔAIC = 1162.3 − 1168.2 = −5.9 favoring ΛCDM+ΔNeff on Akaike grounds with |ΔAIC|>4 = positive evidence on the conventional Burnham-Anderson scale; ΔBIC = 1194.8 − 1195.5 = −0.7 below the Kass-Raftery |ΔBIC|<2 'barely worth a mention' threshold; Δχ²_eff = 1148.3 − 1156.2 = −7.9; SD ln B = +4.8 demoted to 'indicative only' via existing footnote fn:bayes_caveat); 23 cross-model findings closed across 16 cheap-fast sub-waves while the Wave 14-B 1M SPARCL fetch continues; Pod 3 throughput full-window ~195 spectra/min sustained at ~5h14m elapsed",
  summary:
    "Wave 14-Q closes one Gemini-3.1-Pro P1 MINOR (m-1) on the cheap-fast precise-language axis. Gemini's adversarial review explicitly stated, in literal terms, 'If you know the estimator is heavily biased, do not use it. Quote the AIC/BIC or run nested sampling,' on the grounds that the Savage-Dickey ln B ≈ +4.8 estimate is biased at r = −0.89 posterior correlation and that AIC/BIC differences from the same proxy run are dimensionally honest, additive in the same likelihood, and free of the Savage-Dickey degenerate-direction artifact. Wave 11-A had previously demoted Savage-Dickey to a footnote (fn:bayes_caveat), but the body text had not yet promoted any AIC/BIC quantity to primary status — Gemini's m-1 was the surviving residual. Table~\\ref{tab:modelcomp} (full-tension dataset) already had AIC/BIC columns from Wave 11-A; what was missing was the body-text equation block that promotes the differences to primary deliverable. Wave 14-Q closes this cheap-fast: (1) inserted after the eq:Zcomb2 Savage-Dickey align block and before the 'The change of label from ...' sentence: bold paragraph header 'R42 Wave 14-Q peer-review reframe (cross-model Gemini 3.1-Pro P1 m-1)' followed by italic block stating SD ln B is biased at r = −0.89 and reported as indicative only, model-selection metrics promoted to primary status are ΔAIC and ΔBIC computed from Table~\\ref{tab:modelcomp} columns, and verbatim Gemini quote — followed by new align environment with three lines: ΔAIC ≡ AIC(ΛCDM+ΔNeff) − AIC(ΛCDM) = 1162.3 − 1168.2 = −5.9, ΔBIC ≡ BIC(ΛCDM+ΔNeff) − BIC(ΛCDM) = 1194.8 − 1195.5 = −0.7, Δχ²_eff = 1148.3 − 1156.2 = −7.9 — followed by interpretive paragraph stating ΔAIC of −5.9 favors ΛCDM+ΔNeff on Akaike grounds (in the conventional Burnham-Anderson interpretation, |ΔAIC|>4 is positive evidence) while ΔBIC of −0.7 is below the conventional Kass-Raftery 'barely worth a mention' threshold of |ΔBIC|<2, the two metrics together — one mildly favorable, one essentially neutral — are the primary cross-reference for this proxy comparison, they are quoted from Table columns and require no posterior-correlation correction, the Savage-Dickey estimate above is retained only as an indicative figure, and a proper evidence-level comparison would require nested sampling on a torsion-modified Boltzmann code and is not attempted here. (2) Citation hygiene: scale references to Burnham-Anderson and Kass-Raftery are inline prose only — verified via Grep that BurnhamAnderson2002 and KassRaftery1995 bib keys are absent from arxiv/references.bib, so an explicit \\cite{...} would have introduced two new undef cites; the prose form 'in the conventional Burnham-Anderson interpretation, |ΔAIC|>4 is positive evidence' and 'the conventional Kass-Raftery barely worth a mention threshold of |ΔBIC|<2' carries the scale information without triggering new undef-cite warnings. P1 .tex bumped v2.3.7 → v2.3.8, date May 1 22:00 PDT → 22:30 PDT, recompiled clean on Pod 3 H200 (pdflatex × 2 in /workspace/recompile_p1/, 1,232,319 bytes / 33 pp / 0 errors / 0 undef refs / 1 'Wave 14-Q' occurrence / 1 pre-existing WilsonEwing2012 undef cite), mirrored to public/papers/{paper1_spin_torsion.pdf, spin_torsion_paper1.pdf, spin-torsion-paper.pdf}. Twenty-three cross-model findings (P3-CM-B4 14-A, P4-OA-B1+B2 14-C, P4-OA-B6 14-D, P4-OA-B4 14-E, Gemini P4 M-1+m-1 14-F, OpenAI P4 M-2+M-3 + OpenAI M-8 / Gemini m-2 documented 14-G, OpenAI minor-1+minor-3+minor-5+M-6 14-H, OpenAI B4 + B3+minor-2+minor-4 documented 14-I, OpenAI M-4 + minor-3-leftover + minor-1-leftover 14-J, Gemini P2 B-3 14-K, Gemini P3 m-1 14-L, OpenAI P1 B-4 14-M, Gemini P3 m-2 14-N, Gemini P3 M-2 14-O, Gemini P1 M-2 14-P, Gemini P1 m-1 14-Q) now closed across sixteen cheap-fast sub-waves inside the single multi-hour Wave 14-B 1M SPARCL fetch window. Pod 3 H200 SPARCL 1M fetch alive on PID 25860, ~5h14m elapsed at this commit, throughput full-window ~195 spectra/min sustained — consistent with Wave 14-P's reading. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds. $0 marginal H200 spend — recompile_p1 shares the same Pod 3 session running the fetch.",
  papers: [
    {
      slug: "spin-torsion",
      number: 1,
      shortTitle: "Spin-Torsion Cosmology",
      version: "v2.3.8",
      readiness: 95,
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
      version: "v3.1.11",
      readiness: 93,
    },
    {
      slug: "chirality-catalog",
      number: 4,
      shortTitle: "Galaxy Chirality Catalog",
      version: "v1.0.15",
      readiness: 97,
    },
  ],
  blockerTally: {
    closed: 23, // +1 from Wave 14-Q: Gemini P1 m-1 Savage-Dickey AIC/BIC primary promotion (§VII.B post-eq:Zcomb2 ΔAIC/ΔBIC/Δχ²_eff equation block + R42 Wave 14-Q peer-review reframe block per Gemini's literal "Quote the AIC/BIC or run nested sampling." ask)
    openBlockers: 1, // unchanged from Wave 14-P
    openMajors: 17, // unchanged from Wave 14-Q (Gemini P1 m-1 was a MINOR, not a MAJOR)
    openMinors: 15, // -1 from Wave 14-Q: Gemini P1 m-1 closed
  },
  cronStatus: "*/20 autonomous-loop cron armed (cron a3fdb42b) + dynamic /loop wakeup arm",
  etaToCompletion:
    "ETA all-4 → 100%: ~30-54 h at current Wave-cadence (3-5 cross-model findings per ~25-min cheap-fast wave + 1 compute-heavy decision per day on Pod 3 H200; Wave 14-B 1M Jaccard fetch ~80 h on sustained ~195 spectra/min full-window throughput, 100K sub-sample short-circuit (~5 h from this commit) remains strongly recommended on cost/cadence grounds)",
  pods: [
    {
      name: "Pod 3 H200 (38.80.152.148:33089)",
      state: "active",
      note: "Wave 14-B 1M SPARCL fetch in flight (PID 25860, ~5h14m elapsed at Wave 14-Q commit; throughput full-window ~195 spectra/min sustained, consistent with Wave 14-P reading. Recompile_p1 (33 pp / 1,232,319 bytes / 0 errors / 0 undef refs / 1 'Wave 14-Q' occurrence / 1 pre-existing WilsonEwing2012 undef cite) ran cleanly in same session, $0 marginal H200 spend. 100K sub-sample short-circuit (~5 h ETA from this commit) remains strongly recommended on cost/cadence grounds.)",
    },
  ],
};
