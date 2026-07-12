# P1U NJ6 truth-audit — v1U.0.17 — STRICT ledger-first — STREAK 1→2

**Wave:** NJ6 (2026-07-12) — SECOND consecutive re-test of the v1U.0.17 AA-channel
bound fix (DP1U-NJ4-01). **NO content changes since the 0-new NJ5 adjudication.**
(The working-tree v1U.0.18 delta is a purely editorial "far→comfortably sub-critical"
internal-consistency fix at the App. njl_gap leg-(B) intro — no numeric or physics
change — closing the residual NJ5 INT-Claude wording MINOR; it does not alter any
reviewer-facing claim.)
**Adjudicator stance:** skeptical, verdict-first, NOT told a convergence conclusion.
**Method:** `tools/ledger_match.py` pre-triage → full §3 manual truth-audit of every
finding vs `arxiv/paper1_unified.tex` v1U.0.17 + `project-context/peer-reviews/DISPOSITIONS/P1U.md`.

## Verdict matrix (raws read verbatim before any disposition)
| Leg | Reviewer | Verdict | Raw / source |
|-----|----------|---------|--------------|
| INT | OpenAI (gpt-5.5) | REJECT | run.log 10:49Z |
| INT | Grok (grok-4.3) | REJECT | run.log 10:49Z |
| INT | Gemini (gemini-3.1-pro) | **MINOR** (softened from MAJOR) | run.log 10:49Z |
| INT | Claude (opus-4-8, subscription subagent) | MINOR | intwave_P1U_claude_0346.md |
| EXT | Grok | MAJOR (4 MAJOR + 2 MINOR) | NJ6/P1U_grok_NJ6.md l.1 `VERDICT: MAJOR REVISIONS` |
| EXT | ChatGPT | REJECT (14 MAJOR + 2 MINOR) | NJ6/P1U_chatgpt_NJ6.md l.1 `VERDICT: REJECT` |

Gemini's INT verdict softened MAJOR→**MINOR** on the hardened NJL version — a
2nd-consecutive relaxation on unchanged content = presentational referee variance
(pattern-066), NOT new content. It surfaces zero new class of finding.

## AA-bound fix — HOLDS on 2nd independent re-test
No edit to the load-bearing NJL leg since NJ5. INT-Claude (0346) re-confirmed the
leg-(A) convention-independent scalar sign exclusion + leg-(B) magnitude bound
(worst-case AA `2×0.156=0.31`, sub-critical) against the committed
`njl_gap_equation_route1_results.json`. The DP1U-NJ4-01 PP-only overstatement fix
holds a second time.

## Genuinely-new vs re-flag — 0 genuinely-new reader-visible editable findings

### EXT-Grok NJ6 (4 MAJOR + 2 MINOR) → all source-cited re-flags
- [MAJOR] "channel-level assessment of four enumerated routes … not proven a complete
  diffeo basis" yet framed as decisive no-go/closure; qualification must be as prominent
  as the positive claim → **DP1U-06/-20/-21** (paper's own "channel-level, not an
  operator-level theorem" L1219/L1389-1390; DP1U-21 disclosure-backfire — honest hedge
  recast as weakness). RE-FLAG-DISCLOSED / OPINION.
- [MAJOR] R4 closed by naturalness/explanatory-deficit vs amplitude-suppression of R1–R3;
  wants a separate tiered classification → **DP1U-11** (R4 naturalness-vs-exclusion, CC
  relocation — the paper already labels R4 a naturalness argument, not an amplitude no-go).
