# P4_v1095 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0130pt_P4_v1095_R14_R-round_real
**Wall time**: 83.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=82262, completion=4934, reasoning=3106, total=87196

---

# Verdict

No BLOCKER-grade findings. But there are 4 MAJOR methodology/significance regressions; v1.0.96 is needed before external review.

## PAPER-GPT5-M1 — MAJOR — MASTER “same data” overclaim persists

| Audit field | Text |
|---|---|
| Section | Abstract; §IV.A Dipole; Conclusions “Headline finding” |
| Paper says verbatim | “The pre-MASTER value and the post-MASTER headline differ in mask, in input-map definition, in monopole-subtraction treatment, and in MASTER mode-coupling inversion” |
| Paper also says verbatim | “inflates the raw pseudo-$C_\ell$ at $\ell\!=\!1$, collapsing to $-0.12\sigmaunit$ once the MASTER mode-coupling matrix is applied on the same data” |
| On-disk artifact says | Not available in prompt; manuscript cites `master_power_spectrum.json`, `canonical_n_master_l1_direct.json`, `monopole_mask_null_results.json` |
| Verdict | STILL-UNRESOLVED / REGRESSION |

Concrete issue: The abstract correctly admits the pre/post comparison changes map, mask, monopole subtraction, and estimator, but the conclusion reverts to the false “MASTER on same data” causal framing. This overstates MASTER as a clean deconvolution proof.

Fix: Replace all “collapses once MASTER is applied on the same data” language with “the full chain (map choice + monopole subtraction + mask choice + MASTER) yields the null; pure same-input MASTER cancellation is not demonstrated.”

## PAPER-GPT5-M2 — MAJOR — injection-recovery arithmetic still internally inconsistent

| Audit field | Text |
|---|---|
| Section | §IX.J Sensitivity; Table `mc_injection` |
| Paper says verbatim | “$N_{\rm MC,null}=1000$ per realization” |
| Paper says verbatim | “a per-pixel-shuffle null with $N_{\rm MC}=500$ realizations is run for significance” |
| Paper says verbatim | “$900$ injection fits ($N_{\rm inj}\!=\!100$ axes $\times$ $9$ amplitudes …) calibrated against $N_{\rm MC,null}\!=\!1000$ … per amplitude” |
| Paper says verbatim | “full per-injection table … for every one of the $500$ injections” |
| On-disk artifact says | Manuscript claims canonical artifact `injection_recovery_extended.json` has `n_mc_inj_per_amp=100`; artifact itself not available in prompt |
| Verdict | REGRESSION |

Concrete issue: The intended closure is 900 injection fits with 1000 null MC per amplitude, but the body still says 500 nulls, the table says 1000 per realization, and the parenthetical says 500 injections. This makes the reported recovery probabilities non-auditable.

Fix: State one convention everywhere: “900 injections = 9 amplitudes × 100 axes; each amplitude calibrated against a 1000-realization per-pixel-shuffle null.” Delete “500” and “per realization” unless actually true.

## PAPER-GPT5-M3 — MAJOR — hemisphere LEE framing is statistically contradictory

| Audit field | Text |
|---|---|
| Section | §IV.G Hemisphere Asymmetry; Fig. hemisphere caption; §IX.B |
| Paper says verbatim | “The maximum asymmetry found is $3.05\sigmaunit$ … does not survive a look-elsewhere correction … reduces the effective significance to $<\!1\sigmaunit$.” |
| Paper says verbatim | “zero of $N_{\rm MC}=10{,}000$ label-shuffle nulls reach the data, giving $p_{\rm LEE} \le … 10^{-4}$” |
| Paper says verbatim | “The direct-MC look-elsewhere null is therefore in the tail at $p_{\rm LEE}<10^{-4}$, tightening the Bonferroni / BH-FDR conclusion” |
| On-disk artifact says | Not available in prompt; manuscript cites `wave12_hemi_2026-05-01/results.json` |
| Verdict | STILL-UNRESOLVED |

