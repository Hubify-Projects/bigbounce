# Houston Decision Package — LOAD-BEARING Findings (UPDATED 2026-06-08 14:32pt after fire 14)

After 14 autoloop fires + v3.2 meta-reviewer + v3 content-diff tool
(replaces broken keyword fingerprinting; commit `b1a25f2d`), fire 14 added
16 NEW substantive ESS findings on top of fire 13's 12. Total queue is now
TIER A (fire 13: 9 items) + TIER A2 (fire 14: 16 items) = 25 confirmed
scientific issues for Houston decision.

Self-terminate counter remains 0/3 (NEW > 0 in both fire 13 and fire 14).
The autoloop is NOT converging — it's mining deeper layers of issues per
fire. See AUTOLOOP_IMPROVEMENTS.md for the tooling upgrades behind this
clearer picture.

## TIER A2 — fire 14 NEW high-impact discoveries

**Standout**: 3 NEW P1A ESS findings (αem coupling-family mismatch,
θ-as-propagating-field ontology, "cubic axial-current operator" algebra error)
on top of fire 13's Holst→Pontryagin error. Combined, this means P1A has
SIX major theoretical issues identified by gpt-5-pro across two fires that
no prior fire (or per-vendor reviewer) ever caught.

### 🔴 #A2-1 — P1A αem/(4π) coupling-family mismatch in gravity loop

**File**: `arxiv/paper1a_ech_nogo.tex`, Sec. IV.B (Eq. 15 narrative), p. 9–10.

**The flaw**: paper writes "The dimensionless coefficient is O(αem/4π)…"
for the Holst/Nieh-Yan-induced operator θNY–J5. But αem is the
electromagnetic loop factor, and there is NO EM field in the Route-2 operator
θNY–J5. The correct loop normalization for the gravity-fermion sector is
1/(16π²) (times appropriate gravitational/matter vertex factors).

**Recommended fix**: Replace αem/(4π) → 1/(16π²) with the appropriate
gravity-fermion dimensionless vertex factors. Re-derive the amplitude.
Update the suppression estimate and conclusions. If an EM loop IS genuinely
intended, show the explicit chain from θNY–J5 to photon-sector birefringence
with the correct gauge couplings.

**Effort**: ~2h text rewrite + verification. Effect: the suppression estimate
may change by orders of magnitude, materially affecting the no-go scope.

---

### 🔴 #A2-2 — P1A θ-as-propagating-field ontology error

**File**: same as #A2-1, Sec. IV.B (Eq. 14) + surrounding narrative.

**The flaw**: paper writes "θ(x) is the Nieh–Yan pseudoscalar" as if it were
a propagating field with ∂μθ ∼ H₀ today. But in minimal Einstein–Cartan
with constant γ and non-propagating torsion, θ_NY is a DENSITY built from
torsion/contorsion — NOT a free field with time evolution. Using ∂μθ as
a slowly-varying background scalar is unjustified.

**Recommended fix**: Either (i) promote γ to a bona fide dynamical
pseudoscalar (with a kinetic term) and show how θ acquires dynamics, OR
(ii) drop the ∂μθ J5 operator as a late-time source and remove the
birefringence comparison based on it. State clearly what θ is and is NOT
in the minimal EC–Holst theory.

**Effort**: This is structural — could touch the entire late-time-ALP narrative.
~1 day text + math.

---

### 🔴 #A2-3 — P1A "cubic axial-current operator" algebra error

**File**: same as #A2-1, Sec. II.C.1, p. 6–7 (Order-of-magnitude matching).

**The flaw**: text says "this holds at the cubic axial-current operator level
because the cube of the fermion bilinear scales as the cube of the fermion
number density." There IS no cubic axial-current operator in minimal EC:
torsion ∝ J5, induced contact ∝ J5·J5 = (J5)², not (J5)³.

**Recommended fix**: Remove "cubic axial-current operator" language. Correct
the scaling discussion: torsion scales linearly with J5; the induced
four-fermion energy density scales as (J5)² ∝ n_ψ², not as the cube of a
bilinear. Re-derive D_inf with the corrected scaling chain.

**Effort**: ~1h text fix + scaling re-derivation.

---

### 🔴 #A2-4 — P1B βALP arithmetic check fails

**File**: `arxiv/paper1b_mcmc_companion.tex`, Sec. IV.

