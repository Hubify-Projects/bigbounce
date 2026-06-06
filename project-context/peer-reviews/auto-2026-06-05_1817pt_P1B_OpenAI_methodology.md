# P1B auto-2026-06-05_1817pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7072 chars)
**Wall time**: 458.6s

---

Referee report for PRD submission: “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model” (P1B)

Scope of review
- Focus: methodological rigor, statistical validity, internal arithmetic consistency, dimensional checks, reproducibility, and correct handling of statistical “σ” claims.
- I audited all numbers in the abstract and conclusions against the body, recomputed quoted σ values and combinations, and checked key equations for dimensional consistency.

Overall assessment
The manuscript intends to document three technical verifications: (i) a stock-CAMB ΛCDM+ΔNeff proxy MCMC, (ii) a NaMaster pseudo-Cℓ pipeline validation via birefringence-angle injection, and (iii) an ALP-based consistency calculation for cosmic birefringence. Much of the statistical arithmetic checks out, and the paper repeatedly warns about scope and non-comparability of some results. However, there are several essential methodological and presentation issues that must be addressed before PRD publication:

- Mixing parameterizations without a consistent methods narrative (ΔNeff vs w0–wa); Table II presents a w0–wa result despite the methods section framing only a ΔNeff extension. This is a hard inconsistency.
- Meta-review/version-history language is embedded in the main text.
- The NaMaster “pipeline SNR” and bias claims lack an explicit estimator definition, uncertainty quantification for the bias, and a consistent noise model justification. Calling 10 μK·arcmin “conservative” for a Planck-based map is incorrect.
- Inconsistent dataset labeling (DESI DR1 vs DR2; Planck PR3/PR4) across sections; must be harmonized and precisely specified for each analysis.
- “Headline” σ-level departures in w0–wa are reported absent a corresponding evidence calculation; language should be tempered or the evidence supplied.

Findings and required actions

ESSENTIAL

P1B-E1 (Section III, p.4; and earlier on p.3–4) — Meta-review/version-history content in the manuscript
- Offending text examples:
  - p.4: “This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood…”
  - p.3: “An earlier count erroneously quoted ‘98.6% quintom-B’ weight…”
- Problem: PRD manuscripts must not include peer-review process commentary or version-history diagnostics.
- Required fix: Remove all references to earlier reviewer concerns, prior mistaken counts, and similar meta-commentary throughout.

P1B-E2 (Abstract p.1; Sec. III p.2–5; Sec. V.A p.6; Table II p.4) — Dataset-version incoherence
- Offending content:
  - Sec. V.A lists “DESI 2024 DR1 BAO [18]” while Table II caption and Sec. III “Physics interpretation (Table II)” use “DESI DR2.”
  - Multiple places toggle between “Planck 2018 NPIPE” and “Planck PR4/NPIPE” with ref. [17] being Planck A6 (PR3) parameters, not the PR4/NPIPE processing paper.
- Problem: The methods and results are not unambiguously tied to consistent data releases. This invalidates traceability and reproducibility.
- Required fix:
  - For each analysis (ΔNeff proxy, w0–wa chain, NaMaster injection), list the exact dataset releases and likelihoods used (e.g., Planck PR4/NPIPE CamSpec TTTEEE vX.Y + low-ℓ TT/EE vZ + lensing.native vW), with appropriate references to the PR4/NPIPE papers, and whether DESI DR1 or DR2 is used. Align all references and text accordingly.
  - Update [17] and add the correct PR4/NPIPE references for the likelihoods actually used.

P1B-E3 (Sec. IV, p.5–6; Eq. (1)) — Missing estimator definition and uncertainty quantification for NaMaster pipeline recovery; incorrect “conservative” noise claim
- Offending text:
  - “β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32)” and analogous SNR=25.71 for β=0.342°.
  - Noise stated as “ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check).”
- Problems:
  - No explicit estimator for β is defined (e.g., likelihood for EB, estimator formula, bandpowers included, weighting). No MC distribution (mean ± std) is shown; “SNR” is undefined operationally.
  - 10 μK·arcmin is not conservative for a Planck-based analysis; Planck polarization noise is typically larger. If the aim is to stress-test bias, the noise choice must be justified or rerun with Planck-like noise.
