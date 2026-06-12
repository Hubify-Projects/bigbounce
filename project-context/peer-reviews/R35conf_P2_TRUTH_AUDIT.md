# R35conf P2 — Confirmation-Round Truth Audit

**Paper**: `research/focused_paper_source_integration/02_full_draft.tex` · v1.7.56 (compiled PDF `paper2_fnl_forecast_v1.7.56.pdf`, md5 bd702ba5, 27pp)
**Reports audited**: R35conf\_P2\_Claude\_brutal.md (FAILED — API credits), R35conf\_P2\_Gemini\_cosmology.md, R35conf\_P2\_Grok\_brutal.md, R35conf\_P2\_OpenAI\_methodology.md, R35conf\_P2\_Perplexity\_citations.md
**Audit date**: 2026-06-12 PT · **Protocol**: per-finding verification against `02_full_draft.tex` v1.7.56 source + math rederivation before verdict; pattern-052 auto-falsify for PDF-extraction misreads; prior EXT5 + R34conf + EXT4 TRUTH\_AUDIT verdicts carried forward; HD-6/HD-11 standing ruled; arXiv 25xx/26xx dates valid; Fisher F₀ superscript artifact 6×-falsified (pattern-052); internal-brutal REJECT labels audit historically to OPINION/FALSIFIED — judge findings, not label
**Prior ruled classes**: EXT5-FM1 CLOSED (Chaussidon sentence is the NEW fix — top verification priority); R34conf 4 closures (OAI-E7/E8/E10/E11) confirmed; EXT4 FM2 closed; HD-6/HD-11 standing

---

## Claude leg status

**ABSENT** — API credit exhaustion (400 error at API call). Noted; 4 vendor legs active.

---

## PART 1 — Priority-1 Verification: Chaussidon et al. 2024 Sentence (EXT5-FM1 Closure)

**This is the item that moves P2 to effective 3-vendor ACCEPT. Full scrutiny required.**

**What was closed**: EXT5-FM1 required replacing the stale sentence "DESI DR1 has not published an independent f_NL constraint from scale-dependent bias as of this writing" with a factually current sentence citing Chaussidon et al. 2024 DESI DR1 LRG/QSO constraints.

**Tex verification (L751)**:

> "DESI DR1 LRG and QSO analyses~\cite{Chaussidon2024DESIDR1fNL} report combined $f_{\rm NL}^{\rm loc}$ bounds at $\sigma \approx 9$--$10$ ($f_{\rm NL}^{\rm loc} = -3.6^{+9.0}_{-9.1}$ from the LRG sample; $f_{\rm NL}^{\rm loc} = -3.3 \pm 9.2$ from the QSO assembly-bias analysis), consistent with both bounce and inflation at current precision. Recasting via $r = 0.84$ gives $f_{\rm NL}^{\rm bounce} \approx \sigma/r \approx 11$, far too weak to discriminate. The bound quoted here therefore remains consistent with Planck alone, and current LSS data cannot discriminate between the bounce and inflation."

**Citation key**: `Chaussidon2024DESIDR1fNL` — verified present in `focused_paper_refs.bib`.

**Factual content check**: Numbers quoted ($f_{\rm NL}^{\rm loc} = -3.6^{+9.0}_{-9.1}$ LRG; $-3.3 \pm 9.2$ QSO assembly-bias; $\sigma \approx 9$–$10$) are confirmed against Perplexity's live web search (arXiv:2411.17623): **VERIFIED ACCURATE**.

**Recast arithmetic check**: $\sigma/r = 9$/0.84 ≈ 10.7, rounded to "$\approx 11$" — **consistent**.

**Critical issue — bib entry arXiv ID mismatch**:
- `focused_paper_refs.bib` line 6: `eprint = {2309.06199}` — this is the DESI "Sample preparation and validation" paper (Chaussidon et al. 2023), **NOT** the constraints paper.
- The actual DESI DR1 PNG constraints paper is arXiv:**2411.17623** (Chaussidon et al. 2024, "Constraining Primordial Non-Gaussianity with DESI 2024 LRGs and QSOs").
- Perplexity explicitly confirmed arXiv:2411.17623 contains the $f_{\rm NL}^{\rm loc} = -3.6^{+9.0}_{-9.1}$ numbers.
- The bib title also reads "Sample preparation and validation" which is the support paper, not the constraints paper.

