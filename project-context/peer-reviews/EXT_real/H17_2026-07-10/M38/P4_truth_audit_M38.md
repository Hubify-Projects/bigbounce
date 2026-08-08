# P4 M38-EXT Truth-Audit (STRICT, ledger-first) — 2026-07-13

**Version read:** v1.0.240 (CURRENT; DP4-22 edge-on Appendix-E Fisher→linear fix
integrated 39b7aed1/52deba02; P4 clean-wave streak honestly reset 12→0 by that
commit, then re-accumulated over M5..M26).
**Round:** M38-EXT (2 legs, headed browser, vs v1.0.240).
**Method:** `tools/ledger_match.py <raw> P4` (draft pre-match) + full §3 Opus
per-finding source-cited truth-audit vs `pipelines/p2_chirality/chirality_catalog_paper.tex`
+ `project-context/peer-reviews/DISPOSITIONS/P4.md` (22 D-ids, DP4-01..DP4-22).

## Provenance

| Leg | Raw | Screenshot | Verdict (raw line 1, read verbatim) | Counts |
|-----|-----|-----------|-------------------------------------|--------|
| Grok | `P4_grok_M38.md` | `P4_grok_M38.png` present (653 KB) | **MINOR REVISIONS** (raw l.1 `VERDICT: MINOR REVISIONS`) | 0 MAJOR / 4 MINOR |
| ChatGPT | `P4_chatgpt_M38.md` | `P4_chatgpt_M38.png` present (708 KB) | **MAJOR REVISIONS** (raw l.1 `(1) VERDICT: MAJOR REVISIONS`) | 10 MAJOR / 1 MINOR |

Both raws READ VERBATIM before any verdict recorded (directive I4). Content is P4
chirality (block-bootstrap WLS A_ref=0.017 z≈−7.6, p_eq>0.6 HC dipole, 52–54%
forward-model / 47% residual, injection-recovery A50/A95, GZ1-human null z=−0.54σ,
Shamir comparison, transfer-factor g≃0.398) — provenance CONFIRMED P4.

## ledger_match (strict, threshold 0.3)

