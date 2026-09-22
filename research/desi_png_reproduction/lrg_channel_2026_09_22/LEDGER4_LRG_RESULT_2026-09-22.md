# Ledger #4 — the LRG channel, opened (2026-09-22)

**Lane:** `LS11-row4-lrg` · **Pre-registration:** `PRE_REGISTRATION.md`,
committed as `87b850b8` **before any statistic was computed** · **Run log:**
`RUN_LOG.md` · **Manifest:**
`reproducibility/manifests/experiments/ledger4-desi-dr1-lrg-fnl-channel.json`

Ledger row 4 carried "**LRG channel NOT STARTED**" through five result
versions (v1–v5, 2026-09-04), blocked on ≈64 GB of catalogues against ~10 GB
of free disk. It is now open, at the fidelity v5 established for QSO, with
**zero bulk catalogue bytes written to disk**.

---

## 1. Headline

Official DESI DR1 LRG window matrix + measured P_ℓ + EZmock covariance, all
three z-bins; b₁ free, n_shot fixed at 0, 0.003 ≤ k ≤ 0.08 h/Mpc, ℓ = 0,2,4,
profile-likelihood Δχ² = 1. Exactly the v3/v5 QSO machinery.

| z-bin | z_eff | f_NL (p = 1.0) | b₁ | χ²/dof |
|---|---|---|---|---|
| 0.4–0.6 | 0.50963 | −7.92 ± 9.91 | 1.8656 | 1.286 |
| 0.6–0.8 | 0.70580 | −1.38 ± 8.98 | 2.0546 | 1.193 |
| 0.8–1.1 | 0.91859 | −0.80 ± 10.38 | 2.2132 | 1.350 |

| combination | p | f_NL | 68 % interval |
|---|---|---|---|
| **three bins (pre-registered headline)** | **1.0** | **−3.40 ± 5.74** | **[−9.19, +2.30]** |
| three bins | 1.6 | −6.63 ± 13.68 | [−20.40, +6.97] |
| three bins, p-marginalised midpoint | [1.0, 1.6] | −5.02 | ~9.71 |
| 0.6 < z < 1.1 (published sample definition) | 1.0 | −1.14 ± 6.90 | [−8.23, +5.57] |
| 0.6 < z < 1.1 | 1.6 | −2.41 ± 14.87 | [−17.68, +12.06] |

Both combinations are reported because Chaussidon et al. 2024's LRG PNG
sample is 0.6 < z < 1.1 — the upper two of the three official z-bins. The
pre-registered headline is the three-bin number; the two-bin number is given
**alongside** it, not instead of it. The difference between them is driven
entirely by the z0.4–0.6 bin's −7.92, which is 0.49σ from each of the other
two bins: noise, not a discrepancy.

**b₁ rises monotonically with z_eff (1.87 → 2.05 → 2.21)**, the expected
LRG behaviour, and it was never imposed — b₁ is free in every fit and was
only *started* from 1.7/D(z).

### The error bar is optimistic and must not be read as beating DESI

σ = 5.74 is **smaller** than the published ±9.0 for LRG+QSO. This is not a
better measurement. Three disclosed reasons, all in the conservative
direction for anyone quoting it:

1. **Two free parameters per bin** (b₁, f_NL) with n_shot fixed at 0. DESI
   marginalises over a full nuisance set (shot noise, EFT bias/counterterms,
   imaging-systematic amplitudes); that marginalisation broadens their
   posterior and is absent here.
2. **The three z-bins are treated as independent.** No cross-bin official
   covariance product exists, so their shared large-scale modes and shared
   systematics are unmodelled. This under-estimates the combined σ.
3. **No θ-cut and no rotated data vector** — the untreated products were used,
   matching what v3–v5 used for QSO.

The honest reading: this is an *internally consistent* reproduction on one
convention, good for comparing LRG against QSO within this lab's pipeline,
**not** a competitive independent constraint.

---

## 2. Agreement with the QSO channel — AGREE

