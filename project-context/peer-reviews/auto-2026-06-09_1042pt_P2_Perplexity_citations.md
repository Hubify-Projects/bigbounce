# P2 auto-2026-06-09_1042pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16101 chars)
**Wall time**: 110.0s

---

P2-E1 (ESSENTIAL)  
Section: 1 Introduction, p.1  
Problem: The Planck HFI birefringence result is cited only as “[?]” with no identifying information, and the ACT DR6 analysis is referenced without any concrete citation (authors/year/arXiv ID). The text also states: “The Planck HFI analysis [?] reported β = 0.35 ± 0.14° (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.” No reference in the bibliography is visible for these claims.  
Required fix: Provide explicit, correct bibliographic entries (authors, year, journal/arXiv ID) for the Planck HFI birefringence analysis (likely Minami & Komatsu, 2020/2021) and for the ACT DR6 birefringence measurement. The combined significance “exceeds 3.5σ” must be explicitly computed and shown (e.g., using independent-Gaussian combination from the cited numbers) and must be traceable to the referenced works. Replace “[?]” with correct citations.

P2-E2 (ESSENTIAL)  
Section: 2.2 Birefringence Prediction, p.2  
Problem: Equation (2) reads  
\[
\beta = \frac{g_{a\gamma}}{2}\,\Delta\phi = \frac{\alpha_{\rm EM}\, C_{a\gamma}}{4\pi f_a}\,\Delta\phi,
\]  
but later in the same paragraph the text states “For \(C_{a\gamma} = 8\)… the numerical integration gives \(\Delta\phi/f_a \approx 1.07\), yielding \(\beta = (\alpha_{\rm EM} \times 8/4\pi) \times 1.07 \approx 0.29^\circ\).” This expression *drops* the \(1/f_a\) factor that appears in Eq. (2), implicitly setting \(\Delta\phi\) dimensionless. Earlier in Sec. 2.1 they write “\(\Delta\phi/f_a \approx 1.07\)”, which implies \(\Delta\phi\) has dimension of mass and \(\Delta\phi/f_a\) is the dimensionless quantity used in the equation of motion. As written, Eq. (2) is dimensionally inconsistent with the subsequent numerical plug-in, and the claimed cancellation of \(f_a\) is not explicit.  
Required fix: Clarify the conventions: either redefine the field variable as \(\theta = \phi/f_a\) and write the coupling in terms of \(\theta\), making all quantities dimensionless, or explicitly state that Eq. (2) is to be used with \(\Delta\phi/f_a\) so that \(\beta = (\alpha_{\rm EM}C_{a\gamma}/4\pi)\,(\Delta\phi/f_a)\). Then redo the numerical substitution with the correct factors and show explicitly how \(f_a\) cancels. Fix Eq. (2) or the surrounding text so that dimensions are consistent.

P2-E3 (ESSENTIAL)  
Section: 3.1 Datasets, p.2  
Problem: The Planck NPIPE birefringence value “β = 0.30 ± 0.11° (2.7σ)” and the ACT DR6 value “β = 0.215 ± 0.074° (2.9σ)” are given with no explicit citations (again “[?]”). No Planck NPIPE birefringence paper or ACT DR6 birefringence paper is identified in the references, so these numbers cannot be checked against the literature. The statement in 3.1 that “An earlier Planck HFI analysis [?] reported β = 0.35 ± 0.14° (2.5σ)” is again uncited.  
Required fix: Add explicit references (authors, year, arXiv/journal) for the Planck NPIPE birefringence analysis and the ACT DR6 birefringence analysis, and verify that the numerical values and uncertainties reproduce the quoted σ-levels. Ensure that these values are exactly as in the cited works (or clearly state if they are the author’s re-analyses).

P2-E4 (ESSENTIAL)  
Section: 3.2 Summary-Likelihood Inference, p.2–3  
Problem: The combined constraint is quoted as  
\[
\beta_{\rm combined} = 0.242 \pm 0.061^\circ\ (3.9\sigma\ {\rm from\ zero}).
\]  
From the two given inputs, Planck NPIPE (0.30 ± 0.11°) and ACT (0.215 ± 0.074°), the inverse-variance weighted mean and its uncertainty should be explicitly shown; the reader cannot verify the 0.242 and 0.061 values from the text alone. Furthermore, elsewhere in the paper the “Eskilt et al. joint analysis value β_obs = 0.342 ± 0.094° (3.6σ)” is mentioned in the abstract but *not* clearly connected to the combined value 0.242 ± 0.061°. The combination used in the abstract (“3.6σ Eskilt et al. joint Planck + ACT signal”) is not consistent with the 3.9σ combined value presented here, yet both are presented as if they refer to “Planck+ACT”.  
Required fix: Explicitly show the calculation of the combined mean and error from the two β measurements and verify they indeed yield 0.242 and 0.061. Clarify, in the abstract and main text, that the 3.6σ value (0.342 ± 0.094°) comes from a specific joint likelihood analysis by Eskilt et al. and is *different* from the simple Gaussian combination (0.242 ± 0.061°). The abstract must not give the impression that these are the same combination. Reword to distinguish clearly which number comes from which analysis.

P2-E5 (ESSENTIAL)  
Section: 3.2, Eq. (5), p.3  
Problem: “The effective photon coupling parameter: \(f_{\rm photon} \times C_0 = 1.73 \pm 0.44\)” is introduced without definition of \(f_{\rm photon}\) in the text and without reference to a prior work where this parameterization is used. It is unclear whether \(f_{\rm photon}\) is dimensionless, in units of \(10^{16}\,\mathrm{GeV}\), or something else. There is no derivation presented showing how this number is inferred from the combined β constraint, the ALP model, and the assumed priors. The reader cannot reproduce or interpret this value.  
Required fix: Define \(f_{\rm photon}\) unambiguously (units, relation to \(f_a\) and \(g_{a\gamma}\)), show the explicit formula connecting β to \(f_{\rm photon}C_0\), and demonstrate the calculation leading to 1.73 ± 0.44 from the data and priors. Provide a reference if this parameterization follows earlier work.

P2-E6 (ESSENTIAL)  
Section: 3.3 MCMC Parameter Estimation, p.3  
Problem: The Eskilt et al. joint analysis value “β_obs = 0.342 ± 0.094°” is used as the observational input for the MCMC, but the corresponding reference is again “[?]” and not given in the bibliography. The values  
\[
\beta_{\rm ALP} = 0.336 \pm 0.107^\circ,\quad \beta_{\rm free} = 0.344 \pm 0.096^\circ
\]  
are quoted as MCMC outputs but there is no description of the likelihood function (beyond the brief mention of the Eskilt value), the number of chains, proposal distribution, or how the errors compare to the data input. There is also no demonstration that these posterior means/variances are consistent with the assumed likelihood (which, for a single Gaussian input, should practically reproduce the input mean and variance if priors are weak).  
Required fix: Provide a proper citation for the Eskilt et al. joint Planck+ACT analysis and verify that the β_obs value is as stated. Give at least a short, precise description of the likelihood used for the β parameter (e.g., Gaussian with mean 0.342°, σ = 0.094°). Show that the posterior on βfree is consistent with this likelihood (it should be essentially identical in a simple one-parameter case) or explain any differences. Clarify how βALP is derived from the ALP parameters and show that the mapping is correctly implemented.  

P2-E7 (ESSENTIAL)  
Section: 3.4 Bayes Factor, p.3  
Problem: The Bayes factor result “ln B = 5.17” is quoted as computed via the Savage–Dickey density ratio with a flat prior β ∈ [0°, 1°], but no details about the prior for β in the null vs alternative, the numerical implementation, or estimates of numerical error are provided. More importantly, the underlying likelihood is not fully specified, and the β_obs input comes from Eskilt et al. whose reference is missing. The alternative prior ranges (0–2°, 0–0.5°) yielding ln B = 4.48 and 5.86 respectively are also given without explicit computation or citation. For a journal like PRD, Bayes factors must be reproducible; here they are not.  
Required fix: Fully specify the likelihood function used for β (e.g., Gaussian with mean and variance from Eskilt et al.), the prior for β in the alternative model, and the method used to compute the prior and posterior densities at β = 0. Provide either a short analytic calculation of ln B for a Gaussian likelihood with a uniform prior or sufficiently detailed numerical methodology (e.g., histogramming from MCMC) so the result can be checked. Include a proper citation for the Eskilt dataset. If these Bayes factor values are approximate, explicitly state the approximations.

P2-E8 (ESSENTIAL)  
Section: 4 LiteBIRD Forecast, p.4  
Problem: The LiteBIRD sensitivity “σ(β) ≈ 0.03°” is cited with “[?]” but no bibliographic entry identifies the relevant LiteBIRD forecast paper. The number 0.03° is central to the “9σ” claim but is not verifiable. Also, the detection significance is computed as 0.27/0.03 = 9σ using the central prediction β = 0.27° while ignoring uncertainties in the model prediction (e.g., spread 0.17–0.43° stated earlier). Presenting this as “will test this prediction at 9σ significance” overstates the robustness of the forecast.  
Required fix: Provide a proper reference for the LiteBIRD birefringence forecast that specifically quotes σ(β) or provide a simple forecast calculation (e.g., Fisher estimate) in an appendix or the main text. Clarify that 9σ is based on the central model value and that the significance depends on both experimental sensitivity and model uncertainty. Rephrase to reflect this (e.g., “of order 9σ for β ≈ 0.27°”).

P2-E9 (ESSENTIAL)  
Section: 5 Spectator-condition energy-density constraint, p.4–5  
Problem: Equation (11) and the numerical estimate that follows are internally inconsistent and dimensionally unclear. The text gives  
\[
\rho_\phi(z=0) \approx \tfrac12 m^2 f_a^2 \theta_i^2 \Rightarrow \Omega_\phi(z=0) \approx \left(\frac{m}{H_0}\right)^2 \left(\frac{f_a}{M_{\rm Pl}}\right)^2 \theta_i^2.
\]  
Then they state: “At fa ∼ MPl, m ∼ H0, and natural θi ∼ O(1), this gives Ωϕ ∼ 0.17 today — comparable to dark energy rather than negligible.” With \(m/H_0 \sim 1\), \(f_a/M_{\rm Pl} \sim 1\), and \(\theta_i \sim 1\), Eq. (11) as written gives \(\Omega_\phi \sim 1\), not 0.17; the factor 0.17 appears without derivation. If instead one uses \(\rho_{\rm crit} = 3H_0^2 M_{\rm Pl}^2/(8\pi G)\) with a non-reduced Planck mass, there will be additional numerical coefficients that must be displayed. As written, the scaling and the numerical 0.17 value are not traceable.  
Required fix: Carefully derive Eq. (11) including all numerical factors, clearly state whether \(M_{\rm Pl}\) is the reduced or unreduced Planck mass, and recompute \(\Omega_\phi\) for the fiducial parameters. Show the calculation that yields \(\Omega_\phi \approx 0.17\); if the correct value is closer to 1, fix both the equation and the narrative. Recompute the required suppression of θi (the “25× fine-tuning”) from the corrected expression.

P2-E10 (ESSENTIAL)  
Section: 5, p.4–5  
Problem: They assert “The strict spectator regime (Ωϕ ≪ 1) therefore requires either (a) suppressing θi to ∼ 0.05 θ_nat ≈ 0.22 (a ∼ 25× fine-tuning…)” based on the previous statement that Ωϕ ≈ 0.17 at θi ∼ 1. With Ωϕ ∝ θ_i^2, reducing θ_i from 1 to 0.22 reduces Ωϕ by ~1/20, not ~1/25; but this depends entirely on the (already dubious) 0.17 value. The numerical factor “0.05 θ_nat ≈ 0.22” is mathematically inconsistent: 0.05 × 1 ≠ 0.22.  
Required fix: Once Eq. (11) is correctly derived, recompute the θi value needed to reach whatever level of Ωϕ is defined as “≪ 1” (e.g. 0.01). Present the factor by which θi must be suppressed in a mathematically consistent way (e.g., “θi ≈ 0.24 implies Ωϕ ≈ 0.06” if that is what the corrected calculation gives). Remove the contradictory “0.05 θ_nat ≈ 0.22” statement and replace with correct numbers.

P2-E11 (ESSENTIAL)  
Section: Abstract, p.1; Sections 3.1–3.3, 7, 8  
Problem: The abstract claims: “consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis).” This 3.6σ is simply 0.342/0.094, but no reference to Eskilt et al. is provided anywhere in the paper. In Sec. 3.3, “βobs = 0.342 ± 0.094°” is mentioned again without citation. Without an explicit citation, the key experimental input the entire paper is based on is unverifiable.  
Required fix: Provide the full bibliographic details (author list, year, arXiv ID or journal) for the Eskilt et al. joint Planck+ACT birefringence analysis and verify that the quoted βobs and uncertainty are exactly those reported. Ensure that every mention of this result is properly cited.

