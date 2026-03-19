# Role of the Gradient Expansion Now

**Created:** 2026-03-19
**Purpose:** Decide the proper role of the gradient expansion result within the full project.

---

## Decision: SUPPORTING_CROSS_CHECK

---

## Justification

### Why not CORE_FRONTIER_RESULT?

A core frontier result must reveal something no other analysis has. The gradient expansion reveals nothing new:
- Sign, magnitude, shape, parameter-freedom: all established by the execution phase
- Exact coefficient: not resolved (same bottleneck as the in-in approach)
- Survey detectability: already computed to much higher precision by the forecast hardening program
- Bayesian discrimination: not addressed by the GE at all

The focused-path terminal has advanced the program far beyond the GE's scope: 800,000 Monte Carlo samples for Bayesian discrimination, 5 publication-ready figures, survey realism reconciliation, GR contamination hardening, inflation mimicry analysis, and a complete paper skeleton. The GE does not touch any of this.

### Why not APPENDIX / TECHNICAL_NOTE?

The GE has real scientific content: it provides an independent mathematical route to the same structural conclusions. In a paper, this is worth mentioning as a consistency check, not merely relegated to a footnote. The fact that two formalisms (cubic action + in-in vs gradient expansion + nonlinear Einstein equations) agree on all structural features is a meaningful statement about the robustness of the prediction.

### Why not REDUNDANT_DUPLICATE?

Despite being largely duplicative of the execution phase, the GE adds the specific value of formalism independence. If an anonymous referee questions whether the in-in result is an artifact of a specific calculational approach, the GE provides a defense: "We also verified the prediction using the gradient expansion, which uses completely different mathematical machinery (nonlinear Einstein equations in position space, no Fourier-space mode functions, no cubic action) and arrives at the same structural conclusions." This has real defensive value in peer review.

### Why SUPPORTING_CROSS_CHECK is the right classification

The gradient expansion:
1. **Confirms** structural features already established by a more detailed analysis
2. **Does not advance** any open question (coefficient, convention, bounce transfer)
3. **Does not produce** any new observable prediction or forecast
4. **Adds** independent-formalism confirmation, which has paper-level value as a robustness argument
5. **Should not be extended** further, because extending it leads to the same bottleneck

This is textbook "supporting cross-check": valuable for the evidence stack but not the frontier.

---

## Should This Line Be Actively Extended?

**NO.** Actively extending the gradient expansion would mean:
- Evaluating the growing-mode-squared coupling through second-order Einstein equations
- This is the SAME mathematical step as evaluating the in-in time integral for Terms 5-6
- The same bottleneck (arbitrary-precision arithmetic for cancelling divergences) applies
- No computational advantage over the in-in approach

The symbolic cancellation analysis (`fnl_symbolic_cancellation/`) already achieved the furthest independent numerical advance: f_NL = 35/16 from Terms 1-4. Extending the GE would at best reproduce this same number.

**The GE line should be FOLDED into the evidence stack and cited as a cross-check in the paper.** No further computation along this line is warranted.

---

## Recommended Paper Treatment

In the f_NL forecast paper (research/live_forecast_packaging/), the gradient expansion should appear as:

> "We additionally verified the structural prediction using the Salopek-Bond gradient expansion (Appendix B), which independently confirms the negative sign, O(1) magnitude, local shape, and parameter-freedom of the matter-bounce bispectrum using a completely different mathematical framework (nonlinear superhorizon evolution in position space, without reference to the cubic action or Fourier-space mode functions). Both approaches converge on f_NL in [-35/8, -35/16], with the precise coefficient determined by the growing-mode coupling through second-order perturbation theory."

This is approximately 3-4 sentences in the main text or a 1-page appendix. It does not warrant a dedicated section or extended discussion.

---

## Immediate Action

1. The gradient expansion directory (`research/gradient_expansion_fnl_derivation/`) should be marked as CLOSED with status SUPPORTING_CROSS_CHECK
2. No further sessions should be allocated to extending it
3. Its key result (formalism-independent confirmation) should be incorporated into the paper skeleton at `research/live_forecast_packaging/01_manuscript_skeleton.md`
4. The focused-path terminal's work is the authoritative frontier -- all further research effort should build on that, not on the GE