**The flaw**: paper quotes "βALP = 0.336° ± 0.107° (C_aγ = 8 fixed),
Δϕ/f_a ∈ [0.2, 1.1]". Using paper's own formula β = [α_EM/(4π)] C_aγ
(Δϕ/f_a) with max Δϕ/f_a = 1.1: maximum attainable β is much less than
0.336°. The arithmetic does NOT close.

**Recommended fix**: Re-derive β from formula + parameters and reconcile.
Either correct the quoted 0.336° OR identify which input parameter was
actually used.

**Effort**: ~30min math + text.

---

### 🔴 #A2-5 — P2 β arithmetic with standard convention gives 0.002° not 0.27°

**File**: P2 source, Sec. 2.2 + Abstract.

**The flaw**: with the standard normalization L ⊃ −(g_aγ/4)φ F F̃ and
g_aγ = (α/2π)(C/f_a), the predicted rotation is β = (α/4π) C (Δφ/f_a).
Using the paper's own Δφ/f_a ≈ 0.24 (from Eq. 1) and C ~ O(1) gives
β ≈ 0.002° — NOT the quoted 0.27°. Two orders of magnitude off.

**Recommended fix**: Reconcile. Either justify a different coupling
convention OR correct the headline β prediction. This compounds with
#A3 (fire 13: fa cancellation) and #A4 (fire 13: spectator/Ω_φ).

**Effort**: ~2h text + careful derivation.

---

### 🔴 #A2-6 — P3 γ ± 0.382 vs CI [2.304, 2.882] arithmetic inconsistency

**File**: `pipelines/p3_anomaly_engine/paper3_draft.tex`, §App E (PTA MCMC).

**The flaw**: paper writes "γ = 2.567 ± 0.382 (median 2.591, 68% CI [2.304,
2.882])". The ±0.382 Gaussian gives ~0.76 width at 1σ; the quoted CI width
is 0.578. Either the ± is not 1σ or the CI is not 68%.

**Recommended fix**: Pick a single interval convention. Use either ±σ
(Gaussian-approximation) or [16%, 84%] CI consistently.

**Effort**: ~15min text fix.

---

### 🔴 #A2-7 — P5 1.98pp vs 1.7pp canonical-config range cross-section contradiction

**File**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, Table II
vs Discussion text.

**The flaw**: Table II canonical V-Web f_CW values {0.4836, 0.5034, 0.4980,
0.4963} → range 0.0198 = 1.98pp. Body text elsewhere quotes 1.7pp range
for the SAME canonical config. Internal inconsistency.

**Recommended fix**: Sweep all "1.7pp" mentions and reconcile against
Table II. Pick the correct number.

**Effort**: ~15min text fix.

---

