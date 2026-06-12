# P1B R35conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.61.pdf` md5=56ec3f27 pages=19
**Input format**: TEXT + web search + pass-2 self-critique (15079 chars)
**Wall time**: 88.1s

---

P1B-E1 – Reference [4] has an impossible arXiv ID  
- **Location:** References section, page 15  
- **Problem:** Reference [4] is listed as “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” The arXiv identifier `2509.13654` corresponds to a future year (2025, September) and does not currently exist on arxiv.org.[7]  
- **Required fix (ESSENTIAL):** Replace this with the correct bibliographic information for the ACT DR6 birefringence analysis actually available at submission time (correct author list, title, arXiv ID, and year). If the DR6 paper is genuinely not yet on arXiv, it must be cited as “in preparation” without a fabricated arXiv ID, and any quantitative result taken from it must either be removed or clearly labeled as provisional and not used as load‑bearing evidence.

---

P1B-E2 – Overstated ACT DR6 detection significance and mis-citation  
- **Location:** Sec. IV, “Birefringence measurements are adopted…”, page 5; again in Sec. VI “Headline observational constraint”, page 9; also References [3]–[4].  
- **Problem:** The text quotes “β = 0.215◦ ± 0.074◦ (ACT DR6 [4])” and later uses this in an inverse‑variance combination to claim a joint 3.9σ significance (Eq. (4)). The only ACT birefringence constraints currently in the literature are pre‑DR6 and have different values and uncertainties than quoted here. There is no verifiable ACT DR6 birefringence paper with β = 0.215◦ ± 0.074◦ or arXiv:2509.13654.[7]  
- **Required fix (ESSENTIAL):**  
  - Replace the ACT value with an actually published ACT birefringence measurement (correct β, σβ, reference) *or* explicitly label the DR6 number as an internal/forecast value without a bibliographic citation and do not use it in any formal combined-significance calculation.  
  - Remove Eq. (4) as a claimed 3.9σ “auxiliary cross-check” unless it is recomputed using only published, verifiable measurements and a correct treatment of correlated systematics (see next item).  
  - Update [4] to the real ACT birefringence reference or clearly mark the ACT number as “private communication” and de‑emphasize it (no quantitative headline).

---

P1B-E3 – Unsupported 3.9σ combined-significance claim from Planck+ACT  
- **Location:** Sec. VI, paragraph “Summary-likelihood combination (auxiliary cross‑check).”, page 10.  
- **Problem:** Eq. (4) claims a combined value and significance “βcombined = 0.241◦ ± 0.061◦ (3.9σ)” built from the Planck NPIPE β = 0.30◦ ± 0.11◦ and ACT DR6 β = 0.215◦ ± 0.074◦ measurements. The ACT DR6 measurement is not traceable to a published paper, and the Planck NPIPE number is actually from Diego‑Palazuelos et al. (PRL 128, 091302), which quotes β ≈ 0.30◦ ± 0.11◦ based on PR4 data.[3] Moreover, the text acknowledges the presence of shared calibration systematics but still presents 3.9σ as an “inverse‑variance” combination, which is mathematically inconsistent with the presence of positive correlations (the nominal σ is too small). No ACT DR6 paper provides that combined estimate.  
- **Required fix (ESSENTIAL):**  
  - Remove the 3.9σ combined-significance claim from the paper, or relegate it to a clearly marked “toy” calculation, with an explicit warning that it is not physically meaningful because correlated systematics are ignored.  
  - The only robust headline significance must be directly taken from a published joint analysis with a documented covariance (e.g., Eskilt & Komatsu WMAP+Planck 3.6σ).  
  - Ensure that any appearance of “3.9σ” is accompanied by a clear statement that it is *not* a published measurement and not reliable for inference.

---

