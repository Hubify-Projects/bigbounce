# P4 R-round — DeepSeek-V3.5 Adversarial Confabulation-Hunter Review

**Reviewer simulated:** DeepSeek-V3.5 (confabulation specialty; matches numerical claims to on-disk artifacts and hunts arithmetic inconsistencies; non-Anthropic perspective)
**Date:** 2026-05-13 10:52 PDT
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.47, 2,732 lines, 38 bibitems, compiled PDF 25,707,541 bytes, 26 pp.
**Mode:** R-round adversarial. Focus: paper-claimed numbers vs on-disk JSON artifacts. Internal arithmetic consistency.

**Headline:** 2 BLOCKER · 4 MAJOR · 6 MINOR · 4 NIT = **16 findings** total.

---

## BLOCKERS (must close before submission)

### B-DS-1 — The headline "94.6σ → 0.43σ" collapse has no reproducible artifact for the pre-TTA endpoint; the only saved raw-dipole significance on disk is **2.31σ**, not 94.6σ

The paper invokes "94.6σ" as the **headline pre-TTA dipole significance** at 10 sites (lines 77, 217, 256, 1097, 1699, 1703, 1713, 1725, 1739, 1759, 1809) and treats the "94.6σ → 0.43σ" collapse as the bias-hardening narrative spine (§VI.A, fig:raw_vs_eq, conclusions). However:

| Claim location (line) | Paper value | On-disk artifact | Value in artifact |
|---|---|---|---|
| L77 ("fake a $94.6\sigma$ pseudo-dipole") | 94.6σ | `pipelines/p2_chirality/outputs/dipole/summary.json` (`dipole.significance_sigma`) | **2.3119654291** |
| L1097 ("the $94.6\sigma$ dipole") | 94.6σ | same | 2.31σ (rebuild_note: "PRE-TTA pipeline run (2.31 sigma)") |
| L1713 ("collapse from $94.6\sigma$ to $0.43\sigma$") | 94.6σ → 0.43σ | summary.json pre_tta=true + `pod2_chirality_2026-04-29/dipole_catalog_c.json` post-TTA | 2.31σ → 0.43108σ |

The 94.6σ figure appears in only two places on disk: (1) **prose/commentary** in closure JSON `pipelines/p3_anomaly_engine/r42_results/wave_14_zz_p4_oa_m9_closure.json` (where it is asserted as a `key_argument` string, not computed); (2) the paper's own LaTeX source. **No JSON / NPZ / parquet artifact stores 94.6 as a computed significance value.** The pre-R42 skeptical reviewer already flagged this exact discrepancy on 2026-04-18: "the mismatch between the pre-TTA artifact (2.31σ, fitted axis 18.9° from Shamir's axis) and the post-TTA result deserves a dedicated paragraph, not a footnote" (`project-context/peer-reviews/autonomous-2026-04-18/04_paper4_dipole_skeptic.md` L15).

