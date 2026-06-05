# P3 auto-2026-06-05_1418pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9669 chars)
**Wall time**: 318.1s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path‑C Unique Anomalies …”

Scope of review: methodological rigor (statistics, derivations, internal arithmetic, dimensional consistency, estimator pre-declaration, figure/table audit, abstract/conclusions scalars traceability).

Overall: The paper presents a very large cross‑archive anomaly catalog built with an autoencoder pipeline and uses it to motivate cosmological forecasts. While the scope is ambitious, there are multiple essential methodological inconsistencies and arithmetic/dimensional errors that must be corrected before PRD can consider publication. Below I itemize all findings with classification and required fixes.

ESSENTIAL FINDINGS

P3-E1 (Sec. V, p. 10; Table IV caveat (i), p. 13)
Problem: Dimensional/arithmetic error in the Fisher forecast baseline. The text states “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747”. If σstd = 8.982, then F0 must be 1/σstd^2 = 1/(8.982)^2 ≈ 0.012398, not 1/8.982 ≈ 0.1113. The reported central σ(fNL)=8.14 only follows if F0=1/8.982^2.
Required fix: Correct F0 everywhere to 1/(8.982)^2 and audit every downstream occurrence (Sec. V, Table IV (i), Appendix C/Fig. 8 text) for internal consistency. State explicitly that the “positivity‑respecting” form uses inverse variance (not inverse σ).

P3-E2 (Table I footnote ♡, p. 7; Sec. III C, p. 5)
Problem: Inconsistent and incorrect “top‑1%” labeling for SDSS counts. The text calls 77,905 SDSS anomalies a “top‑1% continuity slice” on a 1,925,279‑spectrum sample, but 1% of 1,925,279 is 19,253 (which you also list). 77,905/1,925,279 = 4.05%, not 1%. Table I uses Ntotal=2,304,830 and reports 77,905 (3.38%), adding further inconsistency.
Required fix: Correct all SDSS percentages and “top‑1%” labels. Provide one consistent Ntotal for the sample actually scored and use correct percentages for every count. Clarify which SDSS slice is your primary (and why), and remove/confine all others to an appendix.

P3-E3 (Multiple locations: Sec. II A p. 2; Sec. II B p. 2; Sec. III B p. 5)
Problem: Unresolved figure references “Fig. ??” appear in the camera‑ready PDF (e.g., architecture schematic; per‑band residuals; DR9 cutouts for z~6 candidates).
Required fix: Resolve all “??” references and include the missing figures. The paper cannot proceed without complete cross‑referencing.

P3-E4 (Sec. II C, p. 3; Table V p. 15)
Problem: Wall‑clock time inconsistency. You claim “approximately 42 hours” total, “dominated by” DESI (19,705 s ≈ 5.47 h) and LAMOST (11.4M spectra; throughput ~950/s ⇒ ~3.3 h). With other surveys <10 s each, the stated numbers sum to <9 h, not 42 h. In Table V, Planck CAE “train time” is listed as 10.6 s for 2×10^5 patches — implausible by 2–3 orders of magnitude on an A100 for a 1.1M‑param CAE.
Required fix: Provide a complete, reconciled time budget: per‑survey preprocessing time (CPU), data transfer, GPU forward/inference time, and training times, with consistent units. If “42 hours” includes I/O and serial preprocessing, say so and report separate CPU/GPU components. Correct unrealistic training times (e.g., Planck CAE 10.6 s) or justify with reproducible logs.

P3-E5 (Sec. V, p. 10; Appendix C/Fig. 8, p. 16; Table VII p. 15)
Problem: Two different single‑tracer σ(fNL) baselines are used without explicit “not directly comparable” warnings: σstd = 8.98 in Sec. V/Table VII vs. 16.85 in Fig. 8 (appendix). Per journal instruction, placing sigma values from different null procedures or configurations without explicit comparability disclaimers is not acceptable.
Required fix: Use a single consistent σstd throughout, or clearly label each baseline with its tracer sample, redshift binning, volume, and modeling assumptions, and state explicitly at each juxtaposition that they are not directly comparable. If Fig. 8 uses a different survey geometry/configuration, label it on the figure and in the caption.

