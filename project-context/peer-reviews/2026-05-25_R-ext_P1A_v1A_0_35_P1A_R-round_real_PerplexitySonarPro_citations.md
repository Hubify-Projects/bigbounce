# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-25_R-ext_P1A_v1A_0_35
**Wall time**: 26.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30058, completion=1665, total=31723

---

## PAPER-PER-B1 – Mis-cited core reference Cai:2009fn

**Location:** Abstract & throughout (e.g. “matter-bounce class” line ~60); Table captions and Sec. \ref{sec:surviving}.

**Issue:** The paper repeatedly cites “Cai:2009fn” as the source of the matter‑bounce prediction \(\fnl=-35/8\), but the arXiv ID 0903.0631 corresponds to “Non-Gaussianity in a Matter Bounce” with authors Brandenberger et al., not a Cai‑first‑author paper as implied by the “Cai:2009fn” label and surrounding prose (“Cai & Zhu”, “Cai:2009fn” etc.).[1] The label therefore fuses an incorrect author tag (“Cai”) with the correct arXiv ID and topic.

**Fix:** Rename the BibTeX entry and in‑text tag to match the actual paper (e.g. `\cite{Brandenberger2009MatterBounce}`) and update narrative text to refer to “Brandenberger et al.”, or else change the arXiv ID and metadata if the intention was to cite a genuinely Cai‑authored work.


## PAPER-PER-M1 – Missing bibliographic metadata for all citations

**Location:** Entire manuscript; no explicit bibliography shown in the excerpt.

**Issue:** The LaTeX source uses many `\cite{…}` keys (e.g. `Planck2018params`, `Weinberg1989`, `Ashtekar2011`, `Hehl1976`, `Freidel2005`, `Mercuri2009`, etc.), but the actual BibTeX entries (titles, authors, arXiv IDs, journal venues) are not present in the provided text, so it is impossible to verify that each citation’s metadata (author set, title, arXiv category) matches the claims in prose. For example, the text asserts Planck2018params is a Planck parameter paper and Ashtekar2011 a status report on LQC, but we cannot confirm the corresponding BibTeX entries are correct or unfused.

**Fix:** Ensure the final submission includes a complete `references.bib` file or explicit `thebibliography` environment with full metadata, and run an automated cross‑check (e.g. using ADS or arXiv APIs) to confirm that each key maps to the intended paper (correct authors, title, arXiv ID, journal) and that no fused or swapped metadata are present.


## PAPER-PER-m1 – Ambiguous DESI citations (DESI2024, DESI2025DR2)

**Location:** Introduction paragraph 1, first lines: “DESI 2024–2025 BAO results suggest…”

**Issue:** The text cites `\cite{DESI2024,DESI2025DR2}` for BAO‑based evidence of dynamical dark energy at “3.1–4.2σ” but gives neither titles nor arXiv IDs in‑line; without seeing the BibTeX, it is not verifiable that `DESI2024` and `DESI2025DR2` correspond to actual DESI Collaboration BAO / DR2 dark‑energy analyses rather than to other DESI outputs (e.g. target selection, instrument). The σ‑range quoted is sensitive to exactly which DESI paper is meant.

**Fix:** In the bibliography, map `DESI2024` and `DESI2025DR2` explicitly to the correct DESI BAO / DR2 cosmology papers (full titles, arXiv IDs, collaboration as author) and check that their quoted σ‑range for dynamical dark energy matches what those papers actually state; adjust the σ‑numbers or text if needed.


## PAPER-PER-m2 – Unsupported claim of “Heinrich+2024 σ(fNL)≈0.7”

**Location:** Table \ref{tab:summary} footnote and Sec. \ref{sec:falsification} and \ref{sec:surviving} (SPHEREx forecast discussion).

**Issue:** The manuscript attributes a Fisher‑ideal SPHEREx forecast of \(\sigma(f_{\rm NL})\approx 0.7\) to “Heinrich+2024” and uses this as a quantitative basis for claiming “3–5σ realistic significance,” but the reference key `\cite{Heinrich:2023}` would, if standard, correspond to a 2023 arXiv posting, not a 2024 result, and we cannot verify that any specific Heinrich et al. paper actually reports this exact 0.7 number for the matter‑bounce shape rather than for a different configuration or survey.[2]

**Fix:** Check the Heinrich et al. paper being cited (and correct its key to match its true year and arXiv ID) to confirm what \(\sigma(f_{\rm NL})\) values are actually forecast, and rewrite the text so that any numerical claims (0.7, 1.0, “3–5σ realistic”) match the cited paper’s quantitative results and survey assumptions, or else clearly label them as this work’s own forecast rather than as Heinrich et al.’s.


## PAPER-PER-n1 – Incomplete metadata for Planck birefringence references

**Location:** Abstract and Sec. \ref{sec:EB}, \ref{sec:discussion}: references to “Planck/ACT DR6 3.6σ signal,” “Minami & Komatsu” and “Eskilt2022b”.

**Issue:** The text claims consistency with a “published Planck/ACT DR6 3.6σ signal” and later references “Minami & Komatsu” and “Eskilt2022b” without giving explicit arXiv IDs or full titles, making it impossible to confirm that the numbers used (e.g. \(\beta=0.342^\circ\pm 0.094^\circ\)) match those publications rather than some internal combination or later update. Several different Minami / Eskilt birefringence analyses exist with slightly different central values and significances.

**Fix:** In the bibliography, map `Minami2020`, `Eskilt2022b`, and any Planck/ACT DR6 birefringence key to specific arXiv IDs and titles, and double‑check that the quoted central value and significance are taken from one well‑defined paper or clearly described combined analysis; adjust numbers or add clarifying prose if they differ from the source.


## PAPER-PER-n2 – Self‑citation placeholders for companion papers without arXiv IDs

**Location:** Abstract, Introduction, Secs. \ref{sec:obs}, \ref{sec:falsification}, \ref{sec:related}, \ref{sec:surviving}, and Table/footnotes citing `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`, `Golden2026supplement`.

**Issue:** The manuscript uses internal labels like `Golden2026P1b` for multiple “companion” papers and a “supplement,” but no arXiv IDs, journal references, or DOIs are provided, so these cannot be independently located or verified; as currently written they function more as project‑internal placeholders than as standard citations.

**Fix:** For journal submission, replace each `Golden2026P…` key with proper bibliographic entries (authors, titles, arXiv IDs or journal references) if those works are or will be public by the time of publication; otherwise explicitly tag them as “in preparation” or “private communication” and remove any claims that rely on them for essential, non‑reproducible numerical results.
