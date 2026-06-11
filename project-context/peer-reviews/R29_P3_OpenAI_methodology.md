# P3 R29 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.88.pdf` md5=bbc52726 pages=26
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7351 chars)
**Wall time**: 270.5s

---

Referee report (PRD – Methodology)

Overall scope and contribution
The manuscript presents a multi-archive autoencoder-based anomaly catalog, with per-survey native retraining (“Path-C”) and a 7-way 5″ deduplication yielding 378,280 unique entries (200 of which are Planck map patches). It further reports a DESI-only anomaly rate, several validation gates (k-fold Jaccard, injection–recovery), cross-survey overlap counts, an archival novelty check on the top-1,000 DESI anomalies, and two cosmology applications (a multi-tracer fNL Fisher forecast using an empirically measured bias ratio and a refit to the NANOGrav 15-yr KDE free-spectrum).

I audited all equations, numerical statements, ratios, percentages, significances, and cross-referenced the abstract and conclusions against the body. Many internal arithmetic checks pass (e.g., 195,829/22.50M = 0.87%; 388,493 − 10,213 = 378,280; 284/298 = 95.3%; 17/436 = 3.90% and 3.90% / 1.52% ≈ 2.56; χ2ν = 376,713/24,048 = 15.66). However, there are several critical issues that must be corrected for PRD standards:

- A dimensionally incorrect Fisher baseline is printed repeatedly (F0 reported as 1/8.98 instead of 1/8.98^2), although subsequent numbers happen to be consistent with the squared form.
- The eROSITA anomaly-score axis (SBigAE) is declared irreproducible in the text yet is still tabulated/used. Publishing an anomaly-score column that the authors themselves say cannot be reproduced is not acceptable for PRD.
- The manuscript contains extensive version-history language and internal bookkeeping/pathnames (“earlier draft quoted…”, “withdrawn figure”, “r24conf…json”), which must be removed from the body of a PRD paper.
- The data/weights release is referenced with placeholders (“will be made public with the arXiv posting”, “DOI inserted at submission”). PRD requires finalized, citable release information at acceptance.
- Several methodology claims rely on qualitative statements where reproducible numbers or precise definitions are required (e.g., the out-of-distribution SPARCL sweep “>50%” flag rate; details of injection procedures for each survey; the precise construction of the 5,384-object QSO-candidate sample used in the bias measurement).

Below I list all findings with classification and required fixes.

Findings

ESSENTIAL

P3-E1 (Sec. V, pp. 15–16; Table IV (i), p. 19; Abstract, p. 1)
Problem: Fisher baseline printed with wrong dimensionality. Text states “1/σ^2(fNL) = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747”. If σstd = 8.98, then F0 must be 1/(8.98)^2 ≈ 0.01238, not 1/8.98 ≈ 0.111. The reported central σ(fNL) = 8.14 and the envelope [3.92, 8.98] are consistent only with F0 = 1/σ^2 = 1/(8.98)^2.
Required fix: Correct every occurrence of F0 to F0 = 1/(8.98)^2 (and the analogous numerical value wherever quoted). State units/dimensions explicitly: “F0 ≡ 1/σ^2std”. Ensure all downstream text and any plotted numbers are recomputed/checked.

P3-E2 (Sec. III.E, pp. 8–9; Table III, p. 10; Table I footnotes, pp. 9–10)
Problem: eROSITA score axis (SBigAE) is declared irreproducible (“could not be reconciled… non-monotone… do not use SBigAE as a continuous science data product”), yet these values are printed in Table III and a “threshold 0.259” is used in prose. Publishing a catalog score column that the authors state cannot be reproduced falls below PRD reproducibility standards.
Required fix: Either (a) provide a fully reproducible scoring axis (precise computation pipeline; code and scaler statistics sufficient to regenerate the per-object values; show that the 0.259 threshold is recovered on re-run), or (b) remove the SBigAE column from all tables and text, and present the eROSITA selection strictly as a membership list ranked by a documented, reproducible raw-score axis; adjust all thresholds/descriptions accordingly.

