# Row 23 GAP-2 — the growth observable

**Lane:** `bb-LS8-row23-growth` · **Date:** 2026-09-22 · **Layer:** Open Questions
(inherited unchanged from `../ROW23_MEMO.md`, which inherits it from
`research/archaeology_2025/memos/COSMIC_FATE_MEMO.md`). Nothing here is a BigBounce
claim; no paper, SSOT row, or null is changed by this lane.

**Pre-registration:** `PREREGISTRATION_GAP2.md`, committed alone before any statistic
(`908d87f7`). Every number below is produced by `growth_separation.py` and read out of
`growth_separation.json`; none is hand-typed.

**The gap:** `../ROW23_MEMO.md` GAP-2 — *"no citable DESI DR2-era `fσ8` … the growth
observable is therefore not computed, and the k-essence-specific `c_s²` direction is
untested. This is the highest-value cheap extension: it is the one observable that
separates M3 from M1."*

---

## Verdict, up front

**GAP-2 is closed, and it closes as a NULL — the pre-registered "not separable"
branch.** Growth does not separate the k-essence member from the canonical one, and it
does not strengthen LS7's boundary either.

1. **No citable DESI DR2-era growth measurement exists.** Not "not found" — *does not
   exist*: the one DR2 full-shape analysis that reports a growth rate withdrew it. The
   pre-registered fallback to **DESI DR1 full-shape** is taken and labelled throughout.
2. **M3 is NOT distinguishable from M1.** Over the *entire* `c_s²` range the model
   permits — a range **derived**, not assumed — and over `k ∈ [0.01, 0.2] h/Mpc`, the
   largest separation is **`max|Δ| = 0.0043σ`**. The published precision would have to
   shrink by a factor **233** to reach 1σ.
3. **The null is structural, not a parameter accident.** Across a factor ~20 in
   background strength the maximal `c_s²` signature stays a fixed **3.83 % ± 0.09 %** of
   the model's own background growth signature. There is no corner of the family where
   growth separates M3 from M1.
4. **Growth adds nothing to LS7's boundary.** At LS7's 1σ BAO boundary
   (`α* = −0.3995`, `w₀ = −0.951`) the growth separation is **0.113σ** against BAO's
   1.00σ. Growth alone would need `w₀ = −0.500` (M1) or `ξ = 0.153` (M2) — both already
   separated by BAO at many σ.

**Net effect on row 23:** the LS7 boundary stands exactly as published. Row 23's
deliverable is still the `w₀` threshold with its factor-3.93 fate ambiguity; this lane
removes the caveat that a missing observable might have changed it. It does not.

---

## Step 1 — the citation, and the honest failure to find a DR2 one

Searched 2026-09-22. Recorded in `PREREGISTRATION_GAP2.md` §1 **before** computing:

| Candidate | Outcome |
|---|---|
| DESI DR2 Results II, arXiv:2503.14738 | **BAO-only.** No growth measurement. |
| arXiv:2602.18761, *joint DESI DR1 Full-Shape and DR2 BAO* (2026-02) | DR2-era, but its growth information is **DR1** full-shape and it reports `σ8`, not `fσ8(z)`. |
| DESI DR2 Lyα forest full-shape, arXiv:2607.27411 | Abstract, verbatim: *"mock studies reveal a significant bias in the inferred growth-rate parameter fσ8, leading us to exclude this measurement from the final analysis."* **DESI withdrew it. It is not used, and no substitute is invented.** |
| DR2 full-shape talk, PIRSA 26040071 (2026-04-29) | A talk is not a citable measurement with an uncertainty. Not used. |

**Conclusion, stated plainly:** as of 2026-09-22 there is **no** citable DESI DR2-era
`fσ8` with an uncertainty. The pre-registered fallback is taken.

### The source actually used

**DESI Collaboration, *DESI 2024 V: Full-Shape Galaxy Clustering from Galaxies and
Quasars*, arXiv:2411.12021, JCAP 09 (2025) 008.** PDF v5 fetched and read 2026-09-22.

