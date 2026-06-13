# EXT6 P5 Truth Audit — v0.1.69 (8a6e800f)

**Audit date:** 2026-06-12 PT
**Paper:** Paper 5 — DESI chirality / DESIVAST three-algorithm test, v0.1.69
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Grok Heavy (ACCEPT), Gemini Thinking (MINOR REVISIONS)
**Source of truth:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`,
`outputs/30_ext4_galzone_complement_contrasts.json`,
`outputs/31_ext5_appendixB_tables.json`
**Protocol:** [`feedback_peer_review_truth_audit_protocol.md`] · pattern-052 re-raise auto-falsify · pattern-pre-EXT4 closures binding

**Calibration signal:** Grok Heavy moved from MINOR (EXT5) → **ACCEPT** (EXT6). Grok performed
a full end-to-end re-read of v0.1.69 and confirmed all prior items closed with no regressions and
no new BLOCKERs/MAJORs. This is the cleanest non-Anthropic verdict to date on P5 and the strongest
calibration anchor for the audit: any external finding that conflicts with Grok's pass requires
extra-strong on-disk evidence.

---

## Verdict schema

- **VERIFIED** — finding correct against source/artifact on disk.
- **FALSIFIED** — finding contradicted by source/artifact.
- **STALE / RE-RAISE** — already closed in prior round (EXT4 GALZONE / R35conf 3.56%). Auto-falsify per pattern-052.
- **MISLABELED** — real but severity wrong (e.g., MINOR called MAJOR).
- **OUT-OF-SCOPE** — outside paper claims.
- **GENUINE-NEW** — not in any prior round, verified on disk.

---

## Section A — ChatGPT findings

ChatGPT opening paragraph itself states: *"the GALZONE estimand-family fix is real, Appendix B's
contingency-table regression is fixed, and the duplicate-row bookkeeping is now internally
consistent."* The MAJOR REVISIONS verdict is driven entirely by **carry-over B3** (k=20 VoidFinder
headline retained for continuity, not by GALZONE or 3.56% re-raise).

### A1. GALZONE estimand-family — is ChatGPT raising a new issue?

| Field | Value |
|---|---|
| Claim | "GALZONE estimand-family fix is real" (top of report); no new finding in §3 |
| Cited tex location | §VIII.D, Table X area |
| On-disk verification | tex l.453–459 prints the two GALZONE catalog-native two-sample contrasts: V2-REVOLVER \|Δ\|=0.0037, z=−1.25, p=0.21, n_void=104,912 vs n_non-void=40,877; V2-VIDE \|Δ\|=0.0019, z=+0.72, p=0.47, n_void=74,111 vs n_non-void=71,678. Tex l.1016–1019 lists all five Bonferroni-5 estimators uniformly as "void vs non-void f_CW". Artifact `30_ext4_galzone_complement_contrasts.json` reproduces every number to four decimals. |
| Verdict | **VERIFIED-CLOSED (NOT a re-raise)** — ChatGPT is acknowledging the EXT4 closure, not challenging it. No action. |

### A2. 3.56% duplicate tracking — is ChatGPT naming a NEW site missing the denominator?

| Field | Value |
|---|---|
| Claim | "duplicate-row bookkeeping is now internally consistent" (top of report); no new finding in §3 |
| Cited tex location | n/a — ChatGPT raises no new duplicate-tracking site |
| On-disk verification | 5 in-prose sites with `3.56%` all carry the inline denominator "of 812,793 env-labeled rows" (tex l.384, l.1063, l.1116, l.2340, l.2426). Zero stale `2.7%` strings remain anywhere in the tex (verified with full-file grep). |
| Verdict | **VERIFIED-CLOSED (NOT a re-raise)** — ChatGPT is acknowledging the R35conf fix, not challenging it. No action. |

### A3. New MAJOR — "largest controlled sample (n=56,981)" misleading vs V2-REVOLVER 102,911/104,912

| Field | Value |
|---|---|
| Claim | tex l.944 says DESIVAST primary has "the largest controlled sample (n=56,981)" but the same Bonferroni-5 family in §VIII.D reports V2-REVOLVER sphere-PIS n_void=102,911 and V2-REVOLVER catalog-native GALZONE n_void=104,912 |
| On-disk verification | tex l.944–945 confirms wording: `it has the largest controlled sample ($n_{\rm void}^{\rm DESIVAST} = 56{,}981$)`. Artifact `30_ext4_galzone_complement_contrasts.json` confirms V2-REVOLVER catalog-native n_void=104,912 ✓ |
| Verdict | **GENUINE-NEW MINOR (mislabeled MAJOR)** — Wording inconsistency real. Severity is wording/ledger fix, not a science change; mislabeled as MAJOR. Closure: replace "largest controlled sample (n=56,981)" with "a properly powered VoidFinder DESIVAST sample (~130× the V-Web void bin); the largest single DESIVAST row is V2-REVOLVER catalog-native GALZONE n_void=104,912." |

### A4. New MAJOR — footprint-restricted result not in main primary table

| Field | Value |
|---|---|
| Claim | The footprint-restricted control (n_void=57,081, Δf_CW=+0.0018, z=+0.78, p=0.43) lives in §VIII.E rather than as a row in Table X (the primary table) |
| On-disk verification | tex search confirms the footprint result is in §VIII.E sky-stratification block; Table X (anchored near tex l.2120) shows the original three sphere-PIS rows. Result is genuinely positioned outside the primary-family table. |
| Verdict | **GENUINE-NEW MINOR (mislabeled MAJOR)** — Real placement issue, but adding a single row or sibling table is presentation-polish, not a science gap. Severity MINOR not MAJOR. Closure: add row "VoidFinder exact, hole-support-footprint-restricted control" to Table X or new Table XI. |

### A5. New MINOR — Fig. 3 PNG title still says n=791,635

| Field | Value |
|---|---|
| Claim | Plot title baked into `fig_p5_cw_by_env_bar.png` reads "n = 791,635" while the LaTeX caption reads "n=812,793 env-labeled spiral rows" |
| On-disk verification | LaTeX caption (l.1110–1112) correctly states 812,793 env-labeled rows covering 783,820 of the 791,635 unique. Baked-in PNG title cannot be verified from .tex alone. |
| Verdict | **GENUINE-NEW MINOR (figure-asset regen needed)** — Cosmetic. Regenerate `fig_p5_cw_by_env_bar.png` with corrected title string. |

### A6. New MINOR — paper title parent "791,635 DR1 matched spirals"

| Field | Value |
|---|---|
| Claim | Title (tex l.305) says "across 791,635 DR1 Matched Spirals" but the V-Web env-labeled parent is 783,820 unique / 812,793 rows |
| On-disk verification | tex l.305 confirms title: "Cross-Check Across 791,635 DR1 Matched Spirals". 791,635 is the chirality-relevant matched-spiral parent (correct number for "DR1 matched spirals"); the V-Web env-labeled subset is 783,820 of those 791,635. So the title number is technically the full matched parent, but reads as if it's the env-labeled parent. |
| Verdict | **GENUINE-NEW MINOR** — Title is ambiguous, not strictly wrong (791,635 IS the full matched-spiral parent). Closure: re-word to "across the DR1 matched-spiral sample" or "across 783,820 environment-matched spirals" per ChatGPT's proposed fix. |

### A7. New MINOR — residual RSD sentence

| Field | Value |
|---|---|
| Claim | §VIII opening still contains an outdated lead-in: "bounds the fractional membership shift to well below the statistical uncertainty" — while the later, correct sentence in the same section reports membership rises 57,081 → 76,490 ± 161 (~34%) |
| On-disk verification | Cited but not directly grepped here. Plausible carry-over from earlier draft layer; ChatGPT consistently identified this thread across rounds. |
| Verdict | **GENUINE-NEW MINOR (provisional)** — Wording cleanup. Closure: delete the obsolete sentence; retain "void membership is not insensitive; Δf_CW is stable under fixed-void-geometry perturbation." |

### A8. New MINOR — data-availability DOI promised, not printed

| Field | Value |
|---|---|
| Claim | Appendix C data-availability still says DOI will be minted upon journal submission; no DOI printed |
| On-disk verification | Standard pre-submission posture; legitimately tracked. |
| Verdict | **VERIFIED-DEFERRED (OUT-OF-SCOPE for closure now)** — Genuine but resolves at journal submission, not at this audit. Track as caveat. |

### A9. Carry-over B3 — k=20 VoidFinder headline retained "for continuity"

| Field | Value |
|---|---|
| Claim | Paper headlines 56,981 k=20 VoidFinder void spirals; exact k-unbounded rerun gives 57,081 (+100); ChatGPT says the headline should switch to exact rerun |
| On-disk verification | Verified that 56,981 is the headline VoidFinder count in title, primary-path declaration, and Table X. The exact rerun (57,081) is reported but not headlined. |
| Verdict | **GENUINE-CARRY-OVER (severity disputed — judgment call, not science change)** — The +0.18% membership shift between k=20 and exact does not change any verdict (paper is null either way). Houston's published preference is to keep the conservative k=20 headline with the exact rerun as cross-check. This is the source of ChatGPT's MAJOR REVISIONS verdict and is the same disagreement as EXT5. Both Grok and Gemini consider it closed. Tag as **DEFERRED-AUTHOR-DECISION** (not a closure-blocking finding). |

---

## Section B — Grok findings

### B1. All closures verified, no new BLOCKERs/MAJORs

| Field | Value |
|---|---|
| Claim | Full end-to-end re-read (31 pp.); ACCEPT recommendation |
| On-disk verification | Two cited polish items (Table VIII caption k-sufficiency guard; §VIII.D explicit GALZONE complement counts n=40,877 / n=71,678) both verified in tex and artifact JSON ✓ |
| Verdict | **VERIFIED — CALIBRATION ANCHOR** — Grok's ACCEPT is the cleanest signal in the round. |

---

## Section C — Gemini findings

### C1. MAJOR — Appendix sequence indexing & cross-reference audit

| Field | Value |
|---|---|
| Claim | New Appendix B (contingency tables) shifts the appendix layout tree; if cross-references are hardcoded ("Section V pointing to Appendix B for data availability") they will resolve to wrong targets |
| On-disk verification | Full-file grep for `Appendix [A-Z]\b` outside comment blocks: **zero hits**. All cross-references use `\ref{}` macros tied to labels (`app:toy_eft`, `app:contingency`, `sec:data_code`). The appendix ordering in the .tex file is: `\appendix` → `app:toy_eft` (l.3307) → `app:contingency` (l.3375) → `sec:data_code` (l.3446). Every inline reference uses the label macros, which auto-resolve regardless of order. |
| Verdict | **FALSIFIED** — Premise is wrong. No hardcoded appendix letters exist in the tex; the LaTeX label/ref system handles reorder automatically. Closure: none required. |

### C2. MINOR — stale 2.7% strings in Section IV A and Figure 3 caption

| Field | Value |
|---|---|
| Claim | Sweep .tex to confirm old 2.7% string is fully purged |
| On-disk verification | Full-file grep for `2.7%` / `2\.7\\percent`: **zero hits** in non-comment text. Reference inline at l.384, l.1063, l.1116, l.2340, l.2426 all use 3.56% with the 812,793 denominator. |
| Verdict | **FALSIFIED (STALE / RE-RAISE)** — Already closed in R35conf (pattern-052). No action. |

---

## Counts

| Reviewer | Findings (non-closed) | Verified-Closed | Genuine-New | Falsified/Stale | Mislabeled (severity demotion) |
|---|---|---|---|---|---|
| ChatGPT | 7 new (2 MAJOR, 4 MINOR, 1 carry-over B3) + 2 verified-closed at top | 2 | 5 (A3, A4 demoted MAJOR→MINOR; A5, A6, A7 MINOR) + 1 deferred (A8) + 1 author-decision (A9) | 0 | 2 (A3, A4) |
| Grok | 0 new findings; ACCEPT | n/a | 0 | 0 | 0 |
| Gemini | 1 MAJOR + 1 MINOR | 0 | 0 | 2 (C1 falsified, C2 stale re-raise) | 0 |
| **Totals** | **9 net new candidates** | **2** | **5 genuine-new + 1 deferred + 1 author-decision** | **2** | **2** |

**Genuinely-new actionable count: 5** (all MINOR after demotion).

---

## Top closure (highest leverage)

**A5 + A6 — figure title + paper title parent-number sync.**
Both are mechanical: regenerate `fig_p5_cw_by_env_bar.png` with `n = 812,793 env-labeled rows`
in the title bar, and re-word the paper title to "across the DR1 matched-spiral sample" (or
"across 783,820 environment-matched spirals"). One commit, two surfaces, closes the most visible
"the headline number doesn't match the methods section" complaint that drove Gemini's MINOR REVISIONS
verdict and one of ChatGPT's MINORS.

After A3 + A4 + A5 + A6 + A7 closure: P5 has zero open MINORS from EXT6 and Grok-equivalent ACCEPT
posture across two of three external reviewers (Grok: clean; Gemini: falsified, no real action; ChatGPT:
all genuine items are MINOR-polish, plus the standing B3 author-decision about k=20 headline).

---

## Pattern-052 (re-raise auto-falsify) hits

- **Gemini C2** — stale 2.7% re-raise → FALSIFIED.
- **ChatGPT A1, A2** — acknowledged by reviewer himself as closed; not re-raises but confirmations.

---

## Pattern impact

- Pattern-052 (re-raise auto-falsify) caught 1 of Gemini's 2 findings.
- Pattern-pre-EXT4 (GALZONE) and pattern-R35conf (3.56%) closures held under independent re-review by all three vendors.
- Severity-inflation pattern: ChatGPT mislabeled 2 MINOR-polish items as MAJOR (A3, A4). Worth tracking in r-round-pattern-mine for a possible new pattern: "external reviewer escalates wording/placement to MAJOR when underlying science is unchanged."

---

## Recommendation

Calibration: **Grok ACCEPT** = strongest signal; **Gemini MINOR REVISIONS** = falsified entirely;
**ChatGPT MAJOR REVISIONS** = driven by author-decision carry-over (B3) plus 5 polish items.

Effective external-reviewer posture on v0.1.69:
- 2 of 3 reviewers (Grok, Gemini after audit) show **zero open MAJORS or BLOCKERS**.
- 1 of 3 (ChatGPT) shows 0 verified MAJORS (after severity demotion) + 1 author-decision item.
- Net: P5 is at the polish-pass threshold. No re-run / re-MCMC / re-classification required.

**Closure bundle for the next paper-version bump (v0.1.70):**
1. A3 — re-word "largest controlled sample" line at tex l.944.
2. A4 — add hole-support-footprint-restricted row to Table X (or new Table XI).
3. A5 — regenerate `fig_p5_cw_by_env_bar.png` with corrected n=812,793 title.
4. A6 — re-word paper title parent-count to "DR1 matched-spiral sample" or "783,820 environment-matched spirals".
5. A7 — strike the obsolete RSD lead-in sentence in §VIII opening.
6. Defer A8 (DOI on journal acceptance) and A9 (k=20 headline = author decision) per Houston's prior posture.

After closure → readiness oscillation: v0.1.69 → v0.1.70 + clean three-stage review on the bumped version.
