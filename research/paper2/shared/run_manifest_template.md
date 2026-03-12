# Run Manifest

## Run ID
- **run_id**: `<YYYYMMDD_HHMM>_<short_description>`
- **track**: <track name>
- **date**: <ISO 8601>
- **operator**: Houston Golden (automated via research pipeline)

## Repository State
- **commit**: `<git commit hash>`
- **branch**: `<branch name>`
- **config_hash**: `<sha256 of primary config file>`

## Environment
- **python**: `<version>`
- **key_packages**: see `pip_freeze.txt` in this directory
- **hardware**: <pod type, GPU/CPU, RAM>
- **pod_id**: <RunPod pod ID>

## Datasets Used
| Dataset | Version | Source | Hash |
|---------|---------|--------|------|
| <name>  | <ver>   | <url>  | <sha256> |

## Commands
```bash
# Exact commands to reproduce this run
<commands>
```

## Outputs
| File | Description | Hash |
|------|-------------|------|
| <path> | <description> | <sha256> |

## Notes
<any relevant notes, warnings, limitations>
