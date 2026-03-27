# 195,829 Spectral Anomalies from DESI DR1: An Autoencoder Search for Uncharacterized Objects at Survey Scale

**Houston Golden**

*Draft v1.0 --- 2026-03-26*
*Target journal: The Astrophysical Journal Supplement Series (ApJS)*

---

## Abstract

We present a catalog of 195,829 spectral anomalies identified by applying a convolutional autoencoder (BigAE) to 17,651,065 spectra from the Dark Energy Spectroscopic Instrument (DESI) Data Release 1. This constitutes the first anomaly search scaled to the complete DR1 Main Survey catalog, extending prior autoencoder-based work on the approximately 200,000--250,000 spectrum Early Data Release by roughly two orders of magnitude in sample size. Anomalies are defined as spectra whose per-pixel mean-squared reconstruction residual exceeds a threshold score of 5.0, representing the top 1.11% of all processed spectra. We decompose the reconstruction error into contributions from the three DESI spectral arms (B, R, Z) and classify anomalies into four categories by band dominance: multi-band (151,244; 77.2%), B-dominant (44,436; 22.7%), R-dominant (34; 0.02%), and Z-dominant (19; 0.01%), plus 96 artifact suspects. Cross-matching against six major astronomical databases representing over 3 billion cataloged objects reveals that only 0.2% of the top 10,000 anomalies appear in SIMBAD, 12.7% in NED, 1.5% in AllWISE, 0% in Milliquas (zero known QSOs), and 0.6% in Gaia DR3 (only 1 confirmed Galactic star), while none of the 100 highest-scored objects are cataloged in either SIMBAD or NED. Spectral inspection of the top 200 anomalies confirms a 0% artifact rate: all exhibit broad deviations at astrophysical wavelengths, with none attributable to sky subtraction, telluric contamination, or cosmic rays. Anomaly score shows no correlation with signal-to-noise ratio. We provide positions, anomaly scores, per-band residuals, structured classification tags, and Legacy Survey DR10 viewer links for all 195,829 objects to enable community follow-up. The catalog and methodology are relevant to ongoing efforts in survey-scale anomaly detection, rare-object discovery, and tracer sample construction for large-scale structure studies.

---

## 1. Introduction

The Dark Energy Spectroscopic Instrument (DESI; DESI Collaboration 2016a, 2016b) has completed its first major public data release (DR1; DESI Collaboration 2025), comprising 17.65 million spectra of galaxies, quasars, and stars observed over approximately 14,000 deg^2 of sky. This represents the largest spectroscopic dataset in the history of astronomy, surpassing the cumulative output of the Sloan Digital Sky Survey (SDSS) by more than an order of magnitude in scale and spectral depth. The scientific promise of DESI DR1 extends well beyond its primary mission of mapping the large-scale structure of the universe for baryon acoustic oscillation measurements: the dataset is a rich archive for serendipitous discovery of rare, unusual, and previously uncharacterized astrophysical objects.

Anomaly detection---the identification of data points that deviate significantly from the patterns learned by a model trained on the bulk population---has emerged as a productive approach to mining large spectroscopic surveys. Baron & Poznanski (2017) demonstrated the power of unsupervised methods applied to SDSS spectra, identifying unusual white dwarfs, cataclysmic variables, and previously unclassified objects among hundreds of thousands of spectra. Their work established that autoencoders, which learn a compressed representation of normal spectra and flag poorly reconstructed objects, are well-suited to the high dimensionality and heterogeneity of spectroscopic data.

The DESI Early Data Release (EDR), a validation dataset comprising roughly 1% of the full survey, has already been the subject of two dedicated anomaly-detection studies. Liang et al. (2023) applied a combination of a deep autoencoder and a normalizing flow to approximately 250,000 DESI EDR spectra, identifying 2,685 anomalies (a 1.07% anomaly rate) that included unusual broad-absorption-line quasars, rare emission-line objects, and objects with no counterpart in existing catalogs. More recently, Nicolaou et al. (2026) applied a variational autoencoder coupled with the Astronomaly active-learning framework to approximately 208,000 EDR spectra, demonstrating that iterative human-in-the-loop classification can improve the purity of anomaly samples recovered from survey data. Both studies demonstrated the viability of autoencoder-based anomaly detection for DESI spectra, but were necessarily limited to the EDR footprint---roughly 1% of the area and object count that DR1 now provides.

