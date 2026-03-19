# 01: Estimator Frame Audit

## The Three Estimator Approaches for f_NL

### 1. Scale-Dependent Bias (SDB) — Power Spectrum Based

**How it works:** Primordial local non-Gaussianity induces a scale-dependent correction to galaxy bias:
b(k) = b₁ + Δb(k) where Δb(k) = 2(b₁-1)·f_NL·δ_c / [α(k,z)·D(z)·T(k)·k²]

The 1/k² growth at large scales is detectable in the galaxy power spectrum P_g(k).

**Advantages:**
- Directly measures squeezed-limit bispectrum (where matter bounce IS exactly local)
- No template mismatch for our signal
- Multi-tracer technique can beat cosmic variance (Seljak 2009)
- Already the standard method for LSS f_NL constraints

**Disadvantages:**
- Requires accurate modeling of galaxy bias b₁
- Systematic floors from survey geometry, photo-z errors, stellar contamination
- Relativistic projection effects create an effective f_NL ~ O(1) contamination (see below)

**Appropriate for:** SPHEREx (primary), MegaMapper (primary), DESI, Euclid

### 2. Galaxy Bispectrum Estimator

**How it works:** Directly measure the three-point correlation of galaxies in Fourier space and fit to the local template.

**Advantages:**
- More information than power spectrum alone
- Can distinguish shapes (local vs equilateral)
- Less sensitive to bias modeling (enters differently)

**Disadvantages:**
- Much harder to measure than the power spectrum
- Higher noise (6-point function in the covariance)
- Current implementations are computationally expensive
- Typically gives WEAKER constraints than SDB for local f_NL

**Appropriate for:** MegaMapper (supplementary), not SPHEREx primary

### 3. CMB Bispectrum Estimator (KSW)

**How it works:** Measure the three-point function of CMB temperature/polarization maps and fit to the local template with signal-to-noise weighting.

**Advantages:**
- Well-understood, mature methodology
- Template projection is explicit and computable

**Disadvantages:**
- For local f_NL, LSS will beat CMB (Planck σ ~ 5, CMB-S4 σ ~ 2.5)
- Template mismatch with the matter-bounce shape is non-trivial for CMB (our shape is "loosely local" but not exactly local in the full triangle space)

**Appropriate for:** Planck (already done), CMB-S4 (supplementary)

## Which Estimator for Which Survey?

| Survey | Primary Estimator | Why |
|--------|------------------|-----|
| **SPHEREx** | Scale-dependent bias (P(k)) | Photo-z survey; SDB is the standard f_NL method |
| **MegaMapper** | Scale-dependent bias (P(k)) | Spectroscopic; multi-tracer gives best σ(f_NL) |
| Planck | CMB bispectrum (KSW) | Already published: f_NL = -0.9 ± 5.1 |
| CMB-S4 | CMB bispectrum | σ ~ 2.5 — supplementary to LSS |

## Is "f_NL^local" the Right Language?

**YES, for LSS surveys.** The SDB estimator is intrinsically a squeezed-limit measurement. The matter-bounce bispectrum is exactly local in the squeezed limit (|B|_NL → -35/8 as k₁/k → 0). There is no approximation involved — the survey estimator and the theoretical prediction match exactly in the relevant limit.

**APPROXIMATELY, for CMB surveys.** The KSW estimator integrates over all triangles. The matter-bounce shape differs from the exact local template in the equilateral and folded regions. The effective f_NL measured by the CMB estimator would be f_NL^local × cos(θ), where cos(θ) requires a proper computation with CMB transfer functions.

## Should We Use a Custom Template?

**NO for LSS forecasts.** The local template IS the right template because SDB probes the squeezed limit.

**POSSIBLY for CMB.** A custom template would extract the full matter-bounce signal. But CMB is not the primary test (LSS will do better), so this is low priority.

## The Matter-Bounce Signal Should Be Treated As:

**EXACTLY LOCAL for LSS purposes.** Not "approximately local" or "loosely local" — EXACTLY local in the limit that matters for the estimator. The equilateral and folded deviations are invisible to the SDB estimator.
