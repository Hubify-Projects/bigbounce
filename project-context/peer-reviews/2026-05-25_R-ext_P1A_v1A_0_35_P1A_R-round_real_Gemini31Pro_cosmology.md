# P1A R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P1A_v1A_0_35
**Wall time**: 145.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=29646, completion=15996, reasoning=15359, total=45642

---

## PAPER-GEM-B1
**Location:** Section IV.B (Route 2) and IV.D (Route 4)
**Issue:** Fatal dimensional conflation of the pseudoscalar $\theta$. In Eq 16, $\beta = (\alpha/M)\Delta\theta$ requires $\theta$ to have mass dimension +1 (since $\alpha/M$ has dim -1). However, in Sec IV.B, the text sets $\partial_\mu\theta \sim H$ (implying $\theta$ is dimensionless, dim 0), which subsequently causes the one-loop action in Eq 13 to have invalid mass dimension -1 (due to the $1/M_{Pl}$ prefactor). 
**Fix:** Consistently assign $\theta$ mass dimension +1, correct the background derivative to $\partial_\mu\theta \sim H f_a$ (or $H M_{Pl}$), and re-evaluate the dimensionless ratio in Eq 14.

## PAPER-GEM-M1
**Location:** Section XIII, Header and Item (1)
**Issue:** The section header and bolded text claim $f_{NL}=-35/8$ is a "Surviving Mechanism-Independent Test", but the inline text explicitly admits it requires a "scalar-only $w=0$" assumption and fails for ekpyrotic, Cuscuton, or quintom bounce variants. This directly overstates UV-completion independence.
**Fix:** Rename the section to "Surviving Class-Level Tests" and remove the "mechanism-independent" label from the $f_{NL}$ prediction.

## PAPER-GEM-M2
**Location:** Section I.A and Section XIV.D (Structural Tension)
**Issue:** The kinematic scaling $k_{\rm bounce}^{\rm phys} = k_{\rm SPHEREx}^{\rm phys}\,e^{N_{\rm tot}-N_{\rm exit}}$ conflates the physical wavenumber today with the physical wavenumber at horizon exit. To scale a physical wavenumber from today to the bounce, one must multiply by the full scale factor ratio $a_{\rm today}/a_{\rm bounce} = e^{N_{\rm post-inf}} e^{N_{\rm tot}}$, not the sub-horizon inflationary differential $e^{N_{\rm tot}-N_{\rm exit}}$.
**Fix:** Replace $k_{\rm SPHEREx}^{\rm phys}$ with $k_{\rm exit}^{\rm phys}$ (which equals $H_{\rm inf}$) in the scaling equation, or correctly use the comoving wavenumber $k_{\rm comoving}$ divided by $a_{\rm bounce}$.

## PAPER-GEM-M3
**Location:** Section II.C.1, line ~235 ("standard cold-relic scaling")
**Issue:** The text justifies $a^{-3}$ fermion dilution from the Planck-scale bounce by calling it "standard cold-relic scaling for a non-relativistic species". Fermions at the bounce are ultra-relativistic; $n \propto a^{-3}$ is
