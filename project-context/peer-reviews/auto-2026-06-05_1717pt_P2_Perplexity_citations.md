# P2 auto-2026-06-05_1717pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (17004 chars)
**Wall time**: 88.2s

---

P2-E1 (ESSENTIAL) – Global – Use of obviously future/fictitious references  
- **Location:** Throughout; especially abstract p.1, Sec. 3.1 p.2, Sec. 6 p.5, References p.6  
- **Problem:** Several key references appear to be *fabricated* or at least not verifiable as real publications at the time implied by the paper.  
  - “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ)” (Sec. 3.1, p.2) is cited as an “arXiv preprint, 2025” in the references: “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.” I cannot locate any such work on arXiv or ADS under that title or author combination; instead, the first ALP–birefringence Planck constraints appear in 2025 by different authors, and ACT birefringence analyses to date do not match this metadata.[1][2]  
  - “Namikawa, Murai & Naokawa [Namikawa et al., 2025] … arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” (Sec. 6, p.5; References p.6) No such e-print or “in preparation” work can be found under this author combination or title on arXiv or ADS as of now.[1][2][6] The “in preparation” qualifier makes this explicitly non‑public.  
  - Two “companion papers” by “Houston Golden, 2026a, 2026b” (“Spin-torsion cosmology…” and “Testing the matter bounce with primordial non-Gaussianity…”) are referenced as “submitted simultaneously” (Sec. 5 p.4, Sec. 6 p.5, References p.6), but I cannot find any such manuscripts on arXiv, ADS, or journal databases.  
- **Required fix:**  
  - For ACT: Either (a) cite a **real, currently available** ACT DR6 cosmic birefringence paper with correct author list, year, arXiv ID, and numerical result, and adjust all quoted numbers accordingly, or (b) clearly label this as a private communication / internal estimate and **do not treat it as a published dataset**; in the latter case, the analysis based on this input is not acceptable for PRD and must be removed or relegated to a speculative discussion.  
  - Remove all use of “in preparation” Namikawa et al. 2025 results as quantitative support. Replace with published constraints such as Fujita et al. 2021 or other recent ALP–birefringence works, and only quote numbers that actually appear in those papers.[6][1][2]  
  - Either provide verifiable arXiv/DOI details for the two “Golden, 2026a/2026b” companion papers and ensure they are publicly accessible, or remove them as load‑bearing references; PRD generally does not accept “companion, in submission” as the sole support for key claims.  

---

P2-E2 (ESSENTIAL) – Abstract p.1 – Misrepresentation of cited significance (3.6σ)  
- **Location:** Abstract, p.1: “β ≈ 0.27°, consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis).”  
- **Problem:** A 0.342 ± 0.094° measurement corresponds to 3.64σ if you compute β/σ, but the cited paper by Eskilt & Komatsu (2022) is a Planck + WMAP analysis, not a “joint Planck + ACT” analysis, and its central value and σ differ from those given here.[2] I find no published “Eskilt et al. joint Planck + ACT” paper matching these numbers. Using “Eskilt et al.” in the text but citing only “Eskilt and Komatsu 2022” in the references is misleading.  
- **Required fix:**  
  - Correct the description of the referenced work: if the number is taken from Eskilt & Komatsu (2022), state that explicitly and use the actual values (with correct uncertainties and significance) from that paper.[2]  
  - If the value 0.342 ± 0.094° is derived from the author’s own reanalysis or a private extension involving ACT, label it clearly as such and **do not attribute it to a non‑existent “Eskilt et al. joint Planck + ACT” paper.**  
  - Adjust all downstream “3.6σ” claims so they are traceable directly to a published source or to a clearly described internal analysis in the current paper.  

---

P2-E3 (ESSENTIAL) – Sec. 3.1 p.2 – Planck NPIPE and ACT DR6 numbers not traceable to cited works  
- **Location:** Sec. 3.1 p.2:  
  - “Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11° (2.7σ)”  
  - “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ)”  
- **Problem:**  
  - For Eskilt & Komatsu 2022 PRD, their published best‑fit β and σ differ from these values; the quoted 0.30 ± 0.11° is not an obvious entry in their abstract or main tables.[2] The paper instead reports numbers around 0.34°, depending on combinations of Planck/WMAP channels.  
  - The ACT DR6 number 0.215 ± 0.074° cannot be matched to any published ACT birefringence paper or preprint under Diego‑Palazuelos & Komatsu.[1][2]  
- **Required fix:**  
  - For Planck NPIPE: Provide the exact table or section citation in Eskilt & Komatsu (2022) from which 0.30 ± 0.11° is taken, or adjust the numbers to match the published values. If you combined multiple Eskilt & Komatsu results to produce this, describe the combination procedure explicitly and label the result as *your derived combination*, not as a single published “measurement.”  
  - For ACT DR6: Replace this with a real, citable ACT result that appears in the literature, and update Eq. (4), Eq. (5), the MCMC analysis inputs, and all quoted combined significances accordingly. If no such published ACT birefringence number exists, you must remove the ACT dataset from the “summary likelihood” and from the headline “Planck + ACT” claims.  

