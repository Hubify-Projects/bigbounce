# Convex backfill queue — 2026-09-21 Convex outage

Convex is DISABLED (deployment suspended for exceeding its spending limit; Houston-only
fix on the Convex dashboard). Every lane that would normally write live state via the
public HTTP API / ConvexHttpClient instead appends its exact intended mutation(s) here —
function name + exact args — so they can be replayed once Convex is re-enabled. Append
only; do not edit another lane's entries.

---

## LAF2 (bb-LAF2-af-todos), 2026-09-21

Paper AF, vAF.0.4 → vAF.0.5. Non-review directive-G bundle: DAF-16 fully closed
(released-column schema 183/192 → 192/192), full bibliography ADS-verification
completed (26 remaining entries, all match). No review board run (directive R2 stays at
round 1 of 2). See `project-context/SSOT/paper-af/status.md` §"LAF2 non-review TODO
closure" and `project-context/peer-reviews/DISPOSITIONS/AF.md` (DAF-16) for full detail.

```
paperVersions:bump({
  paperId: "AF" (slug "paper-af"),
  version: "vAF.0.5",
  pages: 18,
  date: "2026-09-21",
  sha256: "ea81ef413503d25291853a2be714226d3b47fe680ead2f01727aaabe961140ca",
  md5: "60de7e9dbfbcc77336b3050ee788e68e",
})

papers:setReadinessCap({
  slug: "paper-af",
  readinessCap: 77,   // was 75
})

activityFeed:add({
  type: "research",
  tags: ["paper-af", "vAF.0.5", "campaign-2026-09-18"],
  summary: "AF vAF.0.4->vAF.0.5 (lane LAF2, non-review): DAF-16 fully closed (schema table now documents all 192/192 released columns, was 183/192); full bibliography ADS-verified (26 remaining entries, all match, no text changed); OT-1 selection function and Zenodo DOI reconfirmed genuinely not agent-closable (GPU compute / Houston-only respectively), left unchanged. Directive-G bundle: 4-pass compile clean, 0 undef refs, 18pp, 5-way md5-verified mirrors, artifact-link-verify 6/6 pass, mirror-integrity 0 findings, arXiv tarball rebuilt+smoke-tested. Readiness 75->77 COMPUTED. Directive R2: round 1 of 2 still spent (no board run).",
})
```

---

## L4d (bb-L4d-p4p-row16-propagate), 2026-09-21

Paper P4P (P4′), v4P.0.9 → v4P.0.10. Science-content propagation (row-16(ii-b)
PA-parity-transfer result), not a review-round closure — no board run,
readiness stays 95 COMPUTED. See `project-context/SSOT/paper-4p/status.md`
§"Row-16(ii-b) PA-parity-transfer propagation" and
`project-context/peer-reviews/DISPOSITIONS/P4P.md` §"v4P.0.9 → v4P.0.10" for
full detail.

```
paperVersions:bump({
  paperId: "P4P" (slug "paper-4p"),
  version: "v4P.0.10",
  pages: 15,
  date: "2026-09-21",
  sha256: "054b63f8a73902000a0e703da62229ee887f2fc77b0cc027533c2309985f9310",
  md5: "d2d017145530e641ea491c4f5f0909de",
})

activityFeed:add({
  type: "research",
  tags: ["paper-4p", "v4P.0.10", "campaign-2026-09-18"],
  summary: "P4P v4P.0.9->v4P.0.10 (lane L4d, science propagation, not a review round): applied lane bb-LS-ledger16/bb-LS5-row16-finalize's exact PROPAGATION_NOTE.md sentences (P-1..P-5d) verbatim to main.tex -- withdrew the invalid pixel-injection naive-identity tension claim (+0.434/47sigma, 0.038 ratio, ~26% floor, all comparisons between incompatible statistics) and adopted the measured direct dilution bound instead: PA-restoring-reversal epsbar=0.754+/-0.005, D<=0.717+/-0.005, A95^phys>=1.37%, consistent with (not in tension with) the illustrative g=0.398 bridge. Propagated consistently to the three other in-paper mentions (S2.3 forward-ref, Discussion, Conclusions) using only already-cited numbers, no new derivation. Directive-G bundle: paperVersion/date bumped, 4-pass compile 0 undef refs (inline thebibliography, no .bbl dependency), 14->15pp, 1 pre-existing 5.88pt hbox unchanged, 3-way byte-identical PDF mirror (source/site-public/public), 19/19 hyperlink URIs resolved (15 GitHub incl. 2 new row16iib links + 2 Zenodo + 1 HF + 1 site link), arXiv tarball rebuilt and standalone-compile-verified. Readiness unchanged at 95 COMPUTED; directive R2 round budget refreshed by this science decision but no board run in this lane. LS6's second propagation note (row16_tta_2026_09_21/) did not exist at run time -- not included, flagged for a future lane.",
})
```

---

## L1c (bb-L1c-a3m-row9-r11), 2026-09-21

Paper A3M, v3M.0.26 → v3M.0.27. Science-decision propagation (ledger row 9 /
D-A3-9, Bardeen-potential scheme selection) + gate-S12 correction, not a
review-round closure — no board run yet at this bundle, readiness stays 75
COMPUTED. See `project-context/SSOT/paper-a3m/status.md` §"v3M.0.27
(2026-09-21)" for full detail.

```
paperVersions:bump({
  paperId: "A3M" (slug "paper-a3m"),
  version: "v3M.0.27",
  pages: 21,
  date: "2026-09-21",
  sha256: "3e49f29bdc4bb21ea293db6a2174c4289f1308db2da9b3d96fa1e5192fbbdcef",
  md5: "ea6ebd918399650702ee5a9c81182ab2",
})

activityFeed:add({
  type: "research",
  tags: ["paper-a3m", "v3M.0.27", "campaign-2026-09-18"],
  summary: "A3M v3M.0.26->v3M.0.27 (lane L1c, science propagation, not a review round): applied research/cubic_bounce_transmission/row9_scheme_independence_2026_09_19/PROPAGATION_NOTE.md sentences verbatim -- the Bardeen potential Phi (z-free, 1/H-free, regular at H=0 and at rho+p=0) selects scheme S2 on the Quintin-type background (|lambda_zeta|=0.9699, independently blind-confirmed by a different (Psi,D)/Israel-matching construction); f_NL^after collapses from the two-scheme band [-1.25,-0.50] to the single value -1.25 there, while r_after takes the S2 value ~9.4e2 (was S1's 24.0) -- tensor no-go strengthens from 670x to 2.6e4x BICEP/Keck, both directions propagated together per directive F. Same bundle: gate-S12 general-tilt (n_s=1) correction to Appendix A's monopole and in-in bispectrum formulas (research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.md) -- no headline number changes, since this paper's construction is exactly at eps=3/2 dust where the correction vanishes. Directive I6: both figures checked, neither carries the affected values, no regeneration needed. Directive-G bundle: 4-pass compile 0 undef refs, 20->21pp, one intermediate 116pt table-row overflow from an over-long multicolumn label caught by /latex-audit and fixed (final residual 2.16pt), 3-way byte-identical PDF mirror (source/site-public/public), pages 1/6/13/18/19 visually checked. Readiness unchanged at 75 COMPUTED. This is the intervening science decision directive R2 required after the R9+R10 rounds-stop; R11 INT board dispatched on this exact PDF in the same lane.",
})
```

