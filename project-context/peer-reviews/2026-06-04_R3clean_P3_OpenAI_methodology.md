# P3 2026-06-04_R3clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 49.2s

---

Referee report – Physical Review D  
Manuscript P3   “Spectrally Unusual Sources at Scale …”  
Round: 2026-06-04_R3clean   (≈50 pp)

I have audited the statistics, derivations, internal arithmetic and error‐propagation.  
Findings are grouped by severity.

--------------------------------------------------------------------
ESSENTIAL (paper cannot be accepted without correction)
--------------------------------------------------------------------

P3-E1   Fisher-coefficient inconsistency  
• Sec. V, p. ?? (“…1/σ(fNL )2 = F0 + c α2 with F0 = 1/8.982…”)  
• Appendix VI D(i) (“…anchor values (F0 ,c)=(1/80.64,0.0747)…”)  
The same formula is quoted with two different F0. 1/8.982 gives
σfloor = 2.998, not 8.982.  
Required fix: unify the definition (either 1/σ or 1/σ2) and recompute every
σ(fNL) number, text and figure that depend on it (8.14, 8.27±2.37,
[3.92,8.98], Gold+Silver 1.95, etc.). Provide a reproducible notebook.

P3-E2   σ(fNL) arithmetic wrong at α = 0  
With the published quadratic mapping and the stated F0=1/8.982, the
single-tracer base comes out 2.998, contradicting the text (8.982).  All
following central values are therefore numerically suspect.  
Required fix: recalculate and error-propagate after correcting E1.

P3-E3   Mixing incommensurable anomaly thresholds  
Table I aggregates counts obtained with: (a) absolute S>5 (DESI),
(b) 99th-percentile cuts (LAMOST, SDSS native), (c) fixed top-1 %
(Planck, Gaia, NEOWISE), (d) an IsolationForest raw-score knee
(eROSITA).  The headline “378 280 anomalies” combines detections on
non-comparable scales and is subsequently used in density and
“×141 larger than Liang et al.” arguments.  
Required fix: choose and justify ONE uniform significance definition or
split headline statistics by threshold family and do not cross-compare.

P3-E4   Surveys that fail the declared 5 σ, 50 % recovery gate are still
included in the headline catalogue  
LAMOST (5.8 %), Gaia (5.2 %), eROSITA (1.2 %) all fail the gate yet
113 342 + 500 + 298 objects are counted. Either (i) drop those objects
from the public catalogue and the 378 280 total, or (ii) raise the gate
or justify in writing why the gate is not binding.

P3-E5   Undeclared estimator selection (α)  
The bias-enhancement α estimator and the three angular bins, jack-knife
scheme and target sample were chosen after looking at the data;
no preregistration exists.  
Required fix: pre-specify the estimator or move all α-related claims to a
clearly labelled exploratory section and weaken any statistical
interpretation accordingly.

P3-E6   Numerical mismatch in “≈265 000 catalogue-grade” figure  
DESI 195 829 + SDSS 77 905 + eROSITA 298 + Gaia 500 + NEOWISE 419 =
274 951, not “≈265 000”.  Either a component is missing or the figure is
wrong.  Trace it.

P3-E7   Internal version-history language and file-path artefacts  
The manuscript is full of strings such as  
“companion artifact pipelines/p3 anomaly engine/…/result.json”,
“earlier draft flagged”, “R5 Gemini-M3”, “Round-5”, etc.  
Required fix: remove every development tag, path and draft note.

P3-E8   σ values from different null models compared on the same axis  
Linear error propagation (σ=8.27±2.37) is juxtaposed with the
quadratic “positivity-respecting” envelope without flagging that the
error bars live on different statistical manifolds.  
Required fix: present all σ intervals on the same mathematical footing
or explicitly label them as incomparable.

--------------------------------------------------------------------
MAJOR (significant revision)
--------------------------------------------------------------------

