# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v138verify_P4_v1_0_138
**Wall time**: 22.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=107353, completion=1001, total=108354

---

## PAPER-PER-B1 – Shamir 2022 DESI citation block

The paper’s Shamir (2022) DESI description matches the real article: arXiv:2208.13866 has title “Analysis of spin directions of galaxies in the DESI Legacy Survey,” is by Lior Shamir, and is published as MNRAS 516, 2281 with DOI 10.1093/mnras/stac2372, exactly as cited here.[0] The abstract also explicitly refers to “nearly 1.3·10^6 spiral galaxies,” consistent with the manuscript’s “nearly 1.3×10^6 spiral galaxies” phrasing.[0] No fused metadata or ID/title/venue mismatch found.  
Fix: None. No blocker-grade issue here.

---

## PAPER-PER-m1 – Shamir 2020 SDSS+Pan-STARRS block

The Shamir (2020) reference is correctly given as arXiv:2007.16116, title “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” author Lior Shamir, published in Ap&SS with DOI 10.1007/s10509-020-03850-1, which matches the arXiv record.[1] The manuscript’s description (“∼6.4×10^4 SDSS spirals plus ∼3.3×10^4 Pan-STARRS galaxies,” parity-violation multipole framing) is also faithful to the abstract.[1]  
Fix: None.

---

## PAPER-PER-m2 – CE-ResNet (Jia et al. 2023) metadata

The CE-ResNet citation is internally consistent: arXiv:2210.04168 has title “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” authors He Jia, Hong-Ming Zhu, Ue-Li Pen, accepted by ApJ with DOI 10.3847/1538-4357/aca8aa, and the paper explicitly discusses a parity-symmetric, chirality-equivariant CNN applied to SDSS/DESI images, matching the manuscript’s description.[2]  
Fix: None.

---

## PAPER-PER-m3 – Iye et al. 2021 Galaxy Zoo bias paper

The Iye–Yagi–Fukumoto paper is correctly cited as arXiv:2011.00662, title “Spin Parity of Spiral Galaxies III -- Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations,” accepted in ApJ with DOI 10.3847/1538-4357/abb3bb.[3] The manuscript’s summary (they re-analyze Shamir SDSS spins, find a 4σ dipole in the raw catalog that collapses to ≈0.3σ after removing duplicates, concluding SDSS data alone do not support large-scale symmetry breaking) matches the abstract.[3]  
Fix: None.

---

## PAPER-PER-m4 – Shamir 2020 vs 2022 usage separation

The text carefully treats Shamir (2020) SDSS+Pan-STARRS and Shamir (2022) DESI Legacy as distinct comparators, not a fused “single Shamir” value, and it explicitly attributes the 6.4×10^4/3.3×10^4 split to 2007.16116 and the ~1.3M DESI input reduced to ~2×10^5 to 2208.13866, which both match the arXiv abstracts.[0][1] The “2–4%” asymmetry range is explicitly described as the union of the two papers’ reported amplitudes, not invented.  
Fix: None; this is correctly de-fused metadata.

---

## PAPER-PER-m5 – No blocker-grade citation errors found

Across the inspected cosmology/morphology references (Shamir 2012/2020/2022, Iye et al. 2021, Jia et al. 2023), arXiv IDs, titles, authors, and journal/DOI metadata all match the authoritative records on arXiv/ADS, and the surrounding prose does not misrepresent what those papers actually claim.[0][1][2][3] There is no evidence of fused titles+IDs, invented venues, or wrong-article citations in these key chains.  
Fix: None; there are currently no blocker-grade or major-grade citation forensics issues in this slice of the paper.


