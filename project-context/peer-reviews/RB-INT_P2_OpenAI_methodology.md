# P2 RB-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5503a196 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9026 chars)
**Wall time**: 258.1s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
I evaluated the manuscript for methodological rigor: estimator definitions, derivations, internal arithmetic/units, propagation of uncertainties, statistical and Bayesian claims, and consistency between abstract/body/tables/figures. I recomputed each stated σ, ratio, and key percentage from the provided numbers and audited whether claims are traceable to the body text.

Overall assessment
The paper presents a sensitivity recast of SPHEREx and a scoping outlook for MegaMapper to test the matter‑bounce prediction fNL = −35/8 via the galaxy bispectrum and scale‑dependent bias, with a detailed discussion of template mismatch, a factor‑of‑two normalization audit (Cai vs. Li), and a Bayes‑factor model comparison. The author is careful to say “recast, not an independent forecast,” and flags many caveats.

However, several load‑bearing claims rest on approximations that are not rigorously tied to the survey Fisher metric, internal code‑artifact placeholders appear in the abstract/body, the code/DOI is missing, and parts of the analysis (e.g., using a single scalar template‑overlap r to rebook σ, the “noise‑weighted r = 0.84 ± 0.02” uncertainty, the GR‑nuisance quadrature) need either a principled derivation in the relevant Fisher metric or a more conservative treatment. The manuscript is also unusually long for a sensitivity recast and contains tangential material (cosmic birefringence). Below I list concrete issues and required fixes.

Findings (ESSENTIAL / MAJOR / MINOR / NIT)

P2‑E1 (ESSENTIAL)
Location: Abstract, p.1 (first page), lines discussing “c8 fnl running fisher.json …”
Problem: The abstract contains internal file names/versioning (“c8 fnl running fisher.json, Planck 2018, CAMB 1.6.6”), which are internal bookkeeping artifacts, not suitable for an abstract in PRD.
Required fix: Remove all internal file/artifact names and version strings from the abstract. Restrict the abstract to scientific results, not implementation details. If provenance is needed, cite methods sections, not file names.

P2‑E2 (ESSENTIAL)
Location: Data and Code Availability, pp. 25–26: “archived at Zenodo (DOI inserted at submission)”.
Problem: Missing permanent, frozen DOI. “DOI inserted at submission” is a placeholder and violates reproducibility standards.
Required fix: Provide the actual Zenodo DOI for the exact code/data snapshot corresponding to the submitted manuscript. Freeze the release and list its DOI here. Ensure all artifact names in the text map unambiguously to files in that release.

P2‑E3 (ESSENTIAL)
Location: Method (Sec. III.B pp. 8–10; Sec. IV pp. 10–11), Eq. (5) and usage throughout
Problem: The central procedure rescales σ(fNL) by a single scalar r computed in an off‑survey shape metric: fmeas = r fbounce and σeff = σlocal/r. This is exact only if (i) the estimator is linear in amplitude, (ii) the weighting matches the survey Fisher metric, and (iii) off‑template “projection noise” is negligible in that metric. The paper uses a mixture of unweighted shape cosine and several heuristic weights, with the CMB ℓ‑space Fisher quoted as a “consistency check,” not the SPHEREx 3D Fisher. The claimed r = 0.84 is then applied to Heinrich et al.’s σ(fNL) without re‑running the cross‑Fisher projection or quantifying projection‑noise variance under the SPHEREx bispectrum covariance.
Required fix: Provide a proper cross‑Fisher calculation in the SPHEREx bispectrum Fisher metric that projects the matter‑bounce shape onto the local template, and report (i) the amplitude loss r in that metric and (ii) the additional variance contribution from the orthogonal component (i.e., the exact increase in σ due to template mismatch in the survey Fisher covariance). Alternatively, if you insist on a recast, provide a conservative bound on σeff that includes projection noise computed with the SPHEREx covariance (not the unweighted rcos). Without this, the 5.2–5.5σ “optimistic” headline is not methodologically secured.

