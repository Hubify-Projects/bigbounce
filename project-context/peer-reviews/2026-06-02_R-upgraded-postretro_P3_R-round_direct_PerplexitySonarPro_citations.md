# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-postretro
**Wall time**: 28.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79741, completion=1908, total=81649, search_context_size=low, cost={'input_tokens_cost': 0.23922, 'output_tokens_cost': 0.02862, 'request_cost': 0.006, 'total_cost': 0.27384}

---

## PAPER-PER-B1 — Mis-citation / mis-framing of Heinrich et al. 2023 forecast (BLOCKER)

**Location:** Introduction, para 3 (around “multi-tracer methodology of Heinrich et al. [Heinrich2023] … anchored to the Heinrich+2024 σ_fNL ≈ 0.7 bispectrum-only forecast …”)  

**Issue:** The paper cites *Heinrich et al.* “JCAP 2024, arXiv:2311.13082” as giving a **bispectrum-only σ(fNL) ≈ 0.7 SPHEREx forecast**, but the actual paper “Probing primordial non-Gaussianity and general relativity with the SPHEREx galaxy power spectrum” (arXiv:2311.13082, JCAP 05 (2024) 074) is a **power‑spectrum / multi‑tracer** forecast, not the bispectrum‑only SPHEREx bispectrum forecast usually quoted at ~0.7.[Heinrich2023] The paper’s internal “internal Fisher ≈0.07–0.12, 3–10× tighter than the Munchmeyer et al. 2019 consensus σ_fNL ≈0.4–0.9 for SPHEREx-class surveys” is also anchored to those external numbers strongly; given the mis-labeled external anchor, this becomes a fragile chain of comparisons.  

**Fix:** Rewrite the Heinrich et al. citation text in the Introduction and §5 so it correctly describes the 2311.13082 paper as a **multi-tracer power‑spectrum forecast** (with its actual σ(fNL) values) and, if a ≈0.7 *bispectrum-only* SPHEREx forecast is needed, introduce the correct separate bispectrum reference and detach that value from Heinrich+2024. Also make sure the “3–10× tighter” comparison is recalculated or clearly marked as internal-only once the correct external numbers are used.


## PAPER-PER-M1 — Wands 2010 reference does not contain the specific fNL = –35/8 result (MAJOR)

**Location:** Introduction, para 3, citation string “Wands2010,Cai:2009fn,WilsonEwing2012” associated with “quasi‑matter bounce model predicts fNL = −35/8”.  

**Issue:** Wands (2010), “Local non-Gaussianity from inflation” (Class. Quant. Grav. 27, 124002) is a *review* of local non‑Gaussianity in inflationary models and does **not** itself derive the matter‑bounce fNL = −35/8 result.[Wands2010] That specific value is derived in Cai et al. 2009 (JCAP 05 (2009) 011, arXiv:0903.0631) and later bounce‑focused work; Wilson‑Ewing (JCAP 03 (2013) 026, arXiv:1211.6269) is loop‑quantum‑cosmology–focused and does not give that exact number either. Bundling Wands 2010 into the fNL=−35/8 citation string is therefore misleading (“math‑impossible attribution” / pattern‑025).  

**Fix:** Restrict the fNL = −35/8 statement’s primary citation to Cai et al. 2009 (and, if desired, one other bounce‑specific review) and remove Wands 2010 from that particular parenthetical. If Wands 2010 is needed as general background on local non‑Gaussianity, cite it separately where that broader context is discussed, not as support for the specific bounce value.


## PAPER-PER-M2 — NANOGrav15 KDE free-spectrum citation chain is incomplete as written (MAJOR)

**Location:** §5 (Cosmological Applications) and §6 / Appendix PTA-MCMC, discussion of “NANOGrav 15-year HD‑correlated free-spectrum KDE likelihood release (Zenodo 10.5281/zenodo.8060824)” and “NANOGrav 15-year data set: Evidence for a gravitational-wave background”.  

