# EXTDB P2 Grok — chat: https://grok.com/c/113398f6-91c3-49b1-8172-28f570777069

Provider: Grok
Model/Tier: Expert (Thinks hard)
PDF: /tmp/EXTDB_P2.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Thought time: 1m 26s
Round: EXTDB (DE-BIASED, R57 PDFs)

---

Referee Report: MNRAS / Phys. Rev. D / JCAP
Paper: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Author: Houston Golden
Date: 26 June 2026

1. Recommendation
MINOR REVISIONS

The paper is a careful, technically solid sensitivity recast that adds genuine value through its bispectrum normalization audit, template-overlap quantification, and Bayesian model-comparison framework. It does not overclaim (explicitly labels itself a recast, not an independent forecast) and maintains high transparency on assumptions and approximations. No calculation errors, internal inconsistencies, or fatal methodological flaws were identified in the rendered PDF. The work is publishable after addressing a small number of clarity, completeness, and scoping issues detailed below.

2. BLOCKERS
None.

3. MAJORS
None.

4. MINORS

M1 (Presentation / Reproducibility — MINOR)
The headline "~2.6–5σ realistic" range in the abstract and Sec. IV is scientifically honest but not self-contained. The text later decomposes it (GR-only floor ≈3σ; all-combined conservative endpoint 2.6–2.8σ; partial-budget variants filling the upper part of the band), yet a reader scanning only the abstract cannot map the quoted interval to specific systematic combinations without hunting through Sec. VII and Table IV. Add a single parenthetical or footnote in the abstract explicitly tying the lower/upper edges to the combinations used. Low-effort clarity fix.

M2 (Completeness of Uncertainty Budget — MINOR)
The quadrature combination of systematics is labeled a "transparent scoping choice whose conservatism a full joint Fisher would need to confirm." Appropriate language, but the paper does not supply a compact breakdown table showing the contribution of each term to the final σ_eff or significance degradation. Such a table would let readers assess sensitivity to individual items and verify that the 2.6–5σ envelope is robust. Polish item, not a scientific gap.

M3 (Derivation of ε-correction Range — MINOR)
Sec. II C states that explicit cubic-action prefactors give ~0.6% while mode-function growth "potentially amplifies to ~1–8%," yielding fNL ∈ [−4.35, −4.02]. No intermediate numerical values, scaling formula, or reference for the mode-function amplification factor are provided. Because this range directly informs the recommended σ_theory = 1.0 Gaussian prior width, a short derivation paragraph or citation would strengthen the claim. Completeness issue, not a correctness issue.

M4 (Scope of MegaMapper Forecast — MINOR)
The 3–7σ envelope for MegaMapper is appropriately caveated as "illustrative… reflects design uncertainty as much as measurement uncertainty." However, the text does not quantify which design parameters (survey area, number density, redshift range, multi-tracer implementation quality) dominate the factor-of-two spread. A one-sentence decomposition would make the envelope more actionable.

M5 (Minor Notation / Cross-Reference Polish — MINOR)
Low-level readability items: consistent use of "gauge-frame" vs. "conformal-Fermi physical-observer frame" when quoting the single-field consistency relation; adding a parenthetical to the abstract's BF ≈ 9–14 statement to align with detailed bookkeeping paragraph in Sec. VI D; cross-referencing the injection-recovery test caveat in Sec. III B when r = 0.84 ± 0.02 is adopted. All straightforward; no new calculations required.

5. Strengths (≥ 3)

S1. Rigorous, self-contained audit of the matter-bounce bispectrum normalization. The symbolic verification of the in-in commutator identity that fixes the Cai et al. full result at −35/8 (Planck convention) and explains the Li et al. single-time-ordering intermediate as exactly half is a valuable technical contribution. The three-benchmark validation (Table I) and convention chain in Appendix A close the loop cleanly.

S2. Multi-method, high-statistics quantification of local-template mismatch. The combination of (i) 10,000-sample null-space Monte Carlo, (ii) Fisher-weighted overlap under ten physically motivated weighting schemes, (iii) 200-realization KSW-style injection-recovery, and (iv) shape-cosine stability (r_cos > 0.97) constitutes best-practice template-projection analysis. The resulting r = 0.84 ± 0.02 (noise-weighted) is robust and properly propagated.

S3. Principled and unusually transparent treatment of both theoretical and observational uncertainties. The explicit six-assumption list (Sec. II C), identification of assumption (d) as the "weakest link," bounded ε-correction, null-space systematic, and additive-quadrature systematics budget with clear caveats set a high standard for forecast papers.

S4. Innovative closed-form Bayesian model comparison validated by three independent 10⁵-realization Monte Carlo ensembles. Prior-sensitivity grid, kinematic-vs-parametric asymmetry discussion, and explicit interpretation caveats are executed at a level rarely seen in single-paper forecasts.

S5. Appropriate self-positioning as a "sensitivity recast." Repeated unambiguous statements that the work imports the Heinrich et al. σ(fNL) ≈ 0.7 baseline and applies controlled degradations manage expectations correctly while still delivering new physics content.

Summary
The manuscript is already at or above the acceptance threshold for a high-bar cosmology journal. The minor revisions requested are almost entirely presentational or completeness-oriented; none alter the central scientific conclusions or require new heavy computations.
