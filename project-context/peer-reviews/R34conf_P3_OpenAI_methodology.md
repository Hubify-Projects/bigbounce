# P3 R34conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.97.pdf` md5=4de854dd pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6093 chars)
**Wall time**: 336.5s

---

Referee report (PRD methodology)

Scope and bar: PRD requires mathematical/statistical rigor, unambiguous definitions, reproducibility, and clean, publication‑ready prose free of version history, placeholders, and internal engineering artifacts.

I read the full 28‑page manuscript (including figures, tables, appendices) and audited every load‑bearing number in the abstract and conclusions, key ratios, and statistical claims. Below I list findings with severity, page/section references, the problem, and a required fix.

ESSENTIAL

P3-E1 (Sec. V.b Fisher forecast; p. 16–17)
Problem: Dimensional/typographical inconsistency in the baseline Fisher term. Text: “F0 = 1/8.982 = 0.01239 (units: 1/σ(fNL)^2 …).” Numerically 1/8.982 ≈ 0.1115, not 0.01239. The 0.01239 value actually equals 1/8.982^2, which is the correct F0 if F0 ≡ 1/σ^2. As written, the left‑hand expression is wrong.
Required fix: Replace “F0 = 1/8.982 = 0.01239” with “F0 = 1/8.982^2 = 0.01239”, and check every location where F0 is referenced for consistency with F0 ≡ 1/σ^2. Keep the “positivity-respecting” form unchanged.

P3-E2 (Abstract; p. 1)
Problem: Version‑history language in abstract: “An earlier draft quoted 264,938/264,738 …” PRD abstracts must not contain version history or internal revision notes.
Required fix: Remove this sentence entirely from the abstract. If needed, move a brief methodological note to an appendix without referring to “earlier drafts.”

P3-E3 (Appendix A/Table VI footnote; p. 23)
Problem: Version‑history/provenance language: “an earlier draft listed 10.6 s, which is inconsistent … and has been withdrawn.” This is not suitable for the main text.
Required fix: Delete this sentence. If wall‑clock training time is unknown, state only that it was not recorded; do not reference earlier drafts.

P3-E4 (Data availability; p. 22)
Problem: Placeholders: “will be publicly released with the arXiv posting,” and “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).” PRD requires finalized links/DOIs at submission and discourages forward‑looking placeholders.
Required fix: Replace with working, permanent DOIs/URLs for all datasets, code, and model weights at the time of resubmission. Include a frozen release tag/commit hash list matching what is analyzed in the paper.

P3-E5 (Sec. III.E eROSITA; p. 10–11; Table I footnotes; Table IV caption)
Problem: The eROSITA selection axis is explicitly reported as “irreproducible,” yet a numeric threshold (“0.259”) appears in the main text. Presenting a non‑reproducible threshold in the Results section undermines reproducibility.
Required fix: Either (a) re‑run eROSITA to produce a fully reproducible per‑object score axis used for selection and report that axis and threshold; or (b) remove every numerical threshold/value tied to the unrecoverable axis from the main text and tables and present the eROSITA tier strictly as a membership list (ranked by a committed, reproducible raw or IF‑based score), ensuring that no downstream analysis in the paper uses the non‑reproducible axis.

P3-E6 (Throughout, multiple locations)
Problem: Ubiquitous version‑history/queue/defer language in the body: “earlier draft quoted…,” “withdrawn,” “queued,” “deferred to the catalog release,” “will be made public,” “companion data repository… committed artifacts,” file paths/JSON audit artifacts in main prose. PRD manuscripts must be publication‑ready and not read like an internal engineering log.
Required fix: Remove version‑history and “queued/deferred” language throughout. Move all internal file paths and JSON audit references to a reproducibility appendix or Supplemental Material, replacing them in the main text with concise, publication‑grade statements and a single pointer to the supplement.

P3-E7 (Sec. III.F Planck CMB; p. 11–12)
Problem: The released top‑200 anomaly patches are drawn from a scored bank that includes the training patches; 152/200 of the released anomalies are in the training split. The text argues this is “standard practice,” but at PRD rigor level, a held‑out evaluation is required when quoting detection rates or top‑k rankings.
Required fix: Provide a held‑out re‑scoring of an independent patch bank (disjoint from training/validation) and report the top‑200 under that setting, or demonstrate with a quantitative leakage analysis that rankings are invariant to excluding training patches (e.g., top‑200 overlap and rank correlation between full‑bank and held‑out‑only scoring). Keep the current overlap statistic, but add a held‑out result.

