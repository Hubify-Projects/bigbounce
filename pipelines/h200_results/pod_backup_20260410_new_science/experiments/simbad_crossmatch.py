"""
SIMBAD/NED Cross-Match of Top Anomaly Candidates
=================================================
Cross-matches high-z QSO anomaly candidates and Gaia anomalies against
SIMBAD (and NED for unmatched sources) to determine:
  - How many are known objects?
  - What are their catalogued types?
  - How many have NO known counterpart (potentially novel)?

Sources:
  1. Top 200 high-z QSO candidates from Pipeline 1 (by anomaly_score)
  2. Top 100 Gaia DR3 anomalies (by anomaly_score, is_top1pct)
"""

import os
import json
import time
import numpy as np
import pandas as pd

try:
    from astroquery.simbad import Simbad
    from astroquery.ipac.ned import Ned
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    HAS_ASTROQUERY = True
except ImportError:
    HAS_ASTROQUERY = False
    print("[warn] astroquery not installed, will pip install")

import subprocess
import sys

OUTPUT_DIR = "/root/results/simbad-crossmatch"
os.makedirs(OUTPUT_DIR, exist_ok=True)

MATCH_RADIUS_ARCSEC = 3.0
TOP_N_QSO = 200
TOP_N_GAIA = 100

# ---------------------------------------------------------------------------
# Data paths
# ---------------------------------------------------------------------------
QSO_CATALOG = "/root/p1_outputs/highz_qso_candidates.csv"
GAIA_CATALOG = "/workspace/bigbounce/backups/20260406_231143/gaia-dr3-expanded/gaia_anomalies.csv"

print("=" * 70)
print("SIMBAD/NED CROSS-MATCH OF ANOMALY CANDIDATES")
print("=" * 70)

