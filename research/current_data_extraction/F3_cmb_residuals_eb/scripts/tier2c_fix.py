import numpy as np
import healpy as hp
import pymaster as nmt
import json, time

DATA = '/root/bigbounce/F3_cmb_residuals_eb/data/planck_pr3'
print('TIER 2C: NaMaster EB (fixed lmax)')

maps = hp.read_map(DATA+'/smica_full.fits', field=[0,1,2])
T, Q, U = maps
mask = hp.read_map(DATA+'/mask_pol.fits', field=0)

nside_work = 256  # use 256 to be safe
Q_low = hp.ud_grade(Q, nside_work)
U_low = hp.ud_grade(U, nside_work)
mask_low = hp.ud_grade(mask, nside_work)
mask_low[mask_low < 0.5] = 0; mask_low[mask_low >= 0.5] = 1.0
mask_apo = nmt.mask_apodization(mask_low, 2.0, apotype='C1')
fsky = np.mean(mask_apo)
print('NSIDE=%d, fsky=%.3f' % (nside_work, fsky))

lmax_field = 3*nside_work - 1
f_E = nmt.NmtField(mask_apo, [Q_low, U_low], purify_b=True)
b = nmt.NmtBin.from_lmax_linear(lmax_field, 20)
ell_eff = b.get_effective_ells()

print('Computing spectra (lmax=%d)...' % lmax_field)
t0 = time.time()
w = nmt.NmtWorkspace()
w.compute_coupling_matrix(f_E, f_E, b)
cl_coupled = nmt.compute_coupled_cell(f_E, f_E)
cl_decoupled = w.decouple_cell(cl_coupled)
CL_EE, CL_EB, CL_BE, CL_BB = cl_decoupled
print('Done in %.1fs' % (time.time()-t0))

m = (ell_eff >= 50) & (ell_eff <= 500)
wt = 2*ell_eff[m]+1
EB_avg = np.average(CL_EB[m], weights=wt)
EE_avg = np.average(CL_EE[m], weights=wt)
beta_deg = 0.5 * np.degrees(EB_avg / EE_avg)

rng = np.random.default_rng(42)
betas = [0.5*np.degrees(np.average(CL_EB[m][rng.choice(np.sum(m),np.sum(m))], 
         weights=wt[rng.choice(np.sum(m),np.sum(m))]) / 
         np.average(CL_EE[m][rng.choice(np.sum(m),np.sum(m))],
         weights=wt[rng.choice(np.sum(m),np.sum(m))])) for _ in range(500)]
beta_std = np.std(betas)

print('beta (NaMaster) = %.4f +/- %.4f deg' % (beta_deg, beta_std))
print('beta (pseudo-Cl) = 0.167 +/- 0.021 deg')
print('Prediction: 0.27 deg')

result = dict(method='NaMaster_purified', nside=nside_work, fsky=float(fsky),
    beta_deg=float(beta_deg), beta_err_deg=float(beta_std),
    ell_range=[50,500])
with open('/root/bigbounce/tier2c_namaster_results.json','w') as f:
    json.dump(result, f, indent=2)
print('Saved')
