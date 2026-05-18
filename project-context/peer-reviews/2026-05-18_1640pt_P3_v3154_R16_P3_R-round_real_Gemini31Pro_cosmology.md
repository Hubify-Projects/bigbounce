# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1640pt_P3_v3154_R16
**Wall time**: 88.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=67072, completion=11440, reasoning=10459, total=78512

---

## Finding 1 (BLOCKER)
**ID:** PAPER-GEM-B1
**Section:** 1, 5, Appendix D'
**Issue:** The paper heavily motivates the $f_{\rm NL} = -35/8$ and $\gamma=3.0$ targets from the "simplest scalar-only matter-dominated ($w=0$) bounce class." This specific model predicts a tensor-to-scalar ratio $r \approx 24\pi \approx 75$, which is catastrophically falsified by CMB bounds ($r < 0.036$); viable matter bounces require additional fields (e.g., a curvaton) which break the rigid $f_{\rm NL} = -35/8$ prediction.
**Fix:** Explicitly state the $r$ tension for the scalar-only $w=0$ bounce and clarify that viable multi-field bounce completions render the $f_{\rm NL}$ amplitude model-dependent rather than rigidly $-35/8$.

## Finding 2 (BLOCKER)
**ID:** PAPER-GEM-B2
**Section:** Abstract, 5
**Issue:** The multi-tracer Fisher forecast requires $\alpha$ to be the bias enhancement of the *anomaly tracers* relative to the *standard DESI QSOs*. The empirical measurement computes $\alpha \equiv b_{\rm QSO\,cand}/b_{\rm full\,anomaly} - 1$, which is the internal bias contrast of the anomaly catalog, making its insertion into the standard-QSO-anchored Fisher pipeline mathematically invalid.
**Fix:** Recompute the empirical bias ratio against the standard DESI QSO catalog, or explicitly redefine the Fisher baseline to use the full anomaly catalog as the low-bias tracer.

## Finding 3 (MAJOR)
**ID:** PAPER-GEM-M1
**Section:** Abstract, 5
**Issue:** The text retains the linear error propagation $\sigfnl = 8.27 \pm 2.37$ as a "reference", using the slope $-3.66$. This is a secant slope from the stationary point $\alpha=0$ to $\alpha=0.15$; the true tangent slope of $(F_0 + c\alpha^2)^{-1/2}$ at $\alpha=0.19$ is $\approx -7.6$, making the quoted $\pm 2.37$ reference mathematically invalid even as a non-canonical baseline.
**Fix:** Completely remove the local-linear $\pm 2.37$ and $\pm 7.43$ references; quote only the exact asymmetric bounds derived from the Fisher-positivity-respecting $\alpha^2$ form.

## Finding 4 (minor)
**ID:** PAPER-GEM-m1
**Section:** 5
**Issue:** The text claims GR projection effects "perfectly mimic local-PNG scale-dependent bias at large scales." While they share the $k^{-2}$ scaling, GR projection terms have distinct redshift evolution and tracer-response dependencies (magnification bias $s$, evolution bias $f_{\rm evo}$) that break the degeneracy in tomographic/multi-tracer analyses.
**Fix:** Change "perfectly mimic" to "mimic the $k^{-2}$ scale dependence of" and note that distinct redshift and tracer-response dependencies allow them to be separated.

## Finding 5 (minor)
**ID:** PAPER-GEM-m2
**Section:** 5
**Issue:** The empirical bias ratio $b_{\rm QSO\,cand}/b_{\rm full\,anomaly}$ compares a subset to a parent set that contains it. This introduces correlated shot noise ($P_{12}^{\rm noise} \neq 0$) which biases the Landy-Szalay cross-correlation and ratio estimators if not explicitly subtracted.
**Fix:** State whether the cross-shot-noise was subtracted, or measure the ratio against the disjoint non-QSO anomaly subset ($b_{\rm QSO\,cand}/b_{\rm non\,QSO}$) to ensure independent shot noise.

## Finding 6 (nit)
**ID:** PAPER-GEM-n1
**Section:** Appendix D'
**Issue:** The text invokes "Savage-Dickey on the existing chain" to compare the $\gamma=3.0$ and $\gamma=4.33$ points. Savage-Dickey is for nested models with integrated parameters; comparing two fixed points in the same parameter space is just a direct ratio of their marginal posterior densities.
**Fix:** Replace "Savage-Dickey" with "ratio of marginal posterior densities" for the fixed-point comparison.
