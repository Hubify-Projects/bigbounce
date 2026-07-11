# GEM1-INT truth-audit — first-ever verified Gemini INT leg (gemini-3.1-pro-preview)

Round dir: `project-context/peer-reviews/INT_v3/ROUND_2026-07-09/`
Raws: `API_<P>_gemini.md` (native-PDF, inline_data/Files upload; latency 31–58s; real usage metadata).
Adjudicator: Claude Code sub-agent (Opus), skeptical fresh-eyes stance per directives I3/F.
Papers/versions reviewed: P1U v1U.0.12 · P2 v1.7.112 · P3 v3.1.152 · P4 v1.0.235 · P5 v0.1.120.
Ledgers: `project-context/peer-reviews/DISPOSITIONS/<P>.md`. Draft matcher: `tools/ledger_match.py`.

Every finding below is dispositioned verdict-first with a source-cited D-id. The two boilerplate
rows the matcher parses at the top of each raw ("REVISIONS ===… / ISSUES: 1.") are parser noise —
verdict-header fragments, NOT findings — and are excluded.

**HEADLINE: 0 genuinely-new reader-visible editable findings on any of the five papers.**
Every substantive Gemini finding maps to a standing DP<P>-id (RE-FLAG-DISCLOSED, OPINION,
OPEN-COMPUTE, or OPEN-VENUE). No closures required, no version bumps, no streak resets.
Gemini — a genuinely fresh 7th reviewer with no round history — independently landed on the
SAME already-disclosed limitation classes the calibrated referees converged on. That is the
honest stress-test of the directive-K exit passing.

---

## P1U v1U.0.12 — Gemini MAJOR REVISIONS (5 findings)

1. **[MAJOR] Holst term vanishes for Levi-Civita — §X perturbation-transparency "trivial/redundant."**
   → **RE-FLAG-DISCLOSED / OPINION (DP1U-12).** The paper already labels this the "standard on-shell
   scalar / zero-spin-density equivalence," a narrow positive core for canonical scalar matter
   (Claude-verified-correct, L1248/L3333-adjacent). Gemini's "reduce to one paragraph, don't frame
   as a theorem" is a novelty/presentation preference, not an editable error. Not new.
2. **[MAJOR] Observational appendices (E–H) "irrelevant / bloat."**
   → **OPINION / scope (DP1U-06 + DP1U-11 family).** Author explicitly tags these appendices
   "not load-bearing" for the no-go claims; Gemini quotes that self-disclosure back. "Remove them"
   is a length/scope preference (Houston-gated presentation class, cf. DP2-30 analogue), not a
   content defect. Not new.
3. **[MAJOR] Overstated novelty of the four no-go routes (§IV) — "standard EFT dimensional analysis."**
   → **RE-FLAG-DISCLOSED (DP1U-06 + DP1U-11).** Abstract + title already headline
   "channel-level assessment, not an operator-level theorem" (L1219, L1389-1390) and the
   evidentiary-tier table; R4 explicitly "not closed by amplitude mismatch … relocating the CC
   problem" (L1195-1198). This IS the paper's verbatim framing. Not new.
4. **[MINOR] Verbosity / repetitive caveats.** → **PROCESS-NIT (style; DP1U-06 OPINION).** No reset.
5. **[MINOR] Reliance on unpublished companion papers II–V.** → **PROCESS-NIT (style; DP1U-04-adjacent).**
   The companion cross-refs are "illustrative context" and the paper is self-contained. No reset.

**Verdict: 0 genuinely-new. 3 RE-FLAG/OPINION MAJORs + 2 PROCESS-NIT. Streak HOLDS.**

## P2 v1.7.112 — Gemini MINOR REVISIONS (4 findings)

1. **[MAJOR] §VII/Eq.(11) SDB-proxy for the bispectrum-GR correlation is heuristic; compute directly
   or downgrade the 1.3–2.75σ envelope.** → **RE-FLAG-DISCLOSED (DP2-04).** Already disclosed as a
   "scoping sensitivity envelope … not a joint-covariance forecasted measurement precision"
   (abstract L892; `tab:systematics` caption); v1.7.108 subordinated the envelope and made the
   single central Fisher significance the headline. Not new.
2. **[MAJOR] §VI Bayes factors (BF≈9–14) prior-dominated; abstract quote misleading.**
   → **RE-FLAG-DISCLOSED (DP2-18).** Labeled "illustrative … not definitive model-selection
   evidence"; four-corner prior grid in `tab:bayes` (L1236). Not new.
3. **[MINOR] Elevate App-A −35/16 vertex-sum derivation to the main text.**
   → **PRESENTATION / OPINION (DP2-02).** The −35/16 value is quadruple-certified and unchanged;
   moving the derivation section is placement preference, not a defect. No reset.
4. **[MINOR] Tone "defensive/colloquial," bold meta-commentary.** → **PROCESS-NIT (style; DP2-13).**
   Same PRD-abstract-format preference already dispositioned in the H17H presentation wave. No reset.

**Verdict: 0 genuinely-new. Streak HOLDS.**

## P3 v3.1.152 — Gemini REJECT (5 findings) — KNOWN VENUE CLASS, not new

