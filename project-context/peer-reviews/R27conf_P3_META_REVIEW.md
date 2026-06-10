# P3 R27conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 396.1s

---

Meta‑review (focus: blind spots missed by all 5 prior referees)

P3‑META‑E1
- Severity: ESSENTIAL
- Section + page: II.D Step 5 (p.5) and III.F (Planck CMB; p.8–9), Table I (p.9)
- Why others missed it: Reviewers flagged Planck “top‑1%” vs fixed‑200 inconsistencies, but not the mismatch between the injection‑recovery gate and the published selection threshold.
- Problem (quote + analysis):
  - Gate definition: “Injection‑and‑recovery… recovery above the 99th‑percentile clean‑MSE threshold.” (p.5)
  - Published Planck tier: “Top‑200 native anomaly patches… the Path‑C native pipeline extracts… 2×10^5 patches… with the Planck tier held at the same canonical count of 200 (the top‑ranked patches of the native re‑score).” (p.9)
  - This means the detector is validated at the 99th percentile, while the catalog is selected at the 99.9th percentile (top‑200 of 200k). A 100% recovery at the 99th percentile does not guarantee adequate efficiency at the much harsher 99.9th‑percentile catalog cut.
- Required fix:
  - Re‑run the Planck injection–recovery at thresholds matching the published selection (≥99.9th percentile). Report the recovery fraction at 5σ under the 99.9th‑percentile gate (and at neighboring percentiles), or else lower the catalog selection to match the validated 99th‑percentile threshold. Make this alignment explicit in §II.D and §III.F.

P3‑META‑M1
- Severity: MAJOR
- Section + page: II.D Step 1 (p.4)
- Why others missed it: Reviewers criticized presentation and consistency, but not the scale‑invariance of the Step‑1 validation‑loss gate.
- Problem (quote + analysis):
  - “Retained if (a) validation loss ≤ 0.30 after ≤ 100 epochs, or (b) injection‑recovery ≥ 50% at 5σ.” (p.4)
  - The gate uses an absolute MSE cutoff (0.30) across heterogeneous inputs (496‑dim spectra vs 4096‑dim CMB patches vs 15–47‑dim tabular features) and different per‑survey standardizations. A fixed 0.30 is not comparable across surveys and risks misclassifying an otherwise well‑trained model (e.g., Planck val‑loss 0.4437 “fails” only because its per‑patch standardization and dimensionality set a different MSE scale).
- Required fix:
  - Replace the hard 0.30 threshold with a scale‑free criterion (e.g., improvement over an identity/mean‑reconstruction baseline; or a percentile of the clean‑MSE distribution; or an R^2/normalized MSE). Re‑evaluate which surveys PASS/FAIL under a scale‑free gate and update any text that relies on the old binary outcome.

P3‑META‑M2
- Severity: MAJOR
- Section + page: II.B.a Tabular‑survey preprocessing (p.3)
- Why others missed it: Prior reviews focused on data leakage and eROSITA score axis, not on missing‑value handling.
- Problem (quote + analysis):
  - eROSITA: “NaN/Inf entries are set to 0; the 33 rate/flux/count columns receive a signed log(1+|x|) transform; each column is then standardized…” (p.3)
  - NEOWISE/Gaia follow the same family recipe (NaN→0, clipping). Setting missing astrophysical measurements to zero before a log transform and standardization conflates “missing” with a physically meaningful value (0 → log(1)=0 → near the column mean after standardization). This can suppress anomaly sensitivity for precisely those sources with informative missingness patterns and may induce biases in the anomaly ranking.
- Required fix:
  - Reprocess with a principled missing‑data treatment: impute with median (pre‑transform) and include explicit missingness indicator features per column, or use algorithms that handle NaN natively. Quantify the impact on rankings (Spearman/Jaccard vs the published lists); if negligible, state it; if material, update the affected catalogs and all downstream uses.

P3‑META‑M3
- Severity: MAJOR
- Section + page: II.B (per‑arm residuals) (p.3); III.A (DESI arm dominance, p.5); Table VI (p.21)
- Why others missed it: Others mentioned “B‑dominant contamination” qualitatively but not the methodological root cause.
- Problem (quote + analysis):
  - “For spectroscopic surveys, we additionally decompose the score into per‑band contributions rB, rR, rZ: the mean absolute residual… The per‑arm sub‑scores are computed on the common normalized input scale and are not independently z‑scored per arm… used only for within‑object arm‑dominance comparisons.” (p.3)
  - The paper nevertheless reports global arm‑dominance fractions (e.g., B‑dominant 22.7% in Table VI; p.21) and uses them diagnostically. Because rB,rR,rZ are not variance‑normalized per arm, any arm with higher residual variance or different calibration noise will spuriously win “dominance,” biasing the B‑dominant fraction upward independently of astrophysics.
- Required fix:
  - Redefine arm dominance using variance‑normalized sub‑scores (e.g., z‑scores per arm) or SNR‑weighted residuals, and re‑tabulate Table VI. Provide a sensitivity analysis showing how the B‑dominant fraction changes under normalization. If you retain the current definition, explicitly warn that the dominance counts mix astrophysics with arm‑noise systematics and should not be over‑interpreted.

