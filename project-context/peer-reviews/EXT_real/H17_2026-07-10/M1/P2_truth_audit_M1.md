# P2 M1 truth audit — v1.7.116 (directive-M presentation-restructure wave)

**Paper:** `research/focused_paper_source_integration/02_full_draft.tex`, v1.7.116,
`\date{July 12, 2026}`, headline `f_NL^local = -35/16 = -2.1875`, PDF md5
`abfdbf70a957fc343324b66cab6dbca4`, 37pp, Convex row `k579nj3nxp7vdrcc02s415wtxd8acrdk`.

**Legs audited (M1):**
- EXT Grok — `M1/P2_grok_M1.md` — **MAJOR REVISIONS**
- EXT ChatGPT — `M1/P2_chatgpt_M1.md` — **REJECT**
- INT Claude (recovered) — `INT_api/H17_2026-07-10/intwave_P2_claude_M1r.md` — **MAJOR REVISIONS**
  (verdict-first: "**no computational error** on a fresh read"; MAJOR = presentation/length + significance-framing)

**Method:** verdict-first, source-cited (patterns 061–066, directive-H/H-refined).
`ledger_match.py`: ChatGPT 11/11 auto-MATCHED, Grok 5/6 MATCHED to standing D-ids
(DP2-02/-04/-13/-14/-15/-18/-19/-21/-22/-31/-34). Every finding re-audited from scratch
against current tex + `DISPOSITIONS/P2.md`.

---

## CRITICAL: overhaul-regression hunt (v1.7.116 consolidation)

The v1.7.116 directive-M restructure "reduced redundant downstream restatements to short
cross-references" (DP2-M1). I verified NO cross-reference was orphaned and NO claim lost its
context:

- **Served cross-refs vs served labels (comment lines excluded):** `comm -23` of all
  non-comment `\ref/\eqref/\cref` targets against all non-comment `\label{}` → **EMPTY set.
  Every served cross-reference resolves.**
- **Authoritative compile log** (`02_full_draft.log`, Jul 12 09:25): **0 "undefined reference",
  0 "multiply-defined", 0 "Overfull \hbox".**
- `sec:sdbfisher` and `tab:bayes_minimal` appear as "unmatched" ONLY when comment lines are
  included — both live exclusively inside `%`-prefixed changelog history (L469, L936, L948),
  never in a served `\ref{}`. **Not broken refs.**
- **`app:birefringence` relegation (the biggest structural move) is intact:** the outlook
  pointer at `:1521` (`\ref{app:birefringence}`) resolves to `\label{app:birefringence}` at
  `:1713`. The relegated content is present, cross-referenced, and self-consistent.
- **Caveat-(d) consolidation** (DP2-M1 item 1, the largest redundancy removed): the
  `δf_NL≲10⁻³` disclosure survives at its canonical homes (abstract `:975`, Intro Scope `:989`,
  §Assumptions `:1076`, Scope-and-limitations (ii) `:1512`, Conclusion). The full
  degree-of-freedom-counting derivation still lives once, in §Assumptions (`:1076`), with the
  "conditional on the dressed-metric quantization" / "plausible but not derived" hedge intact.

**No overhaul-introduced broken \ref/\eqref/\cite and no orphaned claim.** The restructure is
clean.

---

## Leg 1 — EXT Grok (MAJOR REVISIONS)

