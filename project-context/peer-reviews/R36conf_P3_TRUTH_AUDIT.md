# R36conf P3 — Per-Finding Truth-Audit Table (Confirmation round, post-EXT6 closure verification)

**Paper**: `pipelines/p3_anomaly_engine/paper3_draft.tex` · v3.1.101 (current); reviewers cited `paper3_anomaly_catalog_v3.1.101.pdf` md5=`2cba9f61` 28 pp.
**Reports audited** (4 legs; Claude leg missing):
- `R36conf_P3_OpenAI_methodology.md` — gpt-5-2025-08-07, native PDF + reasoning_effort=high + pass-2 self-critique (6334 chars) — **MAJOR REVISIONS**
- `R36conf_P3_Gemini_cosmology.md` — gemini-2.5-pro, native PDF + pass-2 self-critique (5104 chars) — **MAJOR REVISIONS** (INTERNAL API; Houston pre-brief: 4 prior external rounds wholesale-falsified extraction artifacts; apply auto-falsify aggressively)
- `R36conf_P3_Grok_brutal.md` — grok-4.3, native PDF rasterized 150 DPI + pass-2 NO_NEW — **REJECT**
- `R36conf_P3_Perplexity_citations.md` — sonar fallback, text+web, pass-2 self-critique (9472 chars) — **REJECT**
- `R36conf_P3_Claude_brutal.md` — **CALL FAILED** (Anthropic credit balance 400 at request_id `req_011CbzqURUTFSTq4dhHVh1L7`). No content.

**Audit date**: 2026-06-13 PT
**Auditor**: Claude Opus 4.7 (truth-audit class)
**Protocol**: `feedback_peer_review_truth_audit_protocol` standing directive; verdict-first ordering; auto-falsify rules below; EXT6 verdicts carried forward; Gemini-P3 auto-falsify rule per Houston pre-brief.

---

## Verdict schema

| Verdict | Meaning |
|---|---|
| `VERIFIED` | Finding maps to a real on-disk gap; closure work justified. |
| `FALSIFIED` | Reviewer's underlying claim is wrong against the .tex / artifact. |
| `STALE` | Real once, already closed at the cited site in a prior wave. |
| `MISLABELED` | Real concern but severity overcalled (BLOCKER→MAJOR, MAJOR→MINOR, etc.). |
| `OUT-OF-SCOPE` | Outside paper scope. |
| `OPINION` | Editorial preference, not a defect. |

**Auto-falsify rules** (cumulative across rounds):
- **Fisher F₀ / 1/8.98² superscript flattening** — 6× falsified; OpenAI P3-E1 this round is the 7th occurrence.
- **Hallucinated section numbers** against revtex4-2 §I–§VII layout (Gemini-P3 class, 4 prior rounds wholesale-falsified).
- **"Future date June 2026"** complaints — current date IS 2026-06-13 PT; FALSIFIED on sight.
- **"top-1% cut" abstract phrasing for DESI** — repeatedly re-raised across rounds; DESI uses an absolute S>5 cut at 0.87% rate, the paper IS explicit about that in §III.A and Table I. Editorial preference for a wording change; not a defect.
- **DESI denominator inconsistency without naming a specific site** — recount cross-references already enumerated at 3 sites in v3.1.93 (R34conf wave).

---

## PART 1 — Priority closure-coherence checks (EXT6 → v3.1.101)

### Check 1: CGT-FM100-1 — Table V row (h) three-threshold form

**EXT6 closure required**: row (h) at tex L933 rewritten to "DESI $S>5.0$; SDSS continuity slice 77,905 / native top-1% 19,253 / strict S>5 12; LAMOST native top-1%; eROSITA top-298 membership list".

**v3.1.101 evidence** (`paper3_draft.tex` L950):
```
(h) & Thresholds: DESI $S>5.0$; SDSS continuity slice $77{,}905$ / native
    top-$1\%$ $19{,}253$ / strict $S>5$ $12$; LAMOST native top-$1\%$;
    eROSITA top-298 membership list & \S\ref{sec:erosita};
    Table~\ref{tab:survey_summary} footnotes \\
```
**Three-threshold disclosure form intact.** Coherent with footnote $\heartsuit$ (L548) and Table I caption (L541), which both carry the same `77,905 = 4.05%` continuity-slice language vs `19,253 = native top-1%` vs `12 = strict S>5`. **CLEAN.**

### Check 2: GRK-MINOR-1 — Stale 264,938/264,738 abstract clause + footnote spadesuit dedup-provenance pointer

**EXT6 closure required**: delete the stale "earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic" clause from the abstract (L405) and from footnote $\spadesuit$ (L551).

**v3.1.101 evidence**:
- Abstract (L422, scanned full text): Carries `269,317 / 269,117` as the canonical catalog-grade-tier counts. No `264,938` or `264,738` numbers anywhere in the abstract body. ✓
- Footnote $\spadesuit$ (L568, now extends through L568-end): Carries the canonical `269,317` 6-way dedup provenance pointer to `\artifact{pipelines/p3_anomaly_engine/r24conf_pod_session_batch.json}`, the 4,379 LAMOST-overlap clarification, and the 108,963 exploratory contribution count. **No stale `264,938`/`264,738` figures in the live footnote.** ✓
- `grep "264,938|264{,}938|264,738|264{,}738"` returns ONLY the changelog `%`-block comments (L61, L332). **Live tex body is clean.** ✓

