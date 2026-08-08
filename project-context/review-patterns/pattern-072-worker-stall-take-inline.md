# Pattern 072 — Worker-agent stall storms: resume once, then take the work inline

**Class:** orchestration-reliability
**First observed:** 2026-07-22 site-fix batch (three consecutive Sonnet worker stalls, 600s watchdog)

## Observation
During API-turbulence windows, execution workers can stall repeatedly before
making ANY edit. Each stall costs 10 minutes of wall-clock. Three consecutive
stalls on the same well-specified batch is strong evidence the turbulence is
systemic, not task-specific.

## Rule
(1) On first stall: resume the same agent from its transcript (cheap, preserves
context). (2) On second stall of a FRESH agent on the same batch: stop
delegating — the orchestrator executes the batch inline. Verify with git status
which items landed before re-running anything. Never leave a half-applied batch
undiagnosed.
