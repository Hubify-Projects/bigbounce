# Cosmic Fate: can an accelerating universe recollapse?

**Technical memo · worker W3 · 2025 legacy-archaeology campaign · 2026-09-18**

> **Evidence layer: Open Question.** Literature review plus textbook-GR derivation.
> Nothing in this memo is a BigBounce claim, a prediction, or a result. It changes no
> manuscript, no SSOT row, and no existing null. Houston's stated preference for a
> regenerative universe is the reason the question is *asked* and enters nothing else.

**Numerics:** every number quoted below is produced by
`research/archaeology_2025/outputs/cosmic_fate_turnaround_2026_09_18.py`
(run recorded in the JSON as `generated_utc = 2026-09-19T00:05:32+00:00`; output
`cosmic_fate_turnaround_2026_09_18.json`).
No number in this memo was typed by hand.

---

## 1. Scope and relation to existing BigBounce work

**What already exists in this repo, and which this memo does not duplicate:**

| Existing work | Path | What it settles |
|---|---|---|
| Branch I — bounce-compatible dark-energy sectors | `research/branch_I_bounce_compatible_DE/` (`01_problem_statement.md`, `02_candidate_DE_classes.md`, `03_nontrivial_compatibility_tests.md`, `horndeski_bounce_stability/`) | Which DE sectors are *compatible with* a spin-torsion bounce at ρ ~ M_Pl⁴ — a UV/early-time stability question. Explicitly *not* a derivation of DE from the bounce. |
| P1N — ECH torsion-bounce note | `arxiv/paper1bc_ech_note/main.tex` | The committed statement of the torsion-bounce mechanism, and the systematic closure of four candidate routes from minimal ECH torsion to a late-time Λ-like density. |
| Popławski spin-axis dipole exclusion | `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` (Track C1 / P4′) | The rotating-parent-black-hole spin-axis prediction is excluded against the DESI A95 upper limit. Closed; nothing here reopens it. |

