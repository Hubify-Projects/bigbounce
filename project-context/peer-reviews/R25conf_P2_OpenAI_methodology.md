# P2 R25conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.47.pdf` md5=a6ea2ee9 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8920 chars)
**Wall time**: 381.1s

---

Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook”

Role focus: methodology rigor, derivations, dimensional analysis, statistical validity, internal arithmetic consistency, and traceability of every scalar quoted in the abstract and conclusions.

Overall assessment: The paper ambitiously attempts three technically demanding tasks: (i) auditing/normalizing the Cai et al. matter-bounce bispectrum and the −35/8 prediction; (ii) quantifying the template mismatch to the local estimator and recasting SPHEREx/MegaMapper sensitivities; (iii) performing a Bayesian model comparison. There is a substantial amount of careful bookkeeping in several places, and many numerical statements check out. However, there are two critical methodology errors and several major issues that must be addressed for Physical Review D standards:

- A fundamental algebraic error in the Bayes factor evaluation inflates all reported Bayes factors against a flat-prior competitor by a factor ~√(2π)σ. This propagates to the headline “BF ~ 10–17” envelope and multiple tables/figures.
- Equation (2) defining BNL is dimensionally inconsistent and contradicts the adjoining text; the numerator/denominator are inverted relative to the stated dimensional argument. This is load-bearing for the shape function discussion.
- The manuscript contains version-history/correction notes and internal bookkeeping/provenance text embedded in the main body, which is not acceptable for PRD presentation.
- Several systematic-degradation percentages and ancillary forecasts are asserted without sufficient derivational detail to be reproducible; some numerical claims are made using non-comparable estimators without sufficiently explicit caveats at the point of juxtaposition.

Detailed findings follow.

ESSENTIAL

P2-E1 (Sec. II.A, p.3–4): Dimensionally inconsistent and self-contradictory definition of BNL
- Offending text/equation: Eq. (1) AT = 3/(256 k1^2 k2^2 k3^2) P(k1,k2,k3). Eq. (2) BNL = (10/3) P/AT Σi k_i^3, followed by “P has degree 9, the prefactor of Eq. (1) removes degree 6, and the Σ k_i^3 denominator removes the remaining degree 3. Note that BNL retains its full dependence on the coefficients (c1,…,c6) through P via AT; no cancellation of P occurs between Eqs. (1) and (2).”
- Problem: With AT as defined in Eq. (1), AT has homogeneous degree 3. The printed Eq. (2) uses P/AT, which has degree 6, and dividing by Σ k_i^3 (degree 3) leaves degree 3—not dimensionless—contradicting the paragraph’s dimensional argument. Moreover, since AT ∝ P, the ratio P/AT cancels P identically, contradicting “no cancellation of P occurs.”
- Required fix: Replace Eq. (2) with the dimensionally consistent expression BNL = (10/3) AT/(Σi k_i^3). Keep the surrounding dimensional argument, which then becomes correct, and revise the sentence to “BNL retains its dependence on the coefficients through AT (which is linear in P).” Audit Fig. 1 and Table I to ensure they were computed with the correct formula; if code used the correct form, state explicitly that the printed Eq. (2) was a sign/inversion error and that all numerics used the corrected expression.

