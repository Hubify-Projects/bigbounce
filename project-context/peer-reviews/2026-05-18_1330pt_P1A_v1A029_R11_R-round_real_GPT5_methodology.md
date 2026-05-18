# P1A_v1A029_R11 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 159.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28539, completion=8773, reasoning=7768, total=37312

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR

**Section:** Secs. `\ref{sec:dilution}`, `\ref{sec:structural_tension}`, App. `\ref{app:dimensions}`  
**Issue:** The App. B “ansatz dependence is only ~2%” statement only varies the bounce-scale normalization, while holding the unproved dilution law \(\mathcal D_{\rm inf}\propto e^{-3N_{\rm tot}}\) fixed. If the torsion-sourced energy scales as the usual integrated-out EC contact term \(\rho_T\propto n_\psi^2\propto a^{-6}\), the same hierarchy gives \(N_{\rm tot}\sim 46\), not \(92\), eliminating the claimed \(N_{\rm tot}>60\) \(\fnl\)-erasure tension.  
**Fix:** State explicitly that \(N_{\rm tot}\approx92\) and the DE-vs-\(\fnl\) tension are conditional on a **linear-contorsion** dilution ansatz; propagate an exponent \(p\) in \(e^{-pN}\) or remove the “\(\pm2\)” systematic claim.

## PAPER-GPT-M2 — MAJOR

**Section:** Sec. `\ref{sec:r2_oneloop}`  
**Issue:** The Route-2 “dimensionless” suppression ratio is still not a controlled dimensional reduction: the text gives two orderings, \(10^{-58}\)–\(10^{-60}\) and \(10^{-33}\), differing by \(\sim 27\) orders of magnitude. That is not a cross-check; it signals an unresolved mapping from the Holst/axial-current loop term to a photon Chern-Simons rotation angle.  
**Fix:** Derive a single unit-invariant expression for the induced photon birefringence after marginalizing/identifying the photon coupling, or downgrade Route 2 to a qualitative Planck-suppression argument.

## PAPER-GPT-M3 — MAJOR

**Section:** Barrier 12, Sec. `\ref{sec:barriers}`  
**Issue:** \(\Omega_{\rm GW}^{\rm ECH}|_{\rm bounce}\lesssim(\rho_{\rm crit}/\rho_{\rm Pl})^2\) is not a valid energy-density-fraction bound as written. If \(\Omega_{\rm GW}\equiv\rho_{\rm GW}/\rho_{\rm tot}\), the trivial ceiling is \(1\), not \((\rho_{\rm crit}/\rho_{\rm Pl})^2\); if normalized to \(\rho_{\rm Pl}\), it is not \(\Omega\).  
**Fix:** Define the normalization and derive the square from an explicit GW production model, or remove the numerical \(0.07\)–\(0.17\) ceiling.

## PAPER-GPT-m1 — minor

**Section:** Sec. `\ref{sec:structural_tension}`  
**Issue:** The sentence “absolute scaling \(k e^{N_{\rm tot}}\sim e^{30}\times k_{\rm SPHEREx}\)” is arithmetically wrong for \(N_{\rm tot}\sim92\). \(e^{30}\) is the relative \(N_{\rm tot}-N_{\rm exit}\) scaling, not the absolute \(e^{N_{\rm tot}}\) scaling.  
**Fix:** Replace with either \(k_{\rm phys,bounce}\sim e^{92}k_{\rm phys,end}\) for absolute scaling or \(e^{32}\) for the bounce-to-CMB-exit differential.

## PAPER-GPT-m2 — minor

**Section:** Reheating thermal-reset paragraph in Sec. `\ref{sec:dilution}`  
**Issue:** The thermal-reset argument compares torsion to \(n_\psi(T_{\rm reh})\), but EC torsion tracks the axial spin density \(J^5\), not the scalar number density. An unpolarized thermal bath has \(\langle J^5\rangle\simeq0\), so the stated “larger thermal torsion” comparison is not the right ensemble quantity.  
**Fix:** Recast the reset as loss of coherent axial-spin memory, using \(\langle J^5\rangle\) and/or \(\langle J^5J^5\rangle\), not \(n_\psi\) alone.

## PAPER-GPT-n1 — nit

**Section:** Barrier 12  
**Issue:** Reference `Sec.~\ref{sec:lqc}` is undefined; the LQC density window is in `Sec.~\ref{sec:bounce}`.  
**Fix:** Change the reference label to `\ref{sec:bounce}`.
