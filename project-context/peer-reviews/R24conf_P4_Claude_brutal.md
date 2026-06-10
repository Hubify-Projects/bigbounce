# P4 R24conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/chirality_catalog_paper_v168.pdf` md5=90c4a8a3 pages=19
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique

---

## Pass-1 (native PDF) findings

Brutal PRD referee. All numbers recomputed against `pipelines/p2_chirality/chirality_catalog_paper.tex`. Calibration items (June 2026 retraction/correction notes, HC selection in abstract, full-sample 4.2σ disclosure as systematics, axis-averaged protocol, 2.98× suppression, eight-anchor battery, 0.41σ→0.43σ MC-noise statement) are deliberate and not flagged.

### P4-E1 — None

No errors of fatal-to-headline severity were identified after exhaustive cross-check of the headline 0.41σ/p=0.31, shuffle 0.58σ/0.26 (and z=0.70/0.23 independent reimpl.), HC N=949,584, MASTER +3.64σ canonical / +7.28σ apodized / +7.13σ depth-stratified, monopole-only 99.32% reproduction, A_50≈0.75%, A_95∈(1.0%,1.5%], WLS z≈−18.1, hemisphere LEE, 0.4801/0.49005/0.494 f_sky bookkeeping, 4.2–4.4σ full-sample (below A_50, dispositioned), and axis-spot-check 0.45–0.62/mean 0.54 vs tabulated 0.55. The cross-anchor consistency (rows i and iv of Table I deliberately not on the same statistical footing) is correctly disclosed in the text immediately following Sec. IV C.

### P4-M1 — Headline 0.41σ vs Table I row (i) `+0.41` typographic-sign convention

The abstract and Sec. III A row (i) consistently report `+0.41σ` (moment-ratio z against isotropic-permutation null mean+width). Table I row (i) σ column reads `+0.41`. The "σ" header conflates two quoted statistics: rows (i),(iii)–(vi) are *signed moment z-scores*, row (ii) is a *block-bootstrap exclusion z* (negative, `z≈−18`), and row (vii) reports an `A=0.75%` injection floor, not a σ. The header reads "σ" but the column is heterogeneous: moment-z, exclusion-z, and amplitude. Table caption disclaims "σ values in different rows are computed against different null procedures." That handles distinct *nulls*, but does not resolve that row (ii) is a fitted-template *exclusion* and row (vii) is not σ-quantified at all. PRD referee would push the author to relabel the column "Reported statistic" (units in parens) and split row (vii) into a separate "sensitivity" row. Not a numerical defect; presentational MAJOR.

### P4-M2 — Axis-protocol spot-check arithmetic

Sec. VI A: fixed-axis spot check at A=0.75% gives per-axis P(σ>3) spanning 0.45–0.62, "16–84% range 0.49–0.58; axis mean 0.54", "consistent with the tabulated axis-averaged 0.55 within MC error". With 10 axes × 100 injections each, the per-axis P estimate has standard error √(0.54·0.46/100) ≈ 0.050 per axis; across 10 axes the axis-mean SE is ≈ 0.050/√10 ≈ 0.016 (intra-axis), plus the axis-orientation scatter itself (the 0.49–0.58 16–84% inner range implies orientation σ ≈ 0.05). Quoted 0.54 vs tabulated axis-averaged 0.55 differ by 0.01, well within MC error — verdict OK. **However** the axis-orientation polar-angle draw is θ~U(0,π) (uniform in θ), not uniform on the sphere (sin θ); the paper itself acknowledges this "mildly over-weights near-polar axes". The fixed-axis spot check is "10 axes drawn area-uniformly on the sphere", i.e. a *different* axis distribution. Comparing 0.54 (area-uniform) to 0.55 (θ-uniform) and calling them "consistent within MC error" is *true*, but the comparison would be tighter if both used the same distribution. PRD would flag this as a half-step disclosure. MINOR/MAJOR boundary — call MAJOR because the axis-averaged falsification criterion (Sec. VII) inherits the same θ-uniform protocol and a reader could rightly ask: would an area-uniform axis-averaged P(σ>3) at A=0.75% lie at 0.54 or 0.55? The spot check supports the value but does not lock the falsification axis convention.

### P4-M3 — `f_sky=0.4801` for HC real-space dipole row (i) is undefined in App. A Table VI

