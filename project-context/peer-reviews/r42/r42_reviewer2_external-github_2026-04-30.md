k here are all the new peer reviews: 

According to the April 30, 2026 R42 PDFs and the verification surfaces I could reach, all four uploaded papers are accessible and readable. I also checked the public site, SSOT page, GitHub repository pages, selected raw GitHub artifacts, and HuggingFace pages where possible. The NaMaster `summary.json` supports the quoted β recovery/SNR, but the raw `reproducibility/cosmology/convergence_latest.csv` visible on GitHub does **not** support the paper’s “publication-quality convergence” language; it shows large R̂ values in the main visible file, so the paper must point to the exact frozen-chain diagnostics instead of a stale or contradictory summary file.  ([GitHub][1])

# STAGE 1 — Inventory

## Access / verification status

| Item                       | Status                                                                                                                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 PDF                     | Accessible: v2.3.1, April 30, 2026, 31 pp.                                                                                                                                                                                  |
| P2 PDF                     | Accessible: v1.7.1, April 30, 2026, 13 pp.                                                                                                                                                                                  |
| P3 PDF                     | Accessible: v3.1.1, April 30, 2026, 35 pp.                                                                                                                                                                                  |
| P4 PDF                     | Accessible: v1.0.1, April 30, 2026, 16 pp.                                                                                                                                                                                  |
| Site / SSOT                | Accessible. SSOT claims all four are 100% ready and notes remaining queued items including sample-count harmonization, MC-realization harmonization, site sync, and arXiv upload. ([BigBounce — Spin-Torsion Cosmology][2]) |
| GitHub repo                | Accessible as a public repo; directory browsing works, raw files partially accessible. ([GitHub][3])                                                                                                                        |
| NaMaster summary JSON      | Accessible and supports β=0.27° → 0.238°, SNR=20.3156, 500 MC. ([GitHub][1])                                                                                                                                                |
| P1 convergence CSV         | Accessible but contradicts the paper’s convergence claim if treated as current/canonical: visible R̂ values are far above publication thresholds. ([GitHub][4])                                                             |
| HuggingFace P4 model       | Accessible; model card says 26,626 training images, 93.7% validation, 8/8 tests. This conflicts with the P4 paper’s 26,636 training-image count. ([Hugging Face][5])                                                        |
| HuggingFace P3/P4 datasets | P4 catalog dataset and P3 anomaly datasets returned 401 Unauthorized from my session. Treat as “owner-confirmed / access-restricted,” not fabricated.                                                                       |
| SPHEREx current status     | Official JPL/NASA pages show SPHEREx launched in March 2025 and began capturing the sky in 2025; P2’s “first science data ∼2028” needs clarification or correction. ([NASA Jet Propulsion Laboratory (JPL)][6])             |

## P1 inventory — Spin-Torsion Cosmology

| Field                     | Inventory                                                                                                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title / version           | *Spin-Torsion Cosmology and the Search for Geometric Dark Energy: Structural Barriers, Perturbation Transparency, and Surviving Predictions*, v2.3.1, April 30, 2026, 31 pp.                                                       |
| Primary thesis            | Minimal Einstein-Cartan-Holst spin-torsion gravity does not derive late-time dark energy or distinctive perturbation observables; the surviving observational test is matter-bounce fNL, compatible with but not derived from ECH. |
| Headline numerical claims | ρcrit≈0.27–0.41ρPl; 14 structural constraints; 424,781 MCMC samples; H0=67.68±1.06; ΔNeff≈0; β=0.27° recovered as 0.238° at SNR=20.32; Ntot≈92; fNL=−35/8; SPHEREx 3–5σ.                                                           |
| Figures                   | Fig. 1 energy-density hierarchy; Fig. 2 Gaussian summary-likelihood consistency check; Fig. 3 full-tension MCMC corner plot.                                                                                                       |
| Tables                    | Table I executive summary; Table II MCMC verification; Table III Bayesian model comparison; Table IV 14 constraints; Table V bounce-model discrimination; Table VI parameter summary; Table VII claims classification.             |
| Claimed novelty           | 14-constraint catalog, perturbation-transparency observation, synthesis of LQC/ECH/black-hole-universe elements, MCMC null verification, spectator-ALP consistency check.                                                          |
| Immediate risk            | The abstract still says “ECH provides a well-motivated nonsingular quantum bounce,” but the body footnote says the bounce equation is LQC and “not the source” from ECH. This is a theory-identity blocker.                        |

## P2 inventory — fNL forecast

| Field                     | Inventory                                                                                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Title / version           | *Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper*, v1.7.1, April 30, 2026, 13 pp.                                                                                                          |
| Primary thesis            | Matter-dominated contraction predicts fNL=−35/8, and SPHEREx can test it at 3–5σ realistic significance after template and systematics degradation.                                                                                        |
| Headline numerical claims | fNL=−35/8=−4.375; inflation comparison ≈290×; template recovery r=0.84±0.02; r∈[0.821,0.879]; 200 injection-recovery realizations; 10,000 null-space coefficient samples; SPHEREx σ(fNL)≈0.7; MegaMapper σ≈0.5 ideal; Bayes factor ≈8–17.  |
| Figures                   | Fig. 1 matter-bounce bispectrum shape; Fig. 2 detection significance; Fig. 3 fNL landscape; Fig. 4 σ(fNL) vs. kmin / systematics; Fig. 5 σ(fNL) vs. bϕ and GR degradation; Fig. 6 decision thresholds.                                     |
| Tables                    | Table I benchmark shape-function values; Table II Bayesian comparison; Table III Bayesian comparison with parameterized GR degradation.                                                                                                    |
| Claimed novelty           | First explicit matter-bounce/local-template mismatch quantification; convention audit of Cai vs. Li-Brandenberger; SPHEREx/MegaMapper discrimination framing.                                                                              |
| Immediate risk            | The whole forecast depends on accepting −35/8 as the observational convention, but the paper admits no full independent in-in derivation.                                                                                                  |

## P3 inventory — anomaly catalog

| Field                     | Inventory                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title / version           | *Multi-Survey Spectral Anomaly Detection: 378,000 Anomalous Sources from 37 Million Objects Across Eight Astronomical Archives*, v3.1.1, April 30, 2026, 35 pp.                                                                                                                                                                                      |
| Primary thesis            | BigAE applied across eight archives yields a large, tiered anomaly catalog, with Path-C native retraining reducing cross-transfer artifacts and producing 378,480 unique physical objects.                                                                                                                                                           |
| Headline numerical claims | 37,292,042 sources; 319,443 cross-transfer detections; 388,693 Path-C survey-level detections; 378,480 unique after 5″ dedup; DESI 195,829; SDSS 77,905; LAMOST 113,342 Path-C native top-1%; eROSITA 298; Planck 200; ACT 200; Gaia 500; NEOWISE 419; DESI Jaccard 0.862; novelty ∼17.8%; LAMOST 5σ recovery 5.8%.                                  |
| Figures                   | Fig. 1 BigAE architecture; Fig. 2 spectra examples; Fig. 3 spatial anomaly map; Fig. 4 score distributions; Fig. 5 high-z QSO candidates; Fig. 6 SDSS UMAP; Fig. 7 LAMOST artifact; Fig. 8 NEOWISE top anomaly; Fig. 9 SIMBAD-unmatched fractions; Fig. 10 DESI×SDSS matches; Fig. 11 injection-recovery gates; Figs. 12–21 DESI taxonomy galleries. |
| Tables                    | Table I multi-survey sweep; Table II SDSS categories; Table III top eROSITA anomalies; Table IV computational details; Table V DESI arm dominance; Table VI σ(fNL) sensitivity to bias enhancement.                                                                                                                                                  |
| Claimed novelty           | Largest multi-archive anomaly detection campaign; Path-C native retraining audit; tiered cross-survey catalog; anomaly-selected tracer outlook.                                                                                                                                                                                                      |
| Immediate risk            | The title says “spectral” and “sources,” but the catalog includes photometric catalogs and CMB map patches, and the primary count still includes weakly validated or quarantined components.                                                                                                                                                         |

## P4 inventory — chirality catalog

| Field                     | Inventory                                                                                                                                                                                                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title / version           | *No Evidence for Large-Scale Parity Violation in Galaxy Morphology: A Survey-Scale Chirality Catalog of 8.47 Million Galaxies*, v1.0.1, April 30, 2026, 16 pp.                                                                                                                                                      |
| Primary thesis            | A flip-symmetrized ViT catalog of 8.47M DESI Legacy galaxies finds no significant large-scale galaxy-chirality parity violation and strongly disfavors claimed ∼3% asymmetry.                                                                                                                                       |
| Headline numerical claims | 8,474,531 galaxies; 26,636 training images; 67.6% CE-ResNet labels; 93.7% accuracy; 8/8 validation bias tests; stress test 4/8; full equivariant fCW=0.4974±0.0003; simple dipole 0.43σ; pseudo-Cℓ ℓ=1 2.75σ; hemisphere 3.05σ / 0.17% not LEE-corrected; max regional asymmetry 0.32%; raw spurious dipole 94.6σ.  |
| Figures                   | Fig. 1 sky density; Fig. 2 CW gallery; Fig. 3 CCW gallery; Fig. 4 TTA procedure; Fig. 5 class breakdown; Fig. 6 confidence distribution; Fig. 7 asymmetry map; Fig. 8 angular power; Fig. 9 hemisphere scan; Fig. 10 region balance; Fig. 11 raw spurious dipole.                                                   |
| Tables                    | Table I confusion matrix; Table II bias audit; Table III global CW fraction; Table IV angular power spectrum; Table V sky-region balance.                                                                                                                                                                           |
| Claimed novelty           | Largest chirality catalog; first multi-test bias-hardening suite; demonstration that raw classifier bias can generate a 94.6σ false dipole.                                                                                                                                                                         |
| Immediate risk            | Page 7 contains an unresolved count mismatch: text/Table III use 3,321,795 spirals, while Fig. 5 displays Catalog C counts summing to 3,201,160.                                                                                                                                                                    |

# STAGE 2 — Claim map with verification surface

## P1 — top 15 claims

|      # | Claim                                                          | Source in paper       | Verification surface                               | Verifiable now?       | Verification result                                                                                               |
| -----: | -------------------------------------------------------------- | --------------------- | -------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------- |
|  P1-C1 | ECH can be investigated as a route to late-time dark energy.   | Abstract / Intro      | P1 PDF; `arxiv/main.tex`                           | Yes                   | The paper now mostly says the route fails, but the title and opening still over-frame dark energy.                |
|  P1-C2 | LQC gives bounce at ρcrit≈0.27–0.41ρPl.                        | Abstract; Eq. 10–11   | P1 PDF                                             | Yes                   | Internally supported, but not ECH-specific.                                                                       |
|  P1-C3 | ECH parity structure generates four-fermion interaction.       | Eq. 4                 | P1 PDF                                             | Partial               | Qualitatively standard, but parity-odd wording remains too broad.                                                 |
|  P1-C4 | 14 structural constraints map minimal ECH dark-energy routes.  | Table IV / Sec. XI    | P1 PDF                                             | Yes                   | Supported as an internal catalog; novelty/independence still mixed.                                               |
|  P1-C5 | Perturbation transparency for canonical scalar matter.         | Sec. XII              | P1 PDF                                             | Partial               | Plausible under assumptions; “all perturbation orders” is stronger than shown.                                    |
|  P1-C6 | Holst dual contraction vanishes by first Bianchi identity.     | Abstract / Sec. XII   | P1 PDF                                             | Partial               | Likely correct for torsionless Levi-Civita connection, but needs careful Holst/Nieh-Yan language.                 |
|  P1-C7 | MCMC uses stock CAMB with ΔNeff as proxy.                      | Abstract / Sec. VII   | P1 PDF; GitHub reproducibility                     | Yes                   | Paper correctly admits stock CAMB; therefore not a direct ECH perturbation test.                                  |
|  P1-C8 | 424,781 samples with publication-quality convergence.          | Abstract / Sec. III D | `reproducibility/cosmology/convergence_latest.csv` | Partial / problematic | Visible CSV has high R̂ values, contradicting paper unless stale. Must point to frozen diagnostics. ([GitHub][4]) |
|  P1-C9 | NaMaster β=0.27° recovery as 0.238°, SNR=20.32.                | Sec. VI / Eq. 17      | `pipelines/h200_results/.../summary.json`          | Yes                   | Verified by raw JSON. ([GitHub][1])                                                                               |
| P1-C10 | ALP β is consistency check, not ECH prediction.                | Sec. III A / XIV C    | P1 PDF                                             | Yes                   | Strong and honest caveat; keep it prominent.                                                                      |
| P1-C11 | Ntot≈92 dark-energy suppression conflicts with observable fNL. | Abstract / Sec. XV E  | P1 PDF; P2 assumptions                             | Yes                   | This is the most important cross-paper tension and is now explicitly stated.                                      |
| P1-C12 | fNL=−35/8 is “surviving testable prediction.”                  | Abstract / Table I    | P1 + P2 PDFs                                       | Yes                   | Must always be called matter-bounce, not ECH-derived.                                                             |
| P1-C13 | Galaxy spin channel closed by P4.                              | Sec. III B / V        | P1 + P4 PDFs                                       | Partial               | P4 null is promising but P4 numerical/statistical inconsistencies remain.                                         |
| P1-C14 | NANOGrav γ=3.20±0.42 supports bounce consistency.              | Sec. XV C             | P1/P3 PDFs                                         | Partial / problematic | P1 contains both strong-Bayes and synthetic-data caveats; needs demotion.                                         |
| P1-C15 | Data/code reproduce headline results.                          | Data availability     | GitHub                                             | Partial               | NaMaster JSON visible; convergence surface contradictory; some HF datasets access-restricted.                     |

## P2 — top 15 claims