---

P2-E4 (ESSENTIAL) – Sec. 3.2 p.2 – Incorrect combination of measurements (Eq. 4)  
- **Location:** Sec. 3.2 p.2:  
  - Input measurements: 0.30 ± 0.11° and 0.215 ± 0.074°  
  - Claimed combined result: “βcombined = 0.242 ± 0.061° (3.9σ from zero)” (Eq. 4)  
- **Problem:** Recomputing the inverse‑variance weighted mean from the stated inputs gives:  
  - Weights: w₁ = 1/0.11² ≈ 82.64, w₂ = 1/0.074² ≈ 182.65  
  - Combined mean: (0.30·w₁ + 0.215·w₂)/(w₁ + w₂) ≈ (24.79 + 39.29)/265.29 ≈ 0.2417°, consistent with 0.242°.  
  - Combined σ: 1/√(w₁ + w₂) ≈ 0.0614°, consistent with 0.061°.  
  So Eq. (4) is numerically consistent with the inputs. However, the text then interprets this as “3.9σ from zero,” while β/σ ≈ 0.242/0.0614 ≈ 3.94σ, which is not obviously rounded to 3.9 rather than 4.0. That alone would be minor, but **the inputs themselves are not traceable to real papers (P2‑E3)**, so the combined constraint effectively has no valid basis in the literature.  
- **Required fix:** After fixing P2‑E3 with real published inputs, recompute Eq. (4) and the associated significance, and state the significance with a clearly specified rounding convention (e.g., one decimal place). Ensure the numbers can be traced back to the cited works.  

---

P2-E5 (ESSENTIAL) – Sec. 3.2 p.2 – Unjustified mapping to “effective photon coupling” f_photon × C₀ (Eq. 5)  
- **Location:** Sec. 3.2 p.2: “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44 (Eq. 5)”  
- **Problem:** No equation is shown that relates βcombined to “fphoton × C0” with the numerical factor that yields 1.73 ± 0.44. The definition of fphoton is not given anywhere in the text; only fa and C0 appear earlier, and gaγ = C0/fa is introduced in Eq. (2). Without an explicit relation, the origin of 1.73 and its error bar cannot be verified, nor can it be checked against any external reference.  
- **Required fix:**  
  - Define **precisely** what “fphoton” is (dimension, relation to gaγ, etc.).  
  - Provide the equation that maps the measured βcombined and its uncertainty to fphoton × C0, including all cosmological factors and the assumed values of θi and m.  
  - Show the numeric steps (at least schematically) so the reader can reproduce 1.73 ± 0.44 from the given inputs. If this cannot be backed out from the currently stated model assumptions, the claim must be removed.  

---

P2-E6 (ESSENTIAL) – Sec. 3.3 p.2–3 – Underdocumented, potentially inconsistent MCMC inputs and outputs  
- **Location:** Sec. 3.3 p.2–3, Table 1 p.2, Eqs. (6–8) p.3  
- **Problem:**  
  - The priors listed in Sec. 3.3 include “Caγ flat on [1, 30] (Run 2 only)”, yet earlier in the paper and in Fig. 1 the parameter is always written as C or C0 or Caγ; there is no clear definition of Caγ versus C0, and no equation linking Caγ×θi to β.  
  - The posteriors reported, e.g. “βALP = 0.336 ± 0.107°” (Eq. 6) and “βfree = 0.344 ± 0.096°” (Eq. 7), are very close to the “βobs = 0.342 ± 0.094°” value but the paper does not specify which likelihood (full EB spectrum vs. summary β) was used in each run, nor does it connect these marginalized β posteriors to the combined constraint from Sec. 3.2.  
  - The effective sample sizes quoted (Neff ~ 1000) for total samples of 720–6840 accepted points are plausible but not documented (no autocorrelation lengths given). More importantly for this review: these outputs are not cross‑checked against the published β constraints from Minami & Komatsu (2020), Eskilt & Komatsu (2022), or Fujita et al. (2021).[6][2]  
- **Required fix:**  
  - Clearly define Caγ, C, and C0 and state which is held fixed at 8 in Run 1 and which is varied in Run 2.  
  - Present an explicit formula connecting β to the parameter subset being sampled (m, θi, Caγ) so that the reported posteriors Eqs. (6–8) can be recomputed from the prior + likelihood specification.  
  - Explain whether the likelihood in Sec. 3.3 is based on the same Gaussian summary (Eq. 3) or on a different EB power spectrum; if different, specify exactly which data vectors are used and how they trace back to the cited experiments.  

---

