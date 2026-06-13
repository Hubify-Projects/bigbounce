# EXT6 P2 — External Truth-Audit (Round EXT6, in-thread delta)

**Paper**: `research/focused_paper_source_integration/02_full_draft.tex` · v1.7.57 (current); reviewers cited v1.7.55/57 PDF (paper2_fnl_forecast_v1.7.57.pdf · cb95f253)
**Reports audited**:
- `EXT6_P2_ChatGPT.md` — ChatGPT Pro Extended — **MAJOR REVISIONS, narrowly** (null-space carry-forward + 2 fresh: MegaMapper 3.5σ arithmetic, DESI ref splitting)
- `EXT6_P2_Grok.md` — Grok Heavy — **ACCEPT** (all prior MINORS closed; manuscript "pristine")
- `EXT6_P2_Gemini.md` — Gemini Thinking — **MINOR REVISIONS** (REGRESSION from EXT5 ACCEPT; 2 fresh MAJORs claimed: Eq.3 δ_e/δ_c mismatch + Table IV header corruption "fNL7/0"; 2 fresh MINORs)

**Audit date**: 2026-06-12 PT
**Protocol**: per-finding verification against `02_full_draft.tex` v1.7.57 source + math rederivation BEFORE verdict; pattern-052 auto-falsify for PDF-extraction misreads; EXT5 + R35conf TRUTH_AUDIT verdicts carried forward; arXiv 25xx/26xx dates valid; HD-6/HD-11 standing ruled; Fisher F₀ superscript 6×-falsified class.

---

## PART 1 — Pattern-051 regression check (EXT5 + R35conf closure verification)

EXT5 required FM1 (DESI DR1 current-data fix) → v1.7.56. R35conf closures (Chaussidon citation form, β=0.27° removal, 1/c scaling): all confirmed in tex changelog L27–L46. No reviewer this round raises regression on a previously-closed item. **PASS.**

---

## PART 2 — Per-finding verdict table (EXT6 fresh findings)