P3-E6 (Data availability, p. 14)
Problem: “private pending arXiv acceptance; public upon acceptance.” PRD requires data/code availability that allows reviewers and readers to reproduce key results. Private repositories are not acceptable at acceptance.
Required fix: Make the datasets, trained weights, and analysis scripts publicly accessible at resubmission (or provide a PRD‑approved confidential link for referees now and commit to permanent public access upon publication). State exact DOIs/commit hashes.

P3-E7 (Sec. III C/D; Table I, p. 7; Abstract p. 1)
Problem: Mixing threshold families compromises methodological clarity. You claim a “~6500× SDSS rate compression after native retraining” by comparing cross‑transfer S>5 anomalies (77,905) to native S>5 anomalies (12). But the headline SDSS native release is also reported as “top‑77,905 at S ≥ 0.1060”, which is not S>5 and not 1%. The abstract’s “~6500× after native retraining” is therefore a threshold‑mix artifact.
Required fix: Pre‑declare a single primary anomaly definition per survey (S>5 for spectra; or top‑p%), use that consistently for all cross‑survey rate compares, and move all alternative thresholds to a controlled appendix. If you wish to discuss cross‑transfer inflation, compare like‑for‑like thresholds only (e.g., S>5 cross‑transfer vs. S>5 native).

MAJOR FINDINGS

P3-M1 (Abstract p. 1; Table I footnotes p. 7; Sec. II D p. 3–4)
Problem: Catalog‑grade subset counting ambiguity. Abstract recommends “~265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE), excluding LAMOST,” and explicitly distinguishes Planck map patches. Table I footnote, however, states “catalog‑grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938,” i.e., includes Planck patches. This contradicts the abstract and your own object/patch stratification.
Required fix: Define the catalog‑grade subset once (point‑sources only or not) and report one number consistently across abstract, main text, and Table I. If you include Planck in a “catalog‑grade” tier, justify why map patches are mixed with point sources, and provide separate counts for point‑sources and patches everywhere.

P3-M2 (Sec. III A p. 4)
Problem: Untraceable rate ratios. “Galaxies are flagged at ~20× the QSO rate (0.75% vs 0.037%); anomalies peak at z ~ 0.75 vs z ~ 0.93...”. No denominators or per‑class sample sizes are given, and the statement is partially duplicated on the same page (near‑verbatim paragraph repetition).
Required fix: Provide the per‑class totals (Ngal, Nqso) and anomaly counts so the rates can be verified, add uncertainties (binomial or Poisson), and remove duplicate prose.

P3-M3 (Sec. II A p. 2; III A p. 4)
Problem: Per‑arm residuals rB, rR, rZ are used repeatedly (and in Fig. 6/III B candidate selection) but never precisely defined. “Computed over [wavelength ranges]” is not sufficient for reproducibility.
Required fix: Provide explicit formulas for rB, rR, rZ (normalization, weighting, noise model, handling of masked pixels/sky lines), and release code that reproduces these sub‑scores.

P3-M4 (Sec. IV A p. 8–9; Fig. 5 p. 9)
Problem: Novelty accounting is scattered and key claims are unsupported in the PDF. The 0.2% SIMBAD and 12.7% NED rates for “top 10,000 DESI anomalies” and the “0% of top‑100 appear in any database” are not documented in a table or supplement; neither is the 20‑catalog CDS X‑Match list used for the 17.8% “genuine novelty” computation (though partly named in text).
Required fix: Add a table with the full cross‑match results (counts, fractions, search radii) for the DESI top‑1,000 and top‑10,000, and list the exact 20 catalogs used with their versions. Provide how duplicates across catalogs were resolved and report estimated spurious‑match rates (and uncertainties).

P3-M5 (Sec. III F p. 6; Table V p. 15)
Problem: CMB method reproducibility. The native Planck CAE is only described briefly (3 conv layers + FC 128, 1.1×10^6 params). No architecture diagram/hyperparameters (kernel sizes, strides, padding, activation functions, loss scaling), data standardization, training schedule, or masking pipeline details are provided.
Required fix: Include a methods appendix with full CAE architecture details and preprocessing (beam, mask, standardization, augmentation), and training hyperparameters sufficient to reproduce the 0.4437 validation loss and the top‑200 list.

