# EXT6 P4 — Truth-Audit (v1.0.179)

**Paper**: pipelines/p2_chirality/chirality_catalog_paper.tex @ v1.0.179
**PDF**: chirality_catalog_paper_v179.pdf (3ba688c1) · harvested 2026-06-12 PT
**Auditor**: Claude Opus 4.7
**Date**: 2026-06-12 PT
**Inputs**: EXT6_P4_{ChatGPT,Grok,Gemini}.md
**Reference**: outputs/canonical_provenance/ext4_fb1_flip_identity_qc_catalogwide.json

Verdict schema: VERIFIED · FALSIFIED · STALE · OUT-OF-SCOPE · OPINION.
Auto-falsify rules: (a) 2√3 Fisher factor re-raise without new arithmetic; (b) +3.64σ re-raise at a site already scoped pre-MASTER unless naming a NEW unscoped site; (c) version-decimal renderer collisions (e.g. "z=−18.1.34").

---

## Round summary

| Reviewer | Recommendation | Items raised | New/genuine | Re-raise | Hallucination |
|---|---|---|---|---|---|
| ChatGPT Pro Extended | MAJOR REVISIONS | 1 BLOCKER + 4 MAJOR + 4 MINOR | 1 MAJOR (provenance pin) + 1 MINOR (Fig 2 caption) | 2 (Shamir M7, +3.64σ via M6) | 0 |
| Gemini Thinking | MINOR REVISIONS | 1 MAJOR + 1 MINOR | 0 | 0 | 2 |
| Grok Heavy | ACCEPT | 1 MINOR (polish only) | 1 MINOR (eq numbering) | 0 | 0 |

**Aggregate genuinely-new**: 1 lingering MAJOR (provenance commit pin mismatch already known) + 1 MINOR (Fig 2 caption / D4 grid mislabel) + 1 MINOR (eq. (9) renumber). Zero BLOCKER. Zero re-raise of the 2√3 Fisher factor. Zero re-raise of +3.64σ at a previously-scoped site.

---

## Per-finding table

### Priority 1 — Gemini "misplaced imaging-leg paragraph in Appendix D"

| Item | Gemini MAJOR — Appendix D body interleaves a duplicated `e. Per-imaging-leg systematics` header inside the density-stratified-null paragraph; should be relocated to Appendix C |
|---|---|
| Claim | The (a–h) eight-anchor list at the head of Appendix D names (e) density-stratified null and (f) boundary-distance variance, but the body allegedly prints a duplicated `e. Per-imaging-leg systematics` block containing the BASS+MzLS +0.30σ / DECaLS +4.50σ / DES +2.46σ confidence-bin decomposition. |
| On-disk check | chirality_catalog_paper.tex line 734: anchor list reads `(a)~apodized-mask robustness, (b)~multipole-spectrum coherence, (c)~quality-quartile stratification, (d)~leg-proxy cross-power, (e)~density-stratified null, (f)~boundary-distance variance, (g)~joint nuisance-marginalized WLS template fit, (h)~direct cross-spectrum`. Body paragraphs lines 736–755 follow that order exactly: 736 (a), 739 (b), 742 (c), 745 (d "Leg-proxy ℓ=1 partial closure"), 748 (e "Density-stratified null"), 751 (f "Boundary-distance variance check"), 754 (g "Joint nuisance-marginalized WLS fit"). NO duplicated `e. Per-imaging-leg systematics` header anywhere in Appendix D body. The BASS+MzLS / DECaLS / DES per-bin decomposition lives ONLY in Appendix C line 728 (`\paragraph{Per-imaging-leg systematics.}`), which IS its proper home. The Appendix C overview at line 714 already explicitly lists "per-imaging-leg systematics" as an Appendix C anchor. |
| Verdict | **FALSIFIED** (hallucinated paragraph displacement; the structure Gemini describes does not exist in the source) |
| Closure | No action. The structure is already correct. |

