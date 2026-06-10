# P3 R27conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.86.pdf` md5=31284b90 pages=26
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 149.7s

---

**Referee Report on "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies..."**

**To the Editor of Physical Review D,**

This manuscript presents a large-scale anomaly detection campaign across seven major astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply a custom autoencoder framework (BIGAE), develop a "Path-C" native-retraining protocol to address cross-survey domain shift, and use the resulting catalog for several downstream applications, including cosmological forecasts for primordial non-Gaussianity (fNL) and consistency checks of bouncing cosmology models against NANOGrav data.

The scale of the work is impressive, and the core methodological lesson regarding the necessity of native retraining (demonstrated powerfully with the LAMOST and SDSS results) is an important contribution to the field of astronomical data mining. The cosmological applications, while currently limited by statistical uncertainty, demonstrate the potential of such catalogs as a new resource for fundamental physics.

However, the manuscript in its present form falls significantly short of the standards required for publication in Physical Review D. It is plagued by the inclusion of internal review notes, version history, and project management artifacts that are entirely inappropriate for a peer-reviewed scientific paper. Furthermore, there are major issues with clarity, reproducibility, and the presentation of key results that must be addressed before the paper can be reconsidered.

Below is a detailed list of required revisions.

---

### **ESSENTIAL Revisions**

These issues must be resolved for the paper to be considered for publication.

*   **P3-E1: Removal of Internal Versioning and Review Artifacts.**
    *   **Location:** Abstract (p. 1), §IV.B (p. 12), Table IV (p. 19).
    *   **Problem:** The manuscript is littered with language that belongs in internal drafts or lab notebooks, not a final publication. This is a critical failure of professional presentation.
        *   Abstract: "an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic..."
        *   §IV.B: "(An earlier draft quoted 38,330 pixels with χ²ᵥ = 3.76; that artifact's pixel-selection and variance model could not be recovered from the committed analysis tree, and the figure is withdrawn in favor of the reproducible recompute above.)"
        *   Table IV: This entire table is an internal audit log, not a scientific table of caveats. It lists resolutions like "union-find recompute" and "ceffyl KDE chain".
    *   **Fix:** Remove every instance of such language. The paper should present the final, validated results and methods. The history of the analysis is irrelevant to the reader. Table IV must be completely removed and any scientifically relevant caveats from it must be rewritten and integrated into the main limitations section (§VI.C).

*   **P3-E2: Irreproducible eROSITA Anomaly Score Axis.**
    *   **Location:** §III.E (p. 7-8).
    *   **Problem:** The authors state that the published eROSITA anomaly score axis (`S_BigAE`) could not be reconciled with the canonical definition in Eq. (2), is non-monotone with the raw reconstruction error, and that no committed score axis reproduces the production threshold. They explicitly state: "meta-analyses that require eROSITA anomaly scores on a reproducible axis... cannot be performed from the published S_BigAE values". This is a fundamental methodological failure for this survey's tier. While the transparency is commendable, publishing a non-reproducible score axis and ranking does not meet scientific standards. The only reproducible element is the fixed membership list.
    *   **Fix:** The eROSITA tier cannot be presented as a ranked list of anomalies if the ranking axis is not reproducible. The authors must either (a) succeed in deriving a reproducible score axis and re-present the results, or (b) downgrade the eROSITA results to an unranked, un-scored collection of 298 interesting sources, and make this limitation extremely clear in the abstract and conclusions. The current presentation is unacceptable.

---

### **MAJOR Revisions**

These issues represent significant flaws in the paper's structure, clarity, and scientific presentation.

*   **P3-M1: Abstract Clarity and Bookkeeping.**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The abstract is dense and immediately bogs down in complex, confusing bookkeeping (e.g., "the recommended catalog-grade subset is ~ 269,000 unique entries (269,317 from a direct... leaving the 269,117 catalog-grade point-source subset... an earlier draft quoted...)"). This makes the top-line results nearly impossible to parse. The abstract should summarize the most important outcomes, not the tortuous path of catalog subset definition.
    *   **Fix:** Rewrite the abstract to be clear and concise. State the main unique anomaly count (378,280). State the most important catalog subset size and its definition simply. Move the detailed arithmetic of how subsets are derived into the main text. The abstract must be readable and impactful.

