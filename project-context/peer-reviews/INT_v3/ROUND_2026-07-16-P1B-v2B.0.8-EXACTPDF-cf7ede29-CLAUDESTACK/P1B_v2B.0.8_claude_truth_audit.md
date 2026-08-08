# P1B v2B.0.8 — Claude referee leg — truth audit

Binding: paper `arxiv/paper1b_namaster_proof.tex` / package
`packages/namaster-proof/` (version 0.1.6), exact PDF SHA-256
`cf7ede299ee5d6c28209817c7a0ee195000fe8dd77c276e830d8d04f5d2c3195`, 5 pages,
JORS-SOFTWARE profile. Report under audit:
`INT_v3/ROUND_2026-07-16-P1B-v2B.0.8-EXACTPDF-cf7ede29-CLAUDESTACK/API_P1B_claude.md`
(claude-opus-4-8, PARSED VERDICT MAJOR REVISIONS, 2 MAJOR / 4 minor).

Stance: fresh, skeptical, source-cited. No finding dismissed without a citation;
where in doubt, GENUINELY-NEW-REAL. Executable verification (wheel/sdist build +
install + test run) performed locally; nothing was published anywhere.

---

## Executable verification performed

Copied `packages/namaster-proof/` to a scratch dir and built with PEP-517
isolation (python3.12, hatchling fetched by build isolation):

- `pip wheel . --no-deps` → **wheel builds cleanly**:
  `namaster_proof-0.1.6-py3-none-any.whl`, size 11748,
  sha256 `134d05fccf8bfded7d1b82a43302765994429b1f76fbd78f2d3e8e323ed1ec28`.
  Wheel payload = the 5 `src/namaster_proof/*.py` modules + dist-info +
  `entry_points.txt` (the `namaster-proof` console script) + bundled LICENSE.
- `python -m build --sdist` → **sdist builds cleanly**:
  `namaster_proof-0.1.6.tar.gz`; ships README, LICENSE, CITATION.cff,
  pyproject, `src/`, `examples/`, and the full `tests/` tree.
- Fresh venv `pip install wheelout/*.whl pytest` → `import namaster_proof` OK.
- **Full suite run from a complete monorepo checkout: 41 passed in 0.34 s** —
  the paper's 41/41 claim (§7 Quality Control, l.180) is CONFIRMED in-repo.
- **Full suite run against the STANDALONE-installed package (monorepo scripts
  absent): 39 pass, 2 ERROR.** The 2 failures are `tests/test_legacy_equivalence.py`,
  which does `ROOT = Path(__file__).resolve().parents[3]` and
  `importlib`-loads `reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py`
  and `.../multipole_contract.py` — files that live OUTSIDE the package, elsewhere
  in the monorepo. From an archived wheel/sdist those 2 tests raise
  `FileNotFoundError`.

This is the load-bearing result for M2 and is reflected in the dispositions
below.

---

## Dispositions

### [MAJOR] 1 — No archival deposit / persistent identifier → **ALREADY-TRACKED-GATE + DISCLOSED-RE-FLAG**

