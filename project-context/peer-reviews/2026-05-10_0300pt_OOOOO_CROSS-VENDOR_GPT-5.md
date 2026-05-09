# Cross-vendor R-round (OOOOO) — GPT-5 simulated review

**Reviewer profile:** simulated GPT-5, numerical-rigor / statistical-orthodoxy bias.
**Wave:** 14-OOOOO (post-NNNNN/LLLLL on the four-paper bundle).
**Anchoring:** four prior CCAI rounds at <3B+<5M each; surface-level errors closed.
**Mandate:** find issues a same-vendor reviewer might miss because of training-set
overlap. Apply maximum scrutiny in the numerical / Bayesian-vs-frequentist /
MC-convergence / prior-sensitivity / non-Gaussian-likelihood / Wilks invocation
direction.

## Summary table
| Paper | Version | BLOCKER | MAJOR | MINOR | NIT | Total |
|---|---|---|---|---|---|---|
| P1A | v1A.0.18 | 0 | 1 | 2 | 1 | 4 |
| P2  | v1.7.24  | 1 | 1 | 2 | 1 | 5 |
| P3  | v3.1.35  | 1 | 2 | 2 | 1 | 6 |
| P4  | v1.0.44  | 0 | 1 | 1 | 1 | 3 |
| **Total** | | **2** | **5** | **7** | **4** | **18** |

## Convergence judgement

**P1A v1A.0.18 — Submission-ready (PRD theory).** The no-go logic is sound, the
amplitude closures of R1–R4 are reproducible at order-of-magnitude level, and
the hedging on B8/B14 non-independence is honest. One MAJOR — a stale
cross-paper PTA γ value — must be reconciled with P3 before submission, but
this is a one-line edit. Otherwise, ready.

**P2 v1.7.24 — Not yet ready for PRL submission.** The Bayes-factor framing
hides a genuine prior-sensitivity problem that the abstract resolves toward the
high end of the plausible range. The "≥6×10⁵ MC realizations" boilerplate
disguises that the result is fully analytic and the MC neither tightens it nor
stress-tests anything that prior choices don't already control. One BLOCKER on
the SDB σ(n_fNL)=0.086 / σ_marg(f_NL)=0.44 joint-Fisher figure: the ρ=0.966
correlation, if real, makes the marginal a sample-size question, not an
information-content question, and the paper does not show the Fisher-matrix
inputs (k_min, n̄(z), b₁(z), b_φ scheme, six-bin geometry) needed to verify.

**P3 v3.1.35 — Not yet ready for ApJS submission.** The catalog-construction
logic is well-documented and the Path-C-vs-cross-transfer disclosure is
exemplary, but two issues block submission. The internal "Wave 14-II" Fisher
forecast σ(f_NL)≈0.07–0.12 (factor-of-3–10 below Münchmeyer 2019 consensus
0.4–0.9) is reported as "internal consistency check" but appears in the
abstract as a stratification; this is a quantitative claim that the cross-vendor
reader cannot reproduce without seeing the cross-tracer correlation kernel
choices. And the abstract / figure caption conflict on injection-recovery
PASS/FAIL counting (3-PASS abstract vs. 1-PASS figure caption) is the kind of
inconsistency referees flag instantly.

**P4 v1.0.44 — Submission-ready (MNRAS).** This is the strongest of the four
papers statistically: the MASTER-deconvolved -0.12σ at ℓ=1, the bootstrap p=0.30
on the simple dipole, and the LEE-corrected hemisphere result are all defensible.
One MAJOR remains on the post-MASTER null at N_MC=500: the 4.5%-of-σ MC
uncertainty on σ_null is documented, but the Bayes factor or likelihood-ratio
interpretation that distinguishes "consistent with null" from "Wilks doesn't
apply at this multiplicity" is left implicit.

## Per-finding detail (grouped by paper)

### P1A v1A.0.18

