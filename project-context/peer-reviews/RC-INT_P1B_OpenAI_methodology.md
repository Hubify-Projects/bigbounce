# P1B RC-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=0b1108a9 pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4730 chars)
**Wall time**: 427.2s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model” (22 pp)

General assessment
The manuscript documents three verification exercises: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy; (ii) a NaMaster pseudo-Cl Monte Carlo on synthetic CMB polarization skies to validate EB-based rotation recovery; (iii) an ALP-based birefringence consistency check using a Gaussian summary likelihood for β from the literature. The author is careful to present all three as compatibility checks rather than claims of model preference or detections. Many caveats and internal-consistency checks are provided.

Methodologically, most arithmetic checks and dimensional relations are correct (spot-checks below). However, several items fall short of PRD standards for a methods paper: the use of an overlap-uncorrected DES-SN5YR×Pantheon+ product likelihood to quote sharpened w0–wa constraints (even as an “exploratory cross-check”) needs hard guardrails; the NaMaster validation should include a minimal beam-mismatch stress test and an ℓ-range robustness sweep; and the data/code availability needs stable, citable DOIs rather than “pending” placeholders. A few numerical and wording cleanups are also required.

Below I provide a detailed, itemized audit with required fixes.

Findings

ESSENTIAL

P1B-E1
Section: Data and Code Availability (p. 18–20)
Problem: Datasets are hosted on GitHub/HuggingFace with “DOI assignment is pending; identifiers will be inserted at submission.” PRD requires stable, citable archival. Pending DOIs are insufficient at acceptance.
Required fix: Mint permanent DOIs (e.g., Zenodo) for (i) the exact Git snapshot corresponding to the paper version, (ii) frozen MCMC chains backing Tables I–II and ALP chains in Table IV/Fig. 4, (iii) NaMaster artifacts (masks, seeds, outputs), and (iv) configuration files (Cobaya YAMLs). Replace all “pending” language with the final DOIs and the exact release/tag hashes used in the paper. Confirm that the archived snapshot reproduces the numbers in the manuscript.

P1B-E2
Section: w0wa cross-check (pp. 12–13; Table II)
Problem: The DES-SN5YR × Pantheon+ SN product likelihood double-counts ~20% shared events without a joint covariance. Although the overlap caveat is stated, the text still reports tightened marginalized constraints (e.g., wpivot = −0.952 ± 0.019; w0 + wa = −1.4788 ± 0.1485) and states “phantom crossing” in the survey range. Even with caveats, presenting narrowed posteriors from a known-overlapping product-likelihood risks overinterpretation.
Required fix: One of:
- Provide overlap-controlled alternatives: two control chains (CMB+BAO+Pantheon+ only; CMB+BAO+DES-SN5YR only) and quantify the shift in (w0, wa, wpivot) relative to the combined product. Or,
- Remove all sharpened σ-level widths (and the phantom-crossing redshift inference) from the main text and figure captions; relegate the overlap-uncorrected chain to an appendix as an illustrative, not-for-quantification diagnostic. Keep only qualitative, non-quantitative statements in the body. In either case, make it explicit next to every quoted width from this chain that it is not a valid uncertainty due to double counting.
Also add an explicit “not directly comparable” disclaimer anywhere these widths appear alongside properly combined constraints.

P1B-E3
Section: Data methods: CMB E–B analysis (pp. 9–12; Fig. 3)
Problem: The pipeline validation asserts robustness of the recovered β to mask choices and apodization scale, but (by design) omits any beam mismatch test and exercises only one ℓ-range/weighting choice in the production configuration (unweighted). As a methods paper, a minimum stress test is needed to justify the “observed pipeline bias floor” characterization.
Required fix: Add at least:
- One beam-mismatch stress test: generate skies and templates with a modestly different Gaussian beam FWHM (e.g., 1° vs 0.8°), and report the resulting shift in β̂ (mean over N=500 realisations) relative to the “no-beam” baseline.
- One ℓ-range robustness test: repeat the β recovery restricting bins to e.g. 30 ≤ ℓ ≤ 512, and report β̂ and bias compared to the full-range unweighted fit. This is particularly important given the demonstrated sensitivity of the bias to inverse-variance weighting (high-ℓ noise-dominated bins).
If these tests are deferred, remove the term “bias floor” and rephrase as “bias observed under the specific unweighted, no-beam, mask-apodization configuration; does not bound real-sky systematics.”