**The two numbers describe different objects** (94.6σ is presumably a pseudo-C_ℓ derived from Catalog A's raw labels under mask-coupled normalization; 2.31σ is the simple real-space dipole fit), but the paper presents 94.6σ as if it were the headline pre-TTA dipole. A reader who pulls `summary.json` finds 2.31σ, not 94.6σ — that is the textbook definition of an unreproducible headline.

```bash
# Show only artifact-backed pre-TTA dipole significance on disk:
python3 -c "import json; d=json.load(open('pipelines/p2_chirality/outputs/dipole/summary.json')); print('pre_tta:', d['dipole']['pre_tta'], 'sigma:', d['dipole']['significance_sigma'])"
# pre_tta: True sigma: 2.3119654291443537

# Hunt 94.6 as a numerical (not string) artifact:
find pipelines -name "*.json" | xargs grep -l '"significance_sigma":[ ]*94' 2>/dev/null
# (no output)
```

**Fix paths (pick one, not both):**
- **(a) Reproduce 94.6σ in a saved artifact.** Re-run the raw-Catalog-A pseudo-C_ℓ at ℓ=1 under the paper's claimed normalization (N_spiral=3,201,160, f_sky=0.491) and save the resulting significance to a JSON. Cite that JSON path next to every "94.6σ" claim. Then 94.6σ is artifact-backed and the issue closes.
- **(b) Demote the headline.** Replace "94.6σ → 0.43σ" everywhere with "2.31σ simple-dipole real-space fit collapses to 0.43σ post-TTA" (the only artifact-backed pair). Reserve any pseudo-C_ℓ-derived sigma for a quantitatively-cited line referencing the pseudo-C_ℓ run, not the real-space dipole.

Either path is fine. The current state — a 10-instance headline number with no underlying JSON — is the kind of thing a non-Anthropic referee will catch in the first 30 minutes and use to argue confabulation across the rest of the manuscript.

---

### B-DS-2 — Table III rows 2–5 do not reproduce from any on-disk MASTER pseudo-C_ℓ artifact; the only artifact that backs row 1 is the **superseded** Apr-28 master_power_spectrum.json (n_galaxies=5,547,858, f_sky=0.659), which is inconsistent with the paper's claimed canonical (N_spiral=3,201,160, f_sky=0.491)

Paper Table III (L1146–L1150) reports:

| Bandpower (ℓ_eff) | C_ℓ × 10⁶ | σ | Interpretation |
|---|---|---|---|
| 4 (ℓ∈[2,6]) | **1.494** | **−0.122** | Null (MASTER-deconvolved) |
| 9 (ℓ∈[7,11]) | **1.546** | **1.47** | Null |
| 14 (ℓ∈[12,16]) | **1.81** | **1.63** | Null |
| 19 (ℓ∈[17,21]) | **0.88** | **0.91** | Null |
| 24 (ℓ∈[22,26]) | **1.12** | **1.22** | Null |

Compared against the two MASTER pseudo-C_ℓ artifacts in the repo:

```bash
# Apr 28 master_power_spectrum.json (paper §V's claimed source for ell1):
python3 -c "
import json; d=json.load(open('pipelines/p2_chirality/master_results/master_power_spectrum.json'))
print('n_galaxies:', d['n_galaxies'], 'f_sky:', d['f_sky'])
for i in range(5):
    print(f\"  ell={d['ells_effective'][i]}: Cl_master={d['Cl_master_decoupled'][i]*1e6:.3f}\")
"
# n_galaxies: 5547858  f_sky: 0.6588541666666666
#   ell=4.0:  Cl_master=1.494   <-- matches paper row 1 C
#   ell=9.0:  Cl_master=1.572   <-- paper row 2 says 1.546 (MISMATCH)
#   ell=14.0: Cl_master=1.157   <-- paper row 3 says 1.81  (MISMATCH)
#   ell=19.0: Cl_master=1.732   <-- paper row 4 says 0.88  (MISMATCH)
#   ell=24.0: Cl_master=1.639   <-- paper row 5 says 1.12  (MISMATCH)

# May 1 wave_14_pp_namaster_verification.json (canonical N_spiral=3.2M, f_sky=0.491):
python3 -c "
import json; d=json.load(open('pipelines/p2_chirality/r42_results/wave_14_pp_namaster_verification.json'))
print('n_spiral:', d['n_spiral'], 'fsky:', d['fsky'])
for i in range(5):
    print(f\"  ell={d['ells_effective'][i]}: cl_pseudo={d['cl_pseudo_corrected'][i]*1e6:.3f}, sigma_decoupled={d['sigma_decoupled_per_bin'][i]:.3f}\")
"
# n_spiral: 3201160 fsky: 0.4914143880208333
#   ell=4.0: cl_pseudo=1.173, sigma_decoupled=6.097   <-- paper row 1 says 1.494/-0.122 (MISMATCH)
#   ell=9.0: cl_pseudo=-0.023, sigma_decoupled=2.232  <-- paper row 2 says 1.546/1.47 (MISMATCH)
#   ell=14:  cl_pseudo=-0.198, sigma_decoupled=2.626  <-- paper row 3 says 1.81/1.63 (MISMATCH)
```

**Findings:**

1. Table III row 1 (ℓ_eff=4: C=1.494, σ=−0.122) matches only the Apr-28 `master_power_spectrum.json` (`Cl_master_decoupled[0]=1.494e-6`, `ell1_dipole.significance_sigma=-0.12189`). That artifact uses **n_galaxies=5,547,858 and f_sky=0.659**, which the paper itself supersedes in §V (canonical N_spiral=3,201,160, f_sky=0.491). The headline post-MASTER −0.122σ is therefore traceable only to an artifact whose normalization the paper has explicitly retired.

2. Table III rows 2–5 (1.546/1.47, 1.81/1.63, 0.88/0.91, 1.12/1.22) **match neither artifact**. The Apr-28 file gives C_ℓ values (1.572, 1.157, 1.732, 1.639) that disagree at the ≥10% level on every row. The May-1 canonical-N run gives entirely different magnitudes (sub-microcosmic for ell≥2 after subtraction) and per-bin significances of 6.1, 2.2, 2.6, ... (none of which round to 1.47/1.63/0.91/1.22).

3. The v1.0.47 closure changelog (SSOT paper-4/status.md) says "B3 Table III column relabel ... post-MASTER −0.122σ headline now arithmetically reproducible from displayed 3-sig-fig values" and "M3 Table III values bumped to 3 sig figs." But arithmetic reproducibility from 3-sig-fig column values is a different claim than artifact reproducibility. The 3-sig-fig display does let you back out σ = (C_master − ⟨C_null⟩) / σ_null if you trust C=1.494 — but C=1.494 itself doesn't trace to the canonical-N run.

**Fix:** Re-run the MASTER pseudo-C_ℓ pipeline at the paper's claimed canonical normalization (N_spiral=3,201,160, f_sky=0.491) and save the bandpower-binned C_ℓ + per-bin σ for ℓ_eff = 4, 9, 14, 19, 24 to a fresh JSON. The headline post-MASTER −0.122σ at ℓ=1 plus the four null-consistent higher bins must all originate from the same artifact under the same normalization. Cite that JSON path in the Table III caption.

---

## MAJORS

### M-DS-1 — `n_galaxies=5,547,858` in `master_results/master_power_spectrum.json` is never mentioned in the paper but is the source of the headline −0.122σ; paper claims canonical-N=3,201,160 throughout

Direct consequence of B-DS-2. Line 974–977 derives σ_pop = √(p(1−p)/N) = 0.000279 from N=3,201,160 (verified arithmetically below). But the paper's signature −0.122σ dipole comes from a NaMaster run on **n=5,547,858 galaxies** (5.55M, mid-way between full catalog 8.47M and spiral subset 3.2M). Where does 5.5M come from? It is consistent with a CW-confidence-cut subset of all 8.47M galaxies (not just spirals), or some other intermediate selection — but the paper never declares this. Reader pulls the JSON, sees 5,547,858, has no idea what slice this is.

**Fix:** Add a one-line provenance footnote at Table III caption: "Bandpower estimates derived from `master_results/master_power_spectrum.json`, which operates on a [exact selection definition] sample of n=5,547,858 galaxies. The canonical N_spiral=3,201,160 normalization in §V applies to the simple-dipole and CW-fraction estimators; the MASTER pseudo-C_ℓ uses [reason for different selection]." Or — preferably — re-run on the canonical 3,201,160 subset and let Table III come from a single artifact with a single N.

### M-DS-2 — Paper-claimed v1.0.47 closure "Table III headline now arithmetically reproducible from displayed 3-sig-fig values" is true only for row 1; rows 2–5 are not arithmetically self-consistent against any displayed null-mean

Paper L1146–L1150 lists C_ℓ and σ but not the null-mean ⟨C^null⟩ or null-std σ_null per bin. Row 1: σ = (1.494 − 1.546) / 0.429 ≈ −0.121 reproduces the displayed −0.122 to rounding. Rows 2–5 cannot be independently arithmetic-checked from the displayed values alone — the reader would have to assume the same null_std=4.29e-7 from ell1_dipole, but that null_std is computed at ℓ=1, not at ℓ=9/14/19/24. The mc_std for higher bins is 5.7e-7, 4.5e-7, etc. (from wave_14_pp), which gives a completely different per-bin σ.

**Fix:** Add a "C_ℓ^null" and "σ_null" column (or footnote-row giving per-bin null statistics) so the displayed σ in column 3 actually reproduces from the other displayed columns. Without this, the "arithmetically reproducible" claim only covers the first row.

### M-DS-3 — `paperTimestamp` says "2026-05-12 00:00 PDT" but PDF mtime is May 11 17:41 2026 PDT; the date stamped on the title page is 7 hours in the future of the compile

```bash
ls -la pipelines/p2_chirality/chirality_catalog_paper.pdf
# May 11 17:41:47 2026
grep paperTimestamp pipelines/p2_chirality/chirality_catalog_paper.tex
# \newcommand{\paperTimestamp}{2026-05-12 00:00 PDT}
```

The mismatch is small and easily explained as "midnight rounding," but for arXiv submission the date on the title page should match the compile date or the intended submission date. A v1.0.47 dated 2026-05-12 compiled at 2026-05-11 17:41 will draw a "stale recompile?" question from a referee.

**Fix:** Either recompile on 2026-05-12 (so PDF mtime > paperTimestamp) or back-date the timestamp to the actual compile date.

### M-DS-4 — Golden:2026 P1A/P2/P3 self-references are "in preparation" bibitems with internal report numbers (Hubify-2026-001/002/003) but the in-text \cite{} calls (L151–L154) don't visually signal placeholder status to a referee

```latex
% L2663-L2675
\bibitem{Golden:2026P1A}
H.~Golden, "Einstein-Cartan-Holst Spin-Torsion Cosmology: ...",
in preparation (2026), Hubify-2026-001.
% (similarly for P2 and P3)
```

```latex
% L151-L154 in-text
program; the spin-torsion no-go (Paper~I; \cite{Golden:2026P1A}),
... (Paper~II; \cite{Golden:2026P2}), ...
(Paper~III; \cite{Golden:2026P3}) cover orthogonal observational
```

These are companion-papers-in-progress. The bibitem text says "in preparation (2026)" but the in-text rendering ("Paper~I; [38]") looks like a normal published reference. arXiv referees will check the citation list and discover three unpublished self-citations; that is fine if disclosed, mildly suspicious otherwise.

**Fix:** Add "(companion paper, in preparation)" parenthetical at first cite of each (L151, L153, L154), or add a footnote at first cite stating "Companion papers P1A, P2, P3 are in preparation and will appear on arXiv in [month] 2026."

---

## MINORS

### m-DS-1 — Verified-OK list (confabulation sweep negatives; documented for audit trail)

The following claims **do** reproduce from on-disk artifacts:

| Claim | Paper value | On-disk artifact | Status |
|---|---|---|---|
| Catalog total | 8,474,531 galaxies | `wave_14_pp_namaster_verification.json.n_total` | ✓ matches |
| Canonical spiral N | 3,201,160 | `wave_14_pp.n_spiral`, `wave_14_oo.n_input`, `wave_11c.n_spiral` | ✓ matches across 3 artifacts |
| CW raw count | 1,592,107 | `wave_14_pp.n_cw` | ✓ matches |
| CCW raw count | 1,609,053 | `wave_14_pp.n_ccw` | ✓ matches |
| CW fraction (Catalog C eq) | 0.49735 | `wave_14_pp.cw_fraction_global = 0.49735314698` | ✓ matches |
| σ = √(p(1−p)/N) | 0.000279 | computed: 0.0002795 ✓ | ✓ arithmetic reproduces |
| 9.5σ monopole | (0.5−0.49735)/0.000279 = 9.47σ → rounded 9.5σ | ✓ arithmetic reproduces |
| GZ1 accuracy spiral-only | 69.91% | `B20_B21_results.json.spiral_only_CW_vs_CCW_eq = 0.6991084` | ✓ matches |
| Platt A = 1/4.65 ≈ 0.21505 | 0.21505 | `wave_14_fff_gz1_platt_recal.json.platt_orig.A = 0.21505376` | ✓ matches |
| Platt B = −1.58 | −1.58 | `wave_14_fff_gz1_platt_recal.json.platt_orig.B = -1.58` | ✓ matches |
| L-BFGS recalibration at chance | 0.519 | `wave_14_fff.calibration_quality.gz1.accuracy = 0.51935154` | ✓ matches |
| Catalog A raw bootstrap A | 0.01576 | computed from CW=1687069, CCW=1634726: (CW-CCW)/(CW+CCW) = 0.01576 ✓ | ✓ matches |
| Catalog A raw monopole | 28.8σ | computed: (0.50788−0.5)/√(0.25/3321795) = 28.72σ ≈ 28.8 ✓ | ✓ matches |
| Post-MASTER ell=1 σ | −0.122σ | `master_power_spectrum.json.ell1_dipole.significance_sigma = -0.12189` | ✓ matches (but see M-DS-1 caveat on N) |
| Post-TTA simple dipole | 0.43σ | `pod2_chirality_2026-04-29/dipole_catalog_c.json.sigma = 0.43108` | ✓ matches |
| Raw pseudo-C_ℓ ell=1 | 6.48σ | `wave_14_pp.sigma_pseudo_per_bin[0] = 6.4847` | ✓ matches |
| Raw pseudo-C_ℓ decoupled ell=1 | 6.08σ | `wave_14_pp.sigma_decoupled_per_bin[0] = 6.0973` | ✓ matches |
| ℓ_eff=4 spans ℓ∈[2,6] | ℓ_eff=4 | `wave_14_pp.ells_effective[0] = 4.0` | ✓ matches |
| f_sky = 0.491 | 0.491 | `wave_14_pp.fsky = 0.49141438` | ✓ matches (per canonical) |

This list is the confabulation-hunt negative-control. The B-DS-1 and B-DS-2 findings are not "everything is wrong"; they are the two specific gaps in an otherwise well-traced numerical foundation. Worth keeping the audit trail of negatives so future R-rounds can skip these.

### m-DS-2 — Paper line 1338 (Fig 11 caption text) still refers to "the original raw pseudo-C_ℓ (ℓ=1 at 2.75σ relative to the original shot-noise floor)"; the 2.75σ is the same superseded snapshot value explicitly retired elsewhere

```latex
% L1338
Note: the figure as plotted shows the original raw pseudo-$C_\ell$
($\ell=1$ at $2.75\sigmaunit$ relative to the original shot-noise floor).
After the corrected $N_{\rm spiral}$ normalization the pseudo-$C_\ell$
SNR is $6.48\sigma$ ...
```

This is honest — the caption explicitly says "the figure shows the old value, the corrected value is 6.48σ" — but a referee may flag the figure-display/text-display inconsistency. The footnote works; better would be to regenerate Fig 11 with the corrected 6.48σ value so the caption text matches the figure axis. (SSOT m6 already says "P4 Fig 11 DPI regen pending"; align that with the σ-value fix too.)

### m-DS-3 — `master_power_spectrum.json` reports `f_sky=0.6589` and the pod2 SUMMARY.md reports `f_sky=0.4928`; paper claims `f_sky=0.491` (canonical) and `f_sky≈0.46` in narrative passages

Three different f_sky values for what should be the same survey mask:

| Source | f_sky |
|---|---|
| Paper L1175 ("DESI Legacy footprint covers f_sky ≈ 0.46") | 0.46 |
| Paper L1195, L1213, L1264 (production canonical) | 0.491 |
| Paper L1280 ("12 binned, f_sky=0.4928") | 0.4928 |
| Paper L1868 ("coverage f_sky ≈ 0.46") | 0.46 |
| Paper L1953 ("f_sky≈0.32, finite across all seven proxies") | 0.32 |
| Paper L2001 ("spirals/pixel cut, f_sky=0.4240") | 0.424 |
| `master_results/master_power_spectrum.json.f_sky` | 0.6589 |
| `wave_14_pp_namaster_verification.json.fsky` | 0.4914 |
| `pod2/master_power_spectrum.json` (per SUMMARY.md) | 0.4928 |

Different mask cuts / different binnings legitimately give different f_sky values. The paper does (mostly) disclose this. But the appearance of 7 different f_sky figures across the paper without a single comparison table will draw a referee question. Tighten by adding a one-line "f_sky table" or by glossing each instance ("at the ⟨X⟩ binning, f_sky = 0.Y; at the ⟨Z⟩ binning, f_sky = 0.W").

### m-DS-4 — fn:mc_count footnote uses 1/√(2(N−1)) for N=500, gives 3.2%; the paper has 0.122σ deviation with 3.2% MC error on σ_null; the |deviation|/σ_null = 0.12σ is BELOW the 3.2% MC noise floor on σ_null itself, so the −0.122σ result is consistent with "MC-precision-limited zero"

The fn:mc_count footnote (L1078) correctly identifies that σ_null at N_MC=500 has a 3.2% relative standard error. With C1_null_std = 4.29e-7 (from ell1_dipole), the SE on σ_null itself is ≈ 1.4e-8. The reported signal (C1_signal = 2.36e-7) is 0.55 × σ_null, giving |significance| = 0.12σ.

But 0.12σ is **smaller** than the 3.2% MC noise on σ_null, which means: if you re-ran the MC null with a different seed at N=500, σ_null could shift by ~3.2%, and the reported significance would jitter accordingly. The footnote says "3.2% relative SE on σ_null is well below the |0.12σ| deviation" — but 3.2% of 0.12σ is 0.004σ, which the footnote claims is the comparison. The actual comparison should be "is the σ_null itself stable to within better than the noise floor at which we are claiming null." It is, narrowly.

This isn't wrong, but the wording is a bit slippery — "3.2% relative SE on σ_null is well below the |0.12σ| deviation" reads as "MC noise is well below signal," but the signal IS the MC-precision-limited null (the null is the signal here). Reframe to: "σ_null is stable to 3.2% at N_MC=500; the |−0.12σ| result is consistent with null at MC-precision."

### m-DS-5 — The "94.6σ → 0.43σ" arithmetic does not check against the M_ℓℓ^−1 mode-coupling inversion language M4 promises

SSOT closure (v1.0.47, M4): "M_ℓℓ⁻¹ mode-coupling inversion language replaces 'factor of ~2' handwave for 6.48σ→−0.122σ post-MASTER collapse." The paper §V text now does explain the 6.48σ → −0.122σ collapse via M_ℓℓ⁻¹. But the **94.6σ → 0.43σ collapse** (which the paper presents as the headline) is a *different* collapse — it's the raw real-space dipole on Catalog A (uncorrected labels) collapsing to the equivariant Catalog C real-space dipole. The M_ℓℓ⁻¹ explanation does not apply; that's mode-coupling deconvolution of pseudo-C_ℓ, not Catalog-A → Catalog-C equivariant averaging.

The paper conflates the two collapses by listing them adjacent in the narrative without distinguishing the mechanisms. Eq.~(tta) drives 94.6σ→0.43σ; M_ℓℓ⁻¹ drives 6.48σ→−0.122σ. They are independent reductions and should be presented as such, not stacked.

**Fix:** L1714, L1739, L1714–L1720 paragraph: rewrite to clarify "the 94.6σ → 0.43σ collapse is driven by equivariant TTA averaging on the real-space asymmetry map; the 6.48σ → −0.122σ collapse is driven by MASTER mode-coupling deconvolution in spherical-harmonic space. The two are independent and address different systematics."

### m-DS-6 — "28.80σ" bootstrap-derived asymmetry significance (L995) is artifact-backed (matches 28.72σ analytic Poisson), but the paper presents it inside a parenthetical that downplays it ("not an external-validation σ")

The 28.80σ figure reproduces ((CW−CCW)/(CW+CCW) bootstrap on Catalog A raw spirals; analytic Poisson 28.72σ ≈ rounded 28.8σ). The paper's clarification "the 28.80σ figure is the bootstrap-stability metric of the chirality-fraction estimator, not an external-validation σ" is the right disclaimer.

But the paper does not separately quote the analytic 28.7σ Poisson value, so a reader gets the bootstrap-stability number with a "not external-validation" disclaimer and is left wondering what the actual analytic asymmetry significance is. Add one sentence: "The analytic Poisson asymmetry significance is 28.7σ (from p = 0.50788, N=3,321,795); the bootstrap stability gives 28.80σ as a self-consistency check."

---

## NITs

### n-DS-1 — L1280 says "12 binned" but the artifacts show 38 bandpower bins (ells_effective[0..37])

Probably a typo or stale text. The wave_14_pp and master_power_spectrum both report 38 ℓ_eff bins (4, 9, ..., 189). "12 binned" should be "38 binned" or whatever the production binning actually is.

### n-DS-2 — `\paperVersion = v1.0.47` is invoked in `\date{}` macro but the v1.0.47 SSOT update note in `paper-4/status.md` says "v1.0.46 → v1.0.47 (Houston-directed standalone-publication readiness wave)"; that the paper is at v1.0.47 is correct, but it would help future reviewers if the title-page date line included a "(R-round closure: 14/15 R42-multi-vendor MAJORs)" footnote so they don't have to dig into SSOT

### n-DS-3 — Hubify-2026-001 / 002 / 003 internal report numbers in self-cite bibitems will look weird on arXiv (no one outside the project knows what "Hubify-202X-NNN" means)

Either drop the report numbers or expand the bibitem to say "Hubify Labs internal report 2026-001" (still vague) or convert to a footnote pointer ("companion preprint, in preparation, will appear at arXiv:2606.XXXXX").

### n-DS-4 — `chirality_catalog_paper_arxiv_submission.tar.gz` (20MB) is dated Apr 18 2026, which is older than v1.0.25 and predates 25 of the 47 version bumps in the changelog

```bash
ls -la pipelines/p2_chirality/chirality_catalog_paper_arxiv_submission.tar.gz
# -rw-r--r--  20150714  Apr 18 12:48
```

If this tarball is meant to be a "ready to submit" artifact, it is stale by ~3.5 weeks and ~22 version bumps. Re-tar from the v1.0.47 sources before submission.

---

## Summary verdict

**16 findings: 2 BLOCKER · 4 MAJOR · 6 MINOR · 4 NIT.**

The numerical foundation of P4 v1.0.47 is genuinely well-traced — 18 separate claims reproduce exactly against on-disk JSON (see m-DS-1 audit table). This is a paper with real artifacts behind real numbers, which is more than most cosmology papers can say.

**Most concerning single confabulation (one sentence as requested):**

> The paper's headline "94.6σ → 0.43σ" collapse appears 10 times as the bias-hardening narrative spine, but the only on-disk pre-TTA dipole significance is **2.31σ** in `outputs/dipole/summary.json` (rebuild_note explicitly: "PRE-TTA pipeline run (2.31 sigma)"), and no JSON / NPZ / parquet artifact in the repo stores 94.6 as a computed significance — only as a prose assertion inside `wave_14_zz_p4_oa_m9_closure.json` and the paper's own LaTeX source.

Close B-DS-1 by either (a) re-running the raw-Catalog-A pseudo-C_ℓ pipeline and saving 94.6σ to a JSON, or (b) demoting the headline to the artifact-backed 2.31σ → 0.43σ pair.

Close B-DS-2 by re-running MASTER pseudo-C_ℓ on the paper's claimed canonical normalization (3,201,160 spirals at f_sky=0.491) so Table III rows 1–5 all come from a single JSON under a single N — not from the superseded 5.55M / 0.659 file for row 1 and from-thin-air for rows 2–5.

With those two closures (estimated 2–4 pod-hours of compute + ~30 lines of LaTeX edits), P4 is genuinely arXiv-ready by the confabulation standard. Without them, a non-Anthropic referee will catch B-DS-1 in the first 30 minutes and use it to argue the rest of the paper deserves the same scrutiny.

Readiness assessment under the 99%-cap rule: this review identifies real artifact gaps that postdate the v1.0.47 SSOT closure note; readiness should sit at **88–90%** (down from the claimed 92%, but only because two artifact-traceability gaps surfaced in this round; the headline science remains sound).
