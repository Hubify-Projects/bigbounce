# CHANGELOG

Per-paper version log for the BigBounce repository. Each entry pins a
paper version (from the in-tex `\newcommand{\paperVersion}` stamp) to
the matching version-stamp commit SHA in the repository git log, with
a short summary of the wave that produced it. Where a paper version
points to HuggingFace datasets (MCMC chain diagnostics, NaMaster
pipeline artifacts, ALP parameter chains), the DOI / dataset URL is
recorded here so the paper's data-availability claim survives future
README rewrites.

The full per-fix narrative for each paper is preserved in the comment
block at the top of the corresponding `.tex` source file.

---

## Paper I(b) — `arxiv/paper1b_mcmc_companion.tex`

### v1B.0.57 (2026-06-10) — EXT2 external-round closure wave

- Commit: `63931207` (`feat(P1B v1B.0.57): EXT2 closure wave — 176,240
  chain-confirmed, planck_bao_sn CORRECTED diagnostics added, root
  CHANGELOG created`).
- Wave: EXT2 truth-audit (`project-context/peer-reviews/EXT2_P1B_TRUTH_AUDIT.md`).
  Highlights: `freeze_diagnostics_CORRECTED.json` sample count
  regenerated from raw chains (176,840 → 176,240);
  `parameter_summary_CORRECTED.json` + units README added to
  `planck_bao_sn_20260312_1954/diagnostics/`; this CHANGELOG created as
  the canonical version→commit pin replacing the unbacked git-tag claim;
  Vincenzi et al. 2025 (arXiv:2501.06664) SN-overlap citation;
  "natural parameters" framing removed at 3 sites.
- HuggingFace datasets (DOI / URL): unchanged from v1B.0.56 (see below).

### v1B.0.56 (2026-06-10) — R29 post-EXT1 internal-round closure wave

- Commit: `6eac1a51e07e01307aee6fafd01fe17900fc2ced`
  (`feat(P1B v1B.0.56): R29 closure wave — export-script off-by-one
   root-caused from chains, artifact warning rewritten`)
- Wave: EXT1 truth-audit (`project-context/peer-reviews/EXT1_P1B_TRUTH_AUDIT.md`)
  + R29 post-EXT1 internal round closure pass. Export-script
  off-by-one column-permutation root-caused against the raw chains;
  the `parameter_summary_CORRECTED.json` companion file and the
  artifact warning paragraph in the Data-Availability section
  document the diagnosis.
- HuggingFace datasets (DOI / URL):
  - MCMC chain diagnostics — pending DOI assignment; live at
    `https://huggingface.co/datasets/Hubify/p1b-mcmc-diagnostics`.
  - NaMaster pipeline artifacts — pending DOI assignment; live at
    `https://huggingface.co/datasets/Hubify/p1b-namaster-artifacts`.
  - ALP parameter chains — pending DOI assignment; live at
    `https://huggingface.co/datasets/Hubify/p1b-alp-chains`.

### v1B.0.55 (2026-06-10) — EXT1 closure wave

- Commit: `d48a423fd13eddc6dc9efd5f6c5b3da3c20a0c14`
  (`feat(P1B v1B.0.55): EXT1 closure wave — verify stamp, fix repro
   paths, page-1 version restored`).

### v1B.0.54 (2026-06-10) — R26conf P1B-clean closeout

- Commit: `7ab04964...` (`feat(P1A+P1B R26conf): P1B CLEAN; P1A audit
  closures → v1A.0.54 / v1B.0.54`).

### v1B.0.53 (R24conf closeout)

- 12 textual closures from the R24conf truth-audit; details inline at
  `arxiv/paper1b_mcmc_companion.tex` v1B.0.53 changelog block.

### v1B.0.50 (2026-06-09) — R22prov closure wave

- Closure wave per `project-context/peer-reviews/R22prov_P1B_TRUTH_AUDIT.md`.

### v1B.0.48 (2026-06-09) — P1B-E1 + P1B-E2 closures

- Closure wave including one new figure; details inline at the
  v1B.0.48 changelog block in `paper1b_mcmc_companion.tex`.

### Older (v1B.0.22 through v1B.0.47)

Full per-version narratives are preserved at the top of
`arxiv/paper1b_mcmc_companion.tex` and the corresponding round
synthesis MDs under `project-context/peer-reviews/`. Git tags
`paper1b-v1B.0.NN` exist for the published round-fire snapshots
through v1B.0.41 and can be cross-referenced via
`git tag -l 'paper1b-*'`.

---

## Paper I(a) — `arxiv/paper1a_ech_nogo.tex`

Per-version narrative preserved at the top of
`arxiv/paper1a_ech_nogo.tex`. The current frozen version stamp lives
in the `\newcommand{\paperVersion}` macro of that file; the matching
commit is the most recent commit touching the file.

---

## Paper II — `research/focused_paper_source_integration/02_full_draft.tex`

Per-version narrative preserved at the top of `02_full_draft.tex`. The
current frozen version stamp lives in the `\newcommand{\paperVersion}`
macro of that file.

---

## Note on git tags

Where a paper-version commit was promoted to a git tag, the tag name
follows the convention `paperNN-vNN.NN.NN` (e.g. `paper1b-v1B.0.41`).
Not every paper version is tagged; for versions without a tag, the
version-stamp commit identified above is the authoritative pointer.