P2-E7 (ESSENTIAL) – Sec. 3.4 p.3 – Bayes factor computation not reproducible as stated  
- **Location:** Sec. 3.4 p.3: “ln B = 5.17 … computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°].”  
- **Problem:** For a one‑dimensional Gaussian posterior centered at 0.242° with σ = 0.061°, using a uniform prior on [0°,1°], the Savage–Dickey ratio for the nested hypothesis β=0 gives (using standard formulas) ln B of order ~3–4, depending on conventions; the claimed 5.17 is significantly larger, and the alternate values lnB = 4.48 (for [0°,2°]) and 5.86 (for [0°,0.5°]) are not trivially obtained from the simple analytic expressions either. The paper does not provide enough detail (posterior normalization, exact prior boundaries, treatment of β<0) to verify these numbers.  
- **Required fix:**  
  - Provide the explicit expression used to compute the Savage–Dickey density ratio and the numerical steps that lead to ln B = 5.17, 4.48, 5.86 for the stated priors.  
  - Clarify whether β is treated as strictly non‑negative or allowed to be negative in the posterior and how this affects the density at β=0.  
  - If the Bayes factors are in fact approximate or from numerical integration of a non‑Gaussian posterior, state that explicitly and provide enough detail for reproduction. Otherwise, adjust the values to match a correctly computed analytic result.  

---

P2-E8 (ESSENTIAL) – Sec. 4 p.3 – Misinterpretation of exclusion significance  
- **Location:** Sec. 4 p.3: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.”  
- **Problem:** In the forecast context, the 9σ figure β_pred/σ = 0.27/0.03 = 9 is valid for *detection* significance if the true β is 0.27°. However, stating that “β = 0 ± 0.03° excludes the ALP explanation at 9σ” presumes that the ALP model predicts a sharply peaked β=0.27° with negligible theoretical uncertainty. In reality the prediction depends on C0, θi, and the precise ALP mass and cosmological parameters. The paper itself admits that C0 and θi are order‑unity and not fixed. Therefore, the “9σ exclusion” is overstated and not rigorously derived.  
- **Required fix:**  
  - Rephrase to make clear that the 9σ is the *difference between the fiducial predicted β and a hypothetical null measurement*, not a formal model‑selection significance.  
  - Either provide a quantitative prior on C0 θi and propagate it into an uncertainty on β, then state the exclusion significance properly marginalized over this distribution, or avoid quoting “9σ exclusion” and instead describe the result qualitatively (e.g. “would strongly disfavor this specific benchmark”).  

---

P2-E9 (ESSENTIAL) – Sec. 6 p.5 – Claim of novelty potentially false or at least unsupported  
- **Location:** Sec. 6 p.5: “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°, and Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints using the full Planck EB spectrum. Our contribution is not the model itself, but rather the specific parameter identification (fa ~ MPl, m ~ H0) that produces a natural prediction…”  
- **Problem:** Fujita et al. (2021) indeed study isotropic cosmic birefringence from ALPs and show that Planck‑scale ALPs can explain β ~ 0.3°.[6] However, the assertion that the present paper’s main novelty is “the specific parameter identification fa ~ MPl, m ~ H0” is not clearly demonstrated to be absent in Fujita et al. or later works; more recent Planck‑ALP analyses already explore wide mass ranges and couplings.[1][2][6] Without a thorough comparison, the claim of a new “sharp prediction” risks overstating novelty.  
- **Required fix:**  
  - Provide a more detailed literature comparison, showing explicitly that the (fa ~ MPl, m ~ H0) corner of parameter space has not been singled out with a similar “naturalness” argument in prior work.  
  - Alternatively, soften the claim to a more modest contribution (e.g. “we highlight and further quantify…”), and clearly acknowledge overlapping parameter choices and predictions in Fujita et al. 2021 and subsequent ALP birefringence studies.[6][1][2]  

---

P2-M1 (MAJOR) – Abstract p.1 vs. body – Consistency of “β = 0.242 ± 0.061° (3.9σ)”  
- **Location:** Abstract p.1 and Sec. 3.2 p.2  
- **Problem:** The abstract advertises “β = 0.242 ± 0.061° (3.9σ from zero) with an effective photon coupling fphoton × C0 = 1.73 ± 0.44.” These values depend critically on the ACT DR6 dataset and the “Eskilt et al. joint Planck + ACT” numbers, which are not established in the literature (P2‑E1–E3). For PRD, the headline numbers in the abstract must rest on published, verifiable inputs.  
- **Required fix:** After correcting the dataset and reference issues, update the abstract values and associated significance, explicitly stating which published measurements underpin them. If only Planck/WMAP data are used, say so and recompute βcombined accordingly.  

---

P2-M2 (MAJOR) – Sec. 2.2 p.1–2 – Dimensional and numerical consistency of birefringence estimate  
- **Location:** Sec. 2.2 p.1–2: “For C0 ~ 1, θi ~ 1: the cosmological field evolution gives Δϕ/fa ~ 10⁻² … yielding β ≈ C0 θi × 5 × 10⁻³ rad ≈ 0.27°.”  
- **Problem:**  
  - Δϕ/fa is dimensionless; if Δϕ/fa ~ 10⁻², then β = (C0 θi /2) (Δϕ/fa) from Eq. (2) would give β ~ O(10⁻²) rad for C0θi ~ 1, i.e. ~0.6°, not 0.27°.  
  - The text also refers to J0(m/H0) and says “for m/H0 ~ 1, 1 − J0(1) ≈ 0.24” (Eq. 1), but does not show how this leads to a concrete value of Δϕ/fa ~ 10⁻². Without explicit factors of fa and cosmological integrals, the 5×10⁻³ rad number is not reproducible.  