P1B-E4
Section: Abstract (p. 1) and Sec. IV (pp. 8–12)
Problem: Multiple significance metrics are juxtaposed: pipeline template-fit SNRs (20–26), published sky measurements 2.7–2.9σ (Planck NPIPE/ACT DR6), and 3.6σ (WMAP+Planck joint). While much of the text warns about incomparability, the abstract lists “2.7–2.9σ” and “3.6σ” in proximity without an explicit “not directly comparable” qualifier in that sentence.
Required fix: In every place where the 2.7–2.9σ Planck/ACT values and the 3.6σ WMAP+Planck value are mentioned together (notably abstract and Sec. IV), add an explicit clause that they are derived from different datasets and analysis pipelines and are not directly comparable. Also explicitly distinguish these from the pipeline SNR values, which are MC-recovery significances on synthetic skies.

MAJOR

P1B-M1
Section: Sec. III “MB–H0 joint-posterior offset check” (pp. 7–8)
Problem: Arithmetic for the Pantheon+ degeneracy constant slightly off. Using the paper’s numbers: MB = −19.263, h = 0.6768 gives −19.263 − 5 log10(0.6768) = −18.418 (not −18.415). The stated offset “0.156 mag” vs Riess’s “−18.571” is then ~0.153 mag. The qualitative point stands but the numeric should be corrected.
Required fix: Correct the constant and offset values, or report to 0.01 mag precision to avoid spurious accuracy. Add exact calculation or provide a line showing the computed numbers.

P1B-M2
Section: Sec. IV; Fig. 3 caption and main text (pp. 9–12)
Problem: The “observed NaMaster pipeline bias” is reported as a single worst-case figure (0.040° ± 0.002°) from the unweighted estimator. The text usefully shows that inverse-variance weighting removes ~80% of the bias at βinj=0.27°, and that a lensed-BB injection reduces the multiplicative under-recovery by ~5 percentage points. However, amplitude-independence of these remedial effects is not demonstrated at βinj=0.342°, where the worst-case bias is quoted.
Required fix: Report the β̂ recovered for the inverse-variance-weighted estimator and for the lensed-BB injection also at βinj=0.342°, or state explicitly that the improvement has not been verified at that amplitude. If not run, remove any implication that the 0.040° worst-case bias applies unchanged under those remedial changes.

P1B-M3
Section: Sec. III (pp. 3–8)
Problem: Release pairing substitution test (2018 low-ℓ EE/lensing vs PR4-consistent low-ℓ EE/lensing) is summarized only for ΔNeff. H0, σ8, S8, Ωm are stated to agree within <0.1σ, but no numbers are tabulated.
Required fix: Add a small table (or an appendix line) listing the differences (in σ units) for H0, σ8, S8, Ωm between the frozen chain and the c15 verification rerun, for completeness.

P1B-M4
Section: Sec. VI (pp. 13–17)
Problem: The Ωa < 0.01 “spectator-safe” classification relies on Eq. (9) evaluated with H0 fixed to a single value; the text says marginalizing H0 changes Ωa by ≲3% but does not show the calculation.
Required fix: Provide a short derivation: since Ωa ∝ H0^−2, show numerical shift for H0 = 67.68 ± 1.06 (or a bracketing by ±1σ), and confirm the quoted ≤3% change explicitly. One line is sufficient.

