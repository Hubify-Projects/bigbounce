# P1B R55 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R55_P1B/paper1b_mcmc_companion.pdf` md5=2d80d814 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5256 chars)
**Wall time**: 459.5s

---

Referee report on: “Technical Verification Companion to the ECH Spin‑Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator‑ALP Model” (21 pp)

Scope of review
- Focus: methodology rigor, statistical validity, internal arithmetic consistency, error propagation, clarity of estimator definitions, and reproducibility.
- I audited every quoted scalar in the abstract and conclusions against numbers traceable in the body and checked arithmetic for key statements (σ-distances, ratios, percent differences, conversions, and dimensional consistency).

Overall assessment
- The paper is careful about scope and caveats, and most scalars in the abstract trace to the body with correct arithmetic. However, several issues must be resolved for PRD standards: persistent identifiers for data (DOIs) are missing, some headline σ-distances are reported from an overlap‑uncorrected SN product likelihood, the final ΛCDM+ΔNeff results use a mixed Planck PR4 high‑ℓ with Planck‑2018 low‑ℓ/lensing pairing, and the manuscript contains extensive repository logistics (commit hashes, file paths, internal QA labels) that are not appropriate for the main text of a PRD article. The NaMaster estimator/bias is well documented in the body but should be explicitly identified in the abstract as the “unweighted template-fit” estimator.

Findings

ESSENTIAL (paper cannot be accepted without these)

P1B-E1 (Data availability; p. 17–19)
- Problem: “HuggingFace datasets … DOI assignment is pending.” Multiple in-text references to live GitHub/HF URLs and a moving “version-stamp” commit (b22f8cc9) without a frozen, citable archive.
- Required fix: Provide stable, citable DOIs (e.g., Zenodo or similar) for (i) the frozen MCMC chains supporting Tables I–II, (ii) NaMaster MC artifacts and scripts, and (iii) ALP-MCMC chains and configs. Include the exact commit hash of the code archived under the DOI and a tag/release. The manuscript must cite the DOIs in the Data and Code Availability section.

P1B-E2 (Internal versioning/process text in main article; p. 17–19 and scattered)
- Problem: Main text contains internal version-history language and process logs: “in‑tex v1B.0.76 stamp,” “current snapshot commit: b22f8cc9,” “parameter_summary_CORRECTED.json,” “column-permutation warning,” “overlay artifact reproducibility/…/c13_s8_desy3_overlay.json,” etc.
- Required fix: Move all repository logistics, file paths, and internal QA commentary (column permutation bug, chain-directory layouts, pod names) to a separate Supplementary Material or to the archived README referenced by a DOI. Keep the paper’s main text to scientific content and essential, citable links only.

P1B-E3 (SN overlap systematic vs. quoted σ-distances; pp. 4–6, 12)
- Problem: The w0wa σ-distances (+4.3σ in w0 and −3.6σ in wa) are quoted from a DES‑SN5YR × Pantheon+ product likelihood that the paper explicitly states double-weights ~20% shared SNe and lacks a joint covariance. Although caveats are present, these σ-distances are placed prominently and will be overinterpreted.
- Required fix: Either (a) supply the two overlap‑robust control analyses you mention (DESI+Planck+Pantheon+ only; DESI+Planck+DES‑SN5YR only) and show the (w0,wa) shifts and σ-distances alongside the product‑likelihood results, or (b) remove the σ‑distance numbers from the main text and relegate them to a supplementary diagnostic, replacing them with a qualitative statement of direction with explicit overlap-covariance caveat. In either case, the abstract/conclusions must not foreground σ‑distances based on the overlap‑uncorrected product.

P1B-E4 (Abstract: pre‑declare estimator for pseudo‑Cℓ bias; p. 1)
- Problem: The abstract reports NaMaster recovery “bias” values (−0.032°, −0.040°) without stating that these refer specifically to the unweighted χ² template‑fit estimator. In the body you show the inverse‑variance alternative reduces the bias ≈80%.
- Required fix: Amend the abstract to read “unweighted template‑fit pseudo‑Cℓ pipeline” (or similarly explicit) wherever those bias figures appear, and add one clause indicating that inverse‑variance weighting reduces the bias substantially (details in Sec. IV). This prevents misinterpretation and satisfies “estimator pre‑declaration.”

