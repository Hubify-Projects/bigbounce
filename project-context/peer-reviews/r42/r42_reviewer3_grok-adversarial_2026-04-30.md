══════════════════════════════════════════════════════════════════════════════
**ADVERSARIAL MULTI-AGENT PEER REVIEW — ROUND R42**
══════════════════════════════════════════════════════════════════════════════

### STAGE 1 — INVENTORY

**P1: Spin-Torsion Cosmology and the Search for Geometric Dark Energy**
*   **Version / Date:** v2.3.1 | April 30, 2026 | 31 pages
*   **Primary Thesis:** Minimal Einstein-Cartan-Holst (ECH) gravity yields a nonsingular quantum bounce but fails to inherently produce late-time dark energy without phenomenological tuning; scalar/tensor observables cleanly decouple from the parity-odd sector.
*   **Headline Numerical Claims:** LQC bounce at $\rho_{crit} \simeq 0.27-0.41 \rho_{Pl}$ (Eq 11); 14 structural constraints mapping ECH failure modes (Table IV); $H_0 = 67.68 \pm 1.06$, $\Delta N_{eff} = -0.020 \pm 0.169$ recovering $\Lambda$CDM (Table II); NaMaster $\beta = 0.238^\circ$ at SNR 20.32 (Sec VI).
*   **Figures / Tables:** Fig 1 (Energy density hierarchy). Table I (Executive summary). Table II (MCMC verification). Table IV (14 Constraints).
*   **Stated Novelty:** Comprehensive mapping of 14 structural constraints closing ECH dark energy pathways; formal proof of perturbation transparency decoupling the Holst sector from standard observables.

**P2: Testing the Matter Bounce with Primordial Non-Gaussianity**
*   **Version / Date:** v1.7.1 | April 30, 2026 | 13 pages
*   **Primary Thesis:** The matter bounce prediction $f_{NL}=-35/8$ is robustly testable by SPHEREx at 3–5$\sigma$ despite a local-template mismatch, and Bayesian evidence favors the bounce over tuned multifield inflation given a detection.
*   **Headline Numerical Claims:** Template overlap $r=0.84 \pm 0.02$ (Eq 5); Bayes factor 8–17 with $\sigma_{theory}=1.0$ prior (Table II); SPHEREx significance 5.2–5.5$\sigma$ (ideal) to 3–5$\sigma$ (realistic).
*   **Figures / Tables:** Fig 1 ($B_{NL}$ convergence). Fig 2 (Detection significance). Fig 3 ($f_{NL}$ landscape). Table III (Bayes factors vs GR degradation).
*   **Stated Novelty:** First explicit quantification of the matter-bounce vs. local template overlap; updated Bayesian discrimination resolving the Cai vs. Li-Brandenberger factor-of-2 discrepancy.

**P3: Multi-Survey Spectral Anomaly Detection: 378,000 Anomalous Sources**
*   **Version / Date:** v3.1.1 | April 30, 2026 | 35 pages
*   **Primary Thesis:** A unified BigAE architecture applied across 8 surveys identifies 378,480 unique anomalous objects, exposing massive instrument/training biases (LAMOST) and finding novel astrophysical sources.
*   **Headline Numerical Claims:** 378,480 unique physical objects; 98% LAMOST blue-excess artifact (21.5x reduction post-retrain); 17.8% genuine novelty floor; 5-fold CV $\overline{J}=0.862$ (Sec II.B).
*   **Figures / Tables:** Fig 3 (Spatial map). Fig 7 (LAMOST bias). Fig 11 (Injection-recovery). Table I (Survey summary). Appendix D (Taxonomy galleries).
*   **Stated Novelty:** Largest multi-survey anomaly catalog (37.3M sources); discovery of survey-scale ML artifacts; 8-way 5" positional deduplication.