### 🟠 #A2-8 — P4 per-pixel-shuffle null constancy by construction

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`, Sec. IV.D +
App. A.

**The flaw**: paper repeatedly describes the main null as "per-pixel
random-label permutation" or "per-pixel-shuffle". If labels are permuted
within each pixel p while holding N_CW(p) and N_CCW(p) FIXED, the per-pixel
A_p is invariant by construction and the null distribution is constant.
That cannot be the actual null used.

**Recommended fix**: Specify the actual permutation domain. If labels are
shuffled ACROSS pixels (not within), say so. If within, the null is broken.

**Effort**: ~1h text clarification + verification.

---

### 🟠 #A2-9 — P4 MASTER mode-coupling matrix missing ℓ=0 completeness

**File**: same as #A2-8, Sec. IV.D + footnote on MASTER.

**The flaw**: text states "the MASTER mode-coupling matrix does NOT include
ℓ=0 on either the input or output side." With incomplete mode coupling on
a cut sky, low-ℓ leakage into adjacent ℓ-bins may not be properly accounted
for. Should be documented with explicit NaMaster bin_options + code-level
verification.

**Recommended fix**: Document the binning + cl1 ranges explicitly; show
that low-ℓ leakage into ℓ=1 (the headline statistic) is bounded.

**Effort**: ~2h text + NaMaster code check.

---

### 🟠 #A2-10 to #A2-16 — Additional fire 14 ESS

Brief list (see `project-context/peer-reviews/auto-2026-06-08_1424pt_*_META_REVIEW.md` for full):

- P1B-META-E2: χ²±5.6 weighted-sample mean is not a recognized GOF statistic.
- P2-META-E2: Flat prior β∈[0°,1°] is one-sided → biases Bayes factor.
- P3-META-E1: Per-element MSE without inverse-variance whitening — score depends on instrument noise floor.
- P3-META-E2: eROSITA selection threshold (S>0.259) inconsistency with definition (z-scored MSE).
- P3-META-E3: 0.2% SIMBAD match rate at-or-below random-coincidence floor (~2.4×10⁻³).
- P5-META-E2: Tidal field z∈[0.01, 2.0] vs matched catalog zmax=3.83 selection mismatch.
- P5-META-E3: DESIVAST non-void definition issue.

Each ~30min text or methodology clarification.

---

## TIER A — fire 13 NEW high-impact discoveries (none of the 5 reviewers caught these; gpt-5-pro meta-reviewer did)

### 🔴 #A1 — P1A Holst → Pontryagin identity is mathematically WRONG — **CATASTROPHIC**

**File**: `arxiv/paper1a_ech_nogo.tex`, Eq. (23), Sec. X (pp. 14–15), Abstract,
Sec. I.

**The error**: paper claims `ε^{μνρσ} R_{μνρσ} = (1/2) *R R ≡ ∂_μ K^μ`

## TIER A — fire 13 NEW high-impact discoveries (none of the 5 reviewers caught these; gpt-5-pro meta-reviewer did)

### 🔴 #A1 — P1A Holst → Pontryagin identity is mathematically WRONG — **CATASTROPHIC**

**File**: `arxiv/paper1a_ech_nogo.tex`, Eq. (23), Sec. X (pp. 14–15), Abstract,
Sec. I.

**The error**: paper claims `ε^{μνρσ} R_{μνρσ} = (1/2) *R R ≡ ∂_μ K^μ`
(Pontryagin density, total derivative). The Pontryagin density is
`ε^{μνρσ} R_{μν}^{αβ} R_{ρσαβ}` (TWO curvatures). The Holst term has only ONE
curvature. They are not equal.

**The correct identity** (per Bianchi + Nieh-Yan):
`e ∧ e ∧ R = −NY + T ∧ T`. For torsion-free `T = 0` this is Bianchi-trivial
(no EOM contribution from a topological variation) but **it is not the
Pontryagin density**. The "perturbation-transparency" claim that depends on
this equality is therefore unsupported.

**Recommended fix**: Replace every "Holst → Pontryagin" statement with the
correct Bianchi-trivial / Nieh-Yan formulation. Provide a corrected derivation
of perturbation-transparency that does not invoke the false equivalence with
`R R̃`. Show explicitly that the Holst term's variation vanishes on torsion-free
backgrounds by Bianchi identity arguments (not by reduction to Pontryagin).

**Effort**: ~1 day text rewrite (substantial: this touches the paper's core
mathematical claim). Effect on headline: the no-go theorem's scope statement
needs revision; the structural conclusion may survive but the path through
Pontryagin does not.

---

### 🔴 #A2 — P4 v1.0.160 footnote regression — **I introduced this in the LOAD-BEARING round**

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`, §IV.D
`fn:binomial_nspiral` footnote (added in v1.0.160 commit `73522984`).

**The flaw**: the footnote claims "a parallel rerun on N(p)_all-trial draws is
queued… expected to shift the per-pixel inflation by ⟨N_all/N_spiral⟩ ≈ 1.49 in
trial count, with a sub-0.1σ effect on the headline pre-MASTER reproduction
figure because mode-coupling decoupling absorbs the trial-count normalization."

**Why it's wrong**: mode-coupling decoupling is a POST-MASTER operation. It
cannot affect a PRE-MASTER (pseudo-Cℓ-on-mask) statistic by definition. The
99.3% reproduction figure in Table tab:monopole_mask_null is the pre-MASTER
quantity. Claiming MASTER decoupling absorbs its trial-count is internally
inconsistent.

**Recommended fix** (two options):
- **Option A (mechanical, 1h)**: Remove the "mode-coupling decoupling absorbs"
  sentence. Replace with: "The per-pixel inflation factor in trial count is
  expected to be sub-percent for sky regions where N_NS(p) ≪ N_spiral(p) and
  the effect on pre-MASTER pseudo-Cℓ is a re-normalization that propagates
  through MASTER decoupling unchanged."
