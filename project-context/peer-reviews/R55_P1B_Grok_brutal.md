# P1B R55 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R55_P1B/paper1b_mcmc_companion.pdf` md5=2d80d814 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 267.9s

---

**Referee Report**

**P1B-E1 (ESSENTIAL, Abstract + p. 1)**  
The abstract states specific load-bearing scalars (e.g., \(\Delta N_{\rm eff}=-0.020\pm0.169\), \(H_0=67.68\pm1.06\)) without the explicit qualifier that appears on p. 3: “Not a spin-torsion theory module.” The abstract therefore overstates the result relative to the body’s final calibrated scope statement. Required fix: insert the scope qualifier into the abstract or remove the numerical claims.

**P1B-E2 (ESSENTIAL, p. 1–2 and throughout)**  
The paper is not standalone. Every major result (MCMC chains, \(\beta\) recovery, ALP scan) is defined only by reference to the unavailable “Paper I(a)” or to external GitHub commits. A reader cannot recompute or even interpret the quoted \(\sigma\) values without those documents. Required fix: either embed the minimal self-contained definitions or withdraw the numerical claims.

**P1B-E3 (ESSENTIAL, p. 3, 7, 11)**  
Multiple side-by-side \(\sigma\) statements (e.g., “3.6\(\sigma\) headline” vs. “pipeline bias 0.040°”) appear without the explicit “not directly comparable” language required by the journal’s policy on null-procedure comparisons. The text on p. 3 acknowledges the distinction only once and then repeatedly juxtaposes the numbers.

**P1B-M1 (MAJOR, p. 1, 21 pp total)**  
A 21-page “technical verification companion” whose abstract and introduction repeatedly disclaim any new physics result exceeds reasonable length for the claimed contribution. Recommended maximum: 8–10 pages.

**P1B-M2 (MAJOR, p. 4, Table I)**  
The one-sided 95 % upper limits on \(\Delta N_{\rm eff}\) are derived from a post-hoc renormalization of the negative tail. The procedure is described only in a footnote and is not reproducible from the published chains without the exact `getdist` settings. Required fix: supply the precise post-processing script or drop the one-sided limits.

**P1B-M3 (MAJOR, p. 9–10, Fig. 3)**  
The NaMaster pipeline-recovery bias (\(\Delta\hat\beta=-0.032^\circ\) to \(-0.040^\circ\)) is presented as a “validation figure, not a sky-detection significance.” Yet the caption and surrounding text still quote template-fit SNRs (20.32, 25.71) that a casual reader will misinterpret as detection significance. Required fix: remove all SNR numbers or add an explicit “do not interpret as detection” warning in every figure that displays them.

**P1B-N1 (MINOR, p. 1)**  
Paper date “June 20, 2026” is chronologically impossible for a submission in the current review cycle. Cosmetic.

**P1B-N2 (MINOR, multiple tables)**  
Axis labels and units are internally consistent, but several tables (I, II, IV) contain 6–7 significant figures on derived quantities whose input covariances are quoted to only 2–3 figures. Minor rounding audit required.

**P1B-NIT-1**  
Minor typographic duplication (“canonical canonical-mask”) appears once in the source text but is not visible in the rendered PDF.

**Summary recommendation**  
MAJOR REVISIONS

The manuscript is a conscientious but over-long technical appendix whose central numerical claims cannot be evaluated by a standalone reader and whose abstract overstates scope relative to the body’s own repeated disclaimers. The methodological care is evident, yet the combination of non-self-contained results, length, and missing explicit comparability warnings violates PRD standards for a methods/verification paper. A substantially shortened, fully standalone revision that removes all numerical claims not reproducible from the supplied material would be reconsidered.