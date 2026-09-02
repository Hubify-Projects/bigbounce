# A3-1 — PBH abundance via the compaction-function criterion at f_NL = −35/16

**Date:** 2026-09-02 · **Ledger item:** `NEXT_SCIENCE_LEDGER.md` #3, open sub-item **A3-1**
· **Script:** `pbh_compaction_fnl.py` · **Outputs:** `outputs/pbh_compaction_fnl.{json,png}`
· **Manifest:** `reproducibility/manifests/experiments/a3-pbh-compaction-fnl.json`
· **Venue:** local (Apple M5), no GPU, cost **$0**, measured wall time **215 s**

This note **supersedes §2 of `A3_MULTICHANNEL_BRIEF_2026-09-02.md`** (the
Press–Schechter first pass in `pbh_abundance_fnl.py`). The first pass is kept on
disk as the record of what was computed; **its central conclusion is reversed
here.**

---

## 1. Why the first pass had to be redone

`pbh_abundance_fnl.py` applied Press–Schechter to the truncated local map
ζ = ζ_G + (3/5) f_NL (ζ_G² − σ²). For f_NL < 0 that map is a downward parabola in
ζ_G with an **absolute ceiling**

    ζ_max = −5/(12 f_NL) + (3/5)|f_NL| σ²   →   0.190 at −35/16,  0.0952 at −35/8

so β ≡ 0 identically at the standard curvature thresholds ζ_c ≈ 0.45–1. That
ceiling is an artefact of truncating the map at quadratic order, not physics.
The brief flagged this as the largest open item in Track A3.

The compaction function removes it. In the compaction formalism the quadratic
non-linearity appears in **C**, not in a bound on ζ: C is a downward parabola in
C_lin with maximum C_max = f(w) = 2/3 at C_lin = 2f(w) = 4/3, but the map
ζ_G → C_lin is unbounded because C_G is an unbounded Gaussian variable.
**Every threshold C_th < 2/3 is therefore reachable at every f_NL**, and there is
no ζ ceiling at all.

---

## 2. Setup

Followed from **Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025**, *"Negative
non-Gaussianity as a salvager for PBHs with PTAs in bounce"*, arXiv:2409.18983,
**EPJC 85:472** — equation numbers below are theirs, read from the published PDF on
2026-09-02. Companion formalism: Young, Byrnes & Sasaki 2019 (arXiv:1904.00984,
Eqs. 5–6, 17–18); Yoo, Harada, Garriga & Kohri 2018 (1805.03946); Yoo, Gong &
Yokoyama 2019 (1906.06790); Kehagias, Perrone & Riotto 2019 (1904.00970);
Ferrante, Franciolini, Iovino & Urbano 2023 (2211.01728); **Musco 2019**
(1809.02127) for the threshold.

### 2.1 Equations implemented

Compaction function on superhorizon scales, spherical symmetry [their Eq. 30;
identical to YBS19 Eq. 6], with f(w) = 3(1+w)/(5+3w) = **2/3** in radiation:

    C(r) = − f(w) r ζ′(r) [ 2 + r ζ′(r) ]

Peak condition [Eq. 31]: C′(r_p) = 0 ⟹ ζ′(r_p) + r_p ζ″(r_p) = 0. At the peak the
compaction equals the volume-averaged density contrast [Eq. 34], δ_p = C(r_p), so
the formation criterion is **C(r_p) > C_th**.

Local non-Gaussianity [Eq. 35] — the *same* map the first pass used:

    ζ = ζ_G + (3/5) f_NL (ζ_G² − ⟨ζ_G²⟩),      J ≡ dζ/dζ_G = 1 + (6/5) f_NL ζ_G

Compaction in Gaussian variables [Eq. 40], with C_G = −2 f(w) r ζ_G′(r):

    C = C_lin − C_lin² / (4 f(w)),      C_lin = C_G · J

Joint PDF of (C_G, ζ_G) [Eq. 49] with γ_cr = σ_cr²/(σ_c σ_r) [Eq. 50]:

    P_G = 1/(2π σ_c σ_r √(1−γ_cr²)) · exp[ −ζ_G²/(2σ_r²)
              − (C_G/σ_c − γ_cr ζ_G/σ_r)² / (2(1−γ_cr²)) ]

