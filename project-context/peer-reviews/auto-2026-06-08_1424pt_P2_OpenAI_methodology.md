# P2 auto-2026-06-08_1424pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5527 chars)
**Wall time**: 490.3s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts” (6 pages)

Scope of review
I evaluated the statistical methodology, derivation chains, dimensional consistency, internal arithmetic, and figure/table coherence. I recomputed every quoted σ, ratio, and Bayes factor from the numbers given, and checked symbol definitions and units.

Overall assessment
The paper aims to argue that a minimal ALP with fa ~ MPl and m ~ H0 “naturally” predicts an isotropic cosmic birefringence β ≈ 0.27°, consistent with Planck/ACT hints, and to present a light-weight inference and a LiteBIRD forecast. While the high-level narrative is plausible, several core methodological elements are not derivationally supported, and there are internal inconsistencies in the analytical development and in the Bayesian evidence calculation. Key symbols and normalizations (g_aγ, C0, C, Caγ, “fphoton”) are left undefined or used inconsistently; the pivotal displacement formula (Eq. 1) is introduced without derivation and contradicts the later numerical scaling; and the Bayes factor quoted in the abstract does not follow from the reported likelihood numbers. These are not cosmetic issues; they affect the central claim that the setup “naturally” yields β ≈ 0.27°. At present the work does not meet PRD methodological standards.

Detailed findings and required fixes

ESSENTIAL

P2-E1 (Abstract; Sec. 2.1–2.2, pages 1–2)
Problem: Contradictory scalings for Δφ/fa.
- Sec. 2.1/Eq. (1): “Δφ ≈ fa θi × O(1)” with 1 − J0(1) ≈ 0.24 implies Δφ/fa ~ 0.24 for θi ~ 1.
- Sec. 2.2: “cosmological field evolution gives Δφ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5×10−3 rad ≈ 0.27°.”
These are inconsistent by more than an order of magnitude and feed directly into the headline β ≈ 0.27°.
Required fix: Provide a transparent, step-by-step derivation (from the Klein-Gordon equation with H(z)) of Δφ/fa between recombination and today, with explicit assumptions on when rolling begins, and produce a single consistent numerical value. Remove one of the incompatible claims, and propagate the corrected Δφ/fa consistently to the quoted β prediction and all downstream inferences.

P2-E2 (Sec. 1 and 2.2, pages 1–2)
Problem: Inconsistent and undefined coupling normalization; missing α/(2π).
- Sec. 1 states β = Δφ/(2fa).
- Sec. 2.2 then uses β = gaγ Δφ/2 with gaγ = C0/fa.
Standard conventions are g_aγ = (α/2πfa) C (possibly model-dependent hypercharge mixing factors). Dropping α/(2π) (~1/860) changes normalization by orders of magnitude, and the paper alternates between C0, C, and Caγ without definitions.
Required fix: Adopt a single, explicit normalization for the ALP–photon interaction in the Lagrangian (spell out the exact coefficient multiplying Fμν F̃μν), define all symbols (C0, C, Caγ, g_aγ), include or justify exclusion of α/(2π), and use the same normalization in every equation and figure. If you choose a nonstandard normalization, provide a mapping to the standard one.

P2-E3 (Sec. 3.2–3.4; Abstract; page 2–3)
Problem: Bayes factor inconsistent with reported likelihood and unit dependence not handled.
- Using βcombined = 0.242° ± 0.061° (Eq. 4) and a flat prior β ∈ [0°, 1°], Savage–Dickey gives posterior density at zero ≈ (1/√(2π)σ) exp(−β̂2/2σ2) ≈ 0.0025–0.0028 per degree. With uniform prior density 1 per degree, B10 ≈ 1/0.0026 ≈ 380; ln B10 ≈ 5.9, not 5.17 as quoted. Your alternative prior ranges also do not match this recomputation.
- The Bayes factor depends on the choice of units unless the prior is transformed appropriately. Your presentation uses degrees without stating how prior densities transform, and labels the result as “indicative” only.
Required fix: Provide the exact formula used, including units and prior normalization, and the numerical inputs used to compute ln B for each prior range. Recompute ln B consistently, or correct the values. State explicitly that evidence and z-scores are not directly comparable (see P2-E8) and that the reported ln B pertains to “rotation vs. no rotation” under a 1D Gaussian summary likelihood, not “ALP vs. null.”

