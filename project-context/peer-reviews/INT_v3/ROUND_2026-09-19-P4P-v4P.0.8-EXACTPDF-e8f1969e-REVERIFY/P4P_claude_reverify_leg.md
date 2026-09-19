# P4′ v4P.0.8 — Claude INT referee leg, re-verification round

**Reviewer leg:** Claude INT (independent ApJS referee, verdict-blind)
**Model:** claude-opus-5[1m]
**Manuscript:** `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p4prime_chirality_test/paper/main.pdf`
**sha256:** `e8f1969e415777622561dde0f21a8ac7d6398c3b2ef55f69200ba50a89d91cd2`
**md5:** `b2399780320a50542279c35410b6b545`
**Pages:** 14 · **Producer:** pdfTeX-1.40.29 · **PDF CreationDate:** 2026-09-18 23:03:53 PDT
**Version stamp on p.1:** `(Dated: September 18, 2026; Version v4P.0.8)` — matches `\paperVersion`/`\paperTimestamp` (main.tex L61–62).
**Source:** `main.tex`, 1368 lines. Compile log: 0 undefined references, 0 multiply-defined labels, 1 Overfull \hbox (5.88 pt, L371–385), 2 "float is stuck" warnings (input L703).

**Scope of this review.** Full cold read of the whole manuscript, with extra scrutiny on §A.1 `sec:robustness_disclosure`. Every quoted number below was checked against the committed artifact it derives from (`row16i_full_parent_dipole.json`, `row16ib_axis_shift.json`, `row16ivb_bgs_environment.json`, `a95_observed_label_upper_limit_v1_0_265.json`, `a95_upper_limit_2026_09_02.json`, `outputs/a95_null_cl_2026_09_02.json`, `poplawski_dipole_exclusion_2026_09_02.json`, `g3_joint_estimator_covariance_master_v2.json`, `p4_primary_hc_safe_label_shuffle_10k_v1_0_257.npy`, `row16-image-level-injection-n20k.json`), or against the cited source papers `chirality_catalog_paper.tex` (v1.0.274) and `p5_desi_chirality.tex` (v0.1.147). No prior-round truth-audit or disposition file was read.

---

## PART 0 — Independently verified as CORRECT

Everything in this table was recomputed or matched byte-for-byte against the cited committed source. This is a long list because the manuscript's transcription discipline is, on the whole, unusually good.

