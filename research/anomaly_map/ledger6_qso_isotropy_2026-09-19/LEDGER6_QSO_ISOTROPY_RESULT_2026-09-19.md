# Ledger #6, second discriminator — large-angle isotropy of DESI DR1 quasars

**Date:** 2026-09-19 · **Lane:** `bb-LS2-ledger6` (campaign `CAMPAIGN_2026-09-18_publication_push.md`)
**Ledger item:** `NEXT_SCIENCE_LEDGER.md` row 6 · **Vision route:** `VISION.md` route 3
**Pre-registration:** `PREREGISTRATION.md`, committed **c1acb329** *before* any statistic in this
document existed. Nothing below deviates from it except where §6 says so explicitly.

**One line:** a first-of-its-kind DESI DR1 quasar measurement of the CMB hemispherical-asymmetry
observable finds **no large-angle anisotropy**, and finds the Planck asymmetry axis to be
completely unremarkable among 1,536 admissible axes (p_LEE = 0.58) — but the footprint's own
axis-to-axis scatter (0.141) is twice the CMB amplitude, so the honest verdict is
**NULL, sensitivity-limited** (pre-registered outcome 3), not a refutation.

---

## 1. What was tested and why

Row 6's third anomaly class — the hemispherical/large-angle asymmetry — had been closed only on
the *theory* side: the Erickcek–Kamionkowski–Carroll route needs f_NL^loc ~ 10², and the lab's
matter-contraction value is −35/16 = −2.1875, so a bounce cannot *produce* the asymmetry
(`LEDGER6_DISCRIMINATOR_BRIEF_2026-09-02.md` §1.3, §3). That says nothing about whether the
asymmetry is real. The empirical question, which had never been asked in this lab, is:

> Is the Planck dipolar power modulation a **scale-independent primordial modulation of the
> initial conditions** — in which case an independent tracer of those same initial conditions, at
> a different epoch and different scales, must show it along the same axis?

If yes, the anomaly strains single-field inflation and becomes a genuine route-3 target (one no
existing bounce model in this lab predicts either). If an independent tracer bounds it below the
CMB value on the same axis, the asymmetry cannot be cited as evidence for bounce-scale initial
conditions and the class gets a **current-data verdict** rather than a deferral.

DESI DR1 quasars are the right independent tracer available on this disk: 856,831 spectroscopic
objects at 0.8 < z < 2.1, an epoch and a set of scales entirely disjoint from last scattering,
with a survey selection function supplied as random catalogues and an imaging-systematics weight
that can be switched on and off as a control.

## 2. Data and method (unchanged from the pre-registration)

DESI DR1 LSS clustering catalogues (already local; no download):
`QSO_{NGC,SGC}_clustering.dat.fits` + randoms 0–3 per cap, 0.8 < z < 2.1,
**N = 555,913 (NGC) + 300,918 (SGC) = 856,831** data and 50,768,005 randoms, `WEIGHT` applied,
FKP weights not applied. HEALPix nside = 64 maps; mask = pixels with weighted random count above
0.5 × the cap median. Masked footprint: **10,660 pixels = 8,947 deg²**, mean surface density
95.8 deg⁻², effective 71 weighted counts per 0.84 deg² pixel, NGC/SGC pixel overlap = 0.

- **S2 (primary)** — the LSS analogue of the CMB observable: fit
  ⟨δ² − shot⟩ = σ²_cap (1 + 2A · n̂·p̂) for a single modulation amplitude `A` along the
  Planck 2018 VII axis (l, b) = (209°, −15°), for which the CMB gives A ≈ 0.07 at ℓ ≲ 60.
- **S1 (diagnostic)** — the number-count dipole `d` from δ = m_cap + d·n̂.
- Nulls N1 (Poisson/selection, 500 realisations), N2 (1,536-axis look-elsewhere scan),
  N3 (seven-way systematics bracket + per-cap split).

Measured clustering amplitude at the pixel scale: σ_clust = 0.0693 (NGC), 0.0788 (SGC), i.e. a
clustering variance 0.37–0.40 × the shot-noise variance — the regime where shot-noise subtraction
has to be exact, which is why the per-pixel Σw² shot term is used rather than a global mean.

## 3. Estimator validation (injection–recovery)

Simulated maps with a known modulation (Gaussian clustering of the measured amplitude, modulated
as σ²_cap(1 + 2A_in x), plus the measured Poisson shot noise), 200 realisations each:

