import type { Metadata } from "next";
import Link from "next/link";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export const metadata: Metadata = {
  title: "Contributions",
  description:
    "Every novel contribution from the BigBounce research program ranked on the canonical N1–N4 novelty scale. Self-claim ceiling is N3 (first-of-kind). N4 (paradigm-shifting / Nobel-worthy) is reserved for outside arbiters and never self-claimed.",
};

type Tier = "N4" | "N3" | "N2" | "N1";

interface Contribution {
  id: string;
  tier: Tier;
  title: string;
  paper: string;
  oneLine: string;
  why?: string;
  what?: string;
  equation?: string;
  prior?: string;
  ours?: string;
  verify?: { label: string; href: string }[];
}

const TIER_LABEL: Record<Tier, string> = {
  N4: "PARADIGM-SHIFTING (RESERVED)",
  N3: "FIRST-OF-KIND DEMONSTRATION",
  N2: "NOVEL COMBINATION / EXTENSION",
  N1: "INCREMENTAL REFINEMENT / REPLICATION",
};

const TIER_DEF: Record<Tier, string> = {
  N4: "Paradigm-shifting / consensus-breaking / Nobel-worthy. Awarded by the field over time — never self-claimed by the authors.",
  N3: "First-of-kind demonstration, new constraint, or new direction that meaningfully opens or closes a measurable testbed. Ceiling for our self-claims.",
  N2: "Novel application or combination of existing methods — applying a known technique to a regime it hasn't seen, or combining pipelines to broaden what's measurable.",
  N1: "Incremental refinement or replication — tightens an existing measurement, fixes a known bias, or reproduces a prior result with a new dataset.",
};

const TIER_COLOR: Record<Tier, string> = {
  N4: "var(--tier-n4)",
  N3: "var(--tier-n3)",
  N2: "var(--tier-n2)",
  N1: "var(--tier-n1)",
};

