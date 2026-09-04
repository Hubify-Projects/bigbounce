# A3-3 — Scalar-induced GWs at nHz from the lab's own curvature spectrum

**Date:** 2026-09-04 · **Ledger:** `NEXT_SCIENCE_LEDGER.md` row 3 (A3-3)
· **Audit item:** `DA3M-R4-02` (MAJOR, SCIENCE) in
`project-context/peer-reviews/INT_v3/A3M_v3M.0.9_R4_TRUTH_AUDIT_2026-09-04.md`
· **Script:** `sigw_nhz_from_lab_spectrum_2026_09_04.py` (to be committed with outputs)

## Plan (header committed before the computation; results appended below)

1. Derive f ↔ k for a mode re-entering in radiation domination; evaluate over the
   NANOGrav band f ∈ [2, 60] nHz.
2. Evaluate the lab's Δ²_ζ(k) (A_s = 2.1e−9, k_* = 0.05 Mpc⁻¹, n_s = 0.9649; plus the
   pure-dust n_s = 1 bracket) at those k, with the A2 scale-independent bounce transfer;
   report kη_B at nHz for each committed background/T_B to test the transfer's
   kη_B ≲ 1e−2 validity domain.
3. Compute Ω_GW(f) with the Kohri–Terada (arXiv:1804.08577) radiation-era kernel,
   numerically integrated over the broad spectrum; fit the local slope across the band
   → γ_pred via Ω_GW ∝ f^{5−γ}; compare amplitude to NANOGrav 15 yr.
4. Determine what nHz spectral shape would give γ=3 (P_R ∝ k), the k_B / T_B / H_B it
   would require, and compare with §V's T_B ≳ 1e8–1e10 GeV.
5. VERDICT (A) null/tension, or (B) a consistent γ=3 statement under stated assumptions.

**Integrity:** no tuning toward γ=3; every number emitted by the committed script.

---

## Results (computed 2026-09-04; every number from the committed script)

**Run:** `sigw_nhz_from_lab_spectrum_2026_09_04.py` → `outputs/sigw_nhz_from_lab_spectrum_2026_09_04.{json,png}`,
stdout `outputs/sigw_nhz_2026_09_04.log`. Local CPU, 3.2 s wall, $0.

### 1. f ↔ k

For a mode re-entering the horizon in radiation domination, f = kc/(2πa₀) with a₀ = 1:

> k [Mpc⁻¹] = 2πf · (Mpc_km / c_km s⁻¹) = **6.4671×10¹⁴ · f[Hz]**

so **k = 6.467×10⁵ Mpc⁻¹ per nHz** — i.e. k(10 nHz) = 6.47×10⁶ Mpc⁻¹, confirming the
audit's §0 figure of ≈6.5×10⁶ Mpc⁻¹. Band endpoints: k(2 nHz) = 1.293×10⁶ Mpc⁻¹,
k(60 nHz) = 3.880×10⁷ Mpc⁻¹, k(f_yr = 31.69 nHz) = 2.049×10⁷ Mpc⁻¹.

### 2. Kernel validation (done BEFORE any lab spectrum was inserted)