#### M1 (MAJOR) [Sec. 10.5 / Table V / App. A] — PTA γ value is stale relative to the companion P3 KDE-likelihood result; cross-paper inconsistency

Lines 1073–1074 and Appendix Table tab:params (line 1366) report
γ_PTA = 3.20 ± 0.42 from "GPU MCMC, companion Paper II/III". The companion
P3 v3.1.35 (line 557, abstract, and Appendix App.~app:pta_mcmc) replaces this
with γ = 2.567 ± 0.382 from a real-KDE-likelihood fit to the NANOGrav 15-yr
free spectrum (the synthetic-from-power-law summary fit at γ=3.20±0.42 is
explicitly superseded; P3 quantifies the shift as -1.48σ in standard-deviation
units). Carrying the stale γ=3.20±0.42 in P1A while P3 uses γ=2.567±0.382 is
an internal inconsistency that any cross-checking referee will flag. The
discrimination-table claim "Bounce prediction γ=3.0 at 0.48σ" (line 1074) does
not survive the update: with γ=2.567±0.382 the bounce sits at +1.13σ above
the posterior mean, not 0.48σ. **Concrete fix:** harmonize the abstract /
Sec. 10.5 / Table V row to γ = 2.567 ± 0.382 with bounce-prediction deviation
+1.13σ and SMBHB at +4.61σ, citing companion Paper III. CLAUDE.md (line 58)
also still has the stale value and must be updated in the same commit.

#### m1 (MINOR) [Sec. 4.2 / Eq. above eq:oneloop_parity_odd] — One-loop ratio numerical span

Line 590–593 quotes the one-loop suppression ratio as "10⁻⁵⁸ to 10⁻⁶⁰". A
direct evaluation of the formula immediately above gives
10⁻³ × 10⁻⁶¹ / (10⁻² × 6×10⁻³) ≈ 1.67×10⁻⁶⁰, i.e. ~10⁻⁶⁰. The 10⁻⁵⁸ end of
the range is described as reflecting "ε-correction scaling and the eV-vs-GeV
convention", but the convention factor between eV and GeV is exactly 10⁹, not
10²; the 10² discrepancy is therefore not a unit conversion issue. Either
specify the actual sources of the 100× spread or quote the single value
~10⁻⁶⁰ with the band labeled "convention/ε ambiguity ≲ 1 dex". This is
purely a presentation issue; the no-go conclusion is unaffected.

#### m2 (MINOR) [App. B / Eq. dimensions] — Dimensional-analysis "scaling ansatz" framing

The text correctly flags the +1 → +4 mass-dimension gap as a scaling ansatz
rather than a derivation, but the on-shell substitution K~M_Pl, R~M_Pl² is
not justified at the bounce by an EFT power-counting argument; it is a
parametric guess. A parametric guess of M_Pl scaling for K that is off by a
loop factor (4π or g²/16π²) would propagate three orders of magnitude into
ρ_Λ. The paper says "no quantitative conclusion in this paper depends on
resolving this gap" — that is true for the no-go, since the no-go runs in
the *opposite* direction (the operator is too small, not too large). Add one
sentence acknowledging that a fully off-shell EFT derivation could in
principle *enhance* (α/M)·M_Pl by O(10³), strengthening rather than
weakening the no-go.

#### NIT [Abstract / line 102] — Sentence-length grammar

The abstract carries a 35-line embedded clause "Barrier 8 is the observational
consequence of the perturbation-transparency theorem Barrier 14, retained in
the catalog for historical mechanism-class completeness; counted separately
for catalog continuity, the two are not logically independent" that re-states
the same point three times. Tighten to a single phrasing.

### P2 v1.7.24

#### B1 (BLOCKER) [Sec. 9.4 / Joint (f_NL, n_fNL) Fisher; line 367] — Joint-Fisher 9.9σ figure is not reproducible from the manuscript

