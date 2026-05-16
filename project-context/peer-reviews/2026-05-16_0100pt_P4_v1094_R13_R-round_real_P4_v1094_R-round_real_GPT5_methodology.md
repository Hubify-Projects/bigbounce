# P4_v1094 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0100pt_P4_v1094_R13_R-round_real
**Wall time**: 113.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=81609, completion=7441, reasoning=5681, total=89050

---

No BLOCKER-grade findings. Not ready for external Houston-shared review: 5 MAJORs remain, including a convergence-regression in the leakage/Master wording and arithmetic/provenance contradictions in the injection sweep.

## PAPER-GPT-M1 — MAJOR — Conclusions / NaMaster appendix

**Issue:** The Conclusions reintroduce the false “same data” collapse: “inflates the raw pseudo-\(C_\ell\) at \(\ell=1\), collapsing to \(-0.12\sigma\) once MASTER … is applied on the same data.” This is not same data: the pre-MASTER leakage diagnostic uses the canonical mask, un-monopole-subtracted CW-fraction map; the \(-0.12\sigma\) headline uses a subsample/superset mask, monopole-subtracted CW-deficit map, different apodization/null treatment. The appendix also says input-field choice is the “only methodological difference,” but mask/apodization/null differ too.

| Truth audit | Result |
|---|---|
| Checked claim | “Same data” / pure MASTER collapse to \(-0.12\sigma\). |
| Evidence | Abstract correctly says map choice + monopole subtraction + mask choice + MASTER; Conclusions/appendix contradict it. |
| Verdict | False regression of a previously closed issue. |

**Fix:** Replace with: “the full chain changes map definition, monopole treatment, mask, and MASTER inversion; canonical post-MASTER is \(+1.85\sigma\), while the subsample-mask headline is \(-0.12\sigma\).” Remove “same data” and “only methodological difference.”

## PAPER-GPT-M2 — MAJOR — §IX.A Systematic dipole / §IX.D Edge-on contamination

**Issue:** Residual TTA overclaim remains. The text says TTA makes the soft-weighted chirality score \(p_{\rm CW}^{\rm eq}-p_{\rm CCW}^{\rm eq}\) “average to zero per galaxy,” and edge-on disks get “exactly equal CW and CCW probabilities.” Eq. (2) only guarantees flip-swap equivariance of the protocol; it does not imply per-galaxy equality or zero chirality score.

| Truth audit | Result |
|---|---|
| Checked claim | TTA forces per-galaxy zero/equal CW–CCW probabilities. |
| Evidence | Eq. (2): \(p_{\rm CW}^{eq}-p_{\rm CCW}^{eq}=\frac12[(p_{\rm CW}^{orig}-p_{\rm CCW}^{orig})-(p_{\rm CW}^{flip}-p_{\rm CCW}^{flip})]\), not identically zero. |
| Verdict | False; contradicts the paper’s own \(p_{\rm CW}=0.4974\), \(D_4\) argmax shift, and 21% flip-rate caveats. |

**Fix:** State only that TTA enforces output-level flip-equivariance/mirror-swap consistency. Delete “zero per galaxy,” “exactly equal,” and any “eliminates” wording except for the horizontal-flip protocol symmetry.

## PAPER-GPT-M3 — MAJOR — §IX.C Sensitivity / Table injection sweep

**Issue:** Injection-recovery provenance is internally inconsistent. The prose says \(N_{\rm inj}=100\) axes and \(N_{\rm MC}=500\); Table caption says \(N_{\rm inj}=100\), \(N_{\rm MC,null}=1000\); later prose says “450,000 dipole fits (50 fits × 9 amplitudes × 1000 MC)” and “every one of the 500 injections.” These cannot all be true. Conclusions also quote \(P(\sigma>3)=0.50\) at \(A=0.75\%\), while Table gives 0.55.

