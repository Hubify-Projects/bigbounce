# P2 M23-EXT truth-audit (vs byte-unchanged v1.7.116)

Raws read verbatim before any verdict: `P2_grok_M23.md` (MAJOR, 3M/2m),
`P2_chatgpt_M23.md` (REJECT, 9M/2m). ledger_match.py drafts + full §3 manual
truth-audit vs `research/focused_paper_source_integration/02_full_draft.tex`
+ `DISPOSITIONS/P2.md`.

**Verdict: 0 genuinely-new real+editable findings. Every finding is a
source-cited re-flag of a standing DP2 D-id. clean-wave streak 9→10; cap 68 HOLDS.**

## Grok (MAJOR) — 3 MAJOR + 2 MINOR
1. **[MAJOR] headline ~2.6–2.75σ / 1.3–2.75σ = single-source Heinrich recast, framing
   overstates independence** → **DP2-04 + DP2-17** (recast-not-independent-forecast
   disclosed verbatim, abstract Scope L888 + scope-summary (i) L1512; envelope
   subordinated). Re-flag.
2. **[MAJOR] −35/8 → −35/16 correction not reproduced in full self-contained algebra**
   → **DP2-02 + DP2-16** (−35/16 quadruple-certified; four-vertex algebra `tab:vertices`
   L1561, `tab:vertexwalk`, `eq:order_grouped`, in-in identity all present since
   v1.7.104). Re-flag.
3. **[MAJOR] assumptions (d)/(f) conditional; no sensitivity plot for (d) violation /
   torsion reactivation** → **DP2-13** (load-bearing caveat ★, disclosed as
   single-clock scaling estimate, sign of subleading gradient coefficient the sole
   residual; assumption (f) scoped L1076). Re-flag.
4. **[MINOR] r=0.84 vs r_eff≈0.99 tension, null-space 0.85±0.13 not propagated** →
   **DP2-14 + DP2-15** (reconciled §spherex; the 0.85±0.13 is an amplitude-invariant
   stress band that never enters σ_eff; reparametrization caveat verbatim L1032). Re-flag.
5. **[MINOR] BF≈9–14 prior-width sensitive, no dedicated prior figure** → **DP2-18**
   (labeled "illustrative … not definitive model-selection evidence"; four-corner prior
   grid `tab:bayes`). Re-flag.

Grok's own closing paragraph AFFIRMS the central −35/16 claim is supported — disputes
framing/conditionality only. Grok M18-MINOR→M20-MAJOR→M23-MAJOR = pattern-066 variance.

## ChatGPT (REJECT) — 9 MAJOR + 2 MINOR
1. **[MAJOR] Appendix-A Eq.(A4) polynomial → coefficients (3,1,−9,5,−33,9) not adopted
   (2,7,3,−12,−69,19); null-space "artificial"; released code uses superseded −35/8
   amplitudes; additive-vs-global rescaling contradiction** → **DP2-15 + DP2-03 + DP2-28.**
   The reference vector (2,7,3,−12,−69,19) is present verbatim L1032 as the SHAPE-polynomial
   reference (the null-space scan is an amplitude-invariant stress band that never enters
   σ_eff — L1032). The "additive vs global rescaling" contradiction is DP2-03: L1556 states
   verbatim the term "is not itself a naive additive shift" and drives −35/16→−305/64 (NOT
   −35/8). The "released null-space code uses −35/8 amplitudes" is the DP2-28 stale-generator
   hygiene item (NOT `\includegraphics`'d; no PDF corruption; directive-I6 N/A). No
   reader-visible error. Re-flag.
2. **[MAJOR] σ=σ_local/r invalid unless r is the cross-Fisher response; 0.84 not the
   SPHEREx estimator response** → **DP2-14 + DP2-17 + DP2-22** (recast disclosed; r=0.84
   flat-weight conservative headline; r_eff≈0.99 validation). Re-flag.
3. **[MAJOR] in-house Fisher not equivalent to Heinrich (single global bias nuisance,
   omits b2/bs2)** → **DP2-22** (reproduction-vs-Heinrich limitation list disclosed
   §spherex; validation not independent forecast). Re-flag.
4. **[MAJOR] ρ=−0.868 transferred from SDB power-spectrum channel; |ρ|=0.95 cosine
   substitution** → **DP2-07 (+ DP2-26)** (headlined ρ=−0.868 with the |ρ|=0.95→0.8σ
   lower-edge row added `tab:systematics`; Cov_B not public = OPEN-VENUE DP2-26). Re-flag.
5. **[MAJOR] cubic-order transmission bound not established; degree-of-freedom counting
   insufficient** → **DP2-13** (single-clock nonlinear adiabaticity closure disclosed
   conditional on dressed-metric quantization L1076; "weakest link" flagged). Re-flag.
6. **[MAJOR] Appendix A.1(d) misreads Cai ε-grouped Eqs.(34–36) as undoubled; not an
   independent factor-of-2 certification** → **DP2-16 + DP2-02** (in-in identity `eq:commid`
   L1690 explicitly states it does NOT by itself adjudicate; −35/16 certified four
   independent ways; ε-order-grouped is one of them). Re-flag.
7. **[MAJOR] conflation of Wilson-Ewing LQC vs low-c_s ΛCDM bounce models** → **DP2-19**
   (assumption (a) fixes c_s=1 quasi-dust benchmark L1076; low-c_s a separate qualitative
   note). Re-flag.
8. **[MAJOR] κ_ε∈[2.8,40] schematic, not from a calculation; Eq.(13) parametrization not
   derived consistency relation** → **DP2-20** (κ_ε labeled single-prefactor-derivative
   estimate; fNL–n_s relation disclosed indicative). Re-flag.
9. **[MAJOR] BF≈9–14 arbitrary prior-volume ratio; multifield = uniform prior on f_NL** →
   **DP2-18** (labeled illustrative prior-volume ratio; prior-width sensitivity mapped). Re-flag.
10. **[MINOR] gauge-frame terminology (observable gauge-invariant after projection)** →
    **DP2-21** (framing dispute over comoving-gauge consistency-term interpretation; no
    numeric error). Re-flag.
11. **[MINOR] length/scope + mutable-filenames + immutable tagged archive vs future Zenodo
    DOI** → **DP2-30** PROCESS-NIT (presentation-streamlining + real Zenodo DOI at
    submission; Houston-gated venue). No reset.

ChatGPT's own §(3) closing concedes "the exact-dust algebra supporting −35/16 is credible"
— disputes the observational recast, not the arithmetic. Structural harsh-referee floor
(directive-H, DP2-24).

## DAS cross-check (per M22-P3 DP3-21 pattern)
Grep of both M23 P2 raws for data-availability / DAS / released / self-contradiction:
NO Data-Availability self-contradiction of the M22-P3 class was flagged. ChatGPT #11's
"mutable scripts / immutable tagged archive" is a reproducibility PROCESS-NIT (DP2-30), NOT
an internal self-contradiction between the DAS and the body. Cleared.

## Integrity
No ACCEPT faked; every finding dispositioned to a source-cited D-id; no math fabricated;
no hedging removed; no bump (0 genuinely-new); directive_g.sh NOT run (no edit).
Verdicts recorded as-is (Grok major-revisions, ChatGPT reject) via post_verdict.sh.