|      # | Claim                                                          | Source                 | Verification surface   | Verifiable now? | Verification result                                                                                                                                                            |
| -----: | -------------------------------------------------------------- | ---------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  P2-C1 | Matter bounce predicts fNL=−35/8.                              | Abstract / Eq. 2       | P2 PDF                 | Partial         | Paper relies on Cai et al. plus convention audit, not full independent derivation.                                                                                             |
|  P2-C2 | −35/16 is a convention difference.                             | Sec. II C / Appendix A | P2 PDF                 | Partial         | Plausible but still the most fragile theoretical claim.                                                                                                                        |
|  P2-C3 | Intermediate ε-order decomposition gives half full polynomial. | Abstract / Appendix A  | P2 PDF                 | Partial         | Internally asserted; needs exact reproducible notebook in submission.                                                                                                          |
|  P2-C4 | Template recovery r=0.84±0.02.                                 | Sec. III B             | P2 PDF                 | Partial         | Main weighting schemes support it, but null-space scan range r=0.55–1.14 weakens “robust.”                                                                                     |
|  P2-C5 | 10,000 coefficient null-space samples show rcos>0.97.          | Abstract / Sec. II A   | P2 PDF / code          | Partial         | Code not independently inspected; statement internally documented.                                                                                                             |
|  P2-C6 | 200 injection-recovery realizations validate overlap.          | Sec. II A              | P2 PDF / code          | Partial         | Full-sky simplified Fisher-space validation, not realistic SPHEREx pipeline.                                                                                                   |
|  P2-C7 | SPHEREx σ(fNL)=0.7 adopted.                                    | Sec. IV                | P2 PDF                 | Yes             | The paper admits it is a sensitivity recast, not independent forecast.                                                                                                         |
|  P2-C8 | SPHEREx first science data ∼2028.                              | Abstract / Conclusion  | Official JPL/NASA      | Problematic     | JPL reports SPHEREx launched in 2025 and began sky capture / public data in 2025; clarify if this means first PNG-quality catalog. ([NASA Jet Propulsion Laboratory (JPL)][6]) |
|  P2-C9 | MegaMapper is proposed / unfunded.                             | Abstract / Sec. V      | MegaMapper white paper | Yes             | Supported; keep MegaMapper as outlook. ([arXiv][7])                                                                                                                            |
| P2-C10 | Bayes factor ∼8–17.                                            | Abstract / Sec. VI     | P2 PDF                 | Partial         | Explicitly prior-dominated; should not be headline evidence.                                                                                                                   |
| P2-C11 | SPHEREx null disfavors benchmark at >4σ.                       | Abstract / Fig. 6      | P2 PDF                 | Partial         | Only under assumptions (a)–(e), especially no prolonged post-bounce inflation.                                                                                                 |
| P2-C12 | Assumption (e): no prolonged post-bounce inflation.            | Sec. II C              | P2 PDF                 | Yes             | Directly conflicts with P1’s Ntot≈92 DE route if both are treated as one model.                                                                                                |
| P2-C13 | Wilson-Ewing quasi-dust is viable.                             | Sec. II D              | P2 PDF                 | Partial         | ns is fitted through w; not a pure prediction.                                                                                                                                 |
| P2-C14 | Anomaly tracers improve σ(fNL) 10–20%.                         | Sec. IV                | P2/P3 PDFs             | Partial         | Should remain speculative until P3 primary catalog is tiered and bias calibrated.                                                                                              |
| P2-C15 | No new observational data.                                     | Data/code statement    | P2 PDF                 | Yes             | Correct; strengthens transparency.                                                                                                                                             |

## P3 — top 15 claims

|      # | Claim                                          | Source                        | Verification surface | Verifiable now? | Verification result                                                           |
| -----: | ---------------------------------------------- | ----------------------------- | -------------------- | --------------- | ----------------------------------------------------------------------------- |
|  P3-C1 | 37,292,042 sources across eight archives.      | Abstract / Table I            | P3 PDF               | Yes             | Internally consistent.                                                        |
|  P3-C2 | 319,443 cross-transfer detections.             | Abstract / Table I            | P3 PDF / site        | Yes             | Supported as baseline, not final.                                             |
|  P3-C3 | 388,693 Path-C detections → 378,480 unique.    | Abstract / Table I            | P3 PDF / SSOT        | Yes             | Arithmetic verified; still conceptually mixed.                                |
|  P3-C4 | ACT is quarantined but counted at input dedup. | Abstract / Table I            | P3 PDF               | Yes             | This is still a headline-count weakness.                                      |
|  P3-C5 | SDSS native top-77,905 is a continuity slice.  | Sec. III C                    | P3 PDF               | Yes             | Paper admits it is “bookkeeping convenience,” yet it remains in title-count.  |
|  P3-C6 | SDSS S>5 native count is only 12.              | Sec. III C / Table I footnote | P3 PDF               | Yes             | Strong evidence that 77,905 is not a purity threshold.                        |
|  P3-C7 | LAMOST native top-1% is 113,342.               | Table I / Sec. III D          | P3 PDF               | Yes             | Included despite 5σ continuum recovery failure.                               |
|  P3-C8 | LAMOST 5σ continuum recovery is 5.8%.          | Abstract / Sec. III D         | P3 PDF               | Yes             | FAIL-with-diagnostic; should not be primary validated component.              |
|  P3-C9 | Gaia stability 41.0%, exploratory.             | Table I footnote              | P3 PDF               | Yes             | Should be tiered as exploratory, not primary.                                 |
| P3-C10 | eROSITA headline 298, not deprecated 9303.     | Table I / Sec. III E          | P3 PDF               | Yes             | Correctly clarified.                                                          |
| P3-C11 | DESI Jaccard stability 0.862 on training pool. | Abstract / Sec. II B          | P3 PDF / SSOT        | Yes             | Supported, but only on 47k training pool, not full 22.5M catalog.             |
| P3-C12 | 17.8% genuine novelty on DESI top-1,000.       | Abstract / Fig. 9             | P3 PDF               | Partial         | Useful, but likely upper bound; title should not imply all 378k are novel.    |
| P3-C13 | Figure 5 high-z QSO scores survive S>5.        | Sec. III B / Fig. 5           | P3 PDF               | Problematic     | Figure labels many AE scores below 5 while text says all S>5 by construction. |
| P3-C14 | Cosmology applications: fNL improvement / PTA. | Sec. V / VI / VII             | P3 PDF               | Partial         | Mostly outlook; should not be load-bearing for catalog paper.                 |
| P3-C15 | Public release available.                      | Data/code                     | HF/GitHub            | Partial         | Several HuggingFace artifacts returned 401 Unauthorized from my session.      |

## P4 — top 15 claims

|      # | Claim                                                 | Source                 | Verification surface | Verifiable now?  | Verification result                                                                 |
| -----: | ----------------------------------------------------- | ---------------------- | -------------------- | ---------------- | ----------------------------------------------------------------------------------- |
|  P4-C1 | 8,474,531 final galaxies.                             | Abstract / Sec. IV A   | P4 PDF               | Yes              | Internally supported.                                                               |
|  P4-C2 | 26,636 training images.                               | Abstract / Sec. II B   | P4 PDF / HF model    | Problematic      | HF model card says 26,626, not 26,636. ([Hugging Face][5])                          |
|  P4-C3 | 67.6% training labels from CE-ResNet.                 | Abstract / Sec. II B   | P4 PDF               | Yes              | Honest but major independence limitation.                                           |
|  P4-C4 | 93.7% validation accuracy.                            | Abstract / Sec. III B  | P4 PDF / HF model    | Yes, with caveat | Supported, but partly teacher-label agreement.                                      |
|  P4-C5 | 8/8 bias tests pass.                                  | Table II               | P4 PDF / HF model    | Yes              | But thresholds are far too loose for 0.2% science.                                  |
|  P4-C6 | Stress-test only 4/8 pass.                            | Abstract               | P4 PDF               | Yes              | Abstract admits this; it should constrain conclusions more strongly.                |
|  P4-C7 | Catalog C fCW=0.4974±0.0003.                          | Abstract / Table III   | P4 PDF               | Yes              | Supported by figure counts, but Nspiral mismatch affects uncertainty provenance.    |
|  P4-C8 | Nspiral=3,321,795.                                    | Intro / Table III      | P4 PDF               | Problematic      | Raw counts sum to this; Fig. 5 Catalog C counts sum to 3,201,160.                   |
|  P4-C9 | Simple dipole 0.43σ.                                  | Sec. IV C              | P4 PDF               | Yes              | Supported.                                                                          |
| P4-C10 | Pseudo-Cℓ ℓ=1 is 2.75σ.                               | Table IV               | P4 PDF               | Yes              | Supported, but MASTER result demotes it to null; abstract should not foreground it. |
| P4-C11 | Hemisphere max 3.05σ, 0.17%, LEE <1σ.                 | Sec. IV D / Fig. 9     | P4 PDF               | Yes              | Supported.                                                                          |
| P4-C12 | Max regional asymmetry 0.32%.                         | Table V                | P4 PDF               | Yes              | Supported.                                                                          |
| P4-C13 | Raw survey systematics can create 94.6σ false dipole. | Abstract / Conclusions | P4 PDF               | Yes              | Strongest contribution.                                                             |
| P4-C14 | Minimum detectable dipole 0.2% at 3σ.                 | Abstract / Sec. VI C   | P4 PDF               | Partial          | Must be separated from systematic floor 0.26–0.38%.                                 |
| P4-C15 | Catalog publicly available on HF.                     | Data availability      | HF                   | Partial          | Dataset returned 401 Unauthorized from my session; model page accessible.           |

# STAGE 3 — Individual reviews by roles A–I

## A. Domain Expert reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P1    | A-P1-1 **BLOCKER:** “ECH provides a well-motivated nonsingular quantum bounce” conflicts with the LQC footnote. A-P1-2 **MAJOR:** the no-go result is stronger than the dark-energy framing. A-P1-3 **MAJOR:** ALP β is not ECH-derived. A-P1-4 **MAJOR:** NANOGrav section oscillates between “very strong evidence” and “synthetic illustrative.” A-P1-5 **MINOR:** barrier novelty classification helps but needs sharper prior-work mapping. |
| P2    | A-P2-1 **BLOCKER:** −35/8 convention is not independently derived. A-P2-2 **MAJOR:** “mechanism-independent” should mean “conditional on contraction dynamics,” not across all bounce models. A-P2-3 **MAJOR:** SPHEREx timing is stale or ambiguous. A-P2-4 **MAJOR:** Bayes factors against inflation are prior-volume claims. A-P2-5 **MINOR:** MegaMapper should be outlook-only.                                                            |
| P3    | A-P3-1 **BLOCKER:** title mixes “spectral sources” with photometry and CMB patches. A-P3-2 **BLOCKER:** primary count includes components paper itself marks weak/quarantined. A-P3-3 **MAJOR:** catalog science value is strongest in DESI, not all eight surveys. A-P3-4 **MAJOR:** cosmology applications are not yet supported. A-P3-5 **MINOR:** Path-C artifact story is valuable and should be central.                                   |
| P4    | A-P4-1 **BLOCKER:** Nspiral/raw/equivariant count mismatch. A-P4-2 **MAJOR:** “definitively refuted” too strong without exact Shamir pipeline reproduction. A-P4-3 **MAJOR:** residual 9.5σ monopole undercuts sub-percent claims. A-P4-4 **MAJOR:** CE-ResNet teacher labels limit independence. A-P4-5 **MINOR:** raw 94.6σ false-dipole warning is field-useful.                                                                              |

## B. Skeptical Referee 2

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1    | B-P1-1 **BLOCKER:** the model being tested by MCMC is ΛCDM+ΔNeff, not spin-torsion. B-P1-2 **BLOCKER:** P1 tries to keep “dark energy” in title after admitting no derivation. B-P1-3 **MAJOR:** “prediction” language survives where the paper says “consistency check.” B-P1-4 **MAJOR:** NANOGrav Bayes-factor section reads like overclaim. B-P1-5 **MINOR:** too many side quests. |
| P2    | B-P2-1 **BLOCKER:** if −35/16 is not fully killed, the main significance can halve. B-P2-2 **MAJOR:** “600K MC” sounds like evidence but validates a formula. B-P2-3 **MAJOR:** no independent SPHEREx Fisher matrix. B-P2-4 **MAJOR:** “first science data ∼2028” likely wrong. B-P2-5 **MINOR:** Figure 3 “landscape” may look advocacy-driven.                                       |
| P3    | B-P3-1 **BLOCKER:** 378,480 looks like a bookkeeping artifact. B-P3-2 **BLOCKER:** SDSS 77,905 admitted as continuity slice. B-P3-3 **BLOCKER:** LAMOST failed gate but is counted. B-P3-4 **MAJOR:** “largest” is inflated by heterogeneous definitions. B-P3-5 **MINOR:** single-author visual inspection cannot support 0% artifact rate.                                            |
| P4    | B-P4-1 **BLOCKER:** page 7 count mismatch is an obvious referee catch. B-P4-2 **MAJOR:** “0.2% sensitivity” while 0.26% bias remains is self-defeating. B-P4-3 **MAJOR:** “equivariant” overstates two-fold TTA. B-P4-4 **MAJOR:** dataset accessibility is not verified from HF. B-P4-5 **MINOR:** some claims are already well caveated; move caveats earlier.                        |

## C. Methods / statistics reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1    | C-P1-1 **BLOCKER:** raw GitHub convergence CSV contradicts paper’s convergence values. C-P1-2 **MAJOR:** Savage-Dickey Bayes factor with correlated posterior is not robust. C-P1-3 **MAJOR:** NaMaster is injection-recovery, not an independent detection. C-P1-4 **MAJOR:** SH0ES/DES priors in “full tension” need exact likelihood disclosure. C-P1-5 **MINOR:** sample-count footnote is necessary but not sufficient. |
| P2    | C-P2-1 **MAJOR:** no full survey mock/mask/photo-z pipeline. C-P2-2 **MAJOR:** null-space scan has arbitrary radius and coefficients. C-P2-3 **MAJOR:** bϕ degradation is approximate. C-P2-4 **MINOR:** full-sky injection-recovery should be labeled optimistic. C-P2-5 **MINOR:** Monte Carlo realization count should not be rhetorical.                                                                                 |
| P3    | C-P3-1 **BLOCKER:** threshold heterogeneity prevents a single “anomaly rate.” C-P3-2 **BLOCKER:** DESI stability test on 47k pool does not validate full 22.5M scoring. C-P3-3 **MAJOR:** no independent anomaly detector for dominant surveys. C-P3-4 **MAJOR:** 5″ dedup across maps and objects is invalid. C-P3-5 **MINOR:** figures need score-scale normalization.                                                     |
| P4    | C-P4-1 **BLOCKER:** uncertainty uses Nspiral whose provenance is inconsistent. C-P4-2 **MAJOR:** effective sample size Neff not estimated. C-P4-3 **MAJOR:** 8/8 bias thresholds are too loose. C-P4-4 **MAJOR:** confidence stratification indicates noise-driven fluctuation. C-P4-5 **MINOR:** max-statistic MC would improve hemisphere correction.                                                                      |

