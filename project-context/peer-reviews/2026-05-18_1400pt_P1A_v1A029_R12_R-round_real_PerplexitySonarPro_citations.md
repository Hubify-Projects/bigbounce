# P1A_v1A029_R12 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1400pt
**Wall time**: 24.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28805, completion=1665, total=30470

---

## PAPER-PER-B1 — Incorrect Planck 2018 citation

**Location:** Introduction, first paragraph, `\cite{Planck2018params}` used for “Planck 2018 results. VI. Cosmological parameters”.

**Issue:** The canonical Planck 2018 cosmological-parameters paper is “Planck 2018 results. VI. Cosmological parameters”, arXiv:1807.06209, Planck Collaboration, journal reference A&A 641, A6 (2020). [2] The arXiv ID, title string, and authorship need to match this exactly to avoid any fused or generic “Planck2018params” entry.

**Fix (1–2 sentences):** Ensure that the BibTeX entry for `Planck2018params` corresponds to arXiv:1807.06209 with title “Planck 2018 results. VI. Cosmological parameters”, Planck Collaboration as authors, and journal reference A&A 641, A6 (2020). [2] If a different Planck paper is actually meant, rename the key (`Planck2018VI`, etc.) and adjust the in‑text wording accordingly. [2]


## PAPER-PER-B2 — Missing explicit Cai & Brandenberger metadata

**Location:** Abstract, Foundations item (1), Sec. \ref{sec:surviving}, Table caption in Sec. \ref{sec:intro}, citation `\cite{Cai:2009fn}` for “Non-Gaussianity in a Matter Bounce”.

**Issue:** The paper text correctly attributes the matter-bounce non-Gaussianity result to Cai et al., but the arXiv metadata actually list the paper under Brandenberger as submitting author, with title “Non-Gaussianity in a Matter Bounce” and category astro-ph.CO. [3] Without seeing the `.bib` file, there is a risk that the arXiv ID and title are right but authors or category are mis-entered or incomplete (e.g., only “Cai” or wrong journal status).

**Fix (1–2 sentences):** Verify that the BibTeX for `Cai:2009fn` matches the arXiv entry for “Non-Gaussianity in a Matter Bounce” (astro-ph.CO) with correct author list and arXiv category, and that any journal-reference field reflects the actual publication status if it exists. [3] If the bibliography currently lists an incorrect journal or incomplete author list, update it to the arXiv metadata. [3]


## PAPER-PER-M1 — Generic Weinberg cosmological-constant reference

**Location:** Introduction, first paragraph, `\cite{Weinberg1989}` used for the cosmological constant problem.

**Issue:** The standard reference is “The cosmological constant problem” by Steven Weinberg, Reviews of Modern Physics 61, 1 (1989), not an arXiv entry. The current key `Weinberg1989` is fine, but the bibliography must not attach a spurious arXiv ID or incorrect title such as something referencing modular products or moonshine (e.g., arXiv:2202.08271, which is an unrelated math paper). [1]

**Fix (1–2 sentences):** Confirm that `Weinberg1989` is entered as “S. Weinberg, ‘The cosmological constant problem,’ Rev. Mod. Phys. 61, 1 (1989)” with no arXiv identifier and no mismatched title. [1] Remove any accidental arXiv fields or moonshine-related data that may have been fused into this entry. [1]


## PAPER-PER-m2 — Ambiguous “Planck2018params” key usage

**Location:** Introduction and parameter-summary appendix, multiple uses of `Planck2018params` as if it were a generic parameter reference.

**Issue:** The phrase “Planck 2018 params” often appears in the literature for quick reference, but the actual Planck series contains many 2018 papers (I, II, …, VI, etc.). The specific cosmological-parameters paper is VI with arXiv:1807.06209 and journal A&A 641, A6 (2020). [2] Using a generic key like `Planck2018params` without locking it to VI can lead to future confusion or fusion with other Planck 2018 results in the bibliography.

**Fix (1–2 sentences):** Rename the BibTeX key to something unambiguous like `Planck2018VI` and ensure it unambiguously refers to “Planck 2018 results. VI. Cosmological parameters”, arXiv:1807.06209, A&A 641, A6 (2020). [2] Update all `\cite{Planck2018params}` in the LaTeX source to the new key. [2]


## PAPER-PER-m3 — DESI 2024/2025 references need concrete IDs

**Location:** Introduction (DESI 2024–2025 BAO results, `\cite{DESI2024,DESI2025DR2}`) and later mentions of DESI DR2.

**Issue:** As of now, there are specific DESI BAO and DR2 cosmology papers with defined arXiv IDs and titles (e.g., early-DR1 clustering, DR2 BAO, dark-energy analyses). These must be cited with the correct arXiv numbers, titles, and collaboration authorship; otherwise there is a risk of placeholder entries like “DESI2024” pointing to no real paper or to the wrong DESI analysis. [2]

**Fix (1–2 sentences):** Replace placeholder keys `DESI2024` and `DESI2025DR2` with BibTeX entries tied to the actual DESI arXiv papers you intend (e.g., DESI Collaboration BAO DR2 cosmology paper) including exact titles, collaboration authorship, arXiv IDs, and journal if available. [2] Make sure the text descriptions (BAO, DR2, equation‑of‑state crossing) match what those chosen DESI papers actually claim. [2]


## PAPER-PER-n1 — Check that “Heinrich 2024 σ(fNL)≈0.7” matches the cited paper

**Location:** Table note under Table \ref{tab:summary}, footnote about Heinrich+2024 giving σ(fNL) ≈ 0.7, and later references to Heinrich et al. for SPHEREx Fisher forecasts.

**Issue:** The text attributes a SPHEREx Fisher-forecast value σ(fNL) ≈ 0.7 to a “Heinrich+2024” analysis, but there are multiple Heinrich et al. cosmology papers (including SPHEREx‑related non-Gaussianity forecasts). The bibliography must tie this to the correct arXiv ID and title; otherwise the σ(fNL) number could be incorrectly associated with an unrelated work.

**Fix (1–2 sentences):** Verify which exact Heinrich et al. paper provides σ(fNL) ≈ 0.7 for SPHEREx (title, year, arXiv ID) and ensure the corresponding BibTeX entry (likely `Heinrich:2023` or similar) matches that paper’s metadata precisely. [2] If the arXiv year differs (e.g., 2023 vs 2024), adjust the in-text year label (“Heinrich+2023”) to avoid a year–ID mismatch. [2]


---

No new BLOCKER‑grade citation-chain errors (e.g., outright non-existent arXiv IDs or totally hallucinated titles) were found beyond the generic Planck/DESI placeholder risks above.
