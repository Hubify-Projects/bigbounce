# P2 R10v3 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar` [FALLBACK from sonar-pro]
**Input format**: TEXT + web search
**Wall time**: 21.5s

---

I can audit the internal consistency and reference plausibility of the supplied text, but I cannot actually verify the full bibliography against live arXiv/ADS in this interface because no browser tools are available beyond the provided search snippets. That means I can flag clear citation and arithmetic problems in the paper text, and I can verify only the items covered by the search results you supplied[1][2][3][6].

**Essential findings**

- **P2-E1 — Abstract, page 1:** The abstract claims “the 3.6σ isotropic birefringence signal” with \(\beta_{\rm obs}=0.342\pm0.094^\circ\), but the paper elsewhere gives the same value and uses it inconsistently with the claimed significance. If \(\beta/\sigma=0.342/0.094\approx 3.64\), the 3.6σ statement is numerically fine, but the paper also claims a separate combined result of \(0.242\pm0.061^\circ\) and labels that “3.9σ from zero”; \(0.242/0.061\approx 3.97\), so this should be stated as 4.0σ or derived explicitly with the same convention used throughout. Required fix: make the significance convention explicit and use consistent rounding across the abstract and body.

- **P2-E2 — Sec. 2.1, page 1:** Equation (1) is not mathematically or dimensionally justified as written: \(\Delta\phi \approx f_a\theta_i\left(1-J_0(m/H_0)/J_0(0)\right)\) introduces a Bessel function with no derivation, while the text below says “For \(m/H_0\sim1\), \(1-J_0(1)\approx 0.24\)” and then later asserts \(\Delta\phi/f_a\sim 10^{-2}\). Those numbers conflict by two orders of magnitude. Required fix: derive the field-displacement estimate from the actual cosmological equation of motion or remove the Bessel-function expression and replace it with a defensible numerical integration result.

- **P2-E3 — Sec. 2.2, page 1:** The chain “\(\Delta\phi/f_a\sim10^{-2}\) … yields \(\beta\approx C_0\theta_i\times5\times10^{-3}\,\mathrm{rad}\approx0.27^\circ\)” is internally inconsistent. \(5\times10^{-3}\,\mathrm{rad}=0.286^\circ\), so the arithmetic is roughly consistent only if \(C_0\theta_i\approx1\); but the preceding sentence says the model uses “order-unity inputs” without showing that the product is fixed near unity. Required fix: state the actual numerical values used for \(C_0\) and \(\theta_i\), and show the calculation from \(\beta=\Delta\phi/(2f_a)\) explicitly.

- **P2-E4 — Sec. 3.1 vs Sec. 3.2, page 2:** The paper says the summary-likelihood combination uses Planck NPIPE \((0.30\pm0.11^\circ)\) and ACT DR6 \((0.215\pm0.074^\circ)\), but the combined result \(0.242\pm0.061^\circ\) is not reproduced transparently from those inputs. A weighted average gives approximately \(0.248^\circ\), and the quoted uncertainty is plausible, but the paper does not show the weights or check the calculation. Required fix: provide the explicit combination formula and verify the arithmetic step-by-step.

- **P2-E5 — Sec. 3.1, page 2:** The text says “For the MCMC parameter estimation … we use the Eskilt et al. joint analysis value \(\beta_{\rm obs}=0.342\pm0.094^\circ\), which differs because it fits the full EB cross-spectrum rather than combining point estimates.” This is a major methodology mismatch: the paper uses one dataset for the summary likelihood, a different dataset for MCMC, and then compares the resulting posteriors as if directly interchangeable. Required fix: justify the use of two different observational summaries, or use one consistent likelihood throughout.

- **P2-E6 — Sec. 3.2, page 2:** Equation (3) is malformed typographically and mathematically ambiguous. The product and exponential are missing the standard \(\sum_i\) form in the exponent, and the notation \(\sigma_i\) is not typeset consistently. Required fix: rewrite the likelihood in standard notation and define all symbols.

- **P2-E7 — Sec. 3.2/Table 1, page 2:** Table 1 says “Run 1 ALP (\(C=8\) fixed)” while the surrounding text uses \(C_0\), \(C\), and \(C_{a\gamma}\) interchangeably. The notation is fused and inconsistent, making it unclear whether the parameter fixed at 8 is the anomaly coefficient, the photon coupling, or a derived product. Required fix: use a single symbol set and define whether 8 is dimensionless, a coupling normalization, or something else.

