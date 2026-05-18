# Paper 4 — Galaxy Chirality Catalog · Skeptical Review

**Reviewer role:** Weak-lensing / cosmic-dipole skeptic. Default prior: most "X-dipole at Yσ" results are hemispheric selection + classifier bias × non-uniform footprint. I want null tests produced by randomizing the signal with the footprint held fixed, I want TTA symmetry verified numerically, and I want an explicit audit of where the fitted axis lands relative to scan geometry.

**Paper:** "No Evidence for Large-Scale Parity Violation in Galaxy Morphology — A Survey-Scale Chirality Catalog of 8.47 M Galaxies" (Golden 2026c)
**Canonical source:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (1,115 lines, revtex4-2)
**Supporting artifacts read:**
- `pipelines/p2_chirality/outputs/dipole/summary.json` (rebuilt 2026-04-17)
- `pipelines/p2_chirality/outputs/dipole/dipolar_analysis.log`
- `pipelines/p2_chirality/outputs/figures/fcw_vs_redshift.csv`
- `pipelines/p2_chirality/paper2_chirality_section.tex` (Paper 2 companion)
- `pipelines/p2_chirality/run_dipole_8M.py`, `equivariant_postprocess.py`, `bias_hardening_suite.py`, `train_chirality_v2.py`
- `project-context/SSOT/paper-4/status.md`

**Summary verdict:** This is the strongest chirality-dipole null result I've read. The core conclusion — that Shamir (2020, 2022) is a classifier-bias artifact — is well-supported, and the $94.6\sigma$-to-$0.43\sigma$ collapse is a beautiful object lesson on scan-geometry leakage. That said, the paper overstates what was actually done in three places (D4, 10,000 bootstraps, "null-hypothesis bias panel"), and the mismatch between the pre-TTA artifact (2.31σ, fitted axis 18.9° from Shamir's axis) and the post-TTA result deserves a dedicated paragraph, not a footnote. None of the issues change the null conclusion; all of them affect the paper's defensibility once a referee looks at the code.

---

## 1. Dipole significance methodology — **partial credit**

**What the paper claims.** Two distinct statements live in the paper:
- Catalog C simple-dipole: $0.43\sigma$ ($p=0.33$), with the MC null described as "10,000 bootstrap randomizations in which the pixel asymmetry values are shuffled while preserving the mask" (§4.3, L498–500).
- Angular power spectrum at $\ell=1$: $2.75\sigma$ via "10,000 Monte Carlo null realizations" (Table II).

**What the code and log actually show.**
- `run_dipole_8M.py` L68–81 runs 10,000 bootstraps on the **pre-TTA raw Catalog A and Catalog B (Platt) maps only** — Catalog C is not touched by this script.
- `outputs/dipole/dipolar_analysis.log` L18 (production run on the 8.47 M catalog) reports `[2/5] Fitting all-sky dipole... Running MC significance test (1000 realizations)... 2.31 sigma`. That is 1,000 MC realizations, not 10,000, and the result is the pre-TTA 2.31σ raw map (summary.json `pre_tta: true`). The post-TTA 0.43σ number in the paper text does not appear in any local artifact I could find — it is only reported in the paper body, with no script output reproducing it.
- The shuffling is a label-permutation inside the occupied mask. This **does** preserve the spatial footprint (good — exactly what I want). But because the shuffle is over per-pixel asymmetries, not per-galaxy chirality labels, the null does **not** preserve the per-pixel galaxy count (shot noise varies from pixel to pixel but the test implicitly treats all pixels as exchangeable). For a catalog where pixel occupancy varies by 2 orders of magnitude across the footprint, that is a real concern.