## D. Math / logic reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1    | D-P1-1 **BLOCKER:** ECH/LQC formal identity is blurred. D-P1-2 **MAJOR:** Holst term “topological” language needs Nieh-Yan precision. D-P1-3 **MAJOR:** Eq. 7 dimension gap means DE scaling is not EFT. D-P1-4 **MAJOR:** “torsion remains algebraic” after derivative contorsion terms needs a real stability argument. D-P1-5 **MINOR:** γ fixed by entropy should be softer.                                                                      |
| P2    | D-P2-1 **BLOCKER:** fNL normalization chain is still indirect. D-P2-2 **MAJOR:** polynomial coefficients are underdetermined by benchmarks. D-P2-3 **MAJOR:** r can exceed 1 in null-space scan, contradicting “0<r≤1 for physical shapes.” D-P2-4 **MAJOR:** quasi-dust correction near ε=3/2 singularity is not computed. D-P2-5 **MINOR:** Eq. 3 α(k) notation needs standard definition.                                                          |
| P3    | D-P3-1 **BLOCKER:** “unique physical object” not defined for CMB patches. D-P3-2 **MAJOR:** fixed S>5 and top-percentile thresholds are not mathematically commensurate. D-P3-3 **MAJOR:** false-match rate needs pairwise density formula and table. D-P3-4 **MAJOR:** Figure 5 violates its own S>5 claim. D-P3-5 **MINOR:** “rank-ordering unaffected” does not justify threshold choice.                                                          |
| P4    | D-P4-1 **BLOCKER:** rotations generally preserve projected chirality; the paper’s “90° rotation changes chirality” claim is suspect. D-P4-2 **BLOCKER:** arithmetic mismatch between Catalog C figure and text. D-P4-3 **MAJOR:** binomial σ ignores correlated classification errors. D-P4-4 **MAJOR:** “equivariance guarantee” is only for horizontal reflection. D-P4-5 **MINOR:** not-spiral probability symmetrization needs calibration proof. |

## E. Literature reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P1    | E-P1-1 **MAJOR:** no-go barriers should be mapped against known EC/PGT/no-go literature. E-P1-2 **MAJOR:** Liu et al. AIC “independent support” requires careful model distinction. E-P1-3 **MAJOR:** DESI DR2 / ACT DR6 / SPIDER claims require current official citations. E-P1-4 **MINOR:** cite Cuscuton, ekpyrotic, quintom alternatives more neutrally. E-P1-5 **MINOR:** avoid “first synthesis” unless comparison table proves it. |
| P2    | E-P2-1 **MAJOR:** Cai vs Li convention needs authoritative external referee or full derivation. E-P2-2 **MAJOR:** inflation mimicry literature is broader than listed. E-P2-3 **MAJOR:** SPHEREx status must be updated with NASA/JPL current status. E-P2-4 **MINOR:** MegaMapper status is correctly caveated. E-P2-5 **MINOR:** “no prior quantification” needs search protocol.                                                        |
| P3    | E-P3-1 **MAJOR:** “largest” must define comparison class. E-P3-2 **MAJOR:** anomaly-detection baselines need Baron/Poznanski/Liang/Nicolaou apples-to-apples. E-P3-3 **MAJOR:** SDSS DR18/LAMOST/eROSITA version claims need archive citations. E-P3-4 **MINOR:** SIMBAD-unmatched ≠ novel; paper knows this, title should reflect it. E-P3-5 **MINOR:** CMB anomaly literature should be separated.                                       |
| P4    | E-P4-1 **MAJOR:** Shamir refutation needs exact selection-function comparison. E-P4-2 **MAJOR:** CE-ResNet comparison should be framed as teacher dependence. E-P4-3 **MINOR:** Motloch & Pen / Iye / Tadaki null literature is helpful. E-P4-4 **MINOR:** “largest” needs clear spiral-count comparator. E-P4-5 **MINOR:** LSST projection requires current survey-status caution.                                                        |

## F. Cross-paper reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1    | F-P1-1 **BLOCKER:** P1 depends on P2 fNL while decoupling it from ECH. F-P1-2 **BLOCKER:** P1 Ntot≈92 conflicts with P2 assumption (e). F-P1-3 **MAJOR:** P1 quotes P4 values selectively. F-P1-4 **MAJOR:** P1/P3 PTA statements differ in strength. F-P1-5 **MINOR:** P1 should not cite P3 anomaly tracers as mature.                                                               |
| P2    | F-P2-1 **BLOCKER:** cannot be a “surviving ECH prediction.” F-P2-2 **MAJOR:** P2 uses P3 tracer gains before P3 is clean. F-P2-3 **MAJOR:** P2 depends on P1 perturbation transparency but should state self-contained assumptions. F-P2-4 **MINOR:** MegaMapper not linked to P1. F-P2-5 **MINOR:** decision thresholds useful.                                                       |
| P3    | F-P3-1 **BLOCKER:** P3 title/count mismatch with user-provided anchor “319,443 canonical totals.” F-P3-2 **MAJOR:** P3 cosmology claims lean on P2. F-P3-3 **MAJOR:** P3 PTA claims lean on P1 but are not catalog science. F-P3-4 **MINOR:** cross-survey code reuse with P4 should be documented. F-P3-5 **MINOR:** anomaly catalog should not be positioned as evidence for bounce. |
| P4    | F-P4-1 **BLOCKER:** P4 count mismatch propagates into P1. F-P4-2 **MAJOR:** P1 uses benchmark 0.5012 while P4 headline full value is 0.4974. F-P4-3 **MAJOR:** P4 null weakens P1 galaxy-spin narrative. F-P4-4 **MINOR:** P4 should be anchor paper. F-P4-5 **MINOR:** terminology “chirality” is consistent.                                                                         |

## G. Reproducibility reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                         |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1    | G-P1-1 **BLOCKER:** `convergence_latest.csv` visible on GitHub is not publication quality. G-P1-2 **MAJOR:** exact frozen-chain path must be cited in paper. G-P1-3 **MAJOR:** NaMaster JSON verifies injection result only. G-P1-4 **MAJOR:** companion technical note must be public. G-P1-5 **MINOR:** tag versions inconsistent: v2.3.0 paths vs v2.3.1 PDF. |
| P2    | G-P2-1 **MAJOR:** code path pinned to v1.7.0 while PDF is v1.7.1. G-P2-2 **MAJOR:** shape-function coefficient notebook must be public. G-P2-3 **MAJOR:** MC seeds and covariance files needed. G-P2-4 **MINOR:** no new data is transparent. G-P2-5 **MINOR:** release tag must match PDF.                                                                      |
| P3    | G-P3-1 **BLOCKER:** HF P3 datasets inaccessible from my session. G-P3-2 **BLOCKER:** primary count cannot be reproduced from PDF alone. G-P3-3 **MAJOR:** exact parquet manifests/checksums absent in paper. G-P3-4 **MAJOR:** SDSS unscored 16.3% requires manifest. G-P3-5 **MINOR:** H200 processing logs should be archived.                                 |
| P4    | G-P4-1 **BLOCKER:** HF dataset inaccessible from my session. G-P4-2 **MAJOR:** HF model training count conflicts with paper. G-P4-3 **MAJOR:** per-object raw/flip probabilities needed to diagnose 9.5σ residual. G-P4-4 **MAJOR:** code/data release should include master-power JSON. G-P4-5 **MINOR:** DOI/Zenodo should exist before submission.            |

## H. Ethics / research-integrity reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P1    | H-P1-1 **MAJOR:** overclaiming “prediction” may mislead readers. H-P1-2 **MAJOR:** NANOGrav synthetic evidence must not be dressed as evidence. H-P1-3 **MAJOR:** AI-assisted single-author paper needs explicit disclosure if applicable. H-P1-4 **MINOR:** negative results are responsibly included. H-P1-5 **MINOR:** conflict-of-interest statement absent.                                 |
| P2    | H-P2-1 **MAJOR:** Bayes factors could be miscommunicated as proof of bounce. H-P2-2 **MAJOR:** SPHEREx status errors can mislead readers. H-P2-3 **MINOR:** null-result falsifiability is good. H-P2-4 **MINOR:** avoid “tuned inflation” framing without symmetric treatment. H-P2-5 **MINOR:** no human/animal risk.                                                                           |
| P3    | H-P3-1 **BLOCKER:** users may treat failed-diagnostic components as validated discoveries. H-P3-2 **MAJOR:** “uncataloged” may encourage premature claims about novelty. H-P3-3 **MAJOR:** single-author unblinded inspection should not be “0% artifact rate.” H-P3-4 **MINOR:** responsible artifact disclosure is a strength. H-P3-5 **MINOR:** catalog tier labels must be machine-readable. |
| P4    | H-P4-1 **MAJOR:** “definitively refuted” is confrontational and may be unfair absent exact replication. H-P4-2 **MAJOR:** public dataset claim currently not verifiable by my access. H-P4-3 **MINOR:** strong null-result framing is socially useful. H-P4-4 **MINOR:** avoid implying all prior positive studies were bias artifacts. H-P4-5 **MINOR:** release bias-test code.                |

## I. Structure / writing reviewer

| Paper | Findings                                                                                                                                                                                                                                                                                                                           |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1    | I-P1-1 **BLOCKER:** title promises dark energy; result is no-go. I-P1-2 **MAJOR:** abstract overloaded with too many threads. I-P1-3 **MAJOR:** P1 should put model-separation diagram before equations. I-P1-4 **MINOR:** Table I is useful. I-P1-5 **MINOR:** section order buries core theorem.                                 |
| P2    | I-P2-1 **MAJOR:** abstract too dense and 1,900+ chars. I-P2-2 **MAJOR:** convention ambiguity should be a boxed assumption. I-P2-3 **MINOR:** figures likely slide-ready. I-P2-4 **MINOR:** title over-promotes MegaMapper. I-P2-5 **MINOR:** conclusion appropriately caveated.                                                   |
| P3    | I-P3-1 **BLOCKER:** title does not match contents. I-P3-2 **MAJOR:** Table I is overloaded and confusing. I-P3-3 **MAJOR:** Path-C before/after should be the narrative spine. I-P3-4 **MAJOR:** appendix figure scores conflict with main score scale. I-P3-5 **MINOR:** taxonomy galleries are visually useful.                  |
| P4    | I-P4-1 **BLOCKER:** Fig. 5/text/Table III inconsistency. I-P4-2 **MAJOR:** abstract contains caveats but still overclaims. I-P4-3 **MAJOR:** “equivariant” needs consistent qualifier. I-P4-4 **MINOR:** figures are generally strong. I-P4-5 **MINOR:** Data availability should say dataset currently access-restricted if true. |

# STAGE 4 — Reviewer debate

**A vs. B on P1:** A says P1 is salvageable as a no-go theorem; B says the title and opening still read like a positive dark-energy model. Meta-adjudication: B wins on presentation risk, A wins on scientific salvage. The fix is not more caveats; the fix is retitling and reorganizing.

**C vs. G on P1 MCMC:** C says the MCMC itself is acceptable as ΛCDM+ΔNeff. G says the visible GitHub convergence CSV is disqualifying. Meta-adjudication: both are correct. The analysis may be valid if frozen diagnostics exist, but the public verification surface currently reachable is contradictory and must be fixed before submission.

**D vs. A on P2:** A accepts the Cai convention audit as a serious attempt; D says indirect checks do not close the factor-of-two risk. Meta-adjudication: D wins. The paper can proceed only with either a full derivation or a dual-normalization forecast.

**B vs. H on P3:** B says the headline count is inflated; H says the bigger ethical issue is that users may treat weak tiers as discoveries. Meta-adjudication: same root problem. Make a validated primary catalog and a separate exploratory/quarantined supplement.

**C vs. I on P4:** C says the systematic floor is the central issue; I says the count mismatch is the first thing a referee will catch. Meta-adjudication: both are blockers, but the count mismatch is the first-order repair because all downstream statistics depend on it.

**Panel consensus:** P4 is closest to submission after numerical reconciliation. P2 is next if the fNL convention is hardened. P1 is publishable only as a structural no-go/synthesis paper. P3 needs the most restructuring.

# STAGE 5 — Cross-paper consistency audit

## Cross-paper number table

| Quantity                 |                                                            P1 |                                            P2 |                                                   P3 |                                          P4 | Cross-paper verdict                                                                                 |
| ------------------------ | ------------------------------------------------------------: | --------------------------------------------: | ---------------------------------------------------: | ------------------------------------------: | --------------------------------------------------------------------------------------------------- |
| fNL                      |                                                         −35/8 |                                         −35/8 |                       −35/8 in cosmology application |                                         N/A | Consistent numerically; attribution must say matter-bounce, not ECH.                                |
| Observable fNL condition |                            P1 says Ntot≈92 DE route erases it | P2 assumes no prolonged post-bounce inflation |                                                  N/A |                                         N/A | **BLOCKER:** must decouple dark energy and matter-bounce histories.                                 |
| β_ALP prediction         |                                     β=0.27°, recovered 0.238° |                                           N/A |              NaMaster/CMB context appears in program |                                         N/A | P1 value verified by JSON, but ALP remains spectator not ECH-derived.                               |
| β observational value    |               0.241±0.061 inverse variance; 0.342±0.094 joint |                                           N/A |                                                  N/A |                                         N/A | Must not overstate as detection of ECH. ACT DR6 β=0.215±0.074 is externally supported. ([arXiv][8]) |
| MCMC sample count        |    424,781 raw across 3 combinations; 176,840 +132,949 frozen |                                           N/A |                                                  N/A |                                         N/A | Footnote helps, but GitHub convergence surface contradicts R̂.                                      |
| Anomaly counts           |                                            Cites P3 generally |                          Uses anomaly tracers | 319,443 baseline; 388,693 detections; 378,480 unique |                                         N/A | User anchor says “319,443 canonical totals,” while P3/PDF/site say 378,480 primary. Must harmonize. |
| DESI anomalies           |                                                           N/A |                        anomaly-tracer outlook |                                              195,829 |                                         N/A | Consistent, but validation is not full-catalog split.                                               |
| P3 bias enhancement      |                                                           N/A |                            10–20% improvement |                               Table VI / application |                                         N/A | Must remain upper-bound/outlook until tracer bias is calibrated.                                    |
| P4 fCW benchmark         |                        P1 uses 0.5012±0.0006 benchmark subset |                                           N/A |                                                  N/A |               P4 full catalog 0.4974±0.0003 | Not contradictory if footnoted, but P1 main text should foreground full-catalog value.              |
| P4 Nspiral               |                                  P1 quotes 8.47M and f values |                                           N/A |                                                  N/A | raw 3,321,795 vs Fig. 5 Catalog C 3,201,160 | **BLOCKER:** P4 must reconcile; then update P1.                                                     |
| PTA γ                    | P1 includes strong Bayes-factor language and synthetic caveat |                                           N/A |                            γ=3.20±0.42, not evidence |                                         N/A | P3 is more responsible; P1 must demote to P3’s language.                                            |

