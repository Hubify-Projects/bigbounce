# P2 auto-2026-06-05_1418pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11618 chars)
**Wall time**: 84.8s

---

P2-E1  
Section: Abstract, page 1  
Problem: The abstract cites “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis” and “3.6σ isotropic birefringence signal.” I cannot find any “Eskilt et al.” joint Planck+ACT birefringence paper in arXiv or the literature, nor any result with those exact numbers. Eskilt & Komatsu (2022) is WMAP+Planck only, with β ≈ 0.30° ± 0.11°, not including ACT.[2][3] There is also no public “joint Planck + ACT” 3.6σ result traceable to an existing paper.  
Required fix: Either provide a verifiable published or posted arXiv reference that reports β = 0.342 ± 0.094° from a true Planck+ACT joint analysis, or clearly state that this is the author’s own combined re-analysis (with methods and data described) and remove attribution to “Eskilt et al.” If no such external analysis exists, remove the “Eskilt et al. joint Planck + ACT analysis” phrasing and any numeric claim that cannot be traced to a cited paper.

P2-E2  
Section: 1 Introduction, page 1  
Problem: “The Planck HFI analysis [Minami and Komatsu, 2020] reported β = 0.35 ± 0.14° (2.5σ)…” Minami & Komatsu (2020) indeed report β ≈ 0.35° ± 0.14° in PRL 125, 221301.[1] However, the ACT DR6 analysis and “combined >3.5σ” claim are not supported by any existing ACT DR6 birefringence paper. No paper by “Diego-Palazuelos and Komatsu” on ACT birefringence can be found; ACT cosmic birefringence results (if any) are not yet in the literature under that authorship.[3][4] The quoted ACT number “β = 0.215 ± 0.074° (2.9σ)” also does not trace to any known result.  
Required fix: Correct the ACT reference to an actual paper (or remove entirely if unpublished), and only quote constraints that appear in that paper. If these numbers are an internal or projected ACT DR6 analysis, they must be clearly labeled as such (and likely removed for a PRD methods paper relying on public data). Adjust or remove the “combined, the evidence exceeds 3.5σ” statement unless it is recomputed from published measurements with a transparent method in the text.

P2-E3  
Section: 3.1 Datasets, page 2  
Problem: The reference “[Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ)” is not traceable. Searching arXiv, ADS, and major preprint servers returns no paper with those authors on “Cosmic birefringence from the Atacama Cosmology Telescope.”[3][4] There is no arXiv identifier, journal, or DOI, and the year “2025” is in the future relative to current ACT birefringence literature. This looks like a fabricated or speculative citation.  
Required fix: Either (a) replace this with a real, posted ACT birefringence paper (with correct authors, year, and numbers), or (b) remove this dataset entirely and redo all derived quantities (combined constraint, Bayes factor, etc.) using only verified public data, or clearly mark it as a private communication / projection and avoid using it as if it were a published constraint.

P2-E4  
Section: 3.1 Datasets, page 2, and throughout  
Problem: Multiple derived quantities rely on the unverified ACT DR6 dataset and the unverified “Eskilt et al. joint” value, including:  
- Eq. (4) βcombined = 0.242 ± 0.061° (3.9σ)  
- f_photon × C0 = 1.73 ± 0.44 (Eq. 5)  
- The Bayes factor ln B = 5.17 (Sec. 3.4)  
- Several “3.6σ” claims in abstract and conclusion.  
Since at least one of the input measurements is not tied to a verifiable published result, all dependent numbers lack a solid evidential basis.  
Required fix: Recompute all combined constraints and Bayesian evidences using only datasets that are documented in the literature and correctly cited. Provide explicit calculation steps so another reader can reproduce Eq. (4) and Eq. (5) from the referenced measurements. Remove or clearly qualify any result that depends on unpublished or unverifiable inputs.