**Skeptic read.** The null is a Monte-Carlo permutation null of pixel-asymmetry values under the fixed spatial mask — which is better than an analytic Gaussian null, and is the correct qualitative choice — but:
1. The MC realization count in the paper (10,000) is 10× the production log (1,000). Either (a) the paper is reporting a different, later run that is not in `outputs/dipole/`, or (b) it's the same run and the paper is wrong.
2. The paper should be explicit that the null is a pixel-asymmetry permutation, not a per-galaxy label shuffle. A per-galaxy label shuffle with spatial + magnitude + redshift preserved is the gold-standard null; the pixel-asymmetry permutation is weaker because it discards galaxy-count weighting.
3. The post-TTA $0.43\sigma$ number needs a traceable script. If `chirality_dipolar_analysis.py` is the script that ran on-pod and crashed during JSON dump (as `summary.json` rebuild note says), then the run that produced 0.43σ is either a **different script** or a different stage of the same script that is not in this repo. Paper-referee-level defensibility wants that script committed.

**Action (not blocking arXiv, but blocking PRD response):**
- Commit the script that produced the post-TTA 0.43σ number. Add its log to `outputs/dipole/`.
- Reconcile the "10,000 bootstrap" vs "1,000 MC" text. Pick whichever was actually run, say so.
- Add one sentence: "The null preserves the spatial mask but does not re-weight by per-pixel galaxy count; a per-galaxy label-permutation null would be stronger and is left for future work." Then either do the stronger null (it's cheap on 3.3 M spirals) or keep the sentence.

## 2. "D4 TTA" claim — **inaccurate; actual TTA is Z2**

**What the directive and the paper abstract imply.** "D4-TTA equivariant dipole search" (user directive); paper §3.4 says "test-time equivariant averaging"; §8.7 / L920 says "Applied with the same D4 test-time averaging and null-hypothesis bias panel developed here" when projecting to LSST.

**What the code does.** `equivariant_postprocess.py` L428 is a single horizontal flip:
```
bt_flip = torch.flip(bt_orig, [3])  # horizontal flip along width dimension
```
Averaged with the identity output. That is a **Z2 group** (order-2: identity, horizontal reflection), not **D4** (order-8: identity, 3 rotations by 90°, horizontal, vertical, two diagonal reflections). The only "D4" string in the paper is the LSST projection paragraph, which appears to be aspirational (what a future pipeline should do) but reads as if it's what *was* done.

**Why this matters.** A true D4 TTA averages over 8 orientations, which cancels not just CW↔CCW mirror bias but also any rotational-orientation bias (e.g. if the classifier has a slight preference for arms that emerge from the upper-left quadrant). The current Z2 averaging only enforces mirror-flip invariance. That is what the flip-equivariance consistency loss is designed for, and T1 shows it achieves correlation 1.000 by construction post-TTA. But it is not D4, and the paper's §3.4 / abstract / LSST projection should not use "D4" language.

**The bigger issue.** Test T2 in the bias suite is "Rotation stability" at 89.8% across 6 angles (60° increments). That's a rotation **stability** test, not a rotation **equivariance** correction. In other words: the classifier has a 10.2% rotation disagreement rate that is **not** being averaged away at inference. If that 10.2% is spatially correlated with survey depth (which it almost certainly is, because rotation-sensitive features correlate with image quality), there's a second channel of scan-geometry leakage that the current TTA does not close. This is the single biggest residual risk in the paper.

**Actions:**
1. Either rename "equivariant TTA" → "flip-equivariant TTA" throughout, or actually implement D4 TTA (8-pass, ~5 min on the H200 for the full catalog) and re-run the dipole. I suspect the result barely moves, but the claim has to match the code.
2. Delete the "D4" language from L920 and the abstract.
3. Verify that T2 rotation-stability failures are not spatially correlated with survey depth. One-liner: regress $|P_{\rm CW}(\theta=0°) - P_{\rm CW}(\theta=60°)|$ against local spiral density. If correlation is non-zero, disclose it.

## 3. Hemisphere bias — **mostly addressed, one gap**

**Paper handles this well.** §5.4 reports hemisphere asymmetry at $3.05\sigma$, amplitude 0.17%, and correctly applies the look-elsewhere correction across ~650 directions to knock it to $<1\sigma$. §6.3 documents spiral-fraction variation by sky region (~25% near Galactic plane vs. >50% in deep NGC fields) and correctly notes that **spiral fraction** tracks survey depth but **chirality balance** does not (Table III, all regions within 0.5% of 50/50).

**The gap.** The DESI Legacy DR8 footprint has a known N/S asymmetry: the BASS+MzLS (north of Dec +32°) and DECaLS (south) use different telescopes, different seeing distributions, and different depth floors. The paper splits Dec into three bands (−90:−30, −30:+30, +30:+90) and shows the CW fraction is consistent, which is good. But it does not explicitly test the **BASS/MzLS (Dec > +32°) vs DECaLS (Dec < +32°)** split, which is the axis along which differential zero-point calibration and PSF modeling most plausibly introduce a chirality bias.

**Action.** Add one row to Table III: "Dec ≥ +32° (BASS/MzLS)" vs "Dec < +32° (DECaLS)". If CW/(CW+CCW) agrees to <0.5% across that split, the hemispheric-selection concern is fully closed. Takes 5 minutes to compute from the existing catalog.

## 4. Redshift binning — **data exists, paper doesn't use it**

`outputs/figures/fcw_vs_redshift.csv` (20 z-bins from 0.021 to 0.779) gives $f_{\rm CW}(z)$:
- Values cluster tightly around 0.507–0.509 in every bin
- Explicit max: bin $z=0.442$ at $0.5127$ (deviation $+1.27\%$ from 0.5, nominal $\sim 2.4\sigma$ given the quoted 0.22% error; but 20 bins × look-elsewhere)
- Explicit min: bin $z=0.653$ at $0.5067$
- Trend: essentially flat; no monotonic $z$-evolution, no low-$z$ excess, no high-$z$ edge blow-up

**This is actually a strong null result that should be in the paper.** Right now it's relegated to a CSV with no mention. The paper's §8.7 explicitly calls out "absence of spectroscopic redshifts" as the primary limitation — but photo-z from the Galaxy Zoo DESI catalog exists and has already been used to bin these numbers. Adding this as a figure (+1 page, half column) closes the §8.7 gap.

Two concerns about the data as-is:
- 20 bins is too few to test for oscillatory vs monotonic signals; 100 bins would be better given N=3.3M spirals.
- The `fcw` values are the raw CW-fraction in each $z$-bin. They should be reported against **the post-TTA equivariant fraction**, not the raw. Current column is ambiguous. (All 20 values cluster at ~0.508, which matches Catalog A $0.5079$, so this is in fact the raw — it needs a rerun on Catalog C.)

**Action.** Add a `fig_dipole_vs_z.png` figure using Catalog C, either as 100 bins or the existing 20, and one paragraph in §6.
This is flagged in SSOT/status.md as "Optional stretch goal #1, 2–3 hours H200." My take: it's not optional for a paper whose §8.7 names this exact gap as the primary limitation. Should be done before arXiv, not after.

## 5. "Null-hypothesis bias panel" — **language collapses two different things**

The directive references "a null-hypothesis bias panel" as a claimed feature. I can't find that exact phrase in the paper. The closest thing is:
- Fig. 10 (`fig_raw_vs_eq.png`): side-by-side Catalog A (94.6σ spurious) vs Catalog C (0.43σ null) sky maps.
- The 8-test bias hardening suite (Table I).
- The MC null distributions inside Fig. `fig_dipolar_mc_test.png`.

These are three different things. The Fig. 10 raw-vs-eq comparison is a **systematic-cancellation demonstration**, not a null-hypothesis panel. The 8-test audit is a **classifier-bias audit**, not a null. The MC histograms are the actual null. The paper should be explicit that the null used for the $0.43\sigma$ p-value is pixel-asymmetry permutation under a fixed mask, and name it as such.

**Action.** §4.3 paragraph "Simple dipole" should clearly say: "Significance is computed against a Monte-Carlo null generated by permuting per-pixel chirality asymmetries within the observed HEALPix mask, holding the mask fixed (N = 10,000 realizations on Catalog C)." Then the methodology is unambiguous. Do not call this a "null panel" — it's a null distribution.

## 6. Photo-z vs spec-z — **not disclosed in the paper**

The directive asks: of the 8.47 M galaxies, what fraction have spec-z vs photo-z?

**The paper never states this.** §8.7 says "absence of spectroscopic redshifts" and proposes DESI cross-match as future work, implying most/all are photo-z or none. But the `fcw_vs_redshift.csv` was produced somehow, which means somebody had a $z$ estimate for each galaxy. My guess: these are photo-z from the DESI Legacy / Galaxy Zoo DESI cross-match (`Walmsley:2023`). The paper should say so, and should quote the $\sigma_z / (1+z)$ figure so the reader can propagate it into the radial profile.

For a $\sigma_z \sim 0.03 (1+z)$ photo-z error, at $z=0.5$ that's $\Delta z \sim 0.045$, which smears adjacent bins of width 0.04 almost completely into each other. **That would wash out any real $z$-evolution signal.** The fact that we see no trend in the 20-bin plot may partly reflect that — not a guaranteed null.

**Action.** Add to §2.1: "Redshift estimates are photometric from the Galaxy Zoo DESI cross-match [Walmsley:2023], with typical $\sigma_z / (1+z) \approx X$. No spectroscopic redshifts are used." State the $X$. Then in §6 / §8.7, note that this smearing sets a floor on $z$-evolution sensitivity of order $\Delta z \sim 0.05$, so no conclusion about $z < 0.1$ fine structure can be drawn.

## 7. "Chirality on AGN/QSOs" — **paper is clean here; directive concern is moot**

Paper 1's GOLD/SILVER QSO classifications (Pipeline 1) do not feed Paper 4. Paper 4 uses only the 3-class VIT output (CW / CCW / NOT_SPIRAL) and quarantines AGN/QSO/non-spirals into the NOT_SPIRAL bucket. §6.2 explicitly handles the edge-on galaxy contamination case (the one remaining morphological subtype where chirality is not well-defined) and correctly notes that equivariant averaging assigns exactly 50/50 CW/CCW to any galaxy whose mirror is morphologically indistinguishable — so edge-on contamination dilutes sensitivity but cannot bias.

The paper is correct that "chirality is meaningful only for resolved spirals, and the 3-class network exiles everything else." The 3.32M spirals are used for all parity statistics. **No double-count with Pipeline 1 GOLD/SILVER QSOs.** This concern is closed.

## 8. LSST projection (L908–929) — **back-of-envelope checks out**

> "Under a 10-year LSST nominal depth assumption and conservative spiral-fraction scaling, we project a catalog of ~$10^{8}$ resolved spirals—about 30× the present equivariant-spiral count."

My sanity check:
- LSST WFD survey area: 18,000 sq deg → factor ~2× the DESI Legacy DR8 useful-footprint of ~9,000 sq deg after masking.
- LSST 10-year co-add depth: $r \sim 27.5$ vs. DESI Legacy $r \sim 23.4$ → ~4 mag deeper → ~40× more galaxies per unit area (rough Euclidean count at faint end).
- Resolved-spiral fraction at LSST depth: drops as a function of magnitude because many faint galaxies become unresolved or ambiguous. The paper's implicit assumption is that the resolved-spiral fraction drops by a factor of maybe 2–3 relative to DR8, leaving a net ~15× improvement per unit area × 2× area = ~30× total. That's self-consistent.
- 3.32M current spirals × 30 = $10^8$. ✓

Minimum detectable dipole scaling: $\sigma \propto 1/\sqrt{N}$, so $\sqrt{30} \approx 5.5×$ tighter, from 0.2% at $3\sigma$ to 0.036% at $3\sigma$. Paper says $\sim 0.04\%$. ✓ Arithmetic checks out.

**One unstated caveat.** LSST is Southern Hemisphere; DESI Legacy is mostly Northern. This is a **different footprint**, not a superset. Any LSST $+$ DESI joint analysis requires a careful seam-treatment at Dec $\approx 0°$. The paper should at least acknowledge this in one sentence.

**No block; the arithmetic is fine; add a one-line footprint caveat.**

## 9. Data availability — **OK, with one missing DOI**

§9 pins `v2026.04` tags on both the HuggingFace dataset and model:
- `huggingface.co/datasets/bamfai/galaxy-chirality-catalog/tree/v2026.04` ✓
- `huggingface.co/bamfai/galaxy-chirality-v2/tree/v2026.04` ✓
- GitHub release `paper4-v1.0` ✓

**Missing:** Zenodo DOI. The text says "a Zenodo mirror with a minted DOI will be linked from the HuggingFace repository README at arXiv submission time." That's a future promise inside the submitted paper, which is a minor weakness — referees (and arXiv's own data-availability policy) prefer the DOI to already exist. Mint the Zenodo snapshot before submission.

