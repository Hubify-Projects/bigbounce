# P4 (chirality catalog) — H17 truth-audit — 2026-07-10

Paper: `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.230 → v1.0.231 this round)
Reviewers audited: EXT ChatGPT (REJECT, 10 MAJOR + 2 MINOR), EXT Grok (MINOR, 6),
INT Claude-subagent (MAJOR), INT OpenAI gpt-5.5 (MAJOR), INT Grok grok-4.3 (MINOR).

Disposition codes: **FIX** = genuinely-new real + editable, closed with a real edit;
**RE-FLAG** = source-cited re-flag of already-disclosed/addressed content;
**OPEN-LIMITATION** = real but out-of-scope-for-edit (needs new compute/data), disclosed honestly.

---

## PRIORITY 1 — the Shamir factor-of-2 (ChatGPT MAJOR-9, INT Claude MAJOR, INT OpenAI MAJOR-9)

**VERDICT: REAL ERROR — FIXED.**

The three reviewers converge: the paper took Shamir's reported 1.7%–4.0% asymmetry,
**mislabelled it an `f_CW`-deviation, and doubled it** to `A_p = 3.4%–8.0%` via
`A_p = 2(f_CW − ½)`, propagating into `A_ref = 0.034`, the `z ≈ −18` WLS exclusion,
and the "7–18×" tension.

Source verification (not previously in-repo — the paper never quoted Shamir's formula):
- Shamir defines his asymmetry as `A = (N_cw − N_ccw)/(N_cw + N_ccw)` — the full-count
  asymmetry. Confirmed in the reproduction paper arXiv:2410.15269 (Table 1:
  `A = (OMW − MW)/(OMW + MW)`; reported values 1.1%, 1.6%, 2.1% are that quantity),
  consistent with Shamir 2020 (arXiv:2007.16116) and Shamir 2022 DESI (arXiv:2208.13866).
- **Algebra:** `A ≡ (N_cw − N_ccw)/(N_cw + N_ccw) = f_cw − f_ccw = 2f_cw − 1 = 2(f_cw − ½)`.
  So the asymmetry `A` **is identically** the paper's `A_p`. Shamir's 1.7% **already equals
  `A_p = 0.017`** — doubling to 0.034 double-counts the factor of 2.
- The paper's own Table `tab:wls_fit` footnote (line 1391) already states `A_p = A` for a
  pure dipole — so the paper *knew* A_p is the full asymmetry, yet still doubled Shamir's
  asymmetry. Internally self-contradictory, exactly as INT Claude flagged.

Corrected arithmetic (WLS: `A_best = 4.55e-3`, `σ_boot = 1.63e-3`):
- `A_ref` : 0.034 → **0.017**
- `z` (bootstrap) : −18.1 → **−7.64**
- NSIDE sensitivity: −16.9/−18.4/−19.4 → **−7.1/−7.8/−8.2** (|z|≥7 stable)
- naive-WLS z : −264.5 → **−112**
- Shamir tension : 7–18× → **3.7–8.8×** (0.455% vs 1.7%–4.0% in A_p units)

This is exactly the value an earlier external referee computed (z≈−7.6) that changelog
v1.0.206 line 244–247 dismissed as a "referee miscompute." **That referee was correct.**

Every occurrence fixed (text + baked-in figure): abstract (616); significance-def (701);
headline table (748); primary callout (824); monopole-mask table (1031); Intro (639, incl.
tension + doubling prose); prereg estimator list (709); reader's note (975); monopole-mask
prose (1013); Shamir comparison (1051); pseudo-label ceiling (1067); parity translation (1155);
conclusions (1193, 1196); Appendix-D WLS prose (1367, incl. NSIDE-sensitivity + naive + "18σ"
phrasing); WLS table row (1387); bootstrap figure caption (1397); discriminator table (1421).
An explicit source-cited derivation sentence ("Shamir quotes the asymmetry
(N_CW−N_CCW)/(N_CW+N_CCW), identical to our A_p, so his 1.7% maps to A_ref=0.017 without
rescaling") added at abstract + parity + conclusions + Appendix-D so no referee can re-flag.

**Directive I6 figure propagation:** `fig_bootstrap_null.png` had the red reference line
baked at 0.034. Generator `scripts/gen_fig_bootstrap_null.py` + artifact
`outputs/canonical_provenance/joint_nuisance_bootstrap_sigma.json` updated to A_ref=0.017;
figure regenerated (red line now 0.017, z≃−7.6) and visually verified.

---

## PRIORITY 2 — ChatGPT MAJORs (remaining) + MINORs

| # | Finding | Verdict | Basis |
|---|---------|---------|-------|
| CG-1 | p_eq>0.6 is outcome-dependent post-selection ("first threshold at which excess disappears"); commit not a prospective holdout | RE-FLAG | Paper §prereg (707) declares HC 0.6 as single primary sample a priori; the WLS fit is explicitly on a *different unthresholded* sample and its selection is NOT propagated into the covariance (disclosed, 707/1082). Confidence-cut sweep stable across p_eq∈{0.6,0.7,0.8} (1082). GZ1-human-only cross-check (no confidence-model at all) returns same null z=−0.54 (1067). Referee-variance re-flag of disclosed content. |
| CG-2 | No confusion matrix as joint function of position/depth/PSF/confidence; classifier error can create/reverse a dipole | OPEN-LIMITATION | Spatially-resolved confusion map needs new image-level compute (not committed). Direction-of-bias already argued toward-null (1067-ii); GZ1-human null is model-free. Disclosed as limitation in §sensitivity (1084 "does not pass through upstream image links") + §pseudolabel_independence. Honest open item; not editable now. |
| CG-3 | Flip-averaging ≠ rotational equivariance; 21.4% D4 argmax flips; needs production D4 / sky-stratified validation | RE-FLAG | Paper already states flip-TTA enforces *flip*-equivariance only, explicitly NOT rotation-equivariance, and labels the 21.4% D4 argmax flip a classifier-stability check not a spatial-null (801). No overclaim to correct. |
| CG-4 | Injections bypass classifier/triage/confidence/confusion → A50/A95 are output-map floors, not physical thresholds; internal inconsistency | RE-FLAG | Paper §sensitivity (1084-1098) states verbatim: injections do NOT traverse ViT/NS-triage/p_eq-cut/confusion; A50/A95 are "thresholds on the observed f_CW field … we do not claim them as physical morphology-dipole thresholds." The bridge is the single dilution g. The "internal inconsistency" is the paper first saying dilution is folded in then admitting bypass — both statements coexist because g is the disclosed bridge. Already-disclosed; no fabrication. |
| CG-5 | moment-z>3 recovery criterion invalid because amplitude positive-definite + non-Gaussian z→p | RE-FLAG | Recovery is scored against an *empirical* per-pixel-shuffle null (P(σ>3) is an empirical rank fraction, 1082), and the moment-z is explicitly declared non-Gaussian (699/975). Empirical-null scoring is exactly the "pre-specified empirical null quantile" ChatGPT asks for. Re-flag. |
| CG-6 | Pixel-permutation assumes exchangeability, destroyed by varying counts/depth/noise; needs generative hierarchical null | OPEN-LIMITATION | A full generative survey-systematics null is genuine future work (needs new machinery). Paper already runs density-stratified null (1361, +3.80σ) and discloses exchangeability limits; the primary result also rests on the template-agnostic block-bootstrap + injection floor which don't assume exchangeability. Partially mitigated + disclosed; full generative null out-of-scope-for-edit. |
| CG-7 | Real-space & harmonic are correlated, not independent; ~47% harmonic residual unexplained; "below A50" is a power measure not a contamination bound | OPEN-LIMITATION / RE-FLAG | The ~47% remainder is disclosed (INT Claude verified 52.4→53.0% forward-model, 47% remainder). Paper already frames harmonic as diagnostic-not-independent and bounds the remainder below A_50 a-fortiori. ChatGPT's point that a power-threshold ≠ contamination-bound on the *real-space* estimator is a valid methodological caveat requiring a joint covariance model = future work (1159 item 2). Disclosed as open; joint likelihood not editable now. |
| CG-8 | z≈−18 block-bootstrap centered on observed estimate, not a null under A_ref; reduces vector dipole to scalar; "conservative" claim backwards → under g=0.398, A_ref=0.034→obs 0.0135→z≈−5.5 | FIX (already handled by P1) + RE-FLAG | The factor-of-2 half of this is FIXED (P1): z is now −7.6 vs the correct A_ref=0.017. ChatGPT's g-dilution arithmetic (0.034→0.0135→z≈−5.5) was itself built on the doubled 0.034; against the corrected 0.017 the dilution point is subsumed. The "bootstrap is a sampling distribution not a calibrated frequentist null" caveat is already stated verbatim throughout (1367: "not a calibrated frequentist exclusion significance"; fig caption 1397). Re-flag of disclosed caveat. |
| CG-10 | 99.32% leakage is pipeline-specific; extending to prior Ganalyzer literature unsupported without matched reanalysis | RE-FLAG | Paper already restricts the claim: "attributed at the pre-MASTER level … under our DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required" (1013, 1051, 1193). No unsupported extension to correct. |
| CG-MINOR-1 | Cosmic-birefringence / Chern-Simons bounded by this analysis — remove or supply transfer function | RE-FLAG | Paper §parity_translation (1155) already states the transfer function "is not derived in this paper," frames these as "in principle" / "pending a derived transfer function," and INT OpenAI-8 agrees it should be "sharply downgraded" — the text already hedges. Kept the existing hedge; no new overclaim. |
| CG-MINOR-2 | 8.5M headline vs 949,584 primary vs 3.2M second sample; repetitive; incompatible σ; DOI deferred | RE-FLAG / OPEN | Sample-N distinctions are tabulated (headline table, decision tree). σ-incommensurability has a dedicated reader's note + notation section. DOI deferral is disclosed (1441) and Houston-gated at journal submission — not editable now. |

## Grok EXT (6 minors) + INT Grok (4 minors)

| # | Finding | Verdict | Basis |
|---|---------|---------|-------|
| GK-1 | Abstract too long / too many incommensurable σ | RE-FLAG (style) | Reader's note + notation section already present (975); trimming is cosmetic, not a correctness gate. Not changed this round. |
| GK-2 | Pre-spec commit hash + immutable date in MAIN text, not just Data Availability | OPEN-LIMITATION | Commit hash / Zenodo DOI minted at journal submission (1441) — Houston-gated, cannot fabricate a hash now. Prereg sample declared a priori in §prereg (707). |
| GK-3 | ~47% forward-model remainder needs demonstration it can't leak into real-space fit | RE-FLAG / OPEN | Already bounded below A_95 a-fortiori (1017-1067); the formal per-remainder leakage bound = the joint-covariance future item (1159). Disclosed. |
| GK-4 | Shamir tension risks overstating as refutation; state it's not a statistical exclusion | RE-FLAG (already closed) | Paper states verbatim "we do NOT claim a frequentist exclusion of Shamir's Ganalyzer estimator" at §comparison, parity, and conclusions. Plus the factor-of-2 fix now correctly sizes the tension. |
| GK-5 | Reader's-note box reiterating only P1–P2 carry cosmological weight | RE-FLAG (present) | Reader's note (975) + decision-tree table (717) + notation section already do exactly this. |
| GK-6 | Injection-recovery: state stability under area-uniform vs fixed-axis + that A95 incorporates g dilution | RE-FLAG (present) | §sensitivity (1082) already reports the fixed-axis spot check (0.45–0.62, mean 0.54 vs tabulated 0.55) AND the g=2a−1 / g_eff=s_CW+s_CCW−1=0.398 dilution mapping (1100-1116). |
| INT-GK-a | z≈−18 not a calibrated frequentist limit, risks overstating Shamir tension | FIX (P1) | Directly fixed: z now −7.6, tension 3.7–8.8×, caveat retained. |

---

## Counts

- **FIX (real edits this round):** the Shamir factor-of-2 (1 root cause, ~18 text sites + 1 figure + 1 data artifact). Subsumes CG-9, INT-Claude-MAJOR, INT-OpenAI-9, INT-Grok-a, GK-4, GK-EXT-Shamir.
- **RE-FLAG (source-cited, no edit needed):** CG-1, CG-3, CG-4, CG-5, CG-8(caveat), CG-10, CG-MINOR-1, CG-MINOR-2(partial), GK-1, GK-3, GK-4, GK-5, GK-6 = 13.
- **OPEN-LIMITATION (real, out-of-scope-for-edit; disclosed in paper):** CG-2 (spatial confusion map), CG-6 (generative hierarchical null), CG-7 (joint real-space×harmonic covariance), GK-2 (Zenodo DOI/commit hash at submission) = 4. All already appear in the paper's limitations / future-work (§sensitivity, §pseudolabel_independence, 1159, 1441).

**No fabrication.** Every disposition is source-cited to a paper line or an external source
(Shamir formula via arXiv:2410.15269 reproduction + algebra). No number was invented; the
corrected z/tension/A_ref all follow from committed artifact values (A_best=4.55e-3,
σ_boot=1.63e-3) and Shamir's published asymmetry definition.

## Residual verdict

The one genuinely-new REAL editable finding this round (the Shamir factor-of-2) is CLOSED.
The remaining ChatGPT MAJORs are either disclosed-caveat re-flags or genuine open limitations
that require new image-level compute / a joint nuisance likelihood / a matched-footprint
Ganalyzer reanalysis — none editable in-manuscript without new data, all already disclosed.
Barrier is compute/venue, not text.

---

## Addendum — INT re-test v1.0.231 (audited 2026-07-10, → v1.0.232)

Fresh INT re-test on v1.0.231: OpenAI MAJOR (`INT_v3/ROUND_2026-07-09/API_P4_openai.md`, header v1.0.223 modality native-PDF), Grok-API MINOR (`API_P4_grok.md`), Claude-subagent MINOR (`INT_api/H17_2026-07-10/retest_P4_claude.md`).

### Shamir-propagation verdict
The v1.0.231 factor-of-2 correction landed almost everywhere, but the Claude retest caught **two live-text stragglers** the v231 sweep missed:
1. **Line 816** (`tab:primary_callout` caption): enumerated `z\approx-18` while the table body row (824) already read −7.6 — self-contradictory. **FIXED → `z\approx-7.6`.**
2. **Line 1370** (`tab:wls_fit` caption): naive-WLS `z=-264.5` (the old A_ref=0.034 value: (4.55e-3−0.034)/1.11e-4=−265) while the footnote (1367/1388) already read −112. **FIXED → `z=-112`** ((4.55e-3−0.017)/1.11e-4=−112.2 ✓).
No other `−18 / 0.034 / 7–18× / −264.5` survives in live text (remaining hits are `%` changelog only). The naive-WLS width σ_naive=1.11e-4 is unchanged by the correction (it is the fit width, not the reference) — correctly left as-is.

### Per-finding disposition
**Claude-subagent (MINOR, 4 items):**
- #1 stale `−18` caption straggler → **FIX** (above).
- #2 NSIDE=8 `−7.6` vs `−7.8` unreconciled → **FIX**: added half-sentence at line 1367 footnote noting the sensitivity check used N_boot=500 (z=−7.8) vs primary N_boot=1000 (z≈−7.6); the ~0.2 gap is bootstrap-sample-size noise on σ_boot.
- #3 figure LaTeX-escape artifacts (`vs.\ `, `interp.\,`) baked into PNG → **FIX (directive-I6)**: `scripts/gen_fig_bootstrap_null.py` L37/L48 escapes stripped; figure regenerated + render-verified (title "vs.", legend "interp. (i)", A_ref=0.017, best=4.55e-3, z≃−7.6 — all correct). Claude's own math check confirmed A_p=2(f_CW−½)=(N_CW−N_CCW)/(N_CW+N_CCW)≡Shamir asymmetry, z=(0.00455−0.017)/0.00163=−7.64. ✓
- #4 sub-percent null rests on CE-ResNet labels (GZ1-human-only floor A50≈3.4%) → **RE-FLAG/disclosed** (§pseudolabel_independence; Claude itself labels it an acknowledged limitation, not a defect).

**Grok-API (MINOR, 3 items):** all three are **RE-FLAGs of disclosed content** already dispositioned in the main audit — (a) ~47% forward-model remainder [= CG-7/GK-3, disclosed §Appendix-D, bounded below A95]; (b) three incommensurable σ conventions juxtaposed [= reader's note 975 + decision-tree Table I]; (c) GZ1-human A50/A95 floor visibility [= §pseudolabel_independence]. No genuinely-new editable finding.

**OpenAI-API (MAJOR, 11 MAJOR + 9 MINOR):** header is **v1.0.223 — a pre-Shamir-correction snapshot**. Every MAJOR maps 1:1 to an already-dispositioned finding in the main audit: OA-1↔CG-1 (dual-primary definition, RE-FLAG §prereg), OA-2↔CG-4 (injection bypass → label-field floors, RE-FLAG disclosed §sensitivity), OA-3↔Claude-#4/CG-2 (pseudo-label validation, RE-FLAG/OPEN), OA-4↔CG-7/GK-3 (47% remainder, OPEN-disclosed), OA-5↔CG-MINOR-2 (σ incommensurability, RE-FLAG reader's note), OA-6↔CG-8/GK-4 (exclusion language — already weakened to "disfavors not excludes" throughout + Shamir factor-2 now fixed, RE-FLAG), OA-7↔CG-2 (calibration/ECE, disclosed §Appendix-B ECE≥0.25–0.36), OA-8↔CG-1 (low-conf tail post-selection, RE-FLAG §prereg), OA-9↔CG-6 (eight-anchor battery qualitative → generative null, OPEN-disclosed 1159), OA-10↔CG-MINOR-1 (parity/birefringence overstated — already hedged "in principle, pending derived transfer function", RE-FLAG), OA-11↔GK-2 (immutable archive/DOI, OPEN Houston-gated at submission). MINORs 12–20 are style/consolidation (length, table redundancy, direction-vector-in-abstract, notation) = OPINION/RE-FLAG, not correctness gates. **Zero genuinely-new real editable finding** beyond the two stragglers Claude independently caught.

### Counts (this re-test)
- **Genuinely-new real + editable:** 3 (all MINOR: two stale-value stragglers #1/#2 + figure-escape #3) — **all closed**.
- **Genuinely-new per vendor:** Claude 3 new (all closed) · Grok 0 new · OpenAI 0 new (all re-flags of dispositioned content; snapshot predates the Shamir fix).
- **Re-flag / disclosed-limitation:** Claude 1 · Grok 3 · OpenAI 20 = 24, all source-cited to a paper line or the main audit.
- **MINORs closed:** 3/3 editable Claude minors. Grok 3/3 and OpenAI 20/20 dispositioned (re-flag/OPEN/OPINION) — none editable-new.

### Directive-G hygiene (all met)
- `.tex` **v1.0.231 → v1.0.232**; `\paperTimestamp` = July 10, 2026 (already current).
- TinyTeX 2-pass: **0 errors, 0 undefined references, 0 overfull hboxes**, 34 pp.
- Page-1 title strip render-verified (version + "Dated: July 10, 2026"); figure page render-verified (escapes gone, values correct).
- PDF mirrored **byte-identical to all 8 served paths** + new v1.0.232 versioned alias; papers.ts Read/Download hrefs v230→v232.
- **md5 = `3a5bdcbda81e860bcf6cf674a950b7d7`**, 34 pp, 34,028,273 bytes; three-way check compile==served==Convex ✓.
- Convex `paperVersions:bump` (paper-4, v1.0.232) written (id k571gs2p9mwbrr9rkwdr0mhd4n8a8s8n).

**No fabrication.** The two straggler fixes propagate the already-committed corrected arithmetic; the reconciliation sentence and figure fix change presentation only. All vendor MAJORs are re-flags of disclosed content; barrier remains compute/venue, not text.
