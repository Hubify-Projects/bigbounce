# P4_v1099 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0300pt_P4_v1099_R17_R-round_real
**Wall time**: 26.3s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=74859, completion=2014, reasoning=1187, total=76873

---

**PAPER-GRO-B1 (BLOCKER)**  
**Section:** Abstract + §I + §IX (multiple sites)  
**Issue:** The paper repeatedly frames its result as identifying a leakage channel that "can mimic" and "explains" Shamir's ~2–4% claims at the percent level, yet explicitly states no matched-footprint reanalysis under Shamir's Ganalyzer + exact cuts was performed. The amplitude inconsistency claim (factor ~6–12) is therefore not a formal exclusion and rests on pipeline differences the authors themselves flag as disqualifying.  
**Fix:** Remove all language implying the leakage accounts for prior detections; state only that the present pipeline yields a null at |A| ≳ 0.75% and that a like-for-like Shamir reanalysis is required for any exclusion claim.

**PAPER-GRO-B2 (MAJOR)**  
**Section:** §IX.J + abstract + §I  
**Issue:** The headline sensitivity is quoted as the empirical 50%-recovery 3σ threshold |A| ≈ 0.75% on the HC subsample (N=471k), while the Fisher floor on the full 3.2M catalog is ~0.29%. No injection sweep was run on the full catalog, so the quoted 0.75% is not demonstrated as the operational full-sample bound and the ~2.6× "gap factor" language is misleading.  
**Fix:** State the 0.75% threshold applies only to the HC subsample; report the full-catalog Fisher value as an ideal-statistical asymptote only and defer the systematic-inclusive full-catalog bound.

**PAPER-GRO-B3 (MAJOR)**  
**Section:** Abstract + §IX (conclusions) + §VI.C  
**Issue:** The +1.85σ canonical-mask ℓ=1 residual is labeled an "unresolved sub-detection-threshold systematic" yet is still presented as part of the load-bearing story alongside the –0.12σ subsample-mask headline. This creates the impression of a clean null while retaining a non-null estimator on the exact mask used for the leakage diagnostic.  
**Fix:** Move the canonical-mask +1.85σ result to a dedicated systematics appendix and state explicitly that the headline null is carried solely by the two estimators that bypass the canonical-mask leakage channel.

**PAPER-GRO-B4 (MAJOR)**  
**Section:** Title + abstract + §I  
**Issue:** The title and abstract lead with a "quantifiable monopole-mask leakage channel can mimic large raw pseudo-C_ℓ chirality dipoles," yet the central scientific claim is a null result after correction. The framing implies the work primarily resolves prior positive claims, when the actual load-bearing result is simply another (larger) null with an identified systematic mode.  
**Fix:** Shorten title to emphasize the null dipole measurement at sub-percent sensitivity; move the leakage demonstration to a methods/results subsection.

**PAPER-GRO-B5 (minor)**  
**Section:** Multiple (e.g., §I, §IX, Table III)  
**Issue:** Residual "parity-violating" phrasing persists in places even after the v1.0.99 sweep (e.g., "primordial parity-violating signal" in signal-hunt and hemisphere sections). The paper correctly notes the ℓ=1 dipole is parity-even, but the language is not uniformly updated.  
**Fix:** Global search-replace of remaining "parity-violating" instances with "isotropy-breaking axial-vector" or "chirality dipole" as appropriate.

**PAPER-GRO-B6 (minor)**  
**Section:** §IX (sensitivity) + Table I  
**Issue:** The 2.5× gap-factor language comparing HC empirical threshold to full-catalog Fisher floor is retained even though the authors note it is not a meaningful empirical-vs-Fisher comparison.  
**Fix:** Delete the 2.5× sentence; report only the HC like-for-like ratio (~1.0) and the deferred full-catalog injection result.
