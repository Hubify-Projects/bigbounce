# P1B RA-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=f2838e5b pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5576 chars)
**Wall time**: 532.4s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model” (22 pages)

Overall scope and contribution
The manuscript presents three technical verifications: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy (Cobaya) on Planck/BAO/SN combinations, (ii) a NaMaster pseudo-Cℓ Monte Carlo validation of an EB-based birefringence angle estimator on synthetic skies, and (iii) a consistency check of the observed CMB isotropic cosmic-birefringence angle with a spectator ALP (fa ~ MPl) model, using a Gaussian summary likelihood for the Eskilt–Komatsu WMAP+Planck constraint.

The paper is careful in scoping: it does not claim evidence for torsion or bounce cosmology, avoids Bayes factors, and repeatedly flags that some widths are overlap-narrowed (DES-SN5YR × Pantheon+). The numerical work is largely traceable. However, several issues require significant revision before the work meets PRD methodological and presentation standards.

Findings

ESSENTIAL

P1B-E1 (Sec. III, pp. 3–7; Abstract p. 1; Conclusions p. 17): Mixed-release Planck pairing used in the primary ΔNeff chains without a complete quantitative robustness table
Problem: The primary frozen chains pair Planck PR4/NPIPE high-ℓ CamSpec with Planck 2018 low-ℓ TT/EE + 2018 lensing, and a verification rerun substitutes PR4-consistent low-ℓ/lensing. The text reports only ΔNeff agreement at 0.04σ; H0, σ8, S8, Ωm are said to agree “within <0.1σ” only for one rerun, in prose.
Required fix: Provide a compact side-by-side table (means ±1σ) for all headline parameters (ΔNeff, H0, σ8, S8, Ωm, τ, ns) comparing the mixed PR4+2018 pairing to the PR4-consistent pairing, with identical priors and sampling settings. This quantitative release-pairing robustness table must appear in the main text.

P1B-E2 (Sec. IV, pp. 9–12): Primary EB estimator knowingly biased; bias not minimized in the canonical pipeline
Problem: The canonical estimator is an unweighted χ² template fit, which the robustness battery shows is the dominant source of a ≃12% multiplicative under-recovery (bias −0.032° at βinj=0.27°; −0.040° at 0.342°). An inverse-variance-weighted fit removes ≈80% of the bias (to −0.006°), yet the paper “adopts” the unweighted version as canonical to match public scripts.
Required fix: For a methodology paper, the canonical pipeline should be the statistically sound choice. Either (a) promote the inverse-variance-weighted estimator to the mainline pipeline and carry forward its residual bias and uncertainty, or (b) justify quantitatively why matching historical, non-optimal scripts outweighs bias minimization (include the exact impact on β recovery and uncertainty), and present both estimators’ bias and variance in a comparative table.

P1B-E3 (Abstract p. 1; Sec. VI pp. 13–17): Bibliographic inconsistency for SH0ES “H0.riess2020Mb” and “Riess+2020” while citing the 2022 SH0ES result
Problem: The text repeatedly labels the SH0ES likelihood “H0.riess2020Mb” and states “Riess+2020” for MB, but references and numbers correspond to Riess et al. 2022 (ApJL 934, L7; H0=73.04±1.04 km s−1 Mpc−1; MB=−19.253±0.027 mag). This confuses provenance of a load-bearing likelihood.
Required fix: Correct all year labels and likelihood names to the actual SH0ES release used, and align citation [9] with the in-text labels. If a 2020 MB anchor is actually used in YAML, cite and quote its numbers; otherwise, change all “2020” labels to 2022 and rename the likelihood accordingly.

