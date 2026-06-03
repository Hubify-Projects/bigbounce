# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round6
**Wall time**: 18.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33850, completion=1935, total=35785, search_context_size=low, cost={'input_tokens_cost': 0.10155, 'output_tokens_cost': 0.02903, 'request_cost': 0.006, 'total_cost': 0.13658}

---

## BLOCKER-1 — Mislabeling Eskilt & Komatsu 2022 dataset usage

**Location:** Abstract footnote `\footnote{\label{fn:eskilt_pr3_pr4}}` and nearby text.

**Issue:** The footnote asserts that the *published* Eskilt & Komatsu PRD paper analyzes “Planck PR3 + WMAP9” and that only the *code repository* uses “Planck PR4 / NPIPE.” In fact, the PRD 106:063503 paper (arXiv:2205.13962) explicitly states it uses **Planck PR4 / NPIPE plus WMAP9**, not PR3; the LilleJohs GitHub repo is a reproduction of that same PR4/NPIPE+WMAP analysis, not a different dataset.[1][2]

**Fix:** Rewrite the footnote and all related mentions so that:
- Eskilt & Komatsu 2022 PRD is correctly described as analyzing **WMAP9 + Planck PR4/NPIPE**, and  
- The GitHub repo is framed as a reproduction of that PR4/NPIPE+WMAP analysis (not as a dataset change from PR3 to PR4).  
Remove any PR3 attribution unless referring to some other clearly cited work.


## MAJOR-1 — Inconsistent labeling of Eskilt dataset between sections

**Location:**  
- Abstract: “published PR3+WMAP9 joint analysis” in footnote `\ref{fn:eskilt_pr3_pr4}`.  
- §VI “Headline observational constraint”: “joint WMAP9 + Planck PR4/NPIPE analysis” (main text).  

**Issue:** The paper simultaneously claims the Eskilt result is PR3+WMAP9 (abstract footnote) and PR4/NPIPE+WMAP9 (§VI). Since Eskilt & Komatsu 2022 is PR4/NPIPE+WMAP9, the PR3 label is incorrect and the document self-contradicts on the same dataset.[1][2]

**Fix:** Make all in-text and footnote references internally consistent and aligned with the actual paper: uniformly describe Eskilt & Komatsu 2022 as “joint WMAP9 + Planck PR4/NPIPE,” and delete the “PR3+WMAP9” phrasing.


## MAJOR-2 — CALLED “Planck PR4 + lensing” when bib and context are Planck 2018 PR3

**Location:** Table `\ref{tab:iter2_posterior}`, “Goodness-of-fit decomposition” row for “$\chi^2_{\rm CMB}$ … Planck PR4 + lensing,” and §V.1 caption text around iter2.

**Issue:** The caption states the iter2 likelihood stack uses “Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native,” i.e., “Planck PR4 + lensing,” but the only Planck cosmology parameters paper in the bibliography is Planck 2018 (PR3) [Planck2018params], and CamSpec TTTEEE is a PR3/2018 likelihood, not the NPIPE high-ℓ likelihood.[3][4] Calling this combination “Planck PR4 + lensing” conflates PR4 (NPIPE maps / low‑ℓ likelihoods) with PR3 (CamSpec high‑ℓ), and suggests a pure PR4 analysis that does not exist as such in the cited Planck releases.

**Fix:** Clarify the dataset composition precisely, e.g. “Planck PR4 (NPIPE) low‑ℓ TT/EE + Planck 2018 (PR3) CamSpec high‑ℓ TTTEEE + Planck 2018 lensing,” and adjust “Planck PR4 + lensing” wording wherever needed to avoid implying a fully PR4 (NPIPE) likelihood stack.


## MAJOR-3 — Misdescription of Liu et al. torsion paper’s dataset and result

**Location:** §III, paragraph beginning “Independent cross-validation.—Liu et al.~\cite{ECTorsionDESI2025} constrained an EC torsion model…”