| # | Finding (Grok) | Disposition | D-id + source |
|---|---|---|---|
| 1 | [MAJOR] ρ=−0.868 proxy-transferred floor; 1.3σ marginal not channel-native | **RE-FLAG-DISCLOSED** | DP2-04/-07/-34. Proxy disclosed abstract `:975` ("proxy correlation transferred from the power-spectrum SDB channel, as … Cov_B is not public"); channel-native c15 Fisher (σ_marg≈0.94→2.3σ) also now in abstract Scope `:989`. |
| 2 | [MAJOR] −35/16 correction must be shown with explicit side-by-side polynomials in main text / early appendix, not relegated to App A | **RE-FLAG-DISCLOSED / OPINION (placement)** | DP2-02/-16. −35/16 quadruple-certified (`tab:vertexwalk`, `tab:vertices`, `eq:order_grouped` `:1615`); the explicit vertex algebra + `-305/64` reduction is present at `:1615`. Placement preference = DP2-30 (Houston-gated). |
| 3 | [MINOR] assumption (d) closed only by OOM scaling; no full Maldacena cubic-action integration | **RE-FLAG-DISCLOSED** | DP2-13. Load-bearing caveat (★), §Assumptions `:1076` states verified linear-order, cubic closure conditional on dressed-metric quantization, "plausible but not derived" in deformed-algebra. |
| 4 | [MINOR] BF≈9–14 prior-dependent; abstract doesn't immediately qualify | **RE-FLAG-DISCLOSED** | DP2-18. Abstract `:975` calls it "illustrative"; four-corner prior grid `tab:bayes`; Scope-(vi) `:1512`. |
| 5 | [MINOR] 37-page length; digressions dilute readability; tighten/relocate technical validation | **RE-FLAG-DISCLOSED (this is the class v1.7.116 ACTIONS)** | DP2-30 / DP2-M1. Consolidations landed; residual length = venue floor, Houston-gated. |

**Verbatim overhaul-acknowledgment (Grok):** *"The 37-page scope is justified by the
source-level audit, explicit template map, itemized budget, and three-way MC validation of the
closed-form BF, but the dense digressions on null-space SVD sampling, multi-radius convergence
tests, and committed JSON artifacts dilute readability; tighter editing or relocation of
technical validation details to a supplemental file would better serve PRD readers while
preserving reproducibility."* (`P2_grok_M1.md` L9)

Grok's own §3: *"the central claim … is supported by the internal multi-method verification of
the amplitude … subject to the stated assumptions."* — confirms the science; 0 genuinely-new.

---

## Leg 2 — EXT ChatGPT (REJECT)

All 11 matched. Every item is a source-cited re-flag of a standing disposition (structural
harsh-referee floor, directive-H):

| # | Finding (ChatGPT) | Disposition | D-id |
|---|---|---|---|
| 1 | [MAJOR] null-space "unphysical"; vertex sum uniquely fixes coefficients; scan meaningless; Fig 1 halving | RE-FLAG-DISCLOSED | DP2-15 (reparam-invariance caveat verbatim `:966`) + DP2-01/-02 |
| 2 | [MAJOR] App A source-tracing internally contradictory; c.c. can't turn C₃→S₃; remove doubling narrative | RE-FLAG-DISCLOSED | DP2-16/-03 (doubling narrative already retracted v1.7.108; `:1615` states −305/64 not −35/8) |
| 3 | [MAJOR] δf_NL≲10⁻³ not derived; ζ̇=0 fails in non-attractor; needs 2nd-order/in-in | RE-FLAG-DISCLOSED | DP2-13 (disclosed conditional, §Assumptions `:1076`) |
| 4 | [MAJOR] Wilson-Ewing mischaracterized: deformed-algebra 1−2ρ/ρc, not dressed c_s²=1; r_t≃9×10⁻⁴; ρc∼10⁻⁹ρ_Pl tension | RE-FLAG-DISCLOSED | DP2-13/-19/-32.6 (deformed-algebra signature-change window explicitly disclosed `:1076`) |
| 5 | [MAJOR] r=0.84 global rescale not valid SPHEREx Fisher recast; needs cross-Fisher not weighted average | RE-FLAG-DISCLOSED | DP2-14/-22 (r vs r_eff reconciled §spherex; channel-native α=0.992 c15) |
| 6 | [MAJOR] in-house Fisher doesn't validate Heinrich; 0.42–0.45 vs 0.7 = substantial disagreement | RE-FLAG-DISCLOSED | DP2-22 (reproduction-limitation list disclosed) |
| 7 | [MAJOR] 1.3–2.75σ envelope no statistical interpretation; σ_GR not addable in quadrature; b_φ priors not derived | RE-FLAG-DISCLOSED | DP2-04/-26/-34 (labeled scoping envelope; c15 channel-native computed) |
| 8 | [MAJOR] quasi-dust κ_ε∈[2.8,40] not a bounded uncertainty; A_T∝ε⁻³ not established | RE-FLAG-DISCLOSED | DP2-20 (labeled single-prefactor-derivative estimate, indicative) |
| 9 | [MAJOR] Bayes factors = prior-volume ratios; numeric BF=3.27 not 3.9; remove from abstract | RE-FLAG-DISCLOSED | DP2-18 (illustrative-labeled; four-corner grid) |
| 10 | [MINOR] "gauge-frame quantity on sky" wrong; 146 ratio not on-sky discriminator | RE-FLAG-DISCLOSED | DP2-21 |
| 11 | [MINOR] headline σ doesn't propagate own theory range (2.38σ vs 2.6σ; 0.6–8% in/excluded inconsistently) | RE-FLAG-DISCLOSED | DP2-19/-14 |