- **Option B (hard, ~4h compute)**: Run the actual N(p)_all-trial null and
  report the empirical impact. Update Table IV with both rows.

**Effort**: Option A 1h text, Option B 4h compute + text. **Option B
recommended** per `feedback_take_critiques_seriously` and
`feedback_default_hardest_path` — the meta-reviewer specifically asks for
the actual rerun rather than a re-justified assertion.

---

### 🔴 #A3 — P2 fa CANCELLATION in central β formula

**File**: `research/focused_paper_source_integration/02_full_draft.tex` (or
canonical P2 source), Sec. 2.2, Abstract, Conclusion.

**The flaw**: with `g_aγ = C_0/f_a` and `Δφ ≈ f_a θ_i × F(m/H_0)`, Eq. (2)
gives `β = (C_0/2 f_a) Δφ ≈ (C_0 θ_i/2) F(m/H_0)`. **f_a cancels.** The
"Planck-scale decay constant" claim is irrelevant for the isotropic β amplitude
under the author's own definitions.

**Recommended fix**: (i) Either justify a coupling choice where `g_aγ` is NOT
`1/f_a` (carry α/2π and show how f_a enters β), or (ii) remove the
"Planck-scale" naturalness claim from the β prediction and clarify where f_a
actually enters other observables (energy density, anisotropies, astrophysical
constraints).

**Effort**: ~2h text fix.

---

### 🔴 #A4 — P2 spectator-ALP claim conflicts with Ω_φ ≈ 0.17

**File**: same as #A3, Sec. 5 + Discussion.

**The flaw**: For `m ≈ H_0`, `f_a ≈ M_Pl`, `θ_i ≈ O(1)`:
`Ω_φ ≈ (1/6)(m/H_0)^2 θ_i^2 ≈ 0.17`. That is NOT a spectator. For `m/H_0 ≳ 10`
(hinted in Fig. 1), `Ω_φ ≫ 1` — incompatible with ΛCDM.

**Recommended fix**: Either constrain (m, θ_i, f_a) to ensure `Ω_φ,0 ≪ 1`,
or reframe the ALP as a dark-energy-like component and confront it against
SN/BAO/CMB constraints.

**Effort**: ~2h text fix + maybe a constraint propagation.

---

### 🔴 #A5 — P1B SNR(per-realization) ≠ SNR(mean)

**File**: `arxiv/paper1b_mcmc_companion.tex`, Sec. IV, p. 5–6 (Eq. (1) +
"Independent verification" block).

**The flaw**: The quoted "pipeline-recovery SNR = 20.32 (500 MC)" is almost
certainly `μ / SE[μ] = √N · μ/σ`, not the per-realization detectability
`μ/σ`. With N=500: per-realization SNR ≈ 20.3/√500 ≈ **0.9**, explaining the
large disparity vs Planck/ACT sky errors. As written, readers can mistake
SNR-on-the-mean for per-map detectability.

**Recommended fix**: Define SNR unambiguously. Report both `μ/σ` (per-realization)
and `μ/SE(μ)` (estimator calibration). Replace the headline SNR with the
per-realization SNR when contrasting against sky measurements. Provide
`σ(β̂)` across realizations and `SE(μ) = σ/√N`.

**Effort**: ~30min text fix.

---

### 🔴 #A6 — P1A internal contradiction Sec.IV.D vs Sec.XII fine-tuning

**File**: `arxiv/paper1a_ech_nogo.tex`, Sec. IV.D (pp. 10–11) vs Sec. XII (p. 16).

**The flaw**: Sec. IV.D calls `m_θ ≈ H_0` "precisely the cosmological constant
problem in disguise" and "a dimensionful tuning of order 10^{-61}". Sec. XII
then says "A spectator ALP with f_a ∼ M_Pl, m ∼ H_0 is consistent … without
fine-tuning." Direct contradiction.

**Recommended fix**: Pick one position uniformly. Either remove the "without
fine-tuning" line from Sec. XII OR supply a symmetry/mechanism that fixes
`m_θ ∼ H_0` and revise Sec. IV.D.

**Effort**: ~30min text fix.

---