Model checkpoint: correctly pinned to the `v2026.04` tag. The training hyperparameters are fully specified in §3.2. Reproducibility score here is high.

## 10. Cross-paper Paper 2 double-count concern — **clean**

Paper 2's Fisher forecast uses "2.28× bias" from the **anomaly-clustering** analysis (Pipeline 3), not the chirality catalog. The chirality catalog informs a logically separate parity test and is not folded into the $f_{\rm NL}$ Fisher. `paper2_chirality_section.tex` is a companion section describing the catalog as a complementary observable; it does not propagate chirality into the $\sigma(f_{\rm NL})$ number.

**No double-count.** The cross-ref in `paper2_chirality_section.tex:255` has been updated from "will be presented in future work" to a proper citation of Paper 4. Good.

## 11. Figures — **not inspected directly, but concerns from captions**

I did not open the 11 PNGs, but from captions and context:
- `fig_sky_map.png` Mollweide, color scale $\pm 5\%$ — OK.
- `fig_hemisphere.png` should use colorblind-safe scheme for the "red diamond" peak marker. Paper only says "red diamond"; consider switching to orange/triangle for accessibility.
- `fig_multipoles.png` shows $\ell=1$–5 with 1σ and 2σ envelopes. Missing: 3σ envelope (the threshold for "evidence"). Adding the 3σ band visually confirms $\ell=1$ at $2.75\sigma$ sits below the evidence line.
- `fig_raw_vs_eq.png` side-by-side A vs C — same color scale? Paper doesn't say. Must be matched or the 94.6σ-to-0.43σ collapse is not visually honest. Verify.