Per-bin uncertainties are **derived in code** as `sqrt(C[2][2])` from the published 4×4
ShapeFit Gaussian covariances, Appendix A Eqs. (A.1)–(A.12) (ShapeFit-alone), divided by
the Table-11 fiducial `(fσs8)_fid`. No uncertainty is hand-typed, estimated or
interpolated.

| tracer | z_eff | `fσs8` datavector | σ (derived) | `(fσs8)_fid` | ε = σ/fid |
|---|---|---|---|---|---|
| BGS | 0.295 | 0.377174 | 0.09408 | 0.4723 | **19.92 %** |
| LRG1 | 0.510 | 0.513635 | 0.06426 | 0.4733 | **13.58 %** |
| LRG2 | 0.706 | 0.483623 | 0.05303 | 0.4608 | **11.51 %** |
| LRG3 | 0.919 | 0.422164 | 0.04730 | 0.4398 | **10.75 %** |
| ELG2 | 1.317 | 0.376715 | 0.03741 | 0.3944 | **9.49 %** |
| QSO | 1.491 | 0.434858 | 0.04448 | 0.3750 | **11.86 %** |

Combined: the abstract's *"combined precision of 4.7 % on the amplitude of the redshift
space distortion (RSD) signal"*.

**Baseline is ShapeFit-alone, not ShapeFit+BAO** — row 23 Step 2 already uses DESI DR2
BAO distances, so the +BAO rows would double count. The +BAO variant is carried as a
sensitivity.

**DESI's own restriction is honoured.** §7.1 of the same paper states the derived `fσ8`
values *"should only serve for visualization purposes, and they should never be used to
infer cosmology, for which one should use the actual fσs8 results."* Accordingly **no
measured central value enters any decision here**: only the published *precision* is
used, as the yardstick for a model-vs-model forecast separation. No goodness-of-fit is
computed anywhere (GAP-3 discipline unchanged).

---

## Step 2 — what was computed

Backgrounds are **imported unchanged** from `../observable_separation.py`, so the
fixed-parameter convention (`Ω_m = 0.2975`, `h·r_d = 101.54 Mpc`, no re-fit) is literally
the same code. All models share the primordial amplitude and transfer function, so
`σ8(z)/σ8^ΛCDM(z) = δ(z)/δ^ΛCDM(z)`; every result is a **ratio** and no absolute `σ8` is
used or quoted.

### Lemma G1 — the `c_s²` range is derived, not assumed

From `P = KX + LX² − V` (`cross_table.py` lemma L3), with `s ≡ LX`:

```
rho = K X + 3 L X^2 + V      p = K X + L X^2 - V
no ghost:               P_X + 2 X P_XX = K + 6 L X > 0
non-phantom / no gradient instability:  rho + p = 2X(K + 2LX) >= 0  =>  K + 2s >= 0
subluminality:          1 - c_s^2 = 4s/(K + 6s) >= 0  =>  L >= 0
c_s^2 = (K + 2s)/(K + 6s)
```

Sympy evaluates the endpoints: `c_s² = 0` exactly at `K = −2s`, `c_s² → 1` as `K → ∞`,
`c_s² = 1/3` at `K = 0`. So **the family sweeps the full interval `[0, 1)`**, and
`c_s² = 1` holds **iff `L = 0`, which is exactly M1**. M1 is the `c_s² → 1` endpoint of
M3 — which is why the comparison below is the whole question.

### Lemma G2 — the coupled growth equation is derived, with its assumptions named

For the covariant choice `Q^μ = Q u_c^μ` (energy transfer along the CDM four-velocity ⇒
no momentum transfer in the CDM frame ⇒ **CDM Euler unmodified**; Valiviita, Majerotto &
Maartens, arXiv:0804.0232; Amendola, PRD 62 043511), smooth DE with `w = −1`, `δQ`
neglected at sub-horizon order, whole pressureless sector coupled (LS7's background
convention), sympy returns

```
D^2 delta + (2 + dlnE/dN + gamma) D delta
          + [ (2 + dlnE/dN) gamma + D gamma - (3/2) Omega_m(a) ] delta = 0
gamma(N) = Q/(H rho_c) = xi / rho_c(N)        D gamma = 3 gamma - gamma^2
```

