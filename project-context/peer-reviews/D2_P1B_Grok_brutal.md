# P1B D2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=b166f4c0 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 272.6s

---

**P1B-E1 (ESSENTIAL)**  
**Location:** Abstract (p. 1) + Table I (p. 5) + §III (p. 3)  
**Problem:** Abstract states “\(\Delta N_{\rm eff}=-0.020\pm0.169\) (full-tension)” and “\(H_0=67.68\pm1.06\) km s\(^{-1}\) Mpc\(^{-1}\)” as the headline result. These numbers are recovered only after post-processing (renormalized CDF, 30 % burn-in cut, one-sided 95 % upper limit). The body never states the raw two-sided posterior mean before these cuts.  
**Required fix:** Add an explicit sentence in the abstract and §III stating the raw MCMC mean and the exact post-processing steps required to obtain the quoted numbers.

**P1B-E2 (ESSENTIAL)**  
**Location:** p. 10, line “the canonical canonical-mask bias of −0.032°”  
**Problem:** Duplicate word (“canonical canonical-mask”).  
**Required fix:** Correct typographical error.

**P1B-E3 (ESSENTIAL)**  
**Location:** Abstract (p. 1) + §IV (p. 7–10) + Fig. 3 caption  
**Problem:** Abstract and Fig. 3 caption present NaMaster pipeline-recovery numbers (\(\hat\beta=0.238^\circ\), bias \(0.040^\circ\)) as a verification result. The text repeatedly states these are “not a competitive sky detection” and “not directly comparable” to the published 3.6\(\sigma\) Planck/ACT value. The abstract omits this qualification.  
**Required fix:** Abstract must contain the explicit qualifier “pipeline-validation figure only; not a sky-detection significance claim.”

**P1B-M1 (MAJOR)**  
**Location:** §I (p. 2) and throughout  
**Problem:** The paper is 21 pages long yet repeatedly asserts it is only a “technical verification companion” whose central claim is a null result. PRD page limits and scope for companion/technical notes are routinely enforced at \(\lesssim12\) pages for such material.  
**Required fix:** Reduce to \(\leq12\) pages or reclassify as a regular article with a clear scientific increment.

**P1B-M2 (MAJOR)**  
**Location:** p. 2 (“Scope of the validation”), p. 7 (Fig. 2 caption), p. 10  
**Problem:** Multiple 3.6\(\sigma\) and 2.9\(\sigma\) statements appear side-by-side with the explicit statement that they are “not directly comparable.” The qualification is not repeated at every juxtaposition.  
**Required fix:** Insert the phrase “not directly comparable” at every numerical comparison of pipeline bias versus published sky significance.

**P1B-M3 (MAJOR)**  
**Location:** §VI (p. 12–15) and abstract  
**Problem:** The spectator-ALP consistency check is presented as supporting the observed birefringence signal, yet the text states the same \(\beta\approx0.27^\circ\) arises in any GR+ALP model. The abstract does not contain the sentence “not a distinctive ECH prediction.”  
**Required fix:** Add the explicit non-distinctiveness statement to the abstract.

**P1B-N1 (MINOR)**  
**Location:** Header (p. 1)  
**Problem:** Paper dated “June 19, 2026” (future date).  
**Required fix:** Correct date.

**P1B-N2 (MINOR)**  
**Location:** Fig. 1 caption (p. 7) and Table I footnote a  
**Problem:** Footnote refers to “\(R-1<3\times10^{-3}\)” while the table header shows “Worst \(\hat R-1\)”. Inconsistent notation.  
**Required fix:** Standardize Gelman–Rubin statistic notation.

**P1B-N3 (NIT)**  
**Location:** Multiple figure captions (Figs. 2, 3)  
**Problem:** Axis labels and legend fonts are legible but at the lower limit of PRD production standards; no scientific content is lost.  
**Required fix:** None required for acceptance.

## Summary recommendation
**MINOR REVISIONS**

The manuscript is a careful, narrowly scoped technical verification paper whose central claims are repeatedly caveated. The only issues that block acceptance are (1) an abstract that omits scope qualifiers present in the body, (2) a typographical duplication that must be fixed, and (3) the absence of an explicit statement of the post-processing steps needed to recover the headline numbers. All other problems are either cosmetic or length-related and can be addressed by shortening or reclassification. Once the three essential items are corrected the paper meets PRD standards for a methods/companion article.