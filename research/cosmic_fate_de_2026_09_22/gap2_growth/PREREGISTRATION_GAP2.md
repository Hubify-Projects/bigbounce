# Row 23 GAP-2 — Pre-registration (growth / fσ8)

**Lane:** `bb-LS8-row23-growth` (campaign 2026-09-18 publication push)
**Written:** 2026-09-22, committed BEFORE any statistic is computed.
**Parent:** `research/cosmic_fate_de_2026_09_22/` (lane `bb-LS7-row23-fate-de`,
`PREREGISTRATION.md`, `ROW23_MEMO.md`). This file extends that pre-registration; every
rule there that is not restated here still binds (never-invent, nulls stay nulls, no
paper/SSOT/site edits, Convex mutations queued not sent).

**The gap being closed** — `ROW23_MEMO.md` GAP-2, verbatim:

> No citable DESI DR2-era `fσ8` measurement with an uncertainty was obtained in this lane
> […] The growth observable is therefore **not computed**, and the k-essence-specific
> `c_s²` direction is untested. This is the highest-value cheap extension: it is the one
> observable that separates M3 from M1.

---

## 1. The citation search — result recorded BEFORE the computation

Searched 2026-09-22 for a DESI **DR2-era** growth-rate measurement with an uncertainty.
Outcome, stated honestly:

- **No DESI DR2 galaxy full-shape / RSD measurement exists.** DR2 Results II
  (arXiv:2503.14738) is BAO-only; the DR2-era combination papers reachable
  (e.g. arXiv:2602.18761, *joint DESI DR1 Full-Shape and DR2 BAO*, 2026-02) still take
  their growth information from **DR1** full-shape and report `σ8`, not `fσ8(z)`.
- **The one DR2 full-shape analysis that exists explicitly refuses to report `fσ8`.**
  DESI DR2 Lyα forest full-shape validation, arXiv:2607.27411, abstract (fetched
  2026-09-22): *"mock studies reveal a significant bias in the inferred growth-rate
  parameter fσ8, leading us to exclude this measurement from the final analysis."*
  A value DESI itself withdrew for bias is not usable, and none is invented here.
- A DR2 full-shape conference talk exists (PIRSA 26040071, 2026-04-29). **A talk is not
  a citable measurement with an uncertainty** and is not used.

**Therefore the pre-registered fallback is taken and labelled everywhere it appears:**
the yardstick is **DESI DR1 full-shape**, arXiv:2411.12021 (*DESI 2024 V: Full-Shape
Galaxy Clustering from Galaxies and Quasars*, JCAP 09 (2025) 008), PDF v5 fetched and
read 2026-09-22. This is **pre-DR2 growth data**; the weakening is stated in §5.

### The numbers that will be used (source-bound, transcribed, never estimated)

| Source | What is taken | Where |
|---|---|---|
| arXiv:2411.12021 App. A, Eqs. (A.1)–(A.12) | ShapeFit-only datavector + **full 4×4 Gaussian covariance** per bin; element (3,3) is `Var[fσs8(z)]` | uncertainty **derived in code** as `sqrt(Var)`, not hand-typed |
| arXiv:2411.12021 Table 11 | fiducial `(fσs8)_fid(z)` per bin | denominator of the fractional precision |
| arXiv:2411.12021 Table 1 | `z_eff` per tracer: BGS 0.295, LRG1 0.510, LRG2 0.706, LRG3 0.919, ELG2 1.317, QSO 1.491 | evaluation redshifts |
| arXiv:2411.12021 Table 9 | ShapeFit-only and ShapeFit+BAO MAP ratios `fσs8/(fσs8)_fid` with 68% errors | cross-check of the derived σ; ShapeFit+BAO = sensitivity variant |
| arXiv:2411.12021 abstract | *"a combined precision of 4.7% on the amplitude of the redshift space distortion (RSD) signal"* | combined-precision yardstick |
| arXiv:2411.12021 Table 6 row 1 | ShapeFit template cosmology (ωb 0.02237, ωcdm 0.1200, h 0.6736, 10⁹A_s 2.0830, n_s 0.9649) | provenance of `(fσs8)_fid` |

