#!/usr/bin/env python3
"""
P3-A-TYPING-PHASE — TESS sector 45/72 cross-check for TIC 374313355.

Fire #15 established P = 13.782 d (FAP 3.9e-263) on sector 46 FFI-cutout
photometry. This script repeats the Lomb-Scargle analysis on sectors 45
and 72 to test whether the periodicity and phase remain consistent —
which rules in/out rotation vs EB vs instrumental artifact.

Verdict logic:
  - If both 45 + 72 give P ≈ 13.782 d AND phase offset vs sec 46 is
    < 30°  → "consistent_rotation"  (long rotation period stable over
    1+ year baseline)
  - If both give the same P AND phase is incoherent (> 60° offset)
    across sectors → "eclipsing_binary" (EB with ephemeris drift) or
    otherwise period-stable but phase-scrambled source
  - If sectors disagree on P by > 1% → "artifact_rejected"

Output: /workspace/bigbounce_scan/outputs/p3a_phase/phase_cross_check.json

Runtime cap: 30 min.
"""

import json
import time
import pathlib
import traceback
import numpy as np

OUT_DIR = pathlib.Path("/workspace/bigbounce_scan/outputs/p3a_phase")
OUT_DIR.mkdir(parents=True, exist_ok=True)

TIC = "TIC 374313355"
RA = 160.148889
DEC = 5.091599
SEC46_PERIOD_DAYS = 13.782472108082912
SEC46_PHASE_REF_T0_BJD = None  # We reconstruct phase from peak crossing time in sec 46

t0 = time.time()
results = {
    "task": "P3-A-TYPING-PHASE",
    "target": TIC,
    "ra_deg": RA, "dec_deg": DEC,
    "sec46_reference": {
        "period_days": SEC46_PERIOD_DAYS,
        "peak_power": 0.31042915728740045,
        "false_alarm_prob": 3.8853139892386195e-263,
        "source": "fire #15 FFI-cutout",
    },
    "sectors": {},
}

try:
    import lightkurve as lk
    from astropy.timeseries import LombScargle
