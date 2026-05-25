# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-25_R-ext_P4_v1_0_128
**Wall time**: 26.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=97833, completion=1712, total=99545

---

## PAPER-PER-B1 – Mis-cited early Shamir 2020 sample size / surveys

**Location:** Introduction, paragraph starting “Shamir (2020) extended this to ∼10^5 galaxies from multiple surveys, reporting asymmetries of ∼3%…”  

**Issue:** Shamir (2020, arXiv:2007.16116) explicitly analyzes ≈6.4×10⁴ SDSS galaxies with spectra and ≈3.3×10⁴ Pan-STARRS galaxies, i.e. ≈9.7×10⁴ total, not “∼10⁵ galaxies from multiple surveys” in the sense of a single combined sample at ~10⁵, and the abstract emphasizes SDSS spectra + Pan-STARRS separately with no single 10⁵-number headline.[0] The text’s wording “extended this to ∼10⁵ galaxies from multiple surveys” is technically close in magnitude but conflates the specific split (SDSS vs Pan-STARRS) and makes it sound like a single ~10⁵ survey-union sample.  

**Severity:** minor  

**Fix:** Rephrase to match Shamir’s numbers and separation, e.g. “Shamir (2020) analyzed ≈6.4×10⁴ SDSS spirals with spectra and ≈3.3×10⁴ Pan-STARRS spirals, i.e. ≈10⁵ galaxies in total, reporting ≈3% asymmetries with a consistent dipole axis.”[0]


## PAPER-PER-M1 – Shamir 2022 DESI sample characterization slightly off

**Location:** Introduction, paragraph beginning “Shamir 2022 (MNRAS 516 2281, DOI 10.1093/mnras/stac2372) describes the analyzed DESI Legacy sample as nearly 1.3×10⁶ spiral galaxies.”  

**Issue:** Shamir 2022 (arXiv:2208.13866) describes the sample as “nearly 1.3·10⁶ spiral galaxies” spun out into two hemispheres, consistent with the quoted phrase, but the parenthetical in your main comparator sentence earlier says “DESI Legacy Survey, ∼1.3×10⁶ galaxies,” without explicitly reiterating that these are already spiral-classified, while your own 3.2M figure is explicitly “spirals.”[1] This can be read as mixing “imaged galaxies” vs “spirals” in a way that slightly muddies the like-for-like nature of the 2.5× factor discussion.  

**Severity:** MAJOR (comparative-statistics clarity; may mislead readers about sample comparability)  

**Fix:** Tighten the wording so both sides are explicitly spiral samples, e.g. “Shamir 2022 analyzes nearly 1.3×10⁶ *spiral* galaxies in DESI Legacy; our 3.2×10⁶ *spiral* catalog is ~2.5× larger, though differences in cuts and classifier mean the samples are not strictly like-for-like.”[1]


## PAPER-PER-m2 – Shamir 2012 citation phrasing vs actual object count

**Location:** Introduction, sentence “Shamir (2012) reported a 2–4σ dipole significance with per-bin asymmetry amplitudes of ∼5–20% using ∼10⁴ SDSS galaxies…”  

**Issue:** Shamir 2012 is based on SDSS data, but the abstract frames the sample as “~10⁴ SDSS spiral galaxies with spectra,” which is more precisely ≈15,158 in the body, while your text uses only “∼10⁴ SDSS galaxies” without “spiral” and without the spectral qualifier.[0] It’s a mild under-specification that could confuse comparisons, especially since you are very precise about spiral-only counts elsewhere.  

**Severity:** minor  

**Fix:** Add the spiral+spectra qualifiers for consistency: “using ∼10⁴ SDSS spiral galaxies with spectra classified by Ganalyzer.”[0]


## PAPER-PER-m3 – Slightly loose paraphrase of Shamir 2020 results

**Location:** Introduction, “Shamir (2020) extended this to ∼10⁵ galaxies from multiple surveys, reporting asymmetries of ∼3% with a consistent dipole axis.”  

**Issue:** Shamir 2020’s abstract emphasizes a statistically significant asymmetry whose magnitude and direction change with direction and redshift; it reports significant quadrupole and dipole/quadrupole alignments, but does not summarize the main result as simply “∼3%” with a “consistent dipole axis” across all redshifts and subsamples.[0] Your paraphrase compresses several nuanced statements (varying asymmetry and quadrupole-dominated fit) into a single clean “3%” plus “consistent dipole axis,” which is directionally correct but a bit over-simplified relative to the actual claims.  

**Severity:** minor  

**Fix:** Loosen the paraphrase to track the abstract, e.g. “reporting statistically significant asymmetries at the few-percent level and dipole/quadrupole alignments whose preferred axis is similar across SDSS and Pan-STARRS.”[0]


## PAPER-PER-n1 – Redundant dual Shamir 2022 entries (Shamir:2022 vs Shamir:2022DESI)

**Location:** Bibliography entries `\bibitem{Shamir:2022}` and `\bibitem{Shamir:2022DESI}` and nearby text in Introduction comparing “Shamir 2022 (arXiv:2208.13866, DESI Legacy Survey, ∼1.3×10⁶ galaxies, MNRAS 516 2281).”  

**Issue:** Both arXiv:2208.13866 and DOI 10.1093/mnras/stac2372 refer to the *same* MNRAS paper “Analysis of spin directions of galaxies in the DESI Legacy Survey.”[1] You currently split this into two bibitems (one as “Shamir 2022” PASJ context, one as “Shamir 2022 DESI” MNRAS), which risks metadata fusion confusion and inconsistent citing (especially since the PASJ paper text suggests a different journal).  

**Severity:** nit  

**Fix:** Collapse to a single bibitem for arXiv:2208.13866 / MNRAS 516, 2281, and clearly distinguish PASJ vs MNRAS Shamir 2022 papers in-text by journal and title, not by reusing the same year tag with different suffixes. Make sure the PASJ reference has its own distinct arXiv/DOI if included.[1]


## PAPER-PER-n2 – Minor wording around CE-ResNet catalog size and footprint

**Location:** Introduction, “Jia et al. (CE-ResNet) … who released ∼1.95 million galaxy chirality classifications across the SDSS+DESI imaging footprint; CE-ResNet has no NS head and all galaxies receive a CW or CCW label.”  

**Issue:** The CE-ResNet paper gives 1,953,246 galaxies and describes the dataset as combining SDSS, Pan-STARRS1, and DESI Legacy pre-imaging, not strictly “SDSS+DESI imaging footprint” as a binary sum.[2] Your description is broadly right in scale and content, but the “SDSS+DESI” phrasing is slightly incomplete (omits Pan-STARRS) relative to Jia et al.’s abstract.  

**Severity:** nit  

**Fix:** Amend to “across SDSS, Pan-STARRS, and DESI Legacy pre-imaging” and keep the 1.95M figure as-is; this aligns exactly with the CE-ResNet catalog description.[2]
