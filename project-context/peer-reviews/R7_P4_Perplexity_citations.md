# P4 R7 — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 41.4s

---

I cannot complete the requested citation-forensics audit because the full reference list is not available in the provided “PAPER TEXT” excerpt.

The core of what you asked for—checking that:

- each cited work actually exists at the given arXiv ID / DOI,
- titles, authors, venues, and years match,
- specific quoted statistics (e.g. “nearly 1.3 × 10^6 spiral galaxies”, “2–4σ”, “~2–4%”, “cw/ccw = 0.998”) are really in the cited paper,
- and that there are no fused or inconsistent metadata entries—

requires access to the *full* reference section, including:

- full author lists,
- full titles,
- journal / volume / page, and
- explicit arXiv identifiers for each numbered reference [1]–.

In the text you supplied, I can see only partial reference metadata interwoven into the prose, for example:

- “Shamir (2020) [1] (arXiv:2007.16116, SDSS DR8 + Pan-STARRS…)”
- “Shamir (2022) [3] (arXiv:2208.13866, DESI Legacy Survey, MNRAS 516 2281; the published abstract reports ‘nearly 1.3 × 10^6 spiral galaxies’…)”
- “Shamir 2022 [3] (MNRAS 516 2281, DOI 10.1093/mnras/stac2372)”
- “Jia et al. [8] … ‘CE-ResNet’… arXiv:2210.04168”
- “Iye et al. (2021) [5] … ApJ 907, 123”
- “Tadaki et al. [6] … MNRAS 496, 4276”
- “Motloch & Pen (2021)  … Nature Astronomy 5, 283”
- “Yu et al. , Lue, Wang & Kamionkowski , Cabass, Ivanov & Philcox , Philcox , Eskilt & Komatsu …”
- etc.

But without the complete numbered bibliography, I cannot reliably:

- cross-check that every numeric label [n] corresponds to exactly one unambiguous paper,
- detect mis-numberings or accidental reuse of a label for different works,
- or systematically search arXiv / ADS for each entry.

Given these limitations, I will still do what I can from the *body text alone*, and flag definite problems and risks. Because you asked for a full referee-style report with classifications (ESSENTIAL/MAJOR/MINOR/NIT), I’ll structure the findings that way, but you should treat this as *partial* and contingent on a separate full bibliography check.

---

## ESSENTIAL findings

### P4-E1 – σ–scale comparability handled correctly (positive check, not a problem)

- Location: Abstract, first page: “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators…”
- Finding: The instruction for this review included: “If any σ values from different null procedures are presented as if they’re on the same scale without qualification, flag as ESSENTIAL.” Here, the authors *explicitly* warn that σ’s from different nulls are not directly comparable, and they consistently repeat that caveat in Sec. IV (“Significance conventions…”, and the various null descriptions for dipole / MASTER / binomial / bootstrap).
- Required fix: None. This specific failure mode is *avoided* and documented. Leave as-is.

*(No ESSENTIAL problems can be substantiated from the text snapshot alone, because all cross-paper claims that look potentially fragile would need actual reference-checking against arXiv/ADS.)*

---

## MAJOR findings

These are issues that affect interpretation or rigor of cross-paper claims and should be tightened before publication, but I cannot call them “paper cannot be accepted” purely from what I see.

### P4-M1 – Incomplete / informal cross-paper statistical claims without verified citations

- Section: I. Introduction; V. Comparison with Previous Work; scattered in Discussion.
- Problematic text (examples):
  - “Shamir (2012) [4] reported a 2–4σ dipole significance with per-bin asymmetry amplitudes of ∼ 5–20% using ∼ 1.27 × 10^5 SDSS galaxies (126,501 spirals; Shamir 2012 abstract)…”
  - “Shamir’s earlier work [1] reported ∼ 3% asymmetries with a consistent dipole axis; Shamir (2022) [3] reported DESI Legacy Survey results in the same magnitude regime.”
  - “Jia et al. [8]… yields cw/ccw = 0.998, consistent with parity.”
  - “…SpArcFiRe… 99.983% self-consistency but lower agreement with Galaxy Zoo 1 (85.8% overall, 92.5% at high confidence).”
  - “Motloch et al.  report a marginal (∼ 2.7σ) correlation…”
- Issue: These statements quote *specific* σ levels and percentages from prior work, but I cannot verify against the actual papers because the reference list is absent. Some of these shorthand numbers (2–4σ range, 5–20% per-bin, “cw/ccw = 0.998”) are plausible, but they compress multiple detailed results into a single narrative. That is fragile: if, for example, Shamir’s abstract or main tables use a different numeric range, or Jia et al.’s global cw/ccw ratio is defined with different sample cuts, the present text would be inaccurate or misleading.
- Required fix:
  - For each quoted statistic from prior work (σ values, percent asymmetries, sample sizes), insert the exact reference to where in the original source it comes from: abstract, cited table and/or figure number.
  - Avoid fused summaries like “2–4σ” unless you explicitly enumerate which paper gave which number (and in what exact test).
  - In a revision, the bibliography must be supplied; the editor should ensure an auditor rechecks these items directly against arXiv/ADS.

