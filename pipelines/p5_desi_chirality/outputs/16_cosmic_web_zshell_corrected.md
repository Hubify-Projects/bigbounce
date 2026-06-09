# 16 — z-shell selection-corrected cosmic-web chirality test
_Generated 2026-06-09T18:36:11Z · pipeline runtime 102s · closes P5-META-E1/E2_

Shell scheme: dz=0.05 for z<0.5; dz=0.10 for 0.5<=z<1.5; merged 1.5-1.7 (21 shells, all >=216k galaxies).
Grid/smoothing/threshold identical to canonical: N=256, R_s=25.0 Mpc/h, lambda_th=0.0.
Per-shell mean density spans 294.05 (z=0.01-0.05) to 0.46 (z=1.5-1.7) gal/cell vs the single
global canonical mean of 4.64 — a factor-640 radial selection gradient
that the canonical classifier absorbed directly into delta.
Buffer cut: galaxies within 77 Mpc/h of the dilated-mask exterior (= within R_s of the occupancy-footprint boundary).

## Migration matrix (all 14.6M DESI galaxies; rows=canonical, cols=corrected)

| canonical \ corrected | void | wall | filament | cluster |
|---|---|---|---|---|
| void | 72,365 | 98,487 | 62,326 | 7,426 |
| wall | 108,083 | 736,040 | 741,749 | 35,586 |
| filament | 104,342 | 2,161,258 | 5,880,450 | 1,863,632 |
| cluster | 0 | 133,037 | 1,284,843 | 1,332,659 |

Row-normalized: void keeps 30.1%, wall 45.4%, filament 58.7%, cluster 48.5% of their canonical members.

## Canonical (recomputed; matches published Table values exactly)
| env | n | f_CW | sigma(0.5) | sigma(monopole) |
|---|---|---|---|---|
| void | 428 | 0.4836 | -0.68 | -0.56 |
| wall | 6,673 | 0.5034 | +0.55 | +1.01 |
| filament | 408,187 | 0.4980 | -2.61 | +0.99 |
| cluster | 397,505 | 0.4963 | -4.66 | -1.11 |
| ALL | 812,793 | 0.4972 | -5.07 | +0.00 |

## z-shell corrected
| env | n | f_CW | sigma(0.5) | sigma(monopole) |
|---|---|---|---|---|
| void | 4,353 | 0.4971 | -0.38 | -0.01 |
| wall | 154,541 | 0.4968 | -2.51 | -0.30 |
| filament | 472,547 | 0.4973 | -3.73 | +0.13 |
| cluster | 181,352 | 0.4973 | -2.33 | +0.07 |
| ALL | 812,793 | 0.4972 | -5.07 | +0.00 |

## z-shell corrected + interior buffer cut
| env | n | f_CW | sigma(0.5) | sigma(monopole) |
|---|---|---|---|---|
| void | 3,976 | 0.5003 | +0.03 | +0.39 |
| wall | 153,737 | 0.4968 | -2.53 | -0.33 |
| filament | 471,866 | 0.4973 | -3.74 | +0.11 |
| cluster | 181,352 | 0.4973 | -2.33 | +0.06 |
| ALL | 810,931 | 0.4972 | -5.06 | +0.00 |

## Verdict

(a) Class populations DO shift substantially: spiral-level void 428 -> 4,353 (10x), wall 6,673 -> 154,541 (23x),
filament 408,187 -> 472,547 (+16%), cluster 397,505 -> 181,352 (-54%). The canonical high-z 'void' excess and
cluster excess were selection artifacts, as the E1 finding predicted.

(b) The null conclusion HOLDS and is STRENGTHENED. Corrected per-class f_CW collapses to 0.4968-0.4973
(range 0.05 pp vs canonical 1.98 pp). Every class sits within |sigma| <= 0.33 of the sample monopole
(f_CW = 0.4972); with the buffer cut, |sigma| <= 0.39. Nothing approaches the >4-sigma-beyond-monopole
discovery threshold. The residual sigma_from_half values (-2.3 to -3.7) are pure P4 catalog-monopole
leakage, identical in interpretation to the published result.
