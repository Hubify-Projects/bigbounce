#!/usr/bin/env python3
"""Execute the public P1B BBN setting through CAMB 1.6.5."""

from __future__ import annotations

import hashlib
from pathlib import Path

import camb
import camb.bbn
import numpy as np
import yaml


ROOT = Path(__file__).resolve().parent
YAMLS = (
    "cobaya_planck.yaml",
    "cobaya_planck_bao.yaml",
    "cobaya_planck_bao_sn.yaml",
    "cobaya_full_tension.yaml",
)
TABLE = "PRIMAT_Yp_DH_ErrorMC_2021.dat"
TABLE_SHA256 = "ea5adce061720b937d8abda3a04a384aedaab3168dbf17414ff600cc91a7160c"


def main() -> None:
    assert camb.__version__ == "1.6.5", f"expected CAMB 1.6.5, got {camb.__version__}"
    assert camb.bbn.default_interpolation_table == TABLE
    table_path = Path(camb.__file__).resolve().parent / TABLE
    assert hashlib.sha256(table_path.read_bytes()).hexdigest() == TABLE_SHA256

    table = np.loadtxt(table_path)
    assert (float(table[:, 0].min()), float(table[:, 0].max())) == (0.005, 0.04)
    assert (float(table[:, 2].min()), float(table[:, 2].max())) == (-3.0, 7.0)

    for name in YAMLS:
        config = yaml.safe_load((ROOT / name).read_text())
        extra_args = config["theory"]["camb"]["extra_args"]
        assert extra_args["bbn_predictor"] == TABLE
        params = camb.CAMBparams()
        params.set_cosmology(
            H0=67.4,
            ombh2=0.0224,
            omch2=0.12,
            tau=0.054,
            nnu=3.044,
            num_massive_neutrinos=extra_args["num_massive_neutrinos"],
            theta_H0_range=extra_args["theta_H0_range"],
            bbn_predictor=extra_args["bbn_predictor"],
        )
        loaded = Path(params.bbn_predictor.interpolation_table)
        assert loaded.name == TABLE
        assert hashlib.sha256(loaded.read_bytes()).hexdigest() == TABLE_SHA256
        print(f"PASS {name}: CAMB {camb.__version__} loaded {loaded.name}")


if __name__ == "__main__":
    main()
