# P4 2026-06-04_1920pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 93.8s

---

# Referee Report on HUBIFY-2026-004

## Summary of the Paper
This paper presents a detailed analysis of galaxy chirality using a new catalog of 3.2 million spiral galaxies derived from 8.47 million sources in the DESI Legacy Imaging Surveys. The authors employ a Vision Transformer (ViT) classifier and use Test-Time Averaging (TTA) to enforce flip-equivariance, a key technique for mitigating systematic biases. The primary scientific result is a null detection of a large-scale angular dipole (`ℓ=1`) in the galaxy chirality field, with the two main estimators yielding significances of +0.43σ (real-space) and -0.12σ (spherical harmonic space).

The paper also transparently reports and investigates a statistically significant (`+3.64σ`) residual found on a specific "canonical" survey mask. Through an extensive "multi-null battery" of tests—including analysis of the power spectrum shape, cross-correlation with galaxy density, and behavior under data quality cuts—the authors build a compelling case that this residual is not a primordial cosmological signal but rather a coherent systematic correlated with survey depth and imaging properties. The paper provides a detailed theoretical discussion correctly distinguishing the parity-even nature of the dipole observable (an isotropy test) from parity-odd observables (a direct parity violation test). The work concludes by placing a stringent upper bound on any isotropy-breaking axial-vector signal in the late-universe morphology channel.

## General Comments
The work presented in this manuscript is of exceptionally high quality. The analysis is remarkably thorough, demonstrating a deep understanding of the potential systematic pitfalls in this type of measurement. The authors' approach of transparently reporting a significant-looking residual and then systematically demonstrating its instrumental origin is a model of good scientific practice. The distinction between parity-even and parity-odd observables is handled with the precision required for a theoretical physics journal. The efforts toward reproducibility, including the public release of the catalog, model, and analysis scripts, are commendable.

The scientific conclusion—a null result for the chirality dipole—is robustly supported by multiple, complementary estimators that are designed to be insensitive to the primary systematic channels. The investigation of the canonical-mask residual is a valuable contribution in its own right, serving as a powerful case study in survey systematics.

My primary concern is not with the scientific content, but with the presentation. At 56 pages, the paper is excessively long for a PRD article, even for a detailed methods/catalog paper. The narrative is dense and highly repetitive, with key arguments and numerical results reiterated in the abstract, introduction, results, discussion, and conclusions. This structure makes the paper difficult to digest and obscures the main logical flow. The paper would be significantly improved by a major restructuring to a more standard journal format, with a concise main text and detailed supporting information moved to appendices.

## Findings

### ESSENTIAL

**P4-E1: Paper Length and Structure (General)**
- **Problem:** The manuscript, at 56 pages, is far too long for a standard PRD publication. The current structure leads to significant repetition of the core arguments and numerical results across multiple sections (e.g., the discussion of the `+3.64σ` residual and its interpretation is repeated at least four times). The "Discussion" section (VI), in particular, is largely a narrative re-statement of the "Results" section (IV). This format is more appropriate for a thesis or a technical monograph than a journal article.
- **Fix:** The paper must be substantially restructured and shortened to a maximum of 20-25 pages for the main text.
    1.  The main text should focus on the primary scientific result: the null dipole measurement. It should present the data, the core methodology (TTA), the primary null results (+0.43σ and -0.12σ), and the final sensitivity/falsification criterion.
    2.  The detailed investigation of the `+3.64σ` canonical-mask residual, while scientifically valuable, is a secondary analysis of a systematic effect. The main text should summarize the finding and the conclusion that it is a systematic, but the extensive multi-null battery, cross-spectrum analysis, joint-nuisance model fits, and signal-hunt diagnostics should be moved to one or more appendices.
    3.  The "Discussion" section should be heavily condensed. It should not simply repeat the results but should focus on the broader implications, the comparison to prior work, and the theoretical context (as in Sec. VI.G). Much of the content in Sec. VI.A-VI.F is a detailed re-explanation of results already presented and can be drastically shortened or integrated elsewhere.
    4.  The detailed derivation of the Fisher sensitivity floor (Sec. VI.C) is standard and should be moved to an appendix.