which reduces to the standard equation at `γ = 0`.

**A methodological trap, found and avoided.** RSD measures the *velocity divergence*, not
`dlnδ/dlna`. From `Dδ = −Θ − γδ`, the observed rate is `f_RSD = dlnδ/dlna + γ`. The
friction term `γ` suppresses `dlnδ/dlna` below ΛCDM, and adding `γ` back moves the
*observed* rate partly **towards** ΛCDM. Scoring M2 with `dlnδ/dlna` therefore
**overstates** its separation — measured here as **0.409σ instead of the correct 0.154σ
at `ξ = 0.025`, a factor 2.65**. Both are reported per `ξ` in the JSON.

### M3's clustering DE

Matter plus a DE fluid of rest-frame sound speed `c_s²`, sub-horizon Newtonian gauge,
evolved in `V_d ≡ (1+w)θ_d/ℋ` so the thawing field's `1/(1+w)` singularity is removed,
with adiabatic ICs at `a = 0.1`. M3's background **is** M1's (lemma L3), so BAO distances
are identical by construction and `c_s²` is the only difference.

---

## Step 3 — results

### PRIMARY — does `c_s²` separate M3 from M1? **No.**

Separation of M3 from M1 at identical backgrounds, `α* = −0.3995` (LS7's 1σ BAO
boundary), in units of the published DR1 precision:

| `c_s²` | k = 0.01 | k = 0.03 | k = 0.10 | k = 0.20 |
|---|---|---|---|---|
| 0 | **0.0043** | 0.0043 | 0.0043 | 0.0043 |
| 10⁻⁴ | 0.0043 | 0.0040 | 0.0020 | 0.0006 |
| 10⁻³ | 0.0039 | 0.0021 | 0.0002 | 0.0001 |
| 10⁻² | 0.0020 | 0.0003 | 0.0000 | 0.0000 |
| 1/3 | 0.0001 | 0.0000 | 0.0000 | 0.0000 |
| 0.99 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

**Maximum over the entire derived range: `max|Δ| = 0.00430σ`** (`c_s² = 0`; `k`-independent
there, as it must be, since `κ²c_s²` vanishes). Combined-precision figure: 0.006. The
separation is **monotone decreasing in `c_s²` at every `k`** (checked, not assumed), so
the pre-registered bracketing argument applies: **the `c_s² = 0` endpoint bounds every
`c_s²(a)` trajectory inside `[0,1)`, including time-dependent ones.**

**The published precision would have to shrink by a factor 233** for the maximal
k-essence signature to reach 1σ. That is a statement about this calculation against this
published precision — not a forecast for any future DESI release.

### The null is structural

At `c_s² = 0` (maximal clustering), across the family:

| α | w₀ | 1+w₀ | max\|Δ\| M3 vs M1 | max\|Δ\| M1 vs ΛCDM | ratio |
|---|---|---|---|---|---|
| −0.2000 | −0.9876 | 0.0124 | 0.0011 | 0.0289 | 0.0379 |
| −0.3995 | −0.9509 | 0.0491 | 0.0043 | 0.1131 | 0.0380 |
| −0.6000 | −0.8907 | 0.1093 | 0.0094 | 0.2466 | 0.0382 |
| −0.8000 | −0.8091 | 0.1909 | 0.0161 | 0.4195 | 0.0385 |
| −1.0000 | −0.7079 | 0.2921 | 0.0241 | 0.6217 | 0.0388 |

Across a factor ~20 in background strength the maximal `c_s²` signature holds at
**3.83 % ± 0.09 %** of the background signature. **This is the real content of GAP-2:**
the k-essence sound-speed freedom is not merely small at one parameter point — it is
*structurally* subdominant to the background effect everywhere, and the background effect
is itself subdominant to BAO. There is no corner of the family where growth separates M3
from M1 while BAO has not already separated the background from ΛCDM far more strongly.

### SECONDARY — does growth strengthen LS7's boundary? **No.**

