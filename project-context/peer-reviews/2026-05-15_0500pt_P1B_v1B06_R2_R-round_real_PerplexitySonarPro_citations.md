# P1B_v1B06_R2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0500pt
**Wall time**: 79.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=13299, completion=1437, total=14736

---

## PAPER-PER-B1 — Liu torsion cosmology metadata (MAJOR)

Issue: The paper cites “Liu 2025 ECTorsionDESI2025 arXiv:2507.04265” as “Liu et al. constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6).” This matches the real paper “Torsion cosmology in the light of DESI, supernovae and CMB observational constraints” (Liu et al.) with arXiv:2507.04265, DESI DR2 BAO + PantheonPlus + DESY5 + Planck 2018, and ΔAIC improvements ≈ −5.68 to −6.62, but the in-text label “ECTorsionDESI2025” is an internal nickname and not the published title or arXiv label.  
Fix: Clarify the bibliography entry and first mention to use the real title and a neutral tag, e.g. “Liu et al. (2025), ‘Torsion cosmology in the light of DESI, supernovae and CMB observational constraints’ (arXiv:2507.04265), hereafter Liu+25-DESI-torsion,” and drop or relabel “ECTorsionDESI2025” wherever it appears.

---

## PAPER-PER-B2 — Diego-Palazuelos Planck NPIPE birefringence (MAJOR)

Issue: The paper quotes “β = 0.30° ± 0.11° (Planck NPIPE)” and attributes it to “DiegoPalazuelos2022,” pointing at the Planck DR4 cosmic birefringence analysis by Diego-Palazuelos et al. (arXiv:2201.07682), whose abstract indeed reports β = 0.30 ± 0.11 (68% C.L.), but the arXiv and journal metadata refer to “Cosmic Birefringence from Planck Data Release 4,” not specifically “NPIPE,” and NPIPE is one of the data products used.  
Fix: Keep the numerical value but adjust wording and bib entry to “Cosmic Birefringence from Planck Data Release 4 (Planck DR4/NPIPE; Diego-Palazuelos et al. 2022, arXiv:2201.07682)” so the title and data tag match the actual paper.

---

## PAPER-PER-B3 — Eskilt joint Planck+ACT headline value (minor)

Issue: The paper cites “Eskilt 2022b” for the joint Planck+ACT value β = 0.342° ± 0.094° (3.6σ) and treats it as the primary headline result; this matches the published joint analysis by Eskilt et al. that combines Planck PR4 and ACT DR6 with shared calibration systematics, but the internal label “Eskilt2022b” must consistently correspond to that specific joint paper (and not to the Planck-only or ACT-only analyses) in the .bib entry.[1]  
Fix: Ensure the .bib entry for “Eskilt2022b” has the correct title, author list, year, and arXiv ID for the joint Planck+ACT cosmic birefringence paper, and verify that “Eskilt2022” and “Eskilt2022b” are not swapped between Planck-only and joint analyses.

---

## PAPER-PER-B4 — Diego-Palazuelos ACT DR6 citation (minor)

Issue: The text uses “DiegoPalazuelos2025” for ACT DR6 birefringence (β = 0.215° ± 0.074°), but the real ACT DR6 birefringence analysis is by Diego-Palazuelos et al. using ACT DR6 polarization data and is more naturally associated with the same author group as the Planck DR4 paper; any mismatch between “2025” in the key and the actual publication year or arXiv date would be fused metadata.[1]  
Fix: Check that the ACT DR6 birefringence paper’s real year and arXiv ID are used in the .bib entry (e.g., 2024–2025), and, if the year in the key is wrong, rename the key to something neutral like “DiegoPalazuelos_ACTDR6” and correct the year in both text and bibliography.

---

## PAPER-PER-B5 — Cai:2009fn / matter-bounce reference (nit)

Issue: The paper’s discussion of the matter-bounce class and non-Gaussianity likely points to Cai et al. (or Brandenberger and collaborators) but the ADS/arXiv record arXiv:0903.0631 is “Non-Gaussianity in a Matter Bounce” without “Cai” as first author; using a label like “Cai:2009fn” for arXiv:0903.0631 would fuse an author-based tag with a Brandenberger-only paper.  
Fix: Align the in-text label and .bib entry: either cite arXiv:0903.0631 correctly as “Brandenberger 2009, ‘Non-Gaussianity in a Matter Bounce’” or, if “Cai:2009fn” is intended, point it to the appropriate Cai et al. matter-bounce paper with the correct arXiv ID.

---

## PAPER-PER-B6 — Cross-paper Eskilt / Diego-Palazuelos consistency (nit)

Issue: The paper’s cross-paper status table and conclusions reference Eskilt and Diego-Palazuelos results across P1A–P4; any inconsistency in which numeric values (0.30°, 0.215°, 0.342°) are labeled “headline,” “auxiliary,” or “Planck/ACT DR6 2.4–2.9σ” versus “3.6σ joint” risks cross-paper confusion even though each underlying value matches its source.[1]  
Fix: Add a one-sentence cross-paper convention (e.g., “Across P1–P4 we adopt Eskilt et al. joint Planck+ACT β = 0.342° ± 0.094° as the headline value; Planck DR4/NPIPE β = 0.30° ± 0.11° and ACT DR6 β = 0.215° ± 0.074° are used only for auxiliary checks”) and ensure all four papers use the same hierarchy and labels.
