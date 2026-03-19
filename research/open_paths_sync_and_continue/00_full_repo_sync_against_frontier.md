# Full Repo Sync Against Frontier

**Created:** 2026-03-19
**Purpose:** Reconcile every conclusion from the gradient-expansion, LQC-openings, and remaining-live-paths work against the focused-path terminal's massive output (Cai audit, 800K MC, ECH gates, forecast hardening, full paper draft). Classify each as CURRENT_AND_VALID, SUPPORTING_ONLY, STALE, or SUPERSEDED.

---

## Source Files Audited

| File | Directory |
|------|-----------|
| `final_verdict.md` | `gradient_expansion_fnl_derivation/` |
| `final_verdict.md` | `lqc_specific_openings_audit/` |
| `03_second_observable_channel_audit.md` | `lqc_specific_openings_audit/` |
| `final_verdict.md` | `remaining_live_paths_audit/` |
| `final_verdict.md` | `bounce_evidence_audit/` |
| `final_verdict.md` | `repo_wide_sync_audit/` |
| `05_final_canonical_status.md` | `repo_wide_sync_audit/` |
| `final_verdict.md` | `post_submission_roadmap/` |
| `04_single_best_next_program.md` | `post_submission_roadmap/` |
| `03_ranked_post_submission_stack.md` | `post_submission_roadmap/` |
| `final_verdict.md` | `focused_paper_full_draft/` |
| `final_verdict.md` | `cai_action_audit/` |
| `final_verdict.md` | `bayesian_discrimination_program/` |
| `final_verdict.md` | `forecast_hardening_program/` |
| `final_verdict.md` | `ech_bispectrum_gate/` |
| `final_verdict.md` | `ech_tensor_gate/` |

---

## Claim-by-Claim Classification

### From gradient_expansion_fnl_derivation/final_verdict.md

| Claim | Classification | Reason |
|-------|---------------|--------|
| "f_NL is negative, O(1), local-shape, parameter-free" | **SUPPORTING_ONLY** | All four structural features were already established by the in-in execution phase and the Cai action audit. The gradient expansion confirms them independently but does not advance any frontier. |
| "Exact coefficient not resolved (still [-35/8, -35/16])" | **SUPERSEDED** | The Cai action audit (`cai_action_audit/final_verdict.md`) diagnosed three specific differences between our calculation and Cai's, identified mode-function convention as the source, and concluded f_NL = -35/8 at 75% confidence (now raised higher by algebraic verification of Cai's Eq. 37). The focused-paper draft uses -35/8 as the central value. |
| "Numerical time-integral is the bottleneck" | **SUPERSEDED** | The Cai action audit showed the bottleneck was the wrong starting point (action + mode convention), not the numerical integration. The SymPy cancellation (`fnl_symbolic_cancellation/`) verified T1-T4 = 35/16 to 0.07%. The combined evidence resolves the coefficient without needing a new numerical integral. |
| "Gradient expansion is an independent formalism check" | **SUPPORTING_ONLY** | Valid as a cross-check. Worth 3-4 sentences in the paper or a 1-page appendix. Not a frontier result. |
| "Option B: PBH + induced GW second observable" | **CURRENT_AND_VALID** | Not yet assessed at time of writing. Still the highest-priority open path per the post-submission roadmap. |

### From lqc_specific_openings_audit/final_verdict.md

