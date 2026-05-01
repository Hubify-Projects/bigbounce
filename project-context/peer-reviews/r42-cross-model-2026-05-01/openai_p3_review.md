---
model: gpt-5
paper: p3 — Anomaly Catalog — 8-survey 37.3M sources, 319,443 anomalies
pdf: /Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf
date: 2026-05-01
input_tokens: 51327
output_tokens: 7953
total_tokens: 59280
reviewer: openai (cross-model adversarial)
---
## BLOCKERs
1) Anomaly-score definition is internally inconsistent and unit-confused, undermining all thresholded counts (e.g., S > 5). Evidence: Eq. (1) in §II B defines S as the raw per-element MSE; the Fig. 4 caption explicitly redefines S as a z-scored quantity, S = (MSE − μval)/σval; §II B (in-sample/OOD paragraph) further states “S > 5 … corresponds to MSE ∼ 0.143 in the rescaled z-units,” mixing raw MSE and z-units. eROSITA (§III E, Table III) lists “scores” 4,424–34,182 while §III E defines the selection at S > 0.259. Fix: Choose one canonical definition of S, state it once with a precise equation, and revise all figures/tables/text to use that definition consistently. Provide the explicit μval, σval per survey and a mapping between raw MSE and the reported S. Recompute every thresholded count (DESI S > 5, SDSS native, eROSITA S-knee, etc.) under the consistent definition.

2) Headline/catalog size is inconsistent between title/abstract and the main text; the paper advertises 319,443 anomalies while the canonical result is 378,280 unique objects. Evidence: Title and Abstract first sentence emphasize “319,443 anomalies,” which the paper later calls the pre–Path-C cross-transfer baseline (§I, §III, Table I caption/footnotes), whereas the stated “primary result” is 378,280 unique objects after Path-C native retrains and 7-way 5″ dedup (§I, Abstract; Table I “Path-C unique (primary)”). Fix: Make the title and abstract reflect the canonical Path-C result (378,280 unique objects; 388,493 survey-level detections across non-quarantined surveys), and demote 319,443 to “baseline before native retraining” everywhere.

3) The CMB native-retrain violates the stated validation-loss gate but is retained anyway without amending the gate criterion. Evidence: §II D, Step 1 sets “Training-gate: validation loss ≤ 0.30”; §III F reports the Planck native CAE val loss = 0.4437 (fail) but declares the gate “PASS” via injection-recovery. Table I footnote repeats val loss 0.4437 and still treats Planck as retained. Fix: Either (a) change the formal gate to a two-part criterion where injection-recovery can override validation MSE, and apply it consistently across all surveys; or (b) retrain the Planck CAE to meet the ≤ 0.30 gate, or justify with formal cross-validation that 0.4437 is acceptable on this domain and revise the gate threshold for CMB with quantitative support.

4) eROSITA scoring is irreconcilable as written (three incompatible score scales). Evidence: §III E defines the selection as BigAE MSE S > 0.259 (top 0.03%); Table I repeats this; but Table III lists “Scores” of 4,424–34,182 for the top anomalies. §VI D(v) then discusses IsolationForest on a 16-d AE latent for eROSITA cross-validation. It is impossible to tell what “score” produced the catalog or Table III. Fix: Specify the exact detector used for the published eROSITA catalog (BigAE-MSE vs IF), define its score scale, and replace Table III with scores on that same scale. If Table III used a different metric, explicitly say so and provide both metrics per object or remove the conflicting table.

5) Cosmological forecast (σ(fNL)) is not reproducible and lacks essential assumptions/noise model; as written it is not publishable in PRD. Evidence: §V and Appendix C claim a Fisher forecast (7 bins, 5-tracer configuration) yielding σ(fNL) = 8.43 (6.1% improvement) but give no explicit window functions, volumes, k-ranges, bias models, shot-noise terms per tracer, or priors. The “linear scaling with α” in Table VI is asserted without showing the base Fisher matrix elements or the full covariance. Fix: Provide the full Fisher formalism (equations and inputs), survey volumes/redshift binning, P(k) modeling, bias and number-density assumptions for each tracer, shot-noise terms, and priors; release the forecasting code or a detailed supplementary with all matrices. Alternatively, remove the σ(fNL) forecast and confine the paper to the catalog.

6) Title claims “37.3 Million Spectra” while the catalog includes non-spectroscopic sources and CMB map patches; this is materially misleading. Evidence: Table I and §I/§III include eROSITA (X-ray catalog features), Gaia (variability+astrometry), NEOWISE (IR photometry), and Planck CMB patches (images), none of which are spectra; §I, abstract, and title repeatedly say “from 37.3 million spectra.” Fix: Change the title/abstract to “from 37.3 million sources” (or “sources and map patches”), and clearly stratify point sources vs CMB map patches (you already provide the 378,080 vs +200 Planck split in Table I footnote).

## MAJOR
1) DESI anomaly counts are computed with in-sample leakage; the OOD check does not validate ranking stability on the full catalog. Evidence: §II B admits the 22.5M-scored DESI catalog includes the 47k training spectra; the 5-fold CV is run only on the 47k pool (not the 22.5M) and reports fold val losses 0.76–4.91 (not converged), and no out-of-sample ranking stability on the full dataset; the “100k OOD” paragraph reports only distributional shifts but not overlap/ranking agreement. Fix: Score a large, fully held-out DESI subset (e.g., ≥1M random DR1 spectra not used in training/validation) and report top-1% Jaccard overlap between the production model’s anomalies and a model trained without any exposure to those 1M spectra. Alternatively, withhold a random sky region and repeat.