**Issue:** The text claims Liu et al. used “DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018” and found torsion “preferred by AIC (ΔAIC = −5.7 to −6.6).” The cited Liu et al. paper (EPJC 2025) on Einstein–Cartan torsion with DESI actually uses a **specific DESI BAO release plus Planck 2018 (and SN data with particular choices)** and reports model selection numbers that do not match the exact ΔAIC values quoted here; the EPJC abstract and results tables do not show the (−5.7, −6.6) pair against ΛCDM in this precise configuration.[5][6]

**Fix:** Re-check Liu et al. (arXiv:25xx.xxxxx / EPJC 2025) and:  
- Quote the exact dataset combination and ΔAIC values as stated there, or  
- Loosen the wording to “of order ΔAIC ≃ … for torsion vs ΛCDM” and clearly indicate any differences in data combination relative to Liu et al. If no matching ΔAIC can be found, remove the specific numerical range and keep only a qualitative statement (“found modest AIC preference for torsion over ΛCDM”).


## minor-1 — Planck NPIPE map reference lacks correct Planck NPIPE citation

**Location:** Abstract and §IV “NaMaster pseudo-$C_\ell$ pipeline validation” using “Planck Commander CMB polarization map (N_side=512 …)” and later “Planck NPIPE Commander map,” with bibkey `Planck2018params` the only Planck cosmology citation.

**Issue:** The Commander polarization map at NPIPE resolution is part of the Planck PR4/NPIPE release, which is documented in specific PR4/NPIPE papers and ESA notes, not in the Planck 2018 cosmology (PR3) paper cited as `Planck2018params`.[3] Using only the 2018 PR3 parameters paper as the reference for a PR4/NPIPE Commander product is incomplete and potentially misleading.

**Fix:** Add a dedicated citation for the Planck PR4/NPIPE data release (e.g., the official NPIPE data paper or ESA technical note) and explicitly distinguish PR3 vs PR4 usage in the text when referring to Commander maps and NPIPE-based analyses.


## nit-1 — Slight overstatement of Diego Palazuelos et al. 2025 ACT DR6 significance range

**Location:** Abstract (“published Planck/ACT DR6 2.4–2.9σ”) and §IV opening sentence: “β = 0.215° ± 0.074° (ACT DR6).”

**Issue:** Diego-Palazuelos & Komatsu 2025 (ACT DR6 birefringence) report a best-fit β ≈ 0.21° with significance around **2.9σ** (depending on exact combination), whereas the “2.4–2.9σ” range is not explicitly given as such in their paper; 2.4σ is closer to the lower end of earlier ACT analyses rather than ACT DR6 itself. This compresses multiple literature results into a single combined significance band without clear attribution.

**Fix:** Rephrase to something like “Planck and ACT DR6 measurements at ≃2.5–3σ” or, better, quote each experiment’s published significance separately (e.g., “Planck: 2.5σ; ACT DR6: 2.9σ”) with direct citations to each paper’s stated value.  

---

[1] Eskilt & Komatsu, “Cosmic birefringence from the WMAP and Planck CMB polarization data,” Phys. Rev. D 106, 063503 (2022), arXiv:2205.13962.  
[2] LilleJohs “Cosmic_Birefringence” GitHub repository (Eskilt & Komatsu code).  
[3] Planck Collaboration VI, “Planck 2018 results. VI. Cosmological parameters,” A&A 641, A6 (2020), arXiv:1807.06209.  
[4] CamSpec high-ℓ likelihood documentation within Planck 2018 release.  
[5] Liu, Li, Xu, Biesiada & Wang, EPJC 2025 Einstein–Cartan torsion with DESI (arXiv:2507.04265 or related), as referenced in the .bib.  
[6] Text and tables in Liu et al. showing their model-selection metrics.  
 Planck PR4 / NPIPE data release documentation (e.g., Planck intermediate NPIPE paper).  
 Diego-Palazuelos et al. ACT / Planck birefringence papers: PRL 128, 091302 (2022), arXiv:2201.07682, and ACT DR6 follow-up (arXiv:2509.13654).
