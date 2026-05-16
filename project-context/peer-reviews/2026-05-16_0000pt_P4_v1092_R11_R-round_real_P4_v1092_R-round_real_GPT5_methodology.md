# P4_v1092 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0000pt_P4_v1092_R11_R-round_real
**Wall time**: 108.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=81249, completion=7324, reasoning=5359, total=88573

---

## PAPER-GPTM-B1 — BLOCKER — 0.75% “systematic-inclusive” threshold is just the Fisher floor for the 471k HC subsample

| Field | Audit |
|---|---|
| Location | Abstract; §Sensitivity, Table “Per-pixel-shuffle null MC injection-recovery”; Conclusions item 1 |
| Paper says verbatim | “The load-bearing systematic-inclusive sensitivity is the empirical 50% recovery-at-3σ threshold of \|A_dipole\|≈0.75%…” |
| Paper says verbatim | “HC-spiral subsample, n=471,049” |
| On-disk artifact says verbatim | Not accessible in supplied packet; cited artifact is `.../injection_recovery_extended.json`. |
| Verdict | NOVEL BLOCKER |

Concrete issue: The 0.75% injection threshold is measured on only 471,049 high-confidence spirals, not the 3,201,160-object headline sample. The ideal full-amplitude 3σ Fisher floor for N=471,049 is \(3\sqrt{3/N}=0.757\%\), so the “empirical 0.75%” result is consistent with pure counting statistics, not a demonstrated systematic-inclusive degradation from the full-catalog 0.29% floor.

Fix: Either rerun injection recovery on the full 3.2M Catalog C sample, or relabel 0.75% everywhere as the HC-spiral-subsample threshold and compare it to the HC Fisher floor, not the full-catalog Fisher floor.

---

## PAPER-GPTM-B2 — BLOCKER — MASTER “collapse to −0.12σ” is not a like-for-like deconvolution

| Field | Audit |
|---|---|
| Location | Abstract; §Dipole Analysis; Conclusions “Headline finding” |
| Paper says verbatim | “collapsing to −0.12σ once the MASTER mode-coupling matrix is applied on the same data” |
| Paper says verbatim | “The pre-MASTER value and the post-MASTER headline differ in mask, in input-map definition, in monopole-subtraction treatment, AND in MASTER mode-coupling inversion…” |
| On-disk artifact says verbatim | Not accessible; paper-reported values cite `master_power_spectrum.json` for −0.12σ and `canonical_n_master_l1_direct.json` for +1.85σ. |
| Verdict | REGRESSION BLOCKER |

Concrete issue: The paper still claims a causal MASTER-only removal to −0.12σ, but the −0.12σ result changes map definition, monopole subtraction, and mask; the like-for-like canonical post-MASTER result is +1.85σ, not −0.12σ. This invalidates the headline “MASTER removes the leakage on the same data” phrasing.

Fix: Present paired pre/post-MASTER results on identical map/mask/null. State that the canonical mask gives +1.85σ post-MASTER, while −0.12σ is a separate larger-mask, monopole-subtracted estimator.

---

## PAPER-GPTM-B3 — MAJOR — TTA still overclaims bias cancellation “by construction”

| Field | Audit |
|---|---|
| Location | §Systematic dipole; Fig. raw-vs-eq caption; Future directions |
| Paper says verbatim | “Equivariant averaging eliminates the real-space systematic by construction… any residual bias cancels to machine precision.” |
| Paper says verbatim | “Equivariant averaging … eliminates this systematic entirely” |
| Paper says verbatim | “Catalog C classifications, which eliminate handedness-dependent systematic biases by construction” |
| On-disk artifact says verbatim | Not accessible; paper-reported D4 holdout says argmax CW fraction shifts 0.5156→0.5021 and 21.4% of galaxies change argmax. |
| Verdict | REGRESSION MAJOR |

Concrete issue: Eq. (TTA) guarantees flip-equivariance of the output protocol, not \(p_{\rm CW}=p_{\rm CCW}\), not hard-label balance, and not cancellation of training/rotation/depth biases. The claimed “machine precision” cancellation is directly contradicted by the 9.5σ monopole, 1.35% D4 argmax shift, and 21.4% argmax instability.

Fix: Replace all “eliminates/cancels by construction/machine precision” language with “suppresses the horizontal-flip component at probability level; residual hard-label, rotational, and training-label biases remain and are propagated as systematics.”