P2-E5  
Section: 3.1 Datasets, page 2; References, page 6  
Problem: The citation to “Eskilt and Komatsu, 2022” is incorrect in details. The referenced paper is by “J. R. Eskilt and E. Komatsu” in Phys. Rev. D 106, 063503 (2022), titled “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data,” which is correctly given in the reference list.[2] However, the text says “Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11° (2.7σ)”. The actual headline constraint in that paper is β ≈ 0.30° ± 0.11° (consistent), but the description as purely “Planck NPIPE” is incomplete: the analysis uses both WMAP and Planck data. Calling it “Planck NPIPE” alone could mislead and does not match the paper’s scope.  
Required fix: Clarify that the result is from a WMAP+Planck (NPIPE) analysis, and explicitly state where in Eskilt & Komatsu (2022) the quoted value comes from (e.g., main result or specific data combination). Ensure the exact numbers (0.30 ± 0.11°) match a specific entry in their tables or summary.

P2-E6  
Section: 3.2 Summary-Likelihood Inference, Eq. (4), page 2  
Problem: The combined constraint βcombined = 0.242 ± 0.061° is claimed to be derived from the two measurements in Sec. 3.1. If one uses standard inverse-variance weighting on β1 = 0.30 ± 0.11° and β2 = 0.215 ± 0.074°, the combined mean is  
\[
\barβ = (β_1/σ_1^2 + β_2/σ_2^2)/(1/σ_1^2 + 1/σ_2^2) \approx 0.241°,
\]  
and the combined error is  
\[
σ ≈ (1/σ_1^2 + 1/σ_2^2)^{-1/2} ≈ 0.062°,
\]  
which is compatible within rounding. However, since β2 itself is not traceable to a published result (P2-E3), the numerical correctness is moot—its provenance is not secure.  
Required fix: Once the datasets are restricted to verifiable measurements, redo the combination and show the explicit calculation leading to Eq. (4). For PRD standards, the paper should at least outline the weighting and consider possible correlations between datasets (Planck vs. ACT) rather than assuming independence without justification.

P2-E7  
Section: 3.3 MCMC Parameter Estimation, Table 1 and text, pages 2–3  
Problem: The parameter “C” in “Model ALP (C = 8 fixed)” and “ALP (C free)” is ambiguous. Earlier, the notation uses “C0” and “Caγ” for anomaly and coupling parameters. “C” is never clearly defined in the Methods section, yet it appears as a key model parameter in the MCMC runs and in the later statement “Run 2, C free” and “C = 8 fixed.” This is not a citation issue but a clarity defect affecting reproducibility.  
Required fix: Define precisely what “C” is (C0? Caγ? some combination) and ensure notation consistently matches the parameters used in Sec. 2 and Eq. (2). For an inference-based methods paper, ambiguous parameter notation is unacceptable.

P2-E8  
Section: 3.3 MCMC results, Eqs. (6)–(8), page 3  
Problem: The quoted values  
- βALP = 0.336 ± 0.107°  
- βfree = 0.344 ± 0.096°  
- Caγ × θi = 3.4 ± 1.1  
are not directly traceable to any external citations (they are the author’s own results). That is acceptable, but these are then compared to βobs = 0.342 ± 0.094°, again attributed to “Eskilt et al. joint analysis,” which is not verifiable (P2-E1).  
Required fix: Before using βobs as a benchmark, the paper must either derive this value internally from clearly described data/methods or replace it with a published benchmark (e.g., from Eskilt & Komatsu 2022). Otherwise, all claims of “no tension” are based on an unvalidated comparison point.

P2-E9  
Section: 3.4 Bayes Factor, Eq. (9), page 3  
Problem: The paper states “ln B = 5.17 … computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°]. The evidence is prior-dependent: ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].” The indicated Bayes factors are not cross-checked against any citation; they must be internally reproducible. Given βcombined ≈ 0.242 ± 0.061°, a rough Gaussian approximation for evidence against β=0 is consistent with ln B of order 4–6, so the numbers are plausible. However, because βcombined itself depends on an unverified dataset (P2-E3), these Bayes factors are not anchored to published measurements.  
Required fix: Once the dataset is corrected to include only verifiable measurements, recompute ln B and outline the calculation. Also explicitly note that Bayes factors derived from summary Gaussians (rather than full likelihoods) may differ from those obtained from full CMB power-spectrum analyses, to avoid implicit comparison with other works.

