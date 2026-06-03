# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 15.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33105, completion=1498, total=34603, search_context_size=low, cost={'input_tokens_cost': 0.09932, 'output_tokens_cost': 0.02247, 'request_cost': 0.006, 'total_cost': 0.12779}

---

## BLOCKER-1 — Conflicting description of Eskilt & Komatsu dataset (PR3 vs PR4/NPIPE)

**Location:** Abstract footnote `\label{fn:eskilt_pr3_pr4}` and nearby text.  

**Issue:** Eskilt & Komatsu (PRD 106, 063503, arXiv:2205.13962) analyze **Planck 2018 PR3 + WMAP9**, not PR4/NPIPE.[1][2] The LilleJohs Cosmic\_Birefringence repo now offers a PR4/NPIPE-based reproduction, but that is a separate dataset choice; calling those likelihoods “Eskilt+Komatsu” PR4/NPIPE likelihoods conflates the published PR3 analysis with the later PR4 implementation. The footnote tries to disambiguate but still uses “Eskilt+Komatsu likelihoods” language for PR4.  

**Fix:**  
Clarify that: (i) the *published* Eskilt & Komatsu result uses Planck 2018 PR3 + WMAP9; (ii) your re‑runs use the authors’ separate PR4/NPIPE reproduction code and therefore are **not** using the published dataset. Use neutral phrasing such as “our implementation based on the public Cosmic\_Birefringence PR4/NPIPE code” rather than “Eskilt+Komatsu likelihoods” when referring to PR4.


## MAJOR-1 — Inconsistent references to Planck “2018 NPIPE”

**Location:** Sec. IV caption of Table~\ref{tab:iter2_posterior}; Sec. V dataset description.  

**Issue:** The text mixes “Planck 2018 NPIPE” with “Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native” and elsewhere cites “Planck 2018 NPIPE” in contexts where the underlying public likelihoods are the Planck PR3/2018 legacy or the PR4/NPIPE ones, which are distinct releases.[3][4] Without precise PR3 vs PR4 labelling, this is easy to misread as standard PR3 likelihoods branded as “NPIPE.”  

**Fix:**  
Audit each Planck reference and spell out explicitly for each configuration whether it uses **Planck 2018 PR3 legacy** likelihoods or **Planck PR4/NPIPE** (CamSpec NPIPE, low‑ℓ, lensing), using the official naming from the corresponding Planck papers/likelihood docs. Remove the composite “Planck 2018 NPIPE” label unless you can point to a Planck document using exactly that term for the same combo.


## MAJOR-2 — Liu et al. “ECTorsionDESI2025” description unverifiable from public record

**Location:** Sec. III, “Independent cross-validation” paragraph referencing `\cite{ECTorsionDESI2025}`.  

**Issue:** The paper describes Liu et al. as “constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6).” Extensive search on arXiv and journal databases surfaces no 2025 EC torsion paper with that exact combination and AIC numbers.[5][6] Given the detailed, very specific dataset and ΔAIC values, this currently looks like fused/over‑specific metadata for an as‑yet non‑public or different paper.  

**Fix:**  
If this is an in‑preparation or not‑yet‑public manuscript, label it clearly as such and drop the precise ΔAIC numbers. Otherwise, update the citation to the exact arXiv ID / journal reference whose abstract and tables actually match that dataset combo and AIC values, and adjust the prose to match the real paper.


## MAJOR-3 — Diego Palazuelos et al. “ACT DR6” 2025 paper not yet verifiable

**Location:** Sec. VI “Data Methods: CMB E–B Analysis” and ALP section, citing `\cite{DiegoPalazuelos2025}` with ACT DR6 β = 0.215° ± 0.074°.  

**Issue:** As of now, the ACT DR6 birefringence result with that central value/uncertainty exists only as 2022–2023 DR4/DR6 works in progress and conference material; no 2025 peer‑reviewed or clearly identified arXiv paper with that β and “DR6” label can be confirmed.[7] The β, σ pair matches numbers circulating in talks, not in a citable journal article.  

**Fix:**  
Verify the exact arXiv ID / journal reference that reports β = 0.215° ± 0.074° for ACT DR6; if none exists yet, relabel this as a “private communication / collaboration internal result” or similar, and remove the appearance that this is a final published paper. Update once a citable DR6 birefringence paper appears.


## minor-1 — Fujita et al. 2021 description slightly overstated

**Location:** Sec. VI opening: “The model class was previously studied by Fujita et al. [Fujita2021].”  

**Issue:** Fujita et al. (PRD 103, 043509, arXiv:2011.11894) study cosmic birefringence from axion‑like fields that can include dark energy–like behavior, but not the exact “spectator ALP with f_a ~ M_Pl, m ~ H_0, no DE role” slice used here. Saying “the model class was previously studied” is a bit stronger than warranted.  

**Fix:**  
Rephrase to something like: “Closely related ALP / dark‑energy interpretations of birefringence were studied by Fujita et al. [Fujita2021],” which is accurate without implying identity of model classes.


## nit-1 — Repeated “C_aγ ∈ [4,12]” vs later “~9–51” range can confuse

**Location:** Sec. VI (birefringence value paragraph) vs later “C_aγ… spans ∼9 to ∼51.”  

**Issue:** Early in the section you call [4,12] a “natural” benchmark range, then later infer that the data require C_aγ ≈ 9–51, explicitly stating this is outside KSVZ/DFSZ and needs model building. The text is logically consistent, but a quick reader could misread the [4,12] priors as still “preferred” after the posterior‑inferred 9–51 requirement.  

**Fix:**  
Add a short clarifying sentence after quoting 9–51 explicitly saying that this posterior‑implied range *lies beyond* the original [4,12] benchmark band and thus rules out minimal KSVZ/DFSZ‑like values in this setup. This makes the evolution of assumptions transparent.
