#!/usr/bin/env python3
"""Deterministic spectator-conditioned ALP prior-predictive calculation.

Draws the same theta_i/log10(m/eV) priors used by the existing unconditional
Paper 1B calculation, evaluates the committed nonlinear ALP equation once per
draw, and derives both the fixed-C and broad-C arms from that shared trajectory.
The result reports unrestricted, joint spectator-and-band, and explicitly
conditioned P(band | Omega_a < 0.01) frequencies without likelihood weighting.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import multiprocessing as mp
import os
import platform
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
ALP_DIR = REPO / "research/branch_R_alp_birefringence/phase2_mcmc"
sys.path.insert(0, str(ALP_DIR))

import alp_ode as ALP  # noqa: E402

SCHEMA_VERSION = 1
N_DRAWS = 100_000
SEED = 1234
THETA_RANGE = (0.01, math.pi)
LOG10M_RANGE = (-35.0, -30.0)
C_RANGE = (4.0, 60.0)
FIXED_C = 8.0
BETA_OBS_DEG = 0.342
SIGMA_BETA_DEG = 0.094
OMEGA_SPECTATOR_MAX = 0.01
DEFAULT_RESULT = HERE / "alp_spectator_conditioned_prior_predictive_result.json"
DEFAULT_RECEIPT = HERE / "alp_spectator_conditioned_prior_predictive_receipt.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def generate_draws(n_draws: int, seed: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Match the existing seed/order: theta, log-mass, then broad coupling."""
    rng = np.random.default_rng(seed)
    theta = rng.uniform(*THETA_RANGE, n_draws)
    log10m = rng.uniform(*LOG10M_RANGE, n_draws)
    broad_c = rng.uniform(*C_RANGE, n_draws)
    return theta, log10m, broad_c


def trajectory_fast(pair: tuple[float, float]) -> tuple[float, float]:
    """Return (delta_theta, Omega_a today) from the committed EOM."""
    theta_i, log10m = pair
    mass = 10.0**log10m
    ln_a_start = -np.log(1.0 + 3000.0)
    ln_a_rec = -np.log(1.0 + ALP.Z_REC)
    solution = solve_ivp(
        ALP._ode_rhs_lna,
        [ln_a_start, 0.0],
        [theta_i, 0.0],
        args=(mass, ALP.H0_EV, 0.315),
        method="DOP853",
        rtol=1e-7,
        atol=1e-10,
        dense_output=True,
    )
    if not solution.success:
        return math.nan, math.nan
    theta_rec = solution.sol(ln_a_rec)[0]
    theta_0, dtheta_dlna_0 = solution.sol(0.0)
    delta_theta = theta_rec - theta_0
    theta_dot_0 = dtheta_dlna_0 * ALP.H0_EV
    kinetic = 0.5 * ALP.M_PL_EV**2 * theta_dot_0**2
    potential = mass**2 * ALP.M_PL_EV**2 * (1.0 - np.cos(theta_0))
    omega_a = (kinetic + potential) / (3.0 * ALP.H0_EV**2 * ALP.M_PL_EV**2)
    return float(delta_theta), float(omega_a)


def beta_from_delta(delta_theta: np.ndarray, coupling: np.ndarray | float) -> np.ndarray:
    return np.degrees(np.asarray(coupling) * ALP.ALPHA_EM * delta_theta / (4.0 * np.pi))


