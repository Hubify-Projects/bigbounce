# P4_v1096 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0200pt_P4_v1096_R15_R-round_real
**Wall time**: 20.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=82346, completion=1503, total=83849

---

## PAPER-PER-B1 – Ivezic LSST citation metadata (MAJOR)

**Location:** Bibliography entry for Ivezić et al. 2019 (near end of file, `\bibitem{Ivezic:2019}`).

**Issue:** The bib entry currently mixes the ApJ reference-design paper (ApJ 873, 111, 2019) with the *wrong* arXiv ID and description; arXiv:0805.2366 is the LSST Science Book (large white paper), not the preprint of the ApJ reference-design article.[1] This is exactly the kind of fused “journal article + unrelated arXiv preprint” metadata you are trying to avoid.

**Fix:** Change the entry to cite only the ApJ reference with its correct DOI, and either drop the arXiv ID entirely or replace it with the correct preprint (if there is one). For example, keep: “Astrophys. J. 873, 111 (2019), DOI 10.3847/1538‑4357/ab042c” and remove the 0805.2366 arXiv line, or explicitly state that 0805.2366 is the LSST Science Book if you want to cite that *separately*.


## PAPER-PER-B2 – CE‑ResNet (Jia et al.) metadata (nit)

**Location:** Bibliography entry `\bibitem{Jia:2023}` and scattered in-text references.

**Issue:** The title, journal, year, and arXiv identifier for Jia et al. (CE‑ResNet) appear correct and match ApJ 943, 32 (2023) with arXiv:2210.04168.[2] However, you previously flagged this paper for possible DOI/volume/page confusion; the current bib entry asserts a specific DOI and page mapping without giving the DOI explicitly in the text. Since ApJ DOIs sometimes get mis-copied, this is a potential confabulation point (though I did not see an explicit wrong DOI string in the LaTeX).

**Fix:** Double‑check the DOI against ApJ/ADS (e.g. 10.3847/1538‑4357/aca8aa) and either (a) include the correct DOI explicitly in the bib item, or (b) omit the DOI entirely and keep only journal, volume, page, and arXiv:2210.04168, which are already correct. This is cosmetic, but it closes the previous “fused DOI” concern.


## PAPER-PER-B3 – DESI Legacy Surveys (Dey et al. 2019) metadata (nit)

**Location:** Bibliography entry `\bibitem{Dey:2019}` and first usage in Sec. 2 (Galaxy Images).

**Issue:** The Dey et al. “Overview of the DESI Legacy Imaging Surveys” citation is essentially correct (AJ 157, 168, 2019; arXiv:1804.08657), but the DOI is a common failure mode (sometimes mis‑typed as “ab089b” etc.). ADS confirms 10.3847/1538‑3881/ab089d as the correct DOI.[1]

**Fix:** Verify that your BibTeX/`thebibliography` entry uses exactly DOI `10.3847/1538-3881/ab089d` and arXiv:1804.08657, and that there is no mixed-in or truncated DOI (e.g. missing the trailing “d”). If any older fused DOI is still present in your `.bib` file, correct it to the ADS value.


## PAPER-PER-B4 – Tadaki et al. 2020 HSC‑SSP citation (nit)

**Location:** Bibliography entry `\bibitem{Tadaki:2020}` and discussion in Introduction.

**Issue:** The paper text describes Tadaki et al. as an HSC‑SSP spiral‑spin null result, which matches the real “Spin parity of spiral galaxies II” paper in MNRAS 496, 4276 (2020). However, this object has been a common target of ID/DOI mixups across drafts. I did not see a wrong arXiv or journal ID in your LaTeX, but given the history, this is a residual risk area.

**Fix:** Confirm that the bibline for Tadaki et al. exactly matches ADS (MNRAS 496, 4276, 2020, arXiv:2006.02331, correct DOI), and that you are not accidentally reusing the Iye et al. 2021 arXiv ID (2011.00662) or vice versa. If any mismatch remains in your `.bib`, correct it; if it already matches ADS, no change to the LaTeX is needed.


## PAPER-PER-B5 – SpArcFiRe reference (Davis & Hayes 2014) (nit)

**Location:** Bibliography entry `\bibitem{Davis:2014}` and Sec. \ref{sec:sparcfire}.

**Issue:** The description of SpArcFiRe (ApJ 790, 87, 2014) matches the real paper, but this reference has previously been prone to arXiv mismatches (1407.1452 vs the correct 1402.1910). ADS shows the correct arXiv:1402.1910 for ApJ 790, 87 (SpArcFiRe).[2]

**Fix:** Ensure your bib entry for Davis & Hayes uses arXiv:1402.1910 and not a different 2014 SpArcFiRe‑related arXiv ID. If you currently omit the arXiv ID in the in‑paper bibliography, check the underlying `.bib` to remove any stale 1407.1452 mapping so it doesn’t leak into future versions.


## PAPER-PER-B6 – General fused‑metadata risk note (minor)

**Location:** Multiple places where you explicitly discuss past metadata issues (e.g. LSST, CE‑ResNet, SpArcFiRe notes in the bibliography comments).

**Issue:** The paper embeds meta‑commentary about past incorrect DOIs/IDs and their corrections. This is helpful for internal provenance but can confuse readers and referees, and it increases the risk that an outdated ID (e.g. 0805.2366 for the Ivezic ApJ paper, or an old CE‑ResNet DOI guess) remains somewhere in auxiliary files or BibTeX entries even if the visible LaTeX is now correct.[1][2]

**Fix:** For the arXiv submission version, keep the *correct* concise citations in the main bibliography and, if you really want to document the history, move the “this was wrong in vX.Y” commentary into a short internal changelog or a repository README instead of `thebibliography`. That reduces chances of lingering fused‑metadata errors and makes the citation list cleaner for MNRAS/PRD referees.
