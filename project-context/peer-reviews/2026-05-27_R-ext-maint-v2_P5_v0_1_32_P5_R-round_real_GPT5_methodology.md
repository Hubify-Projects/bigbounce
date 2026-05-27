# P5 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P5_v0_1_32
**Wall time**: 101.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=29172, completion=5716, reasoning=4660, total=34888

---

No blocker-grade convergence confirmation: convergence does **not** hold; blocker issues remain.

## PAPER-GPT-B1 — BLOCKER — Abstract / Table I / Table II / §VII “Phase 2”

**Issue:** The headline sample universe is arithmetically inconsistent. The V-Web class counts sum to 812,793, not the stated 791,635 chirality-relevant spirals; class CW counts sum to 404,111, not Table I’s 393,592. Phase-2 also reports a filament bin with \(n=3{,}696{,}152\), impossible for the stated matched CW/CCW sample, and its canonical range \(0.165\) pp contradicts Table II’s \(1.98\) pp.

**Fix:** Define one analysis sample per result, regenerate all tables/abstract claims from that sample, and add a reconciliation table. Do not mix the 791,635 strict sample, 812,793 relaxed env-labeled superset, and any larger catalog in the same headline statistic.

## PAPER-GPT-B2 — BLOCKER — §IV.A V-Web algorithm, steps 8–11

**Issue:** The Fourier tidal-tensor sign is wrong as written. With \(\nabla^2\Phi=\delta\), \(\Phi(k)=-\delta_k/k^2\), so \(T_{ij}=\partial_i\partial_j\Phi=-k_i k_j\Phi=+k_i k_j\delta_k/k^2\); the paper writes \(T_{ij}=k_i k_j\Phi\), giving \({\rm Tr}\,T=-\delta\) and potentially swapping overdense/underdense classifications.

**Fix:** State the exact convention and verify \({\rm Tr}\,T=\delta\). If the code uses the paper’s sign, rerun all V-Web labels; if the code differs, correct the derivation and add a unit test.

## PAPER-GPT-M1 — MAJOR — §IV V-Web / §X limitations

**Issue:** The V-Web density field is built from raw DESI counts in a thin, flux-limited, evolving survey shell without a random catalog, radial selection correction, angular completeness weights, or proper window deconvolution. A global in-mask mean plus FFT smoothing in a cubical box is not a valid survey-window treatment; the paper itself later finds severe edge artifacts and poor DESIVAST/ASTRA agreement.

**Fix:** Recompute the density contrast as \((D-R)/R\) using DESI randoms/selection weights, mask-aware smoothing or constrained reconstruction, and boundary tests. Otherwise downgrade the V-Web labels to exploratory and make DESIVAST/ASTRA the primary environment classifiers.

## PAPER-GPT-M2 — MAJOR — §I, §V, §VII cross-survey residuals

**Issue:** Statistical significance is framed inconsistently. Paper IV’s \(f_{\rm CW}=0.4974\pm0.000279\) is \(\sim9.3\sigma\) from 0.5 statistically, not “consistent with parity at \(\sim1\sigma\)” unless an explicit systematic error dominates; later sections call the same monopole \(\sim9.5\sigma\). The P5 monopole subtraction also treats the estimated global monopole as fixed and does not propagate its uncertainty/covariance with class bins.

**Fix:** Separate statistical and systematic uncertainties. Use a hierarchical/binomial or multinomial model with a shared catalog-monopole nuisance parameter and environment offsets, reporting marginalized environment-offset posteriors or profile-likelihood intervals.

## PAPER-GPT-M3 — MAJOR — §VII.E Tempel / §VII concurrent literature / §VIII ASTRA

**Issue:** “Concordance” is overclaimed. Matching \(f_{\rm CW}\) between different samples/classifiers mostly tests that both inherit the same global chirality monopole, not that the environment classifiers agree. The paper also calls the Tempel filament result “load-bearing” despite earlier saying it is supporting only.

**Fix:** Replace fraction-agreement claims with same-galaxy confusion matrices, conditional two-sample tests within the overlap, and classifier-uncertainty propagation. Remove “load-bearing” language for Tempel/T-Web volume-fraction comparisons.

## PAPER-GPT-M4 — MAJOR — §X Conclusions, “Mapping to a physical operator”

**Issue:** The EFT bound is dimensionally and physically under-specified. The operator’s mass dimensions are not defined, \(g_\phi|\nabla\phi|/H_0\) is not shown to be dimensionless, \(\hat z\) is observer-frame rather than covariant, and no transfer function connects the operator to \(\Delta f_{\rm CW}\).

**Fix:** Either remove the numerical coupling bound or recast it as a purely phenomenological amplitude bound on \(\Delta f_{\rm CW}^{\rm env}\). A real EFT constraint needs field normalization, operator dimension, selection/transfer model, and marginalized nuisance parameters.