The Sec. 9.4 paragraph reports σ(n_fNL)=0.086, σ_marg(f_NL)=0.44, ρ=0.966 on a
six-redshift-bin SPHEREx SDB Fisher, yielding a 9.9σ idealized detection
significance for f_NL=-4.375 alone. This is the second-largest detection
significance claim in the paper (after the dual-normalization Cai-convention
5.25σ headline). However: (i) the six-bin Fisher matrix inputs are not
specified — k_min(z), tracer n̄(z) at each bin, b₁(z) prescription, b_φ scheme
(universality vs. per-bin), photometric-z scatter σ_z(z), survey volume per
bin, fiducial cosmology — none of these appear in the manuscript or in any
companion artifact pointer. (ii) The ρ=0.966 correlation between f_NL and n_fNL
is suspicious for a Fisher with non-trivial bin-by-bin geometry: at this
correlation, the eigenvector along (f_NL, n_fNL) is essentially one-dimensional
and σ_marg should grow by 1/√(1-ρ²)=3.78× from the unmarginalized σ. The
paper reports σ_marg/σ_unmarg = 0.44/0.7 → degradation factor 1.57 (claimed),
but ρ=0.966 → factor 3.78 (Fisher-orthodoxy). Either ρ is much smaller than
reported, or the marginal σ is much larger, or the unmarginalized σ is not
0.7. Resolution requires reporting the 2×2 Fisher submatrix
F_{(f_NL, n_fNL)} explicitly. (iii) The 9.9σ "idealized detection" is then
floated against the 5.25σ bispectrum-only headline as if both come from the
same Fisher; they do not, and the relation between them is non-trivial because
the SDB and bispectrum estimators access partially-overlapping information.
**Concrete fix:** report the 2×2 SDB Fisher inputs and submatrix in a new
table; clarify which six bins are used; if ρ is genuinely 0.966 then the
σ_marg(f_NL)=0.44 number is internally inconsistent with σ_unmarg(f_NL)=0.7
and one of the two must be re-derived. As currently written, the 9.9σ figure
is unrechecked and PRL referees will demand the same details.

#### M1 (MAJOR) [Sec. 6 / Bayes-factor MC] — "≥6×10⁵ Monte Carlo realizations" headline disguises an analytic result

Lines 198–219 report the Bayes-factor program "validated over 6×10⁵ Monte
Carlo realizations across three frameworks". The text correctly clarifies
(twice) that the result is analytic and the MC "serves primarily to validate
the analytic Bayes factor formula and map its sensitivity to nuisance
parameter draws". This is an honest disclosure but it is buried *after* the
abstract has already claimed MC validation as a strength. A statistical-
orthodoxy referee will read this as Bayesian-vs-frequentist confusion: the
6×10⁵ realizations are a sensitivity scan over priors, not a frequentist
convergence proof. The Bayes factor depends on prior widths (already shown,
abstract acknowledges the BF~6–17 spread), and the dominant sensitivity is
*to the prior* not *to MC sample size*. **Concrete fix:** either (a) drop
the ">6×10⁵ realizations" framing and quote only the analytic BF with
prior-sensitivity bands, or (b) replace it with the more honest framing
"6×10⁵-sample sensitivity scan over priors and survey-performance nuisance
draws". The current language reads as MC-as-rigor, which it is not.

#### m1 (MINOR) [Sec. 7 / Table II GR-marginalization "Corrected (10% residual)" row] — Sanity row exposed as no-op

Line 287 footnote explicitly admits the "Corrected (10% residual)" row of
Table II is by construction equal to the "Ideal (no GR)" row at the reported
significant-figure level (ΔBF<0.1). Including a no-op row in a 4-row table
where the column tracks BF vs. SSFSR over many orders of magnitude is
confusing — a referee skimming the table will compare 3.3×10⁶ to 3.3×10⁶ and
ask "what does the 10% residual mean?". Either drop the row or footnote-
hoist the equality at the bottom of the table.

#### m2 (MINOR) [Abstract / Table II convention sensitivity] — Halving rule applied incorrectly

