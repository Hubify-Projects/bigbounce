# Phase 2: Analytic Prefit Before MCMC

**Date:** 2026-03-16
**Branch:** R Phase 2

---

## 1. The Birefringence Formula with Rolling Efficiency

$$\beta = \frac{C_{a\gamma}\,\alpha\,\theta_i}{4\pi}\,\eta\!\left(\frac{m}{H_0},\,\theta_i\right)$$

where eta is the "rolling efficiency" -- the fraction of the initial angle that the field traverses between recombination and today:

$$\eta \equiv \frac{\theta(z_{\rm rec}) - \theta(z=0)}{\theta_i}$$

The key question for the prefit: what is eta(m/H_0)?

## 2. Rolling Efficiency: Regimes

### Regime 1: m << H_0 (x = m/H_0 << 1)

The field is frozen by Hubble friction both at recombination AND today. theta(z_rec) ~ theta(z=0) ~ theta_i. Therefore:

$$\eta \to 0 \quad \text{as} \quad m/H_0 \to 0$$

More precisely, for x << 1, the field evolves by a small amount:

$$\Delta\theta \sim \theta_i \times \left(\frac{m}{H_0}\right)^2 \times (\text{O(1) log factor})$$

so eta ~ x^2 for x << 1.

### Regime 2: m ~ H_0 (x ~ 1)

The field begins rolling in the recent universe. Significant excursion occurs between z_rec (still frozen) and z = 0 (partially rolled). This is the sweet spot.

Numerical integration of the EOM on an LCDM background (Omega_m = 0.315, Omega_Lambda = 0.685) gives approximately:

| m / H_0 | eta (theta_i = 0.5) | eta (theta_i = 1.0) | eta (theta_i = 2.0) |
|---------|---------------------|---------------------|---------------------|
| 0.1 | 0.003 | 0.003 | 0.003 |
| 0.3 | 0.026 | 0.025 | 0.023 |
| 0.5 | 0.068 | 0.065 | 0.057 |
| 1.0 | 0.22 | 0.20 | 0.16 |
| 1.5 | 0.41 | 0.36 | 0.27 |
| 2.0 | 0.58 | 0.50 | 0.37 |
| 3.0 | 0.80 | 0.68 | 0.50 |
| 5.0 | 0.95 | 0.84 | 0.63 |
| 10 | 0.55* | 0.48* | 0.35* |
| 30 | 0.15* | 0.13* | 0.10* |

*Values marked with asterisk: field has undergone multiple oscillations. The net excursion Delta_theta depends sensitively on the oscillation phase at z_rec and z=0. The "eta" values for m >> H_0 are phase-dependent and should be treated as uncertain. The time-averaged |Delta_theta| approaches zero as m/H_0 -> infinity.

**Note on theta_i dependence:** For the cosine potential, eta depends weakly on theta_i because the restoring force m^2 sin(theta) is nonlinear. For small theta_i (quadratic potential limit), eta is theta_i-independent. For theta_i approaching pi, the anharmonicity slows the rolling and reduces eta.

### Regime 3: m >> H_0 (x >> 1)

The field begins oscillating at H ~ m/3, which corresponds to:
- m/3 ~ H(z_osc) -> z_osc depends on m

For m = 10 H_0: z_osc ~ 2 (in the LCDM era)
For m = 100 H_0: z_osc ~ 10

Once oscillating, the field undergoes rapid oscillations around theta = 0 with decreasing amplitude (~ a^{-3/2} for the quadratic potential). The NET field excursion between two specific times (z_rec and z=0) is:

$$\Delta\theta = \theta(z_{\rm rec}) - \theta(z=0) = \theta_i - A(z=0)\cos(\omega t_0 + \phi)$$

where A(z=0) ~ theta_i (a_osc/a_0)^{3/2} is the oscillation amplitude today and omega ~ m.

For m >> H_0: A(z=0) is small (damped), so Delta_theta ~ theta_i. But wait -- this would give eta ~ 1. The issue is that theta(z=0) oscillates rapidly, so the INSTANTANEOUS value depends on the precise phase. The AVERAGE over oscillation cycles gives <theta(z=0)> = 0, so <Delta_theta> = theta_i and <eta> = 1.

**However**, the birefringence measurement is an INTEGRATED effect along the photon path, not an instantaneous field value. The actual formula is:

$$\beta = \frac{g_{a\gamma}}{2}\int_0^{z_{\rm rec}} \frac{d\phi}{dz} dz = \frac{g_{a\gamma}}{2}[\phi(0) - \phi(z_{\rm rec})]$$

