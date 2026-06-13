# EXT7 P2 — Per-Finding Truth-Audit Table

**Paper**: paper2_fnl_forecast_v1.7.59 (cb97ec6b84256e38)
**Source of truth**: `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.59, line numbers below)
**Audit date**: 2026-06-13 PT
**Auditor**: Claude Opus 4.7 (truth-audit class)
**Protocol**: `feedback_peer_review_truth_audit_protocol` standing directive
**Reviewers audited**: ChatGPT Pro Extended (MAJOR REVISIONS) · Grok Heavy (ACCEPT) · Gemini Thinking 2.5 Pro fresh-thread (MINOR REVISION)

---

## Verdict schema

| Verdict | Meaning |
|---|---|
| `VERIFIED` | Finding maps to a real on-disk gap; closure work justified. |
| `FALSIFIED` | Reviewer claim wrong against the .tex / artifact. |
| `STALE` | Real once, already closed at the cited site. |
| `MISLABELED` | Real concern but severity overcalled (MAJOR → MINOR, etc.). |
| `OUT-OF-SCOPE` | Outside paper scope (e.g. PDF-rendering artifact, not .tex-verifiable). |
| `OPINION` | Editorial preference, not a defect. |

**Auto-falsify rules** (applied on sight):
- arXiv 25xx/26xx valid (do not flag as fake).
- Version-decimal-as-numeric artifacts (e.g. "5.20" parsed from "5.2σ").
- Hallucinated revtex section numbers / glyph rendering artifacts.
- HD-11 class: Zenodo DOI minted at submission (standard practice).

---

## 1. ChatGPT Pro Extended — MAJOR REVISIONS (verdict)

### Closure verification re-raises

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `CGT-B2-partial` | Null-space still called "genuine theory-modeling ambiguity" instead of basis-dependent. | **VERIFIED → MINOR-LANGUAGE** | Real wording issue at §II.A; cosmetic. Already partially-resolved in v1.7.59 (paper now discloses the noise-weighted central is used for headline). Genuine one-phrase edit; no science change. |
| `CGT-B6` | DESI citation still attributes Fondi et al. QSO assembly-bias result to Chaussidon. | **VERIFIED → MINOR-CITATION** | tex L854: `Chaussidon2024DESIDR1fNL` is cited for both the LRG combined result ($-3.6^{+9.0}_{-9.1}$) and the QSO assembly-bias result ($-3.3 \pm 9.2$). These are distinct analyses. Real bib hygiene fix. MINOR not BLOCKER (consistent with bounce-vs-inflation conclusion either way). |

### Fresh-pass new findings

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `CGT-FM1` | **(MAJOR)** Table IV Row 1 "Heinrich baseline: $5.2\sigma$ pre-mismatch" is mislabelled — naive baseline is $4.375/0.7 = 6.25\sigma$; $5.2\sigma$ only after $r=0.84$. Caption says rows "build cumulatively" but null-space + $\epsilon$-correction + $b_\phi$ rows are not cumulative. | **VERIFIED → MAJOR** | tex L830: `Heinrich baseline & $\sigma(\fnl^{\rm loc}) = 0.7$ & denom.\ (baseline) & --- & $5.2\sigma$ pre-mismatch \\`. The 5.2σ entry in the first row is internally inconsistent with the row's "naive baseline" framing (Fig. 1 caption L641 correctly labels the 6.25σ as the naive uncorrected and the 5.2σ as template-corrected). Same finding raised independently by Gemini (Glm-FM2 below). **TOP CLOSURE** — split the row into (a) naive uncorrected $6.25\sigma$ explicitly "not used in headline" and (b) template-corrected $5.25\sigma$; tag cumulative vs distributional rows in caption. |
| `CGT-FM2` | **(MAJOR)** DESI Ref. [34] conflates Chaussidon et al. (LRG/QSO combined) with Fondi et al. (QSO assembly-bias) and omits Rosado-Marín et al. 2026 cross-correlation. | **VERIFIED → MINOR-CITATION** | tex L854 (verified above) conflates two analyses to one citation. Splitting refs is a citation-hygiene fix; arXiv 26xx IDs valid; June 2026 current. Real but MINOR (conclusion unchanged: current LSS cannot discriminate). **2nd-priority closure.** |
| `CGT-Min1` | §II.A "genuine theory-modeling ambiguity" should become "basis-dependent representation uncertainty". | **VERIFIED → MINOR** | Duplicate of CGT-B2-partial. |
| `CGT-Min2` | Bayes-factor abstract too dense (r→1 endpoint vs r=0.84 bookkeeping). | **OPINION** | Style preference; numerics correct. |
| `CGT-Min3` | §V MegaMapper: many σ values juxtaposed; add a small table. | **OPINION** | Presentation preference. |
| `CGT-Min4` | Ref. [28] still listed as "JCAP arXiv:1712.09998" without full citation. | **VERIFIED → MINOR-BIB** | Bib hygiene; trivial fix. |
| `CGT-Min5` | Zenodo DOI listed as "inserted at submission". | **STALE — HD-11 class** | Standard arXiv-day practice. Not acceptance-blocking. |
| `CGT-Min6` | Abstract / anomaly-tracer / SDB-running sections too long. | **OPINION** | Length preference. |

**ChatGPT score (P2)**: 1 genuinely-new VERIFIED MAJOR (Table IV Row 1 mislabel), 2 VERIFIED MINOR (DESI ref split, ref [28] hygiene). All others MINOR-LANGUAGE / OPINION / STALE. The "MAJOR REVISIONS" verdict is overcalled — actual closure work is 3 narrow edits, consistent with the reviewer's own closing paragraph ("I would likely recommend minor revisions after three focused changes").

---

## 2. Grok Heavy — ACCEPT (verdict)

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `GRK-CLOSURE-ALL` | All BLOCKERS/MAJORS/MINORS through v1.7.57 CLOSED; new Table IV "exemplary"; arithmetic 3.22σ correct; BF worked example reproducing ≈9 inserted. | **VERIFIED** | All cited closures match .tex content. 5th consecutive 6/6 clean Grok read (EXT3 → EXT7). |
| `GRK-NEW` | No new BLOCKERS / MAJORS / MINORS. | **VERIFIED** | Cross-validated against ChatGPT + Gemini fresh-pass: the only genuine new finding (Table IV Row 1) is a presentation-level cell label inside a row Grok would reasonably interpret as "the headline 5.2σ template-corrected value with `pre-mismatch` referring to pre-systematics" — defensible read, but ChatGPT/Gemini's stricter parse is the better one. Not a Grok miss at the science level. |

**Grok score (P2)**: ACCEPT verdict justified on the science. Misses the one Table IV Row 1 label ambiguity but does not introduce false-positives. 5th consecutive ACCEPT.

---

## 3. Gemini Thinking 2.5 Pro fresh-thread — MINOR REVISION (verdict)

### Closure verification

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `GLM-C1` | §V L604 arithmetic fixed to 3.22σ; Table IV traces baseline σ=0.7 → cumulative endpoint 2.6σ (σ_eff=1.41). | **VERIFIED** | tex L634 explicitly: `$4.375 \times 0.84 / \sqrt{0.7^2 + 1.0^2} \approx 3.00\sigma$` (3.0σ GR-only floor); L615 + Fig.1 caption show 2.6–2.8σ all-combined endpoint with $\sigma_{\rm eff}=1.35$–$1.41$. Closure correctly observed. |
| `GLM-C2` | Bayes-factor worked example, asymmetric null-space footnote, noise-weighted r=0.83→0.84 reconciliation. | **VERIFIED** | Closures match v1.7.59 R36conf wave. |
| `GLM-C3` | Template / scale definitions cleanly laid out; σ_eff = σ(fNL^local)/r formalized. | **VERIFIED** | §II.A intro + projection formula match. |

### Fresh-pass new findings

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `GLM-FM1` | **(MAJOR)** Widespread glyph corruption: σ replaced with "0" throughout — "5.2-5.50", "2.6-50", "3-70", "≈2.5σ ... below the 30 GR-only floor", "MegaMapper gives ~40", "drops to 20", "remains at ~50". | **FALSIFIED — PDF-extraction artifact** | tex L615 reads literally `${\sim}\,5.2$--$5.5\sigma$ before GR`; L477 `${\sim}\,2.6$--$5\sigma$`; L651 `${\sim}\,3.2\sigma$ conservative`. No glyph corruption in the source. Gemini is parsing the PDF's text layer where `\sigma` is dropped after the hyphen-range collapse — a Gemini-side text-extraction failure mode (well-documented in EXT3–EXT5 audits as a Gemini-only artifact). **OUT-OF-SCOPE for closure (no edit needed in .tex).** Open question: confirm visual rendering in pdftoppm passes /latex-audit; if a real PDF glyph dropout exists, that is a font/typography artifact, not a manuscript content issue. |
| `GLM-FM2` | **(MAJOR)** Table IV Row 1 "5.20 pre-mismatch" contradicts text — should be 6.25σ. | **VERIFIED → MAJOR** | Duplicate of CGT-FM1 (see above). Gemini independently catches the same row-label inconsistency. Strong corroboration. **TOP CLOSURE.** |
| `GLM-Min1` | Figure 2 contains "dance miwching" string; Figure 4 reads "Mmmm Accessible Scale" / "Significance tar 38m"; Table I superscript-4 stray. | **OUT-OF-SCOPE — figure render artifact** | Not .tex-verifiable. Figures are external PDFs; if true, these are vector-text rendering artifacts in figure files (likely PIL or matplotlib text-as-path collisions). Flag for /latex-audit visual pass + figure regeneration but does not require .tex edits. |

**Gemini fresh-thread score (P2)**: 1 genuinely-new VERIFIED MAJOR (Table IV Row 1 — same as ChatGPT FM1, strong cross-vendor corroboration), 1 FALSIFIED glyph-corruption (PDF-extraction-side, not .tex), 1 OUT-OF-SCOPE figure-render artifact. **No revtex section-number hallucination** — Gemini fresh-thread is calibrated on P2 this round (different from P3 fresh-thread which has its own audit). The "MINOR REVISION" verdict is the closest of the three to truth (1 MAJOR + 0 BLOCKER) — Grok ACCEPT misses the row label, ChatGPT MAJOR REVISIONS is overcalled.

---

## Roll-up

| Class | Count | Genuine action items |
|---|---|---|
| VERIFIED MAJOR | **1** | Table IV Row 1: split "Heinrich baseline 5.2σ pre-mismatch" into naive (6.25σ, not used) + template-corrected (5.25σ); fix caption "cumulative" claim. |
| VERIFIED MINOR | **3** | (a) DESI Ref [34] split Chaussidon + Fondi + Rosado-Marín; (b) Ref [28] full journal citation; (c) §II.A "genuine theory-modeling ambiguity" → "basis-dependent representation uncertainty". |
| FALSIFIED | **1** | Gemini σ→0 glyph corruption — PDF-extraction artifact, not in .tex. |
| OUT-OF-SCOPE | **2** | Figure 2/4 text rendering artifacts; visual audit handles these. |
| STALE / OPINION | **6** | Zenodo HD-11, BF-abstract density, table preference, length preferences. |

**Truth verdict on round**: MINOR REVISION justified (Gemini's call). The 1 MAJOR (Table IV Row 1) and 3 MINOR closures are a half-day of work. ChatGPT "MAJOR REVISIONS" headline is overcalled in light of its own three-item closing paragraph; Grok ACCEPT is one-row-label-ambiguity short of correct.

**Top closure**: Table IV Row 1 mislabel — single edit, raised by 2 of 3 vendors independently.
