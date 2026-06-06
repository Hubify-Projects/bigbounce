# P5 auto-2026-06-05_1717pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 312.7s

---

META-REVIEW (focus: blind spots none of the 5 prior referees caught)

P5-META-E1
- Severity: ESSENTIAL
- Section/page: IV.A steps 1–7 (pp. 3–4), plus Fig. 1
- Why missed by others: Reviewers noted “survey-shell” edge effects but did not recognize the deeper selection-function error driving the 3D density field itself.
- Problem (quote/context): “We compute environment labels via the V‑Web tidal‑tensor classifier… (1) filter DR1 to ZWARN==0, SPECTYPE∈{GALAXY,QSO}… (4) Cloud-in-Cell deposit… (5) build a survey-footprint mask… ρ̄cell=4.64 galaxies/cell. (6) Convert counts to overdensity δ=ρ/ρ̄−1. (7) Gaussian-smooth δ…”
  The 3D overdensity is formed from a highly heterogeneous, redshift‑dependent tracer mix (BGS/LRG/ELG/QSO) without any correction for the radial selection function n(z), completeness, or per‑tracer weighting, and with ρ̄ taken as a single global scalar over the in‑mask volume. This guarantees a strong, spurious radial gradient in δ and hence in the tidal tensor, independent of true LSS. It is not sufficient to then argue “edge artifacts inflate the void class”; the field itself is selection‑dominated.
- Required fix: Rebuild the density field with a proper selection-function correction, e.g. divide counts by an expected density field from a random catalog (per‑tracer, per‑z; FKP‑style weights) before forming δ, or restrict the classifier to a volume‑limited BGS sample with uniform n(z). Demonstrate (via numbers/tables) that class fractions and per-class fCW are stable after this correction.

P5-META-M1
- Severity: MAJOR
- Section/page: IV.A step 8 (p. 4)
- Why missed by others: Edge/systematics were mentioned, but not the boundary condition mismatch of the Poisson solve itself.
- Problem (quote/context): “Solve Poisson in k-space: Φ(k)=−δk/k^2 (with k=0 mode zeroed).” The FFT Poisson solver assumes periodic boundaries, but the input cube is a thin, irregularly masked survey shell (18.8% of the cube “in‑mask”), with zeros outside the dilated mask. This choice imposes unphysical periodic boundary conditions and injects large, mask‑correlated long modes into Φ and hence Tij, even away from edges.
- Required fix: Either (a) inpaint the masked volume and solve with an appropriate boundary treatment (e.g., constrained realization/Wiener filtering), (b) solve Poisson on the masked domain with suitable Dirichlet/Neumann conditions, or (c) demonstrate using mocks that the periodic-FFT approximation does not bias the resulting class assignment at the reported precision. Provide a quantitative before/after comparison of class fractions and fCW residuals.

P5-META-M2
- Severity: MAJOR
- Section/page: IV.A steps 4 and 7 (p. 4)
- Why missed by others: The grid/smoothing choice looked innocuous; no one checked resolution adequacy.
- Problem (quote/context): “Ngrid=256^3 … cell 25.9 Mpc/h,” “Gaussian-smooth … Rs=25 Mpc/h.” The Gaussian smoothing scale is effectively one grid cell (σ ≈ one voxel). A T/V‑Web classifier typically requires the smoothing kernel to be resolved by multiple cells to avoid aliasing and stair‑stepped eigenvalue fields. Under‑resolved smoothing makes class boundaries highly sensitive to grid phase.
- Required fix: Increase resolution (e.g., 512^3) or choose Rs ≥ 2–3 grid cells; re‑run one robustness cell to show that class fractions and per‑class fCW are stable at the ≤0.1–0.2 pp level under a factor‑2 grid refinement and/or larger Rs.

P5-META-M3
- Severity: MAJOR
- Section/page: IV.A step 12; VI.D (within-class density quartiles) (pp. 4, 6)
- Why missed by others: Interpolation method is rarely examined; here it directly affects per‑galaxy labels.
- Problem (quote/context): “NN‑interpolate the per‑cell label + smoothed logdensity to each galaxy.” Nearest‑neighbour mapping of a categorical field defined on a coarse grid introduces discretization noise and boundary locking (galaxies near cell boundaries inherit step‑function class changes). Using this field to form within‑class density quartiles compounds the issue.
- Required fix: Replace NN with trilinear interpolation of continuous fields (e.g., eigenvalues or density), then re‑assign classes from the interpolated eigenvalues at galaxy locations; or perform class assignment directly on a higher‑resolution grid (or by majority within a local kernel). Quantify the impact on per‑class counts and fCW.

P5-META-M4
- Severity: MAJOR
- Section/page: VI.B (p. 6)
- Why missed by others: The logistic model form was not scrutinized.
- Problem (quote): “A logistic regression of the CW indicator on {z, |sin δ|, cos α, confidence}…” This basis cannot represent a general large‑scale angular pattern: including only cos α (no sin α) fixes the RA phase at 0; using |sin δ| (no cos δ) removes sign sensitivity in declination. The model cannot detect an arbitrary dipole/quadrupole on the sphere and is therefore an under‑powered diagnostic for sky‑dependent residuals.
- Required fix: Use a properly specified angular basis (e.g., spherical harmonics up to ℓ=1 or 2: {Y10, Y11c, Y11s} or equivalently {sin δ, cos δ cos α, cos δ sin α}) alongside z and confidence. Report coefficients with standard errors and a global LRT/WAIC/AIC comparison to the null model.

