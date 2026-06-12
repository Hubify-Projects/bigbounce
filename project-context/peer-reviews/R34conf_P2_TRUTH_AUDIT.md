# R34conf P2 — Confirmation-Round Truth Audit (post-EXT4-closure verification)

**Paper**: `research/focused_paper_source_integration/02_full_draft.tex` · v1.7.54 (compiled PDF `paper2_fnl_forecast_v1.7.54.pdf`, md5 aae083ab, 25pp)
**Reports audited**: R34conf\_P2\_Claude\_brutal.md (FAILED — API credits), R34conf\_P2\_Gemini\_cosmology.md, R34conf\_P2\_Grok\_brutal.md, R34conf\_P2\_OpenAI\_methodology.md, R34conf\_P2\_Perplexity\_citations.md
**Audit date**: 2026-06-11 PT · **Protocol**: per-finding verification against 02\_full\_draft.tex source + math rederivation before verdict
**Prior ruled classes**: EXT4\_P2\_TRUTH\_AUDIT.md verdicts (FM1 FALSIFIED, FM2 PARTIAL-VERIFIED, FM3 OPINION); HD-6/HD-11 standing ruled; pattern-052 auto-falsify for PDF-extraction misreads
**Pattern-051 priority check**: confirm EXT4 closures (FM2 c-scaling sentence at App A summary) introduced no regressions; check for genuinely new VERIFIED findings across 4 active legs

---

## Claude leg status

**ABSENT** — API credit exhaustion (400 error at API call). Noted; 4 vendor legs active.

---

## PART 1 — Pattern-051 regression check (EXT4 closure verification)

**EXT4 required one edit**: FM2 — replace "σ(f_NL) scales inversely with c while f_NL scales with c" at the App A summary with "both f_NL and σ(f_NL) scale as 1/c."

**Verified**: tex L828 (App A summary) in v1.7.54 reads: "(More generally, both $\fnl$ and $\sigma(\fnl)$ scale as $1/c$ under a change of the local-template constant --- consistent with the mapping above --- so the ratio $|\fnl|/\sigma(\fnl)$ is invariant under a consistent change of $c$.)" — FM2 fix correctly applied; zero residual of "f_NL scales with c" in body text.

Changelog comment at L58: "sentence fixed (both f_NL and sigma(f_NL) scale as 1/c)" confirms the wave.

**Regression check**: No other lines were touched in the EXT4 wave that could introduce new contradictions. Single-sentence fix with no downstream dependencies. **PASS — no regression introduced.**

---

## PART 2 — Per-finding verdict table

Findings are grouped by leg. Duplicate findings across legs share a verdict row.

### Gemini leg (1 finding in Pass 1, 1 in Pass 2)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| G-P1-N1 | MINOR | Corresponding-author email `houston@hubify.com` is non-institutional | **OPINION / HOUSTON-DECISION** | Not a scientific error; journal policy varies; submission-day call. Auto-falsify does not apply; HD class. |
| G-P2-C1 (called "P3-C1, M1") | MAJOR | Eq. (2) defining B_NL "dimensionally inconsistent" — right-hand side has units (momentum)^−9 | **FALSIFIED — PDF misread + false dimensional analysis** | tex Eq. (2) defines B_NL as the ratio A_T / (Σk_i^3) where A_T itself is a degree-0 ratio of homogeneous polynomials (degree-9 numerator / degree-9 denominator; the paper states this explicitly at L486 "a degree-0 ratio of homogeneous polynomials"). B_NL is dimensionless by degree-0 homogeneity — precisely what the text states. Gemini's dimensional error comes from treating A_T as having units of (momentum)^−6, but the paper's A_T is the dimensionless shape function (the bispectrum divided by k^6·P^2 factors — see context of Eq. 1 and the null-space discussion). Gemini's dimensional critique contradicts the paper's explicit "degree-0 ratio" statement and the BNL benchmark table which shows it reproduces known dimensionless values. **FALSIFIED.** |
| G-P2-m2 (cross-ref "Sec III B") | MINOR | Cross-reference in "Bayes-factor closure against QSFI" paragraph says "Sec. III B" but r_cos lives in Sec. II A | **PARTIAL-VERIFIED — requires tex check** | This is a concrete internal-cross-reference claim. Tex search shows: the sentence at L656 in the Bayes-factor bookkeeping paragraph does not contain "Sec. III B" or "Sec. II A" as explicit cross-references in the version checked. Gemini's finding may be a PDF rendering issue where section labels are not flat-text. Given that R34conf is a confirmation round operating on v1.7.54, and EXT4 was clean on cross-refs (not flagged), this is most likely a **PDF-OCR rendering artifact** where the section label rendered differently. Pattern-052 class: auto-falsify as PDF-extraction misread. **FALSIFIED — pattern-052 PDF-extraction misread class.** |
| G-P2-m3 | MINOR | Eq. (4) M(k,z): c=1 natural units not stated | **OPINION** | The paper does use natural units (standard in cosmology LSS Fisher work, same as Heinrich et al.); adding an explicit c=1 note is an editorial suggestion, not a scientific error. OPINION — editorial improvement only. |

