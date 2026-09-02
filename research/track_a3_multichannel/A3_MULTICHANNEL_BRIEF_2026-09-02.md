# Track A3 — Multi-channel consistency of the matter-bounce prediction at f_NL = -35/16

**Date:** 2026-09-02 · **Ledger item:** `NEXT_SCIENCE_LEDGER.md` #3 · **Status:** first pass complete

Every number below carries one of three labels:

| label | meaning |
|---|---|
| **reproduced** | re-derived here from a committed artifact, and diffed against the committed record |
| **new** | computed here for the first time, by a script committed alongside this brief |
| **cited** | quoted from a published abstract, verified verbatim on 2026-09-02; never recomputed |

Scripts: `pta_gamma_reproduce.py`, `pbh_abundance_fnl.py`, `survey_reach_fnl.py`.
Outputs: `outputs/*.json`. Manifests: `reproducibility/manifests/experiments/a3-*.json`.

---

## 0. The parameter under test

The lab's adopted matter-bounce squeezed amplitude is

> **f_NL^local = -35/16 = -2.1875**

following Li et al. (2016, arXiv:1612.02036), against the printed **-35/8 = -4.375** of
Cai et al. (2009, arXiv:0903.0631). P2's audit attributes the factor of two to
permutation-counting conventions in the in-in commutator and to a spurious
`+(99/128) Σ k_i^3` term in the Cai shape polynomial, whose removal halves the bare
squeezed limit exactly. **Ledger item #1 (an independent second-method derivation)
remains OPEN**, so the factor of two is *adopted*, not *settled*; both values are
carried in parallel throughout this brief.

**Same-day update (commit `d7dac953`).** The parallel theory-audit lane completed
its independent second-method (separate-universe / non-attractor δN) derivation on
2026-09-02 and returned verdict **OTHER**: it obtains
f_NL^local(ε) = (5ε − 35)/8, i.e. **−55/16 = −3.4375** at ε = 3/2, which is not a
rational multiple of either candidate and therefore **does not adjudicate the factor
of two**. It does establish three narrower things that this brief relies on: the two
published values use identical f_NL conventions (so the gap is not definitional);
the gap is exactly a factor of 2 (so it is not a single vertex coefficient); and
Cai et al.'s *printed* shape function does not reduce to their own stated −35/8 —
under the distinct-monomial reading of the (5,2,2) orbit it reduces to exactly
−35/16. See `research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.md`.
Item #1 stays OPEN; open item A3-2 below is unchanged.

---

## 1. Channel 1 — PTA free-spectrum slope (REPRODUCED)

### 1.1 What was reclaimed

`pipelines/p3_pta_mcmc/` holds a committed 320,000-sample emcee chain fit to the
NANOGrav 15-yr HD-correlated Ceffyl free-spectrum KDE posteriors
(Zenodo `10.5281/zenodo.8060824`, pack `30f_fs{hd}_ceffyl`, 30 frequency bins,
T_obs = 16.03 yr). The chain file is present and intact:

```
pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy
sha256 50abc38a04e1bf886adc833b5eb653be4e986877fe2476f87a78927f4f3610fc
```

**Nothing had to be restored from HuggingFace or B2.** `pta_gamma_reproduce.py`
re-derives every published summary from that chain and diffs against the two
committed JSON records; it reports `REPRODUCED: true`.

### 1.2 Reproduced numbers

| quantity | value | agreement with committed record |
|---|---|---|
| γ (mean ± std) | **2.5665 ± 0.3818** | exact (0.0 difference) |
| γ median [16%, 84%] | 2.5913 [2.3041, 2.8822] | exact |
| log10 A | −14.0252 ± 0.3796 | exact |
| Savage–Dickey B(γ=3 / free) | **3.228** | 3.1 × 10⁻¹⁵ absolute |
| Savage–Dickey B(γ=13/3 / free) | 4.522 × 10⁻⁴ | 2.4 × 10⁻¹⁸ |
| B(γ=3 / γ=13/3) | **7.138 × 10³** (log₁₀ = +3.854) | 3.1 × 10⁻¹¹ |
| z(γ = 3) | **+1.135 σ** | exact |
| z(γ = 13/3, SMBHB) | +4.627 σ | exact |
| z(γ = 5, scale-invariant tensors) | +6.373 σ | exact |

