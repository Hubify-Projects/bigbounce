# M37-EXT truth-audit — P5 (v0.1.127, byte-unchanged)

**Raws READ verbatim before any verdict:** `P5_grok_M37.md` (MINOR REVISIONS, 0 MAJ/4 MIN),
`P5_chatgpt_M37.md` (MAJOR REVISIONS, 10 MAJ/3 MIN). Verdict lines literal in each raw
(Grok l.1 `VERDICT: MINOR REVISIONS`; ChatGPT l.1 `(1) VERDICT: MAJOR REVISIONS`).

**Provenance:** Both raws review the DESIVAST void / spiral-chirality paper (∆f_CW, VoidFinder,
T-Web, 2.26-pp de-attenuation, Paper-IV κ=0.40, ≈0.9-pp systematic envelope, Bonferroni-5 family) →
correct paper. ✓

**ledger_match (tools/ledger_match.py P5):** Grok 3/5 auto-MATCHED (2 UNMATCHED: #1 scaffold-header
non-finding + #5 monopole-reconciliation low-score); ChatGPT 11/14 auto-MATCHED (3 UNMATCHED: #1
scaffold-header non-finding + #7 monopole-cancellation-scope + #10 theory-scale interpretation). Every
finding below adjudicated with a source-cited D-id verdict, matched or not.

---

## SPECIAL HARD CHECK — DP5-26 (artifact-ID range descriptor [A1]--[A32]) ABSENCE

DP5-26 fingerprint (ledger l.165-169): the reader-visible in-PDF strings asserting the artifact index
runs `[A1]--[A32]` (acknowledgments AI-methodology para + Appendix C numbering note + table caption),
stale vs the artifact-map table now running through `[A34]`. CLOSED-BY-EDIT v0.1.127.

- **Grok M37:** `grep -niE 'artifact|\[A1\]|\[A32\]|\[A34\]|\[A33\]|A1--A|artifact index|artifact-map'` →
  **NONE.** The artifact-range descriptor is not re-raised.
- **ChatGPT M37:** one grep hit (l.49) is the phrase "all analysis **artifacts** are version-locked by
  commit hash" inside the Paper-IV companion-dependency MAJOR (→ DP5-21) — this is NOT the DP5-26
  artifact-ID range descriptor; no `[A1]`/`[A32]`/`[A34]` range string, no artifact-index numbering claim.

**CONFIRMED: DP5-26 is ABSENT from BOTH raws.** The v0.1.127 artifact-range fix STAYS HELD (same result
as M29/M31/M34; the reader-visible `[A1]--[A32]` range is gone from the served PDF and neither fresh EXT
read re-flags it).

---

## Grok (MINOR REVISIONS, 0 MAJ / 4 MIN) — ledger_match 3/5 auto; #1 scaffold-header non-finding

| # | finding (raw) | verdict | D-id + source-cited disposition |
|---|---------------|---------|----------------------------------|
| 1 | scaffold parse header `REVISIONS ISSUES:` | non-finding | Parser artifact (score 0.00), not a reviewer finding. |
| 2 | Abstract/§I companion catalog cited only as `arXiv:XXXX.XXXXX` placeholder; needs real ID / DOI. | **RE-FLAG** | **DP5-21** (OPEN-VENUE): "placeholder arXiv IDs … acceptance framed as conditional on co-review of Paper IV" (ledger l.153-157; fingerprint "placeholder arXiv, coordinated submission"). Houston-gated venue barrier, not an editable defect. |
| 3 | §V B / abstract: DESIVAST path is post-hoc "exploratory, not pre-registered"; abstract must MORE prominently label DR1 exploratory (current "designated-primary" insufficiently cautious). | **RE-FLAG** | **DP5-13** (RE-FLAG-DISCLOSED): §V B `sec:primary_path` l.1668 + `tab:analysis_tree` l.1848 disclose post-hoc designation + "no timestamped plan predates the data"; abstract l.729-730 labels bounds exploratory (ledger l.99-103). Score 0.88. Presentational emphasis request. |
| 4 | §VIII / Table XI: ≈0.9-pp "honest effective 2σ systematic envelope" quadrature terms not tabulated individually / sum not shown explicitly; wants supplementary table or equation block. | **RE-FLAG** | **DP5-11** (RE-FLAG-DISCLOSED): §VIII gives the explicit term list + √0.886=0.94pp; Eq.(4)/`eq:sys_budget` displays the eight-term multline (DP5-25, seven→eight fix v0.1.126). Method fully disclosed; "prefer a calibrated joint interval" = OPINION on statistical philosophy, honestly presented (ledger l.86-90). Score 0.55. |
| 5 | §II / §VIII F: internal P5 matched-sample monopole f_CW^P5=0.49719 stated consistent with Paper IV −0.0026 offset; ~8% amplitude difference "reconciled in §VIII F" but reconciliation terse; wants one-sentence derivation of the 0.0002 shift. | **RE-FLAG** | **DP5-11 / DP5-08** (RE-FLAG-DISCLOSED): the §VIII.F monopole-reconciliation item is the disclosed reconciliation paragraph (M29 audit mapped §VIII.F reconciliation → DP5-11/-08; ledger DP5-09 fingerprint "monopole cancels algebraically … §VIII F"). Monopole enters σ_pred only and cancels in the Δf_CW difference (DP5-08 l.66-72). Score 0.27 (low overlap, but Opus-confirmed RE-FLAG: a request to expand a disclosed reconciliation paragraph, not a new numeric defect). |

**0 genuinely-new.** Same disclosed-content set as M28/M29/M31/M34 Grok (post-hoc primary DP5-13 +
envelope DP5-11 + Paper-IV DP5-21 recur every read = cross-run stability). Grok's one-sentence: the
central ≲2.3-pp null "is supported by the large-sample, multi-algorithm null results and explicit
systematic envelope" — endorses the claim.

---

## ChatGPT (MAJOR REVISIONS, 10 MAJ / 3 MIN) — ledger_match 11/14 auto; 3 UNMATCHED Opus-adjudicated RE-FLAG

| # | finding (raw) | verdict | D-id + source-cited disposition |
|---|---------------|---------|----------------------------------|
| 1 | scaffold parse header `REVISIONS (2) ISSUES:` | non-finding | Parser artifact (score 0.00), not a reviewer finding. |
| 2 | §VIII B/E footprint-restricted control = author union of void-hole discs ∩ radial span, NOT DESIVAST/BGS completeness mask/randoms; recompute w/ official mask or per-void matched/IPW; Table XII uses unrestricted 621,964 control. | **RE-FLAG** | **DP5-06** (RE-FLAG-DISCLOSED): §VIII B "Footprint ≠ selection function" para (tex l.3033) states the footprint is the geometric hole-disc ∩ radial union, explicitly NOT the mask/vetoes/randoms, residual folded into `tab:systematic_budget` (ledger l.54-58). IPW/matched control = DR2-deferred robustness item. Score 0.32. |
| 3 | §V B / §VIII B / Tables X, XIV multiplicity: primary = exact footprint-restricted 57,081/+0.0018 but Table XIV VoidFinder member = k=20 unrestricted 56,981/+0.0007; Bonferroni-5 family doesn't contain the advertised primary. | **RE-FLAG** | **DP5-01 / DP5-02** (CLOSED-BY-EDIT v0.1.114/115): §XV rewritten to lead +0.0018@57,081; exact-membership row added; k=20 rows relabeled sensitivity control (ledger l.24-34). Score 0.72. (post-hoc-correction-doesn't-fix-forking-paths tail → DP5-13.) |
| 4 | §VIII C–E five void estimators: point-in-effective-radius-sphere for REVOLVER/VIDE is author-created; VoidFinder hole-union is permissive proxy; mixed with official GALZONE on different 145,789 parent; 0.60-pp any-hole→maximal-sphere change > headline contrast. | **RE-FLAG** | **DP5-16** (RE-FLAG-DISCLOSED): `tab:desivast_three_algo` caption l.3310 states sphere-PIS is "an author-constructed approximation … not the catalog-native definition," VoidFinder any-hole "a permissive proxy"; GALZONE rows ARE the official definitions tabulated (ledger l.117-121). 0.60-pp membership-convention = disclosed geometry term (DP5-06 fingerprint). Score 0.83. |
| 5 | Table XI/Eq.(4): "honest 2σ envelope" = quadrature of counting interval + correlated peak-shifts is not a defined CI; terms correlated/uncalibrated; confidence+match-radius are full-sample shifts not primary-contrast shifts; RSD computed for unrestricted; 0.9-pp conflicts w/ ~1.1-pp Bonferroni bound. | **RE-FLAG** | **DP5-11** (RE-FLAG-DISCLOSED): envelope method + term list disclosed; peak-excursions-vs-SDs stated; "prefer a calibrated joint interval" = statistical-philosophy OPINION (ledger l.86-90). Cluster/coverage tail → DP5-10 (OPEN-COMPUTE). Score 0.55. |
| 6 | §V/§VIII B uncertainty model: binomial galaxy-level SE treats ~10⁵ labels as independent Bernoulli; galaxies share voids/imaging/sky/target/classifier systematics → understated at sub-percent; label-shuffle destroys correlated structure; needs void-level/angular-block jackknife/cluster-sandwich/hierarchical. | **RE-FLAG** | **DP5-10** (OPEN-COMPUTE): CI explicitly labeled "counting-statistics-only … not a full systematic budget"; cluster/void-level bootstrap is the disclosed open recompute item (ledger l.80-84). Score 0.44. |
| 7 | §II/VIII F/XI/App A monopole cancellation: literal constant additive monopole cancels but paper finds program/imaging/confidence dependence + size/mag/inclination/SB/morphology not shown balanced → establishes only a classifier-label difference under unverified nondifferential-error assumption. | **RE-FLAG** | **DP5-08 + DP5-09** (score 0.29, UNMATCHED): algebraic-cancellation claim correctly scoped to the catalog-wide monopole, NOT env-dependent per-galaxy relabeling — handled via the v0.1.118 void-stratified confusion matrix (`gz1_stratified_confusion.json`, diff −0.018 z=−0.89 p=0.37, ±3.7pp corroborates-but-cannot-exclude → DP5-09 caveat STAYS); reviewer cites the paper's OWN disclosed differential-error axis (ledger l.66-78; identical to RS2b UNMATCHED#9 disposition l.337). |
| 8 | Abstract/§XII B/App A de-attenuation 1/(2a−1) valid only for known symmetric nondifferential CW/CCW rates; global accuracy floor insufficient; uncertainty not propagated; void-specific validation ±3.7-pp asymmetry >> 0.9-pp bound → remove 2.26-pp or use latent-class/error-matrix. | **RE-FLAG** | **DP5-08 / DP5-09** (RE-FLAG-DISCLOSED): abstract l.749-757 flags the symmetric-error approximation; §XII B/App A carry the caveat + label the physical bound the weaker quantity; the ±3.7-pp void-arm CI is the paper's OWN v0.1.118 measurement corroborating-but-not-excluding (ledger l.66-78). Score 0.53. |
| 9 | §VIII RSD: perturbing distances w/ fixed void catalog tests only boundary sensitivity; displacing holes+galaxies together w/o reconstructing tracer field + rerunning void finder can't capture detection/radii/merging/topology changes → 0.024-pp shift doesn't bound RSD; remove from Table XI. | **RE-FLAG** | **DP5-12 / DP5-22** (CLOSED-BY-COMPUTE first-order v0.1.122): first-order Zel'dovich reconstruction (Hamaus et al. 2014 profile) displaces galaxies+holes together, 0.024-pp bound; the full nonlinear catalog re-derivation (re-run VoidFinder on reconstructed field) is the paper's OWN disclosed residual tex l.847-850 (ledger l.92-97). Score 0.35. |
| 10 | §I/XII B/XV/App B theory: primary DESIVAST estimator not defined at T-Web R_s=25 Mpc/h scale (that's secondary); no transfer calc maps winding/membership/classifier errors to a parity parameter; "≳25 Mpc/h" bound unsupported; App B noncovariant toy operator remove/relegate. | **RE-FLAG** | **DP5-20 + DP5-14** (score 0.27, UNMATCHED): App B + Conclusions already label the EFT mapping "speculative … outside the empirical scope … not a derived constraint," relegated (DP5-20 l.147-151); the 25-Mpc/h scale is the secondary T-Web channel, disclosed secondary/diagnostic (DP5-14 l.105-109). Same class as M14/M22 UNMATCHED "no-forward-model / parity-even-operator" (ledger l.8, l.5). |
| 11 | §XIII/App A,D companion dependency: per-galaxy labels are indispensable input yet Paper IV has arXiv placeholder + pending DOI; movable repo tag ≠ archival record; cannot accept before Paper IV supplied + version-locked by commit hash + archival DOI. | **RE-FLAG** | **DP5-21** (OPEN-VENUE): §I "Independence from Paper IV internals" + §XIII + App A disclose public labels + coordinated submission; a known venue/coordination barrier, Houston-gated, not an editable defect (ledger l.153-157). Score 0.56. (NOT DP5-26 — this is the companion arXiv/DOI dependency, not the in-PDF artifact-index range descriptor.) |
| 12 | §IV/VI/IX canonical T-Web: random-catalog rebuild changes ~73% of matched-galaxy environment labels + reduces void volume fraction ~23×; T-Web dominated by selection function; condense/replace w/ completeness-weighted; must not support physical-scale/robustness claims. | **RE-FLAG** | **DP5-14** (RE-FLAG-DISCLOSED): T-Web explicitly secondary/diagnostic/not-load-bearing (abstract l.718); the ~73%/~23× randoms sensitivity is the paper's OWN disclosure driving the demotion (ledger l.105-109). Score 0.58. |
| 13 | Figs 6, 9 denominators: Fig 6(a) "maximal voids per pixel" but 3,303-pixel / 50–734 range = matched-spiral sky scan not DESIVAST maximal-void map; Fig 9 T-Web sample 791,635 but four class counts sum 812,793 row-level; distinguish unique galaxies vs repeated rows. | **RE-FLAG** | **DP5-22** (RE-FLAG-DISCLOSED): figure legibility + the 791,635/812,793 unique-vs-program-row reconciliation is the standing D-round cosmetic-polish item, already reconciled (ledger l.159-163; M9/M22 mapped Fig 6/9 counts → DP5-22). Score 0.33. Cosmetic, no science defect. |
| 14 | Abstract/Conclusions: "null holds," "environment independence," "leaving no room" overstate a post-hoc non-detection; report as exploratory absence w/ asymmetric CIs + (if practical equivalence) prespecified equivalence margin + formal test. | **RE-FLAG** | **DP5-13 / DP5-19** (RE-FLAG-DISCLOSED): abstract labels bounds exploratory (DP5-13 l.99-103); non-rejection≠independence + equivalence-interval framing is DP5-19's disclosed presentation preference (ledger l.141-145 fingerprint "non-rejection not evidence, environment independence, formally defined equivalence"). Score 0.50. |

**0 genuinely-new reader-visible editable.** Same disclosed-content set as M14/M17/M19/M22/M31/M34
ChatGPT (footprint≠selection, Bonferroni-5 family, 0.9-pp envelope, binomial-independence OPEN-COMPUTE,
de-attenuation, monopole-scope, RSD-first-order, T-Web-secondary, EFT-toy, Paper-IV-venue). ChatGPT's
own Q3 concedes "the data support a qualitative non-detection … in the classifier-assigned labels."

---

## Verdict

- **ChatGPT MAJOR (M37)** = the modal ChatGPT P5 verdict (MAJOR on M14/M34/M37; the reject↔major
  oscillation on byte-unchanged v0.1.127 is the documented maximal-harsh-referee structural floor,
  pattern-066 — does NOT itself drive the streak).
- **Grok MINOR (M37)** — central null endorsed; 4 minors all standing re-flags.
- **0 genuinely-new reader-visible editable findings across BOTH legs** — every finding fingerprint-matches
  a canonical DP5 disposition with a source-cited verdict → **no bump (v0.1.127 stands), directive_g.sh
  NOT run** (no edit).
- **DP5-26 ABSENT from both raws → v0.1.127 artifact-range fix STAYS HELD.**
- **Clean-wave streak 3 → 4** (M31 streak 1→2, M34 streak 2→3, M37 streak 3→4 — fourth consecutive
  0-genuinely-new wave on the post-DP5-26 v0.1.127 content). Per directive-K a genuinely-new finding on
  any paper would reset this count; none surfaced.
- **Cap: post_verdict.sh authoritative** — latest-per-reviewer (by _creationTime): Grok MINOR 12 +
  ChatGPT MAJOR 6 + latest-Gemini carry = holds the M34 computed 74 (no verdict-tier change from M34:
  Grok MINOR unchanged, ChatGPT MAJOR unchanged). Recorded per post_verdict.sh recompute, not hand-set.

**Integrity:** both raws READ verbatim before any verdict; verdict lines quoted literal; no ACCEPT
faked; every finding source-cites a tex line / artifact / ledger D-id; no finding dismissed without a
source-cited verdict; no math fabricated. The two UNMATCHED ChatGPT MAJORs (#7 monopole-scope, #10
theory-scale) and the low-score Grok #5 were Opus-adjudicated against the ledger + tex, not force-matched.
