# A3-1b — The lab's own primordial curvature spectrum Δ²_ζ(k) at PBH scales

**Date:** 2026-09-03 · **Ledger:** `NEXT_SCIENCE_LEDGER.md` #3 (sub-item A3-1b), #6 (early-SMBH discriminator)
· **Script:** `inlab_delta2_zeta_2026-09-03.py` · **Outputs:** `outputs/inlab_delta2_zeta_2026-09-03.{json,png}`
· **Manifest:** `reproducibility/manifests/experiments/a3-1b-inlab-delta2-zeta.json`
· **Venue:** local (Apple M-series), no GPU, cost **$0**, measured wall time **170 s**

**Purpose.** `PBH_COMPACTION_NOTE_2026-09-02.md` closed A3-1 but left the PBH channel
depending on an *external* spectrum: Choudhury et al. 2025's RRR one-loop Δ²_ζ, which
their published paper does not make reconstructible (their deviation **D1**), forcing a
lognormal stand-in with a **scanned** amplitude. This note removes that dependence by
computing what the lab's own matter-bounce model actually delivers, and feeding it into
the committed compaction machinery unmodified.

---

## 1. The spectrum

For a contracting phase with equation of state w [LITERATURE: Wands 1999 gr-qc/9809062;
Cai, Easson & Brandenberger 2012 arXiv:1206.2382 §2–4; Quintin, Sherkatghanad, Cai &
Brandenberger 2015 arXiv:1508.04141 §2]:

    Δ²_ζ(k) = A_s (k/k_*)^{n_s−1},      n_s − 1 = 12w/(1+w)

exactly scale-invariant for pure dust (w = 0), with a small tilt from a small deviation
of w. **The lab does not predict w independently, so the tilt is calibrated, not
predicted.** Two branches are carried:

| branch | n_s | implied w | Δ²_ζ(10² Mpc⁻¹) | Δ²_ζ(10⁴) | Δ²_ζ(10¹³) | Δ²_ζ(10¹⁵) |
|---|---|---|---|---|---|---|
| MB-anchored (Planck 2018 tilt) | 0.9649 | −0.00292 | 1.608e−9 | 1.368e−9 | 6.611e−10 | 5.624e−10 |
| pure dust (bracket) | 1 (exact) | 0 | 2.100e−9 | 2.100e−9 | 2.100e−9 | 2.100e−9 |

Amplitude anchor: **A_s = 2.1×10⁻⁹ at k_* = 0.05 Mpc⁻¹** (Planck 2018 TT,TE,EE+lowE
+lensing). The ±1σ tilt band (n_s ± 0.0042) at k = 10¹⁵ Mpc⁻¹ is [4.80e−10, 6.58e−10] —
i.e. **the 16-decade extrapolation is uncertain by only ±15%,** because the tilt itself is
tiny. The extrapolation is a single power law with **no feature**.

### 1.1 Assumptions of the extrapolation to k ~ 10⁵–10¹⁵ Mpc⁻¹

* **E1** — w stays at its CMB-calibrated value across those decades: no w-evolution
  epoch, no USR-like stage, no spectator/curvaton sector, no resonance. The lab's
  committed model contains none of these.
* **E2** — the bounce transfer is scale-independent, which A2 establishes **only for
  kη_B ≪ 1** (`research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md`
  §4.3: the post-bounce spectrum is flat across the k grid to 1.2–4.2%, the residual
  being the finite-k (kη_B)² truncation; the growing branch dominates via
  |r| = 9A²I_∞/k³, and T = (1−ρ)/2 is k-independent at leading gradient order).

**Where the extrapolation breaks — k_B.** A2 reports η_B in bounce units
(LQC effective dust 1.06015, analytic non-LQC poly 0.57735, Quintin-type 0.44960, so
k_B = 1/η_B = 0.943 / 1.732 / 2.224 in those units). Converting to Mpc⁻¹ needs the bounce
energy scale, which **the lab has not committed** (no ρ_c or T_B in the repo), so it is
reported as a function of it:

| bounce scale T_B | k_B (Mpc⁻¹) | kη_B at k = 10¹⁵ Mpc⁻¹ |
|---|---|---|
| 10¹⁶ GeV | 1.71e23 | 5.8e−9 |
| 10¹⁴ GeV | 1.71e21 | 5.8e−7 |
| 10¹⁰ GeV | 1.71e17 | 5.8e−3 |

