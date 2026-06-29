# P3 RB-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=b5565d8e pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 206.6s

---

**P3-E1 (ESSENTIAL)**  
Page 1 (abstract) vs. page 2 (body): The abstract headline states “269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies”. The body immediately qualifies the 269,317 figure as the post-7-way-dedup recommended tier after removing the 200 Planck patches and applying the validated catalog-grade cut. No sentence in the abstract carries the corresponding qualifier that the headline number is *not* the raw detection count. Required fix: rewrite abstract sentence 1 to match the exact body definition and caveats.

**P3-E2 (ESSENTIAL)**  
Page 4, Eq. (2) and surrounding text: \(S(\mathbf{x})\) is defined per-survey using each survey’s own \(\mu_\text{val},\sigma_\text{val}\). The paper repeatedly places \(S>5\) thresholds from DESI, SDSS, LAMOST, etc., in the same tables/figures without the explicit qualifier “not directly comparable” at every juxtaposition. Instruction 7 violation. Required fix: insert the qualifier in every table, figure caption, and results paragraph that mixes surveys.

**P3-E3 (ESSENTIAL)**  
Page 1 and page 9 (Table I): The abstract and Table I headline claim a “multi-survey catalog of 269,317… anomalies”. The table shows that 113,342 of the LAMOST objects and 77,905 of the SDSS objects are produced by *cross-transfer* scoring from a DESI-trained model before native retraining; only the final Path-C native-retrain numbers are science-grade. The abstract does not disclose this. Required fix: abstract must state the fraction that are native-retrain vs. cross-transfer.

**P3-M1 (MAJOR)**  
Pages 2–3 and 5: The paper is 30 pages. A catalog/data-release paper whose primary deliverable is a numbered list of anomalies plus six injection-recovery tests does not justify this length in PRD. Recommended maximum: 18 pages (including all tables/figures). Required fix: condense or split into a short methods letter + data-release note.

**P3-M2 (MAJOR)**  
Page 5, §II.D and page 6: All reproducibility claims rest on GitHub links, pipeline scripts, and “committed production state” that are not frozen with a DOI or Zenodo snapshot at submission time. The Data Availability paragraph lists only a future HuggingFace DOI. Required fix: provide a permanent, version-stamped archive of every script and model weight used for the headline numbers.

**P3-M3 (MAJOR)**  
Page 7 (Fig. 2) and page 9 (Table I): The spatial map and rate table mix seven surveys whose selection functions, magnitude limits, and sky footprints differ by orders of magnitude. No effective-volume or selection-function weighting is applied before claiming “largest multi-survey anomaly search”. Required fix: either restrict claims to per-survey rates or supply a properly weighted comparison.

**P3-M4 (MAJOR)**  
Page 17, §V.A: The Fisher forecast claims a “central 9.4 % improvement” on \(\sigma(f_\text{NL})\) that disappears once the empirically measured bias \(\alpha_{jk}=0.19\pm0.65\) is inserted. The de-biased result is statistically indistinguishable from the single-tracer baseline. The abstract and introduction still advertise the multi-tracer methodology as delivering a meaningful gain. Required fix: remove or explicitly caveat the improvement claim.

**P3-N1 (MINOR)**  
Page 4, Eq. (1): MSE is written without the conventional \(1/N\) factor in some inline references; the displayed equation is correct but the surrounding prose is inconsistent. Required fix: uniform notation.

**P3-N2 (NIT)**  
Multiple figure captions contain the internal tag “Path-C” without definition on first use. Required fix: define acronym at first appearance.

**P3-E4 (ESSENTIAL)**  
Page 1 (abstract) and page 14 (Fig. 6): The 17.8 % “genuine novelty fraction” is computed on the top-1,000 DESI stratum only. The abstract presents it as a survey-wide property. Required fix: restrict the claim to the stratum on which it was measured.

**P3-E5 (ESSENTIAL)**  
Page 2 and page 5: The paper states that \(S\) values “are not directly comparable across surveys” yet still reports an aggregate “1.01 %” anomaly rate for the full 37 M sources. The aggregate rate is therefore meaningless. Required fix: remove the aggregate rate or recompute it with survey-specific effective volumes.

**P3-M5 (MAJOR)**  
Page 12, §III.H and page 13 (Fig. 5): The top NEOWISE anomaly is interpreted as “extreme W1–W2 color excess” with no quantitative SED fit or alternative hypothesis test supplied. The physical-interpretation paragraph is purely qualitative. Required fix: either drop the interpretation or supply a minimal model comparison.

**P3-E6 (ESSENTIAL)**  
Page 1 and page 24 (Table VIII): The abstract advertises a “multi-tracer” cosmological application. Table VIII shows that even the optimistic fixed-bias-prior forecast yields at most a 20 % improvement only at \(\alpha=0.50\), far outside the regime justified by the data. The abstract claim is therefore unsupported. Required fix: remove cosmological-application language from the abstract.

**Summary recommendation**  
REJECT

The manuscript is a large catalog data release whose headline numbers rely on survey-specific normalizations that are explicitly declared incomparable, whose cosmological “gain” vanishes under the authors’ own bias measurement, and whose reproducibility artifacts are not frozen at submission. These are not cosmetic issues; they are fatal to the central claims. The work belongs in a data-release journal or as a short, heavily caveated methods note, not in Physical Review D in its present form.