P3-M6 (Sec. III E p. 6–8; Table III p. 8)
Problem: eROSITA anomaly thresholding. You define the 298 published anomalies via a “score‑knee” at S>0.259 but do not specify an objective knee‑finding algorithm. The equivalence to “top 0.03%” is asserted but not shown.
Required fix: Specify the knee‑finding procedure (e.g., Kneedle, derivative threshold, mixture model), show the score CDF with the knee marked, and provide sensitivity of the count to ±ΔS near the knee.

P3-M7 (Sec. IV C p. 10–11; Fig. 6 p. 11)
Problem: Cross‑survey matches: lack of matching protocol details. You report 637 multi‑survey clusters at 5″, but do not specify handling of proper motion (Gaia), multiple matches in crowded regions, or redshift/photometric consistency checks.
Required fix: Describe the matching algorithm (priority order, tie‑break rules, use of Gaia PM corrections, per‑survey astrometric uncertainties), and provide a confusion matrix of pairwise overlap counts.

P3-M8 (Sec. II D p. 3–4; Table I p. 7)
Problem: “Gate PASS/FAIL” framework is not standard and lacks pre‑registration. The six‑step “Path‑C” protocol, gate thresholds (e.g., ≥50% recovery at 5σ), and acceptance criteria are introduced ad hoc after showing cross‑transfer failures.
Required fix: Recast this as a pre‑declared validation protocol: define each gate, its statistical justification, and how it affects inclusion/exclusion a priori. Move cross‑transfer diagnostics to an appendix and present only native, gate‑validated results in the main text.

P3-M9 (Sec. II B p. 2–3; Fig. 2 p. 5)
Problem: The anomaly score S is repeatedly described as “validation z‑units,” but Figure 2 shows cross‑transfer SDSS S up to 1.9×10^11. While mathematically possible (MSE scaled by σval), calling these “z‑scores” invites misinterpretation.
Required fix: Clarify that S is a standardized residual relative to the training‑validation set and that in cross‑transfer regimes the scale is not interpretable as a Gaussian z‑score. Consider renaming to “standardized MSE” in such contexts.

P3-M10 (Appendix E, p. 16–17)
Problem: Savage–Dickey Bayes factors require careful density estimation at a point. You quote BMB/free = 3.23 and BSMBHB/free = 4.52×10^-4 with a uniform γ prior [0,7], but do not document how the posterior density at γ=3.0 and 4.33 was estimated (KDE bandwidths, boundary corrections).
Required fix: Provide the exact KDE method and bandwidth selection used to evaluate posterior densities at fixed γ (and prior densities), with uncertainty estimates on the Bayes factors (e.g., via bootstrap).

MINOR FINDINGS

P3-m1 (Sec. II D p. 4)
Problem: Duplicate phrase. “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)”.
Required fix: Remove the duplicate clause.

P3-m2 (Sec. III A p. 4)
Problem: Paragraph duplication. The “Across the 6.5 million spectra…” paragraph repeats content already stated just above (rates and Z‑dominant objects).
Required fix: Merge and de‑duplicate.

P3-m3 (Fig. 1, p. 4; Table I, p. 7)
Problem: Figure shows ACT DR6 points in the legend despite ACT being “quarantined,” which can mislead casual readers.
Required fix: Gray out ACT symbols and add “Quarantined: cross‑transfer artifact, excluded from results” directly on the figure/caption.

P3-m4 (Sec. III H, p. 8)
Problem: NEOWISE top anomaly “score = 11.5” is large relative to “top‑1%” selection; no context of score distribution is given for NEOWISE.
Required fix: Add a small panel/histogram showing the NEOWISE S distribution with the 99th percentile and the example’s score marked.

P3-m5 (Sec. II B p. 2)
Problem: Training set sizes and validation splits are given, but not random seeds for all surveys; DESI provides seeds later, others do not.
Required fix: Provide seeds for all training/validation splits or commit to releasing the exact index lists.

P3-m6 (Sec. IV B p. 9–10)
Problem: Spatial χ^2 uniformity test uses Nside=64 (38,330 pixels) without stating effective sky masks per survey; result is dominated by footprint inhomogeneity (as you note).
Required fix: Move χ^2 numbers to an appendix and retain the dust and |b| correlation tests as the main result, or provide footprint‑weighted expectations.

