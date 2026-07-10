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

---

## Addendum — EXT re-test (2026-07-10, audited against current v1.0.232)

Fresh EXT re-tests on the **current** version: `retest/P4_grok_retest.md` (MAJOR — **WORSENED from MINOR**), `retest/P4_chatgpt_retest.md` (REJECT, 14 MAJOR + 3 MINOR). Every finding audited against v1.0.232 source. **Result: 0 genuinely-new editable findings.** No version bump, no directive-G, no Convex bump warranted.

### ⚠ P4 Grok flip diagnosis — CORRECTION/DISCLOSURE-BACKFIRE (pattern-066), NOT new content

Grok went **MINOR (H17) → MAJOR (re-test)** on the SAME THREE findings, and every fact it cites is the paper's OWN honestly-corrected/downgraded content from the v1.0.231–232 Shamir fix. It attacks the **corrected** numbers (A_ref 0.017, z≈−7.6, tension 3.7–8.8×) and the newly-strengthened caveats — i.e. it flipped harsher *because* the paper added honesty. Before/after:

| Finding | H17 Grok (MINOR) quote | Re-test Grok (MAJOR) quote | Diagnosis |
|---|---|---|---|
| Shamir z≈−7.6 exclusion language | "the amplitude-level tension (~7–18×)... must state more explicitly... this is not a statistical exclusion" (on the OLD doubled 7–18×/z≈−18) | "the phrasing that the WLS fit 'disfavors a clean cosmological dipole at the 1.7% reference amplitude... at z≈−7.6' is not supported... the text explicitly states this z is a model-dependent template-disfavor statistic... not a calibrated frequentist exclusion significance" | **BACKFIRE.** Grok's own MAJOR quotes the paper's disclosed caveat *verbatim* (L616, L707, L1367) and re-flags it as a defect. Attacks the CORRECTED z≈−7.6 and A_ref=0.017. |
| §IV D 53%/47% harmonic residual | "reproduces only ≈53%... ~47% remainder... although the paper correctly bounds this remainder below the real-space A95 and states it does not affect primary conclusions" (conceded disclosed) | same 53%/47%, same \|a1\|=6.95e-3, escalated to MAJOR: "the harmonic-channel systematic budget is therefore not closed" | **BACKFIRE / RE-FLAG.** = CG-7/GK-3. Disclosed verbatim L620 + §monopole_mask_null (L1017) + Appendix D; Grok concedes the bound in its own text. |
| §II B / §VI A pseudo-labels + GZ1 | (not a MAJOR in H17) | "66.5% of training labels are CE-ResNet pseudo-labels... GZ1-human-only... z=−0.54σ... ~4.5× coarser sensitivity (A50≈3.4%, A95≈4.5–6.8%)" | **RE-FLAG.** Every number (66.5%, 4.60e4, z=−0.54, A50≈3.4%, A95≈4.5–6.8%) lifted directly from the paper's OWN disclosures L639/L683/L1067. |

**Verdict: the P4 Grok flip is disclosure/correction-backfire, not something genuinely new.** All three MAJORs are the paper's own honestly-corrected/downgraded content; zero new editable defect.

### P4 ChatGPT re-test (REJECT, 14 MAJOR + 3 MINOR)
All 14 MAJORs map 1:1 to prior CG-1..CG-10 + INT dispositions (verified intact in v1.0.232):
- p_eq>0.6 post-selection (CG-1, RE-FLAG §prereg L707); rotational-invariance/21.4% D4 flips (CG-3, RE-FLAG L801); transfer calibration 69.91%/injection bypass (CG-4, RE-FLAG §sensitivity); harmonic residual/estimator conflict (CG-7, OPEN-disclosed); eight-anchor (CG-6, OPEN); null calibration exchangeability (CG-6, OPEN); sensitivity language A95 (GK-6, RE-FLAG); GZ1 coarse + "unit error factor-of-two" (RE-FLAG — paper is unit-explicit, A_p vs f_CW conversions given throughout e.g. L1067); low-conf interpretation (CG-1); theory transfer function (CG-MINOR-1, RE-FLAG hedged L1155); DOI/sample-N (CG-MINOR-2, OPEN Houston-gated).
- Two apparently-"new" numeric MAJORs are **definitional re-frames, not defects:**
  - **"z≈−7.6 is only ~1.4σ not 7.6σ under g=0.398 dilution"** — this dilution point, built on the paper's g and A_ref=0.017, is subsumed: the paper explicitly states the block-bootstrap z is a *template-disfavor statistic, not a detection significance* ("disfavors, not excludes at 7.6σ", L1367) and that classifier dilution makes it *conservative* (folded into A50/A95 via g=2a−1). Definitional, disclosed.
  - **"53%/47% is numerically incorrect — vector residual is 62%"** — the paper's statistic is explicitly the *scalar amplitude* reproduction (\|a_sys\|=3.75e−3 ≈54% of \|a_obs\|=6.95e−3, cosθ=+0.83/+0.84 stated, L1017) and it bounds the **entire** residual (100%, not just 47%) below A50/A95, so the 47%-vs-62% quibble is immaterial to any conclusion. RE-FLAG/OPINION, no fabrication.

