# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-maint_P5_v0_1_32
**Wall time**: 19.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29388, completion=1529, total=30917

---

## PAPER-PER-B1 — Missing external-paper details (Alexander & Yunes 2009)

**Location:** Bibliography entry `\bibitem{AlexanderYunes2009}` and EFT paragraph “Mapping to a physical operator (v0.1.32)”.

**Issue (MAJOR):**  
The paper is correctly titled “Chern–Simons Modified General Relativity,” authors and journal (Phys. Rep. 480, 1 (2009)) and arXiv:0907.2562 are all accurate, so the citation metadata is fine.[1] However, the text implicitly treats it as a generic cosmological-parity reference for environment‑dependent chirality without pointing to specific sections or results; the review is actually broad (parity-violating gravity, cosmology, GW, etc.), not focused on galaxy‑environment chirality, so “Chern–Simons-style coupling in the Alexander & Yunes sense” is a bit too loose as stated.[1]

**Fix:**  
Clarify in the EFT paragraph that Alexander & Yunes is cited specifically as a general review of gravitational parity-violating operators and Chern–Simons couplings, not as a paper predicting environment-dependent spiral chirality; add an in-text phrase like “for general discussion of gravitational parity-violating operators in cosmology, see…” so the scope is not overstated.[1]


## PAPER-PER-B2 — Lue–Wang–Kamionkowski metadata / content match

**Location:** `\bibitem{LueWangKamionkowski1999}` and mapping paragraph citing “cosmological parity-violating interactions”.

**Issue (MAJOR — but already basically correct):**  
The citation metadata are internally consistent: title “Cosmological signature of new parity-violating interactions,” authors A. Lue, L. Wang, M. Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), DOI 10.1103/PhysRevLett.83.1506, arXiv:astro-ph/9812088, all match the actual paper.[2][3] The text describes it as about “cosmological parity-violating interactions” and “chiral-gravitational-wave coupling”, which aligns with the abstract: they study cosmological birefringence and asymmetry between right/left-handed gravitational waves in the CMB.[2][3] No fused or fabricated metadata here.

**Fix:**  
None required at the level of citation forensics; if you want extra precision, you can explicitly note in the main text that Lue–Wang–Kamionkowski focus on CMB polarization and GW chirality as parity-violating signatures, not galaxy-level chirality, to make the analogy nature clearer.[2][3]


## PAPER-PER-B3 — Tempel et al. 2014 FoF catalog description

**Location:** `\bibitem{Tempel2014}` and discussion in §Tempel cross-validation.

**Issue (minor):**  
The metadata for Tempel et al. are accurate: title “Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation,” A&A 566, A1 (2014), arXiv:1402.1350, and the catalog size “588,193 galaxies” with groups/clusters from SDSS DR10 all match the arXiv paper.[4] The description as a modified FoF on SDSS DR10 with flux limit \(m_r \le 17.77\) is also consistent.[4] There is no obvious fabrication or fused ID here.

**Fix:**  
No change needed; if anything, you could add the explicit A&A DOI 10.1051/0004-6361/201423585 for completeness since you already mention DOIs for the parity-violation references.[4]


## PAPER-PER-B4 — Shamir 2022 DESI Legacy asymmetry

**Location:** §“Comparison to Shamir 2022 DESI Legacy” and `\bibitem{Shamir2022DESI}`.

**Issue (minor):**  
Shamir (2022) in MNRAS 516, 2281 (“Asymmetry between galaxies with clockwise and counterclockwise handedness in DESI Legacy Survey data”) indeed reports a few‑percent large-scale handedness asymmetry on \(\sim 1.3\times10^6\) Ganalyzer‑classified galaxies; the title, journal, year, and qualitative claim (2–4% asymmetry) are consistent with the actual paper.[5] There is no sign of an invented title or mismatched arXiv/journal combination.

**Fix:**  
None as far as citation correctness; if you want to tightly match the literature, you can quote his reported asymmetry more precisely (e.g. his best-fit amplitude and significance) and add the explicit arXiv ID used in the MNRAS paper (arXiv:2208.13866).[5]


## PAPER-PER-B5 — Planck 2018 cosmological parameters reference

**Location:** `\bibitem{Planck2018cosmoparams}` and V-Web algorithm step using Planck 2018 cosmology.

**Issue (nit):**  
The citation “Planck 2018 results. VI. Cosmological parameters, A&A 641, A6 (2020)” with arXiv:1807.06209 is accurate; that paper is indeed the Planck 2018 cosmological-parameters release.[6] The use in the text (“compute comoving distance via Planck 2018 cosmoparams”) matches the purpose of that paper; no metadata fusion is present.

**Fix:**  
No fix needed; if you want maximal clarity, you can add the A&A DOI 10.1051/0004-6361/201833910 to mirror the style used for other key references.[6]


## PAPER-PER-B6 — Overall blocker assessment

**Location:** Whole bibliography and inline claims about the specifically checked external papers.

**Issue (BLOCKER check):**  
For the papers the text flags as “foundational” or “load-bearing” and that are explicitly bibliographed with arXiv IDs or DOIs (Alexander & Yunes 2009, Lue–Wang–Kamionkowski 1999, Tempel et al. 2014, Shamir 2022, Planck 2018), the titles, authors, venues, years, and IDs all match the corresponding arXiv/publisher records, and the way they are summarized in the prose is broadly faithful to their actual scope.[1][2][3][4][5][6] I see no fabricated titles, no mismatched arXiv IDs, and no fused metadata (e.g. title from one paper with ID from another) among these checked entries.

**Fix:**  
State explicitly in your internal notes that no blocker‑grade citation forensics issues were found for the checked external references; the remaining tweaks are stylistic precision, not correctness.
