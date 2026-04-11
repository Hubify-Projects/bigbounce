# Next-Gen Research Queue — Real Science on Real Data

**Created: 2026-04-11**
**Principle: Every experiment must use REAL data, train NEW models, and answer a SCIENTIFIC QUESTION that hasn't been answered before.**
**No synthetic reruns. No script validation loops. Every GPU hour must produce publishable insight.**

---

## TIER 1: MASSIVE SCALE, HIGHEST IMPACT (deploy first)

### 1. Galaxy Morphology Foundation Model (Paper 4 extension)
**Question:** Can we build the best galaxy morphology classifier in the world and open-source it?
**Data:** Full Galaxy Zoo DESI (8.7M galaxies with vote fractions) + Smith42/galaxies (8.47M images, already on HuggingFace)
**Scale:** 8.47M images × 3 bands = ~1 TB inference data
**Model:** Fine-tune DINOv2-Large or SigLIP on GZ-DESI labels → 4-head output (spiral/elliptical/merger/irregular + CW/CCW chirality + bar detection + ring detection)
**Novel science:** First foundation model that simultaneously classifies morphology AND chirality with equivariance. Would supersede our current ViT-Small (93.7%) with a ~97%+ model.
**GPU time:** ~24-48h on H200
**Output:** Best-in-class model + full catalog + confusion matrix + training curves (the Paper 4 finishing touches Houston needs)
**Why it matters:** This becomes THE reference model for galaxy morphology. Anyone studying galaxy evolution, mergers, bars, or parity violation uses our model.

### 2. DESI DR1 Full Spectral Re-Analysis with Transformer
**Question:** Does a Transformer autoencoder find different anomalies than BigAE?
**Data:** Full DESI DR1 spectra (22.5M, already processed once by BigAE). Download via DESI public API.
**Scale:** 22.5M spectra × 7,958 pixels = ~360 GB
**Model:** Vision Transformer adapted for 1D spectra (ViT-1D). Patch size=50, d_model=512, 12 layers, ~50M params. Train on 1M spectra, infer on full 22.5M.
**Novel science:** Cross-architecture anomaly validation. Objects flagged by BOTH BigAE and Transformer are highest-confidence true anomalies. Objects flagged by only one reveal architecture-dependent blind spots.
**GPU time:** ~48-72h
**Output:** Second-opinion anomaly catalog, cross-architecture agreement map, new Paper 3 figure
**Why it matters:** Multi-architecture consensus is the gold standard for anomaly detection. No one has done this at 22.5M scale.

### 3. Real NANOGrav + Multi-PTA Gravitational Wave Analysis
**Question:** Does the matter bounce GW spectrum fit the REAL NANOGrav 15yr data better than SMBHB?
**Data:** NANOGrav 15yr public data release (real timing residuals, not synthetic). Also EPTA DR2, PPTA DR3 if public.
**Scale:** ~67 pulsars × 15 years × biweekly observations
**Model:** enterprise + PTMCMCSampler (proper PTA likelihood, not emcee approximation). Full noise marginalization.
**Novel science:** FIRST proper Bayesian model comparison of bounce vs SMBHB using real PTA data with enterprise. Our current result (γ=3.33±0.40) used simplified likelihood. The real analysis with enterprise noise modeling could change the result.
**GPU time:** ~24-48h (MCMC is CPU-heavy but GPU-accelerated likelihood evaluation helps)
**Output:** Publication-ready NANOGrav result for Paper 1, proper Bayes factors
**Why it matters:** The PTA community cares deeply about the GW background origin. A proper bounce vs SMBHB comparison from real data would be cited.

---

## TIER 2: NOVEL SCIENCE, MEDIUM SCALE