def binomial_se(fraction: float, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return math.sqrt(fraction * (1.0 - fraction) / denominator)


def wilson_interval(successes: int, total: int, z: float = 1.959963984540054) -> list[float] | None:
    if total == 0:
        return None
    p = successes / total
    denominator = 1.0 + z * z / total
    centre = (p + z * z / (2.0 * total)) / denominator
    half = z * math.sqrt(p * (1.0 - p) / total + z * z / (4.0 * total**2)) / denominator
    return [centre - half, centre + half]


def summarize(beta: np.ndarray, omega_a: np.ndarray) -> dict:
    finite = np.isfinite(beta) & np.isfinite(omega_a)
    in_band = np.abs(beta - BETA_OBS_DEG) < SIGMA_BETA_DEG
    spectator = omega_a < OMEGA_SPECTATOR_MAX
    n_valid = int(np.count_nonzero(finite))
    n_band = int(np.count_nonzero(finite & in_band))
    n_spectator = int(np.count_nonzero(finite & spectator))
    n_joint = int(np.count_nonzero(finite & spectator & in_band))
    unrestricted = n_band / n_valid
    spectator_prior = n_spectator / n_valid
    joint = n_joint / n_valid
    conditioned = n_joint / n_spectator if n_spectator else math.nan
    return {
        "n_valid": n_valid,
        "n_failed": int(len(beta) - n_valid),
        "n_within_1sigma_unrestricted": n_band,
        "n_spectator_omega_a_lt_0p01": n_spectator,
        "n_joint_within_1sigma_and_spectator": n_joint,
        "fraction_within_1sigma_unrestricted": unrestricted,
        "mc_se_unrestricted": binomial_se(unrestricted, n_valid),
        "fraction_spectator_in_prior": spectator_prior,
        "mc_se_spectator_in_prior": binomial_se(spectator_prior, n_valid),
        "fraction_joint_within_1sigma_and_spectator": joint,
        "mc_se_joint": binomial_se(joint, n_valid),
        "fraction_within_1sigma_given_spectator": conditioned,
        "mc_se_conditioned": binomial_se(conditioned, n_spectator),
        "wilson95_conditioned": wilson_interval(n_joint, n_spectator),
    }


def validate_fast_against_reference(n_validate: int = 40, seed: int = 20260715) -> dict:
    rng = np.random.default_rng(seed)
    max_beta = 0.0
    max_omega = 0.0
    classification_mismatches = 0
    for _ in range(n_validate):
        theta_i = float(rng.uniform(*THETA_RANGE))
        log10m = float(rng.uniform(*LOG10M_RANGE))
        coupling = float(rng.uniform(*C_RANGE))
        delta, omega_fast = trajectory_fast((theta_i, log10m))
        beta_fast = float(beta_from_delta(np.array([delta]), coupling)[0])
        reference = ALP.compute_alp_birefringence(theta_i, log10m, C_agamma=coupling)
        max_beta = max(max_beta, abs(beta_fast - reference["beta_deg"]))
        max_omega = max(max_omega, abs(omega_fast - reference["Omega_a"]))
        classification_mismatches += int(
            (omega_fast < OMEGA_SPECTATOR_MAX)
            != (reference["Omega_a"] < OMEGA_SPECTATOR_MAX)
        )
    return {
        "n": n_validate,
        "seed": seed,
        "reference": "alp_ode.compute_alp_birefringence (rtol=1e-10, max_step=0.05)",
        "fast": "same _ode_rhs_lna with DOP853 rtol=1e-7, atol=1e-10",
        "max_abs_beta_deg": max_beta,
        "max_abs_omega_a": max_omega,
        "spectator_classification_mismatches": classification_mismatches,
    }


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
        ).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-draws", type=int, default=N_DRAWS)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--workers", type=int, default=max(1, min(8, os.cpu_count() or 1)))
    parser.add_argument("--chunksize", type=int, default=100)
    parser.add_argument("--result", type=Path, default=DEFAULT_RESULT)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--validate-n", type=int, default=40)
    args = parser.parse_args()
    if args.n_draws <= 0 or args.workers <= 0 or args.validate_n <= 0:
        parser.error("n-draws, workers, and validate-n must be positive")

    started = time.monotonic()
    theta, log10m, broad_c = generate_draws(args.n_draws, args.seed)
    tasks = zip(theta.tolist(), log10m.tolist())
    context = mp.get_context("fork" if "fork" in mp.get_all_start_methods() else "spawn")
    with context.Pool(args.workers) as pool:
        trajectories = np.asarray(
            pool.map(trajectory_fast, tasks, chunksize=args.chunksize), dtype=float
        )
    delta_theta, omega_a = trajectories[:, 0], trajectories[:, 1]
    beta_broad = beta_from_delta(delta_theta, broad_c)
    beta_fixed = beta_from_delta(delta_theta, FIXED_C)
    validation = validate_fast_against_reference(args.validate_n)
    runtime = time.monotonic() - started

    result = {
        "schema_version": SCHEMA_VERSION,
        "status": "pre-release scientific artifact; immutable release tag/DOI pending",
        "description": (
            "Unconditional and Omega_a<0.01-conditioned prior-predictive "
            "frequencies from the committed fixed-background ALP equations"
        ),
        "n_draws_per_arm": args.n_draws,
        "seed": args.seed,
        "draw_order": ["theta_i", "log10_m_eV", "C_agamma_broad"],
        "shared_trajectories_across_arms": True,
        "priors": {
            "theta_i": {"distribution": "uniform", "range": list(THETA_RANGE)},
            "log10_m_eV": {"distribution": "uniform", "range": list(LOG10M_RANGE)},
            "fixed_coupling": FIXED_C,
            "broad_coupling": {"distribution": "uniform", "range": list(C_RANGE)},
            "f_a": "reduced M_Pl",
        },
        "selection": {
            "beta_obs_deg": BETA_OBS_DEG,
            "sigma_beta_deg": SIGMA_BETA_DEG,
            "signed_band": "abs(beta-beta_obs) < sigma_beta",
            "spectator": "Omega_a(z=0) < 0.01",
            "likelihood_weighting": False,
        },
        "validation": validation,
        "results": {
            "fixed_C_agamma_8": summarize(beta_fixed, omega_a),
            "broad_C_agamma_uniform_4_60": summarize(beta_broad, omega_a),
        },
        "interpretation": {
            "unrestricted": (
                "fixed-background ALP prior-predictive fraction; not a spectator-model "
                "probability, Bayesian evidence, posterior probability, or prior cost"
            ),
            "conditioned": (
                "Monte Carlo conditional frequency among draws satisfying Omega_a<0.01 "
                "under the same fixed-background equations; not Bayesian evidence or a "
                "self-consistent-background posterior"
            ),
        },
    }
    atomic_json(args.result, result)

    generator = Path(__file__).resolve()
    equation_source = ALP_DIR / "alp_ode.py"
    receipt = {
        "schema_version": 1,
        "status": "pre-release execution receipt; immutable release tag/DOI pending",
        "result_path": args.result.resolve().relative_to(REPO).as_posix(),
        "result_sha256": sha256_file(args.result),
        "generator_path": generator.relative_to(REPO).as_posix(),
        "generator_sha256": sha256_file(generator),
        "equation_source_path": equation_source.relative_to(REPO).as_posix(),
        "equation_source_sha256": sha256_file(equation_source),
        "repository_head_context": git_head(),
        "n_draws_per_arm": args.n_draws,
        "seed": args.seed,
        "workers": args.workers,
        "chunksize": args.chunksize,
        "runtime_seconds": runtime,
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "platform": platform.platform(),
        },
        "validation": validation,
        "result_counts": {
            name: {
                key: value
                for key, value in summary.items()
                if key.startswith("n_")
            }
            for name, summary in result["results"].items()
        },
    }
    atomic_json(args.receipt, receipt)
    print(json.dumps({
        "result": str(args.result),
        "result_sha256": receipt["result_sha256"],
        "receipt": str(args.receipt),
        "runtime_seconds": runtime,
        "results": result["results"],
    }, indent=2))


if __name__ == "__main__":
    main()
