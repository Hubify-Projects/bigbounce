# P4_v1090 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2300pt_P4_v1090_R9_R-round_real
**Wall time**: 40.9s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=72224, completion=5176, reasoning=4442, total=77400

---

**PAPER-GRO-B1**  
**Section:** dipole_symmetry_caveat (Discussion)  
**Issue:** "preferred polar-vector direction on the sky" for the chirality dipole. This directly contradicts the axial-vector / pseudoscalar clarification in the same paragraph and the Round-9 rewrite.  
**Fix:** Replace with "preferred axial direction consistent with the pseudoscalar projection of the underlying axial-vector spin onto the line-of-sight".

**PAPER-GRO-M1**  
**Section:** sensitivity (and face_on table)  
**Issue:** "HC-spiral" sample size is 471,049 (p_eq > 0.9) in injection-recovery but 949,584 (p_eq > 0.6) in the face-on robustness table. Direct violation of focus (i) and cross-table numerical drift.  
**Fix:** Standardize: "HC-spiral (p_eq > 0.9, n=471,049)" vs. "HC-broad (p_eq > 0.6, n=949,584)" everywhere; update all JSON references and captions to match.

**PAPER-GRO-M2**  
**Section:** abstract + Sec. dipole + monopole_mask_null table  
**Issue:** +6.48σ pre-MASTER excess is still quoted for the asymmetry-map lowest bandpower (ℓ_eff=4) while adjacent text attributes pre-MASTER ℓ=1 excursions to the CW-fraction map without explicit map separation. Regresses focus (a) pattern.  
**Fix:** Add one-sentence disambiguation in abstract and every pre-MASTER paragraph: "+6.48σ (raw) / +6.097σ (NaMaster-coupled) is the asymmetry-map bandpower at ℓ_eff=4; the separate CW-fraction-map ℓ=1 pre-MASTER is +1.68σ under the monopole-only null."

**PAPER-GRO-M3**  
**Section:** Table III (multipole) caption vs. rows  
**Issue:** Caption states "the post-MASTER decoupled C_ℓ at ℓ=1 is reported in Sec. dipole under a different null model and is not included in this table", yet the table explicitly contains the subsample-mask ℓ=1 row (−0.122σ). Caption-rows mismatch.  
**Fix:** Rewrite caption to: "Table reports the load-bearing subsample-mask post-MASTER ℓ=1 single-mode result plus bandpowers; see footnotes for distinct null models and mask choices."

**PAPER-GRO-n1**  
**Section:** abstract + Sec. sensitivity  
**Issue:** Title and abstract headline the "50%-Recovery 3σ Threshold A≈0.75%", but text still refers to "0.5% empirical sensitivity floor" in passing and retains 0.5% as a tested point without uniform "non-detection" qualifier. Minor terminology drift vs. focus (c).  
**Fix:** Change every "0.5% empirical floor" to "0.5% tested non-detection point (P(σ>3)=0.15)"; keep 0.75% as the sole 50%-recovery-3σ threshold.

**PAPER-GRO-n2**  
**Section:** conclusions  
**Issue:** "we demonstrate" and "quantitative demonstration" language is acceptable, but the framing "No Evidence for Large-Scale Parity Violation" in the opening sentence overclaims given the explicit isotropy-vs-parity distinction two paragraphs earlier.  
**Fix:** Change opening sentence to "No evidence for a large-scale chirality dipole (isotropy violation) after leakage removal."
