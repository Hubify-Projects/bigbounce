# paper4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R24_P4_v1_0_122
**Wall time**: 31.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=95401, completion=1451, total=96852

---

## PAPER-PER-B1 – Shamir 2012 / 2020 / 2022 consistency

**Issue (MAJOR)**  
Lines ~110–150: text says Shamir 2012 used “∼10⁴ SDSS galaxies …” and Shamir 2020 “extended this to ∼10⁵ galaxies from multiple surveys.”[0] In fact, arXiv:2007.16116 uses ∼6.4×10⁴ SDSS galaxies with spectra and ∼3.3×10⁴ Pan-STARRS galaxies (combined ≳10⁵), not merely “extending” the 2012 sample to 10⁵.[0]  

**Fix**  
Rephrase to: “Shamir (2012) analyzed ∼10⁴ SDSS spirals with Ganalyzer. Shamir (2020; arXiv:2007.16116) analyzed ∼6.4×10⁴ SDSS spirals plus ∼3.3×10⁴ Pan-STARRS spirals (≳10⁵ total) and reported ≃3% asymmetries with quadrupole/dipole structure.”[0]

---

## PAPER-PER-M1 – Shamir 2022 metadata & numbers

**Issue (MAJOR)**  
Introduction and comparison sections describe “Shamir 2022 (arXiv:2208.13866, DESI Legacy, ∼1.3×10⁶ galaxies, MNRAS 516 2281)” as DESI Legacy analysis and elsewhere also cite it as “MNRAS 516 2281.” In reality, arXiv:2208.13866 (“Analysis of spin directions of galaxies in the DESI Legacy Survey”) is the DESI Legacy paper and its journal is MNRAS 516, 2281; there is not a separate “Shamir 2022 DESI” paper beyond this.[1] The text sometimes treats “Shamir 2022” and “Shamir 2022 DESI” as distinct comparators, which risks implying two different 2022 papers instead of one paper in both roles.  

**Fix**  
Clarify that Shamir (2022, arXiv:2208.13866, MNRAS 516, 2281) is the *single* DESI Legacy analysis, and use one consistent bib entry for all mentions. Drop the “Shamir 2022 DESI” pseudo-key or map it explicitly to the same bibitem as Shamir:2022.[1]

---

## PAPER-PER-m1 – “Shamir 2022 DESI 1.3M spirals” wording

**Issue (minor)**  
In Sec. 1 the text writes that Shamir 2022 “ran Ganalyzer over ∼1.3×10⁶ Ganalyzer‑analyzed galaxies (the total input sample, NOT the spiral‑classified subsample), of which only ∼200,000 were retained as spirals.” That is consistent with the abstract of arXiv:2208.13866 (“nearly 1.3⋅10⁶ spiral galaxies” per Shamir’s *own* wording), but the parenthetical correction conflicts with Shamir’s claim that those 1.3×10⁶ are spiral galaxies.[1]  

**Fix**  
Make the reinterpretation explicit: “Shamir (2022) describes ‘nearly 1.3×10⁶ spiral galaxies’ in DESI Legacy.[1] Under our re-analysis of his pipeline description, this is better interpreted as ≈1.3×10⁶ *input* galaxies, of which ≈2×10⁵ are actually spirals after Ganalyzer cuts; we adopt that reinterpretation for sample-size comparisons here.”

---

## PAPER-PER-m2 – CE‑ResNet citation details

**Issue (minor)**  
Where CE‑ResNet is introduced (Sec. 1) the paper gives author names and basic description but does not include the ApJ bibliographic details, while the BibTeX later correctly gives ApJ 943, 32 and DOI 10.3847/1538‑4357/aca8aa.[2] That’s fine, but you should ensure that any in‑text parenthetical like “Jia et al. 2023” matches the actual year and venue (ApJ 943, 32, 2023), which is indeed correct.[2]  

**Fix**  
Optionally tighten one first mention to: “Jia et al. (2023, ApJ 943, 32) introduced CE‑ResNet, a chirality‑equivariant ResNet for Z‑wise vs S‑wise spirals.”[2]

---

## PAPER-PER-m3 – Shamir titles & arXiv IDs

**Issue (minor)**  
The text associates (a) arXiv:2007.16116 with “Patterns of galaxy spin directions in SDSS and Pan‑STARRS show parity violation and multipoles” and (b) arXiv:2208.13866 with “Analysis of spin directions of galaxies in the DESI Legacy Survey,” both by L. Shamir.[0][1] These titles, authors, and IDs are all correct; the MNRAS DOI for the DESI paper is correctly given as stac2372.[1]  

**Fix**  
No change required; keep these as they are. If you want ultra‑explicitness, you can state once: “Shamir 2020 refers to arXiv:2007.16116 (Ap&SS 365, 136); Shamir 2022 refers to arXiv:2208.13866 (MNRAS 516, 2281).”[0][1]

---

## PAPER-PER-n1 – Jia 2023 sample size statement

**Issue (nit)**  
The paper says CE‑ResNet “released ∼1.95 million galaxy chirality classifications across the SDSS+DESI imaging footprint,” while Jia et al. describe a classifier trained on SDSS and applied to DESI, but the abstract does not itself state “1.95M classifications” in that exact phrasing.[2] This is plausible but not explicitly quoted from the paper, and could be phrased more clearly as your own catalog‑matching number, not as a direct citation.  

**Fix**  
Rephrase to: “Using the published CE‑ResNet catalog, we find ≈1.95M galaxies with chirality classifications over the SDSS+DESI imaging footprint (our count; Jia et al. 2023 describe the method and release the underlying catalog).”[2]


