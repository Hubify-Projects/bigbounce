# Ledger #6 — early-universe anomaly map: first derived discriminator with a current-data verdict

**Date:** 2026-09-02 · **Ledger item:** `NEXT_SCIENCE_LEDGER.md` #6 (OPEN → FIRST TEST DONE)
**Vision route:** VISION.md route 3 — "anomalies that strain single-field inflation, measured
in public data, connected to explicit bounce-vs-inflation discriminators"
(`PORTFOLIO_DECISION_2026-09-02.md` Addendum: *the anomaly line is redirected, not retired*).

**Rules honoured:** evidence decides; a null is a result; every number below is either a
literature citation or output of the committed script
`research/anomaly_map/ledger6_png_highz_abundance.py`
(sha256 `f1121e2b79c4d43a98117d022876e72d9c972754d26b9e090b7b96e446742365`).

---

## 1. Literature scan — three anomaly classes, three discriminator questions

### 1.1 z > 10 over-massive galaxies

*Observed status.* Labbé et al. 2023 (Nature 616, 266; arXiv:2207.12446) reported six CEERS
candidates at 7.4 ≤ z ≤ 9.1 with implied M\* ≳ 10¹⁰ M⊙ and a cumulative stellar-mass density
far above pre-JWST expectations. Boylan-Kolchin 2023 (Nat. Astron. 7, 731; arXiv:2208.01611)
framed the model-independent version of the tension: the observed ρ\*(>10¹⁰ M⊙) requires a
baryon-to-star conversion efficiency ε ≳ 0.5–1 inside ΛCDM haloes, i.e. it stresses the
*halo abundance*, not only galaxy physics. Subsequent work has softened but not removed the
tension: MIRI photometry lowered several masses (Papovich et al. 2023, arXiv:2403.02399);
spectroscopy showed part of the excess is AGN/"little red dot" continuum
(Kocevski et al. 2023; Maiolino et al. 2024); COSMOS-Web (Casey et al. 2024, ApJ 965, 98;
arXiv:2308.10932) and JADES (Eisenstein et al. 2023, arXiv:2306.02465) extended the census.
The most recent synthesis, McCaffrey, Hardin, Wise & Regan 2026 (*Beyond No Tension: JWST
z > 10 Galaxies Push Simulations to the Limit*, OJA; arXiv:2509.07695), finds MoM-z14
(z ≈ 14.44) reproducible by the Renaissance suite while **GS-z14 remains an outlier even
after cosmic variance**. Net: a residual, model-dependent excess at the factor-of-few-to-ten
level with mass systematics ≳ 0.3 dex.

*What single-field inflation + ΛCDM predicts.* A Gaussian, near-scale-invariant initial
field. The abundance of M_h ≳ 10¹¹·⁵ M⊙ haloes at z ≈ 10–12 is then fixed (ν ≈ 5–8 peaks) and
exponentially sensitive to the tail; there is no free knob other than baryonic efficiency.

*What a matter-bounce / nonsingular bounce changes.* A matter-dominated contraction generates
a **local-shape** bispectrum with f_NL^loc = −35/16 in the squeezed configuration — a lab
result now closed by two independent routes (ledger #1, `research/theory_audit/`,
commits d7dac953 / aa2987cf / 66cf1cb0), with the orientation dependence
f(μ) = −35/16 + (15/16)μ² already contained in Li et al. 2016 Eq. (4.19). Local PNG shifts
the *tail* of the density field, hence the rare-halo abundance, and does so with the sign of
f_NL. **This is the discriminator: single-field slow-roll gives f_NL^loc ≈ 0 (Maldacena 2002
consistency relation, f_NL^loc = 5(1−n_s)/12 ≈ 0.015); matter contraction gives −2.1875.**

### 1.2 Isolated early SMBHs