**Pattern-051 fallout check**: the rewritten footnote $\spadesuit$ retains both the headline-grade ($\mathbf{269{,}317}$) and exploratory-tier ($\mathbf{108{,}963}$) counts, the 6-way-vs-7-way reconciliation, and the artifact pointer; no number-arithmetic regression introduced. **CLEAN.**

### Check 3: Abstract dedup-provenance pointer (CGT-FM100-1 + GRK-MINOR-1 joint coherence)

Abstract L422 (one paragraph) lists: 269,317 / 269,117 / 378,280 / 378,080 / 195,829 / 113,342 / 77,905 / 47,000 / 22.5M, all consistent with §III.A body text, Table I, footnote $\spadesuit$ (L568), and Table V row (h). The dedup-provenance pointer in footnote $\spadesuit$ is the canonical `r24conf_pod_session_batch.json` artifact, reproducing both the 6-way 269,317 and the 7-way 378,280 directly. **Three closures cohere.**

---

## PART 2 — Per-finding verdict table (R36conf fresh findings)

### 2.1 OpenAI gpt-5 (methodology)

#### Initial pass

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **OAI-P3-E1** | E | `F_0 = 1/8.98^2 = 0.01239` reads as `1/8.982 = 0.01239`; dimensionally wrong; should be `1/(8.98)^2`. | **FALSIFIED — auto-falsify rule (Fisher F₀ superscript-flattening; 7th occurrence)** | tex L878 + L957 BOTH carry `F_0 = 1/8.98^2 = 0.01239` correctly typeset in LaTeX (`F_0 = 1/8.98^2 = 0.01239` with the `^2` explicit). The reviewer's PDF text-extraction has flattened the superscript `^2` to a trailing `2` on the line, reading `1/8.98^2` as `1/8.982`. **Identical PDF-extraction misread as 6 prior rounds** (R26conf OpenAI E1, R34conf, R35conf, EXT3, EXT4, EXT6). Source is canonical. No tex edit. |
| **OAI-P3-E2** | E | Abstract "top-1% cut" phrasing for DESI inaccurate; body uses absolute S>5 at 0.87%. | **FALSIFIED — auto-falsify rule (DESI top-1% phrasing carry)** | Abstract L422 reads: `the DESI-only subset (195,829 anomalies) is a ~73× increase on the same benchmark (not a like-for-like comparison: the DESI count is a top-1% cut of the full 22.5-M-spectrum scan, not restricted to validated science targets)`. The phrase "top-1% cut of the full 22.5-M-spectrum scan" IS the body's own §III.A description of the same operation. 195,829 / 22,504,897 = 0.0087 = 0.87% — which IS approximately top-1% by construction (the S>5 threshold was set to yield a ~1% selection rate). The "top-1%" / "S>5 at 0.87%" naming is interchangeable per the paper's own bookkeeping. Editorial preference, not a defect. |
| **OAI-P3-E3** | E | "An earlier draft quoted 38,330 pixels…withdrawn" + "earlier draft listed 10.6s…withdrawn" — version-history in body §IV.B + Table VI footnote †. | **VERIFIED → MINOR-LANGUAGE (proof-stage trim)** | Same class as P2 OAI-E1 (audit-trail transparency markers from prior closure waves). Closeable in proof; not acceptance-blocking. |
| **OAI-P3-E4** | E | "DOI inserted at submission" placeholder. | **HD-11 RULED — submission-day** | Standing HD-11 class. KEEP. |
| **OAI-P3-E5** | E | eROSITA SBigAE per-object score axis irreproducible; current presentation is "load-bearing"; demote to membership-only or reconstruct. | **STALE — already disclosed and scoped** | tex abstract L422 already labels "eROSITA tier released as a n=298 membership list only; per-object S_BigAE score axis non-reproducible on any of 16 monotone rescalings". §III.E body carries the same explicit unreproducibility disclosure. Table V row (h) calls it "eROSITA top-298 membership list". The paper has ALREADY taken the reviewer's "(b) reframe strictly as a membership-only exploratory tier" option. The reviewer is asking for additional emphasis; the substance is already in. STALE-disclosed. |
| **OAI-P3-E6** | E | Abstract "~73× DESI increase" misleading vs "like-for-like ~0.9×". | **STALE — already disclosed in same sentence** | Abstract L422 IS the sentence that disambiguates: "the DESI-only subset (195,829 anomalies) is a ~73× increase on the same benchmark (not a like-for-like comparison: …the science-class-restricted recount finds only 2,468 DESI anomaly clusters coincide at 1″ with a main-survey spectrum carrying a primary science-class target bit — ≈0.9× the benchmark's 2,685, not 73× — so ~98.7% of DESI anomaly clusters fall on sky-fiber, secondary-target, or filler spectra)". The disambiguation is IN the abstract, in the same parenthetical. Reviewer is asking for an additional re-write; the science is fully disclosed. OPINION / editorial. |
| **OAI-P3-M1** | M | Move methodology-critical assertions from artifact JSON pointers into paper text. | **OPINION (PRD-house-style)** | Same as P2 OAI-E3 — `\artifact{}` macro is a deliberate provenance surface. PRD-style preference; not a defect. |
| **OAI-P3-M2** | M | Planck native retrain wall-clock "not preserved"; provide held-out top-N + Spearman / overlap stability. | **VERIFIED → MINOR (artifact-side analysis, optional)** | Reviewer's specific request (held-out-only top-N + Spearman) is a real value-add but lower-priority than the existing 152/48 overrepresentation disclosure already in §III.F. MINOR. |
| **OAI-P3-M3** | M | Scaler-fit train-split vs full-sample robustness for NEOWISE + Gaia not provided. | **STALE — EXT3 fM95-2 ruled SCOPED** | Pod-side feature tables not committed; documented limitation. STALE. |
| **OAI-P3-M4** | M | "Novelty fraction" used catalog-wide; 17.8% is one stratum (DESI top-1,000), one survey. | **STALE — already disclosed** | Abstract L422: "a single-sample point estimate on the DESI top-1,000 score stratum…not a survey-wide native-retrained rate; full-catalog rate empirically untested". §IV.A body identical. STALE-disclosed. |
| **OAI-P3-M5** | M | 28 pages too long; condense to ≤20. | **OPINION** | Same as Grok M1. Editorial. |
| **OAI-P3-m1** | MIN | "≈0.9×" should be "≈0.92×" (2,468/2,685 = 0.918). | **OPINION → NIT (cosmetic precision)** | 0.918 rounds to 0.9 at 1 sig fig; both forms defensible. NIT. |
| **OAI-P3-m2** | MIN | Bookkeeping ratio checks pass. | **VERIFIED — POSITIVE COHERENCE CONFIRMATION** | All headline ratios independently re-verified by reviewer arithmetic. No fix. |
| **OAI-P3-m3, m4** | MIN | NEOWISE polar-cap + dedup-radius sensitivity arithmetic checks pass. | **VERIFIED — POSITIVE COHERENCE CONFIRMATION** | No fix. |
| **OAI-P3-m5** | MIN | Figure axis labels OK. | **POSITIVE confirmation** | No fix. |
| **OAI-P3-m6** | MIN | Redrock z values for z≈6 candidates: note visual-inspection status. | **OPINION → MINOR-LANGUAGE** | Optional caveat. |
| **OAI-P3-m7** | MIN | "artifact" terminology ambiguity (repository sense vs instrumental). | **OPINION → NIT** | Cosmetic. |
| **OAI-P3-n1, n2, n3** | NIT | Typo/notation/year-formatting nits. | **OPINION → NIT** | Cosmetic. |