- **P2-E8 — Sec. 3.3, page 2:** The priors “\(\log_{10}(m/\mathrm{eV})\) flat on [−35, −30]” are incompatible with the earlier physical discussion that the model uses \(m\sim H_0\), which corresponds to \(\log_{10}(m/\mathrm{eV})\approx -33.1\), so that part is fine, but the paper never explains why the posterior is not prior-dominated given the extremely broad interval. Required fix: demonstrate prior sensitivity or narrow the parameterization to the physically motivated region.

- **P2-E9 — Sec. 3.3, page 2:** The paper reports “sample sizes (720–6,840 accepted samples)” and “\(N_{\rm eff}\sim 1{,}000\)” while also claiming \( \hat R -1 < 0.01\). These diagnostics are not sufficient to justify the Bayes factor or tail estimates for a low-dimensional cosmological inference problem, especially when the paper itself admits modest sample sizes. Required fix: either increase the chains substantially or remove overstrong evidence claims.

- **P2-E10 — Sec. 3.3, page 2:** Equation (6) \(\beta_{\rm ALP}=0.336\pm0.107^\circ\), Eq. (7) \(\beta_{\rm free}=0.344\pm0.096^\circ\), and the observed \(\beta_{\rm obs}=0.342\pm0.094^\circ\) are presented as distinct constraints, but the paper never specifies whether the posteriors are independent, derived from the same data, or sharing a common likelihood. Required fix: state the data source and likelihood for each posterior and avoid presenting them as independent measurements if they are not.

- **P2-E11 — Sec. 3.4, page 3:** The Bayes factor is not reproducible as presented. “\(\ln B=5.17\)” via Savage–Dickey with a flat prior \(\beta\in[0^\circ,1^\circ]\) is stated without the prior density at zero, the posterior density estimate, or the normalization convention. Required fix: provide the full Savage–Dickey calculation and specify whether \(\beta\) is restricted to positive values.

- **P2-E12 — Sec. 4, page 3:** Equation (10) states “Significance \(=0.27/0.03=9\sigma\)” and then “If LiteBIRD measures \(\beta=0\pm0.03^\circ\), the ALP explanation is excluded at \(9\sigma\).” This conflates discovery significance for a nonzero prediction with exclusion significance under a null observation; these are not identical statements. Required fix: distinguish forecast detection significance from exclusion significance and specify the assumed test statistic.

- **P2-E13 — Sec. 5, page 4:** The claim that the prediction is “independent of bounce cosmology” is reasonable only if the ALP dynamics are truly spectator and the post-bounce history does not affect \(\Delta\phi\), but the paper offers no derivation. Required fix: add a short argument showing why the result is insensitive to the background expansion history, or weaken the claim.

- **P2-E14 — Sec. 6, page 5:** The paper says “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces \(\beta\sim0.3^\circ\), and Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints using the full Planck EB spectrum.” The first citation is verifiable from search results only for title/venue/DOI, not for the specific quantitative claim; the second citation is listed as “arXiv e-prints, 2025” and “in preparation,” which is inconsistent and unverifiable from the provided search results. Required fix: remove unsupported quantitative attribution unless directly traceable to the cited paper’s abstract or tables, and replace the “in preparation” placeholder with a real bibliographic entry or delete it.

**Major findings**

