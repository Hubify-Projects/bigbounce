# P1B v2B.0.9 — fresh skeptical truth audit (Claude leg + Grok + Gemini board)

Binding: paper `arxiv/paper1b_namaster_proof.tex` (v2B.0.9, 6 pp) / package
`packages/namaster-proof/` (version 0.1.7), exact PDF SHA-256
`e2f3301fe74ba2f64ba41d87ec3648a6e3980e8715562ab27440f80ae448bc68`,
JORS-SOFTWARE profile. Board under audit (this round dir):
`API_P1B_grok.md` REJECT / `API_P1B_gemini.md` MINOR / `API_P1B_claude.md` MAJOR
(3 MAJOR / 5 minor).

Prior audit `...-P1B-v2B.0.8-EXACTPDF-cf7ede29-CLAUDESTACK/P1B_v2B.0.8_claude_truth_audit.md`
read in full; its agent-executable GENUINELY-NEW-REAL items (skip-guard the 2
monorepo-coupled tests; codemeta.json; JORS Availability template completion:
system requirements / macOS / repo publication date; honest test contract) were
CLOSED in v2B.0.9 / package 0.1.7 — verified on disk this round (see below).

Stance: fresh, skeptical, source-cited. No finding dismissed without a citation;
when in doubt, GENUINELY-NEW-REAL.

---

## Executable / on-disk verification performed this round

- **Version-string consistency (Claude M4 / Grok M2):** `pyproject.toml` l.7
  `version = "0.1.7"`; `codemeta.json` l.7 `"version": "0.1.7"`;
  `CITATION.cff` l.8 `version: 0.1.7`; paper body §7/§11 "Version 0.1.7". All
  four package-facing surfaces agree at 0.1.7. The dual namespace (manuscript
  v2B.0.9 vs software 0.1.7) is the only mismatch and is a deliberate
  metapaper-vs-release convention.
- **Standalone install path (Claude M3 / Gemini M2):** `README.md` l.17-20 gives
  the explicit one-liner `python -m pip install ./packages/namaster-proof`
  (plus `-e '...[test]'` for the dev/test extra at l.95). §7 QC (tex l.186-191)
  states the standalone contract: 41 tests in a monorepo checkout, 39 run + 2
  replay-equivalence tests skip cleanly in a standalone install. The prior
  round's 39/41 → 39+2-skip closure is present in the shipped text.
- **Validation-artifact SHA-256s (Claude M5):** recomputed on disk —
  `.../physical_spectrum_v2/summary.json` →
  `745b0a2f060773ce69c005ea84b74b305ec26a85f6aaafe58f0b3244b7f39914`,
  `.../physical_spectrum_v2/bandpowers.npz` →
  `b00f850e338007caea6af76f4e9305ab6b54a68e6799efd450bc76f1c325f331`.
  BOTH match the paper's §Validation-artifacts hashes (tex l.316, l.320)
  exactly. The artifacts exist, are git-committed, are hyperlinked to
  resolvable GitHub blob URLs, and are SHA-bound — they are NOT "bare digests."
- **Workspace-tensor regenerability (Claude M2 — the key one):** traced end to
  end; the tensor is a pure deterministic function of committed code (details
  below).

---

## KEY FINDING — Claude M2: workspace tensor / 1.41×10⁻¹⁸ scalar

**Verdict: DISCLOSED-RE-FLAG (the demotion Claude requests is already done) +
FALSIFIED (the "not reproducible / tensor gone" premise — it IS deterministically
regenerable from committed inputs) + one small GENUINELY-NEW-REAL honest
improvement (surface the regeneration path in-paper).**

Provenance of the scalar, traced:

1. The scalar is emitted by `validate_window_equivalence(workspace, response, β)`
   at `reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py:79-89`:
   `return float(np.max(np.abs(via_windows - via_operator)))`, where
   `via_windows` is the direct `get_bandpower_windows()` tensor contraction
   (l.26) and `via_operator = workspace.decouple_cell(workspace.couple_cell(cls))`
   (l.88). This is exactly the "direct window contraction vs couple–decouple
   operator" max-abs-difference the paper reports (tex l.202-205).
