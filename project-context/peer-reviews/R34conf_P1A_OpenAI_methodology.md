# P1A R34conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.62.pdf` md5=9a1a725b pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9284 chars)
**Wall time**: 642.7s

---

Referee report for Physical Review D (methodology-focused)

Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes …”

Overall scope
The paper aims to provide a channel-level no-go for four “minimal ECH” dark-energy routes, anchored by a perturbation-transparency statement (Holst sector decouples for canonical scalar matter) and a barrier catalog. The authors explicitly label many steps as ansatz-level rather than derived.

As a methodology referee, I focused on dimensional analysis, internal arithmetic, estimator definitions, significance accounting, and the “standalone-reader” and reproducibility criteria. Below are all findings, each with severity, location, problem, and required fix.

ESSENTIAL findings

P1A-E1 (Sec. IV A, p. 11): Catastrophic unit error in number-density conversion and NJL amplitude bound
- Text: “at recombination the baryon/electron number density is nb(z ≃ 1100) ≈ 330 cm−3 ≈ 2.5 × 10−12 eV3, giving ρNJL ∼ n2ψ/M2Pl ≈ 4 × 10−80 eV4 ∼ 10−69 ρΛ”
- Problem: 330 cm−3 ≠ 2.5 × 10−12 eV3. Using ℏ = c = 1, 1 m = 5.067×10^6 eV−1 ⇒ 1 m−3 = (5.067×10^6)^3 eV^3 ≈ 1.30×10^20 eV^3; 1 cm−3 = 10^6 m−3 ⇒ 1.30×10^26 eV^3. Therefore nb ≈ 330×1.30×10^26 ≈ 4.29×10^28 eV^3, not 2.5×10−12 eV^3. The quoted NJL energy density bound is off by ~40 orders of magnitude or more. With the correct conversion, n^2/M^2Pl ≈ (4.29×10^28)^2/(1.22×10^28)^2 eV^4 ≈ O(10) eV^4, which actually exceeds ρΛ ~ 2.8×10^−11 eV^4 by many orders; of course this back-of-envelope is not physically meaningful because ⟨J5⟩→0 in a thermal, unpolarized bath (as you correctly stress elsewhere) and the appropriate correlator is not simply n^2. But as written, the numerical argument is wrong and misleading.
- Required fix: Remove the faulty cm−3→eV^3 conversion and any numerical NJL amplitude statements based on it. If you want a quantitative NJL upper bound, compute the correct thermal expectation of J5μJ5μ (or a rigorous upper bound) in a relevant plasma, and convert with correct units. Otherwise, argue qualitatively (parity-even; algebraic torsion; thermal ⟨J5⟩≈0) without spurious numbers.

P1A-E2 (Abstract; Secs. I, III, V, VII, XIII–XV; Table IV; Data & Code Availability, multiple pages): Standalone-reader failure; load-bearing results rely on “companion papers in preparation” and frozen private chains
- Problem: Critical pieces (ΛCDM+ΔNeff MCMC verification, NaMaster pipeline validation, ALP parameter fitting, galaxy spin classifier performance, PTA reanalysis) are only in “companion works in preparation,” not citable and not reproducible from this manuscript. Table IV lists “Verified Value” from private frozen chains. Figures and narrative depend on these.
- Required fix: For PRD, all load-bearing analyses must be self-contained or in citable, publicly available references (with arXiv IDs/DOIs). Either (a) include full methodological details and results as appendices here (datasets, likelihoods, priors, chains, diagnostics, masks, code versions, burn-in, thinning), or (b) defer all such claims and remove quantitative values imported from non-public work. Table IV must not list “verified values” sourced solely from in-prep companions.

P1A-E3 (Throughout; e.g., title page, p. 1; footnote a p. 2; Sec. X D footnote 7 p. 19; Data & Code Availability p. 24): Version-history and internal bookkeeping language in the paper
- Text examples: “(Dated: June 11, 2026 PDT — v1A.0.62)”; “Earlier versions of this manuscript erroneously…”; “bundle v1A.0.59-bundle (resynced 2026-06-10)…text-only restamp…”
- Problem: PRD forbids version-history, internal revision logs, and self-auditing prose within the published article.
- Required fix: Remove all references to version tags, bundles, “earlier versions,” resync notes, and similar internal workflow comments from the body, captions, footnotes, and data-availability text.