P2-E10  
Section: 4 LiteBIRD Forecast, page 3, Eq. (10)  
Problem: The projection “LiteBIRD is projected to achieve σ(β) ≈ 0.03° … [LiteBIRD Collaboration, 2023]” must come from a specific forecast paper. The reference given is “LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky CMB polarization survey. Prog. Theor. Exp. Phys., 2023:042F01, 2023. doi: 10.1093/ptep/ptac150.” This is the well-known LiteBIRD forecast paper, which indeed quotes birefringence sensitivities of order 0.02–0.05° depending on assumptions.[4] However, σ(β) ≈ 0.03° is not explicitly shown in the text as a single canonical number; it depends on analysis choices.  
Required fix: Cite the exact table/figure in the LiteBIRD paper from which σ(β) is read off, or qualify this as “of order 0.03° depending on the self-calibration strategy, consistent with the sensitivities in [LiteBIRD Collaboration, 2023].” The simple 0.27/0.03 = 9σ ratio is dimensionally and numerically fine, but it should be phrased as an approximate forecast.

P2-E11  
Section: 5 Relationship to Bounce Cosmology, page 4; References page 6  
Problem: Two references are listed as:  
- “Houston Golden. Spin-torsion cosmology and the search for geometric dark energy: Structural barriers, perturbation transparency, and surviving predictions. Companion paper, submitted simultaneously, 2026a.”  
- “Houston Golden. Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.”  
No arXiv IDs, journal references, or DOIs are provided. Searches for these titles and author return nothing in arXiv or ADS.[3] These appear to be truly simultaneous submissions, not yet public. For PRD, referencing “companion papers” that are not available to readers and referees is problematic, especially when claims such as “the matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b]” are used.  
Required fix: Either provide arXiv identifiers or published references so the reader can verify the claims, or remove the quantitative claims that depend on these companion papers (e.g., specific fNL value) and only mention them in very generic terms. At minimum, the paper must not rely on unverifiable external results to support its main physics narrative.

P2-E12  
Section: 6 Discussion, page 5  
Problem: “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].” The specific value fNL = −35/8 must be documented in the cited work. Since [Golden, 2026b] is not publicly available, this number cannot be checked. No other citation is provided for this exact value.  
Required fix: Either (a) independently derive or summarize this result in the present paper with sufficient detail, or (b) provide a public reference where this value is established. Otherwise, remove or soften the claim (e.g., “a characteristic O(−4) fNL signal predicted in matter-bounce models”) without a precise uncheckable number.

P2-E13  
Section: 6 Discussion, page 5  
Problem: Claim of novelty: “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.” Fujita et al. (2021) already studied ALP-induced birefringence with Planck-scale decay constants and dark-energy-scale masses and noted that such models can yield β ~ 0.3° consistent with Planck’s signal.[5] Recent work by Namikawa et al. (2025) (Planck constraints on ALPs through isotropic cosmic birefringence) also considers similar parameter ranges.[3][5] The statement risks overstating the novelty and is not clearly separated from prior literature.  
Required fix: Explicitly acknowledge that Fujita et al. (2021) already pointed out that Planck-scale ALPs can explain β ~ 0.3°, and clarify in what precise sense this paper goes beyond (e.g., particular combination with H0-scale mass, explicit summary-likelihood with specific datasets, or LiteBIRD forecast under this model). Rephrase to avoid implying that the parameter identification itself is new if it already appears in the literature.

P2-M1  
Section: Abstract, page 1; Section 7 Conclusion, page 5  
Problem: The abstract claims: “We forecast that LiteBIRD, with σ(β) ≈ 0.03°, will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.” The conclusion similarly states “LiteBIRD will provide a decisive test at ∼ 9σ statistical significance, contingent on the self-calibration strategy and systematic error budget.” This is framed as a very sharp statement but is based on:  
- A signal prediction β ≈ 0.27° that itself depends on somewhat heuristic “order-unity” inputs (Sec. 2.2).  
- A σ(β) figure that is forecast-dependent and may be degraded by systematics.[4]  
There is no discussion of how instrumental systematics, calibration uncertainties, or possible degeneracies could weaken the effective significance; only a brief qualitative comment appears.  
Required fix: Rephrase these claims as conditional and approximate (e.g., “LiteBIRD is expected to achieve σ(β) of order 0.03°, which, if realized and if the signal is truly β ≈ 0.27°, would correspond to a ≳ 9σ detection.”). Explicitly acknowledge that the numerical 9σ should be understood as a best-case statistical forecast, not a guaranteed outcome.

