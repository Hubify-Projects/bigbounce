#!/usr/bin/env python3
"""
gen_fig_injection_recovery.py

R1 closure item R5 (self-containedness restoration, Route A item 8):
plots the committed observed-label injection-recovery curve underlying
Eq. eq:a95_obs (A_95^obs=0.98%). Reads ONLY the already-committed P4 JSON
artifact (no new inference, no re-run of the ViT classifier or the
injection sweep):

    pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.json

Writes pipelines/p4prime_chirality_test/paper/fig_injection_recovery.png
(P4'-local only; does not touch the P4 source repo).
"""

from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman", "Computer Modern Roman"],
    "savefig.dpi": 300,
    "figure.dpi": 300,
})

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
SRC = REPO / "pipelines" / "p2_chirality" / "analysis" / "a95_observed_label_upper_limit_v1_0_265.json"
OUT = HERE / "fig_injection_recovery.png"


def main() -> None:
    d = json.loads(SRC.read_text())
    pa = d["per_amplitude"]
    amps = [p["A_injected_pct"] for p in pa]
    det = [p["detection_fraction"] for p in pa]
    a95 = d["A95_obs_pct"]

    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.plot(amps, det, "o-", color="#1e3a5f", markersize=4, linewidth=1.3,
            label="recovered detection probability")
    ax.axhline(0.95, linestyle="--", color="#94a3b8", linewidth=1.0,
                label="95% coverage")
    ax.axvline(a95, linestyle=":", color="#dc2626", linewidth=1.2,
                label=f"$A_{{95}}^{{\\rm obs}}={a95:.2f}\\%$")
    ax.axvline(0.467, linestyle="-.", color="#16a34a", linewidth=1.2,
                label="observed $A_{\\rm dip}=0.467\\%$")
    ax.set_xlabel("injected full-amplitude $A$ (%)", fontsize=10)
    ax.set_ylabel("detection probability\n(one-sided rank $p<0.05$)", fontsize=10)
    ax.set_title("Observed-label injection--recovery,\nprimary $\\HCRI$ channel"
                  .replace("\\HCRI", "HC-RI"), fontsize=10.5)
    ax.set_xlim(0.3, 2.05)
    ax.set_ylim(0, 1.03)
    ax.legend(loc="lower right", fontsize=7.5, frameon=True)
    fig.tight_layout()
    fig.savefig(OUT, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