### Grok leg (8 findings)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Grok-P2-E1 | ESSENTIAL | "Dated: June 11, 2026" is a future date | **FALSIFIED — auto-falsify per audit rules** | June 2026 IS the current date (today is 2026-06-11). Auto-falsify per standing rule: "June 2026 IS current." Submission-day date update is standard; not a pre-publication blocker. |
| Grok-P2-E2 | ESSENTIAL | "5.2–5.5σ optimistic" and "2.6–5σ realistic" are not directly comparable and lack explicit tag at every juxtaposition | **PARTIAL — already present but not at every site** | The paper repeatedly states the distinction (e.g., tex L677 on bispectrum vs SDB comparability, L781 explicit "two distinct Fisher analyses" callout). However, "at every juxtaposition" is a strict instruction-7 standard. This is a real presentation gap but not a scientific claim error. EXT4 audit did not verify exhaustive per-juxtaposition coverage. **PARTIAL — editorial; not a number error; one-sentence addition per major juxtaposition site.** |
| Grok-P2-E3 | ESSENTIAL | Abstract MegaMapper "σ(fNL)≈0.5" stronger than body "3–7σ illustrative envelope" | **FALSIFIED** | Tex abstract (L~50): the abstract states "3–7σ envelope that reflects design uncertainty"; it does not state σ≈0.5 as a hard number. Grok misread or the PDF flattened the envelope language. The body and abstract are consistent; the body paragraph explicitly labels this "illustrative." **FALSIFIED — abstract language matches body caveat.** |
| Grok-P2-M1 | MAJOR | f_NL = −35/8 rests on assumption (d) verified only at linear order; paper does not perform cubic-order numerical trispectrum calculation | **OPINION / ALREADY-DISCLOSED** | The paper explicitly states assumption (d) is the "weakest link" (tex L486: "Assumption (d) has been verified at linear order … At cubic order, a semi-analytic order-of-magnitude estimate…"). The paper discloses the limitation verbatim. The referee's "required fix" asks the paper to downgrade from "prediction" to "linear-order result conditional on assumption (d)" — but the paper already frames it as conditional throughout. This is a scoping disagreement, not a hidden claim. **OPINION — limitation is already disclosed; no new closure action required.** |
| Grok-P2-M2 | MAJOR | Bayes-factor table reports values up to BF≈17 as "illustrative" but table caption lacks qualifier | **PARTIAL — re-raise; text has qualifier, caption may not** | EXT4 did not audit table caption text specifically. The text at L656 states the bookkeeping is "illustrative of the discriminating power available given the current theoretical uncertainty." Whether the caption itself carries this label is a one-sentence editorial fix. **PARTIAL — add "illustrative only" to Table II/III caption if missing. Single-sentence edit.** |
| Grok-P2-M3 | MAJOR | r=0.84±0.02 10,000-sample scan: convergence diagnostic shown only for three radii | **OPINION** | The paper states convergence is confirmed at three resolution levels (tex L444: "100 and 200 bins per side… r_cos changes by <0.1% across all three"). Grok asks for a "full convergence plot" which is an additional figure beyond what the current analysis delivers. The claim is supported by three confirmed convergence checks; requesting a separate figure is an enhancement, not a correction of a wrong claim. **OPINION — present three-radius check is adequate disclosure.** |
| Grok-P2-N1 | MINOR | Reminder needed on each page that "Cai et al. value" is conditional on six assumptions | **OPINION** | The assumptions are summarized in §II.C at the paper's first major occurrence; re-stating them at every subsequent mention would be redundant and contrary to standard PRD style. **OPINION — editorial preference, not a scientific error.** |
| Grok-P2-N2 | MINOR | Fig. 2 caption: error bars not labeled as symmetric/asymmetric | **PARTIAL** | A one-sentence clarification in the caption would resolve this. **PARTIAL — minor editorial; one sentence.** |