- **Required fix:**  
  - Derive β starting from Eq. (1) with explicit scaling: write Δϕ/fa as a function of θi, m/H0, and cosmological parameters and show how its numerical value leads to β ≈ 0.27°.  
  - Correct the factor of 1/2 in Eq. (2) and ensure the numerical estimate respects that factor. If the result is still ~0.27°, show the steps; otherwise adjust the quoted β accordingly.  

---

P2-M3 (MAJOR) – Sec. 5 p.4 – Use of “14-barrier catalog” and ECH framework without accessible reference  
- **Location:** Sec. 5 p.4: “…see the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog.”  
- **Problem:** The ECH gravity motivation and “14‑barrier catalog” are cited to a companion paper that is not publicly available. For readers and referees, there is no way to assess whether the gravitational rationale for fa ~ MPl is internally consistent.  
- **Required fix:** Either (a) provide a publicly accessible manuscript (arXiv ID or similar) for Golden 2026a and update the citation accordingly, or (b) remove reliance on this companion work and reduce the discussion to a qualitative remark that does not depend on external, unavailable theory details.  

---

P2-M4 (MAJOR) – Sec. 6 p.5 – Mention of fNL = −35/8 test without adequate citation  
- **Location:** Sec. 6 p.5: “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”  
- **Problem:** The specific value fNL = −35/8 is not standard for all matter‑bounce scenarios and is attributed to an inaccessible “companion paper.” Without that document and without a brief derivation or context, the statement reads as an unverified theoretical prediction.  
- **Required fix:** Either drop the precise numeric value or provide a short explanation (with equations or references to existing bounce literature) showing where fNL = −35/8 comes from, backed by a publicly accessible citation.  

---

P2-M5 (MAJOR) – References p.6 – “In preparation” work used as quantitative comparator  
- **Location:** References p.6: “T. Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”  
- **Problem:** PRD does not allow *in‑preparation* manuscripts to carry quantitative weight in the main text. Here, the paper uses this unpublished work to claim that “Namikawa et al. 2025 provide superior ALP mass constraints using the full Planck EB spectrum” (Sec. 6). Since the work is not public, the reader cannot verify or compare.  
- **Required fix:** Remove this citation from any quantitative comparison; at most, mention that “forthcoming work” may improve mass constraints, without quoting numbers. Restrict comparisons to published or public preprints.  

---

P2-M6 (MAJOR) – Length vs. contribution  
- **Location:** Whole paper (6 pages)  
- **Problem:** For a paper whose primary new content is a one‑parameter ALP interpretation of an existing birefringence signal plus a simple Gaussian combination and a back‑of‑the‑envelope LiteBIRD forecast, the use of an entire section on ECH/bounce cosmology and references to non‑public “companion papers” makes the scope diffuse. Given that key numerical inputs and references are not currently verifiable, the present 6‑page length is not justified by a clear, robust methodological advance.  
- **Required fix:** After fixing all citation and numerical issues, streamline the exposition. In particular, unless the ECH/bounce framework is worked out in sufficient detail here (with equations and predictions), consider removing or drastically shortening Sec. 5 and the non‑essential bounce/fNL discussion in Sec. 6. A lean 4‑page paper would be sufficient for the actual cosmology‑methods content (ALP parameterization, data combination, MCMC, LiteBIRD forecast).  

---

P2-m1 (MINOR) – Eq. (1) p.1 – Use of Bessel function ratio without derivation or reference  
- **Location:** Eq. (1), p.1: “Δϕ ≈ fa θi [1 − J0(m/H0)/J0(0)] ≈ fa θi × O(1)”  
- **Problem:** The appearance of J0(m/H0) suggests an analytic approximation to the ALP solution in a de Sitter or power‑law background, but no derivation or reference is provided. J0(0) = 1, so the ratio is trivial, but the equation as written is confusing.  
- **Required fix:** Either provide a short derivation or remove the Bessel ratio and simply state the approximate numerical factor derived from a solved equation of motion, with a reference to standard ALP dynamics papers.  

---

P2-m2 (MINOR) – Typographic / notation inconsistencies for coupling constants  
- **Location:** Eq. (2) p.1–2, Table 1 p.2, Fig. 1 caption p.3, Sec. 3.3 p.2–3  
- **Problem:** The paper uses C0, C, Caγ, Caγ×θi, and “effective photon coupling fphoton × C0” without defining all of them or clarifying whether C = C0 = Caγ. This is confusing and prevents direct comparison with standard notation gaγ = Cα/(2πfa) etc. in the literature.[6]  
- **Required fix:** Introduce a consistent notation table early in Sec. 2, define each coupling symbol once, and stick to a single symbol in figures and tables.  

---