P1B-E4 – Future-dated ACT DR6 reference used as if published  
- **Location:** Throughout Sec. IV and VI; References [3] and [4], page 15.  
- **Problem:** The paper treats ACT “data release 6” as if it were fully analyzed and published, including calibrated birefringence values and uncertainties, yet the cited arXiv entry is future‑dated and non-existent (arXiv:2509.13654).[7] Using non‑existent future data in a PRD submission is unacceptable.  
- **Required fix (ESSENTIAL):**  
  - Strip all “DR6” load‑bearing quantitative content unless it can be matched cleanly to a published arXiv or journal article with correct metadata.  
  - If the intention is to anticipate an upcoming DR6 analysis, this must be stated plainly and any numbers labeled as “anticipated / internal” and not used in formal consistency checks or forecasts.  
  - Adjust the narrative so that all load‑bearing birefringence constraints are drawn from verifiable sources (primarily Eskilt & Komatsu 2022 and Diego‑Palazuelos et al. 2022).

---

P1B-E5 – Use of a non-existent ACT DR6 paper in the bibliography  
- **Location:** References [4], page 15.  
- **Problem:** Reference [4] describes an ACT DR6 birefringence paper as an “arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO]”. No such entry exists on arXiv or NASA ADS; the date and identifier are speculative.[7] PRD standards do not permit fabricated or anticipated citations.  
- **Required fix (ESSENTIAL):**  
  - Either replace [4] by a properly identified, actually existing ACT birefringence paper (with correct arXiv ID, title, author list, and year) or remove it entirely.  
  - If no ACT birefringence paper beyond Eskilt & Komatsu exists at submission, drop ACT as an independent constraint rather than citing a non-existent preprint.

---

P1B-M1 – Inconsistent labeling and use of “PR4/NPIPE” vs “PR3” in reference [5]  
- **Location:** Footnote “a” on page 1; Reference [5], page 15.  
- **Problem:** Footnote “a” correctly states that the *published* Eskilt & Komatsu paper analyzes Planck PR3 + WMAP9, while the public code repository has been updated to PR4/NPIPE. The main text sometimes refers to “PR4/NPIPE likelihoods” in connection with the repository, and elsewhere to “the abstract β = 0.342◦ ± 0.094◦ (3.6σ) headline.” If any numerical value in the body is taken from the PR4 rerun rather than the published PR3 analysis, this must be clearly distinguished.  
- **Required fix (MAJOR):**  
  - Explicitly tag every usage of β = 0.342◦ ± 0.094◦ as “Eskilt & Komatsu PR3+WMAP9 published summary likelihood” and state unambiguously that *no* result from the PR4/NPIPE rerun is used in this paper’s inference.  
  - If any numbers are actually taken from the PR4 repository instead of the published article, those must be re‑checked against the published PRD version and adjusted, or the paper must state that it is using the repository rerun and not the journal result.

---

P1B-M2 – Overstated independence of “verification” results vs. cited literature  
- **Location:** Abstract, lines “Both frozen dataset combinations find ∆Neff consistent with zero… and H0 consistent with standard ΛCDM”; also Sec. II–III, and conclusions.  
- **Problem:** The paper frames the ΛCDM+ΔNeff analysis as an independent “null-consistency test” but the results (e.g., H0 ≈ 67.7, Neff consistent with 3.046) essentially reproduce Planck 2018 + BAO + SN standard results. The text occasionally gives the impression of novelty (“Independent cross-validation”) without clearly acknowledging that these constraints are numerically almost identical to Planck’s baseline results and add little new information. Planck 2018 cosmological-parameter constraints are well established.  
- **Required fix (MAJOR):**  
  - Tightly qualify claims of “independent verification/cross‑check” and explicitly state that the MCMC proxy reproduces existing Planck+BAO+SN constraints within uncertainties and does not add statistically significant new information.  
  - Remove or soften any phrasing that suggests a new or sharper constraint compared to the primary Planck analyses.

---

