# INT Codex-subscription Review — P5 v0.1.136-2026-07-15 — gpt-5.6-sol (high)
paper: P5  version: v0.1.136-2026-07-15  tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=43873a9cc0182e15b3f9eda93f0b80602b1e35406b28d1577288a3f9860b6a4d  prompt_sha256=d7928f7a7f6320ee8963ee6a5b33e01f940043c7397f1e0d5327e037e635ad6b
provenance: commit=e97f0b7365267355d06e5a979738ea5d6675950f  source_sha256=6cff40bf8be5a21f5031226237b53677c80494f3b90d5bd572089cf889bc7c16
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/cd3c8e81fc6811438d8db7059631feb2d9ccf324f2996370ee555e68def91fc4.pdf  sha256=cd3c8e81fc6811438d8db7059631feb2d9ccf324f2996370ee555e68def91fc4  pages=40
venue: The Astronomical Journal  article_type: Observational research article  profile: AJ-OBSERVATIONAL
source_tree: clean detached sparse tree at e97f0b7365267355d06e5a979738ea5d6675950f (scope=pipelines/p5_desi_chirality/paper)
UTC: 2026-07-16T07:04:33Z
context-note: Exact-PDF confirmation after truth-audited v0.1.135 confirmation closure

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] The classifier-label validation is not demonstrably independent. No retained object manifest proves that the 6,637 GZ1 training objects were excluded from the later GZ1 validation sample, while the void-specific validation has only 933 objects and a ±3.7 percentage-point uncertainty—far wider than the 0.145-point focal contrast. Either provide independent validation tied to the exact checkpoint or restrict interpretation strictly to the recorded classifier labels. `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:4805-4820`, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:4860-4916`

2. [MAJOR] The manuscript retains contradictory focal estimands and an unjustified target-program leakage bound. The declared focal result is the adjusted 145,766-object contrast of +0.00145442, but active discussion calls the separate 57,081-void footprint sensitivity (+0.0018) “focal.” Moreover, multiplying the marginal bright/dark difference by the difference in program fractions is not a maximum leakage bound when a program-by-environment interaction remains untested; the reported dark-only contrast is +4.71 percentage points. `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:1665-1773`, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:2290-2302`, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:3211-3221`, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:4329-4337`

3. [MAJOR] Clustering robustness has not been demonstrated for the promoted 13-column headline inference. Its CR1 interval and wild-score test use 50 NSIDE=4 angular clusters, whereas the 3,750-nearest-MAXIMALS sensitivity applies only to the different 78-column model. A like-for-like three-dimensional or multi-resolution clustering analysis is required for the focal model. `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:1736-1763`

4. [MAJOR] The submission is not yet supported by the availability statement it requires. The manuscript admits that no immutable public tag or DOI exists, while also claiming that canonical T-Web grid arrays are retained; those arrays are absent from the committed tree, which contains configurations and summary reports only. The complete analysis release must be archived and its regeneration verified before acceptance. `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:5054-5096`, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:5117-5127`, `pipelines/p5_desi_chirality/data/README.md:16`

5. [MINOR] The Phase-2 Bonferroni comparison does not match the reported search statistic. Each cell reports the maximum over four classes, but that statistic is compared with a nine-test threshold rather than calibrating the class maximum or all class-by-cell comparisons; the committed permutation result should be used as the primary multiplicity control. `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:2517-2527`

6. [MINOR] The statement that the weighted rebuild reassigns approximately 73% of T-Web “void” galaxies is unsupported. The committed artifact reports that 26.6% of all matched spirals retain their class, meaning 73.4% change class overall; it does not give a void-specific 73% reassignment fraction. `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:3785-3815`, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:4381-4390`

7. [MINOR] The focal provenance contract is internally inconsistent: the manuscript promotes the 13-column model as focal, whereas its generating artifact describes it as a sensitivity that does not replace the 78-column estimate. The source, artifact metadata, equation, and manuscript hierarchy must agree. `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:1696-1713`, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:1732-1763`

(3) Yes—narrowly, the committed data reproduce the central catalog-specific classifier-label non-detection, but they do not support a physical-handedness or cosmological inference.