**Branch I asks an early-time question** ("does this DE sector break the bounce?").
**This memo asks the opposite-end question** ("does any DE sector let the *future*
expansion turn around?"). They intersect only in the model taxonomy of §3, and the
intersection is stated where it occurs — a DE model can pass Branch I's bounce-stability
test and still be fate-irrelevant, and vice versa.

**What this memo adds:**

1. A self-contained derivation of the turnaround condition from the Friedmann and
   Raychaudhuri equations, with the k-sign and unit conventions written out (§2).
2. An exact closed-ΛCDM recollapse criterion derived here and cross-checked numerically
   — including the result that at the observed matter density **no positive Λ permits
   recollapse at any curvature** (§3b, §3 table).
3. The correct reading of the 2025-era `M_crit = Λc²r³/(3G)` relation, including a new
   observation: applied to a homogeneous sphere it collapses identically onto the
   *deceleration* condition ä < 0, not onto any fate condition (§6).
4. A clean separation of Crunch from Bounce, with the P1N mechanism statement quoted
   rather than re-derived (§5).

**What this memo does not do:** it does not fit data, does not run an MCMC, does not
compute posterior fractions, does not propose a paper, and does not assign probabilities
to any branch of the fate tree. §8 is a taxonomy, not a ranking.

---

## 2. Turnaround conditions from the Friedmann and Raychaudhuri equations

### 2.1 The two equations (standard textbook GR/cosmology)

For a Friedmann–Lemaître–Robertson–Walker metric with scale factor a(t) and a perfect-fluid
total stress tensor, the Einstein equations give the **Friedmann equation**

```
    H² = (8πG/3) ρ_tot − k c² / a²          (SI; ρ_tot = total MASS density)     (2.1)
```

and the **acceleration (Raychaudhuri) equation**

```
    ä/a = −(4πG/3) ( ρ_tot + 3 p_tot / c² )                                       (2.2)
```

Both are standard and are quoted here, not derived; any GR text (e.g. Weinberg,
*Cosmology*, §1.5; Hawking & Ellis, *The Large Scale Structure of Space-Time*, §5.4)
contains them.

**Units and the curvature term.** Two conventions are in circulation and the 2025-era
notes mixed them:

* **Dimensionful-a convention.** a has units of length, k ∈ {−1, 0, +1} dimensionless.
  Then `k c²/a²` has units m² s⁻² / m² = s⁻² ✓, matching `[Gρ] = m³ kg⁻¹ s⁻² · kg m⁻³ = s⁻²` ✓.
* **Dimensionless-a convention.** a is dimensionless with a(t₀) = 1, and k carries units
  m⁻²; `k c²/a²` again has units s⁻². ✓

In natural units (c = 1) with ρ read as an **energy** density, (2.1) is `H² = (8πG/3)ρ − k/a²`.
All three forms are used in the literature; this memo uses SI mass density in §2–§3 and
flags any switch. Throughout, k > 0 ⇔ closed, k = 0 ⇔ flat, k < 0 ⇔ open, and
`Ω_k ≡ −k c²/(a₀²H₀²)`, so Ω_k < 0 ⇔ closed.

### 2.2 The turnaround condition

A **turnaround** is a moment t_t at finite scale factor a_t = a(t_t) where expansion stops
and contraction begins:

```
    H(a_t) = 0     and     ä(a_t) < 0                                             (2.3)
```

Setting H = 0 in (2.1) gives the **density condition at turnaround**

```
    ρ_tot(a_t) = 3 k c² / (8πG a_t²)                                              (2.4)
```

Two mutually exclusive cases follow immediately, and they exhaust the possibilities:

* **k > 0 (closed).** The right-hand side of (2.4) is positive, so a turnaround can occur
  at a positive total density. Positive spatial curvature is the only way to stop
  expansion without any negative-energy component.
* **k ≤ 0 (flat or open).** The right-hand side is ≤ 0, so a turnaround requires
  `ρ_tot(a_t) ≤ 0`. Since ordinary matter, radiation and a positive Λ all contribute
  ρ > 0, **at least one component must carry negative energy density** — a negative
  cosmological constant, or a scalar field sitting at negative potential energy
  (`ρ_φ = φ̇²/2 + V(φ) < 0` requires `V < −φ̇²/2 < 0`). For k = 0 exactly, (2.4)
  demands `ρ_tot(a_t) = 0`.

The second condition in (2.3), via (2.2), is

```
    ä(a_t) < 0   ⇔   ρ_tot(a_t) + 3 p_tot(a_t)/c² > 0                             (2.5)
```

i.e. the **strong energy condition must hold at the turnaround**. Dimensional check on
(2.5): `p/c²` has units Pa/(m²s⁻²) = kg m⁻¹ s⁻² · m⁻² s² = kg m⁻³ ✓, the same as ρ.

**Note on Ḣ versus ä.** The brain-dump (§1 of the input) writes the second condition as
`Ḣ(a_t) < 0`. From `Ḣ = ä/a − H²`, at a point where H = 0 we have `Ḣ = ä/a` exactly, so the
two statements coincide *at the turnaround* and only there. Away from H = 0 they differ.
This is not an error in the dump but it is worth pinning down, because the same identity
run in the opposite direction defines a **bounce**: `H = 0` with `ä > 0`, i.e. `Ḣ > 0`, i.e.
`ρ + 3p/c² < 0`. Turnaround and bounce are the *same* equation with opposite signs of the
SEC combination. That is the formal reason §5 exists: nothing in the fate problem supplies
the sign flip.

---

## 3. Model taxonomy: the explicit turnaround condition, model by model

Write the expansion rate as `E²(a) ≡ H²/H₀² = Ω_m a⁻³ + Ω_r a⁻⁴ + Ω_k a⁻² + Ω_DE f(a)`
with `Ω_k = 1 − Ω_m − Ω_r − Ω_DE`. Radiation is dropped below (Ω_r ~ 10⁻⁴ and decays
fastest; it cannot affect a future turnaround). A turnaround exists iff `E²(a) = 0` has a
root at some a > 1.

### (a) Flat ΛCDM with constant Λ > 0 — **no turnaround, ever**

```
    H²(a) = (8πG/3) ρ_m(a) + Λc²/3 ,      ρ_m(a) = ρ_m,0 a⁻³ ≥ 0
    ⇒ H²(a) ≥ Λc²/3 > 0   for every a > 0.                                        (3.1)
```

H² is bounded strictly below by a positive constant, so H never reaches zero and (2.3)
can never be satisfied. There is no turnaround at any finite or infinite a. The universe
approaches de Sitter, `H → H₀√Ω_Λ`. Script check: at a = 10⁶ the code returns
`E² = 0.685`, exactly the Ω_Λ floor, and `turnaround = None`.

This is the single most important line in the memo. **Under flat ΛCDM with a genuinely
constant, genuinely positive Λ, a Big Crunch is not unlikely — it is impossible.** Any
Crunch scenario must therefore break one of the three words "flat", "constant",
"positive". The late-time thermodynamic endpoint of this branch (heat death /
asymptotically empty de Sitter) is discussed in e.g. Lundgren, Bondarescu & Bondarescu,
arXiv:1201.1298, which is the dump's citation [2]; it is a de Sitter-thermodynamics paper
and supports the *endpoint* statement, not the dynamical one derived here.

### (b) Closed ΛCDM (k > 0, Λ > 0) — turnaround possible only in a region observations are nowhere near

With `g(a) ≡ a³E²(a) = Ω_Λ a³ + Ω_k a + Ω_m` (same sign as E² for a > 0), note the identity
`g(1) = Ω_m + Ω_k + Ω_Λ = 1 > 0`: the present epoch is always an allowed expanding state.
For Ω_Λ > 0, g is a cubic with positive leading coefficient, so it can dip below zero only
if Ω_k < 0 (closed), and only at its single positive stationary point

```
    g'(a) = 3Ω_Λ a² + Ω_k = 0   ⇒   a_* = √( |Ω_k| / (3Ω_Λ) )                      (3.2)
    g(a_*) = Ω_m − (2/3)|Ω_k| a_*                                                  (3.3)
```

A root exists iff `g(a_*) ≤ 0`, i.e. iff `4|Ω_k|³ ≥ 27 Ω_m² Ω_Λ`. But existence of a root is
not enough: because g(1) > 0, the root pair either straddles the past (a < 1 — the
"no-Big-Bang" loitering class) or the future (a > 1 — recollapse). The future case requires
`a_* > 1`. Hence the **complete closed-ΛCDM turnaround criterion**:

```
    future turnaround  ⇔   Ω_Λ < 0
                        OR ( Ω_Λ > 0  AND  |Ω_k| > 3Ω_Λ  AND  4|Ω_k|³ ≥ 27 Ω_m² Ω_Λ )   (3.4)
```

(This is the standard Carroll–Press–Turner recollapse boundary written in a form derived
from scratch here. `4|Ω_k|³ = 27Ω_m²Ω_Λ` is the familiar critical curve; the `|Ω_k| > 3Ω_Λ`
clause is the branch selector that distinguishes recollapse from a no-Big-Bang solution.)

**The consequence that matters.** Substituting `Ω_k = 1 − Ω_m − Ω_Λ < 0`, the condition
`|Ω_k| > 3Ω_Λ` reads `Ω_m + Ω_Λ − 1 > 3Ω_Λ`, i.e.

```
    Ω_Λ < (Ω_m − 1)/2                                                              (3.5)
```

For any `Ω_m < 1` the right-hand side is negative. **At the observed matter density, no
positive cosmological constant permits recollapse, for any amount of positive curvature.**
Closing the universe does not help; it never did at Ω_m < 1.

Script output (`A1`, bisection on Ω_Λ at fixed Ω_m, cross-checked against the analytic
discriminant):

| Ω_m | Ω_Λ,crit (recollapse requires Ω_Λ below this) |
|---|---|
| 0.10 | −0.000000 |
| **0.31** | **−0.000000** |
| 0.315 | −0.000000 |
| 0.50 | −0.000000 |
| 0.90 | −0.000000 |
| 1.00 | −0.000000 |
| 1.05 | +0.000017 |
| 1.50 | +0.008666 |
| 2.00 | +0.041889 |
| 3.00 | +0.167659 |
| 5.00 | +0.562998 |
| 10.00 | +1.939489 |

The boundary is **exactly zero for every Ω_m ≤ 1** and only lifts off zero for Ω_m > 1, as
(3.5) requires. Spot checks at Ω_m = 0.31 (script `A2`) confirm: Ω_Λ = 0.69, 0.80, 1.00,
1.50, 2.00 and 0.00 all give `a_turn = None`; Ω_Λ = −0.01, −0.10, −0.345, −0.69 give
a_turn = 8.580, 2.989, 1.866, 1.515 respectively. The switch is the *sign of Λ*, not the
curvature.

Asked the other way (script `A3`): holding Ω_Λ = 0.685 at its observed value, recollapse
would require **Ω_m ≥ 5.516**, i.e. **17.5× the observed matter density**. That is the
quantitative distance between the data and the closed-recollapse region.

The analytic-vs-brute-force cross-check (`A4`) agrees on all nine test models, including
the exactly-solvable case Ω_m = 1.2, Ω_Λ = 0 where the criterion gives
a_turn = Ω_m/|Ω_k| = 6.0 and the numerics return 6.000.

### (c) Flat universe with matter and a **negative** cosmological constant

Take k = 0, Λ < 0, write `Ω_Λ = −|Ω_Λ|`. Flatness forces `Ω_m = 1 + |Ω_Λ| > 1`. Then

```
    E²(a) = Ω_m a⁻³ − |Ω_Λ| = 0   ⇒   a_turn/a₀ = ( Ω_m / |Ω_Λ| )^{1/3}             (3.6)
```

and at that point `ρ_tot = 0`, exactly case k = 0 of (2.4). The SEC check (2.5) is satisfied:
at ρ_tot = 0 we have `ρ + 3p/c² = 3p/c²`, and with `p_m ≈ 0`, `p_Λ = −ρ_Λc² = +|ρ_Λ|c² > 0`,
so ä < 0 ✓ — the turnaround is a genuine turnaround, not an inflection.

The model is exactly solvable. Substituting `a(t) = a_turn [sin x]^{2/3}` with
`x = (3/2)√|Ω_Λ| H₀ t` into (2.1) gives `H = √|Ω_Λ| H₀ cot x`, hence
`H² = |Ω_Λ|H₀²(1/sin²x − 1) = Ω_m a⁻³ − |Ω_Λ|` in H₀² units ✓ — the ansatz is verified, not
assumed. Turnaround is at x = π/2, the crunch (a → 0) at x = π, and today (a = 1) at
`x₀ = arcsin √(|Ω_Λ|/Ω_m)`. The script reproduces `H(t₀)/H₀ = 1.000000` in every row as an
internal check. With 1/H₀ = 14.5073 Gyr (H₀ = 67.4 km/s/Mpc):

| \|Ω_Λ\| | Ω_m (flatness) | a_turn/a₀ | age today (Gyr) | t_turnaround (Gyr) | now → turnaround (Gyr) | now → crunch (Gyr) |
|---|---|---|---|---|---|---|
| 0.001 | 1.001 | 10.003 | 9.668 | 480.414 | 470.745 | 951.159 |
| 0.010 | 1.010 | 4.657 | 9.639 | 151.920 | 142.281 | 294.201 |
| 0.050 | 1.050 | 2.759 | 9.515 | 67.941 | 58.426 | 126.366 |
| 0.100 | 1.100 | 2.224 | 9.367 | 48.041 | 38.674 | 86.716 |
| 0.345 | 1.345 | 1.574 | 8.745 | 25.865 | 17.120 | 42.985 |
| 0.685 | 1.685 | 1.350 | 8.079 | 18.356 | 10.277 | 28.632 |

**This pure model is already excluded**, and the table shows why twice over: every row
needs Ω_m > 1 (observed: 0.315 ± 0.007), and every row gives a present age below 10 Gyr
against a measured ≈ 13.8 Gyr. The rows are a scaling reference for the *mechanism*, not a
fit. The physically live version of this branch is not "Λ is negative today" but "the
dark-energy density crosses zero in the future" — which is case (d).

### (d) Canonical quintessence with a potential that crosses zero

Mechanism, in the flat case. For a canonical scalar,
`ρ_φ = φ̇²/2 + V(φ)` and `p_φ = φ̇²/2 − V(φ)` (c = 1 in this paragraph). A flat-universe
turnaround needs `ρ_tot = ρ_m + ρ_φ = 0`, i.e.

```
    V(φ) = −( ρ_m + φ̇²/2 )   < 0                                                   (3.7)
```

so the field must be at **negative potential energy** deep enough to cancel the matter
density and its own kinetic energy. The SEC check is then automatic:

```
    ρ_tot + 3p_tot = 0 + 3( φ̇²/2 − V ) = 3( φ̇²/2 + ρ_m + φ̇²/2 ) = 3( ρ_m + φ̇² ) > 0  (3.8)
```

using (3.7). So **whenever a canonical scalar drives ρ_tot through zero, ä < 0 there
automatically** and the turnaround is genuine. This is the cleanest statement of the
mechanism: no fine-tuning of the second condition is required once the first is arranged.

Toy potentials that do this include a linear potential `V = V₀ − αφ` (the field slides to
arbitrarily negative V) and a quadratic-top `V = V₀ − m²φ²/2`. In both, acceleration today
and collapse later are controlled by the same parameters, which is what makes the class
observationally constrainable rather than unfalsifiable.

Verified references for this class:
* **Kallosh & Linde**, *Dark Energy and the Fate of the Universe*, arXiv:astro-ph/0301087,
  JCAP 0302:002 (2003) — abstract verified 2026-09-18: "in many models based on
  supergravity, the dark energy eventually becomes negative and the universe collapses
  within the time comparable to the present age of the universe", with collapse on
  10¹⁰–10¹¹ yr timescales.
* **Kallosh, Kratochvil, Linde, Linder & Shmakova**, *Observational Bounds on Cosmic
  Doomsday*, arXiv:astro-ph/0307185 (2003) — abstract verified: linear-potential model;
  data then available implied the universe's remaining lifetime exceeds ~10 Gyr, with a
  forecast that SNAP+Planck could push the bound to `t_c > 40 Gyr` at 95% CL.
* **Garriga, Pogosian & Vachaspati**, *Forecasting Cosmic Doomsday from CMB/LSS
  Cross-Correlations*, arXiv:astro-ph/0311412, Phys. Rev. D **69**, 063511 (2004) —
  abstract verified: "The negative potential energy eventually turns the expansion into
  contraction and the local universe undergoes a big crunch." This is the dump's citation
  [3], now resolved (it was delivered as a bare APS URL).

Relation to Branch I: `02_candidate_DE_classes.md` rates quintessence "generally
compatible" with the bounce, with only a weak early-time constraint. That verdict is about
ρ_φ at ρ ~ M_Pl⁴ and is untouched by (3.7), which is a statement about V at
a ≫ 1. **A quintessence model can be simultaneously bounce-compatible (Branch I) and
Crunch-producing (this memo).** The two analyses do not conflict and do not overlap.

### (e) Interacting dark sector — the generic requirement

If dark energy exchanges energy with dark matter,
`ρ̇_DE + 3H(1+w)ρ_DE = Q`, `ρ̇_DM + 3Hρ_DM = −Q`, the fate condition is unchanged: a
turnaround still requires (2.4). Generically, therefore, the interaction must do one of
exactly two things at large a:

1. drive the **effective** dark-energy density `ρ_DE,eff(a) → 0 and through zero`
   (a sustained drain, Q < 0 in the DE equation, strong enough to beat the `−3H(1+w)ρ_DE`
   term), reproducing case (d)'s condition by other means; or
2. leave `ρ_DE,eff > 0` asymptotically, in which case no turnaround occurs (case (a)'s
   proof applies to any positive asymptotic floor, not just to a constant Λ).

Merely *making w evolve* is not enough; a coupled model whose ρ_DE stays positive at all a
has the same fate as ΛCDM. Branch I's Class 6 finds the same sector only weakly
constrained by the bounce, again a disjoint question.

### (f) Phantom (w < −1) → **Big Rip, not a Crunch** — a common and important conflation

For a constant equation of state w, `ρ_DE ∝ a^{−3(1+w)}`. For w < −1 the exponent is
positive: **the dark-energy density grows with expansion**. In the DE-dominated flat limit,
with `m ≡ −3(1+w)/2 > 0`,

```
    ȧ = H₀ √Ω_DE  a^{1+m}
    ⇒ ∫ a^{−1−m} da = H₀√Ω_DE (t−t₀)
    ⇒ a(t)^{−m} = 1 − m H₀√Ω_DE (t−t₀)
    ⇒ a → ∞  at   t − t₀ = 1 / ( m H₀ √Ω_DE ) = 2 / ( 3|1+w| H₀ √Ω_DE )             (3.9)
```

a **finite-time divergence of the scale factor**. Dimensional check: the right-hand side of
(3.9) is a pure number times 1/H₀, i.e. a time ✓. (This DE-only estimate neglects matter,
which only shortens the interval.) The endpoint is the Big Rip of **Caldwell, Kamionkowski
& Weinberg**, *Phantom Energy and Cosmic Doomsday*, arXiv:astro-ph/0302506,
Phys. Rev. Lett. **91**, 071301 (2003) — abstract verified 2026-09-18: "The positive
phantom-energy density becomes infinite in finite time ... before the death of the Universe
in a 'Big Rip'."

**Phantom dark energy takes the universe further from a Crunch, not closer.** Both
outcomes are sometimes filed under "cosmic doomsday", and that shared label — plus the
shared title word "Doomsday" in the Kallosh et al. and Caldwell et al. papers — is the
likely origin of the conflation. Any statement of the form "DESI's w < −1 hints point to a
Crunch" is wrong on its face: w < −1 points to a Rip.

### (g) Modified gravity

One sentence, as scoped: f(R), Horndeski/DHOST, massive gravity and braneworld models can
produce an effective `ρ_eff + 3p_eff > 0` at late times and hence a turnaround, but the
condition is model-by-model and no useful general criterion exists — it is not derived here,
and Branch I (`02_candidate_DE_classes.md` Classes 4 and 7,
`horndeski_bounce_stability/`) already owns the modified-gravity sector from the
bounce-stability side.

---

## 4. What current observations permit

### 4.1 What the data actually say (verified this session)

* **DESI DR2 BAO** — DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon
  Acoustic Oscillations and Cosmological Constraints*, arXiv:2503.14738 (submitted
  18 Mar 2025; Phys. Rev. D 112, 2025). Abstract verified: the data favour "a solution in
  the quadrant with w₀ > −1 and w_a < 0"; dynamical dark energy is "preferred over ΛCDM at
  3.1σ for the combination of DESI BAO and CMB data", and 2.8–4.2σ with SNe depending on
  the SNe sample.
* **DESI DR2 Lyα full shape** — DESI Collaboration, *DESI DR2 Results IV:
  Alcock-Paczyński Measurements from the Lyman Alpha Forest and Cosmological Constraints*,
  arXiv:2607.27410 (submitted 29 Jul 2026). Abstract verified: 1% AP precision at
  z_eff = 2.33, `D_H/r_d = 8.600 ± 0.066`, `D_M/r_d = 39.32 ± 0.33`; under ΛCDM with a
  BBN prior, `H₀ = 66.5 ± 1.3 km/s/Mpc` and `Ω_m = 0.325 ± 0.018`; evolving dark energy
  "preferred over ΛCDM at 2.7σ for the combination of DESI and CMB data, and at 3.2σ when
  also including supernovae."

**The 2026-07-30 DESI result the dump cites does exist**, and I located it: the press item
`desi.lbl.gov/2026/07/30/...` corresponds to arXiv:2607.27410 (plus companion papers
2607.27411–13). The dump's characterisation is **half right and needs correcting**: the
release does say the new full-shape central value "shifts toward ΛCDM" with substantially
smaller uncertainty, but the same paper's abstract still reports the joint dataset
preferring w₀w_aCDM at 2.7σ / 3.2σ. Quoting only the shift-toward-ΛCDM half understates the
state of the evidence. Both facts must be stated together.

* **Background cosmology used for all numerics**: Planck Collaboration, *Planck 2018
  results. VI. Cosmological parameters*, arXiv:1807.06209, A&A 641, A6 (2020). Abstract
  verified: `Ω_m = 0.315 ± 0.007`, `H₀ = 67.4 ± 0.5 km/s/Mpc`, `σ₈ = 0.811 ± 0.006`.
  The spatial-curvature constraint is **not in that abstract** and is therefore
  **[UNVERIFIED — not quoted]**: no Ω_k number is used anywhere in this memo. §3(b) does
  not need one, because the criterion (3.5) rules out positive-Λ recollapse at Ω_m < 1 for
  *any* curvature.

### 4.2 Why extrapolating a CPL (w₀, w_a) fit to a → ∞ is not a fate forecast

Three independent reasons, the third derived here.

1. **Range of validity.** CPL, `w(a) = w₀ + w_a(1−a)`, is a two-parameter Taylor expansion
   about a = 1 calibrated by data at z ≲ 2.5 (a ≳ 0.29). Evaluating it at a = 10 or a → ∞
   is extrapolating a truncated expansion by orders of magnitude outside its support. It is
   a fitting function, not a Lagrangian; it has no equation of motion, no stability
   conditions, and no UV completion to constrain its asymptotics.
2. **No physically complete model behind it.** The DESI-preferred quadrant (w₀ > −1,
   w_a < 0) implies w crossing −1 in the past. A single canonical scalar cannot cross the
   phantom divide; a physically complete realisation needs at least two fields, a
   non-canonical kinetic term, or modified gravity — and the fate depends entirely on which
   one, not on the fit.
3. **Taken literally, CPL does not predict a Crunch anyway.** Integrating
   `d lnρ_DE/d ln a = −3(1+w)`,

   ```
       ρ_DE(a) = ρ_DE,0 · a^{−3(1+w₀+w_a)} · e^{−3 w_a (1−a)}                       (4.1)
   ```

   (verified by differentiating: `d lnρ/d ln a = −3(1+w₀+w_a) + 3w_a a = −3(1+w(a))` ✓).
   For w_a < 0 the exponential factor is `e^{3w_a(a−1)} → 0` as a → ∞ and dominates any
   power law, so `ρ_DE → 0⁺` monotonically — **it decays to zero and never becomes
   negative**. A flat CPL universe with w_a < 0 therefore has `E²(a) = Ω_m a⁻³ + ρ_DE/ρ_c,0 > 0`
   for all a: no turnaround, no Rip, just an asymptotic coast. The "DESI implies collapse"
   inference does not even follow from the fitting function, let alone from physics.

### 4.3 Bottom line on the data

* **Current data do not imply a future Crunch.** Nothing measured to date requires,
  favours, or forecasts a turnaround.
* **Current data do not exclude one for specific physically complete models.** They
  constrain the *timing* of any turnaround in those models (Kallosh et al. 2003:
  lifetime ≳ 10 Gyr from the data then available).
* **Excluded now**, at current precision: flat matter + negative Λ as the whole story
  (needs Ω_m > 1 and an age < 10 Gyr, §3c); closed ΛCDM recollapse with Ω_Λ > 0 at
  Ω_m ≈ 0.315 (excluded by (3.5) *identically*, for any curvature, not merely by data);
  any Crunch under exactly-constant Λ > 0 with k = 0 (impossible by (3.1)).
* **Still viable**, in the sense of not excluded: quintessence/multi-field dark energy whose
  potential crosses zero in the future (§3d); interacting dark sectors whose effective DE
  density crosses zero (§3e); modified-gravity late-time effective-SEC restoration (§3g).
  All three are viable precisely because they are indistinguishable from ΛCDM today and
  differ only in an unobserved future — which is also their falsifiability problem (§10).
* **A "model-independent probability of a Big Crunch" cannot be computed** and must never
  be quoted. Posterior statements exist only within an explicit, physically complete model
  class with a stated prior.

---

## 5. Crunch ≠ Bounce

Turnaround and contraction are settled by (2.3)–(2.5) at low density. What happens when the
contracting universe reaches high density is an entirely independent physics question, and
the fate analysis contributes nothing to it. From §2.2: a bounce needs `H = 0` with
`ρ + 3p/c² < 0` — the *opposite* sign of the very inequality (2.5) that made the turnaround
a turnaround. **Nothing in a Crunch supplies that sign flip.** Four candidate high-density
behaviours:

### 5.1 Classical GR — singularity

The Hawking–Penrose singularity theorems (standard textbook GR; Hawking & Ellis 1973,
Ch. 8) state qualitatively: given a suitable energy condition (strong or null, depending on
the theorem), a causality/global condition, and a trapped surface or a closed contracting
FLRW slice, the spacetime is geodesically incomplete. A contracting FLRW universe with
ordinary matter satisfies these hypotheses, so classical GR terminates contraction in a
singularity, not a bounce. **What produces `H = 0` with `Ḣ > 0`: nothing.** The theorems
are what must be evaded, and they are evaded only by violating a hypothesis — an energy
condition (torsion, quantum effects), or the classical field equations themselves.

### 5.2 ECSK spin–torsion — effective repulsion at extreme fermion density

Verified statements only, from abstracts I fetched 2026-09-18:

* Popławski, *Cosmology with torsion: An alternative to cosmic inflation*, arXiv:1007.0587,
  Phys. Lett. B **694**, 181 (2010) [Erratum B**701**, 672 (2011)]: "The torsion of
  spacetime generates gravitational repulsion in the early Universe filled with quarks and
  leptons, preventing the cosmological singularity: the Universe expands from a state of
  minimum but finite radius", with torsion density parameter `Ω_S ≈ −10⁻⁶⁹`.
* Popławski, *Big bounce from spin and torsion*, arXiv:1105.6127, Gen. Rel. Grav. **44**,
  1007 (2012): "Spacetime torsion, generated by spin of Dirac fields, induces gravitational
  repulsion in fermionic matter at extremely high densities and prevents the formation of
  singularities. Accordingly, the big bang is replaced by a bounce that occurred when the
  energy density ε ∝ gT⁴ was on the order of n²/m_Pl²", with n ∝ gT³ the fermion number
  density and g the number of thermal degrees of freedom.

**What produces `H = 0` with `Ḣ > 0`:** the spin–spin contact interaction contributes to the
effective source with the opposite sign to the fermion energy density, so `ρ_eff` decreases
with increasing compression and passes through the value required by (2.4); because the
contact term's effective `ρ + 3p` is negative, `Ḣ > 0` there. The **explicit coefficient**
of the `s²` term in the ECSK Friedmann equation (the "−(πG/c⁴)s²"-type expression) is
**[UNVERIFIED — not stated here]**: it does not appear in either abstract and I did not
verify it from the full text this session. The negative sign of `Ω_S` and the bounce scale
`ε ~ n²/m_Pl²` above *are* verified and are all this memo asserts. See also W5's
parent–child bookkeeping memo and W2's bibliography for the fuller ECSK reference set.

### 5.3 The ECH mechanism as committed in P1N — quoted, not re-derived

From `arxiv/paper1bc_ech_note/main.tex` (abstract): "Popławski's Einstein–Cartan black-hole
cosmology replaces the classical singularity with a torsion-supported bounce: eliminating
the non-propagating spin connection from the minimal Einstein–Cartan–Holst (ECH) action
generates a spin–spin four-fermion contact term that, in the Einstein–Cartan limit
γ → ∞, reduces to the Hehl–Datta term underlying that bounce mechanism."

And from `main.tex` §"The Contact Term: Same Mechanism as the Bounce", the paper's own
sign-of-pressure statement: "writing the contact term's contribution to the effective stress
tensor as ρ_4ψ = −L_4ψ, p_4ψ = L_4ψ for a term with no explicit time derivatives, a
repulsive (halts collapse) contact interaction requires ρ_4ψ + 3p_4ψ < 0, i.e. 2L_4ψ < 0,
i.e. L_4ψ < 0", which Eq. (4fermi)'s coefficient `−(3κ/16)γ²/(1+γ²) < 0` supplies "whenever
J⁵ is normalized spacelike ... the case realized by a spin-aligned fermion ensemble's axial
current in the nonrelativistic, high-spin-density regime."

**What produces `H = 0` with `Ḣ > 0`:** exactly the `ρ + 3p < 0` condition of §2.2, supplied
by the four-fermion contact term with the sign established above. Note that P1N states this
sign result for the stated regime only and explicitly declines to claim it "for a general
(e.g. boosted or oscillating) J⁵ configuration". Note also P1N's scope: the paper's result
is that this same term **cannot** source late-time dark energy — so the ECH sector is a
bounce mechanism and is not available as a fate mechanism. That is directly relevant here:
**BigBounce's own committed result forbids using ECH torsion to drive a turnaround.**

### 5.4 Loop quantum cosmology — effective dynamics

The LQC effective Friedmann equation is

```
    H² = (8πG/3) ρ ( 1 − ρ/ρ_c ) ,      ρ_c = 3/(κ γ² λ²) ≈ 0.41 ρ_Pl               (5.1)
```

**Verification status:** Ashtekar & Singh, *Loop Quantum Cosmology: A Status Report*,
arXiv:1108.0893, Class. Quantum Grav. **28**, 213001 (2011) — title, authors and journal
verified 2026-09-18; the equation and the numerical value of ρ_c are **not** in the abstract
and I could not extract them from the article body this session. The form (5.1) together
with `ρ_c = 3/(κγ²λ²) ≈ 0.41 ρ_Planck` was verified verbatim from the arXiv HTML of
arXiv:1307.5527 (*Loop Quantum Cosmology and the Fine Structure Constant*), a secondary
source; Ashtekar, Pawlowski & Singh, *Quantum Nature of the Big Bang: Improved dynamics*,
arXiv:gr-qc/0607039, Phys. Rev. D **74**, 084003 (2006), abstract verified, states only the
qualitative version — with the improved Hamiltonian constraint the bounce "occurs only at a
Planck-scale density". **Treat the numeral 0.41 as verified-secondary, not
verified-primary**, pending a full-text check.

**What produces `H = 0` with `Ḣ > 0`:** directly from (5.1), H = 0 at ρ = ρ_c. Differentiate
(5.1) and use the (unmodified) continuity equation `ρ̇ = −3H(ρ+p)`:

```
    2HḢ = (8πG/3) ρ̇ (1 − 2ρ/ρ_c)  =  −8πG H (ρ+p)(1 − 2ρ/ρ_c)
    ⇒ Ḣ = −4πG (ρ+p)(1 − 2ρ/ρ_c)                                                   (5.2)
    ⇒ at ρ = ρ_c :  Ḣ = +4πG (ρ+p) > 0   for any NEC-satisfying matter.             (5.3)
```

So the bounce is generic in this effective description: no negative-energy component and no
energy-condition violation by the *matter* is needed — the quantum-geometry `−ρ²/ρ_c` term
does the work. Dimensional check of (5.2): `[Gρ] = s⁻²` and `Ḣ` has units s⁻² ✓.

### 5.5 Summary of the chain

```
   fate problem          →  singularity problem   →  inheritance problem  →  observability
   (does H reach 0       )  (does contraction     )  (what survives       )  (is any of it
   (with ä < 0?  §2–§4   )  (end in a bounce? §5  )  (the bounce? W4/W5   )  (measurable?)
```

Each arrow is a *non*-implication. Resolving one says nothing about the next. In
particular, a Crunch does **not** imply a Bounce, and a Bounce mechanism (LQC, ECSK, ECH)
does **not** imply that our universe will ever Crunch — the mechanisms live at ρ ~ ρ_Pl and
are utterly irrelevant at the ρ ~ 10⁻²⁷ kg m⁻³ scale where the fate question is decided.

---

## 6. The historical `M_crit = Λc²r³/(3G)` relation

### 6.1 Derivation (Newtonian limit with Λ)

In the weak-field, slow-motion limit of GR with a cosmological constant, the acceleration of
a test particle at radius r from a spherical mass M is

```
    r̈ = − GM/r²  +  (Λc²/3) r                                                       (6.1)
```

(the second term is the Newtonian limit of the Λ contribution; standard result). Dimensional
check: `[GM/r²] = m³kg⁻¹s⁻² · kg / m² = m s⁻²` ✓; `[Λc²r/3] = m⁻² · m²s⁻² · m = m s⁻²` ✓.

The **zero-acceleration radius** — the largest radius at which a shell can be held back by
M against the Λ repulsion, i.e. the maximum turnaround radius — is

```
    GM/r² = (Λc²/3) r   ⇒   r_ta = ( 3GM / (Λc²) )^{1/3}                            (6.2)
```

and rearranging (6.2) gives the historical form exactly:

```
    M = Λ c² r³ / (3G)     ≡  the 2025 notes' "M_crit"                              (6.3)
```

**Verification:** Pavlidou & Tomaras, *Where the world stands still: turnaround as a strong
test of ΛCDM cosmology*, arXiv:1310.1920, JCAP (2014) — abstract verified 2026-09-18: the
maximum turnaround radius is `(3GM/Λc²)^{1/3}`, "independently of cosmic epoch, dark matter
properties, or baryonic effects."

### 6.2 What it means and the numbers

It is a **local structure statement**: the largest radius at which a bound object of mass M
can still be turning around against the accelerating background. It is a sharp ΛCDM test at
the scale of groups and clusters. It says **nothing whatsoever about global dynamics**.

With Λ from the memo's reference cosmology (`Λ = 3Ω_Λ H₀²/c²` with H₀ = 67.4 km/s/Mpc,
Ω_Λ = 0.685, giving `Λ = 1.090911 × 10⁻⁵² m⁻²`), script section `C`:

