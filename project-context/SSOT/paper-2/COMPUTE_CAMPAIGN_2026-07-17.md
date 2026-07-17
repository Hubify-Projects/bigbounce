# P2 Open-Compute Campaign — 2026-07-17 (Phase 1)

**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.122 (PRD,
triple-ACCEPT board converged, verified cap 80).
**Objective (directive L / M):** close the three open-compute/venue gates that hold P2
below all-ACCEPT with **real computation**, not text waves. Integrity absolute
(`/never-fabricate-derivation`, pattern-036): every number is a script output; no
gate is claimed closed by this campaign; honest negatives are results.

**Standing routing (directive N):** orchestrator = Opus/Fable-5; workers = Sonnet/Haiku
via Claude Code subagents; Codex/OpenAI PAUSED. RunPod available (`RUNPOD_API_KEY` in
`.env.local`) — but see per-gate "where it runs": G1/G3 are CPU/symbolic, G2's real
close is external-data-gated.

---

## Gate → disposition map (from DISPOSITIONS/P2.md + truth audit)

| Gate | Canonical id | Class | One-line |
|------|--------------|-------|----------|
| **G1** Direct cubic bounce transfer | DP2-13 (+DP2-25) | RE-FLAG-DISCLOSED / OPEN-COMPUTE | Leading gradient-transmission coefficient uncomputed (OOM only); subleading sign scheme-dependent. |
| **G2** Channel-native Fisher / SPHEREx Cov_B | DP2-34 (done, surrogate) + DP2-26/-29 (open) | closed-by-compute (surrogate) / OPEN-COMPUTE (real Cov_B) | Surrogate channel-native Fisher already committed (`c15`); real external per-triangle Cov_B not publicly released. |
| **G3** Model-specific torsion bound | assumption (f), tex L1102/L1036 | OPEN (theory) | No explicit Einstein–Cartan four-fermion operator bound on δf_NL. No script yet. |

---

## G1 — Direct cubic bounce transfer (DP2-13)

### What the paper claims now
Contraction-phase amplitude `f_NL^local = -35/16` fixed exactly by the four-vertex sum
(`scripts/p2_vertex_check.py`, quadruple-certified). Every observational number is
**conditional on assumption (d)** (tex L1102): faithful cubic transmission through the
bounce. Current derivation (v1.7.91): single-clock super-horizon ζ-conservation
(Weinberg 2003, all orders; effective LQC adds no new scalar dof) ⇒
transmission `= 1 ± O((k η_B)²)`, `δf_NL ≲ 1e-3`. **Disclosed residual (DP2-13):** the
leading gradient-correction **coefficient** is an order-of-magnitude scaling estimate,
not a computed number, and its subleading **sign is quantization-scheme dependent**.

### Prior committed attempts (both honest-negative — do not repeat)
- `research/cubic_bounce_transmission/pathz_full_inin_bounce.py` → SHAPE-only
  (scale-independent transfer); contraction-only f_NL missed −35/8 by ~2.5× ⇒ not
  amplitude-faithful.
- `research/cubic_bounce_transmission/pathz2_calibrated_inin.py` → failed the Maldacena
  squeezed calibration gate (2/5); single-vertex in-in quadrature is the wrong-order
  object for an amplitude.
- **Lesson carried forward:** a brute-force in-in *amplitude* through the bounce is not
  the right object. The tractable, amplitude-**faithful** route is the LINEAR
  super-horizon transmission of the conserved ζ mode (a pure ratio; no absolute
  normalization), lifted to the cubic bispectrum by Weinberg's single-clock theorem
  (nonlinear ζ conserved to all orders as k→0 ⇒ bispectrum transmission = linear mode
  transmission at leading gradient order).

### Phase-1 computation (RAN this session — real, committed)
Script: `research/cubic_bounce_transmission/g1_gradient_transmission_scheme.py`
Output: `.../g1_gradient_transmission_results.json` + `.log`.
1. **[A] Vertex anchor (exact sympy):** reproduces squeezed `-35/16`, equilateral
   `-255/128`, Li c_s=1 → `-35/16`. **PASS** (regression guard for the amplitude the
   transmission multiplies).
