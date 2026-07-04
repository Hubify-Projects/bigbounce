# Cover Letter — Paper 4

**Title area:** A survey-scale chirality-labeled galaxy catalog and a null spiral-handedness dipole
**Source:** `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Suggested venue:** Physical Review D (or ApJ / MNRAS)

Dear Editor,

Please consider this manuscript. This cover letter states its contribution,
scope, and disclosed limitations plainly.

## Contribution
The paper presents, to our knowledge, the largest chirality-labeled galaxy
catalog to date: 8,474,531 DESI Legacy DR8 galaxies classified by a
flip-equivariant Vision Transformer pipeline (3,201,160 spirals), released with
weights and reproducibility scripts. Its primary scientific result is a
**real-space chirality dipole consistent with null** at sub-percent sensitivity:
+0.41σ on the high-confidence equivariant sample against an isotropic
permutation null, with a block-bootstrap WLS template fit disfavoring a clean
1.7% cosmological dipole. The null is verified-robust: the confidence cut
(p_eq > 0.6) is git-pre-specified in the generator script (not tuned post-hoc);
the null holds across the high-confidence regime; a systematic battery brackets a
step-function detection floor (A₉₅ between 1.0% and 1.5%); and — importantly — a
GZ1-only sub-model trained on human labels alone recovers the same null
(z ≈ −0.04).

## Scope statement
This is a **standalone observational null result**, not a detection and not a
direct parity-violation test — the ℓ=1 observable is parity-even
(isotropy-breaking axial-vector channel). The harmonic MASTER pseudo-C_ℓ channel
is explicitly a **systematics diagnostic, not an independent cosmological null**:
its post-MASTER residuals are attributed to residual survey systematics and are
not claimed as detections.

## Disclosed limitations (stated up front)
1. **~Half of the ℓ=1 residual is unexplained.** The eight-anchor forward model
   accounts for only ~52–54% of the observed canonical-mask ℓ=1 systematic
   residual amplitude; ~47% remains an explicit, disclosed open item. The central
   null rests on the systematics-bypassing real-space primary estimators, not on
   the harmonic residual — but we disclose the residual gap up front rather than
   overclaiming full accounting.
2. **Pseudo-label independence.** ~66.5% of training labels derive from CE-ResNet
   predictions, so the shuffle nulls randomize the model's own outputs and do not
   by themselves rule out inherited large-scale structure. This is bounded by the
   GZ1-only (human-label) null and the template-regression / cross-spectrum
   diagnostics of Appendix D, and disclosed as a corollary limitation.

## The judgment for the referee
The questions LLM referees flag but cannot fully adjudicate are: **(a) is the
~47% unexplained ℓ=1 residual — with the primary null resting on independent
systematics-bypassing estimators — an acceptable disclosed limitation, or must
the forward model close the residual first? And (b) is the GZ1-only human-label
null plus the sub-1.5% inherited-dipole ceiling a sufficient independence
demonstration, or does a full-catalog re-inference at headline sample size on
human labels alone gate publication?** We believe the pre-specified cut, the
step-function systematic characterization, and the human-label GZ1 null make this
a robust, honestly-disclosed null; we ask you to weigh these two open items.

No genuinely-new correctness defect is outstanding.

Sincerely,
Houston Golden (houston@hubify.com)
