# P2_v1730 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P2_v1730_R3_R-round_real
**Wall time**: 182.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=31248, completion=11617, reasoning=9840, total=42865

---

## PAPER-GPT-B1 — BLOCKER — `f_{\rm NL}` convention logic is internally inconsistent

- **Location:** Abstract caveat; Appendix A/A.2; Conclusion.
- **Concrete issue:** The paper treats the `-35/16` alternative both as a mere normalization convention and as a physically halved signal. If it is only a convention, `f_{\rm NL}` and `\sigma(f_{\rm NL})` rescale together and the detection significance cannot halve; if it is a physical missing-in-in-factor ambiguity, it is not a convention. Appendix A also states the Planck/Komatsu-Spergel **ζ** convention as `c=2`, contradicting the abstract’s correct `B_\zeta=(6 f_{\rm NL}/5)[PP+\cdots]`.
- **Truth audit:**

| Paper claim | Audit |
|---|---|
| “same physical bispectrum” / convention difference | significance should be invariant |
| Table A.2 uses same `σ=0.7` and halves significance | only valid for a physical amplitude change, not convention |
| Planck ζ convention has `c=2` | conflicts with `ζ=ζ_g+(3/5)f_{\rm NL}ζ_g^2` |

- **Fix:** Define one observational convention, preferably `B_\zeta=(6/5)f_{\rm NL}[PP+\cdots]`, and redo the Cai/Li-Brandenberger mapping. Remove the halved-significance “convention” language unless the paper proves a physical factor-of-two amplitude ambiguity.

## PAPER-GPT-B2 — BLOCKER — headline `3–5σ` systematic budget is not actually propagated

- **Location:** Abstract; Secs. 4, 7, 8.2, Conclusion.
- **Concrete issue:** The `3–5σ after combined systematic budget` claim is assembled from individual degradations, not from a joint covariance/Fisher/likelihood propagation. Using the paper’s own conservative factors can push the significance below `3σ`.
- **Truth audit:**

| Step | Value from paper’s numbers |
|---|---:|
| naive `4.375/0.7` | `6.25σ` |
| template overlap `r≈0.83` | `≈5.2σ` |
| quasi-dust lower amplitude `4.02` | `≈4.8σ` |
| plus `b_\phi` 50%, GR 30%, photo-z 5% | `≈2.3–2.5σ` |

- **Fix:** Provide a single systematic-budget table with `σ_eff` or a nuisance-marginalized Fisher matrix. Downgrade “SPHEREx tests at `3–5σ`” and the “null excludes at `>4σ`” claim unless the joint propagation supports them.

## PAPER-GPT-M1 — MAJOR — template-overlap uncertainty is based on an artificial coefficient null space

- **Location:** Sec. 2.1 “The Prediction”; Sec. 3.2 “Template Projection”.
- **Concrete issue:** The paper treats the six polynomial coefficients as underdetermined because three benchmark configurations give only three constraints. But the cited Cai et al. bispectrum is a full shape calculation, not a three-point interpolation problem; arbitrary null-space coefficient scans are not a physical theory prior.
- **Truth audit:**

| Paper procedure | Audit |
|---|---|
| Fit six coefficients from three benchmark triangles | self-created underdetermination |
| Sample null-space balls of radius 10–500 | no physical measure/prior |
| Use resulting `r=0.85±0.13` in systematic budget | not a validated matter-bounce uncertainty |

- **Fix:** Use the exact published polynomial or rederive it from the cubic action. Treat null-space scans only as a numerical stress test, not as a physical uncertainty entering the forecast.

## PAPER-GPT-M2 — MAJOR — joint `(f_{\rm NL},n_{f_{\rm NL}})` Fisher result is unsupported and partly mis-scoped

- **Location:** Sec. 8.3 “Joint `(f_{\rm NL}, n_{f_{\rm NL}})` Forecast”.
- **Concrete issue:** The arithmetic `1/sqrt(1-ρ²)=3.86` for `ρ=0.966` is correct, but the implied unmarginalized `σ(f_{\rm NL})≈0.114` is `≈6.1×` sharper than the published SPHEREx `σ≈0.7` baseline and no Fisher inputs are released. The same paragraph also lists the bispectrum shape-mismatch factor `r=0.84` in the SDB joint systematic budget after correctly saying `r` does not apply to SDB.
- **Truth audit:**

| Quantity | Audit |
|---|---:|
| `ρ=0.966` degradation | `3.86`, correct |
| `0.44/3.86` | `0.114`, correct |
| `4.375/0.44` | `9.9σ`, arithmetic correct |
| Published/input support | absent in manuscript |

- **Fix:** Remove the `9.9σ`, `σ(n_{fNL})=0.086`, and `σ(fNL)=0.44` as forecast claims until the six-bin Fisher inputs/code are released and benchmarked. Do not include bispectrum `r` in SDB-only systematics.

## PAPER-GPT-M3 — MAJOR — residual mechanism-independence / consistency-relation overclaim remains

- **Location:** Sec. 2.2 “Mechanism Independence”; Conclusion.
- **Concrete issue:** Sec. 2.2 says the prediction depends only on assumptions `(a)–(c)` and “does not depend on the specific bounce mechanism,” omitting the later load-bearing assumptions `(d)–(f)` on cubic transmission, no prolonged post-bounce inflation, and negligible fermions. The conclusion also states that in the physical-observer frame “matter bounce predicts `-4.375`,” but no CFC-frame transformation of the bounce bispectrum is derived, and earlier text says the surveys measure the gauge-frame local template.
- **Truth audit:**

| Site | Audit |
|---|---|
| Intro/Assumptions | mostly scoped to scalar-only, no prolonged inflation, negligible fermions |
| Sec. 2.2 | stale overbroad mechanism-independence claim |
| Conclusion CFC comparison | overstates applicability beyond derived observable |

- **Fix:** Rewrite Sec. 2.2 to say “UV-completion independent only within the scalar-only `w≈0` class satisfying assumptions `(a)–(f)`.” Remove or qualify the CFC-frame bounce `-4.375` statement unless explicitly derived.

## PAPER-GPT-M4 — MAJOR — Bayes-factor and reproducibility metadata are still not audit-clean

- **Location:** Sec. 6.3; Conclusion; Data and Code Availability; citation text around Cai/Li/Heinrich.
- **Concrete issue:** The Bayes-factor section calls the GR/`b_\phi` treatment “marginalization,” but the displayed evidence integral marginalizes only over `f_{\rm NL}`; nuisance effects are sampled externally as shifts/σ-draws, which is sensitivity mapping, not a hierarchical evidence calculation. Metadata also contradicts itself: body/abstract say `3×10^5` realizations, conclusion says `>6×10^5`; the code tag is `v1.7.26` for a `v1.7.30` manuscript; the factor-of-two reference alternates between Cai & Brandenberger, Li & Brandenberger, and Li et al.
- **Truth audit:**

| Claim | Audit |
|---|---|
| “marginalized GR contamination” | no nuisance evidence integral shown |
| MC validation count | `3×10^5` vs stale `>6×10^5` |
| reproducibility tag | old `v1.7.26` tag |
| bibliography identity | inconsistent names for load-bearing convention paper |

- **Fix:** Either write the full hierarchical evidence integral over GR, `b_\phi`, survey efficiency, and theory width, or relabel the exercise as prior/sensitivity scanning. Correct the realization count, pin the actual v1.7.30 artifact/commit, and canonicalize the bibliography metadata.