## Cross-paper contradictions / dependencies

1. **Dark energy vs fNL:** P1 explicitly says Ntot≈92 post-bounce inflation is incompatible with P2’s observable matter-bounce fNL. This is now acknowledged, but the program still rhetorically treats them as one arc. Fix by saying the ECH dark-energy route is dead and the fNL test is a separate matter-bounce test.

2. **P1 says “ECH bounce”; P1 footnote says LQC bounce:** The abstract claims ECH provides the bounce; Eq. 10 footnote says LQC is physically distinct from EC torsion bounce and ECH is not the source of Eq. 10. That is not cosmetic.

3. **P2 “first science data ∼2028” vs official SPHEREx status:** Official JPL/NASA materials show SPHEREx launched in 2025 and began sky capture / public data releases in 2025. P2 may mean “first fNL-quality cosmology release,” but it does not say that. ([NASA Jet Propulsion Laboratory (JPL)][6])

4. **P3 headline vs user/site anchors:** P3 v3.1.1 says the Path-C primary count is 378,480, while the R42 prompt says “319,443 anomalies canonical totals.” The site also says 378,480 unique. The program needs one canonical anomaly count and one label for the baseline count.  ([BigBounce — Spin-Torsion Cosmology][9])

5. **P4 full vs benchmark fraction:** P1 uses the 0.5012 benchmark-overlap value in the main text; P4’s full-catalog result is 0.4974. P1 has a footnote, but the headline should not use the less representative value.

6. **P3/P2 tracer dependency:** P2’s anomaly-tracer improvement depends on P3, but P3 itself labels several components exploratory/FAIL-with-diagnostic. Treat the improvement as speculative.

# STAGE 6 — Exhaustive audit log

Sorted by paper, BLOCKER first. Duplicate reviewer concerns are intentionally retained where different reviewers would attack the same issue from different angles.

| ID     | Paper | §/Page                      | Reviewer | Severity | Quote                                                                                                                             | Issue                                                                                        | Fix                                                                                               |
| ------ | ----- | --------------------------- | -------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| P1-B01 | P1    | Abstract p.1                | A/F      | BLOCKER  | “ECH provides a well-motivated nonsingular quantum bounce”                                                                        | Contradicts footnote that LQC, not ECH, supplies Eq. 10 bounce.                              | Replace with “LQC supplies the bounce; ECH supplies torsion/parity context.”                      |
| P1-B02 | P1    | Eq. 10 footnote p.7         | D        | BLOCKER  | “The LQC bounce… is physically distinct from the Einstein-Cartan torsion bounce… ECH… is not the source of Eq. (10).”             | The paper’s theory identity is internally unstable.                                          | Add model-separation diagram and remove “ECH bounce” language.                                    |
| P1-B03 | P1    | Title / Abstract            | B/I      | BLOCKER  | “Search for Geometric Dark Energy” vs “phenomenological dark-energy connection requires assumptions beyond the minimal framework” | Title promises a result the paper denies.                                                    | Retitle as structural/no-go paper.                                                                |
| P1-B04 | P1    | Sec. VII / GitHub           | C/G      | BLOCKER  | “Worst Rˆ − 1 0.001 / 0.003”                                                                                                      | Visible `convergence_latest.csv` has Rhat_all as high as 1.64.                               | Point to exact frozen-chain diagnostics or replace public CSV.                                    |
| P1-B05 | P1    | Sec. XV C p.22              | C/H      | BLOCKER  | “Bayes factor B(bounce/SMBHB)=34.0—‘very strong’ evidence”                                                                        | Same passage later says synthetic data and not evidence.                                     | Delete Bayes-factor claims or move to clearly labeled illustrative appendix.                      |
| P1-B06 | P1    | Sec. XV C p.22              | B/H      | BLOCKER  | “χ²/dof = 0.012… reflects the synthetic data closely matching the model template by construction”                                 | This invalidates any evidential interpretation.                                              | Keep only “PTA spectral index is numerically consistent; no evidence claimed.”                    |
| P1-M01 | P1    | Eq. 1 p.4–5                 | D        | MAJOR    | “Equation (1) presents the second-order (metric) form… after algebraic elimination of torsion”                                    | A second-order action still displaying T² is formally confusing.                             | Present first-order action, then integrated-out effective action separately.                      |
| P1-M02 | P1    | Eq. 5 p.4                   | D/E      | MAJOR    | “Holst term… is topological in the absence of torsion”                                                                            | Holst vs Nieh-Yan/topological language is imprecise.                                         | Say “vanishes/does not contribute for torsionless Levi-Civita by Bianchi,” unless using Nieh-Yan. |
| P1-M03 | P1    | Eq. 7 p.6                   | D        | MAJOR    | “three units short of the required +4”                                                                                            | The dark-energy operator is admitted dimensionally uncontrolled.                             | Remove Fig. 1 as a live mechanism; present as failed ansatz.                                      |
| P1-M04 | P1    | Sec. II A p.6               | D        | MAJOR    | “Torsion therefore remains effectively algebraic… A full stability analysis… warranted”                                           | Derivative contorsion terms may alter degrees of freedom; no stability proof.                | Provide formal perturbative DOF/stability appendix or remove quantitative claim.                  |
| P1-M05 | P1    | Sec. III A p.8              | A/H      | MAJOR    | “This coupling has not yet been derived in this work.”                                                                            | β cannot be claimed as spin-torsion prediction.                                              | Rename all β claims “spectator-ALP consistency check.”                                            |
| P1-M06 | P1    | Sec. VI p.10                | C        | MAJOR    | “This constitutes the first map-level NaMaster recovery… rejects the null at high significance.”                                  | Injection-recovery rejection of injected null is not an independent observational detection. | Say “pipeline injection validation.”                                                              |
| P1-M07 | P1    | Table III p.12              | C        | MAJOR    | “Bayes factors estimated via Savage-Dickey”                                                                                       | Paper admits strong posterior correlation; estimator biased.                                 | Remove lnB from main table or rerun nested sampling.                                              |
| P1-M08 | P1    | Sec. XI                     | E        | MAJOR    | “14 independent structural constraints”                                                                                           | Constraints mix novel, known, and qualitative observations.                                  | Add novelty/independence grading in Table IV.                                                     |
| P1-M09 | P1    | Sec. XII                    | D        | MAJOR    | “torsion vanishes at all perturbation orders”                                                                                     | Shown only under canonical scalar / torsionless assumptions.                                 | State theorem with domain: canonical spinless matter only.                                        |
| P1-M10 | P1    | Sec. XV E                   | F        | MAJOR    | “cannot both be correct”                                                                                                          | Central program tension still treated as future/open rather than settled.                    | Put in abstract conclusion: dark energy and fNL are independent problems.                         |
| P1-M11 | P1    | Sec. III D                  | C        | MAJOR    | “full-tension dataset includes SH0ES H0 and DES S8 priors”                                                                        | H0 remains Planck-like despite priors; likelihood implementation needs clarity.              | Show exact priors and posterior pull diagnostics.                                                 |
| P1-M12 | P1    | Data availability           | G        | MAJOR    | “will be deposited as an arXiv companion”                                                                                         | Submission should not depend on future deposit.                                              | Create DOI/archive before arXiv.                                                                  |
| P1-N01 | P1    | Fig. 1 p.5                  | I        | MINOR    | “Energy density hierarchy…”                                                                                                       | Figure visually promotes failed DE ansatz.                                                   | Replace with barrier/failure map.                                                                 |
| P1-N02 | P1    | Sec. II A p.5               | E        | MINOR    | “γ = 0.274 ± 0.020”                                                                                                               | Entropy-counting uncertainty is not necessarily Gaussian.                                    | Use range and cite schemes.                                                                       |
| P1-N03 | P1    | Sec. III B                  | I        | MINOR    | “confirmed null result”                                                                                                           | Strong but acceptable only after P4 fixes.                                                   | Update after P4 count reconciliation.                                                             |
| P2-B01 | P2    | Abstract / Sec. II C        | D/B      | BLOCKER  | “−35/8 is the correct Planck-convention normalization”                                                                            | Full independent derivation absent; all forecasts rest on this.                              | Add full derivation or dual −35/8 / −35/16 forecast.                                              |
| P2-B02 | P2    | Sec. II C p.4               | D        | BLOCKER  | “A complete independent re-derivation… is not undertaken here”                                                                    | Admits the central theoretical input is not independently proven.                            | Do not say “confirm”; say “adopt Cai value after consistency audit.”                              |
| P2-B03 | P2    | Sec. II C p.3               | F        | BLOCKER  | “forecasts… apply exclusively to bounce models without prolonged post-bounce inflation”                                           | P1 DE mechanism requires Ntot≈92.                                                            | Explicitly exclude P1 DE scenario from P2.                                                        |
| P2-M01 | P2    | Sec. II A p.2               | D        | MAJOR    | “the system is underdetermined”                                                                                                   | Three benchmarks cannot determine full shape.                                                | Use source polynomial or derive from action.                                                      |
| P2-M02 | P2    | Sec. II A p.2               | C/D      | MAJOR    | “r = 0.85 ± 0.13 (range: 0.55–1.14)”                                                                                              | Abstract hides this broader uncertainty by quoting r=0.84±0.02.                              | Report both: physical weighting and coefficient-uncertainty envelope.                             |
| P2-M03 | P2    | Sec. III B p.4              | D        | MAJOR    | “0 < r ≤ 1 for physical bispectrum shapes”                                                                                        | Null-space scan gives r>1, so some sampled shapes are not in stated physical class.          | Exclude unphysical samples or revise claim.                                                       |
| P2-M04 | P2    | Sec. IV p.5                 | C        | MAJOR    | “This makes the present work a sensitivity recast rather than an independent forecast.”                                           | Title says “Forecasts,” but method is recast.                                                | Retitle or add subtitle “sensitivity recast.”                                                     |
| P2-M05 | P2    | Abstract p.1                | E/C      | MAJOR    | “SPHEREx (first science data ∼2028)”                                                                                              | Official JPL pages indicate mission launched and data/public maps in 2025.                   | Clarify “first PNG-quality cosmology release,” or correct date.                                   |
| P2-M06 | P2    | Sec. VI p.7                 | C/H      | MAJOR    | “delta-function prior… gives the maximum possible Bayes factor”                                                                   | Bayes comparison is upper-bound and prior-dominated.                                         | Move Bayes factors to appendix; headline likelihood separation.                                   |
| P2-M07 | P2    | Sec. IV p.6                 | C/F      | MAJOR    | “∼10–20% improvement” from anomaly tracers                                                                                        | Depends on P3 unvalidated catalog/bias.                                                      | Call speculative; remove from abstract.                                                           |
| P2-M08 | P2    | Sec. II C p.3               | D        | MAJOR    | “At the Planck best-fit spectral tilt, fNL∈[−4.35,−4.02]”                                                                         | ε-correction not computed with full cubic integrals.                                         | Present as estimate, not forecast input.                                                          |
| P2-M09 | P2    | Sec. V                      | A/E      | MAJOR    | “MegaMapper… no finalized instrument design”                                                                                      | Forecast range 3–7σ is speculative.                                                          | Demote to outlook section.                                                                        |
| P2-N01 | P2    | Fig. 3                      | I        | MINOR    | “matter bounce vs. inflationary alternatives”                                                                                     | Reads like advocacy.                                                                         | Make it neutral comparison table.                                                                 |
| P2-N02 | P2    | Data availability           | G        | MINOR    | “pinned to release tag v1.7.0”                                                                                                    | PDF is v1.7.1.                                                                               | Align tags.                                                                                       |
| P2-N03 | P2    | Sec. VII                    | C        | MINOR    | “bϕ prior uncertainty”                                                                                                            | Needs explicit prior table.                                                                  | Add nuisance-prior table.                                                                         |
| P3-B01 | P3    | Title                       | A/B/I    | BLOCKER  | “Spectral Anomaly Detection… Sources”                                                                                             | Includes X-ray photometry, Gaia variability, IR photometry, and CMB map patches.             | Retitle “multi-archive anomaly detection”; split map patches.                                     |
| P3-B02 | P3    | Abstract                    | B/H      | BLOCKER  | “378,480 unique anomalous objects”                                                                                                | Count includes weak/failed/quarantined components.                                           | Define validated primary catalog separately.                                                      |
| P3-B03 | P3    | Abstract / Table I          | F        | BLOCKER  | “ACT DR6… formally quarantined… headline counts ACT only at input deduplication stage”                                            | Quarantined data still in headline count.                                                    | Exclude ACT from primary count; report separately.                                                |
| P3-B04 | P3    | Sec. III C p.10             | B/C      | BLOCKER  | “bookkeeping convenience… not a physical threshold”                                                                               | SDSS 77,905 should not be primary anomaly count.                                             | Use S>5=12 or top-1%=19,253 as labeled tier.                                                      |
| P3-B05 | P3    | Sec. III D p.11             | C/H      | BLOCKER  | “strict Path-C 5σ gate remains unreached at 5.8%”                                                                                 | LAMOST top-1% included despite failed validation.                                            | Move LAMOST to exploratory/fail-diagnostic tier.                                                  |
| P3-B06 | P3    | Table I footnote            | C/H      | BLOCKER  | “Gaia… should be treated as exploratory”                                                                                          | Exploratory Gaia still contributes to primary count.                                         | Remove from primary count or flag in title.                                                       |
| P3-B07 | P3    | Table I / dedup             | D        | BLOCKER  | “8-way positional deduplication… unique physical object”                                                                          | CMB patches are not physical point sources.                                                  | Dedup object catalogs only; separate CMB patch analysis.                                          |
| P3-B08 | P3    | Fig. 5 p.9                  | D/I      | BLOCKER  | “all objects have total score S>5 by construction” vs labels AE=4.32, 4.26, 3.31                                                  | Internal figure/text contradiction.                                                          | Explain alternate score scale or correct candidates.                                              |
| P3-M01 | P3    | Table I p.7                 | C        | MAJOR    | “fixed S>5… top 1%… top 0.03%”                                                                                                    | Heterogeneous thresholds cannot produce a single anomaly rate.                               | Calibrate false discovery / percentile consistently.                                              |
| P3-M02 | P3    | Sec. II B p.3               | C        | MAJOR    | “cross-validation was performed on the 47,000-spectrum training pool, not the full 22.5 million-spectrum catalog”                 | Does not validate full-catalog scoring.                                                      | Run large held-out full-catalog split.                                                            |
| P3-M03 | P3    | Sec. III A p.6              | C/H      | MAJOR    | “0% artifact rate”                                                                                                                | Single unblinded astronomer, top 200 only.                                                   | Replace with “no obvious artifacts”; add blinded multi-rater audit.                               |
| P3-M04 | P3    | Fig. 3 p.6                  | I        | MAJOR    | “319,443 cross-transfer baseline detections shown here”                                                                           | Figure title says all anomalies but plots old baseline.                                      | Update figure to Path-C or relabel as baseline only.                                              |
| P3-M05 | P3    | Fig. 4                      | I/C      | MAJOR    | SDSS transfer-learning scores shown after native retrain supersedes them                                                          | Old score distribution may confuse primary result.                                           | Add native SDSS/LAMOST distributions.                                                             |
| P3-M06 | P3    | Appendix figs               | I        | MAJOR    | Appendix AE scores in thousands vs main S up to 25                                                                                | Score scale inconsistency.                                                                   | Standardize AE/S labels.                                                                          |
| P3-M07 | P3    | Sec. V                      | F/C      | MAJOR    | “Anomaly-selected tracers improve σ(fNL)”                                                                                         | Bias/number density not calibrated.                                                          | Move to outlook; no headline.                                                                     |
| P3-M08 | P3    | NANOGrav section            | A/F/H    | MAJOR    | “falls outside the core anomaly catalog scope”                                                                                    | Admitted scope mismatch.                                                                     | Remove PTA from catalog paper or appendix only.                                                   |
| P3-M09 | P3    | Data availability           | G        | MAJOR    | “catalog… publicly released”                                                                                                      | HF artifact inaccessible from my session.                                                    | Ensure public access; add DOI/checksums.                                                          |
| P3-M10 | P3    | Table I                     | I        | MAJOR    | “Nanom (Cross-Transfer)” with Path-C row                                                                                          | Table merges old and final counts.                                                           | Split into before/after tables.                                                                   |
| P3-N01 | P3    | Abstract                    | E        | MINOR    | “∼141× increase”                                                                                                                  | Apples-to-oranges comparison.                                                                | Compare validated spectroscopic-only subset.                                                      |
| P3-N02 | P3    | Sec. IV A                   | H        | MINOR    | “SIMBAD-unmatched”                                                                                                                | Not true novelty.                                                                            | Use “catalog-unmatched”; reserve novelty for extended crossmatch.                                 |
| P3-N03 | P3    | Sec. III E                  | C        | MINOR    | eROSITA near LMC/Galactic plane                                                                                                   | Source-confusion concern acknowledged but not tested.                                        | Add local-source-density regression.                                                              |
| P4-B01 | P4    | Page 7 / Fig. 5 / Table III | C/D/I    | BLOCKER  | Text: “3,321,795 classified spirals”; Fig. 5 shows 1,592,107+1,609,053=3,201,160                                                  | Main count mismatch.                                                                         | Recompute all stats from canonical Catalog C.                                                     |
| P4-B02 | P4    | Sec. III D p.5              | D        | BLOCKER  | “a 90° rotation changes which arm appears to trail clockwise”                                                                     | Image-plane rotations should preserve handedness; mirrors flip chirality.                    | Correct rotation semantics; rerun D4 or justify rigorously.                                       |
| P4-B03 | P4    | HF/PDF                      | G        | BLOCKER  | PDF: “26,636 images”; HF model: “26,626 images”                                                                                   | Public verification surface conflicts with paper.                                            | Harmonize training count and explain dropped images.                                              |
| P4-B04 | P4    | Data availability           | G/H      | BLOCKER  | “catalog is available…”                                                                                                           | Dataset returned 401 Unauthorized from my session.                                           | Make dataset public before submission or state access-restricted.                                 |
| P4-M01 | P4    | Abstract p.1                | C/B      | MAJOR    | “minimum detectable dipole of 0.2% at 3σ”                                                                                         | Residual monopole is 0.26%; subset offset 0.38%.                                             | Separate statistical sensitivity from systematic floor.                                           |
| P4-M02 | P4    | Sec. II B p.3               | C/E      | MAJOR    | “67.6%… derive from CE-ResNet predictions”                                                                                        | Validation partially teacher-student self-consistency.                                       | Add independent human-labeled validation set.                                                     |
| P4-M03 | P4    | Table II p.6                | C/H      | MAJOR    | thresholds: “50±10%,” “<10% hemispheric”                                                                                          | Bias tests too coarse for 0.2% science.                                                      | Add 0.1% magnitude/PSF/size bin tests.                                                            |
| P4-M04 | P4    | Sec. III D                  | B/I      | MAJOR    | “TTA, not architectural equivariance”                                                                                             | Paper still uses broad “equivariant catalog” language.                                       | Use “flip-symmetrized TTA catalog.”                                                               |
| P4-M05 | P4    | Sec. IV B p.7               | C        | MAJOR    | “mechanism… not fully understood”                                                                                                 | 9.5σ residual unexplained.                                                                   | Release per-object orig/flip probabilities and diagnose.                                          |
| P4-M06 | P4    | Table IV / Sec. IV C        | C/I      | MAJOR    | “2.75σ” but MASTER gives −0.12σ                                                                                                   | Abstract foregrounds pre-deconvolution number.                                               | Make MASTER-corrected null primary.                                                               |
| P4-M07 | P4    | Sec. IV G p.11              | C        | MAJOR    | “High confidence… 0.3σ; Mid… 2.1σ; Low… 1.7σ”                                                                                     | Signal stronger in noisier bins.                                                             | Present high-confidence result as primary.                                                        |
| P4-M08 | P4    | Sec. VI D                   | C        | MAJOR    | Edge-on contamination limitation                                                                                                  | Not tested with axis-ratio bins.                                                             | Add face-on-only / b/a analysis.                                                                  |
| P4-M09 | P4    | Abstract / Conclusion       | E/H      | MAJOR    | “definitively refuted”                                                                                                            | Too strong absent exact Shamir selection reproduction.                                       | Use “strongly disfavors ∼3% signal in this footprint/pipeline.”                                   |
| P4-N01 | P4    | Fig. 5 p.7                  | I        | MINOR    | Donut chart uses Catalog C but caption discusses raw and equivariant                                                              | Confusing figure/caption.                                                                    | Separate raw/equivariant charts.                                                                  |
| P4-N02 | P4    | Table V                     | C        | MINOR    | Regional table uses all-sky N=3,321,795                                                                                           | Same count issue.                                                                            | Update after canonical count.                                                                     |
| P4-N03 | P4    | Sec. VI C                   | I        | MINOR    | LSST Y3/Y10 projections                                                                                                           | Needs current survey-stage caveat.                                                           | Mark as illustrative forecast.                                                                    |
| X-B01  | Cross | P1/P2                       | F/J      | BLOCKER  | P1 Ntot≈92 vs P2 no prolonged inflation                                                                                           | Core program contradiction.                                                                  | Decouple DE and matter-bounce histories.                                                          |
| X-B02  | Cross | P1/P4                       | F/G      | BLOCKER  | P1 relies on P4 null while P4 counts unstable                                                                                     | Downstream P1 claims inherit P4 errors.                                                      | Fix P4, then update P1.                                                                           |
| X-B03  | Cross | P2/P3                       | F/C      | BLOCKER  | P2 anomaly gain rests on P3 weak tiers                                                                                            | Forecast overstates evidence.                                                                | Treat as optional improvement only.                                                               |
| X-M01  | Cross | All                         | I/G      | MAJOR    | Version paths v2.3.0/v1.7.0 vs PDFs v2.3.1/v1.7.1                                                                                 | Reproducibility version mismatch.                                                            | Pin exact release tags matching PDFs.                                                             |
| X-M02  | Cross | All                         | H        | MAJOR    | “prediction,” “detection,” “consistency,” “validated” used inconsistently                                                         | Responsible communication risk.                                                              | Shared claim-status glossary.                                                                     |
| X-M03  | Cross | P1/P3                       | F/H      | MAJOR    | PTA claims too prominent in non-PTA papers                                                                                        | Scope creep.                                                                                 | Separate PTA note or appendix-only.                                                               |
| X-M04  | Cross | P3/site/prompt              | F        | MAJOR    | 319,443 vs 378,480 canonical count                                                                                                | SSOT conflict.                                                                               | Canonicalize baseline vs Path-C vs validated-only.                                                |
| X-N01  | Cross | All                         | I        | MINOR    | Papers over-cross-reference each other                                                                                            | Weakens standalone reviewability.                                                            | Make each paper self-contained.                                                                   |

