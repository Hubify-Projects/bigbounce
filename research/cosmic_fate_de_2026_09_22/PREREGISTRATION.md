# Row 23 — Pre-registration

**Lane:** `bb-LS7-row23-fate-de` (campaign 2026-09-18 publication push)
**Written:** 2026-09-21, committed BEFORE any statistic is computed.
**Ledger row:** 23 — *Cosmic fate under bounce-compatible dark energy.*

> For the DE classes Branch I finds bounce-compatible, which admit a future
> turnaround (ρ_DE reaching and crossing zero), and does any **present-day**
> observable distinguish those from ΛCDM at DESI DR2 precision?

**Inherited evidence layer.** `COSMIC_FATE_MEMO.md` is an Open-Questions-layer
document and asserts no BigBounce claim. This lane inherits that layer. It may
only be raised if this lane's own committed computation earns it — a computed
>1σ present-day separation would make row 23 a *forecast lane*, still not a
manuscript claim.

---

## 1. The two sets being crossed (fixed here, before any computation)

**Set B — Branch I bounce-compatible classes.** Taken verbatim from
`research/branch_I_bounce_compatible_DE/02_candidate_DE_classes.md` (Classes
1–7) and `horndeski_bounce_stability/phase1_results.md` (Phase-1 verdicts
A–F). Each class carries Branch I's own verdict word; this lane does **not**
re-adjudicate bounce compatibility and does not promote an
`EFT_INAPPLICABLE`/`UNDETERMINED` verdict to "compatible".

**Set T — classes admitting a future turnaround.** Decided by the row-20
criterion, i.e. `COSMIC_FATE_MEMO.md` Eqs. (2.3)–(2.5):

```
turnaround at a_t  ⇔  H(a_t) = 0  and  ä(a_t) < 0
H = 0   ⇔   ρ_tot(a_t) = 3 k c² / (8πG a_t²)            (2.4)
ä < 0   ⇔   ρ_tot(a_t) + 3 p_tot(a_t)/c² > 0            (2.5)
```

with the flat/open corollary that `k ≤ 0` forces `ρ_tot(a_t) ≤ 0`, hence some
component must reach and cross zero density.

## 2. Step 1 — the cross-table (pre-registered form)

One row per Branch I class. Columns: Branch I verdict (quoted) · the class's
`ρ(a)`, `p(a)` in closed form · the criterion (2.4)+(2.5) evaluated
**symbolically** for that class (sympy where it helps) · PASS / FAIL /
UNDETERMINED · **the equation that decides it**, written out.

Pre-registered rules:
- A class is `UNDETERMINED` in Set T when no general criterion exists for it
  (memo §3g, modified gravity) or when Branch I left its bounce status
  undetermined. `UNDETERMINED` is never counted as a pass on either axis.
- Nothing enters "both sets" unless it PASSES on both axes with the deciding
  equation shown.

## 3. Step 2 — the present-day observable separation (pre-registered)

For **every class in BOTH sets**, and only those, compute against a ΛCDM
reference:
1. `w(z)` and `ρ_DE(z)/ρ_DE,0` trajectories over `0 ≤ z ≤ 2.5` (the DR2 range);
2. the DESI DR2 distance observables `D_M/r_d`, `D_H/r_d` (and `D_V/r_d` where
   that is what DR2 reports) at the DR2 effective redshifts;
3. `f σ8(z)` **only if** a citable DR2-era measurement with an uncertainty is
   available without downloading a catalogue; otherwise it is a **named gap**.

**Separation statistic (fixed now):** for each observable `O_i` with published
DR2 1σ uncertainty `σ_i`,

```
Δ_i = ( O_i^model − O_i^ΛCDM ) / σ_i      (per-point, in σ)
Δ_tot = sqrt( Σ_i Δ_i² )                  (quadrature over independent points,
                                           reported alongside max_i |Δ_i|)
```

Both are reported. `Δ_tot` treats the quoted DR2 points as independent because
the published covariance is not in hand — this is an **optimistic** separation
and is labelled as such everywhere it appears. The **decision** uses the
conservative per-point `max_i |Δ_i|` unless a covariance is obtained.

