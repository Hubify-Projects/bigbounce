# Row 23 — Cosmic fate under bounce-compatible dark energy

**Lane:** `bb-LS7-row23-fate-de` · **Date:** 2026-09-21/22 · **Layer:** Open Questions
(inherited from `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md`, which asserts no
BigBounce claim; nothing here is a manuscript claim, and nothing here changes a paper,
an SSOT row, or a null).

**Pre-registration:** `PREREGISTRATION.md`, committed before any statistic
(`c8031ce6`). Every number below is produced by `cross_table.py` or
`observable_separation.py` and is read out of their JSON; none is hand-typed.

**The question (ledger row 23).** For the DE classes Branch I finds bounce-compatible,
which admit a future turnaround (ρ_DE reaching and crossing zero), and does any
*present-day* observable distinguish those from ΛCDM at DESI DR2 precision?

---

## Verdict, up front

**PARTIAL / BOUNDARY — the pre-registered third outcome, and it resolves to the
success side: a real but bounded forecast lane exists.**

1. The intersection is **not empty**: three Branch I bounce-compatible classes admit a
   future turnaround.
2. A **>1σ present-day separation from ΛCDM does exist** at published DR2 uncertainties,
   but only for a sub-region of each class's parameter space.
3. The boundary of that sub-region is **sharp in the present-day equation of state and
   blunt in the fate**: across the two quintessence potential families tested, the 1σ
   boundary sits at `w₀ = −0.951` vs `w₀ = −0.934` (spread 0.017) while the corresponding
   turnaround epoch moves by a factor **3.93** (53.8 Gyr vs 13.7 Gyr).

**The scientific content of row 23 is that third point.** DESI DR2 constrains the
*present-day dark-energy equation of state* of these models, not their fate; the map from
the measured quantity to a turnaround epoch is set by the assumed potential family and is
not an observable. A DR2-era bound therefore yields a statement of the form "turnaround
later than *t* Gyr **within this potential family**", which is exactly the form of
Kallosh, Kratochvil, Linde, Linder & Shmakova's `t_c ≳ 10 Gyr` (arXiv:astro-ph/0307185)
and is the honest shape of any future result in this lane.

---

## Step 1 — the cross-table

Set B = Branch I's bounce-compatible classes, quoted, never re-adjudicated
(`02_candidate_DE_classes.md` Classes 1–7; `horndeski_bounce_stability/phase1_results.md`
Phase-1 verdicts A–F). Set T = the row-20 turnaround criterion,
`COSMIC_FATE_MEMO.md` Eqs. (2.3)–(2.5). Six sympy lemmas (L1–L6) do the deciding;
full output in `cross_table.json`.

| Branch I class | Branch I verdict | Turnaround? | Deciding equation |
|---|---|---|---|
| 1 — Λ | trivially compatible | **FAIL** | L1: `E²(a) ≥ Ω_Λ > 0` ∀a (memo Eq. 3.1); and memo Eq. (3.5) — at `Ω_m < 1` no positive Λ recollapses at *any* curvature |
| 2 / A — canonical quintessence | compatible | **PASS** (V crossing zero) | L2: `ρ_tot = 0 ⇒ V = −(ρ_m + φ̇²/2)`, and then `ρ_tot + 3p_tot = 3(ρ_m + φ̇²) > 0` identically (memo Eqs. 3.7–3.8) |
| 3 / B — k-essence `P(X,φ)` | compatible (X→0 canonical limit) | **PASS** (effective V crossing zero) | L3: `ρ = 2XP_X − P = KX + 3LX² + V`; at the crossing `ρ_tot + 3p_tot = 3(ρ_m + 2KX + 4LX²) > 0` while `P_X + 2XP_XX = K + 6LX > 0` keeps the mode healthy |
| 4a — viable f(R) | trivially compatible (Test I-2) | **FAIL** for the viable sub-class | L1 applied to the positive asymptotic effective floor the model needs in order to be dark energy today (memo §3e case 2) |
| 4b / C — cubic braiding | **EFT_INAPPLICABLE** → undetermined | undetermined | not in Set B; Branch I's verdict is not promoted |
| 4c / D — non-minimal `ξRφ²` | compatible with caveat | **UNDETERMINED — GAP-1** | the criterion (2.3) is frame-dependent for `ξ ≠ 0`: `H = 0` in the Jordan frame is not `H̃ = 0` in the Einstein frame, and no frame-invariant criterion is derived here (memo §3g) |
| 4d / E — quartic/quintic Horndeski | trivially compatible (GW170817 forces `G₄=G₄(φ)`, `G₅=0`) | **UNDETERMINED — GAP-1** | same frame-dependence obstruction |
| 4e / F — DHOST | EFT_INAPPLICABLE → undetermined | undetermined | not in Set B |
| 5 — vacuum sequestering | compatible but disconnected | **FAIL** at the observed sign | the residual `Λ_eff` is a constant, so the class inherits row 1 exactly; a turnaround needs `Λ_eff < 0`, contradicting present-day acceleration |
| 6 — interacting dark sector | compatible (weak) | **PASS** (sustained drain) | L5: with `Q/H = −ξ ρ_c0`, `ρ_DE(u) = Ω_DE0 − ξu` reaches zero at `u = Ω_DE0/ξ`; the complementary sub-class (any coupling leaving `ρ_DE,eff > 0` asymptotically) FAILS by L1 (memo §3e) |
| 7 — massive gravity / bigravity | possibly not compatible → undetermined | undetermined | not in Set B |