P2‑E4 (ESSENTIAL)
Location: Sec. III.B, p. 8–9 (Eq. 6 and surrounding prose)
Problem: Inconsistency in the quoted uncertainty for r. The text claims a “noise‑weighted central value r = 0.84 ± 0.02” while listing concrete values 0.829 (SDB), 0.830 (SPHEREx‑like), 0.835 (flat), and 0.876 (CMB‑Fisher). If the CMB‑Fisher endpoint is excluded from the “noise‑weighted” spread (as the text says), the span 0.829–0.835 is ±0.003 around 0.832—not ±0.02. The source and definition of the ±0.02 are unclear and not reproducible from the given numbers.
Required fix: Precisely define which weighting schemes enter the “noise‑weighted” band; list the values and compute the uncertainty accordingly. If the ±0.02 comes from additional “region‑masked variants” or Monte‑Carlo noise, tabulate those values in the SPHEREx Fisher metric. Otherwise, correct the ±0.02 to the actual spread you computed for SPHEREx‑like weightings and propagate the corrected uncertainty to the significance range.

P2‑E5 (ESSENTIAL)
Location: Throughout body (e.g., Sec. II.A p.4 n.1; Sec. II.B–C p.6–7; Sec. III.B p.9; Sec. VI pp. 12–16; Tables captions)
Problem: Internal code‑artifact names and JSON filenames (“c9i epsilon ratio check.json”, “null space analysis.py”, “phase3 bispectrum shape overlap.json”, etc.) are referenced repeatedly in the scientific narrative, not only in Data Availability. PRD articles should not depend on reading file names in the body to follow the argument.
Required fix: Move all such artifact references out of the main text into a short “Supplemental Material / Data Availability” note, or cite an Appendix where these artifacts are listed. Keep the body self‑contained (definitions, equations, results). Retain one clean sentence that a complete reproduction package is archived at DOI:… (see P2‑E2).

P2‑E6 (ESSENTIAL)
Location: Sec. VI.C, Eq. (9) and associated discussion (pp. 12–15)
Problem: For the Gaussian bounce prior, the Bayes‑factor formula is described qualitatively (“replace the bounce likelihood by the prior‑convolved marginal”) but no explicit closed‑form expression is given. Yet specific numerical values (e.g., 9.80 at σtheory = 1.0, broad [−15, +15]) are quoted as “exact CDF evaluations.”
Required fix: Write the explicit analytic form of the evidence for the Gaussian bounce prior (convolution of two Gaussians, still analytic) and the resulting Bayes factor, and show the numeric evaluation that yields 9.80. Provide the arguments (means/variances) used. This must be explicit enough for a reader to reproduce with a calculator.

P2‑E7 (ESSENTIAL)
Location: Sec. II.A pp. 3–5; Sec. II null‑space analysis
Problem: Claims about the null‑space sampling (10,000 samples, rcos > 0.97, median r = 0.85 etc.) are central to arguing robustness of template mismatch, but the measure is admitted to be basis‑dependent and arbitrary. The abstract and conclusions promote “validated via … 10,000‑sample null‑space scan (rcos > 0.97 for all samples).”
Required fix: Either (a) present basis‑invariant diagnostics (e.g., scan in the orthonormalized eigenbasis of the Fisher metric induced by the bispectrum covariance, or reparametrize by independent S3‑invariants) and show stability of rcos and r under reparametrizations; or (b) demote these statements to illustrative checks, not “validation,” and remove them from the abstract. At minimum, put the explicit 3×6 constraint matrix and the SVD singular values in an Appendix so a reader can verify conditioning.

P2‑E8 (ESSENTIAL)
Location: Sec. IV p. 10 (Fiducial‑shift invariance)
Problem: The claim that applying σ(fNL) = 0.7 “at the bounce-fiducial fNL = −4.375” is safe is supported only by a back‑of‑the‑envelope ζ‑space scaling (Eq. 7) that ignores galaxy bias, shot noise, and the six‑point covariance relevant for a multi‑tracer, photometric‑z bispectrum. The author states this is “a heuristic … not a covariance‑level derivation.”
Required fix: Provide a quantitative check in the galaxy field consistent with Heinrich et al.’s survey covariance (even a one‑bin simplified calculation) showing that second‑order fNL corrections to the bispectrum covariance are negligible at fNL ≈ −4.4 for SPHEREx scales. Alternatively, state explicitly that the 0.7 value is adopted as‑is and that no rigorous check was performed, and remove the heuristic calculation to avoid overstating rigor.