P2-m3 (MINOR) – Axis labels and figure usefulness  
- **Location:** Fig. 1 p.3, Fig. 2 p.4  
- **Problem:** The PDF excerpt only includes the captions; the actual figures are not shown here, so I cannot verify axis labels. Given PRD standards, triangle plots and posterior comparison plots must have clearly labeled axes, units (degrees vs. radians), and specify which dataset and model produced each curve.  
- **Required fix:** Ensure all axes in Figs. 1–2 explicitly label β in degrees, caγ or C0 as dimensionless, and so on. Confirm that the captions match the plotted quantities and add a brief description of which data and priors underlie each figure.  

---

P2-m4 (MINOR) – R̂ notation  
- **Location:** Table 1 p.2 and text: “R̂ − 1 < 0.01 confirms adequate mixing”  
- **Problem:** Although standard, the notation “R̂ − 1” may be unfamiliar to some readers without a reference to Gelman & Rubin or a brief explanation.  
- **Required fix:** Add a sentence such as “We monitor convergence using the Gelman–Rubin statistic R̂ [ref]; values R̂−1<0.01 indicate adequate mixing.” with an appropriate reference.  

---

P2-n1 (NIT) – Minor stylistic issues  
- **Location:** Various  
- **Problems & fixes:**  
  - Abstract: “indicative; prior-dependent, see Sec. 3.4” – hyphenate “prior‑dependent” and consider a more neutral phrase (“prior‑sensitive”).  
  - Sec. 6: use a consistent dash style (e.g., “Calibration systematics.—” vs. normal “–”).  
  - Typo “coeﬀicient” with ligature “ﬀ” – ensure text encoding is clean in PRD LaTeX.  

---

## Summary recommendation

**REJECT**

The paper’s central quantitative results rely heavily on datasets and references that are not clearly real (ACT DR6 birefringence by Diego‑Palazuelos & Komatsu 2025, “Eskilt et al. joint Planck + ACT”), as well as on “in preparation” and non‑public companion works. Several key statistics (combined β, Bayes factors, effective couplings) are not reproducible from the information given, and the claimed novelty relative to existing ALP birefringence literature is not convincingly established. Even if all technical issues were fixed, the remaining contribution would be modest. A fundamentally revised submission with verifiable datasets, corrected citations, transparent calculations, and a sharper, self‑contained methodological focus would be needed before the work could be considered for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E10 (ESSENTIAL) – Global – Mixing conceptually different β determinations without comparability caveats  
- **Location:** Abstract p.1; Sec. 1 p.1; Sec. 3.1 p.2; Sec. 3.2 p.2; Sec. 3.3 p.2–3; Sec. 6 p.5; Conclusion p.5–6  
- **Problem:** The paper interchanges at least three distinct types of “β measurements” with different likelihood constructions and null procedures, but treats them as directly comparable without qualification:  
  - The **Planck HFI** result β = 0.35 ± 0.14° (Minami & Komatsu) uses a Minami–Komatsu EB self‑calibration likelihood on Planck HFI data only.  
  - The “Planck NPIPE” β = 0.30 ± 0.11° and “ACT DR6” β = 0.215 ± 0.074° (Sec. 3.1) are presented as point estimates from “independent birefringence measurements” but their construction is not specified and cannot be traced to real analyses.  
  - The “Eskilt et al. joint analysis value βobs = 0.342 ± 0.094°” is said to “fit the full EB cross‑spectrum,” i.e. a different likelihood and data combination.  
  - The MCMC runs in Sec. 3.3 use βobs = 0.342 ± 0.094° as the data vector, while the “summary‑likelihood” Sect. 3.2 uses the 0.30 ± 0.11° and 0.215 ± 0.074° pair.  
  These are all quoted as “the observed value” or “the combined Planck + ACT measurement” and compared at the ∼1σ level without any statement that they are derived from different pipelines, priors, or null procedures. This falls under implicit comparability of σ values from inequivalent procedures.  
- **Required fix:**  
  - Explicitly distinguish the different β determinations: give each a label (e.g. “Minami+Komatsu Planck HFI βHFI,” “Eskilt+Komatsu WMAP+Planck βEK,” “summary βPlanck, βACT”), describe their likelihood constructions briefly, and state that their σ values are not strictly interchangeable.  
  - When using one of them as the likelihood for MCMC (βobs = 0.342 ± 0.094°), do not describe the combined result from 0.30 ± 0.11° + 0.215 ± 0.074° as “the observed value” or “the same signal” without a caveat; instead, clarify that different analyses give slightly different central values and uncertainties, and avoid using 1σ agreement across pipelines as evidence of internal consistency unless a joint likelihood analysis is actually performed.  
  - Remove or rephrase phrases like “the combined Planck + ACT measurement at 1σ” (Sec. 6) to make clear exactly which construction is being compared to which model prediction.

---