**P4: No Evidence for Large-Scale Parity Violation in Galaxy Morphology**
*   **Version / Date:** v1.0.1 | April 30, 2026 | 16 pages
*   **Primary Thesis:** Utilizing a test-time equivariant Vision Transformer on 8.47 million galaxies definitively refutes prior claims of a 3% parity-violating chirality dipole.
*   **Headline Numerical Claims:** Global CW fraction $0.4974 \pm 0.0003$; True dipole $0.43\sigma$ vs 94.6$\sigma$ raw artifact (Sec IV.C); Minimum detectable dipole 0.2% at 3$\sigma$; 3.86x TTA suppression factor (Sec VI.D).
*   **Figures / Tables:** Fig 11 (Raw 94.6$\sigma$ vs Eq $0.43\sigma$ maps). Table II (Bias suite). Table III (Global CW fraction tiers). Table V (Sky region balance).
*   **Stated Novelty:** Largest bias-hardened chirality catalog (17x larger spiral sample than Shamir); explicit application of Test-Time Averaging resolving a decade-long literature controversy.

---

### STAGE 2 — CLAIM MAP 

| Claim | Source | Verification Surface | Verifiable? | Result |
| :--- | :--- | :--- | :--- | :--- |
| **1. 14 structural barriers map minimal ECH** | P1 §XI, Table IV | `arxiv/main.tex` | Y | **PASS**. Enumerated explicitly in text. |
| **2. $\Delta N_{eff} \approx 0$, 424,781 MCMC samples** | P1 §III.D, Table II | `reproducibility/cosmology/.../chains/dneff/` | Y | **PASS**. Sample counts perfectly match the repo fix from R41. |
| **3. NaMaster $\beta = 0.238^\circ$, SNR 20.32** | P1 Abstract, §VI | `pipelines/h200_results/pod1_namaster_umap_2026-04-29/.../summary.json` | Y | **PASS**. JSON contains these exact values. |
| **4. Incompatibility of DE ($N_{tot}\approx 92$) and $f_{NL}$** | P1 §XV.E | `arxiv/main.tex` | Y | **PASS**. Tension explicitly acknowledged. |
| **5. Template overlap $r=0.84 \pm 0.02$** | P2 §III.B | `research/focused_paper_source_integration/02_full_draft.tex` | Y | **PASS**. Verified by 10,000 null-space coefficient scan. |
| **6. Bayes factor 8-17** | P2 §VI.C, Table II | `research/focused_paper_source_integration/02_full_draft.tex` | Y | **PASS**. $\sigma_{theory}=1.0$ spread prior is utilized in text. |
| **7. 378,480 unique anomalies** | P3 Abs, Table I | `https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog` | Y | **PASS**. Parquet `pathc_unique_objects.parquet` matches row count. |
| **8. 17.8% Genuine Novelty** | P3 §IV.A.a | `pipelines/p3_anomaly_engine/...` | Y | **PASS**. Admitted in text; derived from VizieR cross-match. |
| **9. 5-fold CV $\overline{J}=0.862$** | P3 §II.B, §VI.D(i) | `pathc_desi_kfold/results/kfold_stability_summary.json` | Y | **PASS**. Metric exists, but strictly evaluated on the 47k pool. |
| **10. eROSITA top cut is 298 anomalies** | P3 Table I, §III.E | `pipelines/p3_anomaly_engine/...` | Y | **PASS**. Clarified vs deprecated 9,303 metric. |
| **11. Pipeline-1 Gold+Silver bias = 1.58x** | P3 §VI.C | `projects/cross_survey/results/bias_validation.json` | Y | **PASS**. Confirms 1.58x, purging R41's ghost 2.28x. |
| **12. Global CW fraction 0.4974** | P4 Abs, Tab III | `public/spreadsheets/*.csv` | Y | **PASS**. Data reflects this exact split. |
| **13. Raw 94.6$\sigma$ dipole collapses via TTA** | P4 §VI.A, Fig 11 | `pipelines/p2_chirality/outputs/dipole/...` | Y | **PASS**. Logs confirm raw vs TTA dipole fits. |
| **14. 65.7% edge-on contamination leakage** | P4 §VI.D | `pipelines/p2_chirality/chirality_catalog_paper.tex` | Y | **PASS**. Text explicitly admits this leakage. |

---

### STAGE 3 — INDIVIDUAL REVIEWS

