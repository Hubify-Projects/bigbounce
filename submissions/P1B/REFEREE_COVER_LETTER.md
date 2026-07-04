# Cover Letter — Paper 1B

**Title area:** Reproducibility and null-consistency material for the ECH spin-torsion cosmology program (companion to Paper 1A)
**Source:** `arxiv/paper1b_mcmc_companion.tex`
**Suggested venue:** Physical Review D (companion / supplementary to Paper 1A), or an ApJS reproducibility note

Dear Editor,

Please consider this manuscript. This cover letter states its contribution,
scope, and limitations plainly.

## Contribution
The paper documents three adjacent numerical cross-checks for the
Einstein–Cartan–Holst (ECH) spin-torsion program of Paper 1A: (1) a stock-CAMB
ΛCDM+ΔN_eff MCMC null-consistency proxy (Cobaya v3.6.1, 309,189 frozen samples
across two converged dataset combinations, finding ΔN_eff consistent with zero
and H₀ consistent with Planck-ΛCDM, with the ~3.6σ SH0ES tension unreduced); (2)
a foreground-free synthetic-sky NaMaster pipeline recovery validation; and (3) a
GR+ALP literature-data accommodation with the tuning honestly quantified
(25×/100×). It additionally derives from first principles the bespoke ECH-sector
ΔN_eff contribution, which scales as (T/M_Pl)² and is astrophysically negligible
(~10⁻⁴⁴). All three reviewers confirmed the material error-clean: the §III.A
ΔN_eff derivation was accepted and a prior dimensional bug was fixed.

## Scope statement
This is a **technical reproducibility / consistency-check companion, not
independent evidence for (or verification of) the spin-torsion theory.** The
abstract's "Scope, stated up front" paragraph says so directly: none of the three
analyses implements or tests a torsion-modified Boltzmann/theory module, and none
verifies the ECH spin-torsion sector. Each is a bounded numerical cross-check —
a ΛCDM proxy, a synthetic-pipeline validation, and a literature accommodation.

## Disclosed limitations (stated up front)
1. **Zero direct ECH-sector verification.** The stock-CAMB proxy uses generic
   extra radiation, not the torsion-modified sector; the abstract and §III both
   state this explicitly.
2. **Synthetic, foreground-free NaMaster validation** with a disclosed β–α
   degeneracy scope note — a pipeline-recovery check, not a real-sky measurement.
3. **ALP accommodation** is a GR+ALP fit to literature data with the tuning
   (25×/100×) quantified in-text, labeled by-design-limited.

Note: the exploratory overlap-uncorrected w0wa supernova appendix — the sole
basis of an earlier external reject — was **surgically cut** (v1B.0.95), as it
was orthogonal to the paper's core ECH/NaMaster/ALP results and zero-cost to
remove. A post-cut external re-check returned a genuine **Gemini ACCEPT**, with 0
genuinely-new findings surviving truth-audit.

## The judgment for the referee
The one residual question — flagged by an LLM referee as a subjective
venue/scope opinion, not a correctness defect — is: **is a reproducibility /
consistency-check companion a standalone PRD article, or is it best published as
supplementary material to Paper 1A?** The paper is scoped up front as exactly a
companion note; we believe it belongs alongside Paper 1A as a PRD companion (or
as an ApJS reproducibility note) and defer the format call to your editorial
judgment. No manuscript change is needed to resolve it.

No genuinely-new correctness defect is outstanding.

Sincerely,
Houston Golden (houston@hubify.com)
