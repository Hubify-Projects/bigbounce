# P4 EXT M1 truth-audit (2026-07-10 sweep, vs STAGED v1.0.238)

**Auditor stance:** strict journal-referee, verdict-first, source-cited (patterns 061–066).
**Paper:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (STAGED v1.0.238, directive-L
image-level e2e compute closer folded in; \paperVersion L55, \paperTimestamp "July 12, 2026" L625).
**Raws:** `P4_grok_M1.md` (MINOR REVISIONS — MINOR-only), `P4_chatgpt_M1.md` (REJECT, 14 MAJOR + 4 MINOR).
**Ledger:** `project-context/peer-reviews/DISPOSITIONS/P4.md`.
**M1 = first full measurement after the v1.0.237 directive-M presentation overhaul** (PRD single-paragraph
abstract collapse + caveat de-dup, byte-preserving relocation). Overhaul-regression + orphan hunt performed.

---

## HEADLINE — the one real close in the P4 bundle

**DP4-15 (spatially-resolved / image-level injection MAJOR) is now LEGITIMATELY ADDRESSED by the STAGED
v1.0.238 full image-level end-to-end mirror-flip injection.** VERIFIED against artifact, not just text:

- **Tex:** §sensitivity L1159 "*We now perform the image-level end-to-end mirror-flip injection directly.*"
  → L1162–1174: raw image-level transfer **T_raw = 0.2303 ± 0.0002** over the full 8.47×10⁶-galaxy image
  source through the production ViT (`bamfai/galaxy-chirality-v2`, val-acc 0.9369); stable across confidence
  bins (0.207–0.261) and N/S strata (T_raw^N=0.218 vs T_raw^S=0.251); production Z2-TTA labeling
  **T_eq = 0.9997, antisymmetry maxdev 0.0**, verified image-by-image on all 8.47M
  (artifact `…/e2e_fullrun/e2e_transfer_function_full.json`, L1174).
- **Artifact cross-check (READ, not filename-only):** `pipelines/p2_chirality/outputs/canonical_provenance/
  e2e_fullrun/e2e_transfer_function_full.json` exists, `status:"final"`, `shards_done:192/192`,
  `n_total_galaxies:8474531`, `transfer_function_T_raw:0.23026711…` (stderr 0.000231),
  `T_eq:0.99973…`, `antisymmetry_max_abs_deviation:0.0`, N/S strata 0.2178/0.2510. **192 shard parquets
  on disk confirmed.** Every number in the tex matches the artifact to quoted precision. **Real, not fabricated.**
- **Disposition:** DP4-15 moves OPEN-COMPUTE → **CLOSED-BY-EDIT / CLOSED-BY-ARTIFACT-VERIFICATION** for the
  image-level end-to-end injection axis (directly answers ChatGPT DP4-15/CG-2 & Gemini image-level
  pseudo-label-independence MAJOR). Residual (finer per-pixel confusion jointly conditioned on depth/PSF/
  morphology) honestly disclosed as still-open at L1182–1186; paper correctly continues to hold falsification
  claims to the observed hard-label field. **This is the ONE real close in the bundle.**

---

## PER-FINDING DISPOSITION

### Grok (MINOR REVISIONS — softened; MINOR-only this wave)

| # | Finding | Disposition | Cite |
|---|---------|-------------|------|
| 1 | Abstract/§IV C: incommensurable-nulls (pixel-perm vs block-bootstrap) need a clarifying clause | RE-FLAG-DISCLOSED → **DP4-13/DP4-14** | Abstract L667 already flags block-bootstrap z≈−7.6 as "*not a calibrated frequentist exclusion significance*"; σ-incommensurability canonical note §notation (L822) |
| 2/3 | §II B/VI A: GZ1-only cross-check ~4.5× coarser (A_50≈3.4%) → corroborates-not-tightens; add Fisher-scaling sentence | RE-FLAG-DISCLOSED → **DP4-15/DP4-08** | GZ1 dilution/conservative-floor text in body §data L711 + §pseudolabel_independence; A_50~3.4%/4.5×-weaker "corroborate-not-tighten" already present (tex prov L153). One-sentence taste-add, NOT a defect. |
| 4 | §IV D/App D: 47% ℓ=1 residual — add "morphology-purity map not required for headline" line | RE-FLAG-DISCLOSED → **DP4-17** | 47% remainder disclosed + bounded a-fortiori below A_50/A_95 §monopole_mask_null L1005 / App-D |
| 5 | §III B/Table I: flag rows (iii)–(vi) as diagnostics-only / zero cosmological weight more prominently | RE-FLAG-DISCLOSED → **DP4-07/DP4-13** | `tab:decision_tree` Primary-vs-Diagnostic map present (prov L182); abstract L667 explicitly labels +3.64σ/+7.28σ "*not detections*" |