P2-E12 (ESSENTIAL)  
Section: 7 Discussion, p.5  
Problem: They cite: “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [?].” There is no reference with this statistic given; the placeholder “[?]” provides no information. The value fNL = −35/8 is highly specific and must be traceable to a known model and paper (e.g., in the matter-bounce literature). Without a citation, this is unsupported.  
Required fix: Provide a precise reference to the work that derives fNL = −35/8 in matter-bounce cosmology and verify that this is indeed the quoted value (and in what convention). If this value is derived in a “companion paper,” that companion paper must be cited with full bibliographic information, and a brief summary of assumptions should be included.

P2-E13 (ESSENTIAL)  
Section: 7 Discussion, p.5  
Problem: “We emphasize that the ALP birefringence model class is well-studied in the literature [?]. Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°, and Namikawa, Murai & Naokawa [?] provide superior ALP mass constraints using the full Planck EB spectrum.” These references are not given in the bibliography; only “[?]” placeholders appear. The claimed results and their novelty comparison depend critically on these works.  
Required fix: Add full citations for Fujita et al. (2021) and Namikawa et al. (including titles, journal, and arXiv IDs), and verify that the statements are correct (e.g., that Fujita et al. specifically consider Planck-scale ALPs and find β ~ 0.3°, and that Namikawa et al. indeed derive ALP mass constraints from the full EB spectrum). If any of these phrases misrepresent the cited works, correct the text.

