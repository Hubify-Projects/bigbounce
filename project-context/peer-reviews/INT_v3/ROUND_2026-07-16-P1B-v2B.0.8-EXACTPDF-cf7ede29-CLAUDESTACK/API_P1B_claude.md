# INT v3 Referee Report — P1B (namaster-proof)

- **Model:** claude-opus-4-8 (Claude Code subagent, independent INT leg)
- **Date:** 2026-07-16 (PT)
- **Paper:** P1B — `namaster-proof: Exact pseudo-Cℓ window inference and content-bound validation for reproducible spin-2 analyses` v2B.0.8
- **PDF reviewed:** `arxiv/paper1b_namaster_proof.pdf` (all 5 pages, exact-PDF-bound)
- **pdf_sha256:** `cf7ede299ee5d6c28209817c7a0ee195000fe8dd77c276e830d8d04f5d2c3195`
- **Venue / profile:** Journal of Open Research Software (JORS-SOFTWARE, software metapaper)
- **PARSED VERDICT:** MAJOR REVISIONS

---

## Referee prompt (as executed)

> You are an expert referee for the Journal of Open Research Software. Review this Software metapaper manuscript under profile JORS-SOFTWARE to the standard of a real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim supported?
> JORS reviews software papers on: software quality/reusability, archival deposit, metadata completeness, and the paper's description quality — apply the real JORS criteria.

---

## (1) VERDICT: MAJOR REVISIONS

## (2) ISSUES

**[MAJOR] 1 — No archival deposit / persistent identifier (§11 Availability → "Archive").**
JORS policy requires the software version under review to be deposited in a repository that mints a persistent identifier (e.g. Zenodo/figshare/Software Heritage DOI) before publication; the "Software location — Archive" sub-block (name, persistent identifier, publisher, date) is mandatory in the JORS metapaper template. The paper itself states "A persistent archival identifier is not yet available. This is an explicit submission blocker" and that version 0.1.6 must be bound to an immutable archive before submission. As submitted there is no archived, citable snapshot, so the availability requirement is not met and the reviewed artifact is not a frozen version — this is a foundational JORS blocker, not a copy-edit.

**[MAJOR] 2 — Reusability / installability: no packaged distribution; code lives inside an unrelated monorepo (§11 Code repository, §4 Implementation, §12 Reuse potential).**
The sole stated install path is a subdirectory (`packages/namaster-proof`) of the `Hubify-Projects/bigbounce` cosmology research monorepo. There is no PyPI/conda package, tag, or release referenced, so `pip install` reproducibility and discoverability — both core JORS reusability axes — are unestablished, and a general-purpose reproducibility tool buried in a domain research repo raises real reuse friction. Consequently the quality claims that most support reuse (41 automated tests; CI on Linux 3.10–3.13 and Windows 3.12; machine-precision equivalence) cannot be independently verified from a non-archived, non-packaged monorepo path; JORS reviewers need a stable, installable, archived artifact to confirm them.

**[MINOR] 3 — Version labeling inconsistency (title/§7 Quality Control/§11 Availability).**
The manuscript header labels the paper "v2B.0.8" while the body repeatedly names the software "Version 0.1.6" (Quality Control, Availability, Archive) with no crosswalk. State unambiguously which software version is under review and, ideally, decouple paper-version metadata from software-version metadata so a reviewer/citer is not left guessing which release the tests, CI matrix, and archive should bind to.

**[MINOR] 4 — Availability metadata gaps (§9 Author Contributions, §11 Availability).**
No author ORCID is given; the code repository entry lacks a "date of publication"; the CI/OS matrix covers Linux and Windows only (macOS untested/unstated); and "additional system requirements" (memory/CPU expectations for the N_side=512, ℓ_max=1024 workspace path) are not specified. These are standard JORS Availability fields.

**[MINOR] 5 — Machine-readable metadata completeness (§11 Availability).**
Only `CITATION.cff` is mentioned. JORS favors complete machine-readable metadata; a `codemeta.json` (dependencies, license SPDX, authors/ORCID, keywords) is absent/unmentioned and would strengthen the metadata-completeness axis.

**[MINOR] 6 — Empty "Overview" section / template fit (§1 Overview).**
Section 1 "Overview" contains only a Keywords line; the actual overview content is folded into §2 Introduction. Align to the JORS structure so the Overview conveys a self-contained summary rather than acting as a keyword stub.

### Positives noted (not blocking)
- Statement of Need is clear and the scope is honestly bounded ("not a sky-analysis pipeline, foreground model, or cosmological inference engine").
- The rotation algebra (Eqs. 1–3, uniform birefringence rotation of EE/EB/BE/BB for initially vanishing EB) and the precontracted three-component evaluation (Eqs. 4–5) are standard and internally consistent; the reported 1.41×10⁻¹⁸ max-abs difference vs. couple/decouple on a [4,20,4,1025] workspace is a credible machine-precision equivalence, and the caveat that it is "not a self-contained reproducibility claim or a universal error bound" is commendably honest.
- Internal numeric consistency holds (ℓ_max=1024 ⇒ n_ℓ=1025 = "final exclusive edge ℓ_max+1", matching the [4,20,4,1025] tensor).
- Reuse Potential, Limitations, and AI Usage Disclosure sections are present, thorough, and transparent; MIT license is OSI-approved.

## (3) Is the central claim supported?

Yes — the central claim (a focused, tested verification layer delivering exact full-window pseudo-Cℓ inference and SHA-256 content-bound receipts) is supported by the description and the machine-precision equivalence result, but the software's JORS-required archival availability and packaged reusability are not yet met, so publication is contingent on major revisions rather than immediate acceptance.
