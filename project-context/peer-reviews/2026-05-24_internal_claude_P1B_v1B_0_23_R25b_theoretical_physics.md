# P1B v1B.0.23 — R25b theoretical-physics verdict

**Reviewer**: Internal Claude, theoretical-cosmologist / Gemini-cosmology-rotation persona
**Round**: R25b (round 1-of-3 of fresh §4.4.1 cross-model verification streak on v1B.0.23)
**Date**: 2026-05-24
**Protocol**: Top-to-bottom paper read + dimensional/units consistency cross-check + arithmetic verification of every prefactor and range against on-disk JSON / chain artifacts.
**Persona**: Maldacena-style "is the formula right and does it land where the paper says it lands?" rigor; Bayesian/frequentist sharpness; post-hoc-vs-prediction discipline.

---

**1 BLOCKER / 2 MAJOR / 2 minor / 0 nit**

(NB: R25a already swept the "+4.3σ" framing per its MAJ-2 and the v1B.0.23 header documents the FALSIFIED disposition at L584. I confirmed by re-reading L376–392 + L584 that the unsampled-tail caveat is in fact present in the live body; I will NOT re-raise it. The findings below are NEW defects that survived R25a.)

---

## BLOCKER

### BLK-1 — Spectator-ALP β prediction range "$\beta \approx 0.17$–$0.43^\circ$" is arithmetically wrong; the true range from the paper's own quoted parameter intervals is $[0.027^\circ, 0.439^\circ]$ — the lower bound is off by a factor of ~6

**Claim location**: §VI ("Cosmic Birefringence: Spectator ALP Consistency Check"), line 644:
> "The prediction spans $\beta \approx 0.17$–$0.43^\circ$ over $C_{a\gamma}\in[4,12]$, $m/H_0\in[1,3]$, $\theta_i\in[0.5,2]$, comfortably bracketing the observed value without fine-tuning."

**Reproduced from paper's own formula** (Eq. on L639–641): $\beta = \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi}\,(\Delta\phi/f_a)$.
- $\alpha_{\rm EM}/(4\pi) = (1/137.036)/(4\pi) = 5.807 \times 10^{-4}$ rad.
- Paper's quoted $\Delta\phi/f_a$ range (L636) = $[0.2, 1.1]$.
- $\beta_{\min} = 5.807\times 10^{-4} \times 4 \times 0.2 = 4.65\times 10^{-4}$ rad $= \mathbf{0.0266^\circ}$.
- $\beta_{\max} = 5.807\times 10^{-4} \times 12 \times 1.1 = 7.66\times 10^{-3}$ rad $= \mathbf{0.439^\circ}$.

**On-disk evidence** (paper version-history comment at L98 — preamble, NOT rendered):
> "ALP beta-range arithmetic [4,12]x[0.2,1.1]x0.0333 = [0.027, 0.44] vs [0.17, 0.43] (GPT-B6)"

i.e., a prior 5-vendor reviewer (GPT-B6) already independently caught this in a previous round, and it was logged as a DEFERRED item in the v1B.0.13 history block. **It has remained deferred through v1B.0.13 → v1B.0.18 → v1B.0.22 → v1B.0.23, with the wrong numbers still in the live body text on L644.** Three R-rounds and one brutal-honesty round have closed since, none of them re-flagged it because they didn't redo the arithmetic.

**Defect rationale**: This is the classic "post-hoc vs prediction" tell. The "comfortably bracketing the observed value $0.342^\circ$" framing reads like an a-priori test that the model passes; but the true lower-end prediction of the spectator-ALP class as quoted in the paper is $0.027^\circ$, **13× smaller** than the observed signal. The actual observation is bracketed *only at the upper end* of the $C_{a\gamma}$ × $\Delta\phi/f_a$ grid — i.e., the model accommodates the signal only when both parameters are pushed to their natural maxima ($C_{a\gamma} \gtrsim 9$, $\Delta\phi/f_a \gtrsim 1.0$). My independent arithmetic check using $\beta_{\rm obs}/[\alpha/(4\pi)] = 10.28$ requires $C_{a\gamma} \in [9.3, 51.4]$ over the $\Delta\phi/f_a$ range — the abstract footnote at L818 actually states this correctly ($C_{a\gamma}\in[9, 51]$). So the conclusion text and the §VI body text **disagree internally**: the conclusion gives the correct C-range, but the §VI prediction range $\beta\in[0.17, 0.43]$° is computed with a $\Delta\phi/f_a$ floor of $\sim 0.66$, not the $0.2$ floor that the same paragraph quotes for the field-displacement range. Either (a) the lower $\beta$ bound is wrong (most likely, since $0.17 / [\alpha/(4\pi) \times 4] = 0.65$ — i.e., the lower bound was computed at $\Delta\phi/f_a = 0.65$, the median value from L633, not the parameter-grid minimum $0.2$), or (b) the $\Delta\phi/f_a$ range on L636 should be $[0.65, 1.1]$ not $[0.2, 1.1]$. Pick one and make them consistent.

