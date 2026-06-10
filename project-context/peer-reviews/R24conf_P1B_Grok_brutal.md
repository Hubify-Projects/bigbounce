# P1B R24conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.52.pdf` md5=4047dfe1 pages=15
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 164.2s

---

**Referee Report for P1B (PRD)**

**P1B-E1**  
Section: Title page (p. 1)  
Problem: Header states “(Dated: June 9, 2026 PDT)”. A submission date in the future is unacceptable.  
Required fix: Remove entirely.

**P1B-E2**  
Section: Abstract (p. 1) and §III (p. 3)  
Problem: Abstract headline result “\(\Delta N_{\rm eff}\) consistent with zero” is presented as a physics statement while the body repeatedly declares “Not a spin-torsion theory module” and “does not test the ECH spin-torsion sector directly.” The abstract therefore misrepresents the actual claim.  
Required fix: Rewrite abstract to state only the methodological result (null-consistency test of stock CAMB) and remove any implication of a physical constraint on the target theory.

**P1B-E3**  
Section: §I (p. 2) and §VI (p. 8)  
Problem: Paper is 15 pages (including 4 appendices) yet contributes only (i) a stock-CAMB null run, (ii) a 500-realization NaMaster bias test on synthetic skies, and (iii) a spectator-ALP consistency check whose result is already known from standard GR. No new observable, no new likelihood, no new constraint on ECH parameters.  
Required fix: Reduce to Letter length (<8 pages) or withdraw.

**P1B-M1**  
Section: p. 9 (“an earlier draft quoted”) and p. 10 (“Correction note”, “committed truth”)  
Problem: Multiple internal editing and version-control phrases remain in the text.  
Required fix: Delete all such language.

**P1B-M2**  
Section: Table I (p. 3) and text p. 3  
Problem: Two frozen chains are labeled “full-tension” and “Planck+BAO+SN”; a third accumulating Planck-only chain is mentioned but never shown. The headline \(\Delta N_{\rm eff}\) numbers are therefore not the result of a single, documented posterior.  
Required fix: Either include the third chain or remove the “full-tension” label.

**P1B-M3**  
Section: Fig. 3 caption and §IV (p. 6–7)  
Problem: Pipeline-recovery bias \(\Delta\hat\beta = -0.032^\circ\) is reported without a quantitative statement of the systematic floor (\(0.040^\circ\)) in the same sentence; the two numbers appear side-by-side without the required “not directly comparable” qualifier.  
Required fix: Add explicit warning at every juxtaposition.

**P1B-N1**  
Section: Eq. (3) (p. 9)  
Problem: Numerical prefactor \(4.93\times10^{-3}\) is given without derivation or reference to the exact normalization of \(\alpha_{\rm EM}/4\pi\) used in the EOM integrator.  
Required fix: Supply one-line derivation or cite the precise convention.

**P1B-N2**  
Section: References (throughout)  
Problem: Multiple “Paper I(a)”, “Paper III”, “Paper IV” citations are listed as “posted concurrently on arXiv” with no actual arXiv numbers.  
Required fix: Replace with real identifiers or remove cross-paper claims.

**P1B-NIT1**  
Section: p. 1 author affiliation  
Problem: “Independent Researcher, Los Angeles, California, USA” with no institutional e-mail domain.  
Required fix: Standard PRD formatting.

## Summary recommendation
**REJECT**

The manuscript is a 15-page technical appendix whose only quantitative results are (a) a null \(\Delta N_{\rm eff}\) run in unmodified CAMB and (b) a 500-realization pipeline test whose bias is already smaller than the published observational uncertainty. The paper itself repeatedly states that none of these tests constrain the target ECH theory. Combined with residual internal editing language, an impossible future date, and an abstract that misrepresents the scope, the manuscript falls well below the threshold for a standalone PRD article.