P1B-E5 (Planck likelihood pairing consistency for headline ΔNeff; pp. 3, 11–12, 16)
- Problem: The frozen ΔNeff results use PR4/NPIPE CamSpec high‑ℓ with Planck‑2018 low‑ℓ TT/EE and lensing. A PR4‑consistent re‑run is presented separately (planck 2020 lollipop.lowlE + planckpr4lensing) and shows 0.04σ agreement, but the headline table keeps the mixed pairing.
- Required fix: For PRD, adopt a single, consistent Planck pairing as the headline result (preferably PR4‑consistent low‑ℓ and lensing) and move the mixed‑pairing result to a robustness check, or show both side‑by‑side in Table I with explicit “release pairing” labels. The abstract should reflect the chosen, consistent pairing.

MAJOR (significant revision required)

P1B-M1 (MC sufficiency demonstration for pipeline bias; p. 8–11, Fig. 3)
- Problem: Bias uncertainties are given as the SE of the 500‑MC mean. No demonstration that N=500 is sufficient (stability of the bias vs. N or across independent seeds) is shown.
- Required fix: Add a short N_MC robustness check (e.g., N=200/500/1000 on one mask) showing the estimated bias and SE converge, or quote an a priori calculation of the target precision and show that 500 realizations meet it for the reported 0.002° SE.

P1B-M2 (Estimator choice and effect on “pipeline floor”; p. 10–11)
- Problem: The concluding phrase “carry forward 0.040° as the observed NaMaster pipeline bias floor” is ambiguous since the bias is estimator‑dependent and falls to 0.006° with inverse‑variance weighting.
- Required fix: Rephrase all instances of “pipeline bias floor” to “unweighted‑estimator pipeline bias” and add the inverse‑variance value (−0.006°) as an alternative recommended estimator in the main text (not only in robustness). Explicitly state that this choice was made to match prior public scripts, not because it is optimal.

P1B-M3 (Presentation style: internal QA/claims classification; pp. 17–20, Table V)
- Problem: The “Claims classification” table and process‑audit prose (e.g., “Int. verified (frozen chains)”) read like internal QA and are not standard for PRD. They dilute the scientific presentation.
- Required fix: Move Table V and related internal auditing notes to Supplementary Material (linked by DOI). Keep the main text focused on methods, results, and essential reproducibility pointers.

P1B-M4 (Notation consistency for ALP mass; multiple pages)
- Problem: The ALP mass is denoted m in the narrative and ma in appendices/equations. This could confuse readers.
- Required fix: Use ma consistently throughout (and define it once at first use). Where m/H0 is used, explicitly state m≡ma.

P1B-M5 (Effect size for CPL background; p. 6)
- Problem: The paper states H(z=0.5) differs by ≈+1.7% from ΛCDM at (w0,wa)=(−0.812,−0.667). No derivation or supporting plot is shown.
- Required fix: Provide a short calculation or figure in the text (or supplemental) showing the percent H(z) difference over 0<z<1 for the posterior mean (and preferably the 68% contour band). This helps contextualize the quoted σ‑distances.

MINOR (address but paper can proceed)

P1B-m1 (Arithmetic checks – all OK; keep explicit statements)
- Verified: 
  - H0 tension 73.04−67.68=5.36; σcomb≈1.485; 5.36/1.485≈3.61σ (quoted “∼3.6σ”).
  - S8 tension: 0.827±0.010 vs 0.776±0.017 gives Δ=0.051; σcomb=0.0197; 2.59σ (quoted 2.6σ).
  - Pivot wpivot=−0.952±0.019; distance from −1 is 2.5σ.
  - β product Caγ Δϕ/fa ≈ 10.3 for β=0.342° and α/(4π)=5.807×10−4 rad; correct.
  - ρcrit,0 ≈ 3.7×10−11 eV4 consistent with H0=1.44×10−33 eV and MPl=2.44×10^27 eV.
- Suggestion: Retain these explicit numeric back‑of‑the‑envelope validations as they currently are; no changes required.

P1B-m2 (Equation (1) clarity; p. 9)
- Problem: The EB template is written once as sin(2β)cos(2β)CEE and once as ½ sin(4β) CEE. They are equivalent, but the switch may confuse.
- Required fix: Immediately below Eq. (1), add “We use ½ sin(4β)=sin(2β)cos(2β).”

P1B-m3 (Mask/ℓ‑range wording; p. 9–10)
- Problem: The text says “bins above ℓmax=1024 carry zero template weight … so the 20‑bin sum is effectively restricted to ℓ≤1024.” Strictly, those bins still contribute a β‑independent constant to χ².
- Required fix: Clarify: “They add a β‑independent constant and do not affect the minimizer; hence the β solution is effectively driven by ℓ≤1024.”

