# EXT10 Harvest — P4 — ChatGPT
- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc65e-2488-83e8-90f8-fcacbf9d4378
- PDF md5: 414048af
- Harvested: 2026-06-13 15:16 PDT

---

## Referee report — MNRAS style

**Manuscript:** Survey-Scale Galaxy Chirality with Equivariant TTA (v1.0.185)

---

**Recommendation: MINOR REVISIONS**

I have reviewed the full submitted PDF. The paper is scientifically publishable after correction of one bibliographic/reproducibility blocker and a small number of clarity/statistical-strengthening revisions. I do not see a remaining load-bearing scientific defect that would justify major revisions: the primary real-space null is clearly separated from the MASTER diagnostic channel; the systematic interpretation of the harmonic residual is supported by multiple, mutually consistent controls; and the paper is appropriately cautious about not claiming a formal matched-pipeline exclusion of Shamir/Ganalyzer.

The main result I would allow to stand is: for the high-confidence Catalog C real-space estimator, the chirality dipole is null, z_mom = +0.41, empirical-rank p=0.31, with amplitude A_dip = 4.4×10^{-3} and robustness under per-galaxy label shuffling and independent least-squares implementations.

The revisions below are important for correctness and reader trust, but they do not require a new analysis of the primary result.

---

**2. BLOCKERS — must fix before publication**

**B1. Reference [2] is a bibliographic chimera; fix the Shamir 2020/2022 split**
Location: References, p. 22, entry [2]; also Sec. I, p. 2; Sec. V.A, p. 12.
Issue: The reference list entry [2] combines the title and arXiv identifier of one Shamir paper with the journal/DOI of another. In the PDF, [2] is listed as "Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies," Publ. Astron. Soc. Jpn. 74, 1114 (2022), arXiv:2101.04068, DOI:10.1093/pasj/psac058. However, arXiv:2101.04068 corresponds to a different paper (published in Particles with DOI 10.3390/particles4010002); the PASJ 74, 1114 paper with DOI 10.1093/pasj/psac058 is instead "Using 3D and 2D analysis for analyzing large-scale asymmetry in galaxy spin directions," arXiv:2208.00893.
Proposed fix: Split or correct the citations. If both are used, give them separate reference numbers and update "Shamir (2022a)" in Sec. I and Sec. V.A accordingly.

---

**3. MAJORS — should fix**

**M1. Front-load the high-confidence selection rationale; the null depends on the p_eq>0.6 primary sample**
Location: Sec. III.B, p. 3–4; Sec. IV.C, p. 7–8; Abstract and Conclusions.
Issue: The primary real-space result is robust within the declared HC-broad selection p_eq>0.6, N=949,584, but the unthresholded Catalog C sample gives a visible z≃4.2–4.4 real-space dipole later attributed to a low-confidence-tail systematic. The logic is scattered across Sec. IV.C and the appendices.
Proposed fix: Add a compact "Primary sample definition" paragraph before the first dipole result, giving: the exact primary selection p_eq>0.6, N=949,584; when and why it was fixed; the unthresholded result explicitly labelled "diagnostic/systematics-sensitive"; and the confidence-cut sweep as the evidence that the excess lives in the low-confidence tail.

**M2. Do not describe A_dip<6.8×10^{-3} as a true 95% upper limit unless a coverage calculation is supplied**
Location: Abstract, p. 1; Sec. IV.C, p. 7; Conclusions, p. 15.
Issue: The body text correctly defines A_{95,nq}=6.8×10^{-3} as the 95th percentile of the null amplitude distribution, explicitly "not a signal-injected limit and carrying no frequentist coverage guarantee." However, "A_dip<6.8×10^{-3} at 95% UL" would be too strong if it appears in the final paper or abstract.
Proposed fix: Use: "The 95th percentile of the isotropic-null amplitude distribution is 6.8×10^{-3} in A_p units" or distinguish it clearly from the signal-injected 95%-recovery falsification scale A_{95}∈(1.0%,1.5%].

**M3. Strengthen or soften the ℓ=2 cross-spectrum diagnostic**
Location: Appendix D.i, p. 20–21; Sec. IV.D summary, p. 11–12.
Issue: The ℓ=2 pixel-density cross-spectrum result, r_{ℓ=2}=−0.65, z=−2.89, is plausible and consistent with the rest of the evidence, but the null uses only 200 permutations, giving limited resolution on the tail probability.
Proposed fix: Either rerun the A_p × n_total cross-spectrum null with at least N_MC=1000 (preferably 5000) and report the empirical rank p, or soften the language from "supporting discriminator" to "suggestive cross-spectrum evidence."

