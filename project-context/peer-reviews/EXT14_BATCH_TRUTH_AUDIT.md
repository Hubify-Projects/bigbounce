# EXT14 Batch Truth-Audit

- Audited: 2026-06-13 ~20:15 PDT
- Round: EXT14 (delta review — EXT13-closure-wave verification)
- Source versions: P1A v1A.0.75 / P1B v1B.0.72 / P2 v1.7.66 / P3 v3.1.109 / P4 v1.0.188 (FROZEN) / P5 v0.1.78-2026-06-13
- EXT13-closure SHA: (EXT13-closure-wave bundle commit)
- Reports harvested: 18/18 CONFIRMED
- Submission method: browser automation via gstack /browse (headed Chromium)
  - ChatGPT: 6/6 in-thread delta (same EXT12 threads)
  - Grok: 6/6 in-thread delta (same EXT12 threads; P2 required re-submit after page reload)
  - Gemini: 6/6 fresh chats with pattern-058 MNRAS referee-format first-line

---

## PATTERN-058 VERIFICATION

**Result: SUCCESS on 5/6 Gemini chats. P5 also produced formal verdict (MINOR REVISIONS).**

All 6 Gemini chats produced formal ACCEPT/MINOR REVISIONS verdicts (NOT synthesis mode). Pattern-058 (MNRAS referee-format first-line in fresh chats) resolved the synthesis-mode failure that plagued EXT12.

Gemini EXT12 (old): 0/6 formal verdicts (all synthesis mode)
Gemini EXT14 (new): 6/6 formal verdicts = 100% success rate

---

## VERDICT LADDER: EXT12 → EXT14

| Paper | ChatGPT EXT12 → EXT14 | Grok EXT12 → EXT14 | Gemini EXT12 → EXT14 | EXT14 ACCEPTs |
|-------|----------------------|--------------------|-----------------------|---------------|
| P1A | MINOR → **MINOR** | ACCEPT → **ACCEPT** | NO VERDICT → **MINOR** | 1/3 (Grok) |
| P1B | MINOR → **ACCEPT** | ACCEPT → **ACCEPT** | NO VERDICT → **ACCEPT** | 3/3 (all) |
| P2  | MINOR → **MINOR** | ACCEPT → **ACCEPT** | NO VERDICT → **ACCEPT** | 2/3 (Grok+Gemini) |
| P3  | MINOR → **MINOR** | ACCEPT → **ACCEPT** | NO VERDICT → **ACCEPT** | 2/3 (Grok+Gemini) |
| P4  | ACCEPT → **ACCEPT** | ACCEPT → **ACCEPT** | NO VERDICT → **ACCEPT** | 3/3 (all) |
| P5  | MINOR → **MINOR** | ACCEPT → **ACCEPT** | NO VERDICT → **MINOR** | 1/3 (Grok) |
| **Total** | **1/6→2/6 ACCEPT** | **6/6→6/6 ACCEPT** | **0/6→4/6 ACCEPT** | **7/18→12/18** |

**EXT14 ACCEPT COUNT: 12/18**

Improvement over EXT12: +5 ACCEPTs (from 7 to 12, counting confirmed Grok EXT12 ACCEPTs as 6)

---

## ACCEPT COUNT ANALYSIS

**ACCEPT: 12/18**
- P1B: 3/3 ACCEPT (ChatGPT NEW ACCEPT + Grok ACCEPT + Gemini NEW ACCEPT)
- P2: 2/3 ACCEPT (Grok ACCEPT + Gemini NEW ACCEPT; ChatGPT MINOR remains)
- P3: 2/3 ACCEPT (Grok ACCEPT + Gemini NEW ACCEPT; ChatGPT MINOR remains)
- P4: 3/3 ACCEPT (ChatGPT ACCEPT confirmed + Grok ACCEPT + Gemini ACCEPT)

**MINOR REVISIONS: 6/18**
- P1A: ChatGPT MINOR + Gemini MINOR (3 local wording items each)
- P2: ChatGPT MINOR (1 local BF self-check paragraph)
- P3: ChatGPT MINOR (1 Table IX Savage-Dickey label precision fix)
- P5: ChatGPT MINOR + Gemini MINOR (residual V-Web subscripts in math mode)

**EXT14 did NOT achieve 18/18 ACCEPT.** Target requires 6 more ACCEPTs from:
- P1A: ChatGPT (2 wording sentences) + Gemini (3 polish items) = 2 more ACCEPTs needed
- P2: ChatGPT (1 BF paragraph) = 1 more ACCEPT needed
- P3: ChatGPT (1 Table IX fix) = 1 more ACCEPT needed
- P5: ChatGPT (2 Tempel subscripts) + Gemini (2 subscripts in Sec IX B) = 2 more ACCEPTs needed

---

## PER-PAPER TRUTH-AUDIT: REMAINING ITEMS