Also verified symbolically, because it is the most common error in this area:
**L4** reproduces memo Eq. (4.1) and confirms that CPL's
`ρ_DE(a) = ρ₀ a^{−3(1+w₀+w_a)} e^{−3w_a(1−a)}` is a product of strictly positive factors —
no CPL extrapolation ever crosses zero, so no CPL fit implies a Crunch.
**L6** reproduces memo Eq. (3.6): a constant negative `Λ_eff` does turn around, at
`a_t = (Ω_m/|Ω_Λ|)^{1/3}`, but flatness then forces `Ω_m = 1 + |Ω_Λ| > 1`, already excluded.

**Intersection (both sets): 3 classes** — zero-crossing quintessence, zero-crossing
k-essence, interacting dark sector with a sustained drain.

---

## Step 2 — present-day separation from ΛCDM at DR2 precision

**Reference and protocol.** ΛCDM at the DESI DR2 BAO-only values `Ω_m = 0.2975`,
`h·r_d = 101.54 Mpc` (DESI DR2 Results II, arXiv:2503.14738, as quoted in arXiv:2507.01380
Table I under "ΛCDM^DESI"); `r_d = 147.09 Mpc` (Planck DR3 prior, same paper Table IV) ⇒
`h = 0.6903`, `1/H₀ = 14.1642 Gyr`. Radiation `Ω_r h² = 4.15×10⁻⁵` (standard; the run is
repeated with `Ω_r = 0`). Each model is evaluated at the **same** `Ω_m` and `h·r_d` — it
is **not re-fit** — so every separation below is an **upper bound** on what a marginalised
analysis would find. This bias direction is stated with every number.

**Uncertainties.** Per-bin `σ` and correlations are **derived in code** from the DR2
covariance blocks transcribed verbatim from arXiv:2507.01380 §III.B, which reconstructs
them from "the publicly released uncertainties and correlation coefficients" of DESI DR2
Results II (its Table IV). Secondary source, flagged as such. No uncertainty in this lane
is hand-typed, estimated or interpolated. Data vector: `D_V/r_d` at BGS `z=0.295`, plus
`(D_M/r_d, D_H/r_d)` at `z = 0.510, 0.706, 0.934, 1.321, 1.484, 2.330` — 13 points, the
same (`D_M`,`D_H`) basis the DESI likelihood uses to avoid double counting.

**Statistic** (pre-registered): `Δ_i = (O_i^model − O_i^ΛCDM)/σ_i`; the **conservative
per-point `max_i|Δ_i|` decides**, with `Δ_tot` reported both as the pre-registered
independent quadrature and, as an improvement now that the 2×2 blocks are in hand, with
the published per-bin correlation.

### The ruler

A constant-`w` model at the DESI DR2 BAO-only wCDM central value `w = −0.916 ± 0.078`
(arXiv:2507.01380 Table I, "wCDM^DESI") — a `1.08σ` *marginalised* departure from `w=−1` —
gives `max|Δ| = 2.41σ` in this fixed-parameter metric (worst point LRG3+ELG1 `D_M/r_d`).
Conversion factor `κ = 2.24` fixed-parameter σ per marginalised σ. Single-ruler,
one-parameter, order-of-magnitude only — **not** a marginalised likelihood analysis.

### M1 — zero-crossing quintessence, linear potential `V = V₀ + αφ`

Kallosh et al. (arXiv:astro-ph/0307185) model, integrated exactly (no slow-roll
approximation) from `a = 10⁻⁴` with the thawing initial condition `φ' = 0`, shooting on
`V₀` so that `E(z=0) = 1` to machine precision.

