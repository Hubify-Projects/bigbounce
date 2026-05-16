# P5 config

`p5_config.yaml` is the **single source of truth** for every P5 run. Every
script accepts `--config` and reads exclusively from this file.

When you change a semantic parameter (radius, filter, threshold), bump
`version` so output sidecars carry the new tag. Reproducibility scripts hash
the config and store the hash in every output's provenance sidecar.
