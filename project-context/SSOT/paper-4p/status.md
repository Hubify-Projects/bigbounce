# P4' status — current authoritative section

**Current candidate:** v4P.0.2 · `pipelines/p4prime_chirality_test/paper/main.tex`
**Directive-P readiness:** not yet scored (R1 closure just landed; no fresh
review board run yet on v4P.0.2)

## Lineage

P4' folds two already-reviewed sources into one ≤15-page ApJS-style paper,
per `project-context/PORTFOLIO_DECISION_2026-09-02.md` (Track C1 Addendum)
and `project-context/NEXT_SCIENCE_LEDGER.md` item 5:

- **P4** v1.0.274 · `pipelines/p2_chirality/chirality_catalog_paper.tex` —
  the 8,474,531-galaxy DESI Legacy DR8 catalog and its primary real-space
  chirality-dipole null (HC, $N_{\rm support}=887{,}472$;
  $z_{\rm mom}=+0.635$, $p=0.238$; $A_{95}^{\rm obs}\simeq0.98\%$).
- **P5** v0.1.147-2026-08-03 · `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` —
  the DESIVAST void/non-void environment contrast on 145,766 classifier-labelled
  galaxies ($\Delta f_{\rm CW}=+0.00145$, $p=0.66$), folded in as one
  condensed section rather than kept as a standalone 42-pp paper.

P4' adds one new section not present in either source: **"The black-hole-universe
prediction and its exclusion"** (Sec. 5 of `main.tex`), which reads Poplawski's
rotating-black-hole-universe papers (arXiv:1007.0587, 1111.4595, 1410.3881,
1910.10819) and finds they state only a qualitative preferred-axis alignment
tendency, not a computed dipole amplitude. Under the minimal closure needed
to make the claim testable ($A_{\rm pred}\approx\eta$, the alignment
fraction), the catalog's own $A_{95}^{\rm obs}\simeq0.98\%$ sensitivity floor
excludes $\eta>0.98\%$ at $\geq95\%$ coverage — a factor of $2$–$20\times$
below the $\sim7$–$33\%$ amplitudes reported by Longo (2011) and Shamir
(2012, 2020, 2022, 2025), the observational literature the model is invoked
to explain. This confirms the independent reanalyses of Iye, Yagi & Fukumoto
(2021, arXiv:2011.00662) and Patel & Desmond (2024, arXiv:2404.06617). No
bounce claim is made beyond this stated test (Sec. 6, Discussion, is
explicit that this bears on the black-hole-universe model's spin-axis claim
only, not on the separate matter-bounce cosmology this program otherwise
develops).

Computation for the exclusion is in the committed, deterministic script
`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`
(numpy only; no fitting, no randomness — every output is a literal cited
input or a closed-form arithmetic function of inputs), output
`research/bh_universe_dipole/outputs/poplawski_dipole_exclusion_2026_09_02.json`.
Reproducibility manifest:
`reproducibility/manifests/experiments/p4prime-bh-universe-dipole-exclusion.json`.

No number in P4' is re-derived from raw data; every quantitative result is
quoted verbatim (with a section pointer) from the reviewed P4 v1.0.274 and P5
v0.1.147 sources, or is a deterministic output of the exclusion script above.
The catalog pipeline was NOT re-run.

## Current build

- **Version:** v4P.0.2, dated 2026-09-02.
- **Pages:** 10 (target 13–15 per the R1 truth-audit closure plan; landed
  short — see "R1 closure" below for what was and was not restored within
  this wave).
- **Compile:** 4-pass `pdflatex`, 0 undefined references/citations, 0
  overfull hboxes >10pt (one 5.9pt residual overfull hbox in the
  bias-hardening table, under the hygiene threshold), 0 LaTeX warnings in
  the final pass log.
- **Visual audit:** every page rendered via `pdftoppm -r 60` and inspected.
  Figure 1 (full 8.47M-galaxy chirality asymmetry map, honestly recaptioned
  per R3 — no longer mislabelled as the 887,472-galaxy HC sample or as a
  CW-fraction map), Figure 2 (observed-label injection–recovery curve, new,
  plotted from the committed A95 JSON), and Figure 3 (T-Web bar chart,
  regenerated per R16 — "Paper IV" legend replaced with "catalog global") all
  render cleanly.