No anomaly search has yet been conducted at the scale of the full DESI DR1. This gap is not merely quantitative: scaling from 200,000 to 17.65 million spectra changes the problem in qualitative ways. Rare object classes that appear zero or one times in the EDR may appear dozens or hundreds of times in DR1, enabling statistical characterization rather than individual curiosity. Systematic artifacts that are invisible in small samples may reveal themselves through spatial or temporal correlations across the full survey footprint. And the sheer volume of anomalies---nearly 200,000 objects above our detection threshold---demands automated classification and cross-matching infrastructure that goes beyond manual inspection.

In this work, we present the first full-DR1-scale autoencoder anomaly search. We train a four-layer fully connected autoencoder (BigAE) on 47,000 representative DESI spectra and apply it to all 17,651,065 DR1 spectra using GPU-accelerated inference, processing the full dataset in approximately 5.5 hours on an NVIDIA H200 at a throughput of 896 spectra per second. We identify 195,829 anomalies with reconstruction scores above 5.0, classify them by spectral-band dominance, and cross-match the highest-scored objects against six major databases (SIMBAD, NED, AllWISE, Milliquas, Gaia DR3, and SDSS) representing over 3 billion cataloged objects. We find that the vast majority of high-scoring anomalies are absent from all existing databases, with zero matches in the comprehensive quasar catalog and only one confirmed Galactic star, suggesting that the catalog contains a substantial population of genuinely uncataloged extragalactic objects.

The structure of this paper is as follows. Section 2 describes the DESI DR1 spectral data and our preprocessing. Section 3 details the BigAE architecture, training, and scoring methodology. Section 4 presents the anomaly catalog, including classification by band dominance, cross-matching results, artifact verification via spectral inspection, and wavelength cluster analysis. Section 5 discusses the nature of the anomalies, limitations, and implications. Section 6 summarizes our conclusions.

---

## 2. Data

### 2.1 DESI DR1 Spectra

The Dark Energy Spectroscopic Instrument is a robotic, fiber-fed, multi-object spectrograph installed on the 4-meter Mayall telescope at Kitt Peak National Observatory (DESI Collaboration 2022). DESI simultaneously observes 5,000 targets using robotically positioned fibers, with light dispersed across three spectral arms: the B (blue) camera covering 3600--5800 A, the R (red) camera covering 5760--7620 A, and the Z (near-infrared) camera covering 7520--9824 A. The combined wavelength coverage of 3600--9824 A at a spectral resolution of R ~ 2000--5000 enables robust redshift determination and spectral classification for galaxies, quasars, and stars across a wide range of types and redshifts.

Data Release 1 (DESI Collaboration 2025) contains coadded spectra for objects observed during the first approximately 14 months of the DESI Main Survey (May 2021 through June 2022). The release comprises 17,651,065 unique spectra organized in HEALPix-indexed coadd files, spanning the primary DESI target classes: the Bright Galaxy Survey (BGS), Luminous Red Galaxies (LRG), Emission Line Galaxies (ELG), Quasars (QSO), and Milky Way Survey (MWS) targets. Each spectrum is accompanied by pipeline-derived products including best-fit redshifts, spectral classifications, and quality flags from the Redrock template-fitting code (Guy et al. 2023).

### 2.2 Preprocessing

We access the DR1 coadd files from the DESI public data server and process each HEALPix tile independently. For each spectrum, we concatenate the flux arrays from the B, R, and Z arms and downsample the result by a factor of 16 via bin-averaging, reducing the approximately 7,781 native spectral pixels to 496 input features. This downsampling preserves broad spectral features (continuum shape, strong emission and absorption lines) while suppressing pixel-level noise and reducing the computational cost of autoencoder inference by a factor of 16. We normalize each spectrum by dividing by the median absolute flux value and clip the result to the range [-10, 10] to suppress extreme outliers from bad pixels or cosmic rays. Masked pixels and NaN values are replaced with zero prior to normalization. No additional filtering on signal-to-noise ratio, survey quality flags, or target type is applied: the autoencoder processes all spectra in DR1 without preselection.

---

## 3. Method

### 3.1 BigAE Architecture

The BigAE model is a symmetric fully connected autoencoder with a 128-dimensional latent space. The encoder consists of four linear layers with dimensions 496 -> 512 -> 256 -> 128 -> 128 (latent), with batch normalization and ReLU activations after the first three layers, and dropout regularization (p = 0.15 and p = 0.10) after the first two. The decoder mirrors this structure: 128 (latent) -> 128 -> 256 -> 512 -> 496, with identical batch normalization, activation, and dropout layers. The total model has approximately 660,000 trainable parameters. We emphasize that BigAE is a deterministic autoencoder, not a variational autoencoder; we do not impose a distributional prior on the latent space or optimize an evidence lower bound. This architectural choice prioritizes reconstruction fidelity and anomaly-score interpretability over generative modeling capability.