The persistent archival identifier is an already-tracked external gate. SSOT
`project-context/SSOT/paper-1/status.md` line 1 (CURRENT P1B banner):
"Persistent archive identifier and author-supplied correspondence metadata
remain external/human gates. Readiness HOLDS 56 pending exact v2B.0.8
confirmation and human review." The prior v2B.0.8 truth audit
(`...-JORS-NONANTHROPIC-CONFIRM/P1B_v2B.0.8_truth_audit.md`) maps this to the
DP1B-15 external gate and dispositions the identical Grok REJECT / Gemini MAJOR
finding there. The paper itself discloses it, verbatim, as a blocker
(`arxiv/paper1b_namaster_proof.tex` l.284-287, §Availability→Archive: "A
persistent archival identifier is not yet available. This is an explicit
submission blocker, not a completed release claim."). Not a new executable or
scientific defect; no readiness change. Same finding, third reviewer.

### [MAJOR] 2 — No packaged distribution; code inside a monorepo; test claims unverifiable from an archived artifact → **compound: DISCLOSED-RE-FLAG + GENUINELY-NEW-REAL + PARTIALLY-FALSIFIED**

Split into its three constituent claims:

- **(2a) "install path is a monorepo subdirectory; no PyPI/conda" — DISCLOSED-RE-FLAG.**
  The paper openly states exactly this: §Code repository (l.273-278) gives the
  monorepo tree URL `.../tree/main/packages/namaster-proof` as the install path,
  and makes NO PyPI/conda/`pip install <name>` claim anywhere (grep confirms). No
  overclaim exists to falsify; the referee is describing disclosed content.
  Overlaps the archive gate (1).

- **(2b) "publish a packaged, installable release" — GENUINELY-NEW-REAL (bounded, verified buildable).**
  The package directory is complete and PEP-517-buildable TODAY: `pyproject.toml`
  (hatchling backend, name/version/deps/license/entry-point all present), and both
  wheel and sdist build and install cleanly with no in-repo blocker (see
  verification above). A tagged standalone release → Zenodo deposit (mints the
  DOI that closes gate 1) → optional PyPI publish is therefore a REAL, bounded
  closure, not aspirational. **This finding COLLAPSES INTO gate 1's closure**: the
  single act "cut an immutable versioned release and deposit it" simultaneously
  satisfies the archive/DOI gate and the packaging concern. Minimal honest fix is
  identical to the DP1B-15 closure and is already the tracked human/external gate.

- **(2c) "CI/41-test claims are unverifiable from an installable artifact" — PARTIALLY FALSIFIED (and yields a small genuinely-new item).**
  FALSIFIED for 39/41: those tests run and pass from the pip-installed wheel with
  no monorepo present. TRUE, but for a reason the referee did not identify, for
  2/41: `tests/test_legacy_equivalence.py` structurally reaches
  `parents[3]/reproducibility/p1_namaster_500mc/scripts/*.py`, so it CANNOT pass
  from any archived wheel/sdist even after a PyPI release — publishing the package
  does not, by itself, make all 41 tests independently reproducible. The honest,
  bounded remediation (see GENUINELY-NEW-REAL below) is to guard those 2 tests
  with a graceful skip when the monorepo helpers are absent, so a standalone
  `pip install` + `pytest` yields a clean pass on the 39 self-contained tests
  instead of 2 hard errors. The paper's CI matrix (§Availability l.264-265: Linux
  3.10–3.13, Windows 3.12) runs on a full-repo GitHub checkout, so 41/41 in CI is
  legitimate; the gap is purely archived-artifact reproducibility.

### [MINOR] 3 — Version labeling v2B.0.8 vs Version 0.1.6 → **DISCLOSED-RE-FLAG (already dispositioned)**

Prior truth audit already dispositioned the identical Grok item: "The claimed
v2B.0.8/package-0.1.6 mismatch is false: these are intentionally distinct
manuscript and software-release namespaces." Not a defect. The referee's
constructive add — one explicit crosswalk sentence tying paper-version metadata
to software-version 0.1.6 — is a cheap, honest, optional editorial polish
(SCOPE-VENUE-OPINion); no correctness impact.

### [MINOR] 4 — Availability metadata gaps → **SPLIT: ALREADY-TRACKED-GATE (ORCID) + GENUINELY-NEW-REAL (macOS / system requirements / repo date)**

- **ORCID / correspondence:** ALREADY-TRACKED. §Author Contributions l.242-243:
  "Correspondence metadata remain author-supplied submission metadata and are not
  inferred by the software release process." Maps to the SSOT "author-supplied
  correspondence metadata remain external/human gates." Author/human gate, not a
  code defect.
- **macOS untested/unstated, missing "Additional system requirements", missing
  code-repo date-of-publication:** GENUINELY-NEW-REAL and factually accurate.
  Confirmed: §Availability has paragraphs for Operating system, Programming
  language and dependencies, Code repository, License, Archive, Validation
  artifacts — but NO "Additional system requirements" paragraph, and CI is stated
  Linux+Windows only (l.264-265). These are standard JORS Availability fields;
  adding a one-paragraph system-requirements note (memory/CPU for the N_side=512,
  ℓ_max=1024 workspace) and a macOS status line is a cheap honest completion.

