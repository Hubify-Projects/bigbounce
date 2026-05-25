# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-25_R-ext_P5_v0_1_30
**Wall time**: 22.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=25221, completion=1511, total=26732

---

## PAPER-PER-B1 – Mis-citation of Tempel et al. 2014 dataset (DR10 vs DR10+DR12)

**Location:** Comment block near top (`v0.1.3` changelog) and §Tempel cross-validation text describing catalog origin.

**Issue:** The paper states “Tempel+2014 SDSS DR10 FoF catalog INGESTED from CDS VizieR J/A+A/566/A1 — 588,193 galaxies,” while the cited Tempel et al. paper (A&A 566, A1, 2014, arXiv:1402.1350) is based on SDSS DR10 but the CDS catalog there is “Flux- and volume-limited groups/clusters for the SDSS galaxies” with 588,193 galaxies and 82,458 groups, not a pure “FoF catalog” of galaxies alone as phrased here.[3] The wording risks fusing the group-catalog description with a galaxy-level FoF catalog that does not exist separately under that ID.

**Fix:** Rephrase the provenance to match Tempel et al.’s actual description, e.g. “Tempel et al. (2014) SDSS DR10 flux- and volume-limited group/cluster catalog (FoF-based, 588,193 galaxies in 82,458 groups) from CDS VizieR J/A+A/566/A1” and ensure any references to a “FoF catalog of 588,193 galaxies” explicitly mention it is the DR10 group catalog, not a distinct DR12 or DR10+DR12 product.[3]


## PAPER-PER-M1 – Incomplete author list for Tempel et al. 2014

**Location:** Bibliography, `\bibitem{Tempel2014}`.

**Issue:** The author list is truncated compared to the actual paper. Tempel et al. 2014 A&A 566 A1 lists additional co-authors (e.g. I. Suhhonenko, R. Kipper, M. Einasto) beyond those included here.[3] For a bib entry that otherwise gives full names, this is an accuracy issue.

**Fix:** Update the author list in the bibitem to match the full author list from the article (as given on arXiv:1402.1350 / A&A 566 A1) or truncate explicitly with “et al.” after the first few authors rather than listing a partial set.[3]


## PAPER-PER-M2 – Shamir 2022 citation: title mismatch

**Location:** Bibliography, `\bibitem{Shamir2022DESI}` and §Comparison to Shamir 2022.

**Issue:** The bibliography gives the title “Asymmetry between galaxies with clockwise and counterclockwise handedness in DESI Legacy Survey data,” whereas the actual title on arXiv:2208.13866 and in MNRAS is “Analysis of spin directions of galaxies in the DESI Legacy Survey.”[4] The current title is close in spirit but not the published one, so this is a fused/approximate title rather than a faithful citation.

**Fix:** Replace the title string with the published/arXiv title “Analysis of spin directions of galaxies in the DESI Legacy Survey.”[4]


## PAPER-PER-M3 – Hahn et al. 2007 author order / list mismatch

**Location:** Bibliography, `\bibitem{Hahn2007}`.

**Issue:** The arXiv/Journal record for astro-ph/0610280 lists authors as “Oliver Hahn, Cristiano Porciani, C. Marcella Carollo, Avishai Dekel.”[1] The bibitem currently lists “O.~Hahn, C.~M.~Carollo, C.~Porciani, and A.~Dekel,” which both changes the Porciani/Carollo order and abbreviates first names in a way that could create confusion when cross-checking with databases.

**Fix:** Adjust the author sequence to match the published order (“O. Hahn, C. Porciani, C. M. Carollo, and A. Dekel”) while keeping your journal formatting, or collapse to “O. Hahn et al.” to avoid partial reordering.[1]


## PAPER-PER-m1 – Hoffman et al. 2012 classification description slightly off

**Location:** §V-Web cosmic-web classification (“We compute environment labels via the V-Web tidal-tensor classifier (Hahn et al. 2007; Hoffman et al. 2012; Cautun et al. 2014)” and the subsequent algorithm list).

**Issue:** Hoffman et al. 2012 (arXiv:1201.3367) defines the “V-web” using the velocity shear tensor rather than the gravitational tidal tensor used in the original T-web / Hahn et al. 2007; the abstract explicitly states “the new algorithm is based on the analysis of the velocity shear tensor rather than the gravitational tidal tensor.”[2] Your algorithm description uses a potential-based tidal tensor \(T_{ij} = k_i k_j \Phi(k)\), which is a T-web, not a velocity-shear V-web, but cites Hoffman et al. as if it were the exact method implemented.

**Fix:** Clarify that your implementation follows a tidal-tensor (T-Web-style) classifier inspired by Hahn et al. 2007, with Hoffman et al. 2012 cited for conceptual context about kinematic/velocity-based web classification rather than for the exact algorithm; alternatively, modify the algorithm to actually use the velocity shear tensor if you intend a true V-web in the Hoffman sense.[1][2]


## PAPER-PER-n1 – Minor mismatch in Cautun et al. 2014 method label

**Location:** §V-Web cosmic-web classification, step 11 and surrounding text (referring to “Cautun et al. geometric default \(\lambda_{\rm th}=0\)”).

**Issue:** Cautun et al. 2014 (arXiv:1401.7866) focuses on the NEXUS/NEXUS+ multiscale morphology filter rather than a single-scale tidal-tensor classifier with a fixed \(\lambda_{\rm th}=0\); the paper does discuss volume fractions and morphology but does not introduce \(\lambda_{\rm th}=0\) as a canonical “geometric default” in the same simple T-web scheme you use.[2] The current wording could mislead readers into thinking that specific threshold choice is directly prescribed by Cautun et al.

**Fix:** Soften the attribution to something like “following common T-/V-web practice (e.g. Hahn et al. 2007) we adopt \(\lambda_{\rm th}=0\); Cautun et al. 2014 discuss related morphological fractions with NEXUS/NEXUS+” rather than calling \(\lambda_{\rm th}=0\) the Cautun “geometric default.”[1][2]