P2-M2  
Section: 2.1 Field Dynamics, Eq. (1), page 1  
Problem: The field displacement expression  
\[
\Delta\phi \approx f_a \theta_i \left(1 - \frac{J_0(m/H_0)}{J_0(0)}\right)
\]  
is presented with a Bessel function J0, and then approximated as Δφ ≈ fa θi × O(1) with “For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24; the precise value depends on the cosmological integration through the matter and dark-energy eras.” There is no citation for the origin of this analytic form, and no derivation or reference to prior work using this approximation. This is non-standard enough that a PRD methods paper should either derive it or cite a source.  
Required fix: Provide a derivation (even in an appendix) or add a citation to literature that obtains a similar Bessel-function solution for a light scalar rolling at late times in FRW spacetime. Clearly state approximations used (e.g., constant H, small-angle approximation), and verify that the numerics are consistent with a proper cosmological integral.

P2-M3  
Section: 2.2 Birefringence Prediction, Eq. (2), page 1  
Problem: Eq. (2) writes β = gaγ Δφ / 2 = C0 Δφ / (2 fa) ≈ C0 θi / 2 × O(1), but later the text states “the cosmological field evolution gives Δφ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27°.” There is an inconsistency: plugging Δφ/fa ~ 10−2 into β = (C0/2)(Δφ/fa) gives β ~ 5×10−3 C0 rad only if Δφ/fa ∼ 10−2 and the extra factor of 1/2 is retained; the text seems to drop factors casually. The “10−2” is not derived, merely asserted. No citation is provided for that numerical estimate, whereas Fujita et al. (2021) provide more careful numerical results for similar models.[5]  
Required fix: Provide an explicit calculation or citation showing that Δφ/fa ~ 10−2 for the chosen parameter range. Maintain consistent factors of 2 between Eq. (2) and the subsequent numerical estimate. For instance, state clearly “For our fiducial model, numerical integration gives Δφ/fa ≈ 0.010, leading to β ≈ (C0 θi/2)× 0.010 ≈ 5×10−3 C0 θi rad ≈ 0.27° for C0 θi ≈ 1.” Without this, the “no fine-tuning” quantitative claim is under-justified.

P2-M4  
Section: 3.3 MCMC Parameter Estimation, page 3, Table 1  
Problem: The MCMC analysis is presented with extremely small sample sizes (720–6840 samples) and only a single Gelman-Rubin metric R̂-1 < 0.01 to claim convergence. While the author acknowledges that these are “modest by modern standards,” the paper then uses these chains to report posteriors, Bayes factors, and “no tension” claims. For a PRD-level methods paper, such limited sampling is not adequate to support precise inference, especially for tails and evidence.  
Required fix: Either re-run the MCMC with substantially larger sample sizes (e.g., ≥ 50,000 effective samples) and present robust convergence diagnostics (multiple chains, autocorrelation times, effective sample sizes), or clearly downgrade the status of these results to exploratory and avoid giving them equal rhetorical weight as the combined summary-likelihood constraints.

P2-M5  
Section: 6 Discussion, page 5  
Problem: The paper states that “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°, and Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints using the full Planck EB spectrum.” The Fujita et al. paper is “Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy,” Phys Rev D 103, 043509 (2021), with doi 10.1103/PhysRevD.103.043509.[5] That is correctly referenced. However, “Namikawa, Murai & Naokawa” seems to be a mis-typing of “Naokawa” vs “Nakao” or similar; there is no public “arXiv e-prints, 2025. In preparation” paper titled “Constraints on axion-like particles from cosmic birefringence” as of now.[3][5] The “in preparation” label plus a future year and no arXiv ID make this effectively unverifiable, and the phrase “superior ALP mass constraints” cannot be checked.  
Required fix: Either provide an arXiv ID or remove the Namikawa et al. (2025) citation until it exists as a publicly accessible work. Avoid qualitative assessments (“superior mass constraints”) of unpublished work.

P2-M6  
Section: References, page 6  
Problem: The entry “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.” lacks volume, page, arXiv ID, or any present record.[3][4] Similarly, “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” is not found on arXiv or in ADS. Referring to “arXiv e-prints” while the work is explicitly “in preparation” is contradictory, and “future-dated” citations are not acceptable for PRD.  
Required fix: Remove or replace these references with actual, currently available works. If the author wishes to refer to ongoing work, it should be done in text (e.g., “work in preparation”) without using it as a formal reference or as the basis for concrete numeric claims.