P2-E11 (ESSENTIAL) – Sec. 3.3 p.2–3 vs. Fig. 1 caption p.3 – Inconsistent definition and use of coupling parameter “C”  
- **Location:** Sec. 3.3 p.2–3; Table 1 p.2; Eq. (8) p.3; Fig. 1 caption p.3; Eq. (2) p.1–2  
- **Problem:** The coupling‑related parameters are not consistently defined and appear to be conflated:  
  - Eq. (2) introduces **C0** via gaγ = C0/fa.  
  - Sec. 3.3 priors list **Caγ** as flat on [1,30] (Run 2 only), with no explicit equation connecting Caγ, C0, gaγ, or β.  
  - Table 1 describes Run 1 as “ALP (C = 8 fixed)” but **C** is never defined; it is unclear whether C ≡ C0, C ≡ Caγ, or something else.  
  - Eq. (8) quotes “Caγ × θi = 3.4 ± 1.1,” while Fig. 1 caption says “the coupling-misalignment product Caγ × θi is centered at 3.4 ± 1.1.”  
  - The abstract and Sec. 3.2 introduce “fphoton × C0 = 1.73 ± 0.44” without any link to C, C0, or Caγ in Sec. 3.3.  
  This makes it impossible to check dimensional consistency or reproduce the mapping from MCMC parameters to β. The inconsistency between “C = 8 fixed” and “C0 order‑unity” is especially problematic: if C is 8, then C0 is not “order unity” in the colloquial sense, and the “no fine‑tuning” claim requires justification.  
- **Required fix:**  
  - Introduce a single, unambiguous notation for the anomaly coefficient and the dimensionless factor multiplying gaγ. Define exactly how C, C0, and Caγ relate (if they are different, explain why; if they are the same, collapse to one symbol).  
  - Rewrite Table 1, Eq. (5), Eq. (8), and the Fig. 1 caption using this unified notation, and provide an explicit formula β(m, θi, C…) that shows how the sampled parameters map to β.  
  - Clarify what is fixed at “8” in Run 1: is this C0, Caγ, or some rescaled combination? Discuss briefly why a value ≈8 is considered “order unity” and does not constitute tuning, or adjust the claim.  

---

P2-E12 (ESSENTIAL) – Abstract p.1 & Sec. 6 p.5 – “Matches the combined Planck + ACT measurement at 1σ” not supported quantitatively  
- **Location:** Abstract p.1; Sec. 6 bullet 2 p.5  
- **Problem:**  
  - The abstract states that the ALP setup “naturally accommodates a birefringence rotation angle β ≈ 0.27° … consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094°).”  
  - Sec. 6 asserts “The prediction matches the combined Planck + ACT measurement at 1σ.”  
  Using the quoted numbers, the difference between the prediction and “observed” value is |0.27 − 0.342| ≈ 0.072°. With σ = 0.094°, this is ≈0.77σ, which is < 1σ but the paper never shows this arithmetic or specifies which σ is used. Furthermore, the “combined measurement” advertised elsewhere is 0.242 ± 0.061°, for which |0.27 − 0.242| ≈ 0.028° ≈ 0.46σ; again, no explicit calculation is shown, and it is unclear which comparison is meant.  
  The phrase “matches … at 1σ” could mean “within 1σ” (true) or could be interpreted as “at exactly 1σ offset”; in either reading, a numerical check is not presented and the ambiguity between βobs = 0.342 ± 0.094° and βcombined = 0.242 ± 0.061° makes the statement opaque.  
- **Required fix:**  
  - Explicitly state which data point is being compared to β ≈ 0.27° and show the numeric offset in σ units (e.g. “|βpred − βobs| / σobs ≈ 0.8”).  
  - Clarify wording to something like “lies within 1σ of the observed value” instead of “matches at 1σ,” and distinguish between the “Eskilt” βobs and the summary βcombined.  
  - If the intent is to highlight a specific σ‑level (e.g. “0.8σ agreement”), quote that number; otherwise, avoid quantitative phrases that hide the actual delta/σ.  

---

P2-M7 (MAJOR) – Abstract p.1 vs. Sec. 3 body – “fphoton × C0 = 1.73 ± 0.44” lacks traceable definition and numerical origin  
- **Location:** Abstract p.1; Sec. 3.2 p.2; Sec. 3.3 p.2–3  
- **Problem:** The abstract emphasizes “an effective photon coupling fphoton × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning).” In the body, Eq. (5) simply restates this number without derivation; there is no definition of fphoton, no connection to gaγ = C0/fa in Eq. (2), and no explanation of how the uncertainty propagates from βcombined and the assumed cosmology/theory inputs. Sec. 3.3 then introduces different coupling parameters (C, Caγ) without ever tying them back to fphoton. As a result, a central quantitative claim in the abstract has no reproducible derivation in the body. This goes beyond the earlier criticism (P2‑E5) by highlighting an abstract–body mismatch: the abstract frames “order‑unity fphoton × C0” as a key result, yet the body never actually shows how this is obtained or how it relates to the parameters used in the MCMC.  
- **Required fix:**  
  - Define fphoton in Sec. 2 or 3 (dimension, relation to fa and cosmological integrals), write an explicit equation fphoton × C0 = F(β, m, θi, …), and show (even briefly) how inserting βcombined and the fiducial parameter values yields 1.73 ± 0.44.  
  - Ensure the same coupling parameterization is used consistently in the MCMC (Sec. 3.3) and in the discussion/figures, and connect Eq. (8) to Eq. (5).  
  - If such a mapping cannot be made cleanly under the current assumptions, remove this parameter from the abstract or downgrade it to a qualitative statement.  