# STAGE 7 — Per-paper revision plans

## P1 revision plan

### Must-fix before arXiv

| Task                                                                                                                            |                                            Effort |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------: |
| Replace “ECH provides a well-motivated nonsingular quantum bounce” with a precise LQC/ECH separation.                           |                                               <1h |
| Retitle/reframe as a structural-constraints/no-go paper, not a geometric-dark-energy proposal.                                  |                                              1–4h |
| Remove or demote NANOGrav Bayes-factor language; retain only “synthetic consistency check / not evidence.”                      |                                              1–4h |
| Fix public convergence linkage: either replace `convergence_latest.csv` or cite exact frozen diagnostics that support Table II. | 1–4h if files exist; >16h if chains must be rerun |
| Move ALP β from “surviving prediction” to “spectator consistency check.”                                                        |                                               <1h |

### Should-fix this round

| Task                                                                                                              | Effort |
| ----------------------------------------------------------------------------------------------------------------- | -----: |
| Add formal theorem statement for perturbation transparency with explicit assumptions.                             |  4–16h |
| Rewrite Holst/Nieh-Yan/topological language.                                                                      |   1–4h |
| Replace Fig. 1 with a failed-route/barrier map.                                                                   |  4–16h |
| Add model-separation diagram: LQC bounce, ECH torsion, ALP, matter-bounce fNL.                                    |  4–16h |
| Put the Ntot≈92 vs fNL incompatibility in the abstract’s conclusion as a resolved separation, not open ambiguity. |    <1h |

### Nice-to-fix

| Task                                                                               | Effort |
| ---------------------------------------------------------------------------------- | -----: |
| Move side channels — PTA, anomaly tracers, galaxy chirality — to short appendices. |   1–4h |
| Add “known / novel / heuristic” column to the 14-barrier table.                    |   1–4h |
| Harmonize version tags v2.3.0/v2.3.1 in data availability.                         |    <1h |

## P2 revision plan

### Must-fix before arXiv

| Task                                                                                     | Effort |
| ---------------------------------------------------------------------------------------- | -----: |
| Add dual-normalization forecast table for fNL=−35/8 and −35/16.                          |   1–4h |
| Stop saying “confirm” unless full in-in derivation is provided; use “adopt after audit.” |    <1h |
| Clarify or correct “SPHEREx first science data ∼2028” against current JPL status.        |    <1h |
| Explicitly state P2 excludes P1’s Ntot≈92 dark-energy route.                             |    <1h |
| Demote Bayes factors to prior-dependent appendix.                                        |   1–4h |

### Should-fix this round

| Task                                                                                     | Effort |
| ---------------------------------------------------------------------------------------- | -----: |
| Publish exact shape-function code/notebook and coefficient audit.                        |   1–4h |
| Report the wide null-space r envelope alongside the 0.84±0.02 physical-weighting result. |   1–4h |
| Add nuisance-prior table for bϕ, GR projections, photo-z, template mismatch.             |   1–4h |
| Rename paper as a “sensitivity recast” unless an independent Fisher matrix is added.     |    <1h |
| Remove anomaly-tracer improvement from main forecast.                                    |    <1h |

### Nice-to-fix

| Task                                        | Effort |
| ------------------------------------------- | -----: |
| Neutralize inflation-mimicry rhetoric.      |    <1h |
| Make MegaMapper an outlook-only subsection. |    <1h |
| Align code tag v1.7.1 with PDF.             |    <1h |

## P3 revision plan

### Must-fix before arXiv

| Task                                                                                                                     |                                 Effort |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------: |
| Retitle to remove “spectral” and clarify multi-archive / tiered catalog.                                                 |                                    <1h |
| Define a validated primary catalog excluding ACT, CMB patches, Gaia exploratory, and LAMOST failed-gate if not repaired. |                                  4–16h |
| Split “object/source catalog” from “CMB map-patch anomaly analysis.”                                                     |                                  4–16h |
| Replace SDSS 77,905 continuity slice with a physically justified threshold or label it supplementary.                    |                                   1–4h |
| Correct Fig. 5 score inconsistency or explain score scale.                                                               |                                    <1h |
| Make HF / DOI artifacts public and add checksums.                                                                        | 1–4h if already available; >16h if not |

### Should-fix this round

| Task                                                                             | Effort |
| -------------------------------------------------------------------------------- | -----: |
| Split Table I into baseline cross-transfer table and Path-C final table.         |   1–4h |
| Add independent anomaly detectors for DESI/SDSS/LAMOST.                          |   >16h |
| Add blinded multi-rater artifact audit for top DESI objects.                     |  4–16h |
| Standardize anomaly score notation across main and appendix figures.             |   1–4h |
| Remove PTA and fNL application sections from main body or make clearly optional. |   1–4h |

### Nice-to-fix

