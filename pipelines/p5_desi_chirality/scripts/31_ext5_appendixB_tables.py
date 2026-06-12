"""
EXT5 closure: regenerate Appendix B contingency tables from committed artifact
arrays.

Inputs (committed):
  outputs/17_v0151_closure_recomputes.json
    - parent_env_superset.per_class: exact integer (n, n_cw) per V-Web class
      (Filament, Cluster, Wall, Void) on the 812,793-row env-labeled parent
    - T2_contingency_class_x_program.table.{bright,dark}.{void,wall,filament,cluster}:
      exact integer bright/dark cells on the 811,609-row bright+dark subset

Outputs:
  - Prints LaTeX rows + marginal block for tab:contingency_classCWCCW
  - Prints LaTeX rows + marginal block for tab:contingency_classProgram
  - Writes outputs/31_ext5_appendixB_tables.json with the cell values
  - Asserts cell sums equal stated row marginals exactly

Run:
  python3 pipelines/p5_desi_chirality/scripts/31_ext5_appendixB_tables.py
"""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "outputs" / "17_v0151_closure_recomputes.json"
DST = REPO / "outputs" / "31_ext5_appendixB_tables.json"


def fmt_int(n: int) -> str:
    """LaTeX-formatted integer with thin-space thousands separators."""
    s = f"{n:,}".replace(",", "{,}")
    return s


def main() -> None:
    data = json.loads(SRC.read_text())

    per_class = data["parent_env_superset"]["per_class"]
    all_row = data["parent_env_superset"]["ALL"]
    t2 = data["T2_contingency_class_x_program"]["table"]
    n_bd = data["T2_contingency_class_x_program"]["n_bright_plus_dark"]

    # ---------- Table 1: CW/CCW x V-Web class on 812,793-row env-labeled parent
    classes_order = ["filament", "cluster", "wall", "void"]
    rows_cwccw = []
    cw_sum = 0
    ccw_sum = 0
    n_sum = 0
    for cls in classes_order:
        c = per_class[cls]
        n = int(c["n"])
        n_cw = int(c["n_cw"])
        n_ccw = n - n_cw
        f_cw = n_cw / n
        cw_sum += n_cw
        ccw_sum += n_ccw
        n_sum += n
        rows_cwccw.append({
            "class": cls.capitalize(),
            "n": n,
            "n_cw": n_cw,
            "n_ccw": n_ccw,
            "f_cw_exact": f_cw,
        })

    # Marginals MUST sum exactly to ALL row marginals
    assert n_sum == int(all_row["n"]), (n_sum, all_row["n"])
    assert cw_sum == int(all_row["n_cw"]), (cw_sum, all_row["n_cw"])
    assert ccw_sum == int(all_row["n"]) - int(all_row["n_cw"]), (
        ccw_sum, int(all_row["n"]) - int(all_row["n_cw"])
    )

    # ---------- Table 2: V-Web class x bright/dark on 811,609-row subset
    rows_prog = []
    bright_sum = 0
    dark_sum = 0
    n_prog_sum = 0
    for cls in classes_order:
        b = int(t2["bright"][cls])
        d = int(t2["dark"][cls])
        n_bd_cls = b + d
        f_bright = b / n_bd_cls
        bright_sum += b
        dark_sum += d
        n_prog_sum += n_bd_cls
        rows_prog.append({
            "class": cls.capitalize(),
            "n_bright_plus_dark": n_bd_cls,
            "n_bright": b,
            "n_dark": d,
            "f_bright_exact": f_bright,
        })

    assert n_prog_sum == int(n_bd), (n_prog_sum, n_bd)

    # ---------- Print LaTeX rows ----------
    print("% --- tab:contingency_classCWCCW rows (env-labeled parent) ---")
    for r in rows_cwccw:
        print(
            f"{r['class']:<8} & ${fmt_int(r['n'])}$ & ${r['f_cw_exact']:.4f}$ & "
            f"${fmt_int(r['n_cw'])}$ & ${fmt_int(r['n_ccw'])}$ \\\\"
        )
    print(
        f"% Row marginals: n={fmt_int(n_sum)}; CW={fmt_int(cw_sum)}; "
        f"CCW={fmt_int(ccw_sum)}"
    )

    print()
    print("% --- tab:contingency_classProgram rows (bright+dark subset) ---")
    for r in rows_prog:
        print(
            f"{r['class']:<8} & ${fmt_int(r['n_bright_plus_dark'])}$ & "
            f"${r['f_bright_exact']:.4f}$ & "
            f"${fmt_int(r['n_bright'])}$ & ${fmt_int(r['n_dark'])}$ \\\\"
        )
    print(
        f"% Row marginals: n_bright+dark={fmt_int(n_prog_sum)}; "
        f"bright={fmt_int(bright_sum)}; dark={fmt_int(dark_sum)}"
    )

    out = {
        "source_artifact": str(SRC.relative_to(REPO.parent)),
        "tab_contingency_classCWCCW": {
            "n_total": n_sum,
            "cw_total": cw_sum,
            "ccw_total": ccw_sum,
            "rows": rows_cwccw,
        },
        "tab_contingency_classProgram": {
            "n_bright_plus_dark_total": n_prog_sum,
            "bright_total": bright_sum,
            "dark_total": dark_sum,
            "rows": rows_prog,
        },
        "marginal_assertions": "all cell sums match stated row marginals exactly",
    }
    DST.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {DST}")


if __name__ == "__main__":
    main()
