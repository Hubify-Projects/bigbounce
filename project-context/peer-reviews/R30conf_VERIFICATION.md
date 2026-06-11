# R30conf — Confirmation Sweep Verification

**Date**: 2026-06-10
**Scope**: Confirmation of R29 patch wave + restamp across all six papers (READ-ONLY on papers).
**Baseline**: commit `120a6d40` (pre-R29-closure); HEAD `dc3c6d84` at time of sweep.
**Method per paper**: (a) every VERIFIED/PARTIAL R29 truth-audit item with a committed fix re-checked in the current stamped `.tex`; (b) pattern-008 scan of ±2 paragraphs around each edit; (c) mechanical battery — `tools/artifact_crosscheck.py`, pattern-045 abstract-vs-body 3-claim spot-check, pattern-048 grep on `git diff 120a6d40..HEAD` changed hunks.

---

## Mechanical battery summary (all six papers)

| Paper | Version | artifact_crosscheck | pattern-045 (abstract↔body) | pattern-048 (changed hunks) |
|---|---|---|---|---|
| P1A `arxiv/paper1a_ech_nogo.tex` | v1A.0.58 | **PASS 0 problems** (1 path OK) | PASS (3/3) | PASS — all keyword hits carry number/pointer/label |
| P1B `arxiv/paper1b_mcmc_companion.tex` | v1B.0.56 | **PASS 0 problems** (17 paths OK) | PASS (3/3) | PASS — zero keyword hits in changed regions |
| P2 `research/focused_paper_source_integration/02_full_draft.tex` | v1.7.50 | **PASS 0 problems** | PASS (3/3) with 1 nit (below) | PASS — all hits labeled (e.g. δf_NL∼10⁻³ "scaling estimate, not a derived bound") |
| P3 `pipelines/p3_anomaly_engine/paper3_draft.tex` | v3.1.89 (+HD-7) | **PASS 0 problems** (5 paths OK) | PASS (3/3) | PASS — 0.24% false-match computed; 4.999″ measured; deferrals labeled |
| P4 `pipelines/p2_chirality/chirality_catalog_paper.tex` | v1.0.173 | **PASS 0 problems** (13 paths OK; `WARN-OLD-COMMIT 297aa805` is the documented pin-policy behavior — 297aa805 IS the v1.0.173 stamp commit, per the E03 convention sentence now in Data Availability) | PASS (4/4) | PASS — zero keyword hits |
| P5 `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` | v0.1.62 | **PASS 0 problems** (23 paths OK) | PASS (3/3) | PASS — zero keyword hits |

