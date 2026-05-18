# P4_v1_0_108_R_INTERNAL R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1645pt
**Wall time**: 62.9s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=79374, completion=3761, reasoning=2906, total=83135

---

**PAPER-GRO-B1: Abstract + §IV.D (multi-null battery)**

The 3-interpretation closure logic does not rigorously rule out interpretation (i) a real cosmological dipole. The bootstrap null collapses to -0.22σ and the quartile washout is reported, but the paper provides no injection test demonstrating that a coherent low-ℓ dipole at the ~1.7% effective amplitude recovered under the binomial null would survive or be rejected by the bootstrap resampling; ℓ=2 > ℓ=1 is suggestive but not decisive without that control.

**Fix:** Add a short injection-recovery subsection (or table row) running the exact 4-null battery on synthetic dipole maps at A ≈ 1.7% and report the recovered σ values under bootstrap vs. binomial.

**PAPER-GRO-B2: Abstract + Conclusions framing**

The headline framing “canonical-mask result null under bootstrap null, NOT a detection” is defensible on the subsample mask but is undercut by the abstract’s continued prominent display of the binomial +3.64σ and apodized +3.57σ numbers before the bootstrap result. This structure risks external readers quoting the higher numbers as a marginal detection.

**Fix:** Lead the abstract and the §IV.D verdict paragraph with the bootstrap -0.22σ and sky-rotation +2.56σ results; move the binomial/apodized numbers to a supporting table with explicit “not load-bearing” footnote.

**PAPER-GRO-B3: §IX.J (sensitivity floor)**

The empirical 50%-recovery threshold is reported as |A| ≈ 0.75% on the HC subsample (N = 471k) while the ideal-statistical Fisher floor on the full 3.2M catalog is quoted as ~0.29%. The text correctly flags this as a cross-sample comparison and defers the full-catalog injection sweep, but the abstract still presents 0.75% as the operational sensitivity without sufficient qualification that it applies only to the smaller subsample.

**Fix:** In the abstract and sensitivity paragraph, state explicitly “0.75% (HC subsample, N = 471k); full-catalog systematic-inclusive bound deferred” and remove any implication that 0.75% is the catalog-wide limit.

**PAPER-GRO-B4: Title + abstract opening**

The title and abstract opening sentence frame the work as demonstrating a “quantifiable monopole-mask leakage channel” that “can mimic” prior claims. This is accurate for the present pipeline but overstates generality; no matched-footprint Ganalyzer reanalysis is performed, so the paper cannot claim to explain the amplitude of Shamir’s specific detections.

**Fix:** Change title to “Monopole-Mask Leakage Produces Spurious Raw Pseudo-C_ℓ Chirality Dipoles in This DESI Legacy / ViT Pipeline” and qualify the abstract claim as “under the present classifier and footprint.”

**PAPER-GRO-B5: §IV.D + Table III (low-ℓ bandpowers)**

The joint χ²/dof = 4.24 on the low-ℓ bandpowers is attributed to mask-coupled monopole leakage, yet the table still reports individual +2–6σ excursions without a clear statement that these are not interpreted as parity signals. The single-mode ℓ=1 post-MASTER result is the only load-bearing statistic; the bandpower table functions as a diagnostic but is presented at equal visual weight.

**Fix:** Add a one-sentence footnote to Table III: “Bandpower excursions are mask-leakage diagnostics only; the isotropy-breaking observable is the single-mode ℓ=1 post-MASTER value (-0.12σ on subsample mask).”

**PAPER-GRO-B6: Overall narrative density**

The manuscript contains an unusually high density of internal artifact citations, footnotes, and cross-references to JSON files and prior versions. While excellent for reproducibility, this makes the text difficult for an external reviewer to follow without constant repo access and creates the appearance of defensive over-documentation.

**Fix:** Move the majority of artifact paths and version-history notes to a single “Reproducibility” appendix or table; keep only the most load-bearing JSON references in the main text.
