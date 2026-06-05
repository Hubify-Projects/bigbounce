# P2 R10v3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high
**Wall time**: 43.1s

---

Referee report on  
“Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”  
(Paper tag P2, 6 pages)

---------------------------------------------------------------------
FINDINGS  
Each item is labelled P2-E# (ESSENTIAL), P2-M# (MAJOR), P2-m# (MINOR), P2-n# (NIT).

ESSENTIAL – must be fixed before the manuscript can be considered
---------------------------------------------------------------------
P2-E1  Sect. 2.1–2.2, p. 2  
Text: “∆φ ≈ f_a θ_i (1 – J₀(m/H₀)) … 1 – J₀(1) ≈ 0.24” followed by “cosmological field evolution gives ∆φ/f_a ∼ 10⁻² … β ≈ C₀ θ_i × 5 × 10⁻³ rad ≈ 0.27°.”  
Problem: The two quoted factors (0.24 and 10⁻²) differ by ≃ 25. Inserting the first into eq. (2) gives β ≈ 0.12 C₀ θ_i rad ≃ 7° for C₀ θ_i ≈ 1, contradicting the advertised 0.27°. No derivation is presented to justify the extra ~2 × 10⁻² suppression.  
Required fix: Provide a step-by-step, dimensionally explicit derivation from the equation of motion through to β, showing how the 0.24 factor is reduced to 10⁻². All numbers in the abstract and conclusions must trace to that derivation.

P2-E2  Sect. 2.1, p. 2  
Text: “J₀(m/H₀)/J₀(0)” with J₀(0)=1.  
Problem: The argument m/H₀ is dimensionful; J₀ requires a pure number. H₀ must be converted to natural units before division.  
Required fix: State explicitly which unit system is used and demonstrate that m/H₀ is dimensionless. If a rescaling by ħ or c is implicit, write it.

P2-E3  Sect. 3.1 & Eq. (4), pp. 3–4  
The Planck and ACT measurements are treated as statistically independent when forming the combined likelihood. The two experiments share ≈ 40 % of sky area and the same cosmic variance; they are therefore correlated. Ignoring covariance inflates the quoted significance (3.9 σ).  
Required fix: Provide an estimate of the cross-covariance (even approximate, e.g. from mask overlap or published covariance matrices) and recompute β_combined and its significance. Label all results “CV-corrected” vs “raw” so that incomparable σ’s are not juxtaposed.

P2-E4  Sect. 3.3, Table 1, p. 3  
Accepted MCMC samples: 2 160; 6 840; 720. 68 %-level errors of O(3 %) are nevertheless quoted. Effective sample sizes are only O(10²–10³), too small for evidence ratios (ln B) and for tail-probability statements such as “3.9 σ” or “R̂–1 < 0.01”.  
Required fix: Increase each chain to ≥ 5 × 10⁴ effective samples or use an analytic likelihood. Re-evaluate all error bars, ln B and R̂, or state that evidence is not reported.

P2-E5  Sect. 3.4, p. 3  
Text: “ln B = 5.17 … indicative evidence.”  
Problem: ln B is computed with a Savage–Dickey ratio using the undersampled chains above; prior volume is changed ad hoc and gives ±0.7 swings. Claiming “indicative evidence” is overstated.  
Required fix: Recompute ln B with properly converged chains and quote an uncertainty. Alternatively drop the Bayes-factor claim.

P2-E6  Table 1 caption, p. 3  
Run 1 fixes C = 8 with no motivation anywhere in the text; C denotes the anomaly coefficient earlier labelled C₀.  
Required fix: Explain and justify the choice C = 8. If it is a placeholder, remove it or sample it.

P2-E7  Units, throughout (e.g. eq. (2), p. 2; LiteBIRD forecast, p. 4)  
Radians and degrees are mixed without always indicating the conversion. Example: “5 × 10⁻³ rad ≈ 0.27°” appears one line after writing β in degrees.  
Required fix: State units every time β is converted; propagate factors of 57.3 explicitly in formulas and numerical estimates.

P2-E8  Sect. 3.2, p. 3  
Equation (3) (product of Gaussians) is labelled a “summary-likelihood.” No justification is given that the quoted β_i errors are Gaussian or that systematic uncertainties (band-pass, calibration) are folded in.  
Required fix: Document the likelihood choice and test Gaussianity (e.g. χ² per dof). If systematics dominate, incorporate them or state that the result is purely statistical.

MAJOR – substantial revision needed
-----------------------------------
P2-M1  Abstract & Sect. 4, p. 4  
Claim: “LiteBIRD will test at 9 σ significance.” The forecast uses only statistical noise (σ_β = 0.03°) and ignores calibration systematics, which the authors themselves note could be 0.1–0.3°.  
Required fix: Either include LiteBIRD’s systematic error budget in the forecast or downgrade the claim to “up to 9 σ if systematic errors can be controlled below 0.03°.”

P2-M2  Sect. 2.2, p. 2  
Statement: “C₀ ∼ 1 … no fine-tuning.” The later posterior gives C_aγ × θ_i = 3.4 ± 1.1, which is not O(1).  
Required fix: Clarify which parameter is taken to be natural and quantify acceptable ranges.

P2-M3  Sect. 3.1, p. 3  
Both the Eskilt joint analysis (β = 0.342 ± 0.094°) and the authors’ combined value (0.242 ± 0.061°) are used interchangeably. The reader cannot know which estimate drives which figure/table.  
Required fix: Adopt one primary β dataset for all statistical inferences or clearly annotate every result with the dataset used.

P2-M4  References, p. 6  
“Namikawa, Murai & Naokawa” – surname typo; paper listed as “in preparation, 2025”. Citations to unpublished work must be labelled “private communication” or removed.  

P2-M5  Eq. (8), p. 3  
Caγ × θ_i = 3.4 ± 1.1 reported but neither Caγ nor θ_i marginal distributions are shown.  
Required fix: Provide 1-D posteriors for each to demonstrate that neither parameter hits the prior edge.

MINOR – advisable but not publication-critical
----------------------------------------------
P2-m1  Title/Abstract  
“Predictions, Constraints, and LiteBIRD Forecasts” → plural noun agrees with three items, OK but mildly wordy; suggest trimming.

P2-m2  Sect. 5, p. 4  
Duplicate phrase: “This birefringence prediction is independent of bounce cosmology.” appears twice almost verbatim.

P2-m3  Fig. 1 & Fig. 2 captions, pp. 4–5  
Axes tick labels are tiny (<6 pt) in the PDF; enlarge for readability in print.

NIT – purely cosmetic
---------------------
P2-n1  Sect. 3.3, p. 3  
“Gelman-Rubin convergence diagnostic R̂ − 1 < 0.01 confirms adequate mixing” – should be written \( \hat R-1\).

P2-n2  Typo p. 5: “non-Gaussianity fNL = −35/8 provides” → either “f_NL” or “f_{NL}”.

P2-n3  p. 5, line 2: “significance reported here.” → “significance reported above.”

---------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The manuscript is concise and topical, but its central numerical claim (β ≈ 0.27° emerging “naturally”) is internally inconsistent, and the statistical treatment (covariance, MCMC volume, Bayes factor) is not yet robust. The essential issues listed above must be resolved; otherwise the quoted 3.9 σ detection and 9 σ forecast are not supported.