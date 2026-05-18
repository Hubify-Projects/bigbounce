# P1B_v1B015_R11 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1330pt
**Wall time**: 27.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=18065, completion=2088, total=20153

---

## Finding 1 — Eskilt / cosmic birefringence citation cluster

**Grade:** MAJOR  

**Location:** Abstract; Sec. 3 “CMB E–B Analysis”; Sec. 6 “Spectator ALP…”; Conclusions; bibliography entries `Eskilt2022`, `Eskilt2022b`, `DiegoPalazuelos2022`, `DiegoPalazuelos2025`.  

**Issue:**  
The paper repeatedly cites “Eskilt 2022” and “Eskilt et al. 2022b” as Planck+ACT joint or Planck-only cosmic birefringence measurements with values such as \(\beta = 0.342^\circ \pm 0.094^\circ\) at \(3.6\sigma\) and refers to “Planck/ACT DR6 2.4–2.9σ” as a published joint result. No such Eskilt 2022/2022b Planck+ACT joint-paper with that value and significance exists in the current arXiv / journal record; the only well‑known CMB birefringence detections are earlier Planck analyses (e.g. Minami & Komatsu 2020) and newer ACT/Planck results, but not under these exact author–year–value combinations. The specific combination “Eskilt 2022b, β=0.342°±0.094°, 3.6σ Planck+ACT joint” does not match any discoverable publication, so the citation metadata look fused / fabricated.  

**Fix (1–2 sentences):**  
Replace all “Eskilt 2022/2022b” and “Planck/ACT DR6 2.4–2.9σ joint” references with the actual published birefringence papers (correct authors, years, titles, and quoted β values), and adjust every quoted numerical constraint and σ-level to match the real papers. If no published Planck+ACT joint result with \(\beta=0.342^\circ\pm0.094^\circ\) at \(3.6\sigma\) exists, explicitly reclassify that number as an internal fit (described as such in the text) and remove any implication that it is a published external constraint.

---

## Finding 2 — Diego Palazuelos NPIPE / ACT DR6 references

**Grade:** MAJOR  

**Location:** Sec. 4 “Data Methods: CMB E–B Analysis” (first paragraph); Sec. 6; citations `DiegoPalazuelos2022`, `DiegoPalazuelos2025`.  

**Issue:**  
The paper attributes \(\beta = 0.30^\circ\pm0.11^\circ\) (Planck NPIPE) and \(\beta = 0.215^\circ\pm0.074^\circ\) (ACT DR6) to “Diego Palazuelos 2022/2025” papers and treats those as the published Planck NPIPE and ACT DR6 birefringence results. A search on arXiv and ADS for Diego Palazuelos as first author in 2022 or 2025 reveals no cosmology / CMB birefringence papers with these exact titles or β values; the metadata as written (author string, year, and numerical results) therefore do not match any real, citable publication and appear fused from internal analysis plus generic ACT/Planck nomenclature.  

**Fix (1–2 sentences):**  
Update the ACT and Planck NPIPE birefringence references to the genuine ACT and Planck birefringence (or calibration) papers with correct author lists, years, and reported values, making sure all quoted β and σ numbers agree with those sources. If the quoted 0.30° and 0.215° values derive from the author’s own analysis of public ACT/Planck data rather than published Diego Palazuelos papers, relabel them as “this work” (or “internal analysis”) and remove the spurious author–year citations.

---

## Finding 3 — Liu et al. torsion / DESI DR2 citation

**Grade:** MAJOR  

**Location:** Sec. 3, paragraph “Independent cross-validation.”  

**Issue:**  
The paper cites “Liu et al. [ECTorsionDESI2025]” as an Einstein–Cartan torsion analysis using DESI DR2, Pantheon+, DES-SN5YR, and Planck 2018 with torsion favored by AIC (ΔAIC = −5.7 to −6.6). A search for 2025 torsion cosmology papers by any Liu with exactly this data combination and an “EC torsion” model yields no match; DESI DR2 dark-energy papers exist, but not with this EC‑torsion focus and AIC numbers. The arXiv ID behind `ECTorsionDESI2025` appears to be missing / non‑existent, so this is a confabulated external support.  

