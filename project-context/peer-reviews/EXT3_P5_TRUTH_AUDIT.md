# EXT3 P5 Truth Audit — v0.1.64

**Paper:** P5 — Environmental Dependence of Spiral Chirality · v0.1.64-2026-06-11 · 30 pp
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Gemini 3.5 Thinking (MAJOR REVISIONS — held), Grok Heavy (ACCEPT)
**Mode:** EXT3 in-thread DELTA review (closure verification + fresh pass)
**Audit date:** 2026-06-11 · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.64) + `site/public/papers/p5_desi_chirality_v0.1.64.pdf` (extraction spot checks) + EXT2_P5_TRUTH_AUDIT.md

**SAMPLE+ESTIMATOR+NULL baseline:** DESIVAST primary: k=20 VoidFinder n_void=56,981 (exact k-unbounded 57,081) from n_lz=678,945 z≤0.24 matched spirals. V-Web secondary: 812,793 env-labeled rows / 783,820 unique env-matched spirals (791,635 chirality-relevant matched; 7,815 lack env rows; n=811,609 χ² convention). All verdicts identify estimator and null before concluding.

---

## Verdict Table — Fresh Findings (EXT3)

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| NM1 | ChatGPT | MAJOR | Title says the T-Web cross-check is "Across 791,635 DR1 Matched Spirals," but only 783,820 carry an environment row (791,635 − 7,815) | **VERIFIED (genuinely new) → title text HOUSTON-DECISION** | Title l.167 vs abstract l.211–212 ("783,820 unique chirality-relevant matched spirals with an environment row (791,635 minus 7,815 without)"). The cross-check does not operate on all 791,635. Fix options per ChatGPT: "783,820 environment-matched DR1 spirals" or "the 791,635 chirality-relevant DR1 matched sample". |
| NM2 | ChatGPT | MAJOR | Bonferroni-5 primary family is evaluated on one-sample \|σ_void\| (vs 0.5), not the declared void-vs-non-void Δf_CW contrast; Tables VIII–X still lack SE(Δ), z_Δ, p_Δ, CI | **VERIFIED (sharpened re-raise of open EXT2 EF2/EF3)** | l.819–822: "all five return $\|\sigma_{\rm void}\| < 2$ … Treating the five DESIVAST estimators as a Bonferroni-5 family" — the family statistic is the one-sample test. v0.1.63/64 landed only EF1/EF4/EF9/EF5; the EF2 Δ-columns and EF3/EF11 contrasts were left open and are now externally re-flagged. ChatGPT's worked numbers (Δf_CW=+0.0007, SE≈0.00219, z≈0.31, p≈0.76, CI≈[−0.0036,+0.0050]) give the clean primary null. DO-NOW: tabulate Δ statistics and re-anchor the Bonferroni family on them. |
| NM3 | ChatGPT | MAJOR | "Completeness-corrected" V-Web rebuild over-named: it is a BGS-BRIGHT-randoms, 0.01<z<0.50 window stress test, and phrases like "rewrites the environment field wholesale" / "holds under … completeness-corrected environment definitions" can over-read | **PARTIAL (genuinely new, phrasing-level)** | l.2306 ("rewrites the environment field *wholesale*") and l.2320 ("holds under both the survey-selection-shaped and completeness-corrected environment definitions") confirmed; the scope caveat IS present immediately after (l.2322–2326: BGS randoms, z<0.5 window, 99.3% of signal, z>0.5 not probed). Rename to "BGS-randoms-weighted low-z stress test" at the 2 headline sites; keep the caveat. |
| Nm1 | ChatGPT | MINOR | Fig 3 rendered title says n=791,635 while caption/tables use 812,793 rows / 783,820 unique | **PARTIAL** | Same baked-in figure-title staleness family as P3 Fig 2. Caption-side counts are correct in source; the PNG title requires figure regen to fix/verify. |
| Nm2 | ChatGPT | MINOR | §VII.A typo "Pre-cell label-shuffle null" | **VERIFIED** | l.1646 item header reads "\textbf{Pre-cell label-shuffle null.}" while the subsection (l.1583) is "Per-cell significance framework". Genuine typo. |
| Nm3 | ChatGPT | MINOR | §X lists "DESIVAST per-galaxy cross-match, §IX C" — wrong cross-reference (should be §VIII.A) | **VERIFIED** | l.2797–2798: "(i)~DESIVAST per-galaxy cross-match, \S\ref{sec:tweb\_concurrent}" — the \ref points to the concurrent-lit T-Web section; the DESIVAST per-galaxy cross-match is \label{sec:desivast\_xmatch} at l.1753. Real \ref bug. |
| Nm4 | ChatGPT | MINOR | No archival DOI in draft | **HOUSTON-DECISION (ruled)** | Mint-at-submission policy; Appendix B states it explicitly. |
| Nm5 | ChatGPT | MINOR | Conclusion opens with the V-Web null before the DESIVAST primary null | **PARTIAL** | Conclusions (l.3038 ff.) lead with the V-Web class fractions. The paper's own analysis tree declares DESIVAST primary. Reorder is a legitimate consistency polish. |
| Gf1 | Gemini | BLOCKER | §XV conclusions corrupted: "{food, foll, filament f_CW^{ciuster}} = 0.484, 0.503, 0.498, 0.496}" — regex/search-replace mangled the math | **FALSIFIED — extraction artifact** | Source l.3042–3044: `$\{f_{\rm CW}^{\rm void}, f_{\rm CW}^{\rm wall}, f_{\rm CW}^{\rm filament}, f_{\rm CW}^{\rm cluster}\} = \{0.484, 0.503, 0.498, 0.496\}$` — pristine LaTeX. pdftotext of the reviewed PDF contains no "food"/"ciuster"; the only "foll" hits are hyphenated "follow-up". Gemini's own extractor mangled the superscripted math. No corruption exists. |
| Gf2 | Gemini | MAJOR | App A: "For V aligned with the cosmic-web gradient" — ∇φ symbol vanished | **FALSIFIED — extraction artifact** | l.3091: "For $\nabla\phi$ aligned with the cosmic-web gradient $\nabla\rho$" — operator present in source and renders in PDF. |
| Gf3 | Gemini | MAJOR | App A: Lagrangian printed as raw text "Lparity" | **FALSIFIED — extraction artifact** | l.3080: `\(\mathcal{L}_{\rm parity}\supset g_\phi\,(\nabla_i\phi)\,…\)` — proper math mode. Extractor flattening of \mathcal glyphs. |
| Gf4 | Gemini | MINOR | Fig 8 caption double operator "with≥ >200 spirals" | **FALSIFIED — extraction artifact** | l.2263: "with $\geq 200$ spirals" — single operator; pdftotext renders "≥ 200 spirals" cleanly ×3. |
| Gf5 | Gemini | MINOR | §IX.A "agree to < 10^{-6%}" — percent sign inside exponent | **FALSIFIED — extraction/misread** | l.1472: "volume fractions agree to $<\!10^{-6}$" — no percent sign in the source exponent. |
| Gk1 | Grok | MINOR | Abstract: add "(primary analysis path, §VIII)" cross-ref to the DESIVAST n=56,981 parenthetical | **OPINION (useful polish)** | Cross-ref insertion; no error. |
| Gk2 | Grok | MINOR | Table II ASTRA row still reads "env-label concordance" while §X prose says "supporting diagnostic consistency check with EDR overlap-size caveat" | **PARTIAL (accurate)** | l.878: "ASTRA EDR per-object & env-label concordance & --- & descriptive" — row label not updated when the §X prose was demoted at v0.1.63 (EF9). One-cell edit. |
| Gk3 | Grok | MINOR | Table VIII caption still lacks the "(k=20 KDTree yields identical conclusions to 0.18% level)" parenthetical | **PARTIAL (accurate carryover of its own EXT2 EF13)** | Not applied in v0.1.63/64 (changelog covers EF1/EF4/EF9/EF5 only). One-line caption edit. |

