# P1A_v1A028_R10 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1300pt
**Wall time**: 134.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28315, completion=6670, reasoning=5696, total=34985

---

## PAPER-GPT-B1 — BLOCKER

**Location:** Appendix B, Eq. `\ref{eq:onshell_rho}`; Secs. `\ref{sec:rotation}`, `\ref{sec:gdp}`, abstract.  
**Issue:** The load-bearing relation `\rho_\Lambda^{bounce}\sim(\alpha/M)M_{\rm Pl}^5\sim10^{-2}M_{\rm Pl}^4` remains an on-shell dimensional insertion, not a derived dimension-4 EFT operator. It is still used to motivate `\Xi`, `N_{\rm tot}\approx92`, and the dark-energy/bounce tension, so labeling it “ansatz” does not remove the dimensional defect.  
**Fix:** Either rederive a genuine local dimension-4 operator with all mass powers and coupling normalization fixed, then recompute `N_{\rm tot}`, or remove all `M_{\rm Pl}^5` / quantitative dark-energy-scaling claims.

## PAPER-GPT-B2 — BLOCKER

**Location:** Sec. `\ref{sec:dilution}` and Sec. `\ref{sec:structural_tension}`.  
**Issue:** The suppression law uses `D_inf=e^{-3N_tot}` by tracking torsion/number density, but the actual EC four-fermion energy density scales as `n_\psi^2/M_{\rm Pl}^2 \propto a^{-6}` unless a derived linear-in-torsion vacuum operator is supplied. This exponent controls the quoted `N_tot≈92`; changing it can erase the claimed `f_NL` structural tension.  
**Fix:** Derive the dilution exponent from the explicit operator sourcing `\rho_\Lambda`; otherwise remove the quantitative `N_tot≈92` and “definitively erased” claims.

## PAPER-GPT-M1 — MAJOR

**Location:** Sec. `\ref{sec:r2_oneloop}`, one-loop ratio following Eq. `\ref{eq:oneloop_parity_odd}`.  
**Issue:** Route 2 is still dimensionally unstable: the text gives two “dimensionless” orderings differing by ~25 orders of magnitude (`10^{-58}`–`10^{-60}` vs `10^{-33}`), which is not a valid derivation. Also `\partial_\mu\theta\sim H` implies dimensionless `\theta`, making the displayed `/M_{\rm Pl}` action term dimensionally inconsistent unless the field normalization is specified.  
**Fix:** Define the mass dimension and normalization of `\theta`, derive the photon/birefringence coupling once, and keep only one dimensionless ratio.

## PAPER-GPT-M2 — MAJOR

**Location:** Sec. `\ref{sec:dilution}`, “Reheating thermal-reset barrier”.  
**Issue:** The thermal-reset argument substitutes `n_\psi(T_{\rm reh})\sim T^3` for the axial spin source of torsion. Minimal EC torsion tracks the local spin/axial-current expectation, not total fermion number density; an unpolarized thermal bath has zero mean axial current.  
**Fix:** Compute `\langle J_5^\mu\rangle` or `\langle J_5^\mu J^5_\mu\rangle` in the reheating state, including polarization/chiral asymmetry, or delete the reset barrier.

## PAPER-GPT-M3 — MAJOR

**Location:** Sec. `\ref{sec:fourroute_summary}` vs Scope paragraph in Sec. `\ref{sec:fourroute}`.  
**Issue:** The paper first states R1–R4 are not an operator-level exhaustive basis and explicitly omits Jackiw–Pi gravitational Chern–Simons and the parity-odd four-fermion partner, then later says R1–R4 “exhaust” the available minimal-ECH parity-odd/dark-energy channels. That overstates the no-go theorem.  
**Fix:** Replace “exhaust” with “cover the four enumerated channels studied here” and keep all closure claims channel-level only.

## PAPER-GPT-m1 — minor

**Location:** Sec. `\ref{sec:discussion}`, “Spectator-ALP birefringence”.  
**Issue:** The text says `m\sim H_0` is “without fine-tuning,” but Sec. `\ref{sec:r4_birefringence}` correctly calls `m_\theta\sim H_0` a cosmological-constant-scale tuning.  
**Fix:** Make the language consistent: describe the ALP fit as phenomenologically viable but mass-tuned, not natural.
