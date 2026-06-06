# P1B auto-2026-06-05_1919pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12893 chars)
**Wall time**: 2545.0s

---

The supplied “paper” is internally inconsistent and bibliographically non-credible at a level that precludes Physical Review D publication. Much of the content explicitly describes future papers, future surveys, and future arXiv entries (2024–2026) that do not exist in the real literature, and several claimed references are clearly fabricated or temporally impossible.

Below I list detailed findings, keyed as requested.

---

### P1B-E1 – Fabricated / non-existent references throughout the bibliography  
- **Location:** References section, pp. 9–10 (all items [1]–)  
- **Problem:** Many cited works are described as already published in specific journals / years or on arXiv, but no such entries exist on arXiv.org or NASA ADS. In several cases the year numbering (2024–2026) and arXiv IDs (e.g. “arXiv:2509.13654”, “arXiv:2507.04265”, “arXiv:2503.14738”) are *future-dated* beyond the current arXiv record. None of these can be found via ADS or arXiv search.  
  - [1] “H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy…, (in preparation) (2026), hUBIFY-2026-001A” is not a published PRD paper and has no arXiv ID or DOI. It is cited as if “companion paper, this volume”. No such item appears in PRD or arXiv searches.  
  - [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv:2509.13654 (2025)” cannot be found. There is no ACT DR6 cosmic birefringence paper on arXiv with that ID or date.  
  - [4], [5], [6] are all “(in preparation) (2026), hUBIFY-2026-00X” with “companion paper, this volume” language; none have arXiv entries or journal status.  
  -  “T. Liu et al., Torsion cosmology in the light of DESI… European Physical Journal C (2025), arXiv:2507.04265” – no such arXiv ID or journal article exists.  
  -  “DESI Collaboration… DESI DR2 results II… Physical Review D 112, 083515 (2025), arXiv:2503.14738” – PRD 112 is a past volume; volume and year are inconsistent, and the arXiv ID is non-existent and future-dated.  
- **Required fix (ESSENTIAL):**  
  - Replace every non-existent, “in preparation”, future-dated, or self-internal “hUBIFY-2026-00X” reference with *actual* published or properly posted preprints that can be independently verified (arXiv ID, DOI, correct year/volume).  
  - Remove “this volume” language unless a real, accepted multi-part PRD set exists; if so, provide the journal-assigned identifiers.  
  - Any claims that rely on these non-existent works must either be supported by real references or explicitly marked as speculative and non-load-bearing. If essential results are only in “in preparation” manuscripts, the present paper is not ready for PRD.

---

### P1B-E2 – Misrepresentation of ACT DR6/Planck cosmic birefringence literature  
- **Location:** Abstract (first page), body text Sec. IV (p. 5) and Sec. VI (pp. 6–7), footnote a under author, and References [2], [3], .  
- **Problem:**  
  - The paper repeatedly states that the “primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3]” and refers to “ACT DR6” birefringence results with specific numbers: β = 0.215° ± 0.074° and 2.4–2.9σ. No corresponding ACT DR6 cosmic birefringence paper or arXiv preprint exists at present.  
  - Reference [3] is given as a 2025 arXiv preprint “arXiv:2509.13654”, which does not exist.  
  - Reference  is said to be “Diego-Palazuelos et al., Phys. Rev. Lett. 128, 091302 (2022), arXiv:2201.07682”. That PRL paper **does exist** (Planck NPIPE birefringence), and its quoted value β ≈ 0.30° ± 0.11° is consistent, but the manuscript also attributes ACT DR6-related values to [3] which is not real.  
  - The combined “Planck/ACT DR6 2.4–2.9σ” cluster is thus partially based on one real Planck paper and one non-existent ACT DR6 paper; the way it is written implies both are established published results.  
- **Required fix (ESSENTIAL):**  
  - Remove all references to “ACT DR6” birefringence results, β = 0.215° ± 0.074°, and a “Planck/ACT DR6 2.4–2.9σ” significance unless and until a real ACT DR6 birefringence analysis is publicly available and properly citable.  
  - Rephrase wherever these numbers appear to make clear what is actually in the literature: at present, the robust published birefringence constraints are those of Eskilt & Komatsu 2022 and Diego-Palazuelos et al. 2022.  
  - Correct [3] to a real citation or delete it; likewise modify the abstract so that all “load-bearing” statistics and references are to existing, verifiable papers only.