The radiation-era induced-GW kernel (Kohri & Terada 2018, arXiv:1804.08577; same form in
Domènech's review arXiv:2109.01398 Eq. (2.21)) was validated against the published closed
form for an exactly scale-invariant P_ζ = A, Ω_GW = 0.8222 A²
(Espinosa–Racco–Riotto 2018; Kohri–Terada 2018):

| quantity | value |
|---|---|
| computed coefficient | **0.822542** |
| published coefficient | 0.8222 |
| relative error | **4.2×10⁻⁴** |

*(A defect was found and fixed in the as-written kernel during this lane: its `I_s` term
carried a 6/(uv) scale error relative to the canonical 3(u²+v²−3)/(4u³v³) prefactor and
returned 0.0738 on this benchmark — an 11× shortfall. Commit `54c77251`. The benchmark is
now an executing assertion in `main()`, so the normalisation cannot silently drift.)*

### 3. Transfer validity at nHz

The A2 bounce transfer is scale-independent only for kη_B ≲ 10⁻². At the hardest point of
the band (60 nHz):

| background | k_B [Mpc⁻¹] | kη_B = k/k_B at 60 nHz |
|---|---|---|
| T_B = 10¹⁶ GeV | 1.71×10²³ | 2.26×10⁻¹⁶ |
| T_B = 10¹⁴ GeV | 1.71×10²¹ | 2.26×10⁻¹⁴ |
| T_B = 10¹⁰ GeV | 1.71×10¹⁷ | 2.26×10⁻¹⁰ |
| T_B = 10⁸ GeV  | 1.71×10¹⁵ | 2.26×10⁻⁸  |

**The transfer is defended here.** Every committed background at or above §V's
T_B ≳ 10⁸ GeV puts the entire PTA band at kη_B ≤ 2.3×10⁻⁸ — six or more orders inside the
validity domain, unlike the k ~ k_B regime where the scale-independent transfer is
unvalidated. So the nHz prediction below is *not* limited by transfer uncertainty; it is a
clean consequence of the CMB-anchored spectrum.

### 4. Ω_GW(f) and the slope from the lab's own spectrum

Δ²_ζ(k) = A_s (k/k_*)^{n_s−1}, A_s = 2.1×10⁻⁹, k_* = 0.05 Mpc⁻¹
(`outputs/inlab_delta2_zeta_2026-09-03.json`), pushed through the validated RD kernel and
redshifted with Ω_GW,0h² = 1.62×10⁻⁵ (g_*/106.75)(g_*s/106.75)^{−4/3} Ω_GW,prod.
Slope fitted over f ∈ [2, 60] nHz; γ_pred ≡ 5 − dlnΩ/dlnf (the paper's own convention,
`pta_gamma_reproduce.py:22–31`).

| background / branch | kη_B at 10 nHz | γ_pred | Ω_GW h² at 10 nHz | NANOGrav 15 yr at 10 nHz |
|---|---|---|---|---|
| MB, CMB-anchored n_s = 0.9649 | 3.8×10⁻⁹ (T_B = 10⁸ GeV); ≤3.8×10⁻¹⁷ (T_B ≥ 10¹⁶ GeV) | **5.070** | **1.62×10⁻²³** | 9.5×10⁻¹⁰ |
| pure-dust bracket n_s = 1 | same | **5.000** | **5.88×10⁻²³** | 9.5×10⁻¹⁰ |
| — NANOGrav 15 yr (A = 2.4×10⁻¹⁵, γ = 3.2) | — | 3.2 ± 0.36 | — | 9.5×10⁻¹⁰ |

The numerical slope reproduces the analytic self-similarity result γ = 5 − 2(n_s − 1) to
1 part in 10⁴ (5.0702 numerical vs 5.0702 analytic; 5.0000 vs 5.0000) — a pure power-law
Δ²_ζ through a scale-free kernel gives Ω_GW ∝ k^{2(n_s−1)} exactly, with no log correction.

Two independent failures against Channel I's γ = 3:

- **Slope.** γ_pred = 5.07, not 3. In NANOGrav's own units that is **5.1σ** from the
  measured γ = 3.2 (using the 90% interval width ±0.6 → σ ≈ 0.36); the pure-dust bracket is
  4.9σ. The honest reading of the lab spectrum is γ ≈ 5 — precisely the row §IV D
  disfavours at 3.1σ/4.63σ. This is a **tension, not a consistency**.
- **Amplitude.** Ω_GW h²(f_yr) = 1.45×10⁻²³ vs the NANOGrav power law's 6.3×10⁻¹⁰:
  a shortfall of **10^14.3** (10^13.7 for the pure-dust bracket). The lab spectrum's induced
  GWs are fourteen orders of magnitude below the PTA signal.

### 5. What spectral shape at nHz WOULD give γ = 3, and what it costs

For a broad power law P_R ∝ k^n in radiation domination the induced spectrum is
Ω_GW ∝ f^{2n} (Domènech arXiv:2109.01398). With γ ≡ 5 − dlnΩ/dlnf, γ = 3 requires
dlnΩ/dlnf = 2, hence

> **n = 1 — i.e. P_R ∝ k¹ sustained across the whole 2–60 nHz band.**

The lab spectrum has n = n_s − 1 = **−0.0351** (or exactly 0 in the pure-dust bracket).
Getting to n = +1 is not a small correction: it is a change of sign and of order unity in
the tilt, over a decade and a half in k, at k ≈ 10⁶–10⁷ Mpc⁻¹.

Amplitude cost, on top of the shape: matching the NANOGrav amplitude at f_yr through
Ω = 0.8222 Δ⁴ needs Δ²_ζ(f_yr) = **1.65×10⁻²**, against the lab's **1.05×10⁻⁹** — a
**10^7.2** enhancement. That is the PBH-forming regime; §V C's headline null (7 decades
short of PBH formation) is exactly the statement that the model does *not* have it. The
two channels cannot both describe this model — which is item DA3M-R4-02's charge, now
confirmed numerically.

