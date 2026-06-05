# P2 2026-06-04_R4fixed — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 13.8s

---

**Referee Report for P2 (Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook)**

**P2-E1 (ESSENTIAL)**  
Section: Abstract (entire), page 1–2.  
Problem: The abstract contains multiple internal-audit and version-history artifacts, including “R4: older-draft parenthetical removed,” “post-arXiv TODO,” “the abstract previously gave only the central ∼2.6σ,” and repeated references to “the convention-reversal halving applies independently of where in the systematic-budget chain the figure is quoted.” These are review-log prose, not manuscript content.  
Required fix: Delete every such phrase. The abstract must stand alone as a clean summary of results.

**P2-E2 (ESSENTIAL)**  
Section: Abstract, page 1–2.  
Problem: The abstract does not accurately summarize what the paper proves. It presents a headline 3–5σ range, an optimistic 5.2–5.5σ, a halved range under an alternative convention, a Bayes-factor envelope 10–17, and a separate idealized joint (fNL, nfNL) Fisher result whose numerical value is explicitly “not quoted here in the abstract until that release lands.” The reader cannot determine what is actually demonstrated versus what is hoped for or deferred.  
Required fix: Rewrite the abstract to state only the quantities that are fully computed and justified in the body under a single, fixed convention and set of assumptions. Remove all deferred or conditional numbers.

**P2-E3 (ESSENTIAL)**  
Section: Abstract and §IV (page 7–8).  
Problem: σ(fNL) values obtained under different null procedures (CMB Fisher signal-only weighting r = 0.876 versus realistic LSS/SPHEREx noise weighting r ≈ 0.83) are presented as if they lie on the same scale and can be directly converted into a single “∼3–5σ” headline. No qualification is given that the two weightings produce systematically different effective variances.  
Required fix: Either adopt one fixed weighting scheme throughout or explicitly propagate the difference into separate, non-overlapping significance ranges with no combined headline.

**P2-E4 (ESSENTIAL)**  
Section: Entire manuscript (multiple locations, e.g., §II C, §VI, Table II captions, page 10–12).  
Problem: The body is saturated with review-log language, prior-version captions, cross-references to “the abstract envelope,” “the recommended headline,” “a reader who only reads this subsection,” and explicit statements that certain numbers were changed between rounds. Examples include the long Table II note beginning “Note: prior versions of this caption…” and the paragraph that states “the abstract, Table II, and the bullet list above are now numerically aligned.” These are internal audit tags.  
Required fix: Remove every such sentence. The manuscript must read as a finished paper, not a response to previous referee comments.

**P2-M1 (MAJOR)**  
Section: Abstract and §IV.  
Problem: The paper repeatedly describes itself as a “sensitivity recast” of Heinrich et al. (2024) rather than an independent forecast, yet the abstract and conclusion present 3–5σ and 5.2–5.5σ figures as new results. The distinction is never made clear to the reader.  
Required fix: State unambiguously in the abstract and introduction that all numerical significances are rescalings of a previously published Fisher matrix, and quantify the additional uncertainty introduced by that rescaling.

**P2-M2 (MAJOR)**  
Section: §VI and Table II.  
Problem: Bayes factors are reported as “BF ∼ 10–17” while the text simultaneously states that the values are “sensitive to the assumed prior widths,” that the delta-function prior is “the theoretical-maximum upper bound,” and that any realistic theoretical uncertainty “would reduce the Bayes factor.” The headline envelope therefore mixes an unrealistic limiting case with a recommended case without clear separation.  
Required fix: Report only the Bayes factor obtained under the single recommended prior choice; move all prior-sensitivity scans to a dedicated subsection or appendix and do not quote the delta-prior maximum in the abstract or conclusion.

**P2-M3 (MAJOR)**  
Section: §II A (page 3–4).  
Problem: The claim that the template mismatch is quantified “for the first time” is unsupported. The text itself cites a literature search “confirming no prior quantification … (2009–2024),” but no systematic search protocol or exclusion criteria are provided, rendering the “first” assertion unverifiable.  
Required fix: Either remove the “first time” phrasing or supply a reproducible search statement with explicit date range and keywords.

**P2-M4 (MAJOR)**  
Section: §IX D (page 16–17).  
Problem: An idealized joint (fNL, nfNL) Fisher significance of ∼9.9σ is quoted even though the required six-bin Fisher inputs are “deferred to a companion artifact” and “not yet on disk.” The number is therefore not reproducible from the present manuscript.  
Required fix: Remove the 9.9σ figure until the companion inputs are public or recompute it from material contained in this paper.

**P2-N1 (MINOR)**  
Section: Multiple locations (e.g., §IV, §V).  
Problem: The paper states that MegaMapper “is not yet approved or funded” and that its projections are “speculative motivation, not firm forecasts,” yet still quotes a 3–7σ range in the abstract.  
Required fix: Move all MegaMapper numbers to a clearly labeled “illustrative projection” subsection and remove them from the abstract.

**P2-N2 (NIT)**  
Section: Table I caption and surrounding text.  
Problem: The table states that all values “match the published results [7] exactly,” but the preceding paragraph discusses a 0.5000 ratio at intermediate ϵ-order that is not shown in the table.  
Required fix: Either add the intermediate values to the table or delete the ratio claim from the caption.

**P2-N3 (NIT)**  
Section: Throughout.  
Problem: Repeated near-duplication of long explanatory paragraphs (e.g., the four-corner prior grid is described in prose, then again in the table note, then again in the bullet list).  
Required fix: Consolidate each argument into a single location.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript cannot be accepted in its current form. It is not journal-clean: the body contains extensive review-log prose, version-history language, TODO placeholders, and meta-commentary that belong in a response letter. The abstract does not accurately represent what is proved, mixing deferred quantities, convention-dependent ranges, and idealized Fisher results whose inputs are not supplied. Several headline significances and Bayes factors rest on the conflation of different null weightings or on limiting priors that the text itself labels unrealistic. These are not cosmetic issues; they prevent a reader from determining what has actually been demonstrated. A cleaned and substantially shortened revision that removes all internal audit material, adopts a single fixed convention and weighting scheme, and reports only quantities that are fully reproducible from the present text could be reconsidered.