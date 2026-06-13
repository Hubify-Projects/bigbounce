# P4 R36conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v180.pdf` md5=26c9c91f pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6566 chars)
**Wall time**: 363.8s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

General assessment
- Scope/claim: The manuscript presents a very large chirality-labeled catalog (8.47M galaxies; 3.20M spirals), a real-space dipole measurement consistent with null (+0.41σ), a WLS template-fit exclusion of a 1.7% dipole (z ≈ −18), and a quantitative demonstration that a small global monopole coupled to a patchy mask reproduces ≈99.3% of the pre-MASTER pseudo-Cℓ ℓ = 1 power. The authors repeatedly emphasize estimator hierarchy and non-comparability of σ across distinct nulls.
- Methodology strengths: The declared estimator hierarchy, explicit null procedures (pixel-permutation vs per-galaxy label-shuffle), consistent reporting of moment-z vs rank-p, and extensive systematics audits are commendable. Many scalars in the abstract and conclusions do trace back to tables and text, and I could re-derive representative numbers (binomial errors, dipole z from quoted null moments, leakage fraction, Fisher floor).
- However, the manuscript contains extensive internal versioning/audit prose and in-repo artifact path references interleaved throughout the main text, along with withdrawn-run commentary, which is not acceptable for PRD. Several quantitative claims central to the conclusions are only documented by pointers to JSON artifacts rather than by figures/tables in the paper. There is also a provenance inconsistency between the paper version (v1.0.180) and the pinned commit (v1.0.175) that must be resolved before publication. Finally, some effect-size claims (edge-on contamination penalty; harmonic-channel completeness) are asserted without an in-paper derivation/figure.

Below I itemize findings.

ESSENTIAL findings (must be fixed for PRD acceptance)
P4-E1 (Multiple; pages 1–22): Internal version history, “withdrawn result” narrative, in-repo paths, and audit-log prose in the body text
- Problem: The manuscript repeatedly embeds internal-bookkeeping language and repository file paths (e.g., “artifact pipelines/p2_chirality/...json”), version-history commentary (“An earlier version of this paper reported... that result is withdrawn,” “earlier text mis-attributed...,” “post-R29”), seed numbers, and run logs across the abstract, main text, and appendices (e.g., Abstract p.1; Secs. III–VI; App. A–E).
- Required fix: Remove all internal run logs, file paths, version-history commentary, and audit-prose from the main text. If needed, consolidate provenance in a short “Note on withdrawn estimate” paragraph (one location) or a single appendix subsection without run logs and repository paths. Retain only scientific results necessary for reproducibility; move file-path details to a separate data release or supplementary material. Do not use “superseded/earlier draft/post-Rxx” phrasing in the paper.

P4-E2 (p.21 Data Availability vs. title page): Provenance inconsistency between version tag and commit hash
- Problem: Title page states v1.0.180 (June 12, 2026). Data Availability pins “commit 53b41d12 (v1.0.175, June 2026)” and asserts a two-step stamp-then-pin protocol that should differ by one commit. Here the difference is five versions (175 vs 180). This undermines exact reproducibility.
- Required fix: Freeze a single, exact, immutable release for the catalog, code, and analysis artifacts with a permanent DOI (e.g., Zenodo) and cite that DOI in the paper. The version identifier in the header and the commit/DOI in Data Availability must match exactly. If you keep a Git hash, it must be the exact commit that generated all reported results; remove the “stamp-then-pin” exception language.

P4-E3 (p.21 Data Availability): No persistent DOIs for code, model, and catalog
- Problem: The catalog/model are referenced by mutable HuggingFace/GitHub locations; Zenodo DOI is “not yet minted”. PRD requires citable, immutable artifacts at acceptance.
- Required fix: Archive the exact catalog, model weights, and code used for this paper to repositories that mint DOIs (e.g., Zenodo, institutional archive). Freeze the analysis configuration (masks, null settings) and provide a single DOI bundle. Update Data Availability with DOIs and remove promises of future minting.