P2-E2 (Sec. VI.C, p.10–13; Table II p.12; Table III p.15; Abstract p.1–2; Conclusion p.20): Systematic overstatement of Bayes factors due to normalization error
- Offending text/equation: Eq. (7) B = (fmax−fmin)×L(fobs|f0)/∫_{fmin}^{fmax} L(fobs|f) df. Numerical claims: delta-prior broad-competitor BF ≈ 17 (σ=0.7); delta-prior narrow-competitor BF ≈ 7; σtheory=1.0 broad-competitor BF ≈ 9.8; σtheory=1.0 narrow-competitor BF ≈ 4.0; abstract envelope “BF ∼ 10–17”.
- Problem: For a flat competitor prior of width W = fmax−fmin, the model evidence is (1/W)∫ L df. The Bayes factor should therefore be B = L(f0)/[(1/W)∫ L df] = W × L/∫ L (which is what Eq. (7) encodes algebraically). Evaluated at the central case fobs = f0 and W ≫ σ, ∫ L df ≈ √(2π)σ and L(f0) = 1/(√(2π)σ), giving B = W/(2π σ^2). The central numbers reported throughout instead match Bwrong = W/(√(2π) σ), i.e., as if the denominator integral were erroneously set to 1 rather than √(2π)σ. For SPHEREx σ=0.7 and W=30 (broad [−15,+15]) the correct B is 30/(2π·0.49) ≈ 9.75, not 17.1; for W=10 (narrow [−5,+5]) the correct B is 3.25, not 7.0. Likewise, for a Gaussian bounce prior with σtheory, the correct closed form is B = W/[2π σ √(σ^2+σtheory^2)], giving ~5.6 (not 9.8) for σtheory=1.0, W=30, σ=0.7.
- Required fix: (i) Explicitly write the competitor model evidence as (1/W)∫ L df and derive the closed-form expressions. (ii) Recompute all Bayes factors and their envelopes in the abstract, body, and tables with the correct normalization, including the “template-mismatch bookkeeping” variants. (iii) Update all dependent textual conclusions (e.g., “BF ∼ 10–17” becomes ~6–10 for the broad-competitor column at σ=0.7; the narrow-competitor column becomes ~2–4 depending on the bounce prior). (iv) Where realizations are used, confirm that the code uses the normalized competitor evidence; otherwise, regenerate all Monte Carlo validations. (v) State clearly that the bounce-vs-SSFSR Bayes factors (point vs point) are unaffected by this correction; re-check Table III numerical values accordingly.

P2-E3 (Multiple places, e.g., p.10–11, p.13, p.15, p.18–19): Version-history and correction notes embedded in the main text
- Offending text: Several “Correction note: an earlier version …” annotations (e.g., reversed QSFI endpoints, replaced Bayes-factor numbers, etc.), and internal statements about “values … could not be reproduced” and “are replaced here by … recompute.”
- Problem: PRD articles should not contain version-history commentary or internal audit trail notes in the main body. These disrupt the scholarly narrative and are inappropriate for archival publication.
- Required fix: Remove all version-history/correction annotations from the main text. If essential for transparency, consolidate such commentary in a short endnote or an arXiv ancillary document. In the PRD paper, present only the final, correct statements, with a concise methodological description sufficient for reproduction.

P2-E4 (Sec. IV, p.9; Sec. VIII.A, p.16–17): Comparability of σ and detection significances from different estimators/weightings
- Offending juxtaposition: The paper places side by side the CMB-Fisher “signal-only” r=0.876 and LSS/SPHEREx-noise-weighted r≈0.83, and uses a KSW-like flat-sky injection-recovery to “confirm” r≈0.90 ± 0.01, flowing into detection significances.
- Problem: Although caveats are often given, at several points the text presents these σ or r-derived significances in immediate juxtaposition without an explicit “not directly comparable” warning at that location. Per the instructions, such juxtapositions must be clearly flagged each time.
- Required fix: At every location where σ- or r-derived significances from different pipelines/weightings are placed adjacent (e.g., “5.5σ (CMB-Fisher) vs 5.2σ (LSS-noise) vs 5.2–5.5σ headline”), add an explicit reminder that these are not directly comparable estimators/weightings, and specify which one underwrites the headline claim used for SPHEREx.

MAJOR

P2-M1 (Sec. VII.B, p.14): bϕ prior impact on SPHEREx bispectrum forecast not sufficiently quantified
- Offending text: “If the universality assumption is relaxed and bϕ is marginalized independently per tracer bin… σ(fNL) widens by O(20–50%) … headline 5.2–5.5σ … degrades to ~4.0–4.2σ (30%) and ~3.5–3.7σ (50%).”
- Problem: No explicit Fisher matrix or algebra is provided for how bϕ marginalization propagates in the bispectrum channel (as opposed to SDB). The cited cross-term fNL bϕ b1^2 P P is plausible, but the 20–50% degradation claims require an explicit setup to be reproducible.
- Required fix: Provide the exact Fisher setup (parameters, priors, triangle weighting, redshift binning, and covariance assumptions) used to obtain the 20–50% degradation and the 4.0–4.2σ / 3.5–3.7σ figures, or move these numbers to a clearly labeled heuristic estimate. If relying on Heinrich et al., state precisely what was altered relative to their baseline and show the delta numerically.

