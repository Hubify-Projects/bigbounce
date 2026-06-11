#!/usr/bin/env python3
"""
fig_theory_map.py — Paper 1 Sec II.0 navigational figure.

Maps the bounce-mechanism layer (LQC, ECH/torsion, matter-bounce, quintom,
Cuscuton, ekpyrotic) on the left to the observable-prediction layer
(ALP β, f_NL = -35/8, PTA γ = 3.0, w0-wa, ΔNeff) on the right, with
arrows showing which mechanism produces which prediction.

ECH is highlighted as "structurally closed (this paper)" with a
strikethrough-style box; matter-bounce is highlighted as "surviving"
with a green box.

Outputs:
  arxiv/fig_theory_map.png
  public/images/p1_theory_map.png

Reviewer driver: R3 Grok Heavy (R42 wave 1) — paper jumps between bounce
mechanisms and prediction channels without a navigational map.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

FIG_W, FIG_H = 9.0, 6.5  # inches; column-width on revtex4-2 twocolumn = 3.4in,
                         # but \columnwidth includegraphics rescales fine.

LEFT_X = 0.18
RIGHT_X = 0.82
BOX_W = 0.30
BOX_H = 0.085
GAP_Y = 0.02

# Mechanism layer (left column) — top to bottom
mechanisms = [
    # (label_top, label_bottom, status_tag, color_face, color_edge)
    ("LQC",
     "holonomy bounce",
     "supplies the bounce equation",
     "#eef4fb", "#3b6ea3"),
    ("ECH / torsion",
     r"$\varepsilon^{abcd}K_{ab}R_{cd}$",
     "structurally closed (this paper)",
     "#fbeaea", "#a33b3b"),
    ("Matter bounce",
     r"$w \approx 0$ contraction",
     "surviving prediction",
     "#eaf6ec", "#3b8a4a"),
    ("Quintom",
     "$w_0w_a$ DE bounce",
     "outside ECH; permitted",
     "#f6f1eb", "#7a5a3b"),
    ("Cuscuton",
     "non-dynamical scalar",
     "outside ECH; permitted",
     "#f6f1eb", "#7a5a3b"),
    ("Ekpyrotic",
     "fast-roll contraction",
     "outside ECH; permitted",
     "#f6f1eb", "#7a5a3b"),
]

# Observable-prediction layer (right column) — top to bottom
predictions = [
    # (label_top, label_bottom, color_face, color_edge)
    (r"ALP $\beta$",
     r"$0.27^\circ$ spectator",
     "#eef4fb", "#3b6ea3"),
    (r"$f_{\rm NL}=-35/8$",
     "SPHEREx, mechanism-indep.",
     "#eaf6ec", "#3b8a4a"),
    (r"PTA $\gamma=3.0$",
     r"v.s. data $2.567\pm0.382$ (P3 §6, real-KDE)",
     "#eef4fb", "#3b6ea3"),
    (r"$w_0w_a$ DE",
     "phenomenological only",
     "#f6eaea", "#a33b3b"),
    (r"$\Delta N_{\rm eff}$",
     r"null: $-0.020\pm0.169$",
     "#eef4fb", "#3b6ea3"),
]

# Arrows: (mech_index, pred_index, style)
#   "ok"  = solid green  — mechanism cleanly produces this prediction
#   "off" = solid gray   — outside-ECH mechanism, but the link is real
#   "x"   = dashed red   — link is structurally closed by this paper
arrows = [
    # LQC supplies the bounce that matter-bounce / quintom / Cuscuton / ekpyrotic
    # all sit on top of; treat its only direct observable as ΔN_eff (radiation
    # after bounce) — main text matches.
    (0, 4, "ok"),
    # ECH:
    #   - cleanly closes w0wa DE  (Sec XV.E + barrier catalog)
    #   - perturbation-transparent → does NOT produce f_NL or β alone
    #   - PTA is matter-bounce-channel, not direct ECH
    (1, 3, "x"),    # ECH ⟶ DE: structurally closed
    # Matter bounce:
    #   - the surviving f_NL prediction
    #   - PTA γ = 3 spectral index
    (2, 1, "ok"),
    (2, 2, "ok"),
    # Quintom:
    #   - directly produces w0wa DE
    (3, 3, "off"),
    # Cuscuton:
    #   - f_NL ≈ 0 (so technically a constraint on f_NL, not a predictor)
    #   - draw to f_NL as "predicts ≈ 0" with off-style
    (4, 1, "off"),
    # Ekpyrotic:
    #   - f_NL O(1-10) local
    (5, 1, "off"),
    # Spectator ALP (independent of bounce mechanism):
    #   - we draw the ALP β arrow from "ECH" with the off-style to make clear
    #     ECH MOTIVATES it but does not derive it.
    (1, 0, "off"),
]


def draw_box(ax, x, y, w, h, label_top, label_bottom, fc, ec,
             strikethrough=False, status_tag=None):
    """Draw a rounded label box with optional strikethrough and status tag."""
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.005,rounding_size=0.012",
        linewidth=1.4, facecolor=fc, edgecolor=ec, zorder=2,
    )
    ax.add_patch(box)

    ax.text(x, y + h * 0.12, label_top, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=ec, zorder=3)
    ax.text(x, y - h * 0.18, label_bottom, ha="center", va="center",
            fontsize=8.5, color="#222", zorder=3)

    if strikethrough:
        ax.plot([x - w / 2 + 0.005, x + w / 2 - 0.005],
                [y, y], color=ec, linewidth=1.6, zorder=4)

    if status_tag:
        ax.text(x, y - h / 2 - 0.014, status_tag, ha="center", va="top",
                fontsize=7.5, style="italic", color=ec, zorder=3)


def draw_arrow(ax, x0, y0, x1, y1, style):
    """Draw a curved arrow between two boxes."""
    if style == "ok":
        color = "#3b8a4a"; ls = "-";  lw = 1.4; alpha = 0.95
    elif style == "off":
        color = "#7a7a7a"; ls = "-";  lw = 1.0; alpha = 0.65
    elif style == "x":
        color = "#a33b3b"; ls = "--"; lw = 1.4; alpha = 0.95
    else:
        color = "#444"; ls = "-"; lw = 1.0; alpha = 0.8

    arrow = FancyArrowPatch(
        (x0, y0), (x1, y1),
        connectionstyle="arc3,rad=0.10",
        arrowstyle="-|>", mutation_scale=10,
        linewidth=lw, color=color, linestyle=ls, alpha=alpha,
        zorder=1,
    )
    ax.add_patch(arrow)


def main():
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=200)
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")

    # Header strip
    ax.text(LEFT_X, 0.965, "Bounce mechanism", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color="#222")
    ax.text(RIGHT_X, 0.965, "Observable prediction", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color="#222")
    ax.plot([LEFT_X - 0.18, LEFT_X + 0.18], [0.94, 0.94], lw=0.6, color="#aaa")
    ax.plot([RIGHT_X - 0.18, RIGHT_X + 0.18], [0.94, 0.94], lw=0.6, color="#aaa")

    # Vertical positions
    n_mech = len(mechanisms); n_pred = len(predictions)
    top_y, bot_y = 0.88, 0.10
    mech_ys = [top_y - i * (top_y - bot_y) / (n_mech - 1) for i in range(n_mech)]
    pred_ys = [top_y - i * (top_y - bot_y) / (n_pred - 1) for i in range(n_pred)]

    # Draw mechanism boxes
    for i, (lt, lb, tag, fc, ec) in enumerate(mechanisms):
        strike = (i == 1)  # ECH gets the strikethrough
        draw_box(ax, LEFT_X, mech_ys[i], BOX_W, BOX_H,
                 lt, lb, fc, ec, strikethrough=strike, status_tag=tag)

    # Draw prediction boxes
    for i, (lt, lb, fc, ec) in enumerate(predictions):
        draw_box(ax, RIGHT_X, pred_ys[i], BOX_W, BOX_H, lt, lb, fc, ec)

    # Draw arrows
    for (mi, pi, style) in arrows:
        x0 = LEFT_X + BOX_W / 2 + 0.005
        x1 = RIGHT_X - BOX_W / 2 - 0.005
        draw_arrow(ax, x0, mech_ys[mi], x1, pred_ys[pi], style)

    # Legend (bottom)
    leg_y = 0.04
    legend_items = [
        ("solid green",  "#3b8a4a", "-",  "produces"),
        ("dashed red",   "#a33b3b", "--", "structurally closed (this paper)"),
        ("solid gray",   "#7a7a7a", "-",  "outside-ECH route"),
    ]
    x_cursor = 0.05
    for _, color, ls, label in legend_items:
        ax.plot([x_cursor, x_cursor + 0.04], [leg_y, leg_y],
                color=color, linewidth=1.6, linestyle=ls)
        ax.text(x_cursor + 0.045, leg_y, label, ha="left", va="center",
                fontsize=8.5, color="#222")
        x_cursor += 0.30

    # Outputs
    here = os.path.dirname(os.path.abspath(__file__))
    arxiv_dir = os.path.dirname(here)
    repo_root = os.path.dirname(arxiv_dir)
    out1 = os.path.join(arxiv_dir, "fig_theory_map.png")
    out2 = os.path.join(repo_root, "public", "images", "p1_theory_map.png")
    os.makedirs(os.path.dirname(out2), exist_ok=True)

    fig.savefig(out1, dpi=200, bbox_inches="tight", facecolor="white")
    fig.savefig(out2, dpi=200, bbox_inches="tight", facecolor="white")
    print(f"Wrote {out1}")
    print(f"Wrote {out2}")


if __name__ == "__main__":
    main()
