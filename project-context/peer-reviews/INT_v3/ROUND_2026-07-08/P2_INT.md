# P2 INT — full-source regression check (v1.7.102)

**Reviewer:** Claude Code INT (subscription subagent, full-source read — CLAUDE.md I1)
**Scope:** closure-wave regression check only (9 tone-neutralized passages + r=0.84 / r_eff≈0.99 / significance consistency). No new-finding hunt.
**File:** `research/focused_paper_source_integration/02_full_draft.tex`

## Verdict: CLOSURE WAVE CLEAN — no regressions

### Tone-neutralization (Gemini MAJOR closure, commits f44ceea8 + 0eceaacc)
Every one of the tone edits is a pure register change with meaning preserved:
- SVD conditioning para (`chirality`→n/a): "we emphasize that σ₃/σ₁≈0.3…" → "σ₃/σ₁≈0.3 is an empirical property…" — same claim, declarative.
- f_sky heuristic: "We stress that this 1/√f_sky statement…" → "This 1/√f_sky statement…"; "we do not use this scaling" → "this scaling is not used". Identical content.
- UV-completion qualifier: "We emphasize 'UV-completion-independent' rather than…" → "The qualifier … is used rather than…". Same scope caveat.
- `para:reconcile` head signpost: "a referee may ask" → "a natural question is"; "We emphasize two honest points" → "Two scope points apply". Meaning preserved.
- §IX.E signpost paragraph fully recast "Response to recurring referee concerns" → "Scope summary" — declarative rewrite; every item (i)–(vi) retains its numbers (r=0.84, r_eff≈0.99, 3.2–3.5σ, 1.3–2.75σ, −35/16, −35/8, BF 9–14, c8/c13 artifacts). No claim added or dropped.
- §IX.E body: "We emphasize that a detection of f_NL≈−2 would constitute evidence favoring…" → "A detection of f_NL≈−2 would constitute evidence favoring…". Same.
- App A: "a narrative we explicitly reject" → "is not a dropped-time-ordering artifact"; "We emphasize that the identity…" → "The identity…". Same.
- Sec VI Bayesian: "We emphasize that the delta-function prior…" → "The delta-function prior…". Same.

### Cai–Li Appendix-A consistency (ChatGPT MAJOR → MISREAD; verified internally consistent)
Closure ADDED a clarifying sentence (L~[App A]): Li's printed polynomial (Eq. 4.19) agrees coefficient-for-coefficient with Cai's (Eq. 37) at c_s=1, both reduce to −35/8 under naive squeezed reduction, and the corrected −35/16 comes from re-summing Cai's four cubic vertices directly (bypassing the shared printed polynomial), with Li's closed-form general-c_s (Eq. 5.1) giving −35/16 at c_s=1 independently. This STRENGTHENS internal consistency; introduces no contradiction with the existing spurious-(99/128)Σk³ discrepancy narrative (which is explicitly labeled "one identified discrepancy, not by itself the full mechanism").

### r=0.84 vs r_eff≈0.99 vs significance — ZERO contradictions
Single reconciliation at `\label{para:reconcile}` (L947): r=0.84 = conservative flat-weight shape-overlap cosine (recast factor, Eq. projection); r_eff≈0.99 = survey-optimal amplitude-recovery factor of the independent multi-tracer Fisher (squeezed-dominated covariance). "The independent Fisher confirms r=0.84 is conservative." Abstract (L749), §IX.E items (i)/(iv), and the Fisher paragraph all point HERE and use the numbers identically. Unmarginalized 3.2–3.5σ is consistently distinguished from the systematic/GR-projection-budgeted headline 1.3–2.75σ; the GR bracket "still applies on top and is retained exactly as before."

**No number, no disclosure changed in v1.7.102** (verified from diff headers; date stays July 7/8 2026). Regressions: **none**.
