# R-upgraded-round9 P1B — Synthesis

**Paper**: `arxiv/paper1b_mcmc_companion.tex` v1B.0.41
**Round**: 2026-06-03_R-upgraded-round9
**Counter**: 4/3 EXTENDED (Houston-mandated; standard exit was 3/3 at R7)
**Vendors**: gemini-2.5-pro, gpt-4o (fallback from gpt-5), grok-4, sonar-pro
**Findings total**: 21 (4 GEM, 6 GPT, 6 GRO, 6 PER, minus duplicates collapsed)

---

## Verdict distribution

| Verdict | Count | Notes |
|---------|-------|-------|
| VERIFIED (actionable) | 1 | GEM-m1 (L1211–1215 audit-trail prose) |
| VERIFIED-PARTIAL | 1 | GEM-B1 (real tension in "natural parameters" language — soft fix recommended) |
| STALE | 10 | Reflags of closed material (GPT-B2..B5, GRO-B5, PER-B5/B6, GEM-m2 partial) |
| FALSIFIED | 4 | PER-B1, PER-B2 (PR3/PR4 — pattern-013, 6th consecutive round); PER-B3 (ECTorsionDESI2025 — pattern-035, 6th); GRO-n1 |
| OPINION | 5 | GRO-B1, GRO-B2, GRO-M1, GRO-M2, GPT-B6, PER-B4 |
| OOS | 0 | — |

Pattern-013 (Perplexity PR3/PR4 reflag) and pattern-035 (Perplexity arxiv-id confab) BOTH fired again on PER-B1/B2/B3 — **6th consecutive round**. Auto-FALSIFY per standing rule. PER-B3 cites L569–573 which is BIB stub territory; the body already inlines full Liu et al. metadata via the references.bib entry. Pattern-013 caught 9/9 rounds total on P1B; should be promoted to "resolved at prevention layer" candidate in next pattern-mine pass.

Gemini produced the only actionable new finding this round (GEM-m1: real audit-trail prose at L1211–1215 — "We previously closed an earlier reported product…"). This is exactly the kind of body-prose reviewer-artifact leakage that pattern-014 / pattern-017 catch.

GEM-B1 ("natural parameters" vs ~25× tuning) is internally coherent — the paper DOES disclose the ~25× tuning at fn:theta_backreaction L1133–1146 and at L1191–1204, but uses "natural parameters" framing four times (L654, L1102, L1132, L1227). The fn:theta_backreaction makes clear "natural" refers to the SCAN PRIOR midpoint, not naturalness of the spectator-consistent corner. Soft fix (one-clause hedge at L654 + L1102 + L1227) is appropriate, NOT a blocker. Downgraded to MAJOR-soft.

GEM-M1 (ALP integration in LCDM not quintom-w₀wₐ background): OPINION — methodologically valid but quantitatively immaterial (paper already discloses <few-% Hubble-rate shift at z<1 in fn:wcaveat). Cost-benefit favors keeping LCDM integration with the existing disclosure.

GRO-B1/B2 (delete preamble + delete §6) are pattern-019 / pattern-022 reviewer overreach. Preamble is %-comments (arXiv-tarball stage strips, pattern-014). §6 already labeled "Not a distinctive ECH prediction" at L654 + L1102. GRO-M1 (frozen Table II caption) — already disclosed at GEM-n1 closure in v1B.0.41. GRO-M2 already disclosed at L1191–1204.

GRO-n1 (claim of remaining "R-upgraded-round" strings in body): inspection found 3 hits — L585 (footnote, intentional disambiguation citation), L1134 (footnote), L1485 (footnote). These are LEGITIMATE in-context disclosure footnotes per v1B.0.36 closure rationale, NOT leakage. FALSIFIED.

---

## Closure plan for v1B.0.42

**Real-action close** (1 finding):
1. **GEM-m1** — Strip audit-trail prose at L1211–1215: delete sentence "We previously closed an earlier reported product '$C_{a\gamma}\times\theta_i = 3.4\pm 1.1$' that confused $\theta_i$… by a factor of $\sim 3$." Replace with nothing or with a single ASCII footnote pointer if needed. Pattern-014 / pattern-017 closure.

**Optional polish** (1 partial-VERIFIED finding):
2. **GEM-B1** — Add hedge at L654: change "ALP having natural parameters" → "an ALP whose scan-prior midpoint values fit the signal (the spectator-consistent corner $\theta_i\!\sim\!0.1$ requires $\sim$25× tuning of the misalignment angle; see fn:theta_backreaction)." Mirror at L1102, L1227. Pattern-005 closure (overclaim language).

No version bump required for #1 alone (audit-trail strip is identical to historical pattern-014 fix and was already done for other inline reviewer codes in v1B.0.41 GEM-m1).

Recommend **v1B.0.42 patch bump** if both #1 and #2 land in the same commit.

---

## Exit criteria for cascade

R9 returns **zero novel BLOCKERs**, **zero novel MAJORs**, **1 real-action minor** (GEM-m1), **1 partial-VERIFIED MAJOR-soft** (GEM-B1 polish). All other findings are STALE reflags (pattern-016) or FALSIFIED (pattern-013/035 — 6th time). Pattern-013 + pattern-035 are now at "prevention-layer promotion" candidacy.

Cascade exit recommended after v1B.0.42 closure commit. The 4/3 EXTENDED counter is justified by the discovery of GEM-m1 (genuine new finding); without GEM-m1 the round would be a clean re-exit.
