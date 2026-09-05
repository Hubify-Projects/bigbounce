# P1B v2B.0.20 R3 — TRUTH AUDIT (skeptical, verdict-first)

- Auditor: Claude Opus, independent skeptical truth-auditor. No expected outcome supplied.
- Date: 2026-09-05
- Exact artefact: `arxiv/paper1b_namaster_proof.pdf`
  sha256 `cf57f485c20acd8c5e9dc8277a65ca9a6ce1dac8db4b2e360be98845e7ee50cf`, 15 pp.
  Byte-identical to `site/public/papers/paper1b_namaster_proof_v2B.0.20.pdf` (verified, same sha256).
- Legs audited: Grok_brutal (grok-4.3, JORS-SOFTWARE adversarial) — REJECT;
  Gemini_cosmology (gemini-3.1-pro-preview, PRD-referee) — MAJOR REVISIONS;
  Claude Opus INT leg — major-revisions.
- Protocol: lab truth-audit, directive H-refined. Every finding fingerprinted and
  classified (a) genuinely-new REAL / (b) re-flag of already-addressed-or-disclosed /
  (c) FALSIFIED against source / (d) OPINION-or-venue-preference / (e) OUT-OF-SCOPE
  disclosed limitation. Citations to code/artefacts required for (b)/(c).
- Reference material: `DISPOSITIONS/P1B.md`, R1/R2 audits, `pipelines/namaster_proof/blind_test/`
  (`verify3.py`, `RULES_v3_FROZEN.md`, `RULES_v4_FROZEN.md`, `public3/scorecard.json`).

## PLAN
1. Board (`P1B_v2B.0.20_R3_BOARD_2026-09-05.md`) — per-leg verdicts + counts from raw text.
2. Verify Opus M1 (R7 spot-row predictability), M2 (r7_residual fail-open),
   M3 (batch-3 Clopper-Pearson vs batch-2 refusal; 24/24 vs 30/30) against the code.
3. Freivalds / Fiat-Shamir prior-art check; N3 wording; venue.
4. Grok REJECT rationale item by item; Gemini items.
5. Canonical finding list with class + citation + closure action.
6. CLOSURE PLAN — (i) editorial v2B.0.21, (ii) science (batch 4).
7. R2 statement; DISPOSITIONS/P1B.md update.

*(sections filled below as the audit proceeds)*