### Priority 2 — ChatGPT "+3.64σ taxonomy residuals" (re-raise check)

| Item | ChatGPT carryover M6 + F179-M1 — does the paper still have unscoped +3.64σ exposure? |
|---|---|
| Claim | ChatGPT does NOT itself re-raise +3.64σ as a new BLOCKER. It explicitly marks B3 (+3.64σ vs +7.93σ taxonomy) as CLOSED, and F179-M1 is about the look-elsewhere taxonomy on the hemisphere statistic, not +3.64σ. The +3.64σ value is only referenced inside ChatGPT's own closure-verification language as already-scoped pre/post-MASTER. |
| On-disk check | Every occurrence of `+3.64\sigmaunit` (lines 184, 272, 273, 287, 469, 508, 518, 521, 532, 534, 609, 612, 637, 728, 734, 737, 785, 794, 803-area) carries explicit pre-MASTER-leakage scoping (`99.32\%` reproduction at pre-MASTER; `non-primary`, `systematics-attributed`; post-MASTER `~12\%` only and `+4.84σ` / `+5.14σ` residuals). The 500-MC vs 10⁴-permutation distinction (line 612) is now stated in the abstract too (line 184). |
| Verdict | **VERIFIED-CLOSED** (no genuinely new +3.64σ site is named by ChatGPT; pre-existing scoping is intact). No auto-falsify needed because ChatGPT did not re-raise. |
| Closure | No action. |

### Priority 3 — ChatGPT "monopole interpretation" (what is being challenged?)

| Item | ChatGPT F179-m4 — "Primary finding: a quantifiable monopole-mask leakage channel" in Conclusion VII.b can confuse readers vs the abstract's "primary scientific result is the HC real-space null plus WLS exclusion" |
|---|---|
| Claim | The Conclusion uses "Primary finding" for the leakage channel while the abstract uses it for the real-space null. ChatGPT suggests "Primary methodological finding" for the leakage channel; reserve "primary scientific result" for the null-dipole estimator hierarchy. |
| On-disk check | Abstract line 184 says "The primary scientific result is a real-space chirality dipole consistent with null". Conclusion area uses "primary finding" / "primary methodological finding" wording around the leakage channel (Sec VII.b). Verbiage is genuinely ambiguous; not a scientific challenge to the monopole-mask interpretation itself, but a labeling clarity request. |
| Verdict | **VERIFIED** (genuine readability MINOR; not a science challenge) |
| Closure | Mechanical text edit — rewrite "Primary finding" → "Primary methodological finding" in Conclusion VII.b. Defer to next restamp. |

### Priority 4 — 2√3 Fisher factor re-raise check

| Item | Did ChatGPT or Gemini re-raise the 2√3 Fisher factor? |
|---|---|
| Claim | Neither reviewer mentions the 2√3 Fisher derivation. ChatGPT B-list and F179 list do not touch it; Grok explicitly says "Fisher stands with shown arithmetic"; Gemini says nothing about it. |
| Verdict | **N/A — no re-raise**, no auto-falsify trigger. R34conf REDERIVED-CORRECT status holds. |
| Closure | No action. |

---

## Remaining items (mechanical pass)

### ChatGPT BLOCKER F179-B1 — Data Availability commit pin mismatch (v1.0.179 PDF cites v1.0.175 commit 53b41d12)

| Claim | PDF title is v1.0.179 but Data Availability says "Repository state for this version: commit 53b41d12 (v1.0.175, June 2026)". Stamp-then-pin protocol documented in the same paragraph. |
| On-disk check | chirality_catalog_paper.tex line 55 `\paperVersion{v1.0.179}`; line 165 `\paperTimestamp{June 12, 2026}`; line 803-area Data Availability literally reads `commit \texttt{53b41d12} (v1.0.175, June 2026)`. Both statements are simultaneously true on the page. ChatGPT correctly identifies the stamp-then-pin protocol but flags the journal-grade reproducibility cost. |
| Verdict | **VERIFIED** (real artifact of the stamp-then-pin two-commit protocol; not a scientific defect but is a publish-grade reproducibility concern) |
| Closure | OUT-OF-SCOPE for arXiv-stage closure (the protocol is explicit and the rendered PDF is the authoritative carrier). Pre-journal-submission action: stage one immutable v1.0.179 commit that pins its own hash + Zenodo DOI. Defer to publish-stage. |