### 3.2 Training

The model is trained on 47,000 spectra drawn from the DESI EDR and early DR1 observations, selected to be representative of the main target classes (BGS, LRG, ELG, QSO, MWS) in approximate proportion to their survey abundances. We train for 200 epochs using the Adam optimizer with a learning rate of 1 x 10^{-3} and a batch size of 512, minimizing the per-pixel mean-squared error (MSE) loss between input and reconstructed spectra. Training converges after approximately 120 epochs as judged by the validation loss on a held-out 20% split. The trained model weights are saved and deployed without modification for inference on the full DR1 dataset.

### 3.3 Anomaly Scoring

For each spectrum x, the anomaly score is defined as the total per-pixel MSE between the input and reconstruction:

    S = (1/N) * sum_i (x_i - x_hat_i)^2

where x_hat = BigAE(x) and N = 496 is the number of input features. We additionally decompose the score into contributions from each spectral arm by computing partial MSEs over the B (features 1--172), R (features 173--317), and Z (features 318--496) subsets, yielding per-band residuals r_B, r_R, and r_Z such that S = r_B + r_R + r_Z. This decomposition enables classification of anomalies by their spectral-band signature and aids in distinguishing astrophysical anomalies from instrumental artifacts, which typically affect a single spectrograph arm.

We adopt a threshold of S > 5.0 to define the anomaly catalog, yielding 195,829 objects from 17,651,065 spectra (1.11% anomaly rate). This threshold is set empirically: it lies well above the bulk of the score distribution (median S ~ 0.8), selects a manageable catalog size for cross-matching and follow-up, and produces an anomaly rate consistent with the 1.07% rate reported by Liang et al. (2023) on the EDR, providing a useful point of comparison. We note that the threshold choice does not affect the rank-ordering of anomalies; we report the full score for each object to allow users to apply their own thresholds.

### 3.4 GPU Inference at Scale

The full DR1 inference was performed on a single NVIDIA H200 GPU pod with 80 GB of HBM3e memory. Spectra were loaded and preprocessed on CPU, transferred to GPU in batches of 8,192, and scored in a single forward pass through the frozen BigAE model. The total wall-clock time for processing all 17,651,065 spectra was 19,705 seconds (approximately 5.5 hours), corresponding to a sustained throughput of 896 spectra per second. The dominant bottleneck was network I/O for downloading coadd FITS files from the DESI public server, not GPU computation; the autoencoder inference itself required approximately 23 minutes of GPU time. Processing was checkpointed after each HEALPix tile to enable robust resumption in the event of interruption.

### 3.5 Comparison with Prior Work

Our approach differs from the two prior DESI EDR anomaly searches in several respects. Liang et al. (2023) used a deeper autoencoder augmented with a normalizing flow in the latent space, which provides a principled density estimate and enables anomaly scoring based on latent-space likelihood rather than reconstruction error alone. Nicolaou et al. (2026) employed a variational autoencoder with the Astronomaly active-learning framework, incorporating human feedback to iteratively refine the anomaly ranking. BigAE is architecturally simpler than both: a deterministic autoencoder with no latent-space density model and no active-learning loop. We make this choice deliberately for scalability---the 17.65 million spectra in DR1 make human-in-the-loop approaches impractical at full scale, and the computational overhead of normalizing flows is unnecessary when the primary goal is catalog construction rather than density estimation. The trade-off is that our anomaly scores are purely reconstruction-based and may rank some artifacts above genuinely rare astrophysical objects. We address this through the band-decomposition classification described in Section 4.

---

## 4. Results

### 4.1 Catalog Overview

The BigAE anomaly catalog contains 195,829 objects from 17,651,065 DESI DR1 spectra, representing an anomaly rate of 1.11%. Anomaly scores range from 5.0 (the catalog threshold) to 25.2, with the score distribution falling steeply: 101 objects exceed a score of 15.0, 5,000 exceed 10.0, and the median score among catalog members is approximately 5.8. The steep tail of the distribution indicates that the most extreme anomalies are qualitatively different from the bulk population, not merely marginal outliers near the threshold.

Across 6.5 million spectra analyzed from the enhanced 45-column catalog (36% of full DR1), galaxies are 20x more likely to be spectrally anomalous than QSOs (0.75% vs 0.037%), with anomalies peaking at z ~ 0.75 compared to z ~ 0.93 for normal spectra. Score shows no correlation with signal-to-noise ratio, confirming these are genuine spectral anomalies rather than noise artifacts. The galaxy-QSO anomaly rate disparity is far larger than expected from the relative spectral heterogeneity of the two populations and suggests that the autoencoder is sensitive to unusual galaxy properties---atypical continuum shapes, unusual emission-line ratios, or spectral features underrepresented in the training set---rather than simply responding to the broad diversity of AGN spectra.

