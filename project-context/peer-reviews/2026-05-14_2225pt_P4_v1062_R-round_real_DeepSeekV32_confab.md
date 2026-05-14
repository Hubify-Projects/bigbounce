# P4_v1062 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_2225pt
**Wall time**: 163.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=56351, completion=1917, total=58268

---

## Adversarial Peer Review Findings (v1.0.62)

### PAPER-DEE-B1: BLOCKER — Canonical-N MASTER ℓ=1 direct-MC provenance incomplete
**Lines:** §Conclusions paragraph 'Canonical-N MASTER ℓ=1 direct compute (v1.0.62 — GPT-B2 closed)'  
**Issue:** The direct-MC result σ_canonical_direct = +1.85σ is cited as the closure of GPT-B2, but the provenance chain is broken. The JSON artifact `canonical_n_master_l1_direct.json` is referenced, but the 500-per-realization null distribution `null_distribution.npy` is stated to be "archived on the compute pod" and will be "mirrored to the provenance directory in a follow-up tick." This is unacceptable for a load-bearing number that supersedes an analytic projection. The +1.85σ is used to argue the earlier +0.26σ projection underestimated leakage by ~7×, but the null distribution underpinning this claim is not provided.  
**Fix:** The `null_distribution.npy` file must be deposited in the public repository (e.g., `outputs/canonical_provenance/`) prior to submission, with its SHA256 hash recorded in the manifest. The paper must not claim closure of GPT-B2 until the full numerical artifact is available for independent verification.

### PAPER-DEE-M1: MAJOR — Ambiguous "sensitivity floor" between statistical and empirical
**Lines:** Abstract (L155-174), §Sensitivity (L1553-1574, L1595-1610)  
**Issue:** The abstract states: "the conservative, systematic-inclusive empirical injection-recovery sensitivity floor is |A_dipole| > 0.5% (at A = 0.5% the per-pixel-shuffle MC gives P(σ > 2) = 0.18; explicit 50%-recovery at 3σ is not demonstrated within the tested A ∈ [0.05, 0.50]% grid...)". This is contradictory: a "sensitivity floor" is normally the amplitude at which 50% of injections are recovered at a given significance (e.g., 3σ). Here, at A = 0.5%, P(σ > 2) = 0.18, not > 0.5. The text admits the 50%-recovery threshold is "bounded only above by the highest tested amplitude." Therefore, the empirical floor is > 0.5%, not = 0.5%. The abstract's "> 0.5%" is technically correct but easily misread as "= 0.5%". The subsequent "Fisher-floor statistical Poisson asymptote is |A_dipole| ≲ 0.29% at 3σ" adds confusion because it uses the full-amplitude A, while the preceding derivation uses half-modulation A/2.  
**Fix:** Clarify in the abstract: "The empirical injection-recovery test shows P(σ > 2) = 0.18 at A = 0.5%, so the 50%-recovery threshold lies above 0.5%. We conservatively quote |A_dipole| > 0.5% as the systematic-inclusive detection threshold." Unify the amplitude convention: explicitly state that the 0.29% Fisher floor refers to full amplitude A, and the 0.5% empirical bound is also on A.

### PAPER-DEE-M2: MAJOR — Hemisphere LEE interpretation is contradictory
**Lines:** Abstract (L130-140), §Hemisphere Asymmetry (L1248-1265), §Hemisphere Discussion (L1493-1508)  
**Issue:** The abstract states the hemisphere max-statistic rejects the random-label null at p_LEE ≤ 10⁻⁴ (zero of 10,000 nulls reach the data), corresponding to post-LEE significance ≳ 3.7σ, but then says "per-pixel-shuffle nulls do NOT preserve depth, mask-edge, or other systematic spatial structures, so this rejection... is not equivalent to a primordial-dipole detection." In the discussion, it's attributed to "the same sub-percent depth-coupled / GZ1-training-label systematic." However, the per-pixel-shuffle null by construction destroys any spatial correlation of labels with depth/mask-edge systematics. If the rejection persists under this null, it suggests a spatially correlated signal beyond what the depth/mask systematic can produce. The argument that the rejection is due to systematics is circular: the null explicitly randomizes labels, so any depth/mask correlation is broken. The text needs a clear, testable hypothesis for how a depth-coupled systematic survives per-pixel shuffling.  
**Fix:** Either provide a demonstration that the per-pixel-shuffle null does not adequately destroy the depth-label correlation (e.g., because the systematic is uniform across the footprint and thus survives shuffling), or revise the interpretation to acknowledge that the rejection may indicate a low-level spatially correlated signal, albeit one that is not corroborated by the full-sky dipole estimators. The current explanation is logically inconsistent.

