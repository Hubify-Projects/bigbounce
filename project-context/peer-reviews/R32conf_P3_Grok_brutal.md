# P3 R32conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.93.pdf` md5=a3504a9b pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 73.5s

---

**Referee Report**

**Paper:** Spectrally Unusual Sources at Scale… (BigAE multi-survey anomaly catalog)  
**Journal target:** Phys. Rev. D  
**Round context note (internal only):** v3.1.93 contains the TARGETTYPE-restricted recount (2,468) and the explicit ~98.7 % non-science-target statement. These statements are internally consistent with the body text on pp. 5–6 and do not contradict the retained full-stream headline numbers.

**P3-E1 (ESSENTIAL)**  
**Location:** Abstract (p. 1) + §I (p. 2)  
**Problem:** The abstract opens with the claim of “the largest-scale application of autoencoder anomaly detection across multiple astronomical archives of which we are aware.” No quantitative comparison to the prior single-survey benchmarks (Liang et al. 2023, Baron & Poznanski 2017, etc.) is supplied in the abstract or introduction; the 73× increase language later refers only to the *unrestricted* DESI stream, not to any published multi-survey catalog.  
**Required fix:** Either remove the superlative or insert a one-sentence, citable comparison (e.g., “exceeds the previous largest published catalog by factor X in unique objects after identical deduplication”).

**P3-E2 (ESSENTIAL)**  
**Location:** p. 1, first paragraph after the author block  
**Problem:** Explicit version-history language: “an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic.”  
**Required fix:** Delete all such sentences. PRD does not publish internal revision logs.

**P3-E3 (ESSENTIAL)**  
**Location:** Abstract (p. 1) and §V (p. 15)  
**Problem:** The Fisher-forecast improvement is reported as “6.1 % central-value change” (or 9.4 % in one place) while the text simultaneously states “no multi-tracer improvement at current S/N” and “the central 9.4 % improvement is a noise-driven forecast pending higher-S/N follow-up.” The abstract presents the 9.4 % figure without the decisive caveat that appears only in the body.  
**Required fix:** Abstract must state the *final calibrated result* (zero improvement, prior fixed-α value retained) or the claim must be removed.

**P3-E4 (ESSENTIAL)**  
**Location:** Table I (p. 8) and §III F (p. 11)  
**Problem:** Planck CMB tier is retained in the headline catalog (200 objects) even though the native convolutional autoencoder fails both Path-C gates (val_loss = 0.4437, injection-recovery 100 % only after 5σ planting). The table footnote acknowledges the failure but the catalog still counts the 200 patches.  
**Required fix:** Remove the 200 Planck patches from the primary catalog or re-label the table row “quarantined—methodological artifact only.”

**P3-M1 (MAJOR)**  
**Location:** §II D and all survey sections (pp. 4–11)  
**Problem:** The Path-C “native retrain” protocol is presented as the core methodological advance, yet three of the six surveys fail the 5σ injection-recovery gate and the Planck run fails the validation-loss gate. The paper therefore demonstrates that the protocol is *not* robust across the very archives it claims to unify.  
**Required fix:** Either (a) restrict the headline catalog to the three surveys that pass both gates or (b) add a prominent “limitations of the Path-C protocol” subsection that quantifies the failure rate.

**P3-M2 (MAJOR)**  
**Location:** Fig. 3 (p. 7) and §III C (p. 9)  
**Problem:** The SDSS DR18 anomaly-score distribution is shown on a log-log scale that extends to S ≈ 10¹¹; the caption states this tail is a cross-transfer artifact. No quantitative statement of how much the published SDSS catalog would shrink after the native retrain is supplied in the figure or table.  
**Required fix:** Add a second curve (or column in Table I) giving the native-retrain SDSS count at the same S > 5 threshold.

**P3-M3 (MAJOR)**  
**Location:** §IV A (p. 12) and abstract  
**Problem:** The “genuine novelty fraction” of 17.8 % is derived from a single top-1,000 subsample cross-matched against 18 catalogs. No bootstrap or jackknife uncertainty on this fraction is reported, nor is it shown that the fraction is stable when the matching radius is varied from 3″ to 7″.  
**Required fix:** Supply the radius-variation test and a binomial or Wilson interval on the 178/1,000 figure.

**P3-N1 (MINOR)**  
**Location:** Multiple figure captions (e.g., Fig. 2, Fig. 7)  
**Problem:** Mollweide projections lack explicit statement of the coordinate epoch (ICRS assumed but not written).  
**Required fix:** Add “ICRS J2000” to every all-sky map caption.

**P3-N2 (MINOR)**  
**Location:** Eq. (2) (p. 3)  
**Problem:** The canonical anomaly score S is defined with σ_val taken from the held-out 20 % split, yet the text never states whether this split is the same across all seven surveys or recomputed per survey.  
**Required fix:** One clarifying sentence.

**P3-NIT1 (NIT)**  
**Location:** Throughout  
**Problem:** Inconsistent use of “Path-C” versus “native retrain” terminology in figure captions versus body text.  
**Required fix:** Standardize.

**Summary recommendation: REJECT**

The manuscript is primarily a catalog release accompanied by an extended methodological audit that repeatedly demonstrates the fragility of the proposed pipeline (failed gates on three of six surveys, dominant training-set artifacts, zero gain in the cosmological forecast). The combination of (i) explicit internal revision history in the submitted text, (ii) headline numbers that rely on quarantined or failed runs, and (iii) an abstract whose quantitative claims are materially stronger than the final calibrated body statements places the paper below the acceptance threshold for Phys. Rev. D. A substantially shortened methods-and-lessons paper focused on the LAMOST training-bias result might be viable elsewhere; the present 28-page multi-survey catalog does not meet PRD standards in its current form.