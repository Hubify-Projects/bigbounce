# INT v3 Referee Report — P5 (DESI Chirality, catalog-native DESIVAST test)

- **model:** claude-opus-4-8 (subagent, independent referee leg)
- **date:** 2026-07-16 PT
- **paper:** P5 v0.1.141-2026-07-16 ("A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1")
- **pdf_sha256:** 4cca09d0aa963ae18b908bc17f57e9b1bf8f91e4ec8555f4c18d2e413a7580ac
- **venue:** The Astronomical Journal — profile AJ-OBSERVATIONAL
- **PDF exactness:** CONFIRMED (shasum -a 256 matches the pinned hash byte-for-byte)

**PARSED VERDICT: MAJOR REVISIONS**

---

## Referee report (verbatim)

You are an expert referee for The Astronomical Journal. I reviewed this Observational research article under profile AJ-OBSERVATIONAL to the standard of a real submission.

### (1) VERDICT: MAJOR REVISIONS

### (2) ISSUES

**[MAJOR] 1 — The manuscript's central input is an unpublished companion paper (Paper IV).**
Every chirality label (`class_eq`) and the global classifier monopole ΔfCW = −0.0026 are taken from "Golden, Paper IV, companion manuscript in preparation" (Ref. [3]; §II, §III A, Appendix A). Paper IV has no arXiv identifier and is not itself peer-reviewed. The manuscript's own §XIII Limitations concedes: "P5 must be re-verified against its independently reviewable final label, weight, and provenance release before submission" and "the focal result must be re-verified against the final published Paper IV catalog." A journal cannot complete review of a paper whose load-bearing classifier — its architecture, training, parity-equivariance validation, and accuracy floor — exists only in an in-preparation manuscript. Appendix A reproduces the methodology "for self-contained assessment," but a reproduced summary is not a reviewable source. This is a self-acknowledged pre-submission blocker and by itself forces at least major revisions: Paper IV must be public/submitted and reviewable before this paper can be assessed.

**[MAJOR] 2 — Scientific payload is thin relative to the effort; the null does not constrain physics or cosmology.**
The paper is explicit and repeated that the result "is not a physical-handedness, real-space, or cosmological constraint" (abstract, §I, §XII B, §XV) and that the classifier-label contrast is an attenuated proxy suppressed by a factor ≈ 0.3982 relative to any true physical asymmetry (§Appendix A, "Classifier-label scope"; κ = 0.40, 69.91% binary accuracy). The bounce-vs-inflation motivation that frames the program is essentially absent from the actual deliverable. As written, the headline is a null detection of a classifier-defined quantity in one DR1 catalog. The manuscript must state, in the introduction and abstract, a concrete reason a reader should care about *this specific* null — what hypothesis it forecloses, what future measurement it enables, or what systematic it characterizes — beyond "no literature model predicts this specific estimand" (§XII B). Otherwise this reads closer to a technical/negative note than an AJ observational article.

**[MAJOR] 3 — Post-hoc focal-estimate selection over a large analysis tree (researcher degrees of freedom).**
§V B and Table IV disclose that the analysis was not preregistered and that the focal released-parent hierarchy "was changed after review and after inspecting the data." Table IV enumerates 23 paths; the "focal" one was designated post-hoc, with all others relabeled "sensitivity." The honesty is commendable, but the framing choice — which estimand becomes the headline — was made after seeing outcomes. The null result mitigates the usual fishing concern (there is no detection being fit to), yet the reader still cannot distinguish a genuinely pre-specified estimand from a post-hoc-preferred one. Revision should (a) state plainly that no result in the paper is confirmatory, (b) either preregister the released-parent estimand for a future analysis or present the full path distribution as the primary object rather than elevating one path, and (c) move the "focal" language out of the abstract, where it currently implies a primacy the design does not support.

**[MINOR] 4 — Key void strata are counting-noise limited; the abstract should foreground this.**
The T-Web void bin is n = 428 (§VI B, Table VII); the DESIVAST/T-Web concordance cross-check is 0/6 objects (§VIII A); the void arm of the released-parent estimate is 31,937 of 145,766. The paper handles the smallness correctly (Jeffreys intervals, one-sided Clopper–Pearson, explicit "sample-size limited" statements), but the abstract presents many precise numbers without conveying that the void arm is where all the statistical power is thinnest. State the void-arm n and its 95% CI half-width (±3.7 pp, §XIII) in the abstract so the reach of the null is not overstated.

**[MINOR] 5 — Self-corroboration of the monopole is not independent.**
The paper re-measures the classifier monopole within its own matched sample (fCW^P5 = 0.49719, §VIII G) and describes this as "independently corroborating" Paper IV to ~8%. Because it is the same classifier labels re-binned, this is the same systematic re-measured, not an independent check; the ~8% enhancement is itself attributed to BGS-bright weighting. The language "independently re-measures / corroborates" (§VIII G, Appendix A) should be softened to "re-measures within-sample," and the residual 8% offset explained as a selection-weighting artifact rather than a corroboration.

**[MINOR] 6 — Data availability is incomplete at the submission candidate.**
Appendix C states no immutable Git tag or Zenodo DOI exists ("public tag pending"), and artifact links A37–A40 "will resolve after the release-candidate commit is pushed." The cluster-bootstrap provenance (§App C) notes the May sidecar raw hash does not match the current file and that "byte-identical row provenance ... cannot be independently attested." AJ requires a resolvable, archived data/code release at submission. All artifact IDs must resolve and a DOI-minted snapshot must exist before the paper is sent to referees.

**[MINOR] 7 — Length and defensive density hurt readability.**
At 42 pages with ~26 tables and a large sensitivity apparatus (five DESIVAST variants, T-Web, Tempel, ASTRA, Phase-2 sweep, multiple LEE schemes), much of the text reads as pre-emptive rebuttal rather than exposition. The abstract in particular packs ~15 numerical results into a single paragraph and is hard to parse. Consolidate the sensitivity paths into a single summary table with the detailed per-path material moved to a supplement, and rewrite the abstract to lead with the claim, the scope, and the one-line result.

**[MINOR] 8 — Verify figure legibility (Figs. 6, 8 Mollweide; Figs. 3, 5, 9 CI bars).**
The two full-page Mollweide σ maps (Figs. 6, 8) and the multi-panel CI figures carry the qualitative "no coherent structure" conclusion. Confirm at print resolution that the diverging color scale, the masked (grey) regions, and the small-n error bars remain distinguishable in grayscale and for color-vision-deficient readers, and that panel labels/colorbars are readable at column width.

### (3) Is the central claim supported?

Yes — within its explicitly narrow scope (a catalog-specific, classifier-label, redshift-space non-detection of a void/non-void chirality difference in DESI DR1), the null is well supported by a genuinely thorough battery of cross-checks and appropriately conservative statistics; the paper's principal weaknesses are its dependence on an unpublished companion catalog, its thin physical/cosmological payload, and the post-hoc, not-yet-archived nature of the analysis rather than any error in the null itself.

---

*Independent referee leg; fresh read of the exact pinned PDF. No coordination with other legs; verdict reflects a real-submission AJ bar.*
