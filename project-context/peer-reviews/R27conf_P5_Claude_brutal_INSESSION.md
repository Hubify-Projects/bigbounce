# P5 R27conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/p5_desi_chirality_v0.1.58.pdf` md5=6ffcd714 pages=27
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## §IX.A completeness-weighted rebuild — verification against artifact

Artifact: `pipelines/p5_desi_chirality/outputs/25_completeness_weighted_rebuild.json`.

| Paper claim (lines 2017–2036) | Artifact value | Verdict |
|---|---|---|
| $7.5\times 10^7$ randoms | `n_deposited = 74,728,906` | OK (rounds correctly) |
| $0.01<z<0.50$ window | `z_range_used = [0.01, 0.5]` | OK |
| $99.3\%$ of matched spirals | $786{,}256 / 791{,}635 = 99.3205\%$ | OK |
| Volumes shift up to $21$ pp | max-abs vol shift `20.676 pp` (filament) | OK (rounds 21) |
| $44\%$ common-mask cell-class agreement | `cell_class_agreement_on_common_mask = 0.4380` | OK (rounds 44) |
| $\Delta f_{\rm CW}$ filament $+0.05$ pp | `+0.0514 pp` | OK |
| $\Delta f_{\rm CW}$ cluster $-0.03$ pp | `-0.0274 pp` | OK |
| $\Delta f_{\rm CW}$ wall $-0.40$ pp | `-0.4037 pp` | OK |
| $\Delta f_{\rm CW}$ void $+2.7$ pp ($n\!\approx\!430$) | `+2.697 pp`, $n_{\rm void}^{D}=432$ | OK |
| void $\pm 4.8$ pp counting width | binomial $1\sigma$ at $n=432$ is $2.40$ pp; $4.8$ pp = $2\sigma$ | OK only if read as $2\sigma$; see m1 |
| cube-3 dilation $\le 3.1$ pp | `max_abs_volume_fraction_shift_pp = 3.114` (void) | OK |
| cube-3 spiral agreement $99.6\%$ | `0.99599` | OK |
| cube-3 max $f_{\rm CW}$ shift $\le 0.77$ pp | `max_abs_f_cw_shift_pp = 0.7675` | OK |

Geometry-matching disclosure (no `GALAXY`-spectype analog in BGS_BRIGHT randoms; restriction to $0.01<z<0.50$): the paper carries the disclosure (lines 2017–2022) and it matches the `geometry_matching_disclosure` text in the JSON. **Honest, prominent, and load-bearing — accepted.**

---

### P5-M1 (MAJOR — §IX.A): the "robustness" framing buries the magnitude of the relabeling

The paragraph (lines 2022–2032) presents the completeness-weighted rebuild as confirming environmental-independence. Two numbers in the artifact deserve foreground placement in the paper, not just the `delta_pp` summary:

1. **Spiral-level class agreement is only $26.6\%$** (`spiral_class_assignment_agreement = 0.2662`), not the $44\%$ cell-level number quoted in the paper. Three quarters of the spirals are reassigned a different cosmic-web class under the completeness weighting. The paper quotes the cell-level number ($44\%$) which makes the rebuild sound less disruptive than it is on the matched-spiral subsample that actually carries the headline.

2. **Class volume fractions in the weighted build $B$ are extreme**:
   - $A$ unweighted window: $\{$void $17.6\%$, wall $36.1\%$, filament $44.6\%$, cluster $1.76\%\}$
   - $B$ randoms-weighted window: $\{$void $0.75\%$, wall $19.2\%$, filament $65.3\%$, cluster $14.8\%\}$

   The void fraction *collapses by a factor of ${\sim}23$* and the cluster fraction *grows by a factor of ${\sim}8.4$*. These are not "shifts of up to 21 pp" in the casual sense — the void class essentially disappears as a volume-defined object in the weighted build, and the cluster class swells until it is volume-dominated relative to its unweighted self. The paper's "up to 21 pp" language ($\max$ over four classes of a signed pp shift) understates this by a factor of $\sim 5{-}20$ in relative terms.

This matters because a reader assesses "robust to selection-completeness weighting" against the magnitude of the perturbation. A 26% spiral-level reclassification with an $8{-}23\times$ relative restructuring of the class volume fractions is a *severe* test, not a routine one, and the paper deserves credit for surviving it — but it should *say* the test was severe, not understate it.