#### **A. DOMAIN EXPERT (Cosmology)**
1. **[BLOCKER] P1, Title & Abstract:** *Quote:* "Search for Geometric Dark Energy" (Title). *Issue:* The author conceded the R41 fatal Horizon contradiction, acknowledging in Section XV.E that the 92 e-folds required for the DE mechanism physically erases the matter bounce $f_{NL}$ signature. However, the title and abstract still pitch a "Search for Geometric Dark Energy." You cannot retain this title when your own paper proves the mechanism erases the observable universe. *Fix:* Change the title to "Structural Constraints on Spin-Torsion Cosmology". Present the 92 e-folds purely as a falsified No-Go theorem from the opening line.
2. **[MAJOR] P2, Sec II.D:** *Quote:* "$w=-0.003$, one free parameter tuned to the Planck observed $n_s$". *Issue:* P2 repeatedly frames $f_{NL} = -35/8$ as "minimally parameterized" or "parameter-free." But if the equation of state $w$ is explicitly tuned to match $n_s$, the $\mathcal{O}(\epsilon)$ correction directly shifts $f_{NL}$. This makes it a parametric fit, not an absolute parameter-free prediction. *Fix:* Drop the "parameter-free" rhetoric. Clearly state the exact value of $f_{NL}$ is contingent upon the $n_s$ match.

#### **B. SKEPTICAL REFEREE 2**
3. **[BLOCKER] P3, Sec VI.D(i):** *Quote:* "A 50%-split held-out validation on the full catalog would provide an additional guarantee but requires ~2x the full-survey inference budget and is not executed here". *Issue:* This is a brazenly false excuse. The author's own Table IV states a throughput of 1,142 spectra/sec. Running validation on 100,000 completely unseen spectra would take exactly **87.5 seconds** of GPU time. The author is refusing to test out-of-distribution stability because they fear the MSE distributions will shift. *Fix:* Run the 100k out-of-sample inference.
4. **[MAJOR] P3, Title / Sec IV.A:** *Quote:* "Multi-Survey Spectral Anomaly Detection: 378,000 Anomalous Sources" (Title). *Issue:* In Sec IV.A, you admit that 82.2% of the DESI top-1000 anomalies are known objects in VizieR. Labeling hundreds of thousands of standard stars and known QSOs as "Anomalies" just because they aren't in SIMBAD is pure clickbait. *Fix:* Retitle to "Spectrally Unusual Sources". Lead the abstract with the 17.8% genuine novelty rate.

#### **C. METHODS / STATISTICS REVIEWER**
5. **[BLOCKER] P4, Sec VI.D:** *Quote:* "...so a per-bin axis-ratio test requires a positional cross-match with the parent DESI Legacy photometric catalog... [which] is not executed in the present analysis." *Issue:* You identified that 65.7% of edge-on galaxies ($b/a < 0.3$) receive random CW/CCW labels, injecting massive binomial noise into your dipole fit. You proposed the exact mathematical fix, then admitted you didn't do it to save a simple `pandas.merge()` operation. *Fix:* Perform the positional cross-match, drop the $b/a < 0.3$ objects, and recalculate the final dipole.
6. **[MAJOR] P4, Sec II.B:** *Quote:* "We note that 67.6% of training labels (17,999 of 26,636) derive from CE-ResNet predictions." *Issue:* Quoting 93.7% accuracy on a validation set where 67.6% of the ground-truth answers are derived from another algorithm is measuring model distillation (self-consistency), not ground-truth accuracy. *Fix:* Recalculate and report accuracy *strictly* on the 6,637 independent Galaxy Zoo 1 labels.

#### **D. MATH / LOGIC REVIEWER**
7. **[BLOCKER] P2, Appx A:** *Quote:* "Interpreting the factor of two as the standard in-in commutator factor—$i\langle[\zeta^3, L]\rangle = -2 \text{Im} \langle\zeta^3 L\rangle$..." *Issue:* R41 explicitly instructed you to write out the mathematical Wick contractions to prove the Cai vs Li-Brandenberger convention mapping. You just added a narrative sentence. "Interpreting" is not a mathematical derivation in perturbation theory. *Fix:* Write out the exact integral over conformal time and explicitly show the $-2\text{Im}$ operation mathematically.
8. **[MAJOR] P1, Appx B:** *Quote:* "This is a scaling ansatz dimensionally correct on-shell at the bounce not a derivation from a renormalizable off-shell EFT." *Issue:* The parity-odd operator has mass dimension +1. Evaluating an operator "on-shell" to supply missing dimensions in a Lagrangian violates EFT power counting. Changing the name to "scaling ansatz" prevents it from being a lie, but it remains a mathematical dead end. *Fix:* Move this admission into the main text (Sec II.C) and explicitly state that ECH fails to derive a dimensionally consistent DE operator off-shell.
9. **[MAJOR] P4, Sec IV.B:** *Quote:* "The residual [9.5$\sigma$ deficit] likely reflects a sub-percent asymmetry in the training labels themselves" *Issue:* Test-Time Averaging (Eq 3) forces $P_{CW}^{eq} = \frac{1}{2}(P_{CW}^{orig} + P_{CCW}^{flip})$. The ONLY mathematical way the global fraction drops below 0.5000 is if probability mass leaks asymmetrically into the `NOT_SPIRAL` class during TTA. It cannot be standard CW/CCW training bias. *Fix:* Query the raw probability transition matrices to explicitly report the exact fraction of CW vs CCW logits that get pushed to `NOT_SPIRAL`.

