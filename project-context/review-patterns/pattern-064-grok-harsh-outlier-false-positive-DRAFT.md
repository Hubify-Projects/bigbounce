---
pattern_id: 64
status: draft
first_seen: R52 (2026-06-26)
papers_observed: [P1A, P1B, P4, P5]
finding_count: 4
proposed_by: r-round-pattern-mine 2026-06-26
parent_patterns: [10]
---

# pattern-064: grok-harsh-outlier-false-positive

**Description**: Grok (grok-4.x) consistently issues the harshest verdict (REJECT or
MAJOR REVISIONS) across the paper portfolio and consistently truth-audits to
false-positive at the reason level. Its ESSENTIAL/MAJOR reasons are FALSIFIED against
source in every R52 instance. Grok's outlier verdict is driven by structural biases:
applying a strict standalone-reader standard to deliberately companion-coupled suite
papers; inverting primary and secondary samples; flagging already-disclosed scope
qualifiers as missing; and demanding new computation for labeled-allowance items.

**Root cause**:
1. **Standalone-reader bias**: Grok applies a strict "this paper must stand alone"
   standard to papers that explicitly disclose companion dependencies. The disclosures
   are in the paper; Grok counts the dependencies as defects anyway.
2. **Primary/secondary inversion**: Grok misidentifies which sample is primary (P5:
   treated n=428 T-Web void as the headline when the paper's headline is n=56,981
   DESIVAST).
3. **Disclosure-as-defect misread**: Grok flags already-disclosed scope limitations
   ("theorem scalar-only," "Route 4 is philosophical") as concealed defects when they
   are in the title, abstract, and body.
4. **Dispatch tag inflation**: Grok's dispatch tag may be REJECT while Grok's own
   in-text reasons, individually truth-audited, do not support rejection (see also
   pattern-061).

**Evidence (R52)**:
- P1A: Grok REJECT → FALSE POSITIVE. E1-M4 all FALSIFIED or OUT-OF-SCOPE. E3 "title overclaims" FALSIFIED — title already reads "Channel-Level." M3 "theorem scalar-only" FALSIFIED — in the title.
- P1B: Grok MAJOR outlier → verdict driven by FALSIFIED ESSENTIALs (ΔNeff one-sided UL conflated with two-sided mean) and editorial opinion.
- P4: Grok MAJOR false positive → E1 "catalog size lacks qualifier" FALSIFIED; E2 "comparability warning absent" FALSIFIED (present verbatim at tex 348).
- P5: Grok REJECT false positive → E1-E3 all FALSIFIED (primary/secondary inversion + qualifier already present × 5 captions). Every MAJOR reason FALSIFIED or editorial opinion.

**Why it matters**: A Grok REJECT or MAJOR verdict arriving alongside 2-3 other vendors'
ACCEPT/MINOR draws disproportionate audit attention and can pressure the auditor to
treat a false positive as a real signal. It may cause unnecessary recomputation requests
or scope-expansion to papers that are already correct.

**Detection rule / handling protocol**:
1. When Grok issues REJECT or MAJOR: **truth-audit every Grok reason individually**
   before accepting the verdict.
2. Apply the primary/secondary inversion check: does Grok correctly identify which
   sample/test/claim is PRIMARY vs. SECONDARY in the paper?
3. Apply the disclosure check: for every "missing" item Grok claims, grep the source
   for the exact claim before accepting.
4. Compare Grok's verdict to 2+ other full-PDF vendors: if Claude + Gemini + OpenAI
   all say ACCEPT/MINOR while Grok says REJECT/MAJOR, weight Grok skeptically.
5. Do NOT auto-FALSIFY Grok wholesale — Grok does surface real findings (e.g., P1B
   E2 "pipeline bias comparability" was VERIFIED). Audit per-reason, not per-verdict.

**Prevention**:
- `/peer-review-truth-audit` should flag Grok REJECT/MAJOR as "high-false-positive-
  probability vendor" and mandate reason-by-reason individual audit (vs. treating
  convergent REJECT from 3 vendors the same way as a single-vendor Grok REJECT).
- Truth-audit preamble should note Grok's track record as the context for its severity.

**Severity**: high — false-positive REJECTs are the most expensive triage outcome.

**Relationship to pattern-010**: pattern-010 (Grok convergent silence) is a positive
calibration signal — when Grok stops flagging, that's a convergence indicator. This
pattern (064) is the complementary negative calibration signal — when Grok issues
REJECT/MAJOR, audit every reason skeptically before accepting the verdict.

**Promotion candidate note**: If this pattern fires in 6+ consecutive rounds with ≥80%
false-positive rate, promote to an auto-partial-FALSIFY rule in `/peer-review-truth-audit`
for Grok ESSENTIAL/MAJOR reasons (requiring primary-source corroboration).
