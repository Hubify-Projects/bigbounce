# P5 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v3_P5_v0_1_31
**Wall time**: 32.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=28414, completion=2506, reasoning=1743, total=30920

---

## PAPER-GEM-M1
**ID:** PAPER-GEM-M1
**Class:** MAJOR
**Section:** XII (Limitations)
**Issue:** The paper dismisses redshift-space distortion (RSD) effects on the V-Web classification by comparing the scalar displacement ($\sim 5-8$ Mpc/$h$) to the isotropic smoothing scale ($R_s = 25$ Mpc/$h$). This ignores the fundamental anisotropic nature of RSD (Kaiser effect), which systematically squashes the density field along the line of sight, directly biasing the tidal tensor eigenvalues and artificially promoting wall/filament misclassifications regardless of the isotropic smoothing scale.
**Fix:** Explicitly acknowledge the anisotropic bias of RSD on tidal tensor eigenvalues (not just scalar displacement length) and its specific effect on V-Web class boundaries.

## PAPER-GEM-M2
**ID:** PAPER-GEM-M2
**Class:** MAJOR
**Section:** XI.B (Bounce vs. inflation discrimination)
**Issue:** The paper claims to set an "observational upper bound" on environment-dependent parity signatures but provides zero equations linking the observable ($\Delta f_{CW}$ by environment) to a physical Lagrangian or EFT parameter (e.g., an axion-like particle gradient $\nabla_i \phi$ coupling to matter density). Without mapping the environmental density $\delta$ to a theoretical parity-violating operator, the bound is physically empty and cannot be used by model-builders.
**Fix:** Introduce a standard EFT coupling (e.g., Chern-Simons or ALP-matter density coupling) to physically parameterize what an "environment-dependent parity signature" means in terms of a Lagrangian operator.

## PAPER-GEM-M3
**ID:** PAPER-GEM-M3
**Class:** MAJOR
**Section:** I (Introduction) & XI.B
**Issue:** The paper discusses primordial parity-violating physics and chirality but fails to cite any standard theoretical reviews or foundational literature on cosmological parity violation, Chern-Simons gravity, or chiral gravitational waves (e.g., Alexander & Yunes 2009; Lue, Wang, Kamionkowski 1999). It relies exclusively on self-citations to unpublished companion papers (Golden 2026) for theoretical motivation.
**Fix:** Add citations to foundational cosmological parity-violation and Chern-Simons literature to ground the theoretical motivation in the established field.

## PAPER-GEM-min1
**ID:** PAPER-GEM-min1
**Class:** minor
**Section:** I (Introduction)
**Issue:** The claim "The test is bounce-model agnostic" overstates UV-completion independence. A density-based V-Web test is completely blind to models where parity-violation couples to vector/tensor modes (e.g., vorticity) rather than scalar overdensity.
**Fix:** Change "bounce-model agnostic" to "agnostic to models where parity-violation scales with scalar overdensity."

## PAPER-GEM-min2
**ID:** PAPER-GEM-min2
**Class:** minor
**Section:** VII.A (DESIVAST per-galaxy cross-match)
**Issue:** The point-in-sphere test uses comoving Cartesian coordinates derived directly from observed redshift. Voids defined in redshift space (observed frame) differ systematically from real-space voids (physical frame) due to the outflow velocity field, which expands the apparent void radius along the line of sight.
**Fix:** Note that redshift-space void radii are systematically larger than physical radii, which marginally affects the exact boundary classifications in the point-in-sphere test.
