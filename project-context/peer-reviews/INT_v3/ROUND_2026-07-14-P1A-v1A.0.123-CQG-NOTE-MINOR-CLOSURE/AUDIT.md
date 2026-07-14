# P1A v1A.0.123 CQG Note reproducibility-minor closure audit

Date: 2026-07-14 PDT

Scope: exact closure of the two truth-audited reproducibility/provenance minors
reported by the v1A.0.122 non-Anthropic confirmation board.  No new derivation,
coefficient, regulator result, phenomenological result, readiness change, SSOT
change, site change, or journal-acceptance claim is made.

## Two-commit provenance sequence

1. Artifact commit `7befce143848b925998a3e6ecc850aa510ab3a94` corrects the active NJL script/JSON to the declared three-row `Lambda=M_Pl` scope and preserves the legacy six-row artifact in Git/review history.
2. This v1A.0.123 manuscript closure pins every reader-facing reproducibility link to that already-existing artifact commit.  This avoids an impossible self-referential commit pin.

## Exact frozen manuscript

- Canonical source: `arxiv/paper1a_ech_nogo.tex`
- Canonical PDF: `arxiv/paper1a_ech_nogo.pdf`
- Closure source: `closure/P1A_v1A.0.123.tex`
- Closure PDF: `closure/P1A_v1A.0.123.pdf`
- Closure bibliography: `closure/P1A_v1A.0.123.bbl`
- Source SHA-256: `e08323215579b843a43d6288643f339442560da45bd3ffd91a762dcfb1702233`
- PDF SHA-256: `4c450a6706b2f4e53faac5ffbc6ec720f21e45c7406aa7186ef830f3fef33f71`
- BBL SHA-256: `df9459aff03776469572c8fdfa784a815e0cba8254f5805bf2906fba6c584737`
- PDF: 7 pages; 149,546 bytes; unencrypted.
- Page 1: `v1A.0.123`, `July 14, 2026`, `1:59 PDT` (verified with pypdf).

## Exact finding closures

1. **P1A-122-CONFIRM-01 — NJL artifact cutoff mismatch: CLOSED.** The deterministic script and JSON now contain exactly the displayed `N_f*N_c=1,3,9` rows at `Lambda=M_Pl`; there are zero above-Planck rows.  The retained ratios and `-3/16` scalar-sign result are unchanged.  Two consecutive generations were byte-identical.  The corrected artifacts are frozen in commit `7befce143848b925998a3e6ecc850aa510ab3a94`.
2. **P1A-122-CONFIRM-02 — mixed mutable/immutable links: CLOSED LOCALLY.** `artifact`, `artifactnamed`, `artifactpinned`, and the explicit commit-tree link all target `7befce143848b925998a3e6ecc850aa510ab3a94`.  The PDF contains zero `blob/main`/`tree/main` annotations.  All three referenced file objects pass `git cat-file` with the expected hashes.

## Derivation-fabrication gate

`NEVER_FABRICATE_DERIVATION.md` records the strict added-line scan.  No active
scientific prose or mathematics was added.  Verdict: **CLEAN**.

## Compile and LaTeX audit

- `pdflatex` is unavailable on this host; Tectonic 0.16.9 was used with retained logs/intermediates, BibTeX, two forced reruns, and a second complete build.
- LaTeX errors: **0**.
- Undefined references/citations/control sequences: **0**.
- Overfull hboxes/vboxes: **0**.
- Raw path-like `texttt` strings: **0**.
- Long `date` overflow candidates: **0**.
- Mid-paragraph ad-hoc table candidates: **0**.
- Six underfull prose boxes are non-blocking; no duplicate rendered table was observed.

## All-page visual proof

All seven pages were rendered at 140 dpi under `proof/render/` and inspected
individually.  The page-1 title/version/date, page-3 reader-facing NJL link,
page-6 Data and Code Availability block/Fierz link, page-7 NJL link/table, all
equations, columns, captions, and references are legible.  No clipping, gutter
crossing, margin loss, overlap, malformed equation, table overflow, title/date
overflow, duplicate table, or bad float placement was found.

**Visual verdict: PASS.**

## URL and path proof

- PDF annotations: 19 unique URI targets, 32 annotations total.
- Mutable `main` targets: **0**.
- Nine annotations target exact artifact commit `7befce143848b925998a3e6ecc850aa510ab3a94` (wrapped links may create more than one annotation).
- Three artifact file paths and hashes pass local commit-object verification.
- Five arXiv links return 200.
- Six DOI routes return 200; four additional DOI routes resolve to the correct AIP/APS publisher and then return 403 bot protection.
- The four new immutable GitHub targets return 404 before push.  They are typed **PRE-PUSH**, not missing local content.  Recheck after the serialized push; remote resolution remains a release gate until then.

## Append-only PDF retention

- Object: `project-context/pdf-archive/objects/sha256/4c/4c450a6706b2f4e53faac5ffbc6ec720f21e45c7406aa7186ef830f3fef33f71.pdf`
- Reference: `project-context/pdf-archive/refs/P1A/P1A__v1A.0.123__2026-07-14T140548-0700-PDT__4c450a6706b2.pdf`
- Manifest: `project-context/pdf-archive/manifests/2026/07/20260714T210548Z-p1a-v1A.0.123-cqg-minor-closure-20260714T140548-0700.json`
- Object, reference, closure PDF, and canonical PDF are byte-identical at SHA-256 `4c450a6706b2f4e53faac5ffbc6ec720f21e45c7406aa7186ef830f3fef33f71`; all report seven pages.

## Deliberate exclusions and honest status

`version.json` was already dirty in another agent lane and its paper entries are
globally stale.  It is excluded to avoid overwriting or staging shared work and
is recorded as later serialized release-integration debt together with site,
SSOT, Convex, and readiness synchronization.

The two v1A.0.122 automated minors are closed locally in v1A.0.123.  Readiness
is unchanged.  Human CQG review/editorial decision, immutable archive/DOI,
external science gates, and post-push HTTP resolution remain open.  No automated
verdict is represented as journal acceptance.
