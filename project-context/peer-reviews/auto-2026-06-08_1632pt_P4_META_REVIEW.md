# P4 auto-2026-06-08_1632pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 416.9s

---

P4-META-E1
Severity: ESSENTIAL
Section/page: Abstract p.1; Sec. VI.B p.6 (“Relation to Parity-Violating Sectors”)
Why others missed it: All five focused on statistics/methodology; none audited the parity-transformation claim.
Problem (quote): “We emphasize at the outset that this ℓ = 1 observable is the isotropy-breaking axial-vector channel and is parity-EVEN: it is NOT a direct parity-violation test…”
Required fix: Correct the transformation properties. Under spatial parity, projected spiral handedness flips; for a scalar chirality field A(n) ≡ fCW(n)−fCCW(n), parity implies A′(n) = −A(−n), i.e., the field is parity-odd and its odd-ℓ moments (including ℓ=1) change sign. Rephrase to: “The projected chirality field is parity-odd; a nonzero dipole indicates isotropy breaking in a parity-odd scalar. It is not, by itself, a clean probe of primordial parity violation without a calibrated transfer model.” If the authors have a different formalism (e.g., treating spin as an axial vector yielding a parity-even observable), include a short derivation and citation to justify the claim.

P4-META-E2
Severity: ESSENTIAL
Section/page: Sec. III.C p.3; Appendix B Table V p.8 (Bias-hardening T1); multiple mentions “flip-swap correlation = 1.000”
Why others missed it: Prior reviews questioned thresholds but not that T1 is tautological.
Problem (quote): “This procedure enforces flip-equivariance of the output protocol (flip-swap correlation = 1.000).” and Table V: “T1: Flip-swap r > 0.80 — Result 1.000.”
Required fix: Acknowledge that test-time flip-averaging makes the T1 metric trivially 1.000 by construction; it is not an independent bias test. Remove T1 from the bias-hardening suite or replace it with a pre-TTA evaluation (measure r on raw single-pass outputs) and report that instead. If you retain T1, explicitly state it is a construction check, not evidence of classifier robustness.

P4-META-E3
Severity: ESSENTIAL
Section/page: Appendix A p.7 (NaMaster configuration); Sec. III.D p.3; Sec. IV C–D p.4–5
Why others missed it: One reviewer noted denominator inconsistency; none analyzed the weight–variance mismatch.
Problem (quote): “The NaMaster weight (mask) map assigns Wp = N(p)all… The asymmetry field is Ap = (NCW−NCCW)/(NCW+NCCW) (spirals only)… The depth weighting does not introduce a monopole–dipole coupling because the galaxy-weighted mask-mean ⟨A⟩mask,gw is subtracted…”
Required fix: Use variance-appropriate weights. For the spiral-only field Ap, the natural inverse-variance weight is proportional to Nspiral(p), not Nall(p). Weighting by Nall(p) imports systematics from the non-spiral population into the estimator and can bias both the null mean and the covariance even after monopole subtraction. Provide a rationale and validation for using Nall(p) weights (e.g., show that replacing Wp with Nspiral(p) leaves C1 and its null unchanged within errors). If not, rerun the MASTER analyses with Wp ∝ Nspiral(p) and update all affected results.

P4-META-E4
Severity: ESSENTIAL
Section/page: Abstract p.1; Sec. IV.D p.4–5; Table IV p.5
Why others missed it: One reviewer flagged minimum measurable p for a different test; none addressed uncertainty on finite-MC p for the canonical residual.
Problem (quote): “post-MASTER canonical-mask direct-MC residual is +3.64σ (…; empirical rank pMC = 0.030…)”
Required fix: Report finite-MC uncertainty on empirical p. With N=500 permutations and 15/500 exceedances, quote the Clopper–Pearson interval (e.g., pMC = 0.030 with 95% CI ≈ [0.017, 0.049]) and a Gaussian-equivalent σ with the same one-/two-sided convention used elsewhere. Apply this consistently to all empirical p-values derived from finite ensembles.