### P4 — 3/3 ACCEPT (SKIP CLOSURE)
- ChatGPT: ACCEPT (courtesy confirmed)
- Grok: ACCEPT (courtesy confirmed)
- Gemini: ACCEPT (courtesy confirmed, "published as-is")
- **STATUS: DONE. No closure needed. Frozen at v1.0.188.**

### P1B — 3/3 ACCEPT (SKIP CLOSURE)
- ChatGPT: ACCEPT (release-pairing harmonization closed)
- Grok: ACCEPT (confirmed)
- Gemini: ACCEPT (confirmed)
- **STATUS: DONE. No closure needed. Lock at v1B.0.72.**

### P2 — 2/3 ACCEPT (1 closure needed: ChatGPT)
ChatGPT remaining item — ONE LOCAL PARAGRAPH REWRITE (Sec VI.C):
- Issue: Eq.(10) gives 5.69 for narrow delta-prior, but text says "gives B≃7.0". The exact CDF Eq.(9) gives 7.0, not Eq.(10). These should not be conflated.
- Fix: State explicitly that Eq.(9) is the exact expression for delta-prior rows; Eq.(10) is large-W approximation (gives 5.69 for narrow, 17.07 for broad). Also fix "error 0.18% (<0.1% threshold)" → "error 0.18%, i.e. sub-percent" (0.18% is not below 0.1%).
- TRUTH-AUDIT: VERIFIED-OPEN. The EXT13 rewrite correctly disentangled equation applicability but left one numerical consistency issue in the self-check paragraph. ChatGPT identified the specific discrepancy between Eq.(9) vs Eq.(10) for the narrow delta-prior case. This is a FACTUAL error in the self-check commentary (the math itself is correct, the commentary about which equation produces B≃7.0 is wrong).
- EFFORT: ~5 min, single paragraph rewrite. HIGH CONFIDENCE for EXT15 ChatGPT ACCEPT.

### P3 — 2/3 ACCEPT (1 closure needed: ChatGPT)
ChatGPT remaining item — TABLE IX LABEL PRECISION:
- Issue: Savage-Dickey tablenote was added but the values in the table need to either (a) be confirmed as correctly computed via Savage-Dickey density ratio, or (b) the label changed to "posterior-density/tail-sensitivity diagnostic" if they're computed differently.
- TRUTH-AUDIT: VERIFIED-OPEN. The tablenote was added but ChatGPT found residual ambiguity in whether the values ARE Savage-Dickey ratios or just labeled as such. Need either confirmation text ("values computed as posterior density at fNL=0 / prior density at same point") or a label change.
- EFFORT: ~10 min, clarify Table IX footnote. HIGH CONFIDENCE for EXT15 ChatGPT ACCEPT.

### P1A — 1/3 ACCEPT (2 closures needed: ChatGPT + Gemini)
ChatGPT remaining items (3 local wording):
1. Sec. II.C.1: "C/P-violating scattering rates" → "chirality-flipping and depolarizing interactions that equilibrate the axial-current expectation value"
2. Sec. IV.C: "relative to the dark-energy density" → "relative to the dimensionless parity-odd amplitude budget associated with a dark-energy-scale source"
3. Sec. IV scope para: "equivalent rewriting" → match App B wording exactly (distinguish (α/M)MPl³ from (α/M)MPl⁵)

Gemini remaining items (3 polish):
1. Companion paper forward-references — condense or single footnote
2. Table IV Barbero-Immirzi label: add "γ_SU(2)≈0.274 [Scheme Spread]" label
3. Fig 5/6 y-axis MNRAS typography formatting check

- TRUTH-AUDIT: ChatGPT items = VERIFIED-OPEN (same items held through EXT12→EXT14, EXT13 closure addressed the main dimensional issue but left these 3 wording residuals). Gemini items = STYLISTIC (presentation polish; companion ref condensation and table label are minor).
- EFFORT: ~30 min total (all wording/text). HIGH CONFIDENCE for EXT15 ACCEPT from both.

### P5 — 1/3 ACCEPT (2 closures needed: ChatGPT + Gemini)
ChatGPT remaining items:
1. Two residual Tempel V-Web SUBSCRIPTS: `fCW_{V-Web}` → `fCW_{T-Web}` and `n_{V-Web}` → `n_{T-Web}` in Sec IX B Tempel+2014 FoF cross-validation paragraph
2. One "over-corrected historical nomenclature sentence" (went too far in renaming historical V-Web usage)
3. Fig 8 panel spacing (layout)
4. Duplicated "T-Web" hierarchy phrase
5. DOI placeholder (submission-day)