### ChatGPT MAJOR F179-M2 — Shamir overreach (carryover M7 still open)

| Claim | "can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples" overreaches; the demonstrated mechanism is under THIS DESI/ViT-Small pipeline, not Shamir's SDSS/Ganalyzer pipeline. |
| On-disk check | Line 609 reads "The present null disfavors the Shamir ∼2–4% detection class at the amplitude level under our pipeline; a matched-footprint Ganalyzer reanalysis is required for a formal σ-level exclusion." The narrower phrasing is already partly in place. ChatGPT's specific concern targets a different passage (the "can reproduce ... SDSS-class samples" phrasing). |
| Verdict | **VERIFIED** (genuine carryover; ChatGPT's narrower-language proposal is well-targeted) |
| Closure | Mechanical text edit. Replace "can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples" → "can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required." Defer to next restamp. |

### ChatGPT MAJOR F179-M3 — WLS exact-mask equivalence not visible in paper

| Claim | The block-bootstrap result is well described, but the exact-mask equivalence assertion still lives only in JSON prose, not in a paper-level audit table. |
| On-disk check | Table IX / Appendix D.g referenced. The Table at lines 757–778 (tab:wls_fit) is the canonical WLS template fit table but does not itself contain a mask-equivalence audit row. The mask-equivalence claim is currently asserted in artifact JSON only. |
| Verdict | **VERIFIED** (genuine missing paper-level table; previously logged under EXT4–EXT5 closure waves as a transparency item) |
| Closure | Add a compact mask-equivalence audit subtable in Appendix D.g listing: canonical-mask hash, WLS-artifact mask hash, pixel-count match, in-mask spiral-count match. Defer to next restamp. |

### ChatGPT MAJOR F179-M1 — Table I LEE taxonomy still mixes max-MC vs BH/Bonferroni

| Claim | Table I mixes the direct max-statistic MC p_LEE ≤ 10⁻⁴ with Bonferroni/BH brackets without clearly subscripting the families. |
| On-disk check | Line 723 (hemisphere LEE paragraph) already explicitly states "the principled directional look-elsewhere control is the direct-MC max-statistic null itself" and the BH/Bonferroni pass is "reported only as a conservative heuristic cross-check". The hierarchy is correctly worded in prose. Table I caption is the alleged ambiguity site — ChatGPT did not quote the exact mismatched cells. |
| Verdict | **OPINION** (the prose hierarchy is in place; Table I caption could be tightened but the science is correct) |
| Closure | Defer; tighten Table I LEE caption at next restamp if desired. |

### ChatGPT MAJOR F179-M-(carryover M6) — D4-TTA spatial validation

| Claim | "still uses two ~2000-object D4 hold-outs … no spatially stratified Z2-vs-D4 comparison on the low-confidence-tail dipole estimator. … This no longer blocks the main result … but it remains a limitation." |
| Verdict | **VERIFIED-LIMITATION** (ChatGPT itself downgrades to non-blocking limitation; HC-primary estimator bypasses) |
| Closure | OUT-OF-SCOPE for arXiv (HC is primary; low-confidence tail is already explicitly systematics-attributed). |

### ChatGPT MINOR F179-m1 — Fig 2 caption says "eight D4 transforms" but figure shows Z2 production TTA

| Claim | Caption says illustrates eight D4 transforms; rendered figure shows original/flipped + raw/equivariant probability bars. Reword to "representative Z2 production TTA examples; D4 validation in Appendix B." |
| On-disk check | Fig 2 caption text not extracted into grep results — likely true at face value; consistent with paper's Z2-production / D4-validation split. |
| Verdict | **VERIFIED-LIKELY** (consistent with paper structure; caption mismatch is a low-cost mechanical fix) |
| Closure | Reword caption. Defer to next restamp. |

### ChatGPT MINOR F179-m2 — Table VII "All 8 tests pass" headline

| Claim | "All 8 tests pass" easy to quote out of context; should read "All implemented engineering checks meet their stated thresholds." |
| Verdict | **OPINION** (caveats already in place per ChatGPT's own note; pure phrasing taste) |
| Closure | Defer optional. |

### ChatGPT MINOR F179-m3 — Zenodo DOI not minted

| Verdict | **VERIFIED** (genuine, well-known; pre-journal-submission action) |
| Closure | OUT-OF-SCOPE for arXiv; gate on journal submission. |

### Gemini MINOR — "z = +7.93\sigma = the two values describe the same physical estimator"

| Claim | Trailing equal sign after σ is an accidental operator artifact. |
| On-disk check | Line 612 reads `gives $z\!=\!+7.93\sigmaunit$ --- the $500$-MC $+3.64\sigmaunit$ direct single-mode value is retained for continuity with the leakage analysis`. The character after `\sigmaunit$` is an em-dash `---`, NOT an equals sign. Gemini misread the rendered em-dash in the PDF as `=`. |
| Verdict | **FALSIFIED** (PDF renderer mis-OCR; em-dash not equals sign) |
| Closure | No action. |

### Grok MINOR — Eq. (9) for A_p renumbered relative to earlier (3)

| Claim | A_p definition equation now numbered (9) while older cross-references use (3). |
| On-disk check | Mechanical renumbering artifact from added equations; Grok proposes "formerly Eq. 3" parenthetical or normalize-to-single-label. |
| Verdict | **VERIFIED** (mechanical, low-cost) |
| Closure | Add `\label{eq:ap_def}` already exists (line 637 references `Eq.~\ref{eq:ap_def}`). Ensure all A_p references use the same `\ref`. Defer to next restamp. |

---

## Aggregate closure

| Severity | Count | Action |
|---|---|---|
| BLOCKER | 0 genuinely new (1 provenance-pin item is publish-stage, not arXiv-stage) | None for arXiv-stage. |
| MAJOR | 2 carryover (Shamir narrower-language, WLS mask-equivalence subtable) | Defer to next restamp text edit. |
| MINOR | 4 (Fig 2 caption reword, Table VII headline phrasing, Conclusion "Primary finding" → "Primary methodological finding", Eq. (9) cross-ref normalization) | Defer to next restamp text edit. |
| Falsified | 2 (Gemini misplaced-paragraph hallucination, Gemini em-dash mis-OCR) | None. |
| 2√3 Fisher re-raise | 0 | No auto-falsify trigger. |
| +3.64σ re-raise at unscoped site | 0 | No auto-falsify trigger. |

**Top closure-candidate**: Bundle Conclusion "Primary finding" → "Primary methodological finding" + Shamir narrower-language + Fig 2 caption reword + Eq. (9) cross-ref normalization as a single v1.0.180 mechanical text-edit restamp.

**Overall verdict**: Paper is **substantively clean** at v1.0.179. EXT6 produced **0 new BLOCKERS**, **0 new scientific MAJORS**, **4 phrasing MINORS**, and **2 reviewer hallucinations** (Gemini). Grok's ACCEPT recommendation is the most-aligned with on-disk reality; ChatGPT's MAJOR REVISIONS is driven mostly by the publish-stage provenance-pin protocol (acknowledged design choice, not a scientific defect); Gemini's MINOR REVISIONS rests on a hallucinated structural defect and a renderer mis-OCR.