2) SDSS native re-score omits 16.3% of DR18 and does not demonstrate that missing plates are uncorrelated with anomaly density. Evidence: §III C: 1,925,279 of 2.30M spectra were scored; 376,157 (16.3%) “were not available … predominantly from SDSS-III ancillary programs,” with only a verbal claim that plate distribution does not correlate with anomaly-dense regions. Fix: Provide a sky map of missing vs scored plates and a quantitative test (e.g., compare anomaly density near plate edges vs interior; permutation test) demonstrating that omissions do not bias the anomaly rate. Otherwise, re-run with a complete local mirror or adjust claims to the scored subset only.

3) Injection–recovery “σ” is ill-defined across surveys and plants; results cannot be interpreted. Evidence: §II D Step 5 defines amplitudes as multiples of “per-spectrum σ” with no definition of how σ is computed on normalized, binned spectra; for Gaia/eROSITA the “σ” concept further morphs into subspace displacements and random latent directions (§VI D(v)). Reported 5σ gates thus mix incomparable notions of noise. Fix: Define σ precisely per survey (per-pixel flux error propagated to 496 bins? per-feature uncertainty? robust MAD?), and report both amplitude in physical units and effect size in the model’s native scale. Provide plots for multiple plant morphologies with consistent σ definitions.

4) Planck×ACT “null cross-correlation” is asserted without a statistic or significance. Evidence: §IV D declares a null result but provides no cross-power spectrum, correlation function, or Monte Carlo null with p-value. Fix: Compute an explicit cross-correlation statistic (e.g., patch-centroid two-point cross-correlation vs isotropic null, or cross-power of anomaly density maps with mask/coverage corrections) and report the significance. If infeasible, remove the claim.

5) “Native-trained novelty rates” are oversold; only a DESI top-1,000 slice has a quantified archival novelty fraction. Evidence: §IV A reports 17.8% novelty for DESI top-1,000 and 100% archival IDs for 20-object spot checks in SDSS/eROSITA/NEOWISE/Gaia; Table I and the title phrase imply broader novelty rates. Fix: Limit all “novelty rate” language to the DESI top-1,000 test or provide equivalent large-sample cross-matches for each survey; adjust title/abstract accordingly.

6) Blue-dominant DESI anomalies are acknowledged as calibration-suspect but left unvetted; no contamination fraction is quantified. Evidence: §III A (44,436 B-dominant, 22.7%); §VI C flags likely calibration issues but retains the population without a mask or control test. Fix: Quantify how many B-dominant anomalies persist after imposing independent color outlier cuts (e.g., u−g vs g−r), fiber-throughput quality flags, or excluding high-airmass exposures; report contamination-adjusted rates.

7) Cross-survey deduplication mixes object detections with CMB patches in the headline count despite later stratification. Evidence: Table I footnote clarifies a 378,080 point-source tier plus 200 Planck patches but the abstract and §III/§IV text often discuss a single headline number. Fix: In all summaries, report both numbers (point sources and CMB patches) together and avoid aggregating them in any scientific inference or novelty statistics.

8) The DESI fold CV uses models that did not meet your own convergence gate; stability may be spurious. Evidence: §VI D(i): fold validation losses 0.76–4.91 vs the production-quality ≤ 0.30 gate; nonetheless, top-1% overlap is used to argue stability. Fix: Re-run the 5-fold CV to convergence (or relax/justify the gate for this test) and show that Jaccard stability holds; else down-weight the stability claim.

9) Data availability is not satisfied for review/reproducibility. Evidence: §ACK cites a HuggingFace dataset “private pending arXiv acceptance,” and numerous “companion artifacts” JSON are referenced but not accessible. Fix: Make all catalog parquet files, score vectors, and referenced JSON artifacts publicly accessible to referees (or include them as supplementary material) before acceptance.

## MINOR
- Ambiguous/loaded internal nomenclature (“R42 directive,” “gate-PASS,” “FAIL-with-diagnostic”) clutters the narrative and is non-standard for PRD; define once in §II and remove from captions/footnotes for clarity. Evidence: Table I footnotes; §II D; §VI D.

- Consistency in notation: reuse of “z” for both redshift and z-scored S can confuse; change one symbol. Evidence: Fig. 4 caption, §III B labels vs z ≈ 6.

- Several panel labels use “AE” for rZ while text uses S for total score; call this out directly on figures to prevent misinterpretation. Evidence: Fig. 5 caption.

- The spatial uniformity test in §IV B is close to meaningless without correcting for per-survey selection functions and masks; either qualify more strongly or remove.

## Strengths
- Ambitious, genuinely large-scale cross-survey anomaly sweep with transparent reporting of pathologies (LAMOST blue bias, CMB undertraining) and a thoughtful “Path-C” remediation protocol.

- Good engineering: per-survey native retrains, unified preprocessing, GPU throughput, and an 8-way 5″ deduplication with a calculated chance-coincidence budget.

- Honest limitations are discussed (e.g., DESI B-arm concerns, ACT quarantine), and several diagnostic checks are attempted (DESI k-fold stability, OOD distribution, injection–recovery variants).

- The cross-matched DESI×SDSS examples and the identification of z ~ 6 QSO candidates and an uncataloged BAL QSO candidate demonstrate the scientific utility of the catalog beyond a purely methodological exercise.
