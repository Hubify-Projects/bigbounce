# Houston Decision Package — LOAD-BEARING Findings (after 5 autoloop fires)

5 META findings have been surfaced by the v3.2 meta-reviewer in 3+ consecutive autoloop fires. These are CONFIRMED scientific issues requiring Houston-level decision. The autoloop cannot self-terminate until they are addressed at the .tex level.

For each finding: exact location, current text, recommended fix, estimated effort, and effect on headline numbers.

---

## 🔴 #1 — P1B `lee` (LEE double-correction) — **5/5 rounds** (every single fire)

**File**: `arxiv/paper1b_mcmc_companion.tex`
**Section**: Look-elsewhere test description (likely Sec V or Appendix on null tests — need to confirm exact line)

**Current claim** (from R10v3p1 meta finding):
> "The direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives pLEE ≤ 10⁻⁴ … the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ."

**Issue**: A max-statistic Monte Carlo ALREADY includes the trials factor from scanning 650 directions. Applying Bonferroni/BH on top of pLEE = double-correction. Methodologically wrong.

**Recommended fix** (1 paragraph rewrite):
Choose ONE of:
- (a) Report only the direct-MC pLEE (already LEE-corrected); drop the Bonferroni sentence entirely
- (b) Drop the direct-MC pLEE; report only an analytic local p with Bonferroni
NOT both. Recommended: keep (a), drop (b).

**Effort**: ~10 min text edit
**Effect on headline**: None — pLEE remains unchanged; only the "post-LEE significance < 1σ" sentence changes.

---

## 🔴 #2 — P1B `master` (NaMaster systematic floor not propagated) — 3/5 rounds

**File**: `arxiv/paper1b_mcmc_companion.tex`
**Section**: βfree fit reporting

**Current text** (from R10v3p1 fire 1 meta):
> "The paper adopts a 'NaMaster systematic floor' of ~0.04° from the pipeline test, but does not propagate any comparable systematic into its internal βfree fit (0.344° ± 0.096°)."

**Issue**: If the same pseudo-Cℓ machinery is used in the EB likelihood, a comparable configuration-dependent bias may apply to βfree but is not folded into its uncertainty.

**Recommended fix**:
Either (a) explicitly state that the EB likelihood's bias is not the same as the pipeline-test bias (with a one-sentence justification), or (b) inflate the βfree systematic by 0.04° in quadrature.

**Effort**: ~30 min — needs cross-checking of the pipeline-test methodology
**Effect on headline**: If (b) chosen, βfree uncertainty grows from 0.096° to ~0.104° — minor.

---

## 🔴 #3 — P3 `dedup` (5″ uniform deduplication) — 3/5 rounds

**File**: `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Section**: §II D, Step 6 (dedup methodology)

**Current text** (from R10v3p1 meta):
> "7-way positional dedup at 5″"

**Issue**: A uniform 5″ radius across DESI/SDSS/LAMOST (sub-arcsec astrometry) + Gaia (sub-0.1″ + proper motions) + NEOWISE (~6″ PSF) is naive. Over-merges unrelated neighbors in dense regions, under-merges NEOWISE counterparts.

**Recommended fix** (2 options):
- (a) **MECHANICAL**: Add a paragraph acknowledging this limitation; state that survey-pair-specific radii will be used in a future version; show a sensitivity test changing the 5″ to 3″/7″ and report the headline change.
- (b) **ANALYSIS RERUN**: Switch to Budavári–Szalay probabilistic cross-match ingesting positional uncertainties, epochs, PMs, PSF/beam. Recompute the 10,213 collapsed detections and the 637 multi-survey coincidences.

**Effort**: (a) 30 min text + minimal recomputation. (b) 1-2 days
**Effect on headline**: (a) None initially. (b) The 378,280 unique-object count may shift by 0.1-1%.

---

## 🔴 #4 — P4 `leakage|master|monopole` (post-MASTER residual claim) — 3/5 rounds

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Section**: §IV.D + Table IV

**Current text**:
> "The monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cℓ at ℓ=1 … MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage: the post-MASTER ℓ=1 on the strict-superset subsample mask is −0.122σ; the canonical-mask post-MASTER residual is +3.64σ … is consistent with monopole leakage through survey geometry."

**Issue**: The "99.3% reproduction" applies to PRE-MASTER only. The "+3.64σ" POST-MASTER residual is asserted to be leakage but this is never directly tested by passing the leakage-only null through MASTER on canonical mask.

**Recommended fix**:
Run the monopole-only generative null through the exact post-MASTER pipeline (same mask, same Wp, same monopole-subtraction option) and report the empirical distribution of the post-MASTER ℓ=1 statistic on the canonical mask. If +3.64σ sits within the high end of that distribution, the leakage claim is supported.

**Effort**: 1 day computation (rerun 500 MC realizations through MASTER on canonical mask).
**Effect on headline**: Possibly significant. If the post-MASTER null distribution shows +3.64σ is plausibly within the leakage tail, claim is supported. If not, the canonical-mask residual interpretation needs revision.

---

## 🔴 #5 — P4 `binomial` (null variance: n_total vs N_spiral) — 3/5 rounds

**File**: `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Section**: §IV.D (Monopole+Mask Leakage Generative Null)

