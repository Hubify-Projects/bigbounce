# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R29_P1B_v1B_0_30
**Wall time**: 16.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=24027, completion=1326, total=25353

---

## Finding 1 (MAJOR): Placeholder / non-existent citations

The bibliography includes several references that appear to be self-citations with future or placeholder metadata and no discoverable arXiv/ADS/publisher records (e.g., “Golden 2026 P1(a)–P4” via keys `Golden2026P1a`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`, “ECTorsionDESI2025”, “DESI2025DR2”, “LiteBIRD2023`, “DES2024SN5YR”). These titles, venues, and arXiv IDs (if any) cannot be verified against arXiv.org, ADS, or publisher sites and look like forward-dated internal placeholders rather than real, citable papers.[1]  
**Fix:** Make all such citations explicitly labeled as “in preparation / private communication / internal note” with no fabricated arXiv IDs, or replace them with existing, verifiable literature; remove any arXiv tags that do not correspond to real records and avoid implying refereed status until those works are actually on arXiv or in a journal.

## Finding 2 (MAJOR): Eskilt et al. joint Planck+ACT birefringence reference

The text attributes a “published joint Planck+ACT value \(\beta = 0.342^\circ \pm 0.094^\circ\) (3.6σ)” to “Eskilt et al. 2022b”. There is an Eskilt et al. 2022 Planck-only cosmic birefringence paper and an ACT-based Diego-Palazuelos et al. analysis, but no verifiable joint Planck+ACT paper by Eskilt et al. with exactly this title, combination, and error bar in the current literature.[1]  
**Fix:** Either (a) clearly describe this as an internal combined analysis and not as a published Eskilt et al. paper, or (b) update the citation to the actual published Planck and ACT birefringence papers separately, dropping the “joint Planck+ACT” and “Eskilt 2022b” label unless and until such a joint paper actually exists.

## Finding 3 (MAJOR): “Liu et al. 2025” EC torsion DESI paper

The text cites “Liu et al. (2025)” as having constrained an Einstein–Cartan torsion model with DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, with AIC preference ΔAIC ≈ −5.7 to −6.6, under the key `ECTorsionDESI2025`. No such EC-torsion cosmology paper by Liu et al. using DESI DR2 and these exact datasets can be located on arXiv/ADS/publisher sites; this looks like a fused or hypothetical citation, not a currently real paper.[1]  
**Fix:** Remove or clearly relabel this as “work in preparation / private analysis” and delete any claimed AIC numbers unless they can be tied to a real, publicly available paper; replace with currently published constraints (e.g., existing modified-gravity or torsion bounds) if needed for context.

## Finding 4 (MAJOR): DESI DR2 and DES SN “2025/2024” references

The manuscript cites DESI DR2 BAO and a 2025 DESI DR2 cosmology analysis as if they are already standard references (`DESI2025DR2`), and similarly cites a “DES-SN5YR 2024” paper (`DES2024SN5YR`). Current public releases have DESI DR1 BAO and DES 5-year supernova results under different years/IDs; there is no verifiable DESI DR2+DES-SN5YR paper matching the described combination and dates at the time corresponding to the paper’s timestamp.[1]  
**Fix:** Downgrade these to “expected forthcoming DESI DR2 / DES-SN 5yr analyses” or remove until real DR2/5yr papers are on arXiv; for any actual fits done to internal or pre-public data, label them as such and stop citing them as published DESI/DES references.

## Finding 5 (minor): Diego-Palazuelos ACT DR6 and Planck NPIPE citations

The paper quotes \(\beta = 0.30^\circ \pm 0.11^\circ\) for Planck NPIPE and \(\beta = 0.215^\circ \pm 0.074^\circ\) for ACT DR6, attributing them to “Diego Palazuelos 2022/2025” and treating them as final-published DR6 and NPIPE birefringence results. Existing ACT and Planck polarization systematics papers do not match this exact pairing of author, survey label (“DR6” for ACT birefringence), and quoted values as a single canonical reference; the metadata looks partially fused from several preprints.[1]  
**Fix:** Verify the exact arXiv IDs, titles, and author lists of the Planck NPIPE and ACT birefringence analyses actually used, then cite those concrete papers (with correct author order and survey labels) instead of using “DiegoPalazuelos2022/2025” shorthand; adjust the quoted central values and errors if they differ from the published numbers.

## Finding 6 (nit): LiteBIRD forecast reference

The LiteBIRD forecast is cited as “LiteBIRD 2023” with \(\sigma(\beta) \approx 0.03^\circ\), but there is no single LiteBIRD 2023 paper with that exact title and parameter quoted as the main result; the forecast values come from a combination of instrument and science requirement documents and several white papers.[1]  
**Fix:** Replace the generic “LiteBIRD2023” citation with the specific LiteBIRD science/mission paper actually used for the \(\sigma(\beta)\) forecast (correct arXiv ID, title, and collaboration name), and confirm that the quoted \(\sigma(\beta)\) matches that document’s forecast or clearly state that it is an approximate translation of their sensitivity curves.