- **PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf`
  — MD5 `413705f8cf6ce69da4fe6744b3014ea2`,
  SHA-256 `78936e3610b2d9274e2ba19b8567207b7cd1cb99d9368585d6ff3d78ac9d1db1`.
  Mirrored byte-identically to
  `site/public/papers/paper4prime_chirality_test_v4P.0.2.pdf`,
  `public/papers/paper4prime_chirality_test_v4P.0.2.pdf`, and
  `site/out/papers/paper4prime_chirality_test_v4P.0.2.pdf` (v4P.0.1 files
  kept in place).
- **Registry:** `project-context/draft_paper_registry.json`, id `P4P`
  (version/pages/sha256/md5/served-aliases updated to v4P.0.2).
- **Bibliography:** manual `\begin{thebibliography}` in `main.tex` (matching
  the house style of both folded-in sources, neither of which uses
  bibtex/biber); a deduplicated `references.bib` documentation copy is
  co-located at `pipelines/p4prime_chirality_test/paper/references.bib`.
  R17 (non-AASTeX-author-year numeric citation style) was **not** closed
  this wave — deferred as low-risk/low-value relative to recompile risk
  this late in the closure pass; still OPEN in the disposition ledger.

## R1 closure (v4P.0.1 → v4P.0.2)

Closes `ROUND_2026-09-02-P4P-v4P.0.1-EXACTPDF-a9cc2618-R1`
(`project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P4P-v4P.0.1-EXACTPDF-a9cc2618-R1/P4P_v4P.0.1_R1_truth_audit.md`,
dispositions in `project-context/peer-reviews/DISPOSITIONS/P4P.md`). 20
canonical items (R1–R20, 10 MAJOR/10 MINOR).

**Closed (18/20):**
- **R1** (sample-size denominator) — abstract/§5.2/§6/Discussion now use one
  denominator (887,472) throughout and concede Shamir (2022, $N=1.3$M)
  exceeds the primary channel; "largest sample" restricted to the catalog
  release.
- **R2** ("order of magnitude") — replaced everywhere with the Table 1
  range "2–20×" / "2–33%".
- **R3** (Fig. 1 mislabel) — no committed HC-sample-specific generator
  exists in `pipelines/p2_chirality/`, so per the audit's stated fallback,
  Fig. 1 is honestly recaptioned as the full-catalog FSC asymmetry map (not
  regenerated from new data).
- **R4** (κ=0.97 vs. κ=0.40) — released-classifier κ=0.40/69.91% (N=117,205
  GZ1 cross-match) now reported with the full GZ1 confusion matrix (Table),
  alongside the retrain's κ=0.9733 and P4's exact provenance-distinction
  language; CE-included collapse-to-chance and the 26,616-vs-26,626
  training-record conflict restored.
- **R5** (self-containedness) — Route A: restored catalog schema/release
  contract, selection function, completeness (~30%)/purity (~70%),
  released-classifier confusion matrix, training provenance, estimator spec
  (NSIDE=64, HC-RI/FSC/MAGF supports, fixed-occupancy null construction),
  injection–recovery curve (new figure + table from the committed A95
  JSON), joint 4×4 estimator correlation matrix (real-space/WLS/monopole/
  MASTER ℓ=1, computed from the committed covariance JSON), P5's clustering-
  robustness ladder (NSIDE 2/4/8 + 3,750-cluster scheme) and 5-way
  void-definition sensitivity family (VoidFinder/V2-REVOLVER/V2-VIDE +
  2 GALZONE variants), bias-hardening test table (T1–T8), and an appendix of
  supplementary systematics diagnostics (multipole vector, directional
  partition checks, Fisher scale reference).
- **R6** (FSC ℓ=1 dropped; monopole clause truncated) — FSC $\ell=1$
  $z=+6.923$/$p=0.002$ result restored with its non-overturning caveat; the
  "upstream of the classifier... true sky asymmetry or a DESI imaging
  systematic" open-attribution clause restored verbatim.
- **R7** (non-archival refs / macro bug) — [15] now cites the Zenodo DOI
  10.5281/zenodo.21461899 (not a repo path) and the `\paperVersion{}` macro
  bug at the old l.554 (which stamped this paper's own version onto the P4
  citation) is fixed — [15] now reads a literal "v1.0.274". [16] (P5) has no
  minted DOI (confirmed against this file's own history — readiness 74,
  DOI/tag still open), so per the work order it is cited as the archived
  manuscript at its served URL
  (`https://bigbounce.hubify.app/papers/p5_desi_chirality_v0.1.147-2026-08-03.pdf`)
  with that absence stated explicitly. [14] DESIVAST now carries full
  authors/journal/DOI/arXiv (Rincón et al. 2025, ApJ 982, 38).