**Baseline = ShapeFit-only.** The DR2 BAO distances already carry the row-23 Step-2
separation; using the ShapeFit+BAO rows would double-count that information. ShapeFit+BAO
is reported as a sensitivity variant only.

**DESI's own restriction is honoured.** arXiv:2411.12021 §7.1 states the derived `fσ8`
values *"should only serve for visualization purposes, and they should never be used to
infer cosmology, for which one should use the actual fσs8 results."* Nothing here infers
cosmology from data: **no central value enters any decision** (GAP-3 discipline is kept).
Only the published *precision* on the growth amplitude is used, as a yardstick for a
model-vs-model forecast separation.

## 2. What is computed

Same fixed-parameter convention as `observable_separation.py`: `Ω_m = 0.2975`,
`h·r_d = 101.54 Mpc`, `r_d = 147.09 Mpc`, `Ω_r h² = 4.15e-5`; **no model is re-fit**, so
every separation is an upper bound on a marginalised one. Backgrounds are reused from
`observable_separation.py` unchanged (`quintessence_background`, `interacting_background`).

Normalisation convention, fixed here: all models share the primordial amplitude and the
linear transfer function, so `σ8(z)/σ8^ΛCDM(z) = δ(z)/δ^ΛCDM(z)` with `δ` matched deep in
matter domination (`a_i = 10⁻⁴`, `δ ∝ a`). No absolute `σ8` is needed and none is quoted.

- **ΛCDM, M1 (quintessence, smooth DE):** `δ'' + (2 + dlnE/dlna)δ' = (3/2)Ω_m(a)δ`
  in e-folds; `f = dlnδ/dlna`.
- **M3 (k-essence):** identical background to M1 at the same `α` — by construction the
  BAO separation is identical — with a clustering DE fluid of rest-frame sound speed
  `c_s²`, evolved with the standard sub-horizon Newtonian-gauge two-fluid system, at
  wavenumber `k`. `c_s²` is scanned over the range the model itself permits; that range
  is **derived symbolically** (sympy) from `P = KX + LX² − V` under no-ghost
  (`K + 6LX > 0`), no-gradient-instability / non-phantom (`K + 2LX ≥ 0`) and
  subluminality (`c_s² ≤ 1`) — the range is not assumed.