P3-m7 (References [12], p. 19)
Problem: “(2026, in press)” for Nicolaou et al. Provide an arXiv number or DOI. “Heinrich et al. [33] (publication‑year 2024; bibkey label retained as Heinrich2023…)” is internal bookkeeping; avoid such notes in the reference list.
Required fix: Normalize references to standard PRD style (no internal notes).

NITS

P3-n1 (Throughout)
Problem: Excessive internal jargon (“quarantined”, “gate PASS/FAIL”, “checkpoint”, “Path‑C”) in the main text.
Required fix: Define once and use sparingly; otherwise move process‑control language to a methods appendix.

P3-n2 (Abstract p. 1)
Problem: “Dated: June 2026” is fine, but avoid “largest‑scale”/“largest” claims unless bounded (e.g., “to our knowledge”) and backed with a formal comparative table.
Required fix: Qualify the claim or include a short comparative table versus [10–12] with counts.

P3-n3 (Sec. II B p. 2)
Problem: Parenthetical “z‑scored” vs. astrophysical z explanation is overlong for the methods section.
Required fix: Condense to a footnote.

Arithmetic/consistency spot checks (passed)
- 378,280 unique = 388,493 survey detections − 10,213 dedup = 378,280; compression 2.629% (correct).
- 378,080 point‑source = 378,280 − 200 Planck patches (correct).
- 141× = 378,080 / 2,685 (Liang et al.) (correct).
- 73× = 195,829 / 2,685 (correct).
- NEOWISE polar cap excess: 17/436 = 3.90% vs. 1 − cos 10° = 1.52%; ratio ≈ 2.57 (~2.6×) (correct).
- SIMBAD false matches: n ≈ 3e−5 arcsec−2, r=5″ → pfalse ≈ 2.36×10−3; ×195,829 ≈ 462 (correct).
- Landy–Szalay αjk = 0.19 ± 0.65 → |Z| = 0.29 (<1σ) (consistent).
- Fisher envelope [3.92, 8.98] matches α ∈ [−0.46, +0.84] with F0=1/8.982^2 and c=0.0747 (consistent once F0 is corrected).
- NANOGrav deviations: (3.0−2.567)/0.382 = 1.13σ; (4.33−2.567)/0.382 = 4.61σ; log10(7.14×10^3)=3.85 (consistent).

Length/scope
The manuscript is long (20 pages) and mixes survey‑engineering details with cosmological forecasts. For PRD, focus should be on statistically rigorous methodology and cosmological implications. The cross‑transfer diagnostics, gate process language, and survey‑specific catalog housekeeping could be condensed or moved to appendices. A streamlined main text of ~12–14 pages is recommended.

## Summary recommendation
MAJOR REVISIONS

Justification: There are multiple essential issues that undermine methodological clarity and reproducibility: a dimensional error in the Fisher baseline (F0), inconsistent and incorrect use of “top‑1%” and thresholds (notably for SDSS), unresolved figure references, irreconcilable compute‑time numbers, and inconsistent σ(fNL) baselines presented without comparability warnings. Data/code availability also does not meet PRD standards in its current “private until acceptance” form. These are fixable, but substantial revisions are required to meet PRD’s methodological rigor.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL FINDINGS

P3-E8 (Sec. IV B, p. 9–10)
Problem: Nside pixel-count/d.o.f. inconsistency. The text reports “38,330 HEALPix pixels (Nside = 64)” and uses dof = 38,329 in the χ2 test. For Nside = 64, Npix = 12 Nside^2 = 49,152, not 38,330. If 38,330 is after masking, the mask fraction and effective Npix must be stated, and the d.o.f. recomputed accordingly.
Required fix: Either (a) correct Npix to 49,152 and recompute χ2, dof, and χ2ν, or (b) document the exact sky mask that yields 38,330 pixels and recompute dof = Neff − 1 consistently. Provide the mask area fraction.

P3-E9 (Sec. III F, p. 6; Table I/score conventions)
Problem: Planck anomaly “score range [0.558, 0.621]” is incompatible with the globally defined anomaly score S in Eq. (2), which is a standardized residual (z‑like) and elsewhere takes values > 5 at the anomaly threshold. The Planck CAE values look like raw MSEs, not canonical S.
Required fix: State explicitly which score axis is used for Planck (raw MSE vs canonical S) and, if not S, convert to the canonical S definition or clearly flag that Planck scores are not comparable to the other surveys. Update Table I/Section II B to reflect this exception.

