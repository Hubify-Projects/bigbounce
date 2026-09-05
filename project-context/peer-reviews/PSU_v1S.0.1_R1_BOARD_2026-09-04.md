# PSU v1S.0.1 — R1 review board (2026-09-04)

**Paper**: `paper-su` — "When the separate universe fails: a criterion for the squeezed
bispectrum in non-attractor phases", v1S.0.1, 4 pp.
**Exact PDF**: `arxiv/paper_su_criterion/main.pdf` == `site/public/papers/paper_su_criterion_v1S.0.1.pdf`
**sha256**: `cc0dfb84a232967c45ea359d5de18f642af0727c2907512b289931854ed7c48e`
**Round id**: `ROUND_2026-09-04-PSU-v1S.0.1-EXACTPDF-cc0dfb84-R1`
**Preflight receipt**: `INT_v3/ROUND_2026-09-04-PSU-v1S.0.1-EXACTPDF-cc0dfb84-R1/preflight_receipt.json`
(schema `hubstack.paper-pre-review-receipt/v1`, `finding_count: 0`, generated 2026-09-05T02:09:01Z,
engine sha256 `c81578ce…`, core sha256 `82d81553…`)
**Venue bound**: Physical Review D — Letter / short note (all three legs reviewed to that bar).
**First board for this paper.** No prior PSU round exists; there is no prior disposition ledger,
so every finding is adjudicated here from scratch.

## Verdict matrix (verdict WORDS read verbatim from each raw)

| leg | reviewer | model | verdict (raw text) | E | MAJOR | minor | Q |
|---|---|---|---|---|---|---|---|
| INT | Claude Fable 5.1 (`INT_v3/PSU_v1S.0.1_R1_claude_fable_2026-09-04.md`) | claude-fable-5.1 | **major-revisions** | — | 6 (M1–M6) | 10 (m1–m10) | 5 (Q1–Q5) |
| API | Grok brutal (`ROUND_…_PSU_Grok_brutal.md`) | grok-4.3 | **REJECT** | 7 (E1–E7) | 6 (M1–M6) | 4 (N1–N4) | — |
| API | Gemini cosmology (`ROUND_…_PSU_Gemini_cosmology.md`) | gemini-3.1-pro-preview | **MAJOR REVISIONS** | 2 (F1–F2) | 3 (F3, F4, B1) | — | — |

Raw-leg count: 3 attempted, 3 returned full reports, 0 FAILED. No leg was recorded from a label;
each raw was read in full before any verdict above was written. No OpenAI/ChatGPT leg was run
(directive N pause) — that column is absent, not faked.

## Reviewer-agreed items (independent convergence across legs)

Three legs independently flagged the SAME two defects, which is the strongest signal on this board:

1. **The second-order composition contradicts Table I at the quadrupole.**
   Grok PSU-M6, Gemini Finding 1 (ESSENTIAL), Fable M2. All three did the dust substitution
   and all three got a μ²-dependent number where the paper prints the isotropic −5.
2. **Fig. 1 caption "Both vanish at w = −1" is false for λ.**
   Grok PSU-M5 (pass-2), Gemini B1 (pass-2), and it is visible in the committed figure.
   λ(−1) = 1, not 0.

Two legs agreed on:

3. **Load-bearing results imported from unpublished self-citations [18], [19] (GitHub .md).**
   Grok PSU-E3/E7, Gemini Finding 2 (ESSENTIAL), Fable M1 (third leg, framed as the missing
   Cai+2009 reconciliation rather than as archival policy).
4. **Internal audit strings in the rendered PDF** (script name in §III, manifest path in the
   reproducibility statement). Grok PSU-E5, Gemini Finding 4; Fable m7 flags the same lines for
   a different reason (mid-token line breaks).
5. **The 8/3 headline is not derivable from anything printed in the body.**
   Grok PSU-E1/E6, Fable m1. (Gemini asserts 8/3 is "correct" without deriving it.)

## Board disposition summary (detail in `INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md`)

See the truth audit for the canonical de-duplicated list, per-item class, source-cited verdict,
and the two-part closure plan. Counts are reproduced at the head of that file.
