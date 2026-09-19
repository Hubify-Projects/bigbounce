| Tier | Name | Selection rule | $N$ | Next test |
|---|---|---|---|---|
| FT-A | High-redshift spectroscopic candidates | `SIMBAD/NED-unmatched AND ZWARN == 0 AND z >= 4.0` | 4 | Legacy Survey DR10 grz + WISE forced photometry cutouts at the listed coordinates; DESI DR2 repeat/coadd spectra where the tile is revisited; confirmation spectroscopy (Keck/LRIS, Gemini/GMOS, or SALT/RSS) for any target whose imaging is consistent with the pipeline redshift |
| FT-B | Infrared-excess AGN candidates | `SIMBAD/NED-unmatched AND AllWISE match AND W1-W2 >= 0.8 mag` | 1 | public NEOWISE-R single-exposure light curves for mid-IR variability; ZTF DR optical light curves; archival X-ray coverage (eROSITA-DE DR1, Chandra/XMM serendipitous catalogues) at the listed coordinates |
| FT-C | Reliable-redshift extreme-score candidates | `SIMBAD/NED-unmatched AND ZWARN == 0 AND DELTACHI2 > 25 AND anomaly_score in the top 5% of the released sample` | 5 | visual inspection of the public DESI DR1 coadd spectrum; re-fit with Redrock using the full template set; SDSS DR17 spectra where the footprint overlaps |
| FT-D | Point-source / stellar-locus candidates | `SIMBAD/NED-unmatched AND MORPHTYPE == 'PSF' AND a Gaia DR3 counterpart (GAIA_PHOT_G_MEAN_MAG > 0)` | 0 | Gaia DR3 parallax and proper motion at the listed source_id position; ZTF/ATLAS public light curves for variability; SDSS/LAMOST archival spectra where available |
| FT-E | Taxonomy-spanning representative set | `the highest-anomaly-score member of each of the 25 taxonomy clusters` | 25 | public DESI DR1 coadd spectrum inspection for each representative, plus Legacy Survey DR10 imaging cutouts; any representative whose spectrum is not explained by a known template is escalated to FT-A/FT-B/FT-C handling |

| Tier | TARGETID | R.A. (deg) | Dec. (deg) | Score | $z$ | ZWARN | SPECTYPE | $W1-W2$ | Family/cluster |
|---|---|---|---|---|---|---|---|---|---|
| FT-A | 39627903570285763 | 247.89529 | 4.66991 | 3.496 | 6.0878 | 0 | QSO | — | 0/19 |
| FT-A | 39627607293039577 | 201.10137 | -7.55334 | 3.232 | 6.0638 | 0 | QSO | — | 4/18 |
| FT-A | 39628216868014338 | 239.92839 | 18.01577 | 3.061 | 5.1938 | 0 | QSO | — | 0/20 |
| FT-A | 39627849358909321 | 252.47160 | 2.60073 | 3.033 | 4.3338 | 0 | QSO | — | 0/19 |
| FT-B | 103610381762578 | 223.91434 | 50.21732 | 3.105 | 1.1154 | 4 | GALAXY | 0.822 | 5/24 |
| FT-C | 39627812453222421 | 212.59529 | 0.92095 | 7.151 | 1.0798 | 0 | GALAXY | — | 3/9 |
| FT-C | 39627812461610773 | 213.07783 | 0.96584 | 6.394 | 1.1868 | 0 | GALAXY | — | 3/9 |
| FT-C | 39627877817258319 | 149.92219 | 3.77396 | 6.180 | 1.1989 | 0 | GALAXY | — | 3/9 |
| FT-C | 39633001079899014 | 217.98717 | 36.00150 | 4.747 | 1.3533 | 0 | GALAXY | — | 3/9 |
| FT-C | 39633407088529181 | 97.49930 | 61.65664 | 4.642 | 1.3098 | 0 | GALAXY | — | 6/8 |
| FT-E | 39627812453222421 | 212.59529 | 0.92095 | 7.151 | 1.0798 | 0 | GALAXY | — | 3/9 |
| FT-E | 39633407088529181 | 97.49930 | 61.65664 | 4.642 | 1.3098 | 0 | GALAXY | — | 6/8 |
| FT-E | 39636182677589446 | 64.05184 | -16.74091 | 4.321 | 0.0063 | 0 | GALAXY | — | 0/0 |
| FT-E | 1071051379310604 | 240.34378 | 42.49037 | 4.289 | 0.5392 | 4 | GALAXY | — | 2/12 |
| FT-E | 39627748041295714 | 333.31949 | -1.73961 | 4.252 | 1.4203 | 0 | GALAXY | — | 1/1 |
| FT-E | 39628291237221824 | 260.29164 | 21.13162 | 4.108 | 0.4073 | 4 | GALAXY | — | 7/11 |
| FT-E | 39633396858619848 | 275.81585 | 60.77425 | 3.877 | 2.6193 | 4 | QSO | — | 1/21 |
| FT-E | 1070259272417281 | 210.20609 | 6.12193 | 3.762 | 0.8731 | 4 | GALAXY | — | 2/10 |
| FT-E | 1070185960177669 | 150.13551 | 2.91550 | 3.498 | 0.8218 | 4 | GALAXY | — | 1/6 |
| FT-E | 39627903570285763 | 247.89529 | 4.66991 | 3.496 | 6.0878 | 0 | QSO | — | 0/19 |
| FT-E | 67803973419009 | 130.11975 | 18.65811 | 3.491 | 1.5393 | 4 | GALAXY | — | 0/15 |
| FT-E | 39633418778053415 | 143.59822 | 62.82238 | 3.416 | 1.3659 | 0 | GALAXY | — | 0/13 |
| FT-E | 39628330143583760 | 240.61454 | 22.94852 | 3.400 | 3.1050 | 0 | QSO | — | 0/20 |
| FT-E | 39633432057219468 | 96.54153 | 63.88652 | 3.387 | 0.9304 | 0 | GALAXY | — | 1/7 |
| FT-E | 39633495382820413 | 102.70638 | 70.64374 | 3.334 | 0.4730 | 4 | GALAXY | — | 0/14 |
| FT-E | 39633466035275117 | 293.95821 | 67.33832 | 3.330 | 1.4545 | 0 | GALAXY | — | 0/22 |
| FT-E | 39627817989705740 | 182.69435 | 1.34328 | 3.325 | 1.2954 | 0 | GALAXY | — | 0/17 |
| FT-E | 2394988512018434 | 203.98955 | 49.98956 | 3.295 | 0.5645 | 4 | GALAXY | — | 5/24 |
| FT-E | 39633062929108448 | 182.23513 | 39.17878 | 3.279 | 0.2303 | 0 | GALAXY | — | 5/4 |
| FT-E | 39632946235181990 | 213.68195 | 33.19121 | 3.278 | 0.7249 | 4 | GALAXY | — | 0/23 |
| FT-E | 1070090426515458 | 215.89907 | -1.05994 | 3.247 | 1.4127 | 4 | GALAXY | — | 4/18 |
| FT-E | 39627778101872111 | 325.03381 | -0.42236 | 3.220 | 1.0189 | 0 | GALAXY | — | 0/2 |
| FT-E | 2394624320602116 | 188.48854 | 30.29515 | 3.216 | 1.1496 | 4 | GALAXY | — | 4/5 |
| FT-E | 39633184245159076 | 270.34970 | 45.93852 | 3.194 | 1.4010 | 0 | GALAXY | — | 0/3 |
| FT-E | 39627654445405293 | 147.36232 | -5.59562 | 3.158 | 1.2267 | 4 | GALAXY | — | 0/16 |
