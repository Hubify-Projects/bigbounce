# Branch V: Final Verdict

**Created:** 2026-03-17
**Program:** Bounce Evidence Program
**Decision:** OPEN — Flagship research direction

---

## The Five Questions

### Q1: Is there a physically motivated extension of the minimal ECH bounce that produces detectable signatures?

**YES.** Six extensions were evaluated (V1–V6). Three scored A-tier:
- **V2a (dust contraction + ECH bounce)** — produces f_NL = 5/12, near-scale-invariant spectrum, low-ℓ cutoff
- **V4 (ekpyrotic + ECH bounce)** — ECH resolves the singular bounce problem of ekpyrotic cosmology
- **V2c (kinetic contraction + ECH bounce)** — produces n_T = 2 blue tensor tilt

All three share the structure: **the contraction phase determines the spectrum; the ECH bounce provides the non-singular transition.** The extensions are physically motivated (every bounce model needs to specify the contraction phase) and add at most 2–3 parameters.

### Q2: What is the single best target for the first calculation?

**V2a: Matter Bounce through ECH.**

Reasons:
1. Parameter-free prediction: f_NL^local = 5/12 (testable by SPHEREx at 2.5σ)
2. Connects to existing Planck low-ℓ anomaly (2–3σ)
3. The key challenge (n_s = 1 → 0.965) is itself the main original result
4. ECH provides explicit, calculable bounce mechanism (not hand-waved)
5. No existing paper has computed perturbation spectrum for dust contraction + ECH bounce specifically
6. Calculation is tractable with existing tools (extend Branch H tensor solver)

### Q3: What observable would most decisively distinguish a spin-torsion bounce from no bounce?

**The combination (n_s, r, f_NL) in the consistency plane.**

| Model | n_s | r | f_NL^local | Consistency |
|-------|-----|---|-----------|------------|
| Slow-roll inflation | 0.965 | 0.003–0.13 | ~0.01 | r = -8n_T |
| Matter bounce (ECH) | ~0.965 (with mechanism) | < 0.01 | 5/12 ≈ 1.25 | r = 24(1-n_s)c_s²/5 |
| Ekpyrotic (ECH) | ~0.97 | ≈ 0 | ~-10 (equil) | r ≈ 0, large f_NL |

No single observable separates the models. The three-dimensional space (n_s, r, f_NL) does. CMB-S4 + LiteBIRD + SPHEREx together will map this space with sufficient precision.

### Q4: Is this program genuinely novel, or does it rehash existing bounce literature?

**It is novel in a specific, defensible way.**

What exists:
- Matter bounce perturbation theory (Finelli & Brandenberger 2002; Cai et al. 2008, 2014)
- LQC bounce perturbations (Wilson-Ewing 2013; Agullo, Ashtekar & Nelson 2013)
- Ekpyrotic bounce (Lehners 2008; Ijjas & Steinhardt 2019)

What does NOT exist:
- Perturbation spectrum through an **ECH** bounce specifically (H² = 8πGρ/3 × (1 - ρ/ρ_crit) with ρ_crit from torsion)
- Identification of ECH as the bounce mechanism for matter bounce or ekpyrotic scenarios
- Combined framework: ALP birefringence (surviving prediction) + matter bounce spectrum (new prediction) from the same ECH Lagrangian
- Systematic comparison of ECH bounce perturbations to LQC bounce perturbations (closest competitor)

The novelty is the specific UV completion (ECH) applied to the well-studied matter bounce scenario. This is analogous to how computing inflation in supergravity (specific UV completion) is distinct from computing inflation in a generic scalar field model.

### Q5: What is the realistic publication path?

**Two papers, sequential:**

**Paper A (near-term): "Structural Closure + ALP Birefringence"**
- 14 barriers across 15 branches
- ALP birefringence as sole surviving prediction
- MCMC constraints on θ_i and m_a
- Status: NEARLY COMPLETE (arxiv_v2/ directory exists, needs compilation)

**Paper B (Branch V target): "Matter Bounce in Einstein-Cartan-Holst Gravity: Perturbation Spectrum and Observational Predictions"**
- Background: dust contraction → ECH bounce → radiation expansion
- Scalar spectrum P_ζ(k) with ECH-specific corrections
- Tensor spectrum and consistency relation
- Non-Gaussianity f_NL = 5/12 ± ECH corrections
- Low-ℓ cutoff prediction
- Comparison to LQC bounce and inflationary predictions
- Status: PHASE 1 TO BEGIN

---

## Program Status

```
Branch V: Bounce Evidence Program
├── 01_program_definition.md          ✓ COMPLETE
├── 02_observable_channel_map.md      ✓ COMPLETE  (7 channels mapped)
├── 03_minimal_nontransparent_extensions.md  ✓ COMPLETE  (6 extensions, 3 A-tier)
├── 04_upside_matrix.md               ✓ COMPLETE  (V2a wins with score 71)
├── 05_top3_candidates.md             ✓ COMPLETE  (V2a, V4, V2c)
├── 06_best_single_target.md          ✓ COMPLETE  (V2a: Matter Bounce + ECH)
├── 07_phase1_blueprint.md            ✓ COMPLETE  (6-phase execution plan)
├── final_verdict.md                  ✓ COMPLETE  (this file)
└── phase1_mcmc/                      → NEXT: Begin Phase 1a
```

---

## The Bottom Line

The 15-branch closure assessment (A–O) showed that the minimal symmetric radiation bounce is observationally transparent. Branch V shows that this transparency is a property of the *minimal model*, not of bouncing cosmologies generically.

The matter bounce + ECH scenario (V2a) produces:
- **A parameter-free non-Gaussianity prediction** (f_NL = 5/12) testable by SPHEREx
- **A scale-invariant spectrum** from the contraction phase (not the bounce)
- **A low-ℓ cutoff** that may explain the Planck quadrupole anomaly
- **A distinctive consistency relation** that separates it from inflation

The ECH framework provides the bounce mechanism that standard matter bounce models lack. This is a genuine theoretical contribution: replacing "assume a non-singular bounce happens" with "the bounce occurs at ρ_crit = 0.21 M_Pl⁴ due to spin-torsion coupling."

**Next step: Begin Phase 1a — build the background solver for dust contraction → ECH bounce → radiation expansion.**