| Truth audit | Result |
|---|---|
| Checked claim | Exact MC design for load-bearing \(0.75\%\) empirical threshold. |
| Evidence | 100 axes × 9 amplitudes = 900 injections, not 500; 500 vs 1000 null MC conflicts; 0.50 vs 0.55 conflicts. |
| Verdict | Arithmetic/provenance failure in the sensitivity result. |

**Fix:** Make one canonical statement: exact amplitudes, exact axes per amplitude, exact null realizations per injection, exact total fits, exact artifact filename, and binomial uncertainty on \(P(\sigma>3)\) (e.g. \(55/100\pm5\%\)).

## PAPER-GPT-M4 — MAJOR — §VI.H Hemisphere asymmetry / Fig. hemisphere / §IX.B

**Issue:** The LEE framing remains statistically contradictory. The text says the \(3.05\sigma\) hemisphere peak “does not survive” LEE and becomes \(<1\sigma\), then the direct max-statistic MC gives \(p_{\rm LEE}\le10^{-4}\), which is a post-LEE rejection of the random-label null, not a tightening of the Bonferroni/BH null conclusion.

| Truth audit | Result |
|---|---|
| Checked claim | Bonferroni/BH \(<1\sigma\) and direct MC \(p_{\rm LEE}\le10^{-4}\) are compatible LEE conclusions. |
| Evidence | Direct MC is the actual max-over-directions statistic under the random-label null; zero/10,000 exceedances implies rejection, not null consistency. |
| Verdict | Overclaimed reconciliation; nulls/test statistics are being mixed. |

**Fix:** Say: “The direct random-label max-statistic rejects the random-label null at \(p_{\rm LEE}\le10^{-4}\). We do not interpret this as primordial because the null does not preserve depth/mask-edge/morphology systematics; a systematics-preserving null is deferred.” Remove “does not survive LEE” unless explicitly restricted to the conservative analytic local-test approximation.

## PAPER-GPT-M5 — MAJOR — §IX.C Sensitivity derivation / Conclusions / comparison prose

**Issue:** The half-amplitude/full-amplitude correction is only partially propagated. The paper still calls \(0.2\%\) a “minimum detectable dipole” or “statistical floor” without consistently saying it is the CW-fraction half-modulation or a conservative half-amplitude proxy. Full-amplitude numbers should be \(0.29\%\) Fisher ideal, \(\sim0.4\%\) conservative with mask/\(N_{\rm eff}\), and \(0.75\%\) empirical on the HC subsample.

| Truth audit | Result |
|---|---|
| Checked claim | \(0.2\%\) as dipole amplitude sensitivity. |
| Evidence | Correct formula gives \(3\sqrt{3/N}=0.29\%\) full amplitude for \(N=3.201\)M; \(0.14\%{-}0.2\%\) is half-modulation language. |
| Verdict | Stale factor-of-two ambiguity remains and can overstate sensitivity. |

**Fix:** Globally replace “\(0.2\%\) minimum detectable dipole” with “\(0.2\%\) half-modulation statistical proxy” or delete it. Use full-amplitude convention everywhere in abstract/conclusions: \(0.29\%\) ideal Fisher, \(\sim0.4\%\) conservative Fisher, \(0.75\%\) empirical HC threshold.

## PAPER-GPT-n1 — nit — §III.C Training paragraph

**Issue:** Broken sentence splice: “the observed \(1.2\) pp gap falls within this \([1.118,1.5]\) pp range that the observed \(1.2\) pp gap falls within… assumption, consistent with…” This is grammatically broken and duplicated.

| Truth audit | Result |
|---|---|
| Checked claim | Sentence parses. |
| Evidence | Dangling “assumption” and repeated clause. |
| Verdict | Broken prose. |

**Fix:** Replace with: “The observed \(1.2\) pp gap lies within the \(1.12\)–\(1.5\) pp range spanned by quadrature and direct addition. We do not estimate the cross-correlation \(\rho\); the data are only consistent with comparable, non-independent contributions.”
