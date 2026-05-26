# P1B R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R28_P1B_v1B_0_29
**Wall time**: 86.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=25169, completion=10999, reasoning=10034, total=36168

---

## BLOCKER: PAPER-GEM-B1
**Section:** VI (Spectator-ALP Consistency Check)
**Concrete issue:** The paper claims an ALP with $f_a \sim M_{\rm Pl}$ and $m \sim H_0$ is a "spectator field that does not participate in the bounce dynamics." This is physically impossible: for $\theta_i \sim O(1)$, its energy density is $\rho_\phi \sim m^2 f_a^2 \sim H_0^2 M_{\rm Pl}^2 \sim \rho_{\rm crit}$. This field is dynamically dominant (Quintessence), not a spectator. Furthermore, a canonical scalar field cannot cross the phantom divide, directly contradicting the $w_0+w_a = -1.48$ phantom-crossing requirement derived in Table 1B.
**Fix:** Either restrict the ALP to a true spectator regime ($f_a \ll M_{\rm Pl}$ or $m \ll H_0$, requiring much larger $C_{a\gamma}$ to fit $\beta$), or explicitly model it as the Quintessence dark energy component and address the phantom-crossing contradiction.

## MAJOR: PAPER-GEM-M1
**Section:** III (Scope of the $\Delta N_{\rm eff}$ proxy)
**Concrete issue:** The text claims the Hehl-Datta-Mercuri $M_{\rm Pl}^{-2}$-suppressed 4-fermion interaction's "leading Boltzmann effect is a scattering-amplitude shift... and it does not produce a $\Delta N_{\rm eff}$". At recombination ($T \sim 0.3$ eV), the scattering rate is $\Gamma/H \sim (T/M_{\rm Pl})^3 \sim 10^{-84}$. Motivating a $\Delta N_{\rm eff}$ null-test around this is a severe EFT category error; the macroscopic effect is strictly zero, not just a "shift".
**Fix:** Remove the implication that the HDM interaction could have any measurable Boltzmann effect; state explicitly that $M_{\rm Pl}^{-2}$-suppressed contact interactions decouple at recombination by 84 orders of magnitude.

## MAJOR: PAPER-GEM-M2
**Section:** VI (Birefringence value)
**Concrete issue:** The text claims $C_{a\gamma} \in [9, 51]$ is "comfortably within natural ALP-photon coupling ranges." Anomaly coefficients of $O(50)$ are not natural in standard field theory or string compactifications; they require highly engineered UV completions (e.g., clockwork mechanisms or large-charge representations). This overstates mechanism-independence.
**Fix:** Remove the word "natural" for $C_{a\gamma} \sim 51$ and explicitly note that couplings of this magnitude require specific UV model-building (e.g., clockwork).

## minor: PAPER-GEM-m1
**Section:** VI (MCMC parameter estimation)
**Concrete issue:** The paper reports an MCMC yielding $\beta_{\rm ALP} = 0.336^\circ \pm 0.107^\circ$ by sampling ALP parameters ($m/H_0$, $\theta_i$) with fixed $C_{a\gamma}=8$. Because the data only provides a single scalar constraint ($\beta_{\rm obs}$), sampling a 2D parameter space merely returns the prior volume projected along the $\Delta\phi(m, \theta_i) \propto \beta_{\rm obs}$ degeneracy curve. It provides no statistical validation beyond the algebraic point estimate.
**Fix:** Explicitly state that the ALP MCMC is completely prior-dominated along the $(m/H_0, \theta_i)$ degeneracy axis and serves only as a numerical cross-check of the algebraic trajectory scan.

## minor: PAPER-GEM-m2
**Section:** IV (Data Methods: CMB E-B Analysis)
**Concrete issue:** Rotating a foreground-cleaned CMB map by $e^{2i\beta}$ and recovering it with NaMaster only tests the algebraic $E \to B$ mixing of the pseudo-$C_\ell$ estimator. Because there are no unrotated foregrounds, it does not test the physical separation of $\beta$ from miscalibration $\alpha$. Calling this a "pipeline validation" for cosmic birefringence is an overstatement of a trivial algebraic identity check.
**Fix:** Downgrade the framing from "pipeline validation" to "pseudo-$C_\ell$ algebraic recovery check" to accurately reflect the absence of foreground-induced degeneracy breaking.