*Observed status.* UHZ1 (Bogdán et al. 2024, Nat. Astron. 8, 126; arXiv:2305.15458;
Natarajan et al. 2024, ApJ 960, L1; arXiv:2308.02654): a Compton-thick z ≈ 10.1 quasar,
M_BH ≈ 4 × 10⁷ M⊙ with M_BH/M\* ~ 1 — the first over-massive black-hole-galaxy candidate.
GN-z11 at z = 10.6 hosts M_BH ~ 1.6 × 10⁶ M⊙ (Maiolino et al. 2024, Nature 627, 59;
arXiv:2305.12492). LRDs add a population of z ≈ 5–9 AGN with anomalous M_BH/M\*
(Matthee et al. 2024, ApJ 963, 129; Greene et al. 2024, ApJ 964, 39).

*Predictions.* ΛCDM + light (Pop III remnant, ~10²M⊙) seeds cannot reach 4 × 10⁷ M⊙ by
z = 10 at Eddington; the standard resolutions are heavy direct-collapse seeds (10⁴–10⁶ M⊙) or
super-Eddington episodes — both astrophysical, not cosmological. A bounce enters only through
the *initial condition*: an enhanced small-scale spectrum or PBH seed population.

*Discriminator (deferred, not derived here).* PBH seeding is already an active lab channel
(ledger #3 / A3-1: `research/track_a3_multichannel/pbh_compaction_fnl.py`), and that work
showed f_PBH is **not quotable** at present (>100 dex spread over the collapse threshold);
the robust quantity is the required-amplitude ratio A(−35/16)/A(−35/8) = 1.73 ± 0.05.
Turning early SMBHs into a discriminator therefore requires the in-lab Δ²_ζ (open item
A3-1b) first. Recorded as blocked-on-A3-1b, not attempted.

### 1.3 Hemispherical asymmetry

*Observed status.* Planck 2018 VII (*Isotropy and Statistics of the CMB*, A&A 641, A7;
arXiv:1906.02552): a ~7% dipolar power modulation toward (l, b) = (209°, −15°) over
ℓ ≲ 60, significance approaching 3σ **before** look-elsewhere correction, which the
collaboration itself flags as the dominant caveat. Reconfirmed at similar amplitude in PR4
(e.g. arXiv:2306.14880). The cosmic birefringence angle β = 0.342°+0.094/−0.091 (Eskilt &
Komatsu 2022, PRD 106, 063503; arXiv:2205.13962) is a *separate*, parity-odd, ~3.6σ hint.

*Predictions.* Single-field inflation predicts statistical isotropy at all observed scales;
an asymmetry requires a super-horizon gradient (e.g. Erickcek–Kamionkowski–Carroll modulation
by a long-wavelength mode, which itself needs large f_NL^loc) or a preferred direction from
pre-inflationary/bounce-scale physics. A bounce supplies a natural candidate — a feature at
the bounce scale, or the torsion-bounce preferred axis of route 2 — but no lab-derived
amplitude exists.

*Discriminator (deferred).* The EKC route is quantitatively coupled to §1.1: modulation
amplitude ∝ f_NL^loc × (super-horizon mode amplitude). At |f_NL| = 2.19 the required
super-horizon mode is far outside the perturbative regime; the honest next cheap step is
the **parity-odd** channel instead (chiral SGWB, ledger #7), not the temperature dipole.

---

## 2. The discriminator that was derived and confronted

**Chosen:** the local-PNG modification of the high-z halo/galaxy abundance at
f_NL = −35/16, versus f_NL = 0 (single field) and f_NL = −35/8 (Cai et al. 2009).
It is the only one of the three that is (a) derivable from a *closed* lab number and
(b) confrontable with public data today.

**Method** (all in the committed script, deterministic, CPU-only, ~2 s):

1. Linear P(k) from the Eisenstein & Hu 1998 no-wiggle transfer function
   (astro-ph/9709112 Eqs. 28–31), Planck 2018 cosmology, normalised to σ₈ = 0.8111
   (script reproduces σ(8 h⁻¹Mpc) = 0.8111 exactly).
2. Poisson kernel M_R(k) = (2/3) k²T(k)W(kR)/(Ω_m H₀²).
3. Smoothed skewness from the local bispectrum B_Φ = 2f_NL[P(k₁)P(k₂) + 2 perms],
   by 3-D quadrature; S₃ = ⟨δ_R³⟩/σ_R⁴. Converged to 5 significant figures under
   (n_k, n_μ, k_max) refinement 140/48/60 → 300/96/300.
   **S₃/f_NL = 8.784 × 10⁻⁴ at R = 8 h⁻¹Mpc**, 3.366 × 10⁻⁴ at M_h = 2.15 × 10¹¹ M⊙/h.
4. Non-Gaussian mass function: LoVerde, Miller, Shandera & Verde 2008 (arXiv:0711.4126)
   Eq. (45)/(46), the Edgeworth-corrected Press–Schechter ratio
   R = (dn/dM)_NG/(dn/dM)_G. R is a multiplicative correction, so it is independent of
   which Gaussian fit (PS/ST/Tinker) it multiplies.
5. M\* > 10¹⁰ M⊙ mapped to host halo mass through M_h = M\*/(ε f_b), f_b = Ω_b/Ω_m = 0.1564,
   for ε ∈ {0.05, 0.20, 0.50, 1.00}. ε ≈ 0.05–0.2 is the pre-JWST calibration;
   ε ≳ 0.5 is the Boylan-Kolchin 2023 stress regime.

### 2.1 Predicted effect size

Abundance ratio R = n(f_NL)/n(0) at the M\* > 10¹⁰ M⊙ threshold
(`outputs/ledger6_png_highz_abundance.json`, `threshold_cases`):

| ε | log M_h [M⊙/h] | z | ν | **R(−35/16)** | R(−35/8) |
|---|---|---|---|---|---|
| 0.20 | 11.33 | 10 | 5.63 | **0.948** | 0.896 |
| 0.20 | 11.33 | 11 | 6.15 | **0.932** | 0.863 |
| 0.20 | 11.33 | 12 | 6.66 | **0.912** | 0.824 |
| 0.05 | 11.94 | 11 | 7.42 | **0.881** | 0.762 |
| 0.05 | 11.94 | 12 | 8.04 | **0.847** | 0.694 |
| 0.50 | 10.94 | 11 | 5.48 | **0.951** | 0.903 |
| 1.00 | 10.63 | 11 | 5.04 | **0.962** | 0.924 |

**The lab's bounce value predicts a 5–15% SUPPRESSION of the z ≈ 10–12 massive-galaxy
abundance, not an enhancement.** Stated plainly: the sign goes the *wrong way* for the
"too many massive galaxies" anomaly. Negative local f_NL thins the high-σ tail; the matter
bounce therefore makes the JWST tension marginally *worse*, not better. In the mass-threshold
metric the whole effect is equivalent to shifting the halo-mass threshold by only
Δlog₁₀M_h ≈ +0.005–0.009 dex — three to four times smaller than the ~0.03 dex rounding of a
published mass estimate, and ~50× smaller than the ≳ 0.3 dex SED-fitting systematic.

### 2.2 Confrontation with the data

Two independent public confrontations, both in `outputs/..json` → `confrontation`:

- **Sensitivity of the anomaly to f_NL.** dR/df_NL = 0.0313 at (ε = 0.2, z = 11).
  Changing the abundance by a factor 2 requires |f_NL| ≈ 32; a factor 10 requires ≈ 288
  (at ε = 0.05, z = 12: 14 and 129). Those are *linear-response requirements* well outside
  the Edgeworth validity condition |S₃σν³| ≪ 1, so they are order-of-magnitude scale
  indicators — but the conclusion is robust: **local PNG at any Planck-allowed amplitude
  cannot explain the JWST excess.** At the Planck 2018 IX (arXiv:1905.05697) KSW T+E
  constraint f_NL^loc = −0.9 ± 5.1, the ±2σ envelope spans only R ∈ [0.65, 1.29] at
  (ε = 0.2, z = 11).
- **Detectability of the lab's own value.** The predicted 6.8% (ε = 0.2, z = 11)
  suppression must be compared with the observational error budget on the z ≳ 10
  M\* > 10¹⁰ M⊙ abundance: SED-derived stellar-mass systematics ≳ 0.3 dex (≥ ×2 in
  abundance given the local slope dln n/dln M_h = −5.7), AGN/LRD contamination at the
  tens-of-percent level (Kocevski+2023; Maiolino+2024), and cosmic variance which
  McCaffrey+2026 explicitly invoke as the discriminating axis for GS-z14. The signal is
  ~10–30× below the current systematic floor.

---

## 3. VERDICT

**Not yet testable — and, where it does point, it points against the anomaly.** The lab's
matter-contraction value f_NL^loc = −35/16 predicts a 5–15% *suppression* of the
M\* > 10¹⁰ M⊙ galaxy abundance at z ≈ 10–12 (6.8% at the fiducial ε = 0.2, z = 11;
15.3% at ε = 0.05, z = 12), equivalent to a halo-mass-threshold shift of only
Δlog₁₀M_h ≈ +0.006 dex. That is 10–30× smaller than the current observational systematic
floor on the high-z abundance (≥ 0.3 dex in stellar mass ⇒ ≥ ×2 in number density), so no
public JWST catalog available today — CEERS, JADES, COSMOS-Web, or the MoM/GS-z14
record-holders — can distinguish f_NL = −35/16 from f_NL = 0 through this channel; nor can
it distinguish −35/16 from Cai's −35/8 (8.8% vs 17.6% suppression at ε = 0.2, z = 12), consistent with
ledger #3's conclusion that only the *survey* channel (SPHEREx, 2.6–3.1σ) separates the two.
The scientifically useful outcome is the direction: because local PNG at −35/16 thins rather
than fattens the rare-object tail, **the matter bounce is not a candidate explanation for the
JWST over-massive-galaxy anomaly, and the anomaly cannot be cited as bounce evidence.** This
is recorded as a null, and it is a *useful* null: it removes an attractive-looking but false
connection between route 3 and the flagship line, and it shows the high-z abundance channel
is not where the lab's f_NL is measurable.

**Next cheap step for the other two classes.**
*Early SMBHs* — blocked on ledger item A3-1b (in-lab Δ²_ζ from the bounce spectrum); once
that exists, re-run `pbh_compaction_fnl.py` at the seed masses UHZ1/GN-z11 require
(10⁴–10⁶ M⊙ at z ≈ 15–20) and ask whether the required amplitude is inside or outside the
CMB-µ-distortion bound (COBE/FIRAS |µ| < 9 × 10⁻⁵). ~1 day, CPU-only.
*Hemispherical asymmetry* — the temperature-dipole route is dead at |f_NL| = 2.19 (the
Erickcek–Kamionkowski–Carroll modulation scales as f_NL × super-horizon amplitude, and §2.2
shows the required f_NL is ~10²). Redirect to the **parity-odd** channel, which is
bounce-specific and not f_NL-limited: ledger #7's analytic Δ_h estimate for circular
polarisation of the SGWB from the torsion bounce. That is the item to promote.

---

## 4. Artifacts

| Path | What |
|---|---|
| `research/anomaly_map/ledger6_png_highz_abundance.py` | the computation (numpy/scipy, deterministic) |
| `research/anomaly_map/outputs/ledger6_png_highz_abundance.json` | all numbers quoted above |
| `research/anomaly_map/outputs/ledger6_png_highz_abundance.png` | R−1 vs M_h at z = 8/10/12/14 and the three f_NL values at z = 11 |
| `reproducibility/manifests/experiments/anomaly-map-png-highz-abundance.json` | directive-Q2 manifest (schema-validated) |

Reproduce: `python3 research/anomaly_map/ledger6_png_highz_abundance.py` (~2 s, CPU-only,
no network, no external data files, $0).