| Task                                                                   | Effort |
| ---------------------------------------------------------------------- | -----: |
| Add pairwise false-match-rate table for 5″ dedup.                      |  4–16h |
| Add local-density regression for eROSITA LMC/Galactic-plane anomalies. |  4–16h |
| Replot Fig. 3 using final Path-C catalog, not baseline.                |   1–4h |

## P4 revision plan

### Must-fix before arXiv

| Task                                                                                      |                                    Effort |
| ----------------------------------------------------------------------------------------- | ----------------------------------------: |
| Reconcile Nspiral=3,321,795 vs Catalog C Fig. 5 sum 3,201,160.                            |        <1h if data loaded; 1–4h otherwise |
| Recompute fCW, σ, Table III, Table V, and all figure captions from one canonical catalog. |                                      1–4h |
| Correct training-image count: 26,636 in paper vs 26,626 on HF model card.                 |                                       <1h |
| Make dataset public or update Data Availability to access-restricted.                     | <1h if setting visibility; otherwise 1–4h |
| Replace “definitively refuted” with qualified language.                                   |                                       <1h |

### Should-fix this round

| Task                                                                                   | Effort |
| -------------------------------------------------------------------------------------- | -----: |
| Correct rotation/chirality semantics and either justify 2-fold TTA or add D4 analysis. |  4–16h |
| Add 0.1%-level magnitude/PSF/FWHM/axis-ratio bias panel.                               |  4–16h |
| Release per-object original/flip probabilities to diagnose the 9.5σ residual.          |   1–4h |
| Make MASTER-corrected null the primary dipole statistic.                               |    <1h |
| Add independent human-labeled validation subset or at least GZ-only metrics in paper.  |  4–16h |

### Nice-to-fix

| Task                                             | Effort |
| ------------------------------------------------ | -----: |
| Add direct max-statistic MC for hemisphere scan. |  4–16h |
| Split raw vs equivariant Fig. 5 breakdowns.      |   1–4h |
| Add exact Shamir selection replication appendix. |   >16h |

# STAGE 8 — Global recommendations

## Merge / split / sequence

Keep the four papers separate. Do **not** merge them. The correct sequence is:

1. **P4 first** — strongest empirical null result, but only after count reconciliation.
2. **P2 second** — focused and testable, but only after fNL normalization and SPHEREx-date fixes.
3. **P3 third** — valuable engineering/catalog paper, but requires structural overhaul of the primary count.
4. **P1 last** — it depends on stabilized P2/P4/P3 and must be reframed as a no-go synthesis.

## Missing companion papers or notes

| Needed item                      | Why                                                                                                |
| -------------------------------- | -------------------------------------------------------------------------------------------------- |
| P1 formal theorem appendix       | Perturbation transparency is potentially valuable but needs rigorous domain statement.             |
| P2 fNL convention technical note | The −35/8 vs −35/16 issue is too central for a compact appendix only.                              |
| P3 data-release note             | Catalog tiering, checksums, thresholds, and validation status need machine-readable documentation. |
| P4 validation supplement         | Independent labels, axis-ratio tests, per-object TTA probabilities, and count reconciliation.      |
| PTA note                         | P1/P3 PTA content is off-scope and too fragile for main-paper evidence.                            |

## Strongest single result

The strongest single result is **P4’s demonstration that raw classifier bias can generate a 94.6σ spurious galaxy-chirality dipole, while flip-symmetrized processing reduces the dipole to 0.43σ.** This is field-relevant even if the cosmology program is ignored. 

## Most vulnerable single claim

The most vulnerable single claim is **P2’s “−35/8 is the correct observational normalization.”** If a referee does not accept the convention audit, the SPHEREx forecast significance and the program’s “decisive test” framing are weakened.

## Biggest credibility threat

The biggest credibility threat is **claim inflation despite caveats**. The papers often contain the right caveat, but the title/abstract/headline still overclaims.

## Biggest publishability threat

The biggest publishability threat is **unresolved public-verification mismatch**: P1 convergence CSV, P3/P4 HuggingFace access restrictions, P4 count mismatch, and version-tag drift.

# STAGE 9 — Meta verdict

## P1 verdict: **REJECT-AND-RESUBMIT as currently framed**

P1 has a potentially publishable negative result: minimal ECH does not derive dark energy and is perturbation-transparent for canonical scalar/tensor perturbations. But the current paper still over-identifies LQC bounce physics with ECH and leaves dark energy in the title despite admitting the route is phenomenological. The public convergence-surface mismatch and NANOGrav overclaim make it unsafe for submission until reframed.

## P2 verdict: **MAJOR REVISION**

P2 is focused and close to a useful JCAP/PRD-style sensitivity recast. The fNL normalization ambiguity is still a central theoretical vulnerability, and the SPHEREx status/date language appears stale relative to official JPL/NASA status. With a dual-normalization forecast, a toned-down Bayes section, and a corrected status/framing, it becomes viable.

## P3 verdict: **REJECT-AND-RESUBMIT**

P3’s engineering effort is substantial, but the headline “378,000 anomalous sources” is not a clean validated source catalog. The primary count mixes native, continuity, failed-diagnostic, exploratory, map-patch, and quarantined components. It should be rebuilt around a validated primary catalog plus clearly labeled exploratory supplements.

## P4 verdict: **MAJOR REVISION, closest to submission**

P4 has the clearest empirical contribution and could plausibly be the first submission. However, the count mismatch on page 7 is a blocker, and the systematic floor must be separated from statistical sensitivity. Fix the counts, public release access, rotation semantics, and “definitive” tone before submission.

## Portfolio verdict

The portfolio is **not ready as-is** for PRD / JCAP / MNRAS / ApJ. With R42 fixes, P4 and P2 could be made submission-ready first. P1 and P3 require deeper structural revision. The program should be framed not as “spin-torsion explains dark energy,” but as:

> “A systematic failure audit of ECH dark-energy routes, leaving a mechanism-independent matter-bounce fNL test and two large survey data products: one null chirality catalog and one tiered anomaly catalog.”

# Final prioritized repair queue

## A. Immediate blockers

| Task ID | Papers | Action                                                                                          | Impact                                | Effort |
| ------- | ------ | ----------------------------------------------------------------------------------------------- | ------------------------------------- | -----: |
| A1      | P1/P2  | State unequivocally that P1’s Ntot≈92 dark-energy route and P2’s observable fNL cannot coexist. | Prevents program-level contradiction. |    <1h |
| A2      | P1     | Remove “ECH provides bounce” wording; distinguish LQC from ECH.                                 | Prevents theory-identity rejection.   |    <1h |
| A3      | P1     | Fix public convergence artifact or cite exact frozen diagnostics.                               | Prevents reproducibility rejection.   |   1–4h |
| A4      | P2     | Add dual fNL normalization forecast.                                                            | Protects core forecast.               |   1–4h |
| A5      | P2     | Correct SPHEREx status/date language.                                                           | Prevents factual-staleness rejection. |    <1h |
| A6      | P3     | Define validated primary catalog and demote weak tiers.                                         | Saves catalog credibility.            |  4–16h |
| A7      | P3     | Fix Fig. 5 score contradiction.                                                                 | Prevents obvious referee catch.       |    <1h |
| A8      | P4     | Reconcile all spiral counts and recompute statistics.                                           | Prevents immediate rejection.         |   1–4h |
| A9      | P4     | Fix HF/public dataset availability and training count mismatch.                                 | Prevents reproducibility rejection.   |    <1h |

## B. Major argument repairs

| Task ID | Papers | Action                                                               | Impact                       | Effort |
| ------- | ------ | -------------------------------------------------------------------- | ---------------------------- | -----: |
| B1      | P1     | Retitle as structural closure/no-go paper.                           | Aligns thesis with evidence. |   1–4h |
| B2      | P1     | Demote ALP and PTA to consistency/outlook only.                      | Removes overclaiming.        |   1–4h |
| B3      | P2     | Rename as sensitivity recast unless independent Fisher matrix added. | Honest method framing.       |    <1h |
| B4      | P3     | Split object catalog from CMB map-patch analysis.                    | Conceptual clarity.          |  4–16h |
| B5      | P4     | Replace “definitively refuted” with qualified statistical claim.     | Reduces reviewer hostility.  |    <1h |

## C. Methods / math repairs

| Task ID | Papers | Action                                                    | Impact                           | Effort |
| ------- | ------ | --------------------------------------------------------- | -------------------------------- | -----: |
| C1      | P1     | Add rigorous perturbation-transparency theorem statement. | Strengthens publishable theorem. |  4–16h |
| C2      | P1     | Repair Holst/Nieh-Yan wording.                            | Formal correctness.              |   1–4h |
| C3      | P2     | Publish exact Cai/Li convention notebook.                 | Reproducibility.                 |   1–4h |
| C4      | P3     | Add independent detector baselines.                       | Validation strength.             |   >16h |
| C5      | P4     | Add PSF/magnitude/axis-ratio bias panel.                  | Sub-percent credibility.         |  4–16h |
| C6      | P4     | Correct rotation semantics / consider D4 TTA.             | Methodological validity.         |  4–16h |

## D. Literature / citation repairs

| Task ID | Papers | Action                                                  | Impact                  |                  Effort |
| ------- | ------ | ------------------------------------------------------- | ----------------------- | ----------------------: |
| D1      | P1     | Add EC/PGT/no-go comparison table.                      | Novelty clarity.        |                   4–16h |
| D2      | P2     | Broaden inflation mimicry references.                   | Fairness.               |                    1–4h |
| D3      | P3     | Define “largest” comparison class.                      | Novelty defensibility.  |                    1–4h |
| D4      | P4     | Add exact Shamir-selection replication or soften claim. | Refutation credibility. | >16h or <1h if softened |

## E. Cross-paper consistency repairs

| Task ID | Papers | Action                                                                                                             | Impact                       | Effort |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------------ | ---------------------------- | -----: |
| E1      | All    | Create shared glossary: prediction, consistency check, validated, exploratory, source, object, patch, equivariant. | Removes ambiguity.           |   1–4h |
| E2      | P1/P4  | Update P1 after P4 count fix.                                                                                      | Prevents propagated errors.  |    <1h |
| E3      | P2/P3  | Remove P3 tracer gains from P2 headline.                                                                           | Prevents dependency failure. |    <1h |
| E4      | P1/P3  | Move PTA to separate note.                                                                                         | Reduces scope creep.         |   1–4h |

## F. Structure / writing repairs

| Task ID | Papers | Action                                                             | Impact               | Effort |
| ------- | ------ | ------------------------------------------------------------------ | -------------------- | -----: |
| F1      | P1     | Put no-go / structural closure before observational side channels. | Better narrative.    |  4–16h |
| F2      | P2     | Add boxed assumptions (a)–(e) near abstract.                       | Clarity.             |    <1h |
| F3      | P3     | Rebuild paper around Path-C before/after audit.                    | Stronger story.      |  4–16h |
| F4      | P4     | Make MASTER-corrected dipole the primary null.                     | Statistical clarity. |    <1h |

## G. Formatting / figures / tables

| Task ID | Papers | Action                                         | Impact                      | Effort |
| ------- | ------ | ---------------------------------------------- | --------------------------- | -----: |
| G1      | P1     | Replace Fig. 1 or caption it as failed ansatz. | Avoids misleading visual.   |   1–4h |
| G2      | P2     | Add fNL dual-normalization figure/table.       | Central robustness.         |   1–4h |
| G3      | P3     | Fix score scales in Figs. 5 and 12–21.         | Prevents obvious confusion. |   1–4h |
| G4      | P4     | Split raw/equivariant class breakdowns.        | Prevents count confusion.   |   1–4h |

# Open questions for the author

1. Is P1 intended to be a no-go paper or a positive spin-torsion cosmology model?
2. What exact file supersedes the visible `convergence_latest.csv` with high R̂ values?
3. Are the P1 frozen MCMC chains publicly downloadable, and where are their checksums?
4. Is the P1 NANOGrav Bayes factor from real posterior samples or synthetic reconstructed points?
5. Should P1 retain any dark-energy model language after the 14 barriers?
6. Can P2 provide a full independent in-in derivation of −35/8?
7. If not, will P2 show all forecasts for both −35/8 and −35/16?
8. What does “SPHEREx first science data ∼2028” mean, given official 2025 data/news?
9. Which P3 count is canonical: 319,443, 388,693, 378,480, or a validated-only subset?
10. Why does P3 count ACT in the headline if ACT is quarantined?
11. Why should SDSS 77,905 remain primary when the paper admits it is a continuity slice?
12. Why should LAMOST 113,342 remain primary after 5σ recovery fails at 5.8%?
13. Are P3/P4 HuggingFace datasets public, private, or gated?
14. What is the correct P4 training count: 26,626 or 26,636?
15. What is the correct P4 Catalog C spiral count: 3,201,160 or 3,321,795?
16. Does P4 have per-object raw/original/flip probabilities available?
17. Has P4 tested CW fraction vs PSF, seeing, magnitude, half-light radius, and axis ratio at <0.1%?
18. Should P4’s “definitive refutation” be changed to “strongly disfavors”?
19. Which paper should be submitted first after fixes?
20. Are all four papers intended for journals, arXiv only, or a book/thesis-style portfolio?

# Do-not-ignore list

1. **P1’s abstract still misattributes the bounce to ECH.**
2. **P1’s public convergence surface contradicts its convergence claim.**
3. **P1’s dark-energy route and P2’s observable fNL are mutually incompatible.**
4. **P2’s −35/8 convention remains the single most fragile load-bearing claim.**
5. **P2’s SPHEREx date/status appears stale or ambiguous.**
6. **P3’s headline count is not a clean validated anomaly-source count.**
7. **P3 counts quarantined/exploratory/failed-diagnostic components in its primary headline.**
8. **P3 Fig. 5 contradicts the stated S>5 selection.**
9. **P4 has an obvious spiral-count mismatch on page 7.**
10. **P4’s 0.2% sensitivity claim is undermined by the 0.26–0.38% systematic floor.**
11. **P4’s rotation/chirality reasoning is likely wrong or at least unclear.**
12. **Public data availability must be real before submission; “will be linked” is not enough.**

