# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 16.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=42405, completion=1257, total=43662, search_context_size=low, cost={'input_tokens_cost': 0.12721, 'output_tokens_cost': 0.01886, 'request_cost': 0.006, 'total_cost': 0.15207}

---

## PAPER-PER-B1 — Mis-cited DESIVAST authorship

**Type:** MAJOR  

**Location:** Bibliography, `\bibitem{DESIVAST2025}`  

**Issue:** The bibitem lists “H. Rincon, S. BenZvi, K. A. Douglass *et al.*” as authors.[DESIVAST2025] According to arXiv:2411.00148 and ApJ 982, 38 (2025), the correct first author is **H. Rincón** and the lead author list is “H. Rincón, K. A. Douglass, S. BenZvi, M. R. Blanton, Z. Slepian, ...”.[DESIVAST2025][Planck2018cosmoparams] The order of BenZvi and Douglass is reversed in the paper’s citation, and accents are missing.  

**Fix:** Update the DESIVAST bibitem to match ApJ metadata: correct spelling with accent (Rincón), correct first-author list order (Rincón, Douglass, BenZvi, ...), and ensure journal reference (ApJ 982, 38, 2025, doi:10.3847/1538-4357/adb559) matches the ApJ record.[DESIVAST2025]  


## PAPER-PER-M1 — DESIVAST author list inconsistent with in-text shorthand claim

**Type:** minor  

**Location:** §\ref{sec:primary_path}, paragraph beginning “We designate the DESIVAST-anchored void cross-check …”  

**Issue:** The text describes DESIVAST as “Rincon *et al.* 2025” but the bibitem uses “H. Rincon, S. BenZvi, K. A. Douglass *et al.*”, placing BenZvi before Douglass and omitting other early authors like Blanton and Slepian compared to ApJ/ADS metadata.[DESIVAST2025] This is not strictly wrong (et al. covers it) but is needlessly inconsistent with the canonical author ordering.  

**Fix:** Harmonize in-text shorthand and bibitem with the official author ordering from ApJ: keep “Rincón *et al.* 2025” in text and ensure the first three authors in the bibitem follow ApJ order (Rincón, Douglass, BenZvi) before “et al.”.[DESIVAST2025]  


## PAPER-PER-n1 — Minor mismatch to official Tempel+2014 title capitalization

**Type:** nit  

**Location:** Bibliography, `\bibitem{Tempel2014}`  

**Issue:** ADS and A&A list the title as “Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation” with a hyphen in “Flux- and volume-limited” and “catalogues” spelled in British English.[Tempel2014] The manuscript reproduces the wording but there may be small capitalization/spacing differences compared to the journal record (e.g., “Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation” vs “Flux- and volume-limited groups/clusters for the SDSS galaxies: Catalogues and mass estimation”).  

**Fix:** Align the Tempel+2014 title exactly with the A&A version (including hyphenation, capitalization, and “catalogues”) to avoid cosmetic metadata drift.[Tempel2014]  


## PAPER-PER-n2 — DESIVAST title casing

**Type:** nit  

**Location:** §\ref{sec:desivast_primary}, “The DESIVAST DR1 release … title”  

**Issue:** The text gives the DESIVAST title as “DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,”[DESIVAST2025] whereas ApJ uses a lowercase “redshift” (“Low-redshift Voids”) and American spelling “Catalogs”.[DESIVAST2025] The bibitem mostly matches but might differ on the “Data Release 1” phrasing versus the journal’s final capitalization.  

**Fix:** Check the exact ApJ title string and make the in-text and bibitem titles match it character-for-character (including “Low-redshift” and “Catalogs”).[DESIVAST2025]  


## PAPER-PER-n3 — Shamir 2022 title punctuation

**Type:** nit  

**Location:** Bibliography, `\bibitem{Shamir2022DESI}`  

**Issue:** MNRAS and arXiv list the title as “Analysis of spin directions of galaxies in the DESI Legacy Survey” without a trailing period.[Shamir2022DESI] If the manuscript version adds or alters punctuation within the title field, it is technically off from the official record (though this is stylistic rather than substantive).  

**Fix:** Ensure the title in the bibitem matches the MNRAS wording and punctuation exactly; leave the sentence-final period outside the title braces if required by journal style.[Shamir2022DESI]  


## PAPER-PER-n4 — Minor T-Web metadata softening already consistent

**Type:** nit (no change required)  

**Location:** `\bibitem{TWebDESI2026}` and §\ref{sec:tweb_concurrent}  

**Issue:** The paper correctly cites Ullah, Awais, Matos, and Suárez-Pérez, arXiv:2604.02463, and describes it as a “preprint (2026)” and “in submission to MNRAS,” which matches current arXiv status.[TWebDESI2026] No fabrication or fused metadata is evident.  

**Fix:** None needed; this is just a confirmation that the earlier concern about fabricated IDs is resolved and the current metadata matches arXiv/ADS.
