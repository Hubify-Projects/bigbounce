# ledger_match DRAFT — P3 — P3APJS_chatgpt_M10.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (20 D-ids)  |  findings parsed: 22  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | §3.1, Table 3, and the headline “268,319 point-source anomalies”: The dominant DESI component is not demonstrated to be  | DP3-07 | 0.81 | MATCHED |
| 2 | MAJOR | §2.2 versus §3.3 and §6.4(i), DESI identifier provenance: The manuscript states that only 26,218 released DESI rows cont | DP3-05 | 0.72 | MATCHED |
| 3 | MAJOR | Table 3, DESI science-target reconciliation: The reported GALAXY and QSO rates imply roughly 37,000 anomalies in the val | DP3-07 | 0.46 | MATCHED |
| 4 | MAJOR | §2.2 and §6.4(i), claimed held-out DESI validation: The five fold models each score the full 47,000-spectrum pool, meani | DP3-01 | 0.20 | **UNMATCHED** |
| 5 | MAJOR | §6.4(i), DESI injection-recovery: The plants are inserted into the “cleanest 5%” substrate and evaluated against a tail- | DP3-02 | 0.17 | **UNMATCHED** |
| 6 | MAJOR | §3.1 and §6.4(i), visual artifact bound: The inference from 0 visually flagged objects among the top 200 to a ≤1.5% arti | DP3-06 | 0.36 | MATCHED |
| 7 | MAJOR | §2.2, §3.1, and §6.3, reconstruction statistic: The unweighted MSE ignores the supplied per-pixel uncertainties, bad-pix | DP3-07 | 0.41 | MATCHED |
| 8 | MAJOR | §3.3 and Table 2, SDSS selection: The 77,905-object SDSS tier is chosen solely to preserve the size of the obsolete cros | DP3-14 | 0.61 | MATCHED |
| 9 | MAJOR | §3.8, NEOWISE validation: NEOWISE is included in the validated tier even though its only gate places synthetic positions | DP3-01 | 0.13 | **UNMATCHED** |
| 10 | MAJOR | §3.6 and Table 7, Planck patch independence: The top 200 are selected from 200,000 ten-degree patches drawn from one sky | DP3-06 | 0.58 | MATCHED |
| 11 | MAJOR | §3.6, Planck held-out statistic and injection test: The binomial calculation for 48 validation-split patches assumes ind | DP3-15 | 0.16 | **UNMATCHED** |
| 12 | MAJOR | Title, abstract, Tables 1–2, and the central aggregate count: The catalog unions non-equivalent units—individual spectra | DP3-04 | 0.34 | MATCHED |
| 13 | MAJOR | §4.1, “17.8% genuine novelty”: Absence from 18 catalogs does not establish genuine novelty. This is especially serious b | DP3-07 | 0.24 | **UNMATCHED** |
| 14 | MAJOR | §3.1 and §6.5, “like-for-like” comparison with Liang et al.: The 2,468 count is drawn from all primary DESI classes over | DP3-07 | 0.34 | MATCHED |
| 15 | MAJOR | §3.5, §3.7, and Data Availability, release integrity: The release description is internally inconsistent. The 377,482 to | DP3-20 | 0.33 | MATCHED |
| 16 | MAJOR | End-to-end provenance: The irreproducible eROSITA score axis, synthetic Gaia fallback, loss of the DESI production input | DP3-08 | 0.50 | MATCHED |
| 17 | MAJOR | §4.3, cross-survey associations: The claim that 637 multi-survey clusters are genuine detections at more than 60 times t | DP3-11 | 0.14 | **UNMATCHED** |
| 18 | MAJOR | §5, f NL ​ application: An angular clustering amplitude for a photometric candidate sample without a measured redshift d | DP3-10 | 0.17 | **UNMATCHED** |
| 19 | MAJOR | §5.1, NANOGrav application: This analysis does not use the anomaly catalog and provides no evidence for the catalog’s ce | DP3-10 | 0.08 | **UNMATCHED** |
| 20 | MINOR | Figures 2–4, 8, and 10: These figures prominently display obsolete cross-transfer results, quarantined ACT data, the rem | DP3-14 | 0.22 | **UNMATCHED** |
| 21 | MINOR | Terminology throughout: “Five sigma,” “validated,” “real,” “genuine novelty,” “detection,” “point source,” and “catalog  | DP3-11 | 0.21 | **UNMATCHED** |
| 22 | MINOR | Organization: The manuscript repeatedly re-litigates count reconciliation, exclusions, and caveats in the abstract, intr | DP3-05 | 0.25 | **UNMATCHED** |

**Match rate: 11/22 = 50% MATCHED, 11 UNMATCHED.**

Exit 2 — 11 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
