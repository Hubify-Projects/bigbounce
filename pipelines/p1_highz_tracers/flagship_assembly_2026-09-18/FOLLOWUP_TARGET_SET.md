# Named follow-up set and open tests

A candidate catalogue earns its place by being actionable. This file names the
objects to look at first, the test that would settle each one, and the public
data or instrument that supplies it — plus the open tests the catalogue itself
still needs. Selection rules were fixed from literature criteria (not tuned to
yield a target count) and are replayable by
`scripts/assemble_flagship_evidence.py`; the machine-readable set is
`outputs/followup_targets.{json,csv}`.

All tiers draw from the **675 SIMBAD/NED-unmatched** objects, i.e. the subset
with no catalogued counterpart within 3 arcsec. 32 distinct objects are named
across 35 tier rows (an object may appear in more than one tier).

## Tiers

| Tier | Name | Rule | $N$ |
|---|---|---|---|
| FT-A | High-redshift spectroscopic candidates | unmatched AND `ZWARN == 0` AND $z \ge 4.0$ | 4 |
| FT-B | Infrared-excess AGN candidates | unmatched AND AllWISE match AND $W1-W2 \ge 0.8$ | 1 |
| FT-C | Reliable-redshift extreme-score candidates | unmatched AND `ZWARN == 0` AND `DELTACHI2` $>25$ AND $S \ge P_{95}$ | 5 |
| FT-D | Point-source / stellar-locus candidates | unmatched AND `MORPHTYPE == 'PSF'` AND Gaia DR3 counterpart | 0 |
| FT-E | Taxonomy-spanning representative set | highest-score member of each of the 25 clusters | 25 |

**FT-D returns zero targets, and that is a result.** No unmatched point source
in the catalogue has a Gaia DR3 counterpart in the released photometry: the
unmatched population is fainter than Gaia's limit throughout. Galactic
follow-up of this catalogue is therefore not cheap, and the tier is retained
as a rule that a future, deeper generation can re-run rather than being
deleted.

## The named targets

See `outputs/followup_targets.md` for the full table with coordinates. The
targets that justify a programme:

**FT-A — four $z \ge 4$ pipeline QSO candidates with no catalogued
counterpart.** All four are `SPECTYPE = QSO`, `ZWARN = 0`:

| TARGETID | R.A. (deg) | Dec. (deg) | $z$ | $S$ | Family |
|---|---|---|---|---|---|
| 39627903570285763 | 247.89530 | 4.66991 | 6.0878 | 3.496 | 0 |
| 39627607293039577 | 201.10142 | $-7.55332$ | 6.0638 | 3.232 | 4 |
| 39628216868014338 | 239.92842 | 18.01584 | 5.1938 | 3.061 | 0 |
| 39627849358909321 | 252.47163 | 2.60071 | 4.3338 | 3.033 | 0 |

Stated at its evidential strength: these are **anomaly-selected spectra that
are DESI-pipeline $z>4$ QSO candidates**, two of them at $z>6$. They are not
discoveries and not confirmed quasars; a `ZWARN == 0` Redrock solution is a
pipeline result, and high-redshift QSO identifications from single fits fail
routinely on low-S/N spectra.

*Next test, in cost order:* (1) Legacy Survey DR10 $grz$ + unWISE forced
photometry cutouts at these coordinates — a $z>6$ quasar must be $g$-dropout;
any target with significant $g$ flux is refuted on public data alone, at zero
observing cost. (2) Visual inspection of the public DESI DR1 coadd spectrum
for Ly$\alpha$ break and forest. (3) DESI DR2 repeat coadds where the tile is
revisited. (4) Only then confirmation spectroscopy — Keck/LRIS, Gemini/GMOS,
or SALT/RSS for the brightest; near-infrared (Keck/MOSFIRE, VLT/X-shooter)
for a $z>6$ confirmation.

**FT-B — one infrared-excess AGN candidate.** TARGETID 103610381762578
($\alpha = 223.91430$, $\delta = 50.21730$), $W1-W2 = 0.822$, $z = 1.1154$
(`ZWARN = 0`), $S = 3.105$, family 5. $W1-W2 \ge 0.8$ is the standard mid-IR
AGN criterion (Stern et al. 2012). *Next test:* public NEOWISE-R
single-exposure light curve for mid-IR variability; ZTF DR optical light
curve; archival X-ray coverage (eROSITA-DE DR1, Chandra/XMM serendipitous
catalogues). All four are public-archive queries with no proposal required.

**FT-C — five well-measured, hardest-to-reconstruct spectra.** $S$ from 4.64
to 7.15, all with `ZWARN = 0` and `DELTACHI2 > 25`, i.e. secure redshifts and
strong template discrimination *and* a large reconstruction residual. Three of
the five are in family 3 (the extreme tier); the top target,
TARGETID 39627812453222421 ($\alpha = 212.59530$, $\delta = 0.92100$,
$z = 1.0798$, $S = 7.151$), is the highest-scoring unmatched object in the
catalogue. *Next test:* inspect the public DR1 coadd spectrum; re-fit with
Redrock over the full template set; SDSS DR17 spectra where the footprint
overlaps. This tier is where a genuine spectral anomaly, as opposed to noise
or a reduction artefact, is most likely to be found.

**FT-E — 25 representatives, one per taxonomy cluster.** A follow-up
programme that samples every cluster tests the taxonomy itself rather than one
corner of it. *Next test:* DESI DR1 coadd spectrum inspection plus Legacy
Survey DR10 cutouts for each representative; anything unexplained by a known
template escalates into FT-A/B/C handling.

## Open tests the catalogue needs (not object follow-up)

- **OT-1 — selection function.** No injection-recovery experiment has been run
  for this model on this substrate, so the catalogue has no measured
  completeness or purity and no population-level inference may be drawn from
  it. Requires injecting known spectral classes into DESI DR1 coadds at
  controlled S/N and re-scoring with the SHA-256-bound model. GPU-scale, not
  local.
- **OT-2 — latent-space taxonomy.** The released families are built from
  $(S, \alpha, \delta)$ and carry no material structure in the model's own
  128-dimensional latent space (validation check V12). Re-clustering on the
  latents is cheap and is the obvious next version.
- **OT-3 — blue-arm diagnosis.** The score is driven by the $b$ camera
  ($\rho_s = +0.527$ against $r_B$, versus $-0.04$ and $-0.14$ for $r_R$,
  $r_Z$). Whether that reflects a sky-subtraction/calibration residual at the
  blue end or genuine spectral behaviour decides how much of the catalogue is
  astrophysical. Testable on public data: compare $r_B$ against airmass,
  moon phase, and blue-end sky-subtraction residuals in the DR1 exposure
  tables.
- **OT-4 — wider reference-class benchmark.** The recovery benchmark used 5
  of 11 candidate reference classes; the remaining 6 lacked usable positions.
  Recovering positions for those classes would materially strengthen (or
  weaken) the recovery result.
- **OT-5 — deeper scan.** Ledger row 12 (self-supervised spectral model on the
  full DESI DR1 science-target population) remains the realistic route to a
  confirmed anomalous class; the ledger records it as blocked on RunPod
  provisioning, not on method.