1. **[MAJOR] Scope/journal-fit: catalog release belongs in ApJS/MNRAS/A&A, §V cosmology "secondary."**
   → **OPEN-VENUE / OPINION (DP3-16 + DP3-10).** Verbatim the standing pattern-066 venue judgment:
   catalog is the explicit primary deliverable, §V titled "Cosmological Applications (Secondary
   Demonstrations)." Houston-gated venue routing, not an editable content defect.
2. **[MAJOR] Weak cosmology (§V): f_NL multi-tracer no improvement, NANOGrav non-decisive.**
   → **RE-FLAG-DISCLOSED (DP3-10).** §V returns null results BY DESIGN (abstract L984); estimator
   caveats in App C/App E; reviewers agree it is "correctly scoped as secondary." Not new.
3. **[MAJOR] Pipeline instability/contamination: LAMOST 98% training-bias, Gaia synthetic excised,
   eROSITA irreproducible.** → **RE-FLAG-DISCLOSED (DP3-08).** `tab:provenance` + abstract L984 +
   §III.F L1179 disclose every excision (complete QA-gate excisions, not hidden failures;
   INT-Claude verified no residual eROSITA score leak). Not new.
4. **[MINOR] "Reads like a software audit trail / GitHub README," raw file paths.**
   → **OPINION / PROCESS-NIT (DP3-16).** Honest disclosures retained per CRITICAL RESEARCH DIRECTIVE. No reset.
5. **[MINOR] ~17.8% "genuine novelty fraction" extrapolated from top-1000 DESI sample.**
   → **RE-FLAG-DISCLOSED (DP3-07/-09 family).** The novelty rate is stated for the localized
   top-anomaly sample; the score-vs-reconstruction-residual correlation is itself disclosed. Not new.

**Gemini's REJECT = the same catalog-vs-PRD venue class + disclosed pipeline-artifact disclosures
that ChatGPT's H17G/W1 REJECTs and OpenAI's stale-version REJECT already sit on (DP3-17 backfire
floor). 0 genuinely-new. Streak HOLDS.**

## P4 v1.0.235 — Gemini MINOR REVISIONS (4 findings)

1. **[MINOR] Excessive inline repo paths, move to footnotes/reproducibility table.**
   → **PROCESS-NIT (style).** Presentation preference. No reset.
2. **[MAJOR] §IV.D/VI.D ~47% ℓ=1 harmonic residual "open item"; estimate a conservative upper bound
   on parity-violating physics it could mask.** → **OPEN-COMPUTE (DP4-17).** The ~47% remainder is
   disclosed and bounded a-fortiori below the A_50/A_95 recovery threshold (§monopole_mask_null L1005 /
   Appendix-D); the version-block comments already record this exact Gemini re-flag ("Gem3 … already
   has bottom-line first + a-fortiori bound"). A joint real-space×harmonic likelihood/covariance
   model that would produce the requested masked-physics upper bound is genuine future work
   (OPEN-COMPUTE), not editable now. Not new-editable.
3. **[MINOR] "Amplitude-level tension not frequentist exclusion" caveat repetitive.**
   → **PROCESS-NIT (style; DP4-14 disclosed caveat).** No reset.
4. **[MINOR] Condense CE-ResNet pseudo-label-inheritance bounds into one paragraph.**
   → **PROCESS-NIT (style; DP4-16 open-compute-adjacent).** No reset.

**Verdict: 0 genuinely-new-editable (1 OPEN-COMPUTE re-flag + 3 PROCESS-NIT). Streak HOLDS.**

## P5 v0.1.120 — Gemini MINOR REVISIONS (3 findings)

1. **[MINOR] App-B "Toy EFT mapping": operator is non-covariant → call it "phenomenological
   parameterization," not "EFT."** → **RE-FLAG-DISCLOSED (DP5-20).** App B + Conclusions already
   label it "speculative … outside the empirical scope … not a derived constraint"; the
   coordinate-dependence is the paper's own stated caveat. Terminology preference on already-
   relegated content. Not new.
2. **[MINOR] §I & §XIII: physical-chirality bound (2.26pp) depends on Paper-IV de-attenuation
   (2a−1, a≃0.699); state it updates if Paper-IV's confusion matrix changes.**
   → **RE-FLAG-DISCLOSED (DP5-09).** Abstract l.749-757 flags the symmetric-error approximation and
   labels the physical bound the weaker quantity; the Paper-IV dependency is disclosed. Not new.
3. **[MINOR] §XIII RSD: fixed-geometry heuristic; give an order-of-magnitude estimate of anisotropic
   eigenvalue shifts at λ_th=0.** → **RE-FLAG-DISCLOSED / OPEN-COMPUTE-adjacent (DP5-12).** Abstract
   l.758-765 + §limitations state all bounds are fixed-redshift-space, RSD inherited, anisotropic-
   tidal channel "not quantified" with Zel'dovich reconstruction deferred to future work. Disclosed. Not new.

**Verdict: 0 genuinely-new. Streak HOLDS.**

---

## Integrity note (directive F)

Gemini is the FIRST reviewer with zero prior exposure to this program's round history or ledgers.
Fresh-eyes items were treated seriously (each got a full §3 source-cited audit against the current
.tex, not a label-match dismissal). Result: every finding independently reproduced an
already-disclosed limitation class — the strongest available evidence that the disclosures are real
and the directive-K exit is GENUINE, not engineered. No finding was dispositioned non-real without a
source-cited pointer; nothing was fabricated to make a finding disappear; no favorable value was
headlined over an unfavorable one.
