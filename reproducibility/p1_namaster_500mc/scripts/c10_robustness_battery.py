"""
c10 — NaMaster validation robustness battery (R23conf META-M1/M2/M3/M5/M6).

One battery, five configs, all at beta = 0.27 deg, N_REAL = 500, seed_base = 42
(identical seeds to the canonical run for paired comparison):

  canonical_refit  — canonical sky; THREE fits on the same MC ensemble:
                     (a) unweighted (canonical anchor),
                     (b) inverse-variance weighted (META-M1),
                     (c) unweighted restricted to ell_eff <= 1024 (META-M3)
  apod_fwhm_0p5    — mask apodization 0.5 deg FWHM (META-M5)
  apod_fwhm_3p0    — mask apodization 3.0 deg FWHM (META-M5)
  mask_b30         — Galactic cut |b| > 30 deg (META-M6)
  purify_b         — NmtField(..., purify_b=True) on canonical mask (META-M6)

The pre-2026-07-14 effective-ell-template anchors are retained only as
superseded evidence.  Every fit below uses the exact NaMaster bandpower-window
operator that generated the decoupled estimator.
Output: results/c10_robustness_battery.json
"""
import argparse
import hashlib
import json
import os
import time
from multiprocessing import Pool, get_context
from pathlib import Path

import numpy as np

from windowed_rotation import (
    build_rotation_response,
    recover_beta_deg,
    validate_window_equivalence,
)
from checkpoint_io import publish_json, validate_json_receipt
from physical_spectra import load_camb_lensed_spectra

BASE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.join(
    BASE, "..", "results", "physical_spectrum_v2", "c10_robustness_battery.json"
)
OUT = os.environ.get("C10_OUTPUT", DEFAULT_OUT)
CANONICAL_BANDPOWERS = os.path.join(
    BASE, "..", "results", "physical_spectrum_v2", "bandpowers.npz"
)

NSIDE = 512
LMAX = 2 * NSIDE
BETA = np.deg2rad(0.27)
N_REAL = int(os.environ.get("C10_NREAL", "500"))
SEED_BASE = 42
NOISE_LEVEL_UKARMIN = 10.0
CHECKPOINT_INTERVAL = 25
THEORY_OPERATOR = "NmtWorkspace.get_bandpower_windows exact tensor contraction"
_REALIZATION_STATE = None