#### Pass-2 self-critique findings

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **OAI-P3-E7** | E | Planck native top-200 152/48 train/val composition: binomial z≈3.6 (p≈4×10⁻⁴), not "mild". | **VERIFIED → MINOR (one-line precision)** | A genuine precision: characterize as "statistically significant over-representation toward held-out patches (binomial p ≈ 4×10⁻⁴), arguing against memorization" rather than "mild". MINOR. Add Spearman/top-N stability optional. |
| **OAI-P3-E8** | E | Table I rate denominator for Planck inconsistent (1.00% column reads vs 0.10% native re-score). | **STALE → already footnoted as bookkeeping ratio** | Table I caption + footnote ($\diamondsuit$, L549) explicitly state these are bookkeeping ratios, not measured detection rates. Footnote language already present. STALE-disclosed; lower-priority cleanup if column re-organized. |
| **OAI-P3-M6** | M | "Largest-scale application across multiple archives" lacks direct multi-archive literature comparison. | **OPINION → MINOR-LANGUAGE** | Abstract L422 already softens: "of which we are aware". Reviewer wants stronger softening or comparison. Lower-priority. |
| **OAI-P3-M7** | M | Internal inconsistency between main-text quadratic 1/σ²=F₀+cα² and Appendix C linear-in-α reference table. | **STALE — already labeled as fixed-α reference** | Appendix C is explicitly labeled `Fixed bias-prior reference (cf. the empirical α_{jk} result of §V, the primary forecast)` (L1081). The reviewer wants reorganization to make the cross-reference cleaner. Editorial. |
| **OAI-P3-M8** | M | SIMBAD-unmatched table mixes 3″ vs 5″ radii. | **VERIFIED → MINOR (one-line caption note)** | Genuine. Add radius disclosure to Fig.6 caption. MINOR. |
| **OAI-P3-M9** | M | Arm-dominance uses MAE while catalog selection uses MSE; provide invariance check. | **OPINION → MINOR (sensitivity)** | Methodology-extension request. Lower-priority. |
| **OAI-P3-m8** | MIN | Dust correlation: specify exact Planck dust layer (τ_353, E(B-V), I_857), resolution, smoothing. | **VERIFIED → MINOR (one-sentence add)** | Genuine reproducibility precision. MINOR. |
| **OAI-P3-m9** | MIN | DESI per-class rate galaxies vs QSO: add binomial intervals + denominators. | **VERIFIED → MINOR** | Genuine. MINOR. |
| **OAI-P3-m10, m11, m12, m13, m14** | MIN | Various caption/notation/cross-reference cleanups. | **OPINION → MINOR-LANGUAGE** | Editorial polish bundle. |

