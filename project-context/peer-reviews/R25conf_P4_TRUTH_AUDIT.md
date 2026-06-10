# R25conf P4 — TRUTH AUDIT (post-retraction clean-round 2-of-2 determination)

**Auditor**: Claude (in-session), 2026-06-10, against `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.169 working tree, post in-session polish)
**Scope**: all R25conf SYNTHESIS + META_REVIEW findings (Claude_brutal ×2, Gemini 0 findings, Grok, OpenAI, Perplexity, META).
**CLOSED-PRIOR (STALE)**: in-session leg E1 (Table III caption → App A.b cross-ref), E2 (§VII.e θ-uniform parenthetical), m1 (Table I em-dash note), m3 (equal-area slab); m2 = HOUSTON-DECISION (abstract density, skipped).
**Ground truth used**: `outputs/dipole/catalog_c_summary.json` (0.41σ/p=0.31; shuffle 0.58σ/0.26), `c11_meta_e1_e2_realspace_nulls.json` (3,200,420 in-mask; 0.00566 amp; z 4.16/4.32/4.38), `c9a_10k_nulls.json` + `h200_scripts/experiments/c9a_p4_10k_nulls.py` (per-footprint field conventions), `c9b_injection_completeness.json` (amplitudes_Ap=[.005,.0075,.017,.03]), `c9c_wp_sweep.json` (subtraction follows variant W_p), `scripts/injection_sweep_extended.py` (L104: `p_inj = p_cw_global + 0.5*A*cos_theta`), `scripts/joint_nuisance_bootstrap_sigma.py` (L167: `rng.choice(..., replace=True)`), `gpt5_b3_monopole_correction_audit.json`, `morphology_template_l1_projection.json`, inline `thebibliography`.

## ESSENTIAL

| ID | Claim | Verdict | Disposition |
|----|-------|---------|-------------|
| Claude E1/E2 (+INSESSION twins) | Table III cross-ref; θ-uniform back-ref | **STALE** | Closed in-session pre-audit. |
| META-E1 | A_p undefined where N_spiral=0 on N_all≥1 footprint; effective mask unstated | **VERIFIED** | Script-confirmed (c9a `build_A_sub_apod`: A=0 at N_spiral=0; mean over N_all≥1 ∩ N_spiral≥1 only). Support + zero-assignment + subtraction-domain sentence added to App A.a. **CLOSED (textual, script-backed).** No bias: mean subtraction excludes those pixels. |
| META-E2 | "Single declared data vector" contradiction (f_CW−0.5 vs A_p) | **VERIFIED — substantive** | c9a script/artifact: apodized rows use A_p + W_p=N_all-weighted subtraction; canonical rows use f_CW−0.5 (=A_p/2) + N_spiral-weighted subtraction. App A.a sentence and Table III "single field convention" caption were both wrong. Rewritten to the per-footprint truth; z/rank-p rescaling-invariance stated; C_b non-comparability across blocks stated. **CLOSED same-day (textual, artifact-backed; no number changes — z values untouched).** |
| Grok-E1 | Abstract +0.41σ unqualified vs other σ | **STALE/OPINION** | Each abstract σ names its null/mask inline; conventions paragraph + Table I/III captions; per-juxtaposition repetition rejected in R24conf (conflicts w/ OpenAI anti-repetition). |
| Grok-E2 | Remove withdrawn/audit language | **HOUSTON-DECISION** | Standing disclosure policy (retraction-note removal = Houston call). |
| Grok-E3 | "Largest catalog" unsupported | **PARTIAL→CLOSED** | Body cites largest known competitor (CE-ResNet 1.95M, 1.6×) + Shamir samples. "To our knowledge" added (abstract + conclusions). |
| OpenAI-E1 | Artifact paths/version history in body | **HOUSTON-DECISION** | Deliberate `\artifact{}` reproducibility convention. |
| OpenAI-E2 | A_p vs f_CW unit ambiguity | **PARTIAL→CLOSED** | Conversions already at Eq. 3, Figs 2/5, Table II; added the pure-dipole identity (A_p amplitude = full-amplitude A) at the A_95^UL quote. |
| OpenAI-E3 | A_UL95 mislabeled as upper limit | **PARTIAL→CLOSED** | Already "estimator-level rank construction, not signal-injected"; added "no frequentist coverage guarantee, used in no conclusion". |
| OpenAI-E4 | Abstract σ juxtaposition caveat | **STALE** | Same family as Grok-E1; abstract density = Houston (in-session m2). |
| OpenAI-E5 | No DOI; broken URLs | **HOUSTON-DECISION / FALSIFIED** | DOI-at-acceptance disclosed in Data Availability; "spaced URLs" = PDF line-break extraction artifact (xurl hyperlinks copyable). |
| OpenAI-E6 | 3,200,420 vs 3,201,160 unexplained (740) | **VERIFIED** | Artifact c11_meta_e1_e2 confirms both counts; clarifier added (740 spirals in below-threshold pixels). **CLOSED.** |
| OpenAI-E7 | Null nomenclature inconsistent | **STALE/OPINION** | Conventions paragraph; every value carries its null label. |
| OpenAI-E8 | +7.28σ doesn't state monopole-subtracted field inline | **VERIFIED** | Inline "(monopole-subtracted A_p field; declared data vector, Appendix A)" added at §IV.C. **CLOSED.** |
| Perplexity-E1 | σ mixing, local qualification | **STALE** | Same family. |
| Perplexity-E2 | Audit-trail language | **HOUSTON-DECISION** | Same as Grok-E2/OpenAI-E1. |

## MAJOR

| ID | Verdict | Disposition |
|----|---------|-------------|
| META-M1 (injection generative model unspecified) | **VERIFIED** | Script L104: `p_inj = p_cw_global + (A/2)cosθ`; artifact metadata identical. Explicit formula + baseline + no-clipping sentence added §VI.A. **CLOSED (script-backed).** |
| META-M2 (double LEE correction) | **STALE** | App C + Table I caption already declare direct-MC max-stat the principled control, BH/Bonferroni a deliberately conservative second heuristic (R24conf META-M1 close). |
| META-M3 (mean-subtraction weight mismatch N_all vs N_spiral) | **VERIFIED** | Requested check already exists: c9c sweep (subtraction follows variant W_p; N_spiral-weighted σ=+8.5, verdict unchanged). Clarifier added §IV.C that the sweep includes the field-consistent subtraction. **CLOSED (artifact-backed).** |
| META-M4 (T5 circular-RA Pearson invalid) | **VERIFIED** | Limitation sentence added App B: T5 not counted as independent directional-coupling pass; map-level Y_ℓm regression (all ℓ=1 coeffs null, |z|≤1.25) is the operative test. **CLOSED (textual).** |
| META-M5 (Table V no binomial errors, N=100) | **VERIFIED** | Binomial SE ≤0.05 sentence added Table V caption; A_50 declared grid-precision. Pure arithmetic from stated N. **CLOSED.** |
| Grok-M1 (length) | **HOUSTON-DECISION** | Already condensed 54→20pp. |
| Grok-M2 (σ qualifier every cell) | **STALE** | As Grok-E1. |
| Grok-M3 (+3.64σ residual cosmological fraction unquantified) | **STALE/PARTIAL** | App D: WLS template exclusion z≈−18, quality-quartile washout, 25% leg closure, cross-spectrum r=−0.65 = the quantitative disfavor package. |
| OpenAI-M1 (0.57% unit unspecified) | **VERIFIED** | Artifact amp=0.00566 from A_p-field fit → "(A_p-unit)" added. **CLOSED.** |
| OpenAI-M2 (200-MC diagnostics, 2-decimal σ) | **PARTIAL/QUEUED** | Already declared queued in App E ("threshold sweep under current convention queued with the 10,000-permutation recompute"); recompute-class. |
| OpenAI-M3 (z≈68–218 no in-paper table) | **PARTIAL/HOUSTON** | Values + completeness P(≥3σ) in Conclusions w/ artifact c9b; full table = format choice (R24conf verdict reaffirmed). |
| OpenAI-M4 (rotation-equivariance doc) | **OPINION** | §III.C + App B D₄ hold-out already population-level. |
| OpenAI-M5 (falsification criterion estimator unbound) | **STALE** | §VII.e: "floors of the real-space dipole estimator under its per-pixel-shuffle null" — explicit. |
| OpenAI-M6 (depth-modulated monopole caveat) | **STALE** | §IV.B additive-vs-multiplicative sentence (R24conf META-m4 close). |
| OpenAI-M7 ("isotropic" null naming; rotation null) | **PARTIAL/OPINION** | Null described exactly (permutation preserving one-point dist.); rotation null = recompute, robustness already via label-shuffle + independent reimplementation. Not substantive. |
| OpenAI-M8 (σ 1.85→3.64 while power falls) | **VERIFIED** | Arithmetic-implication explanation added App A (null mean/width shrink more under same subtraction). **CLOSED.** |
| OpenAI-M9 (648-grid latitude spec) | **VERIFIED→QUEUED** | Generating script not in repo (searched scripts/, h200_scripts/, tools/); grid vector cannot be honestly documented without recovery/rerun (pattern-036). Queue: regenerate hemisphere scan with committed script + exact grid metadata. |
| OpenAI-M10 (p_eq precision/recall calibration) | **QUEUED** | Recompute-class (GZ1 cross-match rerun); R24conf Queue #10 still open. |
| OpenAI-M11 (25% leg closure uncertainty) | **PARTIAL→QUEUED** | Artifact has point amplitudes/r only; uncertainty needs MC — recompute-class. |
| OpenAI-M12 (max(A_obs,A_UL95) undefined purpose) | **VERIFIED** | Closed with META-m3 edit (descriptive bound, no coverage guarantee). **CLOSED.** |
| Perplexity-M1 (largest claim) | **PARTIAL→CLOSED** | With Grok-E3. |
| Perplexity-M2 (A_UL95 not mapped to full-A) | **VERIFIED** | Pure-dipole unit identity added (algebra from declared conventions; matches c9b "A = A_p amplitude"). **CLOSED.** |
| Perplexity-M3 ("unmissable" language) | **STALE** | "In this channel's own units, independently of its systematics attribution" already present. |
| Perplexity-M4 (θ-uniform + bracketing) | **STALE** | In-session E2 close + "bracketed, not measured" present. |
| Perplexity-M5 (pipeline detail volume) | **HOUSTON-DECISION** | Reproducibility policy. |
| Perplexity-M6 (−9.5σ understated) | **STALE/OPINION** | Monopole's 9.5σ significance quoted repeatedly; mechanism candidates listed. |
| Perplexity-M7 (uniform weighting unjustified; panel untabulated) | **STALE** | §IV.C robustness (iii) gives numeric panel results (|z|≤0.8, p≥0.20, c12 artifact). |
| Perplexity-M8 (full-A vs A_p mixing) | **VERIFIED→CLOSED** | Via P-M2 identity edit; App D already states A_ref=0.034 A_p ↔ 1.7% f_CW. |
| Perplexity-M9 (real-space field not explicit) | **FALSIFIED** | Eq. 3 + "single canonical chirality-field definition used throughout" + §IV.C fit spec. |
| Perplexity-M10 (axis subtlety in abstract) | **STALE/HOUSTON** | §VII.e carries it; abstract density = Houston. |
| Perplexity-M11 (single-ℓ vs 39-band) | **STALE** | Table III caption "distinct estimator … should not be numerically equated" + App A.b cross-ref. |
| Perplexity-M12 (99.32% w/o absolute C1) | **STALE** | Table IV prints data 1.6961e-2 vs null 1.6846±0.0068e-2 with explicit convention-difference caption. |
| Perplexity-M13 (z≈−18 buried) | **FALSIFIED** | In abstract, §III hierarchy row (ii), Table I, App D bold, Conclusions. |
| Perplexity-M14 (implicit cross-null narrative) | **FALSIFIED/OPINION** | The z≈68–218 vs +7.28σ comparison is within the same channel (the completeness check's purpose); reviewer misread. |

## MINOR / NIT

| ID | Verdict | Disposition |
|----|---------|-------------|
| OpenAI-m1 (Table II rounding) | **STALE** | Caption: "computed from the unrounded fraction." |
| OpenAI-m2 ("C 2 2◦") | **FALSIFIED** | Source `$C^2$ $2^\circ$`; extraction artifact (R24conf n3 repeat). |
| OpenAI-m3 (T7 misprint history) | **HOUSTON-DECISION** | Audit-language policy. |
| OpenAI-m4 (≳25×) | **VERIFIED** | → "∼25×". **CLOSED.** |
| OpenAI-m5 (App E footnote length) | **OPINION** | Editorial. |
| OpenAI-m6 ("Ap=1.7%" unit contradiction) | **FALSIFIED** | c9b artifact: amplitudes_Ap=[0.005,0.0075,0.017,0.03]; "A = A_p amplitude = 2× f_CW modulation". §VII usage correct. |
| OpenAI-m7 ("0.39σ shift" phrasing) | **OPINION** | Statement is exactly difference-of-means/SE(diff); reviewer's requested form. |
| OpenAI-m8 (N_map,weighted scope) | **STALE** | Closed by in-session m1 em-dash note + Table I caption. |
| OpenAI-m9 (N_all/N_spiral histogram) | **QUEUED** | Supplemental recompute; footnote already gives mean 2.83 / global 2.65. |
| OpenAI-m10 (CI on Δ⟨p_CW⟩) | **QUEUED** | Recompute-class minor. |
| OpenAI-n1 (caption length) | **OPINION** | — |
| OpenAI-n2 (bib style) | **FALSIFIED/OPINION** | Inline bibliography uniformly journal+arXiv styled. |
| OpenAI-n3 (+4.31σ navigation) | **STALE** | App E footnote explicitly maps it to the +3.64σ estimator family + leakage channel. |
| META-m1 (conventions box) | **OPINION/HOUSTON** | Format choice; conversions present at each use + new identity sentence. |
| META-m2 (grid/seed metadata) | **VERIFIED→QUEUED** | With OpenAI-M9 (script not in repo). NIT-class for cleanliness. |
| META-m3 (max() purpose) | **VERIFIED→CLOSED** | Coverage-guarantee edit. |
| META-n1 (bootstrap protocol) | **VERIFIED** | Script-verified (replace=True, 440 draws, weights carried, full refit) — protocol parenthetical added App D. **CLOSED.** |
| Grok-N1 (redundant parenthetical) | **FALSIFIED/HOUSTON** | "(3.2 Million Spirals)" is in the title, not adjacent in abstract; title = Houston choice. |
| Grok-N2 (Fig 1 caption grammar) | **FALSIFIED** | "diversity … that the classifier resolves" is grammatical. |
| Grok-N3 (refs 7/12 arXiv-only) | **FALSIFIED** | Ref 7 Jia 2023 = ApJ 943,32+DOI; ref 12 Dosovitskiy = ICLR 2021 proceedings. All bib entries journal-styled; no nonexistent citations found. |
| Grok-N4 (Table VI duplicate Canonical rows) | **FALSIFIED** | Rows differ in Weight/apod. column (none vs C² 2°). |
| Perplexity-m1 (g=2a−1 placement) | **OPINION** | §VI.A gives a=0.6991 inline + confusion-matrix arithmetic. |
| Perplexity-m2 (f_sky bookkeeping) | **STALE** | Table I footnotes + Table VI consolidation. |
| Perplexity-m3 (per-slab N/σ) | **STALE** | §IV.B: N=457,308–309, σ=7.4e-4 quoted. |
| Perplexity-N1–N4 | **STALE / FALSIFIED(N2 grep) / HOUSTON(N3 DOI, N4 AI-statement)** | — |

## Verdict counts
- ESSENTIAL: 16 audited → 4 VERIFIED-closed-same-day (META-E1, META-E2, OpenAI-E6, E8), 3 PARTIAL→closed, 4 STALE, 4 HOUSTON, 1 FALSIFIED-component.
- MAJOR: 31 audited → 9 VERIFIED/closed-same-day (META-M1, M3, M4, M5, OpenAI-M1, M8, M12, P-M2, P-M8), 4 queued (OpenAI-M9 grid-doc, M10, M11, M2-already-queued), 12 STALE, 3 FALSIFIED, 3 HOUSTON/OPINION.
- MINOR/NIT: 3 closed (m4, META-m3, META-n1), 7 FALSIFIED, 3 queued, rest STALE/OPINION/HOUSTON.

**Substantive assessment**: META-E2 was the only finding touching a claim's documentation truth (the "single field convention" statement was factually wrong about the committed pipeline); it changed no number, no z-value, no conclusion, and was closed same-day from committed artifacts. All other verified items were clarity/disclosure additions closed same-day from script/artifact ground truth. Queued items (hemisphere-grid metadata, MC-uncertainty supplements, 200-MC harmonization) are reproducibility-polish recomputes already disclosed as queued in the text or non-blocking minors. Zero verified substantive E/M findings remain open.