**Issue:** The main text cites “NANOGrav 2023 ApJL 951 L8” as the evidential GWB detection paper and separately mentions a Zenodo KDE dataset with DOI 10.5281/zenodo.8060824. The actual NANOGrav chain/data DOI and the mapping between **Agazie et al. 2023 ApJL 951 L8** and the specific **KDE artifact** are not fully specified; moreover, the free‑spectrum KDE DOI is the data product accompanying a separate methods/data release paper.[NANOGrav2023] As written, a reader cannot trivially confirm that the KDE prior/likelihood used in the Savage–Dickey analysis corresponds exactly to the cited ApJL paper and not another data product.  

**Fix:** Add an explicit bibliographic entry for the **KDE data‑release / free‑spectrum likelihood paper** (the NANOGrav 15yr “KDE Representations of GWB Free Spectra” Zenodo record) and clearly separate that from the ApJL detection paper in the bibliography and in §5/Appendix text. State explicitly: “We use the HD‑correlated free‑spectrum KDE likelihood provided in [DATA‑REF], which accompanies the detection analysis of Agazie et al. 2023 [NANOGrav2023].”


## PAPER-PER-m1 — SPHEREx 2014 citation metadata slightly off (minor)

**Location:** Introduction, SPHEREx reference “SPHEREx2014” and bib entry.  

**Issue:** The canonical SPHEREx design/reference paper is Doré et al., “Cosmology with the SPHEREx All‑Sky Spectral Survey” (arXiv:1412.4872), eventually associated with SPHEREx collaboration white papers; journal metadata varies, but the draft suggests it may be treated as a generic “SPHEREx 2014” reference without clear authorship or venue.[SPHEREx2014] That is serviceable but not precise.  

**Fix:** Ensure the bib entry lists full authorship and arXiv ID exactly as on arXiv (Doré et al., arXiv:1412.4872) and, if a journal / SPIE proceedings version exists and is intended, update the journal/volume/year to match that official version.


## PAPER-PER-m2 — Planck 2018 NG paper mis-cited by generic “Planck2018” tag (minor)

**Location:** Data & cosmology sections where Planck is cited both for CMB maps and for primordial NG constraints (e.g., Planck2018, Planck2018IX).  

**Issue:** The bibliography entry “Planck2018” appears to be the overview paper (“Planck 2018 results. I. Overview and the cosmological legacy of Planck”), whereas specific statements about CMB Gaussianity / non‑Gaussianity and NG constraints ought to cite “Planck 2018 results. IX. Constraints on primordial non‑Gaussianity” (A&A 641, A9 (2020)).[Planck2018][Planck2018IX] In a few places the text collapses these into a single generic Planck2018 citation even when the NG constraints are what is being used.  

**Fix:** Where the text relies specifically on non‑Gaussianity constraints or on the Gaussian nature of the CMB temperature field, change the citation to (or add) the dedicated NG paper (Planck 2018 IX, A&A 641 A9 (2020)), keeping the overview paper only for general Planck / map‑processing statements.


## PAPER-PER-n1 — Minor ADS/arXiv cross-check: Cai 2014 review identification (nit)

**Location:** Long comment block in the TeX preamble and Introduction referencing “Cai2014 = Y.-F. Cai review Sci. China Phys. Mech. Astron. 57, 1414 (Exploring bouncing cosmologies with cosmological surveys)”.  

**Issue:** ADS/arXiv confirm Y.-F. Cai’s review “Exploring bouncing cosmologies with cosmological surveys” is indeed published in *Sci. China Phys. Mech. Astron.* 57, 1414 (2014), arXiv:1405.1369;[Cai2014] the internal note is correct but the bib entry should match the canonical title capitalization and page/issue formatting (e.g., “57, 1414–1430 (2014)” if you want to be fully standard). This is already very close and technically usable, but slightly non‑standard.  

**Fix:** Normalize the Cai 2014 bib entry to match ADS / publisher formatting (full title, full page range). This is purely cosmetic and does not affect scientific content.
