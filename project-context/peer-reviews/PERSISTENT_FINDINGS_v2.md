# Persistent Meta-Findings Tracker v2

Tracking META findings across 14 autoloop fires using
content-overlap fingerprinting (5-gram Jaccard >= 0.3).

Total META findings: 891
Distinct content-clusters: 885
Latest round: auto-2026-06-08_1819pt

## LOAD-BEARING (>=3 rounds)

## RECURRING (2 rounds)

### REC ESSENTIAL P1B - 2/14 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The β injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.”...

### REC ESSENTIAL P3 - 2/14 rounds
Rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-06_0004pt']
Example: “For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.”...

### REC ESSENTIAL P1B - 2/14 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “…10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE…”...

### REC MAJOR P1B - 2/14 rounds
Rounds: ['auto-2026-06-06_0021pt', 'auto-2026-06-08_1354pt']
Example: The paper states “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const.” The SN degeneracy is defined with h ≡ H0/(100 km s−1 Mpc−1) (i.e., MB − 5 log10 h), not H0; u...

## NEW this round (auto-2026-06-08_1819pt) - 30 clusters

- NEW ESSENTIAL: **5**
- NEW MAJOR: 11
- NEW MINOR/NIT: 14

### NEW ESS P1B - P1B-META-E1
> ** The abstract footnote and §VI both anchor the comparison to "Eskilt & Komatsu joint **WMAP9 + Planck PR3**" giving 0.342° ± 0.094° (3.6σ). But Appendix C states the actual ALP-MCMC uses "Planck PR4 + **ACT DR6** EB-spectrum likelihoods." This is n...

### NEW ESS P1B - P1B-META-E2
> ** The paper invokes *three different* reference β values from the literature, in three different sections, none clearly the privileged comparator: - §IV intro: "β = 0.30° ± 0.11° (Planck NPIPE) and β = 0.215° ± 0.074° (ACT DR6)" - §VI Eq. (4): "β_co...

### NEW ESS P1B - P1B-META-E3
> ** Section IV describes the mask (fsky = 0.32, C2 apodization at 2°), beam (5' FWHM), purification (purify_b=True), mode-coupling matrix (NmtWorkspace.compute_coupling_matrix), binning (Δℓ = 20, ℓ ∈ [30, 1024]), and noise level (∆_P = 10 µK·arcmin). ...

### NEW ESS P5 - P5-META-E1
> ** DESIVAST is constructed on the *volume-limited* BGS sample at z ≤ 0.24 (Rincón et al. 2025). The Paper IV chirality catalog is *flux-limited* at r ≤ 17.8 in DESI Legacy. When the author restricts to z ≤ 0.24 and assigns void/non-void labels by poi...

### NEW ESS P5 - P5-META-E2
> ** The primary analysis reports |∆fCW| < 0.002 (the spread across three DESIVAST algorithms) but does not compute a proper 2σ upper limit on the environment-dependent effect size. With nvoid = 56,981, the 1σ counting-statistics floor on fCW is 1/(2√5...
