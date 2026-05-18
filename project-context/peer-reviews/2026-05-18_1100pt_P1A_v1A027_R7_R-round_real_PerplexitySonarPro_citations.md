# P1A_v1A027_R7 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1100pt
**Wall time**: 22.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28036, completion=1047, total=29083

---

## PAPER-PER-B1 — Mis-citation of Freidel–Minic–Takeuchi

The text attributes the physical observability of the Barbero–Immirzi parameter via fermion couplings to “Freidel, Minic & Takeuchi 2005” with a Holst/fermion-torsion context, but the actual Freidel–Minic–Takeuchi paper is a group field theory model for 3d quantum gravity coupled to a scalar, not the Holst–fermion parity-odd analysis.  
**Fix:** Replace this citation with an appropriate Holst–fermion reference (e.g. Mercuri’s Holst–Nieh–Yan analyses) and, if Freidel–Minic–Takeuchi is kept at all, clearly separate it as a 3d GFT reference, not the source of the BI–fermion coupling claim.

---

## PAPER-PER-B2 — Incomplete Hehl–Datta reference metadata

The Hehl–Datta four-fermion contact term is cited with an internal macro “HehlDattaNJL1971” but in the text is grouped generically with “Hehl et al. 1976,” which corresponds to the well‑known Einstein–Cartan review rather than the original torsion–NJL derivation.  
**Fix:** Ensure the bibliography includes the 1971 Phys. Rev. D Hehl–Datta paper with correct authors, year, title, journal, and that the main text explicitly cites both the 1971 NJL paper for the contact interaction and the 1976 Rev. Mod. Phys. review for the general EC framework.

---

## PAPER-PER-M1 — Holst 1996 arXiv ID and journal mismatch

The Holst term is discussed as a standard reference but no explicit citation is visible; when added, Holst’s original paper should be “S. Holst, ‘Barbero’s Hamiltonian derived from a generalized Hilbert–Palatini action,’ Phys. Rev. D 53 (1996) 5966–5969, arXiv:gr-qc/9511026,” whereas nearby gr-qc identifiers like 9606062/0503036/0507039 are unrelated to Holst and would be incorrect if used.  
**Fix:** Explicitly include Holst’s correct arXiv ID (gr-qc/9511026) and Phys. Rev. D citation, and verify that no other gr-qc IDs are mistakenly attached to the Holst term or to Ashtekar-type Lagrangians.

---

## PAPER-PER-M2 — Ambiguous Mercuri reference mapping

Multiple Mercuri works are cited (2006, 2009, and Mercuri–Capozziello) for Holst/Nieh–Yan parity structure and one-loop coefficients, but the text conflates roles: the reconstruction of Nieh–Yan and the statement that the BI parameter drops out of classical dynamics come from specific Mercuri papers, while one-loop parity-odd coefficients are analyzed in distinct Shapiro–Teixeira–type works.  
**Fix:** Disentangle the bibliography so that each claim (Nieh–Yan reconstruction, BI dropping out, one-loop parity-odd coefficient) is tied to the correct individual paper with accurate title, authors, journal, and arXiv ID; avoid attributing loop-level results generically to Mercuri when they actually come from Shapiro–Teixeira.

---

## PAPER-PER-M3 — Date–Kaul–Sengupta Immirzi-running citation not fully specified

The running of the Immirzi parameter is attributed to “Date, Kaul & Sengupta 2009” with a specific beta function, but the paper is not explicitly identified (title, arXiv ID, journal), and multiple Date–Kaul–Sengupta works exist on LQG and black-hole entropy.  
**Fix:** Verify that the beta function quoted matches the correct Date–Kaul–Sengupta running‑Immirzi paper (check arXiv.org/ADS) and add full metadata (e.g. arXiv:gr-qc/0xxxxx, JHEP or Class. Quant. Grav. reference) to prevent author/year ambiguity or accidental fusion with their entropy-counting papers.

---

## PAPER-PER-nit1 — Shapiro–Teixeira bibliographic precision

Shapiro & Teixeira are cited for a one-loop estimate of the Nieh–Yan / parity-odd coefficient, but no arXiv ID or journal is given, and there are several closely-related Shapiro loop-gravity papers with different coauthors and venues.  
**Fix:** Identify the exact Shapiro–Teixeira paper that gives the quoted formula (title, arXiv number, and journal) and ensure that the loop structure and context (torsion, Nieh–Yan, BI dependence) match what is claimed in the text.