P1B-M3 – Unsupported or hard-to-trace numerical cross-checks  
- **Location:** Sec. II–III and Table I, page 17; multiple footnotes in Sec. III.  
- **Problem:** The manuscript contains numerous very precise internal reconciliation numbers (e.g., specific burn‑in fractions, sample counts such as “176,240 × 0.7 ≈ 123,368” and “216,432 post-burnin samples”; tension-overlap integrals for S8). These are purportedly derived from the author’s GitHub/HuggingFace artifacts, not from the cited literature. While this is not a citation error per se, PRD readers cannot independently verify these chain-level quantities without accessing non‑archival resources.  
- **Required fix (MAJOR):**  
  - For any key quantitative conclusion that depends on these internal diagnostics (e.g., the S8 tension levels quoted as 2.6σ vs. 2.0σ), provide a minimal derivation in the text (show the formula and enough numbers to recompute).  
  - Archive the exact chain files via a DOI (e.g., Zenodo) rather than only via GitHub/HuggingFace, and cite that DOI explicitly in the Data Availability section so the results are traceable in the long term.

---

P1B-M4 – Ambiguous treatment of correlated systematics in combined β constraints  
- **Location:** Sec. IV and VI, especially the discussion around Eq. (4), pages 5–10.  
- **Problem:** The paper acknowledges that Planck and ACT share polarization-angle calibration systematics, which makes naïve inverse-variance combination inappropriate, yet proceeds to use such a combination for an “auxiliary cross-check” (3.9σ). There is no citation to any work that has quantified the correlation coefficient or validated that the approximate combination is adequate. Eskilt & Komatsu’s joint WMAP+Planck analysis is the proper treatment here.[5]  
- **Required fix (MAJOR):**  
  - Either remove Eq. (4) entirely or rephrase it as a purely illustrative arithmetic example, with explicit text that it does *not* represent a statistically valid joint constraint because correlation has been ignored.  
  - Do not interpret or describe 3.9σ as “evidence”; the only statistically robust significance to quote here should be the published 3.6σ from Eskilt & Komatsu.

---

P1B-M5 – Companion papers [1], [6], [7],  are described as “posted concurrently on arXiv”  
- **Location:** References [1], [6], [7], , page 15; early in Introduction.  
- **Problem:** These four “Paper I(a), II, III, IV” references are described as “companion paper, posted concurrently on arXiv” but are not given arXiv identifiers. For citation forensics, they are effectively unpublished manuscripts. Some load‑bearing claims (e.g., the ECH structural-closure theorem) are delegated to Paper I(a).[1]  
- **Required fix (MAJOR):**  
  - Provide actual arXiv IDs for all four companion papers if they have been posted; otherwise, describe them as “unpublished manuscripts” and adjust the language to avoid implying that they are publicly archived.  
  - Ensure that all results essential to this paper’s logic (e.g., which aspects of torsion are ruled out) are either summarized sufficiently here or explicitly stated to be beyond this companion’s scope, without relying on a non‑archived companion as a black box. PRD does not require all details in a single paper, but it does require that citation targets exist and are accessible.

---

P1B-M6 – Claim that ΔNeff result “confirms” minimal matter-bounce prediction  
- **Location:** Sec. III, “Physics interpretation (Table II).”—pages 3–4.  
- **Problem:** The text states that the proxy run “confirm[s] ΔNeff = −0.020 ± 0.169 (full-tension) and +0.058 ± 0.179 (Planck+BAO+SN) is therefore consistent with the minimal matter-bounce prediction.” Minimal-matter-bounce models predict ΔNeff ≈ 0; Planck 2018 already gives Neff ≈ 2.99 ± 0.17. This paper’s ΔNeff constraints are essentially the same as Planck’s; they do not constitute an independent confirmation of the bounce model but simply show that the data do not prefer extra species.  
- **Required fix (MAJOR):**  
  - Rephrase “confirm” to “are consistent with” and make explicit that current ΔNeff constraints are too weak to distinguish minimal matter-bounce from ΛCDM.  
  - Where possible, cite canonical Neff limits from Planck 2018 to show that the new run is not strengthening the constraint materially.

