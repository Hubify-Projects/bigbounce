# Project Timeline

Chronological history of the spin-torsion cosmology research program.

---

## Phase 0 — Genesis (2025-07 to 2025-11)

**Goal:** Develop a theoretical framework connecting Einstein-Cartan torsion to dark energy.

**What happened:**
- Initial 8,500-word draft exploring the spin-torsion bounce mechanism
- Framework built: ECH action, torsion integration yielding (J^5)^2 four-fermion interaction, modified Friedmann equations, quantum bounce at rho_crit ~ 0.27 rho_Pl
- Identified candidate observational signatures: galaxy spin asymmetry, cosmic birefringence, correlated dipole axes
- Version 0.1.0 (2025-07-15) through 0.2.0 (2025-11-10)

**Result:** Working theoretical framework with ambitious observational predictions.

**What changed:** Expanded from theory sketch to full paper with quantitative predictions.

---

## Phase 1 — Full Paper Build-Out (2025-11 to 2026-02)

**Goal:** Write a complete, submission-ready research paper.

**What happened:**
- Expanded to 32,000 words with 35 sections + 4 appendices
- Built interactive web presentation (index.html) with MathJax rendering
- Integrated 70+ papers from NASA ADS literature review
- Research squad (4 AI agents) contributed systematic analysis
- Versions 0.3.0 through 0.6.0

**Result:** Comprehensive manuscript covering framework, predictions, MCMC methodology, and observational connections.

**What changed:** Paper was ambitious but untested against internal consistency requirements.

---

## Phase 2 — Peer Review Gauntlet (2026-03-02 to 2026-03-04)

**Goal:** Make the paper scientifically defensible through adversarial self-review.

**What happened:**
- **Round 1** (2026-03-02): Self-audit found 10 critical/major issues. H_0 tension reduction claim was 1.4-sigma, not "resolved." Title downgraded from "breakthrough" framing.
- **Round 2** (2026-03-03): Structural audit added dimensional appendix and reproducibility appendix.
- **Round 3** (2026-03-03): Simulated Harsh Reviewer #2 — removed Omega_k from MCMC, deleted unsupported forecast section, downgraded all "predictions" to "MCMC fits."
- **Round 4** (2026-03-03): Skeptical coauthor simulation — renamed misleading terminology, added claims classification table (Appendix K), removed fictional artifacts (CNN classifier, CMB map analysis).
- **Round 5** (2026-03-03): Reproducibility audit — created 4 working Cobaya YAMLs, removed fiction about custom CAMB patches, added KNOWN_GAPS.md.
- **Round 6** (2026-03-04): Research agent literature sweep (148 papers) — 4 new citations added, vacuum dilution mechanism clarified.
- Versions 0.7.0 through 1.0.0

**Result:** Paper went from overclaimed to honest. Many original "predictions" were reclassified as "MCMC fits" or removed entirely. Claims table added. Version 1.0.0 marked "final v1.0."

**What changed:** Recognized that the core dark energy derivation was not on solid ground. Triggered deeper investigation.

---

## Phase 3 — MCMC Verification (2026-03-04 to 2026-03-12)

**Goal:** Run independent MCMC chains to verify claimed parameter fits.

**What happened:**
- Deployed on RunPod GPUs with Cobaya v3.6.1 + stock CAMB
- Ran 4 dataset combinations: planck_only, planck_bao, planck_bao_sn, full_tension
- Each with 5-6 independent chains for convergence diagnostics
- Versions 1.1.0 through 1.5.0

**Key results:**
- full_tension (175,840 samples, R-hat - 1 < 0.001): H_0 = 67.68 +/- 1.06, sigma_8 = 0.803 +/- 0.008, Delta-N_eff = -0.020 +/- 0.169
- planck_bao_sn (132,949 samples): Delta-N_eff = +0.065 +/- 0.17
- **Delta-N_eff consistent with zero** in all datasets — the bounce does not produce detectable dark radiation
- Earlier claim H_0 = 69.2 was artifact of SH0ES prior, not a genuine tension reduction