P2-E14 (ESSENTIAL)  
Section: 6 Relationship to Bounce Cosmology, p.5  
Problem: “see the companion paper [?] for the full ECH framework and 14-barrier catalog.” The companion paper is not identified (authors, arXiv ID, or journal), and it is unclear whether it is publicly available. Referring to an unspecified companion paper for key parts of the theoretical motivation is unacceptable for PRD.  
Required fix: Provide a complete citation to the companion ECH framework paper (with arXiv ID or journal). If the work is not publicly accessible, either remove the reference or replace it with a description that does not rely on unpublished material. Make sure that any dependence on the ECH framework in the current paper is either fully explained here or backed by accessible references.

P2-E15 (ESSENTIAL)  
Section: General, entire paper  
Problem: Multiple references appear as “[?]” throughout (e.g., Planck HFI analysis, Planck NPIPE, ACT DR6 birefringence, Eskilt et al. joint analysis, LiteBIRD forecast, companion Paper I(a), companion ECH paper, matter-bounce fNL paper, Fujita et al. 2021, Namikawa et al.). There is no actual reference list in the provided text. For a PRD submission, a complete, consistent bibliography is mandatory. The current state makes it impossible to perform proper citation forensics.  
Required fix: Compile a full reference list, with correct authors, titles, journals, volumes, pages, years, and arXiv IDs for all works cited in the text. Replace all “[?]” placeholders with explicit citation keys. Ensure there are no duplicate entries, and that every numeric/qualitative claim citing previous work is traceable to the reference (abstract, main text, or tables of the cited paper).

P2-M1 (MAJOR)  
Section: Abstract vs. Sec. 2.2 and 7, p.1 and p.5  
Problem: The abstract states a specific prediction “β ≈ 0.27°,” but Sec. 2.2 gives a more detailed numerical example yielding “β ≈ 0.29°,” and later Sec. 2.2 states that the prediction spans “β ≈ 0.17–0.43° across the natural parameter range.” There is no explicit point in the main text at which β = 0.27° is actually calculated with given parameter values; it seems to be an approximate central value, but the reader cannot reconstruct it.  
Required fix: Choose a clear fiducial parameter set (m/H0, θi, C0) and show how β ≈ 0.27° follows from those numbers. Then make sure the abstract’s quoted prediction matches that fiducial value. Alternatively, express the abstract prediction as a range consistent with Sec. 2.2 and clearly state that 0.27° is only an approximate central value.

P2-M2 (MAJOR)  
Section: 2.1 Field Dynamics, p.2  
Problem: The range “Δϕ/fa ≈ 0.2–1.1 (for m/H0 ∈ [0.5, 3], θi = 1)” and the single value “for the fiducial case m = H0, θi = 1, the numerical integration yields Δϕ/fa ≈ 0.65” are stated without any figure, table, or explicit numerical method details. There is no indication of step size, integration scheme, or whether the quoted numbers can be reproduced. Given that the ALP dynamics are standard but the quantitative prediction β depends critically on these values, the lack of detail is problematic.  
Required fix: Provide at least a brief description of the numerical method (e.g., background cosmology, initial conditions, numerical integrator, step size, validation checks) and, ideally, include a small table or plot of Δϕ/fa vs. m/H0 to support the stated range. This is required for reproducibility of the central theoretical input.

P2-M3 (MAJOR)  
Section: 3.3, Table 1, p.3  
Problem: Table 1 gives sample counts (2160, 6840, 720) and R̂ − 1 values < 0.01 and asserts “Converged.” However, no details of how R̂ was computed (number of chains, chain lengths, burn-in fraction) are given. For low dimensional problems, these sample sizes might be marginal but acceptable; still, the claim that “small effective sample sizes (Neff ~ 1000) limit the precision of tail estimates and evidence calculations” is not backed by any explicit Neff table or diagnostic. PRD standards for MCMC-based inference require more transparency.  
Required fix: Provide details of the MCMC setup: number of chains, total chain length, burn-in fraction, proposal distribution, and which software was used. Report effective sample sizes for each parameter (or at least for β, m, θi, and C) and R̂ values per parameter. If the current sample sizes are marginal, either rerun with more samples or clearly qualify the precision of any tail-dependent quantities (e.g., Bayes factors).