| α | w₀ | t_c [Gyr] | a_turn | max\|Δ\| | Δ_tot (block) |
|---|---|---|---|---|---|
| −0.10 | −0.9969 | 601 | 1.6×10¹¹ † | 0.06 | 0.16 |
| −0.20 | −0.9876 | 169 | 1.2×10³ † | 0.26 | 0.62 |
| −0.30 | −0.9722 | 84.7 | 33.6 | 0.57 | 1.39 |
| −0.40 | −0.9508 | 53.7 | 9.22 | 1.00 | 2.45 |
| −0.60 | −0.8907 | 29.7 | 3.42 | 2.19 | 5.35 |
| −0.80 | −0.8091 | 20.1 | 2.30 | 3.74 | 9.14 |
| −1.00 | −0.7079 | 15.0 | 1.87 | 5.56 | 13.63 |

† `a_turn > 10⁶` flags a formal turnaround at an epoch where a *linear* potential — itself
a local expansion of `V` about today's field value — carries no physical content. Reported
for completeness, not as models.

**Boundary:** `max|Δ| = 1σ` at `α* = −0.3995`, `w₀* = −0.9509`, **`t_c* = 53.8 Gyr`**
(`a_turn = 9.26`, a physically sane epoch). Ruler-calibrated ~1σ *marginalised*
equivalent: `w₀ = −0.888`, `t_c ≈ 29 Gyr`.

The worst point is always LRG3+ELG1 `D_M/r_d` (`z = 0.934`, `σ = 0.152`), the tightest
fractional distance in DR2. The sign is a *deficit*: the model's `ρ_DE` was larger in the
past (`ρ̇_φ = −3Hφ̇² ≤ 0`; at `α = −0.4`, `ρ_DE(z=2.33)/ρ_DE,0 = 1.068`), so `E(z)` is
larger and the distances are shorter than ΛCDM's.

### M1b — potential-shape robustness: quadratic top `V = V₀ − m²φ²/2`

| m² | w₀ | t_c [Gyr] | a_turn | max\|Δ\| |
|---|---|---|---|---|
| 1.0 | −0.9947 | 38.5 | 7.36 | 0.10 |
| 1.5 | −0.9848 | 24.9 | 3.58 | 0.26 |
| 2.0 | −0.9656 | 17.9 | 2.48 | 0.55 |
| 3.0 | −0.8804 | 10.7 | 1.70 | 1.71 |

**Boundary:** `m²* = 2.487`, `w₀* = −0.9338`, **`t_c* = 13.7 Gyr`**.

**This is the central result.** Between the two families the 1σ boundary moves by
**0.017 in `w₀`** and by a **factor 3.93 in `t_c`**. What DR2 measures is the present-day
equation of state; the fate epoch is inferred, not measured, and the inference is
family-dependent.

### M2 — interacting dark sector with a sustained drain

Closed form from lemma L5, `Q/H = −ξ ρ_c0`, `w = −1`: `ρ_DE(u) = Ω_DE0 − ξu`,
`ρ_c(u) = (Ω_m − ξ/3)e^{−3u} + ξ/3` (the coupling is taken to act on the whole pressureless
sector; baryons are not separated).

| ξ | w₀,eff | t_c [Gyr] | a_turn | max\|Δ\| | Δ_tot (block) |
|---|---|---|---|---|---|
| 0.02 | −0.9905 | 1192 | 2.5×10¹⁵ † | 0.80 | 1.52 |
| 0.05 | −0.9763 | 479 | 1.8×10⁶ † | 2.04 | 3.85 |
| 0.10 | −0.9525 | 242 | 1.6×10³ | 4.23 | 7.92 |
| 0.20 | −0.9051 | 123 | 46.8 | 9.16 | 16.79 |
| 0.50 | −0.7627 | 52.3 | 5.69 | 30.88 | 52.33 |

**Boundary:** `ξ* = 0.0250`, but at `a_turn ≈ 2×10¹²` — the absurd-epoch flag applies, so
the honest statement is about the *drain rate*, not the fate: DR2 separates a drain of
`ξ ≳ 0.025` at >1σ, and every member whose turnaround occurs at a sane epoch
(`a_turn < 10⁶`, i.e. `ξ ≳ 0.05`) is already separated at **>2σ**. This class is the most
visible of the three because the drained energy reappears in the pressureless sector and
so moves `ρ_m(z)` as well as `ρ_DE(z)`; its worst point is the Lyα `D_H/r_d`.

### M3 — zero-crossing k-essence

At the background level this is M1 with a rescaled kinetic term (lemma L3:
`ρ = KX + 3LX² + V`, `p = KX + LX² − V`), so its BAO separation is M1's. Its *distinctive*
freedom is `c_s² = (K + 2LX)/(K + 6LX)`, which moves **growth**, not background distances —
and growth is **GAP-2**. No separation is claimed for the k-essence-specific direction.

### QC and robustness