## Verdict Table — Contested Closure Claims

| # | Reviewer claim | Audit verdict | Evidence |
|---|----------------|---------------|----------|
| B1 (ChatGPT: PARTIAL — non-void control not restricted to DESIVAST usable footprint; retabulation queued) | **VERIFIED residual — now THRICE-flagged, DO-NOW** | l.2074: "re-tabulation of the HEALPix sky scan is queued for the data [release]". The "0 maximal voids per pixel" proxy + [−2.04,−0.09] bound remain the documentation. This is the single substantive analysis task left on P5: run the footprint-mask retabulation of the non-void control (computable now; do not leave queued for a fourth round). |
| B2 (ChatGPT: CLOSED — DESIVAST counts 1,489/389/297) | **CONFIRMED** | Counts + 1,461/420/295 preliminary ledger note + l.1908–1922 effective-vs-interior void reconciliation in place. |
| B3 (ChatGPT: NOT ADDRESSED — k=20 retained as primary despite exact rerun) | **AUTO-FALSIFIED (THIRD raise of a twice-FALSIFIED finding)** | Per protocol: falsified at EXT1 (F3) and EXT2 (B3) — the exact k-unbounded rerun IS in the paper (n_void=57,081, +0.18%, f_CW=0.4965, σ=−1.69, "every conclusion … is invariant") with the k=20 continuity rationale documented and the k-sufficiency guard paragraph in §VIII.B. Re-raised a third time with no new evidence → auto-FALSIFIED with note. The residual *presentation* choice (which number leads the title/abstract) is at most HOUSTON-DECISION; the claim "not acceptable as published primary statistic" ignores the documented invariance. |
| B4 (ChatGPT: PARTIAL — Paper IV labels load-bearing, external) | **PARTIAL/HOUSTON-DECISION** | Companion-paper dependency + DOI timing are policy items; monopole propagation is explicit in-text. Unchanged ruling. |
| B5 (ChatGPT: PARTIAL — V-Web/T-Web still foregrounded in title/conclusions) | **PARTIAL/HOUSTON-DECISION** | Primary/secondary declaration complete (Table II, abstract ledger). Title composition and conclusion ordering (see Nm5) are framing calls; the conclusion-reorder half is actionable. |
| M1 (ChatGPT: PARTIAL — prose still says "V-Web" for a Hahn T-Web implementation) | **PARTIAL carryover** | Title says T-Web (Hahn 2007) with the nomenclature footnote (l.167); body retains "V-Web" per the documented backward-compatibility choice (HF slug/release tag). Journal-facing rename of body prose = reasonable, bounded edit pass. |
| M3 (ChatGPT: PARTIAL — overlap-free per-class program split unavailable) | **PARTIAL carryover (disclosed-scoping)** | Cramér's V=0.078 + log10 p≈−1069 in place; the row-level overlap limitation is disclosed in-text. |
| M4 (ChatGPT: PARTIAL — Table IX summarized as "no sign" while dark void 0.4584 vs non-void 0.5056 is a nominal ≈1.97σ contrast) | **VERIFIED residual (open EXT2 consensus item EF3/EF11)** | l.1881: "(\|σ\| ≤ 1.80 for all cells), with no sign of a…" + Table IX rows l.1905/1907 carry both cells but the within-program contrast is never co-reported. The EXT2 consensus one-line parenthetical (ChatGPT EF3 + **Grok's own EF11 major**) was NOT applied in v0.1.63/64. Add it: report the dark contrast as nominal ≈2σ small-n noise, pre-multiplicity. |
| M5 (ChatGPT: PARTIAL — §VII.A "headline robustness statistic" / floor "controls the false-positive rate") | **PARTIAL carryover** | Max-stat info and Rs=10 grid-unresolved labels are in place (EXT2); the residual is the two phrases — the empirical max-stat is the FPR control, the range/floor comparison is descriptive. Two-phrase edit. |
| M6 (ChatGPT: PARTIAL — RSD: FoG MC moves n_void 57,081→76,490±161, so membership is not insensitive) | **PARTIAL carryover** | "RSD-bounded rather than strictly immune" language landed; narrowing the conclusion to "Δf_CW is stable under this fixed-void-geometry perturbation" is a correct, bounded sharpening. |
| M7 (ChatGPT: PARTIAL — no ZCAT_PRIMARY rebuild) | **PARTIAL carryover (disclosed-scoping)** | Unique-TARGETID rebuild present; ZCAT_PRIMARY comparison remains the documented open extension. |
| M8 (ChatGPT: CLOSED — ASTRA scoped as supporting diagnostic) | **CONFIRMED** | EF9 applied at v0.1.63 (changelog); §X prose demoted. (Table II row lag = Gk2.) |
| M9 (ChatGPT: PARTIAL — EFT appendix length) | **OPINION (journal style)** | Labeled heuristic/non-covariant; ChatGPT itself calls it "acceptable". |
| ChatGPT v0.1.62-fresh closures (ledger, permutation-null wording, ASTRA, Table II label: all CLOSED) | **CONFIRMED** | EF1/EF4 at v0.1.63, EF5 at v0.1.64 (changelog + l.211–212, l.878-area, Table II row relabel). Accurate closure verification. |
| ChatGPT: "Tables VIII–X Δ statistics NOT ADDRESSED" | **CONFIRMED carryover** | Same as NM2 — EF2 was an EXT2 P1 item, not landed. |
| Gemini closure: Table VII "stochastic row inversion" NOT ADDRESSED | **AUTO-FALSIFIED (2nd raise of EXT2-FALSIFIED EF17)** | EXT2 verdict stands: the LaTeX tabular (six fixed, separately-headed columns) has no stacked/inverted cells; the "inversion" is Gemini's PDF reader mis-parsing column alignment. Re-raised without new evidence → auto-FALSIFIED. |
| Gemini closure: §IX.C notation collision NOT ADDRESSED | **PARTIAL (accurate carryover)** | EXT2 EF18 fix (f^V_class notation) was not applied in v0.1.63/64. Legitimate open P1 item; "Major" severity over-called for a subscript-disambiguation edit. |
| Grok closures M1–M3 CLOSED | **CONFIRMED — but over-credited overall** | The three listed closures check out against the v0.1.63 changelog and source. However "All prior concerns have been fully addressed" is false: Grok's own EXT2 fresh MAJOR (EF11 dark-cell parenthetical) is still unapplied (l.1881), and the open EXT2 P1 batch (EF2 Δ columns, EF14 dagger footnote, EF18 notation) goes unmentioned. Grok dropped its own finding from its closure ledger. |

## Grok ACCEPT — over-crediting check

Grok's named closures are real, and its three minors are well-targeted (two are accurate carryovers of open items, including its own EF13). But ACCEPT + "exceptionally clean" over-credits: it failed to track its own EXT2 MAJOR EF11 (dark void/non-void co-reporting — the exact "apparent cherry-picking" risk it flagged is still in the prose at l.1881), and it did not re-check the EXT2 consensus P1 batch. Calibrated reading = minor revisions with a short, enumerable fix list.

## Consensus

1. **No new blockers from any reviewer.** ChatGPT: "None beyond the unresolved carry-over blockers." Gemini's fresh "blocker" is FALSIFIED. Grok: none.
2. **Gemini's MAJOR-held verdict is 100% unsupported.** All 5 fresh findings (Gf1–Gf5) are extraction artifacts falsified against source AND the rendered PDF; its "severe text-corruption regressions" narrative describes its own PDF extractor. Its closure section re-raises one EXT2-FALSIFIED item and one accurate-but-minor notation carryover. True Gemini posture ≈ ACCEPT-with-one-footnote. This is the third consecutive round in which Gemini P5 findings are dominated by extraction artifacts (EXT2: 5 falsified; EXT3: 5 falsified + 1 re-raise).
3. **ChatGPT's k=20 re-raise is now triple-falsified** — flag in the EXT4 prompt that B3 is closed-with-prejudice (exact rerun in-paper, conclusions invariant) so review bandwidth goes elsewhere.
4. **The real remaining work is a short, twice/thrice-flagged list:** B1 footprint retabulation (compute), Δf_CW SE/CI columns + Bonferroni family re-anchoring (NM2/EF2), dark-cell within-program parenthetical (M4/EF3/EF11 — 2-reviewer EXT2 consensus, still open), §IX.C notation (EF18), Table II/VIII caption lags (Gk2/Gk3).

## Action Plan (VERIFIED/PARTIAL, hardest first)

1. **B1 — DESIVAST footprint-mask retabulation (thrice-flagged)** — execute the queued HEALPix re-tabulation restricting the non-void control to the DESIVAST usable angular/radial footprint; report the retabulated Δf_CW beside the current proxy + [−2.04,−0.09] bound (l.2074 area). Files: `pipelines/p5_desi_chirality/` analysis script + new artifact JSON + §VIII text.
2. **NM2/EF2 — primary-estimand statistics** — add Δf_CW, SE(Δ), z_Δ, p_Δ, 95% CI columns to Tables VIII–X; restate the Bonferroni-5 family on the Δ tests (l.819–822). ChatGPT's worked example (z≈0.31, p≈0.76) verifies the null gets *cleaner*, not weaker.
3. **M4/EF3/EF11 — dark-split co-reporting** — at l.1881: replace the "no sign" summary with the within-program contrasts: "(dark: void f_CW=0.4584 (n=469) vs non-void 0.5056 (n=5,845), a nominal ≈2.0σ contrast before multiplicity, consistent with small-n noise; bright: …)".
4. **NM3 — rename the rebuild** — "BGS-randoms-weighted low-z stress test" at l.2306/l.2320; keep the existing scope caveat.
5. **NM1 — title/abstract count alignment** — title l.167 "Across 791,635" → "Across 783,820 Environment-Matched DR1 Spirals" (or keep 791,635 with "chirality-relevant matched sample" phrasing). HOUSTON-DECISION on final title text; same edit should fix the Fig 3 rendered title (Nm1, figure regen).
6. **Cross-ref + typo batch** — l.2797 \ref{sec:tweb_concurrent} → \ref{sec:desivast_xmatch} (Nm3); l.1646 "Pre-cell" → "Per-cell" (Nm2); Table II ASTRA row label (Gk2, l.878); Table VIII caption k-parenthetical (Gk3); §IX.C f^V_class notation (EF18); conclusion reorder DESIVAST-first (Nm5); M5 two-phrase fix; M6 conclusion-sentence narrowing.

**HOUSTON-DECISION queue:** title text (NM1/B5); k=20-vs-exact lead number (B3 presentation residue only — closed-with-prejudice as a finding); Paper IV companion timing + DOI (ruled, submission-day); body-prose V-Web→T-Web rename scope (M1); EFT appendix length (M9, journal).

---

## GAP METRIC

| Category | Count | Items |
|----------|-------|-------|
| (a) Genuinely new vs EXT2 | **6** (all ChatGPT) | NM1 (title parent count), NM2 (Bonferroni family statistic — sharpened form of open EF2/EF3), NM3 (completeness-rebuild naming), Nm2 ("Pre-cell" typo), Nm3 (§X wrong \ref), Nm5 (conclusion ordering). EXT2 baseline was 10 net-new → **40% shrink**; Gemini and Grok contributed **zero** genuinely-new findings (Grok's Gk1 is polish on a v0.1.63 sentence). |
| (b) Re-raises | **ChatGPT:** B3 k=20 — **3rd raise, auto-FALSIFIED** — plus ~8 accurate PARTIAL carryovers (B1, B4, B5, M1, M3–M7, EF2) · **Gemini:** Table VII inversion — 2nd raise of EXT2-FALSIFIED — plus 1 accurate carryover (EF18) · **Grok:** 1 accurate carryover (EF13) |
| (c) Policy residue | **5** | DOI (ruled); Paper IV companion dependency; title composition (NM1/B5); V-Web naming back-compat scope (M1); EFT appendix length (M9). |
| Reviewer findings FALSIFIED this round | **7** | Gemini Gf1–Gf5 (all 5 fresh findings — extraction artifacts, verified against source and rendered PDF) + Gemini Table VII re-raise + ChatGPT B3 third raise. |

**Internal-loop note:** v0.1.63/64 landed only the EXT2 P0 items (EF1/EF4/EF9/EF5); the P1 consensus batch (EF2, EF3/EF11, EF14, EF18, EF13) was left open and drew 5 external re-flags across all three reviewers — identical failure mode to P4 this round. Land full P0+P1 batches per closure wave. Also: Gemini's P5 stream is now 10-for-12 extraction artifacts across EXT2+EXT3 — weight its P5 layout/typography findings near zero unless confirmed in source, per the standing source-tex-first rule.

## EXIT-CRITERION ASSESSMENT

**Not yet externally clean; the closest of the three papers after artifact removal.** Modulo HOUSTON-DECISION/policy, the substantive residual set is exactly: B1 footprint retabulation (one queued compute job, thrice-flagged), the Δf_CW primary-estimand statistics (NM2/EF2 — arithmetic from existing counts), the dark-split parenthetical (M4), and a one-pass text batch (NM3 rename, Nm2/Nm3 typo+ref, EF18, Gk2/Gk3, Nm5). **No reviewer challenged the headline null itself — Δf_CW=+0.0007 (z≈0.31 by ChatGPT's own arithmetic), the three-algorithm robustness, or the z-shell/completeness invariance.** Grok is at ACCEPT (over-credited on its own dropped EF11); Gemini's MAJOR is fully falsified (≈ACCEPT in substance); ChatGPT's MAJOR reduces to B1 + the NM2 statistics once the triple-falsified k=20 item and Houston-ruled framing are removed. After the wave + B1 retabulation, expected EXT4 surface is policy-only.

---

*Verdict counts (fresh + contested closures): VERIFIED 7 · PARTIAL 13 · OPINION 3 · FALSIFIED 7 · HOUSTON-DECISION 5 · CONFIRMED-CLOSED 8.*
*Protocol: FALSIFIED = claim contradicted by current source/PDF · AUTO-FALSIFIED = re-raise of a previously-FALSIFIED claim without new evidence (B3 = third raise → closed-with-prejudice) · OPINION = editorial preference · HOUSTON-DECISION = framing/process choice with no single correct answer.*