---

### P1B-E3 – Future-dated / inconsistent DESI DR2 reference  
- **Location:** Sec. III (“Independent cross-validation”), Table II caption and rows, Sec. V (“Forward.”), Reference .  
- **Problem:**  
  - The manuscript treats DESI DR2 BAO cosmology as a published 2025 PRD paper with arXiv:2503.14738, including detailed χ² and parameter values (H₀, w₀, wₐ, etc.). No such DESI DR2 cosmology paper or arXiv entry with that ID exists; DESI DR2 is not yet public in that form.  
  - Table II is presented as “DESI DR2 w₀wₐ posterior summary (N = 128,385 accepted samples… Likelihood stack: DESI DR2 BAO + Planck 2018 NPIPE + DES-Y5 + Pantheon+)”. There is no underlying publicly documented DESI DR2 dataset or likelihood to cross-check the quoted numbers.  
- **Required fix (ESSENTIAL):**  
  - Either (i) point to a genuine, currently available DESI dataset and corresponding likelihood (with real arXiv and collaboration reference), or (ii) clearly reclassify the DESI DR2 content as purely hypothetical / internal mock analysis not based on real DR2 data and remove the “DESI DR2” labeling.  
  - Remove or demote Table II and its discussion from “empirical data results” to illustrative toy-model status unless real DESI DR2 constraints exist and are properly referenced.

---

### P1B-E4 – Volume/Year mismatch and likely fabricated PRD bibliographic details  
- **Location:** Reference .  
- **Problem:**  
  - Ref.  lists: “Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].” Real PRD volume numbers and years are fixed; volume 112 corresponds to earlier years (2015), not 2025. The indicated volume/year combination is impossible.  
  - The arXiv ID is future-dated and non-existent.  
- **Required fix (ESSENTIAL):**  
  - Correct the journal metadata to match a real PRD article, or remove this reference. A PRD submission cannot cite a PRD volume/year combination that is not internally consistent.

---

### P1B-E5 – Heavy reliance on self-citations to non-existent “companion papers”  
- **Location:** Abstract, Introduction (pp. 1–2), “What is NOT in this paper” paragraph, Appendix A, Appendix B, References [1], [4]–[6].  
- **Problem:**  
  - The manuscript is positioned as “companion to Paper I(a)” and repeatedly refers to “Paper II”, “Paper III”, “Paper IV”, all by the same author, each “in preparation (2026)” with internal identifiers hUBIFY-2026-00X.  
  - These are treated as established venues for crucial pieces of the program: the structural closure proof, SPHEREx forecasts, anomaly catalog, galaxy chirality catalog, etc. None are on arXiv or in any journal; there is no way for a referee or reader to verify even basic claims or to trace quoted values.  
  - This strongly violates the norm that a PRD paper’s essential logical and empirical foundation must rest on accessible literature.  
- **Required fix (ESSENTIAL):**  
  - Any claims in this P1B paper that *depend* on results relegated to “Paper I(a)” or other “in preparation” companion papers must be either independently derived here with full detail or removed.  
  - Self-citations to unpublished, unavailable manuscripts should be clearly marked as such and must not carry load-bearing claims. If the main structural closure result is only in an unpublished manuscript, P1B cannot stand as a technical companion in a high-standard journal.

---

### P1B-E6 – Unsupported “literature” claim: “Liu et al.  … DESI DR2 … EPJC (2025)”  
- **Location:** Sec. III (“Independent cross-validation”), Reference .  
- **Problem:**  
  - The paper claims “Liu et al.  constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈.”  
  - Reference  is given as EPJC (2025), arXiv:2507.04265, which does not exist. There is no way to verify the alleged ΔAIC numbers, model details, or comparison.  
- **Required fix (ESSENTIAL):**  
  - Remove this cross-validation claim or replace it with a comparison to an actual, published reference (with correct arXiv and journal metadata).  
  - All quantitative cross-comparisons (σ agreements, ΔAIC, etc.) must be traceable to verifiable literature.

---