For any bounce above the BBN scale, **every PBH scale sits at kη_B ≤ 10⁻²** — comfortably
inside A2's validity domain. The extrapolation is therefore defended, and the
bounce-scale structure that the literature discusses at k ~ k_B is many decades away.

---

## 2. Enhancement candidates in the literature (LITERATURE, labelled as such)

Does any documented matter-bounce mechanism put a small-scale bump into Δ²_ζ **within the
lab's model**? Four checked; **all four: no.**

| reference | claim (theirs) | bump in this model? | why |
|---|---|---|---|
| Quintin, Sherkatghanad, Cai & Brandenberger 2015, arXiv:1508.04141 | growth of the bispectrum amplitude through a non-singular bounce | **no** | the enhancement is on the **cubic** amplitude, not the power spectrum; A2's linear transfer of the same backgrounds is a k-independent factor for kη_B ≪ 1 |
| Agullo, Bolliet & Sreenath 2017, arXiv:1712.08148 | LQC bounce strongly enhances PNG; power spectrum acquires structure near the bounce curvature scale | **no** | the structure lives at k ~ k_B, i.e. exactly where A2 stops being valid; PBH scales are ≥ 17 decades below k_B |
| Chen, Zhu, Yan, Wang & Cai 2022/2023, **arXiv:2207.14532** (JCAP 01 (2023) 015); predecessor arXiv:1609.02571 | **non-linear processes in the bounce phase itself** amplify fluctuations and enhance PBH abundance | **no** | operates on modes that are not deep super-Hubble at the bounce (kη_B ~ 1); importing it would be importing an effect from outside the model's validated domain |
| Papanikolaou, Banerjee, Cai, Capozziello & Saridakis 2024, arXiv:2404.03779 (see also 2405.00207, 2602.12057) | PBHs form by **direct collapse during the pressureless contracting phase** | **no** (different channel) | out of scope of the compaction criterion used here, which assumes radiation-era (w = 1/3) collapse at horizon re-entry — recorded as **new open item A3-1e**, not as an enhancement |

*(The task's pointer "Chen–Wang–Xu et al 2023, arXiv:2210.xxxx" resolves to
**arXiv:2207.14532**; there is no 2210 paper of that description.)*

**No mechanism is imported.** Every one of them is an added ingredient the lab's
committed model does not contain, and adding one to reach PBH formation would be tuning
the spectrum to produce PBHs — forbidden here.

---

## 3. Delivered vs. required amplitude

`pbh_compaction_fnl.py` is **imported and used unmodified**; only its module-level
spectrum function is swapped for the lab power law (and restored afterwards; the script
asserts the restore). "A" now means **Δ²_ζ at the peak scale k_p**, not a lognormal
integrated amplitude. `f_pbh` is evaluated at the module's fixed M_H = 10²⁰ g and the
mass dependence handled by rescaling the target (f_PBH ∝ (M_⊙/M_H)^{1/2}); no committed
result of that script is changed.

**k ↔ M_H is derived, not quoted** (M_H = 4π M_pl²/H with k = aH and entropy
conservation). Validation: k = 2.9×10⁵ Mpc⁻¹ → M_H = 166.2 M_⊙ → M_PBH = γM_H = **33.2 M_⊙**
at γ = 0.2, matching the standard literature anchor (~30 M_⊙).

### 3.1 The table (C_th = 0.5, n_s = 0.9649)

| mass scale | k_p (Mpc⁻¹) | **delivered** Δ²_ζ | **required** (f_PBH = 10⁻³) −35/16 | −35/8 | **required/delivered** at −35/16 |
|---|---|---|---|---|---|
| M_H = 10¹⁵ g | 5.27e15 | 5.31e−10 | 0.00556 | 0.00297 | **1.05e7** |
| M_H = 10²⁰ g (asteroid; the A3-1 mass) | 1.67e13 | 6.49e−10 | 0.00636 | 0.00339 | **9.79e6** |
| M_H = 1 M_⊙ | 3.74e6 | 1.11e−9 | 0.01021 | 0.00545 | **9.19e6** |
| M_H = 30 M_⊙ (LIGO) | 6.83e5 | 1.18e−9 | 0.01095 | 0.00584 | **9.28e6** |
| M_H = 10⁴ M_⊙ (SMBH seed) | 3.74e4 | 1.31e−9 | 0.01247 | 0.00665 | **9.55e6** |

