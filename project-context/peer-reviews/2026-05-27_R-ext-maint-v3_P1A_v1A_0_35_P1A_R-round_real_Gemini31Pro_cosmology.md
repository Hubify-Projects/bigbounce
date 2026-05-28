# P1A R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P1A_v1A_0_35
**Wall time**: 63.2s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=29639, completion=7579, reasoning=6773, total=37218

---

I have reviewed the manuscript as an adversarial cosmology-physics reviewer. 

**Verdict:** No BLOCKER-grade findings. The core theoretical no-go theorem, the dimensional bookkeeping in Appendix B, and the perturbation-transparency derivations hold up to scrutiny. I have identified two MAJOR issues regarding the mischaracterization of observational systematics and the overstatement of model-independence, alongside minor mathematical/notational corrections.

Here are the findings:

## PAPER-GEM-M1 (MAJOR)
**Location:** Sec VII (Falsification Criteria) and Sec VI (Systematic Analysis)
**Issue:** The text describes GR-projection effects as a "~20% amplitude degradation". This fundamentally misrepresents the physics of GR projection effects (e.g., volume distortions, redshift-space distortions, lensing) in large-scale structure. They do not multiplicatively degrade the primordial amplitude; rather, they introduce an *additive* systematic bias ($f_{\rm NL}^{\rm obs} = f_{\rm NL}^{\rm prim} + f_{\rm NL}^{\rm GR}$ with $f_{\rm NL}^{\rm GR} \sim \mathcal{O}(1)$) that mimics local non-Gaussianity. 
**Fix:** Change "amplitude degradation" to "additive systematic bias ($f_{\rm NL}^{\rm GR} \sim \mathcal{O}(1)$)" and correct the description of how this systematic propagates through the Fisher forecast.

## PAPER-GEM-M2 (MAJOR)
**Location:** Sec XIII (Surviving Mechanism-Independent Tests) title and bold headers
**Issue:** The section title explicitly claims the tests are "Mechanism-Independent", but the text immediately (and correctly) concedes that $f_{\rm NL} = -35/8$ is "not a fully mechanism-independent prediction" because it relies strictly on the scalar-only $w=0$ matter-bounce class (failing for ekpyrotic, Cuscuton, or $w \neq 0$ models). The section header directly contradicts the text and overstates the UV-completion independence.
**Fix:** Rename the section to "Surviving Class-Specific Tests" or "Surviving ECH-Independent Tests" to align with the actual scope of the predictions.

## PAPER-GEM-m1 (minor)
**Location:** Sec IV.D (Route 4)
**Issue:** The text states that for the Chern-Simons 4-current $K^\mu \equiv \epsilon^{\mu\nu\rho\sigma} A_\nu F_{\rho\sigma}$, the divergence is $\partial_\mu K^\mu = \frac{1}{2} \tilde{F}_{\mu\nu} F^{\mu\nu}$. Under the standard definition of the dual tensor $\tilde{F}^{\mu\nu} = \frac{1}{2} \epsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}$, the divergence evaluates exactly to $\partial_\mu K^\mu = F_{\mu\nu} \tilde{F}^{\mu\nu}$. The $1/2$ factor is spurious.
**Fix:** Remove the $1/2$ factor to read $\partial_\mu K^\mu = F_{\mu\nu} \tilde{F}^{\mu\nu}$, or write it explicitly as $\partial_\mu K^\mu = \frac{1}{2} \epsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma}$.

## PAPER-GEM-n1 (nit)
**Location:** Appendix B, Eq. (B2) paragraph
**Issue:** The expression $10^{19{\rm\,GeV}\times 4}$ places physical units inside the exponent multiplier, which is mathematically nonsensical notation.
**Fix:** Change to $(10^{19}\,\text{GeV})^4$.
