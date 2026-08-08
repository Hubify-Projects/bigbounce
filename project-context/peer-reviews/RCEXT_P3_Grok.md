# RCEXT P3 Grok — chat: https://grok.com/c/cc93867b-c37d-421f-a4b2-87e73fe4b021
VERDICT: MAJOR REVISIONS

Provider: Grok (Expert)
PDF: RCEXT_P3.pdf (md5: f6b8d9a5e16fc5f4f3301433c9c556dc)
Harvested: 2026-06-29

---

Recommendation: MAJOR REVISIONS

The work delivers a genuinely large-scale, multi-archive anomaly catalog (37.3 M sources processed) with a transparent Path-C native-retrain protocol that diagnoses and mitigates cross-transfer failures. The honesty about limitations (LAMOST training bias, uneven validation gates, exploratory components) and the careful like-for-like science-target recount for DESI are real strengths. However, the paper does not yet meet the high bar for a top-journal data/methods release in two critical respects: (1) reproducibility of the eROSITA tier, and (2) precise, unambiguous tier definitions and headline framing that prevent any risk of readers quoting the more-favorable numbers as fully validated catalog-grade yield.

BLOCKERS (must be resolved for acceptance)

eROSITA tier — irreproducible selection axis (severe): The per-object SBigAE scores are explicitly non-reproducible on any of 16 tested monotone rescalings of the committed raw artifact; the production threshold (0.259) and even the rank-ordering of the top-5 objects cannot be recovered. Required action: Either (a) remove eROSITA entirely from the recommended tier and treat it strictly as an exploratory appendix, or (b) provide a fully reproducible alternative selection. A membership list alone is acceptable only if it is the sole canonical product and is clearly labeled as such. The current framing ("explicit exploratory addendum") is insufficient when the objects still contribute to the headline 269k recommended-tier count.

Tier nomenclature and headline framing (severe): The title, secondary total figures, and some internal references still headline the larger 269,317 recommended-tier number without an immediate, crystal-clear definition of exactly what the extra ~800 objects are and why they are included. Required action: In the abstract and first paragraph, explicitly state the exact composition of (i) the validated catalog-grade subset of ≥268,519 unique anomalies from the four surveys that pass the relevant gate (DESI, SDSS, Planck, NEOWISE), and (ii) the recommended tier of 269,317 that adds the two explicitly flagged exploratory components.

MAJORS

Validation protocol heterogeneity: Gates are survey-specific (5-fold + OOD Jaccard for DESI; 5σ injection-recovery for SDSS/Planck; masking-geometry QA for NEOWISE; explicit FAIL for LAMOST/Gaia/eROSITA). A top journal requires a concise, unified justification of why these disparate tests are treated as commensurate for the "validated catalog-grade" designation.

eROSITA and Gaia exploratory status — boundary with recommended tier: Including objects that fail the 5σ injection-recovery gate (1.2% and 5.2% recovery) and, for Gaia, show only 41% IsolationForest cross-validation stability, dilutes the catalog-grade claim. Consider moving both to a clearly separated "Exploratory Addendum Catalog."

DESI full-stream vs. science-target scope: Every occurrence of the large nominal multipliers (∼141×, ∼73×) must be immediately followed by the like-for-like science-target comparison, enforcing the same discipline as the abstract throughout.

Genuine novelty fraction (17.8%): Clearly state that it is a single-stratum point estimate on the DESI top-1,000 score slice only, not a survey-wide or catalog-wide rate.

MINORS

Table I footnotes and long figure captions are extremely dense; move technical detail to a short appendix.
The spatial uniformity χ² = 15.7 result merits de-emphasis or movement to supplementary material.
ACT DR6 quarantining merits a one-sentence main-text summary of the failure mode.
Confirm in the final version that the companion repository will contain the exact committed raw-score artifact for eROSITA, the union-find deduplication code, and the CDS X-Match query specification.

Strengths

Methodological transparency and diagnostic power: The Path-C native-retrain protocol, explicit diagnosis of cross-transfer failures, and per-survey gate documentation set a high standard for unsupervised ML on heterogeneous archives. The ~6500× SDSS rate compression after native retraining is a particularly powerful internal consistency check.

Careful scope definition and novelty assessment: Distinguishing full-instrument-stream vs. science-target yields, performing the deeper CDS X-Match for a genuine 17.8% novelty fraction, and providing per-object validity flags are exactly the practices that prevent over-claiming in anomaly catalog papers.

Cautious cosmological interpretation: The fNL multi-tracer forecast properly propagates the large empirical uncertainty on αjk (0.19 ± 0.65, consistent with zero at 0.29σ) and explicitly states no significant improvement or detection is claimed. The NANOGrav consistency check includes the necessary environmental-SMBHB caveat. This is model-auditing done correctly.

Scale with documented limitations: Processing 37.3 M sources across seven archives with a single framework, 7-way 5″ deduplication with FoF audit, and public release of catalog + weights + scripts is a substantial technical contribution.

Public-data ethos: The commitment to release the full catalog, model weights, reproducibility scripts, and companion repository aligns with top-journal expectations for data products.

Summary: This is a mature, large-scale data release with unusually honest documentation of systematics and failure modes. After the two blockers and the major framing/validation-protocol items are addressed, the paper would be a strong candidate for publication in MNRAS. I recommend Major Revisions.