def code_sha256():
    """Fingerprint every local module that defines the c10 scientific result."""
    digest = hashlib.sha256()
    for filename in (
        "c10_robustness_battery.py",
        "windowed_rotation.py",
        "checkpoint_io.py",
        "physical_spectra.py",
    ):
        path = Path(BASE) / filename
        digest.update(filename.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def checkpoint_path(output, config_name):
    output = Path(output)
    return output.with_name(f".{output.name}.{config_name}.checkpoint.json")


def _remove_checkpoint(path):
    path = Path(path)
    receipt = path.with_name(path.name + ".receipt.json")
    for candidate in (path, receipt):
        try:
            candidate.unlink()
        except FileNotFoundError:
            pass


def _publish_realization_checkpoint(path, cfg, all_eb):
    completed = len(all_eb)
    if completed <= 0 or completed > N_REAL:
        raise ValueError(f"invalid checkpoint completion count: {completed}")
    payload = {
        "schema_version": 1,
        "config_name": cfg["name"],
        "completed": completed,
        "seed_start": SEED_BASE,
        "seed_end": SEED_BASE + completed - 1,
        "realizations": [np.asarray(value, dtype=float).tolist() for value in all_eb],
    }
    publish_json(
        Path(path),
        payload,
        {
            "suite": "c10-realization-checkpoint",
            "config_names": [cfg["name"]],
            "configs": [cfg],
            "n_real": N_REAL,
            "seed_start": SEED_BASE,
            "seed_end": SEED_BASE + N_REAL - 1,
            "completed": completed,
            "checkpoint_interval": CHECKPOINT_INTERVAL,
            "theory_operator": THEORY_OPERATOR,
            "code_sha256": code_sha256(),
        },
    )


def _load_realization_checkpoint(path, cfg):
    path = Path(path)
    if not path.exists() and not path.with_name(path.name + ".receipt.json").exists():
        return []
    payload, receipt = validate_json_receipt(
        path,
        expected_suite="c10-realization-checkpoint",
        expected_configs=[cfg["name"]],
        expected_config_metadata=[cfg],
        expected_n_real=N_REAL,
        expected_seed_start=SEED_BASE,
        expected_seed_end=SEED_BASE + N_REAL - 1,
        expected_theory_operator=THEORY_OPERATOR,
        expected_code_sha256=code_sha256(),
    )
    completed = payload.get("completed")
    realizations = payload.get("realizations")
    if not isinstance(completed, int) or not 0 < completed <= N_REAL:
        raise ValueError(f"invalid checkpoint completed count in {path}: {completed!r}")
    if receipt.get("completed") != completed:
        raise ValueError(f"checkpoint payload/receipt completion mismatch in {path}")
    if payload.get("config_name") != cfg["name"]:
        raise ValueError(f"checkpoint payload config mismatch in {path}")
    if payload.get("seed_start") != SEED_BASE:
        raise ValueError(f"checkpoint payload seed start mismatch in {path}")
    if payload.get("seed_end") != SEED_BASE + completed - 1:
        raise ValueError(f"checkpoint payload seed end mismatch in {path}")
    if not isinstance(realizations, list) or len(realizations) != completed:
        raise ValueError(f"checkpoint realization count mismatch in {path}")
    arrays = [np.asarray(value, dtype=float) for value in realizations]
    if not arrays or any(value.ndim != 1 for value in arrays):
        raise ValueError(f"checkpoint realization shape mismatch in {path}")
    shape = arrays[0].shape
    if any(value.shape != shape or not np.all(np.isfinite(value)) for value in arrays):
        raise ValueError(f"checkpoint realization data invalid in {path}")
    print(f"[{cfg['name']}] resumed {completed}/{N_REAL} realizations from {path}", flush=True)
    return arrays


def _prepare_config_state(cfg):
    import healpy as hp
    import pymaster as nmt

    cl_ee, cl_bb, spectrum_metadata = load_camb_lensed_spectra(LMAX)

    npix = hp.nside2npix(NSIDE)
    pix_area_arcmin2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600
    noise_sigma = NOISE_LEVEL_UKARMIN / np.sqrt(pix_area_arcmin2)

    mask = np.ones(npix)
    _, lat = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < cfg.get("gal_cut", 20.0)] = 0.0
    ra, dec = hp.pix2ang(NSIDE, np.arange(npix), lonlat=True)
    mask[dec > 25.0] = 0.0
    mask[dec < -65.0] = 0.0
    mask = hp.smoothing(mask, fwhm=np.deg2rad(cfg.get("apod_fwhm", 2.0)))
    mask = np.clip(mask, 0, 1)
    fsky = mask.sum() / npix

    n_bins = 20
    edges = np.linspace(30, 3 * NSIDE, n_bins + 1, dtype=int)
    b = nmt.NmtBin.from_edges(edges[:-1], edges[1:])
    purify = bool(cfg.get("purify_b", False))
    zero = np.zeros(npix)
    f_dummy = nmt.NmtField(mask, [zero, zero], purify_b=purify)
    wsp = nmt.NmtWorkspace()
    wsp.compute_coupling_matrix(f_dummy, f_dummy, b)
    response = build_rotation_response(wsp, cl_ee, cl_bb)
    equivalence_max_abs = validate_window_equivalence(wsp, response, BETA)
    if not np.isfinite(equivalence_max_abs) or equivalence_max_abs > 1e-10:
        raise RuntimeError(
            f"{cfg['name']}: exact-window equivalence failure {equivalence_max_abs:.6e}"
        )
    return {
        "cfg": cfg,
        "cl_ee": cl_ee,
        "cl_bb": cl_bb,
        "spectrum_metadata": spectrum_metadata,
        "npix": npix,
        "noise_sigma": noise_sigma,
        "mask": mask,
        "fsky": fsky,
        "bins": b,
        "purify": purify,
        "workspace": wsp,
        "response": response,
        "equivalence_max_abs": equivalence_max_abs,
    }


def _simulate_realization(index, state):
    import healpy as hp
    import pymaster as nmt

    np.random.seed(SEED_BASE + index)
    maps = hp.synfast(
        [np.zeros(LMAX + 1), state["cl_ee"], state["cl_bb"], np.zeros(LMAX + 1)],
        NSIDE,
        lmax=LMAX,
        new=True,
    )
    q, u = maps[1], maps[2]
    q += np.random.normal(0, state["noise_sigma"], state["npix"])
    u += np.random.normal(0, state["noise_sigma"], state["npix"])
    cos2b, sin2b = np.cos(2 * BETA), np.sin(2 * BETA)
    q_rot = cos2b * q - sin2b * u
    u_rot = sin2b * q + cos2b * u
    field = nmt.NmtField(state["mask"], [q_rot, u_rot], purify_b=state["purify"])
    coupled = nmt.compute_coupled_cell(field, field)
    return state["workspace"].decouple_cell(coupled)[1]


def _initialize_realization_worker(cfg):
    global _REALIZATION_STATE
    _REALIZATION_STATE = _prepare_config_state(cfg)


def _run_worker_realization(index):
    if _REALIZATION_STATE is None:
        raise RuntimeError("realization worker was not initialized")
    return _simulate_realization(index, _REALIZATION_STATE)


