# Future Papers — TBD Notes

_Created 2026-06-26. These are not scheduled commitments — they are ideas to capture
while the campaign data is fresh. Revisit after the 6-paper arXiv drop._

---

## Paper 7 — The Meta-Paper: Self-Improving Scientific Peer Review

### Working title ideas
- "A Self-Improving Internal/External Review Loop for Scientific Papers: Closing the Gap to Zero"
- "From 60 Misses to Zero: A Quantitative Study of an AI-Augmented Multi-Vendor Scientific Review Campaign"
- "Measuring the Internal/External Review Gap: A Campaign of 20+ Rounds Across Six Cosmology Papers"

### Thesis
A multi-vendor AI review loop — alternating internal (5-model API) and external (3-provider browser-tier)
rounds with mandatory truth-audits and per-finding gap tracking — can converge the internal/external
referee gap to **zero** within a bounded campaign (17–22 rounds observed here), while continuously
upgrading its own detection skill via a codified pattern catalog. This is a reproducible, measurable,
and improvable methodology for rigorous pre-submission scientific QA.

### What to measure / data sources

| Metric | Source |
|--------|--------|
| INT/EXT gap per round (# externally-only findings) | `site/src/data/reviewTimeline.ts` → `gapSeries` |
| Gap trajectory: 60 → 32 → 27 → … → 0 | `gapSeries[*].total` |
| Items-per-round trend (decreasing) | `gapSeries` + individual round `keyTakeaways` |
| Pattern catalog growth (34 → 44 → … → 64 patterns) | `skillsSeries[*].patterns` |
| Prompt-rules growth (14 → 19 → … → 24 rules) | `skillsSeries[*].promptRules` |
| Fabrication-class catch: R54 arithmetic regression (Eq.15 Cartan factor-2) | `project-context/review-patterns/pattern-053-closure-arithmetic-regression-audit.md` |
| Integrity audit result (2026-06-26): loop GENUINE, MILD self-bias, corrected | `project-context/peer-reviews/INTEGRITY_AUDIT_2026-06-26.md` |
| False-positive pattern catalog: patterns 052–064 | `project-context/review-patterns/pattern-052-*.md` … `pattern-064-*.md` |
| Readiness trajectory per paper (92 → 97 → 98) | `reviewTimeline.ts` → `readinessCheckpoints` |
| Total rounds: ~22 INT rounds + ~20 EXT browser rounds | `reviewRounds` array |

### Key claims to make (and how to verify)

1. **Gap reaches zero in bounded rounds** — not asymptotic, fully closable.
   - Verify: `gapSeries` shows 60 → 0 over EXT1–EXT17 (17 rounds to zero), with brief rebound
     after EXT18 (new subsection added post-freeze), then re-zero at EXT20.
2. **Internal tier is NOT sufficient alone** — EXT1 baseline = 60 external-only finds after 6 clean internal rounds.
   - Data: `gapSeries[0].total = 60`, `gapSeries[0].note`.
3. **Pattern catalog self-improvement is measurable and monotone** — 34 → 64 patterns, 14 → 24 prompt-rules.
   - Data: `skillsSeries`.
4. **False-positive rate is also measurable** — pattern-052 (re-raise vindication) + pattern-056 (pdftotext artifact)
   + pattern-064 (Grok harsh-outlier) quantify the false-positive burden; truth-audits separate signal from noise.
5. **Integrity audit shows loop is self-correcting** — mild self-bias caught by independent audit, corrected same session.
   - Data: `INTEGRITY_AUDIT_2026-06-26.md` + `INTEGRITY_CLOSURE_2026-06-26.md`.
6. **Round-to-zero is reproducible across paper types** — 6 different papers (cosmological perturbation theory,
   galaxy chirality, anomaly catalog, non-Gaussianity, DESI chirality) all converged.

### Narrative structure (draft)
1. Introduction — the internal/external gap problem in AI-augmented review
2. The method — INT/EXT cycle + truth-audit + per-finding gap tracking + pattern mine
3. Campaign data — 6 papers, ~22 INT + ~20 EXT rounds, 126 archived findings (R52 alone)
4. Gap trajectory — quantitative series, turning points, what drove rebounds
5. Pattern catalog — growth curve, false-positive classes, fabrication-catch event
6. Integrity audit — how to detect and correct self-favoring bias in a review loop
7. Discussion — limits, generalizability, cost (CC+gstack), comparison to human peer review
8. Conclusion — the gap can reach zero; the loop improves faster than the papers accumulate debt

### Venues to consider
- _The Astrophysical Journal Supplement Series_ (methods paper)
- _PLOS ONE_ (open methodology, broad audience)
- _arXiv:astro-ph.IM_ (instrument/methods section)
- A longer-form Hubify white-paper / technical report (no journal required)

---

## Follow-up Paper — Hubify Efficiency Case Study

### Working title ideas
- "Accelerating Scientific Publishing with a Self-Improving AI Review Stack: A Quantitative Case Study"
- "The Hubify Review Loop: Measuring Time-to-Publishable Across a Multi-Paper Campaign"
- "AI-Augmented Scientific QA at Scale: Efficiency, Cost, and Quality Metrics from the Big Bounce Campaign"

### Thesis
Quantify the **speed and efficiency gain** of the self-improving INT/EXT review loop vs. a counterfactual
human-only or first-pass AI review: how many rounds, wall-clock hours, and dollar-equivalent does it take
to go from "draft submitted" to "zero gap / 18/18 ACCEPT" using the Hubify review stack?
This is the marketing/methods paper for Hubify.com — the platform productizing this process.

### Hubify marketing angle
- **"From draft to publishable: quantified."** Show the gap-to-zero curve as a product deliverable.
- **Compression ratios**: human peer review timeline (months) vs. Hubify loop (days/weeks).
- **Reproducibility** across paper types — the loop works for cosmology, it will work for your field.
- **Integrity-first**: the 2026-06-26 audit demonstrates the loop self-corrects for bias — not just a speed tool.
- **Agentic-first**: every round is driven by skill-parameterized AI agents, not human time.

### Key metrics to track (collect now, before the data is stale)

| Metric | Notes |
|--------|-------|
| Wall-clock hours per round (INT vs EXT) | Capture per-round timePT fields in `reviewRounds` |
| Number of rounds to reach 18/18 ACCEPT | EXT17 = round 17 from EXT1 |
| Items-closed per round trend | Declining curve → loop efficiency increasing |
| Skill upgrades per round | `skillsSeries` growth |
| Total cost estimate (CC+gstack credits, RunPod compute) | Rough $ figure for the whole campaign |
| Fabrication-class catches prevented from reaching arXiv | Pattern-053 catch (R54 Eq.15), integrity audit 5 items |
| Gap-to-zero round count by paper complexity | P4 was fastest (frozen early); P1A slowest |
| Integrity-audit result (bias quantification) | 5/19 = ~26% mild self-favoring, fully corrected |

### Hubify productization framing
- The loop is the product: install `hubifystack`, configure vendors, run `/cross-vendor-r-round`
- The pattern catalog is the moat: 64 patterns encode everything the loop learned — each new project
  starts with a stronger prior than the previous one
- The gap chart is the deliverable: a published, auditable record of quality convergence
- The integrity-audit step is the trust layer: shows the system catches its own biases

### Data sources
- `site/src/data/reviewTimeline.ts` (full campaign record, machine-readable)
- `project-context/peer-reviews/` (verbatim round artifacts)
- `project-context/review-patterns/` (64-pattern catalog)
- `project-context/peer-reviews/INTEGRITY_AUDIT_2026-06-26.md`
- `~/.claude/scistack/astrostack/` (skill source files — show the skill-stack as product)
- Any RunPod cost logs / Claude Code session credit burn (rough estimate sufficient)

### Venue
- A Hubify.com technical blog post / white paper first (no peer-review gating needed for a methods/case-study)
- Then submit to a journals-methods venue (JOSS, PLOS ONE, or a science communication venue)
- Or as an invited talk / poster at an AI+science conference

---

_Both papers require the 6-paper arXiv drop to have happened first, so the campaign data is citable.
Revisit this file at arXiv drop + 2 weeks. Set a reminder in YouStack or Hubify tasks._
