# P2 Truth Audit — Round H17 (2026-07-10)

Paper: `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.107 → v1.7.108)
Owner-agent: P2. Raws audited: `EXT_real/H17_2026-07-10/P2_grok.md` (2 MAJOR + 3 MINOR),
`INT_api/H17_2026-07-10/P2_claude.md` (MAJOR), `API_P2_openai.md` (REJECT, 18 MAJOR),
`API_P2_grok.md` (MINOR ×5). ChatGPT/Gemini EXT raws still cooking — deferred.

**Method:** every quantitative claim re-derived from the committed scripts (exact-fraction sympy),
NOT from the raws' framing. Independent second sympy re-derivation spawned and matched.

---

## GROUND TRUTH established this round (committed-artifact re-derivation)

Ran `scripts/p2_vertex_check.py`, `scripts/caili_certification/{cai_vertices,cai_shape,cai_conv,cai_reconcile}.py`
and an independent from-scratch sympy re-derivation. Results (all exact fractions):

| Object | squeezed fNL | equilateral fNL | source |
|---|---|---|---|
| Sum-of-vertices (Cai's own 4 vertices) | **−35/16** = −2.1875 | **−255/128** | `cai_vertices.py`, `p2_vertex_check.py` (6-perm) |
| Cai ε-order-grouped intermediates | **−35/16** | −255/128 | `cai_reconcile.py` |
| Li Eq.(5.1) at c_s=1 | **−35/16** | — | `final_check.py` |
| **Coded "printed A_T" (Cai Eq.37 as transcribed)** | **−305/64** = −4.766 | **−585/128** | `cai_shape.py`, `cai_conv.py` (all conventions) |
| `A_T − Σvertices` (exact) | **−(99/128) Σkᵢ³** | (uniform local shift −165/64 = −2.578) | `cai_vertices.py:32` prints `A_total − A_T = +99/128 Σk³` |

Two hard facts the paper's current text contradicts:
1. **The coded printed A_T does NOT reduce to −35/8 (= −4.375).** It reduces to **−305/64 (= −4.766)** in every convention (`cai_conv.py`: perm6/half × ordered/unordered all give −305/64 or −605/256, never −35/8). Cai's *published* −35/8 is therefore not reproduced by the transcribed printed polynomial.
2. **The spurious-term SIGN in Eq.(spurious) is wrong.** Script gives `Σvert − A_T = +99/128 Σk³` ⟹ `A_T − Σvert = −(99/128)Σk³`. Paper's Eq.(spurious) (line 1414) and abstract (line 827) write `A_T − Σvert = +(99/128)Σk³` — **opposite sign**. A −99/128 local term shifts fNL by −165/64 = −2.578, taking −35/16 → −305/64 (consistent with fact 1); the +99/128 the paper prints would shift the wrong way (+2.578).

The headline value **−35/16 is SOLID and unaffected** — certified 4 independent ways (per-vertex sum, ε-order group, Li Eq.5.1, collapsed degree-9 polynomial). No fabrication in the value.

---

## Per-finding verdicts

### Grok EXT MAJOR #1 — Cai-correction only summarized; reproduce explicit per-vertex + the exact spurious-term step
**VERDICT: PARTIALLY REAL / NEW-REAL-EDITABLE (reframed).** App. A already contains Table VII
(`tab:vertexwalk`, per-vertex squeezed+equilateral), Table VI (`tab:vertices`, the four shape rows
from arXiv:0903.0631 source), the collapsed degree-9 polynomial Eq.(23), and the ε-order-grouped
Eq.(24) — so the per-vertex reduction IS explicit and self-contained. What is NOT self-contained
and is in fact **internally inconsistent** is the "printed-A_T → −35/8 via a +(99/128)Σk³ spurious
term" narrative: the committed A_T gives −305/64 (not −35/8) and the sign is −99/128 (not +99/128).
Grok, INT-Claude, and INT-OpenAI all independently flag exactly this. **Fix (this round):** correct
the sign to −(99/128)Σk³ everywhere (abstract line 827, Eqs. spurious 1414 + 1479, prose 1492/1494);
state honestly that the *coded* printed polynomial reduces to −305/64 and that Cai's *published*
−35/8 is a further (separately-published, non-reproducible-from-his-printed-coefficients) value, so
the −99/128 term is *one identified discrepancy between the vertex sum and the transcribed printed
polynomial*, not the sole mechanism producing Cai's stated −35/8. This is the honest self-contained
statement the artifacts support. The decisive, self-contained evidence for the paper's actual claim
(−35/16 is correct) is the vertex-sum + order-group + Li cross-check, all fully displayed.

### Grok EXT MAJOR #2 — 1.3–2.75σ headline from heterogeneous endpoints w/o joint covariance
**VERDICT: REAL / PRESENTATION-EDITABLE (mostly already disclosed; tighten headline).** Paper already
labels the range a "scoping sensitivity envelope … not a joint-covariance forecasted measurement
precision" (lines 1192, 1388) and §VII opens with an explicit up-front scope statement. But the
*envelope* is still carried as the headline number (abstract, conclusion). Honest fix: subordinate
the envelope to sensitivity brackets and make the single well-defined central Fisher significance the
headline, stating plainly the endpoints are not statistically comparable. NOT inventing a joint
Fisher (would be fabrication) — reframing. Applied in this bundle at the abstract + conclusion.

### Grok EXT MINOR (a) — cubic-transmission gradient coefficient never computed
**VERDICT: REAL / already ~90% disclosed — tighten.** Assumption (d) bound δfNL≲10⁻³ is an
order-of-magnitude single-clock scaling estimate; coefficient of leading gradient correction not
computed. Paper says explicit 3rd-order eval "not required." Honest fix: keep the OOM label, add one
sentence stating what a full computation would require (explicit 3rd-order in-in through the LQC
dressed-metric bounce with the subleading gradient operator) and why the OOM stands (single-clock,
no new dof, (kη_bounce)²∼10⁻⁴). Applied.

### Grok EXT MINOR (b) — r_eff robustness unquantified
**VERDICT: REAL / editable one-sentence caveat.** r=0.84 (flat-weight cosine) vs r_eff≈0.99
(survey-optimal Fisher) reconciliation is attributed to squeezed weighting but the tree-level Fisher
limitations (Gaussian diagonal covariance, b2/bs2 fixed, linear k_max, no FoG) are not propagated to
an uncertainty band on r_eff. Honest fix: add explicit caveat that r_eff is not error-banded and the
0.84 (conservative) is what all quoted significances use. Applied.

### Grok EXT MINOR (c) — density / duplicated numbers
**VERDICT: REAL / cheap cleanup.** r=0.84 and Bayes-factor statements recur with slightly varying
endpoints. Fix: unify to single canonical statements with cross-refs where cheaply done. Applied
where non-disruptive; full 38→shorter restructure is a larger job dispositioned as presentation-scope
(does not change any number).

### INT-Claude MAJOR — Eq.(spurious) sign + "inflates to −35/8" arithmetically wrong; A_T→−305/64
**VERDICT: REAL / NEW-REAL-EDITABLE.** Confirmed exactly (see Ground Truth). Claude mis-stated the
script's print direction but its conclusion is correct: sign is −99/128, A_T→−305/64, a single local
term cannot "double" −35/16→−35/8. **Same fix as Grok MAJOR #1.** Claude's secondary items:
- Table VII provenance ("transcribed from p2_vertex_check.py" but that script prints only the total):
  **REAL / editable.** Fix: re-attribute Table VII to the per-vertex computation and/or add the
  per-vertex print loop; values themselves verified correct by hand + independent re-derivation.
  Dispositioned: attribution wording corrected this round; script-loop add is a follow-up (values are
  independently certified, so not a math defect).
- Stale `fig_4vertex_sum.py` still encoding −35/8: **REAL / editable (not in PDF).** Disposition:
  mark deprecated in a follow-up hygiene pass (not \includegraphics'd, so no figure corruption;
  directive-I6 figure-image check N/A here). Flagged, not blocking this bundle.
- Convention-dependence under-disclosed / c13-c14 σ unverifiable-in-session: **OPEN (non-blocking).**
  Values internally arithmetic-consistent; caption already declares the 6-ordered-perm convention.

### INT-OpenAI REJECT — 18 MAJOR
- MAJOR 2 (spurious term wrong sign/magnitude) + MAJOR 3 (Li/Cai printed-polynomial contradiction):
  **REAL** — same root cause as above; fixed by the honest reframe.
- MAJOR 1, 4, 5, 6 (App A not full in-in derivation; cubic-transfer overclaimed; (d) "weakest link"
  vs "closed"): **RE-FLAG of already-disclosed scope** — the paper explicitly frames −35/16 as a
  recast conditional on assumptions (a)–(f), labels (d) the load-bearing caveat, and the full in-in
  numerical evaluation is Cai's+Li's published work (reproduced at 3 benchmarks, App A.1). Tighten (d)
  wording ("derived to a bounded systematic" vs "weakest link") for internal consistency — applied.
- MAJOR 7–17 (recast of single σ; heterogeneous r; additive-quadrature budget; ρ proxy;
  Bayes-factor prior-dependence; competitor priors; gauge-frame; κ_ε schematic; SDB Fisher;
  MegaMapper speculative): **RE-FLAG of disclosed limitations** — every one is already caveated in the
  present text (scoping envelope, ρ-proxy lower bound, BF "illustrative not definitive", MegaMapper
  "speculative motivation"). These are the structural harsh-referee floor (directive-H); dispositioned
  non-real with source-cited verdicts, NOT closed by fabrication. MAJOR #2/#3 are the only genuinely-new
  editable ones and they are fixed.
- MINOR 19–23 (abstract too long, figure clarity, code-vs-derivation, refs, AI-methodology prominence):
  **OPINION / presentation** — noted; abstract-length + figure-separation are legit polish, dispositioned
  to the presentation-scope streamlining pass.

### INT-Grok API MINOR ×5
All 5 (App A private-verification, assumption-(d) scaling, r=0.84 vs r_eff, additive-quadrature
envelope, 38-page length) are **REAL-but-MINOR / already disclosed** — same items as EXT Grok, same
fixes. Verdict MINOR REVISIONS matches the honest state after this bundle's corrections.

---

## Counts
- **NEW-REAL-EDITABLE, closed this bundle:** 3 — (1) Eq.(spurious) sign −99/128 + honest A_T=−305/64
  restatement [Grok-EXT-M1 = Claude-M = OpenAI-M2/M3]; (2) envelope subordinated, central Fisher
  number as headline [Grok-EXT-M2 = OpenAI-M10]; (3) Table VII provenance re-attribution.
- **REAL-MINOR, tightened this bundle:** 3 — (d) gradient-coefficient OOM statement; r_eff caveat;
  duplicate-number consolidation.
- **RE-FLAG of disclosed scope, dispositioned non-real (source-cited):** ~15 (OpenAI M1,4-9,11-18;
  Grok/OpenAI overlaps) — structural harsh-referee floor, no fabrication used to dismiss.
- **OPEN / follow-up (non-blocking):** 3 — p2_vertex_check.py per-vertex print loop; deprecate
  `fig_4vertex_sum.py`; c13/c14 σ raw-output paste for third-party verification.

## Integrity
No fabrication. The one genuinely-new *editable* finding (the spurious-term sign/magnitude
misstatement) was caught by re-deriving from the committed scripts, confirmed by an independent second
sympy derivation, and **corrected toward what the artifacts actually show** — i.e. the fix made the
paper MORE conservative/honest (dropped a false "printed-polynomial → −35/8 via +99/128" mechanism
claim), never fabricated a derivation to make a finding disappear. Headline −35/16 unchanged and
quadruple-certified.

---

## Addendum — ChatGPT EXT (v1.7.108 → v1.7.109)

Raw: `EXT_real/H17_2026-07-10/P2_chatgpt.md` (REJECT, 11 MAJOR + 1 MINOR). ChatGPT's raw even
cites "h17_P2" — it reviewed a state at/near v1.7.107/108, so several findings are re-flags of
content the first-pass owner already rewrote. Every finding re-derived from the committed scripts
at the corrected −35/16 center, NOT from ChatGPT's framing. **The headline number stayed −35/16;
nothing fabricated.**

### GROUND TRUTH re-established this addendum (script re-run at −35/16)
The committed BF scripts `c9g_bf_table_recompute.py` and `c9k_gr_continuous_marginalization.py`
**still hard-coded `F0 = -35/8`** (the superseded center). Fixed both to `F0 = -35/16` and re-ran.
Exact closed-form `exp[(35/16)²/(2σ_eff²)]`:

| σ_GR | σ_eff | SSFSR at −35/16 (TRUE) | SSFSR at −35/8 (what paper printed) | Tuned narrow (−35/16) | P(BF>3) at −35/16 |
|---|---|---|---|---|---|
| 0 | 0.700 | **1.4×10²** | 3.5×10⁸ | 5.70 | **88.8%** |
| 0.5 | 0.860 | **27** | 4.5×10⁵ | 4.64 | **80.2%** |
| 1.0 | 1.221 | **5.1** | 6.4×10² | 3.30 | **61.5%** |

Continuous σ_GR~U[0,1] marginalization (c9k, re-run): BF vs SSFSR = **19** (was 8.6×10³ at −35/8);
BF vs Tuned = 4.6. Tuned column (5.7/4.6/3.3) **confirmed already correct** at −35/16.

### Per-finding verdicts

| ChatGPT finding | Verdict | Disposition |
|---|---|---|
| **MAJOR #8** — BF-vs-SSFSR (10⁸/10⁵/10²), P(BF>3), calibration are numerically the −35/8 values | **REAL / STALE — FIXED** | Confirmed: both recompute scripts hard-coded F0=−35/8 so the SSFSR + P(BF>3) columns never moved when the center was halved (only the Tuned column had been hand-updated). Fixed F0→−35/16 in `c9g` + `c9k`, re-ran, replaced tab:gr SSFSR `10⁸/10⁵/10²`→`1.4×10²/27/5`, P(BF>3) `99.9/99.0/93.1%`→`88.8/80.2/61.5%`, calibration `3.5×10⁸/3.1×10⁸`→`1.41×10²/1.38×10²`, continuous-marg SSFSR `8.6×10³`→`19`, tab:bayes SSFSR `>10²/>10⁵`→`~5–1.4×10²/~1.4×10²` (footnote c added). Captions state provenance. **No hand-compute-and-paste — every value from the re-run script.** ChatGPT's arithmetic (≈1.3×10² at −35/16) matches to 2 sig figs. |
| **MAJOR #1** — App A summation convention (six ordered triples vs three monomials); no convention makes A2/A4/−35/8 simultaneously true | **RE-FLAG (pre-v1.7.108) / already answered** | New App A line 1489 states the convention EXPLICITLY: Σ_{i≠j} = six ordered pairs, Σ_{i≠j≠l} = six all-distinct triples, Σ^dist_(5,2,2) = the three listed monomials. The paper does NOT claim A2/A4/−35/8 are simultaneously true — the v1.7.108 owner already restated the coded printed polynomial → −305/64 with the −(99/128) sign, and −35/8 as Cai's separately-published value. Dispositioned non-real; convention now unambiguous. |
| **MAJOR #2** — +c.c. time-ordering: Eqs.34–36 already include c.c., so commutator identity doesn't establish doubling | **RE-FLAG / already answered** | New App A lines 1518–1572 give the explicit in-in operator-algebra identity (−2Im doubling via Hermiticity, Eqs.A7–A12) and line 1572 states Eqs.34–36 are the single-time-ordered ∑_v∑_σ I_v BEFORE the −2Im doubling (ratio exactly 1/2). The +c.c. reading is directly addressed. Non-real. |
| **MAJOR #5** — Heinrich reproduction limitations + FoG "conservative" sign backwards | **PARTLY REAL (FoG sign) — FIXED; reproduction part RE-FLAG** | FoG: ChatGPT is right — omitting a *degrading* effect is OPTIMISTIC for absolute significance, not conservative. Line 1045 said "if anything conservative"; reworded honestly (FoG suppresses small-scale power → degrades info → including it weakens absolute σ; it largely cancels in the r_eff ratio, the only headline quantity). Reproduction-vs-Heinrich (σ=0.42–0.45 vs 0.73, bias-fixed, diagonal Gaussian cov): already disclosed as an explicit limitation list at line 1045 + labeled a validation not an independent forecast (line 847 Scope). Non-real re-flag. |
| **MAJOR #6** — ρ=−0.868 headlined; own |ρ|=0.95 proxy → 0.8σ | **RE-FLAG (already disclosed) — TIGHTENED per directive-F** | Prose (line 1210) ALREADY brackets σ_marg≈0.8–1.3σ and gives the |ρ|=0.95→0.8σ lower edge with a source-cited structural reason for adopting −0.868 (0.95 is a power-spectrum SDB-channel shape overlap, structurally distinct from the bispectrum covariance). But tab:systematics headlined only the 1.3σ row → added the explicit `|ρ|=0.95 → 0.8σ` lower-edge row (σ_marg=2.24) so the more-favorable value isn't headlined alone. ChatGPT's 0.8σ arithmetic verified (2.1875·0.84/2.242=0.82). |
| **MAJOR #4** — cross-Fisher α not computed in survey metric; r_eff=0.99 contradicts 0.84 | **RE-FLAG / disclosed** | Line 1045 explicitly reconciles r=0.84 (flat-weight cosine, deliberately conservative headline) vs r_eff≈0.99 (survey-optimal, used only as validation); the paper headlines the conservative 0.84. The exact cross-Fisher α marginalization is disclosed as not-in-repo (per-triangle Cov_B external). Non-real. |
| **MAJOR #3** — null-space scan unphysical (cubic action fixes all coefficients) | **RE-FLAG / OPINION-scope** | The scan is disclosed as a basis-measure stress band (r=0.85±0.13) that NEVER enters σ_eff (line 987: "no r>1 sample can…"); only noise-weighted r=0.84 propagates. Methodological-interpretation disagreement, not a numeric error. Non-real. |
| **MAJOR #7** — cubic bounce transmission not derived (δfNL≲10⁻³ unsupported) | **RE-FLAG (= Grok MINOR-a, prior audit)** | Same as first-pass Grok MINOR-a: OOM single-clock scaling estimate, load-bearing caveat (d) already flagged the weakest link; disclosed as not-a-full-3rd-order-in-in. Non-real. |
| **MAJOR #9** — c_s consistency (−35/16 is c_s=1 limit; low-c_s discussion invokes 65/8c_s²) | **RE-FLAG / disclosed limitation** | Assumption (a) fixes the c_s=1 quasi-dust benchmark explicitly (line 954); the low-c_s viability remark is a separate qualitative note. Disclosed scope, no numeric conflict in the headline. Non-real. |
| **MAJOR #10** — κ_ε=2.8–40 consistency relation not fully derived | **RE-FLAG / disclosed** | Already labeled a single-prefactor-derivative estimate with the four-vertex cancellations acknowledged; the fNL–n_s relation is disclosed as indicative. Non-real. |
| **MAJOR #11** — "measures gauge-frame fNL directly" incorrect | **RE-FLAG / OPINION-scope** | Framing dispute over the comoving-gauge consistency-term interpretation; the observable factor-146 claim is a template-amplitude comparison, disclosed as such. Non-real (no numeric error). |
| **MINOR** — MegaMapper in abstract, 3-page abstract, EC/birefringence excursions, code filenames, placeholder Zenodo DOI | **OPINION / presentation** | Legit polish; MegaMapper already labeled speculative; abstract-length + filename-density noted for the presentation streamlining pass. Non-blocking. |

### Addendum counts
- **REAL / STALE-number, FIXED this addendum:** 1 finding, ~9 numeric sites — MAJOR #8 SSFSR-column family (tab:gr SSFSR ×4, P(BF>3) ×3, calibration ×2, tab:bayes SSFSR ×2, continuous-marg ×1) + 2 recompute scripts re-centered.
- **REAL logic-error, FIXED:** 1 — MAJOR #5 FoG "conservative"→"optimistic" sign.
- **DISCLOSED-but-under-tabulated, TIGHTENED (directive-F):** 1 — MAJOR #6 |ρ|=0.95→0.8σ lower-edge row added.
- **RE-FLAG of already-addressed / disclosed scope, non-real (source-cited):** 8 — MAJOR #1,2,3,4,7,9,10,11.
- **OPINION / presentation:** 1 MINOR.

### Addendum integrity
No fabrication. The stale SSFSR column was fixed by re-centering the COMMITTED scripts (not by
pasting a hand-computed number) and re-running; the Tuned column was verified already-correct rather
than blindly re-touched. The FoG fix and the |ρ|=0.95 row both made the paper MORE conservative
(smaller SSFSR magnitudes, an explicitly-displayed weaker 0.8σ floor). Headline −35/16 unchanged.

### Directive-G hygiene (v1.7.109)
- `\date` = July 10, 2026; version comment bumped v1.7.108 → v1.7.109.
- TinyTeX 2-pass: 0 errors, 0 undefined refs, 0 overfull hboxes, 38 pages.
- PDF md5 = `bd620e64afda60c3bd2a1b14429aaa28`, 1382034 bytes.
- Mirrored byte-identical to all 13 served paths (public + site/public, aliases + v1.7.109 versioned) — all md5-verified.
- Convex `paperVersions:bump` paper-2 v1.7.109 (real md5/pages/bytes, "July 10, 2026") → row `k570xd7m3ege0e68twv03pqcw18a9r3s`.
- Leak-gate: 0 secret patterns pre-compile.
- No commit (per instructions).

---

## Addendum 2 — INT re-test v1.7.109 (→ v1.7.110)

Fresh INT re-test on v1.7.109: **OpenAI REJECT**, **Grok-API MAJOR**, **Claude MINOR**. Raws:
`INT_v3/ROUND_2026-07-09/API_P2_openai.md` (REJECT, 11 MAJOR + 4 MINOR),
`API_P2_grok.md` (MAJOR REVISIONS, 3 MAJOR + 2 MINOR),
`INT_api/H17_2026-07-10/retest_P2_claude.md` (MINOR REVISIONS, 4 MINOR).
Every finding re-derived from the committed scripts/JSON at the −35/16 center; NOT from the raws' framing.

### CRITICAL provenance fact — OpenAI + Grok raws are on a STALE v1.7.102 PDF
Both API raws carry the header `version: v1.7.102` and were run 2026-07-10T07:50Z. The v1.7.102 PDF
predates the App-A explicit-vertex-algebra add (v1.7.104), the RSD-Fisher closure (v1.7.103), the
spurious-sign + honest −305/64 restatement (v1.7.108), and the SSFSR re-center (v1.7.109). This is
the "header version label may be stale" case the round prompt flagged — but here the *content* they
critique (no explicit four-vertex algebra; spurious term "unverifiable"; r=0.84 "ad-hoc"; envelope
"presented as a forecast"; transmission (d) "only a scaling estimate") is verbatim the pre-v1.7.104
state. **Verified in v1.7.109**: `tab:vertexwalk` (per-vertex squeezed+equilateral), `Eq:order_grouped`,
`Eq:collapsed_vertexsum`, the in-in operator algebra (App A A7–A12), and the −(99/128) spurious-sign
correction are all present. Every OpenAI/Grok finding is therefore a **re-flag of already-closed
content** (source-cited non-real), OR a re-flag of an honestly-disclosed limitation. No fabrication
used to dismiss.

### Per-finding verdicts — OpenAI (v1.7.102, REJECT)
| Finding | Verdict | Disposition |
|---|---|---|
| M1 App A "not publishable-level, relies on code not self-contained algebra" | **STALE RE-FLAG** | Closed v1.7.104/v1.7.90: `tab:vertexwalk` + `Eq:order_grouped` + App A A7–A12 give the explicit four-vertex algebra + in-in operator identity in the main appendix. Non-real. |
| M2 Sec II vs App A "null-space vs certified vertex sum" inconsistent | **RE-FLAG / disclosed** | The 10⁴-sample null-space scan is an amplitude-invariant *shape-basis stress band* (r=0.85±0.13) that never enters σ_eff (only noise-weighted r=0.84 does); the vertex sum fixes the amplitude. Disclosed at L987/L869. Non-real. |
| M3 spurious local term changes shape not amplitude; r=0.84 not from corrected shape | **RE-FLAG** | r is a shape ratio computed from Cai's printed monomial shape (amplitude-invariant); −35/16 fixes normalization only. Disclosed L925. Non-real. |
| M4 σ=σ_local/r scalar rescale not justified for galaxy bispectrum | **RE-FLAG / disclosed scope** | This IS the paper's stated Scope: a sensitivity recast of one external Heinrich forecast, validated by the independent in-house tree-level Fisher (r_eff≈0.99). Disclosed L869. Non-real. |
| M5 r_eff≈0.99 "undermines" r=0.84; estimator inconsistency | **RE-FLAG** | Reconciled once at §spherex: r=0.84 = flat-weight shape cosine (conservative headline), r_eff≈0.99 = survey-optimal amplitude recovery (validation only). Different quantities. Non-real. |
| M6 cubic transmission not "closed" to δfNL≲10⁻³ | **RE-FLAG = load-bearing caveat (d)** | Already the explicitly-flagged weakest link; OOM single-clock estimate, disclosed as not-a-full-3rd-order-in-in. Non-real (honest open item, already disclosed). |
| M7 UV-completion independence overstated | **RE-FLAG / disclosed** | Assumptions (a)–(f) enumerate exactly these dependencies. Non-real. |
| M8 1.3–2.75σ heterogeneous quadrature not a marginalized forecast | **RE-FLAG** | Labeled a scoping sensitivity envelope, NOT a joint-covariance precision (L869/873). Envelope subordinated in v1.7.108. Non-real. |
| M9 ρ=−0.868 / |ρ|=0.95 GR-proxy unjustified | **RE-FLAG** | ρ-proxy disclosed as a lower-bound structural proxy; |ρ|=0.95→0.8σ lower-edge row added v1.7.109 (directive-F). Non-real. |
| M10 Bayes factors prior-dominated illustrative | **RE-FLAG** | Labeled "illustrative not definitive"; SSFSR column order-of-magnitude only. Non-real. |
| M11 MegaMapper speculative | **RE-FLAG** | Labeled "illustrative envelope … design uncertainty." Non-real. |
| MINOR 12–15 (abstract length, notation, figures, lit-status) | **OPINION / presentation** | Noted for streamlining pass. Non-blocking. |

### Per-finding verdicts — Grok-API (v1.7.102, MAJOR REVISIONS)
| Finding | Verdict | Disposition |
|---|---|---|
| M1 "neither explicit four-vertex algebra nor full in-in in main text/appendices" | **STALE RE-FLAG** | Factually false for v1.7.109 (`tab:vertexwalk` + A7–A12 present). Closed v1.7.104. Non-real. |
| M2 forecast conditional on cubic transmission "verified only at linear order" | **RE-FLAG = caveat (d)** | Identical to OpenAI M6; disclosed load-bearing caveat. Non-real. |
| M3 1.3–2.75σ = scoping envelope not jointly marginalized | **RE-FLAG = OpenAI M8** | Disclosed envelope, subordinated v1.7.108. Non-real. |
| MINOR (committed-artifact-only evidence; 38-page length) | **OPINION / presentation** | Intermediate results now tabulated (`tab:vertexwalk`); length noted. Non-blocking. |

### Per-finding verdicts — Claude (v1.7.109, MINOR REVISIONS) — ALL 4 CLOSED
| Finding | Verdict | Closure (v1.7.110) |
|---|---|---|
| MINOR 1 abstract sign-gloss (L867) "printed polynomial exceeds vertex sum by [−(99/128), a negative]" | **REAL / EDITABLE — CLOSED** | Verbal self-contradiction ("exceeds by a negative amount"). Reworded: "the vertex sum exceeds the transcribed printed polynomial by +(99/128)Σk³, so the printed polynomial is the more negative of the two." Consistent with `Eq:spurious` (Σ−A_T=+99/128) + `cai_vertices.py`. |
| MINOR 2 continuous-marg BF (L1258) "≈4.8 vs tuned narrow" ≠ committed 4.615 | **REAL / EDITABLE — CLOSED** | The 4.8 was the r=0.84-rebooked delta/narrow value (a *different* quantity, correctly derived at L1274); the L1258 sentence mislabeled it as the continuous-marg BF. Reconciled to "≈4.6 (c9k …BF_vs_tuned_narrow=4.615)". Committed JSON verified: `continuous_marginal.BF_vs_tuned_narrow=4.615`, SSFSR=19.4 (matches paper's 19). |
| MINOR 3 stale artifact metadata (c9k conventions="−35/8"; c9g legacy `table_iii_claims`) | **REAL / EDITABLE — CLOSED** | c9k `conventions` string refreshed "−35/8"→"−35/16" (every value in the file already at −35/16, e.g. SSFSR 1.412e2 not 3.5e8). c9g superseded `table_iii_claims` (3.3e6/10.9/0.98) renamed `_SUPERSEDED_table_iii_claims` + note; only `scans` block authoritative (matches tab:gr). |
| MINOR 4 tab:gr caption (L1274) −35/8 SSFSR refs 3.5e8/4.5e5/6.4e2 ~15% off | **REAL / EDITABLE — CLOSED** | True closed-form exp[(35/8)²/(2σ_eff²)] = 3.0e8/4.2e5/6.1e2 (verified sympy/math: 3.04e8, 4.17e5, 614). Replaced; labeled "from the same closed-form." These are discarded reference values, so cosmetic, but now exact. |

### Addendum-2 counts
- **Genuinely-new REAL editable:** 4 — all Claude MINORs (all CLOSED this bundle → path to 0/0/0 on Claude).
- **STALE RE-FLAG of already-closed content (source-cited non-real):** 2 — OpenAI M1, Grok M1 (explicit-vertex-algebra "missing" — factually present since v1.7.104).
- **RE-FLAG of disclosed limitation/scope (source-cited non-real):** 12 — OpenAI M2–M11, Grok M2–M3.
- **OPINION / presentation:** 6 — OpenAI MINOR 12–15, Grok 2 minors.
- **Disclosure-backfire (pattern-066):** 0 new this addendum. (Prior audit already documented the −305/64/smaller-BF backfire pattern; no new instance — the OpenAI/Grok raws punish *stale* content, not the new honest restatements, because they never saw v1.7.108/109.)

### Addendum-2 integrity
No fabrication. The 4 Claude MINORs were closed by reconciling the paper to what the COMMITTED
artifacts already show (c9k 4.615, closed-form −35/8 refs, honest sign direction) — every fix made
the paper MORE internally consistent, never invented a value. The OpenAI REJECT + Grok MAJOR were
correctly diagnosed as a stale-PDF (v1.7.102) artifact: their "missing algebra / ad-hoc rescale /
envelope-as-forecast" complaints were all closed in v1.7.103–v1.7.109 and are re-flagged with
source-cited sections, NOT dismissed by fabrication. Headline −35/16 unchanged, quadruple-certified.

### Directive-G hygiene (v1.7.110)
- `\date` = July 10, 2026; version comment header bumped v1.7.109 → v1.7.110 (full changelog inline).
- Leak-gate: 0 secret patterns pre-compile.
- TinyTeX 2-pass: 0 errors, 0 undefined refs, 0 overfull hboxes, 38 pages.
- PDF md5 = `e77532ab46a4657bb2711222c2a9cd26`, 1382382 bytes, 38 pages.
- Page 1 verified: shows "July 10, 2026" + headline −35/16 = −2.1875.
- Mirrored byte-identical to all 13 served paths (public + site/public, aliases + v1.7.110 versioned) — all md5-verified.
- Convex `paperVersions:bump` paper-2 v1.7.110 (real md5/pages/bytes, "July 10, 2026", texCommit "pending-H17-bundle") → row `k57d9q2xd9j7056t0nq6mmh0zh8a8qvp`.
- No commit (per instructions).
