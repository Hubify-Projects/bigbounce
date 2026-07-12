# P1U NJ5 truth-audit — v1U.0.17 — STRICT ledger-first

**Wave:** NJ5 (2026-07-12) — FIRST re-test of the v1U.0.17 AA-channel bound fix (DP1U-NJ4-01).
**Adjudicator stance:** skeptical, verdict-first, NOT told a convergence conclusion.
**Method:** `tools/ledger_match.py` pre-triage → full §3 manual truth-audit of every finding
vs `arxiv/paper1_unified.tex` v1U.0.17 + `project-context/peer-reviews/DISPOSITIONS/P1U.md`.

## Verdict matrix (raws read verbatim before any disposition)
| Leg | Reviewer | Verdict | Raw / source |
|-----|----------|---------|--------------|
| INT | OpenAI (gpt-5.5) | REJECT | run.log 10:22Z |
| INT | Grok (grok-4.3) | MAJOR (softened from REJECT) | run.log 10:22Z |
| INT | Gemini (gemini-3.1-pro) | MAJOR | run.log 10:22Z |
| INT | Claude (opus-4-8, subscription subagent) | MINOR | intwave_P1U_claude_0317.md |
| EXT | Grok | MAJOR (4 MAJOR + 2 MINOR) | NJ5/P1U_grok_NJ5.md l.1 `VERDICT: MAJOR REVISIONS` |
| EXT | ChatGPT | REJECT (12 MAJOR + 2 MINOR) | NJ5/P1U_chatgpt_NJ5.md l.1 `VERDICT: REJECT` |

## AA-bound fix — ENGAGED + VERIFIED this wave
INT-Claude (0317) explicitly recomputed the v1U.0.17 leg-(B) AA-channel numbers against
the committed artifacts:
- `eq:AAdecomp` `(J5·J5)→+¼SS+½VV−½AA−¼PP` = column-A of the machine-derived Fierz matrix
  in `fierz_lemma_check.py` (Itzykson-Zuber/Nieves-Pal, F²=1). Correct.
- `G_scalar=−3/64κ` (repulsive) / `G_AA=+3/32κ` / `G_PP=+3/64κ` — all match
  `njl_gap_equation_route1_results.json`.
- AA worst-case = `2×0.156 = 0.31` (factor `G_AA/|G_scalar|=2` exact); "far"→"sub-critical"
  alignment confirmed (abstract L1244 + appendix L5118-5132 + main-text mirror L2704-2710).
- Reviewer verdict on the fix: *"correct, honest, and fully closes the overstatement … no fabrication."*

The DP1U-NJ4-01 PP-only overstatement fix **holds on independent re-test.**

## Genuinely-new vs re-flag — 0 genuinely-new reader-visible editable findings

### INT-Claude 3 MINORs → all PROCESS-NIT (reviewer's own "conclusion is safe / no change required")
1. `G_crit` (scalar-channel critical coupling) used as a proxy yardstick for AA criticality;
   AA's own loop structure not separately derived → **PROCESS-NIT, DP1U-NJ4-01/-19**. Reviewer:
   "does not threaten the conclusion … decisive leg is the channel-independent scalar sign."
   Optional one-line caveat, not a reader-visible defect.
2. Flavor scan tops at `N_fN_c=9`; realistic SM `N_fN_c≈24` → ≈0.42, still sub-critical
   (crossing 1 needs `N_fN_c≈210`), monotone → **PROCESS-NIT, DP1U-19/-05**. Presentation /
   scope-labeling on an already-sub-critical result; conclusion safe per reviewer.
3. Mean-field-NJL qualifier must not be dropped → reviewer states **"no change required"**;
   DP1U-19 disclosed-scope confirmation. **PROCESS-NIT.**

