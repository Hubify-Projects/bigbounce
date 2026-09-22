# LS12 — the pointwise perturbativity diagnostic on the PBH headline grid

**Lane** `LS12-pbh-perturbativity` · **Date** 2026-09-22 · **Item** `DA3M-R12-06` [ESSENTIAL, PARTIAL]
**Pre-registration** `PREREGISTRATION.md`, committed alone at `b289aa0f` **before** any number below existed.
**Outcome: (b) — the headline moves. Pre-registered branch b2: RE-SCOPE, CENTRAL VALUE CHANGES.**

---

## 1. What was open

A3M's Channel II headline is the required-amplitude ratio

> `A(-35/16)/A(-35/8) = 1.84 [1.76, 1.89], std = 0.03, n = 144`  (Eq. `eq:pbh_ratio`, and the abstract)

measured over the 144 scan points whose `gamma_cr` falls in `[0.267, 0.630]`, the interval this model's own
near-scale-invariant spectrum occupies. R12's referee observed that this entire window lies **below** the
`gamma_cr <~ 0.8` region Table V's own caption calls the *non-perturbative branch*, and that the paper's
only quoted perturbativity numbers (`1.2|f_NL|sigma_r ~ 0.54-1.01` and `~1.09-2.02`) are attributed to the
27-point grid at `gamma_cr in [0.766, 0.968]` — a different population. R12 closed this by **disclosure
only**: the paper says the diagnostic "has not been separately evaluated point-by-point on the headline
144-point in-coverage set" and leaves it "for future work". This lane ran it.

## 2. What was computed

For each of the 255 committed scan points (`row11_pbh_residuals/results/row11_gammacr_extension.json`),
the compaction script's own variance integral — Choudhury et al. 2025 Eq. (53) as implemented in
`pbh_compaction_fnl.covariances`, on the wide-k grid the 255 points themselves used — was **re-run at that
point's own spectrum shape and at that point's own stored required amplitude**, giving

```
eps(f_NL) = 1.2 |f_NL| sigma_r ,   sigma_r^2 = Int dk/k W_s^2(k r_p) T^2(k,r_p) Delta^2_zeta(k; A(f_NL))
```

at **both** legs of the ratio: `f_NL = -35/16` at `A = A_-35/16`, and `f_NL = -35/8` at `A = A_-35/8`.
No value was scaled, interpolated or estimated from an adjacent point. `pbh_perturbativity.py`, 1.9 s,
local CPU, $0.

**Validation gates (all five PASS, three of them to exact machine zero):**

| gate | check | result |
|---|---|---|
| G1 | wide-k integrator vs the committed narrow one, lognormal family | max rel. diff `5.7e-16` |
| G2 | recomputed `gamma_cr` vs stored, **all 255 points** | max rel. diff `0.0` (exact) |
| G3 | recomputed `sigma_r` + `1.2 f_NL sigma_r` vs the three committed calibration rows | max rel. diff `0.0` (exact) |
| G4 | recomputed `gamma_cr` vs the committed 27-point grid, narrow integrator | max rel. diff `0.0` (exact) |
| G5 | headline population reproduced from the JSON: `n=144`, `1.83741 ± 0.03117`, `[1.7594, 1.8915]` | exact |

G3 in particular reproduces the paper's own printed `0.5434 / 0.7389 / 1.0112` and
`1.0867 / 1.4777 / 2.0225` bit-for-bit, so the integrator used below is demonstrably the paper's.

## 3. Result

