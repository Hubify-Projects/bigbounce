# R52 P2 — Truth Audit (Opus judgment leg)

**Paper:** P2 — "Testing the Matter Bounce with Primordial Non-Gaussianity:
A SPHEREx Sensitivity Recast with a MegaMapper Outlook" — v1.7.70 (29 pp).
**Canonical PDF:** `site/public/papers/paper2_fnl_forecast_v1.7.70.pdf` (md5 99e6426c, 29 pp).
**Canonical source (CONFIRMED):** `research/focused_paper_source_integration/02_full_draft.tex`
— title matches "...A SPHEREx Sensitivity Recast with a MegaMapper Outlook",
`\date{June 19, 2026}` (L27), version comment `v1.7.70` (L29).
NOTE: `research/focused_paper_source_integration/arxiv_package/main.tex` is a
**STALE/different build** (title "...Forecasts for SPHEREx and MegaMapper",
`\date{\today}`, 270 lines vs 1175) — do NOT cite it as the submission source.

**Reviewer recommendations (as written in-text):**
- Claude/Opus leg: MINOR REVISIONS (1 MAJOR).
- OpenAI (gpt-5) methodology: MAJOR REVISIONS.
- Grok (grok-4.3) adversarial: MAJOR REVISIONS.
- Gemini (2.5-pro) cosmology: ACCEPT WITH MINOR CORRECTIONS.

---

## NET VERDICT: MINOR REVISIONS. No BLOCKER.

The science is sound and the headline arithmetic was independently re-derived by
two reviewer legs (Claude + OpenAI spot-checks) and is consistent with the
committed source. The OpenAI/Grok MAJOR verdicts rest on (i) a submission-time
DOI/release-tag that cannot pre-exist, (ii) labeling/wording refinements the body
text already substantively supports, and (iii) **two falsified misreads of the
rasterized PDF**. The single genuine repo defect is one missing released
artifact (`phase3_bispectrum_shape_overlap.json`), and the headline result it
backs is fully reproducible from the committed generator.

### VERIFIED counts by tier
- **DO-NOW text/repo (real, low-effort):** 1 MAJOR-grade repo defect (missing
  json) + ~10 MINOR labeling/wording fixes + ~2 NIT = **~13 items**.
- **VERIFIED figure-layer (defer to D-round, image-based):** **5 items**.
- **VERIFIED but TRULY-BLOCKED (submission-time):** **1** (Zenodo DOI / frozen tag).
- **FALSIFIED:** **3** (Eq-2 inversion; shot-noise "contradiction"; \date{\today}).
- **STALE:** **1** (Eq-2 "i k^3_i" typesetting — source is clean).
- **OPINION (no required action):** **~6** (length ×2, mission-timeline ×2,
  email, internal-jargon).

---

## ADJUDICATION — the Claude-leg MAJOR (missing `phase3_bispectrum_shape_overlap.json`)

**Verdict: VERIFIED — real released-bundle defect, DO-NOW, LOW effort.**

