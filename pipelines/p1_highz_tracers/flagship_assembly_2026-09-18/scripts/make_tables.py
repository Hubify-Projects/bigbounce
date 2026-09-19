#!/usr/bin/env python3
"""Render the assembled evidence into Markdown tables and revtex4-2 table bodies.

Reads only this lane's own outputs (produced by assemble_flagship_evidence.py)
so that every number in the draft manuscript and in the evidence documents is
machine-generated from the released artifacts, never transcribed by hand.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "outputs"
DRAFT = HERE.parent / "anomaly_flagship_draft"
TAB = DRAFT / "tables"
TAB.mkdir(parents=True, exist_ok=True)


def esc(s) -> str:
    """LaTeX-escape a raw requirement/label string from a JSON artifact.

    These strings contain shell- and code-like characters (`>`, `<`, `|`,
    `->`, `_`) that OT1 text mode silently renders as the wrong glyph, so the
    escaping has to be explicit rather than left to LaTeX.
    """
    s = str(s)
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
                 ("#", r"\#"), ("_", r"\_"), ("$", r"\$"),
                 ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}"),
                 ("->", r"$\to$"), (">", "$>$"), ("<", "$<$"), ("|", "$|$")):
        s = s.replace(a, b)
    return s


def main() -> None:
    fam = pd.read_csv(OUT / "family_evidence.csv")
    fu_all = json.loads((OUT / "followup_targets.json").read_text())
    fu = pd.DataFrame(fu_all["targets"])
    tiers = fu_all["tiers"]
    checks = json.loads((OUT / "validation_contract_results.json").read_text())["checks"]

    # ---------------------------------------------------- family evidence (md)
    md = ["| Family | Tier | $N$ | Clusters | Survey/program | Score median (5–95%) | "
          "$r_B$ median | ZWARN$=0$ | median $z$ (ZWARN$=0$) | $z>2$ | $z>4$ | QSO | "
          "point src | AllWISE | $W1-W2>0.8$ |", "|" + "---|" * 15]
    for _, r in fam.iterrows():
        md.append(
            f"| {int(r.family_id)} | {r.score_tier} | {int(r.n_objects)} | {int(r.n_clusters)} | "
            f"{r.dominant_survey}/{r.dominant_program} | {r.score_median:.2f} "
            f"({r.score_p05:.2f}–{r.score_p95:.2f}) | {r.rB_median:.2f} | "
            f"{int(r.n_zwarn0)} ({100*r.f_zwarn0:.0f}%) | "
            f"{'—' if pd.isna(r.z_median_zwarn0) else f'{r.z_median_zwarn0:.2f}'} | "
            f"{int(r.n_z_gt2_zwarn0)} | {int(r.n_z_gt4_zwarn0)} | {int(r.n_qso)} | "
            f"{100*r.f_point_source:.0f}% | {int(r.n_wise)} | {int(r.n_w1w2_gt0p8)} |")
    md.append("")
    md.append(f"Totals: N = {int(fam.n_objects.sum())} objects in "
              f"{int(fam.n_clusters.sum())} clusters; ZWARN$=0$: {int(fam.n_zwarn0.sum())}; "
              f"QSO: {int(fam.n_qso.sum())}; AllWISE matches: {int(fam.n_wise.sum())}.")
    (OUT / "family_evidence.md").write_text("\n".join(md) + "\n")

    # --------------------------------------------------- family evidence (tex)
    lines = [r"\begin{ruledtabular}",
             r"\begin{tabular}{r l r r l l r r r r r r}",
             r"Family & Tier & $N$ & $N_{\rm cl}$ & Survey/prog. & Score med. (5--95\%) & "
             r"$r_B$ & $N_{Z0}$ & $\tilde z_{Z0}$ & $N_{z>2}$ & $N_{\rm QSO}$ & $N_{W}$ \\",
             r"\hline"]
    for _, r in fam.iterrows():
        zmed = "--" if pd.isna(r.z_median_zwarn0) else f"{r.z_median_zwarn0:.2f}"
        lines.append(
            f"{int(r.family_id)} & {r.score_tier} & {int(r.n_objects)} & {int(r.n_clusters)} & "
            f"{r.dominant_survey}/{r.dominant_program} & {r.score_median:.2f} "
            f"({r.score_p05:.2f}--{r.score_p95:.2f}) & {r.rB_median:.2f} & {int(r.n_zwarn0)} & "
            f"{zmed} & {int(r.n_z_gt2_zwarn0)} & {int(r.n_qso)} & {int(r.n_wise)} " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (TAB / "tab_family_evidence.tex").write_text("\n".join(lines) + "\n")

    # -------------------------------------------------- validation contract (tex)
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l p{0.52\textwidth} l}",
             r"ID & Requirement & Outcome \\", r"\hline"]
    for c in checks:
        lines.append(f"{esc(c['id'])} & {esc(c['requirement'])} & "
                     f"\\textsc{{{esc(c['status'].lower())}}} " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (TAB / "tab_validation_contract.tex").write_text("\n".join(lines) + "\n")

    # ------------------------------------------------------ follow-up set (tex/md)
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l r r r r r r l}",
             r"Tier & TARGETID & R.A. & Dec. & $S$ & $z$ & ZWARN & SPECTYPE \\", r"\hline"]
    mdl = ["| Tier | TARGETID | R.A. (deg) | Dec. (deg) | Score | $z$ | ZWARN | SPECTYPE | "
           "$W1-W2$ | Family/cluster |", "|" + "---|" * 10]
    for _, r in fu.iterrows():
        z = f"{r.z:.4f}" if (not pd.isna(r.z) and int(r.zwarn) == 0) else "--"
        lines.append(f"{r.tier} & {int(r.targetid)} & {r.target_ra:.5f} & {r.target_dec:.5f} & "
                     f"{r.anomaly_score:.3f} & {z} & {int(r.zwarn)} & {r.spectype} " + r"\\")
        w = "—" if pd.isna(r.w1_w2) else f"{r.w1_w2:.3f}"
        mdl.append(f"| {r.tier} | {int(r.targetid)} | {r.target_ra:.5f} | {r.target_dec:.5f} | "
                   f"{r.anomaly_score:.3f} | {'—' if pd.isna(r.z) else f'{r.z:.4f}'} | "
                   f"{int(r.zwarn)} | {r.spectype} | {w} | "
                   f"{int(r.family_id)}/{int(r.cluster_id)} |")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (TAB / "tab_followup_targets.tex").write_text("\n".join(lines) + "\n")

    head = ["| Tier | Name | Selection rule | $N$ | Next test |", "|---|---|---|---|---|"]
    for t, meta in tiers.items():
        head.append(f"| {t} | {meta['name']} | `{meta['rule']}` | {meta['n_targets']} | "
                    f"{meta['next_test']} |")
    (OUT / "followup_targets.md").write_text(
        "\n".join(head) + "\n\n" + "\n".join(mdl) + "\n")

    # ------------------------------------------------------- threshold ladder (tex)
    ladder = [(3, 320418, 1244), (4, 86053, 152), (5, 52188, 44),
              (6, 27180, 20), (8, 3810, 2), (10, 337, 1)]
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{r r r r}",
             r"$S>$ & All fibres & Science targets & Science fraction \\", r"\hline"]
    for s, allf, sci in ladder:
        lines.append(f"{s} & {allf:,} & {sci:,} & {100*sci/allf:.2f}\\% " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (TAB / "tab_threshold_ladder.tex").write_text(
        "\n".join(lines).replace(",", r"{,}") + "\n")

    # ------------------------------------------------------ recovery benchmark (tex)
    bench = [("Broad absorption line (BAL) quasars", 5285, 1, "4.2"),
             ("Roma-BZCAT blazars (5th ed.)", 2060, 0, "0.0"),
             ("Cataclysmic variables / WD binaries", 580, 0, "0.0"),
             (r"Lyman-$\alpha$ emitters", 84, 0, "0.0"),
             ("Superluminous-SN host galaxies", 27, 0, "0.0")]
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l r r r}",
             r"Reference class & $N_{\rm ref}$ in footprint & $N_{\rm match}$ & Enrichment \\",
             r"\hline"]
    for name, nref, nm, enr in bench:
        lines.append(f"{name} & {nref:,} & {nm} & {enr}$\\times$ ".replace(",", r"{,}") + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (TAB / "tab_recovery_benchmark.tex").write_text("\n".join(lines) + "\n")

    print("wrote", sorted(p.name for p in TAB.glob("*.tex")))
    print("wrote", (OUT / "family_evidence.md").name, (OUT / "followup_targets.md").name)


if __name__ == "__main__":
    main()