P2-E4 (Sec. 2.1, Eq. 1; page 2)
Problem: Eq. (1) is introduced without derivation and appears ad hoc (Bessel J0 of m/H0), with J0(0) present although J0(0)=1. It is not evident how a realistic H(z) through matter and Λ eras yields a closed-form J0(m/H0) dependence.
Required fix: Derive Eq. (1) from the field equation in an expanding universe (specify V(φ), linearization if used, regime of slow/fast-roll, and the time dependence of H). If an analytic Bessel approximation is used, state approximations and validity. Alternatively, replace with a numerical integration and provide the resulting Δφ/fa, with code or algorithmic details.

P2-E5 (Sec. 3.2–3.3; pages 2–3)
Problem: “Effective photon coupling fphoton × C0 = 1.73 ± 0.44” is undefined. There is no definition of fphoton anywhere in the manuscript, no units, and no equation linking it to β.
Required fix: Define fphoton rigorously, with units, and show the exact inference mapping from the β likelihood to this parameter (including any cosmological integral factors). If this is meant to be fa in units of MPl or an effective 1/gaγ normalization, write the explicit relation and recompute. If this cannot be defined unambiguously, remove this claim.

P2-E6 (Sec. 3.3; Table 1; pages 3–4)
Problem: Notation inconsistency and missing definition of “C = 8 fixed”; unexplained parameter Caγ. The MCMC uses C=8 in Run 1 and Caγ as a parameter in Run 2; neither is defined earlier, and their relation to C0 (Sec. 2.2) is unclear.
Required fix: Define C, Caγ, and their relation to C0 and g_aγ in the theory section, justify the value “8” if used (or remove the fixed-C run), and ensure that notation is consistent across the paper and figures.

P2-E7 (Sec. 3.2; page 2)
Problem: Independence assumption for Planck NPIPE and ACT DR6 birefringence estimates is asserted without justification. Overlapping sky coverage and common astrophysical systematics (e.g., foreground modeling assumptions) can induce correlations.
Required fix: Either justify independence (e.g., distinct instrument angle self-calibration strategies with negligible shared systematics) or include a correlation coefficient ρ in the combined likelihood and present a sensitivity study (e.g., ρ = 0, 0.2, 0.5) showing the impact on βcombined and its uncertainty.

P2-E8 (Abstract; Sec. 3.2–3.4; page 1–3)
Problem: Different “evidence” metrics (z-scores vs Bayes factors) are presented side-by-side without an explicit statement that they are not directly comparable and arise from different inferential frameworks (frequentist vs Bayesian with prior assumptions).
Required fix: At every juxtaposition of σ-significances and Bayes factors, add a sentence explicitly stating they are not directly comparable and depend on different assumptions (including priors).

MAJOR

P2-M1 (Sec. 1–2; page 1–2)
Problem: The claim “natural prediction” relies on informal O(1) arguments and a hand-waved “cosmological integration factor.” Without a correct coupling normalization (incl. α/2π if appropriate) and a numerically demonstrated Δφ/fa, this claim is not substantiated.
Required fix: Provide a quantitative calculation of β for fa ~ MPl, m ~ H0, and θi ~ O(1), with a chosen C normalization, demonstrating β ≈ 0.27° numerically. Include a plot of β vs m/H0 for representative θi and C, and quantify parameter ranges that yield β within the current 1σ band.

P2-M2 (Sec. 3.3; page 3)
Problem: Primary estimator not pre-declared; the paper reports both a summary-likelihood combination (Eq. 4) and MCMC results driven by a different input (βobs = 0.342 ± 0.094°), leading to different central values.
Required fix: State explicitly what the primary reported constraint is (combined Planck+ACT, or the MCMC using the Eskilt et al. value), and keep the others as cross-checks. Use consistent data combinations when comparing to the ALP model posteriors.

