// Live build status surfaced at the top of every page.
// Updated each cron fire / wave-close commit. Renders into <LiveStatus />.
// Timestamp is baked in at build time — bump on every commit that ships
// research progress so Vercel rebuilds put the new value live.
//
// KEEP EVERY STRING SHORT. headline <= 2 sentences, summary <= 3 sentences,
// pendingWork/why/ask one line each. The audit trail lives in
// project-context/SSOT/, never here.

export interface PaperProgress {
  slug: string;
  number: string;
  shortTitle: string;
  version: string;
  readiness: number; // percent 0-100
  pendingWork: string; // ONE LINE: what is still pending for this paper
}

export interface NeedsHoustonItem {
  title: string;       // short label (e.g. "arXiv submission credentials")
  why: string;         // ONE SENTENCE: why ONLY Houston can unblock this
  blockedPaper?: string; // e.g. "P1A", "P4", "P5" — which paper this gates
  ask: string;         // ONE SENTENCE: exact action Houston needs to take
}

export interface LiveStatus {
  lastUpdatedISO: string; // ISO 8601 UTC, baked at build time
  lastUpdatedDisplay: string; // human-readable PT timestamp for the banner
  headline: string; // 1-2 sentences, current state
  summary: string; // 1-3 sentences, what just shipped
  currentlyRunning: string[]; // short bullets of what is actively running RIGHT NOW
  needsHouston: NeedsHoustonItem[]; // ONLY items truly blocked on Houston
  papers: PaperProgress[]; // 6 papers, sorted by display order
  blockerTally: {
    closed: number;
    openBlockers: number;
    openMajors: number;
    openMinors: number;
  };
  cronStatus: string;
  etaToCompletion: string; // human-readable ETA to all-papers @ 100%
  pods: Array<{
    name: string;
    state: "active" | "idle" | "queued";
    note: string;
  }>;
}