The abstract's "Caveat: if Li & Brandenberger c=1 normalization is adopted...
the post-systematic-budget headline 3-5σ halves to ~1.5-2.5σ" is correct in
direction but the Cai/Li factor-of-two is *not* a c=1-vs-c=2 normalization
issue, as Appendix A.1 correctly explains: it is a missing-second-time-ordering
operator-algebra identity, fixed by Hermiticity of H_int. Folding it into a
"convention sensitivity" caveat in the abstract muddles the message. The
detection-significance halving is a real concern only if a reviewer rejects
the in-in commutator-doubling derivation, which is operator-algebra not
convention. **Concrete fix:** in the abstract, label this as "if a reader
disputes the in-in commutator doubling of Appendix A.1...", not as
"convention reversal".

#### NIT [Eq. r definition / footnote text-flow] — Long footnote on r > 1 logic interrupts abstract reading

The 18-line footnote on r > 1 reconcilliation (around Eq. 6) lives on the
abstract's first reading path and is hard to parse on first read. Move to a
section-level note.

### P3 v3.1.35

#### B1 (BLOCKER) [Abstract + Sec. 11 / "Wave 14-II Fisher floor σ(f_NL)≈0.07"] — Internal Fisher forecast claims 3-10× tighter than literature without auditable inputs

The abstract (paragraph following "anchored to the Heinrich+2023 σ_fnl ≈ 0.7
bispectrum-only forecast") and Sec. 11 (line 550) report a "Wave 14-II"
internal multi-tracer Fisher matrix with a 4n+1-dimensional nuisance block
per tracer, marginalizing over (f_NL, δb_i, δs_i, δlog N_i, δσ_z,i) with
priors (0.05, 0.10, 0.10, 0.001), yielding σ(f_NL) → 0.067-0.116 across six
SPHEREx/DESI/anomaly Fisher configurations. The text correctly notes this is
3-10× tighter than the Münchmeyer et al. 2019 consensus σ(f_NL) ≈ 0.4-0.9 for
SPHEREx-class surveys, and attributes the gap to "idealized cross-tracer
correlation strengths" and "no realistic photo-z correlation kernels". This
attribution is not enough. A factor-of-10 disagreement with the
literature-consensus Fisher requires either: (a) showing the cross-tracer
correlation matrix used and its derivation, or (b) re-running with the
Münchmeyer photo-z and bias-prior assumptions and demonstrating the result
maps onto the consensus, or (c) demoting the σ ≈ 0.07 figure from a quoted
result to an explicitly internal-only diagnostic that does not appear in
abstract or section text. Currently the σ(f_NL)≈0.07 figure appears in the
abstract paragraph and in Sec. 11 line 550 in a way that a hurried referee
will read as a real bound. The qualifier "internal consistency check rather
than a literature-consensus forecast" appears two sentences after the number
and does not survive citation. **Concrete fix:** remove the σ(f_NL)≈0.07
number from the abstract; in Sec. 11, gate the figure behind a clear "this
is an internal upper bound on the dimensionless Fisher floor under unrealistic
photo-z assumptions, not a forecast" prefix; release the full 4n+1 covariance
matrix as a companion artifact so the cross-vendor reviewer can verify the
attribution to "idealized cross-tracer correlation".

#### M1 (MAJOR) [Sec. 5.7 / Sec. 12.5 / Fig. caption fig:injection_recovery] — Abstract claims "3 PASS" injection-recovery; figure caption shows "1 PASS"

The abstract (line 54) claims "Six injection-recovery gates yield 3 PASS
(SDSS continuum-dip, Planck CMB native, NEOWISE) and 3 below the formal
≥50% threshold at 5σ". The figure caption for fig:injection_recovery
(line 603, Sec. 12.5(v)) however reports: "SDSS DR18 continuum-dip (PASS,
64%) is the only survey clearing the gate. Five surveys fail with companion
cross-validation diagnostics". The two statements disagree on which surveys
PASS the 5σ injection-recovery gate. The Path-C protocol (Sec. 5.7) defines
the gate in two parts: criterion (a) val_loss ≤ 0.30 *or* criterion (b)
≥50% recovery at 5σ. NEOWISE is a spatial-mask intervention not an
autoencoder retrain, so its "PASS" applies to a different metric
(specificity 1.51% vs. theory 1.52%, sensitivity 100% at polar caps), not
to the 5σ continuum-dip recovery. Planck CMB native gets 100% recovery on
Gaussian-bump plants at 5σ — this is the criterion-(b) PASS the abstract
counts. So the abstract's "3 PASS" mixes criterion (b)-spectroscopic
(SDSS), criterion (b)-CMB (Planck), and criterion (b)-spatial (NEOWISE),
which are not the same metric. The figure caption uses only the
spectroscopic-criterion-(b) interpretation. This is the kind of accounting
ambiguity that causes ApJS referees to ask for the protocol re-stated in
one place. **Concrete fix:** align the figure caption to the abstract's
3-PASS framing, with explicit metric labels per survey (continuum-dip 5σ
vs. Gaussian-bump 5σ vs. spatial-mask specificity-and-sensitivity), or
align the abstract to the figure's 1-PASS framing by separating
metric-equivalence from metric-different surveys.

