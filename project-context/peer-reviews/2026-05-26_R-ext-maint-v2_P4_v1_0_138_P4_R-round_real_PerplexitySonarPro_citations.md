# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-maint-v2_P4_v1_0_138
**Wall time**: 26.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=107276, completion=1346, total=108622

---

## PAPER-PER-B1 — Wrong journal and year for Shamir (2022)

**Issue (MAJOR)**  
In Sec. 1 and later, Shamir (2022) DESI Legacy is described as “PASJ” in one place and “MNRAS 516 2281” elsewhere; the bib entry `Shamir:2022` is given as PASJ 74 1114 (2022), but the DESI Legacy spin-directions paper is actually an MNRAS article (“Analysis of spin directions of galaxies in the DESI Legacy Survey”, arXiv:2208.13866, MNRAS 516, 2281, DOI 10.1093/mnras/stac2372).[1]  

**Concrete fix**  
Split Shamir’s works cleanly: keep one bib entry for the PASJ paper (if actually used) and a separate, correctly labeled entry for the DESI Legacy MNRAS paper, making all in‑text references to the DESI Legacy analysis point to the MNRAS 516 2281 entry with the correct journal, volume, page, and DOI.[1]

---

## PAPER-PER-B2 — CE‑ResNet metadata partially stale

**Issue (minor)**  
The paper cites Jia et al. (“Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network”) with arXiv:2210.04168 and ApJ 943, 32, DOI 10.3847/1538-4357/aca8aa.[2] The arXiv record confirms this title, arXiv ID, and DOI, but the text notes prior confusion about volume/page and DOI suffix; any residual mention of earlier values (e.g., “ApJ 943 154” or a different DOI suffix) in comments or footnotes would be fused metadata.[2]  

**Concrete fix**  
Search the source for all occurrences of the CE‑ResNet ApJ citation and ensure they consistently use ApJ 943, 32 (2023) with DOI 10.3847/1538-4357/aca8aa and arXiv:2210.04168 in both main text and comments.[2]

---

## PAPER-PER-m1 — Shamir (2020) metadata could be sharper

**Issue (nit)**  
Shamir (2020) is cited as “Shamir (2020) (arXiv:2007.16116, SDSS DR8 + Pan-STARRS, ~6.4×10^4 SDSS spirals plus ~3.3×10^4 Pan-STARRS…, parity-violation multipole framing)”.[3] The arXiv entry confirms the arXiv ID and title “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles”.[3] However, the text compresses this into “parity-violation multipole framing” without giving the explicit paper title once, which makes audit harder.  

**Concrete fix**  
At first mention of Shamir (2020), quote the exact title “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles” alongside arXiv:2007.16116 and then use the shorter paraphrase thereafter.[3]

---

## PAPER-PER-m2 — Explicitly distinguish Shamir (PASJ) vs DESI MNRAS in text

**Issue (minor)**  
The prose often groups “Shamir (2020) and Shamir (2022)” and then immediately talks about DESI Legacy in the same sentence, but the bib entry `Shamir:2022` is PASJ while DESI Legacy is an MNRAS paper (arXiv:2208.13866).[1][3] This is easy to follow for an expert but fragile: a casual reader may not realize that the PASJ methodology paper and the DESI DESI‑Legacy paper are distinct.  

**Concrete fix**  
Standardize wording to “Shamir 2020 (SDSS+Pan-STARRS, ApSS)” and “Shamir 2022 DESI Legacy (MNRAS 516, 2281)” whenever both are mentioned, and ensure the DESI Legacy results always cite the MNRAS / arXiv:2208.13866 entry, while any PASJ analysis references the PASJ bib entry only.[1][3]

---

## PAPER-PER-n1 — Add journal/DOI details for Shamir (2020)

**Issue (nit)**  
For Shamir (2020), the text gives arXiv:2007.16116 but omits the journal and DOI, though the arXiv record shows it is published in Astrophysics and Space Science with DOI 10.1007/s10509-020-03850-1.[3]  

**Concrete fix**  
Extend the Shamir (2020) bib entry to include “Astrophys. Space Sci. 365, 136 (2020), DOI 10.1007/s10509-020-03850-1” and, if space allows, mention ApSS at first textual reference.[3]

---

## PAPER-PER-n2 — Clarify that “parity‑violation framing” in Shamir is a paper title, not internal label

**Issue (nit)**  
The paper notes “parity-violation multipole framing” for Shamir 2020/2022, while Shamir (2020) explicitly frames its title as “parity violation and multipoles”, and Shamir (2022) emphasizes “dipole axis alignment with probability P<10^-5”.[1][3] The current text may read as if “parity-violation framing” is your interpretive label rather than the literal title of one of the cited papers.  

**Concrete fix**  
When first contrasting your scope with Shamir’s, explicitly say “Shamir (2020), titled ‘…parity violation and multipoles’,” to make clear this is the paper’s own wording, then revert to shorter “parity‑violation framing” language later.[3]