const contributions: Contribution[] = [
  {
    id: "perturbation-transparency",
    tier: "N3",
    title: "Perturbation-Transparency Theorem",
    paper: "Paper 1A",
    oneLine:
      "All-orders proof that the Barbero-Immirzi parameter γ is invisible in every perturbative observable for minimally-coupled scalar matter in ECH.",
    why: "Tells you what the bounce CAN'T do: the bounce mechanism itself is invisible to telescopes. Every testable prediction must come from the contraction dynamics before the bounce, not from the bounce mechanism. This redirected the entire research program.",
    what: "5-step proof chain: zero spin density for scalar matter → zero torsion → Levi-Civita connection at all perturbative orders → Holst term reduces to topological Nieh-Yan invariant → no perturbative dynamics from γ. Extended to scalar, vector, AND tensor perturbations.",
    equation:
      "|ε^{μνρσ} R_{μνρσ}| < 10^{-15}  (numerical confirmation of Holst topological identity across 1000 random Riemann tensors with FRW perturbation symmetries)",
    prior:
      "Hehl et al. (1976); Freidel, Minic & Takeuchi (2005); Calcagni & Mercuri (2009); Mercuri (2009); de Berredo-Peixoto et al. (2012); Långvik et al.",
    ours:
      "No prior work combined the known ingredients into an explicit all-orders perturbation theorem for minimally coupled scalar matter in ECH. We formalized it as a 5-step theorem, proved it extends to tensors, verified numerically to machine precision.",
    verify: [
      {
        label: "verify_holst_vanishing.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/transparency_verification/verify_holst_vanishing.py",
      },
    ],
  },
  {
    id: "14-barriers",
    tier: "N3",
    title: "14-Constraint Channel-Level Closure Map",
    paper: "Paper 1A",
    oneLine:
      "Catalog of 14 independent structural constraints establishing channel-level closure, under stated assumptions, of the four enumerated minimal-ECH dark-energy routes.",
    why: "Closes every enumerated minimal route from a nonsingular ECH bounce to late-time dark energy under stated assumptions. Instead of testing one or two mechanisms and hoping, we systematically closed each channel. Tells future researchers exactly where NOT to look.",
    what: "7 foundation studies (A-G) + 17 research branches (H-W). Each barrier is named, quantified, and cross-referenced. Mass-coupling lock, Topological-Shift Duality, scalar-tensor universality, Planck suppression, attractor-sensitivity dilemma, parameter immunity, Liouville conservation, and 7 more.",
    equation:
      "g_eff ~ 10^{-61}  ·  Planck suppression 10^{-122}  ·  graviton-loop fine-tuning 10^{-57}  (across the barrier set)",
    prior:
      "Blagojević & Hehl (2013); Weinberg (1989); 't Hooft (1979); Shie, Nester & Yo (2008).",
    ours:
      "No prior work tested and closed all standard mechanism classes for connecting a nonsingular bounce to late-time dark energy within a single theoretical framework. Each branch opened only after passing a 4-question filter.",
    verify: [
      {
        label: "research/foundation_A_pgt through foundation_G",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research",
      },
    ],
  },
  {
    id: "matter-bounce-fnl",
    tier: "N3",
    title: "f_NL = -35/8 Forecast Package",
    paper: "Paper 2",
    oneLine:
      "First comprehensive forecast for testing Cai et al.'s matter-bounce non-Gaussianity prediction with upcoming surveys.",
    why: "Makes the bounce hypothesis testable. Cai et al. derived f_NL = -35/8 in 2009 but nobody built the full machinery to test it. We did: SPHEREx sensitivity, Bayesian model comparison, template mismatch quantification, robustness against systematics. SPHEREx data (~2028) will confirm or kill this at ~5σ.",
    what: "Parameter-free local non-Gaussianity from matter-dominated contraction: 300× larger than standard inflation, opposite sign. Forecast: σ(f_NL) = 0.7 (Heinrich+2023 multi-tracer Fisher); 3-5σ after systematic budget; 5.2-5.5σ optimistic pre-GR/b_φ degradation; 4.4σ at MegaMapper even at the worst convention.",
    equation: "f_NL^{local} = -35/8 = -4.375",
    prior:
      "Cai, Xue, Brandenberger & Zhang (2009); Heinrich, Doré & Krause (2023); Dalal et al. (2008); Li & Brandenberger (2014).",
    ours:
      "First combination of (a) SPHEREx + MegaMapper sensitivity specific to bounce; (b) Bayesian model comparison with 600K+ MC realizations (bounce favored at 8-17:1 over tuned multifield); (c) GR-projection robustness; (d) template-mismatch (r ≈ 0.85-0.90); (e) ε-correction bounded [1-8%]; (f) cubic bounce transmission estimate; (g) Li-Brandenberger convention resolution.",
    verify: [
      {
        label: "research/bayesian_discrimination_program/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/bayesian_discrimination_program",
      },
      {
        label: "algebraic_commutator_proof.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/matter_bounce_parameters/algebraic_commutator_proof.py",
      },
    ],
  },
  {
    id: "physics-commutator",
    tier: "N3",
    title: "Physics-Derived Full-Commutator Polynomial",
    paper: "Paper 2",
    oneLine:
      "Resolves a 15-year factor-of-2 ambiguity between Cai et al. (2009) and Li et al. (2017) by tracing it to the in-in commutator.",
    what: "Using Cai et al.'s own intermediate vertex contributions (Eqs. 34-36), we derive the full-commutator shape polynomial algebraically: (6, 2, -18, 10, -66, 18). Proven by exact rational arithmetic. Published Eq. 37 coefficients (3, 1, -9, 5, -66, 9) are the single-time-ordering values. The factor of 2 is the in-in commutator: i⟨[ζ³, L]⟩ = -2 Im⟨ζ³ L⟩.",
    why: "Two groups published different answers; nobody knew who was right. We proved both groups are correct at their respective levels. The exact polynomial determines how well SPHEREx can actually detect the signal.",
    equation:
      "Full-commutator polynomial: (6, 2, -18, 10, -66, 18)  ·  template overlap r ≈ 0.85-0.90",
    verify: [
      {
        label: "algebraic_commutator_proof.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/matter_bounce_parameters/algebraic_commutator_proof.py",
      },
    ],
  },
  {
    id: "alp-birefringence",
    tier: "N2",
    title: "ALP Birefringence Consistency",
    paper: "Paper 1A / Paper 2",
    oneLine:
      "ECH parity structure motivates a Planck-scale ALP. Predicted β = 0.27° matches the 3.6σ Planck+ACT observation at 0.5σ.",
    what: "Numerical ΛCDM ALP field evolution gives Δφ/f_a = 0.65-1.07 across the natural mass range m/H₀ ∈ [1, 3]. Fiducial β = 0.27° (at m ≈ 1.8H₀) is consistent with the published joint WMAP+Planck β = 0.342° ± 0.094° (3.6σ). NaMaster validation (synthetic ΛCDM skies, 500 MC): β = 0.27° recovered as 0.238° — a pipeline-validation figure, not a sky measurement.",
    why: "Our benchmark value sits within 1σ of an actual published observation. LiteBIRD tests at 9σ in early 2030s. Bounce-mechanism independent — falsification target separate from f_NL.",
    equation:
      "β = 0.27°  ·  consistent with Eskilt+ β = 0.342° ± 0.094° (3.6σ published detection)",
    verify: [
      {
        label: "alp_field_evolution/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/alp_field_evolution",
      },
    ],
  },
  {
    id: "topological-shift-duality",
    tier: "N2",
    title: "Topological-Shift Duality (Barrier 2)",
    paper: "Paper 1A",
    oneLine:
      "Mass protection and geometric content are mutually exclusive for pseudoscalar fields coupled to the Nieh-Yan 4-form.",
    what: "If Nieh-Yan is topological (standard EC), pseudoscalar mass is shift-symmetry protected but the coupling is a total derivative — no dynamics. If Nieh-Yan is non-topological (metric-affine), dynamics arise but shift symmetry breaks — no mass protection. Cannot have both.",
    why: "Closes a loophole that keeps coming up — people repeatedly try to build light pseudoscalars for dark energy from Nieh-Yan. Applies beyond our framework: constrains any attempt to use topological gravity terms as sources for light pseudoscalars.",
    verify: [
      {
        label: "foundation_B_lock_breaking/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/foundation_B_lock_breaking",
      },
    ],
  },
  {
    id: "chirality-catalog",
    tier: "N3",
    title: "3.2M-Spiral Galaxy Chirality Catalog (8.47M classified)",
    paper: "Paper 4",
    oneLine:
      "Largest chirality-labeled galaxy catalog to date: 8.47M DESI Legacy DR8 galaxies classified CW/CCW/NOT_SPIRAL (3,201,160 spirals) by a flip-equivariant ViT pipeline, with a null real-space chirality dipole.",
    what:
      "8,474,531 galaxies from DESI Legacy Survey DR8 classified by a flip-equivariant Vision Transformer ensemble with test-time D4 averaging (equivariance suppresses the raw classifier asymmetry 2.98×: +1.576% → −0.529% in A-units). Headline: real-space ℓ=1 dipole at +0.41σ (empirical-rank p=0.31) on the high-confidence sample (N=949,584) plus a block-bootstrap WLS template fit disfavoring a clean 1.7% Shamir-class dipole at z≈−18; injection-recovery brackets A95 in (1.0%, 1.5%].",
    why:
      "First chirality null at this scale with an honest falsification window. Constrains any cosmological parity-violating mechanism — including the early-universe consequences of ECH parity-odd structure beyond the ALP birefringence channel — and refutes the claimed ~3% parity signal.",
    equation:
      "Real-space dipole +0.41σ (rank-p = 0.31)  ·  WLS exclusion of 1.7% dipole at z ≈ −18  ·  A50 ≈ 0.75%, A95 ∈ (1.0%, 1.5%]",
    verify: [
      {
        label: "bamfai/galaxy-chirality-catalog (HuggingFace)",
        href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
      },
      {
        label: "chirality_catalog_paper.pdf",
        href: "/papers/chirality_catalog_paper.pdf",
      },
    ],
  },
  {
    id: "anomaly-catalog",
    tier: "N3",
    title: "Multi-Survey Anomaly Catalog (378,280 anomalies)",
    paper: "Paper 3",
    oneLine:
      "First unified anomaly sweep across 7 surveys (37.3M sources): 378,280 unique anomalies (269,317 recommended-tier) after Path-C native retrains and 7-way 5″ positional dedup. The ~141× figure over prior catalogs is a full-instrument-stream vs science-target comparison, not a like-for-like size increase — the like-for-like DESI recount is ≈0.9× the largest single-survey benchmark (2,468 vs 2,685).",
    what:
      "Path-C native-retrained per-survey tallies: DESI DR1 (195,829), SDSS DR18 (77,905), LAMOST DR10 (113,342, exploratory tier), eROSITA DR1 (298), Planck CMB (200), Gaia DR3 (500), NEOWISE (419, after the |b_ecl|<80° ecliptic-pole mask; 436 pre-mask). These sum to 388,493 raw → 378,280 unique after 7-way friends-of-friends union-find at 5″ (10,213 duplicate detections collapsed). Enrichment statistics (e.g. eROSITA) are reported descriptively, not as inferential significances.",
    why:
      "Cross-survey continuity is the load-bearing falsification surface for any new physics claim. Population-level rare-class discovery (z>6 QSOs, ultra-rare AE candidates) is the byproduct.",
    verify: [
      {
        label: "pipelines/p3_anomaly_engine/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p3_anomaly_engine",
      },
    ],
  },
  {
    id: "spherex-fisher",
    tier: "N2",
    title: "SPHEREx f_NL Fisher Forecast",
    paper: "Paper 2",
    oneLine:
      "Multi-tracer Fisher forecast of σ(f_NL) = 0.7 → 4.7-12σ detection of bounce f_NL = -4.375 by 2027.",
    equation:
      "σ(f_NL) = 0.36 (Fisher ideal)  ·  σ(f_NL) = 0.93 (Munchmeyer+2019 conservative)  ·  detection 4.7-12σ",
    what:
      "Externalized to Heinrich+2023 multi-tracer bispectrum forecast with the bounce template; noise-weighted shape mismatch, ε-correction, b_φ marginalization, GR projection all carried through.",
    why:
      "Sets a hard deadline on falsification — SPHEREx will report by ~2027-2028.",
    verify: [
      {
        label: "research/focused_paper_source_integration/02_full_draft.tex",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/focused_paper_source_integration/02_full_draft.tex",
      },
    ],
  },
  {
    id: "desi-environment",
    tier: "N3",
    title: "DESI Chirality × Environment Null (z-shell corrected)",
    paper: "Paper 5",
    oneLine:
      "Galaxy chirality is statistically independent of DESI large-scale-structure environment: 791,635 matched spirals + 56,981 void spirals, with a z-shell selection correction and full covariate robustness.",
    what:
      "Matched 2,232,212 deduped DESI DR1 rows against the Paper-4 chirality catalog (duplicate-TARGETID join root-caused and rebuilt; 100% GZ–DESI join). DESIVAST three-algorithm void test, V-Web + T-Web + Tempel + ASTRA cross-checks, 21-shell z-shell selection-corrected rebuild, omnibus χ² environment nulls (p=0.31/0.99), and covariate-robust regression over size/magnitude/morphology/inclination (Wald p=0.46/0.99).",
    why:
      "Cosmic-web environment is the most natural place to look for spin alignment / handedness correlations. The controlled non-detection constrains the whole class of environment-coupled parity models at the ≳25 Mpc/h smoothing scale.",
    equation:
      "Omnibus χ² nulls p = 0.31 / 0.99  ·  covariate-robust Wald p = 0.46 / 0.99  ·  no class clears Bonferroni significance under any classifier",
    verify: [
      {
        label: "pipelines/p5_desi_chirality/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p5_desi_chirality",
      },
    ],
  },
  {
    id: "mcmc-verification",
    tier: "N2",
    title: "MCMC Verification Infrastructure (309,189 frozen samples)",
    paper: "Paper 1B",
    oneLine:
      "309,189 frozen posterior samples across 2 converged dataset combinations (third accumulating). Honest null: ΔN_eff ≈ 0, H₀ = 67.68 (standard ΛCDM); DESI DR2 w0wa chain gives w_pivot = −0.952 ± 0.019 (+2.5σ from −1, twice-verified).",
    what:
      "Cobaya 3.6.1 + CAMB. Frozen combinations: 176,240 full-tension + 132,949 Planck+BAO+SN, Gelman-Rubin converged. A separate DESI DR2 BAO + Planck NPIPE + DES-Y5 + Pantheon+ w0wa chain reports w_pivot at the decorrelated pivot. Corrected our own earlier artifact (H₀ = 69.2 was a SH0ES prior artifact).",
    why: "Demonstrates honest negative reporting — we found our own bug and disclosed it.",
    verify: [
      {
        label: "reproducibility/cosmology/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility/cosmology",
      },
    ],
  },
  {
    id: "pta-bounce",
    tier: "N2",
    title: "NANOGrav Bounce GW Spectrum",
    paper: "Paper 3, §6",
    oneLine:
      "NANOGrav 15-yr real-KDE free-spectrum re-fit: γ = 2.567 ± 0.382. Matter-bounce γ = 3.0 consistent at +1.13σ; SMBHB γ = 4.33 excluded at +4.61σ.",
    what:
      "Real free-spectrum KDE likelihood (Zenodo chains, emcee re-fit; ESS = 5,507) replacing the earlier synthetic-power-law summary statistic γ = 3.20 ± 0.42. Savage-Dickey Bayes factor decisively favors the bounce slope over the SMBHB slope.",
    why:
      "The PTA spectral slope is one of the few currently-measured observables that discriminates bounce-era tensor spectra from astrophysical SMBHB backgrounds.",
    equation:
      "γ_bounce = 3.0 (+1.13σ consistent)  ·  γ_obs = 2.567 ± 0.382  ·  γ_SMBHB = 4.33 (+4.61σ excluded)",
  },
  {
    id: "namaster-validation-suite",
    tier: "N2",
    title: "NaMaster Pipeline Validation Suite",
    paper: "Paper 1B / Paper 4",
    oneLine:
      "End-to-end pseudo-C_ℓ validation harness: 500-MC birefringence recovery on synthetic ΛCDM skies (P1B) plus MASTER-deconvolved chirality-field nulls with harmonic completeness anchors (P4).",
    what:
      "P1B leg: synthetic ΛCDM polarization skies, ACT-like f_sky = 0.32 mask, 10 μK·arcmin noise, 500 MC — injected β = 0.27° recovered as 0.238° (bias −0.032°, sign-symmetric; σ_β(0.32) = 0.046° measured directly). Scope honestly declared: validates the E→B MASTER deconvolution, not the β–α foreground degeneracy. P4 leg: monopole-only generative nulls (99.3% of pre-MASTER ℓ=1 power), label-shuffle backgrounds, and injection completeness — a Shamir-class 1.7% dipole would recover at z ≈ 68–218 vs the observed +7.3.",
    why:
      "Mask-coupled pseudo-C_ℓ pipelines silently manufacture or destroy low-ℓ signals; a committed, rerunnable validation suite is what separates a believable null from an artifact.",
    equation:
      "β bias = −0.032° (500 MC, synthetic skies)  ·  monopole-only null reproduces 99.3% of pre-MASTER ℓ=1 power",
  },
  {
    id: "provenance-audit",
    tier: "N2",
    title: "Provenance-Audit Methodology (retract-and-rebuild)",
    paper: "Paper 4 / program-wide",
    oneLine:
      "A data-provenance audit traced P4's previously-headlined −0.122σ subsample-mask null to a synthetic-footprint catalog; the result was withdrawn, the paper re-anchored on real-space estimators, and the audit trail published.",
    what:
      "Artifact-level provenance tracing (file hashes, generation scripts, footprint geometry checks) applied to every load-bearing null. When the audit failed, the claim was withdrawn in-paper (P4 Appendix A), the headline was rebuilt on the real-space +0.41σ dipole + WLS template exclusion, and the corrected equivariance suppression factor (3.86× → 2.98×) was propagated through every surface. P2's irreproducible ~9.9σ SDB joint-Fisher claim was withdrawn the same way and replaced by a committed-code 1.4σ/0.6σ subordinate channel.",
    why:
      "Most published nulls and detections never face an artifact-level audit. Treating retraction-and-rebuild as a first-class, documented workflow is itself a transparency contribution — reviewers can replay the exact decision chain.",
  },
  {
    id: "compute-reproducibility-chain",
    tier: "N2",
    title: "12-Job Compute Reproducibility Chain",
    paper: "Program-wide",
    oneLine:
      "All 12 load-bearing compute closures (fsky sweeps, continuous-prior MCMC, permutation rebuilds, sign-symmetry reruns) executed on a dedicated pod with committed scripts + JSON artifacts, for ~$0.55 total.",
    what:
      "Each job ships its driver script, inputs, seeds, and output artifact in-repo; results are stamped into the papers via the \\artifact{} macro pointing at immutable release tags. The chain covers P1B (fsky sweep, Caγ continuous-prior MCMC, c9f sign-symmetry), P4 (10k-permutation Table III rebuild, harmonic completeness injections), and P5 (closure-recompute scripts 17–19).",
    why:
      "A reviewer can rerun any headline number from the committed chain — reproducibility as an artifact, not a promise.",
    verify: [
      {
        label: "h200_scripts/experiments/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/h200_scripts/experiments",
      },
    ],
  },
  {
    id: "bigae-anomaly-detector",
    tier: "N2",
    title: "BigAE Multi-Survey Autoencoder Anomaly Detector",
    paper: "Paper 3",
    oneLine:
      "A deterministic symmetric autoencoder trained per-survey on native data, scoring 269,317 objects across 6 surveys by reconstruction residual — the largest-by-sources autoencoder anomaly search assembled for cosmological-anomaly discovery.",
    why: "Turns 'anomaly' from a hand-tuned cut into a learned, survey-native reconstruction score, so one pipeline scales across heterogeneous surveys and every headline count is reproducible from committed scripts rather than a promise.",
    what:
      "Per-survey NATIVE retrains (the cross-transfer failure mode — a LAMOST-trained model drifts to an ~98% blue-excess artifact on other surveys — forced a native-retrain protocol); standardized reconstruction-residual score S. Validated not by injection-recovery but by a 5-fold cross-validation robustness gate (mean pairwise Jaccard 0.862) plus an out-of-distribution Jaccard gate — a validation methodology for UNSUPERVISED anomaly catalogs. UMAP of the latent space shows the high-score anomalies concentrate in distinct islands rather than scattering.",
    prior:
      "Autoencoder outlier detection (Baron & Poznanski 2017); single-survey spectral anomaly searches.",
    ours:
      "No prior work combined per-survey-native autoencoder retrains into a single 6-survey reconstruction-scored anomaly catalog at this scale, with a cross-validation/OOD validation gate replacing injection-recovery for an unsupervised search. Model + catalog released open-source.",
    verify: [
      {
        label: "6-way dedup artifact (EXACT-MATCH)",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p3_anomaly_engine/outputs/sixway_dedup_artifact.json",
      },
      {
        label: "bamfai/desi-spectral-anomaly-detector (model)",
        href: "https://huggingface.co/bamfai/desi-spectral-anomaly-detector",
      },
      {
        label: "bamfai/bigbounce-anomaly-catalog (dataset)",
        href: "https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog",
      },
    ],
  },
  {
    id: "chirality-equivariant-classifier",
    tier: "N2",
    title: "Z₂-Flip-Equivariant Chirality Classifier (released model)",
    paper: "Papers 4 & 5",
    oneLine:
      "A flip-equivariant Vision Transformer that classifies galaxy spin handedness with parity symmetry built into the architecture — the correct inductive bias for a parity-violation measurement — with D4 test-time averaging giving 2.98× systematic-dipole suppression. Checkpoint released on HuggingFace.",
    why: "For a chirality-DIPOLE measurement, an ordinary classifier can bake in an orientation bias that manufactures a signal; making the network exactly equivariant under the parity flip removes that entire class of systematic by construction rather than by post-hoc correction.",
    what:
      "ViT-Small backbone with Z₂-flip equivariance enforced so CW↔CCW predictions transform correctly under image reflection; D4 (dihedral) test-time averaging suppresses residual orientation systematics 2.98×; calibrated on Galaxy Zoo 1 labels. Released as bamfai/galaxy-chirality-v2 with weights.",
    prior:
      "CNN/ViT galaxy-morphology classifiers (Galaxy Zoo DECaLS, Zoobot); standard non-equivariant chirality classifiers (Shamir et al.).",
    ours:
      "First use of a built-in parity-equivariant classifier for a cosmological chirality-dipole measurement, with the equivariance itself as the systematic-control mechanism; model + weights released for reuse.",
    verify: [
      {
        label: "bamfai/galaxy-chirality-v2 (model)",
        href: "https://huggingface.co/bamfai/galaxy-chirality-v2",
      },
      {
        label: "bamfai/galaxy-chirality-catalog (dataset)",
        href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
      },
    ],
  },
  {
    id: "gz1-only-independence",
    tier: "N2",
    title: "Pseudo-Label-Independence Retrain (GZ1-only null)",
    paper: "Paper 4",
    oneLine:
      "A control classifier trained on Galaxy Zoo 1 human labels ONLY (zero CE-ResNet pseudo-labels; val acc 0.978) reproduces the chirality-dipole null at z = −0.04σ — proving the vanishing dipole is not an artifact inherited from the pseudo-labels.",
    why: "Directly answers the strongest circularity objection to a null from a partly-pseudo-labeled classifier: retrain on fully-independent human supervision and check the physical null survives. It does.",
    what:
      "Retrained the equivariant ViT on GZ1 CW/CCW human labels only (CE-ResNet pseudo-label block gated off), re-inferred the galaxy sample, and ran the IDENTICAL real-space dipole estimator + per-pixel permutation null: z = −0.04σ (rank-p = 0.45), consistent with the canonical +0.41σ null.",
    prior:
      "Self-training / pseudo-label validation typically checks classifier accuracy, not downstream-measurement independence.",
    ours:
      "A downstream-MEASUREMENT pseudo-label-independence test: retrain on fully-independent supervision and confirm the physical null (not merely accuracy) survives — a reusable template for validating ML-derived cosmological null results.",
    verify: [
      {
        label: "gz1only_dipole_result.json",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/outputs/gz1only_dipole_result.json",
      },
      {
        label: "bamfai/galaxy-chirality-v2 (gz1only ckpt)",
        href: "https://huggingface.co/bamfai/galaxy-chirality-v2/tree/main/gz1only",
      },
    ],
  },
];