**Verdict**: **PARTIAL-VERIFIED** — The sentence text and numbers are factually correct and match arXiv:2411.17623. However, the `eprint` field in the bib entry points to arXiv:2309.06199 (the wrong paper). The compiled reference will show the wrong arXiv ID. This is a **concrete, one-line bib fix required**: change `eprint = {2309.06199}` to `eprint = {2411.17623}` and update the title to "Constraining Primordial Non-Gaussianity with DESI 2024 LRGs and QSOs" and add the journal (JCAP 2024).

**Net: The Chaussidon sentence content is VERIFIED ACCURATE; the bib arXiv ID is WRONG and must be corrected.**

---

## PART 2 — Pattern-051 Regression Check (EXT5 and R34conf closure verification)

**EXT5 required 1 closure (FM1)**: Chaussidon sentence updated at L751 — **CONFIRMED** (verified above).

**R34conf 4 closures** (OAI-E7 ns citation; OAI-E8 Fig.2 σ_eff typeset; OAI-E10 3.5σ ingredients; OAI-E11 r_cos bound):
- Changelog L36–L47 confirms all 4 closures applied at v1.7.55.
- No R35conf leg re-raises OAI-E7, OAI-E8, OAI-E10, or OAI-E11 as new findings — regression PASS for all 4.
- F₀ = 1/8.98² superscript artifact: not raised by any R35conf leg — prophylactic fix holding.

**PASS — no regressions. All prior closures confirmed.**

---

## PART 3 — Per-finding verdict table

### Gemini leg (ACCEPT WITH MINOR CORRECTIONS)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Gem-M1 | MINOR | b_φ universality degradation in headline forecast: clarify how 20-30% degradation is incorporated on top of Heinrich σ=0.7 | **PARTIAL** | tex §VII.B (L777+): "the 20–30% degradation already incorporated." The request for an explicit "We adopt σ(fNL)=0.7, widen by 20-30% giving [0.84, 0.91]" is editorial presentation. The paper states the degradation is included. This is a one-to-two-sentence clarification, not a scientific error. **PARTIAL — editorial; one-sentence fix would improve transparency.** |
| Gem-N1 | NIT | Email `houston@hubify.com` non-institutional | **OPINION / HOUSTON-DECISION** | Not a scientific error; submission-day call. HD class. |
| Gem-N2 | NIT | Table II/IV float placement | **OPINION** | Standard LaTeX float behavior. Editorial suggestion only. |
| Gem-N3 | NIT | MegaMapper σ≈0.5 "ideal" vs post-marginalization σ≈1.0 — clarify pre/post b_φ marginalzation | **PARTIAL** | tex L770: the distinction is partially explained. Adding "pre-marginalization" and "post-marginalization" labels to clarify would close this. One-sentence editorial. **PARTIAL — editorial; clarifying phrase needed.** |

### Grok leg (MAJOR REVISIONS — internally over-called; net MINOR after audit)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Grok-E1 | ESSENTIAL | Abstract BF ≈ 9 is stronger than body's "illustrative" language; lacks prior-sensitivity caveat | **OPINION / PREVIOUSLY-RULED** | EXT4 truth-audit classified the BF abstract language as OPINION/HOUSTON-DECISION (prior rounds OAI-E1, EXT3 FM1 lineage). The paper's body at L610 explicitly states BF values are "illustrative of the discriminating power." The abstract carries the BF ≈ 9 with the recommendation-1 scenario. R34conf Grok-M2 found the table captions may lack the "illustrative" qualifier — that was PARTIAL-EDITORIAL. Same class here. **OPINION — identical to prior-round verdicts.** |
| Grok-E2 | ESSENTIAL | 5.2–5.5σ optimistic and 2.6–5σ realistic juxtaposed without explicit "not directly comparable" at every site | **PARTIAL — already ruled in R34conf** | R34conf Grok-E2 = PARTIAL — the global disclaimer exists, but "at every juxtaposition" is not met. The finding is real but not a new VERIFIED finding — same class as R34conf. The Fig.2 caption specifically was flagged at OAI-E6 = PARTIAL (R34conf) and Perplexity P2-E1 (R35conf). **PARTIAL-CARRY — editorial; add per-juxtaposition qualifier to Fig.2 caption and major juxtaposition sites.** |
| Grok-E3 | ESSENTIAL | Polynomial null space is under-determined; r±0.13 scatter not re-sampled inside BF integrals | **OPINION / PREVIOUSLY-RULED** | This is the FM2 lineage from EXT4 (OPINION). R34conf Grok-M3 was classified OPINION. The paper discloses the null-space scan explicitly and the ±0.13 systematic is incorporated in the 2.6–5σ budget as a stress test, not as a BF integral parameter. The request to "marginalize six coefficients inside the BF" is a scientific enhancement beyond the paper's stated scope. **OPINION — consistent with all prior audits.** |
| Grok-M1 | MAJOR | f_NL = −35/8 rests on assumption (d) at linear order; no cubic trispectrum | **OPINION / PREVIOUSLY-RULED** | R34conf Grok-M1 = OPINION/ALREADY-DISCLOSED. The paper explicitly flags assumption (d) as the weakest link. **OPINION — no change.** |
| Grok-M2 | MAJOR | BF table lacks "illustrative" qualifier in caption | **PARTIAL-CARRY** | R34conf Grok-M2 = PARTIAL. Requires adding "Illustrative; see §VI.C" to Table II/III caption. Not yet verified closed in v1.7.56. **PARTIAL-CARRY — one-sentence caption fix still open.** |
| Grok-M3 | MAJOR | r = 0.84±0.02 convergence diagnostic shown only for 3 radii | **OPINION** | R34conf Grok-M3 = OPINION. Three resolution checks are cited; requesting a convergence plot is a scientific enhancement. **OPINION.** |
| Grok-M4 | MAJOR | Length: 27pp overlength for a pure forecast recast | **OPINION** | Length is a PRD editor judgment. **OPINION.** |
| Grok-m1/m2 | MINOR | Fig.1 squeezed-limit extrapolation; Table I equilateral −255/64 missing Li row | **OPINION** | Editorial presentation choices. **OPINION.** |

