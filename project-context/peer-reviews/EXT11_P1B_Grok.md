# EXT11 Harvest — P1B — Grok

- Provider: Grok
- Model/Effort: Heavy (Team of Experts)
- Chat URL: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=6fede933-742f-423b-b1d8-bbbf7254d6c1
- PDF md5: 03c33444 (paper1b_mcmc_companion_v1B.0.70_03c33444.pdf)
- Harvested: 2026-06-13 17:06 PDT

---

## Headline Verdict: ACCEPT

All MINOR items flagged in the previous round (EXT10) have been addressed with precise, one-sentence closures. The new ALP dark-energy fraction Ω_a subsection (p. 13, Eqs. (6)–(9)) is a clear improvement that directly resolves the derivation concern raised by multiple reviewers. No scientific rework, no new load-bearing gaps, and no substantive changes to any of the four specifically scrutinized elements. The manuscript now meets the highest standards for a reproducibility-focused companion paper and is ready for publication.

## Items from EXT10 Still Open

None. All six targeted fixes (pairing-swap note, 40.5 H₀ clarification, phantom-crossing wording, UV-completion sentence, release-pairing language, bias-floor terminology) are cleanly implemented.

## New Items Introduced by Closures (all minor/polish — can be handled in proof stage)

- **p. 13 (new Ω_a subsection):** The H₀ note (E8) + marginalization test sentence is excellent but could be tightened into a single parenthetical to avoid minor local repetition with the earlier fixed-H₀ usage (pure flow preference).
- **Conclusions p. 14:** LiteBIRD ~9σ phrasing remains correctly scoped (null vs. model-separation distinguished).
- **Housekeeping (Data/Code section + CHANGELOG):** v1B.0.70 stamp and b22f8cc9 commit are noted; insert pending DOIs/Zenodo identifiers at final production (already flagged as "pending at submission" — acceptable).

These are trivial production items only; no blockers or majors remain.

## Specific Scrutiny (all fully satisfied — in fact strengthened)

- **309,189 MCMC samples:** Reconciliation footnotes, independent c15 re-run (0.04σ agreement), committed artifacts, and release-pairing caveat all unchanged and robust.
- **ΔN_eff ≈ 0 (+0.058±0.179 Planck+BAO+SN):** Null-consistency framing, one-sided limits, BBN-consistent defaults, and Liu et al. cross-check identical; the new independent-pod verification reinforces the result.
- **NaMaster 500-MC at SNR=20.32σ:** "Observed pipeline bias" terminology now explicit; robustness battery, synthetic-sky scope, and non-sky-detection disclaimers unchanged and exemplary.
- **Spectator-ALP carve-out (f_a ~ M_Pl, m ~ H₀ regime):** The new dedicated Ω_a subsection (with explicit Eqs. (6)–(9), per-step computation, 13% mass for Ω_a < 0.01, 40.5 H₀ median note, and 25× θ_i tuning) makes the spectator-safe restriction bulletproof.

The manuscript requires no further scientific revisions. Recommend immediate acceptance.

*Signed: External Referee, 13 June 2026*