- **M2 (interacting dark sector):** growth equation **derived in-file** (sympy) from the
  perturbed conservation equations for the covariant choice `Q^μ = Q u_c^μ` (energy
  transfer along the CDM four-velocity ⇒ no momentum transfer in the CDM frame, CDM
  Euler unmodified), smooth DE (`w = −1`), `δQ` neglected at sub-horizon order, whole
  pressureless sector coupled (LS7's background convention). The RSD-measured growth rate
  in a coupled model is **not** `dlnδ/dlna`; the velocity-divergence rate is used, and
  both are reported.

Every equation is either derived in the committed script or cited to a named reference —
`/never-fabricate-derivation`.

## 3. The statistic (fixed now)

For each model, at each DR1 full-shape `z_i`:

```
r(z_i)  = [fσ8]_model(z_i) / [fσ8]_ΛCDM(z_i)          (pure ratio; no absolute sigma8)
eps_i   = sqrt( C_SF(z_i)[3,3] ) / (f sigma_s8)_fid(z_i)   (published fractional precision)
Delta_i = ( r(z_i) - 1 ) / eps_i                       (per-point separation, in sigma)
```

Reported: `max_i |Delta_i|` (**the decision uses this**, as in LS7), `Delta_tot` in
quadrature (labelled **optimistic** — DESI does not publish the cross-bin covariance),
and a combined-precision figure using the abstract's 4.7%.

For the M3-vs-M1 question the same statistic is used with **M1 in place of ΛCDM** in the
numerator's reference, at identical background parameters, so the comparison isolates
`c_s²`.

`eps_i` is the precision relative to the ShapeFit *template* cosmology while `r` is
relative to the DR2-BAO ΛCDM reference; the two ΛCDMs differ by a few percent in
`fσ8`, which perturbs `eps_i` at the same few-percent level. Stated with every number and
covered by an explicit ±10% `eps` sensitivity run.

## 4. The decision rule (fixed now, before any number)

**Primary question — does growth separate M3 from M1?**

- **SEPARABLE** if `max_i |Delta_i| > 1` for some `c_s²` in the derived allowed range and
  some `k` in `0.01 ≤ k ≤ 0.2 h/Mpc`, at M1's 1σ-boundary background (`α* = −0.3995`).
- **NOT SEPARABLE — NULL** if the maximum over the *entire* allowed `c_s²` range and that
  `k` range is `≤ 1`. This is published as a null, not softened: GAP-2 would then be
  closed with the answer "no", and the k-essence member stays observationally
  indistinguishable from the canonical one at current precision.
- The bracketing argument is pre-registered: if the separation is monotone in `c_s²` over
  the scan (checked, not assumed), the `c_s² = 0` endpoint bounds every `c_s²(a)`
  trajectory inside `[0,1)`, including time-dependent ones.

**Secondary question — does growth add to LS7's BAO-only boundary?**

- Report `max_i |Delta_i|` vs ΛCDM for M1, M2, M3 across LS7's scan grids and at LS7's
  boundary points (`α* = −0.3995`, `ξ* = 0.0250`). Growth **STRENGTHENS** the row-23
  boundary if it reaches 1σ at a parameter value where BAO does not; **ADDS NOTHING** if
  its separation is everywhere smaller than the BAO one. Either outcome is reported as
  found; neither is a failure.

## 5. How the DR1 fallback weakens the conclusion (stated before the result)

1. **Data volume.** DR1 full-shape is ~1 yr / 4.7M redshifts; DR2 BAO uses ~3 yr. The
   growth yardstick is therefore **looser than the BAO yardstick used in Step 2**, so a
   growth separation is being tested against a weaker ruler and a null is *expected to be
   easier to reach*. A null must be reported as "not separable **at DR1 full-shape
   precision**", never as "not separable at DESI precision".
2. **Forecastable improvement is not a measurement.** No DR2/DR5 error forecast is
   fabricated. If a null is found, the honest extension is: state the factor by which
   `eps_i` would have to shrink for the 1σ threshold to be crossed. That factor is a
   ratio of the computed separation to the published precision — it is a statement about
   this calculation, not a prediction about DESI, and will be labelled as such.
3. **Template mismatch** (§3) and **transfer-function fixing** (§2). For M2 the coupling
   changes the early-time `ρ_c`, hence matter–radiation equality and the transfer
   function, which is **not** modelled here (no Boltzmann code); M2's growth number is
   therefore an approximation and is labelled. **M1 and M3 are unaffected** — DE is
   negligible at `a_i` and `ρ_m(a)` is unchanged — so the primary (M3-vs-M1) result does
   not inherit this limitation.
4. **Scale dependence.** ShapeFit's `fσs8` is a broad-band amplitude assuming
   scale-independent growth; clustering DE is mildly `k`-dependent. The separation is
   quoted at a representative `k` with the `k`-scan shown.

## 6. Deliverables (pre-declared)

| File | Contents |
|---|---|
| `PREREGISTRATION_GAP2.md` | this file, committed alone, first |
| `growth_separation.py` / `.json` | sympy derivations + growth integrations + `Delta_i` |
| `GAP2_MEMO.md` | citation record, tables, QC, verdict, what is still open |
| `../PROPAGATION_NOTE.md` | new section appended for the site lane (existing P-1…P-4 preserved verbatim) |
| `reproducibility/manifests/experiments/…json` | Q2 manifest |

QC discipline inherited from LS7 and mandatory: exact shooting constraint `E(z=0) = 1`;
`ρ_DE` monotonicity; ΛCDM `f(z)` checked against the `Ω_m(z)^0.55` approximation; the
clustering-DE solver checked to reduce to the single-fluid equation in the smooth limit;
derived `σ` cross-checked against the independently published Table 9 errors; sensitivity
of the decision to `eps` (±10%), to `k`, to the ShapeFit+BAO variant, and to the
initial redshift.