| Claim (main.tex loc.) | Value in paper | Verification |
|---|---|---|
| Class counts (L177–179) | CW 1,592,107 / CCW 1,609,053 / NS 5,273,371; spiral 3,201,160; total 8,474,531 | sums exact |
| HC ladder (L186–195) | 949,584 HC − 59,515 unsafe = 890,069 → 887,472 in 23,633 pixels | `a95_..._v1_0_265.json`: `n_selected_rows`=890069, `n_galaxies_in_support`=887472, `n_pixels_support`=23633 ✔ |
| Primary f_CW (L288–290) | 0.5126562 = 454,968/887,472; monopole +1.2656%; A_p=+2.53% | JSON `p_cw_global`=0.5126561739, `n_cw_in_support`=454968; 454968/887472=0.51265617 ✔ |
| Catalog-wide monopole (L283–285) | f_CW=0.497353, −0.265%, A_p=−0.53% | 1,592,107/3,201,160=0.4973537; 2×(−0.0026463)=−0.529% ✔ |
| HC-with-unsafe monopole (L285–286) | 0.496051, −0.395%, A_p=−0.79% | consistent with ROW16IV §1 "sample mean s = f_CW−f_CCW = −0.788%" ✔ |
| Quarantine parity (L294–296) | 14,776 CW / 44,739 CCW = 59,515; 75.2% CCW | 44,739/59,515 = 0.75172 ✔ |
| GZ1 confusion matrix (Table 3) | row/col entries; N=240,919; 58.7%; 117,205; 69.91%; κ=0.40 | row sums 71,615+73,025+96,279=240,919; (39,011+42,928+59,499)/240,919=0.58707; spiral block sums to 117,205; 81,939/117,205=0.69911; κ recomputed = 0.3978 ✔ |
| Retrain held-out (L346–352) | n_total=8,637; 99.31%; 0.9867; κ=0.9733; confusion [[1460,10],[30,1500]] | 2960/3000=0.98667; κ recomputed = 0.97333 ✔ |
| CE-included collapse (L266–270) | 0.5617; 0.106 NS baseline + chance; binary 0.517 | P4 v1.0.274 L1056 verbatim (0.106+0.894×0.5=0.553) ✔ |
| Bias-hardening table (Table 4) | 1.000 / 89.8% / 100% / 84% / 3.6% / 73.6% / 49.7%; T5 removed; |z|≤1.25 | P4 v1.0.274 Table `tab:bias_tests` L1796–1802 + L1789 ✔ |
| Primary dipole (L423) | A=0.467% (0.4665%), z_mom=+0.635, p=0.238 | recomputed from the committed 10k null array: z=0.63465, rank p=0.23768 ✔ |
| Null moments (L459, L485) | 95th pct 0.669%; null mean 0.362% | null array: mean 0.3620291%, p95 0.6693182% ✔ |
| Neyman limit (L474–479) | A_95^CL≃0.75%; bracket 0.75%/p5=0.466%, 0.80%/p5=0.493% | `a95_upper_limit_...json`: 0.75082%; bracket p5 = 0.0046608 / 0.0049291 ✔ |
| Injection-recovery curve (L448, table L541–546) | 0.24@0.40%, 0.91@0.90%, 0.947@0.96%, 0.950@0.98%, 1.000@1.5%; 18 grid pts; 2,000 axes | JSON `per_amplitude`, `amplitude_grid_full_amp` (18), `n_axes_per_amplitude`=2000, `coverage_bracket`=[0.0096,0.0098,0.9465,0.95] ✔ |
| Logistic-vs-linear crossing (L552–554) | linear 0.980%, logistic 0.955%, "better than 0.03 pp" | JSON: 0.0098 / 0.0095478; Δ = 0.0252 pp ✔ |
| Joint covariance (L573–576) | 0.158 / −0.037 / 0.794 / −0.020 / 0.129 / −0.061 | `joint_correlation_4x4` exact ✔ |
| Bootstrap z's (L585–586) | +2.21 / +0.81 / −6.57 / −0.61 | `z_full_over_bootstrap_sigma` = 2.2073 / 0.8083 / −6.5669 / −0.6050 ✔ |
| DESIVAST ladder (L607–610, table) | 694,642 → 145,789 → 145,766 = 31,937 + 113,829 | sums exact; all five numbers present in P5 v0.1.147 ✔ |
| Void contrast (Eq. 3, L636–640) | Δf=+0.00145, SE=0.00332, CI [−0.00504,+0.00795], p=0.661, wild-cluster p=0.673, 99,999 draws, G=50 NSIDE=4 | P5 v0.1.147 L1005–1006, L2019: 0.00145442 / 0.00331502 / [−0.00504290,+0.00795174] / 0.66085 / 0.67345 ✔ |
| Clustering-scale sweep (L682–684) | NSIDE=2 [−0.00622,+0.00912]; NSIDE=8 [−0.00496,+0.00787]; 3-D [−0.00476,+0.00767]; point estimate fixed | P5 L2020 exact to 6 d.p. ✔ |
| Void-definition family (L685–694) | 5 estimators, \|z\|≤1.25 vs Bonferroni-5 2.58, max half-width 0.75 pp | P5 L1795–1810: half-widths 0.60/0.44/0.49/**0.75**/0.67 pp; z_Bonf=2.576 ✔ |
| T-Web bins (L647–649) | 428 / 6,673 / 408,187 / 397,505 = 812,793 | sum exact; all in P5 ✔ |
| T-Web bar values (Fig. 3 caption) | 0.4980 / 0.4958 vs 0.4974 reference | all present in P5; offsets 0.06 pp and 0.16 pp ✔ |
| Fisher scale reference (L972–977) | σ(A)=√(3/3,201,160)=9.7e-4, 3σ ≈ 0.29% | recomputed 9.681e-4 ✔ |
| Declination slabs (L962–966) | 7 slabs of 457,308–457,309; −0.110% to −0.463% | 7×457,308.57 = 3,201,160; P4 v1.0.274 L1289 ✔ |
| Table 5 ratios | 7.1 / 5.1 / 2.0 / 2.0 / 20.4 | low-end/0.98% recomputed exactly; `ratio_claim_low_to_A95_obs` in the committed json ✔ |
| g-bridge flags (L779) | Shamir 2020 & 2022 `exceeds_A95_obs_after_g_bridge=false`, other three true | committed json exact ✔ |
| "4–3,400× larger" (L99, L772) | | 887,472/200,000=4.4; 887,472/263=3,374 ✔ |
| Pixel-injection numbers (L990–994, Table 6) | +0.0167±0.0089; +0.434; 47σ; −0.0093; 2.9σ; N=20,000; 10 seeds; A_0=+0.59% | `row16-image-level-injection-n20k.json` verification string: +0.0167±0.0089, +0.4343, ~47σ, −0.00934, ~2.9–3.0σ, spiral-only A0=+0.59% ✔ |
| Implied ratio arithmetic (L1009–1012) | 0.0167/0.434≈0.038; 0.98%/0.038≈26% | 0.038479; 25.5–25.8% ✔ |
| Full-parent fit (L1048–1052) | 3,200,420 in support; A=0.566%; z=+4.44; RA 278.6°/Dec +25.3° | `row16i_full_parent_dipole.json`: 3200420, 0.00566028, z_moment 4.44016, 278.6297/25.3203 ✔ |
| Graded sweep (L1053–1057) | raw-flip-only removal → z=+0.68; primary_hc removal → z=+9.13 | `row16ib_axis_shift.json` C2 z=0.67719, C1 z=9.12976; direction of the two statements is correct ✔ |
| Leg/Galactic cuts (L1056–1059) | drop DES z=+0.48; no Galactic cut removes it; leakage floor 0.19% | JSON: C0 drop_DES z=0.47640; \|b\|>20 z=4.085, \|b\|>30 z=3.922; leakage 0.19099% ✔ |
| C3 leg values (L1067–1069) | drop DECaLS z=+4.19 A=2.21%; drop DES z=+4.26 A=1.39%; DES-only A=5.83% | JSON: 4.19176/2.2113%, 4.25679/1.389%, 5.8305% ✔ |
| Axis separation 107.5° (L1058–1059) | | `axis_separations_deg.C0_vs_C3`=107.5088; recomputed 107.5° ✔ |
| Structure battery z's (L1091–1098, Table 7) | −0.38, +0.17, −1.05 (from −2.37), −1.63, +0.21, −0.13, free 0.44% vs 0.38%±0.16% z=+0.32 | ROW16IV §2 (a)(b)(c)(d) exact ✔ |
| Shamir-axis "UNAVAILABLE, not fabricated" framing (L1106–1109) | | ROW16IV §1 + §4.2 — the paper's added clause "not because the cited works report no axis" is an honest strengthening ✔ |
| BGS table (Table 8) | all N, f_CW, σ, z | `row16ivb_bgs_environment.json` exact to 5 d.p. in every cell ✔ |
| BGS χ², rotation nulls, dipole \|z\|≤2.15 (L1174–1181) | 1.872 vs 1.984±1.841, z=−0.06 p=0.952; rot z=−0.12 p=0.917; proj z=−1.51 p=0.083; 10-realisation caveat | JSON + ROW16IVB §4.5 exact ✔ |
| LEE accounting (L1182–1187) | 14-statistic battery = 2×(3+1+3); p_local=0.0060 (=6/1000 empirical); ×14 → 0.084; threshold \|z\|≳3.7 | ROW16IVB §0.5; 0.0027/14=1.93e-4 → z=3.73 ✔ |
| "every tercile's median δ_k is overdense" (L1139–1141) | | medians 0.36/1.40/5.51 and 0.53/4.29/19.6, all δ_k>0 — the *substance* of this disclosure is correct (see A5 for the label) ✔ |
| Tracer inventory (L1194–1198) | BGS_BRIGHT-21.5, NGC+SGC, 0.1<z<0.4, 300,043 tracers, 4 randoms/cap → 6.0e6 | ROW16IVB §1 ✔ |
| All in-paper artifact paths | 12 `\artifact{}`/manifest targets | every one exists on disk and is git-tracked ✔ |