### 4. Parity Violation Search in CMB Polarization (Real Planck + ACT data)
**Question:** Is cosmic birefringence β = 0.27° confirmed in real CMB data?
**Data:** Real Planck NPIPE or PR4 polarization maps (publicly available, ~2 GB). Real ACT DR6 IQU maps (5.3 GB, already on pod).
**Scale:** Full-sky Nside=2048 maps
**Model:** NaMaster pseudo-Cl estimator with proper mode-coupling, galactic mask, point source mask, multipole-by-multipole analysis. Cross-frequency consistency check (100 GHz vs 143 GHz vs 217 GHz).
**Novel science:** Independent measurement of cosmic birefringence with proper systematics control. Our current NaMaster validation used synthetic maps. This would be REAL.
**GPU time:** ~8-12h (NaMaster is CPU-intensive, GPU for map transforms)
**Output:** Real β measurement from Planck + ACT for Paper 1
**Why it matters:** The 3.6σ birefringence signal is one of the hottest topics in CMB physics. An independent measurement with our own pipeline would be publishable standalone.

### 5. Spectral Anomaly → Redshift Machine (unsupervised photo-z at scale)
**Question:** Can the BigAE "redshift neuron" (lat_067) be weaponized into a competitive photo-z estimator?
**Data:** DESI DR1 spectra with spectroscopic redshifts (22.5M labeled examples)
**Scale:** 22.5M training examples, 128-dim latent vectors already computed
**Model:** Train a proper regression head on lat_067 + top-20 latent dims. Then train a full neural photo-z network on the 128-dim latent space. Compare against standard broadband photo-z (σ_NMAD comparison).
**Novel science:** First demonstration that UNSUPERVISED spectral compression can match or beat SUPERVISED photo-z methods. The "redshift neuron" finding (18% importance from 1/128 dims, no supervision) is already remarkable — scaling it up could be a standalone paper.
**GPU time:** ~4-8h
**Output:** Competitive photo-z catalog, Paper 3 extension
**Why it matters:** Photo-z is a $100M problem in astronomy (every survey needs it). Showing unsupervised methods work is paradigm-shifting.

### 6. Cross-Survey Multi-Wavelength Anomaly Stacking
**Question:** What do the 123 multi-survey joint anomalies look like across ALL wavelengths?
**Data:** For each of the 123 objects detected in 2+ surveys: download DESI spectrum + SDSS spectrum + Legacy Survey image + WISE photometry + eROSITA X-ray (where available). Build SEDs.
**Scale:** 123 objects × 5 wavelength bands
**Model:** SED fitting with CIGALE or Prospector. Train a multi-modal classifier on the combined data.
**Novel science:** First systematic SED analysis of AI-discovered multi-survey anomalies. Some of these could be genuinely new types of objects — changing-look AGN, tidal disruption events, gravitationally lensed systems.
**GPU time:** ~4-8h
**Output:** Multi-wavelength atlas of 123 anomalies, potential new object classes
**Why it matters:** The intersection of anomalies across wavelengths is where the most exotic objects hide.

---

## TIER 3: SPECULATIVE BUT HIGH-CEILING

### 7. Gravitational Wave Echo Search in LIGO O4 Data
**Question:** Do black hole merger signals show echoes consistent with bounce cosmology?
**Data:** LIGO O4 public strain data (available via GWOSC)
**Scale:** ~100 confirmed merger events × ~4s of data each
**Model:** Matched filter + CNN echo detector. Train on simulated echoes with known bounce-predicted delay times.
**Novel science:** GW echoes would be smoking-gun evidence for non-classical black hole interiors (Planck-scale structure). No convincing detection yet.
**GPU time:** ~12-24h
**Output:** Upper limits or candidate detections, Paper 1 extension
**Why it matters:** If found, this is a Nobel-level discovery.