P3-E3 (Multiple locations: Abstract p. 1; Fig. 2 caption p. 6; Sec. III.E pp. 8–9; Sec. IV.B p. 12; Table V footnote p. 21; elsewhere)
Problem: Version-history/internals in body text: phrases such as “earlier draft quoted 264,938/264,738… superseded”, “an earlier draft listed 10.6 s… withdrawn”, “that artifact’s pixel-selection… could not be recovered… withdrawn”, “artifact r24conf_…json”, “committed training log.json”, “recovered production specification… recovered pod scripts”. PRD manuscripts must not contain internal lab bookkeeping, prior-draft commentary, or pathnames as load-bearing evidence.
Required fix: Remove all version-history and internal-file-path language from the main text and figures. Move essential provenance details (code version, commit hash, artifact names) to a dedicated, concise Reproducibility Appendix and Data Availability section. Eliminate any mention of previous numbers that are not part of the final result.

P3-E4 (Data availability, p. 20)
Problem: Placeholders and non-final release info (“will be made public with the arXiv posting”, “DOI inserted at submission”). PRD requires stable, citable DOIs/URLs at acceptance; “will be” and placeholders are not acceptable.
Required fix: Provide final, minted DOIs (Zenodo, etc.), frozen release tags/commit hashes for code and weights, and a single, self-contained manifest. Ensure the paper text contains everything a reader needs to fetch the exact version used to make the figures/tables.

P3-E5 (Sec. III.H, p. 11; Fig. 10 caption, p. 20; Abstract, p. 1)
Problem: Injection-recovery gates are summarized as “3 PASS”, but only two are detector-sensitivity tests (SDSS, Planck); the NEOWISE “100% PASS” is a mask-geometry QA that by construction must pass. The abstract does include a parenthetical caveat, but the headline “Six injection-recovery gates: 3 PASS … 3 FAIL-with-diagnostic” can still be misread as 3 detector PASSes.
Required fix: In the abstract, main text, and conclusions, rewrite the headline sentence to “2 PASS (detector sensitivity: SDSS 64%, Planck 100%); 1 mask-geometry QA PASS (NEOWISE, not a sensitivity test); and 3 FAIL-with-diagnostic…”. This must be explicit wherever the “3 PASS” count appears.

MAJOR

P3-M1 (Sec. II.D, p. 5; Table I caption/footnotes pp. 9–10)
Problem: Threshold heterogeneity across surveys (DESI fixed S>5; SDSS continuity slice S≥0.1060 sized to cross-transfer count; SDSS top-1% at S≥0.2051 also used; LAMOST native top-1%; eROSITA fixed top-298 “score-knee” on an irreproducible axis; Planck/Gaia/NEOWISE top-1%). The paper mixes selection rules, which complicates cross-survey comparisons and dedup geometry interpretation.
Required fix: Provide a clear, survey-by-survey rationale for final catalog thresholds and add a sensitivity table/figure showing how unique-object counts and overlap structure vary under at least one uniform rule (e.g., per-survey top-1% across all seven, and/or a common absolute S>5 where defined). Alternatively, move the continuity-slice tiers to Supplementary and anchor all main-text comparisons on a single, uniform per-survey rule.

P3-M2 (Sec. II.B, pp. 3–4; Sec. VI.D(i), p. 18)
Problem: Out-of-distribution (OOD) statement “applying [S>5] to a random uncurated SPARCL sweep flags >50% of spectra (a catalog-curation effect, not a threshold artifact)” is a qualitative claim without the exact denominator, OOD sample definition, or a figure/table reference. It is used to justify threshold behavior.
Required fix: Provide the exact OOD sample size, the fraction flagged with uncertainties, and a brief description (or appendix) of curation differences that explain the >50% flag rate. Add a figure or table documenting the OOD MSE/S distributions relative to curated DESI DR1.

P3-M3 (Sec. V, pp. 15–16; Table IV (e), p. 19)
Problem: GR projection corrections are asserted as “|Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1 … internal order-of-magnitude bound”. This is not quantified or referenced to a standard calculation and reads as a qualitative reassurance.
Required fix: Either remove the numeric <0.02% claim, or provide a short calculation (or a clear literature citation with matching setup) showing the expected size from the (H/k)^2 suppression in your Fisher-weighted bands. State all assumptions (monopole only, plane-parallel, bias range, redshift, k-range).

