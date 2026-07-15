#!/usr/bin/env python3
"""Recompute Paper 1B Table IV directly from the four c5 chain files.

The chain files use integer multiplicity weights.  Reported moments and
quantiles are weighted directly.  The single ESS convention used for every
row is a weight-expanded, per-chain Sokal automatic-window estimate for the
marker parameter ``beta_deg`` (window constant c=5); per-chain ESS values are
summed.  Subsets are filtered before weight expansion while preserving chain
order.  This definition is intentionally explicit because ESS for a
post-selected subset is estimator-dependent.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
CHAIN_DIR = HERE / "chains" / "c5_continuous"
CHAIN_FILES = [CHAIN_DIR / f"c5.{index}.txt" for index in range(1, 5)]
OUTPUT = HERE / "c5_table_iv_recompute.json"
H0_EV = 1.44e-33


def load_chain(path: Path) -> dict[str, np.ndarray]:
    header = path.open(encoding="utf-8").readline().lstrip("#").split()
    values = np.loadtxt(path)
    if values.ndim != 2 or values.shape[1] != len(header):
        raise ValueError(f"column mismatch in {path}")
    return {name: values[:, index] for index, name in enumerate(header)}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def weighted_quantile(values, weights, probabilities=(0.16, 0.5, 0.84)):
    order = np.argsort(values)
    sorted_values = np.asarray(values)[order]
    sorted_weights = np.asarray(weights, dtype=float)[order]
    positions = (np.cumsum(sorted_weights) - 0.5 * sorted_weights) / np.sum(sorted_weights)
    return np.interp(probabilities, positions, sorted_values).tolist()


def integrated_time_sokal(values: np.ndarray, c: float = 5.0) -> tuple[float, int]:
    """FFT autocorrelation with Sokal's first m >= c*tau(m) window."""
    x = np.asarray(values, dtype=float)
    n = len(x)
    if n < 2 or np.all(x == x[0]):
        return 1.0, 0
    x = x - np.mean(x)
    fft_size = 1 << (2 * n - 1).bit_length()
    transform = np.fft.rfft(x, n=fft_size)
    acov = np.fft.irfft(transform * np.conjugate(transform), n=fft_size)[:n]
    acov /= np.arange(n, 0, -1)
    rho = acov / acov[0]
    taus = 1.0 + 2.0 * np.cumsum(rho[1:])
    candidate = np.flatnonzero(np.arange(1, n) >= c * taus)
    window = int(candidate[0] + 1) if len(candidate) else n - 1
    tau = max(float(taus[window - 1]), 1.0)
    return tau, window


def summarize_subset(chains, predicate):
    selected = []
    expanded_beta_by_chain = []
    total_raw = total_weight = selected_raw = selected_weight = 0
    for chain in chains:
        weights = chain["weight"].astype(int)
        mask = np.asarray(predicate(chain), dtype=bool)
        total_raw += len(weights)
        total_weight += int(np.sum(weights))
        selected_raw += int(np.count_nonzero(mask))
        selected_weight += int(np.sum(weights[mask]))
        if np.any(mask):
            selected.append({key: values[mask] for key, values in chain.items()})
            expanded_beta_by_chain.append(np.repeat(chain["beta_deg"][mask], weights[mask]))

    if not selected:
        raise ValueError("empty subset")
    merged = {key: np.concatenate([chain[key] for chain in selected]) for key in selected[0]}
    weights = merged["weight"]
    beta = merged["beta_deg"]
    beta_mean = float(np.average(beta, weights=weights))
    beta_std = float(np.sqrt(np.average((beta - beta_mean) ** 2, weights=weights)))
    ess_parts = []
    for expanded in expanded_beta_by_chain:
        tau, window = integrated_time_sokal(expanded)
        ess_parts.append({
            "expanded_samples": int(len(expanded)),
            "tau": tau,
            "window_lag": window,
            "ess": float(len(expanded) / tau),
        })

    return {
        "raw_samples": selected_raw,
        "expanded_weight": selected_weight,
        "raw_fraction": selected_raw / total_raw,
        "surrogate_chain_weight_fraction": selected_weight / total_weight,
        "beta_deg": {
            "mean": beta_mean,
            "std": beta_std,
            "q16_q50_q84": weighted_quantile(beta, weights),
        },
        "m_over_H0_q16_q50_q84": weighted_quantile(
            np.power(10.0, merged["log10_m_eV"]) / H0_EV, weights
        ),
        "theta_i_q16_q50_q84": weighted_quantile(merged["theta_i"], weights),
        "C_agamma_q16_q50_q84": weighted_quantile(merged["C_agamma"], weights),
        "ess_beta_deg": float(sum(part["ess"] for part in ess_parts)),
        "ess_per_chain": ess_parts,
    }


def main() -> None:
    chains = [load_chain(path) for path in CHAIN_FILES]
    subsets = {
        "full": lambda chain: np.ones_like(chain["weight"], dtype=bool),
        "omega_a_lt_0p1": lambda chain: chain["Omega_a"] < 0.1,
        "omega_a_lt_0p01": lambda chain: chain["Omega_a"] < 0.01,
        "theta_i_le_0p1": lambda chain: chain["theta_i"] <= 0.1,
    }
    result = {
        "schema_version": 1,
        "source": "c5_continuous fixed-background surrogate chain",
        "interpretation": (
            "subset fractions are likelihood-weighted selection frequencies in the "
            "fixed-background surrogate chain, not physical posterior probabilities"
        ),
        "h0_eV_for_m_over_H0": H0_EV,
        "ess": {
            "marker": "beta_deg",
            "method": "integer-weight expansion; per-chain FFT ACF; Sokal automatic window c=5; sum per-chain N/tau",
            "subset_ordering": "filter rows first, preserve within-chain order, then expand integer weights",
        },
        "inputs": [
            {
                "path": str(path.relative_to(HERE.parents[2])),
                "sha256": sha256(path),
            }
            for path in CHAIN_FILES
        ],
        "subsets": {
            name: summarize_subset(chains, predicate)
            for name, predicate in subsets.items()
        },
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
