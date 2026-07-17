# P1B v2B.0.10 — fresh skeptical truth audit (Claude leg + Grok + Gemini board)

Binding: paper `arxiv/paper1b_namaster_proof.tex` (v2B.0.10, 6 pp) / package
`packages/namaster-proof/` (software version 0.1.7), exact PDF SHA-256
`c7883afc5050600998b612d7c8a894c7352b5b3770e442befd2b30f78b502673`
(recomputed on disk this round — **exactness gate PASS**), JORS-SOFTWARE profile.
Board under audit (this round dir):
`API_P1B_grok.md` **REJECT** (2 MAJOR / 2 minor) /
`API_P1B_gemini.md` **MAJOR REVISIONS** (2 MAJOR / 3 minor — flipped up from v2B.0.9 MINOR) /
`API_P1B_claude.md` **MAJOR REVISIONS** (EXACTLY 1 MAJOR / 6 minor).

Prior audit `...-P1B-v2B.0.9-EXACTPDF-e2f3301f-CLAUDESTACK-CONFIRM/P1B_v2B.0.9_truth_audit.md`
read in full. Its four optional GENUINELY-NEW-REAL polish items were CLOSED in
v2B.0.10 — **verified on disk this round** (see below).

Stance: fresh, skeptical, source-cited. No finding dismissed without a citation;
when in doubt, GENUINELY-NEW-REAL.

---

## Executable / on-disk verification performed this round

- **Exact-PDF binding:** `shasum -a 256 arxiv/paper1b_namaster_proof.pdf` =
  `c7883afc5050600998b612d7c8a894c7352b5b3770e442befd2b30f78b502673` == required.
  Fail-closed satisfied; all three legs bound the same artifact + commit
  `8ebefbfd3656141304c58a1207e00461c89b43d1`.
- **v2B.0.9 audit's 4 items — all CLOSED in v2B.0.10 (verified):**
  1. *Workspace-tensor regenerability sentence* — PRESENT: tex l.218–224 now
     states the `[4,20,4,1025]` tensor is "deterministically regenerable from
     committed, RNG-free code" and points to `examples/rebuild_workspace_check.py`.
  2. *Rebuild-and-recheck script* — EXISTS on disk:
     `packages/namaster-proof/examples/rebuild_workspace_check.py` (5,944 B).
  3. *Per-example / campaign wall-times* — PRESENT: new "Additional system
     requirements" paragraph tex l.295–307 gives PyMaster example (few s) and
     the 500-realization campaign (~`7×10²` s / 8 workers).
  4. *pip-install one-liner lifted into §11 Code-repository prose* — PRESENT:
     tex l.319–321 (`python -m pip install ./packages/namaster-proof`).
  macOS remains honestly "listed as untested" (tex l.291–293) — the audit's
  allowed no-CI-change option.
- **Software version 0.1.7:** `pyproject.toml` l.7 `version = "0.1.7"`; paper
  §7 l.194 and §11 l.310 "Version 0.1.7". Manuscript-vs-software dual namespace
  (v2B.0.10 vs 0.1.7) is the same deliberate metapaper/release convention as
  every prior round.
- **Validation-artifact SHA-256s** (tex l.339, l.343) — unchanged from v2B.0.9;
  both matched byte-for-byte last round; artifacts still git-committed and
  hyperlinked to resolvable GitHub blob URLs. No regression.

---

## Per-finding adjudication

