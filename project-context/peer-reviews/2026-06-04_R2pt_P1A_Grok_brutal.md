# P1A 2026-06-04_R2pt — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 14.0s

---

**Referee Report: P1A (Round 2026-06-04_R2pt)**

**ESSENTIAL findings**

P1A-E1. Abstract (p. 1) and Sec. I (p. 3): The abstract states “the central result is a perturbation-transparency theorem” and claims the four routes “fail at the amplitude level,” yet the body repeatedly qualifies that the routes are “not proven to be a complete diffeomorphism-invariant operator basis,” the dark-energy mapping is “a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4,” and “we do not claim a full operator-basis closure.” Required fix: Rewrite the abstract to state only what is actually proved under the listed caveats; remove all language implying a general no-go theorem.

P1A-E2. Throughout the manuscript (e.g., p. 1, p. 4, Sec. IV Scope paragraph, Sec. XIV E, Appendix B): The text contains extensive version-history language, internal audit tags, and review-log prose, including “(Dated: June 2, 2026 PDT — v1A.0.44)”, “queued”, “the migration is documented in Paper III § 6”, “earlier-draft analyses”, “on-record-deferred”, “the ∼2% precision of the headline Ntot figure is ansatz-dependent”, and repeated references to “companion work in preparation [2,6]” whose MCMC samples, convergence diagnostics, and Fisher forecasts are never shown. Required fix: Remove every such phrase; the manuscript must be journal-clean and self-contained.

P1A-E3. Sec. I, Sec. IV, Sec. IX, Sec. XIII, and Table II: The paper presents 13 “logically-independent” barriers (14 historical entries) as closing the minimal-ECH dark-energy routes, yet simultaneously states that Barriers 8 and 14 are “not logically independent” (B8 is subsumed by B14) and that two omitted operators (Jackiw–Pi term and parity-odd four-fermion partner) are not closed. Required fix: Either reduce the catalog to the actual number of independent constraints or withdraw the claim of channel-level closure.

P1A-E4. Sec. II C 1 and Sec. XIV D: The structural tension between Ntot ≈ 92 (required for dark-energy suppression) and erasure of the matter-bounce fNL = −35/8 at SPHEREx scales is presented as a robustness check, but fNL = −35/8 is explicitly stated to be “not a distinctive ECH prediction” and “a property of the matter-bounce class [1] derived from the contraction-phase cubic action with no ECH input.” Required fix: Remove the tension as evidence against ECH; it is not a constraint on the theory under review.

P1A-E5. Sec. XIII and abstract: The two “surviving” predictions (fNL = −35/8 and β ≈ 0.27°) are repeatedly labeled “mechanism-independent” and “not predictions of ECH itself.” The abstract nevertheless presents them as part of the paper’s results. Required fix: Excise both from the abstract and from any claim of ECH-derived predictions.

**MAJOR findings**

P1A-M1. Entire manuscript: The paper is 21 pages long yet consists almost entirely of negative results, enumerated barriers, and forward references to six companion papers “in preparation.” The actual new technical content (the perturbation-transparency argument in Sec. X) occupies roughly four pages. Recommended maximum length for the claimed contribution: 8–10 pages.

P1A-M2. Sec. IV (all subsections) and Appendix B: The four routes are closed only after inserting a phenomenological on-shell scaling ansatz whose dimensional mismatch is acknowledged but not derived. The closure statements therefore rest on an assumption external to the minimal ECH action. Required fix: State explicitly in every closure paragraph that the result holds only under the additional ansatz of Eq. (B2) and is not a theorem of the ECH Lagrangian alone.

P1A-M3. Sec. X B and X D: The proof that the Holst term reduces to a total derivative assumes a torsion-free Levi-Civita connection from the outset. The argument is therefore circular for any theory in which torsion is dynamical. Required fix: Restrict the theorem statement to “canonical scalar matter with algebraic torsion only” and add an explicit caveat paragraph.

P1A-M4. Sec. II A 2 and Sec. IV B: The one-loop coefficient in Eq. (14) is introduced as “motivated by (but not literally derived in)” Mercuri et al.; the subsequent amplitude suppression of ∼58–60 orders of magnitude is then treated as a firm no-go. Required fix: Either derive the coefficient or downgrade the claim to “illustrative upper bound under an assumed operator form.”

**MINOR findings**

P1A-m1. Sec. I A (p. 3): The sentence “the original contributions are: 1. 14-constraint catalog…” is factually inconsistent with the later admission that only 13 constraints are logically independent. Required fix: Correct the count.

P1A-m2. Table I footnote a and Sec. XII A: The claim that the framework “reparameterizes the fine-tuning hierarchy from 10122 to ∼105” is presented without qualification that the 105 residual is still set by hand via choice of Ntot. Required fix: Add the explicit statement that no dynamical mechanism selects Ntot.

P1A-m3. Sec. XIII (2): The LiteBIRD forecast significance is given as “∼9σ” using the naive ratio 0.27°/0.03° while the text itself notes that the proper model-discrimination test against the WMAP+Planck central value yields only ∼0.73σ. Required fix: Remove the 9σ figure or replace it with the differential test.

P1A-m4. Sec. IV D: The statement that Route 4 is closed by a “naturalness objection rather than amplitude no-go” is inconsistent with the subsequent paragraph that shows an overshoot of 22–36 orders of magnitude when mθ lies in the natural ALP range. Required fix: Reconcile or delete the contradictory phrasing.

**NIT findings**

P1A-n1. Multiple locations (e.g., p. 1, Sec. IV E): The phrase “the 13 logically-independent mechanism-class constraints (the prior count of 14 retained Barrier 8…)” is unnecessarily convoluted. Simplify.

P1A-n2. Sec. II B: The parenthetical remark that the 0.27–0.41 ρPl window “should be read as a scheme-dependent range rather than as a published LQC range” is an internal note; move to a footnote or delete.

P1A-n3. Sec. XII A: The long paragraph beginning “Physical-versus-mathematical scope of Dinf” is meta-commentary on earlier drafts; condense to a single sentence.

P1A-n4. References: Multiple citations to “Paper II [2]”, “Paper III [46]”, “Paper IV [23]”, and “companion Paper I(b) [6]” that do not yet exist on the arXiv. Replace with “in preparation” only if the works are actually submitted; otherwise remove.

## Summary recommendation
**REJECT**

The manuscript is not a journal-clean, self-contained submission. It is riddled with version-history language, internal audit notes, and forward references to six unpublished companion papers whose numerical results are required to support the claims. The central “closure” result is not a theorem of minimal ECH but a set of negative statements that hold only after the insertion of an external phenomenological ansatz whose dimensional inconsistency is openly acknowledged. The two “surviving” predictions advertised in the abstract are explicitly stated in the body to be neither ECH predictions nor logically independent of the barriers already counted. These defects are structural and cannot be repaired by minor editing.