| # | Reviewer | Sev | Finding | Verdict | Evidence (tex) |
|---|----------|-----|---------|---------|----------------|
| **EXT6-P2-GeM1** | Gemini | MAJOR | Eq.(3) §III.A uses `δ_e` instead of `δ_c`; prose at L1728 defines `δ_c≈1.686`; index mismatch inside SDB kernel | **FALSIFIED — PDF-extraction artifact (pattern-052)** | tex L539–542: `\begin{equation} \Delta b(k,z) = \frac{2\,\fnl\,(b_1 - 1)\,\delta_c}{\mathcal{M}(k,z)}\,, \end{equation}` — equation uses `\delta_c` exactly, with the prose immediately below at L548: `$\delta_c \approx 1.686$ is the spherical-collapse threshold`. `grep "delta_e"` on the tex returns zero hits. Gemini's "δ_e" is a PDF-text-extraction misread of subscript `_c` (the c-subscript flattened to "e" in their pipeline — same OCR class as the `fAL` / `\boxed{}` artifacts of EXT4/EXT5). **VERDICT: FALSIFIED (pattern-052; 7th cumulative carry across rounds). Source is clean; no tex edit.** |
| **EXT6-P2-GeM2** | Gemini | MAJOR | Table IV final column header rendered as "fNL7/0" — string-corruption / automated-replacement collision | **FALSIFIED — PDF-extraction artifact (pattern-052)** | Table IV = `tab:dualnorm` at tex L933–943. Header row at L938 reads exactly: `Convention & $\|\fnl^{\rm bounce}\|$ & SPHEREx $\sigma(\fnl)$ & $\|\fnl\|\,r/\sigma$ \\`. Clean LaTeX, four columns. The string `fNL7/0` does not appear anywhere in the source (grep confirms). Gemini's "fNL7/0" is the PDF-extraction layer flattening `\|\fnl\|\,r/\sigma` → roman `r` mis-read as `7` and `\sigma` mis-rendered as `0` after the slash. Same pattern-052 OCR class as EXT5 GM1 (`fAL`) and EXT5 Gm3 (`\boxed`). **VERDICT: FALSIFIED (pattern-052; 8th cumulative carry).** |
| **EXT6-P2-Gem1** | Gemini | MINOR | §III.B p.8 L1759: "ranger∈ [0.829, 0.876]" — markdown/LaTeX collision flattening `range $r \in$` | **FALSIFIED — PDF-extraction artifact (pattern-052)** | tex L430: `($r \in [0.829,\,0.876]$; CMB Fisher signal-only $r = 0.876$, LSS/SPHEREx noise-weighted $r \approx 0.83$)`. Clean math mode with proper spacing. The "ranger∈" is a PDF-extraction collapse of the prose word "range" abutting `$r \in$` after Gemini's parser strips the math delimiters. Source clean. **VERDICT: FALSIFIED (pattern-052).** |
| **EXT6-P2-Gem2** | Gemini | MINOR | §IV p.9 L1794: "hMpc^{-1}" — missing thin space between h and Mpc | **FALSIFIED — PDF-extraction artifact (pattern-052)** | tex L548: `wavenumbers $k$ are comoving and quoted in $h\,\mathrm{Mpc}^{-1}$ throughout`. The `\,` thin space + `\mathrm{}` font are both present. tex L583 likewise: `$k \sim 0.01$--$0.1\,h\,\text{Mpc}^{-1}$`. Source is canonical; Gemini's parser dropped the `\,`. **VERDICT: FALSIFIED (pattern-052).** |
| **EXT6-P2-OFM1** | ChatGPT | MAJOR | §V p.10: MegaMapper conservative-significance arithmetic `4.375 × 0.84 / √(0.7² + 0.9²) ≈ 3.5σ` is wrong; actual value is 3.22σ | **VERIFIED — numerical inconsistency in tex; ≈ 3.22σ not 3.5σ** | tex L604: `4.375 \times 0.84 / \sqrt{0.7^2+0.9^2} \approx 3.5\sigma`. **REDERIVATION**: numerator = 4.375 × 0.84 = **3.675**; denominator = √(0.49 + 0.81) = √1.30 = **1.1402**; quotient = 3.675 / 1.1402 = **3.224σ ≈ 3.22σ**. ChatGPT is right: the displayed quadrature does NOT yield 3.5σ; it yields 3.22σ. R34conf had OAI-E10 CLOSED on this exact paragraph ("3.5sigma conservative carries explicit ingredients") at tex L65 changelog — the ingredients listing introduced the rounding error. This is a **pattern-051 regression** (EXT5 closure introduced fresh numerical error caught at EXT6) and **pattern-052 re-raise candidate** if not closed in v1.7.58. Severity MAJOR is appropriate (visible quantitative claim that does not match its own formula). **VERDICT: VERIFIED — closure required.** |
| **EXT6-P2-OFM2** | ChatGPT | MAJOR | §VIII.A: ref [Chaussidon2024DESIDR1fNL] is cited for BOTH the LRG `-3.6^{+9.0}_{-9.1}` AND the QSO assembly-bias `-3.3 ± 9.2`; ChatGPT asserts these are TWO separate papers (Chaussidon 2024 vs a 2026 QSO assembly-bias paper). Also requests `f_NL^bounce ≈ σ/r ≈ 11` → `σ(f_NL^bounce) ≈ σ_loc/r ≈ 11` (uncertainty, not central value); also flags un-cited 2026 DESI DR1 cross-correlation result `f_NL = 2.1^{+8.8}_{-8.3}` | **PARTIAL-VERIFIED: notation precision VERIFIED; ref-splitting OPINION-ish (citation-precision); un-cited 2026 cross-correlation OUT-OF-SCOPE for the current-data sentence** | tex L770: `DESI DR1 LRG and QSO analyses~\cite{Chaussidon2024DESIDR1fNL} report combined $f_{\rm NL}^{\rm loc}$ bounds at $\sigma \approx 9$--$10$ ($f_{\rm NL}^{\rm loc} = -3.6^{+9.0}_{-9.1}$ from the LRG sample; $f_{\rm NL}^{\rm loc} = -3.3 \pm 9.2$ from the QSO assembly-bias analysis), consistent with both bounce and inflation at current precision. Recasting via $r = 0.84$ gives $f_{\rm NL}^{\rm bounce} \approx \sigma/r \approx 11$`. (a) **Notation precision (VERIFIED, MINOR-class)**: `f_{\rm NL}^{\rm bounce} \approx \sigma/r \approx 11` is mislabeled — the expression is a recast uncertainty `σ(f_NL^bounce)`, not a central value of f_NL itself. One-character fix (`\sigma(\fnl^{\rm bounce})`). (b) **Ref-splitting (OPINION / citation-precision)**: The bib entry (L1–9 of `focused_paper_refs.bib`) folds both values into a single Chaussidon 2024 (arXiv:2411.17623) reference and the note field explicitly attributes both to that paper. Whether the QSO assembly-bias `-3.3±9.2` value is genuinely from a separate 2026 paper (as ChatGPT asserts) cannot be verified from the repo alone without an external arXiv check — this is an editorial citation-precision issue, not a numerical falsification. Lower-priority editorial. (c) **2026 cross-correlation `2.1^{+8.8}_{-8.3}`**: NEW external constraint ChatGPT raises; the paper would only need to either cite it or scope it out. OPINION / scope-preference — current text adequately conveys "current data cannot discriminate," which is the only headline conclusion. **VERDICT: SUB-FINDING (a) VERIFIED as a one-character precision fix; sub-findings (b)+(c) OPINION / editorial. Severity MAJOR is over-called for (b)+(c) but appropriate for (a) when bundled.** |
| **EXT6-P2-OFM3** | ChatGPT | MAJOR (carry-forward) | Null-space "genuine theory-modeling ambiguity" → demote to "basis-dependent representation uncertainty" | **OPINION — previously-ruled (EXT4 FM3, EXT5 FM2)** | tex L478 retains: `genuine theory-modeling ambiguity in the doubled (in-in--symmetrized) polynomial representation of the bounce bispectrum, not an artifact of an over-large basis`, followed by the explicit `Important scope of the underdetermination claim` paragraph (L478 continuation) that already labels the scatter as basis-dependent: `the quoted scatter should therefore be read as indicative of the null-space spread under this stated convention rather than as a calibrated, basis-independent uncertainty`. The paper's text accurately scopes the ambiguity. ChatGPT proposes no NEW evidence — the request is the same wording-precision demotion previously RULED OPINION at EXT4 and EXT5. Carries the same disposition: optional Houston-discretion wording change at submission, not required. **VERDICT: OPINION — third raise of the same item; previously ruled. Not a closure obligation.** |
| **EXT6-P2-Ofm1** | ChatGPT | MINOR | Fig. 5 title PDF-extraction reads `f_NL=35/8` (missing minus); rendered figure correct | **FALSIFIED — PDF-extraction artifact (pattern-052); ChatGPT self-flags this is not a scientific error** | ChatGPT explicitly states "I would not flag this as a scientific error; just ensure the source string contains the minus sign." This is the pattern-052 PDF-text-layer issue. **VERDICT: FALSIFIED at the science layer; OPTIONAL source-string check.** |
| **EXT6-P2-Ofm2** | ChatGPT | MINOR | Ref [28] formatting `JCAP arXiv:1712.09998` lacks full journal entry | **PARTIAL — editorial bib polish (HD-11-adjacent)** | Pre-submission bib polish. Standard editorial pass at journal submission. **VERDICT: PARTIAL-EDITORIAL — defer to submission-day polish; HD-11-adjacent.** |
| **EXT6-P2-Gr** | Grok | — | ACCEPT, manuscript "pristine," all prior MINORS closed | **VERIFIED — accurate verdict modulo OFM1** | Grok's pristine claim is approximately correct but misses the OFM1 MegaMapper arithmetic error. Reviewer accuracy: HIGH on closure-verification, MISSED one fresh numeric. |
| **EXT6-P2-DOI** | All | HD-11 | Zenodo DOI placeholder | **HD-11 RULED — submission-day** | Standing. KEEP. |