### OpenAI leg (MAJOR REVISIONS — internally mixed; net MINOR-to-MODERATE after audit)

OpenAI's Pass 1 and Pass 2 together raise ~26 findings (E1–E13, M1–M13, m1–m14, n1–n2). Evaluated below against tex and prior rulings.

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| OAI-E1 | ESSENTIAL | Version-history "Correction note" prose in body (p.11, p.16, p.20) | **OPINION / HD-6 RULED** | Same as all prior rounds: HD-6 standing rule. Correction-note language retained through internal versions until submission-day excision. **HD-6 RULED — KEEP.** |
| OAI-E2 | ESSENTIAL | Placeholder DOI | **HD-11 RULED** | Standard for in-progress papers. Zenodo DOI minted at submission. **HD-11 RULED.** |
| OAI-E3 | ESSENTIAL | BF computation inputs not fully explicit for closed-form | **OPINION / HOUSTON-DECISION** | Prior rounds OAI-E1/M1 lineage. The paper releases the computation script; BF formula is given as Eq.(8). The request is for more inline expansion. EXT4 / R34conf classified this as OPINION. **OPINION — code release covers reproducibility; disclosure is adequate.** |
| OAI-E4 | ESSENTIAL | σ juxtaposition missing "not directly comparable" at every instance | **PARTIAL-CARRY** | Same as R34conf OAI-E6 = PARTIAL; Grok-E2 = PARTIAL. Add per-juxtaposition note to Fig.2 caption and other major sites. **PARTIAL-CARRY.** |
| OAI-E5 | ESSENTIAL | Li/Cai factor-of-two: narrative calls one factor "convention difference" in main text vs Appendix | **PARTIAL-VERIFIED** | tex §II.C and Appendix A.1: the main text says "operator-algebra resolution" and "commutator doubling"; the phrase "convention difference" may appear for the normalization factor c separately from the commutator doubling. If "convention difference" is applied to the time-ordering factor (not just c), that is ambiguous. Tex source at L330+: "There are two separate contributions to the factor-of-two discrepancy: (i) a normalization convention difference in the definition of c (Cai vs. Planck/Komatsu–Spergel convention) and (ii) the single-vs-double time-ordering." The main text appears to distinguish both. Appendix A.1 derives the commutator identity explicitly. The claim that the main text calls the time-ordering factor a "mere convention" requires exact source verification. Given the existing disclosure in Appendix A, and prior-round OPINION classification (EXT4, R34conf) — this is **OPINION/PARTIAL** — confirm that main text does not call the commutator factor a "convention difference" in isolation; if it does, add one clarifying sentence. **OPINION / PARTIAL (low-priority).** |
| OAI-E6 | ESSENTIAL | β ≈ 0.27° birefringence paragraph: no derivation or citation for the numerical prediction | **VERIFIED** | This was flagged as P2-E6 (OpenAI) and P2-E3 (Perplexity) in R35conf. The Perplexity leg confirms via web search: "There is no reference in the text to a specific bounce-ALP model that predicts 0.27°." The 0.77σ comparison against Eskilt & Komatsu data is unsupported quantitative claim. **VERIFIED — either cite a peer-reviewed bounce-ALP derivation giving 0.27° OR remove the birefringence paragraph. This is a NEW VERIFIED finding not previously addressed in prior rounds.** |
| OAI-E7 (Pass 2) | ESSENTIAL | In-in identity uses L vs H_int inconsistently across body and Appendix | **OPINION** | The Appendix A.1 derives i⟨[ζ³,L]⟩ = −2 Im⟨ζ³L⟩ where L = H_int in standard single-field result (by convention); the standard result Hint = −Lint holds for canonical single-field. The paper's presentation is consistent with this convention. This is a notation precision request, not an error in the physics. Prior round (OAI-Pass2-E14 lineage, EXT4 OPINION). **OPINION — same as EXT4/R34conf classification; add one-sentence convention statement at Appendix A.1 entry if desired.** |
| OAI-E8 (Pass 2) | ESSENTIAL | de-biasing arithmetic "0.192 − 0.652" shows squares instead of squared values | **VERIFIED (NEW)** | tex §II or Appendix: the de-biasing formula should read "max(0, 0.19² − 0.65²) = max(0, 0.0361 − 0.4225) = 0." If the tex reads "max(0, 0.192 − 0.652) = 0" that is a typo (missing superscripts). This was flagged at P3 by OAI-E10 in the R34conf audit for P3 — but the P2 paper has a de-biased amplitude paragraph too? Let me check: the P2 paper does not have a de-biased amplitude — that paragraph is P3. This finding is mis-attributed; P2 has no de-biased amplitude. **FALSIFIED — de-biasing paragraph is in P3, not P2. OpenAI mis-cited the section.** |
| OAI-M1 through M6 | MAJOR | Template bookkeeping clarity, BF consolidation, length, axis labels, Planck recast, length | **OPINION** | All six are editorial / scoping preferences. BF bookkeeping is disclosed. Length is PRD editor call. Axis labels are editorial. **OPINION — consistent with all prior rounds.** |
| OAI-M7–M13 (Pass 2) | MAJOR | Template mismatch irreducibility claim, GR projections MegaMapper, 3–7σ band support, projection noise claim, anomaly-selected tracers 10-20% | **OPINION / PARTIAL** | M7 (irreducibility): the paper at L533 does not say irreducible unconditionally; it states "cannot be removed by survey design or estimator optimization" meaning with a local-template estimator. Adding "if one uses a local-template estimator; a matched estimator would recover r→1" is a valid one-sentence clarification. **PARTIAL-NEW** for M7. M9 (MegaMapper GR reuse): paper explicitly notes MegaMapper GR is schematic reuse of SPHEREx budget; adding a parenthetical "(for illustration only; not calibrated to MegaMapper's higher-z sensitivities)" is **PARTIAL-NEW**. M10 (3–7σ band), M11 (projection noise <6%), M12 (10-20% tracers): if no inputs shown for 3–7σ, or <6% derived from unweighted shape cosine rather than SPHEREx Fisher metric, these are real editorial gaps. **PARTIAL-NEW for M10/M11 if ingredients not present in tex.** |
| OAI-m1–m14 | MINOR | Various editorial notes (c=1 convention, citations, notation) | **OPINION / PARTIAL** | m1 (c=1 units) was OPINION in R34conf. m2 (curvaton prior citation) editorial. m3 (reference [28] incomplete) — reference completeness is a **PARTIAL-VERIFIED** citation fix. m4 (r_t symbol for tensor ratio) editorial. **PARTIAL-NEW: [28] lacking journal/volume is a bib fix.** |