- [MAJOR] §X perturbation-transparency restricted to canonical scalar matter, excludes
  fermion spin / propagating torsion / dynamical Immirzi / non-minimal / boundary sectors;
  domain must be delimited → **DP1U-12** (transparency = standard EC torsion-free-limit
  corollary; the exclusions are the paper's own stated scope). RE-FLAG-DISCLOSED.
- [MAJOR] R1 NJL Fierz projection / cutoff Λ=M_Pl / mean-field truncation robustness at
  Planckian densities not demonstrated; non-perturbative effects "could reopen" the channel
  → **DP1U-05/-19/-26/-NJ4-01** (regulated-NJL vacuum-condensate exclusion; leg-(A) sign is
  convention/coupling-independent, mean-field scope disclosed). RE-FLAG.
- [MINOR] 13/14 barriers one-line titles, not self-contained → **DP1U-13** (barrier-catalog
  independence; sec:barriers head discloses non-independence + pointers).
- [MINOR] N_tot≈92 two dimensional completions + 63pp length → **DP1U-08/-14** (dimensional
  promotion / N_tot bookkeeping) + **DP1U-22** (length OPINION).
- `ledger_match.py`: 5/8 auto-MATCHED (line-1 verdict header non-finding + 2 prose-diluted
  minors Opus-adjudicated to DP1U-13 / DP1U-08). Grok's own closing sentence: the central
  claim "is supported … subject to the scope limitations and assumptions the paper itself
  enumerates."

### EXT-ChatGPT NJ6 (14 MAJOR + 2 MINOR) → all source-cited re-flags (harsh-referee floor, directive-H)
Structurally identical to every prior ChatGPT REJECT (H17G/W1/W2b/NJ3b/NJ4/NJ5):
Eq(1)-(4) variational hybrid=**DP1U-03**; Eq(6) dim+1 "identity can't change dimension" +
M_Pl-power promotion=**DP1U-08**; App-B1 basis O1=O6 / Nieh–Yan / O4 undefined T_IJ / O5
matter-torsion / CC operator omitted=**DP1U-07/-20**; R1 Fierz f_IJ vs true Fierz matrix /
anticommuting signs / G_scalar=−3κ/64=**DP1U-05/-19/-26/-NJ4-01**; "single-scale NDA no-go =
naturalness not theorem"=**DP1U-08/-18**; R2 (∂ϑ)J5 dim / ∂ϑ~H0 mismatch / 10⁻⁶⁰ not
derived=**DP1U-09**; R3 Δγ→ρ_Λ no map / Benedetti–Speziale=**DP1U-10**; R4 α/M not rigid /
δ_NY uncomputed / floats fit both β_obs+ρ_Λ=**DP1U-11**; N_tot≃92 a⁻³-vs-a⁻⁶ inconsistent
dilution / no torsion memory=**DP1U-14**; matter-bounce −35/16-vs-Cai−35/8 + "definitively
erase" no transfer matrix=**DP1U-14/-17**; §X standard/overclaimed/not novel=**DP1U-12**;
13-constraints slogans not derivations / GW ceiling ansatz=**DP1U-13**; App F–H don't test
theory (stock-CAMB / synthetic-sky / one-number birefringence likelihood)=**DP1U-15/-24**;
MINOR κ conventions=**DP1U-02**; MINOR organization/length/two-page abstract=**DP1U-22**.
`ledger_match.py`: 5/16 auto-MATCHED (11 UNMATCHED all prose-diluted / verbose-restated
re-flags, Opus-adjudicated to the above D-ids). ChatGPT again ENGAGED the NJL appendix only
via leg-(B)/Fierz-exchange; did NOT rebut the leg-(A) convention-independent sign exclusion
(same partial-engagement as NJ2/NJ3b/NJ4/NJ5). **0 genuinely-new.**

### INT OpenAI REJECT / Grok REJECT / Gemini MINOR / Claude MINOR → same disclosed classes
single-scale NDA no-go→DP1U-08; channel-vs-operator→DP1U-06/-20; routes→DP1U-05/-09/-10/-11;
§X→DP1U-12; style/length→DP1U-22/-24. INT-Grok MAJOR→REJECT and INT-Gemini MAJOR→**MINOR** on
unchanged v1U.0.17 = opposite-direction presentational referee variance in the SAME wave
(pattern-066) — dispositive proof the verdict-word motion is noise, not content. **0 genuinely-new.**

## Streak / cap / bump
- **Streak:** prior 1 (NJ5 clean re-test 0→1). NJ6 = 2nd consecutive 0-new on the same
  v1U.0.17 → **1 → 2** (directive-K). This restores the full **five-paper directive-K set**
  to streak-2 with all science closures aboard — **milestone FIRES.**
- **Cap:** 50 + grok(EXT major 6) + chatgpt(EXT reject 0) + gemini(EXT major 6, latest EXT
  Gemini row carry-forward) = **62 HOLDS**. (INT-Gemini MINOR softening does not enter the
  EXT-reviewer cap formula.)
- **Version:** no content bump required — v1U.0.17 stands as the reviewed version. The
  editorial v1U.0.18 wording fix is non-reviewer-facing; `directive_g.sh` NOT re-run for NJ6.

## Integrity
Both EXT raws read verbatim (Grok l.1 `VERDICT: MAJOR REVISIONS`, ChatGPT l.1
`VERDICT: REJECT`) before any disposition. INT-Claude re-confirmed the NJL exclusion.
No faked ACCEPT. No un-sourced dismissal (every finding → §/L + D-id). No math fabricated
(the AA factor-2 / 0.31 is an algebraic consequence of the paper's own `eq:AAdecomp`).
No hedging removed. The opposite-direction INT Grok(REJECT)/Gemini(MINOR) split on identical
content is recorded as the referee-variance signal it is, not steered.
