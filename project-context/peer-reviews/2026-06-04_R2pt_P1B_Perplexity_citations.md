# P1B 2026-06-04_R2pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 25.0s

---

This paper contains **major metadata drift, internal self-contradictions, and multiple citation/attribution problems** that must be fixed before acceptance. The most serious issues are that several in-text claims about papers [2], [3], , , , and  do not match the cited metadata or the abstracted results, and the manuscript repeatedly mixes *paper text*, *repository-readme language*, and *version-control/audit artifacts* into the body prose.

**ESSENTIAL**

- **P1B-E1** — **Sec. I, p. 1–2**  
  **Problem:** The manuscript claims the published joint birefringence result is “the published Planck/ACT DR6 2.4–2.9σ [2, 3]” and later treats [2] as “published PR3+WMAP9” while [3] is “ACT DR6.” This is internally inconsistent with the bibliography, where [2] is Eskilt & Komatsu 2022 on WMAP and Planck, and [3] is a 2025 arXiv preprint on ACT DR6. The paper also says “published Planck/ACT DR6 2.4–2.9σ” without showing that either cited source actually reports a single combined Planck+ACT result.  
  **Required fix:** Separate the published Planck/WMAP result from the ACT DR6 result and stop attributing a combined significance to the pair unless the combination is explicitly in a cited source.

- **P1B-E2** — **Sec. IV and VI, pp. 5–7**  
  **Problem:** The paper states that the “headline observational reference” is the published Eskilt & Komatsu joint WMAP+Planck value \( \beta = 0.342^\circ \pm 0.094^\circ \) (3.6σ) and then in the same subsection says the “published joint WMAP+Planck value” is “the joint WMAP9 + Planck PR4/NPIPE analysis.” The cited paper [2] is a 2022 PRD on WMAP and Planck polarization data; the manuscript’s PR4/NPIPE wording is not supported by the citation metadata shown here.  
  **Required fix:** Use the exact dataset description from the cited paper and, if the result was later re-used in code or README material, clearly label that as repository metadata rather than a bibliographic fact.

- **P1B-E3** — **Sec. V A, V B, VI, pp. 6–8**  
  **Problem:** The paper repeatedly reports \(\sigma\)-deviations from a “LCDM point” for different inference procedures as if they were directly comparable. In particular, the text says “w0 departs by +4.3σ and wa departs by −3.6σ” from a Metropolis-Hastings chain, while also calling this a “marginal-tail posterior-extrapolation departure” and later contrasting it with a future Bayes factor / ln B. These are not the same statistical scale. The manuscript also compares SNR values from NaMaster pipeline recovery to sky-detection significances.  
  **Required fix:** Explicitly qualify every \(\sigma\) value by procedure and scale, and do not present tail-extrapolation \(\sigma\), recovery SNR, and sky-detection significance as directly commensurate.

- **P1B-E4** — **Sec. V B, p. 6; Table II, p. 4**  
  **Problem:** The paper uses the phrase “the canonical quintom signature” for the DESI-based \(w_0,w_a\) fit, but the cited DESI paper [2] only reports preference for \(w_0>-1\), \(w_a<0\) and tensions with \(\Lambda\)CDM in combinations with CMB/SN; it does not establish the manuscript’s derived chain-specific values or the “quintom-B” classification used here.  
  **Required fix:** Rephrase as the authors’ interpretation of their own chain, not as a claim that the cited DESI paper itself proves quintom-B.

- **P1B-E5** — **Sec. VI, pp. 7–8**  
  **Problem:** The manuscript presents \( \beta_{\text{combined}} = 0.241^\circ \pm 0.061^\circ \) from “inverse-variance weighting” of Planck NPIPE  and ACT DR6 [3], but then says this is “auxiliary cross-check only” and not the headline number. If the paper uses this number anywhere as supportive evidence, the combination method is methodologically invalid unless calibration covariance between the two measurements is addressed.  
  **Required fix:** Add the covariance model or remove the combined number from any evidentiary role beyond a clearly labeled heuristic check.

