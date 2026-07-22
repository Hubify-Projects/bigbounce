// AUTO-GENERATED from Convex paper_figures by
// site/scripts/extract-figures-from-convex.mjs — do not edit by hand.
// Source of truth: each paper's current .tex \includegraphics + \caption.
// Re-seed Convex with: node tools/seed_paper_figures.mjs
// Regenerate this snapshot with: cd site && node scripts/extract-figures-from-convex.mjs

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
    "title": "Paper 1B — Technical Verification Companion (MCMC + NaMaster)",
    "count": "6 figures",
    "items": [
      {
        "src": "/images/paper1_corner_full_tension.png",
        "alt": "Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw",
        "number": "Figure 1 (fig:corner_full_tension)",
        "title": "Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw",
        "desc": "Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote ) over Planck+BAO+SN+H0+S_8. The _eff posterior is consistent with zero (-0.020± 0.169), confirming no additional relativistic species at recombination.",
        "source": "Paper 1B · v2B.0.12"
      },
      {
        "src": "/images/fig_dneff_viability_two_frozen.png",
        "alt": "_eff marginal posterior comparison across the two frozen dataset combinations of Table (176,240 and 132,949 s…",
        "number": "Figure 2 (fig:dneff_viability)",
        "title": "_eff marginal posterior comparison across the two frozen dataset combinations of Table (176,240 and 132,949 s…",
        "desc": "_eff marginal posterior comparison across the two frozen dataset combinations of Table (176,240 and 132,949 samples). Panel (a): Gaussian summaries of the _eff marginal posteriors at the Table means ±1σ, with the Standard-Model value _eff=0 marked. Panel (b): all seven Table parameters, normalized to the full-tension mean and σ. Both combinations recover _e…",
        "source": "Paper 1B · v2B.0.12"
      },
      {
        "src": "/images/alp_triangle_plot.png",
        "alt": "Spectator-ALP joint posterior triangle from the continuous-prior cross-check configuration in which the photo…",
        "number": "Figure 3 (fig:alp_triangle)",
        "title": "Spectator-ALP joint posterior triangle from the continuous-prior cross-check configuration in which the photo…",
        "desc": "Spectator-ALP joint posterior triangle from the continuous-prior cross-check configuration in which the photon anomaly coefficient is sampled freely (flat priors C_a[4,60] --- shifted and extended from the earlier [1,30] to cover the posterior-supported coupling band (median 20.7, 16--84\\% [7.3,45.6]); the dropped [1,4) interval lies entirely below the mini…",
        "source": "Paper 1B · v2B.0.12"
      },
      {
        "src": "/images/fig_namaster_beta_vs_nside.png",
        "alt": "NaMaster β recovery vs HEALPix NSIDE",
        "number": "Figure 101",
        "title": "NaMaster β recovery vs NSIDE",
        "desc": "Historical effective-ell NSIDE diagnostic retained for provenance. Its apparent −0.032° recovery floor is superseded by the v1B.0.108 exact-bandpower-window operator, which recovers +0.269° from +0.270° (bias −0.001°) on a synthetic native-coordinate latitude window. Neither result is a sky-detection significance.",
        "source": "Paper 1B · historical diagnostic; superseded by v1B.0.108"
      },
      {
        "src": "/images/dneff_viability.png",
        "alt": "ΔN_eff posterior viability across three frozen dataset combinations",
        "number": "Figure 102",
        "title": "ΔN_eff posterior — three frozen runs",
        "desc": "Joint 1D + 2D ΔN_eff posterior across the full-tension (Planck+SH0ES), Planck+BAO+SN, and Planck-only frozen MCMC chains. The 309,189-sample evidence anchors the §IV ΔN_eff ≈ 0 null-consistency conclusion.",
        "source": "Paper 1B · v1B.0.51"
      },
      {
        "src": "/images/fig_dneff_viability_two_frozen.png",
        "alt": "ΔN_eff viability — two-chain comparison",
        "number": "Figure 103",
        "title": "ΔN_eff two-chain overlay",
        "desc": "Overlay of the two converged frozen chains (full-tension + Planck+BAO+SN) showing how the H_0 — ΔN_eff degeneracy direction differs by dataset. Useful for showing the inverse-variance combination assumption discussion.",
        "source": "Paper 1B · v1B.0.51"
      }
    ]
  },
  {
    "title": "Paper 2 — Matter-Bounce f_NL SPHEREx Forecast",
    "count": "5 figures",
    "items": [
      {
        "src": "/images/fig1_shape_function.png",
        "alt": "Exact four-vertex matter-bounce shape B_NL(k_L,k_S,k_S) as a function of squeeze ratio",
        "number": "Figure 1 (fig:shape)",
        "title": "Exact four-vertex matter-bounce shape B_NL(k_L,k_S,k_S) as a function of squeeze ratio",
        "desc": "Exact four-vertex matter-bounce shape B_NL(k_L,k_S,k_S) as a function of squeeze ratio. The curve is evaluated directly from Eq. and approaches -35/16; the marker identifies the equilateral value -255/128.",
        "source": "Paper 2 · v1.7.126"
      },
      {
        "src": "/images/fig5_inflation_comparison.png",
        "alt": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The blue bar is the imported SPHEREx local-temp…",
        "number": "Figure 2 (fig:inflation)",
        "title": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The blue bar is the imported SPHEREx local-temp…",
        "desc": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The blue bar is the imported SPHEREx local-template uncertainty transformed to bounce-amplitude coordinates by Eq. : σ(f_NL^ bounce)=0.7/0.84=0.83, centered on -35/16. It is not the separate shape-matched surrogate-covariance uncertainty.",
        "source": "Paper 2 · v1.7.126"
      },
      {
        "src": "/images/fig_4vertex_sum.png",
        "alt": "Four-vertex amplitude diagram for spectator-ALP × matter-bounce coupling",
        "number": "Figure 101",
        "title": "4-vertex amplitude sum",
        "desc": "Tree-level vertex sum for the spectator-ALP × matter-bounce coupling channels. Diagrammatic intuition for the f_a cancellation in the rotation amplitude β.",
        "source": "Paper 2 · v1.7.45"
      },
      {
        "src": "/images/alp_beta_comparison.png",
        "alt": "Spectator-ALP β comparison vs Eskilt+ data",
        "number": "Figure 102",
        "title": "ALP β vs Eskilt+2022",
        "desc": "Spectator-ALP β = 0.342° ± 0.094° posterior overlay vs the published joint Planck+ACT Eskilt+2022 measurement. Visualizes the consistency check anchored at f_a = M_Pl, m = H_0.",
        "source": "Paper 2 · v1.7.45"
      },
      {
        "src": "/images/alp_triangle_plot.png",
        "alt": "Spectator-ALP MCMC triangle posterior",
        "number": "Figure 103",
        "title": "ALP MCMC triangle",
        "desc": "Triangle plot for the (θ_i, m_θ, C_aγ, β) posterior on the spectator-ALP joint chain. Shows the parameter degeneracies + the natural-prior box boundary discussion.",
        "source": "Paper 2 · v1.7.45"
      }
    ]
  },
  {
    "title": "Paper 3 — DESI Spectral Anomalies (Multi-Survey Catalog)",
    "count": "24 figures",
    "items": [
      {
        "src": "/images/umap_by_anomaly_score.png",
        "alt": "2D UMAP embedding of the encoder latent space (PCA 12830, then UMAP) for a 500,000-spectrum stratified DESI D…",
        "number": "Figure 1 (fig:umap_score)",
        "title": "2D UMAP embedding of the encoder latent space (PCA 12830, then UMAP) for a 500,000-spectrum stratified DESI D…",
        "desc": "2D UMAP embedding of the encoder latent space (PCA 12830, then UMAP) for a 500,000-spectrum stratified DESI DR1 sample, colored by per-spectrum anomaly score. High-score anomalies concentrate in distinct islands of the embedding (bright lobe, lower right) rather than scattering through the bulk population; the 83 Exemplar-Set anomalies (cyan stars) lie on o…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_skymap_all_surveys.png",
        "alt": "Cross-transfer baseline map (ACT DR6 excluded from science results)",
        "number": "Figure 2 (fig:skymap)",
        "title": "Cross-transfer baseline map (ACT DR6 excluded from science results)",
        "desc": "Cross-transfer baseline map (ACT DR6 excluded from science results). Mollweide projection in equatorial coordinates (RA/Dec, ICRS) of the initial cross-transfer anomaly baseline (319,443 detections; the canonical Path-C unique count of 377,482 is not a deduplication of this baseline --- deduplication only ever reduces its input --- but the 5'' dedup of the…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_score_distributions.png",
        "alt": "Anomaly score distributions for the three main spectroscopic surveys",
        "number": "Figure 3 (fig:score_dist)",
        "title": "Anomaly score distributions for the three main spectroscopic surveys",
        "desc": "Anomaly score distributions for the three main spectroscopic surveys. The score S is the per-spectrum reconstruction MSE rescaled to validation z-units: S = (MSE - _ val)/_ val, where _ val and _ val are the mean and standard deviation of MSE on the held-out 20\\% validation split of the per-survey training pool (; native for DESI, cross-transfer for SDSS an…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_sdss_umap.png",
        "alt": "Cross-transfer SDSS baseline",
        "number": "Figure 4 (fig:sdss_umap)",
        "title": "Cross-transfer SDSS baseline",
        "desc": "Cross-transfer SDSS baseline. UMAP embedding of the 77,905 SDSS DR18 anomalies from the initial DESI-trained cross-transfer scan, colored by HDBSCAN cluster (left) and by inferred physical category (right). The dominant cluster (green, 84\\% of objects) contains ultra-cool dwarfs (M7--T2) that are completely out-of-distribution for the DESI-trained --- the d…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_neowise_top_anomaly.png",
        "alt": "NEOWISE top infrared anomaly at (α, ) = (180",
        "number": "Figure 5 (fig:neowise_top)",
        "title": "NEOWISE top infrared anomaly at (α, ) = (180",
        "desc": "NEOWISE top infrared anomaly at (α, ) = (180.59^, 0.56^), score = 11.5. DESI Legacy Survey DR9 grz composite, 256 × 256 pixels at the native LS DR9 scale of 0.262''/px (256 × 0.262'' = 67'' per side). Extreme W1-W2 infrared color excess; no prior SIMBAD entry within 5''. The optical counterpart is a bright, saturated source with diffraction spikes indicativ…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_novelty_fractions.png",
        "alt": "SIMBAD-unmatched fractions for the five surveys with coordinate-based cross-matching, ranked from lowest (NEO…",
        "number": "Figure 6 (fig:novelty)",
        "title": "SIMBAD-unmatched fractions for the five surveys with coordinate-based cross-matching, ranked from lowest (NEO…",
        "desc": "SIMBAD-unmatched fractions for the five surveys with coordinate-based cross-matching, ranked from lowest (NEOWISE, 45\\%) to highest (DESI DR1, 99\\% of top-10K objects absent from SIMBAD). The dashed line marks the aggregate 58.8\\% SIMBAD-unmatched fraction (pooled over the top-100 anomalies of three surveys --- SDSS, eROSITA, NEOWISE; 235/400 at 3'', where…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/anomaly_sky_distribution.png",
        "alt": "Spatial distribution of the 195,829 DESI DR1 anomalies",
        "number": "Figure 7 (fig:anomaly_sky)",
        "title": "Spatial distribution of the 195,829 DESI DR1 anomalies",
        "desc": "Spatial distribution of the 195,829 DESI DR1 anomalies. Top left: equatorial sky map color-coded by anomaly score S. Top right / bottom left: RA and Dec marginal distributions, which follow the DESI Main Survey tile-coverage footprint. Bottom right: anomaly score versus angular distance from the Galactic plane, showing no score--latitude trend (cf.\\ the com…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_cross_survey_matches.png",
        "alt": "Spectral pairs for the three DESI × SDSS cross-survey matches",
        "number": "Figure 8 (fig:crossmatch)",
        "title": "Spectral pairs for the three DESI × SDSS cross-survey matches",
        "desc": "Spectral pairs for the three DESI × SDSS cross-survey matches. Left column: DESI DR1 spectrum; right column: same object in SDSS DR18. Black: observed flux (normalized); red dashed: reconstruction. (a, b) Known QSO at z ≈ 1.55: both surveys flag the object independently, with mutually consistent reconstructions and the lowest scores of the three matches ---…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_fnl_improvement.png",
        "alt": "Per-redshift-bin decomposition of the Fisher forecast under the fixed bias prior α = 0",
        "number": "Figure 9 (fig:fnl_improvement)",
        "title": "Per-redshift-bin decomposition of the Fisher forecast under the fixed bias prior α = 0",
        "desc": "Per-redshift-bin decomposition of the Fisher forecast under the fixed bias prior α = 0.15 (cf.\\ Appendix ); the primary forecast of this work uses the empirically measured bias of , which is consistent with no multi-tracer improvement. Per-redshift-bin decomposition of the fixed-α = 0.15 reference Fisher forecast (Appendix ). Left: σ(f_NL) per redshift bin…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_injection_recovery.png",
        "alt": "Injection-recovery gate results across the retained-survey spectroscopic tiers (SDSS, LAMOST), with the non-s…",
        "number": "Figure 10 (fig:injection_recovery)",
        "title": "Injection-recovery gate results across the retained-survey spectroscopic tiers (SDSS, LAMOST), with the non-s…",
        "desc": "Injection-recovery gate results across the retained-survey spectroscopic tiers (SDSS, LAMOST), with the non-spectral retrains (Planck CMB native convolutional autoencoder, NEOWISE ecliptic-pole mask, eROSITA latent-subspace) brought into the same axis for comparison; the removed Gaia DR3 tier is overplotted only as a historical methodological-record curve a…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/B11_sigma_fnl_vs_ndensity.png",
        "alt": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gra…",
        "number": "Figure 11 (fig:shotnoise_sensitivity)",
        "title": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gra…",
        "desc": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gray line marks the dense-tracer limit ( = 11.71); the dotted dark-red line marks the single-tracer baseline ( = 16.85). Vertical orange and goldenrod lines mark the gold ( n = 8.5× 10^-6) and silver ( n = 4.5× 10^-5) anomaly sub-samples. The Heinrich-\\…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/fig_gallery_top10.png",
        "alt": "Representative DESI DR1 anomalies across all ten taxonomy families",
        "number": "Figure 12 (fig:gallery_top10)",
        "title": "Representative DESI DR1 anomalies across all ten taxonomy families",
        "desc": "Representative DESI DR1 anomalies across all ten taxonomy families. One highest-scored member per family; 2-row × 5-column layout. Border color indicates taxonomy class. Images are DESI Legacy Survey DR9 grz composites. Panel sublabels give the object RA; the high-z QSO panel additionally gives the redshift and the per-arm Z-arm sub-score r_Z (). The taxono…",
        "source": "Paper 3 · v3.2.0-r11"
      },
      {
        "src": "/images/anomaly_sky_distribution.png",
        "alt": "All-sky distribution of P3 anomalies",
        "number": "Figure 101",
        "title": "Anomaly sky distribution",
        "desc": "Mollweide all-sky distribution of the 14,089 high-confidence DESI + cross-survey anomalies. Color-coded by anomaly score + class. Useful as a hero map alongside the §III architecture figure.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/photo_z_scatter.png",
        "alt": "Photometric redshift scatter for P3 anomaly catalog",
        "number": "Figure 102",
        "title": "Photo-z scatter",
        "desc": "Photo-z vs spectro-z scatter for the P3 anomaly catalog (DESI + cross-matched DR8 + UNIONS). Anchors the photo-z residual quality cut in §III.B.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/photo_z_residuals.png",
        "alt": "Photometric redshift residual distribution",
        "number": "Figure 103",
        "title": "Photo-z residuals",
        "desc": "Residual distribution (Δz / (1+z)) for the photo-z calibration sample. Used to justify the catastrophic-outlier cut at |Δz/(1+z)| > 0.15.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_fnl_improvement.png",
        "alt": "f_NL constraint improvement from P3 anomaly removal",
        "number": "Figure 104",
        "title": "f_NL improvement from anomaly removal",
        "desc": "σ(f_NL) improvement as a function of P3 anomaly-removal threshold. Quantifies the load-bearing claim that the catalog reduces f_NL contamination for SPHEREx-class surveys.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_nanograv_fit.png",
        "alt": "NanoGrav γ_GWB fit on the P3-cleaned sample",
        "number": "Figure 105",
        "title": "NanoGrav γ_GWB fit",
        "desc": "NanoGrav 15yr γ_GWB MAP fit after applying the P3 anomaly catalog to the host-galaxy environment. Anchors the §V γ = 3.0 cross-reference.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_pathc_neowise_ecliptic.png",
        "alt": "NEOWISE ecliptic distribution of Path-C anomalies",
        "number": "Figure 106",
        "title": "Path-C NEOWISE ecliptic",
        "desc": "Ecliptic-coordinate distribution of NEOWISE Path-C native-retrieval anomalies. Shows the residual ecliptic concentration after de-duplication — used to justify the §III.E ecliptic-systematic discussion.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/anomaly_rate_map.png",
        "alt": "Per-pixel anomaly rate map across all 6 surveys",
        "number": "Figure 107",
        "title": "Anomaly rate sky map",
        "desc": "Per-pixel anomaly rate (anomalies / spectra) across all 6 surveys. Visualizes the survey-depth × anomaly-rate correlation discussed in §III.D.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/survey_depth_map.png",
        "alt": "Survey depth (z_max) sky map",
        "number": "Figure 108",
        "title": "Survey depth map",
        "desc": "Per-pixel maximum-z reached by each survey in the P3 catalog. Companion to the anomaly-rate map for diagnosing systematic vs astrophysical anomalies.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/depth_vs_rate_scatter.png",
        "alt": "Survey depth vs anomaly rate scatter",
        "number": "Figure 109",
        "title": "Depth × rate scatter",
        "desc": "Scatter of per-pixel anomaly rate against survey depth. Quantitative anchor for the depth-coupling systematic discussion in §III.D.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/umap_by_anomaly_score.png",
        "alt": "UMAP embedding colored by anomaly score",
        "number": "Figure 110",
        "title": "UMAP × anomaly score",
        "desc": "2D UMAP embedding of the encoder latent space, colored by per-spectrum anomaly score. Hero figure for the §II.A representation-learning approach.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/umap_by_redshift.png",
        "alt": "UMAP embedding colored by redshift",
        "number": "Figure 111",
        "title": "UMAP × redshift",
        "desc": "Same UMAP embedding colored by spectroscopic redshift. Visualizes how the encoder organizes spectra by z without explicit redshift supervision.",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/umap_by_spectype.png",
        "alt": "UMAP embedding colored by spectral type",
        "number": "Figure 112",
        "title": "UMAP × spectral type",
        "desc": "Same UMAP embedding colored by DESI primary spectroscopic class (GALAXY/STAR/QSO). Shows native class separation in the unsupervised latent.",
        "source": "Paper 3 · v3.1.80"
      }
    ]
  },
  {
    "title": "Paper 4 — Galaxy Chirality Catalog (3.3M Spirals)",
    "count": "12 figures",
    "items": [
      {
        "src": "/images/chirality/fig_gallery_cw.png",
        "alt": "Representative high-confidence galaxies from the classified catalog (p_ eq>0",
        "number": "Figure 1 (fig:gallery)",
        "title": "Representative high-confidence galaxies from the classified catalog (p_ eq>0",
        "desc": "Representative high-confidence galaxies from the classified catalog (p_ eq>0.9). Left: clockwise (CW) spirals; center: counter-clockwise (CCW) spirals; right: non-spiral () objects --- ellipticals, mergers, and edge-on galaxies that would contaminate a binary spiral classifier. All cutouts are 224×224pixels in grz bands from DESI Legacy DR8. The gallery ill…",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_gallery_ccw.png",
        "alt": "Representative high-confidence galaxies from the classified catalog (p_ eq>0",
        "number": "Figure 2 (fig:gallery)",
        "title": "Representative high-confidence galaxies from the classified catalog (p_ eq>0",
        "desc": "Representative high-confidence galaxies from the classified catalog (p_ eq>0.9). Left: clockwise (CW) spirals; center: counter-clockwise (CCW) spirals; right: non-spiral () objects --- ellipticals, mergers, and edge-on galaxies that would contaminate a binary spiral classifier. All cutouts are 224×224pixels in grz bands from DESI Legacy DR8. The gallery ill…",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_gallery_notspi.png",
        "alt": "Representative high-confidence galaxies from the classified catalog (p_ eq>0",
        "number": "Figure 3 (fig:gallery)",
        "title": "Representative high-confidence galaxies from the classified catalog (p_ eq>0",
        "desc": "Representative high-confidence galaxies from the classified catalog (p_ eq>0.9). Left: clockwise (CW) spirals; center: counter-clockwise (CCW) spirals; right: non-spiral () objects --- ellipticals, mergers, and edge-on galaxies that would contaminate a binary spiral classifier. All cutouts are 224×224pixels in grz bands from DESI Legacy DR8. The gallery ill…",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_equivariance_demo.png",
        "alt": "Equivariant test-time averaging (TTA)",
        "number": "Figure 4 (fig:equivariance_demo)",
        "title": "Equivariant test-time averaging (TTA)",
        "desc": "Equivariant test-time averaging (TTA). Representative Z_2 production TTA examples (original + horizontal flip); D_4 validation (four rotations × two reflections) in Appendix B. Production inference (Catalog C) uses 2-fold Z_2 TTA --- original + horizontal flip only (). Flips swap the CW CCW class labels by construction. Output probabilities are averaged aft…",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_class_pie.png",
        "alt": "Catalog C composition. Of the 8,474,531 galaxies retained in the released catalog, the equivariant TTA classi…",
        "number": "Figure 5 (fig:class_pie)",
        "title": "Catalog C composition. Of the 8,474,531 galaxies retained in the released catalog, the equivariant TTA classi…",
        "desc": "Catalog C composition. Of the 8,474,531 galaxies retained in the released catalog, the equivariant TTA classifier () assigns N_ CW=1,592,107, N_ CCW=1,609,053, and N_ NS=5,273,371 (non-spiral / edge-on / morphologically indeterminate). The spiral sub-catalog N_ spiral = N_ CW+N_ CCW= 3,201,160 is the analysis target for all chirality statistics below (Table…",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_sky_map.png",
        "alt": "Equivariant (Catalog C) chirality asymmetry map of the 8",
        "number": "Figure 6 (fig:sky_map)",
        "title": "Equivariant (Catalog C) chirality asymmetry map of the 8",
        "desc": "Equivariant (Catalog C) chirality asymmetry map of the 8.47M-galaxy catalog (Mollweide projection, equatorial coordinates; per-pixel asymmetry A_p=(N_ CW-N_ CCW)/(N_ CW+N_ CCW) = 2(f_ CW,p-12) at HEALPix NSIDE=64, color scale [-0.08,+0.08]). The DESI Legacy Imaging footprint covers f_ sky=0.49005 of the sky in the support (N_ spiral(p)10 per pixel; Sec. );…",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_spiral_density.png",
        "alt": "Sky density of the 3,201,160 classified spirals (CW + CCW combined, NSIDE=64 Mollweide)",
        "number": "Figure 7 (fig:spiral_density)",
        "title": "Sky density of the 3,201,160 classified spirals (CW + CCW combined, NSIDE=64 Mollweide)",
        "desc": "Sky density of the 3,201,160 classified spirals (CW + CCW combined, NSIDE=64 Mollweide). Per-pixel spiral counts scale with the DESI Legacy Imaging Surveys depth and exposure pattern; the support used for the primary ℓ=1 analysis () requires N_ spiral(p)10 per pixel. Spatial inhomogeneity at this scale is the leakage channel quantified in .",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_confidence_dist.png",
        "alt": "Distribution of maximum-class confidence (,,) for all 8,474,531 galaxies",
        "number": "Figure 8 (fig:confidence_dist)",
        "title": "Distribution of maximum-class confidence (,,) for all 8,474,531 galaxies",
        "desc": "Distribution of maximum-class confidence (,,) for all 8,474,531 galaxies. Strongly bimodal: 73.6\\% at p0.9 (high-confidence labels) + a long tail of indeterminate cases ( p<0.5, dominated by NS/edge-on systems). The high-confidence (HC) cuts at p_ eq>0.6 (N=949,584) and p_ eq>0.8 (N=624,660) used in the systematics cross-checks () are indicated.",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/chirality/fig_raw_vs_eq.png",
        "alt": "Raw (Catalog A) vs equivariant (Catalog C) chirality sky maps (equatorial RA/Dec, per-pixel CW fraction f_ CW…",
        "number": "Figure 9 (fig:raw_vs_eq)",
        "title": "Raw (Catalog A) vs equivariant (Catalog C) chirality sky maps (equatorial RA/Dec, per-pixel CW fraction f_ CW…",
        "desc": "Raw (Catalog A) vs equivariant (Catalog C) chirality sky maps (equatorial RA/Dec, per-pixel CW fraction f_ CW,p, NSIDE=64; shared color scale [0.47,0.53]). The raw definition is class\\_raw\\_y with class\\_raw\\_x fallback only where the former is missing; in this release all 3,321,795 raw spirals come from class\\_raw\\_y (zero fallback rows), while Catalog C c…",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/fig_harmonic_completeness.png",
        "alt": "Historical injection-completeness diagnostic under the artifact-c9b apodized estimator convention (10^3 injec…",
        "number": "Figure 10 (fig:harmonic_completeness)",
        "title": "Historical injection-completeness diagnostic under the artifact-c9b apodized estimator convention (10^3 injec…",
        "desc": "Historical injection-completeness diagnostic under the artifact-c9b apodized estimator convention (10^3 injections per amplitude and axis). It uses a different weighting/null implementation from the exact-support computation and is retained only as sensitivity provenance; it is not a calibrated recovery threshold or physical limit.",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/fig_bootstrap_null.png",
        "alt": "Historical latitude-mask block-bootstrap distribution",
        "number": "Figure 11 (fig:bootstrap_null)",
        "title": "Historical latitude-mask block-bootstrap distribution",
        "desc": "Historical latitude-mask block-bootstrap distribution. NSIDE=8 resamples of the broader |b_ gal|>15^, N_ total>0 WLS field (N_ boot=1000, seed 42), not the field. The distribution is retained as provenance and is not used for an or physical constraint.",
        "source": "Paper 4 · v1.0.269"
      },
      {
        "src": "/images/fig_template_overlap_robustness.png",
        "alt": "Template-overlap robustness sweep for P4 chirality dipole",
        "number": "Figure 101",
        "title": "Template-overlap robustness",
        "desc": "Sweep of the 9-template nuisance basis overlap parameter (correlation between primordial-dipole basis and depth/density templates). Anchors the §IV.D nuisance-marginalized fit robustness claim.",
        "source": "Paper 4 · v1.0.167"
      }
    ]
  },
  {
    "title": "Paper 5 — DESI Chirality × Cosmic-Web Environment",
    "count": "16 figures",
    "items": [
      {
        "src": "/images/fig_z_histogram.png",
        "alt": "Redshift distribution of the matched chirality × DESI DR1 spiral sample (1'' acceptance, after dedup)",
        "number": "Figure 1 (fig:z_histogram)",
        "title": "Redshift distribution of the matched chirality × DESI DR1 spiral sample (1'' acceptance, after dedup)",
        "desc": "Redshift distribution of the matched chirality × DESI DR1 spiral sample (1'' acceptance, after dedup). The distribution peaks at z ≈ 0.15--0.2 (median 0.168) and falls off steeply above z ≈ 0.5; a sparse tail extends to the maximum z = 3.83 (Table ).",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_p5_volume_fractions_pie.png",
        "alt": "In-footprint T-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283…",
        "number": "Figure 2 (fig:volfrac)",
        "title": "In-footprint T-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283…",
        "desc": "In-footprint T-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283 DESI DR1 spectroscopic galaxies (horizontal bar chart; value labels show percentage to one decimal place). The cluster volume fraction (1.0\\%) reflects the high-density tail; the wall+filament fraction (74.5\\%) dominates as expected for galaxy-trace…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_p5_cw_by_env_bar.png",
        "alt": "CW fraction per cosmic-web class in the secondary T-Web run, on the n=812,793 env-labeled spiral rows (coveri…",
        "number": "Figure 3 (fig:cw_by_env)",
        "title": "CW fraction per cosmic-web class in the secondary T-Web run, on the n=812,793 env-labeled spiral rows (coveri…",
        "desc": "CW fraction per cosmic-web class in the secondary T-Web run, on the n=812,793 env-labeled spiral rows (covering 783,820 of the 791,635 unique chirality-relevant matched spirals; 7,815 lack an environment row, ). Bars show the raw observed f_ CW per class (counts shown; monopole subtraction enters the _ vsmonopole column only); black error bars are 95\\% Jeff…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_cw_vs_z.png",
        "alt": "Equivariant CW fraction versus redshift across the matched DR1 chirality-relevant sample, with 95\\% binomial…",
        "number": "Figure 4 (fig:cw_vs_z)",
        "title": "Equivariant CW fraction versus redshift across the matched DR1 chirality-relevant sample, with 95\\% binomial…",
        "desc": "Equivariant CW fraction versus redshift across the matched DR1 chirality-relevant sample, with 95\\% binomial confidence intervals per bin. The low-z bins that dominate the sample (median z = 0.168) sit on the 0.5 line; bins above z ≈ 0.5 contain few objects and have correspondingly wide intervals. The binned values are consistent with no redshift dependence…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_p5_cw_vs_density.png",
        "alt": "Density-quintile null with Paper IV monopole-prediction overlay",
        "number": "Figure 5 (fig:cw_vs_density)",
        "title": "Density-quintile null with Paper IV monopole-prediction overlay",
        "desc": "Density-quintile null with Paper IV monopole-prediction overlay. (a) CW fraction per projected-density quintile (k=5 NN proxy, N=158,327 per bin) with 95\\% Jeffreys binomial CIs; dashed parity f_ CW=0.5 and dotted Paper IV f_ CW=0.4974 references. (b) Observed _ fromhalf per quintile (bars) vs the Paper IV-monopole prediction _ pred=2Δ f_ CWN (red diamonds)…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_p5_healpix_skymap_nside32.png",
        "alt": "NSIDE=32 Mollweide projections in equatorial coordinates",
        "number": "Figure 6 (fig:healpix_skymap)",
        "title": "NSIDE=32 Mollweide projections in equatorial coordinates",
        "desc": "NSIDE=32 Mollweide projections in equatorial coordinates. Top: matched-spiral count per occupied pixel. Bottom: per-pixel signed _ fromhalf for the chirality-relevant matched-spiral subsample. The observed |σ|^ obs_=4.13 vs the label-shuffle null |σ|^ null,p99_=4.78 gives a look-elsewhere p=0.135; no NSIDE returns p<0.05. The map shows no coherent large-sca…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_p5_phase2_sensitivity_heatmap.png",
        "alt": "Phase 2 sensitivity heat-map",
        "number": "Figure 7 (fig:phase2)",
        "title": "Phase 2 sensitivity heat-map",
        "desc": "Phase 2 sensitivity heat-map: per-cell range of f_ CW across the four environment classes \\void, wall, filament, cluster\\ in percentage points, on the declared env-labeled spiral parent. Each cell corresponds to a complete T-Web re-run on the 14,622,283-galaxy DESI DR1 spectro sample at (R_s, _ th). The maximum range across all nine cells is 4.12percentage…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_p5_voids_vs_chirality_skymap.png",
        "alt": "HEALPix NSIDE = 32 Mollweide projection (equatorial coordinates)",
        "number": "Figure 8 (fig:voids_vs_chirality)",
        "title": "HEALPix NSIDE = 32 Mollweide projection (equatorial coordinates)",
        "desc": "HEALPix NSIDE = 32 Mollweide projection (equatorial coordinates). Top: count of DESIVAST maximal voids per pixel (885 occupied pixels at NSIDE = 32, median 4 voids/pix; the body text uses NSIDE = 16 for the sky-stratification table, yielding 297 occupied pixels at a coarser resolution). Bottom: per-pixel chirality _ from\\ half on the z 0.24 matched-spiral s…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_p5_vweb_vs_tempel_overlay.png",
        "alt": "T-Web vs Tempel+2014 FoF cross-validation",
        "number": "Figure 9 (fig:tempel_overlay)",
        "title": "T-Web vs Tempel+2014 FoF cross-validation",
        "desc": "T-Web vs Tempel+2014 FoF cross-validation: per-class CW fraction with 95\\% Jeffreys binomial credible intervals, shared y-axis [0.43, 0.53]. (a) T-Web full-sample canonical run (shown as reference). (b) Tempel+2014 FoF (96,753-spiral overlap). Dashed reference is parity f_ CW=0.5; dotted-red reference is the Paper IV global f_ CW=0.4974 classifier-monopole…",
        "source": "Paper 5 · v0.1.141-2026-07-16"
      },
      {
        "src": "/images/fig_cw_vs_z.png",
        "alt": "P5 CW fraction vs redshift",
        "number": "Figure 101",
        "title": "f_CW vs z",
        "desc": "Equivariant CW fraction as a function of redshift across the DESI DR1 footprint. Visualizes the z-stratified null check that the chirality-environment signal is z-independent.",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_sky_footprint.png",
        "alt": "P5 sky footprint Mollweide projection",
        "number": "Figure 102",
        "title": "P5 sky footprint",
        "desc": "Mollweide footprint of the P5 DESI×DESIVAST environmental analysis (56,981 void spirals + 791,635 cross-matched DR1 spirals). Useful as a context map.",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_z_histogram.png",
        "alt": "P5 redshift histogram by environment class",
        "number": "Figure 103",
        "title": "z histogram by environment",
        "desc": "Redshift histogram of the P5 sample stratified by V-Web/T-Web environment class (void / wall / filament / knot). Anchors the sample-balance discussion.",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_confidence_sensitivity.png",
        "alt": "P5 confidence-threshold sensitivity sweep",
        "number": "Figure 104",
        "title": "Confidence sensitivity",
        "desc": "Sensitivity of the P5 per-environment Δf_CW signal to the equivariant confidence threshold p_eq cut. Quantifies the robustness of the headline result across p_eq ∈ [0.6, 0.95].",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_radius_sensitivity.png",
        "alt": "P5 void-radius sensitivity sweep",
        "number": "Figure 105",
        "title": "Radius sensitivity",
        "desc": "Sensitivity of the per-environment Δf_CW signal to the DESIVAST void-radius cut. Anchors the §VI robustness check that the signal is not driven by a specific void size.",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_cw_vs_density.png",
        "alt": "P5 CW vs cosmic-web local density",
        "number": "Figure 106",
        "title": "f_CW vs local density",
        "desc": "Equivariant CW fraction as a function of cosmic-web local density (V-Web density-quintile classification). Companion to the per-environment bar chart, showing the continuous trend.",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_healpix_cw_residual.png",
        "alt": "P5 HEALPix CW-fraction residual map",
        "number": "Figure 107",
        "title": "HEALPix CW residual",
        "desc": "Per-pixel residual Δf_CW^eq after subtracting the V-Web environmental prediction. Visualizes spatial coherence of the residual + supports the §VII null-systematic discussion.",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      }
    ]
  }
];
