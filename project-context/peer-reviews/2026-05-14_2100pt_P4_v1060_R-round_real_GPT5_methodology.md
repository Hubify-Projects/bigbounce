# P4_v1060 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_2100pt
**Wall time**: 49.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=57636, completion=2817, total=60453

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR — Abstract; Sec. “Sensitivity Floor”; Conclusions item 1

Concrete issue: Empirical sensitivity is still overstated/inconsistent. Injection recovery only tests up to \(A=0.5\%\) and gives \(P(\sigma>2)=0.18\), with no demonstrated \(P(\sigma>3)\) or 50% recovery; yet multiple places say “\(\sim0.5\%\) at \(3\sigma\)” or “50%-recovery threshold.” The full-amplitude Fisher floor also oscillates between \(\sim0.29\%\), \(\sim0.4\%\), and “\(\lesssim0.2\%\).”

Fix: State strictly: empirical 50%-recovery threshold is \(>0.5\%\) under the tested grid; no \(3\sigma\) recovery threshold is measured. Use one amplitude convention everywhere: \(A/2\) floor vs full \(A\) floor.

## PAPER-GPT-M2 — MAJOR — Sec. “Dipole Analysis”; Table III; Conclusions “Canonical-\(N\) MASTER projection”

Concrete issue: The load-bearing MASTER \(\ell=1\) result is not a direct canonical Catalog-C single-mode run. It is anchored to an analysis subsample/mask and then analytically projected to canonical \(N_{\rm spiral}=3{,}201{,}160\), \(f_{\rm sky}=0.491\) under declared approximations. Calling this “canonical-primary” is stronger than the computation supports.

Fix: Either run the direct canonical single-mode NaMaster \(\ell=1\) MC and replace the projection, or demote the result to “subsample-mask MASTER null plus analytic canonical projection cross-check.”

## PAPER-GPT-M3 — MAJOR — Sec. “Angular power spectrum”; Table III; Fig. multipoles caption

Concrete issue: The text says “all higher multipoles are consistent with null,” but Table III reports \(\ell_{\rm eff}=4\) at \(+6.097\sigma\) and joint \(\chi^2/{\rm dof}=161.2/38=4.24\). Labeling these as “mask-coupled monopole leakage” may be plausible, but they are not null-consistent residuals.

Fix: Remove “all higher multipoles are null.” Explicitly state the map fails a naive low-\(\ell\) null due to residual monopole/mask leakage, and propagate this leakage into the systematic covariance or restrict the claim to the isolated \(\ell=1\) estimator.

## PAPER-GPT-M4 — MAJOR — Sec. “Hemisphere Asymmetry”; Sec. “The 3.05σ Hemisphere Signal”

Concrete issue: The LEE treatment is internally contradictory. Bonferroni/BH is said to reduce the signal to \(<1\sigma\), while direct MC gives \(p_{\rm LEE}\le10^{-4}\) and “tightens” the conclusion; these are opposite verdicts under different nulls. The hemisphere amplitude convention is also unclear: half-difference \(0.17\%\) is reported as full \(A=0.853\%\), which does not follow transparently from \(p_{\rm CW}=\tfrac12(1+A\cos\theta)\).

Fix: Pick the operative null and report the other only as non-load-bearing. Add a depth/mask-preserving null for the max-statistic, and derive the hemisphere half-difference-to-\(A\) conversion explicitly.

## PAPER-GPT-M5 — MAJOR — Table “Sky Region Balance”; Abstract Shamir comparator; Conclusions item 2

Concrete issue: The maximum regional asymmetry \(0.32\%\) and Shamir amplitude-ratio claim rely on a superseded sky-balance snapshot with \(N_{\rm spiral}=3{,}321{,}795\), not the canonical \(3{,}201{,}160\). The canonical row “inherits” fractions without recomputing per-region counts/labels.

Fix: Recompute all seven regional CW fractions on the canonical Catalog-C sample and use only those values for the \(0.32\%\) maximum and Shamir ratio. If not recomputed, mark the regional comparison as provisional.

## PAPER-GPT-m1 — minor — Sec. “Systematic dipole”; Sec. “Test-Time Equivariant Averaging”

Concrete issue: The paper still overstates TTA as eliminating bias “by construction” and canceling residual bias “to machine precision.” That is true only for soft flip-symmetrized probabilities under the horizontal reflection operation, not for hard argmax labels, NS gating, rotations, morphology coupling, or the observed \(9.5\sigma\) monopole.

Fix: Replace “eliminates” with “suppresses the horizontal-flip component in soft outputs.” State that hard-label chirality balance is empirical, not guaranteed.
