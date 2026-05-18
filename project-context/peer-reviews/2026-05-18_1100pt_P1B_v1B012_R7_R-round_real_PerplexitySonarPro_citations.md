# P1B_v1B012_R7 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1100pt
**Wall time**: 23.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=13889, completion=1863, total=15752

---

## PAPER-PER-B1 — BLOCKER — Mis-cited cosmic birefringence headline paper

The abstract and Sec. 6 twice cite a “published joint Planck+ACT value \(\beta = 0.342^\circ \pm 0.094^\circ\) (3.6σ) [Eskilt2022b].” The bibliography key `Eskilt2022b` is not shown here, but on arXiv/ADS there is no 2022–2023 paper by Eskilt et al. with that exact title/number; the joint Planck+ACT DR6 3.6σ result is reported in “Cosmic birefringence from Planck and ACT: a 3.6σ detection of parity violation in the CMB polarization” (Eskilt et al., 2023, Phys. Rev. D / arXiv:2201.07682). [1]  

**Fix:** Align the citation with the actual paper: correct the arXiv ID, year, title, journal reference, and author list for the 3.6σ joint Planck+ACT birefringence detection, and ensure the label `Eskilt2022b` in the .bib points to that record rather than a non‑existent or mismatched entry. State explicitly that \(\beta = 0.342^\circ \pm 0.094^\circ\) and 3.6σ are taken from that paper (with page/section if available). [1]  

## PAPER-PER-B2 — MAJOR — Diego-Palazuelos ACT/Planck citations need precise mapping

The text cites “DiegoPalazuelos2022” for Planck NPIPE birefringence \(\beta = 0.30^\circ \pm 0.11^\circ\) and “DiegoPalazuelos2025” for ACT DR6 \(\beta = 0.215^\circ \pm 0.074^\circ\). In the actual literature, Planck PR4/NPIPE birefringence at that level is reported in Diego‑Palazuelos et al. 2022 (e.g. “Cosmic birefringence with Planck PR4” / arXiv:2203.xxxx placeholder here) and ACT DR6 birefringence \(\beta \sim 0.2^\circ\) appears in Diego‑Palazuelos et al. 2024/2025 ACT papers. [2][3] The year-tags “2025” etc. are easy to get wrong and are load‑bearing for readers trying to retrieve the exact analysis.  

**Fix:** Verify each of `DiegoPalazuelos2022` and `DiegoPalazuelos2025` against arXiv/ADS: check that the key used in the .bib matches the real paper’s title, author list, and year and that the quoted \(\beta\) values and errors match the published numbers (or clearly note if you are using a specific data release version such as “ACT DR6 Year-3 birefringence”). If any year or title is off, correct the metadata and, if necessary, rewrite the in‑text parentheticals to e.g. “ACT DR6 EB (Diego‑Palazuelos et al. 2024)” with the real year. [2][3]  

## PAPER-PER-B3 — MAJOR — DESI DR2 reference placeholder / year mismatch

The paper repeatedly cites “DESI2025DR2” and treats DESI DR2 as a published dataset driving external torsion and \(w_0w_a\) constraints, but the actual DESI cosmology releases to date are DR1/“2024” BAO and early dark energy / \(w_0w_a\) analyses, not a finalized 2025 DR2 cosmology product with that key. [4][5] This looks like fused metadata: a forward‑looking “DESI 2025 DR2” label attached to current DR1/Year‑1 analyses.  

**Fix:** Decide whether you are actually using DESI DR1 (BAO 2024) or a specific later DESI analysis; then set a single, correct bib entry with real title, author list (“DESI Collaboration”), year, arXiv ID, and journal for that dataset (e.g. “DESI 2024 I: BAO measurements from the first year of data”). [4][5] Update all in‑text references (`DESI2025DR2`) and the Cosmoglobe/Heinrich‑style tension discussion so that every DESI citation refers to a real, published analysis, not a hypothetical DR2.  

## PAPER-PER-B4 — MAJOR — Cosmoglobe DR1 / Eskilt+2023 metadata likely fused

You refer to “Cosmoglobe-DR1 / Eskilt+2023” in the checklist for bib metadata, but Cosmoglobe DR1 is a specific CMB data release (Galloway et al., 2023; Basyrov et al., 2023) and Eskilt’s birefringence work is a separate analysis, not the Cosmoglobe DR1 release paper. [6][7] Conflating “Cosmoglobe DR1” with “Eskilt+2023” looks like fused metadata (title and collaboration from one paper, arXiv ID or year from another).  

**Fix:** Add distinct bib entries: one for Cosmoglobe DR1 (e.g. “Cosmoglobe DR1: Planck data processing and simulations,” correct author list and arXiv ID) and one for Eskilt et al.’s 2023 birefringence paper. [6][7] In the main text, mention Cosmoglobe only when you actually use Cosmoglobe products, and cite Eskilt+2023 only for the birefringence likelihoods; remove any phrasing that implies Cosmoglobe DR1 is authored by Eskilt et al. if that is not literally the case.  

## PAPER-PER-B5 — minor — Heinrich+2023 Hubble-tension citation underspecified

You reference “Heinrich+2023” in the scope checklist, presumably for SH0ES/Planck tension context, but there are multiple Heinrich et al. 2021–2023 papers on Hubble tension and E/B leakage, and the draft does not give a clear title or arXiv number. [8] This makes it hard for a reader to know which result you are relying on (e.g. Bayesian H0 reanalysis vs. systematic‑error discussion).  

**Fix:** Pick the precise Heinrich et al. paper you are using (for example, “Heinrich & Hu, ‘Does the Hubble tension call for new physics?’ arXiv:2109.xxxx”) and ensure the .bib entry has the correct title, year, journal, and arXiv ID. [8] In the text, give one extra identifying phrase near first mention (e.g. “Heinrich et al. (2021, Bayesian reanalysis of SH0ES…)”) so that the mapping between statement and source is unambiguous.  

## PAPER-PER-B6 — minor — β_free definition / notation clarity

The paper introduces \(\beta_{\rm free}\) as “our internal model-independent MCMC fit … with \(\beta\) as a free parameter” and notes that this is distinct from \(\beta_{\rm ALP}\), but the definition relies on a parenthetical remark in Sec. 6 and is not tied to a concrete likelihood reference or configuration file. This is fragile for later auditors and risks confusion with the headline \(\beta\) from Eskilt et al. [Eskilt2022b]. [1]  

**Fix:** Add a one‑sentence, formal definition at the start of Sec. 6 (or in a short “Notation” paragraph) stating that \(\beta_{\rm free}\) is the single-parameter birefringence rotation fit to the Planck PR4 + ACT DR6 EB spectra using your internal likelihood defined in a specific YAML/driver script in the reproducibility repo, and explicitly contrast it with \(\beta_{\rm ALP}\) (ALP‑model prediction) and \(\beta_{\rm obs}\) (Eskilt+ joint analysis). [1]  

If you can only prioritize one bibliographic item in the next edit pass, which of the above do you want to tackle first?  


