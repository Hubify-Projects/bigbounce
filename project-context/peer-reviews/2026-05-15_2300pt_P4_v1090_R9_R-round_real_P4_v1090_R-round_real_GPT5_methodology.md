# P4_v1090 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2300pt_P4_v1090_R9_R-round_real
**Wall time**: 97.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=80316, completion=6955, reasoning=4926, total=87271

---

No source line numbers were supplied; section anchors used.

## PAPER-GPT-B1 — BLOCKER — $\ell_{\rm eff}=4$ bandpower is still mis-described as the $\ell=1$ dipole/C1 result

| Field | Audit |
|---|---|
| Section | §Results → Dipole Analysis; §Conclusions |
| Paper says | “After deconvolution, the lowest bandpower (centered at $\ell_{\rm eff}=4$, spanning $\ell\in[2,6]$ … used here as the dipole estimator following the standard pseudo-$C_\ell$ convention for cut-sky $\ell=1$ recovery) is $C_1^{\rm meas}=1.494\times10^{-6}$ …” |
| Paper also says | “the reported MASTER $\ell=1$ result is the single-multipole bin … NOT a bandpower over a range”; Table III footnote: “$\ell_{\rm eff}=4$ … does not include $\ell=1$.” |
| Verdict | REGRESSION |
| Issue | The manuscript still equates the $\ell_{\rm eff}=4$ bandpower over $[2,6]$ with the $\ell=1$ dipole estimator and labels it $C_1$. This directly contradicts the appendix and Table III footnote. The Conclusions also say the leakage “inflates the raw pseudo-$C_\ell$ at $\ell=1$, collapsing to $-0.12\sigma$ once MASTER … is applied on the same data,” but the paper elsewhere states the pre/post values differ in map, monopole subtraction, mask, and MASTER treatment. |
| Fix | Delete the “used here as the dipole estimator…” sentence and any $C_1$ notation attached to the $[2,6]$ bandpower. State only: single-$\ell=1$ MASTER gives $-0.12\sigma$; $\ell_{\rm eff}=4$ is a separate non-dipole bandpower/systematics diagnostic. |

## PAPER-GPT-B2 — BLOCKER — 0.5% sensitivity-floor regression remains, plus numerical drift at $A=0.5\%$

| Field | Audit |
|---|---|
| Section | §Sensitivity; §Conclusions item 1; §Data Availability; §Parity translation |
| Paper says | “The empirical MC floor of $\geq0.5\%$ is the detection threshold…” |
| Paper says | “we achieve a conservative empirical $50\%$-recovery-$3\sigma$ threshold of $\sim0.5\%$…” |
| Paper says | “at $A=0.5\%$ the per-pixel-shuffle MC gives only $P(\sigma>3)=0.03$…” |
| Artifact/table says | Table `injection_recovery_extended.json`: $A=0.50\%$: $P(\sigma>3)=0.15$; $A=0.75\%$: $P(\sigma>3)=0.55$. |
| Verdict | REGRESSION |
| Issue | The paper still calls 0.5% an empirical floor/detection threshold in multiple places, despite the extended sweep showing non-detection at 0.5% and first 50%-recovery-at-3σ at 0.75%. It also quotes $P(\sigma>3)=0.03$ at 0.5%, inconsistent with the table’s 0.15. |
| Fix | Replace every “$\gtrsim0.5\%$ empirical floor/detection threshold” with “$\approx0.75\%$ empirical 50%-recovery-at-3σ threshold”; reserve 0.5% only as a tested non-detection point with $P(\sigma>3)=0.15$. |

## PAPER-GPT-M1 — MAJOR — Hemisphere look-elsewhere treatment is statistically incoherent

