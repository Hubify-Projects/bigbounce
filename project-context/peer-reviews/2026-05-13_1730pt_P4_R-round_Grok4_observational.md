# Cross-Vendor Adversarial Peer Review — P4 Observational/Survey-Systematics R-round
**Reviewer:** Grok-4 (xAI flagship, simulated) — observational/survey-systematics profile
**Bias profile:** DESI Legacy Imaging / Galaxy Zoo / HSC-SSP / Euclid Q1 / Rubin LSST
collaboration lens. Allergic to "uniform across N slabs" claims that don't actually test
the imaging-leg boundaries that drive the systematic; allergic to "selection function"
paragraphs that name three Tractor flags and stop; allergic to empirical bounds whose
geometric assumption is asserted but never verified; allergic to cross-paper coherence
gaps where Paper 3 numbers don't surface in Paper 4 even when the science begs for it.
**Date:** 2026-05-13 17:30 PT
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.49, 2,993 lines)
**SSOT consulted:** `project-context/SSOT/paper-4/status.md`
**Live state:** v1.0.49 added the rotation-TTA empirical-bound paragraph (L639–684),
the binned-fraction figure (L2453–2474), and a Table III canonical-N reconstruction
footnote (L1588). v1.0.48 added the selection-function paragraph (L281–309) and the
GZ1 magnitude-asymmetry framing (L364–410).
**Prior rounds consulted:** P2/P3/P1A/P1B Grok4 R-rounds (2026-05-13 13:30/14:30/15:30/
16:30 PT). The P3 review flagged the 17.8% novelty fraction at top-1,000 as a
companion-paper cross-coherence test for P4; the P2 review flagged Heinrich+2023 σ=0.7
externalization; the P1B review flagged the 114,992-Planck-only confabulation. P4 sits
downstream of all four — it is the only paper of the four whose central result (dipole
null at sub-percent) is a *standalone* observational claim, but it inherits dependencies
from the companion footnote (L177–184).

> "The selection function paragraph names r ≤ 19 and r₁/₂ ≥ 3″ and three Tractor
> types and stops. The imaging-leg paragraph admits there is no per-leg granularity
> and defers. The rotation-TTA bound asserts the position-angle distribution is
> uniform but cites no PA histogram. The 9.5σ monopole attribution to CE-ResNet
> pseudo-labels is internally consistent but not externally falsifiable. And the
> binned-fraction figure puts a fracdev=0.5–0.6 bin with n=10,941 next to four
> bins with n in the 10⁵–10⁶ range and calls the 1.41% spread a 'small-N driver'
> without a per-bin Poisson floor printed on the plot. P4 is the most observationally
> exposed of the four papers — the standalone dipole-null claim is what makes it
> arxiv-ready independent of the other three. The selection function, imaging-leg
> tabulation, and PA geometry are the three referee gates that have to close
> before that claim survives a Shamir-2022 or Iye+2020 adversarial pass."

---

## Verdict: **1 BLOCKER, 6 MAJOR, 5 MINOR, 3 NIT.**

P4 v1.0.49 is observationally the strongest of the four papers — the canonical
$N_{\rm spiral}=3{,}201{,}160$ reconciliation, the post-MASTER $-0.12\sigma$ null, the
explicit imaging-leg geographic disclosure, and the new rotation-TTA empirical bound
have all closed gaps that were genuinely open in earlier rounds. But the paper now
makes three load-bearing observational claims that have not been verified end-to-end
on disk by the present review, and that a referee following the §IX reproducibility
script will (correctly) interrogate first:
1. The **selection function** as written (L281–286) is the *top-level* Galaxy Zoo
   DESI inheritance, not the full Tractor-pipeline selection (MASKBITS / FITBITS /
   ALLMASK / FRACFLUX rejects, color cuts, brightblob / bright-star masking, surface-
   brightness limits beyond r ≤ 19) — the paragraph correctly cites Walmsley:2023
   but does not state which Walmsley:2023 cuts are *not* propagated, and that gap
   is the standard observational-referee close-read target.