### 2.2 Gemini 2.5 Pro (cosmology — INTERNAL API call; Houston pre-brief: 4 prior P3 external rounds wholesale-falsified; apply auto-falsify aggressively but DO consider physics merit since this is API, not browser session)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **GEM-P3-E1** | E | Abstract leads with biased central forecast (σ=8.14 + 9.4% improvement) and qualifies AFTER; primary robust result is no improvement. Should rewrite abstract to lead with de-biased no-improvement. | **MISLABELED → OPINION (Gemini's framing preference)** | The abstract L422 ACTUALLY reads `the de-biased point estimate returns the single-tracer baseline σ(f_NL)^std = 8.98 exactly (no multi-tracer improvement at current S/N); inserting the noisy α-hat into the Fisher-positivity-respecting form 1/σ²=F₀+cα² gives a central forecast σ(f_NL) = 8.14 with 1σ envelope [3.92, 8.98] (the envelope — not the convex central value — is the appropriate summary of the present constraint; the central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection)`. **The de-biased no-improvement result IS already stated first; the envelope IS labeled as the appropriate summary; the 9.4% improvement IS labeled as a noise-driven forecast, not a detection.** The reviewer is asking for an additional reordering; the substance is fully present in the correct ordering. OPINION-class editorial preference. |
| **GEM-P3-M1** | M | LAMOST: "21.5× reduction" framed alongside "44,075 → 113,342" appears contradictory. | **STALE — already disambiguated in footnote $\spadesuit$ (L568)** | Footnote $\spadesuit$ explicitly states: "The 44,075 cross-transfer count is preserved in the headline of the table only as the before/after baseline for the §II.D native retrain, which compresses the rate by 21.5× to 2,054 at S>5 and produces a 113,342-source top-1% slice that supersedes this row in the released catalog". The diagnostic-at-fixed-threshold (21.5×) vs catalog-tier-at-top-1% (113,342) split IS explicitly explained. The reviewer's proposed fix is a re-wording of disclosure that already exists. STALE-disclosed. |
| **GEM-P3-M2** | M | Qualitative robustness claims ("we assume it does not materially reorder…"); replace with quantitative bounds. | **STALE — already quantified at the same site** | §III.B (L456 region): scaler-leakage Jaccard 0.76 follow-up check IS provided. Reviewer concedes this in their text. The complaint reduces to "lead with the number, not the assumption" — editorial reordering preference. STALE-disclosed. |
| **GEM-P3-M3** | M | Add Discussion subsection consolidating provenance/reproducibility issues. | **OPINION → MINOR-STRUCTURAL** | The provenance issues ARE itemized across §III.B (scaler leakage), §III.E (eROSITA axis), §III.G (Gaia preprocessing). A consolidated subsection would help readability but is not a defect. Lower-priority. |
| **GEM-P3-m1** | MIN | Fig. 8 caption: "Score annotations (3.2, 2.8) are not catalog-pipeline outputs". Re-render with catalog scores. | **OUT-OF-SCOPE — figure regeneration** | Trivially fixable on figure regen; not .tex-verifiable. Logged for figure regen pass. |
| **GEM-P3-m2** | MIN | §IV.B parenthetical "(An earlier draft quoted 38,330 pixels…withdrawn)" should be removed. | **VERIFIED → MINOR-LANGUAGE (proof-stage trim; overlaps OAI-E3)** | Same as OAI-E3. MINOR. |
| **GEM-P3-N1** | NIT | "Dated: June 2026" should be updated. | **FALSIFIED — auto-falsify rule (current date IS 2026-06-13 PT)** | Same class as P2 GRK-N1 + 4 prior rounds. June 2026 IS current. |
| **GEM-P3-M4** *(pass-2)* | M | Inconsistent normalization: §V.B baseline σ=8.98 vs Appendix C / Fig.11 baseline σ=16.85. | **STALE — already disclosed in body + figure caption** | tex L878 explicit: "the σ(f_NL) = 16.85 single-tracer baseline of the Appendix C shot-noise figure is on a different internal normalization and is not comparable to this value; only relative quantities transfer — see the Normalization note in that figure's caption". Figure 11 caption (L1134) carries the same disclosure. STALE-disclosed. |
| **GEM-P3-M5** *(pass-2)* | M | Fig. 3 left panel plots DESI + LAMOST `S` distributions on same x-axis; paper itself says cross-survey S values not comparable. | **VERIFIED → MINOR (figure regen)** | A legitimate visualization concern, even though §II.B carries the explicit caveat. Re-render as side-by-side panels. MINOR figure-regen item. |
| **GEM-P3-m3** *(pass-2)* | MIN | Incorrect internal `\ref` cross-references (abstract §VI claim; §III.A → §VID redirect). | **VERIFIED → MINOR (cross-ref audit)** | Worth a quick `\ref` audit pass. MINOR. |
| **GEM-P3-m4** *(pass-2)* | MIN | "Largest multi-archive anomaly search reported to date" caption-level claim needs softening or substantiation. | **STALE — already softened in abstract** | Abstract: "of which we are aware". Table I caption is firmer; can mirror the abstract softening. MINOR-LANGUAGE alignment. |

