# paper3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P3_v3_1_56
**Wall time**: 112.6s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=68617, completion=14062, reasoning=13010, total=82679

---

## PAPER-GEM-B1
**Classification**: BLOCKER
**Section**: Abstract, 5, & 6.4(i)
**Concrete Issue**: The claim that $\alpha=0$ is a stationary point where the derivative of $1/\sigfnl^2$ vanishes is mathematically false. The total multi-tracer Fisher information includes the single-tracer auto-spectrum of the anomaly sample, which scales as $b_{QSO}^2 \propto (1+\alpha)^2$. This introduces a linear term in $\alpha$ ($F_{tot} \propto 2 + 2\alpha + 2\alpha^2$), breaking the assumed $\alpha \to -\alpha$ symmetry. The original linear propagation $\sigfnl(\alpha) \approx 8.98 - 3.66\alpha$ is physically valid; the "correction" to a purely quadratic $F_0 + c\alpha^2$ form is mathematically wrong and artificially degrades the forecast.
**Fix**: Restore the linear Fisher propagation as the canonical envelope and remove the false claim that Fisher information is purely quadratic in $\alpha$.

## PAPER-GEM-B2
**Classification**: BLOCKER
**Section**: 5.1 & Appendix D'
**Concrete Issue**: The paper claims the "simplest scalar-only" $w=0$ matter bounce predicts $\gamma=3.0$ in the PTA band. This is theoretically invalid. In a scalar-only $w=0$ matter bounce, the linear tensor perturbations are unsuppressed and scale-invariant ($r \sim \mathcal{O}(1)$), yielding $\gamma=5$ ($\Omega_{GW} \propto f^0$) which violates CMB bounds and completely swamps the $\gamma=3.0$ ($\Omega_{GW} \propto f^2$) scalar-induced gravitational wave signal. 
**Fix**: Acknowledge that the $\gamma=3.0$ SIGW prediction requires a multi-field or modified sound-speed mechanism to suppress primary tensors, explicitly breaking the "simplest scalar-only" assumption.

## PAPER-GEM-M1
**Classification**: MAJOR
**Section**: 5 & 6.4(e)
**Concrete Issue**: The text claims GR projection effects "perfectly mimic" local PNG and must be deterministically subtracted. This is false in a multi-tracer context. While both scale as $1/k^2$, $f_{NL}$ couples to $(b-p)$ whereas GR effects couple to magnification bias $s$ and evolution bias $b_e$. Multi-tracer cross-correlations with distinct $s$ and $b_e$ break this degeneracy, allowing GR effects to be marginalized.
**Fix**: Change "perfectly mimic" to "are partially degenerate with" and remove the claim that they cannot be marginalized over if $s$ and $b_e$ are free parameters.

## PAPER-GEM-M2
**Classification**: MAJOR
**Section**: 5
**Concrete Issue**: The text claims magnification bias $\delta s$ is the dominant systematic flooring $\sigfnl$, while explicitly stating that $\mathcal{H}^2/k^2$ GR projection effects are omitted from the template. Without GR projection terms, $s$ only enters via weak lensing ($\sim 1/k$) and does not strongly degenerate with local $f_{NL}$ ($\sim 1/k^2$) at tree level in the 3D power spectrum.
**Fix**: Clarify that $\delta s$ only becomes the dominant $1/k^2$ systematic *when* GR projection effects are included in the Fisher matrix, or explain the exact $1/k$ lensing coupling driving the degradation.

## PAPER-GEM-M3
**Classification**: MAJOR
**Section**: 5 vs Appendix C.1
**Concrete Issue**: There is an internal contradiction in the Fisher matrix baselines. Section 5 quotes the single-tracer DESI QSO baseline as $\sigfnl = 8.98$ (with a multi-tracer baseline of 8.43), but Appendix C.1 quotes the single-tracer baseline as $16.85$ (with a dense limit of 11.71).
**Fix**: Reconcile Appendix C.1 to use the exact same 7-bin Fisher configuration and baseline numbers as Section 5.

## PAPER-GEM-m4
**Classification**: minor
**Section**: 5.1 & 6.4(d)
**Concrete Issue**: The paper proposes using the Savage-Dickey density ratio to compare two fixed points ($\gamma=3.0$ vs $\gamma=4.33$). Savage-Dickey evaluates nested models against a prior; comparing two distinct, fixed parameter values is a simple posterior density ratio (or likelihood ratio, if priors are flat).
**Fix**: Replace "Savage-Dickey" with "posterior density ratio" or "likelihood ratio" for point-to-point comparisons.
