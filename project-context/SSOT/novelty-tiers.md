# Novelty Tiers — Canonical Definitions

**Status:** canonical. Every paper, every site surface, every Convex `papers.novelty` field, every science-highlight tag must use exactly these definitions.

**Standing directive (2026-06-03):** No Bigbounce / Hubify paper may self-claim **N4**. The ceiling for self-claims is **N3**. N4 is reserved for outside arbiters (Nobel committees, broad community consensus, decades of replication) to award. See `~/.claude/projects/-Users-houstongolden-Desktop-CODE-2025-bigbounce/memory/feedback_never_claim_n4.md` for the full rationale and the `/never-claim-n4` skill that enforces this mechanically.

---

## Tier table

| Tier | Name | What it means | Self-claim allowed? |
|------|------|---------------|---------------------|
| **N0** | Replication | Standard reproduction of prior work with our pipeline. Useful for verification, doesn't open new ground. | Yes |
| **N1** | Incremental refinement | Tightens an existing measurement, fixes a known bias, reproduces a prior result with a new dataset, or systematizes a known audit. | Yes |
| **N2** | Novel combination / extension | Applies an existing method to a regime it hasn't seen, OR combines two known methods so the joint result is meaningfully tighter or broader than either alone. | Yes |
| **N3** | First-of-kind demonstration | First σ-level constraint on a previously-untested signature; first end-to-end pipeline for a new survey; first systematic audit of a known systematic; first negative result strong enough to falsify a sub-class of models; first new methodology with no prior analog in the literature. **Ceiling for our self-claims.** | Yes — this is the ceiling |
| **N4** | Paradigm-shifting / consensus-breaking | Forces the field to abandon a leading model OR establishes a new one. Nobel-worthy. Awarded by the field over time. | **NEVER self-claim.** |

---

## Approved N3 supporting phrases

When a paper claims N3, the abstract / introduction / contribution-summary must use at least one of these phrases (or an exact synonym) to justify the tier:

- "first systematic …"
- "first end-to-end …"
- "first σ-level …" / "first sigma-level …"
- "first demonstration of …"
- "first constraint on …"
- "first negative test of …"
- "new methodology for …"
- "first-of-kind …"
- "first proof that …"
- "first published …"

If a paper labels itself N3 but uses none of these phrases anywhere in the body, either upgrade the phrasing or downgrade the tier. Audit on every version bump.

## Forbidden phrasing (self-claim leakage to N4)

Never use any of the following in our own authored copy (paper body, abstract, site copy, blog post, social):

- "Nobel-worthy"
- "paradigm-shifting" / "paradigm shift"
- "consensus-breaking"
- "rewrites cosmology" / "rewrites the standard model"
- "overthrows ΛCDM" / "overthrows inflation"
- "definitively settles"
- "first ever" (use "first" or "first-of-kind" — they're stronger because they're survivable under reviewer pushback)

External press / coverage / downstream citations may use these phrases. We do not.

---

## How this doc gets used

1. **Every paper version bump** — `/never-claim-n4` skill greps the paper .tex + papers.ts + live-status.ts + Convex `papers.novelty` for any N4 string or forbidden phrasing. Any hit triggers automatic demotion to N3 in the same atomic bump.
2. **Every new draft** — the novelty section must reference this doc and pick a tier ≤ N3 explicitly.
3. **Every R-round / external review** — if a reviewer says we're "implicitly claiming N4 impact," treat as a real finding and soften the language.
4. **Every site copy edit** — same forbidden-phrasing audit. The site is the most-read surface; an N4 leak here is the worst.

---

## Cross-references

- `~/.claude/projects/-Users-houstongolden-Desktop-CODE-2025-bigbounce/memory/feedback_never_claim_n4.md` — the standing directive itself
- `/never-claim-n4` — the mechanical-audit skill (Houston-mandated gate on every bump)
- `/paper-pre-review-check` — includes novelty-tier check as one of its passes
- `/bigbounce-post-bump-sync` — invokes the novelty-tier audit during the post-bump full-surface sweep
- `project-context/paper1_science_highlights.md` … `paper4_science_highlights.md` — per-paper contribution tables tagged with N-tiers
- `project-context/SSOT/paper-N/status.md` — per-paper readiness with novelty summary line

---

*Created 2026-06-03 in response to the `/never-claim-n4` audit pass. No prior canonical doc existed; this file is now the source of truth.*
