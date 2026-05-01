import time, json, os, sys
import numpy as np
import pandas as pd
import healpy as hp

t0 = time.time()
os.makedirs('/workspace/r42_wave11g_hemi', exist_ok=True)
NSIDE_DIR = 8
N_MC      = 500   # reduced from 1000 for 2 GB RAM constraint
CHUNK     = 64    # directions per matmul chunk
SEED      = 42
print(f'[init] NSIDE_DIR={NSIDE_DIR} ndirs={hp.nside2npix(NSIDE_DIR)} N_MC={N_MC} CHUNK={CHUNK}', flush=True)

cat = pd.read_parquet('/workspace/r42_b20/chirality_catalog/catalog_production.parquet',
                      columns=['ra','dec','class_eq','p_cw_eq','p_ccw_eq','p_ns_eq'])
print(f'[1] loaded {len(cat):,} rows', flush=True)

is_cw  = cat['class_eq'].astype(str).str.upper().eq('CW').values
is_ccw = cat['class_eq'].astype(str).str.upper().eq('CCW').values
mask_sp = is_cw | is_ccw
ra  = np.deg2rad(cat['ra'].values[mask_sp])
dec = np.deg2rad(cat['dec'].values[mask_sp])
cw_label = is_cw[mask_sp].astype(np.float32)
n_sp = len(cw_label)
print(f'[1] spirals: {n_sp:,} (CW={int(cw_label.sum()):,} CCW={n_sp - int(cw_label.sum()):,})', flush=True)

ndirs = hp.nside2npix(NSIDE_DIR)
theta_d, phi_d = hp.pix2ang(NSIDE_DIR, np.arange(ndirs))
ra_dir = np.rad2deg(phi_d)
dec_dir = 90.0 - np.rad2deg(theta_d)
gv = np.empty((n_sp, 3), dtype=np.float32)
gv[:,0] = np.cos(dec)*np.cos(ra)
gv[:,1] = np.cos(dec)*np.sin(ra)
gv[:,2] = np.sin(dec)
dv = np.empty((ndirs, 3), dtype=np.float32)
dv[:,0] = np.sin(theta_d)*np.cos(phi_d)
dv[:,1] = np.sin(theta_d)*np.sin(phi_d)
dv[:,2] = np.cos(theta_d)
print(f'[2] {ndirs} hemisphere centers', flush=True)

# Build HEMI as uint8 to halve memory vs bool (numpy bool=1B already, so same)
print('[3] Computing hemisphere boolean ...', flush=True)
t1 = time.time()
HEMI = np.empty((ndirs, n_sp), dtype=np.uint8)
for i in range(0, ndirs, CHUNK):
    j = min(i+CHUNK, ndirs)
    HEMI[i:j] = (dv[i:j] @ gv.T > 0).astype(np.uint8)
print(f'[3] hemisphere matrix built in {time.time()-t1:.1f}s — {HEMI.nbytes/1e9:.2f} GB', flush=True)

n_total_per_dir = HEMI.sum(axis=1).astype(np.float64)
print(f'[3] n_total per dir: min={int(n_total_per_dir.min())} median={int(np.median(n_total_per_dir))} max={int(n_total_per_dir.max())}', flush=True)

def asym_max_chunked(labels_f32):
    n_cw = np.empty(ndirs, dtype=np.float64)
    for i in range(0, ndirs, CHUNK):
        j = min(i+CHUNK, ndirs)
        # Cast chunk to float32 for BLAS; chunk size 64 * 3.2M = 200M float32 = 0.8 GB
        blk = HEMI[i:j].astype(np.float32)
        n_cw[i:j] = blk @ labels_f32
        del blk
    asym = (2.0*n_cw - n_total_per_dir) / n_total_per_dir
    return float(np.max(np.abs(asym))), int(np.argmax(np.abs(asym)))

print('[4] Computing data asymmetry per direction ...', flush=True)
max_data, argmax_data = asym_max_chunked(cw_label)
print(f'[4] max|A|(data) = {max_data:.6e} at dir #{argmax_data} (RA,Dec)=({ra_dir[argmax_data]:.2f},{dec_dir[argmax_data]:.2f})', flush=True)

print(f'[5] Running {N_MC} label-shuffle nulls (chunked CHUNK={CHUNK}) ...', flush=True)
rng = np.random.default_rng(SEED)
max_null = np.zeros(N_MC)
t_mc = time.time()
for k in range(N_MC):
    perm = rng.permutation(cw_label)
    max_null[k], _ = asym_max_chunked(perm)
    if (k+1) % 25 == 0:
        rate = (k+1)/(time.time() - t_mc)
        eta  = (N_MC - k - 1)/max(rate, 0.001)
        print(f'    [{k+1}/{N_MC}] {rate:.3f} MC/s  ETA {eta/60:.1f} min', flush=True)

p_global = float((max_null >= max_data).sum() + 1) / (N_MC + 1)
print(f'[6] global p-value (look-elsewhere corrected) = {p_global:.6f}', flush=True)
print(f'[6] N_MC nulls >= data = {(max_null >= max_data).sum()}', flush=True)
print(f'[6] max_null mean / p99 = {np.mean(max_null):.4e} / {np.percentile(max_null,99):.4e}', flush=True)

result = {
  'nside_dir': NSIDE_DIR, 'ndirs': int(ndirs), 'n_mc': int(N_MC),
  'n_total': int(len(cat)), 'n_spirals': int(n_sp),
  'cw_count': int(cw_label.sum()), 'ccw_count': int(n_sp-cw_label.sum()),
  'max_A_data': float(max_data),
  'argmax_dir': int(argmax_data),
  'argmax_radec_deg': [float(ra_dir[argmax_data]), float(dec_dir[argmax_data])],
  'max_null_mean': float(np.mean(max_null)),
  'max_null_median': float(np.median(max_null)),
  'max_null_p99': float(np.percentile(max_null,99)),
  'p_value_global_LEE': p_global,
  'wall_time_sec': time.time() - t0,
  'notes': 'NSIDE=8 (768 dirs) hemisphere look-elsewhere null with N_MC=500 label shuffles; chunked float32 matmul to fit 2 GB RAM. Reduced from N_MC=1000 due to pod RAM constraint.',
}
np.save('/workspace/r42_wave11g_hemi/max_null.npy', max_null)
with open('/workspace/r42_wave11g_hemi/results.json','w') as f:
    json.dump(result, f, indent=2)
print(f'[done] wall {result["wall_time_sec"]:.1f}s; results in /workspace/r42_wave11g_hemi/', flush=True)