| α | w₀ | t_c [Gyr] | growth max\|Δ\| | BAO max\|Δ\| (LS7) |
|---|---|---|---|---|
| −0.2000 | −0.9876 | 168.6 | 0.029 | 0.26 |
| −0.3000 | −0.9722 | 84.7 | 0.065 | 0.57 |
| **−0.3995** | **−0.9509** | **53.8** | **0.113** | **1.00** |
| −0.6000 | −0.8907 | 29.7 | 0.247 | 2.19 |
| −0.8000 | −0.8091 | 20.1 | 0.420 | 3.74 |
| −1.0000 | −0.7079 | 15.0 | 0.622 | 5.56 |

Growth is a near-uniform **~8.8×** weaker probe than BAO for M1. Growth alone reaches 1σ
only at `α = −1.335`, `w₀ = −0.500`, `t_c = 10.4 Gyr` — deep inside territory BAO already
excludes at many σ.

M2, interacting dark sector (RSD rate, lemma G2):

| ξ | γ(today) | growth max\|Δ\| | BAO max\|Δ\| (LS7) | (wrong) `dlnδ/dlna` |
|---|---|---|---|---|
| 0.010 | 0.0336 | 0.061 | — | 0.164 |
| **0.025** | 0.0840 | **0.154** | **1.00** | 0.409 |
| 0.050 | 0.1681 | 0.312 | 2.04 | 0.815 |
| 0.100 | 0.3361 | 0.638 | 4.23 | 1.620 |
| 0.200 | 0.6723 | 1.341 | 9.16 | 3.259 |

Growth-only 1σ at `ξ = 0.1527` versus LS7's BAO `ξ* = 0.0250` — again ~6× weaker.

---

## QC

| Check | Result | Verdict |
|---|---|---|
| ΛCDM `f(z)` vs the `Ω_m(z)^0.55` fitting formula | max \|frac diff\| 0.6 % (z=0), ≤0.06 % elsewhere | PASS — the formula is itself ~1 % accurate |
| Two-fluid solver reduces to the single-fluid smooth-DE result at `c_s² = 1` | residuals 6×10⁻⁹ … 6×10⁻⁸ | PASS — independent code path agrees |
| σ derived from the Appendix-A covariance vs the paper's own Table-9 errors | ratios 0.996, 0.970, 0.959, 0.978, 0.862, 0.988 | PASS — transcription confirmed; Table 9 quotes asymmetric MAP intervals, so exact equality is not expected |
| Initial-redshift insensitivity of the ratio (`a_i` = 3×10⁻³, 10⁻³, 3×10⁻⁴) | 0.01523997 / 0.01523997 / 0.01523997 | PASS — stable to 9 digits, as it must be since M1/M3 share `ρ_m(a)`, `ρ_r(a)` with ΛCDM |
| LS7 background checks re-run here (`E(z=0) − 1`, `ρ_DE` monotone in z) | unchanged from LS7 | PASS |
| `ε` ±10 % | M1 at boundary 0.103 … 0.126 (vs 0.113) | decision unchanged |
| ShapeFit+BAO variant instead of ShapeFit-alone | M1 0.125; M3-vs-M1 best 0.0045 | decision unchanged |
| `k` ∈ [0.01, 0.2] h/Mpc | maximum at `c_s²=0`, `k`-independent | decision unchanged |

**Direction of every residual bias, stated:** the derived σ run ~2–14 % *smaller* than the
larger Table-9 error, which makes Δ *larger* and the null therefore **conservative**. The
fixed-parameter protocol likewise makes every separation an **upper bound** on a
marginalised one — again conservative for a null.

---

## How the DR1 fallback weakens this (as pre-registered in §5, answered)

1. **The yardstick is DR1, not DR2.** The correct phrasing of the null is "not separable
   **at DESI DR1 full-shape precision**", never "not separable at DESI precision". This
   caveat is real but it is not close to load-bearing: the M3-vs-M1 result misses 1σ by a
   factor **233**, and no plausible single-survey improvement is a factor of 233.
2. **M2's transfer function is not modelled.** The coupling changes `ρ_c` at early times
   (`(Ω_m − ξ/3)a⁻³`), hence matter–radiation equality, which needs a Boltzmann code.
   M2's growth numbers are approximate and labelled. **M1 and M3 are unaffected** — their
   `ρ_m(a)` and `ρ_r(a)` are identical to ΛCDM's — so the primary result does not inherit
   this.
