#!/usr/bin/env python3
"""Ledger row 4: the pre-registered LRG-vs-QSO comparison (PRE_REGISTRATION
section 5). Decision rule fixed before any number was seen:
|T| < 2 AGREE, 2 <= |T| < 3 MILD TENSION, |T| >= 3 TENSION, with
T = (f_LRG - f_QSO)/sqrt(sigma_LRG^2 + sigma_QSO^2) at matched p and the two
channels treated as independent (disclosed: shared-volume correlation is not
modelled, which makes T conservative toward finding tension).
"""
import json

import numpy as np

from lrg_fit_core import interval

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction"
OUT = f"{HERE}/lrg_channel_2026_09_22/outputs"

# QSO headline, v3 (unchanged through v4/v5): outputs/fnl_official_nshot0_summary.json
QSO = json.load(open(f"{HERE}/outputs/fnl_official_nshot0_summary.json"))
QSO_MAP = {"1.0": QSO["p10"], "1.6": QSO["p16"]}
PUBLISHED = dict(label="Chaussidon et al. 2024 (arXiv:2411.17623), LRG+QSO",
                 f_nl=-3.6, sigma_hi=9.0, sigma_lo=9.1)
BROWN = dict(label="Brown et al. 2026 (arXiv:2606.24651), 2pcf",
             f_nl=-3.0, sigma=12.0)
FLAGSHIP = {"-35/16": -35.0 / 16.0, "-35/8 (superseded)": -35.0 / 8.0}


def rule(t):
    a = abs(t)
    return "AGREE" if a < 2 else ("MILD TENSION" if a < 3 else "TENSION")


def main():
    lrg = json.load(open(f"{OUT}/fnl_lrg_headline.json"))
    out = {"comparisons": {}, "discrimination": {}, "published": {}}
    for p in ("1.0", "1.6"):
        L = lrg["p"][p]["combined"]
        Q = QSO_MAP[p]
        t = (L["f_nl"] - Q["f_nl"]) / np.sqrt(L["sigma"] ** 2 + Q["sigma_fnl"] ** 2)
        out["comparisons"][p] = dict(
            lrg_f_nl=L["f_nl"], lrg_sigma=L["sigma"],
            qso_f_nl=Q["f_nl"], qso_sigma=Q["sigma_fnl"],
            T=float(t), verdict=rule(t))
        sp = PUBLISHED["sigma_lo"] if L["f_nl"] < PUBLISHED["f_nl"] else PUBLISHED["sigma_hi"]
        out["published"][p] = dict(
            target=PUBLISHED["label"], f_nl=PUBLISHED["f_nl"],
            T_vs_published=float((L["f_nl"] - PUBLISHED["f_nl"]) /
                                 np.sqrt(L["sigma"] ** 2 + sp ** 2)),
            T_vs_brown=float((L["f_nl"] - BROWN["f_nl"]) /
                             np.sqrt(L["sigma"] ** 2 + BROWN["sigma"] ** 2)))
        out["discrimination"][p] = {
            name: dict(value=v,
                       distance_in_lrg_sigma=float((L["f_nl"] - v) / L["sigma"]))
            for name, v in FLAGSHIP.items()}
        out["discrimination"][p]["separation_of_the_two_in_lrg_sigma"] = float(
            abs(FLAGSHIP["-35/16"] - FLAGSHIP["-35/8 (superseded)"]) / L["sigma"])
    # Published-sample-matched sub-combination. Chaussidon+2024's LRG PNG
    # sample is 0.6 < z < 1.1 (this lane's own count in that range,
    # 1,631,715, matches their quoted 1,631,716 to one object -- the
    # difference is a strict vs inclusive edge cut). The pre-registered
    # headline stays the three-bin combination; this second number is
    # reported ALONGSIDE it, not instead of it, so the comparison with the
    # published constraint is made on the published sample definition.
    for p in ("1.0", "1.6"):
        curves = []
        for zb in ("0.6-0.8", "0.8-1.1"):
            g, c = np.load(f"{OUT}/profile_LRG_p{float(p)}_{zb}.npy")
            curves.append(c)
        tot = sum(curves)
        best, lo, hi, sig = interval(g, tot)
        Q = QSO_MAP[p]
        t = (best - Q["f_nl"]) / np.sqrt(sig ** 2 + Q["sigma_fnl"] ** 2)
        sp = PUBLISHED["sigma_lo"] if best < PUBLISHED["f_nl"] else PUBLISHED["sigma_hi"]
        out.setdefault("published_sample_matched_0.6_1.1", {})[p] = dict(
            f_nl=best, sigma=sig, lo_68=lo, hi_68=hi,
            T_vs_qso=float(t), verdict_vs_qso=rule(t),
            T_vs_published=float((best - PUBLISHED["f_nl"]) /
                                 np.sqrt(sig ** 2 + sp ** 2)),
            note="bins z0.6-0.8 + z0.8-1.1 only, matching Chaussidon+2024's LRG "
                 "PNG sample definition; reported alongside the pre-registered "
                 "three-bin headline, never in place of it")

    # per-z-bin internal consistency (same tracer, independent volumes)
    zb = lrg["p"]["1.0"]["bins"]
    keys = list(zb)
    pairs = {}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = zb[keys[i]], zb[keys[j]]
            pairs[f"{keys[i]} vs {keys[j]}"] = float(
                (a["f_nl"] - b["f_nl"]) / np.sqrt(a["sigma"] ** 2 + b["sigma"] ** 2))
    out["internal_zbin_consistency_p1.0"] = pairs
    json.dump(out, open(f"{OUT}/lrg_vs_qso.json", "w"), indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