P2-M2 (Sec. IV, p.9; Shot-noise caveat): Quantitative degradation estimates for anomaly-selected tracers lack derivation
- Offending text: “simple Poisson estimate gives a ∼15–30% degradation…”
- Problem: No computation is shown. Given that this is used to bound potential gains from anomaly tracers, a concrete derivation is needed.
- Required fix: Provide a short derivation (even order-of-magnitude, but explicit) or move the estimate to a clearly labeled conjectural remark without quantitative percentages.

P2-M3 (Sec. VIII.A, p.16–17): Planck recast central value
- Offending text: “Recasting … with the CMB Fisher template mismatch factor r = 0.876 gives f_bounce = −0.1 ± 5.7… 0.75σ from the bounce prediction (|−4.375 + 0.1|/5.71).”
- Problem: Under Eq. (5) bookkeeping, both the mean and the uncertainty scale when recasting a local-template measurement to a bounce-amplitude inference: f_bounce = f_local/r and σ_bounce = σ_local/r. The central value should be ~−0.114 rather than −0.1 (numerically negligible here, but the method should be consistent).
- Required fix: State the recast as −0.114 ± 5.71 (rounded as desired) and compute the distance to −4.375 accordingly. Add a one-sentence reminder that the CMB-weighted r is the appropriate choice for Planck.

P2-M4 (Sec. VII.D, p.16): Photometric-z outlier impact claim
- Offending text: “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼5% (from 0.70 to 0.74)…”
- Problem: No explicit modeling of the outlier-induced bispectrum contamination is provided. A 5% claim needs either a calculation or an explicit statement that this is a back-of-the-envelope heuristic with assumptions.
- Required fix: Provide a short calculation (e.g., additive white noise model on the bispectrum covariance and its Fisher impact) or soften to a qualitative statement without precise percentages.

P2-M5 (Sec. IX.D, p.18–19): Joint (fNL, nfNL) SDB Fisher — reproducibility and separation from bispectrum results
- Offending text: Numerical results are quoted (σ(nfNL)=0.295/0.596, σmarg(fNL)=3.08/7.06, ρ values) and contrasted to the bispectrum-only 0.7 forecast, with a correction note about earlier values.
- Problem: While the section now distinguishes the two Fisher matrices, the SDB-joint Fisher setup (k-range, binning, survey window, marginalization set) needs enough detail for reproduction. Also, the “correction note” must be removed (see P2-E3).
- Required fix: Add a concise methodological paragraph specifying the exact SDB Fisher ingredients and inputs and move any historical correction commentary to the data/code availability or remove it.

P2-M6 (General, multiple pages): Excess references to internal file names and “artifact” tags in the main text
- Offending text: Numerous references like “artifact c9i epsilon ratio check.json”, “c9g bf table recompute.py” within the narrative.
- Problem: While data/code availability is welcome, frequent references to internal filenames clutter the scientific narrative.
- Required fix: Consolidate such references into the Data and Code Availability section or footnotes. In the main text, refer at most to a section and figure/table in the repository (e.g., “see repository Appendix A1 for the symbolic check; link in Data and Code Availability”).

MINOR

P2-ns1 (Sec. II.D, p.6–7): Trispectrum estimate rounding
- Offending text: “τNL = (36/25) fNL^2 ≈ 27.56.”
- Check: (36/25)×(4.375)^2 ≈ 27.58. This is inconsequential but should be consistent.
- Required fix: Use 27.6 or 27.58, or omit excessive precision.

P2-ns2 (Sec. II.A, p.3–5): Notational overload and index usage
- Offending text: Use of “σ” for singular values and statistical uncertainties in close proximity could confuse readers.
- Required fix: Distinguish singular values as s_i or λ_i to avoid confusion with σ for standard deviations.

P2-ns3 (Figures 1–2 captions, p.5 and p.9): Axis labels and units
- Check: Fig. 1 horizontal axis labeled “k1/k” (dimensionless) is fine; Fig. 2 should explicitly label the y-axis as “Detection significance (σ)” and clarify that values are template-corrected local-template forecasts, not direct bounce-template fits.
- Required fix: Update Fig. 2 caption to state explicitly “local-template estimator, template-corrected using r”.