### PAPER-DEE-M3: MAJOR — Missing provenance for key numbers in abstract and conclusions
**Lines:** Abstract (L130-140: hemisphere p_LEE ≤ 10⁻⁴, post-LEE ≳ 3.7σ), Conclusions (L1798-1808: +1.85σ direct-MC)  
**Issue:** The abstract's hemisphere p_LEE ≤ 10⁻⁴ and post-LEE ≳ 3.7σ are load-bearing statistics, but their provenance is only partially given in the manifest (`mc_seed_manifest.json`). The exact script that generated the 10,000 MC realizations, the batch size, and the method for computing p_LEE and post-LEE σ must be explicitly documented in the provenance JSON. Similarly, the +1.85σ direct-MC result requires the exact NaMaster command, the mask file, and the random seed for the 500 permutations. The referenced `canonical_n_master_l1_direct.json` must contain all these inputs.  
**Fix:** Expand `mc_seed_manifest.json` to include the exact hemisphere LEE calculation (how p_LEE is derived from the 10,000 nulls, how post-LEE σ is computed). Ensure `canonical_n_master_l1_direct.json` includes the NaMaster command, mask FITS file hash, and the random seed for reproducibility.

### PAPER-DEE-m4: minor — Inconsistent notation for σ in abstract
**Lines:** Abstract (L130-140: "σ_canonical_direct = +1.85σ")  
**Issue:** The notation "σ_canonical_direct = +1.85σ" mixes a variable name with a unit. It should be either "σ = +1.85" or "significance = +1.85σ". The same pattern appears elsewhere (e.g., "−0.122σunit").  
**Fix:** Consistently use "σ" as the unit (e.g., "+1.85σ") or define a variable like "z_score" and report "+1.85". Unify throughout abstract and conclusions.

### PAPER-DEE-m5: minor — "Surviving real-cross-vendor deferrals" update is incomplete
**Lines:** §Surviving real-cross-vendor deferrals (L1760-1797)  
**Issue:** The update states GPT-B2 is "closed at v1.0.62" with the direct-MC artifact, but the description of the three deferrals (i, ii, iii) still lists item (ii) as "The canonical-N MASTER recompute at ℓ=1... is now closed at v1.0.62 by the direct single-mode NaMaster MC." This is redundant with the opening statement. The update should clearly state which deferrals are closed and which remain open. Item (iii) (Shamir 2022 arXiv ID) is noted as pending verification but not marked closed.  
**Fix:** Restructure the paragraph to list: (i) amplitude convention – closed; (ii) canonical-N MASTER ℓ=1 – closed with direct-MC; (iii) Shamir 2022 arXiv ID – open (journal reference retained). Remove the repetitive sentence about closure.

### PAPER-DEE-n6: nit — Typo in "σ_canonical_direct"
**Lines:** §Conclusions (L1798: "σ_canonical_direct = +1.85σ")  
**Issue:** The variable name "σ_canonical_direct" uses a Greek letter in code font, which may render poorly. Use "sigma_canonical_direct" or "z_canonical_direct".  
**Fix:** Use Latin "sigma_canonical_direct" or "z_canonical_direct" for better compatibility.