Covariance elements [Eqs. 52–54], with the **Gaussian** window W_g for C_G, the
spherical window W_s for ζ_G, and the radiation transfer function T(k,r_p)
[Eq. 48] applied to the spectrum [Eq. 56]:

    σ_c²  = 4 (f/3)² ∫ dk/k (k r_p)⁴ W_g² T² Δ²_ζ
    σ_r²  =           ∫ dk/k          W_s² T² Δ²_ζ
    σ_cr² = 2 (f/3)   ∫ dk/k (k r_p)² W_g W_s T² Δ²_ζ

    W_g = exp(−k²r²/2),  W_s = sin(kr)/(kr),  T = 3[sin x − x cos x]/x³, x = kr/√3

(Choudhury et al. state explicitly, under their Eq. 51, that they prefer the
Gaussian window to the top-hat.)

Mass fraction with critical scaling [Eq. 60], γ = 0.36 (RD critical exponent),
K ~ O(1–10):

    β_NG = ∫_D K (C − C_th)^γ P_G(C_G, ζ_G) dC_G dζ_G

Domain D [Eqs. 61, 63–65]: C ≥ C_th **and** C_lin ≤ 2f(w) (the compaction-maximum
condition, selecting **type-I** PBHs; type-II is "highly suppressed" and is
excluded, as they do). Solving C_th = C_lin − C_lin²/(4f) gives
C_lin,− = 2f(w)[1 − √(1 − C_th/f(w))], so type-I is C_lin ∈ [C_lin,−, 2f(w)]:

| C_th | C_lin,− | type-I upper 2f(w) | type-II boundary C_lin,+ |
|---|---|---|---|
| 0.4 | 0.490059 | 1.333333 | 2.176607 |
| 0.5 | 0.666667 | 1.333333 | 2.000000 |
| 0.6 | 0.911696 | 1.333333 | 1.754970 |

We integrate in **(ζ_G, C_lin)** rather than (ζ_G, C_G), with C_G = C_lin/J and
Jacobian dC_G = dC_lin/|J|. This is algebraically identical to their Eq. (65)
limits but numerically robust across the sign change of J at
ζ_G = −5/(6 f_NL), which is exactly their "two separate branches of domain
solutions" and which falls *inside* the bulk of the PDF at these amplitudes
(0.68 σ_r at −35/8, 1.36 σ_r at −35/16). The grid splices a dense patch around
that point.

Present abundance [Eq. 66], at a single horizon mass (deviation D3 below):

    f_PBH = (1/Ω_DM) (M_⊙/M_H)^{1/2} (g_*/106.75)^{3/4} (g_*s/106.75)^{−1}
            β_NG / 7.9×10⁻¹⁰,     Ω_DM = 0.674, g_* = g_*s = 106.75, M_H = 10²⁰ g

### 2.2 Threshold used — and its justification

**Baseline C_th = 0.5, scanned over {0.4, 0.5, 0.6}.** Musco 2019
(arXiv:1809.02127) established that the threshold is **shape-dependent**, running
over ≈ 0.4–0.6 in radiation domination across profile shapes; YBS19 quote
δ_c = 0.55 for a Gaussian profile. Choudhury et al. scan {0.4, 0.5, 0.6} for
precisely this reason and we follow them. All three lie below C_max = f(w) = 2/3,
which Eq. (64) requires (it needs 1 − C_th/f(w) ≥ 0).

### 2.3 Numerical validation

For f_NL = 0 the map is J = 1, the ζ_G direction integrates out exactly, and
Eq. (60) collapses to a one-dimensional quadrature over the marginal
C_G ~ N(0, σ_c). The 2-D grid reproduces it to better than 3%:

| A | β exact (1-D) | β grid (2-D) | ratio |
|---|---|---|---|
| 0.05 | 2.4755×10⁻⁴⁰ | 2.4141×10⁻⁴⁰ | 0.9752 |
| 0.1314 | 1.1880×10⁻¹⁶ | 1.1800×10⁻¹⁶ | 0.9933 |
| 0.2 | 1.3831×10⁻¹¹ | 1.3778×10⁻¹¹ | 0.9962 |

A separate check: doubling the grid in both directions moves β by ≤ 1.5%.
An earlier version of this script clipped log P at −700, which installs a
spurious ~10⁻³⁰⁴ probability floor and fabricates a non-zero β out of nothing;
that clip was removed and the underflow is allowed to go to zero.

---

## 3. Deviations from Choudhury et al. — stated, not hidden

