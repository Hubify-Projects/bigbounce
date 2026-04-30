// AUTO-GENERATED from /figures.html — do not edit by hand.
// Regenerate with: cd site && node scripts/extract-figures.mjs

export interface Figure {
  src: string;
  alt: string;
  number: string;
  title: string;
  desc: string;
  source: string;
}

export interface FigureSection {
  title: string;
  count: string;
  items: Figure[];
}

export const figureSections: FigureSection[] = [
  {
    "title": "Paper 3 — DESI Spectral Anomalies",
    "count": "12 figures",
    "items": [
      {
        "src": "/public/images/z6_qso_spectra_grid.png",
        "alt": "Grid of 12 reionization-era QSO spectra at redshift z greater than 6, showing Gunn-Peterson troughs, Ly-alpha emission, and anomalous spectral features from the DESI DR1 archive",
        "number": "Figure 53",
        "title": "12 Reionization-Era QSO Spectra (z > 6)",
        "desc": "12 QSOs at z > 6 from the gold anomaly catalog showing Gunn-Peterson troughs, Ly-α emission, and anomalous spectral features. Downloaded from the DESI DR1 archive.",
        "source": "Enhanced 22.5M Catalog (2026-03-28)"
      },
      {
        "src": "/public/images/umap_clusters.png",
        "alt": "UMAP Clustering of 195,829 DESI DR1 Spectral Anomalies colored by HDBSCAN cluster",
        "number": "Figure 54",
        "title": "UMAP Clustering of 195,829 Spectral Anomalies",
        "desc": "2D UMAP embedding of 195,829 anomalies colored by HDBSCAN cluster. Two distinct populations: a large B-band noise cluster and a red-anomaly cluster with genuinely unusual spectral features.",
        "source": "Enhanced 22.5M Catalog (2026-03-28)"
      },
      {
        "src": "/public/images/anomaly_rate_map.png",
        "alt": "HEALPix Mollweide sky map of DESI DR1 anomaly rate showing mostly uniform ~1% rate across the survey footprint with Spearman r=0.03 correlation with depth, confirming anomalies are not depth-correlated artifacts",
        "number": "Figure 55",
        "title": "Anomaly Rate Sky Map (Mollweide)",
        "desc": "HEALPix NSIDE=64 map of anomaly rate across the DESI DR1 footprint. Mostly uniform ~1% (Spearman r = 0.03 with depth), confirming anomalies are not depth-correlated artifacts.",
        "source": "Enhanced 22.5M Catalog (2026-03-28)"
      },
      {
        "src": "/public/images/survey_depth_map.png",
        "alt": "HEALPix map of DESI DR1 survey depth showing objects per pixel across the survey footprint with variable coverage across sky regions",
        "number": "Figure 56",
        "title": "DESI DR1 Survey Depth Map",
        "desc": "Objects per HEALPix pixel showing the survey footprint and variable depth across the DESI DR1 coverage area.",
        "source": "Enhanced 22.5M Catalog (2026-03-28)"
      },
      {
        "src": "/public/images/depth_vs_rate_scatter.png",
        "alt": "Scatter plot of DESI DR1 anomaly rate versus survey depth showing weak anti-correlation r=-0.17 with outliers concentrated at survey edges",
        "number": "Figure 57",
        "title": "Anomaly Rate vs Survey Depth",
        "desc": "Scatter plot showing weak anti-correlation (r = −0.17) between anomaly rate and survey depth. Bulk footprint clean; outliers concentrated at survey edges.",
        "source": "Enhanced 22.5M Catalog (2026-03-28)"
      },
      {
        "src": "/public/images/photo_z_scatter.png",
        "alt": "Scatter plot of photometric redshift predicted from 128-dim autoencoder latent vectors versus spectroscopic redshift, showing sigma_NMAD=0.028 and R-squared=0.79 with zero redshift supervision during training",
        "number": "Figure 58",
        "title": "Photo-z from Latent Vectors (σNMAD = 0.028)",
        "desc": "Predicted photometric redshift from 128-dim autoencoder latent vectors vs spectroscopic redshift. σNMAD = 0.028, R&sup2; = 0.79, with zero redshift supervision during training. The autoencoder spontaneously learned spectral features correlated with redshift.",
        "source": "Paper 3 (2026-03-28)"
      },
      {
        "src": "/public/images/photo_z_feature_importance.png",
        "alt": "Bar chart of feature importance for 128 autoencoder latent dimensions predicting redshift, showing lat_067 as the dominant redshift neuron that spontaneously encodes spectroscopic redshift without supervision",
        "number": "Figure 59",
        "title": "Latent Dimension Feature Importance (Redshift Neuron)",
        "desc": "Feature importance of 128 latent dimensions for redshift prediction. lat_067 dominates as the “redshift neuron” — a single latent dimension that spontaneously encodes redshift without any supervision, the strongest individual predictor of spectroscopic z.",
        "source": "Paper 3 (2026-03-28)"
      },
      {
        "src": "/public/images/umap_full_catalog_3panel.png",
        "alt": "Three-panel UMAP embedding of 22.5M DESI DR1 catalog latent space colored by spectral type, redshift, and anomaly score, showing clean separation of galaxy, QSO, and star populations",
        "number": "Figure 60",
        "title": "Full-Catalog Latent Space (Type/Redshift/Score)",
        "desc": "3-panel UMAP embedding of the full 22.5M catalog latent space, colored by spectral type, redshift, and anomaly score. Reveals clean separation of galaxy/QSO/star populations and smooth redshift gradients in the unsupervised embedding.",
        "source": "Paper 3 (2026-03-28)"
      },
      {
        "src": "/public/images/photo_z_residuals.png",
        "alt": "Distribution of photo-z residuals (predicted minus spectroscopic redshift) showing tight core with sigma_NMAD=0.028 and outlier characterization for unsupervised autoencoder-based redshift estimation",
        "number": "Figure 61",
        "title": "Photo-z Residual Distribution",
        "desc": "Distribution of photo-z residuals (zpred − zspec) showing tight core with σNMAD = 0.028 and outlier characterization. Demonstrates the quality of unsupervised redshift estimation from autoencoder latent vectors.",
        "source": "Paper 3 (2026-03-28)"
      },
      {
        "src": "/public/images/taxonomy_umap.png",
        "alt": "UMAP embedding of 2,145 SNR-filtered DESI DR1 anomalies colored by HDBSCAN cluster revealing 10 distinct spectral families including 76 uncataloged AGN, 27 post-starburst galaxies, and 363 blue compact galaxies",
        "number": "Figure 62",
        "title": "Anomaly Taxonomy UMAP (10 Families)",
        "desc": "UMAP embedding of 2,145 SNR-filtered anomalies colored by HDBSCAN cluster, revealing 10 distinct spectral families: 76 uncataloged AGN, 27 post-starburst galaxies, 363 blue compact galaxies, plus 7 additional families. First spectral taxonomy of DESI DR1 anomalies.",
        "source": "Paper 3 (2026-03-29)"
      },
      {
        "src": "/public/images/fnl_comparison.png",
        "alt": "Comparison of sigma(f_NL) between standard DESI tracers and latent-space-selected anomalous tracers, showing 6.1% improvement from DESI alone and 7.93% improvement with 5-tracer combination",
        "number": "Figure 63",
        "title": "fNL Tracer Comparison (6.1–7.93% Improvement)",
        "desc": "Comparison of σ(fNL) between standard DESI tracers and latent-space-selected anomalous tracers. The anomaly-selected sample yields a 6.1% improvement in fNL sensitivity from DESI alone (7.93% with 5-tracer), directly strengthening the flagship matter-bounce prediction for SPHEREx.",
        "source": "Paper 3 (2026-03-29)"
      },
      {
        "src": "/public/images/uncataloged_top50_grid.png",
        "alt": "Grid of the 50 highest-scored DESI DR1 anomalies absent from both SIMBAD and NED catalogs, representing genuinely uncharacterized objects identified from 22.5 million spectra as follow-up targets",
        "number": "Figure 64",
        "title": "Top 50 Uncataloged Anomaly Spectra",
        "desc": "Grid of the 50 highest-scored anomalies absent from both SIMBAD and NED. These represent genuinely uncharacterized objects identified by the autoencoder from 22.5M DESI DR1 spectra — concrete targets for spectroscopic follow-up.",
        "source": "Paper 3 (2026-03-29)"
      }
    ]
  },
  {
    "title": "Paper 4 — Galaxy Chirality Catalog",
    "count": "13 figures",
    "items": [
      {
        "src": "/public/images/chirality/fig_raw_vs_eq.png",
        "alt": "Raw vs Equivariant: Eliminating Survey Systematics",
        "number": "Figure 34",
        "title": "Raw vs Equivariant: Eliminating Survey Systematics",
        "desc": "Side-by-side Mollweide maps showing how equivariant averaging eliminates a 94.6σ systematic pattern down to null. The key figure demonstrating the method’s power: raw CNN outputs contain catastrophic survey-correlated bias that vanishes under flip-averaging.",
        "source": "Paper 4, Figure 11"
      },
      {
        "src": "/public/images/chirality/fig_sky_map.png",
        "alt": "Galaxy Chirality Asymmetry Map (Mollweide)",
        "number": "Figure 35",
        "title": "Galaxy Chirality Asymmetry Map (Mollweide)",
        "desc": "All-sky map of CW–CCW asymmetry from 8.47 M equivariant spiral classifications at NSIDE=64. Blue pixels indicate clockwise excess; red pixels indicate counter-clockwise excess. Post-TTA dipole amplitude 0.0019, 0.43σ — consistent with parity conservation.",
        "source": "Paper 4, Figure 7"
      },
      {
        "src": "/public/images/chirality/fig_multipoles.png",
        "alt": "Angular Power Spectrum (l=1-5)",
        "number": "Figure 36",
        "title": "Angular Power Spectrum (ℓ=1–5)",
        "desc": "Measured C_ℓ vs null expectation from 1,000 random shuffles. The dipole (ℓ=1) is elevated at 2.75σ and ℓ=5 at 2.46σ, while intermediate multipoles are consistent with null. Error bars from bootstrap resampling.",
        "source": "Paper 4, Figure 8"
      },
      {
        "src": "/public/images/chirality/fig_hemisphere.png",
        "alt": "Hemisphere Asymmetry (3.05 sigma)",
        "number": "Figure 37",
        "title": "Hemisphere Asymmetry (3.05σ)",
        "desc": "Galactic north vs south CW fraction with bootstrap distribution. The north–south asymmetry reaches 3.05σ significance, the strongest single-statistic signal in the catalog. Inset shows the bootstrap null distribution with observed value marked.",
        "source": "Paper 4, Figure 9"
      },
      {
        "src": "/public/images/chirality/fig_sky_regions.png",
        "alt": "CW Fraction: Raw vs Equivariant by Sky Region",
        "number": "Figure 38",
        "title": "CW Fraction: Raw vs Equivariant by Sky Region",
        "desc": "Two-panel comparison showing dramatic bias reduction from equivariant averaging. Raw predictions show large region-to-region variation (survey systematics); equivariant predictions collapse to near-uniform CW fraction across all sky regions.",
        "source": "Paper 4, Figure 10"
      },
      {
        "src": "/public/images/chirality/fig_confidence_dist.png",
        "alt": "Classification Confidence Distribution",
        "number": "Figure 39",
        "title": "Classification Confidence Distribution",
        "desc": "Three-class confidence distribution (CW, CCW, NOT_SPIRAL) with CW fraction vs confidence inset. High-confidence classifications (>0.9) show stable CW/CCW balance, confirming the classifier is not introducing artificial asymmetry at any confidence threshold.",
        "source": "Paper 4, Figure 6"
      },
      {
        "src": "/public/images/chirality/fig_spiral_density.png",
        "alt": "Galaxy Density Map",
        "number": "Figure 40",
        "title": "Galaxy Density Map",
        "desc": "Survey footprint showing where spiral galaxies are observed, reflecting the Galaxy Zoo DECaLS sky coverage. Density variations trace the survey geometry and depth, which equivariant averaging is designed to correct for.",
        "source": "Paper 4, Figure 1"
      },
      {
        "src": "/public/images/chirality/fig_cw_fraction_heatmap.png",
        "alt": "CW Fraction Heatmap (RA vs DEC)",
        "number": "Figure 41",
        "title": "CW Fraction Heatmap (RA vs DEC)",
        "desc": "2D spatial distribution of chirality balance in RA–DEC coordinates. Color encodes the local CW fraction, revealing spatial structure in the chirality signal after equivariant correction.",
        "source": "Paper 4"
      },
      {
        "src": "/public/images/chirality/fig_class_pie.png",
        "alt": "Classification Breakdown",
        "number": "Figure 42",
        "title": "Classification Breakdown",
        "desc": "CW/CCW/NOT_SPIRAL donut chart showing the three-class distribution across the full catalog. The near-equal CW and CCW fractions confirm no global classification bias; NOT_SPIRAL objects are excluded from asymmetry analyses.",
        "source": "Paper 4, Figure 5"
      },
      {
        "src": "/public/images/chirality/fig_gallery_cw.png",
        "alt": "High-Confidence Clockwise Spirals",
        "number": "Figure 43",
        "title": "High-Confidence Clockwise Spirals",
        "desc": "4×4 grid of real galaxy images classified as clockwise with high confidence (>0.95). These examples demonstrate clear visual spiral arm winding direction consistent with the CW label.",
        "source": "Paper 4, Figure 2"
      },
      {
        "src": "/public/images/chirality/fig_gallery_ccw.png",
        "alt": "High-Confidence Counter-Clockwise Spirals",
        "number": "Figure 44",
        "title": "High-Confidence Counter-Clockwise Spirals",
        "desc": "4×4 grid of real galaxy images classified as counter-clockwise with high confidence (>0.95). Mirror-image counterparts to the CW gallery, confirming the classifier distinguishes winding direction rather than other morphological features.",
        "source": "Paper 4, Figure 3"
      },
      {
        "src": "/public/images/chirality/fig_gallery_notspi.png",
        "alt": "NOT_SPIRAL Classifications",
        "number": "Figure 45",
        "title": "NOT_SPIRAL Classifications",
        "desc": "Representative sample of objects classified as NOT_SPIRAL: ellipticals, mergers, edge-on disks, and other morphologies where spiral arm winding direction cannot be determined. These are excluded from chirality analyses.",
        "source": "Paper 4"
      },
      {
        "src": "/public/images/chirality/fig_equivariance_demo.png",
        "alt": "Equivariant Averaging Demonstration",
        "number": "Figure 46",
        "title": "Equivariant Averaging Demonstration",
        "desc": "Original vs horizontally flipped predictions for the same galaxy. Equivariant averaging takes the mean of original and mirror-flipped classifications, ensuring that any systematic preference the CNN has for one orientation is exactly cancelled. This is the methodological foundation of the catalog.",
        "source": "Paper 4, Figure 4"
      }
    ]
  },
  {
    "title": "Paper 2 — fNL Forecast",
    "count": "17 figures",
    "items": [
      {
        "src": "/public/images/quintom_fnl_verification.png",
        "alt": "Numerical verification that f_NL equals -35/8 is identical across three bounce mechanisms: pure dust contraction, quintom bounce, and asymmetric Papanikolaou bounce, confirming mechanism independence",
        "number": "Figure 47",
        "title": "fNL = −35/8 Mechanism Independence",
        "desc": "Numerical verification that fNL = −35/8 is identical across three bounce mechanisms: pure dust contraction, quintom bounce (H = &Upsilon;t), and asymmetric Papanikolaou bounce (w: 0&rarr;1/3). The bispectrum is determined by contraction-phase dynamics, not the bounce UV completion.",
        "source": "Literature Audit (2026-03-25)"
      },
      {
        "src": "/public/images/fnl_pbh_regulation.png",
        "alt": "PBH abundance f_PBH versus perturbation amplitude sigma for f_NL values of 0, -35/8, +4.375, and +10, showing how negative matter-bounce f_NL naturally suppresses primordial black hole overproduction without fine-tuning",
        "number": "Figure 48",
        "title": "fNL = −35/8 as PBH Regulator",
        "desc": "Negative fNL from the matter bounce naturally suppresses PBH overproduction. Left: PBH abundance fPBH vs perturbation amplitude σ for fNL = 0, −35/8, +4.375, +10. Right: the non-Gaussian PDF tail cutoff. The matter bounce value keeps fPBH ∈ [10−3, 1] without fine-tuning — a unique advantage over inflationary PBH models.",
        "source": "Literature Audit (2026-03-25)"
      },
      {
        "src": "/public/images/nanograv_bounce_consistency.png",
        "alt": "Matter-bounce induced gravitational wave spectrum with universal f-squared infrared scaling gamma=3.0, shown consistent with NANOGrav 15-year data gamma=3.20 plus or minus 0.42 at 0.48 sigma while SMBH binary prediction gamma=13/3 is excluded at 2 sigma",
        "number": "Figure 49",
        "title": "NANOGrav Consistency with Matter Bounce",
        "desc": "The matter-bounce induced GW spectrum has universal f2 infrared scaling (γ = 3), consistent with NANOGrav 15-year data (γ = 3.20 ± 0.42) at 0.48σ. SMBH binary mergers predict γ = 13/3 (≥2σ tension). The bounce prediction is strongly constrained.",
        "source": "Literature Audit (2026-03-25)"
      },
      {
        "src": "/public/images/nanograv_proper_fit.png",
        "alt": "Four-panel template fit of NANOGrav 15-year free-spectrum data showing matter bounce gamma=3.0 preferred 302-to-1 over SMBH mergers and 81000-to-1 over cosmic strings, with characteristic strain, residuals, Omega_GW, and comparison table",
        "number": "Figure 50",
        "title": "NANOGrav Proper Spectral Fit",
        "desc": "Template fit of NANOGrav 15yr free-spectrum data. Matter bounce (γ=3.0) preferred 302:1 over SMBH mergers (γ=13/3) and 81,000:1 over cosmic strings (γ=5/3). 4-panel: hc(f), residuals, ΩGW, comparison table. Caveat: synthetic data from published power-law, not raw free-spectrum posteriors.",
        "source": "NANOGrav Fit (2026-03-26)"
      },
      {
        "src": "/public/images/enhanced_18m_first_batch.png",
        "alt": "Analysis of first 500K spectra from the 173-column enhanced DESI DR1 catalog showing galaxies 19x more anomalous than QSOs (0.76% vs 0.04%), no score-vs-SNR correlation, and anomaly peak at redshift z~0.3-0.5",
        "number": "Figure 51",
        "title": "Enhanced 22.5M Catalog — First Batch Analysis",
        "desc": "First 500K spectra from the 173-column enhanced DESI DR1 catalog. Key finding: galaxies are 19× more likely to be anomalous than QSOs (0.76% vs 0.04%). Score vs S/N shows no correlation (anomalies are NOT noise artifacts). Anomalies peak at z&sim;0.3–0.5.",
        "source": "Enhanced 22.5M Catalog (2026-03-26)"
      },
      {
        "src": "/public/images/fig1_shape_function.png",
        "alt": "Complete bispectrum shape function S(k1,k2,k3) for matter contraction showing squeezed limit f_NL=-35/8 and equilateral and folded special cases for the matter-bounce primordial non-Gaussianity prediction",
        "number": "Figure 23",
        "title": "Matter-Bounce Bispectrum Shape Function",
        "desc": "The complete bispectrum shape S(k_1,k_2,k_3) for matter contraction, showing squeezed limit f_NL = -35/8 and equilateral/folded special cases.",
        "source": "Paper 2"
      },
      {
        "src": "/public/images/fig2_survey_comparison.png",
        "alt": "Detection significance for f_NL=-35/8 across survey configurations with GR marginalization bands, comparing SPHEREx 3-5 sigma realistic to MegaMapper ~7.5 sigma reach",
        "number": "Figure 24",
        "title": "SPHEREx vs MegaMapper Forecast Comparison",
        "desc": "Detection significance for f_NL = -35/8 across survey configurations, with GR marginalization bands. SPHEREx: 3–5σ realistic; MegaMapper: ~7.5σ.",
        "source": "Paper 2"
      },
      {
        "src": "/public/images/fig3_kmin_cliff.png",
        "alt": "Plot of f_NL detection significance versus minimum measurable wavenumber k_min showing the sensitivity cliff as ultra-large-scale modes are removed from the analysis",
        "number": "Figure 25",
        "title": "k_min Sensitivity Cliff",
        "desc": "How detection significance depends on the minimum measurable wavenumber, showing the critical role of ultra-large-scale modes.",
        "source": "Paper 2"
      },
      {
        "src": "/public/images/fig4_decision_thresholds.png",
        "alt": "Monte Carlo Bayes factor distributions for bounce versus inflation at various f_NL values showing Bayes factor 8-17 versus multifield competitors",
        "number": "Figure 26",
        "title": "Bayesian Decision Thresholds",
        "desc": "Monte Carlo Bayes factor distributions: bounce vs inflation at various f_NL values. Bayes factor ~8-17 vs multifield competitors (prior-dependent).",
        "source": "Paper 2"
      },
      {
        "src": "/public/images/fig5_inflation_comparison.png",
        "alt": "Parameter space comparison showing negative order-1 f_NL is natural for matter bounce but requires fine-tuning for inflation, demonstrating the anti-mimicry property of the matter-bounce bispectrum prediction",
        "number": "Figure 27",
        "title": "Matter Bounce vs Inflation Anti-Mimicry",
        "desc": "Parameter space comparison showing why negative O(1) f_NL is natural for bounce but requires fine-tuning for inflation.",
        "source": "Paper 2"
      },
      {
        "src": "/public/images/fig_bnl_shape_slices.png",
        "alt": "Matter-bounce B_NL versus local template across triangle configurations: squeezed series converging to -35/8 and isosceles series showing 63% variation from folded (-2.25) to equilateral (-3.98), with shaded region showing signal lost by a local estimator",
        "number": "Figure 28",
        "title": "B_NL Shape Slices",
        "desc": "Matter-bounce B_NL vs local template across triangle configurations. Left: squeezed series showing convergence to -35/8. Right: isosceles series showing 63% variation from folded (-2.25) to equilateral (-3.98). The local template is constant at -35/8 for all configurations — the shaded area represents signal lost by a local estimator.",
        "source": "Paper 2 — Template Mismatch"
      },
      {
        "src": "/public/images/fig_template_overlap_robustness.png",
        "alt": "Amplitude recovery factor r across 10 physically motivated weighting schemes using the physics-derived full-commutator polynomial, showing CMB Fisher r=0.90 and LSS r=0.85, with gray bars for adversarial extreme cuts",
        "number": "Figure 29",
        "title": "Template Overlap Robustness",
        "desc": "Amplitude recovery factor r across 10 physically motivated weighting schemes, using the physics-derived full-commutator polynomial (6,2,−18,10,−66,18). With the true polynomial: CMB Fisher r = 0.90, LSS/SDB r = 0.85, giving r ≈ 0.85–0.90. Mismatch is intrinsic to the bounce shape. Gray bars show adversarial extreme cuts.",
        "source": "Paper 2 — Template Mismatch"
      },
      {
        "src": "/public/images/fig_forecast_template_corrected.png",
        "alt": "Two-panel forecast: left shows detection significance with and without template mismatch correction for f_NL=-35/8, SPHEREx dropping from 6.2 sigma naive to 3-5 sigma realistic; right shows normalization sensitivity if -35/16 is correct",
        "number": "Figure 30",
        "title": "Forecast Significance Comparison",
        "desc": "Left: Detection significance with and without template mismatch correction (canonical f_NL = -35/8). SPHEREx drops from 6.2σ naive to 3–5σ realistic. Right: Normalization sensitivity — if -35/16 is correct, SPHEREx drops further to 2.7σ. Template correction matters more for the MegaMapper SDB channel.",
        "source": "Paper 2 — Forecasts"
      },
      {
        "src": "/public/images/fig_true_vs_fitted_polynomial.png",
        "alt": "Comparison of matter-bounce B_NL shape using physics-derived polynomial (6,2,-18,10,-66,18) versus 3-benchmark fit showing isosceles and squeezed series with both converging to f_NL=-35/8 in the squeezed limit",
        "number": "Figure 31",
        "title": "True vs Fitted Polynomial Shape",
        "desc": "Matter-bounce B_NL shape: physics-derived polynomial (6,2,−18,10,−66,18) vs 3-benchmark fit (2,7,3,−12,−69,19). Left: isosceles series showing the true polynomial stays closer to the local template at intermediate configurations. Right: squeezed series showing both converge to -35/8. The physics-derived polynomial gives a less severe template mismatch (r ≈ 0.85--0.90 vs r ≈ 0.84).",
        "source": "Paper 2 — True Polynomial"
      },
      {
        "src": "/public/images/fig_namaster_beta_vs_nside.png",
        "alt": "Cosmic birefringence angle beta measured from Planck SMICA using NaMaster with B-mode purification at increasing NSIDE resolution, showing NSIDE=1024 beta=0.19 plus or minus 0.03 degrees as lead result with bounce ALP prediction at beta=0.27 degrees",
        "number": "Figure 32",
        "title": "NaMaster β vs NSIDE",
        "desc": "Cosmic birefringence β measured from Planck SMICA using NaMaster with B-mode purification at increasing resolution. NSIDE=1024 (β = 0.19 \\pm 0.03°) is the lead result. At NSIDE=2048, β drops to 0.07 \\pm 0.02°, suggesting high-ℓ contamination or noise. Green circle marks the preferred NSIDE=1024 result. Blue band shows the published Planck+ACT measurement. Red dashed line is our ALP prediction.",
        "source": "Paper 2 — Birefringence"
      },
      {
        "src": "/public/images/fig_forecast_true_polynomial.png",
        "alt": "Detection significance for f_NL=-35/8 using physics-derived polynomial with r=0.88 template overlap, showing SPHEREx dropping from 6.2 sigma naive to 3-5 sigma realistic and MegaMapper dropping from 8.8 sigma to ~7.7 sigma after template correction",
        "number": "Figure 33",
        "title": "Updated Forecast with True Polynomial",
        "desc": "Detection significance for f_NL = -35/8 using the physics-derived polynomial (r = 0.88). Template correction reduces SPHEREx from 6.2σ naive to 3–5σ realistic. MegaMapper drops from 8.8σ to ~7.7σ.",
        "source": "Paper 2 — Forecasts"
      }
    ]
  },
  {
    "title": "Paper 1 — ALP Birefringence + MCMC Corner",
    "count": "3 figures",
    "items": [
      {
        "src": "/public/images/paper1_corner_full_tension.png",
        "alt": "Full-tension MCMC corner plot from 119,617 post-burnin samples over H0, Omega_m, sigma8, S8, and Delta N_eff using getdist, showing H0=67.69 plus or minus 1.06 and Delta N_eff consistent with zero",
        "number": "Figure 22 (new, 2026-04-17)",
        "title": "Full-Tension MCMC Corner Plot (H0, Ωm, σ8, S8, ΔNeff)",
        "desc": "Joint posterior over the Planck+BAO+SN+H0+S8 full-tension combination from 119,617 post-burnin MCMC samples via getdist. Marginal results: H0=67.69±1.06, Ωm=0.308±0.006, σ8=0.803±0.008, S8=0.814±0.009, ΔNeff=−0.019±0.169 — consistent with zero, confirming the framework's compatibility with standard cosmology.",
        "source": "Paper 1, &sect;IV — Fig. corner_full_tension"
      },
      {
        "src": "/arxiv_v2/figures/beta_comparison_all_models.png",
        "alt": "Cosmic birefringence angle beta compared across multiple spin-torsion model variants and competing frameworks, with bounce ALP prediction beta=0.27 degrees compared to the observed ACT measurement of 0.342 degrees",
        "number": "Figure 20",
        "title": "β Comparison Across Models",
        "desc": "Cosmic birefringence angle β compared across multiple spin-torsion model variants and competing frameworks, showing the predicted signal range.",
        "source": "Paper 1"
      },
      {
        "src": "/arxiv_v2/figures/triangle_plot.png",
        "alt": "Updated v2 parameter corner plot showing refined cosmological parameter constraints and posterior distributions from additional dataset combinations in the ALP birefringence analysis",
        "number": "Figure 21",
        "title": "Parameter Triangle Plot (v2)",
        "desc": "Updated corner plot from the v2 analysis with refined parameter constraints and additional dataset combinations.",
        "source": "Paper 1"
      }
    ]
  },
  {
    "title": "Paper 1 — Framework Figures",
    "count": "9 figures",
    "items": [
      {
        "src": "/public/images/figure1_lqg_holst_derivation_enhanced.png",
        "alt": "Derivation chain from Planck scale through one-loop parity-odd operator and inflationary suppression to observed dark energy scale rho_Lambda approximately (2.3 meV)^4, showing the energy density hierarchy for spin-torsion cosmology",
        "number": "Figure 1",
        "title": "Energy Density Hierarchy",
        "desc": "Shows the derivation chain from Planck scale through one-loop parity-odd operator, inflationary suppression, to observed dark energy scale ρ_Λ ≈ (2.3 meV)^4.",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure2_galaxy_spin_comprehensive.png",
        "alt": "Galaxy spin dipole amplitude across SDSS DR7, Pan-STARRS, HST Deep, and Longo 2011 surveys with hierarchical Bayesian fit, showing a contested anomaly in the literature",
        "number": "Figure 2",
        "title": "Galaxy Spin Dipole Data",
        "desc": "Dipole amplitude across SDSS DR7, Pan-STARRS, HST Deep, and Longo (2011) with hierarchical Bayesian fit. Status: contested anomaly.",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure_3a_tension_resolution.png",
        "alt": "Spin-torsion model H0 and sigma_8 position between Planck and SH0ES/KiDS measurements. Historical figure: tension reduction was later shown to be SH0ES-prior-driven and not an intrinsic model prediction.",
        "number": "Figure 3a",
        "title": "Hubble & σ_8 Tension Resolution",
        "desc": "Shows spin-torsion model position between Planck and SH0ES/KiDS measurements. Note: tension reduction was disproved by independent MCMC. [Historical: tension reduction was later shown to be SH0ES-prior-driven]",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure3b_tensions_resolution_comprehensive.png",
        "alt": "H0 and sigma_8/S8 measurements from 9 or more probes with spin-torsion model position overlaid. Historical figure: tension reduction was later shown to be SH0ES-prior-driven.",
        "number": "Figure 3b",
        "title": "Comprehensive Tension Comparison",
        "desc": "H_0 and σ_8/S_8 measurements from 9+ probes with spin-torsion model position overlaid for direct comparison. [Historical: tension reduction was later shown to be SH0ES-prior-driven]",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure4_distance_impact.png",
        "alt": "Luminosity and angular diameter distance deviations from Lambda-CDM at the ~2% level showing observational signatures of geometric dark energy from rotation-induced effective cosmological constant",
        "number": "Figure 4",
        "title": "Distance Impact of Rotation-Induced Λ_eff",
        "desc": "Luminosity and angular diameter distance deviations from ΛCDM at the ~2% level, showing observational signatures of geometric dark energy.",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure5_rotation_expansion.png",
        "alt": "H(z) expansion rate comparison showing the spin-torsion rotation contribution is negligibly small (less than 10^-20), confirming the model is expansion-equivalent to Lambda-CDM",
        "number": "Figure 5",
        "title": "Rotation Component Effect on Expansion",
        "desc": "H(z) comparison showing the rotation contribution is negligibly small (< 10^{-20}), confirming the model is expansion-equivalent to ΛCDM.",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure6_parameter_naturalness.png",
        "alt": "Log-scale fine-tuning comparison: Lambda-CDM (10^120), Quintessence (10^60), f(R) gravity (10^40), Spin-Torsion (10^5 illustrative, reparameterized not solved)",
        "number": "Figure 6",
        "title": "Fine-Tuning Comparison",
        "desc": "Log-scale fine-tuning: ΛCDM (10^{120}), Quintessence (10^{60}), f(R) (10^{40}), Spin-Torsion (10^5). Note: 10^5 is illustrative. [Note: 105 figure is reparameterized, not solved]",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure7_observational_timeline.png",
        "alt": "Timeline of key experimental milestones for testing spin-torsion cosmology: SPHEREx, CMB-S4 (2029), LSST (2030), and LiteBIRD (early 2030s JAXA JFY2032)",
        "number": "Figure 7",
        "title": "Observational Timeline",
        "desc": "Key experimental milestones for testing the spin-torsion model: LiteBIRD (early 2030s, JAXA JFY2032), CMB-S4 (2029), LSST (2030), and SPHEREx.",
        "source": "Paper 1"
      },
      {
        "src": "/public/images/figure8_detection_forecast.png",
        "alt": "Combined detection significance projections across multiple observational probes showing cumulative constraining power for the spin-torsion cosmology model over the next decade",
        "number": "Figure 8",
        "title": "Detection Forecast Sensitivity",
        "desc": "Combined detection significance projections across multiple observational probes, showing cumulative constraining power over the next decade.",
        "source": "Paper 1"
      }
    ]
  },
  {
    "title": "Paper 1 — MCMC Verification",
    "count": "6 figures",
    "items": [
      {
        "src": "/paper/figures/full_tension_triangle.png",
        "alt": "Corner plot with 2D posterior contours for all primary cosmological parameters from the full-tension MCMC analysis with 176,840 samples, showing parameter degeneracy structure",
        "number": "Figure 10",
        "title": "Full-Tension Triangle Plot",
        "desc": "Corner plot showing 2D posterior contours for all primary cosmological parameters from the full-tension MCMC analysis with 176,840 samples.",
        "source": "Paper 1 — MCMC"
      },
      {
        "src": "/paper/figures/full_tension_posteriors.png",
        "alt": "1D marginalized posterior distributions for key cosmological parameters H0, Omega_b h^2, Omega_c h^2, and Delta N_eff from full-tension MCMC, showing all parameters consistent with standard cosmology",
        "number": "Figure 11",
        "title": "Full-Tension Posteriors",
        "desc": "1D marginalized posterior distributions for key cosmological parameters including H_0, Ω_b h^2, Ω_c h^2, and Δ N_eff.",
        "source": "Paper 1 — MCMC"
      },
      {
        "src": "/paper/figures/dneff_posterior_full_tension.png",
        "alt": "Posterior distribution for dark radiation parameter Delta N_eff from the full-tension dataset combination, with spin-torsion prediction overlaid, showing consistency with zero within 1 sigma",
        "number": "Figure 12",
        "title": "Δ N_eff Posterior (Full-Tension)",
        "desc": "Posterior distribution for the dark radiation parameter Δ N_eff, with the spin-torsion prediction overlaid. Consistent with zero within 1σ.",
        "source": "Paper 1 — MCMC"
      },
      {
        "src": "/paper/figures/full_tension_final_convergence.png",
        "alt": "Chain convergence traces and R-hat evolution across MCMC iterations confirming R-hat minus 1 less than 0.005 for all parameters, demonstrating full convergence of the full-tension analysis",
        "number": "Figure 13",
        "title": "MCMC Convergence Diagnostics",
        "desc": "Chain convergence traces and R̂ evolution across iterations, confirming R̂ - 1 < 0.005 for all parameters.",
        "source": "Paper 1 — MCMC"
      },
      {
        "src": "/paper/figures/full_tension_final_correlation.png",
        "alt": "Pearson correlation coefficient matrix between all sampled cosmological parameters revealing the degeneracy structure of the spin-torsion model from the full-tension MCMC",
        "number": "Figure 14",
        "title": "Parameter Correlation Matrix",
        "desc": "Pearson correlation coefficients between all sampled cosmological parameters, revealing the degeneracy structure of the spin-torsion model.",
        "source": "Paper 1 — MCMC"
      },
      {
        "src": "/paper/figures/full_tension_final_ess_growth.png",
        "alt": "Effective sample size ESS accumulation across chain iterations demonstrating sufficient independent samples for reliable posterior estimation in the full-tension MCMC analysis",
        "number": "Figure 15",
        "title": "Effective Sample Size Growth",
        "desc": "ESS accumulation across chain iterations, demonstrating sufficient independent samples for reliable posterior estimation.",
        "source": "Paper 1 — MCMC"
      }
    ]
  },
  {
    "title": "Paper 1 — Dataset Comparisons",
    "count": "4 figures",
    "items": [
      {
        "src": "/paper/figures/cosmology_dataset_comparison_two_frozen.png",
        "alt": "H0, Delta N_eff, and S8 posteriors compared across three frozen dataset combinations: Planck+BAO, Planck+BAO+SN, and Full-Tension, showing consistent Delta N_eff approximately zero",
        "number": "Figure 16",
        "title": "Cross-Dataset Comparison",
        "desc": "H_0, Δ N_eff, and S_8 posteriors compared across frozen dataset combinations (Planck+BAO, Planck+BAO+SN, Full-Tension).",
        "source": "Paper 1 — Analysis"
      },
      {
        "src": "/paper/figures/fig_dneff_viability_two_frozen.png",
        "alt": "Delta N_eff posterior distributions from both frozen datasets (Planck+BAO and Planck+BAO+SN) showing both are consistent with Delta N_eff=0 at high significance",
        "number": "Figure 17",
        "title": "Δ N_eff Viability",
        "desc": "Posterior distributions from both frozen datasets, demonstrating that both are consistent with Δ N_eff = 0 at high significance.",
        "source": "Paper 1 — Analysis"
      },
      {
        "src": "/paper/figures/vacuum_scale_sensitivity.png",
        "alt": "Four-panel Monte Carlo analysis showing vacuum scale distribution, N_tot sensitivity, viable fraction of parameter space, and Spearman rank correlations for the spin-torsion framework",
        "number": "Figure 18",
        "title": "Vacuum Scale Sensitivity",
        "desc": "4-panel Monte Carlo analysis: vacuum scale distribution, N_tot sensitivity, viable fraction of parameter space, and Spearman rank correlations.",
        "source": "Paper 1 — Analysis"
      },
      {
        "src": "/paper/figures/pk_feature_window_analysis.png",
        "alt": "Analysis of potential spectral features in the matter power spectrum that could distinguish spin-torsion cosmology from vanilla Lambda-CDM using window function techniques",
        "number": "Figure 19",
        "title": "Power Spectrum Feature Window",
        "desc": "Analysis of potential spectral features in the matter power spectrum that could distinguish spin-torsion cosmology from vanilla ΛCDM.",
        "source": "Paper 1 — Analysis"
      }
    ]
  },
  {
    "title": "Cross-Cutting — Research Program",
    "count": "1 figure",
    "items": [
      {
        "src": "/articles/images/spin_torsion_mindmap.png",
        "alt": "BigBounce research program mind map showing relationships between theoretical foundations, observational tests, and publication milestones",
        "number": "Program Overview",
        "title": "Research Program Mind Map",
        "desc": "Full architecture of the BigBounce research program, mapping the relationships between theoretical foundations, observational tests, and publication milestones.",
        "source": "Research Program"
      }
    ]
  }
];

export const allFigures: Figure[] = figureSections.flatMap((s) => s.items);