#### **E. LITERATURE REVIEWER**
10. **[MINOR] P2, Sec VIII.A:** *Quote:* "Current constraints from Planck (CMB bispectrum, $f_{NL} = -0.9 \pm 5.1$ [23])". *Issue:* This cites the 2018 PR3 results. For state-of-the-art bounds, you must cite the Planck PR4 (NPIPE) re-analyses. *Fix:* Update the citation.

#### **F. CROSS-PAPER REVIEWER**
11. **[BLOCKER] P3 vs P2 Contradiction:** *Quote (P3 Sec V):* "Anomaly-selected tracers... yields $\sigma(f_{NL}) = 8.43$, a 6.1% improvement... combining DESI and SDSS anomalies extends the improvement to ~10-20%". *Quote (P2 Sec IV):* "for anomaly-selected tracers ($\bar{n} \sim 10^{-5}$), shot noise is more significant: a simple Poisson estimate gives a ~15-30% degradation in $\sigma(f_{NL})$". *Issue:* Fatal contradiction. P3 claims a 6.1% improvement citing P2. P2 explicitly says shot noise *degrades* the measurement by 30% for these sparse tracers. *Fix:* P3 must retract the 6-20% improvement claim entirely, unless P2 generates a full multi-tracer Fisher matrix proving covariance cancellation overrides the shot-noise penalty.

#### **G. REPRODUCIBILITY REVIEWER**
12. **[MAJOR] P3, Table I & Sec III.G:** *Quote:* "ACT DR6 (200 patches) is formally quarantined... (the 378,480 headline counts ACT only at the input deduplication stage)". *Issue:* If a survey is quarantined because the model failed (val loss $2\times 10^4$), its outputs are garbage. You cannot include 200 garbage patches in the "388,693" or "378,480" headline sums just to avoid updating your master spreadsheets and abstracts. *Fix:* Drop ACT DR6 from the quantitative sums entirely. The new total is 378,280.

#### **H. ETHICS / RESEARCH-INTEGRITY REVIEWER**
13. **[MAJOR] P3, Sec II.B / VI.D:** *Issue:* Performing 5-fold cross-validation exclusively on the 47,000-spectrum training pool, and burying that fact in Caveat (i) of Section VI.D, borders on data leakage deception. *Fix:* The training-set limitation of the CV must be stated upfront in Section II.B where the CV is first introduced.

#### **I. STRUCTURE / WRITING REVIEWER**
14. **[MINOR] P3, Sec II.D:** *Quote:* "We therefore executed a follow-on 'Path-C rebuild' protocol". *Issue:* The methodology section still reads like a chronological lab diary of failures and retrains. Scientific papers present the final, successful methodology. *Fix:* Present the Path-C native retrains as the *core methodology*. Move the cross-transfer baseline and LAMOST blue-excess artifact to a "Methodological Pitfalls" section.

#### **J. META REVIEWER**
*(See Stage 9 for Synthesis)*

---

### STAGE 4 — DEBATE

*   **Reviewer C (Methods) vs. Reviewer B (Skeptic) on P3 Validation:**
    *   *Methods:* "I agree with Skeptic B. The author's claim that a 50% split requires too much compute is a blatant lie when 100k spectra take 87.5 seconds. But look at the k-fold Jaccard index ($\overline{J}=0.862$) on the training pool. The model is highly stable internally. It's a MAJOR flaw, but quickly fixable."
    *   *Skeptic:* "It doesn't matter how stable the training pool is. An autoencoder measures density. If you evaluate on unseen data, the MSE distribution *will* shift. Reject P3 until the 100k script is run."
    *   *Meta-Verdict:* Skeptic B is correct. The author must execute the 100k out-of-distribution validation. The compute excuse is invalid.