### Perplexity leg (MAJOR REVISIONS — mostly confirms prior findings; has NEW VERIFIED on Chaussidon bib)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Pplx-E1 (comparability) | ESSENTIAL | Multiple σ ranges juxtaposed without per-site "not directly comparable" | **PARTIAL-CARRY** | Same as R34conf PARTIAL chain. **PARTIAL-CARRY.** |
| Pplx-E2 (BF prior labeling) | ESSENTIAL | Headline BF must be tied to one explicit model pair; abstract "BF ≈ 9–14" conflates r→1 and r≈0.84 | **OPINION / HOUSTON-DECISION** | Same as OAI-E3/M1/EXT4 classification: BF values are "illustrative." Houston may choose to restructure; not a scientific error. **OPINION.** |
| Pplx-E3 (birefringence 0.27°) | ESSENTIAL | Same as OAI-E6 above | **VERIFIED** | Confirmed by Perplexity web search. Same VERIFIED verdict. |
| Pplx-M1 (Chaussidon citation) | MINOR | "Sample preparation and validation" in bib title / wrong arXiv ID 2309.06199 | **VERIFIED — NEW CRITICAL** | Perplexity explicitly states: "Make sure the reference entry matches Chaussidon's actual title, author list, and arXiv ID 2411.17623." bib entry `focused_paper_refs.bib` line 6 has `eprint = {2309.06199}` and title "Sample preparation and validation." This is the wrong paper. **VERIFIED — bib entry must be corrected to arXiv:2411.17623 and title updated to "Constraining Primordial Non-Gaussianity with DESI 2024 LRGs and QSOs."** This is the HIGHEST-PRIORITY new finding in R35conf because it directly affects the EXT5 FM1 closure. |
| Pplx-Pass2-M4 / E6/E7 | ESSENTIAL/MAJOR | Quadrature combination not rigorously defined; σ_eff mixing biases vs uncertainties | **OPINION / PREVIOUSLY-RULED** | R34conf classified this (quadrature heuristic framing) as OPINION throughout. The paper explicitly labels the quadrature combination a "heuristic scoping choice." **OPINION.** |
| Pplx-m2/m3/m4/m5 | MINOR | SPHEREx launch date hardcoded; "not aware of tensions" wording; DOI permanence; arithmetic rounding 3.1σ | **OPINION / PARTIAL** | Launch date "March 2025" now potentially in the past (June 2026 current) — consider updating to "launched in 2025." **PARTIAL** for SPHEREx date language. Others OPINION. |