# ---------------------------------------------------------------------------
# Install astroquery if needed
# ---------------------------------------------------------------------------
if not HAS_ASTROQUERY:
    print("Installing astroquery...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "astroquery", "-q"])
    from astroquery.simbad import Simbad
    from astroquery.ipac.ned import Ned
    from astropy.coordinates import SkyCoord
    import astropy.units as u

# ---------------------------------------------------------------------------
# Configure SIMBAD
# ---------------------------------------------------------------------------
Simbad.add_votable_fields("otype", "otypes", "rvz_redshift", "V", "bibcodelist")
Simbad.TIMEOUT = 60

# ---------------------------------------------------------------------------
# Load catalogs
# ---------------------------------------------------------------------------
print(f"\n[1/5] Loading catalogs...")
qso_df = pd.read_csv(QSO_CATALOG)
print(f"  QSO candidates: {len(qso_df):,}")
print(f"  QSO columns: {list(qso_df.columns[:8])}")

gaia_df = pd.read_csv(GAIA_CATALOG)
gaia_anom = gaia_df[gaia_df["is_top1pct"] == 1].copy()
print(f"  Gaia total: {len(gaia_df):,}, top 1%: {len(gaia_anom):,}")

# Sort and select top candidates
qso_top = qso_df.nlargest(TOP_N_QSO, "anomaly_score").reset_index(drop=True)
gaia_top = gaia_anom.nlargest(TOP_N_GAIA, "anomaly_score").reset_index(drop=True)

print(f"\n  Selected: {len(qso_top)} QSO + {len(gaia_top)} Gaia anomalies for cross-match")

# ---------------------------------------------------------------------------
# SIMBAD batch cross-match function
# ---------------------------------------------------------------------------
def simbad_batch_query(ra_list, dec_list, names, radius_arcsec=3.0, batch_size=50):
    """Query SIMBAD in batches for each target. Returns DataFrame of matches."""
    results = []
    n = len(ra_list)
    print(f"  Querying SIMBAD for {n} targets (batch_size={batch_size}, r={radius_arcsec}\")...")

    for i in range(0, n, batch_size):
        batch_ra = ra_list[i:i+batch_size]
        batch_dec = dec_list[i:i+batch_size]
        batch_names = names[i:i+batch_size]

        for j, (ra, dec, name) in enumerate(zip(batch_ra, batch_dec, batch_names)):
            result_row = {
                "name": name, "ra": ra, "dec": dec,
                "simbad_match": False, "simbad_name": None,
                "simbad_otype": None, "simbad_otypes": None,
                "simbad_z": None, "simbad_bibcodes": 0,
            }
            try:
                coord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
                result_table = Simbad.query_region(coord, radius=radius_arcsec*u.arcsec)
                if result_table is not None and len(result_table) > 0:
                    row = result_table[0]
                    result_row["simbad_match"] = True
                    result_row["simbad_name"] = str(row["MAIN_ID"])
                    result_row["simbad_otype"] = str(row["OTYPE"])
                    result_row["simbad_otypes"] = str(row.get("OTYPES", ""))
                    result_row["simbad_z"] = float(row["RVZ_REDSHIFT"]) if row["RVZ_REDSHIFT"] and str(row["RVZ_REDSHIFT"]) not in ("", "--", "nan") else None
                    biblist = row.get("BIBCODELIST_2", "")
                    result_row["simbad_bibcodes"] = len(str(biblist).split(",")) if biblist and str(biblist) not in ("", "--") else 0
            except Exception as e:
                result_row["error"] = str(e)[:100]

            results.append(result_row)

        n_done = min(i + batch_size, n)
        n_matched = sum(1 for r in results if r["simbad_match"])
        print(f"    [{n_done}/{n}] {n_matched} matches so far", flush=True)
        time.sleep(0.5)  # Be polite to SIMBAD

    return pd.DataFrame(results)

# ---------------------------------------------------------------------------
# [2/5] Cross-match QSO candidates
# ---------------------------------------------------------------------------
print(f"\n[2/5] SIMBAD cross-match: {len(qso_top)} high-z QSO candidates...")
qso_names = [f"QSO_{i:04d}" for i in range(len(qso_top))]
qso_matches = simbad_batch_query(
    qso_top["ra"].tolist(), qso_top["dec"].tolist(), qso_names, radius_arcsec=MATCH_RADIUS_ARCSEC
)

# Merge with source data
qso_combined = pd.concat([qso_top.reset_index(drop=True), qso_matches.drop(columns=["name","ra","dec"])], axis=1)

# ---------------------------------------------------------------------------
# [3/5] Cross-match Gaia anomalies
# ---------------------------------------------------------------------------
print(f"\n[3/5] SIMBAD cross-match: {len(gaia_top)} Gaia anomalies...")
gaia_names = [f"GAIA_{i:04d}" for i in range(len(gaia_top))]
gaia_matches = simbad_batch_query(
    gaia_top["ra"].tolist(), gaia_top["dec"].tolist(), gaia_names, radius_arcsec=MATCH_RADIUS_ARCSEC
)
gaia_combined = pd.concat([gaia_top.reset_index(drop=True), gaia_matches.drop(columns=["name","ra","dec"])], axis=1)

# ---------------------------------------------------------------------------
# [4/5] NED query for unmatched QSO sources (top 50 unmatched)
# ---------------------------------------------------------------------------
print(f"\n[4/5] NED query for unmatched QSO sources...")
unmatched_qso = qso_combined[~qso_combined["simbad_match"]].head(50)
ned_results = []

for idx, row in unmatched_qso.iterrows():
    ned_row = {"name": f"QSO_{idx:04d}", "ra": row["ra"], "dec": row["dec"],
               "ned_match": False, "ned_name": None, "ned_type": None}
    try:
        coord = SkyCoord(ra=row["ra"]*u.deg, dec=row["dec"]*u.deg)
        ned_table = Ned.query_region(coord, radius=MATCH_RADIUS_ARCSEC*u.arcsec)
        if ned_table is not None and len(ned_table) > 0:
            ned_row["ned_match"] = True
            ned_row["ned_name"] = str(ned_table["Object Name"][0])
            ned_row["ned_type"] = str(ned_table["Type"][0])
    except Exception as e:
        ned_row["ned_error"] = str(e)[:80]
    ned_results.append(ned_row)
    time.sleep(0.3)

ned_df = pd.DataFrame(ned_results)
ned_matched = ned_df["ned_match"].sum() if len(ned_df) else 0
print(f"  NED: {ned_matched}/{len(ned_df)} matched from unmatched QSOs")

# ---------------------------------------------------------------------------
# [5/5] Summary statistics
# ---------------------------------------------------------------------------
print(f"\n[5/5] Summary statistics...")

# QSO matches
qso_n_matched = qso_combined["simbad_match"].sum()
qso_n_novel = (~qso_combined["simbad_match"]).sum()
qso_otype_counts = qso_combined[qso_combined["simbad_match"]]["simbad_otype"].value_counts().head(10)

# Gaia matches
gaia_n_matched = gaia_combined["simbad_match"].sum()
gaia_n_novel = (~gaia_combined["simbad_match"]).sum()
gaia_otype_counts = gaia_combined[gaia_combined["simbad_match"]]["simbad_otype"].value_counts().head(10)

# z comparison for matched QSOs
qso_matched_z = qso_combined[qso_combined["simbad_match"] & qso_combined["simbad_z"].notna()]
z_agreement = None
if len(qso_matched_z) > 0:
    z_diff = np.abs(qso_matched_z["z"] - qso_matched_z["simbad_z"])
    z_agreement = (z_diff < 0.1).mean()

print(f"\n  === QSO CANDIDATES (top {TOP_N_QSO} by anomaly_score) ===")
print(f"  SIMBAD matched: {qso_n_matched} / {len(qso_combined)} ({100*qso_n_matched/len(qso_combined):.1f}%)")
print(f"  NO KNOWN COUNTERPART: {qso_n_novel} ({100*qso_n_novel/len(qso_combined):.1f}%)")
if z_agreement is not None:
    print(f"  Redshift agreement (|Δz|<0.1): {100*z_agreement:.1f}% of matched")
print(f"  Top object types:")
for otype, cnt in qso_otype_counts.items():
    print(f"    {otype}: {cnt}")

print(f"\n  === GAIA ANOMALIES (top {TOP_N_GAIA}) ===")
print(f"  SIMBAD matched: {gaia_n_matched} / {len(gaia_combined)} ({100*gaia_n_matched/len(gaia_combined):.1f}%)")
print(f"  NO KNOWN COUNTERPART: {gaia_n_novel} ({100*gaia_n_novel/len(gaia_combined):.1f}%)")
print(f"  Top object types:")
for otype, cnt in gaia_otype_counts.items():
    print(f"    {otype}: {cnt}")

if ned_matched > 0:
    print(f"\n  NED rescue: {ned_matched} of {qso_n_novel} unmatched QSOs found in NED")
    total_known = qso_n_matched + ned_matched
    true_novel = len(qso_combined) - total_known
    print(f"  TRUE NOVEL (not in SIMBAD or NED): {true_novel} / {len(qso_combined)}")

# ---------------------------------------------------------------------------
# Save results
# ---------------------------------------------------------------------------
print(f"\nSaving results to {OUTPUT_DIR}...")
try:
    qso_combined.to_csv(os.path.join(OUTPUT_DIR, "qso_simbad_matches.csv"), index=False)
    gaia_combined.to_csv(os.path.join(OUTPUT_DIR, "gaia_simbad_matches.csv"), index=False)
    if len(ned_df) > 0:
        ned_df.to_csv(os.path.join(OUTPUT_DIR, "qso_ned_matches.csv"), index=False)
except Exception as e:
    print(f"[warn] CSV save: {e}", flush=True)

summary = {
    "experiment": "SIMBAD/NED Cross-Match of Anomaly Candidates",
    "match_radius_arcsec": MATCH_RADIUS_ARCSEC,
    "qso_results": {
        "total_queried": len(qso_combined),
        "simbad_matched": int(qso_n_matched),
        "simbad_match_rate_pct": round(100*qso_n_matched/len(qso_combined), 1),
        "no_counterpart": int(qso_n_novel),
        "ned_rescue": int(ned_matched),
        "true_novel_estimate": int(qso_n_novel - ned_matched),
        "z_agreement_pct": round(100*z_agreement, 1) if z_agreement is not None else None,
        "top_otypes": qso_otype_counts.to_dict(),
    },
    "gaia_results": {
        "total_queried": len(gaia_combined),
        "simbad_matched": int(gaia_n_matched),
        "simbad_match_rate_pct": round(100*gaia_n_matched/len(gaia_combined), 1),
        "no_counterpart": int(gaia_n_novel),
        "top_otypes": gaia_otype_counts.to_dict(),
    },
}

try:
    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
except Exception as e:
    print(f"[warn] json save: {e}", flush=True)

print(json.dumps(summary, indent=2))
print("\nCOMPLETE")
