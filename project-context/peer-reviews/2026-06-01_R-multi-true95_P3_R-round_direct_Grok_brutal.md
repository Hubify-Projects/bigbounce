# P3 R-round — DIRECT vendor — Grok-4 brutal-honesty reviewer

**Model**: `grok-4` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 15.8s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=70812, completion=761, total=72195, prompt_details={'text_tokens': 70812, 'audio_tokens': 0, 'image_tokens': 0, 'cached_tokens': 128}, completion_details={'reasoning_tokens': 622, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, num_sources_used=0, cost_in_usd_ticks=918381000

---

**## PAPER-GRO-B1 (BLOCKER) — Abstract + §5 (lines ~80-140)**

The abstract and §5 headline a “central 7.9 % improvement” in \(\sigma(f_{\rm NL})\) while simultaneously stating the result is consistent with null at \(<1\sigma\) and that the linear-extrapolation form yielding that number has been RETRACTED for violating Fisher positivity. The load-bearing claim is therefore the null result, not the improvement.

**Fix:** Replace the 7.9 % sentence with a single declarative statement that the empirical-\(\alpha\) forecast is statistically indistinguishable from the single-tracer baseline at the present precision; move all numerical envelopes to the caveats section.

**## PAPER-GRO-B2 (BLOCKER) — Title + Abstract (first paragraph)**

Title and abstract assert “largest-scale … to date” and “first multi-survey” framing. The paper itself qualifies both claims (141× vs Liang+2023 is scope expansion + native retrain, not like-for-like; seven prior single-survey autoencoder papers exist). The framing is therefore false advertising.

**Fix:** Change title to “A 378 k-object multi-survey anomaly catalog from seven archives with native-retrained autoencoders” and remove “first”/“largest” adjectives from the abstract.

**## PAPER-GRO-B3 (BLOCKER) — §5 + §pathc_caveats (i,j) + conclusions item 5**

All Fisher forecasts rest on two anchor points plus an empirical \(\alpha^2\) Taylor expansion whose coefficient is never re-fit on a 5-point grid in the released text; the 5-grid refit is declared “CLOSED” only by reference to an unreleased artifact. The positivity-respecting envelope is therefore an unverified modeling choice, not a demonstrated result.

**Fix:** Either publish the 5-point Fisher table in the main text or retract the numerical \(\sigma(f_{\rm NL})\) forecasts entirely and report only the \(\alpha\) measurement.

**## PAPER-GRO-M1 (MAJOR) — §pathc_caveats (a) + §crossmatches (lines ~650-670)**

The 9 576 intra-survey duplicate count is asserted to be resolved by an on-disk union-find artifact. No table or pseudocode shows how the friends-of-friends pass distinguishes intra- from inter-survey clusters at 5″; the arithmetic is therefore unverifiable from the paper alone.

**Fix:** Add a one-paragraph methods subsection giving the exact union-find parameters and a small worked example of one intra-survey collapse.

**## PAPER-GRO-M2 (MAJOR) — §nanograv + Appendix D**

The Savage-Dickey factors are presented as decisive, yet the likelihood construction (independent per-bin KDE factors) and the choice of 1-D vs 2-D priors are not varied. The “decisive” language therefore overstates robustness.

**Fix:** Report only the numerical Bayes factors with a one-sentence caveat that they are conditional on the Ceffyl KDE product and the chosen log10A prior; remove Jeffreys-scale adjectives.

**## PAPER-GRO-M3 (MAJOR) — Abstract + §simbad (lines ~300-320)**

The 17.8 % genuine-novelty figure is a single top-1 000 point estimate whose uncertainty is never quantified and whose extrapolation to the full catalog is explicitly disclaimed. Presenting it as the discovery-rate headline is therefore unsupported.

**Fix:** Move the 17.8 % sentence into the limitations paragraph and state only that the top-1 000 stratum shows 17.8 % objects absent from the 20-catalog cross-match.