---

P1B-M7 – Abstract and body conflate “quintom” phenomenology with established evidence  
- **Location:** Sec. V, Table II and surrounding discussion, pages 8–9; Conclusions, page 12.  
- **Problem:** The text describes 4.3σ and 3.6σ departures of w0, wa from ΛCDM using an overlap-uncorrected SN likelihood product that double-counts about 20% of SNe and applies different Malmquist corrections. This is correctly flagged as a caveat later, but earlier sentences could be read as implying strong evidence for phantom crossing. This conflicts with more conservative analyses (e.g., Pantheon+ and DES-Y5 individually) that find much weaker evidence for time-varying w.  
- **Required fix (MAJOR):**  
  - In every place where 4.3σ or 3.6σ are quoted, immediately re‑attach the overlap/covariance caveat and state that these are *provisional* internal posterior distances not suitable for model selection.  
  - Avoid phrasing that could be misconstrued as a claim of definitive evidence for quintom behavior, given that the methodologically correct joint SN analysis has not yet been done.

---

P1B-m1 – Minor metadata inaccuracies in citations  
- **Location:** References section.  
- **Problems:**  
  -  Riess et al. is described as “The Astrophysical Journal Letters 934, L7 (2022).” In fact, ApJ 934, 7 (2022) is not in the Letters section; the official designation is ApJ 934, 7.  
  -  Planck 2018 is listed correctly, but the title is slightly paraphrased compared to the journal version (this is acceptable but should ideally match A&A 641, A6).  
- **Required fix (MINOR):**  
  - Correct  to “Astrophysical Journal 934, 7 (2022)” or the exact journal style used by PRD, and double-check all reference titles and venues against ADS to ensure precise reproduction.

---

P1B-m2 – Use of “posted concurrently on arXiv” without persistent IDs  
- **Location:** References [1], [6], [7], , page 15.  
- **Problem:** “Posted concurrently on arXiv” is vague and non‑persistent; readers cannot easily locate the exact version used.  
- **Required fix (MINOR):**  
  - Once arXiv IDs exist, update all four references with arXiv:YYMM.NNNNN and remove “posted concurrently” language.  

---

P1B-m3 – Effect size framing for σ-level claims  
- **Location:** Multiple places where σ is quoted (e.g., abstract 3.6σ, Table II).  
- **Problem:** The instructions you supplied require that each σ headline carry an effect size. For most external results (e.g., 3.6σ Eskilt–Komatsu), this is fine because β and σβ are quoted. Internally, the 4.3σ and 3.6σ deviations of w0 and wa are given with their absolute shifts, but not always clearly contextualized in terms of impact on, e.g., distances or H(z).  
- **Required fix (MINOR):**  
  - For internal σ-level claims (w0, wa, S8, ΔNeff), add 1–2 sentences explaining the corresponding effect sizes (e.g., fractional change in H(z) at z~0.5, or in S8), so readers can gauge practical significance.

---

P1B-n1 – Slightly confusing mix of PR3 vs. PR4 labels in text and footnote  
- **Location:** Footnote “a”, page 1; Sec. IV, “Planck NPIPE” mention.  
- **Problem:** The interplay between PR3 (published Eskilt & Komatsu) and PR4/NPIPE (code rerun) is somewhat intricate and could confuse readers.  
- **Required fix (NIT):**  
  - Tighten the wording in footnote “a” so that it is crystal clear: this paper only uses the scalar Gaussian summary β, σβ from the *published PR3+WMAP9* analysis; PR4/NPIPE reruns in the GitHub repository are not used here.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core ΛCDM+ΔNeff and NaMaster pipeline work appears broadly consistent with established results, but the paper contains serious citation and provenance problems: a non‑existent future arXiv ID for ACT DR6 birefringence, quantitative use of an unsupported ACT DR6 β and an over‑optimistic combined-significance claim (3.9σ), and over‑strong language around “confirmation” of bounce predictions and quintom behavior. These issues violate PRD standards for bibliographic accuracy and statistical rigor and must be corrected before the work can be considered. If the ACT DR6 content is removed or replaced by verifiable references, and all σ‑level claims are recalibrated against properly published results with clear caveats, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E6 – Several σ-level and “tension” numbers are arithmetically inconsistent or mix incommensurate null procedures  