P2‑E9 (ESSENTIAL)
Location: Sec. VII.C–E and Table III/IV (pp. 17–20)
Problem: The GR‑contamination “σGR” is introduced and combined in quadrature with σbase, then used to quote detection significances and Bayes factors. There is no concrete mapping from σGR to physical projection effects in the SPHEREx bispectrum covariance; the cited Addis et al. paper treats the full relativistic power spectrum, not the bispectrum, and not SPHEREx. Yet the conservative end (σGR = 1.0) sets the lower end of the headline “realistic 2.6–5.5σ”.
Required fix: Either (a) provide a bispectrum‑level estimate (even order‑of‑magnitude) of GR projection contamination appropriate to SPHEREx redshifts and triangle configurations, or (b) clearly label σGR as an internal stress parameter not calibrated to SPHEREx and move all GR‑degraded “headline” numbers out of the abstract/conclusion, keeping them as illustrative only.

P2‑E10 (ESSENTIAL)
Location: Sec. IV Figure 2 caption and text, p. 11
Problem: Different null procedures (naive 6.25σ vs. template‑corrected 5.2–5.5σ vs. post‑budget 2.6–5.5σ) are juxtaposed in one bar plot. Although the caption attempts caveats, PRD requires explicit “not directly comparable” language at every juxtaposition per the journal’s reproducibility guidance.
Required fix: Add explicit statements in the caption and main text that the naive bar is not directly comparable and is shown for reference only, and that the post‑budget bars are sensitivity envelopes under additive‑quadrature heuristics, not joint‑marginalized precisions. Also annotate the figure accordingly.

P2‑M1 (MAJOR)
Location: Sec. III.B p. 9 (“squeezed‑cutoff insensitivity < 0.0002”)
Problem: The claimed absolute shift < 2×10−4 in r when varying x3,min lacks a table/figure or numerical evidence.
Required fix: Provide a small table/plot of r vs. x3,min with values (or move the claim to Supplement with a reference). Otherwise, remove the quantitative bound.

P2‑M2 (MAJOR)
Location: Sec. III.B p. 8–10 (definition of “SPHEREx‑like” and “LSS noise‑weighted” weighting)
Problem: The exact weights used to compute r under “SPHEREx‑like” and “LSS/SDB” schemes are not specified (functional form, k‑cuts, redshift weights).
Required fix: Define the weighting functions and k‑domains used for each scheme so that r can be reproduced without running your code. Provide at least the analytic forms and parameter values.

P2‑M3 (MAJOR)
Location: Sec. II.A footnote 1, p.4 and Appendix A.2 p. 27–28
Problem: The discussion of permutation‑count ratios and monomial‑basis transforms is central to resolving Cai vs. Li normalization and to your coefficient choice, but it remains qualitative. Readers cannot verify this without seeing the explicit monomial‑basis transform.
Required fix: Add an Appendix table that lists the six monomial orbits, their stabilizer sizes, the single‑ordering vs. full S3 orbit counts, and the resulting per‑orbit prefactor ratios. Include one explicit numerical check for a benchmark triangle to illustrate the factor‑of‑two.

P2‑M4 (MAJOR)
Location: Sec. II.C pp. 6–7 (ϵ‑correction 0.6–8%)
Problem: The 0.6–8% range is asserted based on scaling arguments (AT ∝ 1/ϵ^3 and ν dependence) without a worked estimate or error budget.
Required fix: Provide a concrete bound or example calculation showing how the two channels combine to yield the stated 0.6–8% range for Planck ns, or relabel this as a qualitative estimate and remove the numeric range from the abstract.

P2‑M5 (MAJOR)
Location: Sec. IV Shot‑noise caveat, p. 11
Problem: The “√11 ≈ 3.3×” inflation for σ(fNL) at n̄ ∼ 10−5 uses power‑spectrum intuition and is not obviously applicable to the bispectrum estimator in the squeezed limit. The second paragraph partially qualifies this but still quotes numbers.
Required fix: Either provide a bispectrum‑specific scaling derivation or simulation supporting the 15–30% effective degradation at relevant k for SPHEREx, or remove the quantitative statements.

P2‑M6 (MAJOR)
Location: Sec. VI.A–C, pp. 12–16 (Bayes‑factor grid)
Problem: While the delta‑prior results are fine, the reported Bayes factors against SSFSR (10^5–10^8) may mislead; these are trivially huge for a point‑mass alternative vs. a broad prior. The manuscript already cautions, but the table foregrounds them.
Required fix: Move the BF vs. SSFSR column to Supplement or annotate prominently in the table caption that these numbers are trivial consequences of point‑mass vs. broad prior and not meaningful model selection evidence.

