# Persistent Meta-Findings Tracker v2

Tracking META findings across 12 autoloop fires using
content-overlap fingerprinting (5-gram Jaccard >= 0.3).

Total META findings: 825
Distinct content-clusters: 819
Latest round: auto-2026-06-08_1632pt

## LOAD-BEARING (>=3 rounds)

## RECURRING (2 rounds)

### REC ESSENTIAL P1B - 2/12 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin… The β injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.”...

### REC ESSENTIAL P3 - 2/12 rounds
Rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-06_0004pt']
Example: “For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.”...

### REC ESSENTIAL P1B - 2/12 rounds
Rounds: ['auto-2026-06-05_1617pt', 'auto-2026-06-06_0004pt']
Example: “…10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE…”...

### REC MAJOR P1B - 2/12 rounds
Rounds: ['auto-2026-06-06_0021pt', 'auto-2026-06-08_1354pt']
Example: The paper states “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const.” The SN degeneracy is defined with h ≡ H0/(100 km s−1 Mpc−1) (i.e., MB − 5 log10 h), not H0; u...

## NEW this round (auto-2026-06-08_1632pt) - 74 clusters

- NEW ESSENTIAL: **14**
- NEW MAJOR: 36
- NEW MINOR/NIT: 24

### NEW ESS P1A - P1A-META-E1
> The ratio is written “Δθone-loop/Δθobs ∼ [αem/(4π)] [H0/MPl] / [MPl(α/M) βobs] ∼ [αem/(4π)] (H0/MPl) · (M/MPl) · α · βobs” The second step is algebraically incorrect. 1/[MPl(α/M)βobs] = (M)/(α MPl) · (1/βobs), not “(M/MPl)·α·βobs”. Both α and βobs ha...

### NEW ESS P1A - P1A-META-E2
> Two incompatible four-fermion contact coefficients are used without reconciliation: - Eq. (4): Lint = −(3π GN/2) [γ^2/(γ^2+1)] J5·J5 (explicit γ dependence). - Eq. (13): LNJLtor = −(3/16) κ (ψ̄γaγ5ψ)^2 (no γ dependence). The text later asserts “torsi...

### NEW ESS P1B - P1B-META-E1
> Possible supernova double counting and ambiguous DES labeling. Table II’s likelihood stack includes “DES-Y5 + Pantheon+,” while ref. [14] (DES-SN5YR) is also cited elsewhere. If “DES-Y5” denotes the DES Year-5 SN sample (as opposed to 3×2pt lensing/c...

### NEW ESS P1B - P1B-META-E2
> Unspecified BBN treatment with ΔNeff. The ΔNeff constraint depends sensitively on the helium fraction Yp(H, ωb, Neff). The manuscript never states whether Yp was set by BBN consistency (and with which solver, priors, or fitting function) or fixed ind...

### NEW ESS P2 - P2-META-E1
> The model assumes fa ∼ MPl and m ∼ H0 with θi ∼ O(1), while repeatedly calling the ALP a “spectator field.” For a canonical axion with V = m^2 f_a^2 (1 − cos(ϕ/fa)), the mean energy density today is ρϕ ≈ m^2 f_a^2 (1 − cos θi). Using m = H0 and f_a =...

### NEW ESS P3 - P3-META-E1
> Hidden self-normalization in the α estimate. The paper defines b ≡ bQSO_cand/bfull_anomaly and reports αjk = 0.19 ± 0.65 from Landy–Szalay on the 5,384 QSO-candidate sample. It is never stated that the QSO-candidate subset is removed from the “full a...

### NEW ESS P4 - P4-META-E1
> “We emphasize at the outset that this ℓ = 1 observable is the isotropy-breaking axial-vector channel and is parity-EVEN: it is NOT a direct parity-violation test…”...

### NEW ESS P4 - P4-META-E2
> “This procedure enforces flip-equivariance of the output protocol (flip-swap correlation = 1.000).” and Table V: “T1: Flip-swap r > 0.80 — Result 1.000.”...

### NEW ESS P4 - P4-META-E3
> “The NaMaster weight (mask) map assigns Wp = N(p)all… The asymmetry field is Ap = (NCW−NCCW)/(NCW+NCCW) (spirals only)… The depth weighting does not introduce a monopole–dipole coupling because the galaxy-weighted mask-mean ⟨A⟩mask,gw is subtracted…”...

### NEW ESS P4 - P4-META-E4
> “post-MASTER canonical-mask direct-MC residual is +3.64σ (…; empirical rank pMC = 0.030…)”...

### NEW ESS P5 - P5-META-E1
> “Cloud-in-Cell deposit onto a 256^3 comoving grid … Convert counts to overdensity δ = ρ/ρ̄ − 1 … Gaussian-smooth δ in Fourier space … Solve Poisson …” with no mention of random catalogs or any n(z) correction despite using 14.6M DESI spectroscopic ob...

### NEW ESS P5 - P5-META-E2
> “Build a survey-footprint mask by dilation of occupied cells … Gaussian-smooth δ in Fourier space … Solve Poisson in k-space … NN-interpolate the per-cell label.” The Gaussian smoothing and Poisson solve are applied on a masked cube with out-of-footp...

### NEW ESS P5 - P5-META-E3
> “For hypothesis tests we run two complementary nulls: (i) a label-shuffle …; (ii) a position-shuffle that preserves labels but scrambles positions.” Only label-shuffle results are presented (e.g., Table V; Fig. 4; §VII “Pre-cell label-shuffle null”)....

### NEW ESS P5 - P5-META-E4
> “the 21,158-row excess … is the population … whose V-Web env-class assignment passes the relaxed env-label confidence used by the cosmic-web pipeline but is excluded from the headline by a stricter env-class-uncertainty filter.” No definition of “env...