P4-META-M1
Severity: MAJOR
Section/page: Abstract p.1; Sec. VI.A p.6 (Sensitivity floor and injection–recovery)
Why others missed it: Others noted HC-definition ambiguity but not the representativeness of using HC-only to set survey sensitivity.
Problem (quote): “empirical 50%-recovery-3σ threshold at |Adipole| ≥ 0.75% … on the HC-spiral subsample (N = 471,049)”
Required fix: Do not present an HC-only injection threshold as the survey-wide sensitivity floor without qualification. Either (a) run injection–recovery on the full Catalog C under the same estimator/null and report that threshold, or (b) clearly label the 0.75% as “HC-only” and provide a mapping to the full-catalog sensitivity (e.g., via measured dilution/Neff ratios). If classification noise argues HC-only is conservative or optimistic, quantify it.

P4-META-M2
Severity: MAJOR
Section/page: Appendix C c. p.8 (Hemisphere scan)
Why others missed it: They focused on LEE double counting, not on the scan grid itself.
Problem (quote): “Testing all hemisphere-pairs at 10° increments: maximum asymmetry 3.05σ… Bonferroni/BH across ∼650 tested directions…”
Required fix: Specify the hemisphere-orientation grid construction and verify the count. A 10° sampling on S^2 typically yields >650 unique directions; 650 needs justification (e.g., de-duplication of antipodes, mask symmetries). Provide the exact number of tested hemispheres, how they are generated, and ensure the LEE correction (whether direct-MC or Bonferroni) matches that number.

P4-META-M3
Severity: MAJOR
Section/page: Table IV p.5; Appendix A p.7; Table III p.5
Why others missed it: They flagged missing null means and a z arithmetic error, but not the normalization bridge.
Problem (quote): Table IV “Pre-MASTER pseudo-C(ℓ=1)ℓ = 1.696×10−2”; Appendix A: “decoupled C1 … 1.51×10−5”; Table III: “ℓ=1 (single mode) 1.494×10−6 (sr)”
Required fix: Provide a normalization/units bridge explaining how 1.696×10−2 (pre-MASTER pseudo-C1), 1.51×10−5 (decoupled C1, canonical mask), and 1.494×10−6 (decoupled C1, subsample mask) relate. Explicitly state units and normalizations (e.g., whether Cℓ is dimensionless or multiplied by sr), and include the analytic relation (or an empirical check) showing expected scaling from pseudo to decoupled (mask-coupling, ℓ-bin width, 4π factors). Without this, the end-to-end arithmetic chain from map to reported C1 is not auditable.

P4-META-M4
Severity: MAJOR
Section/page: Sec. III.A p.3 (Declared Analysis Hierarchy); Sec. IV C–D p.4–5; Appendix A p.7
Why others missed it: They noted ambiguity in mask definitions but not the risk of post-hoc mask selection.
Problem (quote): “Primary cosmological estimators: … MASTER-deconvolved Cℓ at ℓ = 1 on the analysis subsample mask (fsky = 0.659)… Secondary diagnostic estimators: … canonical-N direct-MC … (fsky = 0.49005)”
Required fix: Address hidden conditioning. State explicitly whether the “subsample mask” choice (apodization, pixel threshold, sky cuts) was fixed before looking at results. If not, present results across a small, pre-specified family of reasonable masks (e.g., with/without 2° apodization; pixel thresholds 5,10,20; canonical vs subsample footprints) and show that the headline ℓ=1 result is stable (include a table/figure or Supplementary Material). This mitigates post-hoc selection concerns.

P4-META-M5
Severity: MAJOR
Section/page: Sec. II.A p.2; Sec. III.C p.3; Appendix B c. p.8
Why others missed it: They questioned D4 stability but not the prerequisite WCS/orientation assumption.
Problem (quote): “Each image is a 224×224 pixel cutout… We restrict to 2-fold TTA (original + horizontal flip)… D4-TTA hold-out…”
Required fix: Verify and document that all cutouts share a uniform WCS orientation (e.g., north up, east left) so that a horizontal flip is a true mirror of the sky scene everywhere. If the pipeline occasionally rotates stamps, a horizontal flip may not enact a true parity operation, and 2-fold TTA may leave orientation systematics. Add a WCS-orientation audit (fraction of stamps with non-standard orientation) and, if needed, prefer full D4-equivariant TTA for production or demonstrate parity consistency under vertical flips too.