P3-M4 (Sec. V, p. 15; Appendix C, p. 21; Fig. 11, p. 22)
Problem: The 5,384-object QSO-candidate sample used for the empirical α measurement is not precisely specified (selection cuts, redshift range, photometry criteria). Later a separate “Gold+Silver” 1,122-object subset is defined, but the 5,384-object construction feeding αjk is not given.
Required fix: Provide an explicit definition of the 5,384-object QSO-candidate selection (all cuts, catalog sources, redshift limits, and masks), so that the bias measurement can be reproduced without the companion repository.

P3-M5 (Sec. II.B, pp. 3–4; Sec. III.G, p. 11)
Problem: Gaia preprocessing is “lineage-inferred” (original 20-feature production script not recovered) and the selection is labeled “training-sample-conditioned” (41% XV-stability), yet the main text still reports a fixed top-1% anomaly set (500 objects).
Required fix: Move the Gaia anomaly list to an exploratory appendix or provide the exact, reproducible 20-feature list and scaler statistics used in the 50,000-source run published here. If the exact script cannot be produced, label this survey as exploratory and exclude it from headline catalog claims.

P3-M6 (Sec. II.D Step 5, p. 5; Fig. 10 p. 20; scattered)
Problem: Injection–recovery details are only partly specified across surveys (e.g., “500 planted signals per survey at six amplitude levels (0.5–20×σ)”, but the morphology of injections for eROSITA and Gaia, the noise model used to define σ, and the decision thresholds per survey are not all given in one place).
Required fix: Add a compact Method Appendix table that, for each survey, specifies: injection morphology (continuum dip, line, latent-space subspace, variability-axis, Gaussian bump), how σ is defined, the number of injections per amplitude, the recovery criterion (e.g., threshold axis), and the resulting recovery fractions (with binomial uncertainties) at the quoted 5σ point.

P3-M7 (Sec. III.C, pp. 6–7; Fig. 3, p. 7)
Problem: Cross-transfer SDSS “S” values as high as 1.9×10^11 are presented on a “validation z-units” axis. While the text notes the cross-transfer domain-shift and axis non-comparability, labeling these as “z-units” can be misconstrued as σ-units in a statistical sense.
Required fix: Add an explicit sentence in the SDSS section and/or Fig. 3 caption clarifying that the “S” axis here is a DESI-validated scale applied out-of-distribution, so numeric magnitudes (e.g., 10^11) do not have a σ-like interpretative meaning and arise from extreme reconstruction residuals under domain shift.

P3-M8 (Sec. IV.C, p. 13)
Problem: Chance-coincidence expectation for the DESI×SDSS 3″ cross-match is quoted as “∼2.3” from a uniform-density analytic calculation, but the underlying surface densities are not shown; the RA-only shift control is acknowledged as heuristic.
Required fix: Provide the analytic calculation inputs (surface densities, sky area overlap) that yield ~2.3, or remove the number and retain only the RA-shift control (while flagging its limitations). If retained, quote uncertainties or a range from alternative controls (e.g., random rotations).

MINOR

P3-m1 (Sec. III.A, p. 5)
Problem: “Top 100” versus “top 10,000” DESI anomaly cross-matching: you report 12.7% in NED for the top 10,000, and “none of the top 100 appear in SIMBAD or NED”. While not logically inconsistent, readers may misread this juxtaposition.
Required fix: Add a clarifying sentence that the top-100 are the highest-score subset of the top-10,000 and happened to have zero NED/SIMBAD matches.

P3-m2 (Sec. II.B, p. 3)
Problem: The DESI MSE threshold translation “S > 5 corresponds to MSE ≈ 0.143” is given without listing σval. It is reconstructible, but a reader would benefit from the numeric σval used (≈0.0229 by back-calculation).
Required fix: Print σval and μval values used for DESI so the 0.143 is transparent.