pattern-045 claims checked: P1A {13-independent-constraints catalog ↔ §conclusions L2439; perturbation-transparency result ↔ §transparency; N_tot−N_exit≳N_coh erasure ↔ §structural_tension}. P1B {ΔNeff −0.020±0.169 / +0.065±0.17 ↔ L708/951/1221/1238; β̂=0.238° recovery ↔ L1363–1426; H0 67.68±1.06 ↔ L1958}. P2 {BF 9–14 headline ↔ L541/550/587/591/595; 5.2–5.5σ optimistic / 3–5σ realistic ↔ §spherex+§megamapper L501; r∈[0.829,0.876] ↔ §template}. P3 {269,317 catalog-grade lead ↔ Table I footnote ♠ L365; 17.8% novelty ↔ L532; γ=2.567±0.382 ↔ §nanograv}. P4 {z≈−18 block-bootstrap exclusion ↔ App. D (−16.9/−18.4/−19.4 sensitivity, |z|≥17 stable); +3.64/+7.93 dual-value ↔ §III.A + Conclusions reconciliation; 0.41σ dipole ↔ §IV.C.a}. P5 {catalog-wide monopole offset BGS-dominated "consistent with" ↔ §VI.A.d; Cramér's V=0.078 small-effect ↔ L1274 body + abstract; Δf_CW=+0.0007 with explicit sign definition ↔ L276–278}.

---

## P1A — v1A.0.58 (R29 audit: R29_P1A_TRUTH_AUDIT.md)

| R29 item | Status | Evidence (current tex) |
|---|---|---|
| E1 — N_tot≳60 erasure criterion → differential N_tot−N_exit≳N_coh (3 sites) | **HOLDS** | L601 (intro contribution 2), L2291 (limitations), L2350+ (§structural_tension incl. quoted ledger label). Zero residual "N_tot≳60-erasure" phrasings (grep clean; only the e-fold-differential parenthetical retains N_exit∼60 as a parameter value, correct). |
| E2 — Cartan footnote κ²→κ step | **HOLDS** | L754–770: "+κ/2 S·S" intermediate removed; single on-shell substitution stated; κ-power bookkeeping explicitly NOT re-derived, cited to Hehl 1976 Eqs. (3.20)–(3.21) + Freidel–Minic–Takeuchi 2005 Eqs. (7)–(13). `/never-fabricate-derivation` honored. |
| E3(b) — Eq.(1) T·T shorthand + Holst convention footnote | **HOLDS** | New footnote at L670–684: (i) ¼T·T flagged as on-shell Hehl–Datta shorthand, not varied independently; (ii) 1/γ vs 1/(2γ) wedge-factor convention note citing Mercuri2009/Freidel2005. Both cite keys present in `arxiv/references.bib` (L51, L136); compile log zero undefined citations. |
| E4 — bundle label resync | **HOLDS** | Tex L2477: `v1A.0.58-bundle` + byte-identical-except-metadata note; `reproducibility/README.md` L6 `v1A.0.58-bundle` with full v0.9.0→.56→.57→.58 lineage note. |
| META-E1 — Bianchi + pair-symmetry dual route | **HOLDS** | Abstract L406–410 (both routes + metric-compatible qualifier); §X step L1953–1968 (pair-exchange derivation shown, "both routes require T=0 AND metric compatibility; vanishing can fail in non-metric connections"). |
| META-E3 — Route-2 parity relabel | **HOLDS** | New footnote L1303–1325: operator classified parity-EVEN; P-violation from background ⟨∂θ_NY⟩≠0; photon-coupling chain explicitly labeled "amplitude-budget bound and not a derived prediction". |
| (bonus, deferred items closed early) "theorem"→"result" sweep; γ_PTA disambiguation | **HOLDS** | All body "perturbation-transparency theorem" instances now "result" (only residual is a % comment L169); γ_PTA defined vs Barbero-Immirzi γ at Fig. 1 caption + §surviving (2 sites). |

pattern-008: ±2-paragraph scans around all six edit sites show no introduced contradictions; the structural-tension section's "differential ∼32, deeply inside the erasure regime" language is consistent with the new N_coh∼O(few) criterion at every site. HOUSTON-DECISION items (companion imports, EXT1 language, Route-2 β scope) untouched as ruled.

**Verdict: CLEAN**

---

## P1B — v1B.0.56 (R29 audit: R29_P1B_TRUTH_AUDIT.md)

| R29 item | Status | Evidence |
|---|---|---|
| E1 — units-README mislabel → column-permutation diagnosis | **HOLDS** | `parameter_summary_units_README.md` fully rewritten ("Column-Permutation Warning… NOT a units issue", exact column map, numpy.loadtxt verification command, 123,369 post-burn samples). Paper Data-Availability paragraph (L2010–2022) rewritten as "Column-permutation warning", no residual "unit-conversion" framing. |
| E7 — DOI pin v1B.0.54 → \paperVersion | **HOLDS** | L2079: `pinned to the \texttt{\paperVersion} commit` — tracks tag automatically. |
| E10 — 2.0σ DES-Y3 relabel | **HOLDS** | L973–984: "within-stack readout… not a measurement-vs-measurement tension but a within-stack posterior shift". Only one 2.0σ site in paper; no contradicting residual. |
| M3 — CMB-S4 σ(Neff)∼0.03 citation | **HOLDS** | `\cite{CMBS4_ScienceBook}` at both sites (L1194, L1961); key defined in references.bib L1142; "first precision test" softened to "will sharpen this constraint substantially" at both sites. |
| M10 — overlap-integral definition | **HOLDS** | L973–977: p1/p2 defined as 1-D S8 marginal densities on common ΔS8=10⁻⁴ trapezoid grid over [0.70,0.90]. |
| Grok-M3 — one-sided convention | **HOLDS** | L887–893: renormalised-on-ΔNeff≥0 CDF construction stated explicitly, applied to both 0.31 and 0.39 limits. |
| Gemini-M2 — garbled `//)` formula | **HOLDS** | grep `//)` returns zero hits; β equation rewritten as aligned display with explicit C_aγ and Δφ/f_a factors (L1678–1687). |

pattern-008: surrounding text consistent; abstract "consistent with zero" claims match Table I / CORRECTED.json values at all four body sites.

**Verdict: CLEAN**

---

## P2 — v1.7.50 (R29 audit: R29_P2_TRUTH_AUDIT.md)

| R29 item | Status | Evidence |
|---|---|---|
| E1 — abstract rewrite (caveat consolidation, confident scoped tone) | **HOLDS** | Abstract now 5 structured paragraphs (L322–333); all informational content preserved (assumptions (d)/(e)/(f), CFC scope, r bookkeeping, systematic budget, BF illustrative qualifier, convention sensitivity); novelty claim now "We quantify the template mismatch…" (no "for the first time"), /never-claim-n4 compliant. |
| E2 — title drop "and Forecasts" | **HOLDS** | Title: "…A SPHEREx Sensitivity Recast with a MegaMapper Outlook". |
| E3+M7 — covariance OOM dimensional fix + 10⁻³/1% reconciliation | **HOLDS** | New labeled Eq. (eq:fiducial_shift): δC/C ∼ f_NL²Δζ²/N_modes, dimensionless throughout; f_NL²Δζ²∼4×10⁻⁸ computed; propagated δσ/σ∼½δC/C ≲5×10⁻⁴ — single consistent bound replaces the inconsistent 10⁻³-vs-1% pair. |
| E4 — assumption-(f) fermion bound → labeled assumption | **HOLDS** | §assumptions: dimensional pseudo-formula removed; "A rigorous order-of-magnitude bound… is not undertaken here. We therefore treat assumption (f) as an externally imposed constraint… per-model bound… required". No fabricated derivation. |
| M1 — Wick orbit 6/3=2 derivation | **HOLDS** | Footnote in §template now derives \|S₃\|/\|stab\|=6 (trivial little group), C₃ orbit of size 3 for the single time-ordering monomial k₁⁷k₂²+k₂⁷k₃²+k₃⁷k₁², ratio \|S₃\|/\|C₃\|=6/3=2, orbit-by-orbit rescaling. |
| M3/M4 — BF rebooking 10–17 → 9–14 headline | **HOLDS, no contradictions** | Abstract leads BF≈9 up to ≈14 (noise-weighted r≈0.84 bookkeeping) with r→1 endpoint 10–17 routed to Table tab:bayes. All five downstream sites consistent: L541 (§bayesian sensitivity paragraph), L550, L587 (tab:bayes caption footnote b), L591, L595 (QSFI closure paragraph). pattern-008 clean — no body site still presents 10–17 as "the abstract envelope" without the rebooking note. |

**Non-blocking nit (new, from abstract rewrite)**: abstract ¶2 states a local estimator "recovers 84%–88% of the bounce signal" while the same sentence's parenthetical gives r ∈ [0.829, 0.876] (lower endpoint 82.9%) and "noise-weighted r ≈ 0.83"; body uses r = 0.84 ± 0.02 ([0.82, 0.86]). Recommend "83%–88%" or "≈84% (range 83–88%)" at the next touch. Not a contradiction in conclusion-bearing values (the recast uses r≈0.83–0.84 consistently); rounding-presentation only.

Deferred-by-audit items confirmed still open as intended: M8 `[Correction note]` blocks (HOUSTON-DECISION, e.g. L595), M2 Zenodo checklist, M6 Fig. 4 PNG.

**Verdict: CLEAN** (one rounding nit logged for next pass; non-blocking)

---

## P3 — v3.1.89 + post-stamp HD-7 (R29 audit: R29_P3_TRUTH_AUDIT.md)

| R29 item | Status | Evidence |
|---|---|---|
| ESS-01 — §III.E body S=1.084 vs membership-only | **HOLDS** | §erosita headline finding now "the rank-1 entry of the n=298 membership list (1eRASS J053856.1−640457; S_BigAE irreproducible per Table caption — see membership-only framing)"; no quantitative S printed in body prose. |
| ESS-02 — abstract eROSITA membership-only disclosure | **HOLDS** | Abstract parenthetical present: "(eROSITA tier released as a n=298 membership list only; per-object S_BigAE score axis non-reproducible on any of 16 monotone rescalings; see §III.E)". |
| ESS-03 — r23conf_dedup_audits.json path drift | **HOLDS** | Both former bare-`\texttt` sites now `\artifact{pipelines/p3_anomaly_engine/pathc_dedup/r23conf_dedup_audits.json}`; artifact_crosscheck verifies path OK on disk. |
| M-17 — byte-identical parquet pair | **HOLDS** | DATA_RELEASE_MANIFEST.md L16–17: identical SHA-256 documented, "_no_act file is canonical", ACT-zero-overlap rationale cited to §planck_act_null. |
| E-07 — Conclusions "is projected" | **HOLDS (closed in v3.1.89)** | Now "is forecast … conditional on future survey execution and anomaly-tracer calibration; it is not a projected detection at current data quality"; §systematics paragraph likewise "The conditional SPHEREx multi-tracer forecast… contingent on…". |
| E-08 — Table I eROSITA 0.03 rate footnote | **HOLDS** | Rate cell now `0.03$^\#$` with new # footnote: predetermined fixed-count, score-knee top-cut, "rate cell should not be interpreted as an independent measurement". |
| E-09 — high-z z=6.20 confirmed-style language | **HOLDS** | "pipeline-inferred z = 6.0–6.23 (spectroscopic confirmation required)"; both TARGETID redshifts qualified "pipeline-inferred… photometric-pipeline estimates requiring spectroscopic confirmation". |
| E-10 — fig_fnl_improvement superseded label | **HOLDS** | Caption opens "Legacy fixed-α reference — superseded by the empirical α_jk result of §V". |
| E-11 — abstract NANOGrav environmental caveat | **HOLDS** | Abstract: "environmentally modified SMBHB models with eccentric binaries or stellar-scattering-driven hardening can produce γ∼2.5–3, so this Bayes factor is decisive only against the idealized circular-orbit reference — see §nanograv". |
| Citation pass (Perplexity items) | **HOLDS** | Nicolaou2026 → MNRAS 547 + arXiv:2506.17376; DESI2025DR1 → AJ accepted, arXiv:2503.14745; ACT_DR6 + arXiv:2304.05202; LAMOST_DR10 repointed to DR10 release URL + Cui et al. RAA 12, 1197 (2012) survey paper (resolves the unresolvable Luo RAA 2024 entry). |

**HD-7 abstract coherence check (post-stamp)**: the abstract now leads with "the recommended **catalog-grade tier contains 269,317 unique entries** (269,117 point-source…), drawn from a full Path-C unique catalog of 378,280 anomalies" — reads coherently; the 378,280 is explicitly subordinated as the full-catalog envelope. No contradicting 378,280-leading claim: the title ("…378,280 Path-C Unique Anomalies…") and body sites (L322 "Canonical catalog", L360 "primary result", L758 Conclusions Scale bullet, L782 Data Availability) all describe 378,280 as the full/canonical catalog count — a role statement, not a recommendation statement — and each carries the stratification/tier framing. Consistent with the abstract's catalog-grade-leads framing. Minor non-blocking redundancy: the 269,317 provenance parenthetical now appears twice in the abstract (leading sentence + retained downstream sentence); harmless duplication, candidate for condensation at next touch.

**Verdict: CLEAN** (Zenodo DOI placeholder + LAMOST RAA/eROSITA A&A spot-checks remain pre-arXiv Houston items per audit, unchanged status)

---

## P4 — v1.0.173 (R29 audit: R29_P4_TRUTH_AUDIT.md)

| R29 item | Status | Evidence |
|---|---|---|
| E01 — NSIDE block-scale sensitivity | **HOLDS** | Appendix D footnote now reports the computed sweep: z = −16.9 (NSIDE 4, ~127 sp) / −18.4 (NSIDE 8, ~439 sp) / −19.4 (NSIDE 16, ~1631 sp), inflation 15.7×/14.4×/13.7×, "headline exclusion \|z\|≥17 stable", artifact `outputs/canonical_provenance/block_bootstrap_nside_sensitivity.json` (verified on disk by crosscheck). The old "No sensitivity test… has been computed" sentence is gone. pattern-008: headline z≈−18.1 (N_boot=1000) vs sensitivity −18.4 (N_boot=500) coexist with the run-size distinction explicit; abstract's "z≈−18" consistent with both. |
| E02 — NS gallery panel | **HOLDS** | Fig. 1 is 3-panel (0.32/0.32/0.32) with `fig_gallery_notspi.png`; file exists at `figs/` and the legacy symlink resolves; caption's new "~62% would leak" claim is supported by two existing body sites (Table I caption "non-spiral galaxies (∼62% of the catalog)" and §V weight-map paragraph). `\NS` macro defined (L51). Compile log: zero undefined refs (only a benign OT1 bold-smallcaps font-shape substitution warning). |
| E03 — Data Availability hash + convention note | **HOLDS** | Hash re-pinned to `297aa805` (= the `feat(P4 v1.0.173)` stamp commit, per follow-up commit 5565cf72); convention sentence present ("hash advances only at explicit paper-version restamps"). artifact_crosscheck WARN-OLD-COMMIT is the documented expected false positive under this pin policy. |
| E04 — +3.64σ twin-meaning bridge | **HOLDS** | Conclusions Canonical-N paragraph now carries the full reconciliation (+3.64 = 500-MC, Gaussian-equivalent ≈1.9σ; +7.93 = 10⁴-perm recompute of same estimator; cross-refs §III.A + Table III caption). §III.A MASTER z-definition corrected to z = (C₁^data − ⟨C₁⟩_null)/σ_null (OpenAI E8). |
| META-m9 — Table I row vi +1.68→+1.69 | **HOLDS** | Table I row (vi) = +1.69; §monopole_mask_null body text = +1.69; harmonized, no residual 1.68. |
| Claude N07 — §IV.A correction note → footnote | **HOLDS** | The 0.43→0.41 regeneration note is now a `\footnote{}` with artifact link; inline `[Correction note:…]` removed from the paragraph. |

HOUSTON-DECISION items (META-E1 augmentation order, Shamir 6–12 footnote, Zenodo DOI, abstract length, App. A.d prose) confirmed untouched as ruled.

**Verdict: CLEAN**

---

## P5 — v0.1.62 (R29 audit: R29_P5_TRUTH_AUDIT.md)

| R29 item | Status | Evidence |
|---|---|---|
| E29-2 — "catalog-level" terminology sweep | **HOLDS** | All four headline-equivalent sites converted: abstract (iii) "catalog-wide monopole offset"; §within_class_density heading paragraph + multiplicity paragraph "catalog-wide-monopole-projected −4.7σ"; sky-scan conclusion "catalog-wide monopole offset is not environment-driven". The 4 remaining `catalog-level` hits (L1310, L1861, L1930, L2109) are exactly the audit-sanctioned non-headline monopole-construct references (bright-vs-dark difference; "carries the full catalog-level monopole" ×2; Paper-IV 9.5σ citation). |
| E29-3 — abstract "confirmed by" → "consistent with" | **HOLDS** | Abstract: "consistent with a tracer-program decomposition in which the catalog-wide monopole offset is dominated by the BGS-bright sample"; zero "confirmed"/"entirely driven" residuals in abstract; cannot-partition caveat retained downstream. |
| M29-1 — Cramér's V small-effect qualifier | **HOLDS** | Abstract: "Cramér's V=0.078 — a small effect by conventional standards, with the χ² driven by sample size n=811,609 rather than effect magnitude —". Matches body §VI.A.d framing. |
| M29-3 — "≤0.01 SE" Wald-shift correction | **HOLDS** | §logistic control: "≤0.12 on their standard errors (void 0.006σ̂, wall 0.10σ̂, cluster 0.11σ̂; shifts computed as \|β_M1−β_M0\|/SE_M0 from \artifact{…27_ext1_logistic_program_control.json})" — matches the audit's recomputed values exactly. |
| (bonus closures of parked items) Meta-E2, Meta-E1, Meta-M1, Gemini-E1 | **HOLDS** | Meta-E2: two void-volume denominators disambiguated (V-Web 24.4% cell volume vs 0.1% DESIVAST-sphere cells, with artifact link). Meta-E1: 885 (NSIDE 32) vs 297 (NSIDE 16) cross-noted at BOTH the body site and the Fig. caption. Meta-M1: resolved-cells header restated "Rs ≳ cell size = 25.9 Mpc/h; Rs ∈ {25,50} retained". Gemini-E1: Δf_CW sign fixed via explicit definition Δf_CW ≡ f_CW^non-void − f_CW^void = +0.0007 (L276–278). |

pattern-008: surrounding text at all edit sites consistent; "concentrated entirely in the 0-maximal-voids bin" retained in abstract is the (separate, factual) stratification statement, not the softened causal claim — correct scope. Remaining batched MINOR/NIT items (Table IV residual-sign header, Table XII recompute, binomial-formula parentheses, n=782,710 vs 783,820 half-sentence) stay open per the audit's own next-pass disposition; none are regressions.

**Verdict: CLEAN**

---

## Final verdicts

| Paper | Version | Verdict | Blocking items |
|---|---|---|---|
| P1A | v1A.0.58 | **CLEAN** | none |
| P1B | v1B.0.56 | **CLEAN** | none |
| P2  | v1.7.50  | **CLEAN** | none (1 non-blocking abstract rounding nit: "84%–88%" vs r lower endpoint 0.829) |
| P3  | v3.1.89+HD-7 | **CLEAN** | none (pre-arXiv Houston items unchanged: Zenodo DOI, LAMOST RAA / eROSITA A&A spot-checks; abstract 269,317-provenance duplication is a cosmetic condensation candidate) |
| P4  | v1.0.173 | **CLEAN** | none |
| P5  | v0.1.62  | **CLEAN** | none |

**R30conf result: 6/6 CLEAN.** Every R29 VERIFIED/PARTIAL committed fix is present and correct in the current stamped tex; no pattern-008 closure-introduced regressions found; mechanical battery passes on all six papers. HOUSTON-DECISION items remain parked exactly as ruled in the R29 audits and the EXT1 decision ledger (cdb0b581).
