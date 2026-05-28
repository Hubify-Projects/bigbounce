# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint-v3_P1A_v1A_0_35
**Wall time**: 25.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30052, completion=1628, total=31680

---

## PAPER-PER-B1 – Mis-cited Cai matter-bounce paper

**Location:** Abstract, multiple later mentions; citation key `\cite{Cai:2009fn}`.  

**Issue:** The paper attributes the matter-bounce prediction \(\fnl=-35/8\) to Cai et al. 2009 with arXiv ID 0903.0631, but arXiv:0903.0631 (“Non‑Gaussianity in a Matter Bounce”) is by Brandenberger (and collaborators), and its arXiv page does not list Cai as first author or use the “Cai:2009fn” tag in the metadata snippet, indicating a mismatch between the key “Cai:2009fn” and the actual arXiv record’s author/title information.[1]  

**Fix (MAJOR):** Check the intended reference: if the correct source is Brandenberger’s 2009 matter‑bounce non‑Gaussianity paper at arXiv:0903.0631, rename the BibTeX key to something like `Brandenberger2009MBNG` and update in‑text mentions so you do not describe it as “Cai:2009fn”; if instead a different Cai et al. paper is intended, correct the arXiv ID, title, and authors in the bibliography so they match the arXiv record.

---

## PAPER-PER-B2 – Planck 2018 parameters citation mismatch

**Location:** Introduction, line “Planck2018params” and surrounding cosmological‑parameter discussion.  

**Issue:** The in‑text label `Planck2018params` implies “Planck 2018 results. VI. Cosmological parameters”, whose correct arXiv ID is 1807.06209 and journal reference A&A 641, A6 (2020), but the provided tool pull for arXiv:1502.01589 corresponds instead to the 2015 parameters paper (“Planck 2015 results. XIII. Cosmological parameters”).[2][3] This risks fused metadata in the .bib (2018 tag but 2015 ID, or vice versa).  

**Fix (minor):** Ensure that the BibTeX entry behind `Planck2018params` uses arXiv:1807.06209, correct 2018 title, and the A&A 641, A6 (2020) reference; if any 2015 metadata from arXiv:1502.01589 is present under that key, split it into a separate `Planck2015params` entry and fix all in‑text citations accordingly.

---

## PAPER-PER-B3 – Missing explicit Weinberg 1989 metadata

**Location:** Introduction, citation `\cite{Weinberg1989}` for the cosmological constant problem.  

**Issue:** The canonical reference is Weinberg’s “The Cosmological Constant Problem”, Rev. Mod. Phys. 61, 1 (1989), but no explicit arXiv ID exists for this classic review, and the paper’s LaTeX text gives no title, journal, or DOI details; if the .bib tried to assign an arXiv ID, it would be incorrect, since the article predates arXiv and is not listed there as such.[4]  

**Fix (nit):** In the bibliography, make `Weinberg1989` a standard journal entry with full title, Rev. Mod. Phys. volume/page, and no arXiv field (or only an ADS link), to avoid implying a non‑existent arXiv ID.

---

## PAPER-PER-B4 – Planck parameters values: 2015 vs 2018 consistency

**Location:** Abstract and Appendix Table~\ref{tab:params}, entries like “\(H_0 = 67.68 \pm 1.06\), \(\Delta N_{\rm eff} \approx 0\) … from that companion”.  

**Issue:** The quoted values (\(H_0\simeq 67.68\), \(\Omega_m\simeq 0.308\)) closely match the 2015 Planck cosmology (\(H_0=67.8\pm0.9\), \(\Omega_m=0.308\pm0.012\)) rather than the 2018 best fits (\(H_0=67.4\pm0.5\), \(\Omega_m=0.315\pm0.007\)).[2][3] If the citation key and narrative claim “Planck 2018” while the numbers actually track 2015, this is a consistency error between cited source and numerical values.  

**Fix (minor):** Decide which release you are actually using: if you intend Planck 2018, update the quoted numbers to match arXiv:1807.06209; if you intend to keep the 2015 values, relabel the citation and text explicitly as “Planck 2015 results. XIII” with the corresponding arXiv:1502.01589 ID.

---

## PAPER-PER-B5 – DESI 2024/2025 BAO citation placeholders

**Location:** Introduction, sentence “DESI 2024–2025 BAO results suggest dynamical dark energy … \cite{DESI2024,DESI2025DR2}”.  

**Issue:** As of the available arXiv and journal records, there is a DESI cosmology/BAO DR1 paper in 2024 and a DR2 preprint in 2025, but the exact citation keys `DESI2024` and `DESI2025DR2` require matching real titles and arXiv IDs (e.g., the 2024 “DESI 2024 cosmological constraints from the full-shape…” BAO paper) which are not visible here; this is a common place where LLM‑generated drafts invent slightly wrong titles or future‑dated IDs. Current arXiv searches show multiple DESI BAO/DR papers, but nothing that exactly matches a generic placeholder “DESI2024” string.[5]  

**Fix (MAJOR):** Replace `DESI2024` and `DESI2025DR2` with concrete, verified references: give the actual DESI BAO/DR1/DR2 paper titles, arXiv IDs, author lists (DESI Collaboration), and year; ensure that the claimed \(3.1–4.2\sigma\) dynamical‑DE significance and “DR2” label match the specific DESI paper you cite.

---

## PAPER-PER-B6 – Companion-paper keys Golden2026P1b / P2 / P3 / P4

**Location:** Abstract and throughout, citations `\cite{Golden2026P1b}`, `\cite{Golden2026P2}`, `\cite{Golden2026P3}`, `\cite{Golden2026P4}`.  

**Issue:** These appear to be internal project designations, not established arXiv IDs or journal publications; current arXiv searches show no public records under those exact titles or author/year combinations.[6] Using them as if they were standard literature risks confusing referees about whether they refer to submitted arXiv preprints or only in‑house notes.  

**Fix (minor):** In the bibliography, either (a) provide full, accurate metadata (title, author, arXiv ID or “in preparation/private communication”) for each Golden 2026 companion paper, or (b) mark them explicitly as “Companion paper in preparation” rather than standard references, and avoid assigning non‑existent arXiv identifiers to them.