P3‑META‑M4
- Severity: MAJOR
- Section + page: V (p.15–16), Appendix C (p.21–22)
- Why others missed it: Reviewers caught the F0 dimensional slip and inconsistent α→σ mappings, but not the 2D/3D scale inconsistency.
- Problem (quote + analysis):
  - The α estimate is derived from an angular two‑point Landy–Szalay measurement over θ ∈ [0.04°, 0.25°] with no 3D distances; yet the text translates the systematics statement into “O(H^2/k^2) … at kmax=0.2 h Mpc−1 (plane‑parallel monopole)” (p.16). kmax refers to a 3D Fourier cutoff that is undefined for a purely angular analysis without a radial selection. The GR‑projection bound framed at kmax=0.2 h/Mpc is therefore not anchored to the actual measurement domain (θ‑space).
- Required fix:
  - Either (a) convert the angular analysis to an effective k‑range using a stated redshift distribution and Limber/spherical‑Bessel mapping and then justify the kmax choice, or (b) restate the systematics bound purely in angular terms (e.g., multipole ℓ‑space) consistent with the measurement. Remove kmax‑based claims unless they are tied to a defensible 3D mapping for your α estimate.

P3‑META‑m1
- Severity: MINOR
- Section + page: III.F (Planck injection spec) and Table V footnote (p.21)
- Why others missed it: They focused on rate/threshold issues, not injection morphology post‑standardization.
- Problem (quote + analysis):
  - Injection convention: “per‑patch standardization (patch mean subtracted… divided by patch std)… the 5σ Gaussian‑bump injection… is added to already‑standardized validation patches and the patch is not re‑standardized after planting.” (p.21)
  - With mean removal and per‑patch variance scaling, a large fraction of real low‑ℓ structure is suppressed ab initio. The injected signal (σ=8 px ≈1.25° bump) is a fairly narrow, local feature in this standardized space and may not be representative of the diffuse/low‑ℓ anomalies the CAE would flag in practice. The 100% recovery thus over‑represents sensitivity to one morphology while under‑stating performance for others.
- Required fix:
  - Complement the bump test with at least one broad‑scale injection (e.g., low‑ℓ gradient/quadruple component or matched‑filter texture) applied before standardization (and then re‑standardized as in inference). Report recovery vs threshold for these morphologies so the gate reflects the range of plausible CMB anomaly shapes under your preprocessing.

P3‑META‑m2
- Severity: MINOR
- Section + page: IV.A (p.11–12)
- Why others missed it: They checked arithmetic/CIs but not multiplicity in cross‑matches.
- Problem (analysis):
  - The 17.8% “genuine novelty” fraction is computed after matching to 20 catalogs, but the paper does not quantify the aggregate chance‑coincidence rate across all 20 layers. Treating 822/1000 as “identified” without a multiplicity‑adjusted false‑match estimate (especially in crowded extragalactic fields) can bias the unmatched fraction downward.
- Required fix:
  - Provide an estimate of the expected number of spurious matches under the 20‑catalog composite (e.g., via local‑density Monte Carlo per object) and report a bias‑corrected novelty fraction (or at minimum, an uncertainty band that reflects plausible over‑matching). State explicitly that the 17.8% is uncorrected for multi‑catalog chance alignments if no correction is applied.

P3‑META‑m3
- Severity: MINOR
- Section + page: III.C (p.6–7) and Fig. 3 caption
- Why others missed it: They noted extreme S values but not the implicit unit ambiguity from using Eq. (2) z‑scores across distributions with heavy tails.
- Problem (analysis):
  - Presenting SDSS cross‑transfer scores as “S” (Eq. 2 z‑units) up to 10^11 implies Gaussian‑like calibration when, in fact, the DESI‑trained residual distribution on SDSS is heavy‑tailed/OOD and S ceases to be interpretable as a “z‑score.” This can be misleading even if qualified as a cross‑transfer artifact.
- Required fix:
  - Add one sentence in Fig. 3 caption or §III.C stating explicitly that “S” ceases to have its usual “z” interpretation under severe domain shift; for SDSS cross‑transfer we use S only as a monotone ranking proxy and interpret magnitudes on a log‑MSE axis (provide the corresponding MSE range for context).

P3‑META‑N1
- Severity: NIT
- Section + page: Table III (p.10)
- Why others missed it: Focused on axis reproducibility.
- Problem:
  - The “Dec” column is reported but not RA for eROSITA top‑5; while the IAU name encodes RA, the asymmetry is awkward for readers wanting both coordinates without decoding. Minor presentation issue.
- Required fix:
  - Add an RA column (or give α, δ explicitly) so the table is self‑contained.

## Meta‑review recommendation
MAJOR REVISIONS

Rationale: In addition to the substantive issues raised by the five referees (dimensional error in the Fisher summary, irreproducible eROSITA axis, tabular data leakage, Planck “top‑1%” labeling, inconsistent α→σ mappings, etc.), there are further methodological problems that directly touch validity and reproducibility: (i) the Planck injection–selection threshold mismatch, (ii) a scale‑dependent Step‑1 validation‑loss gate used across heterogeneous surveys, (iii) missing‑data handling that conflates “missing” with “zero,” and (iv) arm‑dominance claims based on un‑normalized sub‑scores. These require non‑trivial analysis changes or additional validation.

Given the union of all six reviews, I count 6–8 ESSENTIAL/MAJOR blockers that must be addressed (Fisher mapping correction and re‑validation; eROSITA score axis overhaul; removal of internal versioning; Planck selection/gate alignment; tabular leakage and missingness; heterogeneous thresholds and Planck table clarity; cosmology α/k‑space consistency). My confidence the paper would survive external peer review after a thorough, disciplined revision is moderate: the core catalog appears valuable and many problems are repairable, but substantial re‑analysis and editorial tightening are needed to meet PRD standards.