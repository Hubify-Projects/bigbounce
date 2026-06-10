# P2 auto-2026-06-09_0025pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-sonnet-4-6` [FALLBACK from claude-opus-4-7]
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (1370 chars)
**Wall time**: 35624.8s

---

# Referee Report: P2 — "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

## Preliminary Note

All citations in the submitted PDF appear as "[?]" throughout — the bibliography was not compiled. Every observational value cited (βobs, LiteBIRD forecast, Eskilt analysis), every prior-work claim, and every equation convention reference is untraceable. This alone warrants rejection. All further findings below assume the mathematical content stands on its own.

---

## ESSENTIAL ISSUES

**P2-E1: Absent bibliography** [All sections, all pages]
Every one of ~15 citations appears as "[?]". The paper's central numbers (βobs = 0.342 ± 0.094°; σ_LiteBIRD ≈ 0.03°; NPIPE and ACT DR6 values; Fujita et al. 2021 result) have no traceable sources. PRD cannot publish a paper without verifiable citations.

---

**P2-E2: Fundamental inconsistency — spectator condition contradicts birefringence prediction** [Sec. 5, pp. 4–5]

This is the most serious physics error in the paper. Equation (2) gives:
$$\beta = \frac{\alpha_\mathrm{EM} C_{a\gamma}}{4\pi} \cdot \frac{\Delta\phi}{f_a} = \frac{\alpha_\mathrm{EM} C_{a\gamma}}{4\pi} \cdot \theta_i \cdot F(m/H_0)$$
The claim that $f_a$ cancels is correct. However, $\beta \propto \theta_i$: reducing $\theta_i$ reduces $\beta$ proportionally.

Section 5 requires $\theta_i \approx 0.22$ (option a) for the spectator condition $\Omega_\phi \ll 1$ with $f_a \sim M_\mathrm{Pl}$. With $C_{a\gamma} = 8$, $m = 2H_0$, $\Delta\phi/f_a \approx 1.07$ for $\theta_i = 1$, the prediction gives $\beta \approx 0.29°$. Scaling to $\theta_i = 0.22$ (linearly in the small-angle regime) yields:
$$\beta(\theta_i = 0.22) \approx 0.22 \times 0.29° \approx 0.064°$$
This is ~4.5× below the observed signal. To recover $\beta \approx 0.27°$ with $\theta_i = 0.22$ requires $C_{a\gamma} \approx 57$, which is nowhere near "natural DFSZ-type."

The paper states "the $\beta \sim 0.27°$ prediction *continues to hold* by the cancellation above." This is false: the "$f_a$ cancels" argument applies when $f_a$ is varied; it says nothing about what happens when $\theta_i$ is changed. The "spectator" headline parameter point is internally inconsistent with the headline birefringence prediction. The model cannot simultaneously satisfy $\Omega_\phi \ll 1$ (option a), $C_{a\gamma} \sim 8$ (natural), and $\beta \sim 0.27°$ with $f_a \sim M_\mathrm{Pl}$.

*(Note: Option (b), $f_a \sim 0.22\,M_\mathrm{Pl}$, would correctly satisfy both conditions since $f_a$ cancels in $\beta$ while appearing quadratically in $\Omega_\phi$. But the paper explicitly rejects this as "breaking the Planck-scale natural framing.")*

---

**P2-E3: MCMC Neff > total sample count (impossible)** [Sec. 3.3, p. 3]

The paper states "Neff ~ 1,000" for all runs. Run 3 ($\beta$ free) has only 720 accepted samples. Effective sample size cannot exceed the number of accepted samples; Neff > N_accepted is a mathematical impossibility. This invalidates both the Run 3 posterior and the Bayes factor derived from it.

---

**P2-E4: Figure 1 marginals contradict Eq. (8)** [Sec. 3.3, p. 3; Fig. 1, p. 4]

The triangle-plot axis labels show $C_{a\gamma} = 13.4^{+5.6}_{-11}$ and $\theta_i = 1.33^{+0.44}_{-1.1}$. At face value, the product of marginal-peak values is $13.4 \times 1.33 \approx 17.8$, while Eq. (8) reports $C_{a\gamma} \times \theta_i = 3.4 \pm 1.1$ — a factor of ~5 discrepancy. The paper offers no reconciliation. If the posterior is degenerate along $C_{a\gamma} \times \theta_i \approx \mathrm{const}$, the marginal-peak values are physically misleading and should not appear as headline results.

---

**P2-E5: No genuine novelty** [Sec. 7, p. 6]

Section 7 explicitly states: *"Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces $\beta \sim 0.3°$."* The claimed incremental contribution — "specific parameter identification ($f_a \sim M_\mathrm{Pl}$, $m \sim H_0$)" — is identical to what Fujita et al. already showed. The "inference framework" consists of (a) inverse-variance combination of two published measurements (Eq. 3, three lines of algebra) and (b) a 720–6,840 sample MCMC. Neither constitutes a publishable advance. The paper cannot pass the PRD originality bar.

---

**P2-E6: Incomparable σ-values juxtaposed without qualification** [Abstract, pp. 1, 3–4]

The abstract quotes 3.6σ (Eskilt joint Planck+ACT observed signal), 3.9σ (inverse-variance combination of NPIPE + ACT DR6), and 9σ (LiteBIRD forecast) in immediate succession. These are derived from different methodologies, datasets, and statistical frameworks. They are not directly comparable. No "not directly comparable" qualification appears at any of these juxtapositions, violating standard PRD practice.

---

**P2-E7: "fphoton × C0" is undefined and irreproducible** [Abstract; Sec. 3.2; Eq. (5)]

Equation (5), $f_\mathrm{photon} \times C_0 = 1.73 \pm 0.44$, is presented as a key result without ever defining

---

## PASS 2 — self-critique findings (what initial review missed)

## Supplementary Referee Report: Additional Findings for P2

---

### NEW ESSENTIAL ISSUES

**P2-E8: MCMC mass posterior is in the oscillating regime, incompatible with the slow-roll analytic framework** [Sec. 3.3; Fig. 1; Eq. (1)]

The MCMC (Run 2, C free) posterior for the ALP mass peaks at log₁₀(m_a/eV) ≈ −31.4 (visible in Fig. 1). Converting to units of H₀:

$$H_0 \approx 1.44 \times 10^{-33}\ \mathrm{eV} \quad \Rightarrow \quad \log_{10}(H_0/\mathrm{eV}) \approx -32.84$$

$$m_a/H_0 = 10^{-31.4}/10^{-32.84} \approx 27.5$$

The paper's entire analytic framework — Eq. (1), the displacement $\Delta\phi/f_a \approx 0.2\text{–}1.1$, and the birefringence formula — is derived and tabulated for $m/H_0 \in [0.5, 3]$ (slow-roll regime, field frozen until dark-energy era). The MCMC-preferred mass $m_a \approx 27\,H_0$ places the ALP firmly in the **oscillating regime**, where the field begins oscillating at $z_\mathrm{osc}$ satisfying $H(z_\mathrm{osc}) \approx m_a$:

$$H(z)/H_0 = 27 \Rightarrow 0.315(1+z)^3 + 0.685 = 729 \Rightarrow z_\mathrm{osc} \approx 12$$

At $z \approx 12$ (matter domination), the ALP oscillates many times before today. The net birefringence $\beta = (g_{a\gamma}/2)(\phi_0 - \phi_\mathrm{rec})$ for an oscillating field involves many sign-reversing half-cycles between $z = 12$ and $z_\mathrm{rec} = 1100$; the slow-roll displacement