P2‑M7 (MAJOR)
Location: Sec. II.A p. 5 and Sec. II.B p. 6 (injection‑recovery NMC = 200)
Problem: You claim rmeasured = 0.90 ± 0.01 from 200 realizations with a KSW estimator on tiled flat‑sky patches. Without specifying the per‑realization scatter (σr) and showing that σr/√N ≈ 0.01, this precision claim is unverified.
Required fix: Report the sample standard deviation of recovered r across the 200 realizations and the resulting standard error. Provide the noise level and exact weighting used in the KSW estimator to make the result reproducible.

P2‑M8 (MAJOR)
Location: Length and scope, entire manuscript (29 pages)
Problem: For a sensitivity recast that relies on an imported Fisher matrix and does not perform a joint‑covariance forecast, the paper is excessively long and includes tangential material (e.g., cosmic birefringence).
Required fix: Reduce to ≤18 pages by (i) moving extended Bayes‑factor exegesis, null‑space scan details, and code‑artifact inventories to an Appendix/Supplement; (ii) removing the cosmic‑birefringence aside; and (iii) streamlining repeated caveats.

P2‑M9 (MAJOR)
Location: Sec. III.B p. 8–9 (r > 1 statements)
Problem: The text allows r > 1 via null‑space excursions that enhance |BNL| away from the squeezed limit. While mathematically possible under your definition, the physical validity of such coefficients is not demonstrated.
Required fix: Either restrict to coefficient sets for which |BNL| is maximized in the squeezed limit (provide a check or physical criterion) or explicitly state that r is truncated at 1 when used to rebook σ in conservative forecasts. Clarify that no r > 1 case is used in any σeff rebooking (you imply this, but the text is scattered).

P2‑m1 (MINOR)
Location: Abstract and Sec. V, pp. 1 and 11
Problem: Statements about SPHEREx “launched March 2025” and MegaMapper timelines mix status updates with forecast content.
Required fix: Keep mission status factual but minimize forward‑looking schedule language in a PRD methods paper.

P2‑m2 (MINOR)
Location: Sec. II.A, Eq. (2), p. 3
Problem: Notation “kΣ1 ≪ k” appears garbled (“k∑1 ≪ k”?).
Required fix: Fix the notation for the squeezed limit in Eq. (2) and define k explicitly (k ≡ k2 ≈ k3).

P2‑m3 (MINOR)
Location: Sec. IX.D pp. 22–24 (SDB joint Fisher)
Problem: The redshift ranges and sample definitions differ between the SDB Fisher and the SPHEREx bispectrum Fisher (z = 0.1–1.5 vs. 0.5–2). This is said, but the juxtaposed numbers might confuse readers.
Required fix: Add a sentence at the start of Sec. IX.D explicitly reminding the reader that these are different samples/channels and numbers are not to be compared directly to the 0.7 baseline.

P2‑m4 (MINOR)
Location: Figures 4–5 captions (p. 18)
Problem: Axes lack units in captions (kmin is in h Mpc−1, σ(fNL) dimensionless). The blue/orange curve meanings are not repeated in captions.
Required fix: Add units to axis descriptions in the captions and restate the legend mapping.

P2‑m5 (MINOR)
Location: Sec. II.D p. 7 (rt ≈ 10−4)
Problem: This parameter is quoted without context or error bars and is not used later.
Required fix: Either provide a citation and relevance or remove.

P2‑n1 (NIT)
Location: Throughout
Problem: Heavy parenthetical asides interrupt flow and repeat caveats multiple times.
Required fix: Edit for concision; move long caveats to footnotes or a single consolidated caveat paragraph per section.

P2‑n2 (NIT)
Location: Table I caption, p. 6
Problem: The folded configuration footnote uses “a” but the footnote text is inline; slightly awkward formatting.
Required fix: Standardize footnote formatting.

