# P3_v3140_R2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0300pt
**Wall time**: 30.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=57607, completion=1723, total=59330

---

## PAPER-PER-B1 — Heinrich et al. metadata mismatch (MAJOR)

**Location:** Introduction, cosmology paragraph; §5 / §fnl; Appendix references.

**Issue:** The paper cites “Heinrich et al. [Heinrich2023] … Heinrich+2024 σ_fNL ≈ 0.7 … seven-redshift-bin Fisher” as a published external benchmark, but there is no arXiv or journal paper by Heinrich et al. matching that description as of now; this appears to be an internal forecast being treated as a literature result, with no arXiv ID, title, or public venue. The bibliography entry “Heinrich2023” in the TeX is correspondingly under-specified and not mappable to a real, public paper.[1]

**Fix (1–2 sentences):** Recast all “Heinrich+2024” / “Heinrich et al. [Heinrich2023]” mentions as an internal, unpublished Fisher forecast (e.g., “internal calculation following the methodology of Heinrich et al.”) and remove any implication that this is a published external benchmark. In the bibliography, either delete the “Heinrich2023” entry or replace it with a real, citable Heinrich et al. paper with correct authors, title, journal, and arXiv ID.

---

## PAPER-PER-B2 — Cai:2009fn / Brandenberger / Wilson–Ewing IDs (minor)

**Location:** Introduction, sentence “The quasi-matter bounce model predicts … fNL = −35/8 [Wands2010, Cai:2009fn, WilsonEwing2012]”.

**Issue:** The arXiv identifier “Cai:2009fn” is a standard HEP-style tag referring to Cai et al.’s “Non-Gaussianity in a Matter Bounce” (Cai, Xue, Brandenberger, Zhang), which is correctly a matter-bounce non-Gaussianity paper, but the text intermittently treats it as if it were a distinct Brandenberger paper and blends it with Quintin 2014 / Cai 2014 in the later PTA/bounce discussion.[2][3] This is a semantic fusion risk (same arXiv ID, multiple narrative roles) rather than a wrong ID.

**Fix (1–2 sentences):** Make the mapping explicit the first time: “Cai et al. (arXiv:0903.0631, often cited as Cai:2009fn)” and consistently use either the arXiv number or a standard author–year key, not both interchangably. Ensure the BibTeX entry has the correct title (“Non-Gaussianity in a Matter Bounce”) and author list matching arXiv:0903.0631.[3]

---

## PAPER-PER-B3 — Wilson-Ewing 2012 citation form (nit)

**Location:** Introduction and §fnl, references “WilsonEwing2012”.

**Issue:** The cited work is “The Matter Bounce Scenario in Loop Quantum Cosmology”, JCAP 1303:026 (2013), arXiv:1211.6269.[2] The text uses the key “WilsonEwing2012” and phrase “Wilson-Ewing 2012,” which is fine as an internal key, but the year in the author-year style and the year in the journal reference should be clearly 2013 if a journal-year style is used.

**Fix (1–2 sentences):** In the bibliography, ensure the entry gives full metadata: “E. Wilson-Ewing, ‘The Matter Bounce Scenario in Loop Quantum Cosmology’, JCAP 1303 (2013) 026, arXiv:1211.6269.”[2] In the main text, either reference it as “Wilson-Ewing (2013)” or keep “2012” strictly as part of the BibTeX key and not as a publication-year label.

---

## PAPER-PER-B4 — SPHEREx2014 reference is real but incomplete (nit)

**Location:** Introduction, SPHEREx mention; §fnl sensitivity paragraph.

**Issue:** The citation “SPHEREx2014” does correspond to a real paper, “Cosmology with the SPHEREX All-Sky Spectral Survey” (Doré et al., arXiv:1412.4872).[1] However, the current text only labels it as “the SPHEREx satellite” without giving authors, arXiv ID, or a journal/technical-report venue, and the bibliography line in the TeX is skeletal.

**Fix (1–2 sentences):** Expand the bibliography entry to: “O. Doré et al., ‘Cosmology with the SPHEREX All-Sky Spectral Survey’, arXiv:1412.4872.”[1] In the main text, the first mention should explicitly tie “SPHEREx2014” to Doré et al. and, ideally, quote the arXiv ID.

---

## PAPER-PER-B5 — Liang et al. 2023 bib entry is correct but underspecified (nit)

**Location:** Abstract, comparison against “Liang et al. [Liang2023]”; §DESI; §comparison.

**Issue:** The cited work “Outlier Detection in the DESI Bright Galaxy Survey” is a real arXiv paper (Liang et al., arXiv:2307.07664) with a specific author list and scope (DESI BGS outliers).[0] The current text summarizes it correctly (≈250k DESI EDR spectra; 2,685 anomalies; 1.07% rate) but the BibTeX entry should include full metadata and the arXiv ID so external readers can unambiguously trace it.

**Fix (1–2 sentences):** Update the bibliography entry to include the full title, author list, journal status (if any), and arXiv ID: “Y. Liang et al., ‘Outlier Detection in the DESI Bright Galaxy Survey’, arXiv:2307.07664.”[0] Optionally, note in the text that their sample is the DESI BGS subset of EDR to make the comparison axis explicit.

---

## PAPER-PER-B6 — Global bib-audit coverage gaps (minor)

**Location:** Global references to ACT_DR6, NANOGrav2023, eROSITA_DR1, GaiaDR3, Sesana2016, Burke-Spolaor2019, Quintin2014, Cai2014 in text vs. bib list at the end.

**Issue:** Several cited keys are clearly intended to correspond to real and well-known papers (ACT DR6 DR, NANOGrav 15-yr GWB, eROSITA DR1, Gaia DR3, Sesana 2016 SMBHB modeling, Burke-Spolaor 2019 PTA astrophysics, Quintin 2014, Cai 2014), and the textual summaries are broadly consistent with those works, but the snippet of the bibliography in the TeX is truncated and does not show complete metadata for these keys.[0][1][2] This makes it impossible to confirm, from the TeX alone, that each bib entry has the correct title/venue/author list rather than a fused or partial record.

**Fix (1–2 sentences):** For each of these keys, explicitly align the BibTeX entry with the real paper: e.g., ACT DR6 with its ApJ DR6 lensing paper and authors, NANOGrav2023 with Agazie et al. 15-year GWB, Sesana2016 with the MNRAS selection-bias paper, Burke-Spolaor2019 with the A&A Review article, Quintin2014 and Cai2014 with their correct arXiv IDs and journal references.[0][1][2] Then run a cross-check to ensure no title/ID fusions (e.g., SPHEREx title paired with the wrong arXiv) remain.
