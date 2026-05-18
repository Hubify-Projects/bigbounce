# P1B_v1B015_R11 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 56.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=18699, completion=6921, reasoning=6038, total=25620

---

## Finding 1: Savage-Dickey rewrite inconsistency
**ID:** PAPER-GEM-B1
**Classification:** BLOCKER
**Section:** 7.1
**Issue:** Section 7.1 still promises a "Savage-Dickey $\ln B$ recompute against the LCDM point, queued for v1B.0.13+", directly contradicting Section 3, Section 5.2, and Appendix A which correctly state Savage-Dickey is invalid for $>4\sigma$ tails and requires nested sampling. This fails the round context verification requirement (b).
**Fix:** Update Section 7.1 to remove the Savage-Dickey promise, align with the nested-sampling requirement stated elsewhere, and remove the stale "v1B.0.13+" version references.

## Finding 2: ALP spectator energy density inconsistency
**ID:** PAPER-GEM-M1
**Classification:** MAJOR
**Section:** 6
**Issue:** The text claims an ALP with $f_a \sim M_{\rm Pl}$ and $m \sim H_0$ is a "spectator field". However, its energy density $\rho_a \sim m^2 f_a^2 \sim H_0^2 M_{\rm Pl}^2 \sim \rho_{\rm crit}$ makes it a dominant cosmological component today ($\Omega_a \sim 1$), violating the spectator assumption unless the initial misalignment is fine-tuned ($\theta_i \ll 1$).
**Fix:** Acknowledge that for $f_a \sim M_{\rm Pl}$ and $m \sim H_0$, the ALP contributes $\Omega_a \sim \mathcal{O}(1)$ and requires coupled Friedmann+ALP background modeling, or explicitly restrict the parameter space to $f_a \ll M_{\rm Pl}$ / $\theta_i \ll 1$.

## Finding 3: ALP beta-range arithmetic error
**ID:** PAPER-GEM-M2
**Classification:** MAJOR
**Section:** 6
**Issue:** The text claims the birefringence prediction spans $\beta \approx 0.17^\circ$--$0.43^\circ$ for $C_{a\gamma} \in [4,12]$ and $\Delta\phi/f_a \in [0.2,1.1]$. The lower bound is mathematically incorrect: $4 \times 0.2 \times (\alpha_{\rm EM}/4\pi) \approx 0.027^\circ$, not $0.17^\circ$.
**Fix:** Correct the stated range to $\beta \approx 0.027^\circ$--$0.44^\circ$.

## Finding 4: Horndeski generalization omission
**ID:** PAPER-GEM-m1
**Classification:** minor
**Section:** 7.1
**Issue:** The text claims Quintom-B is the "only class admitted to span the dynamical-equation-of-state window the DESI signal populates", ignoring Horndeski and generalized scalar-tensor theories which can cross the phantom divide without ghosts.
**Fix:** Change "only class" to "simplest canonical class" or explicitly acknowledge Horndeski/EFT of dark energy generalizations.

## Finding 5: SN nuisance marginalization note missing
**ID:** PAPER-GEM-m2
**Classification:** minor
**Section:** Table 2 caption
**Issue:** The caption lists 17 sampled parameters (8 cosmological + 9 Planck nuisance) but fails to state how the Pantheon+ and DES-Y5 nuisance parameters are handled, leaving the degrees of freedom ambiguous.
**Fix:** Add a brief note to the caption stating that SN nuisance parameters are analytically marginalized.

## Finding 6: NaMaster SNR abstract scrub
**ID:** PAPER-GEM-m3
**Classification:** minor
**Section:** Abstract
**Issue:** The abstract still reports the pipeline-recovery "SNR=20.32", which risks being misquoted as a sky-detection significance despite the surrounding caveat text.
**Fix:** Remove the numerical SNR value from the abstract entirely, leaving only the bias recovery statement.