P3-E8 (Sec. IV.A; p. 12–13; Fig. 6)
Problem: Mixed matching radii are used for SIMBAD unmatched fractions (per‑survey 5″, pooled aggregate 3″). Although the text discloses this, the pooled 58.8% appears as a single number in Fig. 6 without a clear “3″ radius” label on the figure itself.
Required fix: Add explicit labeling on Fig. 6 that the aggregate value is at 3″ while per‑survey bars are at 5″; or recompute the aggregate at 5″ for consistency. Keep the explanatory paragraph if you retain mixed radii.

P3-E9 (Sec. V.A NANOGrav Bayes factors; p. 18)
Problem: Bayes factors BMB/free and BSMBHB/free are quoted without showing the numerical evaluation of prior and posterior densities at the specific parameter points under the stated KDE likelihood (Savage–Dickey). Without those densities or uncertainty on B, readers cannot audit the calculation or its numerical stability.
Required fix: Add a short subsection or appendix table giving the prior density at γ = 3.0 and 4.33, the estimated posterior densities (with KDE bandwidth), and the resulting Bayes factor with an uncertainty estimate (e.g., via KDE bandwidth variation or MCMC posterior sampling error). Clarify that the prior is uniform on γ ∈ [0,7] and that Bayes factors are prior‑sensitive.

P3-E10 (Conclusions; p. 21; Abstract; p. 1)
Problem: Claim of “largest multi-archive anomaly search to date” must be supported with either a literature survey or a table comparing to prior multi‑archive efforts. The anchor comparison is to the largest single‑survey catalog [11], but the claim is multi‑archive.
Required fix: Either (a) soften to “to our knowledge, larger than prior published single‑survey catalogs (anchor: [11])” or (b) add a supporting table/citation that establishes the lack of multi‑archive catalogs at comparable scale.

MAJOR

P3-M1 (Sec. II.B; p. 3–4)
Problem: The “canonical anomaly score S” uses validation‑set mean and std computed from a scaler fit to the full sample (for some tabular surveys); then an assumption is made that rankings are robust. While eROSITA has a robustness check, NEOWISE and Gaia lack them (“queued”).
Required fix: For Gaia and NEOWISE, provide the same scaler‑fit robustness checks (train‑split‑only vs full‑sample) for the published runs, at least reporting top‑k Jaccard and Spearman ρ. Without them, explicitly state that rankings may change and limit claims accordingly.

P3-M2 (Sec. III.D LAMOST; p. 10)
Problem: LAMOST “98% blue‑excess” artifact attribution is asserted on the basis of rate compression after a native retrain, but the post‑retrain per‑arm dominance fractions are “not re‑tabulated.” The key causal link (blue‑arm training drift) remains inferential.
Required fix: Tabulate per‑arm dominance fractions for the native‑retrained top‑1% slice to confirm whether the blue‑excess concentration disappears; otherwise tone down the causal language to “consistent with” and clearly separate what is measured (rate compression) from the hypothesized cause (training drift).

P3-M3 (Sec. II.D Path‑C gates; p. 5)
Problem: Gate thresholds (val‑loss ≤ 0.30; injection‑recovery ≥ 50% at 5σ; Jaccard ≥ 0.70; OOD ≥ 0.50) are acknowledged as heuristic. For PRD, such gates should be justified quantitatively or via sensitivity to reasonable alternatives.
Required fix: Add a brief sensitivity analysis showing that classification (PASS/FAIL) is unchanged for moderate threshold variations (e.g., val‑loss cut 0.2–0.5; injection recovery 40–60%; Jaccard 0.6–0.8), except where noted (SDSS continuum‑dip). Alternatively, move these gates to Supplement with a short justification.

P3-M4 (Sec. IV.B χ^2 spatial uniformity; p. 13–14)
Problem: A very large χ^2 is quoted (χ^2_ν ≈ 15.7) against a simplistic uniform‑per‑occupied‑pixel model, then immediately caveated as footprint‑dominated. As written, this risks being misread as a detection of clustering.
Required fix: Either remove the χ^2 statistic from the main text or move it to an appendix; retain only the two robust correlation null results (Galactic latitude and dust). If kept, add an effect‑size measure and an explicit “not interpretable without selection‑function modeling” label in the main paragraph.