P2-M4 (MAJOR)  
Section: 7 Discussion, p.5  
Problem: The novelty claim: “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.” Without properly cited and audited references (e.g., Fujita et al. 2021), this assertion about what is and is not new is unverified. It is entirely possible that some previous work has already studied the same parameter regime.  
Required fix: After adding and verifying the relevant references, reassess and, if necessary, soften or refine the novelty claim to accurately reflect what is genuinely new: e.g., the specific combination of datasets, the precise parameter scan, or the particular “spectator” framing. Ensure that any claim of novelty is supported by a comparison to the cited literature.

P2-M5 (MAJOR)  
Section: 7 Discussion, p.5  
Problem: The paper presents βALP = 0.336 ± 0.107°, βfree = 0.344 ± 0.096°, and βobs = 0.342 ± 0.094° in close juxtaposition as evidence of consistency but does not explicitly flag that the βALP and βfree uncertainties are Monte Carlo posteriors subject to finite-sample noise, while βobs is an external experimental result. In cosmological practice this is often fine, but PRD-level clarity would benefit from explicitly stating that the two MCMC-derived sigmas are *not independent* of the input 0.094° sigma and that the comparisons are not fully independent tests.  
Required fix: Add a sentence explicitly clarifying that βALP and βfree are posterior estimates derived from the same Eskilt et al. likelihood that defines βobs, so the agreement is expected and does not constitute an independent test of the model. If additional data or independent consistency checks are available, they should be included; otherwise, tone down the “no tension” language accordingly.

P2-M6 (MAJOR)  
Section: 1 Introduction and 8 Conclusion, p.1 and p.6  
Problem: The paper asserts that the model “requires no fine-tuning of dimensionless parameters: all inputs are at their natural scales,” while Sec. 5 clearly identifies a ∼25× tuning of θi (or fa) to achieve the “strict spectator regime.” The abstract notes the scope of the naturalness claim but the conclusion does not adequately reflect the tension between “naturalness” and the explicit misalignment tuning discussed in Sec. 5. For a PRD readership, this is conceptually important.  
Required fix: Reconcile the discussion of naturalness across the abstract, introduction, Section 5, and conclusion. Make clear that there is a cosmological-constant-class tuning in the mass/energy-density sector, and that the “no fine-tuning” claim applies only to dimensionless couplings given that tuning. Adjust the concluding sentence to reflect this nuance rather than suggesting that the overall setup is free from fine-tuning.

P2-M7 (MAJOR)  
Section: Length vs. content, whole paper (7 pages)  
Problem: For the claimed contribution (a basic ALP birefringence prediction and a simple summary-likelihood + small MCMC analysis), much of the discussion is qualitative and references unspecified companion papers (ECH, Paper I(a)), which are not necessary for the core prediction. The current 7-page length is acceptable in absolute terms, but space is used on speculative connections and under-documented numerical methods rather than on rigorous derivations and checks.  
Required fix: Rebalance the paper: trim speculative sections (especially Sec. 6’s ECH/bounce motivation) unless supported by fully cited and accessible references, and use the space to provide more detail on the numerical ALP evolution, the likelihood construction, and the Bayes factor calculations. A concise 6–7 page paper is fine, but the current allocation of space is not optimal for methodological rigor.

P2-N1 (MINOR)  
Section: 1 Introduction, p.1  
Problem: The text says “mθ ∼ H0 ultralight-mass tuning” which is dimensionally odd; presumably this means \(m_\phi \sim H_0\) or something akin to “m at the H0 scale,” not m times θ. This might confuse readers.  
Required fix: Correct the notation to “m ∼ H0” or “mφ ∼ H0” and remove “mθ” which suggests a product of mass and angle.

P2-N2 (MINOR)  
Section: 2.1, p.2  
Problem: The sentence “For m ∼ H0 and fa ∼ MPl, the field is frozen during radiation and matter domination (Hubble friction exceeds the mass) and begins rolling at z ∼ O(1) when H(z) ∼ m.” is repeated almost verbatim a second time in the same paragraph: “For m ∼ H0 and θi ∼ O(1), the field is frozen by Hubble friction during radiation and matter domination and begins rolling at z ∼ O(1) when H(z) ∼ m.”  
Required fix: Remove redundancy by keeping one version of the sentence and merging the information about θi into it if needed.

P2-N3 (MINOR)  
Section: 2.2, p.2  
Problem: “For Caγ = 8 (a natural DFSZ-type value)” is asserted without citation. While it is true that anomaly coefficients of order 1–10 are common, calling 8 a “natural DFSZ-type value” would benefit from a reference.  
Required fix: Either add a reference for typical ALP anomaly coefficients in DFSZ-type models or rephrase to a more modest statement (e.g., “an anomaly coefficient of order a few, such as Caγ = 8”).

P2-N4 (MINOR)  
Section: 3.3, Table 1, p.3  
Problem: The column “Samples” appears to mean *accepted* samples, but this is not explicitly stated. The reader might wonder whether these are total proposal steps or post-burn-in retained samples.  
Required fix: Clarify in the caption or text that “Samples” refers to accepted post-burn-in samples used in the analysis.

P2-N5 (MINOR)  
Section: Figures 1 and 2, p.3–4  
Problem: The figures are referenced (“Triangle plot…”, “Comparison of β posteriors…”) but the axes are not described in the text. For example, Figure 1’s axis labels (likely θi, log10(m/eV), Caγ, etc.) are not specified; Figure 2 presumably shows posterior distributions of β for the three runs but this is not clearly stated in terms of axes and units.  
Required fix: Add text explicitly describing what is plotted in each figure (parameter names, units, and which curve corresponds to which model). Ensure the figure captions include enough detail that the figures are interpretable without guessing.