P1B-M5
Section: Sec. IV (pp. 9–12)
Problem: The production NaMaster configuration intentionally uses no beam and assumes cancellation in the estimator/template. This is plausible, but the statement “would largely cancel” needs quantification in a single stress test (see P1B-E3). If not provided, at least rephrase to a conditional statement and avoid asserting cancellation without data.
Required fix: Either add the beam-mismatch test (as requested in P1B-E3) or soften the language to “may largely cancel under identical deconvolution, but we have not tested beam mismatch here.”

P1B-M6
Section: Acknowledgments (p. 18)
Problem: The paper acknowledges the use of a generative AI assistant (“Claude”) for systematic analysis and manuscript preparation. PRD has evolving policies on the use and acknowledgment of generative tools and authorship responsibilities.
Required fix: Consult PRD policy; if allowed, include a brief statement clarifying that the tool did not generate scientific claims or results and that the author takes full responsibility; otherwise remove the acknowledgment.

MINOR

P1B-m1
Section: Abstract (p. 1); Conclusions (pp. 17–18)
Problem: Occasional wording suggests “bias floor” for NaMaster pipeline. Given the limited stress testing, “floor” suggests generality that is not fully supported.
Required fix: Replace “observed pipeline bias floor” with “observed bias in our unweighted, no-beam configuration,” or similar, in abstract and conclusions.

P1B-m2
Section: Sec. IV, robustness battery (pp. 11–12)
Problem: The phrase “≈5 percentage-point reduction” in bias could be misread as referring to angle units. It refers to multiplicative under-recovery (12% → ~7%), not degrees.
Required fix: Add “in the multiplicative under-recovery” to eliminate ambiguity.

P1B-m3
Section: Sec. VI (pp. 13–17)
Problem: The statement “Even the lower end exceeds the standard KSVZ/DFSZ benchmark range, which predicts |Caγ| ∼ O(1)” is correct but lacks a citation.
Required fix: Add a standard axion-models reference for Caγ values (e.g., di Cortona et al., JHEP 01 (2016) 034, or an equivalent axion review with explicit Caγ benchmarks).

P1B-m4
Section: Sec. III (p. 5)
Problem: Footnote 1 (burn-in reconciliation) is unusually long and contains process minutiae that do not affect scientific conclusions.
Required fix: Move this footnote’s nonessential audit-trail text to the repository README/CHANGELOG and keep only 1–2 lines in the paper.

P1B-m5
Section: Sec. IV; Fig. 3
Problem: Figure 3 currently does not label that SNR values are “template-fit SNR on synthetic skies.” The text explains it, but the figure is self-contained only if the caption says so.
Required fix: Add “SNR shown is template-fit significance on MC skies; not a real-sky detection significance” to the figure caption.

P1B-m6
Section: Sec. V.A/Table III (p. 13)
Problem: The lensing likelihood variant (native vs clik) is tracked in text. For completeness, note in Table III that “iter2 w0wa uses planck 2018 lensing.native” directly in the table, not only in the caption/narrative.
Required fix: Add this parenthetical to the Table III “iter2 w0wa” row.

P1B-m7
Section: Sec. IV (p. 10)
Problem: The rotation estimator formula (Eq. 1) uses CEE,tmpl but the exact numerical normalization conventions (e.g., whether bandpowers are Dℓ or Cℓ) are not stated explicitly.
Required fix: State explicitly that all bandpowers are Cℓ (not Dℓ) and consistent between maps and templates.

NITS

P1B-n1
Section: Sec. II (p. 3)
Problem: “We frame the proxy as a bounce-class compatibility check” — stylistic but could be read as model-preference language.
Required fix: Consider “We use the proxy only as a compatibility check.”

P1B-n2
Section: Sec. VI (p. 14)
Problem: “Where the data-preferred joint product is Caγ(Δφ/fa) ≈ 10.3” — helpful to also give this number in radians explicitly once (β = 5.97×10^−3 rad) beside the degree value to avoid unit conversion errors by readers.
Required fix: Add “(βobs = 5.97×10−3 rad)” once.

