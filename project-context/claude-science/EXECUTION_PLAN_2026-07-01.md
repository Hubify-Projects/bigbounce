# Execution Plan (BigBounce mirror) — Claude Science Response

**Created:** 2026-07-01
**Full plan:** hubify repo, `project-context/SSOT/EXECUTION_PLAN_2026-07-01.md` (canonical — cross-repo master).
**Thesis:** hubify repo, `project-context/SSOT/MOAT_ADVERSARIAL_REVIEW.md`.
**Directives (verbatim):** `../prompt-history.md` (2026-07-01 entries H1–H9) — note this file is **gitignored by repo convention** (local-only brain dumps); the durable committed copy lives in the private hubify repo at `project-context/prompt-history-claude-science-2026-07-01.md`.
**Companions here:** `INTEGRATION_PLAN.md` · `AI_FOR_SCIENCE_APPLICATION.md`.

---

## Houston's intent (summary)

Claude Science (launched 2026-06-30) is validation, not a threat: use it as **execution substrate** ("proven, better, new"), and double down on BigBounce/Hubify's real moat — the **model- and harness-agnostic, multi-vendor adversarial peer review + self-improvement loop** (internal AND external), which matters more in scientific research than any other domain. Framing ratified verbatim by Houston on 2026-07-01.

## BigBounce ledger — done this session (PR #1)

| Item | Status |
|------|--------|
| `INTEGRATION_PLAN.md` — phased Claude Science leverage (trial → wrap pipelines as specialist agents → keep adversarial review outside the single-vendor runner → author astro skills); maps RunPod/SSH/scistack onto Claude Science HPC/Modal + provenance; names the missing cosmology/astro connector layer as the wedge | ✅ committed + pushed |
| `AI_FOR_SCIENCE_APPLICATION.md` — up-to-$30k credits draft, grounded in real artifacts (six papers, NaMaster MC, Path-C retrains, Cobaya MCMC, Fisher forecasts); honest eligibility caveat; pre-submission checklist; **deadline 2026-07-15** | ✅ committed + pushed |
| README peer-review section — moat framing + real errors the loop caught (overlap-inflated σ, mislabeled catalog tier) | ✅ committed + pushed |
| `prompt-history.md` — session directives verbatim | ✅ this bundle |

(Hubify-side ledger — SSOT canon, homepage redesign + interactive ReviewConsole, /features, README, docs, skills/scaffold upgrades, all verified and deployed green — lives in the canonical plan.)

## BigBounce-relevant forward workstreams

| WS | What | Owner | Notes |
|----|------|-------|-------|
| **WS-1** | **AI-for-Science credits — deadline 2026-07-15** | Agent prep → **Houston submits** | Verify eligibility track for independent researchers; refresh numbers vs live `SSOT/index.md`; tighten to form limits; attach site/GitHub/PDF//reviews links |
| **WS-3.1** | Claude Science Phase-0 trial: reproduce P4 C2/C3 NaMaster provenance run inside Claude Science; write the substrate-boundary note | **Houston** (seat) + Agent | Candidate scripts: `h200_scripts/experiments/` |
| **WS-3.2** | Wrap NaMaster MC / anomaly-engine native retrains / Cobaya MCMC as Claude Science specialist agents (each wrapping existing scripts + QC gates) | Agent | Non-negotiables carried over: `/backup-3plus`, provenance parity, review layer stays outside |
| **WS-4** | Astro connector/skill layer (DESI/SDSS/LAMOST/Gaia/CMB), seeded from BigBounce pipelines — the domain layer Claude Science omits | Agent | Publishable; first content of the Hubify hard-science wedge |
| **WS-5.2** | Surface the adversarial-review timeline on bigbounce.hubify.app as the public case-study exhibit | Agent | Real review rounds only — follow `/bigbounce-site-sync` + Convex directives (A, G) when it's an actual round |

## Standing constraints (unchanged)

- Adversarial review **never** collapses into a single-vendor coordinating agent (Directives B, F).
- No fabricated results, submissions, or affiliations; eligibility caveat stays until verified.
- This doc is a plan, not a review round — no `reviewTimeline.ts` entry required. Any future round that lands from these workstreams follows the standing site-sync/Convex/PDF-hygiene gates in CLAUDE.md.