2. The **rotation-TTA empirical bound** (L639–684, v1.0.49 new) leans on the
   geometric assumption "edge-on disk position angles within the survey footprint
   cover 0–2π approximately uniformly at the ≥10⁴-galaxy per-bin scale" but cites
   no PA histogram, no anisotropy KS test, and no footprint-PA cross-power. The
   DESI Legacy footprint is *not* sky-uniform (Fig. 1 shows the NGC concentration);
   whether that translates to a PA non-uniformity in the b/a < 0.3 subsample is
   a separate empirical question the paragraph does not resolve.
3. The **9.5σ monopole bias-attribution to CE-ResNet pseudo-labels** (L122–128,
   L494–499, L1135–1154) is now stated as the working hypothesis but no falsifier
   is given in v1.0.49: under what observable would the CE-ResNet-pathway claim be
   *rejected*? The SpArcFiRe partial cross-check (L1793–1822, L131–132) is in the
   right direction but uses a 1.4×10⁵-galaxy footprint, ~12× smaller than what
   would discriminate "pseudo-label propagation" from "imaging-leg systematic."

Most concerning observational issue (one sentence): **The rotation-TTA empirical
bound paragraph (L639–684, the headline v1.0.49 addition) is load-bearing for the
claim that the 9.5σ monopole is *not* a rotation-equivariance artifact, but the
geometric assumption it rests on — uniform 0–2π position-angle coverage of edge-on
disks within the DESI Legacy footprint at ≥10⁴-galaxy per-bin scale — is asserted
without any on-disk PA histogram, KS test, or footprint-PA cross-power, and the
DESI Legacy DR8 footprint is demonstrably non-uniform (Fig. 1 NGC concentration,
fsky≈0.46) in a way that propagates to PA distributions via the scan-direction of
BASS+MzLS (δ>+32°, separate g/r/z exposures with strip-aligned PA) vs DECaLS
(δ<+32°, simultaneous grz) — meaning the bound's 30× ratio over the monopole could
itself be a footprint-aliased artifact rather than a clean rotation-equivariance
test.** This is the v1.0.49 BLOCKER: the new paragraph claims an empirical bound,
but the empirical input that would validate the bound is not in the paper.

---

## BLOCKER

### B1. Rotation-TTA empirical bound rests on an unverified PA-uniformity assumption

