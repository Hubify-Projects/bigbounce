# P4 R53 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R53_P4/chirality_catalog_paper.pdf` md5=b716a574 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9420 chars)
**Wall time**: 370.0s

---

Referee report for “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of this review
- Focus: statistical and methodological rigor, estimator definitions, significance accounting, internal arithmetic consistency, dimensional checks, and reproducibility surfaces.
- I audited the abstract and conclusions line-by-line against the body, recomputed ratios, checked null sizes vs quoted precision, and examined figures/tables for consistency.

Overall assessment
- The paper proposes a large chirality catalog and a care-with-systematics analysis. The statistical caution regarding incomparable σ-conventions is commendably frequent.
- However, there are critical inconsistencies in the harmonic-channel significances for the canonical mask, pervasive in-text repository path artifacts that are not PRD style, several imprecise or under-justified choices (e.g., θ-uniform axis draws, multiple null definitions used interchangeably in places), and reliance on low NMC in some headline diagnostics.
- The manuscript must be tightened: unify estimator definitions, reconcile discrepant σ-values for what is claimed to be the “same” configuration, and move internal provenance/file-path chatter to a proper data appendix or external repository.

Findings

ESSENTIAL

P4-E1 — Sec. IV C–D; Table III; p. 9–12, 15
Problem: Canonical-mask MASTER ℓ=1 significance inconsistency (+3.64σ vs +7.93σ). The text states “+3.64σ (500-MC direct run on the canonical unapodized mask),” while Table III reports for “canonical, unapod.” with 10^4 permutations z = +7.93 at ℓ=1. The caption attempts to deflect by stating they are “not mutually comparable,” but for the “canonical, unapodized” configuration the mask, field, subtraction, and band definition appear identical. A change in NMC from 500 to 10^4 should not induce a factor-of-two z shift for a moment-z unless the estimator or field normalization changed.
Required fix: Precisely specify, side-by-side, the full configuration for the +3.64σ and +7.93σ runs (mask, apodization, field definition, monopole subtraction, binning, coupling matrix, weighting, null generation). Demonstrate with a single script that varying only NMC leaves z stable within sampling error. If they are different estimators (e.g., pseudo-Cℓ single-mode without decoupling vs decoupled, or different field normalization), relabel everywhere so the two numbers are never presented as the same “canonical ℓ=1” statistic; report one canonical value consistently and relegate the other to an explicitly different-configuration appendix. Remove language that suggests the difference is due to null-run size alone.

P4-E2 — Global; multiple pages (pp. 1, 9–15)
Problem: Multiple σ-values from distinct nulls and configurations are placed in proximity; although the manuscript often warns they are not directly comparable, there are still instances where direct juxtaposition can mislead (e.g., Sec. VII.c lists +3.64σ canonical, +7.93σ canonical row, +7.28σ apodized footprint all in one paragraph). For PRD standards, every such juxtaposition must carry an explicit local caveat and, ideally, a compact table keyed to a single canonical definition to prevent reader misinterpretation.
Required fix: Wherever more than one σ is quoted in a paragraph, add an explicit parenthetical “not directly comparable; see Table X” pointer, and in that table provide a clear, one-line descriptor (field, mask, subtraction, weight, null). Preferentially choose one diagnostic σ per channel to headline; move the rest to an appendix.

P4-E3 — Global (many locations; e.g., p. 3, 5–8, 9–13, 16–22)
Problem: Pervasive inclusion of internal repository file paths, artifact names, seeds, and local filenames in the main text (e.g., “pipelines/p2_chirality/outputs/…”, “artifact c12 r24conf local batch.json”, “seed 42” lines). These are internal bookkeeping surfaces and not acceptable in the PRD body. They also include ad hoc local JSON names without a persistent DOI.
Required fix: Remove all in-text internal path references from the body and figures. Consolidate provenance pointers into a Reproducibility Appendix and/or a companion data release note. Replace every internal path in-body with a stable DOI/Zenodo link or a single repository URL + commit hash with a short identifier. Keep RNG seeds in that appendix only.

