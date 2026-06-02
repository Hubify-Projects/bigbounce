# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round2
**Wall time**: 22.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=25703, completion=1811, total=27514, search_context_size=low, cost={'input_tokens_cost': 0.07711, 'output_tokens_cost': 0.02717, 'request_cost': 0.006, 'total_cost': 0.11027}

---

## BLOCKER-1 – Fictional or Mis-cited “Liu et al. EC torsion DESI DR2” paper

**Location:** §3 “Independent cross-validation”, paragraph beginning “Liu et al.”  

**Issue:** The citation `Liu~\etal~\cite{ECTorsionDESI2025}` is described as “constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6)”. This combination, title-style (“EC torsion”), dataset mix (DESI DR2 BAO + DES-SN5YR) and 2025 timing appear to correspond to a paper the author claims exists in the .bib but which is not discoverable in arXiv, ADS, or journal databases; there is no trace of an EC torsion DESI DR2 paper by a Liu–Li–Xu–Biesiada–Wang author list matching this description, nor of an arXiv 2507.04265 preprint with that content. The prior round notes explicitly state Perplexity could not find this work, which remains true.  

**Fix:** Either (a) replace this reference with a verifiable, correctly cited torsion/DESI paper that genuinely reports the quoted ΔAIC preference, or (b) delete the cross-validation paragraph entirely and remove the `ECTorsionDESI2025` entry from the bibliography (or mark it “in preparation / private communication” and drop all quantitative claims drawn from it).


## MAJOR-1 – Eskilt & Komatsu 2022 mis-characterized as “Planck+ACT joint value”

**Location:** Abstract; §6 “Headline observational constraint”  

**Issue:** The paper repeatedly attributes the “published joint Planck+ACT value β = 0.342° ± 0.094° (3.6σ)” to Eskilt et al. 2022b / Eskilt & Komatsu 2022.[2205.13962] That PRD paper is a **Planck PR4 + WMAP** birefringence analysis, not a Planck+ACT DR6 joint combination, and ACT DR6 is not included in that dataset.[2205.13962][2201.07682] The true Planck+ACT DR6 joint analyses appear in later works (e.g., Diego-Palazuelos et al. 2025 / other follow‑ups), not in Eskilt & Komatsu 2022 PRD 106:063503.  

**Fix:** Re-label the 0.342° ± 0.094° value as “Planck PR4 (NPIPE) + WMAP” or whatever exact combination the cited paper actually uses, and reserve “Planck+ACT DR6 joint” for the appropriate later Diego‑Palazuelos / ACT collaboration analysis, updating the arXiv/journal citation and numbers accordingly.


## MAJOR-2 – ALP MCMC “9,720 samples” and dataset description lack external support

**Location:** §6 “MCMC parameter estimation” paragraph  

**Issue:** The text claims “Dedicated MCMC sampling … (3 configurations, 9,720 total accepted samples)… Planck PR4 + ACT DR6 EB-spectrum likelihoods”, with internal configuration labels and Appendix A pointer, but there is no cited external paper or public dataset matching this specific ALP+β fit (with fixed C_{aγ}=4,8,12 on Planck PR4 + ACT DR6 EB). No arXiv reference is given, and this sounds like an internal analysis presented as if it were a published result; the distinction between “our internal fit” and “published analyses” is blurred when it is juxtaposed directly with “the observed β_obs = 0.342° ± 0.094°”.  

**Fix:** Explicitly mark this ALP MCMC as an **original, unpublished analysis** (internal to this work), not as a literature result, and remove phrasing that suggests it is a “published” or standard reference. Clarify that only the β_obs number is taken from the literature, and ensure no external paper is implicitly credited for this 9,720‑sample ALP fit.


## MAJOR-3 – Combined Planck/ACT “β_combined = 0.241° ± 0.061° (3.9σ)” not tied to any specific literature method

**Location:** §6 “Summary-likelihood combination (auxiliary cross-check)”  

**Issue:** The inverse-variance combination of β = 0.30° ± 0.11° (Planck NPIPE) and β = 0.215° ± 0.074° (ACT DR6) to β_combined = 0.241° ± 0.061° is presented as a straightforward auxiliary cross-check, but the specific input numbers and their error bars are not both directly traceable to single canonical Planck and ACT birefringence papers with those exact values; published Planck and ACT measurements use different pipelines, masks, and systematics treatments, and no literature reference is given that actually performs this exact 3.9σ combination.  

**Fix:** Either (a) cite the exact Planck and ACT DR6 papers whose central values and uncertainties you use and clearly label this as an *author’s own toy combination with shared systematics neglected*, or (b) drop the explicit 0.241° ± 0.061° (3.9σ) number and just state qualitatively that a naive inverse-variance combination would yield a slightly higher nominal significance than the published joint 3.6σ analysis.


## minor-1 – DESI DR2 BAO reference metadata likely stale / mismatched

**Location:** §5 “Datasets and Configuration” (DESI 2024 DR1 BAO[DESI2024]); conclusion “Forward” paragraph referencing DESI DR2; multiple mentions of “DESI DR2 w₀w_a iter2 chain”  

**Issue:** The text oscillates between “DESI 2024 DR1 BAO” and “DESI DR2” in describing the BAO dataset, but there is only a single DESI BAO reference key (DESI2024 / DESI2025DR2) promised in the comments. Externally, DESI DR1 BAO and DR2 BAO correspond to different arXiv numbers and years; using a single DESI 2024 citation for a DESI DR2 chain (and for “DESI 2025 DR2” in the comments) risks mixing DR1 and DR2 metadata (year, title, collaboration paper) and confusing which exact public release is actually used.  

**Fix:** Standardize on the correct DESI data release actually used in the MCMC (DR1 *or* DR2), and update the in‑text labels and the .bib entry so that the arXiv ID, year, and title match that release exactly (e.g., “DESI Collaboration 2024, DR1 BAO” vs “DESI Collaboration 2025, DR2 BAO”).


## minor-2 – Riess SH0ES reference year / label mismatch

**Location:** §2 “Cosmological Tensions”; iter2 caveats paragraph (references to `H0.riess2020Mb` and “Riess+2020 SH0ES value”); §5 datasets list citing Riess2022  

**Issue:** The SH0ES prior is variously described via a YAML alias `H0.riess2020Mb` (suggesting a 2020 calibration paper) and cited in the text as “Riess+2020 SH0ES value M_B = −19.253 ± 0.027 mag”, while the cosmological-tensions section and dataset list cite “Riess2022” for the H₀ prior. Riess et al. 2021/2022 and the 2020 M_B calibration papers are distinct; conflating “Riess 2020 M_B” with “Riess 2022 H₀” under a single bibkey obscures which publication each number comes from.  

**Fix:** Split the SH0ES citations into two clearly labeled entries (e.g., Riess et al. 2020 for M_B calibration; Riess et al. 2022 for the latest H₀ measurement) and reference each explicitly where its numbers are used, while adjusting the YAML alias description so it is consistent with the cited publication year.
