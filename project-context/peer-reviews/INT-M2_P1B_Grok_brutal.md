# P1B INT-M2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=b3fe7527 pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 120.0s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (Houston Golden)

**Journal target:** Phys. Rev. D

**Date of review:** current

**Finding P1B-E1 (ESSENTIAL)**  
Section: Abstract / p. 1 (first paragraph after title)  
Problem: The lead quantitative claims (“ΔN_eff consistent with zero (−0.020 ± 0.169 full-tension; +0.058 ± 0.179 Planck+BAO+SN)”) are presented without any accompanying statement that these are *stock-CAMB proxy runs that do not solve torsion-modified Boltzmann equations*. The same paragraph later states the run “does not verify the spin-torsion theory module itself.”  
Required fix: Remove the numerical results from the abstract or prepend an explicit scope qualifier in the abstract itself.

**Finding P1B-E2 (ESSENTIAL)**  
Section: p. 1 (Dated line)  
Problem: “(Dated: June 28, 2026)” appears in the rendered PDF. This is an internal placeholder or version artifact.  
Required fix: Delete or correct to the actual submission date.

**Finding P1B-E3 (ESSENTIAL)**  
Section: Abstract + §III (pp. 1, 3)  
Problem: The abstract headline numbers for ΔN_eff are taken from the *physically unmotivated* two-sided posterior; the body (p. 4) explicitly states that the one-sided 95 % upper limit under the motivated restriction ΔN_eff ≥ 0 is ΔN_eff < 0.31 (full-tension). The abstract therefore reports a weaker, non-physical bound.  
Required fix: Replace abstract numbers with the one-sided limits or add an explicit footnote in the abstract.

**Finding P1B-E4 (ESSENTIAL)**  
Section: §I (Scope of this paper, p. 2) and repeated in §III, §VI  
Problem: The paper repeatedly states that none of the three analyses constitutes evidence for or against the ECH framework and that the birefringence signal “is not a distinctive ECH prediction.” The abstract nevertheless frames the work as “Technical Verification Companion to the ECH Spin-Torsion Program.” This is a material mismatch between title/abstract framing and actual scientific content.  
Required fix: Retitle or rewrite the abstract to reflect that the manuscript is a *null-consistency and pipeline-validation study only*.

**Finding P1B-M1 (MAJOR)**  
Section: §IV and Fig. 3 (pp. 8–11)  
Problem: The NaMaster recovery bias is reported as |Δβ̂| ≤ 0.040° (worst-case). The published Planck+ACT value is 0.342° ± 0.094°. The paper never quantifies whether this 0.040° floor is negligible relative to the 0.094° uncertainty; the two numbers are placed side-by-side without an explicit “not directly comparable” qualifier at every juxtaposition.  
Required fix: Add a dedicated paragraph computing the ratio of pipeline bias to published uncertainty and state the implication for any future claim.

**Finding P1B-M2 (MAJOR)**  
Section: §VI and Table IV (pp. 13–18)  
Problem: The spectator-ALP “consistency check” uses a tuned misalignment subspace (θ_i ≲ 0.1) that is ~25× finer than the natural prior midpoint. The paper acknowledges this tuning is required to recover the observed β but does not propagate the tuning into the final quoted significance or Bayes-factor statement.  
Required fix: Either (a) report the evidence ratio after marginalizing over the tuning or (b) downgrade the claim to “illustrative” and remove all numerical tension statements.

**Finding P1B-M3 (MAJOR)**  
Section: Data Availability (p. 18) and Appendix A  
Problem: The reproducibility manifest lists commit b22f8cc9 and version v1B.0.82, yet several frozen-chain names and likelihood-block labels still reference 2018 Planck releases that were superseded by the PR4/NPIPE products used in the headline chains. No SHA256 or DOI of the exact frozen likelihood files is supplied.  
Required fix: Provide a machine-readable manifest with exact commit hashes, likelihood file checksums, and a statement that the released products reproduce every number in Tables I–IV to the quoted precision.

**Finding P1B-N1 (MINOR)**  
Section: p. 2 (footnote 1) and multiple figure captions  
Problem: Duplicate phrasing “canonical canonical-mask” appears in the rendered text.  
Required fix: Proof-read for repeated tokens.

**Finding P1B-N2 (NIT)**  
Section: Throughout  
Problem: The manuscript is 22 pages for three null-consistency exercises whose headline results are all “consistent with zero” or “pipeline bias only.” PRD length guidelines for a pure verification note are typically ≤ 10–12 pages.  
Required fix: Shorten by moving all “reproducibility” appendices to supplementary material or a public repository.

**Finding P1B-E5 (ESSENTIAL – abstract drift)**  
After full-body read: The abstract claims “the ΔN_eff extension does not reduce the residual ~3.6σ tension.” The body (p. 3) shows that the H_0 posterior remains 67.68 ± 1.06 km s^{-1} Mpc^{-1} (Planck-dominated) and that the SH0ES anchor is not included in the proxy run. The abstract therefore overstates what the proxy actually demonstrates.  
Required fix: Rewrite the abstract sentence to match the calibrated body statement.

**Finding P1B-E6 (ESSENTIAL – standalone-reader test)**  
Section: §VI (p. 13)  
Problem: The birefringence consistency argument repeatedly refers to “the ~25× mis-alignment tuning required” and to results “disclosed in Sec. VI and fn. 6,” but the actual derivation of the 25× factor and the spectator-safe cut Ω_a < 0.01 is only in the companion Paper I(a). A reader without that paper cannot reproduce the numerical threshold.  
Required fix: Either embed the short derivation or remove the quantitative claim.

**Summary recommendation**  
**REJECT**

The manuscript is a technical verification companion whose own text repeatedly states that none of its three analyses tests the ECH spin-torsion framework, that the birefringence signal is not distinctive, and that the MCMC exercise is only a stock-CAMB proxy. The quantitative results are null-consistency statements already expected under ΛCDM, the length is excessive for the incremental content, and multiple material mismatches exist between the title/abstract framing and the explicit scope limitations inside the paper. These defects are structural and cannot be repaired by minor revision.