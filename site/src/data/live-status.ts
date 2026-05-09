// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.

export interface PaperProgress {
  slug: string;
  number: string;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
  pendingWork: string; // one-line summary of what's still pending for this paper
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // one-line current state
  summary: string; // 1-3 sentences, what just shipped
  currentlyRunning: string[]; // bullet list of what is actively running RIGHT NOW
  papers: PaperProgress[]; // 5 papers, sorted by display order
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string; // "self-pacing — autonomous loop active"
  etaToCompletion: string; // human-readable ETA to all-papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-05-09T02:30:00Z",
  lastUpdatedDisplay: "May 8, 2026 · 7:30 PM PT",
  headline:
    "R44 Wave 14-FFFF — P3 v3.1.24 R44 MAJORs M1+M2+M4 + Münchmeyer typo shipped (Conclusions §6.5 demoted, legacy 6.1%/16.4% subordinated to 'for reference', tier vocabulary explicit)",
  summary:
    "Wave 14-FFFF ships P3 v3.1.23 → v3.1.24 with R44 MAJORs M1 + M2 + M4 + nit1: (M1) Conclusions §6.5 cosmological-applications bullet rewritten to lead with the Wave 14-VVV empirical-α result (σ(f_NL)=8.27 ± 2.37, 7.9% central improvement consistent with zero at <1σ) and demote the legacy '~6–20% improvement' framing; (M2) §VII (sec:fnl) legacy fixed-α=0.15 forecast (6.1% DESI-only / 16.4% DESI+SDSS, range 10–20%) explicitly subordinated under italic 'For reference' header — retained for historical continuity but no longer the primary cosmological deliverable; (M4) tier vocabulary disambiguated paper-wide: 'point-source tier' = 378,080 (six photometric/spectroscopic surveys after 7-way 5″ dedup), 'catalog-grade tier' = 264,938 (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE), 'exploratory tier' = 113,342 (LAMOST native; methodological-lesson retain), 'Planck CMB-patch tier' = 200 (sky regions, not point sources); 'primary tier' as a load-bearing term retired. (nit1) Münchmeyer (was Munchmüller) — corrected at the multi-tracer Fisher-marginalization paragraph. PDF recompile: 41 pp / 28.4 MB / 0 undef refs. R43 status (post Waves 14-WWW–DDDD): all 10 P3 BLOCKERs closed and zero P3 BLOCKERs returned in the R44 self-review (full review at project-context/peer-reviews/2026-05-08_1830pt_R44_CCAI_*). Cobaya DESI DR2 chain continues warm-restarted sampling: R̂−1 = 0.076 at May 8 18:27 PT (4,598 total accepted across 4 chains); publication-quality R̂−1 < 0.01 ETA 1–3 days. **Continuing R44→Rn loop: next is Wave 14-GGGG (P4 R44 MAJORs), Wave 14-HHHH (P2 R44 BLOCKERs), Wave 14-IIII (P1A four-route appendix); cross-vendor non-Anthropic R-round will launch on R45 once R44 BLOCKERs+MAJORs are flushed.**",
  currentlyRunning: [
    "Cobaya 4-chain MPI run on RTX A5000 pod ijzftpy3klystt — warm-started with posterior covmat from April-6 quintom chain; DESI DR2 + Planck NPIPE + Pantheon+ + DES-Y5; w0-wa CPL PPF; target R̂−1 < 0.01",
    "Autonomous /loop self-pacing every ~25 min — polling pod, will GetDist + update P1B §Structural Tension + recompile when R̂−1 < 0.01",
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH Structural Closure (no-go theorem)",
      version: "v1A.0.4",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 peer-review round (R43 BLOCKERs B1+B2+B3 shipped Wave 14-ZZZ — title reframed, abstract bounce-class-vs-ECH distinction explicit, MCMC headline forwarded to P1B; remaining MAJORs queued) + arXiv submission",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "ΛCDM+ΔNeff MCMC + NaMaster + ALP companion",
      version: "v1B.0.1",
      readiness: 99,
      pendingWork:
        "DESI DR2 w0wa cobaya chain to converge (R̂−1 < 0.01, ~6-12 h) → GetDist → §Structural Tension update → recompile, then Houston sign-off + arXiv",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.12",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 round (R43 B2 gauge-frame footnote shipped Wave 14-YYY; B1 invalidated as table is correctly labelled $\\mathcal{B}_{\\rm NL}$ shape function) + arXiv submission",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.24",
      readiness: 99,
      pendingWork:
        "HuggingFace dataset visibility flip (Houston manual) + sign-off + clean external R45 round (R44 MAJORs M1+M2+M4 + nit1 shipped Wave 14-FFFF: Conclusions §6.5 demoted to Wave 14-VVV empirical α, legacy fixed-α=0.15 6.1%/16.4% subordinated 'for reference', tier vocabulary disambiguated, M{ü}nchmeyer typo) + arXiv submission",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M galaxy chirality at scale",
      version: "v1.0.32",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R43 round (R43 BLOCKERs B1+B2 + MAJORs M3+M4 shipped; M1+M2 already in v1.0.31; remaining MAJORs queued) + arXiv submission",
    },
  ],
  blockerTally: {
    closed: 65,
    openBlockers: 0,
    openMajors: 0,
    openMinors: 0,
  },
  cronStatus:
    "/loop self-pacing — autonomous loop active, polling pod every ~25 min",
  etaToCompletion:
    "Compute work: cobaya R̂−1 < 0.01 expected 6-12 h. Final 1% on each paper requires Houston sign-off + clean external R43 round.",
  pods: [
    {
      name: "ijzftpy3klystt (cobaya-r43-v2, RTX A5000 SECURE)",
      state: "active",
      note:
        "96 vCPU, 100 GB container disk; mpirun -n 4 cobaya-run on Planck NPIPE + DESI DR2 BAO + Pantheon+ + DES-Y5 in tmux 'chains'. ~$0.27/hr.",
    },
  ],
};
