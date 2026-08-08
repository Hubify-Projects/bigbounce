JORS submission bundle — Paper 1B (namaster-proof software metapaper)
=====================================================================

Journal:   Journal of Open Research Software (JORS)
Portal:    https://account.openresearchsoftware.metajnl.com
Type:      Software Metapaper
Rendering: JORS-template rendering of manuscript v2B.0.16 (2026-07-24 18:20 PT)

Why this bundle exists
----------------------
JORS's own "Submission Preparation Checklist"
(https://openresearchsoftware.metajnl.com/about/submissions#submission-checklist,
fetched 2026-07-24) lists, among the items "All submissions must meet":

  "For Software Metapapers: ... The submission conforms to the article
   template. For LaTex submissions, a PDF should be provided along with the
   original LaTex file(s). Submissions in .docx format are also acceptable."

i.e. template conformance is required AT INITIAL SUBMISSION, and the PDF must
accompany the LaTeX source. This bundle satisfies both.

Contents
--------
  paper1b_namaster_proof_jors.tex   Main LaTeX source (\documentclass{jors})
  jors.cls                          JORS class file, byte-identical to the copy
                                    distributed in JORS_Template.zip via the
                                    "LaTex Template" link on the submissions
                                    page (md5 fa935958e955a7eb9ca010c69c479148)
  paper1b_namaster_proof_jors.pdf   Compiled PDF (8 pages, A4)

There is no .bbl or .bib: the bibliography is carried as an inline
`thebibliography` environment (identical bibitems to the canonical manuscript),
so the source compiles standalone with pdflatex alone — no bibtex pass, no
external .bib, and no citation renumbering relative to the canonical PDF.

Build
-----
  pdflatex paper1b_namaster_proof_jors.tex
  pdflatex paper1b_namaster_proof_jors.tex

Verified 2026-07-24 in an isolated extract: 0 LaTeX errors, 0 undefined
references, 0 overfull hboxes, 8 pages.

Relationship to the canonical manuscript
----------------------------------------
The canonical Paper 1B is ../paper1b_namaster_proof.tex (v2B.0.16). Its
v2B.0.13 bytes are permanently archived under Zenodo DOI
10.5281/zenodo.21481842, and it feeds the project site, the PDF mirrors, and
the arXiv tarball lineage. It is NOT restructured. This directory holds a
SECOND rendering of the same manuscript mapped onto JORS's mandated heading
skeleton. The full section mapping is documented in the header comment of
paper1b_namaster_proof_jors.tex.

Content equivalence was re-verified against the canonical v2B.0.16 PDF after
the 2026-07-24 version-legibility closure (see below): the count of
byte-verbatim carried sentences is unchanged from the v2B.0.15 baseline
(45/45), and every remaining divergence is either a pdftotext heading/page-
number artifact or one of the blocks JORS requires to be split into its
granular Availability fields (Programming language / Dependencies; Software
location Archive + Code repository; License), each reconciled one-to-one. The
single deliberate wording difference is that the canonical says the manuscript
stamp sits "on the title page" while this rendering says it is "carried in
this document's page header" -- correct in each, because the JORS rendering
carries the stamp in its running header rather than a title-page date line.
Zero unqualified "Version 0.1.7" strings remain in either rendering. Every honesty disclosure of the canonical manuscript is preserved
verbatim: the 41-test / 39-run-plus-2-monorepo-coupled-skip contract, the
macOS-untested label, the non-self-contained 1.41e-18 scalar caveat, the
"software-recovery checks ... not measurements, detection significances, or
evidence for a physical birefringence model" framing, the
receipts-are-not-signatures caveat, the not-affiliated-with-NaMaster statement,
and the AI usage disclosure.

Software under review
---------------------
  namaster-proof 0.1.7, MIT License
  (The software release line 0.x.y and the manuscript revision stamp v2B.0.x
   are separate namespaces and are not expected to agree; the manuscript now
   states this explicitly in (2) Availability / Software location.)
  Code:    https://github.com/Hubify-Projects/bigbounce/tree/main/packages/namaster-proof
  Archive: https://doi.org/10.5281/zenodo.21481753 (Zenodo, 21 July 2026)

Remaining author-only steps before submission
---------------------------------------------
  1. Create the JORS account at account.openresearchsoftware.metajnl.com.
  2. Budget the £824.00 Software Metapaper APC, or request a waiver/discount
     in the cover letter at the point of submission.
  3. Provide the names and email addresses of five potential peer reviewers
     in the portal's "Comments for the Editor" field; this is an explicit JORS
     Submission Preparation Checklist requirement (five per the checklist —
     see project-context/SSOT/JORS_SUBMISSION_KIT_P1B_2026-07-24.md section 8).
  4. Upload paper1b_namaster_proof_jors.tex + jors.cls + the PDF, tick the
     Submission Preparation Checklist, and submit.