**Sections I found nothing wrong with.** §1 (Introduction), §2.3 (Estimator and null specification, apart from one cross-reference nit), §5.1 (What the model predicts — the reading of Poplawski 2010/2012/2016/2020 matches the committed exclusion script's `finding` field and is honestly scoped), §6 (Discussion) and §7 (Conclusions) are internally consistent and correctly hedged **as far as what they say goes**; my complaint about §5/§6/§7 is about what they omit (A3, A4). The bibliography is complete, correctly formatted, and the `Poplawski:2020` bibitem's self-declared year/identifier mismatch note is exactly the right disclosure.

---

## PART A — MAJOR findings

### A1. The pixel-injection baseline comparison names the wrong sample *and* the wrong amplitude convention

**Location:** main.tex L996–999; PDF p.10 (§A.1, "Pixel-level calibration").

**Claim:** "…the injection baseline itself is $A_0=+0.59\%$ for the spiral-classified population probed here, a different quantity from (and **opposite in sign to**) **the catalog's HC monopole** ($f_{\rm CW}-\tfrac12=-0.265\%$, Sec.~\ref{sec:catalog_classifier}), not the same baseline residual."

**What is wrong — two independent errors:**

1. **Wrong sample.** §2.2 (L283–290) of this same manuscript states three monopoles explicitly and −0.265% is the **catalog-wide** value across all 3,201,160 classified spirals. The **HC** monopole is −0.395% (949,584 rows, with the unsafe rows) or **+1.2656%** (the 887,472-row primary channel). The source doc for the structure battery states this in exactly the paper's own convention: `ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md` §0.2 — *"The catalogue carries a residual handedness monopole (P4′: injection-calibrated residual, **HC monopole f_CW − 1/2 = +1.2656%**)"*. Calling −0.265% "the catalog's HC monopole" contradicts both the source and §2.2 of this paper.

2. **Wrong convention, hence the sign claim fails.** $A_0$ is an asymmetry *amplitude*, $A=(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})$ — the manifest is explicit: `row16-image-level-injection-n20k.json` → *"the spiral-classified-only baseline is A0=+0.59%, same order as the paper's -0.26%, opposite sign"*, and *"Baseline pixel-level asymmetry A0=-21.72%"*, both in the $N_{\rm CW}-N_{\rm CCW}$ convention. The paper's own §2.2 says the catalog-wide value in that convention is $A_p=-0.53\%$, **not** $-0.265\%$. So the sentence compares a full amplitude to a half-amplitude — precisely the convention slip §2.2 goes out of its way to prevent by quoting both.

   Worse, if the comparator is taken to be the **primary channel** (as the words "HC monopole" require), the primary channel's monopole is $+1.2656\%$ ($A_p=+2.53\%$) — the **same** sign as $A_0=+0.59\%$, so "opposite in sign to" is simply false for the sample named.