- **Location:** Sec. III (Hubble-tension discussion), Table I caption and text around S8, Sec. III “Key finding” paragraph, Sec. VII; also overlap with Table II S8 commentary.  
- **Problem:**  
  - The abstract and Sec. II–III state that the ΛCDM+ΔNeff proxy finds “H0 consistent with standard ΛCDM,” but the text repeatedly describes a “canonical 3.6σ Hubble tension” using the local SH0ES value, which is based on a very different likelihood from the Planck+BAO+SN chain, and the actual chain-level offsets quoted are 3.2σ (MB) or ≈4.0σ in H0 (67.68 ± 1.06 vs 73.04 ± 1.04 gives ΔH0 = 5.36 and σcomb ≈ 1.49 → 3.6σ only if *one* of the error bars is ignored or reduced). The mapping between the MB-offset 3.2σ and the H0-axis “canonical 3.6σ” is not recomputed explicitly from the numbers given and conflates at least three distinct tension diagnostics (chain σMB, Riess et al. uncertainty, and full covariance).  
  - In Table I, the 2.6σ and 2.0σ S8 “tension” values are described via overlap integrals and “two-Gaussian” combinations, but the paper does not show the underlying Gaussian parameters it uses to back those σ claims beyond the quoted 0.827 ± 0.010 and 0.776 ± 0.017. The stated 2.6σ (for Planck+BAO+SN vs DES-Y3) is approximately correct (ΔS8 = 0.051, σcomb ≈ 0.0199 → 2.6σ), but the 2.0σ for the full-tension posterior versus DES-Y3 is presented as if it were directly comparable, despite the full-tension posterior *including* the DES-Y3 Gaussian prior as an active likelihood. This is not just a conceptual issue: the text repeatedly labels this as a “tension” number, but in fact it is a *within-stack* posterior shift.  
  - The paper therefore juxtaposes σ values from: (i) external‑vs‑external comparisons (Planck+BAO+SN vs DES-Y3); (ii) internal vs external (full-tension posterior vs DES-Y3 which is already in the stack); and (iii) MB-offset σ in the joint MB–H0 plane, without explicitly warning that these derive from different null procedures and are not directly comparable as “tension levels.”  
- **Required fix (ESSENTIAL):**  
  - Explicitly recompute and show the formulas for all σ and “tension” values in Sec. III and Table I (H0, MB, S8), including which uncertainties and covariances are used in each case.  
  - For the full-tension S8 result, clearly re-label the 2.0σ as an internal posterior displacement relative to the DES-Y3 prior hyperparameters, and state that it is *not* a survey‑vs‑survey tension.  
  - Clarify that the “canonical 3.6σ Hubble tension” is not recomputed from the proxy chain but taken from the literature, and avoid implying it was derived from the MB-offset 3.2σ number.  
  - Add explicit language wherever multiple σ-values are compared (H0, S8) to state that they arise from different null procedures and should not be read as directly comparable statistics.

---

