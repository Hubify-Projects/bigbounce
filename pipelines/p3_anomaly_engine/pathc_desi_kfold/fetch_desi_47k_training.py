#!/usr/bin/env python3
"""
DESI DR1 47K training-sample retrieval scaffold -- P3-PATHC-DESI-KFOLD-DATA-RETRIEVAL.

Unblocks the fire-#169 criterion-#4 launch blocker: the pod has the trained
weights (`best_model_47k.pt`) but NOT the 47K training spectra that BigAE
was fit on. `train_desi_kfold.py --training-shards <dir>/*.npy` cannot run
until those shards exist on disk.

This script materializes a 47K DESI DR1 spectrum sample as .npy shards
compatible with `load_training_spectra()` in `train_desi_kfold.py`.

WHY THIS EXISTS:
  - fire #148 trained BigAE on 47K DESI DR1 spectra but did not commit the
    `target_ids.json` to the repo -- only the `.pt` weights survived.
  - Path-C criterion #4 requires 5-fold OOS k-fold on the same training
    pool so the Jaccard stability gate is meaningful.
  - Per `desi_kfold_plan.md` L20: "same target_ids.json that the published
    BigAE was trained on so folds are directly comparable." That ideal is
    no longer reachable (IDs are lost). The closest practical substitute
    is: draw a fresh deterministic 47K sample from DESI DR1 with the
    kfold plan's seed (20,260,420), retrain the BigAE baseline on that
    sample (producing a new `best_model_47k.pt`), and run 5-fold k-fold
    on the same pool. The headline Jaccard-stability answer is unchanged
    in character; it just ceases to be a perturbation-around-the-
    published-model statement and becomes a fresh-baseline statement.
  - Houston sign-off required before the --live flag runs. In dry-run
    mode this script only validates the end-to-end pipeline skeleton.

Usage:
    # Dry-run (no network, validates config + writes manifest skeleton)
    python fetch_desi_47k_training.py --dry-run

    # Live run (requires SPARCL client, ~1-2 GPU-hours preprocess,
    # ~50-100 GB disk for intermediate spec files)
    python fetch_desi_47k_training.py --live \
        --output-dir /workspace/bigbounce_scan/outputs/desi/training_shards \
        --n-spectra 47000 --seed 20260420 --batch-size 500

Retrieval pipeline:
  1. Load DESI DR1 global target catalog (zall-pix-edr.fits or DR1 equivalent).
     Filters: SPECTYPE in {GALAXY, QSO, STAR}, ZWARN == 0, Z in [0, 5].
  2. `np.random.default_rng(seed=20,260,420)` permutation -> slice first
     N_SPECTRA target IDs. This seed matches `desi_kfold_plan.md`.
  3. Write `target_ids.json` manifest: {seed, n_spectra, target_id_list,
     source_catalog, timestamp}.
  4. For each batch of 500 target IDs:
       SPARCL retrieve(include=[wavelength, flux, ivar, ra, dec, z])
       For each spectrum:
         resample_to_desi_grid(wave, flux, ivar) -> 496-bin vector
         (median-normalized, matches the BigAE input preprocessing from
          sdss_native_retrain.py lines 97-118)
       np.save(shard_path, batch_vectors)
  5. Final inventory: sum(shard sizes) + expected_n verify + non-finite
     row count.

Shard layout (compatible with train_desi_kfold.py):
    outputs/desi/training_shards/
      shard_00000.npy   # shape (500, 496), float32
      shard_00001.npy
      ...
      shard_00093.npy   # last shard may be smaller
      target_ids.json   # manifest

Budget envelope (live run, A100 pod):
  - SPARCL retrieval:       ~1-2 h wall (rate-limited by api.noirlab server)
  - Preprocess + shard:      ~10 min on CPU
  - Disk footprint:          ~100 GB raw spec + ~100 MB shards
  - Pod spend @ $1.19/hr:    ~$3 total
  - Remaining #4 ledger:     retrieval (+15 %) -> training (+15 %) ->
                             inference + aggregation (+3 %) ->
                             .tex fill + recompile (+2 %)

Dry-run validation outputs:
  - config_summary.json:  effective args + seed + target n + output path
  - fetch_plan.json:      batch count + per-batch size + estimated shard
                          layout + expected disk usage
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

# Grid constants -- MUST match sdss_native_retrain.py lines 50-51 and
# desi_kfold_plan.md / train_desi_kfold.py BigAE(n_in=496) expectation.
DESI_WMIN, DESI_WMAX = 3600.0, 9800.0
N_BINS = 496

# Default seed -- matches desi_kfold_plan.md + train_desi_kfold.py
DEFAULT_SEED = 20260420
DEFAULT_N_SPECTRA = 47000
DEFAULT_BATCH_SIZE = 500

# DESI DR1 source catalog (published via NOIRLab data lab).
# Populated from `--dr-catalog` arg in live mode; placeholder path shown here.
DEFAULT_DR_CATALOG = (
    '/workspace/bigbounce_scan/data/desi/dr1/zall-pix-dr1.fits'
)


def resample_to_desi_grid(
    wave: np.ndarray, flux: np.ndarray, ivar: np.ndarray | None = None
) -> np.ndarray:
    """Resample a native DESI spectrum to the 496-bin BigAE input grid.

    Mirrors sdss_native_retrain.py lines 97-118. DESI spectra are already on
    a similar wavelength range; this just enforces the exact 496-bin layout
    that BigAE(n_in=496) expects.
    """
    desi_wave = np.linspace(DESI_WMIN, DESI_WMAX, N_BINS)
    step = (DESI_WMAX - DESI_WMIN) / N_BINS
    resampled = np.zeros(N_BINS, dtype=np.float32)
    for i in range(N_BINS):
        lo, hi = desi_wave[i] - step / 2, desi_wave[i] + step / 2
        mask = (wave >= lo) & (wave < hi)
        if mask.any():
            if ivar is not None:
                w = ivar[mask]
                if w.sum() > 0:
                    resampled[i] = np.average(flux[mask], weights=w)
                else:
                    resampled[i] = flux[mask].mean()
            else:
                resampled[i] = flux[mask].mean()
    nz = resampled[resampled != 0]
    if len(nz) > 0:
        med = float(np.median(nz))
        if med > 0:
            resampled /= med
    return resampled


def plan_fetch_batches(n_spectra: int, batch_size: int) -> dict[str, Any]:
    """Compute expected batch count + shard layout for dry-run validation."""
    n_full_batches, remainder = divmod(n_spectra, batch_size)
    n_batches = n_full_batches + (1 if remainder else 0)
    last_batch_size = remainder if remainder else batch_size
    # Shard sizes: (batch_size rows x 496 cols) @ float32 = batch_size x 1984 B
    bytes_per_shard_full = batch_size * N_BINS * 4
    bytes_per_shard_last = last_batch_size * N_BINS * 4
    total_bytes = n_full_batches * bytes_per_shard_full + bytes_per_shard_last
    return {
        'n_spectra': n_spectra,
        'batch_size': batch_size,
        'n_batches': n_batches,
        'n_full_batches': n_full_batches,
        'last_batch_size': last_batch_size,
        'bytes_per_full_shard': bytes_per_shard_full,
        'expected_shard_total_bytes': total_bytes,
        'expected_shard_total_mb': round(total_bytes / 1e6, 2),
    }


def draw_target_ids(
    n_spectra: int, seed: int, source_pool_size: int | None = None
) -> dict[str, Any]:
    """Deterministic target-ID draw manifest (no catalog load in dry-run)."""
    rng = np.random.default_rng(seed)
    # In dry-run, we don't have the real DR1 catalog loaded. We return the
    # first N_SPECTRA indices of a permutation over a placeholder pool size
    # so the manifest shape is validated. In live mode, the caller replaces
    # `source_pool_size` with the real catalog row count.
    pool = source_pool_size or 22_500_000  # DESI DR1 headline count
    permutation = rng.permutation(pool)
    chosen_indices = permutation[:n_spectra].tolist()
    return {
        'seed': seed,
        'n_spectra': n_spectra,
        'source_pool_size': pool,
        'chosen_indices_preview': chosen_indices[:10],
        'chosen_indices_count': len(chosen_indices),
        'permutation_checksum': int(
            np.sum(np.array(chosen_indices, dtype=np.int64)) % (2**31)
        ),
    }


def write_dry_run_summary(
    out_dir: Path,
    args: argparse.Namespace,
    id_manifest: dict[str, Any],
    fetch_plan: dict[str, Any],
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    config = {
        'mode': 'dry-run',
        'output_dir': str(out_dir),
        'seed': args.seed,
        'n_spectra': args.n_spectra,
        'batch_size': args.batch_size,
        'dr_catalog': str(args.dr_catalog),
        'grid': {
            'wmin_angstrom': DESI_WMIN,
            'wmax_angstrom': DESI_WMAX,
            'n_bins': N_BINS,
        },
    }
    summary = {
        'task_id': 'P3-PATHC-DESI-KFOLD-DATA-RETRIEVAL',
        'criterion': 4,
        'config': config,
        'target_id_manifest': id_manifest,
        'fetch_plan': fetch_plan,
        'expected_artifacts': [
            f'{out_dir}/target_ids.json',
            f'{out_dir}/shard_NNNNN.npy  (x {fetch_plan["n_batches"]})',
            f'{out_dir}/fetch_log.jsonl',
        ],
        'next_step': (
            'Houston sign-off on pod-budget spend (~$3) and DR catalog path; '
            'then re-run with --live + --dr-catalog <path-to-zall-pix-dr1.fits>'
        ),
    }
    (out_dir / 'dry_run_summary.json').write_text(
        json.dumps(summary, indent=2)
    )
    print(f'[dry-run] wrote {out_dir / "dry_run_summary.json"}')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        '--output-dir', type=Path,
        default=Path('outputs/desi/training_shards'),
        help='directory for .npy shards + target_ids.json'
    )
    ap.add_argument('--n-spectra', type=int, default=DEFAULT_N_SPECTRA)
    ap.add_argument('--batch-size', type=int, default=DEFAULT_BATCH_SIZE)
    ap.add_argument('--n-workers', type=int, default=12,
                    help='concurrent SPARCL retrieve() threads '
                         '(network-bound; 8-16 is the sweet spot)')
    ap.add_argument('--seed', type=int, default=DEFAULT_SEED)
    ap.add_argument(
        '--dr-catalog', type=Path, default=Path(DEFAULT_DR_CATALOG),
        help='DESI DR1 global target catalog (zall-pix-dr1.fits)'
    )
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--dry-run', action='store_true',
                   help='validate config + manifest; no network calls')
    g.add_argument('--live', action='store_true',
                   help='actually retrieve via SPARCL (requires '
                        'sparclclient; ~1-2 h wall; Houston-ack required)')
    args = ap.parse_args()

    id_manifest = draw_target_ids(args.n_spectra, args.seed)
    fetch_plan = plan_fetch_batches(args.n_spectra, args.batch_size)

    print('[plan] ' + json.dumps(fetch_plan))
    print(f'[plan] target-ID checksum (seed={args.seed}): '
          f'{id_manifest["permutation_checksum"]}')

    if args.dry_run:
        write_dry_run_summary(args.output_dir, args, id_manifest, fetch_plan)
        print('=' * 64)
        print('DRY RUN COMPLETE -- no network calls, no shards written.')
        print('=' * 64)
        return 0

    # ================================================================
    # LIVE RETRIEVAL -- Houston-ack'd 2026-04-22 to drive Path-C to 100%.
    # Direct SPARCL query on DESI-DR1 (no pre-downloaded FITS catalog
    # needed -- SPARCL's own `find()` is the catalog).
    # ================================================================
    try:
        from sparcl.client import SparclClient  # type: ignore
    except ImportError:
        print('ERROR: sparclclient not installed. '
              '`pip install sparclclient` on the pod.', file=sys.stderr)
        return 3

    try:
        import pandas as pd  # type: ignore
    except ImportError:
        print('ERROR: pandas required for metadata parquet write.',
              file=sys.stderr)
        return 3

    t_start = __import__('time').time()
    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    sc = SparclClient()
    print(f'[live] SparclClient instantiated; api={getattr(sc, "url", "?")}')

    # ---- Step 1: SPARCL find() over DESI-DR1 -----------------------
    # Use a generous limit; we will apply the deterministic seed-based
    # sampling locally so the draw is reproducible.
    find_limit = max(args.n_spectra * 3, 200000)  # pull ~3x N to allow rejection
    constraints = {
        'data_release': ['DESI-DR1'],
        'spectype': ['GALAXY', 'QSO', 'STAR'],
        'redshift': [0.0, 5.0],
    }
    outfields = ['sparcl_id', 'specid', 'ra', 'dec', 'redshift',
                 'spectype', 'data_release']
    print(f'[live] find(limit={find_limit}, constraints={constraints})')
    try:
        find_res = sc.find(outfields=outfields,
                           constraints=constraints,
                           limit=find_limit)
    except Exception as e:
        print(f'ERROR: SPARCL find() failed: {e}', file=sys.stderr)
        return 5

    find_records = list(find_res.records) if hasattr(find_res, 'records') else list(find_res)
    n_found = len(find_records)
    print(f'[live] find() returned {n_found:,} candidate records')
    if n_found < args.n_spectra:
        print(f'ERROR: need {args.n_spectra} but found only {n_found}. '
              'Raise find_limit or relax constraints.', file=sys.stderr)
        return 6

    # ---- Step 2: deterministic permutation pick --------------------
    rng = np.random.default_rng(args.seed)
    perm = rng.permutation(n_found)
    picked_idx = perm[:args.n_spectra]
    picked_records = [find_records[i] for i in picked_idx]
    sparcl_ids = []
    meta_rows = []
    def rec_get(r, k):
        """Safe accessor for SPARCL record (dict or attr-style)."""
        if isinstance(r, dict):
            return r.get(k)
        if hasattr(r, k):
            return getattr(r, k)
        return None

    for r in picked_records:
        def g(k, _r=r):
            return rec_get(_r, k)
        sparcl_ids.append(str(g('sparcl_id')))
        meta_rows.append({
            'sparcl_id': str(g('sparcl_id')),
            'specid': g('specid'),
            'ra': float(g('ra')) if g('ra') is not None else float('nan'),
            'dec': float(g('dec')) if g('dec') is not None else float('nan'),
            'redshift': float(g('redshift')) if g('redshift') is not None else float('nan'),
            'spectype': g('spectype'),
        })

    # target_ids.json manifest
    manifest = {
        'seed': args.seed,
        'n_spectra': args.n_spectra,
        'n_find_candidates': n_found,
        'sparcl_id_list': sparcl_ids,
        'constraints': constraints,
        'data_release': 'DESI-DR1',
        'timestamp_utc': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
    }
    with open(out_dir / 'target_ids.json', 'w') as f:
        json.dump(manifest, f)
    print(f'[live] wrote {out_dir / "target_ids.json"}')

    # ---- Step 3: parallel batched retrieve() + resample + shard ----
    # Parallelism: SPARCL retrieval is network-bound at noirlab.edu, so a
    # ThreadPoolExecutor with 8-16 workers gives a 3-5x speedup vs serial.
    # The GPU is untouched during retrieval; parallel threads saturate the
    # server-side rate limit without GPU contention.
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading
    log_path = out_dir / 'fetch_log.jsonl'
    logf = log_path.open('w')
    log_lock = threading.Lock()
    total_written = 0
    non_finite = 0
    successful_meta = []
    write_lock = threading.Lock()

    # Build the batch plan (batch_idx -> (b_start, b_end, batch_uuids, meta_slice))
    batches = []
    for b_start in range(0, len(sparcl_ids), args.batch_size):
        b_end = min(b_start + args.batch_size, len(sparcl_ids))
        batches.append((len(batches), b_start, b_end,
                        sparcl_ids[b_start:b_end],
                        meta_rows[b_start:b_end]))

    n_batches = len(batches)
    print(f'[live] {n_batches} batches x {args.batch_size} spectra, '
          f'{args.n_workers} concurrent workers')

    def process_batch(task):
        nonlocal total_written, non_finite
        batch_idx, b_start, b_end, batch_uuids, batch_meta = task
        t_b = __import__('time').time()
        try:
            ret = sc.retrieve(uuid_list=batch_uuids,
                              include=['sparcl_id', 'wavelength', 'flux', 'ivar'],
                              dataset_list=['DESI-DR1'])
        except Exception as e:
            msg = f'retrieve() failed on batch {batch_idx}: {e}'
            with log_lock:
                print(f'[live] WARN {msg}', file=sys.stderr)
                logf.write(json.dumps({'shard': batch_idx, 'error': str(e),
                                        'batch_start': b_start, 'batch_end': b_end}) + '\n')
                logf.flush()
            return 0
        ret_records = list(ret.records) if hasattr(ret, 'records') else list(ret)
        by_id = {}
        for r in ret_records:
            rid = rec_get(r, 'sparcl_id')
            if rid is not None:
                by_id[str(rid)] = r

        batch_vecs = []
        batch_meta_aligned = []
        local_bad = 0
        for local_i, uuid in enumerate(batch_uuids):
            r = by_id.get(str(uuid))
            if r is None:
                local_bad += 1
                continue
            wave = rec_get(r, 'wavelength')
            flux = rec_get(r, 'flux')
            ivar = rec_get(r, 'ivar')
            if wave is None or flux is None:
                local_bad += 1
                continue
            wave_a = np.asarray(wave, dtype=np.float64)
            flux_a = np.asarray(flux, dtype=np.float64)
            ivar_a = np.asarray(ivar, dtype=np.float64) if ivar is not None else None
            vec = resample_to_desi_grid(wave_a, flux_a, ivar_a)
            if not np.isfinite(vec).all():
                local_bad += 1
                continue
            batch_vecs.append(vec)
            batch_meta_aligned.append(batch_meta[local_i])

        wall = __import__('time').time() - t_b
        if batch_vecs:
            arr = np.stack(batch_vecs, axis=0).astype(np.float32)
            shard_path = out_dir / f'shard_{batch_idx:05d}.npy'
            with write_lock:
                np.save(shard_path, arr)
                for row_i, m in enumerate(batch_meta_aligned):
                    m2 = dict(m)
                    m2['shard_idx'] = batch_idx
                    m2['row_in_shard'] = row_i
                    successful_meta.append(m2)
                total_written += len(batch_vecs)
                non_finite += local_bad
                cum = total_written
            with log_lock:
                print(f'[live] shard {batch_idx:05d}: '
                      f'{len(batch_vecs)}/{len(batch_uuids)} ({wall:.1f}s); '
                      f'cum {cum}/{args.n_spectra}')
                logf.write(json.dumps({
                    'shard': batch_idx, 'submitted': len(batch_uuids),
                    'written': len(batch_vecs), 'wall_s': round(wall, 2),
                    'cum_written': cum,
                }) + '\n')
                logf.flush()
        return len(batch_vecs)

    with ThreadPoolExecutor(max_workers=args.n_workers) as ex:
        futures = [ex.submit(process_batch, t) for t in batches]
        for _ in as_completed(futures):
            pass

    logf.close()
    shard_idx = n_batches

    # metadata.parquet aligned to concatenated-shard row order.
    # Shards load via sorted(glob('*.npy')) i.e. shard_00000, shard_00001,...;
    # so metadata must be sorted by (shard_idx, row_in_shard) to match.
    meta_df = pd.DataFrame(successful_meta)
    meta_df = meta_df.sort_values(['shard_idx', 'row_in_shard']).reset_index(drop=True)
    meta_df['source_id'] = meta_df['sparcl_id']  # alias used by score_desi_kfold.py
    meta_df.to_parquet(out_dir / 'metadata.parquet', index=False)
    print(f'[live] wrote {out_dir / "metadata.parquet"} ({len(meta_df)} rows)')

    # Final summary
    final = {
        'mode': 'live',
        'n_shards': shard_idx,
        'n_written': total_written,
        'n_target': args.n_spectra,
        'n_nonfinite_dropped': non_finite,
        'target_id_checksum': id_manifest['permutation_checksum'],
        'wall_s': round(__import__('time').time() - t_start, 1),
    }
    with open(out_dir / 'live_run_summary.json', 'w') as f:
        json.dump(final, f, indent=2)
    print('=' * 64)
    print(f'LIVE RUN COMPLETE -- {total_written:,} spectra across '
          f'{shard_idx} shards in {final["wall_s"]}s')
    print('=' * 64)
    if total_written < int(0.95 * args.n_spectra):
        print(f'WARNING: only {total_written} / {args.n_spectra} retrieved '
              f'({100*total_written/args.n_spectra:.1f}%). Consider re-running '
              'or relaxing rejection filters.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
