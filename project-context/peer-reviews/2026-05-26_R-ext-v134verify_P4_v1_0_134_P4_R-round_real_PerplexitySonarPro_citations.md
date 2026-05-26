# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v134verify_P4_v1_0_134
**Wall time**: 36.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=103176, completion=1401, total=104577

---

## PAPER-PER-B1 — Shamir 2022 DESI citation metadata

Shamir (2022) DESI paper is correctly cited as arXiv:2208.13866 with title “Analysis of spin directions of galaxies in the DESI Legacy Survey,” author Lior Shamir, and MNRAS 516, 2281, DOI 10.1093/mnras/stac2372, matching the manuscript’s claims.[1] No fused or incorrect metadata here; also the description “nearly 1.3×10^6 spiral galaxies” and the DESI Legacy context closely track the abstract and are not overstated.[1] 

**Classification:** minor  
**Fix:** None needed; leave as-is but you could explicitly note that “nearly 1.3×10^6 spiral galaxies” is Shamir’s own phrasing, to make the attribution even clearer.

---

## PAPER-PER-B2 — Shamir 2020 SDSS+Pan-STARRS citation

The paper labels Shamir (2020) as arXiv:2007.16116, SDSS DR8 + Pan-STARRS, with approximately 6.4×10^4 SDSS spirals plus 3.3×10^4 Pan-STARRS galaxies after morphological filtering, in a “parity‑violation multipole framing,” which matches the arXiv title, author, data description, and the stated counts in the abstract.[0] The journal venue (“ApSS, accepted”) and DOI 10.1007/s10509-020-03850-1 aligned to this arXiv ID are correct.[0] 

**Classification:** minor  
**Fix:** None; the metadata and summarized content both match the arXiv record.

---

## PAPER-PER-M1 — CE‑ResNet (Jia et al. 2023) metadata

The CE‑ResNet reference is given with correct arXiv ID (2210.04168), title, author list, ApJ venue, and DOI 10.3847/1538-4357/aca8aa, matching arXiv and the publisher record.[3] The paper’s description of CE‑ResNet as a chirality‑equivariant ResNet trained on GZ1, and the claim that it finds human‑bias‑driven Z/S asymmetry reduced from ~7σ to <1.8σ, are consistent with the abstract and discussion in Jia et al.[3] 

**Classification:** minor  
**Fix:** None; the CE‑ResNet citation and the qualitative description of its result are accurate.

---

## PAPER-PER-M2 — Iye et al. 2021 (spin parity III) citation

The manuscript’s Iye et al. (2021) reference is to their Galaxy Zoo–based null result after correcting “reading direction” bias and removing duplicated objects, which matches the arXiv paper “Spin Parity of Spiral Galaxies III — Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations,” arXiv:2011.00662.[2] The abstract indeed reports a cleaned catalog with σ_D ≈ 0.29 (no large-scale symmetry breaking), and the ApJ DOI 10.3847/1538-4357/abb3bb given in the bib matches the arXiv record.[2] 

**Classification:** minor  
**Fix:** None; the citation and the way the result is summarized are consistent with the source.

---

## PAPER-PER-M3 — Shamir 2020/2022 “2–4% / ~3%” amplitude framing

The paper repeatedly compresses Shamir’s amplitudes into a “~2–4% range” or “~3% asymmetry” language when summarizing the SDSS+Pan‑STARRS and DESI analyses.[0][1] In Shamir 2020, the abstract clearly refers to per‑bin asymmetry amplitudes of ~5–20%, not just ~2–4%; Shamir 2022 DESI notes “nearly 1.3×10^6 spiral galaxies” and reports hemispheric differences that, in parts of the text, are larger than 2–4% in raw counts.[0][1] Treating 2–4% as “the union of the amplitudes” is more of a re‑framing than a literal quote and could mislead a reader into thinking Shamir’s reported bin‑level asymmetries never exceed 4%. 

**Classification:** MAJOR  
**Fix:** Rephrase the Shamir‑amplitude summary to match what the papers actually state, e.g. “Shamir (2012, 2020) reports bin‑level asymmetries of ∼5–20% and fits dipole/quadrupole patterns; in DESI (2022) he reports a hemispheric excess consistent with a dipole detected at P<10⁻⁵.” Make it explicit that your “2–4%” comparator is a chosen, narrower amplitude scale for integrated or effective dipole fits, not Shamir’s literal reported per‑bin asymmetry range.

---

## PAPER-PER-N1 — No blocker‑grade citation issues found

Across the core cosmology‑relevant external papers that are explicitly tied to your main conclusions (Shamir 2020, Shamir 2022 DESI, CE‑ResNet, and Iye et al. 2021), the arXiv IDs, titles, authors, DOIs, and high‑level claims align with the sources; I did not find any fused metadata (e.g., title from one paper combined with a different arXiv ID) or completely incorrect venue/author attributions.[0][1][2][3] There is one MAJOR “amplitude compression” issue (PAPER‑PER‑M3) as above, but no citation‑forensics problems that would qualify as BLOCKER level.  

**Classification:** minor (but global statement)  
**Fix:** State explicitly in your internal change log that v1.0.134’s literature‑comparison section has been checked against arXiv/ADS for Shamir 2012/2020/2022, Jia et al. 2023, and Iye et al. 2021, with no remaining ID/title/author/venue mismatches, and clarify the Shamir amplitude framing as in PAPER‑PER‑M3.