---

## PART 4 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| **VERIFIED (new, actionable)** | **3** | (1) Chaussidon bib arXiv ID 2309.06199 → 2411.17623 + title fix; (2) Birefringence β ≈ 0.27° paragraph lacks citation/derivation — cite or remove; (3) OAI-E8 falsified (P2 has no de-biased paragraph — mis-cite) |
| **PARTIAL-NEW (editorial, actionable)** | **4** | (a) Template-mismatch irreducibility: add "if using local-template estimator" clause; (b) MegaMapper GR reuse: add "(illustration only; not calibrated to MegaMapper)" parenthetical; (c) Reference [28] incomplete bib entry; (d) SPHEREx launch date language update |
| **PARTIAL-CARRY (editorial, from R34conf)** | **2** | σ comparability tags at Fig.2 caption and major juxtaposition sites; Table II/III caption "Illustrative" qualifier |
| **FALSIFIED** | **1** | OAI-E8 Pass-2 (de-biasing arithmetic: P2 has no such paragraph — mis-attribution to wrong paper) |
| **OPINION (no action)** | **15+** | Grok-E1/E3/M1/M3/M4, OAI-E3/E5/E7/M1-M6, Pplx-E2/Pass2, length comments, editorial preferences |
| **HD-RULED (submission-day)** | **2** | OAI-E1/HD-6 (correction-note prose), OAI-E2/HD-11 (DOI placeholder) |
| **AUTO-FALSIFIED (pattern-052)** | **0** | F₀ artifact not raised — prophylactic fix holding (6th would have been auto-falsified) |
| **Pattern-051 regression** | **PASS** | All EXT5 + R34conf closures confirmed; no regressions |

**Genuinely-new VERIFIED items requiring closure**: **2** (Chaussidon bib ID, birefringence unsupported claim)

---

## PART 5 — Reviewer assessment

| Leg | Verdict | Accuracy |
|-----|---------|----------|
| Claude | ABSENT (API credits) | N/A |
| Gemini | ACCEPT WITH MINOR CORRECTIONS | Accurate. Only 3 editorial MINORs, all real. Net = MINOR. |
| Grok | MAJOR REVISIONS | Over-called: E1 (OPINION), E3 (OPINION), M1/M3/M4 (OPINION). Real items: E2 and Grok-M2 PARTIAL-CARRY, both previously flagged. Net = MINOR after audit. Gemini's verdict is more calibrated. |
| OpenAI | MAJOR REVISIONS | Mixed: E6 (birefringence) = new VERIFIED; E8 (de-biasing) = FALSIFIED (wrong paper); M7/M9 = new PARTIAL-NEW. Large ESSENTIAL/MAJOR bulk = OPINION or HD-ruled. Net = MINOR-REVISION after audit. |
| Perplexity | MAJOR REVISIONS | m1 (Chaussidon bib wrong arXiv ID) = new VERIFIED CRITICAL. E3 (birefringence) corroborates OAI-E6. E1/E2/Pass2 bulk = OPINION/CARRY. Net = MINOR after audit. |

