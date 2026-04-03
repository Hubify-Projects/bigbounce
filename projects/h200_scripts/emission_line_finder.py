#!/usr/bin/env python3
"""
Emission Line Finder — Classify SDSS anomalies by band-residual patterns.

Loads the sdss_batch_*.parquet anomaly files produced by the SDSS DR18 scan,
uses the per-band residuals (rB, rR, rZ) as proxies for spectral features,
trains a small random forest on SDSS spectral classes (when available),
and cross-references residual peaks with known emission line wavelengths.

Band mapping (from sdss_scan.py resample 496 bins over 3600-9800 A):
  rB: bins   0-170 → 3600-6200 A  (blue optical: [OII], H-beta, [OIII])
  rR: bins 170-340 → 6200-8200 A  (red optical: H-alpha, [NII], [SII])
  rZ: bins 340-496 → 8200-9800 A  (near-IR: CaII triplet, telluric)

Output → /workspace/bigbounce/outputs/emission_lines/
  emission_line_summary.json   — aggregate statistics + category breakdown
  classified_anomalies.parquet — full table with predicted categories
  checkpoint.json              — resume state

Usage:
  pip install pyarrow pandas scikit-learn torch numpy
  python3 emission_line_finder.py
"""

import glob
import json
import os
import sys
import time

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

# ── Paths ─────────────────────────────────────────────────────────────────

DATA_DIR = "/workspace/bigbounce/outputs"
OUT_DIR  = "/workspace/bigbounce/outputs/emission_lines"
CKPT_PATH = os.path.join(OUT_DIR, "checkpoint.json")

ANOMALY_THRESHOLD = 5.0   # same threshold used by classify_sdss_anomalies.py

# ── Known emission/absorption lines (rest-frame Angstroms) ────────────────

KNOWN_LINES = {
    # UV / high-z
    "Ly-alpha": 1216, "CIV": 1549, "CIII]": 1909, "MgII": 2798,
    # Blue optical (rB band: 3600-6200 A)
    "[OII] 3727": 3727, "[NeIII]": 3869, "CaII K": 3934, "CaII H": 3969,
    "H-delta": 4102, "H-gamma": 4340, "H-beta": 4861,
    "[OIII] 4959": 4959, "[OIII] 5007": 5007, "MgI b": 5175, "NaI D": 5893,
    # Red optical (rR band: 6200-8200 A)
    "[OI]": 6300, "H-alpha": 6563, "[NII]": 6584,
    "[SII] 6717": 6717, "[SII] 6731": 6731,
    "O2 B-band": 6870, "TiO 7100": 7100, "H2O telluric": 7200,
    "O2 A-band": 7600,
    # Near-IR (rZ band: 8200-9800 A)
    "TiO 8430": 8430, "CaII 8498": 8498, "CaII 8542": 8542,
    "CaII 8662": 8662,
}

# Partition lines by band for residual-to-line mapping
BAND_RANGES = {"rB": (3600, 6200), "rR": (6200, 8200), "rZ": (8200, 9800)}
LINES_BY_BAND = {band: {} for band in BAND_RANGES}
for name, wave in KNOWN_LINES.items():
    for band, (lo, hi) in BAND_RANGES.items():
        if lo <= wave < hi:
            LINES_BY_BAND[band][name] = wave
            break

# ── Rule-based classifier ─────────────────────────────────────────────────