**Result:** MCMC pipeline works and is reproducible, but key positive claims from Paper 1 (tension reduction, dark radiation) were disproven by our own verification.

**What changed:** The original paper's main selling points (H_0 tension reduction, sigma_8 reduction) were dead. Required fundamental restructuring.

---

## Phase 4 — Derivation Closure Testing / IR Vacuum Program (2026-03-02 to 2026-03-13)

**Goal:** Test whether any of the 4 minimal routes to w = -1 actually work.

**What happened:**
- **Track B (Condensate route):** Wrong sign, too weak, catalysis suppressed, no rescue
- **Branch G v1 (One-loop route):** Fermion determinant gamma-independent at strict one-loop; no vacuum energy shift
- **Route T1 (Scalar reduction):** Reduces to standard ALP after torsion integration; no geometric content
- **Route S1 (ALP reduction):** Generic ALP birefringence; not ECH-specific

**Result:** All 4 minimal derivation routes are closed. The framework is definitively phenomenological at the minimal-model level. Compiled into `supplement_negative_results.pdf` (272 KiB).

**What changed:** Shifted from "derive dark energy" to "characterize what the framework CAN and CANNOT do."

---

## Phase 5 — Foundations A-G: Systematic Mechanism Testing (2026-03-13 to 2026-03-15)

**Goal:** Test every conceivable mechanism class for connecting the bounce to dark energy.

**What happened:**
- **Foundation A (PGT propagating torsion):** Mass-coupling lock — m and g tied by gravitational constant. Fine-tuning transferred, not eliminated. Graviton loop fine-tuning 1 in 10^57.
- **Foundation B (Lock-breaking via geometric ALP):** Topological-Shift Duality — mass protection and geometric content are mutually exclusive for pseudoscalar-4-form couplings.
- **Foundation C (Environmental mass):** Scalar-Tensor Universality — on FRW, all geometric scalars reduce to standard scalar-tensor EFT. T_0 = Q_0 = 0 washes out torsion/non-metricity.
- **Foundation D (Disformal couplings):** Planck Suppression — connection coupling gives 1 partial-phi per vertex (disformal needs 2). All distinctive effects bounded by O(1/M_Pl).
- **Foundation E (Global vacuum integrals):** Scale Separation — bounce V_4 / total V_4 ~ 10^{-60}. Bounce contribution negligible to global integrals.
- **Foundation F (Initial conditions):** Attractor-Sensitivity Dilemma — attractors erase initial conditions; without attractors, 10^{-30} precision fine-tuning required. No middle ground.
- **Foundation G (Cyclic vacuum selection):** Parameter Immunity — cyclic matching does not constrain action parameters. mu^4 remains free. Bounce provides infrastructure, not content.

**Result:** 7 independent structural barriers close all standard mechanism classes. Paper 1.2 restructured as honest closure assessment.

**What changed:** Full pivot away from dark energy derivation. Bounce and DE are independent problems.

---

## Phase 6 — Post-AG Pivot: Branches H-O (2026-03-15 to 2026-03-16)

**Goal:** Test bounce-only observables (tensor spectrum, perturbations, relics, state selection).

**What happened:**
- **Branch H (Tensor spectrum):** P_T ~ 10^{-64}, n_T = 0. Parity-even interaction, no chirality. Unobservable.
- **Branch I (Bounce-compatible DE):** Scale separation dominates. Ships passing in the night.
- **Branch J (State selection):** Barrier 9 — Liouville's theorem prevents state contraction.
- **Branch K (Scalar perturbations):** T(k) = 1 exactly for all observable modes. Time-reversal symmetry. No bounce-specific features.
- **Branch L (UV-IR bridge):** Barrier 10 — UV-IR specificity dilemma. 1 survivor: PGT lower-scale bounce (conditional).
- **Branch M (PGT GW spectrum):** Barrier 12 — vacuum amplification ceiling. Minimum detector gap: 10^17.
- **Branch N (Baryogenesis/relics):** Barrier 13 Face N — gravitational democracy. Torsion is 1 of ~100 Planck-scale channels.
- **Branch O (Hidden-sector vacuum):** Barrier 13 Face O — bounce-vacuum decoupling. Trigger and outcome structurally separated.

