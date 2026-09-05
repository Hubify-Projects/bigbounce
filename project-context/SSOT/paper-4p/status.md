# P4' status — current authoritative section

**Current candidate:** v4P.0.6 · `pipelines/p4prime_chirality_test/paper/main.tex`
**Directive-P readiness:** 95 (unchanged) — row-16 disclosure integrated; Houston sign-off read should use v4P.0.6.

## Row-16 disclosure integrated (v4P.0.5 → v4P.0.6, 2026-09-04)

Added a "Robustness and disclosure" subsection (Sec.~\ref{sec:robustness_disclosure},
end of the Supplementary systematics diagnostics appendix) carrying three
row-16 results at evidential strength, as disclosure/robustness content
(no history narration, per directive Q1):

1. **Pixel-level calibration.** Image-level pixel-parity injection through
   the production equivariant classifier ($N=20{,}000$, 10 seeds) recovers
   $dA/df=+0.0167\pm0.0089$ — 47σ below the naive label-identity slope
   ($+0.434$) and 2.9σ from the mixture-corrected label identity
   ($-0.0093$). Source: `injection_pilot/ROW13_PILOT_2026-09-04.md` (Part A
   at N=20k). Manifest: `reproducibility/manifests/experiments/row13-image-level-injection-pilot.json`.
2. **Full-parent selection behavior.** The 3,200,420-galaxy full-parent
   dipole ($A=0.566\%$, $z=+4.44$, RA 278.6°/Dec +25.3°) is disclosed as a
   confidence-cut/DES-leg systematic — removed by the `primary_hc` cut
   alone ($z=+0.68$) and by dropping the DES leg alone ($z=+0.48$), axis
   shifts 107.5° across selections — reported, not subtracted from the
   primary channel's null. Sources: `full_parent/ROW16I_FULL_PARENT_2026-09-04.md`,
   `full_parent/ROW16IB_AXIS_SHIFT_2026-09-04.md`. Manifests:
   `reproducibility/manifests/experiments/p4p-row16i-full-parent-dipole.json`,
   `reproducibility/manifests/experiments/p4p-row16ib-axis-shift.json`
   (both registered in `reproducibility/manifests/programs/galaxy-chirality.json`).
3. **Structure cross-correlations.** 15 pre-registered chirality×structure
   statistics (environment density, anomaly positions, redshift, CMB
   dipole/quadrupole axes) all null against 1000-realization label-shuffle
   and sky-rotation nulls; data limits stated (QSO-only LSS products, no
   void catalog; Shamir axis unavailable, not fabricated). Source:
   `chirality_structure/ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md`.

No science-conclusion change to the primary channel; readiness stays 95.

