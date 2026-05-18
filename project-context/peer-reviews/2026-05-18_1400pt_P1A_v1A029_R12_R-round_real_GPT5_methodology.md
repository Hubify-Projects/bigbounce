# P1A_v1A029_R12 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1400pt
**Wall time**: 135.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28544, completion=6907, reasoning=6214, total=35451

---

No BLOCKER-grade findings. No new regressions found in M_area-gap, Barrier 12 arithmetic, or App. B dependency statement.

## PAPER-GPT-M1 — MAJOR — Secs. 4.4, 4.5, 12

**Issue:** Route 4’s detailed calculation says the same fitted coupling can match both $\beta_{\rm obs}$ and $\rho_\Lambda$ if $m_\theta\sim H_0$, but the closure summary says “the same coupling cannot deliver both.” Sec. 12 also calls $m\sim H_0$ “without fine-tuning,” contradicting Sec. 4.4’s own $10^{-61}$ dimensionful tuning statement.  
**Fix:** State consistently: R4 can match both only by tuning $m_\theta\sim H_0$; the no-go is tuning/CC-relabeling, not amplitude impossibility. Remove “without fine-tuning” or qualify as technical naturalness only if a protection mechanism is specified.

## PAPER-GPT-M2 — MAJOR — Sec. 4.1 Route 1

**Issue:** Route 1 says adding Holst “does not relax this bound because the torsion-elimination map is independent of $\gamma$ at the classical level,” but Eq. (4fermi) and the Scope paragraph correctly include Holst-dependent coefficients $\gamma^2/(\gamma^2+1)$ and $\gamma/(\gamma^2+1)$. This is an internal convention clash.  
**Fix:** Specify the fermion-coupling convention. For minimal Holst fermions, include the $\gamma^2/(\gamma^2+1)$ factor; if using the Mercuri/Nieh–Yan nonminimal choice, say explicitly why $\gamma$ cancels.

## PAPER-GPT-M3 — MAJOR — Sec. 4.2 Route 2

**Issue:** The “complementary cross-check” giving $\sim10^{-33}$ is not dimensionless as written: it contains $H_0$ rather than $H_0/M_{\rm Pl}$ or an explicitly integrated dimensionless phase. It also differs from the primary $\sim10^{-58}$–$10^{-60}$ estimate by $\sim25$ orders of magnitude without a controlled marginalization.  
**Fix:** Delete the cross-check or redo it with explicit units and the same observable definition. Keep one dimensionally consistent suppression estimate.

## PAPER-GPT-m1 — minor — Sec. 2.3.1 Inflationary Suppression

**Issue:** The text still says $n_\psi(T_{\rm reh})\sim T_{\rm reh}^3$ in the “free-streaming limit”; this is the reheating thermal bath / thermal-equilibrium estimate, not free streaming.  
**Fix:** Replace “free-streaming limit” with “thermal-equilibrium relativistic bath” or equivalent.

## PAPER-GPT-n1 — nit — Cross-references

**Issue:** Several references appear undefined or stale: `Sec.~\ref{sec:route2}`, `Eq.~\ref{eq:route2_ratio}`, and `Sec.~\ref{sec:lqc}`.  
**Fix:** Update to existing labels (`sec:r2_oneloop`, add an equation label if needed, and likely `sec:bounce`).