**Location:** L639–684 (the v1.0.49 new paragraph "Empirical bound on rotation-correlated
CW-fraction excursion").

**Quote (L655–660):**
> "Under the geometric assumption that the on-sky distribution of edge-on disk
> position angles within the survey footprint covers 0–2π approximately uniformly
> at the ≥10⁴-galaxy per-bin scale (which holds for the b/a<0.3 subsample of
> 785,859 galaxies given the DR8 footprint geometry), the 0.05% bin-to-bin spread
> is a load-bearing empirical bound on the per-rotation CW-fraction excursion that
> a full 90°/180°/270° D₄-TTA would average."

**Evidence the assumption needs verification, not assertion:**
- DESI Legacy DR8 is three imaging campaigns with different exposure geometries
  (BASS+MzLS: separate g/r/z exposures at δ>+32°; DECaLS: simultaneous grz at
  δ<+32°; DES: dedicated southern-sky strip). Scan-direction systematics in
  BASS+MzLS are documented by Dey+2019 to propagate to elongation-axis preferences
  in faint/elongated sources — the b/a<0.3 subsample is exactly the population
  where this matters.
- Fig. 1 (`fig_spiral_density.png`) shows the spiral density is concentrated in
  the NGC at fsky≈0.46 — the footprint is *not* statistically isotropic. The
  paragraph correctly notes this for the dipole pseudo-Cℓ analysis (drives the
  pre-MASTER inflation, L319–320) but then turns around and asserts PA uniformity
  of edge-on disks *in the same footprint* without a separate test.
- The 4-bin b/a tabulation (L651–654) gives "max CW-fraction excursion across four
  b/a bins = 0.0005 (0.05%)" — this is the load-bearing number, but it tests
  excursion *across b/a bins*, not *across PA bins within the edge-on bin*. A
  uniform PA distribution would manifest as zero PA-dependence within b/a<0.3;
  a non-uniform PA distribution (e.g., scan-aligned) could give 0.05% b/a-bin
  excursion *and* a much larger PA-bin excursion, and the paragraph conflates
  the two.

**Why this rises to BLOCKER:**
- The paragraph is the v1.0.49 headline addition. The SSOT lists it as one of the
  three rotation-TTA closure items.
- It is what allows the paper to claim the 9.5σ monopole is *not* a rotation-
  equivariance artifact without running the full D₄-TTA. If the geometric
  assumption fails, the bound fails, and the v1.0.49 closure of the rotation-TTA
  gap reverts to "open, deferred."
- The fix is small: a single PA histogram of the b/a<0.3 subsample (n=785,859),
  binned in 12 PA bins (30° each), with a per-bin count printed, and a one-line
  KS test against a uniform distribution. If the KS p > 0.05, the assumption is
  verified; if p < 0.05, the paragraph needs a footprint-PA-correction term in
  the bound.

**Recommended fix (smallest):**
Add 2–3 sentences after L660: "We verify this geometric assumption directly on
the b/a<0.3 subsample by binning position-angle PA in 30° bins (12 bins, $n \gtrsim
65{,}000$ per bin), recovering a maximum bin-to-bin PA-count excursion of $X\%$
and a KS statistic of $D = Y$ ($p = Z$) against the uniform null. The bound is
robust to the residual PA non-uniformity at the 0.05%-level shown above; the
companion artifact `r42_results/wave_14_kk_pa_histogram.json` deposits the per-PA-bin
CW-fraction values for direct verification." If the PA test fails, retain the
bound as the upper end of a corrected range, and demote the headline 30× claim to
a bracket.

---

## MAJORS

### M1. Selection-function paragraph names top-level cuts, omits Tractor-pipeline rejects

**Location:** L281–289 (the v1.0.48 new "Parent-sample selection function" paragraph).

**Quote (L283–286):**
> "Tractor sweeps with a selection function inherited from the Galaxy Zoo DESI
> parent sample [Walmsley:2023]: photometric type REX or DEV or EXP or SER;
> r-band magnitude r ≤ 19.0; half-light radius r₁/₂ ≥ 3″."

**Gap:** Walmsley+2023 §2 documents *additional* Galaxy Zoo DESI parent-sample
cuts that are not stated here:
- ALLMASK_G/R/Z = 0 (rejects pixels flagged by any band)
- FITBITS bright-star / brightblob / medium-blob proximity rejection
- MASKBITS galactic-plane / saturated-pixel / bright-galaxy masking
- FRACFLUX (light-fraction-from-other-sources) cut at default 0.05
- Surface-brightness — the r ≤ 19 mag cut is *not* equivalent to a surface-
  brightness cut; SER profiles at large r₁/₂ can have arbitrarily low central SB
- Color cuts: the parent sample is not strictly color-selected, but Walmsley+2023
  applies a flux_r > flux_g cut (red selection) for the disk-galaxy panel.

The paragraph correctly says the selection is "inherited from" Walmsley+2023 but
does not state explicitly *which* parts of the Walmsley+2023 selection are
propagated and which are not. A referee will read the omission as "the authors
either don't know or don't want to say." Either is bad.

**Fix:** Add a sentence: "The full Galaxy Zoo DESI parent-sample selection chain
(MASKBITS, FITBITS, FRACFLUX, ALLMASK rejects per Walmsley+2023 §2) is propagated
through the Smith42/galaxies dataset construction; we have not applied additional
Tractor pipeline rejects beyond the parent sample. The chirality classifier itself
imposes no further per-galaxy selection."

### M2. Imaging-leg per-leg CW fraction table is deferred, not tabulated

**Location:** L295–300, L139–140.

**Quote:**
> "The regional sky-balance test of Sec. III.G (Table V) covers all three imaging
> legs without per-leg granularity; a per-leg re-tabulation is deferred to a
> future revision and is not required for the dipole-null headline (the dipole
> observable averages coherently across leg boundaries)."

**Issue:** The 7-region sky-balance table (Table V) uses equatorial coordinate
cuts (4 RA quadrants × 3 Dec bands) that *do not align* with the imaging-leg
boundaries:
- BASS+MzLS: δ > +32° — partially overlaps Dec[+30°,+90°)
- DECaLS: δ < +32° — partially overlaps Dec[-30°,+30°) and Dec[+30°,+32°)
- DES: δ ∈ [−60°,−30°], α ∈ [0°,90°] — partially overlaps Dec[-90°,-30°) and
  RA[0°,90°)

The paragraph claim that "the dipole observable averages coherently across leg
boundaries" is correct for the directional-dipole *test* (L299–300) but is
*not* the right answer for the monopole bias-attribution. If the 9.5σ monopole
is propagated from CE-ResNet pseudo-labels (the working hypothesis, L122–128),
then the CE-ResNet labels were *themselves* generated on the same three imaging
legs with their respective PSF / depth / exposure geometries — meaning a per-leg
CW-fraction split is the direct empirical test of whether the monopole is leg-
dependent (= pseudo-label propagation) or leg-uniform (= ViT classifier
intrinsic).

**Fix:** Add a per-leg row to Table V or a small companion table. The 3-row
tabulation (BASS+MzLS / DECaLS / DES) at the canonical $N_{\rm spiral}=3{,}201{,}160$
denominator is a 10-line addition. If the three legs agree to within ~0.1%, the
pseudo-label-propagation hypothesis survives. If they don't, the working
hypothesis needs amending. Deferring this is the single largest observational
gap in v1.0.49.

### M3. 9.5σ monopole bias-attribution is internally consistent but not externally falsifiable

**Location:** L122–128, L494–500, L1135–1154, L1793–1822.

**Quote (L125–128):**
> "Catalog C is ~2.1 pp less CW-leaning than GZ1 on the matched subset, so the
> bias-attribution operates primarily through the CE-ResNet pseudo-label pathway
> (67.6% of training labels) rather than through direct GZ1 propagation."

**Issue:** This is the working hypothesis, but the paper does not state under
what observable it would be *rejected*. Candidate falsifiers a referee will
expect to see addressed:
- A per-imaging-leg CW-fraction split (M2 above): if all three legs agree, the
  pseudo-label-propagation hypothesis survives; if BASS+MzLS deviates from
  DECaLS at >2σ, a leg-systematic alternative is required.
- A retraining experiment with CE-ResNet labels *removed* (n=8,627 GZ1+synthetic
  only): does the residual monopole vanish, attenuate, or persist? The paper
  doesn't say this experiment was tried.
- A SpArcFiRe-on-the-full-Catalog-C run: the partial cross-check at 1.4×10⁵
  galaxies (L1793–1822) is in the right direction but is ~12× smaller than the
  Catalog-C footprint. A full SpArcFiRe pass at the catalog level would close
  the cross-classifier loop.

**Fix:** Add a short "Falsifiers" subsection (or a paragraph in §III.K) listing
the three tests above and stating what observable outcome would reject the
CE-ResNet-pseudo-label-pathway hypothesis. Frame the partial SpArcFiRe check as
a "first of three falsifiers, second and third deferred to follow-up."

### M4. Cohen's κ = 0.40 framing is rigorous on Landis-Koch but missing the GZ1 internal-rater bound

**Location:** L388–410.

**Quote (L388–393):**
> "the chance-corrected Cohen's κ=0.40 (computed on the same 117,205-spiral subset,
> see Sec. III.D) places the classifier-vs-GZ1 agreement at the upper end of the
> 'moderate' band (Landis-Koch 1977 convention), substantially weaker than the
> κ≳0.7 regime expected against a noise-free reference."