def _progress(name, completed):
    if completed % 25 == 0 or completed == N_REAL:
        print(f"[{name}] realizations {completed}/{N_REAL}", flush=True)


def _collect_serial_realizations(cfg, state, realization_checkpoint=None):
    all_eb = (
        _load_realization_checkpoint(realization_checkpoint, cfg)
        if realization_checkpoint is not None
        else []
    )
    for index in range(len(all_eb), N_REAL):
        all_eb.append(_simulate_realization(index, state))
        _progress(cfg["name"], index + 1)
        if realization_checkpoint is not None and (
            len(all_eb) % CHECKPOINT_INTERVAL == 0 or len(all_eb) == N_REAL
        ):
            _publish_realization_checkpoint(realization_checkpoint, cfg, all_eb)
    return all_eb


def run_config(cfg, realization_workers=1, realization_checkpoint=None):
    import healpy as hp
    import pymaster as nmt

    name = cfg["name"]
    t0 = time.time()
    np.random.seed(SEED_BASE)
    state = _prepare_config_state(cfg)
    cl_ee = state["cl_ee"]
    cl_bb = state["cl_bb"]
    noise_sigma = state["noise_sigma"]
    mask = state["mask"]
    fsky = state["fsky"]
    b = state["bins"]
    purify = state["purify"]
    wsp = state["workspace"]
    response = state["response"]
    spectrum_metadata = state["spectrum_metadata"]
    equivalence_max_abs = state["equivalence_max_abs"]

    if cfg.get("canonical_artifact"):
        if not os.path.isfile(CANONICAL_BANDPOWERS):
            raise FileNotFoundError(
                "canonical exact-window bandpowers must finish before robustness battery"
            )
        with np.load(CANONICAL_BANDPOWERS) as canonical:
            all_eb = canonical["beta_0p270"]
        if len(all_eb) != N_REAL:
            raise ValueError(
                f"canonical artifact has {len(all_eb)} realizations, expected {N_REAL}"
            )
        execution = {
            "mode": "canonical_artifact_reuse",
            "realization_workers": 0,
            "result_order": (
                f"saved seed order {SEED_BASE}--{SEED_BASE + N_REAL - 1}"
            ),
        }
    else:
        if realization_workers == 1:
            all_eb = _collect_serial_realizations(
                cfg, state, realization_checkpoint
            )
            execution = {
                "mode": "serial",
                "realization_workers": 1,
                "result_order": (
                    f"ordered indices 0..N-1; seeds {SEED_BASE}--"
                    f"{SEED_BASE + N_REAL - 1}"
                ),
            }
        else:
            all_eb = (
                _load_realization_checkpoint(realization_checkpoint, cfg)
                if realization_checkpoint is not None
                else []
            )
            start_index = len(all_eb)
            # Main-process workspace is not shared across processes. Each spawned
            # worker constructs and caches its own exact workspace once.
            state["workspace"] = None
            del wsp
            context = get_context("spawn")
            with context.Pool(
                processes=realization_workers,
                initializer=_initialize_realization_worker,
                initargs=(cfg,),
            ) as pool:
                for completed, value in enumerate(
                    pool.imap(
                        _run_worker_realization,
                        range(start_index, N_REAL),
                        chunksize=1,
                    ),
                    start=start_index + 1,
                ):
                    all_eb.append(value)
                    _progress(name, completed)
                    if realization_checkpoint is not None and (
                        len(all_eb) % CHECKPOINT_INTERVAL == 0 or len(all_eb) == N_REAL
                    ):
                        _publish_realization_checkpoint(realization_checkpoint, cfg, all_eb)
            execution = {
                "mode": "ordered_seed_parallel",
                "realization_workers": realization_workers,
                "result_order": (
                    f"ordered imap indices 0..N-1; seeds {SEED_BASE}--"
                    f"{SEED_BASE + N_REAL - 1}"
                ),
                "workspace_cache": "one exact NmtWorkspace per spawned worker",
            }

    all_eb = np.array(all_eb)
    mean_eb, std_eb = all_eb.mean(axis=0), all_eb.std(axis=0)
    ell_effs = b.get_effective_ells()

    def fit(weights=None, ell_max=None):
        sel = np.ones(len(ell_effs), bool) if ell_max is None else (ell_effs <= ell_max)
        return float(
            recover_beta_deg(
                mean_eb,
                response,
                weights=weights,
                selection=sel,
            )
        )

    fits = {"unweighted": fit()}
    if cfg.get("extra_fits"):
        fits["invvar_weighted"] = fit(weights=1.0 / (std_eb ** 2 + 1e-20))
        fits["lmax1024_only"] = fit(ell_max=1024)

    res = {"name": name, "fsky": round(float(fsky), 4), "n_real": N_REAL,
           "purify_b": purify, "apod_fwhm_deg": cfg.get("apod_fwhm", 2.0),
           "gal_cut_deg": cfg.get("gal_cut", 20.0),
           "sky_spectrum": "CAMB lensed_scalar raw C_ell EE/BB",
           "physical_spectra": spectrum_metadata,
           "theory_operator": THEORY_OPERATOR,
           "window_shape": list(response["window_shape"]),
           "window_equivalence_max_abs": equivalence_max_abs,
           "execution": execution,
           "software": {"numpy": np.__version__, "healpy": hp.__version__,
                        "pymaster": nmt.__version__},
           "noise_sigma_pix_uK": round(float(noise_sigma), 4),
           "recovered_beta_deg": {k: round(v, 4) for k, v in fits.items()},
           "bias_deg": {k: round(v - 0.27, 4) for k, v in fits.items()},
           "runtime_s": round(time.time() - t0, 1)}
    print(f"[{name}] done in {res['runtime_s']}s: {res['recovered_beta_deg']}", flush=True)
    return res


