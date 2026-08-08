# P3 (ApJS) M20-EXT truth-audit (2026-07-13, vs byte-unchanged v3.1.158-apjs) — STRICT ledger-first

Raws read verbatim BEFORE any disposition:
- `EXT_real/H17_2026-07-10/M20/P3APJS_grok_M20.md` = **MAJOR REVISIONS** (l.1 `VERDICT: MAJOR REVISIONS`; 4 MAJOR + 2 MINOR)
- `EXT_real/H17_2026-07-10/M20/P3APJS_chatgpt_M20.md` = **REJECT** (l.1 `VERDICT: REJECT`; 16 MAJOR + 2 MINOR)

Byte-unchanged **v3.1.158-apjs** — the same disclosed-content set audited at M6/M8/M10/M12/M15/M17.
`ledger_match.py` pre-match (Grok 6/9, ChatGPT 8/19 MATCHED — the high UNMATCHED rate is verbose
ApJS §-anchor restatement + parser-split header/tail fragments, every item Opus-adjudicated below) +
full §3 Opus truth-audit vs `paper3_apjs.tex` + `DISPOSITIONS/P3.md`.

## EXT-Grok MAJOR (4 MAJOR + 2 MINOR) — D-id mappings

- **[MAJOR] G1** "268,519 validated catalog-grade" not uniformly supported (NEOWISE by-construction
  gate; narrow lines recover only ≥15σ; validation "mixed not uniform") not in the lead sentence →
  **DP3-07/-09** (process-volume framing disclosed abstract L984 first sentence + §I reader's guide;
  mixed-validation stated by design, `tab:survey_summary` footnote ♡).
- **[MAJOR] G2** 268,519/377,482 as process-volume multipliers (~141×/~73×) while burying the
  science-target yield + non-detection framing → **DP3-07/-11** (2,468 like-for-like benchmark +
  98.7% sky/filler disclosed up front abstract L984 + §I L1010; "not confirmed physical detections"
  verbatim).
- **[MAJOR] G3** eROSITA (298) + Gaia excised for irreproducibility/synthetic while still discussed
  at length → **DP3-08** (`tab:provenance`: excised from EVERY count; exact 378,280→377,780→377,482
  subtraction §III.F L1179; complete QA-gate excisions, no residual score leak).
- **[MAJOR] G4** LAMOST retained in 377,482 (~113k) despite 98% blue-excess training-bias + native
  retrain 5.8%@5σ (gate FAIL); "methodological lesson" inconsistent with the three-tier framework →
  **DP3-14** (footnote ♡ + version-block disclose LAMOST cross-transfer-vs-native; failed-exploratory
  tier, NOT released per-object per RELEASE_MANIFEST). Disclosed provenance limitation. **0 genuinely-new.**
- **[MINOR] G5** full-sample (not train-split) feature scaling for eROSITA/NEOWISE → potential
  validation-set leakage into normalization; rank-order of extreme tail not shown unaffected →
  **DP3-13** (disclosed §VI + bounded robustness check, Jaccard ~0.76 top-298).
- **[MINOR] G6** §5 multi-tracer f_NL + NANOGrav "secondary" but occupy space + null results
  (α_jk 0.29σ; γ decisive only vs idealized circular-orbit SMBHB) → **DP3-10** (titled "Cosmological
  Applications (Secondary Demonstrations)", null; honest null NOT deleted per CRITICAL RESEARCH
  DIRECTIVE; venue = DP3-16 Houston-gated).

## EXT-ChatGPT REJECT (16 MAJOR + 2 MINOR) — D-id mappings

- **#1** 268,519 "validated catalog-grade" not established; recovery of synthetic perturbations ≠
  purity/FPR/astrophysical validity; NEOWISE by-construction → **DP3-07/-11/-12** (candidate framing
  disclosed; injection-recovery = sensitivity gate, purity residual = DP3-15 pod-blocked).
- **#2** SDSS 77,905 = arbitrary continuity-slice (19,253 @ top-1% knee, 12 @ S>5); "no motivated
  boundary; recompute all counts" → **DP3-09** (footnote ♡ tabulates 77,905/19,253/12 as survey-specific
  non-cross-comparable continuity slice by design; union-of-gated-sets, no single-FDR claim).
- **#3** DESI not reproducible at source (86.6% internal hashes, ~1.3% re-pullable, native parquets
  lost) → **DP3-15** (paper's OWN disclosed numbers §II.F; OPEN-COMPUTE structurally-bounded, pod-gated,
  NOT an edit — does NOT reset streak).
- **#4** dominant DESI tier physical composition unresolved (§3.1 98.7% sky/filler vs §3.3 98.8%
  GALAXY / 0.1% secure z) → **DP3-11** (§III.C reports ZWARN=0 secure 0.10% + "98.8% galaxy" =
  Redrock SPECTYPE composition, NOT a purity claim; both disclosed).
- **#5** DESI validation ≠ reliability of 195,829 (folds fail val-loss gate, 47k pool, OOD =
  stability not truth, 0/200 non-random) → **DP3-01/-12** (three-gate→one-production-gate closure;
  representative catalog-wide precision = DP3-15 pod-blocked).
- **#6** selection function under-specified (47k "representative" without sampling design;
  full-sample scaler; 16× downsample; median norm; unweighted MSE) → **DP3-13/-01** (disclosed §VI +
  `tab:caveats`; within-survey-ranking claim only; LAMOST failure = DP3-14).