### 🟠 #A7 — P4 "MASTER-deconvolved pseudo-Cℓ" terminology contradiction

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`, Abstract +
§IV.C.b.

**The flaw**: Pseudo-Cℓ by definition refers to the masked (not deconvolved)
spectrum. Once MASTER deconvolution is applied it is no longer "pseudo".
The abstract writes "MASTER-deconvolved single-mode pseudo-C_1 … yields
−0.122σ", which is a contradiction in terms.

**Recommended fix**: Use "pseudo-Cℓ" for masked pre-deconvolution and
"MASTER-deconvolved Cℓ" (or simply "Cℓ") for deconvolved quantities.
Sweep the abstract + body.

**Effort**: ~1h text fix.

---

### 🟠 #A8 — P3 42hr wall-clock can't reconcile per-survey throughputs

**File**: `pipelines/p3_anomaly_engine/paper3_draft.tex`, §II.C.

**The flaw**: Paper says "total processing time ≈ 42 hours wall-clock dominated
by DESI DR1 scan (19,705s) + LAMOST DR10 scan". Reconstructed totals from stated
throughputs (DESI 22.5M at 1142 spectra/s ≈ 5.5h; LAMOST 11.4M at 950 spectra/s
≈ 3.3h; SDSS ≈0.6h; Planck/Gaia/NEOWISE/eROSITA all seconds) sum to ~9.4h, not
42h. ~32h unaccounted.

**Recommended fix**: Either correct the 42h total or document I/O + CPU
preprocessing + retries + queueing breakdown.

**Effort**: ~1h text fix + verification.

---

### 🟠 #A9 — P3 "across the five primary target classes" — 22.5M vs 6.5M contradiction

**File**: same as #A8, §III.A.

**The flaw**: Says "we processed all 22,504,897 coadded spectra from the Main
Survey across the five primary target classes BGS/LRG/ELG/QSO/MWS". Same
subsection later: "across the 6.5 million spectra in DESI DR1 that carry a
validated TARGETTYPE classification … the remaining ~16 million spectra are
unclassified filler targets, sky fibers, or calibration exposures."

**Recommended fix**: Clarify exactly which spectra are in the 22.5M production
scan vs which belong to "five primary target classes". Provide exact class
fractions and how non-science fibers were treated in training/scoring.

**Effort**: ~30min text fix.

---

## TIER B — pre-fire-13 LOAD-BEARING items, status updated

### 🟢 #1 — P5 T-Web/V-Web mislabeling — **CLOSED in v0.1.46-2026-06-08**

Closed in commit `73522984` (LOAD-BEARING round). Paper retitled,
Hahn 2007 T-Web footnote added.

### 🟢 #2 — P3 dedup 5″ heterogeneity — **CLOSED in v3.1.76**

Closed in commit `73522984`. New §III.B per-survey astrometric paragraph +
Budavári-Szalay sweep deferred. **Note**: fire 13 still surfaced this as
recurring fingerprint (cluster decay needs another round to flush).

### 🟡 #3 — P4 binomial null trial-count — **CLOSED in v1.0.160 BUT regression in fix**

Closed in commit `73522984` via `fn:binomial_nspiral` footnote — but the
footnote's "mode-coupling decoupling absorbs trial-count" claim is
internally inconsistent (see #A2 above). **The closure introduced a new
ESSENTIAL.** Needs Option B compute rerun.

### 🟡 #4 — P4 post-MASTER null rerun — still queued

1-day MC compute. Not in this round.

### 🟢 #5 — P4 cross-match — **VERIFIED RESIDUAL in fire 12**

Fire 13 still surfaced as recurring fingerprint; cluster decay needs another
round. No new fix required.

---

## Cumulative effort to clear new TIER A

| Item | Effort | Type |
|---|---|---|
| #A1 P1A Holst→Pontryagin rewrite | 1 day | Mathematical |
| #A2 P4 footnote regression — Option B rerun | 4h | Compute + text |
| #A3 P2 fa cancellation | 2h | Text |
| #A4 P2 spectator Ω_φ | 2h | Text |
| #A5 P1B SNR clarification | 30min | Text |
| #A6 P1A fine-tuning contradiction | 30min | Text |
| #A7 P4 pseudo-Cℓ terminology | 1h | Text |
| #A8 P3 42hr wall-clock | 1h | Text |
| #A9 P3 22.5M vs 6.5M | 30min | Text |
| **TOTAL** | **~2 days** | Mostly text + 1 compute rerun |

After Tier A closure, next autoloop fire should test whether the new findings
recur (validation) or fade (closure). Self-terminate counter stays at 0/3
until the cycle re-converges.

---



## 🔴 #1 — P5 algorithm-label mismatch (T-Web vs V-Web) — **VERIFIED in code**

**File**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (paper) +
`pipelines/p5_desi_chirality/env_finder/_compute_vweb_lib.py` (code)

**The verified mismatch**:
- Paper title and body claim "V-Web tidal classification" + cite Hahn+2007 + Hoffman+2012
- Code in `_compute_vweb_lib.py:63-86` computes `T_ij = d²Φ/dx_i dx_j` via Poisson
  solve `phi_k = -delta_k / k²` then `T_ij = -k_i k_j phi_k`
- This is the **T-Web recipe (Hahn+2007)**, NOT V-Web (velocity shear, Hoffman+2012)
- No velocity field is reconstructed anywhere in the pipeline

**Recommended fix** (Houston decision needed):
- **Option A (30-min mechanical)**: Rename "V-Web" → "T-Web" throughout paper.
  Drop the Hoffman+2012 citation (or move to "we use the Hahn+2007 T-Web variant").
  Rename functions/files: `compute_vweb` → `compute_tweb`, `01_compute_vweb.py` →
  `01_compute_tweb.py`. RSD-anisotropy discussion in §Limitations is unchanged
  since T-Web is the simpler tidal classifier.
- **Option B (1 week)**: Actually implement V-Web — reconstruct velocity field
  (linear theory / continuity on selection-function-corrected density) and
  compute Σ_ij. Re-run all environment-dependent chirality tests.

**Recommend**: Option A — the science conclusion (null at sub-pp sensitivity)
does not depend on T-vs-V Web; the classifier choice is methodology only.

**Effect on headline**: None for the null result. Adds clarity for reviewers.

---

## 🔴 #2 — P3 5″ uniform deduplication across heterogeneous surveys — 4/8 rounds

**File**: `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Section**: §II D, Step 6 (the 5″ dedup procedure)