- Required fix:
  - Provide the estimator definition for β (equation), the binning and weighting scheme, and explicitly report for each injected amplitude: mean β̂ ± σ(β̂) from the 500 MCs and the bias ± its standard error [σ(β̂)/√NMC]. Explicitly define SNR = mean(|β̂|)/σ(β̂) and report it with the computed σ.
  - Either justify the ACT-like noise level as “conservative” in terms of bias (not variance) with references, or rerun/show a Planck-like noise test to demonstrate that the reported bias is robust to realistic Planck noise.

P1B-E4 (Sec. III/Table II vs Sec. V.A; p.3–6) — Parameterization inconsistency: ΔNeff vs w0–wa
- Offending content:
  - The paper frames the MCMC verification as “ΛCDM+ΔNeff” (stock CAMB), but then presents a “DESI DR2 w0–wa posterior” (Table II) and discusses “canonical quintom signature” without a dedicated methods description for the w0–wa analysis.
- Problem: Two distinct parameterizations are being reported. The w0–wa analysis lacks a full methods description (priors on w0, wa; nuisance parameters; whether τ priorized; exact likelihood stack; sampling settings).
- Required fix:
  - Add a dedicated methods subsection for the w0–wa chain specifying: priors for all cosmological and nuisance parameters, exact dataset combination and releases, sampler settings, and the convergence diagnostics per parameter. Alternatively, remove Table II and the w0–wa discussion from this paper and defer to another manuscript.

P1B-E5 (Sec. V.B p.6; Table II p.4) — “Headline result” σ-level departures without corresponding model evidence; LCDM point unsampled
- Offending text:
  - “The headline result is w0 = −0.812 ± 0.044 (departing … at +4.3σ) and wa = −0.667 ± 0.186 (… −3.6σ), with w0+wa = −1.48 ± 0.15 requiring phantom crossing…”
- Problems:
  - While the authors note Savage–Dickey is not usable and defer evidence to future work, declaring a “headline result” in σ units risks overclaiming model preference without a Bayes factor, especially since the LCDM point is unsampled by the chain.
- Required fix:
  - Either (a) provide a robust model-evidence calculation on the same likelihood stack (e.g., PolyChord/MultiNest), or (b) remove “headline result” phrasing and present the w0–wa constraints strictly descriptively, with a clear statement that no model preference is claimed absent a Bayes factor and that the reported σ-distances do not translate to a Bayes factor.

P1B-E6 (Abstract p.1; Sec. IV–VI p.5–7) — Mixed σ claims for different datasets without explicit non-comparability at each juxtaposition
- Offending content:
  - Abstract: “primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ…”
  - Sec. VI: “Headline observational constraint— … β = 0.342° ± 0.094° (3.6σ) [2] (WMAP9 + Planck PR4/NPIPE)…”
- Problem: Two different significance levels (Planck/ACT 2.4–2.9σ; WMAP+Planck 3.6σ) are both used as “primary/headline” in different places. Although each appears with context, they are not consistently labeled as non-comparable in every location they are juxtaposed.
- Required fix:
  - Choose a single headline constraint for this paper and mark all other σ values as auxiliary, explicitly stating “not directly comparable” at each juxtaposition. Given your own text, the WMAP+Planck 3.6σ appears to be your headline number; ensure the abstract and conclusions reflect that, with explicit caveats about shared-systematic treatment differences across analyses.

P1B-E7 (Sec. VI p.6–7; Eq. (2)) — ALP ODE solution: missing initial conditions and integration range; numerical provenance of Δϕ/fa ≈ 0.65
- Offending content:
  - “Numerical integration … yields Δϕ/fa ≈ 0.65 (m = H0, θi = 1).”
- Problem: No initial conditions (start redshift, treatment near recombination, initial velocity) or H(z) parameterization (cosmological parameters used) are specified. Reproducibility requires these details.
- Required fix:
  - Provide explicit initial conditions (e.g., ϕ(a=arec)=θi fa, ϕ̇(a=arec)=0), the a-range integrated, the exact H(z) and parameters used, and a code pointer with a fixed commit hash. Include a small table or CSV (in the repo) that reproduces Δϕ/fa for the stated parameter points.

P1B-E8 (Sec. IV p.5–6) — Noise/model mismatch in pipeline validation
- Offending content:
  - Using Planck Commander Q/U + ACT-like noise as a “conservative worst-case bias check.”
- Problem: The “conservative” claim is incorrect; 10 μK·arcmin is significantly lower noise than Planck polarization, yielding artificially high SNR for a Planck map. If the goal is to test bias robustness, justify why this noise choice gives a worst-case bias, or test with Planck-like noise.
- Required fix:
  - Correct the wording (remove “conservative worst-case”) and/or add a Planck-like noise realization test to show the bias is not sensitive to the noise level.