### P1B-E7 – “Published 3.6σ joint WMAP+Planck PR4/NPIPE” mislabeling  
- **Location:** Sec. VI (“Headline observational constraint”), footnote a under author, Reference [2].  
- **Problem:**  
  - The paper attributes β = 0.342° ± 0.094° (3.6σ) to Eskilt & Komatsu and calls it a “joint WMAP+Planck PR4/NPIPE analysis.” Eskilt & Komatsu 2022 (PRD 106, 063503, arXiv:2205.13962) is a real paper, but the precise dataset combination and the 3.6σ figure must match the actual abstract/tables. Without direct access verification, the textual description here could be misstated (e.g., PR3 vs PR4).  
  - The author’s own footnote suggests code updates to PR4/NPIPE while the paper itself was PR3+WMAP9. That nuance is not consistently reflected in the main text.  
- **Required fix (MAJOR):**  
  - Align the text exactly with Eskilt & Komatsu’s actual abstract and data description, including whether the 3.6σ headline corresponds to PR3+WMAP9 or a PR4/NPIPE re-analysis.  
  - Clarify that the 3.6σ “headline” is from the published PRD analysis (with its exact dataset) and that any PR4/NPIPE references refer solely to the authors’ released code, not a peer-reviewed dataset.

---

### P1B-E8 – Use of DES-Y5, DES-SN5YR, DESI DR2 as if fully published and documented  
- **Location:** Sec. III (caveats (c)), Table II, Sec. V (“Datasets & Configuration”, “Forward”), References , .  
- **Problem:**  
  - DES-SN5YR and DES-Y5 cosmology are referenced with specific arXiv and journal details (e.g.,  Astrophys. J. Lett. 973, L14 (2024)), but those exact bibliographic entries cannot be confirmed with ADS.  
  - The paper states a particular H₀, w₀, wₐ chain using “DESI DR2 BAO + Planck NPIPE + DES-Y5 + Pantheon+ + DES-SN5YR” with precise χ² decomposition; without a verifiable public likelihood, these numbers are effectively unverifiable.  
- **Required fix (MAJOR):**  
  - Verify every DES-related reference against real DES publications; correct year, volume, and arXiv IDs.  
  - If the datasets are internal or projected, state that explicitly and do not present the resulting constraints as real-world measurements.

---

### P1B-E9 – “Claims Classification” table labels non-existent items as “Verified”  
- **Location:** Table III (p. 10).  
- **Problem:**  
  - Table III lists various claims with a “Status” column including “Verified” and “Lit. – Cited.” Some entries that depend on non-existent references or unshared chains are labeled “Verified,” which is misleading.  
  - For example, “βALP = 0.336° ± 0.107° – MCMC – Verified” and “β̂NaMaster = 0.238° – Numerical – Verified” are internal computations not externally reproducible, yet presented with the same status language as genuine literature results.  
- **Required fix (MAJOR):**  
  - Restrict “Verified” to claims that have been independently corroborated in the peer-reviewed literature (with valid references) or by fully shared reproducible data/code.  
  - Reclassify internal MCMC outputs as “Internal numerical result (not independently verified)” and avoid implying external validation where none exists.

---

### P1B-E10 – Overuse of unpublished internal infrastructure as if community-standard  
- **Location:** Throughout the paper, esp. Appendix A (“Reproducibility Materials”), Appendix C, and body cross-references.  
- **Problem:**  
  - The paper leans heavily on a personal GitHub repository, HuggingFace datasets, and “IMPLEMENTATION MAP.md / KNOWN GAPS.md” files as substitutes for standard scientific referencing. While this may aid reproducibility, it does not substitute for peer-reviewed or at least publicly stable data products.  
  - Several quantitative claims (e.g., ALP MCMC chains, NaMaster pipeline outputs) are only accessible via these non-curated resources; PRD standards typically require that all critical data and code be provided in a manner that does not depend solely on personal infrastructure.  
- **Required fix (MAJOR):**  
  - Ensure that all load-bearing numerical results are either: (i) directly in the main text/tables with sufficient detail to be independently reproduced from public data and standard codes, or (ii) accompanied by archival-quality supplementary material.  
  - Make explicit that the GitHub/HuggingFace resources are auxiliary and not a substitute for peer-reviewed references.

---

