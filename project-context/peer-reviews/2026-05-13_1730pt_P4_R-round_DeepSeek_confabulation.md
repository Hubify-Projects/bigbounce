# P4 R-round — DeepSeek-V3.5 Adversarial Confabulation-Hunter Review (v1.0.49 cycle)

**Reviewer simulated:** DeepSeek-V3.5 (confabulation specialty; matches paper-claimed numbers against on-disk JSON/NPZ artifacts and hunts arithmetic inconsistencies introduced in the most recent revision; non-Anthropic perspective)
**Date:** 2026-05-13 17:30 PDT
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.49, 2,993 lines.
**Mode:** R-round-3 adversarial. Focus: NEW numerical claims introduced in v1.0.48 → v1.0.49 (Rotation-TTA bound, Table III σ_null reconstruction, joint χ²/dof, McNemar/Cohen κ, fracdev binned figure, 28.80σ bootstrap, 5.55M-vs-3.20M heterogeneity).

**Headline:** **1 BLOCKER · 1 MAJOR · 1 MINOR · 0 NIT = 3 findings** total (down from R-round-2's 16 — most prior issues closed; one fresh arithmetic confabulation introduced in v1.0.49, one heterogeneity disclosure issue, one residual wording sign-error survives from earlier rounds).

**Most concerning confabulation (one sentence):** Paper §V "Empirical bound on rotation-correlated CW-fraction excursion" claims the 0.0005 (0.05%) bin-to-bin spread is **"30× smaller than the monopole itself"**, but the paper's own quoted monopole magnitude in the same paragraph is **0.0026 (0.26%)** — the actual ratio is **5.3×, not 30×** (`0.0026 / 0.0005 = 5.29`), a 5.7-fold arithmetic overstatement of the empirical-bound strength that an external referee will catch by typing two numbers into a calculator.

---

## BLOCKERS (must close before submission)

### B-DS-1 — The new Rotation-TTA "30× smaller than the monopole" claim is arithmetically wrong by 5.7× — it's actually 5.3× smaller; the bound is real but the framing oversells it

This is the **new** v1.0.48 closure that landed at lines 653–664. The paper says (verbatim, lines 653–664):

> "the maximum CW-fraction excursion across the four b/a bins (face-on, intermediate, edge-on, nan-b/a) is **0.0005 (0.05%), well below both the catalog-wide 9.5σ monopole magnitude (0.0026)** and the 0.1% flatness target. […] **The monopole offset is therefore not a rotation-equivariance artifact (the bound is 30× smaller than the monopole itself)**, and the residual ~0.3% catalog-wide CW asymmetry must arise from non-rotational sources"

Both numbers are correct individually — verified against on-disk artifact:

```bash
python3 -c "
import json
d = json.load(open('pipelines/p2_chirality/r42_results/wave_14_kk_ba_reconciliation_results.json'))
fracs = [(r['bin'], r['n_cw_eq']/(r['n_cw_eq']+r['n_ccw_eq'])) for r in d['table']]
for b,f in fracs: print(f'{b:10s} f_cw={f:.6f}')
print('spread =', max(f for _,f in fracs) - min(f for _,f in fracs))
"
# ge_0p5     f_cw=0.497490
# 0p3_0p5    f_cw=0.497015
# lt_0p3     f_cw=0.497528
# nan        f_cw=0.497207
# spread = 0.0005126431520270369   ✓ matches paper 0.0005

# Monopole: |0.5 - 0.49735| = 0.00265   ✓ matches paper 0.0026
```

But the ratio claim does NOT hold:

```bash
python3 -c "print(0.0026 / 0.0005)"
# 5.2  (paper claims 30×)
```

5.3× — five-fold, not thirty-fold. The empirical bound is genuinely strong (0.05% bin-to-bin spread on 785,859 edge-on galaxies is publishable as a constraint on rotation-equivariance violation), and the qualitative conclusion ("monopole offset is not a rotation-equivariance artifact") is correct because 0.05% < 0.26%. But the **numerical strength of the bound is 5× the monopole, not 30×**, and the paper's own number "0.0026" sitting two clauses upstream of "30× smaller than the monopole itself" makes this an own-goal: any referee who reads the paragraph carefully will type `0.0026 / 0.0005` and get 5.2, not 30.

This is the most dangerous class of confabulation in a v1.0.48 closure: the artifact-backed numbers are right, but the rhetorical multiplier connecting them is invented. The "30× smaller" phrasing reads like it was generated from a different baseline (perhaps the 0.1% flatness target divided by some interim bound, or a memory of the 28.8σ-vs-0.43σ ratio).

**Fix:** Replace "the bound is 30× smaller than the monopole itself" with the artifact-correct "the bound is 5× smaller than the monopole itself (0.05% vs 0.26%)" — or, since the 5× ratio is less rhetorically punchy, restructure to lead with the absolute number: "the bound is 0.05%, a factor of ~5 below the 0.26% monopole and a factor of ~2 below the 0.1% flatness target." Both keep the load-bearing scientific claim intact while removing the arithmetic error.

```bash
# Confirm the fix arithmetic from the same artifact:
python3 -c "
spread = 0.0005126431520270369
mono = abs(0.5 - 0.49735314698421823)
print(f'monopole = {mono:.4f} ({mono*100:.2f}%)')
print(f'spread   = {spread:.4f} ({spread*100:.2f}%)')
print(f'ratio    = {mono/spread:.2f}x')
"
# monopole = 0.0026 (0.26%)
# spread   = 0.0005 (0.05%)
# ratio    = 5.29x
```

This is the single most catchable confabulation in the v1.0.49 manuscript. A non-Anthropic referee with five minutes and a calculator will land on it. Fix before submission.

---

## MAJOR (should close before submission)

### M-DS-1 — Table III's ℓ=1 single-mode row uses a different (5.55M, f_sky=0.659) galaxy/footprint configuration than rows 2–5 (3.20M, f_sky=0.491), and the heterogeneity disclosure footnote does not explicitly quote the 5,547,858 galaxy count or the 0.659 f_sky in the table caption

The new v1.0.49 Table III row 1 is well-anchored — the values C₁ = 1.494×10⁻⁶, σ_null = 0.429×10⁻⁶, significance = −0.122σ all reproduce from `pipelines/p2_chirality/master_results/master_power_spectrum.json`:

```bash
python3 -c "
import json
d = json.load(open('pipelines/p2_chirality/master_results/master_power_spectrum.json'))
print('n_galaxies:', d['n_galaxies'])
print('f_sky:', d['f_sky'])
print('Cl[0]:', d['Cl_master_decoupled'][0])
"
# n_galaxies: 5547858
# f_sky:      0.6588541666666666
# Cl[0]:      1.493783415832274e-06   ✓ matches Table III ℓ=1 row
```

And rows 2–5 reproduce from `wave_14_pp_namaster_verification.json` (n_spiral=3,201,160, f_sky=0.491):

```bash
python3 -c "
import json
d = json.load(open('pipelines/p2_chirality/r42_results/wave_14_pp_namaster_verification.json'))
print('n_spiral:', d['n_spiral'])
print('f_sky:', d['fsky'])
print('sigma_decoupled[0:5]:', d['sigma_decoupled_per_bin'][:5])
"
# n_spiral: 3201160
# f_sky:    0.4914143880208333
# sigma_decoupled[0:5]: [6.097..., 2.232..., 2.626..., 2.229..., 2.470...]   ✓ matches rows 2-5
```

The SSOT acknowledges this heterogeneity ("ℓ=1 single-mode row anchors the dipole-parity null (n=5.55M analysis, explicitly disclosed); rows 2-5 are canonical N=3.2M / f_sky=0.491 bandpowers"), and footnote `fn:mc_count` explicitly documents the differing MC counts (500 for ℓ=1, 1000 for ℓ≥2). But the **galaxy-count and f_sky heterogeneity is not explicitly numerically disclosed in the table caption or row footnotes**. A reader sees a single table with five rows and presumes a single underlying catalog; the only way to discover that row 1 uses a 73% larger sample with a 34% larger sky fraction is to read the source JSONs.

This is materially relevant because the ℓ=1 single-mode statistic is **the load-bearing dipole-parity null** (paper line 1280, "canonical primary"), and its noise scale σ_null=0.429×10⁻⁶ is set by a different N and f_sky than the bandpowers it is presented next to.

**Fix:** Add a single line to the Table III caption (or to footnote `a` on the ℓ=1 row): *"The ℓ=1 single-mode row uses the 5,547,858-spiral / f_sky=0.659 MASTER pipeline run (`master_results/master_power_spectrum.json`); rows 2–5 use the canonical 3,201,160-spiral / f_sky=0.491 pseudo-C_ℓ run (`r42_results/wave_14_pp_namaster_verification.json`). The two N differ because the ℓ=1 single-mode estimator was run on an earlier inclusive-spiral cut before the equivariant Catalog-C n_spiral count was finalized; the canonical-N MASTER recompute at ℓ=1 specifically is on the post-arXiv-submission TODO list."*

The disclosure exists in the SSOT — the problem is it has not migrated into the paper text where the table lives.

---

## MINOR (good-to-fix; not blocking)

### m-DS-1 — Paper §I line 116 says "residual global CW excess of 9.5σ from 50/50 (CW fraction 0.4974 ± 0.000279)" — but CW fraction 0.4974 < 0.5 is a CCW excess (CW deficit), not a CW excess; this sign-of-the-claim wording is inconsistent with §V.A (line 788, "deficit"), §V.C (line 1104, "0.26% deficit"), and Table II row C (line 1171, "−0.26")

```bash
grep -n "CW excess\|CCW excess\|CW deficit\|0.4974" chirality_catalog_paper.tex | head -10
# 116: "A residual global CW excess of 9.5σ from 50/50 (CW fraction 0.4974 ± 0.000279)"   <- says "excess"
# 788: "deficit (0.4974 vs. 0.5000) operates at the 0.26% level"   <- says "deficit"
# 1104: "0.5000, a 0.26% deficit"   <- says "deficit"
# 1171: "C (equivariant) & 0.4974 ± 0.0003 & −0.26 & 9.5"   <- table column is "Excess (%)" with value -0.26
```

Verified from artifact:

```bash
python3 -c "
import math
n_cw, n_ccw = 1592107, 1609053
N = n_cw+n_ccw
p = n_cw/N
z = (p-0.5)/math.sqrt(p*(1-p)/N)
print(f'CW fraction = {p:.5f}, z = {z:.2f}σ ({\"CCW\" if z<0 else \"CW\"} excess)')
"
# CW fraction = 0.49735, z = -9.47σ (CCW excess)
```

Catalog C has |z| = 9.47σ → 9.5σ rounded, and the sign is **negative** (CCW excess / CW deficit). The paper says it correctly in 4 places and incorrectly in 1 place (the §I abstract-region wording). Easy one-word fix: change "CW excess" to "CCW excess" (or, more conservatively, "departure from 50/50") at line 116.

This is not a confabulation against artifacts — the **magnitude** 9.5σ is verified — it is an internal-consistency wording bug that survives from pre-R42 rounds. A non-Anthropic referee comparing line 116 against Table II row C will flag it; it is one of the easier "this paper hasn't been edited carefully" tells.

---

## VERIFIED CLAIMS (closed; do not reopen)

The following v1.0.48/v1.0.49 numerical claims **reproduce exactly** from on-disk artifacts and require no further action:

| Paper claim | Value | Artifact | Verified |
|---|---|---|---|
| Equivariant production catalog count | **3,201,160 spirals** | `wave_14_pp_namaster_verification.json` (`n_spiral`) | ✓ exact (33 occurrences in paper) |
| Total joined sample | **8,474,531 galaxies** | `outputs/dipole/summary.json` (`catalog.n_total`), `wave_14_kk_ba_reconciliation_results.json` | ✓ exact |
| Edge-on subsample (b/a<0.3) | **785,859 galaxies** | `wave_14_kk_ba_reconciliation_results.json` (`table[2].n_total`) | ✓ exact |
| Bin-to-bin CW-fraction spread (4 b/a bins) | **0.0005 (0.05%)** | `wave_14_kk_ba_reconciliation_results.json` recomputed from n_cw_eq / n_ccw_eq | ✓ exact (0.000513) |
| 9.5σ monopole magnitude | **0.0026 (0.26%)** | derived from `n_cw=1,592,107, n_ccw=1,609,053` | ✓ exact (\|z\|=9.47σ, deviation=0.265%) |
| Table III ℓ_eff=4 = +6.10σ | **+6.097σ** | `wave_14_pp.sigma_decoupled_per_bin[0]` | ✓ exact |
| Table III ℓ_eff=9..24 (rows 3-6 of pseudo) | +2.23 / +2.63 / +2.23 / +2.47σ | `wave_14_pp.sigma_decoupled_per_bin[1:5]` | ✓ exact match |
| Joint χ²/dof = **161.2 / 38 = 4.24** | sum of σ_decoupled² over 38 bandpowers | `wave_14_pp.sigma_decoupled_per_bin` | ✓ exact (161.197) |
| Pre-MASTER pseudo-C_ℓ at ℓ=1 = **6.48σ** | `wave_14_pp.sigma_pseudo_per_bin[0]` | same JSON | ✓ exact (6.485) |
| Pre-TTA real-space dipole = **2.31σ** | `outputs/dipole/summary.json` (`dipole.significance_sigma`) | same | ✓ exact (2.3120) |
| McNemar Z = **13.4** | `B20_B21_results.json` confusion_eq cells b=18889, c=16377 | computed | ✓ exact (Z=13.376) |
| Cohen κ = **0.40** | same 2×2 (CW/CCW only): p_obs=0.699, p_chance=0.500 | computed | ✓ exact (κ=0.3978) |
| GZ1 cross-match spirals = **117,205** | `B20_B21_results.json` (`n_spiral_eq`) | direct field | ✓ exact (also: 39011+18889+16377+42928 = 117205) |
| Catalog A raw bootstrap = **+28.80σ** | A=0.01576, σ_boot=5.47×10⁻⁴ → 28.81 | `chirality_summary.json` (cw=1,687,069 / ccw=1,634,726) | ✓ exact (analytic Poisson 28.72σ; bootstrap 28.81σ) |
| fracdev (0.5, 0.6] bin n=**10,941** | `wave_14_oo_bin_flatness.json` (denominators.full_spiral.axes.fracdev) | direct | ✓ exact |
| Catalog C CW fraction = **0.4974** | n_cw/(n_cw+n_ccw) = 1592107/3201160 | wave_14_pp + chirality_summary cross-check | ✓ exact (0.49735) |

15 numerical claims reproduce exactly from on-disk JSONs. The v1.0.48 confabulation scrub (94.6σ → 2.31σ replacement) and the v1.0.49 deferred-task closures (Rotation-TTA bound, Table III σ_null, binned-fraction figure, joint χ²/dof) are **artifact-backed except for the one arithmetic overstatement flagged in B-DS-1**.

---

## SUMMARY

**Counts:** 1 BLOCKER · 1 MAJOR · 1 MINOR · 0 NIT = **3 findings**

**Δ vs R-round-2 (1052 PDT):** −1 BLOCKER (B-DS-1 94.6σ closed via v1.0.48 scrub), −1 BLOCKER (B-DS-2 Table III gap closed via v1.0.49 reconstruction), −3 MAJOR (M-DS-1, M-DS-2, M-DS-3 closed; remaining M-DS-1 here is a fresh heterogeneity-disclosure ask, not a recurrence), −5 MINOR, −4 NIT. **Net −13 findings** between R2 and R3.

**Most concerning:** B-DS-1 — the "30× smaller than the monopole" arithmetic is wrong by 5.7× in a brand-new v1.0.48 closure paragraph. Real ratio is 5.3×, computable from two numbers sitting two clauses upstream of the claim. Fix is a one-word edit ("30×" → "5×") or a rephrase ("a factor of ~5 below the 0.26% monopole").

**Readiness recommendation:** the artifact-backing on v1.0.49 is genuinely strong — 15 numerical claims reproduce exactly. Once B-DS-1 (arithmetic), M-DS-1 (table caption disclosure), and m-DS-1 (CW/CCW excess wording) close, the paper is artifact-clean from a confabulation-hunter perspective. No further deferred σ-values, no headline-vs-artifact gap, no invented denominators.

**Standing constraint:** B-DS-1 should be fixed in a same-commit recompile and surface re-mirror per the PDF recompile/restamp protocol. The fix is trivial (one number) so there is no excuse to defer.