**Action items:** spot-check `fig_raw_vs_eq.png` uses a shared color bar; add 3σ band to `fig_multipoles.png`; reconsider red-only color for the hemisphere peak marker.

## 12. Falsifiability — **paper has it implicitly; make it explicit**

The paper does not currently contain a single-sentence falsification criterion. It should. My suggested wording, consistent with everything already in §8.3:

> **Falsification criterion.** If LSST Y3 detects a chirality dipole in a $\geq 10^7$-galaxy sample with amplitude $A \geq 0.1\%$ at $>5\sigma$ post-TTA and look-elsewhere-corrected significance, whose axis agrees with Shamir (2020, 2022) to within $30°$, then the null result presented here is falsified and a cosmological chirality dipole must be accepted.

Add this to §7 (Conclusions). It takes 3 sentences and makes the paper binary-testable.

---

## Residual concerns flagged but not blocking

- **"Rotation stability 89.8%"** is a one-number summary; the rotation-dependence of $P_{\rm CW}$ could be disaggregated by bar presence, axis ratio, and magnitude. That would be another 2-page appendix and is not required.
- **Confidence-stratification result** (§5.5): dipole "peaks in mid-confidence bin" is a great diagnostic for noise-origin signals, but the breakdown 0.3σ / 2.1σ / 1.7σ has no error bars and no MC null. One-liner: what is the sub-sample MC null for each bin? If 2.1σ in mid-confidence is inside the expected fluctuation envelope after look-elsewhere across 3 bins, say so.
- **"Mild CCW excess at intermediate confidence ... consistent with reading-direction bias" (§5.5).** Good catch but the magnitude 0.3% is reported without error. Give $\pm$ in a throwaway parenthetical.
- **"Barred spirals ... +0.4% ± 0.2% (~2σ)" (§5.5).** This is the only sub-2σ-but-nonzero result that could be a real signal. A skeptical referee will ask: run the same test on $P_{\rm CCW}$ (does CCW fraction in barred spirals go DOWN by 0.4%?) and on un-barred spirals as a control. 20 minutes of work.

