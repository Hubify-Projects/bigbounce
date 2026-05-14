# P4 v1.0.49 — Adversarial R-round (Statistical Methodology)

**Reviewer persona:** OpenAI GPT-5 — statistical methodology / numerical rigor.
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.49 (2026-05-13, "deferred-tasks closure"), 2,993 lines, 46 bibitems.
**Compared against:** v1.0.48 R-round-2 closures (8 BLOCKERs + 19 MAJORs); this is a fresh adversarial pass on the new v1.0.49 content and on residual methodology weaknesses untouched by tick 0.
**Output schema:** B (Blocker) / M (Major) / m (minor) / n (nit). Numbering is round-local.

---

## Headline counts

| Severity | Count |
|----------|-------|
| **B (Blocker)** | **1** |
| **M (Major)** | **5** |
| **m (minor)** | **9** |
| **n (nit)** | **6** |
| **Total** | **21** |

**Most concerning finding (single sentence):** the new v1.0.49 §IV.C "Empirical bound on rotation-correlated CW-fraction excursion" paragraph contains an arithmetically wrong "30× smaller than 9.5σ monopole magnitude" claim — the true ratio is **5.2×**, not 30×, and the load-bearing rotation-equivariance-systematic argument that backstops the dipole-null result is therefore quantitatively misstated by a factor of ~6.

**Round verdict:** v1.0.49 is materially stronger than v1.0.48 (Table III is now reproducible; the bin-flatness figure exists; rotation-TTA has an empirical proxy bound) but a NEW BLOCKER was introduced by the deferred-closure work itself, and one v1.0.48 MAJOR (the monopole-leakage interpretation in Table III) is **claimed-closed but unverified**. Net: **not clean**. Net readiness impact: **+0pp expected after closure of the new B and 2-3 of the M's**; if the B is closed cleanly without a regression, readiness should hold at 88% (the 99% cap remains in force per `feedback_readiness_oscillation.md`).

---

## B (Blocker) — 1 finding

### B-1. "30× smaller" arithmetic in §IV.C rotation-TTA empirical bound is wrong by ~6×

**Where:** lines ~639–671 in §IV.C "Empirical bound on rotation-correlated CW-fraction excursion" (new in v1.0.49).

**Verbatim claim from the paper (line ~662–664):**

> "The monopole offset is therefore not a rotation-equivariance artifact (the bound is **30× smaller** than the monopole itself), and the residual ~0.3% catalog-wide CW asymmetry must arise from non-rotational sources..."

**The arithmetic:**

- 9.5σ monopole magnitude (the offset from 0.5000) = **0.0026** in CW-fraction units (= 0.26%).
- Max bin-to-bin CW-fraction spread across the 4 b/a bins (from `wave_14_kk_ba_reconciliation_results.json`) = **0.0005** (= 0.05%).
- True ratio: 0.0026 / 0.0005 = **5.2×**, not 30×.

**For the "30× smaller" claim to be arithmetically correct,** the rotation-TTA spread would need to be ≤ 0.26%/30 ≈ **0.0087%** (i.e., 0.000087), which is ~6× smaller than the actually-reported 0.05% spread. The paper's own quoted numbers do not support its conclusion at the magnitude stated.

**Why this is a Blocker, not a Major:** This is the **load-bearing empirical backstop** for the new "rotation-TTA is not the cause of the monopole" closure inserted in v1.0.49 to discharge one of the 3 deferred R-round-2 items. The closure was meant to elevate rotation-equivariance-residual reasoning from speculation (which Mechanism 2 in §V.B candidates a candidate explanation for the monopole) to an empirically bounded conclusion. With the correct ratio of only **5.2×**, the rotation-equivariance residual could plausibly account for ~20% of the monopole magnitude (not <4% as the 30× claim would imply). The conclusion that the monopole is "not a rotation-equivariance artifact" is significantly weakened — rotation-equivariance is no longer ruled out as a sub-dominant contributor.