---

## PAPER-GPTM-B4 — MAJOR — Hemisphere LEE framing is statistically incoherent

| Field | Audit |
|---|---|
| Location | Abstract; §Hemisphere Asymmetry; Fig. hemisphere caption; §Hemisphere discussion |
| Paper says verbatim | “direct-MC look-elsewhere statistic on the random-label null” gives \(p_{\rm LEE}\le10^{-4}\). |
| Paper says verbatim | “Bonferroni / BH … reduces the local effective significance … to <1σ (consistent with null).” |
| Paper says verbatim | “We treat the multiplicity-corrected <1σ as the conservative null-consistency statement, while noting that the random-label null IS rejected…” |
| On-disk artifact says verbatim | Not accessible; cited artifact `wave12_hemi_2026-05-01/results.json`. |
| Verdict | STILL-UNRESOLVED MAJOR |

Concrete issue: A direct max-statistic MC with zero exceedances in 10,000 trials is not “tightening” a Bonferroni null result; it contradicts it because the statistic/null/axis grid/amplitude convention changed. The abstract calls direct MC primary but then foregrounds a Bonferroni “consistent with null” interpretation, leaving no well-defined hemisphere headline.

Fix: Choose one primary hemisphere statistic and one null. If direct MC is primary, state: “random-label null rejected at \(p_{\rm LEE}<10^{-4}\), interpreted as systematic because primary dipole estimators are null”; move Bonferroni to a non-primary comparison or delete it.

---

## PAPER-GPTM-B5 — MAJOR — Shuffle/null descriptions are internally inconsistent and not systematics-preserving

| Field | Audit |
|---|---|
| Location | Abstract; §Dipole Analysis; §Sensitivity; Conclusions canonical-N MASTER paragraph |
| Paper says verbatim | “per-pixel-shuffle null preserves the global \(p_{\rm CW}=0.4974\) monopole and per-pixel depth/mask-edge correlations.” |
| Paper says verbatim | “per-pixel random-label permutation null preserves the per-pixel marginals … only the CW vs CCW assignments are shuffled globally across the catalog.” |
| On-disk artifact says verbatim | Not accessible; cited artifacts include `canonical_n_master_l1_direct.json`, `injection_recovery_extended.json`. |
| Verdict | NOVEL MAJOR |

Concrete issue: A global label shuffle preserves positions and total pixel counts, but it destroys label–depth, label–PSF, label–morphology, and mask-edge label correlations; it also does not preserve per-pixel CW/CCW marginals. Calling this “systematics-inclusive” is unsupported unless the null explicitly conditions on those covariates.

Fix: Define the shuffle algorithm exactly. For systematics-inclusive claims, use a conditional/null model preserving depth/PSF/morphology/edge correlations, spatial blocks, or stratified shuffles; otherwise call the current null a random-label null only.

---

## PAPER-GPTM-B6 — MAJOR — Table V 4,758-galaxy gap explanation is not demonstrated and uses inconsistent predicates

| Field | Audit |
|---|---|
| Location | Table confidence bins footnote; §Confidence Stratification; §Bin-by-bin flatness |
| Paper says verbatim | “three high-confidence bins [0.6,1.0) sum to 944,826, which is 4,758 galaxies below … HC-spiral_p>0.6 \(n_{\rm spiral}=949,584\).” |
| Paper says verbatim | “difference arises from boundary-edge handling at exact \(p=0.6\) and at \(p=1.0\) … vs canonical `abs(p_cw_eq)>0.6` inclusion convention” |
| On-disk artifact says verbatim | Not accessible; cited artifact `face_on_robustness_results.json`. |
| Verdict | STILL-UNRESOLVED MAJOR |

Concrete issue: The claimed boundary-only explanation requires 4,758 objects exactly at \(p=0.6\) or \(p=1.0\), which is not shown. The cited predicate `abs(p_cw_eq)>0.6` is also not equivalent to \(\max(p_{\rm CW,eq},p_{\rm CCW,eq})>0.6\) and would mishandle high-confidence CCW objects.

Fix: Add an exact reconciliation table: counts at \(p=0.6\), \(p=1.0\), NaNs, class filters, and each predicate. Use one canonical HC-spiral predicate everywhere and update Table V/§Confidence to match it.