P2-M7  
Section: Global (novelty claims, abstract and Sec. 6), pages 1 and 5  
Problem: The paper makes several strong statements about naturalness (“no fine-tuning”) and predictive sharpness (“sharp falsifiability”) without quantifying what ranges of parameters are considered natural or how fine-tuning is assessed. For instance, the prior θi ∈ [0.01, π] implies that achieving β ≈ 0.27° may require θi in a relatively narrow subrange; this is not explored. Fujita et al. also discuss similar naturalness issues.[5]  
Required fix: Provide a quantitative analysis of the fraction of prior volume in (θi, fa, m) space that yields β within, say, 1σ of the observed signal, or soften the claims of naturalness (e.g., “does not require extreme parameter choices”) and explicitly connect to Fujita et al.’s discussion.

P2-M8  
Section: All sections where σ-significances appear (Abstract, Sec. 1, Sec. 3.2, Sec. 4, Sec. 7)  
Problem: Different σ-values derived from different procedures (e.g., Planck-only, ACT-only, combined summary-likelihood, MCMC posterior) are presented side by side without explicit repeated reminders that these are not directly comparable due to differing likelihoods, priors, and treatments of systematics. The user instructions require that such juxtapositions be explicitly qualified.  
Required fix: Every time two or more significance levels from different analyses are juxtaposed (e.g., “Planck HFI 2.5σ, ACT DR6 2.9σ, combined >3.5σ”), add a short explicit qualifier such as “These significances are not directly comparable because they are derived from different datasets and likelihoods; we use a simple Gaussian combination for illustration only.”

P2-N1  
Section: Abstract, page 1  
Problem: Load-bearing scalar consistency. Abstract claims: “β = 0.242 ± 0.061° (3.9σ from zero).” From Eq. (4), 0.242/0.061 ≈ 3.97, which rounds to 4.0σ rather than 3.9σ. The discrepancy is negligible, but PRD usually expects consistent rounding between the abstract and main text.  
Required fix: Use consistent rounding: either 4.0σ in both places, or adjust σ to 0.062° if 3.9σ is preferred.

P2-N2  
Section: 4 LiteBIRD Forecast, Eq. (10), page 3  
Problem: Units and notation: the equation “Significance = 0.27 / 0.03 = 9σ” omits explicit degrees. Although dimensionally obvious, it is cleaner to write “0.27°/0.03°” to make the units match on both numerator and denominator.  
Required fix: Add “°” or explicitly state “in degrees” in the equation or its caption.

P2-N3  
Section: 2.1 Field Dynamics, Eq. (1), page 1  
Problem: In Eq. (1), “J0(0)” is in the denominator. Since J0(0) = 1, this factor is unnecessary and might confuse readers by suggesting a nontrivial normalization.  
Required fix: Simplify Eq. (1) to 1 − J0(m/H0) and state J0(0)=1 in text if needed.

P2-N4  
Section: 3.3 MCMC Parameter Estimation, prior ranges, page 2  
Problem: Notation for prior Caγ is used here, while Eq. (2) and surrounding text use C0 and gaγ. This is likely meant to be the same coupling constant, but the mismatch may confuse.  
Required fix: Standardize notation across the paper (e.g., use C0 and gaγ everywhere, or define Caγ explicitly and use only that).

P2-N5  
Section: Figures 1 and 2 captions, pages 3–4  
Problem: The paper only shows descriptive captions but does not specify axes units or parameter ranges for the triangle plots. While not strictly necessary, it would improve clarity to mention which parameters appear (e.g., θi, log10(m/eV), Caγ) so the figure is self-contained.  
Required fix: Expand captions to note which parameters are plotted and, if possible, units/log-scaling for axes.

P2-N6  
Section: References, page 6  
Problem: Reference formatting is inconsistent: one entry uses “arXiv preprint” while another uses “arXiv e-prints” plus “in preparation.” LiteBIRD is labeled as “Prog. Theor. Exp. Phys., 2023:042F01, 2023,” which is fine, but other journal names are sometimes abbreviated, sometimes written out.  
Required fix: Harmonize reference style to PRD standards (journal abbreviations, inclusion of volume/page, and arXiv IDs where appropriate).