P3-m3 (Sec. IV.B, p. 12)
Problem: Spatial χ2 test uses “occupied pixels” at Nside=64 and a “uniform per-occupied-pixel mean”; this is not a standard null against survey geometry, and the caveat is noted.
Required fix: In one sentence, make explicit that this χ2 statistic is not interpretable cosmologically without per-survey selection functions and is provided as a descriptive inhomogeneity indicator only.

P3-m4 (Sec. III.A, p. 5)
Problem: “0% artifact rate (each spectrum’s peak-residual wavelength was compared against 11 known sky and telluric features…)” without listing the 11 features or a ref.
Required fix: Provide a short list (or a citation to the line list) in a footnote or appendix.

P3-m5 (Fig. 5, p. 11)
Problem: The panel shows a DESI Legacy grz stamp for a NEOWISE anomaly; no scale bar is drawn.
Required fix: Add a nominal angular scale or note the pixel scale in the caption.

P3-m6 (Sec. V.A, p. 16; Appendix E, pp. 22–24)
Problem: “ceffyl” KDE free-spectrum likelihood is used; the citation [36] is Lentati et al. 2013 (general Bayesian method). Consider citing the NANOGrav KDE product DOI directly (you already include Zenodo 10.5281/zenodo.8060824) and one KDE-method reference for context.
Required fix: Add a brief one-line method reference/citation for the KDE approach if distinct from [36], or state explicitly that you use the exact NANOGrav-provided KDE product without modification.

NITS

P3-n1 (Multiple)
Problem: Overuse of em dashes with parentheticals, producing very long sentences that obscure load-bearing statements.
Required fix: Break long sentences where possible; move tertiary clarifications to footnotes or an appendix.

P3-n2 (Table VII, p. 21)
Problem: The table is labeled “Legacy fixed-α reference (superseded)”. PRD generally discourages presenting superseded material in the main body.
Required fix: Move Table VII to an appendix or supplementary, clearly labeled as legacy reference only.

P3-n3 (Fig. 3, p. 7)
Problem: Left panel y-axis “Probability density” and right panel “Prob. density” use slightly different labels.
Required fix: Harmonize axis labels.

Abstract-last drift sweep (pattern-045)
- The abstract’s “genuine novelty fraction of ∼17.8% (Wilson 68% CI ±1.2%; a single-sample point estimate … not a survey-wide … rate)” matches §IV.A and is properly caveated. OK.
- “21.5× LAMOST rate compression and ∼6500× SDSS rate compression” are consistent with §III.C/D (44,075/2,054 ≈ 21.5; 77,905/12 ≈ 6,492). OK.
- “DESI 5-fold Jaccard stability J¯ = 0.862 (≥ 0.70 gate, PASS)” matches §II.B/C. OK.
- “Six injection-recovery gates: 3 PASS (… NEOWISE mask-geometry 100% — a masking-geometry sanity check …)” includes the key caveat. OK once P3-E5 rewrite is made in all occurrences.
- “σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98]” is numerically consistent with the corrected F0 = 1/(8.98)^2. Needs P3-E1 fix.
- “BMB/SMBHB = 7.14×10^3 under the flat γ ∈ [0, 7] prior; prior-sensitive …” and the environment caveat are carried from §V.A. OK.

Provenance surfaces (patterns 046/047)
- Replace all “will be made public/DOI inserted…” with final DOIs and frozen manifests (P3-E4).
- Move internal pathnames and JSON filenames into a concise Reproducibility Appendix; the current scattering across footnotes and captions is not acceptable (P3-E3).

Uncomputed quantitative claims (pattern-048)
- OOD “>50%” claim needs numbers (P3-M2).
- GR projection “<0.02%” needs a calculation or removal (P3-M3).

Standalone-reader test
- Define the 5,384-object QSO-candidate selection precisely (P3-M4).
- Provide a compact per-survey injection table (P3-M6).
- For Gaia, supply the exact feature list/scaler or mark as exploratory (P3-M5).

Effect sizes
- Where χ2ν ≫ 1 is reported (Sec. IV.B), you provide the caveat; add a brief effect-size statement (e.g., excess variance not meaningful without selection-function correction). Covered by P3-m3.
- For the Bayes factor, you already include the prior-sensitivity caveat and the environmental-SMBHB caveat; OK.