**Result:** 6 additional barriers (total: 13). The minimal ECH bounce is observationally inert at all tested scales.

**What changed:** Only extended/modified versions of the bounce could produce observable signals.

---

## Phase 7 — Branches P-W: Extensions, ALP, and Bounce Evidence (2026-03-16 to 2026-03-17)

**Goal:** Find any positive result — extend the model if necessary.

**What happened:**
- **Branch P (PGT lower-scale bounce):** Torsion relic cosmology gated on unknown energy fraction. Conditional.
- **Branch Q (Sourced parity violation):** Phenomenologically identical to standard ALP. No ECH-specific observable.
- **Branch R (ALP birefringence):** PROMISING. beta = 0.27 deg prediction matches 0.35 +/- 0.09 deg observation. MCMC Phase 2 initiated.
- **Branch S (Photon-torsion vertex):** ABJ anomaly is universal, not ECH-specific. beta ~ 10^{-30} deg. 28-40 orders too weak.
- **Branch T (Sourced axion bridge):** Requires free parameters (axial current). No genuine novelty.
- **Branch U (Two-field ALP + DE):** Speculative; deferred unless single-field ALP fails.
- **Branch V (Bounce evidence — generic matter-bounce (LQC-viable)):** FLAGSHIP CANDIDATE. Dust contraction through matter contraction produces f_NL = -35/8 = -4.375 (SPHEREx at 4-6σ, MegaMapper at 3-7σ), low-ell cutoff (Planck anomaly), scale-invariant spectrum.
- **Branch Vb (ECH perturbation gate):** Assessing perturbation propagation through ECH bounce.
- **Branch W (ALP curvaton tilt):** n_s = 1.000 from dust contraction (8.3-sigma excluded). Superseded by Branch V.

**Result:** Two positive paths identified: Branch R (ALP birefringence) and Branch V (generic matter-bounce (LQC-viable)).

**What changed:** Program has a genuine future direction for the first time since the closure era.

---

## Phase 8 — Next-Gen Bounce Signal Assessment (2026-03-17)

**Goal:** Can bounce-scale physics ever reach detectors?

**What happened:**
- **Next-gen bounce signals project:** 12 candidate signal classes evaluated. Chiral GW identified as best single target.
- **Chiral GW program (Phase 0):** Frequency gate FAILED. Bounce frequency today: 10^9 - 10^10 Hz (GHz). Detector gap to LIGO: 10^6. To LISA: 10^12. Five parametric windows tested — all dead. Bringing signal from GHz to mHz kills amplitude by 10^{-104}.

**Result:** All candidates relying on bounce-SCALE physics fail universally. Only contraction-phase signals (pre-bounce) reach observable frequencies, but those are generic.

**What changed:** Definitively confirmed that Branch V (contraction-phase signals through ECH bounce) is the right strategic direction, not bounce-scale signals.

---

## Current State (2026-03-17)

**Three active paths forward:**

1. **Paper 1 manuscript** — v1.6.0-preaudit. Structure: ECH framework + structural closure + spectator ALP birefringence + MCMC constraints + LiteBIRD forecast. Ready to write from locked claims and figure plan.

2. **Branch R (ALP birefringence MCMC)** — Phase 2 initiated. 25+ MCMC subdirectories. Target: publication-quality posteriors and Bayes factors.

3. **Branch V (Generic matter-bounce (LQC-viable))** — Phase 1 blueprint ready. Dust contraction → ECH bounce → radiation. Parameter-free prediction f_NL = -35/8 = -4.375. Tractable calculation extending Branch H tensor solver.

**Everything else is closed, deferred, or superseded.**