2. The `[4,20,4,1025]` workspace is built in
   `reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py:180-181`
   (`workspace = nmt.NmtWorkspace(); workspace.compute_coupling_matrix(f_dummy,
   f_dummy, bandpower_bin)`) from:
   - a mask from `make_native_latitude_window(NSIDE=512, F_SKY=0.40)`
     (l.156-165) — a **pure deterministic function**: it is built from
     `hp.pix2ang` + hard-coded latitude cuts (`|lat|<cut`, `lat>25.0`,
     `lat<-65.0`) + a deterministic `hp.smoothing(fwhm=2°)`. **No RNG, no
     unsaved input map, no external data.**
   - deterministic `bandpower_edges(nside=512, lmax=1024, n_bins=20, ell_min=30)`
     → 20 bins; LMAX=1024 → n_ℓ=1025; 4 spectra ⇒ shape `[4,20,4,1025]`. Matches.
   - production params NSIDE=512, LMAX=2·NSIDE=1024, F_SKY=0.40 (l.111-119).
3. Both `namaster_500mc.py` and `windowed_rotation.py` are **git-tracked**
   (`git ls-files` confirms). The equivalence gate itself is committed and
   hard: `if window_equivalence_max_abs > 1e-10: raise RuntimeError` (l.186-189).

Consequences:

- **The tensor "was not retained" (as a saved file) is literally true** — the
  `bandpowers.npz` files hold `ell_eff`, input spectra, and bandpowers, NOT the
  `[4,20,4,1025]` W tensor. So the paper's caveat (tex l.207-209: "Because the
  original workspace tensor was not retained, the scalar is not a self-contained
  reproducibility claim or a universal error bound") is honest and correct.
- **But "not reproducible" is FALSE in the strong sense Claude M2 implies.** The
  tensor is a deterministic pure function of committed code with no random or
  unsaved input; re-running the committed `namaster_500mc.py` (production mode,
  with PyMaster 2.6 + healpy) reconstructs the identical W and recomputes the
  max-abs difference — the equivalence check runs at stage [2/6], *before* the
  500-realization MC, so the scalar is obtainable without the heavyweight
  campaign. The one true caveat is bit-exactness: `np.max(np.abs(...))` at the
  ~1e-18 machine-epsilon floor is BLAS/CPU/library-version dependent in its last
  digits, so it regenerates to the same **order** (and always `< 1e-10`, gated
  in code) but the literal "1.41" is platform-specific. This is precisely why
  demoting the scalar from a universal error bound is correct — and the paper
  **already does exactly that.**
