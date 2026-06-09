# Persistent Meta-Findings Tracker v2

Tracking META findings across 13 autoloop fires using
content-overlap fingerprinting (5-gram Jaccard >= 0.3).

Total META findings: 861
Distinct content-clusters: 855
Latest round: auto-2026-06-08_1737pt

## LOAD-BEARING (>=3 rounds)

## RECURRING (2 rounds)

### REC ESSENTIAL P1B - 2/13 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The β injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.”...

### REC ESSENTIAL P3 - 2/13 rounds
Rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-06_0004pt']
Example: “For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.”...

### REC ESSENTIAL P1B - 2/13 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “…10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE…”...

### REC MAJOR P1B - 2/13 rounds
Rounds: ['auto-2026-06-06_0021pt', 'auto-2026-06-08_1354pt']
Example: The paper states “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const.” The SN degeneracy is defined with h ≡ H0/(100 km s−1 Mpc−1) (i.e., MB − 5 log10 h), not H0; u...

## NEW this round (auto-2026-06-08_1737pt) - 36 clusters

- NEW ESSENTIAL: **8**
- NEW MAJOR: 14
- NEW MINOR/NIT: 14

### NEW ESS P1B - P1B-META-E1
> * The paper validates the pipeline at fₛₖᵧ = 0.32 (apodized) and claims this exercises the deconvolution behind the published Planck NPIPE β = 0.30°±0.11° and ACT DR6 β = 0.215°±0.074° measurements. But the published Planck birefringence analyses (Es...

### NEW ESS P1B - P1B-META-E2
> * App. C states "Caγ: fixed at one of {4, 8, 12} across the three configurations." But Section VI derives that the observed β = 0.342° requires Caγ(Δφ/fa) ≈ 10.3, and with Δφ/fa ∈ [0.2, 1.1] the required Caγ spans 9–51. *Two of the three grid points ...

### NEW ESS P1B - P1B-META-E3
> * The paper writes "This neglects shared calibration systematics; the published joint analysis at 3.6σ [2] is the headline," implying the 3.9σ figure is an *upper bound* on the true significance. But shared systematics produce *positively correlated*...

### NEW ESS P1B - P1B-META-E4
> * The text states Caγ Δφ/fa ≈ 10.3 with Δφ/fa ∈ [0.2, 1.1] giving Caγ ∈ [9, 51]. But footnote 5 requires θᵢ ~ 0.1 for spectator status, and Sec. VII states "Δφ/fa ∝ θᵢ along the underdamped trajectory." With θᵢ = 0.1 vs the natural-prior midpoint θᵢ ...

### NEW ESS P1B - P1B-META-E5
> * Eq. (2) gives Δφ/fa ≈ 0.65 for (m = H₀, θᵢ = 1). Eq. (3) then evaluates β at (Caγ = 8, θᵢ = 1, m ≈ 2H₀) using Δφ/fa = 1.07, citing "midpoint m ≈ 1.8 H₀, Δφ/fa ≈ 1.0." Going from m = H₀ to m = 1.8 H₀ at fixed θᵢ = 1 cannot simultaneously increase Δφ...

### NEW ESS P4 - P4-META-E1
> ** A null measured with only **50% recovery probability at A = 0.75%** does NOT exclude A = 0.75% signals — it is consistent with them by construction. A future 5σ detection at A = 0.75% would therefore be entirely **consistent** with the present non...

### NEW ESS P4 - P4-META-E2
> ** A +4.31σ Catalog-C dipole estimator is nowhere in Table I, Section IV C, or the headline results. The text presents it as "consistent with 0.43σ" but +4.31σ vs +0.43σ is a factor-10 discrepancy at the same nominal sample — these are NOT consistent...

### NEW ESS P4 - P4-META-E3
> ** §III A lists primary estimators (real-space +0.43σ, subsample-mask MASTER −0.122σ) and demotes the canonical-mask MASTER (+3.64σ) to "diagnostic." But the manuscript also describes the canonical-mask result as the natural matched-footprint estimat...
