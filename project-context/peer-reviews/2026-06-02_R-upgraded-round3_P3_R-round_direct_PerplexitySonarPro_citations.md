# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round3
**Wall time**: 16.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79679, completion=1062, total=80741, search_context_size=low, cost={'input_tokens_cost': 0.23904, 'output_tokens_cost': 0.01593, 'request_cost': 0.006, 'total_cost': 0.26097}

---

## PAPER-PER-B1 — Incorrect Phinney (2001) citation metadata

**Location:** Bibliography entry `Phinney2001` near end.

**Issue:** The cited paper is listed only as “E. S. Phinney, ‘A practical theorem on gravitational wave backgrounds,’ arXiv:astro-ph/0108028 (2001)” but the canonical version is a Caltech technical memo (no journal), often cited explicitly as such; the arXiv entry uses title “A Practical Theorem on Gravitational Wave Backgrounds.” This is slightly incomplete/inexact metadata.

**Fix:** Update the bib entry to “E. S. Phinney, ‘A practical theorem on gravitational wave backgrounds,’ arXiv:astro-ph/0108028 (Caltech-MORE-2001-16, 2001)” or similar canonical technical report reference, matching arXiv’s capitalization and including the institutional report identifier.

---

## PAPER-PER-m1 — Minor drift in Heinrich et al. (2023/2024) metadata

**Location:** Intro (Heinrich et al.), §5 cosmology, bibliography entry `Heinrich2023`.

**Issue:** Text refers to “Heinrich+2024” and “Heinrich et al. (2023)” for the same SPHEREx multi-tracer bispectrum paper, which is a JCAP 2024 publication with arXiv:2311.13082; referring to it as 2023 in some places and 2024 in others is mildly inconsistent but not substantively wrong.

**Fix:** Normalize all in-text references to match the bib (e.g., “Heinrich et al. 2024, JCAP, arXiv:2311.13082”) and avoid mixing 2023/2024 labels for the same work.

---

## PAPER-PER-m2 — Minor inconsistency in NANOGrav dataset citation

**Location:** §5 (NANOGrav consistency), §app:pta_mcmc, bibliography entry `NANOGrav2023`.

**Issue:** The text correctly cites the NANOGrav 15-year ApJL paper for the detection, but the KDE free-spectrum likelihood actually comes from a Zenodo artifact (DOI 10.5281/zenodo.8060824), which is mentioned in prose but not represented as a separate data reference in the bibliography.

**Fix:** Add a distinct bib entry for the Zenodo KDE dataset (authors: NANOGrav Collaboration, title matching the Zenodo record) and explicitly cite that entry wherever the KDE chain is described as the data source, keeping the ApJL entry for the main evidence paper.

---

## PAPER-PER-n1 — Small style/consistency nit on SPHEREx reference

**Location:** Intro, §5, bibliography entry `SPHEREx2014`.

**Issue:** SPHEREx is referenced via the 2014 arXiv concept paper; some text calls that “SPHEREx 2014” while also describing forecasts as “SPHEREx-class surveys.” This is stylistically fine but could confuse readers about whether a later mission design paper is meant.

**Fix:** Clarify once in the main cosmology section that all SPHEREx forecasts in the paper refer specifically to the 2014 Doré et al. concept study (arXiv:1412.4872), and keep later mentions to “SPHEREx (Doré et al. 2014)” or simply “SPHEREx” thereafter.

---

## PAPER-PER-n2 — Minor ambiguity in Munchmeyer et al. comparison

**Location:** Intro, §5, citation to Munchmeyer et al. 2019.

**Issue:** The text compares an internal Fisher forecast σ(fNL)≈0.07–0.12 to “the Munchmeyer et al. consensus σ_fNL ≈ 0.4–0.9 for SPHEREx-class surveys” without specifying that Munchmeyer et al. 2019’s numbers are for kSZ-based constraints, not the exact same multi-tracer configuration.

**Fix:** Add a short qualifier like “kSZ-based SPHEREx-class forecast of Munchmeyer et al. (2019)” so the reader understands the comparison is methodological/scale-level, not against an identical survey + tracer configuration.

---

## PAPER-PER-n3 — Tiny naming nit for PTA new-physics paper

**Location:** Appendix PTA section, bib entry `Afzal2023NewPhys`.

**Issue:** The text calls this “NANOGrav new-physics companion paper” and cites Afzal et al. 2023; that is accurate, but the title could be slightly closer to the published one (“The NANOGrav 15-year Data Set: Search for Signals from New Physics”) to avoid any perception of a paraphrased/LLM-generated title.

**Fix:** Ensure the bib title exactly matches the published ApJL title string from the journal or arXiv record, not a paraphrase.