| M | r_ta |
|---|---|
| 10¹² M_☉ (Milky-Way-scale halo) | **1.1139 Mpc** (3.4372 × 10²² m) |
| 10¹⁴ M_☉ (group / poor cluster) | **5.1703 Mpc** (1.5954 × 10²³ m) |
| 10¹⁵ M_☉ (rich cluster) | **11.1391 Mpc** (3.4372 × 10²³ m) |

(The script round-trips each row through (6.3) and recovers the input mass to 5 significant
figures, as an internal consistency check.)

### 6.3 Why the 2025 reading — "critical mass for universal collapse" — is wrong

Three independent reasons, the third of which appears to be new to this repo:

1. **Wrong equation.** Global fate is governed by (2.1)/(2.2) applied to the *homogeneous*
   background, not by (6.1) applied to a *local* overdensity. Equation (6.1) is a
   Newtonian two-body-plus-Λ problem in an asymptotically de Sitter background; it presumes
   the background it is embedded in and cannot reverse it.
2. **Wrong conclusion even on its own terms.** As §3(a) proves, with Λ > 0 constant and
   k = 0 the Friedmann equation admits no zero of H at any a. There is no mass "large
   enough" because there is no global turnaround condition to satisfy.
3. **The criterion, applied globally, is not a fate condition at all — it is the
   deceleration condition.** Apply `M_encl > Λc²r³/(3G)` to a homogeneous sphere of the
   actual universe, `M_encl = (4π/3) ρ_m r³`. The r³ cancels identically and the inequality
   reduces to

   ```
       ρ_m > Λc²/(4πG) = 2 ρ_Λ        (with ρ_Λ ≡ Λc²/(8πG))                        (6.4)
   ```

   which is exactly the condition for `ä < 0` from (2.2) with `p_Λ = −ρ_Λc²`:
   `ä/a = −(4πG/3)(ρ_m − 2ρ_Λ)`. In terms of density parameters, `Ω_m(1+z)³ > 2Ω_Λ`, i.e.
   (script section `D`) `1+z > 1.6323`, **z > 0.6323**. So the universe *did* satisfy the
   historical `M_crit` inequality — at every redshift above ≈ 0.63 — and it still never
   recollapsed. The relation diagnoses the sign of ä, not the fate. That is the precise
   sense in which the 2025 note was "not entirely nonsense but misinterpreted": it had hold
   of the deceleration/turnaround *scale*, and read it as a *destiny*.

