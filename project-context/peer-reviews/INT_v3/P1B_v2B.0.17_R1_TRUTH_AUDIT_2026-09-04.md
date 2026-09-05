# P1B v2B.0.17 R1 — truth audit (2026-09-04)

**Plan header.** Skeptical truth-auditor, told no expected outcome. Scope: the three
active legs (Grok API `grok-4.3`, Gemini API `gemini-3.1-pro-preview`, Claude INT Opus)
against the exact PDF sha256 `0d0c92ab…4001fcac`, 8 pp. Protocol: patterns 061–066,
directive H-refined. Every finding is fingerprinted, merged across legs, and classified
(a) GENUINELY-NEW REAL / (b) re-flag of a canonical disposition / (c) FALSIFIED with a
source citation / (d) OPINION / (e) OUT-OF-SCOPE disclosed. **Post-freeze work is not a
falsification:** findings already answered by the pre-registered batch 2 (frozen 2026-09-04,
after the PDF was frozen) are classed (a) GENUINELY-NEW REAL and marked
*closable in v2B.0.18 by integrating batch 2*. Sections: canonical list → per-leg counts →
verifications → closure plan (editorial + science).

**Steps:** (1) board [done]; (2) canonical list; (3) named verifications; (4) closure plan.

---

## Verification of the post-freeze evidence trail

Read directly, not taken on assertion:

- `pipelines/namaster_proof/blind_test/RULES_v2_FROZEN.md` — rule set R0–R6 with the
  wall-clock floor demoted to advisory and the M-hash rule withdrawn, plus pre-declared
  thresholds, Clopper–Pearson reporting requirement, the independence caveat, and an
  explicit "no rule may be added, removed, or edited between this freeze and the batch-2
  reveal".
- `pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md` §6 "Batch 2".
- Commit-ordered trail, each in its own commit: `4451b135` (rules alone) → `28efa21c`
  (seal + S6 variant + `public2/sealed_digest.json`, no run output) → `27300504`
  (35 result+receipt pairs + `verdicts.json`) → `974e2859` (`sealed2/key.txt` reveal +
  scorecard) → `b3347c53` (manifest). Sealed key/assignment held outside the working tree
  through the sealed window; sealed digest `c96b5bf1…`, `seal_verified: true`.
- `pipelines/namaster_proof/RELATED_WORK_NOTE_2026-09-04.md` (commit `05b5940a`).
- Abstract of `arxiv/paper1b_namaster_proof.tex` read verbatim to check every quoted claim.

**Batch-2 outcome (35 runs, 7 arms × 5):** honest 0/5 flagged; S1–S4 5/5 each = **20/20**;
S5 metadata forgery escaped 5/5 (pre-declared); **S6 effective-multipole escaped 5/5**, and
**no rule was added after the fact**. One-sided 95% Clopper–Pearson: sensitivity lower
bound **0.861** (= 0.05^(1/20)); FPR upper bound **0.451** (= 1 − 0.05^(1/5)). Batch-1
equivalents, for the pilot framing: 12/12 → lower bound **0.779**; 0/3 → upper bound **0.632**.
