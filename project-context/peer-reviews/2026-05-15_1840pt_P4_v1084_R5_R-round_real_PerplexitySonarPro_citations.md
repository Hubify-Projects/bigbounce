# P4_v1084_R5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_1840pt
**Wall time**: 24.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=76489, completion=1583, total=78072

---

## PAPER-PER-B1 — Shamir 2022 DESI MNRAS metadata (BLOCKER)

**Location:** Intro, comparison sections; bib entry `Shamir:2022DESI`.  

**Issue:** The text claims Shamir’s DESI Legacy spin paper is MNRAS 516, 2281 with DOI `10.1093/mnras/stac2372`, and describes it as “Analysis of spin directions of galaxies in the DESI Legacy Survey.” In ADS this DOI and volume/page indeed correspond to a Shamir paper on DESI spin directions, but you also separately cite “Shamir (2022), PASJ 74, 1114” for a different spin-alignments paper; the narrative occasionally conflates “Shamir (2022)” generically with the DESI paper and with the PASJ paper, risking fused attribution of claims, sample sizes, and survey footprints to the wrong venue.[1]  

**Fix:** Disambiguate consistently: reserve “Shamir 2022 MNRAS (DESI Legacy spin directions, MNRAS 516, 2281, DOI 10.1093/mnras/stac2372)” for the DESI work and “Shamir 2022 PASJ (spin alignment patterns, PASJ 74, 1114)” for the PASJ paper, and ensure each numerical claim (sample size, “nearly 1.3×10⁶ galaxies”, asymmetry amplitude) is tied explicitly to the correct paper and journal in both text and bibliography.[1]  

---

## PAPER-PER-M1 — CE-ResNet citation content (MAJOR)

**Location:** Sec. Introduction, CE-ResNet paragraph; Sec. \ref{sec:ceresnet}; bib `Jia:2023`.  

**Issue:** You state CE-ResNet yields “CW/CCW = 0.998, consistent with parity” and that their catalog “covers a factor of 4 fewer galaxies than the full DESI Legacy footprint.” The CE-ResNet arXiv paper (2210.04168) actually emphasizes that it reduces a human‑induced ≈7σ Z/S excess to <1.8σ and reports a ∼30% increase in both spiral types with DESI images; it does not prominently quote a “0.998” ratio or any simple “factor of 4 fewer than DESI Legacy footprint” statement in those terms, so these look like your derived numbers rather than direct claims from Jia et al.[0]  

**Fix:** Rephrase CE-ResNet discussion to make clear which quantities are your own derived comparisons (e.g. re‑computed CW/CCW ratio, effective footprint fraction) and which are direct results from Jia et al., citing the paper only for the latter (arch-level equivariance, use of GZ1 labels, reduction of human bias), not for numerical ratios they do not explicitly publish in that form.[0]  

---

## PAPER-PER-m1 — SpArcFiRe arXiv/journal linkage (minor)

**Location:** Sec. \ref{sec:sparcfire}; bib `Davis:2014`.  

**Issue:** You now correctly cite SpArcFiRe as ApJ 790, 87 with arXiv:1402.1910, and ADS confirms this mapping. However, one parenthetical note still mentions the earlier erroneous ID “1407.1452” in describing prior corrections, which can confuse readers as to which arXiv entry is actually SpArcFiRe.  

**Fix:** Remove the stray reference to arXiv:1407.1452 or make explicit that 1407.1452 is unrelated and was a previous mistake, and keep only the correct pairing ApJ 790, 87 / arXiv:1402.1910 in the main text and bibliography.  

---

## PAPER-PER-m2 — CE-ResNet DOI / journal metadata (minor)

**Location:** Bib entry `Jia:2023`; surrounding text.  

**Issue:** The arXiv page for 2210.04168 gives the journal as ApJ with DOI `10.3847/1538-4357/aca8aa`, and you reflect that DOI and “ApJ 943, 32” in the text, which matches ADS and arXiv.[0] One parenthetical note about “stale” metadata (e.g. other page/DOI suffixes) is now confusing and could be read as implying there is still doubt about the current citation.  

**Fix:** Keep the clean, correct bib entry only (“ApJ 943, 32, DOI 10.3847/1538-4357/aca8aa”) and remove historical commentary about previous incorrect page/DOI guesses so the present metadata clearly match the actual publication.[0]  

---

## PAPER-PER-m3 — Shamir 2012/2020/2022 grouping (minor)

**Location:** Abstract first paragraph; Intro discussion of “Shamir (2012, 2020, 2022)”.  

**Issue:** You group “Shamir (2012, 2020, 2022)” and quote “2–4% asymmetry, 2–4σ” as if each of those specific numbers applies uniformly across all three papers; in fact, the 2012 Phys. Lett. B paper, the 2020 Astrophys. Space Sci. paper, and the 2022 DESI MNRAS paper report somewhat different nominal amplitudes and significances in different samples and survey combinations.[1]  

**Fix:** Soften the wording to “Shamir (2012, 2020, 2022) report galaxy‑spin asymmetries at the few‑percent level with 2–4σ significances, depending on sample and analysis; here we collectively refer to these as ‘∼3%’ claims” and, where you give a specific number, attribute it to a specific paper and dataset rather than to the grouped citation.[1]  

---

## PAPER-PER-n1 — LSST / Ivezic citation nuance (nit)

**Location:** Sec. \ref{sec:sensitivity}, \ref{sec:future}; bib `Ivezic:2019`.  

**Issue:** You cite Ivezić et al. 2019, ApJ 873, 111 with arXiv:0805.2366 for LSST design; ADS and arXiv confirm that the ApJ article is the reference‑design paper, and 0805.2366 is the long LSST “Science Book”–style preprint from which that article derives.[1] The text is fine, but your note about “plausible‑but‑not‑pure‑identity” may leave readers unsure whether the arXiv ID is actually appropriate.  

**Fix:** Either cite just the ApJ article (873, 111, DOI 10.3847/1538‑4357/ab042c) or clearly indicate “see also the earlier LSST Science Book preprint, arXiv:0805.2366,” so there is no ambiguity that the journal and arXiv records refer to related but not identical texts.[1]  

---

Do you want a second pass focusing only on internal numerical/notation consistency (dipole amplitudes, σ’s, and A vs A/2 conventions), ignoring citations?  


