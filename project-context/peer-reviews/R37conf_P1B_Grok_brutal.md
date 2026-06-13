# P1B R37conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.65.pdf` md5=bac8d620 pages=20
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 67.0s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (P1B)

**Journal:** Physical Review D

**Date of review:** Round R37conf context

**Classification of findings**

**P1B-E1 (ESSENTIAL, Title + p. 1–2, abstract block)**  
The title and opening paragraph frame the work as “technical verification companion to the ECH Spin-Torsion Program.” The body immediately and repeatedly disclaims this: “NOT a spin-torsion theory module,” “does not verify the spin-torsion theory module itself,” “NOT a competitive sky detection,” “not a distinctive ECH prediction.” The actual content is three standard null-consistency tests on unmodified CAMB + NaMaster. This is a direct mismatch between title/claim and delivered content.  
**Required fix:** Retitle as a pure methods/technical note on stock pipelines or withdraw.

**P1B-E2 (ESSENTIAL, p. 1–3, §III scope statement)**  
The paper states it performs “no custom CAMB modifications” and “no torsion modifications.” All reported posteriors are therefore identical to a standard \(\Lambda\)CDM+\(N_{\rm eff}\) run. No ECH-specific prediction is tested. Publication as a PRD companion paper is not justified.

**P1B-E3 (ESSENTIAL, p. 2, abstract + Table I)**  
Headline numbers (\(\Delta N_{\rm eff}=-0.020\pm0.169\), \(H_0=67.68\pm1.06\)) are standard \(\Lambda\)CDM results. The paper itself labels them “null-consistency test.” No new constraint or tension resolution is demonstrated.

**P1B-E4 (ESSENTIAL, p. 6–8, §IV + Fig. 3)**  
The NaMaster “validation” recovers injected \(\beta\) with a worst-case bias of \(0.040^\circ\) that is explicitly called the “systematic floor.” The recovered value \(0.238^\circ\) is therefore not shown to be unbiased at the level of the published \(0.342^\circ\pm0.094^\circ\) (3.6\(\sigma\)) signal. The test is a methods check, not a sky measurement, yet is presented adjacent to the 3.6\(\sigma\) literature value without the required “not directly comparable” qualifier at every juxtaposition.

**P1B-E5 (ESSENTIAL, p. 10–12, §VI + Fig. 4)**  
The spectator-ALP “consistency check” requires \(\sim25\times\) fine-tuning of the misalignment initial condition (\(\theta_i\sim0.1\) vs natural midpoint 0.5) plus \(C_{a\gamma}\gtrsim9\) to reach the observed \(\beta\). The paper states this is “not a distinctive ECH prediction” and occurs identically in GR+ALP. The section therefore demonstrates that the signal is not explained by the ECH framework.

**P1B-E6 (ESSENTIAL, length)**  
20-page article whose every quantitative result is either a null or a standard \(\Lambda\)CDM recovery. PRD does not publish 20-page technical notes whose sole conclusion is “our pipelines behave as expected and we do not claim to test the theory advertised in the title.”

**P1B-M1 (MAJOR, p. 4–5, Table II)**  
\(w_0w_a\) posterior extrapolation (\(+4.3\sigma\), \(-3.6\sigma\)) is presented without a nested-sampling Bayes factor or explicit statement that the point \((w_0,w_a)=(-1,0)\) lies outside the sampled support. The Savage-Dickey ratio is unusable; the claim is therefore unquantified.

**P1B-M2 (MAJOR, p. 18, Table I footnote)**  
The one-sided 95 % upper limits on \(\Delta N_{\rm eff}\) are obtained by post-processing truncation of the CDF. The paper does not demonstrate that the chains have converged in the \(\Delta N_{\rm eff}<0\) tail that is discarded.

**P1B-M3 (MAJOR, p. 9, §V.B)**  
The statement “the \(\Delta N_{\rm eff}\) extension alone does not resolve the Hubble tension” is correct but is presented as a new result when it is the expected outcome of adding one extra parameter to Planck+BAO+SN data.

**P1B-N1–N4 (MINOR)**  
- Repeated “Scope of this paper” blocks are redundant.  
- Fig. 1 corner plot uses getdist thinning without stating the final effective sample size on the figure.  
- Eq. (1) \(\chi^2\) definition omits the explicit statement that the sum is restricted to \(\ell\le1024\).  
- Several arXiv citations lack journal references even when the papers have been published.

**P1B-NIT1–NIT3 (NIT)**  
Minor typos in axis labels, inconsistent use of “full-tension” vs “full tension,” and one duplicated “canonical” in a figure caption.

**Abstract audit (p. 1)**  
Every numerical claim in the front-matter summary (\(\Delta N_{\rm eff}\), \(H_0\), \(\beta\) recovery bias) is traceable to Tables I–II and Fig. 3, but all are null or standard results. The abstract therefore accurately summarizes a null paper; the mismatch is between abstract and title, not abstract and body.

**Bibliography & provenance**  
All cited statistics (Eskilt & Komatsu 3.6\(\sigma\), ACT DR6, etc.) match the referenced abstracts. No stale commit hashes or internal “R37” tags appear in the rendered PDF.

**Summary recommendation: REJECT**

The manuscript is a 20-page technical note whose central results are (i) standard \(\Lambda\)CDM posteriors, (ii) a pipeline bias floor larger than the claimed signal precision, and (iii) an explicit demonstration that the advertised ECH framework is not required to explain any observable. The title and framing are misleading, the length is disproportionate to the incremental content, and the paper contains multiple internal contradictions between claimed scope and delivered analysis. These are not issues that can be repaired by revision; they are fundamental to the submitted work.