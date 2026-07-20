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
    "title": "Paper 1A — ECH Channel-Level Closure (4 Dark-Energy Routes)",
    "count": "10 figures",
    "items": [
      {
        "src": "/images/fig_theory_map.png",
        "alt": "Bounce-mechanism observable-prediction map",
        "number": "Figure 1 (fig:theory_map)",
        "title": "Bounce-mechanism observable-prediction map",
        "desc": "Bounce-mechanism observable-prediction map. Left column: candidate non-singular bounce mechanisms (LQC, ECH/torsion, matter bounce, quintom-B, Cuscuton, ekpyrotic). Right column: distinctive observable channels. ECH appears bordered with a dashed box marked channel-level closure under stated assumptions (this paper)---the 14-constraint catalog narrows the f…",
        "source": "Paper 1A · v1A.0.50"
      },
      {
        "src": "/images/figure1_lqg_holst_derivation_enhanced.png",
        "alt": "Energy density hierarchy from the Planck scale to the observed dark energy scale, illustrating the phenomenol…",
        "number": "Figure 2 (fig:derivation)",
        "title": "Energy density hierarchy from the Planck scale to the observed dark energy scale, illustrating the phenomenol…",
        "desc": "Energy density hierarchy from the Planck scale to the observed dark energy scale, illustrating the phenomenological scaling ansatz _ vac [(α/M)]M_ Pl^4 (Sec. , Appendix ). This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action.",
        "source": "Paper 1A · v1A.0.50"
      },
      {
        "src": "/images/figure5_rotation_expansion.png",
        "alt": "Cosmic rotation vs Hubble expansion H",
        "number": "Figure 3 (fig:rotation_expansion)",
        "title": "Cosmic rotation vs Hubble expansion H",
        "desc": "Cosmic rotation vs Hubble expansion H. Distance-impact of a residual cosmic rotation component on the late-time Hubble flow. The CMB isotropy bound (/H)_0 < 5× 10^-11 from Saadeh pins the rotation contribution to _ eff = c_^2 (Eq. ) at the 10^-22_Λ^ obs level --- negligible at all redshifts. The dark-energy mechanism in this paper is therefore the ^2 term s…",
        "source": "Paper 1A · v1A.0.50"
      },
      {
        "src": "/images/figure7_observational_timeline.png",
        "alt": "Observational decision timeline for the two surviving ECH-independent class-level falsification paths",
        "number": "Figure 4 (fig:obs_timeline)",
        "title": "Observational decision timeline for the two surviving ECH-independent class-level falsification paths",
        "desc": "Observational decision timeline for the two surviving ECH-independent class-level falsification paths. Top: LiteBIRD CMB birefringence (σ(β)≈0.03^, launch early 2030s) testing the spectator-ALP route 4. Bottom: SPHEREx galaxy bispectrum ( 2028 first cosmological data release) testing the matter-bounce f_NL=-35/16 prediction at 1.3--2.75σ realistic significance (foo…",
        "source": "Paper 1A · v1A.0.50"
      },
      {
        "src": "/images/figure6_parameter_naturalness.png",
        "alt": "Naturalness landscape for the four minimal-ECH dark-energy routes (R1 NJL, R2 one-loop effective action, R3 I…",
        "number": "Figure 5 (fig:naturalness)",
        "title": "Naturalness landscape for the four minimal-ECH dark-energy routes (R1 NJL, R2 one-loop effective action, R3 I…",
        "desc": "Naturalness landscape for the four minimal-ECH dark-energy routes (R1 NJL, R2 one-loop effective action, R3 Immirzi running, R4 parity-CMB spectator-ALP). Each route is shown as a point in the (mass×coupling) plane required to source _Λ at the observed value, with the naturalness window (gray band) defined by the scale of the underlying physics (M_ Pl for R…",
        "source": "Paper 1A · v1A.0.50"
      },
      {
        "src": "/images/figure8_detection_forecast.png",
        "alt": "Detection forecast for the two surviving ECH-independent class tests",
        "number": "Figure 6 (fig:detection_forecast)",
        "title": "Detection forecast for the two surviving ECH-independent class tests",
        "desc": "Detection forecast for the two surviving ECH-independent class tests. Top: matter-bounce f_ NL=-35/16 in the SPHEREx multi-tracer f_ NL Fisher landscape (companion Paper II, 1.3--2.75σ projection). Bottom: spectator-ALP cosmic birefringence in the LiteBIRD σ(β) ≈0.03^ window (Paper Ib companion); the WMAP+Planck β=0.342^± 0.094^ and ACT DR6 β=0.215^± 0.074^ point…",
        "source": "Paper 1A · v1A.0.50"
      },
      {
        "src": "/images/figure5_rotation_expansion.png",
        "alt": "Effect of bounce-era cosmic rotation on the expansion history",
        "number": "Figure 101",
        "title": "Rotation × Expansion",
        "desc": "Distance-impact of a residual cosmic rotation component on the Hubble expansion. Visualizes the (ω/H)_0 < 5×10⁻¹¹ Saadeh+2016 isotropy bound and the consequent suppression of any direct rotation signature in the late-time Hubble flow.",
        "source": "Paper 1A · v1A.0.50-2026-06-09"
      },
      {
        "src": "/images/figure6_parameter_naturalness.png",
        "alt": "Parameter naturalness window across the four ECH routes",
        "number": "Figure 102",
        "title": "Naturalness window (4-route map)",
        "desc": "Position of each of the four minimal Einstein–Cartan–Holst dark-energy routes in the (coupling × mass) plane against the natural-parameter window. Visualizes why the closure rests on cosmological-constant-class tuning at m_θ ~ H_0 rather than amplitude mismatch alone.",
        "source": "Paper 1A · v1A.0.50-2026-06-09"
      },
      {
        "src": "/images/figure7_observational_timeline.png",
        "alt": "Observational decision timeline for the surviving ECH tests",
        "number": "Figure 103",
        "title": "Observational timeline",
        "desc": "Timeline of survey decisions (CMB-S4, LiteBIRD, SPHEREx, DESI DR2) that could falsify or confirm the surviving ECH-independent class-level ECH signatures (f_NL = -35/16 matter-bounce + spectator-ALP birefringence).",
        "source": "Paper 1A · v1A.0.50-2026-06-09"
      },
      {
        "src": "/images/figure8_detection_forecast.png",
        "alt": "Detection forecast for the 2 surviving ECH tests",
        "number": "Figure 104",
        "title": "Surviving-test detection forecast",
        "desc": "Detection-significance forecast for the matter-bounce f_NL = -35/16 SPHEREx window + the spectator-ALP birefringence LiteBIRD window. Connects the no-go theorem of §sec:barriers to the surviving falsification paths in §sec:surviving.",
        "source": "Paper 1A · v1A.0.50-2026-06-09"
      }
    ]
  },
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
        "source": "Paper 1B · v1B.0.108"
      },
      {
        "src": "/images/fig_dneff_viability_two_frozen.png",
        "alt": "_eff marginal posterior comparison across the two frozen dataset combinations of Table (176,240 and 132,949 s…",
        "number": "Figure 2 (fig:dneff_viability)",
        "title": "_eff marginal posterior comparison across the two frozen dataset combinations of Table (176,240 and 132,949 s…",
        "desc": "_eff marginal posterior comparison across the two frozen dataset combinations of Table (176,240 and 132,949 samples). Panel (a): Gaussian summaries of the _eff marginal posteriors at the Table means ±1σ, with the Standard-Model value _eff=0 marked. Panel (b): all seven Table parameters, normalized to the full-tension mean and σ. Both combinations recover _e…",
        "source": "Paper 1B · v1B.0.108"
      },
      {
        "src": "/images/alp_triangle_plot.png",
        "alt": "Spectator-ALP joint posterior triangle from the continuous-prior cross-check configuration in which the photo…",
        "number": "Figure 3 (fig:alp_triangle)",
        "title": "Spectator-ALP joint posterior triangle from the continuous-prior cross-check configuration in which the photo…",
        "desc": "Spectator-ALP joint posterior triangle from the continuous-prior cross-check configuration in which the photon anomaly coefficient is sampled freely (flat priors C_a[4,60] --- shifted and extended from the earlier [1,30] to cover the posterior-supported coupling band (median 20.7, 16--84\\% [7.3,45.6]); the dropped [1,4) interval lies entirely below the mini…",
        "source": "Paper 1B · v1B.0.108"
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
    "count": "9 figures",
    "items": [
      {
        "src": "/images/fig1_shape_function.png",
        "alt": "Matter-bounce bispectrum shape function B_NL(k_1, k, k) as a function of the squeeze ratio k_1/k, showing con…",
        "number": "Figure 1 (fig:shape)",
        "title": "Matter-bounce bispectrum shape function B_NL(k_1, k, k) as a function of the squeeze ratio k_1/k, showing con…",
        "desc": "Exact four-vertex matter-bounce shape function B_NL(k_L, k_S, k_S) as a function of the squeeze ratio k_L/k_S, evaluated directly from the exact vertex-sum polynomial and approaching the corrected squeezed-limit value -35/16 = -2.1875; the marker identifies the equilateral value -255/128.",
        "source": "Paper 2 · v1.7.45"
      },
      {
        "src": "/images/fig2_survey_comparison.png",
        "alt": "Detection significance for f_NL = -35/16 across survey configurations",
        "number": "Figure 2 (fig:surveys)",
        "title": "Detection significance for f_NL = -35/16 across survey configurations",
        "desc": "Detection significance for f_NL = -35/16 across survey configurations. Error bars span the optimistic endpoint (published ideal σ(f_NL) with template-overlap correction only) to the conservative endpoint (full budget: r=0.84 overlap, -correction, photometric-z degradation, PNG bias, b_ marginalization); i.e.\\ optimistic-to-conservative ranges accounting for…",
        "source": "Paper 2 · v1.7.45"
      },
      {
        "src": "/images/fig5_inflation_comparison.png",
        "alt": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The bounce prediction (red diamond) is minimall…",
        "number": "Figure 3 (fig:inflation)",
        "title": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The bounce prediction (red diamond) is minimall…",
        "desc": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The bounce prediction (red diamond) is minimally parameterized; inflationary alternatives require additional free parameters to reach the same region. SPHEREx 1σ error bar shown in blue.",
        "source": "Paper 2 · v1.7.45"
      },
      {
        "src": "/images/fig3_kmin_cliff.png",
        "alt": "Left: σ(f_NL) vs.\\ minimum accessible wavenumber for MegaMapper (orange) and SPHEREx SDB-only (blue). The SPH…",
        "number": "Figure 4 (fig:kmin)",
        "title": "Left: σ(f_NL) vs.\\ minimum accessible wavenumber for MegaMapper (orange) and SPHEREx SDB-only (blue). The SPH…",
        "desc": "Left: σ(f_NL) vs.\\ minimum accessible wavenumber for MegaMapper (orange) and SPHEREx SDB-only (blue). The SPHEREx bispectrum channel (σ = 0.7, dotted) avoids the ultra-large-scale fragility. Right: corresponding detection significance for f_NL = -35/16.",
        "source": "Paper 2 · v1.7.45"
      },
      {
        "src": "/images/bphi_sensitivity.png",
        "alt": "Left: σ(f_NL) as a function of b_ prior uncertainty for MegaMapper SDB (blue). The SPHEREx bispectrum constra…",
        "number": "Figure 5 (fig:bphi)",
        "title": "Left: σ(f_NL) as a function of b_ prior uncertainty for MegaMapper SDB (blue). The SPHEREx bispectrum constra…",
        "desc": "Left: σ(f_NL) as a function of b_ prior uncertainty for MegaMapper SDB (blue). The SPHEREx bispectrum constraint (red dashed) is less sensitive to b_ than SDB but not independent of it; the residual dependence enters at tree level through the Δ b(k) f_NL b_ / k^2 cross-terms f_NL b_ b_1^2 P(k_1) P(k_2) in the multi-tracer Fisher matrix , which propagate to…",
        "source": "Paper 2 · v1.7.45"
      },
      {
        "src": "/images/fig4_decision_thresholds.png",
        "alt": "Observational decision thresholds",
        "number": "Figure 6 (fig:thresholds)",
        "title": "Observational decision thresholds",
        "desc": "Observational decision thresholds. Green: strongly favors bounce. Red: strongly disfavors the quasi-dust matter bounce. Blue vertical line: bounce prediction f_NL = -35/16. Error bars: SPHEREx (σ = 0.7) and MegaMapper conservative (σ = 1.5).",
        "source": "Paper 2 · v1.7.45"
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
        "desc": "2D UMAP embedding of the encoder latent space (PCA 12830, then UMAP) for a 500,000-spectrum stratified DESI DR1 sample, colored by per-spectrum anomaly score. High-score anomalies concentrate in distinct islands of the embedding (bright lobe, lower right) rather than scattering through the bulk population; the 83 gold-tier anomalies (cyan stars) lie on or n…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_skymap_all_surveys.png",
        "alt": "Cross-transfer baseline map",
        "number": "Figure 2 (fig:skymap)",
        "title": "Cross-transfer baseline map",
        "desc": "Cross-transfer baseline map. Mollweide projection of the initial cross-transfer anomaly baseline (319,443 detections shown; the canonical Path-C unique count of 377,482 is not a deduplication of this baseline but the 5″ dedup of the count-retained per-survey native-retrained tallies --- see Table Path-C row and §pathc). ACT DR6 is quarantined and excluded. Color-coded by survey (see legend). The DESI DR1 footprint (14,000 d…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_score_distributions.png",
        "alt": "Anomaly score distributions for the three main spectroscopic surveys",
        "number": "Figure 3 (fig:score_dist)",
        "title": "Anomaly score distributions for the three main spectroscopic surveys",
        "desc": "Anomaly score distributions for the three main spectroscopic surveys. The score S is the per-spectrum reconstruction MSE rescaled to validation z-units: S = (MSE - _ val)/_ val, where _ val and _ val are the mean and standard deviation of MSE on the held-out 20\\% validation split of the per-survey training pool (; cross-transfer for SDSS, native for DESI/LA…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_sdss_umap.png",
        "alt": "Cross-transfer SDSS baseline",
        "number": "Figure 4 (fig:sdss_umap)",
        "title": "Cross-transfer SDSS baseline",
        "desc": "Cross-transfer SDSS baseline. UMAP embedding of the 77,905 SDSS DR18 anomalies from the initial DESI-trained cross-transfer scan, colored by HDBSCAN cluster (left) and by inferred physical category (right). The dominant cluster (green, 84\\% of objects) contains ultra-cool dwarfs (M7--T2) that are completely out-of-distribution for the DESI-trained --- the d…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_neowise_top_anomaly.png",
        "alt": "NEOWISE top infrared anomaly at (α, ) = (180",
        "number": "Figure 5 (fig:neowise_top)",
        "title": "NEOWISE top infrared anomaly at (α, ) = (180",
        "desc": "NEOWISE top infrared anomaly at (α, ) = (180.59^, 0.56^), score = 11.5. DESI Legacy Survey DR9 grz composite, 256 × 256 pixels (108'' × 108''). Extreme W1-W2 infrared color excess; no prior SIMBAD entry within 5''. The optical counterpart is a bright, saturated source with diffraction spikes indicative of a luminous red stellar or quasi-stellar object. Phys…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_novelty_fractions.png",
        "alt": "SIMBAD-unmatched fractions for the six surveys with coordinate-based cross-matching, ranked from lowest (Gaia…",
        "number": "Figure 6 (fig:novelty)",
        "title": "SIMBAD-unmatched fractions for the six surveys with coordinate-based cross-matching, ranked from lowest (Gaia…",
        "desc": "SIMBAD-unmatched fractions for the six surveys with coordinate-based cross-matching, ranked from lowest (Gaia DR3, well-characterized variable stars) to highest (DESI DR1, 99\\% of top-10K objects absent from SIMBAD). The dashed line marks the aggregate 58.8\\% SIMBAD-unmatched fraction. The SIMBAD-unmatched fractions plotted here are a database-coverage meas…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/anomaly_sky_distribution.png",
        "alt": "Spatial distribution of the 195,829 DESI DR1 anomalies",
        "number": "Figure 7 (fig:anomaly_sky)",
        "title": "Spatial distribution of the 195,829 DESI DR1 anomalies",
        "desc": "Spatial distribution of the 195,829 DESI DR1 anomalies. Top left: equatorial sky map color-coded by anomaly score S. Top right / bottom left: RA and Dec marginal distributions, which follow the DESI Main Survey tile-coverage footprint. Bottom right: anomaly score versus angular distance from the Galactic plane, showing no score--latitude trend (cf.\\ the com…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_cross_survey_matches.png",
        "alt": "Spectral pairs for the three DESI × SDSS cross-survey matches",
        "number": "Figure 8 (fig:crossmatch)",
        "title": "Spectral pairs for the three DESI × SDSS cross-survey matches",
        "desc": "Spectral pairs for the three DESI × SDSS cross-survey matches. Left column: DESI DR1 spectrum; right column: same object in SDSS DR18. Black: observed flux (normalized); red dashed: reconstruction. (a, b) Known QSO at z ≈ 1.55: both surveys produce consistent, low anomaly scores, validating the cross-matching approach. (c, d) TIC 374313355 at two epochs: th…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_fnl_improvement.png",
        "alt": "Per-redshift-bin decomposition of the fixed-α = 0",
        "number": "Figure 9 (fig:fnl_improvement)",
        "title": "Per-redshift-bin decomposition of the fixed-α = 0",
        "desc": "Per-redshift-bin decomposition of the fixed-α = 0.15 reference Fisher forecast (Appendix ). Left: σ(f_NL) per redshift bin for the standard DESI QSO single-tracer baseline versus the multi-tracer configuration including AI-selected anomaly tracers; the inset shows the combined result (^ std = 8.98 8.43, a 6.1\\% central-value change). Right: AI-selected anom…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_injection_recovery.png",
        "alt": "Injection-recovery gate results across the six retained surveys, with three additional non-spectral retrains…",
        "number": "Figure 10 (fig:injection_recovery)",
        "title": "Injection-recovery gate results across the six retained surveys, with three additional non-spectral retrains…",
        "desc": "Injection-recovery gate results across the six retained surveys, with three additional non-spectral retrains (Planck CMB native convolutional autoencoder, NEOWISE ecliptic-pole mask) brought into the same axis for comparison. Solid curves show recovery fraction versus injection amplitude (multiples of local noise σ). The horizontal dashed line marks the 50\\…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/B11_sigma_fnl_vs_ndensity.png",
        "alt": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gra…",
        "number": "Figure 11 (fig:shotnoise_sensitivity)",
        "title": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gra…",
        "desc": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gray line marks the dense-tracer limit ( = 11.71); the dotted dark-red line marks the single-tracer baseline ( = 16.85). Vertical orange and goldenrod lines mark the gold ( n = 8.5× 10^-6) and silver ( n = 4.5× 10^-5) anomaly sub-samples. The Heinrich-\\…",
        "source": "Paper 3 · v3.1.80"
      },
      {
        "src": "/images/fig_gallery_top10.png",
        "alt": "Representative DESI DR1 anomalies across all ten taxonomy families",
        "number": "Figure 12 (fig:gallery_top10)",
        "title": "Representative DESI DR1 anomalies across all ten taxonomy families",
        "desc": "Representative DESI DR1 anomalies across all ten taxonomy families. One highest-scored member per family; 2-row × 5-column layout. Border color indicates taxonomy class. Images are DESI Legacy Survey DR9 grz composites. Panel sublabels give the object RA; the high-z QSO panel additionally gives the redshift and the per-arm Z-arm sub-score r_Z (). The taxono…",
        "source": "Paper 3 · v3.1.80"
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
    "count": "10 figures",
    "items": [
      {
        "src": "/images/chirality/fig_gallery_cw.png",
        "alt": "Representative high-confidence galaxies from the classified spiral sub-catalog (p_ eq>0",
        "number": "Figure 1 (fig:gallery)",
        "title": "Representative high-confidence galaxies from the classified spiral sub-catalog (p_ eq>0",
        "desc": "Representative high-confidence galaxies from the classified spiral sub-catalog (p_ eq>0.9). Left: clockwise (CW); right: counter-clockwise (CCW). All cutouts are 224×224pixels in grz bands from DESI Legacy DR8. The pairs illustrate the visual diversity within each chirality class --- different morphological types, redshifts, projection angles, and signal-to…",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_gallery_ccw.png",
        "alt": "Representative high-confidence galaxies from the classified spiral sub-catalog (p_ eq>0",
        "number": "Figure 2 (fig:gallery)",
        "title": "Representative high-confidence galaxies from the classified spiral sub-catalog (p_ eq>0",
        "desc": "Representative high-confidence galaxies from the classified spiral sub-catalog (p_ eq>0.9). Left: clockwise (CW); right: counter-clockwise (CCW). All cutouts are 224×224pixels in grz bands from DESI Legacy DR8. The pairs illustrate the visual diversity within each chirality class --- different morphological types, redshifts, projection angles, and signal-to…",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_equivariance_demo.png",
        "alt": "Test-time D_4 equivariant averaging (TTA)",
        "number": "Figure 3 (fig:equivariance_demo)",
        "title": "Test-time D_4 equivariant averaging (TTA)",
        "desc": "Test-time D_4 equivariant averaging (TTA). For each input image x, the classifier is evaluated on the eight D_4 transforms (four rotations × two reflections). Flips swap the CW CCW class labels by construction. Output probabilities are averaged after the swap, yielding a strictly flip-equivariant CW/CCW classifier with flip-swap correlation =1.000 by constr…",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_class_pie.png",
        "alt": "Catalog C composition. Of the 8,474,531 galaxies retained after image-quality QA, the equivariant TTA classif…",
        "number": "Figure 4 (fig:class_pie)",
        "title": "Catalog C composition. Of the 8,474,531 galaxies retained after image-quality QA, the equivariant TTA classif…",
        "desc": "Catalog C composition. Of the 8,474,531 galaxies retained after image-quality QA, the equivariant TTA classifier () assigns N_ CW=1,592,107, N_ CCW=1,609,053, and N_ NS=5,273,371 (non-spiral / face-on / morphologically indeterminate). The spiral sub-catalog N_ spiral = N_ CW+N_ CCW= 3,201,160 is the analysis target for all chirality statistics below (Table…",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_sky_map.png",
        "alt": "Sky distribution of the 8",
        "number": "Figure 5 (fig:sky_map)",
        "title": "Sky distribution of the 8",
        "desc": "Sky distribution of the 8.47M-galaxy chirality catalog (Mollweide projection, _10 N per HEALPix NSIDE=64 pixel). The DESI Legacy Imaging footprint covers f_ sky≈0.49 of the sky in the canonical mask; the N_ all1 analysis footprint (f_ sky=0.494) is used for the apodized MASTER diagnostic. Spatial uniformity of the per-pixel CW fraction is verified across 7…",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_spiral_density.png",
        "alt": "Sky density of the 3,201,160 classified spirals (CW + CCW combined, NSIDE=64 Mollweide)",
        "number": "Figure 6 (fig:spiral_density)",
        "title": "Sky density of the 3,201,160 classified spirals (CW + CCW combined, NSIDE=64 Mollweide)",
        "desc": "Sky density of the 3,201,160 classified spirals (CW + CCW combined, NSIDE=64 Mollweide). Per-pixel spiral counts scale with the DESI Legacy Imaging Surveys depth and exposure pattern; the canonical mask used for the headline ℓ=1 analysis () requires N_ spiral(p)10 per pixel. Spatial inhomogeneity at this scale is the leakage channel quantified in .",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_confidence_dist.png",
        "alt": "Distribution of maximum-class confidence (,,) for all 8,474,531 galaxies",
        "number": "Figure 7 (fig:confidence_dist)",
        "title": "Distribution of maximum-class confidence (,,) for all 8,474,531 galaxies",
        "desc": "Distribution of maximum-class confidence (,,) for all 8,474,531 galaxies. Strongly bimodal: 73.6\\% at p0.9 (high-confidence labels) + a long tail of indeterminate cases ( p<0.5, dominated by NS/edge-on systems). The high-confidence (HC) cuts at p_ eq>0.6 (N=949,584) and p_ eq>0.8 (N=624,660) used in the systematics cross-checks () are indicated.",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_raw_vs_eq.png",
        "alt": "Raw (Catalog A) vs equivariant (Catalog C) chirality asymmetry sky maps (Mollweide projection, A_p per pixel,…",
        "number": "Figure 8 (fig:raw_vs_eq)",
        "title": "Raw (Catalog A) vs equivariant (Catalog C) chirality asymmetry sky maps (Mollweide projection, A_p per pixel,…",
        "desc": "Raw (Catalog A) vs equivariant (Catalog C) chirality asymmetry sky maps (Mollweide projection, A_p per pixel, NSIDE=64). Left: raw single-pass classifier output; the spatially-structured 0.79\\% classifier CW excess, modulated by non-uniform survey depth, produces the 2.31 real-space dipole + +6.48 pre-MASTER ℓ=1 artifact. Right: 2-fold flip-equivariant TTA;…",
        "source": "Paper 4 · v1.0.167"
      },
      {
        "src": "/images/chirality/fig_multipoles.png",
        "alt": "Pseudo-C_ℓ of the chirality field A_p on the canonical mask, ℓ=1--5 (single panel",
        "number": "Figure 9 (fig:multipoles)",
        "title": "Pseudo-C_ℓ of the chirality field A_p on the canonical mask, ℓ=1--5 (single panel",
        "desc": "Pseudo-C_ℓ of the chirality field A_p on the canonical mask, ℓ=1--5 (single panel; grouped bars). Gray bars with error bars: per-galaxy label-shuffle null expectation (N=1,000 shuffles, 1σ); colored bars: measured C_ℓ. The per-ℓ significance annotations embedded in the panel derive from the figure-generation 1,000-shuffle run and are superseded by the canon…",
        "source": "Paper 4 · v1.0.167"
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
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_p5_volume_fractions_pie.png",
        "alt": "In-footprint V-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283…",
        "number": "Figure 2 (fig:volfrac)",
        "title": "In-footprint V-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283…",
        "desc": "In-footprint V-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283 DESI DR1 spectroscopic galaxies. The cluster volume fraction (1.0\\%) reflects the high-density tail; the wall+filament fraction (74.5\\%) dominates as expected for galaxy-traced large-scale structure.",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_p5_cw_by_env_bar.png",
        "alt": "CW fraction per cosmic-web class on the canonical V-Web run, on the n=812,793 env-labeled spiral rows (791,63…",
        "number": "Figure 3 (fig:cw_by_env)",
        "title": "CW fraction per cosmic-web class on the canonical V-Web run, on the n=812,793 env-labeled spiral rows (791,63…",
        "desc": "CW fraction per cosmic-web class on the canonical V-Web run, on the n=812,793 env-labeled spiral rows (791,635 unique chirality-relevant matched spirals; ). Bars show the observed f_ CW per class; black error bars are 95\\% Jeffreys binomial credible intervals. The void bin (n=428) is dominated by counting noise and brackets parity. The dashed horizontal lin…",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_cw_vs_z.png",
        "alt": "Equivariant CW fraction versus redshift across the matched DR1 chirality-relevant sample, with 95\\% binomial…",
        "number": "Figure 4 (fig:cw_vs_z)",
        "title": "Equivariant CW fraction versus redshift across the matched DR1 chirality-relevant sample, with 95\\% binomial…",
        "desc": "Equivariant CW fraction versus redshift across the matched DR1 chirality-relevant sample, with 95\\% binomial confidence intervals per bin. The low-z bins that dominate the sample (median z = 0.168) sit on the 0.5 line; bins above z ≈ 0.5 contain few objects and have correspondingly wide intervals. The binned values are consistent with no redshift dependence…",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_p5_cw_vs_density.png",
        "alt": "Density-quintile null with Paper IV monopole-prediction overlay",
        "number": "Figure 5 (fig:cw_vs_density)",
        "title": "Density-quintile null with Paper IV monopole-prediction overlay",
        "desc": "Density-quintile null with Paper IV monopole-prediction overlay. Left: CW fraction per projected-density quintile (k=5 NN proxy, N=158,327 per bin) with 95\\% Jeffreys binomial CIs; dashed parity f_ CW=0.5 and dotted Paper IV f_ CW=0.4974 references. Right: observed _ fromhalf per quintile (bars) vs the Paper IV-monopole prediction _ pred=2Δ f_ CWN (red diam…",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_p5_healpix_skymap_nside32.png",
        "alt": "Per-pixel signed _ fromhalf for the chirality-relevant matched-spiral subsample at NSIDE=32 (Mollweide projec…",
        "number": "Figure 6 (fig:healpix_skymap)",
        "title": "Per-pixel signed _ fromhalf for the chirality-relevant matched-spiral subsample at NSIDE=32 (Mollweide projec…",
        "desc": "Per-pixel signed _ fromhalf for the chirality-relevant matched-spiral subsample at NSIDE=32 (Mollweide projection, equatorial coordinates). The observed |σ|^ obs_=4.13 vs the label-shuffle null |σ|^ null,p99_=4.78 gives a look-elsewhere p=0.135; no NSIDE returns p<0.05. The map shows no coherent large-scale structure beyond random pixel-level scatter; the h…",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_p5_phase2_sensitivity_heatmap.png",
        "alt": "Phase 2 sensitivity heat-map",
        "number": "Figure 7 (fig:phase2)",
        "title": "Phase 2 sensitivity heat-map",
        "desc": "Phase 2 sensitivity heat-map: per-cell range of f_ CW across the four environment classes \\void, wall, filament, cluster\\ in percentage points, on the declared env-labeled spiral parent. Each cell corresponds to a complete V-Web re-run on the 14,622,283-galaxy DESI DR1 spectro sample at (R_s, _ th). The maximum range across all nine cells is 4.12percentage…",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_p5_voids_vs_chirality_skymap.png",
        "alt": "HEALPix NSIDE = 32 Mollweide projection (equatorial coordinates)",
        "number": "Figure 8 (fig:voids_vs_chirality)",
        "title": "HEALPix NSIDE = 32 Mollweide projection (equatorial coordinates)",
        "desc": "HEALPix NSIDE = 32 Mollweide projection (equatorial coordinates). Top: count of DESIVAST maximal voids per pixel (885 occupied pixels, median 4 voids/pix). Bottom: per-pixel chirality _ from\\ half on the z 0.24 matched-spiral subsample restricted to pixels with 200 spirals (1,496 valid pixels, σ range -3.45 to +3.48). The Pearson correlation across the n_ p…",
        "source": "Paper 5 · v0.1.52-2026-06-09"
      },
      {
        "src": "/images/fig_p5_vweb_vs_tempel_overlay.png",
        "alt": "V-Web (left; full-sample canonical run, shown as reference) vs Tempel+2014 FoF (right; 96,753-spiral overlap)…",
        "number": "Figure 9 (fig:tempel_overlay)",
        "title": "V-Web (left; full-sample canonical run, shown as reference) vs Tempel+2014 FoF (right; 96,753-spiral overlap)…",
        "desc": "V-Web (left; full-sample canonical run, shown as reference) vs Tempel+2014 FoF (right; 96,753-spiral overlap) cross-validation: per-class CW fraction with 95\\% Jeffreys binomial credible intervals, shared y-axis [0.43, 0.53]. Dashed reference is parity f_ CW=0.5; dotted-red reference is the Paper IV global f_ CW=0.4974 classifier-monopole offset. The quanti…",
        "source": "Paper 5 · v0.1.52-2026-06-09"
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