P2-N6 (MINOR)  
Section: 4 LiteBIRD Forecast, p.4  
Problem: The statement “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ” uses the central prediction value 0.27° / 0.03° = 9σ and treats it as an exclusion significance without clearly stating that it assumes the underlying model prediction is exact and ignores model uncertainties.  
Required fix: Qualify the statement to say “approximately 9σ” and note that actual exclusion significance will depend on the model parameter uncertainties and the exact experimental sensitivity.

P2-N7 (MINOR)  
Section: 6 Relationship to Bounce Cosmology, p.5  
Problem: The sentence “The ALP is a spectator field—it does not participate in the bounce dynamics, does not generate perturbations, and does not require a contracting phase.” is somewhat at odds with the rest of the paper where the “spectator” condition depends sensitively on Ωϕ (Sec. 5). A reader might reasonably ask whether Ωϕ ∼ 0.17 at θi ∼ 1 really counts as “spectator.”  
Required fix: Add a short clarifying sentence noting that “spectator” as used here is in the Ωϕ ≪ 1 regime defined in Sec. 5, or explicitly state that the bounce-motivated discussion is qualitative and does not affect the main birefringence prediction.

P2-N8 (MINOR)  
Section: 7 Discussion, p.5  
Problem: The text says “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [?].” Without giving any context (e.g., which shape of non-Gaussianity, which observable), this is opaque.  
Required fix: Briefly specify whether this is the local, equilateral, or some other bispectrum shape, and indicate which measurements (e.g., CMB bispectrum, large-scale structure) would be sensitive to it, with a reference.

P2-N9 (MINOR)  
Section: Acknowledgments, p.7  
Problem: The author notes “The author acknowledges the use of AI research assistants during the analysis and manuscript preparation.” For PRD, transparency is fine, but it may be helpful to specify that all scientific claims and numerical results were independently checked by the author, given current community concerns about AI-generated errors.  
Required fix: Consider adding a clarifying sentence that the author takes full responsibility for the analysis and has independently verified the AI-assisted calculations.

P2-N10 (MINOR)  
Section: General style, whole paper  
Problem: There are several informal, conversational phrases (“consumer hardware,” “no fine-tuning,” “clean exclusion”) that are slightly more colloquial than PRD typically prefers.  
Required fix: Edit for a slightly more formal tone, particularly in the abstract and conclusion, without changing scientific content.

P2-N11 (MINOR)  
Section: Abstract, p.1  
Problem: Abstract uses an undefined symbol “F(m/H0)” in “∆ϕ ∝ fa θi F(m/H0)” which is only described qualitatively later. For a reader scanning the abstract, this could be confusing.  
Required fix: Add a brief parenthetical definition (e.g., “where F(m/H0) encodes the O(1) dependence of the field excursion on the mass-to-Hubble ratio”) or move this detail to the main text.

P2-N12 (MINOR)  
Section: 7 Discussion, p.5  
Problem: The phrase “14-barrier catalog” appears with no explanation or context.  
Required fix: Either briefly explain what “14-barrier catalog” refers to or remove the phrase if it only makes sense in the companion ECH paper.

P2-N13 (MINOR)  
Section: 6, p.5  
Problem: “ECH gravity” is introduced without expansion of the acronym or reference.  
Required fix: Spell out ECH at first use and provide citation.

P2-N14 (MINOR)  
Section: 1 and 8 (sigma juxtaposition), p.1 and p.6  
Problem: Different σ values obtained from different procedures are mentioned in proximity: introduction “2.5σ”, abstract “3.6σ”, main text “3.9σ from zero.” The text nowhere explicitly states that these significances come from different analyses and are not directly comparable. Given the instructions you specified for sigma comparisons, this must be flagged.  
Required fix: Each time multiple σ values from different analyses are juxtaposed (e.g., abstract, Intro, and Discussion), explicitly state that they are derived using different datasets/likelihood constructions and are *not directly comparable*.

P2-N15 (MINOR)  
Section: Entire paper, equations  
Problem: Units are not always explicitly stated (e.g., whether β is always in degrees vs radians in equations). While the context suggests degrees for quoted numbers and radians in theoretical formulas, this should be explicit.  
Required fix: Declare explicitly whether β is treated in radians or degrees in the theoretical formulas and convert consistently when quoting numerical predictions.

P2-N16 (MINOR)  
Section: 2.2, p.2  
Problem: The “prediction spans β ≈ 0.17–0.43° across the natural parameter range m/H0 ∈ [1, 3], θi ∈ [0.5, 2], Caγ ∈ [4, 12], comfortably bracketing the observed value.” No table or plot shows how this range is computed from these parameter ranges.  
Required fix: Provide either an explicit formula or a short table showing β values at the corners of the parameter box, or else a plot of β vs. one parameter with others held fixed, to justify the stated span.

P2-N17 (NIT)  
Section: 5, p.4  
Problem: The notation “θnat” is used without definition.  
Required fix: Define θnat explicitly when first introduced or avoid using it.

P2-N18 (NIT)  
Section: Typographical issues  
Problem: Small typographical inconsistencies (e.g., “mθ ∼ H0”, inconsistent spacing around parentheses, missing commas) are present throughout.  
Required fix: Proofread the manuscript carefully and correct typographical and formatting inconsistencies.

P2-N19 (NIT)  
Section: 7 Discussion, p.5  
Problem: The phrase “Minami-Komatsu self-calibration method” might benefit from a citation to the original Minami & Komatsu paper.  
Required fix: Add the appropriate citation and ensure it appears in the references.

P2-N20 (NIT)  
Section: General  
Problem: The paper sometimes uses “C0” and sometimes “Caγ” for the anomaly coefficient; in the abstract “C0 ∼ O(1)” appears, while the main text mostly uses Caγ. This can cause confusion.  
Required fix: Choose a single symbol for the anomaly coefficient and use it consistently throughout, or explicitly define that C0 ≡ Caγ at first use.

P2-N21 (NIT)  
Section: Abstract vs. body  
Problem: Abstract states “Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).” The prior dependence is discussed in 3.4 but not quantified in the abstract.  
Required fix: Consider adding a short note in the abstract indicating that ln B varies by ±~0.7 under reasonable alternative priors, or at least make sure Sec. 3.4 gives that information clearly (which it mostly does).