Concrete issue: A direct max-statistic MC with zero exceedances is already a LEE-corrected rejection of the random-label null; it cannot “tighten” a Bonferroni/BH conclusion of `<1σ` under the same null. The text mixes different nulls/procedures without demoting the older Bonferroni claim.

Fix: Say plainly: “The random-label max-statistic null is rejected at $p_{\rm LEE}\le10^{-4}$; the older analytic Bonferroni grid calculation is not the operative calibration and is retained only as a conservative heuristic under a different independence assumption.”

## PAPER-GPT5-M4 — MAJOR — TTA derivation incorrectly says chirality score averages to zero per galaxy

| Audit field | Text |
|---|---|
| Section | §IX.A Raw systematics / TTA discussion |
| Paper says verbatim | “the soft-weighted chirality score $p_{\rm CW}^{\rm eq} - p_{\rm CCW}^{\rm eq}$ averages to zero per galaxy.” |
| Paper says verbatim | Earlier §III.D says TTA “does not force $\pcw^{\rm eq}\!=\!\pccw^{\rm eq}$ per galaxy” |
| On-disk artifact says | Not applicable; this is algebraic |
| Verdict | NOVEL / REGRESSION |

Concrete issue: Eq. (2) enforces flip-equivariance, not zero chirality per galaxy. A real chiral galaxy should retain nonzero $p_{\rm CW}^{\rm eq}-p_{\rm CCW}^{\rm eq}$; claiming per-galaxy cancellation is mathematically false and weakens the depth-coupling argument.

Fix: Replace with: “TTA makes the chirality score flip-antisymmetric under image reflection and cancels orientation-paired bias in ensemble; it does not make the per-galaxy chirality score vanish.”

## PAPER-GPT5-m1 — minor — Fisher half/full-amplitude prose still has a factor-of-two ambiguity

| Audit field | Text |
|---|---|
| Section | §IX.J Sensitivity; Conclusions sensitivity paragraph |
| Paper says verbatim | “$\sigma(A/2)\approx … 0.048\%$ … full-amplitude Fisher floor is $2\times0.048\%\approx0.097\%$; the $3\sigma$ full-amplitude floor is $\sim0.29\%$” |
| Paper also says verbatim | “At $3\sigmaunit$ significance the minimum detectable amplitude is $3\times0.048\%\approx0.14\%$, which we round … to $\sim0.2\%$” |
| On-disk artifact says | Not applicable; algebraic |
| Verdict | STILL-UNRESOLVED polish-tier |

Concrete issue: After correctly defining $0.048\%$ as the half-modulation 1σ, the prose immediately calls $3\times0.048\%$ a “minimum detectable amplitude,” which reads as full amplitude. The abstract is mostly fixed, but the derivation remains confusing.

Fix: Rewrite that paragraph as: “$3\sigma(A/2)=0.14\%$ half-modulation, corresponding to $A=0.29\%$ full amplitude; mask/$N_{\rm eff}$ inflation gives a conservative full-amplitude asymptote of $\sim0.4\%$.”

## PAPER-GPT5-m2 — minor — Ivezic LSST fused-metadata flag is closed

| Audit field | Text |
|---|---|
| Section | Bibliography `Ivezic:2019` |
| Paper says verbatim | “Astrophys.\ J.\ \textbf{873}, 111 (2019), DOI 10.3847/1538-4357/ab042c. The preprint arXiv:0805.2366 cited in earlier versions of this bibitem is the older LSST Science Book white paper, NOT the preprint of this specific ApJ reference-design article; the arXiv identifier has been removed…” |
| On-disk artifact says | Not applicable; bibliography source only |
| Verdict | HOLDS |

Concrete issue: No remaining fused arXiv/ApJ metadata problem in the visible bibitem. The explanatory note is acceptable though verbose.

Fix: None required; optional shorten the note for journal style.
