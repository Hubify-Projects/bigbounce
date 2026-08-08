# R55 P3 — Truth Audit (convergence-confirmation)

**Date:** 2026-06-26
**Paper:** P3 — Multi-Survey Spectral Anomaly Detection (`pipelines/p3_anomaly_engine/paper3_draft.tex`, v3.1.113, 30pp)
**Round:** R55 — convergence-confirmation after R52/R53/R54 + EXT21/22
**Source PDF:** `/tmp/R55_P3/paper3_draft.pdf` md5=120624c4 (pre-fix)
**Reviewers:** Anthropic Opus (this audit, Claude Code subagent) + OpenAI gpt-5 (methodology) + Gemini 2.5-pro (cosmology) + Grok-4.3 (adversarial/figures). Perplexity FAILED (API quota 401, fallback also failed) — citation leg unavailable.

Verdict-first. Patterns 061/062/063/064 + calibration applied. Arithmetic recomputed before any VERIFIED/FALSIFIED label.

---

## NET VERDICT

**Substantially converged. Zero fabrication, zero new BLOCKER/MAJOR, R54 Table IX fix intact.** Two genuine but cosmetic/MINOR-NIT arithmetic defects survived to R55, both recomputed and CLOSED in-round (DO-NOW, neither changes a science result). All three PDF-capable vendors return MAJOR-REVISIONS, but every ESSENTIAL/MAJOR they raise is a **pre-disclosed methodological/editorial caveat already explicit in the paper** (Planck train/test overlap, eROSITA irreproducible score axis, "catalog-grade" tier labeling, scaler leakage, "largest" claim, reproducibility placeholders, page length) — not falsifications, not new defects. Truth-audit verdicts: OPINION / STALE-N/A / already-disclosed.

## R54 TABLE IX FIX — VERIFIED INTACT (not re-opened)

All 12 cells of Table IX (`tab:bf_robustness`) match `bf_prior_robustness_R54.json` exactly:
- [0,7] B_MB/free 3.23 (json 3.2276), B_SMBHB/free 4.52e-4 (4.522e-4), B_MB/SMBHB 7.14e3 (7137.6)
- [0,5] 2.31/3.23e-4/7.14e3 (json 2.3054/3.2299e-4/7137.6)
- [1,6] 2.31/3.20e-4/7.24e3 (json 2.3127/3.1955e-4/7237.4)
- [2,5] 1.47/1.69e-4/8.69e3 (json 1.4659/1.6875e-4/8687.2)

Fiducial row reproduces `savage_dickey_2026-05-29.json` exactly (post_mb 0.46108, B_MB/SMBHB 7137.6). γ marginal 2.567±0.382, z-distances +1.13σ / +4.61σ confirmed. R54 fix VERIFIED, untouched.

## TABLE/NUMBER SPOT-CHECK (extra diligence, R54-style) — ALL BACKED

1. **Table I survey summary** — native per-survey sum 195,829+77,905+113,342+298+200+500+419 = **388,493** ✓; dedup 388,493−10,213 = **378,280** (2.629% compression) ✓; point-source 378,080+200 = 378,280 ✓; catalog-grade 269,317+108,963(LAMOST) = 378,280 ✓; cross-transfer 319,243+200(ACT) = 319,443 ✓; SDSS 77,905=4.05% of 1,925,279 ✓; LAMOST 113,342=1% of 11,334,161 ✓; eROSITA IF 284/298=95.3% ✓, 7582/9303=81.5% ✓; Gaia 2048/5000=41.0% ✓.
2. **Table IX bf_robustness** — backed exactly by committed JSON (above).
3. **Sensitivity Table X + Fisher** — F0=1/(8.98)²=0.01239 ✓; central σ=1/√(0.01239+0.0747·0.19²)=8.14 ✓; envelope [3.92,8.98] (α=0.84→3.92; clip→8.98) ✓; de-bias max(0,0.0361−0.4225)=0 ✓; sensitivity table internally consistent linear-scaling reference (imp≈40.7α %), explicitly labeled non-primary; α-grid {5.67,8.98,5.67,3.39,2.35} backed by `r43_4caveats_closure/result.json` ✓.
4. **Dedup cluster accounting** — committed size histogram sums to 9,553 clusters and Σ(size−1)=**10,213** collapsed detections exactly ✓; 637 cross-survey + 9,576 intra = 10,213 ✓; SDSS-swap reproduces 320,020 (19,253 slice) and 301,034 (S>5, 12 rows) ✓; radius sweep 0.086% ✓ (`r23conf_dedup_audits.json`).
5. **Spatial/NEOWISE** — Cramér V √(376713/(378280·24048))=0.0064 ✓; NEOWISE 17/436=3.9%, 2.6× over 1.52% null, binomial z≈4.0 ✓; R39conf fixes (dust p=0.35, F0, α̂², Cramér sqrt) all intact.

**Conclusion: no fabricated or unbacked numbers found.** Every load-bearing scalar is reproducible from a committed artifact or internally self-consistent. OpenAI's independent arithmetic audit (its "Numerical/consistency audit summary") independently re-derived the same set and reported all VERIFIED — concordant with this audit.

