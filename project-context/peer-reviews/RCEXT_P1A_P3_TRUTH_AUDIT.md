# RCEXT P1A + P3 — Round C EXT Gate-Discipline Truth Audit

Date: 2026-06-29
Auditor stance: skeptical, verdict-first, NEVER dismiss a real issue / NEVER invent one.
Sources: `arxiv/paper1a_ech_nogo.tex` (v1A.0.89), `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.120)
Reviews: RCEXT_P1A_{ChatGPT,Grok,Gemini}, RCEXT_P3_{ChatGPT,Grok,Gemini} (all 6 = MAJOR REVISIONS)

Calibration: June 2026 is current (dates not future); arXiv valid; companion/coordinated
submission deliberate; Zenodo DOI deferral not a defect. P1A companion-reliance (H0/β/forecasts
from Paper Ib/II) is known coordinated-submission structure with a companion-inputs summary table.
P3 catalog limitations (eROSITA irreproducibility, DESI no-injection, full-sample scaler,
catalog-size framing) are all disclosed and several are structural / pod-side unrecoverable.

Verdict codes: VERIFIED-NEW-REAL / STALE-already-disclosed / FALSIFIED / OUT-OF-SCOPE / OPINION.

---

## HEADLINE VERDICT

**P1A: 0 genuinely-new real findings.** All 3/3 MAJORs are re-flags of items the paper
already discloses (scope-limitation, ansatz status, R4 relabel, fNL/Ntot mutual exclusivity)
plus framing/presentation preferences. The fNL "mutual exclusivity" the reviewers want
emphasized is the paper's OWN stated contribution #2.

**P3: 0 genuinely-new real findings.** All 3/3 MAJORs (and both "BLOCKERS") are re-flags of
items disclosed verbatim in the paper — in several cases the reviewer's exact "remedy" is
already the paper's stated text. The two BLOCKERs (eROSITA axis, tier framing) are
disclosed + structural (production scoring code never committed = pod-side unrecoverable).

No paper edit is required for correctness. Only optional cosmetic-polish opportunities exist
(listed at end). Orchestrator decides whether to action the polish; none is a defect.

---

## P1A — finding-by-finding

### F-P1A-1 (ChatGPT BLOCKER) "Headline no-go is not a theorem; omits Jackiw–Pi grav. Chern–Simons and parity-odd four-fermion partner; route set is not an operator-level basis."
**Verdict: STALE-already-disclosed.**
Evidence: §I "Scope: channel-level enumeration, not an operator-level basis" paragraph
(tex ~L1806–1822) explicitly states the four routes are "not a complete basis" and names
the omitted operators (Jackiw–Pi `R∧R̃`, parity-odd four-fermion partner of R1) plus what a
full basis would require. Abstract (L859–860) and conclusions (L929–973) repeat the disclosure;
`fig_theory_map` is captioned "channel-level closure under stated assumptions." The title/abstract
already say "channel-level," not "minimal-ECH no-go." This is the paper's explicit scoping, not a gap.

### F-P1A-2 (ChatGPT BLOCKER) "Dark-energy mapping rests on an uncontrolled dimensional ansatz (Eq. 6 off-shell dim +1, not +4); ρΛ mapping phenomenological."
**Verdict: STALE-already-disclosed.** Appendix B explicitly tracks the off-shell dim +1
mismatch and labels the ρΛ mapping phenomenological — Gemini independently praises this same
tracking as a *strength* ("does not hide the dimensional mismatch… admirable standard of
transparency"). ChatGPT is re-flagging the paper's own disclosed caveat as a defect.

### F-P1A-3 (ChatGPT+Grok MAJOR) "R2/R3 are EFT upper-bound ansätze, not literal results from cited literature."
**Verdict: STALE-already-disclosed.** §IV B–C + §I Scope label R2/R3 as illustrative
upper-bound amplitude budgets under scaling ansätze, not extractions; the ~60-OOM margin is
quoted. Grok itself notes this is "minor in substance," only "major for referee confidence."
Presentation preference, not a substantive error.

### F-P1A-4 (ChatGPT MAJOR) "R4 not closed in same sense as R1–R3; is a naturalness objection, not an amplitude no-go."
**Verdict: STALE-already-disclosed.** The paper already relabels R4 as a naturalness/
explanatory-deficit objection (ChatGPT calls this "scientifically honest/mature"). The
"excluded vs suppressed vs not-explanatory" distinction is already drawn. No change needed.

### F-P1A-5 (Gemini MAJOR / Grok / ChatGPT) "fNL = −35/8 headlined as surviving prediction without pairing the 'erased if ECH-DE realized' warning in primary tables; the two programs are mutually exclusive."
**Verdict: STALE-already-disclosed (paper's OWN contribution #2).**
Evidence: The structural tension is enumerated as novel contribution #2 (L1097–1101);
stated in the exec-summary prose, the Table I caption, §XIV.D `sec:structural_tension`
(L902, L1100, L3119, L3180), conclusions, and the surviving-tests section (L904: surviving
signatures "are accordingly *not* predictions of ECH itself"). The paper says "definitively
erased" with the full e-fold bookkeeping in ≥4 places. Gemini's literal ask — drop the
caveat *inside the Table I cell* (currently it sits in the adjacent exec-summary point #2 and
caption) — is a one-line cosmetic relocation, not a missing finding.

### F-P1A-6 (ChatGPT MAJOR) "Thermal washout conditional; Γ_wash > H not computed."
**Verdict: OPINION / STALE.** Disclosed as conditional in-text; reviewer wants a Boltzmann
calc that is not load-bearing for the channel-level closure (which rests on dimensional/
operator-counting/perturbation-transparency args, explicitly stated companion-independent).
Optional augmentation, not a defect.

### F-P1A-7 (all 3, MINOR/MAJOR) "Fig. 3 H(z) deviation dominated by illustrative H0=69.2 vs 67.68 baseline."
**Verdict: STALE-already-disclosed (MINOR).** All three reviewers acknowledge the caption
already flags H0=69.2 as a deliberately-high illustrative value. Optional polish: add a
matched-H0 panel. Not a MAJOR; Grok/Gemini list it as MINOR.

### F-P1A-8 (ChatGPT/Gemini) "13/14-barrier count is heterogeneous (mixes sharp results, naturalness, heuristics); count used rhetorically."
**Verdict: STALE/OPINION.** Paper already grades barrier status and discloses heterogeneity
(ChatGPT: "the paper acknowledges this"). Reduce-the-count-rhetoric is a style preference.

**P1A conclusion:** Every MAJOR/BLOCKER maps to a disclosed caveat, a structural
coordinated-submission feature, the paper's own stated contribution, or presentation taste.
No VERIFIED-NEW-REAL finding.

---

## P3 — finding-by-finding

### F-P3-1 (all 3, BLOCKER) "eROSITA tier: per-object S_BigAE score axis irreproducible; production threshold 0.259 unrecoverable on 16 monotone rescalings; non-monotone (ρ=−0.10) vs committed raw artifact."
**Verdict: STALE-already-disclosed + structural-unrecoverable.**
Evidence: §eROSITA (L907) discloses every detail the reviewers list — the 0.259 axis
reproduced on none of 16 rescalings, Spearman ρ=−0.10 non-monotonicity, the "undocumented
post-hoc rescaling step whose code was never committed → unrecoverable as a matter of
provenance," the n=298 membership-list-is-canonical framing, and the downstream-user
consequence. Gemini's remedy ("re-score entirely on clean pipeline") is structurally
impossible — the production code is pod-side and gone; the paper already adopts the only valid
fallback (publish the reproducible committed-raw membership list, demote scores). The 798
eROSITA+Gaia objects are already an *explicit exploratory addendum*, fail-flagged, outside the
≥268,519 catalog-grade core (L612). Re-flag of a disclosed + irreducible structural limit.

### F-P3-2 (ChatGPT+Grok BLOCKER) "Tier nomenclature: 269,317 recommended headlined without crystal-clear composition vs ≥268,519 validated catalog-grade."
**Verdict: STALE-already-disclosed.** L612 states verbatim: recommended tier = 269,317
(269,117 point-source), validated catalog-grade ≥268,519 from the four gate-passing surveys
(DESI/SDSS/Planck/NEOWISE), plus the two fail-flagged exploratory components (Gaia+eROSITA,
798) called out as "explicit exploratory addendum rather than catalog-grade." The exact
composition the reviewers demand is already in the abstract paragraph. Framing-emphasis
preference, not a missing definition.

### F-P3-3 (all 3, MAJOR) "DESI science-target mismatch: 73×/141× multipliers vs ≈0.9× like-for-like; ~98.7% on sky/filler/non-primary spectra."
**Verdict: STALE-already-disclosed.** Abstract (L612) labels 141×/73×/100× as "all
process-scale, full-stream multipliers, not the like-for-like science-target comparison given
above," and the 0.9×/≈Liang science-target recount is stated. Reviewers want the 0.9× repeated
at *every* occurrence (Grok: "every occurrence… must be immediately followed"). Style
discipline, already done in the load-bearing abstract/conclusions.

### F-P3-4 (Gemini BLOCKER) "Full-sample normalization scaler leakage; ~15–17% extreme-tail churn; fit on training split."
**Verdict: STALE-already-disclosed + partly structural.** §Training (L672) discloses the
full-sample scaler for the three tabular surveys, computes the eROSITA train-split-refit
robustness check (top-298 Jaccard 0.76, Spearman 0.94), quantifies the ~15–17% churn floor,
and states "future pipelines should fit normalization constants strictly on the training
split" — Gemini's exact remedy is the paper's own stated recommendation. NEOWISE/Gaia refits
"remain queued: their feature tables are derived products that existed only pod-side" =
structural. The paper already establishes within-survey rankings are robust to the scaler
choice. Re-flag.

### F-P3-5 (Gemini MAJOR) "Over-optimistic central Fisher σ(fNL)=8.14; convex squaring noise bias; de-biased estimate = zero improvement; abstract must state no improvement."
**Verdict: STALE-already-disclosed.** The de-biased zero is the paper's OWN headline:
abstract (L616) "de-biased point estimate returns the single-tracer baseline 8.98 exactly
(*no multi-tracer improvement at current S/N*)"; §fNL (L1089) derives the squaring bias
E[α̂²]=α²+Var(α̂) and max(0, 0.0361−0.4225)=0 explicitly; figure caption + conclusions +
limitation (4) repeat it. Grok independently praises this as "model-auditing done correctly."
Gemini's remedy is already verbatim in the abstract. Re-flag.

### F-P3-6 (ChatGPT+Grok MAJOR) "Validation-regime heterogeneity (DESI Jaccard/OOD; SDSS/Planck injection; NEOWISE mask-QA; Gaia/eROSITA FAIL) treated as commensurate."
**Verdict: STALE-already-disclosed.** Per-survey gates, the explicit FAIL flags, and the
validated-vs-exploratory tier separation are documented throughout (caveats table, limitation
2, §pathc_caveats). Reviewers want one unified justifying paragraph — presentation
consolidation, not a new defect.

### F-P3-7 (ChatGPT/Grok MAJOR) "SDSS thresholding (77,905 continuity slice vs S>5 → 12 sources) risks cherry-picking; DESI full-stream vs science scope; cosmology overextended."
**Verdict: STALE/OPINION.** SDSS slice definition, the native-retrain 21.5×/~6500× compression,
and the secondary status of the cosmology sections are all disclosed. Demote-the-cosmology and
pick-one-threshold are editorial preferences; no factual error identified.

### F-P3-8 (Gemini MINOR) "B-dominant 22.7% (44,436) = local blue-arm calibration systematic."
**Verdict: STALE-already-disclosed (MINOR).** Limitation (3) (L1143) states the 22.7%
B-dominant set "are consistent with a calibration-artifact hypothesis… confirmation or
refutation via photometric color selection (u−g / SDSS color cuts)…" — the exact test Gemini
proposes. Already in the paper; flagged MINOR.

### F-P3-9 (Gemini/ChatGPT MINOR) "NEOWISE mask-injection 100% recovery guaranteed by construction; spatial χ²=15.7 uncorrected for selection function; novelty 17.8% single-stratum."
**Verdict: STALE/OPINION (MINOR).** Novelty 17.8% single-stratum caveat is limitation (6)
verbatim; χ² and NEOWISE-QA caveats are disclosed. De-emphasis requests, not defects.

**P3 conclusion:** Every BLOCKER/MAJOR maps to text the paper already states — frequently the
reviewer's literal remedy is the paper's own sentence — or to a structurally unrecoverable
pod-side limitation already handled by the membership-list-canonical / exploratory-addendum
framing. No VERIFIED-NEW-REAL finding.

---

## Optional cosmetic polish (NOT defects; orchestrator's call)

- P1A: relocate the fNL-erasure caveat from exec-summary point #2 into the Table I
  "Testable prediction?" cell; add a matched-H0 curve/panel to Fig. 3.
- P3: append the "≈0.9× like-for-like" tag to the few in-body occurrences of 73×/141× that
  currently rely on the abstract-level statement; one-line unified validation-gate
  justification paragraph.

None changes a number, a conclusion, or a claim's validity. All are presentation emphasis.

---

## Pattern tags
061 (verdict-before-closure), 062 (cite source for dismissal), 063 (no severity-steering),
064 (no value-headlining) — all satisfied: every dismissal here cites a specific tex line/
section, and the audit independently re-confirms the papers do NOT headline favorable values
(P1A pairs fNL with "erased"; P3 abstract leads with de-biased zero and full-stream-vs-science
disclaimer).