Length
At 26 pages plus extensive footnotes, the paper is long relative to the core contributions. Given the breadth (seven archives plus two cosmology applications), this may be acceptable for PRD provided the version-history and internal-provenance clutter is removed and technical appendices consolidate details. If tightened, the main text could be reduced by ~15–20% without loss (move legacy/withdrawn/superseded content and many verbose footnotes to appendices).

## Summary recommendation
MAJOR REVISIONS

The science case is interesting and many internal numbers check out, but the manuscript does not yet meet PRD methodological and reproducibility standards. The Fisher-baseline dimensional error must be corrected, the irreproducible eROSITA score axis must be resolved or removed, all version-history/internal-artifact language must be excised from the body, final DOIs and frozen manifests must be provided, and several methodological clarifications are required (uniform threshold sensitivity, OOD quantification, injection tables, precise selection definitions). With these corrections and consolidation, the work could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P3-E6 (Planck selection denominator and “rate,” Sec. III.F pp. 9–10; Table I main block and footnotes; Data-volume tallies)
Problem: The paper presents the Path-C Planck tier as “top-1% (200/20,000)” while the native Path-C pipeline actually extracts and rescored 2×10^5 patches and then fixed the catalog to the top 200 of that 200k bank. That is a 0.10% selection under the native run, not 1.00%. In Table I, Ntotal for Planck is still listed as 20,000 in the Path-C summary row, and the overall processed-source total 37,272,042 therefore excludes the additional 180,000 native Planck patches actually used.
Required fix: Make Planck internally consistent. Either (a) define the published tier as “fixed-count top-200 from a 200,000-patch native bank,” update Ntotal to 200,000 and the “Rate” to 0.10%, and update the overall processed total accordingly; or (b) re-run with a 20,000-patch native bank to preserve the stated 1.00% semantics. In all cases, remove “top-1%” from Planck if the denominator is 200,000.

MAJOR

P3-M9 (Missing spectroscopic preprocessing specification, Sec. II.A/B; throughout)
Problem: For the spectroscopic surveys (DESI, SDSS, LAMOST), the manuscript never specifies the exact input scaling/normalization pipeline used prior to MSE training: e.g., per-spectrum continuum normalization, per-wavelength z-scoring/statistics (global vs split), handling of negative flux, arm-wise rescaling, bad-pixel/sky-mask handling, variance weighting, and whether any per-spectrum renormalization is applied. The “tabular-survey feature preprocessing” is detailed, but the spectral pipeline is not. Without this, Eq. (1)–(2) and the quoted µval ≈ 0.0287 for DESI are not reproducible.
Required fix: Add a compact subsection (or Method Appendix table) documenting the full spectroscopic preprocessing for each survey: resampling/downsampling recipe, flux scaling (what statistics, over what pool/split, stored values), masking rules, SNR handling, any per-arm operations, and NaN/Inf policy.

P3-M10 (Appendix E likelihood definition incomplete: units and mapping, App. E pp. 22–24; Sec. V.A p. 16)
Problem: Equation (E1) introduces log10 ρi without a definition of ρi (units, whether it is the ceffyl KDE variable or a derived power/strain density), and without an explicit mapping to the NANOGrav KDE product’s per-frequency likelihood variable. The text says “ceffyl-style KDE likelihood factorizes,” but does not specify precisely which quantity is being modeled by the KDE and how (E1) maps amplitudes (A, γ) into that variable.
Required fix: Define ρi precisely (name and units), state which ceffyl free-spectrum quantity is used (e.g., log10 ρ(f) ≡ log10 Ared/PTA with HD correlation), and show or cite the exact mapping used by NANOGrav for the KDE product. If you follow the NANOGrav-provided transformation verbatim, cite the specific equation/README line and confirm that (E1) matches their convention.