| injected A | recovered A | bias |
|---|---|---|
| 0.00 | +0.0055 ± 0.0519 | +0.006 |
| **0.07** (the CMB value) | **+0.0766 ± 0.0469** | +0.007 |
| 0.20 | +0.1972 ± 0.0431 | −0.003 |

The estimator is unbiased at the 0.007 level, and — importantly — **a true A = 0.07 would be only
a ~1.5σ measurement in this footprint even in the idealised uncorrelated case**. That number, set
before looking at the answer's significance, is what makes the verdict "sensitivity-limited"
rather than "excluded".

## 4. Results

### 4.1 S2 — dipolar modulation of the clustering amplitude (primary)

| quantity | value |
|---|---|
| **A (Planck axis)** | **−0.0535** |
| fit error | ± 0.0428 |
| delete-one jackknife (31 nside-2 regions) | ± 0.0560 |
| axis-to-axis rms over the 1,536 admissible axes | ± 0.1412 |
| slope b = 2σ²A | −5.88 × 10⁻⁴ |
| geometric leverage rms(n̂·p̂) | 0.581 (x spans −0.98 … +0.98) |

**N1 (Poisson/selection null, evaluated on the slope b, which stays well defined when there is no
clustering to modulate):** p = 0.186 (shot + clustering proxy), p = 0.080 (shot only).
Pre-registered criterion 1 (p < 0.01): **not met**.

**N2 (look-elsewhere):** |A| = 0.052 on the Planck axis sits at the **41.8th percentile** of the
1,536 admissible axes, whose median |A| is 0.067 and maximum 0.452; **p_LEE = 0.58**.
Pre-registered criterion 2 (p_LEE < 0.05): **not met**. The CMB-flagged direction is
indistinguishable from an arbitrary direction in this data set.

**N3 (systematics bracket):** A stays negative in all nine variants and no variant is more than
~1σ from the baseline —

| variant | A | variant | A |
|---|---|---|---|
| baseline (nside 64) | −0.053 ± 0.043 | joint-α | −0.053 ± 0.043 |
| WEIGHT_SYS removed | −0.055 ± 0.044 | nside 32 | −0.096 ± 0.061 |
| \|b_gal\| > 30° | −0.024 ± 0.049 | nside 128 | −0.037 ± 0.020 |
| mask 0.8 × median | −0.035 ± 0.044 | mask 0.95 × median | −0.054 ± 0.047 |
| NGC only | −0.076 ± 0.053 | SGC only | −0.006 ± 0.074 |

NGC vs SGC differ by 0.070 ± 0.091 = **0.76σ** — the two independent caps agree.

**95% upper bounds.** |A| < **0.150** with the pre-registered error (N1 width ⊕ fit error);
|A| < **0.286** with the conservative error (the axis-to-axis rms). Both are above A_CMB = 0.07.

### 4.2 S1 — number-count dipole (systematics diagnostic)

|d| = 0.00446 ± 0.00466, entirely consistent with the Poisson/selection null (p = 0.85; the null's
own mean |d| is 0.0090, i.e. *larger* than the measurement). 95% bound |d| < 0.0123 with per-cap
monopoles, < 0.0087 with a single shared monopole.

Two control results worth keeping:

- **The imaging-systematics weight is doing real work and S2 does not need it.** With `WEIGHT_SYS`
  divided out, the count dipole grows 5× to 0.0221 — several times the kinematic expectation
  (≈ 0.005) — while **A moves by 0.001**. So the primary statistic is insensitive to exactly the
  systematic that dominates the secondary one.
- **The high-resolution dipole is an edge artifact, not a gradient.** At nside 128 |d| = 0.0296,
  falling monotonically to 0.0229 (mask 0.8) and 0.0131 (mask 0.95) as partially-covered boundary
  pixels are removed; at nside 64 with mask 0.95 it is 0.0032. Any future use of this map at
  nside ≥ 128 must apply the stricter mask.

## 5. VERDICT

**NULL — no large-angle anisotropy detected in DESI DR1 quasars, and the result is
sensitivity-limited with respect to the CMB amplitude.** This is pre-registered outcome 3 of
§6 ("measured, not yet constraining"), and it is recorded at exactly that strength:

- Neither pre-registered detection criterion is met (p = 0.19; p_LEE = 0.58). There is **no**
  evidence for a shared primordial modulation, and the Planck axis carries no special status in
  this tracer.