3. **Template mismatch.** `ε` is a precision relative to the ShapeFit Planck template
   while the ratio is relative to the DR2-BAO ΛCDM reference; the two differ by a few
   percent in `fσ8`. Covered by the ±10 % `ε` sensitivity; decision unchanged.
4. **Scale dependence.** ShapeFit's `fσs8` is a broad-band amplitude assuming
   scale-independent growth, while clustering DE is mildly `k`-dependent. The maximum
   over `k` is quoted and it occurs at `c_s² = 0`, where the effect is exactly
   `k`-independent — so this caveat does not affect the bound.

## What this does and does not say

- It does **not** say k-essence and quintessence are the same theory. They differ in
  `c_s²`, and that difference is physical; it is **unmeasurable at this precision in this
  observable**, which is a statement about the data, not about the models.
- It does **not** change the row-20 verdict, the row-23 boundary, or any BigBounce claim.
  Row 23 stays an Open Question at the inherited evidence layer.
- It **does** answer GAP-2's question with a number and closes it: **no**, growth does
  not separate M3 from M1 (`0.0043σ`, 233× short), and **no**, growth does not tighten
  LS7's boundary (`0.113σ` vs `1.00σ`). The one observable that could have distinguished
  the k-essence member cannot, so M3 and M1 remain observationally degenerate and row 23's
  deliverable is unchanged.
- **The null is published as a null.** It is not softened, and the honest consequence is
  recorded: the `c_s²` direction is not a viable near-term discovery lane, so the lane's
  remaining value is concentrated in GAP-1.

## Still open

- **GAP-1 (unchanged, and now the best step in row 23).** The turnaround criterion is
  frame-dependent for non-minimally coupled scalars, so Branch I classes D and E have no
  Set-T verdict. With GAP-2 closed as a null, this is the only remaining piece of row-23
  work with a real chance of changing the row's content.
- **GAP-3 (unchanged).** No citable DR2 central values, so no goodness-of-fit is computed
  anywhere in row 23 — here either.
- A DESI DR2 galaxy full-shape release would replace the DR1 yardstick. Given the factor
  233, it would not change the M3-vs-M1 verdict; it would refine the M1/M2 numbers.

## Sources

1. DESI Collaboration, *DESI 2024 V: Full-Shape Galaxy Clustering from Galaxies and
   Quasars*, arXiv:2411.12021; JCAP **09** (2025) 008. **The growth source.** Table 1
   (`z_eff`), Table 6 row 1 (template cosmology), Table 9 (published ratio errors,
   cross-check), Table 11 (fiducial `fσs8`), Appendix A Eqs. (A.1)–(A.24) (datavectors +
   covariances), §7.1 (the `fσ8` restriction), abstract (4.7 %). PDF v5 read 2026-09-22.
2. DESI Collaboration, *DESI DR2 Results IV: Lyα forest full-shape validation*,
   arXiv:2607.27411 — abstract verified 2026-09-22; source of the withdrawn-`fσ8`
   statement.
3. arXiv:2602.18761, *Cosmological constraints from a joint DESI DR1 Full-Shape and DR2
   BAO* — abstract verified 2026-09-22; confirms DR2-era growth still comes from DR1.
4. DESI Collaboration, *DESI DR2 Results II*, arXiv:2503.14738 — BAO-only (via
   `../ROW23_MEMO.md`).
5. J. Valiviita, E. Majerotto & R. Maartens, *Instability in interacting dark energy and
   dark matter fluids*, arXiv:0804.0232 — the `Q^μ ∥ u_c^μ` perturbation setup.
6. L. Amendola, *Coupled quintessence*, Phys. Rev. D **62** (2000) 043511.
7. In-repo: `../ROW23_MEMO.md`, `../PREREGISTRATION.md`, `../cross_table.py` (lemmas
   L3, L5), `../observable_separation.py` (backgrounds, imported unchanged),
   `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` (row 20).