### 6.4 Recommendation: retire the symbol `M_crit` permanently

Per the director's corrections, this repo already carries **three unrelated historical
meanings** of `M_crit`:

1. the Notion-era `Λc²r³/(3G)` (this section — correctly the **maximum turnaround radius**
   relation, best written as `r_ta`, never as a mass threshold);
2. the retired parent-black-hole threshold `(M_Pl⁴/ρ_vac)^{1/3} ≈ 10⁻³ M_☉` in
   `research/paper_1_01_archive/`;
3. a Horndeski braiding scale in `research/branch_I_bounce_compatible_DE/`.

**Recommendation: never reuse the symbol `M_crit` in any BigBounce artifact.** Use `r_ta`
(or `R_ta,max`) for the Pavlidou–Tomaras scale, and give the other two explicit
subscripted names at their point of use. A grep-level symbol audit across the repo is W1's
lane; this memo supplies the physics ruling on meaning (1).

---

## 7. `P_crit`

**No coherent historical definition of `P_crit` exists.** This memo finds no derivation, no
defining equation, and no dimensionally consistent usage for the symbol in any material
reviewed here; W1's repo-and-git-history source map is the authority on whether any buried
source contains one, and the expectation stated in the campaign inputs is that it does not.
Until W1 produces a derivation, `P_crit` must be treated as a name without a referent and
must not be reconstructed, "fixed", or assigned a value.

