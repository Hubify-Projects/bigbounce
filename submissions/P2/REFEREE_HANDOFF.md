# Referee Handoff — P2 (SPHEREx f_NL Sensitivity Recast)

`research/focused_paper_source_integration/02_full_draft.tex` · slug `paper-2` · **current version: v1.7.85 (2026-07-01)**

## 2026-07-02 compute attempt (new since 2026-07-01 handoff)

**Cubic in-in bispectrum transmission (assumption d) — ATTEMPTED, honest negative result**
(commits `11821d1b`, `9757d4a9`; scaffold at `research/cubic_bounce_transmission/`)

A full Path-Z tree-level ⟨ζζζ⟩ computation was launched: complete Maldacena cubic vertex on
an explicit nonsingular LQC bounce background (H² = (ρ/3)(1−ρ/ρ_c), dust), WKB Bunch-Davies
in-state in deep contraction, numerically-solved Mukhanov–Sasaki mode functions through the
bounce. Two normalization-free observables targeted: growing-mode transfer T_growing and
two-background ratio T3.

**What the computation established:**
- T_growing is scale-independent across k = 0.002–0.05 Mpc⁻¹ (plateau, <5% variation over
  15× in k) — a qualitative signature of faithful bispectrum-shape transmission (f_NL shape
  preserved through the bounce).

**What the computation did NOT establish:**
- T3 normalization is NOT amplitude-faithful: across 5 background depths (coarse → ultradeep),
  the benchmark ratio diverges (×6 to ×28) rather than converging to the contraction-phase
  analytic −35/8. The numerical machinery has an unresolved normalization pathology (reference-time
  mismatch between full-bounce and contraction-only reads on a non-freezing growing-mode
  background). Results in `pathz_results.json` are committed but not suitable as a derived
  bound on f_NL.

**Consequence for the paper:** f_NL = −35/8 **honestly stays conditional** (assumption d,
load-bearing caveat ★ in abstract + conclusion). The computation is documented as a committed
computational attempt with an honest negative: shape-preservation is qualitatively supported;
amplitude faithfulness requires a converged normalization scheme not achieved in this session.
The paper was NOT updated with the pathz results (no amplitude-faithful number to fold in;
folding non-convergent results would be fabrication). The #1 follow-up remains the full
converged cubic in-in computation.

## Convergence status (as of RS11 / 2026-07-01 floor)

P2 has reached the LLM-refereeing floor: **0 genuinely-new real findings** across RS11.
RS11 verdicts — **Grok MAJOR REVISIONS, Gemini MAJOR REVISIONS**. Both re-flag the same two
disclosed structural limitations (cubic-transmission conditionality; single-source Heinrich recast);
neither found a correctness defect. Grok's minors (prior-dependent Bayes factors, illustrative
MegaMapper, 31pp length) are all already labeled in-text.

## Recurring objections a human referee should adjudicate

1. **Single-source (Heinrich recast) vs independent forecast.**
   - Concern: every SPHEREx significance rescales one external Heinrich+2023 Fisher σ≈0.7 by
     overlap r=0.84; non-local bispectrum tails not propagated; not independent evidence.
   - Disclosed: abstract Scope banner — "sensitivity recast of a single externally published
     forecast, not an independent forecast"; `subsec:Caveats` signpost item (i) names the
     independent bounce-fiducial multi-tracer Fisher re-run as the required follow-up.
   - Judgment call: **is a clearly-labeled single-source sensitivity recast publishable as-is,
     or does PRD need the independent Fisher re-run before the 2.6–5.5σ envelope can appear
     as a headline?**

2. **Cubic-order bispectrum transmission (the "single weakest link").**
   - Concern: f_NL = −35/8 assumes faithful cubic-order transfer through the bounce. A full
     Path-Z numerical computation was attempted 2026-07-02 and established scale-independence
     of T_growing (shape preservation) but did NOT converge on amplitude (T3 normalization
     diverges across background depths). f_NL = −35/8 remains conditional.
   - Disclosed: abstract load-bearing caveat (★); Conclusion opening; `sec:assumptions` (d)
     names this the #1 follow-up with the honest negative computation result now documented.
   - Judgment call: **does a forecast conditioned on an unverified cubic transfer — with a
     documented computational attempt showing shape-preservation but not amplitude convergence —
     belong in PRD now, framed as conditional, or does a converged cubic in-in gate submission?**

3. **Additive-quadrature systematic budget.**
   - Concern: systematics combined heuristically in quadrature, not via a joint multi-tracer
     nuisance Fisher.
   - Disclosed: `sec:systematics` up-front heuristic banner; the joint SDB Fisher cross-check
     shows the degeneracy loosens, bounding the heuristic's direction.
   - Judgment call: **heuristic budget with a cross-check — acceptable for a recast, or must
     be replaced by a full joint covariance?**

## What is NOT in question

No genuinely-new correctness defect remains. Arithmetic (r=0.84 propagation through the BF grid,
the 2.6σ floor, Table IV) has been re-verified across rounds; prior "mismatches" were PDF-font
extraction artifacts, not errors. The 2026-07-02 Path-Z computation supports (but does not prove)
shape-faithful transmission without introducing any fabricated number.

## Recommended venue / next step

Submit to **PRD** as an explicitly-scoped sensitivity recast, with the single-source and
cubic-transmission caveats flagged to the editor. The cubic in-in follow-up (amplitude-faithful
T3 normalization) is now a documented open problem with a committed computation scaffold — worth
completing pre-submission if the target editor treats the conditional f_NL as disqualifying;
otherwise a named follow-up with the shape-preservation result cited.