**Severity = BLOCKER**: this is the load-bearing "the observed $\beta$ is comfortably bracketed by natural ALP parameters without fine-tuning" claim. With the corrected range $[0.027^\circ, 0.439^\circ]$ the bracketing is by a factor of ~13 in the lower direction, which mathematically still "brackets" the observed value but contradicts the qualifier "without fine-tuning" — needing $C_{a\gamma} \gtrsim 9$ when the natural range starts at 4 IS fine-tuning by a factor of $\gtrsim 2$. A theoretical reviewer reads this exactly the way GPT-B6 already read it once.

---

## MAJOR

### MAJ-1 — Table I row $n_s = 0.965 \pm 0.004$ disagrees with the on-disk full-tension JSON which reports $n_s = 0.9655 \pm 0.0062$; the displayed posterior uncertainty is ~55% narrower than the actual chain output

**Claim location**: Table~I ("verification" table), L306:
> $n_s$ & $0.965 \pm 0.004$ & $0.967 \pm 0.006$ \\\\

**On-disk evidence**: `research/final_paper_prep/full_tension_physical_parameters.json` (the JSON that anchors every other row of Table~I):
- `ns.mean` = 0.96548
- `ns.std` = 0.006184

Rounded to 3 sig fig: $n_s = 0.965 \pm 0.006$ (not $\pm 0.004$). The mean is consistent; **the σ is wrong by a factor of $0.006184/0.004 \approx 1.5$**.

Other rows in the same table cross-check to JSON cleanly:
- $H_0 = 67.68 \pm 1.06$ ✓ (JSON: 67.684 ± 1.061)
- $\Delta\Neff = -0.020 \pm 0.169$ ✓ (JSON: −0.0196 ± 0.1692)
- $\sigma_8 = 0.803 \pm 0.008$ ✓ (JSON: 0.8034 ± 0.0084)
- $S_8 = 0.814 \pm 0.008$ ✓ (JSON: 0.8141 ± 0.0085)
- $\Omega_m = 0.308 \pm 0.005$ ✓ (JSON: 0.3081 ± 0.0055)
- $\tau = 0.054 \pm 0.007$ ✓ (JSON: 0.0536 ± 0.0070)

Only the $n_s$ uncertainty row is anomalous.

**Defect rationale**: The full-tension chain has the SAME $n_s$ posterior width as Planck baseline cosmology (~0.006), since it's the high-$\ell$ Planck likelihood that drives the constraint. Reporting $\pm 0.004$ in this paper would mean the full-tension chain has *tighter* $n_s$ uncertainty than Planck's own analysis — that would be a notable finding, but the JSON says it isn't true. The Planck+BAO+SN column reports $\pm 0.006$ which is what the full-tension column should also show; an internal cross-check on the same paper that includes BAO + SN + H0 + S8 priors should NOT tighten $n_s$ relative to a strict subset (the priors target Hubble tension, not the scalar-tilt direction). This looks like a transcription error: someone copied "0.004" instead of "0.006" when filling in the table, or the table was prepared from a stale chain before the $n_s$ posterior fully converged.

**Severity = MAJOR**: load-bearing posterior in Table I, used for downstream cross-paper comparison. The σ is the parameter that determines whether the chain's $n_s$ is consistent with Planck-2018's reported $n_s = 0.9649 \pm 0.0042$ — at the displayed $\pm 0.004$ the two agree at 0.05σ (almost suspicious); at the true $\pm 0.006$ they agree at 0.1σ (more honest). The R25a brutal-honesty round didn't catch this because it focused on the sample-count headline; a theoretical-physics rigor round catches it because the first thing a cosmologist does with a parameter table is verify σ-widths against known Planck values.

