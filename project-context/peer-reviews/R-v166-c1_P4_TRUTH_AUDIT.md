# P4 R-v166-c1 — Truth audit (post-retraction clean-round 1 of 2)

**Round verdict: NOT CLEAN — 0/2 counter unchanged. Major-revision wave (v1.0.167) required.**

- Reviewers: Claude Opus 4.7 (REJECT) · GPT-5 (MAJOR REVISIONS) · Gemini 2.5 Pro (MAJOR REVISIONS) · Grok 4.3 (REJECT) · Perplexity sonar-pro (MAJOR REVISIONS)
- PDF reviewed: chirality_catalog_paper_v166.pdf (24 MB / 15 pp; Claude leg on gs-compressed 708 KB copy after 413 size cap)
- Audit method: per `feedback_peer_review_truth_audit_protocol` — every consolidated finding checked against the .tex / artifacts before closure work. Verdicts: VERIFIED / PARTIAL / OPINION / FALSIFIED / HOUSTON-DECISION.

## Consensus findings (2+ vendors, independently)

| # | Finding | Vendors | Verdict | Evidence | Fix class |
|---|---------|---------|---------|----------|-----------|
| C1 | Version-history/withdrawal/audit-log language in abstract + App A + fn:binomial_nspiral ("versions ≤1.0.165", "June 2026 provenance audit", "Artifact:" paths, "earlier version misquoted") | ALL 5 | VERIFIED | tex L75, L369, App A; grep confirms | Scrub to neutral provenance note; full detail → repo README. Pattern-017 recurrence. |
| C2 | Fig 3 pie shows Catalog-A counts (1,687,069/1,634,726/5,152,736) under "Catalog C composition" caption (1,592,107/1,609,053/5,273,371). Pie f_CW=0.5078 = Catalog A | Claude E2, GPT E4, Gemini E1 | VERIFIED | tex L225-236 vs rendered PNG; both sum to 8,474,531 → distinct catalog states | Regenerate fig_class_pie.png from Catalog C counts |
| C3 | Headline asymmetry pair incompatible: Table II "+0.79%/−0.26%" vs Sec IV.B + Fig 2 caption "+2.05%/−0.53%"; 3.86× factor only reproducible from the 2.05 pair (2.05/0.53=3.87; 0.79/0.26=3.04) | Claude E1, GPT E6, Perplexity M7 | VERIFIED | No artifact source for 2.05% found in outputs/ — stale Wave-era number | Recompute canonical pair from Catalog A/C counts; fix 3.86× → correct factor at all sites (also propagates to site keyResults + SSOT) |
| C4 | Table III bandpower significances irreproducible: negative C_ℓ with positive σ (e.g. ℓ_eff=9: −0.248/0.574 → −0.43, printed +2.232); null mean not printed | Claude E3, GPT M5, Gemini M3(p2), Perplexity E6 | VERIFIED | Recomputed from printed columns; ℓ_eff=4: 3.210/0.804=3.99 vs printed +6.097 | Add ⟨C_ℓ⟩_null column + sign convention, recompute from p4 artifacts |
| C5 | Table II Dev(σ) printed 28.8/14.6/9.5 vs recompute-from-printed-f 28.3/14.3/−9.3; sign suppressed on Catalog C; caption says signed (f−0.5)/σ | Claude (audit ≈), GPT E5, Gemini M1+m4, Grok M4, Perplexity m3 | VERIFIED | Computed from unrounded f (f_C=0.497345→9.48); printed f rounded | Print f to 6 dp or recompute Dev from printed values; restore sign on C row |
| C6 | σ from different nulls juxtaposed without local non-comparability caveats (abstract, Table I, Table III, Disc/Concl) — global disclaimer at tex L220 only | Grok E2, GPT E10, Perplexity E4+M6, Claude E6 | VERIFIED | Global disclaimer exists; local caveats absent at juxtapositions | Add per-juxtaposition caveats + null labels in Table I/III captions |
| C7 | Abstract ~900 words, changelog-like (withdrawal note + scope + falsification subclauses + parity clarification) | Claude M1, GPT E1, Grok E1/E3 | VERIFIED | tex L75-81 | Rewrite ≤250 words: one headline estimator + scale + one systematics sentence |
| C8 | Canonical mask threshold contradictory: ">10 spirals" (L300 Sec IV.C) vs "≥5 per pixel" (L260 Fig 5 caption) vs "≥10 spirals" (App A) | Claude E7, GPT E13 | VERIFIED | grep confirms all 3 sites | Pick one (verify against scripts), propagate; restate f_sky |
| C9 | Table I row (v) "p_LEE ≤ 10⁻⁴" while App C says post-Bonferroni/BH (~650 dirs) significance <1σ — raw pre-correction p advertised in headline table | Claude M7, GPT E9+E12, Perplexity M5 | VERIFIED | Caption/table vs App C | Report corrected value in Table I + footnote raw-vs-corrected |
| C10 | A95≈1.5–2% falsification framing is motivated reasoning (bar set at upper recovery edge); A95 itself not quantitatively documented (no recovery-curve table/figure for the 95% point) | Claude M3, GPT M3, Perplexity M2 | VERIFIED (presentation) | tex L81; injection table lacks ≥95% crossing point | Quote A50 + A95 neutrally; add recovery-probability table incl. amplitudes bracketing 95% |
| C11 | Real-space dipole estimator + isotropic bootstrap under-specified (objective, weights, resampling unit); +0.43σ vs p=0.30 mapping inconsistent (z=0.43 ↛ p=0.30 under any standard convention) | GPT M1+M2+E7, Claude M4 (adjacent) | VERIFIED | Sec IV.C gives only N_MC | Add estimator equation + bootstrap spec; state empirical-rank p and sidedness |
| C12 | WLS template fit load-bearing (z≈−18) but no design-matrix/coefficient/covariance table; z≈−264.5 vs z≈−250 duplication for same 1.7% reference | GPT M4+M9, Claude M6, Perplexity m5 | VERIFIED | App D.f prose only | Add template-fit table; single consistent far-tail number + defined z |
| C13 | Hemisphere statistic inconsistent: 3.05σ (main text) vs z=+4.42 (Table IV, monopole+mask null); scan grid described two ways (10° increments vs NSIDE_dir=8) | GPT E12, Perplexity m6 (adjacent) | VERIFIED-LIKELY | Needs per-null labeling; both numbers in tex | Label null per number; single scan spec |
| C14 | A_p / field-definition contradictions: App A item (a) "A_p=(N_CW−N_CCW)/N(p)_total" vs body spirals-only; f_CW−0.5 vs A_p=2(f−0.5) mixed without conversion | GPT E3+E14 | VERIFIED-LIKELY | Body L300-304 spirals-only; App A wording to fix | Single canonical field def + explicit ×2 conversion note |
| C15 | Abstract overstates: "MASTER … removes the leakage" vs body +3.64σ/+7.28σ post-MASTER residuals; +3.64σ moment-z given equal billing with ≈1.9σ Gaussian-equivalent empirical rank | GPT E16, Claude M8 | VERIFIED | Abstract vs Sec IV.D | "substantially reduces"; consistent dual-metric labeling |
| C16 | Shamir/CE-ResNet comparison numbers not traceable: "0.998" (Jia) without table ref; "2–4%"/"~3%" Shamir amplitudes unanchored; "30× extension" vs 3.2M/80k≈40× (or /127k≈25×); Shamir 2020 mislabeled DESI Legacy (is SDSS/Pan-STARRS) | Perplexity E1+E2+E3, GPT M10, Claude m8 | VERIFIED (citation rigor) | tex L97-99, L399 | Pin each number to table/fig of cited work; fix baseline + 2020 survey label; Shamir 2022a/b disambiguation |
| C17 | Table IV pre-MASTER z=+1.68 vs recompute (1.696−1.685)/0.007≈1.57 | Gemini m1, GPT E15 | VERIFIED | Printed values | Recompute or print exact σ |
| C18 | Paper length / operational detail (seeds, paths, 8-test suite granularity) excessive for PRD | Grok M1, Perplexity M4, Claude N1 | OPINION (style, consistent 3-vendor) | — | Condense in v167 where cheap; full condensation = Houston call |
| C19 | "Null" headline framing vs unresolved +7σ harmonic-channel residuals; post-hoc-primary-estimator concern (real-space chosen after harmonic channel went +7σ on corrected catalog) | Claude E4+M4, Grok E3/E4 | PARTIAL — wording fixes VERIFIED; estimator-choice justification = HOUSTON-DECISION | Depth-stratified null leaves +7.13σ → systematic unidentified, only classified | v167: honest abstract framing ("consistent with null; harmonic diagnostics carry systematics-attributed residuals"). Houston decides: pre-registration-style justification vs reframe |
| C20 | GZ1 cross-match κ=0.40 is "fair" agreement; 67.6% labels CE-ResNet-derived → "advances beyond CE-ResNet" / independence overstated; no confusion matrix | Claude M2, GPT M7 | VERIFIED (framing) | Sec II.B | Reframe novelty on scale + bias-hardening; add confusion matrix or per-class P/R |

