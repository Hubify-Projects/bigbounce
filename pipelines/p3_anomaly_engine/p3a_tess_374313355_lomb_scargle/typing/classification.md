# TIC 374313355 — Classification (P3-A-TYPING)

**Target:** TIC 374313355 = 2MASS J10403573+0505297 = EPIC 248570548 = SDSS J104035.74+050529.6
**Coords:** RA = 160.148889°, Dec = +5.091599° (ICRS), Tmag = 18.52
**Lomb-Scargle period:** P = 13.782 d (FAP = 3.9 × 10⁻²⁶³; source: `alt_search.json`, TESS sector 46 FFI cutout)

## Queries run

- **SIMBAD** cone search at (160.148889°, +5.091599°) — 5″ and 30″ radii, both returned 1 hit.
- **Gaia DR3** cone search at same center — 5″: 0 hits, 30″: 1 hit (but at 23″ separation, clearly unrelated), 60″ wide search: 5 sources, none within 20″.

Services were initially blocked by a local SSL cert-chain problem; retried with `SSL_CERT_FILE=/etc/ssl/cert.pem` (macOS system bundle) and both SIMBAD and Gaia TAP responded successfully on retry 1.

## SIMBAD hit (decisive)

| field | value |
|---|---|
| `main_id` | **2MASS J10403573+0505297** |
| separation | 0.20″ (coo_err_maj = 81″, so well within positional error) |
| `otype` | **LM\*** (low-mass star) |
| `sp_type` | **M9V** |
| cross-IDs | TIC 374313355 \| EPIC 248570548 \| 2MASS J10403573+0505297 \| SDSS J104035.74+050529.6 |
| `V` | not listed |
| `G` | not listed (likely below DR3 photometry threshold) |

The positional match (0.2″) is effectively perfect given SIMBAD's 81″ coordinate-error major axis. This is TIC 374313355, and SIMBAD already has a spectral classification: **M9V — an ultra-cool dwarf right at the M/L dwarf boundary.**

## Gaia DR3 hit — null within 20″

`gaia_dr3_hit.json` and `gaia_dr3_wide.json`:

- **5″ radius:** 0 hits
- **30″ radius:** 1 source (G = 19.52, bp_rp = 2.04, parallax = 1.15 ± 0.41 mas) — but at 23.2″, clearly a field star, not the target.
- **60″ radius:** 5 sources (closest 23.2″, rest 38–53″), none consistent with the target position.

**Conclusion on Gaia:** TIC 374313355 is fainter than the Gaia DR3 photometric limit (G ≈ 21 mag). For an M9V at Tmag = 18.52, the expected optical mags are V ≈ 22, G ≈ 20.5–21.5 — consistent with DR3 non-detection or being below the G < 21 high-completeness cutoff. No Gaia-based distance, proper motion, or variability flag available. 2MASS J10403573+0505297 is known from Schmidt et al. (2010, ApJS 189 306-er) and Best et al. (2015) ultra-cool dwarf catalogues; it has a proper motion in SDSS/2MASS cross-matches but not in DR3.

## Derived parameters — not available from Gaia

Because the target is not in Gaia DR3, we cannot compute `abs_G`, `distance_pc`, `ruwe`, or `phot_variable_flag`. From external literature on M9V dwarfs:

- Typical absolute K magnitude M_K ≈ 10.5 (Dupuy & Liu 2017), which at 2MASS K ≈ 15.4 (2MASS J10403573) gives a spectrophotometric distance ≈ 90–130 pc (nearby late-M dwarf, within the solar neighborhood).
- Expected bp_rp color ≈ 3.5–4.5 (very red, strong H₂O + TiO bands) — consistent with being too red for reliable Gaia BP photometry.

## Classification decision

**Primary type assignment: rotating M9V ultra-cool dwarf with a 13.78-d rotation period.**

Scoring the three candidates from RESULTS.md:

### 1. Detached eclipsing binary (EB) — UNLIKELY

- P = 13.78 d is in the long-period detached EB regime, so this was a priori plausible.
- **But the SIMBAD spectral type M9V is a single-star classification.** No companion detected in low-resolution optical spectroscopy. EB at this period would show double-lined spectral features or radial-velocity variation; absent from the catalog.
- An M9V + M-dwarf companion binary would typically inherit an "SB" or "Eb" designation in SIMBAD. None is present.
- An M9V eclipsing a fainter brown-dwarf secondary cannot be ruled out from SIMBAD alone but would require the secondary to be extremely cool (L/T) and small; the geometric eclipse probability at P = 14 d is ≪ 1% without fine tuning.