P2-M3 (Sec. 3.3; Table 1; page 3)
Problem: MCMC diagnostics are incomplete. R̂ requires multiple independent chains; you do not report the number of chains, chain lengths, warm-up/discarded steps, or per-run effective sample sizes (Neff).
Required fix: Report for each run: number of chains, total steps per chain, warmup length, acceptance fraction, R̂, and Neff for each parameter (θi, Caγ, log10 m, β). Increase chain lengths to yield Neff ≳ 5,000 on β for robust tail/evidence estimates (your own text cites tail unreliability).

P2-M4 (Sec. 3.3; page 3)
Problem: Priors are not physically motivated or fully specified. A flat prior on θi ∈ [0.01, π] may not reflect isotropy in field space (often a uniform prior on θi is fine but should be justified), and Caγ ∈ [1, 30] is not justified in terms of the underlying anomaly structure and couplings.
Required fix: Justify the chosen priors physically and explore sensitivity to alternate reasonable priors (e.g., θi uniform vs. sin-weighted; Caγ ranges informed by specific UV models).

P2-M5 (Sec. 3.4; page 3)
Problem: The “Bayes factor” is computed for a 1-parameter β model, but the ALP model evidence depends on (θi, m, Caγ, …) and their priors. The current ln B does not quantify “ALP vs. null.”
Required fix: Either reframe ln B as “rotation vs. no rotation under a Gaussian β likelihood” (not ALP evidence), or compute an honest ALP model evidence against β=0 using the stated priors and an explicit mapping β(θi, m, Caγ) (with numerical integration of the field evolution). State clearly which you report.

P2-M6 (Sec. 3.3; Fig. 1–2; pages 4–5)
Problem: Inconsistencies/omissions in reported posteriors across text and figures. Fig. 1 panel lists “β [deg] = 0.324 ± 0.099” for Run 2, whereas the text reports βALP = 0.336 ± 0.107 (Run 1) and βfree = 0.344 ± 0.096 (Run 3) but does not report the Run 2 β.
Required fix: Report the posterior summary for β in Run 2 in the text and ensure all descriptive statistics (median/mean ± 68% credible intervals) printed on figures match those in the text. Provide credible intervals for Caγ, θi, and log10(m/eV) explicitly.

P2-M7 (Sec. 3.2; page 2)
Problem: Degrees vs radians ambiguity in priors and reported likelihoods; unit choice affects Bayes factor under uniform priors.
Required fix: State the unit in which the β prior is uniform, justify the choice, and show that results are robust to reasonable prior parameterizations (or adopt a unit-invariant prior construction and document it).

P2-M8 (Sec. 2.1–2.2; page 2)
Problem: The text references the “cosmological integration factor” without showing the computation through matter and Λ eras.
Required fix: Either provide an analytic approximation with error bounds validated against a numerical solution, or include a numerical integration showing Δφ/fa as a function of m/H0 with a realistic H(z). This is the linchpin connecting the theory to β and must be explicit.

MINOR

P2-m1 (Sec. 1; page 1)
Problem: “Eskilt et al. joint Planck + ACT analysis” is cited as βobs = 0.342 ± 0.094°. The reference list cites Eskilt & Komatsu (2022) which is Planck+WMAP, not a Planck+ACT joint analysis.
Required fix: Correct the citation to the actual source of β = 0.342 ± 0.094°, and clarify whether it is Planck+WMAP, Planck only, or a joint analysis with ACT (with a proper citation if the latter).

P2-m2 (Sec. 3.2; page 2)
Problem: Independence statement for datasets is asserted tersely.
Required fix: Add one sentence acknowledging possible shared sky/systematic contributions, even if you ultimately assume independence, and cite relevant discussion (e.g., Minami–Komatsu method caveats).

P2-m3 (Abstract; Sec. 6; pages 1,5)
Problem: “No fine-tuning”/“naturalness” is repeatedly asserted qualitatively.
Required fix: Either quantify with a simple sensitivity/fine-tuning measure (e.g., fractional change in β for fractional changes in each parameter), or soften language.