Pre-registered rule (fixed before any number was seen):
T = (f_LRG − f_QSO)/√(σ_LRG² + σ_QSO²); |T| < 2 AGREE, 2 ≤ |T| < 3 MILD
TENSION, ≥ 3 TENSION. Channels treated as independent (disclosed: shared
volume unmodelled, which makes T conservative *toward* finding tension).

| p | LRG (this work) | QSO (v3/v5, unchanged) | T | verdict |
|---|---|---|---|---|
| 1.0 | −3.40 ± 5.74 | −1.13 ± 13.15 | **−0.159** | **AGREE** |
| 1.6 | −6.63 ± 13.68 | −2.17 ± 25.29 | **−0.155** | **AGREE** |
| 1.0, published-sample-matched | −1.14 ± 6.90 | −1.13 ± 13.15 | −0.001 | AGREE |

The two tracers agree at a sixth of a sigma. Against the external targets,
at p = 1.0: T = **+0.018** versus Chaussidon et al. 2024's
−3.6 (+9.0/−9.1), and T = **−0.030** versus Brown et al. 2026's −3 ± 12.

**The closeness of −3.40 to the published −3.6 is a consistency check, not a
confirmation at that precision.** The procedures differ (§1), the σ here is
optimistic, and the agreement is measured against an error bar that is not
the published one. Stated at that strength and no higher.

Internal consistency across z-bins (same tracer, largely independent
volumes), p = 1.0: 0.49σ, 0.50σ, 0.04σ. No bin is an outlier.

---

## 3. The five-row systematics table, on one convention

Same splits, same pypower settings (nmesh 256, N_RAN 4, ℓ = 0,2,4,
edges `arange(0, 0.31, 0.001)`, first-point LOS, TSC, interlacing 2), same
official window + official EZmock covariance, same disclosed **√2
covariance-reuse correction** as v4/v5 — no split-specific official
covariance exists, so the full-sample covariance is reused for each ~50 %
half, which under-estimates σ_Δ by roughly √2. Sixty P(k) measurements
(5 properties × 2 halves × 2 caps × 3 z-bins). Medians computed on the LRG
data catalogue per z-bin, never copied from the QSO run.

Pre-registered verdict rule on the √2-corrected |Δ/σ|: ≥ 2 FLAGS,
1 ≤ |Δ/σ| < 2 MARGINAL WATCH ITEM, < 1 no detectable sensitivity.

| z-bin | systematic | f_NL(high) | f_NL(low) | Δf_NL | σ_Δ | Δ/σ | Δ/σ (√2-corr.) | verdict |
|---|---|---|---|---|---|---|---|---|
| 0.4–0.6 | E(B−V) | −12.68 ± 11.14 | −7.78 ± 10.57 | −4.90 | 15.36 | −0.32 | −0.23 | null |
| 0.4–0.6 | Stellar density | −13.17 ± 10.08 | −5.68 ± 9.93 | −7.48 | 14.15 | −0.53 | −0.37 | null |
| 0.4–0.6 | Galactic depth (z) | −13.51 ± 11.53 | −9.56 ± 9.55 | −3.95 | 14.97 | −0.26 | −0.19 | null |
| 0.4–0.6 | WEIGHT_SYS on/off | −8.17 ± 9.65 | −6.39 ± 7.66 | −1.78 | 12.32 | −0.15 | −0.10 | null |
| 0.4–0.6 | Galactic latitude | −5.84 ± 9.85 | −21.35 ± 14.71 | +15.51 | 17.70 | +0.88 | +0.62 | null |
| 0.6–0.8 | E(B−V) | −4.49 ± 9.74 | −5.60 ± 9.98 | +1.12 | 13.95 | +0.08 | +0.06 | null |
| 0.6–0.8 | Stellar density | −1.00 ± 8.43 | −4.03 ± 9.68 | +3.03 | 12.83 | +0.24 | +0.17 | null |
| 0.6–0.8 | Galactic depth (z) | −9.20 ± 9.02 | −5.16 ± 13.91 | −4.04 | 16.58 | −0.24 | −0.17 | null |
| 0.6–0.8 | WEIGHT_SYS on/off | −1.32 ± 8.93 | +7.12 ± 10.16 | −8.44 | 13.53 | −0.62 | −0.44 | null |
| 0.6–0.8 | Galactic latitude | +0.59 ± 11.86 | −1.60 ± 11.67 | +2.19 | 16.64 | +0.13 | +0.09 | null |
| 0.8–1.1 | **E(B−V)** | −17.62 ± 8.47 | −0.27 ± 8.95 | −17.35 | 12.32 | **−1.41** | **−0.995** | null (see below) |
| 0.8–1.1 | Stellar density | −11.89 ± 19.60 | −4.12 ± 7.39 | −7.77 | 20.95 | −0.37 | −0.26 | null |
| 0.8–1.1 | Galactic depth (z) | −11.02 ± 8.52 | −10.50 ± 11.05 | −0.52 | 13.96 | −0.04 | −0.03 | null |
| 0.8–1.1 | WEIGHT_SYS on/off | +0.45 ± 14.13 | +4.93 ± 15.45 | −4.48 | 20.93 | −0.21 | −0.15 | null |
| 0.8–1.1 | Galactic latitude | −3.46 ± 9.58 | −11.28 ± 9.90 | +7.82 | 13.78 | +0.57 | +0.40 | null |