P1A-E4 (Sec. IV B, pp. 11–12; Eq. (14)–(15)): Incomplete derivation chain for one-loop “parity-odd” route and dimension handling to birefringence estimate
- Problem: The R2 mapping uses an ansatz Γ ⊃ (1/16π^2) β(γ) MPl ∫ √−g ∂μϑNY J5μ, then infers a birefringence level via the anomaly ∂μ J5μ ⊃ (αem/4π)F F̃. As written, the steps from ∂μϑNY J5μ to a CMB-scale rotation angle (including the role of MPl and the time integral) are not fully specified. Equation (15) mixes dimensionful and dimensionless quantities and then “restores” a 1/MPl to produce a “dimensionless ratio”; this leaves room for hidden factors and is not reproducible.
- Required fix: Provide a complete, explicit chain:
  - Define the effective action/operator basis rigorously (with coefficients and dimensions).
  - Show how it induces a photon dispersion relation and a net rotation angle, stating all assumptions (homogeneity, WKB expansion, integration limits, background evolution).
  - Present a clean, dimensionally-consistent formula for Δθ in terms of αem, H0, MPl, and any fitted parameters, with no “alternative orderings” ambiguity.
  - If the only robust statement is an upper bound, state it as such and remove claims of precise O(10^−60) suppression unless derived unambiguously.

P1A-E5 (Sec. I, Abstract, Sec. XII A, Appendix B): Heavy reliance on an acknowledged non-EFT “on-shell scaling ansatz” for the central DE mapping
- Problem: The mapping ρΛ ∼ [(α/M)MPl] M^4Pl × Dinf is explicitly non-EFT (operator dim +1 off-shell, Appendix B), yet used repeatedly to set Ntot ≈ 92 and to support high-level claims. While you acknowledge this is an ansatz, the abstract and conclusions prominently feature the Ntot value and dilution narrative as if quantitatively tied to ECH.
- Required fix: Either (a) provide a controlled EFT operator of correct mass dimension with a fully specified coupling (including MPl powers) and carry through the derivation, or (b) move all Ntot ≈ 92 quantitative conclusions to a clearly labeled, non-load-bearing “phenomenological scenario” subsection, and strip them from the abstract and conclusions. The perturbation-transparency result can stand independently without the ansatz; the Ntot numerics should not headline the paper unless derived.

P1A-E6 (Sec. I A a., p. 3; multiple places): Operator-basis omissions undermine the claim of closure unless explicitly bounded
- Problem: You exclude key parity-odd/torsionful operators (Jackiw–Pi R∧R̃, parity-odd four-fermion partner) from the enumerated routes yet still headline “channel-level closure.” The abstract/conclusions state closure of “four enumerated minimal-ECH routes” but the text risks readers interpreting this as broader than warranted.
- Required fix: In the abstract and conclusions, explicitly add a one-sentence limitation that the closure pertains only to the four explicitly enumerated channels, with the operator-basis closure deferred, and that additional diffeomorphism-invariant parity-odd operators (list them) are not treated here. Also add, in Sec. IV, quantitative upper bounds or sharp reasons why the omitted operators are unlikely to rescue the mechanism, or mark this as an open item.

P1A-E7 (Fig. 4 p. 15; Fig. 6 p. 21; Sec. VII p. 14; Sec. XIII p. 22): Significance claims for SPHEREx fNL rely on external forecasts and “companion” work; not directly comparable σ are juxtaposed without in-text warnings at each juxtaposition
- Problem: You present 2.6–5σ “realistic” SPHEREx forecasts for fNL = −35/8 and compare to inflation/Cuscuton, drawing inferences. These numbers are borrowed (Heinrich et al. 2024) and from your own “companion” forecasts. The figures combine curves without an explicit, local warning that they are forecasts under different null procedures and systematics.
- Required fix: At every instance where σ from different procedures/sources are shown together, insert an in-figure caption caveat: “Forecasted σ values under distinct null procedures; not directly comparable to current data significances.” Also remove any novel quantitative claims not reproduced in this paper or provide the full Fisher pipeline details here.