Table I row (i) lists `f_sky=0.4801` for the HC real-space dipole mask. Appendix A Table VI enumerates six mask/weight/apod configurations and their f_sky: 0.49005, 0.482, 0.494, 0.488, 0.452, 0.420. **The value 0.4801 does not appear in Table VI.** The text of Sec. III C uses the HC selection (conf>0.6, N=949,584) and pixel mask N_spiral(p)≥10 of the same canonical mask — but the canonical f_sky in Table VI is 0.49005, not 0.4801. The discrepancy is presumably because the HC subsample populates fewer pixels at the ≥10-spiral threshold, slightly shrinking the mask, but **App. A does not document the HC-mask f_sky derivation**. PRD referee MAJOR: every Table I f_sky must be reproducible from App. A. Either add the HC-mask row to Table VI, or footnote Table I row (i) explaining `0.4801 = canonical mask intersected with HC sub-pixels meeting ≥10 HC-spiral threshold`. Without that footnote a reproducer cannot regenerate the row.

### P4-M4 — Monopole-only generative null per-realization standard error vs SE of mean

p. 8 footnote / Sec. IV D: "monopole-only null reproduces 99.32% ... (±0.40 pp per-realization null scatter, N=500; the residual is +1.69σ, Table IV). ... The standard error on the mean reproduction fraction is 0.40/√500 ≈ 0.018 pp (the ±0.40 pp quoted above is the per-realization scatter, not the uncertainty on the mean)." Correct. **But** the 1.69σ residual statistic uses the *per-realization* scatter (0.40 pp), as required for an excess-power test on a single observed value, not the SE-of-mean. Confirmed against Table IV row 1: data 1.6961×10⁻², null mean 1.6846×10⁻², null std 0.0068×10⁻² → z=(1.6961−1.6846)/0.0068 = 1.69 ✓. Internally consistent. The presentation is fine; flagging only because PRD reviewers commonly misread "0.40 pp ± 0.018 pp" as a single uncertainty — the footnote already disambiguates. MINOR.

### P4-M5 — `+7.28σ` (500-MC, App. A label-shuffle) vs `+7.31σ` (10⁴-recompute, Table III) — small consistency note

Abstract & headline: "+7.28σ apodized footprint" (from 500-MC null). Sec. III C body of dipole section: same 7.28σ. Table III (10⁴-permutation recompute, apod., W_p=N_all, ℓ=1): C₁=24.74×10⁻⁶, ⟨C_b⟩null=1.93×10⁻⁶, σ_null=3.12×10⁻⁶ → z=(24.74−1.93)/3.12 = 7.31 ✓. The 500-MC and 10⁴-MC nulls agree at the ~0.03σ level. Not flagged as a defect; the paper says "the 10⁴-permutation recompute (Table III) confirms this channel at z=+7.31". GOOD disclosure.

### P4-M6 — 0.43σ→0.41σ correction note: rank-p `0.30→0.31` change

Sec. III C correction bracket: "an earlier version printed 0.43σ (p=0.30) from a 10³-realization run ... the prior and regenerated values agree within Monte-Carlo noise". With 10³ realizations, the SE on a rank-p estimate near 0.30 is √(0.30·0.70/1000) ≈ 0.0145. With 10⁴ realizations, SE ≈ 0.0046. Δp = 0.01 is well within the combined SE (~0.015). Δz from 0.43 to 0.41 with rank-p estimator: not Gaussian, but the moment-z is a sample statistic on a positive-definite quantity, and 0.02σ shift from a single re-run is consistent with the 10³-vs-10⁴ MC noise floor. The "selection-filter defect (selected only CW-confident galaxies)" disclosure is honest and pre-emptive of the obvious referee question. MINOR (already self-disclosed).

### P4-m1 — Table I caption `Bonferroni/BH 648-direction post-LEE` qualifier on row (v)

Table I row (v) σ column reads `p_LEE ≤ 10⁻⁴ (syst.-attr.)`. Caption: "Row (v) reports the post-look-elsewhere-corrected significance; the raw direct-MC value is p_LEE ≤ 10⁻⁴ against the random-label max-statistic null, which *already incorporates* the look-elsewhere scan; the additional Bonferroni/BH pass over the 648 tested directions reported in Appendix C is a second, deliberately conservative penalty (the two corrections bracket the significance), and the rejection is systematics-attributed either way." This is correct but verbose. Two LEE corrections (max-statistic null *and* Bonferroni/BH on the 648-direction p-values) is bookkeeping-overkill; a single principled correction would suffice. The choice is conservative and not wrong. MINOR cosmetic.