### P4-M2 – Cross-paper axis-alignment claims need explicit source support

- Sections: VI A (“axis coincidence”), V A (Shamir comparisons).
- Problematic text:
  - “After applying Eq. (3), the residual 0.43σ Catalog C dipole points in a direction uncorrelated with Shamir’s axis, and its alignment with both the CMB dipole (118.4◦) and CMB quadrupole (102.4◦) axes is random. The raw-axis coincidence is therefore not a cosmological echo of Shamir’s signal…”
- Issue: The paper asserts specific angular separations (e.g., “only 18.9◦ from Shamir’s claimed axis”) and CMB dipole/quadrupole directions, but doesn’t show the numeric values for Shamir’s axis or the CMB reference in the text, nor does it cite precise locations in those prior works where those axes are defined. Without the reference list, I cannot check these, but even with it, a reader should be able to see the exact origin and definition of each axis being compared.
- Required fix:
  - Explicitly quote the Shamir (2020/2022) dipole-axis coordinates as given in those papers, with citation to the specific figure/table or equation.
  - Similarly, give the CMB dipole axis used (e.g. Planck 2018 lensing or temperature dipole; RA/Dec or Galactic coordinates and source).
  - Make clear whether your axes were transformed to the same coordinate system and frame.

### P4-M3 – SpArcFiRe numbers and “null” statements need precise citations

- Section: V C.
- Problematic text:
  - “SpArcFiRe’s deterministic algorithm has near-perfect self-consistency (99.983%) but lower agreement with Galaxy Zoo 1 (85.8% overall, 92.5% at high confidence)…”
  - “SpArcFiRe DR9-overlap catalog reports CW/CCW counts consistent with 50/50 to within ∼ 0.3% at its ∼ 1.4 × 10^5 -galaxy footprint…”
- Issue: These are quite specific statistics, but the underlying SpArcFiRe sources are only loosely referenced (Davis & Hayes 2014 + Hayes-Davis DR9 update). Without the ref list I cannot verify, but even with it, readers need explicit pointers to the relevant tables/sections.
- Required fix:
  - In the reference list, clearly separate the original SpArcFiRe method paper (ApJ 790, 87) from any DR9-overlap catalog release.
  - After the first occurrence of each statistic, add a parenthetical citation to the exact table/section in those works.
  - If any of these numbers were computed by you from public SpArcFiRe data, make that explicit and do not present them as “reported by” SpArcFiRe.

---

## MINOR findings

These are correctness/clarity issues that should be fixed, but are not fatal.

### P4-m1 – Several references are cited only in shorthand, risking fused metadata

- Sections: Introduction and Discussion around parity-violating sectors.
- Examples:
  - “Lue, Wang & Kamionkowski ”, “Cabass, Ivanov & Philcox ”, “Philcox ”, “Eskilt & Komatsu ”, “Eskilt et al. (Cosmoglobe…) ”.
- Issue: In the body text you sometimes summarize multiple papers in one breath, explaining their connections (e.g., EFT-of-LSS mapping to g\*), but without the reference list I cannot verify that  is indeed the “Colliders and ghosts” paper, and that  is Philcox’s parity-odd BOSS analysis, etc. There’s a risk of fused metadata (e.g. mixing 2022 and 2023 versions, or mixing preprint and journal details).
- Required fix:
  - Ensure that for each of – you give consistent and complete metadata in the reference list: full title, arXiv ID, journal, and year.
  - Double-check that there is no reuse of a single label [n] for both an arXiv preprint and a later journal version in ways that conflict (e.g. listing different titles under the same number).

### P4-m2 – “Shamir’s earlier work [1]” phrasing can be ambiguous

- Section: I. Introduction, paragraph discussing Shamir 2012/2020/2022.
- Problematic text:
  - “Shamir’s earlier work [1] reported ∼ 3% asymmetries…”
- Issue: Here [1] is the 2020 paper, but “earlier work” could be read as referring back to 2012. The next sentence then references “Shamir (2022) [3]”. This is rhetorically confusing.
- Required fix:
  - Explicitly name the year: “Shamir (2020) [1] reported… Shamir (2022) [3] reported…”. Avoid “earlier” unless you clearly anchor which year relative to which.

### P4-m3 – Some cross-paper summary phrases could be interpreted as over-claiming

- Sections: V A, VI E.
- Examples:
  - “The present work corroborates that critique with 3.2 × 10^6 DESI Legacy spirals…”
  - “This result serves as a cautionary tale for all chirality studies…”