**Issue**: A uniform 5″ positional radius across DESI/SDSS/LAMOST (sub-arcsec
astrometry), Gaia (sub-0.1″ + proper motions), and NEOWISE (~6″ PSF) is naive.
Over-merges unrelated neighbors in dense regions; under-merges NEOWISE counterparts.

**Recommended fix**:
- **Option A (30 min text + sensitivity)**: Add a paragraph acknowledging the
  per-survey astrometric heterogeneity; cite that the 5″ is conservative for
  the strictest catalog (NEOWISE PSF ~6″) but loose for Gaia; show a
  sensitivity test of {3″, 5″, 7″} on the headline 378,280 count.
- **Option B (1-2 days)**: Switch to Budavári–Szalay probabilistic cross-match
  with per-survey error ellipses + Gaia PM epoch propagation. Recompute the
  10,213 collapsed detections and 637 multi-survey coincidences.

**Recommend**: Option A for now. Option B would be the strongest possible answer
but the headline 378,280 is unlikely to change by more than 0.1%.

---

## 🔴 #3 — P4 binomial null uses n_total instead of N_spiral — 3/8 rounds

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Section**: §IV.D (Monopole+Mask Leakage Generative Null) + Appendix A

**Issue**: After my v1.0.158 documentation of W_p = N_all (CW+CCW+NS), the
binomial null in §IV.D draws `Binomial(n_total, p_CW)`. But the chirality
field A_p is defined on spirals only (CW+CCW). Using n_total (which includes
NS galaxies) over-draws CW trials and inflates the "99.3% reproduction" claim.

**Recommended fix** (mechanical text + 4-hour rerun):
Change `Binomial(n_total, p_CW)` → `Binomial(N_spiral(p), p_CW)` in §IV.D.
Re-run 500 MC realizations on the full canonical mask through MASTER. Update
the "99.3% reproduction" number and Table IV entries (Data 1.696e-2 / Null
1.685±0.007 / z=+1.68).

**Effort**: 4 hours (small computational rerun + Table IV update + 1 paragraph
rewrite).

**Effect on headline**: The "99.3%" likely drops to 70-90% range. The +3.64σ
canonical-mask residual may shift slightly. Direction of shift TBD.

---