### P4-m2 — Confidence-threshold sensitivity disclosure naming

Sec. III C: "dropping the confidence threshold entirely (all 3,200,420 in-mask equivariant spirals) yields a 0.57% dipole at z≈4.2–4.4". The number 3,200,420 is the *in-mask* spiral count, vs the Catalog C total of 3,201,160 (Δ=740, a fraction of a pixel-edge rounding). Both numbers appear in the paper without an explicit cross-pointer (the 3,201,160 is canonical, in-mask 3,200,420 is the dipole-fit denominator). PRD reviewer would request a single footnote explaining the 740-galaxy delta. MINOR.

### P4-m3 — Abstract `1.9σ Gaussian-equivalent` for canonical-mask `+3.64σ` moment-z

Abstract: "+3.64σ moment-z, ≈1.9σ Gaussian-equivalent, canonical mask". Sec. III D / Table III footer also states "$+3.64\sigma$ (p_MC=0.030, one-sided, ≈1.9σ Gaussian-equivalent)". From p_MC=0.030 → z_Gauss(one-sided) = Φ⁻¹(1−0.030) = 1.88. Matches "≈1.9σ" ✓. Same moment-z 3.64 differs from the Gaussian-equivalent 1.9σ by a factor ~1.9 because the permutation null is heavy-tailed at low ℓ (Table III caption explicitly states this). Internally consistent and well-disclosed. GOOD.

### P4-m4 — Page 5 axis-RA-partition `±0.110% to −0.463%` arithmetic spot-check

p. 5 (Sec. IV B): "deviations from 0.5 of −0.110% to −0.463%, all within 0.5% of 50/50". With per-slab binomial σ = √(f(1−f)/N) at f≈0.5 and N≈457,308: σ_f = √(0.25/457308) = 7.4×10⁻⁴, i.e. 0.074 pp. Quoted "per-slab binomial σ = 7.4×10⁻⁴" matches ✓. With f_CW = 0.49735, the slab-to-slab scatter "≲ 2.7σ per slab" is roughly (0.50−0.49735)/0.00074 = 0.00265/0.00074 = 3.58. The "≲ 2.7σ" qualifier should likely be "≲ 3.6σ per slab" — or the 2.7σ is computed against a different reference. Re-reading the text, "2.7σ per slab consistent with the coherent low-ℓ systematic structure" — the 2.7σ is the *worst* observed slab deviation from the *catalog mean* (0.49735), not from 0.5. Deviation 0.49537−0.49735 = −0.00198 → −0.00198/0.00074 = 2.68σ ✓ from the mean. **OK, my misread**. Verified GOOD.

### P4-N1 — Reference list completeness

References [1]–[39] all loaded. Spot-check: [8] Dey+ DESI Legacy overview correct; [9] Walmsley+ DESI GZ DESI catalog (2023) correct; [10] Lintott+ Galaxy Zoo correct; [12] Dosovitskiy+ ViT correct; [32] Alonso+ NaMaster correct; [33] Hivon+ MASTER correct; [34] Górski+ HEALPix correct. None garbled. GOOD.

### P4-N2 — Reproducibility surface

