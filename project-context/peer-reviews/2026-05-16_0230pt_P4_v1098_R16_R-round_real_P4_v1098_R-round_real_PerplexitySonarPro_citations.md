# P4_v1098 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0230pt_P4_v1098_R16_R-round_real
**Wall time**: 27.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=83840, completion=1536, total=85376

---

## PAPER-PER-B1 — Wrong Ivezic LSST arXiv mapping (MAJOR)

**Location:** Bibliography entry for Ivezić et al. 2019 LSST paper; surrounding discussion in Sec. \ref{sec:sensitivity} and \ref{sec:future}.  

**Issue:** The bib entry describes the ApJ LSST reference-design paper (ApJ 873, 111; DOI 10.3847/1538-4357/ab042c) but also discusses arXiv:0805.2366 as if it were the preprint of that same article, while 0805.2366 is actually the much older LSST Science Book and not the ApJ reference-design paper.[1] This is fused metadata (journal details from one work, arXiv ID from another).  

**Fix (1–2 sentences):** Explicitly separate the two works: keep the ApJ 873, 111 reference without any arXiv ID, and if you wish to cite the LSST Science Book, add a second bibitem labeled accordingly with arXiv:0805.2366 and no ApJ journal metadata. Clarify in the text that the ApJ paper and the Science Book are distinct references rather than preprint–journal versions of the same work.  

---

## PAPER-PER-B2 — CE-ResNet metadata now correct (no action) (nit)

**Location:** Bibliography: Jia et al. (2023) CE-ResNet entry and related text in Sec. \ref{sec:ceresnet}.  

**Issue:** Earlier rounds flagged possible confabulation around the CE-ResNet paper’s DOI and ApJ volume/page. In this version, the metadata match arXiv:2210.04168 and the published ApJ record: title, authors, journal (ApJ), year (2023), and DOI 10.3847/1538-4357/aca8aa are all correct.[2]  

**Fix (1–2 sentences):** No change needed; this entry is now accurate. You may want to remove the inline “NOTE” comment about prior corrections from the main TeX if the paper is going to a journal, or move it to an internal changelog.  

---

## PAPER-PER-B3 — Shamir 2020 citation and claims consistent (minor)

**Location:** Sec. \ref{sec:intro}, \ref{sec:shamir}, and bibliography entries for Shamir (2012, 2020, 2022).  

**Issue:** The Shamir (2020) and Shamir (2022) citations correctly match arXiv:2007.16116 and the associated Ap&SS/MNRAS publications in both title and author list.[3] The text summarizes their reported dipole amplitudes (“∼2–4 % large-scale dipole amplitude” and “∼3 % asymmetry”) in a way that is qualitatively consistent with Shamir’s description of a few-percent-level asymmetry, though the exact percentage mapping is not one-to-one with any single number in his abstracts.[3]  

**Fix (1–2 sentences):** No bibliographic correction is required. If you want to be maximally literal, you could rephrase “∼2–4 % large-scale dipole amplitude” to “few‑percent (order 1–3 %) asymmetries as reported by Shamir (2012, 2020, 2022)” to emphasize that this is a qualitative summary rather than a direct quotation of a single number.  

---

## PAPER-PER-B4 — Tadaki 2020 metadata accurate (nit)

**Location:** Tadaki et al. 2020 citation in Sec. \ref{sec:intro}, \ref{sec:comparison}, and reference list.  

**Issue:** The paper’s bibcode (2020MNRAS.496.4276T), journal (MNRAS), and arXiv:2006.13544 match the actual HSC-SSP spin-parity paper; the text’s description (“a smaller sample … with HSC‑SSP imaging and likewise found null results”) is faithful to the abstract’s statement that S-wise and Z-wise counts are nearly equal.[4]  

**Fix (1–2 sentences):** No change needed. If desired, you can explicitly add the ApJ/MNRAS volume and page numbers to the bib entry to make it symmetric with how you treat other references.  

---

## PAPER-PER-B5 — Iye 2021 / Iye & Yagi 2026 citations (minor)

**Location:** Citations labelled Iye:2020 and Iye:2026P6 in abstract, Sec. \ref{sec:intro}, \ref{sec:comparison}.  

**Issue:** The Iye et al. 2021 ApJ paper “Spin parity of spiral galaxies III” is correctly described as a null-result Galaxy Zoo–based reanalysis; its bibcode (2021ApJ...907..123I) matches the cited description and year.[5] The newer Iye & Yagi 2026 HSC paper is correctly identified as arXiv:2605.05570 and “in preparation / anticipated” in the narrative, which is accurate for a fresh arXiv posting that may not yet be in a journal.[5]  

**Fix (1–2 sentences):** No change needed. Once the Iye & Yagi 2026 paper is accepted, update its journal/volume/page in the bibitem; until then, keeping it as an arXiv citation flagged as “arXiv preprint” is correct.  

---

## PAPER-PER-B6 — Overall citation-chain status (no remaining blockers)

**Location:** Whole manuscript, with emphasis on external cosmology/cosmography references.  

**Issue:** Aside from the LSST fused arXiv/journal mapping in PAPER-PER-B1, the other sampled citations (Shamir 2020; Jia et al. 2023 CE‑ResNet; Iye et al. 2021; Tadaki et al. 2020) have correct arXiv IDs, titles, authors, and journal metadata that match ADS/arXiv records.[2][3][4][5] I did not find evidence of “metadata fusion” elsewhere (e.g., titles from one paper glued onto another’s arXiv ID or journal).  

**Fix (1–2 sentences):** After fixing the LSST Ivezic entry as in PAPER-PER-B1, you can state to referees that key external citations (Shamir, CE‑ResNet, Iye, Tadaki) have been explicitly cross-checked against arXiv/ADS and that the bibliography contains no remaining known ID/title/venue mismatches.  

---

Do you want me to do a second pass focusing specifically on the ADS / DOI chain for the parity-odd 4PCF and CMB-birefringence papers (Cabass, Philcox, Hou, Eskilt, Komatsu), or is the LSST fused-ID fix enough for your next Houston external review pass?  