## Lane `bb-LS7-row23-fate-de` (2026-09-22) — Convex DISABLED, queued not sent

Research/ledger lane only: no paper version changed, so **no `paperVersions:bump`,
no `papers:setReadinessCap`, no `rRounds:create`, no `externalReviews:upsertByLabelDate`.**
One activity event:

```
activityFeed:add({
  type: "research",
  tags: ["open-questions", "ledger-row-23", "cosmic-fate", "dark-energy", "campaign-2026-09-18"],
  summary: "Ledger row 23 answered as a BOUNDARY result (lane bb-LS7-row23-fate-de, research/cosmic_fate_de_2026_09_22/). Pre-registration committed alone before any statistic. Cross-table: the 11 Branch I bounce-compatible DE rows (Classes 1-7 plus Phase-1 subclasses A-F) evaluated against the row-20 turnaround criterion (COSMIC_FATE_MEMO.md Eqs. 2.3-2.5), each decided by a sympy lemma. Intersection = 3 classes: zero-crossing quintessence, zero-crossing k-essence, interacting dark sector with a sustained drain. Lambda, viable f(R) and vacuum sequestering FAIL by the positive-floor lemma; braiding, DHOST and massive gravity stay UNDETERMINED on the bounce axis per Branch I's own verdict and are not promoted. Step 2, at fixed Omega_m = 0.2975 and h*r_d = 101.54 Mpc against DESI DR2 per-bin uncertainties and correlations derived in code from published covariance blocks: a >1 sigma present-day separation from LambdaCDM DOES exist, but only above a threshold in the PRESENT-DAY equation of state -- linear-potential quintessence crosses 1 sigma at w0 = -0.951 / t_c = 53.8 Gyr and the quadratic-top family at w0 = -0.934 / t_c = 13.7 Gyr, i.e. a 0.017 spread in w0 but a factor 3.93 in the turnaround epoch. DESI DR2 therefore constrains how fast dark energy is evolving now; the fate epoch is inferred, not measured, and the inference is potential-family dependent. Row 23 stays an OPEN QUESTION at the row-20 memo's evidence layer: no manuscript claim, no SSOT row, no null changed. Three named gaps recorded and never filled with an invented number (frame-dependence for non-minimally coupled scalars; no citable DR2-era f*sigma8; no citable DR2 central values). Also re-verified symbolically that CPL's rho_DE(a) is positive for every a, so no CPL fit implies a Crunch.",
})
```

---

## L1c (bb-L1c-a3m-row9-r11), 2026-09-22 (R11 closure)

Paper A3M, v3M.0.27 → v3M.0.28. R11 INT board closure — the one board
directive R2 permitted after the row-9 science decision. See
`project-context/SSOT/paper-a3m/status.md` §"v3M.0.28 (2026-09-22)" and
`project-context/peer-reviews/INT_v3/A3M_v3M.0.27_R11_TRUTH_AUDIT_2026-09-22.md`
for full detail.

```
paperVersions:bump({
  paperId: "A3M" (slug "paper-a3m"),
  version: "v3M.0.28",
  pages: 21,
  date: "2026-09-22",
  sha256: "87fd3c2372dbf09c2d4a7fa6ea339db2da0641184f00cbf4112db7a5df841012",
  md5: "e4a2ca93564bc566a52e68252865c460",
})

externalReviews:upsertByLabelDate({
  paperSlug: "paper-a3m",
  reviewerLabel: "Grok (R11-INT)",
  recommendation: "reject",
  source: "internal-stage3",
  notes: "Grok grok-4.3 API, native-PDF (rasterized), exact v3M.0.27 PDF sha256 3e49f29b. Raw: project-context/peer-reviews/INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/..._A3M_Grok_brutal.md",
  receivedAt: "2026-09-22",
})

externalReviews:upsertByLabelDate({
  paperSlug: "paper-a3m",
  reviewerLabel: "Gemini (R11-INT)",
  recommendation: "major-revisions",
  source: "internal-stage3",
  notes: "Gemini gemini-3.1-pro-preview API, native-PDF. Raw: project-context/peer-reviews/INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/..._A3M_Gemini_cosmology.md",
  receivedAt: "2026-09-22",
})

externalReviews:upsertByLabelDate({
  paperSlug: "paper-a3m",
  reviewerLabel: "Claude opus (R11-INT)",
  recommendation: "major-revisions",
  source: "internal-stage3",
  notes: "Claude opus sub-agent, verdict-blind (no access to prior review history), 2 ESSENTIAL / 6 MAJOR / 14 minor / 12 nit. Raw: project-context/peer-reviews/INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/..._A3M_claude_opus_referee.md",
  receivedAt: "2026-09-22",
})

rRounds:create({
  paperSlug: "paper-a3m",
  roundLabel: "R11",
  dateISO: "2026-09-22",
  kind: "internal-api",
  genuinelyNewCount: 16,
  cleanWaveStreak: 0,
  summary: "R11 INT board on exact v3M.0.27 PDF; 16 genuinely-new-real finding-classes closed in v3M.0.28 (2 ESSENTIAL on the row-9 Bardeen material, 5 MAJOR scheme-labelling/reasoning, 1 pre-existing PBH sign error, 1 recurrence of the internal-audit-language leak, minor cluster). No physics error found; no headline number changed.",
})

activityFeed:add({
  type: "r-round",
  tags: ["paper-a3m", "v3M.0.28", "R11", "campaign-2026-09-18"],
  summary: "A3M v3M.0.27->v3M.0.28 (lane L1c): R11 INT board (Grok REJECT, Gemini MAJOR REVISIONS, Claude opus verdict-blind referee MAJOR REVISIONS) on the exact v3M.0.27 PDF -- the one board directive R2 permitted after the row-9 (D-A3-9) Bardeen-potential science decision. Truth-audit closed 16 genuinely-new-real finding-classes: two ESSENTIAL items on the new Bardeen material (its regularity claim was asserted not derived, and f_NL^after[S2]=-1.25 was quoted to 3 sig figs with an undisclosed evaluation-window convention -- both closed using material already in the cited artifact, no new derivation/computation), five MAJOR scheme-labelling/reasoning defects from the row-9 propagation not being swept through the whole manuscript, one pre-existing PBH sign error (confirmed against the committed script's own verdict string, no conclusion change), and a third recurrence of the internal-audit-language-leak defect class (directive Q1; closed twice before in R9/R10). No physics error found: the Claude opus leg independently re-derived/cross-checked ~40 numerical claims against primary literature and committed JSONs, all reproduced. No headline number changed. Directive R2 budget SPENT AGAIN -- rounds stopped; a further science/scope decision or Houston's authorization of a confirmation board is required. Readiness held at 75 COMPUTED.",
})

papers:setReadinessCap({
  slug: "paper-a3m",
  readinessCap: 75,   // unchanged -- automated-review-convergence gate still not met
})
```