---

## Ship-or-hold recommendation

**Ship after four fixes:**

1. **(Critical) Reconcile "10,000 bootstrap" with the 1,000-realization production log,** or commit the additional 10K run. No ambiguity on the MC null count in a paper whose central claim is a null.
2. **(Critical) Remove "D4" language** from L920 and anywhere else in the paper. Use "flip-equivariant" or "Z2 TTA." Alternatively, run actual D4 TTA (8-pass) and re-report.
3. **(Strong) Commit the post-TTA dipole script.** The paper headline 0.43σ number must be traceable to code in the repo. The pre-TTA 2.31σ is traceable (`run_dipole_8M.py` → `chirality_dipolar_analysis.py` on pod); the post-TTA is not.
4. **(Strong) Add the $z$-binned dipole figure** using the existing `fcw_vs_redshift.csv` rerun on Catalog C. This closes the §8.7 primary limitation before a referee raises it.

**Nice-to-have:**

5. Add the BASS/MzLS vs DECaLS (Dec $\approx$ +32°) split row to Table III.
6. State the photo-z error $\sigma_z$ in §2.1 and propagate into the $z$-binned sensitivity floor.
7. Mint the Zenodo DOI now.
8. Add an explicit single-sentence falsifiability criterion in §7.
9. Spot-check figure color-bar matching (A vs C panels) and colorblind accessibility.
10. Quick barred-spiral control test.

