# Houston Decision Package — LOAD-BEARING Findings (CORRECTED 2026-06-08)

After 11 autoloop fires + v3.2 meta-reviewer + persistence-tracker bug-fix
(false-positive `lee` substring-matching on `calEE` removed), the actionable
queue for Houston is now 5 confirmed scientific issues.

For each finding: verified location, current text, recommended fix, estimated
effort, and effect on headline numbers.

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