- **P2-M1 — Abstract and Sec. 1, pages 1–1:** The paper states “Planck HFI analysis [Minami and Komatsu, 2020] reported \(\beta=0.35\pm0.14^\circ\) (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.” The provided search result for the ACT paper identifies a completely different arXiv item: **“Planck Constraints on Axion-Like Particles through Isotropic Cosmic ...”** is arXiv:2506.20824 and is about constraints from Planck high-frequency channels, not an ACT DR6 confirmation of birefringence[1][2]. Required fix: verify the ACT citation, correct the title/authors/venue/arXiv ID, and remove the unsupported claim if it is not in the cited paper.

- **P2-M2 — References, page 6:** The citation “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.” is likely incomplete or incorrect. The search result provided points to arXiv:2506.20824, titled **“Planck Constraints on Axion-Like Particles through Isotropic Cosmic ...”**, not an ACT birefringence paper[1][2]. Required fix: replace with the correct arXiv ID, title, coauthors, and publication status, or delete if this reference does not exist as cited.

- **P2-M3 — References, page 6:** The citation “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” is a red-flag bibliographic placeholder. “In preparation” cannot be used as a stable reference in a PRD bibliography unless the manuscript is publicly posted and clearly identified. Required fix: replace with a published or arXiv-posted paper with verifiable metadata, or remove the citation and corresponding claim.

- **P2-M4 — References, page 6:** The bibliography contains mixed citation styles and inconsistent publication status labels: “Physical Review D, 106:063503,” “arXiv preprint, 2025,” “arXiv e-prints, 2025. In preparation,” and “Companion paper, submitted simultaneously, 2026a/2026b.” Required fix: standardize all references to a single journal style with complete metadata and remove non-bibliographic placeholders from the reference list.

- **P2-M5 — Sec. 6, page 5:** The sentence “The matter-bounce non-Gaussianity \(f_{\rm NL}=-35/8\) provides a complementary and independent test [Golden, 2026b].” introduces an unrelated result that is not developed anywhere in the paper and is not necessary to support the birefringence argument. Required fix: either explain the relevance quantitatively or remove the cross-paper claim.

- **P2-M6 — Across Secs. 1–6, pages 1–5:** The paper repeatedly mixes notation \(C_0\), \(C\), \(C_{a\gamma}\), and “\(f_{\rm photon}\times C_0\)” for what appears to be the same coupling combination. This is a substantive clarity problem because it obscures which parameter is actually inferred. Required fix: define one parameterization and use it consistently throughout.

- **P2-M7 — Sec. 3.2/Table 1, page 2:** Table 1 is too sparse to support the claims in the text. It reports only run labels, samples, \( \hat R-1\), and status, but not acceptance rate, burn-in, autocorrelation time, posterior dimensionality, or likelihood model. Required fix: include the missing diagnostics or remove the table.

- **P2-M8 — Sec. 4, page 3:** The forecast statement “LiteBIRD, with \(\sigma(\beta)\approx0.03^\circ\), will test this prediction at 9σ significance” is presented as definitive, but the same section notes dependence on self-calibration and systematics. Required fix: quantify the systematic-error floor and state whether \(0.03^\circ\) is statistical-only or total uncertainty.

- **P2-M9 — Abstract, page 1:** The abstract claims “This birefringence prediction is independent of bounce cosmology.” That is a broader physics claim than the paper establishes, because the only support is a brief qualitative statement in Sec. 5. Required fix: weaken to “in the simplified setup considered here” unless a derivation is added.

**Minor findings**

- **P2-N1 — Sec. 2.1, page 1:** “Hubble friction exceeds the mass” should be written as \(H\gtrsim m\) or equivalent; the prose is imprecise.

- **P2-N2 — Sec. 2.2, page 1:** “ABJ anomaly” should be defined on first use for a general PRD audience.

- **P2-N3 — Sec. 3.1, page 2:** “Planck NPIPE” and “ACT DR6” should be identified with enough detail to make the measurement traceable, including whether the cited values are from a joint fit, a derived posterior, or a summary estimate.

- **P2-N4 — Sec. 5, page 4:** “14-barrier catalog” is unexplained jargon and reads like internal project language. Required fix: define or delete.

- **P2-N5 — References, page 6:** The reference “LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky cmb polarization survey.” should capitalize CMB and preserve the official title formatting.

- **P2-N6 — Abstract, page 1:** “order-unity inputs” is vague in a paper making quantitative claims. Specify the actual parameter values.

**Citation-forensics verification notes**

- The search results confirm that arXiv:2506.20824 is titled **“Planck Constraints on Axion-Like Particles through Isotropic Cosmic ...”** and is an accepted PRD paper, with DOI metadata available via arXiv-issued DOI[1][2]. That does **not** match the paper’s reference to “Cosmic birefringence from the Atacama Cosmology Telescope,” so the ACT citation is very likely wrong or fused with another work[1][2].

- The search results also confirm the existence of a different APS paper, **“Isotropic cosmic birefringence from an oscillating axionlike field”**, DOI 10.1103/PhysRevD.111.043514[3]. That is not the same as the paper’s cited Fujita et al. 2021 title, which may still be correct, but the present search data do not verify the full bibliographic details beyond what is in the paper text.

- No search result in the provided set verifies the “Namikawa, Murai & Naokawa” item, and the paper itself labels it “In preparation,” which is not acceptable as a stable citation.

## Summary recommendation
**REJECT**

The manuscript has major citation-integrity problems, including at least one likely misidentified or fused reference, an “in preparation” citation in the bibliography, and unsupported quantitative attributions to prior work. It also contains internal arithmetic and methodological inconsistencies in the core signal estimates, an unjustified field-evolution formula, inconsistent notation for the coupling parameter, and overstrong claims about significance and cosmology-independence that are not demonstrated in the text.