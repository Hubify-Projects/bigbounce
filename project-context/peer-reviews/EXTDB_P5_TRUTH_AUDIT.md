# EXTDB P5 — Truth Audit (DE-BIASED external round)

Paper: P5 DESI chirality (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, v0.1.87)
Round: EXTDB (de-biased referee prompt)
Verdicts: Grok **MAJOR** (outlier) · ChatGPT **MINOR** · Gemini **MINOR (no majors)**
Audited: 2026-06-27 · patterns 061/063/064 + calibration applied

## Bottom line

**Grok P5 MAJOR is a FALSE-POSITIVE at the MAJOR/integrity tier.** Both of Grok's
load-bearing MAJOR claims (M1 post-hoc DESIVAST garden-of-forking-paths, M2 Paper IV
dependence) are real *issues* but mis-severitied: they are presentation /
self-containedness MINORs that the paper already substantially addresses in-text.
The integrity ("post-hoc selection to favor a result") framing is FALSIFIED.
Calibration matches ChatGPT/Gemini = MINOR. Verdict alignment: **no MAJOR action; ≤2 MINOR polish items.**

---

## Claim 1 (Grok M1) — Post-hoc DESIVAST primary selection / garden of forking paths

**Verdict: FALSIFIED as a result-driving / integrity defect → downgrade to MINOR (abstract wording).**

Three independent falsifiers, all in-source:

1. **Result is ROBUST across void-finders — the choice does not drive the null.**
   The headline is invariant across all FIVE DESIVAST estimators:
   - VoidFinder, V2-REVOLVER, V2-VIDE (sphere-PIS): |Δf_CW| ≤ 0.002 (largest |Δ|=0.0019, V2-REVOLVER), |z_Δ| ≤ 1.12, p_Δ ≥ 0.26 (`tab:desivast_three_algo`, l.1158-1160)
   - V2-REVOLVER + V2-VIDE GALZONE catalog-native: |Δf_CW| ≤ 0.0037, |z_Δ| ≤ 1.25, p_Δ ≥ 0.21 (l.1161-1163, l.586-593)
   - Bonferroni-5 threshold |z|=2.58; **no row approaches it** (l.1163-1168).
   Because every void-finder + GALZONE definition returns the same clean null, "post-hoc
   DESIVAST chosen because it favors the result" is structurally falsified — there is no
   favorable-vs-unfavorable fork *within* DESIVAST. **Grok's own Strength #3 concedes this**
   ("all five estimators give |Δf_CW| ≤ 0.0037 with |z_Δ| ≤ 1.25"), i.e. Grok's report
   contains the falsifier for its own M1.

2. **The primary choice is principled / a priori-justifiable, not result-chasing** (§`sec:primary_path`, l.1122-1139):
   - ~130× larger sample (n_void = 56,981 vs T-Web n=428)
   - peer-reviewed community-standard DR1 BGS catalog (Rincón et al. 2025, ApJ 982, 38)
   - ships 3 independent void-finders for built-in robustness + catalog-native zone memberships
   - T-Web void bin is *demonstrably contaminated*: 0/6 purity vs DESIVAST holes at z ≤ 0.24, survey-edge-artifact dominated (l.2141-2154). The "favorable" path is the *cleaner instrument*, not a cherry-pick.

3. **Post-hoc status is explicitly disclosed** (l.1117-1120): "a single a priori preregistered
   analysis plan was not filed; the choice ... is therefore made post-hoc, and we declare it
   explicitly here to bound the garden-of-forking-paths concern." Full analysis-tree
   declaration in `tab:analysis_tree`; both paths reported.

Honest residual (MINOR, ChatGPT-M2 / ChatGPT-M3 tier): the abstract could state "post-hoc
declared primary path" explicitly and ensure T-Web reads as clearly secondary. This is
wording polish, not a re-analysis. **Not a MAJOR.**

## Claim 2 (Grok M2) — Heavy dependence on unpublished Paper IV

**Verdict: STALE / OUT-OF-SCOPE (R52-addressed) → at most MINOR self-containedness ask.**

- The headline estimand is the **two-sample void-vs-non-void Δf_CW contrast, which is
  explicitly invariant under any catalog-wide monopole shift** (l.488-489, l.719-726):
  "if the Paper IV (or internal) monopole value shifts ... the Δf_CW null does not [move]."
  The R52 reframe is in place — the headline does not depend on P4's monopole.
- The monopole f_CW^P5 = 0.49719 is **measured internally** on the paper's own 812,793
  env-labeled rows (`tab:p4_monopole_residual`, l.481-484, l.711-718); P4 only *corroborates*
  it (internal Δf_CW^P5 ≈ −0.0028 vs P4 −0.0026). Not imported.
- P4's withdrawn harmonic-ℓ=1 channel does **not** touch P5: "the per-galaxy catalog labels
  and the monopole offset consumed by this paper are unaffected by Paper IV's
  harmonic-channel revision" (l.740-742).
- Genuine dependency: P4 supplies the per-galaxy CW/CCW labels (input data) + is "in
  preparation" (l.436-437). That is a data-provenance / companion-timing point, **not** an
  integrity or forking-paths defect. §`sec:p4` + §`sec:chirality_catalog` already give a
  self-contained classifier summary (equivariant ViT-Small + Z₂ TTA).

Honest residual (MINOR): confirm P4 submitted/accepted, or note it, before journal submission.

## Other Grok MAJORs (severity check)

- **M3 (RSD on T-Web class)** — T-Web is the *secondary* path; the primary DESIVAST null
  explicitly "does not depend on the T-Web RSD argument" (l.2118-2121). DESIVAST RSD is
  bounded by an FoG Monte Carlo: Δf_CW stays in [−0.34,+0.37] pp under σ=5 Mpc/h
  perturbation, max |z|=1.93 (l.2087-2102). MINOR-tier at most.
- **M4 (bright/dark ~2σ filament residual)** — secondary per-stratification diagnostic,
  flagged in-text and bounded by Bonferroni-5 primary/secondary separation (l.1171-1176).
  Already partly Gemini-m1's exact-overlap-free request (MINOR).

## Calibration (patterns 061/063/064)

- **064 — Grok is the harsh outlier.** Prior P5 Grok REJECTs were primary/secondary-*inversion*
  false-positives. Here Grok did NOT invert (correctly named DESIVAST primary) but inflated
  honest-and-disclosed presentation points to MAJOR while its own Strengths section already
  concedes the robustness (#3) and honest disclosure (#4) that falsify the MAJOR severity.
- **061/063 — severity inflation.** ChatGPT and Gemini independently rate the *same* facts
  MINOR / no-major. 2-of-3 de-biased referees converge at MINOR; Grok is the lone inflater.

## Action

No MAJOR closure. Two optional MINOR polish items (matching ChatGPT M2/M3):
1. Abstract: add explicit "post-hoc declared primary path" phrase + ensure T-Web reads as secondary.
2. Note Paper IV submission status when known.

Neither requires re-analysis. P5 headline (DESIVAST void/non-void null, Δf_CW=+0.0007,
p=0.76, robust across 5 estimators) stands. Verdict-first: **Grok MAJOR = FALSE-POSITIVE.**
