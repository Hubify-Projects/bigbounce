# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round6
**Wall time**: 19.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29487, completion=1864, total=31351, search_context_size=low, cost={'input_tokens_cost': 0.08846, 'output_tokens_cost': 0.02796, 'request_cost': 0.006, 'total_cost': 0.12242}

---

## BLOCKER-1 — Eskilt & Komatsu dataset description is still wrong / internally inconsistent  

**Location:** Abstract, birefringence paragraphs around line 170; §VI “Headline observational constraint” paragraph.  

**Issue:** The paper now claims the Eskilt & Komatsu result is a “joint WMAP+Planck value” and describes it as “the joint WMAP9 + Planck PR4/NPIPE analysis”, but the actual paper is *“Cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data”*, Phys. Rev. D 106, 063503 (2022), arXiv:2205.13962, which uses WMAP9 plus **Planck-2018 PR3**, not PR4/NPIPE.[1][2] The text has contradictory labels (“WMAP+Planck” generically vs. “PR4/NPIPE” specifically), and the “PR4/NPIPE” part is factually wrong.  

**Fix:** Harmonize all references to Eskilt & Komatsu 2022 as “WMAP9 + Planck 2018 (PR3)” and remove “PR4/NPIPE” wording everywhere; check that all places mentioning “joint WMAP+Planck value” also explicitly say “PR3” and not PR4/NPIPE, and ensure that any comparison to NPIPE is clearly attributed to other works (e.g., Diego Palazuelos et al.), not to Eskilt & Komatsu 2022.  

[1] arXiv:2205.13962  
[2] Phys. Rev. D 106, 063503 (2022)  


## MAJOR-1 — “Planck NPIPE” tag in NaMaster section contradicts cited birefringence source  

**Location:** §4 “Data Methods: CMB E–B Analysis” and NaMaster verification section.  

**Issue:** The NaMaster pipeline tests are described as being run on the Planck Commander map, and the discussion then connects their $\beta$ injections to “the published joint WMAP+Planck value” and the “Planck NPIPE” measurements.[3] The only birefringence value explicitly cited as “joint WMAP+Planck” is again Eskilt & Komatsu 2022, which is **PR3**, not NPIPE; the separate Planck NPIPE birefringence constraint is due to Diego-Palazuelos et al. (Planck PR4/NPIPE + WMAP + ACT), arXiv:2201.07682, PRL 128, 091302.[4] The current prose blurs these two and risks attributing NPIPE properties to Eskilt & Komatsu.  

**Fix:** Explicitly separate (a) Eskilt & Komatsu 2022 (WMAP9 + Planck 2018 PR3) from (b) Diego-Palazuelos et al. 2022 (Planck PR4/NPIPE + WMAP + ACT DR4/DR6), and ensure every statement about NPIPE/ACT DR6 is only tied to Diego-Palazuelos et al., not to Eskilt & Komatsu.  

[3] This manuscript, NaMaster verification section  
[4] arXiv:2201.07682, PRL 128, 091302 (2022)  


## MAJOR-2 — In-text description of Liu et al. torsion paper does not match cited title/scope  

**Location:** §3 “Independent cross-validation” paragraph citing “Liu et al. ECTorsionDESI2025” / EPJC 2025.  

**Issue:** The paper states that “Liu et al. … constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6)”. The bibkey is said to correspond to an EPJC 2025 paper (arXiv:2507.04265), which does not yet exist in the public record and whose title/scope cannot be verified; there is also no current EPJC paper matching that combination of authors, datasets, and a ΔAIC preference for “torsion” in DESI DR2-era data.[5][6] This looks like forward-dated or program-internal work being described as a published, independent cross-check.  

**Fix:** Unless and until arXiv:2507.04265 and the corresponding EPJC paper actually exist and can be verified to use exactly this dataset combination and AIC results, rephrase this to either (a) “in-preparation internal analysis” with no journal claim, or (b) remove the “EPJC 2025” and “Liu et al.” cross-validation entirely.  

[5] arXiv and ADS searches for Liu + Li + Xu + Biesiada + Wang torsion + DESI  
[6] EPJC database search through 2024/early-2025  


## MAJOR-3 — Diego-Palazuelos 2025 ACT DR6 paper metadata not verifiable  

**Location:** Multiple places where “DiegoPalazuelos2025 ACT DR6” with arXiv:2509.13654 is cited as a real 2025 paper.  

**Issue:** The manuscript asserts a 2025 paper “Diego Palazuelos & Komatsu 2025 (arXiv 2509.13654)” giving an ACT DR6 birefringence measurement.[7] There is currently no arXiv:2509.13654 entry, and no ACT DR6 birefringence paper by Diego-Palazuelos & Komatsu dated 2025; the only publicly visible ACT+Planck birefringence work is the 2022 PRL paper (arXiv:2201.07682) at DR4/DR6-era, not a 2025 DR6-only update.[4] Treating this as an existing, citable result is misleading.  

**Fix:** Downgrade all references to this 2025 ACT DR6 paper to “in preparation” / “forthcoming” or remove them until a real arXiv ID and journal entry exist; do not quote numerical values from it as if peer-reviewed unless they match a publicly verifiable paper.  

[4] arXiv:2201.07682, PRL 128, 091302 (2022)  
 ACT/Simons Observatory publication list as of 2024–2026  


## minor-1 — Fujita et al. citation wording slightly overstates novelty  

**Location:** §6 “Spectator-ALP consistency check”, opening note: “The model class was previously studied by Fujita et al. (2021)”.  

**Issue:** Fujita et al., “Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy” (Phys. Rev. D 103, 043509, arXiv:2011.11894), indeed studies ALP interpretations of birefringence but in a somewhat different parameterization and with a broader DE focus. Saying “the model class was previously studied” is defensible but a bit strong, as your specific coupled-trajectory scan and $C_{a\gamma}$ ranges are not literally the same as theirs.  

**Fix:** Soften wording to “closely related ALP interpretations were studied by Fujita et al. (2021)” or similar, to avoid implying exact model equivalence.  

 arXiv:2011.11894, PRD 103, 043509 (2021)  


## nit-1 — LiteBIRD forecast number should be explicitly tied to a specific collaboration document  

**Location:** §6 “LiteBIRD forecast” paragraph claiming “LiteBIRD is projected to achieve σ(β) ≈ 0.03°”.  

**Issue:** LiteBIRD cosmic-birefringence sensitivities are quoted in various units and scenarios (radians vs degrees, different sky models) across different collaboration documents; σ(β) ≈ 0.03° is plausible but should be explicitly grounded in a particular forecast paper or instrumental white paper, e.g. LiteBIRD collaboration JCAP 2022/2023 forecast or the Phase A report. Right now, the statement lacks a precise bibliographic anchor.  

**Fix:** Add a specific citation (LiteBIRD Collaboration forecast paper or technical report) and, if necessary, note the underlying assumption (full mission, fiducial sky model) under which σ(β) ≈ 0.03° is obtained.  

 LiteBIRD Collaboration forecast papers on CMB polarization and cosmic birefringence  
 LiteBIRD Phase A / design reports where σ(β) is tabulated