P1B-E7 – Abstract and body claim “H0 consistent with standard ΛCDM” without quantifying the residual SH0ES tension  
- **Location:** Abstract, first paragraph; Sec. II first paragraph; Sec. III “Key finding” and MB–H0 tension discussion; Conclusions, “ΛCDM+ΔNeff MCMC proxy.”  
- **Problem:** The abstract asserts that both dataset combinations find “H0 consistent with standard ΛCDM,” but the only ΛCDM baseline actually used in the text is the Planck+BAO+SN configuration and the SH0ES local distance-ladder value. The proxy chains reproduce Planck-dominated H0 ≈ 67.7 km s−1 Mpc−1; the tension with SH0ES ≈ 73 km s−1 Mpc−1 is described qualitatively as “canonical 3.6σ,” yet the paper does not give a chain-based comparison or a concrete number for how close the proxy H0 is to Planck 2018’s published H0. Instead, “consistent with standard ΛCDM” could be read as implying that H0 is *also* consistent with SH0ES when extended by ΔNeff, which the body text explicitly denies (“does not resolve the Hubble tension”).  
- **Required fix (MAJOR):**  
  - Amend the abstract and corresponding body text to state explicitly that “H0 is consistent with the Planck ΛCDM value and remains in ≳3σ tension with SH0ES,” with a quantified σ (computed from the numbers given) and a citation to the Planck 2018 H0.  
  - Make clear in the abstract that the ΔNeff extension *fails* to reduce the existing Planck–SH0ES tension in a statistically meaningful way, and that “consistent with standard ΛCDM” refers to agreement with Planck’s baseline ΛCDM constraints, not an independent cross‑check.

---

P1B-M8 – Abstract claims a “NaMaster pipeline SNR consistent with ACT-noise floor” without explicit numerical comparison  
- **Location:** Abstract (NaMaster analysis description); Sec. IV “Production 500-realization run,” “Sky-fraction sweep,” and “Robustness battery and bias attribution.”  
- **Problem:** The abstract states that pipeline SNR values are “not competitive sky measurements” and are “consistent with the ACT-noise floor,” but the body only gives internal template-fit SNR numbers (20.32, 25.71) and per-realization σβ for synthetic skies; it never directly compares these to published ACT measurement uncertainties or ACT per‑patch σβ values. The reader must infer consistency from order‑of‑magnitude arguments.  
- **Required fix (MAJOR):**  
  - Add an explicit quantitative comparison: for example, state the ACT DR6 per-sky σβ (or the published β uncertainty ∼0.074°) and show how the pipeline σβ ∼0.046° at fsky = 0.32 scales to an ACT-like footprint, including any difference in noise level, number of seasons, and sky fraction.  
  - Rephrase “consistent with the ACT-noise floor” to “of the same order as the ACT DR6 per-sky uncertainty” with the numerical factors shown, or soften the claim if the pipeline numbers are actually significantly better or worse than realistic ACT systematics.

---

P1B-M9 – Dimensional consistency and normalization of the β–ALP relation are not fully transparent  
- **Location:** Sec. VI “Birefringence value” and Eq. (3); surrounding ALP parameter discussion and Appendix C.  
- **Problem:** Equation (3) uses \(β ≈ \frac{α_{\rm EM}}{4π} C_{aγ} \frac{Δϕ}{f_a}\) and then converts to degrees as “4.93 × 10⁻³ rad × 180°/π ≈ 0.28°” without explicitly showing how the dimensionless combination \(Δϕ/f_a\) arises from the ODE integration. The text asserts ∆ϕ/fa ≈ 1.06 for m = 3.9H0 and θi = 1, but it is not immediately obvious how this matches the quoted prefactor 4.93 × 10⁻³ rad (since αEM/(4π) ≈ 5.8 × 10⁻⁴ and Caγ = 8; this alone gives ≈4.6 × 10⁻³ even before multiplying by 1.06—there is a slight numerical mismatch). While small, in a technical verification companion the normalization should be shown step‑by‑step.  
- **Required fix (MAJOR):**  
  - Explicitly show the arithmetic: (i) compute αEM/(4π), (ii) multiply by Caγ, and (iii) multiply by the specific ∆ϕ/fa value used (e.g. 1.06) and then convert to degrees.  
  - Confirm that the 4.93 × 10⁻³ rad prefactor is consistent with those inputs or correct it if necessary, and state clearly whether that prefactor already includes ∆ϕ/fa or not.  
  - Add one sentence clarifying that β is dimensionless (an angle in radians) and that the ODE integration returns ∆ϕ/fa as dimensionless as well, so the left-hand side and right-hand side of Eq. (3) have matching units.