def classify_residual_pattern(rB, rR, rZ, score):
    """
    Classify an anomaly by its band-residual pattern.

    Returns (category, likely_lines, confidence).
    """
    total = rB + rR + rZ + 1e-12
    fB, fR, fZ = rB / total, rR / total, rZ / total

    # Artifact: extreme single-band spike with very high score
    if score > 1e4 and (fB > 0.85 or fR > 0.85 or fZ > 0.85):
        return "ARTIFACT", [], "high"

    # High rB only → UV excess / blue emission
    if fB > 0.55 and fR < 0.30 and fZ < 0.25:
        lines = list(LINES_BY_BAND["rB"].keys())[:3]
        if score > 500:
            return "QSO_BLUE_EXCESS", lines, "medium"
        return "UV_EXCESS_YOUNG_STAR", lines, "low"

    # High rR only → H-alpha / optical emission
    if fR > 0.55 and fB < 0.30:
        lines = ["H-alpha", "[NII]", "[SII] 6717"]
        if fZ > 0.20:
            return "AGN_BROAD_EMISSION", lines, "medium"
        return "STAR_FORMING_HALPHA", lines, "medium"

    # High rZ only → near-IR excess
    if fZ > 0.50 and fZ > fB * 2.0:
        lines = list(LINES_BY_BAND["rZ"].keys())[:3]
        return "NIR_EXCESS_HIGH_Z", lines, "medium"

    # High all bands → unusual continuum
    if abs(fB - fR) < 0.12 and abs(fR - fZ) < 0.12 and score > 10:
        return "UNUSUAL_CONTINUUM", [], "low"

    # Blue + Red but not Z → optical emission galaxy
    if fB > 0.25 and fR > 0.25 and fZ < 0.25:
        lines = ["[OIII] 5007", "H-beta", "H-alpha"]
        return "EMISSION_LINE_GALAXY", lines, "medium"

    # Red + Z but not B → intermediate/high-z emitter
    if fR > 0.25 and fZ > 0.25 and fB < 0.25:
        lines = ["H-alpha", "CaII 8542"]
        return "REDSHIFTED_EMITTER", lines, "low"

    return "UNCATEGORIZED", [], "low"


# ── Random Forest classifier (trained on SDSS classes when available) ─────

def train_rf_classifier(df):
    """
    Train a random forest on the subset of anomalies that have SDSS
    spectral class labels (from the 'class' column in the parquet files).
    Uses rB, rR, rZ, anomaly_score, and first 16 latent dims as features.

    Returns (model, label_encoder) or (None, None) if insufficient data.
    """
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder

    if "class" not in df.columns:
        return None, None

    labeled = df[df["class"].notna() & (df["class"] != "") & (df["class"] != "0")]
    if len(labeled) < 100:
        print(f"  Only {len(labeled)} labeled rows — skipping RF training")
        return None, None

    lat_16 = [f"lat_{i:03d}" for i in range(16)]
    feature_cols = ["rB", "rR", "rZ", "anomaly_score"] + lat_16
    avail = [c for c in feature_cols if c in df.columns]

    X = labeled[avail].values.astype(np.float32)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

    le = LabelEncoder()
    y = le.fit_transform(labeled["class"].astype(str).values)

    print(f"  Training RF on {len(labeled):,} labeled objects, "
          f"{len(le.classes_)} classes: {list(le.classes_)}")

    rf = RandomForestClassifier(
        n_estimators=200, max_depth=12, min_samples_leaf=5,
        n_jobs=-1, random_state=42, class_weight="balanced",
    )
    rf.fit(X, y)

    # Quick accuracy check
    train_acc = rf.score(X, y)
    print(f"  RF train accuracy: {train_acc:.3f}")

    return rf, le, avail