2. **[B] Explicit LQC quasi-dust background** (8πG=1, ρc=1, a_b=1, w=0):
   `H²=(ρ/3)(1−ρ/ρc)`, `ε=(3/2)(1−2x)/(1−x)` with `x=ρ/ρc=(a_b/a)³`. Verified: smooth
   bounce (a_min=1, H=0, Ḣ=+ρc/2 finite), ε→3/2 matter limit, localized NEC-violating
   window (ε<0 for x>1/2), conformal half-width `η_B ≈ 1.06`. Perturbation
   `z²=3a²/(1−x)=3x^{-2/3}/(1−x)`.
3. **[C] Scheme-dependence, DEMONSTRATED:** in conformal time the effective-fluid
   `z² ~ 1/(η−η_b)²` diverges at the bounce (H=0 with ρ+p≠0). Integrating the linear
   mode `(z²ζ')'=−c_s²k²z²ζ` (ζ_in=1, super-horizon) across the symmetric bounce for a
   k-tower and fitting `T(k)=1−c(kη_B)²`, the coefficient **c grows without bound as the
   H=0 regulator dcut=(1−x_max)→0**: c = 8.6e2, 2.7e3, 3.9e4 for dcut=1e-5,1e-6,1e-7
   (high-precision cross-run: 9.7e2, 2.5e3, 2.4e4, 6.1e5 for 1e-5…1e-8, ~1/dcut).

### What this establishes (honest result)
The model-agnostic effective-fluid transmission coefficient has **no scheme-independent
limit** — it is fixed entirely by how the bounce's H=0 point is regularized, i.e. by the
quantization scheme that renders z″/z bounded. This **numerically demonstrates** DP2-13's
disclosed statement (coefficient is scheme-dependent), converting an assertion into a
computed result. **The paper's current conditional framing is vindicated, not weakened.**
No paper edit; no gate closed.

### Acceptance criterion to CLOSE G1 honestly
Produce **one concrete, scheme-specific** δf_NL(k) by adopting the **Wilson–Ewing
dressed-metric** effective-LQC perturbation variable `z̃` (bounded `z̃″/z̃ ~ ρc`, the
c_s²=1 completion the paper already cites), rerunning step [C] with `z̃` instead of the
singular fluid z, and reporting the finite coefficient c + δf_NL at observable
`k η_B ~ 1e-2` with an explicit statement that it is scheme-specific (deformed-algebra
gives a different subleading sign — already disclosed). That upgrades DP2-13 from
"OOM estimate" to "computed for the adopted scheme."

### Where it runs / effort
Local CPU (symbolic + light ODE). The `z̃` construction is the real work: build the
holonomy/inverse-triad-corrected mode equation (dressed-metric, WilsonEwing:2012), verify
bounded z̃″/z̃ through the bounce, then the transmission integral is minutes. Est. effort:
~half-day of focused derivation + numerics (human-team ~1 week). **Next-session step.**

---

## G2 — Channel-native Fisher via adopted covariance surrogate (DP2-34 done; DP2-26/-29 open)

### Already delivered (committed)
`research/focused_paper_source_integration/scripts/c15_channel_native_fisher.py`
(output `outputs/c15_channel_native_fisher.json`) implements exactly the directive-L
wording — "channel-native Fisher via an adopted covariance surrogate." It adopts the
committed, Heinrich-validated `c13` tree-level Gaussian multi-tracer covariance (reproduces
σ_local≈0.7 to 2–11%) as Cov_B, computes the joint 3×3 Fisher over {f_NL, b_φ, A_GR}, and
reports the nuisance ladder now in the abstract (3.5σ fixed / 3.1σ A_GR-marg / 2.3σ 30%
b_φ prior / 0.4σ free b_φ) with channel-native ρ. This **superseded the transferred
ρ=−0.868 proxy** (DP2-34, closed-by-compute v1.7.114/115).

### What remains open (DP2-26 / DP2-29)
The **real external** SPHEREx per-triangle multi-tracer bispectrum covariance (Heinrich
et al. 2023) is confirmed **not publicly released** (no arXiv ancillary, no Zenodo DOI,
only a pre-publication WIP branch; `INT_v3/DATA_UNLOCK_2026-07-05.md`). So a *true*
channel-native marginalization is **external-data-gated** — not closable by us without
author contact/release. This is honestly disclosed at every use site.

### Real in-repo advance possible (not externally blocked)
The surrogate's load-bearing assumption **S1** (Gaussian/disconnected covariance only;
connected non-Gaussian pieces neglected) is disclosed as *not demonstrated* for the
normalized correlation ρ. A genuine compute step: **add the connected NG covariance terms**
(B·B, T, P·P_shot loops on the squeezed triangles) to the `c13` surrogate and show whether
the channel-native ρ(f_NL,A_GR) and σ_marg are robust to them. Result either strengthens
the surrogate (ρ stable ⇒ S1 caveat closed) or quantifies the shift (honest). This is a
`c13`-extension script; CPU, a few hours.