P4-E4 — Data Availability; p. 22
Problem: No persistent DOI for the released catalog/model at submission time. PRD reproducibility policy expects a citable, frozen snapshot. The link text to the HF dataset also shows errant spaces (“galaxy- chirality- catalog”).
Required fix: Deposit the exact release (catalog, model weights, scripts) to a persistent archive (Zenodo or similar), cite the DOI in the paper, and fix/verify all URLs (no line breaks/spaces). Pin the code to a permanent tag and record the tag and commit hash in the Data Availability section.

P4-E5 — Abstract and Sec. IV C; p. 1, 7–8
Problem: The abstract claims an “equivariant-catalog high-confidence dipole fit ... gives +0.41σ (moment-z against the isotropic (pixel-)permutation null; empirical-rank p = 0.31, 10^4 isotropic-null realizations).” In Sec. IV C the high-confidence primary fit is described with NMC = 10,000; robustness checks use 2,000 in some cells and 10,000 in others. The null size is stated; however, the quoted +0.41σ moment-z requires that the null mean and width are computed with sufficient precision. With NMC=10,000 and a heavy-tailed null, the sampling error on σnull can bias a sub-σ moment-z. The paper also mixes isotropic pixel permutation and per-galaxy label shuffles; both are used for the same estimator.
Required fix: For the single headline +0.41σ, lock the null definition and NMC; provide the numeric null mean and standard deviation used, and the sampling error on z due to finite NMC. State explicitly which null is used for the primary headline (pick one: pixel-permutation or label-shuffle), and move the other to a robustness footnote. If heavy tails are material, report the rank-p alone as the primary significance for that estimator.

MAJOR

P4-M1 — Sec. IV B; p. 5–6
Problem: “2.98× asymmetry-suppression factor from raw +1.576% to equivariant −0.529%” uses magnitudes of asymmetries but ignores the sign flip. As written, “suppression” suggests magnitude-only; the sign flip underlines different bias structures between Catalog A and C.
Required fix: Rephrase to “magnitude reduced by a factor 2.98 and sign-reversed.”

P4-M2 — Sec. IV C; p. 7–9
Problem: Injection convention and mapping between injected A and recovered Ap are described in multiple places with slightly different centering (around 0.5 vs around pglobalCW). The sentence “for a pure dipole the Ap-dipole amplitude equals the full-amplitude A” is only true with monopole marginalization and when Ap is built around 0.5.
Required fix: State clearly: (i) for estimator scoring you fit a monopole and dipole, so centering does not bias the dipole amplitude; (ii) the equality of Ap-dipole amplitude and injected A holds because the monopole absorbs p0. Add a one-line derivation or move to a short appendix with the linear fit model.

P4-M3 — Sec. VI A; p. 13–14
Problem: Use of θ-uniform axis draws for injection (θ ∼ U(0, π), ϕ ∼ U(0, 2π)) is not area-uniform. A later spot check claims negligible difference, but the main sweep (and quoted A50/A95) are based on the θ-uniform convention.
Required fix: Re-run the main injection-recovery sweep with area-uniform axes (cos θ ∼ U[−1,1]) and report the A50/A95 from that. If identical within MC error, state the quantitative agreement and keep the area-uniform result as canonical.

P4-M4 — Sec. VII.a (Fig. 9 and Table VI); p. 15
Problem: Harmonic-channel completeness claims (e.g., P(≥3σ) ≥ 0.999 at Ap ≥ 0.75%) depend on the channel’s own null. The observed data point is quoted as “+7.28σ” in the body, while the figure says “obs. σ ≈ 7.21 within that null.” This is confusing.
Required fix: In the caption and text, explicitly state that the plotted observed σ is the value computed within the injection sweep’s background null and differs slightly from the paper-canonical 500-MC null. Preferably, recompute the observed σ within the same background null used for the sweep and report only that one value in the figure and body for consistency.

