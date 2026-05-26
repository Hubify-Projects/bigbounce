# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v133verify_P4_v1_0_133
**Wall time**: 36.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=101932, completion=1480, total=103412

---

## PAPER-PER-B1 – Shamir (2022) DESI sample size / spiral count

**Section/lines:** Introduction, Shamir paragraph; later catalog comparison paragraph.

**Issue:** The paper states Shamir (2022) DESI Legacy is “∼1.3×10^6 input galaxies reduced to ∼2×10^5 after Ganalyzer cuts” and elsewhere describes that paper as “nearly 1.3×10^6 spiral galaxies.” These are inconsistent with Shamir (2022), which explicitly says “nearly 1.3×10^6 spiral galaxies” are used in the analysis, not that they are reduced by Ganalyzer to ∼2×10^5 spirals.[1]

**Severity:** MAJOR

**Fix:** Harmonize all mentions to match Shamir’s own description: that the DESI Legacy sample contains nearly 1.3×10^6 spiral galaxies, and only use “∼2×10^5 after Ganalyzer cuts” if you can point to a specific table or statement in that paper; otherwise drop that reduced-count claim or clearly label it as your own reconstruction, not Shamir’s wording.[1]


## PAPER-PER-M1 – Shamir (2020) metadata and amplitude summary

**Section/lines:** Introduction, Shamir (2012/2020) discussion.

**Issue:** The text summarizes Shamir (2020) as “∼6.4×10^4 SDSS spirals plus ∼3.3×10^4 Pan-STARRS galaxies after morphological filtering, parity-violation multipole framing” and “∼3% asymmetries.” Shamir (2020) indeed uses ~6.4×10^4 SDSS and ~3.3×10^4 Pan-STARRS galaxies and presents parity-violating dipole/quadrupole patterns, but the abstract emphasizes quadrupole alignments at >5σ–8σ rather than a single ~3% asymmetry value.[1] Your text could be read as attributing a specific “∼3%” amplitude to that paper when the quoted 2–4%/3% range is your union/summary across multiple Shamir works.

**Severity:** minor

**Fix:** Clarify that the 2–4% / ~3% asymmetry range is your synthesized amplitude range across Shamir 2012/2020/2022, not a single quoted value from Shamir (2020); e.g., “Shamir’s reported asymmetries lie at the few-percent level (2–4%) across these works” and keep the individual- paper descriptions closer to the arXiv abstracts.[1]


## PAPER-PER-m2 – Jia et al. (2023) CE-ResNet metadata

**Section/lines:** CE-ResNet paragraph in Introduction and comparison table.

**Issue:** You cite Jia et al. (2023) with title “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” authors Jia, Zhu, Pen, ApJ 943, 32, DOI 10.3847/1538-4357/aca8aa, and describe a catalog of 1.95M galaxies from DESI pre-imaging with CE-ResNet, which reduces a 7σ human bias to <1.8σ.[2] This matches the arXiv record and abstract.[2]

**Severity:** nit (no correction needed)

**Fix:** None needed. If you want to be maximally precise, you can mirror the “Z-wise vs S-wise” terminology explicitly when first introducing CW/CCW equivalence and note that their 7σ→<1.8σ bias reduction is for the Galaxy Zoo–labelled SDSS DESI sample as stated in their abstract.[2]


## PAPER-PER-m3 – Dey et al. (2019) DESI Legacy Surveys citation

**Section/lines:** Data §2.1, DESI Legacy DR8 description; bibliography.

**Issue:** You reference Dey et al. (2019) “Overview of the DESI Legacy Imaging Surveys” and describe DR8 as combining BASS+MzLS, DECaLS, and DES overlap, with nearly uniform-depth strategy and public catalogs; this matches arXiv:1804.08657 and its AJ paper.[3] The author list, title, and venue are correct.[3]

**Severity:** nit

**Fix:** None. Optionally add the AJ volume/page (AJ 157, 168) exactly as in the ADS entry for extra clarity, but the current metadata (arXiv + DOI 10.3847/1538-3881/ab089d) is already accurate.[3]


## PAPER-PER-m4 – Walmsley et al. (2023) Galaxy Zoo DESI metadata

**Section/lines:** Data §2.1 and references to Galaxy Zoo DESI.

**Issue:** You cite Walmsley et al. (2023) as a Galaxy Zoo DESI morphology catalog of ~8.7M galaxies and 19,000 deg² coverage; this matches arXiv:2309.11425 (“Galaxy Zoo DESI: Detailed Morphology Measurements for 8.7M Galaxies in the DESI Legacy Imaging Surveys”), with subject and context correctly reproduced.[4]

**Severity:** nit

**Fix:** None required. If you want, align your “8.67 million” and “19,000 deg²” numbers exactly to their abstract phrasing, but you’re already consistent within rounding.[4]


## PAPER-PER-m5 – Shamir (2020/2022) arXiv IDs, titles, DOIs

**Section/lines:** Bibliography entries for Shamir (2020) and Shamir (2022 DESI); Introduction citations.

**Issue:** You give arXiv:2007.16116 with title “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles” and note a related DOI 10.1007/s10509-020-03850-1 in Ap&SS; this matches arXiv and the linked journal record.[1] For Shamir (2022) DESI you cite arXiv:2208.13866, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” and DOI 10.1093/mnras/stac2372 in MNRAS, which also matches.[1]

**Severity:** nit

**Fix:** None needed; these IDs, titles, authors, and DOIs are correct. You might delete outdated notes like “methods paper; DESI Legacy spin-directions is cited separately” if those are remnants of earlier versions and no longer apply, but they are not factually wrong.