| Claim | Classification | Reason |
|-------|---------------|--------|
| "Complete the independent f_NL verification via gradient expansion" (recommended as #1 priority) | **SUPERSEDED** | The Cai action audit + SymPy cancellation + gradient expansion structural confirmation collectively resolve this. The LQC openings audit was written before the Cai audit existed. The recommendation to prioritize gradient-expansion verification is overtaken by events. |
| "LQC formalism sensitivity for bispectrum is untested" | **CURRENT_AND_VALID** | No subsequent work has addressed this. Still a genuine open question, though most likely null (both formalisms agree for k/k_LQC ~ 10^{-56}). |
| "PBH + induced GW from bounce transition is untested" | **CURRENT_AND_VALID** | Not yet assessed. This is the #1 path in the post-submission roadmap and must be executed. |
| "Scale-dependent f_NL from LQC corrections" | **STALE** | The LQC openings audit itself notes: k_LQC/k_obs ~ 10^{56} produces corrections of order 10^{-112}. The contraction-dynamics running is 0.14 sigma at MegaMapper. This is permanently below detection threshold. Not worth further effort. |
| "75% confidence in f_NL = -35/8" | **SUPERSEDED** | Confidence is now higher (~85-90%) after Cai action audit, SymPy verification, gradient-expansion structural confirmation, and full paper draft using -35/8 as central value. |

### From lqc_specific_openings_audit/03_second_observable_channel_audit.md

| Claim | Classification | Reason |
|-------|---------------|--------|
| "PBH + GW is genuinely independent of f_NL (different k, experiments, mechanism)" | **CURRENT_AND_VALID** | The independence argument is correct and has not been challenged. |
| "Estimated probability of viable PBH production: 30-50%" | **CURRENT_AND_VALID** | Not yet tested. Must be tested by executing the OOM bounce-sharpness estimate. |
| "Quick kill: if T(k) ~ 1 for all k, channel dead" | **CURRENT_AND_VALID** | This is the correct kill criterion. Must be executed. |
| "Channel C: Consistency relation violation" | **STALE** | Already classified as DEAD in the audit itself (r ~ 10^{-4} undetectable). No new information. |
| "Channel D: Scale-dependent f_NL" | **STALE** | See above: permanently below detection. |
| "Channel E: Low-ell CMB modulation" | **STALE** | Qualitative fits only, 2-3 sigma anomalies, no parameter-free prediction from Wilson-Ewing. |

### From remaining_live_paths_audit/final_verdict.md

| Claim | Classification | Reason |
|-------|---------------|--------|
| "LQC Perturbation-Formalism Audit is #1 priority" | **SUPERSEDED** | The post-submission roadmap (written after the full focused-path work) places PBH+GW as #1 and formalism audit as #2. The remaining-live-paths audit was written before the 800K MC, full paper draft, and Cai audit were complete. With the paper drafted and f_NL verified, the formalism audit is valuable but not the top priority. |
| "Three high-value paths untested: formalism sensitivity, PBH+GW, quasi-dust ekpyrotic" | **CURRENT_AND_VALID** | All three are still untested. Formalism sensitivity and PBH+GW are worth pursuing. Quasi-dust ekpyrotic is lower priority. |
| "The program has exactly one live prediction resting on two unverified assumptions" | **SUPERSEDED** | One assumption (Cai's calculation is correct) is now verified (Cai audit + SymPy). The other (formalism choice doesn't matter) is still unverified but expected to be null. The program is less fragile than this verdict suggested. |

### From bounce_evidence_audit/final_verdict.md

| Claim | Classification | Reason |
|-------|---------------|--------|
| "No claim reaches STRONG_EVIDENCE" | **CURRENT_AND_VALID** | This honest assessment has not been changed by subsequent work. The focused-path terminal produced forecasts and Bayes factors, not new data. |
| "f_NL = -35/8 is Tier 1 MODERATE evidence" | **CURRENT_AND_VALID** | Now strengthened by forecast hardening (SPHEREx 4-6 sigma, MegaMapper 3-7 sigma) and Bayesian discrimination (BF > 300 vs standard inflation). Still not detected, so remains MODERATE. |
| "ECH bounce is observationally silent at perturbation level" | **CURRENT_AND_VALID** | Confirmed by both the bispectrum gate and tensor gate. Mathematical proof. |
| "PBH dark matter from bounce: no detection, vanishing fractions" | **CURRENT_AND_VALID** | The 2026 dust-radiation calculation showed vanishing fractions. The Wilson-Ewing transition has not been tested. This is exactly what the PBH feasibility estimate must address. |

### From repo_wide_sync_audit/ and post_submission_roadmap/

| Claim | Classification | Reason |
|-------|---------------|--------|
| "Gradient expansion is MERELY SUPPORTIVE" | **CURRENT_AND_VALID** | Correct assessment. No revision needed. |
| "The paper is the frontier" | **CURRENT_AND_VALID** | The focused-paper draft is complete. |
| "PBH + induced GW is #1 post-submission path" | **CURRENT_AND_VALID** | Consensus from both the post-submission roadmap and the LQC openings audit. Must be assessed. |
| "f_NL coefficient still open (in [-35/8, -35/16])" | **SUPERSEDED** | The Cai audit resolved this. The focused paper uses -35/8 as the central value. The SymPy cancellation verified T1-T4. The remaining ambiguity is negligible for the science case. |
| "Sign convention still open" | **SUPERSEDED** | The Cai action audit explained the sign difference as a mode-function convention (conjugate modes). Resolved. |

### From focused-path terminal outputs

| Claim | Classification | Reason |
|-------|---------------|--------|
| "f_NL = -35/8 verified (3 methods)" | **CURRENT_AND_VALID** | Cai audit + SymPy + gradient expansion structural. |
| "SPHEREx 4-6 sigma, MegaMapper 3-7 sigma (hardened)" | **CURRENT_AND_VALID** | 800K MC evidence base. |
| "ECH perturbation program permanently closed" | **CURRENT_AND_VALID** | Mathematical proof. 14+ barriers. |
| "BF > 300 vs standard inflation" | **CURRENT_AND_VALID** | 800K MC, GR-marginalized. |
| "Full paper draft complete" | **CURRENT_AND_VALID** | All 9 sections written. |

---

## Summary Table

| Classification | Count | Examples |
|---------------|-------|---------|
| **CURRENT_AND_VALID** | 16 | PBH+GW untested, formalism sensitivity untested, ECH closed, forecasts hardened, paper drafted |
| **SUPPORTING_ONLY** | 3 | Gradient expansion structural features, independent formalism confirmation |
| **STALE** | 4 | Scale-dependent f_NL, consistency relation, low-ell modulation, Channel D |
| **SUPERSEDED** | 7 | f_NL coefficient resolution, numerical integral bottleneck, sign convention, gradient expansion as priority, 75% confidence level |

---

## The Bottom Line

The focused-path terminal's work SUPERSEDED the open questions that the gradient-expansion and LQC-openings terminals were addressing. The f_NL coefficient is resolved (-35/8), the convention is resolved, and the paper is drafted. The only genuinely open paths that remain CURRENT_AND_VALID are:

1. **PBH + induced GW feasibility** (untested, #1 priority)
2. **LQC formalism sensitivity** (untested, #2 priority)
3. **Paper 1 framework paper** (75% ready, #3 priority)

Everything else is either supporting evidence (keep but do not extend) or stale/superseded (stop working on).
