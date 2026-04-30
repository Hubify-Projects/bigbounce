# R42 Wave 2/3 Pod Inventory (live, 2026-04-30)

## Active (4× H200, ~$15.36/hr → ~25.5h headroom on $392 budget)

| Pod | GPU | $/hr | Status | SSH | Job |
|---|---|---|---|---|---|
| `r42-b10-ood` `cqlrp2iko5tk8t` | H200 NVL | $3.39 | RUNNING | `root@154.54.101.58 -p 11637` | B10 P3 100k OOD inference |
| `r42-pod-b` `b5o3od0k592067` | H200 SXM | $3.99 | RUNNING | `root@103.196.86.10 -p 55951` | P4 cached-logit reanalysis (B19+B20+B21) |
| `r42-pod-c` `bsr1burbl2me11` | H200 SXM | $3.99 | RUNNING | `root@213.181.111.130 -p 17385` | B6 chain rerun + P2 sympy (B8+B9) |
| `regular_green_pig-migration` `kfmtdje25y88tf` | H200 SXM | $3.99 | RUNNING | `root@38.80.152.148 -p 33089` | NaMaster MCMC repro + P4 systematics (M14/M15/M17/M18/M19) |

## Paused / EXITED ($0/hr, host-saturated, retry queue)

- `blonde_silver_eel` `rx4x18p7v4gz66` — H200 SXM
- `frail_tomato_koi` `1detyybywd556o` — H200 SXM
- `regular_green_pig` `xzgst22n006n0g` — H200 SXM (orig host; manually migrated by Houston to `kfmtdje25y88tf`)

## Operating discipline (Houston directive 2026-04-30)

1. **PAUSE pods when not needed.** As soon as a workload completes and results are written + scp'd back + verified on disk, pause the pod via `podStop` to drop $/hr to $0 (volume preserved).
2. **Full backup before pause.** Every active pod's `/workspace/r42_pod_*_outputs/` must be rsync'd into `/Users/houstongolden/Desktop/CODE_2025/bigbounce/r42_outputs/` on this Mac AND mirrored to the external backup drive before `podStop`.
3. **Burn audit at every fire.** If a pod is RUNNING but not actively computing (idle GPU on `nvidia-smi`), pause it.
4. **Don't auto-resume paused-on-saturated-host pods.** They will fail with "not enough free GPUs"; Houston will migrate manually if extra capacity is needed.
