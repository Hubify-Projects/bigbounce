# CAMB 1.6.5 BBN provenance receipt

The frozen `*.updated.yaml` files for the executed P1B chains record CAMB
1.6.5 and no `bbn_predictor` override. CAMB therefore used its stock default:

- predictor class: `camb.bbn.BBN_table_interpolator`
- table/config value: `PRIMAT_Yp_DH_ErrorMC_2021.dat`
- table SHA-256: `ea5adce061720b937d8abda3a04a384aedaab3168dbf17414ff600cc91a7160c`
- interpolation grid: `ombh2` 0.005--0.040 (52 nodes), `DeltaN` -3--7
  (25 nodes), where `DeltaN = nnu - 3.044`

The public reproduction YAMLs explicitly name that table so they reproduce the
executed default. The prior on `ombh2` is wider than the tabulated grid, but the
frozen posterior is in the standard cosmological region; CAMB's spline otherwise
extrapolates rather than enforcing a hard bound.

Evidence was obtained from the official PyPI CAMB 1.6.5 source distribution
(`camb-1.6.5.tar.gz`, SHA-256
`402c14e76faf541a383bdc5a0fcc56e5d8fdf1636fc9a8fa082ab0fa8a0c4a05`,
tag commit `53c1f1c0208f75223cf3da2b163187deb7310f42`) and confirmed by executing
the validation below in CAMB 1.6.5.

`PArthENoPE` is not a valid CAMB table name and raises `FileNotFoundError`.
The valid legacy table spelling is `PArthENoPE_880.2_standard.dat`, but it was
not used by the frozen chains. At `ombh2=0.0224`, `DeltaN=0`, substituting that
legacy table changes `YHe` from 0.24586829 to 0.24540717 (difference 0.00046112).
Across `ombh2=0.020--0.024` and the sampled `nnu=2.046--5.046` range, the
absolute table difference is 0.000332--0.000649. This hypothetical swap is a
small model-systematic sensitivity, but it is immaterial to the published chain
provenance because the chains and corrected reproduction YAMLs both use PRIMAT;
no chain result has been relabelled as a PArthENoPE execution.

Validation command (requires exactly CAMB 1.6.5 and PyYAML):

```bash
python reproducibility/cosmology/test_bbn_provenance.py
```