---

## PART 3 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED (new, actionable) | **2** | OFM1 (MegaMapper 3.5σ arithmetic → 3.22σ), OFM2(a) (σ/r=11 notation: `f_NL^bounce` → `σ(f_NL^bounce)`) |
| FALSIFIED (pattern-052 PDF-extraction) | **5** | GeM1 (Eq.3 δ_e), GeM2 (Table IV "fNL7/0"), Gem1 (ranger∈), Gem2 (hMpc^-1), Ofm1 (Fig.5 minus sign) |
| OPINION / previously-ruled / scope-preference | **3** | OFM2(b) Chaussidon ref-splitting, OFM2(c) 2026 cross-correlation, OFM3 null-space wording (3rd raise) |
| PARTIAL-EDITORIAL | **1** | Ofm2 (Ref [28] bib polish) |
| HD-RULED | **1** | DOI (HD-11) |
| Pattern-051 regression (EXT5 closure introduced new error) | **1** | OFM1 (R34conf OAI-E10 closure introduced the 3.5σ rounding artifact) |
| Pattern-052 auto-falsify cumulative carry | **5 (this round) / 13 total across EXT3–EXT6** | All Gemini fresh-MAJORs + Gemini/ChatGPT minors |

**Genuinely-new substantive (VERIFIED)**: **2** — OFM1 (MegaMapper arithmetic) + OFM2(a) (σ/r notation).