**D1 (the one that matters).** Their Δ²_ζ is the *regularized–renormalized–
resummed* (RRR) one-loop spectrum of an EFT of non-singular bounce with a
contraction + bounce + SR-I + USR + SR-II mode history (their Eq. 55
decomposition, Sec. III B). **This is not reconstructible from the published
paper.** The paper describes the RRR construction but prints neither a
closed-form Δ²_ζ(k) nor the complete numerical parameter set needed to regenerate
it — the loop-counterterm normalisation, the tabulated EFT coefficients, and the
adopted (k_s, k_e, ΔN_USR) values are all absent from the text we could read.
**That is exactly what is missing, and it is the single ingredient we cannot
reproduce.** In its place this work uses the standard stand-in for a
USR-amplified peak, a lognormal
Δ²_ζ(k) = A/(√(2π)Δ) exp[−ln²(k/k_p)/(2Δ²)], with Δ scanned over {0.35, 0.5, 0.8},
and it **scans the amplitude A rather than adopting theirs**.

**D2.** r_p = 1/k_p (c_s = 1) rather than their r_p = 1/(c_s k_H) with
0.88 ≤ c_s ≤ 1; sensitivity to r_p k_p ∈ {0.75, 1.0, 1.5} is reported throughout.

**D3.** Their Eq. (66) integrates d ln M_H; we evaluate at the single
M_H = 10²⁰ g so the number is directly comparable to the first pass, which used
the same mass. For a narrow peak this is an O(1) width factor.

**D4.** K = 4 (mid-range of their O(1–10)). f_PBH is linear in K, so K cancels
exactly in every ratio quoted below.

**D5.** No g_NL, no loop corrections, c_s = 1 fixed.

---

## 4. Results

### 4.1 At the amplitude where the Gaussian case gives f_PBH = 1 (r_p k_p = 1, Δ = 0.5)

| C_th | A* | σ_c | σ_r | γ_cr | f_PBH (f_NL=0) | f_PBH (−35/16) | f_PBH (−35/8) |
|---|---|---|---|---|---|---|---|
| 0.4 | 0.07109 | 0.06036 | 0.2070 | 0.8877 | 1.000 | **5.82×10⁻²¹** | 4.50×10⁻⁷ |
| 0.5 | 0.13145 | 0.08208 | 0.2815 | 0.8877 | 1.000 | **3.62×10⁻¹⁴** | 1.57×10⁻² |
| 0.6 | 0.24622 | 0.11234 | 0.3852 | 0.8877 | 1.000 | **2.81×10⁻⁸** | 8.21×10¹ |

The perturbativity diagnostic 1.2 |f_NL| σ_r is **0.54–1.01 at −35/16 and
1.09–2.02 at −35/8**: at the amplitude PBH formation actually requires, the
quadratic truncation of the local map is *not* perturbatively controlled. This is
the same class of statement as Choudhury et al.'s own |f_NL| ≲ 60 perturbativity
bound, and it should be read as a limitation of the quadratic ansatz shared by
both papers, not as a defect of one of them.

### 4.2 The robust observable: amplitude required to reach the Choudhury+ band

f_PBH itself is exponentially sensitive to γ_cr (see §4.3), and γ_cr is set by the
spectrum shape — the ingredient D1 says we cannot reproduce. The **ratio of
required amplitudes** is not. Over a 27-point grid spanning Δ ∈ {0.35, 0.5, 0.8},
r_p k_p ∈ {0.75, 1.0, 1.5}, C_th ∈ {0.4, 0.5, 0.6} — i.e. **γ_cr ∈ [0.766, 0.968]** —
the amplitude A needed to reach f_PBH = 10⁻³ (the floor of their band) satisfies

> **A(−35/16) / A(−35/8) = 1.732, range [1.610, 1.809], std 0.050 (n = 27)**

i.e. **stable to ±6% while f_PBH itself moves by more than 100 decades.** K, Ω_DM,
g_*, and M_H all cancel in this ratio. This is the one number this channel
supports.

Representative rows (full grid in the JSON):

| Δ | r_p k_p | C_th | γ_cr | A(0) | A(−35/16) | A(−35/8) | ratio |
|---|---|---|---|---|---|---|---|
| 0.35 | 0.75 | 0.5 | 0.8965 | 0.1400 | 0.2456 | 0.1391 | 1.767 |
| 0.35 | 1.5 | 0.5 | 0.9675 | 0.0875 | 0.7601 | 0.4542 | 1.673 |
| 0.5 | 1.0 | 0.5 | 0.8877 | 0.1091 | 0.2120 | 0.1223 | 1.734 |
| 0.8 | 0.75 | 0.6 | 0.7660 | 0.3145 | 0.1833 | 0.1014 | 1.809 |
| 0.8 | 1.5 | 0.4 | 0.8567 | 0.0799 | 0.1567 | 0.0934 | 1.677 |

