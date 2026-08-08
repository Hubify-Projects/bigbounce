# P3APJS M2c truth-audit (vs v3.1.158-apjs) — ChatGPT REJECT retry, release-live; completes the M2 wave

**Wave role:** M2c is the recovered ChatGPT EXT leg (the M2 ChatGPT GAP; FAILED-dead in
M2, retry harvested here) on the release-live P3 ApJS variant (v3.1.158-apjs; pinned
immutable release `p3-v3.1.157` + DP3-15 held-out re-inference honesty upgrade in
v3.1.158). Verdict word: **REJECT**. Grok M2 (MAJOR, adjudicated in `M2/P3APJS_truth_audit_M2.md`,
0 genuinely-new) already dissolved its immutable-release hinge; M2c tests whether
ChatGPT's does too.

## ChatGPT M2c — REJECT (17 MAJOR + 2 MINOR; ledger_match 11/19 auto, all 8 UNMATCHED Opus-adjudicated → RE-FLAG)

| # | sev | verdict | source-cited disposition |
|---|-----|---------|--------------------------|
| 1 | MAJOR | RE-FLAG-DISCLOSED | DP3-07/-09/-14 — abstract process-volume "not confirmed detections … 2,468 like-for-like"; footnote ♡ tabulates 77,905/19,253/12 threshold families. |
| 2 | MAJOR | RE-FLAG-DISCLOSED | DP3-07/-11 — §3.1 SPECTYPE≠TARGETTYPE; "different filter stacks" is the paper's own disclosure. |
| 3 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-01/-12 — 5-fold not out-of-fold (80% in-sample); folds fail val_loss gate; §pathc_caveats(i) states the two Jaccard checks are correlated fold-stability probes, NOT independent gates. |
| 4 | MAJOR | RE-FLAG / OPEN-COMPUTE | DP3-15 — no production held-out re-inference; pod-lost native parquets; §II.F DP3-15 disclosure now quantifies the pod-block + demonstrates pipeline reproduction (v3.1.158). |
| 5 | MAJOR | RE-FLAG-DISCLOSED | DP3-11 — §3.1 ZWARN/SPECTYPE composition reported honestly; count labeled "anomaly-candidate," not a purity claim. |
| 6 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-12 — injection-recovery = model sensitivity not FDR/catalog reliability; disclosed §II.F + tab:caveats. |
| 7 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-13/-09 — selection function / downsample-496 / unweighted-MSE / no inverse-variance masking all disclosed as future-work / by-design. |
| 8 | MAJOR | RE-FLAG-DISCLOSED | DP3-14 — cross-transfer vs native-77,905 conflation; footnote ♡ discloses classification stats derive from cross-transfer, released tier is native re-score; overlap = DP3-15 pod-blocked gap. |
| 9 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-11/-13 — SDSS Spearman ρ=0.036 kept WITH the negligible-effect-size caveat; not headlined. |
| 10 | MAJOR | RE-FLAG-DISCLOSED | DP3-06 — Planck spatial leakage; paper discloses 152/200-in-training + overlapping-tile inflation as a lower bound needing a spatial jackknife; over-representation toward HELD-OUT patches. |
| 11 | MAJOR | RE-FLAG-DISCLOSED | DP3-06 — Planck 5σ post-standardization bump = disclosed sensitivity gate; patches labeled reconstruction-outlier tiers, not "validated CMB anomalies." |
| 12 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-07/-09 — 17.8% novelty labeled "database-coverage measurement, NOT a discovery rate" (Wilson CI disclosed). |
| 13 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-07 — 58.8% pooled/stale-denominator figure carries the disclosed-caveat footnote; 17.8% is the headline. |
| 14 | MAJOR | RE-FLAG-DISCLOSED | DP3-03/-04 — 37.3M process-volume; footnote ⊗ reconciles 36.76/36.93/37.29M (verified 37,272,042 = 37,292,042 − 20,000). |
| 15 | MAJOR | RE-FLAG-DISCLOSED | DP3-20/-18 — Data-Availability contradiction: LAMOST excluded from released tables (failed-exploratory, §lamost) is exactly the v3.1.157 release wording; pod-blocked artifacts = DP3-15, NOT the immutable-release bar (see below). |
| 16 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-10 — §V f_NL forecast "Secondary Demonstrations," returns null; App C/E estimator caveats; the 8.98-vs-16.85 incompatible-normalization point already truth-audited RE-FLAG (H17G MAJOR#13); Table IX/Fig-11 disclosed as distinct non-comparable representations. |
| 17 | MAJOR | RE-FLAG-DISCLOSED | DP3-10 — Bayes-factor KDE tail: §V.1 secondary; App E discloses the KDE/tail estimation; "decisive" scoped by the env-SMBHB caveat. |
| 18 (UNMATCHED) | MAJOR | RE-FLAG-DISCLOSED | DP3-11 — twelve z≃6 QSO candidates labeled "High-z QSO Candidates" (not Confirmed); internal-evidence-only, follow-up disclosed as needed. |
| MINOR-a | MINOR | RE-FLAG-DISCLOSED | DP3-16 PROCESS-NIT — superseded-labeled figures retained per CRITICAL RESEARCH DIRECTIVE. |
| MINOR-b (rewrite) | MINOR | OPINION | DP3-16 — presentation/venue OPINION, pattern-066, Houston-gated. |

## CRITICAL: the immutable-release hinge has DISSOLVED (parallel to Grok M2)

The prior ChatGPT ApJS REJECT hinge (M1/H17G) was the verbatim **"catalog described
prospectively rather than supplied as an immutable reviewable release … disqualifying
for an ApJS catalog submission"** = DP3-20, CLOSED-BY-RELEASE in v3.1.157. **M2c does
NOT re-raise that bar.** Its only Data-Availability MAJOR (raw L41) now reads:

> "…the manuscript states that the native score parquets required for full held-out
> re-inference are unavailable … the manuscript also acknowledges that key DESI
> production-score artifacts and the Planck checkpoint/tensor needed for full
> re-inference are unavailable. The assertion that every headline result is
> independently recomputable from the public release is therefore not demonstrated."

That is the **pod-blocked end-to-end re-inference residual (DP3-15, OPEN-COMPUTE)** — a
disclosed methodology limitation needing a GPU re-run, NOT an edit — plus the standing
**catalog-vs-PRD validated-purity venue judgment (DP3-07/-09/-12/-16, Houston-gated)**.
The pinned tag `p3-v3.1.157` + `RELEASE_MANIFEST.json` (25 files, SHA-256) + recompute
recipe are live in the tex (L1700) and M2c does not challenge them. The "disqualifying"
bar is gone.

### Remaining REJECT basis (verbatim, closing line):
> "The central claim that the paper delivers a validated catalog-grade set of 268,519
> real anomalies is not supported by the evidence presented, because its membership is
> partly post hoc or predetermined, its validation does not establish catalog purity or
> production-level out-of-sample stability, and its dominant DESI and SDSS sample
> definitions remain internally inconsistent."

Category: **(b) standing catalog-vs-PRD / validated-purity venue-and-validation judgment
(DP3-07/-09/-12/-16, Houston-gated) + (c) disclosed pod-blocked out-of-sample residual
(DP3-15, OPEN-COMPUTE).** NOT (a) the closed immutable-release bar; NOT (d) a genuinely-new
editable defect.

## FINAL COUNT
Genuinely-new real editable findings: **0.** All 19 findings map to standing DP3-xx with
source-cited verdicts; identical to the H17G ChatGPT REJECT class, none re-raising the
closed DP3-20 immutable-release bar. ChatGPT REJECT→REJECT on unchanged disclosed content
= DP3-17 backfire floor (directive-H maximal-harsh-referee structural floor).

## Streak
The M2 wave already recorded Grok EXT clean (0 genuinely-new, streak conservatively held
pending this ChatGPT retry). M2c = 0 genuinely-new, hinge confirmed dissolved →
**the M2 wave completes clean; streak 0 → 1.** No bump; v3.1.158 stands. `directive_g.sh`
not run (no edit).

## Integrity
Raw REJECT READ verbatim before disposition. The immutable-release-hinge dissolution
verified from the raw (L41) against the tex closure (L1700), not inferred from the verdict
label. Every finding source-cites a live tex line / DP3-id. DP3-15 residual honestly kept
OPEN-COMPUTE, not papered over. No ACCEPT faked; no math fabricated.