except Exception as e:
    results["error"] = f"import failed: {e}\n{traceback.format_exc()}"
    with open(OUT_DIR / "phase_cross_check.json", "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    raise

def analyze_sector(sector_num, budget_s_remaining):
    print(f"[P3A] === Sector {sector_num} ===")
    tic_t0 = time.time()
    entry = {"sector": sector_num}
    try:
        tpfs = lk.search_tesscut(TIC, sector=sector_num).download(cutout_size=11)
        if tpfs is None:
            entry["status"] = "no_tpf_returned"
            return entry
        # Simple aperture: threshold mask around central pixel
        try:
            mask = tpfs.create_threshold_mask(threshold=3, reference_pixel="center")
        except Exception:
            mask = tpfs.pipeline_mask
        lc = tpfs.to_lightcurve(aperture_mask=mask).remove_nans().flatten(window_length=401)
        entry["n_points"] = int(len(lc.time.value))
        if len(lc.time.value) < 100:
            entry["status"] = "insufficient_points"
            return entry
        time_d = np.asarray(lc.time.value, dtype=float)
        flux = np.asarray(lc.flux.value, dtype=float)
        mask_f = np.isfinite(flux) & np.isfinite(time_d)
        time_d = time_d[mask_f]; flux = flux[mask_f]
        flux = flux - np.median(flux)
        # Lomb-Scargle — scan around expected period plus broader window
        f_min = 1.0 / 25.0    # 25 days
        f_max = 1.0 / 2.0    # 2 days
        freqs = np.linspace(f_min, f_max, 50000)
        ls = LombScargle(time_d, flux)
        power = ls.power(freqs)
        peak = np.argmax(power)
        best_f = freqs[peak]
        best_P = 1.0 / best_f
        fap = float(ls.false_alarm_probability(power[peak]))
        # Phase offset vs sec46: phase of flux peak relative to first time stamp,
        # computed at the expected period
        P_ref = SEC46_PERIOD_DAYS
        phase_ref = ((time_d - time_d[0]) / P_ref) % 1.0
        # Find the photometric maximum in phase
        order = np.argsort(phase_ref)
        # Bin the phase curve into 50 bins and find max
        nb = 50
        bin_edges = np.linspace(0, 1, nb + 1)
        bin_means = np.full(nb, np.nan)
        for b in range(nb):
            m = (phase_ref >= bin_edges[b]) & (phase_ref < bin_edges[b + 1])
            if m.sum() > 3:
                bin_means[b] = np.median(flux[m])
        if np.isfinite(bin_means).any():
            phase_peak = (bin_edges[:-1] + bin_edges[1:]) / 2
            phase_max_deg = 360.0 * phase_peak[np.nanargmax(bin_means)]
        else:
            phase_max_deg = None
        entry.update({
            "status": "ok",
            "peak_period_days": float(best_P),
            "peak_power": float(power[peak]),
            "false_alarm_prob": fap,
            "phase_max_deg_at_P_ref": (float(phase_max_deg)
                                       if phase_max_deg is not None else None),
            "period_frac_diff_vs_sec46": float((best_P - P_ref) / P_ref),
            "runtime_s": round(time.time() - tic_t0, 1),
        })
        print(f"[P3A]  sec {sector_num}: P={best_P:.4f}d, FAP={fap:.2e}, "
              f"Δphase={phase_max_deg}")
        return entry
    except Exception as e:
        entry["status"] = f"error: {e}"
        entry["traceback"] = traceback.format_exc()
        print(f"[P3A]  sec {sector_num} FAILED: {e}")
        return entry

# Sector 46 = reference (fire #15 already computed; we compute here too for
# a phase anchor using the same aperture pipeline)
results["sectors"]["46"] = analyze_sector(46, 1600)
elapsed = time.time() - t0
if elapsed < 1600:
    results["sectors"]["45"] = analyze_sector(45, 1600 - elapsed)
else:
    results["sectors"]["45"] = {"status": "skipped_budget_exceeded"}
elapsed = time.time() - t0
if elapsed < 1600:
    results["sectors"]["72"] = analyze_sector(72, 1600 - elapsed)
else:
    results["sectors"]["72"] = {"status": "skipped_budget_exceeded"}

# Phase offsets vs sector 46
ref_phase = results["sectors"].get("46", {}).get("phase_max_deg_at_P_ref")
for k in ("45", "72"):
    entry = results["sectors"].get(k, {})
    ph = entry.get("phase_max_deg_at_P_ref")
    if ref_phase is not None and ph is not None:
        delta = abs(ph - ref_phase)
        if delta > 180:
            delta = 360 - delta
        entry["phase_offset_deg_vs_sector46"] = float(delta)
    else:
        entry["phase_offset_deg_vs_sector46"] = None

# Verdict
def _sec_ok(s):
    return s and s.get("status") == "ok"
s45 = results["sectors"].get("45", {})
s46 = results["sectors"].get("46", {})
s72 = results["sectors"].get("72", {})

if _sec_ok(s45) and _sec_ok(s72):
    frac_45 = abs(s45["period_frac_diff_vs_sec46"])
    frac_72 = abs(s72["period_frac_diff_vs_sec46"])
    phase_45 = s45.get("phase_offset_deg_vs_sector46")
    phase_72 = s72.get("phase_offset_deg_vs_sector46")
    if frac_45 > 0.01 or frac_72 > 0.01:
        verdict = "artifact_rejected"
    elif (phase_45 is not None and phase_72 is not None
          and phase_45 < 30 and phase_72 < 30):
        verdict = "consistent_rotation"
    elif (phase_45 is not None and phase_72 is not None
          and (phase_45 > 60 or phase_72 > 60)):
        verdict = "eclipsing_binary"
    else:
        verdict = "ambiguous"
else:
    verdict = "inconclusive_missing_sectors"

results["verdict"] = verdict
results["runtime_s"] = round(time.time() - t0, 1)
results["completed_at_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

with open(OUT_DIR / "phase_cross_check.json", "w") as fh:
    json.dump(results, fh, indent=2, default=float)
print(f"[P3A] Wrote {OUT_DIR / 'phase_cross_check.json'}")
print(f"[P3A] VERDICT: {verdict}")
print(f"[P3A] TOTAL runtime {time.time()-t0:.1f}s")
print("[P3A] DONE")