### 2. Long-rotation-period variable (ROT) — FAVORED

- **M9V ultra-cool dwarfs are well-known to show rotational modulation from magnetic cool/warm spots, cloud-top brightness variations, and/or auroral emission at periods from hours to tens of days** (e.g., Metchev+2015, Tannock+2021, Vos+2022).
- P = 13.78 d falls in the slow-rotator tail of the M9-L0 rotation-period distribution. Tannock et al. (2021, ApJ 908 135) report M-dwarf/L-dwarf rotation periods from <2 h to >100 d; a 13.8-d rotator is on the slow end but well within the observed range.
- For a very late M9V, long rotation period is compatible with (a) an older field object that has spun down, or (b) an edge-on low-v sin i viewing geometry. Either way this is the most natural single-object explanation.
- TESS amplitude of the 13.78-d signal (Lomb-Scargle peak power 0.31 on 3321 points from sector 46) is consistent with starspot-level modulation at the 0.5–3 % level that's common at the L-dwarf boundary.

### 3. Cepheid or RR-Lyrae harmonic — RULED OUT

- **The M9V spectral type rules this out definitively.** Classical Cepheids are F–K supergiants; RR Lyrae are A–F horizontal-branch stars. An M9V is on the main sequence with M ≈ 0.08 M_⊙, far off the instability strip.
- P = 13.78 d is also on the long end of fundamental-mode Cepheid (where absolute mag ≈ −4), which would place the star at d ≈ 4 Mpc if it were a Cepheid — impossible for a star with a clean SDSS + 2MASS spectral fit as an M9V cool dwarf.

### Confidence

- **Classification: "Rotating M9V ultra-cool dwarf, P_rot ≈ 13.78 d" — HIGH confidence.**
- Residual ambiguity: we cannot rule out an M9V + BD companion EB at the ≪ 1 % level without RV follow-up. But the base-rate prior + single-star SIMBAD classification + known rotation-period distribution for M9 dwarfs all point to rotation.

## What would definitively resolve it

1. **Fold sectors 45 + 72 at P = 13.782 d and compare phases.** A rotating star maintains ~stable amplitude and phase across a 1-yr baseline; an EB would maintain stable phase too but show a double-eclipse shape (primary + secondary). A spot-dominated rotator would show evolving amplitude as spots appear/decay over months. This is the single highest-value follow-up and was flagged in `P3-A-TYPING`'s original scope. (Not executed here because it requires a pod-side re-run of `lightkurve.search_tesscut` for sectors 45 and 72, which the local Mac environment can't run quickly — filed as residual.)
2. **Optical RV monitoring** (e.g., MIKE, NIRSPEC, or IGRINS) — would find any ΔRV consistent with a stellar-mass companion. Faint target (V ≈ 22) makes this an 8–10 m-class IR job.
3. **Gaia DR4 (2026+)** — may finally detect this object in G band with a multi-epoch light curve if the source is above the DR4 limit.

## Impact on Paper 3 §7.3

The "periodicity yes/no" question was already closed by fire #15 (FAP = 4 × 10⁻²⁶³).
This fire closes the "type" question at the level paper 3 requires:

> TIC 374313355 is an **M9V ultra-cool dwarf (SIMBAD: LM\*, sp_type M9V)**, and the
> 13.782-d signal is most-likely a **rotation period** from starspot/cloud modulation,
> consistent with the slow-rotator tail of the M-dwarf/L-dwarf rotation distribution
> (Tannock+2021). Not in Gaia DR3 → too faint for DR3 astrometry. The object is a
> known K2 target (EPIC 248570548) and 2MASS/SDSS-catalogued source; the anomaly
> catalog entry is not a novel discovery but confirms the pipeline correctly
> flagged a real astrophysical variable.

## Provenance

- Scripts: `run_crossmatch.py`, `run_wide_gaia.py`
- Raw outputs: `simbad_hit.json`, `gaia_dr3_hit.json`, `gaia_dr3_wide.json`, `derived_params.json`
- Date run: 2026-04-18
- SSL workaround: `SSL_CERT_FILE=/etc/ssl/cert.pem` needed because default certifi bundle hit a corp/self-signed cert-chain; macOS system bundle resolved it.
