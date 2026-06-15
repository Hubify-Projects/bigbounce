# P2 EXT18 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5a8a1af4 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 121.1s

---

**Referee Report: P2**

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook (Houston Golden)

**Journal:** Physical Review D

**Date of review:** (simulated)

I have examined every page, equation, figure, table, and caption in the rendered PDF. The paper is a 25-page sensitivity recast that imports the Heinrich et al. (2024) Fisher matrix, applies a local-template projection with an ad-hoc overlap factor \(r \approx 0.84\), and performs a closed-form Bayes-factor comparison. It does not contain an independent derivation of the galaxy bispectrum covariance or a new end-to-end simulation pipeline.

### ESSENTIAL findings (paper cannot be accepted without correction)

**P2-E1** Abstract, p. 1 (and repeated in §IV, p. 9)  
The abstract states “realistic range is \(\sim 2.6-5\sigma\)” and “BF \(\approx 9\)–14” as headline results. These numbers appear only after the reader accepts the specific choice \(\sigma_{\rm theory}=1.0\) and the noise-weighted \(r=0.84\) bookkeeping. The body (§VI.C, Table II) shows that BF drops to \(\sim 4\)–7 under the narrower \([-5,+5]\) competitor prior that the authors themselves label “recommended.” The abstract therefore presents an upper-bound result as the primary claim.  
**Required fix:** Rewrite the abstract to state the conservative (narrow-prior, full systematic budget) numbers first, or remove the BF range from the abstract entirely.

**P2-E2** §IV (p. 9) and Table IV (p. 20)  
The headline 5.2–5.5\(\sigma\) (bispectrum-only) and 2.6–5\(\sigma\) (post-systematics) figures are obtained by multiplying the Heinrich et al. \(\sigma(f_{\rm NL})=0.7\) by the single scalar \(r=0.84\) and then adding GR and \(b_\phi\) terms in quadrature. No joint marginalization over the six nuisance parameters that enter the Heinrich Fisher matrix is performed. The paper therefore reports a rescaled conditional uncertainty, not a marginal one.  
**Required fix:** Either perform the joint marginalization or label every quoted significance “conditional on fixing all other parameters at fiducial values.”

**P2-E3** §II.B (p. 4) and Fig. 2 (p. 11)  
The 10 000-sample null-space scan yields a 16th–84th percentile range \(r\in[0.75,0.94]\). The headline numbers use only the median \(r=0.84\). Propagating the full range changes the optimistic significance from 5.5\(\sigma\) to 4.4–6.2\(\sigma\). The abstract and §IV do not carry this interval.  
**Required fix:** Replace every single-number significance with the interval obtained from the 16th–84th percentile of the null-space distribution.

**P2-E4** §VI.C (p. 12) and Eq. (8)–(9)  
The closed-form Bayes factor is derived under a Gaussian likelihood whose variance is taken from the template-corrected Fisher matrix. The same section states that the true posterior is non-Gaussian once the full null-space coefficient scatter is included. The analytic BF values (Table II) are therefore internally inconsistent with the Monte-Carlo validation the authors themselves perform.  
**Required fix:** Replace the analytic BF column with the Monte-Carlo histogram or withdraw the closed-form claim.

### MAJOR findings

**P2-M1** Length vs. contribution (entire manuscript)  
A 25-page “recast” whose only new quantitative step is a 6-dimensional SVD of three benchmark triangles plus a shape-cosine overlap integral exceeds PRD norms for incremental forecast papers. Recommended maximum length after cuts: 12–14 pages.

**P2-M2** §III.B (p. 8) and Eq. (6)  
The noise-weighted central value \(r=0.84\pm0.02\) is obtained with CMB/LSS-motivated weighting. The SPHEREx-specific weighting (scale-dependent bias) gives \(r=0.829\). The two numbers are presented side-by-side without the explicit statement “these two estimators are not directly comparable.” This violates the journal’s requirement for unambiguous significance statements.

**P2-M3** §II.C (p. 6) Assumption (f)  
The claim that the prediction is “robust across the bounce class” is conditioned on “negligible fermion energy density.” No quantitative bound on the fermion fraction is supplied, nor is the resulting shift in \(f_{\rm NL}\) computed. The statement is therefore an unquantified modeling assumption, not a demonstrated robustness result.

**P2-M4** Fig. 3 (p. 11) and Table II (p. 15)  
The landscape plot and Bayes-factor table use different competitor priors for the same “recommended” row. The figure caption does not state which prior was used; the table caption does. A reader comparing the two obtains inconsistent visual and numerical impressions.

### MINOR findings

**P2-m1** p. 1 (author affiliation)  
“Independent Researcher, Los Angeles, California, USA” with a future date “June 13, 2026” is unconventional but not forbidden. Add an institutional e-mail or arXiv identifier for traceability.

**P2-m2** §VIII.A (p. 19)  
The recast of Planck PR4 (\(f_{\rm NL}=-0.1\pm5.0\)) onto the bounce template is performed with the CMB Fisher weighting only. The corresponding LSS weighting result is omitted; it should be shown for completeness.

**P2-m3** Multiple instances of “bookkeeping” language (“\(r\to1\) endpoint,” “abstract headline”)  
These phrases appear in the body text (pp. 12, 14, 15). Replace with standard scientific phrasing (“endpoint of the prior-sensitivity scan,” “upper edge of the reported range”).

### NITs (cosmetic)

- Inconsistent use of “\(\sigma_{\rm eff}\)” vs. “\(\sigma(f_{\rm NL})\)” in Table IV.  
- Fig. 1 caption lists three benchmark points but the plotted curves are continuous; add a legend entry for the continuous function.  
- Reference list contains two preprints with arXiv numbers but no journal status; update if accepted.

### Summary recommendation

**MAJOR REVISIONS**

The manuscript is a technically competent but over-long sensitivity recast whose headline numerical claims rest on conditional uncertainties, a single scalar overlap factor, and an analytic Bayes-factor formula whose assumptions are contradicted by the authors’ own Monte-Carlo tests. The abstract presents the most optimistic numbers without the caveats that appear only later in the text. Until the significance statements are made unambiguously marginal (or explicitly conditional), the length is reduced by roughly half, and the abstract is rewritten to match the conservative results actually demonstrated in the body, the paper does not meet Physical Review D standards for a forecast or methods article.