### 4.3 What is *not* robust: the sign of the effect relative to Gaussian

Recalibrating A at each point so the Gaussian case gives f_PBH = 1:

| Δ | r_p k_p | γ_cr | f_PBH(−35/16) | f_PBH(−35/8) |
|---|---|---|---|---|
| 0.8 | 0.75 | 0.7660 | 3.53×10³ | 2.20×10⁸ |
| 0.8 | 1.0 | 0.8078 | 3.39×10⁻¹ | 8.23×10⁵ |
| 0.5 | 0.75 | 0.8461 | 1.82×10⁻³ | 4.48×10⁴ |
| 0.8 | 1.5 | 0.8567 | 5.75×10⁻⁹ | 1.60×10¹ |
| 0.5 | 1.0 | 0.8877 | 3.62×10⁻¹⁴ | 1.57×10⁻² |
| 0.35 | 0.75 | 0.8965 | 1.67×10⁻¹¹ | 1.02×10⁰ |
| 0.35 | 1.0 | 0.9295 | 3.06×10⁻³² | 3.21×10⁻¹³ |
| 0.5 | 1.5 | 0.9340 | 5.27×10⁻⁴² | 1.78×10⁻¹⁹ |
| 0.35 | 1.5 | 0.9675 | 5.32×10⁻¹⁰⁷ | 7.03×10⁻⁵⁹ |

Negative f_NL **enhances** the abundance relative to Gaussian for γ_cr ≲ 0.85 and
**suppresses** it above; the crossover sits in the middle of the plausible range.
**But f_PBH(−35/8) > f_PBH(−35/16) at every single point.**

### 4.4 Why, and continuity in f_NL

At C_th = 0.5, r_p k_p = 1, A = A*:

| f_NL | 0 | −0.02 | −0.05 | −0.1 | −0.2 | −0.35 | −0.5 | −1 | −35/16 | −3 | −35/8 | −6 | −10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f_PBH | 1.00 | 2.4e−2 | 8.5e−6 | 2.7e−17 | 3.9e−47 | 7.5e−55 | 2.4e−50 | 4.1e−33 | 3.6e−14 | 3.1e−8 | 1.6e−2 | 8.9e+1 | 2.6e+6 |

Smooth, with a deep minimum near f_NL ≈ −0.35. The mechanism: γ_cr ≈ 0.89 is
large and positive, so in the Gaussian case the dominant contribution rides the
correlation ridge C_G/σ_c ≈ ζ_G/σ_r with **both variables positive**. As soon as
f_NL < 0, J = 1 + (6/5) f_NL ζ_G *shrinks* on that ridge (ζ_G > 0), so C_lin = C_G J
can no longer reach C_lin,−; the ridge is destroyed. The system is forced into the
anti-correlated quadrant (ζ_G < 0, C_G > 0) — which is exactly what Choudhury et
al. describe: *"For f_NL < 0, the domain is shown to align towards the
anti-correlated direction"* — at a large probability cost. Once there, a **larger**
|f_NL| buys more leverage in J per unit of ζ_G excursion, so the abundance recovers
monotonically with |f_NL|. Hence −35/8 always beats −35/16.

---

## 5. Comparison with the Press–Schechter first pass

| | first pass (Press–Schechter, quadratic map) | this work (compaction function) |
|---|---|---|
| f_PBH at −35/16 | **7.32×10⁻³** | 3.62×10⁻¹⁴ (C_th = 0.5, γ_cr = 0.888) |
| f_PBH at −35/8 | **3.75×10⁻⁶** | 1.57×10⁻² (same point) |
| ratio (−35/16)/(−35/8) | **1.95×10³** (−35/16 *larger*) | **2.3×10⁻¹²** (−35/16 *smaller*) |
| ζ ceiling | 0.190 / 0.0952 — β ≡ 0 at ζ_c ≈ 0.45–1 | **none** |
| reaches standard thresholds? | no | yes, at every f_NL |

