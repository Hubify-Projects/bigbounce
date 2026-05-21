# paper4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R23_P4_v1_0_122
**Wall time**: 25.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=95399, completion=1118, total=96517

---

## PAPER-PER-B1 – CE-ResNet metadata now correct (no issue)

The CE-ResNet paper is cited as Jia et al. (2023), “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” arXiv:2210.04168, ApJ 943, 32, DOI 10.3847/1538-4357/aca8aa, authors He Jia, Hong‑Ming Zhu, Ue‑Li Pen.[0]  
These arXiv ID, title, author list, venue, year, and DOI all match the arXiv and journal records exactly; earlier-version fused metadata (wrong initials, page, DOI) are explicitly described as corrected in-text, so there is no remaining citation bug to fix.[0]  
**Classification:** nit (no change required; this item confirms a resolved prior problem rather than a new defect).

---

## PAPER-PER-M1 – Shamir 2022 DESI citation: ID, DOI, journal all consistent

The paper cites “Shamir (2022)… DESI Legacy Survey, ∼1.3×10^6 galaxies, MNRAS 516 2281, arXiv:2208.13866, DOI 10.1093/mnras/stac2372”.[1]  
On arXiv, arXiv:2208.13866 is titled “Analysis of spin directions of galaxies in the DESI Legacy Survey,” author Lior Shamir, with related DOI 10.1093/mnras/stac2372 and the abstract explicitly stating “nearly 1.3·10^6 spiral galaxies” in the DESI Legacy Survey, exactly matching the claimed survey, scale and journal metadata.[1]  
**Issue:** None; this is a correct, non‑fused mapping of arXiv ID, title, author, and DOI.  
**Classification:** nit (explicitly affirmed accurate; no change needed).

---

## PAPER-PER-M2 – Iye et al. 2021 citation is accurate

The manuscript’s Iye et al. reference is “Spin Parity of Spiral Galaxies III – Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations,” ApJ 907, 123 (2021), arXiv:2011.00662, DOI 10.3847/1538-4357/abb3bb.[2]  
The arXiv record for 2011.00662 has exactly this title, author list (Masanori Iye, Masafumi Yagi, Hideya Fukumoto), “accepted and to be published in ApJ” with related DOI 10.3847/1538‑4357/abb3bb, and its abstract states that a Shamir DR8 catalog’s apparent 4σ dipole collapses to σ_D≈0.29 after duplicate removal, exactly matching the textual description.[2]  
**Issue:** None; the paper is correctly identified and summarized.  
**Classification:** nit (verification only).

---

## PAPER-PER-M3 – No fused arXiv ID / graphene in this text (false historical concern)

The graphene “Making Graphene Nano Inductor Using Table Top Laser Engraver” paper is arXiv:2006.02331, physics.app-ph, unrelated to galaxy chirality.[3]  
The current manuscript does not cite arXiv:2006.02331 at all and does not attribute any cosmology content to that ID; this resolves the kind of title/ID fusion error you were worried about from earlier versions, so there is no present citation-chain bug here.[3]  
**Issue:** None in this version; just a cross-check that a known physics ID is not misused.  
**Classification:** nit.

---

## PAPER-PER-m4 – Shamir 2012 & 2020 references appear plausible but not fully rechecked here

The text references Shamir (2012) as a Phys. Lett. B paper on handedness asymmetry with SDSS (arXiv:1207.5464) and Shamir (2020) “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.[2][1]  
While we did not fetch those two arXiv pages in this round, the metadata patterns (author, subject, years and venues) are consistent with how they are cited in Iye et al. (2020/2021) and Shamir’s own DESI paper; nothing in the surrounding citations indicates a fused title/ID problem for these entries.[2][1]  
**Issue:** Not confirmed in this tool pass, but no positive evidence of a mismatch; if you want a full Shamir-2012/2020 line-by-line claim check, that should be scheduled as a separate, deeper audit with those IDs directly fetched.  
**Classification:** minor (scope note about unverified-but-plausible external references, not an error in the present LaTeX).
