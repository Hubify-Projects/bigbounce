# INT leg — Claude (Anthropic subscription, Claude Code subagent)
- model: claude-opus-4-8 (Opus-tier subagent)
- date: 2026-07-16 (PT)
- paper: P5 v0.1.140-2026-07-16
- pdf_sha256: 287c6494a07a0c394517adc62d80b9c5cf53950a304221494ac4d46ddab38773
- venue: The Astronomical Journal (AJ-OBSERVATIONAL, Observational research article)
- PARSED VERDICT: MAJOR REVISIONS

---

## Referee report — The Astronomical Journal (AJ-OBSERVATIONAL)

Manuscript: "A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1" (H. Golden, single author, Independent Researcher).

I reviewed this as a fresh referee with no prior program history, judging only the rendered 41 pages.

### (1) VERDICT: MAJOR REVISIONS

### (2) ISSUES

**[MAJOR] 1 — Foundational dependence on an unpublished, un-refereed companion catalog (Paper IV).**
The entire analysis consumes the per-galaxy `class_eq` CW/CCW labels and the catalog-wide monopole from "Paper IV" ([3]), which is explicitly a "companion manuscript in preparation" with "no arXiv identifier or Zenodo DOI ... asserted" (§XIII, Appendix A, §Public availability p.36). The paper's central datum — the classifier labels — cannot be independently assessed by a referee because the classifier's training set, validation, and label provenance live in an unpublished document. Appendix A reproduces the *methodology* but not an independently verifiable *validation*. Section XIII itself concedes "P5 must be re-verified against its independently reviewable final label, weight, and provenance release before submission." A real AJ submission cannot be accepted while its load-bearing data product is neither public nor refereed. The most concrete required revision is that Paper IV (or an equivalent independently reviewable label+weight release with a DOI) must be public and citable before this manuscript can stand on its own.

**[MAJOR] 2 — Data, code, and DOI are not actually released; provenance is incomplete.**
Appendix C states plainly: "No immutable public v0.1.140-2026-07-16 tag or Zenodo DOI is claimed to exist yet; both are explicit pre-submission release tasks," artifact links "A37–A40 will resolve after the release-candidate commit is pushed," the historical DESIVAST-join parquet "is not present in the current release tree; byte-identical historical provenance for that intermediate is therefore not claimed," and the May sidecar raw-hash does not match (§Cluster-bootstrap provenance, p.38). AJ requires a working Data/Software availability statement at review time. As submitted, a referee cannot fetch the primary artifacts, and at least one intermediate cannot be reproduced byte-for-byte. This must be resolved (public repo + DOI + resolvable artifact links + reconciled hashes) before acceptance.

**[MAJOR] 3 — The measured quantity is an attenuated classifier proxy with, by the authors' own statement, no physical or cosmological reach.**
The abstract and §XIII, §Classifier-label scope (p.35) establish the classifier's 69.91% binary accuracy (κ=0.40) implies an attenuation factor of ≈0.3982, so "a classifier-label contrast cannot be read directly as physical handedness." The result is therefore "a catalog-specific non-detection for classifier labels, not a physical-handedness, real-space, or cosmological constraint." This is honest, but it also means the scientific reach of the null is very limited: it constrains neither environment-dependent physical chirality (a genuine signal would be suppressed by ~2.5×, uncorrected here) nor any bounce/inflation cosmology (§XII.B, §XIII). The manuscript needs to make a sharper, up-front case for why a null on a heavily attenuated, catalog-specific proxy meets the AJ significance/impact bar; at present the contribution reads as an internal systematics audit more than a self-standing scientific result.

**[MAJOR] 4 — Post-hoc, non-preregistered focal estimand chosen after inspecting the data, embedded in a very large analysis tree.**
Section V.B and Table IV are explicit that "the analysis was not preregistered, and the focal reporting hierarchy was changed after review from an author-constructed any-hole estimator to the released GALZONE-parent estimate ... This change is post-hoc." Table IV enumerates 23 paths; the focal 13-column (vs 78-column) model was likewise "declared after review and inspection of the data." The paper defends this with Bonferroni/whole-tree/empirical-max-stat corrections and notes every path is null, which does mitigate the forking-paths risk *for a null conclusion*. Nonetheless, a post-hoc-selected focal estimand and model, chosen after seeing the data, is a genuine weakness that the paper should either (a) frame consistently as purely exploratory throughout (removing any language that implies a confirmatory constraint), or (b) support with a preregistered replication on an independent sample. The manuscript should not present the +0.00145442 contrast with confirmatory-grade precision while simultaneously disclaiming preregistration.

