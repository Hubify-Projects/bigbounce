# Persistent Meta-Findings Tracker v2

Tracking META findings across 10 autoloop fires using
content-overlap fingerprinting (5-gram Jaccard >= 0.3).

Total META findings: 684
Distinct content-clusters: 678
Latest round: auto-2026-06-08_1424pt

## LOAD-BEARING (>=3 rounds)

## RECURRING (2 rounds)

### REC ESSENTIAL P1B - 2/10 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The β injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.”...

### REC ESSENTIAL P3 - 2/10 rounds
Rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-06_0004pt']
Example: “For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.”...

### REC ESSENTIAL P1B - 2/10 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “…10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE…”...

### REC MAJOR P1B - 2/10 rounds
Rounds: ['auto-2026-06-06_0021pt', 'auto-2026-06-08_1354pt']
Example: The paper states “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const.” The SN degeneracy is defined with h ≡ H0/(100 km s−1 Mpc−1) (i.e., MB − 5 log10 h), not H0; u...

## NEW this round (auto-2026-06-08_1424pt) - 67 clusters

- NEW ESSENTIAL: **16**
- NEW MAJOR: 35
- NEW MINOR/NIT: 16

### NEW ESS P1A - P1A-META-E1
> The text inserts an electromagnetic loop factor αem/(4π) into a purely gravitational/fermion one‑loop estimate for a Holst/Nieh–Yan–induced operator. Quote: “The dimensionless coefficient is O(αem/4π)…” There is no EM field in the Route‑2 operator θN...

### NEW ESS P1A - P1A-META-E2
> The manuscript treats “θ(x) is the Nieh–Yan pseudoscalar” as a propagating field with ∂μθ ∼ H0 today, without introducing a dynamical Immirzi field or propagating torsion. In minimal EC with constant γ and non-propagating torsion, θNY is a density bu...

### NEW ESS P1A - P1A-META-E5
> The text claims “this holds at the cubic axial-current operator level because the cube of the fermion bilinear scales as the cube of the fermion number density.” There is no cubic axial-current operator in minimal EC (torsion ∝ J5; the induced contac...

### NEW ESS P1B - P1B-META-E1
> “βALP = 0.336° ± 0.107° (Caγ = 8 fixed), … The field-displacement range Δϕ/fa ∈ [0.2, 1.1] …” Using the paper’s own formula β = [αEM/(4π)] Caγ (Δϕ/fa), the maximum β attainable with Caγ = 8 and Δϕ/fa ≤ 1.1 is: βmax ≈ (5.8×10−4) × 8 × 1.1 rad ≈ 0.0051...

### NEW ESS P1B - P1B-META-E2
> “χ2total 14037.4 ± 5.6 … The mean-of-total χ2 here is GetDist’s weighted-sample average over the full posterior…” A posterior-weighted mean χ2 with an attached “±” spread is not a recognized GOF statistic for model checking; it conflates parameter-vo...

### NEW ESS P2 - P2-META-E1
> With the standard normalization L ⊃ −(g_aγ/4)φF F̃ and g_aγ = (α/2π)(C/f_a), the predicted rotation is β = (α/4π) C Δφ/f_a. Using the paper’s own Δφ/f_a ≈ 0.24 (from Eq. 1) and C ~ O(1) gives β ≈ 0.00058 × 0.24 ≈ 1.4×10^−4 rad ≈ 0.008°, not 0.27°. To...

### NEW ESS P2 - P2-META-E2
> The Bayes factor is computed with a flat prior β ∈ [0°, 1°], i.e., a one-sided prior. Isotropic cosmic birefringence can be positive or negative. Using a one-sided prior doubles the prior density at β=0 relative to the natural symmetric choice β ∈ [−...

### NEW ESS P3 - P3-META-E1
> The anomaly score is built on an unweighted per-element MSE, “MSE(x) = (1/N) ∑(xi − x̂i)^2” (Eq. 1), with no statement that inputs are whitened by per-pixel uncertainty or even standardized feature scales for the catalog surveys. For spectra this ign...

### NEW ESS P3 - P3-META-E2
> The eROSITA selection is described as “Anomaly count: 298 at S > 0.259 (top 0.03%; data-driven score-knee threshold).” Elsewhere the paper defines S as the z-scored BigAE MSE, while Table III introduces SIF,raw as the IsolationForest raw score and SB...

### NEW ESS P3 - P3-META-E3
> The paper highlights “only 0.2%” of the DESI top-10,000 anomalies are in SIMBAD. At 5″, the stated SIMBAD random-coincidence probability is Pfalse ≈ 2.4×10^-3 per source. For 10,000 sources, the expected number of random matches is ≈24. The observed ...

### NEW ESS P3 - P3-META-E4
> In the NANOGrav MCMC summary, you report “γ = 2.567 ± 0.382 (median 2.591, 68% CI [2.304, 2.882]).” A ±0.382 Gaussian summary is inconsistent with the quoted 68% interval width (2.882 − 2.304 = 0.578; half-width ≈ 0.289). The “±” value does not match...

### NEW ESS P4 - P4-META-E1
> The paper repeatedly describes the main permutation null as “per-pixel random-label permutation” or “per-pixel-shuffle.” If labels are permuted within each pixel p while holding NCW(p) and NCCW(p) fixed, the per-pixel asymmetry Ap = (NCW−NCCW)/(NCW+N...

### NEW ESS P4 - P4-META-E2
> The MASTER mode-coupling matrix is constructed without ℓ = 0 on either input or output: “the MASTER mode-coupling matrix does NOT include ℓ=0 on either the input or output side.” With an incomplete sky and a nontrivial mask, this prevents the deconvo...

### NEW ESS P5 - P5-META-E1
> The paper claims two incompatible “ranges” for the same canonical configuration. Earlier (Table II) the canonical V‑Web run has fCW values {0.4836, 0.5034, 0.4980, 0.4963}, a range of 0.0198 = 1.98 percentage points. But Table VI reports for Rs=25, λ...

### NEW ESS P5 - P5-META-E2
> The tidal field is built only from 0.01 ≤ z ≤ 2.0 (“yields 14,622,283 galaxies”), but the matched catalog contains objects up to zmax = 3.83 (Table I). The manuscript never states that environment labels are restricted to z ≤ 2 for the chirality anal...

### NEW ESS P5 - P5-META-E3
> The DESIVAST void/non-void comparison appears to treat “non-void” as “not inside any DESIVAST hole” across the entire z ≤ 0.24 matched sample (nnon-void = 621,964). Pixels with zero DESIVAST coverage are then, by construction, classified as “non-void...