- **Version:** v4P.0.6, dated 2026-09-04.
- **Compile:** 4-pass `pdflatex`, 0 undefined refs, 0 overfull hboxes
  >10pt (one pre-existing 5.88pt overfull unchanged), 12 pages (+1 from
  v4P.0.5's 11, the new subsection).
- **PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf` — MD5
  `4e40b0507b924690310e26aae52e26e5`. Mirrored byte-identically to
  `site/public/papers/paper4prime_chirality_test_v4P.0.6.pdf`,
  `public/papers/paper4prime_chirality_test_v4P.0.6.pdf`, and
  `site/out/papers/` (gitignored build output). Three-way md5 verified
  (compile == served == Convex).
- **arXiv tarball:** `project-context/SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.6.tar.gz`,
  standalone-compile smoke tested (extract + 4-pass pdflatex, 0 undefined
  refs, 12 pages).
- **Convex:** `paperVersions:bump` written (slug `paper-4p`, version
  v4P.0.6) and read back verified; `activityFeed:add` written.

## Final-review REVISE executed (v4P.0.4 → v4P.0.5, 2026-09-02)

Final-review found the ApJS abstract exceeded the 250-word single-paragraph
cap (v4P.0.4 abstract measured 311 words). Trimmed to **246 words**
(pdftotext, page-1 abstract block) with **no science change** — every
required quantitative fact preserved verbatim: $N_{\rm support}=887{,}472$
of $890{,}069$ rows (parent 8,474,531); $z_{\rm mom}=+0.635$, one-sided
$p=0.238$; $A_{95}^{\rm obs}\simeq0.98\%$; Neyman $A_{95}^{\rm
CL}\simeq0.75\%$; $\Delta f_{\rm CW}=+0.00145$, two-sided $p=0.66$ on
145,766 DESIVAST-classified galaxies; the black-hole-universe mechanism
papers' qualitative-only alignment claim; the $2$–$20\times$ /
$\sim2$–$33\%$ literature-amplitude comparison; the
not-adopted-for-strengthening observed-to-physical bridge caveat; and the
confirmation of Iye et al. (2021) and Patel & Desmond (2024). No
parenthetical (Author Year) citations remain in the abstract. Convergence
statement unchanged — this is a presentation-only revision.

- **Version:** v4P.0.5, dated 2026-09-02.
- **Compile:** 4-pass `pdflatex`, 0 undefined refs, no new overfull hboxes
  >10pt, 11 pages (unchanged from v4P.0.4).
- **PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf` — MD5
  `f0d874e93cebf95f86e408f780f002e0`, SHA-256
  `b60781c761ea10eb26e3ce1b9ccb06a0a17c05d44588972a9c42f6602991a5fb`.
  Mirrored byte-identically to
  `site/public/papers/paper4prime_chirality_test_v4P.0.5.pdf` and
  `public/papers/paper4prime_chirality_test_v4P.0.5.pdf`.
- **Registry:** `project-context/draft_paper_registry.json` id `P4P` updated
  (version/pages/sha256/md5/served_aliases).
- **arXiv tarball:** rebuilt per `bib-tarball-rebuild`,
  `project-context/SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.5.tar.gz`.
- **Kits:** `project-context/SSOT/PORTAL_KITS_2026-09-02.md` and
  `ENDORSER_OUTREACH_2026-09-02.md` paste-ready abstracts updated to the
  trimmed v4P.0.5 text; "needs trim" note removed.

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

- **Version:** v4P.0.3, dated 2026-09-02.
- **Pages:** 11 (up from 10 in v4P.0.2; target 12–15 per the R2 truth-audit
  closure plan — landed just under the 12–13pp estimate. The added schema
  table, completeness/purity table, expanded monopole disclosure, and
  expanded bootstrap-z/CL paragraphs account for the growth; R17 citation
  style is still deferred, so no further mechanical page growth from it).
- **Compile:** 4-pass `pdflatex`, 0 undefined references/citations, 0
  overfull hboxes >10pt (one 5.9pt residual overfull hbox in the
  bias-hardening table, unchanged from v4P.0.2, under the hygiene
  threshold). One soft `aastex702` "float is stuck (cannot be placed)"
  warning on the Fig. 3 (T-Web bar) float — the float still places cleanly
  by the next page break; not a hard-gate item (0 undef refs / 0 hboxes
  >10pt are the hygiene gates), tried `[tbp]` placement without eliminating
  it, left as a known cosmetic AASTeX two-column float-queue warning.
- **Visual audit:** every page rendered via `pdftoppm -r 60` and inspected.
  Figure 1 (full 8.47M-galaxy chirality asymmetry map; body text at
  §3 now matches its own caption — DP4P-26 fixed), Figure 2
  (observed-label injection–recovery curve), Table 1 (new catalog schema,
  DP4P-42), Table 2 (new completeness/purity vs. threshold, DP4P-43),
  Table 4 (bias-hardening battery with T5 restored as an explicit
  "removed" row, DP4P-27), and Figure 3 (T-Web bar chart, per-class N now
  stated in-text, DP4P-31) all render cleanly.
- **PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf`
  — MD5 `cb7429779c820f03daf125a49b395ec5`,
  SHA-256 `e8b517d22f61ed733dca043ae2b8253eceffd856ffdfc09e65b422c90b3a8200`.
  Mirrored byte-identically to
  `site/public/papers/paper4prime_chirality_test_v4P.0.3.pdf`,
  `public/papers/paper4prime_chirality_test_v4P.0.3.pdf`, and
  `site/out/papers/paper4prime_chirality_test_v4P.0.3.pdf` (v4P.0.1/v4P.0.2
  files kept in place).
- **Registry:** `project-context/draft_paper_registry.json`, id `P4P`
  (version/pages/sha256/md5/served-aliases updated to v4P.0.3;
  `review_paths` extended with the R2 audit directory).
- **Bibliography:** manual `\begin{thebibliography}` in `main.tex` (matching
  the house style of both folded-in sources, neither of which uses
  bibtex/biber); a deduplicated `references.bib` documentation copy is
  co-located at `pipelines/p4prime_chirality_test/paper/references.bib`.
  R17 (non-AASTeX-author-year numeric citation style) was **not** closed
  this wave either — still OPEN, deferred to packaging as low-risk/
  low-value relative to recompile risk; this is now the sole remaining R1
  residue (both R1's page-target shortfall and R17 were carried into R2's
  own item list as DP4P-42/43 (page target — now substantially closed) and
  a residual R17 line item, respectively).

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

## R2 closure (v4P.0.2 → v4P.0.3)

Closes `ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2`
(`project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2/P4P_v4P.0.2_R2_truth_audit.md`,
dispositions in `project-context/peer-reviews/DISPOSITIONS/P4P.md`). 21
canonical items (DP4P-21 through DP4P-24, DP4P-25 through DP4P-41,
DP4P-42/43; 6 MAJOR/15 MINOR), all four closure waves.

**The monopole science decision (DP4P-21, MAJOR)** — the audit's preferred
R2-budget-satisfying decision: the primary $887{,}472$-galaxy channel's own
monopole was never previously stated. Recomputed directly from the
committed strict-primary catalog: $f_{\rm CW}=0.5126562$
($454{,}968/887{,}472$), the opposite sign from the two narrated monopoles
(catalog-wide $0.497353$; HC-with-unsafe $0.496051$). Cause: the 59,515
quarantined `raw_flip_qc_unsafe` rows are 75.2% CCW ($44{,}739$ CCW /
$14{,}776$ CW), so removing them for the release-safety cut flips the HC
monopole's sign. All three values are now stated together in §2.2 with the
quarantine asymmetry disclosed as a previously unstated, checkable property
of the QC flag. This does **not** propagate to the primary null: the
injection-recovery generator draws its baseline CW probability from the
same strict sample/support it injects into (correct by construction), and
the real-space estimator absorbs any constant monopole into its fitted
monopole term (confirmed generatively: binomial nulls at the global $f_{\rm
CW}$ and at $p=0.5$ give statistically identical dipole-amplitude nulls,
$0.39\sigma$ apart) — both facts are now stated in-paper.

**The CL decision (DP4P-22, MAJOR)** — re-run chosen and executed, not
dropped. `research/bh_universe_dipole/a95_upper_limit_2026_09_02.py`
performs the Neyman inversion (5th percentile of `recovered_amp` vs.
injected amplitude, same estimator/support/null as the committed
detection-power script, `N_AXES=2000` matching the committed script — no
precision tradeoff was needed, full grid ran in 77.7s, well inside the
~60-min budget) and finds a genuine 95% CL upper limit
$A_{95}^{\rm CL}\simeq0.75\%$ (bracket $[0.75\%,0.80\%]$), reported in §3
as Eq. 2 alongside the existing detection-power floor
$A_{95}^{\rm obs}=0.98\%$. The paper's prior "genuine 95% CL statement"
(the null's own 95th percentile, $0.669\%$) is now correctly relabelled as
the same no-signal critical value already reported as the rank test
($p=0.238$), not a CL bound on $A_{\rm dip}$ — the audit's finding that
this label was itself wrong is fixed, not just supplemented.

**Wave 1 (science, transcribe-only):** DP4P-23 (withheld per-estimator
bootstrap $z$'s: $+2.21$ real-space, $+0.81$ WLS, $-0.61$ MASTER $\ell=1$,
now printed alongside the monopole's $z=-6.57$, with the block-bootstrap
$z=+2.21$ explicitly distinguished from the primary null's fixed-occupancy
$z_{\rm mom}=+0.635$); DP4P-24 (abstract now carries the g-bridge caveat).

**Wave 2:** DP4P-22, above.

**Wave 3 (venue, ~1 pp):** DP4P-42 (new catalog schema table, Table 1);
DP4P-43 (new completeness/purity-vs-threshold table, Table 2).

**Wave 4 (editorial, all 15 MINORs closed):** DP4P-25 (intro N corrected
890,069→887,472); DP4P-26 (Fig. 1 body sentence no longer contradicts its
own caption); DP4P-27 (T5 restored as an explicit "removed" row with P4's
circular-RA disposition); DP4P-28 (DOI-sharing between [15]/[17] explained
as one Zenodo concept record, versioned vs. concept DOI distinguished);
DP4P-29 ("four rows" → "five rows / four statistic families"); DP4P-30
(catalog-wide monopole now stated with its own $\sigma$/significance,
$-9.47\sigma$, in the same sentence as its value); DP4P-31 (T-Web per-class
$N$ stated: Void 428, Wall 6,673, Filament 408,187, Cluster 397,505, with
the Void bin's power limitation noted); DP4P-32 (keywords converted to UAT
terms with identifiers); DP4P-35 (T5 row-width overfull hbox fixed;
residual 5.9pt hbox and one soft stuck-float warning remain, both
documented above as non-hard-gate); DP4P-36 (Poplawski 2020's preprint
status and arXiv-date/year mismatch stated explicitly in the
bibliography); DP4P-37 (949,584 sample renamed "pre-support-cut HC sample"
to stop colliding with the paper's own 887,472 "primary channel"); DP4P-38
(internal "on-vision" governance framing removed from §1 body); DP4P-39
(internal "post-review" qualifier removed from the nuisance-basis
description; the legitimate exploratory/not-preregistered disclosure a few
lines later is unchanged); DP4P-40 (Data Availability now states the
manuscript's own version + git-tracked source URL and the catalog's
versioned Zenodo DOI as the reproducibility pin); DP4P-41 (title changed
from "...and an Exclusion of the Rotating-Black-Hole-Universe Dipole" to
"...and a Sensitivity Confrontation with the Rotating-Black-Hole-Universe
Prediction", matching the abstract's own caveat that no computed amplitude
exists to exclude).

**All 21 canonical R2 items closed.** New committed artifacts this wave:
`research/bh_universe_dipole/a95_upper_limit_2026_09_02.py` (+ its output
JSON), `reproducibility/manifests/experiments/p4prime-a95-neyman-cl-2026-09-02.json`.
No P4/P5 source repo file was touched.

Git commit `a47ca06104bfb140e4982b346c0440cfb7d04501`. Convex
`paperVersions:bump` id `k578hqea3a00ddg6qf4gr0f0y18dnze3`; `activityFeed:add`
id `j57dptwy56ktbenejeeewkq6r18dnpx3` (first `paperVersions:bump` call used a
malformed `texCommit` string and was superseded by the corrected call above —
recorded here so the earlier id is not mistaken for the authoritative one).

## R3 closure (v4P.0.3 → v4P.0.4) — FINAL, automated review converged

Truth audit: `project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P4P-v4P.0.3-EXACTPDF-e8b517d2-R3VERIFY/P4P_v4P.0.3_R3_truth_audit.md`
(sha256 of reviewed manuscript `e8b517d22f61ed733dca043ae2b8253eceffd856ffdfc09e65b422c90b3a8200`,
verified this session). Dispositions: `project-context/peer-reviews/DISPOSITIONS/P4P.md`.

**R3 verdicts (verdict words diagnostic only, per directive H):** Claude INT
`minor-revisions` (0 MAJOR / 5 MINOR + 1 NIT, 6 items); Grok API `grok-4.3`
`REJECT` (0 BLOCKER / 3 ESSENTIAL / 3 MAJOR / 2 NIT, 8 items); Gemini API
`gemini-3.1-pro-preview` `MINOR REVISIONS` (0 BLOCKER / 3 ESSENTIAL / 1 MAJOR /
1 MINOR, 5 items); Perplexity **ABSENT** (401 insufficient_quota, optional
leg). **0 BLOCKER across the round.** 19 raw findings → 12 canonical after
dedup: 7 GENUINELY-NEW-REAL (1 MAJOR-by-Rule-8.4, 6 MINOR), 4
RE-FLAG-OF-DISCLOSED, 2 FALSIFIED, 3 OPINION/GENRE. Part A independently
re-verified 21/21 R2 closures real (0 overstated); the Neyman inversion was
re-run and byte-reproduced $A_{95}^{\rm CL}=0.7508188\%$. No arithmetic,
transcription, or derivation error found in v4P.0.3.

**Item → edit table (all 7 SUBSTANTIVE items closed, no new computation):**

| ID | Item | Edit in v4P.0.4 |
|---|---|---|
| DP4P-44 | Monopoles quoted only as $f_{\rm CW}-\tfrac12$ (primary +1.2656%) while every other amplitude uses $A_p=2(f-\tfrac12)$; primary is actually $A_p=+2.53\%$ | `main.tex` §2.2 (ll.~295-303): added "$f_{\rm CW}-\tfrac12=+1.2656\%$, equivalently $A_p=2(f_{\rm CW}-\tfrac12)=+2.53\%$ in the amplitude convention of Fig.~1 and Eqs.~1-2" plus the catalog-wide ($A_p=-0.53\%$) and HC-with-unsafe ($A_p=-0.79\%$) equivalents |
| DP4P-45 | Data Availability names a `dr8_id` column; Table 1 and the released parquet (verified with pyarrow) both say `object_id` | `main.tex` l.~1000: `\texttt{dr8\_id}` → `\texttt{object\_id}` |
| DP4P-46 | Table 1 typesets `raw_flip_qc_unsafe` as two rows | `main.tex` Table 1 source: merged into one `\texttt{raw\_flip\_qc\_unsafe}` row |
| DP4P-47 | `a95_upper_limit_2026_09_02.py` docstring claims N_AXES was reduced from 2000 for a wall-time tradeoff; code sets `N_AXES = 2000` (no tradeoff happened) | `research/bh_universe_dipole/a95_upper_limit_2026_09_02.py` docstring: deleted the stale tradeoff paragraph, kept "No new physics; N_AXES = 2000, matching the committed v1.0.265 script." No numbers changed. |
| DP4P-48 (MAJOR, 3-leg convergent) | Abstract calls $A_{95}^{\rm obs}=0.98\%$ a "sensitivity upper limit," omits $A_{95}^{\rm CL}=0.75\%$; the CL-below-floor relationship unremarked | Abstract: "detection-power sensitivity floor $A_{95}^{\rm obs}\simeq0.98\%$ (full-amplitude; the corresponding Neyman $95\%$ CL upper limit on the measured amplitude is $A_{95}^{\rm CL}\simeq0.75\%$, and we confront the model with the more conservative floor)." §3 after Eq. 2: added the full CL-vs-floor remark (realization-independent floor vs. Neyman inversion conditioned on the observation; exact coverage retained; the standard unified/CL$_s$ motivation named) per the CL-vs-floor ruling recorded in the truth audit and DISPOSITIONS/P4P.md |
| DP4P-49 | "DR1 companion" undefined; §2 builds a DR8 catalog | `main.tex` §4 l.~599: defined as "the DESI DR1 spectroscopic TARGETID cross-match of the DR8 chirality catalog, as constructed in \cite{Golden:P5v147} (joined on TARGETID)" |
| DP4P-50 | Table 1 caption "release v1.0.244" vs. ref [15] "v1.0.274 archived release" reads as a mismatch (both strings individually correct — catalog release vs. release-paper version; premise FALSIFIED, ambiguity real) | `main.tex` Table 1 caption: "catalog release v1.0.244, documented in the v1.0.274 archived release paper \cite{Golden:P4v274})"; no renumbering |

RE-FLAG/FALSIFIED/OPINION items (Grok E2/E3/M1/M2/M3, Gemini E3/N1, Grok N1) —
no edits required; source-cited dispositions recorded in
`DISPOSITIONS/P4P.md`. Grok's REJECT rests entirely on this bucket plus
DP4P-48; the audit found no science defect behind it.

**Hygiene (directive G), same bundle:** `\paperVersion` v4P.0.3 → v4P.0.4;
`\paperTimestamp` unchanged (September 2, 2026 — already current); 4-pass
`pdflatex`, 0 undefined refs/citations; one residual overfull hbox
(5.88pt, ll.381-395, below the 10pt hard-gate, pre-existing); `pdftoppm -r 60`
render of all 11 pages spot-checked (abstract, monopole ¶, Eq. 2/CL remark,
Table 1 schema, DR1 companion sentence, references) — all edits render
clean, no new overflow. Pages: 11 (unchanged). md5 `ed6b8f661b407e6845cb5d42c3efd8d2`,
sha256 `fbf6915390b474883fc98f08322093232312b429bb90e501cf1bfdecad0e951a`.
Mirrored byte-identical (md5-matched) to
`pipelines/p4prime_chirality_test/paper/main.pdf`,
`site/public/papers/paper4prime_chirality_test_v4P.0.4.pdf`,
`public/papers/paper4prime_chirality_test_v4P.0.4.pdf`.
`project-context/draft_paper_registry.json` P4P entry bumped (version,
pages, sha256, md5, served_aliases, review_paths).

**arXiv submission tarball (v4P.0.4):** rebuilt clean in `/tmp` per
`/bib-tarball-rebuild` (bibliography is inline `\bibitem`, no `.bbl`/bibtex
step needed) — `main.tex`, `aastex702.cls`, and the 3 referenced figures
(`fig_sky_map.png`, `fig_injection_recovery.png`,
`fig_p5_cw_by_env_bar.png`); smoke-tested by re-extracting to a clean dir
and standalone-recompiling 4 passes: 0 undefined refs, 11 pages. Stored at
`project-context/SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.4.tar.gz`,
sha256 `db10841372689d9531b576a7ddfbc6aea3833b0e9d092b7be3808620b8665548`.

Git commit `d87b69b030d0d8e114027551fc894a8fb8d65d84`. Convex
`paperVersions:bump` id `k576j98mgmh32egg4rme7xe7jh8dmnp0`; `activityFeed:add`
id `j5766j1vgb1b6m45edz0aaqdyh8dnf1p`.

**CONVERGENCE STATEMENT (directive R2):** Rounds stop after v4P.0.4. R3 was
authorized as a verification pass and functioned as one: 21/21 R2 closures
verified real, the Neyman inversion byte-reproduced, and R3 returned no
substantive science finding — zero genuinely-new findings touch a number,
derivation, selection, or the paper's scope. The 7 items closed are
presentation, terminology, provenance-labelling, and script-documentation;
remaining leg verdict words (Grok REJECT, Claude/Gemini minor-revisions) are
genre/venue, not science. Automated review convergence = 0 genuinely-new-real
findings outstanding across the active legs on the current exact PDF, per
directive H-refined. No further review round on P4' is authorized. P4' now
moves to the publication phase under directive P: agent gates complete →
publication readiness **95**; the final 5 reserved for Houston's explicit
per-paper sign-off; venue/submission/endorsement tracked separately and never
subtracted from the score.

## Open gates (as of v4P.0.2 closure — SUPERSEDED, kept for history; see R3 closure above for current state)

- ~~No INT or EXT review board has been run on v4P.0.3 yet~~ — SUPERSEDED:
  R3 (verification pass) ran on v4P.0.3 and returned only presentation/
  genre/venue items (see "R3 closure" section above). Rounds now stop per
  directive R2; v4P.0.4 is the final closed version pending Houston sign-off.
- Site/Convex sync (`papers.ts`, `live-status.ts`, review timeline, Convex
  `paperVersions:bump`) — the version bump itself is done as part of this
  closure (see Convex ids below); the review-timeline entry for this R2
  round and any papers.ts/live-status.ts text sync remain out of scope for
  this closure worker (site code was not touched per the closure mandate).
- `PAPER_LINEAGE` has not been updated by this closure — P4 and P5
  originals were left untouched, as instructed.
- Whether/when P5's standalone 42-pp paper is formally retired (vs. kept as
  an archived companion with its own diagnostics) remains Houston-gated.
- R17 (citation style) remains the sole open R1-era item, still deferred to
  packaging.
- Houston sign-off (readiness 95→100) has not been sought.

## Historical status ledger

- **2026-09-02 (R2 closure, v4P.0.2 → v4P.0.3):** 21/21 canonical R2
  truth-audit items closed across all four closure waves, including both
  R2-budget-satisfying science decisions (monopole disclosure; genuine 95%
  CL upper limit computed via Neyman inversion, $A_{95}^{\rm CL}\simeq
  0.75\%$). See "R2 closure" section for the full item→edit mapping.
- **2026-09-02 (R1 closure, v4P.0.1 → v4P.0.2):** 18/20 canonical R1
  truth-audit items closed (both waves); 2 deferred (page-target shortfall,
  citation-style conversion) with reasons recorded above. See "R1 closure"
  section for the full item→edit mapping.
- **2026-09-02 (draft creation, v4P.0.1):** first entry for P4'.

## Final review 2026-09-02 (orchestrator)
APPROVE at the agent gates; readiness cap 95 (Convex). See `SSOT/FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md`. 100 awaits Houston sign-off.
