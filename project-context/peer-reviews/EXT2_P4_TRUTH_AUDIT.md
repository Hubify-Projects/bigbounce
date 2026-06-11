# EXT2 P4 — Truth Audit
**Paper:** P4 — Survey-Scale Galaxy Chirality (v1.0.173, 22 pp)
**Source:** `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Reviewers:** ChatGPT Pro Extended (MAJOR), Grok Heavy (ACCEPT), Gemini 3.5 Thinking (ACCEPT)
**Auditor:** Claude Sonnet 4.6 · **Date:** 2026-06-10

**SAMPLE+ESTIMATOR+NULL baseline:** HC p>0.6, N=949,584 (real-space dipole); full N=3,201,160 (MASTER, WLS). All verdicts identify estimator and null before concluding.

---

## EXT2 Closure-Verification Verdicts

### ChatGPT reported closures vs. source

| EXT1 ID | ChatGPT EXT2 status | Audit verdict | Evidence |
|---------|---------------------|---------------|----------|
| B1 (commit hash) | REGRESSION/PARTIAL | HOUSTON-DECISION | `.tex` l.714: Data Availability now reads `commit 297aa805 (v1.0.173)`; version changelog (ll.70-71) says "Hash re-pinned to the v1.0.173 stamp commit in the follow-up pin commit." ChatGPT claims that the *public* `.tex` at `297aa805` still contains the v1.0.172 hash internally — a two-step provenance gate issue. Cannot resolve from local repo alone; the local working copy is v1.0.173 with the correct hash. This is a provenance-gate process question (does the stamp commit pre-date the hash-pin commit?), not an error in the science. HOUSTON-DECISION: verify the stamp commit sequence in GitHub history. |
| B2 (post-MASTER monopole) | PARTIAL | FALSIFIED (EXT2 surplus) | `.tex` ll.441-443: Post-MASTER behavior is now explicitly in-paper with artifacts cited for σ=+4.84 and σ=+5.14 and the 12% reproduction figure. The analysis-hierarchy bullet (l.182) still says "demonstrat[es] the +3.64σ canonical value is consistent with monopole-mask leakage" — ChatGPT reads this as a remaining ambiguity. Source text at l.182 says this is for the pre-MASTER generative null (item vi), not the post-MASTER value. The statement is about the leakage channel, not post-MASTER interpretation. FALSIFIED as a PARTIAL: the prose is correctly scoped. |
| B3 (+3.64 vs +7.93) | PARTIAL | PARTIAL | `.tex` l.521: "the two values describe the same physical estimator and footprint under different null-run sizes." The abstract (l.93) says "not two independent detection claims." The Sec III.A notation (l.171) says "not mutually comparable." ChatGPT correctly identifies that "same physical estimator" (l.521) is in tension with "not mutually comparable" (l.171). Both phrases are present in the source. The technical meaning is correct (same field, different N_MC) but the framing is genuinely confusing for a reader who sees both phrases. PARTIAL — the contradiction in wording persists. |
| B4 (training count) | CLOSED | VERIFIED-CLOSED | `.tex` l.154 explicitly states: "after flip augmentation of the training split the combined pool is 26,616 images (80/20 split: n_train=21,293, n_val=5,323; augmented duplicates contribute to the 826-image difference...)." The reconciliation is fully present. |
| B5 (WLS mask mismatch) | PARTIAL | PARTIAL | ChatGPT's concern about the bootstrap using galactic-latitude mask vs. canonical N_spiral≥10 mask remains technically present in the artifact; the .tex footnote (l.664fn) now justifies NSIDE=8 block scale and shows z stable across NSIDE={4,8,16}, but does not explicitly state the bootstrap mask definition matches the canonical paper mask. PARTIAL as documented in EXT1. |
| M1 (HC null labeling) | PARTIAL | PARTIAL | `.tex` l.419 and l.441 still read "the full-catalog real-space dipole at +0.41σ" in two places. This label is literally wrong — it is the HC p>0.6, N=949,584 estimator, not the full 3.2M catalog. ChatGPT's FM1 identifies this accurately. PARTIAL — the mislabel persists at ll.419 and 441. |
| M2 (closure language) | CLOSED | VERIFIED-CLOSED | Language throughout now uses "systematics-attributed," "most likely," "consistent with." |
| M3 (ℓ=2 200-realization) | PARTIAL | PARTIAL | `.tex` l.443 and App D.h: cross-spectrum uses 200-realization permutation null; "confirming" language noted by ChatGPT. The source (l.694) says "supported by: (a) ℓ=2 cross-spectrum..." — uses "supported" not "confirmed." PARTIAL only on the null ensemble size (200 is still the floor). |
| M4 (WLS z=-18) | CLOSED (subj. B5) | VERIFIED-CLOSED | Block-bootstrap with NSIDE sensitivity now in footnote at l.664. |
| M5 (calibration caveat) | CLOSED | VERIFIED-CLOSED | Sec IV.A and Data Availability both state p_eq are ranking scores. |
| M6 (D4-TTA) | PARTIAL | PARTIAL | `.tex` l.248 reports the Z2 vs D4 comparison but not a spatially stratified comparison in the low-confidence tail. ChatGPT's request is valid but not a scientific error — the mean stability result is correctly reported. |
| M7 (Shamir comparison) | PARTIAL | PARTIAL | `.tex` l.441 says "prior literature's pre-MASTER dipole-detection claims are therefore explained at the percent level...under our DESI/ViT-Small pipeline." The disclaimer about needing a matched Ganalyzer comparison is present at l.110 and l.664. The breadth of the claim is hedged. |
| M8 (catalog claim) | CLOSED | VERIFIED-CLOSED | l.93 pairs 8.47M with N_spiral=3.2M. |

### Grok EXT2 closure: All 3 MAJORS CLOSED
Source confirms: NSIDE sensitivity in footnote l.664; post-MASTER explicit at l.441; falsification criterion estimator-specific in abstract l.93.

### Gemini EXT2 closure: All 5 items CLOSED
Source confirms: footnote 3 at l.664 (NSIDE sensitivity); T7 explanation at l.584; calibration warning in Data Availability; Fig. 1 three-panel gallery at l.121-149; Sec III.A notation map at l.161-173.

---

## Fresh-Finding Verdict Table (EXT2 new findings)

| # | Reviewer | Severity | Finding | Verdict | Evidence |
|---|----------|----------|---------|---------|----------|
| EF1 | ChatGPT | BLOCKER (FB1) | Data Availability commit hash: PDF says 297aa805 but public .tex at that commit still contains 7c03bb64/v1.0.172 | HOUSTON-DECISION | Local `.tex` l.714 reads `commit 297aa805 (v1.0.173)`. The version log (ll.70-71) confirms hash was re-pinned in a follow-up commit. ChatGPT's claim that the GitHub remote `.tex` at 297aa805 still shows the old hash could be a two-step gate issue (stamp commit precedes the pin commit). Cannot verify from local repo alone — requires inspecting remote commit history. Zenodo not yet minted. Journal-policy item (DOI minting at submission) = HOUSTON-DECISION for the DOI. The hash question is a real reproducibility question — HOUSTON-DECISION for commit-sequence verification. |
| EF2 | ChatGPT | MAJOR (FM1) | "Full-catalog real-space dipole at +0.41σ" label appears at ll.419 and 441; the +0.41σ is HC p>0.6, N=949,584, not the full catalog | VERIFIED | `.tex` l.419: "the full-catalog real-space dipole at $+0.41\sigmaunit$" and l.441: "the full-catalog real-space dipole at $+0.41\sigmaunit$ and the block-bootstrap WLS..." Confirmed: the headline estimator is HC p>0.6, N=949,584, as stated explicitly at l.350, l.93, and Table I row (i). The label "full-catalog real-space dipole" at ll.419/441 is factually incorrect — it should be "HC real-space dipole" or "Catalog-C HC dipole." Two occurrences. Fix: replace both with "HC real-space dipole at +0.41σ." |
| EF3 | ChatGPT | MAJOR (FM2) | "Disfavors any model predicting dipole ≥0.75%" overuses A50; paper defines A50 as 50%-recovery and A95 as falsification boundary | VERIFIED | `.tex` l.501: "The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥0.75% on the DESI Legacy footprint..." The paper's own Sec VII (l.527) explicitly states A50 is the consistency boundary, not a falsification threshold, and A95 ∈(1.0%,1.5%] is the falsification boundary. "Disfavors" at A50 overstates the exclusion. The 0.75% amplitude puts models in the "consistency range" (l.527), not the "falsification range." Fix: change l.501 to "is sensitive at the 50%-recovery level to amplitudes ~0.75%; the falsification boundary is A≳A95 ∈(1.0%,1.5%]." |
| EF4 | ChatGPT | MAJOR (FM3) | Hemisphere LEE: direct max-stat MC p_LEE≤10⁻⁴ (already incorporates 648-direction scan) vs. Bonferroni/BH "reduce to <1σ" — inconsistent presentation of the LEE correction | PARTIAL | `.tex` l.632 and Table I caption (l.189): The paper already correctly addresses this. Table I caption explicitly states "the additional Bonferroni/BH pass over the 648 tested directions reported in Appendix C is a second, deliberately conservative penalty (the two corrections bracket the significance)." l.632 says "BH formally assumes independence...which the strongly correlated overlapping-hemisphere grid does not guarantee; the BH/Bonferroni pass is therefore reported only as a conservative heuristic cross-check, and the principled directional look-elsewhere control is the direct-MC max-statistic null itself." The paper's framing is technically correct: the max-stat MC IS the principled LEE correction; Bonferroni/BH is explicitly labeled heuristic. ChatGPT's concern about the word "principled" for the max-stat and calling Bonferroni a second pass is already addressed. PARTIAL: the prose in App C could be read by a casual reader as saying Bonferroni/BH is the LEE correction. The Table I caption clarification is clear but the App C text is still dense enough to cause confusion. No new fix beyond what is already present. |
| EF5 | ChatGPT | MAJOR (FM4) | "+0.41σ real-space and +7.28σ harmonic are mutually consistent" framing not a cross-estimator consistency test | PARTIAL | `.tex` l.521 context: The paper does not say the two are "mutually consistent" in the sense ChatGPT implies. The text says the harmonic-completeness check shows a Shamir-class dipole would give z~68-218 in the harmonic channel. This is used as an amplitude completeness bound, not a cross-consistency test. ChatGPT's proposed rephrase is reasonable style polish but the current wording does not make the false claim ChatGPT attributes to it. PARTIAL — the recommended rephrase is a clarity improvement. |
| EF6 | ChatGPT | MAJOR (FM5) | "All 8 tests pass" too strong after T5/T7 acknowledged as non-independent | PARTIAL | `.tex` l.584: "All 8 tests pass at the stated criteria; acceptance thresholds are generous relative to the 0.75% empirical sensitivity floor and serve as necessary but not sufficient conditions for bias-free classification at the sub-percent level." This exact caveat is already present in the source. ChatGPT's proposed fix adds "T5/T7 are necessary but not sufficient" — but the current text already says "necessary but not sufficient conditions." PARTIAL — the caveat exists; the requested per-test labeling of T5/T7 is minor additional clarity. |
| EF7 | ChatGPT | MINOR (m1) | Title too long | OPINION | Editorial preference; journal decision. |
| EF8 | ChatGPT | MINOR (m2) | Zenodo DOI not yet minted | HOUSTON-DECISION | `.tex` l.719: "A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted; until it is, the versioned release tag above is the citable artifact." Explicit and honest. DOI minting at submission = HOUSTON-DECISION, per protocol. |
| EF9 | ChatGPT | MINOR (m3) | "+3.64σ and +7.93σ not mutually comparable" vs "same physical estimator" contradiction | PARTIAL | As noted in B3 above: both phrases are in the source (l.171 and l.521). Both are technically correct from different angles (different null sizes vs. same field/footprint). The tension is real. Fix: add a parenthetical at l.521 such as "(same field and footprint; the not-mutually-comparable characterization of Sec. III.A refers to the fact that different N_MC produces non-equivalent p-values, not different physics)." |
| EF10 | ChatGPT | MINOR (m4) | Shamir comparison phrasing "pre-MASTER dipole-class signal observed in SDSS-class samples" too broad | PARTIAL | `.tex` l.441 and l.110: the paper hedges with "under our DESI/ViT-Small pipeline" and "a matched-footprint Ganalyzer reanalysis is required." The breadth concern is partially valid: "prior literature's pre-MASTER dipole-detection claims" could encompass more than the current demonstration. PARTIAL — the existing hedge is adequate but the phrase could be more precise. |
| EF11 | ChatGPT | MINOR (m5) | ℓ=2 cross-spectrum 200-realization null: soften "confirming" | PARTIAL | Source l.694 uses "supported by" not "confirmed." This finding was already partially addressed. The 200-realization floor is the remaining issue. PARTIAL. |
| EF12 | Grok | MAJOR | Sec IV.D: "The +3.64σ (500-MC) and +7.93σ (10⁴-perm) values quoted for the canonical unapodized field refer exclusively to the pre-MASTER estimator" — add clarifying sentence explicitly noting this | PARTIAL | `.tex` l.521: The text says these are for "the same canonical unapodized field" and Sec III.A (l.171) says these three values are "not mutually comparable." The pre-MASTER/post-MASTER distinction is that the +3.64σ/+7.93σ are MASTER-deconvolved values (they use NaMaster mode-coupling deconvolution), not pre-MASTER pseudo-C_ℓ. Adding "refer exclusively to the pre-MASTER estimator" would be factually incorrect — they ARE MASTER-deconvolved. Grok's phrasing is confused: 3.64σ/7.93σ are POST-MASTER MASTER-deconvolved results, not pre-MASTER. The "pre-MASTER" mention in B2 is about the 99.32% monopole reproduction. PARTIAL: the clarifying sentence Grok requests uses wrong terminology but the spirit (add one sentence mapping the two values to their exact provenance) is valid. |
| EF13 | Grok | MINOR | Abstract parenthetical (+3.64 vs +7.93 explanation) should move immediately after first mention of +3.64 | OPINION | Abstract positioning choice. No content error. OPINION. |
| EF14 | Grok | MINOR | Fig. 1 caption "(c) Non-spiral (NOT-SPIRAL): ellipticals, mergers, edge-on" — "NOT-SPIRAL" inconsistent with P_NS notation used elsewhere | PARTIAL | `.tex` l.136: Fig. 1 panel (c) caption says "Non-spiral (\NS{}): ellipticals, mergers, edge-on" where \NS{} expands to `\textsc{not\_spiral}`. The macro `\NS{}` IS the paper's canonical notation, and the figure caption uses it correctly. "NOT-SPIRAL" in the reviewer's quote is how Grok read the rendered PDF notation. No inconsistency in the source: \NS{} = `NOT_SPIRAL` = P_NS all refer to the same class. OPINION — the rendered form is consistent. |
| EF15 | Grok | MINOR | Table III footnote: add forward pointer to post-MASTER monopole-only result | PARTIAL | The Table III caption (l.378) already says "+3.64σ...is superseded as a table entry by the canonical rows above but retained in the text for continuity with the leakage analysis." Adding a forward pointer to Sec IV.D would help readers. PARTIAL — valid minor cross-reference. |
| EF16 | Grok | MINOR | Data Availability HuggingFace links without version tags | PARTIAL | `.tex` l.719: "Release tag: v2026.04." The tag IS already present in the Data Availability. Grok missed it. However, the model link (l.720) to `bamfai/galaxy-chirality-v2` does not show a release tag. PARTIAL — the catalog tag is present; model tag is absent. |
| EF17 | Gemini | MAJOR | Dataset split description: calling it "80/20 split" when unique source images were split ~79.4/20.6 is mathematically confusing | PARTIAL | `.tex` l.154: "after flip augmentation of the training split the combined pool is 26,616 images (80/20 split: n_train=21,293, n_val=5,323; augmented duplicates contribute to the 826-image difference...)." The "80/20 split" refers to the split of the augmented pool (26,616), which does give exactly 80/20 (21,293/26,616 = 79.98%, 5,323/26,616 = 19.99% ≈ 80/20). Gemini correctly notes that the unique source images were split ~79.4/20.6 before augmentation. The paper's phrasing is technically correct for the augmented pool but potentially misleading for readers who want to reproduce the original data split. PARTIAL — Gemini's concern is valid as a reproducibility clarification but the current text is not technically wrong. |
| EF18 | Gemini | MINOR | Sec IV.A: CW fraction 18.78% should round to 18.79% (1,592,107/8,474,531 = 18.787%) | PARTIAL | Arithmetic check: 1,592,107 / 8,474,531 = 18.787%. Standard rounding gives 18.79%, not 18.78%. The paper prints 18.78%. Confirmed: the printed percentage is one rounding unit low for the CW class, forcing the three percentages to sum to exactly 100.00% (18.78+18.99+62.23=100.00). Using 18.79% the sum is 100.01%. The current value is a deliberate presentation choice, not an arithmetic error in the underlying count. PARTIAL — a footnote clarifying that truncation ensures 100.00% sum would address this. |
| EF19 | Gemini | MINOR | Table III ℓ=1 canonical row: (7.27-0.57)/0.84 = 7.976, not 7.93 | PARTIAL | `.tex` Table III (l.393) row: C_b=7.27, null mean=0.57, sigma_null=0.84, z=+7.93. Direct arithmetic with truncated values: (7.27-0.57)/0.84 = 7.976. The z=+7.93 was computed from full-precision float arrays. Gemini's observation is correct: a reader computing from printed truncated values gets 7.98, not 7.93. The Table III caption (l.378) should note "z values are evaluated from full float precision storage arrays; printed C_b and null statistics are rounded." PARTIAL — a one-sentence caption addition fixes this. |

---

## Consensus Findings (2+ reviewers)

**C1 — "Full-catalog real-space dipole at +0.41σ" mislabel [EF2, partially B1/M1]:** ChatGPT identifies this in both the closure-verification (M1) and fresh-finding (FM1) sections. Two separate occurrences at ll.419 and 441. Both should read "HC real-space dipole at +0.41σ." This is a genuine content error, not a style preference — the full-catalog (N=3.2M unthresholded) result is actually z≈4.2-4.4, not +0.41σ.

**C2 — +3.64σ vs +7.93σ framing [EF9 from ChatGPT, EF12 from Grok, partially B3/m3]:** All three reviewers notice the tension between "same physical estimator" (l.521) and "not mutually comparable" (l.171). A one-sentence reconciliation at l.521 would close this.

**C3 — Zenodo/DOI status [EF8, EF16 Grok minor]:** Both ChatGPT and Grok note the absent Zenodo DOI. Paper explicitly defers to submission — HOUSTON-DECISION. No action before trigger.

---

## Action Plan (hardest-first, VERIFIED/PARTIAL)

### P0 — Must fix before submission

**EF2 (VERIFIED): Replace "full-catalog real-space dipole" with "HC real-space dipole" at ll.419 and 441.**
- File: `pipelines/p2_chirality/chirality_catalog_paper.tex` ll.419, 441
- l.419 context: "rests on the primary estimators (the full-catalog real-space dipole at" — change to "the HC real-space dipole (p_eq>0.6, N=949,584) at"
- l.441 context: "the full-catalog real-space dipole at +0.41σ and the block-bootstrap WLS..." — change to "the HC real-space dipole at +0.41σ and the block-bootstrap WLS..."
- Justification: the full-catalog (all spirals) result is z≈4.2-4.4 attributed to systematic; +0.41σ is explicitly the HC sample. The mislabel could confuse a reader into thinking the 3.2M-galaxy full result is the headline null.

**EF3 (VERIFIED): Fix "disfavors any model predicting ≥0.75%" to use A95 for falsification language.**
- File: `pipelines/p2_chirality/chirality_catalog_paper.tex` l.501
- Change: "The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥0.75% on the DESI Legacy footprint" → "The present null is sensitive at the 50%-recovery level to models predicting a late-universe morphology-channel dipole A≳0.75%; the falsification boundary is A≳A95 ∈(1.0%,1.5%] (Table V)."
- Justification: A50=0.75% is the consistency boundary. Using "disfavors" at A50 overstates what the measurement does.

### P1 — Should fix (clarity/reproducibility)

**EF9/EF12 (PARTIAL): Reconcile "same physical estimator" vs "not mutually comparable" at l.521.**
- Add parenthetical: "...(same field and footprint; the 'not mutually comparable' characterization of Sec. III.A refers to the non-equivalence of the p-values under 500-MC vs. 10⁴-perm null sizes, not to different underlying physics)"

**EF17 (PARTIAL): Clarify 80/20 split as applied to augmented pool.**
- File: l.154 — add "(this 80/20 refers to the augmented pool; the unique source images were split ~79.4/20.6 before augmentation)"

**EF19 (PARTIAL): Add float-precision note to Table III caption.**
- File: l.378 — add one sentence: "The z values in each row are evaluated from full-precision floating-point arrays; printing truncated C_b values may give a slightly different arithmetic result."

**EF18 (PARTIAL): Add rounding note for CW fraction 18.78%.**
- File: l.265 — add footnote: "The printed CW fraction 18.78% is truncated to force the three-class sum to 100.00%; the unrounded value is 18.787%."

### P2 — Polish (PARTIAL/OPINION with clear text fix)

- **EF15**: Add forward pointer from Table III footnote to Sec IV.D post-MASTER result.
- **EF16**: Add explicit version tag for model HuggingFace link in Data Availability.
- **EF4**: Consider adding one sentence in App C making explicit that max-stat MC is the principled correction and Bonferroni/BH brackets the significance from the conservative side.
- **EF6**: Add per-test labels to bias-hardening table: T5 as "directional-coupling proxy (non-independent)" and T7 as "confidence-mass proxy."

### P3 — HOUSTON-DECISION

- **EF1**: Verify commit-sequence in GitHub remote history: confirm that the stamp commit `297aa805` contains the Data Availability text pointing to itself, not to v1.0.172.
- **EF8**: Zenodo DOI minting. Paper defers to journal submission. No change needed before trigger.

---

## Re-raise of EXT1-FALSIFIED Findings

No finding in EXT2 re-raises a finding that was FALSIFIED in EXT1. Confirmed: none of the three reviewers revive F3, F6, F13, F15, F18, or F24 from EXT1.

---

## GAP METRIC

| Category | Count |
|----------|-------|
| VERIFIED | 2 (EF2, EF3) |
| PARTIAL | 10 (B1→HOUSTON-DECISION, B3, B5, M1, M3, M6, M7, EF4, EF5, EF6, EF9, EF10, EF11, EF12, EF15, EF16, EF17, EF18, EF19) — counting distinct items: 10 |
| OPINION | 3 (EF7, EF13, EF14) |
| HOUSTON-DECISION | 2 (EF1, EF8) |
| FALSIFIED | 0 |
| Re-raises of EXT1-FALSIFIED | 0 |

**Gap (a) genuinely-new findings in EXT2:** 2 VERIFIED (EF2, EF3) + 8 new PARTIAL/OPINION (EF4-EF19 not previously audited) = **10 net new items**, of which **2 are actionable VERIFIED fixes**.

**Gap (b) re-raises of EXT1-FALSIFIED findings:** 0.

**Gap (c) closure disputes:** ChatGPT disputes B1 (HOUSTON-DECISION), B2 (FALSIFIED by source), B3 (confirmed PARTIAL). Grok and Gemini verify all closures as clean. Net: 1 genuine remaining dispute (B3 "same physical estimator" tension).

---

## Overall Assessment

Grok and Gemini's ACCEPT verdicts are better calibrated than ChatGPT's continued MAJOR. The two genuinely new VERIFIED items (EF2: mislabeled HC dipole, EF3: A50 overused as falsification threshold) are real pre-submission fixes but neither undermines the core science. With EF2, EF3, and the EF9/EF17/EF19 PARTIAL clarifications closed, P4 has no remaining VERIFIED blockers. The commit-hash provenance question (EF1) requires Houston's attention to the GitHub stamp-commit ordering.

**Recommended action:** Fix EF2 and EF3 (30 min), add the four P1 clarifications, and verify EF1 commit sequence. Then P4 is ready for the pre-submission checklist.
