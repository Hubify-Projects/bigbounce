# P2 2026-06-04_R4fixed — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 30.4s

---

# Referee report on P2 – “Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook”

I have read the manuscript line-by-line with the charge of checking statistical methodology, derivation continuity, dimensional consistency, arithmetic, and the traceability of every scalar quoted in the abstract and conclusions.  My comments are grouped by severity.

--------------------------------------------------------------------
ESSENTIAL
--------------------------------------------------------------------
P2-E1  Sec. VI/Table II & surrounding text ‑ version-history artefacts  
• Problem Body prose contains explicit review-log language:  
  “prior versions of this caption…”, “R42 Gemini 3.1-Pro P2 BLOCKER B-3”, “(immediately before §VI’s closing paragraph)”.  
  These violate instruction 8 and break anonymity.  
• Fix Delete every piece of version-tracking or review-audit meta-text from the scientific narrative.

P2-E2  Eq. (5) (p. 7) ‑ algebraic inconsistency between amplitude and variance mapping  
• Problem Equation (5) states  
  σ(f NL bounce) = σ(f NL local)/r,  
  yet all subsequent significances use r|fNL|/σ(fNL local) (i.e. **do not** divide the variance by r).  
  Only one mapping can be true.  The present paper mixes them, so at least one set of σ values is on the wrong scale.  
• Fix Provide a single coherent propagation formula, redo every numerical significance that depends on it, and update text, Figs. 2, 5 and Table IV.

P2-E3  Sec. III B vs. Sec. II null-space scans – incompatible quoted uncertainties for r  
• Problem Noise-weighted scan gives r = 0.84 ± 0.02; null-space scan gives 0.85 ± 0.13 (range 0.55–1.14).  Both are later used interchangeably.  
• Fix Adopt one master value (with an error budget that includes polynomial under-determination **and** noise weighting) and recalculate all projected significances.

P2-E4  Bayes-factor calculation – required inputs not released  
• Problem Headline Bayes factors (BF ≈ 10–17) rely on a Fisher matrix that depends on “framework-specific priors detailed in §VI” but the full six-bin kmin(z), n̄(z), … file is declared “deferred to a companion artifact”.  Reproduction is impossible.  
• Fix Upload the exact prior grids and Fisher inputs to the Git repo cited, cite the commit hash, and ensure that running the script yields the numbers in Table II and III.

P2-E5  Mixing σ values from incommensurable procedures  
• Problem The Planck PR4 number σ(fNL)=5.0 (CMB bispectrum) is recast together with the SPHEREx forecast σ=0.7 (galaxy bispectrum) inside the same sentence (“current data cannot discriminate…”).  These σ come from different estimators, sky coverage and systematics.  Presenting them side-by-side without qualification violates instruction 7.  
• Fix State explicitly that they are **not** comparable and never combine them in a ratio or joint significance.

P2-E6  Internal TODO tags still present  
• Problem “full four-vertex numerical evaluation discussed in Sec. II C”, “post-arXiv TODO”, “companion artifact”, “to our knowledge … only by Cai et al.” are un-resolved placeholders.  
• Fix Either provide the missing derivations/files or delete the placeholder language.

--------------------------------------------------------------------
MAJOR
--------------------------------------------------------------------
P2-M1  Systematic budget only sketched, not propagated  
The abstract headline “3–5 σ after the combined systematic budget” is not derived anywhere.  Individual degradations (photo-z, GR, bφ, etc.) are quoted qualitatively but never multiplied through.  A reader cannot reproduce the 3 σ floor.  Provide a table that lists every systematic, its multiplicative factor, the source citation, and the final combined σ.

P2-M2  Confusion between gauge-frame and CFC statements  
The manuscript first claims that the bounce-vs-inflation contrast is ∼290 in “either frame”, but later stresses that the CFC observable goes to zero in slow-roll.  This is self-contradictory.  Clarify exactly which observable each forecast uses and remove the sentence “either frame” in the abstract.

P2-M3  Unreferenced numbers  
The κ1 range 5.6–80 and c′ range 0.7–10 are stated with no explicit derivation, table, or equation reference.  Provide the algebra or numerical notebook that gives these bounds.

P2-M4  Over-claiming significance for MegaMapper  
σ(fNL)=0.5 is taken from the original MegaMapper white paper **without** the photometric-z scatter and GR corrections that you later admit are severe at z>2.  The claimed 7 σ upper end is therefore optimistic by at least a factor 1.5.  Quote a corrected range or label it clearly as “no-systematics”.

P2-M5  Paper length vs. contribution  
The manuscript is 22 pp, but 5 pp are version-history discussion and long quotation of other papers’ equations.  Recommend cutting to ≤18 pp.

--------------------------------------------------------------------
MINOR
--------------------------------------------------------------------
P2-m1  Duplication: “canonical Planck/local-template gauge convention” appears twice in the same line of the abstract.  
P2-m2  Typo: “phase3 fisher overlap.json” (missing capital).  
P2-m3  Figure 4 axis labels unreadable at journal column width – increase font.  
P2-m4  Footnote marker “3” in Sec. III B refers to no footnote.  
P2-m5  Cite the exact version of CAMB used for the ℓ-space Fisher check.

--------------------------------------------------------------------
NIT
--------------------------------------------------------------------
P2-n1  Eq. (A6) missing differential measure d3k in Fourier transform.  
P2-n2  “ultra-large-scale” adjective hyphenation inconsistent.  
P2-n3  Replace “Hehl-Datta–Mercuri” with the standard “Hehl–Datta–Mercuri”.

--------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

While the central idea is interesting and most scalar values check out numerically, the manuscript still contains internal audit tags, contradictory propagation of the template-mismatch factor, unreleased priors, and a non-reproducible systematic budget.  These must be fixed before the paper can be considered for publication.