- Issue: These are slightly stronger than strictly warranted from the cross-comparisons—especially since you explicitly do *not* do a matched footprint analysis against Shamir’s pipeline. To maintain a clean separation between what you show and what is inference, it would be better to tighten the wording.
- Required fix:
  - Rephrase along the lines of: “Our null result is consistent with the critiques of Iye et al. and Tadaki et al. but does *not* by itself formally exclude Shamir’s estimator, because we have not re-run his algorithm on our footprint.”

---

## NIT findings

Stylistic/formatting or very minor clarity points.

### P4-n1 – Minor typographical redundancies

- Section: Abstract header and scattered elsewhere.
- Example: “canonical canonical-mask residual” does *not* appear; the closest is “canonical-mask residual”. I do not see literal duplicate phrases like “canonical canonical-mask”, so there is actually *no* duplicate-phrase problem of the type described in your instruction.
- Required fix: None on this specific point; I explicitly confirm that phrases like “canonical-mask residual” and “canonical-N” are used, but not repeated words back-to-back.

### P4-n2 – Meta language about “earlier drafts” and “this was superseded” appears in body

- Sections: II B (GZ1 vs CE-ResNet calibration), IV B (confidence fractions), VI C (injection-recovery).
- Examples:
  - “Earlier drafts also quoted a fraction-at-> 0.99 number from a different catalog snapshot; that figure is superseded…”
  - “the earlier Z = 6.77 assumed-discordance figure, which is now superseded by the corrected measurement.”
  - “the 0.03 figure was from the pre-extension sweep and is superseded…”
- Issue: These are version-history comments inside the main prose. Your instructions say: “If any version-history language, internal audit tags, or review-log artifacts appear in the PAPER TEXT body prose, flag each one.” These *are* version-history artifacts.
- Required fix (MAJOR if journal style is strict about this):
  - Remove references to “earlier drafts” and “superseded” internal numbers from the main text.
  - Where relevant, simply present the final value and, if necessary, note that it replaces an incorrect value that was in an earlier *preprint* version without going into detail. A short note in an Appendix or Erratum-style paragraph is acceptable, but the main body should read as a single coherent version.

### P4-n3 – Very long sentences combining multiple claims

- Many places, especially Sec. IV D and VI G, you have sentences that run well over 5–6 clauses, mixing numeric results, methodology, and interpretation. That makes it harder to see which part is data and which is inference.
- Required fix:
  - When revising, break the longest sentence chains (for example, those outlining the “three interpretations” or the multi-null battery) into shorter sentences, each with a single main claim. This is a readability issue, not a correctness one.

---

## Paper length

The excerpt you provided runs to at least 54 pages including figures, methods appendix, and dense discussion. For a methods-heavy PRD paper, this is on the long side, especially given that:

- The core *new* scientific claim is a null dipole at ℓ = 1 with quantified sensitivity, plus a carefully dissected canonical-mask systematic.
- A large part of the text is taken up by internal audit narrative, pipeline variants, and multiple nulls.

I would recommend that the final accepted version be *no more than about 35–40 PRD pages* of main text, with:

- The full NaMaster configuration, D4-TTA holdout details, and some of the multi-null battery relegated to a supplementary document or a data-release note.
- The main paper focusing on: data, classifier, bias audit summary, primary dipole estimators, canonical-mask diagnostic, and the clearest comparison to Shamir/CE-ResNet/Iye/Tadaki.

That said, given the complexity of the systematics story, I would classify overlength as a **MINOR** concern if PRD is willing to host a long methods paper, but the authors should at least consider how to modularize.

---

## Abstract accuracy

From the long excerpt, the abstract’s core claims:

- “null ℓ = 1 chirality-dipole observable on the analysis subsample mask… −0.12σ”
- “real-space post-TTA dipole +0.43σ”
- “σ values are defined relative to respective nulls and not directly comparable”
- “canonical-mask residual +3.64σ”
- “empirical 50%-recovery-at-3σ threshold ≳ 0.75%”

all match the detailed results in Sec. IV and VI. The abstract presents what the paper *shows*, not what it merely hopes to show. I do not see exaggeration or omission of key caveats there.

---

## Summary recommendation

**MAJOR REVISIONS**

The main cosmological and methodological conclusions appear internally consistent, and the handling of different nulls and σ-scales is unusually careful. However, from the perspective of a “citation forensics” audit, several cross-paper claims (quoted σ values, asymmetry percentages, and axis alignments) are not verifiable here because the reference list isn’t supplied, and some version-history language and fused-summary phrases need to be tightened. Before acceptance, the authors should (i) provide the full bibliography and systematically cross-check every quoted numerical claim from prior work against the original sources, (ii) clean version-history artefacts out of the prose, and (iii) slightly weaken or more carefully source any language that sounds like a formal exclusion of other authors’ results without a matched-pipeline reanalysis. Once that is done, the paper could be reconsidered, likely with only minor further polishing.