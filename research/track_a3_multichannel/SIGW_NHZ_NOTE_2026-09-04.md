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