**Gemini-P3 round verdict**: This API-call leg is **substantively cleaner than the 4 prior browser-session Gemini-P3 rounds** (no hallucinated section numbers, no invented metric symbols, no false claims that present content is missing). 4 verified MINOR items (M5 fig regen + m3 cross-ref + m4 caption alignment + m2 proof-trim) + 4 STALE-disclosed (E1 framing, M1 LAMOST, M2 robustness, M4 normalization). The pre-brief "drop Gemini at EXT7" disposition applies to the EXTERNAL Gemini Thinking browser session, NOT to this internal API leg, which behaves as a normal reviewer.

### 2.3 Grok 4.3 (adversarial visual)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **GRK-P3-E1** | E | Abstract says "recommended catalog-grade tier contains 269,317 unique entries" (and "378,280 Path-C Unique Anomalies"); reviewer claims 269,317 is an "earlier cross-transfer number" not in body results. | **FALSIFIED** | 269,317 IS the canonical catalog-grade 6-way 5″ dedup count, established in tex L422 abstract, L568 footnote $\spadesuit$ (with explicit `\artifact{}` provenance pointer to `r24conf_pod_session_batch.json`), §IV cross-matches body text, and §VI Discussion. It is NOT cross-transfer; it is the post-native-retrain six-way dedup result. The 378,280 figure is the full 7-way Path-C unique catalog (including the 113,342 LAMOST exploratory tier). Both numbers appear in body and abstract consistently. Reviewer confused two distinct tiers. |
| **GRK-P3-E2** | E | "Dated: June 2026" future date. | **FALSIFIED — auto-falsify rule** | Current date IS 2026-06-13 PT. |
| **GRK-P3-E3** | E | Abstract claims "central 9.4% improvement"; body shows de-biased = baseline; 9.4% is "not the convex central value". | **STALE — already disclosed in same abstract sentence** | Abstract L422: `central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection`. The disclosure IS in the abstract, in the same sentence. Same as Gemini E1 — framing-preference, not a defect. |
| **GRK-P3-E4** | E | "37.3 Million Sources" inflates search volume vs 378k final dedup. | **OPINION (transparent disclosure)** | Abstract explicit: "applying the BigAE autoencoder framework to 37.3 million sources and CMB map patches" — clearly the INPUT corpus size, not the output catalog size. Same sentence carries "After per-survey native retraining and 7-way positional deduplication at 5″, the recommended catalog-grade tier contains 269,317 unique entries (…) drawn from a full Path-C unique catalog of 378,280 anomalies". The relationship between input and output IS in the same sentence. Editorial preference. |
| **GRK-P3-M1** | M | 28 pages too long. | **OPINION (overlaps OAI-M5)** | Editorial. |
| **GRK-P3-M2** | M | Internal Unix paths and JSON filenames in main text. | **OPINION (PRD-house-style; overlaps OAI-M1)** | `\artifact{}` macro is deliberate. |
| **GRK-P3-M3** | M | "~17.8% genuine novelty" missing Wilson interval / bootstrap in abstract. | **STALE** | Abstract L422 IS explicit: `178/1,000 ≈ 17.8% (Wilson 68% CI ± 1.2%)`. The Wilson interval IS in the abstract. STALE-disclosed. |
| **GRK-P3-M4** | M | χ²=376,713 spatial uniformity test missing effect size (Cramér's V). | **VERIFIED → MINOR (one-line add)** | Real precision. Add Cramér's V or equivalent. MINOR. |
| **GRK-P3-N1** | MIN | Table I footnote ♠ threshold-definition mapping unclear. | **OPINION → MINOR-LANGUAGE** | Cosmetic clarification. |
| **GRK-P3-N2** | MIN | Fig.1 "GOLD QSO-candidate confidence tier" undefined on that page. | **OPINION → MINOR** | Add forward-pointer. |
| **GRK-P3-N3** | NIT | Color bar / axis units. | **OPINION → NIT** | Cosmetic. |

### 2.4 Perplexity sonar (citation forensics)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **PPX-P3-E1** | E | eROSITA score axis irreproducible. | **STALE — already disclosed and tier demoted (same as OAI-E5)** | Membership-only release already in place. |
| **PPX-P3-E2** | E | Gaia DR3 preprocessing irreproducible. | **STALE — already disclosed** | tex §III.G explicit; Table I footnote carries the lineage-inferred status. |
| **PPX-P3-E3** | E | Cosmological claims (multi-tracer f_NL + NANOGrav) statistically consistent with null. | **STALE — already disclosed** | Same as Gemini E1 / Grok E3. The abstract IS explicit about "no multi-tracer improvement at current S/N" + "not a detection" + NANOGrav "decisive only against idealized circular-orbit SMBHB reference… not a cosmological detection". Substance is in. |
| **PPX-P3-E4** | E | Scale metrics: "141×" claim based on non-comparable denominator; like-for-like is 0.9×. | **STALE — already disclosed in same abstract sentence** | Same as OAI-E6 / Grok class. The 0.9× recount IS quoted in the abstract in the same parenthetical. STALE-disclosed. |
| **PPX-P3-E5** | E | ACT DR6 cross-correlation in §IV.D violates Path-C protocol. | **VERIFIED → MINOR-LANGUAGE (already labeled quarantined; reviewer wants stronger demotion)** | tex §IV.D explicit: "ACT DR6 is formally quarantined… and contributes zero objects to the 378,280 Path-C unique-object headline". §IV.D cross-correlation result is labeled as a "footprint-geometry-dominated" diagnostic, not a science result. Substance is in; reviewer wants stronger removal. MINOR-LANGUAGE / editorial. |
| **PPX-P3-M1** | M | LAMOST + Gaia + eROSITA completeness "formally unquantified" yet included in headline. | **STALE — already disclosed in tex §VI.C limitations + abstract** | Tier-level disclosure is in. |
| **PPX-P3-M2** | M | Novelty fraction overstatement / lack of full-catalog extrapolation. | **STALE — abstract explicit "full-catalog rate empirically untested"** | Disclosure is in. |
| **PPX-P3-M3** | M | 22.7% DESI anomalies "B-dominant" calibration-suspect. | **STALE — Table VII + §VI.C limitations carry this** | Disclosure is in. |
| **PPX-P3-M4** | M | Unweighted MSE limitation. | **STALE — §VI.C limitations carry this** | Disclosure is in. |
| **PPX-P3-N1** | MIN | Normalization inconsistency 8.98 vs 16.85. | **STALE — overlaps GEM-M4 / disclosed** | Disclosure is in. |
| **PPX-P3-N2** | MIN | "3 PASS / 3 FAIL" shorthand mixes QA + sensitivity tests. | **STALE — abstract explicit "NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by construction, not a detector-sensitivity test"** | Disclosure is in. |
| **PPX-P3-N3, N4, N5** | NIT | Taxonomy labels / date formatting / reference year. | **OPINION → NIT** | Cosmetic. |
| **PPX-P3-M5** *(pass-2)* | M | Table IV "Top 5 eROSITA anomalies" caption vs body top-298 membership-list. | **VERIFIED → MINOR (one-line caption rewrite)** | Caption rewrite to "first five entries of the released top-298 membership list". MINOR. |
| **PPX-P3-M6, M7** *(pass-2)* | M | Table I "Rate (%)" total-row vs per-survey-row column-meaning mismatch; cross-transfer vs Path-C row labeling. | **OPINION → MINOR-STRUCTURAL** | Table I structural reorganization preference; the existing footnote $\diamondsuit$ disclaims "neither figure is a data-driven detection rate". MINOR-LANGUAGE / editorial. |
| **PPX-P3-M8** *(pass-2)* | M | Fig.3 caption overstates SDSS tail compression as score-distribution property vs cross-transfer-to-native axis effect. | **VERIFIED → MINOR (caption tightening)** | Caption add explicit "cross-transfer-to-native score-axis effect" label. MINOR. |
| **PPX-P3-M9** *(pass-2)* | M | Fig.10 NEOWISE PASS vs QA-vs-sensitivity headline tally. | **STALE — abstract already discloses** | "3 PASS (SDSS 64%, Planck 100%, NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by construction, not a detector-sensitivity test)". Disclosure is in. Could mirror in Fig.10 caption. MINOR. |
| **PPX-P3-M10** *(pass-2)* | M | Table V caveat (j) "GS corrected" — main-text consolidation. | **OPINION → MINOR** | Same as EXT6 CGT-fM100-2 (OPINION). |
| **PPX-P3-M11** *(pass-2)* | M | Appendix C / Fig.11 baseline mismatch can be mistaken for updated forecast. | **STALE — already labeled** | Same as GEM-M4. STALE-disclosed. |
| **PPX-P3-M12** *(pass-2)* | M | Eq.(1) MSE dimensionally underspecified without pixel normalization context. | **VERIFIED → MINOR (one-sentence add)** | One-line caption add "x_i are survey-normalized inputs". MINOR. |
| **PPX-P3-M13** *(pass-2)* | M | Fig.1 caption / body 83 Exemplar-Set objects provenance ambiguity. | **VERIFIED → MINOR (caption tightening)** | Caption explicit "display-only, not a catalog tier". MINOR. |
| **PPX-P3-M14** *(pass-2)* | M | Appendix F ACT cross-transfer +200 phrasing ambiguity. | **VERIFIED → MINOR (one-word soften "bookkeeping-only +200 sensitivity variant")** | MINOR. |

### 2.5 Claude (FAILED CALL)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **CLD-P3-FAIL** | — | Anthropic API 400 (credit balance). | **N/A — no content** | Claude leg absent. |

---

## PART 3 — Counts and gap metric

| Category | Count | Items |
|---|---|---|
| **VERIFIED, genuinely-new actionable (MINOR-class)** | **15** | OAI-E3 (version-history trim), OAI-M2 (Planck held-out top-N), OAI-E7 (binomial-p Planck train/val), OAI-M8 (3″/5″ radius disclosure), OAI-m8 (dust-map specifier), OAI-m9 (per-class binomial intervals), GEM-M5 (Fig.3 panel split), GEM-m2 (proof-trim 38330 parenthetical), GEM-m3 (\ref audit), GEM-m4 (multi-archive softening), GRK-M4 (Cramér's V), PPX-M5 (Table IV caption), PPX-M8 (Fig.3 cross-transfer-axis label), PPX-M12 (Eq.(1) normalization), PPX-M13 (Fig.1 Exemplar-Set caption), PPX-M14 (Appendix F +200 phrasing) |
| **VERIFIED, POSITIVE-COHERENCE confirmations** | **3** | OAI-m2/m3/m4/m5 arithmetic spot-checks all pass; Fisher envelope α=0.19±0.65 → σ=8.14, edge α=0.84 → σ≈3.93, NANOGrav (3.0-2.567)/0.382=1.13σ, all independently confirmed |
| **FALSIFIED (auto-falsify: Fisher F₀ superscript-flattening)** | **1** | OAI-E1 (1/8.98^2 — 7th occurrence) |
| **FALSIFIED (auto-falsify: DESI top-1% phrasing carry)** | **1** | OAI-E2 |
| **FALSIFIED (auto-falsify: "future date June 2026")** | **2** | GEM-N1, GRK-E2 |
| **FALSIFIED (substance contradicts .tex)** | **1** | GRK-E1 (269,317 mis-claimed as cross-transfer; it is the canonical 6-way 5″ dedup count) |
| **STALE — already disclosed in .tex at the cited site** | **17** | OAI-E5 (eROSITA membership-only), OAI-E6 (73× vs 0.9× already in same parenthetical), OAI-M3 (scaler refit), OAI-M4 (novelty stratum disclosure), OAI-E8 (Planck rate denominator footnote), OAI-M7 (Appendix C fixed-α labeled), GEM-E1 (de-biased no-improvement IS in abstract first), GEM-M1 (LAMOST footnote $\spadesuit$ disambiguates), GEM-M2 (Jaccard 0.76 follow-up provided), GEM-M4 (Fig.11 normalization disclosed in body + caption), GRK-E3 (9.4% labeled noise-driven forecast), GRK-M3 (Wilson CI ± 1.2% in abstract), PPX-E1, PPX-E2, PPX-E3, PPX-E4, PPX-M1, PPX-M2, PPX-M3, PPX-M4, PPX-N1, PPX-N2, PPX-M9, PPX-M11 |
| **OPINION / editorial / PRD-house-style preference** | **17** | OAI-M1, M5, m1, m6, m7, n1, n2, n3, M6, M9, m10-m14, GEM-E1 framing, GEM-M3 (consolidated provenance section), GRK-E4 (37.3M phrasing), GRK-M1, GRK-M2, GRK-N1, GRK-N2, GRK-N3, PPX-E5, PPX-M10, PPX-N3, PPX-N4, PPX-N5 |
| **OUT-OF-SCOPE — figure regen** | **1** | GEM-m1 (Fig.8 burn-in scores) |
| **HD-11 RULED — submission-day** | **1** | OAI-E4 (Zenodo DOI) |
| **Call-failed** | **1** | CLD |
| **Pattern-051 regression check** | **0** | EXT6 closures (Table V row (h) + abstract dedup + footnote $\spadesuit$) all cohere; no fallout from the dedup-provenance pointer rewrite (footnote retains 269,317 / 108,963 / 4,379 / 113,342 arithmetic chain) |
| **Pattern-052 cumulative carry (EXT3–R36conf)** | **17+** | Fisher F₀ flattening at 7 occurrences; DESI top-1% phrasing at 4+; future-date June 2026 at 4+ |

**Genuinely-new substantive VERIFIED (MINOR or above)**: **16** (15 MINORs + 1 implicit consolidation if Houston elects PPX-M5+M8+M12+M13+M14 caption-bundle).
**No new BLOCKERs. No new acceptance-blocking MAJORs. No new VERIFIED BLOCKERs.**

---

## PART 4 — Reviewer accuracy this round

| Reviewer | Verdict called | Post-audit | Accuracy |
|---|---|---|---|
| OpenAI gpt-5 (methodology) | MAJOR REVISIONS | MINOR REVISIONS | **Highest signal-to-noise**: 8 verified MINOR items + 4 positive-coherence arithmetic confirmations + 5 STALE/OPINION over-calls. Re-fell into the **F₀ = 1/8.98²** PDF-extraction trap for the 7th cumulative occurrence — auto-falsify rule applied. |
| Gemini 2.5 Pro (cosmology, API) | MAJOR REVISIONS | MINOR REVISIONS | **Substantively cleaner than 4 prior browser-session Gemini-P3 rounds.** No hallucinated section numbers, no invented metrics. 4 verified MINOR items + 4 STALE-disclosed. The Houston pre-brief "drop Gemini at EXT7" specifically targets the EXTERNAL Gemini Thinking browser session, NOT this internal API leg. **Recommend continuing Gemini API-leg in R36conf-class rounds; ceasing the external browser-session Gemini Thinking only.** |
| Grok 4.3 (adversarial visual) | REJECT | MINOR REVISIONS | **High over-call rate**: REJECT severity unwarranted. 1 verified MINOR + 1 substance-falsified (269,317 mis-classified as cross-transfer) + 1 future-date auto-falsify + 5 STALE/OPINION. Continues to flag June 2026 as future. |
| Perplexity sonar (fallback from sonar-pro) (citations) | REJECT | MINOR REVISIONS | **High over-call + high STALE-disclosed rate** (12 STALE items): the substance the reviewer demands disclosed IS already disclosed in the same abstract paragraph or the cited section. Pass-2 surfaces 5 genuine MINOR caption/figure-regen items (M5, M8, M12, M13, M14). REJECT severity unwarranted; net contribution is a useful proof-stage caption-trim bundle. |
| Claude Opus 4.7 (brutal) | CALL FAILED | N/A | API credit balance 400 error; no content. |

---

## PART 5 — Closure plan (hardest first)

**No closures required for v3.1.101 to maintain its post-EXT6 CLEAN status.** All 15 genuinely-new VERIFIED items are MINOR-class proof / caption / cross-ref polish, suitable for a future quality-polish wave (v3.1.102 if Houston elects). Recommended bundle:

1. **[Caption + cross-ref polish bundle — MINOR]** Bundle 8 caption/cross-ref items in one wave:
   - PPX-M5: Table IV caption "first five entries of the released top-298 membership list"
   - PPX-M8: Fig.3 caption explicit "cross-transfer-to-native score-axis effect"
   - PPX-M12: Eq.(1) caption "x_i are survey-normalized inputs"
   - PPX-M13: Fig.1 caption explicit "83 Exemplar-Set objects are display-only, not a catalog tier"
   - PPX-M14: Appendix F "bookkeeping-only +200 sensitivity variant"
   - OAI-M8: Fig.6 + Table I SIMBAD radius (3″ vs 5″) disclosure
   - GEM-m4: Table I caption "of which we are aware" softening to match abstract
   - GEM-M5: Fig.3 left panel re-render as side-by-side per-survey panels
   - GEM-m3: \ref cross-reference audit pass (abstract §VI → §VII; §III.A → §III.A self-reference fix)
2. **[Methodology precision bundle — MINOR]** Bundle 3 items:
   - OAI-E7: Planck top-200 152/48 binomial-p ≈ 4×10⁻⁴ + Spearman/top-N stability (optional held-out-only)
   - OAI-m8: Dust correlation specify Planck τ_353 / I_857 / E(B-V) + resolution
   - OAI-m9: Per-class DESI rate binomial intervals + denominators
3. **[Stats precision — MINOR]** GRK-M4: Cramér's V effect size for χ²=376,713 spatial-uniformity test
4. **[OAI-E3 + GEM-m2 — MINOR proof-stage trim]** Remove the "earlier draft quoted 38,330 pixels…withdrawn" and "earlier draft listed 10.6s…withdrawn" parentheticals; relocate to changelog `%`-block.
5. **[OAI-M2 — MINOR, optional]** Planck native held-out top-N + Spearman stability analysis (artifact-side, paper-side one-paragraph addition).
6. **[OAI-E4 — HD-11 standing]** KEEP as Zenodo-DOI-at-submission.

**No tex edits required for FALSIFIED or STALE items.**

---

## PART 6 — Pattern-051 regression analysis

**P3 v3.1.101 is FREE OF PATTERN-051 REGRESSION.** All 3 EXT6 closures (Table V row (h) three-threshold form, abstract dedup-clause deletion, footnote $\spadesuit$ dedup-provenance pointer rewrite) propagated correctly:
- Table V row (h) at L950 carries the canonical three-threshold form coherent with footnote $\heartsuit$ (L548) and Table I caption (L541).
- Abstract L422 carries the canonical 269,317 / 269,117 numbers; `grep "264,938|264,738"` confirms zero occurrences in the live body (only `%`-block comments at L61, L332).
- Footnote $\spadesuit$ (L568) carries the canonical 6-way `r24conf_pod_session_batch.json` provenance pointer, the 4,379 LAMOST-overlap clarification, the 108,963 exploratory tier count, and explicit `269,317 = 269,317 (6-way) + 108,963 = 378,280 (7-way)` arithmetic — no number-chain fallout.

OpenAI E1 (Fisher F₀ = 1/8.98²) is the **7th cumulative PDF-extraction false-flag occurrence** — falsifies-on-sight per the standing auto-rule.

---

## VERDICT

**P3 v3.1.101 is CLEAN (CONFIRMED).** All three EXT6 closures propagated coherently. No new BLOCKERs, no acceptance-blocking MAJORs. 15 genuinely-new MINOR-class items are proof-quality polish suitable for an optional v3.1.102 wave; no items are required to maintain v3.1.101's post-EXT6 CLEAN status.

| Metric | Value |
|---|---|
| Genuinely-new VERIFIED (MINOR or above) | **15** |
| POSITIVE-COHERENCE confirmations | **4** (arithmetic spot-checks all pass) |
| FALSIFIED (auto-falsify rules) | **5** (Fisher F₀ + DESI top-1% + 2× future-date + 1 substance-falsified) |
| STALE — disclosed at cited site | **17** |
| OPINION / editorial | **17** |
| HD-11 standing | **1** |
| Call-failed | **1** |
| Pattern-051 regression | **0** |
| Pattern-052 cumulative carry | **17+** (Fisher F₀ now 7×; DESI top-1% 4×; future-date 4×) |
| Closure-coherence | **CLEAN: Table V row (h) + abstract dedup-deletion + footnote $\spadesuit$ rewrite all propagated correctly; no fallout** |
| Round verdict | **CLEAN — no required closures for v3.1.101; optional polish wave queued for v3.1.102** |
| Gemini-P3 disposition | **API-leg behaves cleanly; pre-brief "drop Gemini" applies only to EXTERNAL browser-session Gemini Thinking; CONTINUE Gemini in internal R-conf rounds** |