*   **Reviewer A (Domain) vs. Reviewer D (Math) on P1 Dimensional Ansatz:**
    *   *Math:* "P1's scaling ansatz evaluates off-shell operators on-shell to fix units. That violates EFT power counting. It's mathematically dead."
    *   *Domain:* "The author *admits* it's a scaling ansatz in Appx B. They aren't claiming it's rigorous EFT."
    *   *Meta-Verdict:* The author must move the admission from the Appendix to the main text (Sec II.C) so readers see the EFT violation upfront.
*   **Reviewer F (Cross-Paper) vs. Reviewer A (Domain) on P3 Tracer Utility:**
    *   *Cross-Paper:* "P3 claims a 6.1% improvement from anomaly tracers. P2 says shot noise degrades it by 30%. That's a blocker."
    *   *Domain:* "P2 says anomaly tracers *would* degrade if used alone. As a multi-tracer add-on, they break the $b_1/b_\phi$ degeneracy, which is where the improvement might come from."
    *   *Meta-Verdict:* The text in P2 does not explicitly calculate the multi-tracer covariance cancellation against the Poisson noise. Until it does, P3's 6.1% improvement claim is physically unsupported and must be retracted.

---

### STAGE 5 — CROSS-PAPER CONSISTENCY

| Metric / Claim | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Status / Flag |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$f_{NL}$ Prediction** | -35/8 | -35/8 | -35/8 | N/A | **MATCH**. Consistent across portfolio. |
| **$\beta_{ALP}$ Birefringence**| $0.27^\circ$ | N/A | $0.27^\circ$ | N/A | **MATCH**. |
| **Anomaly Total** | N/A | N/A | 378,480 | N/A | **NO**. Includes 200 quarantined ACT patches. Must be 378,280. |
| **Tracer Utility** | N/A | 15-30% loss | 6.1% gain | N/A | **FATAL MISMATCH (F14)**. P3 claims an improvement P2 explicitly refutes. |
| **MCMC Samples** | 424,781 | N/A | N/A | N/A | **MATCH**. Arithmetic fixed from R41. |
| **PTA $\gamma$** | N/A | $3.20 \pm 0.42$ | $3.20 \pm 0.42$ | N/A | **MATCH**. |
| **Parity Dipole** | $0.43\sigma$ | N/A | N/A | $0.43\sigma$ | **MATCH**. |

---

### STAGE 6 — EXHAUSTIVE AUDIT LOG

| ID | Paper | § / Page | Reviewer | Severity | Quote/Issue | Fix |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AL01** | P1 | Title, Abs | A. Domain | **BLOCKER** | "Search for Geometric Dark Energy" | The theory destroys itself via the 92 e-fold horizon problem. Retitle to "Structural Constraints on Spin-Torsion Cosmology" and reframe as a No-Go theorem. |
| **AL02** | P3 | §VI.D(i) | B. Skeptic | **BLOCKER** | "requires ~2x the full-survey inference budget" | False excuse for avoiding out-of-distribution validation (takes 87s for 100k spectra). Run the 100k unseen validation. |
| **AL03** | P3/P2| P3(§V), P2(§IV)| F. Cross | **BLOCKER** | P3 claims 6.1% improvement; P2 warns of 15-30% shot noise degradation. | Retract the 6.1% improvement claim in P3, or provide the shot-noise marginalized Fisher matrix in P2 to back it up. |
| **AL04** | P4 | §VI.D | C. Methods | **BLOCKER** | "requires a positional cross-match... is not executed" | Refusing to do a basic table join to filter 65.7% edge-on contamination ruins catalog purity. Filter $b/a < 0.3$. |
| **AL05** | P2 | Appx A | D. Math | **BLOCKER** | "Interpreting the factor of two as the standard in-in commutator..." | Math discrepancy resolved via narrative text rather than formulas. Write out explicit Wick contractions. |
| **AL06** | P3 | Title | B. Skeptic | **MAJOR** | "378,000 Anomalous Sources" | Title implies discovery; text admits 82.2% are known in VizieR. Change title to "Spectrally Unusual Sources"; highlight 17.8% true novelty. |
| **AL07** | P1 | Appx B | D. Math | **MAJOR** | "scaling ansatz dimensionally correct on-shell at the bounce" | Evaluating dim+1 operators on-shell to get dim+4 violates EFT. Move admission to main text (Sec II.C). |
| **AL08** | P4 | §IV.B | D. Math | **MAJOR** | Attributes 0.4974 deficit to "training labels themselves". | TTA mathematically requires this to be `NOT_SPIRAL` leakage. Compute the transition matrix to prove leakage. |
| **AL09** | P4 | §II.B | C. Methods | **MAJOR** | "67.6% of training labels... derive from CE-ResNet" | 93.7% accuracy is self-consistency, not ground truth. Report accuracy strictly on the 6,637 GZ1 labels. |
| **AL10** | P3 | Table I | G. Repro | **MINOR** | "388,693 detections - 10,213 duplicates = 378,480" | Includes 200 quarantined ACT patches. Subtract them. Headline = 378,280. |
| **AL11** | P1 | §VII | A. Domain | **MINOR** | "The extended parameter space adds $\{\Delta N_{eff}...\}$" | Bayes factor +4.8 is for generic $\Delta N_{eff}$, not specific to ECH. Clarify this in abstract/text. |
| **AL12** | P3 | §II.D | I. Struct | **MINOR** | "Path-C rebuild" chronological diary format. | Unprofessional structure. Present native retrains as core methodology; move cross-transfer failures to Discussion. |