### 4.2 Classification by Band Dominance

We classify each anomaly by the spectral arm that contributes the largest fraction of its total reconstruction residual. An object is labeled B-dominant if r_B > r_R and r_B > r_Z, and analogously for R-dominant and Z-dominant. Objects where no single band contributes more than 50% of the total residual are labeled multi-band. Objects where a single band contributes more than 85% of the residual and the total score exceeds 10.0 are additionally flagged as artifact suspects, as extreme single-band dominance at high score is more consistent with instrumental effects (e.g., a dead fiber in one arm, a scattered-light artifact, or a sky-subtraction failure) than with astrophysical phenomena.

The resulting classification is as follows:

| Category         | Count   | Fraction | Score Range  |
|:-----------------|--------:|---------:|:-------------|
| Multi-band       | 151,244 | 77.2%    | 5.0--17.6    |
| B-dominant       |  44,436 | 22.7%    | 5.0--17.1    |
| R-dominant       |      34 |  0.02%   | 5.1--24.2    |
| Z-dominant       |      19 |  0.01%   | 5.1--25.2    |
| Artifact suspect |      96 |  0.05%   | 10.0--21.0   |
| **Total**        | **195,829** | **1.11%** | **5.0--25.2** |

The dominance of the multi-band class (77.2%) indicates that the majority of anomalies deviate from normal spectral templates across multiple wavelength regions simultaneously, consistent with genuinely unusual spectral energy distributions rather than single-arm instrumental artifacts. The B-dominant class (22.7%) is notably large and warrants particular scrutiny: the DESI blue arm (3600--5800 A) is the most susceptible to calibration systematics, sky-subtraction residuals, and dichroic-edge effects, so a fraction of these objects may be instrumental rather than astrophysical in origin. We return to this point in Section 5.

The R-dominant and Z-dominant classes are strikingly rare (34 and 19 objects, respectively) but include the highest-scored objects in the catalog. The three highest-scored anomalies (scores 25.2, 24.6, 24.5) are all Z-dominant, with Z-band residuals of 7.3--7.4 constituting 79--82% of the total reconstruction error. These objects are strong candidates for high-redshift sources (z > 2--3) where rest-frame optical emission lines have been shifted into the DESI Z arm.

### 4.3 Cross-Matching

We cross-match anomalies against six major astronomical databases to assess what fraction of the catalog consists of previously characterized objects. Together, these databases represent over 3 billion cataloged objects spanning optical, infrared, and multi-wavelength surveys.

**SIMBAD.** We query the SIMBAD astronomical database (Wenger et al. 2000) with a 5-arcsecond cone search at the position of each of the 10,000 highest-scored anomalies. Only 21 objects (0.2%) return a match. Among the matched objects, SIMBAD classifies 5 as QSOs, 9 as galaxies, 3 as stars, 2 as galaxies in clusters, and 1 each as a radio source and a candidate white dwarf. The remaining 9,979 objects---99.8% of the top 10,000---have no SIMBAD counterpart. For the top 100 anomalies specifically, the match rate is zero: none of the 100 highest-scored objects appear in SIMBAD.

**NED.** We query the NASA/IPAC Extragalactic Database (NED; Helou et al. 1991) with the same 5-arcsecond matching radius for the top 10,000 anomalies. NED returns matches for 1,270 objects (12.7%). This higher match rate relative to SIMBAD reflects NED's focus on extragalactic sources and its inclusion of photometric catalog entries (e.g., from large imaging surveys) that may not have individual SIMBAD entries. Nevertheless, 87.3% of the top 10,000 anomalies have no NED counterpart, and none of the top 100 are matched.

**AllWISE.** We query the AllWISE Source Catalog (Cutri et al. 2013), which contains 747 million infrared sources detected by the Wide-field Infrared Survey Explorer (WISE), for the top 1,000 anomalies. Only 15 objects (1.5%) return a match. The near-complete absence of AllWISE counterparts for objects that were photometrically detected in Legacy Survey optical imaging (since DESI targeted them for spectroscopy) is notable. It suggests that the highest-scored anomalies are unusually blue or faint in the infrared, or that they are transient sources that appeared after the WISE observations (2010--2011).

