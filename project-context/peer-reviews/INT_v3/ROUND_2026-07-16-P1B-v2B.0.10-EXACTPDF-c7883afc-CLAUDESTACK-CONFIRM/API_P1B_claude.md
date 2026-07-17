# INT v3 — Independent Referee Report (Claude subagent)

- **Model:** claude-opus-4-8 (subagent, orchestrator-independent leg)
- **Date:** 2026-07-16 (PT)
- **Paper:** P1B — `namaster-proof`: Exact pseudo-$C_\ell$ window inference and content-bound validation for reproducible spin-2 analyses
- **Manuscript version:** v2B.0.10 (software version described: 0.1.7)
- **pdf_sha256:** `c7883afc5050600998b612d7c8a894c7352b5b3770e442befd2b30f78b502673`
- **PDF path:** `arxiv/paper1b_namaster_proof.pdf` (6 pages)
- **Venue:** Journal of Open Research Software (JORS) — profile JORS-SOFTWARE
- **Exactness gate:** PASS (computed SHA-256 == required SHA-256; fail-closed satisfied)

---

## PARSED VERDICT: MAJOR REVISIONS

---

## Referee prompt (as executed)

> You are an expert referee for the Journal of Open Research Software. Review this Software metapaper manuscript under profile JORS-SOFTWARE to the standard of a real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim supported?

---

## (1) VERDICT

**MAJOR REVISIONS**

The manuscript is well-written, honestly scoped, and describes genuinely useful,
well-tested software. It is not acceptable as-is under JORS because a mandatory
element of the JORS metapaper structure — deposition of the software in an
archive with a persistent identifier — is by the authors' own statement not yet
satisfied. That single hard gate, plus a small number of minor items, defines
the revision.

## (2) ISSUES

**[MAJOR] 1. §11 Availability / "Archive" — mandatory persistent identifier is
absent.** JORS requires that the exact described software version be deposited in
an archival repository (e.g. Zenodo, figshare, Software Heritage) that issues a
persistent identifier (DOI), and that this identifier appear in the Software
Location block. The manuscript states plainly: "A persistent archival identifier
is not yet available. This is an explicit submission blocker, not a completed
release claim." A GitHub repository (a code repository, mutable) does not satisfy
the archive requirement. Until v0.1.7 is bound to an immutable archive and the
DOI is recorded in §11, the Software Location section is structurally incomplete
and the paper cannot be accepted. This is the sole reason the verdict is MAJOR
rather than MINOR — everything else is in place. The authors' honesty about the
gap is commendable but does not remove it.

**[MINOR] 2. §7 Quality Control / §11 Validation artifacts — the headline
validation scalar $1.41\times10^{-18}$ is not fully reproducible.** The paper
foregrounds a max-abs-difference of $1.41\times10^{-18}$ between direct window
contraction and the couple–decouple operator, then concedes "the original
workspace tensor was not retained, [so] the scalar is not a self-contained
reproducibility claim or a universal error bound," and that only the committed
$<10^{-10}$-gated equivalence check is reproducible (via
`examples/rebuild_workspace_check.py`). This is disclosed correctly, but a reader
skimming the abstract/QC could take the specific digits as a reproducible result.
Recommend demoting the exact $1.41\times10^{-18}$ figure to "well below the
committed $10^{-10}$ acceptance gate" as the primary claim, or depositing the
exact workspace tensor as a validation artifact so the quoted scalar itself is
reproducible.

**[MINOR] 3. §7 Quality Control — no explicit test-invocation command or coverage
figure.** The QC section states 41 automated tests exist (39 in a standalone
install) and describes their scope well, but gives no exact command to run them
(e.g. the `pytest` invocation after `pip install '.[test]'`) and reports no line/
branch coverage percentage. JORS QC benefits from both. Add the concrete
run-the-tests command and, ideally, a coverage number.

**[MINOR] 4. Title/§2 — package name `namaster-proof` risks confusion with the
official NaMaster project.** The name (and repeated `namaster-proof verify` /
`validate` CLI strings) reads as an official NaMaster subcomponent. The paper
already states NaMaster is not an install dependency; add one explicit sentence
of non-affiliation/independence (this is a downstream verification layer, not a
NaMaster release) to avoid provenance confusion for users and citers.

**[MINOR] 5. Whole manuscript — no figures.** A software metapaper may omit
figures, but a single architecture schematic of the three-module design
(windows / multipoles / receipts and their data flow) or a recovery-vs-injection
plot from the synthetic campaign would materially aid comprehension of the
exact-window path and the fail-closed receipt lifecycle. Optional but
recommended.

**[MINOR] 6. §11 Availability / dual versioning — reconcile the metapaper version
(v2B.0.10) with the software version (0.1.7).** The manuscript is consistent
internally (it describes 0.1.7 throughout), but the front-matter version string
v2B.0.10 alongside a software version of 0.1.7 may confuse readers about which
artifact the DOI will bind. State once, explicitly, that the archived/cited
software artifact is v0.1.7.

**[MINOR] 7. §11 Operating system — macOS listed as untested.** CI covers Linux
(3.10–3.13) and Windows (3.12); macOS is "expected to work … but is not currently
exercised." Given the package is pure Python + NumPy, adding a macOS CI job would
be low-cost and would close the last supported-platform gap; otherwise the
current honest caveat is acceptable.

## (3) Is the central claim supported?

Yes — the central claim, that `namaster-proof` is a focused, tested verification
layer providing exact pseudo-$C_\ell$ window inference (the $4\beta$ rotation
decomposition and full-tensor precontraction of Eqs. 1–5 are standard and
correct) plus fail-closed content-bound receipt validation, is adequately
supported by the described 41-test suite, the worked examples, and the disclosed
synthetic recovery campaign; the only unmet requirement is the mandatory JORS
archival persistent identifier, which is a release/submission gate rather than a
defect in the software or its argument.