- **#7** point sources + Planck 10°×10° patches not commensurate under 5″ FoF → **DP3-11** (patch
  bookkeeping disclosed §III.F; area-aware clustering = disclosed methodology limitation).
- **#8** Planck validation inadequate (same correlated patch bank; 5σ bump post-standardization not
  end-to-end) → **DP3-06** (Planck patch-bank + denominators disclosed §III.F; header clarified v3.1.151).
- **#9** "genuine novelty fraction" unsupported (5″ absence ≠ discovery; 178 need object-by-object) →
  **DP3-07/-09** (novelty = catalog-non-association under the stated matching procedure, disclosed;
  not a discovery claim).
- **#10** cross-survey association not catalog-grade (uniform 5″ FoF ignores astrometry/epochs;
  637 need probabilistic matching) → **DP3-09/-11** (5″ FoF + stability-over-3–7″ disclosed methodology;
  probabilistic-matching = disclosed limitation).
- **#11** "like-for-like" 2,685 EDR comparison not like-for-like (different denominators/thresholds) →
  **DP3-07** (2,468 vs 2,685 recount disclosed §III.C + §6.5 as ≈0.92× benchmark, denominators stated).
- **#12** SDSS astrophysical characterization from the FAILED cross-transfer set, not the native tier
  (84% cool-dwarf, taxonomy); ρ=0.036 too small → **DP3-14** (footnote ♡ discloses classification stats
  derive from cross-transfer while released tier = native re-score; membership overlap = DP3-15 gap).
- **#13** §5 f_NL not a valid downstream constraint (5,384 QSO no z-dist/confirmation; angular ratio ≠
  3-D bias; inconsistent Fisher normalizations) → **DP3-10** (secondary null demo, estimator caveats
  App C/E disclosed).
- **#14** §5.1 NANOGrav disconnected/overinterpreted (γ=3 mapping not derived; KDE 4.6σ tail) →
  **DP3-10/-18/-19** (secondary demo; γ mapping + parameter-shift disclosed, SMBHB reference caveat
  L1555; +4.63/+1.14σ corrected v3.1.154/-155).
- **#15** provenance failures too serious for archival catalog (synthetic Gaia, eROSITA axis lost,
  DESI linkage lost, Planck checkpoint/tensor lost, LAMOST contradictory) → **DP3-08/-15** (all
  paper's OWN disclosures §III.E–G; DP3-20 immutable-release CLOSED; end-to-end re-run = DP3-15 pod-gated).
- **#16** internal accounting contradictions (DESI PASS labeling; LAMOST in-377,482-but-excluded;
  Gaia removed-but-mentioned; 36.76/36.93/37.29M) → **DP3-03/-04/-08/-20** (37.3M footnote-⊗
  reconciliation v3.1.152; LAMOST/Gaia excision bookkeeping disclosed; manifest = authoritative per DP3-20).
- **[MINOR] #17** Figures 1/5/8/10 don't display the evidence (force-included exemplars; optical
  vs NEOWISE image; "display" scores; Fig 10 omits DESI) → **DP3-11 OPINION** (figure-provenance
  disclosed in captions; presentation preference).
- **[MINOR] #18** excessively repetitive; "largest/validated/real/confirmed/genuine" should be
  restricted; separate cosmology → **DP3-16 OPINION / PROCESS-NIT** (venue judgment Houston-gated;
  honest disclosure retained per CRITICAL RESEARCH DIRECTIVE).

ChatGPT's own close: "the manuscript supports the existence of a large ranked set of reconstruction
outliers, but not … a reproducible, uniformly validated, catalog-grade anomaly sample" — the
standing catalog-vs-PRD/ApJS validated-purity venue judgment (DP3-07/-09/-12/-16, Houston-gated) +
the pod-blocked purity/re-inference residual (DP3-15). DP3-20 immutable-release bar stays DISSOLVED
(neither leg re-raises "described prospectively/disqualifying"). Structural maximally-harsh ApJS
floor (DP3-17 backfire). **0 genuinely-new.**

## Verdict

**0 genuinely-new reader-visible editable findings** across both legs (all source-cited standing
DP3 re-flags + OPEN-COMPUTE pod-gated + venue OPINION + PROCESS-NIT). Prior M17-EXT rebuilt streak
to 7. **M20-EXT = 0 genuinely-new on byte-unchanged v3.1.158-apjs → clean-wave streak 7→8**
(directive-K). No content bump; **v3.1.158-apjs stands; `directive_g.sh` NOT run.**

## Cap HOLDS 56

Unchanged EXT verdict words vs M17 — Grok MAJOR (6) + ChatGPT REJECT (0) + Gemini EXT REJECT/carry (0)
= 50 + 6 = **56**. Cap **56 HOLDS**.

## Integrity

Both raws read verbatim before any disposition (Grok l.1 `VERDICT: MAJOR REVISIONS`, ChatGPT l.1
`VERDICT: REJECT`). No ACCEPT faked. Every finding source-cited to an existing DP3 D-id + §-anchor;
every ledger_match-UNMATCHED finding source-verified against the live `paper3_apjs.tex`. DP3-15
end-to-end re-inference = OPEN-COMPUTE pod-gated (does NOT reset streak — reviewer cites the paper's
OWN 86.6%/~1.3% numbers). DP3-20 immutable-release bar DISSOLVED (not re-raised). No un-sourced
dismissal; no math fabricated; no version bumped.