P3-E10 (Internal cross-references to caveats; Table IV vs body text)
Problem: Mixed and inconsistent caveat labels. The paper cites “§VI D (i)” in some places, but “§VI D (v)” and “§VI D (f)” elsewhere, while Table IV enumerates caveats (a)–(j). There is no “(v)” index in Table IV.
Required fix: Standardize caveat labels across the paper (either letters a–j or numerals i–x) and correct all cross-references so each citation unambiguously points to an entry in Table IV or a clearly labeled subsection.

P3-E11 (Sec. II D Step 5, p. 3–4; Sec. III H p. 8; Fig. 7 p. 13)
Problem: Inconsistent injection–recovery sample sizes and definitions. Step 5 states “500 planted signals per survey at six amplitude levels,” but NEOWISE reports “1000/1000 = 100%,” and Gaia/eROSITA primarily report cross‑validation stabilities rather than injection recovery at 5σ. The NEOWISE “mask injection” is not a standard signal injection into features but a region cut.
Required fix: Harmonize the injection protocol across surveys or clearly separate (a) true feature‑space signal injection tests (with N injects per amplitude), (b) map‑mask tests, and (c) cross‑validation stability surrogates. Report actual Ninject per survey and amplitude, and keep the “≥50% at 5σ” gate only for the surveys where a true injection test was performed.

P3-E12 (Sec. III C, Fig. 3)
Problem: Body–figure mismatch on SDSS clustering. The text claims “3 latent-space populations (Fig. 3), dominated by cool dwarfs (84%),” while the figure panel labeling (and legend text in the figure) indicate many clusters (e.g., 14 clusters, 99.4% clustered). The numerical cluster count and fractions do not match the body statement.
Required fix: Reconcile the described number of clusters with what Fig. 3 actually shows. If “3 populations” are super-clusters composed of multiple HDBSCAN clusters, say so and provide both the fine (cluster) and coarse (population) counts and fractions.

P3-E13 (Sec. II C p. 3; Table V p. 15 — beyond Planck CAE)
Problem: Implausible training times beyond the already flagged Planck row. Reported “Train time (s)” entries of 7.6 s (eROSITA, 120k params, up to 200 epochs), 1.2 s (Gaia, 80k params), and 1.6 s (NEOWISE, 70k params) are not credible for the stated training schedules and dataset sizes on an A100, even with tiny models; these look like inference or data‑loading snippets, not end‑to‑end training.
Required fix: Provide reproducible logs showing epochs, wall‑clock per epoch, total epochs to early stop, and hardware; separate CPU preprocessing and GPU training time. If the reported numbers are inference or a single epoch, relabel them accordingly and add true training wall‑clocks.

P3-E14 (Sec. IV A p. 8–9; Abstract p. 1)
Problem: Contradictory novelty phrasing. The body claims for DESI “none of the top 100 appear in any database,” whereas later it shows that 82.2% of the top‑1,000 have archival IDs across 20 catalogs. “Any database” appears to mean only the six named in §III A (SIMBAD, NED, AllWISE, Milliquas, Gaia DR3, SDSS), but this is ambiguous and reads as a blanket novelty claim.
Required fix: Replace “none of the top 100 appear in any database” by the precise statement relative to the exact catalog set searched (list them), and immediately note that an extended 20‑catalog search yields 82.2% archival identifications at the top‑1,000 stratum.

MAJOR FINDINGS

P3-M11 (Sec. IV D, p. 10)
Problem: Scientific inference drawn from quarantined ACT anomalies. The main text concludes that the Planck×ACT cross-correlation “demonstrates CMB patch anomalies are dominated by survey-specific systematics,” yet this uses the ACT cross‑transfer set explicitly labeled as failing both gates and “not a science result” (Appendix F).
Required fix: Move the Planck×ACT cross-correlation to Appendix F with an explicit “methodological only” disclaimer in the main text, or redo the test with a gate‑passing ACT native retrain. Remove/main‑text claims that rely on quarantined data.