- **R8** — internal `project-context/PORTFOLIO_DECISION_2026-09-02.md` path
  deleted from the §1 body.
- **R9** (Eq. 1 power-vs-CL conflation) — Eq. 1 now stated explicitly as a
  detection-power threshold, not a CL exclusion; a genuine 95% CL statement
  ($A_{\rm dip}=0.467\%$ vs. the committed null's 95th percentile, 0.669%)
  is computed by the new script `research/bh_universe_dipole/a95_null_cl_2026_09_02.py`
  from the exact committed 10,000-draw null array
  (`pipelines/p2_chirality/apjs_release_v1.0.259_strict/primary_strict_fixed_occupancy_amps_10000.npy`,
  cross-checked to match P4's own quoted null mean/std to 6 s.f.) and stated
  alongside Eq. 1.
- **R10** (Table 1 non-commensurable pooling) — caption now states the
  four label-space families are pooled; text reports the committed script's
  own g-bridge exceedance flip (Shamir 2020/2022 drop below the floor under
  $g=0.398$).
- **R11–R20** (minor items) — all closed: Table 1 no longer implies an
  $N$-scaling column it doesn't have; Assumption 3 corrected
  (`healpy.fit_dipole` fits direction too); Shamir 2025's 20–33% now labelled
  a count ratio, not an asymmetry fraction; Longo's "$>5\sigma$" changed to
  "$\sim5\sigma$" to match the committed script; Software/Facilities/
  Acknowledgements section added (ORCID still absent — Houston has not
  supplied one to any paper in this repo, so none was fabricated); Fig. 3
  legend fixed (R16, regenerated PNG, see below); a one-line multiplicity
  note added across the three headline tests (R18); Fig. 3's
  Filament/Cluster sub-parity offsets captioned as the same R6 residual
  monopole (R19); catalog file format/schema/size stated in Data
  Availability (R20).

**Not closed (2/20):**
- **R5's page target** — Route A restoration is real and substantial (6pp
  → 10pp, essentially every restoration item on the audit's list is present
  in some form) but landed at 10pp against the audit's 13–15pp estimate.
  Further expansion would need more restored material (e.g. a full catalog
  schema table, deeper P5 GALZONE-construction detail) than this closure
  pass had room for; no content was padded to hit a page count.
- **R17** (citation style) — hand-rolled numeric `thebibliography` was not
  converted to AASTeX author-year format; deferred as a stylistic,
  low-risk-to-defer item given recompile risk this late in the pass.

New committed artifacts this wave:
`research/bh_universe_dipole/a95_null_cl_2026_09_02.py` (+ its output JSON),
`pipelines/p4prime_chirality_test/paper/regen_fig_cw_by_env_bar.py`,
`pipelines/p4prime_chirality_test/paper/gen_fig_injection_recovery.py`. None
touches the P4/P5 source repos — all write only into
`pipelines/p4prime_chirality_test/paper/` or `research/bh_universe_dipole/`.

## Open gates (this draft has NOT been through a fresh review board)

- No INT or EXT review board has been run on v4P.0.2 yet — this closure
  addressed the R1 truth-audit's findings on v4P.0.1; a fresh round on
  v4P.0.2 is the natural next step.
- Site/Convex sync (`papers.ts`, `live-status.ts`, review timeline, Convex
  `paperVersions:bump`) has NOT been done — out of scope for this closure
  worker; site code and Convex were intentionally not touched per the
  closure mandate.
- `PAPER_LINEAGE` has not been updated by this closure — P4 and P5
  originals were left untouched, as instructed.
- Whether/when P5's standalone 42-pp paper is formally retired (vs. kept as
  an archived companion with its own diagnostics) remains Houston-gated.
- Houston sign-off (readiness 95→100) has not been sought.

## Historical status ledger

- **2026-09-02 (R1 closure, v4P.0.1 → v4P.0.2):** 18/20 canonical R1
  truth-audit items closed (both waves); 2 deferred (page-target shortfall,
  citation-style conversion) with reasons recorded above. See "R1 closure"
  section for the full item→edit mapping.
- **2026-09-02 (draft creation, v4P.0.1):** first entry for P4'.