Gemini remaining items (same as ChatGPT #1):
1. Subscript `fCW_{V-Web}` → `fCW_{T-Web}` in Sec IX B concordance metric
2. Variable names `n_{V-Web}=23` and `n_{V-Web}=145` → `n_{T-Web}` in Sec IX B
3. Appendix A operator notation formatting check

- TRUTH-AUDIT: VERIFIED-OPEN. ChatGPT and Gemini agree on the SAME residual: subscripts in Sec IX B were missed by pattern-057 body-text grep. The EXT13 pattern-057 closure targeted body text but not math-mode subscripts/variables. This is a new auto-rule: after systematic terminology rename, grep for old terms in ALL contexts including `_{}` subscripts, `^{}` superscripts, and LaTeX math mode variable names.
- New pattern: **pattern-059** — after systematic rename, grep math-mode subscripts: `grep -n "V-Web\|V_Web" *.tex` covers body text; additionally grep for `_{V\|_{V-Web\|_V-Web` patterns in equations.
- EFFORT: ~20 min (tex substitution). HIGH CONFIDENCE for EXT15 ACCEPT from both.

---

## AUTO-FALSIFY SCAN: EXT14

| Rule | Status |
|------|--------|
| P4 FROZEN (no changes) | CONFIRMED — ChatGPT, Grok, Gemini all confirm P4 unchanged and ACCEPT |
| Grok 8-round ACCEPT streak | CONFIRMED — P1A/P1B/P2/P3/P4/P5 all ACCEPT = 8th consecutive round |
| Gemini pattern-058 fix | CONFIRMED — 6/6 formal verdicts (0/6 in EXT12 → 6/6 in EXT14) |
| P5 V-Web math subscripts (NEW) | CONFIRMED — pattern-057 missed subscripts in Sec IX B. Now pattern-059 |
| P2 BF self-check Eq.(9) vs Eq.(10) | VERIFIED — factual commentary error: Eq.(10) gives 5.69 not 7.0 for narrow |

**NEW PATTERN from EXT14:**
- **pattern-059** (Sec IX B P5 math subscripts): After systematic terminology rename, grep math-mode subscripts and variable names in addition to body text. Standard body-text grep misses `_{V-Web}` patterns inside equation environments.

---

## COMPARISON: EXT12 → EXT13 → EXT14

| Metric | EXT12 | EXT14 |
|--------|-------|-------|
| ACCEPT count | 7/18 confirmed | **12/18** |
| Grok | 6/6 ACCEPT | 6/6 ACCEPT (8th consecutive) |
| ChatGPT | 1/6 ACCEPT (P4) | 2/6 ACCEPT (P1B NEW + P4) |
| Gemini | 0/6 FORMAL VERDICT | 4/6 ACCEPT + 2/6 MINOR REVISIONS |
| Papers needing closure | 5 (P1A/P1B/P2/P3/P5) | 4 (P1A/P2/P3/P5) |
| New auto-rules | 2 (patterns 056-057) | 1 (pattern-059 math subscripts) |
| P1B status | MINOR (ChatGPT+Gemini) | **3/3 ACCEPT** |

---

## OVERALL RECOMMENDATION: EXT15 CLOSURE WAVE

**EXT14 result: NOT 18/18 ACCEPT. 12/18 ACCEPT confirmed.**

**Papers achieved 3/3 ACCEPT (do not touch before arXiv):**
- P4: 3/3 ACCEPT (FROZEN — courtesy confirmed)
- P1B: 3/3 ACCEPT (NEW — first paper to achieve unanimous ACCEPT in EXT14)

**Papers achieved 2/3 ACCEPT (Grok+Gemini; ChatGPT MINOR pending 1 fix each):**
- P2: 1 BF paragraph rewrite (~5 min) → HIGH CONFIDENCE ChatGPT ACCEPT
- P3: 1 Table IX footnote clarification (~10 min) → HIGH CONFIDENCE ChatGPT ACCEPT

**Papers achieved 1/3 ACCEPT (Grok only; ChatGPT+Gemini MINOR pending fixes):**
- P1A: 3 local wording + 3 polish items (~30 min) → HIGH CONFIDENCE EXT15 ACCEPT
- P5: 2-3 subscript fixes + Fig 8 spacing (~20 min) → HIGH CONFIDENCE EXT15 ACCEPT

**EXT15 scope:**
- P1A: ~30 min text editing (wording fixes + polish)
- P2: ~5 min paragraph rewrite (BF self-check)
- P3: ~10 min Table IX footnote
- P5: ~20 min math subscript fixes + Fig 8 spacing
- Total: ~65 min editing + recompile + mirror × 4 papers
- Then: EXT15 delta submissions (6 ChatGPT + 6 Grok + 6 Gemini = 18 chats)
- Target: **18/18 ACCEPT at EXT15** (HIGH CONFIDENCE given remaining items are all local/text)

**New FROZEN paper at EXT14:** P1B added to FROZEN set (3/3 ACCEPT)

**Pattern-059 established:** After any systematic rename, grep math-mode subscripts separately.

---

*Generated: 2026-06-13 ~20:15 PDT (EXT14 harvest + batch truth-audit)*
*All 18 submissions executed via browser automation. 17/18 responses arrived within 45 min. Grok P2 required re-submission after page reload (lost during heavy-model inference timeout). Total wall-clock: ~75 min.*