**[MAJOR] 5 — The null rests on a monopole-leakage interpretation of several genuinely large raw deviations; this interpretation should be stress-tested, not asserted repeatedly.**
Multiple raw statistics are strongly non-zero: cluster class −4.7σ (Table VII), the sky no-coverage region −5.00σ / −5.28σ (§VIII.G, §VI.B), bright-program −5.28σ (Table XXI), match-radius rows −5.07/−5.22σ (Table XXI). The paper attributes all of them to the Paper IV catalog-wide classifier monopole (Δf = −0.0026) leaking into subsamples ∝√N, and shows |σ_vs monopole| < 1.15 after monopole subtraction. This is plausible and is partially supported by the independent re-measurement of a spatially uniform monopole (f_CW = 0.49719, §VIII.G). But the defense is somewhat circular — it presumes the Paper IV monopole is a pure classifier systematic rather than partly astrophysical — and it recurs a dozen times without a single decisive test that could *falsify* the leakage hypothesis (e.g., an injection–recovery mock, which §T-Web class p.13 explicitly declines to run: "We do not run this mock here"). At least one such end-to-end selection-function/injection test on the focal contrast (not only on the secondary T-Web sign-flip) would materially strengthen the paper.

**[MINOR] 6 — T-Web void bin (n=428) vs DESIVAST void (n≈57k) discrepancy and the +8–18 pp void-fraction mismatch.**
The two "void" definitions disagree by ~130× in count and by +8–18 pp in void fraction (§IX.C, §VIII.A, Table XII/XV). The paper handles this by designating T-Web "secondary/diagnostic" and DESIVAST "focal," and attributes the T-Web deficit to a survey-shell selection artifact. This is defensible but the reader is left unsure whether the focal/secondary split was itself informed by which definition gave the cleaner statistic. A brief, explicit statement of why DESIVAST is the a priori-preferable void definition (independent of the results it produced) would help.

**[MINOR] 7 — Length, density, and redundancy.**
41 pages, 25 tables, 9 figures, and 46 lettered artifacts for a null result is far beyond what the science requires. The monopole-leakage explanation, the "exploratory / post-hoc / not preregistered / secondary / sensitivity" disclaimers, and the "not pooled into a joint constraint" caveat are each repeated many times (abstract, §I, §V.B, §VI, §XII, §XIII, §XV). Much of Tables XIII–XXV and the appendix artifact log reads like an internal audit trail rather than journal content. The manuscript should be condensed substantially (a large fraction of the sensitivity tables belong in an online-only supplement), with a single clear statement of scope and one consolidated systematics discussion.

**[MINOR] 8 — Abstract is a wall of numbers.**
The abstract front-loads ~a dozen numerical values (contrast, SE, CI, p-values from three different nulls) before the reader knows the question or the scope. It should lead with the science question and the qualitative result, then give one headline number with its interval, deferring the battery of secondary p-values to the body.

**[MINOR] 9 — Grid-unresolved R_s=10 rows retained "for completeness."**
Table XI / §VII retain R_s = 10 Mpc/h cells that sit below the 25.9 Mpc/h grid sampling scale and are "excluded from the robustness claim." Carrying sub-grid, physically meaningless smoothing cells in the headline sweep table (even flagged) invites confusion; these belong in a supplement or a footnote, not the main sensitivity table.

**[MINOR] 10 — "AI-assisted methodology" statement and single-author verification.**
The disclosure (§Acknowledgments, "AI coding and review tools assisted pipeline execution and manuscript preparation") is appropriate, but given issue #2 (broken/incomplete provenance and unresolved hashes), the assurance that "the author verified the reported quantities against the versioned code and artifacts" cannot presently be checked by a referee. Resolving #2 also resolves the verifiability of this statement.

### (3) Is the central claim supported?

Within the data presented, yes — the environmental non-detection of a classifier-labelled void/non-void CW-fraction difference is internally well-supported and robust across an unusually thorough battery of nulls and sensitivities; but its scientific reach is narrow (an attenuated, catalog-specific proxy that the authors themselves say constrains neither physical handedness nor cosmology), and the paper cannot yet stand as an independent, reproducible AJ contribution while its foundational label catalog (Paper IV) is unpublished and its own data/DOI/provenance release is incomplete.