**The first pass's central conclusion is reversed.** It reported that halving
|f_NL| from −35/8 to −35/16 *weakens the suppression by 3–10 orders of magnitude*
and that "the halved value is the one that sits in the sizeable-abundance band."
Under the compaction-function criterion the opposite holds: at fixed curvature
amplitude −35/16 produces **fewer** PBHs than −35/8, at every point of the
(Δ, r_p, C_th) grid, and it needs **1.73× more curvature amplitude** to reach the
same abundance.

The first pass's one analytic statement — that the quadratic-map ceiling
−5/(12 f_NL) exactly doubles from 0.0952 to 0.190 when |f_NL| is halved — remains
arithmetically correct but is now **without physical content**, because the
ceiling is an artefact of the truncation and the compaction criterion has no
ceiling at all. The A3 brief's §2.2 headline ("halving |f_NL| exactly doubles the
ceiling — the single sharpest thing this channel says") should be read as
superseded.

---

## 6. Agreement and disagreement with Choudhury et al. 2025

**Comparable, and it agrees — unforced.** At C_th = 0.5, Δ = 0.5, r_p k_p = 1 and
the Gaussian-calibrated amplitude, f_NL = −35/8 gives **f_PBH = 1.6×10⁻²**, inside
their reported band 10⁻³ ≤ f_PBH ≤ 1 for the same f_NL value. Nothing was tuned to
make that happen: A was fixed by requiring the *Gaussian* case to give f_PBH = 1,
and −35/8 landed in their band on its own. Their qualitative claim that a large
negative f_NL mitigates PBH overproduction (i.e. suppresses relative to Gaussian)
is reproduced here for γ_cr ≳ 0.85.

**Comparable, and it disagrees.** For γ_cr ≲ 0.85 our implementation of their
equations gives **enhancement**, not suppression, relative to the Gaussian case at
fixed amplitude (§4.3). We cannot tell whether their RRR spectrum sits above or
below that crossover, because of D1. This is recorded as a discrepancy, not
resolved.

**Not comparable at all.** Their absolute curvature amplitude, their c_s ∈
[0.88, 1], their SIGW fit to NANOGrav15/EPTA, and their |f_NL| ≳ −60 perturbativity
bound all depend on the RRR spectrum (D1). None of these is reproduced, and none
is contradicted, here.

**And note:** −35/16 does not appear in Choudhury et al. at all. They study
f_NL = (−39.95, −35/8). The −35/16 numbers in this note are new.

---

## 7. What this means for Track A3

The honest statement for the multi-channel brief, replacing §2.4:

- Under the compaction-function criterion, **negative f_NL of this magnitude is a
  large effect on PBH abundance, and the −35/16 vs −35/8 difference is a factor
  1.73 ± 0.10 in required curvature amplitude** — equivalently many decades in
  f_PBH at fixed amplitude. The channel *is* sensitive to which value is right.
- **The direction is opposite to what the first pass reported.** −35/16 is the
  *more* PBH-suppressing value at fixed amplitude, not the less.
- **The channel cannot yet be turned into a constraint**, because the absolute
  f_PBH depends exponentially on γ_cr, which is fixed by the curvature spectrum
  shape. Closing that needs a bounce curvature spectrum computed in this lab, not
  a lognormal stand-in — which is the same prerequisite as open item **A3-3**
  (propagating the matter-bounce scalar spectrum through the SIGW kernel).
  A3-1 and A3-3 should therefore be done together.
- Ledger item **#1** (the independent −35/16 derivation) still gates the
  scientific content: it decides which column of §4.2 is the prediction.

---

## 8. Open items created or updated by this note

| # | item | status |
|---|---|---|
| A3-1 | compaction-function redo at −35/16 | **CLOSED** by this note; first-pass conclusion reversed |
| A3-1b | **NEW** — obtain the matter-bounce curvature spectrum Δ²_ζ(k) in-lab so γ_cr is predicted rather than scanned; without it f_PBH is not constrainable | OPEN, blocks quantitative use of this channel |
| A3-1c | **NEW** — the quadratic NG truncation is non-perturbative (1.2\|f_NL\|σ_r ≈ 0.5–2) at the amplitudes PBH formation needs; assess a resummed or exact-δN map | OPEN |
| A3-1d | **NEW** — resolve the γ_cr ≲ 0.85 enhancement branch against Choudhury et al.'s suppression claim | OPEN, blocked on D1 |
| A3-3 | SIGW-kernel amplitude for the matter bounce | OPEN, now coupled to A3-1b |
