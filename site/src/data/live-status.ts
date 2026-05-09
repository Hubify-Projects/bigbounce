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
  lastUpdatedISO: "2026-05-09T05:00:00Z",
  lastUpdatedDisplay: "May 8, 2026 · 10:00 PM PT",
  headline:
    "R44 Wave 14-KKKK — P3 v3.1.25 high-confidence-restricted α re-measurement shipped: α_GS,jk = +1.83 ± 2.03 on 1,122 Gold+Silver subset (Path B closure), σ(f_NL)_GS = 2.28 ± 7.43 reported alongside full-sample α_jk = 0.19 headline",
  summary:
    "Wave 14-GGGG ships P4 v1.0.32 → v1.0.33 with R44 MAJORs M1+M2+M3 + nit2: (M1) p_LEE harmonization at three abstract/body/discussion sites — the point estimate $9.999\\times 10^{-5}$ replaced everywhere with the MC-resolution upper bound $p_{\\rm LEE}<10^{-4}$ (and explicit prose noting that $1/(N_{\\rm MC}+1)$ is a sample-size floor, not a measured probability density). Abstract paren-mismatch typo cleaned. (M2) GZ1 Platt parameters now reported to six significant figures: GZ1-recalibrated $A = 0.215143$, $B = -1.581205$ vs CE-ResNet $A = 0.215127$, $B = -1.581389$ — agreement at $|\\Delta A|=1.6\\times 10^{-5}$, $|\\Delta B|=1.8\\times 10^{-4}$ (precision-of-fit floor, not a 4-sig-fig rounding artifact). (M3) GZ1 48.4% vs Catalog-C 49.7% CW-fraction gap reframed as a paired McNemar test (b=4,205, c=3,607, $\\chi^2_1 = 598^2/7{,}812 = 45.78$, $Z=6.77$); the unpaired binomial 5.5σ formula in earlier versions undercounted because per-galaxy Catalog-C ↔ GZ1 correlations reduce the effective variance below the uncorrelated null. The reframing actually strengthens the gap from 5.5σ to 6.77σ rather than weakening it; both papers' interpretation (gap consistent with combined ~1% GZ1 + ~0.5% Cat-C systematic floors, monopole not parity test) unchanged. (nit2) Stray `PUSHBACK` prose tokens swept (Sec VI.D bin-flatness 'PUSHBACK with reframe' → 'non-flatness'; closure stance label normalized to 'closed'). PDF: 22 pp / 25.65 MB / 0 undef refs. Wave 14-FFFF predecessor (P3 v3.1.23 → v3.1.24): Conclusions §6.5 cosmological-applications bullet rewritten to lead with Wave 14-VVV empirical α (σ(f_NL)=8.27±2.37 forecast, consistent with zero at <1σ); §VII legacy fixed-α=0.15 forecast (6.1% / 16.4%) subordinated under italic 'For reference' header; tier vocabulary disambiguated paper-wide (point-source 378,080 + catalog-grade 264,938 + exploratory 113,342 + Planck CMB-patch 200); Münchmeyer typo fix. R43 status (post Waves 14-WWW–DDDD): all 10 P3 BLOCKERs closed and zero P3 BLOCKERs returned in the R44 self-review. Cobaya DESI DR2 chain continues warm-restarted sampling: R̂−1 = 0.076 at May 8 18:27 PT (4,598 total accepted across 4 chains); publication-quality R̂−1 < 0.01 ETA 1–3 days. **Continuing R44→Rn loop: next is Wave 14-HHHH (P2 R44 BLOCKERs B1+B2 + MAJORs), Wave 14-IIII (P1A four-route appendix); cross-vendor non-Anthropic R-round will launch on R45 once R44 BLOCKERs+MAJORs are flushed.**",
  currentlyRunning: [
    "Cobaya 4-chain MPI run on RTX A5000 pod ijzftpy3klystt — warm-started with posterior covmat from April-6 quintom chain; DESI DR2 + Planck NPIPE + Pantheon+ + DES-Y5; w0-wa CPL PPF; target R̂−1 < 0.01",
    "Autonomous /loop self-pacing every ~25 min — polling pod, will GetDist + update P1B §Structural Tension + recompile when R̂−1 < 0.01",
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH Structural Closure (no-go theorem)",
      version: "v1A.0.6",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R44 peer-review round (R44 MAJOR M3 four-route no-go appendix shipped Wave 14-IIII; cross-paper companion bibitems Golden2026P{1b,2,3,4} + Eskilt2022b joint Planck+ACT defined Wave 14-JJJJ — all natbib cite warnings cleared) + arXiv submission",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "ΛCDM+ΔNeff MCMC + NaMaster + ALP companion",
      version: "v1B.0.2",
      readiness: 99,
      pendingWork:
        "DESI DR2 w0wa cobaya chain to converge (R̂−1 = 0.076 at 18:27 PT, ~1-3 days) → GetDist → §Structural Tension update → recompile, then Houston sign-off + arXiv. Wave 14-JJJJ refreshed bibitems + version stamp; cross-paper Golden2026P{1a,2,3,4} + Eskilt2022b joint Planck+ACT now defined as proper @article entries.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = -35/8 SPHEREx forecast",
      version: "v1.7.13",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R44 round (R44 BLOCKERs B1+B2 shipped Wave 14-HHHH: 9.9σ n_fNL site reframed as joint-Fisher pre-systematic-budget upper bound; convention-reversal halving stated for both 5.25σ→2.6σ optimistic AND 3-5σ→1.5-2.5σ post-systematic in abstract; conclusion-section 1.5-2.5σ unchanged) + arXiv submission",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378K-anomaly multi-survey catalog",
      version: "v3.1.25",
      readiness: 99,
      pendingWork:
        "HuggingFace dataset visibility flip (Houston manual) + sign-off + clean external R45 round (R44 MAJORs M1+M2+M4+nit1 shipped Wave 14-FFFF; R44-M5 high-confidence-restricted α re-measurement shipped Wave 14-KKKK: α_GS,jk = +1.83 ± 2.03 on 1,122 Gold+Silver subset, σ(f_NL)_GS = 2.28 ± 7.43, central 74% improvement consistent with no improvement at <1σ; full-sample α_jk = 0.19 ± 0.65 retained as load-bearing headline) + arXiv submission",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M galaxy chirality at scale",
      version: "v1.0.33",
      readiness: 99,
      pendingWork:
        "Houston sign-off + clean external R44 round (R44 MAJORs M1+M2+M3 + nit2 shipped Wave 14-GGGG: p_LEE harmonized to MC upper bound at three sites, GZ1 Platt parameters reported to 6 sig figs, GZ1 vs Cat-C gap reframed as paired McNemar Z=6.77 (was unpaired binomial 5.5σ), PUSHBACK token cleanup; M4-M7 incl. RA/Dec ablation queued) + arXiv submission",
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