P1A-E8 (Sec. I, Abstract; Sec. III B; Sec. V; Ref. [23]): Galaxy-spin “confirmed null” depends on an in-prep companion; not reproducible here
- Problem: You state a “confirmed null” with p-values and sample sizes, but the methods/results are deferred to a companion “in preparation.” This violates the standalone-reader standard.
- Required fix: Either include a methods appendix summarizing the classifier architecture, training set, selection, bias audits, sky mask, validation accuracy, and the exact dipole estimator and null distribution with numerical results, or remove the claim. A mere pointer to an in-prep paper is not sufficient.

P1A-E9 (Data & Code Availability, p. 24): Reproducibility surface incomplete and contains version-history text; no frozen DOI/commit hash recorded for the exact artifacts
- Problem: The GitHub link is provided but the text uses bundle labels (v1A.0.59) and “text-only restamp” language; there is no explicit tag/commit hash in the manuscript ensuring reproducibility. The “frozen MCMC chains” are said to be included, but without hashes, checksums, or a DOI.
- Required fix: Provide a precise repository tag or commit hash, Zenodo/DOI archival links for code and data, and SHA256 checksums for frozen chains. Remove version-history language from the section. State explicit instructions to reproduce any numbers that remain in the paper.

P1A-E10 (Sec. X B–D, pp. 18–19): Perturbation-transparency “proof” is a sketch; lacks a full variational treatment
- Problem: The argument relies on “torsion vanishes ⇒ Levi-Civita ⇒ εR = 0 by Bianchi” without presenting the perturbation action and a proper variation showing vanishing contributions to all orders for scalar and tensor sectors. As a methodology paper hinging on this theorem, a complete derivation or a precise literature reference is required.
- Required fix: Provide a rigorous derivation: write the action to the relevant order, set T=0, vary with respect to perturbations, and show the Holst sector contributes zero to the EOM for scalar and tensor modes at all orders. Alternatively, cite a standard reference proving εR(˚Γ)=0 contributes no dynamics, with clear conditions. Include caveats (non-metricity, boundary terms) precisely.

MAJOR findings

P1A-M1 (Eq. (1), p. 5 and footnote): Inconsistent action writing: include TabcTabc under 1/(16πG) and then assert it is “not varied independently”
- Problem: The displayed action S_ECH places T·T inside the gravitational prefactor, but the footnote says it is “a shorthand … not varied independently.” Mixing pre- and post-elimination forms in a single action is confusing and methodologically brittle.
- Required fix: Present one of the following cleanly: (a) the bare Einstein–Cartan–Holst+Dirac action, then eliminate torsion to get the effective four-fermion term; or (b) the already-reduced effective action with the four-fermion operator and no T·T term. Do not include T·T in the varied action if it is not varied.

P1A-M2 (Sec. IV D, p. 12–14; Appendix C): ALP coupling normalization and basis-conversion footnote
- Problem: You discuss α/M versus gaγ with caveats about 1/(4π) vs 1/(2π) conventions and “10× gap.” The text is convoluted and risks misinterpretation.
- Required fix: In one place (preferably Appendix C), define the two normalizations explicitly, give the exact conversion formula with cγ, fa, and show a worked numeric example that recovers α/M = 10^−21 GeV−1 from a chosen gaγ, fa, cγ. Remove narrative ambiguity from the main text.

P1A-M3 (Sec. IV B footnote 3, p. 11): “Parity-odd” labeling vs operator parity
- Problem: You label the operator “parity-odd” while noting ∂μϑNY J5μ is actually parity-even; the parity breaking is through background evolution. This inconsistency can confuse readers.
- Required fix: Relabel the route/operator consistently as “parity-violating phenomenology via a P-odd background,” and avoid calling the operator itself parity-odd.

P1A-M4 (Fig. 5 top panel, p. 17): RG running plot without a stated β-function or calculation details
- Problem: The “Renormalization Group Running of α/M” figure has axes and a curve but no equation, no scheme, no input values beyond a “primordial benchmark.” It is not reproducible.
- Required fix: Either (a) provide the β-function and the integration used to generate the curve (with uncertainties), or (b) remove the plot and keep only a qualitative statement that running is expected to be slow.