### EXT-Grok (4 MAJOR + 2 MINOR) → all source-cited re-flags
- [MAJOR] four-route "channel-level closure not exhaustive at M_Pl power-counting" → **DP1U-06/-07/-20**
  (paper's own "channel-level, not an operator-level theorem" L1219/L1389-1390).
- [MAJOR] 13/14-barrier repackages amplitude-suppression, not independent → **DP1U-13**
  (sec:barriers head discloses non-independence).
- [MAJOR] §X perturbation-transparency = standard EC torsion-free-limit corollary, overstates
  novelty → **DP1U-12** (RE-FLAG-DISCLOSED, OPINION on novelty).
- [MAJOR] parity-odd dim+1 → ρ_Λ via single-scale NDA is phenomenological ansatz "relocates not
  solves CC" → **DP1U-08 (+DP1U-11)** (verbatim the paper's disclosed framing).
- [MINOR] 63pp length/self-reference → **DP1U-22**.
- [MINOR] "explicit SS/PP/VV/AA channel tabulation with numerical coefficients would strengthen
  reproducibility" → **DP1U-19 (+DP1U-NJ4-01)** — *DIRECTLY answered by the v1U.0.17 AA addition*
  (`eq:AAdecomp` L5029 + G_scalar/G_AA/G_PP coefficients tabulated L5118-5132); a re-flag the fix
  already satisfies.
- `ledger_match.py`: 5/7 auto-MATCHED (line-1 header non-finding + MINOR-length prose-diluted).
- Grok's own closing sentence: the four-route closure "is supported under the stated assumptions."

### EXT-ChatGPT (12 MAJOR + 2 MINOR) → all source-cited re-flags (harsh-referee floor, directive-H)
Identical structure to every prior ChatGPT REJECT (H17G/W1/W2b/NJ3b/NJ4):
Eq(1)-(4) variational hybrid=**DP1U-03**; dim+1 "identity can't change dimension"/Eq(6)/basis
O1=O6/O4 undefined=**DP1U-08/-07/-20**; R1 NJL ⟨J5⟩⇏⟨J5J5⟩ + Fierz exchange/mean-field
ambiguity=**DP1U-05/-19/-26/-NJ4-01**; R2 (∂ϑ)J5 dim/field-excursion/10⁻⁶⁰=**DP1U-09**;
R3 Immirzi-running not connected to observable=**DP1U-10**; R4 ALP not minimal-ECH/fixed-vs-floated
=**DP1U-11**; §X transparency standard/domain-mismatch=**DP1U-12**; D_inf/N_tot≃92/erasure=**DP1U-14**;
f_NL −35/16 vs Cai −35/8=**DP1U-17**; 13-barrier not independent=**DP1U-13**; MINOR App F–H don't
test ECH=**DP1U-15/-24**; MINOR κ conventions/notation/length=**DP1U-02/-22**.
`ledger_match.py`: 8/12 auto-MATCHED (4 UNMATCHED prose-diluted, Opus-adjudicated to the above).
ChatGPT ENGAGED the NJL appendix via leg-(B)/Fierz only; did not rebut the leg-(A)
convention-independent sign exclusion (same partial-engagement as NJ2/NJ3b).

### INT OpenAI REJECT / Grok MAJOR / Gemini MAJOR → same disclosed classes
single-scale NDA no-go→DP1U-08; channel-vs-operator→DP1U-06/-20; routes→DP1U-05/-09/-10/-11;
§X→DP1U-12; style/length→DP1U-22/-24. INT Grok REJECT→MAJOR softening on the improved v1U.0.17 =
presentational pattern-066, not new content. **0 genuinely-new.**

## Streak / cap / bump
- **Streak:** prior 0 (RESET at NJ4 by DP1U-NJ4-01). NJ5 = 0 genuinely-new on the re-test →
  **RESET(0) → 1** (directive-K). The AA-bound fix holds on independent re-test.
- **Cap:** 50 + grok(major 6) + chatgpt(reject 0) + gemini(major 6) = **62 HOLDS**.
- **Version:** no bump — v1U.0.17 stands (no edit); `directive_g.sh` NOT run.

## Integrity
Both EXT raws read verbatim before any disposition. INT-Claude recomputed the AA-bound and
confirmed the fix correct. No faked ACCEPT. No un-sourced dismissal (every finding → §/L + D-id).
No math fabricated (the AA factor-2/0.31 is an algebraic consequence of the paper's own `eq:AAdecomp`).
The 3 INT-Claude MINORs were dispositioned PROCESS-NIT on the reviewer's OWN "conclusion is safe /
no change required" statements, not waved away. No hedging removed.
