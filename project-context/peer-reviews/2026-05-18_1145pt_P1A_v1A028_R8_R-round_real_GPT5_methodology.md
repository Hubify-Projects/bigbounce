# P1A_v1A028_R8 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1145pt
**Wall time**: 111.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28352, completion=5886, reasoning=5178, total=34238

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR — Sec. 9 / Barrier 12

**Issue:** Barrier 12 no longer functions as a “barrier.” After removing the invalid PTA comparison, the statement $\Omega_{\rm GW}^{\rm ECH}|_{\rm bounce}\lesssim0.07$–$0.17$ is only a loose bounce-era energy-fraction ceiling and does not exclude any observable GW channel without a spectrum and transfer function.

**Fix:** Reclassify B12 as a non-closing diagnostic or remove it from the independent closure count unless a propagated present-day spectral constraint is supplied.

## PAPER-GPT-M2 — MAJOR — Sec. 4, immediately after “Scope”

**Issue:** The internal adversarial-review/meta-commentary paragraph is still present despite the R7 closure claim. It includes vendor names, version-history prose, and unresolved internal audit language; it also introduces dangling refs to `sec:route2` and `eq:route2_ratio`.

**Fix:** Delete the entire paragraph. If any scientific content is needed, restate it as normal manuscript text and add valid labels.

## PAPER-GPT-M3 — MAJOR — Sec. 12 “Theoretical Implications”

**Issue:** This section is stale relative to the updated four-route closure. It says the one-loop route fails because BI dependence “does not contribute at one loop,” contradicting Sec. 4 R2 where a one-loop parity-odd term is explicitly written but amplitude-suppressed; it also reverts to “no photon coupling” language inconsistent with the R4 ALP-photon treatment.

**Fix:** Rewrite this paragraph to match the current R1–R4 conclusions: R1 parity-even/Planck suppressed, R2 loop-generated but negligible, R3 dimension-locked/running-suppressed, R4 viable as spectator ALP but not ECH dark energy.

## PAPER-GPT-m4 — minor — Sec. 9 / Barrier 12

**Issue:** `Sec.~\ref{sec:lqc}` is undefined. The relevant LQC/bounce label appears to be `sec:bounce`.

**Fix:** Replace `\ref{sec:lqc}` with `\ref{sec:bounce}` or add the missing label.

## PAPER-GPT-m5 — minor — Secs. 12–13 / ALP tuning language

**Issue:** The manuscript says an ALP with $m\sim H_0$ is “without fine-tuning” in Sec. 12, while Sec. 4 R4 correctly characterizes $m_\theta\sim H_0$ as a dimensionful CC-scale tuning. This is an internal methodological inconsistency.

**Fix:** Use one position consistently: spectator ALP birefringence is phenomenologically viable but its use as dark energy requires the usual ultralight-mass tuning.

## PAPER-GPT-n6 — nit — Sec. 10 “Proof”

**Issue:** The Holst term with the Levi-Civita connection is described as “topological” and then as vanishing identically by the Bianchi identity. In the torsionless case the Holst density vanishes identically; the Nieh–Yan/topological wording is imprecise.

**Fix:** Replace “becomes topological” with “reduces to the torsionless Holst density, which vanishes identically by the first Bianchi identity.”