**Publication verdict:** strong paper, ready for astro-ph.CO primary / astro-ph.GA secondary once items 1–4 are closed. Items 5–10 are all $\leq 30$ min each and would raise it from "good" to "bulletproof." **None of the findings change the headline null result.**

---

## Receipts

- **D4 mismatch:** `equivariant_postprocess.py:428` is `torch.flip(bt_orig, [3])` (horizontal flip only; Z2); paper abstract + §3.4 + L920 uses "equivariant" / "D4" language. No `rot90` or D4 transform anywhere in `pipelines/p2_chirality/`.
- **MC realization count:** `outputs/dipole/dipolar_analysis.log:18` = 1,000; paper L499 = 10,000. `run_dipole_8M.py:72,114` = 10,000 but runs only on raw and Platt-calibrated, not Catalog C.
- **Pre-TTA vs post-TTA script:** pre-TTA 2.31σ traceable to `chirality_dipolar_analysis.py` (pod-only, summary.json `source_script: "/root/experiments/chirality_dipolar_analysis.py (pod snapshot, see paper Appendix D)"` — Appendix D does not exist in the paper). Post-TTA 0.43σ not traceable.
- **fcw_vs_redshift.csv uses raw Catalog A:** 20 rows, all values cluster at 0.507–0.513, matching raw $0.5079$, not equivariant $0.4974$.
- **Photo-z disclosure gap:** $\sigma_z$ not stated in paper; only reference is "absence of spectroscopic redshifts" (§8.7).
- **Shamir-axis alignment red herring:** `summary.json` reports `shamir_claimed_axis.separation_deg: 18.9` (ALIGNED) for the **pre-TTA 2.31σ raw dipole**. This is not a hint that Shamir is right; it's a hint that the raw pipeline reproduces Shamir's result when you don't correct for classifier bias × scan geometry — which is the paper's central point, but only visible once you read the supplementary JSON. The paper text does not currently call out that the 18.9° alignment of the raw pre-TTA axis with Shamir's claimed axis is itself evidence that Shamir's signal is systematics, not physics. **This is actually a beautiful result that strengthens the paper; include it.**

---

*Reviewer: dipole skeptic, autonomous 2026-04-18 review round.*
*No source edits performed; no commits made.*