`E(z=0) − 1 = 0` exactly for every model (shooting constraint); `ρ_DE` verified
non-decreasing in `z` for both dynamical models, as `ρ̇_φ = −3Hφ̇² ≤ 0` requires.
Re-evaluated at `α*`: using the tighter DR2-IV Lyα errors changes `max|Δ|` by
`6×10⁻¹⁰`; dropping radiation entirely changes it by `5×10⁻⁴`. The decision is
insensitive to both.

---

## Named gaps (never filled with an invented number)

- **GAP-1 — frame-dependence.** Branch I Classes D and E (non-minimally coupled scalars,
  and post-GW170817 quartic/quintic Horndeski, which reduces to them) are squarely inside
  Set B but have **no Set-T verdict**: the turnaround condition `H = 0` is frame-dependent
  for `ξ ≠ 0` and no frame-invariant criterion is derived here. This is the single
  best-defined next piece of theory work in row 23.
- **GAP-2 — growth.** No citable DESI DR2-era `fσ8` measurement with an uncertainty was
  obtained in this lane (disk constraints forbid catalogue downloads and no abstract-level
  value was verified). The growth observable is therefore **not computed**, and the
  k-essence-specific `c_s²` direction is untested. This is the highest-value cheap
  extension: it is the one observable that separates M3 from M1.
- **GAP-3 — central values.** DR2 *central* values were not obtained from a citable source
  in this lane, only uncertainties and correlations. No goodness-of-fit to the data is
  computed anywhere here; every number is a model-vs-ΛCDM separation in units of the
  published σ. The pipeline's ΛCDM predictions at `z = 0.510`
  (`D_M/r_d = 13.256`, `D_H/r_d = 22.466`) are recorded in `observable_separation.json`
  so the pipeline can be checked against published central values later.

---

## What this does and does not say

- It does **not** say the universe will recollapse, or that any bounce-compatible DE model
  is favoured. Nothing here changes the row-20 verdict: under a constant Λ > 0 a Crunch is
  impossible, and current data neither require nor exclude a zero crossing.
- It does **not** promote the memo's evidence layer. This lane's computation earns a
  quantitative boundary, not a claim; row 23 stays on the Open-Questions surface.
- It **does** answer row 23's question with a number: yes, present-day BAO distances
  separate these models from ΛCDM at >1σ, but only above a threshold in `w₀`
  (`≈ −0.95…−0.93`), and the corresponding statement about the *fate* carries a factor-4
  potential-family ambiguity.
- The DESI-preferred `w₀ > −1, w_a < 0` quadrant is qualitatively the direction these
  models occupy, and that is precisely why the lane is worth keeping open — while noting
  (lemma L4, memo Eq. 4.1) that **CPL itself never crosses zero**, so the DESI fit is not
  evidence for a turnaround and must never be quoted as such.

## Recommended next step (one, bounded)

Close **GAP-2**: obtain a citable DR2-era `fσ8` value with its uncertainty and run the
same fixed-parameter separation on growth. That is the only observable that separates the
k-essence member from the canonical one, and it is the direction in which a zero-crossing
DE sector deviates fastest.

## Sources

1. DESI Collaboration, *DESI DR2 Results II: BAO measurements and cosmological
   constraints*, arXiv:2503.14738; Phys. Rev. D **112** (2025). Abstract verified
   2026-09-21 (full text fetched; the per-tracer measurement table was not reachable —
   see GAP-3).
2. arXiv:2507.01380, *Comparing ΛCDM, wCDM, and w₀w_aCDM models with DESI DR2 BAO*,
   §III.B and Tables I, III, IV. **Secondary source**, used for the covariance blocks it
   reconstructs from [1] and for the DESI values it quotes from [1]. Full text read
   2026-09-21.
3. DESI Collaboration, *DESI DR2 Results IV: Alcock–Paczyński from the Lyα forest*,
   arXiv:2607.27410 — via `COSMIC_FATE_MEMO.md` §4.1 (abstract verified 2026-09-18).
4. Planck Collaboration, *Planck 2018 results VI*, arXiv:1807.06209 (background reference).
5. R. Kallosh, J. Kratochvil, A. Linde, E. V. Linder & M. Shmakova, *Observational Bounds
   on Cosmic Doomsday*, arXiv:astro-ph/0307185 (2003) — the linear-potential model.
6. R. Kallosh & A. Linde, *Dark Energy and the Fate of the Universe*,
   arXiv:astro-ph/0301087; JCAP **0302**:002 (2003).
7. In-repo: `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` (Eqs. 2.3–2.5, 3.1,
   3.5–3.8, 4.1; §3e, §3g, §10) and `research/branch_I_bounce_compatible_DE/*`.