**MAJOR**

- **P1B-M1** — **Bibliography, pp. 11–12**  
  **Problem:** Reference [3] is cited as “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654.” The query requires verification against arXiv/ADS; the manuscript itself treats this as a published or at least stable preprint result, but the citation information here is incomplete and may be unstable or not yet the right final bibliographic form.  
  **Required fix:** Verify the arXiv ID/title/author list against arXiv and ADS, then update the citation to the exact published or arXiv form with correct title capitalization and venue status.

- **P1B-M2** — **Bibliography , , , pp. 11–12**  
  **Problem:** The paper mixes “DESI 2024 VI”  with “DESI DR2 results II”  and cites “DES-SN5YR” via , but the text repeatedly attributes “DESI DR2 BAO” and “DESI 2024 DR1 BAO” interchangeably. That is a metadata fusion problem: DR1, DR2, and the 2024 cosmological-constraints paper are not the same dataset release or paper.  
  **Required fix:** Normalize every DESI reference to the correct release, analysis paper, and dataset label; do not use DR1/DR2/2024 interchangeably.

- **P1B-M3** — **Sec. II, III, V, pp. 2–4, 6**  
  **Problem:** The manuscript claims “stock CAMB with \(\Delta N_{\rm eff}\) as a free parameter” and then states “both frozen dataset combinations find \(\Delta N_{\rm eff}\) consistent with zero … and H0 consistent with standard \(\Lambda\)CDM.” However, the paper’s own Table I and narrative use a “full-tension” combination that includes SH0ES and S8 priors, while Table II uses no SH0ES prior. The text repeatedly slides between these two likelihood stacks when discussing H0 tension.  
  **Required fix:** Keep the likelihood stacks fully separated in the prose and make every conclusion explicit about which datasets are included.

- **P1B-M4** — **Sec. III, footnote 1, p. 3**  
  **Problem:** The footnote contains a long reconciliation of sample counts, burn-in fractions, “stale csv” artifacts, and a “stale mid-burn-in diagnostic.” This is review-log / audit material, not scientific paper prose. It also states a previous draft footnote was an arithmetic error.  
  **Required fix:** Remove the audit narrative and keep only the final reproducible chain-count statement that is scientifically necessary.

- **P1B-M5** — **Sec. III, Table I, p. 3**  
  **Problem:** Table I says “Worst R̂ − 1” and “Min ESS” are “Sourced from convergence latest.csv” and also includes a note that one earlier diagnostic is “Not the stale mid-burn-in diagnostic convergence gpu 20260305 stale.csv.” This is internal version-history language in the body of the paper.  
  **Required fix:** Move these repository-specific audit comments to a supplement or remove them; the paper should report only final diagnostics.

- **P1B-M6** — **Sec. V A and Table II, pp. 6 and 4**  
  **Problem:** The paper says the DESI DR2 \(w_0w_a\) chain is “CONVERGED below the standard R̂−1 < 10−2 publication target,” yet Table II lists \(R̂−1 = 0.00820\) with 128,385 samples and then elsewhere says a separate chain is still running and “queued for v1B.0.16+.” The manuscript mixes final and provisional status.  
  **Required fix:** Decide whether the chain is final or preliminary and remove all “queued” language from the main paper if the results are being presented as final.

- **P1B-M7** — **Sec. VI, p. 7**  
  **Problem:** The text states “the same birefringence arises in standard GR with an identical ALP; it is not a distinctive ECH prediction,” but the title and abstract still package the ALP check as part of an “ECH Spin-Torsion Program.” This overstates the paper’s theoretical linkage.  
  **Required fix:** Rewrite the abstract and title so the ALP check is presented as an external consistency test, not as evidence for ECH.

