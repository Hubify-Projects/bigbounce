# P5 Cross-match Diagnostics

_Generated from `p5_matched_chirality_desi.parquet`._  
Config version: **0.1.0** (hash `83970171f71bb863`)  

## Top-level counts

```json
{
  "desi_input_rows": 16361731,
  "matched_primary": 2349908,
  "matched_primary_deduped": 2232212
}
```

## Chirality among matched spirals

```json
{
  "n_cw": 393592,
  "n_ccw": 398043,
  "n_spirals": 791635,
  "cw_fraction": 0.4971887296544493,
  "binomial_sigma_from_half": -5.002592189664475
}
```

## Schema

| Column | Dtype | Non-null | Example |
|--------|-------|----------|---------|
| `desi_targetid` | int64 | 16,361,731 | `39628473198710603` |
| `desi_ra` | float64 | 16,361,731 | `23.764862479118218` |
| `desi_dec` | float64 | 16,361,731 | `29.832378962505196` |
| `desi_z` | float64 | 16,361,731 | `0.8042057637744875` |
| `desi_zerr` | float64 | 16,361,731 | `9.589004434794145e-06` |
| `desi_zwarn` | int64 | 16,361,731 | `0` |
| `desi_spectype` | object | 16,361,731 | `GALAXY` |
| `desi_subtype` | object | 1,695,998 | `b'HIZ'` |
| `desi_desi_target` | int64 | 16,361,731 | `0` |
| `desi_bgs_target` | int64 | 16,361,731 | `0` |
| `desi_program` | object | 16,361,731 | `other` |
| `desi_survey` | object | 16,361,731 | `cmx` |
| `desi_healpix` | int32 | 16,361,731 | `2152` |
| `desi_morphtype` | object | 15,976,322 | `EXP` |
| `match_dr8_id` | object | 16,361,731 | `494512_4597` |
| `match_ra` | float64 | 16,361,731 | `23.76619883339166` |
| `match_dec` | float64 | 16,361,731 | `29.840359893113014` |
| `match_class_eq` | object | 16,361,731 | `CCW` |
| `match_p_cw` | float64 | 16,361,731 | `0.4918863773345947` |
| `match_p_ccw` | float64 | 16,361,731 | `0.5079857707023621` |
| `match_p_ns` | float64 | 16,361,731 | `0.00012789257743861526` |
| `match_confidence_eq` | float64 | 16,361,731 | `0.5079857707023621` |
| `match_imaging_leg` | object | 16,361,731 | `DECaLS` |
| `sep_arcsec` | float64 | 16,361,731 | `29.03284386911637` |
| `matched_primary` | bool | 16,361,731 | `False` |
| `matched_0.5arcsec` | bool | 16,361,731 | `False` |
| `matched_1.0arcsec` | bool | 16,361,731 | `False` |
| `matched_2.0arcsec` | bool | 16,361,731 | `False` |
| `matched_3.0arcsec` | bool | 16,361,731 | `False` |
| `matched_5.0arcsec` | bool | 16,361,731 | `False` |
| `match_confidence` | float64 | 16,361,731 | `0.5079857707023621` |
| `matched_primary_deduped` | bool | 16,361,731 | `False` |

## Sensitivity (matches at alternate radii)

| Radius (arcsec) | Matches |
|---:|---:|
| 0.5 | 2,337,849 |
| 1.0 | 2,349,908 |
| 2.0 | 2,365,167 |
| 3.0 | 2,390,252 |
| 5.0 | 2,439,418 |

## Provenance pointer

Sidecar: `p5_matched_chirality_desi.parquet.provenance.json`