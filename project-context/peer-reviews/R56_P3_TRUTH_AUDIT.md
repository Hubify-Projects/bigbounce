# R56 P3 Truth Audit — hardened / de-biased full re-review

Paper: `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.115)
Source PDF compiled to `/tmp/R56_P3/paper3_draft.pdf` (31 pp post-fix; 0 undef refs/cites).
Vendors: OpenAI gpt-5, Gemini-2.5-pro, Grok-4 OK; Perplexity FAIL (API quota). Plus own Opus read + artifact spot-checks.

## NET VERDICT: MINOR REVISIONS (post-closure)
One genuine MAJOR (load-bearing rendering bug suppressing honest-reporting disclosures) + one genuine MINOR (internal nomenclature inconsistency) found and CLOSED. Catalog-class size is not treated as a defect. R54 Table IX fix, R55 fixes, and the v3.1.115 Gaia/eROSITA carve-out all verified intact — not re-opened.

## NEW VERIFIED FINDINGS CLOSED

### F1 — MAJOR (load-bearing rendering bug; self-favoring-presentation effect). CLOSED.
Table I (`tab:survey_summary`) note block lived INSIDE the `table*` float. A single float cannot exceed one page; the block overflowed by ~676pt ("Float too large for page" at L740) and was **silently clipped off page 7 — absent from the rendered PDF**. Confirmed via `pdftotext`: before fix, the following footnote definitions did NOT appear in the PDF at all:
- `$^\star$` Gaia DR3 reliability warning ("more than half of the published anomaly selection is training-sample-conditioned … treat as exploratory")
- `$^\#$` eROSITA membership-only disclosure
- `$^\spadesuit$` LAMOST "transparent FAIL"
- `$^\S$` IsolationForest cross-validation footnote
- `$^\diamondsuit$` Planck "neither figure is a data-driven detection rate"

Superscript markers `$^\star\,^\#\,^\heartsuit\,^\spadesuit\,^\diamondsuit$` appeared in the table with NO visible definition. Net effect: the paper's adverse, honest-reporting caveats were invisible to a PDF reader while the headline counts showed — a self-favoring presentation under the hardened bar. Same class as the EXT9 FM103-1 closure.
**Fix:** moved the `\begin{flushleft}…\end{flushleft}` note block OUT of the `table*` float to regular body text (L719–740). Recompiled ×3: 0 undef, "Float too large" GONE, all six previously-clipped footnotes now present in `pdftotext` (each ≥1×). Visual audit pp.5–9: notes flow cleanly across pp.7–8, no overlap/clipping.

### F2 — MINOR (internal inconsistency). CLOSED.
Two sites (L743 footnote, L883 body) labelled the eROSITA selection "canonical-$S$ top-298." The paper's own central eROSITA finding is that there is **no reproducible canonical-$S$ axis** for eROSITA (caption L703: 0.259 axis "distinct from the canonical $S$ of Eq. score"; released selection is the committed-raw top-298, raw threshold 3.4119). Calling it "canonical-$S$ top-298" contradicts that.
**Fix:** both sites → "committed-raw top-298 membership list" (the paper's own accurate term). PDF now shows 0 occurrences of "canonical-S top-298".

## TABLE SPOT-CHECKS (R54/R55 vigilance continued) — ALL BACKED
- **Table IX (`tab:bf_robustness`)** rows exactly match committed `bf_prior_robustness_R54.json`: [0,7] 3.23/4.52e-4/7.14e3; [0,5] 2.31/3.23e-4/7.14e3; [1,6] 2.31/3.20e-4/7.24e3; [2,5] 1.47/1.69e-4/8.69e3. R54 fabrication fix intact. γ=2.5665±0.3818 → abstract 2.567±0.382 ✓; MB +1.13σ ✓; SMBHB +4.61σ ✓.
- **DESI recount (`tab:recount`)** matches `ext3_b2_targettype_recount.json`: 190,015 clusters; 2,468@1″ / 2,531@2″ / 3,390@5″; SPECTYPE 2371 GAL / 95 QSO / 2 STAR; denom 20,299,155; control 189,675@1″ ✓.
- **Abstract arithmetic** recomputed: 378,080+200=378,280 ✓; 269,317−108,963 LAMOST split ✓; 195,829/22.5M=0.87% ✓; 2,468/2,685=0.92× ✓; 378,080/2,685=141× ✓; 44,075→2,054 = 21.5× ✓; α_jk 0.19/0.65=0.29σ ✓; 8.98→8.14 = 9.4% ✓; 77,905/12≈6500× ✓.

No fabricated/unbacked numbers found beyond F1/F2.

## RESIDUAL (noted, not closed — already-disclosed / calibration)
- NEOWISE "100% injection-recovery" wording: substance is reframed in-text as "passes by construction … masking-geometry QA, not a detector-sensitivity test." Disclosed; "recovery" vs "correct-exclusion" terminology is a borderline clarity nit, not a hidden inconsistency.
- GR-projection `|Δσ/σ|<0.02%`: explicitly labelled an internal order-of-magnitude bound, non-load-bearing. Disclosed.
- OpenAI's other ~12 "MAJOR" labels (filenames-in-body, data-availability placeholders, "catalog-grade includes exploratory"): already-disclosed (v3.1.115 carve-out intact) or stylistic; do not survive the hardened+calibration filter as genuine new findings.
- Grok "internal project log / future date / unreleased code / largest-claim unsupported": calibration over-rejection — counts/comparison are explicitly caveated; not actionable.

## SELF-FAVORING ITEM UNDER HARDENED BAR?
Yes — F1: clipped disclosures meant the rendered PDF suppressed adverse caveats while showing headline counts. Now closed; honest reporting restored.

## LEGS
OpenAI ✓, Gemini ✓ (MINOR REVISIONS, "new standard for transparency"), Grok ✓ (over-harsh), Perplexity ✗ (quota). Own Opus read + artifact spot-checks ✓.

## CONVERGENCE STATEMENT
NOT yet converged. R56 surfaced a genuine MAJOR (clipped honest-reporting disclosures) that all prior rounds missed because they checked source text, not rendered PDF — plus one MINOR. Both closed and re-verified in the recompiled PDF. One confirmation round (R57) recommended to confirm the rendering fix holds and to triage the residual NEOWISE-recovery wording; no other open BLOCKER/MAJOR.
