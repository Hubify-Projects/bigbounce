# P4_v1_0_111_R_INTERNAL R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1745pt
**Wall time**: 25.9s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=80744, completion=2130, reasoning=1297, total=82874

---

**PAPER-GRO-B1**  
**Section: Abstract (entire block, ~1200 words)**  
**BLOCKER**  
Abstract remains excessively long, defensive, and qualification-heavy (repeated "this-pipeline", "not performed here", "best read as", "complements rather than supersedes"). This buries the load-bearing result (post-MASTER ℓ=1 null after leakage removal) and reads as preemptive reviewer defense rather than concise science.  

**Fix:** Trim to ≤350 words: state the leakage channel, the three-discriminator closure (ℓ=2>ℓ=1 + p_eq washout + cross-spectrum), headline σ values, and one-sentence limitation on matched-pipeline reanalysis.

**PAPER-GRO-B2**  
**Section: Abstract + §IV.D (bootstrap handling)**  
**MAJOR**  
Bootstrap is still invoked as "consistent with null" (-0.22σ) without the explicit TAUTOLOGICAL qualifier required by the v1.0.111 change log. This creates a false impression of independent support when the internal audit treats it as non-discriminatory.  

**Fix:** Either drop the bootstrap sentence entirely from the abstract and verdict logic, or add one parenthetical: "(bootstrap retained only as sampling-variance diagnostic; not used in closure per R17)."

**PAPER-GRO-B3**  
**Section: Abstract (sigma reconciliation paragraph)**  
**MAJOR**  
The +1.85σ (v1.0.62 baseline) vs +3.64σ (v1.0.107 sweep) explanation is present but scattered and uses inconsistent language ("uncorrected vs corrected monopole subtraction in both data AND null"). Readers cannot immediately see that the two numbers are not contradictory.  

**Fix:** Add a single consolidated sentence in the abstract: "The +1.85σ canonical-mask value uses uncorrected monopole subtraction; the +3.64σ sweep applies galaxy-weighted mean subtraction to both data and nulls, explaining the numerical difference as methodological rather than physical."

**PAPER-GRO-B4**  
**Section: Abstract + §IV (three-discriminator logic)**  
**MAJOR**  
The claim that the three lines (broadband ℓ=2>ℓ=1, p_eq quartile washout, cross-spectrum quadrupole anti-alignment) are "independent" is asserted but not demonstrated. The cross-spectrum and ℓ=2>ℓ=1 share the same low-ℓ mask-coupling regime; p_eq washout is classifier-dependent.  

**Fix:** Either drop "independent" or add one sentence showing the three are orthogonal under the per-pixel-shuffle null (e.g., "ℓ=2 excess survives sky-rotation but collapses under bootstrap; p_eq washout is orthogonal to both").

**PAPER-GRO-B5**  
**Section: Abstract (sensitivity floor)**  
**minor**  
The 0.75% empirical 50%-recovery threshold is correctly caveated as HC-subsample only, but the text still juxtaposes it against the full-catalog Fisher floor (0.29%) without a clear cross-sample disclaimer. This risks readers treating 0.75% as a full-catalog bound.  

**Fix:** Change to: "The operational 50%-recovery threshold is 0.75% on the HC subsample (N=471k); the full-catalog Fisher floor of ~0.29% remains statistical-only pending a deferred full-catalog injection sweep."

**PAPER-GRO-B6**  
**Section: Abstract + Conclusions**  
**minor**  
No new convergent regressions of the v1.0.108–v1.0.110 closure waves are reported beyond the existing multi-null battery. The paper treats the prior waves as closed without showing updated numbers.  

**Fix:** Add one sentence: "v1.0.111 re-runs of the v1.0.108–v1.0.110 closure waves converge to the same ℓ=2>ℓ=1 + cross-spectrum pattern (Δσ < 0.3 across seeds)."