P4-M5 — Sec. II.B; p. 3
Problem: 66.5% of training labels are CE-ResNet pseudo-labels, so survey-scale patterns can in principle leak into this model’s outputs. The paper acknowledges this but then relies on label-shuffle and pixel-permutation nulls that randomize this model’s outputs, not the CE-ResNet structure.
Required fix: Provide a direct cross-spectral test between your Ap field and the CE-ResNet field (or a proxy), or at minimum report the cross-correlation between the two catalog maps at low ℓ to bound inherited structure. If not feasible, downscope the independence claim in the Introduction and emphasize that cosmological interpretation strictly relies on the real-space primary estimator with monopole marginalization.

P4-M6 — Sec. III.B; p. 4–5
Problem: The “Declared analysis hierarchy” is good, but the primary cosmological estimator is described twice with slightly different Nspiral counts and fsky values (full vs HC subsets). This contributes to confusion about which selection underlies which headline.
Required fix: Add a one-line table keyed to the two primaries, specifying sample size, mask, fsky, estimator, and null. All headline claims should then point to a row in that table.

P4-M7 — Appendix A.c; p. 16–17
Problem: The effective sky fraction f_eff,sky definitions are given, but the text mixes “mask pixel fraction” and “effective sky fraction” in places without a quick reminder of units. Some rows list both fsky and f_eff,sky across different masks/weights; it is easy to confuse them.
Required fix: Add explicit column labels “geometric fsky” vs “effective f_eff,sky” in Table VII; ensure all references to these quantities elsewhere use the same terms.

P4-M8 — Data Availability; p. 22
Problem: The catalog retains rows flagged by a QC “flip identity violator” and instructs users to filter if they want to replicate the baseline. For PRD, the default public artifact should reproduce the paper baseline without requiring user filtering.
Required fix: Provide a baseline-ready release file (or a view) that exactly matches the analysis sample used for the primary results, with a clear filename and DOI. Keep the full catalog with flags as a separate artifact.

MINOR

P4-m1 — Sec. IV B; p. 6
Problem: “An equal-area partition (8 declination bands of equal in-mask pixel count …) gives … max |z| = 2.9 vs. the global rate.” No numerical per-slab values are shown, and the referenced artifact is internal.
Required fix: Add a compact table (or a supplement) with the per-slab fCW and z, or provide a public DOI to a CSV with those values.

P4-m2 — Sec. IV C; p. 8–9
Problem: Confidence-cut sweep reports z for several thresholds with different NMC sizes (“2000-permutation pixel nulls per cell”). Sub-σ precision is claimed in some cells with NMC=2000 but not accompanied by sampling errors on z.
Required fix: Append the sampling error on z for each cut (e.g., via bootstrap on the null variance or an analytic estimate) or switch to reporting rank-p only for these supporting cells.

P4-m3 — Sec. VI A; p. 13–14
Problem: The “true-amplitude” mapping g = 2a−1 assumes symmetric CW/CCW errors and no triage. The text admits asymmetry in Table IX and triage to not-spiral.
Required fix: Move the 1.88% “true” mapping into a clearly labeled back-of-the-envelope box; make the operative falsification bounds explicitly those measured in observed space.

P4-m4 — Sec. IV D; p. 10–12
Problem: Hemisphere statistic: NSIDEdir=8 grid (768 directions) vs the 10° grid (648 directions) are both used in different places. The paper states they’re not comparable, but the reader has to track this manually.
Required fix: Add the grid definition alongside each hemisphere-statistic number where it appears.

P4-m5 — Appendix B.d; p. 17–18
Problem: Test T5 (metadata leakage) uses linear Pearson with RA, a circular variable. The limitation is noted; however, a better standard test is available (circular-correlation or Yℓm regression).
Required fix: Promote the low-ℓ Yℓm regression result (already mentioned) into the main bias-hardening text and demote T5 to a minor check.

P4-m6 — Sec. VII.b; p. 15
Problem: “Matched-footprint Ganalyzer reanalysis remains required for a formal σ-level exclusion” is appropriate, but the text elsewhere occasionally leans toward exclusion phrasing.
Required fix: Ensure all such statements are consistently framed as amplitude-incompatibility under the present pipeline, not formal exclusion.