*   **P3-M2: Inappropriate Table Structure and Footnotes.**
    *   **Location:** Table I (p. 9).
    *   **Problem:** The main table body reports the initial, superseded cross-transfer anomaly counts, while the final, canonical native-retrained counts (the paper's primary results) are buried in extremely long and convoluted footnotes. This is backwards. The table should present the final science-ready numbers, with the diagnostic/historical numbers in the notes if necessary.
    *   **Fix:** Restructure Table I. The `N_anom` column should list the final, Path-C native-retrained anomaly counts for each survey. A separate column or a concise footnote can be used to list the initial cross-transfer counts for the before/after diagnostic. The footnotes must be drastically shortened and simplified.

*   **P3-M3: Unclear Provenance of Gaia Training Data.**
    *   **Location:** §II.B.a (p. 3).
    *   **Problem:** The authors state: "the exact 20-feature production script for the published 50K-source run was not recovered from any committed backup; its nearest committed lineage... is lineage-inferred rather than directly recovered." This is a major reproducibility issue. A core part of the analysis pipeline is not precisely known.
    *   **Fix:** The authors must either recover the exact script or provide a much more detailed justification for why the "lineage-inferred" script is a faithful substitute. The uncertainty introduced by this missing component must be quantified and discussed in the limitations section.

*   **P3-M4: Confusing Figure Captions.**
    *   **Location:** Fig 1 (p. 2), Fig 2 (p. 6), Fig 8 (p. 15).
    *   **Problem:** Several figure captions contain confusing asides, bookkeeping, or statements about the data that undermine the figure's integrity.
        *   Fig 1: "the 83 gold-tier anomalies... is distinct from the 116-object GOLD QSO-candidate confidence tier". This use of "gold" for two different, un-reconciled sets is confusing.
        *   Fig 2: "the canonical Path-C unique count of 378,280 is not a deduplication of this baseline". This is complex logic that belongs in the text, not a figure caption.
        *   Fig 8: "the burned-in 'Score' annotations are display values from that script rather than catalog-pipeline outputs". Figures in a scientific paper must display the actual data from the final analysis pipeline, not arbitrary "display values".
    *   **Fix:** Rewrite all captions to be clear, concise descriptions of what the figure shows. Remove all complex bookkeeping and disclaimers. The figures must be reproducible from the final data products. For Fig 8, the plots must be regenerated using the final, canonical catalog scores.

*   **P3-M5: "Residual Caveats" Section Structure.**
    *   **Location:** §VI.D (p. 18).
    *   **Problem:** This section reads like a point-by-point rebuttal to previous review comments or an internal checklist. It mixes genuine limitations (e.g., DESI in-sample overlap) with summaries of validation tests (e.g., injection-recovery synthesis). This is not a standard section for a scientific paper.
    *   **Fix:** Disassemble this section. Move genuine limitations and caveats into the main Limitations section (§VI.C). Move summaries of validation procedures into the Methods section (§II.D) where the protocol is described. The current structure is confusing and unprofessional.

---

### **MINOR Revisions**

These issues should be addressed to improve the paper's quality.

*   **P3-m1: Data Leak in Feature Scaling.**
    *   **Location:** §II.B.a (p. 3).
    *   **Problem:** The authors note that for eROSITA, NEOWISE, and Gaia, the feature scalers (e.g., mean/variance or median/IQR) are fit on the full sample before the train/validation split. This constitutes a minor data leak from the validation set into the training process.
    *   **Fix:** The authors have correctly disclosed this. However, they should add a sentence quantifying why this is expected to have a negligible effect on the final anomaly *ranking* (which is the quantity of interest), even if it affects the absolute MSE values.

*   **P3-m2: Heterogeneous Anomaly Thresholds.**
    *   **Location:** §II.B.b (p. 3) and Table I (p. 9).
    *   **Problem:** The study uses a mix of absolute score cuts, percentile cuts, fixed-N cuts, and a score-knee method. This makes direct comparison of anomaly *rates* across surveys (e.g., 0.87% for DESI vs. 3.38% for SDSS) potentially misleading, as the rates are functions of both the intrinsic population and the chosen thresholding method.
    *   **Fix:** Add a paragraph in the discussion (§VI) explicitly addressing this heterogeneity. The authors should clarify that cross-survey comparisons should be based on object-level analysis (cross-matches) rather than a direct comparison of the reported anomaly rates, which are not defined in a uniform way.

---

### **NITs**

*   **P3-N1: Redundant Phrasing.**
    *   **Location:** Throughout.
    *   **Problem:** Occasional redundant phrases appear, e.g., "canonical canonical-mask".
    *   **Fix:** Proofread for and remove such redundancies.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper reports on a scientifically valuable and ambitious project. The resulting anomaly catalog is a significant resource, and the methodological findings are important for future large-scale surveys. However, the manuscript is not yet in a publishable state. The inclusion of extensive internal notes, version history, and project management artifacts is unacceptable for a formal scientific publication. Combined with major issues in reproducibility (eROSITA, Gaia), clarity (abstract, captions), and presentation (Table I), the paper requires a thorough revision and professionalization. The authors must strip the manuscript of all internal commentary and restructure it to present its scientific results and methods clearly and reproducibly. Once these fundamental issues are addressed, the paper will be a strong candidate for publication.