P2-ns4 (Sec. III.B, p.7–8): Squeezed cutoff insensitivity claim
- Offending text: “varying x3,min from 0.001 to 0.200 changes r by < 0.0002”.
- Comment: This is plausible given the weights, but such a tight bound would benefit from a parenthetical note on the adopted k-grid measure and why the bulk of Fisher weight lies away from the extreme squeezed configurations.
- Required fix: Add a short parenthetical rationale (e.g., intermediate/folded configurations dominate mismatch; templates coincide in extreme squeeze).

P2-ns5 (Sec. VIII.B, p.16–17): ns–fNL relation constants
- Offending text: “ns = 8ϵ−11.”
- Comment: Correct as written given the definitions; consider reminding readers of the normalization ϵ = 3(1+w)/2 to avoid confusion with slow-roll ϵSR.

NIT

P2-N1 (Throughout): Em dashes and overuse of parentheses
- Suggested fix: Where possible, break very long sentences containing multiple em dashes into two sentences for readability.

P2-N2 (References): Ensure all references have consistent styles (journal, year). E.g., Ref. [27] “JCAP arXiv:1712.09998” should include volume/page if available or be marked as arXiv e-print consistently.

P2-N3 (Data and Code Availability, p.20–21): Consider shortening the list of individual file names and point instead to a single README that enumerates them; keep the paper focused.

Length
The paper is 24 pages. Given the methodological breadth (bispectrum normalization audit; template mismatch quantification; Fisher recasts; Bayes-factor comparison), this length can be justified. After removal of version-history notes, tightening of code-file references, and consolidation of some repetitive caveats, the main text could be shortened by ~2–3 pages without loss of content.

Internal arithmetic spot-checks (selected)
- |f_bounce|/|f_inf| = 4.375/0.015 ≈ 291.7 (rounded “≈ 290”) — OK.
- Naive SPHEREx bispectrum significance: 4.375/0.7 = 6.25 — OK.
- Template-corrected: r=0.83 → 4.375*0.83/0.7 = 5.19 (“5.2σ”); r=0.876 → 5.48 (“5.5σ”) — OK.
- Li et al. −35/16 case: r=0.83 → 2.19*0.83/0.7 = 2.59 (“~2.6σ”); r=0.876 → 2.74 (“~2.75σ”) — OK.
- Planck PR4 recast σ: 5.0/0.876=5.71 (“±5.7”) — OK; mean should be scaled as well (see P2-M3).
- 8% reduction floor: 0.92×5.2=4.78 (“~4.8σ”) — OK.
- τNL baseline: (36/25) fNL^2 ≈ 27.6 — see P2-ns1.
- Joint-SDB covariance identity check: 1.53/√(1−0.87^2)=3.10 vs quoted 3.08 — OK within rounding.

Novelty/claims
The “first quantification” of the matter-bounce vs local-template mismatch appears plausible; I am not aware of a prior dedicated overlap analysis for this specific bounce shape. The text should remain cautious (“to our knowledge”) and perhaps add a brief literature scan statement.

## Summary recommendation
MAJOR REVISIONS

The Bayes factor normalization error materially impacts the headline Bayesian discrimination claims and requires a full recalculation with corrected formulas. The dimensionally inconsistent Eq. (2) must be corrected, and all places relying on it audited. Version-history notes should be removed from the main text. Several systematic-degradation percentages need either derivations or softening. After these essential and major fixes, the paper could meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (fresh-eyes)

P2-E5 (Sec. VII.C, Table III; Abstract/Systematics prose): GR-degradation percentage is internally inconsistent with the σeff model used
- Claim: “σGR = 0.5 corresponds to a ∼15% degradation” (text).
- Model used: σeff = √(0.7^2 + σGR^2). For σGR = 0.5, σeff = 0.860 ⇒ degradation in σ is 0.860/0.700 ≈ 1.229, i.e., +22.9%, not 15%. For σGR = 1.0, σeff = 1.22 ⇒ +74% in σ.
- Evidence: Table III “BF vs SSFSR” values match σeff = 0.86 (σGR = 0.5) and 1.22 (σGR = 1.0), so the table used the quadrature model. The % figures in text do not match that model.
- Required fix: Either (i) revise the quoted % degradations to match σeff = √(σ0^2 + σGR^2), or (ii) adopt a degradation parameterization that truly yields 10–30% and use it consistently in both the text and tables. State explicitly how σGR maps to σ degradation and why that mapping is justified by Jolicoeur et al.