P3-M5 (Sec. IV.C multi‑survey matches; p. 14–16)
Problem: The RA‑shifted control for random coincidence expectation is not geometry‑preserving; this is stated but then used for a numerical expectation (2.75) that readers may over‑interpret.
Required fix: Provide a rotation‑scrambled control (random great‑circle rotations) or HEALPix‑weighted local‑density control to estimate random coincidences, or delete the numeric expectation and keep only the “comparable to expectation; spectroscopic confirmation distinguishes them” qualitative statement.

P3-M6 (Appendix C; p. 22–24)
Problem: Two different normalizations for σ(fNL) baselines are used (8.98 in the main text vs 16.85 in the shot‑noise appendix). While you say they are not comparable, the figure annotates both prominently.
Required fix: Make the normalization difference visually unavoidable in the figure (e.g., “INTERNAL NORMALIZATION – NOT COMPARABLE TO MAIN TEXT” in the panel label). Optionally re‑express both on the same normalization.

P3-M7 (Sec. III.A DESI novelty via SIMBAD; p. 8)
Problem: SIMBAD match fractions for DESI top‑10k (0.2%) are given with a false‑match expectation (~0.24%)—good—but the text could be misread as implying 0% artifacts. The next sentence says “0% artifact rate” in the top‑200 by manual inspection, which is a different statement.
Required fix: Clarify separation: database coverage vs artifact rate from spectral inspection. Add an explicit statement that the 0.2% SIMBAD match fraction is consistent with random false matches at 5″, and that artifact rate is a separate manual assessment of the top‑200 only.

MINOR

P3-m1 (Sec. III.F Planck; p. 11–12)
Problem: Report “100% injection‑recovery (500/500)” without uncertainty. Binomial 68% CI for 500/500 is [~99.4%, 100%].
Required fix: Add the binomial CI for recovery fractions quoted at fixed N where exact 100% occurs.

P3-m2 (Sec. II.C GPU pipeline; p. 5)
Problem: Informal operational note “a single ~11 h pod‑restart… after a network blip” is engineering chatter irrelevant to scientific throughput.
Required fix: Delete or move to Supplement.

P3-m3 (Sec. IV.A Fig. 6)
Problem: The asterisk in the figure (“training‑bias artifact”) is not defined in the caption text itself (though explained elsewhere).
Required fix: Add a one‑sentence caption note defining the asterisk within the figure context.

P3-m4 (Sec. II.B; p. 3–4)
Problem: The symbol z is reserved for astrophysical redshift and “z‑scored” is avoided—good—but ensure no lingering uses of “z‑score” shorthand in figures/legends. I saw “z‑units” once.
Required fix: Replace “z‑units” with “standardized units” everywhere.

P3-m5 (Sec. V; p. 16–18)
Problem: The “envelope” for σ(fNL) is a deterministic mapping of α̂±σ_α, not a 68% CI on σ; well stated in prose, but the numbers appear in a way that some readers may misread.
Required fix: On first appearance of the bracket [3.92, 8.98], explicitly label “deterministic envelope from α̂±σ_α, not a probabilistic CI.”

P3-m6 (Tables/figures)
Problem: Several tables/footnotes are extremely long and contain narrative text (e.g., Table I footnotes ♠, ♡).
Required fix: Move long narrative footnotes to an appendix or Supplement; leave concise, citable statements in the table.

NITS (cosmetic/editorial)

P3-n1 (Throughout)
Problem: Overuse of em‑dashes and parenthetical asides; reads like lab notebook rather than PRD style.
Required fix: Streamline prose; move engineering/provenance to Supplement.

P3-n2 (Sec. II.D; p. 5)
Problem: “7-way positional dedup at 5′′ .” Extra space before period, stray thin space mark.
Required fix: Correct spacing/typography.

P3-n3 (Sec. III.H; p. 12)
Problem: “1000/1000 = 100% … passes by construction” repeats twice across main text and figure caption.
Required fix: Keep once; remove duplication.

Arithmetic/consistency audit (selected checks)

