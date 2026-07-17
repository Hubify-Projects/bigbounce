# INT v3 Referee Report — P1B (namaster-proof)

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-16 (PT)
- **Paper:** P1B — namaster-proof, v2B.0.9
- **pdf_sha256:** e2f3301fe74ba2f64ba41d87ec3648a6e3980e8715562ab27440f80ae448bc68
- **PDF path:** arxiv/paper1b_namaster_proof.pdf (6 pages)
- **Venue:** Journal of Open Research Software (JORS) — profile JORS-SOFTWARE
- **PARSED VERDICT:** MAJOR REVISIONS

---

## Prompt

> You are an expert referee for the Journal of Open Research Software. Review this Software metapaper manuscript under profile JORS-SOFTWARE to the standard of a real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim supported?

---

## Referee response (verbatim)

**(1) VERDICT: MAJOR REVISIONS**

**(2) ISSUES:**

1. **[MAJOR] §11 Availability — Archive (missing persistent identifier / DOI).** The manuscript itself states, under "Archive," that "A persistent archival identifier is not yet available. This is an explicit submission blocker... The submission candidate must bind version 0.1.7 to an immutable archive before journal submission." A deposited archive with a persistent identifier (e.g. Zenodo/figshare DOI), name, version, license, and deposit date is a *mandatory* JORS "Software location — Archive" field, not an optional one. As submitted, a required metapaper field is unmet by the authors' own admission, so the paper cannot be accepted in its current state. Provide the archive DOI bound to the exact released version.

2. **[MAJOR] §7 Quality Control / §5 Exact-Window Inference — headline exactness scalar is not reproducible from the package.** The strongest numerical evidence for the "Exact... window inference" claim in the title is the reported maximum absolute difference of 1.41×10⁻¹⁸ between direct window contraction and the couple–decouple operator for a [4, 20, 4, 1025] workspace. The manuscript correctly cautions that "Because the original workspace tensor was not retained, the scalar is not a self-contained reproducibility claim or a universal error bound." This honesty is commendable, but it means the flagship exactness figure cannot be independently regenerated from the archived package. Either retain and archive the workspace tensor (or a script that reconstructs it deterministically) so the 10⁻¹⁸ result is reproducible, or demote it explicitly to an illustrative provenance record and let the self-contained zero-tolerance synthetic test carry the exactness claim in the text. The self-contained synthetic tests do substantiate exactness; the paper should not lean on a non-reproducible scalar rhetorically.

3. **[MAJOR] §11 Availability — Code repository / installation and standalone release.** The software location given is a subdirectory of a larger monorepo (github.com/Hubify-Projects/bigbounce/tree/main/packages/namaster-proof). No package-index (PyPI/conda) release or one-line install path is stated in the paper, and installation instructions are only referred to indirectly. JORS reuse and availability require a reader to obtain and install the *named* software unambiguously. State the install command(s), confirm the standalone package builds and installs independently of the monorepo (the QC section notes 39/41 tests run standalone, so a standalone install path exists — surface it), and give the exact released version string that matches the archive.

4. **[MINOR] Version labelling consistency.** The manuscript is titled v2B.0.9 while the software described is "Version 0.1.7" (§7, §11). This dual-versioning (metapaper vs. package) is defensible but should be stated once explicitly so a reader is not left reconciling "2B.0.9" against "0.1.7"; ensure the archive DOI, CITATION.cff, codemeta.json, and abstract all cite the single software version being released (0.1.7).

5. **[MINOR] §7/§8 Validation-artifact provenance.** The two "Validation artifacts" are cited only as bare SHA-256 digests behind hyperlinked text ("repository summary artifact", "repository bandpower artifact"). Without a persistent location these digests are unverifiable to an external reader. Bind each artifact to the same archive/DOI so the hashes anchor to retrievable objects.

6. **[MINOR] §11 Operating system — macOS untested.** macOS is listed as "expected to work... but is not currently exercised in continuous integration and is therefore listed as untested." Acceptable and honest, but for a pure-Python + NumPy package a single macOS CI job is cheap; adding it (or explicitly stating why it is deferred) would close the last availability gap.

7. **[MINOR] Reference breadth.** Only four references are cited. The MASTER [1], NaMaster [2], CAMB [3], and HEALPix [4] citations are correct and appropriate, but a software metapaper asserting a reproducibility/provenance contribution would be strengthened by situating the receipt/content-binding module against at least one existing provenance or research-object standard, to substantiate the "reuse potential" argument in §12.

8. **[MINOR] Scope-guard prose (positive note, retain).** The repeated, explicit disclaimers — "not a sky-analysis pipeline, foreground model, or cosmological inference engine" (Abstract), the recovery results being "software-recovery checks under the stated simulation contract, not measurements, detection significances, or evidence for a physical birefringence model" (§8), and the receipt system being "content bindings, not digital signatures" (§10) — are exemplary honest scoping and should be preserved verbatim through revision.

**(3) Central claim supported?** Yes — the central claim that the package provides an exact NaMaster bandpower-window operator evaluation plus fail-closed content-bound JSON receipts is well supported by the described synthetic zero-tolerance equivalence tests and the 41-test suite, and the scope is honestly bounded; the paper is nonetheless not yet acceptable because the mandatory JORS archive/DOI field is, by the authors' own statement, unmet and the flagship 10⁻¹⁸ exactness scalar is not reproducible from the released package.

---

## Summary

- **VERDICT:** MAJOR REVISIONS
- **MAJOR count:** 3
- **MINOR count:** 5