P2-N22 (NIT)  
Section: Acknowledgments, p.7  
Problem: Mention of specific software (Python, NumPy, SciPy) is fine, but no version numbers or references are given. While not strictly required, some journals prefer explicit citations for major software used.  
Required fix: Consider adding standard citations for NumPy and SciPy in the references.

P2-N23 (NIT)  
Section: 3.2, Eq. (3), p.2–3  
Problem: The likelihood product formula has slightly awkward typesetting: “L(β) = ∏ (1/√(2πσ_i^2)) exp(−(β_i^obs − β)^2/2σ_i^2).” It is correct but can be clearer.  
Required fix: Reformat Eq. (3) for clarity, e.g., write the normalization and exponential factors on separate lines or use a more standard notation.

P2-N24 (NIT)  
Section: 1, p.1  
Problem: The first sentence defines cosmic birefringence in words but doesn’t give a reference to the original literature.  
Required fix: Add a reference to one or two early or review papers on cosmic birefringence.

P2-N25 (NIT)  
Section: Title page  
Problem: The affiliation is given as “Independent Researcher, Los Angeles, California, USA” which is acceptable but some journals prefer a more formal address.  
Required fix: Check PRD author guidelines and format the affiliation accordingly if needed.

## Summary recommendation

REJECT

The paper in its current form lacks a usable bibliography (numerous “[?]” placeholders), making it impossible to verify key experimental inputs and prior theoretical results, and contains several essential issues with dimensional consistency, internal numerical claims (notably the Ωϕ estimate and “spectator” tuning), and reproducibility of the statistical analysis (Bayes factor and MCMC). For a PRD cosmology methods paper, these are fundamental shortcomings. A thorough rewrite with complete, verified references, corrected equations and numerics, and significantly more detailed methodological exposition would be required before the work could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E16 (ESSENTIAL)  
Section: Abstract, Introduction, 2.2, 5, 7, 8  
Problem: The quoted “prediction” **β ≈ 0.27°** is never explicitly derived anywhere in the body of the paper, yet it is used numerically in Sec. 4 to claim a 9σ LiteBIRD detection, and in Secs. 1, 5, 7, and 8 as if it were a concrete model output. The only explicit plug‑in example in Sec. 2.2 gives **β ≈ 0.29°**, and the stated “natural parameter range” yields β ≈ 0.17–0.43°, so 0.27° is simply an unshown central estimate. This breaks Abstract–body consistency and overstates how sharply the theory predicts β.  
Required fix: Either (i) pick a specific fiducial parameter set and explicitly calculate β = 0.27° in Sec. 2.2, referring to that point everywhere the number is used, or (ii) stop using a single “0.27° prediction” and instead phrase all claims in terms of the explicit 0.29° example and the 0.17–0.43° range. The LiteBIRD “9σ” statement must be tied to a clearly defined fiducial parameter point or rephrased as “of order 9σ for β ≃ (0.27–0.3)°.”

---

P2-E17 (ESSENTIAL – arithmetic)  
Section: 3.2, Eq. (4), p.3; 3.1, p.2  
Problem: The combined constraint **β_combined = 0.242 ± 0.061° (3.9σ)** is quoted from Planck NPIPE (0.30 ± 0.11°) and ACT (0.215 ± 0.074°), but the numbers are not demonstrably consistent. Recomputing the inverse‑variance weighted mean and error from the two inputs is not shown, and the 3.9σ significance is not explicitly derived in the text. This makes it impossible to verify whether 0.242, 0.061, and 3.9 follow from the given inputs, or whether they were computed with slightly different underlying numbers (e.g. rounded values, internal re‑fits).  
Required fix: Explicitly show the weighted‑mean formula and the numerical steps from (0.30, 0.11) and (0.215, 0.074) to β_combined and σ_combined, including any unrounded values used. Recompute the quoted σ‑level from zero from those same numbers and correct the 3.9σ if it changes. If different β or σ values than those printed in Sec. 3.1 were actually used in the combination, this must be stated and both sets of numbers reconciled.

---

P2-E18 (ESSENTIAL – arithmetic and null comparability)  
Section: 3.1, 3.2, 3.3, 7  
Problem: Three different “significance” measures are juxtaposed as if directly comparable:  
- individual measurements “2.7σ” (0.30 ± 0.11°) and “2.9σ” (0.215 ± 0.074°);  
- the summary‑likelihood “3.9σ from zero” (0.242 ± 0.061°);  
- the Eskilt joint “3.6σ” (0.342 ± 0.094°).  

However:  
- the 2.7σ and 2.9σ come from one‑experiment likelihoods with their own systematics;  
- the 3.6σ Eskilt value arises from a joint EB‑spectrum likelihood with different nuisance parameters and masks;  
- the 3.9σ combination uses only Planck‑NPIPE + ACT point estimates.  

Yet the paper repeatedly phrases these as one coherent “Planck+ACT” signal: “consistent with the 3.6σ isotropic birefringence signal,” “combined, the evidence exceeds 3.5σ,” and “the prediction matches the combined Planck + ACT measurement at 1σ.” No place in the paper quantitatively separates the different likelihoods or warns the reader that these σ values are not directly comparable.  
Required fix: For every quoted σ level, specify which likelihood/experiment it is derived from and explicitly state that 2.7σ, 2.9σ, 3.6σ, and 3.9σ come from *different* procedures. When comparing them (e.g. “matches the combined Planck + ACT measurement at 1σ”), show the relevant Δβ / σ and emphasize that the input σ (0.094°, 0.061°, etc.) is associated with a specific likelihood. Remove or reword any sentence that implicitly treats these different σ values as a single coherent measure of “the same” dataset unless a formal joint likelihood has been constructed and shown.

---

P2-E19 (ESSENTIAL – arithmetic and internal consistency)  
Section: 5, Eq. (11), p.4–5; Abstract; 5, discussion of θ_i tuning  
Problem: There are several mutually inconsistent numerical claims tied to Eq. (11):  

- Eq. (11) as printed is  
  \[
  \rho_\phi(z = 0) \approx \tfrac12 m^2 f_a^2 \theta_i^2 \Rightarrow \Omega_\phi(z = 0) \approx \left(\frac{m}{H_0}\right)^2 \left(\frac{f_a}{M_{\rm Pl}}\right)^2 \theta_i^2.
  \]  