- The point estimate is **negative** (−0.053), i.e. slightly *less* clustering power toward the
  CMB's high-power hemisphere — the opposite sign to a shared modulation. Taken at the fit or
  jackknife error this would disfavour A = +0.07 at 2.9σ / 2.2σ. **Those figures are reported but
  not adopted**, because the footprint's own axis-to-axis scatter (0.141) is 2.5–3.3× larger than
  those errors, which is direct evidence that they do not capture the large-angle
  cosmic-variance-plus-systematics floor of an 8,947 deg² two-cap geometry. Against that
  conservative error the measurement is 0.87σ from +0.07 and cannot exclude it.
- Therefore: **the hemispherical asymmetry is neither confirmed nor excluded by DESI DR1
  quasars.** What row 6 gains is a measured number with a validated estimator where before it had
  only a theory-side closure, plus a quantified reason why this footprint cannot settle it.

**What this does and does not say about bounce vs single-field inflation.** Nothing here supports
either. A shared scale-independent modulation was not found, so — as of this test — the asymmetry
supplies no positive anomaly for route 3 to build on, and the pre-registered rule already forbade
citing it as bounce evidence in that case. It also remains true that the lab's own f_NL = −35/16
could not generate such a modulation if it were found (ledger 6, first test). Both ΛCDM +
single-field inflation and the lab's matter bounce remain untouched by this measurement.

**Literature context (not a lab number).** A scale-independent power asymmetry extending to
quasar scales was already constrained by Hirata 2009 (arXiv:0907.0703) with SDSS quasars at a
level below the CMB amplitude, which is the origin of the standard statement that the asymmetry,
if primordial at all, must be strongly scale-dependent. The present measurement is an
independent check in a different dataset with a different systematics chain — not a competitive
new bound.

## 6. Declared deviations from the pre-registration

1. **Nulls evaluated on the slope b, not on A.** In a pure-noise realisation the clustering
   variance σ²_cap → 0 and A = b/(2σ²) diverges; the first run produced a meaningless null
   (A_std ≈ 5.8 × 10⁴). The null is therefore computed on the well-defined slope b and rescaled
   to A-equivalent units with the *data* value of σ². This changes only the null, not the
   statistic, and it is strictly more conservative than the degenerate version.
2. **N1 run twice** — shot-only (as pre-registered) and with an added white clustering component
   of the measured variance. The headline p-value uses the second, larger-variance null.
3. **Delete-one jackknife added** (31 nside-2 superpixel regions) as an empirical error that
   includes pixel–pixel correlations. Pre-registered bound kept as the headline; the jackknife and
   axis-scatter bounds are reported alongside.
4. **Two extra mask variants** (0.95 × median at nside 64 and 128) added after the nside-128
   dipole looked large; they diagnosed it as an edge effect (§4.2).
5. **Injection–recovery validation added** (§3). Not pre-registered; it strengthens the verdict.

No statistic, axis, threshold, or decision rule in §3–§5 of the pre-registration was changed after
seeing a result.

## 7. Next step for row 6

The limiting factor is not quasar shot noise — it is footprint geometry plus the large-angle
systematics floor, which a 2.5× larger DESI area will not fix by √N alone. The correct next
instrument for this observable is a **full-sky photometric quasar sample** (Gaia-unWISE/Quaia or
CatWISE), where the same estimator has real hemispheric leverage; the DESI spectroscopic sample
then serves as the systematics-controlled cross-check that this run has now calibrated.
Recommended as the row-6 follow-up, **not** started here (it needs a new public catalogue
download, and this machine has ~10 GB free).

## 8. Artifacts

| Path | What |
|---|---|
| `PREREGISTRATION.md` | pre-registration, commit c1acb329, written before any statistic |
| `build_maps.py` | catalogue → HEALPix maps (23 s, CPU) |
| `analyze_isotropy.py` | S1, S2, N1, N2, N3, injection–recovery, jackknife (5 s, CPU) |
| `make_figure.py` | the figure |
| `outputs/ledger6_qso_isotropy.json` | every number in this document |
| `outputs/ledger6_qso_isotropy.png` | map + modulation fit + look-elsewhere histogram |
| `outputs/maps_nside{32,64,128}.npz`, `outputs/maps_meta.json` | the maps (2 MB total) |
| `outputs/axis_scan_A.npy`, `outputs/run_log.txt` | axis scan, full stdout |
| `reproducibility/manifests/experiments/anomaly-map-qso-large-angle-isotropy.json` | directive-Q2 manifest |

Reproduce: `python build_maps.py && python analyze_isotropy.py && python make_figure.py`
(~30 s total, CPU-only, no network; needs the DR1 QSO clustering catalogues at
`~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/`). Deterministic given seed 20260919.