## 🔴 #4 — P4 post-MASTER leakage explanation unproven — 3/8 rounds

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Section**: §IV.D + Table IV

**Issue**: The "99.3% reproduction" applies to PRE-MASTER pseudo-C_ℓ. The
+3.64σ POST-MASTER residual is asserted to be leakage but this is never
directly tested by passing the leakage-only null through MASTER on the
canonical mask.

**Recommended fix**:
Run the monopole-only generative null through the exact post-MASTER pipeline
on the canonical mask. Report the empirical distribution of the post-MASTER
ℓ=1 statistic. If +3.64σ sits in the high end, the leakage claim is supported.

**Effort**: 1 day computation (rerun 500 MC realizations through MASTER on
canonical mask).

**Effect on headline**: Could revise the canonical-mask residual interpretation.

---

## 🔴 #5 — P4 cross-match methodology audit — 4/8 rounds

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Section**: §II (catalog construction) + §III (GZ1 cross-match)

**Issue**: The meta-reviewer keeps flagging cross-match systematics. After
inspection, this is likely a re-flagging of: (a) the 234,282 GZ1 cross-match
that I fixed in v1.0.159; (b) the GZ1 dilution factor that I fixed in v1.0.159;
(c) potentially a new concern about the GZ1 cross-match radius.

**Recommended fix**: Verify whether 4/8 rounds is a residual recurrence of
already-fixed issues OR a genuinely new concern. If new, address it; if
residual, the fixes need a couple more autoloop fires to fully propagate
through the consensus_key clustering.

**Effort**: 30 min audit.

---

## ⚠️ DOWNGRADED: P1B `lee` was a FALSE POSITIVE

Previously listed as the top LOAD-BEARING item (6/8 rounds). After fixing the
persistence_tracker's substring matching, this is **NOT a real LEE issue** —
the keyword `lee` was matching on `calEE` (the Planck calibration nuisance
parameter `cal_E×E` that recurs in P1B's MCMC parameter list of 17 nuisances).

The actual P1B-META-E1 finding is about **`wpivot` definition**:
> "The paper reports wpivot = −1.0344 ± 0.0301 '−1.1σ from −1' but never defines
> the pivot redshift zp or the construction of wpivot (e.g., decorrelation
> procedure, choice of zp, dependence on the chosen dataset stack)."

**P1B real fix**: add a precise definition of wpivot, the method used to
determine zp, and a robustness check. **Effort: 1 hour text + table.**

---

## 🟡 RECURRING items (2/8 rounds, monitor)

- P3 `deduplication` — separate fingerprint, likely same as #2 above
- P4 `monopole`, `master`, `table_ii`, `label`, `fsky`, `leakage` —
  overlapping fingerprints with #3/#4
- P5 `v-web` — re-flagging of #1 above
- P1B `label`, `table_ii` — minor recurring patterns

---

## Cumulative effort estimate to clear LOAD-BEARING tier

| Item | Effort | Type |
|---|---|---|
| #1 P5 T-Web/V-Web rename (Opt A) | 30 min | Mechanical text + code |
| #2 P3 dedup sensitivity test (Opt A) | 30 min | Mechanical text |
| #3 P4 binomial null rerun | 4 hours | Computational + text |
| #4 P4 post-MASTER null rerun | 1 day | Computational + text |
| #5 P4 cross-match audit | 30 min | Audit (likely residual) |
| Plus P1B wpivot definition | 1 hour | Text + table |
| **TOTAL** | **~2 days** | Mostly text + 2 reruns |

Once Houston applies these, fire 12+ should see the autoloop's NEW-ESS
counter increment toward zero across 3 consecutive rounds and self-terminate.

---

## Files referenced

- `project-context/peer-reviews/PERSISTENT_FINDINGS.md` (auto-regenerated by v3_persistence_tracker.py)
- `project-context/peer-reviews/PAPER_VERSION_TIMELINE.md` (auto by v3_version_aware_track.py)
- `project-context/peer-reviews/AUTOLOOP_LOG.md` (per-fire summary)
- `project-context/peer-reviews/auto-2026-06-0*_P*_META_REVIEW.md` (per-paper per-fire meta findings)
- `project-context/peer-reviews/TRIAGE_QUEUE_2026-06-05.md` (earlier mechanical fixes already shipped in v1.0.159)