P2-m4 (Fig. 2; page 5)
Problem: Axis labels and legend are clear, but the observed-value band should specify whether it is 68% or 1σ Gaussian.
Required fix: Annotate the band as “±1σ”.

P2-m5 (Acknowledgments; page 6)
Problem: “The author acknowledges the use of AI research assistants...” PRD has evolving policies on AI tools.
Required fix: Ensure compliance with PRD policy; if required, move this to a disclosure note as per journal guidance or remove.

NIT

P2-n1 (Sec. 2.1; page 2)
Problem: J0(0) appears in a denominator though J0(0)=1, making the ratio unnecessary.
Required fix: Drop J0(0) from Eq. (1) or explain why it is written that way.

P2-n2 (Typos/formatting)
Problem: Minor hyphenation artifacts (e.g., “configura￾tions”), inconsistent spaces before degree symbols, occasional en-dash/minus mismatches.
Required fix: Clean with the journal’s typesetting tools.

Arithmetic checks performed

- Weighted average of Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°) gives βcombined = 0.242° ± 0.061°, significance ≈ 3.97σ. Your Eq. (4) is consistent.
- LiteBIRD 0.27°/0.03° = 9.0σ as stated.
- Bayes factor recomputation with your Eq. (4) yields ln B ≈ 5.9 for a flat prior on [0°, 1°] under a standard Savage–Dickey calculation, not 5.17 (see P2-E3).

Length
At 6 pages the paper is concise. The issue is not length but methodological solidity. After addressing the essential/major issues, the current length may increase slightly to include the missing derivations and numerical checks; that is appropriate.

## Summary recommendation
REJECT

The manuscript contains multiple foundational methodological and internal-consistency problems: the key Δφ/fa scaling is contradictory; the ALP–photon coupling normalization is undefined/inconsistent and omits standard factors; the “effective photon coupling” reported is not defined; the Bayes factor is numerically inconsistent with the stated likelihood and sensitive to unit choices without disclosure; and the central analytic expression for Δφ is introduced without derivation. Because these issues directly affect the headline claim of a “natural” prediction for β ≈ 0.27°, the paper does not currently meet PRD standards. A thorough rewrite with correct and consistent normalization, a proper derivation or validated numerical computation of Δφ/fa, explicit definitions of all parameters, justified priors, a transparent evidence calculation, and a justified treatment of dataset correlations would be required for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P2-E9 (Sec. 1–2; energy budget vs “spectator” claim)
Problem: With m ~ H0, fa ~ MPl, and θi ~ O(1), the ALP’s background energy density is generically non-negligible and can be a sizable fraction of today’s critical density, contradicting the repeated “spectator” characterization.
- For the periodic potential V(φ) = m^2 f^2 (1 − cos(φ/f)), ρφ ≈ m^2 f^2 (1 − cos θi). The fractional density today is Ωφ ≡ ρφ/(3 MPl^2 H0^2) ≈ (m/H0)^2 (f/MPl)^2 (1 − cos θi)/3. With m ≈ H0, f ≈ MPl, and θi ~ 1 rad, Ωφ ≈ (1 − cos 1)/3 ≈ 0.15; for θi closer to π it can be ≳ 0.6.
Required fix: Quantify Ωφ(m, fa, θi) and demonstrate consistency with background expansion constraints (e.g., w(z), BAO/SNe, CMB) or explicitly impose priors that keep Ωφ subdominant. If the intent is that the field is a dark-energy-like component, state and analyze that, including wφ(z). If it must be a true spectator, restrict θi and/or (m, f) accordingly and propagate to β.

P2-E10 (Fig. 1 vs text; Run 2 numbers incompatible)
Problem: The caption and text state the Run 2 product Caγ × θi = 3.4 ± 1.1, but the 1D marginals visible in Fig. 1 show θi ≈ 1.33 and Caγ ≈ 13.4, whose product is ≈ 17.8, not 3.4. This is an order-of-magnitude inconsistency between the plotted marginals and the stated derived parameter.
Required fix: Recompute and report the correct product posterior consistent with the shown marginals, or correct the plotted marginals/labels. Provide the exact definition of Caγ and the computation of the product (including units/normalization).

