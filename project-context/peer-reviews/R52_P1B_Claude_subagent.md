# R52 — P1B Referee Report (Claude / Opus leg)

**Recommendation: MINOR REVISIONS**

Paper: P1B — "Technical Verification Companion to the ECH Spin-Torsion Program:
ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence
Consistency Check with a Spectator-ALP Model."
PDF reviewed end-to-end (21 pp). Source truth-audited: `arxiv/paper1b_mcmc_companion.tex`.

Summary judgment: This is an unusually honest and internally consistent paper.
Every σ-tension, the precision-weighted S8 combination, the Eq.(4) birefringence
product, the w_pivot decorrelation in the Table II footnote, and the χ²
decomposition all reproduce on independent recomputation. The three analyses are
explicitly scoped as null/compatibility checks, not detections, and the scope
limitations are stated in the abstract and at every point of use. There are no
fabricated or irreproducible core claims, hence no blockers. The remaining items
are (a) two methodologically substantive controls that are disclosed but
deferred, and (b) clarity/reproducibility-presentation issues. None require
substantial scientific rework of the load-bearing conclusions (ΔN_eff consistent
with zero, H0 recovers ΛCDM, NaMaster validates the deconvolution algebra, ALP β
consistent with the published value), so the verdict is MINOR REVISIONS with two
MAJOR-tier comments the authors should close or down-scope before submission.

---

## 1. BLOCKERS

None. The three headline results are each backed by committed chains/artifacts
(`reproducibility/cosmology/frozen/...`, `reproducibility/p1_namaster_500mc/...`,
`research/branch_R_alp_birefringence/phase2_mcmc/chains/...`), the arithmetic is
self-consistent, and every limitation that could otherwise be a blocker is
disclosed in-text. Nothing here is wrong-as-rendered or unsupported-as-claimed.

---

## 2. MAJORS

**MAJOR-1 — The w0wa quintom-B significances (Table II; §V.C; caveat (e), §IV
Physics-interpretation paragraph) rest on an overlap-uncorrected product
likelihood whose known bias points toward the reported signal.**
Table II reports w0 = −0.8122 ± 0.0436 (+4.3σ from −1), wa = −0.6666 ± 0.1864
(−3.6σ from 0), w0+wa = −1.4788 ± 0.1485 ("phantom crossing indicated"). The
iter2 likelihood multiplies DES-SN5YR and Pantheon+ as independent factors while
the two catalogs share ≈20% of supernovae with different Malmquist corrections
(caveat (e), citing Vincenzi et al. 2025, arXiv:2501.06664). The paper itself
states the double-counting bias direction is *toward* w0+wa < −1 — i.e. toward
the very quintom-B signature being reported — and that a rigorous joint-covariance
treatment "has not been demonstrated quantitatively." Reporting 4.3σ/3.6σ figures
in a results table, even heavily caveated, invites out-of-context citation of a
number the authors do not actually claim.
*Proposed fix:* run the queued SN-overlap-controlled w0wa re-fit (the tex
comments at lines 216–224 already scope this) with a joint DES-SN5YR×Pantheon+
covariance, OR demote Table II to posterior means/widths only and remove the
"+4.3σ / −3.6σ / phantom-crossing-indicated" significance annotations, relegating
them to text framed strictly as marginal-tail extrapolation distances. The two
disclosed SN-overlap control chains (DESI+Planck+Pantheon-only;
DESI+Planck+DES-SN5YR-only) would close this directly if reported here rather
than deferred.

**MAJOR-2 — The NaMaster validation does not exercise the systematic that the
real measurement actually depends on (Sec. IV; tex line 1116).**
The 500-MC suite injects β onto synthetic ΛCDM skies that "contain no galactic
foregrounds, so the very component that breaks the β–α degeneracy in published
Planck/ACT DR6 measurements is absent by construction." The MC therefore
validates the algebraic E→B pseudo-C_ℓ deconvolution under MASTER mode coupling
— the tractable part — but not the foreground-driven separation of the
cosmic-rotation angle β from the instrument miscalibration angle α, which is the
error-prone step in any real birefringence detection. Consequently the 0.040°
"worst-case pipeline bias floor" carried forward (§IV) is a bias on foreground-
free recovery and may not bound the real-sky bias, yet it is presented as *the*
NaMaster systematic floor.
*Proposed fix:* add at least one foreground/α-rotation injection MC (or a
beam-mismatch MC, currently also deferred) to demonstrate the floor is robust to
the dominant systematic; OR explicitly restrict every downstream use of the
0.040° floor to "deconvolution-algebra bias on foreground-free skies, not a
real-sky bias bound," wherever the figure is quoted. The current single
disclosure sentence is necessary but does not make the control complete.

---

## 3. MINORS