### MAJ-2 — Conclusion §VIII NaMaster paragraph says "bias $\leq 0.032^\circ$" but the production summary.json reports bias = 0.040° at β = 0.342° injection; the larger of the two bias values is the one that should anchor the systematic floor

**Claim location**: Conclusions §VIII, L811:
> "the 500-MC pseudo-$C_\ell$ analysis on the Planck Commander map confirms that the deconvolution pipeline recovers injected birefringence angles with bias $\leq 0.032^\circ$"

The body text on L538–547 correctly states **both** bias values (0.032° at $\beta=0.27°$, 0.040° at $\beta=0.342°$) and explicitly says "the deconvolution is therefore unbiased at the $0.04^\circ$ level in the worst-case injection, which we carry forward as the NaMaster systematic floor". The conclusion is internally inconsistent with this body text.

**On-disk evidence**: `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json`:
- `beta_paper1.bias_deg` = 0.032 (at injection 0.27°)
- `beta_observed`: input 0.342°, recovered 0.302° → bias = 0.040°

**Defect rationale**: The conclusion paragraph cites the smaller of two bias values as if it were the controlling systematic, but the paper's own body text (and the R7 GEM-B2 / GPT-B4 closure block at L542–545) explicitly states the systematic floor is 0.040°, not 0.032°. The bias scales with injected amplitude — this is in fact a known and documented physical effect of $C_2$ apodized-mask EB leakage at $f_{\rm sky}=0.32$, where the relative pipeline bias is roughly amplitude-independent but the absolute bias scales mildly with the signal. Quoting the lower bias in the conclusion misrepresents the controlling systematic for a downstream user reading only the conclusion. The honest correction is `bias $\leq 0.040^\circ$` (the upper bound across both physically-relevant injections) OR `bias in the range $[0.032^\circ, 0.040^\circ]$ across injections $\beta \in [0.27^\circ, 0.342^\circ]$, scaling mildly with amplitude`.

**Severity = MAJOR**: load-bearing systematic-error claim in the Conclusion. The conclusion is the paragraph an external reader scans first; if it says 0.032° and the body says 0.040°, a peer-review round will flag the internal inconsistency. The fix is one word ("$\leq 0.040^\circ$" not "$\leq 0.032^\circ$" in the conclusion).

---

## minor

### MIN-1 — Frozen full-tension chain 6 contains 102,468 rows while chains 1–5 contain ~14,500–15,000 rows each (~7× imbalance); this is a yellow flag for Gelman-Rubin diagnostics which assume roughly equal-length chains

**Claim location**: implicit — the abstract claim of "frozen samples across two converged dataset combinations" anchored on `convergence_latest.csv` $\hat R$-1 < 3×10⁻³ assumes well-mixed chains of comparable lengths.

**On-disk evidence**: `wc -l` of `reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/chain_0*/spin_torsion.1.txt`:
- chain_01: 15,055
- chain_02: 14,818
- chain_03: 14,701
- chain_04: 14,671
- chain_05: 14,533
- chain_06: 102,468

Chain 6 is **6.7× longer than the median of chains 1–5**. The Gelman-Rubin statistic is defined for $M$ chains of equal length $N$; for unequal-length chains, the standard practice is either to (a) truncate to the shortest length before computing $\hat R$, or (b) use a length-weighted estimator and explicitly note the imbalance. The paper's footnote `fn:rhat_csv` cites $\hat R - 1 = 9.74\times 10^{-4}$ as the worst row without commenting on whether chain 6's outsized contribution biases the diagnostic.

**Defect rationale**: not a blocker — the chain 6 imbalance was already noted in R25a BLK-1 as part of the working-chain-dir discussion, but it's specifically a Gelman-Rubin-validity concern that R25a didn't separately call out. A theoretical-statistics reviewer would want a one-line footnote noting that the $\hat R$ values were computed on the length-balanced subset OR length-weighted, and that the chain 6 over-run does not bias the convergence diagnostic. This is a 1-sentence addition to footnote `fn:rhat_csv`, not a re-run.

