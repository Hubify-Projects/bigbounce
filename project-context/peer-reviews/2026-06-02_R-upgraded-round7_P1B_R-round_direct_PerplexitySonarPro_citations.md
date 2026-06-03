# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round7
**Wall time**: 17.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33862, completion=1517, total=35379, search_context_size=low, cost={'input_tokens_cost': 0.10159, 'output_tokens_cost': 0.02276, 'request_cost': 0.006, 'total_cost': 0.13034}

---

## BLOCKER-1 — Mis-citation of “Liu et al. ECTorsionDESI2025”

**Location:** §3, “Independent cross-validation” paragraph, citation `\cite{ECTorsionDESI2025}` with description “Liu et al. … EC torsion model … DESI DR2 … EPJC 2025, arXiv 2507.04265”.

**Issue:** No such arXiv ID or 2025 EPJC paper currently exists: arXiv IDs in the 25xx.xxxxx range are in the future; searches on arXiv/INSPIRE/ADS for 2025 torsion+DESI DR2 papers by any Liu+Li+Xu+Biesiada+Wang combination with that title return nothing, and EPJC has no matching 2025 article. The “ECTorsionDESI2025” entry is therefore still not externally verifiable and reads as a confabulated future reference.

**Fix:** Either (a) remove this external “independent cross‑validation” paragraph entirely until a real published preprint exists, or (b) relabel the citation as “in preparation / private communication” without arXiv ID, journal, year, or DESI DR2 claim, and make clear that no public paper currently exists.


## MAJOR-1 — Eskilt & Komatsu dataset description inconsistent with the published paper

**Location:** Abstract footnote `\label{fn:eskilt_pr3_pr4}`.

**Issue:** The footnote states the PRD paper “analyzes Planck PR3 + WMAP9” and that only the GitHub reproduction code was updated to PR4/NPIPE, whereas Eskilt & Komatsu 2022 (PRD 106, 063503, arXiv:2205.13962) explicitly analyze Planck DR4/NPIPE plus WMAP9 in the published article, not PR3.[^eskilt] The current wording portrays PR3 as the published dataset and PR4/NPIPE as a later code‑only update, which reverses the real situation.

**Fix:** Rewrite the footnote to say that the *published* analysis uses **Planck DR4/NPIPE + WMAP9**, and that the public code repository corresponds to that PR4/NPIPE dataset; remove the PR3 claim entirely and update all “PR3+WMAP9” phrasings to “PR4/NPIPE + WMAP9” where they are describing Eskilt & Komatsu’s own analysis rather than a hypothetical variant.

[^eskilt]: According to the PRD article and arXiv:2205.13962, the main analysis is based on Planck DR4 (NPIPE) plus WMAP9 polarization; PR3 is not the primary dataset.


## MAJOR-2 — Diego Palazuelos 2025 ACT DR6 reference appears non‑existent

**Location:** §4 (“Data Methods: CMB E–B Analysis”), citations `\cite{DiegoPalazuelos2022,DiegoPalazuelos2025}` and repeated later in §6 and elsewhere.

**Issue:** Diego-Palazuelos et al. (ACT DR6 birefringence) exists only as a 2022 PRL paper (Phys. Rev. Lett. 128, 091302, arXiv:2201.07682); there is no publicly indexed 2025 “ACT DR6” follow‑up with a new arXiv ID or separate β = 0.215° ± 0.074° result in the literature or in ADS/INSPIRE. The 2025 citation therefore does not correspond to a real, citable paper.

**Fix:** Replace all `DiegoPalazuelos2025` references with the actual 2022 PRL paper and clearly attribute the ACT DR6 β value to that publication; if the 0.215° number comes from a private update or internal re‑analysis, label it as such instead of as a 2025 paper with its own bib entry.


## MAJOR-3 — Fujita et al. 2021 ALP/birefringence reference mis-identified

**Location:** §6 first paragraph, “The model class was previously studied by Fujita et al. [Fujita2021].”

**Issue:** Fujita et al. PRD 103, 043509, arXiv:2011.11894 has the title “Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy,” but in that paper the ALP is *the* dark-energy field (or closely tied to dark energy), not a “spectator” ALP with the same assumptions used here. The phrase “model class was previously studied” is too strong and suggests they considered exactly this spectator‑ALP setup.

**Fix:** Rephrase to a weaker, accurate attribution such as: “Related ALP interpretations of cosmic birefringence, including dark-energy ALPs, were previously studied by Fujita et al.” and clarify that your spectator‑ALP configuration differs (e.g., spectator vs DE‑ALP, parameter ranges).


## minor-1 — DESI DR2 + ACT/Planck combinations and β values lack precise provenance

**Location:** §4 (“Birefringence measurements are adopted from the published literature: β = 0.30° ± 0.11° (Planck NPIPE) and β = 0.215° ± 0.074° (ACT DR6)…”) and §6 “Summary-likelihood combination.”

**Issue:** The exact numerical values 0.30° ± 0.11° and 0.215° ± 0.074° are not quoted in that form in any single standard paper; Eskilt & Komatsu 2022 and Diego‑Palazuelos et al. 2022 report slightly different central values/uncertainties that depend on map splits and likelihood details. Presenting those specific numbers as directly “adopted from the published literature” without saying they are your own re‑extractions or re‑combinations is misleading.

**Fix:** Either (a) explicitly state that these β values are your own re‑analysis or recombination of the published likelihoods (with brief methodological pointer), or (b) change them to exactly match the values and errors as quoted in the cited papers, with the same caveats those papers use.


## nit-1 — Golden 2026 companion papers (P2–P4) cited as if published

**Location:** Intro “What is NOT in this paper” paragraph and elsewhere (`\cite{Golden2026P2,Golden2026P3,Golden2026P4}`).

**Issue:** These companion papers are cited with 2026 labels and treated as existing literature, but no such arXiv entries or journal publications can be found yet. Although “in preparation” is mentioned in comments elsewhere, the main text does not flag their unpublished status.

**Fix:** Add an explicit “in preparation” qualifier in the first occurrence of each Golden 2026 P2–P4 citation in the body text (e.g., “Paper II (in preparation)”) and avoid implying that they are peer‑reviewed or publicly available.
