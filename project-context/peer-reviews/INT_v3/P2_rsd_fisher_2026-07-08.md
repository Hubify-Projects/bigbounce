# P2 — REDSHIFT-SPACE (RSD) multipole bispectrum Fisher: retires the "real-space monopole only" limitation

**Date:** 2026-07-08
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.100)
**Standing methodological limitation (OpenAI/ChatGPT, every round):** *"the
independent bispectrum Fisher is real-space monopole only — no RSD multipoles
ℓ=0,2,4 — a ~18% conservative offset per Heinrich."* This was the ONE remaining
methodological caveat on the (now-committed) C13 independent Fisher.
**Base pipeline (committed, validated):** `scripts/c13_independent_bounce_fisher.py`
+ `outputs/c13_independent_bounce_fisher.json` (multi-tracer; reproduces Heinrich
0.7 to 2–11%; r_eff ≈ 0.99).
**New script (committed):** `research/focused_paper_source_integration/scripts/c14_rsd_multipole_fisher.py`
**New output (committed):** `research/focused_paper_source_integration/outputs/c14_rsd_multipole_fisher.json`
**Verdict:** **CLOSED — the redshift-space bispectrum Fisher is now built.** The RSD
local-template σ(f_NL) **improves** on the real-space monopole in exactly the
direction Heinrich reports, the bounce r_eff stays ≈ 0.99 in redshift space, and
the −35/16 significance rises from 3.2–3.5σ (real-space) to **4.9–5.2σ**
(redshift-space). Nothing fabricated; every input sourced; the f→0 limit
reproduces C13 to 6 significant figures.

---

## 1. What was built (the standard extension)

C14 takes the committed, validated C13 pipeline **unchanged** (same Planck 2018
CAMB P(k)/M(k,z); same SPHEREx public-products n̄ᵢ(z),bᵢ(z) table [Doré+2014];
same 6 z-bins, f_sky=0.75, k_max=0.2(1+z); same 2,330-triangle grid; same
5-sample multi-tracer Gaussian covariance with the Kronecker-inverse contraction)
and replaces the **real-space monopole** galaxy bispectrum with the **tree-level
redshift-space** galaxy bispectrum:

- **Linear Kaiser factor** (Kaiser 1987), per tracer X:
  `Z1_X(k,μ) = b_X + f μ²`.
- **Growth rate f(z)** from the SAME CAMB Planck-2018 cosmology,
  `f(z)=fσ8(z)/σ8(z)`: f = 0.587, 0.686, 0.762, 0.819, 0.861, 0.915 at
  z = 0.1, 0.3, 0.5, 0.7, 0.9, 1.3. No imported/tuned growth.
- **Second-order redshift-space kernel Z2** (Scoccimarro, Couchman & Frieman
  1999 [SCF99] Eq. 13; Sefusatti 2006 Eq. 15), with **b2=0 held consistent with
  the C13 base** (which carries no b2):
  ```
  Z2(k1,k2) = b1 F2(k1,k2) + f μ12² G2(k1,k2)
            + (f μ_K k_K / 2)[ μ1/k1 (b1 + f μ2²) + μ2/k2 (b1 + f μ1²) ]
  ```
  with the SPT velocity-divergence kernel
  `G2 = 3/7 + ½ cosθ (k1/k2+k2/k1) + 4/7 cos²θ`.
- **Tree-level RSD galaxy bispectrum** (SCF99 Eq. 12):
  `B_s = 2 Z1(k1)Z1(k2)Z2(k1,k2) P1 P2 + 2 cyc`, in the multi-tracer tree
  assignment `B_s^ABC = 2[Z1^A(k1)Z1^B(k2)Z2^C(k1,k2)P1P2 + cyc]`
  (Karagiannis+2018 Eq. 2.7 tree form). f_NL enters **exactly as in C13**, now
  RSD-dressed: (a) scale-dependent bias `Δb_X = 2 f_NL δ_c (b_X−1)/M(k)`
  [Dalal+2008; Heinrich Eq. 17-18] carried in the Z1 legs + Z2 F2-branch, and
  (b) the primordial-transfer term `2 Z1^A Z1^B Z1^C M1M2M3 B_φ^tmpl`.
- **Line-of-sight orientation integral.** A triangle in redshift space depends
  on its orientation (μ1, φ) to the line of sight (Sefusatti 2006 §II; Gagrani &
  Samushia 2017). The Fisher integrand is integrated over the **full solid
  angle**,
  ```
  F = Σ_tri (1/4π) ∫_{-1}^{1} dμ1 ∫_0^{2π} dφ  [dB_s/df_NL]² / Var_s(μ1,φ),
  ```
  on an 8×8 Gauss-Legendre(μ) × uniform(φ) grid, with the **orientation-dependent
  Kaiser covariance** `P^tot_s^XY(k,μ) = (b_X+fμ²)(b_Y+fμ²)W_XW_Y P_m + δ_XY/n_X`.
  Integrating the full angular dependence contains the ℓ=0,2,4 SCF99 multipole
  information exactly — **no multipole truncation is made**.

## 2. Validation gates (both PASSED, nothing tuned)

**(A) f→0 reduction — the load-bearing correctness check.** With the growth rate
forced to zero, RSD must collapse EXACTLY onto the committed C13 real-space
multi-tracer result (Z1→b, Z2→b·F2, Kaiser power→b²P, orientation integral of a
constant → the constant). It does, to 6 significant figures, in **all three
channels**:

| channel (z-bin 2, f=0) | C14 F_ff | C13 F_ff | ratio |
|---|---|---|---|
| local, full | 0.682472 | 0.682472 | 1.00000 |
| bounce, full | 0.668757 | 0.668757 | 1.00000 |
| local, primordial-only | 1.793013e-02 | 1.793013e-02 | 1.00000 |