### THE GATE (all three legs converge here)
**Claude MAJOR-1 / Grok MAJOR-1 / Gemini MAJOR-1 — §11 Archive: no persistent DOI**
→ **ALREADY-TRACKED-GATE + DISCLOSED-RE-FLAG.**
The paper discloses it verbatim (tex l.330–333: "A persistent archival identifier
is not yet available. This is an explicit submission blocker… must bind version
0.1.7 to an immutable archive before journal submission."). This is the standing
Houston/external gate — SSOT `project-context/SSOT/paper-1/status.md` l.2:
"Readiness cap 56 HOLDS (DOI/correspondence/human gates)." Not a new executable
or scientific defect. Claude explicitly calls it "the sole reason the verdict is
MAJOR rather than MINOR — everything else is in place." Grok's REJECT is its
standing archive-gate floor.

### Grok MAJOR-2 / Claude minor-6 — version v2B.0.10 vs 0.1.7 "no reconciliation/changelog"
→ **DISCLOSED-RE-FLAG + SCOPE-VENUE-OPINION (cheap editorial), same as prior round.**
Deliberate distinct namespaces (manuscript version vs software release). All
package surfaces consistent at 0.1.7 (verified prior round: pyproject/codemeta/
CITATION.cff). The paper already ties the archived artifact to the software
version — tex l.333 "must bind **version 0.1.7** to an immutable archive."
Grok elevating this to MAJOR-with-REJECT is referee variance (pattern-066), not
a defect. A one-clause crosswalk sentence ("this v2B.0.10 metapaper describes
software release 0.1.7") is honest polish; no correctness impact.

### Gemini MAJOR-2 — "future placeholder dates (July 16, 2026 / 2026-07-16) must be corrected"
→ **FALSIFIED (reviewer training-cutoff date confusion).**
Today is 2026-07-16; the `\date{July 16, 2026}` (tex l.46) and repo-publication
date `2026-07-16` (tex l.324) are the **actual, current** release date, not
placeholders. Gemini's model treats 2026-07-16 as future because it postdates
its training horizon. No defect exists. **This falsified item is what drove
Gemini's MINOR→MAJOR flip** (it counted a phantom second MAJOR alongside the
standing DOI gate) — so the flip reflects zero new real content.

### Gemini minor-3 — §9 correspondence-metadata meta-sentence → replace with contact email
→ **ALREADY-TRACKED-GATE (correspondence metadata) + cheap editorial.**
tex l.266–267 carries the meta-sentence "Correspondence metadata remain
author-supplied submission metadata and are not inferred by the software release
process." "Correspondence metadata" is an explicitly tracked component of the
same standing external gate — SSOT l.2/l.4: "(DOI/**correspondence**/human
gates)" / "persistent archive DOI, correspondence metadata, human software review
remain." Collapses into that gate. The observation that the meta-sentence reads
awkwardly and should be removed/replaced with standard corresponding-author
contact is a fair cheap editorial nit, but it is the tracked correspondence item,
not new real content.

### Claude minor-2 — §7 headline scalar 1.41×10⁻¹⁸ "not fully reproducible"
→ **DISCLOSED-RE-FLAG (and the requested remedy is now IN the paper).**
This is the prior-round Claude M2. v2B.0.10 closed exactly the demote/regenerate
ask: tex l.216–224 keeps the honest "was not retained… not a self-contained
reproducibility claim or a universal error bound" caveat AND adds the positive
regenerability statement + `rebuild_workspace_check.py`. Claude's own text
concedes the disclosure is "correct." The underlying "not reproducible" premise
was FALSIFIED last round (deterministically regenerable from committed RNG-free
code) and remains so. Fully dispositioned.

### Claude minor-7 / (Grok/Gemini none) — §11 macOS untested
→ **DISCLOSED-RE-FLAG (honest) + optional.**
tex l.291–293 lists macOS as expected-but-untested; CI = Linux 3.10–3.13 +
Windows 3.12. Honest disclosure, JORS-acceptable as written; a macOS CI job is a
cheap optional completion, not a defect. Same disposition as prior M6.

### Claude minor-5 — whole manuscript has no figures
→ **SCOPE-VENUE-OPINION (optional).**
Claude itself: "A software metapaper may omit figures… Optional but recommended."
JORS permits figureless software metapapers. An architecture schematic would aid
comprehension but is not required and is not a defect.

### Gemini minor-4 — §8 inline code snippets → formatted standalone code block
→ **SCOPE-VENUE-OPINION (cheap presentation).**
tex l.233–236 uses inline `\texttt{}`. Reformatting to a display block is pure
typesetting preference; no correctness or reproducibility impact.

### Gemini minor-5 — §5 "explicitly define ordering [EE,EB,BE,BB] for W_{bℓ}^{ij}"
→ **PARTIALLY FALSIFIED + cheap editorial.**
The ordering IS already stated: §3 l.94–95 "NaMaster exposes a bandpower-window
tensor with spectrum ordering `[EE,EB,BE,BB]`," and §5 l.151–152 defines
`W_{bℓ}^{ij}` mapping input spectrum j to output spectrum i. Repeating the
explicit `[EE,EB,BE,BB]` label at Eq. (4)/(5) is a cheap clarity add, not a
missing definition.

### Grok minor — abstract "not a sky-analysis pipeline" vs §8 end-to-end recovery = over-claiming
→ **DISCLOSED-RE-FLAG (FALSIFIED premise).**
§8 already forecloses the over-claim it worries about — tex l.251–253: "These are
software-recovery checks under the stated simulation contract, **not measurements,
detection significances, or evidence for a physical birefringence model**."
Abstract l.61–63 and §12 Limitations reinforce the scope. No over-claim survives.

### Grok minor — §6 atomic replacement "two files not one transaction… no concrete mitigation"
→ **FALSIFIED (mitigation is in the text).**
tex l.185–187: coordinated replacement of both files "requires an external
receipt anchor or trusted expected metadata to detect" — and Limitations l.279–281
repeats: "not… protection against coordinated replacement without an external
anchor." The concrete mitigation (external receipt anchor / trusted expected
metadata) is stated exactly where Grok says it is absent.

