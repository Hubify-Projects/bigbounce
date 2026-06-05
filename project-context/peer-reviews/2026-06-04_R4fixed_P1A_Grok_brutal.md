# P1A 2026-06-04_R4fixed — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 13.0s

---

**Referee Report: P1A**

**Paper Title:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

**Date of Report:** 2026-06-04

The manuscript is not journal-clean. It contains pervasive internal review artifacts, version-history language, references to non-public companion papers, and hedging that undermines its own central claims. The abstract does not accurately represent what the body proves. The contribution is a negative result (channel-level amplitude closure under restrictive assumptions) presented with inflated framing. The paper is excessively long for the actual advance.

**ESSENTIAL findings**

- **P1A-E1** (Abstract, p. 1): The abstract states “we report 13 logically-independent mechanism-class constraints” while the body immediately qualifies that “B8 is subsumed by B14” and the routes “are not proven to be a complete diffeomorphism-invariant operator basis.” The abstract therefore misrepresents the logical independence and scope. Required fix: Rewrite the abstract to state exactly what is proven (four enumerated channels closed at amplitude level under an on-shell scaling ansatz, restricted to canonical scalar matter) without the independence claim.
- **P1A-E2** (Abstract and Sec. I, throughout): The text repeatedly refers to “companion work in preparation [2,6]”, “Paper I(b) [6]”, “internal MCMC analysis”, “frozen accepted samples”, “R̂ − 1 ≈ 3×10−2”, and running chains. These are review-log artifacts. Required fix: Remove every reference to non-public or in-preparation companions; all numerical results used in the argument must be either published or removed.
- **P1A-E3** (Sec. I A, p. 3 and Sec. IV Scope paragraph): The paper claims a “perturbation-transparency theorem” and “14-constraint catalog” while explicitly limiting the result to canonical scalars and stating that Jackiw–Pi and parity-odd four-fermion operators are omitted. The framing “theorem” and “catalog” is false. Required fix: Retitle and rephrase all claims as “channel-level amplitude constraints under the stated restrictions.”
- **P1A-E4** (Sec. II C 1 and Appendix B): The dark-energy mapping rests on an on-shell scaling ansatz whose off-shell dimension is +1. The text acknowledges this but still presents Ntot ≈ 92 as a structural result. Required fix: State in the abstract, introduction, and conclusions that the entire dark-energy route is an ansatz, not a derivation from the ECH action.
- **P1A-E5** (Sec. X and Sec. XIII): The two “surviving” predictions (fNL = −35/8 and β ≈ 0.27°) are explicitly stated to be “not predictions of ECH itself” and “not a distinctive ECH prediction.” Their inclusion as headline results is therefore misleading. Required fix: Remove both from the abstract and executive summary or clearly label them as external to the ECH closure claim.

**MAJOR findings**

- **P1A-M1** (Entire manuscript): The paper is 21 pages long yet delivers a negative result whose positive content is a single restricted decoupling statement plus a list of known barriers. Recommended maximum length after revision: 12 pages.
- **P1A-M2** (Sec. IX and Table II): Barriers 5, 6, 7, 9, and 13 are labeled “known results” or “structural/philosophical observations.” Their inclusion inflates the count of “constraints.” Required fix: Remove or clearly segregate non-novel items.
- **P1A-M3** (Sec. IV B, Eq. 15): The one-loop suppression calculation contains an explicit admission that an earlier version treated eV·s as dimensionless. The corrected ratio is still presented as robust, but the derivation is ad hoc. Required fix: Provide a fully dimensionally consistent derivation or drop the quantitative claim.
- **P1A-M4** (Sec. XIV D): The “structural tension” between Ntot ≈ 92 and erasure of fNL is presented after the four-route closure has already been asserted. It functions as post-hoc reinforcement rather than an independent result. Required fix: Either integrate it into the main no-go argument or remove it.
- **P1A-M5** (Sec. I and Sec. XV): The abstract and conclusions use “central result” and “theorem” language for a statement valid only for canonical scalar matter with no non-minimal couplings. Required fix: Add the restriction to every occurrence of the result.

**MINOR findings**

- **P1A-m1** (Sec. II A 2): The one-loop coefficient α/M is motivated by Freidel et al. and Mercuri but not derived from them. The text acknowledges this; the motivation paragraph should be shortened to one sentence.
- **P1A-m2** (Sec. XII A): The reheating thermal-reset barrier is introduced as “supporting B14” after B14 has already been proven. It is redundant and should be deleted.
- **P1A-m3** (Table I footnote): The footnote mixes Fisher-ideal and post-systematic significances without a single clear number. Replace with one unambiguous forecast value or remove the table entry.

**NIT findings**

- **P1A-n1** (p. 2 Contents): “Barrier 8” and “Barrier 14” are listed separately despite the explicit statement that they are not independent. Minor editorial cleanup required.
- **P1A-n2** (Sec. II B): The range ρcrit ≃ 0.27–0.41 ρPl is described as “scheme-dependent” yet used as a fixed window in later equations. Add a single clarifying clause.

**Summary recommendation**

**MAJOR REVISIONS**

The manuscript cannot be accepted in its present form. It is saturated with internal review language, references to unpublished companion papers, and self-undermining hedges that render the abstract inaccurate. The actual scientific content is a restricted negative result whose scope is narrower than the title and abstract imply. After removal of all non-public material, excision of non-novel barriers, correction of the abstract, and reduction to ≤12 pages, the paper could be reconsidered as a concise note on perturbation decoupling in minimal ECH with canonical scalars. Until those changes are made, the paper does not meet Physical Review D standards for clarity, accuracy, or appropriate length.