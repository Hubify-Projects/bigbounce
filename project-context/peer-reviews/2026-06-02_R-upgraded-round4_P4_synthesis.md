# P4 R-upgraded-round4 — synthesis (cascade counter 1/3 → 2/3)

**Paper**: P4 chirality catalog
**Pre-round version**: v1.0.148
**Post-round version**: v1.0.149 (1 verified BLOCKER + 1 verified MAJOR closure)
**Vendors**: 4 (Gemini-2.5-Pro, GPT-4o fallback, Grok-4, Perplexity Sonar Pro)
**Date**: 2026-06-02 PDT
**Cascade counter**: 1/3 → **2/3** (post-truth-audit)
**Pattern catalog**: 34 patterns referenced

---

## Per-finding truth-audit table

| Finding | Class | Verdict | Pattern-ID | Closure |
|---------|-------|---------|------------|---------|
| GRO-B1 (canonical +3.64σ tension) | BLOCKER | **STALE** | pattern-008 (reviewer-on-older-version) | closed-by-truth-audit-falsification — v1.0.137 6-anchor canonical block + joint-fit conditional-null language already present |
| GRO-B2 (Shamir factor-6–12 amplitude) | BLOCKER | **FALSIFIED** | pattern-008 | closed-by-truth-audit-falsification — L142–146 already states "no likelihood-level exclusion without matched-footprint Ganalyzer reanalysis" |
| GRO-M1 (leakage-as-novel framing) | MAJOR | OPINION | pattern-012 (style-not-error) | deferred-genuine — bib NOTE already cites Hivon 2002 mode-coupling; framing is editorial |
| GRO-M2 (hierarchy pre-spec) | MAJOR | STALE | pattern-008 | closed-by-truth-audit-falsification — pre-spec note already in §5.1 |
| GRO-m1 (D4-TTA propagation) | minor | STALE | pattern-008 | closed-by-truth-audit-falsification — 1.21× derivation landed v1.0.136 §sec:tta |
| GRO-n1 (abstract defensive tone) | nit | OPINION | pattern-012 | deferred-genuine |
| GEM-M1 (D4-TTA hold-out 21.4% flip) | MAJOR | OUT-OF-SCOPE | pattern-014 (GPU-bound) | deferred-genuine — full-catalog D4-TTA is GPU-bound (already on remaining-work list per status.md L7) |
| GEM-M2 (contiguous-patch test for canonical +3.64σ) | MAJOR | OPINION | pattern-009 (additional-test-request) | deferred-genuine — 6-anchor block already sufficient; this is a 7th-anchor ask |
| GEM-m1 (dipole-pattern wording) | minor | OPINION | pattern-012 | deferred-genuine |
| GEM-m2 (bootstrap framing) | minor | OPINION | pattern-012 | deferred-genuine |
| GPT-B1 (vague leakage method) | BLOCKER | **FALSIFIED** | pattern-008, pattern-017 (reviewer-skim-error) | closed-by-truth-audit-falsification — §V.D 10pp full quantitative methodology present + cited from abstract |
| GPT-M1 (GZ1-bias attribution weak) | MAJOR | FALSIFIED | pattern-008 | closed-by-truth-audit-falsification — Hayes 2017 winding-bias cite + alternative discussion present |
| GPT-M2 (0.43σ "overclaim") | MAJOR | FALSIFIED | pattern-017 | closed-by-truth-audit-falsification — paper explicitly says "consistent with null" everywhere |
| GPT-M3 (BHS detail) | MAJOR | FALSIFIED | pattern-017 | closed-by-truth-audit-falsification — Table II + §IV.B 8-test enumeration present |
| GPT-M4 (sys floor quantification) | MAJOR | STALE | pattern-008 | closed-by-truth-audit-falsification — systematic budget table present |
| GPT-N1 (parity terminology) | nit | OPINION | pattern-012 | deferred-genuine |
| PER-B1 (Shamir 2012 sample size 10⁴) | BLOCKER | **VERIFIED** | pattern-003 (numerical-claim-vs-source) | **closed-by-real-action** — L128 corrected 10⁴ → 1.27×10⁵ (126,501; WebFetch arXiv:1207.5464 abstract) in v1.0.149 |
| PER-M1 (Motloch fused metadata) | MAJOR | FALSIFIED | pattern-006 (citation-misread) | closed-by-truth-audit-falsification — bib L4456 correctly has 4 authors (Motloch, Yu, Pen, Xie) matching arXiv:2003.04800; §heading "Motloch & Pen" is conventional shorthand only |
| PER-M2 (Shamir 2022 1.3M parent vs spiral) | MAJOR | **VERIFIED** | pattern-003 | **closed-by-real-action** — L134 corrected "1.3M input reduced to 2×10⁵ spiral" → quote-exact "nearly 1.3×10⁶ spiral galaxies" matching Shamir abstract; pre-cut parent size note added (WebFetch arXiv:2208.13866 abstract) in v1.0.149 |
| PER-m1 (Yu:2020 transfer-function framing) | minor | OPINION | pattern-012 | deferred-genuine — already says "future work" elsewhere |
| PER-m2 (SpArcFiRe 140k provenance) | minor | OPINION | pattern-006 | deferred-genuine — paper attribution to Hayes-Davis DR9 update already present in L2714 |
| PER-n1 (Iye in-prep dangling) | nit | OPINION | pattern-012 | deferred-genuine |

