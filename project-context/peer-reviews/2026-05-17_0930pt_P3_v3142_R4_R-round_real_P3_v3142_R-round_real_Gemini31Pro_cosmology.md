# P3_v3142 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0930pt_P3_v3142_R4_R-round_real
**Wall time**: 56.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=59356, completion=4990, reasoning=3826, total=64346

---

## PAPER-GEM-B1: BLOCKER - Impossible Deduplication Arithmetic
**Section:** 4.3 (Cross-Survey Matches) & 6.4 (Path-C Rebuild Residual Caveats)
**Issue:** The paper claims 388,493 input detections and exactly 637 pairwise cross-survey matches (no triples), yielding a headline catalog of 378,280 unique objects. This arithmetic is impossible: 637 pairs collapse 1,274 detections into 637 objects, reducing the total by exactly 637. $388,493 - 637 = 387,856$, leaving 9,576 objects unaccounted for. You cannot defer the fundamental arithmetic of the headline catalog size in a data release paper.
**Fix:** Recompute the union-find manifest to find the missing 9,576 objects (likely intra-survey duplicates) and explicitly document them, or correct the headline 378,280 figure to match the actual graph collapse.

## PAPER-GEM-M1: MAJOR - Ignored R3 Instruction on "Strict Subset" Claim
**Section:** 3.4 (eROSITA DR1)
**Issue:** The abstract acknowledges the R3 finding to "soften to 'high overlap' or add Table 2 intersection verification" regarding the BigAE vs IsolationForest sets. However, Section 3.4 still explicitly asserts: "The 298-source canonical-S catalog is a strict subset of the 9,303-source IsolationForest top-1% reference." There is no mathematical guarantee that L2-reconstruction outliers are a strict subset of latent-space tree-path outliers.
**Fix:** Change "is a strict subset of" to "has high overlap with" in Section 3.4, or provide the exact empirical intersection count to prove the strict subset claim.

## PAPER-GEM-M2: MAJOR - GR Projection Effects Omitted from Fisher Systematics
**Section:** 5 (Cosmological Applications)
**Issue:** The multi-tracer $f_{\rm NL}$ forecast marginalizes over magnification bias ($\delta s$) and linear bias ($\delta b$), but ignores GR projection effects (Doppler, Sachs-Wolfe, Shapiro delay). These effects introduce deterministic theoretical contamination at $\mathcal{O}(\mathcal{H}^2/k^2)$ that perfectly mimics the scale-dependent bias of local primordial non-Gaussianity. Claiming a "zero-systematics upper bound" without acknowledging this theoretical degeneracy invalidates the cosmological forecast.
**Fix:** Explicitly add GR projection effects to the list of unmarginalized systematics in Section 5 and acknowledge they mimic the $f_{\rm NL}$ signal at large scales.

## PAPER-GEM-M3: MAJOR - Missing R3 Deferrals in Section 6.4 Tracking
**Section:** 6.4 (Path-C Rebuild Residual Caveats)
**Issue:** The abstract explicitly lists two new R3 deferrals: "GR projection effects on multi-tracer $f_{\rm NL}$" and "'strict subset' BigAE vs IsolationForest verification". However, the actual tracking list in Section 6.4 ("Real cross-vendor R-round deferrals") only enumerates items (a)-(d) from v3.1.40, completely dropping the two new R3 items.
**Fix:** Add items (e) and (f) to the Section 6.4 deferral list to maintain accurate cross-round tracking and match the abstract's claims.

## PAPER-GEM-m1: minor - Fisher Arithmetic Verification (PASS)
**Section:** 5 (Cosmological Applications)
**Issue:** R4 Adversarial Focus item (a) requested verification of the Fisher error propagation rewrite. The R3 hallucination has been successfully replaced with clean linear propagation: $\sigma_{\sigfnl} = |-3.66| \cdot 0.65 = 2.379$. The derivation is now mathematically unambiguous and correct.
**Fix:** None required. Logged as verified per prompt instructions.

## PAPER-GEM-m2: minor - Sloppy Arithmetic in 95% Confidence Interval
**Section:** 5 (Cosmological Applications)
**Issue:** The text states the 95% CI for $\alpha$ is $[-1.08, +1.46]$. Using the stated linear mapping $\sigfnl(\alpha) = 8.98 - 3.66\alpha$, the exact bounds are $8.98 - 3.66(1.46) = 3.636$ and $8.98 - 3.66(-1.08) = 12.932$. The text quotes $[3.66, 12.94]$ and justifies it as $8.27 \mp 1.96 \cdot 2.37$, but $1.96 \cdot 2.379 = 4.66$, which yields $[3.61, 12.93]$. The $3.66$ lower bound is an arithmetic error.
**Fix:** Correct the 95% $\sigfnl$ interval to $[3.64, 12.93]$ to exactly match the linear mapping of the $\alpha$ boundaries.
