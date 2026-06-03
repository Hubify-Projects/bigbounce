# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round7
**Wall time**: 13.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=42432, completion=1274, total=43706, search_context_size=low, cost={'input_tokens_cost': 0.1273, 'output_tokens_cost': 0.01911, 'request_cost': 0.006, 'total_cost': 0.15241}

---

## PAPER-PER-B1 — DESIVAST author list / “et al.” placement

**Severity:** minor  

**Location:** Bibliography, `\bibitem{DESIVAST2025}`  

**Issue:** The bibitem lists “H. Rincón, K. A. Douglass, S. BenZvi *et al.*” but the actual author list on ApJ 982, 38 is “H. Rincón, S. BenZvi, K. A. Douglass, T. K. Gaisser, C. Hahn, Y. Hoffman, …” with BenZvi, not Douglass, as second author, and many additional authors beyond the three named.[DESIVAST2025][DESIVAST2025] The “3 + et al.” truncation therefore reorders the first three authors relative to the journal.  

**Fix:** Reorder the explicit authors to match ApJ (“H. Rincón, S. BenZvi, K. A. Douglass, *et al.*”) before the “et al.” so that the shown prefix reflects the true author order.

---

## PAPER-PER-M1 — T-Web DR1 volume-fraction ranges and tracer mix

**Severity:** MAJOR  

**Location:** §X “Concurrent-literature DR1/EDR cosmic-web cross-validation”, paragraph starting “The T-Web DR1 in-footprint volume fractions reported in Ref.~\cite{TWebDESI2026} are …”  

**Issue:** Ullah et al. (arXiv:2604.02463) report environment fractions separately for BGS, LRG, ELG samples and use a cubic 800 Mpc box; the paper here quotes broad ranges “{0.06–0.16, 0.45–0.48, 0.37–0.40, 0.04–0.06} (ranges across the three BGS/LRG/ELG tracer samples)” and then directly compares these to a DR1-all-galaxies V-Web run.[TWebDESI2026] This compresses multiple tables into a single range and glosses over different tracers and redshift cuts, overstating “strong concordance.”  

**Fix:** Replace the single 4-number range with an explicit statement that T-Web fractions are tracer-dependent (quote one tracer explicitly, e.g. BGS) and note that any comparison to the all-spectro V-Web fractions is approximate because of differing samples and volumes.

---

## PAPER-PER-m1 — ASTRA description and “BGS-anchored volume-filling-fraction calibration”

**Severity:** minor  

**Location:** §X, paragraph describing ASTRA-DESI 2026 (“BGS-anchored volume-filling-fraction calibration”)  

**Issue:** Zapata‑Zuluaga et al. (arXiv:2604.01456) state that they calibrate classification thresholds using *GAMA* volume-filling fractions and BGS as the main DESI tracer, not that the calibration is “BGS‑anchored” in the sense implied here.[ASTRADESI2026] The current phrasing can be read as implying ASTRA is a DESI‑BGS‑based calibration standard.  

**Fix:** Rephrase to “ASTRA calibrates classification thresholds using GAMA volume-filling fractions with DESI BGS as the primary tracer” to match the abstract language and avoid implying a DESI‑BGS standard beyond the paper.

---

## PAPER-PER-n1 — Alexander & Yunes and Lue–Wang–Kamionkowski metadata

**Severity:** nit  

**Location:** Bibliography, `\bibitem{AlexanderYunes2009}`, `\bibitem{LueWangKamionkowski1999}`  

**Issue:** The titles, journals, years, and arXiv IDs match the actual papers, but both entries omit arXiv categories and exact page ranges (“1–102” for Alexander & Yunes, “1506–1509” for Lue–Wang–Kamionkowski).[AlexanderYunes2009][LueWangKamionkowski1999] Not wrong, but slightly incomplete versus common cosmology citation style.  

**Fix:** Optionally add page ranges and arXiv categories for completeness; no change needed for correctness.

---

## PAPER-PER-n2 — Tempel 2014 SDSS DR10 group-catalog description

**Severity:** nit  

**Location:** §Tempel cross-validation, first paragraph  

**Issue:** Tempel et al. 2014 describe “flux- and volume-limited” group catalogues but note that the primary FoF catalog on SDSS DR10 is *magnitude-limited* with separate volume-limited subsamples.[Tempel2014] The text here calls it simply “friends-of-friends group catalog … defines environment by FoF group multiplicity,” which is correct but omits that the environment mapping depends on flux-limited selection.  

**Fix:** Add a short qualifier, e.g. “the magnitude-limited SDSS DR10 FoF group catalog of Tempel et al. (with additional volume-limited subsamples), using group multiplicity as an environment proxy.”

---

## PAPER-PER-n3 — Shamir 2022 amplitude comparison wording

**Severity:** nit  

**Location:** §“Comparison to Shamir 2022 DESI Legacy”  

**Issue:** Shamir 2022 finds an asymmetry up to ~4% in some sky regions, not a uniform 2–4% global dipole; the text’s “reported a ~2–4% large-scale asymmetry on ~1.3×10^6 galaxies” compresses position-dependent results into a single number.[Shamir2022DESI]  

**Fix:** Rephrase to “reported local asymmetries up to ~2–4% in some large-scale regions on ~1.3×10^6 galaxies” to better reflect that the signal is spatially structured rather than a single global amplitude.