- **P1B-M8** — **Abstract, p. 1**  
  **Problem:** The abstract says “We report the technical verification material for the Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program.” A technical verification paper should not promise a “no-go program” if the body explicitly says the stock CAMB \(\Delta N_{\rm eff}\) run does not test the spin-torsion sector directly and the ALP analysis is not distinctive to ECH.  
  **Required fix:** Make the abstract accurately describe what is *shown* versus what is merely *contextualized*.

- **P1B-M9** — **Sec. IV and VI, pp. 5–7**  
  **Problem:** The paper says the Planck Commander map is “foreground-cleaned CMB-only” and that foregrounds are excluded, while simultaneously claiming the map “removes the very component that breaks the β–α degeneracy.” This is a substantive physics claim requiring explicit support from the cited literature or a derivation, which is not given.  
  **Required fix:** Either cite a source demonstrating the degeneracy-breaking role of the removed component or remove the claim.

- **P1B-M10** — **References , , p. 11**  
  **Problem:** The bibliography cites Hehl et al.  and Mercuri  to support the claim that the “Hehl-Datta-Mercuri parity-even four-fermion contact interaction that survives torsion elimination is dimension-6 and \(M_{\rm Pl}^{-2}\)-suppressed.” The cited papers are general torsion/Immirzi references, not direct support for the manuscript’s exact EFT scaling statement in this context.  
  **Required fix:** Add a direct EFT citation for the operator dimension and scaling, or restrict the wording to what [8,9] explicitly establish.

- **P1B-M11** — **Table III, p. 9**  
  **Problem:** The table explicitly says “Versions and readiness percentages are intentionally pinned,” “the live program continues to advance,” and “P1(b) is now post-v1B.0.40 in development.” This is version-history chatter, not paper content.  
  **Required fix:** Remove the live-program/version-tracking statements from the manuscript body.

- **P1B-M12** — **Sec. VII, pp. 8–9**  
  **Problem:** The prose refers to “R12 GEM-M2 closure,” “R8 GEM-B3 nit,” “R-upgraded-round4 GEM-B1,” and “v1B.0.13+.” These are internal audit tags and round labels.  
  **Required fix:** Delete all internal audit tags and replace with ordinary scientific prose.

- **P1B-M13** — **Sec. III, Table I and Eq./footnotes, p. 3**  
  **Problem:** The paper states “the chain is centered well into quintom-B territory” and then later says “the same \(\sigma\) from different null procedures” can be used to interpret the result. This is methodologically unsafe: a posterior-tail distance, a detection SNR, and a Bayesian evidence scale cannot be interpreted interchangeably.  
  **Required fix:** State the statistical meaning of each quantity and stop translating one inference procedure into another.

- **P1B-M14** — **Sec. VI, footnote 4, p. 7**  
  **Problem:** The footnote uses the phrase “the natural-prior-anchored spectator-consistent result sits at \(\theta_i \sim 0.1\)” while the main text’s scan prior is \(\theta_i \in [0.5,2]\). That means the claimed “natural prior midpoint” is not the prior actually used in the scan.  
  **Required fix:** Align the prior discussion with the actual scanned prior or clearly mark the \(\theta_i\sim 0.1\) point as outside the sampled space.

- **P1B-M15** — **Sec. VI, p. 7**  
  **Problem:** The manuscript says \(C_{a\gamma}\) “fixed at 8” gives \(\beta_{\rm ALP}=0.336^\circ \pm 0.107^\circ\), and also says the model-independent fit is \( \beta_{\rm free}=0.344^\circ \pm 0.096^\circ \). The two fits are then both described as “All three within 1σ,” but they are not the same observable and do not test the same model assumptions.  
  **Required fix:** Explicitly distinguish fixed-coupling model fit from free-amplitude phenomenology and do not collapse them into one qualitative statement.

**MINOR**

- **P1B-m1** — **Bibliography , p. 12**  
  **Problem:** The citation text for  includes an inline note: “reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B.” That is not bibliographic formatting and belongs nowhere in the reference list.  
  **Required fix:** Remove manuscript-internal line references from the reference entry.