P2-Length  
Global  
Problem: The paper is relatively concise (6 pages) for the claimed contribution, which is primarily a simple ALP birefringence estimate plus a light-weight summary-likelihood combination and a LiteBIRD forecast. The length is not excessive; if anything, additional methodological detail (especially on data handling and MCMC) would be warranted for PRD.  
Required fix: No need to shorten; instead, add missing methodological/citation detail as required above.

## Summary recommendation

MAJOR REVISIONS

Several key numerical inputs (ACT DR6 constraint, “Eskilt et al. joint” value, future “in preparation” works) are not traceable to any publicly available paper, yet they underpin the combined constraint, Bayes factor, and some of the main claims. There are also overstated novelty and naturalness claims, ambiguous parameter notation, and underdeveloped methodology for MCMC and Bayes-factor computation. These issues are incompatible with PRD’s standards of verifiability and rigor. The core idea—ALP-induced birefringence with Planck-scale decay constant and H0-scale mass—is interesting and connected to current literature, but the paper must replace unverifiable citations with real ones, recalculate all results using only published data, and significantly strengthen the methodological and citation foundations before being suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E14  
Section: 2.2 Birefringence Prediction, Eq. (2), page 1  
Problem (arithmetic + internal consistency): Eq. (2) writes β = gaγ Δϕ/2 = C0Δϕ/(2fa), but the subsequent text states “the cosmological field evolution gives Δϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27°.” To get 5×10−3 rad from Δϕ/fa ∼ 10−2 one must *drop the factor 1/2* in Eq. (2). If Eq. (2) is correct, then β ≈ (C0θi/2)×10−2 = 5×10−3 C0θi rad only if Δϕ/fa ≈ 10−2; but the text never shows this intermediate step and is numerically inconsistent with the “≈ fa θi × O(1)” expression in Eq. (1), which would instead give Δϕ/fa = O(1), not 10−2.  
Required fix: Make the numerical chain explicit and self-consistent: either (a) correct Eq. (1) to show a small dimensionless displacement Δϕ/fa ≈ 10−2 with appropriate derivation, or (b) correct the “10−2” estimate and the 0.27° number so they follow from Eq. (1) and (2) with all factors of 2 included. As written, the prediction β ≈ 0.27° is not traceable to the preceding equations.

P2-E15  
Section: 3.2 Summary-Likelihood Inference, Eq. (4), page 2  
Problem (arithmetic): The combined “3.9σ from zero” significance is computed from βcombined = 0.242 ± 0.061°. The ratio 0.242/0.061 ≈ 3.97, so 3.9σ is fine, but this rests on the unverified ACT DR6 input already flagged (P2-E3) and is then rhetorically elevated to “3.6σ isotropic birefringence signal” in the abstract using a *different* βobs = 0.342 ± 0.094° value from a different analysis. These two σ-values come from different procedures and datasets yet are discussed as if interchangeable.  
Required fix: (i) State explicitly which σ corresponds to which dataset and likelihood (combined summary vs. full EB), and (ii) avoid using “3.6σ signal” in the abstract unless you recompute that number transparently from documented inputs. Clarify that 3.9σ (βcombined) and 3.6σ (βobs) are *not* the same statistic.

P2-E16  
Section: 3.3 MCMC Parameter Estimation, pages 2–3; Table 1; Figure 2  
Problem (σ comparability + hedged language): The text claims “The ALP model reproduces the observed birefringence with no tension” comparing βALP = 0.336 ± 0.107°, βfree = 0.344 ± 0.096°, and βobs = 0.342 ± 0.094°. These are all within ~0.01° of each other, but the statement “no tension” is unquantified, and βALP and βfree are internal posterior summaries based on the *same* βobs summary input (Sec. 3.1), not independent measurements. The phrase “no tension” implicitly treats these as separate constraints.  
Required fix: Explicitly state that βALP and βfree are posterior inferences conditioned on βobs and therefore are not independent measurements; replace “no tension” with a quantitative comparison (e.g., difference normalized by the posterior σ) or with language acknowledging that the agreement is tautological given the setup.