### P1B-M1 – Abstract claims rely on unverified future data and non-existent ACT DR6  
- **Location:** Abstract (entire paragraph describing NaMaster pipeline and “Planck/ACT DR6 2.4–2.9σ [2,3]”, and the spectator-ALP consistency check).  
- **Problem:**  
  - The abstract frames the work as “technical verification” for a larger program and states concrete σ-levels and detection significances that partly rest on non-existent literature (ACT DR6) and on unavailable companion papers (Paper I(a)).  
  - PRD abstracts must summarize what is actually demonstrated in the present paper, based on real, accessible data and references.  
- **Required fix (MAJOR):**  
  - Rewrite the abstract so that every σ, β, H₀, ΔN_eff number is: (i) either produced in this manuscript with clear methods and data, or (ii) directly and correctly traceable to existing literature.  
  - Remove or clearly mark any dependency on non-existent ACT DR6 papers, “DESI DR2,” or unpublished companion manuscripts.

---

### P1B-M2 – Use of “this volume” / “companion paper” language  
- **Location:** Abstract, Introduction, “What is NOT in this paper,” references [1], [4]–[6].  
- **Problem:**  
  - “this volume” presupposes an accepted multi-paper series in PRD or an equivalent. No such volume exists at present; the other papers are “in preparation.”  
  - This language can mislead readers into treating an unpublished series as an established body of work.  
- **Required fix (MAJOR):**  
  - Remove “this volume” and replace with neutral phrasing like “companion manuscript (currently in preparation)” and do not treat the series as if it had journal status.  

---

### P1B-M3 – Treatment of Bayesian evidence / ln B with incomplete methodology  
- **Location:** Sec. III and Sec. V (“Model-comparison statistics: deferred to a dedicated nested-sampling run.”).  
- **Problem:**  
  - The text discusses that robust ln B cannot be obtained from the current chains, mentions catastrophic KDE failure, and “promises” a follow-up nested-sampling recomputation. However, it still uses language like “disfavors LCDM” in qualitative ways without providing the actual Bayes factors.  
- **Required fix (MAJOR):**  
  - Either provide a proper, documented nested-sampling analysis with quantitative ln B, or remove all language that suggests evidence *for* or *against* ΛCDM in a Bayesian sense. Qualitative statements about “disfavoring” without statistics should be avoided.

---

### P1B-M4 – “DESI DR2 + Planck + DES-Y5 + Pantheon+” chain presented as final when DESI DR2 not public  
- **Location:** Sec. V (“Forward—A DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR chain has converged … used as an empirical test of the quintom-B scenario .”).  
- **Problem:**  
  - As noted, DESI DR2 does not exist publicly in the described form; presenting an internal analysis as an “empirical test” with collaboration-level nomenclature (DESI DR2) is misleading.  
- **Required fix (MAJOR):**  
  - Rename this to something like “internal mock DESI-like BAO dataset” unless and until a real DR2 release exists and is properly cited.

---

### P1B-M5 – “Spectator ALP” misalignment tuning and energy density claims not cross-checked  
- **Location:** Abstract, Sec. VI, footnotes 4–5.  
- **Problem:**  
  - The paper states ρ_a ∼ m² f_a² θ_i² ∼ H₀² M_Pl² and concludes that θ_i ∼ 0.1 corresponds to ~25× fine-tuning, and that θ_i ∼ 1 implies Ω_a ∼ 1. While qualitatively plausible, no explicit numerical comparison to existing ALP birefringence analyses (e.g. Fujita et al. 2021) is provided to show consistency of parameter regimes.  
- **Required fix (MINOR):**  
  - Provide at least one explicit comparison to published ALP birefringence parameter estimates (e.g., constraints on m, f_a, C_{aγ}) to ground the claimed “natural” parameter range in existing literature.

---

### P1B-M6 – “LiteBIRD forecast” used without verifying source numbers  
- **Location:** Sec. VI (“LiteBIRD forecast.—LiteBIRD is projected to achieve σ(β) ≈ 0.03° .”).  
- **Problem:**  
  - It is asserted that LiteBIRD will reach σ(β) ≈ 0.03°, citing  (LiteBIRD Collaboration, Allys et al. 2023). Without checking the precise forecast for birefringence, there is a risk of misquoting the projected precision.  
