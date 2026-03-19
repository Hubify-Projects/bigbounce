# Final Verdict: Packaging Pass

## 1. Exact Recommended Deliverable

**A focused forecast paper:** "Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper"

~15 pages, targeted at JCAP or PRD. Centered entirely on the observational test of f_NL = -35/8.

## 2. Strongest Defensible Central Claim

"The generic matter-bounce scenario predicts f_NL^local = -35/8 = -4.375, a parameter-free, mechanism-independent signature that is ~300× larger than standard inflationary predictions and opposite in sign. The SPHEREx multi-tracer galaxy bispectrum is forecast to test this prediction at ~6σ significance, with MegaMapper providing a more powerful but systematics-sensitive follow-up at 3-7σ. A robust detection of f_NL ≈ -4 would provide strong evidence favoring a contracting/bounce origin over standard single-field inflation."

## 3. Wording to AVOID

- ❌ "proves a pre-Big-Bang contracting phase"
- ❌ "rules out inflation"
- ❌ "we derived f_NL = -35/8" (say "verified" or "confirmed")
- ❌ "definitive test" (say "strong test" or "meaningful test")
- ❌ "MegaMapper will detect at 8.75σ" (say "could reach 8.75σ under ideal conditions; realistic range is 3-7σ")
- ❌ Any claim of uniqueness without caveat about exotic multi-field inflation

## 4. Must-Have Figures/Tables

**Figures (5, all laptop-generatable from existing code):**
1. Shape function / squeezed-limit convergence
2. Survey significance comparison (SPHEREx vs MegaMapper, scenario ranges)
3. Fisher sensitivity to k_min (the "cliff" plot)
4. Decision threshold diagram (confirm/weaken/kill regions)
5. Inflation comparison (f_NL landscape)

**Tables (4):**
1. Prediction package (f_NL, n_s, r, shape ratios with classifications)
2. Survey hierarchy (σ, significance, key assumptions)
3. Systematics threat matrix (threat, severity, mitigation)
4. Decision thresholds (measured f_NL ranges → verdicts)

## 5. Is Anything Material Still Missing?

**NO.** All content exists in the repository:
- Theory: verified shape function, prediction package, ECH closure statement
- Forecasts: SPHEREx (from literature), MegaMapper (from Fisher scan + literature)
- Systematics: GR effects, b_φ, k_min (from literature audit)
- Thresholds: confirm/weaken/kill criteria
- Figures: code exists, plots need generation (matplotlib, ~1 hour)

## 6. Exact Next Step

**Generate the 5 figures from existing code, then begin full draft writing.**

The figure generation is the last mechanical step. Once the figures exist, all material for the full manuscript is assembled. The draft itself should take 2-3 focused sessions.

Sequence:
1. Generate Figure 1 (shape function) from the AT evaluation code
2. Generate Figure 3 (Fisher k_min sensitivity) from the Fisher robustness code
3. Generate Figures 2, 4, 5 (bar charts / schematics) from the numbers in the audit files
4. Begin full draft: Introduction → Theory → Observational Framework → Forecasts → Systematics → Discussion