The historical usage appears to have blended at least four distinct quantities: a mass
threshold (`M_crit`, §6), the LQC bounce density, the Planck density/curvature scale, and
an "pressure" in the ICBP/QGBW brainstorming. The **correct, model-specific** thresholds,
each of which is well defined and none of which is universal, are:

| Threshold | Where it is defined | Status here |
|---|---|---|
| `ρ_c = 3/(κγ²λ²) ≈ 0.41 ρ_Pl` | LQC effective dynamics, Eq. (5.1) | Verified-secondary (§5.4) |
| torsion / spin-density bounce scale, `ε ~ n²/m_Pl²` | ECSK, Popławski arXiv:1105.6127 | Verified from abstract (§5.2) |
| curvature invariants (`R`, Kretschmann `K`) | any nonsingular-completion criterion | Standard |
| `ρ_tot(a_t) = 3kc²/(8πG a_t²)` | the *turnaround* density, Eq. (2.4) | Derived here |

Note that the last row is the only one relevant to the fate problem and it is ~120 orders of
magnitude below the first two. Conflating them is precisely the error §5 exists to prevent.

---

## 8. Cosmic reproduction fate tree (taxonomy, not probabilities)

No branch is assigned a likelihood. Ordering is arbitrary. "Relation to BigBounce" means
*relation to results already committed in this repo*, not to aspirations.