P3-M11 (Planck contribution to “processed totals” inconsistent with native pipeline, Table I and Sec. III.F)
Problem: The Path-C “processed total” 37,272,042 excludes the extra 180,000 native Planck patches actually used for training/rescoring. This creates a mismatch between the narrative (“native retrain on 200k patches”) and the headline data-volume accounting (“20k patches”).
Required fix: Reconcile the processed-total accounting with the actual native Planck run (see P3-E6). Either update totals to include 200k or clearly segregate “selection denominator (historical cross-transfer 20k)” versus “native training/rescore bank (200k)”, and stop labeling a 200/200k selection as “1.00%”.

P3-M12 (Ambiguous definition of α in the fNL section, Sec. V pp. 15–16; Fig. 9; App. C)
Problem: The text uses both “bias ratio b ≡ bQSO-cand/bfull-anomaly” and “α” without explicitly defining α. From numbers (bgeo = 1.27 → αgeo = 0.27), α appears to be α ≡ b − 1. This must be stated once, unambiguously, where α first appears.
Required fix: Add a sentence: “We define α ≡ b − 1 = bQSO-cand/bfull-anomaly − 1,” and propagate that definition consistently.

MINOR

P3-m7 (SIMBAD “Novel” labeling misleads, Table III p. 10; Sec. III.E pp. 8–9)
Problem: The eROSITA Table III column “SIMBAD” labels entries “Novel” for “no SIMBAD counterpart,” but the body text elsewhere stresses that SIMBAD-unmatched is not equivalent to true catalog novelty. The table header and footnote could be read as endorsing “novel.”
Required fix: Relabel to “No SIMBAD match (5″)” and add “not a catalog-novelty claim” in the table note, consistent with §IV.A.

P3-m8 (Per-class DESI rates lack denominators, Sec. III.A p. 5)
Problem: The statement “galaxies are flagged at ~20× the rate of QSOs (0.75% vs. 0.037%)” is not accompanied by the explicit per-class counts/denominators used. This prevents a reader from reproducing the rates.
Required fix: Provide the per-class anomaly counts and total class sizes (numerators/denominators), or a citation to a table/appendix where they are printed.

P3-m9 (7-way random-coincidence estimate lacks construction details, Sec. IV.A p. 12)
Problem: The claim “for the 7-way 5″ deduplication, the expected random coincidence contribution is ≲10 across all survey pairs” is not supported by the inputs/geometry used to obtain the number.
Required fix: Provide the calculation (pairwise surface densities, overlap area, radius, and the summation over survey pairs), or move the claim to an appendix with the null-construction details.

P3-m10 (Figure 6 caption radius)
Problem: The body text notes that the pooled 58.8% SIMBAD-unmatched fraction was computed at 3″ (not the 5″ default used elsewhere), but the Figure 6 caption does not restate the 3″ radius.
Required fix: Add “computed at 3″” to the Figure 6 caption.

P3-m11 (Definition of SNR for score–SNR test, Sec. III.A p. 5)
Problem: The Spearman test “ρ = −0.03” is reported without defining the SNR metric (per pixel? per arm? pipeline S/N?). A one-line definition would make the result interpretable and reproducible.
Required fix: Specify the SNR definition and its source (e.g., Redrock median per-pixel S/N over [λ1, λ2]).

P3-m12 (Fig. 7 bottom-right panel)
Problem: The red dashed line appears to mark S = 5 but is not referenced in the caption.
Required fix: Note in the caption that the red dashed line indicates the DESI catalog threshold S = 5.

NITS

P3-n4 (Terminology consistency for Planck tier)
Problem: Mixed phrasing “top-1%” versus “fixed-count 200” for Planck appears in different places. Given P3-E6/E11, standardize the language.
Required fix: Use a single phrasing everywhere, consistent with the corrected denominator.

P3-n5 (Define ρi symbol on first use)
Problem: ρi appears in Eq. (E1) without a preceding in-text verbal definition before the equation.
Required fix: Add a one-clause definition immediately before Eq. (E1) to aid readability.

Explanation
These items were not raised in my initial review because they only become apparent when (i) reconciling native-Planck bookkeeping against Table I totals/rates, and (ii) executing a strict reproducibility read for spectroscopic preprocessing and the PTA likelihood mapping. The additional arithmetic/caption/definition gaps above are typical “second-pass” failures that surface under PRD’s reproducibility bar.