---

P1B-M10 – Several internal σ and “effect size” statements still lack explicit physical impact quantification  
- **Location:** Sec. III “Physics interpretation (Table II)” and “Caveats”; Table II note for wpivot; Sec. V.B “Results”; Conclusions paragraph “Exploratory w0 wa cross‑check.”  
- **Problem:** The revised text improves over generic σ headlines by quoting w0, wa, wpivot, and S8 values, but the physical impact of these deviations remains only partly quantified. For example, the paper notes that wpivot = −0.952 ± 0.019 is +2.5σ from −1, and that w0 and wa differ from ΛCDM by 4.3σ and 3.6σ, but the only “effect size” explanation is that the CPL trajectory crosses w = −1 at z× ≈ 0.39; there is no explicit statement about the corresponding fractional change in H(z), distances, or growth at a representative redshift, which your own instructions require for σ-level claims. Similar issues remain for the S8 tension: σ-levels are given, but percentage differences in S8 or σ8, and their impact on clustering amplitudes, are not spelled out.  
- **Required fix (MAJOR):**  
  - For the w0–wa posterior, add one or two sentences quantifying the implied fractional change in H(z) or luminosity/angular diameter distance at a representative redshift (e.g., z ≈ 0.5) relative to ΛCDM.  
  - For S8, explicitly state the fractional change (e.g., “the Planck+BAO+SN S8 is ≈6–7% higher than DES‑Y3”) and describe qualitatively what this means for matter clustering amplitudes.  
  - Ensure that every internal >2σ claim (w0, wa, S8, ΔNeff) is accompanied by such an effect‑size description, not just a σ number.

---

P1B-M11 – Some “consistency / compatibility” hedges remain unquantified or ambiguous  
- **Location:**  
  - Sec. II: “spin-torsion framework alone does not resolve cosmological tensions at the present data precision.”  
  - Sec. III: “the proxy run confirming ΔNeff … is therefore consistent with the minimal matter-bounce prediction.”  
  - Sec. VI: multiple uses of “consistent with” (e.g., βALP vs βobs, βfree vs βobs, “consistent with the model-independent fit”).  
- **Problem:** Several of these “consistent with / does not resolve / not a discriminator” statements are qualitative and rely on reader inference. For example, “spin-torsion framework alone does not resolve cosmological tensions” is not numerically anchored: it would be clearer to specify that the proxy H0 differs from SH0ES by ≳3σ and that the ΔNeff posterior is consistent with 0 at <0.5σ. For the ALP section, many “consistent with” phrases do quote β and σβ, but at least one (ΔNeff vs minimal bounce) uses Planck’s baseline Neff only implicitly.  
- **Required fix (MAJOR):**  
  - For each “consistent with” in the cosmology sections (ΔNeff, H0, S8), add the explicit Δ/σ or posterior interval demonstrating that consistency numerically.  
  - For the ALP consistency claims, ensure that every “consistent with βobs” statement either references the exact Δ/σ it uses (as is partly done for βALP vs βobs) or is removed as redundant.  
  - Where the text says the spin‑torsion framework “does not resolve tensions,” explicitly state the before/after tension σ, so the reader can see how ineffective the extension is in quantitative terms.

---

P1B-m4 – A few internal cross‑references still point to places that no longer carry the promised content  
- **Location:**  
  - Sec. III, footnote about COUNT_EXPLANATION.md and “convergence summary.json”;  
  - Appendix A “HuggingFace datasets” and “reproduce cosmology.sh” references;  
  - Table V note on “program‑wide content used by Paper IV, not by this paper’s analyses.”  