## Single-vendor findings worth closing (spot-checked)

| # | Finding | Vendor | Verdict | Fix |
|---|---------|--------|---------|-----|
| S1 | "quality-quartile washout" cited as evidence (b) but analysis nowhere in paper | Gemini M2(p2) | VERIFIED-LIKELY (grep in v167 wave) | Add to App D or drop claim |
| S2 | Fig 8 caption "Top/Bottom two panels" vs actual single 5-bar chart; "2.7σ at ℓ=1" unreconciled with any body number; ℓ=5 red bar undiscussed | Claude E8 | VERIFIED-LIKELY (caption text confirmed in tex) | Regenerate caption + label null; reconcile or remove |
| S3 | "Four-null battery" (abstract) vs six labeled anchors in App D | Claude E9 | VERIFIED-LIKELY | Rename "five-anchor"/count correctly everywhere |
| S4 | 471,049 HC subsample defined as p_eq_CW>0.9 (asymmetric, CCW excluded); inconsistent with p_eq>0.6/0.8 cuts elsewhere | GPT E11 | VERIFIED (tex L75 confirms p_CW^eq>0.9) | Symmetric max(p_CW,p_CCW)>0.9 definition + consistent N |
| S5 | Fisher floor σ(A/2)≈0.048% → 0.29% underived / unreconciled with binomial σ=0.0279% | GPT E17 | VERIFIED-LIKELY | Show derivation or correct |
| S6 | Apodized f_sky 0.482 (App D.a) vs 0.488/0.494/0.452/0.420 (App A.c) mapping unclear | GPT E18 | VERIFIED-LIKELY | Single f_sky/f_eff table |
| S7 | Family-corrected p=0.0086 sidedness/method unspecified; possible double correction | GPT E19 | VERIFIED-LIKELY | Specify method + sidedness |
| S8 | 99.3% monopole reproduction quoted without uncertainty; residual still +1.68σ | Grok M2 | VERIFIED | Add uncertainty + residual statement |
| S9 | Walmsley GZ-DESI 8.7M → sharpen to "largest *chirality-labeled* catalog" | Claude M5 | VERIFIED | One-word fix |
| S10 | PACS obsolete; "ViT−Small-Small" typo; flip-swap corr=1.000 circular; future "Dated: June 2026"; CW/CCW first-use definition; pseudo-C_ℓ notation; DOI-less data availability; informal AI-tools phrasing | Claude m1-m5, GPT m3+m6, Grok E5/N1, Gemini N3, Perplexity m2/n1 | VERIFIED (mechanical batch) | Sweep in v167 |
| S11 | Title overclaims "A Null … Dipole" for a <1σ non-detection; retitle | Grok E4 | OPINION (Gemini calls title fine but long; Claude does not flag) | HOUSTON-DECISION — keep v166 title or soften |
| S12 | Condense to ≤6 pages or withdraw | Grok M1 | OPINION (overruled by GPT: "15pp acceptable for PRD") | No action beyond C18 |