---

## NEW VERIFIED DEFECTS CLOSED IN-ROUND (DO-NOW, recomputed)

**R55-P3-1 (FALSIFIED→CLOSED, NIT-arithmetic). Fig 5 (`fig:neowise_top`, L910) cutout angular size wrong.**
- Was: "256 × 256 pixels ($108'' \times 108''$)". Recompute: LS DR9 scale 0.262″/px (used consistently elsewhere — 128px→33.5″ at L818/L1335) gives 256 × 0.262 = **67.07″**, not 108″. 108″ implies 0.422″/px ≠ LS DR9.
- Fix: → "256 × 256 pixels at the native LS DR9 scale of 0.262″/px (256 × 0.262″ = 67″ per side)." Source: OpenAI P3-M6 (pass-2 self-critique). Verified by recomputation; renders correctly post-recompile. No science impact (display cutout size only).

**R55-P3-2 (FALSIFIED→CLOSED, MINOR-consistency). Cramér's V denominator off-by-one (L967).**
- Was: V = √(χ²/(N·(k−1))) = √(376713/(378280 × **24,047**)). Stated dof = 24,048 and k = 24,049 occupied pixels ⇒ (k−1) = 24,048. The 24,047 is the *dust-correlation* t-test df (N−2 = 24,049−2) cross-contaminated into the V denominator.
- Fix: 24,047 → **24,048** (matches stated dof and the (k−1) formula). Recomputed V = √(376713/(378280·24048)) = 0.006435 → **0.0064 unchanged**. Source: OpenAI P3-n5. No value impact; internal-consistency fix.

## VENDOR ESSENTIALS/MAJORS — TRUTH-AUDIT DISPOSITION (no closure; pre-disclosed)

| Finding | Verdict | Reason |
|---|---|---|
| OpenAI E2 / Gemini M1 Planck train/test overlap | OPINION / disclosed | Paper explicitly states scoring includes training patches + over-representation check; listed as caveat. Re-run is a research preference, not a fabrication. |
| OpenAI E3 / Gemini M2 eROSITA irreproducible 0.259 axis | disclosed | Abstract + §erosita + Table I footnote # already state membership-only, score axis non-reproducible (16 rescalings). |
| OpenAI E4/M3 "catalog-grade" includes exploratory | OPINION | 269,317 tier explicitly carries per-object exploratory validity flags; naming preference. |
| OpenAI E6/Gemini m2 scaler full-sample leakage | disclosed | eROSITA bounded (15–17% tail churn); NEOWISE/Gaia disclosed as queued. |
| OpenAI E7/Grok M2 "largest" claim | OPINION | Hedged "of which we are aware"; benchmark anchored to Liang2023. |
| OpenAI E1/E5 reproducibility placeholders / internal paths | editorial | arXiv-prep cleanup, not a science defect. |
| Grok E1/E2/M3 f_NL 9.4% + NANOGrav "decisive" overstated | OPINION / over-mitigated | Every occurrence already says "consistent with zero / not a detection"; environmental SMBHB caveat present in abstract, §nanograv, conclusions. |
| Grok N1 date line "June 19 2026" | N/A | Intentional `\date{}` version stamp. |
| Gemini E1 Table I layout confusing | OPINION | Presentation preference; numbers verified correct. |
| OpenAI n6 "2.3 vs 2.75" coincidence | not-a-defect | Two distinct estimators (2.3 analytic uniform-density, 2.75 empirical RA-shifted), both disclosed. |

None rise to FALSIFIED. These are recurring referee preferences the paper already addresses by explicit disclosure (catalog-class transparency stance).

---

## COMPILE / OVERFLOW

- pdflatex ×3 (post-fix): exit 0, **0 undefined references/citations**, 30 pages.
- Overflow audit: **1 overfull hbox, 4.68pt (<5pt threshold), in Table IX alignment L1381–1388 — pre-existing, sub-threshold, unrelated to R55 edits (text-only).** 84 underfull hboxes are spacing-only (not overflow). 0 overfull vbox. PASS.
- Both edits verified rendered via pdftotext (108″ gone; 24,048 consistent).

## CONVERGENCE STATEMENT

P3 is **CONVERGED on science content**: zero fabrication across a full R54-style spot-check of all major tables and the dedup accounting, R54 Table IX fix intact and exact, all headline numbers backed by committed artifacts. R55 surfaced only two cosmetic arithmetic defects (one wrong figure-caption angular size, one off-by-one in a Cramér denominator with zero value impact), both recomputed and closed in-round. Remaining vendor MAJORs are pre-disclosed methodological caveats / referee preferences, not defects. Recommend: one more confirmatory cross-vendor round expected to return convergent silence on arithmetic; outstanding items are editorial (arXiv-prep path cleanup, optional length reduction) and research-preference (held-out Planck re-run), tracked as documented caveats — none block. **Do NOT bump/mirror this round (per directive).**
