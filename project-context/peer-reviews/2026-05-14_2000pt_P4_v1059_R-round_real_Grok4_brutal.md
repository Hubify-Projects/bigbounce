# P4_v1059 R-round — REAL cross-vendor — Grok-4 brutal-honesty reviewer

**Model**: `x-ai/grok-4` (via OpenRouter)
**Round**: 2026-05-14_2000pt
**Wall time**: 76.5s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=52453, completion=1034, total=53487

---

## PAPER-GRO-B1 (MAJOR): Abstract and Sec. I, sensitivity claims
Overclaim on sensitivity: Abstract touts "sub-percent" and "0.29% Fisher / 0.5% empirical" but conflates statistical-only Fisher floor (0.29% full-amplitude) with systematic-inclusive empirical (>0.5%), inflating perceived precision; narrative dodges that empirical floor is the operational limit, not the lower Fisher asymptote. Fix by explicitly stating in abstract and intro that primary sensitivity is the empirical >0.5% (systematic-inclusive), with 0.29% as zero-systematics ceiling only.

## PAPER-GRO-B2 (MAJOR): Sec. VIII.B and Sec. X, amplitude convention
Inconsistent amplitude definitions: Sensitivity section derives floors on half-modulation (A/2 ≈0.14-0.2%) but quotes full-A floors (0.29-0.4%) without clear disclosure until late; risks misleading readers comparing to Shamir's full-amplitude ~3%. Add explicit paragraph at Sec. VIII.B head clarifying full-A vs. half-modulation conventions, and propagate to all quoted floors with "full-amplitude" qualifier.

## PAPER-GRO-M1 (MAJOR): Sec. I and Sec. VII, 'first' and 'novel' framings
Dishonest 'first' claims: "First published multi-test bias hardening audit" ignores prior equivariance in Jia (2023) and bias checks in Iye (2020); "novel" catalog scale (1.6x Jia) is incremental, not unprecedented given Shamir's ~10^6 total galaxies. Remove 'first/novel/unprecedented' qualifiers; reframe as "largest spiral subsample with equivariant post-processing" without superlatives.

## PAPER-GRO-M2 (MAJOR): Sec. X, falsification criterion
False confidence in falsification: Proposed LSST Y3 criterion (dipole ≥0.1% at >5σ) is arbitrary and underestimates systematics; evades that own residual monopole (9.5σ) could project differently in deeper data. Strengthen by tying to own empirical floor (>0.5% at 3σ recovery), and add clause requiring independent bias audit passing equivalent 8-test suite.

## PAPER-GRO-m1 (minor): Sec. IX.H, SpArcFiRe cross-check
Overclaim on hypothesis test: SpArcFiRe null is called "strongest independent probe" but is only ~1.4e5 galaxies (partial), not decisive; "rules out" alternative is too strong for consistency evidence. Soften to "consistent with working hypothesis, disfavors alternative at overlap scale" and note scale limitation.

## PAPER-GRO-n1 (nit): Bibliography, arXiv IDs
Lingering bib issues: Shamir (2022) and Jia (2023) entries note removed bogus arXiv IDs but lack correct ones; pattern repeats prior errors (e.g., tick 14 Shamir:2022). Verify and insert actual arXiv IDs if existent, or explicitly state "no preprint available" in notes.
