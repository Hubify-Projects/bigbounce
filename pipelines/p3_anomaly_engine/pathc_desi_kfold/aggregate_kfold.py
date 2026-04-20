#!/usr/bin/env python3
"""
DESI 5-Fold Stability Aggregator — P3-PATHC-DESI-KFOLD (criterion #4)
======================================================================
Consumes the 5 per-fold score parquets produced by `score_desi_kfold.py`
and computes the cross-fold Jaccard matrix + consensus-set statistics
that gate Path-C criterion #4.

Gate: mean pairwise Jaccard at top-1% ≥ 0.70 ⇒ DESI anomaly population
is stable across folds and Paper 3 Table 1 DESI number stands.

Run (local, no GPU needed):
    python3 aggregate_kfold.py \\
        --scores-dir outputs/desi_kfold/scores \\
        --out outputs/desi_kfold/kfold_stability_summary.json \\
        --top-frac 0.01

Inputs: scores-dir/fold_{0..4}_scores.parquet with columns
        (source_id, ra, dec, anomaly_score).
Output: JSON + a small consensus_top.parquet with the sources that were
        top-1% in ≥ 3 of 5 folds ("robust DESI anomalies").
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    u = len(a | b)
    return len(a & b) / u if u > 0 else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scores-dir', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--consensus-parquet', type=Path,
                    default=None,
                    help='write sources top-1% in ≥ 3 folds (defaults alongside --out)')
    ap.add_argument('--top-frac', type=float, default=0.01,
                    help='top fraction defining "anomaly" (default 0.01)')
    ap.add_argument('--gate-jaccard', type=float, default=0.70)
    args = ap.parse_args()

    fold_paths = sorted(args.scores_dir.glob('fold_*_scores.parquet'))
    if len(fold_paths) < 2:
        raise SystemExit(f'need ≥ 2 fold parquets, found {len(fold_paths)} in {args.scores_dir}')

    print(f'[agg] loading {len(fold_paths)} fold score files')
    fold_top_ids: list[set] = []
    fold_sizes = []
    for fp in fold_paths:
        df = pd.read_parquet(fp)
        n = len(df)
        k = max(1, int(args.top_frac * n))
        top = df.nlargest(k, 'anomaly_score')
        ids = set(top['source_id'].astype(str).tolist())
        fold_top_ids.append(ids)
        fold_sizes.append({'path': str(fp), 'n_rows': n, 'top_k': k})
        print(f'  {fp.name}: {n:,} rows, top-{args.top_frac*100:.2f}% = {k:,}')

    n_folds = len(fold_top_ids)

    # Pairwise Jaccard matrix
    J = np.eye(n_folds)
    pair_list = []
    for i, j in itertools.combinations(range(n_folds), 2):
        val = jaccard(fold_top_ids[i], fold_top_ids[j])
        J[i, j] = val
        J[j, i] = val
        pair_list.append({'i': i, 'j': j, 'jaccard': float(val)})

    off_diag = [J[i, j] for i in range(n_folds) for j in range(n_folds) if i < j]
    mean_jacc = float(np.mean(off_diag))
    min_jacc = float(np.min(off_diag))

    # Consensus (majority in ≥ 3 of 5) + singleton stats
    all_ids = set().union(*fold_top_ids)
    membership = {sid: sum(sid in fs for fs in fold_top_ids) for sid in all_ids}
    consensus_ids = {sid for sid, c in membership.items() if c >= 3}
    all_5_ids = {sid for sid, c in membership.items() if c == n_folds}
    singleton_ids = {sid for sid, c in membership.items() if c == 1}

    consensus_path = args.consensus_parquet or (args.out.parent / 'consensus_top.parquet')
    if consensus_ids:
        pd.DataFrame({
            'source_id': sorted(consensus_ids),
            'n_folds_present': [membership[s] for s in sorted(consensus_ids)],
        }).to_parquet(consensus_path, index=False)
        print(f'[agg] wrote {consensus_path} ({len(consensus_ids):,} consensus rows)')

    summary = {
        'task': 'P3-PATHC-DESI-KFOLD (criterion #4) — stability analysis',
        'n_folds': n_folds,
        'top_frac': args.top_frac,
        'fold_sizes': fold_sizes,
        'pairwise_jaccard': pair_list,
        'mean_pairwise_jaccard': mean_jacc,
        'min_pairwise_jaccard': min_jacc,
        'gate_jaccard_required': args.gate_jaccard,
        'gate_pass': bool(mean_jacc >= args.gate_jaccard),
        'counts': {
            'union_top': int(len(all_ids)),
            'consensus_ge3': int(len(consensus_ids)),
            'all_5_folds': int(len(all_5_ids)),
            'singleton_only': int(len(singleton_ids)),
        },
        'consensus_fraction_of_union': (
            float(len(consensus_ids) / len(all_ids)) if all_ids else 0.0
        ),
        'interpretation': (
            'gate_pass=True: DESI anomaly population is robust across folds; '
            'Paper 3 Table 1 DESI number (195,829 top-1% anomalies) stands unchanged. '
            'gate_pass=False with mean J in [0.50, 0.70): Paper 3 adds a stability row '
            'quoting Jaccard + consensus count. '
            'gate_pass=False with mean J < 0.50: switch Paper 3 headline to the '
            'consensus-set count and flag the DESI single-sample result as '
            'training-sample-conditioned.'
        ),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'[agg] wrote {args.out}  '
          f'mean_jacc={mean_jacc:.3f}  min={min_jacc:.3f}  '
          f'gate_pass={summary["gate_pass"]}  '
          f'consensus|union={len(consensus_ids)}/{len(all_ids)}')


if __name__ == '__main__':
    main()