---

P2-M8 (MAJOR) – Sec. 3.3 p.2–3 vs. Fig. 2 caption p.4 – Missing quantitative comparison of posteriors  
- **Location:** Sec. 3.3 p.2–3; Fig. 2 caption p.4  
- **Problem:** Sec. 3.3 gives numerical posterior means and standard deviations: βALP = 0.336 ± 0.107°, βfree = 0.344 ± 0.096°, βobs = 0.342 ± 0.094°. Fig. 2 caption says “All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094°.” However, the figure is not reproduced in the text provided, and no quantitative measure of “consistency” is given (e.g. Δβ/σ, overlap integrals, Kullback–Leibler distances). Given that the same βobs is explicitly used as the data point in the likelihood, some near‑agreement is expected by construction; the claim that this demonstrates non‑tension is therefore somewhat tautological. This is a case of an unquantified hedge (“consistent with”) hiding the fact that the ALP model βALP is driven very closely to βobs, rather than being an independent prediction.  
- **Required fix:**  
  - Provide a quantitative comparison in the text, e.g. |βALP − βfree| / σ or a statement that the posteriors are statistically indistinguishable given the current error bars.  
  - Clarify that βobs = 0.342 ± 0.094° is the input to the likelihood and that βALP and βfree are merely different parameterizations of the same underlying one‑dimensional posterior, so the agreement is not an independent test of the ALP model.  
  - If Fig. 2 is retained, ensure the axis labels and plotted distributions are explicitly described in the text (e.g. which posterior corresponds to which color or line style).  

---

P2-M9 (MAJOR) – Sec. 4 p.3 & Sec. 6 p.5 – LiteBIRD 9σ claim used inconsistently as both detection and exclusion metric  
- **Location:** Sec. 4 p.3; Sec. 6 bullet 3 p.5; Conclusion p.5–6  
- **Problem:**  
  - Eq. (10) correctly computes 0.27/0.03 = 9, which is the *detection significance* if the true β = 0.27° and LiteBIRD achieves σ(β) = 0.03°.  
  - Sec. 4 then states “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ,” while Sec. 6 calls this “a decisive confirmation or a clean exclusion” and the conclusion repeats “a decisive test at ∼ 9σ statistical significance.”  
  There is no treatment of theoretical uncertainty on β (from C0, θi, cosmology) nor of the fact that the forecasted σ(β) depends on systematics and self‑calibration choices; yet the same 9σ figure is used interchangeably for forecasted detection and exclusion. This goes beyond P2‑E8 by noting the **abstract and conclusion** also frame 9σ as a generic “test significance” without clarifying that it is a very specific benchmark based on fixed fiducial parameters.  
- **Required fix:**  
  - In the abstract, Sec. 4, Sec. 6, and the conclusion, clearly distinguish between “9σ if the true β ≈ 0.27° and σ(β) ≈ 0.03°” (detection) and the more nuanced statement about exclusion: either remove the “9σ exclusion” phrasing or qualify it as applying to this particular benchmark model with fixed C0 θi, etc.  
  - Add at least a brief discussion of theory‑parameter uncertainty, and state whether the forecast treats β as a delta‑function prediction or a distribution; if the latter, adjust the exclusion significance accordingly or refrain from quoting a σ‑level.  

---