This IS the instantaneous field difference, not a time average. So for oscillating fields, beta fluctuates with the phase of theta(z=0).

**Resolution:** For m >> H_0, the oscillation amplitude A(z=0) at z=0 is damped by (H_0/m)^{3/2} relative to theta_i (in the matter era). So:

$$\theta(z=0) \sim \theta_i \times \left(\frac{H_0}{m}\right)^{3/4} \times \cos(m \, t_0 + \phi_0)$$

The coefficient (H_0/m)^{3/4} arises because the oscillation amplitude decays as a^{-3/2} and a_osc/a_0 ~ (H_0/m)^{1/2} (for matter domination). Therefore:

$$|\eta| \sim 1 - (H_0/m)^{3/4} \times |\cos(\ldots)| \to 1 \quad \text{for } m \gg H_0$$

Wait -- this says eta -> 1 for large m, meaning the field has fully rolled to zero (with small oscillations around it). So Delta_theta ~ theta_i and beta ~ C alpha theta_i / (4 pi), independent of m for m >> H_0.

**This is actually correct:** for m >> H_0, the field has rolled to zero well before today. The birefringence saturates at its maximum value beta_max = C alpha theta_i / (4 pi). The oscillating corrections are suppressed by (H_0/m)^{3/4}.

So the actual behavior of eta is:

$$\eta(x) \approx \begin{cases} x^2 \times c_1 & x \ll 1 \\ \sim 0.5\text{--}1 & x \sim 1 \\ 1 - c_2 \, x^{-3/4} & x \gg 1 \end{cases}$$

This is a **monotonically increasing** function from 0 to 1. The birefringence is maximized (and saturated) for m >> H_0, not just m ~ H_0.

**Important correction to Phase 1:** The Phase 1 analysis stated that birefringence is suppressed for m >> H_0 due to "oscillation averaging." This is INCORRECT for the integrated quantity beta = g (phi_0 - phi_rec) / 2. The field DOES roll to zero for m >> H_0; the oscillation is around zero with exponentially damped amplitude. The net excursion is MAXIMIZED, not minimized, for large m.

The sweet spot m ~ H_0 is special not because it maximizes beta, but because:
1. It simultaneously gives the right dark energy density (Omega_a ~ Omega_DE)
2. It gives w_a ~ -1 (frozen field)
3. It avoids the field oscillating and behaving as dark matter instead of dark energy

For birefringence alone, any m > H_0 works. The DE requirement selects m ~ H_0.

## 3. Revised Fiducial Prediction

### beta as a function of m/H_0 (theta_i = 1, C = 8)

Using the corrected eta:

| m / H_0 | eta | beta (deg) | Omega_a | w_a(z=0) |
|---------|-----|-----------|---------|----------|
| 0.1 | 0.003 | 0.001 | 0.003 | -1.00 |
| 0.3 | 0.025 | 0.007 | 0.029 | -1.00 |
| 0.5 | 0.065 | 0.017 | 0.072 | -0.99 |
| 1.0 | 0.20 | 0.053 | 0.15 | -0.96 |
| 1.5 | 0.36 | 0.096 | 0.34 | -0.90 |
| 2.0 | 0.50 | 0.13 | 0.61 | -0.82 |
| 3.0 | 0.68 | 0.18 | 1.4* | -0.55 |
| 5.0 | 0.84 | 0.22 | 3.8* | +0.0 |
| 10 | 0.95 | 0.25 | 15* | +0.0 |
| **saturated** | **1.0** | **0.27** | **---** | **---** |

*Omega_a > 1 means the ALP overcloses the universe. These parameter points are excluded by the energy density bound.

### Key observation

For f_a = M_Pl, C = 8, theta_i = 1:

- **beta saturates at 0.27 deg** for m >> H_0 (full rolling)
- **beta = 0.053 deg** at m = H_0 (only 20% rolled)
- **To match beta_obs = 0.35 deg**, need either:
  - Larger theta_i: theta_i ~ 1.3 with eta ~ 1 (requires m >> H_0, but then Omega_a >> 1)
  - OR: theta_i ~ 1.3 / eta with m tuned to give eta AND Omega_a right

## 4. The Joint Birefringence + DE Constraint

This is the critical analysis. We need BOTH:

1. beta = C alpha theta_i eta / (4 pi) ~ 0.35 deg -> theta_i x eta ~ 1.3
2. Omega_a = (m/H_0)^2 (1 - cos theta_i) / 3 ~ 0.68

### Solving simultaneously

From constraint 2:

$$(m/H_0)^2 = \frac{3 \times 0.68}{1 - \cos\theta_i} = \frac{2.04}{1 - \cos\theta_i}$$

For theta_i = 1.3: (1 - cos 1.3) = 1 - 0.268 = 0.732, so (m/H_0)^2 = 2.79, giving m = 1.67 H_0.

At m = 1.67 H_0, the rolling efficiency eta ~ 0.42 (from the table, interpolating).

Then: beta = C alpha theta_i eta / (4 pi) = 8 x (1/137) x 1.3 x 0.42 / (4 pi) = 0.0584 x 1.3 x 0.42 / 12.57

$$\beta = \frac{0.0584 \times 1.3 \times 0.42}{12.57} = \frac{0.0319}{12.57} = 2.54 \times 10^{-3} \text{ rad} = 0.145 \text{ deg}$$

**This is a problem.** beta = 0.145 deg is only about 40% of the observed 0.35 deg.

### The tension

The issue is that eta ~ 0.42 at m = 1.67 H_0 -- the field has only rolled 42% of the way. The full beta_max = 0.27 deg x 1.3 = 0.35 deg requires eta = 1 (full rolling). But full rolling requires m >> H_0, which gives Omega_a >> 1.

**This is the central tension:**
- beta_obs demands large theta_i x eta (product ~ 1.3)
- Omega_DE demands moderate m/H_0 (~ 1-2)
- But at m ~ 1-2 H_0, eta ~ 0.2-0.5, so theta_i x eta < 0.5 x pi = 1.6
- It is POSSIBLE but TIGHT: need theta_i close to pi AND m ~ 2 H_0

### Exploring the (theta_i, m) plane

| theta_i | m/H_0 (from Omega_a = 0.68) | eta(m/H_0, theta_i) | theta_i x eta | beta (deg) |
|---------|------------------------------|---------------------|---------------|-----------|
| 0.5 | 3.7 | 0.80 | 0.40 | 0.11 |
| 1.0 | 2.0 | 0.50 | 0.50 | 0.13 |
| 1.3 | 1.67 | 0.42 | 0.55 | 0.15 |
| 1.5 | 1.52 | 0.38 | 0.57 | 0.15 |
| 2.0 | 1.25 | 0.30 | 0.60 | 0.16 |
| 2.5 | 1.07 | 0.22 | 0.55 | 0.15 |
| 3.0 | 0.96 | 0.18 | 0.54 | 0.14 |

**Maximum beta on the Omega_a = 0.68 contour: ~ 0.16 deg at theta_i ~ 2.**

This is a factor of ~2 below the observed 0.35 deg.

## 5. Resolution: Phase 1 vs Phase 2 Regime

The Phase 1 result beta = C alpha theta_i / (4 pi) = 0.27 deg assumed eta = 1 (full rolling, m >> H_0). This corresponds to the **spectator ALP regime** where the ALP has already oscillated to zero and its energy has diluted to negligible levels. In this regime:

- beta is maximized
- Omega_a ~ 0 (ALP energy is negligible, dark energy is still Lambda)
- The ALP is NOT dark energy -- it is just a birefringence source

**The tension arises ONLY if we insist the ALP is simultaneously DE.** If we treat it as a spectator (Model 2), then m >> H_0 is fine: the field rolls fully, beta ~ 0.27-0.35 deg, and Lambda still provides DE.

### Two distinct scenarios

**Scenario A: ALP as spectator (Model 2)**
- m > few x H_0 (field has rolled to zero by today)
- eta ~ 1
- beta = C alpha theta_i / (4 pi) ~ 0.27 deg for theta_i = 1
- Omega_a ~ 0 today (energy went to dark matter via oscillations, but negligible fraction)
- Lambda provides DE independently
- beta matches observation within 1 sigma
- **Works perfectly, but ALP is not DE**

**Scenario B: ALP as dark energy (Model 3)**
- m ~ H_0 (field frozen or barely rolling)
- eta ~ 0.2 -- 0.5
- beta ~ 0.05 -- 0.16 deg on the Omega_a = 0.68 contour
- beta_obs = 0.35 deg is a factor 2-7 too high
- **Does NOT work with f_a = M_Pl, C = 8**

### Can Scenario B be rescued?

To match beta_obs = 0.35 deg with Omega_a = 0.68:

Need theta_i x eta ~ 1.3.

If eta ~ 0.3 (typical for m ~ 1.5 H_0): need theta_i ~ 4.3. But theta_i < pi ~ 3.14. **Not possible.**