**Current text**:
> "per-pixel CW count is drawn from Binomial(ntotal, pglobalCW) on the exact canonical mask"

**Issue**: `ntotal` in the generator includes NS galaxies (per the W_p = N_all definition I added in v1.0.158/v1.0.159). But the chirality field A_p is defined on spirals only (CW+CCW). Using n_total in the binomial OVER-draws CW trials, mismatching the denominator and inflating the "99.3% reproduction" claim.

**Recommended fix** (mechanical text + minor recomputation):
Change `Binomial(ntotal, p_CW)` → `Binomial(N_spiral(p), p_CW)` in §IV.D. Recompute the 99.3% number. Recompute the +1.68σ / +3.64σ entries in Table IV.

**Effort**: 4 hours (small computational rerun + Table IV update + 1 paragraph rewrite)
**Effect on headline**: The "99.3%" probably drops to 70-90% range. The +3.64σ canonical mask residual may shift. Depending on direction, the leakage explanation may strengthen or weaken.

---

## Other 🟡 RECURRING items (2/5 rounds, may promote to LOAD-BEARING)

- P5 `tidal_tensor` (T-Web vs V-Web mislabeling)
- P4 `monopole`, `master`, `table_ii`, `fsky` (overlapping with LOAD-BEARING #4/#5)
- P1B `table_ii` (cross-reference issue analogous to pattern-039)

---

## Cumulative effort estimate to clear LOAD-BEARING tier

| Item | Effort | Type |
|---|---|---|
| #1 P1B `lee` | 10 min | Text edit only |
| #2 P1B `master` | 30 min | Text edit + cross-check |
| #3 P3 `dedup` | 30 min (option a) or 1-2 days (b) | Text/analysis |
| #4 P4 `leakage` proof | 1 day | Computational rerun |
| #5 P4 `binomial` | 4 hours | Small rerun + text |
| **TOTAL (option a route)** | **~2 days** | Mostly text + 1 rerun |

Once Houston applies these fixes:
- Fire 6+: All 5 should appear as CLOSED in next persistence-tracker run
- Self-terminate counter starts incrementing toward 3 consecutive zero-new-ESS rounds
- Autoloop converges and self-terminates within 3 more fires (~3 hours)

---

## Files referenced

- `project-context/peer-reviews/PERSISTENT_FINDINGS.md` (auto-generated by v3_persistence_tracker.py)
- `project-context/peer-reviews/PAPER_VERSION_TIMELINE.md` (auto-generated by v3_version_aware_track.py)
- `project-context/peer-reviews/TRIAGE_QUEUE_2026-06-05.md` (manually maintained — has more recent meta items)
- `project-context/peer-reviews/auto-2026-06-05_*_P*_META_REVIEW.md` (raw meta-reviewer output per round)
