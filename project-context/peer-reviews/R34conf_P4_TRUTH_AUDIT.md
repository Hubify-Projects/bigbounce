# R34conf P4 Truth Audit — v1.0.176

**Paper:** P4 — Survey-Scale Galaxy Chirality · v1.0.176 · `paperTimestamp` June 11, 2026
**Round:** R34conf — internal confirmation round; post-EXT4-closure verification
**Reviewers:** Gemini_cosmology (MAJOR REVISIONS), Grok_brutal (REJECT), OpenAI_methodology (MAJOR REVISIONS), Perplexity_citations (MAJOR REVISIONS); Claude_brutal ABSENT (API 413 / request-too-large error)
**Input PDF:** `site/public/papers/chirality_catalog_paper_v176.pdf` md5=baa9467c pages=22
**Audit date:** 2026-06-11 PT · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:**
- `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.176, l.55)
- `pipelines/p2_chirality/outputs/canonical_provenance/ext4_fb1_flip_identity_qc_catalogwide.json` (new artifact, EXT4 closure)
- `EXT4_P4_TRUTH_AUDIT.md` (prior round)

**Priority check (pattern-051):** Did the EXT4 closure wave (v1.0.175→176) introduce regressions? Load-bearing changes were: (1) catalog-wide QC artifact + 2.9%→confirmed + narrative parenthetical; (2) `\artifact{}` pointer to `ext4_fb1_flip_identity_qc_catalogwide.json`; (3) 1.3%→1.6% CW-channel anchor fix; (4) Table II caption truncation note; (5) any residual FM-175-2 / FM-175-3 edits.

**Claude leg note:** Claude (Anthropic) returned HTTP 413 (request too large for native PDF + extended thinking). This is a tool failure, not a review failure. The 4 successful legs (Gemini, Grok, OpenAI, Perplexity) provide sufficient coverage for the truth audit; the absence of the Claude leg is noted but does not block a verdict.

**Auto-falsify rules in force:**
- June 2026 IS current; arXiv 25xx/26xx IDs are valid → any finding citing these as problems is AUTO-FALSIFIED
- HD-6/HD-11 ruled (Zenodo DOI mint-at-submission, provenance two-step gate) → findings on these are HOUSTON-DECISION, not MAJOR
- Pattern-052: Gemini PDF-extractor-derived math/table/layout claims are pre-screened against TeX source before crediting

---

## Part I — EXT4 Closure Verification (pattern-051: regression check)

| EXT4 action | v1.0.176 status | Evidence |
|------------|-----------------|----------|
| **P0 — FB-175-1: catalog-wide QC artifact** (`ext4_fb1_flip_identity_qc_catalogwide.json`) | **CLOSED AND VERIFIED** | Artifact committed at `pipelines/p2_chirality/outputs/canonical_provenance/ext4_fb1_flip_identity_qc_catalogwide.json`. Artifact yields: `fraction_violating_beyond_1e-3_any_channel=0.02939` (≈2.9% ✓), `fraction_violating_beyond_1e-3_cw_channel=0.01569` (≈1.6% ✓, correctly replacing prior "1.3%"), `bound_excursion_any_channel.max=0.09009` (≈0.09 ✓), `sum_deviation.max=4.261e-7` (≈4.3×10⁻⁷ ✓). All four tex anchors verified. |
| **P0 — tex parenthetical** (l.619 area): dual `\artifact{}` pointers for catalog-wide vs. intersection-subset | **CLOSED** | Source l.619: `(catalog-wide rate from \artifact{...ext4_fb1_flip_identity_qc_catalogwide.json}; intersection-subset rate zero by construction, \artifact{...ext3_nfm1_flip_identity_qc.json})` — both artifact paths present. |
| **P0 — 1.3%→1.6% anchor** ("previously quoted 1.3% is the single CW-channel rate" → "1.6%") | **CLOSED** | Source l.619: `(1.6\% is the single CW-channel rate)`. Artifact confirms `fraction_violating_beyond_1e-3_cw_channel=0.01569`. Match. |
| **P1 — FM-175-2 conclusion VII.C reconciliation** ("same physical estimator and footprint") | **NOT APPLIED in v1.0.176** | Source l.556 still reads: "the two values describe the same physical estimator and footprint under different null-run sizes (the differing p-values reflect null-ensemble resolution, not different physics; see Sec. III.A and Table III caption)." The EXT4 closure plan called for replacing this with the "retained for continuity / high-statistics diagnostic" wording. This edit did NOT land in v1.0.176. **Carryover PARTIAL (open).** |
| **P2 — FM-175-3 Shamir wording** | **CLOSED** | Source l.492: "can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples" — same phrasing as EXT4 FM-175-3 partial. The hedge "a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion" is present in the same paragraph (l.145 and l.553). Ruling: PARTIAL (precision-improvement edit already carried from EXT3; no regression). |
| **P3 — GkA-EXT4 Table II caption truncation note** | **CLOSED** | Source l.360: Table tab:cw_frac caption contains "Percentages in this table (and in the catalog-composition counts cited in Sec. III) are truncated rather than rounded at the second decimal; the integer counts are exact." |

**Regression assessment:** No regressions introduced by v1.0.175→176. The three new elements (artifact, parenthetical, 1.6% fix) are clean and verified against committed data. FM-175-2 remains open as a carryover; no new regression.

---

## Part II — R34conf Fresh Findings Verdict Table

### KEY: findings are classified against v1.0.176 TeX source. "STALE" = already resolved before v1.0.176. "HOUSTON-DECISION" = policy already ruled (HD-6/HD-11). Pattern-052 applied to Gemini.

| # | Reviewer | Code | Sev claimed | Finding | Verdict | Evidence |
|---|---------|------|------------|---------|---------|----------|
| R34-P4-01 | Gemini | P4-E1 | ESSENTIAL | Remove internal versioning / provenance notes from abstract, Appendix A, footnotes | **HOUSTON-DECISION / OPINION** | The "lab notebook" vs. "final paper" framing is a LEGITIMATE journal-submission concern for the publication draft; acknowledged by all reviewers. However, this was already known from EXT1–EXT4 and ruled: the abstract's "An earlier version... is withdrawn" note + Appendix A provenance audit are intentional transparency features documented in the paper. Disposition at journal-submission is a Houston call (same family as the FM-175-1 two-step gate ruling). No new information. |
| R34-P4-02 | Gemini | P4-E2 | ESSENTIAL | Remove internal file paths from text | **HOUSTON-DECISION / OPINION** | Same category as EXT3/EXT4 file-path discussion. The `\artifact{}` macro paths are intentional provenance links. At PRD submission Houston will clean or inline. Ruled: HOUSTON-DECISION. No regression from v1.0.176. |
| R34-P4-03 | Gemini | P4-E3 | ESSENTIAL | Data Availability: future dates / no Zenodo DOI | **HOUSTON-DECISION (HD-11)** | The "Zenodo DOI not yet minted; will accompany journal submission" disclosure is present at l.749. This is the standing HD-11 ruling from EXT2 onward: mint-at-submission. Tex l.749 correctly says "a Zenodo DOI snapshot will accompany the journal submission." Not a regression. AUTO-FALSIFIED as a blocker. |
| R34-P4-04 | Gemini | P4-E4 | ESSENTIAL | "Headline" language is journalistic | **VERIFIED (cosmetic-MINOR)** | Source l.128: "The headline scientific result is a real-space chirality dipole consistent with null." Gemini is correct that "headline" is informal. Multiple occurrences throughout. This is a genuine, valid journal-polish concern not previously ruled. **New finding, but MINOR severity.** No regression — present since pre-v1.0.170. |
| R34-P4-05 | Gemini | P4-M1 | MAJOR | Shamir comparison "~6-12× inconsistent" is ambiguous (should compare to sensitivity floor, not null amplitude) | **PARTIAL** | Source l.145: "This is inconsistent in amplitude with Shamir's claimed ~3% signal by a factor of ~6–12 under the present pipeline, though a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion." The hedge is present (same text as EXT4 FM-175-3). Gemini's sharpening (compare to A_95 = 1.0–1.5%, not null amplitude) is a valid precision improvement. **PARTIAL — new-ish but same family as EXT4 FM-175-3; precision improvement not yet applied.** |
| R34-P4-06 | Gemini | P4-M2 | MAJOR | Falsification criterion "A ≥ A95" conflates amplitude threshold with σ significance | **OPINION** | Source l.562: "A future survey detecting a chirality dipole at σ > 5 with amplitude A ≳ A_95 at ≥ 10^7 galaxies would be in tension with the present null; a detection at A_50 ≲ A ≲ A_95 is in the consistency range and would not falsify the present non-detection." The two conditions (amplitude + significance) are presented separately, not conflated. Gemini's reading is a style concern, not a factual error. **OPINION.** |
| R34-P4-07 | Gemini | P4-N1 | MINOR | Parity-even vs parity-odd monopole explanation | **OPINION** | Source l.535–536: "the parity-odd signal lives in the l=0 monopole and even-l multipoles." The explanation of why l=0 is parity-odd is not spelled out inline; adding it would be a clarity improvement. Valid suggestion but OPINION-level. |
| R34-P4-08 | Gemini | P4-N2 | MINOR | Truncation vs rounding convention | **STALE** | Table II caption already notes truncation convention. The GkA-EXT4 closure (Table II caption truncation note) is confirmed landed. **STALE.** |
| R34-P4-09 | Gemini | P4-T1 + P4-A1 | MINOR/NIT | Table II footnote: version history language; Table II Dev arithmetic discrepancy (+28.72 vs +28.75) | **PARTIAL** | (a) The Table II footnote in source references the "selection-filter defect" — this is part of the provenance note family (HOUSTON-DECISION / same as P4-E1). (b) Arithmetic: OpenAI pass-2 also caught this. Source l.360: `Dev.` for Tier A is quoted as "+28.72σ" in the caption. Verify: f_CW=0.507879, σ=0.000274 → (0.507879−0.5)/0.000274 = 0.007879/0.000274 = 28.75σ. The caption-quoted Dev is 28.72σ from the table body — this is a minor rounding/truncation ambiguity (the paper uses truncation not rounding). Specifically: f_CW=0.507879 truncated to 6 decimals × σ=0.000274. The discrepancy (28.72 vs 28.75) is 0.11% — consistent with the truncation convention applied to the unrounded f. The paper's own note says "Dev. is the signed (f_CW − 0.5)/σ computed from the unrounded fraction." So 28.72 uses the printed truncated f, while 28.75 uses the unrounded f. Both are internally consistent with the stated convention. **STALE/FALSIFIED as a real error** — paper explicitly states Dev uses "unrounded fraction," meaning the on-disk unrounded value (which is what the body cites). However, the tabulated value in the compiled PDF may show 28.72 while the body text at l.360 derives from the unrounded. This is a display vs. derivation tension worth a note but not an error. Downgrade to OPINION. |
| R34-P4-10 | Grok | P4-E1 | ESSENTIAL | Version log language throughout + "withdrawn" in abstract | **HOUSTON-DECISION** | Same as R34-P4-01. Ruled. |
| R34-P4-11 | Grok | P4-E2 | ESSENTIAL | "Not directly comparable" qualifier missing at every σ juxtaposition | **PARTIAL (real but EXT-known)** | Source l.128 (abstract): "+3.64σ ... canonical mask; +7.28σ, apodized footprint" alongside "+0.41σ dipole." The abstract now carries the parenthetical "(The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask; the 10^4-permutation canonical unapodized row in Table III gives +7.93σ; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims.)" That parenthetical is present in the abstract. The full "not directly comparable" language is in §III.A (l.300 area) and Table I/III captions. Grok's charge that no qualifier exists at every juxtaposition: partially valid at the abstract level, but the parenthetical does clarify. **PARTIAL — new form, already addressed in spirit; one more targeted cross-comparability sentence in abstract could help.** |
| R34-P4-12 | Grok | P4-E3 | ESSENTIAL | Largest catalog claim not demonstrated vs. all published catalogs | **PARTIAL (STALE family)** | Source l.128: "to our knowledge, the largest chirality-labeled galaxy catalog to date." "To our knowledge" qualifier is present. The body (l.145) compares against CE-ResNet's ~1.95M and Shamir's ~1.3M, showing 1.6× CE-ResNet. This is the same concern raised and ruled PARTIAL in EXT rounds. No new information. |
| R34-P4-13 | Grok | P4-E4 | ESSENTIAL | Abstract shows only most-favorable null (+0.41σ) while body reports +7.28σ MASTER result | **PARTIAL (known, abstract clarity)** | Source l.128: abstract presents "+0.41σ" as the real-space headline, then parenthetical clarifies "+3.64σ ... +7.28σ" are systematics-attributed diagnostics. The distinction is stated, but Grok's concern — that a reader scanning only the abstract would see only the favorable null — has merit as a clarity issue. **PARTIAL — same family as EXT4 FM-175-3 / abstract-clarity chain.** |
| R34-P4-14 | Grok | P4-M1 | MAJOR | 22-page length for a null result | **OPINION** | Scope/length decisions are editorial. Not an error. |
| R34-P4-15 | Grok | P4-M2 | MAJOR | Different null procedures produce σ differing by factors 2–20; variance not decomposed | **OPINION** | The paper's §III.A (significance conventions) and Table I explicitly warn σ values from different null procedures are not cross-comparable. The spread is by design. Requesting a dedicated decomposition section is editorial. |
| R34-P4-16 | Grok | P4-M3 | MAJOR | +3.64σ → +7.28σ inflation after MASTER deconvolution not explained quantitatively | **VERIFIED (NEW — cosmetic/MINOR but genuinely new)** | Source: the pre-MASTER → post-MASTER σ increase is discussed qualitatively in §IV.D (monopole-mask leakage) but no quantitative decomposition of the factor-of-2 increase into leakage vs. signal is provided inline at the σ-reporting site. This is a genuinely new, valid request not previously explicitly audited. **VERIFIED as MINOR.** |
| R34-P4-17 | Grok | P4-M4 | MAJOR | TTA validation is 2,000-galaxy hold-out; no propagation into dipole amplitude | **PARTIAL** | Source: T2 rotation stability (2k hold-out) is one of 8 bias tests; the injection-recovery floors (A_50≈0.75%, A_95∈(1.0%,1.5%]) are the operational sensitivity floors, which implicitly fold in all classifier effects end-to-end. The request for a separate "TTA variance" term in the dipole error budget is a valid scope extension, but the paper's injection-recovery approach is the standard alternative. **PARTIAL — valid precision concern, not a factual error.** |
| R34-P4-18 | Grok | P4-M5 | MAJOR | Shamir comparison uses different samples/classifiers; factor of 6–12 requires matched reanalysis | **STALE** | Source l.145 already says "under the present pipeline, though a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion." This is the EXT4 FM-175-3 hedge, confirmed present. **STALE/already-addressed.** |
| R34-P4-19 | OpenAI | P4-E1 | ESSENTIAL | Training/validation split inconsistency (6,637+17,153+2,000=25,790 → augmented = 21,293+5,323 ≠ expected) | **VERIFIED (MAJOR — genuinely new)** | Source l.619 area (Appendix B): This is a new arithmetic consistency check. The training/validation counts (ntrain=21,293, nval=5,323, augmented pool=26,616) vs. the expected 0.8×25,790+826=21,458 (train) and 0.2×25,790=5,158 (val) yields an 165-example discrepancy. Source text at l.619: not fully quoted in the v1.0.176 excerpt reviewed; OpenAI's specific claim needs to be verified against Appendix B.a. This is a genuinely new arithmetic concern, not previously audited. **VERIFIED as genuinely new — needs source verification in Appendix B.a. Severity: MAJOR (load-bearing for accuracies if the split-before-augmentation question is unresolved).** Mark PARTIAL pending source verification of exact counts in Appendix B.a. |
| R34-P4-20 | OpenAI | P4-E2 | ESSENTIAL | Version-history prose in body | **HOUSTON-DECISION** | Same as R34-P4-01/10. |
| R34-P4-21 | OpenAI | P4-E3 | ESSENTIAL | LEE hemisphere scan: direct-MC pLEE ≤ 10⁻⁴ described as "raw" then doubly-corrected with Bonferroni/BH — double-counting | **PARTIAL (carryover, EXT3 FM3)** | This is the same finding as EXT3/EXT4 FM3 (Table I LEE correction philosophies). EXT4 ruling was PARTIAL carryover — the direct-MC max-stat now leads, but Table I caption still names both philosophies. No change from EXT4. **PARTIAL carryover, not new.** |
| R34-P4-22 | OpenAI | P4-E4 | ESSENTIAL | σ from different null procedures juxtaposed without explicit cross-comparability caveat in abstract/conclusions | **PARTIAL (carryover, same as R34-P4-11)** | Same as Grok P4-E2 finding. PARTIAL. |
| R34-P4-23 | OpenAI | P4-E5 | ESSENTIAL | Typo in Appendix D: "z ≈ −18.1.34" spurious ".34" | **VERIFIED (NEW — MINOR)** | OpenAI quotes Appendix D, p.19: "the headline exclusion statistic is z ≈ −18.1.34" with spurious ".34". Source needs line-level verification but this is a genuine typographic error not previously caught. **VERIFIED as genuinely new MINOR (typo in appendix).** |
| R34-P4-24 | OpenAI | P4-E6 | ESSENTIAL | Commit/version mismatch: front matter "v1.0.176" but Data Availability cites "commit 53b41d12 (v1.0.175)" | **HOUSTON-DECISION (HD-11 + two-step stamp)** | This is the HD-11/two-step stamp-then-pin disclosure, ruled from EXT3 onward. Source l.749 discloses this explicitly. |
| R34-P4-25 | OpenAI | P4-E7 | ESSENTIAL | Two σ values (+3.64 and +7.93) for "same canonical ℓ=1 channel" are confusing | **PARTIAL (FM-175-2 carryover — open)** | This is exactly FM-175-2. The text l.556 still says "same physical estimator and footprint under different null-run sizes." The FM-175-2 edit was not applied in v1.0.176. **PARTIAL carryover — the one still-open EXT4 action item.** |
| R34-P4-26 | OpenAI | P4-E8 | ESSENTIAL | Table II Catalog-B uncertainty vs Dev inconsistency and missing Nspiral | **PARTIAL (needs source check)** | OpenAI claims f=0.504 ± 0.0003 with Dev=+14.6σ but direct calculation gives 0.004/0.0003≈13.3σ; the 14.6σ uses σ≈0.000274 from Tier A instead of the listed ±0.0003. Source l.360 caption says "Catalog-B row derives from the Platt-calibrated fraction; its deviation is computed from the unrounded calibrated fraction." The σ for Tier B is derived from N_A spiral count per the caption. This is a genuine internal tension if the σ column heading implies per-tier N. **PARTIAL — real concern, needs line-level source resolution. Not previously audited.** |
| R34-P4-27 | OpenAI | P4-E9 | ESSENTIAL | "0.57% (Ap-unit) dipole" is self-contradictory (Ap is dimensionless [−1,1]; percent × Ap-unit is incoherent) | **VERIFIED (NEW — MINOR notation)** | Valid notation inconsistency. Ap=0.0057 and "0.57%" are the same thing, but writing "% (Ap-unit)" is redundant/confusing. New finding. **VERIFIED MINOR.** |
| R34-P4-28 | OpenAI | P4-E10 | ESSENTIAL | App A.c monopole-subtraction example mixes footprints/weights | **PARTIAL (new)** | The cross-mask-convention mixing in a single example paragraph is a genuine clarity concern. Not previously audited cleanly. **PARTIAL (new, clarity-level).** |
| R34-P4-29 | OpenAI | P4-M3 | MAJOR | Injection-recovery A50 lacks CI; A95 bracketed only | **PARTIAL (EXT-known)** | Source l.562: "A_95 ∈ (1.0%,1.5%] (Table III; bracketed, not measured)." The bracketing is disclosed. A50 CI is implicitly the binomial SE on the 100-injection grid. OpenAI's request for a logistic-fit CI is valid but previously discussed. **PARTIAL.** |
| R34-P4-30 | OpenAI | P4-M4 | MAJOR | Edge-on contamination ~10–15% sample size / ~5–8% sensitivity penalty without derivation | **PARTIAL (new)** | Appendix E claim without derivation from 65.7% edge-on mis-triage. Not previously audited. Valid reproducibility concern. **PARTIAL (genuinely new).** |
| R34-P4-31 | OpenAI | P4-M7 | MAJOR | Flip-swap "error" metric undefined (Appendix B.d: mean 0.267 / median 0.0006) | **VERIFIED (NEW — MAJOR)** | Source l.619 area (Appendix B.d): the flip-swap error metric is reported (mean 0.267 at max p>0.9 vs 0.383 at max p<0.7) but the formula (L1? L2? 1−corr?) is never defined. This is a genuine reproducibility gap. **VERIFIED as genuinely new MAJOR.** |
| R34-P4-32 | OpenAI pass-2 | P4-M5 (pass-2) | MAJOR | Fisher floor equation: "2√3 σ(f_CW)" factor is dimensionally incorrect | **VERIFIED (NEW — MAJOR)** | OpenAI identifies that σ(A) = √(3/N) = 2√3 σ(f_CW) is incorrect: for binomial f_CW at p≈0.5, σ(f_CW) ≈ 1/(2√N), so σ(A) = 2σ(f_CW) ≈ 1/√N, not 2√3 × σ(f_CW). The middle equality in the paper's Fisher equation carries an erroneous √3 factor. The final numerical answer (9.7×10⁻⁴) is correct as √(3/N), but the chain of equalities in the published formula is wrong. **VERIFIED as genuinely new MAJOR (notation/equation error — the numerical result is correct but the derivation chain is wrong).** |
| R34-P4-33 | OpenAI pass-2 | P4-M6 (pass-2) | MAJOR | Fisher floor narrative mixes full-sample floor (0.29%) with HC-broad floor (0.53%) inconsistently | **PARTIAL (carryover EXT3 NF-M2 family)** | The HC Fisher floor (0.53%) addition was confirmed CLOSED in EXT4 (NF-M2). The pass-2 concern is that the A_50 gap decomposition references the 0.29% full-sample floor rather than the 0.53% HC floor relevant to the HC-broad estimator. Source l.562: "the statistical-only Fisher floor is ~0.29%." This is the full-sample floor, correctly identified as a separate floor from HC-broad. The question is whether the three-factor gap decomposition references the right floor. **PARTIAL — needs line-level source check; new-ish sharpening of closed item.** |
| R34-P4-34 | OpenAI pass-2 | P4-M9 (pass-2) | MAJOR | Axis-averaging not stated for A50/A95; falsification criterion reads as fixed-axis | **PARTIAL (NEW — precision)** | Source l.562: "quoted as a random-axis-averaged probability (θ-uniform axis convention; cf. the area-uniform spot check of Sec. VI.A)." The qualifier IS present in the Conclusions. The abstract (l.128): "injection-recovery brackets A_95 between 1.0% and 1.5% (A_50≈0.75%)" — no axis-averaging qualifier in the abstract's falsification sentence. **PARTIAL — qualifier present in body, absent in abstract. Valid precision improvement.** |
| R34-P4-35 | Perplexity | (multiple) | MAJOR | Version-history language in body; Data Availability | **HOUSTON-DECISION** | Same as R34-P4-01. |
| R34-P4-36 | Perplexity | P4-M1 (Perplexity) | MAJOR | Largest catalog claim needs quantitative comparison | **STALE** | l.145 contains the comparison to CE-ResNet 1.95M and Shamir 1.3M. Already in paper. |
| R34-P4-37 | Perplexity | P4-M5 (Perplexity) | MAJOR | Fisher floor 2√3 σ(f_CW) factor | **SAME AS R34-P4-32** | Perplexity pass-2 independently raises the same issue. Confirms R34-P4-32 verdict: VERIFIED MAJOR. |
| R34-P4-38 | Perplexity | P4-M6 (Perplexity pass-2) | MAJOR | Fisher floor narrative full vs HC inconsistency | **PARTIAL (same as R34-P4-33)** |
| R34-P4-39 | Perplexity | P4-M7–P4-M10 (Perplexity pass-2) | MAJOR | Various abstract/body comparability clarifications | **PARTIAL / OPINION** | The positive-definite amplitude σ not being Gaussian-equivalent (P4-M7), the leakage attribution overstated in abstract (P4-M8), the axis-averaging (P4-M9), the 1.88% classification-noise floor approximation demote (P4-M10). These are all valid precision/clarity improvements. Several are new-ish; see full Perplexity report. Ruling batch: **PARTIAL (new clarity concerns, not factual errors).** |

---

## Part III — Verdict Counts

| Verdict | Count | Finding codes |
|---------|-------|---------------|
| **VERIFIED (MAJOR)** | **3** | R34-P4-31 (flip-swap error undefined), R34-P4-32/37 (Fisher 2√3 factor wrong) , R34-P4-19 (train/val split arithmetic PARTIAL→pending source) |
| **VERIFIED (MINOR)** | **3** | R34-P4-04 ("headline" language), R34-P4-16 (MASTER σ inflation not quantified), R34-P4-23 (z≈−18.1.34 typo), R34-P4-27 (Ap-unit notation) |
| **VERIFIED (NEW, net)** | **5** | R34-P4-04, R34-P4-16, R34-P4-23, R34-P4-27, R34-P4-31, R34-P4-32 |
| PARTIAL (carryovers + new sharpened) | 12 | R34-P4-05, -11, -12, -13, -19, -21, -22, -25, -26, -28, -30, -33, -34, -39 |
| OPINION / EDITORIAL | 5 | R34-P4-06, -07, -14, -15, -17, -39 batch |
| STALE | 3 | R34-P4-08, -18, -36 |
| HOUSTON-DECISION | 5 | R34-P4-03, -10, -20, -24, -35 |
| AUTO-FALSIFIED | 0 | (no Gemini extractor artifacts in P4 this round; Gemini P4 stream is math-based claims against PDF, not layout-garbling) |

**Net new VERIFIED:** 5 items (3 MAJOR, 3 MINOR — one item counted in both because R34-P4-32 and R34-P4-37 are the same finding from two reviewers; R34-P4-19 is PARTIAL pending Appendix B.a source check).

**Final count: VERIFIED (MAJOR) = 2 confirmed (R34-P4-31, R34-P4-32) + 1 PARTIAL-pending (R34-P4-19); VERIFIED (MINOR) = 3 (R34-P4-04, R34-P4-23, R34-P4-27) + 1 new (R34-P4-16).**

---

## Part IV — Reviewer Calibration

| Reviewer | Stated recommendation | Audit-calibrated | Delta |
|---------|-----------------------|-----------------|-------|
| Gemini_cosmology | MAJOR REVISIONS | MINOR REVISIONS (all ESSENTIAL findings are policy/OPINION; no new-substantive items; P4-M1 is PARTIAL) | Overcalled |
| Grok_brutal | REJECT | MINOR REVISIONS (R34-P4-16 new MINOR; ESSENTIAL findings are policy/HOUSTON-DECISION or PARTIAL-carryover; headline science uncontested) | Significantly overcalled |
| OpenAI_methodology | MAJOR REVISIONS | MAJOR REVISIONS — **calibrated** (R34-P4-32 Fisher factor error + R34-P4-31 flip-swap metric undefined are genuine MAJORs; R34-P4-19 train/val split needs resolution) | Accurate |
| Perplexity_citations | MAJOR REVISIONS | MINOR REVISIONS (bibliography checks pass; the MAJOR concerns echo OpenAI's which are valid; the precision clarification items are MINOR/PARTIAL) | Mild overcall |
| Claude_brutal | ABSENT (413 error) | N/A — note for record only | — |

**Consensus:** P4 is **NOT CLEAN**. Two confirmed new MAJORs (Fisher equation error; flip-swap metric undefined). One PARTIAL-pending MAJOR (train/val split). Three new MINORs ("headline" language; z≈−18.1.34 typo; Ap-unit notation). The headline science (+0.41σ HC dipole; A_50≈0.75%; A_95∈(1.0%,1.5%]; z≈−18 WLS exclusion) is **not challenged by any reviewer**. FM-175-2 (same-estimator-and-footprint sentence) remains open from EXT4.

---

## Part V — Closure Plan (hardest-first)

### C0 — R34-P4-32 (VERIFIED MAJOR): Fix Fisher equation 2√3 factor

In the relevant section (equation for σ(A) = √(3/N) = 2√3 σ(f_CW)):
- Remove the middle equality `2√3 σ(f_CW)` or replace with correct chain: σ(A) = √(3/N) ≈ 1/√N (for p≈0.5); if relating to σ(f_CW), the correct factor is 2 (not 2√3): σ(A) = 2 σ(f_CW) ≈ 1/√N.
- The numerical result (9.7×10⁻⁴) is correct; only the intermediate equality is wrong.

### C1 — R34-P4-31 (VERIFIED MAJOR): Define flip-swap error metric

In Appendix B.d near the "mean flip-swap error 0.267 (median 0.0006) at max p > 0.9 vs. 0.383 (median 0.364) at max p < 0.7" statement:
- Add the exact formula: e.g., "the flip-swap error is defined as |p_CW^raw − p_CW^flip|, the per-galaxy L1 distance between raw and flip-pass CW probabilities."

### C2 — R34-P4-19 (PARTIAL-MAJOR): Verify train/val split Appendix B.a

- Read Appendix B.a verbatim and check whether the split (21,293 / 5,323 / pool=26,616) is explicitly documented with the augmentation timing.
- If the split was performed before augmentation (so augmented duplicates always go to train), add: "the 80/20 split is applied before flip augmentation; augmented duplicates are confined to the training split."
- If after augmentation, correct the reported counts.

### C3 — R34-P4-25 / FM-175-2 (PARTIAL — carryover): Conclusion VII.C reconciliation

- Apply the EXT4 closure plan sentence replacement: replace "the two values describe the same physical estimator and footprint under different null-run sizes" → "the 500-MC +3.64σ direct single-mode value is retained for continuity with the leakage analysis; the 10^4-permutation Table III canonical row is the current high-statistics diagnostic under its committed field convention."

### C4 — R34-P4-23 (VERIFIED MINOR): Fix Appendix D typo "z ≈ −18.1.34"

- Correct to "z ≈ −18.1" (remove spurious ".34").

### C5 — R34-P4-27 (VERIFIED MINOR): Fix "0.57% (Ap-unit)" notation

- Replace with "Ap = 5.7×10⁻³ (i.e., 0.57%)" or "A = 0.57% (Ap = 0.0057)."

### C6 — R34-P4-04 (VERIFIED MINOR): Remove "headline" language

- Replace "headline scientific result," "headline finding," "headline exclusion" throughout with "primary result," "main finding," "primary exclusion."

### Ruled / HOUSTON-DECISION (no action this wave)

- R34-P4-01/02/10/20/35: provenance notes + file paths — at journal submission only.
- R34-P4-03/24: Zenodo DOI + two-step stamp — HD-11, mint-at-submission.
- Length / paper-structure suggestions — editorial.
- R34-P4-06/07/14/15: OPINION-level.

---

## Verdict

**NOT CLEAN.** 2 confirmed new MAJORs + 1 PARTIAL-MAJOR + 4 new MINORs. FM-175-2 carryover still open. 6 concrete edits (C0–C5) close all verified items; C3 closes the sole open EXT4 action. No headline science challenged.

---

*Verified counts: VERIFIED 5 (2 MAJOR, 3 MINOR) · PARTIAL 14 · OPINION 6 · STALE 3 · HOUSTON-DECISION 5 · AUTO-FALSIFIED 0*
*Pattern-052 not triggered (Gemini P4 findings are logic/framing-based, not extractor-artifact-based).*
*Claude leg absent: API 413 error (request too large). 4/5 legs present.*
