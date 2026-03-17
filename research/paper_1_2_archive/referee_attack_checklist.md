# Paper 1.2 — Referee Attack Simulation Checklist

**Date:** 2026-03-14

---

## Attack 1: "Part I is just standard ΛCDM+ΔNeff — what's new?"

**Severity:** Medium — the most predictable criticism.

**Where it's addressed:**
- Section 3.2.2 (line 319–321): "The MCMC analysis is phenomenologically equivalent to any ΛCDM+ΔNeff extension—the tension reduction is a property of the parameter space, not uniquely of spin-torsion cosmology."
- Section 9.1 (line 917–920): Honest positioning as "more than generic ΛCDM" but "less than a first-principles derivation."
- Section 9.3, paragraph 1 (line 954–963): Explicit comparison acknowledging statistical equivalence with generic ΔNeff models; advantage is fine-tuning reduction.
- Claims table (Appendix C): ΔNeff as distinctive signal is explicitly **Retired**.

**Strength of defense:** Good. The paper preempts this criticism by framing Part I as a phenomenological starting point, not the contribution. The contribution is Parts II–III. A referee who reads past Part I will see this.

**Residual risk:** A referee who stops reading after Part I will recommend rejection on this basis alone. The abstract's second and third paragraphs must hook them into Parts II–III. Currently they do.

---

## Attack 2: "The mass-coupling lock is a one-paragraph observation, not a result."

**Severity:** Medium-high — threatens the paper's central claim.

**Where it's addressed:**
- Section 6.6 (lines 640–675): Full structural explanation with general Lagrangian, canonical normalization, PGT instance, Brans-Dicke analogy, W boson counterexample, and evasion conditions.
- Section 8.1 (lines 775–841): Concrete PGT derivation with Eq. (9), numerical suppression (10²⁹), unitarity scale behavior, symmetry exclusion, DR assessment.
- DR5 (lines 735–747): Formal decision rule with explicit test procedure.
- 10 locations total (documented in `task_final_mcl_sharpening_note.md`).

**Strength of defense:** Strong. The lock is stated as a general field-theory pattern (canonical normalization), demonstrated concretely in PGT, cross-checked against Brans-Dicke, given a counterexample (W boson), and translated into a testable decision rule. This is more than a one-paragraph observation — it is a structural analysis.

**Residual risk:** A referee expecting a multi-page calculation may still feel the argument is "too simple." Response: the observation IS the result. The lock is a structural pattern, not a computation. Its value is in being recognized and articulated, not in computational difficulty.

---

## Attack 3: "You haven't proven this applies to ALL geometric DE theories."

**Severity:** Low — the paper doesn't claim universality.

**Where it's addressed:**
- Section 6.6 (line 649): "occurs generically when a single parameter controls both the kinetic normalization and the mass" — states the condition, not a universal claim.
- Section 6.6 (lines 663–669): Explicit evasion mechanisms listed — the paper acknowledges the lock CAN be evaded.
- 07_final_strength_check.md (lines 28–36): "The paper does not prove a no-go theorem. It identifies a structural pattern... A referee could ask for a formal proof... That proof does not exist and the paper does not claim it."

**Strength of defense:** Strong. The paper claims the lock is "a constraint that must be checked," not a universal no-go. This is the correct level of claim.

**Residual risk:** Minimal if the paper's language stays precise. A referee would have to misread to attack on this basis.

---

## Attack 4: "w = -1 is assumed, not derived — the whole framework is circular."

**Severity:** High — targets the framework's deepest limitation.

**Where it's addressed:**
- Section 3.1 (lines 269–285): Explicitly labeled "What this is" (phenomenological scaling ansatz) and "What this is not" (not a derivation of w = -1). The paragraph "For the residual to persist as a true vacuum energy, one must show..." directly states the gap.
- Section 5 (closures): Four failed attempts to derive w = -1 are the paper's central negative result.
- Section 8.1 (Foundation A): Fifth attempt, also failed.
- Conclusion (lines 1074–1075): "The derivation of late-time w = -1 from geometry... remain[s] open problems."
- Claims table: w = -1 listed as **Assumed — Not derived**.

**Strength of defense:** Strong. The paper's entire thesis is "we tried to derive this and failed; here is what we learned from the failures." This is not circular — it is the scientific content.

**Residual risk:** A referee who believes only derivation-based papers belong in PRD could recommend rejection. Response: the systematic closure of derivation routes and the identification of structural requirements (especially the mass-coupling lock) ARE the results. This is a landscape-mapping paper.

---

## Attack 5: "Why should I care about closures of routes YOU chose? Other routes might work."

**Severity:** Medium — challenges completeness.

**Where it's addressed:**
- Section 4 (lines 468–504): Routes are described as "four routes... each with predefined gates and kill criteria frozen before computation." They are not arbitrary — they are the four minimal routes available in the minimal ECH+Dirac model.
- Section 8 (lines 766–906): Three non-minimal directions identified (Foundations A, B, C). Foundation A tested. B and C explicitly listed as untested.
- Section 9.4 (lines 1017–1033): "What would change this assessment" — explicitly lists four developments that would upgrade the framework.

**Strength of defense:** Good. The routes tested are the exhaustive set of minimal-model approaches. The paper explicitly flags what remains untested (Foundations B, C) and what new physics could change the picture. No claim of exhaustiveness beyond the minimal model.

**Residual risk:** A referee with a specific untested mechanism in mind could say "you didn't try X." Response: the decision rules (DR1–DR5) provide a pre-built test for any proposed X. The paper's contribution is not closing all routes — it is providing the methodology and requirements for evaluating any route.

---

## Summary

| Attack | Severity | Defense strength | Risk |
|--------|----------|-----------------|------|
| Part I is standard | Medium | Good (preempted) | Referee stops reading |
| MCL is too simple | Medium-high | Strong (10 locations) | Referee wants computation |
| Not universal | Low | Strong (not claimed) | Minimal |
| w = -1 circular | High | Strong (entire thesis) | PRD standards |
| Routes are arbitrary | Medium | Good (exhaustive + DR framework) | Specific counterexample |

**Overall assessment:** No attack is unanswered. The two highest risks (circularity and "too simple") are addressed structurally by the paper's design. The paper is defensible.