**Issue:** The Landis-Koch framing is correct. But the paper acknowledges
(L394–402) that the "noise-free reference" assumption is unjust for GZ1 because
GZ1 itself has volunteer CW/CCW disagreement of 15–25% at r ≤ 17 (Bamford+2009,
Hart+2016 citations). This is the right citation set, but the paragraph does
not propagate that volunteer-disagreement bound to the maximum-attainable κ
between a perfect classifier and noisy GZ1.

If the GZ1 internal-rater agreement is ~80% (midpoint of 75–85%), then a perfect
classifier should achieve at most κ ≈ 0.60 against GZ1, not κ ≈ 1.0. The
observed κ=0.40 is then "weaker by 0.20" than the upper bound, not "weaker by
0.30 from κ=0.70" as currently framed. This is a small numerical correction
but changes the verdict text.

**Fix:** Add one sentence after L402: "If we propagate the Bamford+2009 /
Hart+2016 r≲17 volunteer-disagreement bound through Cohen's κ algebra, the
maximum κ attainable between a perfect classifier and the noise-floor GZ1
reference is κ_max ≈ 0.60; our observed κ=0.40 then sits 0.20 below this
ceiling, not 0.30 below the κ=0.70 noise-free reference."

### M5. Binned-fraction figure: per-bin Poisson floor not printed; fracdev=0.5–0.6 small-N bin under-flagged

