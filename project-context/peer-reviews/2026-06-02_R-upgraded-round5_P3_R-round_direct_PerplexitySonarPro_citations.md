# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 16.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79619, completion=1436, total=81055, search_context_size=low, cost={'input_tokens_cost': 0.23886, 'output_tokens_cost': 0.02154, 'request_cost': 0.006, 'total_cost': 0.2664}

---

## PAPER-PER-B1 — Mis-cited ACT DR6 reference

**Level:** MAJOR  

**Location:** Bibliography entry `ACT_DR6` near end; multiple references in main text (e.g. abstract, §3.1, Appendix \ref{sec:act_appendix})  

**Issue:** The paper cites “F. J. Qu et al. (ACT Collaboration), *The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth*, ApJ 962, 112 (2024)” as the ACT DR6 reference. The actual ACT DR6 lensing paper is by Madhavacheril et al., not Qu et al., and the title, first author, and details in your citation do not correspond to a real ACT DR6 publication. This looks like fused / confabulated metadata.  

**Fix:** Replace the ACT DR6 citation with the correct ACT DR6 reference from arXiv/ADS (proper first author, title, journal/DOI) and ensure that all `\cite{ACT_DR6}` instances point to the corrected BibTeX entry.  

---

## PAPER-PER-M1 — Heinrich et al. 2023 / 2024 naming inconsistency

**Level:** MAJOR  

**Location:** Intro, lines around “…Heinrich et al. \cite{Heinrich2023} (anchored to the Heinrich+2024 σ_fNL ≈ 0.7 bispectrum-only forecast…)”; §5 and conclusions where “Heinrich+2024” is called the “anchor σ_fNL ≈ 0.7”  

**Issue:** The paper consistently uses a single BibTeX key `Heinrich2023` for “Heinrich et al.” but refers in prose to “Heinrich+2024” as the σ_fNL≈0.7 SPHEREx bispectrum forecast anchor. ADS/arXiv show a JCAP 2024 paper (arXiv:2311.13082) whose bibliographic year is 2024, not 2023. Using a 2023-style key while calling it “Heinrich+2024” in text is internally inconsistent and makes it hard to verify which paper is meant.  

**Fix:** Rename the BibTeX entry to match the actual publication year (e.g. `Heinrich2024`) and update all citations accordingly, or explicitly state in a footnote that `Heinrich2023` refers to the JCAP 2024 paper (arXiv:2311.13082) to avoid confusion.  

---

## PAPER-PER-m2 — SPHEREx arXiv / mission reference mismatch

**Level:** minor  

**Location:** Intro, sentence “SPHEREx satellite \cite{SPHEREx2014}”; bibliography entry for SPHEREx  

**Issue:** The text refers to “SPHEREx 2014” but the canonical SPHEREx mission white paper is generally cited as Doré et al. 2014/2016 (arXiv:1412.4872) and some later survey design papers. The BibTeX key and year should unambiguously map to a real SPHEREx reference; if you are relying on arXiv:1412.4872 as in other rounds, the current “2014” label is fine, but make sure the bibliographic metadata (authors/title/journal) exactly match that arXiv entry and not a hybrid of later mission summaries.  

**Fix:** Double‑check the SPHEREx BibTeX against arXiv:1412.4872 (or the intended mission paper) and correct title / authors / year so that `\cite{SPHEREx2014}` points to an actually verifiable document.  

---

## PAPER-PER-n3 — Mismatched description of Munchmeyer et al. forecast range

**Level:** minor  

**Location:** Intro, “Münchmeyer et al. \cite{Munchmeyer2019} consensus σ_fNL ≈ 0.4–0.9 for SPHEREx-class surveys”  

**Issue:** The Munchmeyer et al. 2019 paper is about kSZ tomography forecasts; it is not itself a SPHEREx forecast paper and does not quote σ_fNL≈0.4–0.9 for SPHEREx-class surveys in that form. That σ_fNL range appears to be a secondary summary, not a direct claim from the cited paper.  

**Fix:** Rephrase to attribute correctly, e.g. “...roughly in the σ_fNL ≈ 0.4–0.9 regime for SPHEREx-class surveys (as summarized in [ref])” or replace with a SPHEREx‑specific fNL forecast citation that actually states that range.  

---

## PAPER-PER-n4 — Slightly fused description of NANOGrav free-spectrum dataset

**Level:** minor  

**Location:** §5 and Appendix \ref{app:pta_mcmc}, description of “NANOGrav 15-year HD-correlated free-spectrum KDE likelihood release (Zenodo 8060824; 30 Fourier-frequency bins; Ceffyl-compatible KDEs)”  

**Issue:** The NANOGrav 15‑yr GWB analysis did release free-spectrum products and Ceffyl-compatible KDEs, but the exact naming (“HD‑correlated free-spectrum KDE pack”) and structure (30 bins, product naming, etc.) should match the Zenodo record. There is a risk of fused terminology from NANOGrav + Ceffyl/PTArcade docs, even if numerically consistent.  

**Fix:** Cross‑check the exact dataset name and description on Zenodo (ID 8060824) and adjust wording to match the official record (e.g. correct product name and number of frequency bins), keeping your methodological description but clearly separating your notation from the dataset’s title.  

---

## PAPER-PER-n5 — Ambiguous “ACT DR6 lensing” scope vs. citation

**Level:** nit  

**Location:** ACT references in §3, §4.5, Appendix \ref{sec:act_appendix}  

**Issue:** The main text treats ACT DR6 mostly as a temperature-map source for CMB patches, but the (incorrect) ACT citation is framed as a DR6 *lensing* power-spectrum paper. Lensing and temperature analyses are distinct data products; tying your ACT use case to a (mis-cited) lensing paper is misleading.  

**Fix:** Once the ACT citation is corrected (PAPER-PER-B1), adjust the prose to describe ACT simply as providing DR6 temperature maps (or intensity maps) unless you actually use lensing reconstructions; reserve the lensing reference for contexts where lensing is relevant.
