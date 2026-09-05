# P1B v2B.0.20 R3 — REVIEW BOARD (verdicts read from raw text, not labels)

**Exact artefact.** `arxiv/paper1b_namaster_proof.pdf`
sha256 `cf57f485c20acd8c5e9dc8277a65ca9a6ce1dac8db4b2e360be98845e7ee50cf`, 15 pp.
Byte-identical to `site/public/papers/paper1b_namaster_proof_v2B.0.20.pdf`
(both hashed at audit time — same digest, verified).

**Preflight receipt.**
`INT_v3/ROUND_2026-09-05-P1B-v2B.0.20-EXACTPDF-cf57f485-R3VERIFY/preflight_receipt.json`
— core sha256 `5af8959c1fc7e6c3904c8443adb7595517a16633c4b9e35603673b83304ff71e`,
generated 2026-09-05T08:32:47Z, engine `pre_review_check.py` sha256 `c81578ce…`
@ commit `79a436e2`, 9 rules, **0 findings**; source `arxiv/paper1b_namaster_proof.tex`
sha256 `8e8f5f4851de9f64e86a1a4c49e8a2e99866e6655f75af848e6133140b41a13a`.
Leg log: `…-R3VERIFY/api_legs_run.log`. No leg raw contains "Reviewer call FAILED".

## Per-leg verdicts (quoted from the raws)

| Leg | Model | Stance | Verdict (raw text) | E | M | m | Q |
|---|---|---|---|---|---|---|---|
| `Grok_brutal` | grok-4.3 | adversarial JORS-SOFTWARE referee, PDF→PNG 150 DPI | **REJECT** | 5 | 3 | 2 | 0 |
| `Gemini_cosmology` | gemini-3.1-pro-preview | PRD cosmology-physics referee, native PDF | **MAJOR REVISIONS** | 2 | 2 | 1 | 0 |
| `Claude Opus INT` | Opus INT leg | independent skeptical, repo-inspecting | **major-revisions** | – | 6 | 11 | 5 |

Raws:
- `../ROUND_2026-09-05-P1B-v2B.0.20-EXACTPDF-cf57f485-R3VERIFY_P1B_Grok_brutal.md`
  (packet `dee953a22101ff85…`, wall 58.9 s) — summary line: "REJECT".
- `../ROUND_2026-09-05-P1B-v2B.0.20-EXACTPDF-cf57f485-R3VERIFY_P1B_Gemini_cosmology.md`
  (packet `e48a1b7e6a04e21b…`, wall 125.6 s) — summary line: "MAJOR REVISIONS".
- `P1B_v2B.0.20_R3_claude_opus_2026-09-05.md` — "**Verdict: major-revisions.**"

Raw item counts: Grok E1–E5, M1–M3, N1–N2 = **10**; Gemini E1–E2, M1–M2, N1 = **5**;
Opus M1–M6 + minors 1–11 + Q1–Q5 = **17 findings + 5 questions**. Gross **32 + 5 Q**.

## Verdict trajectory (P1B active legs, directive M-AMENDED)

| Round | PDF sha256 | pp | Grok API | Gemini API | Claude INT |
|---|---|---|---|---|---|
| R1 v2B.0.17 (2026-09-04) | `0d0c92ab…` | 8 | — | — | major-revisions |
| R2 v2B.0.18 (2026-09-04) | `354d63b2…` | 12 | REJECT | MINOR REVISIONS | major-revisions |
| **R3 v2B.0.20 (2026-09-05)** | `cf57f485…` | 15 | **REJECT** | **MAJOR REVISIONS** | **major-revisions** |

Gemini moved MINOR → MAJOR on a paper that grew by a batch (batch 3 + R7 + the PyMaster
cross-check, 12 → 15 pp). That is not a regression in quality: Gemini's MAJOR is driven
almost entirely by one defect class introduced with the new batch-3 text (run-level
Clopper–Pearson intervals + the `24/24` slip), which the R2 round had just removed from
the batch-2 presentation. Grok's REJECT is unchanged in kind from R2 (genre/venue-length
plus the same in-house-estimator complaint), i.e. structurally a re-flag of D-R2-20/23.

## Integrity check on the board itself

No leg was dropped, no verdict inferred from a label, and no leg was re-run after seeing
its output. The Opus leg records what it verified in-repo (batch-3 commit ordering, sealed
assignment digest `abfe2793bc6fa2c0…`, PyMaster cross-check numbers) and its own integrity
note states the `24/24` slip runs *against* the authors' interest — consistent with the
recomputation in the truth audit (`§2 D-R3-04`). Full adjudication:
`P1B_v2B.0.20_R3_TRUTH_AUDIT_2026-09-05.md`.