- **ABSENT?** YES. `find` over the repo (excluding `.git`) returns zero hits.
  It is referenced only in **body prose at L713** ("...archived as
  `phase3_bispectrum_shape_overlap.json` (released with the paper's code)...
  enabling independent reproduction of the r = 0.84 ± 0.02 noise-weighted central
  value"). It is **NOT** even listed in the formal "Data and Code Availability"
  section (L1066–1068) — so the body over-promises an artifact the formal list
  omits and the repo lacks. Two-way internal inconsistency.

- **REPRODUCIBLE?** YES. The generator `null_space_analysis.py` IS committed and
  runnable; it computes and **prints** the r = 0.85 ± 0.13 null-space scan and the
  r ≈ 0.84 weighting values. Caveat: the script is **print-only — it writes no
  JSON** (grep: no `open()/dump/np.save`). So "just re-run it" does not by itself
  emit the named artifact; the json must be added as an explicit dump.

- **All OTHER named artifacts EXIST** (verified present):
  `phase3_fisher_overlap.json` (under `research/matter_bounce_parameters/`,
  inside the `/tree/main/research/` URL the paper points to — resolves, though not
  co-located), `c8_fnl_running_fisher.py`, `c9g_bf_table_recompute.py`,
  `c9h_nullspace_significance_propagation.json`, `c9i_epsilon_ratio_check.json`,
  `null_space_analysis.py`, `c9j_bf_template_rescale.py`,
  `c9k_gr_continuous_marginalization.py`,
  `c9l_sigma_theory_continuous_marginalization.py`. Only the one json is missing.

- **FIX (DO-NOW, hardest-path-first primary):** add a JSON-dump block to
  `null_space_analysis.py` emitting the full bispectrum-shape coefficient map +
  per-configuration overlap values for the six monomial coefficient sets; run it;
  commit `phase3_bispectrum_shape_overlap.json`; ADD it to the formal Data &
  Code Availability list (L1068). Then run `/artifact-link-verify`.
  **Fallback (minimal):** repoint the L713 prose from the nonexistent json to the
  committed `null_space_analysis.py` (already in the formal list). Primary is
  cheap (script already computes everything) and honors the paper's
  "everything-released-and-reproducible" credibility model — take it.

---

## DEDUPED FINDINGS + VERDICTS

### FALSIFIED (do NOT act; do not "fix" a false positive)
- **OpenAI P2-E6 — Eq.(2) dimensional inversion (claims `B_NL ∝ P/A_T`).**
  FALSIFIED. Source Eq.(2) L620 is `B_NL = (10/3) A_T / Σ_i k_i³` (A_T in the
  **numerator**, not P/A_T). The degree-count at L623 is correct and
  self-consistent: A_T = P(deg 9)/(k1²k2²k3²)(deg 6) → deg 3; ÷ Σk_i³(deg 3) →
  deg 0, dimensionless. Reviewer misread the rasterized math. Gemini + Grok
  (both full-PDF) flagged no such error — corroborates.
- **OpenAI P2-M7 — shot-noise "numerically contradictory" (15–30% vs √11≈3.3×).**
  FALSIFIED as a contradiction. L736 explicitly separates the two: the naive
  Poisson amplitude scaling gives 3.3×, while the **bispectrum-estimator effective
  degradation at the squeezed-limit modes** that dominate f_NL is 15–30% (because
  the squeezed limit downweights the high-k modes where shot noise bites). Same
  sentence reconciles them. Downgraded to a MINOR mis-attribution clarity fix
  (the opening clause loosely attributes "15–30%" to "a simple Poisson estimate")
  — see DO-NOW #2. Not load-bearing (anomaly-tracer caveat, not the headline).
- **Claude m4 — `\date{\today}`.** FALSIFIED against the canonical source
  (`02_full_draft.tex` already uses `\date{June 19, 2026}`). Real only for the
  stale `arxiv_package/main.tex` dupe — folded into DO-NOW #10.

### STALE
- **OpenAI P2-m1 — Eq.(2) "i k^3_i" ambiguous typesetting.** Source L623 defines
  `\sum_i k_i^3 \equiv k_1^3+k_2^3+k_3^3` explicitly. Rasterization read artifact;
  no source action.

### VERIFIED — DO-NOW (text / repo, low effort)
1. **[MAJOR-grade]** Missing `phase3_bispectrum_shape_overlap.json` — see
   adjudication above. Action: regenerate + commit + add to formal list (+
   `/artifact-link-verify`).
2. **[MINOR]** Shot-noise opening sentence (L736) mis-attributes "15–30%" to "a
   simple Poisson estimate" (Poisson → 3.3×; 15–30% is the bispectrum-downweighted
   value). One-clause rewrite to attribute each number to its mechanism.
3. **[MINOR]** Abstract: explicitly label the 2.6–5σ "realistic" band as an
   additive-in-quadrature systematic budget (NOT a joint Fisher); add the
   curvaton-narrow BF ≈ 4–7 alongside 9–14; add "(after r→1 bookkeeping)"
   qualifier on the BF headline. (Claude m1; OpenAI E5, M6; Grok E1, E4.) Body
   already supports all three (L734, L818, L873) — abstract-only edits.
4. **[MINOR]** Soften "robust across the bounce class" re assumption (d)
   cubic-order ε-transfer → state it is supported at linear order with an
   order-of-magnitude superhorizon estimate, and that the forecast uses the
   central κ_ε (∈[5.6,80] is a schematic span, not a forecast band). (Claude m3;
   Grok M2.) Body L990 already hedges heavily; tighten the one "robust" claim.
5. **[MINOR]** Add the explicit Gaussian-bounce-prior Bayes-factor formula
   (marginal N(f_obs; μ0, σ²+σ_theory²) → closed form with σ_eff→√(σ²+σ_theory²))
   so Table II Gaussian rows are reproducible from text. (OpenAI E4.)
6. **[MINOR]** Add a compact r-vs-weighting table (the four values 0.829 / 0.830 /
   0.835 / 0.876) and reconcile the "10 schemes / five region-masked / four
   values" wording (L708 lists exactly 10 schemes; only 4 r-values feed the
   headline). (OpenAI E3, M4.)
7. **[MINOR]** Reframe the ℓ-space CMB-Fisher overlap (r = 0.878 ± 0.012) as a
   cross-check rather than a "validation," noting limited commensurability with
   the 3D LSS bispectrum. (OpenAI M8.)
