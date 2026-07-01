# Leveraging Claude Science for BigBounce

**Created:** 2026-07-01
**Status:** Working plan. Companion to the AI-for-Science credits application in this directory.
**Stance (from Hubify SSOT `MOAT_ADVERSARIAL_REVIEW.md`):** Claude Science is **execution substrate**, not a competitor. Let it run the coordinating agent, connectors, and HPC jobs; BigBounce keeps the cross-vendor adversarial review + provenance discipline on top.

---

## 1. What Claude Science is (relevant facts)

Anthropic's AI workbench for scientists, beta since 2026-06-30 (macOS/Linux; Pro/Max/Team/Enterprise):

- Generalist coordinating agent that spawns sub-agents + user-authored specialist agents.
- 60+ optional databases/connectors + skills (life-sciences first: genomics, single-cell, proteomics, structural biology, cheminformatics).
- Native artifact rendering (protein structures, genome tracks, chemistry drawings).
- **Auditable provenance** — every artifact traces to the code that produced it.
- Runs locally **or over SSH / HPC login node**, and can burst to **Modal** — one GPU to hundreds; review/revoke any job before submission.

## 2. Why it maps almost 1:1 onto how BigBounce already operates

| BigBounce practice (today) | Claude Science equivalent |
|----------------------------|---------------------------|
| RunPod pods over SSH (`compute-queue.md`), tmux jobs, H200/A4000 | Native SSH/HPC login-node execution + Modal burst |
| `/houston-method-v2` QC→analyze→expand→backup; scistack skills | Coordinating agent + user specialist agents |
| `/backup-3plus`, per-round PDF hygiene, `reviewTimeline` provenance | Auditable artifact→code history |
| Convex-is-live-site, artifact-link-verify | Provenance + reproducible outputs |

We are not adopting a new paradigm — we are moving a workflow we already run manually onto a supported substrate, and **reclaiming the substrate work** (pod babysitting, job submission plumbing) as agent-managed.

## 3. The gap Claude Science does NOT close (and why it's our wedge)

The 60+ connectors are **life-sciences**. There is **no cosmology/astro data layer** — no DESI, SDSS, LAMOST, Gaia, eROSITA, Planck/ACT CMB, or galaxy-catalog connectors. BigBounce's pipelines (P3 anomaly engine, P4/P5 chirality catalogs, P1/P2 f_NL + NaMaster MASTER) all bring their own domain data plumbing.

**Implication:** BigBounce gets Claude Science's *compute + provenance + orchestration* value immediately, but supplies its own astro data. That gap is exactly the Hubify wedge (own the hard-science domains Anthropic skipped) — and it is worth authoring reusable BigBounce **specialist agents / skills** for the astro surveys as the first content of that layer.

## 4. Integration plan (concrete)

**Phase 0 — Trial (this week, no credits needed).** Run one real BigBounce task inside Claude Science on an existing Pro/Max seat to feel the substrate boundary:
- Candidate: reproduce a P4 chirality provenance run (C2/C3 NaMaster MC), which is CPU-bound and already scripted (`h200_scripts/experiments/`). Confirm the artifact→code provenance survives round-trip and matches our `canonical_provenance/*.json`.
- Deliverable: a one-page "where Claude Science ends and BigBounce discipline begins" note appended here.

**Phase 1 — Wrap existing pipelines as specialist agents.** Author Claude Science specialist agents for: (a) NaMaster/MASTER MC forecasts, (b) anomaly-engine survey retrains (SDSS/LAMOST/CMB native, per `drive-to-100.md` Path C), (c) Cobaya/MCMC chain runs. Each wraps an existing script + our QC gates.

**Phase 2 — Keep the adversarial review layer OUTSIDE.** Claude Science is single-vendor; our cross-vendor R-rounds, `/peer-review-truth-audit`, `/review-integrity-audit`, and external browser review stay in scistack, running *on* the artifacts Claude Science produces. This is the moat — do not collapse it into the single-vendor coordinating agent.

**Phase 3 — Author the astro connector/skill set** as the first hard-science domain layer (the Hubify wedge). Publishable as reusable BigBounce skills.

## 5. Non-negotiables carried over

- Provenance parity: Claude Science artifact history must reconcile with our `canonical_provenance/` + `reviewTimeline.ts`. Do not trust one source (Directive E: ALWAYS-backup to local + HF + B2).
- No single-vendor convergence: a paper never closes on Claude Science's coordinating agent alone — cross-vendor + external + integrity audit still gate (Directives B, F).
- Every round still adds a `reviewTimeline.ts` entry (STANDING directive); a Claude Science skill-adoption is a `kind:"skill-improvement"` entry.

## Sources

- Anthropic — Claude Science announcement (2026-06-30): https://www.anthropic.com/news/claude-science-ai-workbench
- Product page: https://claude.com/product/claude-science