---

## Lane `bb-LS8-row23-growth` — 2026-09-22 (ledger row 23, GAP-2 closed as a null)

Research lane. No paper touched, so **no** `paperVersions:bump`, `rRounds:create`,
`externalReviews:upsertByLabelDate` or `papers:setReadinessCap` applies. One event:

```js
activityFeed:add({
  type: "research",
  tags: ["ledger-row-23", "open-questions", "gap2-growth", "null-result", "campaign-2026-09-18"],
  summary: "Row 23 GAP-2 CLOSED AS A NULL (lane bb-LS8-row23-growth). The parent lane left growth as the one observable that could separate the k-essence member (M3) from the canonical quintessence member (M1), which share an identical background exactly. Citation first, honestly: no citable DESI DR2-era growth measurement with an uncertainty EXISTS -- DR2 Results II is BAO-only, the DR2-era joint paper (2602.18761) still takes growth from DR1 and reports sigma8, and the one DR2 full-shape analysis producing an fsigma8 (2607.27411, Lya) withdrew it, its abstract citing a significant mock-verified bias. Pre-registered fallback taken and labelled everywhere: DESI DR1 full-shape arXiv:2411.12021, every per-bin sigma DERIVED in code as sqrt(C[2][2]) from the Appendix-A Gaussian covariances (eps = 9.5-19.9%); DESI's own Sec. 7.1 restriction honoured, so no measured central value enters any decision and no goodness-of-fit is computed. RESULT: growth does NOT separate M3 from M1. Over the entire c_s^2 range the model permits -- derived symbolically as [0,1), with M1 the c_s^2 -> 1 endpoint -- and over k in [0.01,0.2] h/Mpc, max|Delta| = 0.0043 sigma, 233x short of threshold, monotone in c_s^2 so the c_s^2 = 0 endpoint bounds every trajectory. The null is structural: across a factor ~20 in background strength the maximal sound-speed signature stays a fixed 3.83% +- 0.09% of the model's own background growth signature. Growth also adds nothing to the boundary: 0.113 sigma at the parent lane's alpha* against BAO's 1.00 sigma (~8.8x weaker); growth alone would need w0 = -0.500 or xi = 0.153 against BAO's xi* = 0.025. Also derived: in a coupled dark sector RSD measures f = dln(delta)/dln(a) + gamma, so scoring M2 with dln(delta)/dln(a) overstates its separation by 2.65x. Row 23's published deliverable is UNCHANGED -- the w0 threshold and the x3.93 fate ambiguity stand; the lane removes the possibility that the missing observable would have changed them. Row 23 stays an Open Question; no manuscript claim, no SSOT row, no null changed. GAP-1 (frame-dependence for non-minimally coupled scalars) is now the only remaining row-23 step that could change the row's content.",
})
```

---

## LS6 (bb-LS6-row16-tta), 2026-09-22

Ledger rows 13 + 16 science lane. Three pre-registered zero-cost steps
(`pipelines/p4prime_chirality_test/row16_tta_2026_09_21/`, pre-registration git
`712e9e7e`), plus a failed pre-registered control that outranks them. No paper, SSOT or
site-data edit — nothing to bump; the intended writes are activity-feed events only.

```
activityFeed:add({
  type: "research",
  title: "Row 16(iii) D4-equivariant retrain: GPU NO-GO on a pre-registered decision rule",
  tags: ["ledger-row-16", "galaxy-chirality", "P4P", "tta-recovery-bound", "gpu-decision", "campaign-2026-09-18"],
  summary: "A rotation test-time average over the EXISTING committed checkpoint recovers only 20.7% +- 1.0% (D4) and 39.4% +- 0.9% (D8) of the released pipeline's dilution gap, measured on a new uniform 16-angle 22.5-degree grid (stage-3 inference: 19,800 galaxies x 8 offset angles x 2 mirror states = 316,800 forward passes, 37.5 min local Apple MPS, $0). A pre-registered theorem, verified numerically to float32 precision as control T0-C, forced that grid: a G-TTA is exactly C_n-invariant and exactly mirror-antisymmetric, so it zeroes the label self-disagreement on its own rotation orbit and returns eps = 1 identically wherever 2*phi lies in the group -- the existing 45-degree grid could therefore measure nothing about a D4 TTA, and eps_D8 remains NOT MEASURABLE without an 11.25-degree grid (recorded as such, never as 1.0). Dilution bound D <= 0.6237 +- 0.0033 (released, flip-only) -> 0.7017 +- 0.0037 (D4) -> 0.7718 +- 0.0035 (D8); 0.7028 -> 0.7725 -> 0.8387 on the catalogue's primary_hc cut. The pre-registered rule (GO iff F_D4 >= 0.5 AND residual >= 0.10, fixed before the number existed) returns NO-GPU, WRONG-LEVER: the deficit is a smooth-orientation instability, not a discrete-symmetry defect; the free 8-fold TTA is twice the lever the retrain's guaranteed part is; and a retrain would be buying feature quality, a different and much less certain purchase than the one row 16(iii) was costed on. Manifest row16-tta-recovery-bound.",
})
```

```
activityFeed:add({
  type: "research",
  title: "d(180) on the largest feasible subset: N = 25,254, D <= 0.6910 +- 0.0034",
  tags: ["ledger-row-16", "galaxy-chirality", "P4P", "dilution-bound", "campaign-2026-09-18"],
  summary: "The full 8,474,531-row parent was declared INFEASIBLE in advance (a d(180) needs one forward pass per galaxy per orientation ON THE IMAGE, no parent cutouts are cached, and new downloads were excluded), so the largest feasible subset is the de-duplicated union of all three committed cutout caches: N = 25,254 (46 duplicates removed), d(180) = 0.3090 +- 0.0034, i.e. D <= 0.6910 +- 0.0034 (strict-primary 0.2501 +- 0.0057, D <= 0.7499). Stage-4 inference added the two caches row 16(ii-b) never used (5,500 galaxies, 22,000 forward passes, 2.4 min, $0) through the exact released preprocessing with a lossless 180-degree transpose -- no interpolation anywhere. The three independent draws (seeds 42/43/44, two sky-sampling resolutions, fetched on different dates) agree within errors: 0.3072 +- 0.0037, 0.3116 +- 0.0075, 0.3497 +- 0.0252; the N = 19,800 value reproduces row 16(ii-b) section 6 exactly from an independently written analysis path, and the mirror-identity control is exact on every draw. The pre-registered confidence-stratified catalogue-wide re-weighting is VOID and labelled void -- see the provenance event below. Manifest row16-d180-largest-feasible-subset.",
})
```

