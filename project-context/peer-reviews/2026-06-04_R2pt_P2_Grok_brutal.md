# P2 2026-06-04_R2pt — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 12.8s

---

**Referee Report: P2 (Testing the Matter Bounce with Primordial Non-Gaussianity)**

**ESSENTIAL**

**P2-E1**  
Section: Abstract (p. 1)  
Problem: The abstract states “the SPHEREx multi-tracer bispectrum achieves … template-corrected significance ∼ 3–5σ after the combined systematic budget” and “the bispectrum-only 5.2–5.5σ is the headline forecast,” while only parenthetically noting that the Li & Brandenberger convention halves these numbers to ∼ 1.5–2.5σ. The body (Sec. II C, App. A) shows the convention choice is unresolved and that the halved values are the correct Planck-convention lower bound.  
Required fix: Rewrite the abstract so the headline significance range is 1.5–5σ (or equivalent) with the convention ambiguity stated as a leading caveat, not an afterthought. The abstract must reflect only what the body rigorously proves under both conventions.

**P2-E2**  
Section: Abstract & Sec. VI (pp. 1, 10–12)  
Problem: Bayes-factor claims (BF ∼ 10–17) are presented as the headline result while the text repeatedly states that these values are prior-dependent, that broader bounce priors monotonically reduce BF, that the delta-prior row is only a “theoretical maximum,” and that the numbers are “illustrative … not definitive model-selection evidence.” Different Monte-Carlo ensembles and analytic formulae are mixed without a single, reproducible prior set.  
Required fix: Remove all numerical BF claims from the abstract. Retain only a qualitative statement that discrimination power is prior-dependent and at most O(10) under the authors’ preferred priors. Supply a single, fixed prior specification and a clean table in Sec. VI.

**P2-E3**  
Section: Entire manuscript (multiple locations, e.g., pp. 1, 10, 12, 16, 22)  
Problem: The text contains extensive internal review artifacts: version strings (“v1.7.43”, “v1.7.35”, “R-next-c-MAJ-1”), script filenames (“04b fast ensemble.py”, “02 compute gr aware bayes update.py”), phrases such as “corrected v1.7.36 R-next-d-MIN-1 from prior ∼ 12”, and repeated “R42 reviewer” commentary. These are not journal-clean.  
Required fix: Delete every occurrence. The manuscript must read as a finished submission with no audit tags or version history.

**P2-E4**  
Section: Sec. II B & III B (pp. 3–7)  
Problem: Multiple distinct Fisher weightings (CMB signal-only, LSS noise-weighted, scale-dependent-bias 1/k^{2}, uniform) produce r values in [0.829, 0.876] that are then used to rescale the same σ(fNL) = 0.7. These weightings are not equivalent; the resulting “σ” values are not on a common scale, yet they are combined into single headline ranges (3–5σ, 5.2–5.5σ).  
Required fix: Present each weighting scheme’s forecast in a separate, clearly labeled column or subsection. Do not quote a single combined significance range unless an explicit joint marginalization is performed and documented.

**P2-E5**  
Section: Abstract & Sec. IV (pp. 1, 8)  
Problem: The abstract claims the 5.2–5.5σ figure is obtained “after the combined systematic budget,” yet the body shows that relaxing the bϕ universality assumption alone degrades the optimistic value to ∼ 3.5–4.5σ and that GR marginalization at σGR = 1.0 further reduces it. The abstract therefore misrepresents the post-systematic result.  
Required fix: Align the abstract exactly with the most conservative post-systematic range that survives all listed systematics (including bϕ marginalization and convention choice).

**MAJOR**

**P2-M1**  
Section: Sec. VI & Table II (pp. 10–12)  
Problem: The four-corner prior grid and the “recommended headline” BF ∼ 10 are chosen after the fact; the text acknowledges that the curvaton-natural [−5, +5] prior is more physically motivated yet still promotes the broader [−15, +15] result.  
Required fix: Adopt one physically justified prior set as baseline before any results are quoted; recompute and present all numbers under that single choice.

**P2-M2**  
Section: Sec. IX & abstract (pp. 1, 16)  
Problem: The claim that the joint (fNL, nfNL) SDB Fisher yields ∼ 9.9σ is presented as an “idealized-Fisher self-consistency check,” but the required six-bin Fisher inputs are deferred to a companion artifact that does not exist in the submission.  
Required fix: Either remove the 9.9σ number or supply the full Fisher matrix and inputs in the present manuscript.

**P2-M3**  
Section: Sec. II B (p. 4)  
Problem: The 10,000-sample null-space scan and the 200-injection-recovery test both rely on an internal symmetrized monomial basis that the authors themselves note is not the basis used by Cai et al. The under-determination is therefore partly an artifact of the authors’ basis choice.  
Required fix: Quantify the template mismatch using Cai et al.’s original single-time-ordering polynomial (or demonstrate that the symmetrized basis yields identical physical predictions).

**P2-M4**  
Section: Length (23 pp.)  
Problem: The manuscript is dominated by repeated explanations of the same systematics, prior-sensitivity tables, and self-referential script citations. The core methodological advance (template-overlap quantification for one specific bispectrum shape) does not justify 23 pages.  
Required fix: Reduce to ≤ 15 pages by moving all prior grids, script lists, and extended convention audits to a concise appendix or companion note.

**MINOR**

**P2-m1**  
Section: Sec. I (p. 2)  
Problem: Repeated use of “minimally parameterized” and “mechanism-independent” without a crisp one-sentence definition that survives the six assumptions listed two paragraphs later.  
Required fix: Provide a single-sentence operational definition.

**P2-m2**  
Section: Sec. III B (p. 6)  
Problem: The statement “the mismatch is intrinsic to the shape” is correct but is repeated almost verbatim in three places.  
Required fix: Consolidate.

**NIT**

**P2-n1**  
All figure captions and Table I: axis labels and column headings use inconsistent capitalization and spacing.  
Required fix: Standardize.

**P2-n2**  
Sec. II A (p. 3): “the radius choice across more than an order of magnitude in scan volume” is unnecessary repetition of the preceding sentence.  
Required fix: Delete.

**Summary recommendation**  
REJECT

The manuscript cannot be considered for publication in its present form. It contains pervasive internal review artifacts, an abstract that materially misrepresents the robustness of the quoted significances, and an uncontrolled proliferation of prior- and convention-dependent numerical claims presented as headline results. Even after removal of the audit language, the scientific content would require a major rewrite (new abstract, single fixed prior set, separate treatment of incompatible Fisher weightings, and substantial shortening) before it could be re-evaluated. The core template-mismatch calculation is potentially publishable as a concise methods note once these issues are addressed, but the current 23-page submission does not meet PRD standards for clarity, reproducibility, or honest reporting of uncertainties.