**M4. Clarify the scope of the z≃−18 template-fit exclusion**
Location: Appendix D.g, p. 19–20; Abstract; Conclusions.
Issue: In every headline use of this number, the qualification "under the adopted NSIDE=8 block-bootstrap error model" should be unavoidable to prevent readers from treating z≃−18 as a universal likelihood-level exclusion.

---

**4. MINORS — polish**

- m1: Archive and version labels should match v1.0.185: Data Availability states "commit 53b41d12 (v1.0.180, June 2026)" while manuscript is v1.0.185. Before publication, deposit the exact v1.0.185 state.
- m2: Reduce title/abstract density; shorten title to emphasize "Survey-scale galaxy chirality catalog," "null real-space dipole," and "MASTER systematics diagnostic."
- m3: Consolidate significance conventions: keep full explanation in Sec. III.A and add a compact notation table; later captions refer back to that table.
- m4: Figure 8 should be visually tied to Table III: add parenthetical "200-MC diagnostic battery; high-statistics recomputation in Table III."
- m5: Tone down "all 8 tests pass" language: use "all 8 diagnostic checks meet their stated criteria."
- m6: Minor style clean-up: replace "unmissable" with "would be detected with high completeness"; standardize "not spiral" versus not_spiral.

---

**5. Strengths**

- Scale and public value: 8,474,531 DESI Legacy DR8 galaxies, 3,201,160 Catalog C spirals, three catalog tiers, model weights, code, and reproducibility artifacts.
- Clear methodological advance: the flip-equivariant TTA protocol and the explicit not-spiral class address known failure modes in chirality work. The raw-versus-equivariant comparison in Fig. 7 is especially convincing.
- Good estimator hierarchy: the paper clearly distinguishes primary cosmological estimators from secondary harmonic diagnostics.
- Strong systematics audit: the monopole-mask leakage calculation, the confidence-cut sweep, the quality-quartile washout, and the WLS template fit together make a coherent case.
- Transparency about limitations: the paper openly states that 66.5% of training labels derive from CE-ResNet predictions and that p_eq values are ranking scores rather than calibrated probabilities.
- Fair comparison with prior work: the paper avoids overclaiming a formal matched-pipeline exclusion of Shamir/Ganalyzer.

---

**6. Specific scrutiny requested**

**Real-space ℓ=1 dipole headline:** The +0.41σ, empirical-rank p=0.31 result is supported for the HC-broad Catalog C estimator. The wording issue is the "95% UL" phrasing: the 6.8×10^{-3} number is a null-quantile, not a true signal upper limit. I find no remaining load-bearing use of the withdrawn −0.122σ subsample-mask MASTER null in v1.0.185.

**Joint nuisance-marginalized template fit:** Credible under the adopted block-bootstrap model. I would keep the result but require the qualification "under the adopted block-bootstrap error model" wherever z≃−18 appears in headline form.

**MASTER channel as a systematics diagnostic:** One of the strongest parts of the paper. The pre-MASTER monopole-only generative null reproduces 99.32% of the observed raw ℓ=1 pseudo-Cℓ power, and the +7.28σ apodized-footprint result is appropriately presented as a systematics diagnostic, not a cosmological measurement.

**ℓ=2 cross-spectrum r=−0.65, z=−2.89:** Useful supporting evidence for a depth-correlated systematic, but because the cross-spectrum null uses only 200 permutations, I would either increase the null ensemble or present the result as suggestive rather than decisive.

**Shamir 2020 vs 2022 split and arXiv IDs:** This needs correction before publication. Shamir 2020, arXiv:2007.16116, matches the SDSS/Pan-STARRS parity/multipoles paper. The problematic entry is the paper's current [2], which mixes arXiv:2101.04068 with the PASJ 2022 DOI; those are different publications.

---

**Final verdict**

The paper should be accepted after minor revisions. The remaining issues are not a failure of the primary science; they are a bibliographic correction, a few wording/selection-logic clarifications, and one diagnostic that should either be strengthened with more permutations or described more cautiously.
