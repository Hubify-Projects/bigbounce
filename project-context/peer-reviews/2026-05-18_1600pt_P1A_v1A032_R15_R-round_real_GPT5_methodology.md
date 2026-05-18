# P1A_v1A032_R15 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1600pt
**Wall time**: 143.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28562, completion=6535, reasoning=5696, total=35097

---

No BLOCKER-grade findings; R15 is 0-BLOCKER.

## PAPER-GPT-M1 — MAJOR — Sec. 4.1 / Eq. (4fermi), Route 1

Concrete issue: Route 1 says adding the Holst term “does not relax this bound because the torsion-elimination map is independent of \(\gamma\),” but Eq. (4fermi) explicitly has \(\gamma^2/(\gamma^2+1)\), and Sec. 4 scope notes the parity-odd partner \(\gamma_{\rm BI}/(\gamma_{\rm BI}^2+1)\cdot 8\pi G\). This is an internal derivation inconsistency.

Fix: State that the Holst-fermion four-fermion coefficients are \(\gamma\)-dependent but remain Planck-suppressed; only claim \(\gamma\)-independence if invoking the specific non-minimal Nieh–Yan/Mercuri tuning and say so explicitly.

## PAPER-GPT-M2 — MAJOR — Sec. 4.2, Route 2 one-loop ratio

Concrete issue: The same one-loop birefringence ratio is allowed to be either \(\sim10^{-58}\)–\(10^{-60}\) or \(\sim10^{-33}\), depending on “ordering.” A 25–27 OOM ambiguity in a load-bearing amplitude estimate means the dimensional reduction is still not uniquely specified.

Fix: Derive \(\beta\) from one normalized effective photon Chern–Simons operator and one line-of-sight integral; delete the alternative ordering or relegate it as an invalid dimensional contraction.

## PAPER-GPT-M3 — MAJOR — Sec. 4.4 and Sec. 4.5 closure summary

Concrete issue: Route 4 explicitly shows \(\alpha/M\sim10^{-21}\,\mathrm{GeV}^{-1}\), \(\beta\simeq6\times10^{-3}\), and \(m_\theta\sim H_0\) reproduce \(\rho_\Lambda\) within \(O(1)\), but the summary says “the same coupling cannot deliver both dark-energy density and the observed \(\beta\).” That is false as written; the actual closure is tuning, not algebraic impossibility.

Fix: Replace “cannot deliver both” with “delivers both only by tuning \(m_\theta\sim H_0\), reintroducing the CC hierarchy.”

## PAPER-GPT-M4 — MAJOR — Sec. 12, “Spectator-ALP birefringence”

Concrete issue: The text says an ALP with \(f_a\sim M_{\rm Pl}, m\sim H_0\) is consistent “without fine-tuning,” contradicting Sec. 4.4, which correctly identifies \(m_\theta\sim H_0\) as a \(10^{-61}\)-scale dimensionful tuning. This is an overclaim.

Fix: Say “phenomenologically consistent but not natural; \(m\sim H_0\) is an input tuning.”

## PAPER-GPT-m1 — minor — Sec. 14.4 structural-tension scaling

Concrete issue: The scale statement \(k^{\rm phys}_{\rm bounce}\sim k^{\rm phys}_{\rm SPHEREx}e^{N_{\rm tot}-N_{\rm exit}}\) is only correct if \(k^{\rm phys}_{\rm SPHEREx}\) denotes the physical wavenumber at inflationary horizon exit, not today. If read as present-day physical \(k\), multiplying by \(e^{32}\) does not establish subhorizon status relative to \(H_{\rm inf}\).

Fix: Write the invariant statement directly: \(k_{\rm phys,bounce}/H_{\rm inf}\simeq e^{N_{\rm tot}-N_k}\), with \(N_k\simeq50\)–\(60\) depending on the SPHEREx mode.