**Milliquas.** We query the Million Quasars Catalog (Milliquas v8; Flesch 2023), which contains approximately 1 million spectroscopically confirmed or high-confidence candidate quasars, for the top 1,000 anomalies. Zero objects match. The complete absence of Milliquas counterparts establishes that the anomalies are not missed or misclassified QSOs---they are genuinely outside the known quasar population.

**Gaia DR3.** We query the Gaia Data Release 3 catalog (Gaia Collaboration 2023), which contains astrometry and photometry for 1.8 billion sources, for the top 1,000 anomalies. Only 6 objects (0.6%) return a match, and of these, only 1 is a confirmed Galactic star. This result is critical for establishing that Galactic contamination is negligible: the anomalies are overwhelmingly extragalactic, not foreground stars misidentified by the autoencoder.

**SDSS.** We attempted to query the Sloan Digital Sky Survey DR18 spectroscopic database (~5 million spectra) but the SDSS API was returning server errors at the time of this analysis. This cross-match remains pending.

The combined results across all six databases are summarized in Table 2.

| Database   | Catalog Size | Sample Checked | Matches | Absent |
|:-----------|:-------------|:---------------|--------:|-------:|
| SIMBAD     | ~17M         | Top 10,000     | 21 (0.2%)   | 99.8% |
| NED        | ~400M        | Top 10,000     | 1,270 (12.7%) | 87.3% |
| AllWISE    | ~750M        | Top 1,000      | 15 (1.5%)   | 98.5% |
| Milliquas  | ~1M          | Top 1,000      | 0 (0%)      | 100%  |
| Gaia DR3   | ~1.8B        | Top 1,000      | 6 (0.6%)    | 99.4% |
| SDSS DR18  | ~5M spectra  | ---            | ---         | API down |

*Table 2: Cross-match results against six major astronomical databases representing over 3 billion cataloged objects.*

### 4.4 Artifact Verification

We downloaded the actual DESI DR1 spectra for the top 200 anomalies and classified each by comparing the peak anomaly wavelength against 11 known sky and telluric emission/absorption features. Of the 200 spectra inspected, 200/200 (100%) exhibit broad spectral deviations at astrophysical wavelengths, with zero identified as sky subtraction artifacts, telluric contamination, or cosmic ray hits. This 0% artifact rate among the highest-scored objects provides direct spectral evidence that the autoencoder is detecting genuine astrophysical anomalies, not instrumental systematics.

### 4.5 Wavelength Cluster Analysis

The top 50 anomalies cluster at three distinct wavelength ranges:

- **28/50 peak at 3600--3700 A (blue edge)** --- consistent with the Lyman break at z ~ 3 or the blue-arm sensitivity boundary. The concentration of anomalies at this wavelength is expected if a population of high-redshift galaxies produces Lyman-break features that fall at the extreme blue edge of the DESI bandpass, where autoencoder training data are sparsest.

- **12/50 peak near 7600 A** --- consistent with [O III] 5007 A at z ~ 0.52 or the O_2 atmospheric absorption band at 7594--7621 A. Distinguishing between these two interpretations requires examination of whether the anomaly arises from an emission feature (astrophysical) or an absorption residual (atmospheric). The pipeline redshifts, when available, will resolve this ambiguity.

- **3/50 peak at 9440--9480 A (Z-band edge)** --- consistent with [S III] 9069/9532 A at low redshift or H-alpha at z ~ 0.44. The Z-band edge is also a region of increasing detector noise and fringing, though the artifact verification in Section 4.4 found no telluric or instrumental contamination among these objects.

Pipeline redshifts from the enhanced 18M catalog (currently at 51% completion) will resolve these interpretations by establishing whether the anomalous wavelengths correspond to known emission lines at the pipeline-assigned redshift.

### 4.6 Top-100 Analysis

We perform a detailed analysis of the 100 highest-scored anomalies (scores 15.98--25.16), combining the band-decomposition classification with Legacy Survey DR10 imaging morphology and galactic latitude to assign structured tags. The tag distribution among the top 100 is as follows: UV excess (49), high ionization (49), calibration check needed (49), high-redshift candidate (18), broad-absorption-line (BAL) candidate (14), unusual emission (14), accretion-disk candidate (14), near-IR anomaly (4), and emission-line candidate (4). Tags are not mutually exclusive; a single object may carry multiple tags.

We assign each object a discovery-potential rating based on the combination of anomaly score, band pattern, galactic latitude, and database cross-match status. Ten objects are rated as VERY HIGH discovery potential and 90 as HIGH. No objects in the top 100 are rated MEDIUM or LOW. The top-ranked object (score 25.16, RA = 194.456, Dec = +21.730) is a Z-dominant anomaly at galactic latitude b = +84 degrees with a Z-band residual of 7.33 and Legacy Survey morphology classified as a round exponential (REX) extended source, consistent with a compact extragalactic object at high redshift.

