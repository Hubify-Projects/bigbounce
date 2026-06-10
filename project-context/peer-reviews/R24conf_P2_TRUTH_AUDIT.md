# P2 R24conf — TRUTH AUDIT (remaining findings)

**Date**: 2026-06-10 · **Auditor**: closure agent
**Source audited**: `research/focused_paper_source_integration/02_full_draft.tex` (working tree, → v1.7.47)
**Scope**: every SYNTHESIS + META finding NOT closed in-session. In-session closures (marked STALE here, untouched): Claude M1 (verification-row italic relabel), M2 (MC-SE caption sentence), M3 (3–7σ crosswalk), m2 (arXiv 2603 FALSIFIED — valid in June 2026), plus all `_INSESSION` duplicates.
**Verdict counts (52 rows)**: VERIFIED→CLOSED 14 · PARTIAL 6 (4 closed with edits, 2 no-edit) · STALE 14 · FALSIFIED 8 · OPINION 7 · HOUSTON-DECISION 3 · QUEUED 1 (fig4 legend-label regen, queue #42; the only other recompute-class item, Grok M2, was RUN this round as c9k).
**New artifact**: `c9k_gr_continuous_marginalization.py` + `outputs/c9k_gr_continuous_marginalization.json` (Grok M2).

Auto-falsification rules applied: SPHEREx-launch/future-date findings FALSIFIED (SPHEREx launched 2025-03; it IS June 2026); citation-nonexistence claims checked against the .bib + live DOI/arXiv resolution; correction-note-removal + length demands = HOUSTON-DECISION.

## META_REVIEW (8)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| META-E1 | Abstract attributes significance-halving to c=1↔c=2 rescaling while App A.2 proves c-invariance — contradiction | **VERIFIED → CLOSED** | Real internal contradiction. Abstract caveat + conclusion rewritten: halving now attributed to the single-time-ordering content (−2 Im doubling, App A.1), explicitly "not a pure c-rescaling, under which \|fNL\|/σ would be invariant". |
| META-M1 | "Null space" is a fitting artifact, not physical | **PARTIAL (no edit)** | Already extensively scoped (v1.7.43+): "this paper's symmetrization choice", measure-non-invariance disclaimer, ±0.13 demoted to indicative; footnote documents that Cai Eq. 37 coefficients do not transplant (c9i artifact). Reviewer's option (a) requires re-deriving from the full Cai shape — covered by the existing honest-restricted-subset framing. |
| META-M2 | 0.01 squeezed-grid shift vs <0.0002 cutoff claim inconsistent | **VERIFIED → CLOSED** | Both statements true but procedures differ. Reconciliation paragraph added at the x3,min site: cutoff removes near-degenerate squeezed triangles at fixed measure; grid reweighting changes density across all configurations incl. the mismatch-dominating intermediate/folded region. |
| META-M3 | σ_theory=1.0 does NOT encompass Li value −2.1875 (2.19σ away) | **VERIFIED → CLOSED** | Arithmetic confirmed: \|−4.375−(−2.1875)\|/1.0 = 2.19. All 3 "encompassing both values" sites (recommendation ¶, bullet, tab:bayes caption) corrected: ε-range covered within 1σ; Li et al. value at 2.19σ (∼2σ tail, not 1σ); 1σ coverage needs σ_theory ≳ 2.0. |
| META-M4 | r symbol collision (tensor-to-scalar vs template overlap) | **VERIFIED → CLOSED** | Single tensor-to-scalar occurrence (§II D) renamed r_t with explicit disambiguation note. |
| META-M5 | 1/√fsky scaling inappropriate for 3D LSS | **VERIFIED → CLOSED** | Sentence added: CMB-estimator heuristic for the 2D test only; does not transfer to 3D photometric bispectrum; not used in any quantitative forecast. |
| META-M6 | "BF → 1" at QSFI endpoint unfounded | **VERIFIED → CLOSED** | Softened (merged with E6 endpoint fix): shape discrimination weakens; residual BF set by amplitude priors + nuisances; "shape degeneracy alone does not force BF→1". |
| META-m7 | Abstract cites §II C for 0.55–1.14 range that lives in §II A/B | **VERIFIED → CLOSED** | Cross-ref changed sec:assumptions → sec:benchmark. |
| META-m8 | r_cos inner-product measure undefined | **VERIFIED → CLOSED** | Definition verified in `null_space_analysis.py` (cosine of S_bounce=B_NL·S_local vs S_templ∝S_local, unweighted Euclidean over the 23,098-point dimensionless grid; Fisher weight enters r only). Formula + measure added to §II A. |

## OpenAI_methodology (25)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | Table III "BF vs Tuned = 7.0" irreproducible; closed form gives 5.7 | **FALSIFIED** | Reviewer used untruncated W/(√2π σ) = 5.70, ignoring truncation of the uniform [−5,+5] competitor at obs=−4.375 near the prior edge. Exact: Z_b=0.5699, Z_c=(Φ(13.39)−Φ(−0.893))/10=0.0814 → BF=7.00. Reproduced this round and matches committed c9g output. |
| E2 | r=0.84±0.02 inconsistent with range incl. 0.876 | **VERIFIED → CLOSED** | Scoping sentence added at Eq. (r_noise): ±0.02 characterizes the noise-weighted scheme spread; signal-only 0.876 endpoint lies outside the band and is always quoted separately. |
| E3 | Internal artifact filenames in main text | **HOUSTON-DECISION / STALE** | R23 already moved prose mentions to Data Availability; survivors live in footnotes/captions as deliberate provenance audit-trail (repo standard; correction-note class). |
| E4 | σ-levels juxtaposed without non-comparability flags | **STALE** | Abstract labels (CMB Fisher)/(realistic LSS) at every pairing; §IX D (i)/(ii) block + in-session M3 crosswalk close the residue. |
| E5 | AT/BNL definitions inconsistent; "no cancellation" wrong | **STALE** | R23 closure: Eq. (2) is B_NL=(10/3)A_T/Σk³ (reviewer misread the PDF fraction); explicit degree bookkeeping + no-cancellation sentence present at L273. |
| E6 | QSFI squeezed-limit endpoints reversed | **VERIFIED → CLOSED** | Genuine physics error. Chen-Wang scaling: shape/local ∝ (k3/k1)^Δ, Δ=3/2−ν; local limit at μ/H→0 (massless isocurvaton), suppression (k3/k1)^{3/2} at μ/H=3/2. Both sites (§VI C b ¶, §IX D) corrected with correction notes; "structurally compatible regime" → μ/H→0. |
| E7 | 1.75/√(1−0.9692)=10.0 not 7.06 | **FALSIFIED** | Source reads 1.75/√(1−0.969²)=7.06 (PDF text-extraction dropped the superscript). Recomputed: 1.75/0.2469=7.09 ≈ quoted 7.06 (ρ from committed c8 script). |
| M1 | x3,min <2×10⁻⁴ implausibly precise | **VERIFIED → CLOSED** | Same closure as META-M2 (procedures distinguished). |
| M2 | No quantitative combination for 3–5σ | **PARTIAL (no edit)** | Budget chain exists: 6.25σ → ×r → 5.2–5.5 → b_φ 4.0–4.2/3.5–3.7 → GR → 3.0; one-place reconciliation ¶ at §VII end. A single multiplicative table = presentation preference. |
| M3 | 10–20% anomaly-tracer + photo-z 5% unsupported | **STALE** | Both already scoped: "upper bound pending shot-noise-corrected Fisher" + "simplified Fisher degradation estimate" + Pullen/Giannantonio cites (R23). |
| M4 | Convention mapping to Planck/SPHEREx normalization | **STALE** | App A ζ-field 6/5 ↔ Φ-field c=2 exact mapping present (R23 E5 closure). |
| M5 | UV-independence overclaim | **STALE** | §II B retitled "UV-Completion Independence (Conditional...)" with assumption (d) conditioning (v1.7.42). |
| M6 | M(k,z) definition/units | **PARTIAL → CLOSED** | T→1, D(0)=1 already stated; added "wavenumbers k are comoving, in h Mpc⁻¹ throughout". |
| M7 | Table III precise numbers vs "order-of-magnitude only" | **PARTIAL → CLOSED** | tab:bayes caption reworded: entries are exact closed-form evaluations; the order-of-magnitude qualifier applies to interpretation under prior-width variation. |
| M8 | "First time to our knowledge" novelty claim | **OPINION** | Properly hedged ("to our knowledge") + (iii) literature-search statement; supplying a search string would be fabrication. |
| M9 | "Centered on the same value" inaccurate (0.85 vs 0.877) | **VERIFIED → CLOSED** | Replaced: five-set scan value lies within IQR [0.75,0.94], offset ∼0.03 from median; "consistent though not identically centered". |
| M10 | 290 vs 299.2 ratio | **FALSIFIED** | Paper computes 4.375/0.015 = 291.7 ≈ 290 from its own quoted fInf≈0.015 rounding (Perplexity m2 independently verified the same). Using unrounded 0.014625 gives 299; both ≈ "≈290–300" at the quoted precision; internally consistent as written. |
| m1 | r_meas=0.90±0.01 LSS applicability | **STALE** | Full "2D flat-sky CMB-style, not 3D galaxy estimator" clause present (R23). |
| m2/m8 | Figure tick precision | **OPINION** | Cosmetic; no figure regeneration in scope. |
| m3 | Pick one BF bookkeeping | **PARTIAL (no edit)** | r→1 endpoint declared primary; both alternatives quantified in the bookkeeping ¶ (c9j). Structural preference. |
| m4 | Planck PR4 −0.1±5.0 vs PR3 | **FALSIFIED** | §VIII A already cites Jung 2025 PR4 and separately notes PR3 −0.9±5.1 — exactly the check requested. |
| m6 | kη_bounce order-of-magnitude | **STALE** | "Scaling estimate, not a derived bound" present. |
| m7 | Hyphenation artifacts | **FALSIFIED** | U+FFFD "para￾meterized" strings are the reviewer's PDF text-extraction artifacts; source + typeset PDF are clean. |
| n1–n5 | Title caps, A.1 labels, axes, length | **OPINION** (n3 **CLOSED**: "No observational tensions" softened to "We are not aware of…") | Style/structural; length = Houston's call. |

## Grok_brutal (9)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | Correction notes = process language, remove | **HOUSTON-DECISION** | Deliberate transparent disclosure; notes retained (standing decision since R23). |
| E2 | Abstract σ quotes lack convention caveat | **FALSIFIED** | The abstract carries the full convention caveat sentence (now strengthened by META-E1 closure); halved values 2.6–2.75σ / 1.5–2.5σ quoted in-abstract. |
| E3 | Abstract quotes optimistic BF edge as headline | **STALE** | Abstract already leads with recommended BF≈10 baseline, delta-prior 17 labeled theoretical maximum; tab:bayes PRIMARY row is σ_theory=1.0. |
| M1 | Null-space stability insufficient for 5σ claim | **STALE** | c9h percentile propagation (4.4–6.2σ, 16–84%) committed in R23; abstract carries ±0.13 scatter. |
| M2 | Discrete σ_GR grid; need continuous marginalization or <0.1 log-evidence convergence | **VERIFIED → CLOSED (recompute run)** | NEW artifact c9k: continuous U[0,1] marginal BF=6.04 vs tuned (inside discrete 4.7–7.0; 3-point grid converged to 0.007 in log-evidence on that column); BF≈8.6×10³ vs SSFSR (between σ_GR=0.5/1.0 cells). Sentence + artifact added to §VII C + Data Availability. |
| M3 | Fig 2 error bars omit GR/b_φ | **FALSIFIED** | Caption explicitly defines bars as optimistic→conservative endpoint including the full §VII budget (R22prov2 V7 closure). |
| N1 | "First time" needs search string | **OPINION** | Same as OpenAI M8. |
| N2 | "(Dated: June 2026)" anachronism | **FALSIFIED** | It IS June 2026; \date is standard revtex preprint practice. |
| N3 | "We note that" repetition | **OPINION** | Copyedit tier. |

## Gemini_cosmology (10)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| M1 | Correction notes unprofessional | **HOUSTON-DECISION** | Retained (see Grok E1). |
| M2 | Birefringence section dilutes focus | **HOUSTON-DECISION / OPINION** | Deliberately retained with explicit "we do not perform EB cross-power analysis" scoping (v1.7.42 deferral stands; structural). |
| m1 | Abstract BF 5–7 spread hard to trace | **VERIFIED → CLOSED** | Better: it was numerically inconsistent — tab:gr/tab:bayes row gives 4.7–7.0. Abstract corrected to 4.7–7.0. |
| m2 | Signpost the two Fisher analyses | **STALE** | Explicit (i)/(ii) block in §IX D. |
| m3 | Fig 1 slice vs benchmark markers | **OPINION** | Caption states the (k1,k,k) slice; folded marker lies on the slice at k1/k=2. |
| m4 | Joint (fNL,n_fNL) analysis located in Discussion | **HOUSTON-DECISION / OPINION** | Structural relocation; subordinate-cross-check framing is deliberate. |
| m5 | DESI/Euclid/LSST forecasts not like-for-like | **VERIFIED → CLOSED** | Channel-comparability note added to the Complementary Experiments list. |
| N1 | "3-50" sigma garbling | **FALSIFIED** | Source uses $3$--$5\sigma$ correctly; reviewer's extractor mangled σ→0. |
| N2 | "atr fi fbounce" typo | **FALSIFIED** | String absent from source (PDF extraction artifact of math layout); grep confirms. |
| N3 | "kills live lane" colloquial | **PARTIAL (queued)** | Caption already translates the legend label formally; the label itself is burned into fig4 PNG → regeneration queued (R24CONF_COMPUTE_QUEUE). |

## Perplexity_citations (16)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | σ mixing without per-site disclaimers | **STALE** | Same closure set as OpenAI E4. |
| E2 | "Cai & Brandenberger 2014" citation unverifiable/incorrect | **VERIFIED → CLOSED** | Confirmed by live DOI resolution: PRD 90, 023534 (2014) is Kallosh-Linde-Westphal "Chaotic inflation in supergravity after Planck and BICEP2" — wrong paper. True −35/16 source identified and verified: Li, Quintin, Wang & Cai, JCAP 03 (2017) 031, arXiv:1612.02036. Bib entry replaced (key retained, provenance comment added) + 17-site author-attribution sweep (Cai&B / Li&B → Li et al.) incl. App A title and dual-norm table row. |
| E3 | BF recomputes opaque, inputs scattered | **STALE** | Four-corner inline grid + tab:gr caption σ_eff formula + c9g/c9j/c9k artifacts named in Data Availability. |
| E4/E8 | "Same physical bispectrum" / "established" overclaim | **STALE** | §II C closes with "validated through cross-checks rather than a fully independent derivation"; App A.1 gives the operator identity explicitly. |
| E5 | Length/scope | **HOUSTON-DECISION** | Structural; Houston's call. |
| E6 | BF numbers arithmetically inconsistent/undefined | **STALE / FALSIFIED** | All quoted BFs verified against c9g/scipy in R23 + this round (7.00/17.10/9.80/4.01/13.91/5.65 all reproduce); inputs now in tab:gr caption + §VI bullets. |
| E7 | 3–5σ not backed by single budget calc | **PARTIAL (no edit)** | Same as OpenAI M2. |
| M1 | Correction notes | **HOUSTON-DECISION** | Retained. |
| M2 | Informal language ("kills live lane", "headline") | **PARTIAL** | Caption translation exists; figure-label regen queued (Gemini N3); "headline" = defined usage, OPINION. |
| M3 | Novelty overclaim | **OPINION** | Hedged; see OpenAI M8. |
| M4/N2 | SPHEREx "launched March 2025" wrong | **FALSIFIED** | Auto-falsify: SPHEREx launched 2025-03-11; first sky survey completed 2025-12; it IS June 2026. Tense factual. |
| M5 | "Rederivation" language without real derivation | **STALE** | Explicitly scoped: "not undertaken here … validated through cross-checks". |
| M6 | r and σ_eff used three ways | **STALE** | c9j bookkeeping ¶ + §IX D distinction close this. |
| M7 | Abstract validation claims under-quantified | **OPINION** | ℓ-space ±, injection-recovery ±, null-space percentiles all quoted; cosmic-variance/mask depth = future-mock territory, flagged in text. |
| m1–m8, N1 | Degree counting, arithmetic spot-checks, bib metadata, URL format, repetition | **STALE / FALSIFIED (all-clear) / OPINION** | m2/m3 are reviewer all-clears; m4 URL = journal-production preference; m6 ratios shown at their sites (1.19 mask factor etc.); m7 κ_ε two-channel derivation present (v1.7.42). |

## Claude_brutal (non-INSESSION residue, 6)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| E1 | "No existential findings" | **all-clear** | No action. |
| N1 | 3–7σ abstract headline attribution | **STALE** | Abstract ties 3–7σ to the MegaMapper sentence; §VII reconciliation ¶ (in-session M3) gives the crosswalk. |
| m1 | "this is a convention difference" antecedent | **VERIFIED → CLOSED** | "this" → "this factor-of-two discrepancy". |
| m3 | κ_ε / c_1 confusion note unnecessary | **OPINION** | Harmless disambiguation; retained. |
| m4 | Planck recast arithmetic | **all-clear** | Reviewer's own check passed. |
| M1/M2/M3/m2 | (in-session) | **STALE** | Closed by session lead; untouched. |