P1A-M5 (Sec. XII A; Appendix B): Ntot ≈ 92/94 conflicting values and dependence on the non-EFT ansatz; inconsistent presentation
- Problem: Two different Ntot values (≈92 and ≈94) are presented. While you explain the difference, the abstract and conclusions cite 92 prominently, blurring that this hinges on a non-EFT rescaling by 10^−2.
- Required fix: Choose one consistent presentation (e.g., Ntot ≈ 94 from the true hierarchy, and separately note that using the on-shell ansatz shifts it by ~2%). Move both numbers to a single subsection and remove 92 from the abstract.

P1A-M6 (Fig. 3 caption, p. 7): “Rotation contribution … is a distinct and negligible term” claim is fine numerically but requires a direct citation for (ω/H) bound and a clear unit normalization
- Problem: You cite Saadeh et al. for (ω/H)0 < 5 × 10^−11. You then say it is “∼ 1.2 × 10^−21 of ρΛ.” The arithmetic is fine: (ω/H)^2/(3ΩΛ) ~ 2.5e−21/2.1 ≈ 1.2e−21. But you should state the model dependence (Bianchi type, isotropization assumptions).
- Required fix: Add 1–2 sentences (or a footnote) specifying the cosmological model assumptions behind using (ω/H)0 as an isotropic Λ surrogate, and that the entry is only a bookkeeping bound.

P1A-M7 (Sec. XI, p. 20): “Hybrid DE loophole” lists seven disguised forms but provides no quantitative test
- Problem: The section enumerates possibilities but presents neither equations nor constraints, yet the narrative implies they are excluded or equivalent to ΛCDM+w0wa.
- Required fix: Either provide a compact quantitative test (even at the level of degrees-of-freedom counting and Akaike/Bayes penalties), or move this section to brief discussion as speculative.

P1A-M8 (Bibliography; multiple entries): Several in-prep or year-forward citations
- Problem: Some references (e.g., [5], [37]) are labeled with 2025 dates or “arXiv preprint” without published metadata; [6], [23], [46] are “companion papers” without arXiv identifiers in this manuscript.
- Required fix: Ensure all load-bearing citations have accessible arXiv IDs and that their results are not critical for claims in this paper. If a ref is not publicly available, remove any reliance on it.

MINOR findings

P1A-m1 (PACS numbers, p. 2): PACS are deprecated
- Fix: Remove PACS or replace with modern keywords.

P1A-m2 (Typos/notation): “Domaga la” spacing (p. 6), “R Re” vs “R∧R̃” typographical inconsistency (pp. 2, 19), “Nieh–Yan” consistently hyphenated; “ALP” acronym defined once
- Fix: Clean up orthography and maintain consistent notation (Pontryagin density R∧R̃; use tilde consistently).

P1A-m3 (Sec. II A 2 Footnote 2, p. 6): Overlong footnote mixing conventions
- Fix: Move the convention choice and Sabc back-substitution to an appendix for readability.

P1A-m4 (Fig. 1, p. 5; Fig. 4, p. 15; Fig. 6, p. 21): Programmatic “decision timeline” and “mechanism map” look like roadmap figures, not methods/results
- Fix: Consider removing or moving to supplementary material to streamline the methods paper.

P1A-m5 (Acknowledgments, p. 24): AI-assistant acknowledgment is acceptable, but policy may require declaring that no text was generated without author verification
- Fix: Ensure compliance with PRD policy; otherwise no change needed.

P1A-m6 (Effect-size context per journal guidelines): Where you quote σ, also give fractional amplitude or practical effect size. You do this for β and ∆H/H; maintain consistently.
- Fix: For all σ statements retained, add fractional amplitudes or relevant observable magnitudes.

NIT findings

P1A-n1: Several long sentences could be tightened. No scientific change required.
P1A-n2: Ensure all axes in figures carry units explicitly (H(z) already has km s−1 Mpc−1; check all figures).
P1A-n3: Ensure consistent use of reduced vs unreduced MPl; you note it, but re-affirm once in Appendix B.