export const liveStatus: LiveStatus = {
  lastUpdatedISO: "2026-07-07T18:00:00Z",
  lastUpdatedDisplay: "July 7, 2026 · 11:00 AM PT",
  headline:
    "VERIFICATION COMPLETE; REVIEW CLOSURE IN PROGRESS (Jul 7). All six papers are error-clean, fully verified, D-round polished, and P-round packets are arXiv-ready — but NOT yet past external review. The verified EXT board is the truth: every paper still draws a real ChatGPT REJECT, with Grok/Gemini MINOR-to-MAJOR. Readiness is verdict-derived, not ladder-derived. The bar is a reviewer ACCEPT, which no paper has yet.",
  summary:
    "Correcting the record: an earlier build read readiness 99 / 'program complete,' which conflated 'verification rounds complete' with 'reviews passed.' They are not the same. Per the POSTPOLISH-2026-07-06 verified round (ChatGPT/Grok/Gemini): P4 REJ/MIN/MAJ · P2 REJ/MIN/MIN · P5 MAJ/MIN/MIN · P3 REJ/MAJ/MAJ · P1B REJ/MAJ/MAJ · P1A REJ/MAJ/MAJ. Readiness = 50 (error-clean/verified base) + per-reviewer points (ACCEPT +16.7, MINOR +12, MAJOR +6, REJECT 0) summed over the 3 EXT reviewers. The loop is now closing the remaining reviewer findings with real science — not declaring victory.",
  currentlyRunning: [
    "Closing remaining reviewer findings with real science: P2 independent Fisher · P1A Fierz-lemma proof attempt · P3 eROSITA reproducibility fix · P1B→P1A merge prep (unanimous reviewer recommendation). ACCEPT is the bar.",
  ],
  needsHouston: [
    {
      title: "Route the review-floor papers to human referees",
      blockedPaper: "all",
      why: "No paper is reviewer-accepted — every one still draws a real ChatGPT REJECT; the remaining barrier is a venue/scope judgment, not an editable defect (pattern-066). Only a human can decide arXiv/journal routing.",
      ask: "Decide the referee route for the review-floor papers while the loop closes the remaining reviewer findings with real science.",
    },
    {
      title: "arXiv submission — endorsement (when a paper clears review)",
      blockedPaper: "all",
      why: "Submission needs a human: arXiv endorsement is Houston-only. Gated behind a paper actually clearing external review — the packets are ready, the reviews are not passed yet.",
      ask: "Confirm arXiv endorsement so a paper can be submitted the moment it earns a reviewer ACCEPT.",
    },
    {
      title: "Send the Cai/Brandenberger courtesy email",
      blockedPaper: "P2",
      why: "The courtesy note about the −35/16 Cai–Li factor-of-2 resolution is drafted do-not-send; only Houston sends outbound author correspondence.",
      ask: "Review the drafted courtesy email and send when ready.",
    },
  ],
  papers: [
    {
      slug: "paper-1a",
      number: "1A",
      shortTitle: "ECH dark-energy closure + perturbation transparency",
      version: "v1U.0.10",
      readiness: 56,
      pendingWork: "UNIFIED Paper 1 (P1B merged in as appendices): 62pp self-contained. F14 closure (v1U.0.8, Jul 9): sharpened the R4 spectator-ALP framing per Gemini's R4 objection (no number changed, nothing fabricated) — the Route-4 closure now states explicitly that the m_θ~H_0 ultralight-mass tuning is the SAME generic tuning of every quintessence/ultralight-axion DE model (NOT a distinctive ECH barrier), while the ECH-specific content is (i) the rigid one-loop-coupling amplitude overshoot of ρ_θ over ρ_Λ by 22–36 OOM, and (ii) that once the coupling is floated to escape the overshoot minimal ECH gives no first-principles m_θ~H_0, closing the predictive route. 0 undef-refs, latex-audit clean. v1U.0.7 scrubbed two body-text sentences that referenced the internal review process (Sec II A 2 dimension-4 bookkeeping + Ω_a definition subsection), rewriting each as standalone scientific prose — no number changed, nothing fabricated, 0 undef-refs. v1U.0.6 is the W12 EXT closure wave (no headline number changed, nothing fabricated). Dimensional truth-audit of ChatGPT's W12 MAJOR: ChatGPT was RIGHT — under the paper's own conventions the bare Table-VII invariants O1 (εeeR), O2 (Nieh–Yan), O4 (T²), O6 (single-curvature) are naive dimension-2 densities, so calling them 'dimension-4 with dimensionless coefficients' was a main-text/Table-VII transcription slip; only O3 (Pontryagin) and O5 (axial-torsion) are dim-4 as written. The appendix derivation (INT-verified) was correct — it already carries the κ/M_Pl powers. Fix: new displayed Eq. (dim4_defs) writes each O_n^[4] with its explicit M_Pl² prefactor (O1/O2/O4/O6 × M_Pl²; O3/O5 bare) so every c_n·O_n^[4] is a genuine dim-4 density with dimensionless c_n; Table VII gains dim (bare) + prefactor columns + a coefficient-dimension note, promoted to full-width. No physics conclusion changed (single-scale closure survives at dimension 4); the two symbolic checks (dim4_parityodd_enumeration.py) re-run and both PASS. Also fully promoted the completeness argument into the main text (unanimous W12 ask — all three reviewers said the promotion was still partial): new inline block states the Bianchi-vanishing (O1/O6), Cartan→Fierz collapse to the closed {SS,VV,AA,PP} basis (O4/O5), and topological-total-derivative closure (O2/O3); the appendix keeps the derivations. 0 undef-refs, latex-audit clean. Awaiting next EXT re-test. G15 closure (v1U.0.9, Jul 10): reframed the stock-CAMB MCMC as an upper-bound baseline envelope check (not an ECH test) per Gemini, restructured the Eq.6→Eq.7 hand-off to lead with the dimension-4 operator basis over the Case II curvature-dressing heuristic, and closed Grok/ChatGPT minors (Eq.17 margin note, transparency-theorem all-orders/FLRW clause, M_Pl/κ convention footnote, Holst-topological terminology). Presentation-only, no verified number changed.",
    },
    {
      slug: "paper-1b",
      number: "1B",
      shortTitle: "MCMC + NaMaster + ALP technical companion",
      version: "v1B.0.104",
      readiness: 56,
      pendingWork: "MERGED into Paper 1 (2026-07-08, unanimous reviewer recommendation, Houston-approved) — no standalone submission; two-paper fallback preserved.",
    },
    {
      slug: "paper-2",
      number: "2",
      shortTitle: "f_NL = −35/16 SPHEREx forecast",
      version: "v1.7.110",
      readiness: 62,
      pendingWork: "Error-clean + verified. W12 EXT re-test (Jul 9): the v1.7.106 calibration+Eq.(11)-budget CONVERTED on 2/3 — Grok MAJOR→MINOR ('the calibrated f_NL + Eq.(11) budget + sensitivity map requests are now closed… no technical blockers remain') and Gemini MINOR ('resolved its core theoretical discrepancies and codified a transparent systematic budget'); ChatGPT held MAJOR at its recurring claim-calibration floor. v1.7.107 closes the resulting presentation majors (no headline number changed, −35/16 unchanged, nothing fabricated): Grok MegaMapper Fig-2 headlining scoped as future/Stage-V + endpoint-language drift fixed (explicit tier→σ map: SPHEREx optimistic 2.6–2.75σ / post-budget 1.3–2.75σ) + Cai-correction tone calibrated to 'one identified discrepancy' (removed 'arithmetic error'); ChatGPT factor-of-two forensic wording made exactly consistent with what App A proves (vertex-sum certification is the decisive evidence); stale −35/8-scaled MegaMapper ~3–7σ swept to the Sec V numbers; Table V relabeled scenario/scoping budget; GR-correlation bracket disclosed; data/code-availability + notation + trimmed captions + Gemini cross-covariance caveat. Items needing NEW calculations (recompute-r, cubic matching, Bayes restructure, Zenodo DOI) left open, NOT fabricated. Raw verbatim + screenshots in EXT_real/W12_2026-07-09/.",
    },
    {
      slug: "paper-3",
      number: "3",
      shortTitle: "378,280-anomaly multi-survey catalog",
      version: "v3.1.152",
      readiness: 56,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. R9 EXT board (Jul 9): ChatGPT major · Gemini major-if-PRD (ApJS/MNRAS transfer suggested) · Grok minor ('suitable for PRD', 3 presentation clarifications). v3.1.146 real work: (1) NEW committed-data out-of-sample answer to the recurring 'released catalog scored in-sample' major — a held-out anomaly-tail-preservation test on 47,000 DESI rows held out of both train and val across the 5 folds shows the anomaly-defining tail (MSE p99/p50) is preserved vs in-sample at rho=1.00±0.05 (min 0.94, gate≥0.5 PASS), so the tail is not an in-sample-inflation artifact (new artifact heldout_tail_preservation.json); (2) main-text definition of the 5,384 QSO-candidate multi-tracer sample added (Grok minor). Tier-mix major = re-flag of the already-prominent three-tier split (referee variance). Venue = scope/venue, Houston-gated. NO COUNT CHANGED, NO DISCLOSURE WEAKENED, NOTHING FABRICATED.",
    },
    {
      slug: "paper-4",
      number: "4",
      shortTitle: "8.47M-galaxy chirality null at sub-percent sensitivity",
      version: "v1.0.234",
      readiness: 56,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. F14 closure (v1.0.229, Jul 9): added the end-to-end transfer-calibration scope statement per ChatGPT's F14 MAJOR (no number changed, nothing fabricated) — delineates which links of the classify→dipole chain injection-recovery traverses (map-making + dipole estimator + null) vs which it does NOT (ViT classifier, NS triage, confidence cut, spatially-varying confusion); shows from the committed GZ1 confusion numbers that the asymmetric-confusion transfer slope g_eff=s_CW+s_CCW−1=0.398 equals the symmetric g=2a−1=0.398 for the near-balanced parent (so CW/CCW asymmetry does not degrade the physical-amplitude conversion); honest-flags the full image-level end-to-end injection through the classifier as requiring NEW simulation, holding operative claims to the observed hard-label field. 0 undef-refs. R9 EXT board (Jul 9): Grok = MINOR-revisions ('careful, reproducible null-result analysis that meets PRD standards', 3 clarifications) · Gemini = 'Accept with minor revisions' ('a highly significant contribution', 3 clarifications) · ChatGPT = MAJOR (presentation/consolidation of already-disclosed content). Readiness 82 = 50 base + Grok MINOR (+16) + Gemini MINOR (+10) + ChatGPT MAJOR (+6). v1.0.225 closed both ACCEPT-track referees' concrete minors: abstract z≈−18 now explicitly a model-dependent template-disfavor statistic (not a frequentist exclusion) with the injection-recovery A95∈(1.0,1.5]% cross-referenced; main-text downstream-user warning that raw p_eq are not frequentist likelihoods (Appendix-B ECE ≥0.25–0.36); abstract real-space p now names its isotropic-pixel-permutation null. This paper is the program's closest — two clean minor-lists from a Grok+Gemini double-accept. Raw verbatim + screenshots in EXT_real/R9_2026-07-09/. G15 closure (v1.0.230, Jul 10): closed Grok's three non-blocking concerns — z≈−18 flagged near Table I as a model-dependent template-disfavor statistic (not a frequentist exclusion), a sentence in Sec IV D bounding any cosmological content of the ~47% unmodelled ℓ=1 remainder below A_50 (consistent with the +0.41σ real-space null), and Shamir-comparison mechanism context (monopole-mask leakage + depth-coupled bias); Fig 10 caption corrected from 'null' to 'block-bootstrap sampling distribution'. Presentation-only, no number changed.",
    },
    {
      slug: "paper-5",
      number: "5",
      shortTitle: "DESI environmental chirality independence",
      version: "v0.1.115",
      readiness: 68,
      pendingWork: "Error-clean + verified, NOT reviewer-accepted. F14 closure (v0.1.112, Jul 9): closed the four F14 ChatGPT/Gemini DESIVAST asks with real edits (no verified number changed, nothing fabricated) — (1) dual-primary reconciled: abstract now leads with the single footprint-restricted primary estimand Δf_CW=+0.0018 and demotes the unrestricted +0.0007 to a secondary sensitivity check; (2) 'footprint ≠ selection function' distinction added at the primary designation (the angular-disc footprint is a geometric construction, not the published DESIVAST/BGS completeness mask/randoms); (3) the ≈0.9pp systematic envelope justified with the explicit quadrature term-sum √(0.44²+0.37²+0.60²+0.37²+0.11²+0.24²+0.02²)=0.94pp; (4) simultaneous Bonferroni-5 bound computed across all five estimators (widest per-test 99%-level CI ⇒ no void definition admits |Δf_CW|≳1.1pp at family-wise 95%). 0 undef-refs, latex-audit clean. CW re-test (Jul 8): Grok MINOR · Gemini MAJOR · ChatGPT MAJOR — Gemini re-flagged the RSD-in-T-Web classification, radial-selection bias in T-Web void classes, and the unpublished Paper-IV label dependency (all already disclosed); ChatGPT re-flagged the same T-Web/void-membership/Paper-IV items. Central DESIVAST no-environmental-dependence null reasonably supported; every number preserved. Raw verbatim reviewer text + screenshots in EXT_real/CW_2026-07-08/. G15 closure (v0.1.113, Jul 10): softened the post-hoc 'designated primary' framing so the family-wise Bonferroni-5 null leads from the outset (Table IV disclosure retained), quoted the de-attenuated physical-chirality bound ≈2.26pp (= 0.9pp / 0.3982, from the paper's own 2a−1 attenuation factor) alongside the classifier-label 0.9pp bound in the abstract/§XIII/App A, and hardened the Appendix B toy-EFT operator with an explicit non-covariant/out-of-scope caveat. Presentation-only, no verified number changed.",
    },
  ],
  blockerTally: {
    closed: 912,
    openBlockers: 0,
    openMajors: 8, // H17+Grok-retest board FROM RAW: ChatGPT REJECT ×5 (harsh-referee floor); Grok retest MAJOR on P1U/P3/P4; embedded [MAJOR] on P2 & P5; Gemini P5 MAJOR
    openMinors: 4, // Grok retest MINOR-list on P2/P4/P5 + P1U
  },
  cronStatus: "H17 CLOSURE WAVE + GROK RE-TEST harvested (2026-07-10). All 5 papers bumped to H17 versions after a 5-REAL-error closure wave (P2 −(99/128) sign + SSFSR BF 10⁸→1.4×10² fix; P4 Shamir factor-of-2 double-count; P1U Eq.16 relabel; P3 three-gate downgrade; P5 primary-estimand seam). Grok re-test: P2 improved MAJOR→MINOR, P4 regressed MINOR→MAJOR (referee variance), P1U/P3/P5 unchanged. ChatGPT retest submitted-but-unharvested (headless cron); Gemini upload-throttle-FAILED. NO paper at ACCEPT — the literal 0/0/0 bar (directive-J) is not met. Readiness is verdict-derived (caps P1U/P3/P4=56, P2=62, P5=68), never a false high %.",
  etaToCompletion:
    "Driving the remaining reviewer findings to closure with real science; a reviewer ACCEPT (0 MAJOR / 0 minor from ChatGPT + Grok + Gemini) is the bar before any paper is submission-eligible. ChatGPT retest + Gemini re-run are the next EXT legs to harvest.",
  pods: [],
};