P1B-m4 (AI acknowledgement; p. 17)
- Problem: “Acknowledges the use of Claude (Anthropic).” PRD has no prohibition, but content should make clear that all results were independently verified by the author (already stated).
- Required fix: None strictly required; optional: move this line to a brief parenthetical in Acknowledgments.

P1B-m5 (ALP EOM notation; p. 13)
- Problem: EOM given as ϕ¨+3Hϕ˙+m^2 f_a sin(ϕ/f_a)=0. Some readers expect ϕ¨+3Hϕ˙+m^2 sin(ϕ/f_a)=0 (dimensionless angle). Your form is correct for V(ϕ)=m^2 f_a^2[1−cos(ϕ/f_a)].
- Required fix: Add one line noting V′(ϕ)=m^2 f_a sin(ϕ/f_a) to settle any dimension concerns.

NIT (cosmetic)

P1B-n1 (Typos/formatting)
- Several long dashes and “︁” artifacts (likely PDF extraction) appear in the copy but are unlikely in the typeset manuscript. Ensure consistent dash use and remove stray combining characters.
- “CamSpec” capitalization is consistent; okay.

P1B-n2 (Length)
- The main text (21 pp) is dense and includes extensive pipeline logistics. After moving repository/process details to Supplementary Material, the main text could likely be reduced by ~2–3 pages without loss of scientific content.

Abstract-last drift sweep (pattern‑045)
- All abstract scalars trace to the body and are arithmetically correct.
- REQUIRED tweak (see P1B‑E4): note “unweighted template-fit” in the pseudo‑Cℓ bias line.
- The abstract’s strong caveats that (i) ΔNeff is a stock‑CAMB proxy, (ii) NaMaster SNRs are MC pipeline recovery figures, and (iii) spectator‑ALP consistency is not an ECH‑specific prediction are properly reflected in the body.

Provenance surfaces (patterns 046/047)
- See P1B‑E1/E2: provide DOIs; move commit/file‑path details to the archived README and cite the DOI in the paper.

Uncomputed quantitative claims (pattern‑048)
- Most “consistent with,” “dominates,” and “negligible” statements are backed by numbers. Two places to tighten:
  - Explicitly show (or cite) the ≈80% bias reduction for inverse‑variance weighting in the main text (you quantify it, but add the numerical β̂ value alongside the claim—already present as 0.264°; good).
  - Provide a brief N_MC sufficiency rationale (P1B‑M1).

Standalone‑reader test
- The paper states it is a companion but is methodologically self‑contained for the three analyses. Ensure that all symbols are defined locally (e.g., define Caγ, fa, ma on first appearance in Sec. VI and keep notation consistent; fix P1B‑M4).

Effect sizes
- Good practice: you already provide a 1.7% H(z) effect at z=0.5 for CPL; extend with one additional redshift (e.g., z=1) or a small inset figure if space allows (P1B‑M5).

## Summary recommendation
MAJOR REVISIONS

Rationale: The core methodology and arithmetic are careful and, with the added clarifications, likely publishable. However, PRD requires stable, citable data/code releases (missing DOIs), avoidance of internal process language in the main text, and caution with σ‑level claims drawn from an overlap‑uncorrected SN product likelihood. The Planck likelihood pairing for the headline ΔNeff result should be made internally consistent. The NaMaster abstract line needs to declare the estimator explicitly. Addressing these will bring the manuscript to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes audit)

ESSENTIAL

P1B-E6 (Convergence of the PR4-consistent ΔNeff re-run)
- Problem: The PR4-consistent verification run used to support the “0.04σ agreement” claim reports R̂−1 = 0.0147 (> 0.01), i.e., not at the study’s own publication-grade convergence threshold.
- Required fix: Re-run the PR4-consistent chain to R̂−1 < 0.01 and then quote the ΔNeff agreement. Otherwise, label the 0.04σ figure as preliminary and do not use it as a robustness bound.

MAJOR

