# P4_v1093 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0030pt_P4_v1093_R12_R-round_real
**Wall time**: 127.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=81577, completion=8460, reasoning=6214, total=90037

---

# Review Findings

## PAPER-GPT-B1 — BLOCKER — MASTER / monopole-leakage conflation regressed

**Section:** Abstract; §Conclusions “Headline finding”; §NaMaster appendix.  
**Issue:** The paper still conflates different estimators/data vectors. The Conclusions say the raw pseudo-$C_\ell$ at $\ell=1$ “collaps[es] to $-0.12\sigma$ once MASTER … is applied on the same data,” but the $-0.12\sigma$ result uses a monopole-subtracted CW-deficit map on the $f_{\rm sky}=0.659$ subsample mask, while the 99.3% pre-MASTER leakage diagnostic uses an un-monopole-subtracted CW-fraction map on the canonical $f_{\rm sky}\simeq0.494$ mask. The abstract also says the asymmetry map has “zero monopole by construction,” which is false for $A_p=(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})$ unless an explicit mean subtraction is performed.  
**Fix:** Remove “same data” and state the full chain as map choice + monopole subtraction + mask choice + MASTER. If claiming a MASTER collapse, provide same-input pre/post MASTER numbers. Explicitly state whether $A_p$ is mean-subtracted; otherwise delete “zero monopole by construction.”

| Truth-audit item | Check | Verdict |
|---|---:|---|
| $A_p$ has zero monopole by construction | $A_p$ has nonzero mean if global CW fraction $\ne0.5$ | False as written |
| Pre-MASTER leakage map equals headline post-MASTER map | CW-fraction canonical un-subtracted vs CW-deficit subsample subtracted | False |
| $-0.12\sigma$ is canonical-mask post-MASTER result | Canonical direct-MC is $+1.85\sigma$ | False |

## PAPER-GPT-B2 — MAJOR — TTA “eliminates/by construction” overclaim remains

**Section:** §Future Directions; §Systematic Dipole; §Edge-On Galaxy Contamination.  
**Issue:** Remaining language says Catalog C “eliminate[s] handedness-dependent systematic biases by construction,” and §Systematic Dipole claims the soft chirality score $p_{\rm CW}^{\rm eq}-p_{\rm CCW}^{\rm eq}$ “averages to zero per galaxy.” Eq. (2) only enforces flip-equivariance of the two-pass protocol; it does not force per-galaxy CW=CCW, global hard-label balance, rotation invariance, or removal of training/depth bias.  
**Fix:** Replace all “eliminate/by construction/zero per galaxy” language with “enforces horizontal-flip equivariance at the soft-probability protocol level.” Keep the residual $9.5\sigma$ monopole, 1.35% $D_4$ argmax shift, and 21% argmax-flip rate as explicit non-cancellation evidence.

| Truth-audit item | Check | Verdict |
|---|---:|---|
| Eq. (2) implies $p_{\rm CW}^{\rm eq}=p_{\rm CCW}^{\rm eq}$ per galaxy | Difference remains generally nonzero | False |
| Catalog C eliminates handedness systematics by construction | Residual monopole and $D_4$ shifts are measured | False |
| TTA guarantee is only horizontal-flip equivariance | Supported by Eq. (2) | True |

## PAPER-GPT-B3 — MAJOR — 0.75% Fisher-floor reframe not fully propagated; dilution arithmetic wrong

**Section:** Introduction; §Pre-Registered Analysis Hierarchy; §Sensitivity; §Conclusions item 1.  
**Issue:** Body text still frames the $A\simeq0.75\%$ threshold as a “systematic-inclusive” experiment sensitivity in proximity to the full $3.2$M catalog, instead of consistently stating it is measured on the $N=471{,}049$ HC-spiral subsample. The GZ1 dilution calculation is also arithmetically wrong: if agreement implies dilution $1-2\varepsilon\simeq0.63$, a measured 0.75% threshold corresponds to a true amplitude $\sim0.75/0.63=1.19\%$, not $\sim0.79\%$. Conclusions also say $P(\sigma>3)=0.50$ at $A=0.75\%$ while Table IX gives 0.55.  
**Fix:** Everywhere 0.75% appears, append “on the $N=471{,}049$ HC-spiral subsample.” Delete “systematic-inclusive full-catalog” implications. Correct dilution arithmetic or remove the dilution reinterpretation. Use 0.55 consistently.