8. **[MINOR→MAJOR writing]** Tighten the injection–recovery description: state it
   is a 2D KSW-type test, full-sky, SPHEREx Gaussian noise covariance, 200
   realizations; specify patch/k-range; explain why r_meas = 0.90 ± 0.01 exceeds
   r_CMB = 0.876; move to an appendix labeled as a consistency check with stated
   limitations. (OpenAI E2, M3.) Real reproducibility-from-text gap; not a
   numerical error.
9. **[MINOR]** Rephrase the LSS noise-weighting sentence (L713/§III B: "noise
   concentrated at large scales where the bounce template departs most") for
   precision — the templates coincide in the exact squeezed limit; the
   *integrated* mismatch over non-squeezed configs drives the drop. (Gemini M1,
   with a ready replacement sentence.)
10. **[MINOR repo-hygiene]** Reconcile/remove the stale
    `arxiv_package/main.tex` (different title, `\date{\today}`) so it can't be
    mistaken for the v1.7.70 submission source; canonical is `02_full_draft.tex`.
    (Disposes Claude m4.)
11. **[NIT]** Justify/cite the "CMB Fisher weighting ∝ k²" label or relabel as an
    ad-hoc sensitivity check. (OpenAI m10.)
12. **[NIT]** δC/C ≲ 5×10⁻⁴ (L730): inputs are already given at scaling level
    (Δ_ζ²≈2.1e-9, f_NL²Δ_ζ²~4e-8, N_modes~V k²δk/2π²) and explicitly labeled a
    heuristic check — optionally plug one V_survey/δk number. Low priority.
    (OpenAI M1.)
13. **[NIT]** Gemini N2: use `b_φ` (not `bφ`) in the Table IV caption.

### VERIFIED — figure-layer (DEFER to D-round; image-based, not science)
14. Grok P2-E3: Fig. 2 — conservative-b_φ SPHEREx bars shown without error bars
    while the caption claims the bars span optimistic→conservative endpoints.
    Correct figure or caption.
15. OpenAI P2-M9: Fig. 5 — flat red dashed σ(f_NL)=0.7 line conflicts with the
    "20–50% b_φ degradation" prose; annotate as "UMF-fixed baseline" or add the
    degraded curve.
16. OpenAI P2-M5: Figs. 4 & 5 — add k-units (h Mpc⁻¹), k_min/k_max sampled,
    z-binning, number-density assumptions to captions.
17. OpenAI P2-M10: Fig. 2 — define the MegaMapper "conservative" and
    "single-tracer" bars (σ(f_NL), priors, z-range).

### VERIFIED — TRULY-BLOCKED (submission-time only)
18. Zenodo DOI placeholder "(DOI inserted at submission)" + frozen git tag /
    commit hash (OpenAI E1; Grok m3; Gemini N3). Cannot pre-exist a deposit.
    Route to the P-round / arXiv-kit checklist; mint DOI + stamp tag at submission,
    then verify every named artifact resolves in the frozen release.

### OPINION (no required action)
- 29-page length "too long for a recast" (OpenAI M2; Grok M1) — editor preference.
- SPHEREx mission-timeline staleness "launched March 2025" (OpenAI m3; Gemini N1)
  — optional footnote.
- Non-institutional email (Gemini N4) — no scientific change.
- Internal "headline / bookkeeping / rebooking" jargon, hyphenation nits (OpenAI
  m5, n2) — optional copy-edit.

---

## CLOSURE PLAN (tiers)

**DO-NOW (this revision):** items 1–13. Item 1 is the only repo action
(regenerate + commit json + amend Data Availability + `/artifact-link-verify`);
items 2–13 are `02_full_draft.tex` edits (abstract labeling, one equation, one
small table, several one-sentence rewrites, symbol fix) + removing the stale
`arxiv_package/main.tex`. All low-effort; none touches the science or the
verified arithmetic.

**DEFER to D-round (visual pass):** items 14–17 (figure/caption corrections;
image-based, belongs in `/paper-design-round`).

**TRULY-BLOCKED until submission:** item 18 (Zenodo DOI + frozen tag) → P-round /
arXiv-kit checklist.

**NO ACTION:** FALSIFIED (E6, M7-as-contradiction, m4-canonical), STALE (m1),
OPINION cluster.

---

*Audit: Opus judgment leg, R52, 2026-06-26. Verdict-first anti-fabrication gate.
Source confirmed against v1.7.70 PDF before citing line numbers. No ACCEPT faked;
the missing artifact is real and actioned; two reviewer "MAJOR/ESSENTIAL" math
findings were falsified against the source rather than "fixed."*