Values at p = 1.6 are in `outputs/systematics_table_lrg.json`; every Δ/σ
agrees with the p = 1.0 value to two decimals, because p rescales f_NL and
its error together. The Δ/σ verdicts are therefore p-independent.

**All fifteen rows are nulls at this fidelity.** Three statements that keep
that honest:

- **The one row that came closest is named, not buried.** E(B−V) at
  z0.8–1.1 is **−0.995σ** after the √2 correction (−1.41σ raw) — it falls
  on the null side of a threshold fixed in advance by **0.005σ**. It is the
  single largest imaging sensitivity in the LRG channel and is recorded here
  as the first thing to re-test if anyone revisits this table. Calling it a
  null is what the pre-registered rule says; treating it as settled would
  not be.
- **Some split halves fit poorly**, χ²/dof up to 2.67 (z0.8–1.1 Galactic
  latitude, low half), against 1.19–1.35 for the full-sample headline fits.
  That is expected from reusing a full-sample covariance on a half-sample
  and is exactly the approximation the √2 correction is disclosed for; it
  also means these Δ/σ values should not be read to better than ~±0.2.
- **No threshold, weight, bin or convention was changed after seeing a
  number.**

### WEIGHT_SYS behaves completely differently in LRG than in QSO

This is the most interesting result in the table. In the QSO channel (v5),
WEIGHT_SYS on/off was the dominant systematic: Δ/σ = −4.31 raw, −3.05
corrected, with χ²/dof degrading from ~0.85 to ~4.4 when the correction was
divided out. In LRG it is a **null in every z-bin** (−0.10, −0.44, −0.15
corrected).

The honest reading: DESI's imaging-systematics correction does large,
necessary work on quasars and very little on LRGs at these scales. That is
consistent with the known picture — quasar target selection is far more
sensitive to imaging depth and stellar contamination than LRG selection —
and it means **the single largest item in the lab's QSO systematics budget
simply does not transfer to the LRG channel**. It is not evidence that
either measurement is wrong.

---

## 4. Does the LRG channel discriminate the flagship prediction? No.

| p | f_NL | distance from −35/16 = −2.1875 | distance from −35/8 = −4.375 (superseded) | separation of the two |
|---|---|---|---|---|
| 1.0 | −3.40 ± 5.74 | 0.21σ | 0.17σ | **0.38σ** |
| 1.6 | −6.63 ± 13.68 | 0.32σ | 0.17σ | 0.16σ |

