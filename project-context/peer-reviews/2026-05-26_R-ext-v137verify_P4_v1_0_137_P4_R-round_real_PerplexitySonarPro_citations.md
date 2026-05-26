# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v137verify_P4_v1_0_137
**Wall time**: 32.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=106438, completion=1411, total=107849

---

## PAPER-PER-B1 — Shamir 2022 DESI citation metadata

**Issue (MAJOR).** The bib entry `Shamir:2022DESI` is described in the text as “Shamir 2022 DESI Legacy, MNRAS 516 2281, DOI 10.1093/mnras/stac2372”, which matches the actual paper “Analysis of spin directions of galaxies in the DESI Legacy Survey” (MNRAS 516, 2281, 2022; DOI 10.1093/mnras/stac2372).[1] However, the earlier generic `Shamir:2022` entry is cited as PASJ methodology, and there is a risk of readers confusing the PASJ methods paper with the DESI-Legacy-specific MNRAS analysis if both share the same “Shamir (2022)” label in prose; PASJ and MNRAS venues and content differ.[1]

**Fix.** Ensure the PASJ methods paper and the DESI Legacy MNRAS paper have clearly distinct citation keys and prose labels (e.g., “Shamir 2022 PASJ (methods)” vs “Shamir 2022 MNRAS (DESI Legacy)”), and verify that all in‑text “Shamir (2022)” references that talk about DESI Legacy explicitly cite the MNRAS paper, not the PASJ one.

---

## PAPER-PER-M1 — Shamir 2020 SDSS+Pan-STARRS description

**Issue (minor).** The text states that Shamir (2020, arXiv:2007.16116) analyzes “∼6.4×10⁴ SDSS spirals plus ∼3.3×10⁴ Pan-STARRS galaxies after morphological filtering”, which is consistent with the abstract that quotes “~6.4·10⁴ SDSS spiral galaxies… and ~3.3·10⁴ Pan-STARRS galaxies”.[0] However, calling the SDSS set “spirals” is slightly interpretive: the abstract describes them as “spiral galaxies” but the paper’s methodology section clarifies they’re selected via the Ganalyzer pattern-recognition tool, not an external, independent spiral catalogue.[0]

**Fix.** Slightly soften the wording to “~6.4×10⁴ SDSS galaxies classified as spirals by Ganalyzer and ~3.3×10⁴ Pan-STARRS galaxies” to make clear these are Ganalyzer-selected spiral candidates rather than an externally defined spiral sample.

---

## PAPER-PER-m2 — Jia et al. (CE‑ResNet) metadata

**Issue (minor).** The paper cites Jia et al. with the title “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network” and links it to arXiv:2210.04168 and an ApJ DOI 10.3847/1538-4357/aca8aa; this exactly matches the arXiv and publisher metadata.[2] The in‑text description that CE‑ResNet guarantees equivariance under horizontal reflection and reports CW/CCW imbalance dropping from a ~7σ volunteer bias to <1.8σ with CE‑ResNet is consistent with the abstract.[2]

**Fix.** None required for citation; keep as-is. If you want to be ultra-precise, you could add the explicit ApJ volume/page (“ApJ 943, 32”) in the bibliography for easier lookup, but the DOI+arXiv pair is already correct.

---

## PAPER-PER-m3 — Iye et al. (2021) and arXiv:2011.00662

**Issue (minor).** The manuscript cites Iye et al. (2021) with the title “Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,” matching arXiv:2011.00662 and ApJ 907, 123; the abstract explicitly concludes that a “cleaned” catalogue shows only σ_D ≈ 0.29 and is compatible with random spins.[3] The text’s summary that Iye et al. find no significant signal after dealing with duplication and biases aligns with that conclusion.[3]

**Fix.** None. Citation and interpretation are accurate; just verify that the ApJ volume/page and DOI in your .bib match the arXiv record (ApJ 907, 123; DOI 10.3847/1538-4357/abb3bb).

---

## PAPER-PER-m4 — Galaxy Zoo DESI metadata

**Issue (minor).** The manuscript cites Walmsley et al. (Galaxy Zoo DESI) as “Galaxy Zoo DESI: detailed morphology measurements for 8.7M galaxies in the DESI Legacy Imaging Surveys” with arXiv:2309.11425 and an MNRAS acceptance statement; the arXiv entry indeed has that title and 8.67M galaxies figure.[4] The way the paper uses it—as the source of the 8.7M‑galaxy parent sample and as the origin of the DR8 morphology and selection function—is consistent with the abstract.[4]

**Fix.** None; metadata and usage are correct.

---

## PAPER-PER-n1 — General arXiv/DOI consistency on key cosmology-chirality references

**Issue (nit).** For the main cosmology/chirality anchors (Shamir 2012 ApSS, Shamir 2020 ApSS / arXiv:2007.16116, Shamir 2022 MNRAS 516, 2281; Jia 2023 ApJ 943, 32 / arXiv:2210.04168; Iye et al. 2021 ApJ 907, 123 / arXiv:2011.00662; Galaxy Zoo DESI arXiv:2309.11425), the arXiv IDs, titles, and journals all match their arXiv and publisher records.[0][1][2][3][4] There is no evidence of fused metadata (e.g., mismatched title/ID or venue/ID) for these load‑bearing citations.

**Fix.** None needed; you can explicitly note in your internal checklist that the key arXiv IDs, titles, and venues for these cosmology/chirality references have been cross‑verified against arXiv and, where applicable, the publisher DOIs.
