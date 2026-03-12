#!/usr/bin/env python3
"""
Paper-1 Clean Restart — Generate Cobaya YAML Configs

Creates fresh configs for all 32 chains (4 datasets × 4 chains × 2 models).
Uses warm-start covmats from gpu_run_snapshot_20260305_0824.

Usage: python3 paper1_generate_configs.py
"""

import yaml
import os
import hashlib
import json
from datetime import datetime, timezone

CANONICAL_DIR = "/workspace/bigbounce/reproducibility/cosmology/canonical_run_001"
COVMAT_DIR = f"{CANONICAL_DIR}/warm_start_assets/gpu_20260305_covmats"
PACKAGES_PATH = "/workspace/cobaya_packages"

# ── Dataset likelihood definitions ──────────────────────────────────

LIKELIHOODS = {
    "planck_only": {
        "planck_NPIPE_highl_CamSpec.TTTEEE": None,
        "planck_2018_lowl.TT": None,
        "planck_2018_lowl.EE": None,
        "planck_2018_lensing.clik": None,
    },
    "planck_bao": {
        "planck_NPIPE_highl_CamSpec.TTTEEE": None,
        "planck_2018_lowl.TT": None,
        "planck_2018_lowl.EE": None,
        "planck_2018_lensing.clik": None,
        "bao.sdss_dr16_baoplus_lrg": None,
        "bao.sdss_dr16_baoplus_lyauto": None,
        "bao.sdss_dr16_baoplus_lyxqso": None,
        "bao.sdss_dr16_baoplus_qso": None,
        "bao.sdss_dr7_mgs": None,
        "bao.sixdf_2011_bao": None,
    },
    "planck_bao_sn": {
        "planck_NPIPE_highl_CamSpec.TTTEEE": None,
        "planck_2018_lowl.TT": None,
        "planck_2018_lowl.EE": None,
        "planck_2018_lensing.clik": None,
        "bao.sdss_dr16_baoplus_lrg": None,
        "bao.sdss_dr16_baoplus_lyauto": None,
        "bao.sdss_dr16_baoplus_lyxqso": None,
        "bao.sdss_dr16_baoplus_qso": None,
        "bao.sdss_dr7_mgs": None,
        "bao.sixdf_2011_bao": None,
        "sn.pantheonplus": None,
    },
    "full_tension": {
        "planck_NPIPE_highl_CamSpec.TTTEEE": None,
        "planck_2018_lowl.TT": None,
        "planck_2018_lowl.EE": None,
        "planck_2018_lensing.clik": None,
        "bao.sdss_dr16_baoplus_lrg": None,
        "bao.sdss_dr16_baoplus_lyauto": None,
        "bao.sdss_dr16_baoplus_lyxqso": None,
        "bao.sdss_dr16_baoplus_qso": None,
        "bao.sdss_dr7_mgs": None,
        "bao.sixdf_2011_bao": None,
        "sn.pantheonplus": None,
        "H0.riess2020Mb": None,
        "S8_DES": {
            "external": "lambda sigma8, omegam: stats.norm.logpdf(sigma8*np.sqrt(omegam/0.3), loc=0.776, scale=0.017)"
        },
    },
}

# ── Common theory block ─────────────────────────────────────────────

THEORY = {
    "camb": {
        "path": None,
        "extra_args": {
            "lens_potential_accuracy": 1,
            "num_massive_neutrinos": 1,
            "theta_H0_range": [40, 100],
        },
    }
}

# ── Parameter definitions ───────────────────────────────────────────

PARAMS_DNEFF = {
    "logA": {
        "prior": {"min": 1.61, "max": 3.91},
        "ref": {"dist": "norm", "loc": 3.044, "scale": 0.014},
        "proposal": 0.001,
        "latex": "\\log(10^{10} A_s)",
        "drop": True,
    },
    "As": {
        "value": "lambda logA: 1e-10*np.exp(logA)",
        "latex": "A_s",
    },
    "nnu": {
        "prior": {"min": 2.046, "max": 5.046},
        "ref": {"dist": "norm", "loc": 3.346, "scale": 0.2},
        "proposal": 0.05,
        "latex": "N_\\mathrm{eff}",
    },
    "ns": {
        "prior": {"min": 0.8, "max": 1.2},
        "ref": {"dist": "norm", "loc": 0.9649, "scale": 0.0042},
        "proposal": 0.002,
        "latex": "n_s",
    },
    "ombh2": {
        "prior": {"min": 0.005, "max": 0.1},
        "ref": {"dist": "norm", "loc": 0.02237, "scale": 0.00015},
        "proposal": 0.0001,
        "latex": "\\Omega_b h^2",
    },
    "omch2": {
        "prior": {"min": 0.001, "max": 0.99},
        "ref": {"dist": "norm", "loc": 0.12, "scale": 0.0012},
        "proposal": 0.0005,
        "latex": "\\Omega_c h^2",
    },
    "tau": {
        "prior": {"min": 0.01, "max": 0.8},
        "ref": {"dist": "norm", "loc": 0.054, "scale": 0.007},
        "proposal": 0.003,
        "latex": "\\tau_\\mathrm{reio}",
    },
    "theta_MC_100": {
        "prior": {"min": 0.5, "max": 10},
        "ref": {"dist": "norm", "loc": 1.04092, "scale": 0.00031},
        "proposal": 0.0002,
        "latex": "100\\theta_{MC}",
        "drop": True,
        "renames": "theta",
    },
    "cosmomc_theta": {
        "value": "lambda theta_MC_100: 1.e-2*theta_MC_100",
        "derived": False,
    },
    "H0": {
        "latex": "H_0 \\; [\\mathrm{km/s/Mpc}]",
        "min": 40,
        "max": 100,
    },
    "sigma8": {"latex": "\\sigma_8"},
    "omegam": {"latex": "\\Omega_m"},
    "S8": {
        "derived": "lambda sigma8, omegam: sigma8*np.sqrt(omegam/0.3)",
        "latex": "S_8",
    },
    "delta_neff": {
        "derived": "lambda nnu: nnu - 3.046",
        "latex": "\\Delta N_\\mathrm{eff}",
    },
    "age": {"latex": "{\\rm{Age}}/\\mathrm{Gyr}"},
}

