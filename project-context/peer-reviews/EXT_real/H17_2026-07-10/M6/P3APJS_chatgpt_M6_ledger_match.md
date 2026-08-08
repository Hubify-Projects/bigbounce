# ledger_match DRAFT — P3 — P3APJS_chatgpt_M6.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (20 D-ids)  |  findings parsed: 20  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | Central catalog definition (§§2.2–3; Tables 1–2): The 268,519-object “validated catalog-grade” subset is not selected by | DP3-07 | 0.40 | MATCHED |
| 2 | MAJOR | SDSS headline component (§3.3; Table 2 footnote ♡): The 77,905-object SDSS contribution is explicitly chosen to equal th | DP3-14 | 0.50 | MATCHED |
| 3 | MAJOR | DESI injection-recovery validation (§2.2; §6.4(i)): The decisive injection test does not reproduce the released catalog  | DP3-15 | 0.59 | MATCHED |
| 4 | MAJOR | DESI object provenance and reproducibility (§2.2; Data Availability): The released identifier field contains real DESI T | DP3-15 | 0.34 | MATCHED |
| 5 | MAJOR | DESI population interpreted as real astrophysical sources (§3.1; §3.3): Approximately 98.7% of DESI anomaly clusters lac | DP3-07 | 0.57 | MATCHED |
| 6 | MAJOR | Irreconcilable DESI denominator accounting (§3.1; Table 3): The reported per-class rates imply of order 3.7×10 4 anomali | DP3-07 | 0.34 | MATCHED |
| 7 | MAJOR | Claimed comparison with Liang et al. (§3.1; §6.5): Comparing 2,468 DR1 candidates with 2,685 EDR candidates and calling  | DP3-07 | 0.40 | MATCHED |
| 8 | MAJOR | Training-set representativeness and spectral preprocessing (§§2.1–2.2): A 47,000-spectrum training pool is used for 22.5 | DP3-13 | 0.13 | **UNMATCHED** |
| 9 | MAJOR | Validation does not establish catalog purity or completeness (§2.4; §6.4): Validation-loss thresholds measure reconstruc | DP3-09 | 0.21 | **UNMATCHED** |
| 10 | MAJOR | Planck catalog construction (§3.6; Table 7): The model is trained and scored on the same bank of spatially overlapping 1 | DP3-06 | 0.58 | MATCHED |
| 11 | MAJOR | NEOWISE validation (§3.8): The reported 100% recovery is guaranteed by planting sources outside a latitude mask and then | DP3-07 | 0.18 | **UNMATCHED** |
| 12 | MAJOR | Novelty claim (§4.1): Absence from 18 positional catalogs is mislabeled “genuine novelty.” It can result from blank-sky  | DP3-11 | 0.21 | **UNMATCHED** |
| 13 | MAJOR | Data-release definition is internally inconsistent (Data Availability): The manuscript says that LAMOST is excluded from | DP3-20 | 0.33 | MATCHED |
| 14 | MAJOR | Inclusion of a known failed tier (§3; §3.4; Conclusions): The 377,482-object “inclusive” result contains the LAMOST popu | DP3-20 | 0.26 | **UNMATCHED** |
| 15 | MAJOR | End-to-end provenance control (§3.5; §3.7; Data Availability): A synthetic Gaia fallback entered the production outputs, | DP3-08 | 0.40 | MATCHED |
| 16 | MAJOR | Headline scan volume (title, abstract, Tables 1–2): The manuscript gives 36.758 million, 36.93 million, and 37.292 milli | DP3-04 | 0.65 | MATCHED |
| 17 | MAJOR | Cosmological applications (§5; Appendices C and E): The f NL ​ analysis combines a 5,384-object bias sample with a 40,19 | DP3-10 | 0.17 | **UNMATCHED** |
| 18 | MINOR | Obsolete and non-catalog figures (Figs. 3, 4, and 8): Several principal figures display cross-transfer populations that  | DP3-14 | 0.22 | **UNMATCHED** |
| 19 | MINOR | Validation-summary inconsistency (Fig. 10; abstract; §6.4): Figure 10 omits the dominant DESI injection-recovery result  | DP3-02 | 0.17 | **UNMATCHED** |
| 20 | MINOR | Presentation and scope: The manuscript is highly repetitive and repeatedly foregrounds “largest,” “141×,” “73×,” and “pr | DP3-07 | 0.57 | MATCHED |

**Match rate: 12/20 = 60% MATCHED, 8 UNMATCHED.**

Exit 2 — 8 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