def predict_rf(rf, le, avail, df):
    """Apply trained RF to all rows. Returns predicted class + probability."""
    X = df[avail].values.astype(np.float32)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

    preds = rf.predict(X)
    probs = rf.predict_proba(X).max(axis=1)

    return le.inverse_transform(preds), probs


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t0 = time.time()

    print("=" * 65)
    print("EMISSION LINE FINDER — SDSS Anomaly Classification")
    print("=" * 65)

    # ── Load checkpoint ────────────────────────────────────────────────
    if os.path.exists(CKPT_PATH):
        with open(CKPT_PATH) as f:
            ckpt = json.load(f)
        if ckpt.get("status") == "COMPLETE":
            print("Already complete — remove checkpoint.json to re-run.")
            return
        print(f"Resuming from checkpoint: {ckpt.get('files_loaded', 0)} files done")
    else:
        ckpt = {"files_loaded": 0, "status": "RUNNING"}

    # ── Load parquet files ─────────────────────────────────────────────
    files = sorted(glob.glob(f"{DATA_DIR}/sdss_batch_*.parquet"))
    print(f"Found {len(files)} parquet files in {DATA_DIR}")
    if not files:
        sys.exit("ERROR: no sdss_batch_*.parquet found — check DATA_DIR")

    id_cols  = ["plate", "mjd", "fiberid"]
    band_cols = ["rB", "rR", "rZ"]
    lat_cols = [f"lat_{i:03d}" for i in range(128)]
    # Try to load 'class' column if present (SDSS spectral class label)
    optional_cols = ["class", "z", "ra", "dec", "zwarning"]

    # Probe first file for available columns
    probe_schema = pq.read_schema(files[0])
    probe_names = set(probe_schema.names)
    want_cols = id_cols + ["anomaly_score"] + band_cols + lat_cols
    want_cols += [c for c in optional_cols if c in probe_names]

    chunks = []
    for i, fpath in enumerate(files):
        if i < ckpt.get("files_loaded", 0):
            continue
        tbl = pq.read_table(fpath, columns=[c for c in want_cols
                                             if c in probe_names])
        chunk = tbl.to_pandas()
        chunk = chunk[chunk["anomaly_score"] > ANOMALY_THRESHOLD]
        chunks.append(chunk)
        if (i + 1) % 10 == 0 or i == len(files) - 1:
            n_so_far = sum(len(c) for c in chunks)
            print(f"  Loaded {i+1}/{len(files)} | anomalies: {n_so_far:,}")

    if not chunks:
        print("No new data to process.")
        return

    df = pd.concat(chunks, ignore_index=True)
    print(f"\nTotal anomalies (score > {ANOMALY_THRESHOLD}): {len(df):,}")
    sys.stdout.flush()

    # Sanitise band columns
    for col in band_cols:
        df[col] = df[col].replace([np.inf, -np.inf], np.nan).fillna(0.0)

    # ── Step 1: Rule-based classification ──────────────────────────────
    print("\nStep 1: Rule-based classification by band residuals...")

    categories, likely_lines_list, confidences = [], [], []
    for _, row in df.iterrows():
        cat, lines, conf = classify_residual_pattern(
            row["rB"], row["rR"], row["rZ"], row["anomaly_score"]
        )
        categories.append(cat)
        likely_lines_list.append("|".join(lines) if lines else "")
        confidences.append(conf)

    df["rule_category"] = categories
    df["likely_lines"] = likely_lines_list
    df["rule_confidence"] = confidences

    # Print category summary
    cat_counts = df["rule_category"].value_counts()
    print(f"\n{'CATEGORY':<30} {'COUNT':>8} {'%':>7}")
    print("-" * 48)
    for cat, cnt in cat_counts.items():
        print(f"  {cat:<28} {cnt:>8,} {cnt/len(df)*100:>6.1f}%")
    sys.stdout.flush()

    # ── Step 2: Random Forest (if labels available) ────────────────────
    print("\nStep 2: Random Forest classifier...")
    rf_result = train_rf_classifier(df)
    if rf_result is not None and rf_result[0] is not None:
        rf, le, avail = rf_result
        rf_preds, rf_probs = predict_rf(rf, le, avail, df)
        df["rf_class"] = rf_preds
        df["rf_prob"] = rf_probs
        print(f"  RF predictions applied to {len(df):,} rows")

        # RF class distribution
        rf_counts = df["rf_class"].value_counts()
        print(f"\n  RF class distribution:")
        for cls, cnt in rf_counts.items():
            print(f"    {cls:<20} {cnt:>8,} ({cnt/len(df)*100:.1f}%)")
    else:
        df["rf_class"] = ""
        df["rf_prob"] = 0.0
        print("  No RF model trained (missing or insufficient class labels)")
    sys.stdout.flush()

    # ── Step 3: Cross-reference with emission line wavelengths ─────────
    print("\nStep 3: Emission line wavelength cross-reference...")

    # For each anomaly, find which band dominates and list the likely
    # emission lines that could produce excess in that band
    dominant_bands, primary_lines = [], []
    for _, row in df.iterrows():
        vals = {"rB": row["rB"], "rR": row["rR"], "rZ": row["rZ"]}
        dom = max(vals, key=vals.get)
        dominant_bands.append(dom)

        # Top line in the dominant band sorted by prominence
        band_lines = LINES_BY_BAND[dom]
        if band_lines:
            # Pick the strongest expected line for this band
            primary_lines.append(list(band_lines.keys())[0])
        else:
            primary_lines.append("")

    df["dominant_band"] = dominant_bands
    df["primary_line_candidate"] = primary_lines

    # Line candidate distribution
    line_counts = df["primary_line_candidate"].value_counts()
    print(f"\n{'PRIMARY LINE CANDIDATE':<30} {'COUNT':>8}")
    print("-" * 40)
    for line, cnt in line_counts.head(15).items():
        print(f"  {line:<28} {cnt:>8,}")
    sys.stdout.flush()

    # ── Step 4: Save outputs ───────────────────────────────────────────
    print("\nSaving outputs...")

    # 4a. Classified parquet
    out_cols = (id_cols + ["anomaly_score"] + band_cols
                + ["rule_category", "likely_lines", "rule_confidence",
                   "dominant_band", "primary_line_candidate",
                   "rf_class", "rf_prob"])
    # Include z, ra, dec if available
    for c in ["z", "ra", "dec", "class"]:
        if c in df.columns:
            out_cols.append(c)

    out_parquet = os.path.join(OUT_DIR, "classified_anomalies.parquet")
    df[out_cols].to_parquet(out_parquet, index=False, engine="pyarrow")
    print(f"  {out_parquet} ({len(df):,} rows)")

    # 4b. Summary JSON
    elapsed = time.time() - t0

    # Build per-category stats
    cat_stats = []
    for cat in cat_counts.index:
        sub = df[df["rule_category"] == cat]
        cat_stats.append({
            "category": cat,
            "count": int(len(sub)),
            "fraction": round(len(sub) / len(df), 5),
            "median_score": round(float(sub["anomaly_score"].median()), 3),
            "median_rB": round(float(sub["rB"].median()), 5),
            "median_rR": round(float(sub["rR"].median()), 5),
            "median_rZ": round(float(sub["rZ"].median()), 5),
            "top_line": sub["primary_line_candidate"].mode().iloc[0]
                        if len(sub) > 0 else "",
        })

    summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_seconds": round(elapsed, 1),
        "input_files": len(files),
        "anomaly_threshold": ANOMALY_THRESHOLD,
        "total_anomalies": len(df),
        "category_counts": {cat: int(cnt) for cat, cnt in cat_counts.items()},
        "line_candidate_counts": {k: int(v) for k, v in
                                   line_counts.head(20).items()},
        "rf_trained": bool(rf_result and rf_result[0] is not None),
        "rf_classes": list(df["rf_class"].unique()) if "rf_class" in df.columns
                      else [],
        "band_ranges_angstrom": BAND_RANGES,
        "known_lines_count": len(KNOWN_LINES),
        "categories": cat_stats,
    }

    summary_path = os.path.join(OUT_DIR, "emission_line_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  {summary_path}")

    # 4c. Checkpoint
    with open(CKPT_PATH, "w") as f:
        json.dump({
            "status": "COMPLETE",
            "files_loaded": len(files),
            "total_anomalies": len(df),
            "elapsed_seconds": round(elapsed, 1),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }, f, indent=2)
    print(f"  {CKPT_PATH}")

    # ── Final report ───────────────────────────────────────────────────
    print(f"\n{'=' * 65}")
    print(f"COMPLETE: {len(df):,} anomalies classified in {elapsed:.1f}s")
    print(f"{'=' * 65}")
    print(f"\nCategory breakdown:")
    for cat, cnt in cat_counts.items():
        print(f"  {cat:<30} {cnt:>8,}")
    print(f"\nOutputs in: {OUT_DIR}/")
    print(f"  classified_anomalies.parquet — full classified table")
    print(f"  emission_line_summary.json   — statistics + category details")
    print(f"  checkpoint.json              — completion state")


if __name__ == "__main__":
    main()
