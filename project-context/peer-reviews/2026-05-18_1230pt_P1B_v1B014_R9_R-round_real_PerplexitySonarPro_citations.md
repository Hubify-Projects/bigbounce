# P1B_v1B014_R9 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1230pt
**Wall time**: 21.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=17912, completion=1596, total=19508

---

## PAPER-CIT-B1 — Incorrect citation label for Planck PR4 birefringence paper (Diego-Palazuelos)

**Issue.** Throughout, the Planck PR4 birefringence measurement is cited as “DiegoPalazuelos2022” and described as “Planck NPIPE” with \(\beta = 0.30^\circ \pm 0.11^\circ\) and arXiv ID 2201.07682, but the actual paper is titled “Cosmic Birefringence from Planck Data Release 4,” authored by P. Diego-Palazuelos et al., and is commonly referred to as “Diego-Palazuelos et al. (2022)” rather than “Diego Palazuelos 2022” as if “DiegoPalazuelos” were a first+last name.[1] The arXiv ID and numerical result are correct, but the labeling conflates surname structure and the specific “NPIPE” vs “DR4” naming used by the paper itself.[1]

**Severity.** minor

**Fix.** Rename the bib entry and in-text label to something like `DiegoPalazuelos2022PlanckDR4` and in prose call it “Diego-Palazuelos et al. (Planck DR4)” or “Planck DR4 birefringence,” making clear that it is the DR4/PR4 analysis, not an ACT paper and not literally titled “Planck NPIPE.”


## PAPER-CIT-B2 — Eskilt joint Planck+ACT paper metadata needs alignment

**Issue.** The text repeatedly cites an “Eskilt et al. joint Planck+ACT” result \(\beta = 0.342^\circ \pm 0.094^\circ\) at \(3.6\sigma\) as ref. `Eskilt2022b`, but no explicit title, arXiv ID, or journal metadata is given in the LaTeX, and there are multiple Eskilt cosmic-birefringence works in 2022–2024 (Planck-only, ACT-only, and joint analyses). The number \(\beta = 0.342^\circ \pm 0.094^\circ\) matches the “joint Planck+ACT DR4/DR6” style analyses reported by Diego‑Palazuelos and Eskilt collaborations, but you must ensure `Eskilt2022b` actually corresponds to the final joint-constraint paper, not e.g. the Planck‑only DR4 paper (which is Diego‑Palazuelos first author, arXiv:2201.07682).[1]

**Severity.** MAJOR (if bib entry currently points to the wrong Eskilt paper; minor if the bib is already correct but underspecified)

**Fix.** Ensure the `Eskilt2022b` bib entry points to the actual joint Planck+ACT paper that reports \(\beta = 0.342^\circ \pm 0.094^\circ\) (correct title, authors, arXiv ID, and journal). In the text, give the correct paper title or experiment label (“joint Planck DR4 + ACT DR6 cosmic birefringence”) and verify the quoted central value and uncertainty match that specific work.


## PAPER-CIT-B3 — ACT DR6 birefringence citation label likely mis-specified

**Issue.** The ACT DR6 birefringence measurement is cited as `DiegoPalazuelos2025` with \(\beta = 0.215^\circ \pm 0.074^\circ\), but no clear arXiv ID or journal is given. There is at least one cosmic-birefringence analysis using ACT DR4/DR6 polarization power spectra with Diego‑Palazuelos and Eskilt on the author list, but its actual title, year, and arXiv ID need to be fixed in the bibliography to ensure `DiegoPalazuelos2025` is not a placeholder or mis-dated reference fused with the Planck DR4 paper (arXiv:2201.07682 is 2022, PRL 2022, not 2025).[1]

**Severity.** MAJOR

**Fix.** Confirm the existence and metadata of the ACT DR6 birefringence paper that reports \(\beta = 0.215^\circ \pm 0.074^\circ\) and update the `DiegoPalazuelos2025` bib entry to match its real title, year, arXiv ID, and journal; if no such 2025 paper exists yet, downscope the claim to “private communication / preliminary ACT DR6 result” or update to the latest published ACT birefringence result with its correct numbers and citation.


## PAPER-CIT-N1 — Fujita et al. ALP paper metadata needs explicit verification

**Issue.** The spectator‑ALP model is said to have been “previously studied by Fujita et al. [Fujita2021],” but the bib entry is not shown here, and there are several Fujita ALP/birefringence papers around 2020–2021 (e.g., Fujita, Takahashi, et al. on axionlike fields and CMB polarization). Without explicit title and arXiv ID, there is latent risk of fused metadata (e.g., mixing a Fujita ALP‑isocurvature paper with a different birefringence paper).[1]

**Severity.** nit (assuming the current bib already points to the intended Fujita ALP‑birefringence paper; higher if it does not)

**Fix.** Double‑check that `Fujita2021` points to the specific Fujita et al. paper that actually studies an ALP-induced cosmic birefringence scenario with parameters comparable to those used here, and add its correct title and arXiv ID in the `references.bib` entry; if the current entry targets a different Fujita paper, replace it with the correct one.


## PAPER-CIT-N2 — DESI DR2 torsion paper label `ECTorsionDESI2025` needs concrete bib metadata

**Issue.** The text cites “Liu et al. [ECTorsionDESI2025]” as an Einstein–Cartan torsion model analysis using DESI DR2, Pantheon+, DES‑SN5YR, and Planck 2018, finding torsion preferred by AIC with \(\Delta\mathrm{AIC}=-5.7\) to \(-6.6\), but no arXiv ID, journal, or exact title is given, and I cannot verify this paper under that label in standard literature databases.[1]

**Severity.** MAJOR if the paper is not actually on arXiv/ADS yet; minor if it exists but the bib key is nonstandard

**Fix.** If the Liu et al. torsion paper is on arXiv or published, update the bib entry to its real title, authors, arXiv ID, and journal, and adjust the in‑text label away from an internal name like `ECTorsionDESI2025`. If it is still in preparation, explicitly label it as “Liu et al., in prep.” or similar, drop the precise \(\Delta\mathrm{AIC}\) numbers, and do not treat it as a fully published external constraint.