### MAJOR

**P4-M1: Overly Dense and Repetitive Prose (General)**
- **Problem:** The paper is filled with long, compound sentences packed with numerical values, cross-references to other sections, and parenthetical clauses. This makes the text very difficult to read. As noted in P4-E1, the same complex arguments are repeated in multiple sections, making the reader navigate the same dense thicket of information several times. For example, the list of three discriminators against the "real cosmological dipole" interpretation appears in the abstract, on page 4, page 18, and page 36.
- **Fix:** As part of the restructuring in P4-E1, the prose should be streamlined.
    1.  Present a result or argument once, clearly, in the appropriate section. Use cross-references to point back to it, but do not repeat the entire argument.
    2.  Break up long sentences. Move some numerical values and detailed specifications from the main prose into tables or figure captions.
    3.  The abstract should be a concise summary. The introduction should set the stage. The methods should describe the "how". The results should present the "what". The discussion/conclusion should explain "what it means". The current draft blurs these lines significantly.

### MINOR

**P4-m1: Theoretical Scoping of the Falsification Criterion (Abstract, p.1)**
- **Problem:** The abstract states: "A like-for-like matched-footprint Ganalyzer reanalysis under Shamir’s pipeline + cuts is required for a likelihood-level exclusion under his estimator; we do not perform that reanalysis here." This is a correct and important caveat. However, the falsification criterion later in the abstract ("Detection of a chirality dipole at σ > 5... would falsify the present null") does not carry a similar caveat regarding the estimator. While a `>5σ` detection in LSST would be compelling regardless of the pipeline, for formal falsification, it would need to be shown that the new detection is not subject to a new class of systematics specific to that pipeline.
- **Fix:** The statement is acceptable as a practical criterion, but for theoretical precision, it could be slightly rephrased to acknowledge this subtlety. For example: "...would falsify the present null, *pending a rigorous systematics analysis of the new detection*." This is a minor point, as the current wording is common practice.

**P4-m2: Terminology for `+3.64σ` Residual (Abstract, p.1; Sec. VII.b, p.46)**
- **Problem:** The abstract refers to the `+3.64σ` as the "post-MASTER canonical-mask direct-MC residual". Later, on page 46, it is clarified that this is a "moment-z" value and the empirical-rank p-value is `p_MC = 0.030` (which is `~2.2σ` two-sided). While the paper is transparent about this distinction, repeatedly leading with the `+3.64σ` "moment-z" value could be misleading, as it implies a Gaussian tail probability that the paper itself states is not validated.
- **Fix:** The authors should consider leading with the more robust empirical-rank significance when first introducing this diagnostic result. For example: "The post-MASTER canonical-mask direct-MC residual has an empirical-rank significance of p=0.030 (moment-z of +3.64σ)...". This would more accurately reflect the statistical evidence from the outset.

### NIT

**P4-N1: Citation of `paper4-v1.0.152` (Page 2)**
- **Problem:** The first sentence on page 2 states: "reproducibility scripts are publicly released under the immutable release tag paper4-v1.0.152." This is a self-reference to the paper's own versioning system. While useful for reproducibility, it's unconventional for a journal publication.
- **Fix:** This information is better placed in the Data Availability section or an appendix. The main text should simply state that scripts are publicly available and refer the reader to the appropriate section for the specific version tag.

---

## Summary Recommendation

**MAJOR REVISIONS**

This is an excellent scientific paper containing a rigorous and important null result in a field where positive claims have been controversial. The analysis of systematics is exemplary. However, the paper in its current form is not suitable for publication in PRD due to its excessive length and repetitive structure. The scientific content is strong enough to warrant publication, but only after a significant restructuring to improve clarity and conciseness. The authors should follow the recommendations in finding P4-E1 to create a focused main article, moving the extensive but secondary diagnostic details into appendices. If the authors can successfully condense and restructure the manuscript, it will be a valuable and impactful contribution to the literature.