**Fix**: add one sentence quoting (a) the $26.6\%$ spiral-level reassignment number and (b) the absolute volume-fraction vector in $B$ (or the void-collapse ratio), so the reader can judge the perturbation size for themselves.

### P5-m1 (minor — §IX.A): "$\pm 4.8$ pp counting width" should be labeled $2\sigma$

Line 2030: "well inside that bin's $\pm 4.8$ pp counting width" — the binomial $1\sigma$ on $f_{\rm CW}$ at $n = 432$ is $0.5/\sqrt{432} = 2.41$ pp, so $\pm 4.8$ pp is a $2\sigma$ counting band. The +2.7 pp observed shift is then $\approx 1.1\sigma$ — null but only mildly so. The text reads as if 2.7 pp is comfortably $\ll$ the natural statistical floor; in fact it is right at $1\sigma$. Label the band $2\sigma$ explicitly, or quote $\sigma_{\rm 1\sigma} = 2.4$ pp and characterize 2.7 pp as a $1.1\sigma$ deviation, which is honest and still null.

### P5-m2 (minor — §IX.A): scope-of-test caveat on $0.01<z<0.50$

The 99.3% retention is over *matched* spirals, which already concentrate near $z \approx 0.17$ (Fig. 1, median 0.168). The $z>0.5$ tail of the matched sample is small *by selection of the catalog*, but the *parent* selection-function pathology that §IX.A's preamble flags — per-shell mean density spanning $\bar n \approx 294 \to 0.46$ over a factor of ${\sim}640$ — is concentrated at $z > 0.5$ where this completeness rebuild does *not* run. Add one sentence: the rebuild tests selection-completeness sensitivity in the regime where most of the matched-spiral signal lives, but does not by itself rule out residual radial-selection contamination of the V-Web labels at $z > 0.5$; that is bounded separately by the z-shell correction of §IX.A second paragraph and the geofootprint check of §IX.A.b. (The bound exists in the paper, it just isn't tied back to the completeness paragraph.)

### P5-m3 (minor — §IX.A): cube-3 dilation summary loses sign information

Line 2034: "shifts volumes by $\le 3.1$ pp" — this is dominated by the void fraction *decreasing* by 3.11 pp (24.4% $\to$ 21.2%), a $\sim 13\%$ relative decrease in the smallest-population class that carries the headline counting noise. The number is faithfully reported but the directional read (void shrinks under more aggressive dilation) is suppressed. Optional: one phrase noting which class drives the maximum.

---

## Beyond §IX.A — focused pass over anything the new paragraph touches

### P5-m4 (minor — §IV.A vs §IX.A wording on completeness): half-fixed standing claim

Line 2010–2015 (§IV.A end) still says "no spectroscopic tiling/completeness weighting (e.g.\ DESI random-catalog or FKP-like per-cell weights) is applied when building $\delta$." Strictly true for the canonical pipeline. The next sentence ("The randoms-weighted rebuild has now been run…") does pivot, but a reader skimming §IV.A in isolation will see only the negative claim. Add a half-sentence cross-reference: "(but see §IX.A for the randoms-weighted rebuild)." Cosmetic, helps reviewers.

### P5-E1 (explicit all-clear, with arithmetic): every quoted number in §IX.A reconciles with the JSON

Recomputed against `25_completeness_weighted_rebuild.json`:

- randoms: 74,728,906 $\to$ $7.5\times10^7$ ✓
- $786{,}256 / 791{,}635 = 0.99320 = 99.3\%$ ✓
- $\max(|{-16.81}|, |{-16.86}|, |20.68|, |12.99|) = 20.68 \approx 21$ pp ✓
- cell-class agreement $0.4380 \to 44\%$ ✓
- per-class $\Delta f_{\rm CW}$: $(+0.0514, -0.4037, +0.0514, -0.0274)$ rounds to (filament $+0.05$, wall $-0.40$, void $+2.70$, cluster $-0.03$) ✓
- cube-3: $\max |\Delta {\rm vol}| = 3.114$, spiral agreement $0.99599$, $\max |\Delta f_{\rm CW}| = 0.768$ ✓

No arithmetic miscall in §IX.A.

### P5-E2 (explicit all-clear): the deliberately calibrated items are correctly disclosed