P1B-n3
Section: General
Problem: A few long parenthetical clauses and repository-process notes (e.g., “Column-permutation warning” on p. 18) distract from the scientific narrative.
Required fix: Consider moving such process notes to a short “Reproducibility notes” appendix or the repository docs, leaving only essential items in the paper.

Numerical/dimensional spot-checks (passed)
- 309,189 frozen samples = 176,240 + 132,949 (p. 3) — correct.
- H0 tension: (73.04 − 67.68)/sqrt(1.06^2 + 1.04^2) = 3.61σ — consistent with “~3.6σ.”
- σpix from ΔP = 10 μK·arcmin at Nside=512: Ωpix ≈ 47.21 arcmin² ⇒ σpix ≈ 1.455 μK — correct.
- EB template normalization: CEB ≈ 0.5 sin(4β) (CEE − CBB). The code/template uses CEE only and discusses the −CBB omission; consistent with attribution of part of the bias.
- Multiplicative under-recovery: 0.238/0.27 = 0.881; 0.302/0.342 = 0.883 (~12% under) — correct.
- SE of mean at fsky=0.32 with σβ=0.046°, N=500 ⇒ 0.046/√500=0.0021° — consistent with ±0.002°.
- Inverse-variance weighting reducing bias from 0.032° to 0.006° (~81%) — correct.
- w-pivot math (Table II): ap ≈ 0.790, zp ≈ 0.27, and σwpivot ≈ 0.019 — correct from supplied covariances.
- Inverse-variance combination of Planck NPIPE and ACT DR6 β (Eq. 5): 0.241° ± 0.061°, 3.93σ — correct; properly flagged as optimistic upper bound ignoring correlations.
- Birefringence formula (Eq. 4): α/(4π) ≈ 5.81×10^−4; with Caγ=8 and Δφ/fa=1.06 ⇒ β ≈ 0.282° — correct.
- ρcrit,0 ≈ 3.7×10^−11 eV^4 — correct.
- Mass prior in eV and relation to H0: log10 ma/eV ∈ [−35, −30] ⇒ m/H0 ≈ [7×10^−3, 7×10^2] — correct.

Length
At 22 pages, the paper is dense but focused on three concrete verifications. Provided the essential/major fixes are addressed, the length is acceptable for PRD-Methods; otherwise consider moving some repository-process content to the Supplement/Appendices or the online repository to streamline the narrative.

## Summary recommendation
MAJOR REVISIONS

Justification: The core methodology is sound and carefully caveated, and the numerical checks largely pass. However, PRD publication requires (i) stable, citable archival DOIs for all artifacts; (ii) stronger guardrails (or relocation to an appendix) for the overlap-uncorrected DES-SN5YR×Pantheon+ w0wa chain; and (iii) minimal additional robustness/stress tests for the NaMaster validation (beam mismatch and ℓ-range). Several smaller clarifications and one arithmetic cleanup are also needed. After these are addressed, the paper would meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER FRESH-EYES AUDIT

P1B-M7
Section: Table I note (p. 5)
Problem: Misstated “0.01σ” agreement. The text claims the full-tension S8 = 0.814 ± 0.008 agrees with the naive two-Gaussian combination 0.814 ± 0.009 “at the 0.01σ level.” The means are identical; the only difference is the quoted width (0.008 vs 0.009). A 0.001 change in σ relative to 0.009 corresponds to ≈0.11σ, not 0.01σ, if one insists on expressing as a fraction of the larger σ.
Required fix: Replace “0.01σ level” with a neutral phrasing such as “numerically identical mean and a 0.001 absolute difference in the quoted width (0.008 vs 0.009).” If you retain a σ phrasing, use ≈0.1σ, not 0.01σ.

