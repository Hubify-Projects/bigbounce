# P4_v1_0_109_R_INTERNAL R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1715pt
**Wall time**: 49.4s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=80113, completion=3695, reasoning=2783, total=83808

---

**PAPER-GRO-B1: Abstract (multiple paragraphs)**

**BLOCKER**  
The abstract remains a 1200+ word defensive log of prior reviewer points, version tags ("v1.0.108 multi-null battery", "P4-EXT ChatGPT-B3"), and scope carve-outs rather than a concise statement of result + limitation. The "multi-null verdict" and "99.3% reproduction" are load-bearing but buried in parentheticals.  

**Fix**: Cut abstract to ≤300 words: state the null at ℓ=1 post-MASTER on subsample mask, the 99.3% monopole-leakage reproduction on canonical mask, the bootstrap + cross-spectrum resolution of the +3.64σ residual, and the explicit matched-pipeline caveat for Shamir. Move all version notes and estimator hierarchies to Methods.

**PAPER-GRO-B2: Section 4.3 / monopole_mask_null + conclusions**

**MAJOR**  
The verdict logic "(i) ruled out by ℓ=2>ℓ=1 + bootstrap + p_eq + cross-spectrum" is asserted but not demonstrated as rigorous closure. The cross-spectrum r_ℓ=2 = -0.65 (σ = -2.89) is against a permutation null that breaks spatial covariance; the bootstrap is stated to capture only marginal overdispersion. No joint test or systematics-modeling null is shown that would exclude a residual coherent depth signal at the observed amplitude.  

**Fix**: Add one paragraph with a quantitative statement: "Under the bootstrap null the residual is -0.22σ; under a depth-preserving null the amplitude is still consistent with the observed cross-spectrum anti-correlation at the 2.9σ level. A full joint likelihood over auto + cross spectra with depth maps is left to future work."

**PAPER-GRO-B3: Title + abstract sensitivity claim**

**MAJOR**  
Title advertises "Sub-Percent Sensitivity (50%-Recovery 3σ Threshold A≈0.75%)". The 0.75% figure is the empirical threshold on the HC subsample (N=471k); the full-catalog Fisher floor is 0.29% but never empirically demonstrated. The headline number therefore mixes two different samples and is not load-bearing for the full 3.2M catalog claim.  

**Fix**: Change title to "... at 0.75% Empirical 50%-Recovery Threshold on High-Confidence Subsample (Fisher Floor 0.29% on Full Catalog)". State the distinction once in the abstract and once in Sec. 4.3.

**PAPER-GRO-B4: Abstract + Sec. 4.3 cross-spectrum narrative**

**minor**  
The cross-spectrum is presented as the "smoking gun" confirming interpretation (ii). The quoted r_ℓ=2 = -0.65, σ = -2.89 is internally consistent with the text, but the permutation null used for the cross-spectrum is not the same as the bootstrap null used for the auto-spectrum. This creates a mild apples-to-oranges comparison that a reviewer will flag.  

**Fix**: Add one sentence: "The cross-spectrum significance is evaluated against a per-pixel permutation null that destroys spatial correlations; the bootstrap null used for the auto-spectrum preserves marginal per-pixel variance but not off-diagonal covariance."

**PAPER-GRO-B5: Overall framing (Introduction + Conclusions)**

**minor**  
The paper correctly states it does not supersede Iye/Tadaki nulls and requires matched-pipeline reanalysis for Shamir. However, repeated emphasis on "largest catalog" and "quantifiable leakage channel" still reads as novelty inflation when the core result is a pipeline-specific systematics demonstration on a known mask-coupling effect.  

**Fix**: Replace "advances beyond CE-ResNet in three respects" with "extends CE-ResNet coverage by 1.6× while adding an explicit pre/post-MASTER leakage diagnostic." Remove any residual implication that the 99.3% figure generalizes beyond this classifier + footprint.

**PAPER-GRO-B6: Data Availability + reproducibility artifacts**

**nit**  
Dozens of GitHub artifact links with full paths and release tags are useful for reproducibility but clutter the main text and footnotes. Several are cited only for internal verification.  

**Fix**: Move the long list of artifact URLs to a single "Reproducibility" subsection in Data Availability. Retain only the three or four load-bearing JSONs in the main text.