---

## PART 4 — Reviewer accuracy

| Reviewer | Verdict | Accuracy |
|----------|---------|----------|
| ChatGPT | MAJOR REVISIONS, narrowly | **Strong**: caught real numerical error (OFM1) and real notation precision (OFM2a). Over-called severity on OFM2(b)+(c) and OFM3 (carry-forward OPINION, 3rd raise). Net: 2 genuine catches out of 4 MAJORs called. Best-performing reviewer this round. |
| Grok | ACCEPT | **High closure-verification accuracy but MISSED OFM1** (visible numerical error in §V). Reviewer 3-of-3 closed all prior MINORs correctly; failed to recompute the 3.5σ arithmetic. Under-call. |
| Gemini | MINOR REVISIONS (regression from EXT5 ACCEPT) | **Low signal-to-noise this round**: both fresh MAJORs (GeM1 Eq.3 + GeM2 Table IV) are pattern-052 PDF-extraction artifacts; both MINORs likewise. Gemini's PDF-text pipeline continues to manufacture phantom errors. 4-out-of-4 fresh findings FALSIFIED. Cumulative pattern-052 contributions by Gemini across rounds: 8+. |

---

## PART 5 — Closure plan (hardest first)

1. **[OFM1 — REQUIRED, one-line numeric fix]** §V tex L604: Replace `4.375 \times 0.84 / \sqrt{0.7^2+0.9^2} \approx 3.5\sigma` with `4.375 \times 0.84 / \sqrt{0.7^2+0.9^2} \approx 3.2\sigma`, AND change the surrounding qualitative descriptor "${\sim}\,3.5\sigma$ conservative" to "${\sim}\,3.2\sigma$ conservative" in the same sentence. This is the canonical pattern-051 fix: prior closure (R34conf OAI-E10) introduced the rounding artifact that the next round caught. Bundle with a `% pattern-051 closure note: OFM1 3.5→3.2 sigma arithmetic correction (EXT6-OFM1)` in the changelog block.

2. **[OFM2(a) — REQUIRED, one-character notation fix]** §VIII.A tex L770: Replace `$f_{\rm NL}^{\rm bounce} \approx \sigma/r \approx 11$` with `$\sigma(\fnl^{\rm bounce}) \approx \sigma_{\rm loc}/r \approx 11$` (or `$\sigma(\fnl^{\rm bounce}) \approx 11$` with the explicit `σ_loc/r` derivation in prose). One-character notation precision.

