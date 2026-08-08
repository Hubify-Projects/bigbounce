# EXTDB2 P3 ChatGPT — chat: https://chatgpt.com/c/6a40ea1a-5318-83e8-91a6-c942129721cd

Provider: ChatGPT (Instant tier)
PDF md5: d3d662cb8d0c737032580465397911f2
Harvested: 2026-06-28

---

Referee Report — Paper P3
Recommendation: MAJOR REVISIONS

The paper is ambitious and unusually transparent, but it is not yet ready for acceptance at MNRAS/PRD/JCAP level. The major issue is not lack of effort; it is that the headline catalog/result framing remains stronger than the validated science-grade subset supports. Several components are explicitly exploratory, some score axes are non-reproducible, and major cosmological applications are forecast-level or illustrative rather than demonstrated.

BLOCKERS

1. Headline catalog size overstates validated catalog-grade content. The abstract leads with 378,280 total and 269,317 recommended-tier objects, but the validated catalog-grade subset is only given as a conservative lower bound, ≥268,519 unique, with Gaia/eROSITA exploratory and LAMOST excluded. This is disclosed, but the headline still encourages readers to treat heterogeneous tiers as one catalog. Fix: title/abstract should foreground "≥268,519 validated catalog-grade" and clearly demote 378,280 to "total including exploratory/methodological tiers."

2. eROSITA score axis is non-reproducible. The paper states that the eROSITA production score threshold cannot be reproduced by any committed score axis and the tier is membership-list-only. This is a serious reproducibility limitation. Fix: either remove eROSITA from recommended-tier language or publish only as an explicitly separate exploratory appendix with no score-based downstream use.

3. DESI catalog dominated by non-primary science spectra. The DESI headline is 195,829 anomalies, but the science-class recount finds only 2,468 science-target anomaly clusters and ~98.7% on non-primary/filler/sky spectra. The paper discloses this, but still uses the full-stream DESI count for scale claims. Fix: make the science-target recount the primary DESI science result.

MAJORS

1. No DESI injection-recovery test. DESI is the anchor survey, but its validation rests on Jaccard/OOD/visual checks rather than injection-recovery. Those are useful but not equivalent to detector sensitivity.

2. LAMOST retained in total despite failing the relevant scientific gate. LAMOST is correctly described as a training-bias lesson, but its 113,342 objects still inflate the total Path-C catalog.

3. Threshold policy is heterogeneous and partly fixed-count. DESI uses S>5, SDSS uses a fixed-size continuity slice, LAMOST top-1%, Planck/Gaia/NEOWISE top-1%, eROSITA top-298. This makes aggregate "rate" and "catalog size" difficult to interpret physically.

4. Cosmology section is too prominent for the evidential strength. The fNL improvement is explicitly consistent with zero; NANOGrav Bayes factor is only against an idealized SMBHB reference. These are interesting applications, but should not share headline status with the catalog.

5. Data/code release is promised, not yet citable/frozen. A top-journal catalog paper needs a DOI or stable release at submission, especially given the reliance on many artifact JSONs and recovered scripts.

MINORS

1. The abstract is overlong and contains too many caveats for a reader to parse reliably.
2. The use of "largest" is acceptable only with the existing caveats, but should be less promotional.
3. Figure captions are unusually dense and sometimes function as methods sections.
4. Several "PASS/FAIL" gates are heuristic; this should be stated earlier.
5. "SIMBAD-unmatched" should be visually and textually deprioritized relative to the 17.8% genuine novelty estimate.

Strengths

1. Exceptional transparency about failures, artifacts, score-axis problems, and tier validity.
2. Strong methodological contribution: the LAMOST failure is a valuable warning for large-scale unsupervised anomaly detection.
3. Useful multi-survey architecture and deduplication framework.
4. DESI/SDSS cross-survey examples are compelling follow-up targets.
5. The paper provides many quantitative robustness checks rather than hiding weaknesses.

Bottom line: publishable after substantial reframing and reproducibility tightening, but not acceptable in the current headline form.
