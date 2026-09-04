# A3M v3M.0.11 — R5VERIFY truth audit (independent, verdict-first)

- **Round:** `ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY`
- **Manuscript:** `research/track_a3_multichannel/paper/main.tex` + `main.pdf`, v3M.0.11, 14 pp
- **sha256 (bound):** `790fafa691e1a6ef0c476309d8224c5f2af2a59e4a3966f6afa0cf9d9dff4105`
- **Board:** `INT_v3/A3M_v3M.0.11_R5_BOARD_2026-09-04.md`
- **Prior canon:** `DISPOSITIONS/A3M.md`; `INT_v3/A3M_v3M.0.9_R4_TRUTH_AUDIT_2026-09-04.md` (ids `DA3M-R4-*`).
- **Legs audited:** Grok API `grok-4.3` (REJECT, 3E/3M/2m/2N); Gemini API `gemini-3.1-pro-preview`
  (MAJOR REVISIONS, 4E/3M/1m/1N); Claude Fable 5.1 INT subagent (major-revisions, 5 MAJOR / 16 minor).
  OpenAI ABSENT (directive N pause); Perplexity ABSENT (quota) — recorded, never counted clean.
- **Auditor:** skeptical in both directions, told no expected outcome. Every verdict below is decided
  from a source — a `.tex` line, a committed JSON/script, or the auditor's own arithmetic.
- **Protocol:** `/peer-review-truth-audit` + `/bigbounce-truth-audit`, patterns 061–066,
  directive H-refined, directive R2.

## PLAN (this audit, in order)

1. Independent verification table — re-check the physics behind the five Fable MAJORs
   (M1 S1-only `0 ≤ T < 1/2` vs S2 `λ_ζ=0.97`; M2 `2.1–4.4 decades` vs `|f_NL|≈1.2e3` equilateral;
   M3 NANOGrav `6.3e-10` vs `3.6e-9` and the 13.6/14.3 gap; M4 δN normalisation; M5 Choudhury sign)
   and Grok's three ESSENTIALs + Gemini's four ESSENTIALs, each against a committed source.
2. Per-leg / per-class counts.
3. Canonical numbered findings with class + verdict citation + closure action.
4. Closure plan split (i) editorial/real edits for v3M.0.12 (Sonnet lane, exact file/lines,
   incl. the two >10pt overfull baselines) and (ii) SCIENCE items needing a ledger computation.
5. `DISPOSITIONS/A3M.md` update.

*(Sections appended below as each is completed and committed.)*