**Compounding concern:** the SSOT entry (status.md line ~5) describes this closure approvingly as "0.05% max bin-to-bin spread across 4 b/a regimes...providing a geometric proxy for in-plane rotation." The SSOT does not call out the arithmetic discrepancy with the paper text. This means both the paper and the canonical lab-internal status record carry the same erroneous "30× smaller" framing, untested.

**Fix required:**

1. Change "30× smaller than the monopole itself" → "5.2× smaller than the monopole itself" (or equivalent: "approximately five times smaller", "below 20% of the monopole magnitude") wherever it appears in §IV.C and any cross-reference.
2. Soften the conclusion: replace "must arise from non-rotational sources" with "the dominant contribution to the monopole offset is therefore not rotation-equivariance violation, but a sub-dominant rotation-equivariance contribution at the ≤20%-of-monopole level cannot be excluded by this proxy bound."
3. Cross-check whether any downstream claim in the v1.0.49 abstract, §V (Catalog~C residual mechanism enumeration), §VII.C (SpArcFiRe), or §IX (Conclusions) inherits the "rotation excluded as monopole source" framing; if so, soften consistently.
4. Update `project-context/SSOT/paper-4/status.md` to record the correction.

**Pushback path:** If the paper wishes to retain the "geometric proxy" framing but tighten the conclusion, the alternative is to compute a quantitative upper bound: with 4 bins and 0.0005 spread, the implied per-rotation-angle CW excursion at any single in-plane orientation is bounded by (binwise scatter / sqrt(N_orientations_per_bin)), which on the 785,859-galaxy edge-on subsample gives a much tighter pixel-level bound. This would salvage the spirit of the closure but with honest arithmetic. I do not recommend that route until the proxy validity is independently established (see m-3 below).

---

## M (Major) — 5 findings

### M-1. Table III "monopole leakage" interpretation: not verified, only asserted

**Where:** Table III (line ~1252–1300), footnote `^b`, and §V/§IX cross-references.

**The setup (clarifying the question the reviewer was tasked to verify):**

The table reports
- ℓ=1 single-mode post-MASTER: **−0.122σ** at n=5.55M analysis subsample (canonical primary, anchors the dipole-parity null).
- Five canonical-N bandpowers at ℓ_eff = 4, 9, 14, 19, 24: significances **+6.10σ, +2.23σ, +2.63σ, +2.23σ, +2.47σ**.
- Footnote `^b` attributes the +6.10σ at ℓ_eff=4 specifically to "the 9.5σ residual monopole (uniform across 7 equatorial coordinate slabs)...mode-coupling into low-ℓ bandpowers through the partial-sky mask kernel."

**Why this is a Major, not just a methodology nit:**

The interpretation that "+6.10σ at ℓ_eff=4 is monopole leakage" is the **only** thing standing between the table-as-presented and a reader concluding "there is a real ~6σ chirality signal in the ℓ=2–6 bandpower." It is the load-bearing physics interpretation of the table's most significant deviation from null. But the paper does not verify it numerically. Specifically:

(a) **The expected monopole leakage amplitude is not computed.** Standard mode-coupling theory predicts C_ℓ^pseudo leakage from a monopole a_00 ≠ 0 as approximately `|M_{ℓ,0}/M_{0,0}|² · |a_00|²`, where M_{ℓ,ℓ'} is the mask-coupling matrix at NSIDE=64 with f_sky=0.491. For a 0.26% monopole and a partial-sky mask, the expected ℓ_eff=4 leakage can be computed from the same NaMaster setup the paper already uses. It is not.

(b) **The +2.23σ — +2.63σ pattern at ℓ_eff = 9, 14, 19, 24 is unexplained.** Pure monopole leakage should fall off rapidly with ℓ (the mask-coupling matrix is heavily diagonal-dominant once you move away from low-ℓ); a single uniform ~+2.3σ tail across 5 disparate bandpowers is **not** the standard monopole-leakage signature. It looks more like a global ~+2σ residual that the post-MASTER null calibration is not fully capturing, which would be a calibration-of-the-null problem, not a monopole-leakage problem.

(c) **Joint χ²/dof = 161.2 / 38 = 4.24 is in the table.** Under the null hypothesis with a properly-calibrated covariance, χ²/dof should be ~1. **A χ²/dof of 4.24 corresponds to a >9σ joint rejection of the null** (Wilson-Hilferty z ≈ 9.3σ). The footnote's qualitative "dominated by mask-coupled monopole" line elides this: under the monopole-leakage hypothesis, the leakage prediction should be subtracted from each bandpower BEFORE the joint χ² is computed, and the residual χ²/dof after that subtraction is what tests null consistency. The paper does not do this subtraction. As stated, the table jointly rejects null at >9σ on the equivariant Catalog~C bandpowers — which would be a sensational result if not explained.

**The reading the paper invites is ambiguous:**

> Reading 1 (paper's apparent intent): "ℓ=1 single mode is null at −0.122σ; the rest of the table is contaminated by monopole leakage and should not be read as a parity-violation signal."

> Reading 2 (a hostile reviewer would extract): "After full MASTER deconvolution, Catalog~C still shows χ²/dof = 4.24 at >9σ joint rejection of null across ℓ_eff = 4–24. The paper's defense is that this is all monopole leakage, but the paper does not numerically verify that the leakage prediction matches the observed pattern."

**Fix:**

1. Compute the predicted monopole-leakage contribution to each bandpower from the existing NaMaster mask-coupling matrix. The arithmetic is ~10 lines of pymaster on the same H200 pod that ran the original deconvolution; output goes into a new `wave_14_pp_monopole_leakage_prediction.json`.
2. Add a sixth column to Table III: **"Predicted monopole leakage (σ)"**, showing what fraction of each row's significance the monopole leakage hypothesis actually explains.
3. If the prediction matches the observed pattern (e.g., predicts ~+6σ at ℓ_eff=4, ~+0.5σ at ℓ_eff=9, ~0σ at higher ℓ_eff), the +2.23σ tail is then unexplained and must be acknowledged as residual mask-coupling calibration uncertainty rather than monopole leakage.
4. Report the post-leakage-subtraction joint χ²/dof as the load-bearing null statistic instead of the raw 161.2/38.

**Pushback path:** If the canonical-N MASTER recompute at ℓ=1 specifically (the post-arXiv-submission TODO already on record as a deferred MAJOR) closes this row, that is the right gate. Until then, the +6.10σ bandpower must carry a "interpretation pending recompute" caveat in the table caption, not in a footnote.

### M-2. Joint χ²/dof = 4.24 framing is incomplete

**Where:** Table III last row.

The "Joint χ²/dof (38 bandpowers) — 161.2/38 = 4.24" entry is presented with the single-word interpretation "Dominated by mask-coupled monopole." For a paper claiming a null detection of parity violation at sub-percent sensitivity, the headline statistical statement of the multipole analysis cannot be a χ² that **rejects the null at >9σ**. The reader's eye lands on "4.24" and asks "if the null is right, why is the joint test rejecting it at p ≈ 10⁻¹⁶?"

The fix is the same as M-1 (compute the leakage-corrected χ²), but it is worth flagging as a separate finding because **even if the leakage interpretation is correct**, the paper still owes the reader the post-correction χ²/dof. A monopole-leakage-corrected χ²/dof ≈ 1.0 would close this. A monopole-leakage-corrected χ²/dof ≈ 2.0 would still be tension. The paper as written punts on this question.

### M-3. The rotation-TTA "geometric proxy" assumption is not validated

**Where:** §IV.C lines ~644–660, the new v1.0.49 paragraph.

**The argument:** Edge-on disks (b/a < 0.3) have their projected major axis sampled uniformly across all in-plane position angles by DESI Legacy footprint geometry; therefore CW-fraction variation across b/a bins is a proxy for in-plane rotation-equivariance violation.

**The problem:** This is a clever idea but it is asserted, not validated. Two specific concerns:

(a) **The b/a binning collapses inclination AND classifier-output correlations.** An edge-on galaxy classifier looks at the projected disk shape; CW vs CCW for an edge-on disk depends not just on rotation angle but on whether the projected arm winding is visible at all. The b/a < 0.3 subsample is exactly where the classifier is *least* informative about chirality — so finding 0.05% spread there could equally mean "rotation-TTA is well-corrected" OR "the classifier returns near-random labels in this regime, so rotation-correlated bias is washed out." These are not the same thing.

(b) **The "DESI Legacy footprint geometry samples 0–2π uniformly at the ≥10⁴-galaxy per-bin scale" claim is asserted in one sentence without verification.** The DESI Legacy footprint is *deeply* non-isotropic (BASS+MzLS / DECaLS / DES legs with different scan directions, depths, and seeing). Position-angle uniformity on the sky does not follow trivially from footprint coverage alone. A direct histogram of edge-on disk position angles in the relevant b/a bin against the survey footprint should be plotted, or a Kolmogorov-Smirnov / Rayleigh test against uniformity should be reported. Neither is.

**Fix:** Either (i) compute and report the position-angle Rayleigh-test p-value across the 785,859-galaxy edge-on subsample as a footnote, or (ii) downgrade the language from "load-bearing empirical bound" to "consistency check pending direct $D_4$-TTA validation, which remains the canonical test."

### M-4. Falsification criterion is not internally consistent with the paper's own sensitivity claim

**Where:** §IX conclusions, lines ~2707–2720, item 5 "Falsification criterion."

**The claim:** "If a future survey (e.g. LSST Y3) detects a chirality dipole in a ≥10⁷-galaxy sample with amplitude A ≥ 0.1% at >5σ post-equivariant-averaging and look-elsewhere-corrected significance, then the result of this paper is falsified."

**The problem:** the paper's own empirical sensitivity floor (50%-recovery, systematic-inclusive, under per-pixel-shuffle nulls) is **0.5%** on 3.2M spirals. Scaling 1/√N from 3.2M to 10⁷ spirals gives a factor of 0.566 improvement: 0.5% × 0.566 ≈ **0.28%** empirical floor. The statistical-only Fisher floor scales similarly: 0.2% × 0.566 ≈ **0.11%**.

So LSST Y3 with 10⁷ spirals can plausibly *detect at 5σ* a dipole of amplitude ~0.28%–0.55% under the empirical-floor regime, or ~0.11%–0.20% under the statistical-only regime. **A 0.1% detection at 5σ in 10⁷ galaxies sits at or below the statistical-only Fisher floor for that sample size and below the empirical-MC floor.** The falsification criterion as written is essentially unfalsifiable: it asks for a detection at LSST that LSST Y3 could not, on the paper's own arithmetic, actually achieve.

If the intent is "any detection at all above the LSST Y3 sensitivity floor would falsify us," the criterion should be re-stated as a tightened LSST-projected sensitivity (e.g., "A ≥ 0.2% at >5σ on a ≥10⁷-galaxy sample after equivariant averaging and look-elsewhere correction"), making the falsification gate match the actually-achievable LSST sensitivity.

**Fix:** Recompute the falsification amplitude threshold to match the LSST Y3 sensitivity floor that the paper's own scaling arguments imply. Either tighten to A ≥ 0.05%–0.1% AND state explicitly that this assumes the statistical-only Fisher regime (requiring an LSST-grade systematic mitigation strategy beyond what is in the current pipeline), or loosen to A ≥ 0.3%–0.5% to match the empirical-MC scaling. The current "0.1% at 5σ" sits in a gap between the two regimes.

### M-5. The "sub-percent sensitivity" title language is technically defensible but loose

**Where:** Title (line ~48–50), abstract first paragraph, throughout.

**The claim:** the title and headline framing read "A Null Detection of Large-Scale Parity Violation in Galaxy Morphology at Sub-Percent Sensitivity."

**The issue:** the user-facing empirical sensitivity floor (§IX conclusion item 1, §VI.J injection-recovery) is **0.5%** under systematic-inclusive 50%-recovery against per-pixel-shuffle nulls. The 0.2% Fisher statistical-only floor is explicitly framed (§VI.J, §IX) as a theoretical asymptote, not the user-facing sensitivity. So the paper's own loadbearing empirical sensitivity is **at** the sub-percent boundary, not comfortably inside it.

0.5% IS technically "sub-percent" (since 0.5 < 1.0), but for a reader, the natural reading of "sub-percent" is closer to "comfortably under 1%, in the 0.1%–0.5% regime." A reviewer who reads "sub-percent" expects to find a 0.1% or 0.2% empirical floor in the body and discovers 0.5% instead. The title language is *defensible* but a sharper alternative would more accurately telegraph what is delivered.

**Suggested fix:** "...A Null Detection of Large-Scale Parity Violation in Galaxy Morphology at the 0.5% Empirical Sensitivity Floor" or "...at Half-Percent Sensitivity" or "...at Sub-Percent Statistical Floor." The last is the most aggressive but matches the asterisked framing in the abstract.

**Pushback path:** if the title is locked for arXiv submission psychology reasons (Houston already approved current title), then keep the title and add one sentence in the abstract immediately after the headline-numbers paragraph: "We adopt the empirical 0.5% 50%-recovery floor as the user-facing sensitivity; the 0.2% Fisher statistical asymptote is reported as a theoretical bound, not as the recommended detection threshold."

---

## m (minor) — 9 findings

### m-1. Figure caption arithmetic for fig:binned_cw_fraction is slightly off

**Where:** §VI.J figure caption (lines ~2456–2473, new in v1.0.49).

Caption reads "fracdev $\Delta = 1.41\%$ (driven by the smallest-N fracdev bin at $n = 10{,}941$)". The 1.41% spread in CW fraction over a bin of n=10,941 implies the bin has Poisson SE = √(0.5 · 0.5 / 10941) ≈ 0.48%. A 1.41% spread is ~2.9σ on the bin's own Poisson scatter, which means the spread is **statistically significant**, not just "driven by small N." The framing "small-N drives the spread" understates what is actually a statistically-significant morphology-CW correlation at the high-fracdev end. Suggest: "driven by the high-fracdev tail (smallest-N bin $n = 10{,}941$, where the per-bin Poisson SE is ~0.48%); the spread is statistically significant at ~2.9σ on the bin's own scatter, consistent with the morphology-classification coupling discussed in §IV.D."

### m-2. Table III σ_null column unit/notation is dense; clarify

**Where:** Table III column 3 header "σ_null × 10⁶ (sr)".

The column is described in the caption as "the per-bin standard deviation of the MC null distribution at that bandpower." But for the ℓ=1 single-mode row, σ_null = 0.429 × 10⁻⁶ sr, and for ℓ_eff=4 (a 5-mode bandpower), σ_null = 0.804 × 10⁻⁶ sr. These are NOT computed the same way (single-mode vs 5-mode bandpower averaging changes the variance by √5). The caption should explicitly state that σ_null is per-bandpower-as-defined, not per-mode.

### m-3. The "single-mode ℓ=1" vs "5-mode bandpower" distinction is a footnote concern

**Where:** Table III first row caption + footnote `^a`.

Row 1 is labeled "ℓ=1 (single mode)" with n=5.55M analysis subsample and f_sky=0.659; rows 2-5 are 5-mode bandpowers on the canonical N=3.2M / f_sky=0.491 analysis. These use **different masks, different shot-noise normalizations, and different MC null counts** (500 for single-mode, 500 for bandpowers — but with different mode-coupling kernels). The paper acknowledges this in the caption ("differ only in the analysis mask and normalization, so agreement is expected but not numerically verified at the time of this release") and lists the recompute as a TODO. This is honest disclosure. But: a reader can also conclude that the dipole-parity headline result (−0.122σ) lives on a DIFFERENT analysis from the rest of the table that justifies it. This is the same observation as the v1.0.48 R-round-2 closure ("canonical-N MASTER recompute at ℓ=1 specifically remains the post-arXiv-submission TODO"). Restating it here so the v1.0.49 reader does not lose the gate. **Disposition:** retained from v1.0.48 R-round-2 as the one open MAJOR; no fix expected pre-arXiv-submission.

### m-4. McNemar Z=13.4 calculation is in the right ballpark but signed-vs-unsigned conventions blur

**Where:** §III.B "Independent GZ1 cross-match and joint label tabulation," lines ~960–966, and abstract para 3.

`(b-c)/√(b+c) = 2512/√35266 = 13.376σ` — confirmed numerically. The paper reports both McNemar χ² = 178.9 (= 13.376²) and signed Z = +13.4. **The convention "signed (uncorrected) two-sided Z" is non-standard.** McNemar's signed Z is one-sided by construction (the sign carries the direction of marginal-handedness disagreement); the two-sided p-value comes from |Z|. Calling it "two-sided Z" is technically correct as a notation but invites confusion with a two-sided z-statistic.

Suggested fix: rename "signed (uncorrected) two-sided Z" → "signed Z (one-sided convention; two-sided p-value from |Z|)" or just drop the parenthetical entirely.

### m-5. The "67.6% CE-ResNet pseudo-label pathway" attribution is causal-leaning, not strictly causal

**Where:** §III.B (line ~127, abstract); §IV.A and §VI.J cross-references.

The McNemar result indicates Catalog~C is 2.1pp LESS CW-leaning than GZ1 on the matched subset, opposite from the global +0.5% CW excess. The paper concludes this "rules out a simple GZ1 bias → direct propagation → Catalog~C residual attribution and instead points to the CE-ResNet pseudo-label pathway (67.6% of training labels) as the dominant bias-attribution channel."

This causal claim does follow from the sign reversal but assumes the only two possible attribution channels are "GZ1 direct" and "CE-ResNet pseudo-labels." A third channel — a residual ViT-S inductive bias not present in either training source — is not ruled out by the McNemar tabulation. The paper should soften "instead points to the CE-ResNet pseudo-label pathway as the dominant bias-attribution channel" → "is consistent with the CE-ResNet pseudo-label pathway being the dominant bias-attribution channel; a residual classifier-architecture inductive bias remains an alternative explanation that the joint tabulation does not distinguish."

### m-6. Recent literature: nothing from 2024–2026 except self-citations

The latest non-self citations are 2023 (Hou:2023, Cabass:2023, Eskilt:2023). Specific suggestions:

- **Philcox-Hou-Slepian 2024–2025 follow-ups** on parity-odd 4PCF — there have been ≥2 follow-up papers (Philcox 2024 EFT-of-LSS comparison; Hou+ 2024 systematic-budget treatment) that should be at least mentioned in §VIII.E.(ii) to keep the cosmology-translation paragraph current.
- **CMB-birefringence updates post-Eskilt 2023** — the LiteBIRD design paper and ACT DR6 EE/EB analyses have moved the constraint envelope; §VIII.E.(i) cites Eskilt:2023 + Komatsu:2022 but a one-line ACT DR6 reference would close this.
- **2024–2025 Galaxy Zoo / Walmsley follow-ups** — there is at least one Walmsley 2024 paper extending Galaxy Zoo DESI morphology to bar/no-bar substructure that is directly relevant to §VI.J bar-spiral discussion.

**Disposition:** not a Major because the standalone paper is self-contained and the cited literature is sufficient to support the paper's claims; flagged so Houston can decide whether the 2024–2026 update is in scope before arXiv submission.

### m-7. §VIII.E.(i) qualitative complementarity language is honest but could be sharper

**Where:** §VIII.E.(i), lines ~2520–2543, "Chiral gravitational-wave power asymmetry Π."

The paragraph (rewritten in v1.0.48 R-round-2 to drop the dropped numerical |Π| bound) reads as honest but vague: "the morphology channel and the CMB-birefringence channel are not directly numerically comparable in any common parameter, and we emphasize only that the two channels are *complementary*: a model can saturate one constraint while satisfying the other."

This is true. But "complementary" without further structure leaves the reader unsure whether the paper is claiming morphology adds independent constraining power, or just that it doesn't *contradict* CMB-birefringence. A one-sentence sharpening: "the morphology channel constrains the parity-violating tidal-torque coupling at the late-universe matter-distribution stage, while CMB birefringence constrains the axion-photon Chern-Simons coupling at recombination; the two probes test different sectors of the parity-violating EFT and a non-detection in one does not constrain the other."

### m-8. Some loose self-citation framing in §I

**Where:** §I introduction footnote (lines ~177–184) on the "four-paper companion program."

Reads "The chirality catalog is also the morphology channel of a four-paper companion program covering parity-violation observables (spin-torsion no-go theorems [P1A], SPHEREx f_NL forecast [P2], multi-survey anomaly catalog [P3]), but the present null dipole result and the catalog construction stand independent of those companions."

For standalone-arXiv submission, this footnote is the only mention of the program. Two improvements: (i) explicitly state that the cited companions are "in preparation, to be deposited on arXiv with cross-resolvable identifier" — currently this lives only in the bibitem entries (lines ~2924–2937), not in the main text where readers see it. (ii) Verify that arXiv submission of P4 alone with cross-references to "in preparation" companions is acceptable to arXiv astro-ph.CO/astro-ph.GA submission gates; some arXiv moderators flag uncrossable citations.

### m-9. The "axis-agnostic falsification" framing in §IX item 5 is correct but underexplained

**Where:** §IX conclusions item 5, line ~2714.

"The criterion is axis-agnostic: a cosmological parity-violation signal is not required to align with any previously-reported dipole axis, so the falsification condition is solely the amplitude × significance product."

This is statistically correct (no theoretical prior demands the LSST dipole align with Shamir's axis or with the present catalog's residual axis), but the framing invites a hostile reading: "the authors are pre-emptively immunizing against axis-coincidence skepticism." A cleaner version: "We do not require axis-alignment with any previous claim because a true cosmological signal at LSST scale would be measured to high precision in its own direction; cross-survey axis comparison becomes meaningful at >10σ, not at the 5σ falsification threshold."

---

## n (nit) — 6 findings

### n-1. The "uniform across 7 equatorial coordinate slabs" phrase is repeated 8+ times

Once defined in §VI.E (sky-region balance), the phrase is repeated verbatim across abstract, §V, §VI.B, §VI.J, and §IX. Suggest defining it once as "equatorial-slab uniform" or "ESU" the first time and using the shortened form thereafter; saves ~1 column-inch of text.

### n-2. Bin-flatness footnote at §IV.D (line ~2412) has stray text

Reads: "(HC-broad: $n{=}949{,}584$, $\max(p_{\rm CW,eq},p_{\rm CCW,eq},p_{\rm NS,eq}){>}0.6$ -- this is the broader cut that includes confident-NS galaxies, distinct from the spiral-only HC-spiral cut $n=471{,}049$ used in §IX.J for MC injection-recovery):"

The clarification is correct but the double-dash "--" inside a parenthetical reads as an injected editorial note from a prior revision. Suggest restructuring: drop the parenthetical clarification and add it as a separate sentence after the bin-flatness table, since the distinction is also made explicitly in §VI.J.

### n-3. Throughout, $\sigmaunit$ macro is sometimes spelled out as "σ" in the text body

E.g. line ~98 uses "$3\sigmaunit$" (macro) but line ~104 uses raw $\sigma$. Mostly consistent but a `grep -nE "\\\\sigma( |\\\\)|σ"` pass would catch the ~5 inconsistent uses.

### n-4. "9.5σ" appears as both "9.5σ" and "9.5 σ" (one space variant)

Style nit: the paper sometimes writes the σ flush to the number ("$9.5\sigmaunit$") and sometimes with a thinspace. Cosmetic; revtex4-2 style usually flush.

### n-5. The acknowledgments section is thin

§ Data Availability + acknowledgments could mention the McNemar tabulation tool / SpArcFiRe DR9 update / NaMaster development team. Adds two lines; community-goodwill.

### n-6. Some bibitems still use the inconsistent year-in-parens convention

E.g. Dosovitskiy:2020 bibitem reads "in *Proc. Int. Conf. Learning Representations (ICLR)* (2021)" — the bibkey says :2020 but the venue year is 2021 (ICLR conference for the 2020 arXiv submission). Cosmetic but a careful reviewer notices. Same pattern: Cahn:2021 bibkey vs published year 2023. These are venue-vs-arXiv year mismatches that revtex4-2 doesn't auto-resolve.

---

## Diff vs prior 2 R-rounds

This round is focused on **new v1.0.49 content** + **unverified v1.0.48 claims**. Findings B-1, M-1, M-2 (the central methodology gaps) are new to this round and were not flagged by either the v1.0.46→v1.0.47 5-agent review or the v1.0.47→v1.0.48 5-vendor R-round-2 review.

- The R-round-2 GPT-5 reviewer (2026-05-13 1052pt) flagged "Table III column relabel" (closed in v1.0.48) and "M_ℓℓ⁻¹ mode-coupling inversion language" (closed in v1.0.48) but did NOT check the **numerical reproducibility of the post-MASTER monopole-leakage attribution**. That gap is what M-1 closes here.
- The R-round-2 closure documentation in `project-context/SSOT/paper-4/status.md` mentions "0.05% max bin-to-bin spread across 4 b/a regimes" approvingly but does not check the **arithmetic of the "30× smaller" claim in the paper text**. That gap is what B-1 closes here.
- M-4 (falsification threshold internal consistency) is a new check enabled by the v1.0.48 R-round-2 conversion of "0.2% Fisher" → "0.5% empirical" — the LSST projection downstream was not updated to match.

Conclusion: tick 0 + R-round-2 did real work on the citations, confabulation, and headline framing. The methodology-rigor surface area is where new findings continue to land.

---

## Recommendations for closure path

**Pre-arXiv-submission (must close):**
- **B-1**: 1 line edit in §IV.C ("30× smaller" → "5.2× smaller") + SSOT update + downstream language sweep. ~15 min.
- **M-1**: pymaster monopole-leakage prediction recompute + Table III sixth column + post-correction χ²/dof. ~30 min on H200, ~1 hr writing time. **This is the single largest remaining methodology defensibility item.**
- **M-4**: recompute LSST Y3 falsification threshold to match scaling. ~5 min arithmetic, 2-sentence text edit.

**Post-arXiv-submission (defer with on-record acknowledgment):**
- M-2: dependent on M-1 closure.
- M-3: rotation-TTA proxy validation (position-angle Rayleigh test on 785K edge-on subsample). ~15 min compute.
- M-5: title sharpening (Houston call).
- m-6: 2024–2026 literature scan (Houston call).

**Cosmetic (next pass):**
- m-1 through m-9 + n-1 through n-6.

If B-1 + M-1 close cleanly, the paper is ready for arXiv submission at materially higher confidence than v1.0.48. If only B-1 closes (i.e., M-1's leakage-prediction recompute is deferred to post-submission), an arXiv referee with statistics rigor will flag M-1 essentially verbatim. Better to close it pre-submission.

---

**End of review.**

— GPT-5 (statistical-methodology), 2026-05-13 17:30 PDT