3. **[OFM2(b) — OPTIONAL, citation-precision]** If Houston elects: verify whether the QSO assembly-bias `-3.3 ± 9.2` value is genuinely from Chaussidon 2024 (current bib) or from a separate later DESI 2026 paper; split the citation if separate. Lower-priority editorial; current attribution is at minimum defensible from the bib note field. PUNT to submission-day bib polish unless Houston requests pre-submission split.

4. **[OFM2(c) — OPTIONAL, scope]** Optionally add a one-line citation of the 2026 DESI DR1 cross-correlation `f_NL = 2.1^{+8.8}_{-8.3}` result. Does not change headline conclusion ("current LSS cannot discriminate"). Submission-day discretion.

5. **[OFM3, Ofm1, Gemini MAJORs/MINORs — NO TEX EDIT]** All pattern-052 PDF-extraction artifacts or previously-ruled OPINION. Source is clean.

6. **[Ofm2 — HD-11-adjacent, defer]** Bib polish at submission. KEEP.

---

## PART 6 — Pattern-051 regression analysis

**OFM1 IS a pattern-051 regression**: R34conf OAI-E10 closure required §V to list the explicit conservative-significance ingredients (`r=0.84, sigma=0.7, 30% b_phi widening->sigma~0.9; arithmetic shown.`). The closure inserted the displayed quadrature expression with a rounding error — the previous-round phrase "${\sim}\,3.5\sigma$ conservative" was retained but the now-displayed arithmetic does not produce that number. This is the third round in a row where a closure introduced or exposed a fresh numeric mismatch (cf. EXT4 OAI-M13 → R35conf; EXT5 FM1 → v1.7.56 DESI sentence rewrite → fresh `σ/r ≈ 11` notation issue at L770). Pattern-051 mitigation: every numerical closure that displays a formula MUST recompute the formula at the symbol-level before committing — even when the qualitative descriptor is preserved.

---

## VERDICT

**P2 v1.7.57 requires TWO substantive closures (OFM1 + OFM2a) to be publication-ready.** Both are mechanical: one numerical (3.5σ → 3.2σ) and one notational (`σ(f_NL^bounce)`). After v1.7.58 with these two fixes: Grok ACCEPT remains correct, Gemini's MAJORs and MINORs all falsified-pattern-052, ChatGPT's remaining items are OPINION/editorial. Net post-closure status: **CLEAN (ACCEPT)**.

| Metric | Value |
|--------|-------|
| Genuinely-new VERIFIED | **2** |
| FALSIFIED (pattern-052) | **5** |
| OPINION / previously-ruled | **3** |
| PARTIAL-EDITORIAL / HD-11 | **2** |
| Pattern-051 regression | **1 (OFM1)** |
| Pattern-052 cumulative carry across EXT3–EXT6 | **13+** |
| Round verdict | **2 required closures (OFM1, OFM2a) → v1.7.58; then CLEAN** |

---

## Reviewer-by-reviewer summary

- **Gemini → MINOR REVISIONS (regression)**: SHOULD HAVE BEEN ACCEPT. All 4 fresh findings are pattern-052 PDF-extraction artifacts. Reviewer regression from EXT5 ACCEPT is an artifact of Gemini's PDF pipeline, not a real manuscript regression. **Recommend: pin Gemini to native-PDF input only (no text-layer fallback) for next round.**
- **Grok → ACCEPT**: Closure-verification accurate; missed the OFM1 arithmetic. ACCEPT verdict is approximately correct (would be CLEAN-after-OFM1).
- **ChatGPT → MAJOR REVISIONS, narrowly**: Best reviewer this round. Caught the only two real items (OFM1 + OFM2a notation). Over-called on (b)+(c) and OFM3 carry. Net: highest signal-to-noise external reviewer for P2 across rounds.