Abstract-last drift sweep (pattern-045)
- The abstract’s strongest claims (channel-level closure of four enumerated routes; perturbation-transparency; R4 closed by naturalness; Ntot ≈ 92) are broadly mirrored in the body with caveats. However:
  - The Ntot headline is not derived from a controlled EFT operator; per P1A-E5, this must be softened in the abstract or the derivation supplied.
  - The galaxy-spin “confirmed null” is cited in the body as relying on a companion; the abstract’s positioning of it as part of the program is acceptable, but any definitive wording must be removed unless reproducible here.
  - The “14 constraints, 13 independent” claim is consistent with Table II, but several barriers (e.g., B12) are admitted ceiling ansätze. Add “under stated assumptions and ansätze” in the abstract line that introduces the catalog.

Effect-size/statistical accounting
- β comparison WMAP+Planck vs ACT: your 1.06σ difference is computed correctly: 0.127° / sqrt(0.094^2 + 0.074^2) ≈ 1.06.
- LiteBIRD 9σ from 0.27°/0.03° is a naive SNR; you correctly later warn that model discrimination vs 0.342° is only ~0.7σ; keep both caveats co-located wherever 9σ is mentioned.
- fNL significance: ensure every time you quote σ numbers they are labeled “forecast,” with references and not mixed with measured significance.

Dimensional-analysis spot checks
- Eq. (7) leading to [(α/M)MPl] ≈ 3×10^−3 numerically checks out with M = MPl/√γ and ln(ΛUV^2/μ^2) ≈ 74.
- Eq. (10): Λeff = Ξ M^2Pl + cω ω^2; units consistent if ω has units of H (mass).
- Appendix C derivation of 2β = (α/M)Δϕ is correct with WKB and homogeneous θ assumptions.

Length and focus
- The manuscript is long (28 pages) relative to the core contribution (perturbation-transparency + four-route audit). If the essential fixes above are addressed, I recommend reducing the main text to ~15 pages by moving programmatic sections (observational roadmaps, decision timelines, hybrid-loophole enumerations) to appendices or removing them.

## Summary recommendation
MAJOR REVISIONS

The paper contains a substantive and potentially publishable core (the perturbation-transparency statement for canonical scalar matter and a careful channel-by-channel audit), but it currently fails PRD methodology standards on several fronts: a fatal unit error in Sec. IV A; heavy dependence on non-public “companion” analyses for load-bearing claims; incomplete derivation chains (R2 mapping) and overreliance on a non-EFT ansatz for Ntot; and extensive version-history/internal-bookkeeping text embedded in the manuscript. If the authors correct the unit error, remove or fully include methods for all companion-dependent claims, present a rigorous derivation for the transparency result and a clean, dimensionally consistent treatment of the R2 route, and excise revision-log language, the work could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

P1A-E11 (Sec. IV B, Eq. (14)): Dimensional inconsistency in the one-loop operator coefficient
- Text: Γone-loop ⊃ −(1/16π^2) β(γ) MPl ∫ √−g ∂μϑNY J5μ.
- Problem: As written, the coefficient carries mass dimension +1 (MPl), but the integrand ∂μϑNY J5μ has mass dimension +4 and the action must be dimensionless. The narrative below Eq. (14) says the coefficient should scale like (αem/4π)/MPl (one negative power of MPl), not MPl. This is not just a typo: the subsequent ratio in Eq. (15) “restores” a missing 1/MPl, confirming a mismatch between Eq. (14) and the intended counting.
- Required fix: Replace MPl by 1/MPl (or give the full coefficient with explicit dimensions and couplings) and propagate the change consistently through Eq. (15). State the dimension of ϑNY and J5μ explicitly and show the action is dimensionless.

