# EXT1 P1B — Grok Heavy referee report
**Provider**: grok.com web app · effort **Heavy** (Team of Experts)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e
**PDF**: paper1b_mcmc_companion_v1B.0.54.pdf (md5 bd19ee37) · **Harvested**: 2026-06-10T16:45 PDT

---

Thought for 1m 6s

Referee Report: Paper 1B v1B.0.54
Title: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆N_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
Journal: MNRAS (target) / PRD / JCAP
Date: 10 June 2026

1. Recommendation
MINOR REVISIONS

The manuscript is a high-quality technical companion that provides precisely the verification layer promised by its title. All three analyses are executed competently, scoped with unusual (and welcome) explicitness, and supported by a public reproducibility repository. The paper does not overclaim; it repeatedly flags its own limitations, correction notes, and deferred computations. Publication is warranted after light polishing for readability and completeness of artifact listing.

2. BLOCKERS (must fix before publication)
None. No factual errors, no unsubstantiated claims, and no scope violations were identified after end-to-end reading of the full PDF text (all 16 pages) and internal cross-checks of the four requested scrutiny items.

3. MAJORS (should fix)

Section V.A / Table III (likelihood blocks) and Appendix A (reproducibility paragraph): The text states “All materials are at https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility” and lists four Cobaya YAMLs, NaMaster scripts, etc. However, the exact commit hash or tag for the frozen v1B.0.54 state is not given, nor is a direct link to the HuggingFace datasets mentioned in Appendix A.
Proposed fix: Add a one-line “Version of record” statement at the end of Appendix A (or in the Data Availability section) with the specific GitHub commit SHA and HF dataset DOIs that reproduce every number quoted in Tables I–II and Figs. 1–4.
Section IV (NaMaster) / Fig. 3 caption and robustness battery paragraph: The pipeline-recovery SNR values (20.32, 25.71) are correctly identified as template-fit MC quantities, but the sentence “the high pipeline template-fit SNR figures … refer to recovery of injected MC signals and must not be conflated with the published Planck/ACT DR6 2.7–2.9σ sky detection” is buried in a footnote.
Proposed fix: Promote this disclaimer to the main text immediately after the first mention of SNR (p. 6) and repeat it verbatim in the abstract’s NaMaster bullet.

4. MINORS (polish)

The manuscript is footnote-dense (fn. 1–5 plus multiple inline “correction notes”). While the disclosures are deliberate and welcome, several long footnotes (especially fn. 1 on sample-count stratification and fn. 5 on ALP backreaction) could be shortened or moved to Appendix A without loss of transparency.
Some sentences in Sec. III and VI are overly parenthetical; e.g., the quintom-B discussion in Sec. III and the coupling-burden paragraph in Sec. VI would benefit from one-sentence summaries at the end of each paragraph.
Ensure every artifact filename cited (e.g., c10_robustness_battery.json, c5_continuous/c5.input.yaml, reproduce_cosmology.sh) appears exactly once in a consolidated “Artifact index” table in Appendix A (currently spread across paragraphs).
Minor typographic/LaTeX clean-up: a few extraction artifacts in the provided PDF text (e.g., “∆Neff” rendered inconsistently) should be normalized in the final .tex.
Abstract: the phrase “both are MC pipeline-recovery figures, not sky-measurement systematics” is excellent but could be tightened to “both are pipeline-recovery figures only (Monte-Carlo, CMB-only skies)”.

5. Strengths (≥3)

Outstanding reproducibility and open-science standard. The public GitHub repository + HuggingFace datasets, claims-classification table (Appendix B), and explicit “what is NOT included” section set a new benchmark for companion papers. Any reader can regenerate every number in <12 h on modest hardware.
Ruthless and repeated scoping of limitations. The paper repeatedly and explicitly states what each analysis does not do (stock CAMB ≠ full torsion module; synthetic skies contain no galactic foregrounds; ALP birefringence is not ECH-distinctive; spectator regime requires ∼25× θ_i tuning). This honesty is rare and commendable.
Thorough technical validation. The NaMaster 500-MC suite includes a full robustness battery, sky-fraction sweep, sign-symmetry test, and bias-attribution exercise; the MCMC chains have excellent convergence diagnostics (ˆR⁻¹ < 0.003, high ESS); the ALP EOM grid + MCMC cross-check is exhaustive.
Transparency on correction notes and deferred analyses. The deliberate “earlier draft” disclosures and explicit deferral of Bayes factors / nested sampling to a follow-up are models of scientific integrity.

6. Specific scrutiny on the four requested items

309,189 MCMC posterior samples across 2 converged dataset combinations (176,240 full-tension + 132,949 Planck+BAO+SN): Exact arithmetic match (176240 + 132949 = 309189 raw accepted samples). Footnote 1 provides a transparent post-burn-in / thinning reconciliation (∼216k post-burn-in total; 119,617 getdist-thinned for Fig. 1). Convergence metrics (ˆR⁻¹ ≤ 0.003, min ESS > 4692) are publication-quality. No issues.
∆N_eff ≈ 0 result and H_0 = 67.68 ΛCDM-consistent: Confirmed in Table I (full-tension: −0.020 ± 0.169; Planck+BAO+SN: +0.065 ± 0.17) and Fig. 2. H_0 = 67.68 ± 1.06 (full-tension) and 67.79 ± 1.09 (Planck+BAO+SN) are Planck-dominated and explicitly labeled as a null-consistency test (stock CAMB, no torsion Boltzmann modifications). The proxy nature is stated at least six times across abstract, Sec. III, and conclusions. Correct and appropriately caveated.
NaMaster pseudo-C_ℓ pipeline 500 MC recovery at SNR=20.32: Explicitly a bias-injection Monte-Carlo validation on synthetic ΛCDM skies (N_side=512, ACT-like mask f_sky=0.32, 10 µK·arcmin white noise, no galactic foregrounds). Recovered ˆβ = 0.238° for β_inj=0.27° (bias −0.032°); worst-case bias −0.040° at β_inj=0.342°. Template-fit SNR=20.32 (and 25.71) is correctly identified as “matched-template significance of the injected signal against single-realization noise” (footnote 3) and not a sky-detection claim. The scope note (p. 6) and abstract disclaimer are crystal-clear. Robustness battery and f_sky sweep further strengthen the result. No overclaim.
Spectator-ALP carved-out regime (f_a ∼ M_Pl, m ∼ H_0) — explicit parameter-restriction where Ω_φ ≪ Ω_crit holds: Fully addressed in abstract, Sec. VI, fn. 5, and Appendix C. The EOM integration yields ∆φ/f_a ∈ [0.064, 1.19] over the natural box; spectator consistency requires θ_i ∼0.1 (∼25× misalignment tuning relative to scan-midpoint θ_i=0.5), explicitly quantified with posterior mass fractions (0.33 % under flat θ_i prior; drops to 0.068 % under cos θ_i-flat prior). The Ω_a ∼1 regime at θ_i∼1 is carved out as “dark-energy-ALP” and excluded from the spectator claim. The result is labeled “not a distinctive ECH prediction” at least four times. All disclosures are present and accurate.

Overall assessment
This is a model technical companion: rigorous, transparent, and self-critical. The minor revisions requested are purely presentational and will improve readability without altering any scientific content. I recommend acceptance after these light changes. I would be happy to re-review the revised version.

165 sources




Heavy
Attach to message
Drop here to add files to your message
Upgrade to SuperGrok

