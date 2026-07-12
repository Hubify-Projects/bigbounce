# P1U NJ2 truth-audit — v1U.0.15 → v1U.0.16 (2026-07-12)

Wave: NJ2 (Holst 14.3× correction + NJL vacuum-condensate exclusion appendix `app:njl_gap`).
Adjudicator: Fable-5 orchestrator (ledger-first, `tools/ledger_match.py` pre-triage) + Opus closure worker.
Raws (verified read before any verdict):
- EXT Grok `NJ2/P1U_grok_NJ2.md` = **MAJOR REVISIONS**
- EXT ChatGPT `NJ2b/P1U_chatgpt_NJ2b.md` = **REJECT**
- INT (run.log 2026-07-12T07:36:04Z, v1U.0.15): openai=REJECT / grok=MAJOR / gemini=**MINOR** / claude=**MINOR** (`intwave_P1U_claude_0032.md`)

## Verdict-first matrix (all vendors, I1)
| leg | channel | verdict | modality |
|-----|---------|---------|----------|
| Claude | INT | MINOR REVISIONS | full-repo subscription subagent |
| OpenAI | INT | REJECT | native-PDF API |
| Grok | INT | MAJOR REVISIONS | API |
| Gemini | INT | MINOR REVISIONS | API — **FIRST MINOR on P1U** |
| ChatGPT | EXT | REJECT | headed browser |
| Grok | EXT | MAJOR REVISIONS | headed browser |

## GENUINELY-NEW REAL (closed → v1U.0.16)
**N1 [INT-Claude MINOR #1] — leg-(A) sign exclusion is not channel-complete.** The new appendix presents leg (A) as decisive ("no condensate at **any** coupling strength or cutoff", `:2688`, `:5089-5095`). But by the paper's own Fierz lemma `eq:AAdecomp` ($(J^5\!\cdot\!J^5)\to+\tfrac14 SS+\tfrac12 VV-\tfrac12 AA-\tfrac14 PP$), the operator $-\tfrac{3}{16}\kappa(J^5\!\cdot\!J^5)$ gives an **attractive** AA channel ($G_{\rm AA}=+\tfrac{3}{32}\kappa>0$) and an **attractive** PP channel ($G_{\rm PP}=+\tfrac{3}{64}\kappa>0$). Leg (A) only excludes the **scalar** $\chi$SB channel where $\langle\bar\psi\psi\rangle$ lives; the attractive AA/PP channels are excluded ONLY by magnitude leg (B) (which does cover them, $|G_{\rm PP}|=|G_{\rm scalar}|$ equally sub-critical). VERDICT: **VERIFIED genuinely-new, reader-visible** (source-cited with .tex line numbers, on new content). CLOSED-BY-EDIT v1U.0.16: leg (A) scoped to the scalar channel, attractive AA/PP explicitly credited to leg (B). Arithmetic re-derived from the paper's own lemma (nothing fabricated).
- Bundled minors (same closure): "far sub-critical … every case scanned" tempered to "comfortably sub-critical (worst scanned ratio 0.156)" (INT-Claude MINOR #2); Λ² cutoff-sensitivity noted (MINOR #3, partial).

## RE-FLAGS (dispositioned, source-cited)
- **EXT Grok [MAJOR] Sec IV A/App D** — asks that the Fierz projection coefficients + regulated gap-equation solution be displayed in the main text / a self-contained excerpt rather than referenced to `arxiv/scripts/njl_gap_equation_route1.py`. This is a **transparency/self-containment** ask → DP1U-19. Grok's own one-sentence says the central claim IS supported. NOT a physics defeater. **ENGAGED the new appendix** (named the G_scalar=−3/64κ result). PROCESS/transparency re-flag.
- EXT Grok [MAJOR] Routes 2/3 scaling ansätze not first-principles → DP1U-10 (disclosed "explicitly-labeled scaling ansätze").
- EXT Grok [MAJOR] 13-barrier catalog "list not demonstrated set" → DP1U-13. EXT Grok minors → DP1U-08/-12/-19.
- **EXT ChatGPT [MAJOR] #8 NJL condensate exclusion "not established by the displayed Fierz coefficient"** — demands exchange signs, color/flavor contractions, Hartree AND Fock channels, full auxiliary-field decomposition → DP1U-05. **ENGAGED** (re-derived the coupling); this is the known maximal-harsh referee floor on the Route-1 NJL item. The v1U.0.16 leg-(A) scoping partially answers it (mean-field scalar-channel decomposition now explicit); the broader Fock-channel demand is the documented structural-floor re-flag. Not genuinely-new-editable.
- EXT ChatGPT [MAJOR] #1-7,9-14 + MINOR #15 → DP1U-03/-08/-07/-04/-09/-10/-11/-12/-13/-14/-17/-14/-15/-02 (all matched, all pre-existing route/operator/model-definition/numerical/notation classes; the −35/8-vs-−35/16 re-flag #12 = DP1U-17, the companion-derivation disposition).

## Engagement verdict
EVERY reviewer engaged the new science: INT-Claude verified the Holst 14.3× fix + recomputed every ratio against the artifacts; EXT-Grok named the G_scalar result; EXT-ChatGPT re-derived the Fierz coupling. (Corrects the prior W2-ledger note that "neither EXT reviewer engaged the appendix" — ChatGPT #8 and Grok's IV-A MAJOR both do, this wave.)

## Milestone
Gemini INT returned its **first MINOR REVISIONS on P1U** (`.intwave_P1U_gemini_0032.log`), after MAJOR/MAJOR on v1U.0.13/.14. Verified from raw log. Posted to activityFeed (milestone).

## Streak
RESET to 0 (N1 genuinely-new editable finding surfaced, directive-K).

## Integrity
No faked ACCEPT. No un-sourced dismissal. No fabricated math (leg-A coupling arithmetic is an algebraic consequence of the paper's own `eq:AAdecomp`). Every finding mapped to a source-cited D-id or a verified genuinely-new closure.