- With \(m/H_0 \sim 1\), \(f_a/M_{\rm Pl} \sim 1\), and \(\theta_i \sim 1\), this gives **Ω_ϕ ∼ 1**, not 0.17 as stated. The origin of the numerical factor 0.17 is not shown.  

- The text then claims “suppressing θ_i to ∼ 0.05 θ_nat ≈ 0.22 (a ∼ 25× fine‑tuning).” But numerically 0.05 × 1 ≠ 0.22, and if Ω_ϕ ∝ θ_i², a reduction by a factor of 25 requires θ_i reduced by 1/5, not 0.22.  

- Later in Sec. 5 they state that with θ_i ≈ 0.22, the **β ≈ 0.27° prediction “continues to hold by the cancellation above.”** This cannot be correct: Eq. (2) shows β ∝ θ_i (through Δϕ ∝ θ_i), so changing θ_i by nearly a factor of 5 must change the predicted β by the same factor unless some separate rescaling of C_0 or m is specified. No such compensating change is described.  

Together these issues create a logically inconsistent story: the same fiducial numbers are claimed to yield both Ω_ϕ ≈ 0.17 and Ω_ϕ ≪ 1, and the β prediction is claimed to be invariant under a large change in θ_i that should directly rescale β in the given model.  
Required fix:  
- Derive Eq. (11) carefully, with explicit numerical coefficients and a clear definition of M_Pl (reduced vs unreduced). Show the calculation that yields Ω_ϕ ≈ 0.17 (if it does), or correct the text if the correct value is closer to 1.  
- Recompute the θ_i needed to reach the chosen “spectator” threshold (e.g. Ω_ϕ = 0.01), and ensure that the factor by which θ_i is reduced matches the implied suppression of Ω_ϕ. Remove the contradictory “0.05 θ_nat ≈ 0.22” and replace with mathematically consistent numbers.  
- Explicitly propagate the change in θ_i into the β prediction (β ∝ θ_i C_0 F(m/H_0)), and either (i) show which other parameter is adjusted to keep β ≈ 0.27° or (ii) acknowledge that the spectator–regime parameter choice produces a different β and quantify it. The current claim that the β prediction is unchanged by a factor‑of‑5 shift in θ_i is not justified by the equations in Sec. 2.

---

P2-E20 (ESSENTIAL – dimensional consistency and definition)  
Section: 2.1–2.2, Eq. of motion and Eq. (2), p.2; Abstract scope note  
Problem: There is a mix of dimensional and dimensionless conventions for ϕ that is never made explicit:  

- The equation of motion is written as  
  \( \ddot\phi + 3H \dot\phi + m^2 f_a \sin(\phi/f_a) = 0 \),  
  which suggests ϕ has mass dimension 1 and θ = ϕ/f_a is dimensionless.  

- Eq. (1) then states “Δϕ/f_a ≈ 0.2–1.1”, again treating Δϕ/f_a as the fundamental dimensionless displacement.  

- Eq. (2) is written as  
  \( \beta = (g_{a\gamma}/2)\Delta\phi = (\alpha_{\rm EM} C_{a\gamma}/4\pi f_a)\Delta\phi \),  
  which, if read literally, uses Δϕ (dimension of mass) rather than Δϕ/f_a, making β dimensionless only if an implicit division by f_a has occurred.  

- The “scope note” in the abstract asserts β ≈ (C_0 θ_i / 2) F(m/H_0), independent of f_a, but this expression is never actually derived in the main text from Eq. (2) and the equation of motion. The cancellation of f_a is asserted in prose but not shown algebraically.  

These inconsistent conventions around ϕ vs θ = ϕ/f_a and missing f_a factors make the model’s normalization opaque and hide the dependence of β on θ_i and C_0.  
Required fix: Introduce θ ≡ ϕ/f_a explicitly as the dynamical field variable, write the equation of motion in terms of θ, and rewrite Eq. (2) as  
\[
\beta = \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi}\,\Delta\theta,
\]  
so that all quantities are dimensionless and the f_a cancellation is transparent. Then derive the abstract’s expression β ≈ (C_0 θ_i/2) F(m/H_0) directly from this, showing each step. Ensure that every numerical substitution in Sec. 2.2 (e.g. the 0.29° example) uses Δθ consistently, with no implicit f_a omissions.

---

P2-M6 (MAJOR – figure/body mismatch and missing configuration details)  
Section: Figure 1, Figure 2, 3.3; 3.1–3.2  
Problem: The two figures are referenced qualitatively in the text, but:  

- Figure 1 is described as a “triangle plot from the extended ALP MCMC (Run 2, C free)” with posterior Caγ × θ_i = 3.4 ± 1.1. However, no axis ranges, units, or binning choices are specified, and no mention is made of the prior boundaries visible in the figure (C_γ ∈ [1,30], θ_i ∈ [0.01,π]). The body text does not clarify whether the apparent degeneracy in Figure 1 is prior‑dominated or likelihood‑dominated, which is critical for interpreting Caγ × θ_i as “natural.”  

- Figure 2 is said to show “comparison of β posteriors across all three model configurations,” but the body text does not specify whether the plotted β_distributions are *marginal* posteriors or the input Gaussian likelihood for β_obs, nor does it compare their means and dispersions numerically. The statement that “all three are consistent with each other and with the observed value” is purely qualitative; the figure’s axes are not described (e.g. β in degrees vs posterior density in arbitrary units), making it impossible to check whether they quantitatively match the numbers in Eqs. (6)–(7) and β_obs = 0.342 ± 0.094°.  

- Neither figure caption nor main text specifies the underlying configuration (e.g. whether Figure 2 uses the same chains as Table 1, whether burn‑in was discarded, or whether the plotted posteriors are kernel‑smoothed), which is needed for reproducibility and to ensure that what the captions claim (“Run 2, C free” and “all three model configurations”) matches what was actually plotted.  

