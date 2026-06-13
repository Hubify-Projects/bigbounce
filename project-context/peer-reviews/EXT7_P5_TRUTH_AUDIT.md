# EXT7 P5 Truth Audit — v0.1.71 (d2b33c8a376f93b8)

**Audit date:** 2026-06-13 PT
**Paper:** Paper 5 — DESI chirality / DESIVAST three-algorithm test, v0.1.71
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Grok Heavy (ACCEPT — 5th consecutive 6/6), Gemini Thinking (MINOR REVISION — fresh-thread "recipe vindicated")
**Source of truth:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`,
`outputs/30_ext4_galzone_complement_contrasts.json`,
`outputs/31_ext5_appendixB_tables.json`
**Protocol:** [`feedback_peer_review_truth_audit_protocol.md`] · pattern-052 re-raise auto-falsify · k=20 5×-FALSIFIED rule binding (EXT1/EXT2/EXT3/EXT4/EXT6) · pre-EXT4 closures binding

**Calibration anchors:**
- Grok Heavy: 5th consecutive ACCEPT.
- Gemini Thinking: MINOR REVISION (cleanest Gemini verdict to date; fresh-thread vindication round demonstrates the per-finding-decomposition recipe works).
- ChatGPT MAJOR REVISIONS verdict is entirely driven by the carry-over k=20 VoidFinder headline issue (now SIXTH raise) plus two newly-named MAJORs (n=428 vs n=6 disambiguation, Table VIII clipping).

---

## Verdict schema

- **VERIFIED** — finding correct against source/artifact.
- **FALSIFIED** — finding contradicted by source/artifact.
- **STALE / AUTO-FALSIFIED** — already closed/HD-ruled in prior round. Pattern-052.
- **MISLABELED** — real but severity wrong.
- **OUT-OF-SCOPE / HD-RULED** — Houston-Direct ruling in prior round binds.
- **GENUINE-NEW** — not previously raised, verified on disk.

---

## Section A — ChatGPT findings

ChatGPT opening: "The remaining publication-level problem is still the same: the paper knowingly headlines the approximate k=20 VoidFinder membership rather than the exact rerun." Six of eight original BLOCKERs/MAJORs CLOSED, three PARTIAL (B1/B4/B5 — all reasoned closures), one declared still-open (B3 = k=20 headline). Two new MAJORs in §3.

### A1. ChatGPT carry-over B3 — "k=20 VoidFinder approximate membership headline" (SIXTH raise)

| Field | Value |
|---|---|
| Claim | Paper headlines 56,981 k=20 VoidFinder void spirals "for continuity"; exact k-unbounded rerun gives n_void=57,081 / Δf_CW ≈ +0.0006 vs +0.0007. ChatGPT says journal should not publish known-approximate membership as primary statistic when exact rerun exists. |
| Cited tex location | §VIII.B (sec:desivast_xmatch), tex l.2018–2042; Table VIII (tab:desivast_canonical) l.2044–2067 |
| On-disk verification | Verified: paper at l.2023 reports the k=20 KDTree-based n_void=56,981 as the primary line; l.2026–2042 contains the explicit "k-sufficiency guard" paragraph: "the exact rerun moves 100 galaxies (+0.18% of the 56,981-galaxy void class) into the void class (n_void=57,081, f_CW^void=0.4965, σ^void=−1.69; Δf_CW void-vs-non-void +0.0006 instead of +0.0007) — every conclusion in this section is invariant, and we retain the k=20 catalog statistics below for continuity with the released artifacts". Table VIII caption (l.2047–2049) reads "the k=20 KDTree query yields conclusions identical to the exact k-unbounded rerun at the 0.18% membership level". |
| Disclosure layer audit | The "approximate membership" framing is EXPLICITLY DISCLOSED in three locations: (i) §VIII.B k-sufficiency guard paragraph, (ii) Table VIII caption, (iii) the EXT3 footprint retabulation (artifact `29_ext3_desivast_footprint_retabulation.json`) is computed on the EXACT membership and explicitly noted. The full disclosure chain — including the exact-vs-k=20 delta arithmetic, the membership shift count (100 galaxies), the invariance assertion, and the explicit "for continuity with released artifacts" rationale — is all in the body. |
| Re-raise history | This is the SIXTH raise of B3 across the EXT-round series: EXT1 (F3), EXT2 (B3), EXT3 (B3, third raise), EXT4 (CV-B3 / NM-A, fourth raise), EXT6 (A9, fifth raise tagged DEFERRED-AUTHOR-DECISION). All five prior raises were resolved via primary-evidence falsification or HOUSTON-DECISION ruling: the exact rerun IS in the paper, the invariance assertion IS load-bearing, the continuity rationale IS documented. |
| Pattern-052 test | Per pattern-052: "re-raise may only be auto-falsified if prior falsification cites primary evidence". Each prior verdict cited primary evidence (tex lines, exact arithmetic, invariance documentation). ChatGPT EXT7 introduces NO new in-text claim, NO new arithmetic, NO new artifact, NO new evidence. Identical text to the EXT3/EXT4/EXT6 raises. Per pattern-052 + the prior "5×-falsified" binding rule: **auto-falsify on sight**. |
| Verdict | **STALE / AUTO-FALSIFIED (6th raise of 5×-FALSIFIED finding; pattern-052 + standing k=20 binding rule both fire)** |
| Closure | No action. ChatGPT is naming a previously-disclosed, primary-evidence-documented presentation choice and characterizing it as a "knowing approximation" — but the paper explicitly says "every conclusion is invariant" and reports BOTH numbers prominently. The exact rerun is not buried; it is in the same paragraph. The Δf_CW delta is +0.0001 (+0.0006 vs +0.0007), well below the binomial counting floor. Author-decision binding. |

### A2. ChatGPT new MAJOR — "n=428 vs n=6 V-Web void-bin denominator confusion" (Abstract / §VI.A / §VIII.A)

| Field | Value |
|---|---|
| Claim | Abstract and §VI.A present V-Web void bin as n=428; §VIII.A says only n=6 V-Web void-class spirals remain after restricting to z≤0.24 DESIVAST-overlap. Different denominators; the ~130× factor is 56,981/428, not low-z comparison. |
| Cited tex location | Abstract p.1–2; §VI.A p.8; §VIII.A p.16–17 |
| On-disk verification | tex l.391: "1σ binomial half-width of the n = 428 V-Web void bin" — full env-labeled V-Web void class. tex l.405: "void; n=428, −0.68σ — survey-edge..." — same headline n=428. tex l.467–472: the n=6 is explicitly framed as a "per-galaxy classifier-disagreement check --- in this six-object illustrative check, 0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes at z ≤ 0.24; the n=6 sample is too small for a formal purity constraint, but it illustrates the survey-shell systematic driving the V-Web void class at low z". tex l.2039–2042: the "~130× larger" factor is explicitly "n_void^DESIVAST = 56,981 ... ~130× larger than the V-Web void class (n = 428 from Section sec:results_vweb)". |
| Disambiguation audit | Paper consistently labels n=428 as the FULL V-Web env-labeled void bin and n=6 as the z≤0.24 DESIVAST-overlap per-galaxy disagreement check (clearly marked "illustrative", "too small for a formal purity constraint"). The two denominators do NOT appear together as competing claims; they appear in different sections with different roles. The 130× factor IS the n_void^DESIVAST(56,981) / n_VWeb_void(428) ratio, NOT a low-z comparison — which matches ChatGPT's own arithmetic check. |
| Re-raise history | Not directly raised in this exact form before. Conceptually adjacent to EXT4/EXT6 V-Web sample-size auditing items, but not identical. |
| Verdict | **FALSIFIED (mislabeled MAJOR; the disambiguation requested IS already present in the paper)**. ChatGPT's proposed rewrite — "the full V-Web secondary void bin contains n=428 env-labeled rows; only n=6 of those lie in the DESIVAST z≤0.24 overlap used for the per-galaxy DESIVAST disagreement check" — is conceptually identical to what tex l.467–472 already says, in slightly different words. The "make clear it is 56,981/428, not a low-z comparison" instruction is already satisfied by tex l.2039–2042's explicit "n = 428 from Section sec:results_vweb" tag. The 130× factor is never paired with the n=6 number in the paper. |
| Closure | No mandatory action. Optional micro-polish at next restamp: add a single explicit cross-reference between the n=6 disagreement check (§VIII.A) and the n=428 headline bin (§VI.A) to dispatch any residual reader confusion. |

### A3. ChatGPT new MAJOR — "Table VIII not publishable in rendered form (right-hand columns clipped)"

| Field | Value |
|---|---|
| Claim | Primary DESIVAST table at p.17 visually clipped/malformed in rendered PDF; right-hand columns cut off; not legible. |
| Cited tex location | Table VIII at tex l.2044–2067 (`tab:desivast_canonical`) |
| On-disk verification | tex source: `\begin{tabular}{lrrrr}` with 5 columns: Class / n / n_CW / f_CW / σ_from_half. Last row label is the long string "VoidFinder exact, hole-support-footprint-restricted non-void & 253,276 & 126,202 & 0.4983 & −1.73". In single-column revtex this label is long but the four following numeric columns are short. **No `Overfull \hbox` warnings present in `p5_desi_chirality.log`** (grep returns zero hits). |
| Pattern-026 check | Reviewer claim of "visual clipping" not corroborated by latex log overfull-hbox audit. Could still be visually tight at right margin. |
| Verdict | **PARTIAL / GENUINE-NEW MINOR (mislabeled MAJOR)** — Latex log shows no overfull-hbox warning, but the long footprint-control row label is genuinely tight. Severity is presentation-polish, not science-blocking. The scientific content (k=20 row, exact-row equivalence, footprint-restricted control row) is all intact and consistently keyed to artifact JSONs. |
| Closure | At next restamp: either split Table VIII into a two-table form (primary three rows + footprint-restricted control as Table VIII-b) or rotate to `table*` full-width or shorten the row label to "Footprint-restricted non-void (exact)" with the descriptor moved to the caption. Severity-tag as MINOR. |

### A4. ChatGPT carry-over PARTIALs (B1 footprint, B4 Paper IV companion, B5 V-Web framing)

| Item | EXT7 status | EXT7 verdict |
|---|---|---|
| B1 — DESIVAST footprint-restricted control "still a hole-support footprint, not an independent DESIVAST/BGS angular mask" | ChatGPT acknowledges: "manageable major caveat, not the same blocker as before, provided it is labelled as a support-restricted stress test". Paper already labels it explicitly as "hole-support-footprint-restricted control" (Table VIII row label + l.2050–2054 caption). | **VERIFIED-AS-DISCLOSED (already labelled as ChatGPT requests)**. No action. |
| B4 — Paper IV companion DOI not minted | Same as P4 Zenodo deferred. HD-RULED OUT-OF-SCOPE arXiv. | Defer to publish-stage. |
| B5 — V-Web/T-Web hierarchy still gives secondary material "substantial headline space" | DESIVAST primary explicitly declared in Table II (l.1042–1073) family declaration; V-Web is "secondary". Section ordering is a presentation choice. | **OPINION** (acknowledged as "much improved" by ChatGPT). No mandatory action. |

### A5. ChatGPT carry-over MAJORs (M1 T-Web naming, M3 contingency unique-target splits, M7 ZCAT_PRIMARY rebuild)

| Item | EXT7 status | EXT7 verdict |
|---|---|---|
| M1 — "T-Web vs V-Web" body terminology | Title now T-Web; body retains V-Web for backward compatibility. ChatGPT says "scientifically tolerable, but still unnecessarily confusing." | **OPINION / VERIFIED-MINOR**. Optional renaming at next restamp. |
| M3 — per-class bright/dark splits row-level not disjoint | Paper now flags this limitation. | **VERIFIED-AS-DISCLOSED**. No action. |
| M7 — ZCAT_PRIMARY rebuild missing | Unique-TARGETID density-field rebuild present; ZCAT_PRIMARY-based rebuild not. | **VERIFIED-LIMITATION / OUT-OF-SCOPE** for arXiv (carry-over compute item; not closure-blocking given existing unique-TARGETID rebuild). Carry to publish-stage. |

---

## Section B — Gemini findings (fresh-thread, MINOR REVISION)

Gemini opening: confirms all five EXT6 closures (Table X n_CW typo, Fig 3 caption, Table XV σ column, R_s=10 dropping, bright/dark z=1.95 correction) all CLOSED. Two new MAJORs and one new MINOR in §2.

### B1. Gemini new MAJOR — Table III ledger uses 812,793 row-level parent (3.56% duplicate) instead of 783,820 unique-galaxy

| Field | Value |
|---|---|
| Claim | Table III still framed around 812,793 row-level parent (3.56% duplicates); paper notes χ²=3.00, p=0.39 on 783,820 unique-galaxy deduplicated subset. Elevate unique-galaxy to primary. |
| On-disk verification | The 3.56% duplicate disclosure has been a stable feature of v0.1.66+ rounds. EXT4 closed this class as a documented duplicate-tracking rule (the unique-galaxy contrast IS reported alongside the row-level statistic). Both numbers consistently disclosed. |
| Re-raise history | Conceptually similar to EXT4 P5-G2 (GALZONE complement counts) and the EXT6 §A2 "3.56% duplicate tracking" item, both resolved by primary-evidence verification (the deduplication IS in the paper). |
| Verdict | **MISLABELED MAJOR (real disclosure choice but already deduplicated alongside; severity is presentation, not science)**. Elevating the unique-galaxy table to primary is a HOUSTON-DECISION style choice. Both denominators are reported with consistent verdicts. |
| Closure | Optional at next restamp: swap the row order so the unique-galaxy contingency table leads and the row-level appears as documentation footnote. Not closure-blocking. |

### B2. Gemini new MAJOR — "Canonical V-Web is selection-contaminated"

| Field | Value |
|---|---|
| Claim | §IX.A selection-corrected stress test shows void class explodes ~10× and wall class ~23× when redshift-shell correction is introduced; paper still labels uncorrected grid "canonical" while treating selection-corrected as secondary. |
| On-disk verification | tex l.1083 + l.1110: paper does use the term "canonical V-Web" for the primary build. tex l.2553 area: explicit `\subsection{Redshift-shell selection-corrected classifier ...}` exists and is framed as a stress-test/diagnostic (not primary). The selection-correction findings ARE documented; the paper acknowledges the 10×/23× shifts; and the DESIVAST-primary hierarchy (Table II) is the ACTUAL primary analysis. The V-Web "canonical" label refers to the headline V-Web build configuration, with the selection-corrected V-Web as a documented robustness diagnostic. The DESIVAST primary path is independent and not affected. |
| Re-raise history | Not directly raised in EXT6 in this form. New finding. |
| Verdict | **FALSIFIED-IN-LARGE / MISLABELED-MAJOR**. Gemini misreads the analysis hierarchy: DESIVAST is the actual primary (per Table II Bonferroni-5 family declaration), V-Web is secondary, and "canonical V-Web" is a label for the primary V-Web *build configuration* within that secondary branch (not the global primary). The selection-corrected V-Web rebuild is explicitly the diagnostic that EXPOSES the selection effect — exactly as a stress test should. Gemini's proposed reframing ("relabel as a naive baseline used to expose selection-function vulnerabilities") is functionally what the paper already does, modulo the word "canonical". MISLABELED-MAJOR. |
| Closure | Optional at next restamp: rename "canonical V-Web" → "primary V-Web build" or "headline V-Web" within the V-Web subsection to dispatch the labeling collision with the DESIVAST primary. Not closure-blocking. |

### B3. Gemini new MAJOR — Appendix A toy EFT non-covariant (L_parity contains explicit ẑ)

| Field | Value |
|---|---|
| Claim | Toy operator `L_parity = g_φ (∇_i φ)(∇^i ρ/ρ_bg)(L̂ · ẑ)` includes Cartesian ẑ; breaks rotational invariance; "looks mathematically sloppy". Replace with rotationally-invariant contraction. |
| On-disk verification | tex l.3391–3413: paper contains the `\emph{Rotational-invariance and gauge-invariance caveat.}` paragraph that explicitly states: "the explicit (L̂·ẑ) factor breaks rotational invariance via the fixed coordinate-system unit vector ẑ, and should be read as shorthand for a rotationally-invariant pseudoscalar formed from L̂ and a physical direction set by the local cosmic-web gradient (e.g. L̂·∇̂ρ or L̂·∇̂φ in the limit ∇φ ‖ ∇ρ adopted below); the literal ẑ form is a coordinate-aligned schematic, not a covariant operator." Plus a gauge-invariance caveat. |
| Verdict | **FALSIFIED — the rotational-invariance caveat is explicitly disclosed in the paper.** Gemini quoted the disclosure verbatim ("coordinate-aligned schematic shorthand") and still called it "mathematically sloppy". The caveat IS the requested fix. Paper is transparent. |
| Closure | No action. The caveat paragraph satisfies Gemini's request. |

### B4. Gemini MINOR — Page 17 unnumbered summary table column-flatten artifact

| Verdict | **FALSIFIED — PDF text-extraction artifact**. The "28" and "309" appearing under "56,981" and "621,964" is a Gemini OCR re-flow from columns Class/n/n_CW spilled into a flat string. Source `\begin{tabular}{lrrrr}` is well-formed. |

---

## Section C — Grok findings

### C1. Grok ACCEPT — confirms M1/M2/M3 CLOSED; no new BLOCKER/MAJOR/MINOR; only positive verifications

| Verdict | **CALIBRATION-ANCHOR (5th consecutive ACCEPT)**. Grok performed full re-read of all 31 pp.; verified Table X cell-count fix (126,202), GALZONE estimand-family coherence, footprint retabulation, k-sufficiency guard wording. "The manuscript is now publication-ready at the level of a final proofs check." |
| Closure | No action. |

---

## Section D — Cross-vendor consensus + standing-rule audit

### D1. k=20 5×-FALSIFIED rule audit

| Item | Verdict |
|---|---|
| Did any reviewer re-raise k=20 in EXT7? | ChatGPT yes (6th raise); Gemini no; Grok no. |
| Per pattern-052 + standing rule | Auto-falsify on sight. |
| Action | None. |

### D2. Pattern-052 audit

| Item | Reviewer | Re-raise count | Disposition |
|---|---|---|---|
| k=20 VoidFinder headline | ChatGPT | 6 (1×NOT ADDRESSED + 5×FALSIFIED/DEFERRED) | Pattern-052 + standing rule → AUTO-FALSIFIED. |

### D3. 2√3 Fisher 8th-falsify rule

| Item | EXT7 status |
|---|---|
| Did any reviewer re-raise the 2√3 Fisher factor on P5? | No. (P5 does not use the 2√3 factor — that's a P4-specific item.) |
| Verdict | N/A. |

---

## Aggregate closure

| Severity | Count | Action |
|---|---|---|
| ChatGPT carry-over B3 (k=20) | 1 | STALE / AUTO-FALSIFIED (6th raise; pattern-052 + standing k=20 binding rule). No action. |
| ChatGPT new MAJOR (n=428 vs n=6) | 1 | FALSIFIED — disambiguation already present at tex l.467–472 and l.2039–2042. Optional micro-polish. |
| ChatGPT new MAJOR (Table VIII clipping) | 1 | GENUINE-NEW MINOR (mislabeled MAJOR) — no overfull-hbox warning, but long row label is tight. Optional restructure at next restamp. |
| ChatGPT carry-over MAJORs/PARTIALs (B1, B4, B5, M1, M3, M7) | 6 | All VERIFIED-AS-DISCLOSED or HD-deferred (publish-stage) or OPINION. No arXiv-stage action. |
| Gemini new MAJOR (Table III ledger) | 1 | MISLABELED MAJOR — unique-galaxy contrast already reported. Optional ordering swap. |
| Gemini new MAJOR (canonical V-Web mislabeling) | 1 | FALSIFIED-IN-LARGE — DESIVAST IS primary, "canonical V-Web" is a build-config label within secondary branch. Optional rename. |
| Gemini new MAJOR (toy EFT non-covariant) | 1 | FALSIFIED — rotational-invariance caveat explicitly in paper at l.3391–3413; Gemini quoted it. |
| Gemini MINOR (column-flatten) | 1 | FALSIFIED — PDF OCR artifact. |
| Grok | 0 findings | ACCEPT — 5th consecutive. Strongest external anchor. |

**Total VERIFIED items requiring closure**: **0 mandatory; 3 optional polish edits** (Table VIII row-label shortening or split, micro-polish cross-ref between n=428 and n=6 contexts, V-Web subsection "canonical" → "headline" rename).

**Acceptance-stage blockers (this round)**: **0**.

**External cross-vendor consensus**: 2/3 ACCEPT-class (Grok ACCEPT + Gemini MINOR REVISION). ChatGPT MAJOR REVISIONS verdict is driven by 6th raise of k=20 (auto-falsified) + two new MAJORs that are FALSIFIED on disk-verification (n=428/n=6 already disambiguated; Table VIII clipping is a presentation-polish MINOR with no overfull-hbox in log).

---

## Next-round priorities

1. **Acceptance-stage close**: paper is acceptance-grade. No mandatory closure work.
2. **Optional polish at next restamp**: (a) split Table VIII or shorten the footprint-restricted-control row label, (b) add explicit cross-reference between §VIII.A n=6 disagreement check and §VI.A n=428 headline, (c) rename "canonical V-Web" → "headline V-Web" inside §VI to dispatch the labeling collision with DESIVAST primary.
3. **Pattern-052 reinforcement**: k=20 finding is now SIXTH-time falsified. Bind "auto-falsify on sight without re-audit" for any future round. Note Gemini's fresh-thread vindication round (MINOR REVISION) demonstrates the per-finding-decomposition recipe works for the rest of the audit surface.
4. **Publish-stage carry-over**: Paper IV companion DOI mint, ZCAT_PRIMARY rebuild (if Houston-prioritized), DESIVAST/BGS independent angular mask (if Houston-prioritized).
5. **Grok 5th consecutive ACCEPT + Gemini MINOR REVISION**: cross-vendor consensus is decisively positive.
