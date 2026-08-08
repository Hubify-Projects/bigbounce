# INT v3 — Independent Referee Report (P2)

- **Model:** claude-opus-4-8 (Claude Code subagent, orchestrated leg)
- **Date:** 2026-07-17 PT
- **Paper:** P2 — "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping" — v1.7.124
- **PDF SHA-256:** b691bdb2f3758f3f460633141c005193d312f7f530a304eb1b8911836591833a
- **Exactness gate:** PASS (computed SHA-256 equals the bound hash)
- **Venue:** Physical Review D — profile PRD-RESEARCH
- **Prompt:** "You are an expert referee for Physical Review D. Review this Research Article manuscript under profile PRD-RESEARCH to the standard of a real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim supported?"
- **PARSED VERDICT:** MAJOR REVISIONS

---

## RAW VERBATIM REPORT

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Sec. IX / App. B (central correction claim). The paper overturns a
published number by asserting the exact matter-contraction squeezed amplitude is
f_NL = -35/16, not Cai et al.'s -35/8. But the paper itself states that TWO
independently published final polynomials — Cai et al.'s Eq. (37) and Li et al.'s
Eq. (4.19) — "agree coefficient-for-coefficient at c_s = 1" and both squeezed-reduce
to -305/64. The correction therefore requires the reader to accept that two
independent transcriptions are wrong in the same way, and that the vertex-sum
reading (-35/16) trumps both agreeing printed polynomials. Two independent
published polynomials converging on the same value is nontrivial evidence; the
manuscript must confront this tension head-on (e.g., establish that Li's printed
polynomial is a copy of Cai's rather than an independent transcription, or show
where each printed polynomial diverges from its own vertex sum) rather than
resolving it by fiat toward the vertex read.

2. [MAJOR] Sec. II.A / Table I / App. B (unexplained uniform factor of two). All
three benchmark configurations are reported as exactly one-half of Cai's stated
values (squeezed -35/16 vs -35/8, equilateral -255/128 vs -255/64, folded -9/8 vs
-9/4). A uniform factor of two across squeezed, equilateral, AND folded is the
canonical signature of an overall normalization / symmetry-factor / f_NL-definition
convention difference — NOT of the spurious -(99/128) Σk_i^3 term the paper
identifies, which is shape-dependent and (by the paper's own arithmetic) shifts the
squeezed value to -305/64, not to any clean 2x multiple. The paper explains the
printed-polynomial discrepancy but leaves the stated-value uniform 2x unexplained,
while simultaneously asserting "same 10/(3 Σk^3) convention, same squeezed limit."
The uniform 2x is circumstantial evidence against that assertion and must be either
mechanistically located or the "erroneous published value" framing softened.

3. [MAJOR] Self-containedness of the decisive reduction (App. B, Tables IV–V,
Eqs. B2–B5). For a manuscript whose primary contribution is correcting a published
result, the load-bearing step — reducing the four general-epsilon vertex expressions
of Table IV to the per-vertex limits of Table V and to the -305/64 printed-polynomial
reduction — is repeatedly deferred to uncited-in-detail scripts
(p2_vertex_check.py, caili_certification/cai_conv.py, cai_shape.py). A PRD referee
cannot run these, and the result should stand on the printed derivation alone. Add
the explicit hand-checkable reduction (at least for the squeezed limit) so the
-35/16 vs -305/64 vs -35/8 arbitration is verifiable in the manuscript.

4. [MAJOR] Scope/significance (Secs. III–VIII, ~40% of the paper + abstract). The
extensive SPHEREx/LSS mapping, template-projection recovery (r), redshift-space
Fisher, and channel-native nuisance ladder are repeatedly and explicitly disclaimed
as "illustrative, not an observational headline," resting on an in-house surrogate
covariance that the paper says "does not replace the unpublished external per-triangle
covariance." As written the paper is a focused technical correction wrapped in a
conditional forecast that the paper itself declares carries no observational weight.
For a Research Article the author should either (a) commit to the forecast by
obtaining/constructing the actual SPHEREx per-triangle covariance, or (b) trim the
conditional apparatus substantially and present the paper as the technical correction
it primarily is. The current structure risks overselling.

5. [MINOR] Sec. III.B / IV. Reporting r = 0.83542294 and r_cos = 0.98167825 to
eight significant figures while simultaneously adopting r = 0.84 ± 0.02 as the
meaningful value is inconsistent precision; quote the flat-grid value to a
justifiable number of digits.

6. [MINOR] Sec. VIII (data consistency). The Planck PR4/NPIPE mapping (f_NL^bounce
= -0.11 ± 5.71, "0.37 sigma from -35/16") is a null diagnostic — the same data are
0.02 sigma from zero — so it discriminates nothing. It is stated honestly, but as
presented it reads as support when it is not; label it explicitly as non-discriminating.

7. [MINOR] Sec. II.B / Eq. (5). The torsion-sourced correction bound is an
order-of-magnitude parametric estimate ("carried symbolically... not fixed by any
committed artifact") whose Einstein–Cartan–Holst coefficient audit is sourced to
Ref. [14], an unpublished companion ("in preparation, this volume"). A load-bearing
input to Sec. II.B should not depend on an unpublished companion; either self-contain
the coefficient or downgrade the claim's status.

8. [MINOR] App. B organization. The two distinct discrepancies (printed-polynomial
vs vertex-sum, and stated-value vs vertex-sum) and the A^epsilon / A^{epsilon^2} /
A^{epsilon^3} decomposition are dense and easy to conflate; the appendix would be far
clearer if the two discrepancies were separated into labeled subsections with a
single summary table of the three competing values (-35/8, -305/64, -35/16) and what
supports each.

(3) The central claim (exact matter-contraction f_NL = -35/16) is internally
self-consistent and has one genuinely independent cross-check (Li et al.'s general-c_s
in-in formula at c_s = 1), but it is not yet established to PRD's standard for
overturning a published result, because two independently printed final polynomials
agree on a different value (-305/64), the uniform factor-of-two versus the stated
-35/8 is unexplained and convention-suggestive, and the decisive reduction is deferred
to code rather than shown in the manuscript.

---

## Reviewer verification notes (not part of the verbatim report)

- Exactness gate passed before review; SHA-256 matches bound value.
- Independently checked internal algebra: Table V squeezed column
  (-25/16, -5/32, 0, -15/32) sums to -35/16; equilateral column
  (-35/32, -5/32, -5/8, -15/128) sums to -255/128 — both correct.
- Eq. (B4) 256 Πk² A coefficients (9, 3, -27, 15, -198, 27) = 3× the Eq. (3)/(4)
  ordered-basis vector (3, 1, -9, 5, -33, 9); consistent with A = (3/256)K_9/Πk².
- Eq. (B5) verified via raw text extraction: f_NL|ε¹ = -5/2, f_NL|ε² = +5/16,
  f_NL|ε³ = 0, sum = -35/16 — internally consistent (an initial image-read
  suspicion of a B5 inconsistency was checked against pdftotext and withdrawn).
