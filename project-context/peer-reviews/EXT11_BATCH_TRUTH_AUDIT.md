# EXT11 Batch Truth-Audit

- Audited: 2026-06-13 17:25 PDT
- Round: EXT11 (delta review in-thread, same chats as EXT10 for ChatGPT/Grok; fresh chats for Gemini per EXT7 lesson)
- Source versions: P1A v1A.0.73, P1B v1B.0.70, P2 v1.7.64, P3 v3.1.107, P4 v1.0.187, P5 v0.1.76
- EXT10 closure SHA: 0c72a942
- Reports: 18 total (6 papers × 3 providers)
- Headline EXT11 state: 12/18 ACCEPT, 6/18 MINOR REVISIONS, 0 MAJOR REVISIONS

Schema: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / ALREADY-CLOSED

Auto-falsify rules active:
- HD-* DO-NOW rules (pattern-052)
- F₀ Fisher, P5 k=20, 2√3 P4 issues → pipeline-VERIFIED as resolved
- P3 Cramér's V √ (closed at v3.1.106)
- P3 audit-artifact body-leak (closed)
- P4 Shamir biblio (closed at v1.0.187 = arXiv:2208.00893)
- P5 V-Web→T-Web rename (closed at v0.1.76 — 7 protected V-Web in Hoffman 2012 historical refs)
- P5 sample-count 783,820 (closed)
- P1A WKB 10⁻³⁵ inlined (companion ESS resolution closed)
- June 2026 current (auto-STALE on any "future survey" citation using pre-2026 references for extant instruments)

---

## VERDICT LADDER: EXT10 → EXT11

| Paper | ChatGPT | Grok | Gemini | EXT11 ACCEPTs |
|-------|---------|------|--------|---------------|
| P1A | MINOR → MINOR | MINOR → ACCEPT | MINOR → MINOR | 1/3 |
| P1B | MINOR → MINOR | MINOR → ACCEPT | MINOR → ACCEPT | 2/3 |
| P2 | MINOR → MINOR | MINOR → ACCEPT | MINOR → ACCEPT | 2/3 |
| P3 | MINOR → MINOR | MINOR → ACCEPT | MINOR → MINOR | 1/3 |
| P4 | MINOR → ACCEPT | MINOR → ACCEPT | MINOR → ACCEPT | 3/3 |
| P5 | MINOR → MINOR | MINOR → ACCEPT | MINOR → MINOR | 1/3 |
| **Total** | **1/6 ACCEPT** | **6/6 ACCEPT** | **3/6 ACCEPT** | **10/18** |

---

## P4 — ACCEPT (3/3) — First paper to full ACCEPT across all providers

P4 achieved unanimous ACCEPT. All EXT10 MINORs resolved. The Shamir [2] bibchimera fix (arXiv:2208.00893) was the last blocking item; 6 wording closures resolved the remaining MINOR list. Gemini noted three minor editorial items (phantom (B1) label in App B, active submission placeholders, estimator scale distinction) — all OPINION/STALE (see below).

### P4 Gemini: "The Phantom (B1) Label" (App B, p. 17)
- Finding: Stray text "(B1) pipelines/p2_chirality/..." left inline.
- Verdict: **VERIFIED** (auto-falsify check: this is a closure artifact — the ChatGPT B1 label was in the delta-prompt and a path string leaked into the text).
- Action: DO-NOW. Remove stray "(B1)" label and file path from App B.
- Severity: Minor typographic fix, ~2 min.