MAJOR

P1B-M1 (Sec. IV p.5–6) — Missing quantitative uncertainty on the reported pipeline biases
- Offending content:
  - Biases reported as 0.032° and 0.040° with no ± uncertainty.
- Required fix:
  - Report bias ± standard error (σ(β̂)/√NMC) from the 500 MC realizations; plot or provide the histogram of β̂ for at least one injection.

P1B-M2 (Sec. III/Table I p.3; Acknowledgments p.8; Appendix A p.8–9) — Reproducibility specifics
- Problem: While the repo is cited, the text should specify the exact repository commit hash and list the exact YAML file names corresponding to each table in the paper; the third, ongoing Planck-only chain is mentioned but not used—clarify its status or remove from conclusions.
- Required fix:
  - Add commit hash(es) and a mapping table (Table or Appendix) listing: result (e.g., Table I, column “full-tension”), YAML filename, likelihood versions, sampler settings, chain filenames, and a checksum/DOI for any deposited chains.

P1B-M3 (Sec. III p.5) — “Independent cross-validation” claim lacks numbers
- Offending content:
  - “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” relative to Liu et al. [11].
- Problem: No explicit numerical comparison is shown; dataset/parameterization mismatches are possible.
- Required fix:
  - Provide the exact values from [11] being compared and the corresponding values from your runs, and show the computed differences in σ units; otherwise remove this comparison.

P1B-M4 (Fig. 1 p.5) — Axis tick marks and labels
- Observation: In the embedded figure, ΔNeff axis tick labels appear as “0.5 0.0 0.5” (the negative sign on −0.5 appears to be missing). There is also a stray “8” near σ8 in the lower-right that looks like a rendering artifact.
- Required fix:
  - Ensure axis tick signs render correctly in the camera-ready PDF and that units for H0 appear on the 1D marginals or in the caption. Remove rendering artifacts.

P1B-M5 (Sec. V.A p.6) — Reference mismatch for Planck PR4/NPIPE likelihoods
- Problem: Ref. [17] is Planck 2018 parameters paper (A6), not the PR4/NPIPE release or CamSpec PR4 documentation.
- Required fix:
  - Add and cite the correct PR4/NPIPE (NPIPE) and CamSpec PR4 likelihood references actually used.

MINOR

P1B-n1 (Abstract p.1; throughout) — Consistency of units and spacing
- Example: “both in km s−1 Mpc−1 ).”
- Fix: Remove superfluous space before the closing parenthesis; ensure “km s−1 Mpc−1” is consistently formatted.

P1B-n2 (Sec. V.B p.6) — Language tempering
- “headline result” for w0–wa should be softened or removed pending a model-evidence calculation (covered by E5).

P1B-n3 (Sec. IV p.5) — Apodization specification
- “C2 apodization at 2°”: briefly define “C2” (e.g., cosine-squared) so the mask recipe is unambiguous.

P1B-n4 (Sec. VI p.7) — Add a forecast citation for σ(Neff) ≈ 0.03 (CMB-S4 or equivalent)
- Provide a standard reference for the quoted Neff sensitivity.

P1B-n5 (Appendix A p.8–9) — External data artifacts
- If possible, provide DOIs for the HuggingFace datasets, or at least a persistent link and a version tag.

P1B-n6 (Acknowledgments p.8) — AI assistant acknowledgment
- PRD policy on AI acknowledgments varies; consider moving to a footnote or confirm journal policy compliance.

Arithmetic and dimensional checks performed

- Table I and abstract ΔNeff and H0 values: consistent.
- Sample counts: 176,240 + 132,949 = 309,189 (as stated); post-burn-in figures are arithmetically consistent with 30% burn-in.
- σ-level departures in Table II:
  - w0 = −0.8122 ± 0.0436; |w0 + 1|/σ = 0.1878/0.0436 = 4.31σ.
  - wa = −0.6666 ± 0.1864; |wa − 0|/σ = 3.58σ. Matches text.
  - wpivot offset: (−1.0344 + 1)/0.0301 ≈ −1.14σ. Matches.