- **P1B-m2** — **Bibliography , p. 12**  
  **Problem:** The reference entry for quintom cosmology appends a long parenthetical note: “canonical quintom-cosmology review (two-field DE with w crossing -1). Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism...” This is citation annotation, not a reference.  
  **Required fix:** Keep the bibliography entry clean and move explanatory notes to the main text or a footnote.

- **P1B-m3** — **Sec. II, p. 2**  
  **Problem:** “the bounce scenario motivates extending ΛCDM by \(\Delta N_{\rm eff}\) (particle production at the bounce)” is presented as if standard and generic, but the manuscript itself later treats this only as a phenomenological proxy.  
  **Required fix:** Add “in this paper’s phenomenological proxy” or soften the statement.

- **P1B-m4** — **Sec. III, p. 3**  
  **Problem:** The manuscript calls the run “stock CAMB with no torsion modifications” and then states it is “a bounce-class compatibility check.” That is fine, but the wording implies a direct correspondence between \(\Delta N_{\rm eff}\) and bounce physics that is not established in the paper.  
  **Required fix:** Clarify this is only a proxy mapping.

- **P1B-m5** — **Sec. IV, p. 5**  
  **Problem:** The description “ACT-noise level \(\Delta_P=10\,\mu{\rm K}\cdot{\rm arcmin}\) (a conservative worst-case bias check)” is not directly tied to a cited benchmark or derivation.  
  **Required fix:** Cite the source or explain the rationale for the chosen noise level.

- **P1B-m6** — **Table II, p. 4**  
  **Problem:** The table says “\(\chi^2_{\rm total} = 14037.4 \pm 5.6\)” and then immediately notes a rounding artifact. That note is unnecessary in the main table.  
  **Required fix:** Remove the rounding-artifact explanation unless the manuscript is specifically about numerical bookkeeping.

- **P1B-m7** — **Sec. VII, p. 8**  
  **Problem:** The sentence “the § Structural Tension section as an empirical test of the quintom-B scenario” is forward-looking editorial text.  
  **Required fix:** Remove roadmap language from the body.

- **P1B-m8** — **Appendix A, p. 10**  
  **Problem:** The repository listing includes file names such as “shoes yaml audit.md” and “IMPLEMENTATION MAP.md” in a way that reads like provenance logs, not a scientific appendix.  
  **Required fix:** Limit the appendix to the actual reproducibility artifacts needed to rerun the analysis.

- **P1B-m9** — **Sec. VI, p. 7**  
  **Problem:** The paper says “LiteBIRD is projected to achieve \(\sigma(\beta)\approx0.03^\circ\)” and “For \(\beta=0.27^\circ\): \(\sim 9\sigma\) statistical significance.” That arithmetic is fine, but it should be labeled as a forecast and not mixed with current evidence.  
  **Required fix:** Add “forecast” explicitly and keep it separate from present-day measurements.

- **P1B-m10** — **Overall length**  
  **Problem:** The manuscript is 12 pages, but a large fraction of the text is consumed by audit notes, version reconciliation, chain-status updates, and cross-paper program management rather than the actual methods/result content. For a PRD methods/catalog paper, that is too much overhead for the stated contribution.  
  **Required fix:** Recommended maximum page count: **8–10 pages** for the core companion manuscript, with audit logs moved to supplement or repository documentation.

## Summary recommendation
**MAJOR REVISIONS**

The paper is not ready in its current form because it repeatedly conflates internal audit/version-control language with scientific prose, mixes incompatible statistical scales, and contains multiple metadata/citation problems that must be repaired before the results can be trusted as a PRD submission. The most serious issues are not stylistic: they affect whether the cited literature actually supports the claims being made, whether the dataset labels and release identifiers are correct, and whether the manuscript is honestly describing a completed analysis versus a mixture of completed, ongoing, and repository-only artifacts.