CONFIGS = [
    {"name": "canonical_refit", "extra_fits": True, "canonical_artifact": True},
    {"name": "apod_fwhm_0p5", "apod_fwhm": 0.5},
    {"name": "apod_fwhm_3p0", "apod_fwhm": 3.0},
    {"name": "mask_b30", "gal_cut": 30.0},
    {"name": "purify_b", "purify_b": True},
]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only-config", choices=[item["name"] for item in CONFIGS])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--realization-workers", type=int, default=1)
    return parser.parse_args()


def main():
    args = parse_args()
    if args.realization_workers < 1:
        raise ValueError("--realization-workers must be at least 1")
    t0 = time.time()
    n_pool = int(os.environ.get("C10_POOL", "3"))
    requested = args.only_config or os.environ.get("C10_CONFIGS", "").strip()
    selected = CONFIGS
    if requested:
        names = {name.strip() for name in requested.split(",") if name.strip()}
        selected = [config for config in CONFIGS if config["name"] in names]
        missing = names - {config["name"] for config in selected}
        if missing:
            raise ValueError(f"unknown C10_CONFIGS names: {sorted(missing)}")
    if args.output is not None:
        output = args.output
    elif args.only_config:
        output = Path(DEFAULT_OUT).parent / "shards" / f"c10_{args.only_config}.json"
    else:
        output = Path(OUT)
    names = [config["name"] for config in selected]
    if args.realization_workers > 1 and len(selected) != 1:
        raise ValueError(
            "inner realization parallelism requires exactly one selected config"
        )
    if not args.force and output.exists():
        try:
            validate_json_receipt(
                output,
                expected_suite="c10",
                expected_configs=names,
                expected_config_metadata=selected,
                expected_n_real=N_REAL,
                expected_seed_start=SEED_BASE,
                expected_seed_end=SEED_BASE + N_REAL - 1,
                expected_theory_operator=THEORY_OPERATOR,
            )
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            pass
        else:
            print(f"validated existing shard; skipping: {output}")
            return
    if len(selected) == 1:
        checkpoints = [checkpoint_path(output, selected[0]["name"])]
        results = [
            run_config(
                selected[0],
                args.realization_workers,
                checkpoints[0],
            )
        ]
    else:
        checkpoints = [checkpoint_path(output, config["name"]) for config in selected]
        with Pool(processes=min(n_pool, len(selected))) as pool:
            results = pool.starmap(
                run_config,
                [(config, 1, path) for config, path in zip(selected, checkpoints)],
            )
    out = {"experiment": "c10 NaMaster robustness battery (R23conf META-M1/M2/M3/M5/M6)",
           "beta_injected_deg": 0.27, "n_real": N_REAL, "seed_base": SEED_BASE,
           "spectrum_policy": "all configurations use pinned raw CAMB lensed EE/BB",
           "superseded_effective_ell_anchor": {
               "recovered_beta_deg": 0.238,
               "bias_deg": -0.032,
               "status": "superseded_by_exact_bandpower_window_operator"
           },
           "configs": results, "total_runtime_s": round(time.time() - t0, 1)}
    receipt = publish_json(
        output,
        out,
        {
            "suite": "c10",
            "config_names": names,
            "configs": selected,
            "n_real": N_REAL,
            "seed_start": SEED_BASE,
            "seed_end": SEED_BASE + N_REAL - 1,
            "runtime_s": out["total_runtime_s"],
            "theory_operator": THEORY_OPERATOR,
            "code_sha256": code_sha256(),
            "window_equivalence_max_abs": max(
                result["window_equivalence_max_abs"] for result in results
            ),
            "software": results[0]["software"],
            "execution": [result["execution"] for result in results],
        },
    )
    print(json.dumps(out, indent=1))
    print(json.dumps(receipt, indent=2))
    for path in checkpoints:
        _remove_checkpoint(path)


if __name__ == "__main__":
    main()