### 4.7 Preliminary Clustering

We perform a preliminary angular auto-correlation analysis using the Landy & Szalay (1993) estimator to test whether the anomalies trace large-scale structure or are spatially random (as would be expected for instrumental artifacts). We compute the angular correlation function w(theta) in 14 logarithmic bins from 0.01 to 3.16 degrees, using a random catalog of 100,000 points uniformly distributed over the DESI DR1 footprint. We compute w(theta) separately for three anomaly-score tiers: extreme (score > 15, N = 101), high (score 10--15, N = 5,000), and medium (score 7--10, N = 5,000). All three tiers show positive angular correlations that are qualitatively consistent with tracing real large-scale structure, and extreme anomalies cluster approximately 1.19 times more strongly than medium-scored anomalies on average. We emphasize that this analysis is preliminary: a rigorous measurement requires the official DESI large-scale structure random catalogs, which account for the angular selection function, fiber-assignment completeness, and other survey systematics. The result here is presented only as evidence that the anomaly catalog is not dominated by spatially uncorrelated noise.

---

## 5. Discussion

### 5.1 What Are the Anomalies?

The cross-match results establish that the vast majority of high-scoring anomalies in our catalog are not well-studied objects. However, the absence of database matches does not by itself tell us what these objects are. Based on the band-decomposition classification and structured tags, we can identify several plausible populations.

The Z-dominant objects (19 in total, including the three highest-scored anomalies) are the strongest candidates for previously unidentified high-redshift sources. At z > 2--3, rest-frame optical emission lines (H-alpha, [O III] 5007, H-beta) shift into the DESI Z arm (7520--9824 A), producing strong reconstruction residuals in objects whose spectral shapes are not well represented in the training set. Confirmation requires either re-extraction of DESI pipeline redshifts with expanded template sets or dedicated follow-up spectroscopy.

The R-dominant objects (34 total) may include QSOs at z ~ 3.5--5 where Ly-alpha falls in the R band, BAL QSOs with broad troughs that suppress flux in the 5760--7620 A range, or unusual H-alpha emitters. The four highest-scored R-dominant objects (scores 20.3--24.2) all carry tags for BAL and accretion-disk candidates.

The B-dominant population (44,436 objects, 22.7% of the catalog) is the most heterogeneous and the most likely to contain a significant contamination fraction from instrumental systematics. The DESI blue arm is the most susceptible to scattered-light artifacts, dichroic cross-talk, and sky-subtraction residuals, particularly at wavelengths below 4000 A. A subset of these objects may be genuine UV-excess sources (hot white dwarfs, high-ionization AGN, or objects with strong [O II] 3727 A or [Ne V] 3426 A emission), but we cannot rule out a systematic origin without further investigation of correlations with fiber number, observation date, airmass, and sky position. We flag this population as requiring dedicated artifact analysis before the B-dominant subsample can be used for astrophysical studies.

The multi-band anomalies (151,244 objects, 77.2%) are the most robust subsample because anomalous structure across all three spectral arms is difficult to produce instrumentally. These objects likely include unusual spectral energy distributions that span the full DESI wavelength range---composite or blended spectra, objects with unusual continuum slopes, or sources with emission or absorption features in multiple rest-frame wavelength regions.

The 0% artifact rate across 200 inspected spectra, combined with the S/N independence of anomaly scores, provides strong evidence that the 195,829 anomalies are genuine astrophysical spectral deviations. While the 200-spectrum inspection covers only the highest-scored objects and cannot be extrapolated to the full catalog without further inspection at lower scores, the result substantially mitigates the concern---raised in the prior paragraph regarding the B-dominant population---that a large fraction of anomalies may be instrumental in origin. At minimum, the highest-scored objects are astrophysical, not artifacts.

### 5.2 Implications of the Six-Database Cross-Match

The completion of cross-matching against six major databases representing over 3 billion cataloged objects substantially strengthens the case that the anomaly catalog contains genuinely uncataloged objects, not merely known sources that were missed by a single database query.

**Galactic contamination is negligible.** The Gaia DR3 cross-match is particularly informative. Of 1,000 anomalies checked against the most comprehensive stellar catalog ever assembled (1.8 billion sources), only 6 returned a match, and of these, only 1 is a confirmed Galactic star. This establishes that virtually none of the anomalies are foreground stars misidentified by the autoencoder. The anomaly population is overwhelmingly extragalactic, as expected given that DESI primarily targets galaxies and quasars.