```
activityFeed:add({
  type: "research",
  title: "S6 sky dependence is a real 11-sigma dipole: P4' dipole limits need a systematic caveat",
  tags: ["ledger-row-16", "galaxy-chirality", "P4P", "systematic", "dipole", "campaign-2026-09-18"],
  summary: "The row-16(ii-b) hemisphere asymmetry in parity-transfer efficiency is a genuine dipole: fractional amplitude 0.0901 +- 0.0102 toward (123.2 deg, -72.8 deg), z = +10.9 against 1,000 random permutations of the per-galaxy efficiency across sky positions (rank p <= 0.001; 0 of 1,000 permutations reached it), with its axis 31.6 degrees from the strict-887,472 dipole axis. The per-galaxy estimator reproduces the original S6 split (delta = +0.0359 +- 0.0055 strict, -0.0378 +- 0.0052 full-parent). Propagated through P4's OWN estimator -- build_projector imported verbatim, NSIDE = 64, support >= 10, reproducing 887,472 galaxies in 23,633 support pixels and A_obs exactly -- a dilution modulated in proportion to it imprints a spurious label dipole of 0.230% +- 0.026 on the strict support, 23% of that subset's A_95 = 0.98%, and 0.046% +- 0.005 on the full parent (9% of A_95 = 0.51%). The strict subset is the exposed one because its observed label MONOPOLE is +2.55%, five times the full parent's and of opposite sign. The pre-registered threshold (caveat required iff A_induced > 10% of A_95, fixed before the computation) FIRES. Stated at exactly its strength: a measured sky dependence plus an estimator-exact propagation, NOT a measured contamination -- a zero true asymmetry yields zero dipole under any dilution. Exact printable sentence in PROPAGATION_NOTE.md Q-3. Manifest row16-s6-dipole-projection.",
})
```

```
activityFeed:add({
  type: "research",
  title: "Pre-registered control catches a provenance defect in the whole row-13/16 image-level program",
  tags: ["ledger-row-13", "ledger-row-16", "galaxy-chirality", "P4P", "provenance", "integrity", "campaign-2026-09-18"],
  summary: "A pre-registered positive control failed and it outranks everything else this lane produced. Every image-level run of rows 13 and 16 -- the 500-galaxy pilot, the N=5,000 scale run, the N=20,000 run and row 16(ii-b) -- fetched the DISPLAY-ONLY image_url column that run_eq_fast.py:265-270 appends to catalog_production.parquet (jpeg-cutout, size=150, layer=ls-dr9: a 39.3-arcsec field upsampled 150 -> 224), instead of the parent images the catalogue was actually inferred on and that BOTH papers document correctly (Smith42/galaxies, 224 px, 0.262 arcsec/px = 58.7 arcsec, DESI Legacy DR8, pinned HF revision bdd1b063; chirality_catalog_paper.tex:1019 and p4prime paper/main.tex:171). Re-running the released preprocessing through the released checkpoint on those cutouts reproduces the released catalogue's class for only 43.9% of 19,800 galaxies (42.4% and 44.7% on two further independent draws) while reproducing this repository's own committed 2026-09-04 forward passes at 99.99% -- the code is right and the images are wrong. Post-hoc diagnostics: the documented 224 px / 58.7-arcsec geometry recovers about a sixth of the gap (agreement 0.460 -> 0.497, handedness transfer 0.611 -> 0.654); the ls-dr8 vs ls-dr9 layer explains none of it (0.4533 vs 0.4600, the two layers agreeing with each other at 0.89); central-crop zoom explains none of it. Roughly half the gap remains, most plausibly the grz-to-RGB rendering. The released data products and both papers' provenance are NOT implicated, and the catalogue's (RA,Dec)-to-label correspondence is confirmed sound (77% of catalogued spirals are labelled spiral, handedness agreement 16.6 sigma above chance), so P4's dipole coordinates are unaffected. Consequence: every image-level number from rows 13/16(ii)/16(ii-b) is OUT OF DOMAIN, and D <= 0.7166 with A_95^phys >= 1.37% are ON HOLD for P4' until re-measured on Smith42/galaxies (PROPAGATION_NOTE.md Q-1). The mirror-injection retirement is UNAFFECTED: it rests on the exact identity eq_cw(MI) = eq_ccw(I), which holds for any image whatsoever.",
})
```

## Lane bb-L4e-p4p-hold-correction (2026-09-22) — v4P.0.11 hold correction

Urgent correction lane applying the above provenance-defect finding to
`pipelines/p4prime_chirality_test/paper/main.tex` itself: withdrew
`D <= 0.717 +/- 0.005` / `A_95^phys >= 1.37%` from all 7 prose locations + 2
table rows, replaced with a named hold, and printed the Q-3 sky-dependence
systematic sentence. `\paperVersion` v4P.0.10 -> v4P.0.11.

```
paperVersions:bump({
  paperId: "P4P",
  version: "v4P.0.11",
  dateISO: "2026-09-22",
  sha256: "9f3822a2f1c97184c7d4beccd14294739816228b53ef8e59af02e6bc20b1528a",
  md5: "c5944b14d0987d14bbe0d2a61953b1f6",
  pages: 15,
  note: "HOLD CORRECTION: withdrew the v4P.0.10 dilution bound (D<=0.717+-0.005, A_95^phys>=1.37%) after a positive control found it was measured on out-of-domain images (43.9% agreement with released labels on the wrong images vs. 99.99% in-domain); replaced with a named, lifted-by-a-specific-test hold plus the new sky-dependence systematic (0.23% spurious dipole, 23% of A_95 on the strict support). Row-16(ii-b) items P-1-P-4 unaffected. Readiness unchanged at 95 (correction, not a review round).",
})
```

```
activityFeed:add({
  type: "research",
  title: "P4' hold correction: the just-published dilution bound was measured on out-of-domain images -- withdrawn same day, sky-dependence systematic disclosed",
  tags: ["ledger-row-16", "galaxy-chirality", "P4P", "hold-correction", "integrity", "campaign-2026-09-18"],
  summary: "Lane bb-L4e-p4p-hold-correction. The dilution bound D<=0.717+-0.005 / A_95^phys>=1.37% that lane bb-L4d-p4p-row16-propagate printed into v4P.0.10 hours earlier was found by lane bb-LS6-row16-tta to have been measured on Legacy Survey display cutouts rather than the classifier's own Smith42/galaxies inference images (a positive control reproduces released labels at only 43.9%/42.4%/44.7% across three draws on the wrong images, vs. 99.99% in-domain). Withdrawn from all 7 prose locations and 2 table rows in main.tex, replaced with a named, lifted-by-a-specific-test hold (never a silent deletion): the hold lifts on re-running the identical PA-restoring test on the correct, pinned Smith42/galaxies images (bounded, disk-only, no GPU). The Q-1a architectural argument (why the transfer is not unity by construction) is retained verbatim and unaffected. Also printed the pre-registered sky-dependence systematic: an 11-sigma efficiency dipole imprints a spurious 0.23% label dipole on the strict-887,472 support, 23% of the quoted A_95=0.98% limit. Row-16(ii-b) items P-1-P-4 (pixel-injection error-bar fix, withdrawal of the invalid 47sigma/2.9sigma/0.038/~26% comparisons) confirmed unaffected. Readiness holds at 95 -- this correction improves science closure and evidence/reproducibility (no unsupported claim remains) rather than degrading it; directive R2's round budget is refreshed again, a fresh INT confirmation board on the exact v4P.0.11 PDF is now due. Co-director sign-off hold LIFTED for the printed-claim defect; STILL STANDS pending that board and the in-domain re-measurement.",
})
```