- **Problem:** The manuscript frequently refers the reader to repository files (COUNT_EXPLANATION.md, convergence CSVs, implementation maps) and HuggingFace datasets for verification. This is fine in principle, but for a PRD submission the *paper itself* must be internally consistent: the cross‑references should point to sections or appendices where the essential formulas or configurations are summarized, not solely to external resources. At present, some statements (“per-parameter convergence tables are archived at … and mirrored in the HuggingFace dataset”) leave the reader with no in‑paper description of what those tables contain; similarly, “reproduce cosmology.sh (∼4–12 h per configuration on 4 CPU cores)” is mentioned without a brief summary of its key options.  
- **Required fix (MINOR):**  
  - For each external-file cross-reference that is used as part of a logical argument (e.g., chain counts, convergence, priors), add a brief in‑paper summary of the relevant content (e.g., list which parameters are sampled, typical ESS ranges, or key YAML settings).  
  - Check all “see Appendix A” and file-name references to ensure the reader can understand the essential point without having to run code; adjust wording where necessary (e.g., “the detailed script is provided in the repository; here we summarize the relevant settings as follows…”).

---

P1B-m5 – Abstract–body fidelity: NaMaster and ALP sections oversell “verification” relative to what is actually demonstrated  
- **Location:** Abstract (description of the three analyses); Sec. IV (NaMaster), Sec. VI (ALP), Conclusions.  
- **Problem:** The abstract calls this a “technical verification companion” and describes the NaMaster run as “pipeline validation” and the ALP exercise as a “consistency check,” which is appropriate, but the body text occasionally edges into stronger language—for example, stating that the NaMaster exercise “confirms the algebraic pseudo-Cℓ E → B deconvolution under MASTER mode coupling” and that ALP evolution “accommodates the observed signal.” Without a direct comparison to independent code (for NaMaster) or to alternative parity-violating models (for ALP), “confirms” is arguably stronger than warranted for a single-pipeline internal Monte Carlo.  
- **Required fix (MINOR):**  
  - Soften “confirms the algebraic pseudo-Cℓ E → B deconvolution” to “is consistent with the expected algebraic pseudo-Cℓ E → B deconvolution” or similar, acknowledging that this is a single‑code MC test.  
  - In the ALP section and conclusions, ensure the wording consistently refers to “accommodates” and “is consistent with,” and avoid phrasing that could be read as a *verification* of the mechanism relative to rivals (you already largely do this; a final pass to remove any lingering “predicts” or “confirms” language would align the abstract and body perfectly).  

---

P1B-n2 – Minor arithmetic and rounding clarifications  
- **Location:**  
  - Table II footnote (wpivot calculation and σwpivot);  
  - Sec. IV “Sky-fraction sweep” standard error estimates;  
  - Sec. VI “LiteBIRD forecast” (9σ forecast, 0.7σ separation).  
- **Problem:** The wpivot arithmetic is correct but compressed; for a verification paper, some numbers are given without rounding explanations (e.g., wpivot = −0.952 vs intermediate values like −0.8122 – 0.210×0.6666). The LiteBIRD “∼9σ” and “≈0.7σ” figures are numerically reasonable, but readers have to mentally recompute them from the given 0.27°, σ(β) ≈ 0.03°, and βobs = 0.342 ± 0.094°.  
- **Required fix (NIT):**  
  - Add one line to the wpivot footnote showing the numerical intermediate: e.g., “−0.8122 + 0.210×(−0.6666) = −0.8122 – 0.1400 ≈ −0.952”.  
  - In the LiteBIRD paragraph, explicitly show “0.27°/0.03° ≈ 9” and “|0.342–0.27|/√(0.032²+0.094²) ≈ 0.7” so the reader does not have to reconstruct the calculation.  

---

If you address the earlier citation/ACT issues and the new points above—especially the σ/tension arithmetic and the comparability caveats—the manuscript will come much closer to PRD’s standards for quantitative and statistical rigor.