Note also that γ = 3 is **not** the universal IR causal tail. That floor is Ω_GW ∝ f³,
i.e. γ = 2 (Cai, Pi & Sasaki 2020, PRD 102 083528, arXiv:1909.13728), and it applies only
below the source's own support. γ = 3 is neither the causal floor nor the flat-spectrum
result; it is specifically the P_R ∝ k¹ case.

**Could a bounce-scale feature supply it?** Only if the feature scale k_B sat inside the
band. k_B ≤ k(60 nHz) = 3.88×10⁷ Mpc⁻¹ requires

> **T_B ≈ 2.3 GeV**, H_B ≈ 7.2×10⁻¹⁸ GeV

i.e. **7.6 decades below** §V's own condition T_B ≳ 10⁸–10¹⁰ GeV, and below the QCD scale.
A bounce that low is excluded by the paper's own BBN/baryogenesis argument for T_B. So the
γ = 3 shape cannot be obtained from a k ~ k_B feature either: it would have to come from an
*additional*, unmotivated, PBH-scale enhancement placed by hand at k ≈ 10⁷ Mpc⁻¹.

## VERDICT — (A) the PTA channel is a null/inconsistency for the CMB-anchored spectrum

**The lab's own committed curvature spectrum gives γ_pred = 5.07 (CMB-anchored) or 5.00
(pure-dust bracket), 5.1σ / 4.9σ from NANOGrav's γ = 3.2, at an amplitude 10^14.3 below the
signal. It does not give γ = 3.** The γ = 3 attribution in §IV D is borrowed from
Papanikolaou 2025's low-k tail, whose spectrum carries a small-scale enhancement that
§V C explicitly denies this model has. Confirmed: the two sections assume mutually
inconsistent spectra, and the lab spectrum sides with §V C.

**What §IV must now say.** §IV D's Channel I must be rewritten from a claimed γ = 3
consistency to a stated null, with three components:

1. **State the model's actual prediction.** From the CMB-anchored Δ²_ζ carried through the
   standard radiation-era induced-GW kernel, γ_pred = 5.07 and Ω_GW h²(f_yr) = 1.45×10⁻²³
   — cite this note and `outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json`.
2. **Delete the Papanikolaou γ = 3 attribution** (`main.tex:585–597`). It borrows the IR
   slope of a *different*, small-scale-enhanced spectrum. Retain the citation only as a
   contrast case, explicitly flagged as requiring an enhancement the model lacks.
3. **Reclassify the channel.** PTA is not a supporting channel and not a constraint: at
   10^14.3 below the signal the model is unconstrained by NANOGrav, and its slope is in
   tension with the observed one *if* one insisted the model sourced the signal. State it
   as a null — "the model predicts an induced-GW background fourteen orders of magnitude
   below the PTA band and does not account for the NANOGrav signal" — and note that a
   γ = 3 statement would require P_R ∝ k¹ plus a 10^7.2 enhancement at k ≈ 10⁷ Mpc⁻¹, or a
   bounce at T_B ≈ 2 GeV, both excluded by §V.

The transfer is not the limitation (kη_B ≤ 2.3×10⁻⁸ across the band), so this null is a
robust consequence of the CMB anchoring, not an artefact of the bounce modelling.

**Integrity note:** nothing was tuned toward γ = 3. The kernel normalisation was fixed
against a published scale-invariant benchmark before any lab spectrum was inserted, and
that benchmark runs as an assertion on every execution.
