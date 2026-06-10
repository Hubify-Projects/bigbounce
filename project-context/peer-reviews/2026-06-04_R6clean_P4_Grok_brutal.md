# P4 2026-06-04_R6clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 16.4s

---

**Referee Report for P4 (Physical Review D submission)**

**ESSENTIAL — P4-E1**  
Section: Abstract (opening paragraph) and title; also Sec. IV C (p. ~17–19) and Table II.  
Problem: The headline result is presented as “−0.12σ” (subsample-mask MASTER) while the body simultaneously reports +3.64σ (canonical-mask direct-MC), +4.84σ (monopole-only post-MASTER), and multiple other estimators whose null distributions are explicitly stated to be non-comparable. The qualification note (“σ values … are not directly comparable across estimators”) appears only after the abstract and is not repeated in the title or abstract itself.  
Required fix: Rewrite the abstract and title so that every quoted σ is immediately accompanied by its null procedure and mask; remove any implication that −0.12σ is a single, universal significance.

**ESSENTIAL — P4-E2**  
Section: Sec. VI C (sensitivity floor) and abstract.  
Problem: The claimed “sub-percent sensitivity” and “0.29% Fisher floor” are derived under the assumption of zero systematic dipole projection. The catalog retains a 9.5σ residual monopole after TTA; no cross-correlation of that residual with PSF ellipticity, depth, or scan direction is shown to be consistent with zero on cosmological scales. The 0.2% / 0.75% numbers are therefore statistical-only upper bounds presented as experiment sensitivity.  
Required fix: Either (a) perform and report the PSF/depth cross-power test that closes the systematic floor, or (b) relabel all sensitivity statements as “statistical-only” and state the systematic floor explicitly as “not yet demonstrated.”

**ESSENTIAL — P4-E3**  
Section: Body prose throughout (e.g., Sec. III E, Sec. IV B, Sec. VI D 0 c).  
Problem: Multiple instances of version-history / retraction language appear in the published text: “We therefore retract the original ∆ = −1.35% argmax-CW-fraction claim”, “the earlier ∼0.79% value … is corrected here”, “supersedes the earlier analytic projection”. These are internal audit/review artifacts.  
Required fix: Remove every sentence that describes what was retracted, corrected, or superseded in prior drafts. Retain only the final scientific statements.

**MAJOR — P4-M1**  
Section: Entire manuscript (54 pages).  
Problem: The paper is a null result plus a detailed systematics autopsy. The scientific payload (one new null at ℓ = 1 after two independent bias-mitigation stages, plus a quantified leakage channel) does not justify 54 pages.  
Required fix: Condense to ≤25 pages. Move all MC tables, injection-recovery grids, per-leg×confidence matrices, and repository URLs to supplementary material or a data-release note.

**MAJOR — P4-M2**  
Section: Sec. IV D and Sec. VI G 0 a (canonical-mask residual interpretation).  
Problem: The +3.64σ residual is attributed to “depth/morphology-correlated systematic” on the basis of three suggestive anchors (ℓ = 2 cross-spectrum, leg-proxy 25% closure, density-stratified null). No joint nuisance-marginalized spatial likelihood is performed; the bootstrap-rescaled zboot ≈ −18 is presented as decisive disfavour of a 1.7% primordial dipole while the text simultaneously admits the bootstrap does not calibrate far-tail probabilities.  
Required fix: Either downgrade the language to “suggestive but not confirmatory” or supply the missing joint fit with explicit covariance.

**MAJOR — P4-M3**  
Section: Sec. I and Sec. V A (comparison with Shamir).  
Problem: The text repeatedly states that a matched-footprint Ganalyzer reanalysis “is required for a likelihood-level exclusion” yet never performs it, while still claiming the present pipeline “disfavors” Shamir’s 2–4% amplitudes by a factor 6–12. This is an overclaim.  
Required fix: Remove all quantitative “factor of ∼6–12” language; retain only the statement that the result is inconsistent under the present classifier/selection/footprint.

**MINOR — P4-m1**  
Section: Sec. IV C (Table VI caption and surrounding text).  
Problem: The ℓ ≥ 2 bandpowers are reported with χ²/dof = 161.2/38 and attributed to monopole leakage, yet the table is still presented as part of the “angular power spectrum of the chirality asymmetry map.”  
Required fix: Move the ℓ ≥ 2 rows to a systematics-diagnostic table or clearly label them “not interpreted as parity signal.”

**MINOR — P4-m2**  
Section: Sec. III A (declared analysis hierarchy).  
Problem: The hierarchy is explicitly post-hoc (“fixed after the first round of catalogue results”). While the text is honest, the section heading “Declared Analysis Hierarchy” is misleading.  
Required fix: Retitle “Post-hoc Estimator Hierarchy (fixed after first catalogue results).”

**NIT — P4-n1**  
Section: Multiple figure captions and table footnotes.  
Problem: Repeated use of “available in the companion data repository” (≈30 occurrences) clutters the text.  
Required fix: Replace with a single statement in Sec. IX that all supplementary material is deposited at the cited repository.

**NIT — P4-n2**  
Section: Sec. VI G 0 a (symmetry classification paragraph).  
Problem: The long parenthetical clarification of parity-even vs. parity-odd observables is correct but interrupts the narrative.  
Required fix: Move to a footnote or short appendix.

## Summary recommendation  
**MAJOR REVISIONS**

The manuscript contains a technically careful null result and a useful quantification of a monopole–mask leakage channel. However, the combination of (i) an over-long 54-page format, (ii) headline σ values drawn from non-comparable nulls without uniform qualification, (iii) explicit version-history/retraction prose in the body, and (iv) statistical-only sensitivity claims presented as experiment reach requires substantial revision before the paper can be considered journal-clean. Once the essential fixes above are addressed and the manuscript is condensed, the core scientific claim (no detectable ℓ = 1 dipole above the demonstrated empirical threshold under the present pipeline) would be acceptable.