P4-E4 (Sec. VI A; VII a; p.12–15): Injection-recovery/“completeness” claims not shown in-paper for the harmonic channel
- Problem: The abstract and Sec. VII(a) claim harmonic-channel completeness P(≥3σ) ≥ 0.999 at Ap ≥ 0.75% and enormous z for injections (median z ≈ 68–218 at Ap = 1.7%), but the paper contains no figure/table for these harmonic-channel injections (only a pointer to “artifact c9b”).
- Required fix: Include a figure or table in the manuscript showing the ℓ = 1 MASTER-channel injection-recovery curves (P(≥3σ) vs amplitude) and the distribution of recovered z for at least two amplitudes (e.g., 0.5%, 0.75%, 1.7%). This is load-bearing to the “unmissable” argument; it cannot live only as an artifact pointer.

P4-E5 (Sec. C Hemisphere look-elsewhere; p.18): Double-correction of LEE
- Problem: For the hemisphere scan the manuscript reports the principled direct-MC max-statistic pLEE ≤ 10−4 (correct) and then additionally applies Bonferroni/Benjamini–Hochberg to the same 648-direction set, reducing the post-LEE significance to < 1σ. This is a double-penalty and confuses the statistical interpretation (the direct-MC max-statistic already accounts for the trials and their correlations).
- Required fix: Choose a single, principled LEE procedure. Report the direct-MC max-statistic pLEE as primary. If you wish to show per-direction uncorrected p-values with BH as a heuristic check, present them separately and explicitly label them as secondary, not a second LEE correction applied to the max-statistic.

P4-E6 (Units; Table III caption p.11): Cℓ “sr” units misuse
- Problem: The caption states “Ap-map ×10−6 sr scale” for Cb amplitudes. For a dimensionless scalar field, Cℓ is dimensionless under the usual HEALPix/NaMaster conventions (up to a normalization choice), not “per sr”.
- Required fix: Correct the units language. If you rescale Cb by 10−6 for presentation, state “values shown in 10−6 units” and remove “sr.” If you use a non-standard normalization, define it precisely.

MAJOR findings
P4-M1 (Abstract p.1 and throughout): Length and density; excessive in-line provenance
- Problem: At 22 pages, much of the narrative is devoted to run-by-run provenance, seed counts, and artifact paths that obscure the methodological core. PRD Methods papers should be concise and self-contained.
- Required fix: Substantially condense the main text. Move low-level run bookkeeping to a dedicated, short “Reproducibility notes” appendix or an external data-release note. I recommend ≤15 pages for main text plus appendices, eliminating repeated artifact/path references. Keep only results that inform methodology and conclusions.

P4-M2 (Sec. VI A; p.13): Edge-on contamination penalty asserted without calculation
- Problem: The paper asserts “edge-on galaxy contamination ... reduces effective sample size by ∼10–15%, corresponding to a ∼5–8% sensitivity penalty,” but no derivation/numbers are shown.
- Required fix: Provide the calculation (or a short derivation) that maps the measured edge-on fraction and class-confusion to an effective-sample-size reduction and the implied sensitivity penalty. A short table or worked example suffices.

P4-M3 (Sec. II B; App. B; p.2,16): Training/augmentation accounting unclear
- Problem: The training set description says 25,790 source images; after flip augmentation of the training split, the “combined pool is 26,616” (80/20 → 21,293/5,323). It is unusual to frame augmentation as increasing the dataset count by +826, and it is unclear whether validation images were augmented.
- Required fix: Clarify precisely which splits were augmented, which transformations were applied, and how the 826-image delta arises. State explicitly whether validation data were augmented (they should not be) and whether augmented copies are counted as separate samples for bookkeeping only.

P4-M4 (Sec. VII e; p.15): Ambiguous “≥107 galaxies”
- Problem: The falsification boundary line says “≥107 galaxies,” which is ambiguous (could be 107 rather than 10^7).
- Required fix: Typeset as 10^7 (or “ten million”) unambiguously.

P4-M5 (Throughout): Mixed σ from different null procedures; add explicit non-comparability reminder at each juxtaposition
- Problem: While the manuscript often stresses non-comparability of σ across different nulls, there remain a few side-by-side juxtapositions without an immediate qualifier (e.g., Sec. VI opening: 2.31σ real-space vs +6.48σ pre-MASTER; Sec. VII(a): z≈68–218 vs observed +7.28σ).
- Required fix: Add a short parenthetical at each such juxtaposition explicitly stating “different fields and nulls; not directly comparable” (as done elsewhere). This is a PRD-standard clarity requirement.

