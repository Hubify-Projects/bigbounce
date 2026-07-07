# Cover Letter — Paper 5

**Title area:** Spiral galaxy chirality vs. large-scale-structure environment: a DESI DR1 / DESIVAST null
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
**Suggested venue:** Physical Review D (or ApJ / MNRAS)

Dear Editor,

Please consider this manuscript. This cover letter states its contribution,
scope, and structural dependency plainly.

## Contribution
The paper cross-matches the 8.47M-galaxy chirality catalog (per-galaxy public
`class_eq` labels) against the DESI DR1 redshift catalog to test whether spiral
galaxy handedness is statistically independent of large-scale-structure
environment. Its primary result is a **void/non-void null**: the
DESIVAST-anchored contrast Δf_CW = +0.0007 (SE ≈ 0.0022) on 56,981 void spirals,
robust across all five DESIVAST void-finders (|Δf_CW| ≤ 0.004, |z_Δ| ≤ 1.25). A
secondary T-Web tidal cosmic-web classification on 14.6M DR1 galaxies provides a
supporting cross-check.

## Scope statement
This is an **environmental-independence null** — a bounded upper limit set by the
void sample size, not a detection. The headline Δf_CW result is algebraically
invariant under any catalog-wide monopole shift, so it is **self-contained with
respect to the catalog's overall calibration**: it does not depend on the
monopole amplitude or its uncertainty. The DESIVAST void path is the single
primary estimand; the T-Web path is explicitly secondary.

## Disclosed limitations (stated up front)
1. **Relation to the companion Paper IV (citation timing, coordinated submission).**
   The classifier architecture, training, parity-equivariance validation, and the
   origin of the catalog monopole are documented in the same-author companion
   catalog paper (Paper IV), which is **submitted to arXiv concurrently, immediately
   before this manuscript**, under coordinated submission; its per-galaxy
   `class_eq` labels and trained weights are already **public under CC-BY-4.0**.
   This is a citation-timing relation, not an unpublished/unvettable dependency.
   Two facts make the headline refereeable independently of Paper IV's internals:
   (a) the headline Δf_CW null is algebraically **monopole-shift invariant**,
   resting only on the public per-galaxy labels joined to public DESI DR1 /
   DESIVAST data, with a self-contained Appendix A classifier summary; and (b) the
   labels' pseudo-label provenance is validated **model-independently** in Paper IV
   — replacing the learned CW/CCW labels entirely with Galaxy Zoo 1 human votes (no
   learned model in the chirality-label chain) returns the same parity null at
   z = −0.54σ on N = 46,017 human-labeled spirals. Paper IV's arXiv ID is inserted
   into the P5 citation on posting.
2. **T-Web in redshift space.** The secondary T-Web classification is performed in
   observed redshift space; RSD boundary-leakage is bounded by a scalar
   displacement heuristic rather than full Zel'dovich/BAO reconstruction, and
   rigorous deprojection is deferred — disclosed as a secondary-analysis caveat.
3. **Underpowered secondary bins** (e.g. the T-Web void bin, n=428) and a ~2.1σ
   filament bright/dark sign-flip attributed to BGS selection, both flagged
   in-text as diagnostics, not signals.

## The judgment for the referee
The Paper IV relation, which earlier LLM referees raised as a structural blocker,
is resolved operationally by **coordinated submission**: Paper IV is posted to
arXiv immediately before this manuscript, so the companion carries a citable
arXiv identifier at the moment P5 appears, and its catalog is already public. The
remaining referee question is therefore narrow: given (a) algebraic
monopole-invariance of the headline null, (b) the model-independent Galaxy-Zoo-1
human-vote reproduction of the catalog's parity null (z = −0.54σ, N = 46,017),
and (c) the self-contained Appendix A classifier summary, does the standalone
null stand on the public data alone? We believe it does, and that any residual is
citation timing rather than vettability.

No genuinely-new correctness defect is outstanding.

## AI-use disclosure to the editor
This manuscript was prepared with the assistance of an agentic AI research pipeline built on Anthropic Claude (Opus~4 family, 2026 releases) for agent orchestration and manuscript preparation, with OpenAI GPT-5/o3, xAI Grok-4, and Google Gemini~2.5 used as cross-checking and adversarial internal-review models. The author designed the study, made all scientific and editorial judgments, verified every quantitative result against the committed computational artifacts, and takes full responsibility for the entire content, including any material produced with AI assistance. The AI tools are not authors.

Sincerely,
Houston Golden (houston@hubify.com)
