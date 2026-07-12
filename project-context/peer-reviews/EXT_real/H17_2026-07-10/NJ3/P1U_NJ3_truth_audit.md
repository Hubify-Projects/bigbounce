# P1U NJ3 truth-audit (v1U.0.16)

**Wave:** NJ3 · **NOW-UTC:** 2026-07-12T08:44:21Z · **auditor:** Fable-5 orchestrator, STRICT ledger-first.

Raws read verbatim before any verdict:
- EXT Grok `NJ3/P1U_grok_NJ3.md` = **MAJOR REVISIONS** (verified).
- INT (run.log 2026-07-12T08:24:xxZ, v1U.0.16): openai=**REJECT** / grok=**REJECT** / gemini=**MAJOR** / claude=**MINOR** (`intwave_P1U_NJ3.log`, `API_P1U_*.md`).
- ChatGPT EXT leg = **FAILED-dead** (NJ3b retry in flight). Recorded as a chart GAP, NOT a zero. Do NOT wait.

The ONLY content delta v1U.0.15→v1U.0.16 is the DP1U-26 NJL leg-(A) precision fix (scalar χSB channel scoping; attractive AA/PP credited to leg B). Every finding this wave is judged against that delta.

## Verdict-first matrix (all vendors)
| leg | channel | verdict | modality |
|-----|---------|---------|----------|
| Claude | INT | MINOR REVISIONS | full-repo subscription subagent |
| OpenAI | INT | REJECT | API native-PDF |
| Grok | INT | REJECT | API |
| Gemini | INT | MAJOR REVISIONS | API |
| Grok | EXT | MAJOR REVISIONS | headed browser |
| ChatGPT | EXT | FAILED (dead) | — (NJ3b retry in flight) |

## ledger_match pre-triage
`tools/ledger_match.py … P1U` → 5/6 MATCHED (finding #1 is the parser-noise "REVISIONS ISSUES:" header, not a real finding). All 5 real EXT-Grok findings MATCHED.

## EXT Grok per-finding adjudication
- **[MAJOR] Abstract/title/Sec IV "four-route no-go / channel-level closure" overstates as a structural theorem** → **DP1U-06** (RE-FLAG-DISCLOSED). Title already reads "Under Stated Assumptions"; abstract/§IV already say "channel-level assessment, not an operator-level theorem" (L1219, L1389-90) with an evidentiary-tier table. Grok itself lists the paper's own qualifiers — exactly the disclosed framing. RE-FLAG, no reset.
- **[MAJOR] Sec X perturbation-transparency "all-orders" ambiguity vs S=0 branch** → **DP1U-12** (RE-FLAG-DISCLOSED; OPINION on novelty). Labeled the "standard on-shell equivalence," narrow positive core for canonical scalar matter, fermions/torsion/dynamical-γ explicitly excluded (Claude-verified). RE-FLAG, no reset.
- **[MINOR] Sec IX 14-barrier catalog mixes tiers / redundancy → tiered classification** → **DP1U-13** (RE-FLAG-DISCLOSED). `sec:barriers` head already states "no barrier is a logical consequence of another … not thirteen separately decisive theorems," flags B8⊂B14, B9 heuristic, etc. RE-FLAG, no reset.
- **[MINOR] Sec IV A / App D NJL Route-1 mean-field caveats (curved-space, Planck-suppressed, cutoff-scheme)** → **DP1U-05** (CLOSED-BY-COMPUTE v1U.0.14) + **ENGAGES the DP1U-26 delta**. Grok engaged the corrected appendix (regulated gap-eq, repulsive scalar channel, sub-critical coupling) and asks only for a mean-field-breakdown caveat paragraph. The standard mean-field framework is already stated in-paper; strong-coupling-beyond-mean-field is disclosed OUT-OF-SCOPE. RE-FLAG, no reset.
- **[MINOR] length/self-referential/condense Sec IX + move technical verifications to supplement** → **DP1U-18 / DP1U-24** (CLOSED-BY-EDIT + style-disclosure). Presentation preference. RE-FLAG, no reset.

## Gemini-P1U INT oscillation diagnosis (MIN→MAJ)
**Referee variance (pattern-066), NOT a response to new content.**
- NJ2 (v1U.0.15): Gemini INT = **MINOR** (its first-ever P1U minor, verified from `intwave_P1U_..._0032.log`).
- NJ3 (v1U.0.16): Gemini INT = **MAJOR** (`API_P1U_gemini.md`, PARSED VERDICT line 6).
- The only content change between the two versions is the DP1U-26 NJL leg-A scoping fix. Reading the NJ3 Gemini raw quote-by-quote: its **three MAJORs are #1 title/abstract too long + PRD-style ("over 600 words, reads like a legal contract"), #2 excessive meta-commentary/defensiveness/tier-labels ("belongs in a cover letter"), #3 Sec X "trivial corollary" framing.** NONE of the three touches the NJL/DP1U-26 delta. Its two MINORs (#4 NDA "no-go" terminology → soften to "naturalness constraint"; #5 NJL mean-field breakdown near M_Pl) are the only items near the changed appendix, and both are DISCLOSED re-flags (→ DP1U-05/DP1U-19 and the naturalness class).
- So Gemini re-weighted long-standing **presentational** complaints (abstract length, meta-text, Sec-X novelty framing — all → DP1U-24 style-disclosure + DP1U-12) from MINOR to MAJOR on content whose only real delta it did not object to. Its own one-sentence: "The central claim … is robustly supported by the physics presented." **Oscillation = presentational-axis referee variance on unchanged science, not a genuinely-new finding.** Its MAJORs #1/#2 map to **DP1U-24**, #3 to **DP1U-12** — all pre-existing dispositions.

## Adjudication outcome
**0 genuinely-new reader-visible editable findings** across EXT-Grok + all INT legs (INT-Claude MINOR content also maps to existing dispositions; OpenAI/Grok INT REJECTs are the documented maximal-harsh structural floor on the operator-basis/route-completeness items → DP1U-06/-07/-10). All findings are source-cited RE-FLAGs / OPINION / OPEN structural-floor. **NO bump; v1U.0.16 stands. directive_g.sh not run (no edit).**

## Streak
P1U clean-wave streak was RESET to 0 at NJ2 (DP1U-26 genuinely-new editable finding, closed in v1U.0.16). NJ3 clean (0 genuinely-new) → **streak 0→1** under directive-K.

## Cap
post_verdict after Grok EXT MAJOR (unchanged verdict): 50 + grok(major 6) + chatgpt(reject 0) + gemini(major 6) = 62 → **cap 62 HOLDS**.

## Integrity
No faked ACCEPT. No un-sourced dismissal — every finding cites a §/L + D-id. No fabrication. Gemini MIN→MAJ diagnosed against the raw as presentational referee variance, not steered. ChatGPT FAILED recorded as a GAP.