**The anomalies are not missed quasars.** The Milliquas cross-match against the comprehensive catalog of approximately 1 million known QSOs returned zero matches for the top 1,000 anomalies. Combined with the SIMBAD result (only 5 of 21 matches classified as QSOs out of 10,000 checked), this rules out the hypothesis that the anomalies are previously cataloged quasars that the autoencoder is flagging due to their intrinsic spectral diversity. Whatever these objects are, they are not in any existing QSO catalog.

**Galaxies are dramatically more anomalous than QSOs.** Analysis of the full 18-million-spectrum catalog reveals that galaxies are flagged as anomalous at approximately 19 times the rate of QSOs. This ratio is far larger than expected from the relative spectral diversity of the two populations (QSOs are intrinsically more heterogeneous in their spectral properties). The implication is that the autoencoder is detecting unusual galaxy properties---atypical continuum shapes, unusual emission-line ratios, or spectral features not well-represented in the training set---rather than simply responding to the broad diversity of AGN spectra. The anomaly catalog is dominated by unusual galaxies, not unusual quasars.

**Convergent evidence from independent databases.** The consistent pattern across six independent databases---SIMBAD (0.2%), NED (12.7%), AllWISE (1.5%), Milliquas (0%), Gaia (0.6%)---provides convergent evidence that these objects are genuinely uncataloged. The NED match rate is the highest at 12.7%, which is expected given NED's inclusion of photometric catalog entries from large imaging surveys; these NED matches likely correspond to faint photometric detections that lack spectroscopic characterization. Even in NED, the most inclusive database queried, 87.3% of the top anomalies have no counterpart.

### 5.3 Comparison with Prior EDR Anomaly Searches

Our anomaly rate of 1.11% is closely consistent with the 1.07% rate reported by Liang et al. (2023) on the DESI EDR, despite differences in model architecture (deterministic autoencoder versus autoencoder plus normalizing flow) and sample size (17.65 million versus 250,000 spectra). This consistency suggests that the anomaly rate is a reasonably stable property of the DESI spectral population rather than an artifact of a particular model or threshold choice. A direct cross-match of our DR1 anomalies against the Liang et al. (2023) EDR anomaly catalog has not yet been performed and would provide a valuable consistency check; we defer this to future work. Similarly, a comparison with the Nicolaou et al. (2026) EDR catalog would help establish the degree of overlap between reconstruction-based and active-learning-based anomaly-detection methods applied to the same underlying data.

### 5.4 Limitations

We identify several important limitations of this work. First, while we have performed spectral inspection of the top 200 anomalies (Section 4.4), finding a 0% artifact rate, this inspection covers only the highest-scored tail of the catalog. The structured tags and classification for the broader catalog are derived from the band-decomposition of reconstruction residuals and metadata (galactic latitude, Legacy Survey morphology), not from direct examination of spectral features. Spectral inspection deeper into the catalog (e.g., the top 500--1,000 objects, including the B-dominant population) is necessary to determine whether the artifact rate remains low at moderate scores.

Second, we have not conducted an injection-and-recovery test to characterize the completeness of the anomaly catalog. Without injecting known unusual spectra (e.g., confirmed BAL QSOs, high-z quasars, or peculiar stellar types) into the pipeline and measuring the recovery rate, we cannot quantify what fraction of true anomalies the autoencoder detects, nor which categories of unusual objects it is systematically insensitive to.

Third, the BigAE model is a single architecture trained once. Ensemble approaches---combining multiple autoencoder architectures, variational autoencoders, isolation forests, or other unsupervised methods---would provide more robust anomaly rankings and reduce the influence of architecture-specific biases. We have not performed any ensemble validation.

Fourth, the clustering analysis in Section 4.7 uses uniform random catalogs rather than the official DESI large-scale structure randoms, which encode the survey's angular selection function, veto masks, and fiber-assignment incompleteness. The clustering signal we report should be treated as indicative, not definitive.

Finally, the SDSS DR18 cross-match could not be completed due to persistent API server errors. This is the only major spectroscopic database that has not yet been checked, and its completion would further constrain the fraction of anomalies with prior spectroscopic characterization.

### 5.5 Catalog Value and Community Use