#### M2 (MAJOR) [Sec. 11 / α_jk = 0.19 ± 0.65 → σ_fNL = 8.27 ± 2.37] — Forecast uncertainty propagated linearly through a non-linear Fisher; check formula

The Wave 14-VVV result α_jk = 0.19 ± 0.65 is propagated to σ_fNL = 8.27 ±
2.37 via "linear scaling of the fiducial 7-bin Fisher result at α=0.15"
(stated in App. A, line 716). At α=0.15, σ_fNL=8.43. Linear scaling
Δσ/σ_std = (6.1%/0.15)·α = 0.407·α gives:
- α=0.19: σ = 8.98·(1-0.407·0.19) = 8.98·(1-0.0773) = 8.29 (consistent
  with reported 8.27)
- α=0.19+0.65=0.84: σ = 8.98·(1-0.407·0.84) = 8.98·0.658 = 5.91
- α=0.19-0.65=-0.46: σ = 8.98·(1+0.407·0.46) = 8.98·1.187 = 10.66
  (reported +1σ tail = 10.64; consistent)

The asymmetry of the propagated uncertainty (8.27 + 2.37 = 10.64 OK; 8.27 -
2.37 = 5.90 OK only on the σ_fNL side, since α=0.19+0.65 produces σ=5.91)
is hidden by reporting it as ±2.37 symmetric. This is a Bayesian-vs-
frequentist orthodoxy issue: the linear-scaling map is not symmetric in α,
so the ±2.37 should be asymmetric (~+2.37 / -2.36 — accidentally close to
symmetric only because we're near α=0.19 where the slope is shallow), but
also the 95% CI α∈[-1.08, +1.46] *does* include the regime α<-1/0.407 ≈
-2.46 where the linear-scaling map predicts σ_fNL > σ_fNL^std (no
improvement, formally a degradation). The α=-1.08 endpoint maps to σ_fNL =
8.98·(1+0.407·1.08) = 12.92, beyond what is reported. **Concrete fix:**
either propagate via MC over the full α-jackknife distribution and quote
asymmetric uncertainties on σ_fNL, or restate σ_fNL=8.27 as the central-
value forecast and quote the 95% CI σ_fNL ∈ [linear-scaled bounds] without
hiding the asymmetry. The current ±2.37 is misleadingly symmetric.

#### m1 (MINOR) [Sec. 5.7 / Step 1 (b) gate] — Two-part gate "criterion (a) OR (b)" admits Planck CMB at val_loss=0.4437 by criterion (b)

The Path-C two-part gate is criterion (a) val_loss ≤ 0.30, OR criterion (b)
≥50% injection-recovery at 5σ. Planck CMB native fails (a) at 0.4437 (50%
above threshold) but passes (b) at 100% — admitted under (b). The text
justifies the OR-gate by noting "the near-Gaussianity of the input
distribution sets a floor on achievable per-pixel reconstruction MSE that
is quantitatively higher than the 0.30 threshold but does not preclude
unambiguous anomaly detection". The justification is conceptually sound
but quantitatively unsupported: how does 0.30 relate to the floor of a
near-Gaussian input distribution? In a CMB temperature field with σ_T ~
30 µK at 64×64 patches, the per-pixel MSE floor under a perfect identity
map is ~σ_T² in the natively-scaled units, which depending on
normalization could be 0.4 or could be 1.0 — the 0.4437 result has to be
compared against this floor, not against the 0.30 cross-survey threshold.
Add one sentence quantifying the irreducible MSE floor for the CMB input
distribution and showing 0.4437 is within ~10% of it.

#### m2 (MINOR) [Sec. 5.6 / 7-way 5″ dedup] — False-match expectations vs. observed cluster count

Sec. 6.3 line 477 estimates ~10 expected random coincidences across all
survey pairs at 5″, vs. observed 637 multi-survey clusters. The 637 is a
strong signal that the matches are real, not random. But the 10-vs-637
ratio is 1:64, and the false-match estimate uses global mean source
densities; line 477 admits "position-dependent estimates using local
density (which varies by >10× between Galactic plane and poles) would
give more accurate per-source false-match probabilities". Add a sky-
density-stratified false-match calculation (or release as a companion
artifact) — without it, a referee can challenge the 0.1%-per-pair claim
in dense fields like the Galactic plane and the LMC, where eROSITA's 298
top anomalies concentrate.

#### NIT [Tables tab:bayes / tab:gr / tab:sensitivity] — "Three Bayes-factor tables" for one underlying Fisher input

The paper has tab:bayes (4-row prior sensitivity), tab:gr (4-row GR
sensitivity), and tab:sensitivity (8-row α sensitivity), plus the in-prose
2×2 prior-corner. Five places to look up "what is the Bayes factor for X".
Consolidate into one master table.

### P4 v1.0.44

#### M1 (MAJOR) [Sec. 14 / MASTER deconvolution -0.12σ at N_MC=500] — Wilks-style threshold test on a non-Gaussian post-MASTER null

The MASTER-deconvolved ℓ=1 result is C₁_meas = 1.49×10⁻⁶, ⟨C₁_null⟩ =
1.55×10⁻⁶, σ_null = 4.29×10⁻⁷ from N_MC=500 realizations of the full
M_ℓℓ' inversion. The "-0.12σ" significance is computed as
(C_meas - ⟨null⟩)/σ_null. This is fine *if* the MASTER-deconvolved null
distribution is approximately Gaussian. The N_MC=500 footnote (line 1073
fn:mc_count) acknowledges 4.5% MC uncertainty on σ_null but does not
test the Gaussianity assumption. For a chi-squared estimator with 1 dof
(post-deconvolution single-mode pseudo-C_ℓ at ℓ=1), the null distribution
is NOT Gaussian and Wilks' theorem doesn't apply at this multiplicity —
the proper statistic is a likelihood ratio against a Gaussian quadratic
form, not a (x-μ)/σ z-score. With the deviation at -0.12 (well within
typical chi-squared scatter at 1 dof) the conclusion "fully consistent
with null" is correct, but the *quoted significance* "-0.12σ" implicitly
assumes Gaussianity. **Concrete fix:** report the empirical p-value from
the 500-MC null distribution (the rank of C_meas in the sorted null), not
just the z-score; and add one sentence on why a Gaussian approximation
is justified at this null amplitude (or use the Anderson-Darling or
Kolmogorov-Smirnov statistic against the empirical null).

#### m1 (MINOR) [Sec. 6 / Eq. for σ_global] — Discrepancy between abstract 9.5σ and direct calculation

Abstract reports CW/(CW+CCW) = 0.4974 ± 0.0003 at 9.5σ from 0.5000.
Direct: σ_p = √(p(1-p)/N) at N=3,201,160, p=0.4974 → σ_p = 0.000279.
(0.5 - 0.4974)/0.000279 = 9.32σ, not 9.5σ. The text uses three-significant-
figure σ=0.0003 → (0.5000-0.4974)/0.0003 = 8.67σ. None of these match
9.5σ exactly. The 9.5σ is presumably from a more precise σ
calculation or a different effective N — but the headline number should
match the supporting calculation to one decimal place. **Concrete fix:**
either re-compute or footnote the precise definition of σ used in the
9.5σ statement.

#### NIT [Sec. 6 / r=1 reconciliation footnote] — Long expository footnote could be inline

The footnote explaining why r > 1 is allowed for the matter-bounce shape
(Sec. on Eq. r-bound) is itself a useful piece of reasoning that belongs
in the main text, not as a 12-line footnote.

---

## Cross-paper consistency issues (flagged but not double-counted in summary)

1. **PTA γ inconsistency P1A vs. P3** (counted as P1A M1). P1A still cites
   γ=3.20±0.42 (synthetic-from-power-law summary fit); P3 explicitly
   supersedes this with γ=2.567±0.382 (real-KDE-likelihood). The
   bounce-prediction deviation flips from 0.48σ (P1A claim) to +1.13σ
   (P3 claim). CLAUDE.md line 58 carries the stale value.

2. **σ(f_NL) anchor inconsistency P2 vs. P3.** P2 quotes σ(f_NL)≈0.7 from
   Heinrich+2023 as the SPHEREx bispectrum-only baseline; P3 quotes
   σ(f_NL)^std = 8.98 as the DESI-only standard QSO baseline. Both are
   correct in their own contexts (different surveys, different sufficient
   statistics) but a reader looking at both papers will be confused about
   which is "the" σ(f_NL). Add a one-line cross-reference in P3 abstract
   clarifying that 8.98 is DESI-only and 0.7 is SPHEREx-bispectrum-only.

3. **f_NL = -35/8 = -4.375** is consistent across all four papers. ✓
   **β = 0.27°** ALP birefringence is consistent across P1A and P2. ✓
   **N_total ≈ 92** dark-energy suppression is consistent in P1A. ✓
   **σ_pix calculation in P4** is reproducible: 1/(2√4168) = 0.00774 → 0.77%. ✓

---

## Summary in one paragraph

This is a careful four-paper bundle, post four CCAI rounds. The same-vendor
reviewer would likely have nothing left to find. As a different-vendor
reviewer with numerical-rigor priors, I find: (1) a stale PTA γ in P1A that
must be reconciled with P3 before either ships (1 MAJOR, 1-line fix); (2) an
under-specified σ_marg(f_NL)=0.44 / ρ=0.966 joint Fisher in P2 Sec. 9.4
that doesn't reproduce from the manuscript (1 BLOCKER, requires Fisher
submatrix to be released); (3) a P3 internal Fisher floor σ(f_NL)≈0.07 that
disagrees with literature consensus by 3-10× and appears in the abstract
without sufficient gating (1 BLOCKER, fix is to demote the figure or release
the cross-tracer correlation matrix); (4) a P3 abstract-vs-figure-caption
PASS-counting conflict (1 MAJOR); (5) a P3 asymmetric-uncertainty
propagation hidden by symmetric ±2.37 reporting (1 MAJOR); (6) a P4
"-0.12σ" significance that implicitly assumes Gaussianity of the
post-MASTER 1-dof null at N_MC=500 (1 MAJOR). Plus 7 minors and 4 nits.
**Honest count: 2 BLOCKER + 5 MAJOR + 7 MINOR + 4 NIT = 18 findings, mostly
on P2 and P3.** Houston is paying for adversarial diversity, not echo
chambers; this is what cross-vendor finds that same-vendor systematically
under-flags.
