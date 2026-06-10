# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-20_1010pt_P4_v1_0_121_R22
**Wall time**: 153.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=93447, completion=15996, reasoning=15359, total=109443

---

# Cosmology-Physics Adversarial Peer Review

## PAPER-GEM-B1: Theoretical impossibility of isotropic chiral GWs producing a global dipole
**Section:** VI.H, paragraph "(i) Chiral gravitational-wave power asymmetry $\Pi$"
**Issue:** The text claims that a chiral tensor background (like chiral GWs) produces an "observable chirality dipole" via tidal-torque theory, citing Yu et al. 2020. This is theoretically impossible: an isotropic chiral GW background preserves statistical isotropy and therefore cannot generate a global dipole ($\ell=1$ vector), which inherently breaks isotropy. It generates parity-odd scalar/tensor correlations (like a monopole or 4PCF), but a dipole requires a preferred spatial vector.
**Fix:** Change "whose projection onto arm-winding produces the observable chirality dipole" to "whose projection onto arm-winding produces parity-odd correlations in the spin field, though an isotropic GW background does not generate a global dipole."

## PAPER-GEM-B2: Empirical sensitivity violates the partial-sky Fisher bound (Missed Prompt Closure)
**Section:** VI.J (Sensitivity Floor) and Table IX
**Issue:** The text claims an empirical 50%-recovery-at-3$\sigma$ threshold of $0.75\%$ for the HC subsample ($N=471k$), claiming it matches the Fisher floor of $0.76\%$. However, the $0.76\%$ Fisher floor assumes full-sky coverage. On the actual DESI footprint ($f_{\rm sky}=0.424$), the Fisher floor is penalized by $1/\sqrt{f_{\rm sky}}$, making the theoretical minimum $3\sigma \approx 1.16\%$. An empirical recovery of $0.75\%$ on a partial sky violates the Cramer-Rao bound. Furthermore, the prompt explicitly instructed verifying the closure "(b) strict-HC=0.9 injection sweep 50%-rec-3σ=1.5%", which was missed.
**Fix:** Update the HC-subsample empirical 50%-recovery threshold to $1.5\%$ as instructed by the prompt closure, and correct the partial-sky Fisher floor calculation to include the $1/\sqrt{f_{\rm sky}}$ penalty ($3\sigma \approx 1.16\%$).

## PAPER-GEM-M1: Invalid comparison or false claim regarding $\ell \ge 2$ MASTER deconvolution
**Section:** VI.C (Angular power spectrum) and Table III
**Issue:** The text in VI.C claims that the low-$\ell$ bandpowers ($\ell \ge 2$) "remain +2 to +6$\sigma$ above null even after MASTER deconvolution". However, the Table III caption states that the $\ell \ge 2$ rows "use the cheaper $N_{\rm MC}=1000$ bootstrap-of-CW-labels null without mode-coupling inversion". Comparing MASTER-decoupled data to a pseudo-$C_\ell$ null is mathematically invalid; if
