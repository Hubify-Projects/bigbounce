# P2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict-v3_P2_v1_7_37
**Wall time**: 16.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33389, completion=1390, total=34779

---

## PAPER-PER-B1 – Mis-cited Cai et al. arXiv ID

**Location:** Multiple places where “Cai et al. 2009” is referenced, starting abstract first sentence and Sec. 2 bispectrum benchmark, with BibTeX key `Cai:2009fn`.

**Issue:** The paper clearly intends the matter-bounce non-Gaussianity calculation “Non-Gaussianity in a Matter Bounce,” which is arXiv:0903.0631, but the arXiv ID is not explicitly given and must match this reference; any other 2009 Cai ID would be wrong and would break cross-checks against arXiv/ADS.[1]

**Fix:** Explicitly ensure the bibliography entry `Cai:2009fn` corresponds to arXiv:0903.0631 with the correct title “Non-Gaussianity in a Matter Bounce” and correct author list/venue, and add the arXiv ID in the text or references to make this unambiguous.[1]

---

## PAPER-PER-m1 – Missing explicit metadata for Cai et al. 2009

**Location:** Abstract first sentence and Sec. 2 (“Cai et al. 2009”; “Cai et al. [\cite{Cai:2009fn}]”) but no explicit metadata in the provided LaTeX snippet.

**Issue:** For a forensic citation chain, the title, authors, and year for the key bispectrum source should be visible in the .tex, but here only a key `Cai:2009fn` appears and the explicit bibliographic line isn’t shown; this makes it harder to verify that the cited work is indeed the 2009 matter-bounce non-Gaussianity paper on arXiv:0903.0631.[1]

**Fix:** In the `.bib` file, set `Cai:2009fn` to “Yi-Fu Cai, Taotao Qiu, Robert Brandenberger, Xinmin Zhang, ‘Non-Gaussianity in a Matter Bounce’, JCAP 03 (2011) 003, arXiv:0903.0631 [astro-ph.CO]”, and optionally mention “Cai et al. (JCAP 2011, arXiv:0903.0631)” once in the main text.[1]

---

## PAPER-PER-m2 – Unspecified metadata for Cai & Brandenberger 2014

**Location:** Assumptions subsection (discussion of factor-of-two; “Cai & Brandenberger [\cite{CaiBrandenberger:2014}] obtain \(\fnl = -35/16\)”), and Appendix A.

**Issue:** The source “Cai & Brandenberger 2014” is central to the claimed convention discrepancy and should map to a specific arXiv ID and title, but this is not shown in the snippet; without clear metadata it is hard to externally verify the asserted factor-of-two relationship and the claim that \(-35/16\) is a single-time-ordering result of the same bispectrum calculation.[1]

**Fix:** Ensure the BibTeX entry for `CaiBrandenberger:2014` contains the correct title, arXiv ID, and journal reference (and that it is indeed a paper where those authors report \(\fnl=-35/16\) for a matter bounce), and add a parenthetical “(Cai & Brandenberger, YEAR, arXiv:XXXX.YYYY)” at first mention to make the target paper easy to audit.[1]

---

## PAPER-PER-m3 – Unspecified metadata for Wilson–Ewing model reference

**Location:** Introduction (paragraph “The prediction is robust across the bounce class … Wilson-Ewing 2012”), and “The Viable Model” subsection: `\cite{WilsonEwing:2012}`.

**Issue:** The Wilson–Ewing quasi-dust matter-bounce model is a core ingredient in the phenomenology, but the provided LaTeX snippet does not show that `WilsonEwing:2012` is mapped to the correct LQC bounce paper (title, journal and arXiv ID), which impedes external verification that the quoted relations for \(n_s\) and \(w\) really come from that specific source.[1]

**Fix:** In the bibliography, ensure `WilsonEwing:2012` includes the full title and correct arXiv ID (e.g., the loop quantum cosmology matter-bounce paper) and, at first mention in the main text, give a short parenthetical like “(Wilson–Ewing, JCAP …, arXiv:XXXX.YYYY)” so that readers can directly match formulae like \(n_s = 1 + 12w\) to the correct paper.[1]

---

## PAPER-PER-n1 – Ambiguous use of “Cai et al. bispectrum calculation”

**Location:** Abstract sentence “We audit the Cai et al. bispectrum calculation, confirming that the intermediate \(\epsilon\)-order decomposition (their Eqs. 34–36) …” and later in Assumptions section.

**Issue:** The phrase “Cai et al.” is potentially ambiguous: it could mean the 2009 matter-bounce paper (arXiv:0903.0631) or another Cai et al. paper; for citation forensics it should be crystal clear which article’s Eqs. (34–36) and Eq. (37) are being referenced.[1]

**Fix:** Replace the first occurrence with something like “Cai et al. (2009, arXiv:0903.0631)” or “Cai et al. (JCAP 2011, arXiv:0903.0631)” and ensure the equation-number references (34–36, 37) match that specific paper’s numbering in the final typeset version.[1]

---

## No blocker-grade issues found

Based on the snippet and external checks, I do not see a clear blocker-grade citation-confabulation such as a non-existent arXiv ID, a fused title/ID from different papers, or a clearly false claim about what arXiv:0903.0631 contains; the issues above are completeness/clarity problems rather than fatal errors.[1]

Do you want a second pass focused specifically on the Heinrich et al. SPHEREx bispectrum citation (ID, figure/table numbers, and the stated \(\sigma(f_{\rm NL})\))?
