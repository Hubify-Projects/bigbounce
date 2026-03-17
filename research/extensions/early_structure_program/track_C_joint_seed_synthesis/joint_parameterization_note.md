# Track C — Joint Seed Synthesis

## Parameterization Note

**Status:** Specification draft
**Date:** 2026-03-13
**Depends on:** Track A (model_spec.md), Track B (model_spec.md)

---

## 1. Can Tracks A and B Share a Parameterization?

**Yes.** Both tracks are ultimately driven by the same underlying quantity: the primordial power spectrum $\mathcal{P}(k)$ at small comoving scales. A single P(k) modification simultaneously determines:

- The halo mass function modification (Track A input)
- The PBH abundance (Track B input)

The shared parameterization is a P(k) enhancement characterized by:

$$
\mathcal{P}(k) = \mathcal{P}_{\rm standard}(k) \times \left[1 + A_{\rm bump} \exp\!\left(-\frac{(\ln k/k_{\rm bump})^2}{2\Delta_k^2}\right)\right]
$$

where $(A_{\rm bump}, k_{\rm bump}, \Delta_k)$ are the three shared parameters.

## 2. Shared Parameter: $A_{\rm bump}(k)$

| Parameter | Symbol | Role in Track A | Role in Track B |
|-----------|--------|----------------|----------------|
| Bump amplitude | $A_{\rm bump}$ | Sets the fractional increase in $\sigma(M)$, hence halo abundance | Sets $\beta(M)$ and $f_{\rm PBH}(M)$ |
| Bump scale | $k_{\rm bump}$ | Determines which halo mass scale is enhanced | Determines the PBH mass scale: $M_{\rm PBH} \propto k_{\rm bump}^{-2}$ |
| Bump width | $\Delta_k$ | Controls the mass range of enhanced halos | Controls the PBH mass function width |

The key insight: both outputs are monotonically increasing functions of $A_{\rm bump}$. Larger P(k) enhancement produces both more massive halos (good for SMBH seeds) AND more PBHs (potentially violating constraints). The joint analysis finds where enhancement is helpful but not excluded.

## 3. Track A Output: Enhanced Halo Abundance

For each $(A_{\rm bump}, k_{\rm bump})$, Track A computes:

1. **Modified variance:** $\sigma^2(M) = \int \mathcal{P}(k)\,W^2(kR)\,d\ln k$ with the enhanced P(k)
2. **Modified halo mass function:** using Press-Schechter or Sheth-Tormen formalism with the modified $\sigma(M)$
3. **Enhancement factor:** $\eta(M, z) = n_{\rm enhanced}(M, z) / n_{\rm standard}(M, z)$, the fractional increase in halo number density at mass $M$ and redshift $z$
4. **DCBH host abundance:** the number density of halos with $M > M_{\rm min,DCBH}$ (typically $\sim 10^7\text{--}10^8\,M_\odot$ at $z \sim 15\text{--}25$) where DCBH formation conditions can be met

The relevant mass scales for SMBH seeds correspond to comoving wavenumbers:

$$
k_{\rm halo} \sim 10^5\text{--}10^6\,\mathrm{Mpc}^{-1}
$$

which map to halo masses $M_{\rm halo} \sim 10^6\text{--}10^8\,M_\odot$ at $z \sim 20$.

## 4. Track B Output: PBH Constraints

For each $(A_{\rm bump}, k_{\rm bump})$, Track B computes:

1. **Density variance:** same $\sigma^2(M)$ integral (same code)
2. **PBH formation fraction:** $\beta(M) \approx \mathrm{erfc}(\delta_c / (\sqrt{2}\,\sigma(M)))$
3. **Present-day PBH abundance:** $f_{\rm PBH}(M)$ from $\beta(M)$
4. **Constraint comparison:** is the predicted $f_{\rm PBH}(M)$ below all observational upper limits from PBHbounds?

The output is a binary mask on $(A_{\rm bump}, k_{\rm bump})$ space: **allowed** (below all constraints) or **excluded** (violates at least one constraint).

## 5. Joint Analysis: The Allowed Window

The central question: is there a region in $(A_{\rm bump}, k_{\rm bump})$ space where P(k) enhancement:

- Significantly increases massive halo abundance at $z > 15$ (alleviating the SMBH seed problem), AND
- Does not overproduce PBHs beyond observational constraints?

### Why a window might exist

The SMBH seed problem requires P(k) enhancement at $k \sim 10^5\text{--}10^6\,\mathrm{Mpc}^{-1}$, corresponding to mass scales $M \sim 10^3\text{--}10^6\,M_\odot$. At these masses, the PBH constraints are:

| Constraint channel | Upper limit on $f_{\rm PBH}$ | Source |
|-------------------|------------------------------|--------|
| CMB accretion | $\sim 10^{-3}\text{--}10^{-5}$ | Ali-Haimoud & Kamionkowski 2017 |
| Wide binary disruption | $\sim 10^{-2}\text{--}10^{-3}$ | Monroy-Rodriguez & Allen 2014 |
| Dynamical friction (dwarfs) | $\sim 10^{-3}\text{--}10^{-4}$ | Brandt 2016 |
| X-ray/radio accretion | $\sim 10^{-4}\text{--}10^{-6}$ | Manshanden et al. 2019 |

These are among the weaker constraints in the full PBH mass spectrum (compare to $f_{\rm PBH} \lesssim 10^{-10}$ from microlensing at $\sim 10^{-7}\,M_\odot$).

### Threshold analysis

The P(k) enhancement needed for significant halo abundance increase is MUCH smaller than that needed for PBH formation:

- **Halo enhancement:** $\sigma(M)$ increases by $\sim 10\%$ require $\mathcal{P}(k_{\rm bump}) \sim \mathrm{few} \times 10^{-9}$ (modest enhancement)
- **PBH formation:** requires $\mathcal{P}(k_{\rm bump}) \sim 10^{-2}$ (enormous enhancement)

This six-order-of-magnitude gap suggests that the halo-enhancement regime is comfortably below PBH constraints. The joint figure will quantify this.

## 6. Key Finding Preview

There IS likely a viable window, but for a reason that is almost trivial: the P(k) enhancement needed to significantly modify the halo mass function is vastly smaller than the enhancement needed to produce PBHs. PBH constraints only become relevant if one pushes to $\mathcal{P}(k) \gtrsim 10^{-2}$, while meaningful halo modifications occur at $\mathcal{P}(k) \sim 10^{-8}$.

The more interesting question is whether the bounce framework actually produces ANY enhancement at these scales. That remains an open calculation.

## 7. Recommendation: Separate Build, Joint Figure

### Build separately

Tracks A and B should be implemented as separate modules because:

- **Different observational data:** Track A uses high-z SMBH catalogs; Track B uses PBHbounds constraint curves
- **Different validation:** Track A validates against known SMBH growth models; Track B validates against published PBH constraint figures
- **Different audiences:** Track A connects to the SMBH/galaxy formation community; Track B connects to the PBH/dark matter community
- **Independent utility:** Each track produces publishable results without the other

### Combine for joint constraint figure

The joint analysis produces a single figure that is greater than the sum of its parts:

**Joint constraint figure specification:**
- x-axis: $k_{\rm bump}$ (Mpc$^{-1}$, log scale)
- y-axis: $\mathcal{P}(k_{\rm bump})$ (log scale)
- Color regions:
  - **Red:** excluded by PBH overproduction (above all observational constraints)
  - **Blue:** produces > 10x enhancement in massive halo abundance at $z = 20$
  - **Green overlap:** the allowed window (if it exists)
  - **Gray dashed:** FIRAS $\mu$-distortion constraint
  - **Gray dotted:** projected PIXIE sensitivity
- Vertical band: the $k$ range relevant for SMBH seeds ($10^5\text{--}10^6\,\mathrm{Mpc}^{-1}$)

### Shared infrastructure

Both tracks share:
- `cosmology_utils.py` — $t(z)$, $D(z)$, $H(z)$ calculations (Planck 2018 parameters)
- `pk_model.py` — parameterized P(k) with bump
- `sigma_M.py` — $\sigma^2(M)$ integration with window functions
- These should live in a shared `../shared/` directory

## 8. Open Questions for Implementation

1. **Window function choice:** top-hat vs Gaussian smoothing affects $\sigma(M)$ by $\mathcal{O}(1)$ factors. Use top-hat for halo mass function (standard), Gaussian for PBH (conventional).

2. **Critical collapse scaling:** PBH masses are not exactly $M_H$ at horizon crossing — there is a critical scaling $M_{\rm PBH} = K M_H (\delta - \delta_c)^\gamma$ with $\gamma \approx 0.36$. This broadens the PBH mass function even for monochromatic P(k). Include for accuracy.

3. **Non-Gaussianity:** the bounce could produce non-Gaussian perturbations, which would modify both the halo mass function AND the PBH formation rate. This is a second-order effect that can be parameterized but not predicted without the perturbation calculation.

4. **Spectral distortion cross-check:** enhanced P(k) at $k \sim 10^5\,\mathrm{Mpc}^{-1}$ is above the FIRAS $\mu$-distortion window ($k \sim 1\text{--}10^4\,\mathrm{Mpc}^{-1}$). Need to verify this scale is not constrained by $\mu$- or $y$-distortions.
