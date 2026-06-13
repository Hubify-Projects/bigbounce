# P4 R37conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v182.pdf` md5=d3785514 pages=23
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 29.3s

---

I cannot complete the requested citation-forensics audit from the material provided because I do **not** have the rendered PDF, figure images, or live web search results for the paper’s references. The only “search results” included are accessibility/tooling pages unrelated to cosmology, so I cannot verify arXiv IDs, DOI metadata, titles, authors, or venue accuracy against arXiv/NASA ADS as requested.

What I *can* do from the pasted paper text is flag a few **internal textual issues** that are visible without external lookup:

- **Potential internal inconsistency in the bibliography and references section**
  - The reference list is truncated in the provided text at item , and item  is cut off mid-entry. This prevents verification of the full bibliography and is not acceptable for a complete audit.

- **Potential duplicate / inconsistent terminology**
  - The manuscript alternates between “MASTER”, “pseudo-Cℓ”, “pre-MASTER”, “post-MASTER”, and “single-mode” in ways that require very careful cross-checking. Some of these are explicitly qualified, but the text is dense enough that a standalone reader may still struggle to determine which estimator is primary in each sentence.
  - The paper also mixes “fsky”, “fsky eff”, “Nall ≥ 1 footprint”, “canonical mask”, and “apodized footprint” across multiple tables. This is not automatically wrong, but it is a high-risk area for bookkeeping errors.

- **Potential notation / dimensionality concern**
  - The equation \(A_p = (N^{(p)}_{CW} - N^{(p)}_{CCW})/(N^{(p)}_{CW} + N^{(p)}_{CCW})\) is dimensionless and fine, but the text repeatedly interprets values in “Ap units”, “asymmetry-A units”, and “fCW-deviation units” in a way that could confuse a referee unless the mapping is kept perfectly consistent everywhere.

- **Potential self-contradiction risk around significance conventions**
  - The manuscript repeatedly states that different \(\sigma\) values are “not directly comparable,” which is good, but it also places them side by side in the abstract and results. Under your instruction set, any juxtaposition of nulls without explicit non-comparability language would be a serious issue; from the pasted text, this is handled in some places but would need line-by-line checking in the actual PDF.

- **Potential provenance / release-state ambiguity**
  - The Data Availability section says a Zenodo DOI “will accompany the journal submission” and that the DOI “has not yet been minted.” For a PRD submission, that is a serious provenance weakness unless the editorial policy allows a non-final release-state exception.

- **Potential over-claiming in the abstract**
  - The abstract is heavily interpretive and mixes primary results with systematics diagnostics. It claims a “null real-space chirality dipole” while also emphasizing several non-null harmonic diagnostics. That is defensible only if the body truly establishes the harmonic terms as systematics and the real-space estimator as the primary science result. This needs a full-body consistency check.

Because I cannot verify the bibliography or recompute the quoted statistics against the actual rendered tables/figures, I cannot responsibly provide the full referee report you requested.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript may well be salvageable, but on the evidence available here I cannot certify the bibliography, statistics, or provenance claims at PRD level. The paper also appears to rely on a highly intricate estimator hierarchy and a dense provenance story that will require exact internal consistency, explicit separation of comparable vs non-comparable nulls, and a fully frozen release artifact before it can meet the journal’s standard.