### [MINOR] 5 — codemeta.json absent → **GENUINELY-NEW-REAL (minor, optional, cheap)**

Accurate: only `CITATION.cff` is present/mentioned (confirmed on disk). A
`codemeta.json` (SPDX license id, dependencies, keywords, authors/ORCID) is a
real JORS machine-readable-metadata axis and is a low-cost, honest addition. Not
a blocker (CITATION.cff is JORS-acceptable), but a genuine improvement.

### [MINOR] 6 — Empty "Overview" section / template fit → **DISCLOSED-RE-FLAG / SCOPE-VENUE-OPINION**

Factually accurate: §1 Overview (l.52-55) contains only a `\paragraph{Keywords.}`
line, then §2 Introduction. Gemini's prior-round MINOR raised the same
JORS-heading-structure point and the prior audit dispositioned it as "editorial
improvement, not executable or scientific defect." Real template-fit item,
low-cost editorial, no correctness impact.

---

## GENUINELY-NEW-REAL (minimal honest fixes)

1. **Standalone versioned release + Zenodo DOI (+ optional PyPI).** Bounded and
   VERIFIED buildable (wheel sha `134d05fc…`, sdist clean, installs + imports).
   This single act closes MAJOR-1 (archive/DOI gate DP1B-15) and answers MAJOR-2's
   packaging concern together. Already the tracked human/external gate — no code
   change needed to build; the gate is the deposit/publish action itself.
2. **Guard the 2 monorepo-coupled tests** (`tests/test_legacy_equivalence.py`):
   wrap the `parents[3]/reproducibility/...` loads in a graceful
   `pytest.skip`/`importorskip` when the monorepo helpers are absent, so a
   pip-installed package gives a clean 39-pass run rather than 2 `FileNotFoundError`
   errors. Makes the "41 automated tests" claim honestly reproducible from the
   archived artifact (39 standalone + 2 skipped-with-reason), directly closing the
   real half of MAJOR-2(c). Small, in-repo, no science impact.
3. **Availability-template completion (MINOR-4 real half):** add an "Additional
   system requirements" paragraph, a macOS status line, and a code-repo
   date-of-publication. Cheap, honest, factual.
4. **Add `codemeta.json`** (MINOR-5): SPDX + deps + keywords + author metadata.
   Cheap machine-readable-metadata completion.

Optional editorial (not required, no correctness impact): one version-crosswalk
sentence (MINOR-3); fold a self-contained summary into §1 Overview (MINOR-6).

---

## Verdict summary

- **ALREADY-TRACKED-GATE:** MAJOR-1 (persistent archive / DP1B-15);
  MINOR-4 ORCID/correspondence (author gate). 2 tracked gates re-surfaced.
- **DISCLOSED-RE-FLAG:** MAJOR-1 (also disclosed in-paper); MAJOR-2a
  (monorepo path disclosed, no PyPI overclaim); MINOR-3; MINOR-6.
- **GENUINELY-NEW-REAL:** MAJOR-2b release-is-buildable (collapses into gate-1
  closure); MAJOR-2c test-skip-guard; MINOR-4 macOS/sysreq/repo-date;
  MINOR-5 codemeta.json.
- **PARTIALLY-FALSIFIED:** MAJOR-2c rationale — 39/41 ARE verifiable from the
  installed wheel; only 2 monorepo-coupled tests are not.
- **SCOPE-VENUE-OPINION:** MINOR-6 template-fit; MINOR-3 crosswalk sentence.

No new BLOCKER. No scientific/executable defect in the software's central claim:
exact full-window pseudo-Cℓ inference + SHA-256 content-bound receipts, 41/41 in
a full checkout, machine-precision (1.41×10⁻¹⁸) couple/decouple equivalence,
honestly scoped. The two open MAJORs both reduce to the ONE tracked
archive/release gate (DP1B-15) plus one small honest test-portability fix; the
minors are cheap JORS-template completions. Readiness HOLDS 56 pending the
human/external release+deposit and human review — consistent with the prior
audit. The referee's MAJOR-REVISIONS word is venue-appropriate for an
un-deposited software metapaper but surfaces no new executable defect over the
Grok/Gemini board.