P1A-E12 (Appendix B; Fig. 5; Sec. XII A): Inconsistent size of the Planck-to-ρΛ hierarchy and Planck-mass convention
- Text: “genuine cosmological-constant hierarchy … ∼ 10122”; elsewhere, Fig. 5 shows ΛCDM 10120; body sometimes uses unreduced MPl.
- Problem: Using unreduced MPl = 1.22 × 1019 GeV and ρΛ ≈ (2.3 meV)4 gives M4
Pl/ρΛ ≈ O(10123). Using reduced M̄Pl gives ≈ 10121. The manuscript mixes 10120, 10122 and unreduced-vs-reduced conventions without pinning one choice.
- Required fix: Choose one Planck-mass convention and one headline hierarchy number (e.g., 10121 with M̄Pl, or 10123 with MPl), state it once (Appendix B and main text), and ensure Fig. 5’s bar labels and Sec. XII A align. If you keep 10122, explain the chosen convention and rounding.

P1A-E13 (Fig. 3 and caption; Sec. II C): Non-reproducible H(z) comparison; missing parameter values
- Problem: The ECH curve implicitly fixes Ξ in Λeff = Ξ M2
Pl but no value (or error band) is given; cω and ω/H normalization are also unspecified. Readers cannot reproduce ΔH/HΛCDM without Ξ and cosmology inputs.
- Required fix: Provide the exact Ξ used to draw the orange curve, the baseline cosmology, and explicitly set cω and ω/H0 in the caption. If Ξ is tuned to ρΛ, say so and show the curve is therefore identical to ΛCDM within plotting precision.

P1A-E14 (Sec. X B and D): Incorrect condition attached to the first Bianchi identity
- Text: “the Holst dual contraction … vanishes identically on the Levi-Civita connection (T = 0, metric-compatible) by the first (algebraic) Bianchi identity … and can fail in non-metric connections even when torsion is zero.”
- Problem: The algebraic (first) Bianchi identity Rμ[νρσ] = 0 holds for any torsionless (symmetric) connection, independent of metric compatibility. The qualifier “metric-compatible” is unnecessary and the claim that it “can fail” with non-metricity (but T=0) is generally false.
- Required fix: Remove “metric-compatible” from the condition and the suggestion that the identity can fail in non-metric, torsionless cases. If you intend a different caveat (e.g., for non-Riemannian geometries with torsion), state it precisely.

P1A-E15 (Sec. IV E, “Closure summary” vs Sec. IV A): Internal contradiction about NJL vacuum scale
- Text: Sec. IV A argues ρNJL ≪ ρΛ (after the now-corrected unit conversion, this numerical argument must be removed anyway). Sec. IV E states “The condensate mechanism yields a vacuum energy that is parametrically too large by many orders of magnitude.”
- Problem: These two statements point in opposite directions (“too small” vs “too large”). Even after deleting the faulty recombination-number estimate (per your earlier essential fix), the summary should not contradict the route-specific section.
- Required fix: Make the characterization consistent across sections. If the intended point is “not viable” (for structural reasons: parity-even, thermal ⟨J5⟩ ≈ 0, etc.), state that without “too large/too small” language unless quantitatively supported with a correct calculation.

P1A-M9 (Sec. IV C, Eq. (16) and following): Unsubstantiated Δγ/γ ≈ 10−2 claim
- Problem: The one-loop β-function ansatz for γ-running is presented without derivation or a direct link to a worked-out RG solution, yet the text uses it to state Δγ/γ ∼ 10−2 from the GUT to IR. Benedetti & Speziale are cited generally, but no quantitative bridge is shown.
- Required fix: Supply the explicit β-function used (including matter content), the integration range, and a worked example that yields Δγ/γ ∼ 10−2; or soften to a qualitative statement that any effect will remain Planck-suppressed at late times, without a numeric claim.

P1A-M10 (Appendix C; Fig. C-logic): WKB smallness estimate missing the scale factor in ϕ′ for homogeneous rolling
- Problem: You estimate (α/M)ϕ′ ∼ (α/M) fa H0 and compare to k ∼ 150 GHz, concluding a ~31-order hierarchy. For a homogeneous field in FRW, ϕ′ = a ˙ϕ; your text invokes conformal invariance for Maxwell, but the comparison k ≫ (α/M)ϕ′ is done in conformal variables. If you use conformal time, the relevant smallness parameter is (α/M)ϕ′/k with both quantities in conformal units; if you use cosmic time, show the appropriate mapping.
- Required fix: Add one line clarifying the time variable and include (or justify neglecting) factors of a in ϕ′ when forming ω± ≃ k ∓ ½(α/M)ϕ′. The numerical hierarchy will remain huge, but the normalization must be internally consistent.