---

### STAGE 7 — PER-PAPER REVISION PLAN

#### **P1: Spin-Torsion Cosmology**
1.  **Must-fix (BLOCKER):** Title change is mandatory. "Search for Geometric Dark Energy" implies viability of a theory the text systematically destroys (via the 92 e-fold horizon problem). Reframe explicitly as "Structural Constraints on Spin-Torsion Cosmology".
2.  **Should-fix (MAJOR):** Move the $\rho_\Lambda = \Xi M_{Pl}^4$ dimensional scaling derivation from Appendix B into the main text (Sec II.C). Explicitly state that ECH fails to generate a dimensionally consistent DE operator off-shell.
3.  **Nice-to-fix (MINOR):** Clarify that the MCMC Bayes factor of +4.8 tests a generic thermal history ($\Delta N_{eff}$), not ECH torsion specifically.
*Estimated Effort: 2-6h (Heavy structural text rewriting).*

#### **P2: Testing the Matter Bounce**
1.  **Must-fix (BLOCKER):** Replace the narrative text in Appendix A with the explicit mathematical Wick contraction equations ($\langle \zeta \zeta \zeta \mathcal{L} \rangle$) demonstrating the $-2\text{Im}$ operation that resolves the Cai vs Li-Brandenberger discrepancy.
2.  **Must-fix (BLOCKER):** Resolve the P3 contradiction. If anomaly tracers have $\bar{n} \sim 10^{-5}$, explicitly calculate the shot-noise penalized Fisher matrix. If it degrades, force P3 to retract the 6.1% improvement claim.
3.  **Should-fix (MAJOR):** Soften the "parameter-free" language in the abstract, acknowledging that the prediction requires an $\mathcal{O}(\epsilon)$ tuning to match $n_s$.
*Estimated Effort: 4-8h (Math derivations).*

#### **P3: Multi-Survey Spectral Anomaly Catalog**
1.  **Must-fix (BLOCKER):** Execute the BigAE inference script on 100,000 completely unseen DESI spectra. Plot the MSE distribution and prove it matches the training-set validation distribution. Delete the false excuse about compute time.
2.  **Must-fix (BLOCKER):** Retract the claim in Section V that anomaly tracers improve $\sigma(f_{NL})$ by 6.1%, as P2 mathematically refutes this due to shot noise.
3.  **Should-fix (MAJOR):** Retitle the paper to "Multi-Survey Spectrally Unusual Sources". Feature the 17.8% true novelty rate prominently. Restructure Section II/III to present Native Retrains as the core pipeline.
4.  **Nice-to-fix (MINOR):** Remove the 200 ACT DR6 patches from all quantitative sums (new total: 378,280).
*Estimated Effort: 4-12h (100k inference + rewrite).*