| Field | Audit |
|---|---|
| Section | §Hemisphere Asymmetry; Fig. hemisphere caption; §Hemisphere discussion |
| Paper says | “Bonferroni … reduces the effective significance to $<1\sigma$.” |
| Paper says | “zero of $N_{\rm MC}=10{,}000$ label-shuffle nulls … giving $p_{\rm LEE}\le10^{-4}$ … direct-MC look-elsewhere null is therefore in the tail…” |
| Paper says | “The two corrections refer to different test procedures … We treat the multiplicity-corrected $<1\sigma$ as the conservative null-consistency statement, while noting that the random-label null IS rejected…” |
| Verdict | STILL-UNRESOLVED |
| Issue | The direct max-over-directions MC is the relevant LEE calibration for the random-label null; if it gives $p_{\rm LEE}\le10^{-4}$, the same random-label null cannot simultaneously be summarized as “$<1\sigma$ consistent with null.” The text mixes a local-grid Bonferroni calculation and a max-statistic MC as if both can support opposite verdicts. |
| Fix | Pick one primary null. If random-label is primary, state “hemisphere max rejects random-label null; likely systematics because systematics-preserving null absent.” If systematics-inclusive null is primary, compute it and stop using the Bonferroni $<1\sigma$ claim as evidence. |

## PAPER-GPT-M2 — MAJOR — Table III z-scores are not reproducible from the reported columns

| Field | Audit |
|---|---|
| Section | Table III / `tab:multipole` |
| Paper says | $\ell_{\rm eff}=4$: $C_\ell=3.210$, $\sigma_{\rm null}=0.804$, significance $+6.097$ |
| Paper says | $\ell_{\rm eff}=9$: $C_\ell=-0.248$, $\sigma_{\rm null}=0.574$, significance $+2.232$ |
| Artifact/table should say | $z=(C_{\ell}^{\rm meas}-\langle C_{\ell}^{\rm null}\rangle)/\sigma_{\ell}^{\rm null}$, requiring the null mean. |
| Verdict | NOVEL |
| Issue | The table omits the null mean, so the quoted z-scores cannot be audited. Worse, $3.210/0.804=3.99$, not 6.097, and negative measured bandpowers with positive z-scores imply large negative null means that are not reported. |
| Fix | Add a null-mean column for every row and recompute all z-scores visibly from `(data-null_mean)/null_std`. Also fix the caption’s “rows 2--5” wording because the table has five non-dipole bandpower rows. |

## PAPER-GPT-M3 — MAJOR — High-confidence sample definitions and counts are internally inconsistent

| Field | Audit |
|---|---|
| Section | §Sensitivity; §Edge-on robustness; §Bin flatness; Table face-on |
| Paper says | Injection recovery uses “HC-spiral” with $p_{\rm eq}>0.9$, $n=471{,}049$. |
| Paper says | Face-on robustness uses “HC-spiral ($p_{\rm eq}>0.6$)”, $n=949{,}584$. |
| Paper says | Bin-flatness “HC-broad: $n=949{,}584$, $\max(p_{\rm CW,eq},p_{\rm CCW,eq},p_{\rm NS,eq})>0.6$ … includes confident-NS galaxies.” |
| Artifact/table says | Table face-on: HC-spiral $p_{\rm eq}>0.6$ has $N_{\rm spiral}=949{,}584$. |
| Verdict | STILL-UNRESOLVED |
| Issue | The same $n=949{,}584$ is assigned to incompatible cuts: spiral-only $\max(p_{\rm CW},p_{\rm CCW})>0.6$ and broad all-class $\max(p_{\rm CW},p_{\rm CCW},p_{\rm NS})>0.6$ including NS galaxies. Those cannot both be the same denominator. |
| Fix | Define immutable sample labels: HC-spiral-0.9, HC-spiral-0.6, HC-broad-0.6. Recompute/report exact counts for each and ensure `face_on_robustness_results.json` and `face_on_isotropic_null_results.json` use the same cut. |

## PAPER-GPT-m1 — minor — “polar-vector direction” wording remains and contradicts the axial-vector correction

| Field | Audit |
|---|---|
| Section | §Dipole symmetry caveat / §Parity translation |
| Paper says | “A nonzero chirality dipole therefore strictly tests isotropy (the existence of a preferred polar-vector direction on the sky)…” |
| Paper also says | “the dipole vector itself is an axial vector, not a polar vector…” |
| Verdict | REGRESSION |
| Issue | The remaining “polar-vector direction” phrase reintroduces the axial/polar confusion. For projected spin chirality, $\vec L$ is axial and $\vec L\cdot\hat n$ is a pseudoscalar; the fitted dipole coefficient is parity-even/axial, not polar. |
| Fix | Replace “preferred polar-vector direction” with “preferred axis / axial-vector spin-projection direction”; reserve “polar” only for the line-of-sight vector $\hat n$. |