P4-m7 — References
Problem: Check the typography of a few bibliography entries (e.g., [27] shows “Mon. Not. R. Astron. Soc. 509, 3966 (2022)” which is correct, but ensure all DOIs/arXiv IDs correspond to the stated journals/years).
Required fix: Run a final bibliography consistency pass; fix any missing DOIs where standard.

NIT

P4-n1 — Typos and hyphenation; multiple pages
- Stray spaces in some links (“galaxy- chirality- catalog”).
- Occasional duplicated descriptors (e.g., “canonical unapodized” appears as both “canonical” and “unapodized” repeatedly; unify).
- Minor math typography: use consistent Ap vs A, and consistent ×10−6 formatting.

P4-n2 — Figure axis labeling; Figs. 4, 7
- Ensure axis labels explicitly indicate coordinate system and that color-bar units are stated once in the caption and once on the bar.

P4-n3 — Section headers
- Some parenthetical reminders in headers are long; consider moving as first sentence in section to improve navigation.

Abstract-last drift sweep
- The abstract is unusually careful with caveats and repeatedly states “diagnostic only” and “not directly comparable.” The main discrepancy is P4-E1: the canonical-mask σ-values (+3.64σ vs +7.93σ) — both appear already in the abstract’s qualifiers. This must be reconciled or the abstract adjusted to cite only one canonical value with its configuration.

Provenance surfaces
- Many in-text artifact references violate PRD style (P4-E3). Move them to a Reproducibility Appendix and cite a DOI snapshot.

Effect sizes
- For each σ headline, you generally provide amplitudes (e.g., Adip ≈ 4.4×10−3). Continue this practice consistently; where absent (some robustness cells), add the recovered amplitude.

Recommended page-length
- The paper is long (23 pages), largely because of in-text provenance not appropriate for the main body. After removing internal file-path chatter and consolidating estimator definitions, this can likely be reduced by 3–5 pages without loss of substance.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript has a solid methodological core and is unusually explicit about null conventions and systematics. However, a critical inconsistency remains in the canonical harmonic-channel σ-values that must be reconciled with precise, reproducible estimator definitions (ESSENTIAL). In addition, pervasive in-text internal file-path artifacts must be removed or moved to a reproducibility appendix with a persistent DOI, and several methodological clarifications and unifications are needed before this meets PRD standards. Once these are addressed and the primary claims are tied cleanly to a single, well-defined estimator/null with consistent numbers, the paper can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