P4-META-M6
Severity: MAJOR
Section/page: Sec. IV.B p.4; Sec. IV.A p.3; Appendix E b. p.9
Why others missed it: They noted general inconsistencies but not this specific one.
Problem (quote): Sec. IV.A: “Mean classification confidence is 0.951, median 0.9997.” Appendix E b.: “HC-strict (peq > 0.8, N = 624,660).”
Required fix: Disaggregate confidence statistics by class. The quoted median 0.9997 over all 8.47M objects (dominated by “not spiral”) is not informative for the spiral subset, where only ~20% meet peq>0.8. Report the confidence distribution for the spiral-only subset and reconcile it with HC counts used in analyses. Otherwise, readers will infer a conflict between near-unity confidences and a small HC spiral pool.

P4-META-M7
Severity: MAJOR
Section/page: Sec. III.C p.3 (“we restrict to 2-fold TTA”) and Appendix B c. p.8 (D4-TTA validation)
Why others missed it: They noted rotation stability but not the missing ablation.
Problem (quote): “We restrict to 2-fold TTA … D4-TTA hold-out … confirms mean per-galaxy pCW is stable … argmax labels flip in 21.4% of cases…”
Required fix: Provide an ablation showing how the headline cosmological estimators change if D4-TTA is used in production instead of Z2-TTA. Since per-galaxy argmax flips for ~21% of borderline cases under D4, a survey-scale parity measurement could shift. Report the ℓ=1 C1 and real-space dipole estimates under D4-TTA to demonstrate robustness.

P4-META-m1
Severity: MINOR
Section/page: Appendix A p.7 (bins) vs Table III p.5 (bandpowers) vs “Joint χ2/dof (38 bandpowers)”
Why others missed it: They noted missing null means but not the bin-count inconsistency.
Problem (quote): “Bins: single-multipole linear (nlb=1) … The reported MASTER ℓ=1 result is the single-multipole bin… Joint χ2/dof (38 bandpowers) — 161.2/38 = 4.24”
Required fix: Clarify the binning scheme(s). If the headline ℓ=1 uses nlb=1 while Table III shows wide bandpowers and a joint χ2 over 38 bins, state the exact set of bins used for χ2 and ensure consistency between text and table captions. Include the list of bin edges and lmax in an appendix or supplement.

P4-META-m2
Severity: MINOR
Section/page: Sec. IV.C a. p.4 (real-space dipole bootstrap)
Why others missed it: They flagged tailing ambiguity, not the bootstrap design detail.
Problem (quote): “p = 0.30 from the isotropic-null bootstrap at NMC = 10,000”
Required fix: Specify whether the bootstrap resamples pixels, galaxies, or rotates the map; whether weights are preserved; and whether the statistic is the weighted least-squares dipole amplitude. Add a one-line validation (e.g., isotropic simulations recover nominal p-uniformity). This guards against hidden conditioning in the bootstrap procedure.

P4-META-N1
Severity: NIT
Section/page: Appendix C e. p.8 (“15-cell joint label-shuffle max-statistic null”)
Why others missed it: They flagged LEE handling broadly, not this bookkeeping detail.
Problem (quote): “Under the 15-cell joint label-shuffle max-statistic null (NMC = 5,000), the family-corrected p-value is 0.0086…”
Required fix: Define the “15 cells” precisely (e.g., 3 imaging legs × 5 confidence bins) and confirm whether cell correlations are accounted for in the max-statistic null. If not, state that this is an upper bound on the true family-wise error due to positive correlations among cells.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are at least a dozen essential/major blockers: parity-transformation misclassification; tautological bias test; weight–variance mismatch; finite-MC p-value uncertainty omissions; HC-only injection used as survey sensitivity; hemisphere scan accounting; missing normalization bridge across pseudo/deconvolved Cℓ; potential post-hoc mask selection; WCS/orientation audit; inconsistency between global confidence and HC spiral pool; lack of D4-TTA ablation; and multiple documentation gaps in nulls/binning. My confidence that the paper would survive external peer review after addressing these points is moderate; the core null result is likely robust, but several methodological clarifications and reruns (weights, D4-TTA, mask family) are needed to bring the analysis to PRD standards.