### Branch A — eternal expansion / heat death, no daughter mechanism
* **Required physics:** flat (or open) geometry with a positive asymptotic dark-energy
  floor; no nonsingular black-hole interior that produces a causally disconnected region.
* **Current constraints:** fully consistent with everything measured. It is the default
  reading of flat ΛCDM (§3a).
* **Falsifiability:** the cosmological half is testable *only* through the dark-energy
  sector — detect a future-crossing potential and Branch A is out. The "no daughter
  mechanism" half is not observationally testable from inside.
* **Unknowns:** the actual asymptotic behaviour of ρ_DE; black-hole interior physics.
* **Relation to BigBounce:** the null baseline. Every fate claim must beat this branch.

### Branch B — eternal expansion **plus** local black-hole daughter universes
* **Required physics:** a nonsingular black-hole interior that opens into a causally
  disconnected expanding region (ECSK/Popławski-type; Popławski, *Universe in a black hole
  in Einstein-Cartan gravity*, arXiv:1410.3881, ApJ **832**, 96 (2016) — abstract verified:
  matter "bounce[s] at finite density and expand[s] into a new spacetime region, functioning
  as a nonsingular closed universe").
* **Current constraints:** the parent-universe cosmology is unconstrained by this branch —
  that is the point. The specific *inherited-observable* route in this repo is **closed**:
  the rotating-parent spin-axis prediction is excluded against DESI A95
  (`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`).
* **Falsifiability:** poor from inside the daughter. Only inherited-observable signatures
  are testable, and the one this repo tested is a null.
* **Unknowns:** mass/energy/entropy bookkeeping across the interior — W5's lane.
* **Relation to BigBounce:** heat death of *our* expansion would not exclude this branch.
  That is a genuine logical point (it is the salvageable core of the 2025 "hope after the
  Big Freeze" idea) and it is **not evidence for anything**.

### Branch C — global turnaround → Crunch → classical singularity
* **Required physics:** one of §3(b)–(e) to produce the turnaround, *plus* the classical
  singularity theorems holding all the way down (§5.1) — i.e. no ECSK, no LQC, no quantum
  gravity effect that violates the relevant energy condition at ρ ~ ρ_Pl.
* **Current constraints:** the turnaround half is unconstrained-but-unsupported (§4.3). The
  singularity half is in tension with essentially every candidate quantum-gravity
  completion, which is the interesting part: Branch C requires *nothing new* at the Planck
  scale.
* **Falsifiability:** the turnaround half is falsifiable through the DE sector; the
  singularity half is not.
* **Unknowns:** Planck-scale physics.
* **Relation to BigBounce:** this is the branch a bounce programme must argue *against* if
  a Crunch ever occurs.

### Branch D — global turnaround → contraction → **nonsingular bounce** → new expansion
* **Required physics:** both a turnaround mechanism (§3) **and** an independent bounce
  mechanism (§5). The two must be supplied by different sectors. In this repo, P1N's result
  makes the pairing harder, not easier: the ECH contact term supplies the bounce and is
  shown not to supply late-time acceleration, so it cannot also supply the turnaround.
* **Current constraints:** same as C for the turnaround half; the bounce half is unconstrained
  at present (ρ ~ ρ_Pl is unreachable).
* **Falsifiability:** only through the turnaround half, and through whatever survives the
  bounce (the inheritance problem — W4/W5).
* **Unknowns:** everything about the inheritance problem.
* **Relation to BigBounce:** this is the branch Houston's motivating picture lives in. It
  requires **two** independent pieces of new physics, and the repo's own committed result
  (P1N) removes the most obvious way to get them from one mechanism. That is a cost, and
  stating it is the point of this memo.

### Branch E — other model-specific endpoints
Big Rip (§3f, phantom); "little rip"/pseudo-rip variants; a de Sitter phase followed by a
vacuum-decay transition to a different vacuum; cyclic/ekpyrotic constructions with their own
turnaround mechanism. Each has its own required physics and constraints; none is analysed
here. Listed so the taxonomy is exhaustive rather than a false dichotomy.

---

## 9. Answers to the dump's synthesis questions (§18), ≤ 4 sentences each

**Q1 — Can our universe Crunch despite accelerating?**
Not under flat ΛCDM with a constant positive Λ: H² is bounded below by Λc²/3 > 0, so a
turnaround is impossible, not merely improbable (§3a). It can Crunch only if the
dark-energy density eventually goes to zero and through it — which requires dark energy to
be dynamical, not a constant. Positive curvature does not help: at Ω_m < 1 no positive Λ
permits recollapse at any curvature (Eq. 3.5). So the honest answer is "only if dark energy
is not Λ", and nothing currently measured says it isn't.

**Q2 — What physical changes are required?**
Exactly one thing, in one of several disguises: the total energy density must be able to
reach the value `3kc²/(8πG a_t²)` (Eq. 2.4), which for k ≤ 0 means reaching zero, which
means some component must carry negative energy density. Concretely: a negative
cosmological constant, a scalar potential that crosses zero (Eq. 3.7), an interaction that
drains the effective DE density through zero, or a modified-gravity effective source that
does the same. The second condition, `ρ + 3p > 0` at the turnaround, then comes for free in
the canonical-scalar case (Eq. 3.8). Nothing else in the Friedmann system can be adjusted to
produce a turnaround.

**Q3 — What do September 2026 observations permit?**
DESI DR2 BAO (arXiv:2503.14738) and the DR2 Lyα full-shape analysis (arXiv:2607.27410)
both prefer evolving dark energy over ΛCDM at the 2.7–4.2σ level depending on the dataset
combination, with the newest Lyα central value shifting *toward* ΛCDM at substantially
smaller uncertainty. None of this implies, forecasts, or favours a future turnaround;
extrapolating the CPL fit to a → ∞ is invalid, and taken literally it does not even produce
a Crunch (Eq. 4.1 gives ρ_DE → 0⁺ for w_a < 0). Data exclude the pure flat-negative-Λ model
and all positive-Λ closed recollapse at the observed Ω_m, and are silent about
future-crossing quintessence. A model-independent "probability of a Crunch" is not a
computable quantity.

**Q4 — Does Crunch imply Bounce?**
No. Classical GR with ordinary matter in a contracting FLRW universe satisfies the
hypotheses of the singularity theorems and ends in a singularity (§5.1). A bounce requires
`ρ + 3p < 0` at H = 0, which is the exact sign-reverse of the condition (2.5) that made the
turnaround a turnaround — the fate problem supplies no reason for it to flip. Crunch and
Bounce are independent problems at densities separated by ~120 orders of magnitude.

**Q5 — Which nonsingular mechanisms could convert one to the other?**
ECSK spin–torsion (Popławski arXiv:1007.0587, arXiv:1105.6127: torsion-induced repulsion in
fermionic matter, bounce at ε ~ n²/m_Pl²); the ECH contact term as committed in P1N, whose
repulsive sign is established for a spin-aligned fermion ensemble; and LQC effective
dynamics, where `H² = (8πG/3)ρ(1−ρ/ρ_c)` gives H = 0 at ρ = ρ_c and `Ḣ = +4πG(ρ+p) > 0`
there (Eq. 5.3) for any NEC-satisfying matter. Each is a Planck-density mechanism and is
irrelevant to whether the Crunch happens in the first place. Note the repo-internal
constraint: P1N's own result is that the ECH term cannot source late-time acceleration, so
it cannot double as the turnaround mechanism.

**Q12 — Was the historical `M_crit` meaningful?**
The *relation* was: `M = Λc²r³/(3G)` inverts to `r_ta = (3GM/Λc²)^{1/3}`, the established
maximum-turnaround-radius scale (Pavlidou & Tomaras, arXiv:1310.1920) — 1.11 Mpc for
10¹² M_☉, 11.14 Mpc for 10¹⁵ M_☉. The *interpretation* ("critical mass to initiate
universal collapse") was wrong, because it applies a local Newtonian-plus-Λ condition to a
global question whose governing equation admits no solution at all for Λ > 0, k = 0.
Applied to a homogeneous sphere the criterion reduces identically to `ρ_m > 2ρ_Λ`, i.e. the
condition for `ä < 0`, satisfied by the real universe at all z > 0.6323 without any
recollapse. Verdict: salvage the relation as `r_ta`, retire the symbol `M_crit` and the
interpretation.

**Q13 — Did `P_crit` ever exist coherently?**
No coherent definition is recoverable, and none should be manufactured (§7). The historical
usage appears to conflate a mass threshold, the LQC bounce density, the Planck scale, and an
ad hoc pressure ansatz. Model-specific, well-defined substitutes exist — `ρ_c` in LQC, the
spin/torsion density scale in ECSK, curvature invariants generally, and the turnaround
density (2.4) for the fate problem — and should be used by name instead. W1's source map is
the final authority on whether a buried derivation exists; absent one, `P_crit` is retired.

---

## 10. Open questions this memo leaves, and whether anything new is falsifiable

**Candidate ledger item text (≤ 3 lines), for `project-context/NEXT_SCIENCE_LEDGER.md`:**

> **Cosmic fate under bounce-compatible dark energy.** For the DE classes Branch I finds
> bounce-compatible, determine which admit a future turnaround (ρ_DE crossing zero), and
> whether any *present-day* observable distinguishes them from ΛCDM at DESI DR2 precision.
> Open question / literature + derivation lane; no paper unless a present-day discriminant
> is found.

**Other open questions, recorded honestly:**

1. Is there any DE model that is simultaneously (i) bounce-compatible in Branch I's sense,
   (ii) future-turnaround-producing, and (iii) distinguishable from ΛCDM today? The
   intersection may be empty; that would itself be worth writing down.
2. The `0.41 ρ_Pl` LQC value needs a primary-source verification (§5.4).
3. The explicit `s²` coefficient in the ECSK Friedmann equation needs full-text
   verification before it is ever written into a BigBounce artifact (§5.2).
4. What is the observational reach of `r_ta` as a ΛCDM test in current group/cluster
   catalogs? This is a *present-day* test and therefore the only genuinely data-facing
   thread in this memo — and it is Pavlidou & Tomaras's programme, not a new idea.

**Does any of this yield a NEW falsifiable prediction not already tested by BigBounce?**

**None currently.** Every fate branch differs from ΛCDM only in an epoch we cannot observe;
the discriminating information lives entirely in the present-day dark-energy sector, which
DESI already measures and which BigBounce does not currently improve on. The one
present-day handle surfaced here — the maximum-turnaround-radius test (§6) — is an existing
published ΛCDM test, not a bounce prediction, and it constrains Λ rather than the fate. The
honest statement is that §1–§9 clear away three wrong claims and a symbol collision, and
produce no new prediction.

---

## References

**Verified by direct arXiv-abstract fetch during this session (2026-09-18) by W3:**

1. DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations
   and Cosmological Constraints*, arXiv:2503.14738 (2025).
2. DESI Collaboration, *DESI DR2 Results IV: Alcock-Paczyński Measurements from the Lyman
   Alpha Forest and Cosmological Constraints*, arXiv:2607.27410 (2026).
3. Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters*,
   arXiv:1807.06209; A&A **641**, A6 (2020).
4. V. Pavlidou & T. N. Tomaras, *Where the world stands still: turnaround as a strong test
   of ΛCDM cosmology*, arXiv:1310.1920; JCAP (2014).
5. R. Kallosh & A. Linde, *Dark Energy and the Fate of the Universe*, arXiv:astro-ph/0301087;
   JCAP **0302**:002 (2003).
6. R. Kallosh, J. Kratochvil, A. Linde, E. V. Linder & M. Shmakova, *Observational Bounds on
   Cosmic Doomsday*, arXiv:astro-ph/0307185 (2003).
7. J. Garriga, L. Pogosian & T. Vachaspati, *Forecasting Cosmic Doomsday from CMB/LSS
   Cross-Correlations*, arXiv:astro-ph/0311412; Phys. Rev. D **69**, 063511 (2004).
   [= the dump's citation [3], resolved]
8. R. R. Caldwell, M. Kamionkowski & N. N. Weinberg, *Phantom Energy and Cosmic Doomsday*,
   arXiv:astro-ph/0302506; Phys. Rev. Lett. **91**, 071301 (2003).
9. N. J. Popławski, *Cosmology with torsion: An alternative to cosmic inflation*,
   arXiv:1007.0587; Phys. Lett. B **694**, 181 (2010) [Erratum B **701**, 672 (2011)].
10. N. J. Popławski, *Big bounce from spin and torsion*, arXiv:1105.6127;
    Gen. Relativ. Gravit. **44**, 1007 (2012).
11. N. J. Popławski, *Universe in a black hole in Einstein-Cartan gravity*, arXiv:1410.3881;
    Astrophys. J. **832**, 96 (2016).
12. A. Ashtekar & P. Singh, *Loop Quantum Cosmology: A Status Report*, arXiv:1108.0893;
    Class. Quantum Grav. **28**, 213001 (2011). *(Bibliographic data verified; the
    ρ_c ≈ 0.41 ρ_Pl numeral was NOT verified from this source — see §5.4.)*
13. A. Ashtekar, T. Pawlowski & P. Singh, *Quantum Nature of the Big Bang: Improved
    dynamics*, arXiv:gr-qc/0607039; Phys. Rev. D **74**, 084003 (2006).
14. A. P. Lundgren, M. Bondarescu & R. Bondarescu, *Depressing de Sitter in the Frozen
    Future*, arXiv:1201.1298 (2012). [= the dump's citation [2], resolved]

**Verified-secondary (HTML full text fetched, but a review/secondary source):**

15. arXiv:1307.5527, *Loop Quantum Cosmology and the Fine Structure Constant* — used solely
    to verify the written form `ρ_c = 3/(κγ²λ²) ≈ 0.41 ρ_Planck` and Eq. (5.1). Flagged in
    §5.4; not to be used as the citation of record.

**Cited as standard textbook material (no arXiv record; stated as textbook, not as a claim):**

16. Friedmann and Raychaudhuri equations, Eqs. (2.1)–(2.2): any GR/cosmology text.
17. Hawking–Penrose singularity theorems, §5.1 (qualitative use only): Hawking & Ellis,
    *The Large Scale Structure of Space-Time* (1973), Ch. 8.

**Cross-references to campaign siblings:** W2's
`research/archaeology_2025/bibliography/VERIFIED_BIBLIOGRAPHY.md` and
`archaeology_2025.bib` are the campaign's bibliography of record and agree with items 1–14
above where they overlap. The dump's citation [11] (a NASA press page on spiralling
supermassive black holes) is **not used here for anything**, per W2's instruction.

**Repo cross-references:** `research/branch_I_bounce_compatible_DE/*`;
`arxiv/paper1bc_ech_note/main.tex`;
`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`;
`research/archaeology_2025/outputs/cosmic_fate_turnaround_2026_09_18.py` (+ `.json`).