- Path‑C per‑survey native counts sum to 388,493. Dedup collapsed 10,213 (2.629%) to 378,280 unique. Verified: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; 10,213/388,493 = 2.629%.
- Point‑source unique = 378,080, plus 200 Planck patches = 378,280. Consistent with zero overlaps between map patches and point sources at 5″.
- NEOWISE mask: retained 419/436 = 96.1%; removed 3.9%; polar‑cap area fraction at |b_ecl|>80° ≈ 1 − sin 80° ≈ 1.52%; 3.9%/1.52% ≈ 2.57× (rounded to 2.6×). OK.
- SDSS native: 77,905/1,925,279 = 4.05%; top‑1% = 19,253. OK. Applying S>5 yields 12 objects; cross‑transfer inflation factor ≈ 77,905/12 ≈ 6.49×10^3. OK.
- LAMOST native re‑score pool 11,334,161 of 11,418,594 (84,433 lost, 0.74%); top‑1% = 113,342; cross‑transfer/native S>5 compression 44,075/2,054 ≈ 21.5×. OK.
- DESI dedup clusters 190,015; science‑class 1″ matches 2,468 = 1.30%; rate on 20,299,155= 0.0122%. OK.
- “Largest prior single‑survey catalog 2,685 [11]”; scaling: 378,080/2,685 ≈ 140.8×; 269,117/2,685 ≈ 100.2×; DESI 195,829/2,685 ≈ 72.9×. OK (with caveats noted in text).
- Novelty fraction 178/1000 = 17.8%; Wilson 68% ≈ ±1.2%. OK.
- NANOGrav sigmas: |3.0 − 2.567|/0.382 ≈ 1.13σ; |4.33 − 2.567|/0.382 ≈ 4.61σ. OK.

Stand‑alone reader test

- Several key claims rely on external audit artifacts (JSON paths) and “companion repository” scripts. While helpful, the main text should not require opening those to understand or verify the argument. Move all file‑path minutiae to Supplement and include brief, self‑contained numeric summaries in the paper itself.

Page length

- At 28 pages with heavy narrative footnotes and engineering prose, the paper is longer than needed for the contribution. Recommend ≤ 18 pages main text by moving engineering detail, file paths, and long narrative table footnotes to Supplement, and tightening prose.

## Summary recommendation
MAJOR REVISIONS

The manuscript presents impressive scale and careful caveats, but several issues prevent PRD acceptance in its current form: (1) a core dimensional/typographical error in the Fisher baseline (must fix), (2) pervasive version‑history/placeholders that must be purged, with finalized DOIs provided, (3) the eROSITA irreproducible threshold must be either made reproducible or excised from the main results, and (4) the Planck top‑k ranking needs a held‑out confirmation. Additional major points concern justification/sensitivity of heuristic gates and clearer, audit‑ready Bayes factor computation. Addressing these, and moving engineering artifacts to Supplement, will bring the paper in line with PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (PRD methodology audit — new issues only)

ESSENTIAL

P3-E11 (Sec. II.B “Canonical anomaly score S”; Fig. 3; Table I footnotes)
Problem: Inconsistent global definition of S. The paper states that “S refers to the per‑survey standardized residual” with two exceptions (Planck raw MSE; eROSITA), but SDSS and LAMOST cross‑transfer figures use S standardized by the DESI validation statistics, not by an SDSS/LAMOST native validation pool. This third exception is only implied later in Table I footnotes, not in the canonical definition section.
Required fix: Amend the global S definition to explicitly include the cross‑transfer exception (SDSS/LAMOST when scored with the DESI‑trained model use DESI’s µval, σval), and ensure all figures/captions that use the cross‑transfer S axis state this explicitly.

P3-E12 (Sec. II.C GPU Inference Pipeline; Sec. III.F; Table VI footnote)
Problem: Hardware inconsistency. The text says “All inference was performed on a single NVIDIA H200,” but Sec. III.F/Table VI footnote state the 2×10^5‑patch Planck native re‑score was done on an A100 (25.3 s). Both cannot be true as written.
Required fix: Correct the hardware statement to specify which surveys/passes were inferred on H200 and which on A100, and adjust any throughput summaries that currently assume “all inference” on H200.

P3-E13 (Sec. III.B; Fig. 5 caption — Legacy Survey cutout scales)
Problem: Arcsecond sizes given for DESI Legacy Survey DR9 cutouts are inconsistent with the survey’s pixel scale. The text says 128×128 px ≈ 54″ and 256×256 px ≈ 108″; at the LS DR9 coadd scale (0.262″/px), these should be ≈33.5″ and ≈67.1″, respectively. No alternative resampling scale is stated.
Required fix: Provide the correct arcsecond sizes (or explicitly state a different pixel scale if images were resampled), and make sizes consistent across all captions that cite them.