Arithmetic and consistency audit (spot‑checks)
- |fNL|/σ = 4.375/0.7 = 6.25 (naive). Correct.
- Template‑corrected: 4.375×0.829/0.7 = 5.186; 4.375×0.876/0.7 = 5.475. The reported 5.2–5.5σ range is consistent.
- GR σGR = 1.0: σeff = √(0.7^2+1.0^2) = 1.221; 4.375×0.84/1.221 = 3.01σ. Matches ~3.0σ.
- “All combined (0.9+1.0)”: σeff = √(0.9^2+1.0^2)=1.345; 4.375×0.84/1.345 = 2.73σ. Matches ~2.7σ.
- Bayes factor delta prior broad: 30/(√(2π)·0.7) = 17.1. Matches.
- Rebooked σeff = 0.833: 30/(√(2π)·0.833) = 14.36. Matches.
- Delta prior narrow: 5.69/(Φ(13.4)−Φ(−0.893)) ≈ 5.69/0.814 ≈ 7.0. Matches.
- SDB Fisher: σunmarg 1.53 → σmarg 3.08 gives ρ ≈ −0.87. Matches stated.

Abstract‑last drift sweep
- The abstract’s 5.2–5.5σ optimistic, 2.6–5.5σ realistic ranges appear in the body and table IV, with the caveat that they are sensitivity envelopes under additive‑quadrature, not joint‑marginalized forecasts. However, per P2‑E3 and P2‑E9, the methodological basis (r‑only rebooking; GR quadrature) must be strengthened or the claims demoted in the abstract.
- The Bayes‑factor headline “≈ 9–14” (noise‑weighted rebooking) and “10–17” (r → 1) are consistent with Sec. VI, pending P2‑E6.
- The “validated via ℓ‑space Fisher overlap, 200 injection‑recovery, and a 10,000‑sample null‑space scan” summary in the abstract overstates the rigor of the r‑projection for the SPHEREx bispectrum unless P2‑E3/E7 are satisfied. Toning down the verb “validated” is needed unless you provide the SPHEREx‑metric cross‑Fisher.

Provenance surfaces
- Provide the permanent DOI (P2‑E2).
- Ensure the version of CAMB, Planck cosmology vector, and survey inputs are logged in a short Methods appendix (not the abstract) and match the archived code.

Stand‑alone reader test
- The paper is mostly self‑contained, but several key steps explicitly defer to external code artifacts (null‑space SVD, weight definitions). Move necessary definitions into the text or an appendix (P2‑E7, P2‑M2, P2‑M3).

Effect sizes
- The translation from fNL to fractional changes in bias/power is discussed in Sec. III.A, but a compact effect‑size statement near the main 5.2–5.5σ claim would help contextualize the detection (e.g., typical fractional change in the bispectrum amplitude in squeezed configurations at z~1).

## Summary recommendation
MAJOR REVISIONS

Justification
The manuscript contains valuable and careful work, and many numerical claims check out. However, several methodological pillars are presently heuristic: (i) the use of a single scalar template‑overlap r to rebook σ(fNL) without a SPHEREx‑metric cross‑Fisher and projection‑noise accounting; (ii) the “noise‑weighted r = 0.84 ± 0.02” uncertainty inconsistency; and (iii) the GR‑nuisance quadrature adopted as part of the headline “realistic” range without a bispectrum‑level calibration. In addition, the abstract/body include internal file names, and a frozen DOI is missing. Addressing the ESSENTIAL items (especially a proper cross‑Fisher projection or a conservative bound that includes projection noise under the SPHEREx covariance) and the MAJOR clarity/provenance issues is required before the paper can meet PRD’s methodological standards. The length should also be reduced for a sensitivity recast.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second‑pass audit)

I re‑audited the manuscript with the requested A–J checklist and found several new issues that were missed in my first review. I list only new items below, using the same tagging scheme. None of these duplicate items in my initial report.

P2‑E11 (ESSENTIAL)
Location: Sec. II.A (null‑space/overlap grid), Sec. III.B (template overlap scan), methods description of the triangle grid
Problem: The triangle sampling states “uniform grid in (k1,k2,k3) … subject to the triangle inequality (k1 ≤ k2 ≤ k3 ≤ k1 + k2)” but omits the lower triangle inequality |k1 − k2| ≤ k3. Without enforcing the lower bound, the grid admits non‑physical triplets (k3 < k2 − k1), biasing the r and rcos computations.
Required fix: Explicitly enforce the full triangle domain |k1 − k2| ≤ k3 ≤ k1 + k2 (with the chosen ordering convention) in the overlap grid and recompute r and rcos. Report the change (if any) to the headline r = 0.84 and to the CMB‑Fisher cross‑check. If the lower bound was implicitly enforced in code, state that and correct the text.

