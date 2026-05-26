# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-phase2-verify_P4_v1_0_131
**Wall time**: 97.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=100370, completion=7166, reasoning=6103, total=107536

---

## PAPER-GEM-M1: Table II $N_{MC}$ Contradictions [MAJOR]
**Section:** Table II (Data Vectors)
**Issue:** The newly added Table II contains $N_{MC}$ values that directly contradict the executed pipelines described in the main text. Row (i) lists $N_{MC}=500$, but Section IV.C and footnote 4 explicitly state $N_{MC}=10,000$ for the real-space dipole bootstrap. Row (vi) lists $N_{MC}=500 + 100/A$, but Section IX.J states $N_{MC,null}=1000$ and $N_{inj}=100$. 
**Fix:** Update Table II Row (i) to $N_{MC}=10,000$ and Row (vi) to $N_{MC,null}=1000, N_{inj}=100$ to match the canonical executed pipelines.

## PAPER-GEM-m2: Arithmetic Error in S4 Closure [minor]
**Section:** Table I, footnote (c)
**Issue:** The text claims that "doubling the per-bin Poisson $\sigma$ to account for the worst-case (an independent 21% chance of flip per galaxy) widens each hard-binned diagnostic by ~1.21x". This is mathematically incorrect. Adding the binomial variance of a 21.4% flip rate ($\sigma_{flip}^2 \approx 0.168N$) to the base Poisson variance ($0.25N$) yields a total variance of $\sim 0.418N$, which widens the standard deviation by $\sqrt{0.418/0.25} \approx 1.29\times$. 
**Fix:** Correct the arithmetic to: "adding the binomial variance of an independent 21.4% flip rate widens the empirical standard deviation by $\sim\!1.29\times$".

## PAPER-GEM-m3: Theoretical Physics - GR Projection Effects Cancellation [minor]
**Section:** Section IX.H (or Section IV.C)
**Issue:** The paper correctly utilizes the fractional asymmetry ratio $A_p = (N_{CW} - N_{CCW}) / (N_{CW} + N_{CCW})$ but misses a key theoretical strength: standard GR projection effects (magnification bias, redshift-space distortions) that modulate the total number density $N_{total}$ cancel out to first order in this ratio. This makes the chirality dipole theoretically cleaner than standard number-count dipoles.
**Fix:** Add a brief sentence noting that the fractional asymmetry observable $A_p$ is theoretically robust against standard GR projection effects (e.g., magnification bias, RSDs), which cancel to first order in the ratio.

## PAPER-GEM-m4: Theoretical Physics - EFT Operator Dimension [minor]
**Section:** Section IX.H, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Issue:** The text refers to "dimension-7 operators in the EFT of Inflation" citing Cabass et al. 2023. While defensible in pure derivative counting (1 time + 6 spatial = 7), the standard energy-dimension counting in the cited Cabass/Philcox/Liu literature classifies the leading ghost-free parity-odd scalar operators (e.g., $\dot{\pi}(\partial^2\pi)^3$) as dimension-8.
**Fix:** Change "dimension-7 operators" to "leading-order parity-odd scalar operators (e.g., dimension-8 in standard EFT counting)" to align perfectly with the nomenclature in the cited literature.

## PAPER-GEM-n5: Unformatted Editing Artifact [nit]
**Section:** Table I, footnote (c)
**Issue:** There is an unformatted editing artifact left in the text: `( scope restoration the mean-probability invariance \Delta p\!<\!0.0016 on two small holdouts is the load-bearing population diagnostic but does NOT close... )`.
**Fix:** Remove the unformatted "( scope restoration " prefix and integrate the sentence cleanly into the footnote prose.

## PAPER-GEM-n6: Mangled Sentence from Merge Conflict [nit]
**Section:** Section IV.C (paragraph 3) and Figure 6 Caption
**Issue:** A sentence appears to have been mangled during a text merge: "Under this three-discriminator framework not assigned a physical interpretation in this manuscript, not as a primordial signal; it supersedes the earlier analytic projection $+0.26\sigmaunit$, which is retained only as a methodological-comparison reference."
**Fix:** Rewrite for grammatical coherence, e.g., "Under this three-discriminator framework, the canonical-mask residual is not assigned a physical interpretation as a primordial signal; this empirical result supersedes the earlier analytic projection of $+0.26\sigmaunit$."