function ContributionCard({ c }: { c: Contribution }) {
  const color = TIER_COLOR[c.tier];
  return (
    <Card
      id={c.id}
      style={{
        padding: 20,
        borderLeft: `3px solid ${color}`,
        scrollMarginTop: 80,
      }}
    >
      <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: 10 }}>
        <span
          style={{
            display: "inline-block",
            padding: "2px 8px",
            borderRadius: 4,
            background: color,
            color: "#fff",
            fontFamily: "var(--font-mono-stack)",
            fontSize: 10,
            fontWeight: 700,
            letterSpacing: 0.4,
          }}
        >
          {TIER_LABEL[c.tier]}
        </span>
        <span
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: 11,
            color: "var(--text-muted)",
          }}
        >
          {c.paper}
        </span>
      </div>
      <h3
        style={{
          marginTop: 10,
          marginBottom: 6,
          fontFamily: "var(--font-mono-stack)",
          fontSize: 16,
          fontWeight: 600,
        }}
      >
        {c.title}
      </h3>
      <p style={{ marginTop: 0, fontSize: 13, lineHeight: 1.6 }}>{c.oneLine}</p>
      {c.equation && (
        <div
          style={{
            marginTop: 10,
            padding: "8px 12px",
            background: "color-mix(in srgb, var(--accent) 6%, var(--surface))",
            borderLeft: "2px solid var(--accent)",
            fontFamily: "var(--font-mono-stack)",
            fontSize: 12,
            lineHeight: 1.6,
          }}
        >
          {c.equation}
        </div>
      )}
      <h4 style={{ marginTop: 14, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
        Why it matters
      </h4>
      <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.why}</p>
      <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
        What it is
      </h4>
      <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.what}</p>
      {c.prior && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            What existed before
          </h4>
          <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.prior}</p>
        </>
      )}
      {c.ours && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            What we did
          </h4>
          <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.ours}</p>
        </>
      )}
      {c.verify && c.verify.length > 0 && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            How to verify
          </h4>
          <ul style={{ margin: 0, paddingLeft: 18, fontSize: 13, lineHeight: 1.8 }}>
            {c.verify.map((v) => (
              <li key={v.href}>
                <a
                  href={v.href}
                  target={v.href.startsWith("http") ? "_blank" : undefined}
                  rel="noopener noreferrer"
                  style={{ color: "var(--accent)", fontFamily: "var(--font-mono-stack)", fontSize: 12, overflowWrap: "anywhere" }}
                >
                  {v.label}
                </a>
              </li>
            ))}
          </ul>
        </>
      )}
    </Card>
  );
}