The two candidate values are 2.19 apart; the LRG channel's σ is 5.74. They
remain **indistinguishable**, exactly as ledger rows 3 and 4 already record
for QSO. Opening the LRG channel improves the reach by a factor ~2.3 in σ
(13.15 → 5.74 at p = 1.0) and that is still an order of magnitude short of
what a discrimination needs. The near-coincidence of the central value with
either prediction is a coincidence and carries no evidential weight.

**This channel is a null result for the flagship question, and that is the
outcome reported.**

---

## 5. What this cost, and what it proves about method

| quantity | value |
|---|---|
| bytes streamed (catalogues + randoms) | 6,233,140,800 |
| bytes streamed (official VAC products) | 651,939,768 |
| **total streamed** | **6,885,080,568 B (6.89 GB)** |
| **bulk catalogue bytes written to disk** | **0** |
| **peak disk** | **2,381,031,400 B (2.38 GB)** — derived float32 column cache outside the repo |
| free disk at lane start | ~11 GB |
| wall clock | 376 s streaming the cache; 1,299 s headline fits; 1,755 s for 60 P(k) measurements; ~190 s of split fits |
| compute venue / cost | local CPU, **$0.00** |

The blocker that held this row for five versions was disk, not compute. The
`bb-LS10` streaming pattern removed it: 6.89 GB moved through memory, 2.38 GB
of derived columns kept, and the 59,525,171 catalogue rows the analysis
needed were never materialised as files. A reproducer needs ≥ 3 GB free, not
64 GB.

**Verification receipts**, all committed:

- `tests/regress_qso.py` reproduces v5's published QSO headline on the local
  QSO products before any LRG number was believed: χ² = 62.4010 and
  b₁ = 2.24932 to the last printed digit, f_NL matching to 2 × 10⁻⁵ σ.
- The b1-quadratic reorganisation agrees with the original expression to
  1.2 × 10⁻¹² (float64 roundoff).
- The z_eff parameterisation is **bit-for-bit the same code path** as the
  QSO fits when evaluated at z_eff = 1.491 (asserted at run time; the fit
  refuses to produce a number otherwise).
- Lab-native object count in the published sample range: **1,631,715** vs
  Chaussidon et al.'s **1,631,716** — one object, the strict-vs-inclusive
  edge cut. Provenance match, not a measurement.
- Whole-file sha256 for all 10 streamed catalogues
  (`outputs/stream_manifest.json`) and all 9 streamed official products
  (`outputs/fnl_lrg_headline.json`).
- Vectorised Galactic latitude vs `astropy.SkyCoord`: max |Δb| = 3.06 × 10⁻⁶ deg.

---

## 6. Standing open items after this round

1. **E(B−V) at z0.8–1.1, −0.995σ** — the closest row to the watch threshold;
   first thing to re-test at higher fidelity.
2. **No split-specific official covariance exists** for any of the 15 rows
   (disclosed approximation, same class as v4/v5's QSO table). The elevated
   split χ²/dof (up to 2.67) is the visible symptom.
3. **No cross-bin covariance** for the three-bin combination — the combined
   σ = 5.74 is under-estimated for this reason as well as the nuisance
   reason in §1.
4. **Galactic latitude in QSO remains marginal** (−1.26σ to −1.78σ, v5). The
   LRG channel does **not** close that item — LRG's Galactic-latitude rows
   are nulls (+0.62, +0.09, +0.40), which is a *different* sample's answer,
   not a resolution of the QSO one.
5. **Neither channel can discriminate −35/16 from −35/8.** Unchanged.
6. The `_thetacut0.05` and `-rotated` official variants exist and were not
   used (v3–v5 used the untreated QSO products; this channel matched that).
   Re-running on them is a bounded, named next step.

**Never tuned toward the published value.** The three-bin headline, the
two-bin published-matched combination, the fifteen null rows, the borderline
E(B−V) row and the optimistic-σ caveat are all reported exactly as measured.
