# Cover Letter — Paper 1B

**Title area:** Reproducibility and null-consistency material for the ECH spin-torsion cosmology program (companion to Paper 1A)
**Source:** `arxiv/paper1b_mcmc_companion.tex` (v1B.0.101, 22 pp)
**Bundle:** `submissions/P1B/arxiv_p1b_v1B.0.101.tar.gz`
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
(~10⁻⁴⁴) — a genuine, self-contained result of *this* companion (derived here,
not imported from Paper 1A). The internal full-source review (with access to the
source, chains, and scripts) verifies that the three data-backed results
reproduce from committed artifacts and rates the manuscript error-clean up to
minor items; the §III.A four-fermion ΔN_eff derivation was accepted, and the one
concrete quantitative issue the external referees raised — a
reduced-vs-non-reduced Planck-mass inconsistency in the boxed ΔN_eff numbers —
has been fixed (v1B.0.100), so the values now reproduce directly from (T/M_Pl)².

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
remove.

## Coordinated submission
This is Paper 1B of a coordinated two-paper posting: **1B posts to arXiv in the
first wave so that Paper 1A can cite its assigned arXiv identifier same-day** (and
reciprocally). Cross-references to Paper 1A carry a clearly-marked
`[arXiv:XXXX.XXXXX]` placeholder that is replaced with the real identifier at
submission; the procedure is documented in `submissions/P1B/SUBMISSION_NOTE.md`.

## Current external-review status (stated honestly)
The most recent external LLM-referee sweep (2026-07-05, raw responses archived
under `project-context/peer-reviews/EXT_real/ROUND_2026-07-05/`) returned
scope/venue objections: ChatGPT (reject) and Gemini / Grok (major revisions) all
argue the work reads as a technical companion to Paper 1A rather than a
standalone advance, and re-flag the paper's own honestly disclosed limitations
(generic-radiation proxy, foreground-free synthetic skies, GR+ALP accommodation).
No genuinely-new correctness defect survived truth-audit against the source; the
single concrete quantitative item (the ΔN_eff Planck-mass convention) was real
and is fixed. The residual objection is therefore the venue/format judgment
below, not a content error.

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
