# R5-18 — γ_cr coverage of the 27-point PBH grid, and the standing of the 1.7–1.9 ratio

**Audit item:** `DA3M-R5-18` (A3M v3M.0.11 R5 truth audit, closure plan §(ii)-lite).
**Script:** `research/track_a3_multichannel/r5_18_gammacr_coverage.py`
**Output:** `outputs/r5_18_gammacr_coverage.json`
**Manifest:** `reproducibility/manifests/experiments/a3-r5-18-gammacr-coverage.json`
**Venue:** local CPU, seconds, $0. No re-derivation: this is a re-reading of two
committed result JSONs (`pbh_compaction_fnl.json`, `inlab_delta2_zeta_2026-09-03.json`).

## Question

Two things the paper does not report: (a) whether any of the 27 `(Δ, r_p k_p, C_th)`
grid points fall at `γ_cr ≲ 0.85` — the scale at which `pbh_compaction_fnl.py`'s own
step (4) finds the **sign** of the non-Gaussian effect flips (enhancement below,
suppression above); and (b) whether the quoted required-amplitude ratio
`A(−35/16)/A(−35/8) = 1.7–1.9` is *inside* the γ_cr range actually scanned.

`γ_cr = σ_cr²/(σ_c σ_r)` [Choudhury *et al.* 2025, arXiv:2409.18983, Eq. 50] is a
function of the spectrum **shape** `(Δ, r_p k_p)` only — it does not depend on `C_th`.

## γ_cr per grid point (27 points, 9 distinct γ_cr)

| Δ | `r_p k_p` | γ_cr | ratio at `C_th` = 0.4 / 0.5 / 0.6 |
|---|---|---|---|
| 0.8  | 0.75 | **0.7660** | 1.7324 / 1.7736 / 1.8086 |
| 0.8  | 1.0  | **0.8078** | 1.7079 / 1.7533 / 1.7918 |
| 0.5  | 0.75 | **0.8461** | 1.7230 / 1.7661 / 1.8026 |
| 0.8  | 1.5  | 0.8567 | 1.6765 / 1.7275 / 1.7705 |
| 0.5  | 1.0  | 0.8877 | 1.6835 / 1.7335 / 1.7756 |
| 0.35 | 0.75 | 0.8965 | 1.7232 / 1.7665 / 1.8031 |
| 0.35 | 1.0  | 0.9295 | 1.6714 / 1.7237 / 1.7677 |
| 0.5  | 1.5  | 0.9340 | 1.6354 / 1.6941 / 1.7433 |
| 0.35 | 1.5  | 0.9675 | 1.6097 / 1.6734 / 1.7265 |

**Covered range:** `γ_cr ∈ [0.766, 0.968]`. Ratio range over the grid:
`[1.610, 1.809]` (mean `1.732 ± 0.050`, n = 27).

**Enhancement branch:** **9 of 27** points (the three bold γ_cr rows) sit at
`γ_cr ≤ 0.85`. The grid **straddles** the sign-flip scale rather than sitting
entirely on the suppression side — so the `f_PBH(−35/16) < f_PBH(−35/8)` ordering
reported at *every* grid point is not an artefact of scanning only one branch.

## Is the quoted 1.7–1.9 inside the scanned coverage?

**No — not for this lab's own spectrum shape.** The in-lab near-scale-invariant
spectrum gives, over its IR-cutoff scan `k_min/k_p ∈ {10⁻⁵, 10⁻³, 10⁻², 10⁻¹}`,

    γ_cr = 0.2668, 0.3581, 0.4458, 0.6298   →  γ_cr ∈ [0.267, 0.630],

**entirely below** the scanned `[0.766, 0.968]`. At that shape the ratio is
**1.85–1.89** (A3-1b note), outside the grid's own `[1.610, 1.809]`.

So the quoted `1.7–1.9` is the **union** of (i) the 27-point scan, `1.732 ± 0.050`,
range `[1.610, 1.809]`, over `γ_cr ∈ [0.766, 0.968]`, and (ii) a **single**
out-of-coverage evaluation at the in-lab shape, `1.85–1.89`, at
`γ_cr ∈ [0.267, 0.630]`. It is honest as a combined range and it is *stable* at the
~10% level across a γ_cr range more than twice as wide as the grid's — but it is
**not** a scan result over that whole range, and the narrower `1.732 ± 0.050` must
not be quoted as if it were universal.

## Statement the paper may make (at evidential strength)

> The 27-point `(Δ, r_p k_p, C_th)` grid carries nine distinct `γ_cr` values spanning
> `[0.766, 0.968]`, of which nine points lie at `γ_cr ≤ 0.85` — the grid straddles the
> sign-flip scale, so the reversed ordering is not a one-branch artefact. The ratio
> over that grid is `1.732 ± 0.050` (range `[1.610, 1.809]`); this lab's own
> near-scale-invariant shape sits at `γ_cr ∈ [0.27, 0.63]`, *outside* the scanned
> coverage, and gives `1.85–1.89`. The quoted `1.7–1.9` is accordingly the union of a
> scan and one out-of-coverage evaluation — stable at the ~10% level over a much wider
> `γ_cr` range than was scanned, but not itself a scan result over that range, and
> conditional throughout on the unresolved Choudhury *et al.* sign disagreement.