MINOR findings
P4-n1 (Sec. VI A; Eq. 4; p.12): Notation clarity for σ(A)
- Problem: In-line typesetting of “σ(A) = s 3/Nspiral” is slightly ambiguous in the parsed text; presumably √(3/Nspiral).
- Required fix: Ensure the square root is clearly typeset, e.g., σ(A) = √(3/Nspiral) = 2√3 σ(fCW).

P4-n2 (Sec. III D; Fig. 2; p.6): Minor notation typos
- Problem: Occasional artifacts like “ˆ zˆ,” “C 2 2◦,” and extra spaces appear.
- Required fix: Clean typography (single hat, consistent apodization notation “C2, 2°”).

P4-n3 (Sec. IV B; p.5–6): Monopole uniformity statements could carry numeric summaries in-text
- Problem: The slab ranges are stated (e.g., fCW spans 0.49537–0.49890) but not the corresponding per-slab |z| values.
- Required fix: Add a brief parenthetical: “max |z| ≈ 2.7 per slab” (as already computed later) for immediate context.

P4-n4 (App. A c; p.16): “Effective sky fraction” definitions
- Problem: The definition is given carefully, but a one-line reminder that NaMaster uses the exact coupling matrix, i.e., feff_sky is descriptive only, would help (it is said later).
- Required fix: Add “Note: NaMaster uses the exact coupling matrix; feff_sky is descriptive and not used in decoupling.”

P4-n5 (App. B d; p.17): T7 “calibration proxy” wording
- Problem: The implemented T7 is a heuristic proxy, not ECE. Current wording is acceptable, but a one-sentence clarification that this is not a calibrated reliability curve would help.
- Required fix: Add “T7 is a coarse proxy; we do not claim a calibrated reliability curve absent per-object truth.”

NITs (cosmetic)
P4-N1 (Throughout): Hyphenation artifacts “Hugging￾Face”, “apod￾ization”
- Fix: Clean hyphenation.

P4-N2 (Abstract; p.1): “to our knowledge, the largest ...” novelty phrasing
- Fix: Consider softening by giving a direct comparison to CE-ResNet scale (you already do later).

Arithmetic and internal-consistency spot checks
- Catalog counts: 1,592,107 + 1,609,053 + 5,273,371 = 8,474,531; Nspiral/Ntotal = 3,201,160/8,474,531 ≈ 0.37778 → 37.78% (as stated).
- Table II binomial errors: For Catalog A, σ ≈ √(0.507879×0.492121/3,321,795) ≈ 0.000274; deviation (0.507879–0.5)/σ ≈ 28.7σ. For Catalog C, σ ≈ 0.000279; deviation ≈ −9.5σ. Matches.
- Real-space HC dipole: NMC = 10,000 permutations; z = +0.41; rank-p = 0.31 (stated); per-galaxy label-shuffle variants z ≈ 0.58 and 0.70 in independent implementations (text supports abstract’s 0.70).
- MASTER apodized ℓ=1: Cdata = 2.348×10−5, null mean 1.71×10−6, σ = 2.99×10−6 → z ≈ 7.28 (matches).
- Canonical unapodized 10k-permutation: 7.27×10−6 vs 0.57×10−6 ± 0.84×10−6 → z ≈ 7.93 (Table III).
- Monopole+mask pre-MASTER leakage fraction: 1.6846/1.6961 ≈ 0.9932 → 99.32%; z = (1.6961−1.6846)/0.0068 ≈ 1.69 (Table IV). Matches.
- Fisher floor: √(3/Nspiral) with Nspiral = 3,201,160 → 9.7×10−4; 3σ ≈ 0.29%. With N = 949,584 → 1.78×10−3 (3σ ≈ 0.53%). Matches.
- WLS template fit: Abest = 4.55×10−3 (Ap units) → 0.2275% in fCW units; σboot = 1.63×10−3; z vs Aref = 0.034 is ≈ −18.1. Matches.
- Hemisphere max-stat under the monopole-only null: 3.484×10−3 vs 1.693±0.405×10−3 → z ≈ 4.42. Matches.