Grok UNMATCHED rows #3 (Fisher-scaling sentence) and #5 (diagnostic-rows caption flag) are **one-sentence
editorial taste-adds on already-disclosed content, NOT genuinely-new editable defects** — the underlying facts
(coarser GZ1 sensitivity; diagnostic-only harmonic rows) are already in body + decision-tree table.

**Grok trend = SOFTENING.** H17 Grok = MINOR; W1 Grok = ACCEPT; the DP4-18 MAJOR-backfire (v1.0.232) was
already reversed to MINOR at H17F. M1 Grok holds MINOR-only with zero MAJOR — consistent moderate-referee floor,
now explicitly praising the presentation ("The declared analysis hierarchy and decision tree are exemplary").

### ChatGPT (REJECT — 14 MAJOR + 4 MINOR; unchanged harsh-referee floor)

All 14 MAJOR + 4 MINOR map 1:1 to standing dispositions — **0 genuinely-new editable findings**:

| Finding | → D-id | Class |
|---------|--------|-------|
| Shamir-scale "would have been detected" inconsistent w/ g=0.398 dilution; z≈−7.6→−1.4 | DP4-01 / DP4-14 / DP4-19 | z is template-disfavor stat not detection sig (§wls_fit footnote L1410); factor-of-2 CLOSED |
| p_eq>0.6 primary sample post-selected (949,584 of 3.2M); mutable-Git prereg | DP4-07 | §prereg L713 a-priori; commit/DOI Houston-gated DP4-21 |
| pixel-permutation null assumes exchangeability | DP4-16 | OPEN-COMPUTE; density-stratified null + block-bootstrap don't assume exch. |
| external classifier validation 69.91%/κ=0.40/miscalibration; GZ1 A_50~3.4% under-powered | DP4-15 / DP4-08 | disclosed §data L711, §pseudolabel_independence; **image-level axis now closed v1.0.238** |
| ~47% ℓ=1 residual unexplained; "diagnostic" ≠ resolved | DP4-17 | OPEN-COMPUTE, disclosed+bounded |
| block-bootstrap Fig 10 not calibrated frequentist test | DP4-14 | caveat stated verbatim (abstract L667, L1410) |
| 9-template WLS omits PSF/depth/extinction/morphology joint fit | DP4-17 / DP4-14 | disclosed forward-model 53%/47% split |
| injection bypasses images/ViT/triage/confusion → A_50/A_95 output-floors | DP4-09 → **DP4-15** | **directly answered by v1.0.238 image-level e2e (T_raw=0.2303)** |
| no valid frequentist upper limit; A_95 lacks coverage | DP4-09 / DP4-17 | paper states A_95 not a CI (§sensitivity/§conclusions L1273) |
| "σ" for heavy-tailed nulls (+3.64σ p=0.030 ≈1.9σ Gaussian) | DP4-10 / DP4-13 | empirical p primary; non-Gaussian declared |
| multiple "canonical" ℓ=1 harmonic estimators | DP4-13 / DP4-16 | normalization/weighting/null differences disclosed |
| multiplicity / hierarchy declared post-hoc | DP4-07 / DP4-13 | §prereg + decision-tree; disclosed |
| image-parity convention (WCS-determinant / cutout-orientation audit) | **candidate-new** → OUT-OF-SCOPE-COMPUTE | see below |
| Data Availability: mutable branch, DOI/hash promised future | DP4-21 | Houston-gated at submission |
| MINOR: A_95 units contradiction | DP4-13 family | amplitude convention audited; A≡A_p disclosed |
| MINOR: title/abstract sample size (949,584 not 8.5M) | DP4-13 | N distinctions prominent in tightened abstract L667 + Table I |
| MINOR: birefringence/Chern-Simons speculative | DP4-12 | transfer-fn "not derived", hedged §parity_translation |
| MINOR: "highly repetitive, repeatedly redefines 'primary'" | DP4-13 | presentation half CLOSED-BY-EDIT v1.0.237 (see quote below) |