---

## Closure tally

- **Real-action closures**: 2 (PER-B1 Shamir 2012 numerical correction; PER-M2 Shamir 2022 quote-fidelity)
- **Truth-audit falsifications**: 10 (3 Grok, 5 GPT, 1 Perplexity, 1 Gemini implicit)
- **Genuine deferrals (OPINION/GPU-bound)**: 10

**Net new actionable BLOCKERs**: 1 (Perplexity B1, closed in v1.0.149)
**Net new actionable MAJORs**: 1 (Perplexity M2, closed in v1.0.149)
**Stands findings**: 20 — all OPINION-tier polish, GPU-bound (Gemini-M1 D4-TTA), or stale (reviewers on pre-v1.0.137 mental model)

---

## Cascade counter advance

This is the second round in the post-Motloch-arXiv-ID / post-Jia / post-significance cascade. Previous round (counter 1/3) closed Motloch arXiv ID + Jia metadata + significance wording. This round (now **2/3**) closes 2 verified citation-numerical errors (Shamir 2012 sample size, Shamir 2022 1.3M quote-fidelity) that survived all prior rounds because no reviewer previously cross-checked the abstracts against the prose claims.

3-of-5 vendor convergent-silence target: NOT YET (Perplexity returned 2 verified-MAJOR + 1 verified-MINOR; need clean Perplexity in next round before exit). Next round will be counter 3/3.

---

## Gemini signal

**Gemini-2.5-Pro is the cleanest reviewer this round**: 0 BLOCKERs, 2 MAJOR (D4-TTA hold-out + canonical contiguous-patch test) + 2 minor polish. Both MAJORs are genuine 7th-anchor / extra-test requests, not falsifications of existing material. Opens its review with "No blocker-grade findings. The paper is exceptionally thorough." This is the strongest standalone Gemini endorsement P4 has received across all R-rounds; it tracks the cascaded-loop-exit signal (P4 has had 6+ consecutive 5/5 PERFECTLY CLEAN R-rounds prior to v1.0.148).

**Cosmology-physics persona consensus**: scope-boundary language and consistency-relation framing are now defensible per Gemini's specific review brief. No "mechanism-independent" overclaim flag. No parity-violation/ALP/Chern-Simons mis-reference flag.

---

## Convex / SSOT actions deferred

Per Houston's "no commit" instruction this turn — Convex bigbounce MCP closure mutations, SSOT/paper-4/status.md update, and site sync will be bundled in next commit. PDF mirrored byte-identical to all 3 hosting paths (md5 7cbbf34ac600b2c882ac5d95132c4a43).
