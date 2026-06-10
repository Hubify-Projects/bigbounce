# R24conf P1B — Truth-Audit Table (closeout 2026-06-10, v1B.0.52 → v1B.0.53)

Verdicts: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION.
Ground truth honored: run1_full 0.336±0.10, run3 0.344±0.10, c5 median 20.7 [7.3,45.6], c10/c10b artifacts (reproducibility/p1_namaster_500mc/results/, research/branch_R_alp_birefringence/phase2_mcmc/).

All Claude_brutal findings duplicate Claude_brutal_INSESSION; in-session closures (E1/E2/m1/m2/m3 envelope floor 0.064 + union-over-box clarifier + z_p collision note; N1 model-preference disclaimer §V.B; N2 two-fine-tunings sentence §VI) marked STALE.

| Finding | Sev | Verdict | Evidence / action (post-edit paper1b_mcmc_companion.tex) |
|---|---|---|---|
| Claude/INSESSION E1 (required-C band) | ESS | STALE | In-session closure: floor 0.064 → ≈160 consistent (L1469, L1589) |
| Claude/INSESSION E2 (envelope cross-check) | ESS | STALE | Union-over-box clarifier in-session (L1513–1517) |
| Claude/INSESSION E3 (β_combined arithmetic) | ESS | FALSIFIED | Reviewer's own recompute reproduces 0.241°±0.061°, 3.9σ — paper correct |
| Claude/INSESSION M1 (c10 reconciliation) | MAJOR | FALSIFIED | c10_robustness_battery.json matches text exactly: invvar 0.264/−0.006, camb_lensed 0.251/−0.019, apod 0.239/0.238, b30 0.238, purify 0.238 |
| Claude/INSESSION m1 (z_p 0.27 collision) | MINOR | STALE | In-session note landed |
| Claude/INSESSION m2 (abstract envelope ambiguity) | MINOR | STALE | In-session |
| Claude/INSESSION m3 (160 vs 171.7) | MINOR | STALE | In-session floor reset to 0.064 preserves ≈160 (10.3/0.064=161) |
| Claude/INSESSION N1 (Bayes placeholder) | NIT | STALE | In-session §V.B model-preference disclaimer |
| Claude/INSESSION N2 (two fine-tunings) | NIT | STALE | In-session §VI sentence (L1595–1601) |
| Gemini E1 (restructure manuscript) | ESS | OPINION/HOUSTON-DECISION | Wholesale reorganization = scope call; w0wa section already scoped as separate analysis |
| Gemini E2 (companion framing/title) | ESS | HOUSTON-DECISION | Companion-paper framing is deliberate program structure |
| Gemini E3 (correction notes removal) | ESS | HOUSTON-DECISION | Keep, per standing correction-note policy |
| Gemini E4 (Table IV/App B meta-table removal) | ESS | HOUSTON-DECISION | Claims-classification table is deliberate reproducibility disclosure |
| Gemini M1 (ALP section signposting) | MAJOR | OPINION | Configurations now explicitly enumerated with counts (L1556–1560); dense but accurate |
| Gemini m1 (broken H₀ formula) | MINOR | STALE | L1078 reads `$|67.79-68.41|/\sqrt{1.09^2+0.32^2}$` — properly typeset |
| Gemini m2 (verbose footnotes) | MINOR | OPINION | Reproducibility-first style, deliberate |
| Gemini m3 (headline provenance) | MINOR | OPINION | "Headline result" scoped within §V.B w0wa analysis |
| Gemini m4 (sample counts) | MINOR | STALE | fn sample_stratification fully reconciles 309,189/216,432/123,368/119,617 |
| Grok E1 (future date) | ESS | FALSIFIED | AUTO-FALSIFY: it IS June 2026; date not in the future |
| Grok E2 (abstract misrepresents) | ESS | STALE | Abstract carries "no torsion modifications… null-consistency test, not evidence" scope inline (L649–653) |
| Grok E3 (reduce to 4pp) | ESS | OPINION | Length/scope preference |
| Grok M1 (version language) | MAJOR | HOUSTON-DECISION | Same as Gemini E3 |
| Grok M2 (third chain) | MAJOR | STALE | fn discloses Planck-only chain: 114,992 raw, R̂−1~0.05, excluded from all headlines (L840–845) |
| Grok M3 (bias/floor juxtaposition) | MAJOR | VERIFIED | Abstract clause added: −0.040° floor named in same sentence as −0.032° bias; both MC figures, not comparable to sky significances (L663–668) |
| Grok N1 (4.93×10⁻³ derivation) | NIT | STALE | Convention paragraph L1495–1504 fixes normalization; 5.8×10⁻⁴×8×1.06=4.92×10⁻³ reproduces displayed value |
| Grok N2 (no arXiv numbers) | NIT | HOUSTON-DECISION | Posted-concurrently policy |
| Grok NIT1 (affiliation) | NIT | OPINION | Independent-researcher affiliation is PRD-acceptable |
| META-E1 (S8 prior pull) | ESS | VERIFIED+QUEUE | Exact prior disclosed from committed YAML (0.776±0.017, cobaya_full_tension.yaml L31); naive combination 0.802±0.012 vs joint 0.814±0.008 disclosed with degeneracy explanation in Table I caption; chain-level overlay pull check → COMPUTE_QUEUE |
| META-M1 (PR4+2018 pairing) | MAJOR | VERIFIED+QUEUE | Limitation sentence added (§III, L818–825); swap-test MCMC → COMPUTE_QUEUE |
| META-M2 (injection/template mismatch) | MAJOR | VERIFIED | Reviewer premise inverted vs committed script: camb_lensed swaps the injected-sky BB; template is EE-only in ALL configs. Clarification paragraph citing c10_robustness_battery.py added (L1325–1334); matched-injection−CBB-template config → COMPUTE_QUEUE |
| META-M3 (θ prior choice) | MAJOR | VERIFIED+QUEUE | Direction argument added: cosθ-flat density ∝sinθ carries less small-θ mass → spectator-sliver fractions decrease; flat-θ is the generous choice (L1640–1648); cosθ-flat rerun → COMPUTE_QUEUE |
| META-M4 (β periodicity) | MAJOR | VERIFIED | Periodicity note added: β≡β+n·90°, posterior support |β|≲0.7°≪90°, wrapping negligible (L1570–1576) |
| META-M5 (3.2σ conditioning) | MAJOR | VERIFIED | Caveat added: marginal-σ_MB-normalized descriptive offset, not conditioned on MB–H0 covariance; conditioned statement = canonical H0 tension (L1049–1055) |
| META-M6 (ΔP units domain) | MAJOR | VERIFIED | Thermodynamic µK_CMB·arcmin sentence added, synfast-consistent, no bandpass conversions (L1205–1209) |
| META-m1 (σβ on plot) | MINOR | STALE | Caption already quotes dedicated-rerun σβ=0.046° at the fsky=0.32 point (L1128–1131) |
| META-m2 (Caγ band harmonization) | MINOR | VERIFIED | Parenthetical at the ≈8.6–160 quote: [4,60] scan coverage + Δφ/fa≲0.17 corners outside scan (L1589–1594) |
| META-m3 (S8 undefined) | MINOR | VERIFIED | S8 ≡ σ8(Ωm/0.3)^{1/2} added to Table I caption, matching YAML derived-parameter definition exactly |
| META-N1 (pixel window) | NIT | VERIFIED | Common pixel-window cancellation clause added; no deconvolution, no mismatch (L1170–1175) |
| Perplexity E1 ([3] Diego-Palazuelos PRL 128:091302) | ESS | FALSIFIED | .bbl entry internally consistent (PRL 128, 091302 (2022), arXiv:2201.07682 is the real PR4 birefringence paper); Perplexity citation-existence record 15/15 false |
| Perplexity E2/E8 ([4] ACT DR6 arXiv:2509.13654) | ESS | FALSIFIED | 25xx arXiv IDs valid in 2026; entry consistent; pattern-001 confab class |
| Perplexity E3 (Liu torsion-DESI) | ESS | FALSIFIED | 5th+ reflag; references.bib carries real Liu+Li+Xu+Biesiada+Wang EPJC 2025 arXiv:2507.04265 (audited in R25/R26/R27 rounds) |
| Perplexity E4/E9 (DESI DR2 results II) | ESS | FALSIFIED | arXiv:2503.14738 = DESI DR2 BAO cosmology paper; future-date auto-falsify + 15/15 record |
| Perplexity E5 (DES-Y5 SN) | ESS | FALSIFIED | Reviewer's own check confirms arXiv:2401.02929 matches |
| Perplexity E6 (LiteBIRD PTEP) | ESS | FALSIFIED | Reviewer's own check confirms exact match |
| Perplexity E7/M9 (σ juxtapositions) | ESS | PARTIAL | Most sites carry local disclaimers (fn.3, scope notes); abstract clause added this round (Grok M3 closure); Fig.1 S8/DES-Y3 comparison now contextualized via Table I caption disclosure |
| Perplexity E10 (σ arithmetic) | ESS | PARTIAL | 3.6σ verified consistent by reviewer's own math; MB 3.2σ conditioning closed via META-M5 edit |
| Perplexity E11 (σpix dimensions) | ESS | FALSIFIED | Text has σpix=ΔP/√Ωpix with exact steradian equivalence shown (L1199–1204); reviewer misquoted formula |
| Perplexity E12 (Eq. 3 normalization) | ESS | STALE | Convention paragraph (gaγ=Cαem/(2πfa), β=(gaγ/2)Δφ) committed at L1495–1504 |
| Perplexity E13 (0.42 vs grid) | ESS | FALSIFIED | 0.42 (m=2H0,θi=1) lies inside [0.064,1.19]; correction note documents superseded draft values |
| Perplexity M1 (Eskilt PR3/PR4 footnote) | MAJOR | STALE | fn eskilt_pr3_pr4 already disambiguates published-paper vs code-repo datasets |
| Perplexity M2/M10 (natural-params overclaim) | MAJOR | STALE | In-session N1 closure + 25× tuning disclosed at abstract/intro/§VI/caveats (L750–753, L1717) |
| Perplexity M3/m9 (LiteBIRD 9σ decisive) | MAJOR | VERIFIED | Rewritten: forecast-under-assumptions caveat + two-null-hypotheses + 0.7σ discrimination arithmetic (L1709–1720) |
| Perplexity M4 (Riess MB usage) | MAJOR | OPINION | Reviewer confirms values and algebra correct |
| Perplexity M5 (quintom-B anchor language) | MAJOR | STALE | "Empirical anchor" wording audited STALE in prior round (pattern-016); §V.B carries internal-fit provenance |
| Perplexity M6 (earlier-draft language) | MAJOR | HOUSTON-DECISION | Correction-note policy |
| Perplexity M7 (AI acknowledgement) | MAJOR | HOUSTON-DECISION | Factual disclosure; author retains responsibility statement |
| Perplexity M8 (overlength) | MAJOR | OPINION | Scope preference (= Gemini E1/Grok E3) |
| Perplexity M11 (abstract cross-refs) | MAJOR | OPINION | Abstract↔Table I↔§III mapping explicit |
| Perplexity m1 (3.6σ traceability) | MINOR | VERIFIED | β/σ=0.342/0.094≈3.6 + Gaussian-summary note added (L1148–1152) |
| Perplexity m2/m7 (Fig 2 SM label) | MINOR | FALSIFIED | Rendered figure legend reads "SM (ΔNeff = 0)" — pdftotext dropped the Δ glyph |
| Perplexity m3 (spectator wording) | MINOR | STALE | fn theta_backreaction + repeated spectator-sliver reminders present |
| Perplexity m4 ("canonical") | MINOR | OPINION | Style |
| Perplexity m5 (artifact filenames) | MINOR | HOUSTON-DECISION | Reproducibility-first house style |
| Perplexity m6 (cross-ref V.A) | MINOR | STALE | §II now states (ω/H)₀, Ω_k fixed inline (L778–782) |
| Perplexity m8 (δ/σ for "consistent") | MINOR | VERIFIED | 0.04σ arithmetic added at the all-three-within-1σ claim (L1580–1585); spectator subset already had 0.5σ |
| Perplexity n1 (hyphenation) | NIT | OPINION | — |
| Perplexity n2 (PACS) | NIT | OPINION | — |
| Perplexity n3 (pivot algebra note) | NIT | OPINION | Note (b) algebra correct as written |
| Perplexity n4 (URL formatting) | NIT | OPINION | — |
| OpenAI (all) | — | — | OpenAI_methodology returned zero findings for P1B |

**Counts (distinct findings audited: 62):** VERIFIED 12 · PARTIAL 2 · STALE 18 · FALSIFIED 12 · OPINION 11 · HOUSTON-DECISION 7.

**Recompute-class queued:** META-E1 (S8 overlay/pull from frozen chains), META-M1 (release-pairing swap MCMC), META-M2 (matched CAMB-BB injection + −CBB template 500-MC), META-M3 (cosθ-flat prior c5 rerun) → R24CONF_COMPUTE_QUEUE.md.

**Clean-round verdict:** CLEAN after closures: no — 7 verified ESSENTIAL/MAJOR findings (META-E1, M1–M6 family, Grok M3, Perplexity M3) remained before closures; all closed textually this round, 4 recompute items queued.