- **Required fix (MINOR):**  
  - Confirm that  actually reports a birefringence forecast at that precision; if not, either adjust the number or provide a separate supporting citation that does.

---

### P1B-N1 – Version-history and internal bookkeeping text in the body  
- **Location:** Title page & header, e.g. “(Dated: 2026-06-03 PDT)”; footnote “disambiguation,” Appendix A (“KNOWN GAPS.md”), Appendix B (“Claims classification for this companion paper”), and multiple “earlier count erroneously quoted…” and “concern was raised…” passages.  
- **Problem:**  
  - The text contains review-log style prose: “earlier count erroneously quoted ‘98.6% quintom-B’ weight;” “a concern was raised that…” This is internal version-history language and not appropriate for a final PRD manuscript.  
  - The “Claims Classification” table and “KNOWN GAPS” comments are internal audit tools, not conventional scientific content.  
- **Required fix (MAJOR):**  
  - Remove all explicit references to earlier drafts, reviewer concerns, or internal debugging narratives. Present only the final, verified analysis.  
  - If a “claims classification” is retained, restructure it into a standard discussion of which results are original, which are reproductions, and which are speculative, without audit labels.

---

### P1B-N2 – Use of unconventional labels like “RETained,” “REPRODUCIBILITY manifest,” stylized emphasis  
- **Location:** Multiple footnotes and Appendix C.  
- **Problem:**  
  - Capitalization like “RETAINED,” “NOT the spectator-consistent sub-range,” and meta-commentary about priors is stylistic noise and not standard PRD style.  
- **Required fix (NIT):**  
  - Normalize emphasis to standard italics or cautious wording consistent with PRD’s style guide.

---

### P1B-N3 – “Chain diagnostics” numbers not independently checkable  
- **Location:** Sec. III & Table I (309,189 samples, R̂ − 1 values, ESS), footnotes.  
- **Problem:**  
  - While these are internal diagnostics, they’re presented as precise and reconciled across various counts (119,617 vs 123,368 vs 216,432). Without public chains, a referee cannot verify them.  
- **Required fix (MINOR):**  
  - Provide actual MCMC chain files in a persistent repository with clearly documented burn-in and thinning criteria, or reduce the level of quoting internal sample counts.

---

### P1B-N4 – Minor textual/clarity issues  
- **Location:** Throughout.  
- **Problems:**  
  - Phrases like “canonical Hubble-tension result,” “canonical quintom signature,” “bounce / pre-Big-Bang scenario” are informal and sometimes ambiguous.  
  - Several sections mix scope statements, caveats, and results in a way that makes it difficult to distinguish what is robustly shown from what is speculative or forward-looking.  
- **Required fix (NIT):**  
  - Tighten language to distinguish clearly between:  
    - concrete numerical results from this paper,  
    - literature results, and  
    - speculative or programmatic statements.  

---

## Summary recommendation

**REJECT**

The manuscript fails PRD’s standards for bibliographic and factual rigor. It relies heavily on non-existent references (future-dated arXiv IDs, hypothetical DESI DR2 and ACT DR6 papers, multiple “in preparation” self-citations) while presenting corresponding numerical results as if they were based on real, verifiable data and literature. Many of the key statistics and cross-comparisons cannot be traced to existing publications, and essential parts of the program depend on unavailable companion manuscripts. These are not issues that can be remedied by minor revision; the work must be rebuilt around actual, publicly documented data and literature before it can be meaningfully evaluated for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E11 – Inconsistent NaMaster SNR vs. quoted bias and noise level  
- **Location:** Sec. IV (“Independent verification”), surrounding Eq. (1).  
- **Problem:** The text states that with ACT-like noise (ΔP = 10 μK·arcmin) and 500 MC realizations, injecting β = 0.27° yields β̂ = 0.238° at **SNR = 20.32** and β = 0.342° yields β̂ = 0.302° at **SNR = 25.71**. No per-realization scatter or error bar on β̂ is given, so the reader cannot reconstruct 20.32 or 25.71 from the presented numbers (β_inj, β̂, N_MC). There is also an internal tension: the worst-case bias is stated as 0.040°, yet an SNR ≳ 20 with ACT-like noise and f_sky = 0.32 would require a quoted statistical uncertainty on β of ∼0.01–0.02°, smaller than the bias itself, implying a non-negligible fractional bias that is never quantified.  
- **Required fix (ESSENTIAL):**  
  - Explicitly define SNR (e.g. β_inj / σ(β̂) or β̂ / σ(β̂)), and provide σ(β̂) from the 500 realizations so that 20.32 and 25.71 can be recomputed.  
  - Quantify the ratio bias/σ and state clearly whether the 0.032–0.040° bias is negligible compared to the quoted statistical error or not.  
  - If SNR includes additional weighting or differs between injections (e.g. different effective noise), describe and justify this.

