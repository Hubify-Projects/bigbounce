# CLAUDE INT Referee Report — Paper P5 (DESI Chirality)

**Manuscript:** *A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1*
**Author:** Houston Golden
**Version reviewed:** v0.1.141-2026-07-16 (Dated July 16, 2026, 16:36 PT), 42 pp
**PDF path:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf`
**Target venue:** AJ (Astronomical Journal)
**Referee leg:** Claude INT (Claude-stack), independent journal referee
**Review date:** 2026-07-22

## EXACT-PDF BINDING VERIFICATION

- Bindings file: `scratchpad/intwave_bindings.json`, paper P5.
- Recorded sha256: `4cca09d0aa963ae18b908bc17f57e9b1bf8f91e4ec8555f4c18d2e413a7580ac`
- Computed `shasum -a 256` on the on-disk PDF: `4cca09d0aa963ae18b908bc17f57e9b1bf8f91e4ec8555f4c18d2e413a7580ac`
- **RESULT: MATCH.** Review proceeds against the exact bound PDF. Every page read (pdftotext -layout, 2520 lines / 42 pp).

---

## SUMMARY ASSESSMENT

This is a mature, heavily-audited null-result methods manuscript. It is scrupulously
hedged: it repeatedly and correctly frames the result as an exploratory, post-hoc,
non-preregistered, catalog-specific classifier-label non-detection — explicitly *not*
a physical-handedness, real-space, or cosmological constraint. The internal-consistency
bar is met to an unusually high degree: I recomputed the headline contrast flow, every
4×2 contingency table, the σ-from-half values, the multiplicity bound, the forward-leakage
reproduction fractions, Eq.(4) term count, and the version stamps, and all reconcile.

I find **no BLOCKER and no MAJOR** internal-consistency, arithmetic, or scope-honesty
defect. Remaining items are genuine but minor presentation/provenance nits, one of which
(orphan references) is a concrete AJ copyediting requirement.

---

## VERIFICATION LEDGER (checks that PASSED — evidence cited)

**Headline focal contrast (abstract ↔ §VI A ↔ Table VI ↔ §VIII C ↔ §XV Conclusions):**
∆fCW = +0.00145442, SE = 0.00331502, 95% CI [−0.00504290, +0.00795174], normal p = 0.66085,
null-imposed 99,999-draw Rademacher wild-cluster score p = 0.67345, seed 20260715, G=50
NSIDE=4 clusters, N=145,766, K=13. Identical in all five locations. ✓

**Sample flow (abstract ↔ Table V ↔ §VIII C):** GALZONE TARGET universe 694,642
(= 604,032 NGC + 90,610 SGC ✓); joined 145,789; OUT=0 quality parent 145,766; VoidFinder
hole-union member 31,937 (15,873 CW) / non-member 113,829 (56,741 CW); crude contrast
= 56741/113829 − 15873/31937 = 0.49848 − 0.49701 = +0.00147 ≈ +0.001466 ✓.

**Eq.(4) "eight terms" systematic budget:** Eq.(4) nuisance covariates = {z, r, logR, q,
E, P(PHOTSYS), M(morphology), e(GALZONE edge)} = 8, mapping exactly onto the abstract's
list "redshift, imaging leg, magnitude, size, morphology, extinction, classifier
confidence, GALZONE edge flag." Intercept + void indicator + 8 nuisance, expanding through
categorical PHOTSYS(3→2 dummies) + morphology to the stated 13 design columns. Consistent
with §VIII C. ✓

**Designated-primary / exploratory estimand language:** Abstract, §I, §II, §V B, §VIII,
§XII, §XV all consistently designate one focal descriptive released-parent estimand and
label all VoidFinder any-hole / sphere-PIS / T-Web / Tempel / ASTRA paths as sensitivities
or secondary diagnostics; the post-hoc hierarchy change is disclosed in the abstract and
§V B. ✓

**Multiplicity bound [A45]/[A46] (§V B):** Table IV enumerates 1 focal + 5 DESIVAST
sensitivity + 9 Bonferroni-9 secondary + 8 descriptive = **23 paths** ✓ (matches "N=23").
pglobal ≤ min(1, 23 × pmin) with pmin=0.036 → min(1, 0.828) = 0.82 ✓. Whole-tree
non-detection statement consistent.

**Forward-leakage injection [A47]/[A48] (§VI E, Table X):** 3.61/4.66=77.5%→78% (cluster),
3.74/4.74=79% (cluster bright arm), 3.67/4.75=77% (no-void-coverage sky); single-arm range
77–79% ✓; sign-flip 1.87/2.13=88% ✓ (predicted −0.81 pp/zpred=−1.87 vs observed −0.92 pp/
zobs=−2.13, residual z=−0.26 ✓); filament-class over-prediction 133% leaving +0.85σ
(obs −2.61 − pred −3.45 = +0.84) ✓. "77–88%" summary window is correct. Forward-injection
prediction (program-mixture-weighted, e.g. −3.67 for no-void bin) is correctly distinguished
from the single-scalar σpred subtraction (−3.20 for the same bin, §VIII F) — not a conflict.

**σ-from-half definition self-consistency:** Table VII void −0.68 [(207−214)/(0.5√428)],
filament −2.61, cluster −4.66, wall +0.55 all reproduce from the tabulated integers ✓.
Eq.(1) σpred = 2·∆fCW·√N reproduces filament −3.32, cluster −3.28, density-quintile 2.07,
no-void 3.20, 6+ bin 2.64. ✓

**Contingency tables (Appendix B):** Table XXIII 4×2 sums to n=812,793, marginals CW=404,111
/ CCW=408,682, per-class integers all check (e.g. filament 203,261/204,926) ✓; χ²=3.55,
3 dof, p=0.31 ✓. Table XXIV bright+dark subset n=811,609, per-class bright/dark integers
check, χ²=4933, Cramér's V=√(4933/811609)=0.078 ✓.

**ASTRA overlap (Table XXI):** T-Web on-overlap 1/2/7,972/17,211 = 25,186 ✓ (filament 31.7%,
cluster 68.3%); ASTRA argmax 2,985/7,980/8,864/5,357 = 25,186 ✓; the "repeated 31.7%"
coincidence (ASTRA sheet 7,980 vs T-Web filament 7,972) is explicitly flagged as
non-copy-error ✓.

**DESIVAST membership variants (Tables XIII, XVI, XVII):** hole spheres 89,003+12,860=101,863
✓; maximal voids 3,241+524=3,765 ✓; exact k-unbounded void 57,081 vs k=20 56,981 (100
galaxies, 0.18%) consistently distinguished; exact unrestricted ∆fCW=+0.0006 vs k=20
+0.0007 vs footprint-restricted exact +0.0018 — all three internally reconciled and
correctly cross-referenced across §VIII A/B/F and Table XIII.

**Bright/dark marginal-mixture (§VI E, Table XV):** void 469/56,981=0.82% dark, non-void
5,845/621,964=0.94% dark, diff 0.12 pp ✓; 0.81 pp × 0.0012 ≈ 0.001 pp ✓; Table XV
sub-totals (56,946 void + 620,923 non-void; 35 + 1,041 = 1,076 short) all check ✓;
tracer-program split bright 775,760 + dark 14,782 + backup 875 + other 218 = 791,635 ✓.

**Monopole self-corroboration:** catalog fCW=0.497353(279) (App A) ↔ P5 matched-sample
fCW^P5=0.49719 (§II, §VIII G) ↔ Paper IV ∆fCW^P4=−0.0026; ~8% enhancement reconciled in
§VIII G (observed −5.00σ on 791,635 ⇒ ∆fCW≈−0.0028). ✓

**Version stamps:** title-page "(v0.1.141-2026-07-16)", Appendix C "release candidate
v0.1.141-2026-07-16", Appendix D artifact map "candidate v0.1.141-2026-07-16" all agree. ✓

**Paper IV status (bibitem [3]) — checked per instruction:** consistently and honestly
stated as "companion manuscript in preparation," "not yet a verified public preprint,"
"no arXiv identifier or Zenodo DOI asserted," "Paper IV has no verified arXiv identifier
at this stage." The public CC-BY-4.0 label/weight artifacts are correctly separated from
the unpublished manuscript. **No misstatement of Paper IV status** — the known tracked
back-patch gate is disclosed, not misrepresented. Not flagged.

**No undefined `??` cross-references; Figures 1–9 and Tables I–XXVI all present and
referenced.** ✓

---

## FINDINGS

### MINOR-1 (presentation; AJ copyedit requirement) — Two orphan references
References **[4] (Paper II — "f_NL = −35/8 Forecast: SPHEREx Discrimination…")** and
**[8] (Hamaus, Sutter & Wandelt, "Universal density profile for cosmic voids," PRL 112,
041304)** appear in the reference list but are **never cited anywhere in the body text**.
Evidence: exhaustive in-text citation count over pp.1–39 gives [4]=0 and [8]=0 occurrences
(the only range citation in the body is "[5–7]" in §XIII Limitations, which does not cover
[4] or [8]); the strings appear solely in the bibliography (p.40). AJ/ApJ copyediting flags
uncited references. **Fix:** either cite them at a natural point (Paper II in the §I/§XII
bounce-vs-inflation-scope framing; Hamaus in the §VIII void-geometry / RSD-displacement
discussion) or remove them from the reference list. The task explicitly asked to check the
Paper-II bibitem cross-reference — Paper II [4] is present but uninvoked.

### MINOR-2 (provenance/version-stamp) — Multiplicity-bound artifact one patch behind
Appendix D (Table XXVI) lists [A45]/[A46] as
`analysis/global multiplicity bound v0 1 140.py`/`.json` — a **v0.1.140** filename stamp
carried into a **v0.1.141** manuscript — whereas the sibling forward-leakage artifacts
[A47]/[A48] are stamped `…v0 1 141`. This is visible to a referee reading the artifact map.
It is not an error if the bound was unchanged since v0.1.140 (the analysis tree is frozen),
but the mixed stamping invites a "why is this one older?" query. **Fix:** either re-stamp to
v0.1.141 or add a one-line note in Appendix C/D that the multiplicity bound is unchanged
since v0.1.140 and intentionally retains its creation stamp.

### MINOR-3 (numeric presentation) — Monopole counting-significance quoted at two values
The catalog-monopole counting significance is written as "≈ 9σ" in the abstract, §I, and
Table I, but as "−9.47σ" (App A), "∼ 9.5σ" and "∼9.5σ" (§VIII G). All are consistent to
rounding, but the abstract/intro "≈9σ" visibly understates the 9.47σ figure used later.
**Fix:** standardize on a single value (recommend "≈9.5σ") across abstract, §I, Table I,
§VIII G, and Appendix A. Trivial, but it is exactly the kind of headline-vs-body drift a
careful referee circles.

### (Tracked gate, not a defect) — Paper IV public-release dependency
The focal contrast depends on the Paper IV per-galaxy `class_eq` labels; the manuscript
correctly (a) notes the labels/weights are already public under CC-BY-4.0, (b) shows the
headline void/non-void ∆fCW is algebraically monopole-invariant and thus refereeable from
public DESI/DESIVAST/GZ1 data alone, and (c) states the focal inputs must be re-verified
against the final published Paper IV release before submission (§II, §XIII, Appendix A,
Appendix C). This is the known tracked back-patch gate; it is disclosed accurately and does
not alter my verdict. No action beyond the existing pre-submission gate.

---

## SCOPE-HONESTY ASSESSMENT
Strong. The post-hoc focal-estimand selection (garden-of-forking-paths risk) is disclosed
in the abstract and §V B, and the whole-tree multiplicity bound (pglobal=0.82) demonstrates
that no path survives correction — so the disclosure is backed by a quantitative bound, not
just a caveat. The T-Web path is repeatedly and correctly demoted to a secondary,
survey-shell-contaminated diagnostic. Physical-handedness de-attenuation (2a−1=0.398 factor)
is stated but explicitly *not* applied. The paper does not overclaim.

## RECOMMENDATION
No BLOCKER, no MAJOR. Three MINOR fixes (orphan references [4]/[8]; artifact version-stamp
harmonization; single monopole-σ value). The orphan-reference fix is a concrete AJ
requirement. Recommend **MINOR-REVISIONS**.

VERDICT: MINOR-REVISIONS