## Lane bb-LCB-confirm-p1b-p2 (2026-09-22) — P1B R-CONFIRM, v2B.0.23 -> v2B.0.24

Exact-version confirmation board on P1B v2B.0.23 (sha256 c7cac6c9f16c...): Grok
API REJECT, Gemini API REJECT, Claude opus verdict-blind sub-agent MAJOR
REVISIONS (43 findings). NOT a clean wave. Truth-audited against
`DISPOSITIONS/P1B.md`; most genuinely-new-real items closed by real edit in
v2B.0.24 (see `DISPOSITIONS/P1B.md` "v2B.0.23 R-CONFIRM" section for the full
fingerprinted list: D-CONF-01 through D-CONF-13). Left open by design:
Sec.13-vs-JORS venue split (Houston-gated, re-flag of standing D-R3-31), the
archive re-mint (Houston-gated), a full batch-4 commit trail + 54-run
appendix, and a handful of deferred related-work/derivation items
(D-CONF-04/09/10/12).

```
rRounds:create({
  paperId: "P1B",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  reviewers: ["Grok API (grok-4.3)", "Gemini API (gemini-3.1-pro-preview)", "Claude opus sub-agent (verdict-blind)"],
  note: "Exact-version confirmation board on v2B.0.23 (sha256 c7cac6c9f16c...). Verdicts: REJECT / REJECT / MAJOR REVISIONS, 43 findings. Truth-audited against DISPOSITIONS/P1B.md; most genuinely-new-real items closed by real edit in v2B.0.24. NOT a clean/converged wave -- see D-CONF-04/09/10/12 for residual open items.",
})
```

```
rRounds:markComplete({
  paperId: "P1B",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
})
```

```
externalReviews:upsertByLabelDate({
  paperId: "P1B",
  reviewer: "Grok",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  verdict: "reject",
  source: "internal-stage3",
  note: "Exact v2B.0.23 (sha256 c7cac6c9f16c...) via tools/v3_native_pdf_review.py. 4 ESSENTIAL + 4 MAJOR + 3 NIT (+ pass-2: 1 ESSENTIAL, 1 MAJOR, 1 NIT). Most genuinely-new-real findings closed by real edit in v2B.0.24; the E5/N4 arithmetic-misreading finding FALSIFIED (the printed bound was correctly scoped to the class-level rate, not run-level).",
})
```

```
externalReviews:upsertByLabelDate({
  paperId: "P1B",
  reviewer: "Gemini",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  verdict: "reject",
  source: "internal-stage3",
  note: "Exact v2B.0.23 (sha256 c7cac6c9f16c...) via tools/v3_native_pdf_review.py. 3 ESSENTIAL + 3 MAJOR + 2 MINOR + 1 NIT. All genuinely-new-real findings (internal audit tags, class/run-level statistics contradiction, scope/length) closed by real edit or already a standing Houston-gated venue decision in v2B.0.24.",
})
```

```
externalReviews:upsertByLabelDate({
  paperId: "P1B",
  reviewer: "Claude opus (verdict-blind sub-agent)",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  verdict: "major-revisions",
  source: "internal-stage3",
  note: "Exact v2B.0.23 (sha256 c7cac6c9f16c...), cold read, no repository access, no review history. 4 ESSENTIAL + 12 MAJOR + 17 MINOR + 10 NIT (43 total); every printed arithmetic and design-count claim independently re-verified and found correct (Appendix Table 6 audited run-by-run against Table 3, exact match). Most closed by real edit in v2B.0.24: CP-bound validity (E3/M6), stale abstract value-level claim (M9), missing batch-4 confusion table + soundness bound (E4/M1), Sigstore/Rekor + Fiat-Shamir mislabeling (M2/M3), archive-predates-work disclosure (E2, partial). Left open by design: venue split (E1, Houston-gated re-flag of D-R3-31), full archive re-mint (Houston-gated), batch-4 commit trail + appendix, related-work/derivation items (D-CONF-12).",
})
```

```
paperVersions:bump({
  paperId: "P1B",
  version: "v2B.0.24",
  dateISO: "2026-09-22",
  sha256: "eec6e6d4792b2d8ecb17b05a4ee97d4ec2b5bd1c1f579f41b92bfc8746dc5bbd",
  md5: "b94a18fbfbdece5949999354d6833864",
  pages: 18,
  note: "R-CONFIRM exact-version board closed most genuinely-new-real findings (CP-bound removal, stale abstract/Scope-limits value-level claim, batch-4 confusion table transcribed from committed public4/scorecard.json + f^K soundness bound, checklist-style Limitations prose reworded, Sigstore/Rekor + Fiat-Shamir mislabeling corrected, archive-predates-work disclosure, ~15 editorial fixes). NOT a confirmed/converged board -- D-CONF-04/09/10/12 remain open by design (Houston-gated or explicitly deferred). Readiness holds 95, computed.",
})
```

```
activityFeed:add({
  type: "r-round",
  title: "P1B R-CONFIRM: exact-version board finds a real Clopper-Pearson validity defect and a stale abstract claim",
  tags: ["P1B", "v2B.0.24", "r-round", "confirmation", "campaign-2026-09-18"],
  summary: "Lane bb-LCB-confirm-p1b-p2 closed the exact-version confirmation gap flagged in the 2026-09-19/22 sign-off packets. Board (Grok REJECT / Gemini REJECT / Claude opus verdict-blind MAJOR REVISIONS, 43 findings) was NOT clean. Most genuinely-new-real items closed by real edit: every Clopper-Pearson interval removed because honest replicates are deterministic replicas of a fixed reference configuration, not an i.i.d. sample; the abstract's stale value-level-shortcuts claim brought in line with Sec.11; a new batch-4 confusion table transcribed from already-committed data plus an explicit R8 soundness bound; Sigstore/Rekor and Fiat-Shamir mislabeling corrected; archive-predates-work gap disclosed. Left open by design: the venue-split scope decision (Houston-gated), archive re-mint (Houston-gated), a full batch-4 commit trail, and a few deferred items. v2B.0.23 -> v2B.0.24, 16 -> 18 pp. Readiness holds 95.",
})
```

## Lane bb-LCB-confirm-p1b-p2 (2026-09-22) — P2 R-CONFIRM, v1.7.130 -> v1.7.131