**MINOR-1 — Sample-count proliferation in footnote 1 is hard to audit (p.3).**
Footnote 1 cites 309,189 / 216,432 / 176,240 / 132,949 / 123,368 / 123,129 /
123,066 / 119,617 / 106,361 / 93,066 / 93,064 / 114,992 with several
reconciliation sub-notes (burn-in convention, GetDist weight-thinning, per-chain
rounding). The reconciliation is correct but unfollowable in prose.
*Fix:* replace the footnote narrative with a small table (raw / post-burn-in /
GetDist-effective per chain per dataset), keeping one footnote pointer.

**MINOR-2 — Fiducial β = 0.27° vs Eq.(4) result 0.28° (abstract; §VI Eq.(4)).**
Eq.(4) evaluates the product to β ≈ 0.28° while the stated fiducial is 0.27°.
The text attributes this to retaining the four-figure Δφ/f_a = 1.06 vs the
two-figure prefactor, but the two values appear side by side without flagging
which is canonical.
*Fix:* state once that 0.27° is the rounded fiducial and 0.28° is the
four-figure EOM evaluation, and use one consistently downstream.

**MINOR-3 — Eq.(3) presents Δφ/f_a = 0.42 (m = 2H0, θ_i = 1) as "the" field
displacement, but the fiducial β uses Δφ/f_a ≈ 1.06 at m ≈ 3.9H0 (§VI).**
A reader plugging Eq.(3)'s 0.42 into Eq.(4) gets ≈0.11°, not 0.27°. The box
spans 0.064–1.19 and the resolution is internally consistent, but the juxtaposition
of Eq.(3)'s 0.42 with the 1.06 used in Eq.(4) is pedagogically confusing.
*Fix:* annotate Eq.(3) that 0.42 is one corner of the (m, θ_i) box and that the
fiducial sits at the m ≈ 3.9H0 / Δφ/f_a ≈ 1.06 point.

**MINOR-4 — Canonical f_sky = 0.32 artifact lacks per-realization σ_β; required a
rerun (Fig. 3b; fn. 4).** The error bars in Fig. 3(b) come from a dedicated rerun
because σ_β "was not recorded in the original canonical artifact." Disclosed and
immaterial to the central value, but a reader reproducing Fig. 3 from the
committed canonical JSON cannot recover panel (b).
*Fix:* commit the rerun's per-realization scatter alongside the canonical
artifact, or note the exact rerun script/seed in the Fig. 3 caption (currently
only in fn. 4).

**MINOR-5 — No model-selection statistic anywhere (ΔAIC/ΔBIC/lnB), for any of the
three analyses (§V; Table V).** The paper makes "compatibility" statements but
never a Bayesian model comparison, deferring lnB to a nested-sampling follow-up.
This is legitimately scoped, but it limits the inferential reach of a paper whose
parent program (Paper I(a)) claims bounce > ΛCDM+inflation: a verification
companion that reports only parameter posteriors cannot, on its own, support any
preference statement.
*Fix:* add one sentence in §V and the abstract making explicit that this paper
establishes *compatibility only* and that all model-preference inference is
deferred — so the companion is not mis-cited as evidence for the bounce.

---

## 4. STRENGTHS

- **Exceptional transparency.** Every analysis carries an explicit scope statement
  ("Not a spin-torsion theory module," "Not a competitive sky detection," "Not a
  distinctive ECH prediction") in the abstract, the section head, and at each
  point of use. The paper never overclaims; the spectator-status fine-tuning, the
  SN-overlap systematic, and the foreground-free validation limitation are all
  disclosed where a less careful paper would bury them.
- **Internally consistent arithmetic.** Independent recomputation of the
  σ-tensions (w0 +4.3σ, wa −3.6σ, w_pivot +2.5σ), the precision-weighted S8
  two-Gaussian combination (0.827⊗0.776 → 0.814 ± 0.009), the Eq.(4) birefringence
  product (5.81×10⁻⁴ × 8 × 1.06 → 0.28°), the w_pivot decorrelation (a_p = 0.210,
  σ_wpivot = 0.019), and the χ² decomposition (10.6+10983.9+3043.0 = 14037.5) all
  reproduce to quoted precision. This is rare and reflects real care.
- **Committed, regenerable reproducibility layer.** Frozen chains, NaMaster MC
  artifacts, ALP chains, a CORRECTED parameter-summary with a documented
  off-by-one column-bug disclosure, an independent re-run cross-check
  (ΔN_eff = +0.0514 ± 0.171, 0.04σ vs frozen), an independent external
  cross-validation (Liu et al. 2025, agreeing at 0.5σ in H0 / 1.3σ in S8), a
  KNOWN_GAPS.md, and a claims-classification table (Table V) keyed to commit
  b22f8cc9. The work can be audited from the committed branch.
- **Honest negative/null framing throughout.** The ΔN_eff null is presented as a
  bounce-class compatibility check, not spun as a detection; the H0 result is
  reported as "does not resolve the Hubble tension"; the ALP birefringence is
  correctly identified as arising identically in GR and therefore not ECH-specific.
  This is exactly the disposition a verification companion should have.