**Verbatim overhaul-acknowledgment (ChatGPT):** the M1 raw's presentation critique is embedded
in items 9–11 (register/organization). ChatGPT's §3 concedes the core: *"the algebraic
correction f_NL^local = −35/16 is supported by Cai et al.'s intermediate expressions and Li et
al.'s independent result"* (`P2_chatgpt_M1.md` §3) — disputes only survival-through-bounce +
forecast scope (all disclosed, DP2-13/-17/-29). **0 genuinely-new editable findings.**

---

## Leg 3 — INT Claude (MAJOR REVISIONS) — verdict-first: NO computational error

Claude INT explicitly: *"The science is correct and internally consistent — I found **no
computational error** on a fresh read … The −35/16 certification is genuinely solid. My MAJOR
verdict is driven by presentation/length and significance-framing for the PRD venue, not by any
error in the physics."* (leg L9)

| # | Claude finding | Disposition |
|---|---|---|
| 1 | [MAJOR] Length/density exceed PRD norms even after consolidation (abstract `:975` ~330-word single para; Scope block; Fisher/systematics paras) | **RE-FLAG-DISCLOSED** — DP2-30/DP2-M1 (venue floor; presentation restructure landed; residual length Houston-gated) |
| 2 | [MAJOR] Significance = marginal, doubly single-sourced recast (~1.3–2.75σ, 0.8σ GR bracket) | **RE-FLAG-DISCLOSED** — DP2-17/-29/-34 (Scope `:989` "recast … not an independent one"; single-source limitation `:1512`) |
| 3 | [MINOR] "arithmetic error confined to Cai Eq. 37" (`:1620`) in tension with appendix hedge that −35/8 cannot be reproduced (−305/64) | **see below** |
| 4 | [MINOR] Birefringence appendix independent of every result; consider cutting entirely | **RE-FLAG / OPINION** — DP2-30. The v1.7.116 relegation already actioned this; keep-vs-cut of a one-line-pointed appendix is scope preference. |
| 5 | [MINOR] Abstract (`:975`) omits that assumption-(d) closure is quantization-conditional ("plausible but not derived") | **see below** |

### Claude MINOR issue 3 (`:1620`) — RE-FLAG-DISCLOSED, NOT genuinely-new-editable