Abstract-last drift sweep
- All headline numbers in the abstract are traceable: N, counts, +0.41σ (HC dipole), z ≈ −18 WLS exclusion, 99.32% pre-MASTER leakage reproduction, +3.64σ canonical vs +7.28σ apodized residuals (with a parenthetical explaining they are diagnostics and from different runs), A50 ≈ 0.75% and A95 bracket (1.0–1.5%); the explicit caveat that harmonic-channel completeness is diagnostic and not interchangeable with the real-space falsification boundary is present. No overclaim detected.

Bibliography spot checks
- Shamir (2012) Phys. Lett. B 715, 25; arXiv:1207.5464 — OK.
- Jia et al. (2023) ApJ 943, 32; arXiv:2210.04168 — OK.
- NaMaster (2019) MNRAS 484, 4127 — OK.
- DESI Legacy Surveys AJ 157, 168 (2019) — OK.
No inconsistencies found.

## Summary recommendation
MAJOR REVISIONS

The methodological core is strong and many numerical claims check out, but the manuscript in its current form is not suitable for PRD due to (i) pervasive internal versioning/audit language and repository path references in the main text, (ii) unresolved provenance inconsistency between the stated paper version and the pinned commit, (iii) lack of in-paper figures/tables for some load-bearing injection-recovery results (harmonic-channel completeness), and (iv) a few unquantified effect-size assertions that require short derivations. Clean these issues, consolidate and condense the presentation, mint DOIs for all released artifacts, and the paper would be suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (additional to prior report)

ESSENTIAL
- P4-E7 (Significance reporting under heavy-tailed nulls; Table III and related text): For the apodized MASTER ℓ=1 diagnostic you quote zmom ≈ +7.3 while the permutation rank p ≈ 6×10−4 corresponds to ≈3.2σ Gaussian-equivalent. You do note heavy tails, but the paper inconsistently leads with moment-z in some places and rank-p in others. Required fix: For every estimator whose null is demonstrably non-Gaussian, specify a single primary significance metric (recommend rank-p), and relegate moment-z to a secondary diagnostic. State this choice explicitly in Sec. III A and apply it consistently anywhere both are shown (Table III, Sec. IV C–D, Sec. VII c).

- P4-E8 (Mask/field support mismatch on the apodized footprint): Appendix A.a states that the MASTER diagnostic on the Nall ≥ 1 footprint uses Wp = Nall, and pixels with Nspiral = 0 carry Ap = 0 and are excluded only from the mean-subtraction support, not from the field. That leaves a mismatch between the field’s effective support (Nspiral ≥ 1) and the weight mask (Nall ≥ 1). Such support mismatches can bias mode-coupling estimates and error bars. Required fix: Either (i) set Wp = 0 wherever Nspiral = 0 so the mask and field supports are identical, or (ii) demonstrate in-paper invariance of the ℓ=1 result to replacing the weight mask by the support intersection (Nall ≥ 1 ∩ Nspiral ≥ 1). Include a small table/figure showing z (or rank-p) under both choices.

- P4-E9 (Ambiguous “103 injections” vs 10^3): Sec. VII(a) says the MASTER-channel completeness used “103 injections per amplitude per axis,” which reads as 103, not 10^3. With 103 realizations one cannot resolve ≥0.999 completeness. Required fix: Correct all such exponent typos (use 10^3 consistently) and state the exact number of realizations used per amplitude and per axis.

- P4-E10 (“UL95” naming implies coverage): Sec. IV C labels the 95th percentile of the pixel-permutation null as “AUL95,” then explains it has no coverage guarantee. Required fix: Rename to a non-coverage term (e.g., “A95,null-quantile”) wherever it appears, or explicitly label it as “non-coverage reference quantile” to avoid misinterpretation as a statistical upper limit.

MAJOR
- P4-M6 (Weight-map robustness is asserted, not shown): Sec. IV C claims the apodized MASTER ℓ=1 excess “persists under all three weightings,” quoting z shifts at the ±1σ level, but gives no in-paper table/figure (only artifact pointers). Required fix: Add a compact table showing, for the apodized footprint, C1, ⟨C1⟩null, σnull, and rank-p for Wp ∈ {binary, Nspiral, Nall}. This underpins your claim that the excess is not an artifact of the weight choice.

