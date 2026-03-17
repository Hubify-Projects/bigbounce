# 03: Detector Band Comparison

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Detector Sensitivity Bands

| Detector / Concept | Frequency Band | Status | Circular Polarization Sensitivity? |
|-------------------|---------------|--------|-----------------------------------|
| NANOGrav / IPTA | 1–100 nHz | Operating (15yr data) | Yes (Gair et al. formalism) |
| LISA | 0.1–100 mHz | Approved, launch ~2035 | Yes (cross-correlation channels) |
| DECIGO / BBO | 0.1–10 Hz | Proposed | Yes (multiple spacecraft) |
| Einstein Telescope (ET) | 1–10⁴ Hz | Funded, ~2035 | Yes (triangular configuration) |
| LIGO/Virgo/KAGRA | 10–5000 Hz | Operating (O4) | Limited |
| High-frequency GW concepts | 10⁶–10¹² Hz | Speculative R&D | Very limited |

---

## ECH Bounce Signal: f_0 ~ 10⁹–10¹⁰ Hz (GHz)

### Overlap with detectors

| Detector | Overlap? | Gap (orders of magnitude) |
|----------|----------|--------------------------|
| PTA (nHz) | **NO** | 18 orders |
| LISA (mHz) | **NO** | 12 orders |
| DECIGO (Hz) | **NO** | 9 orders |
| ET (Hz–kHz) | **NO** | 6 orders |
| LIGO (10 Hz–kHz) | **NO** | 6 orders |
| High-f concepts (MHz–GHz) | **MARGINAL** | 0–1 orders |

### High-frequency GW detector concepts

Several groups have proposed detection methods for GWs in the MHz–GHz range:
- **Bulk acoustic wave resonators** (10⁶–10⁹ Hz): Aggarwal et al. 2021
- **Magnon-graviton conversion** (10⁸–10¹⁰ Hz): Ito et al. 2020
- **Inverse Gertsenshtein effect** (10⁹–10¹² Hz): Li et al. 2009
- **Levitated sensors** (10⁴–10⁸ Hz): Arvanitaki et al. 2013

**Status:** All of these are at the concept or early prototype stage. No detector has demonstrated sensitivity to GWs above ~10 kHz. The strain sensitivity of proposed MHz–GHz detectors is typically h ~ 10⁻²⁰–10⁻²², which is far worse than LIGO's h ~ 10⁻²³ at 100 Hz.

**Can the ECH chiral signal be detected by these?** Depends on the signal amplitude. The SGWB amplitude from the bounce scales as:

$$
\Omega_{\rm GW}(f) \sim \frac{\rho_{\rm GW}(f)}{\rho_{\rm crit,0}} \sim r \times \frac{\rho_\gamma}{\rho_{\rm crit,0}} \times \left(\text{spectral shape}\right)
$$

For Planck-scale bounce: the tensor-to-scalar ratio for modes near k_b is not suppressed (T ~ O(1)). But the spectral energy density falls off for modes far from the peak. A rough estimate: Ω_GW ~ 10⁻⁶–10⁻⁵ at the GHz peak (from BBN/CMB bounds on the total GW energy density).

With Ω_GW ~ 10⁻⁶ at f ~ 10 GHz, the strain is:

$$
h_c(f) = \sqrt{\frac{3H_0^2}{2\pi^2 f^2}\Omega_{\rm GW}} \sim 10^{-30}
$$

This is **8–10 orders of magnitude below** even the most optimistic high-frequency detector projections.

**No realistic high-frequency detector can see this signal.**

---

## Lower-bounce-energy scenarios

If we allow ρ_bounce < ρ_crit^{ECH}:

| ρ^{1/4}_bounce | f_0 | Detector | Ω_GW estimate | Detectable? |
|----------------|-----|----------|---------------|-------------|
| 10¹⁸ GeV (ECH) | 10¹⁰ Hz | None | ~10⁻⁶ | NO |
| 10¹⁶ GeV (GUT) | 10⁸ Hz | High-f concepts | ~10⁻⁶ | NO (too faint) |
| 10¹⁰ GeV | 10² Hz | ET/LIGO | ~10⁻⁶ × (10¹⁰/10¹⁸)⁴ ~ 10⁻³⁸ | NO (amplitude vanishes) |
| 10⁶ GeV | 10⁻² Hz | LISA | ~10⁻³⁸ × ... | NO |
| 1 GeV | 10⁻⁸ Hz | PTA | ~10⁻⁵⁴ × ... | NO |

**Wait — there's a crucial subtlety.** The SGWB amplitude from the bounce depends on the bounce energy scale. For a lower-energy bounce:

$$
\Omega_{\rm GW} \propto \frac{\rho_{\rm bounce}}{M_{\rm Pl}^4} \propto \left(\frac{\rho^{1/4}_{\rm bounce}}{M_{\rm Pl}}\right)^4
$$

A bounce at 10¹⁰ GeV has:

$$
\frac{\Omega_{\rm GW}^{10^{10}}}{\Omega_{\rm GW}^{\rm Planck}} \sim \left(\frac{10^{10}}{10^{18}}\right)^4 = 10^{-32}
$$

The signal amplitude at the bounce is suppressed by (ρ_bounce/M_Pl⁴)², and the chirality fraction Δ_h is also suppressed (parity coupling weaker at lower curvature). **Lowering the bounce energy to reach observable frequencies simultaneously kills the signal amplitude.**

This is the fundamental frequency-amplitude trade-off:
- High bounce energy → strong signal but at GHz (undetectable)
- Low bounce energy → accessible frequency but negligible amplitude

---

## The Frequency-Amplitude No-Go

For any bounce signal:

$$
f_0 \propto T_{\rm bounce} \propto \rho_{\rm bounce}^{1/4}
$$

$$
\Omega_{\rm GW} \propto \rho_{\rm bounce}^2 / M_{\rm Pl}^4 \propto f_0^8
$$

To get from f_0 = 10¹⁰ Hz (GHz) to f_0 = 10⁻³ Hz (LISA):

$$
\frac{f_0^{\rm LISA}}{f_0^{\rm ECH}} = 10^{-13}
$$

$$
\frac{\Omega_{\rm GW}^{\rm LISA}}{\Omega_{\rm GW}^{\rm ECH}} = (10^{-13})^8 = 10^{-104}
$$

**The signal amplitude drops by 104 orders of magnitude when the frequency is brought into the LISA band.** This is a fundamental scaling that cannot be evaded by adjusting parameters.

---

## Conclusion

There is **no realistic overlap** between the ECH bounce chiral signal and any current or planned GW detector. The signal is at GHz with adequate amplitude, or at detectable frequencies with negligible amplitude. This is not a parameter-tuning problem — it is a fundamental scaling relation.