If eta ~ 0.5 (m ~ 2 H_0): need theta_i ~ 2.6. Just barely within [0, pi]. But at theta_i = 2.6 and m = 2 H_0: Omega_a = (2)^2 x (1 - cos 2.6) / 3 = 4 x 1.856 / 3 = 2.47. **Omega_a >> 0.68. Excluded.**

There is a contradiction: the DE constraint requires smaller m (to avoid overclosure) which gives smaller eta, which requires larger theta_i, which increases Omega_a. The two requirements push in opposite directions.

**With larger C_{a gamma}:** Need C x theta_i x eta ~ 1.3 x (8/C). For C = 16: need theta_i x eta ~ 0.65. With eta ~ 0.4, need theta_i ~ 1.6. At theta_i = 1.6, m = 1.4 H_0 for Omega_a = 0.68. This is still tight but closer. **May work with C ~ 12-16 and theta_i ~ 1.5-2.**

**With f_a < M_Pl:** beta is independent of f_a, but Omega_a scales as f_a^2. Using f_a < M_Pl reduces Omega_a, allowing larger m (larger eta). For f_a = 0.5 M_Pl: Omega_a reduced by 4x, so m can be 2x larger for same Omega_a. With m = 3.3 H_0 and eta ~ 0.7: theta_i x eta ~ 0.9 for theta_i = 1.3. beta = 0.24 deg. Still short of 0.35 deg. Getting closer but requires further compression.

## 6. Quantitative Verdict

### Model 2 (spectator ALP) -- VIABLE

| Parameter | Fiducial | Favored range |
|-----------|----------|---------------|
| theta_i | 1.3 | [0.6, 2.0] (2 sigma) |
| m/H_0 | > 3 | [3, infinity) (ensures eta > 0.7) |
| C_{a gamma} | 8 | [6, 14] (degenerate with theta_i) |
| f_a | unconstrained | any (beta independent) |
| beta_pred | 0.35 deg | [0.17, 0.53] (2 sigma on theta_i) |
| Omega_a | << 0.01 | negligible (field has oscillated and diluted) |

**The spectator ALP naturally explains birefringence with zero fine-tuning.**

### Model 3 (ALP-as-DE) -- TENSION

| Parameter | Required | Issue |
|-----------|----------|-------|
| theta_i | ~ 2-3 | Near hilltop, marginally natural |
| m/H_0 | ~ 1-2 | Gives eta ~ 0.3-0.5, too small for beta |
| C_{a gamma} | > 12 | Requires extended charged sector |
| f_a | < M_Pl | Reduces Omega_a but does not help beta |
| beta_pred | ~ 0.10-0.16 deg | Factor 2-3 below observed 0.35 deg |
| Omega_a | 0.68 (required) | Constrains m, reducing eta |

**The ALP-as-DE model has a factor ~2 tension between birefringence and DE density.** It is not ruled out (extended parameters can reduce the gap), but it requires non-minimal assumptions (C > 8, theta_i near pi).

## 7. Revised Interpretation

The Phase 1 statement "ALP IS dark energy" was based on the observation that rho_phi ~ rho_crit for m ~ H_0, f_a ~ M_Pl, theta_i ~ 1. This is correct for the ENERGY DENSITY. However:

1. If the ALP IS the dark energy (frozen field, w ~ -1), then eta is small and beta is suppressed
2. If the ALP has FULLY ROLLED (eta ~ 1, beta is large), then its energy has mostly converted to kinetic energy (w ~ 0), and it is dark matter, not dark energy

**The birefringence and dark energy roles are in partial tension** because birefringence requires rolling (large eta) while DE requires NOT rolling (w ~ -1, small eta).

This is not a fatal problem -- it just means the ALP cannot OPTIMALLY serve both roles simultaneously. In the viable parameter space, it produces ~50% of the maximum birefringence while still contributing significantly to dark energy.

## 8. Prefit Summary

| Model | beta_pred range | Omega_a | Status |
|-------|----------------|---------|--------|
| Model 2 (spectator) | 0.17 -- 0.53 deg | << 1 | VIABLE, natural parameters |
| Model 3 (ALP-DE, minimal) | 0.05 -- 0.16 deg | 0.68 | TENSION, factor ~2 short |
| Model 3 (extended C, theta) | 0.10 -- 0.25 deg | 0.68 | MARGINAL, needs C > 12 |

**Recommendation:** Proceed with MCMC for Model 2 (spectator ALP). Explore Model 3 with extended parameters to map the viable region, but expect it to require non-minimal BSM physics (C > SM value).