#### **P4: Galaxy Chirality Catalog**
1.  **Must-fix (BLOCKER):** Perform the positional cross-match with the DESI Legacy axis-ratio data. Filter out edge-on galaxies ($b/a < 0.3$), and recalculate the final dipole on the clean face-on subset.
2.  **Should-fix (MAJOR):** Stop blaming the 9.5$\sigma$ monopole deficit (0.4974) on GZ1 human bias. Compute the transition matrix into `NOT_SPIRAL` to prove the asymmetric leakage.
3.  **Should-fix (MAJOR):** Recalculate and report the classifier accuracy *strictly* on the 6,637 Galaxy Zoo 1 labels to avoid CE-ResNet circularity.
*Estimated Effort: 4-8h.*

---

### STAGE 8 — GLOBAL RECOMMENDATIONS

*   **The Paradigm Shift:** The author successfully executed the R41 recommendations for P1 and P4. P1 is now intellectually honest about the failure of the dark energy mechanism (the Horizon contradiction), and P4 mathematically quantifies the TTA leakage via the 3.86x suppression factor. **However, the author refuses to update the titles and abstracts to reflect this.** A paper that proves ECH dark energy fails cannot be titled "The Search for Geometric Dark Energy".
*   **The Weak Link (P3):** P3 currently suffers from a massive data leakage flaw (CV restricted to training set) and an incoherent, chronological narrative structure. By running the 100k out-of-sample validation and restructuring the text, it will function excellently as an ML methods paper highlighting the dangers of domain shift.
*   **Publication Strategy:**
    1.  **P4 (Chirality)** $\rightarrow$ ApJ. It is computationally magnificent and solves a decade-old controversy. Execute the $b/a$ filter.
    2.  **P2 (Forecast)** $\rightarrow$ JCAP. Solid Fisher recast. Write out the Appendix A math.
    3.  **P3 (Anomaly)** $\rightarrow$ ApJS. Requires the 100k out-of-sample validation and narrative cleanup.
    4.  **P1 (Theory)** $\rightarrow$ PRD. Radically rewrite to frame as a No-Go theorem constraint map.

---

### STAGE 9 — META VERDICT

**P1: Spin-Torsion Cosmology**
**Verdict: MAJOR REVISION**
*Justification:* The 14 structural barriers are a phenomenal contribution, but the paper retains a title and abstract implying a successful dark energy mechanism that the text itself proves is mathematically and physically excluded (via the 92 e-fold horizon problem). The paper must be reframed entirely to accept its own negative results: ECH cannot solve dark energy natively. Change the title.

**P2: Testing the Matter Bounce**
**Verdict: MINOR REVISION**
*Justification:* The template mismatch calculation ($r=0.84$) is rigorous, and the Bayesian priors have been fixed successfully from R41 ($\sigma_{theory}=1.0$). The remaining blockers are resolving the shot noise contradiction with P3, and replacing the narrative explanation in Appendix A with the actual Wick contraction equations.

**P3: Multi-Survey Spectral Anomaly Catalog**
**Verdict: REJECT AND RESUBMIT**
*Justification:* Refusing to validate an ML model on out-of-sample data because of a fabricated compute-time excuse (87 seconds vs "2x inference budget") is a fatal methodological violation. Furthermore, claiming a 6.1% cosmological improvement that directly contradicts P2's shot-noise findings destroys credibility. Must OOD-validate on 100k spectra and retract the $f_{NL}$ claims.

**P4: Galaxy Chirality Catalog**
**Verdict: MINOR REVISION**
*Justification:* The TTA pipeline brilliantly solves the 94.6$\sigma$ survey artifact. However, the author refuses to filter out 65.7% edge-on contamination ($b/a < 0.3$) because it requires a table join, introducing massive binomial noise. The author must filter the edge-on galaxies, quantify the `NOT_SPIRAL` leakage to explain the $0.4974$ deficit, and report accuracy on independent GZ1 labels.

**PORTFOLIO VERDICT:**
The transition to R42 shows excellent responsiveness to the hardest theoretical critiques (the Horizon Contradiction). The remaining issues are primarily data-engineering laziness (refusing to cross-match axis ratios in P4, refusing to run 100k out-of-sample inference in P3) and rhetorical overhangs (clickbait titles, refusing to write out equations). Execute these final fixes, perform the basic table joins, and this is a formidable, multi-journal publication suite.