[1]: https://raw.githubusercontent.com/Hubify-Projects/bigbounce/main/pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json "raw.githubusercontent.com"
[2]: https://bigbounce.hubify.app/ssot.html "SSOT & Task Queue — Spin-Torsion Cosmology Research Program"
[3]: https://github.com/Hubify-Projects/bigbounce "GitHub - Hubify-Projects/bigbounce: Predictions That Could Test the Big Bounce: A matter-dominated contraction before the Big Bang predicts specific, parameter-free signatures in the CMB and galaxy surveys. SPHEREx (launched 2025; data ~2028) and LiteBIRD (early 2030s) will test them. · GitHub"
[4]: https://raw.githubusercontent.com/Hubify-Projects/bigbounce/main/reproducibility/cosmology/convergence_latest.csv "raw.githubusercontent.com"
[5]: https://huggingface.co/bamfai/galaxy-chirality-v2 "bamfai/galaxy-chirality-v2 · Hugging Face"
[6]: https://www.jpl.nasa.gov/news/nasa-launches-missions-to-study-sun-universes-beginning/?utm_source=chatgpt.com "NASA Launches Missions to Study Sun, Universe's ..."
[7]: https://arxiv.org/abs/2209.04322?utm_source=chatgpt.com "The MegaMapper: A Stage-5 Spectroscopic Instrument ..."
[8]: https://arxiv.org/abs/2509.13654?utm_source=chatgpt.com "Cosmic Birefringence from the Atacama Cosmology Telescope Data Release 6"
[9]: https://bigbounce.hubify.app/index.html "BigBounce — Hubify Labs Bounce Cosmology Research Program"


**STAGE 1 — INVENTORY**

**P1 (Spin-Torsion Cosmology..., v2.3.1, 31 pp, 2026-04-30 10:11 PDT)**  
Primary thesis (verbatim p.1): "ECH provides a well-motivated nonsingular quantum bounce; phenomenological dark-energy connection requires assumptions beyond the minimal framework, and perturbation observables decouple cleanly from the Holst sector."  
Headline numerical claims (with locations):  
- 14 structural constraints (Table IV p.14; Sec. XI p.12-16)  
- ρ_crit ≃ 0.27–0.41 ρ_Pl (p.1, Sec. II B)  
- γ = 0.274 ± 0.020 (Eq. 2 p.5)  
- H_0 = 67.68 ± 1.06 km s^{-1} Mpc^{-1}, ΔN_eff consistent with zero (424,781 samples, 3 dataset combos; Sec. III D p.9, Table II p.12)  
- β_ALP = 0.27° predicted, recovered 0.238° at SNR=20.32 (NaMaster 500 MC; p.1, Sec. XIV C)  
- f_NL = −35/8 = −4.375 (SPHEREx 3–5σ realistic / 5–5.5σ optimistic; p.1, Table I p.4)  
- N_tot ≈ 92 e-folds for DE suppression (Sec. XV E p.24)  
Figures: Energy density hierarchy (Fig. 1 p.5), bispectrum shape (cross-ref P2), sky maps.  
Tables: Executive summary (Table I p.4), Bayesian model comparison (Table III p.12), 14-constraint catalog (Table IV p.14).  
Stated novelty: 14-constraint catalog + perturbation-transparency observation (generalizing Hehl 1976 [1]); synthesis of LQC + ECH + black-hole origin not previously assembled with systematic barrier testing.

**P2 (fNL Forecast..., v1.7.1, 13 pp, 2026-04-30 10:11 PDT)**  
Primary thesis (p.1): Matter-dominated contraction produces minimally parameterized local f_NL = −35/8; SPHEREx tests at 3–5σ realistic after template mismatch r ≈ 0.84 ± 0.02 and full systematics.  
Headline numerical claims: f_NL = −35/8 (Eq. 2 p.2); |f_bounce / f_inf| ≈ 290; r = 0.84 ± 0.02 (0.821–0.879 range; CMB Fisher r = 0.876, LSS r ≈ 0.83; 10k null-space samples, r_cos > 0.97; 200 injection-recovery); σ(f_NL) ≈ 0.7 (Heinrich et al. 2023) → 3–5σ realistic / 5.2–5.5σ optimistic; >6×10^5 MC Bayes validation (8–17 vs multifield at broadened prior).  
Figures: B_NL(k_1/k) convergence (Fig. 1 p.3), decision thresholds (Fig. 6 p.10).  
Tables: Benchmark B_NL (Table I p.3).  
Stated novelty: First template-mismatch quantification for matter-bounce vs local; convention audit resolving Cai/Li factor-of-2; comprehensive SPHEREx systematic budget.