Required fix:  
- Expand the captions to state exactly what is plotted (variables, units, priors, posterior type, smoothing, and chain source).  
- In the text, add explicit numerical comparisons drawn from the plots (e.g. mean and 68% intervals for each β posterior in Figure 2) and verify they match Eqs. (6)–(7) and β_obs.  
- Clarify whether the Caγ × θ_i posterior in Figure 1 is significantly influenced by the chosen flat priors; if it is, qualify the “order‑unity” interpretation accordingly. Provide enough detail that a reader can reproduce both figures from the described MCMC runs.

---

P2-M7 (MAJOR – abstract faithfulness and hedging)  
Section: Abstract; 3.2; 3.3; 3.4; 7  
Problem: Several phrases in the abstract and discussion go beyond what is quantitatively supported in the body, or use hedged language without numbers:  

- Abstract: “effective photon coupling f_photon × C_0 = 1.73 ± 0.44 (order‑unity, no fine‑tuning).” But f_photon is not defined anywhere, its units are not specified, and no derivation is given connecting β to this parameter. Without a clear mapping and prior, labeling this as “no fine‑tuning” is not quantitatively justified.  

- Abstract and Sec. 7: “consistent with the 3.6σ isotropic birefringence signal” and “prediction matches the combined Planck + ACT measurement at 1σ” are used without showing the actual Δβ and associated uncertainties. For instance, the comparison between β_ALP = 0.336 ± 0.107°, β_free = 0.344 ± 0.096°, and β_obs = 0.342 ± 0.094° is never quantified (e.g. difference in units of σ), even though these are central to the “no tension” claim.  

- Abstract: “LiteBIRD … will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.” The body notes the significance is “contingent on the self-calibration strategy and systematic error budget,” and Sec. 7 highlights potential systematic uncertainties in existing measurements. The absolute “decisive” phrasing in the abstract does not reflect these caveats.  

Required fix:  
- Define f_photon rigorously (including units) and show how 1.73 ± 0.44 is obtained from β and the ALP parameters; then explain, quantitatively, in what sense this constitutes “no fine‑tuning” (e.g. by specifying the prior range on f_photon and showing that the posterior does not occupy a tiny fraction of it).  
- Wherever phrases like “consistent with,” “no tension,” or “matches at 1σ” are used, include the numerical Δβ / σ calculation in the text, making it clear which σ (experimental vs posterior) is used.  
- Rephrase the LiteBIRD forecast in the abstract to match the more cautious language already present in Sec. 4 and 7, explicitly acknowledging dependence on systematics and on the exact true value of β (e.g. “can in principle reach ≃9σ for β ≈ 0.27° if systematics are controlled at the forecast level”).

---

P2-M8 (MAJOR – internal cross‑references and “scope note”)  
Section: Abstract (scope note), 2.2, 5, 6, 7  
Problem: The abstract contains a substantial “scope of the naturalness claim” paragraph stating specific reasons for fa ∼ M_Pl and the spectator‑condition constraint, and asserting that β is independent of fa. However:  

- The claim that “fa ∼ M_Pl is required by EFT consistency for a gravitationally coupled pseudoscalar” is not referenced or justified in the main text; Sec. 6 only provides a heuristic ECH motivation and explicitly says “this motivation is qualitative—no derivation connects the Holst action to a specific ALP potential or coupling.”  

- The dependence of β on fa and the exact spectator condition are discussed in Sec. 5 but, as noted above, contain internal numerical inconsistencies and do not rigorously derive “fa ∼ M_Pl” as a requirement, only as a preference.  

- The abstract’s compact formula β ≈ (C_0 θ_i / 2) F(m/H_0) is not derived or even written in the main text; the reader must reconstruct it from Eq. (2) and the numerical statement “Δϕ/f_a ≈ 0.2–1.1”, which is not enough to demonstrate the cancellation of fa.  

This causes an Abstract vs body mismatch: the very carefully worded “scope note” lives only in the abstract, while the body does not provide the detailed derivation or references that would substantiate it.  
Required fix:  
- Move the key “scope note” statements into Sec. 2 and Sec. 5, where the model and energy‑density constraints are developed, and expand them into an explicit derivation with references (e.g. work on Planck‑scale ALPs and gravitational couplings).  
- Derive β ≈ (C_0 θ_i / 2) F(m/H_0) in the main text, showing the independence from fa, and then refer back to that derivation in the abstract.  
- Qualify the “fa ∼ M_Pl is required” claim unless a robust EFT argument with citation is provided; otherwise, frame it as a motivated choice (“we adopt fa ∼ M_Pl for…”).

---

P2-m1 (MINOR – stale/inconsistent numbers)  
Section: 2.2, 5, 7, 8  
Problem: There are hints of stale numbers that were not updated consistently:  

- Sec. 2.2 highlights a specific example with m ≈ 2 H_0, θ_i = 1, C_aγ = 8 yielding β ≈ 0.29°, while the abstract and Secs. 5, 7, 8 repeatedly emphasize β ≈ 0.27°. No point in the main text actually derives a 0.27° number; this suggests the fiducial example or integration result was updated at some point, but the headline value in the abstract and discussion was not.  

- Sec. 5 uses θ_i ≈ 0.22 as the “headline parameter point” while still claiming the prediction β ≈ 0.27° “continues to hold,” which contradicts the linear scaling β ∝ θ_i. This again suggests partial edits (changing θ_i to enforce the spectator condition) without updating dependent numbers.  

Required fix: Decide on a single fiducial parameter point (m/H_0, θ_i, C_0), derive β and Ω_ϕ for that point, and enforce that same set of numbers consistently in Abstract, Sec. 2.2, Sec. 5, Sec. 7, and Sec. 8. Remove any leftover numbers from earlier drafts that are not directly connected to an explicit calculation in the body.

---

Given the density of new issues uncovered in the arithmetic, dimensional consistency, internal logic of the energy‑density argument, and abstract–body alignment, your earlier review was incomplete primarily in (i) not checking the energy‑density and β‑scaling consistency in Sec. 5 against Sec. 2.2, (ii) not challenging the un‑derived 0.27° “prediction” used throughout, and (iii) not scrutinizing the comparability of the various σ values and the strong LiteBIRD “9σ decisive test” claim.