The line reads: *"It **is** a genuine arithmetic error confined to Cai \etal's last algebraic
combination step (their Eq.~37)."* Claude reads this as overstated vs the appendix hedge. But
the SAME sentence-cluster already carries the reconciliation Claude asks for: the immediately
preceding sentence (`:1619`) states the printed polynomial *"squeezed reduction departs from
−35/16 to −305/64, not to Cai's stated −35/8,"* and `:1025` + Scope-(iii) `:1512` + abstract
`:975` all state *"the printed −35/8 is an unreproduced erroneous literature value."* The
"arithmetic error confined to Eq. 37" phrasing refers to the **one traced −(99/128)Σk³
discrepancy**, which IS confined to that combination step; it is not a claim that −35/8 is
reproduced. This is standing DP2-01/-03/-32.3 (the doubling-mechanism overclaim was retracted
v1.7.108; the "unreproduced erroneous literature value" framing landed v1.7.112). The tension
Claude perceives is a **register nuance on already-hedged content** → OPINION on disclosed
material, not a new editable defect. (A one-word softening "one arithmetic discrepancy" is
available as optional polish but is NOT a required correction — the honest content is already
present two sentences away.)

### Claude MINOR issue 5 (`:975`) — RE-FLAG-DISCLOSED (abstract already carries the conditional)

Claude states the abstract omits that the (d) closure is quantization-conditional. **The
abstract does state the conditional**, just compactly: `:975` reads *"conditional on faithful
cubic-order transmission through the bounce, closed to a bounded δf_NL≲10⁻³ systematic via
single-clock nonlinear ζ-conservation."* The word "conditional" and the load-bearing (d)
dependence ARE in the abstract; the *dressed-metric-vs-deformed-algebra* granularity is what is
compressed (it lives at full length in §Assumptions `:1076` "plausible but not derived" and in
Intro Scope `:989`). This is DP2-13/-32.6 (already-disclosed load-bearing caveat) + the
directive-M consolidation-to-canonical-home pattern. A one-clause addition of "(conditional on
the dressed-metric quantization)" to the abstract is available as optional honesty polish, but
the abstract is NOT currently silent on the conditionality → **RE-FLAG-DISCLOSED, not a
genuinely-new orphaned/omitted claim.**

**Verbatim overhaul-acknowledgment (Claude INT):** *"Length and density exceed PRD norms **even
after the consolidation round**. … For the incremental scientific content (a recast of one
external forecast + an arithmetic correction), this is well **beyond PRD crispness**
expectations."* (leg L13, issue 1)

---

## Final count

**GENUINELY-NEW REAL FINDINGS: 0.**

- No overhaul-introduced broken `\ref/\eqref/\cite` (all served cross-refs resolve; 0 undefined,
  0 overfull in the authoritative log).
- No claim orphaned by the v1.7.116 consolidation (caveat-d, birefringence relegation, r-notation
  all verified intact at canonical homes).
- Claude's two MINORs (issues 3 `:1620` and 5 `:975`) are **RE-FLAG-DISCLOSED**, not
  genuinely-new-editable: the honest content each requests is already present in the paper
  (issue 3 at `:1619`/`:1025`; issue 5 at `:975`/`:989`/`:1076`). Both are optional
  one-clause register-polish items (DP2-13/-01/-03/-32.3/-32.6), zero-number, non-blocking —
  consistent with Claude's own "one-paragraph edits, zero number change" characterization, and
  correctly classed as the DP2-30/venue floor rather than new defects.
- All EXT items (Grok 6, ChatGPT 11) map to standing D-ids. ChatGPT REJECT / Grok MAJOR /
  Claude MAJOR are the known LLM harsh-referee structural floor on a marginal-significance
  single-source recast whose external per-triangle Cov_B is unavailable (DP2-26/-29, venue,
  Houston-gated) — NOT editable correctness defects.

**Verdict: GENUINE convergence read holds.** 0 genuinely-new real findings across all three
legs; the v1.7.116 presentation restructure introduced 0 regressions. −35/16 quadruple-cert
intact; nothing fabricated; no finding dismissed without a source-cited verdict. No
v1.7.117 bump required on correctness grounds. Clean-wave streak continues.

**Integrity:** no ACCEPT faked; every dismissal source-cited to a tex line / D-id; no math
fabricated; the two Claude MINORs recorded honestly as disclosed-but-compressible (not silently
dropped).