P5-META-M5
- Severity: MAJOR
- Section/page: VIII.F, Fig. 6 and accompanying text (pp. 12–14)
- Why missed by others: The pixel‑level correlation was accepted at face value without examining heteroskedasticity.
- Problem (quote/context): “Per‑pixel Pearson correlation … across n=727 valid pixels is r=+0.006 (p=0.88).” The dependent variable is a per‑pixel σ-from‑half, whose uncertainty varies strongly with the number of spirals per pixel (≥200 cut is not sufficient to homogenize errors). An unweighted Pearson treats all pixels as equally precise, biasing r toward zero under heteroskedastic noise.
- Required fix: Recompute the correlation using (a) inverse‑variance weights for each pixel’s σ estimate, or (b) a meta‑analytic GLS with pixel‑level variances, or (c) a regression of the raw CW fraction with binomial weights against maximal‑void count. Report whether conclusions change.

P5-META-M6
- Severity: MAJOR
- Section/page: VIII.B (“point‑in‑sphere test against 101,863 DESIVAST VoidFinder hole spheres”) (p. 11)
- Why missed by others: Reviewers focused on sample size; not on the membership operator itself.
- Problem (quote/context): “point‑in‑sphere test against 101,863 DESIVAST VoidFinder hole spheres” to define “DESIVAST void galaxies.” VoidFinder’s “holes” overlap and are surrogate spheres composing a larger maximal‑void; naïvely classifying a galaxy as “void” if it falls in any hole can mislabel wall filaments near void boundaries (overlap/union artifacts). DESIVAST also publishes catalog‑native GALZONE/ZONEVOID memberships that encode watershed topology more faithfully.
- Required fix: Use the catalog‑native GALZONE/ZONEVOID membership as the primary void definition (you do report it as a cross‑check later), and move the sphere‑union test to a secondary consistency check; explicitly quantify the difference between hole‑union vs catalog‑native labels in terms of per‑galaxy confusion and ΔfCW.

P5-META-m1
- Severity: MINOR
- Section/page: V.A (nulls), VI.E (HEALPix), VII (Phase‑2) (pp. 4, 8–10)
- Why missed by others: They checked σ thresholds but not null comparability within a single figure/panel.
- Problem (pattern): Several places juxtapose σfrom‑half (binomial) with permutation‑null max‑σ and with σpred (monopole) in the same panel or paragraph, but the figures/tables do not flag which σ belongs to which null, nor indicate that sampling distributions (and units, “pp” vs fraction) differ. This risks casual miscomparison across unequal nulls even within a single analysis block.
- Required fix: In every table/figure that reports more than one type of σ or mixes “pp” with fractions, add a legend row explicitly mapping symbols to nulls and units; add a short sentence “σ statistics in this panel are not directly comparable across nulls.”

P5-META-m2
- Severity: MINOR
- Section/page: VI.D/Table IV (p. 6)
- Why missed by others: Values appear plausible; no one asked how “density” was defined.
- Problem (quote/context): Table IV bins “cluster” and “filament” by “V‑Web per‑galaxy density,” but the paper never defines this quantity precisely (is it 1+δ, log(1+δ), or the smoothed δ rescaled; is it measured at the galaxy via interpolation or cell mean?). Without a definition, the quartile labels and their physical interpretation are ambiguous.
- Required fix: Define the per‑galaxy density field explicitly (mathematical form, interpolation, smoothing), and state whether quartiles are formed globally or within class, and on which scalar (δ vs log‑density). Provide units or a normalization convention.

P5-META-m3
- Severity: MINOR
- Section/page: VIII.F (p. 12)
- Why missed by others: Focus was on the monopole value itself.
- Problem (quote): “the observed −5.00σ corresponds to ΔfP5CW ≈ −0.0028, ∼8% larger than the P4 catalog‑mean. This residual 8% enhancement is consistent with the spectroscopically‑confirmed subsample being more strongly weighted to the BGS‑bright leg…” This interprets the 8% as selection weighting without actually showing the bright/dark composition of the 791,635‑object set versus Paper IV’s full catalog. The causal statement is unsubstantiated as written.
- Required fix: Provide a short decomposition of the matched sample by tracer program versus Paper IV’s global mix, and show that the expected Δf from per‑leg offsets predicts the observed −0.0028 within uncertainties.

P5-META-N1
- Severity: NIT
- Section/page: IV.A step 5 (p. 4)
- Why missed by others: Considered harmless implementation detail.
- Problem (quote): “build a survey‑footprint mask by dilation of occupied cells: 2,417,697 occupied → 3,150,086 in‑mask.” The choice of dilation kernel/iterations is unstated and can materially change the effective mask and the class volume fractions in Fig. 1.
- Required fix: Specify the morphological dilation parameters and demonstrate that varying the dilation by ±1 iteration changes in‑footprint volume fractions and downstream class counts by <0.5 pp (or justify the chosen dilation via a footprint reference).

Meta-review recommendation
MAJOR REVISIONS

Across the six reviews, the manuscript’s biggest blockers are: dependence on an unpublished input catalog; incorrect or unclear statistical thresholds and equations; ambiguous sample definitions; and data/code availability. This meta‑review adds several methodological issues in the construction of the 3D tidal field (selection‑function correction, boundary conditions, grid/smoothing resolution, and interpolation), plus under‑specified regression and pixel‑level correlation choices. My assessment is that, if the authors (1) correct the selection‑function and boundary‑condition handling in the tidal‑tensor pipeline or explicitly downgrade V‑/T‑Web results to purely secondary diagnostics, (2) fully document the sample flows and statistical procedures, and (3) make the code/data public with DOIs, the paper can survive external peer review. Blocker count (union of all reviews): ~10–12 essential/major items. Confidence it can be brought to PRD standards after revision: moderate (60–70%), contingent on addressing the density‑field construction issues rather than just softening language.