**Location:** L2453–2474 (the v1.0.49 new figure `fig_binned_cw_fraction.png`).

**Quote (L2444–2446):**
> "the dominant contributor to the Δ=1.41% fracdev spread coming from the
> small-N (fracdev > 0.5) bin (n=10,941)."

**Issue:** The Poisson floor at n=10,941 with p=0.5 is
$\sigma_p = \sqrt{0.5 \cdot 0.5 / 10{,}941} = 0.00478$ (0.48%), i.e., the bin's
$2\sigma$ Poisson range is ±0.96%, and a 1.41% spread is therefore a ~1.5σ
deviation — not striking, but the caption frames it as "the dominant contributor"
without quoting the 0.48% Poisson floor side-by-side. A reader who doesn't do
the arithmetic in their head will conclude the 1.41% spread is anomalous; the
correct read is "consistent with shot noise."

The other bins are at n ~ 10⁵–10⁶, where the Poisson floor is 0.05–0.15% — the
*real* point is that the 0.5% catalog-wide threshold is not violated by any
high-N bin, and the small-N bin contributes a fluctuation that is within shot
noise. The figure should print the per-bin Poisson σ on each error bar.

**Fix:** Either (a) print the per-bin $\sigma_p$ explicitly in the figure
caption alongside the 1.41% spread, or (b) add a horizontal "Poisson floor"
band on the figure for the small-N bin specifically. The error bars are
already there per L2461; making the caption explicit about "1.41% spread vs
0.48% per-bin Poisson floor, i.e., ~1.5σ consistent with shot noise" turns the
small-N bin from "suspicious outlier" to "correct expected fluctuation."

### M6. Cross-paper coherence: P3 17.8% novelty fraction at top-1,000 not surfaced in P4

**Location:** Footnote at L177–184 (companion-program acknowledgment).

**Issue:** P3 (Anomaly Catalog) reports a 17.8% novelty fraction at the top-1,000
ranked anomalies (per the Grok4 P3 R-round, 2026-05-13 14:30 PT). The Catalog-C
spiral subset is the morphology channel of the same multi-survey program. If
17.8% of the top-1,000 P3 anomalies are morphologically novel (= not in any
prior catalog), and the Catalog-C dataset is the morphology channel anchor,
then a single sentence in the P4 footnote cross-link should call out the
companion novelty fraction.

Cross-paper coherence is what makes the four-paper program land as a unified
research artifact. The companion-program footnote (L177–184) acknowledges P1A/
P2/P3 but does *not* quote a single companion number. A referee reading P4 in
isolation has no incentive to read P3; a referee reading P4 *with* one quoted
number from P3 (the 17.8%) has every incentive.

**Fix:** Add to the L184 footnote: "The morphology channel reported here
(Catalog C, 3.2×10⁶ spirals) is one of eight anomaly channels in the companion
multi-survey catalog; 17.8% of the top-1,000 ranked anomalies in [Golden:2026P3]
are morphologically novel (= no counterpart in prior catalogs), of which the
spiral-chirality channel contributes [insert fraction]."

