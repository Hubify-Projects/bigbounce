# Final Verdict: Repo-Wide Sync Audit

**Created:** 2026-03-19
**Status:** COMPLETE

---

## 1. Is the gradient-expansion result genuinely new, merely supportive, or superseded?

**MERELY SUPPORTIVE.**

The gradient expansion confirms four structural features (negative sign, O(1) magnitude, local shape, parameter-freedom) that were ALL already established by the in-in execution phase. It does NOT resolve the exact coefficient (-35/8 vs -35/16), which is the only open quantitative question. Its sole new contribution is formalism-independent confirmation, which has paper-level value as a robustness argument but does not advance any frontier question.

13 of 14 claims in the GE verdict are either already known or still open without resolution by the GE. Only 1 claim (independent formalism confirmation) represents a genuinely new contribution.

---

## 2. Does it still address a live frontier question?

**NO.** The live frontier questions are:
1. Resolving -35/8 vs -35/16 (the GE reaches the same bottleneck and cannot resolve it)
2. Sign convention resolution (the GE does not address this)
3. Drafting the forecast paper (the GE adds nothing to the 800,000 MC evidence base)
4. PBH/GW second channel (the GE is irrelevant)
5. LQC formalism sensitivity (the GE is irrelevant)

The GE addressed questions that were live BEFORE the focused-path terminal's extensive work. It was working with an outdated picture of the project state.

---

## 3. What later focused-path work already goes beyond it?

**Substantially.** The focused-path terminal completed 21 directories of work that the GE terminal was apparently unaware of:

| Work Package | What It Achieved | Files |
|-------------|-----------------|-------|
| Cai action audit | Full diagnosis of action discrepancy (3 differences) | `cai_action_audit/` |
| SymPy cancellation | f_NL(T1-T4) = 35/16, matching L-B to 0.07% | `fnl_symbolic_cancellation/` |
| ECH bispectrum gate | Mathematical proof: ECH contributes zero | `ech_bispectrum_gate/` |
| ECH tensor gate | Same closure for tensor sector | `ech_tensor_gate/` |
| Forecast hardening | SPHEREx 3-6 sigma, MegaMapper 2-9 sigma | `forecast_hardening_program/` |
| Fisher surface | k_min sensitivity quantified (factor 100x) | `fisher_robustness_surface/` |
| Ultra-large-scale audit | GR contamination, b_phi, bispectrum channel | `ultra_large_scale_systematics_audit/` |
| Survey realism | SPHEREx first test, MegaMapper follow-up | `survey_realism_reconciliation/` |
| Inflation mimicry | Standard excluded 300x, non-attractor not natural | `inflation_mimicry_deep_comparison/` |
| Bayesian discrimination | Median BF 53:1 (combined), 100k MC | `bayesian_discrimination_program/` |
| GR-aware Bayes | BF > 329 vs SSFSR, 500k MC | `gr_contamination_claim_hardening/` |
| Last-mile robustness | 83% of realizations give BF > 10 | `last_mile_robustness_program/` |
| Mock validation | 200k synthetic spectra, BF 425:1 | `optional_premium_robustness/` |
| Paper packaging | Skeleton, 5 figures, claims table, abstract | `live_forecast_packaging/` |

**Total: 800,000+ Monte Carlo samples, 200,000 synthetic power spectra, 5 publication-ready figures, a complete paper skeleton, and full systematics characterization.** The gradient expansion adds one sentence of robustness to this evidence base.

---

## 4. Should this line continue, or should it be folded into the supporting evidence stack?

**FOLDED INTO THE SUPPORTING EVIDENCE STACK.**

Active extension of the gradient expansion would:
- Lead to the same mathematical bottleneck (growing-mode-squared coupling)
- Provide no computational advantage over the in-in approach
- At best reproduce the 35/16 that SymPy already found
- Consume sessions that should be spent on the paper draft

The GE's key result (formalism-independent confirmation) should appear as 3-4 sentences in the paper or a 1-page appendix. No further computation warranted.

---

## 5. What exact next step should follow immediately after this sync audit?

**DRAFT THE f_NL FORECAST PAPER.**

The entire research program is quantitatively complete:

| Pillar | Status | Evidence |
|--------|--------|---------|
| Theory | f_NL in [-35/8, -35/16], two formalisms | 6 technical directories |
| Forecast | SPHEREx 3-6 sigma, MegaMapper 2-9 sigma | 4 hardening passes |
| Systematics | k_min, GR, b_phi all quantified | 3 audit directories |
| Anti-mimicry | Kinematic vs parametric asymmetry | 2 comparison directories |
| Bayesian | Median BF 53:1 combined, 83% robust | 800k MC samples |

All material exists at `research/live_forecast_packaging/`: skeleton (`01_manuscript_skeleton.md`), claims table (`02_strongest_defensible_claims_table.md`), figure plan (`03_figure_plan.md`), 5 generated figures, abstract drafting notes.

**The science is done. The evidence is assembled. The figures exist. Write the paper.**

### Parallel actions (do not block paper drafting):
1. Correct CLAUDE.md: change "f_NL = 5/12" to "f_NL in [-35/8, -35/16]"
2. Correct results matrix row 27
3. Resolve sign convention (1 session of algebra)

### After paper draft:
1. PBH + induced GW order-of-magnitude estimate (second observable channel)
2. Arbitrary-precision 6-term integral (resolves coefficient -- include as erratum or v2 if completed after submission)

---

## The One-Sentence Summary

The gradient expansion is a valid supporting cross-check that was overtaken by 21 directories of focused-path work; the project's live frontier is now the paper itself, which has all the science, all the figures, and all the evidence it needs.