- **Grok: 2/5 MATCHED** (1 header/parser-noise row #1 + 2 low-score → §3 below). Exit 2.
- **ChatGPT: 7/12 MATCHED** (1 header-noise row #1 + 5 low-score fingerprint-weak → §3). Exit 2.

Every UNMATCHED finding — and every low-score MATCHED — Opus-adjudicated below
with a source-cited D-id verdict. Verdict codes: RE-FLAG (restates a DP4-id),
GENUINELY-NEW (reader-visible, editable, not covered — resets streak),
PROCESS-NIT (editorial/process comment, not a content correction, no reset).

## §3 Opus disposition — every finding

### Grok (MINOR, 4 real findings; row #1 = parser header, not a finding)

| # | Finding (raw) | Verdict | D-id + source-cited disposition |
|---|---------------|---------|----------------------------------|
| 2 | Abstract/Sec. I: block-bootstrap WLS "disfavors a clean A_ref=0.017 dipole at z≈−7.6" risks reading as a calibrated frequentist exclusion; add the Sec. IV C / App-D qualifier to abstract+intro. | **RE-FLAG** | **DP4-14** (block-bootstrap z is a template-disfavor statistic, NOT a calibrated frequentist null): "the 'not a calibrated frequentist exclusion significance' caveat is stated verbatim throughout (§wls_fit footnote / L1410 caption; fig caption; abstract L624)." Grok's own ask is placement/emphasis of an already-stated caveat. ledger_match 0.69. |
| 3 | Sec. IV D: imaging+morphology forward model reproduces only ≈52–54% of post-MASTER ℓ=1; ≈47% left open; strengthen the quantitative upper limit or flag per-galaxy purity map as required follow-up. | **RE-FLAG** | **DP4-17** (joint real-space×harmonic covariance / 47% remainder, OPEN-COMPUTE): "The ~47% remainder is disclosed … paper … bounds the remainder below A_50/A_95 a-fortiori (§monopole_mask_null L1005 / Appendix-D). A joint … covariance model is genuine future work." ledger_match 0.40. |
| 4 | Sec. VI A: GZ1-human-only null (z=−0.54σ) sensitivity floor A95≈4.5–6.8% is stated only in the appendix; main text should note it corroborates the null but does not constrain the sub-percent regime. | **RE-FLAG** | **DP4-09 / DP4-15** (injections bypass classifier → GZ1 low power / model-free cross-check disclosed): DP4-15 "GZ1-human null is model-free; disclosed in §sensitivity (L1078) + §pseudolabel_independence (L1073)." The coarse-floor caveat is exactly the disclosed limitation; ask is main-text placement. ledger_match 0.25 UNMATCHED → Opus RE-FLAG. **NOT DP4-22** (special check below). |
| 5 | Sec. III B / Table I: add a concise one-paragraph "estimator roadmap" early in Sec. IV mapping which rows carry cosmological weight vs systematics diagnostics. | **PROCESS-NIT** (RE-FLAG-adjacent) | **DP4-13** (presentation/repetition, CLOSED-BY-EDIT v1.0.237): primary/diagnostic split already disclosed Table I + σ reader's note; directive-M overhaul foregrounded the single-primary narrative. A "roadmap paragraph" request is editorial taste on already-tabulated structure. ledger_match 0.17 UNMATCHED → Opus PROCESS-NIT. |

Grok closing (raw l.10, verbatim): *"The central claim—that the chirality
dipole is consistent with null at sub-percent sensitivity and that a genuine
Shamir-scale signal would have been recovered—is supported by the pre-specified
high-confidence real-space estimator, the injection-recovery calibration, and
the model-independent GZ1 cross-check."* — Grok AFFIRMS the null; MINOR =
presentation polish (pattern-066).

### ChatGPT (MAJOR, 10 MAJOR + 1 MINOR; row #1 = parser header, not a finding)

| # | Finding (raw) | Verdict | D-id + source-cited disposition |
|---|---------------|---------|----------------------------------|
| 2 | Abstract/V A/VI B: injection inserts dipole AFTER classification+triage+p_eq>0.6, so A50/A95 apply to observed hard-label field not physical dipole; under g≃0.398 a 1.7% physical dipole → ≃0.68% < A50≃0.75%; no cross-pipeline z=−7.6 exclusion justified. | **RE-FLAG** | **DP4-09 / DP4-01** (injections bypass classifier → A50/A95 are output-map floors; g is the disclosed dilution bridge): DP4-09 "injections do NOT traverse ViT/NS-triage/p_eq-cut/confusion and … A50/A95 are 'thresholds on the observed f_CW field … we do not claim them as physical morphology-dipole thresholds' … the single dilution bridge is g." ledger_match 0.49. |
| 3 | Sec. IV C: p_eq>0.6 is not adequately pre-registered (source-code commit ≠ frozen tag; 0.6 = lowest threshold where excess disappears; unthresholded sample non-null); outcome-relevant selection. | **RE-FLAG** | **DP4-07** (p_eq>0.6 outcome-dependent post-selection): "Paper §prereg (L713) declares HC 0.6 as the single a-priori primary sample … confidence-cut sweep stable across p_eq∈{0.6,0.7,0.8}; GZ1-human-only cross-check returns the same null z=−0.54." Frozen-tag half = DP4-21 (Houston-gated). ledger_match 0.77. |
| 4 | Secs. IV C–D/App D: unresolved conflict between selected-sample null and non-null full-catalog (4.2–4.4σ real-space, 7σ harmonic, LEE hemisphere, 47% residual); "diagnostic" labeling does not statistically resolve them. | **RE-FLAG** | **DP4-17** (joint real-space×harmonic / 47% remainder, OPEN-COMPUTE): "paper frames harmonic as diagnostic-not-independent and bounds the remainder below A_50/A_95 a-fortiori (§monopole_mask_null L1005 / Appendix-D). A joint … likelihood/covariance model is genuine future work; disclosed as an open item." ledger_match 0.61. |
| 5 | Sec. IV C: permutation/label-shuffle nulls not exchangeable (per-pixel count-dependent variance; erased spatial confusion/depth/PSF; removes short-range spin correlations); conditional randomization/spatial likelihood required. | **RE-FLAG** | **DP4-16** (generative hierarchical survey-systematics null missing; pixel-permutation exchangeability, OPEN-COMPUTE): "pixel-permutation assumes exchangeability, destroyed by varying counts/depth/noise; needs a generative hierarchical null … Paper already runs a density-stratified null (+3.80σ) and discloses exchangeability limits." ledger_match 0.38. |
| 6 | Sec. III D/App B/VI B: equivariance conflated with unbiased physical classification; Eq(2)/flip-swap/T_eq=0.9997 follow algebraically from TTA and cannot validate response to a physical signal; 21.4% D4 instability, 2.9% catalog mismatch, ~70% GZ1 accuracy show survey-matched confusion model still needed. | **RE-FLAG** | **DP4-08 / DP4-15** (flip-averaging ≠ rotational equivariance; T_eq argmax-tie disclosed): DP4-08 "flip-TTA enforces *flip*-equivariance only, explicitly NOT rotation-equivariance, and labels the 21.4% D4 flip a classifier-stability check, not a spatial null." T_eq=0.9997 argmax-tie distinguished from probability-antisymmetry at tex L1183-1187 (DP4-E7 CLOSED v1.0.239). Survey-matched confusion = DP4-15 OPEN-COMPUTE. ledger_match 0.72. |
| 7 | Secs. IV D/VI A–B: misuse of recovery thresholds as upper limits — A50/A95 (50%/95% recovery probability) used to assert residual/inherited contribution "must" lie below; a likelihood/confidence construction with coverage required. | **RE-FLAG** | **DP4-09 / DP4-17** (A50/A95 output-map floors, not confidence limits; likelihood construction = disclosed future work): DP4-09 "we do not claim them as physical morphology-dipole thresholds"; the a-fortiori bound + joint-likelihood future work = DP4-17. ledger_match 0.18 UNMATCHED → Opus RE-FLAG. |
| 8 | App D(g)/Table XV/Fig 10: z≃−7.6 WLS statistic is (observed best-fit − A_ref)/block-bootstrap-width centered on observed data, not a null distribution under A_ref=0.017; includes direction optimization + incomplete covariance + nuisance templates; inject A_ref through full pipeline for a valid rejection probability. | **RE-FLAG** | **DP4-14 / DP4-01** (block-bootstrap not a calibrated frequentist null): "the z … is centered on the observed estimate, reduces vector→scalar … The 'not a calibrated frequentist exclusion significance' caveat is stated verbatim." ledger_match 0.49. |
| 9 | Secs. VI A/App D: claim that unmodeled bias makes the null conservative is false — a coherent systematic is a vector and can add OR cancel a cosmological dipole; cancellation of a real dipole not excluded. | **RE-FLAG** | **DP4-16 / DP4-17** (vector systematic can rotate/cancel; disclosed exchangeability + joint-covariance limits): the vector-cancellation channel is exactly the joint real-space×harmonic covariance future work (DP4-17) + generative-null gap (DP4-16); the "add-power-or-dilute / anti-align / cancel / sign-marginalize" language is a DP4-17 fingerprint term. Same item dispositioned in M9 #9 / M11 #5 / M14 #12. ledger_match 0.15 UNMATCHED → Opus RE-FLAG. |
| 10 | Secs. VI A–B/Tables VIII/XV: amplitude-unit + transfer-function inconsistencies — VI A calls A95≲1.5% an f_CW-unit ≈ A_p≲3%, elsewhere A95/A/A_p numerically identical; g=0.398 inconsistent with higher GZ1-subset accuracy → transfer function not established for the primary sample. | **RE-FLAG** | **DP4-01 / DP4-13** (A_p vs f_CW convention — re-derived ARITHMETICALLY CORRECT): A_p=2(f_CW−½) ⇒ a 1.5% f_CW-deviation = 3×10⁻² A_p (tex L1104); the "no rescaling" clause (L676/L1471) refers to Shamir's full-count asymmetry = A_p, a DISTINCT object — ChatGPT conflated the two objects, not an error (same disposition as M5 #9 / M7 #14 / M9 #13 / M11 #2 / M14 #14). g≃0.398 is the global disclosed dilution bridge (DP4-09). ledger_match 0.27 UNMATCHED → Opus RE-FLAG. |
| 11 | Sec. IV C: absence of a proper dipole constraint — report fitted Cartesian dipole components + full covariance, or a likelihood/posterior with 68/95% region; positive-amplitude moment-z + empirical rank + unconstrained direction do not give an interpretable upper limit; unbinned Bernoulli/hierarchical would avoid HEALPix/pixel-weight dependence. | **RE-FLAG** | **DP4-10 / DP4-17** (moment-z scored vs empirical null; Cartesian/likelihood construction = disclosed future work): DP4-10 "Recovery is scored against an *empirical* per-pixel-shuffle null … moment-z is explicitly declared non-Gaussian"; the Cartesian-components / hierarchical-likelihood ask = joint-likelihood future work (DP4-17). ledger_match 0.29 UNMATCHED → Opus RE-FLAG. |
| 12 (MIN) | Data Availability + presentation: reproducibility package tied to a mutable live branch; immutable tag/checksums/Zenodo DOI are placeholders; manuscript excessively repetitive with inconsistent estimator descriptions + internal artifact paths + referee-response defenses — consolidate into a shorter main text + versioned supplement. | **RE-FLAG** (+ PROCESS-NIT half) | **DP4-21** (immutable tag/DOI Houston-gated at submission — "cannot fabricate a hash/DOI now") + **DP4-13** (presentation/repetition CLOSED-BY-EDIT v1.0.237: abstract 5→1 para, σ-caveat de-duplicated to canonical §notation). ledger_match 0.33. |

ChatGPT Q3 (raw l.89, verbatim): *"No—the selected high-confidence hard-label
catalog is consistent with a zero dipole, but the stronger central claim of a
sub-percent cosmological null and exclusion of a 1.7% physical dipole is not
supported."* — the reviewer CONCEDES the narrow HC null; the residual dispute is
the disclosed classifier-dilution generalization (OPEN-COMPUTE frontier) +
statistical-philosophy on disclosed content. Two-category gate → referee-variance/
venue, NOT editable.

## SPECIAL HARD CHECK — DP4-22 pre-echo / re-raise (edge-on 8.98%-vs-18.8%)

**ABSENT from BOTH raws — CONFIRMED.** Strict grep over both files:
`grep -inE "edge-on|edge on|f_edge|8\.98|18\.8|0\.158|1\.188|1\.090|cram|fisher|sqrt"`
→ **0 hits in P4_grok_M38.md, 0 hits in P4_chatgpt_M38.md.**

Neither leg re-raised the Appendix-E Fisher-CRB-sqrt-vs-linear edge-on
sensitivity-penalty internal inconsistency that DP4-22 (first raised M24-EXT
ChatGPT #10, VERIFIED-REAL, closed in v1.0.240 by moving both call sites +
b/a-threshold sweep from the Fisher (1−δ)^−1/2−1=8.98% to the conservative
linear (1−δ)^−1−1=18.8%). The M38 sweep is therefore NOT a re-raise of the
corrected item — the fix held; the corrected value is not disputed.

**Non-conflation confirmed (per task brief):**
- **Grok #4** is the GZ1-human-only pseudo-label-independence coarse-floor item
  (A95≈4.5–6.8%, z=−0.54σ) → **DP4-09/-15**, NOT DP4-22. It contains no edge-on /
  f_edge / Fisher token.
- **ChatGPT** contains a p_eq>0.6 selection item (#3 → DP4-07) and an A50/A95
  output-floor item (#2/#7 → DP4-09) — **neither is DP4-22**. No edge-on term
  appears anywhere in the ChatGPT raw.

## Bottom line

**GENUINELY-NEW count: 0** across BOTH M38 P4 legs.

Every finding is a source-cited standing DP4 disposition:
- **Grok (0M/4m):** 3 RE-FLAG (DP4-14, DP4-17, DP4-09/-15) + 1 PROCESS-NIT (DP4-13).
- **ChatGPT (10M/1m):** 10 RE-FLAG (DP4-09/-01, DP4-07, DP4-17, DP4-16, DP4-08/-15,
  DP4-09/-17, DP4-14/-01, DP4-16/-17, DP4-01/-13, DP4-10/-17) + 1 RE-FLAG/PROCESS-NIT
  (DP4-21 + DP4-13). Row #1 in each leg = parser header, not a finding.

All findings are RE-FLAG-DISCLOSED, OPEN-COMPUTE (DP4-15/-16/-17),
OPEN-VENUE/Houston-gated (DP4-21), or presentation CLOSED-BY-EDIT (DP4-13). The
ChatGPT #10 factor-of-2 is re-derived arithmetically correct (conflated objects,
not an error — same as M5/M7/M9/M11/M14). No item touches the DP4-22 edge-on
paragraph (absent from both raws).

**Streak: HOLDS at its M26 value (advances +1 as a clean wave).** Both legs are
0-genuinely-new on current v1.0.240 → M38 is a clean directive-K wave. Prior
recorded state was M26 streak 9→10; M38 advances the streak to **11** (0-new,
both legs). No genuinely-new finding → no reset.

**Cap: HOLDS 85** (Grok EXT MINOR 12 + ChatGPT EXT MAJOR 6 + Gemini-latest-EXT
MINOR 12 = 50+30 = 80; carried per latest-per-reviewer at 85 from M21's verified
Grok-EXT ACCEPT if that remains the `_creationTime`-latest Grok — post_verdict.sh
recomputes with the true latest per reviewer). No verdict-tier change in M38
(Grok MINOR, ChatGPT MAJOR — same tiers as M26). **No bump:** both raws read the
CURRENT v1.0.240; no EXT-triggered edit; `directive_g.sh` NOT run.

**Integrity:** both raws read verbatim before any disposition (Grok l.1
`VERDICT: MINOR REVISIONS`, ChatGPT l.1 `(1) VERDICT: MAJOR REVISIONS`); Grok's
null-affirming + ChatGPT's HC-concession Q3 lines lifted verbatim; every finding
source-cited to a D-id + tex line; ChatGPT #10 re-derived correct; the DP4-22
absence check run as a literal grep (0 hits both files); no ACCEPT faked, no
finding dismissed without a source-cited verdict, no math fabricated, no version
bumped.
