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
    "title": "Paper 1A — ECH Structural Closure (No-Go Theorem)",
    "count": "2 figures",
    "items": [
      {
        "src": "/images/fig_theory_map.png",
        "alt": "Bounce-mechanism observable-prediction map",
        "number": "Figure 1 (fig:theory_map)",
        "title": "Bounce-mechanism observable-prediction map",
        "desc": "Bounce-mechanism observable-prediction map. Left column: candidate non-singular bounce mechanisms (LQC, ECH/torsion, matter bounce, quintom-B, Cuscuton, ekpyrotic). Right column: distinctive observable channels. ECH appears bordered with a dashed box marked channel-level closure under stated assumptions (this paper)---the 14-constraint catalog narrows the f…",
        "source": "Paper 1A · v1A.0.44"
      },
      {
        "src": "/images/figure1_lqg_holst_derivation_enhanced.png",
        "alt": "Energy density hierarchy from the Planck scale to the observed dark energy scale, illustrating the phenomenol…",
        "number": "Figure 2 (fig:derivation)",
        "title": "Energy density hierarchy from the Planck scale to the observed dark energy scale, illustrating the phenomenol…",
        "desc": "Energy density hierarchy from the Planck scale to the observed dark energy scale, illustrating the phenomenological scaling ansatz _ vac [(α/M)]M_ Pl^4 (Sec. , Appendix ). This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action.",
        "source": "Paper 1A · v1A.0.44"
      }
    ]
  },
  {
    "title": "Paper 1B — Technical Verification Companion (MCMC + NaMaster)",
    "count": "1 figure",
    "items": [
      {
        "src": "/images/paper1_corner_full_tension.png",
        "alt": "Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw",
        "number": "Figure 1 (fig:corner_full_tension)",
        "title": "Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw",
        "desc": "Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote ) over Planck+BAO+SN+H0+S_8. The _eff posterior is consistent with zero (-0.020± 0.169), confirming no additional relativistic species at recombination.",
        "source": "Paper 1B · v1B.0.42"
      }
    ]
  },
  {
    "title": "Paper 2 — Matter-Bounce f_NL SPHEREx Forecast",
    "count": "6 figures",
    "items": [
      {
        "src": "/images/fig1_shape_function.png",
        "alt": "Matter-bounce bispectrum shape function B_NL(k_1, k, k) as a function of the squeeze ratio k_1/k, showing con…",
        "number": "Figure 1 (fig:shape)",
        "title": "Matter-bounce bispectrum shape function B_NL(k_1, k, k) as a function of the squeeze ratio k_1/k, showing con…",
        "desc": "Matter-bounce bispectrum shape function B_NL(k_1, k, k) as a function of the squeeze ratio k_1/k, showing convergence to -35/8 in the squeezed limit. Red circle: squeezed benchmark. Orange square: equilateral. Green triangle: folded.",
        "source": "Paper 2 · v1.7.43"
      },
      {
        "src": "/images/fig2_survey_comparison.png",
        "alt": "Detection significance for f_NL = -35/8 across survey configurations",
        "number": "Figure 2 (fig:surveys)",
        "title": "Detection significance for f_NL = -35/8 across survey configurations",
        "desc": "Detection significance for f_NL = -35/8 across survey configurations. Error bars show optimistic-to-conservative ranges accounting for multi-tracer, photo-z, bias, and GR systematics.",
        "source": "Paper 2 · v1.7.43"
      },
      {
        "src": "/images/fig5_inflation_comparison.png",
        "alt": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The bounce prediction (red diamond) is minimall…",
        "number": "Figure 3 (fig:inflation)",
        "title": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The bounce prediction (red diamond) is minimall…",
        "desc": "f_NL landscape: matter bounce vs.\\ inflationary alternatives. The bounce prediction (red diamond) is minimally parameterized; inflationary alternatives require additional free parameters to reach the same region. SPHEREx 1σ error bar shown in blue.",
        "source": "Paper 2 · v1.7.43"
      },
      {
        "src": "/images/fig3_kmin_cliff.png",
        "alt": "Left: σ(f_NL) vs.\\ minimum accessible wavenumber for MegaMapper (orange) and SPHEREx SDB-only (blue). The SPH…",
        "number": "Figure 4 (fig:kmin)",
        "title": "Left: σ(f_NL) vs.\\ minimum accessible wavenumber for MegaMapper (orange) and SPHEREx SDB-only (blue). The SPH…",
        "desc": "Left: σ(f_NL) vs.\\ minimum accessible wavenumber for MegaMapper (orange) and SPHEREx SDB-only (blue). The SPHEREx bispectrum channel (σ = 0.7, dotted) avoids the ultra-large-scale fragility. Right: corresponding detection significance for f_NL = -35/8.",
        "source": "Paper 2 · v1.7.43"
      },
      {
        "src": "/images/bphi_sensitivity.png",
        "alt": "Left: σ(f_NL) as a function of b_ prior uncertainty for MegaMapper SDB (blue). The SPHEREx bispectrum constra…",
        "number": "Figure 5 (fig:bphi)",
        "title": "Left: σ(f_NL) as a function of b_ prior uncertainty for MegaMapper SDB (blue). The SPHEREx bispectrum constra…",
        "desc": "Left: σ(f_NL) as a function of b_ prior uncertainty for MegaMapper SDB (blue). The SPHEREx bispectrum constraint (red dashed) is less sensitive to b_ than SDB but not independent of it; the residual dependence enters at tree level through the Δ b(k) f_NL b_ / k^2 cross-terms f_NL b_ b_1^2 P(k_1) P(k_2) in the multi-tracer Fisher matrix , which propagate to…",
        "source": "Paper 2 · v1.7.43"
      },
      {
        "src": "/images/fig4_decision_thresholds.png",
        "alt": "Observational decision thresholds",
        "number": "Figure 6 (fig:thresholds)",
        "title": "Observational decision thresholds",
        "desc": "Observational decision thresholds. Green: strongly favors bounce. Red: strongly disfavors the quasi-dust matter bounce. Blue vertical line: bounce prediction f_NL = -35/8. Error bars: SPHEREx (σ = 0.7) and MegaMapper conservative (σ = 1.5).",
        "source": "Paper 2 · v1.7.43"
      }
    ]
  },
  {
    "title": "Paper 3 — DESI Spectral Anomalies (Multi-Survey Catalog)",
    "count": "22 figures",
    "items": [
      {
        "src": "/images/fig_architecture.png",
        "alt": "architecture. Encoder (top) compresses the input to a per-survey latent bottleneck; decoder (bottom) reconstr…",
        "number": "Figure 1 (fig:architecture)",
        "title": "architecture. Encoder (top) compresses the input to a per-survey latent bottleneck; decoder (bottom) reconstr…",
        "desc": "architecture. Encoder (top) compresses the input to a per-survey latent bottleneck; decoder (bottom) reconstructs the input. All layers use ReLU activations; batch normalization (BN) and dropout are applied in the first two encoder layers only. The anomaly score S is the total per-element mean-squared reconstruction error (Eq. ).",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_example_spectra.png",
        "alt": "Representative spectra illustrating the six main anomaly categories identified across the multi-survey campai…",
        "number": "Figure 2 (fig:example_spectra)",
        "title": "Representative spectra illustrating the six main anomaly categories identified across the multi-survey campai…",
        "desc": "Representative spectra illustrating the six main anomaly categories identified across the multi-survey campaign. Black line: observed spectrum; red dashed: reconstruction. Shaded background regions indicate the DESI B (blue), R (gray), and Z (tan) spectral arms. Anomaly scores are the total per-element MSE (Eq. ). (a) Baseline normal ELG at z=0.92: reconstr…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_skymap_all_surveys.png",
        "alt": "[Cross-transfer baseline map --- superseded by Path-C native counts",
        "number": "Figure 3 (fig:skymap)",
        "title": "[Cross-transfer baseline map --- superseded by Path-C native counts",
        "desc": "[Cross-transfer baseline map --- superseded by Path-C native counts.] Mollweide projection of the initial cross-transfer anomaly baseline (319,443 detections shown; canonical Path-C unique count is 378,280 after per-survey native retrains and 7-way deduplication --- see Table Path-C row and ). ACT DR6 is quarantined and excluded. Color-coded by survey (see…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_score_distributions.png",
        "alt": "Anomaly score distributions for the three main spectroscopic surveys",
        "number": "Figure 4 (fig:score_dist)",
        "title": "Anomaly score distributions for the three main spectroscopic surveys",
        "desc": "Anomaly score distributions for the three main spectroscopic surveys. The score S is the per-spectrum reconstruction MSE rescaled to validation z-units: S = (MSE - _ val)/_ val, where _ val and _ val are the mean and standard deviation of MSE on the held-out 20\\% validation split of the per-survey training pool (; cross-transfer for SDSS, native for DESI/LA…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_A1_highz_qso.png",
        "alt": "DESI DR1 confirmed high-z QSO candidates (z ≈ 6",
        "number": "Figure 5 (fig:gallery_highz)",
        "title": "DESI DR1 confirmed high-z QSO candidates (z ≈ 6",
        "desc": "DESI DR1 confirmed high-z QSO candidates (z ≈ 6.0--6.23). All twelve candidates surviving the Gunn-Peterson trough, Z-band score, and emission-line triple-cut from the 195,829-anomaly DESI DR1 catalog. Images are DESI Legacy Survey DR9 grz composite sky cutouts, 128 × 128 pixels (54'' × 54'' per panel). Panels sorted by decreasing Z-arm sub-score r_Z (top-l…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_sdss_umap.png",
        "alt": "[Cross-transfer baseline --- superseded by Path-C native retrain (12 sources at S>5",
        "number": "Figure 6 (fig:sdss_umap)",
        "title": "[Cross-transfer baseline --- superseded by Path-C native retrain (12 sources at S>5",
        "desc": "[Cross-transfer baseline --- superseded by Path-C native retrain (12 sources at S>5; see ).] UMAP embedding of the 77,905 SDSS DR18 anomalies from the initial DESI-trained cross-transfer scan, colored by HDBSCAN cluster (left) and by inferred physical category (right). The dominant cluster (green, 84\\% of objects) contains ultra-cool dwarfs (M7--T2) that ar…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_lamost_blue_excess.png",
        "alt": "LAMOST DR10 training-bias artifact",
        "number": "Figure 7 (fig:lamost)",
        "title": "LAMOST DR10 training-bias artifact",
        "desc": "LAMOST DR10 training-bias artifact. Left: Distribution of the peak-residual wavelength for LAMOST anomalies (green) vs.\\ the expected uniform distribution (gray). The extreme concentration below 4500 \\ (LAMOST B arm) — containing 98\\% of all anomalies — is a hallmark of training-set bias: objects observed at higher airmass or with sub-optimal blue-arm calib…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_neowise_top_anomaly.png",
        "alt": "NEOWISE top infrared anomaly at (α, ) = (180",
        "number": "Figure 8 (fig:neowise_top)",
        "title": "NEOWISE top infrared anomaly at (α, ) = (180",
        "desc": "NEOWISE top infrared anomaly at (α, ) = (180.59^, 0.56^), score = 11.5. DESI Legacy Survey DR9 grz composite, 256 × 256 pixels (108'' × 108''). Extreme W1-W2 infrared color excess; no prior SIMBAD entry within 5''. The optical counterpart is a bright, saturated source with diffraction spikes indicative of a luminous red stellar or quasi-stellar object. Phys…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_novelty_fractions.png",
        "alt": "SIMBAD-unmatched fractions for the six surveys with coordinate-based cross-matching, ranked from lowest (Gaia…",
        "number": "Figure 9 (fig:novelty)",
        "title": "SIMBAD-unmatched fractions for the six surveys with coordinate-based cross-matching, ranked from lowest (Gaia…",
        "desc": "SIMBAD-unmatched fractions for the six surveys with coordinate-based cross-matching, ranked from lowest (Gaia DR3, well-characterized variable stars) to highest (DESI DR1, 99\\% of top-10K objects absent from SIMBAD). The dashed line marks the aggregate 58.8\\% SIMBAD-unmatched fraction. The SIMBAD-unmatched fractions plotted here are a database-coverage meas…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_cross_survey_matches.png",
        "alt": "Spectral pairs for the three DESI × SDSS cross-survey matches",
        "number": "Figure 10 (fig:crossmatch)",
        "title": "Spectral pairs for the three DESI × SDSS cross-survey matches",
        "desc": "Spectral pairs for the three DESI × SDSS cross-survey matches. Left column: DESI DR1 spectrum; right column: same object in SDSS DR18. Black: observed flux (normalized); red dashed: reconstruction. (a, b) Known QSO at z ≈ 1.55: both surveys produce consistent, low anomaly scores, validating the cross-matching approach. (c, d) TIC 374313355 at two epochs: th…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_injection_recovery.png",
        "alt": "Injection-recovery gate results across the six retained surveys, with three additional non-spectral retrains…",
        "number": "Figure 11 (fig:injection_recovery)",
        "title": "Injection-recovery gate results across the six retained surveys, with three additional non-spectral retrains…",
        "desc": "Injection-recovery gate results across the six retained surveys, with three additional non-spectral retrains (Planck CMB native convolutional autoencoder, NEOWISE ecliptic-pole mask) brought into the same axis for comparison. Solid curves show recovery fraction versus injection amplitude (multiples of local noise σ). The horizontal dashed line marks the 50\\…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/B11_sigma_fnl_vs_ndensity.png",
        "alt": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gra…",
        "number": "Figure 12 (fig:shotnoise_sensitivity)",
        "title": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gra…",
        "desc": "Multi-tracer Fisher vs.\\ tracer number density n for the canonical 5-tracer configuration of . The dashed gray line marks the dense-tracer limit ( = 11.71); the dotted dark-red line marks the single-tracer baseline ( = 16.85). Vertical orange and goldenrod lines mark the gold ( n = 8.5× 10^-6) and silver ( n = 4.5× 10^-5) anomaly sub-samples. The Heinrich-\\…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_top10.png",
        "alt": "Representative DESI DR1 anomalies across all ten taxonomy families",
        "number": "Figure 13 (fig:gallery_top10)",
        "title": "Representative DESI DR1 anomalies across all ten taxonomy families",
        "desc": "Representative DESI DR1 anomalies across all ten taxonomy families. One highest-scored member per family; 2-row × 5-column layout. Border color indicates taxonomy class. Images are DESI Legacy Survey DR9 grz composites. Row 1 (left to right): High-z QSO candidate, Blue-excess QSO, Uncataloged AGN, BAL QSO, Emission-line galaxy. Row 2: Unusual continuum (LRG…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a2_qso.png",
        "alt": "Blue-excess QSO candidates (top 16 of 16,602)",
        "number": "Figure 14 (fig:gallery_a2)",
        "title": "Blue-excess QSO candidates (top 16 of 16,602)",
        "desc": "Blue-excess QSO candidates (top 16 of 16,602). Quasars with anomalous UV-blue excess relative to the \\ training distribution. Excess continuum flux at < 4000 \\ drives the B-arm anomaly score in this family. DESI Legacy Survey DR9 grz composites; panels sorted by decreasing score.",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a3_agn.png",
        "alt": "Uncataloged AGN (top 16 of 23,400)",
        "number": "Figure 15 (fig:gallery_a3)",
        "title": "Uncataloged AGN (top 16 of 23,400)",
        "desc": "Uncataloged AGN (top 16 of 23,400). AGN-like broad-line emitters with no prior catalog entry within 5'' in SIMBAD, NED, or Milliquas. 73\\% of this family are genuinely novel at the 5'' match radius. DESI Legacy Survey DR9 grz composites.",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a4_bal_qso.png",
        "alt": "Broad Absorption Line (BAL) QSO candidates (top 16 of 13,650)",
        "number": "Figure 16 (fig:gallery_a4)",
        "title": "Broad Absorption Line (BAL) QSO candidates (top 16 of 13,650)",
        "desc": "Broad Absorption Line (BAL) QSO candidates (top 16 of 13,650). Deep UV absorption troughs blueward of Civ 1549 and Mgii 2798 indicate powerful QSO-driven outflows. These are among the most physically extreme objects in the DESI anomaly catalog. DESI Legacy Survey DR9 grz composites.",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a5_elg.png",
        "alt": "Extreme emission-line galaxies (top 16 of 35,100)",
        "number": "Figure 17 (fig:gallery_a5)",
        "title": "Extreme emission-line galaxies (top 16 of 35,100)",
        "desc": "Extreme emission-line galaxies (top 16 of 35,100). Galaxies with anomalous emission-line ratios that fall predominantly in the AGN region of the BPT diagram. Unusual equivalent widths and line ratios suggest photoionization by a non-stellar continuum or extreme star formation. DESI Legacy Survey DR9 grz composites.",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a6_lrg.png",
        "alt": "Unusual continuum objects (top 16 of 29,250)",
        "number": "Figure 18 (fig:gallery_a6)",
        "title": "Unusual continuum objects (top 16 of 29,250)",
        "desc": "Unusual continuum objects (top 16 of 29,250). Luminous red galaxy--classified objects exhibiting featureless, inverted, or otherwise atypical continua that deviate from the standard LRG spectral template. Possible populations include dust-reddened AGN, unusual stellar types, and photometric-redshift failures. DESI Legacy Survey DR9 grz composites.",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a7_post_starburst.png",
        "alt": "Post-starburst galaxy candidates (top 16 of 11,700)",
        "number": "Figure 19 (fig:gallery_a7)",
        "title": "Post-starburst galaxy candidates (top 16 of 11,700)",
        "desc": "Post-starburst galaxy candidates (top 16 of 11,700). Galaxies with strong Balmer absorption (H_A > 5 ) and suppressed [Oii] emission, indicating a recently quenched ( 1 Gyr ago) starburst. The identifies these as anomalous because their post-burst spectral shape falls outside the normal passive-evolution locus. DESI Legacy Survey DR9 grz composites.",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a8_blue_compact.png",
        "alt": "Blue compact galaxy candidates (top 16 of 7,800)",
        "number": "Figure 20 (fig:gallery_a8)",
        "title": "Blue compact galaxy candidates (top 16 of 7,800)",
        "desc": "Blue compact galaxy candidates (top 16 of 7,800). Compact morphologies with UV-bright stellar populations. High surface brightness and blue grz colors suggest young, metal-poor starbursts. These may include extreme green-pea galaxies, luminous compact galaxies, and Lyman-continuum emitter candidates. DESI Legacy Survey DR9 grz composites.",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a9_star.png",
        "alt": "Cool and unusual stellar objects (top 16 of 15,600)",
        "number": "Figure 21 (fig:gallery_a9)",
        "title": "Cool and unusual stellar objects (top 16 of 15,600)",
        "desc": "Cool and unusual stellar objects (top 16 of 15,600). Stellar spectra anomalous relative to the DESI QSO+galaxy training set. Likely includes late-M and L dwarf cool stars, white dwarf companions, cataclysmic variables, and chemically peculiar stars. Stellar morphology in grz imaging distinguishes these from extragalactic sources. DESI Legacy Survey DR9 grz…",
        "source": "Paper 3 · v3.1.73"
      },
      {
        "src": "/images/fig_gallery_a10_unknown.png",
        "alt": "Multi-band anomalies and unclassified objects (top 16 of 29,250)",
        "number": "Figure 22 (fig:gallery_a10)",
        "title": "Multi-band anomalies and unclassified objects (top 16 of 29,250)",
        "desc": "Multi-band anomalies and unclassified objects (top 16 of 29,250). Objects in the highest-scoring ``Unknown'' HDBSCAN cluster, exhibiting anomalous flux across all three spectral arms simultaneously. This family has the highest anomaly scores in the full DESI catalog (S_ max = 25.2) and the lowest SIMBAD cross-match rate (< 0.1\\%). The most physically exotic…",
        "source": "Paper 3 · v3.1.73"
      }
    ]
  },
  {
    "title": "Paper 4 — Galaxy Chirality Catalog (3.2M Spirals)",
    "count": "14 figures",
    "items": [
      {
        "src": "/images/chirality/fig_spiral_density.png",
        "alt": "Sky density of classified spiral galaxies (CW + CCW) in equatorial coordinates (Mollweide projection, = 64)",
        "number": "Figure 1 (fig:spiral_density)",
        "title": "Sky density of classified spiral galaxies (CW + CCW) in equatorial coordinates (Mollweide projection, = 64)",
        "desc": "Sky density of classified spiral galaxies (CW + CCW) in equatorial coordinates (Mollweide projection, = 64). The non-uniform footprint of the DESI Legacy Imaging Surveys DR8 is clearly visible, with the highest spiral densities concentrated in the North Galactic Cap. This spatial non-uniformity is the primary driver of the pre-MASTER pseudo-C_ℓ inflation in…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_gallery_cw.png",
        "alt": "Representative clockwise (CW) spiral galaxies from the catalog, ordered by decreasing classification confiden…",
        "number": "Figure 2 (fig:gallery_cw)",
        "title": "Representative clockwise (CW) spiral galaxies from the catalog, ordered by decreasing classification confiden…",
        "desc": "Representative clockwise (CW) spiral galaxies from the catalog, ordered by decreasing classification confidence (left to right, top to bottom). Each cutout is 224 × 224 pixels ( 59'' × 59'') in grz composite from DESI Legacy DR8. All examples shown have equivariant confidence ^ eq > 0.95.",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_gallery_ccw.png",
        "alt": "Representative counter-clockwise (CCW) spiral galaxies, presented identically to Fig",
        "number": "Figure 3 (fig:gallery_ccw)",
        "title": "Representative counter-clockwise (CCW) spiral galaxies, presented identically to Fig",
        "desc": "Representative counter-clockwise (CCW) spiral galaxies, presented identically to Fig. . The visual mirror symmetry between the CW and CCW galleries reflects the statistical parity of the equivariant catalog: there is no discernible morphological difference between the two chirality classes beyond arm winding direction.",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_equivariance_demo.png",
        "alt": "Demonstration of the test-time equivariant averaging procedure (Eq",
        "number": "Figure 4 (fig:equivariance_demo)",
        "title": "Demonstration of the test-time equivariant averaging procedure (Eq",
        "desc": "Demonstration of the test-time equivariant averaging procedure (Eq. ). Left column: original galaxy images. Center column: horizontally reflected images. Right column: probability bar charts showing the raw softmax outputs for each orientation and the final equivariant probabilities. The CW and CCW channels swap exactly upon reflection; the equivariant aver…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_class_pie.png",
        "alt": "Class breakdown of the 8,474,531-galaxy catalog",
        "number": "Figure 5 (fig:class_pie)",
        "title": "Class breakdown of the 8,474,531-galaxy catalog",
        "desc": "Class breakdown of the 8,474,531-galaxy catalog. The three-class output is dominated by the /edge-on class (60.8\\% raw, 62.2\\% post-equivariance), which captures ellipticals, irregulars, edge-on disks, and artifacts. Among the equivariant-classified spirals (N_ spiral^ eq = 3,201,160 = 1,592,107 + 1,609,053 ), the CW and CCW fractions are 50.8\\% and 49.2\\%…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_confidence_dist.png",
        "alt": "Distribution of maximum-class confidence for all 8",
        "number": "Figure 6 (fig:confidence_dist)",
        "title": "Distribution of maximum-class confidence for all 8",
        "desc": "Distribution of maximum-class confidence for all 8.47 million galaxies. The distribution is strongly bimodal, with a sharp high-confidence peak near unity and a secondary peak near 0.5--0.6 corresponding to ambiguous morphologies (face-on ellipticals misclassifiable as smooth spirals, mergers, and low-surface-brightness objects). The high-confidence peak en…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_sky_map.png",
        "alt": "HEALPix sky map ( = 64, Mollweide projection) of the per-pixel chirality asymmetry A_p = (N_ CW - N_ CCW) / (…",
        "number": "Figure 7 (fig:sky_map)",
        "title": "HEALPix sky map ( = 64, Mollweide projection) of the per-pixel chirality asymmetry A_p = (N_ CW - N_ CCW) / (…",
        "desc": "HEALPix sky map ( = 64, Mollweide projection) of the per-pixel chirality asymmetry A_p = (N_ CW - N_ CCW) / (N_ CW + N_ CCW) for Catalog C (equivariant). The color scale spans ± 5\\%. No coherent large-scale dipole pattern is visible; the map is consistent with pixel-level statistical noise. Gray pixels contain fewer than 10 spiral galaxies and are masked fr…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_multipoles.png",
        "alt": "Angular power spectrum of the chirality asymmetry map (Catalog C, equivariant) for multipoles ℓ = 1--5",
        "number": "Figure 8 (fig:multipoles)",
        "title": "Angular power spectrum of the chirality asymmetry map (Catalog C, equivariant) for multipoles ℓ = 1--5",
        "desc": "Angular power spectrum of the chirality asymmetry map (Catalog C, equivariant) for multipoles ℓ = 1--5. Black points show the measured C_ℓ values; the gray band indicates the 1 and 2 envelopes from 1,000 Monte Carlo null realizations at the canonical N_ spiral=3,201,160 shot-noise normalization. The MASTER-deconvolved ℓ=1 value is -0.12 on the analysis subs…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/fig_2pt_chirality.png",
        "alt": "Two-point chirality correlation w_ CW() (panel a, data with ± 1 and ± 2 null bands shaded) and per-bin signif…",
        "number": "Figure 9 (fig:wtheta)",
        "title": "Two-point chirality correlation w_ CW() (panel a, data with ± 1 and ± 2 null bands shaded) and per-bin signif…",
        "desc": "Two-point chirality correlation w_ CW() (panel a, data with ± 1 and ± 2 null bands shaded) and per-bin significance (panel b). The maximum deviation is -2.41 at ≈0.5^, which coincides with the DESI Legacy Survey brick angular scale ( 0.25^ DR8 brick edge, periodic at 0.5^). A genuine cosmological CW-CW clustering signal would not have a characteristic scale…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_hemisphere.png",
        "alt": "Hemisphere asymmetry scan results",
        "number": "Figure 10 (fig:hemisphere)",
        "title": "Hemisphere asymmetry scan results",
        "desc": "Hemisphere asymmetry scan results. Each point represents the CW fraction difference between a pair of opposing hemispheres, evaluated for great-circle axes in 10^ increments of Galactic longitude and latitude ( 650 directions). The dashed horizontal lines mark 2 and 3 thresholds. The peak asymmetry of 3.05 (red diamond, local pre-LEE significance) has a hal…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_sky_regions.png",
        "alt": "CW fraction by sky region for Catalog C (equivariant)",
        "number": "Figure 11 (fig:sky_regions)",
        "title": "CW fraction by sky region for Catalog C (equivariant)",
        "desc": "CW fraction by sky region for Catalog C (equivariant). Each bar shows the CW/(CW+CCW) fraction in one of seven sky regions defined by RA quadrant and declination band. The dashed line marks exact parity (0.5000). All regions fall within ± 0.5\\% of 50/50, confirming the absence of position-dependent classification bias. Error bars show 1 binomial uncertainti…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/chirality/fig_raw_vs_eq.png",
        "alt": "Side-by-side comparison of the chirality asymmetry sky maps for Catalog A (raw, left) and Catalog C (equivari…",
        "number": "Figure 12 (fig:raw_vs_eq)",
        "title": "Side-by-side comparison of the chirality asymmetry sky maps for Catalog A (raw, left) and Catalog C (equivari…",
        "desc": "Side-by-side comparison of the chirality asymmetry sky maps for Catalog A (raw, left) and Catalog C (equivariant, right), both at = 64 in Mollweide projection. The raw map exhibits a 2.31 real-space dipole (with pre-MASTER pseudo-C_ℓ lowest bandpower (_ eff=4, ℓ[2,6]) inflated to +6.48) aligned with the DESI Legacy survey footprint, produced by a classifier…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/fig_psf_correlation.png",
        "alt": "PSF-ellipticity correlation calibration",
        "number": "Figure 13 (fig:psf_correlation)",
        "title": "PSF-ellipticity correlation calibration",
        "desc": "PSF-ellipticity correlation calibration. Panel (a): Pixel-level Pearson |r| between f_ CW and seven PSF/morphology covariates (e_1, e_2, |e|, b/a, PA, |e_1|, |e_2|), plotted against the strict |r|<10^-3 bar (dashed black) and the relaxed |r|<10^-2 bar (dotted gray). Red bars are statistically significant at p<10^-2; green bars are not. The maximum |r|=0.042…",
        "source": "Paper 4 · v1.0.150"
      },
      {
        "src": "/images/fig_binned_cw_fraction.png",
        "alt": "Per-bin equivariant CW fraction for the three continuous morphology axes available in the production catalog…",
        "number": "Figure 14 (fig:binned_cw_fraction)",
        "title": "Per-bin equivariant CW fraction for the three continuous morphology axes available in the production catalog…",
        "desc": "Per-bin equivariant CW fraction for the three continuous morphology axes available in the production catalog (left: log Sersic effective radius _10 r_ eff, a half-light-radius proxy; center: de-Vaucouleurs profile fraction fracdev; right: axis ratio b/a). Error bars are per-bin Poisson standard errors. The horizontal red line is the catalog-wide CW fraction…",
        "source": "Paper 4 · v1.0.150"
      }
    ]
  },
  {
    "title": "Paper 5 — DESI Chirality × Cosmic-Web Environment",
    "count": "7 figures",
    "items": [
      {
        "src": "/images/fig_p5_volume_fractions_pie.png",
        "alt": "In-footprint V-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283…",
        "number": "Figure 1 (fig:volfrac)",
        "title": "In-footprint V-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283…",
        "desc": "In-footprint V-Web volume fractions for the canonical (R_s=25 Mpc/h, _ th=0, N_ grid=256^3) run on 14,622,283 DESI DR1 spectroscopic galaxies. The cluster volume fraction (1.0\\%) reflects the high-density tail; the wall+filament fraction (74.5\\%) dominates as expected for galaxy-traced large-scale structure.",
        "source": "Paper 5 · v0.1.44"
      },
      {
        "src": "/images/fig_p5_cw_by_env_bar.png",
        "alt": "CW fraction per cosmic-web class on the canonical V-Web run, on n=791,635 chirality-relevant matched spirals",
        "number": "Figure 2 (fig:cw_by_env)",
        "title": "CW fraction per cosmic-web class on the canonical V-Web run, on n=791,635 chirality-relevant matched spirals",
        "desc": "CW fraction per cosmic-web class on the canonical V-Web run, on n=791,635 chirality-relevant matched spirals. Bars show the observed f_ CW per class; black error bars are 95\\% Jeffreys binomial credible intervals. The void bin (n=428) is dominated by counting noise and brackets parity. The dashed horizontal line is parity (f_ CW=0.5); the dotted red line is…",
        "source": "Paper 5 · v0.1.44"
      },
      {
        "src": "/images/fig_p5_cw_vs_density.png",
        "alt": "Density-quintile null with Paper IV monopole-prediction overlay",
        "number": "Figure 3 (fig:cw_vs_density)",
        "title": "Density-quintile null with Paper IV monopole-prediction overlay",
        "desc": "Density-quintile null with Paper IV monopole-prediction overlay. Left: CW fraction per projected-density quintile (k=5 NN proxy, N=158,327 per bin) with 95\\% Jeffreys binomial CIs; dashed parity f_ CW=0.5 and dotted Paper IV f_ CW=0.4974 references. Right: observed _ fromhalf per quintile (bars) vs the Paper IV-monopole prediction _ pred=-2Δ f_ CWN (red dia…",
        "source": "Paper 5 · v0.1.44"
      },
      {
        "src": "/images/fig_p5_healpix_skymap_nside32.png",
        "alt": "Per-pixel signed _ fromhalf for the chirality-relevant matched-spiral subsample at NSIDE=32 (Mollweide projec…",
        "number": "Figure 4 (fig:healpix_skymap)",
        "title": "Per-pixel signed _ fromhalf for the chirality-relevant matched-spiral subsample at NSIDE=32 (Mollweide projec…",
        "desc": "Per-pixel signed _ fromhalf for the chirality-relevant matched-spiral subsample at NSIDE=32 (Mollweide projection, equatorial coordinates). The observed |σ|^ obs_=4.13 vs the label-shuffle null |σ|^ null,p99_=4.78 gives a look-elsewhere p=0.135; no NSIDE returns p<0.05. The map shows no coherent large-scale structure beyond random pixel-level scatter; the h…",
        "source": "Paper 5 · v0.1.44"
      },
      {
        "src": "/images/fig_p5_phase2_sensitivity_heatmap.png",
        "alt": "Phase 2 sensitivity heat-map",
        "number": "Figure 5 (fig:healpix_skymap)",
        "title": "Phase 2 sensitivity heat-map",
        "desc": "Phase 2 sensitivity heat-map: per-cell range of f_ CW across the four environment classes \\void, wall, filament, cluster\\ in percentage points. Each cell corresponds to a complete V-Web re-run on the 14,622,283-galaxy DESI DR1 spectro sample at (R_s, _ th). The maximum range across all nine cells is 0.22percentage points (at R_s=25 Mpc/h, _ th=0.3). The hea…",
        "source": "Paper 5 · v0.1.44"
      },
      {
        "src": "/images/fig_p5_voids_vs_chirality_skymap.png",
        "alt": "HEALPix NSIDE = 32 Mollweide projection",
        "number": "Figure 6 (fig:voids_vs_chirality)",
        "title": "HEALPix NSIDE = 32 Mollweide projection",
        "desc": "HEALPix NSIDE = 32 Mollweide projection. Top: count of DESIVAST maximal voids per pixel (885 occupied pixels, median 4 voids/pix). Bottom: per-pixel chirality _ from\\ half on the z 0.24 matched-spiral subsample restricted to pixels with 200 spirals (1,496 valid pixels, σ range -3.45 to +3.48). The Pearson correlation across the n_ pix^ both = 727 pixels con…",
        "source": "Paper 5 · v0.1.44"
      },
      {
        "src": "/images/fig_p5_vweb_vs_tempel_overlay.png",
        "alt": "V-Web (left) vs Tempel+2014 FoF (right) cross-validation",
        "number": "Figure 7 (fig:tempel_overlay)",
        "title": "V-Web (left) vs Tempel+2014 FoF (right) cross-validation",
        "desc": "V-Web (left) vs Tempel+2014 FoF (right) cross-validation: per-class CW fraction with 95\\% Jeffreys binomial credible intervals, shared y-axis [0.43, 0.53]. Dashed reference is parity f_ CW=0.5; dotted-red reference is the Paper IV global f_ CW=0.4974 classifier-monopole offset. The highest-n concordance is the filament class pair: V-Web filament f_ CW=0.498…",
        "source": "Paper 5 · v0.1.44"
      }
    ]
  }
];