P2‑E12 (ESSENTIAL)
Location: Sec. VII.B (PNG bias discussion), paragraph beginning “at tree level, fNL enters the galaxy bispectrum…”
Problem: Dimensional inconsistency/missing kernel in the displayed “cross‑terms.” The text writes that ∆b(k) ∝ fNL bϕ/k^2 “propagates into the bispectrum estimator through cross‑terms fNL bϕ b1^2 P(k1)P(k2).” The cross‑term should be proportional to ∆b(ki) b1^2 P(kj)P(kk), i.e., it carries the 1/M(k) (or explicit 1/[k^2T(k)D(z)]) factor. As written, the expression is dimensionally incomplete and can mislead readers about the k‑dependence that drives the estimator weight.
Required fix: Replace the schematic term by the correct form with its explicit ∆b(ki) dependence (or M−1(k) kernel), and clarify how it is implemented in the Heinrich et al. Fisher. If this was shorthand, label it clearly as such and include the full expression in an appendix.

P2‑M10 (MAJOR)
Location: Sec. III.B (projection noise paragraph), p. 8–9
Problem: rcos is used as a proxy to claim “projection noise is subdominant” via 1 − rcos^2 ≲ 3–6%. This bound is not derived in the SPHEREx bispectrum Fisher metric and, in general, the variance increase from template mismatch depends on the survey covariance, not on an unweighted Euclidean shape cosine.
Required fix: Quantify the projection‑noise contribution in the SPHEREx bispectrum covariance (cross‑Fisher in the survey metric), or remove the 1 − rcos^2 bound and replace it with a conservative statement. This can be folded into the cross‑Fisher requirement in P2‑E3, but the specific numeric 3–6% claim should be retracted unless shown in the correct metric.

P2‑M11 (MAJOR)
Location: Sec. III.B (weighting schemes), bullet list and text describing “CMB Fisher, w ∝ k^2”
Problem: The “CMB Fisher” weight is described as w ∝ k^2 in k‑space, but the true CMB bispectrum Fisher weight is in ℓ‑space with Cℓ covariances. A k^2 proxy is not justified and risks confusing the reader about what the CMB cross‑check actually measures.
Required fix: Either (a) show the ℓ‑space Fisher calculation explicitly (with Cℓ and noise) and report r from that metric, or (b) relabel the k^2 proxy as a heuristic toy model, not a “CMB Fisher” weight. In either case, ensure that only the SPHEREx‑metric cross‑Fisher enters the headline (cf. P2‑E3).

P2‑M12 (MAJOR)
Location: Sec. IV (photo‑z “catastrophic outliers” paragraph), p. 11
Problem: The stated ≈5% degradation of σ(fNL) for a 10% catastrophic outlier fraction is not supported by a bispectrum‑covariance calculation; the formula fcat^2/(1+fcat)^2 ≈ 0.8% is a signal‑dilution heuristic that does not translate to the estimator variance. Yet a 5% total degradation is asserted.
Required fix: Provide a bispectrum‑level calculation (or simulation) of the degradation for representative SPHEREx bins and triangle weights, or clearly label the 5% number as a heuristic and remove it from any sensitivity accounting.

P2‑M13 (MAJOR)
Location: Sec. VII.B (bϕ prior sensitivity), Fig. 5 caption and text
Problem: The claimed O(20–50%) widening of σ(fNL) in the SPHEREx multi‑tracer bispectrum when relaxing bϕ universality is asserted by analogy to SDB (with Barreira 2022 cited) but not demonstrated for the bispectrum Fisher used here.
Required fix: Provide a bispectrum‑Fisher calculation (even simplified) showing the σ(fNL) change when bϕ is treated as a free parameter per tracer bin, or relabel the 20–50% range as a heuristic bracket and remove it from the post‑budget headline range.