Verified per calibration list:
- ZONEVOID correction and SGC over-write defect (page 16): documented, corrected version explicit, supersession noted.
- Count ledger (abstract + §VIII F + §VI A): 14,622,283 row parent / 12,479,283 unique TARGETIDs / 791,635 chirality-relevant / 783,820 environment-joined unique spirals / 812,793 row-level env-labeled / 7,815 lacking env row — internally consistent across all five surfaces.
- Stratified LEE: $p_{\rm strat}=0.135$ on NSIDE=32, sit ${\sim}2.4\times$ above $\sqrt{p(1-p)/N_{\rm MC}}$ floor; explicitly characterized as stream fluctuation, not a verdict change.
- Unique-parent rebuild (§VIII F + `23_unique_parent_rebuild.json` ref): wall $-0.70$, filament $+0.68$, cluster $+0.20$, void $-0.18$ pp; 97.8% cell + 97.9% spiral agreement; $\le 0.23$ pp per-class $f_{\rm CW}$ delta; correctly reported as headline-invariant.
- Sample-ledger one-breath sentence (abstract): all five subsample sizes (56,981 / 791,635 / 7,815 / 812,793 / 783,820) appear and are traceable to §VIII and §VI A.

All five deliberate disclosures are present and correctly characterized.

---

## Pass-2 self-critique

Re-read of the paper §IX.A paragraph (lines 2016–2036) against my own M1/m1/m2/m3:

- **M1 retained.** The 26.6% spiral-level reassignment and the absolute volume vector $\{0.75, 19.2, 65.3, 14.8\}\%$ for the weighted build $B$ really are buried, and a brutal reviewer would press on this. They show that the headline survives a much harsher rearrangement than the paper's plain-language summary suggests, and the paper should *claim that strength*, not hide it. The fix is one sentence.
- **m1 retained but soft.** "Counting width" is widely used colloquially for $\pm 2\sigma$ in the systematics literature and is not a hard error; calling it M1-level would be over-call. It is genuinely minor.
- **m2 retained but soft.** The paper *does* address the $z>0.5$ regime separately (z-shell correction, geofootprint cross-check, DESIVAST primary path), so the §IX.A scope limitation is not a load-bearing gap, only a paragraph-level clarity ask. A "could be elevated" pass-2 alternative would be: argue the §IX.A rebuild is *presented* as the answer to the radial-selection systematic flagged in the same paragraph's opening, but it only directly answers it for $z<0.5$. Stays at minor — the paper carries the bound elsewhere.
- **m3 retained as cosmetic.**
- **m4 retained as cosmetic.**

No new finding upgraded on second pass; no existing finding downgraded.

I also re-checked whether a brutal reviewer would dispute the **circularity** of the test (per-class $f_{\rm CW}$ stays near 0.5 because the Paper IV monopole *is* near 0.5, so any environment reclassification leaves the per-class average near 0.5). The paper explicitly inoculates against this in §V (monopole-referenced $\sigma_{\rm vs\,monopole}$) and Table X (residuals after monopole subtraction), and §VIII F derives the per-class $\sigma_{\rm pred}$ as a *prediction* of the catalog-monopole leak. So the circularity charge is not maintainable on a fair read — the paper has done the right hygiene. **No additional finding raised.**

---

## Summary recommendation + counts line

The new §IX.A completeness-weighted rebuild paragraph is *numerically faithful* to its artifact and *correctly anchors* the geometry-matching disclosure. The brutal-mode concern is presentational, not analytical: the paragraph understates the severity of the test it survives (26% spiral-level reassignment, ${\sim}23\times$ void-fraction collapse) and uses $\pm 4.8$ pp without labeling it $2\sigma$. Both fixes are one-sentence edits and neither changes the headline conclusion. The cube-3 dilation, $z<0.5$ scope caveat, and §IV.A cross-reference are minor cleanups. The paper is publication-ready conditional on M1 (foreground the perturbation magnitude) and m1 (label the $2\sigma$ band) being addressed.

**Recommendation**: ACCEPT with minor revisions (one MAJOR-presentation, three minor, one cosmetic).

**Counts**: P5-E0 / P5-M1 / P5-m4 / P5-N0 — 0 BLOCKER, 1 MAJOR, 4 minor, 0 novelty.