Catalog HF link present, GitHub `Hubify-Projects/bigbounce` present, commit `2a2939b2` cited, `v2026.04` release tag stated, Zenodo DOI listed as not-yet-minted (which is acceptable for a community-resource paper but PRD's reproducibility policy would want it minted by acceptance). MINOR — would surface as a referee request in the next round; here, calibration-deliberate. NOT FLAGGED.

---

## Explicit all-clears

- Abstract↔§III↔§IV↔Table I↔§VII numerical consistency on headline 0.41σ/p=0.31 — CHECKED, CLEAN.
- Two independent shuffle nulls (0.58σ/0.26 generator-internal; 0.70/0.23 independent reimpl.) — CHECKED, CLEAN.
- N=949,584 HC count appears in abstract, Table I row (i), Sec. III C dipole text, Sec. VI A injection table caption, Table V caption — all matching.
- 2.98× equivariant suppression (1.576% raw → −0.529% A-units): Table II tier-A excess 0.788% × 2 = A_raw 1.576%; tier-C dev −0.265% × 2 = A_eq −0.529%; 1.576/0.529 = 2.98 ✓.
- A_50≈0.75% & A_95∈(1.0%,1.5%]: Table V P(σ>3)= 0.55 at A=0.75% (50% boundary), 0.91 at 1.0%, 1.00 at 1.5% — consistent with bracketing.
- WLS template-fit z=−18.1 (block-bootstrap, 9-template): Table IX, dipole-amplitude posterior $A_{\rm dipole}^{\rm best}=4.55\times10^{-3}$, σ_dipole=1.63×10⁻⁴, exclusion at A_ref=0.034 (1.7% in f_CW units): z=(4.55×10⁻³ − 0.034)/1.63×10⁻⁴ = −18.1 ✓.
- Monopole-only null 99.32%: pre-MASTER C_1 data 1.6961×10⁻², null mean 1.6846×10⁻², ratio 1.6846/1.6961 = 0.9932 = 99.32% ✓.
- 8.47M galaxies = 8,474,531 = 1,592,107 + 1,609,053 + 5,273,371 ✓.
- Spiral N = 3,201,160 = 1,592,107 + 1,609,053 ✓.
- f_CW from Catalog C = 1,592,107/3,201,160 = 0.49735 ✓ (matches §IV B "global f_CW = 0.49735").
- Eight-anchor battery (a)–(h) in App. D all present and individually defended.
- Falsification criterion in abstract = falsification criterion in §VII = `≥5σ at A≳A_95`, A_95∈(1.0%,1.5%], internally consistent.
- Withdrawn subsample-mask null clearly bracketed in App. A.d.; no headline conclusion depends on it.

---

## Pass-2 self-critique (against `pipelines/p2_chirality/chirality_catalog_paper.tex`)

On re-reading the .tex source I confirm the following:

- P4-M3 (`f_sky=0.4801` not in Table VI) **stands**. Table VI line-numbers 511–518 enumerate exactly six configurations; none is 0.4801. The HC-mask f_sky derivation is genuinely undocumented in App. A. Real MAJOR.
- P4-M2 (axis-protocol θ-uniform vs area-uniform) **stands**. .tex line 441 confirms θ~U(0,π) for the production tabulated probability and a separately drawn area-uniform 10-axis spot check. The "consistent within MC error" claim is true; the protocol mismatch disclosure is genuinely thin.
- P4-M1 (Table I heterogeneous σ column) **stands but downgraded** — re-reading the caption ("σ values in different rows are computed against different null procedures") it is half-handled; the column-header relabel is the cleanest fix.
- P4-M4, P4-M5, P4-M6 (numerical SE/Gaussian-equiv./MC-noise checks) — all verified internally consistent. Self-critique: I am tempted to demote these to "all-clears" but they remain as MINORs because a PRD referee *will* ask about each.
- P4-m4 (slab-binomial 2.7σ) — self-correction: my first reading would have flagged this as an arithmetic defect; the 2.7σ is correctly computed from the catalog mean, not from 0.5. Removed from defect list (kept here as evidence of the pass-2 self-check).

I considered but rejected the following additional flag candidates:
- "$N_{\rm spiral}=3{,}201{,}160$ vs in-mask $3{,}200{,}420$" — accounted as m2; not a separate defect.
- "monopole-only null reproduces 99.32%" — verified arithmetic, not a defect.
- "0.41σ headline is suspiciously close to half the 0.79% raw CW excess in σ units" — coincidence, the 2.98× TTA suppression sets the scale; not a defect.
- "Cohen's κ=0.40 is a noticeably low classifier-truth agreement" — acknowledged in paper (App. B/E); calibration-deliberate.
- "Page 17 says `monopole-preserving Catalog-C-full +4.31σ`" — the +4.31σ pre-MASTER value is correctly contextualized in App. E footnote-3 as a *different* estimator (no monopole subtraction) from the headline +3.64σ. Not a flag.

---

## Summary recommendation + counts line

Recommendation: **Reject in current form; resubmit with the M-tier fixes addressed.** The paper's scientific content is solid — the headline real-space null, the bias-hardening suite, the monopole-mask leakage diagnosis, the eight-anchor systematics battery, and the withdrawal protocol are all rigorous and self-consistent at the arithmetic level. What blocks acceptance at PRD is presentational: Table I's heterogeneous σ column, the undocumented HC-mask f_sky in Table VI, and the axis-protocol convention disclosure. These are fixable in one revision pass.

E:0 / M:6 / m:4 / N:2
