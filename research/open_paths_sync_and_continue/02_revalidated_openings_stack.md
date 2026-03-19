# Revalidated Openings Stack

**Created:** 2026-03-19
**Purpose:** Re-rank all genuinely open paths after full reconciliation of the focused-path terminal's work against the gradient-expansion, LQC-openings, and remaining-live-paths audits.

---

## Methodology

Every path that any previous audit flagged as "open" or "worth pursuing" was re-evaluated against three criteria:

1. **Still genuinely open?** Has subsequent work (Cai audit, 800K MC, ECH gates, full paper draft) resolved or superseded it?
2. **Non-duplicative?** Does it produce information that no existing work already provides?
3. **Positive expected value?** Is the probability of a positive result times the payoff greater than the session cost?

---

## #1: PBH + Induced GW Second Observable Channel

**Still genuinely open:** YES. Nobody has computed the Wilson-Ewing bounce transfer function T(k) at k ~ k_bounce. The 2026 dust-radiation calculation (Quintin & Brandenberger framework) showed vanishing PBH fractions, but the specific Wilson-Ewing LQC effective dynamics have NOT been tested.

**Novelty:** HIGH. This is a second observable family -- different k-range (10^5 - 10^15 Mpc^{-1}), different experiments (LISA/ET vs SPHEREx/MegaMapper), different generation mechanism (bounce transition dynamics vs pre-bounce contraction dynamics). If viable, it breaks the single-point-of-failure architecture.

**Quick kill available:** YES. If the Wilson-Ewing bounce is too smooth at all observable scales, T(k) ~ 1 for all k below Planck frequency, and the channel is dead in one session. The key calculation is an OOM estimate of the bounce sharpness and the corresponding enhancement scale.

**NOT duplicative:** Correct. No work in the repository has touched this specific calculation. The chiral GW program (`project_chiral_bounce_GW/phase0_results.md`) tested the frequency reach of bounce-scale GWs and found they are at ~10^{9-10} Hz (GHz) -- permanently inaccessible. But the PBH mechanism is different: it relies on perturbation enhancement at scales near k_bounce, not on direct GW production at the bounce. The question is whether the enhancement at k_bounce maps to observable PBH masses and GW frequencies after expansion.

**Estimated probability of positive result:** 30-50% (per the LQC openings audit). But note the chiral GW frequency gate result: if the enhancement is at k ~ k_bounce ~ a_bounce * M_Pl, and this maps to f ~ 10^{13} Hz today, the same frequency-gate problem kills the PBH channel. This must be checked explicitly.

**Priority:** EXECUTE IMMEDIATELY (File 05).

---

## #2: LQC Formalism Sensitivity Audit

**Still genuinely open:** YES. No paper has compared dressed-metric vs hybrid LQC perturbation formalisms for the bispectrum. The comparison exists for the power spectrum (arXiv:2405.12296), but the bispectrum extension has not been checked.

**Novelty:** MODERATE. The most likely outcome is null -- both formalisms agree for superhorizon modes at k/k_LQC ~ 10^{-56}. But if they disagree, this is testable quantum gravity.

**Quick kill available:** YES. If arXiv:2405.12296 shows superhorizon power spectrum formalism-independence, and the bispectrum inherits this by dimensional analysis, resolved in hours.

**NOT duplicative:** Correct. No work in the repository has addressed this.

**Estimated probability of positive (non-null) result:** ~15%.

**Priority:** NEXT after PBH assessment. Even a null result strengthens the paper by formally establishing robustness.

---

## #3: Paper 1 Framework Paper Completion

**Still genuinely open:** YES, in the sense that the paper is ~75% ready but not finished.

**Novelty:** LOW for new science. This is a compilation exercise using existing material (ECH closure, ALP birefringence, MCMC verification, 14 barriers).

**Quick kill:** N/A -- this is a writing task, not a research question.

**NOT duplicative:** Correct. The material has not been published.

**Estimated effort:** 2-3 sessions for completion.

**Priority:** THIRD. Worth doing after the research questions (#1, #2) are resolved, since those results could inform the framework paper's discussion section.

---

## #4: Companion Theory Paper (ECH -> LQC Narrative)

**Still genuinely open:** YES. The systematic closure of 14 ECH perturbation routes has not been published. No comparable analysis exists in the literature.

**Novelty:** MODERATE (for the community, even though the results are known internally).

**Priority:** FOURTH. Lower than the research questions and the framework paper. Can be compiled from existing verdicts after the above are done.

---

## #5: Quasi-Dust Ekpyrotic Two-Field Model

**Still genuinely open:** CONDITIONALLY. The 2025 paper (arXiv:2509.06148) claims viability. Whether it produces a different f_NL has not been checked.

**Novelty:** LOW to MODERATE. If it produces a different f_NL, there is a potential for a multi-model discrimination analysis. If it reproduces -35/8, it adds nothing.

**Priority:** FIFTH. Only worth checking if a literature search reveals that nobody has computed f_NL for this specific model. Quick check, not a calculation program.

---

## Deprioritized (DO NOT PURSUE)

| Path | Reason |
|------|--------|
| Scale-dependent f_NL | LQC correction: 10^{-112}. Contraction running: 0.14 sigma. Permanently undetectable. |
| Consistency relation (r, n_T) | r ~ 10^{-4}, below all detector thresholds. |
| Low-ell CMB modulation | Qualitative fits, no parameter-free prediction from Wilson-Ewing. |
| ECH perturbation anything | Mathematical proof of transparency. 14+ barriers. PERMANENTLY CLOSED. |
| Gradient expansion extensions | SUPPORTING_CROSS_CHECK only. Coefficient resolved by Cai audit. |
| Numerical in-in integral | Superseded by Cai audit + SymPy. |
| More MCMC | Reconfirms Delta-N_eff = 0. No new theory to test. |
| Hybrid DE splice | 7 forms rejected exhaustively. |
| Teleparallel / f(T) / f(Q) | Sprawl without discriminators. |
| Chiral GW | Frequency gate failed. 5 independent closures. |
| Galaxy spin dipole | 9-12 OOM coupling gap. |

---

## Decision Protocol

Strict stack ordering. Do not skip ahead.

1. Execute PBH+GW feasibility assessment (#1). This is File 05 of this series.
2. Based on #1 result:
   - If PBH viable: proceed to detailed PBH/GW calculation. This becomes a major new research track.
   - If PBH dead: proceed to LQC formalism audit (#2).
3. After #2:
   - If formalism-sensitive: major finding, write it up.
   - If formalism-insensitive: document as robustness confirmation.
4. Then proceed to framework paper (#3) and companion theory paper (#4) as compilation exercises.

**Do not work on lower-ranked paths while higher-ranked paths remain open.**
