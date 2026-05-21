# paper4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R25_P4_v1_0_122
**Wall time**: 26.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=95347, completion=1750, total=97097

---

## PAPER-PER-B1 – Shamir 2022 DESI sample description

**Location:** Intro, paragraph starting “The Shamir 2022 DESI Legacy analysis…”.

**Issue:** The text states that Shamir 2022 “ran Ganalyzer over ∼1.3×10^6 Ganalyzer-analyzed galaxies (the total input sample, NOT the spiral-classified subsample), of which only ∼200,000 were retained as spirals by Ganalyzer's deterministic decision tree.” In Shamir (2022) the “nearly 1.3·10^6 spiral galaxies” refers to galaxies already labelled as spirals in the working sample; the paper does not document a factor ~6 further cut down to ~200k “retained spirals” as described here, nor is that number traceable in the arXiv or MNRAS versions.[1]

**Fix:** Rephrase to align strictly with what Shamir (2022) claims, e.g. “Shamir (2022) analyzed nearly 1.3×10^6 spiral galaxies in DESI Legacy Surveys as identified by his pipeline” and, if you want to argue about effective spiral counts, mark any smaller “retained” number explicitly as your own re-interpretation with a reproducible derivation, not as a number taken from Shamir.

---

## PAPER-PER-M1 – CE‑ResNet metadata (title/DOI) now correct but history confusing

**Location:** Multiple spots, especially Sec. Introduction around “CE‑ResNet” description and Table comparing Jia et al.

**Issue:** The current citation metadata for Jia et al. matches arXiv:2210.04168 and ApJ DOI 10.3847/1538‑4357/aca8aa (title “Galaxy Spin Classification I: Z‑wise vs S‑wise…”; authors He Jia, Hong‑Ming Zhu, Ue‑Li Pen).[3] However, the text spends several lines explaining earlier wrong combinations of page numbers and DOI suffixes as if those were external problems; that history was due to prior fusing errors in this manuscript, not in the source, and now reads as process noise rather than science.

**Fix:** Keep a single clean citation (arXiv ID, ApJ volume/page, DOI) and delete the narrative about earlier mis‑metadata. It’s not needed for the cosmology argument and will distract a referee looking for factual clarity rather than your previous LLM corrections.

---

## PAPER-PER-M2 – Iye 2021 description slightly off

**Location:** Intro, paragraph starting “Meanwhile, Iye et al. (2021)…”.

**Issue:** Iye et al. (2021) analyse Shamir’s SDSS DR8 catalog and show that duplications plus other issues reduce an apparent ∼4σ dipole down to ∼0.3σ; they do not describe “duplication of photometric objects (e.g., star-forming knots within the same galaxy counted multiple times)” in exactly that phrasing.[4] Their duplications are multiple catalogue entries of the same galaxy (same object ID / position), not subcomponents like “knots” being counted as separate galaxies.

**Fix:** Reword to match their actual claim, e.g. “they also showed that multiple catalogue entries of the same galaxy in Shamir’s sample artificially boost the apparent dipole, and when these duplicates are removed the significance drops to σ_D ≈ 0.29,” and drop the “star‑forming knots” wording unless you can point to text in Iye et al. that uses that specific example.

---

## PAPER-PER-M3 – Shamir (2012, 2020, 2022) significance / sample sizes should match sources

**Location:** Intro paragraph summarizing Shamir 2012, 2020, 2022; also Sec. 7.1 “Shamir (2012, 2020, 2022)”.

**Issue:**  
- Shamir 2020 explicitly uses ∼6.4×10^4 SDSS and ∼3.3×10^4 Pan‑STARRS galaxies (not “∼10^5 from multiple surveys”), and reports quadrupole significance >5σ, >8σ at z>0.15, not just “dipole significance of 2–4σ”.[2]  
- Shamir 2022 clearly says “nearly 1.3·10^6 spiral galaxies” in DESI Legacy and quotes a hemisphere asymmetry and a cosine‑fit dipole with P<10^-5; the manuscript compresses this as “reported asymmetries of ~3% with a consistent dipole axis” and later as a “∼3% asymmetry signal,” which is acceptable as a rough amplitude summary but would benefit from explicit numbers and terminology that match his abstract (hemisphere excess, cosine dipole, P<10^-5).[1]

**Fix:** For each Shamir paper, quote the sample sizes and stated significances in the same form as in the abstracts and clarify whether you are talking about dipole, quadrupole, or hemisphere asymmetry. For example: “Shamir (2020) used 6.4×10^4 SDSS and 3.3×10^4 Pan‑STARRS spirals, finding a quadrupole alignment at >5σ (rising to >8σ for z>0.15),” and similarly make Shamir 2022’s “P<10^-5” and “nearly 1.3·10^6 spiral galaxies” explicit.

---

## PAPER-PER-m1 – Iye VI / arXiv:2605.05570 is 2025, not “(2026)” in the bib label

**Location:** Sec. 7.1, paragraph mentioning “Iye & Yagi (2026) — Iye & Yagi (2026) is anticipated…” and bibliography entry “Iye:2026P6”.

**Issue:** The paper “Spin Parity of Spiral Galaxies VI – A Search for Dynamical Memory in the Spin Distribution of Galaxies in HSC WIDE Survey Regions” is currently on arXiv as arXiv:2505.05570 (May 2025) and is not tagged as a 2026 publication on arXiv or in a journal at this time; the manuscript cites it as “(2026)” with arXiv ID “2605.05570”, which does not exist.[5]

**Fix:** Correct the arXiv ID and year to match the actual posting (e.g. “arXiv:2505.05570 (2025)” if that is the real identifier), and only label it “2026” if/when it receives a 2026 journal publication year, with the appropriate journal reference.

---

## PAPER-PER-n1 – Minor: LSST reference and arXiv ID

**Location:** Bibliography entry for Ivezić et al. LSST paper; discussion in Sec. 9.5 “Future directions”.

**Issue:** The canonical LSST reference‑design paper is ApJ 873, 111 (2019) with DOI 10.3847/1538‑4357/ab042c, and its preprint is arXiv:0805.2366.[6] The text currently has an extended note about earlier confusion and fused metadata; that’s fine, but in at least one place the arXiv ID is dropped entirely and the reference looks like “ApJ 873, 111; the preprint arXiv:0805.2366 cited in earlier versions … is the older LSST Science Book,” which is backwards: arXiv:0805.2366 *is* the preprint of that ApJ article.

**Fix:** Make the reference consistent and minimal: “Ivezić, Ž. et al. 2019, ApJ, 873, 111, arXiv:0805.2366, DOI 10.3847/1538‑4357/ab042c,” and remove or tighten the meta‑discussion about earlier citation mistakes.