Raising the target from f_PBH = 10⁻³ to 1 moves the required amplitude by only ~20–50%
(full grid in the JSON) — the requirement is exponentially steep, so **which f_PBH target
is chosen is irrelevant to the verdict.**

At the delivered amplitude the committed machinery returns **f_PBH = 0 exactly** in double
precision at every mass and every f_NL. To quantify rather than report a bare zero, the
Gaussian-limit exponent is also computed: at M_H = 10²⁰ g the threshold sits at
**8.9×10⁴ σ_c**, i.e. log₁₀β ≈ **−1.7×10⁹**.

### 3.2 Sensitivity

| C_th | A(0) | A(−35/16) | A(−35/8) | ratio (−35/16)/(−35/8) |
|---|---|---|---|---|
| 0.4 | 0.03512 | 0.00450 | 0.00243 | 1.85 |
| 0.5 | 0.06494 | 0.00636 | 0.00339 | 1.88 |
| 0.6 | 0.12160 | 0.00899 | 0.00475 | 1.89 |

A near-scale-invariant spectrum makes σ_r **logarithmically IR-sensitive**, so the IR
cutoff is scanned rather than hidden (the committed integrator's grid edge is
k_min/k_p = 10⁻⁵):

| k_min/k_p | γ_cr | A(−35/16) at f_PBH = 10⁻³ |
|---|---|---|
| 1e−5 (grid edge) | 0.2668 | 0.00636 |
| 1e−3 | 0.3581 | 0.00941 |
| 1e−2 | 0.4458 | 0.01317 |
| 1e−1 | 0.6298 | 0.02652 |

**A factor 4 across the whole scan — against a shortfall of 10⁷.** The verdict is not
IR-cutoff sensitive.

**One genuine extension of the A3-1 result.** The scale-invariant shape gives
γ_cr ≈ 0.27–0.63, *below* the γ_cr ∈ [0.766, 0.968] range the lognormal grid of
`PBH_COMPACTION_NOTE` spanned. There the required-amplitude ratio was
A(−35/16)/A(−35/8) = **1.732 ± 0.050**; here it is **1.85–1.89**. So the ratio is stable
at the ~10% level over a much wider γ_cr range than previously tested, but the A3-1
quoted range [1.610, 1.809] does **not** cover this shape — the honest combined statement
is **≈1.7–1.9**, and the A3 paper should say so rather than quoting 1.73 ± 0.05 as if it
were universal.

---

## 4. FIRAS μ-distortion

μ = 2.2 ∫ dlnk Δ²_ζ(k) [e^{−k/5400 Mpc⁻¹} − e^{−(k/31.6 Mpc⁻¹)²}]
[LITERATURE: Chluba, Erickcek & Ben-Dayan 2012, arXiv:1203.2681]; bound
|μ| < 9×10⁻⁵ (95% CL, COBE/FIRAS, Fixsen et al. 1996).

**The lab's own spectrum is comfortably allowed:** μ = **1.65×10⁻⁸** (n_s = 0.9649) and
**2.24×10⁻⁸** (pure dust) — 1.8×10⁻⁴ and 2.5×10⁻⁴ of the FIRAS bound. The maximum
k-independent Δ²_ζ FIRAS permits over the window is **8.43×10⁻⁶**.

### 4.1 Ledger #6 — the early-SMBH seed channel

A seed of 10³–10⁶ M_⊙ crosses the horizon at k ~ 10³–10⁵ Mpc⁻¹, on or just above the μ
window, so **the required seed amplitude is directly constrained**. Required amplitude
here is for f_PBH = 10⁻³ at f_NL = −35/16 (the −35/8 numbers are ~1.9× smaller and reach
the same verdict).

| M_seed | k_seed (Mpc⁻¹) | required Δ²_ζ | μ if broadband | μ if narrow (Δ = 0.5) | verdict |
|---|---|---|---|---|---|
| 10³ M_⊙ | 1.18e5 | 0.01182 | 1.56e−1 (1.7e3×) | 1.90e−6 (0.021×) | broadband **EXCLUDED**, narrow peak allowed |
| 10⁴ M_⊙ | 3.74e4 | 0.01247 | 1.58e−1 (1.8e3×) | 3.18e−4 (3.5×) | **EXCLUDED, both** |
| 10⁵ M_⊙ | 1.18e4 | 0.01319 | 1.60e−1 (1.8e3×) | 5.18e−3 (58×) | **EXCLUDED, both** |
| 10⁶ M_⊙ | 3.74e3 | 0.01401 | 1.64e−1 (1.8e3×) | 1.89e−2 (2.1e2×) | **EXCLUDED, both** |

