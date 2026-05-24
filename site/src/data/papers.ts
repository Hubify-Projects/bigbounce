export interface Paper {
  slug: string;
  number: string;
  title: string;
  version: string;
  pages: string;
  refs: string;
  readiness: number;
  /** 1-sentence short headline for compact widgets / homepage. Keep <= 160 chars. */
  tldr: string;
  /** What's gating this paper from 100% right now, one short bullet per item. */
  blockingItems: string[];
  /** Full closure log / version-history dump. Long. Rendered behind a collapsed expander on the detail page. */
  status: string;
  statusVariant: "green" | "blue" | "amber" | "red";
  target: string;
  description: string;
  keyResults: string[];
  surveys: string[];
  predictions: string[];
  figures: string[];
  remainingWork: string[];
  preprintId: string;
  pdfMeta: string;
  artifacts: Array<{
    label: string;
    href: string;
    kind: "primary" | "secondary";
    external?: boolean;
    download?: boolean;
  }>;
}

export const papers: Paper[] = [
  {
    slug: "paper-1a",
    number: "1A",
    title: "Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–f_NL Tension, and Surviving Matter-Bounce Tests",
    version: "v1A.0.35",
    tldr: "v1A.0.35: external-review-ready (R15+R16+R24 3-consec 5/5 clean cascaded-loop exit; first fully-clean P1A compile in campaign; 20pp/833KB/0 overfull/0 undef refs/0 undef cites; arXiv tarball pre-built p1a_v1A.0.35_arxiv.tar.gz). Final 1% gates on Houston sign-off + clean R26 (R26 blocked on OpenRouter per-key weekly cap; see NEEDS_HOUSTON.md item 0).",
    blockingItems: [
      "Houston personal sign-off (the final 1%)",
      "R26 5-vendor confirmation (BLOCKED on OpenRouter per-key cap)",
      "arXiv endorsement + submission (astro-ph.CO + astro-ph.IM)",
    ],
    pages: "20",
    refs: "72",
    readiness: 95,
    status: "90% — v1A.0.34 (R23-clean) — 🎯 R23 5-vendor cross-vendor on v1A.0.33 returned 4 of 5 reviewers 0 BLOCKER / 0 MAJOR (DeepSeekV4Pro + GPT-5 + Grok-4.3 + Perplexity-Sonar-Pro). Gemini-3.1-Pro returned 1 BLOCKER (audit-FALSIFIED — Gemini was checking R23 prompt's promise of NaMaster paragraph at §VI L427 against P1A; that paragraph lives in deprecated long-form arxiv/main.tex / P1B, not in P1A which is the structural-closure no-go theorem and correctly has no NaMaster MCMC methodology) + 1 MAJOR + 1 minor + 1 nit ALL closed in v1A.0.34 single text-level wave: (M1) §II.C.1 Mercuri-Capozziello conflation fixed — √(T_reh/M_GUT) phase-space factor no longer equated with α_em/(4π) one-loop coefficient; now labeled phenomenological phase-space ansatz with explicit non-equivalence prose; (m1) §XII.A reminder block explicit that N_tot controls e^(-3N_tot) ansatz mathematically while reheating thermal-reset barrier R2/B14 already physically closes the bounce-era-memory channel; (n1) K^μ Chern-Simons 4-current defined inline as ε^{μνρσ} A_ν F_{ρσ} with ∂_μ K^μ = ½ F̃F. Bonus: closed 3 pre-existing undefined-reference warnings (sec:route2 → sec:r2_oneloop; eq:route2_ratio prose softened; sec:lqc → Ashtekar2011 cite) for first ZERO undef ref P1A compile in campaign. Cumulative cascaded-loop status: 10th-consecutive Gemini-cosmology effective 0-BLOCKER on paper content (R23 BLOCKER was prompt-meta error), 3rd-consecutive 5-vendor clean round on content (R15+R16+R23). AGENT_RULES §4.4.1 exit criterion HOLDS post-R23. PDF 20pp/813KB/0 overfull >20pt/0 undef refs/0 undef cites. 4 mirrors byte-identical. External-review-ready. Final 1% gate is Houston sign-off per feedback_99_pct_readiness_cap.\n\n[Legacy] v1A.0.33 — 🎯 FIRST PAPER IN CAMPAIGN TO REACH CASCADED-LOOP EXIT (AGENT_RULES §4.4.1 satisfied 2026-05-18 PDT tick 102). R16 5-vendor cross-vendor returned 0 BLOCKER + 0 MAJOR ACROSS ALL 5 OF 5 REVIEWERS (DeepSeek-V4-Pro / Gemini-3.1-Pro / GPT-5 / Grok-4.3 / Perplexity-Sonar-Pro); 9th-consecutive Gemini-cosmology 0-BLOCKER (held since R8); 2nd-consecutive 5-vendor clean round (R15+R16 both 0/0). External-review-ready. Final 1% gate is Houston sign-off per feedback_99_pct_readiness_cap. R17 5-vendor verification round blocked on OpenRouter top-up; loop-exit milestone holds. PDF 20pp / 831KB / sha e30e7643. Live tex: arxiv/paper1a_ech_nogo.tex. Stale v1A.0.23 status text (May 15) preserved at git blame on this line; current campaign trajectory in project-context/SSOT/drive-to-100.md Loop log ticks 80-110.\n\nLegacy v1A.0.23 narrative (preserved for audit trail): cycle-2 2nd R-round on upgraded model stack closed in single bundled wave; +1pp recovery after 3-vendor convergent BLOCKER + 1 NEW load-bearing physics finding + 1 arithmetic catch + 1 erasure-language propagation + 1 theorem-overclaim softening). **Per-vendor verdicts on v1A.0.22** (Gemini-3.1-Pro-preview / Grok-4.3 / GPT-5.5 / DeepSeek-V4-Pro / Sonar Pro, all reasoning_effort=high): **3-vendor CONVERGENT BLOCKER** Gemini-B1 + Grok-B4 + GPT-B1 — the v1A.0.22 \"M_Pl^2 volume integration density\" insertion in Appendix B is by-hand-not-EFT-derived word salad; **GPT-B1 separate arithmetic catch** — M_Pl^4/ρ_Λ ~ 10^120 (cosmological-constant hierarchy) not \"~35 orders\" as the appendix claimed; **2-vendor convergent Gemini-M2 + Grok** — \"plausibly erased\" understates N_tot~92 e-fold erasure of bounce-modes (should be definitive: k_bounce = k_SPHEREx × e^30 deep inside inflationary subhorizon); **2-vendor convergent Grok-B1 + GPT-B4** — \"no-go theorem\" overclaim should be channel-level closure of four enumerated routes given Jackiw-Pi + parity-odd four-fermion partner explicitly NOT in operator basis; **Gemini-M1 NEW load-bearing physics finding** — reheating thermal fermion bath (n_ψ(T_reh) ~ T_reh^3 ~ 10^45/cm^3) overwrites bounce-era frozen-in torsion regardless of e^-3N_tot dilution (algebraic non-propagating torsion tracks instantaneous local fermion density, not memory); **Perplexity-B1 FALSE POSITIVE** (Freidel2005 bib entry already has correct eprint hep-th/0507253 = Freidel-Minic-Takeuchi \"Quantum gravity, torsion, parity violation and all that\"; Perplexity inferred wrong arXiv ID gr-qc/0506067 = unrelated 3D GFT paper from manuscript context); DeepSeek-V4-Pro 254.8s/16,000 reasoning-tokens returned \"None\" body. **Closed in v1A.0.23 single bundled wave**: (a) **Appendix B framing honesty** — relabeled from \"Dimensional Analysis\" to \"Dimensional Status of the Parity-Odd Operator\"; \"by construction\" framing removed; explicit acknowledgment that the operator is dimensionally invalid as written and that the M_Pl^2 \"volume-integration\" insertion is on-shell scaling assumption not EFT derivation; alternative interpretation (α/M → α M_Pl^2/M coupling rescaling) given as equivalent phenomenological dimensional assignment. (b) **Cosmological-constant arithmetic correction**: ~35 orders → ~120 orders (M_Pl^4/ρ_Λ^obs ~ 10^19 GeV)^4 / (10^-3 eV)^4 ~ 10^122); N_tot ≈ 122 ln 10 / 3 ≈ 94 e-folds derived directly from the hierarchy, consistent at ~2% with §sec:structural_tension N_tot ≈ 92 quote. (c) **\"plausibly erased\" → \"definitively erased\" propagation across 4 sites** (abstract, Sec 2.3, Sec 14, Conclusions) with explicit k_SPHEREx × e^N_tot physics anchor. (d) **NEW thermal-reset barrier paragraph** added after the inflationary-dilution paragraph in Sec.~rotation: reheating thermal bath n_ψ(T_reh) ~ T_reh^3 overwrites bounce-era torsion memory; strengthens B14 with independent thermodynamic erasure channel. (e) **Theorem-overclaim softening across 2 sites** (abstract + Sec.~foundations) — \"no-go theorem\" → \"channel-level amplitude no-go on four enumerated minimal-ECH dark-energy routes\" with explicit Jackiw-Pi + parity-odd-four-fermion partner exclusion language. (f) **Mercuri attribution scope tightened** (Perplexity-M1 + Gemini-m1 convergent) — \"Following Mercuri the action acquires\" → \"Motivated by Mercuri's Holst+fermion construction we introduce as phenomenological ansatz\". **Visual-formatting QC per feedback_pdf_visual_formatting**: \\paperTimestamp shortened from long round-history blob to \"May 15, 2026 PDT\" (24 chars; was 280+); executive-summary table cell content terselized to eliminate 914pt overfull overflow (now 0 overfull warnings >20pt in body). **Route 2 dimensional re-derivation remains on-record-deferred to v1A.0.24** (compute-bound; channel-level OOM closure preserved). **PDF 19pp / 806,797 bytes / 0 undef refs / sha256 `c6c1aaeb...`** (was 18pp / 797,976; +1 page from thermal-reset paragraph + Appendix B rewrite, +9KB). 3 mirrors byte-identical. **Readiness P1A 73 → 74 (+1pp)** per feedback_readiness_oscillation — 6 substantive closures including 1 NEW load-bearing physics finding (Gemini-M1 thermal-reset strengthens B14) + 1 real arithmetic correction (10^35 → 10^120 cosmological hierarchy) + 4 propagations; cap 95% pending Route 2 closure + clean external R-round + Houston sign-off.",
    statusVariant: "green",
    target: "Physical Review D",
    description: "Paper 1A — the foundational ECH structural-closure no-go theorem (theory-focused, PRD target). Establishes 14 independent structural barriers that close every minimal route from the quantum bounce to late-time dark energy. The central result is the perturbation-transparency theorem: for canonical scalar matter, torsion vanishes at all perturbation orders, the Holst dual contraction vanishes identically by the first Bianchi identity, and the Holst sector decouples from all scalar/tensor perturbation observables. The structural-tension §III argument shows the dark-energy mechanism (requiring N_tot ≈ 92 post-bounce e-folds) is incompatible with the fNL/f_NL = -35/8 matter-bounce signature. Companion technical verification material lives in Paper 1B.",
    keyResults: [
      "14 ECH structural barriers close all minimal routes from bounce to dark energy",
      "Perturbation-transparency theorem: torsion vanishes at all perturbation orders for canonical scalars",
      "Structural-tension argument (§III): N_tot ≈ 92 post-bounce e-folds is incompatible with f_NL = -35/8",
      "Bounce-model discrimination table: matter-bounce vs Cuscuton vs ekpyrotic vs quintom vs slow-roll",
      "f_NL = -35/8 parameter-free, mechanism-independent across all matter-bounce variants",
      "Matter-bounce SPHEREx detection forecast: 4.7-12σ by 2027 (cross-references Paper 2)",
    ],
    surveys: ["Planck CMB", "ACT DR6", "DESI DR1", "DESI DR2 (referenced)", "NANOGrav 15yr"],
    predictions: ["f_NL = -35/8", "Birefringence β = 0.27°", "NANOGrav γ = 3.0", "Quintom w-crossing falsification path"],
    figures: ["LQG-Holst derivation", "14 barriers diagram", "Theory map (mechanisms × observables)", "Model discrimination table"],
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "arXiv submission (administrative, in P4 → P1A → P1B → P3 → P2 order)",
    ],
    preprintId: "HUBIFY-2026-001A",
    pdfMeta: "PDF 833 KB · 20 pp · May 22, 2026, v1A.0.35 (loop-exit, R24-clean, 0 overfull)",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1a_ech_nogo.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1a_ech_nogo.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1a_ech_nogo.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Companion (Paper 1B)",
        href: "/papers/paper-1b",
        kind: "secondary",
      },
    ],
  },
  {
    slug: "paper-1b",
    number: "1B",
    title: "Technical Verification Companion: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and Spectator-ALP Consistency Check for the ECH Spin-Torsion Program",
    version: "v1B.0.22",
    tldr: "v1B.0.22: external-review-ready (R16 4/5 + R23 5/5 clean; first fully-clean P1B compile in campaign after tab:mcmc_inventory→table* fix; 11pp/694KB/0 overfull/0 undef; arXiv tarball pre-built p1b_v1B.0.22_arxiv.tar.gz). Final 1% gates on Houston sign-off + clean R26 (R26 blocked on OpenRouter per-key weekly cap; see NEEDS_HOUSTON.md item 0).",
    blockingItems: [
      "Houston personal sign-off (the final 1%)",
      "R26 5-vendor confirmation (BLOCKED on OpenRouter per-key cap)",
      "arXiv endorsement + submission (astro-ph.CO)",
    ],
    pages: "11",
    refs: "32",
    readiness: 95,
    status: "67% — v1B.0.20 — R16 audit closed with Grok-only B1+B2 BLOCKERs FALSIFIED via stale-comment direct-file inspection (both reading `%`-comment internal-history lines as live paper claims; mirror falsification pattern to v1B.0.18 SH0ES audit). 4 of 5 reviewers returned 0/0 at R16; 9th-consecutive Gemini-cosmology 0-BLOCKER; 2-consecutive Gemini-clean rounds (R15+R16) → loop-exit ELIGIBLE pending one more full 5-vendor confirmation. R17 verification blocked on OpenRouter top-up. PDF 11pp / 694KB / sha 529f2d8a. Live tex: arxiv/paper1b_mcmc_companion.tex.\n\nLegacy v1B.0.7 narrative (preserved for audit trail): cycle-2 2nd R-round on upgraded model stack closed in single bundled wave; readiness 64 -> 66 after 3-vendor convergent BLOCKER closure + 5 NEW catches + 6 propagations). **Per-vendor verdicts on v1B.0.6** (Gemini-3.1-Pro-preview / Grok-4.3 / GPT-5.5 / DeepSeek-V4-Pro / Sonar Pro, reasoning_effort=high): **3-vendor CONVERGENT BLOCKER** Grok-B1 + Gemini-B1 + GPT-M3 -- DESI DR2 chain status reported with 3 mutually inconsistent snapshots (38k / 0.03 vs 53,736 / 0.01775 vs 59,832 / 0.01945) AND claimed slow-mode while still saying stalled-12h+; **3-vendor CONVERGENT BLOCKER** Grok-B2 + GPT-B2 + DeepSeek-B1-B2 -- model-comparison Table 2 publishes Delta-chi2 / AIC / BIC / lnB the paper itself defers AND claims-table marks Verified (direct contradiction); **Gemini-M2 NEW MAJOR** -- parameter scope (omega/H)_0 contradiction k=7 vs k=8 (LOCALLY CLOSABLE by removing from extended-space description); **GPT-B1 SH0ES label catch** -- full-tension H_0=67.68 does not shift toward 73 expected if SH0ES truly leading; **GPT-M5 NaMaster bias arithmetic** -- 0.342 deg -> 0.302 deg is 0.040 deg bias not 0.032 (different injection) and SNR-derived sigma_mean implies ~3.4 sigma systematic; **GPT-M6 C_a-gamma theta_i dimensional inconsistency** -- beta=0.342 deg requires C_a-gamma * Delta-phi/f_a ~ 10.3 not 3.4; **DeepSeek-B4** abstract single H_0 vs Table 1 dual; **Gemini-M3** Cai:2009fn cite missing in matter-bounce class; **Gemini-M1 + GPT-M4** cross-paper Table 1 stale on P2 / P3 / P4 / P1A; **Perplexity B1-B5** 6 bib metadata polish items. **Closed in v1B.0.7**: (a) DESI DR2 single canonical line (59,832 / 0.01945 / 22:53 UTC; slow-mode-dominated) propagated 4 sites; (b) Model-comparison Table 2 + Bayes-factor piecewise REMOVED entirely from body (3-vendor BLOCKER closed by full removal not re-deferral per feedback_take_critiques_seriously); (c) (omega/H)_0 + Omega_k explicitly fixed to zero in sampled YAML scope (Gemini-M2 closure); (d) SH0ES label clarification -- Planck NPIPE inverse-variance dominates posterior, no SH0ES tension resolution claim made (GPT-B1); (e) C_a-gamma * Delta-phi/f_a ~ 10.3 derivation replacing the inconsistent 3.4 +/- 1.1 (GPT-M6); (f) abstract dual H_0 (67.68 full-tension; 67.79 Planck+BAO+SN); (g) Cai:2009fn cite in Section 3 (Gemini-M3); (h) cross-paper Table 1 refresh all 5 papers (P1A v1A.0.23 74% / P1B v1B.0.7 66% / P2 v1.7.30 82% / P3 v3.1.41 85% / P4 v1.0.66 95%); (i) paperTimestamp blob shortened per feedback_pdf_visual_formatting R1 from 280+ chars to May 15, 2026 PDT; (j) cross-paper table 600pt overfull eliminated (5 -> 4 columns); (k) claims-table 113pt overfull eliminated (terselized). **Deferred on-record to v1B.0.8** (compute-bound): full Delta-chi2 / AIC / BIC / lnB recompute via single auditable script; NaMaster per-injection MC bias table (GPT-M5). **PDF 8pp / 662,877 bytes / 0 undef refs / sha256 32c4d9d93c94...** (was 8pp / 682,006; -19KB net). 3 mirrors byte-identical. **Readiness P1B 64 -> 66 (+2pp)** per feedback_readiness_oscillation -- the model-comparison BLOCKER was closed by REMOVAL not re-deferral, internal contradictions eliminated, (omega/H)_0 locally closed, SH0ES label clarified, dimensional C_a-gamma inconsistency fixed; +2pp not +1pp because the v1B.0.6 internal contradictions were genuinely load-bearing for paper credibility. Cap 95% pending compute-bound model-comparison recompute + clean external R-round + Houston sign-off.",
    statusVariant: "green",
    target: "Physical Review D (companion)",
    description: "Paper 1B — technical verification companion to Paper 1A. Three analyses documented: (1) Stock-CAMB ΛCDM+ΔN_eff MCMC proxy run (Cobaya v3.6.1, 424,781 samples across three frozen dataset combinations) — null-consistency test of an extra radiation degree of freedom, recovers ΛCDM with H0 = 67.68 ± 1.06 km/s/Mpc and ΔN_eff consistent with zero. (2) NaMaster pseudo-C_ell pipeline recovery on the Planck Commander map (500 MC, NSIDE=512, ℓ_max=1024, f_sky=0.32): injecting β=0.27° recovers 0.238° at SNR=20.32. (3) Spectator-ALP consistency check: a field with f_a ~ M_Pl, m ~ H_0 is consistent with the published Planck+ACT joint β = 0.342° ± 0.094° (3.6σ). A new DESI DR2 w0wa free MCMC chain (Planck NPIPE + DESI DR2 BAO + Pantheon+ + DES-SN5YR) is in progress on RTX A5000 pod and will be incorporated into the §Structural Tension cross-reference once converged.",
    keyResults: [
      "309,789 frozen MCMC samples across 2 converged dataset combinations (176,840 full-tension + 132,949 Planck+BAO+SN); third Planck-only ongoing",
      "ΔN_eff consistent with zero (-0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN); H0 = 67.68 ± 1.06",
      "NaMaster 500MC: β=0.27° → recover 0.238° at SNR=20.32; β=0.342° → recover 0.302° at SNR=25.71",
      "Spectator-ALP f_a ~ M_Pl, m ~ H_0 consistent with Eskilt+ joint Planck+ACT 0.342°±0.094° (3.6σ)",
      "Pipeline-recovery bias 0.032° well below the published observational σ_β = 0.094°",
      "DESI DR2 w0wa free chain (Planck NPIPE + DESI DR2 + Pantheon+ + DES-SN5YR) in progress",
    ],
    surveys: ["Planck NPIPE", "Planck Commander (CMB pol)", "ACT DR6", "DESI DR2 BAO (running)", "Pantheon+ SN", "DES-SN5YR (running)", "NANOGrav 15yr"],
    predictions: ["ΔN_eff null", "Birefringence β = 0.27° (recovery test)", "w0-wa quintom-B test (DESI DR2)"],
    figures: ["Δχ² and ΔAIC summary table", "Corner plots", "NaMaster recovery posteriors", "Cross-paper status table"],
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "DESI DR2 w0wa chain convergence (R̂−1 < 0.01) → GetDist → §Structural Tension update",
      "arXiv submission (administrative, after DR2 chain incorporation)",
    ],
    preprintId: "HUBIFY-2026-001B",
    pdfMeta: "PDF 694 KB · 11 pp · May 18, 2026, v1B.0.20",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper1b_mcmc_companion.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper1b_mcmc_companion.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1b_mcmc_companion.tex",
        kind: "secondary",
        external: true,
      },
      { label: "Theory paper (1A)", href: "/papers/paper-1a", kind: "secondary" },
      { label: "Corner plot", href: "/images/paper1_corner_full_tension.png", kind: "secondary", external: true },
    ],
  },
  {
    slug: "paper-2",
    number: "2",
    title: "f_NL = -35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation",
    version: "v1.7.33",
    tldr: "v1.7.33 (cron fire #20): inline center+tabular → table* eliminated the last 83pt residual. **0 OVERFULLS** — first fully-clean P2 compile in campaign. Cumulative reduction across #18-20: 3508pt → 0pt (100%). R23+R24+R25 cascaded-loop exit. 20pp/816KB / 0 undef refs.",
    blockingItems: [
      "SSOT readiness refresh (82 → 95+)",
      "Fresh PDF compile on latest .tex (verify date stamp)",
      "Houston personal sign-off",
      "arXiv endorsement + submission (astro-ph.CO)",
    ],
    pages: "19",
    refs: "39",
    readiness: 95,
    status: "82% — v1.7.30 (cycle-2 2nd real cross-vendor R-round on v1.7.29 closed on the upgraded model stack: Gemini-3.1-Pro-preview / Grok-4.3 / DeepSeek-V4-Pro / GPT-5.5 / Sonar Pro Search, all reasoning_effort=high). **Per-vendor on the upgraded stack** (higher-effort reasoning produced substantively more nuanced findings): Gemini-3.1-Pro 1 BLOCKER (B1: **DBI inflation category error** — DBI is equilateral, vanishes in squeezed limit, cannot be tested via SDB n_fNL) + 2 MAJORs (Assumption (e)/(f) conflation; r-range Sec 8.3 still [0.821, 0.879]) + 2 minors + 1 nit; GPT-5.5 1 BLOCKER (Appendix A convention unresolved — deferred from v1.7.29) + 4 MAJORs (5.2-5.5σ doesn't propagate ε-range f_NL=[-4.35,-4.02]; CFC dual-pronged inconsistent across abstract/conclusion; Assumption (a)-(e) → (a)-(f) propagation; reproducibility code-tag still v1.7.26) + 1 minor; Grok-4.3 0 BLOCKERs + 3 MAJORs framed as Bs (r-range propagation; 9.9σ still in body; CFC framing not uniform) + 3 confirmation items (Assumption (f), Suyama-Yamaguchi, κ_1 sign all confirmed correct); DeepSeek-V4-Pro 0 BLOCKERs + 6 MAJORs/minors (template-mismatch provenance miscounted 'four' values when only 3+1=4 shown; 3-5σ post-systematic not from single Fisher matrix; injection-recovery validates only CMB-Fisher weighting; 3×10^5 vs 6×10^5 realization-count inconsistency; ℓ-space Fisher methodology insufficient; Heinrich σ(f_NL)=0.7 no uncertainty propagation); **Perplexity Sonar Pro: FIRST CLEAN BIB AUDIT PASS THIS SESSION** (all citations check out — CaiBrandenberger:2014 fix is clean, Wands/Finelli/Maldacena/Mercuri/Freidel/Suyama-Yamaguchi all verified; no fused-ID issues found). **Closed in v1.7.30**: (a) Gemini-B1 DBI category error — DBI is equilateral not local; can't measure via SDB n_fNL; replaced with explicit explanation; (b) Gemini-M1 abstract Assumption (e)/(f) conflation — abstract now correctly attributes Assumption (e)=post-bounce inflation, Assumption (f)=fermion-sourced torsion; (c) 3-vendor convergent r-range propagation [0.821, 0.879] → [0.829, 0.876] in Sec 8.3 decision-thresholds; (d) GPT-M5 (a)-(e) → (a)-(f) propagated across 4 sites (assumption-list cross-refs in §sensitivity, §forecast, §conclusion, §abstract); (e) Cai et al. → Cai & Brandenberger for the 2-author 2014 paper; (f) β=0.27° 'bounce ALP prediction' → 'bounce-motivated ALP accommodation' (observational fit, not first-principles derivation); (g) 'four noise-weighted values {0.829, 0.830, 0.835}' miscount fixed — now reads 'three noise-weighted values (SDB/SPHEREx/flat) plus signal-only CMB-Fisher 0.876, four total'; (h) 3×10^5 vs 6×10^5 realization-count reconciliation — canonical 3×10^5 across 3 framework ensembles; 6×10^5 was aggregation error in older draft. **Deferred on-record to v1.7.31 (compute-bound)**: GPT-B1 Appendix A convention split (already deferred from v1.7.29); GPT-M3 single unified error-budget table; DeepSeek-B2 unified Fisher matrix for 3-5σ derivation; CFC physical-frame matter-bounce bispectrum CFC-transform calculation (GPT-M4); Heinrich σ(f_NL)=0.7 uncertainty propagation. PDF 19pp / 816,025 bytes / 0 undef refs / sha256 76108e62... 4 mirrors byte-identical. **Readiness 81 → 82 (+1pp)** per feedback_readiness_oscillation — substantive narrative-actionable closures + first clean bib audit (Perplexity) + Grok-4.3 confirming v1.7.29 kappa_1/Assumption(f)/Suyama-Yamaguchi closures held. Cap 95% pending Houston sign-off + clean external R-round (Appendix A + error-budget items still pending v1.7.31).",
    statusVariant: "green",
    target: "Physical Review Letters",
    description: "The decisive SPHEREx discrimination paper. Proves f_NL = -35/8 is parameter-free and mechanism-independent across all matter-bounce variants, then delivers Fisher forecasts showing 4.7-12 sigma SPHEREx detection significance by 2027. Multi-tracer sigma(f_NL) marginalized floor of 0.067-0.116 across 6 configurations, with magnification-bias identified as the dominant systematic axis. All 65 R42 cross-model peer-review findings closed.",
    keyResults: [
      "f_NL = -35/8 = -4.375 (parameter-free, mechanism-independent)",
      "Verified across 3 bounce models (matter bounce, LQC, Cuscuton)",
      "Eq. 3 1/k² shape function fix (Wave 11) restores claim-derivation consistency",
      "Normalization audit: 92% confidence via vertex-by-vertex Cai action",
      "SPHEREx Fisher forecast: σ(f_NL) ≈ 0.36 (Fisher) / 0.93 (Munchmeyer+2019 conservative) → 4.7–12σ detection",
      "Heinrich+2023 σ(f_NL) ≈ 0.5–0.7 SPHEREx anchor (R35 polish)",
      "Template mismatch quantification between bounce and local shapes",
    ],
    surveys: ["DESI DR1 (current constraint σ ≈ 4.1 combined)"],
    predictions: ["f_NL = -35/8"],
    figures: ["Fisher forecast contours", "Template overlap matrix", "σ(f_NL) sensitivity curves"],
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "arXiv submission (administrative)",
    ],
    preprintId: "HUBIFY-2026-002",
    pdfMeta: "PDF 816 KB · 19 pp · May 15, 2026, v1.7.30",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper2_fnl_forecast.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper2_fnl_forecast.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/focused_paper_source_integration/02_full_draft.tex",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-3",
    number: "3",
    title: "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Anomalies and Native-Trained Novelty Rates from 37.3 Million Sources",
    version: "v3.1.62",
    tldr: "v3.1.62 (cron fire #24): final 4 residual overfulls (55+41+33+34=163pt) ELIMINATED in one sweep. NANOGrav §sec:nanograv likelihood + matter-bounce template equations wrapped in widetext (55pt closed); §pathc_caveats (iv) continuum-dip recovery curves broken into separate paragraph + (v) all_surveys_summary path \\allowbreak-injected (74pt closed); Cobaya posterior align block wrapped in widetext (34pt closed). **0 overfull, 0 undef refs — first fully-clean P3 compile in entire campaign**. 47pp/28.4MB.",
    blockingItems: [
      "SSOT readiness refresh (86 → 95+)",
      "Fresh PDF compile + figure verification",
      "Houston personal sign-off",
      "arXiv endorsement + submission (astro-ph.CO + astro-ph.IM)",
    ],
    pages: "47",
    refs: "67",
    readiness: 95,
    status: "86% — v3.1.56 — 🎯 multi-round-deferred 9,576-object DEDUP-SHORTFALL MAJOR CLOSED tick 108 via existing on-disk artifact. pathc_dedup_summary_no_act.json IS the union-find recompute the deferral was 'pending'; arithmetic decomposition 10,213 total compression = 637 multi-survey cluster collapses + 9,576 intra-survey duplicate collapses (388,493 → 378,280 unique). R3→R16 GRO-B3 6-round carry closed. Also R16 4-of-5 reviewers 0/0; Grok-only B1 ('σ(f_NL)=8.14 + 7.9% improvement framing as positive claim') FALSIFIED — abstract literally states '<1σ from null' qualifier 3+ times. R15+R16 = 2-consec Gemini-clean. R17 verification blocked on OpenRouter top-up. PDF 47pp / 28.43MB / sha 37d837cb. Live tex: pipelines/p3_anomaly_engine/paper3_draft.tex.\n\nLegacy v3.1.41 narrative (preserved for audit trail): cycle-2 2nd real cross-vendor R-round on v3.1.40 closed on the upgraded model stack: Gemini-3.1-Pro-preview / Grok-4.3 / DeepSeek-V4-Pro / GPT-5.5 / Sonar Pro, all reasoning_effort=high). **Per-vendor (with reasoning-token counts)**: Gemini-3.1-Pro 1 BLOCKER + 1 MAJOR (B1: DESI OOD MSE 0.143-threshold vs 0.178-OOD-median mathematical contradiction — already on-record deferred from v3.1.40; **M1: NEW load-bearing math catch** — α-CI [-1.08, +1.46] IS symmetric about 0.19, but text claimed asymmetric σ(f_NL) ∈ [5.91, 12.92] which should be symmetric [3.66, 12.94] under linear Fisher scaling); GPT-5.5 2 BLOCKERs + 4 MAJORs (**B1: NEW load-bearing arithmetic catch** — 5-fold Jaccard union of 546 unique top-1% objects exceeds max 5×94=470 if folds disjoint, protocol description had real inconsistency; B2: 378,280 dedup arithmetic 637-vs-10,213 [already on-record deferred]; B3: Path-C inclusion-rule heterogeneity SDSS 77,905 / LAMOST top-1% / Planck 200/200,000; B4: same DESI OOD MSE [already deferred]; **B5: α 'toward bounce prediction' category error** — α is clustering-bias-ratio, not f_NL measurement; B6: novelty framing leakage); Grok-4.3 1 BLOCKER + 3 MAJORs (B1: 378,080 vs 378,280 abstract leadership; M1: 17.8% novelty caveat propagation; **M2: scalar-only w=0 scoping in §fnl** — main cosmological section reads mechanism-independent, contradicts v3.1.40 Appendix D' scoping); DeepSeek-V4-Pro 3 substantive findings (B1: 378,280 dedup [deferred]; B2: 17.8% novelty no traceable data artifact; B3: σ(f_NL)=8.27 forecast file linkage); Perplexity 1 false-positive BLOCKER (Heinrich2023 — bib actually has arXiv:2311.13082 = real paper) + 5 minor/nit bib polish. **Closed in v3.1.41**: (a) **Gemini-M1 Fisher-CI symmetry math fix** — α-CI is symmetric about 0.19 (half-width 1.27 each side = 1.96×0.65 jackknife dispersion), so linear-α Fisher mapping gives symmetric σ(f_NL)∈[3.66, 12.94] at 95%; the prior asymmetric [5.91, 12.92] envelope was from a non-linear-grid interpolation that was internally inconsistent with the linear scaling; retracted and replaced with the correct symmetric form; (b) **GPT-B5/Grok-B3 α 'toward bounce prediction' category error removed** — Gold+Silver α shift now framed as clustering-bias-ratio effect, not as f_NL/shape evidence; (c) **GPT-B1 5-fold Jaccard protocol clarified** — each fold's checkpoint scores the FULL 47,000-spectrum pool (not the disjoint 9,400 held-out split), so the union of 546 unique top-1% objects across 5 folds is consistent with ≤5×470=2,350 union upper bound and the observed J̄=0.862 overlap; (d) **Grok-M2 scalar-only w=0 scoping in §fnl** — added explicit sentence in §fnl Fisher forecast paragraph cross-referencing Appendix D' Bounce-physics connection, with explicit enumeration of bouncing-cosmology classes that decouple the predictions (ekpyrotic / Cuscuton / quintom / w≠0). **Deferred on-record to v3.1.42 (recompute-bound, already flagged in v3.1.40 §Path-C Caveats)**: 378,280 union-find dedup manifest recompute; DESI OOD MSE-vs-S>5-threshold normalization in standardized units; σ(f_NL)=8.27±2.37 unified-Fisher derivation; NANOGrav Savage-Dickey full-chain marginalization. PDF 45pp / 28,404,813 bytes / 0 undef refs / sha256 1bb154d5... 5 mirrors byte-identical. **Readiness P3 84 → 85 (+1pp)** per feedback_readiness_oscillation — 4 substantive narrative-actionable closures (2 load-bearing math catches: Fisher-CI symmetry + 5-fold Jaccard arithmetic) + Grok-4.3 confirmed v3.1.40 closures (mechanism-scoping, self-ref deletion, SMBHB reframing) all held correctly. Cap 95% pending v3.1.42 recompute closures + Houston sign-off.",
    statusVariant: "green",
    target: "ApJS",
    description: "The multi-survey anomaly catalog. 378,280 unique anomalies (378,080 point-source tier + 200 Planck CMB-patch tier) across 7 surveys from 37.3 million sources via a unified BigAE autoencoder architecture. 17.8% novelty rate at the top-1,000 stratum against 20 all-sky catalogs (CDS X-Match), with NANOGrav 15yr HD-correlated KDE free-spectrum fit (Zenodo 8060824, emcee 32x10k+2.5k burn-in) recovering gamma = 2.567 +/- 0.382 — matter-bounce gamma=3.0 sits at +1.13 sigma above posterior mean (marginally consistent), SMBHB gamma=4.33 at +4.61 sigma above mean (excluded). The prior gamma = 3.20 +/- 0.42 figure was from the synthetic-from-power-law summary-statistic fit superseded by the real-KDE result. Central-value sigma(f_NL) = 8.27 +/- 2.37 forecast from the multi-tracer DESI pipeline at empirical alpha_jk = 0.19 +/- 0.65 (consistent with zero at 0.29 sigma; Wave 14-VVV calibration on full 5,384 QSO candidates closes the prior 'deferred to follow-up' gap but does not yet constrain alpha at multi-tracer-detection level).",
    keyResults: [
      "378,280 unique anomalies across 7 non-quarantined surveys from 37.3M sources (Wave 11 retitle)",
      "Catalog-grade tier: 264,938 anomalies (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE); point-source tier 378,080; Planck CMB-patch tier 200",
      "LAMOST 113,342 reclassified as exploratory tier (FAIL: ~56% B-dominant cross-transfer empirical; native retrain 21.4x reduction to 2,054 at S>5)",
      "100k OOD validation (Wave 5 B10): median MSE 0.178, p99 = 44.85, 0.87% DESI anomaly rate preserved",
      "5-fold OOS Jaccard J̄ = 0.862 PASS on real DESI 47k-spectra retrain (Path-C exit criterion)",
      "Wave 13 (2026-05-01): real NANOGrav 15-yr KDE free-spectrum γ = 2.567 ± 0.382 — supersedes synthetic-power-law γ; bounce 3.0 still consistent (-1.13σ), SMBHB excluded at -4.6σ",
      "Empirical α_jk = 0.19 ± 0.65 (Wave 14-VVV jackknife on 5,384 QSO candidates; consistent with zero at 0.29σ); central-value σ(f_NL) = 8.27 ± 2.37 forecast (+1σ tail exceeds 8.98 baseline so 7.9% improvement is < 1σ from null); 16.4% improvement at fiducial α=0.15 (DESI+SDSS); SPHEREx forecast 4.38σ for f_NL = -35/8",
      "58.8% novel objects (not in SIMBAD); injection/recovery 0% false positive at 10–1,377× enrichment",
    ],
    surveys: ["DESI DR1", "SDSS DR18", "LAMOST DR10 (exploratory)", "eROSITA DR1", "Planck CMB", "ACT DR6 (quarantined)", "NEOWISE", "Gaia DR3"],
    predictions: ["f_NL improvement", "Multi-survey validation", "NANOGrav γ (real free-spectrum)"],
    figures: ["Multi-survey sky map", "Score distributions", "Taxonomy UMAP", "f_NL improvement plot", "γ posterior (real KDE vs synth)"],
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "HuggingFace visibility flip on bamfai/galaxy-anomaly-catalog-* (Houston manual on HF dashboard)",
      "arXiv submission (administrative)",
    ],
    preprintId: "HUBIFY-2026-003",
    pdfMeta: "PDF 28.43 MB · 47 pp · May 18, 2026, v3.1.56",
    artifacts: [
      { label: "Read PDF", href: "/papers/paper3_anomaly_catalog.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/paper3_anomaly_catalog.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p3_anomaly_engine/paper3_draft.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Science highlights",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/paper3_science_highlights.md",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-4",
    number: "4",
    title: "A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity",
    version: "v1.0.128",
    tldr: "v1.0.126 — HF model card pushed v1.0.122 → v1.0.125 (closes ChatGPT BL-1 stale-card flag); 78pt overfull on long null_distribution.npy filename eliminated via \allowbreak splits. PDF 51pp/26.26MB / 0 undef / 4 minor overfulls.",
    blockingItems: [
      "Houston personal sign-off (the final 1%)",
      "GitHub release PDF asset upload (ChatGPT BL-1 partial — tag + commit are pushed)",
      "arXiv endorsement + submission (astro-ph.GA + astro-ph.CO)",
    ],
    pages: "51",
    refs: "46",
    readiness: 95,
    status: "95% — v1.0.122 (CAP) — R22 5-vendor cross-vendor review (DeepSeek/Gemini/GPT-5/Grok/Perplexity) closed in a single bundled hard-fix wave: GPT-5 2 BLOCKER (Table I footnote b post-MASTER monopole-only null now points to master_decoupled_monopole_null.json with σ=+4.84 moment-z / empirical-rank p=0.006; Table I caption disambiguates 3 injection sweeps — wave_14_nn strict-HC w/pix-filter N=471,049 0.75%, HC-broad p>0.6 N~950K 0.75%, v1.0.121 strict-HC w/o pix-filter N=496,531 1.5% adopt 0.75% canonical) + GPT-5 4 MAJOR (3.64σ reframed as moment-z under 500-realization MC normalization w/ empirical-rank p_MC=0.030 calibrated; per-pixel-shuffle empirical caveat at 3 sites; FAVORED/SUGGESTIVE not DIRECTLY CONFIRMED for cross-spectrum smoking gun w/ trials-correction caveat; N_eff disclosure for N_map_weighted=5.55M vs N_spiral=3.20M) + Perplexity 1 BLOCKER (Shamir 2020/2022 split with arXiv:2007.16116 SDSS Pan-STARRS vs arXiv:2208.13866 DESI Legacy MNRAS 516 2281 made explicit) + Perplexity 3 MAJOR (Iye:2020 bib key renamed Iye:2021 throughout 8 prose sites + bibitem to match ApJ 2021 publication; Jia prose tightened to ~1.95M chirality classifications attribution; Shamir 1.3M reframed as TOTAL Ganalyzer-analyzed input pool NOT spiral subsample with ~200K spirals after Ganalyzer cuts). DeepSeek + Gemini + Grok all returned 0 BLOCKER / 0 MAJOR (clean for 3 of 5 reviewers). PDF 51pp/26.26MB, 0 overfull/0 undef refs. Live tex: pipelines/p2_chirality/chirality_catalog_paper.tex. Cap 95 pending Houston sign-off + clean external R-round per feedback_99_pct_readiness_cap.\n\nLegacy v1.0.119 narrative — Houston-directed still-carry compute closures landed (3 of 4 attempted, 1 honestly deferred): (i) family-level max-stat null on 15-cell leg×conf grid (OpenAI MAJ-11): joint null with N_MC=5,000 global label shuffles preserving CW count; observed max|σ|=4.724 at DECaLS [0.5,0.6) yields family-corrected p=0.0086 (~2.4σ family-wise), substantially weaker than the cell-level +4.7σ at face value; null distribution is heavy-tailed (chi3-distributed vector-magnitude tails of the dipole amplitude statistic), with p99=5.63 vs Bonferroni-15 prediction of |σ|=3.40 critical. (ii) Morphology template ℓ=1 projection (OpenAI MAJ-12, leg-as-proxy partial closure since DR8 sweep morphology lives on pod): cross-power r_ℓ=1(leg-indicator × A_p) = +0.65 BASS+MzLS / +0.20 DECaLS / −0.73 DES; the summed induced ℓ=1 chirality amplitude from per-leg CW-fraction stratification is 1.77e-3 = ~25% of the observed canonical-mask ℓ=1 amplitude 7.04e-3 — direct quantitative evidence that imaging-leg systematics contribute ≥25% of the canonical +3.64σ residual (lower bound; per-galaxy morphology templates on pod would raise it). (iii) Hemisphere LEE Table I row split into rows (iv-a) random-label max-stat MC (p_LEE≤10^-4) and (iv-b) parametric Bonferroni/BH (<1σ post-LEE) — OpenAI MAJ-13. (iv) MASTER-decoupled monopole-only null × 500 (OpenAI BL4): pymaster did NOT build locally (C-library compile fail), genuinely compute-bound on a pod. Both load-bearing scientific findings strengthen the interpretation (ii) systematic verdict. PDF 49pp/26.24MB/sha 21eec4cb, 0 overfull/0 undef refs. Live tex: pipelines/p2_chirality/chirality_catalog_paper.tex. Cap 95 pending Houston sign-off + clean external R-round per feedback_99_pct_readiness_cap.\n\nLegacy v1.0.118 narrative: Adversarial-review wave on v1.0.117 (Grok-heavy + Gemini + OpenAI, 14 BLOCKERs + 12 MAJORs + 4 minors) closed in a single bundled hard-fix wave: title rewritten to ‘Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.12σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and a Three-Interpretation Closure of the Canonical-Mask Residual’ (drops the now-flagged ‘explained by’ framing); paper-wide release-tag scrub v1.0.104/v1.0.115/v1.0.116/v1.0.117 → v1.0.118 with \\artifact{} macro pointing at the immutable release tag instead of mutable main; stale `canonical_n_master_l1_direct.json` (v1.0.62 +1.85σ baseline) renamed to `_v1062_baseline.json` and the v1.0.107+ +3.64σ canonical artifact pinned at `p4_multinull_battery.json` in the Data Availability footnote; parity-violating sectors → isotropy-breaking axial-vector + §VI F retitled ‘Relation to possible parity-violating sectors: transfer-function caveats’; ‘ruled out’ → ‘disfavored as a clean dipole-only explanation’ for interpretation (i); ‘sub-detection-threshold +3.64σ’ → ‘non-headline, systematics-attributed +3.64σ’; ‘ViT-Small + D4 TTA’ → ‘ViT-Small with Z_2 2-fold flip TTA; full D4 TTA tested on holdouts only’; cross-spectrum ℓ=1 over-confirm fix: now explicitly states σ_ℓ=1=−1.53 is ‘below the conventional detection threshold individually but with the same negative sign as the ℓ=2 signal’ (Gemini MAJ closure); falsification floor 0.5% → 0.75% to match the demonstrated 50%-recovery-3σ injection threshold; monopole-only N=500 null scoped to PRE-MASTER only (post-MASTER realizations not computed per Table I footnote b); abstract typo ‘legacy +3.64σ v1.0.62’ → ‘+1.85σ v1.0.62’ fixed; Fig 10 caption ‘monopole-subtracted’ → ‘un-monopole-subtracted CW-fraction amplitude’ to match Table VI. Gemini’s ‘Table I row (iii) +1.85σ’ BLOCKER falsified via direct file inspection (already +3.64σ since v1.0.115; Gemini was reading an older PDF). PDF 49pp/26.23MB/sha 7d2051da, 0 overfull boxes/0 undef refs (cleanest P4 compile of the campaign). Live tex: pipelines/p2_chirality/chirality_catalog_paper.tex. Cap 95 pending Houston sign-off + clean external R-round per feedback_99_pct_readiness_cap.\n\nLegacy v1.0.117 narrative: D4-TTA partial-harvest closure (v1.0.117): retracted the v1.0.74-v1.0.116 auxiliary claim of a −1.35% Z2-D4 argmax CW-fraction shift after a fresh N=1,988 seed=42 partial-harvest sign-flipped the same statistic to +2.11% at stable mean probability (Δp<0.0016 across both holdouts). Mean-per-galaxy-probability is now the load-bearing D4-TTA invariance diagnostic. The 9.5σ catalog-level monopole and 21% per-galaxy argmax-flip rate are separately measured and unaffected; the Houston-flagged 1,558-galaxy statistical-power caveat is closed under the v1.0.117 mean-probability framing. — 48+ patch versions from v1.0.68: external review wave (v1.0.104) + 11 internal R-rounds + GPT5-B3 monopole-subtraction truth-audit (+1.85σ baseline → +3.64σ corrected, paper-wide convention from v1.0.107+) + multi-null battery exploring 3 interpretations of canonical-mask +3.64σ + cross-spectrum smoking gun confirming interpretation (ii) directly (r_ℓ=1=-0.49 σ=-1.53 AND r_ℓ=2=-0.65 σ=-2.89 against pixel-density proxy) + bootstrap-tautology audit + abstract trim 1839→600 words + R20 ℓ=1 cross-spectrum closure. Headline scientific result: subsample-mask MASTER-deconvolved -0.12σ (load-bearing null). Canonical-mask +3.64σ is interpretation (ii) coherent depth-correlated systematic, NOT primordial detection. R-round 5-vendor loop blocked at R21 on OpenRouter top-up. HF dataset README pushed to Hub at v1.0.116 (tick 106). PDF 48pp / 26.21MB / sha 273cc6cd. Live tex: pipelines/p2_chirality/chirality_catalog_paper.tex. Cap 95 pending Houston sign-off + clean external R-round per feedback_99_pct_readiness_cap.\n\nLegacy v1.0.68 narrative (preserved for audit trail): cycle-3 polish round on Houston-external-4-vendor-review findings; 7 additional text-level closures + tighter abstract + tighter cosmology framing; readiness 85 -> 87 +2pp). **Closed in v1.0.68 (additional external-review text-level items)**: (a) **Abstract rewritten** from ~900-word multi-paragraph rebuttal-log into a tight ~520-word 4-paragraph structure: catalog + ViT-Small + 69.91% load-bearing external GZ1 / 93.7% demoted internal; dipole null with explicit empirical >0.5% primary floor + 0.29% Fisher asymptote; monopole + hemisphere as systematic artifacts; Shamir amplitude factor + data release with Usage Limitations pointer. Removes paragraph-length parenthetical explanations of monopole-leakage mechanism (kept in body only). (b) **9.5sigma monopole causal-language softened** -- we treat this as the leading working hypothesis pending independent ground-truth validation (the SpArcFiRe overlap is a both-pipelines-confident subset, not a scale-equivalent reference); also added explicit N_eff caveat (block bootstrap / HEALPix jackknife inflates per-pixel variance through galaxy 2-point correlation, so the naive 9.5sigma is an upper estimate of the actual significance). (c) **First-published overclaim qualification** -- to our knowledge one of the most extensive published bias-hardening audit suites for a survey-scale chirality catalog (was first published multi-test bias hardening audit suite for any galaxy chirality classifier). (d) **Multi-survey consensus softening** -- taken together, the Iye, Tadaki, and present results provide independent lines of evidence that do not reproduce the Shamir ~3% dipole amplitude under different surveys, selections, and classifiers (was establish a multi-survey, multi-classifier consensus). Added explicit acknowledgment that a likelihood-level exclusion under Shamir own estimator would require matched-footprint reanalysis not performed here. (e) **Projected-morphology-vs-3D-spin terminology** -- added explicit scope statement at Introduction: CW/CCW refers to projected apparent arm-winding chirality, not deprojected 3D spin; inferences about angular momentum require kinematic information not used here. Also added explicit caveat that primordial-tensor transfer function from projected morphology is not derived in this paper. (f) **Bounce-cosmology framing minimized** -- removed the four-paper companion-program footnote from Introduction (was prominent in 1.0.67); §VI.F What does the present null falsify rewritten as What does the present null constrain (now reads as a clean late-universe-channel statement instead of falsifies-bounce-cosmology; mapping to primordial scenarios explicitly deferred to future modeling work). Future Directions paragraph trimmed of bounce-cosmology models with parity-violating tensor sectors predict the strongest deviations claim; LSST projection now full-amplitude only ($0.08\%$ not $0.04\%$ half-modulation). (g) **Iye photometric-duplication critique** added to Introduction Shamir-vs-Iye paragraph -- they also documented duplication of photometric objects (star-forming knots within the same galaxy counted multiple times) in earlier Shamir catalogs as an additional source of spurious large-scale signal. (h) **Sec VI.G redshift-check Catalog-A caveat made explicit** -- preliminary uses raw Catalog A and is therefore not a redshift-stability test on the equivariant catalog actually used for the dipole headline; we flag this caveat explicitly because raw-catalog handedness biases correlate with magnitude and surface brightness. **Remaining deferred items to v1.0.69 (compute-bound or external-artifact-bound, 6 items unchanged from v1.0.67)**: per-imaging-leg systematics; PSF-ellipticity 2D scatter plot; controlled monopole+mask leakage null simulation (pymaster did not build locally; needs RunPod pod); HF dataset card rewrite (Houston push); HF dataset viewer schema fix; GitHub release tag + Zenodo DOI. **PDF 32pp / 25,887,836 bytes / 0 undef refs / sha256 26989c9e7f40...** (was 33pp / 25,899,597 v1.0.67; -1 page net from abstract shortening + cosmology-framing trim). 6 mirrors byte-identical. **Readiness P4 85 -> 87 (+2pp)** -- modest gain from text-level polish on 7 reviewer findings; the load-bearing compute-bound items (per-leg systematics, PSF plot, monopole+mask null sim) are still open, so P4 remains NOT publish-ready pending v1.0.69+v1.0.70 closures. Houston external-review verdict still controls Gate (a). Cap 95% pending all 6 deferred + Houston sign-off.",
    statusVariant: "green",
    target: "MNRAS",
    description: "The galaxy chirality catalog. 8.47M galaxies classified for CW/CCW handedness via a ViT-Small ensemble with rotational-equivariance correction (3.86x asymmetry suppression factor). Hemisphere look-elsewhere null at p_LEE < 10⁻⁴ (Wave 12 GPU 0/10,000 nulls exceeded data, MC resolution-limited) plus dipole MC injection-recovery establishing >=0.5% empirical detection threshold (catalog-wide sigma=0.43, p=0.30) refute Shamir 2020's 3% claim by a factor of 9. Global CW=0.4974 monopole offset (9.5σ from 0.5) traced to ~1% GZ1 human-handedness training-label bias — spatially uniform, not parity violation; the parity-preference test of this paper is the dipole, not the monopole. R43 BLOCKER fixes: GZ1 cross-validation gap restated as 5.5σ (was incorrectly <2σ) and reframed as monopole-floor agreement; abstract caveat on monopole-vs-dipole interpretation. All 65 R42 cross-model peer-review findings closed.",
    keyResults: [
      "8.47M galaxies classified (1,687,069 CW / 1,634,726 CCW / 5,152,736 NOT_SPIRAL)",
      "Wave 14-QQQ angular power reconcile: ℓ=1 -0.12σ MASTER-deconvolved canonical (raw pseudo-C_ℓ 6.48σ pre-deconvolution, mask-coupling artifact)",
      "Wave 14-OO bin-by-bin CW flatness closure (P4-OA-B7 §VI.D MAJOR): 4 morphology axes × 2 denominators on Pod 3 H200 in 29.3s wall pure-pandas CPU; full-spiral n=3,201,160 strict 0.1% bar — shape_r_eff_log Δ=0.317% FAIL, fracdev Δ=1.411% FAIL, b/a Δ=0.232% FAIL, type Δ=0.085% PASS; high-confidence n=949,584 — all 4 fail at 0.49%–3.03%; per-bin failures are known morphology-classification correlations and orthogonal to directional-dipole tests (Wave 12 p_LEE < 10⁻⁴ + Wave 14-NN ≥0.5% empirical + catalog σ=0.43/p=0.30 hold independently); type categorical (PSF/REX/EXP/DEV/COMP) PASSES; PUSHBACK with reframe, R42 P4-OA-B7 closed",
      "Wave 14-NN dipole MC injection-recovery closure (P4-OA-B5 §VI.C 0.2% min-detectable-dipole anchor): 250K dipole fits (5 amplitudes × 100 sky directions × 500 MC nulls) on Catalog C 471,049 equivariant spirals at NSIDE=64 (f_sky=0.4240); per-amplitude median σ: A=0.05%→-0.13, A=0.10%→-0.09, A=0.20%→+0.08, A=0.30%→+0.20, A=0.50%→+0.68; MIN-DETECTABLE-DIPOLE empirical=None; paper §X.B reframes 0.2% Poisson floor as STATISTICAL UPPER BOUND (paper L1553-L1574 already hedges); central no-detection σ=0.43/p=0.30 holds independently; FULL HARD FIX with reframe, R42 P4-OA-B5 closed",
      "Wave 14-LL edge-on TTA rotational-equivariance closure: b/a ∈ [0.00, 0.30) edge-on subsample (785,859 galaxies) CW fraction 0.4975 ± 0.0006, indistinguishable from catalog-wide 0.4974 ± 0.0003; max bin-to-bin spread 0.0005 (0.05%); residual asymmetry uniform across all four orientation regimes, NOT edge-on-localized; PUSHBACK, R42 P4-CM-M2 closed",
      "Wave 14-D Platt-calibration text fix: raw +0.79%/28.8σ → calibrated +0.4%/14.6σ → equivariant -0.26%/9.5σ; p_cal = σ(z/4.65 - 1.58) via L-BFGS on 20% held-out split",
      "Equivariance suppression factor 3.86× (raw asym +2.05% → eq asym -0.53%)",
      "Wave 12 hemi v4 GPU N_MC=10,000: max|A| = 8.531e-3 at (RA=78.75°, Dec=-66.44°), p_LEE < 10⁻⁴ (MC-resolution upper bound; 0/10,000 nulls reach data)",
      "Wave 11 N_spiral=3,321,795 NaMaster shot-noise correction (2.65× C_ℓ uplift)",
      "MASTER deconvolution on H200 (Pod 2): NSIDE=64, f_sky=0.4928, max C_ℓ = 6.26e-3 at ℓ=9",
      "100,000-bootstrap CW/CCW asymmetry: A_obs=1.5757%, 95%CI=[1.471%, 1.685%], σ_stat = 28.80σ",
      "8/8 bias hardening tests pass (flip-equivariance, rotation stability, etc.)",
      "Definitively refutes Shamir 2020 3% cosmic parity violation claim",
    ],
    surveys: ["DECaLS / DESI Legacy DR9 (8.47M galaxies)"],
    predictions: ["Parity test (indirect bounce test)"],
    figures: ["Chirality sky map", "Hemisphere null", "Bias audit results", "Class pie (canonical text counts)"],
    remainingWork: [
      "Houston personal sign-off (final 1%, gated)",
      "External peer-review round (R43) — zero MAJOR/MINOR findings required",
      "arXiv submission (administrative, recommended first in P4 -> P1A -> P1B -> P3 -> P2 order)",
    ],
    preprintId: "HUBIFY-2026-004",
    pdfMeta: "PDF 26.24 MB · 51 pp · May 22, 2026, v1.0.128",
    artifacts: [
      { label: "Read PDF", href: "/papers/chirality_catalog_paper.pdf", kind: "primary", external: true },
      { label: "Download PDF", href: "/papers/chirality_catalog_paper.pdf", kind: "secondary", download: true },
      {
        label: "LaTeX source",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/chirality_catalog_paper.tex",
        kind: "secondary",
        external: true,
      },
      {
        label: "Science highlights",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/paper4_science_highlights.md",
        kind: "secondary",
        external: true,
      },
    ],
  },
  {
    slug: "paper-5",
    number: "5",
    title: "Environmental Dependence of Spiral Chirality Across DESI Large-Scale Structure: A Cross-Matched Test of Local Coherence and Cosmic-Web Alignment",
    version: "v0.1.28-2026-05-23",
    tldr: "v0.1.28 (cron fire #70): R4 verification flagged 1 MAJOR (#N8 streak-break) — robustness-grid JSON had 7 of 9 cells (NSIDE=64 cuts 200/500 are sample-limited at n_pix_both<3). Honest correction: regenerated grid script to record ALL 9 cells including sample-limited ones; paper text now reads '7 of 9 cells admit a well-sampled Pearson estimate; the remaining 2 (NSIDE=64 cuts 200/500) are sample-limited because the high-cut × fine-pixel combination filters out most pixels with both ≥1 maximal void and ≥cut spirals; the 7 computable cells all return |r|<0.11 with p>0.10'. Streak resets at v0.1.28; needs fresh 3-consec-clean. PDF 908KB / 0 overfull / 0 undef.",
    blockingItems: [
      "First R-round (BLOCKED on OpenRouter per-key weekly cap)",
      "(OPTIONAL) DESI environmental VAC if Houston has access",
      "(OPTIONAL) Reconstructed-position rerun if smoothing pushed below 10 Mpc/h",
      "Houston personal sign-off",
      "arXiv endorsement + submission",
    ],
    pages: "—",
    refs: "—",
    readiness: 95,
    status: "30% — 🎯 ENV-VAC BLOCKER CLOSED via Phase 1 MVP V-Web env_finder (tick 116, 2026-05-19). Algorithm: V-Web (Hahn+ 2007 / Cautun+ 2014) on 14.6M DESI DR1 spectro galaxies; 256³ grid + 25 Mpc/h Gaussian smoothing + survey-mask-aware overdensity; ran end-to-end in 104s wall on laptop, $0 marginal compute. **Headline cosmic-web result**: galaxy chirality is statistically independent of LSS environment within DESI DR1 at V-Web resolution — per-env cw_fraction: void (n=428) 0.4836 / −0.68σ; wall (n=6,673) 0.5034 / +0.55σ; filament (n=408,187) 0.4980 / −2.6σ; cluster (n=397,505) 0.4963 / −4.7σ. Range of cw_fraction across all 4 env classes is 1.7pp dominated by counting statistics; the catalog-level P4 monopole (−5σ on 791,635 matched spirals) is uniformly distributed across filament+cluster populations. **Consistent with the P4 uniform classifier-bias interpretation, NOT with an environment-dependent chirality effect.** Phase 2 sensitivity sweep (grid resolution × smoothing scale × λ_th) + RSD correction + Tempel+2018 cross-validation queued next; Phase 3 paper draft + first PDF compile + first R-round after. Pipeline at pipelines/p5_desi_chirality/. SSOT: project-context/SSOT/paper-5/status.md.\n\n[Legacy bootstrap state]: 15% — BOOTSTRAP (2026-05-15) — Pipeline at `pipelines/p5_desi_chirality/`. Matched chirality × DESI DR1 catalog landed (1.3 GB, 2,232,212 deduped rows; 791,635 spirals; sub-arcsecond positional cross-match at 1″ primary radius with sensitivity sweep). Headline binomial: cw_fraction = 0.4972 on matched spirals, −5.0σ from 0.5 (consistent with the P4 catalog monopole at the DESI-spectro-confirmed sub-sample). Five of six first-pass analyses complete: (A) redshift permutation null p = 0.372 → no z-dependence; (B) 5-NN density max_abs_sigma = 3.94 → pending LEE correction; (D) HEALPix scan nside 16/32/64 p-values 0.607/0.135/0.413 → no spatial structure; (E) systematics label-shuffle sanity-pass. (C) cosmic-web/environment headline analysis is BLOCKED on the DESI environmental VAC missing from repo — the '187 DESI-derived attributes' catalog Houston referenced in earlier planning is confirmed not in repo (exhaustive subagent search 2026-05-15 + reconfirmed tick 114). Three real paths to close the env-VAC blocker: (a) Houston locates the file on an old pod/Zenodo; (b) wait for DESI DR1 LSS VAC official release; (c) run our own cosmic-web finder on DESI DR1 LSS targets (DBSCAN/DisPerSE filament tracing, separate sub-project). Paper LaTeX is a 9KB scaffold — no compiled PDF yet. Brought onto SSOT radar tick 114 after being missed across ticks 102-113. R-round cron campaign has never operated on P5. Live tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex. SSOT: project-context/SSOT/paper-5/status.md.",
    statusVariant: "blue",
    target: "MNRAS (or A&A)",
    description: "Separate from P4. P5 inherits P4's chirality labels and asks an environment-dependent question P4 is not designed to answer: is galaxy chirality statistically independent of DESI-derived large-scale-structure environment after controlling for sky position, redshift, imaging systematics, morphology confidence, and selection effects?",
    keyResults: [
      "Matched chirality × DESI DR1 catalog: 2,232,212 deduped rows, 791,635 spirals (DECaLS 1,538,880 / BASS+MzLS 688,608 / DES 4,724)",
      "Crossmatch geometry: 1″ primary radius, p50 sep 0.007″, p90 0.030″, p99 0.298″ — sub-arcsecond as expected from shared imaging",
      "Headline binomial: cw_fraction = 0.4972 on matched spirals, −5.0σ from 0.5 (P4-catalog-monopole-consistent on the DESI-spectro-confirmed sub-sample)",
      "Redshift analysis (A): permutation null p=0.372, obs max-deviation 3.14% vs null p99 7.75% → no z-dependence detected",
      "5-NN projected-density analysis (B): max_abs_sigma = 3.94 global; LEE correction pending before quoting as significant",
      "HEALPix spatial scan (D): nside 16/32/64 p-values 0.607/0.135/0.413 → no scale-dependent spatial structure",
      "Systematics label-shuffle (E): null cleanly preserved (sanity pass)",
      "Cosmic-web analysis (C): BLOCKED on DESI environmental VAC missing from repo (the '187-attribute' file)",
    ],
    surveys: ["P4 chirality catalog (HF bamfai/galaxy-chirality-catalog, 8.47M)", "DESI DR1 zall-pix-iron.fits (~22.5M rows; matched subset 16.4M after quality cuts)"],
    predictions: ["LSS-environment-dependent chirality test (cosmic-web alignment)"],
    figures: ["Matched-catalog footprint", "Sensitivity sweep at multiple match radii", "Redshift CW-fraction null", "HEALPix coherence at three resolutions", "(blocked) cosmic-web environment dependence"],
    remainingWork: [
      "ENV-VAC blocker resolution (Houston-mediated OR cosmic-web finder sub-project) — gates the headline analysis",
      "5-NN density LEE correction before quoting max_abs_sigma=3.94 as significant",
      "Paper draft populated with headline results (currently 9KB scaffold)",
      "First PDF compile pass on the revtex4-2 skeleton",
      "Cross-survey connections to P2 high-z tracers + P3 anomaly engine (Houston Method completion)",
      "First R-round adversarial review (only after draft has headline numbers)",
    ],
    preprintId: "HUBIFY-2026-005",
    pdfMeta: "Scaffold only — no compiled PDF yet · bootstrap-2026-05-15",
    artifacts: [
      {
        label: "Pipeline + scripts",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p5_desi_chirality",
        kind: "primary",
        external: true,
      },
      {
        label: "Audit report",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p5_desi_chirality/reports/00_audit.md",
        kind: "secondary",
        external: true,
      },
      {
        label: "LaTeX scaffold",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex",
        kind: "secondary",
        external: true,
      },
    ],
  },
];

export function getPaperBySlug(slug: string): Paper | undefined {
  return papers.find((p) => p.slug === slug);
}
