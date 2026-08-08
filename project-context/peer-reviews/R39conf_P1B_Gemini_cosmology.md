# P1B R39conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1b_mcmc_companion.pdf` md5=06410d7c pages=20
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 116.0s

---

**Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"**

**To the Editor of Physical Review D,**

I have reviewed the manuscript "Technical Verification Companion to the ECH Spin-Torsion Program..." by Houston Golden. The paper presents three distinct but related technical analyses that serve as verification material for a larger research program. The analyses are: (1) a stock-CAMB MCMC analysis of the `ACDM+ΔNeff` model, (2) a Monte Carlo validation of a `NaMaster` pseudo-C_ell pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The manuscript is exceptionally well-written, methodologically sound, and demonstrates a high level of scientific rigor and transparency. The authors are commendably careful in defining the scope of each analysis, explicitly stating limitations, and providing detailed discussions of potential systematics and caveats. The level of documentation, particularly concerning reproducibility and the provenance of numerical results, is exemplary and should serve as a model for computational papers in the field. The distinction between pipeline validation figures and sky-measurement significance is maintained with admirable clarity. The caveats regarding fine-tuning in the ALP model are stated upfront and properly quantified.

While the paper is of very high quality, I have identified a few minor points that should be addressed before publication. My findings are detailed below.

---
### Detailed Findings

#### MINOR

**ID: P1B-M1**
*   **Location:** Section III (page 3) and Section V (page 9)
*   **Problem:** The structural organization of the results is slightly counter-intuitive. The `wowa` chain results and their physics interpretation are discussed in detail in Section III (page 4, "Physics interpretation (Table II)") before the main `ACDM+ΔNeff` proxy results are formally presented in Section V.B (page 9, "Results: ACDM+ΔNeff proxy"). While the `wowa` analysis is methodologically separate, presenting its interpretation before the primary proxy results disrupts the narrative flow.
*   **Required Fix:** Consider restructuring to present all MCMC results in Section V, then follow with their interpretations. For instance, a new subsection "V.C: wowa quintom-B diagnostic" could contain the material currently on page 4, following the presentation of the `ΔNeff` results. This would logically group the primary results of the MCMC analyses together.

**ID: P1B-M2**
*   **Location:** Page 5, "Independent cross-validation" paragraph
*   **Problem:** The comparison with Liu et al. [18] states: "their torsion-consistent-with-zero result parallels our `Neff`-consistent-with-zero null finding." While factually correct, this could be slightly misleading. The Liu et al. model is a specific torsion model, whereas the `ΔNeff` run is a generic phenomenological proxy that is not a direct test of any torsion model (as the authors correctly state elsewhere). The parallel is between two different extensions both finding no significant deviation from the standard model, but the physical connection is weak.
*   **Required Fix:** Please rephrase slightly to clarify that the parallel is in the outcome (a null result for a model extension) rather than implying a deep physical correspondence between the two tested models. For example: "Their finding that the torsion parameter is consistent with zero provides a parallel null result in a specific EC model, similar to our finding that the generic `ΔNeff` proxy is consistent with zero."

**ID: P1B-M3**
*   **Location:** Page 16, Appendix C, "Effective sample sizes (ESS)" table
*   **Problem:** The ESS for the `β_free` parameter in the `run3_baseline` chain is 265, which is correctly described in the text as "marginal". For a single-parameter fit, this is indeed low and could affect the stability of the posterior width. While the caveat is present, the quoted uncertainty `±0.10°` might be under-sampled.
*   **Required Fix:** Add a brief sentence acknowledging that while the posterior mean is likely stable, the quoted 1σ uncertainty from this marginal chain should be treated with caution. This reinforces the paper's already high standard of transparency.

#### NIT

**ID: P1B-N1**
*   **Location:** Page 1, Title block
*   **Problem:** The date of the paper is listed as "(Dated: June 13, 2026)". This is a futuristic date.
*   **Required Fix:** Please correct the date to the submission date.

**ID: P1B-N2**
*   **Location:** Page 8, first paragraph of "Robustness battery and bias attribution"
*   **Problem:** There is a minor typographical repetition: "an independent local rerun of the canonical configuration reproduces the pod anchor exactly (β = 0.238°, bias -0.032°). The bias is then unchanged under an apodization-scale sweep...". The phrase "The bias is then unchanged" is slightly abrupt.
*   **Required Fix:** Suggest rephrasing for better flow, for example: "This bias proves to be unchanged under an apodization-scale sweep...".

**ID: P1B-N3**
*   **Location:** Page 11, paragraph "MCMC parameter estimation"
*   **Problem:** The text states "...settles at θi ~ 1.32 ± 0.41 and m ~ 10-10^2 H_0 (posterior median m ≈ 36 H_0) i.e. outside the natural envelope box...". The mass range `10-10^2 H_0` is slightly awkward notation.
*   **Required Fix:** Clarify the notation. Perhaps "m in the range [10, 100] H_0" or similar. The subsequent parenthetical `(posterior median m ≈ 36 H_0)` is clear, but the primary statement could be improved.

**ID: P1B-N4**
*   **Location:** Page 18, Table I caption
*   **Problem:** The caption contains the phrase "agreement at the 0.01σ level". This is likely a typo for "0.1σ level" or refers to the absolute difference being 0.01 times the standard deviation.
*   **Required Fix:** Please verify the intended meaning and correct the text. If the difference is 0.01 absolute units and σ is ~0.009, then the agreement is at the ~1σ level, not 0.01σ. Please clarify.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent and meticulously prepared manuscript. It provides valuable, well-documented technical results with a level of care and transparency that is truly commendable. The claims are appropriately scoped, and the potential pitfalls and limitations of the analyses are discussed with clarity and intellectual honesty. The paper is a significant contribution to the field's methodological literature and, once the minor points above are addressed, will be a strong candidate for publication in Physical Review D.