**Severity.** MAJOR. This is a newly added sentence whose entire function is a baseline comparison, in the subsection a referee will scrutinise hardest, and it is wrong in both the sample identifier and the amplitude convention. It is also self-contradicting against §2.2 two pages earlier, which is the kind of defect that costs a reader confidence in every other number. Fix is small (name the catalog-wide sample; quote $A_p=-0.53\%$), but it must be fixed.

---

### A2. "A third, near-antipodal axis" is quantitatively false, and the axis-instability evidence is selectively reported

**Location:** main.tex L1055–1059; PDF p.11 (§A.1, "Full-parent selection behavior").

**Claim:** "…removing only the `primary_hc` confidence cut does not ($z=+9.13$, **at a third, near-antipodal axis**); … **The axis is inconsistent across selections (shifting by $107.5^\circ$)**, … This pattern — signal present only in the population the primary QC cuts are designed to exclude, removed by a single confidence or footprint-leg cut, **with an unstable axis** — is consistent with a confidence-cut/footprint systematic…"

**What is wrong.** From the committed `full_parent/row16ib_axis_shift.json`, the four QC selections' best-fit axes are C0 (278.630°, +25.320°), C1 (168.540°, −73.225°), C2 (294.305°, +16.029°), C3 (195.482°, −57.162°). Recomputing every pairwise angular separation:

| pair | separation |
|---|---|
| C0–C1 | **119.9°** |
| C0–C2 | **17.3°** |
| C0–C3 | 107.5° (matches the JSON's own `axis_separations_deg.C0_vs_C3` = 107.509) |
| C1–C2 | 115.2° |
| **C1–C3** | **19.3°** |
| C2–C3 | 108.2° |

Three consequences:

- **Nothing is "near-antipodal."** The largest separation anywhere in the sweep is 119.9° (C0–C1); antipodal is 180°. Even treating these as unsigned axes (mod π) the largest is 72.5°. The descriptor overstates the instability by ~60°. (The wording is inherited from `ROW16IB_AXIS_SHIFT_2026-09-04.md`, which asserts "nearly antipodal" without computing it; the JSON in the same directory does not support it. The predecessor doc `ROW16I_FULL_PARENT_2026-09-04.md` compounds this with an impossible "295° arc separation".)
- **The omitted fact cuts the other way.** The C1 axis (the $z=+9.13$ selection the paper calls "a third" axis) sits **19.3° from the primary channel's own best-fit axis C3** — i.e. it is the *closest* axis in the sweep to the paper's headline channel, not a third independent direction. Likewise C0 and C2 agree to **17.3°**. The sweep therefore contains two tight axis pairs (C0≈C2, C1≈C3) separated by ~107–120°, which is a materially different — and more interesting — pattern than "three mutually inconsistent axes", and one a referee would want interpreted rather than flattened.
- The paper reports only the single largest pairwise number (107.5°) as *the* measure of inconsistency, while both ~17–19° agreements go unmentioned.

**Severity.** MAJOR. The axis-instability claim is load-bearing: it is one of the three legs on which the paragraph attributes the $z=+4.44$ full-parent dipole to systematics rather than signal. A referee cannot accept a systematics attribution resting on a descriptor that the paper's own committed artifact contradicts, nor on a selective read of the separations. The correct numbers still support "inconsistent across selections", so the fix does not change the verdict — but the statement as written does not survive checking.

---

### A3. The headline exclusion sections are never told about the manuscript's own pixel-level measurement

**Location:** §5 (`sec:bh`, PDF p.7–8), Assumption 2 at main.tex L832–838 (PDF p.8), §3 at L493–501 (PDF p.5), the Abstract (L92–98), §6 and §7 — versus §A.1 at L1004–1026 (PDF p.10).

**What is wrong.** §A.1 states, correctly and in the paper's own words, that the new pixel-level slope implies a response ratio ≈0.038, "roughly an order of magnitude smaller than $g=0.398$", that propagating it "would move the observed-label floor $A_{95}^{\rm obs}=0.98\%$ to a physical-amplitude floor of order … $26\%$", and that "this new direct measurement of the pipeline's own pixel-to-label transfer **is not consistent with that bridge value at face value**" and "Resolving this … is necessary before the Sec. 5 exclusion can be treated as more than illustrative."

That is a first-class qualification of the paper's headline claim. Yet `grep -n "robustness_disclosure" main.tex` returns exactly two hits: the `\label` itself (L983) and one pointer in Data Availability (L1236). **There is no forward reference to §A.1 from anywhere in §3, §5, §6, §7 or the Abstract.** Concretely:

- Assumption 2 (L832–838) still reads "…an illustrative bridge factor $g=0.398$ used there for a different comparison is explicitly not an established calibration and **is not used to strengthen this statement**." The only failure mode it contemplates is that $g$ might have *strengthened* the exclusion. It does not say that the manuscript now contains a direct measurement inconsistent with $g$ by an order of magnitude in the *weakening* direction.
- §3 L493–498 still says the physical bound "additionally requires a spatially resolved morphology transfer function, **which remains an open gate** in the archived release paper," with no note that §A.1 now reports a first direct empirical probe of that transfer.
- The Abstract discloses the $g=0.398$ weakening ("under an illustrative, not-adopted-for-strengthening bridge the two largest comparison samples drop below this floor") but not the much larger one implied by the pixel slope (4–5 of 5 rows).

**Severity.** MAJOR. This is not a missing-caveat complaint — the caveat exists, it is well written, and I credit the authors for writing it. The defect is **placement**: a reader of §1→§3→§5→§6→§7 (i.e. anyone who does not read the appendix) comes away with "floor ≈1%, 2–20× below the literature claims" and no signal that the paper's own appendix contains a measurement which, taken at face value, inverts that comparison. For an ApJS paper whose headline is an exclusion, the qualification must appear where the exclusion is stated. Minimum fix: one sentence in Assumption 2 and one in §3's observed-label paragraph, each pointing at §A.1, plus a clause in the Abstract and Conclusions.

---

### A4. §3's primary null never mentions that the primary channel itself fails leg-removal stability

**Location:** §3 (`sec:dipole`, PDF p.4–6), Abstract, §6, §7 — versus main.tex L1065–1073 (PDF p.11).

**What is wrong.** §A.1 discloses, honestly, that "The same per-leg partition applied instead to the primary $887{,}472$-galaxy channel (C3) is less clean: two drop-one-leg variants (dropping DECaLS, $z=+4.19$, $A=2.21\%$; dropping DES, $z=+4.26$, $A=1.39\%$) and the DES-only fit ($A=5.83\%$) exceed $A_{95}^{\rm obs}=0.98\%$… it indicates the primary channel's own footprint-stability nulls are not uniformly clean under leg removal, a residual not resolved by this disclosure."

Those are $z>4$ *formally significant* fits, on the paper's primary science channel, at amplitudes 1.4–2.2× above the paper's own headline sensitivity floor. Nothing in §3, the Abstract, §6, or §7 refers to this, and §3 contains no forward pointer to §A.1. §3's only stability discussion (L556–596) is the block-bootstrap covariance, which does not probe footprint sub-selection at all.

**Severity.** MAJOR, and in my judgement the most consequential structural issue in the manuscript alongside A3. The primary result — "$z_{\rm mom}=+0.635$, null-consistent, floor 0.98%" — is presented across four sections with no indication that removing a single imaging leg from the *same* sample produces $z\approx+4.2$. A referee will ask, reasonably, why the disclosure is in an appendix subsection titled "Robustness and disclosure" rather than in the section reporting the result it qualifies. It also needs interpretation the paper does not supply: are these drop-one-leg excursions consistent with the increased variance expected from a smaller support, or not? The paper reports $z$ against each variant's own matched null, so the excursion is not a naive variance artefact and deserves a sentence of analysis, not just disclosure.

---

### A5. The DESI DR1 BGS environment split is described as a tercile split; it is a 20/60/20 quintile-edge split

**Location:** main.tex L1137–1141 and Table 8 (`tab:bgs_environment`); PDF p.12 (§A.1, "External environment").

**Claim:** "Table~\ref{tab:bgs_environment} reports the **three-way density-tercile split** (labelled void-like/wall-filament/node-like by relative rank; **every tercile's** median $\delta_k$ is in fact overdense…)."

**What is wrong.** The committed analysis code bins on the 20th/80th percentiles, not terciles:

- `chirality_structure/row16ivb_bgs_environment.py` L66–68:
  ```python
  """Density contrast, then quintile bins -> 0 void-like, 1 wall, 2 node-like."""
  q = np.quantile(dl, [0.2, 0.8])
  ```
- and its module docstring (L7–8): *"Bins: void-like (lowest quintile), wall/filament (middle three), node-like (top quintile)."*
- The frozen pre-registration `ROW16IVB_BGS_ENVIRONMENT_2026-09-05.md` §0.2 is equally explicit: *"**void-like** = lowest quintile of δ_k; **wall/filament** = middle three quintiles; **node-like** = top quintile."*

The paper's own Table 8 proves it: 24,284 / 72,849 / 24,284 of 121,417 and 189,917 / 569,750 / 189,917 of 949,584 are exactly 20% / 60% / 20% in both subsets — not 33/33/33.

**Severity.** MAJOR. (a) The paper's text is contradicted by the paper's own table on the same page. (b) A reader attempting to reproduce the result from the description would bin at terciles and obtain different $N$, different $f_{\rm CW}$, and different $z$ in every cell. (c) It is the one methodological sentence in a paragraph whose purpose is disclosure of an external-tracer test. The conclusion (null) is unaffected — I verified every cell of Table 8 against `row16ivb_bgs_environment.json` and the transcription is exact — but the method statement is wrong and must be corrected to "lowest/top density quintile, middle three quintiles" in both places.

---

### A6. The 0.79-correlation parenthetical is not supported by the covariance matrix it cites

**Location:** main.tex L580–586; PDF p.6 (§3).

**Claim:** "The monopole is the only channel with $|z|>3$ against its own bootstrap scatter ($z=-6.57$; **the FSC harmonic diagnostic above is the same structure seen through a different estimator, consistent with its $0.79$ correlation to the real-space channel here**); the other three channels are all non-significant…"

**What is wrong.** The parenthetical is attached to, and syntactically qualifies, the *monopole* channel, and offers the 0.79 correlation as the evidence that the FSC harmonic residual and the monopole are the same structure. The cited matrix (`g3_joint_estimator_covariance_master_v2.json`, `joint_correlation_4x4`) says the opposite:

- monopole ↔ $C_1^{\rm master}$ = **−0.061**
- monopole ↔ real-space = **−0.037**
- The **0.794** figure is real-space ↔ $C_1^{\rm master}$, and has nothing to do with the monopole.

The paper itself says so eight lines later: "The monopole is **nearly uncorrelated with the other three**." So on the natural reading, the sentence cites a number that refutes it, and self-contradicts within the same paragraph.

On the alternative reading — that "the same structure" refers to the real-space channel rather than the monopole — the claim still does not hold: the FSC harmonic diagnostic of §3 is $z=+6.923$ (fixed-occupancy $\ell=1$ moment on the 24,087-pixel FSC support), whereas the $C_1^{\rm master}$ channel in this bootstrap is $z=-0.605$ on the 949,584-galaxy pre-support-cut HC sample. Different sample, different support, different null, opposite sign, and 7.5σ apart in significance; a 0.79 bootstrap correlation between the real-space and MASTER channels does not license identifying a $+6.9\sigma$ FSC statistic with a $-0.6\sigma$ HC statistic.

**Severity.** MAJOR. The FSC $\ell=1$ residual ($z=+6.923$, $p=0.002$) is the single formally significant harmonic result in the paper, and this parenthetical is one of the two in-text arguments for treating it as systematic structure rather than signal. Whichever reading is intended, the cited evidence does not support it, and the sentence is contradicted either by the matrix or by the paper's own next-but-one sentence. It needs to be rewritten to say precisely which two channels are correlated at 0.79 and precisely what that does and does not imply for the FSC diagnostic.

---

## PART B — MINOR findings

**B1. The executed-statistic count in the structure battery does not reconcile (L1078–1081, PDF p.11).**
"a pre-registered battery of **15 of 17** declared chirality×structure statistics was executed (**the Shamir-axis statistic** below was unavailable; the full ×17 Bonferroni correction is retained rather than loosened to ×15)". The pre-registration (`ROW16IV` §0.5) enumerates (a) 2 + (b) 9 + (c) 2 + (d) 4 = 17, and §2 reports (a) 2, (b) 9 (8 bins + NN), (c) 2, (d) 3 (CMB dipole, CMB quad/oct, free best-fit) = **16** executed. One statistic is named as unavailable; 17 − 1 = 16, not 15. The source doc carries the same off-by-one (§4.4). No result changes — the conservative ×17 threshold is retained either way — but the arithmetic in the manuscript does not close.

**B2. The full-parent channel's own recalibrated sensitivity floor is omitted (L1048–1064, PDF p.11).**
`row16i_full_parent_dipole.json` records `injection_recovery.A95_obs_pct = 0.5095` for the 3,200,420-galaxy parent, i.e. that channel's own injection-calibrated floor is **0.51%**, and the observed $A=0.566\%$ **exceeds it**. The source doc leads with exactly this ("formally significant … exceeds its own injection-calibrated $A_{95}^{\rm obs}=0.51\%$ sensitivity floor — a materially different outcome"). The paper reports $A$ and $z$ but not the exceedance, and not the fact that a channel 3.6× larger has a floor roughly half the paper's headline 0.98%. Given the manuscript's headline is a sensitivity floor, the existence of a (systematics-contaminated) 0.51% channel is information a referee expects to see stated, even if it is then set aside.

**B3. Two different null realisations of the same C0 fit are mixed in one sentence (L1052–1055).**
$z=+4.44$ is the ROW16I value (`row16i_full_parent_dipole.json`, `null.seed`=20260904, 10,000 draws). The $+0.68$ / $+9.13$ / $+0.48$ values in the same sentence chain come from `row16ib_axis_shift.json`, whose own C0 row gives $z=+4.3263$ (different seed). The "graded QC sweep" the paper describes is the ROW16IB sweep, whose internally consistent C0 value is **+4.33**. Either quote +4.33 for the sweep, or state that +4.44 is from a separate independently seeded run.

**B4. The C3 leg exceedances are incompletely enumerated (L1065–1069, PDF p.11).**
The paper names three C3 fits exceeding $A_{95}^{\rm obs}$. From `row16ib_axis_shift.json`, **five of the six** C3 leg fits do: only-BASS+MzLS 3.916% ($z=+2.00$), only-DECaLS 1.657% ($z=+2.20$), drop-DECaLS 2.211% ($z=+4.19$), only-DES 5.830% ($z=+2.49$), drop-DES 1.389% ($z=+4.26$); only drop-BASS+MzLS (0.658%) is below. The sentence reads as an enumeration and understates the extent of the instability it is disclosing.

**B5. "except Shamir (2025)" is inconsistent with the Table-5 convention (L1012–1014, PDF p.10).**
"…a physical-amplitude floor of order $0.98\%/0.038\approx26\%$, under which every literature amplitude in Table 5 **except Shamir (2025)** would fall below the floor". Table 5's caption declares "Ratio is the claim's **low-end** amplitude over $A_{95}^{\rm obs}$" (and the ratios confirm it: 20/0.98 = 20.4). Shamir 2025's low end is **20%**, which is below ~25.5–25.8%. Under the paper's own convention all five rows fall below; only Shamir 2025's *high* end (33%) exceeds. Either say "all five rows' low-end amplitudes would fall below" or say "only Shamir (2025)'s range straddles the floor".

**B6. Data Availability contradicts §4 on the T-Web diagnostic (L1217–1221 vs L646–672, PDF p.12 vs p.6).**
DA: "…the void/non-void secondary diagnostic paths (author VoidFinder, **T-Web**, Tempel, ASTRA) **are not reproduced in this condensed manuscript**". But §4 does reproduce the T-Web four-class diagnostic: Fig. 3 (`fig:voidbar`), 812,793 env-labelled rows, all four class $N$, and two bar values quoted in the caption. §4's own sentence is correct ("author-constructed VoidFinder and the Tempel and ASTRA web classifications are retained as further secondary diagnostics in the archived companion study") — DA should drop "T-Web" from that list.

**B7. The 0.1<z<0.4 window is attached to the wrong sample (L1142–1144, PDF p.12).**
"…the 121,417-spiral DESI spectroscopic-redshift subset (three-dimensional comoving density, **cut from a $0.1<z<0.4$ tracer-matched 231,549-spiral parent**)". `ROW16IVB` §4.2 records the opposite dependency: the P5 parent is $0<z<0.6$ with 231,549 spirals, and the $0.1<z<0.4$ restriction (forced by the BGS tracer volume) is what reduces it to 121,417. As written, the window is ascribed to the 231,549-row parent, which never had it.

**B8. The "67–72%" CE-composition range is misattributed (L353–355, PDF p.3).**
"…the historical CE-ResNet-derived $17{,}153$-row component (${\sim}67$–$72\%$ of the historical training composition, **by either committed count**)". The archived release says both committed accounts give the *same* figure: "one reconstruction gives 26,616 rows and 826 CE-ResNet-selected non-spirals (**67.5% CE-derived**), whereas the committed benchmark report gives 26,626 and 846" and "**Both pool accounts are approximately 67.5% CE-derived**" (v1.0.274 L1010, L1054). The 72% figure is a different quantity from a different denominator — "the CE-only pool — **72% of the spiral labels**" (L1056), i.e. 17,153/23,790 = 72.1%. Recomputing: (17,153+826)/26,616 = 67.55% and (17,153+846)/26,626 = 67.60%. So the two committed counts do **not** bracket 67–72%; they agree to 0.05 pp.

**B9. Table 4's "quoted verbatim" claim drops the source's scope markers (L358–360, PDF p.4).**
The caption says the bias-hardening results are "quoted verbatim". The source table (`chirality_catalog_paper.tex` L1796–1802) labels three of the seven rows "T2: Rotation stability **(historical)**", "T4: Perturbation robustness **(historical)**", "T6: Hemispheric difference **(historical)**". P4′ drops all three qualifiers while asserting verbatim quotation. Either restore "(historical)" or soften the caption.

**B10. The training-composition conflict is presented as unresolved when the cited source says it has been adjudicated (L330–344, PDF p.3).**
The paper: "no retained object-ID manifest or random-state record **resolves the conflict**…" and "the released classifier's own training provenance **cannot be independently audited beyond the confusion matrix above**". The archived release it cites reports a subsequent CE-ResNet re-provisioning from the Zenodo deposit whose seeded assembly "reproduces the two large historical components **exactly** — 6,637 GZ1 confident CW/CCW and 17,153 CE-ResNet spirals — and yields **819** CE non-spirals … the entire 826-vs-846 / 26,616-vs-26,626 conflict is now **isolated** to the seeded 50,000-object non-spiral subsample crossmatch … **the conflict is now adjudicated (isolated) rather than left open**" (v1.0.274 L1056, L1741). P4′'s framing is strictly more pessimistic than its own source supports, and the "cannot be independently audited" clause is overstated given that two of the three components now regenerate exactly. Separately: the paper quotes "26,626 total rows and 846 CE non-spirals" without noting that this pair is itself arithmetically inconsistent with the stated components (6,637+17,153+846+2,000 = 26,**636**), a discrepancy the archived release attributes to the non-spiral subsample boundary.

**B11. The spec-z ⊂ projected nesting is asserted but not evidenced (L1145–1149, PDF p.12).**
"…this projected subset is not disjoint from the spec-z subset — the 121,417 spec-z rows are a **nested subset** of the 949,584…". The two arms are built from different files by `row16ivb_bgs_environment.py`: the spec-z arm from `p5_matched_chirality_desi.parquet` under `matched_primary_deduped & class_eq∈{CW,CCW} & zwarn==0 & 0.1<z<0.4 & match_confidence_eq>0.6` (L167–175), the projected arm from the release parquet under `primary_hc` + CW/CCW label. The cuts are compatible (both are $p_{\rm eq}>0.6$ spirals), so the claim is plausible, but no intersection count is recorded in the JSON, the source doc, or the manifest. For a statement used to caveat the independence of two reported subsets, an actual cardinality check should be committed.

---

## PART C — NITS

**C1.** main.tex L396: `\CW/\CCW label totals` — `\CCW` gobbles the following space, so the PDF (p.4, line 235) reads "**CW/CCWlabel** totals". Add `{}` or `\ `. This is the only space-gobbling site I found; every other macro use is safe.

**C2.** main.tex L406–407: "The distinct \FSC{} harmonic diagnostic (Sec.~\ref{sec:dipole}, **above**)" appears in §2.3, which *precedes* §3. Should be "below". (§3's reciprocal reference at L503–504 is correct.)

**C3.** main.tex L1066: "the primary $887{,}472$-galaxy channel **(C3)**" — `C3` is an internal selection code from `ROW16IB_AXIS_SHIFT_2026-09-04.md` and is never defined in the manuscript. Either define the C0–C3 ladder or drop the label.

**C4.** Manifest metadata inconsistency: `reproducibility/manifests/experiments/row16iv-chirality-structure.json` and `row16ivb-bgs-environment.json` carry `"paper": "P4"`, while `p4p-row16i-full-parent-dipole.json` and `p4p-row16ib-axis-shift.json` carry `"paper": "P4P"`. The Data Availability section lists all four as this (P4′) manuscript's manifests. All four files exist and are git-tracked; only the `paper` field disagrees.

**C5.** One Overfull \hbox, 5.88 pt, main.log:757, from the Table 4 caption (L371–385). Rendered page 4 shows no visible intrusion into the gutter; cosmetic only.

**C6.** Two "LaTeX Warning: A float is stuck (cannot be placed) on input line 703" in main.log. The `deluxetable` (Table 5) does place correctly on p.8 in the final PDF, but the warning is worth clearing before submission since float placement can shift on the arXiv/journal toolchain.

**C7.** `Poplawski:2020` is cited in text as "Poplawski~(2020)" throughout §1 and §5 while the bibitem correctly records arXiv:1910.10819 as posted **October 2019** with no journal publication. The bibitem's self-disclosure is exactly right; consider also flagging the year at first in-text use, since a reader checking the citation will hit the mismatch before reaching the bibliography.

---

## Assessment

The quantitative spine of this manuscript is solid. I attempted to break roughly fifty transcribed numbers against their committed artifacts and the two archived source papers, and re-derived the arithmetic wherever it was checkable — the primary dipole ($z_{\rm mom}$, rank $p$, null mean and 95th percentile recomputed directly from the 10,000-draw null array), the Neyman inversion bracket, the full 4×4 correlation matrix, both Cohen's κ values, the confusion-matrix marginals, the Fisher floor, every DESIVAST and BGS cell, every literature ratio. All of it reproduces. The four disclosure results added in this subsection are, individually, honest reporting of results that *weaken* the paper's own position, which is to the authors' credit and is rarer than it should be.

The problems are of two kinds. First, five localised factual/consistency errors in the newly added disclosure text (A1, A2, A5, plus B1–B5, B7, B8) — wrong sample label, wrong amplitude convention, an axis descriptor contradicted by the committed JSON, a quintile split called a tercile split, and several transcription slips from the source docs. These are individually small and collectively fixable in an afternoon, but their density in the *new* material, versus their near-absence in the older material, suggests the disclosure subsection did not get the same verification pass the rest of the paper did.

Second, and more seriously, a structural problem (A3, A4): §A.1 contains two results that materially qualify the paper's headline — a pixel-to-label transfer measurement inconsistent with the bridge factor by an order of magnitude, and a demonstration that the primary channel's own drop-one-leg fits reach $z\approx+4.2$ above the sensitivity floor — and **neither is referenced from §3, §5, §6, §7 or the Abstract**. The caveats are present and well written; they are simply in the wrong place. A paper whose central claim is an exclusion cannot put the strongest challenge to that exclusion in an appendix with no forward pointer. Fixing this requires editorial restructuring, not just a correction, which is what moves my verdict past "minor".

I want to be explicit about what I am *not* finding: I found no fabricated number, no unsupported strengthening of a claim, no dismissed limitation, and no place where the paper reports the more favourable of two available values. Where the manuscript had an opportunity to overstate — the FSC $\ell=1$ residual, the full-parent $z=+4.44$, the $g$-bridge, the exploratory status of the void basis, the $A_{95}^{\rm CL}$ vs $A_{95}^{\rm obs}$ choice — it consistently took the conservative option and said so. A6 is the one case where I believe an argument for the conservative reading is made with evidence that does not support it, and even there the conclusion is probably right for other reasons.

---

## Verdict

**major-revisions**
