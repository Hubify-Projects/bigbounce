# BigBounce agent instructions

Read these sources in order before acting:

1. `AGENTS.md`
2. `project-context/AGENT_ONBOARDING.md`
3. `CLAUDE.md`
4. `AGENT_RULES.md`
5. `ops/PLAN.md`
6. `project-context/SSOT/index.md`

Use `project-context/paper_registry.json` for paper identity and paths, then the
relevant per-paper SSOT status and revision evidence. Never infer truth from a
LaTeX comment or public site projection when it conflicts with the SSOT.

Truth-audit every review finding, preserve raw evidence, never fabricate an
acceptance or derivation, and keep SSOT/Convex/site changes atomic. Directive P
separates readiness from publishing: four agent gates total 95; only Houston's
explicit per-paper sign-off reaches 100.