P2-M10 (MAJOR) – Sec. 1 p.1 & Conclusion p.5–6 – “Combined Planck + ACT evidence exceeds 3.5σ” not arithmetically or procedurally justified  
- **Location:** Sec. 1 p.1; Conclusion p.5–6  
- **Problem:** The introduction states “The Planck HFI analysis reported β = 0.35 ± 0.14° (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.” The conclusion then refers back to a “3.6σ Eskilt et al. joint Planck + ACT signal.” No explicit calculation is given showing how two “comparable significance” detections combine to > 3.5σ, especially given that the ACT determination itself is not properly sourced. In Sec. 3.2, the only explicit combined result (based on 0.30 ± 0.11° and 0.215 ± 0.074°) yields ≈ 3.94σ, but this is a different combination and arises from different central values and uncertainties. The paper never explains how the 3.6σ figure is derived or how it relates to the 3.9σ from Eq. (4), leading to internally inconsistent “combined significance” statements.  
- **Required fix:**  
  - Provide a transparent calculation of the combined significance for whichever datasets you actually intend (e.g. Minami+Komatsu Planck HFI + a real ACT measurement or WMAP+Planck Eskilt). If the combination yields 3.6σ, show the numbers; if it yields 3.9σ, use that consistently.  
  - Remove generic statements like “combined, the evidence exceeds 3.5σ” unless they are backed by a clear reference or reproduced calculation in the text.  
  - Ensure that the abstract, introduction, Sec. 3.2, and conclusion all use a single, well‑defined combined significance number derived from published data and clearly labelled as such.  

---

P2-m3 (MINOR) – Eq. (1) p.1 – Dimensional and numerical vagueness in “≈ fa θi × O(1)”  
- **Location:** Eq. (1) p.1; Sec. 2.1 p.1  
- **Problem:** Eq. (1) writes  
  \[
  \Delta\phi \approx f_a \theta_i\Big(1 - \frac{J_0(m/H_0)}{J_0(0)}\Big) \approx f_a \theta_i \times O(1).
  \]  
  Since J0(0) = 1 by definition, the ratio is unnecessary and slightly confusing. The text then notes “For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24; the precise value depends on the cosmological integration…” but does not show even a schematic integral that would yield this 0.24, nor does it explain why “O(1)” is an appropriate characterization when the factor is ~0.24. In Sec. 2.2 this morphs into Δϕ/fa ∼ 10⁻² without an explicit step connecting 0.24 to 10⁻². This is more than a stylistic issue: the combination of “O(1)” and later “10⁻²” muddles the scaling argument and makes it hard for the reader to check whether the 0.27° estimate is dimensionally/numerically consistent.  
- **Required fix:**  
  - Remove the unnecessary Bessel ratio J0(m/H0)/J0(0) and write the expression in the simplest consistent form, e.g. Δϕ/fa ≈ θi × F(m/H0) with F(1) ≈ 0.24, providing a reference or a brief derivation of F.  
  - Replace “× O(1)” with the explicit numerical factor you actually use downstream; if that factor is not O(1), avoid the O(1) notation and instead emphasize the actual magnitude.  
  - Tie this explicitly to the later claim Δϕ/fa ∼ 10⁻², or adjust that claim to match the factor derived from Eq. (1).  

---

P2-m4 (MINOR) – Fig. 1 & Fig. 2 captions vs. text – Missing explicit axis labels and units  
- **Location:** Fig. 1 caption p.3; Fig. 2 caption p.4; Sec. 3.3 p.2–3  
- **Problem:** The captions describe triangle plots and comparison of β posteriors but do not specify axis units or the exact quantities plotted (e.g. whether β is in degrees or radians, whether Caγ is dimensionless). The body text quotes β and Caγ × θi numerically but does not cross‑reference the figures with explicit axis descriptions. This leaves room for confusion, particularly given the unit change between Eq. (2) (β in radians) and the rest of the text (β in degrees).  
- **Required fix:**  
  - Amend the captions and/or Sec. 3.3 text to state clearly that β is plotted in degrees, that Caγ is dimensionless (if so), and what ranges are shown on each axis.  
  - Where β is discussed in radians (e.g. β ≈ 5×10⁻³ rad in Sec. 2.2), clarify the unit conversion when comparing to figure results.  

---

P2-m5 (MINOR) – Abstract and Sec. 5–6 – Unqualified “no fine-tuning” and “natural” language  
- **Location:** Abstract p.1; Sec. 2.2 p.2; Sec. 5 p.4; Sec. 6 bullet 1 p.5; Conclusion p.5–6  
- **Problem:** The paper repeatedly uses qualitative phrases such as “no fine-tuning,” “natural prediction,” and “all inputs are at their natural scales” without any quantitative criterion for naturalness (e.g. prior volumes, sensitivity measures). This is particularly delicate because at least one dimensionless parameter (C or C0) is set to a value as large as 8 in Run 1, and the actual required θi range is not specified. While these are not strictly numerical errors, they are unquantified hedges that may overstate how generic the parameter choice is.  
- **Required fix:**  
  - Either provide a quantitative measure of “naturalness” (for example, define a prior range for C0 and θi and compute what fraction of that range yields β within the observed interval), or soften the language to “plausible”/“order‑unity parameters can reproduce the signal” without categorical “no fine-tuning” claims.  
  - Make clear that “natural” here refers qualitatively to fa ∼ MPl and m ∼ H0, not to a formal naturalness measure in the sense used in particle physics or Bayesian model comparison.  

---

NO FURTHER ARITHMETIC DISCREPANCIES FOUND BEYOND THOSE ALREADY FLAGGED  
- All explicitly given σ values derived from a single mean and error (e.g. 0.35/0.14 = 2.5σ; 0.30/0.11 ≈ 2.7σ; 0.215/0.074 ≈ 2.9σ; 0.242/0.061 ≈ 3.97σ; 0.336/0.107 ≈ 3.1σ; 0.344/0.096 ≈ 3.6σ; 0.342/0.094 ≈ 3.6σ; 0.27/0.03 = 9σ) are internally consistent at the arithmetic level.  
- The main issues are **not wrong numeric calculations from given inputs**, but **unjustified or non-traceable inputs**, ambiguous mappings (β → coupling parameters), and inconsistent reuse of σ as if all came from a common null procedure.