### 8. Primordial Black Hole Mass Function from f_NL Constraint
**Question:** What PBH mass distribution does f_NL = -35/8 predict, and is it consistent with all observational constraints?
**Data:** PBH constraint compilation (microlensing, CMB, GW, dynamical). Publicly available.
**Scale:** Numerical integration over mass function with non-Gaussian corrections
**Model:** Extended Press-Schechter with Edgeworth expansion (already prototyped in PBH experiment). Full mass function sweep.
**Novel science:** Definitive PBH mass function from the matter bounce, compared against ALL constraints simultaneously. The f_NL = -35/8 naturally suppresses overproduction — quantify exactly how much.
**GPU time:** ~2-4h
**Output:** PBH mass function figure, asteroid-mass PBH dark matter viability assessment
**Why it matters:** PBH dark matter is a hot topic. Our f_NL constraint uniquely pins the mass function.

### 9. Fine-Tune LLM on Astronomical Spectra (AstroGPT)
**Question:** Can a language model learn to "read" astronomical spectra and classify them in natural language?
**Data:** DESI DR1 spectra (22.5M) + SDSS spectra (2.3M) + Redrock classifications + our anomaly labels
**Scale:** ~25M spectra tokenized as 1D sequences
**Model:** Fine-tune a small LLM (Phi-3-mini or Llama-3-8B) to take spectral tokens as input and output natural language descriptions: "This is a z=3.2 QSO with broad Ly-alpha emission and a damped Lyman-alpha absorber at z=2.8."
**Novel science:** First spectral-language model. Would allow astronomers to "ask questions" about spectra in plain English.
**GPU time:** ~48-72h
**Output:** AstroGPT model on HuggingFace, demo webapp
**Why it matters:** This could genuinely transform how astronomers interact with survey data.

---

## DEPLOYMENT ORDER (next week)

| Day | Experiment | Data source | Est. Hours | Expected Output |
|-----|-----------|------------|------------|-----------------|
| 1 | #3 NANOGrav real PTA | NANOGrav 15yr public | 24-48h | Proper bounce vs SMBHB Bayes factor |
| 1 | #4 Real birefringence | Planck NPIPE + ACT DR6 | 8-12h | Real β measurement |
| 2-3 | #1 Galaxy morphology foundation model | GZ-DESI + Smith42 | 24-48h | Best-in-class classifier + Paper 4 figures |
| 3-4 | #5 Photo-z from latent space | DESI DR1 latents | 4-8h | Competitive unsupervised photo-z |
| 4-5 | #8 PBH mass function | Constraint compilation | 2-4h | Definitive PBH mass function |
| 5-7 | #2 DESI Transformer re-analysis | DESI DR1 full | 48-72h | Cross-architecture anomaly consensus |

**Total GPU budget: ~130-200h = ~$470-720 at $3.59/hr**

---

## WATCHDOG v2 PROTOCOL

The old watchdog was broken — it kept the GPU "busy" with synthetic loops that produced nothing. New protocol:

1. **Each experiment gets a completion handler** that writes results to `/root/results/<experiment>/summary.json` AND updates `/root/STATUS.md` with the finding
2. **Between experiments**: 5-minute cooldown for results verification, NOT immediate next launch
3. **If GPU idle >30 min with no experiment running**: launch next experiment from queue above
4. **If experiment crashes**: log error, skip to next, do NOT retry the same script endlessly
5. **Daily backup**: at end of each day's experiments, tar results to local, commit to GitHub
6. **Science gate**: before each experiment, ask "will this produce a result that changes a paper or a page on the site?" If no, skip it.

---

## WHAT MAKES THIS DIFFERENT FROM THE SYNTHETIC LOOP

| Old approach | New approach |
|-------------|-------------|
| Synthetic data generators | Real astronomical survey data |
| Same 5 scripts repeated 600+ times | 9 unique experiments, each run ONCE |
| AUC=0.58 every time (identical) | Each experiment answers a different scientific question |
| No new figures, no new papers | Every experiment produces at least one publication figure |
| $135 spent, 0 findings | $470-720 estimated, 9 genuine findings |
| Kept GPU "busy" (letter of the rule) | Keeps GPU PRODUCTIVE (spirit of the rule) |