So the FIRAS answer to ledger #6 is **two-part and must be stated as two parts**:

1. **Any broadband route to PBH SMBH seeds is FIRAS-excluded by ~3 orders of magnitude**,
   for every seed mass 10³–10⁶ M_⊙. This is a *model-independent* statement about the
   required amplitude, not about the lab's model.
2. **A sufficiently narrow peak evades FIRAS only for the lightest seeds** (10³ M_⊙,
   k ≳ 10⁵ Mpc⁻¹, above the window). At 10⁴ M_⊙ and heavier a Δ = 0.5 lognormal peak is
   already 3.5–210× over the bound.

And **the lab's own spectrum is ~7 dex below the required amplitude at every one of these
scales anyway**, so the lab's model does not supply SMBH seeds by this route. Ledger #6's
early-SMBH discriminator is therefore **a null for the matter bounce**, and — as with the
z > 10 abundance discriminator — the honest use is as a *constraint that the model does
not violate*, not as evidence for it.

---

## 5. Verdict

> **The lab's own Δ²_ζ produces no PBHs — by ~7.0 orders of magnitude in curvature
> amplitude, at every candidate mass scale from 10¹⁵ g to 10⁴ M_⊙, at both f_NL = −35/16
> and −35/8, for every f_PBH target from 10⁻³ to 1, over a threshold scan
> C_th ∈ {0.4, 0.5, 0.6} and an IR-cutoff scan spanning 4 decades.** f_PBH is exactly zero
> in double precision (Gaussian-limit log₁₀β ≈ −1.7×10⁹ at the asteroid mass). This is a
> **clean "no"**, not a small number: f_PBH is not quotable in either direction, and the
> channel cannot be a *positive* test of this model.
>
> **The required amplitude for the early-SMBH seed channel is FIRAS-excluded** by ~10³ if
> broadband, and excluded even as a narrow peak for seeds ≥ 10⁴ M_⊙; the lab's own
> spectrum sits 1.8×10⁻⁴ of the FIRAS bound, i.e. safely allowed and far too small.

**What this changes for the A3 paper (§IV, PBH channel).** The channel's dependence on
Choudhury et al.'s unreproducible spectrum is **removed**, and the honest §IV statement
becomes:

* the required-amplitude ratio A(−35/16)/A(−35/8) ≈ **1.7–1.9** (widened from 1.73 ± 0.05
  by this shape's lower γ_cr) remains the robust f_NL-discriminating output;
* **the lab's own spectrum delivers ~10⁻⁹ against a requirement of ~10⁻², so the channel
  is a null for this model** — it constrains nothing and predicts nothing, and any
  quotable PBH signal would require an added small-scale amplification mechanism that the
  model does not contain. This should be stated as a **null**, not as an open promise.

**Integrity record.** The spectrum was fixed by the CMB anchor before any PBH number was
computed and was never adjusted afterwards; no enhancement mechanism was imported; every
number above is emitted by the committed script; literature claims are labelled as
literature and are not used as lab results.

---

## 6. Open items

| # | item | status |
|---|---|---|
| **A3-1b** | in-lab Δ²_ζ at PBH scales | **CLOSED by this note** — the PBH channel is a NULL for the lab's model, 7 dex short |
| **A3-1e** | **NEW** — PBHs by *direct collapse during the dust contraction* (Papanikolaou+2024, 2404.03779): a different formation channel that the compaction criterion does not cover and the lab has not tested | OPEN |
| A3-1c | resummed / exact-δN map (quadratic truncation non-perturbative at PBH amplitudes) | OPEN — **now moot for the lab's own spectrum** (which never reaches those amplitudes); still relevant to any comparison with Choudhury et al. |
| A3-1d | γ_cr ≲ 0.85 enhancement branch vs Choudhury et al.'s suppression claim | OPEN — this note's γ_cr ≈ 0.27–0.63 sits deep in the enhancement branch and confirms it is reached by a physically-motivated shape, not only by grid corners |
| A3-3 | SIGW amplitude at nHz from the matter-bounce spectrum | OPEN — **unblocked**: the spectrum this note fixes is the required input |
| ledger #6 | early-SMBH discriminator | **UNBLOCKED and ANSWERED** — FIRAS excludes the broadband seed amplitude; the lab's model does not supply seeds |