P1A-M11 (Fig. 5 bottom; Sec. XII A): “Fine-tuning score” bars lack definitions/citations
- Problem: Bars labeled 1060 (quintessence) and 1040 (f(R)) are presented without a definition of the metric (exactly what “orders of magnitude” measure?) or a source.
- Required fix: Define the scoring rule (e.g., prior volume fraction, mass scale ratio, or parameter cancellations) and provide citations or a short derivation. Otherwise remove the bars and retain qualitative text.

P1A-M12 (Sec. III A, Eq. (12) and narrative): Mixed-use of small-angle EB formula and estimator practice
- Problem: You display CℓEB ≈ 2β(CEE
ℓ − CBB
ℓ) (small-angle, uniform β) but then note modern β estimators include lensing BB and do not use this back-of-envelope. This can mislead readers into thinking Eq. (12) underlies your quoted β values.
- Required fix: Add a one-sentence clarification immediately after Eq. (12): “We do not use Eq. (12) for any numerical inference; quoted β values come from the published estimators in [3–5].”

P1A-M13 (Sec. II A 2, Eq. (7)): Use of αem at low-energy value without scale mention
- Problem: You take g2 = 4παem ≈ 0.092 with αem ≈ 1/137; at the electroweak/GUT scales αem ≈ 1/128–1/127. While this is order-of-magnitude, the text presents a specific 3×10−3 outcome.
- Required fix: Add “using αem at low energy; the result varies by O(1) with scale choice.” Or evaluate with αem(MZ) to be consistent.

P1A-M14 (Sec. II C 1, “Reheating thermal-reset” paragraph): Claim requires at least one quantitative rate comparison
- Problem: The conclusion “any coherent axial component is washed out” hinges on Γwash/H > 1 for specific channels; only rough verbal estimates are given.
- Required fix: Provide one explicit numerical ratio (e.g., Γt/H at Treh = 1015 GeV) with the constants used, or rephrase as a conditional: “If Γwash/H > 1 (as expected given …), the coherent component is reset.”

P1A-m7 (Fig. 3 axes/units; Fig. 5 top): Minor clarity items
- Fig. 3: State H(z) baseline parameters in the caption (H0, Ωm, etc.) to lock the axis scaling.
- Fig. 5 top: Add the explicit β-function used to draw the running of α/M in the caption, or remove the curve.

P1A-m8 (Sec. X D, notation): “RH(˚Γ) ≡ ½ εR” is nonstandard symbol
- Problem: RH is introduced without prior definition and is not used elsewhere.
- Required fix: Either drop RH and write the contraction explicitly or define RH once and use it consistently.

P1A-m9 (Sec. II A 2, Step 2, Eq. (4) and surrounding text): Sign/normalization hygiene
- Problem: You write Lint = −(3πGN/2)(γ2/(γ2+1)) J5·J5; earlier you write +¼ Tabc Tabc inside the action but say it is “not varied independently.” This mixture can confuse readers about the origin of the sign.
- Required fix: Tie Eq. (4) to the precise bare action used (no explicit T·T term is varied) and cite the standard derivation equation where the −3κ/16 coefficient appears after eliminating torsion. Cross-reference to footnote 2 or move that derivation to an appendix.

P1A-m10 (Appendix B vs main text): Keep the Ntot ≈ 94 primary value in one place
- Problem: The body uses both 92 and 94, with explanations scattered.
- Required fix: Consolidate the Ntot discussion into Appendix B (single canonical value from the true M4
Pl-to-ρΛ hierarchy) and refer to it from the main text; in the abstract, avoid any single number unless derived from a controlled operator (per your earlier essential fix).

Explanation
The additional issues above were not covered in the initial report and arose from a second-pass focus on dimensional consistency (Eq. 14), internal numerical coherence (Planck hierarchy), figure reproducibility (Fig. 3), a misstatement about the first Bianchi identity, and several clarity/rigor gaps (γ-running size, WKB normalization, fine-tuning bars). Addressing these, in addition to the essential fixes already listed in the first report, will substantially improve methodological rigor and reproducibility.