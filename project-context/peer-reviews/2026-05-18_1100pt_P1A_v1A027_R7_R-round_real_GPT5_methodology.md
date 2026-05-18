# P1A_v1A027_R7 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1100pt
**Wall time**: 191.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=27795, completion=9942, reasoning=8756, total=37737

---

# Review

No BLOCKER-grade finding.

## PAPER-GPT-M1 — MAJOR

**Section:** Sec. 4.1 Route 1, Eq. `\ref{eq:NJL_torsion}`; Sec. 2.1 Eq. `\ref{eq:4fermi}`  
**Issue:** The bound `\rho_{\rm NJL}\sim \kappa n_\psi^2/m^2` is dimensionally wrong: `\kappa n^2/m^2` has mass dimension `+2`, not energy-density dimension `+4`. Also the claim that the Holst torsion-elimination map is classically independent of `\gamma` contradicts the paper’s own Eq. `\ref{eq:4fermi}` with `\gamma^2/(\gamma^2+1)`.  
**Fix:** Remove the spurious `/m^2` and recompute as `\rho_{\rm NJL}\sim \kappa n_\psi^2` up to spin/polarization factors. State explicitly whether the minimal Holst-fermion coupling or Mercuri non-minimal cancellation is being used, and keep the corresponding `\gamma` factor consistently.

## PAPER-GPT-M2 — MAJOR

**Section:** Sec. 4.2 Route 2, Eq. `\ref{eq:oneloop_parity_odd}` and following ratio  
**Issue:** Route 2 is still not dimensionally closed. The dimension of `\theta` is undefined, `\partial_\mu\theta\sim H` is inserted without a normalized kinetic term, and no derived map to a photon Chern-Simons/birefringence coefficient is given. The text also admits two “dimensionless orderings” giving `10^{-58}`–`10^{-60}` versus `10^{-33}`, a 25+ order ambiguity.  
**Fix:** Derive the canonically normalized one-loop operator through to the photon-rotation angle with all mass dimensions explicit; keep one ratio only. Until then, mark Route 2 as deferred/qualitative, not quantitatively closed.

## PAPER-GPT-M3 — MAJOR

**Section:** Sec. 4.4 Route 4, Eq. `\ref{eq:beta_bound}`  
**Issue:** The written Chern-Simons coupling `(\alpha/M)\partial_\mu\theta\,\tilde F^{\mu\nu}F_{\mu\nu}` is not a scalar: the index `\mu` is left uncontracted. The subsequent `\beta=(\alpha/M)\Delta\theta` formula is the standard ALP result, but it does not follow from the operator as written.  
**Fix:** Replace with `\mathcal L \supset -(g_{\theta\gamma}/4)\theta F_{\mu\nu}\tilde F^{\mu\nu}` or the integrated-by-parts form `\partial_\mu\theta\,K^\mu`, then rederive `\beta` and the `\rho_\theta` relation. State that R4 closure is conditional on fixing `\alpha/M` by the one-loop/ECH matching; if `\alpha/M` is free, the amplitude no-go does not hold.

## PAPER-GPT-M4 — MAJOR

**Section:** Abstract; Sec. 13 “Structural incompatibility”; Sec. 14.3 `\ref{sec:structural_tension}`  
**Issue:** The scale mapping `k_{\rm bounce}^{\rm phys}\sim k_{\rm SPHEREx}^{\rm phys} e^{N_{\rm tot}-N_{\rm exit}}` uses today’s physical SPHEREx wavenumber with only the inflationary differential `e^{32}`. That omits the post-inflation expansion/reheating factor; by itself it does not establish that SPHEREx modes are “deep inside” the inflationary subhorizon regime.  
**Fix:** Redo the mapping with an explicit scale-factor normalization: compute `k/(a_b H_b)` or use `k/a_b=e^{N_{b\to exit}}H_{\rm exit}` for modes that actually exit during inflation. Downgrade “definitively erased” unless the corrected ratio is shown.

## PAPER-GPT-M5 — MAJOR

**Section:** Sec. 9, Barrier 12  
**Issue:** The arithmetic and comparison are wrong. `(0.27–0.41)^2 = 0.07–0.17`, not `\sim10^{-2}`. More importantly, `\Omega_{\rm GW}\sim10^{-2}` is not “far below” the NANOGrav signal scale (`\sim10^{-9}`); a total bounce energy fraction cannot be compared directly to the present-day PTA spectral density.  
**Fix:** Recompute the numerical ceiling and propagate it through redshift, transfer functions, and the PTA frequency band before comparing with NANOGrav. Otherwise remove the NANOGrav claim from Barrier 12.

## PAPER-GPT-m1 — minor

**Section:** Sec. 2.1, Eq. `\ref{eq:Seff}` and surrounding text  
**Issue:** The area-gap mass scale is stated as `M_{\rm area-gap}\sim\sqrt{\gamma}M_{\rm Pl}`. From `\Delta\propto\gamma \ell_P^2`, the inverse length/energy scale is `M_\Delta\sim M_{\rm Pl}/\sqrt{\gamma}` up to numerical constants.  
**Fix:** Correct the scaling or declare `M` to be a phenomenological mass unrelated to the inverse LQG area-gap scale.