P3-M12 (Appendix E, Eq. E1 p. 16)
Problem: Dimensional/normalization ambiguity in the PTA likelihood model. The symbol ρi is introduced via a log‑power relation including factors of 12π^2, fyr, fi, and Tobs without defining the physical quantity (per‑bin PSD? strain power?), its units, or the discretization convention that brings Tobs into the formula.
Required fix: Define ρi precisely (units, relation to standard PTA S(f) or h2c), state the binning and normalization (one‑sided/two‑sided PSD, factors of Tobs/Δf), and provide a citation that matches the exact convention. Ensure both sides of Eq. (E1) are dimensionally consistent.

P3-M13 (Sec. II D p. 3–4; Sec. IV C p. 10)
Problem: Dedup “friends‑of‑friends” can percolate. A 5″ friends‑of‑friends union‑find without an explicit maximum cluster radius can chain multiple near‑neighbors into clusters whose terminal separations exceed 5″, especially in crowded fields, biasing the 637 multi‑survey coincidences and the 10,213 total merges.
Required fix: Specify whether a hard maximum cluster radius is enforced or only pairwise links; if the latter, quantify cluster radii and re‑run with a non‑percolating rule (e.g., maximum MST edge ≤ 5″ and maximum cluster diameter ≤ 5″) or show that the observed clusters do not percolate beyond 5″ diameter.

P3-M14 (Sec. V, Table IV (i), Appendix C/Fig. 8)
Problem: c‑coefficient derivation opaque. The text uses a “5‑α refit” to set c in 1/σ(fNL)^2 = F0 + c α^2 but does not state which α values, tracer configuration, redshift bins, or Fisher setup were used to obtain c = 0.0747.
Required fix: Provide the exact α grid, survey/tracer configuration, kmax, binning, nuisance parameters, and the resulting fit (plot 1/σ^2 vs α^2) so readers can reproduce c. State uncertainties on c.

MINOR FINDINGS

P3-m8 (Sec. III A p. 4)
Problem: SNR–score decorrelation test under‑specified. The reported Spearman ρ = −0.03 (p = 0.12) comes from a “stratified subsample of 2,670 spectra, log‑uniform in SNR” without stating the random seed, SNR binning, or selection procedure.
Required fix: Provide seed, stratification procedure, and bin counts, or release the exact index list.

P3-m9 (Sec. II D p. 4; Appendix D p. 16)
Problem: “PASS > 0.90” thresholds (e.g., UMAP trustworthiness) appear post‑hoc. While acceptable as heuristics, they should be declared in a methods appendix, not embedded as implicit pass/fail language in results.
Required fix: Move such heuristic thresholds to a methods/validation appendix with justification or prior citations.

P3-m10 (Wording; Sec. III E p. 6)
Problem: “eastern half under Rosatom proprietary control” is editorial and unnecessary.
Required fix: Replace with neutral phrasing (e.g., “the eastern hemisphere is not yet publicly released”).

P3-m11 (Sec. IV A p. 8–9; Table I footnotes)
Problem: Roman vs lettered caveat labels also leak into footnotes (e.g., “§VI D caveat (v)”), which do not exist in Table IV’s scheme.
Required fix: Covered by P3‑E10; ensure footnotes are corrected too.

P3-m12 (Fig. 2 caption vs axis labels)
Problem: Right panel y‑axis labeled “Prob. density” on a log–log plot spanning 12 orders of magnitude; the caption describes a “score distribution” but does not specify whether curves are PDFs or histograms normalized to unity.
Required fix: State explicitly whether the plotted quantity is a normalized PDF or a histogram count, and ensure axis labels reflect that choice.

NITS

P3-n4 (Throughout)
Problem: Occasional internal code/package names (“Ceffyl KDE chain”) appear in prose without citation or footnote.
Required fix: Add a reference or footnote at first mention, or replace with a generic description (e.g., “published KDE free‑spectrum likelihood”).

P3-n5 (Typos/grammar)
Problem: Minor wording issues (“supersedes” vs “supersede,” repeated commas, occasional tense/agreement slips).
Required fix: Copy‑edit.

Explanation
This fresh pass focused on arithmetic consistency, figure/body agreement, equation dimensionality, cross‑reference integrity, and use of quarantined data. Several new inconsistencies were found (HEALPix pixel counts/d.o.f.; Planck score axis; caveat label mismatches; injection‑recovery protocol coherence; SDSS clustering counts; training‑time plausibility; novelty phrasing; dedup percolation risk; opaque Fisher c‑fit). These are in addition to the issues identified in the initial review and should be addressed for PRD‑level methodological rigor.