### Claude minor-3 — §7 QC: no explicit test-invocation command or coverage figure
→ **GENUINELY-NEW-REAL (minor; in-paper, not gated on the human/DOI floor).**
§7 (tex l.194–203) describes 41 tests but gives no `pytest` run command and no
coverage number. The only test-related invocation in the paper is the
`-e '.[test]'` install-extra lifted into §11 (l.321) — that installs the extra,
it does not tell a referee how to *run* the suite. Adding the concrete
`pip install '.[test]' && pytest` line to §7 is a real, cheap QC-completeness
improvement (the coverage-percentage half is softer / SCOPE-VENUE-OPINion, but
the run-command core is a legitimate new actionable). Not previously flagged.

### Claude minor-4 — title/§2 `namaster-proof` name may read as an official NaMaster component
→ **GENUINELY-NEW-REAL (minor; in-paper presentation/provenance).**
The paper states NaMaster is not an install dependency (tex l.128) but carries no
explicit non-affiliation/independence sentence; grep for
`affiliat|independent of|not.*official|downstream verification` = NONE. Given the
package name and the `namaster-proof verify` / `validate` CLI strings, one
sentence clarifying this is an independent downstream verification layer (not an
official NaMaster release or subcomponent) is a real, cheap, honest provenance
add. Not previously flagged.

---

## Verdict counts (this board)

| Disposition | Findings |
|---|---|
| **ALREADY-TRACKED-GATE** | Claude M1 / Grok M1 / Gemini M1 (archive DOI); Gemini m3 (correspondence metadata) — all one standing external/human gate |
| **DISCLOSED-RE-FLAG** | Grok M2 & Claude m6 (version namespace); Claude m2 (scalar — remedy now in paper); Claude m7 (macOS); Grok m1 (scope over-claim) |
| **SCOPE-VENUE-OPINION** | Claude m5 (no figures); Gemini m4 (code-block formatting); version-crosswalk / coverage-% halves |
| **FALSIFIED / PARTIALLY-FALSIFIED** | Gemini M2 (future-date confusion — drove the flip); Grok m2 (atomic-replacement mitigation IS in text); Gemini m5 (index ordering already stated) |
| **GENUINELY-NEW-REAL (minor, in-paper, non-blocking)** | **(1)** Claude m3 — add explicit `pytest` test-run command (+ optional coverage) to §7 QC. **(2)** Claude m4 — add one non-affiliation/independence sentence re: the official NaMaster project. |

**Zero new BLOCKER. Zero scientific or executable defect in the central claim.**
Central claim (exact windowed spin-2 rotation inference + fail-closed content-bound
receipts) is supported by all three legs.

---

## GENUINELY-NEW-REAL list (survivors beyond the tracked gate)

Two small, cheap, **in-paper** editorial/QC items — closable in a v2B.0.11 text
bump WITHOUT the human/DOI gate:

1. **§7 QC test-invocation command.** Add the concrete run line, e.g.
   `python -m pip install '.[test]' && pytest` (optionally a coverage number).
   *Minimal fix: one sentence in §7.*
2. **Non-affiliation sentence.** State once that `namaster-proof` is an
   independent downstream verification layer, not an official NaMaster release or
   subcomponent (NaMaster is not an install dependency).
   *Minimal fix: one sentence in §2 or §4.*

Both are presentation/QC-tier completeness, not correctness defects; neither
touches the science, the numbers, or readiness. They do NOT require the archive
DOI, correspondence metadata, or human review — they are author-closable now.

---

## Convergence statement

The P1B in-paper/in-package **science** iteration is exhausted: across the exact
v2B.0.10 board no finding survives as a scientific or executable defect. Every
MAJOR on the board reduces to the single tracked external/human gate — the
immutable archive DOI (with correspondence metadata + human software review) —
which the paper discloses verbatim as an explicit submission blocker. Grok's
REJECT is its standing archive-gate floor; Gemini's MINOR→MAJOR flip is driven by
the DOI gate plus a **falsified** "future date" artifact (2026-07-16 is the real,
current release date, not a placeholder), i.e. zero new real content; Claude's
lone MAJOR is the DOI gate by its own statement.

Two GENUINELY-NEW-REAL items survive, but both are **minor in-paper editorial/QC
completeness** (a §7 test-run command; a non-affiliation sentence) — author-
closable in a v2B.0.11 text bump, independent of the human gate. They do not
block, do not touch the science, and do not move readiness.

**Net:** the remaining pre-submission actions are (a) an optional cheap v2B.0.11
that closes the two minor editorial items above, and (b) the Houston-gated
immutable archive (Zenodo DOI or equivalent) + correspondence metadata + human
software review — the standing gate that has held readiness at cap 56 across
every round. No prompt-gaming, no watered-down claims, integrity rules intact.
Readiness cap 56 HOLDS.