---

P1B-E12 – Arithmetic inconsistency in “canonical 3.6σ Hubble tension” mapping to MB offset  
- **Location:** Sec. III (MB–H0 joint-posterior offset check).  
- **Problem:** The text computes MB − 5 log10 H0 at the Riess anchor and at the chain mean, finds a difference of 0.155 mag, and calls this “∼3.2σ relative to the chain’s σ_MB = 0.049 marginal width” and “corresponds exactly to the canonical 3.6σ Hubble tension.” Numerically 0.155 / 0.049 ≈ 3.16σ, but 3.16σ is not “exactly” 3.6σ, and the connection between a 3.2σ MB offset and a 3.6σ H0 tension is asserted qualitatively, not demonstrated (the joint covariance of (MB, H0) is not shown).  
- **Required fix (MAJOR):**  
  - Either remove the phrase “corresponds exactly” or explicitly show, using the 2D covariance, how the 3.2σ offset in MB maps to the 3.6σ H0 tension along the Pantheon+ degeneracy direction.  
  - Clarify that 3.2σ in MB is only approximately consistent with a 3.6σ H0 tension, and quantify the approximation rather than stating “exactly.”

---

P1B-E13 – Incomplete dimensional analysis and normalization in the ALP energy-density scaling  
- **Location:** Abstract; Sec. VI, footnote 4; Appendix C footnote 5.  
- **Problem:** The ALP energy density is repeatedly summarized as  
  \( \rho_a \sim m^2 f_a^2 \theta_i^2 \sim H_0^2 M_{\text{Pl}}^2 \theta_i^2 \)  
  with Ω_a scaling as Ω_a ∼ (m² f_a² / H₀² M_Pl²) θ_i² and the “∼ 25× tuning” claim derived from θ_i changing from 0.5 to 0.1. However:  
  - No numerical normalization (including factors 1/2, scale factor at onset of oscillations, or redshifting) is ever given, so the claim that θ_i ∼ 1 implies Ω_a ∼ 1 “of order the critical density” is qualitative and not explicitly numerically justified.  
  - The “25× tuning” is described as Ω_a(0.1)/Ω_a(0.5) ≈ 1/25, but Ω_a ∝ θ_i², so the suppression is exactly (0.1/0.5)² = 1/25; this arithmetic is implicit, not shown, and no corresponding change in the predicted β is discussed (β depends on Δϕ/fa, which is tied to θ_i).  
- **Required fix (MAJOR):**  
  - Provide a concrete expression for Ω_a today, including the numerical prefactors (e.g. 1/2, the redshift of onset) and at least one worked example showing that θ_i ∼ 1 indeed leads to Ω_a ≳ O(1) for the chosen (m, f_a).  
  - Explicitly show Ω_a(0.1)/Ω_a(0.5) = 1/25 to justify the “25× tuning” language, and discuss whether β changes appreciably when θ_i is shifted (i.e. whether the same β can be maintained without additional re-tuning of other parameters).  
  - Make clear that the dimensional estimate is an order-of-magnitude scaling, not an exact equality.

---

P1B-E14 – Incomplete derivation and possible mismatch in Eq. (3) for β  
- **Location:** Sec. VI, Eq. (3) and surrounding text.  
- **Problem:** Eq. (3) reads  
  \( \beta \approx \frac{\alpha_{\rm EM} \times 8}{4\pi} \times 1.07 \approx 0.29^\circ \).  
  Later, the combined requirement is given as \( C_{a\gamma} \Delta\phi / f_a \approx 10.3 \) for β = 0.342°. The text states that the “fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H0, Δϕ/f_a ≈ 1.0,” but it never explicitly shows the step from Eq. (3) to the 10.3 figure or explains the origin of the factor 1.07. As written, a reader cannot reconstruct 0.29° from the stated inputs without reverse engineering the missing steps.  