**Model–ΛCDM comparison protocol.** The comparison is made at fixed present-day
`Ω_m` and `H₀ r_d` — i.e. the model is *not* re-fit to the data. A separation
computed this way is an upper bound on what a marginalised analysis would find;
this direction of the bias is stated with every number. If a class's separation
survives only because parameters were held fixed, it is reported as
`FIXED-PARAM ONLY` and does not on its own trip the success rule.

**Sources of DR2 numbers (the only ones allowed):**
- DESI Collaboration, *DESI DR2 Results II: BAO measurements and cosmological
  constraints*, arXiv:2503.14738 (Phys. Rev. D 112, 2025).
- DESI Collaboration, *DESI DR2 Results IV: Alcock–Paczyński from the Lyα
  forest*, arXiv:2607.27410 — values already verified into
  `COSMIC_FATE_MEMO.md` §4.1: `D_H/r_d = 8.600 ± 0.066`,
  `D_M/r_d = 39.32 ± 0.33` at `z_eff = 2.33`; `H₀ = 66.5 ± 1.3`,
  `Ω_m = 0.325 ± 0.018` (ΛCDM + BBN).
- Planck 2018 VI, arXiv:1807.06209, for the ΛCDM reference background
  (`Ω_m = 0.315 ± 0.007`, `H₀ = 67.4 ± 0.5`).

**Never-invent rule (hard).** Every uncertainty used must be traceable to one
of those citations, quoted with its source line. If a needed uncertainty is not
obtainable from a citable source in this lane, the corresponding observable is
recorded as a **named gap** in the output memo and is excluded from `Δ_tot` —
it is never estimated, interpolated, or "assumed comparable to" another point.

## 4. Step 3 — the decision rule (row 23's own success/kill rule, fixed now)

- **OPENS A FORECAST LANE** if ≥1 class is in **both** sets **and** its
  conservative separation `max_i |Δ_i| > 1σ` at DR2 precision for parameter
  values that are not already excluded by the same data.
- **CLOSES AS AN OPEN QUESTION** if the intersection is empty, or if every
  class in the intersection has `max_i |Δ_i| ≤ 1σ` everywhere its parameters
  are allowed. This outcome is published as such — a null is the result, not a
  failure, and it goes on the public Open-Questions surface.
- **Partial/boundary outcome:** if the separation exceeds 1σ only for a
  sub-region of parameter space, the deliverable is the explicit boundary
  (e.g. the turnaround epoch `t_c` at which the separation crosses 1σ), and
  the verdict states which side of it the model must lie on to be testable
  now. This is pre-registered as an allowed outcome so it cannot be
  retro-fitted into a success.

## 5. Integrity constraints carried into this lane

- `/never-fabricate-derivation`: every equation in the cross-table is either
  derived in-file (sympy, with the script committed) or cited to a specific
  equation of `COSMIC_FATE_MEMO.md` / a named reference. No new math claim
  without one of those two.
- Nulls stay nulls. The memo's §10 states the honest prior expectation that the
  intersection may be empty or observationally silent; this lane must not
  soften a null into a "promising" word.
- No paper `.tex`, no SSOT, no site data is touched by this lane. Only the
  row-23 status cell of `NEXT_SCIENCE_LEDGER.md`, this output directory, a Q2
  manifest, and (if anything is publishable to the Open-Questions surface) the
  exact printable text in `PROPAGATION_NOTE.md` for a site lane.
- Convex is disabled (spending limit): every intended mutation is appended to
  `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`, never sent.

## 6. Pre-declared deliverables

| File | Contents |
|------|----------|
| `PREREGISTRATION.md` | this file, committed alone, first |
| `cross_table.py` / `.json` | symbolic Set-B × Set-T evaluation, one record per class |
| `observable_separation.py` / `.json` | trajectories + Δ_i / Δ_tot per model in the intersection |
| `ROW23_MEMO.md` | cross-table, separation results, named gaps, verdict |
| `PROPAGATION_NOTE.md` | exact printable Open-Questions text, or a statement that none is warranted |
| `reproducibility/manifests/experiments/…json` | Q2 manifest (sources, scripts, compute venue, cost, wall-clock) |
