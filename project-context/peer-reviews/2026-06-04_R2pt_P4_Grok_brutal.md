# P4 2026-06-04_R2pt — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 15.3s

---

**Referee Report for P4 (HUBIFY-2026-004)**

**Paper length**: 56 pages. PRD methods/catalog papers are typically 15–30 pages. This manuscript is grossly inflated by repetitive prose, exhaustive null-by-null tabulations, artifact-path citations, and multi-page interpretive appendices that belong in supplementary material. Required fix: condense to ≤25 pages (core methods + headline results + one focused systematics section). All other findings below are secondary to this structural failure.

**ESSENTIAL findings**

P4-E1. Section I (pp. 2–4) and abstract. The abstract states the “headline scientific result is a null ℓ=1 chirality-dipole observable… −0.12σ” while the body devotes the majority of its length to a +3.64σ canonical-mask residual and its multi-null interpretation. The abstract does not honestly represent what the paper actually proves (a systematics-attributed residual on one mask, not a clean null). Required fix: rewrite abstract to state the load-bearing result (−0.12σ on the subsample mask) and explicitly characterize the +3.64σ value as a non-primordial, systematics-attributed residual.

P4-E2. Throughout (e.g., abstract, Sec. IV C, Table II, Sec. VII). Despite the footnote that “σ values… are not directly comparable across estimators,” the manuscript repeatedly presents −0.12σ, +0.43σ, +3.64σ, +3.57σ, etc., in the same narrative without consistent qualification. This is a direct violation of the instruction on σ values from different null procedures. Required fix: either (a) report only p-values or rank statistics or (b) add an explicit, repeated disclaimer in every results paragraph and in the abstract.

P4-E3. Throughout body prose (e.g., pp. 1, 3, 5, 9, 10, 15, 18, 21, 24, 27, 35, 44). Multiple instances of internal audit tags, reproducibility-artifact paths (“pipelines/p2_chirality/…”, “paper4-v1.0.153”, “companion artifact … .json”, “SHA-256 stamped”, version strings, “queued”, “retracted”, “superseded”), and review-log language remain in the submitted text. Required fix: remove every such string; none may appear in a journal submission.

P4-E4. Sec. III A (p. 6) and Sec. IV D. The analysis hierarchy was “fixed at v1.0.76… after the first round of catalogue results.” This post-hoc declaration is unacceptable for a methods paper claiming a null result. Required fix: either remove all language implying post-hoc choice or provide a time-stamped pre-registration document.

**MAJOR findings**

P4-M1. Abstract and Sec. I. Claims of “first”, “new”, “advances beyond CE-ResNet in three respects” are not honest given the literature (Iye et al. 2021, Tadaki et al. 2020, Jia et al. 2023). The paper is a larger-sample null with a different classifier; it does not demonstrate a qualitatively new observable or method. Required fix: excise all novelty language; describe the work as “an independent, larger-sample test using a ViT+TTA pipeline.”

P4-M2. Sec. IV C and Sec. VI G. The +3.64σ canonical-mask residual is interpreted via a three-discriminator framework that is presented as decisive, yet the bootstrap injection test explicitly shows that a real 1.7% dipole would also be consistent with the bootstrap null. The manuscript therefore overclaims the strength of the evidence against a primordial dipole. Required fix: state clearly that interpretation (i) is disfavored but not formally excluded by the current tests.

P4-M3. Sec. VI C. The statistical-only Fisher floor (~0.29% full-amplitude at 3σ) is repeatedly contrasted with the empirical 0.75% threshold without acknowledging that the 0.2% figure quoted in earlier prose referred to the half-modulation A/2. The sensitivity claim is therefore internally inconsistent. Required fix: adopt a single, explicitly defined convention (full amplitude A) and recompute all quoted floors.

P4-M4. Sec. V A. The comparison with Shamir (2012, 2020, 2022) is framed as amplitude inconsistency “under the present pipeline,” yet the text repeatedly states that a matched-footprint Ganalyzer reanalysis was not performed. This is a material limitation that must be elevated to a primary caveat, not buried in a parenthetical.

**MINOR findings**

P4-m1. Table I caption and multiple figure captions contain duplicate or truncated phrases (“canonical canonical-mask”, “Nspiral = 3,201,160 (canonical equivariant total; see Sec. IV A)”). Required fix: proofread all tables and captions for exact duplication.

P4-m2. Sec. II B and Sec. III E contain long parenthetical asides on McNemar statistics, Cohen’s κ, and D4 hold-out retraction that interrupt the scientific narrative. Required fix: move to an appendix or shorten to one sentence.

P4-m3. Multiple sections cite companion JSON artifacts as the “canonical record.” This is not acceptable in a journal article. Required fix: move all such references to a single Data Availability statement.

**NIT findings**

P4-n1. Inconsistent use of “canonical” (sometimes the fsky = 0.49005 mask, sometimes the Nspiral = 3,201,160 count). Standardize terminology.

P4-n2. Several figure captions still contain legacy snapshot values (e.g., “older snapshot value 2.75σ”). Remove all superseded numbers.

**Summary recommendation**

**REJECT**

The manuscript is 56 pages of methods/catalog material that should occupy ≤25 pages. It contains pervasive internal audit tags, version-history language, and reproducibility-artifact citations that render it unsuitable for journal submission. The abstract misrepresents the central result, σ values from incommensurate nulls are presented without consistent qualification, and the analysis hierarchy was declared post-hoc. These are not cosmetic issues; they violate PRD standards for clarity, reproducibility, and honest reporting. A drastically shortened, journal-clean resubmission that focuses exclusively on the −0.12σ subsample-mask null and the quantified monopole-mask leakage channel could be reconsidered, but the present document cannot.