# P5 RS1 truth-audit — v0.1.122 → v0.1.123 (2026-07-12)

Wave: RS1 (first-order RSD reconstruction bound integrated — new §VIII content).
Adjudicator: Fable-5 orchestrator (ledger-first, `tools/ledger_match.py`) + Opus closure worker.
Raws (verified read before any verdict):
- EXT Grok `RS1/P5_grok_RS1.md` = **MINOR REVISIONS**
- EXT ChatGPT `RS1/P5_chatgpt_RS1b.md` = **REJECT**
- INT (run.log 2026-07-12T07:12:44Z, v0.1.122): openai=REJECT / grok=MINOR / gemini=MINOR / claude=**MAJOR** (`intwave_P5_claude_0008.md`)

## Verdict-first matrix (all vendors, I1)
| leg | channel | verdict | modality |
|-----|---------|---------|----------|
| Claude | INT | MAJOR REVISIONS | full-repo subscription subagent |
| OpenAI | INT | REJECT | native-PDF API |
| Grok | INT | MINOR REVISIONS | API |
| Gemini | INT | MINOR REVISIONS | API |
| ChatGPT | EXT | REJECT | headed browser |
| Grok | EXT | MINOR REVISIONS | headed browser |

## GENUINELY-NEW REAL (closed → v0.1.123) — caught by TWO independent reviewers
**R1 [INT-Claude MAJOR #1 AND EXT-ChatGPT MAJOR #5] — new RSD reconstruction mislabels the estimand + flips the sign.** Abstract (`:835-840`) and §VIII (`:2921-2924`) state "the **primary** footprint-restricted $\Delta f_{\rm CW}$ moves from $-0.069$ to $-0.045$ pp." But the generating script `scripts/27_rsd_void_recon_bound.py:219-224,304-305` computes the void bin against **all** non-void spirals with **no footprint mask** — the paper's own **unrestricted (secondary)** contrast ($n_{\rm nonvoid}\approx621{,}929$; `outputs/29_..._retabulation.json` `contrast_unrestricted`, $z=0.282$), NOT the footprint-restricted primary ($\Delta f_{\rm CW}=+0.001809$, $z=0.781$, $n_{\rm nonvoid}=253{,}276$). The two estimands differ by ~0.11 pp (~5× the reported RSD shift). Compounding: the script convention is $f_{\rm void}-f_{\rm nonvoid}$, the **opposite** of the paper's $\Delta f_{\rm CW}\equiv f_{\rm nonvoid}-f_{\rm void}$, so the printed values carry the wrong sign; in the paper's own convention they are $+0.069\to+0.045$ pp. VERDICT: **VERIFIED genuinely-new, reader-visible** (source-cited to script + artifact line numbers; independently corroborated by EXT-ChatGPT #5 which states "$+0.18$ pp under the manuscript's stated sign convention … it corresponds to an unrestricted any-hole contrast with the opposite sign convention"). The $|{\rm shift}|=0.024$ pp magnitude and null-preserved conclusion SURVIVE (computed self-consistently within one sample). CLOSED-BY-EDIT v0.1.123: relabeled as the unrestricted (secondary) contrast, sign corrected to $+0.069\to+0.045$ pp, clause added that the primary estimand was not itself reconstructed.
- Bundled: quadrature intermediate $\sqrt{0.886}\to\sqrt{0.898}$ (INT-Claude MINOR #2, artifact-verified 8-square sum = 0.898); one sentence noting reconstruction reassigns void membership 57,058→42,864 (−25%) but parity-symmetric so ΔfCW shift stays tiny (INT-Claude MINOR #3, `n_void_recon=42,864` confirmed in `outputs/27_...json`).

## RE-FLAGS (dispositioned, source-cited)
- EXT Grok [MINOR] ×5 → DP5-13 (post-hoc primary / pre-registration), DP5-11 (absolute-null language), DP5-14 (T-Web secondary bin), DP5-21 (Paper-IV dependency), DP5-12 (RSD fixed-redshift-space residual — its exact wording credits the "0.024 pp shift … reassuring", **ENGAGED** the new bound, re-flags the disclosed no-full-nonlinear-re-derivation residual). Central claim IS supported.
- EXT ChatGPT [MAJOR] ×11 → DP5-07 (edge-void/VoidFinder sample), DP5-06 (footprint-not-selection-function), DP5-13 (multiplicity/primary-in-family), DP5-11 (0.9pp RSS envelope), **DP5-16 (its #5 RSD = the same estimand/sign item = R1 above, but ChatGPT frames the fix-need; recorded as corroboration of R1)**, DP5-08 (de-attenuation 2a−1), DP5-10 (binomial independence / block bootstrap), DP5-16 (V2 sphere-membership), DP5-14 (T-Web randoms), DP5-20 (physics-interp parity-parity), DP5-21 (Paper-IV dependency). MINOR #16 → DP5-14. **ENGAGED** the new RSD content (independently re-derived R1).

## Engagement verdict
EVERY reviewer engaged the new RSD science. INT-Claude verified it against the committed artifacts line-by-line (and caught R1); EXT-ChatGPT independently re-derived the estimand+sign (corroborating R1); EXT-Grok credited the 0.024 pp coherent-outflow bound.

## Streak
RESET to 0 (R1 genuinely-new editable finding surfaced, directive-K). Note: the prior W2/FR1/FR1b chain streaks are superseded — a real defect in the new v0.1.122 content resets it.

## Integrity
No faked ACCEPT. No un-sourced dismissal. No fabrication — the fix is a labeling+sign correction verified against the paper's own committed artifacts (no new computation invented). Two independent reviewers catching the identical defect is the strongest possible signal it was real; recorded honestly.