P1B-E4 (Abstract p. 1; Sec. IV pp. 8–12; Eq. (5) p. 14): Sigma values from different null procedures/data combinations juxtaposed without explicit “not directly comparable” every time
Problem: Multiple places juxtapose 2.7–2.9σ (Planck/ACT DR6), 3.6σ (WMAP+Planck PR3), and the internal 3.9σ “naive upper bound” (zero-correlation assumption). Although caveats appear in some paragraphs, not all juxtapositions explicitly state non-comparability of the significances.
Required fix: At every juxtaposition of 2.7–2.9σ vs 3.6σ vs 3.9σ, add an explicit “not directly comparable” clause stating that these come from different datasets and covariance treatments. In the abstract and Sec. IV, append one clause making this explicit.

MAJOR

P1B-M1 (Sec. IV, pp. 9–11; Fig. 3 caption p. 9): Bins above ℓmax=1024 included in χ² sum; justification relies on “zero template weight” only
Problem: The χ² sum extends to ℓ=1536 for Nside=512. The manuscript asserts bins above ℓmax carry zero template weight and “change nothing,” but the unweighted χ² adds noise-only bins that could, in principle, influence numerical minimization because EB_meas can be non-zero and coupling/pixelization subtleties may leak β-dependence at high ℓ.
Required fix: Show explicitly that the best-fit β grid profile is unchanged (to within 0.0005°) when restricting the fit to ℓ≤1024 by plotting χ²(β) with and without the high-ℓ bins. Alternatively, remove high-ℓ bins from the fit in the canonical pipeline.

P1B-M2 (Sec. VI, pp. 13–17; Table IV p. 18): Fixed-Caγ=8 ALP posterior: missing credible interval on m/H0 and explicit posterior for spectator-safe subset
Problem: The text quotes median m≃36 H0 for the fixed-coupling run but does not provide 16–84% credible intervals for m/H0 in that configuration. Table IV shows percentiles for the continuous-prior run but not the fixed-coupling one emphasized in the abstract.
Required fix: Report 16–84% credible intervals for m/H0 in the fixed-Caγ=8 chain (full and Ωa<0.01 subset). Include a short table or add a row to Table IV.

P1B-M3 (Sec. VI, pp. 15–16): Prior dependence and spectator fraction
Problem: The Ωa fractions (44% for Ωa<0.1; 13% for Ωa<0.01) are prior dependent. While this is stated, the main text should quantify how these fractions change under the (arguably better-motivated) cosθi-flat prior (you mention 0.068% mass for θi≤0.1 in a rerun but do not quote the Ωa subset fractions under the cosθ prior).
Required fix: Provide the Ωa<0.1 and Ωa<0.01 posterior-mass fractions under the cosθi-flat prior for the continuous-prior configuration, alongside the flat-θi values, to make the prior dependence explicit.

P1B-M4 (Sec. VI, p. 14; Eq. (4)): Birefringence normalization conventions
Problem: The text states gaγ = Caγ αEM/(2π fa) and β = (gaγ/2) Δφ. This is fine, but many readers use alternative normalizations (e.g., β = (gaγ/2) Δa with a ≡ φ/fa). The manuscript already uses Δφ/fa explicitly; however, the mapping to the commonly used a-normalization is not stated.
Required fix: Add a one-line note explicitly relating your expression to the “axion field a” normalization, i.e., β = (αEM/(4π)) Caγ Δa, with a ≡ φ/fa, to avoid confusion.

P1B-M5 (Sec. V, p. 12; Sec. III, pp. 3–7): Nested-sampling/evidence deferred; model-comparison statement still implied by wording in places
Problem: Several places note that ΛCDM is “unsampled” or that posterior centers are displaced; even with caveats, some sentences risk being read as weak preference claims.
Required fix: Add an explicit single-sentence disclaimer at the end of Sec. V C that no model-preference inference (AIC/BIC/ln B) can be drawn from the presented chains, and that the overlap-uncorrected widths invalidate any tail-distance-based exclusion statements.

P1B-M6 (Data and Code Availability, pp. 18–20): “DOI assignment is pending” for all artifacts
Problem: PRD requires stable, citable long-term archives at acceptance. “Pending DOI” and reliance on a moving repository commit hash are inadequate for publication.
Required fix: Before acceptance, deposit the frozen chains, NaMaster artifacts, and ALP chains in a DOI-minted archive (Zenodo or equivalent), and replace all “pending” placeholders with the final DOIs in the manuscript.