- χ2 contributions in Table II sum within rounding to the total: 10.6 + 10983.9 + 3043.0 = 14037.5 vs 14037.4 ± 5.6 (noting rounding).
- MB–H0 degeneracy constant check: at Riess anchor −19.253 − 5 log10(73.04) = −28.571; at chain mean −19.263 − 5 log10(67.69) = −28.416; difference 0.155 mag ≈ 3.16σ for σMB = 0.049. Consistent with text.
- Inverse-variance combination of β (Planck 0.30 ± 0.11°, ACT 0.215 ± 0.074°): β = 0.242 ± 0.061°, significance ≈ 3.9σ. Consistent with text (noting rounding).
- ALP birefringence conversion: α/(4π) ≈ 5.8×10−4; with Caγ = 8 and Δϕ/fa ≈ 1.07 gives β ≈ 0.00497 rad ≈ 0.285°, consistent with the stated 0.29°.
- Required Caγ for βobs = 0.342°: β(rad) ≈ 5.97×10−3; hence Caγ Δϕ/fa ≈ 10.3; with Δϕ/fa ∈ [0.2, 1.1] implies Caγ ∈ [9.4, 51.5], consistent with text.

Dimensional checks
- ALP EOM: ϕ¨ + 3Hϕ˙ + m2 fa sin(ϕ/fa) = 0 is dimensionally consistent in natural units. Birefringence formula β = (αEM/4π) Caγ Δϕ/fa is dimensionless as required.

Length
- 10 pages is acceptable for a methods companion if the essential clarifications above are addressed. No page reduction requested.

## Summary recommendation
MAJOR REVISIONS

The core numerical results (ΔNeff and H0) are consistent and appropriately caveated; the ALP consistency arithmetic checks out. However, the paper mixes parameterizations without a coherent methods narrative (ΔNeff vs w0–wa), includes meta-review text in the body, and lacks essential methodological details for the NaMaster pipeline estimator and uncertainty quantification. Dataset-version labeling is inconsistent across sections. These issues must be corrected for PRD standards of methodological rigor and reproducibility.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER FRESH-EYES AUDIT

P1B-E9 (Sec. III fn. 1) — Post–burn-in sample-count inconsistency
- Issue: The text first states the full-tension post–burn-in count is 123,129 (actual), but then asserts “the correct both-chains post-burnin total is 216,432,” which is just 0.7×(176,240+132,949). Using the stated actual 123,129 for the full-tension chain, the total would be 123,129 + 0.7×132,949 = 216,193, not 216,432.
- Required fix: Report the actual post–burn-in counts from the saved chains for each dataset, and avoid mixing nominal 70% burn-in with an “actual” count.

P1B-E10 (Table I note, p.3) — Misclassification and miscount of nuisance parameters
- Issue: The note calls “+10 Planck likelihood nuisance” and then lists Aplanck... calEE, Mb, where Mb is not a Planck nuisance parameter. The phrasing implies all 10 are Planck nuisances, which is incorrect.
- Required fix: Separate Planck nuisances from SN Mb explicitly and make the total parameter count transparent (e.g., “7 cosmological + 9 Planck nuisances + 1 SN nuisance (MB) = 17”).

P1B-E11 (Conclusions, p.8 vs Table I) — Planck-only run “reported in Table I” but no such column exists
- Issue: The conclusions say the 114,992-sample Planck-only run is “reported separately in Table I,” yet Table I contains only two columns (full-tension; Planck+BAO+SN).
- Required fix: Either add a Planck-only column to Table I or remove/retune that sentence.

P1B-E12 (Sec. VI, p.7) — βfree vs βALP MCMC conflation and sample-count mismatch
- Issue: The βfree (model-independent) fit is said to use “9,720 accepted samples across the 3 ALP-MCMC configurations Caγ={4,8,12},” but βfree should not depend on Caγ at all. As written, the βfree and βALP runs are conflated.
- Required fix: Clearly delineate two distinct runs: one for βfree (with its own sample count) and one (or three) for the ALP runs at fixed Caγ. Provide separate Nsamples and R̂ per run.

P1B-E13 (Sec. IV, p.5) — Commander beam specification likely incorrect or unreferenced
- Issue: The text adopts “Planck-2018 effective Gaussian beam (5′ FWHM at 143 GHz)” for a component-separated Commander CMB polarization map. The effective beam of a component-separated CMB product is not simply the 143 GHz instrument beam.
- Required fix: Use the proper effective beam window for the specific Commander CMB polarization product (with citation), or justify the 5′ approximation by demonstrating negligible impact on the β bias in a sensitivity test.

P1B-E14 (Sec. III, p.4) — Dimensional/log issue in MB − 5 log10(H0)
- Issue: Taking log10 of dimensional H0 is formally improper. While the difference between two points cancels units, the present expression is dimensionally sloppy and obscures reproducibility.
- Required fix: Re-express with h = H0/(100 km s−1 Mpc−1) as MB − 5 log10 h + const, or explicitly note that any constant arising from the choice of H0 units cancels in the difference.