## FALSIFIED / no-action

- Perplexity m3 (Table II 9.5σ "no numerical change strictly required") — superseded by C5: the sign error is real even if magnitude is rounding.
- Grok N2 ("3.2 Million" vs 3,201,160 rounding) — standard title rounding; no action.
- Gemini praise of retraction transparency vs 4-vendor demand to scrub version language — resolved in favor of scrubbing (C1): keep the *fact* of the correction, lose the version numbers/paths.

## Meta-reviewer findings (gpt-5-pro, blind-spot pass)

| # | Finding | Verdict | Evidence | Fix class |
|---|---------|---------|----------|-----------|
| META-E1 | Training-label arithmetic: 6,637+17,153+2,000=25,790 ≠ stated 26,636 total; CE-ResNet share 17,153/26,636=64.4% ≠ stated 67.6% | VERIFIED | tex L135 recomputed | Reconcile against training manifest; tabulate sources; fix share |
| META-E2 | Malformed HF URLs with embedded spaces | FALSIFIED | tex L573-574 `\url{}` well-formed; spaces are PDF text-extraction line-break artifacts | No action (optionally add Zenodo DOIs per Perplexity m2) |
| META-E3 | T7 calibration criterion "<50% at confidence >0.9" vs Fig 6 "73.6% at max p ≥ 0.9", yet Table V marks T7 PASS | VERIFIED | tex L270 vs L486/L500 | Investigate true T7 criterion vs measurement; fix spec or verdict; add ECE/Brier |
| META-M1 | Fig 7 panel image internally labeled "Fig. 11" while caption says FIG. 7 | VERIFIED-LIKELY (native-PDF observation) | Needs PNG check in closure | Regenerate panel or strip embedded numbering |
| META-M2 | Fisher floor uses f_sky=0.46 vs 0.490–0.494 everywhere else | VERIFIED | tex L415 | Single documented f_sky + show derivation (merges with S5) |
| META-M3 | Permutation-null trial-pool ambiguity: shuffles among spirals only or all galaxies (NS included)? Not stated per null | VERIFIED (spec gap) | Multiple null phrasings in tex | Define each null's shuffle pool; rerun if any used NS-contaminated pool (compute) |
| META-M4 | Cross-spectrum r_ℓ undefined (negative auto-powers make ρ ill-defined); "σ = −2.89" sign misuse | VERIFIED-LIKELY | App D.g | Define r_ℓ + de-biasing + sidedness |
| META-M5 | Underpowered MC for tail claims: N=500 permutations (p_MC=0.030 resolution) + N_MC,inj=100/amplitude behind A95 | VERIFIED (design) | tex L415 confirms N_MC,inj=100 | Compute: ≥10k permutations, ≥1k injections/amplitude + P_det(A) curve (pairs with C10) |
| META-M6 | Weighting/observable mismatch: A_p defined on spirals but NaMaster weight W_p=N_all; +7.28σ vs +9.78σ sensitivity to W_p choice unexplained conceptually | VERIFIED (design) | Sec IV.C + App A.a | Compute: rerun with W_p∈{N_spiral, N_all, uniform}; adopt consistent choice |
| META-m1/m2 | Abstract "at z≈−18" duplication; "471,049 high-confidence per-spiral" wording + asymmetric p_CW cut | VERIFIED | tex L75 | Merge with S4 + C7 abstract rewrite |
| META-N1 | f_sky/f_eff values scattered, no consolidated table | VERIFIED | Merges with S6 | Single mask/weight/apod → (f_sky, f_eff) table |

## Disposition

- v1.0.167 closure wave: C1–C17, C20, S1–S10 (text/table/figure fixes; several need artifact recomputes: Table III null means, asymmetry pair C3, Fisher floor S5).
- HOUSTON-DECISION items: C19 estimator-choice justification; S11 title; C18 full condensation depth.
- After v167 lands: restart clean-round counter — this round does NOT count toward the required 2.
- Meta-reviewer (gpt-5-pro) findings to be appended when pass completes.