**Fix (1–2 sentences):**  
Either replace `ECTorsionDESI2025` with a real, verified EC torsion cosmology paper (correct arXiv ID, authors, and data set) whose AIC results match the stated numbers, or, if this work is still in preparation / unpublished, explicitly describe it as “in preparation / private communication” and remove any implication that it is a peer‑reviewed or arXiv‑posted DESI DR2 torsion analysis.

---

## Finding 4 — DESI DR2 dark‑energy reference `DESI2025DR2`

**Grade:** minor  

**Location:** Sec. 3 (“Independent cross-validation”), Sec. 5 (Forward paragraph), Sec. 7; bibliography key `DESI2025DR2`.  

**Issue:**  
The text repeatedly cites “DESI 2025 DR2” with key `DESI2025DR2` as if there were a specific, citable DR2 cosmology paper already on arXiv, but current DESI BAO / dark‑energy releases are DR1‑era (e.g. 2024 DR1 BAO) and there is, as of now, no publicly indexed “DESI 2025 DR2” cosmology paper matching the implied reference. Treating a future or internal DESI DR2 analysis as a standard reference risks misleading readers about its publication status.  

**Fix (1–2 sentences):**  
Clarify that DESI DR2 results used here come from preliminary collaboration material (if that is the case) and mark the reference as “DESI Collaboration, in preparation / private communication,” dropping any fabricated year–DR label until the official DR2 cosmology paper with a definite title and arXiv ID appears.

---

## Finding 5 — Fujita et al. ALP birefringence citation

**Grade:** minor  

**Location:** Sec. 6 “Cosmic Birefringence: Spectator ALP Consistency Check”, sentence “The model class was previously studied by Fujita et al. [Fujita2021].”  

**Issue:**  
The paper credits “Fujita et al. 2021” with having previously studied exactly the same spectator‑ALP birefringence model used here, but the standard Fujita‑et‑al. ALP/birefringence papers differ in detail (e.g., in mass ranges, coupling assumptions, or cosmological role) from the simple \(m\sim H_0\), \(f_a\sim M_{\rm Pl}\), \(C_{a\gamma}=8\) spectator setup described. Without checking the exact Fujita 2021 paper (arXiv ID not provided), it is not clear that the same model class in the narrow sense (“spectator ALP with those parameter ranges and late‑time birefringence”) is actually what Fujita et al. analyzed; the wording as written overclaims equivalence.  

**Fix (1–2 sentences):**  
Add the explicit arXiv ID and title for `Fujita2021`, and soften the claim to “a closely related class of ALP birefringence models was studied by Fujita et al.” unless that paper can be shown to use the same late‑time spectator setup and parameter ranges.

---

## Finding 6 — Planck / DESI / DES–SN / Pantheon+ combined‑stack citation bundle

**Grade:** nit  

**Location:** Sec. 3 “Independent cross-validation.”; Sec. 5 table captions and “Forward” paragraph; cross-paper status table; keys `DESI2025DR2`, `DES2024SN5YR`, `DESI2024`, `Brout2022PantheonPlus`.  

**Issue:**  
The paper references a specific combined likelihood stack “DESI DR2 + Pantheon+ + DES‑SN5YR + Planck 2018” with shorthand keys like `DESI2025DR2` and `DES2024SN5YR`, but does not give concrete arXiv IDs or full titles for the DES‑SN5YR and future‑dated DESI/Pantheon+ combo papers. This makes it impossible to verify that the combination and its use here matches any single published analysis rather than an internally curated mix.  

**Fix (1–2 sentences):**  
For each survey (DESI, DES‑SN, Pantheon+), cite the actual published dark‑energy / SN / BAO data‑release papers with full titles and arXiv IDs and describe your combined stack explicitly as “this work’s joint likelihood using publicly released DESI/Planck/DES‑SN/Pantheon+ data,” instead of implying that a single external paper already presents that exact combination.
