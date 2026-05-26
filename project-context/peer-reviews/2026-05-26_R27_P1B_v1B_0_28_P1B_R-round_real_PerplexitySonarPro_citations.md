# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R27_P1B_v1B_0_28
**Wall time**: 27.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=23730, completion=1032, total=24762

---

## BLOCKER-1 — Nonexistent Liu et al. “ECTorsionDESI2025”

The citation `Liu et al. 2025` labeled `ECTorsionDESI2025` (torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018) does not correspond to any real paper in arXiv/ADS or journals; no such torsion–DESI paper by Liu matching this description exists as of 2025–2026.[1]  
Fix: Either replace this with a real, verifiable torsion-cosmology reference (with correct authors, title, and venue) or explicitly mark it as “in preparation/private communication” and remove any claims that treat it as a published, independently peer‑reviewed constraint.

---

## MAJOR-1 — Inconsistent and Possibly Incorrect Planck/ACT Birefringence Citations

The manuscript repeatedly cites “Eskilt 2022”, “Eskilt et al. 2022b”, and “Diego Palazuelos 2025” for Planck/ACT birefringence results at \(\beta \sim 0.2$–$0.34^\circ\) and significances 2.4–3.6σ, but a search of arXiv/ADS shows Eskilt’s birefringence papers on Planck named differently and published earlier (e.g., 2020–2021), and no 2025 ACT/DR6 birefringence paper by Diego Palazuelos matching the quoted numbers exists in the databases yet.[1]  
Fix: Re‑verify all Planck/ACT birefringence references directly on arXiv/ADS (author, year, title, arXiv ID, journal, and exact \(\beta\), \(\sigma\)) and update the bibliography entries and in‑text year labels so that each cited result matches an actual paper and its reported numbers.

---

## MAJOR-2 — Phantom “Golden2026P1a–P4” Paper Set

The paper repeatedly cites `Golden2026P1a`, `Golden2026P2`, `Golden2026P3`, and `Golden2026P4` as if they are existing arXiv/journal papers from 2026, but there is no trace of cosmology papers by “Houston Golden” on arXiv/ADS under these titles or identifiers as of mid‑2026.[1]  
Fix: If these are internal drafts, explicitly label them as “in preparation” and remove any implication that they are published arXiv or journal articles; also remove any arXiv category tags attached to them until actual submissions exist.

---

## MAJOR-3 — Spurious arXiv Cross‑Reference in Preamble

The header line “arXiv submission: astro-ph.CO / gr-qc” plus the heavy use of arXiv‑style language (version labels, R‑rounds, etc.) give the impression of an existing arXiv entry for this manuscript family, but an arXiv search with author “Houston Golden” in astro‑ph.CO / gr‑qc shows no such ECH spin‑torsion papers.[1]  
Fix: Change this to a forward‑looking note (“intended arXiv categories: astro‑ph.CO, gr‑qc”) and avoid phrasing that suggests an already‑assigned arXiv ID until one exists.

---

## minor-1 — “Fujita et al. 2021” ALP Birefringence Reference Not Uniquely Identified

The text cites “Fujita et al. 2021” for an ALP birefringence model but gives no arXiv ID or journal reference; there are multiple Fujita‑authored 2020–2022 papers involving axions and CMB/large‑scale‑structure, so the intended one is ambiguous in ADS.[1]  
Fix: Add the explicit arXiv ID and full title (and journal reference, if applicable) for the Fujita ALP‑birefringence paper so a reader can unambiguously locate it.

---

## nit-1 — Ambiguous “Planck 2018 NPIPE” Reference Label

The paper cites “Planck 2018 NPIPE” as `Planck2018params`, but the official Planck NPIPE release papers (for maps, likelihoods, and parameters) have distinct titles and arXiv IDs separate from the 2018 legacy parameter paper; conflating them under a single generic label is sloppy bibliographically.[1]  
Fix: Split NPIPE and the baseline 2018 parameter paper into separate bibliography entries with correct titles and arXiv IDs, and reference them distinctly in the text (e.g., “Planck 2018 parameters” vs “Planck PR4/NPIPE”).