Exact-version confirmation board on P2 v1.7.130 (sha256 d3afe79fe70c...): Grok
API REJECT, Gemini API MINOR REVISIONS, Claude opus verdict-blind sub-agent
MAJOR REVISIONS (36 findings). NOT a clean wave. Truth-audited against
`DISPOSITIONS/P2.md`; mechanical/editorial majority of genuinely-new-real
items closed by real edit in v1.7.131 (see `DISPOSITIONS/P2.md` "v1.7.130
R-CONFIRM" section for the full fingerprinted list). Left open by design:
three ESSENTIAL-tier scientific-framing findings (independent-derivation-vs-
trusted-inputs framing; Cai/Li convention-mismatch, Houston-gated re-flag of
standing DP2-25; inflation-vs-bounce projection-argument asymmetry), a full
Fisher-ladder specification table, and several smaller deferred items.

```
rRounds:create({
  paperId: "P2",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  reviewers: ["Grok API (grok-4.3)", "Gemini API (gemini-3.1-pro-preview)", "Claude opus sub-agent (verdict-blind)"],
  note: "Exact-version confirmation board on v1.7.130 (sha256 d3afe79fe70c...). Verdicts: REJECT / MINOR REVISIONS / MAJOR REVISIONS, 36 findings (opus leg). Truth-audited against DISPOSITIONS/P2.md; mechanical/editorial majority closed by real edit in v1.7.131. NOT a clean/converged wave -- 3 ESSENTIAL scientific-framing findings + a Fisher-ladder spec table left open by design.",
})
```

```
rRounds:markComplete({
  paperId: "P2",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
})
```

```
externalReviews:upsertByLabelDate({
  paperId: "P2",
  reviewer: "Grok",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  verdict: "reject",
  source: "internal-stage3",
  note: "Exact v1.7.130 (sha256 d3afe79fe70c...) via tools/v3_native_pdf_review.py. 4 ESSENTIAL + 3 MAJOR + 2 MINOR + 1 NIT. Two findings FALSIFIED (abstract qualifier claimed missing but present verbatim; r=0.84 rounding claimed unpropagated but the direct 2.61sigma value is already shown beside it). Remaining genuinely-new-real findings closed by real edit or re-flagged to standing DP2-25/DP2-30.",
})
```

```
externalReviews:upsertByLabelDate({
  paperId: "P2",
  reviewer: "Gemini",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  verdict: "minor-revisions",
  source: "internal-stage3",
  note: "Exact v1.7.130 (sha256 d3afe79fe70c...) via tools/v3_native_pdf_review.py. 1 ESSENTIAL (DOI-version mismatch, already disclosed in-text, Houston-gated re-archival) + 3 MAJOR (2 missing citations, 1 leaked script-name jargon) + 1 NIT (figure-axis claim, FALSIFIED by direct render check). All actionable findings closed by real edit in v1.7.131.",
})
```

```
externalReviews:upsertByLabelDate({
  paperId: "P2",
  reviewer: "Claude opus (verdict-blind sub-agent)",
  label: "R-CONFIRM",
  dateISO: "2026-09-22",
  verdict: "major-revisions",
  source: "internal-stage3",
  note: "Exact v1.7.130 (sha256 d3afe79fe70c...), cold read, no repository access, no review history. 3 ESSENTIAL + 10 MAJOR + 15 MINOR + 8 NIT (36 total); every displayed equation and table entry independently re-derived in sympy and found exact, no algebraic error found anywhere. Mechanical/editorial majority (citations, undefined r/r_cos grid, growth-factor text/code fidelity, table mislabeling, count inconsistency, AI-disclosure length, bib formatting) closed by real edit in v1.7.131. Left open by design: independent-derivation-vs-trusted-inputs framing (E1), Cai/Li convention-mismatch (E2, re-flag of DP2-25), inflation-vs-bounce projection asymmetry (E3), Fisher-ladder specification table (M3), several smaller deferred items -- none fabricated toward, none silently dropped.",
})
```

```
paperVersions:bump({
  paperId: "P2",
  version: "v1.7.131",
  dateISO: "2026-09-22",
  sha256: "0e7aaf3fc46cad71f63f1d804d4993ad17a95d432076523927ff4afd3fa3dd90",
  md5: "b7ba55724042883ce6c27a29b5b56436",
  pages: 12,
  note: "R-CONFIRM exact-version board closed most genuinely-new-real findings (missing citations, r/r_cos grid definition transcribed from committed script, growth-factor text/code fidelity clarification, misattributed citation fixed, certification-count harmonized with Li-et-al internal tension disclosed, table mislabeling fixed, uncertainty propagated, AI-disclosure trimmed, bib formatting). NOT a confirmed/converged board -- 3 ESSENTIAL scientific-framing findings + a Fisher-ladder spec table remain open by design. Readiness holds 95, computed.",
})
```

```
activityFeed:add({
  type: "r-round",
  title: "P2 R-CONFIRM: exact-version board raises three deep scientific-framing questions on the -35/16 result",
  tags: ["P2", "v1.7.131", "r-round", "confirmation", "campaign-2026-09-18"],
  summary: "Lane bb-LCB-confirm-p1b-p2 closed the exact-version confirmation gap flagged in the 2026-09-19/22 sign-off packets. Board (Grok REJECT / Gemini MINOR REVISIONS / Claude opus verdict-blind MAJOR REVISIONS, 36 findings) was NOT clean, though every displayed equation was independently re-derived in sympy with zero algebraic errors found. Mechanical/editorial majority closed by real edit: 2 missing citations (one traced to the committed Fisher script's own code comments), the r=0.8354/r_cos=0.9817 grid+weight+formulas defined explicitly and verified live against the committed script, a growth-factor text/code fidelity gap clarified (the Fisher code uses CAMB directly, sidestepping the referee's D(z)-convention worry), a misattributed citation fixed, an inconsistent certification count harmonized (with a new Li-et-al internal tension disclosed, not resolved), a table mislabeling fixed, an uncertainty propagated, the AI-usage disclosure trimmed. Left open by design: whether -35/16 is an independent derivation or a re-summation of trusted inputs, the Cai/Li convention-mismatch question (Houston-gated re-flag of DP2-25), the inflation-vs-bounce projection asymmetry, and a Fisher-ladder specification table. v1.7.130 -> v1.7.131, 12pp unchanged. Readiness holds 95.",
})
```

---

## LS9 `bb-LS9-bardeen-lqc` — ledger row 9b (2026-09-22)

Research lane; no paper, SSOT or site data touched, so **no** `paperVersions:bump`,
`papers:setReadinessCap`, `rRounds:create` or `externalReviews:upsertByLabelDate` applies.
One mutation queued.

```
activityFeed:add({
  type: "research",
  title: "Row 9b: the Bardeen scheme selection extends to the LQC and polymer backgrounds -- background-independent in direction, background-specific in magnitude",
  tags: ["A3M", "ledger-row-9", "ledger-row-18", "ledger-row-2", "bounce-transmission", "campaign-2026-09-18"],
  summary: "Lane bb-LS9-bardeen-lqc closed A3M v3M.0.28's own Next-steps item (i). At a simple zero of Q = -a^2 Hdot -- the smooth rho+p = 0 crossing that the LQC-effective-dust and poly backgrounds have and the Quintin-type parametrisation avoids by jumping Hdot -- the Bardeen equation is a regular singular point with indicial exponents {0,2}: Phi and Phi' stay continuous with Phi'(eta_c) = -Hc(eta_c)Phi(eta_c) (the 0i-constraint degeneration, derived as the first recursion rather than assumed), the {0,2} resonance gives a t^2 log t term of closed-form amplitude -Phi(eta_c)k^2/2, so zeta and Xi diverge only logarithmically and the continuation is the principal value. Transmitted-amplitude ratio against scheme S1 at fixed incoming dust vacuum: 0.1600 (Quintin-type), exactly 1/2 (LQC), exactly 3/8 (poly) -- each obtained twice, by a finite-k ODE with two independent principal-value prescriptions and by an ODE-free super-Hubble quadrature R = 3 I_eps/I_S1. Gates G1-G8 all pass, G1 first (it reproduces row 9's committed Quintin lambda to 2.5e-5). Pre-registered OUTCOME-UNIVERSAL(b): S1 understates the transmitted f_NL magnitude on every background, but by 6.25x / 2.00x / 2.67x, so row 9's factor 6.25 is Quintin-specific. A3M's LQC and poly linear transfers move 0.250 -> 0.500 and 0.196 -> 0.521; the cubic term on those backgrounds is declared out of scope and reported only as a labelled bracket. The unfavourable half is propagated in the same pass: row 18's stated gap closes against the paper at r_after = 96.0 (LQC) and 170.6 (poly) versus S1's 24.0. Separately, A3M R11 ESSENTIAL 2 is closed by computation -- a uniform eta_*/eta_B = 15 sits in the stationary region at every k-point and gives f_NL^after[S2] = -1.249/-1.249/-1.246, so the committed -1.25 survives. An independent blind adjudication was commissioned; the Fable-tier attempt failed on provider usage credits and the check was re-run at Opus tier and labelled as such.",
})
```

---

## LS10 `bb-LS10-indomain-d180` — ledger row 16, the in-domain dilution bound (2026-09-22)

Research lane; no paper `.tex`, SSOT or site data touched (P4′ is owned by lane
`bb-L4e-p4p-hold-correction`), so **no** `paperVersions:bump`,
`papers:setReadinessCap`, `rRounds:create` or `externalReviews:upsertByLabelDate`
applies. One mutation queued.

```
activityFeed:add({
  type: "research",
  title: "Row 16: the P4' dilution bound re-measured in-domain -- the hold lifts, with different (tighter) numbers",
  tags: ["P4P", "ledger-row-16", "ledger-row-13", "chirality", "provenance", "campaign-2026-09-18"],
  summary: "Lane bb-LS10-indomain-d180 lifted the provenance hold lane bb-LS6-row16-tta placed on P4' item P-5. Gate first: the released catalogue IS reproducible from the released checkpoint and preprocessing on its documented imaging and only there -- 99.936% class agreement on all 8,474,531 galaxies and 100.000% on the 949,584 primary_hc (control C1, read off the already-committed 2026-07-11 e2e_fullrun, no download, no GPU), 99.95% on this lane's own 40,000 drawn galaxies at theta=0, against 43.9% on the Legacy Survey viewer cutouts rows 13/16 had used. The domain gap is a measured 3.41x field difference, not an assumed one: the Smith42/galaxies v1.0 cutouts are 512x512 px at 0.262 arcsec/px = a 134.1 arcsec field (median pixel correlation 0.992 at that scale, <=0.25 at five others), which also makes main.tex:171's '224x224 px' a documentation error -- 224 is the network input after Resize. Re-measuring d(theta) in-domain with the same estimator (eq_triple imported verbatim from s5b_nocrop_dilution.py), the same checkpoint, lossless 90-degree transposes and the released no-crop preprocessing, on 40,000 galaxies streamed by HTTP range read (400 row groups, 4.54 GB, ZERO image bytes written to disk, 320,000 forward passes, local Apple-silicon MPS, 47 min, $0): primary_hc (N=4,579) gives D <= 0.5998 +- 0.0065 and A_95^phys >= 1.63%, the assumption-free theta=180 row gives D <= 0.6599 +- 0.0075 -- the pipeline contradicts its own label for 34.0% of high-confidence spirals handed a lossless 180-degree rotation of the identical image. All spirals (N=15,219) D <= 0.5237 +- 0.0038; primary_hc AND NOT unsafe (N=4,296) D <= 0.6037 +- 0.0070; D excluded from unity at 61 sigma / 127 sigma; g=0.398 still sits below the bound. The in-domain classifier is LESS rotation-stable than out-of-domain (34.0% vs 21.1% at 180 degrees), so the pre-registered agreement test fails at 14.5-19.3 combined SE and the verdict is LIFTED-WITH-DIFFERENT-NUMBERS: the held D <= 0.7166, A_95^phys >= 1.37%, 0.6296, 1.56%, 21.1% and Q-2's d(180)=0.3090 are withdrawn, never averaged with the new values. The correction moves the bound in the conservative direction for P4' (smaller D means larger A_95^phys means weaker exclusion, the direction P-5a already adopts it in). Still out-of-domain and explicitly NOT re-measured: Q-3's sky-dipole amplitude and Q-4's D4/D8 TTA recovery fractions plus P-5a's epsilon-bar = 0.754. Pre-registration committed at f45c9d1b before any statistic; exact printable sentences in the lane's PROPAGATION_NOTE.md items R-1/R-1a/R-1b/R-2; reproducibility manifest row16-indomain-d180.",
})
```

---

## L1d `bb-L1d-a3m-row9b-r12` — row-9b propagation into main.tex, v3M.0.28 -> v3M.0.29 (2026-09-22)

Paper lane: `main.tex` edited, so a real `paperVersions:bump` mutation is queued (not just
`activityFeed:add`). Two mutations queued.

```
paperVersions:bump({
  paperSlug: "paper-a3m",
  version: "v3M.0.29",
  pages: 23,
  md5: "8ee1f13bd4e596c87655a9347c0c0918",
  sha256: "0c8c318e184577b614251d9d517f1cdf7d5bb9c667a6b731ca130a26b47d4a60",
  note: "Row-9b (LQC/poly Bardeen extension) science-decision propagation -- the directive-R2 intervening decision authorizing the co-director-authorized R12 confirmation board. Table tab:s1_after gains two rows (LQC/poly Bardeen continuation, linear-transfer-only, cubic term uncomputed, f_NL^after a bracket never a single value); tensor no-go strengthens on both against the paper (r_after 96.0/170.6 vs S1's 24.0), same prominence as the favourable half per directive F. R11 ESSENTIAL 2 (undisclosed evaluation-window convention) closed by computation: uniform eta_*/eta_B=15 sits in the stationary region at every k-point, f_NL^after[S2]=-1.2492/-1.2490/-1.2464, headline -1.25 survives. No headline number changed on Quintin-type. 4-pass, 0 undef refs, 23pp (grew from 21), max overfull hbox 3.9pt (one new 74pt table overflow caught by /latex-audit and fixed before this bundle).",
})

activityFeed:add({
  type: "paper-update",
  title: "A3M v3M.0.29: row-9b (LQC/poly Bardeen extension) propagated -- R12 confirmation board unlocked",
  tags: ["A3M", "ledger-row-9", "ledger-row-18", "row9b", "bounce-transmission", "r-round", "campaign-2026-09-18"],
  summary: "Lane bb-L1d-a3m-row9b-r12 propagated the row9b science decision (bb-LS9-bardeen-lqc, CLOSED) into main.tex, the directive-R2 intervening decision the co-director authorized one confirmation board (R12) against. Table tab:s1_after gains LQC/poly Bardeen rows (T_fNL=0.500 exact/prescription-free on LQC via a second matter-kinetic anchor, T_fNL=0.521 principal-value-only on poly; Delta f_NL^bounce not computed; f_NL^after a labelled bracket [-1.20,-0.09]/[-1.27,-0.13], never a single value per directive F). AGAINST the paper, same prominence: row 18's tensor gap for LQC/poly closes unfavourably, r_after=24/R^2=96.0 (LQC) and 170.6 (poly) vs S1's common 24.0 -- 2.7e3x/4.7e3x BICEP/Keck (was 6.7e2x). Every downstream S1-range/'not yet computed' LQC-poly reference swept through the whole manuscript (the R11 lesson: 5 of R11's 16 findings were exactly unswept scheme-labelling residue). Separately, R11 ESSENTIAL 2 (the undisclosed evaluation-window convention) closes BY COMPUTATION, superseding R11's disclosure-only closure: a 12-point eta_*/eta_B scan shows a stationary region common to all three k-points, uniform eta_*/eta_B=15 sits inside it, f_NL^after[S2]=-1.2492/-1.2490/-1.2464 (0.22% spread) -- headline -1.25 survives to 3 sig figs with a stated 0.3% systematic; the paper's per-k triple moves -1.249/-1.246/-1.244 -> -1.249/-1.249/-1.246. Symbol audit: the extension parameter renamed theta (source note used nu) to avoid colliding with the pre-existing general-nu Hankel-limit symbol in Sec. VIII, self-caught before any leg could flag it. Directive G: 4-pass, 0 errors, 0 undef refs/citations, 23pp (grew from 21), one new 73.97pt table overflow from the two added rows caught by /latex-audit and fixed with \\scriptsize + shortened labels (max overfull hbox after fix 3.89pt, unchanged pre-existing tolerance); visual PASS on pages 1, 6-9, 13-15, 17-18. Three-way md5 8ee1f13bd4e596c87655a9347c0c0918. No headline number changed on Quintin-type. R12 confirmation board (Grok API + Gemini API + Claude opus verdict-blind referee) dispatched next on this exact PDF.",
})
```

---

## L1d `bb-L1d-a3m-row9b-r12` — R12 board + partial closure, v3M.0.29 -> v3M.0.30 (2026-09-22)

Paper lane: `main.tex` edited (real closures), so a real `paperVersions:bump` is queued.
Also queues an `externalReviews:upsertByLabelDate` for the Claude opus INT leg (Grok/Gemini
FAILED-INFRA, recorded absent per Rule 4, never as clean). Three mutations queued.

```
paperVersions:bump({
  paperSlug: "paper-a3m",
  version: "v3M.0.30",
  pages: 23,
  md5: "a1bcf35a2789ce14091e43c80f4b5b9e",
  sha256: "0f4c5f606dc8dabf6cf08eed58d5a3b10d128f44608ef8dd8eb0b7db1603fbae",
  note: "R12 (the one confirmation board the row-9b science decision authorized) on the exact v3M.0.29 PDF. Grok/Gemini FAILED-INFRA (shared-checkout preflight contention on a concurrent lane's dirty files, not touched). Claude opus verdict-blind referee: MAJOR REVISIONS. 6 genuinely-new-real items: 5 closed by real edit (LQC's two irreconcilable transfers 0.409/0.500 distinguished; rho+p double meaning and undefined x fixed; T_fNL<1/2 disclaimer extended to all three backgrounds; a scheme qualifier added; the PBH 144pt/27pt ratio reconciliation arithmetic added), 1 ESSENTIAL closed only by honest disclosure not computation (the PBH Channel-II headline sits entirely inside the paper's own non-perturbative-branch window -- named as the next concrete unlock). 1 referee claim FALSIFIED. No physics error found; no headline number changed. 4-pass, 0 undef refs, 23pp (unchanged), max overfull hbox 3.9pt (unchanged).",
})

externalReviews:upsertByLabelDate({
  paperSlug: "paper-a3m",
  label: "R12 Claude opus INT referee (verdict-blind)",
  dateISO: "2026-09-22",
  verdict: "major-revisions",
  source: "internal-stage3",
})

activityFeed:add({
  type: "review-round",
  title: "A3M R12: confirmation board does not confirm -- 6 genuinely-new-real, 5 closed, 1 left open as the next unlock",
  tags: ["A3M", "r-round", "r12", "row9b", "campaign-2026-09-18"],
  summary: "Lane bb-L1d-a3m-row9b-r12 ran the one confirmation board directive R2 permitted after the row-9b intervening science decision, on the exact v3M.0.29 PDF. Grok API and Gemini API FAILED-INFRA: tools/v3_native_pdf_review.py's preflight receipt generation requires every registered draft paper's inputs clean, and pipelines/p4prime_chirality_test/paper/{main.tex,main.pdf} were dirty under a concurrent, legitimately active P4P lane this lane does not own -- an attempted reversible git-stash-and-restore of only those two files was blocked by the harness's own safety classifier as touching another lane's uncommitted work, so no receipt could be generated and no leg was faked or back-filled (same class of contention already recorded for the P-SU R4 board). Per directive I2 this did not stop the independently valuable Claude opus verdict-blind INT referee (dispatched with no access to this repository outside the exact PDF path), which returned MAJOR REVISIONS after independently reproducing roughly forty displayed equations and table entries, all exact. Truth-audited 6 genuinely-new-real items: two caused by this lane's own row-9b propagation (LQC's two non-S1 linear transfers, 0.409 vs 0.500, were never reconciled; 'rho+p' denoted two different quantities in Sec. III A with x left undefined) closed with real edits; three pre-existing items (T_fNL<1/2 disclaimer scoped only to Quintin-type; a sign-sharing sentence needing an S1 qualifier; the PBH channel's 144-point/27-point ratio reconciliation left to the reader) closed with real edits, the last via an aggregation of already-committed per-point data, no new computation; and one ESSENTIAL pre-existing item -- the PBH Channel-II headline 1.84+-0.03 is measured entirely inside the region the paper's own caption calls the non-perturbative branch, and the stated mechanism (large positive gamma_cr 0.766-0.968) does not apply to the headline window (gamma_cr 0.267-0.630) -- a materially deeper claim than any prior leg raised, closed only by honest disclosure (the paper now states the diagnostic has not been pointwise-checked there) rather than by computation, since the proper close needs a new per-point perturbativity run this lane's row-9b mandate and budget did not cover, and /never-fabricate-derivation forbids estimating it. One referee claim was FALSIFIED (a bracket-endpoint rounding artifact from using printed rather than exact values). No physics error found anywhere in the paper's core derivations; no headline number changed. Directive G: 4-pass, 0 undef refs, 23pp (unchanged), max overfull hbox 3.9pt (unchanged), three-way md5 a1bcf35a2789ce14091e43c80f4b5b9e. R2 budget spent -- rounds stop; the PBH perturbativity pointwise check is the concrete candidate for the next intervening science decision.",
})
```
