# P3_v3152_R14 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1500pt
**Wall time**: 26.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=64601, completion=1573, total=66174

---

## PAPER-PER-B1 — Liang et al. citation details

**Class:** MAJOR  

**Location:** Introduction, paragraph 2; abstract, DESI comparison sentences.  

**Issue:** The paper cites Liang et al. as “Liang et al. (2023) … 2,685 anomalies on DESI EDR; 250,000 spectra” which matches arXiv:2307.07664 in scope and numbers, but gives no arXiv ID and may be mis-bibliographed in the unseen `.bib` file. The correct metadata are: title “Outlier Detection in the DESI Bright Galaxy Survey”, authors Yan Liang et al., arXiv:2307.07664, astro-ph.GA. [1]  

**Fix:** In the bibliography entry for `\cite{Liang2023}`, ensure the title, author list, arXiv ID (2307.07664), and subject class (astro-ph.GA) match the arXiv record exactly. Add the explicit arXiv identifier in the main text (e.g., “Liang et al. 2023, arXiv:2307.07664”) at the first mention to make cross-checking trivial.  

---

## PAPER-PER-nit1 — Liang numbers wording

**Class:** nit  

**Location:** Abstract, DESI scaling paragraph.  

**Issue:** The text currently says “Liang et al. (2023) … approximately 250,000 DESI Early Data Release spectra, finding 2,685 anomalies at a 1.07% rate,” and then in the abstract uses “2,685 anomalies on DESI EDR; 378,080/2,685 = 140.8 ≈ 141”. The arXiv paper indeed describes BGS outlier detection in DESI EDR with 2,685 outliers; however, the phrase “on DESI EDR” is loose shorthand for “on BGS spectra from DESI EDR”. [1]  

**Fix:** Tighten the wording to “2,685 outliers in the DESI Early Data Release Bright Galaxy Survey sample” and keep the 250,000 and 2,685 numbers as-is; no change to the ratio arithmetic is needed.  

---

## PAPER-PER-minor1 — Missing explicit arXiv mapping for several key citations

**Class:** minor  

**Location:** Introduction, cosmology paragraph; Section 5 references to Wands, Cai, Wilson-Ewing, SPHEREx, Heinrich, Münchmeyer.  

**Issue:** Several key cosmology papers are cited only via short keys (e.g., `\cite{Wands2010,Cai:2009fn,WilsonEwing2012,SPHEREx2014,Heinrich2023,Munchmeyer2019}`) with no visible arXiv IDs in the LaTeX source. These works do correspond to real papers (e.g., Wands 2010 review on local non-Gaussianity, SPHEREx white paper by Doré et al., Heinrich et al. fNL Fisher forecast, Münchmeyer et al. 2019). However, without explicit arXiv IDs, readers cannot easily verify the claims, and it is easy for titles or IDs to be fused in the unseen `.bib`. [1]  

**Fix:** For each of these central cosmology references, add explicit arXiv IDs in the `.bib` entries and, for at least the first mention of each key work in the main text, add a parenthetical like “(Heinrich et al. 2024, arXiv:2311.13082)” or similar, matching the actual arXiv record. Double-check titles, author order, and venues in the `.bib` against arXiv/ADS before submission.  

---

## PAPER-PER-minor2 — SDSS DR18 citation incompleteness

**Class:** minor  

**Location:** Introduction, first paragraph describing SDSS DR18; Table I caption and survey summary.  

**Issue:** The paper cites SDSS DR18 as `\cite{SDSS_DR18}` but does not show the exact title, author list, or arXiv ID in the provided LaTeX. The real DR18 spectroscopy paper by the SDSS Collaboration (Almeida et al.) has a specific title and arXiv metadata that should be matched exactly; partial or fused metadata in the bibliography would be easy to miss here. [1]  

**Fix:** Confirm that `SDSS_DR18` in the `.bib` matches the official DR18 spectroscopy paper (correct full title, leading author, collaboration, journal, and arXiv ID). Add the arXiv ID in the `.bib` and optionally in a short parenthetical at first mention in the text.  

---

## PAPER-PER-nit2 — eROSITA DR1 citation specificity

**Class:** nit  

**Location:** Introduction, first paragraph; eROSITA section.  

**Issue:** eROSITA DR1 is cited as `\cite{eROSITA_DR1}`, but the text loosely refers to “eROSITA DR1 (X-ray)” without clarifying that the reference is the eROSITA SRG all-sky survey DR1 overview paper by Merloni et al., which has a specific arXiv and A&A reference. Ambiguous or fused DR1 references (mixing catalog paper vs. mission overview) are a common LLM failure mode. [1]  

**Fix:** In the `.bib`, ensure `eROSITA_DR1` points specifically to the DR1 catalog/overview paper you intend (e.g., Merloni et al. A&A DR1 paper) with the correct title and arXiv ID. In the introduction, add a few words clarifying “the SRG/eROSITA all-sky survey DR1 catalog of 930,203 sources” so readers know exactly which DR1 paper is being cited.  

---

## PAPER-PER-minor3 — Table I caption wording “S>5 for three spectroscopic surveys”

**Class:** minor  

**Location:** Table~\ref{tab:survey_summary} caption, footnotes discussing thresholds for DESI, SDSS, and LAMOST.  

**Issue:** The caption currently states that three spectroscopic surveys use a “fixed canonical-$S$ cut at $S > 5.0$,” yet the same caption later explains that SDSS and LAMOST rows show counts at much lower thresholds (e.g., SDSS top-1% at $S \ge 0.1060$; LAMOST top-1% at $S \ge 0.4613$), with only 12 SDSS and 2,054 LAMOST objects above $S>5$. This is internally confusing and could mislead readers about how “S>5 for three spectroscopic surveys” is actually implemented. [1]  

**Fix:** Rewrite the Table I caption line to: “A fixed canonical-$S$ cut at $S>5.0$ is used to define the DESI DR1 headline and the strict high-significance subsets of SDSS and LAMOST; the tabulated SDSS and LAMOST counts use lower percentile cuts as noted in the footnotes.” This keeps the statement true while acknowledging that the tabled numbers for SDSS/LAMOST are not at $S>5$.