Note: I only list NEW issues not covered in my initial report. Codes follow the same scheme [P4-E#, P4-M#, P4-m#, P4-n#].

ESSENTIAL

P4-E6 — Table III arithmetic: z values don’t match the displayed inputs
- Issue: Using the tabulated numbers in Table III, several moment-z values are arithmetically inconsistent.
  • Canonical, unapodized, ℓ=1: z should be (7.27−0.57)/0.84 = 7.98, but table prints +7.93.
  • Canonical, unapodized, ℓ∈[2,6]: z should be (1.42−0.56)/0.20 = 4.30, but table prints +4.20.
  • Apodized, Wp=Nall, ℓ∈[7,11]: z should be (3.12−1.92)/0.50 = 2.40, table prints +2.41 (this one is fine within rounding; listing for completeness).
- Why it matters: These are core diagnostics. If the displayed inputs are rounded, the resulting z should remain consistent within rounding. Here the discrepancies are bigger than simple rounding in at least the first two bullets.
- Required fix: Either (i) print z derived from the displayed numbers (rounded consistently), or (ii) add a note that z is computed from full-precision arrays and provide those exact values for Cdata, ⟨C⟩null, and σnull in a machine-readable supplement. Recompute and correct all inconsistent z values.

P4-E7 — Appendix A.c “decoupled C1” values are stale/inconsistent with Table III
- Issue: Appendix A.c states “monopole subtraction reduces decoupled C1 from 2.30×10−5 to 1.51×10−5 and increases σ from +1.85 to +3.64.” In Table III the canonical-unapodized decoupled ℓ=1 C1 is 7.27×10−6 (and the apodized-footprint ℓ=1 C1 is 24.74×10−6). The quoted 2.30×10−5 and 1.51×10−5 do not match either footprint shown in Table III.
- Required fix: Specify precisely which footprint/field those 2.30×10−5 → 1.51×10−5 numbers refer to, or update them to match the current configurations. If they are from an earlier estimator convention, mark them explicitly as such and reconcile with the tabled values.

P4-E8 — “∼12%” MASTER-decoupled monopole-only reproduction is not numerically demonstrated
- Issue: Sec. IV D claims the monopole-only decoupled null reproduces “∼12%” of the post-MASTER C1. No number is shown for the monopole-only decoupled null mean to substantiate 12%. The only visible null means are the label-shuffle rows in Table III, which imply ≈7.8% (1.93/24.74 for apodized; 0.57/7.27 for canonical).
- Required fix: Report the actual MASTER-decoupled monopole-only null mean(s) and the data/null ratio(s) for both footprints (canonical-unapodized and apodized). If 12% pertains to a different field normalization, spell that out and show the corresponding data/null numbers so the fraction is reproducible.

MAJOR

P4-M9 — Harmonic-channel significance: moment-z vs rank p are wildly inconsistent; headline the rank p
- Issue: For the apodized ℓ=1 row (Table III), z ≈ +7.31 while rank p = 6×10−4. A Gaussian would put z ≈ 3.25 for that p, indicating an extremely heavy-tailed null. Quoting z ≈ 7 as a “σ” headline in this channel can be misleading.
- Required fix: For heavy-tailed permutation nulls at low ℓ, lead with empirical rank p (and optionally a Gaussian-equivalent based on rank p) and demote moment-z to secondary. Add this policy explicitly where the +7.31/+7.28 values are discussed.

P4-M10 — Hemisphere look-elsewhere (LEE) p-value limited by NMC
- Issue: The LEE control uses N = 10,000 random-label max-statistic draws, yielding pLEE ≤ 10−4 (the minimum resolvable with that N). For a central headline that rejects the random-label null, resolving below 10−4 is often expected.
- Required fix: Increase the max-statistic NMC (e.g., ≥ 10^6) or provide a confidence interval/upper bound methodology (e.g., Clopper–Pearson on zero exceedances) to quantify the uncertainty on pLEE. State the exact one- or two-sided convention.

P4-M11 — Figure 8 caption vs body: pre-MASTER vs post-MASTER confusion
- Issue: Fig. 8 shows pre-MASTER pseudo-Cℓ with per-ℓ σ annotations. Nearby text discusses the post-MASTER canonical-mask residual +3.64σ. Although the caption mentions different estimators elsewhere, the figure itself does not stamp “pre-MASTER” prominently. This is easy to misread as the same statistic later cited in the body.
- Required fix: Stamp “pre-MASTER (no decoupling)” in the panel title and add a single-sentence caption line pointing to the distinct post-MASTER value and where it is quoted. In the body, one sentence should explicitly connect and contrast the two.

P4-M12 — Parity classification of the ℓ=1 observable needs a clear definition and justification
- Issue: Sec. VI.B states: “This ℓ=1 observable is parity-even (isotropy-breaking axial-vector), not a direct parity-violation test.” For a sky field that changes sign under mirror (chirality asymmetry), the multipole behavior under parity depends on whether the field is scalar or pseudo-scalar on S^2 and on how parity is defined for the observable. This is asserted, not shown.
- Required fix: Define the transformation of A( n̂ ) under parity and show how its spherical-harmonic coefficients transform. Justify precisely why ℓ=1 in this construction is parity-even and thus not a direct parity-violation test. Provide a citation or short derivation.

MINOR

P4-m8 — Table I row (vi) lacks the “pre-MASTER” qualifier
- Issue: Row (vi) “monopole+mask null … +1.69” is a pre-MASTER pseudo-Cℓ diagnostic per Sec. IV D and Table IV, but the row label does not say pre-MASTER.
- Required fix: Amend the row label to “pre-MASTER pseudo-Cℓ” to prevent conflation with the post-MASTER results.

P4-m9 — Table VII labeling inconsistency for apodized rows
- Issue: The preamble says binary-mask rows quote geometric fsky and weighted/apodized rows quote effective f_eff,sky. The “Canonical (binary, C2 2°)” row lists 0.482 without an explicit “effective” label, which can be misread as geometric fsky.
- Required fix: Add explicit column headers “geometric fsky” and “effective f_eff,sky” and place each value in the appropriate column. Ensure every apodized/weighted entry is in the f_eff,sky column.

P4-m10 — “Summed leg-induced ℓ=1 amplitude is ∼25%” needs an amplitude-space demonstration
- Issue: Appendix D.d quotes rℓ=1 correlations for leg proxies and then asserts their “summed” contribution is ∼25% of the observed amplitude. A correlation coefficient alone does not determine contribution to amplitude without explicit normalization and phase alignment.
- Required fix: Provide the actual template-fit amplitudes (or cross-power-derived amplitudes with uncertainties) and show how the ∼25% figure is computed in amplitude units, not correlations. If “summed” means quadrature or linear sum, specify.

P4-m11 — Two-point chirality correlation: claim of brick-boundary artifact lacks numbers/plot
- Issue: Appendix C.d states the −2.41σ at ≈0.5° “vanishes” to −0.03σ in a brick-interior subsample, but no figure/table is provided.
- Required fix: Include a small figure or a DOI to a CSV showing the correlation function with and without brick-boundary pixels, including uncertainties.

P4-m12 — Figure/number pairing: add the decoupled-monopole numbers that explain “σ rises while C1 falls”
- Issue: Appendix A.c explains that monopole subtraction lowers C1 but raises σ. The narrative would benefit from reporting the null mean/width before and after subtraction to make the explanation quantitative.
- Required fix: Add a two-line numeric summary (⟨C1⟩null, σnull) before/after subtraction for the cited configuration.

P4-m13 — Clarify footprint for the “2.30×10−5 → 1.51×10−5” numbers
- Issue: Closely related to P4-E7, but here as clarity: readers cannot tell whether those values correspond to the apodized footprint, the canonical mask, or an older setting.
- Required fix: Append “(apodized footprint)” or “(canonical mask, unapodized)” to the sentence, or remove the numbers if stale.

P4-m14 — Report rank p alongside σ for depth-stratified nulls cited in Appendix A.d
- Issue: For Wp=Nall/Nspiral, the depth-stratified σ values are given (+7.13/+9.06), but no rank-p is shown.
- Required fix: Add the corresponding rank p for those runs to maintain the paper’s practice of pairing z with rank p in heavy-tailed regimes.

P4-m15 — Make explicit why Nmap,weighted equals the total-galaxy count
- Issue: Table I notes Nmap,weighted = 8,474,531 for the Nall≥1 footprint. This equals the catalog size, which is correct because the footprint includes every pixel containing ≥1 galaxy, but this could puzzle readers.
- Required fix: Add a short footnote: “Because the Nall≥1 footprint includes every pixel hosting at least one classified galaxy, ∑p Wp = total catalog size.”

NO CHANGES TO PRIOR FINDINGS

- Several items I flagged previously (e.g., path/seed artifacts in the body, canonical σ duplications across different nulls) still stand and are not repeated here.

Why these were missed initially
- I focused on null comparability and configuration drift on the first pass; I did not recompute z from displayed inputs in every table nor reconcile Appendix numeric examples against the current tables. The fresh-eyes arithmetic/consistency sweep surfaced the z mismatches (P4-E6), the stale C1 pair in Appendix A.c (P4-E7), and the need to publish the monopole-only decoupled-null mean to substantiate the “∼12%” claim (P4-E8). The moment-z vs rank p tension in the strongly heavy-tailed harmonic channel warrants a stronger presentation change (P4-M9) than I requested before.