Sampling priors γ ~ U[0,7], log₁₀A ~ U[−18,−11]; Savage–Dickey uses a Scott-bandwidth
Gaussian KDE on the γ marginal against the uniform prior density 1/7.

### 1.3 What the matter bounce actually predicts — and a correction

With the characteristic-strain convention h_c(f) ∝ f^{(3−γ)/2} and
Ω_GW = (2π²/3H₀²) f² h_c², the slope maps as **Ω_GW ∝ f^{5−γ}** (*new*, one line of
algebra, in `pta_gamma_reproduce.py`):

| model | γ | Ω_GW slope |
|---|---|---|
| matter-bounce **induced** (second-order, scalar-sourced) GWs | **3** | f² |
| GW-driven SMBHB inspirals | 13/3 | f^{2/3} |
| scale-invariant **primordial tensors** (n_T = 0) | **5** | f⁰ |

**Correction to an assumption in the task framing.** γ = 3 is *not* the n_T = 0
scale-invariant-tensor case. n_T = 0 gives Ω_GW ∝ f⁰, i.e. **γ = 5**. The matter-bounce
γ = 3 is the *universal infrared f² scaling of the induced (scalar-sourced) GW
background*, which is what Papanikolaou (2025, arXiv:2504.11641, "Gravitational wave
signatures of non-singular matter bouncing cosmology in NANOGrav and beyond") reports
— his abstract states "an induced GW background with a universal infrared (IR)
frequency scaling of f²" in "excellent agreement" with the NANOGrav nHz data (*cited*).
The nearly scale-invariant *scalar* spectrum of a matter contraction
(Cai, Easson & Brandenberger 2012, arXiv:1206.2382) is a separate statement and does
not set γ.

### 1.4 Verdict for channel 1

- **γ = 2.567 ± 0.382 is consistent with the matter-bounce induced-GW prediction γ = 3
  at 1.14 σ** (*reproduced*). The Savage–Dickey factor mildly favours the fixed-γ=3
  hypothesis over free γ (B = 3.23, "substantial" on the Kass–Raftery scale, but only
  just).
- **The SMBHB expectation γ = 13/3 sits 4.63 σ away** and is disfavoured against γ = 3
  by log₁₀ B = +3.85 under uniform sampling priors (*reproduced*). This is a strong
  statement *within this likelihood and prior choice*; the committed
  `bf_prior_robustness.json` shows B(γ=3/free) drifting 3.23 → 1.47 as the γ prior is
  narrowed from U[0,7] to U[2,5], so the *nested-model* factor is prior-sensitive while
  the *ratio* B(MB/SMBHB) is stable at 7.1–8.7 × 10³.
- **Honest tension #1.** The *primordial-tensor* route to a nHz signal (n_T ≈ 0 → γ = 5)
  is excluded at 6.37 σ by this same posterior. The matter bounce's PTA consistency
  therefore rests **entirely on the second-order induced channel**, not on its primordial
  tensor spectrum.
- **Honest tension #2 (the important one).** Ω_GW ∝ f² is the *causality-limited*
  infrared slope of essentially any scalar-induced GW background, whatever sources it.
  γ = 3 is therefore a **consistency check, not a discriminator**: the matter bounce
  passes it, and so does any other SIGW scenario. The discriminating power in this
  channel is against SMBHB, not in favour of the bounce specifically.

---

## 2. Channel 2 — PBH abundance at −35/16 vs −35/8 (NEW)

### 2.1 Setup

`pbh_abundance_fnl.py` implements Press–Schechter with the standard local quadratic map
(Young & Byrnes 2013, arXiv:1307.4995, JCAP 1308:052; Franciolini et al. 2018,
arXiv:1801.09415):

    ζ = ζ_G + A (ζ_G² − σ²),    A = (3/5) f_NL,    ζ_G ~ N(0, σ²)
    β(ζ_c) = P(ζ > ζ_c)

inverted analytically (the survival function is used at both interval ends; a naive
`cdf(hi) − cdf(lo)` underflows to exactly 0 in the rare tail). Mass fraction → present
abundance uses the standard radiation-era relation
f_PBH = 1.68×10⁸ (γ_c/0.2)^{1/2} (g_*/106.75)^{−1/4} (M/M_⊙)^{−1/2} β
(Sasaki, Suyama, Tanaka & Yokoyama 2018, arXiv:1801.05235), with γ_c = 0.2,
g_* = 106.75, M = 10²⁰ g (the asteroid-mass window).

### 2.2 The analytic result: a ceiling that doubles

For f_NL < 0 the map is a downward parabola with an **absolute ceiling**

    ζ_max = −5/(12 f_NL) + (3/5)|f_NL| σ²

No realisation of ζ can exceed it. The leading term scales as 1/|f_NL|, so (*new*):

| f_NL | ζ_max (leading term) |
|---|---|
| −35/8 = −4.375 | **0.09524** |
| −35/16 = −2.1875 | **0.19048** |
| 0 | ∞ |

**Halving |f_NL| exactly doubles the ceiling — ratio 2.000000, analytic.** This is the
single sharpest thing this channel says about −35/16 vs −35/8.

### 2.3 Fixed-amplitude comparison (the physically meaningful one)

The curvature power-spectrum amplitude is set by the source (e.g. the SIGW amplitude
required by the PTA signal), and f_NL then decides whether PBHs are overproduced. So:
calibrate σ on the **Gaussian** case so that f_PBH = 1, then read off f_PBH at each
f_NL at that same σ (*new*):

| ζ_c | σ* (Gaussian → f_PBH = 1) | f_PBH at −35/16 | f_PBH at −35/8 | ratio (−35/16)/(−35/8) |
|---|---|---|---|---|
| 0.05 | 0.006325 | **7.32 × 10⁻³** | 3.75 × 10⁻⁶ | 1.95 × 10³ |
| 0.08 | 0.010120 | 1.24 × 10⁻⁴ | 1.12 × 10⁻¹⁴ | 1.11 × 10¹⁰ |
| 0.10 | 0.012650 | 3.75 × 10⁻⁶ | 0 (ζ_c above ceiling) | — |
| 0.12 | 0.015179 | 4.29 × 10⁻⁸ | 0 (ζ_c above ceiling) | — |
| 0.15 | 0.018974 | 1.82 × 10⁻¹² | 0 (ζ_c above ceiling) | — |

Perturbativity of the local expansion, 0.6|f_NL|σ, stays ≤ 0.04 everywhere in this
table, so the quadratic truncation is self-consistent in the amplitude sense.

Equivalently, the amplitude needed to *reach* f_PBH = 1 (*new*):

| ζ_c | σ required, Gaussian | −35/16 | −35/8 |
|---|---|---|---|
| 0.05 | 0.00632 | 0.00680 (×1.08) | 0.00746 (×1.18) |
| 0.08 | 0.01012 | 0.01146 (×1.13) | 0.01429 (×1.41) |
| 0.10 | 0.01265 | 0.01492 (×1.18) | 0.04259 (×3.37) |
| 0.15 | 0.01897 | 0.02574 (×1.36) | 0.14444 (×7.61) |

### 2.4 Verdict for channel 2

- **What changes at −35/16 vs −35/8: the suppression weakens by 3 to 10 orders of
  magnitude** at fixed amplitude, and the ceiling on ζ doubles. Negative f_NL suppresses
  PBH formation (confirmed here, *new*), but −35/16 is a **much weaker suppressor** than
  −35/8.
- **This is a favourable direction for the −35/16 value, and it is quantitative.** At
  ζ_c = 0.05, f_NL = −35/16 lands at f_PBH = 7.3 × 10⁻³, i.e. *inside* the window
  10⁻³ ≤ f_PBH ≤ 1 that Choudhury et al. 2025 report as "sizeable abundance"
  (*cited*), while −35/8 falls to 3.8 × 10⁻⁶, three orders below that window. Under the
  Press–Schechter treatment used here, **the halved value is the one that sits in the
  sizeable-abundance band**, not the printed Cai value. That is a coincidence worth
  stating, not a reproduction of their result — see the next bullet.
- **Honest limitation, stated up front.** The naive quadratic map has a hard ceiling that
  forbids PBH formation *entirely* (β = 0 identically) at the standard curvature
  thresholds ζ_c ≈ 0.45–1 in the rare-tail regime, at **both** −35/16 and −35/8
  (*new*, verified at σ = 0.02). That is an artefact of the truncated quadratic map, not
  a physical no-PBH theorem. It is precisely why Choudhury et al. use the
  **compaction-function** formation criterion with the full nonlinear ζ → C relation.
- **Not reproduced.** Choudhury, Dey, Ganguly, Karde, Singh & Tiwari, *"Negative
  non-Gaussianity as a salvager for PBHs with PTAs in bounce"*, EPJC 85:472 (2025),
  arXiv:2409.18983, study f_NL = (−39.95, −35/8) — the ekpyrotic and matter-bounce
  values — in an EFT-of-non-singular-bounce plus ultra-slow-roll setup, and report
  10⁻³ ≤ f_PBH ≤ 1, complete mitigation of PBH overproduction, and a perturbativity
  upper bound |f_NL| ≲ 60 (*cited, abstract verbatim*). **They do not treat −35/16.**
  Redoing their calculation at −35/16 requires their compaction-function pipeline and
  their USR power spectrum, neither of which is implemented here. **That is the single
  largest open item in this track.**

### 2.5 SAME-DAY UPDATE (2026-09-02, later) — compaction-function redo: §2.4 IS REVERSED

Open item **A3-1 is now closed**. `pbh_compaction_fnl.py` implements the
Choudhury et al. 2025 compaction-function criterion (their Eqs. 30, 31, 34, 35,
40, 41, 48-56, 60-66, read from the published PDF) in place of the
Press-Schechter quadratic map above. Full write-up:
**`PBH_COMPACTION_NOTE_2026-09-02.md`**. Nothing in §2.1-§2.4 is deleted; it is
the record of what the first pass computed. But its conclusion does not survive.

**What changed.**

1. **The ζ ceiling was an artefact.** In the compaction formalism the quadratic
   non-linearity bounds **C** (at C_max = f(w) = 2/3), not ζ. The map ζ_G → C_lin
   is unbounded, so every threshold C_th < 2/3 is reachable at every f_NL and
   β > 0 throughout. §2.2's "halving |f_NL| exactly doubles the ceiling" remains
   arithmetically true but is **without physical content** and is superseded as
   "the single sharpest thing this channel says."
2. **The ordering flips.** §2.4 said −35/16 is the *weaker* suppressor and "the
   halved value is the one that sits in the sizeable-abundance band." Under the
   compaction criterion the opposite holds: at fixed curvature amplitude
   **f_PBH(−35/16) < f_PBH(−35/8) at every point** of a 27-point
   (Δ, r_p k_p, C_th) grid spanning γ_cr ∈ [0.766, 0.968].

| | first pass (§2.3) | compaction redo |
|---|---|---|
| f_PBH at −35/16 | 7.32 × 10⁻³ | 3.62 × 10⁻¹⁴ |
| f_PBH at −35/8 | 3.75 × 10⁻⁶ | 1.57 × 10⁻² |
| ratio (−35/16)/(−35/8) | 1.95 × 10³ | 2.3 × 10⁻¹² |

3. **The robust number.** f_PBH itself is exponentially sensitive to γ_cr (>100
   decades across the grid), so it is *not* quotable. The stable observable is
   the amplitude required to reach the floor of the Choudhury+ band:
   **A(−35/16)/A(−35/8) = 1.732, range [1.610, 1.809], std 0.050 (n = 27)** —
   ±6% while f_PBH moves by 100+ dex. K, Ω_DM, g_*, M_H all cancel in it.
4. **Unforced agreement with Choudhury et al.** at the one comparable point:
   −35/8 lands at f_PBH = 1.6 × 10⁻², inside their reported 10⁻³ ≤ f_PBH ≤ 1,
   with the amplitude fixed only by requiring the *Gaussian* case to give
   f_PBH = 1. Their qualitative "negative f_NL mitigates overproduction" is
   reproduced for γ_cr ≳ 0.85.
5. **A disagreement, recorded not resolved.** For γ_cr ≲ 0.85 our implementation
   of their equations gives *enhancement*, not suppression, at fixed amplitude.
   Which side their setup sits on cannot be determined — see next point.
6. **What is missing from their paper.** Their Δ²_ζ is the regularized-
   renormalized-resummed one-loop EFT-of-bounce + USR spectrum (their Sec. III B,
   Eq. 55). The paper describes the construction but prints no closed-form
   Δ²_ζ(k) and no complete parameter set (loop-counterterm normalisation,
   tabulated EFT coefficients, k_s/k_e/ΔN_USR). **This is the single ingredient
   that cannot be reproduced from the paper**, and it is what fixes γ_cr. A
   lognormal stand-in is used and the amplitude is scanned, never adopted.
7. **Perturbativity caveat, shared with them.** At the amplitudes PBH formation
   needs, 1.2|f_NL|σ_r ≈ 0.5-1.0 at −35/16 and 1.1-2.0 at −35/8 — the quadratic
   truncation of the local map is not perturbatively controlled. Same class of
   statement as their own |f_NL| ≲ 60 bound.

**Revised verdict for channel 2.** The channel *is* sensitive to which f_NL value
is right (factor 1.73 in required amplitude), but it **cannot yet be turned into a
constraint**, because the absolute f_PBH depends exponentially on γ_cr and hence on
a curvature spectrum this lab has not yet computed. That prerequisite is the same
one as **A3-3**, so A3-1b and A3-3 should be done together.

---

---

## 3. Channel 3 — Survey reach for f_NL^local = −2.1875 (NEW arithmetic on CITED σ)

The matter-bounce bispectrum is not exactly the local shape; P2 adopts a noise-weighted
shape overlap **r = 0.84**, so an experiment quoting σ_local constrains the bounce
amplitude at σ_local/r. Both bare and r-projected significances are given.

### 3.1 Forecast reach (`survey_reach_fnl.py`)

| survey | σ(f_NL^local) | source | bare, −35/16 | r-projected, −35/16 | bare, −35/8 |
|---|---|---|---|---|---|
| SPHEREx, bispectrum only (fiducial) | **0.7** | Heinrich, Doré & Krause 2023, arXiv:2311.13082 (abstract, *cited*) | **3.13 σ** | **2.63 σ** | 6.25 σ |
| SPHEREx, target (P + B combined) | **0.5** | same abstract: "still on target for being σ_fNL = 0.5 once the power spectrum will be included" (*cited*) | **4.38 σ** | **3.68 σ** | 8.75 σ |
| MegaMapper-class z > 2 spectroscopy | **~1** (order unity) | Ferraro et al. 2019, arXiv:1903.09208 (abstract: "crossing the crucial theoretical threshold of σ(f_NL^local) of order unity") (*cited*) | 2.19 σ | 1.84 σ | 4.38 σ |
| *illustrative* next-generation floor | 0.3 | **not a published forecast** | 7.29 σ | 6.12 σ | 14.58 σ |
| *illustrative* CV-limited floor | 0.1 | **not a published forecast** | 21.88 σ | 18.37 σ | 43.75 σ |

**Deliberate refusal.** The task framing suggested σ(f_NL) ≈ 0.1–0.3 for MegaMapper. No
such number appears in the Ferraro et al. 2019 or Sailer et al. 2021 (arXiv:2106.09713,
FishLSS) abstracts, and MegaMapper is an unapproved design; consistent with P2's standing
policy ("We do not transfer the SPHEREx systematic budget or quote a headline
significance for an unapproved design"), MegaMapper is quoted **only at the published
order-unity level**, and the two tighter rows are flagged ILLUSTRATIVE in both the script
and the JSON. Sailer et al. 2021 is cited as the Fisher *framework*, not as a source of a
MegaMapper σ.

### 3.2 Current constraints — DESI DR1

Chaussidon et al. 2024, arXiv:2411.17623, *"Constraining primordial non-Gaussianity with
DESI 2024 LRG and QSO samples"* (1,631,716 LRGs at 0.6 < z < 1.1; 1,189,129 QSOs at
0.8 < z < 3.1) report (*cited, abstract verbatim*):

- **f_NL^loc = −3.6 (+9.0 / −9.1)** at 68%, with the merger model for the QSO PNG bias;
- **f_NL^loc = +3.5 (+10.7 / −7.4)** at 68%, assuming universality for the QSO bias;
- the most precise LSS PNG measurement to date, 2.3× better than eBOSS DR16.

Derived here (*new*):

| DESI DR1 variant | tension with −35/16 | tension with −35/8 | discriminating power ‖f_NL‖/σ |
|---|---|---|---|
| merger-model QSO bias | **0.16 σ** | 0.09 σ | 0.24 |
| universality QSO bias | 0.77 σ | 1.06 σ | 0.24 |

### 3.3 Verdict for channel 3

- **The matter-bounce value is fully consistent with DESI DR1** (0.16 σ from the headline
  central value), and DESI DR1 has essentially **no discriminating power** on it:
  |f_NL|/σ = 0.24. The bias-model choice moves the tension from 0.16 σ to 0.77 σ, which
  is itself larger than the difference between −35/16 and −35/8 in that comparison —
  i.e. **current data cannot separate the two candidate matter-bounce values.**
- **SPHEREx is the first instrument that can.** At its target σ = 0.5 the two values
  differ by 4.4 σ (bare) or 3.7 σ (r-projected) in predicted significance; at the
  bispectrum-only fiducial σ = 0.7 the gap is 3.1 σ / 2.6 σ. Settling ledger item #1
  before SPHEREx data arrive is therefore not academic.

---

## 4. The multi-channel statement

**Consistent, with two honest qualifications and one genuine gap.**

1. **PTA (reproduced).** γ = 2.567 ± 0.382 agrees with the matter-bounce induced-GW
   γ = 3 at 1.14 σ, and disfavours SMBHB by log₁₀ B = +3.85. *Qualification:* Ω_GW ∝ f²
   is the universal SIGW infrared slope, so this channel confirms rather than
   discriminates; and the primordial-tensor route (γ = 5) is excluded at 6.37 σ. The PTA
   channel is **insensitive to the value of f_NL** — it constrains the slope, not the
   bispectrum amplitude — so it cannot separate −35/16 from −35/8 either.
2. **PBH (new).** Negative f_NL suppresses PBH formation; at fixed amplitude the −35/16
   suppression is 3–10 orders of magnitude weaker than at −35/8, and the ζ ceiling
   doubles from 0.0952 to 0.1905. Under the Press–Schechter treatment, −35/16 sits inside
   the 10⁻³ ≤ f_PBH ≤ 1 band that Choudhury et al. report for their bounce setup, while
   −35/8 falls three orders below it. *Qualification:* the quadratic-map ceiling makes
   this treatment unable to reach standard thresholds ζ_c ≈ 0.45–1; a compaction-function
   redo is required before any of it is quoted as a match to Choudhury et al.
3. **LSS bispectrum (new arithmetic on cited σ).** −35/16 is consistent with DESI DR1 at
   0.16 σ and is detectable at 2.6–3.7 σ by SPHEREx once the shape projection r = 0.84
   is applied. This is the only channel that is sensitive to the *value* of f_NL.

**The tension that matters is internal, not observational.** Every channel is consistent
with the data; but only channel 3 depends on which of −35/16 or −35/8 is right, and it
depends on it strongly. **Ledger item #1 gates the scientific content of this track.**

---

## 5. Open items (in priority order)

| # | item | why | cost |
|---|---|---|---|
| ~~A3-1~~ | ~~Redo the PBH channel with the **compaction-function** criterion (Choudhury et al. setup) at −35/16~~ | **CLOSED 2026-09-02** — `pbh_compaction_fnl.py` + `PBH_COMPACTION_NOTE_2026-09-02.md`; §2.4's conclusion is reversed (see §2.5) | done, local, $0 |
| A3-1b | Compute the matter-bounce curvature spectrum Δ²_ζ(k) in-lab so γ_cr is **predicted** rather than scanned | f_PBH depends exponentially on γ_cr; without it channel 2 is not a constraint. Couples to A3-3 | weeks |
| A3-1c | Assess a resummed / exact-δN NG map | 1.2\|f_NL\|σ_r ≈ 0.5–2 at the required amplitudes — the quadratic truncation is non-perturbative | days |
| A3-1d | Resolve the γ_cr ≲ 0.85 *enhancement* branch against Choudhury et al.'s suppression claim | our implementation of their equations flips sign across γ_cr ≈ 0.85 | blocked on their spectrum |
| A3-2 | Settle **ledger #1** (independent −35/16 derivation) | it is the only thing channel 3 actually discriminates on | see ledger |
| A3-3 | Propagate the matter-bounce *scalar* spectrum through the SIGW kernel to get Ω_GW amplitude (not just slope) at the nHz band | would upgrade channel 1 from slope-consistency to an amplitude test, which *is* discriminating | weeks |
| A3-4 | Re-derive the r = 0.84 shape overlap at the −35/16 fiducial rather than importing P2's | P2's r was computed for a shape whose normalisation the factor-of-2 audit changed | hours, local, $0 |
| A3-5 | Recover a published MegaMapper σ(f_NL^local) from the Sailer et al. 2021 FishLSS body (not the abstract), or state that none is citable | the illustrative rows should be replaced by a real number or dropped | hours |

---

## 6. Provenance

- Chain: `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy`
  (sha256 `50abc38a…10fc`), upstream Zenodo `10.5281/zenodo.8060824`.
- Prior framing of the PTA result: `project-context/SSOT/paper-3/status.md`,
  `arxiv/main.tex` §NANOGrav (which records the 2026-06-09 provenance audit retracting an
  earlier synthetic-from-power-law γ = 3.20 ± 0.42 / B = 34.0 and replacing it with the
  real-KDE γ = 2.567 ± 0.382 / B_MB/SMBHB = 7.14 × 10³ reproduced above).
- Portfolio origin: `project-context/bounce_portfolio_strategy.md` (2026-03-24), Track C.
- Ranked next-science list: `research/project_nextgen_bounce_signals/`.
- All computations: venue **local** (Apple M5, 24 GB, macOS 26.5), no GPU, cost **$0**,
  total measured wall time **< 0.1 s**.
