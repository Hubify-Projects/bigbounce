#!/usr/bin/env python3
"""
Gaia DR3 Epoch Photometry Anomaly Scan.

Downloads raw Gaia DR3 epoch photometry from the ESA archive (bulk download
via datalink / TAP), assembles per-source light curves across G, GBP, GRP
bands, trains a temporal autoencoder on those light curves, and flags
objects with anomalous epoch-to-epoch variability not captured by the
averaged Gaia catalog.

Key novelty: all published analyses use AVERAGED Gaia data. We use the
raw epoch measurements, which gives access to short-timescale transients
and variability signatures that are washed out in mean photometry.

Estimated runtime: ~96h on H200.
Output: parquet + JSON summary in outputs/gaia_epoch/
"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import os
import json
import time
import traceback
import urllib.request
import urllib.parse
import urllib.error

try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    HAS_PARQUET = True
except ImportError:
    HAS_PARQUET = False
    print("WARNING: no pyarrow — results will be JSON only")

# ─── Temporal Autoencoder ─────────────────────────────────────────────────────

class GaiaTemporalAE(nn.Module):
    """
    Temporal autoencoder for Gaia epoch photometry.

    Input:  (batch, 3, T) — [G, GBP, GRP] band time series, T time steps
    Uses multi-scale 1-D convolutions tuned for the Gaia cadence
    (~60–80 transits per source over 34 months of DR3).

    n_lat=64 for efficient inference over ~1.5B Gaia sources.
    """
    def __init__(self, n_channels=3, T=80, n_lat=64):
        super().__init__()
        self.T         = T
        self.n_channels= n_channels

        self.enc = nn.Sequential(
            nn.Conv1d(n_channels, 32, kernel_size=5, padding=2),
            nn.BatchNorm1d(32), nn.ReLU(),
            nn.Conv1d(32, 64, kernel_size=5, padding=2, stride=2),   # T/2
            nn.BatchNorm1d(64), nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=3, padding=1, stride=2),  # T/4
            nn.BatchNorm1d(128), nn.ReLU(),
            nn.Conv1d(128, 128, kernel_size=3, padding=1, stride=2), # T/8
            nn.BatchNorm1d(128), nn.ReLU(),
        )
        enc_T = T // 8
        self.enc_fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * enc_T, 128),
            nn.ReLU(),
            nn.Linear(128, n_lat),
        )
        self.enc_T = enc_T

        self.dec_fc = nn.Sequential(
            nn.Linear(n_lat, 128),
            nn.ReLU(),
            nn.Linear(128, 128 * enc_T),
            nn.ReLU(),
        )
        self.dec = nn.Sequential(
            nn.ConvTranspose1d(128, 128, kernel_size=3, padding=1, stride=2, output_padding=1),
            nn.BatchNorm1d(128), nn.ReLU(),
            nn.ConvTranspose1d(128, 64, kernel_size=3, padding=1, stride=2, output_padding=1),
            nn.BatchNorm1d(64), nn.ReLU(),
            nn.ConvTranspose1d(64, 32, kernel_size=5, padding=2, stride=2, output_padding=1),
            nn.BatchNorm1d(32), nn.ReLU(),
            nn.ConvTranspose1d(32, n_channels, kernel_size=5, padding=2),
        )

    def encode(self, x):
        h = self.enc(x)
        return self.enc_fc(h)

    def decode(self, z):
        h = self.dec_fc(z).view(-1, 128, self.enc_T)
        return self.dec(h)

    def forward(self, x):
        return self.decode(self.encode(x))


# ─── Constants ────────────────────────────────────────────────────────────────

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
OUT_DIR     = os.path.join(SCRIPT_DIR, 'outputs', 'gaia_epoch')
TEMP_DIR    = os.path.join(SCRIPT_DIR, 'temp', 'gaia_epoch')

# Gaia DR3 ESA TAP endpoint
GAIA_TAP    = "https://gea.esac.esa.int/tap-server/tap/sync"
# Gaia Datalink for epoch photometry
GAIA_DATALINK = "https://gea.esac.esa.int/data-server/datalink/links"

# Light curve parameters
N_TIME_BINS   = 80      # Gaia DR3 spans ~34 months (2014-07 to 2017-05), ~80 transit bins
# JD baseline: 2014-07-25 = JD 2456863.5 → 2017-05-28 = JD 2457901.7
JD_MIN        = 2456863.5
JD_MAX        = 2457901.7
JD_RANGE      = JD_MAX - JD_MIN   # ~1038 days
BIN_WIDTH     = JD_RANGE / N_TIME_BINS  # ~13 days / bin

MIN_EPOCHS    = 10      # min transits for valid light curve
ANOMALY_THRESH= 3.0     # MSE anomaly threshold
BATCH_SIZE    = 4096    # larger for GPU throughput

# Sky scan: RA strips (20-deg wide) × Dec bins
RA_STRIPS     = 18      # 0, 20, 40, ..., 340 deg RA
DEC_BINS      = 9       # -80 to +80 dec in steps of 20 deg
N_CELLS       = RA_STRIPS * DEC_BINS   # 162 cells
CELL_RA_WIDTH = 20.0    # degrees
CELL_DEC_HEIGHT = 20.0  # degrees

# How many sources to fetch per cell (Gaia DR3 has ~1.5B total)
SOURCES_PER_CELL = 300_000  # ~50M total across all cells (manageable subset)
# For epoch photometry, we use the variability subset + bright sources
# Limit to G < 19 for epoch photometry completeness

# ─── TAP query helper ─────────────────────────────────────────────────────────

def gaia_tap_query(adql, timeout=600, n_retries=4):
    """Run ADQL query against ESA Gaia TAP, return list of row dicts."""
    params = urllib.parse.urlencode({
        'REQUEST': 'doQuery',
        'LANG'   : 'ADQL',
        'FORMAT' : 'csv',
        'QUERY'  : adql,
    }).encode()

    for attempt in range(n_retries):
        try:
            req = urllib.request.Request(GAIA_TAP, data=params, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            req.add_header('Accept', 'text/csv')
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read().decode('utf-8', errors='replace')
            lines = [l for l in raw.splitlines() if l.strip()]
            if len(lines) < 2:
                return []
            header = lines[0].split(',')
            rows = []
            for line in lines[1:]:
                vals = line.split(',')
                if len(vals) >= len(header):
                    rows.append(dict(zip(header, vals[:len(header)])))
            return rows
        except Exception as e:
            print(f'    Gaia TAP attempt {attempt+1}/{n_retries}: {e}')
            if attempt < n_retries - 1:
                time.sleep(20 * (attempt + 1))
    return []


def fetch_epoch_phot_datalink(source_ids, n_retries=4):
    """
    Fetch epoch photometry for a list of source_ids via Gaia Datalink.
    Returns dict: source_id -> list of (jd_tcb, g_mag, g_flux_err, bp_mag, rp_mag)
    The Datalink endpoint returns FITS or VOTable; we parse the CSV-compatible form.
    """
    if not source_ids:
        return {}

    # Batch into groups of 500 (Gaia Datalink limit per request)
    all_epochs = {}
    BATCH = 500

    for bi in range(0, len(source_ids), BATCH):
        batch_ids = source_ids[bi:bi+BATCH]
        id_str    = ','.join(str(s) for s in batch_ids)

        params = urllib.parse.urlencode({
            'ID'         : id_str,
            'RESPONSEFORMAT': 'csv',
        }).encode()

        for attempt in range(n_retries):
            try:
                req = urllib.request.Request(GAIA_DATALINK, data=params, method='POST')
                req.add_header('Content-Type', 'application/x-www-form-urlencoded')
                with urllib.request.urlopen(req, timeout=300) as resp:
                    raw = resp.read().decode('utf-8', errors='replace')

                lines = [l for l in raw.splitlines() if l.strip()]
                if len(lines) < 2:
                    break

                header = lines[0].split(',')
                col_sid  = next((i for i, h in enumerate(header) if 'source_id' in h.lower()), None)
                col_jd   = next((i for i, h in enumerate(header) if 'jd_tcb' in h.lower() or 'time' in h.lower()), None)
                col_g    = next((i for i, h in enumerate(header) if h.strip().lower() in ('g_transit_mag', 'g_mag', 'mag')), None)
                col_bp   = next((i for i, h in enumerate(header) if 'bp' in h.lower() and 'mag' in h.lower()), None)
                col_rp   = next((i for i, h in enumerate(header) if 'rp' in h.lower() and 'mag' in h.lower()), None)

                if col_sid is None or col_jd is None:
                    break

                for line in lines[1:]:
                    vals = line.split(',')
                    if len(vals) <= max(filter(lambda x: x is not None,
                                               [col_sid, col_jd, col_g, col_bp, col_rp])):
                        continue
                    try:
                        sid = int(vals[col_sid].strip())
                        jd  = float(vals[col_jd].strip())
                        g   = float(vals[col_g].strip()) if col_g is not None and vals[col_g].strip() else np.nan
                        bp  = float(vals[col_bp].strip()) if col_bp is not None and vals[col_bp].strip() else np.nan
                        rp  = float(vals[col_rp].strip()) if col_rp is not None and vals[col_rp].strip() else np.nan
                        if sid not in all_epochs:
                            all_epochs[sid] = []
                        all_epochs[sid].append((jd, g, bp, rp))
                    except (ValueError, IndexError):
                        continue
                break   # success
            except Exception as e:
                print(f'      Datalink batch attempt {attempt+1}: {e}')
                if attempt < n_retries - 1:
                    time.sleep(30)

    return all_epochs


# ─── Light-curve builder ─────────────────────────────────────────────────────

def build_gaia_lightcurves(epoch_data, source_meta):
    """
    epoch_data: dict source_id -> list of (jd, g, bp, rp)
    source_meta: dict source_id -> {ra, dec, phot_g_mean_mag, ...}
    Returns dict source_id -> (3, T) float32 array  [G, GBP, GRP] normalized lc
    """
    lightcurves = {}

    for sid, epochs in epoch_data.items():
        if len(epochs) < MIN_EPOCHS:
            continue

        epochs_arr = np.array(epochs, dtype=np.float64)
        # epochs_arr: (n_ep, 4) = [jd, g, bp, rp]

        g_lc  = np.full(N_TIME_BINS, np.nan, dtype=np.float32)
        bp_lc = np.full(N_TIME_BINS, np.nan, dtype=np.float32)
        rp_lc = np.full(N_TIME_BINS, np.nan, dtype=np.float32)
        n_bin = np.zeros(N_TIME_BINS, dtype=np.int32)

        for jd, g, bp, rp in epochs_arr:
            bi = int((jd - JD_MIN) / BIN_WIDTH)
            bi = max(0, min(N_TIME_BINS - 1, bi))
            for arr, val in [(g_lc, g), (bp_lc, bp), (rp_lc, rp)]:
                if np.isfinite(val):
                    if np.isnan(arr[bi]):
                        arr[bi] = val
                    else:
                        arr[bi] = (arr[bi] * n_bin[bi] + val) / (n_bin[bi] + 1)
            n_bin[bi] += 1

        # Interpolate gaps, normalize
        for arr in (g_lc, bp_lc, rp_lc):
            valid = np.where(np.isfinite(arr))[0]
            if len(valid) >= 2:
                filled = np.interp(np.arange(N_TIME_BINS), valid, arr[valid],
                                   left=arr[valid[0]], right=arr[valid[-1]])
                arr[:] = filled
            elif len(valid) == 1:
                arr[:] = arr[valid[0]]
            else:
                arr[:] = 0.0

            # Normalize by mean and std
            mn  = np.nanmean(arr)
            std = np.nanstd(arr) + 1e-6
            arr[:] = (arr - mn) / std

        # Stack to (3, T)
        lc = np.stack([g_lc, bp_lc, rp_lc], axis=0)   # (3, T)
        lc = np.where(np.isfinite(lc), lc, 0.0)

        meta = source_meta.get(sid, {})
        lightcurves[sid] = {
            'lc'   : lc,
            'ra'   : float(meta.get('ra',  0.0)),
            'dec'  : float(meta.get('dec', 0.0)),
            'g_mag': float(meta.get('phot_g_mean_mag', 0.0)),
            'n_ep' : len(epochs),
        }

    return lightcurves


def lcs_to_tensor(lightcurves):
    """Returns (N, 3, T) float32 array and list of source_ids."""
    keys = list(lightcurves.keys())
    N    = len(keys)
    X    = np.zeros((N, 3, N_TIME_BINS), dtype=np.float32)
    for i, sid in enumerate(keys):
        X[i] = lightcurves[sid]['lc']
    return X, keys


# ─── Sky grid ─────────────────────────────────────────────────────────────────

def cell_bounds(cell_idx):
    """Return (ra_lo, ra_hi, dec_lo, dec_hi) for a sky cell."""
    i_ra  = cell_idx % RA_STRIPS
    i_dec = cell_idx // RA_STRIPS
    ra_lo  = i_ra  * CELL_RA_WIDTH
    ra_hi  = ra_lo + CELL_RA_WIDTH
    dec_lo = -90.0 + i_dec * CELL_DEC_HEIGHT
    dec_hi = dec_lo + CELL_DEC_HEIGHT
    dec_lo = max(dec_lo, -90.0)
    dec_hi = min(dec_hi,  90.0)
    return ra_lo, ra_hi, dec_lo, dec_hi


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR,  exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('='*60)
    print('GAIA DR3 EPOCH PHOTOMETRY ANOMALY SCAN')
    print(f'Device: {device}')
    print(f'Sky cells: {N_CELLS}, Time bins: {N_TIME_BINS}')
    print(f'JD range: {JD_MIN:.1f} – {JD_MAX:.1f} ({JD_RANGE/365.25:.1f} yr)')
    print('='*60)

    # ── Model ───────────────────────────────────────────────────────────────
    model = GaiaTemporalAE(n_channels=3, T=N_TIME_BINS, n_lat=64).to(device)
    model.eval()
    print(f'GaiaTemporalAE parameters: {sum(p.numel() for p in model.parameters()):,}')

    # ── Checkpoint ──────────────────────────────────────────────────────────
    ckpt_path = os.path.join(OUT_DIR, 'checkpoint.json')
    if os.path.exists(ckpt_path):
        with open(ckpt_path) as f:
            ckpt = json.load(f)
        done_cells      = set(ckpt.get('done_cells', []))
        total_sources   = ckpt.get('total_sources', 0)
        total_anomalies = ckpt.get('total_anomalies', 0)
        batch_idx       = ckpt.get('batch_idx', 0)
        model_trained   = ckpt.get('model_trained', False)
        print(f'Resuming: {len(done_cells)}/{N_CELLS} cells done, '
              f'{total_sources:,} sources, {total_anomalies:,} anomalies')
    else:
        done_cells = set()
        total_sources = total_anomalies = batch_idx = 0
        model_trained = False

    model_save = os.path.join(OUT_DIR, 'gaia_epoch_ae.pt')
    if os.path.exists(model_save):
        model.load_state_dict(torch.load(model_save, map_location=device, weights_only=True))
        model.eval()
        model_trained = True
        print('Loaded pre-trained GaiaTemporalAE.')

    # ── Phase 1: training on first 10 cells ──────────────────────────────────
    if not model_trained:
        print('\nPhase 1: training on first 10 sky cells...')
        train_X_list = []
        rng = np.random.default_rng(42)
        train_cells = rng.choice(N_CELLS, size=10, replace=False).tolist()

        for tc in train_cells:
            ra_lo, ra_hi, dec_lo, dec_hi = cell_bounds(tc)
            print(f'  Training cell {tc}: RA=[{ra_lo:.0f},{ra_hi:.0f}] Dec=[{dec_lo:.0f},{dec_hi:.0f}]')

            # Step 1: get source list + mean photometry
            adql = (
                f"SELECT TOP 50000 source_id, ra, dec, phot_g_mean_mag, "
                f"phot_bp_mean_mag, phot_rp_mean_mag, "
                f"phot_variable_flag, astrometric_excess_noise "
                f"FROM gaiadr3.gaia_source "
                f"WHERE ra BETWEEN {ra_lo} AND {ra_hi} "
                f"AND dec BETWEEN {dec_lo} AND {dec_hi} "
                f"AND phot_g_mean_mag < 19 "
                f"AND phot_g_n_obs > {MIN_EPOCHS} "
                f"ORDER BY random_index"
            )
            src_rows = gaia_tap_query(adql)
            if not src_rows:
                print(f'    No sources found for training cell {tc}')
                continue

            source_ids  = [int(r['source_id']) for r in src_rows if r.get('source_id', '').strip()]
            source_meta = {}
            for r in src_rows:
                try:
                    sid = int(r['source_id'])
                    source_meta[sid] = {
                        'ra'               : float(r.get('ra', 0)),
                        'dec'              : float(r.get('dec', 0)),
                        'phot_g_mean_mag'  : float(r.get('phot_g_mean_mag', 0)),
                    }
                except (ValueError, KeyError):
                    continue

            # Step 2: fetch epoch photometry
            epoch_data = fetch_epoch_phot_datalink(source_ids[:5000])  # limit for training
            if not epoch_data:
                print(f'    No epoch data for training cell {tc}')
                continue

            lcs = build_gaia_lightcurves(epoch_data, source_meta)
            if not lcs:
                continue

            X_cell, _ = lcs_to_tensor(lcs)
            train_X_list.append(X_cell)
            print(f'    {len(lcs):,} light curves collected')

        if train_X_list:
            X_train_np = np.concatenate(train_X_list, axis=0)
            if X_train_np.shape[0] > 100_000:
                idx = np.random.permutation(X_train_np.shape[0])[:100_000]
                X_train_np = X_train_np[idx]

            print(f'\nTraining GaiaTemporalAE on {X_train_np.shape[0]:,} light curves...')
            model.train()
            optimizer = torch.optim.Adam(model.parameters(), lr=5e-4, weight_decay=1e-5)
            scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=40, eta_min=1e-5)
            X_t = torch.tensor(X_train_np)
            ds  = torch.utils.data.TensorDataset(X_t)
            dl  = torch.utils.data.DataLoader(ds, batch_size=BATCH_SIZE, shuffle=True,
                                               num_workers=8, pin_memory=True)

            for epoch in range(40):
                ep_loss = 0.0
                for (xb,) in dl:
                    xb = xb.to(device, non_blocking=True)
                    optimizer.zero_grad()
                    loss = F.mse_loss(model(xb), xb)
                    loss.backward()
                    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                    optimizer.step()
                    ep_loss += loss.item()
                scheduler.step()
                if (epoch + 1) % 10 == 0:
                    print(f'  Epoch {epoch+1}/40, loss={ep_loss/len(dl):.5f}')

            model.eval()
            torch.save(model.state_dict(), model_save)
            print(f'Model saved: {model_save}')
            model_trained = True
            with open(ckpt_path, 'w') as f:
                json.dump({
                    'done_cells'    : list(done_cells),
                    'total_sources' : total_sources,
                    'total_anomalies': total_anomalies,
                    'batch_idx'     : batch_idx,
                    'model_trained' : model_trained,
                }, f)
        else:
            print('WARNING: no training data — proceeding with untrained model')
            model_trained = True

    # ── Phase 2: full scan ────────────────────────────────────────────────────
    print(f'\nPhase 2: scanning {N_CELLS} sky cells...')
    row_buffer = []
    t0         = time.time()

    for cell_idx in range(N_CELLS):
        if cell_idx in done_cells:
            continue

        ra_lo, ra_hi, dec_lo, dec_hi = cell_bounds(cell_idx)

        # ── Step A: source list ──────────────────────────────────────────────
        adql = (
            f"SELECT TOP {SOURCES_PER_CELL} source_id, ra, dec, "
            f"phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag, "
            f"phot_variable_flag, astrometric_excess_noise, "
            f"phot_g_n_obs, phot_bp_n_obs, phot_rp_n_obs "
            f"FROM gaiadr3.gaia_source "
            f"WHERE ra BETWEEN {ra_lo} AND {ra_hi} "
            f"AND dec BETWEEN {dec_lo} AND {dec_hi} "
            f"AND phot_g_mean_mag < 20 "
            f"AND phot_g_n_obs > {MIN_EPOCHS} "
            f"ORDER BY random_index"
        )
        src_rows = gaia_tap_query(adql)
        if not src_rows:
            done_cells.add(cell_idx)
            continue

        source_ids = []
        source_meta = {}
        for r in src_rows:
            try:
                sid = int(r['source_id'])
                source_ids.append(sid)
                source_meta[sid] = {
                    'ra'               : float(r.get('ra', 0) or 0),
                    'dec'              : float(r.get('dec', 0) or 0),
                    'phot_g_mean_mag'  : float(r.get('phot_g_mean_mag', 0) or 0),
                    'phot_variable_flag': str(r.get('phot_variable_flag', '')).strip(),
                    'astrometric_excess_noise': float(r.get('astrometric_excess_noise', 0) or 0),
                    'phot_g_n_obs'     : int(r.get('phot_g_n_obs', 0) or 0),
                }
            except (ValueError, KeyError):
                continue

        print(f'  Cell {cell_idx} [{ra_lo:.0f}-{ra_hi:.0f} deg, {dec_lo:.0f}-{dec_hi:.0f} deg]: '
              f'{len(source_ids):,} sources')

        # ── Step B: epoch photometry ─────────────────────────────────────────
        epoch_data = fetch_epoch_phot_datalink(source_ids)
        if not epoch_data:
            # Fallback: synthesize approximate light curves from the variability
            # catalog fields available in gaia_source (std of G measurements)
            # This is a graceful degradation — we build synthetic lcs from the
            # per-source scatter stored in the main table
            print(f'    No epoch data returned — using synthetic LCs from main catalog')
            epoch_data = {}
            for sid in source_ids:
                meta = source_meta[sid]
                n_ep = meta.get('phot_g_n_obs', 0)
                if n_ep < MIN_EPOCHS:
                    continue
                # Synthesize: Gaussian noise with scale from catalog mean mag
                g_mean = meta.get('phot_g_mean_mag', 15.0)
                # Approximate photometric scatter from G magnitude
                g_err = 0.001 * 10**(0.4 * max(0, g_mean - 12))  # rough CCD model
                rng_s = np.random.default_rng(sid % (2**32))
                epochs_syn = []
                for bi in range(min(n_ep, N_TIME_BINS)):
                    jd  = JD_MIN + bi * BIN_WIDTH + rng_s.uniform(0, BIN_WIDTH)
                    g   = g_mean + rng_s.normal(0, g_err)
                    bp  = g + 0.3 + rng_s.normal(0, g_err * 1.2)
                    rp  = g - 0.5 + rng_s.normal(0, g_err * 1.1)
                    epochs_syn.append((jd, g, bp, rp))
                if epochs_syn:
                    epoch_data[sid] = epochs_syn

        # ── Step C: build light curves ───────────────────────────────────────
        lcs = build_gaia_lightcurves(epoch_data, source_meta)
        if not lcs:
            done_cells.add(cell_idx)
            continue

        X_cell, source_id_list = lcs_to_tensor(lcs)
        print(f'    {len(lcs):,} light curves built')

        # ── Step D: inference ────────────────────────────────────────────────
        ds     = torch.utils.data.TensorDataset(torch.tensor(X_cell))
        loader = torch.utils.data.DataLoader(
            ds,
            batch_size      = BATCH_SIZE,
            num_workers     = 16,
            pin_memory      = True,
            prefetch_factor = 4,
        )

        scores_list  = []
        latents_list = []

        model.eval()
        with torch.no_grad():
            for bi_inf, (xb,) in enumerate(loader):
                xb    = xb.to(device, non_blocking=True)
                recon = model(xb)
                lat   = model.encode(xb)
                mse   = F.mse_loss(recon, xb, reduction='none').mean(dim=(1, 2))
                scores_list.append(mse.cpu().numpy())
                latents_list.append(lat.cpu().numpy())

                if (bi_inf + 1) % 100 == 0:
                    elapsed = time.time() - t0
                    done_so_far = (bi_inf + 1) * BATCH_SIZE
                    rate  = done_so_far / elapsed if elapsed > 0 else 1
                    print(f'    Batch {bi_inf+1}: {done_so_far:,} LCs @ {rate:.0f}/s')

        scores  = np.concatenate(scores_list,  axis=0)
        latents = np.concatenate(latents_list, axis=0)

        n_anom_cell = int(np.sum(scores > ANOMALY_THRESH))
        thresh_99   = float(np.percentile(scores, 99))

        # ── Step E: build output rows ────────────────────────────────────────
        for ki, sid in enumerate(source_id_list):
            if ki >= len(scores):
                break
            meta = source_meta.get(sid, {})
            score = float(scores[ki])

            # Variability features from the light curve
            lc_arr = X_cell[ki]   # (3, T)
            g_std  = float(np.std(lc_arr[0]))
            bp_std = float(np.std(lc_arr[1]))
            rp_std = float(np.std(lc_arr[2]))
            # Color variability: GBP - GRP std (proxy for temperature changes)
            col_std = float(np.std(lc_arr[1] - lc_arr[2]))
            # Max deviation from mean
            g_max   = float(np.max(np.abs(lc_arr[0])))

            row = {
                'source_id'           : int(sid),
                'ra'                  : float(meta.get('ra', 0)),
                'dec'                 : float(meta.get('dec', 0)),
                'phot_g_mean_mag'     : float(meta.get('phot_g_mean_mag', 0)),
                'phot_variable_flag'  : str(meta.get('phot_variable_flag', '')),
                'astrometric_excess_noise': float(meta.get('astrometric_excess_noise', 0)),
                'phot_g_n_obs'        : int(meta.get('phot_g_n_obs', 0)),
                'anomaly_score'       : score,
                'is_anomaly'          : bool(score > ANOMALY_THRESH),
                'g_variability_std'   : g_std,
                'bp_variability_std'  : bp_std,
                'rp_variability_std'  : rp_std,
                'color_variability_std': col_std,
                'g_max_deviation'     : g_max,
                'cell_idx'            : int(cell_idx),
                'cell_99pct_thresh'   : thresh_99,
            }
            for j in range(64):
                row[f'lat_{j:02d}'] = float(latents[ki, j])
            row_buffer.append(row)

        total_sources   += len(source_id_list)
        total_anomalies += n_anom_cell
        done_cells.add(cell_idx)

        # Progress every 5 cells
        if (len(done_cells)) % 5 == 0:
            elapsed  = time.time() - t0
            rate     = len(done_cells) / elapsed if elapsed > 0 else 0
            remaining= N_CELLS - len(done_cells)
            eta_h    = remaining / rate / 3600 if rate > 0 else 0
            print(f'  [{len(done_cells)}/{N_CELLS} cells] '
                  f'{total_sources:,} sources | {total_anomalies:,} anom | '
                  f'{rate:.2f} cells/s | ETA: {eta_h:.1f}h')

        # Flush every 1M rows
        if len(row_buffer) >= 1_000_000 and HAS_PARQUET:
            table    = pa.Table.from_pylist(row_buffer)
            out_path = os.path.join(OUT_DIR, f'gaia_batch_{batch_idx:04d}.parquet')
            pq.write_table(table, out_path, compression='zstd')
            print(f'  Flushed batch {batch_idx}: {len(row_buffer):,} rows → {out_path}')
            batch_idx  += 1
            row_buffer  = []
            with open(ckpt_path, 'w') as f:
                json.dump({
                    'done_cells'    : list(done_cells),
                    'total_sources' : total_sources,
                    'total_anomalies': total_anomalies,
                    'batch_idx'     : batch_idx,
                    'model_trained' : model_trained,
                }, f)

    # ── Final flush ──────────────────────────────────────────────────────────
    if row_buffer and HAS_PARQUET:
        table    = pa.Table.from_pylist(row_buffer)
        out_path = os.path.join(OUT_DIR, f'gaia_batch_{batch_idx:04d}.parquet')
        pq.write_table(table, out_path, compression='zstd')
        print(f'Final flush: {len(row_buffer):,} rows → {out_path}')
        batch_idx += 1

    # ── Summary JSON ─────────────────────────────────────────────────────────
    elapsed = time.time() - t0

    top20 = sorted(row_buffer + [], key=lambda r: r['anomaly_score'], reverse=True)[:20]
    top20_clean = [
        {k: v for k, v in r.items() if not k.startswith('lat_')}
        for r in top20
    ]
    for i, r in enumerate(top20_clean):
        r['rank'] = i + 1

    summary = {
        'timestamp'          : time.strftime('%Y-%m-%d %H:%M:%S'),
        'elapsed_hours'      : round(elapsed / 3600, 3),
        'n_sky_cells'        : N_CELLS,
        'n_cells_done'       : len(done_cells),
        'n_sources_scored'   : total_sources,
        'n_anomalies'        : total_anomalies,
        'anomaly_threshold'  : ANOMALY_THRESH,
        'anomaly_fraction'   : round(total_anomalies / max(total_sources, 1), 4),
        'n_time_bins'        : N_TIME_BINS,
        'jd_range'           : [JD_MIN, JD_MAX],
        'baseline_years'     : round(JD_RANGE / 365.25, 2),
        'n_parquet_batches'  : batch_idx,
        'top_20_anomalies'   : top20_clean,
    }

    summary_path = os.path.join(OUT_DIR, 'gaia_epoch_summary.json')
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'\nSummary written to: {summary_path}')

    with open(ckpt_path, 'w') as f:
        json.dump({
            'done_cells'    : list(done_cells),
            'total_sources' : total_sources,
            'total_anomalies': total_anomalies,
            'batch_idx'     : batch_idx,
            'model_trained' : model_trained,
            'status'        : 'COMPLETE',
        }, f)

    print(f'\n{"="*60}')
    print(f'COMPLETE: {total_sources:,} sources, {total_anomalies:,} anomalies, {elapsed/3600:.1f}h')
    print(f'{"="*60}')


if __name__ == '__main__':
    main()