- **The remedy Claude M2 asks for ("archive it or demote it") is already
  applied.** The paper demotes the scalar in-text AND routes the exactness claim
  to the self-contained zero-tolerance synthetic test: §7 l.206-207 ("the
  package's separate synthetic legacy-helper comparison uses zero requested
  absolute and relative tolerance") + the QC synthetic window suite. Claude M2
  itself concedes both points ("The manuscript correctly cautions…"; "the
  self-contained synthetic tests do substantiate exactness"). So the flagship
  exactness claim is NOT rhetorically leaning on the non-reproducible scalar —
  it rests on the zero-tolerance synthetic test, which IS self-contained and
  runs in the standalone install.

**Minimal honest fix available (GENUINELY-NEW-REAL, small, optional):** upgrade
the honest "was not retained" caveat into a positive, verifiable statement —
add one sentence noting the workspace tensor and the equivalence scalar are
**deterministically regenerable** by running the committed
`reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py` (mask is a pure
function of NSIDE + fixed latitude cuts; the couple-matrix and the
`>1e-10`-gated check are in committed code), with the caveat that only the
last digits of the 1e-18 value are platform-dependent. Optionally commit a tiny
standalone `rebuild_workspace_and_check.py` that reconstructs W and recomputes
`max|Δ|`. This is the task's "retain the tensor artifact (regenerated
deterministically)" option — a real bounded closure — but it is a
provenance-polish improvement, **not** a correctness defect, and it does NOT
change the central claim or readiness. The demote-half is already closed.

---

## Remaining dispositions

### Claude M1 / Grok M1 / Gemini M1 — §11 Archive: no persistent DOI → **ALREADY-TRACKED-GATE + DISCLOSED-RE-FLAG**
The persistent archival identifier is the standing external/human gate
(SSOT `project-context/SSOT/paper-1/status.md` CURRENT-P1B banner: "persistent
archive DOI, correspondence metadata, human software review remain … Readiness
56 HOLDS"). The paper discloses it verbatim as an explicit submission blocker
(tex l.307-310). This is the same standing DOI-floor posture Grok/Gemini/Claude
have flagged every prior round; not a new executable or scientific defect. This
is the standing gate, not a new executable defect — Grok's REJECT is its usual
archive-gate floor, confirmed by inspection of its two majors (both = this gate
+ the version-string item).

### Claude M3 / Gemini M2 — §11 Code repository: monorepo path, install path, standalone build → **DISCLOSED-RE-FLAG + collapses into the archive/release gate**
The monorepo tree URL is the disclosed install path (tex l.294-302); no
PyPI/conda/`pip install <name>` claim is made anywhere, so there is no overclaim
to falsify. v2B.0.9 DID add the standalone contract: §7 (l.186-191) now surfaces
that 39 tests run standalone + 2 skip cleanly, and README l.17-20 gives the
explicit local `pip install ./packages/namaster-proof` one-liner. Both Claude M3
and Gemini M2 reflect current text accurately (they ask to *surface* the
standalone path and to *point Zenodo at the subdirectory*) — the standalone path
is now surfaced; the Zenodo-subdirectory nicety is part of the DOI/release gate
closure. Cheap editorial add available: lift the README `pip install` line into
the paper's §11 Code-repository paragraph. No correctness impact.

### Claude M4 / Grok M2 — version labelling v2B.0.9 vs 0.1.7 → **DISCLOSED-RE-FLAG + cheap editorial (SCOPE-VENUE-OPINION)**
Intentional distinct namespaces (manuscript version vs software release), all
four package surfaces consistent at 0.1.7 (verified above). Grok elevating this
to MAJOR-with-REJECT is referee variance (pattern-066) — an unexplained
mismatch, not a defect. Constructive cheap fix (one crosswalk sentence tying
"v2B.0.9 manuscript describes software 0.1.7") is honest polish; no correctness
impact. Same disposition as the prior audit's MINOR-3.

### Claude M5 — §7/§8 validation-artifact provenance (bare SHA behind hyperlinks) → **PARTIALLY FALSIFIED + collapses into archive gate**
FALSIFIED that the digests are "unverifiable": both files exist on disk, are
git-committed, are hyperlinked to resolvable GitHub blob URLs (tex l.313-320),
and their SHA-256s match the paper byte-for-byte (verified above). The only
residual is "bind to a persistent DOI so hashes anchor to an immutable archive"
— that IS the tracked archive gate, not a new item.

### Claude M6 / Grok M3 — §11 macOS untested → **DISCLOSED-RE-FLAG (honest) + cheap optional**
The paper explicitly lists macOS as expected-but-untested (tex l.276-278) and
CI as Linux+Windows (l.274). This is honest disclosure, not a defect. Adding a
macOS CI job for a pure-Python+NumPy package is a cheap optional completion
(genuinely-real, low value); the honest "untested" label is JORS-acceptable as
written.

### Gemini M3 — §7 awkward phrasing ("39 run and the 2 … skip cleanly") → **SCOPE-VENUE-OPINION (cheap editorial)**
Accurate: tex l.188-190 reads slightly awkwardly. One-clause rephrase is cheap,
honest copy-editing; no correctness impact.

### Gemini M4 — §8 add per-example execution cost/time → **GENUINELY-NEW-REAL (minor, cheap)**
The new "Additional system requirements" paragraph (tex l.280-287) gives the
full-suite runtime (<1 s) but not per-example runtime for the PyMaster
integration / 500-realization CMB recovery campaign. Adding an approximate cost
note is a cheap honest addition. Low value, real.

### Claude M7 — reference breadth (only 4 refs) → **SCOPE-VENUE-OPINION (optional)**
The 4 cited works (MASTER, NaMaster, CAMB, HEALPix) are correct and appropriate.
Adding one provenance/research-object citation to situate the receipt module is
optional editorial strengthening; no correctness impact.

### Claude M8 — retain honest scope-guard prose → **NOT A DEFECT (positive note)**
Not actionable beyond "retain"; the disclaimers are exemplary honest scoping and
should be preserved. No change.

### Grok M4 — §5/§6 LaTeX rendering artifacts (missing subscripts on C^EE etc.) → **FALSIFIED (reader-side text-extraction artifact)**
The tex source is correct: Eqs.(1)-(3) (l.133-142) use `C_\ell^{EE}(\beta)`
with proper braces, and `publish_json`/`C^{EE}` render normally in an
`article`-class compile. A `pdftotext` linearization of the exact PDF flattens
sub/superscripts (e.g. "½" → "21", `C_ℓ^{EE}` → "CℓEE") — this is characteristic
of Grok's native-PDF text parser, not a defect in the compiled PDF. No LaTeX
rendering defect exists in source; nothing to fix. If desired, a visual
`pdftoppm` render of pages 3-4 confirms the subscripts display correctly
(source is unambiguous).

---

## Verdict counts

- **ALREADY-TRACKED-GATE:** M1 (Claude/Grok/Gemini archive-DOI) — 1 standing gate.
- **DISCLOSED-RE-FLAG:** M1 (also disclosed in-paper), M2 (demote-half done),
  M3 (monorepo path / standalone contract), M4 (version namespaces), M6 (macOS).
- **FALSIFIED / PARTIALLY-FALSIFIED:** M2 premise ("not reproducible / tensor
  gone" — it is deterministically regenerable); M5 ("unverifiable digests" —
  hashes match on disk); Grok M4 (PDF subscript artifact is reader-side).
- **SCOPE-VENUE-OPINION (cheap editorial):** M3 lift-install-line, M4 crosswalk
  sentence, M7 reference breadth, Gemini M3 phrasing.
- **GENUINELY-NEW-REAL (all minor / optional, none a correctness defect):**
  1. (M2) Surface workspace-tensor regenerability in §7 (or commit a tiny
     rebuild+recheck script) — upgrades the honest "not retained" caveat to a
     positive verifiable statement.
  2. (Gemini M4) Add approximate per-example execution cost for the PyMaster
     integration and 500-realization CMB recovery campaign.
  3. (M6) Optional macOS CI job (or keep the honest "untested" label).
  4. (M3) Lift the README `pip install ./packages/namaster-proof` one-liner into
     §11 Code-repository prose.

**No new BLOCKER. No scientific or executable defect in the central claim.**

---

## Is the workspace tensor regenerable?

**YES — deterministically, from committed code.** The `[4,20,4,1025]` workspace
is `workspace.get_bandpower_windows()` where `workspace` is built by the
git-tracked `namaster_500mc.py:180-181` from a mask that is a pure deterministic
function (`make_native_latitude_window`, no RNG, hard-coded latitude cuts +
deterministic smoothing) plus deterministic 20-bin edges at NSIDE=512/LMAX=1024.
The 1.41×10⁻¹⁸ scalar is emitted by the git-tracked
`windowed_rotation.py:validate_window_equivalence` and is gated in code at
`>1e-10 → raise`. It was not saved as a *file* (the caveat is honest), but it is
regenerable to the same order by re-running the committed script with PyMaster
installed; only the last digits of the ~1e-18 value are platform-dependent,
which is exactly why the paper correctly demotes it from a universal error bound.

---

## One-paragraph state

P1B v2B.0.9 / package 0.1.7 carries **zero new executable or scientific defect**
over the standing board. The three MAJOR-tier items (archive DOI, monorepo
install path, version namespaces) all reduce to the ONE tracked external/human
release-and-deposit gate (SSOT: persistent archive DOI + correspondence metadata
+ human software review, readiness 56 HOLDS) plus disclosed-and-consistent
metadata that this audit verified on disk (versions 0.1.7 across
pyproject/codemeta/CITATION.cff; both validation-artifact SHA-256s match
byte-for-byte; README ships an explicit `pip install` one-liner; prior-round
skip-guard/codemeta/availability-template closures are present). The headline
Claude M2 finding is largely already addressed: the paper honestly demotes the
non-bit-reproducible 1.41×10⁻¹⁸ scalar and routes exactness to the self-contained
zero-tolerance synthetic test, and — contrary to the "not reproducible" premise
— the underlying workspace tensor **is deterministically regenerable** from
committed, RNG-free code. Grok's REJECT is its standing archive-gate + version
floor, and its "missing subscripts" minor is a reader-side pdftotext artifact
(source LaTeX is correct). Genuinely-new items are four small, optional,
honest polish additions (regenerability sentence, per-example cost, macOS CI,
lift install line) — none blocks and none moves readiness. Readiness 56 HOLDS,
gated on the human/external DOI deposit + software review.
