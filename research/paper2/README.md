# BigBounce Paper 2+ Research Program

Four parallel research tracks extending Paper 1 (Einstein-Cartan geometric dark energy).

## Tracks

| Track | Code | Goal | Pod Type |
|-------|------|------|----------|
| **WP4** | `wp4_dneff_microphysics/` | Explicit post-inflation ΔNeff mechanism | CPU |
| **WP5** | `wp5_spin_amplitude/` | First-principles A₀ spin dipole scaling | CPU |
| **P7** | `p7_cnn_spin_classifier/` | CNN galaxy spin classifier with bias audits | GPU |
| **P6** | `p6_cmb_eb_pipeline/` | Independent CMB EB birefringence pipeline | CPU/RAM |

## Rules

1. No changes to Paper 1 outputs or manuscript while these tracks run.
2. Every track produces: runnable pipeline, reproducible artifact pack, short writeup with citations.
3. Each run has MANIFEST.md with commit hash, dataset version, config hash, commands.
4. Pinned versions; environment specs stored.
5. Intermediate results saved frequently; nothing critical in /tmp.

## Shared Resources

- `shared/citations.bib` — Combined bibliography
- `shared/dataset_registry.csv` — All datasets with provenance
- `shared/run_manifest_template.md` — Template for run manifests
- `shared/env/` — Shared environment specifications