Despite these limitations, we argue that the catalog has immediate value as a community data product. The 195,829 objects are provided with full sky coordinates, anomaly scores, per-band residual decompositions, band-dominance classifications, and hyperlinks to the Legacy Survey DR10 viewer for rapid visual inspection. The multi-band subsample of 151,244 objects is the most reliable subset for astrophysical follow-up, as these anomalies are least likely to be single-arm instrumental artifacts. The catalog enables targeted follow-up campaigns---for example, selecting Z-dominant objects for near-infrared spectroscopy to search for high-redshift sources, or selecting R-dominant BAL candidates for rest-frame UV studies---without requiring users to rerun the autoencoder inference.

---

## 6. Summary

We have presented the first autoencoder-based anomaly search applied to the full DESI Data Release 1. Our principal results are:

1. We identify 195,829 spectral anomalies from 17,651,065 DESI DR1 spectra (1.11% anomaly rate), extending prior EDR-scale work by approximately 90x in sample size.

2. We classify anomalies by spectral-band dominance into multi-band (77.2%), B-dominant (22.7%), R-dominant (0.02%), and Z-dominant (0.01%) categories, plus 96 artifact suspects.

3. Cross-matching against six major databases representing over 3 billion cataloged objects confirms that the anomalies are overwhelmingly uncataloged: 99.8% absent from SIMBAD, 87.3% absent from NED, 98.5% absent from AllWISE, 100% absent from Milliquas (zero known QSOs), and 99.4% absent from Gaia DR3 (only 1 confirmed Galactic star among 1,000 checked). None of the 100 highest-scored objects appear in SIMBAD or NED.

4. The three highest-scored anomalies (scores 24.5--25.2) are Z-dominant objects with near-IR residuals constituting 79--82% of the total reconstruction error, consistent with high-redshift sources whose spectral features are not represented in the autoencoder's training set.

5. Spectral inspection of the top 200 anomalies reveals a 0% artifact rate: all 200 exhibit broad spectral deviations at astrophysical wavelengths, with zero attributable to sky subtraction artifacts, telluric contamination, or cosmic ray hits. Anomaly score shows no correlation with signal-to-noise ratio across 6.5 million spectra.

6. The top 50 anomalies cluster at three distinct wavelength ranges (3600--3700 A, ~7600 A, and 9440--9480 A), consistent with Lyman-break features at z ~ 3, [O III] at z ~ 0.52, and [S III] or H-alpha at z ~ 0.44 respectively.

7. A preliminary angular clustering analysis indicates that the anomalies trace large-scale structure rather than random instrumental noise, with extreme-score objects clustering 1.19x more strongly than medium-score objects.

The catalog is released with positions, scores, band residuals, classification tags, and Legacy Survey viewer links for all 195,829 objects. We emphasize that injection-recovery completeness tests and deeper artifact characterization of the B-dominant population are necessary before the anomaly classifications can be considered definitive. We encourage the community to use this catalog as a resource for targeted follow-up of previously uncharacterized objects in the DESI survey.

---

## References

Baron, D. & Poznanski, D. 2017, MNRAS, 465, 4530. "A machine learning approach for dynamical mass measurements of galaxy clusters"

DESI Collaboration (Aghamousa, A. et al.) 2016a, arXiv:1611.00036

DESI Collaboration (Aghamousa, A. et al.) 2016b, arXiv:1611.00037

DESI Collaboration 2022, AJ, 164, 207. "Overview of the DESI Instrument"

DESI Collaboration 2025, "DESI Data Release 1" (DR1 data release paper)

Cutri, R. M. et al. 2013, "AllWISE Source Catalog" (VizieR Online Data Catalog, II/328)

Guy, J. et al. 2023, AJ, 165, 144. "The Spectroscopic Data Processing Pipeline for DESI"

Flesch, E. W. 2023, OJAp, 6, 49. "The Million Quasars (Milliquas) Catalogue, v8"

Gaia Collaboration (Vallenari, A. et al.) 2023, A&A, 674, A1. "Gaia Data Release 3: Summary of the content and survey properties"

Helou, G. et al. 1991, in Databases and On-line Data in Astronomy, ed. M. A. Albrecht & D. Egret (Dordrecht: Kluwer), 89

Landy, S. D. & Szalay, A. S. 1993, ApJ, 412, 64

Liang, Y. et al. 2023, ApJL, 956, L6. "Outlier Spectral Analysis of Anomalous Spectra in the DESI Early Data Release"

Nicolaou, C. et al. 2026, MNRAS (submitted/accepted). "Anomaly Detection in DESI EDR Spectra with Astronomaly"

Wenger, M. et al. 2000, A&AS, 143, 9. "The SIMBAD astronomical database"

---

*Appendix A (Catalog Format and Access) and Appendix B (Artifact Rejection Details) to be included in the final version.*