**The diagnostic over the 144-point headline window** (`eps` at each point's own required amplitude):

| leg | min | median | max |
|---|---|---|---|
| `-35/16` | 0.543 | 0.703 | **1.048** |
| `-35/8`  | 0.817 | 1.035 | **1.534** |

**Perturbative by the paper's own criterion (`eps <= 1` at BOTH legs): 62 of 144.**
The `-35/8` leg fails at **82** points; the `-35/16` leg fails at 1.

| population | n | ratio | std | range |
|---|---|---|---|---|
| H — full headline window (what the paper prints) | 144 | **1.8374** | 0.0312 | [1.7594, 1.8915] |
| P — perturbative at both legs | **62** | **1.8121** | 0.0241 | [1.7594, 1.8511] |
| H \ P — non-perturbative | 82 | 1.8565 | 0.0205 | [1.7972, 1.8915] |

`P` passes the pre-registered diversity test (both spectrum families — 34 lognormal, 28 power-law —
18 distinct shapes, 5 values of `r_p k_p`, 2 values of `C_th`), so branch **b1 does not fire**. Branch
**b2 fires**: `mean(P) = 1.8121` rounds to **1.81**, not 1.84. Stated with equal prominence: the shift,
`0.0253`, is **within** the quoted std `0.0312`, so the headline is not overturned — but the printed
three-significant-figure value changes, and so does the abstract's. The range statement survives
(`[1.7594, 1.8511]` sits inside the printed `[1.76, 1.89]`); the std tightens `0.031 -> 0.024`.

### 3.1 What actually separates perturbative from non-perturbative — and it is not `gamma_cr`

`P` and `H \ P` span the **identical** `gamma_cr` range, `[0.2679, 0.6298]`. Inside the headline window
`gamma_cr` does not discriminate at all. What discriminates is the **formation threshold `C_th`**:

| `C_th` | perturbative | non-perturbative |
|---|---|---|
| 0.4 | 47 | 1 |
| 0.5 | 15 | 33 |
| 0.6 | 0 | 48 |

Higher `C_th` needs a higher curvature amplitude, hence larger `sigma_r`, hence larger `eps`. **Every
`C_th = 0.6` point of the headline window is non-perturbative; almost every `C_th = 0.4` point is not.**

### 3.2 The caption's `gamma_cr <~ 0.8` "non-perturbative branch" label is inverted, pointwise

Over the full 255-point scan `eps` **rises** with `gamma_cr` (Pearson `+0.32`, OLS slope `+0.33` per unit
`gamma_cr`). Evaluated at their own required amplitudes, the two windows compare as:

| window | `eps(-35/16)` | `eps(-35/8)` |
|---|---|---|
| headline `gamma_cr in [0.267, 0.630]`, n=144 | [0.543, **1.048**] | [0.817, **1.534**] |
| 27-point grid window `[0.766, 0.968]`, n=42 | [0.635, **2.220**] | [0.965, **3.217**] |

So the headline window is, pointwise, the **more** perturbative of the two — the opposite of what Table V's
caption implies by attaching "non-perturbative branch" to the `gamma_cr <~ 0.8` rows. That caption label is
tied to `f_PBH > 1` uncapped, which is an amplitude-calibration statement, not this diagnostic. **The
referee's premise that the headline sits in a worse regime than the 27-point grid is, measured pointwise,
false; the underlying concern — that the headline population is not perturbatively controlled — is
nevertheless confirmed, on 82 of its 144 points.**

### 3.3 The ratio is not independent of the control parameter — the material weakness

Inside the headline window the ratio and the diagnostic are strongly correlated: Pearson `rho = +0.829`,
OLS slope `+0.161` per unit `eps`. The subset mean therefore **slides monotonically with wherever the cut
is placed**, and no point of the headline population is comfortably perturbative (`eps <= 0.5`: **0 of
144**; `eps <= 1.5`: 143 of 144):

| cut `max(eps) <=` | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.6 |
|---|---|---|---|---|---|---|---|---|
| n | 0 | 33 | **62** | 84 | 114 | 132 | 143 | 144 |
| mean ratio | — | 1.798 | **1.812** | 1.819 | 1.828 | 1.833 | 1.837 | 1.837 |

This is the honest characterisation: **the whole headline population is marginal, `eps ~ O(1)` everywhere,
and the "robust observable" moves with the parameter that measures its own lack of control.** The 1.81
figure is the value at the paper's own threshold, not a cut-independent number.

### 3.4 A separate, smaller accuracy finding

The paper attributes `1.2|f_NL|sigma_r ~ 0.54-1.01` and `~1.09-2.02` to "the displayed 27-point grid".
G3 shows those six numbers are reproduced **exactly** from the three
`calibrated_amplitude_comparison` rows of `outputs/pbh_compaction_fnl.json` — one single shape
`(Delta, r_p k_p) = (0.5, 1.0)` at `C_th = 0.4/0.5/0.6`, evaluated at the **Gaussian-calibrated** `A_*`
where `f_PBH(f_NL=0) = 1`, which is not the amplitude the ratio is defined at. The 27-point window's
diagnostic at its own ratio amplitudes is `[0.635, 2.220]` and `[0.965, 3.217]`. The attribution is
inaccurate and understates the range.

## 4. Effect on the headline, stated plainly

* The headline **is not withdrawn**. `A(-35/16)/A(-35/8)` remains a real, computed, shape-robust property
  of the compaction criterion, and the perturbative subset is large (62) and diverse.
* The headline **is re-scoped**. Restricted to the points that satisfy the paper's own perturbativity
  criterion at both legs, it is **`1.81 [1.76, 1.85]`, std `0.02`, n = 62**, not `1.84 [1.76, 1.89]`,
  std `0.03`, n = 144.
* The disclosure paragraph ("this diagnostic has not been separately evaluated point-by-point … left for
  future work") is now **false** and must be replaced by the computation.
* The paper must state that `eps <= 1` fails at 82 of the 144 points (all of `C_th = 0.6`), that no point
  reaches `eps <= 0.5`, and that the ratio correlates with `eps` at `rho = +0.83` so the subset value is
  threshold-dependent. Reporting `1.81 ± 0.02` without that correlation would be a different kind of
  dishonesty from the one this item was raised about.
* The PBH channel's standing scientific conclusion is **untouched**: the in-lab spectrum is 7.0 dex short
  of the required amplitude and the channel is a NULL (ledger row 11 / A3-1b). Nothing here changes that.

## 5. Limits of this lane

1. `eps <= 1` is a **necessary control diagnostic** for the quadratic local map, not a proof that the
   truncated expansion converges. A point that passes is reported as "passes the paper's own criterion".
2. The lane re-ran only the variance integral. Every `A(f_PBH = 1e-3)` is read from the committed JSON,
   unchanged; no compaction solve was repeated.
3. The correlation in §3.3 means the perturbative-subset statistic is a **conditional** number. A
   genuinely cut-independent Channel II observable would need either a resummed (non-quadratic) NG map —
   already named open item A3-1c — or a restriction to a `C_th` at which the whole window is controlled
   (`C_th = 0.4` gives 47 of 48 perturbative, ratio worth quoting separately if the paper wants a clean
   statement).
4. `sigma_r` is evaluated with the same IR-cutoff-dependent power-law family the scan uses; the
   IR-divergence of the `O(eps^2)` saddle term identified in row 11(a) is a separate, already-recorded
   issue and is not re-opened here.
