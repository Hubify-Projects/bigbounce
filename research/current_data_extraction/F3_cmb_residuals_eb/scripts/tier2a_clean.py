import numpy as np
import healpy as hp
import json, time, os

DATA = '/root/bigbounce/F3_cmb_residuals_eb/data/planck_pr3'
os.makedirs('/root/bigbounce/tier2a_results', exist_ok=True)

print('='*70)
print('TIER 2A: EB INJECTION RECOVERY')
print('='*70)

mask = hp.read_map(DATA+'/mask_pol.fits', field=0)
nside_sim = 256
mask_low = hp.ud_grade(mask, nside_sim)
mask_low = (mask_low > 0.5).astype(float)
fsky = np.mean(mask_low > 0.5)
lmax = 3 * nside_sim - 1
ell = np.arange(lmax + 1)
ClTT = 5000.0 / (ell * (ell+1) / (2*np.pi) + 1) * 2*np.pi / (ell*(ell+1) + 1)
ClEE = ClTT / 50.0
ClBB = ClEE / 100.0
ClTT[0:2] = 0; ClEE[0:2] = 0; ClBB[0:2] = 0

beta_levels = [0.0, 0.1, 0.27, 0.5, 1.0]
n_sims = 50
results = {}

for beta_deg in beta_levels:
    beta_rad = np.radians(beta_deg)
    recovered = []
    for isim in range(n_sims):
        np.random.seed(isim * 100 + int(beta_deg * 1000))
        alms_T = hp.synalm(ClTT, lmax=lmax, new=True)
        alms_E = hp.synalm(ClEE, lmax=lmax, new=True)
        alms_B = hp.synalm(ClBB, lmax=lmax, new=True)
        Q_map, U_map = hp.alm2map_spin([alms_E, alms_B], nside_sim, 2, lmax)
        cos2b = np.cos(2 * beta_rad)
        sin2b = np.sin(2 * beta_rad)
        Q_rot = Q_map * cos2b - U_map * sin2b
        U_rot = Q_map * sin2b + U_map * cos2b
        T_map = hp.alm2map(alms_T, nside_sim)
        cls = hp.anafast([T_map*mask_low, Q_rot*mask_low, U_rot*mask_low], lmax=lmax)
        CL_EE = cls[1] / fsky
        CL_EB = cls[4] / fsky
        ell_arr = np.arange(lmax+1)
        m = (ell_arr >= 30) & (ell_arr <= 300)
        w = 2*ell_arr[m] + 1
        EB_avg = np.average(CL_EB[m], weights=w)
        EE_avg = np.average(CL_EE[m], weights=w)
        beta_rec = 0.5 * np.degrees(EB_avg / EE_avg) if EE_avg > 0 else 0.0
        recovered.append(beta_rec)
    rec = np.array(recovered)
    bias = np.mean(rec) - beta_deg
    bias_sig = abs(bias) / (np.std(rec) / np.sqrt(n_sims)) if np.std(rec) > 0 else 0
    results[str(beta_deg)] = dict(injected=beta_deg, mean=float(np.mean(rec)),
        std=float(np.std(rec)), bias=float(bias), bias_sigma=float(bias_sig))
    status = 'PASS' if bias_sig < 3 else 'FAIL'
    print('  b_inj=%5.2f: rec=%+6.3f +/- %.3f  bias=%+.3f (%4.1fs)  %s' % (
        beta_deg, np.mean(rec), np.std(rec), bias, bias_sig, status))

verdict = 'PASS' if all(r['bias_sigma'] < 3 for r in results.values()) else 'FAIL'
print('\nVERDICT:', verdict)
with open('/root/bigbounce/tier2a_results/tier2a_injection_results.json', 'w') as f:
    json.dump(dict(results=results, verdict=verdict, n_sims=n_sims), f, indent=2)
print('Saved: tier2a_results/tier2a_injection_results.json')