P2-E6 (Sec. III.A, Eqs. 3–4): Units/h-factor inconsistency in M(k, z) given k is “quoted in h Mpc−1 throughout”
- Issue: M(k, z) = 2 k^2 T(k) D(z) / [3 Ωm H0^2] is standard only if k is in Mpc−1. If k is in h Mpc−1, an extra factor h−2 is implicit. As written, Δb(k, z) acquires a hidden h-dependence.
- Required fix: Specify the unit convention used in the code and formulas (e.g., “k in Mpc−1, not h Mpc−1” or include an explicit h−2 factor). State how this choice was handled in all Fisher computations.

P2-E7 (Sec. VII.C, Table III, “Corrected (10% residual)” row): Ambiguous/unsupported mapping of “10% residual” to σeff
- Claim: “Corrected (10% residual; = Ideal, verification only)” produces the same BF as the “Ideal” case.
- Problem: Under σeff = √(σ0^2 + σGR^2), a “10% residual” in GR contamination should map to a nonzero σGR and hence a non-ideal σeff. The text does not define “10% of what” or how it yields σGR ≈ 0.
- Required fix: Define precisely how “10% residual” translates to σGR (or to σeff), and recompute the row accordingly. If this is a bookkeeping placeholder, label it as such and remove it from the main comparison.

P2-M7 (Sec. III.B, weighting schemes): Ambiguous “CMB Fisher, w ∝ k^2” description without a derivation
- Issue: The statement that a “CMB Fisher” weighting corresponds to w ∝ k^2 (in 3D k-space) is nonstandard and risks confusing readers, since CMB bispectrum Fisher weights live in ℓ-space with Cℓ-dependent weights.
- Required fix: Either remove “w ∝ k^2” (keep only the ℓ-space validation you already provide) or add a short derivation/justification showing how this k^2 weighting approximates the ℓ-space Fisher inner product used in your CMB validation.

P2-M8 (Abstract/Sec. II C vs. Appendix A.1): Over-claim on “establishing” Cai’s −35/8 by symbolic verification
- Claim: “Appendix A establishes that the Cai convention is correct…”, “we verify symbolically… Eqs. 34–36 are exactly half the full result.”
- Issue: Appendix A.1 shows the general identity i⟨[Q, H]⟩ = −2 Im⟨QH⟩ (correct), but it does not explicitly demonstrate that Cai’s specific Eqs. (34–36) are the single-ordering piece nor that their Eq. (37) already includes the second ordering. That mapping is asserted, not shown.
- Required fix: Either (i) add a concrete term-by-term demonstration (even schematic) that links Cai’s printed intermediate and full expressions through the −2 Im doubling, or (ii) soften the language to “consistent with” rather than “establishes,” making clear you are relying on the general in-in identity plus benchmark checks.

P2-M9 (Sec. III.B): “0 < r ≤ 1 holds strictly for canonical single-field…” stated without citation or proof
- Issue: The monotonicity bound on r is presented as “canonical,” but no reference or proof is provided, and you immediately allow r > 1 for some bounce-coefficient realizations.
- Required fix: Provide a citation or a short proof for the r ≤ 1 claim in the canonical single-field/local context, or rephrase as a heuristic expectation rather than a strict inequality.

P2-M10 (Fig. 5, text vs. graphic thresholds): Possible mismatch between plotted “3σ, 5σ thresholds” and text values
- Issue: The caption indicates “3σ” and “5σ” decision thresholds in the right panel. The text states SPHEREx bispectrum stays at ∼5σ optimistic, ∼3–4σ with GR degradation. Without explicit y-axis ticks, it is unclear if the plotted SPHEREx curve aligns numerically with ~5 and ~3–4 after the assumed degradations.
- Required fix: Add y-axis ticks/labels in Fig. 5 and confirm the plotted curves correspond to the numerical claims in the text (e.g., annotate representative points). If not, correct the figure or revise the text.

