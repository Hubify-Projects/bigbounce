# Anomaly flagship assembly — 2026-09-18

Assembly of the anomaly flagship from the completed phase-3 v2 landing
(campaign criterion A7, `project-context/campaigns/CAMPAIGN_2026-09-18_publication_push.md`).
Ledger rows 6, 8 and 12 frame the scope: ledger #8 answered **data release**,
not discovery paper, so nothing here claims a discovery.

| File | What it is |
|---|---|
| `SELECTED_SAMPLE_DEFENSE.md` | why the clean v2 science-only $S>3$, $n=1{,}244$ sample is the manuscript's sample, with today's provenance re-run |
| `VALIDATION_CONTRACT.md` | 16 machine-checkable release requirements, their outcomes, and the three material results |
| `TAXONOMY_FAMILY_EVIDENCE.md` | the 8 families / 25 clusters with per-family evidence tables and their honest limits |
| `FOLLOWUP_TARGET_SET.md` | 32 named targets in 5 rules-based tiers + 5 open tests |
| `scripts/assemble_flagship_evidence.py` | computes everything above from the released artifacts (CPU, < 1 min, no network) |
| `scripts/make_tables.py` | renders the evidence into Markdown tables and revtex table bodies |
| `outputs/` | machine-readable results: provenance re-check, validation contract, family evidence, follow-up targets, zcatalog re-join repair table |
| `figures/` | score-vs-exposure-quality and per-family evidence figures |

The manuscript skeleton built on this evidence is
`pipelines/p1_highz_tracers/anomaly_flagship_draft/` (revtex4-2 +
reproducibility manifest).

Reproduce:

```sh
python3 pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/assemble_flagship_evidence.py
python3 pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/make_tables.py
```