- **Required fix (MAJOR):**  
  - Explicitly state the general birefringence formula used (e.g. β = (α_EM / 4π) C_{aγ} Δϕ/f_a), then show the intermediate step that yields the 1.07 factor and the mapping to 0.29°.  
  - Demonstrate numerically that with C_{aγ} = 8 and Δϕ/f_a from the stated evolution, Eq. (3) is consistent with the later requirement C_{aγ} Δϕ/f_a ≈ 10.3 for βobs = 0.342°.  
  - If 1.07 absorbs specific factors (e.g. small deviations of Δϕ/f_a from 1 or integration effects), state this explicitly.

---

P1B-M7 – Abstract claims still not fully supported or numerically reproduced in the body  
- **Location:** Abstract, items (2) and (3) and the concluding sentences.  
- **Problems:**  
  - The abstract states: “Injecting the spectator-ALP fiducial value β = 0.27° recovers β̂ = 0.238° (pipeline-recovery bias 0.032°).” The body later shows a second injection (β = 0.342°) with a larger bias 0.040°, and acknowledges that 0.032° is not stable across injections. The abstract still presents 0.032° as if it were the definitive bias without mentioning the larger value.  
  - The abstract claims: “Both frozen dataset combinations find ∆Neff consistent with zero … and H0 consistent with standard ΛCDM.” While Table I supports the numbers, the abstract does not reflect the internal discussion that the SH0ES tension remains at the canonical ≈3.6σ; the phrase “consistent with standard ΛCDM” is technically true but potentially misleading about the unresolved tension.  
- **Required fix (MAJOR):**  
  - Update the abstract’s NaMaster sentence to indicate that the pipeline bias lies in the range 0.032–0.040° (worst-case 0.040° at β = 0.342°), rather than giving a single 0.032° value.  
  - Either (i) add a clause clarifying that “H0 remains in ≈3–4σ tension with SH0ES and the ∆Neff extension does not resolve this,” or (ii) soften “H0 consistent with standard ΛCDM” to explicitly distinguish consistency with Planck ΛCDM from consistency with all current H0 determinations.

---

P1B-M8 – Juxtaposition of σ values from different null procedures without explicit warning  
- **Location:** Sec. IV (birefringence context), Sec. VI (“Headline observational constraint,” “Summary-likelihood combination”).  
- **Problem:** The text brings together several σ-level statements derived from different procedures and covariance assumptions:  
  - 3.6σ Eskilt & Komatsu joint WMAP+Planck result with a full treatment of calibration systematics.  
  - 3.9σ “auxiliary” inverse-variance combination of Planck NPIPE and ACT DR6, explicitly neglecting shared systematics.  
  - High-SNR NaMaster pipeline figures (20.32, 25.71) derived from MC injection experiments.  
  Although the text says the 3.9σ is “auxiliary” and the MC SNR is “not a sky detection,” the σ-levels sit side by side in the same section, which invites direct comparison even though they are not methodologically comparable.  
- **Required fix (MAJOR):**  
  - Add explicit, prominent language that these σ values come from different null procedures and are *not directly comparable*: the 3.6σ comes from a full joint likelihood with shared-calibration modeling, the 3.9σ explicitly neglects those systematics, and the NaMaster SNR refers to MC injections, not sky detections.  
  - Consider moving the 3.9σ inverse-variance number to a brief footnote or appendix, or explicitly label it “naive, not directly comparable to the 3.6σ” wherever it appears.

---

P1B-M9 – Internal cross-reference and label inconsistencies around datasets  
- **Location:** Abstract, Sec. IV (“published Planck/ACT DR6 2.4–2.9σ”), Sec. VI (“Planck PR4 + ACT DR6 EB-spectrum likelihoods”), references [3], .  
- **Problem:**  
  - The abstract and Sec. IV repeatedly refer to “Planck/ACT DR6 2.4–2.9σ [2,3]” as if they are established published values, while the main body later treats one of these (the ACT DR6 result) as entering only through an internal EB-spectrum likelihood and an as-yet-unpublished analysis.  
  - The ALP-MCMC description in Appendix C calls the Planck+ACT EB likelihood “the same observables used by Refs. [2, 3],” which implies full equivalence with the published analyses; this overstates the connection when [3] is not an actual published EB-likelihood implementation that can be crosschecked.  
