# P4 R7 — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 13.1s

---

**Referee Report for P4 (Physical Review D)**

**P4-E1 (ESSENTIAL)**  
Section: Abstract (p. 1)  
Problem: The abstract states a headline null result ("−0.12σ Subsample-Mask ℓ = 1 Null") while the body contains a +3.64σ canonical-mask residual (Sec. IV C, VII) that is only later attributed to systematics via a multi-null battery. The abstract does not accurately summarize what the paper proves.  
Required fix: Rewrite the abstract to explicitly state both the primary null (−0.12σ on the subsample mask) and the non-headline canonical-mask residual (+3.64σ, systematics-attributed), with a one-sentence qualification that σ values derive from distinct null procedures.

**P4-E2 (ESSENTIAL)**  
Section: Throughout (e.g., Abstract, Sec. IV C, Table VI, Sec. VI B, Table II footnotes)  
Problem: Multiple σ values are reported from qualitatively different null procedures (per-pixel-shuffle, label-shuffle/MASTER, binomial monopole-only, bootstrap, direct-MC rank). The single sentence in the abstract ("Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators") is insufficient; headline numbers continue to be presented as if on a common scale.  
Required fix: Remove all cross-estimator σ comparisons from the abstract, introduction, and conclusions. Retain only p-values or explicit per-estimator statements. Add a dedicated methods subsection that tabulates each estimator, its null, and its variance properties.

**P4-E3 (ESSENTIAL)**  
Section: Sec. I (p. 3), Sec. V A, Sec. VI A  
Problem: Repeated language of internal revision history and supersession ("the 3,321,795 snapshot … is superseded", "earlier drafts also quoted … that figure is superseded", "the ∆ = −1.35% … sign-flips"). These are review-log artifacts appearing in the paper text.  
Required fix: Delete every instance of "superseded", "earlier drafts", "preliminary", and "working hypothesis" phrasing that refers to the evolution of the manuscript itself.

**P4-M1 (MAJOR)**  
Section: Entire manuscript (54 pp)  
Problem: The paper is far too long for its central contribution (a null dipole result plus a systematics diagnosis). The contribution does not justify 54 pages of tables, footnotes, multi-null batteries, and injection-recovery sweeps.  
Required fix: Reduce to ≤ 25 pages. Move all but the two primary estimators, the monopole-leakage null, and the injection-recovery threshold into a concise methods appendix or separate data-release note.

**P4-M2 (MAJOR)**  
Section: Sec. IV D, Table VIII, Sec. VI G 0 a  
Problem: The canonical-mask +3.64σ residual is presented as "strongly disfavoured" for a primordial dipole via a 9-template WLS fit, yet the paper simultaneously states that the bootstrap covariance only calibrates a scale, not a tail probability, and that a fully specified spatial likelihood is future work. The claim exceeds what is proved.  
Required fix: Downgrade the language to "inconsistent with a clean primordial dipole at 1.7% under the adopted 9-template model" and explicitly label the result as preliminary pending a proper spatial likelihood.

**P4-M3 (MAJOR)**  
Section: Sec. VI C (sensitivity floor)  
Problem: The abstract and Sec. I quote a "sub-percent sensitivity" and a 0.29% Fisher floor, but the empirically demonstrated 50%-recovery-at-3σ threshold on the actual pipeline is 0.75%. The statistical-only Fisher number is presented as the operative sensitivity.  
Required fix: Replace all sensitivity statements with the empirical 50%-recovery threshold (0.75%) as the primary quoted number; move the Fisher derivation to an appendix and label it "ideal-statistical limit only."

**P4-N1 (MINOR)**  
Section: Title (p. 1)  
Problem: The title is 7 lines long and contains three distinct scientific claims plus a sample size.  
Required fix: Shorten to a single declarative sentence (e.g., "Null ℓ = 1 chirality dipole in 3.2 million DESI Legacy spirals after equivariant test-time averaging").

**P4-N2 (MINOR)**  
Section: Sec. III A (Declared Analysis Hierarchy)  
Problem: The hierarchy is explicitly post-hoc ("declared after the first round of catalogue results").  
Required fix: Remove the paragraph or rephrase as "We adopt the following ordering of estimators for the cosmological conclusion."

**P4-N3 (NIT)**  
Section: Multiple tables and figure captions  
Problem: Repeated boilerplate ("Verification data are available in the companion data repository", "available in the companion data repository") appears dozens of times.  
Required fix: Replace with a single statement in Sec. IX.

**P4-N4 (NIT)**  
Section: Sec. IV B, Table V  
Problem: The 9.5σ monopole offset is reported to high precision while the text simultaneously states that the true uncertainty may be larger because of spatially correlated systematics (Neff < Nspiral).  
Required fix: Quote only the binomial σ and add the explicit caveat that it is a lower bound.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript reports a technically careful null result on a large sample, but the central claim is not new in kind, the paper is grossly over-length, multiple non-comparable σ values are headlined, the abstract misrepresents the body’s treatment of the +3.64σ residual, and the text contains numerous internal-audit and revision-history artifacts. These problems are fixable but require substantial cuts and re-framing; a 25-page revision focused on the two primary null estimators and the monopole-leakage demonstration would be appropriate for Physical Review D.