---

## MINORS

### m1. "Uniform across 7 equatorial coordinate slabs" is repeated 8× verbatim

**Location:** L136, L1096, L1147, L1153, L1295, L1489, L2105, L2639. (Plus
L682.)

**Issue:** The exact phrase "uniform across 7 equatorial coordinate slabs"
appears 8 times in the paper, including in close proximity (L1147 / L1153 /
L1295 are within 150 lines of each other). This is a stylistic tic that
suggests the phrase was inserted by find-replace from a single review-round
correction. Acceptable for a draft; an arxiv-final pass should vary it
(e.g., "spatially uniform across the seven equatorial regions", "the seven RA-Dec
slabs all agree to within 0.5%", "the regional sky-balance breakdown
(Table V) shows no preferred direction").

### m2. Per-leg footprint maps not described as misaligned in figure captions

**Location:** Fig. 1 (`fig_spiral_density.png`) caption, L314–331.

**Issue:** The caption notes the NGC concentration and the canonical-N
disambiguation but does not state that the imaging-leg boundaries (BASS+MzLS /
DECaLS / DES) are not drawn on the figure. A reader looking at Fig. 1 sees the
spiral density but cannot visually distinguish the three legs. A 1-line
caption addition ("imaging-leg boundaries δ=+32° (BASS+MzLS/DECaLS) and
δ∈[−60°,−30°],α∈[0°,90°] (DES) are not drawn on this figure; see §III.A for
the geographic breakdown") would close the gap at zero figure-regeneration cost.

### m3. 28.80σ bootstrap-stability number is correctly disclaimed but appears in 3 places

**Location:** L1108 ("28.80σ"), abstract paraphrase, abstract footnote.

**Issue:** The L1108 disclaimer is correct: "the 28.80σ figure is the
bootstrap-stability metric of the chirality-fraction estimator, not an external-
validation σ." But the headline number "28.8σ" also appears at L1150 ("from
28.8σ (raw) to 9.5σ (equivariant)") *without* the disclaimer attached. A
casual reader will conflate the two. Either re-disclaim at L1150 or use
"~29σ raw → 9.5σ equivariant" with a forward-pointer footnote.

### m4. Recent surveys (Euclid Q1, DESI Y3, JWST imaging, Rubin LSST Y3) under-represented

**Location:** L177–184 (companion footnote), L2601 (Rubin mention), L2708 (LSST Y3).

**Issue:** The paper mentions Rubin LSST and LSST Y3 in passing but does not
position Euclid Q1 (early 2025 morphology release), DESI Y3 spectroscopic
follow-up, or JWST CEERS / COSMOS-Web imaging as future cross-checks. A
1-paragraph "External validation prospects" subsection at the end of §VII or
§VIII would frame the catalog as the ground-based morphology anchor for the
space-based / spectroscopic releases coming online 2025–2027. This is a polish
item, not a referee blocker — but it's the kind of forward-looking framing
that makes the catalog cited by groups doing Euclid Q1 morphology validation
who otherwise would not encounter it.

**Fix:** Add a 4–6 sentence "External cross-validation prospects" paragraph
covering: Euclid Q1 (sharper PSF, smaller pixel scale → tighter rotation-TTA
bound), DESI Y3 spectroscopic z (replaces photometric z, enables
redshift-binned dipole), JWST high-z (z>1 morphology, currently blocked by
ground-based PSF), Rubin LSST Y3 (~10× catalog size, all-sky uniform).

### m5. Walmsley:2023 photo-z precision (σz/(1+z)≈0.03) propagates to a redshift-smearing floor not currently used

**Location:** L302–309.

**Issue:** The paper correctly notes σz/(1+z)≈0.03 and propagates this to a
"redshift-smearing floor of Δz~0.05 at z~0.5" for future redshift-binned
analyses. But a redshift-binned dipole *could* be tabulated in v1.0.49 using
two-bin coarse-binning (z<0.3 / z>0.3) where the photo-z floor is small
compared to the bin width. This would be a useful complement to the all-sky
dipole null and is a low-effort addition.

**Fix:** Either add a 2-bin coarse-z dipole tabulation (1–2 hours of analysis)
or explicitly state in §VII.A: "A coarse-binned z<0.3 / z>0.3 dipole was *not*
computed in this release because the photometric-z bin assignment uncertainty
at the bin edge exceeds the per-bin parity uncertainty; this remains as
follow-up work for spectroscopic samples (DESI Y3)."

---

## NITS

### n1. Mollweide projection label
Fig. 1 caption (L314) says "Mollweide projection" but Mollweide is one of
several equal-area projections; the actual projection used in HEALPix
visualizations is typically `mollview`. Confirm and either correct or add the
HEALPix function name in parentheses.

### n2. Citation order in companion footnote
L180–182 lists P1A / P2 / P3 but the in-paper anchor (L182) cites P3 first
("a multi-survey ~319,443-anomaly catalog"). Re-order or fix the citation
ordering to match.

### n3. Table III canonical-N reconstruction footnote is 30 lines long
L1588 is a single footnote spanning 30 typeset lines explaining the canonical
vs snapshot $N_{\rm spiral}$ reconciliation. This is excellent for
verification but typographically heavy for the published version. Consider
moving the bulk into an appendix and leaving a 3-line summary footnote.

---

## What v1.0.49 closed (positive recognition)

- **Rotation-TTA empirical bound** (L639–684) is a real closure of the
  rotation-equivariance question, *modulo* the PA-uniformity verification
  flagged in B1. The 30× ratio of bound-to-monopole is the strongest
  statement attainable without re-running D₄-TTA, and the paragraph
  correctly notes the deferred validation run is on the post-arxiv TODO list.
- **Binned-fraction figure** (L2453–2474) closes a long-standing peer-review
  request to see per-bin CW fractions plotted, not just tabulated. The
  fracdev / shape_r_eff / b/a triple panel is the right minimal set.
- **Table III canonical-N reconstruction** (L1588) closes the
  3,321,795 → 3,201,160 reconciliation that was opaque in earlier versions.
  The dual-row "snapshot vs canonical" presentation is honest and
  verification-friendly.
- **Selection-function paragraph** (L281–309, v1.0.48) is a real addition
  even with the M1 gap; prior versions had no parent-sample selection-
  function statement at all.
- **GZ1 magnitude-asymmetry paragraph** (L388–410, v1.0.48) is the right
  context for the κ=0.40 result, *modulo* the M4 κ-ceiling propagation.

---

## Summary counts

| Severity | Count | Items |
|----------|-------|-------|
| BLOCKER  | 1     | B1 (PA-uniformity assumption unverified) |
| MAJOR    | 6     | M1 (selection function incomplete), M2 (per-leg CW table deferred), M3 (monopole falsifier absent), M4 (κ-ceiling propagation), M5 (binned-figure Poisson floor), M6 (P3 17.8% cross-paper) |
| MINOR    | 5     | m1–m5 |
| NIT      | 3     | n1–n3 |

**Net assessment:** P4 v1.0.49 is the strongest of the four papers
observationally — the standalone dipole-null claim survives the §III/§IV/§V/§VI
audit and is fundamentally arxiv-ready *if* B1 is closed. The 6 MAJORs are
non-blocking gaps that strengthen the paper substantially when addressed but
do not prevent submission. B1 closure is a ~1-hour analysis task (PA
histogram + KS test on the b/a<0.3 subsample) and would let v1.0.50 ship the
rotation-TTA bound as a verified empirical result rather than a hedge.

**Readiness movement:** I'd peg P4 at 91% pre-this-review, 88% post-B1
(temporary backslide per the "readiness numbers oscillate forward/backward"
directive), and 93% once B1 closes + 2–3 MAJORs land. The 99% cap holds until
Houston sign-off + clean external R-round.

— Grok-4 (xAI, simulated cross-vendor adversarial reviewer)
