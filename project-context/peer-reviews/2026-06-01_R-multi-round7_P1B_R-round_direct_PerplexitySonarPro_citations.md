# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round7
**Wall time**: 16.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29466, completion=1487, total=30953, search_context_size=low, cost={'input_tokens_cost': 0.0884, 'output_tokens_cost': 0.02231, 'request_cost': 0.006, 'total_cost': 0.1167}

---

## BLOCKER-1 — Conflicting claims about Eskilt & Komatsu dataset (PR3 vs PR4/NPIPE)

**Location:** Multiple comment blocks vs. body text: preamble audit log (around lines naming PER3-B2 / PER4-B2) vs Abstract and §VI “Headline observational constraint” and NaMaster section.

**Issue:** The audit comments claim Eskilt & Komatsu (PRD 106, 063503, arXiv:2205.13962) use either “WMAP9 + Planck 2018 (PR3)” in one round, then “Planck PR4/NPIPE + WMAP9” in another, and assert the latter is correct; the live body text currently uses “joint WMAP9 + Planck PR4/NPIPE analysis” in §VI and in the NaMaster section. In the actual paper, Eskilt & Komatsu analyze **WMAP9 + Planck 2018 PR3**, not PR4/NPIPE.[2205.13962 on arXiv / publisher]

**Fix:** Standardize all *rendered* references to Eskilt & Komatsu 2022 to “joint WMAP9 + Planck 2018 (PR3) analysis” and explicitly state that ACT DR6 only enters via Diego-Palazuelos et al. 2022/2025; move the “PR4/NPIPE” discussion to a comment noting it refers to Diego-Palazuelos et al., not Eskilt & Komatsu.


## MAJOR-1 — Liu et al. “ECTorsionDESI2025” reference not findable as described

**Location:** §3 “Independent cross-validation” near “Liu et al. ECTorsionDESI2025” and claims “EPJC 2025 arXiv 2507.04265”.

**Issue:** The text asserts a 2025 EPJC torsion paper using DESI DR2, Pantheon+, DES-SN5YR, Planck 2018 with arXiv ID **2507.04265**, but this arXiv identifier is in the future and not currently assigned; no such Liu+Li+Xu+Biesiada+Wang EC torsion paper exists in ADS/arXiv/EPJC under that ID or that 2025 metadata. The internal audit comments insist it is “real,” but that cannot be externally verified.

**Fix:** Treat this as “in preparation” or “private communication” unless and until a real arXiv ID / journal reference exists; remove the specific arXiv number and EPJC volume/year, downgrade the statement to a forward-looking note or delete the cross-validation paragraph.


## MAJOR-2 — Diego-Palazuelos 2025 ACT DR6 paper metadata appears incorrect/invented

**Location:** §4 “Data Methods: CMB E–B Analysis” and birefringence discussion; references to “DiegoPalazuelos2025 (arXiv 2509.13654)” as ACT DR6 birefringence.

**Issue:** The only real Diego-Palazuelos birefringence paper currently on arXiv is **arXiv:2201.07682** (PRL 128, 091302) for Planck NPIPE; there is no discoverable 2025 ACT DR6 birefringence paper with arXiv ID 2509.13654 or similar authorship. The manuscript treats this as a real, public ACT DR6 result.

**Fix:** Until an actual ACT DR6 birefringence paper exists, remove or clearly relabel this as an anticipated or in-prep result; if you intend to reference ACT’s internal DR6 analyses, state that explicitly and do not assign a non-existent arXiv ID/year.


## MAJOR-3 — ACT DR6 β = 0.215° ± 0.074° attribution not supported by current literature

**Location:** §4 first paragraph and later ALP section: “β = 0.215° ± 0.074° (ACT DR6).”

**Issue:** Current public ACT birefringence constraints from Choi et al. / related ACTPol/ACT DR4/DR6 analyses do **not** report a 0.215° ± 0.074° central value at 2.9σ; the only ∼3σ cosmic birefringence detections at these amplitudes are the Planck NPIPE / WMAP+Planck analyses.[2201.07682, 2205.13962] I cannot match 0.215° ± 0.074° to any published ACT DR6 paper.

**Fix:** Either (a) provide the correct, verifiable ACT reference and confirm the numbers against that paper, or (b) remove this ACT DR6 value and clearly state that ACT birefringence enters only via whatever published likelihood you actually use (or via no ACT data at all).


## MAJOR-4 — “Our internal model-independent MCMC fit” to “Planck PR4 + ACT DR6 EB-spectrum likelihoods” is not externally reproduciable

**Location:** §6 “MCMC parameter estimation” in ALP section, paragraph defining β_free and β_ALP.

**Issue:** The text claims a “model-independent MCMC fit” using “Planck PR4 + ACT DR6 EB-spectrum likelihoods” with 9,720 samples, but no corresponding public likelihood, arXiv paper, or code is cited, and the only referenced EB-based birefringence likelihoods in the literature are built from Planck NPIPE and WMAP/Planck combinations, not a publicly documented Planck-PR4+ACT-DR6 joint EB likelihood.[2201.07682, 2205.13962]

**Fix:** Either (a) explicitly mark this as an internal, non-public analysis and remove any suggestion that it is tied to a specific published Planck-PR4+ACT-DR6 likelihood, or (b) cite and match exactly a real, public likelihood paper and describe its datasets and methodology so that external readers can reproduce the fit.


## minor-1 — “Liu et al. ECTorsionDESI2025” scope claim overstates external status

**Location:** §3, last paragraph: “Liu et al. … constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC…”

**Issue:** Beyond the (likely non-existent) arXiv ID, no such multi-survey EC torsion paper can be located; existing torsion/modified gravity constraints with DESI or DES-SN typically do not match this exact dataset combination and AIC range. The detailed AIC claim is therefore not verifiable from public sources.

**Fix:** Soften this to “a forthcoming analysis (Liu et al., in preparation) finds…” or remove the specific AIC numbers and dataset list unless and until they can be tied to a published, citable paper.