P1B-M6 (Misstated magnitude of misalignment fine-tuning under a cosθ prior)
- Problem: The abstract/main text state “≳100×” misalignment fine-tuning for spectator status under a cosθ-flat prior, but the paper itself reports a posterior mass of 0.068% for θi ≤ 0.1 in the cosθ prior run (i.e., ~1/0.00068 ≈ 1,470×), and the prior-volume fraction for θ ≤ 0.1 under a cosθ prior is ≈(1−cos 0.1)/2 ≈ 0.25% (≈400×). The “≳100×” claim substantially understates both the analytic prior-volume fine-tuning (~400×) and the posterior sliver (~1,500×).
- Required fix: Adopt a single, explicit definition of “fine-tuning factor” (e.g., inverse prior-volume, or posterior-mass fraction) and report consistent numbers. If using the cosθ prior, state the analytic prior-volume (~400×) and, separately, the posterior sliver (~1,500×) with their precise fractions. Update abstract/body accordingly.

P1B-M7 (Unweighted “χ²” objective is dimensional; rename or normalize)
- Problem: Eq. (1) is called χ² but, without per-bin variance weighting, it carries units (µK^4) and is not a bona fide χ². This can mislead readers about goodness-of-fit interpretations.
- Required fix: Either (a) rename it “unweighted sum of squared residuals” and state explicitly it is used only as a minimizer, not as a test statistic, or (b) supply per-bin variances and use a properly normalized χ². If you keep the unweighted form, remove any language suggesting χ²-based inference.

P1B-M8 (Robustness-battery results reported without uncertainties/seed stability)
- Problem: Alternative-estimator and configuration recoveries (e.g., 0.264°, 0.251°, 0.239°, “purify_b=True: 0.238°”) are quoted without ±SE or seed-stability checks.
- Required fix: For each robustness configuration, report β̂ ± SE of the 500-MC mean and confirm stability over at least one independent seed set. This also helps establish that N=500 is sufficient (can be merged with your NMC sufficiency check).

MINOR

P1B-m6 (Figure 2 caption mislabeling — Standard Model line)
- Problem: Caption label “SM ( Neff = 0)” is incorrect/confusing. It should be “ΔNeff = 0” (or “Neff = 3.046”).
- Required fix: Correct the caption to “ΔNeff = 0” (or the full Neff value).

P1B-m7 (wpivot redshift rounding)
- Problem: Using ap = 0.790 gives zp = 1/ap − 1 ≈ 0.266, but the text quotes 0.27. This is fine as a rounded value, but elsewhere many numbers are given to three sig figs.
- Required fix: Either state zp = 0.266 (consistent sig figs) or explicitly note rounding.

P1B-m8 (Report uncertainties for reduced-bias alternatives)
- Problem: The inverse-variance-weighted estimator’s bias is given as −0.006° with no uncertainty; same for the CAMB-lensed-BB variant (−0.019°).
- Required fix: Add ±SE for these bias estimates (from the same 500-MC ensembles) so readers can judge whether residual biases are statistically distinguishable from zero.

P1B-m9 (BBN-consistency module scope)
- Problem: You assert the PArthENoPE-based BBN predictor remains within its calibrated domain for Neff ∈ [2.046, 5.046], but no version/citation or uncertainty propagation for YHe(Neff) is provided.
- Required fix: Cite the specific PArthENoPE implementation/version and its Neff-validity domain; clarify whether any extrapolation occurs and whether uncertainties in YHe(Neff) are propagated (or justify neglect).

P1B-m10 (S8 presentation style)
- Problem: Different sections use slightly different deltas/rounding for S8 tensions (e.g., Δ=0.049 vs 0.051). All are numerically consistent, but the presentation jumps between overlap integrals and Gaussian σ-distances.
- Required fix: Harmonize the reporting style (pick overlap or Gaussian z-score for the headline, give the other in parentheses), and keep deltas and σ’s consistently rounded.

P1B-m11 (Table IV column consistency)
- Problem: The “full chain” row mixes a narrative “median ≃ 36” for m/H0, while other subset rows use 16/50/84 percentiles. This hinders straightforward comparisons.
- Required fix: Report 16/50/84% for m/H0 in all rows (including “full chain”) for uniformity.

P1B-m12 (“~0.5σ of ACT” phrasing)
- Problem: 0.040°/0.074° = 0.54σ. You later caution non-comparability, but the 0.5σ phrasing appears before that caveat and invites overinterpretation.
- Required fix: Use “≈0.54σ (not directly comparable; see text)” or move this comparison to a parenthetical after the explicit caveat.

EXPLANATION
These issues were not covered in my initial review because they required a second-pass consistency sweep focused on dimensionality/labeling details (χ² units; figure caption), convergence thresholds for the verification run (R̂), and a more rigorous quantification of the cosθ prior fine-tuning that compares analytic prior volumes against the reported posterior sliver.