**Severity = minor**: methodological-completeness item; doesn't change any reported posterior.

### MIN-2 — Conclusion abstract footnote at L818 quotes $C_{a\gamma}\,\Delta\phi/f_a \approx 10.3$ for $\beta = 0.342^\circ$ giving $C_{a\gamma}\in[9, 51]$ over $\Delta\phi/f_a\in[0.2, 1.1]$; the lower bound $C_{a\gamma}\sim 9$ requires $\Delta\phi/f_a = 1.1$ (the upper end of the displacement range)

**Claim location**: §VIII (Conclusions), L818:
> "$C_{a\gamma}\,\Delta\phi/f_a \approx 10.3$ for $\beta=0.342^\circ$, with $\Delta\phi/f_a$ in the natural range $[0.2,1.1]$ giving $C_{a\gamma}$ between $\sim 9$ and $\sim 51$"

**On-disk evidence**: arithmetic — to get $\beta = 0.342^\circ$ from $\beta = (\alpha/(4\pi)) C_{a\gamma} (\Delta\phi/f_a)$ with $\alpha/(4\pi) = 5.807\times 10^{-4}$:
- $C_{a\gamma}\,(\Delta\phi/f_a) = 0.342 \times \pi/180 / 5.807\times 10^{-4} = 10.28$ ✓
- For $\Delta\phi/f_a = 0.2$: $C_{a\gamma} = 51.4$ ✓
- For $\Delta\phi/f_a = 1.1$: $C_{a\gamma} = 9.3$ ✓

The arithmetic is correct, but the framing reads as if the "natural" parameter range is $C_{a\gamma}\in[9, 51]$, which is the *required* range for $\beta = 0.342°$ to be reproduced — not a separately-motivated natural range. The §VI body text on L644 (the buggy line in BLK-1) quotes a natural ALP-photon-coupling range of $C_{a\gamma}\in[4,12]$. The conclusion's "$[9, 51]$" is the intersection of "the model's natural range" with "the data". Stating it as "natural" without that qualifier is mildly misleading — $C_{a\gamma}=51$ is well outside the "natural" $[4,12]$ band.

**Defect rationale**: framing fix only — the conclusion should say "with $\Delta\phi/f_a$ in the natural range $[0.2,1.1]$ the **observationally required** $C_{a\gamma}$ ranges from $\sim 9$ (at the upper end of the displacement range) to $\sim 51$ (at the lower end), with the $\sim 9$ end matching the natural ALP-photon coupling range and the $\sim 51$ end requiring an enhanced coupling". This re-frames the bracket from "natural accommodation" to "accommodation requires the upper end of the natural coupling range AND the upper end of the displacement range simultaneously". Same numbers, more honest framing.

**Severity = minor**: framing/honesty cleanup; doesn't affect any numerical claim.

---

## Summary

**1 BLOCKER / 2 MAJOR / 2 minor / 0 nit on v1B.0.23**

The R25a brutal-honesty pass closed the load-bearing sample-count + R-hat-coverage defects but missed the **ALP-prediction arithmetic** that GPT-B6 had already independently flagged in a deferred item. The v1B.0.23 paper goes into round 2 with one BLOCKER that has now been independently detected by **two different cross-model rounds** (GPT-B6 then theoretical-physics-rotation), without being closed in the live body text.

Beyond the BLOCKER, two MAJOR findings:
- **MAJ-1**: Table I row $n_s = 0.965 \pm 0.004$ disagrees with the on-disk full-tension JSON (true σ = 0.006); the smaller σ would (incorrectly) make the chain look tighter than Planck's own n_s constraint.
- **MAJ-2**: Conclusion paragraph cites NaMaster bias $\leq 0.032°$ while the body text and on-disk summary.json carry the worst-case bias as 0.040°; one-word fix in the conclusion.

Streak status: round 1-of-3 returns 1 BLOCKER + 2 MAJOR + 2 minor; AGENT_RULES §4.4.1 cascaded-loop-exit NOT satisfied. Round 2 (different persona) and round 3 (different persona) on the v1B.0.24+ artifact still needed before P1B can pass the same exit criterion P1A satisfied. P1B remains capped at 95% per the readiness-oscillation memory directive.

— Internal Claude / theoretical-cosmologist persona, 2026-05-24
