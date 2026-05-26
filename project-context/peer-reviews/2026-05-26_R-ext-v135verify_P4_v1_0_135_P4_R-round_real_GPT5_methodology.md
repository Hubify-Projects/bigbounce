# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v135verify_P4_v1_0_135
**Wall time**: 92.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=103280, completion=4719, reasoning=3624, total=107999

---

## PAPER-GPT-B1 — BLOCKER

**Location:** `\artifact{}` macro; Abstract; Data Availability; v1.0.135 full-catalog injection paragraph.  
**Issue:** All artifact URLs are hardcoded to `paper4-v1.0.134`, while the new v1.0.135 full-catalog injection-recovery artifacts are claimed as added in v1.0.135. External readers cannot verify the additive sweep from the cited immutable tag.  
**Fix:** Publish/tag `paper4-v1.0.135` containing the new JSON/script and update `\artifact{}` + Data Availability, or remove the v1.0.135 injection-recovery claims until the artifacts are externally pinned.

## PAPER-GPT-B2 — BLOCKER

**Location:** Conclusions, “Canonical-$N$ MASTER $\ell=1$ direct compute”; NaMaster appendix.  
**Issue:** The quoted direct-MC numbers are arithmetically inconsistent: `C1=2.298e-5`, null mean `8.004e-6`, null std `8.097e-6` give `(2.298e-5-8.004e-6)/8.097e-6 = 1.85σ`, not `+3.64σ`. Elsewhere `+3.64σ` uses different corrected numbers (`1.51e-5`, `3.12e-6`, `3.31e-6`).  
**Fix:** Replace the stale triplet everywhere with the corrected triplet, or report the stale calculation as `+1.85σ`; make Tables I/III/VI/VIII and captions use one canonical data vector.

## PAPER-GPT-B3 — MAJOR

**Location:** §Monopole+Mask Leakage, v1.0.135 “Full-catalog injection-recovery sensitivity”; §Sensitivity.  
**Issue:** The new full-catalog injection claim is not internally credible: it says “canonical NSIDE=64 mask” but then claims `f_sky=0.74`, conflicting with the canonical `f_sky≈0.49005` and subsample `f_sky=0.659`; `A=0.5%` giving median `+12.62σ` is also inconsistent with the paper’s own Fisher scaling and HC sweep. Injecting `A_p_obs + A_inj d·n` into the observed systematic residual and calibrating against a binomial null does not establish a clean `≤0.50%` detection threshold.  
**Fix:** Re-run/report a like-for-like injection sweep with explicit mask, monopole treatment, noise realization, null class, and baseline subtraction; compare the recovered sigma scaling against the Fisher expectation before claiming `≤0.50%`.

## PAPER-GPT-B4 — MAJOR

**Location:** Table `tab:headline_summary` footnote c; §TTA; version note claiming hard-label variance derivation.  
**Issue:** The 21.4% argmax-flip propagation is numerically wrong. For `p_flip=0.214`, `1+4p(1-p)=1.673`, so the 1σ inflation is `sqrt(1.673)=1.29`, not `1.21`; the text also says “doubling” the Poisson sigma, contradicting both.  
**Fix:** Recompute the hard-label diagnostic error inflation and update all HC/injection/face-on diagnostic uncertainty statements using either variance factor `1.67` or sigma factor `1.29`.

## PAPER-GPT-B5 — MAJOR

**Location:** §Sensitivity; Conclusions item 1; falsification criterion.  
**Issue:** The amplitude convention remains inconsistent: `0.2%` is alternately a half-modulation floor, a statistical upper bound, and a rounded sensitivity; full-amplitude Fisher is quoted as `0.29%`, conservative full-amplitude as `0.4%`, empirical as `0.75%`, and LSST projections appear as both `0.08%` and `0.04%`. This makes the systematic budget and falsification threshold ambiguous.  
**Fix:** Use one convention throughout, e.g. `p_CW=1/2(1+A cosθ)` with all thresholds in full `A`; table the ideal Fisher, fsky/N_eff-inflated Fisher, HC empirical, and full-catalog empirical values separately.

## PAPER-GPT-B6 — MAJOR

**Location:** Abstract; §Dipole Analysis; §Dipole symmetry caveat; Conclusions.  
**Issue:** The systematics-vs-primordial interpretation is overclaimed relative to the statistics. The canonical residual has empirical-rank `p=0.030`, the cross-spectrum anchor is only ~`2.3σ` after trials, density-stratified null does not absorb the residual, and no joint nuisance-marginalized template fit is performed; “favored verdict” / “directly confirmed” language exceeds the evidence.  
**Fix:** Reframe the canonical-mask residual as unresolved but systematics-suggestive, and reserve exclusion/favoring claims for a joint fit marginalizing over depth, PSF, morphology, leg, and a primordial dipole component.