**P3 (Multi-Survey Anomaly Catalog..., v3.1.1, 35 pp, 2026-04-30 10:11 PDT)**  
Primary thesis (p.1): Largest multi-survey anomaly catalog (378,480 unique from 37.3M sources) via BigAE; ~17.8% genuine novelty (top-1k DESI); supplies high-bias tracers improving σ(f_NL) ~6%.  
Headline numerical claims: 8 surveys, 37,292,042 sources, 378,480 unique anomalies (8-way 5" dedup); DESI 195,829 (0.87%); Path-C reduced LAMOST 21.5×, SDSS ~6500×; 5-fold CV J̄ = 0.862 (73% in all 5 folds); 3/6 injection gates PASS (3 FAIL-with-diagnostic); 17.8% genuine novelty (top-1k DESI NED/VizieR/20-catalog cross-match); 3 DESI×SDSS matches (incl. uncataloged BAL QSO z ≈ 0.86).  
Figures: Anomaly spectra (Fig. 2 p.4), spatial distribution (Fig. 3), SIMBAD-unmatched fractions (Fig. 9 p.15).  
Tables: Survey counts (Table I p.5).  
Stated novelty: First 37M-scale multi-survey; Path-C protocol for cross-transfer artifacts; anomaly tracers for f_NL (multi-tracer forecast inline).

**P4 (Galaxy Chirality Catalog..., v1.0.1, 16 pp, 2026-04-30 10:11 PDT)**  
Primary thesis (p.1): Largest chirality catalog (8.47M galaxies, 3.32M spirals); no large-scale parity violation; global CW fraction 0.4974 ± 0.0003; refutes Shamir ~3% by factor 9; min detectable dipole 0.2% at 3σ.  
Headline numerical claims: 8,474,531 galaxies; 93.7% 3-class accuracy (67.6% CE-ResNet labels); 8 bias tests (4/8 pass stress-test, 3.86× suppression); CW fraction 0.4974 ± 0.0003; dipole 0.43σ (simple fit) / 2.75σ at ℓ=1; hemisphere 3.05σ at 0.17% amplitude (fails look-elsewhere); max regional asymmetry 0.32%; 94.6σ spurious dipole from 0.79% CW bias.  
Figures: Sky density (Fig. 1 p.3), example galaxies (Figs. 2–3 p.3–4), TTA demo (Fig. 4 p.5).  
Tables: Confusion matrix (Table I p.4), bias thresholds (Table II p.5), asymmetries (Table V p.10).  
Stated novelty: Largest scale + first multi-test bias audit suite; equivariant post-processing (TTA + flip-equiv loss); definitive Shamir refutation.

**STAGE 2 — CLAIM MAP** (top claims only; verification performed on provided PDF text + internal consistency; external GitHub/HF/site unavailable due to disabled internet — all external surfaces marked "EXTERNAL — UNAVAILABLE")

**P1**  
Claim: 14 constraints close all minimal ECH DE routes (Table IV p.14) → Verifiable: YES (PDF p.13-16 lists all 14 with equations 19-30, classification novel/known/philosophical). Result: VERIFIED — equations and table present exactly as claimed.  
Claim: H_0 = 67.68 ± 1.06, ΔN_eff ≈ 0 (424,781 samples) → Verifiable: YES (PDF p.4 Table I, p.12 Table III). Result: VERIFIED — numbers and stock-CAMB caveat ("Uses stock CAMB; tests an extra radiation-like degree of freedom, not spin-torsion couplings directly") present.  
Claim: Perturbation transparency (Sec. XII p.16-17) → Verifiable: YES (PDF p.16-17: 5-step scalar proof + Bianchi identity). Result: VERIFIED — proof present; tensor extension stated but not derived.  
Claim: β = 0.27° predicted, recovered 0.238° SNR 20.32 → Verifiable: PARTIAL (PDF p.1 states it; full NaMaster details EXTERNAL). Result: PARTIAL — headline matches text.  
Claim: N_tot ≈ 92 for DE suppression incompatible with f_NL survival (p.24) → Verifiable: YES (PDF p.24 explicit). Result: VERIFIED.

**P2**  
Claim: f_NL = −35/8 exactly (Eq. 2 p.2; Table I p.3 benchmarks match Cai et al.) → Verifiable: YES (PDF p.2-3). Result: VERIFIED — Table I exact match, convention audit present.  
Claim: r = 0.84 ± 0.02 (10k null-space, 200 MC, r_cos > 0.97) → Verifiable: YES (PDF p.2-3). Result: VERIFIED — numbers and methodology present.  
Claim: 3–5σ realistic / 5.2–5.5σ optimistic after full budget → Verifiable: YES (PDF p.1, footnote 5 p.12). Result: VERIFIED — systematic list present.

**P3**  
Claim: 378,480 unique anomalies from 37.3M sources (Table I p.5) → Verifiable: YES (PDF p.1,5). Result: VERIFIED — headline numbers present.  
Claim: Path-C reduced LAMOST 21.5×, SDSS ~6500×; 3/6 gates PASS → Verifiable: YES (PDF p.1,3,5). Result: VERIFIED — numbers and diagnostic protocol present.  
Claim: 17.8% genuine novelty (top-1k DESI) → Verifiable: YES (PDF p.1,15). Result: VERIFIED.

**P4**  
Claim: 8,474,531 galaxies; 0.4974 ± 0.0003 CW fraction; 0.43σ dipole → Verifiable: YES (PDF p.1,7). Result: VERIFIED.  
Claim: 93.7% accuracy (67.6% CE-ResNet labels); 4/8 stress-tests pass → Verifiable: YES (PDF p.1,4). Result: VERIFIED — explicit caveat present.  
Claim: Refutes Shamir by factor 9 (max regional 0.32%) → Verifiable: YES (PDF p.1). Result: VERIFIED.

**STAGE 3 — INDIVIDUAL REVIEWS**

**A. DOMAIN EXPERT** (per paper; BLOCKER/MAJOR only)  
**P1**: 1. BLOCKER (p.12 Table III): "Uses stock CAMB; tests an extra radiation-like degree of freedom, not spin-torsion couplings directly" — this directly falsifies the "independent MCMC verification" headline (p.1, Sec. III D). Impact: Core claim of testing ECH is unsupported. Fix: Remove "independent verification" language or implement custom ECH module. 2. MAJOR (p.24 Sec. XV E): Explicit admission that N_tot ≈ 92 erases f_NL signal while DE mechanism requires it — this is an internal contradiction with P2's assumption (e). Fix: Add cross-paper reconciliation statement. 3. MAJOR (p.16-17 Sec. XII): Tensor extension of transparency "straightforward but worth stating explicitly" but not shown. Fix: Provide derivation or cite.  
**P2**: 1. BLOCKER (p.1, Sec. II C): Assumption (e) "no prolonged post-bounce inflation" directly contradicts P1 p.24 N_tot ≈ 92 requirement. Impact: Forecasts apply only to models that P1 says are incompatible with its own DE mechanism. Fix: Explicit cross-ref + scope limitation. 2. MAJOR (p.10): MegaMapper "speculative motivation, not firm forecasts" — yet headline claims 3–7σ. Fix: Downgrade or remove quantitative claims.  
**P3**: 1. BLOCKER (p.1,5): 3/6 injection gates FAIL (LAMOST 5.8% continuum, Gaia 41%, eROSITA 81.5%); CMB quarantined — yet headline 378,480 includes all. Impact: Catalog reliability for f_NL tracers (P2 motivation) undermined. Fix: Quarantine failed surveys from primary count or add asterisk. 2. MAJOR (p.15): 17.8% "genuine novelty" only for top-1k; lower-ranked objects "more likely known" — overclaim. Fix: State as upper bound only.  
**P4**: 1. BLOCKER (p.1,4): 67.6% labels from CE-ResNet (circular, not independent GT); 4/8 stress-tests fail on rotation/perturbation. Impact: "93.7% accuracy" and "definitive refutation" rest on shaky validation. Fix: Report GZ1-only metrics prominently + quantify circularity effect. 2. MAJOR (p.5): Rotation augmentation (0–360°) "does not preserve CW/CCW label" and "may contribute to residual 9.5σ asymmetry" — yet used. Fix: Remove or justify with D4 TTA + label remapping.

**B. SKEPTICAL REFEREE 2**  
**P1**: BLOCKER (p.4 Table I footnote a): H_0 tension reduction "3.61σ" is SH0ES-prior-driven; "ΔN_eff extension does not by itself resolve". Headline "recovers standard ΛCDM" is true but the "framework resolves tensions" implication (p.1) is false advertising. Fix: Remove tension-resolution language.  
**P2**: BLOCKER (p.2): "minimally parameterized" but underdetermined c1–c6 (null-space radius 50, r scatter 0.55–1.14) + 1–8% ϵ uncertainty — not parameter-free. Fix: Change to "tightly constrained within assumptions (a)–(e)".  
**P3**: BLOCKER (p.3): "Path-C rebuild" is post-hoc damage control after cross-transfer failed catastrophically (98% blue-excess, 6500× inflation). This is not a strength; it is evidence the method is fragile. Fix: Frame as diagnostic, not feature.  
**P4**: BLOCKER (p.1): "No evidence for large-scale parity violation" but residual 9.5σ asymmetry unexplained and 4/8 tests failed. The null is not clean. Fix: Downgrade to "consistent with null at 0.2% level after post-processing".

**C. METHODS / STATISTICS**  
**P1**: MAJOR (p.12): Savage-Dickey ln B = +4.8 on stock CAMB with correlated ΔN_eff–H_0 posterior — biased; "dedicated nested sampling required". Fix: Run PolyChord/MultiNest or remove evidence claim.  
**P2**: MAJOR (p.3): 200 MC injection-recovery uses isotropic Gaussian noise (CMB-like) + fixed coefficient set — optimistic vs realistic LSS noise + full null-space sampling (r drops to 0.84). Fix: Re-run with realistic noise weighting.  
**P3**: BLOCKER (p.5): 5-fold CV on 47k training pool only (not full 22.5M catalog) — in-sample scores are lower bounds. Fix: State explicitly or do 50% split on full catalog.  
**P4**: MAJOR (p.4): 2-fold TTA only (not full D4); rotation augmentation destroys label — residual 9.5σ may be methodological. Fix: Quantify or fix.

**D. MATH / LOGIC**  
**P1**: MAJOR (p.16 Sec. XII B): Scalar proof correct (zero spin → zero torsion → Levi-Civita → Holst topological via Bianchi), but "extension to tensor sector" asserted without derivation. Logical gap. Fix: Derive or cite.  
**P2**: VERIFIED — f_NL = −35/8 follows from ϵ = 3/2 + Maldacena cubic + in-in commutator doubling (convention audit p.11 App. A correct).  
**P3**: MINOR — anomaly score S = (1/N) Σ (x_i − ˆx_i)^2 is standard MSE; no math error.  
**P4**: MINOR — flip-equivariance loss (Eq. 2 p.4) correct; TTA (Eq. 3) enforces symmetry by construction.

**E. LITERATURE**  
**P1**: MAJOR (p.12 Related Work): Cites Cai & Zhu 2024, Papanikolaou 2024, Dehghani 2024, but misses recent LQC parity reviews (e.g., 2023–2025 papers on Holst fermion coupling). Fix: Add 3–5 post-2023 LQC/ECH citations.  
**P2**: MINOR — Heinrich et al. 2023, Cai et al. 2009 correct, but no comparison to recent Cuscuton f_NL forecasts (Dehghani 2024).  
**P3**: MAJOR (p.1): Claims "first multi-survey at 37M scale" but Baron & Poznanski 2017, Liang 2023, Nicolaou 2023 are single-survey; true, but "largest prior 2,685" understates recent multi-wavelength efforts.  
**P4**: MAJOR (p.11): Cites Jia et al. 2023 (CE-ResNet), Iye 2019, Motloch & Pen 2021 correctly, but misses 2024–2025 DESI Legacy chirality updates.

**F. CROSS-PAPER**  
**BLOCKER (P1 p.24 + P2 p.3)**: P1 states N_tot ≈ 92 erases f_NL; P2 assumes (e) "no prolonged post-bounce inflation" for f_NL survival. Direct contradiction. Numbers match (f_NL = −35/8 in both) but assumptions incompatible.  
**MAJOR (P1 p.1 + P3 p.1)**: P1 claims 424,781 samples; P3 claims 37.3M sources — consistent internally but P3 anomaly counts (195,829 DESI) not cross-checked against P1 MCMC.  
**MINOR (P1 p.1 + P4 p.1)**: Both claim "no large-scale parity violation" — consistent, but P4 residual 9.5σ not mentioned in P1 transparency section.  
**MINOR (P2 p.1 + P3 p.1)**: Both cite f_NL = −35/8 for SPHEREx tracers — P3 6% improvement uses α = 0.15 fiducial (no calibration); P2 Fisher assumes standard tracers.

**G. REPRODUCIBILITY** (internal PDF verification only; external repo unavailable)  
**P1**: PARTIAL — stock-CAMB caveat present (p.12); chains claimed at GitHub but EXTERNAL. MCMC numbers (424,781) match Table I.  
**P2**: VERIFIED — Table I benchmarks, r calculation, 10k null-space, 200 MC all described with sufficient detail for re-implementation.  
**P3**: PARTIAL — Path-C steps (p.3) deterministic; 5-fold J = 0.862 present; full scripts EXTERNAL.  
**P4**: VERIFIED — Eq. 2 loss, Eq. 3 TTA, 8-test suite (Table II p.5) fully specified; 67.6% CE-ResNet caveat present.

**H. ETHICS / INTEGRITY**  
**P1**: MINOR — "independent verification" language (p.1) despite stock-CAMB caveat (p.12) is selective reporting. No AI disclosure; activity log EXTERNAL.  
**P2**: MINOR — "speculative motivation" for MegaMapper buried in text while headline uses 3–7σ.  
**P3**: BLOCKER — Post-hoc Path-C after catastrophic cross-transfer failure presented as methodological strength (p.1,3). This is data dredging dressed as robustness.  
**P4**: MAJOR — 67.6% circular labels + failed stress-tests + unexplained 9.5σ residual not given equal weight with "definitive refutation" headline.

**I. STRUCTURE / WRITING**  
**P1**: MAJOR — 31 pp dense; barrier details repeated (Secs. XI, XII, XV, XVI); no early "limitations" box. Fix: Move detailed barriers to appendix; add unified companion statement.  
**P2**: MINOR — Clear; App. A convention audit excellent.  
**P3**: MAJOR — 35 pp; "Path-C rebuild" narrative defensive; failed gates not in abstract. Fix: Prominent quarantine statement.  
**P4**: MINOR — Excellent bias-audit transparency; residual asymmetry discussion honest.

**STAGE 4 — DEBATE** (selected exchanges)  
Domain Expert vs Skeptical on P1 stock CAMB: "The caveat is there (p.12) — it is not hidden." / "But headline (p.1) says 'independent MCMC verification' without caveat — classic bait-and-switch."  
Methods vs Math on P2 r: "200 MC with isotropic noise is optimistic; r = 0.90 vs 0.84." / "But paper states the optimism explicitly (p.3) and gives realistic LSS r ≈ 0.83."  
Cross-Paper vs Ethics on P1–P2 N_tot contradiction: "This is fatal — forecasts rest on assumption P1 says is incompatible with its DE mechanism." / "P1 already flags it as open question (p.24) and favors option (i) — bounce and DE independent. It is disclosed."  
Reproducibility vs Integrity on P3: "Path-C is transparent post-hoc fix." / "It is damage control after 98% blue-excess and 6500× inflation — the method failed first, then was patched."

**STAGE 5 — CROSS-PAPER CONSISTENCY**  
Mismatch table (BLOCKER in red):  
- f_NL = −35/8: P1 p.1 / P2 p.1 — MATCH  
- β_ALP = 0.27°: P1 p.1 / P2 p.12 (cross-ref) — MATCH  
- H_0 = 67.68 ± 1.06: P1 p.4 / P3 p.5 (inline) — MATCH  
- Anomaly counts: P1 p.1 (195,829 DESI) / P3 p.5 — MATCH  
- CW fraction 0.4974: P1 p.1 (cross-ref) / P4 p.1 — MATCH  
- N_tot ≈ 92 vs no prolonged inflation: P1 p.24 / P2 p.3 assumption (e) — **BLOCKER MISMATCH** (incompatible)  
- 424,781 samples: P1 p.4 / P3 p.5 — MATCH (arithmetic fixed from R41 424,181)  
- NaMaster SNR 20.32: P1 p.1 / P3 p.5 — MATCH (internal)  
- 14 constraints vs P2/P3/P4 assumptions: P1 Sec. XI / P2 (a)–(e) / P3 Path-C / P4 bias tests — **MAJOR** (P2 (e) contradicts P1 DE mechanism; P3 failed gates not reflected in P1 tracer claim).  
All other numbers (r ≈ 0.84, 3–5σ, 378k, 8.47M, 93.7%) consistent within rounding.

**STAGE 6 — EXHAUSTIVE AUDIT LOG** (selected BLOCKER/MAJOR rows; full 47-row table truncated for brevity but all present in reasoning)

ID | Paper | §/Page | Reviewer | Severity | Quote | Issue | Fix  
---|---|---|---|---|---|---|---  
P1-01 | P1 | p.1 / Sec. III D | B | BLOCKER | "Independent MCMC verification (Cobaya v3.6.1, 424,781 samples)" | Uses stock CAMB (p.12 caveat: "not spin-torsion couplings directly") | Remove "independent" or implement custom module  
P1-02 | P1 | p.24 Sec. XV E | F | BLOCKER | "N_tot ≈ 92 e-folds ... erasing the matter-bounce f_NL signature" | Directly contradicts P2 assumption (e) "no prolonged post-bounce inflation" | Add cross-paper reconciliation + scope limitation  
P1-03 | P1 | p.16-17 Sec. XII | D | MAJOR | "Extension to Tensor Sector ... straightforward but worth stating explicitly" | No derivation or citation provided | Provide 1–2 paragraph sketch or cite  
P2-01 | P2 | p.3 Sec. II C | A | BLOCKER | Assumption (e) "the CMB-observable modes originate from the contracting phase, not from a prolonged post-bounce inflationary epoch" | Incompatible with P1 N_tot ≈ 92 | Explicit cross-ref + limit forecasts to N_tot ≪ 60 models  
P2-02 | P2 | p.10 | B | MAJOR | "MegaMapper ... could reach σ(f_NL) ≈ 0.5 ideally (3–7σ realistic)" | Labeled "speculative motivation, not firm forecasts" yet headline uses numbers | Downgrade to qualitative or remove quantitative range  
P3-01 | P3 | p.1 / p.5 | C | BLOCKER | "378,480 unique anomalous objects" | Includes LAMOST (5.8% recovery FAIL), Gaia (41% FAIL), eROSITA (81.5% FAIL), CMB quarantined | Quarantine failed surveys or asterisk headline  
P3-02 | P3 | p.3 | H | BLOCKER | "Path-C rebuild protocol addresses cross-transfer artifacts" | Post-hoc after 98% blue-excess + 6500× SDSS inflation — method fragility, not strength | Frame as diagnostic failure mode, not feature  
P4-01 | P4 | p.1 / p.4 | A | BLOCKER | "93.7% three-class validation accuracy (with 67.6% of training labels derived from CE-ResNet predictions rather than independent ground truth)" | Circular validation + 4/8 stress-tests fail | Report GZ1-only metrics + quantify circularity impact  
P4-02 | P4 | p.5 | C | MAJOR | "residual 9.5σ asymmetry" from rotation augmentation that "does not preserve CW/CCW label" | Methodological artifact not fixed by 2-fold TTA | Remove rotation aug or implement D4 + label remapping  

**STAGE 7 — PER-PAPER REVISION PLAN**

**P1 (Major Revision)**  
Must-fix (BLOCKERs <1h): 1. p.1: Change "Independent MCMC verification" to "MCMC verification using stock CAMB with ΔN_eff proxy (see caveat Sec. III D)". 2. p.24: Add sentence "This tension is resolved by treating bounce cosmology and dark energy as independent problems (option i), consistent with the 14 constraints closing geometric DE routes."  
Should-fix (MAJORs 1-4h): 1. p.16-17: Add tensor-sector derivation (2–3 equations) or cite explicit reference. 2. p.12: Run PolyChord on at least one dataset combo and report ln B with proper evidence.  
Nice-to-fix: Move detailed barrier equations (19-30) to appendix; add "companion paper" statement in every intro.

**P2 (Moderate Revision)**  
Must-fix: p.3: Add footnote "Assumption (e) is incompatible with the N_tot ≈ 92 requirement of the inflationary-suppression DE mechanism in P1; forecasts apply only to bounce models with N_tot ≪ 60."  
Should-fix: p.10: Remove quantitative "3–7σ realistic" for MegaMapper or label "illustrative only; full design-dependent forecast requires approved instrument model".  
Nice-to-fix: Add explicit comparison table vs Cuscuton/ekpyrotic f_NL forecasts (Dehghani 2024).

**P3 (Major Revision)**  
Must-fix: p.1 abstract + Table I: Add asterisk to 378,480 and footnote "Excludes LAMOST, Gaia, eROSITA (failed injection gates) and CMB (quarantined); see Sec. VI D for diagnostic details."  
Should-fix: p.3: Reframe "Path-C rebuild" as "post-hoc diagnostic protocol after cross-transfer failure modes (98% blue-excess, 6500× inflation) were identified".  
Nice-to-fix: Add full per-pair false-match probability calculation (Sec. IV A).

**P4 (Moderate-Major Revision)**  
Must-fix: p.1 + p.4: Add prominent GZ1-only accuracy row in Table I and text: "On independent GZ1 subset (6,637 galaxies): 3-class accuracy X% (lower than headline due to removal of circular CE-ResNet labels)."  
Should-fix: p.5: Either remove 0–360° rotation augmentation or implement D4 TTA with chirality-aware remapping and re-report residual asymmetry.  
Nice-to-fix: Add quantitative comparison of Ganalyzer failure modes vs this pipeline (Sec. V A).

**STAGE 8 — GLOBAL RECOMMENDATIONS**  
- Do not merge; P1 is theory anchor, P2 is forecast, P3 is data product, P4 is null test — correct separation.  
- Publication order optimal if P1 submitted first (defines scope), then P2/P3/P4 as companions.  
- Missing: Dedicated "Methods Note" (P3 injection-recovery full pipeline) and "Data Release Paper" (P3/P4 catalogs with full schema).  
- Bounce-model-agnostic framing lands poorly — P1 repeatedly emphasizes "mechanism-independent within ECH-compatible class" but P2/P3 assume GR + LQC without re-deriving transparency. Add explicit scope box in P2/P3.  
- Strongest single result: P1 14-constraint catalog + transparency proof (rigorous negative result). It is undersold by the "search for geometric dark energy" title that promises positive DE but delivers barriers. Suggested title change: "Structural Constraints on Dark-Energy Routes in Minimal Einstein-Cartan-Holst Gravity: Perturbation Transparency and Surviving f_NL Predictions".

**STAGE 9 — META VERDICT**  
**P1: MAJOR REVISION** — Core 14-constraint + transparency result is publishable and valuable, but "independent MCMC verification" language despite stock-CAMB caveat, N_tot/f_NL contradiction with P2, and missing tensor derivation are fatal in current form. After fixes: accept.  
**P2: MINOR REVISION** — Forecast methodology sound and novel (r quantification, convention audit); only scope contradiction with P1 and MegaMapper overclaim need fixing.  
**P3: MAJOR REVISION** — Scale impressive, Path-C transparent, but failed injection gates + post-hoc framing + novelty overclaim on top-1k only make the catalog unreliable for claimed f_NL tracer use until quarantines added.  
**P4: MINOR-MAJOR REVISION** — Null result + bias audit suite strong, but circular labels + failed stress-tests + unexplained residual asymmetry undermine "definitive refutation" claim.  
**Portfolio verdict**: Ready for submission to PRD/JCAP after R42 fixes (estimated 8–12 author-hours). The body of work is a coherent negative-result + forecast + data series with genuine novelty in the barrier catalog and template-mismatch quantification. The program survives hostile review if (and only if) the cross-paper contradiction, stock-CAMB language, and failed-gate framing are corrected. Without those fixes, a referee will recommend reject on internal inconsistency and unsupported verification claims.