# ΛCDM: same but nnu fixed at 3.046
PARAMS_LCDM = {k: v for k, v in PARAMS_DNEFF.items() if k != "delta_neff"}
PARAMS_LCDM["nnu"] = {
    "value": 3.046,
    "latex": "N_\\mathrm{eff}",
}

# ── MCMC sampler settings ──────────────────────────────────────────

def mcmc_settings(covmat_path=None, seed=None):
    s = {
        "mcmc": {
            "Rminus1_stop": 0.01,
            "Rminus1_cl_stop": 0.2,
            "burn_in": 0.1,
            "learn_proposal": True,
            "learn_proposal_Rminus1_max": 50,
            "drag": True,
            "oversample_power": 0.4,
            "proposal_scale": 2.4,
            "max_tries": "40d",
        }
    }
    if covmat_path and os.path.exists(covmat_path):
        s["mcmc"]["covmat"] = covmat_path
    if seed is not None:
        s["mcmc"]["seed"] = seed
    return s


# ── Seed generation ─────────────────────────────────────────────────

def generate_seed(dataset, model, chain_num):
    """Deterministic seed from dataset+model+chain for reproducibility."""
    key = f"bigbounce_paper1_canonical_run_001_{model}_{dataset}_chain{chain_num:02d}"
    return int(hashlib.sha256(key.encode()).hexdigest()[:8], 16) % (2**31)


# ── Config generation ───────────────────────────────────────────────

def generate_config(dataset, model, chain_num):
    """Generate a single Cobaya YAML config."""
    is_dneff = (model == "dneff")
    params = PARAMS_DNEFF if is_dneff else PARAMS_LCDM

    chain_dir = f"{CANONICAL_DIR}/{model}/{dataset}/chain_{chain_num:02d}"
    output_prefix = "spin_torsion" if is_dneff else "lcdm"

    # Find best covmat for this dataset (use chain with most samples from old run)
    # Preference: chain6 > chain5 > chain2 > chain7 > chain4 > chain3
    covmat_path = None
    if is_dneff:
        for old_chain in ["chain6", "chain5", "chain2", "chain7", "chain4", "chain3", ""]:
            suffix = f"_{old_chain}" if old_chain else ""
            candidate = f"{COVMAT_DIR}/{dataset}{suffix}/spin_torsion.covmat"
            if os.path.exists(candidate):
                covmat_path = candidate
                break

    seed = generate_seed(dataset, model, chain_num)

    config = {
        "theory": THEORY,
        "likelihood": LIKELIHOODS[dataset],
        "params": params,
        "sampler": mcmc_settings(covmat_path, seed),
        "output": f"{chain_dir}/{output_prefix}",
        "packages_path": PACKAGES_PATH,
    }

    return config, seed


def main():
    os.makedirs(CANONICAL_DIR, exist_ok=True)

    seeds_record = {}
    configs_created = 0

    for model in ["dneff", "lcdm"]:
        for dataset in ["full_tension", "planck_only", "planck_bao", "planck_bao_sn"]:
            for chain_num in range(1, 5):
                config, seed = generate_config(dataset, model, chain_num)
                chain_dir = f"{CANONICAL_DIR}/{model}/{dataset}/chain_{chain_num:02d}"
                os.makedirs(chain_dir, exist_ok=True)

                config_path = f"{chain_dir}/cobaya_config.yaml"
                with open(config_path, "w") as f:
                    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

                seeds_record.setdefault(model, {})\
                    .setdefault(dataset, {})[f"chain_{chain_num:02d}"] = seed
                configs_created += 1

    # Save seeds record
    seeds_path = f"{CANONICAL_DIR}/chain_seeds.json"
    with open(seeds_path, "w") as f:
        json.dump(seeds_record, f, indent=2)

    # Generate MANIFEST
    manifest_path = f"{CANONICAL_DIR}/MANIFEST.md"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(manifest_path, "w") as f:
        f.write(f"# Canonical Run 001 — MANIFEST\n\n")
        f.write(f"**Generated:** {now}\n")
        f.write(f"**Run ID:** canonical_run_001\n")
        f.write(f"**Classification:** CLEAN RESTART\n\n")
        f.write(f"## Chain Configs Created: {configs_created}\n\n")
        f.write(f"### ΔNeff Model (16 chains)\n")
        for ds in ["full_tension", "planck_only", "planck_bao", "planck_bao_sn"]:
            f.write(f"- {ds}: chains 01-04\n")
        f.write(f"\n### ΛCDM Control (16 chains)\n")
        for ds in ["full_tension", "planck_only", "planck_bao", "planck_bao_sn"]:
            f.write(f"- {ds}: chains 01-04\n")
        f.write(f"\n## Warm-Start Covmats\n")
        f.write(f"- Source: gpu_run_snapshot_20260305_0824\n")
        f.write(f"- Applied to: ΔNeff chains only\n")
        f.write(f"- ΛCDM chains: no covmat (starts with prior proposal)\n")
        f.write(f"\n## Seeds\n")
        f.write(f"See chain_seeds.json for deterministic per-chain seeds.\n")

    print(f"Generated {configs_created} Cobaya configs")
    print(f"Seeds saved to {seeds_path}")
    print(f"Manifest saved to {manifest_path}")


if __name__ == "__main__":
    main()
