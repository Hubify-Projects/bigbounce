# P2 R25conf — TRUTH AUDIT (post-fix confirmation round)

**Date**: 2026-06-10 · **Auditor**: closure agent
**Source audited**: `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.47 working tree → v1.7.47+R25conf)
**Inputs**: R25conf_P2_SYNTHESIS.md (132 findings / 7 reviewers incl. regenerated sonar-pro Perplexity leg), R25conf_P2_META_REVIEW.md, R25conf_P2_Claude_brutal_INSESSION.md (≡ Claude_brutal; duplicate leg, counted once).
**Committed ground truth used**: `outputs/{c8,c9g,c9h,c9i,c9j,c9k}_*.json`, `appendix_A1_wick_doubling.py`, `null_space_analysis.py`. New artifact this round: **c9l_sigma_theory_continuous_marginalization.py** (+ JSON).
**Auto-falsification rules applied**: future-date/arXiv-26xx (it IS June 2026); citation-nonexistence checked against the .bbl + R24conf E2 precedent (the one real Perplexity citation catch — re-checked, still correctly fixed); correction-note-removal + abstract-length/AI-acknowledgment = HOUSTON-DECISION.

**Verdict counts (54 deduped rows)**: VERIFIED→CLOSED 19 (incl. all 4 in-session M's) · PARTIAL 4 (no-edit) · STALE 14 · FALSIFIED 8 · OPINION 4 · HOUSTON-DECISION 5 · QUEUED 5 (META-E2, META-E1-recompute, META-M1, META-M2, META-M5 → R24CONF_COMPUTE_QUEUE #43–47) · recompute RUN 1 (Grok M1 → c9l).

## Claude_brutal_INSESSION (4 M + minors) — the open leg

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| M1 | Assumption-(d) "robust across bounce class" overclaim — abstract/§II.C don't re-flag cubic-order is unverified | **VERIFIED → CLOSED** | Weakest-link sentence added in §II.C assumptions ¶ ("verified at linear order… every 'robust across the bounce class' statement is conditional on (d)"); conditional clause added at the §II.B "robust" lead sentence. |
| M2 | Abstract "headline envelope BF~10–17" conflicts with tab:bayes footnote ("17 … not the recommended headline") | **VERIFIED → CLOSED** | Option (b) of the reviewer's fix: "headline envelope" → "recommended-to-theoretical-maximum envelope" (abstract + §VI bracketing ¶, 2 sites). Now consistent with footnote b. |
| M3 | tab:gr "Corrected (10% residual)" row reads as padding; "10% of what" undefined (joint w/ OpenAI E7) | **VERIFIED → CLOSED** | Footnote a rewritten: bookkeeping verification row in the strict zero-residual limit; literal σ_GR=0.05 calibration computed against c9g conventions (BF vs Tuned 6.99, ΔBF=0.01; SSFSR would read 3.1×10⁸ ≠ 3.5×10⁸ — stated, not hidden); "three independent scenarios plus one verification row". |
| M4 | Fig. 6 legend "kills live lane" is dev jargon burned into PNG + caption | **VERIFIED → CLOSED** | PNG regenerated (`generate_all_figures.py` fig4: "BOUNCE EXCLUDED" / "WRONG SIGN (supports exotic multifield inflation)"), copied into paper dir, caption updated. Closes R24CONF queue #42. |
| m5/m6 | "structural extension on the future work" (§IV) + κ_ε four-vertex deferral (§VIII.B) | **VERIFIED → CLOSED** | §IV phrasing replaced (leading-order assumption adopted, no "future work"); §VIII.B scope sentence added (impact bounded by κ_ε\|Δε\|≈0.36, inside σ_theory=1.0). |
| m7 | "Li-Brandenberger row" vs Table IV label "Li et al." | **VERIFIED → CLOSED** | A.2 prose → "Li~\etal\ row". |
| m8 (downgraded N10) | ρ −0.97 (prose) vs √(1−0.969²) (formula) | **VERIFIED → CLOSED** | Prose → −0.969; matches committed c8 correlation −0.9689. |
| m4 | Fig 2 "−35/8B" stray glyph | **PARTIAL (no edit)** | Low-confidence visual nit, self-flagged "pending png inspection"; caption text in tex is correct; figure title regen folded into the queued figure pass if confirmed. |
| m1 | Abstract single-block / withdrawal flag placement | **HOUSTON-DECISION** | Abstract structure is Houston's standing call (R24). |
| Orphan tail finding | "first time to our knowledge" tighten | **OPINION** | Hedged + literature-search statement (iii) present; same as R24 OpenAI-M8. |
| N1–N19 | 23/23 arithmetic spot-checks | **all-clear** | Reviewer's own verifications; used below to falsify vendor arithmetic contradictions. |

## META_REVIEW (10)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| META-E1 | 1−r_cos² projection-noise bound uses unweighted metric, not estimator Fisher metric | **VERIFIED → CLOSED (text) + QUEUED (recompute)** | Premise true (R24 META-m8 closure documents unweighted Euclidean). Reviewer's option (b) executed: bound now scoped in-text as "heuristic shape-similarity indicator, not an estimator-mismatch variance bound under SPHEREx weighting". Fisher-metric recompute → queue #44. |
| META-E2 | 1/S_v symmetry factor in Eq. (A7) unjustified; risks the very factor-of-2 class | **QUEUED (#43)** | `appendix_A1_wick_doubling.py` asserts S_v but does not derive it — cannot close without a real derivation (/never-fabricate-derivation, pattern-036). Materiality bounded: paper's coefficients are fixed from the three published benchmarks, not from Eq. (A7) normalization (c9i confirms non-transplantability), so headline numbers do not flow through A7. |
| META-M1 | Exact-benchmark conditioning inflates r_cos / suppresses worst-case r | **QUEUED (#45)** | Recompute-class (tolerance-conditioned rescan); honest-restricted-subset framing already in-text (R24 META-M1). |
| META-M2 | Missing joint two-template Fisher bias test | **QUEUED (#46)** | Needs survey covariance machinery; text already states zero-estimator-bias assumption via the r-projection framing. |
| META-M3 | PNG cross-terms field-mixing ambiguity (P vs P_ζ, δ_c double-count) | **VERIFIED → CLOSED** | §VII.B clarifier added: P = late-time matter power spectrum; primordial normalization via M(k,z) (Eq. eq:Mkz); δ_c carried inside b_φ=2δ_c(b_1−1), no double count. All verifiable from the paper's own Eqs. (3)–(4). |
| META-M4 | 1/√fsky heuristic inapplicable to the 2D test | **STALE** | R24 META-M5 closure already scopes it: CMB heuristic, 2D test only, "not used in any quantitative forecast". |
| META-M5 | Non-Gaussian covariance at \|fNL\|~4 unchecked | **QUEUED (#47)** | Cite-or-compute scaling bound. |
| META-m1 | Folded row is a measure-zero degenerate limit | **VERIFIED → CLOSED** | tab:benchmarks footnote a added (degenerate boundary k1=k2+k3, evaluated as the limit of k1=2k, k2=k3=k). |
| META-m2 | Cutoff-insensitivity in uniform measure doesn't certify SPHEREx-weighted r | **FALSIFIED** | §III.B states the cutoff scan was run "under 10 physically motivated weighting schemes … scanning over squeezed cutoffs", i.e. per-weighting, not uniform-only; the R24 reconciliation ¶ also distinguishes the procedures. |
| META-N1 | Orbit multiplicity/ordering undefined | **VERIFIED → CLOSED** | Ordered-tuple definition added at §II.A, matching `null_space_analysis.py` (verified: Σ_{i≠j} 6 ordered terms; Σ_{i≠j≠l} 6 ordered permutations). |

## OpenAI_methodology (4E/16M/3N)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | Eq. (1)/(2) B_NL dimensionally inconsistent | **STALE-FALSIFIED** | R24 E5: reviewer misread the PDF fraction; B_NL=(10/3)A_T/Σk³ with explicit degree bookkeeping at the site. Convention-blind repeat. |
| E2 | BF normalization error → systematic overstatement | **FALSIFIED** | The "correct" formula the reviewer derives (W·L/∫L for delta-vs-flat) IS Eq. (7). All quoted BFs (17.10/13.91/9.80/5.65/7.00/4.01) reproduce from c9g conventions this round (independent recompute above + c9l grid). R24 E1 falsified the same class (truncation at the prior edge). |
| E3 | Correction notes in main text | **HOUSTON-DECISION** | Standing decision since R23 (transparent disclosure). |
| E4 | σ comparability flags | **STALE** | Abstract per-pairing labels + §IX.D (i)/(ii) block + §VII reconciliation ¶. |
| E5 | σ_GR=0.5 "~15%" inconsistent with quadrature model (true value 22.9%) | **VERIFIED → CLOSED** | Genuine arithmetic catch. √(0.7²+0.5²)/0.7=1.229 (c9k σ_eff=0.8602 confirms). Text → "~23% degradation in σ(fNL) under the quadrature model of Table III (0.860/0.700=1.23), within the 10–30% range" (still inside Jolicoeur band). |
| E6 (M) | M(k,z) h-unit inconsistency | **FALSIFIED** | In consistent h-units (k in h Mpc⁻¹ with H0=100h), h cancels in k²/H0²; convention pinned in-text since R24 M6. No hidden h-dependence. |
| E7 (M) | "10% residual" mapping undefined | **VERIFIED → CLOSED** | Folded into in-session M3 closure (footnote a rewrite with explicit σ_GR=0.05 calibration + zero-residual-limit labeling). |
| M1/M2/M4 | b_φ 20–50%, Poisson 15–30%, photo-z 5% lack derivations | **STALE** | All scoped with "upper bound pending…"/"simplified Fisher degradation estimate" + Pullen/Giannantonio/Barreira cites (R23/R24). |
| M3 | Planck recast central value must scale by 1/r | **VERIFIED → CLOSED (de minimis)** | True in principle; −0.1/0.876=−0.114 → tension 0.746σ = 0.75σ at quoted precision. Parenthetical added stating exactly this. |
| M5 | SDB joint Fisher reproducibility | **STALE** | c8 script + inputs released; §IX.D documents validation vs Doré lineage. |
| M6 | Artifact filenames clutter | **HOUSTON-DECISION** | Provenance audit-trail standard. |
| M7 | "CMB Fisher, w∝k²" nonstandard | **PARTIAL (no edit)** | Labeled as one of 10 schemes with the ℓ-space validation quoted separately (r=0.878±0.012); heuristic naming, not a forecast input — the LSS noise-weighted r drives the recast. |
| M8 | "Establishes" overclaim re Cai convention | **STALE** | §II.C ends "validated through cross-checks rather than a fully independent derivation"; App A.1 scope ¶ present. |
| M9 | r ≤ 1 claim unproven | **STALE-FALSIFIED** | The footnote at the site states the monotonic-squeezed-maximization assumption AND retains the untruncated r>1 samples — exactly the requested treatment. |
| M10 | Fig 5 threshold alignment | **OPINION** | Figure cosmetics; values cross-stated in caption. |
| M11 | Injection-recovery noise description inconsistent | **PARTIAL (no edit)** | "Isotropic" (angular) + diagonal photo-z covariance (per-mode amplitude) coexist; ¶ already scopes the test as 2D flat-sky CMB-style cross-check, not the SPHEREx estimator (R23/R24 closure). |
| M12 | Fig 2 non-comparability flag | **VERIFIED → CLOSED** | Joint with Perplexity M15: caption budget list now includes GR-projection marginalization explicitly. |
| M13 | n_fNL=0 lacks one-line justification | **VERIFIED → CLOSED** | Degree-zero (scale-free) shape-function argument added — verifiable from the paper's own degree bookkeeping. |
| N1–N3 | Em dashes, ref style, file list length | **OPINION** | Copyedit tier. |

## Grok_brutal (2E/3M/2N/1NIT)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | Abstract 5.2–5.5σ not final forecast | **FALSIFIED** | Abstract leads with 3–5σ post-budget; 5.2–5.5σ explicitly labeled "optimistic case before GR and b_φ degradation"; the reviewer's own required fix ("explicitly qualify as pre-systematic") is already verbatim satisfied. |
| E2 | Convention halving not stated in abstract/forecast sections | **FALSIFIED** | Abstract carries the full halving caveat (2.6–2.75σ / 1.5–2.5σ) + App A.2 dual-norm table; §X restates. Auto-falsifiable repeat of R24 E2. |
| M1 | No continuous marginalization over prior width | **VERIFIED → CLOSED (recompute RUN)** | NEW artifact c9l: σ_theory ~ U[0.5,2.0] → BF=8.8 broad / 3.6 narrow; between grid endpoints, close to recommended 9.80/4.01; BF>1 across entire support; 3-pt grid <0.03 in log-evidence. Sentence + Data Availability entry added. |
| M2 | r distribution tail incompletely characterized | **STALE** | c9h percentile propagation (4.4–6.2σ at 16–84%) committed R23; abstract carries ±0.13 + 16th-percentile statement; full untruncated range 0.55–1.14 quoted. |
| M3 | 24 pages → condense to ≤14 | **HOUSTON-DECISION** | Length is Houston's call (standing since R23). |
| N1 | Decimal-place inconsistency Table I | **FALSIFIED** | Squeezed −4.375, equilateral −3.984, folded −2.250 — all four significant figures / three decimals, uniform; exact fractions in adjacent column. |
| N2/NIT1 | Tone; axis units | **OPINION / queued figure pass** | Axis-units regen rides queue #24-style figure pass (P2 portion folded into queue #42 follow-ups if needed). |

## Perplexity_citations (8E/24M/2N, sonar-pro regenerated leg)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | Not PRD form (URLs, artifact names, correction notes) | **HOUSTON-DECISION** | Standing transparent-disclosure decision. |
| E2/E8 | Speculative qualifiers / length | **HOUSTON-DECISION (length) / STALE** | MegaMapper explicitly "speculative motivation, not firm forecasts" — the qualifier IS the requested fix. |
| E3 | σ stacking not checkable | **STALE** | §VII end reconciliation ¶ (6.25→×r→5.2–5.5→b_φ→GR→3.0). |
| E4 | κ_ε lower endpoint attribution | **STALE** | Two-channel derivation present (v1.7.42; R24 m7). |
| E5 | Cai-vs-Li resolution overclaim | **STALE** | Same closure set as OpenAI M8. |
| E6 | BF prior-driven, hard to audit | **STALE** | Four-corner grid + c9g/c9j/c9k (+ now c9l) named in Data Availability. |
| E7 | σ mixing without qualification | **STALE** | Same as OpenAI E4. |
| M6 | Cai 2009 citation check | **all-clear** | Reviewer's own verification: correct. |
| M7 | Heinrich σ=0.7/0.5 usage | **all-clear** | §IV quotes exactly bispectrum-alone 0.7, combined 0.5. |
| M8 | Planck −0.9±5.1 vs PR4 | **STALE-FALSIFIED** | §VIII.A cites Jung 2025 PR4 (−0.1±5.0) AND notes PR3 −0.9±5.1 — R24 m4 repeat. |
| M9 | Future arXiv IDs (2603.13924 etc.) | **AUTO-FALSIFIED** | June 2026 current; arXiv 26xx valid; .bbl entries resolve (R24-verified). In-session N19 concurs. |
| M10 (refs) | Pajer/Chen-Wang/DESI metadata | **all-clear** | Reviewer reports consistency. |
| M10 (abstract σ propagation) | 8% extreme → 4.8σ inconsistent | **FALSIFIED** | 5.2×0.92 = 4.78 ≈ 4.8σ; chain exact. In-session leg verified the surrounding arithmetic 23/23. |
| M11 (null-space range) | 4.4–6.2σ vs 3σ floor contradiction | **FALSIFIED** | 16th-percentile 4.4σ > 3σ floor — consistent, not contradictory. |
| M12 (Eqs 1–4 dimensions) | Normalization not explicit | **STALE** | Degree bookkeeping + unit convention at the sites (R23 E5 / R24 M6). |
| M12 (AI acknowledgment) | Remove AI/computing lines | **HOUSTON-DECISION** | Transparency disclosure retained. |
| M13/M16 | ε-correction 0.6–8% vs 1–8% status mismatch | **VERIFIED → CLOSED** | Real residual inconsistency: 4 sites harmonized to the derived 0.6–8% (prefactor floor 0.6% = 5.6×0.0045/4.375; ceiling 8% = 80×0.0045/4.375 — both verified). |
| M14 | "Establishing via in-in identity" overstates A.1 | **STALE** | Same as OpenAI M8/E5 closure set. |
| M15 | Fig 2 caption omits GR from "full budget" list | **VERIFIED → CLOSED** | GR-projection marginalization (σ_GR, Table III) added to the caption list; caption tail already said "and GR systematics". |
| M17 | MC dispersions ≠ population σ | **STALE / OPINION** | MC-SE caption sentence (R24 in-session M2) + percentile framing. |
| M18 | "Convention" language vs physical content | **STALE** | R24 META-E1 closure: halving attributed to time-ordering content, "not a pure c-rescaling" at abstract + conclusion + A.2. |
| M19 | MegaMapper window drift across sections | **STALE** | R24 N1: abstract 3–7σ tied to MegaMapper sentence; §VII crosswalk ¶. |
| M20 | Unquantified hedges | **OPINION** | ALP site quantifies 0.77σ; others are scoped qualitative statements. |
| M21 | "Combined systematic budget" overpromise | **PARTIAL (no edit)** | Components itemized in abstract; §VII reconciliation ¶ + shot-noise exclusion flagged in-text. |
| N1/N2 | Repetition; notation collisions | **OPINION** | r_t rename (R24 META-M4) already done; rest copyedit. |

## Gemini_cosmology — zero findings (clean leg). No rows.

## Cross-checks on the in-session 23/23 arithmetic all-clears
No vendor finding contradicts any of the 23 verified spot-checks; the two vendor arithmetic attacks that brushed them (OpenAI E2 BF values, Perplexity M10/M11 propagation) were falsified against c9g/c9l and direct recompute, not against reviewer assertions.

## Compile status
pdflatex ×2 + bibtex + pdflatex ×2 clean: 24 pages, 0 undefined references/citations. Overfull hboxes: 2.95pt (tab:benchmarks) + 1.23pt (in-in identity line) — **both pre-existing in the committed v1.7.47 build** (verified by compiling the pre-edit backup), sub-millimeter; no new overflow introduced. Float warnings unchanged from baseline.

## Substantive-cleanliness assessment
- Every substantive VERIFIED finding was closed same-day in-text (incl. the one genuine number-truth catch, OpenAI E5's 15%→23%, which is a prose-vs-model bookkeeping fix — the Table III BFs themselves were already correct per c9k).
- Grok M1 (the only recompute-class finding bearing on a headline claim) was RUN (c9l) and confirms the published ranking; no published number changed.
- Queued items #43–47 are robustness/derivation-audit extensions (META blind-spot tier), none of which contradicts a published number; #43's materiality is bounded because headline coefficients are benchmark-anchored, not A7-derived.
- No reviewer-verified error in any published quantitative claim survives this round.

**P2 ROUND VERDICT: CLEAN** (0 substantive verified E/M outstanding: all verified items closed same-day as presentation/bookkeeping fixes; 1 recompute run confirming published ranking; 5 robustness extensions queued, none contradicting a published number)