P1B-E15 (Table II caption, p.4) — PR3/PR4 low-ℓ/high-ℓ mixing stated ambiguously
- Issue: Caption reads “Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native,” which mixes “Planck 2018” (PR3) with “NPIPE” (PR4) terminology. It is unclear which low-ℓ set (PR3 or PR4/NPIPE) is actually used.
- Required fix: Specify exactly which low-ℓ likelihoods (PR3 vs PR4/NPIPE) enter the w0–wa chain and update references accordingly.

P1B-M6 (Sec. III fn. 2) — Torsion/Immirzi strong-coupling scale formula needs justification
- Issue: The expression Λstrong ∼ MPl/√γBI is given without derivation. Since γ is dimensionless, an MPl/|γ| scaling is at least as plausible; the chosen √γ form may be incorrect.
- Required fix: Provide a derivation and citation for the γ dependence, or correct the formula.

P1B-M7 (Sec. IV, p.5) — EB estimator purification choice may bias EB
- Issue: purify_b=True, purify_e=False can leave E leakage in E (and thus affect EB). For EB-based β estimators, many analyses purify both E and B.
- Required fix: Justify the choice or rerun with purify_e=True and quantify the change in β bias.

P1B-M8 (Sec. IV, p.5) — TB channel omitted without justification
- Issue: The methods only mention EB. Many birefringence analyses jointly use EB and TB. Excluding TB can reduce SNR or bias cross-channel consistency checks.
- Required fix: State explicitly whether TB is included. If excluded, justify and verify that EB-only does not bias β in your pipeline test.

P1B-M9 (Sec. IV, p.5–6) — Choice of Commander polarization map for EB test needs justification
- Issue: Commander CMB polarization maps are typically noisier and less commonly used for EB analyses than SMICA/NILC/PR4 map products. Using Commander for a bias test is permissible, but the choice should be justified.
- Required fix: Explain the selection or add a parallel test with a standard PR4/NPIPE CMB polarization CMB map (e.g., SMICA/NILC) to demonstrate the bias conclusion is robust to map choice.

P1B-M10 (Sec. V.A, p.6; Appendix A) — Cobaya version mapping ambiguity
- Issue: The text says “v3.5 original; v3.6.1 verification” but does not map which figures/tables were produced with which version.
- Required fix: Provide a per-result version map (table or appendix) so reproductions know which Cobaya version to use for each result.

P1B-M11 (Sec. III, p.4) — Filename mismatch for YAML configs
- Issue: The text references a “spin torsion.input.yaml,” but Appendix A lists different filenames (e.g., cobaya full tension.yaml). This impedes reproducibility.
- Required fix: Replace with the exact filename used in the repository for the full-tension run (and others).

P1B-n7 (Sec. IV–VI) — Equation numbering on non-equations; missing estimator equation
- Issue: Eq. (1) and Eq. (2) are stated numerical results, not equations; the actual β estimator equation is still missing.
- Fix: Renumber only true equations and add the explicit β estimator definition (complements P1B-E3).

P1B-n8 (Sec. IV, p.5) — Beam window reference too informal
- Issue: “beam=bPlanckℓ wpixℓ” is not a reproducible identifier.
- Fix: Provide the exact beam window function file/name used for the chosen map product.

P1B-n9 (Conclusions/Abstract) — “first precision test” for σ(Neff) ≈ 0.03 is overstated
- Issue: Planck already provides a precision constraint; CMB-S4 improves it. “First precision test” is over-strong.
- Fix: Soften to “next-generation sub-0.03 precision” and add a CMB-S4 reference distinct from LiteBIRD (also complements P1B-n4).

P1B-n10 (Sec. VI, p.7) — Minor rounding inconsistency in inverse-variance β combination
- Issue: The inverse-variance combination of 0.30±0.11° and 0.215±0.074° gives 0.242°±0.061°; the text prints 0.241°.
- Fix: Standardize rounding and show the intermediate weights or exact values used.

P1B-n11 (Refs. [15], [22]) — Reference annotations contain meta/internal notes
- Issue: [15] and [22] include internal commentary (e.g., “the value used at L256/L416 of P1B,” “Used in P1A Sec. VI…”), which is nonstandard in references.
- Fix: Remove internal/meta notes from the reference annotations to meet PRD style.