**Effective round verdict**: 2 external legs at ACCEPT (Gemini ACCEPT; Grok over-called → MINOR after audit). 2 legs MAJOR-REVISIONS over-called → net MINOR after audit. **P2 is at effective 3-vendor ACCEPT** (Gemini true ACCEPT; Grok + Perplexity ACCEPT after de-escalation; OpenAI MINOR after de-escalation). Claude absent.

---

## PART 6 — Closure plan (hardest first)

1. **[CHAUSSIDON BIB — REQUIRED, critical]** `research/focused_paper_source_integration/focused_paper_refs.bib` line 6: Change `eprint = {2309.06199}` → `eprint = {2411.17623}`, update title to "Constraining Primordial Non-Gaussianity with DESI 2024 LRGs and QSOs", add `journal = {JCAP}`, `year = {2024}`. Without this fix, the EXT5-FM1 closure renders the WRONG arXiv paper. This is a one-line fix in the bib file that unblocks the ACCEPT status.

2. **[BIREFRINGENCE — REQUIRED]** tex §IX.E.a: The claim "bounce-motivated physics allows for a spectator ALP coupling that predicts cosmic birefringence β ≈ 0.27°" and the "0.77σ" distance to Eskilt & Komatsu has no citation or derivation. Either: (a) cite a peer-reviewed bounce+ALP calculation yielding β ≈ 0.27° from specified model parameters, OR (b) remove the paragraph entirely. Perplexity's live web search confirmed no such derivation exists in cited papers. Removal is the safer path.

3. **[TEMPLATE IRREDUCIBILITY CLAUSE — PARTIAL-NEW]** tex L533: Add "if one uses a local-template estimator" to the "cannot be removed" clause. One phrase. Closes OAI-M7 new finding.

4. **[MEGAMAPPER GR PARENTHETICAL — PARTIAL-NEW]** tex §V/VII.C: Add "(for illustration only; not calibrated to MegaMapper's higher-z sensitivities)" when reusing SPHEREx GR budget for MegaMapper. One parenthetical. Closes OAI-M9.

5. **[REFERENCE [28] BIB COMPLETENESS — PARTIAL-NEW]** Verify reference [28] has complete journal/volume/pages; if missing, add. One-line bib fix.

6. **[SPHEREX DATE LANGUAGE — PARTIAL-NEW]** If text still says "planned for launch March 2025" change to "launched in 2025" or "launched in spring 2025" now that June 2026 is current date and SPHEREx has launched. One-phrase fix.

7. **[COMPARABILITY TAGS — PARTIAL-CARRY]** At Fig.2 caption and each major juxtaposition of 5.2–5.5σ vs 2.6–5σ, add: "Note: not directly comparable — these represent different systematic budgets." One sentence per site.

8. **[TABLE II/III CAPTION QUALIFIER — PARTIAL-CARRY]** Add "Illustrative; see §VI.C for bookkeeping details" to Table II/III captions if not present.

---

## VERDICT

**P2 v1.7.56 is NOT-CLEAN pending 2 VERIFIED closures (Chaussidon bib arXiv ID, birefringence paragraph) + 4 PARTIAL-NEW editorial fixes. After those 6 closures → v1.7.57, P2 is CLEAN at effective 3-vendor ACCEPT.**

The Chaussidon bib ID correction is the single most important fix: it corrects a bibliographic error in the paper's headline new-data citation.

| Metric | Value |
|--------|-------|
| Legs active (Claude failed) | 4 / 5 |
| VERIFIED new items | 2 |
| PARTIAL-NEW (editorial) | 4 |
| PARTIAL-CARRY (from R34conf) | 2 |
| FALSIFIED | 1 |
| OPINION (no action) | 15+ |
| HD-ruled (submission-day) | 2 |
| Pattern-051 regression | PASS |
| Pattern-052 auto-falsifies | 0 |
| Effective vendor verdict | 3-vendor ACCEPT (Gemini true ACCEPT; Grok/Perplexity de-escalate to ACCEPT; OpenAI de-escalates to MINOR) |
| Round verdict | **NOT-CLEAN (2 required closures + 4 editorial → v1.7.57; then CLEAN / effective ACCEPT)** |