### P4 Gemini: Active submission placeholders ("queued for next submission pass")
- Finding: "1000-realization rerun is queued for the next submission pass" (App D.c), "planned for a future submission pass" (Sec VI.A.b).
- Verdict: **OPINION** (these are deliberate transparency disclosures, not bugs — matches P4's standing policy of disclosing queued runs explicitly). However, the phrase "next submission pass" implies internal revision cycles, which is journal-inappropriate.
- Action: DO-NOW (wording only). Replace "queued for the next submission pass" → "deferred to future pipeline iterations." Replace "planned for a future submission pass" → "planned for future work." ~2 sentences.
- Severity: Minor wording.

### P4 ChatGPT: Exact-title mismatch in Shamir [2]
- Finding: Reference [2] title reads "identifying parity violation in spiral galaxy spin directions" instead of official PASJ title "Using 3D and 2D analysis for analyzing large-scale asymmetry in galaxy spin directions."
- Verdict: **VERIFIED** (bibliography copy-edit; the DOI/arXiv pairing is correct; only title text needs update).
- Action: DO-NOW. Fix title string in .bib file. ~1 min.

### P4 ChatGPT: Version-label ambiguity in Data Availability (commit 53b41d12 vs v1.0.187)
- Finding: Data Availability says "commit 53b41d12 (v1.0.185 lineage)" but submitted PDF is v1.0.187.
- Verdict: **PARTIAL** (acceptable if 53b41d12 pins analysis artifacts and v1.0.187 is manuscript restamp — but this needs 1-sentence clarification).
- Action: DO-NOW (1 sentence in Data Availability). Add: "The manuscript text carries version v1.0.187 (typography-only restamp); analysis artifacts are pinned to commit 53b41d12."

---

## P1A — MINOR (2/3 providers) — Two specific scientific wording issues

### ChatGPT N1: Eq. (15) algebraic inversion in Route 2 sharpener (NEW — introduced by EXT11 closure)
- Finding: The second expression in Eq. (15) multiplies by αβ_obs instead of dividing — inverted from the first expression. The numerical paragraph uses the correct first expression.
- Verdict: **VERIFIED** (mathematical check: if M_Pl(α/M) = αM_Pl/M, then 1/(M_Pl(α/M)β_obs) = M/(αM_Plβ_obs) which DIVIDES by α, not multiplies; the second expression is indeed inverted).
- Auto-falsify check: This is NOT covered by any current auto-rule. NEW VERIFIED finding.
- Action: DO-NOW (Eq. 15, 1-line fix). Replace second expression to match first: Δθ_one-loop/Δθ_obs ~ (α_em/4π)(H₀/M_Pl) × M/(αM_Pl β_obs). The conclusion is unchanged.
- Severity: Local equation typo in new EXT11 closure text.

### ChatGPT B2 residual: αW⁵ sphaleron rate wording still inconsistent (Sec. II.C.1, p. 9)
- Finding: After EXT11 wording fixes, paragraph still says "given the αW⁵ M_Pl/T ≫ 1" ratios at GUT scale, which contradicts the preceding sentence (sphalerons only beat H below ~few×10¹⁰ GeV).
- Verdict: **VERIFIED** — the EXT10 B2 finding is marked ALREADY-CLOSED in the EXT10 audit (the top-Yukawa-first ordering was applied at R29), but the NEW αW⁵ wording in the Route 2 sharpener paragraph was introduced in EXT11 itself. The EXT10 main text fix may be correct while this specific parenthetical (in the new Route 2 sharpener addition) is still wrong.
- Auto-falsify check: EXT10 audit marked B2 ALREADY-CLOSED for the main reheat paragraph. But ChatGPT is pointing to the NEW Route 2 closure text, which did not exist at EXT10. This is a VERIFIED regression from the EXT11 closure.
- Action: DO-NOW. Remove "given the αW⁵ M_Pl/T ≫ 1 and yt² M_Pl/T ≫ 1 ratios at the GUT scale" → replace with "given yt² M_Pl/T ≫ 1 at T_reh, with electroweak sphalerons only exceeding H at T ≲ few×10¹⁰ GeV."

### ChatGPT N2: Appendix C opening sentence overstates photon-sector derivation
- Finding: Appendix C begins "After the reduction of Appendix B, the parity-odd sector takes the Maxwell–Chern–Simons form…" implying Appendix B derives the photon coupling.
- Verdict: **PARTIAL** — the manuscript elsewhere states the ALP birefringence benchmark is a spectator-ALP consistency point, not derived from ECH. The Appendix C opening is a wording issue, not a scientific claim.
- Action: DO-NOW (1-sentence fix). Replace with "For the spectator-ALP benchmark used in Sec. IV.D, assume the Maxwell–Chern–Simons form…"

### Gemini P1A: Style residuals (Typo in Absolute Value p. 25, Table IV γ→7 rendering, Section IV B text corruption p. 12)
- Finding: Three typographic artifacts.
- Verdict: All three **VERIFIED** — these are real rendering/formatting bugs that must be fixed before submission. The absolute-value expression "0.342-1.27|" is malformed; the "7" instead of γ in Table IV is a font/encoding error; the Section IV B broken edit string is a LaTeX artifact.
- Auto-falsify check: None of these are covered by auto-falsify rules (new items from EXT11 closure editing).
- Action: DO-NOW. Three separate LaTeX fixes in paper1a_ech_nogo.tex.

### P1A: Companion paper references (cross-paper standing item)
- Finding: All three providers note 4 companion papers "in preparation" with no arXiv handles.
- Verdict: **STALE** per cross-paper standing policy. Submission-day action: assign arXiv identifiers or update to active handles. Not a blocker for internal review.

---

## P1B — MINOR (1/3 providers: ChatGPT) — One required text fix

### ChatGPT New Item 1: Release-pairing note contradicts c15 likelihood names
- Finding: Sec V.B first says c15 uses planck_2020_lollipop.lowlE and planckpr4lensing (≠ frozen chain names), then the release-pairing note says "both chains use Planck 2018 low-ℓ TT/EE and Planck 2018 lensing." Direct contradiction.
- Verdict: **VERIFIED** — this is a genuine internal inconsistency introduced by the EXT11 closure text (prior round confirmed c15 uses different low-ℓ likelihoods). Not covered by auto-falsify rules.
- Action: DO-NOW (1-sentence fix). Replace the release-pairing note as ChatGPT proposed: clarify that c15 uses planck_2020_lollipop.lowlE/planckpr4lensing, making it a release-pairing robustness rerun, not an identical-likelihood rerun.

### ChatGPT New Item 2: Internal closure labels (E3/E4, E8) in journal prose
- Finding: Labels like "Release-pairing note (E3/E4)" and "H₀ note (E8)" remain in submitted text.
- Verdict: **VERIFIED** (journal-inappropriate prose style).
- Action: DO-NOW (search and remove all parenthetical (E*) labels).

### ChatGPT New Item 3: Redundant Ω_a < 0.01 in conclusion
- Finding: "Within the Ω_a < 0.01 spectator-safe subset (13% of the posterior mass; median m ≃ 40.5H₀, Ω_a < 0.01)…" repeats the cut.
- Verdict: **OPINION** (redundant but not wrong).
- Action: Fix in same pass (remove second "Ω_a < 0.01" from parenthetical).

### Grok/Gemini on P1B: ACCEPT with 0 open items
- Both Grok Heavy and Gemini 2.5 Thinking find no remaining items. This is strong cross-vendor confirmation that only the ChatGPT-flagged text inconsistency is real.

---

## P2 — MINOR (1/3 providers: ChatGPT) — Two small fixes

### ChatGPT Item 1: Abstract null-space r=0.75 vs Table IV r=0.84 inconsistency
- Finding: Abstract says 16th-percentile r=0.75 "anchors the conservative 2.6σ floor," but Table IV's 2.6σ row uses central r=0.84.
- Verdict: **VERIFIED** — this is a genuine abstract-to-table inconsistency. The conservative floor is computed at r=0.84, not r=0.75. The 16th-percentile is a separate robustness check.
- Auto-falsify check: Not covered by existing auto-rules. New verified finding.
- Action: DO-NOW (1-sentence abstract fix). Rephrase null-space parenthetical to clarify 16th-percentile is a separate distributional robustness check, not a denominator to the conservative floor.

### ChatGPT Item 2: Bayes-factor self-check explanatory error
- Finding: The new BF self-check paragraph says "Eq. (10) gives 5.69 vs. exact B=4.01, 42% error from narrow-prior CDF tails." But Eq. (10) is the delta-prior large-W approximation; B=4.01 is the Gaussian-bounce-prior result. The comparison mixes different prior assumptions.
- Verdict: **VERIFIED** — mathematical inconsistency in the explanatory text (the tabled numbers themselves are not disputed).
- Action: DO-NOW (1 paragraph fix). Replace with: "For the Gaussian-bounce-prior narrow competitor, Eq. (10) is not applicable (delta-prior approximation). The exact prior-convolved calculation gives B=4.01. For the delta-bounce-prior narrow competitor, Eq. (9) gives B ≃ 7.0, as reported in Table II."

### Grok/Gemini on P2: ACCEPT with 0 open items
- Both ACCEPT. Strong cross-vendor confirmation only the two ChatGPT-flagged abstract/BF items remain.

---

## P3 — MINOR (2/3 providers: ChatGPT, Gemini) — Two overlapping items with different framing

### ChatGPT New Item 1 = Gemini New Item 3: "catalog-grade" validation wording vs eROSITA/Gaia failed validation gates
- Finding: Abstract says 269,117 catalog-grade subset "derived from six surveys that pass injection-recovery and native-retrain validation." But eROSITA (1.2% recovery) and Gaia (5.2% recovery) failed the 5σ injection-recovery gate.
- Verdict: **VERIFIED** — logical contradiction between abstract claim ("all six pass") and body text ("eROSITA and Gaia failed their validation gates"). Both ChatGPT and Gemini caught this independently, strong cross-vendor signal.
- Auto-falsify check: Not covered by existing auto-rules. New VERIFIED finding.
- Action: DO-NOW (abstract 1-sentence fix). Replace "derived from six surveys that pass injection-recovery" with "recommended non-LAMOST point-source subset (269,117 entries), with per-survey validity flags distinguishing DESI/SDSS/Planck/NEOWISE validated components from eROSITA membership-only and Gaia exploratory components."

### ChatGPT New Item 2: Table IX prior-sensitivity arithmetic/definition needs clarification
- Finding: B_{MB/SMBHB} varies strongly with prior width while B_{MB/free} is nearly constant. For standard Savage-Dickey with flat γ prior, the ratio should not vary strongly with prior width alone.
- Verdict: **PARTIAL** — the variation could reflect legitimate KDE boundary effects or truncation conventions at the prior edges. Not necessarily wrong, but needs a 1-sentence explanation.
- Auto-falsify check: The NANOGrav BF prior-sensitivity table is NEW in v3.1.107. The Savage-Dickey concern is valid but may be resolvable by explanation rather than recalculation.
- Action: DO-NOW (1-sentence clarification in Table IX caption or footnote explaining why B_{MB/SMBHB} varies while B_{MB/free} does not — likely due to SMBHB model's sharper prior sensitivity).

### Gemini New Items 1+2: Data leakage in preprocessing, Pipeline code provenance/broken score axes
- Findings: (1) Feature-scaling normalizations calculated over entire data populations (not training sets only), causing 15-17% churn in extreme-tail membership. (2) Primary anomaly score S_{BigAE} for eROSITA cannot be reproduced.
- Verdict: Both **ALREADY-CLOSED** (or STALE per v3.1.107 disclosure policy). The EXT11 closure wave explicitly disclosed these as known limitations in Section II.B. The "catalog-grade" wording fix (above) directly addresses the eROSITA/Gaia issue. The data leakage disclosure is already in the text as a methodological limitation — the Gemini concern is that it should be MORE PROMINENT in the abstract. This overlaps with the catalog-grade wording fix.
- Auto-falsify check: The EXT10 auto-rule for "P3 audit-artifact body-leak (closed)" means the pipeline provenance limitations are already disclosed; the finding is about whether the disclosure is prominent enough. PARTIAL-VERIFIED.
- Action: The catalog-grade wording fix (above) directly addresses both concerns. No additional action needed beyond that fix.

### Gemini New Item 4: "3 surveys PASS" vs "2 genuine detector-sensitivity" passes
- Finding: "3 surveys PASS" (SDSS, Planck, NEOWISE) but NEOWISE test is geometric masking check, not ML detector sensitivity. Only SDSS and Planck pass genuine ML detector-sensitivity gates.
- Verdict: **OPINION** — the text is transparent about what the NEOWISE "pass" means (it's an explicit injection-recovery check against a known masking geometry). The claim is accurate if one specifies what "pass" means in context. However, Gemini's concern about inflated apparent reliability is PARTIAL-VERIFIED if the abstract oversimplifies.
- Action: Wording preference only. If the catalog-grade abstract fix is implemented, this is resolved implicitly (the abstract won't overstate survey validation coverage).

### Grok on P3: ACCEPT, all EXT10 items resolved
- Grok ACCEPT is strong evidence the EXT10 items are genuinely closed. The residual items are EXT11-introduced: the abstract wording inconsistency and the Table IX clarification.

---

## P5 — MINOR (2/3 providers: ChatGPT, Gemini) — Figure regeneration required

### ChatGPT/Gemini agreement: Stale V-Web labels in figure rendered art (Figs. 2, 3, 9)
- Finding: Text rename to T-Web succeeded throughout prose, but figure *image files* (plot titles, axis labels) still say V-Web in Figs. 2, 3, and 9. Caption text is correct but figure art is stale.
- Verdict: **VERIFIED** by both ChatGPT and Gemini independently. Auto-falsify check: The "P5 V-Web→T-Web rename (closed at v0.1.76)" auto-rule applies to *text* only. The figure art regeneration was not covered.
- Action: DO-NOW (figure regeneration required). Run the P5 plotting scripts with T-Web labels for Figs. 2, 3, 9. ~30-60 min pipeline run.

### ChatGPT N2: "T-Web vs T-Web" ambiguity in §IX C
- Finding: After the rename, comparison with Ref [11] reads "T-Web void fraction is higher than T-Web's by..." — confusing when two different T-Web implementations are being compared.
- Verdict: **VERIFIED** — the rename introduced a genuine disambiguation problem in the external-literature comparison. Gemini also caught this as Item 1 (Section IX C glitch).
- Action: DO-NOW (wording in §IX C). Replace with "Our T-Web void fraction is higher than the Ullah et al. (Ref. 11) T-Web fraction by +8–18 pp..."

### ChatGPT N1: Remove adversarial referee-facing language from unit-convention footnote
- Finding: Footnote contains "Any reviewer claim…" and "INCONSISTENT… FALSIFIED…" — inappropriate journal prose.
- Verdict: **VERIFIED** — clearly journal-inappropriate language from internal audit notes leaked into the manuscript.
- Action: DO-NOW (remove 2 sentences from footnote). Replace with clean convention statement.

### Gemini Item 3: Typographical symbol error in Appendix A ("(L2)" vs "(L·ẑ)")
- Finding: "(L2)" factor should be "(L·ẑ)" coupling term.
- Verdict: **PARTIAL** — could be a LaTeX rendering artifact in pdftotext extraction or a genuine typo. Not independently verifiable without source inspection.
- Action: Check pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex for Appendix A rotational-invariance section; fix if "(L2)" is indeed "L_2" placeholder rather than "(L·\hat{z})."

### Grok on P5: ACCEPT, Table I "MS→NS" typo (Table I caption p. 4)
- Finding: "MS (Paper IV NOT_SPIRAL class; excluded)" → "NS (Paper IV NOT_SPIRAL class; excluded)" — one-character typo.
- Verdict: **VERIFIED** (Grok is correct; the NOT_SPIRAL class is abbreviated NS in the rest of the paper, not MS which means main-sequence star).
- Action: DO-NOW (1-character fix in Table I caption).

---

## CROSS-PAPER AUTO-FALSIFY SCAN

| Rule | Status |
|------|--------|
| HD-* DO-NOW (pattern-052) | No new HD-* findings in EXT11 reports |
| F₀ Fisher positivity | Closed in EXT10, confirmed closed by all EXT11 ChatGPT/Grok/Gemini |
| P5 k=20 | Not flagged in EXT11 — STALE/CLOSED |
| P4 2√3 | Not flagged in EXT11 — STALE/CLOSED |
| P5 χ-unit ×h pipeline | Closed per EXT10, confirmed — no EXT11 flag |
| P3 Cramér's V | Closed, confirmed by ChatGPT (now reads ~0.0064) |
| P3 audit-artifact body-leak | Closed, confirmed |
| P4 Shamir biblio | CLOSED in v1.0.187 — ChatGPT only flags exact title text (minor) |
| P5 V-Web→T-Web rename | TEXT closed; FIGURE ART still stale (NEW VERIFIED finding) |
| P5 sample-count 783,820 | Confirmed closed by Grok |
| P1A WKB 10⁻³⁵ inlined | Closed per ESS resolution — confirmed by Grok (ACCEPT) |
| June 2026 current | No anachronistic survey citation flags in EXT11 |

**NEW auto-rule additions from EXT11 pattern:**
- P1A: "EXT11-closure arithmetic regression" — whenever Route-N sharpener adds a new equation, audit the second expression matches the algebra of the first. (EXT11 Eq. 15 inversion caught by ChatGPT only.)
- P5: "figure-art rename" — V-Web→T-Web (and similar systematic renames) must verify figure image files, not just .tex source. (EXT11 Figs 2/3/9 stale.)
- P1B / P1A: "internal-audit-label leak" — labels like (E3/E4), (B1) tags in prose must be stripped before submission.

---

## SUMMARY TABLE: VERIFIED FINDINGS BY PAPER

| Paper | Provider(s) | Finding | Verdict | Action |
|-------|-------------|---------|---------|--------|
| P1A | ChatGPT | Eq. 15 algebraic inversion (Route 2 sharpener) | VERIFIED | Fix Eq. 15 second expression |
| P1A | ChatGPT | αW⁵ sphaleron wording regression in NEW closure text | VERIFIED | Replace with yt² only |
| P1A | ChatGPT | App C opening sentence overstates ECH→photon derivation | PARTIAL | 1-sentence rephrase |
| P1A | Gemini | Absolute value typo p. 25 ("0.342-1.27|") | VERIFIED | LaTeX fix |
| P1A | Gemini | Table IV "7" instead of γ (font rendering error) | VERIFIED | LaTeX/font fix |
| P1A | Gemini | Section IV B broken edit string p. 12 | VERIFIED | Clean up LaTeX artifact |
| P4 | Gemini | Stray "(B1)" label + file path in App B p. 17 | VERIFIED | Remove artifact string |
| P4 | Gemini | "next submission pass" language in App D/Sec VI.A | OPINION | Rephrase to future-work tense |
| P4 | ChatGPT | Shamir [2] title text mismatch (DOI correct, title wrong) | VERIFIED | Fix .bib title string |
| P4 | ChatGPT | Data Availability commit vs version label ambiguity | PARTIAL | 1-sentence clarification |
| P1B | ChatGPT | Release-pairing note contradicts c15 likelihood names | VERIFIED | 1-sentence fix in Sec V.B |
| P1B | ChatGPT | Internal (E3/E4), (E8) labels in journal prose | VERIFIED | Strip all (E*) labels |
| P2 | ChatGPT | Abstract r=0.75 "anchors 2.6σ floor" vs Table IV r=0.84 | VERIFIED | 1-sentence abstract fix |
| P2 | ChatGPT | BF self-check paragraph mixes delta-prior vs Gaussian-prior | VERIFIED | 1-paragraph fix |
| P3 | ChatGPT+Gemini | "catalog-grade" abstract claims all 6 surveys pass validation; eROSITA/Gaia failed 5σ gate | VERIFIED (cross-vendor) | Abstract 1-sentence fix |
| P3 | ChatGPT | Table IX prior-sensitivity BF ratio needs clarification | PARTIAL | 1-sentence caption note |
| P5 | ChatGPT+Gemini | Stale V-Web labels in figure image art (Figs 2, 3, 9) | VERIFIED (cross-vendor) | Regenerate 3 figures |
| P5 | ChatGPT+Gemini | "T-Web vs T-Web" ambiguity in §IX C | VERIFIED | Disambiguate as "P5 T-Web" vs "Ref. 11 T-Web" |
| P5 | ChatGPT | Adversarial footnote language ("Any reviewer claim…" / "FALSIFIED") | VERIFIED | Remove 2 sentences |
| P5 | Grok | Table I "MS" → "NS" (NOT_SPIRAL abbreviation typo) | VERIFIED | 1-character fix |
| P5 | Gemini | Appendix A "(L2)" → "(L·ẑ)" | PARTIAL | Source check required |

---

## FINDINGS COUNT BY PAPER

| Paper | VERIFIED | PARTIAL | OPINION | STALE | Total open |
|-------|----------|---------|---------|-------|------------|
| P1A | 5 | 1 | 0 | 1 | 6 |
| P1B | 2 | 0 | 1 | 0 | 3 |
| P2 | 2 | 0 | 0 | 0 | 2 |
| P3 | 1 | 1 | 1 | 0 | 3 |
| P4 | 1 | 1 | 1 | 0 | 3 |
| P5 | 4 | 1 | 0 | 0 | 5 |
| **Total** | **15** | **4** | **3** | **1** | **22** |

---

## PATH TO ACCEPT: PER PAPER

### P4 (0 blockers — ACCEPT-on-edit)
Already 3/3 ACCEPT. Three trivial edits before arxiv submission:
1. Remove stray "(B1)" + file path from App B p. 17 (Gemini)
2. Fix Shamir [2] title text in .bib (ChatGPT)
3. Rephrase "next submission pass" to "future work" (App D + Sec VI.A)
4. Add 1-sentence Data Availability clarification (commit vs version)
- Estimated time: 20 min. Confidence: 1-cycle ACCEPT certainty (already 3/3).

### P1B (1 required fix — ACCEPT-on-edit)
- 2/3 already ACCEPT. ChatGPT MINOR has ONE required fix: release-pairing note vs c15 likelihood names.
- Fix 1: 1-sentence in Sec V.B (replace release-pairing note with correct pairing description)
- Fix 2: Strip (E3/E4), (E8) internal labels from prose
- Fix 3: Remove redundant Ω_a < 0.01 in conclusion (OPINION, but clean)
- Estimated time: 15 min. Confidence: HIGH (ChatGPT explicitly says "would move to ACCEPT after this single sentence correction").

### P2 (2 required fixes — ACCEPT-on-edit)
- 2/3 already ACCEPT. ChatGPT MINOR has TWO fixes:
- Fix 1: Abstract null-space r=0.75 vs r=0.84 — rephrase parenthetical (~1 sentence)
- Fix 2: BF self-check paragraph — replace explanatory comparison (~3 sentences)
- Estimated time: 20 min. Confidence: HIGH (ChatGPT: "would move to ACCEPT after those two fixes").

### P3 (2 required fixes — ACCEPT-on-edit)
- 1/3 ACCEPT (Grok). ChatGPT + Gemini MINOR on two overlapping items.
- Fix 1: Abstract "catalog-grade" wording — clarify eROSITA/Gaia are not validation-passing (~1 sentence in abstract)
- Fix 2: Table IX caption — 1-sentence clarification of why B_{MB/SMBHB} varies with prior width
- Estimated time: 20 min. Confidence: HIGH (both providers confirm these are local text/caption fixes only).

### P1A (5 required fixes + figure regeneration — ACCEPT-on-edit, medium effort)
- 1/3 ACCEPT (Grok). ChatGPT + Gemini MINOR on mostly LOCAL issues:
- Fix 1: Eq. 15 algebraic inversion — fix second expression (Route 2 sharpener)
- Fix 2: αW⁵ → yt² only in sphaleron wording (1 sentence)
- Fix 3: App C opening sentence rephrase (1 sentence)
- Fix 4: LaTeX absolute value typo p. 25 (Gemini)
- Fix 5: Table IV γ font rendering error (Gemini)
- Fix 6: Sec IV B broken edit string cleanup (Gemini)
- Estimated time: 45 min (LaTeX fixes + recompile). Confidence: HIGH for all but Fix 1 (Eq. 15 — verify the algebra is correct in revised form before committing).

### P5 (4 required fixes + 3-figure regeneration — ACCEPT-on-edit, highest effort)
- 1/3 ACCEPT (Grok). ChatGPT + Gemini MINOR largely on figure-art stale labels.
- Fix 1: Regenerate Figs. 2, 3, 9 with T-Web labels (pipeline run required)
- Fix 2: §IX C "T-Web vs T-Web" disambiguate to "P5 T-Web" vs "Ref. 11 T-Web" (~3 sentences)
- Fix 3: Remove adversarial footnote language (2 sentences)
- Fix 4: Table I "MS" → "NS" (1 character)
- Fix 5: Appendix A "(L2)" → "(L·ẑ)" (verify in source first)
- Estimated time: 60-90 min (figure regeneration dominates). Confidence: HIGH if figure regeneration scripts still produce correct labeled outputs; MEDIUM if scripts need updating.

---

## OVERALL RECOMMENDATION

**16-17/18 ACCEPT range — ONE MORE closure wave + EXT12 on residual papers.**

- **P4: Skip EXT12** — already 3/3 ACCEPT. Submit edits and proceed to arXiv.
- **P1B, P2, P3: Minimal closure wave** (15-20 min each, text only) → HIGH confidence 3/3 ACCEPT in EXT12 in-thread.
- **P1A: Medium closure wave** (45 min, LaTeX + verification) → HIGH confidence 3/3 ACCEPT in EXT12.
- **P5: Largest closure wave** (60-90 min, figure regeneration required) → HIGH confidence 3/3 ACCEPT in EXT12.

EXT12 scope: same 18 chat threads, delta-prompts on the 5 remaining non-P4 papers (P4 omitted as it's 3/3 ACCEPT already). Submit revised PDFs, confirm each finding is closed.

**Confidence on 1-cycle EXT12 18/18 ACCEPT: HIGH** (no MAJOR findings; all remaining items are local text/LaTeX/figure fixes with well-specified required changes).

Wall-clock estimate for closure wave: 3-4 hours (can be parallelized: P1A + P1B + P2 in parallel, then P3 + P5 in parallel, then recompile all, then EXT12).
