#!/usr/bin/env python3
"""Row 16(i-b) figure: z per cut/leg (left) + dipole axes on the sky (right)."""
import json
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

d = json.load(open("row16ib_axis_shift.json"))
rows = [(k, v) for k, v in list(d["qc_sweep"].items()) + list(d["legs"].items())
        + list(d["galactic_cuts"].items()) if v.get("status") == "OK"]
fig = plt.figure(figsize=(13, 6.5))
ax = fig.add_subplot(1, 2, 1)
z = [v["z"] for _, v in rows]
ax.barh(range(len(rows)), z, color=["#c0392b" if x < 2 else "#2c7fb8" for x in z])
ax.set_yticks(range(len(rows))); ax.set_yticklabels([k for k, _ in rows], fontsize=7)
ax.axvline(2, ls="--", c="k", lw=1); ax.invert_yaxis()
ax.set_xlabel("z (fixed-occupancy label-shuffle null)")
ax.set_title("Row 16(i-b): graded QC sweep + imaging legs\n(red = z<2, signal removed)", fontsize=10)
ax2 = fig.add_subplot(1, 2, 2, projection="mollweide")
for k, v in rows:
    r = np.radians(((v["axis_ra_deg"] + 180) % 360) - 180)
    ax2.plot(r, np.radians(v["axis_dec_deg"]), "o",
             ms=9 if k in d["qc_sweep"] else 4,
             color="#c0392b" if v["z"] < 2 else "#2c7fb8", alpha=0.85)
    if k in d["qc_sweep"]:
        ax2.annotate(k, (r, np.radians(v["axis_dec_deg"])), fontsize=7, xytext=(4, 4), textcoords="offset points")
ax2.grid(True, alpha=0.3)
ax2.set_title("Best-fit dipole axes (equatorial)\nC0 vs C3 separation = %.0f deg" % d["axis_separations_deg"]["C0_vs_C3"], fontsize=10)
fig.tight_layout(); fig.savefig("fig_row16ib_axis_shift.png", dpi=150)
print("wrote fig_row16ib_axis_shift.png")