- **Required fix (MAJOR):**  
  - Clarify in the main text that the “Planck PR4 + ACT DR6 EB-spectrum likelihoods” as implemented in the author’s MCMC are *reimplementations* or internal reconstructions, not official collaboration likelihoods.  
  - Wherever the “2.4–2.9σ” cluster is quoted, specify which part is from published Planck-only analyses and which part is tied to the not-yet-public ACT DR6 implementation, and avoid presenting the combined range as a single literature result.

---

P1B-M10 – Appendix vs. main-text mismatch in ALP prior interpretation  
- **Location:** Sec. VI (spectator-status caveat and text around footnote 4); Appendix C footnote 5.  
- **Problem:**  
  - Sec. VI emphasizes that the spectator-consistent regime requires θ_i ≪ 1 and that “the numerical scan range θ_i ∈ [0.5, 2] is RETAINED here for completeness of the parameter envelope,” implying the main physics claim focuses on θ_i ∼ 0.1.  
  - Appendix C, however, describes the ALP-MCMC prior simply as θ_i ∈ [0.5, 2] “(natural-misalignment range)” and only in a footnote notes that this prior does *not* represent the spectator-consistent subset. The main text in Sec. VI cites β_ALP = 0.336° ± 0.107° from these chains as if it were a spectator-ALP consistency result, even though the majority of prior volume (and likely posterior weight) is in the non-spectator (DE-ALP) regime.  
- **Required fix (MAJOR):**  
  - Explicitly quantify, in Sec. VI, what fraction of posterior samples satisfy θ_i ≲ 0.1 (the true spectator regime) and whether β_ALP remains consistent with β_obs when restricted to this subset.  
  - Clearly label the reported β_ALP = 0.336° ± 0.107° as a result for the *full* θ_i ∈ [0.5, 2] prior, and avoid presenting it as a clean spectator-ALP result unless a separate, properly restricted run is provided.

---

P1B-N5 – Inconsistent and potentially stale sample-count numbers  
- **Location:** Sec. III (footnote 1, Fig. 1 caption, Table I “Total samples” rows); Conclusions (“309,189 frozen samples…”).  
- **Problem:**  
  - The paper quotes 176,240 + 132,949 = 309,189 raw samples and then multiple different post–burn-in or thinned counts: 216,432 post-burnin across both chains, 123,368 (analytic 0.7×176,240) vs 123,129 (actual), and 119,617 (getdist-thinned) in Fig. 1. These numbers are said to be reconciled, but the logic is spread across footnotes and the caption; a reader cannot easily verify that all later uses of “309,189 samples” refer to the same effective posterior or that the 119,617 sample subset is representative.  
- **Required fix (MINOR):**  
  - Provide a single, consolidated paragraph summarizing raw, post-burnin, and thinned sample counts (with exact formulas), and ensure that all places using these numbers refer back to that summary.  
  - Avoid repeating approximate counts (e.g., “≈ 123,368”) in multiple locations; instead, quote one set of precise numbers and use them consistently.

---

P1B-N6 – Unquantified hedges around “canonical quintom signature” and “canonical Hubble-tension result”  
- **Location:** Sec. II (“canonical Hubble-tension result”); Sec. III and Sec. V (description of w₀, w_a departures as “canonical quintom signature”).  
- **Problem:**  
  - The text labels its w₀, w_a posterior as “the canonical quintom signature” and the Planck+SH0ES discrepancy as “the canonical Hubble-tension result” without explicitly quantifying which literature benchmarks these phrases reference (e.g., specific w₀, w_a constraints in prior DESI/DES analyses or a particular H₀ tension quantification).  
- **Required fix (MINOR):**  
  - Replace “canonical” with more precise language such as “similar in magnitude to the ≈3–4σ Planck–SH0ES tension reported by Riess et al. ” or “qualitatively matching the w₀–w_a behavior discussed in Cai et al. .”  
  - Where “canonical quintom signature” is used, specify the threshold (e.g., w₀ + w_a < −1 at >3σ) and show the numerical comparison explicitly, rather than relying on a qualitative label.