P2-E17  
Section: 3.4 Bayes Factor, Eq. (9), page 3  
Problem (σ comparability, null-procedure comparability): The quoted ln B = 5.17 is explicitly prior-dependent, and alternative priors give ln B = 4.48 and 5.86. Eq. (9) and the text then label this “indicative evidence for nonzero rotation” without quantifying how this relates to the underlying frequentist “3.9σ” detection or warning that ln B values from this Gaussian-summary SDDR are not directly comparable to Bayes factors from full Planck or ACT analyses.  
Required fix: Add a sentence noting that these Bayes factors are computed from a 1D Gaussian summary-likelihood and should not be directly compared to evidence values derived from full multi-parameter CMB likelihoods; explicitly caution that the frequentist σ and ln B reported here come from *different null procedures* and are not interchangeable.

P2-E18  
Section: 4 LiteBIRD Forecast, Eq. (10), page 3  
Problem (arithmetic + over-sharpness): Eq. (10) uses Significance = 0.27/0.03 = 9σ. Mathematically this is fine, but:  
- β = 0.27° is itself a heuristic “order-unity” prediction, not a measured value.  
- σ(β) ≈ 0.03° is forecast-dependent and acknowledged as depending on self-calibration and systematics.  
The equation and the conclusion “LiteBIRD will detect it at overwhelming significance” present 9σ as a firm number rather than an approximate best-case scenario.  
Required fix: Replace Eq. (10) by a statement like “If β ≈ 0.27° and LiteBIRD achieves σ(β) ≈ 0.03°, this would correspond to a detection at ≈ 9σ significance,” and carry this conditional phrasing into the conclusion. This avoids overstating the precision of a forecasted σ relative to a model estimate.

P2-E19  
Section: Figure 1 caption vs. body; Sec. 3.3, Eq. (8), page 3  
Problem (figure–text consistency): Figure 1’s caption states “Caγ × θi is centered at 3.4 ± 1.1, consistent with order-unity natural values.” Eq. (8) in the text gives the same numbers. The description “order-unity” is qualitatively fine, but there is no explicit check in the body that this posterior is actually well constrained by the data rather than prior dominated, especially given the modest sample sizes (720–6840) and wide flat priors on Caγ and θi.  
Required fix: Add a brief quantitative check (e.g., comparison of posterior vs. prior width or an explicit statement that Caγ × θi is constrained beyond the prior) to support the implicit claim that Figure 1 reflects genuine data-driven constraints rather than mostly prior volume.

P2-E20  
Section: Figure 2 caption vs. body; Sec. 3.3, page 3  
Problem (figure–text consistency and σ comparability): Figure 2 caption says “All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094°.” The body text similarly emphasizes agreement. However, the three posteriors correspond to: an ALP model with C fixed, an ALP model with C free, and a phenomenological β model, all conditioned on essentially the same βobs constraint. Presenting three nearly identical β posteriors as if they are independent consistency checks is misleading.  
Required fix: Explicitly note in the caption or in the main text that the similarity of the three β posteriors is expected because they are all effectively constrained by the same βobs input, and that Figure 2 is a sanity check of internal modeling, not an independent cross-validation.

P2-E21  
Section: 6 Discussion, item (2) “Consistency with data”, page 5  
Problem (hedged language masking a numerical gap): The text claims “The prediction matches the combined Planck + ACT measurement at 1σ.” The prediction is β ≈ 0.27°, while βcombined = 0.242 ± 0.061°. The difference is |0.27−0.242| = 0.028°, which is 0.028/0.061 ≈ 0.46σ, so this is in fact well within 1σ and the statement is numerically correct. However, the underlying prediction itself is only justified by the heuristic Δϕ/fa ∼ 10−2 step flagged in P2-E14 and by order-unity assumptions on C0θi, not by a full parameter-space analysis. The phrase “matches… at 1σ” gives a stronger impression of a tuned match than warranted.  
Required fix: Qualify this as “for our fiducial choice C0θi ≈ 1 and Δϕ/fa ≈ 10−2 the predicted β ≈ 0.27° lies within ≈ 0.5σ of the combined constraint 0.242 ± 0.061°”; this makes clear the conditional nature of the “match.”

