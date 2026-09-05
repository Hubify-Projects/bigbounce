# PSU v1S.0.2 — R2 verdict board (2026-09-04)

**Exact artifact:** `arxiv/paper_su_criterion/main.pdf` == `site/public/papers/paper_su_criterion_v1S.0.2.pdf`
sha256 `812dbaf1af7e8eafa5769730fed55c81cfa8b429fbeab022d1125be1527aca31`, md5 `fcbecd03…`, 4 pp.
**Receipt:** `project-context/peer-reviews/INT_v3/ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY/preflight_receipt.json`

| Leg | Model | Verdict (raw) | ESSENTIAL/MAJOR | minor/nit | Questions | Raw |
|---|---|---|---|---|---|---|
| Grok (adversarial, native PDF) | grok-4.3 | **REJECT** | 4 ESSENTIAL (E1–E4) + 3 MAJOR (M1–M3) | 3 (N1–N3) | — | `ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY_PSU_Grok_brutal.md` |
| Gemini (PRD cosmology, native PDF) | gemini-3.1-pro-preview | **MAJOR REVISIONS** | 4 ESSENTIAL (3 + pass-2 PSU-E1) + 2 MAJOR | 3 (MINOR, NIT, pass-2 PSU-m1/PSU-N1 → 3) | — | `ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY_PSU_Gemini_cosmology.md` |
| Claude Fable 5.1 INT | fable-5.1 | **MAJOR REVISIONS** | 6 MAJOR (M1–M6) | 13 | 4 | `INT_v3/PSU_v1S.0.2_R2_claude_fable_2026-09-04.md` |

Fable leg independently re-derived Eq. (1) from ∇_μu^μ and the linear map via Friedmann on
uniform-φ slices, and ran sympy on the composition algebra (report §Integrity note).

Truth-audit: `INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md`.