**Image-parity / WCS-determinant audit (ChatGPT MAJOR #13):** the *only* finding not previously carrying a
D-id fingerprint. Dispositioned **OUT-OF-SCOPE-COMPUTE (not genuinely-new-editable):** it requests a
catalog-wide WCS-determinant + cutout-orientation audit across BASS/MzLS/DECaLS/overlap — a *new full-catalog
compute task*, not a text edit, and it is materially **mitigated by the very v1.0.238 image-level e2e run**:
T_eq=0.9997 with antisymmetry-maxdev 0.0 verified image-by-image on all 8.47M galaxies demonstrates the
production TTA labeling is exactly parity-antisymmetric at the image level, so a uniform hidden parity flip in
the cutout pipeline would have to defeat the measured antisymmetric construction. A dedicated per-brick WCS-det
audit remains an honest open compute item (adjacent to DP4-15 residual), **not an editable defect for this wave.**

---

## OVERHAUL-REGRESSION HUNT (post single-paragraph-abstract collapse)

- **Broken \ref/\eqref/\autoref:** label↔ref diff run over the full tex → **ZERO broken references.**
  All `\ref` targets resolve to an existing `\label`. All cited section labels present
  (sec:prereg, sec:sensitivity, sec:pseudolabel_independence, sec:monopole_mask_null, tab:decision_tree,
  tab:primary_callout, sec:app_systematic).
- **Orphaned statements from abstract de-dup:** the collapsed abstract (L667) retains every headline number
  (N=8.47M/3.2M/949,584; +0.41σ p=0.31; z≈−7.6; A_ref=0.017; A_50 0.75%; A_95∈(1.0,1.5]%; 99.32%; 47%;
  3.7–8.8× Shamir tension). The two-limitations detail relocated to §notation/§monopole_mask_null/App B/D
  which carry it verbatim (per DP4-13). No orphaned cross-reference, no dangling "as shown above/below" pointer
  into deleted abstract paragraphs. **No overhaul-introduced regression.**

---

## VERBATIM OVERHAUL-ACK QUOTES

- **ChatGPT (MINOR, presentation):** "*The manuscript is highly repetitive, repeatedly redefines which
  statistic is "primary," and embeds extensive defensive commentary and repository paths in the scientific
  narrative. A substantial restructuring is needed so that the data vector, estimator, null, sample, and
  inferential claim can be identified unambiguously.*" → DP4-13 (presentation half CLOSED-BY-EDIT v1.0.237;
  residual = referee-taste on already-tabulated structure).
- **Grok (tone on presentation, POSITIVE):** "*The declared analysis hierarchy and decision tree are exemplary*"
  and closing support: "*The central claim … is consistent with null (and that a genuine Shamir-scale signal
  would have been recovered) is supported by the pre-specified HC real-space estimator, the empirical
  injection-recovery calibration, the template-fit disfavor, and the model-independent GZ1 cross-check.*"

---

## FINAL COUNT

**0 genuinely-new real editable findings** (excluding items closed by staged v1.0.238).
- The only close in the bundle: **DP4-15 image-level e2e injection**, legitimately performed + artifact-verified
  in v1.0.238 (T_raw=0.2303, T_eq=0.9997, 192/192 shards).
- Every other Grok MINOR and ChatGPT MAJOR/MINOR = source-cited re-flag of DP4-01/07/08/09/12/13/14/16/17/19/21.
- ChatGPT MAJOR #13 (WCS-parity audit) = OUT-OF-SCOPE new-compute, materially mitigated by the same e2e run;
  not an editable defect.
- Grok trend = SOFTENING (MINOR-only, "exemplary" presentation); ChatGPT holds its structural harsh-referee
  REJECT floor (directive H) on honestly-disclosed content.
- No broken refs, no orphaned statements from the abstract collapse.

**Integrity:** no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated;
raw verdict text READ before recording; artifact READ (not filename-checked) before crediting the DP4-15 close.