P2‑M14 (MAJOR)
Location: Sec. II.A, “injection/recovery test,” p. 5
Problem: The KSW flat‑sky injection‑recovery uses a diagonal “SPHEREx photometric‑z power spectra” noise covariance and full‑sky geometry. This does not represent the 3D multi‑tracer bispectrum covariance (which is non‑diagonal and includes window/mode‑coupling). The quoted precision rmeasured = 0.90 ± 0.01 therefore overstates validation.
Required fix: Either (a) present a 3D bispectrum mock with a realistic survey window and covariance (even for a single redshift bin) to support the precision claim, including the sample standard deviation across realizations; or (b) clearly demote this test to a qualitative consistency check and remove the ±0.01 precision claim.

P2‑M15 (MAJOR)
Location: Sec. IV, opening paragraph of “Why bispectrum is robust,” p. 11
Problem: Overstatement: “the bispectrum channel avoids ultra‑large‑scale mode dependence.” The bispectrum does reduce reliance on the very largest modes compared to SDB, but it does not “avoid” large‑scale sensitivity; window effects and long‑mode triangles still matter.
Required fix: Rephrase to “is less sensitive than SDB to ultra‑large‑scale modes” and, if possible, add a quantitative comparison (e.g., effective kmin of triangles dominating the Fisher weight).

P2‑M16 (MAJOR)
Location: Sec. III.B (squeezed‑cutoff insensitivity), also relates to Fig./table absence
Problem: The statement that varying x3,min from 0.001 to 0.2 changes r by < 0.0002 lacks any table/plot. This is separate from P2‑M1’s request for a plot; here the absolute magnitude (<2×10−4) is implausibly tight given other quoted spreads and should be evidenced.
Required fix: Provide a small table or figure of r vs x3,min, with uncertainties from the numerical integration, or remove the quantitative < 0.0002 claim.

P2‑m6 (MINOR)
Location: Sec. III.B (grid size description), p. 4–5
Problem: The count “23,098 configurations” from a 50×50×50 log grid is plausible after ordering and triangle constraints, but the construction is underspecified for replication (bin edges, range, and whether the lower triangle bound was enforced; see P2‑E11).
Required fix: Specify kmin, kmax, binning scheme (log spacing, inclusive/exclusive edges), and whether both triangle bounds were used, so the configuration count and r can be reproduced without code.

P2‑m7 (MINOR)
Location: Sec. IV, Eq. (7) paragraph (“even before dividing by the mode count”)
Problem: Wording is confusing: Eq. (7) already includes Nmodes in the denominator; the text then says “even before dividing by the mode count,” which reads as if Nmodes were an extra factor.
Required fix: Clarify the sentence (e.g., “Numerically, the numerator fNL^2 Δζ^2 ≈ 4×10−8; with Nmodes≫1 the correction is far smaller than 10−3”).

P2‑m8 (MINOR)
Location: Sec. VI.C (hyperprior paragraph), p. 14–15
Problem: The reported Bayes factors for the σtheory ∼ U[0.5, 2.0] hyperprior are given without the explicit analytic expression (a direct integral over Gaussians) or numerical inputs.
Required fix: Provide the short analytic formula (it is a Gaussian‑prior marginal convolved with a Gaussian likelihood, integrated over a uniform σtheory), or move these numbers to Supplement with a reproducible snippet.

P2‑m9 (MINOR)
Location: Sec. III.B (ℓ‑space Fisher cross‑check), p. 9
Problem: The parameter “stable across ℓref = 50–950” is introduced without definition (what role ℓref plays in the weighting).
Required fix: Define ℓref (pivot or normalization) and how it enters the ℓ‑space Fisher overlap.

P2‑n3 (NIT)
Location: Sec. VII.B and elsewhere
Problem: Occasional shorthand like “cross‑terms fNL bϕ b1^2 P(k1)P(k2)” (missing kernels) and abbreviated references can confuse readers skimming equations.
Required fix: Where equations are schematic, mark them explicitly as “schematic” and point to a full expression in an appendix.

Explanation
These additions arose from targeted checks for (i) geometric correctness of the triangle domain, (ii) dimensional completeness of displayed expressions, and (iii) places where heuristic proxies (shape cosine, k‑space “CMB Fisher” weight, photo‑z dilution) were inadvertently elevated to quantitative claims in the absence of a survey‑metric calculation. Addressing the ESSENTIAL items (P2‑E11, P2‑E12) and the key MAJOR items that directly impact the quoted sensitivities (P2‑M10–M16) will materially improve the methodological rigor expected by PRD.