P2-M11 (Sec. IV, injection–recovery paragraph): Inconsistent noise description
- Issue: The injection–recovery is described as using “SPHEREx photometric-z power spectra as the diagonal noise covariance” and also as “isotropic Gaussian noise (effectively CMB-like weighting).” These two statements are inconsistent; the former implies a redshift- and scale-dependent covariance distinct from CMB weighting.
- Required fix: Clarify exactly what covariance you used in the injection–recovery test. If it is diagonal but z- and k-dependent per SPHEREx, explain why this is “effectively CMB-like,” or remove that phrase.

P2-M12 (Sec. IV, Fig. 2 caption/body consistency): Headline point vs. range needs a local warning on non-comparability
- Issue: Fig. 2 aggregates optimistic (CMB-Fisher r) and conservative (LSS-noise r plus GR/bϕ) endpoints. In multiple places in Sec. IV the 5.5σ vs 5.2σ vs 3.0σ numbers are placed side by side without an immediate “not directly comparable” flag.
- Required fix: Add in-figure or immediate-text qualifiers that the optimistic endpoint uses CMB-like weighting (validation-only), while the headline SPHEREx claim is based on the LSS-noise-weighted bispectrum Fisher with template correction.

P2-M13 (Sec. VIII.B): nfNL = 0 claim lacks a short derivation or reference for the quasi-dust bounce
- Issue: The text asserts nfNL = 0 at leading order. Given the emphasis on (fNL, nfNL) joint forecasting, a one-sentence derivation or citation is warranted.
- Required fix: Cite the specific result (or add a two-line derivation) showing that in quasi-dust contraction the squeezed-limit amplitude has vanishing scale dependence at leading order.

P2-J1 (Abstract vs. Sec. IX.C): Inconsistent “pre-systematics” minimum significance
- Abstract: “5.2–5.5σ… (the ε-correction enters the systematic budget… would lower the pre-budget floor to ∼4.8σ).”
- Sec. IX.C: “a SPHEREx null… excludes… at 5.1–5.5σ before GR and bϕ degradation.”
- Issue: The lower endpoint is 5.2σ elsewhere (r = 0.83). “5.1σ” appears only here and is not supported by the stated r range. If the 5.1 comes from a different r or an extra correction, it should be stated.
- Required fix: Harmonize the lower bound (5.2σ if r = 0.83), or explicitly justify a 5.1σ floor with the exact inputs used.

P2-G1 (Novelty): “first quantification” of the bounce–local template mismatch is not buttressed by a targeted literature scan
- Issue: The “to our knowledge” qualifier helps, but for a “first” claim, a 1–2 sentence scan citing the most closely related overlap/mismatch studies (even if for other non-local shapes) strengthens the claim.
- Required fix: Add a brief literature-scan paragraph (or footnote) justifying that no prior work quantified the bounce-vs-local overlap r for the Cai et al. shape.

P2-ns6 (Sec. III.B, squeezed cutoff insensitivity): Add a compact rationale
- You quote “varying x3,min from 0.001 to 0.200 changes r by < 2×10−4.” Provide a parenthetical note that Fisher weight is dominated by intermediate/folded configurations where the templates differ, while extreme squeezed triangles contribute little mismatch weight because the shapes coincide there.

P2-ns7 (Sec. II.A, notation): P(k1, k2, k3) used for both a polynomial and (elsewhere) power spectra Pζ, PΦ
- Issue: Although you say “three-argument P denotes the polynomial,” the dual use is easy to misread.
- Fix: Consider renaming the polynomial (e.g., 𝒫 or Q) to avoid confusion with Pζ and PΦ.

P2-ns8 (App. A.1, A.7): Suppressed (2π)3 δ(Σk) factors
- Issue: The bispectrum expressions omit the momentum-conserving delta. Readers will assume it’s suppressed, but since you discuss normalizations, add a one-line note that (2π)3 δD(k1+k2+k3) is suppressed throughout.

Explanation
The first-pass review focused mainly on the Bayes-factor normalization error and the BNL inversion/dimensional issue. The fresh pass identified additional internal inconsistencies (GR-degradation mapping), a units/h-convention ambiguity in the SDB kernel, several over-assertions needing either derivations or softened language (in-in “establishes,” nfNL = 0), and clarity gaps (weighting descriptions, figure numeric alignment, injection–recovery noise). These corrections improve methodological rigor and traceability expected for PRD.