| Truth-audit item | Check | Verdict |
|---|---:|---|
| 0.75% threshold measured on full 3.2M catalog | Injection table uses $N=471{,}049$ HC spirals | False |
| 0.75% tracks HC Fisher floor | $3\sqrt{3/471049}=0.76\%$ | True |
| Diluted true amplitude from 0.75% with factor 0.63 | $0.75/0.63=1.19\%$ | Paper’s 0.79% false |
| $P(\sigma>3)$ at 0.75% | Table gives 0.55 | Conclusions 0.50 inconsistent |

## PAPER-GPT-B4 — MAJOR — Hemisphere LEE treatment is internally contradictory

**Section:** §Hemisphere Asymmetry; Fig. hemisphere caption; §Hemisphere Discussion; Abstract.  
**Issue:** The main text says the 3.05σ hemisphere maximum “does not survive” LEE and drops to $<1\sigma$ after Bonferroni/BH, but the direct max-statistic MC gives zero exceedances in 10,000 shuffles, $p_{\rm LEE}\le10^{-4}$, i.e. rejection of the random-label max-null. The paper alternates between calling the Bonferroni result conservative null consistency and calling the direct MC primary; these are different nulls/statistics and cannot be merged into one significance statement.  
**Fix:** Make the direct max-statistic MC the primary LEE result for the random-label null: “random-label max-null rejected at $p\le10^{-4}$.” Then state separately that this is not cosmological because the null omits depth/mask-edge systematics. Demote Bonferroni/BH to a historical/parametric cross-check or remove it.

| Truth-audit item | Check | Verdict |
|---|---:|---|
| Bonferroni across 650 directions gives $<1\sigma$ | Local 3.05σ with trials factor can do this | True under different parametric approximation |
| Direct MC max-statistic gives $p_{\rm LEE}\le10^{-4}$ | Zero/10,000 exceedances | True |
| Both imply “consistent with null” | Direct MC rejects random-label null | False |
| Direct MC and Bonferroni are directly comparable | Different statistics/null assumptions | False |

## PAPER-GPT-B5 — MAJOR — HC-bin 4,758-galaxy discrepancy is not explained

**Section:** Table “Confidence-stratified dipole” footnote; §Confidence; §Bin-by-bin CW flatness.  
**Issue:** The footnote attributes the 4,758-galaxy gap to boundary handling, but the predicates are not equivalent: the table bins use $\max(p_{\rm CW,eq},p_{\rm CCW,eq})$, while the cited canonical cut is described as `abs(p_cw_eq)>0.6` / “HC-spiral p>0.6” in different places. Boundary cases at exactly 0.6 or 1.0 are not a credible explanation without counts, especially for a 4,758-object gap.  
**Fix:** Define one canonical HC-spiral predicate and use it everywhere. Add exact reconciliation counts for: $>0.6$, $\ge0.6$, exact $p=0.6$, exact $p=1.0$, and any missing/NaN rows. Do not call this boundary-only unless the artifact proves it.

| Truth-audit item | Check | Verdict |
|---|---:|---|
| Table HC bins sum | 193,560 + 131,364 + 619,902 = 944,826 | True |
| Canonical HC-spiral count | 949,584 | True |
| Difference | 4,758 | True |
| Boundary handling alone demonstrated | No exact-boundary counts shown | Not demonstrated |
| `abs(p_cw_eq)>0.6` equals max-CW/CCW confidence cut | Not generally | False |

## PAPER-GPT-B6 — minor — Residual text/citation regressions remain

**Section:** §Training; §Comparison with Previous Work; §Conclusions.  
**Issue:** There is still a broken sentence splice in §Training: “the observed 1.2 pp gap falls within this … range that the observed 1.2 pp gap falls within… assumption, consistent with…”. Shamir DESI sample-size language is also inconsistent: the paper alternates between “nearly $1.3\times10^6$ spiral galaxies,” “$\sim200{,}000$ galaxies classified as spiral out of $\sim1.3$M total,” and the bibliography note saying not all 1.3M are spirals. Conclusions also regress to “prior literature did not subtract,” contradicting the intended softer “complements prior nulls” framing.  
**Fix:** Rewrite the malformed training paragraph. Pick one Shamir count convention and use it consistently; if 1.3M is total galaxies, do not call it the spiral sample. Replace “prior literature did not subtract” with “this pipeline demonstrates a leakage channel that may affect uncorrected pre-MASTER analyses; matched-pipeline work is needed.”

| Truth-audit item | Check | Verdict |
|---|---:|---|
| §Training sentence is grammatical | Contains duplicated clause and dangling “assumption” | False |
| Shamir DESI count used consistently | 1.3M spirals vs 200k spirals vs 1.3M total | False |
| Conclusion wording matches softened caveat | “prior literature did not subtract” remains | False |