### Acceptance criterion
Either (a) obtain real Cov_B and run `c10_joint_covariance_marginalization.py` (external,
Houston-gated), OR (b) demonstrate ρ/σ_marg robustness to connected-NG covariance and
retire the S1 caveat. (b) is the honest in-repo lever this campaign can pull.

### Where it runs / effort
Local CPU (CAMB via `c13` import). (b) ~half-day. (a) blocked on external data.

---

## G3 — Model-specific torsion bound (assumption f)

### What the paper claims now
Assumption (f) (tex L1102): "negligible fermion-sourced torsion during contraction and
the bounce." Stated (L1102) as "automatic only in the scalar-only sector; models with
appreciable fermion populations require an explicit bound on the Einstein–Cartan
four-fermion operator." L1036: result "not asserted model independent across …
fermion-sourced torsion sectors." No script exists.

### Computation
Einstein–Cartan gravity with fermions integrates out torsion algebraically, generating a
four-fermion contact operator `~ (κ²) (ψ̄γ^μγ⁵ψ)²` (κ²=8πG). Estimate its contribution to
the contraction-phase curvature bispectrum vs the −35/16 scalar amplitude: the axial
current density scales with the fermion number density n_ψ; the operator's energy-density
fraction is `~ κ² n_ψ² / ρ` at a given epoch. During matter-dominated contraction ρ grows
toward ρc; the fermion contribution is `(κ² n_ψ²/ρ)`-suppressed. Produce a symbolic bound
`|δf_NL^torsion| ≲ f(κ² n_ψ²/ρ_c, ε)` and evaluate for a fiducial cosmological fermion
abundance ⇒ a concrete "negligible below X" number, turning assumption (f) from asserted
to bounded. Cross-check against the Einstein–Cartan bounce literature (Poplawski;
Magueijo–Zlosnik torsion cosmology).

### Acceptance criterion
A committed symbolic script producing `|δf_NL^torsion|` as a function of the four-fermion
coupling + fermion abundance, with a plugged-in fiducial giving a numeric upper bound that
justifies "negligible," + a one-paragraph tex insert for assumption (f). Smallest gate.

### Where it runs / effort
Local CPU (sympy). Est. ~2–4 h. Good candidate for a Sonnet worker given a tight spec.

---

## Phase-1 status & resume

**Ran this session (real, committed):**
- G1 `g1_gradient_transmission_scheme.py` → vertex anchor PASS; explicit LQC background
  verified; **scheme-dependence of the transmission coefficient numerically demonstrated**
  (c ~ 1/dcut, no scheme-independent limit) ⇒ DP2-13 disclosure vindicated. Output JSON+log
  committed. **No gate closed; no paper edit.**

**Blocked / scoped (not startable as a clean close this session):**
- G1 full close needs the Wilson–Ewing dressed-metric bounded-z̃″/z̃ construction (real
  derivation, next-session; the naive fluid z is provably insufficient — that's the
  Phase-1 finding).
- G2 *real* Cov_B is external-data-gated (DP2-26); the honest in-repo lever is the
  connected-NG surrogate-robustness extension (b).
- G3 not yet started (no blocker; clean next task, worker-suitable).

**Resume commands (next session):**
```
cd /Users/houstongolden/Desktop/CODE_YOU/bigbounce
# G1 re-run / inspect the Phase-1 intermediate:
python3 research/cubic_bounce_transmission/g1_gradient_transmission_scheme.py
cat research/cubic_bounce_transmission/g1_gradient_transmission_results.json
# G1 next: implement z_tilde (Wilson-Ewing dressed-metric) in a new
#   g1_dressedmetric_transmission.py, rerun step [C] with bounded z_tilde''/z_tilde.
# G2 next: extend c13 with connected-NG covariance; re-run c15, compare rho/sigma_marg.
python3 research/focused_paper_source_integration/scripts/c15_channel_native_fisher.py
# G3 next: new scripts/g3_torsion_fourfermion_bound.py (sympy Einstein-Cartan estimate).
```

Ledger: DISPOSITIONS/P2.md (DP2-13, DP2-26, DP2-29, DP2-34) and tex L1036/L1102 (assumptions).