P2-E22  
Section: Abstract vs. body, multiple sentences  
Problem (abstract faithfulness):  
- The abstract’s “3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis)” is not transparently derived anywhere in the body; Sec. 3.1 just asserts βobs and refers to “Eskilt et al. joint analysis” without a method or citation.  
- The abstract claims “We perform a Gaussian summary-likelihood inference… finding β = 0.242 ± 0.061° (3.9σ from zero) with an effective photon coupling fphoton × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning).” Eq. (5) presents this coupling, but there is no derivation of how fphoton × C0 is obtained from βcombined, nor any propagation of uncertainty spelled out.  
Required fix: (i) Add a subsection or appendix that explicitly derives fphoton × C0 from βcombined and the model assumptions, and (ii) either provide a full reference and derivation for βobs = 0.342 ± 0.094° or rephrase the abstract to rely only on βcombined and Minami & Komatsu / Eskilt & Komatsu published values.

P2-E23  
Section: 6 Discussion; novelty & naturalness claims, page 5  
Problem (novelty + unquantified “no tuning”): The text states “No tuning is required” and “all inputs are at their natural scales,” without any quantitative analysis of what fraction of the prior ranges (θi ∈ [0.01, π], log10 m/eV ∈ [−35,−30], Caγ ∈ [1,30]) actually yields β within the observed range. This overstates naturalness compared to Fujita et al. (2021), who discuss parameter-space volume more explicitly.  
Required fix: Provide a simple scan or posterior volume estimate showing the fraction of prior space that leads to β within, e.g., ±1σ of the observed signal, or soften phrasing to “does not require extreme parameter values” and explicitly acknowledge that “no tuning” is not quantified here.

P2-E24  
Section: Internal cross-references, global  
Problem (refs not matching content):  
- “see Sec. 3.4” in the abstract regarding prior dependence is correct, but Sec. 3.4 does not show any detailed derivation—only final numbers—so “see Sec. 3.4” overpromises the level of methodological detail.  
- In Sec. 5 the reference “[Golden, 2026a] for the full ECH framework and 14-barrier catalog” points to a non-public companion paper; the reader cannot verify these claims.  
Required fix: Either expand Sec. 3.4 to include enough of the Savage–Dickey calculation to justify “see Sec. 3.4” as a methodological reference, and/or rephrase to “see Sec. 3.4 for numerical examples of the prior dependence.” For the ECH discussion, avoid implying that the 14-barrier catalog is part of the present paper’s evidentiary basis; describe it as “work in preparation” without using it for quantitative support.

P2-E25  
Section: Units and dimensional consistency, Eq. (1), page 1  
Problem (dimensional clarity): Eq. (1) writes Δϕ ≈ faθi(1−J0(m/H0)/J0(0)). This is dimensionally consistent if ϕ has units of fa and θi is dimensionless, but the text does not state this explicitly and later writes Δϕ/fa ∼ 10−2 without reconciling the earlier “× O(1)” statement. This creates avoidable confusion about whether Δϕ/fa is expected to be O(1) or 10−2 for m ∼ H0.  
Required fix: State explicitly that θi ≡ ϕi/fa is dimensionless, that Δϕ/fa is the relevant dimensionless displacement, and reconcile Eq. (1) with the later numerical estimate by either correcting the “O(1)” label or explaining why cosmological evolution reduces the naive Bessel-based estimate to ≈10−2.

P2-E26  
Section: All sections with σ-significances (Abstract, Sec. 1, Sec. 3.2, Sec. 4, Sec. 6–7)  
Problem (null-procedure comparability): Multiple σ values are quoted—2.5σ (Minami & Komatsu), 2.7σ, 2.9σ, 3.6σ, 3.9σ, and 9σ—without clarifying that they arise from different likelihoods, datasets, and null procedures (power-spectrum likelihoods vs. summary Gaussians, different foreground treatments). These are repeatedly juxtaposed (e.g., “Planck HFI… 2.5σ… ACT DR6… comparable significance. Combined, the evidence exceeds 3.5σ”) as if they share a common null.  
Required fix: Add an explicit statement early in Sec. 1 or Sec. 3 explaining that σ-values from different analyses are not strictly comparable and that “combined evidence exceeds 3.5σ” is a qualitative characterization; clarify, for each quoted σ, the dataset and likelihood used and avoid implying a single unified test statistic unless you actually construct one from published likelihoods.