- P4-M7 (Apodization-length insensitivity is asserted, not shown): Appendix A.c asserts numerical stability and “insensitivity to apodization length” based on condition numbers. Required fix: Add a small table (or a one-panel figure) of the recovered ℓ=1 value and rank-p for apodization lengths 1°, 2°, and 3° (same null procedure), to substantiate the statement operationally.

- P4-M8 (Slab-statistics baseline confusion): Sec. IV B mixes deviations from 0.5 (e.g., −0.463%) with later claims that “slab-to-slab scatter about the global fCW = 0.49735 is ≲ 2.7σ per slab,” where the σ evidently uses the baseline 0.49735, not 0.5. Required fix: Clarify the baseline for each z (vs 0.5 or vs the global catalog rate) and give both max |Δf| and the corresponding |z| with the same baseline in the same sentence to avoid ambiguity.

- P4-M9 (Standardize null nomenclature): The manuscript alternates among “isotropic bootstrap,” “pixel-permutation,” and “per-pixel label-shuffle” nulls. Required fix: Define each distinct null once (Sec. III A) with a unique name and use those names consistently throughout (real-space vs harmonic-channel nulls, and whether permutations are across pixels or within-depth strata).

- P4-M10 (Consolidate primary z for HC real-space dipole): The paper quotes slightly different HC real-space dipole significances depending on the run (e.g., +0.41σ in main text/abstract; +0.48σ after excluding QC-flag rows; +0.52σ under an alternate 10^4-permutation convention). Required fix: Pick one canonical setup (mask, sample, null size, seed policy) for the primary HC estimator and report that single value in abstract, main text, and Data Availability. Move all other variants to a brief robustness table to eliminate “number drift.”

MINOR
- P4-n6 (Equation and derivation clarity in Fisher floor): Eq. (4) is dimensionally consistent, but the inline typesetting “σ(A) = s 3/Nspiral” is ambiguous in the parsed text. Also, the identity σ(A) = 2√3 σ(fCW) is used; add one sentence showing the steps (p = 1/2 at A = 0 ⇒ Var(fCW) = 1/4N, ⟨cos^2⟩ = 1/3 ⇒ Var(A) = 3/N). This avoids any dimensional or normalization doubt.

- P4-n7 (Typo in Appendix D.g): The line “z ≈ −18.1.34” appears to splice a footnote marker into the number. Fix to “z ≈ −18.1” with the footnote marker placed correctly.

- P4-n8 (Table II formatting consistency): The Catalog B row lists “0.504 ± 0.0003” with fewer significant digits than the A and C rows. Harmonize formatting/significant digits across rows.

- P4-n9 (Hemisphere scan reporting): Appendix C.c gives the max-hemisphere asymmetry as 3.05σ against a label-shuffle null but does not provide the rank-p for that individual maximum before LEE. Add the one-sided rank-p for the observed maximum (before LEE), then the direct-MC max-stat pLEE (primary), and refrain from mapping moment-z to Gaussian σ for that statistic (heavy-tailed null).

- P4-n10 (Figure 8 caption vs body): The caption now clarifies that the per-ℓ σ come from the “canonical 200-MC battery,” while the body discusses a 500-MC direct run and a 10k-permutation recompute for related channels. Add one sentence to the caption referencing that the plotted σ are from the 200-MC battery, not the 500/10k runs cited elsewhere, to preempt confusion.

- P4-n11 (Baseline definition in slab paragraph): When stating the equal-area partition “max |z| = 2.9 vs. the global rate,” explicitly give the per-band N and the corresponding binomial σ so readers can reproduce the 2.9 number on the spot.

NO REPEATS
- I did not re-list issues already in the first report (e.g., removal of internal run logs and file paths; DOI/provenance; units “sr” for Cℓ; hemisphere double LEE; training/augmentation accounting; edge-on penalty derivation; harmonic-channel injection curves; comparability reminders; ambiguous 10^7), which remain to be addressed.