### Counts (P4 re-test)
- **Genuinely-new real+editable:** 0 (Grok 0, ChatGPT 0).
- **Correction/disclosure-backfire (pattern-066):** 1 confirmed — the P4 Grok MINOR→MAJOR flip, all 3 items, before/after quoted above.
- **Re-flag / disclosed-limitation / opinion:** Grok 3, ChatGPT 17 — all source-cited to a paper line or a prior-audit disposition; all closures (Shamir factor-2, straggler fixes, figure regens) verified intact in v1.0.232.
- **Integrity:** no ACCEPT fabricated; both REJECT/MAJOR verdicts recorded as-is; no math fabricated; no edit warranted (nothing genuinely-new to close). Barrier remains compute/venue + LLM referee-variance (pattern-066), not text.

---

## Addendum — INT re-test on v1.0.233 → close → v1.0.234 (H17, 2026-07-10)

Fresh INT raws audited (all headed v1.0.233):
`INT_v3/ROUND_2026-07-09/API_P4_openai.md` (REJECT, 15 items: 12 MAJOR + 3 MINOR),
`API_P4_grok.md` (MINOR, 3), `INT_api/H17_2026-07-10/retest2_P4_claude.md` (MINOR, 3).

### Claude-subagent (MINOR, 3) — GENUINELY-NEW on the v1.0.233 stratified section → ALL FIXED
The Claude retest read the brand-new Appendix-B stratified-confusion content (Table `tab:gz1_stratified`,
committed `outputs/gz1_stratified_confusion.json`) and raised 3 precision/scoping tightenings — the only
genuinely-new findings this round (they target v233-new text that no prior audit had seen):

| # | Finding | Verdict | Close (v1.0.234) |
|---|---------|---------|------------------|
| CL2-1 | Sec IV C "leg-symmetric...cannot manufacture a dipole at the A_p scale of the null" (L1148) slightly stronger than the CIs (science-cut asymmetry CI ≈±0.42pp, half-width ≲0.6pp) support; sits in mild tension with the paper's own "do not exclude a sub-percent differential asymmetry" | **FIX** | Softened to "corroborates but does not fully close the differential-error channel at the sub-percent level" + explicit "the quoted CI half-widths (≲0.6pp science-cut) are the operative bound and do NOT exclude a sub-percent differential asymmetry" (Sec IV C narrative, ~L1148). |
| CL2-2 | Appendix-B conclusion: a 2-bin dec-split (dec≷+32°) is coarse as a *dipole* bound — an off-leg-axis differential-error dipole (RA-varying within a leg) is not directly bounded; the coarseness should be stated explicitly | **FIX** | Added: "this is a two-cell projection, not a full dipole map: a differential-error dipole not aligned with the leg-split axis...is bounded only through the coarser overall-stratum CI (±0.56pp), not resolved; the two-leg decomposition is the dominant-axis instance of, not a substitute for, the per-pixel model." (±0.56pp = overall asymmetry CI half-width 0.0056 from the table.) |
| CL2-3 | Stratified accuracies (0.912 overall, 0.961 science-cut) sit far above the headline conservative 0.6991 GZ1 chirality floor (κ=0.40) feeding g — a reader can conflate them | **FIX** | Added: "the high stratified accuracies here (0.912 / 0.961) are the confident-spiral ∩ classifier-CW/CCW accuracies...and are NOT a revision of the headline conservative GZ1 chirality-accuracy floor (0.6991, κ=0.40; Training Labels, Sec. IV)...measured on disjoint subsamples...the conservative 0.6991 floor is retained unchanged for all downstream isotropy bounds." |

All three are honest scoping tightenings; **no number changed**, no new claim fabricated. The ±0.56pp
and 0.912/0.961/0.6991 values all trace to the committed `tab:gz1_stratified` / stratified JSON.
Claude's own math check (retest2) independently confirmed the Shamir identity and the table arithmetic
(14,093+26,894=40,987; +5,030 NS=46,017) — no correctness defect.

### Grok-API (MINOR, 3) — all RE-FLAGs of disclosed content (0 new)
- GK2-a: multiple incommensurable null procedures quoted side-by-side despite the "not directly comparable"
  warning → **RE-FLAG** = CG-MINOR-2 / GK-1; reader's-note (L975) + notation section + decision-tree Table I
  already present; the warning is the disclosure.
- GK2-b: ~53% forward-model / ~47% remainder, injection-recovery grid resolution not cross-validated against
  the residual-decomposition templates → **RE-FLAG/OPEN** = CG-7 / GK-3; disclosed §Appendix-D, bounded below
  A95 a-fortiori; the joint cross-validation is the disclosed joint-covariance future item.