P2-E11 (Sec. 3.3; MCMC arithmetic inconsistency)
Problem: The manuscript says accepted samples are 720–6,840 across runs and that “Neff ∼ 1,000.” For Run 3 (720 accepted), Neff cannot exceed the total post–burn-in draws. As written, Neff > N for Run 3 is impossible.
Required fix: Report per-run, per-parameter Neff that do not exceed the actual post–burn-in sample counts, alongside the number of chains, draws per chain, and warmup. If the stated “Neff ~ 1,000” was a rough average across other runs, clarify and give accurate Neff for each run.

MAJOR

P2-M9 (Abstract; Sec. 4; over-strong falsifiability claim)
Problem: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.” A null β would rule out nonzero isotropic rotation under the adopted 1D β-likelihood, but it does not exclude the ALP model class, which includes parameter regions with small C × θi (or different dynamics) yielding β ≈ 0. Rephrase to “this specific prediction” or provide a model-space evidence calculation that supports an “ALP vs null” exclusion.

P2-M10 (Fig. 2 caption/body mismatch on dataset provenance)
Problem: Fig. 2 compares posteriors and states consistency with “βobs = 0.342 ± 0.094°,” but elsewhere the paper elevates the combined Planck+ACT summary βcombined = 0.242 ± 0.061° as the main measurement (Eq. 4). The caption does not disclose that Fig. 2 uses the Eskilt value, not the combined summary. This invites confusion about which dataset underlies each curve.
Required fix: Explicitly state in the Fig. 2 caption and the main text that the figure uses the Eskilt joint-analysis likelihood (0.342 ± 0.094°), whereas Eq. (4) uses the Planck NPIPE + ACT DR6 point-estimate combination. Avoid mixing datasets in graphical summaries without clear labeling.

MINOR

P2-m6 (Sec. 6; references)
Problem: “Namikawa, Murai & Naokawa (2025). In preparation; cited for comparison…” is not an archival source and cannot substantiate any concrete numerical comparison.
Required fix: Replace with a published or arXiv-posted reference (with version/date), or remove the comparative claim.

P2-m7 (Sec. 2.1; onset of rolling criterion)
Problem: The text states rolling begins when H(z) ∼ m. The standard criterion for the end of Hubble friction is m ≳ 3H (or similar O(1) factor depending on definition). This factor-of-few matters for zroll and the integrated Δφ.
Required fix: State the precise criterion used (e.g., m = 3H) and show how zroll and Δφ depend on it; propagate any change to β.

P2-m8 (Abstract vs body; “order-unity” coupling claim)
Problem: The abstract quotes “fphoton × C0 = 1.73 ± 0.44 (order-unity)” without a definition of fphoton (and no units). Beyond the definitional gap already flagged, calling 1.7 “order unity” while Fig. 1 suggests Caγ ~ 13 compounds reader confusion about which coupling is being summarized.
Required fix: Define the coupling consistently across text and figures and avoid “order unity” language unless the same symbol/normalization is being referenced.

NIT

P2-n3 (Fig. 1 caption; derived parameter labeling)
Problem: The caption asserts a posterior on the product Caγ × θi, but the triangle plot does not show a 1D panel for that product; only Caγ, θi, log10 m, and β are labeled. This makes it unclear how the quoted product summary was obtained.
Required fix: Either include the 1D panel for Caγ × θi or remove the quantitative claim from the caption and move it to the text with a clear derivation method.

Explanation for additions
I re-checked all plotted and quoted numbers, recomputed derived quantities from the visible marginals, and audited physical self-consistency at the background level. The energy-density/spectator tension (P2-E9) and the Fig. 1 product inconsistency (P2-E10) were not called out in the initial review and are significant. The Neff > N issue (P2-E11), dataset-label ambiguity in Fig. 2 (P2-M10), and over-strong forecast claim (P2-M9) also emerged on this pass.