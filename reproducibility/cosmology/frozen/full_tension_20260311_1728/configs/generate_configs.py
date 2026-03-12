#!/usr/bin/env python3
"""Generate Cobaya YAML configs for Paper-1 clean restart — 6 chains per dataset."""
import yaml, os, json, hashlib
from datetime import datetime, timezone

BASE = "/workspace/bigbounce"
CHAINS_DIR = f"{BASE}/chains/dneff"
COVMAT_DIR = f"{BASE}/covmats"
CONFIGS_DIR = f"{BASE}/configs"
PACKAGES_PATH = "/workspace/cobaya_packages"

DATASETS = ["full_tension", "planck_only", "planck_bao", "planck_bao_sn"]
N_CHAINS = 6

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

PARAMS = {
    "logA": {
        "prior": {"min": 1.61, "max": 3.91},
        "ref": {"dist": "norm", "loc": 3.044, "scale": 0.014},
        "proposal": 0.001,
        "latex": "\\log(10^{10} A_s)",
        "drop": True,
    },
    "As": {"value": "lambda logA: 1e-10*np.exp(logA)", "latex": "A_s"},
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
    "cosmomc_theta": {"value": "lambda theta_MC_100: 1.e-2*theta_MC_100", "derived": False},
    "H0": {"latex": "H_0 \; [\\mathrm{km/s/Mpc}]", "min": 40, "max": 100},
    "sigma8": {"latex": "\\sigma_8"},
    "omegam": {"latex": "\\Omega_m"},
    "S8": {"derived": "lambda sigma8, omegam: sigma8*np.sqrt(omegam/0.3)", "latex": "S_8"},
    "delta_neff": {"derived": "lambda nnu: nnu - 3.046", "latex": "\\Delta N_\\mathrm{eff}"},
    "age": {"latex": "{\\rm{Age}}/\\mathrm{Gyr}"},
}

def make_seed(dataset, chain_num):
    key = f"bigbounce_paper1_clean_restart_dneff_{dataset}_chain{chain_num:02d}"
    return int(hashlib.sha256(key.encode()).hexdigest()[:8], 16) % (2**31)

seeds = {}
count = 0

for ds in DATASETS:
    seeds[ds] = {}
    covmat_path = f"{COVMAT_DIR}/{ds}.covmat"
    has_covmat = os.path.exists(covmat_path)
    
    for c in range(1, N_CHAINS + 1):
        seed = make_seed(ds, c)
        seeds[ds][f"chain_{c:02d}"] = seed
        
        chain_dir = f"{CHAINS_DIR}/{ds}/chain_{c:02d}"
        os.makedirs(chain_dir, exist_ok=True)
        
        sampler = {
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
                "seed": seed,
            }
        }
        if has_covmat:
            sampler["mcmc"]["covmat"] = covmat_path
        
        config = {
            "theory": THEORY,
            "likelihood": LIKELIHOODS[ds],
            "params": PARAMS,
            "sampler": sampler,
            "output": f"{chain_dir}/spin_torsion",
            "packages_path": PACKAGES_PATH,
        }
        
        config_path = f"{chain_dir}/cobaya_config.yaml"
        with open(config_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        count += 1

# Save seeds
with open(f"{CONFIGS_DIR}/chain_seeds.json", "w") as f:
    json.dump(seeds, f, indent=2)

# Save manifest
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
with open(f"{BASE}/manifests/MANIFEST.md", "w") as f:
    f.write(f"# Paper-1 Clean Restart — Run Manifest\n\n")
    f.write(f"**Generated:** {now}\n")
    f.write(f"**Run ID:** paper1_clean_restart_001\n")
    f.write(f"**Classification:** CLEAN RESTART\n")
    f.write(f"**Model:** ΛCDM + ΔNeff\n")
    f.write(f"**Chains per dataset:** {N_CHAINS}\n")
    f.write(f"**Total chains:** {count}\n\n")
    f.write(f"## Datasets\n")
    for ds in DATASETS:
        f.write(f"- {ds}: chains 01-{N_CHAINS:02d}\n")
    f.write(f"\n## Warm-Start Covmats\n")
    for ds in DATASETS:
        p = f"{COVMAT_DIR}/{ds}.covmat"
        f.write(f"- {ds}: {'YES' if os.path.exists(p) else 'NO'}\n")
    f.write(f"\n## Hardware\n")
    f.write(f"- Pod: CPU5 Compute-Optimized\n")
    f.write(f"- vCPUs: 32\n")
    f.write(f"- RAM: 64 GB\n")
    f.write(f"- Network Volume: 150 GB (EUR-IS-1)\n")
    f.write(f"\n## Provenance\n")
    f.write(f"- All chains are fresh — no imported old chain data\n")
    f.write(f"- Covmats from gpu_run_snapshot_20260305_0824 used as initial proposals only\n")

print(f"Generated {count} Cobaya configs")
print(f"Seeds saved to {CONFIGS_DIR}/chain_seeds.json")
print(f"Manifest saved to {BASE}/manifests/MANIFEST.md")