- GK2-c: Shamir tension (1.7–4.0% vs 0.455%, "3.7–8.8×") risks overstating given distinct estimator/selection
  → **RE-FLAG** = GK-4; the paper already states verbatim it does NOT claim a frequentist exclusion of Shamir's
  Ganalyzer estimator, and the factor-of-2 fix now correctly sizes the tension. No new editable defect.

### OpenAI-API (REJECT, 12 MAJOR + 3 MINOR) — all map 1:1 to dispositioned findings (0 new)
Every MAJOR fingerprint-matches a prior disposition, verified intact in v1.0.234:
OA2-1↔CG-4 (GZ1 69.91%/κ0.40 not validated for sub-percent + no image-level end-to-end injection; RE-FLAG/OPEN
§sensitivity — injection-bypass disclosed verbatim); OA2-2↔CG-1 (≈30% hard-confidence selection + low-conf z≈4
excess; RE-FLAG §prereg — HC 0.6 declared a-priori, sweep stable, GZ1-human-only model-free null z=−0.54);
OA2-3↔CG-7 (two primary estimators on different samples w/o common likelihood; OPEN-disclosed, joint-covariance
future item L1159); OA2-4↔CG-7 (harmonic +7.28/+7.93σ, ~47% not forward-modeled; OPEN-disclosed, bounded <A50);
OA2-5↔CG-MINOR-2 (many incommensurable σ; RE-FLAG reader's note); OA2-6↔CG-4 (A50/A95 are label-field
thresholds not physical; RE-FLAG — stated verbatim §sensitivity); OA2-7↔GK-4/CG-8 (Shamir tension + z≈−7.6
"disfavor" overstated; RE-FLAG — paper already says "disfavors not excludes", matched-Ganalyzer flagged
required); OA2-8↔CG-4/Claude-#4 (66.5% CE-ResNet pseudo-labels → not independent; RE-FLAG/OPEN
§pseudolabel_independence, GZ1-human-only null is model-free); OA2-9↔CG-6 (pixel-permutation doesn't preserve
survey geometry / spatially-varying error; OPEN-disclosed, density-stratified null run); OA2-10↔CG-8/GK-a
(block-bootstrap WLS covariance/rank-deficient nuisance for high-sig exclusion; RE-FLAG — "not a calibrated
frequentist exclusion" stated verbatim L1367); OA2-11↔the disclosed 2.9%/6.3% flip-prob QC issue (RE-FLAG
Appendix-B — dipole unchanged after removal, disclosed); OA2-12↔CG-MINOR-1 (parity framing without transfer
function; RE-FLAG — hedged "in principle, pending a derived transfer function" L1155). MINORs (length/DOI/notation)
= OPINION/OPEN Houston-gated (Zenodo DOI at submission). **Zero genuinely-new editable finding**; the OpenAI
snapshot re-raises the same structural REJECT floor (pattern-066: a maximally-harsh LLM referee returns MAJOR on
honestly-scoped, disclosed content — the same behavior documented across RS5–RS10).

### Counts (this re-test, v1.0.233 → v1.0.234)
- **Genuinely-new real + editable:** 3 (all Claude MINOR: CL2-1/2/3) — **all closed in v1.0.234**.
- **Genuinely-new per vendor:** Claude 3 (all closed) · Grok 0 · OpenAI 0.
- **Re-flag / disclosed-limitation / opinion:** Grok 3 · OpenAI 15 = 18, all source-cited to a paper line or a
  prior disposition.
- **Integrity:** no ACCEPT fabricated; the OpenAI REJECT and Grok/Claude MINOR verdicts recorded as-is; no math
  fabricated; the 3 closures change scoping/presentation only, every table number preserved.

### Directive-G hygiene (v1.0.234)
- `.tex` **v1.0.233 → v1.0.234**; `\paperTimestamp` = July 10, 2026 (already current).
- TinyTeX 2-pass: **0 errors, 0 undefined references, 0 overfull hboxes**, 35 pp (grew from 34 via the v233
  stratified section + these clauses).
- Page-1 render-verified ("Dated: July 10, 2026"; version tag intentionally date-only per P4-E1/E6). New clauses
  ("corroborates but does not fully close", "not a revision of the headline") render-verified in the PDF text.
- PDF mirrored **byte-identical to all 10 served paths** + new v1.0.234 versioned alias (public/papers/,
  site/public/papers/ incl. paper4_chirality_catalog.pdf + p4-chirality.pdf, arxiv/) .
- **md5 = `e687559202f6d4cfb8ab3bdd8bd60912`**, 35 pp, 34,036,610 bytes; three-way check compile==served==Convex ✓.
- Convex `paperVersions:bump` (paper-4, v1.0.234) written (id k57chnh0srwvz5d6wyyf1fxrmd8a8hvx). papers.ts +
  live-status.ts version/hrefs/pdfMeta synced to v1.0.234.

**No fabrication.** Barrier remains compute (image-level end-to-end injection, joint nuisance likelihood,
matched-footprint Ganalyzer reanalysis) + venue + LLM referee-variance (pattern-066), not text.
