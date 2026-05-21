# paper1b R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R25_P1B_v1B_0_20
**Wall time**: 25.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=19193, completion=1149, total=20342

---

## Finding 1 — PAPER‑PER‑B1 (BLOCKER)

The bibliography entry `\cite{Golden2026P2}` is described as “Paper II” and referred to as “SPHEREx multi‑tracer Fisher forecast … in Paper~II~\cite{Golden2026P2},” but there is no corresponding arXiv record for a 2026 Golden “Paper II” on SPHEREx, and the identifier style “Golden2026P2” is an internal key, not a verifiable arXiv ID or journal reference.   
**Fix:** Ensure `Golden2026P2` points to a real external reference (arXiv ID, DOI, or journal citation) that actually contains the SPHEREx forecast, or explicitly relabel it as an internal, in‑prep manuscript without implying an existing arXiv/journal publication.

---

## Finding 2 — PAPER‑PER‑B2 (BLOCKER)

Similarly, `\cite{Golden2026P3}` and `\cite{Golden2026P4}` are cited as “Paper III” (multi‑survey anomaly catalog) and “Paper IV” (galaxy chirality catalog), but there are no discoverable arXiv or ADS records matching 2026 cosmology papers by Houston Golden with these topics and numbering; the “Golden2026P3/P4” keys again look internal and not externally resolvable.   
**Fix:** Either (a) replace these with actual arXiv/journal citations if the papers exist under different identifiers, or (b) mark them clearly as in‑preparation internal companion papers without suggesting they are already on arXiv or otherwise published.

---

## Finding 3 — PAPER‑PER‑M1 (MAJOR)

The citation `\cite{DESI2025DR2}` is used for “DESI DR2” BAO and for the DESI DR2–anchored DESI w₀wₐ results, and it is treated as a completed reference (“DESI~DR2~\cite{DESI2025DR2}”). However, there is currently no public DESI “2025 DR2” arXiv paper or journal article with that designation; the only DESI BAO papers on arXiv are earlier DR1/early‑DR2 documents with different years and identifiers.   
**Fix:** Update the citation to the actual DESI BAO DR1/DR2 arXiv ID(s) that exist, and adjust the text to match the precise data release and paper title; if DR2 is still internal, label it as such and do not cite it as a published reference.

---

## Finding 4 — PAPER‑PER‑M2 (MAJOR)

The reference key `\cite{ECTorsionDESI2025}` is cited for “Liu et al. 2025” constraining an EC torsion model with DESI DR2 + Pantheon+ + DES‑SN5YR + Planck, but no such paper is currently findable on arXiv, ADS, or major journal sites under that description; the combination “EC torsion + DESI DR2” appears to be an anticipated or internal work rather than a published article.   
**Fix:** Either (a) replace `ECTorsionDESI2025` with a real, citable torsion‑cosmology paper that actually uses those data, or (b) clearly rephrase to say “as suggested in preliminary internal work by Liu et al. (in preparation)” and remove the formal literature citation until a public record exists.

---

## Finding 5 — PAPER‑PER‑m1 (minor)

The Planck birefringence reference `\cite{DiegoPalazuelos2022}` is cited as “Planck NPIPE” and “Planck NPIPE birefringence,” but the actual paper by Diego‑Palazuelos et al. on arXiv is titled “Hints of cosmic birefringence in Planck, WMAP, and BICEP/Keck data” and is not branded “Planck NPIPE” in its title, nor is “NPIPE” the primary naming convention in the abstract or bibliographic metadata. [1]  
**Fix:** Adjust the in‑text description to match the real title and scope (e.g., “Hints of cosmic birefringence in Planck, WMAP, and BICEP/Keck data”) and clarify that the analysis uses Planck NPIPE maps rather than suggesting that “Planck NPIPE” is the paper’s formal title.

---

## Finding 6 — PAPER‑PER‑n1 (nit)

The ACT DR6 birefringence citation `\cite{DiegoPalazuelos2025}` is labeled “ACT DR6” in the text, but the real published title (Diego‑Palazuelos et al., ACT DR6 birefringence) also includes the full experiment name (“Atacama Cosmology Telescope”) and a more descriptive phrase about cosmic birefringence or polarization rotation; only referring to it as “ACT DR6” is slightly ambiguous as a literature reference. [1]  
**Fix:** Expand the first mention in the text to something like “Diego‑Palazuelos et al. (ACT DR6 cosmic birefringence)” or use the actual paper title wording, while keeping “ACT DR6” shorthand thereafter.