P3-E14 (Appendix E, Eq. E1 — dimensional/normalization clarity)
Problem: The power‑law mapping used for the ceffyl KDE free‑spectrum fit logs quantities “fyr, fi, Tobs” without explicit unit conventions, yet logs must be dimensionless. The 1/2 factor and constants (e.g., −log10(12π^2)) aren’t tied to a referenced standard form, making it hard to audit normalization.
Required fix: Define units for fi, fyr, and Tobs so all log arguments are dimensionless; cite or derive the exact mapping to the ceffyl free‑spectrum parameterization, including the origin of the 1/2 factor and constants. Provide a brief check (e.g., recover the published free‑spectrum normalization for a reference γ,A pair).

MAJOR

P3-M8 (Sec. IV.B “Spatial Analysis” — correlation tests)
Problem: “Anomaly rate shows no correlation with Galactic latitude (Spearman) or Planck dust (Pearson),” but “rate” is not defined. Without a per‑pixel denominator (e.g., anomalies per scored sources in that pixel) and selection‑function weighting, the correlation nulls are ambiguous.
Required fix: Specify the rate definition and denominator (per scored sources or per area), the pixel weighting scheme, and whether survey footprints/selection are accounted for; recompute with that explicit definition or soften the claim to a qualitative statement and move quantitative results to Supplement with full method.

P3-M9 (Sec. IV.A, last paragraph — “expected random coincidences”)
Problem: The statement “expected random coincidence contribution is ≲10 across all survey pairs” is given without a null model description (source densities, footprints, or scrambling scheme).
Required fix: Provide a proper, geometry‑aware null (e.g., rotation scrambling or HEALPix‑weighted local‑density control) and report the resulting expectation and uncertainty; or remove the numeric “≲10” and keep only the qualitative statement that it is small compared to 637 observed multi‑survey clusters.

P3-M10 (Table VI; Sec. II.C; Sec. III.F — training time plausibility/logging)
Problem: Photometric models report single‑digit‑second total training times (eROSITA 7.6 s, Gaia 1.2 s, NEOWISE 1.6 s) for up to 200 epochs on 50k–930k‑row catalogs. This appears implausible without evidence of early stopping after very few epochs and specific hardware/logs.
Required fix: Provide training logs (epochs actually run, early‑stopping epoch, batch size, GPU), or move training‑time numbers to Supplement and state clearly that early stopping at very low epoch counts produced the quoted wall‑clock. If times are estimates, label them as such.

MINOR

P3-m7 (Sec. II.D Step 5; Fig. 10; Secs. III.C/F/H)
Problem: Recovery fractions are quoted at fixed N without uncertainties (e.g., SDSS 64% at N=500, Gaia 5.2% at N=?, etc.). Only the 500/500=100% case is discussed elsewhere in CI terms.
Required fix: Add binomial 68% CIs for all quoted recovery fractions (state N explicitly for each), or add a single sentence noting N and the approximate ±√[p(1−p)/N] uncertainty for each curve’s 5σ point.

P3-m8 (Sec. III.F Planck; patch‑rank units)
Problem: The Planck top‑200 patch MSE score range [0.558, 0.621] is quoted without stating units or normalization (per‑patch standardized MSE).
Required fix: Add “dimensionless per‑patch reconstruction MSE on standardized patches” to the text or caption where this range is given.

P3-m9 (Sec. II.B “Canonical anomaly score S”)
Problem: Figure 3 caption uses “z‑units” once when referring to the S rescaling (conflicts with the earlier editorial decision to avoid “z‑score” wording to prevent confusion with redshift).
Required fix: Replace “z‑units” with “standardized units” in the caption and anywhere else it appears.

Rationale for completeness
I focused on fresh classes of issues: definition consistency for S under cross‑transfer use, hardware inconsistency in inference claims, incorrect/desultory image scale conversions, insufficiently specified correlation “rate” denominator, unsupported random‑coincidence expectation, plausibility of training‑time claims, and dimensional clarity of the PTA mapping. These were not covered in the initial review and materially affect rigor, auditability, or reader clarity.