export default function ContributionsPage() {
  const grouped: Record<Tier, Contribution[]> = { N4: [], N3: [], N2: [], N1: [] };
  for (const c of contributions) grouped[c.tier].push(c);
  const counts = {
    N4: grouped.N4.length,
    N3: grouped.N3.length,
    N2: grouped.N2.length,
    N1: grouped.N1.length,
  };
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Novelty accounting
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          contributions
        </h1>
        <p className="subtitle">
          Each contribution is scored on the canonical four-tier novelty scale.
          Our self-claim ceiling is <strong>N3</strong> (first-of-kind
          demonstration). <strong>N4</strong> — paradigm-shifting / Nobel-worthy —
          is intentionally reserved for outside arbiters and is never
          self-claimed. Definitions, prior work, and verification links below.
        </p>
      </div>

      <section id="program-arc" style={{ marginTop: 28 }}>
        <p
          className="eyebrow"
          style={{ marginBottom: 8 }}
        >
          How the six papers fit together
        </p>
        <p style={{ marginTop: 0, fontSize: 14, lineHeight: 1.7, maxWidth: "64ch" }}>
          One program, two halves. The <strong>theory arm</strong> (P1A, P1B, P2)
          asks where a nonsingular Einstein–Cartan–Holst bounce could leave a
          falsifiable fingerprint, proves the bounce mechanism itself is invisible
          to telescopes, closes the enumerated dark-energy routes, and isolates the
          one surviving handle — a parameter-free matter-bounce non-Gaussianity
          SPHEREx can test. The <strong>data arm</strong> (P3, P4, P5) mines 45M+
          archival sources for the parity- and anomaly-level signatures any bounce
          would have to imprint, and reports honest nulls with quantified
          falsification windows. Negative theory results narrowed the search space;
          the surveys then went looking exactly where the theory said to look.
        </p>
        <div style={{ display: "grid", gap: 0, marginTop: 16 }}>
          {[
            { n: "P1A", role: "ECH theory + no-go: perturbation-transparency theorem and a 14-constraint channel-level closure of the four minimal bounce→dark-energy routes." },
            { n: "P1B", role: "MCMC + pipeline companion: frozen ΛCDM+ΔN_eff chains (honest null), NaMaster recovery, and an ALP-birefringence consistency check." },
            { n: "P2", role: "f_NL = −35/8 forecast: the surviving falsifiable handle — matter-bounce non-Gaussianity, ~300× inflation and opposite sign, testable by SPHEREx at 3–5σ." },
            { n: "P3", role: "Multi-survey anomaly catalog: 378,280 unique anomalies across 7 surveys + a NANOGrav free-spectrum slope consistent with matter-bounce γ = 3.0." },
            { n: "P4", role: "Galaxy chirality null: 8.47M classified galaxies, a null +0.41σ real-space dipole, refuting the claimed ~3% parity signal at scale." },
            { n: "P5", role: "DESI chirality × environment null: spiral handedness is independent of cosmic-web environment, constraining environment-coupled parity models." },
          ].map((p, i) => (
            <div
              key={p.n}
              style={{
                display: "grid",
                gridTemplateColumns: "56px 1fr",
                gap: 14,
                alignItems: "baseline",
                padding: "10px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--border)",
              }}
            >
              <span
                style={{
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: 13,
                  fontWeight: 700,
                  color: "var(--accent)",
                }}
              >
                {p.n}
              </span>
              <span style={{ fontSize: 13, lineHeight: 1.6 }}>{p.role}</span>
            </div>
          ))}
        </div>
        <p style={{ marginTop: 12, fontSize: 12.5, lineHeight: 1.6, color: "var(--text-muted)" }}>
          Program arc: P1A (ECH theory / no-go) → P1B (MCMC + pipeline companion) →
          P2 (f_NL forecast) → P3 (anomaly catalog) + P4 (chirality null) +
          P5 (DESI chirality × environment). See the{" "}
          <Link href="/paper" style={{ color: "var(--accent)" }}>
            six papers
          </Link>{" "}
          for full status and PDFs.
        </p>
      </section>

      <section
        id="tier-scale"
        style={{
          marginTop: 24,
          padding: 16,
          border: "1px solid var(--border)",
          borderRadius: 8,
          background: "var(--surface)",
        }}
      >
        <div
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: 10,
            textTransform: "uppercase",
            letterSpacing: 0.8,
            color: "var(--text-muted)",
            marginBottom: 10,
          }}
        >
          Novelty tier scale
        </div>
        <div style={{ display: "grid", gap: 8 }}>
          {(["N4", "N3", "N2", "N1"] as Tier[]).map((tier) => {
            const isReserved = tier === "N4";
            return (
              <div
                key={tier}
                style={{
                  display: "grid",
                  gridTemplateColumns: "auto 1fr auto",
                  alignItems: "center",
                  gap: 12,
                  padding: "8px 10px",
                  borderLeft: `3px solid ${TIER_COLOR[tier]}`,
                  background: isReserved
                    ? "color-mix(in srgb, #b91c1c 5%, var(--surface))"
                    : "transparent",
                  opacity: isReserved ? 0.85 : 1,
                }}
              >
                <span
                  style={{
                    display: "inline-block",
                    padding: "2px 8px",
                    borderRadius: 4,
                    background: TIER_COLOR[tier],
                    color: "#fff",
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 10,
                    fontWeight: 700,
                    letterSpacing: 0.4,
                    minWidth: 28,
                    textAlign: "center",
                  }}
                >
                  {tier}
                </span>
                <span style={{ fontSize: 12, lineHeight: 1.5 }}>
                  <strong
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 11,
                      letterSpacing: 0.4,
                      color: TIER_COLOR[tier],
                    }}
                  >
                    {TIER_LABEL[tier]}
                  </strong>
                  {" — "}
                  {TIER_DEF[tier]}
                </span>
                <span
                  style={{
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 11,
                    color: "var(--text-muted)",
                    minWidth: 50,
                    textAlign: "right",
                  }}
                >
                  {isReserved ? "reserved" : `${counts[tier]} item${counts[tier] === 1 ? "" : "s"}`}
                </span>
              </div>
            );
          })}
        </div>
      </section>

      <div className="contrib-layout">
        <aside className="contrib-layout-aside" style={{ position: "sticky", top: 80, alignSelf: "start" }}>
          <div
            style={{
              fontFamily: "var(--font-mono-stack)",
              fontSize: 10,
              textTransform: "uppercase",
              letterSpacing: 0.8,
              color: "var(--text-muted)",
              marginBottom: 8,
            }}
          >
            By tier
          </div>
          {(["N4", "N3", "N2", "N1"] as Tier[]).map((tier) => (
            <a
              key={tier}
              href={`#tier-${tier}`}
              style={{
                display: "block",
                padding: "6px 10px",
                marginBottom: 4,
                fontFamily: "var(--font-mono-stack)",
                fontSize: 12,
                color: "var(--text)",
                textDecoration: "none",
                borderLeft: `2px solid ${TIER_COLOR[tier]}`,
              }}
            >
              <span style={{ color: TIER_COLOR[tier], fontWeight: 700 }}>{tier}</span>
              {" — "}
              {tier === "N4" ? "reserved" : `${counts[tier]} item${counts[tier] === 1 ? "" : "s"}`}
            </a>
          ))}
          <div
            style={{
              fontFamily: "var(--font-mono-stack)",
              fontSize: 10,
              textTransform: "uppercase",
              letterSpacing: 0.8,
              color: "var(--text-muted)",
              marginTop: 18,
              marginBottom: 8,
            }}
          >
            All contributions
          </div>
          {contributions.map((c) => (
            <a
              key={c.id}
              href={`#${c.id}`}
              style={{
                display: "block",
                padding: "4px 10px",
                fontFamily: "var(--font-mono-stack)",
                fontSize: 11,
                color: "var(--text-muted)",
                textDecoration: "none",
                lineHeight: 1.4,
              }}
            >
              {c.title}
            </a>
          ))}
          <Link
            href="/old/contributions.html"
            style={{
              display: "block",
              marginTop: 20,
              padding: "8px 10px",
              fontFamily: "var(--font-mono-stack)",
              fontSize: 11,
              color: "var(--accent)",
              textDecoration: "none",
              border: "1px solid var(--border)",
              borderRadius: 6,
            }}
          >
            ↗ full legacy contributions page
          </Link>
        </aside>

        <div style={{ display: "grid", gap: 14 }}>
          <section id="tier-N4" style={{ scrollMarginTop: 80 }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 10,
                marginBottom: 12,
              }}
            >
              <Badge variant="outline" className="font-mono text-[10px]">
                N4
              </Badge>
              <h2
                style={{
                  margin: 0,
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: 14,
                  textTransform: "uppercase",
                  letterSpacing: 0.6,
                  color: TIER_COLOR.N4,
                }}
              >
                {TIER_LABEL.N4}
              </h2>
            </div>
            <Card
              style={{
                padding: 20,
                borderLeft: `3px solid ${TIER_COLOR.N4}`,
                background: "color-mix(in srgb, #b91c1c 4%, var(--surface))",
              }}
            >
              <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>
                <strong>Intentionally empty.</strong> N4 is reserved for
                paradigm-shifting, consensus-breaking, or Nobel-worthy results.
                That tier is awarded by the field over time — through broad
                community replication, citation, and consensus — not by the
                authors. We cap our own claims at N3 (first-of-kind
                demonstration / new constraint / new direction) and let outside
                arbiters raise the ceiling if any of this work earns it.
              </p>
              <p
                style={{
                  marginTop: 10,
                  marginBottom: 0,
                  fontSize: 12,
                  lineHeight: 1.6,
                  color: "var(--text-muted)",
                }}
              >
                No BigBounce paper self-annotates at N4. Site copy, paper abstracts,
                and all contribution records are capped at N3 by internal review.
              </p>
            </Card>
          </section>

          {(["N3", "N2", "N1"] as Tier[]).map(
            (tier) =>
              grouped[tier].length > 0 && (
                <section key={tier} id={`tier-${tier}`} style={{ scrollMarginTop: 80 }}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: 10,
                      marginBottom: 12,
                    }}
                  >
                    <Badge variant="outline" className="font-mono text-[10px]">
                      {tier}
                    </Badge>
                    <h2
                      style={{
                        margin: 0,
                        fontFamily: "var(--font-mono-stack)",
                        fontSize: 14,
                        textTransform: "uppercase",
                        letterSpacing: 0.6,
                        color: TIER_COLOR[tier],
                      }}
                    >
                      {TIER_LABEL[tier]}
                    </h2>
                  </div>
                  <div style={{ display: "grid", gap: 14 }}>
                    {grouped[tier].map((c) => (
                      <ContributionCard key={c.id} c={c} />
                    ))}
                  </div>
                </section>
              ),
          )}
        </div>
      </div>
    </>
  );
}