P1B-M7 (Throughout; e.g., pp. 3–7, 12, 18–20): Internal versioning and path traces in the main text
Problem: The manuscript includes internal repository commit hashes, pathnames (e.g., reproducibility/.../results/*.json), and “pod” run identifiers within the main text, which is not PRD style and distracts from the scientific content.
Required fix: Move all operational pathnames, run IDs, and commit hashes to a single consolidated Data/Code Appendix or to a separate online Supplementary Material. Keep the main text citation to a single landing page/DOI.

P1B-M8 (Sec. IV, pp. 9–11): Beam/pixel-window treatment
Problem: The test uses no beam and assumes cancellation in the β estimate. While acceptable for a synthetic validation, the absence of even a simple beam-mismatch stress test is a limitation.
Required fix: Add a short quantitative statement (even one line) clarifying that a beam-mismatch test is deferred and noting the expected magnitude of the effect (e.g., from a pilot with ±10% FWHM difference, if available) or explicitly state that this is a limitation of the current validation.

P1B-M9 (Sec. II, p. 3; Abstract p. 1): “~3.6σ” H0 tension wording
Problem: The text states “∼3.6σ tension with SH0ES H0 = 73.04 ± 1.04,” without tying that number to a specific one of the reported H0 posteriors. Using Planck+BAO+SN (67.78±1.09) gives 3.49σ; using full-tension (67.68±1.06) gives 3.61σ.
Required fix: Specify which combination the “∼3.6σ” refers to or give both values explicitly (3.49σ for Planck+BAO+SN; 3.61σ for full-tension).

MINOR

P1B-N1 (Sec. II, p. 3): Definition of (ω/H)0
Problem: (ω/H)0 is invoked as “angular momentum transfer” but not explicitly defined here. While scope says it is fixed to zero and discussed in Paper I(a), a stand-alone reader would benefit from a parenthetical definition.
Required fix: Add a one-clause definition (e.g., “(ω/H)0, a phenomenological angular-momentum-transfer parameter discussed in Paper I(a), is fixed to zero here”).

P1B-N2 (Fig. 2 caption, p. 8): Labeling
Problem: The legend line “SM ( Neff = 0)” is likely meant to indicate ΔNeff = 0. Slightly unclear.
Required fix: Change the legend to “SM (ΔNeff = 0)” for clarity.

P1B-N3 (Sec. III footnote 2, p. 4): Typesetting glitch
Problem: “M−2 Pl -suppressed2:” shows a floating “2” footnote marker fused with the hyphenation.
Required fix: Fix typesetting so the footnote marker does not appear as part of the unit/phrase.

P1B-N4 (Acknowledgments, p. 18): AI assistant acknowledgment
Problem: While transparent, PRD has no standard for AI acknowledgment lines; some editors may prefer this to appear in a footnote or be removed.
Required fix: Move the “use of Claude (Anthropic)” line to a footnote or remove at editor’s discretion.

NIT

P1B-n1 (Sec. III, p. 6): Small arithmetic rounding
Problem: “−18.415” vs recomputed “−18.416” in MB–H0 offset; immaterial.
Required fix: None required, but you may round consistently to three decimals.

P1B-n2 (Length): 22 pages for a technical verification companion
Problem: The main scientific points could be conveyed more concisely; several pages are consumed by pathnames and operational notes.
Required fix: Consider moving operational reproducibility detail to an Appendix/Supplement and target a ~14–16 page main text.

Arithmetic and dimensionality spot-checks (passed)
- ΔNeff one-sided 95% ULs: recomputed 0.318 and 0.389; consistent with 0.31 and 0.40 quoted.
- S8 tension: (0.827−0.776)/sqrt(0.010²+0.017²) = 2.58σ; matches quoted 2.6σ.
- H0 tension: 3.61σ (full-tension); 3.49σ (Planck+BAO+SN). Please clarify as in P1B-M9.
- Pivot algebra: ap=0.790, σ(wpivot)=0.0193, wpivot=-0.952; all consistent.
- NaMaster noise conversion: Ωpix=47.21 arcmin² at Nside=512; σpix=1.455 μK; correct.
- Multiplicative under-recovery factors: 0.238/0.27=0.881; 0.302/0.342=0.883; consistent.
- SE of mean at fsky=0.32: 0.046°/√500 = 0.00206°; matches.
- ALP birefringence normalization: α/(4π)=5.81×10−4; ×8×1.06=4.93×10−3 rad = 0.282°; correct.
- ρcrit,0 ≈ 3.7×10−11 eV⁴ for H0=67.7 km/s/Mpc; correct.

Figures and tables
- Table I numbers match text. Provide the PR4-consistent rerun table as per P1B-E1.
- Table II flags overlap-narrowed widths correctly; no σ-distance claimed.
- Fig. 3 caption correctly distinguishes pipeline SNR from sky significance, but add “not directly comparable” near any mention of 2.7–2.9σ/3.6σ (P1B-E4).

## Summary recommendation
MAJOR REVISIONS

The numerical work is careful and most arithmetic checks out. However, the paper needs (i) a proper quantitative robustness table for the mixed PR4+2018 Planck pairing versus PR4-consistent low-ℓ/lensing, (ii) elevation of the statistically sound inverse-variance-weighted EB estimator (or a compelling quantitative justification for keeping the biased unweighted estimator as canonical), (iii) resolution of the SH0ES year/likelihood labeling inconsistency, (iv) explicit non-comparability flags for all juxtaposed σ values, and (v) finalized DOI-stable data/code archives. In addition, substantial operational detail should be moved to an appendix/supplement to meet PRD style. With these addressed, the paper would be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1B-E5 (Sec. VI, p. 17, LiteBIRD separability line): Typo in variance term leads to a numerically wrong denominator if read literally
- Issue: The text states |0.342−0.27|/sqrt(0.032+0.094^2) ≈ 0.7σ. The “0.032” is almost certainly intended to be 0.03^2. As written, 0.032 would give ≈0.36σ, not 0.7σ.
- Required fix: Replace “0.032” with “0.03^2” (or write out 0.0009 explicitly) and keep the ≈0.7σ result.

MAJOR

P1B-M10 (Table II, “Age [Gyr] 13.763 ± 0.019”): Reported age uncertainty appears unrealistically small for the stated parameter uncertainties
- Issue: With H0 = 67.185 ± 0.455 km/s/Mpc (≈0.68% fractional) and additional dependence on Ωm and w0, wa, one expects a propagated age error closer to ≳0.07–0.10 Gyr, not 0.019 Gyr (19 Myr). This suggests a units/reporting error, fixed-parameter assumption, or a GetDist post-processing artifact.
- Required fix: Re-derive Age uncertainty from the full chain covariance (or provide an explicit propagation) and explain why the result is as small as 0.019 Gyr. If this is a reporting/configuration artifact, correct the table and text.

P1B-M11 (Sec. VI, first paragraph; fn. 6; Table IV): Inconsistent and under-justified “≳100× fine-tuning” claim vs. 25× tuning and quoted posterior fractions
- Issue: The main text claims “≳100× fine-tuning of the misalignment initial condition under a cosθi-flat prior (equivalently ∼25× relative to θi ≈ 0.5 midpoint).” Only the 25× figure is shown (Ωa ∝ θ^2 ⇒ (0.5/0.1)^2 = 25). The “≳100×” is not derived anywhere. Later, a cosθi prior run reports θi ≤ 0.1 mass fraction of 0.068%, but this is not connected to a precise “×” tuning metric.
- Required fix: Define precisely what “× fine-tuning” quantifies (e.g., ratio of posterior mass within θi ≤ 0.1 to a reference fraction; or ratio of energy-density suppression). Provide the quantitative derivation for “≳100×” using your cosθi-prior run and make it consistent with the 25× statement. Otherwise, remove “≳100×” and retain only the demonstrated 25× energy-density tuning.

P1B-M12 (Sec. VI, Ωa computation, Table IV): Use of small-angle quadratic approximation for Ωa across subsets that include θi up to 0.70 not explicitly quantified
- Issue: You say the leading anharmonic correction is O(θ^2/12), “≲8% at θ≈1 and ≲1%” in the Ωa ≤ 0.01 subset (θ≲0.3). But for the Ωa<0.1 subset (16–84% θi = 0.41–0.70), the correction is up to ≈4%. This is never explicitly stated alongside the 44% mass in that subset.
- Required fix: Add a one-line quantitative bound (e.g., “the Ωa<0.1 subset includes θi up to 0.70, implying ≤4% anharmonic correction in Ωa; our subset fractions are insensitive at this level”) or recompute Ωa with an anharmonic correction to verify stability.

P1B-M13 (Table I, convergence line vs. text): Boundary inequality inconsistency for Rhat
- Issue: The table lists “Worst Rˆ−1 = 0.003” for Planck+BAO+SN, while the footnote/text states “all … satisfy Rˆ − 1 < 3 × 10−3.” The listed worst value equals 3×10−3, not strictly less.
- Required fix: Change the inequality to “≤ 3 × 10−3” or quote more digits for the worst Rˆ−1 to resolve the boundary case.

P1B-M14 (Sec. IV, fsky definitions): Ambiguity in fsky after apodization
- Issue: The text quotes fsky ≈ 0.85 for a |b|>5° “Planck-like” mask with 2° apodization. Whether fsky refers to the raw binary footprint, the apodized-weight effective sky fraction (e.g., ⟨W^2⟩), or a simple average of the apodized mask is not stated. This affects direct comparability to published fsky.
- Required fix: State explicitly how fsky is computed after apodization (binary area, ⟨W⟩, or ⟨W^2⟩). If you intend binary sky fraction before apodization, say so.

MINOR

P1B-N5 (Sec. VI, Eq. 5; arithmetic): Naive inverse-variance β mean is ≈0.243°, not 0.241°, using quoted inputs
- Issue: Combining 0.300±0.110 and 0.215±0.074 gives β ≈ 0.2433°, σ ≈ 0.0613°. The manuscript quotes 0.241±0.061°. The 0.002° difference is trivial scientifically but should be numerically consistent.
- Suggested fix: Either align to 0.243° or note that slightly different rounding (or internal values) were used.

P1B-N6 (Sec. III, “MB–H0 joint-posterior offset check”): Minor arithmetic mismatch for the Riess anchor constant
- Issue: −19.253 − 5 log10(0.7304) = −18.570 to −18.5698 depending on rounding, not −18.571 as printed. Tiny but present.
- Suggested fix: Round consistently to 3 decimals (−18.570) to match the precision used elsewhere.

P1B-N7 (Sec. IV): Absolute “bias floor” vs. multiplicative bias
- Issue: You carry forward a 0.040° absolute bias floor. Because your dominant effect is multiplicative under-recovery (~12%), it may be clearer to report both a multiplicative bias (≈0.88) and the absolute floor for the injection range tested. This is a presentation suggestion, not a requirement.

P1B-N8 (Fig. 2 caption): Label clarity
- Issue: The legend entry “SM ( Neff = 0)” should read “SM (ΔNeff = 0)” for clarity (distinct from Neff = 3.046).
- Suggested fix: Update the label accordingly.

NO DUPLICATES
- I have not repeated any items already present in the initial review (e.g., Planck pairing robustness table, estimator choice and bias, SH0ES year/likelihood labeling, σ comparability flags, high-ℓ bin handling, missing Caγ=8 m/H0 intervals, prior-dependence of Ωa fractions, normalization cross-walk, explicit “no model preference” disclaimer, DOI minting, operational pathnames, beam-mismatch stress test, H0-tension specificity, (ω/H)0 parenthetical, footnote typography, AI acknowledgment placement, etc.).