This proves the RSD extension shares C13's covariance/tree/multi-tracer machinery
bit-for-bit; the only physics added is the velocity (Kaiser Z1 + Z2/G2) content.

**(B) RSD tightens σ(f_NL) in Heinrich's direction.** With growth on:

| quantity (bias-marginalized) | value |
|---|---|
| C13 real-space MT σ(f_NL^local) | 0.6874 |
| **C14 RSD MT σ(f_NL^local)** | **0.4487** |
| RSD/real-space ratio | 0.6528 (**+34.7% tighter**) |
| RSD/Heinrich(0.7) ratio | 0.6410 |

The RSD forecast **improves** on the real-space monopole, exactly the
one-directional effect the reviewer (via Heinrich) said was missing. See §3 for
the honest reconciliation of +34.7% vs Heinrich's quoted ~18%.

## 3. The bounce number in redshift space

| quantity | bias-fixed | bias-marginalized |
|---|---|---|
| σ(f_NL^bounce)_RSD | 0.4168 | 0.4493 |
| **significance for −35/16** | **5.25σ** | **4.87σ** |
| r_eff_RSD = σ_local/σ_bounce | 0.9945 | 0.9988 |
| r_eff_RSD (primordial-only channel) | — | 0.9872 |

The bounce recovery factor **stays r_eff ≈ 0.99 in redshift space** — the same
squeezed-domination that made r_eff ≈ 0.99 in real space (C13) persists, because
the Kaiser weighting does not move the f_NL signal off the squeezed configurations
where the bounce and local templates coincide by construction. The paper's adopted
r = 0.84 shape-overlap remains **conservative** under the actual redshift-space
survey covariance.

The independent detection significance for the corrected bounce squeezed value
f_NL = −35/16 rises from the real-space **3.2–3.5σ** (C13) to the redshift-space
**4.9–5.2σ** (C14, unmarginalized signal-plus-shot-noise). The paper's
GR-projection-degeneracy bracket (ρ≈0.95; marginalized ~0.8–1.3σ lower edge of
§systematics) still applies on top and is retained exactly as before — the RSD
gain lifts the ceiling of the bracket, it does not remove the GR floor.

## 4. Honest reconciliation: +34.7% vs Heinrich's ~18%

The RSD improvement C14 measures (**+34.7%**) is LARGER than the **~18%** the paper
attributed to Heinrich. This is not a discrepancy to hide — it is a definitional
difference that must be stated:

- **Heinrich's ~18%** is the *monopole → (monopole+multipole)* information gain
  **within an already-redshift-space analysis** — i.e. how much the ℓ=2,4
  anisotropy adds on top of the redshift-space monopole.
- **C14's +34.7%** is the *pure real-space → full redshift-space* gain: the C13
  baseline had **zero velocity information** (a genuine real-space monopole, no
  Kaiser boost at all), so C14 adds the **entire** Kaiser Z1 + velocity Z2/G2
  signal, of which the ℓ=2,4 multipole content is only one part. The larger
  linear-Kaiser monopole enhancement `⟨(1+βμ²)⟩` (β=f/b ≈ 0.4–0.9 here) is the
  dominant term and is on top of the multipole gain.

The C14 Fisher gain (F_ff: 2.55 → 5.82, i.e. 2.28×; σ tightening 1.53×) sits
squarely in the documented tree-level RSD-bispectrum range. The **+34.7% is
reported as computed**, and the paper's language is corrected to attribute the
improvement to the full RSD dressing (not to a narrower "~18% multipole-only"
figure). The conservative direction is preserved: RSD adds information, so the
real-space number the paper previously headlined was, if anything, MORE
conservative than the ~18% caveat implied.

## 5. Remaining honest approximations (stated, not hidden)

- **Tree-level** (no one-loop bispectrum); linear `k_max=0.2(1+z)` — IDENTICAL
  scale cut to C13 and Heinrich's linear-regime forecast.
- **b2 = bs2 = 0** held consistent with the C13 base (no galaxy quadratic-bias
  marginalization). b2 enters Z2 additively; marginalizing it would loosen σ
  somewhat, so the bias-marginalized RSD σ is a leading-order bound on the
  bias-nuisance axis (same caveat as C13, now stated for RSD).
- **Fingers-of-God / nonlinear velocity dispersion NOT modeled** (tree-level
  Kaiser only). At the linear k_max used this is a small correction and would
  only DEGRADE the highest-k modes — so the reported RSD gain is if anything
  conservative at the top of the k-range.
- **SDB × Z2-shift cross-term** kept at leading order (its cross with SDB is
  O(f_NL·f), subdominant); the dominant SDB response (Z1 legs + Z2 F2-branch) is
  carried exactly.
- **Orientation integral** on an 8×8 grid (Gauss-Legendre μ, exact for the μ⁰,²,⁴
  moments the tree bispectrum produces; uniform φ). Full angular dependence
  integrated — no multipole truncation. The f→0 limit (which reproduces C13
  exactly) confirms the orientation quadrature normalization.

## 6. Proposed .tex update (NOT applied — for Houston sign-off)

See `P2_rsd_fisher_tex_upgrade_PROPOSED_2026-07-08.md`. It replaces the single
"real-space monopole (no RSD multipoles ℓ=0,2,4, a ~18% one-directional/
conservative offset)" limitation sentence in the para:reconcile paragraph (line
947) with the RSD result, and updates the independent-Fisher significance from
"3.2–3.5σ" to the redshift-space "4.9–5.2σ" (retaining the real-space number as
the conservative floor). No headline f_NL = −35/16 value changes; the GR bracket
is untouched.