P3-M1  LAMOST contamination still unresolved  
98 % of the original LAMOST anomalies are instrumental blue-excess.
The native retrain removes most but not all: you still retain
2 054 S>5 objects yet the 5 σ completeness is only 5.8 %.  Explain the
residual bias and supply a vetting procedure or exclude them.

P3-M2  SIMBAD “novelty” exaggerated  
The abstract touts 58.8 % SIMBAD-unmatched yet the body admits that
cross-matching against 20 catalogues lowers the genuine-novelty rate to
17.8 % on the top-1000 sample.  The larger figure is repeatedly quoted
without caveat.  
Fix: restrict novelty statements to the 17.8 % figure (or recompute on
the whole sample).

P3-M3  ACT DR6 numbers still appear in tables and prose although the
survey is “quarantined”.  Remove all ACT counts from every aggregate
total and graph or provide a clearly separated appendix table.

P3-M4  Path-C rebuild description (Sec. II D) mixes methodology with
chronology in an unreadable way.  Provide a clean step-by-step pipeline
diagram and move narrative history to an appendix.

P3-M5  50-page length exceeds PRD norms for a methods paper (typ. 15–30 pp).
Prune all version history, file-path listings, and duplicate caveat text.
Target ≤ 30 text pages + ≤ 10 pages appendices.

P3-M6  Equation (2) defines S = (MSE – μval)/σval but later the text
treats “S = 5 corresponds to MSE ≈ 0.143”.  That is true only for the
DESI scale; elsewhere it is false.  Either index S by survey or define
a universal cut in raw MSE.

P3-M7  Injection-recovery test limited to narrow Gaussians until late in
the paper.  Provide continuum-distortion, spectral-break and composite
plants for ALL spectroscopic surveys and summarise in one table.

P3-M8  Unresolved discrepancy: Table I lists NEOWISE 436 anomalies; text
says 419 after pole mask; both numbers are used in later totals.  Fix.

P3-M9  Many duplicate phrases (“unphysical artifact of the local-linear
mapping”, “catalog-calibration domain shift” twice in same sentence).
Reduce.

--------------------------------------------------------------------
MINOR (should be addressed)
--------------------------------------------------------------------

P3-m1  Confusing dual use of “z” (redshift) and “z-score”.  Rename the
statistical quantity throughout.

P3-m2  Footnote symbols (♡ ♠ ♣ ¶) are unreadable in PDF.  Replace by
standard numeric footnotes.

P3-m3  ≥ and ≤ symbols not rendered in a few places (plain‐text mark-up).

P3-m4  Units: reconstruction MSE is dimensionless but sometimes quoted
as “0.0287 Å−1”.  Remove unit.

P3-m5  Equation numbering skips from (4) to (E1) in the appendices.
Re-number consecutively.

P3-m6  “DESI DR1 footprint (∼14 000 deg2)” → 14 000 deg2 is the full
DESI imaging area, not the DR1 spectroscopic footprint (≈9 400 deg2).

P3-m7  “Compute times 19 705 s equals 11 h” – actual conversion 19 705 s
= 5.47 h.  Correct.

P3-m8  Minor arithmetic: 637+9 576=10 213 (text), elsewhere 10 213
written 10 213 % (typo).  Correct.

--------------------------------------------------------------------
NIT (very minor)
--------------------------------------------------------------------

P3-n1  p. 6 “z-scored” should be “standardised”.

P3-n2  “affine-gap” → “affine gap”.

P3-n3  Missing comma in author list line 2.

P3-n4  Fig. 10 axes labels unreadably small.

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS  

The catalogue is potentially valuable, but the current draft contains
several internal mathematical inconsistencies (most seriously the Fisher
coefficients), aggregates incomparable detection thresholds, includes
objects from surveys that fail the authors’ own quality gate, and is
still littered with development artefacts. A thorough clean-up,
re-calculation of all σ(fNL) figures with a consistent formula, and a
clear separation between accepted and exploratory data are required
before the manuscript can be reconsidered.