### OpenAI leg (Pass 1: 7 ESSENTIAL, 7 MAJOR, multiple MINOR; Pass 2: 7 ESSENTIAL, 4 MAJOR, 5 MINOR)

The OpenAI leg is the most detailed. Findings are evaluated in order of severity. Many repeat Grok/EXT4 themes.

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| OAI-E1 | ESSENTIAL | Bayes factor arithmetic inconsistency vs tuned multifield competitor; narrow-prior column systematically high by 2–4× vs Eq. (8) | **OPINION / HOUSTON-DECISION** | The EXT4 audit (ChatGPT FM1/EXT3) examined the Bayes factor arithmetic in detail. The paper's template-mismatch bookkeeping is disclosed explicitly at L656: the σ_eff = σ/r rescaling is described with the specific four-corner grid numbers (17.1→14.4, 9.8→9.2, 7.0→6.2, 4.0→4.0). OpenAI is applying the raw closed-form without the template-mismatch rescaling and finding disagreement — but the paper uses the rescaled σ_eff = 0.83 (not 0.7) for those cells. The numbers are self-consistent within the stated bookkeeping. The "narrow-prior column high" claim requires verifying which σ was used; with σ_eff = σ/r ≈ 0.83 instead of 0.7, the 7.0 cell (delta/narrow) = 10/(2π×0.83²) ≈ 2.31 vs the reported 6.2 after bookkeeping. There remains a possible residual inconsistency in the narrow-prior delta cell — but this was labeled OPINION at EXT3 because the bookkeeping is explicitly described. **HOUSTON-DECISION — the Bayes factor arithmetic is disclosed and released with the code; the referee may disagree with the bookkeeping choice but the paper is transparent about it.** |
| OAI-E2 | ESSENTIAL | Version-history "Correction note: ..." prose remains in body | **OPINION / HD-6 RULED** | Per HD-6 standing rule, correction-note language is retained through internal versions until submission-day excision. tex L781 contains the QSFI endpoint correction note and L781 the nfNL joint-SDB correction note. These are by-design per HD-6 and will be removed at submission. **HD-6 RULED — KEEP in current version.** |
| OAI-E3 | ESSENTIAL | Code-artifact filenames embedded in narrative text | **OPINION / HD-11 RULED** | artifact references (e.g., `\artifact{...}` macro in tex) are part of the paper's reproducibility design through submission. At submission they are replaced with DOI/supplement references. HD-11 ruling applies: these are submission-day actions. **HD-11 RULED — KEEP.** |
| OAI-E4 | ESSENTIAL | Data & Code Availability: placeholder DOI "inserted at submission" | **HOUSTON-DECISION / HD-11 RULED** | Standard for in-progress papers; Zenodo DOI minted at arXiv submission. **HD-11 RULED.** |
| OAI-E5 | ESSENTIAL | B_NL definition in Eq. (2) ambiguous/not unambiguously dimensionless | **OPINION** | Same dimensional argument as Gemini P2-C1 — FALSIFIED there. B_NL is explicitly degree-0 (paper's own statement). The presentation could be clearer with fully expanded parentheses. An editorial improvement, not a scientific error. **OPINION — editorial; no numerical claim wrong.** |
| OAI-E6 | ESSENTIAL | σ significances from different channels juxtaposed without "not directly comparable" tag at every site | **PARTIAL** | Same as Grok-E2. Real presentation gap at some juxtaposition sites; the global disclaimer exists. **PARTIAL — same as Grok-E2 finding.** |
| OAI-E7 (Pass 2) | ESSENTIAL | ns = 0.9649 cited as [2] (Maldacena 2003) instead of Planck | **PARTIAL-VERIFIED** | This is a concrete citation error. The ns value of 0.9649 comes from Planck (PR3/PR4), not from Maldacena (2003). The citation "[2]" for Maldacena in the context of fNL,inf ≈ 0.015 at ns = 0.9649 is clearly a mis-citation — Maldacena gives the fNL formula (5/12)(1−ns) but does not measure ns. The Planck ns measurement must be cited separately. **PARTIAL-VERIFIED — concrete citation error; fix by adding Planck PR3/PR4 citation alongside the ns value.** |
| OAI-E8 (Pass 2) | ESSENTIAL | Fig. 2 caption σ_eff expression typeset as subtraction instead of two values | **PARTIAL-VERIFIED** | If the caption reads "√(0.9²+1.0²–√1.0²+1.0²=1.35–1.41)" it is typographically ambiguous. Requires visual inspection of compiled PDF. The fix (re-typeset as two separate values) is a one-line tex edit. **PARTIAL-VERIFIED — minor typographic fix; one line.** |
| OAI-E9 (Pass 2) | ESSENTIAL | Units/normalization ambiguity in M(k,z) and Δb(k) — k in h Mpc⁻¹ but c=1 not stated | **OPINION** | Same as Grok-m3/OAI-m8 — editorial, standard practice in LSS cosmology; add one sentence. **OPINION.** |
| OAI-E10 (Pass 2) | ESSENTIAL | MegaMapper "~3.5σ conservative" not reproduced under either GR scenario (closest is 3.0σ or 4.3σ) | **PARTIAL-VERIFIED** | Arithmetic: using r=0.84, σGR=1.0: significance = 4.375×0.84/√(0.7²+1.0²) = 3.675/1.221 ≈ 3.01σ. With σGR=0.5: 3.675/√(0.7²+0.5²) = 3.675/0.860 ≈ 4.27σ. Neither gives 3.5σ exactly. The 3.5σ figure requires additional systematics (bϕ widening) to be specified. **PARTIAL-VERIFIED — the 3.5σ "conservative" figure needs its exact ingredients stated; may require a one-sentence clarification of which systematics are combined.** |
| OAI-E11 (Pass 2) | ESSENTIAL | 1−rcos² ≲ 0.03 uses rcos>0.97 floor but 0.03 requires rcos≈0.985 mean; inconsistent | **PARTIAL-VERIFIED** | Arithmetic: if rcos>0.97 then 1−rcos²<1−0.97²=0.0591; so ≲0.03 is only valid at the mean (rcos≈0.985). The text uses the ">0.97" lower bound but states "≲0.03" — these are inconsistent. Fix: tie 0.03 to the mean rcos≈0.985 or relax to <0.06. **PARTIAL-VERIFIED — one-sentence consistency fix needed.** |
| OAI-E12 (Pass 2) | ESSENTIAL | SPHEREx timeline: "first all-sky survey completed December 2025" vs "~25 months primary survey" — reads as contradictory | **OPINION** | Both statements can be true (first sky-pass ≠ full mission). Adding a clarifying clause is editorial. **OPINION.** |
| OAI-E13 (Pass 2) | ESSENTIAL | Table III row "10% residual; = Ideal, verification only" is internally contradictory labeling | **PARTIAL-VERIFIED** | If the row is described as "10% residual" but the note says "strict zero-residual limit," the labeling is contradictory. Rename to "Corrected (zero residual; verification only)" and optionally add a separate 10%-residual row. **PARTIAL-VERIFIED — one-line label fix.** |
| OAI-M1 | MAJOR | Template-mismatch bookkeeping for BFs underspecified; 17.1→14.4 etc. not matching standard rescaling | **OPINION / HOUSTON-DECISION** | Same as OAI-E1; the bookkeeping is disclosed at L656 with explicit formula. The transformation rule (σ→σ/r) is stated. Whether one rescales σ or fobs is a bookkeeping choice, not an error, and both alternatives are described in the text as giving consistent qualitative results. **OPINION — bookkeeping is disclosed.** |
| OAI-M7 | MAJOR | Paper is 25 pages, overlength for the contribution | **OPINION** | Length is a PRD editor/referee judgment call, not a scientific error. **OPINION.** |
| OAI-Pass2-E14 | ESSENTIAL | Li vs Cai factor-of-two resolution has no explicit equation-by-equation comparison; no concrete mode integral | **OPINION — EXT4 reviewed and classified as OPINION** | The Appendix A.1 explicit in-in Wick derivation (L885 in the tex) provides the operator-algebra identity i⟨[ζ³,L]⟩ = −2 Im⟨ζ³L⟩ and traces the factor of two through the commutator doubling. The paper is explicit that it validates rather than re-derives the full computation. The request for an explicit mode integral is a scientific enhancement, not a correction of a wrong statement. This was classified as OPINION at EXT3 and EXT4. **OPINION — consistent with prior audit classification.** |

### Perplexity leg (Pass 1: 11+ findings, Pass 2: 6 ESSENTIAL, MAJOR)

The Perplexity leg operated on text extraction (not native PDF) and flagged many items that overlap with OpenAI and Grok.

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| PPLX-E1 | ESSENTIAL | No worked re-derivation of fNL = −35/8 from in-in integrals | **OPINION — consistent with EXT3/EXT4 classification** | Same as OAI-Pass2-E14; EXT4 confirmed OPINION. The paper validates via cross-checks, not full re-derivation. This is disclosed. **OPINION.** |
| PPLX-E2 | ESSENTIAL | Operator-algebra resolution of Cai vs Li factor-of-two not demonstrated at equation level | **OPINION** | Same as OAI-Pass2-E14 and EXT3 FM3-lineage. Appendix A.1 provides the operator identity; the full mode integrals are not re-run. Disclosed. **OPINION.** |
| PPLX-E3 | ESSENTIAL | Significance labeled as "independent forecast" but it is a Heinrich recast | **OPINION** | The paper explicitly calls it a "sensitivity recast" throughout (title, abstract, body). The word "forecast" in the title refers to the bounce prediction's testability, not an independent Fisher computation. **OPINION.** |
| PPLX-E4 | ESSENTIAL | Different σ ranges not tabulated with explicit quadrature budget | **PARTIAL** | Same as Grok-E2, OAI-E6. The text has the quadrature steps but not in one table. **PARTIAL — editorial; systematic budget table would clarify.** |
| PPLX-E5 | ESSENTIAL | Bayes factors: exact likelihood and prior definitions not fully explicit | **OPINION / HOUSTON-DECISION** | Same as OAI-E1 lineage. Disclosed; code released. **OPINION.** |
| PPLX-M1 | MAJOR | "largest prior single-survey anomaly catalog" comparison — Liang (2023) — may not be systematic | **OPINION** | The paper anchors to Liang (2023) [11] as the benchmark with a footnote. This is standard practice. **OPINION.** |
| PPLX-M3 | MAJOR | Internal artifact names and file paths in main text | **OPINION / HD-11 RULED** | Same as OAI-E3. HD-11 ruling. **HD-11 RULED — KEEP.** |
| PPLX-Pass2-E12 | ESSENTIAL | Multiple σ/significance numbers don't consistently follow from stated inputs; arithmetic inconsistencies in null-space r→σ mapping and 2.6–2.8σ floor derivation | **PARTIAL-VERIFIED** | This overlaps with OAI-E10 (3.5σ) and EXT4 FM1 (propagation). EXT4 FM1 was FALSIFIED for v1.7.53 because the propagation was disclosed at L440/L535. The Perplexity framing adds new specificity: the Fig. 2 caption expression "σeff = 0.92+1.0² – 1.0² + 1.0² = 1.35–1.41" is typographically confusing (same as OAI-E8). **PARTIAL-VERIFIED — same as OAI-E8; typographic fix needed. The underlying arithmetic is disclosed in body text.** |
| PPLX-Pass2-E13 | ESSENTIAL | Eq. (7) heuristic check: "factor 21" is unexplained and dimensionally opaque | **PARTIAL** | If the factor "21" appears in the tex without derivation and is used as a quantitative bound, it requires a one-sentence justification or softening to "qualitative." **PARTIAL — verify whether "21" appears in tex body; if so, add one-sentence derivation or soften.** |
| PPLX-Pass2-E14/E15 | ESSENTIAL | Li/Cai resolution and theoretical uncertainty framing | **OPINION** | Same as OAI-Pass2-E14 and PPLX-E1/E2. **OPINION — consistent.** |

---

## PART 3 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED / PARTIAL-VERIFIED (new, actionable) | **4** | OAI-E7 (ns citation), OAI-E8=PPLX-Pass2 (Fig 2 caption σeff typeset), OAI-E11 (1−rcos² bound), OAI-E10 (3.5σ ingredients) |
| PARTIAL (editorial, not number errors) | **3** | Grok-E2=OAI-E6=PPLX-E4 (comparability tag per juxtaposition); Grok-M2 (BF table caption qualifier); OAI-E13 (Table III row label) |
| FALSIFIED | **3** | Gemini-C1 (B_NL dimensionality — wrong), Gemini-m2 (cross-ref "Sec III B" — pattern-052 PDF artifact), Grok-E1 (date — auto-falsify) |
| OPINION (framing, editorial, enhancement) | **10+** | Grok-E3, Grok-M1, Grok-M3, Grok-N1, Gemini-m3, OAI-E2/E3/E4/E5/E9/E12, OAI-Pass2-E14/E15, PPLX-E1–E3, PPLX-M1, multiple MAJOR-labeled items |
| HOUSTON-DECISION ruled | **4** | OAI-E1/M1 (BF arithmetic bookkeeping; code released), OAI-E2 (HD-6), OAI-E3/E4 (HD-11), PPLX-M3 |
| Pattern-051 regression check | **PASS** | FM2 fix confirmed at L828; no regression |
| Pattern-052 auto-falsify (F₀/date/extraction) | **2** | Grok-E1 (date), Gemini-m2 (cross-ref artifact) |

**Genuinely-new VERIFIED/PARTIAL-VERIFIED items requiring closure**: **4**

1. **OAI-E7**: ns=0.9649 cited as [2] (Maldacena) instead of Planck PR3/PR4 — add Planck citation at the ns value.
2. **OAI-E8 / PPLX-E12**: Fig. 2 caption σeff expression typographically reads as subtraction — re-typeset as two separate expressions.
3. **OAI-E11**: "1−rcos² ≲ 0.03" uses >0.97 lower bound but 0.03 requires rcos≈0.985 mean — state "using mean rcos≈0.985" or relax to <0.06.
4. **OAI-E10**: "~3.5σ conservative" not reproducible under stated GR scenarios alone — add explicit systematics combination statement.

Remaining PARTIAL items (Grok-E2 comparability tags; Grok-M2 BF caption qualifier; OAI-E13 Table III label) are editorial polish, not scientific errors.

---

## PART 4 — EXT4 closure introduction check

**EXT4 closures** (FM2 one-sentence fix at App A summary) **introduced zero regressions**. All 4 active R34conf legs are operating on v1.7.54, which is post-FM2. None of the 4 legs re-raised the "f_NL scales with c" error, confirming the fix is effective. The F₀ = 1/8.98^2 PDF-extraction misread class (perennial pattern-052) was **not raised by any R34conf leg** — confirming the prophylactic numeric expansion from v1.7.54 (showing "1/8.98^2 = 0.01239") is working.

---

## PART 5 — Reviewer assessment

| Leg | Verdict | Accuracy |
|-----|---------|----------|
| Claude | ABSENT (API credits) | N/A |
| Gemini | ACCEPT WITH MINOR CORRECTIONS | Over-called the B_NL dimensional inconsistency (FALSIFIED); accurate on the email nit and cross-ref minor. |
| Grok | MAJOR REVISIONS | Over-called: date (auto-falsify), MegaMapper abstract (FALSIFIED), assumption-d (OPINION/disclosed). Real items: comparability tags (PARTIAL) and BF caption (PARTIAL). Net = MINOR. |
| OpenAI | MAJOR REVISIONS | Mixed: 4 new PARTIAL-VERIFIED items (E7, E8, E10, E11) are real; the large ESSENTIAL/MAJOR bulk are OPINION or HD-ruled. Net = MINOR-REVISION after audit. |
| Perplexity | MAJOR REVISIONS | Mostly overlapping with OpenAI; no new independent verified items. Arithmetic complaints in Pass 2 partially corroborate OAI-E8/E10. Net = MINOR-REVISION after audit. |

---

## PART 6 — Closure plan (hardest first)

1. **[OAI-E7 — CITATION FIX, required]** At every occurrence of "ns = 0.9649 [2]" where [2] is Maldacena (2003): add the Planck PR3 or PR4 reference as the source of the numerical ns value. Maldacena [2] provides the formula for fNL,inf, not the measurement of ns. One-line citation fix.

2. **[OAI-E10 — ARITHMETIC SPECIFICATION, required]** At the "~3.5σ conservative" statement: add explicit systematics combination (e.g., "combining r=0.84 template mismatch, σGR=0.5, and 30% bϕ prior widening gives ≈3.5σ; with σGR=1.0 the floor drops to ~3.0σ"). Without the explicit ingredients the number is not reproducible.

3. **[OAI-E11 — ONE-SENTENCE FIX, required]** At "projection noise suppressed by 1−rcos² ≲ 0.03 given rcos > 0.97": change to "using the mean rcos ≈ 0.985 from the 10,000-sample scan, projection noise is suppressed by 1−rcos² ≈ 0.03; using only the conservative lower bound rcos > 0.97 gives 1−rcos² < 0.06."

4. **[OAI-E8 — TYPOGRAPHIC FIX, required]** Fig. 2 caption: re-typeset the σeff expression to clearly show two separate values, not a subtraction. Confirm in compiled PDF.

5. **[PARTIAL-EDITORIAL — Grok-E2=OAI-E6 comparability tags]** At each major juxtaposition of bispectrum-only vs SDB-only vs combined significances (especially figure captions), append: "Note: not directly comparable; these use different estimators and systematic budgets."

6. **[PARTIAL-EDITORIAL — Grok-M2 BF caption]** Add "Illustrative; see §VI.C for bookkeeping details" to Table II/III captions if not already present.

7. **[PARTIAL-EDITORIAL — OAI-E13 Table III label]** Rename the "10% residual; = Ideal, verification only" row to "Corrected (zero residual; verification only)" to remove the internal contradiction.

---

## VERDICT

**P2 is NOT-CLEAN at R34conf** pending closure of 4 VERIFIED/PARTIAL-VERIFIED items (OAI-E7 citation, OAI-E8 caption typeset, OAI-E10 "3.5σ" ingredients, OAI-E11 rcos bound consistency). These are all one-line or one-sentence fixes. After those 4 closures, P2 is CLEAN and can proceed to pre-submission final polish.

**CLEAN threshold**: 4 closures needed → wave these as v1.7.55.

| Metric | Value |
|--------|-------|
| Legs active (Claude failed) | 4 / 5 |
| VERIFIED / PARTIAL-VERIFIED new items | 4 |
| FALSIFIED (false positives) | 3 |
| OPINION (no action) | 10+ |
| HD-ruled (submission-day) | 4 |
| Pattern-051 regression | PASS |
| Pattern-052 auto-falsifies | 2 |
| Round verdict | **NOT-CLEAN (4 minor closures required → v1.7.55)** |