P1B-M8
Section: Sec. IV, bias attribution (pp. 10–11)
Problem: Inconsistent attribution of the NaMaster bias source. Early text attributes the −0.032° bias at βinj = 0.27° to “the unweighted template fit plus the −CBB template mismatch.” Later, you report that adding the −CBB term to the fit template produces no further shift (β̂ remains 0.251° when using a lensed-BB injection), and that the improvement to −0.019° arises from changing the injected BB shape, not from carrying CBB in the template. These statements leave the reader uncertain whether the template omission or the BB realization shape is the operative effect.
Required fix: Reconcile and state a single, consistent attribution. For example: “The dominant bias driver is the unweighted estimator; a secondary contribution reflects the assumed BB realization (proxy 0.05 CEE vs lensed-ΛCDM). Including −CBB in the fit template does not materially change β̂ because lensed BB is negligible compared to EE for our settings.” Adjust earlier wording that implies a direct “−CBB template mismatch” cause.

P1B-m8
Section: Fig. 1 caption vs. footnote 1 (pp. 8 and 4)
Problem: Sample-count presentation is confusing. The caption lists 119,617 post-burn-in samples (getdist-thinned), while footnote 1 gives 123,129–123,368 post–30% burn-in counts (pre-thinning), then explains thinning/truncation. As written, a reader may think these are inconsistencies rather than different counting conventions.
Required fix: Add one clarifying clause in the Fig. 1 caption: “119,617 post–30%–burn-in samples after GetDist thinning (pre-thinning post–30%–burn-in count ≈123k; see footnote 1).” This makes clear the two numbers refer to different stages.

P1B-m9
Section: Sec. VI, Ωa definition (pp. 16–17)
Problem: Eq. (9) is written for the oscillatory regime, but the text later handles the “frozen” case (zosc ≤ 0) by prose only. For completeness and to avoid ambiguity, this piecewise definition should be explicit.
Required fix: Add an inline piecewise definition or a sentence immediately below Eq. (9): “For zosc ≤ 0 (field still frozen), we set Ωa = V(θi)/ρcrit,0 (no (1+zosc)−3 dilution).”

P1B-m10
Section: Sec. IV, bins above band limit (p. 11)
Problem: The statement “restricting the fit to bins with ℓ ≤ 1024 changes nothing (0.238°)” is correct because CEE,tmpl = 0 above ℓmax and those terms drop out of the derivative. This relies on the unweighted objective’s derivative argument (not obvious to all readers).
Required fix: Add one clarifying clause: “because bins with CEE,tmpl = 0 do not enter ∂χ2/∂β, they do not affect the minimizer even though they add a constant to χ2.”

P1B-m11
Section: Throughout Sec. IV and Abstract
Problem: Occasional phrasing “pipeline bias floor” remains (even outside places flagged in P1B-m1). Given the limited stress tests, “floor” still overstates generality.
Required fix: Replace residual instances with “observed bias under our unweighted, no-beam configuration,” to avoid implying a bound on real-sky systematics.

P1B-n4
Section: Sec. III, strong-coupling scale footnote 2 (p. 4)
Problem: Heuristic scale Λstrong ∼ MPl/√γBI is cited parenthetically. Because γBI is dimensionless, the scaling is dimensionally fine, but the actual dependence and numerical prefactors are model-dependent.
Required fix: Add a precise citation (beyond [11]) or soften to: “a heuristic EFT-validity estimate, Λstrong ∼ O(MPl/√|γBI|), model dependent; see [11] for derivation context.”

P1B-n5
Section: Abstract (p. 1)
Problem: Wording “not directly comparable to each other’s published sky significances” is grammatically odd and slightly unclear.
Required fix: Change to “not directly comparable to published sky significances” (drop “each other’s”).

Explanation
These issues were not covered in my initial review and emerged from a second-pass audit focused on arithmetic precision, consistency of attributions, and presentation clarity. They are mostly localized fixes and do not alter the scientific conclusions, but they will improve rigor and readability.