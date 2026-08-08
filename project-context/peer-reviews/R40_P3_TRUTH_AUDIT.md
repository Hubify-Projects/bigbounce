# R40 P3 — Truth Audit (final pre-arXiv)

**Paper:** P3 multi-survey anomaly catalog, v3.1.111
**Source:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (PDF md5=4a8c1172, 30pp)
**Reviewers:** OpenAI (gpt-5, methodology) · Gemini (2.5-pro, cosmology) · Grok (grok-4.3, brutal) · Perplexity (FAILED — 100KB limit, 0 findings) · Claude Opus leg (MINOR, 2 verified)
**Auditor:** truth-audit + synthesis lead, per `feedback_peer_review_truth_audit_protocol`

## Verdict legend
VERIFIED-OPEN = real, actionable on this version · STALE = already disclosed/caveated in current .tex · MISLABELED = real text but reviewer mischaracterized severity/meaning · OUT-OF-SCOPE = needs new data/run beyond arXiv polish · OPINION = stylistic preference · DUPLICATE = same root as another item

---

## Claude-leg findings (the 2 the protocol requires we carry)

### (A) NANOGrav chain path is wrong — **VERIFIED-OPEN** ✅
- **Claim:** tex L1333 cites chain at `reproducibility/nanograv_mcmc/`; that dir does NOT exist; real artifacts at `reproducibility/p3_pta_mcmc/`.
- **On-disk:** `reproducibility/nanograv_mcmc/` → **does not exist** (confirmed). `reproducibility/p3_pta_mcmc/` → **exists** (README.md + run_pta_combined_mcmc.sh).
- **Subtlety found:** the README at `reproducibility/p3_pta_mcmc/` is the **combined-4-PTA / ptarcade** bundle (γ=3.19/3.32). The canonical Wave-13 **single-PTA real-KDE** chain (γ=2.567±0.382, log10A=−14.025±0.380, matching the tex exactly) actually lives at `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy` with its Savage-Dickey JSON alongside. So the tex path is wrong AND points at the wrong-location/wrong-run bundle.
- **Fix:** L1333 — replace `reproducibility/nanograv\_mcmc/` with `pipelines/p3\_pta\_mcmc/free\_spectrum\_real\_2026-05-01/` (the path that holds the chain whose marginals match the quoted γ/log10A). Use the `\artifact{}` macro for column-safe rendering.

### (B) Wave-13 real chain + SD JSON uncommitted — **STALE / FALSIFIED** ❌→ collapses into (A)
- **Claim:** canonical real-KDE chain + SD density JSON (0.461, 6.46e-5) not committed; only a superseded synthetic run on disk.
- **On-disk truth:** BOTH are committed and tracked in git:
  - `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy` (5.1 MB, `git ls-files` ✓, last commit `03989fe5` "feat(R42-Wave-13): real NANOGrav KDE free-spectrum γ=2.567±0.382 LANDED")
  - `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/savage_dickey_2026-05-29.json` (`git ls-files` ✓, commit `7b5d1ef3`)
  - JSON contents verified: `posterior_at_matter_bounce_3p0 = 0.46108`, `posterior_at_smbhb_13_3 = 6.4599e-5`, `B_MB/free = 3.2276`, `B_MB/SMBHB = 7137.6`. Exactly matches tex §V (L1054) and abstract.
- **Verdict:** the chain + SD JSON ARE in the committed tree, just at `pipelines/p3_pta_mcmc/` not `reproducibility/`. The "only superseded synthetic run committed" premise is false. No "commit the chain" action needed — the repository is reproducible. The ONLY real defect is the stale path string in (A). Item (B) closes by artifact verification.

---

## Vendor findings audit

### OpenAI (gpt-5) — 13 essential/major + minors, 2-pass
| ID | Claim | Verdict | Evidence |
|----|-------|---------|----------|
| E1 | "catalog-grade" 269,317/269,117 counts confusing; 4,379 LAMOST-into-6-way inconsistent | MISLABELED | Abstract L562 already tabulates 7-way(w/Planck)=269,317, point-source=269,117, full Path-C=378,280, eROSITA membership-only, LAMOST excluded. Definitions are explicit, not "only in footnotes." The 4,379-LAMOST point is a real clarity nit at most → MINOR, not ESSENTIAL. |
| E2 | eROSITA score axis irreproducible yet cited in headline | STALE | Abstract L562 + Table I (L682) already state "eROSITA tier released as n=298 membership list only; per-object S_BigAE non-reproducible on any of 16 monotone rescalings." Self-disclosed; reviewer re-flagged a stated caveat. |
| E3 | Zenodo DOI placeholder; no frozen tag | OUT-OF-SCOPE | L1153: "DOI minted at submission." This is correct arXiv-submission workflow (DOI is assigned at submission). Not a pre-arXiv defect. |
| E4 | Gaia 20-feature preprocessing script "not recovered"; scaler-on-full-sample leakage | STALE (disclosure) / OUT-OF-SCOPE (retrain) | L1153 explicitly discloses "exact 20-feature production preprocessing script not recovered… feature list lineage-inferred." Gaia already flagged exploratory (5.2% recovery, gate FAIL). Retrain = post-arXiv. |
| E5 | NEOWISE geometry QA counted as injection PASS | STALE | Abstract L562: "NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by construction, not a detector-sensitivity test." Already separated in text. |
| E6 | Planck top-200 includes training patches | STALE | §III F already provides the 48/200-validation-overrepresentation check + p≈4e-4 diagnostic and labels the tier appropriately. |
| E7 | p=0.12 on stratified subsample not interpretable | MISLABELED | Real statistical nuance but text already states the sample is "deliberately stratified log-uniform in SNR." Polish: drop p or note design. MINOR. |
| E8 | 4,379 LAMOST merge inconsistent w/ 6-way | DUPLICATE of E1 | — |
| E9 | SDSS 77,905 continuity-slice arbitrary | STALE | Table I (L682) discloses the slice is "sized to equal the cross-transfer count… not a top-1% cut" and gives the alternative thresholds (12 at S>5; 19,253 top-1%). |
| M1 | Threshold heterogeneity hard to follow | OPINION | Restructuring footnotes → subsection is editorial. |
| M2 | NEOWISE dust/AGN interpretation speculative | OPINION/STALE | Already framed as hypotheses. |
| M3 | Fisher refit α-grid/R² not given | OUT-OF-SCOPE (polish) | Optional deposit; not load-bearing for headline (envelope is the summary). |
| M4 | KDE bandwidth not reported | OUT-OF-SCOPE (polish) | Bayes-factor stability is genuine but secondary-application; tex already flags prior-sensitivity. |
| M5–M9, M10–M13 | density map, inspection protocol, plant params, χ² over-interp, Cramér panels, PTA Eq dimensional, "largest" claim, Planck p indep | STALE or OPINION | χ² (M9): L935 already carries a full "Caveat on the χ² figure" paragraph. "Largest" (M12/Grok-M1): L562 already hedged "of which we are aware… anchored to largest single-survey [Liang2023]." |
| **E10** | **Cramér's V form vs number mismatch** | **STALE** | L935 prints `V = √(χ²/(N·(k−1))) = √(376713/(378280×24047)) ≈ 0.0064` — sqrt IS applied to the full fraction. v3.1.106 changelog (L78,81) records this exact fix ("Cramer V corrected 0.020→0.0064, sqrt now applied"). Claude-leg independently verified 0.0064. Reviewer saw a pre-fix render or misread. |
| m1–m14, N1–N5 | minors/nits (dynamic-range inset, hyphenation, Nanom header, seeds, Jeffreys softening) | OPINION | Editorial polish; none block arXiv. |

### Gemini (2.5-pro)
| ID | Claim | Verdict | Evidence |
|----|-------|---------|----------|
| M1 | Abstract "eROSITA stability 81.5%" reads as success | STALE | Abstract L562 already: "3 FAIL-with-diagnostic… eROSITA 1.2%; eROSITA cross-validation stability 81.5%" — FAIL context present. |
| M2 | Broken cross-ref "§VIE" in abstract | MISLABELED | `\S\ref{sec:comparison}` (L562) resolves to §VI E "Comparison with Prior Work" (L1112). Not a broken ref — `\ref` is live. Reviewer read rendered "§VIE" as a dead literal; it is a working hyperlink. No action. |
| m1/m2 | Fig 2 caption dense; Fig 8 display-vs-canonical scores | OPINION/STALE | Fig 8 provenance already disclosed in caption. |
| m3/N1-N5 | Eq E1 ½-factor "typo"; date; f_NL notation; footnote radius | MISLABELED (E1) / OPINION | Eq E1 ½ is the standard ceffyl free-spectrum h_c→ρ log-amplitude convention (h_c ∝ A, so ½ on the 2log10A power term is correct, not a typo — duplicated by Grok); rest editorial. |

### Grok (grok-4.3)
| ID | Claim | Verdict | Evidence |
|----|-------|---------|----------|
| E1 | Abstract "8.98 exactly" false vs body 8.14 | STALE | Abstract L562 states BOTH: "de-biased point estimate returns 8.98 exactly (no multi-tracer improvement)" AND "inserting noisy α̂ … gives central 8.14 with envelope [3.92,8.98]… central improvement is noise-driven, not a detection." Both numbers present and reconciled. Reviewer read half the sentence. |
| E2 | 378,280 is post-dedup, pre-dedup total not in abstract | STALE | Abstract L562 gives 388,493 native sum → 378,280 unique at 7-way 5″ explicitly. |
| E3 | Fisher α̂ uncertainty not propagated | MISLABELED | Envelope [3.92,8.98] IS the α̂-uncertainty band; abstract calls the envelope "the appropriate summary," central value "noise-driven." Already conditional-labeled. |
| E4 | Path-C retrain spec only in external JSON | OUT-OF-SCOPE (polish) | Appendix + companion repo carry epochs/seeds; deposit-in-text is editorial. |
| E5 | Fig 3 S~1e11 panel no KS test | OPINION | Caption already says "not like-for-like." |
| M1 | "largest" unsupported | DUPLICATE of OpenAI-M12 → STALE | Hedged in L562. |
| M2 | eROSITA manifest lacks per-object S column | STALE/OUT-OF-SCOPE | Disclosed as membership-only (L1153 schema-flag table). |
| M3 | 30-region jackknife may underestimate | OUT-OF-SCOPE (polish) | — |
| M4 | 30pp too long | OPINION | — |
| m1–m3 / NITs | acronym table, ICRS epoch, seed, date | OPINION | — |

### Perplexity — **NO FINDINGS** (call failed: 100KB content-length limit). Citation forensics not delivered this round; Claude-leg verified citations clean.

---

## Merged dedupe result

**Distinct VERIFIED-OPEN items across all five legs: 1.**

1. **NANOGrav chain path** (Claude-A; not raised by any vendor) — tex L1333 cites nonexistent `reproducibility/nanograv_mcmc/`; correct path is `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/` (holds the chain whose γ=2.567±0.382 / log10A=−14.025 marginals match the quoted numbers).

**Item B → closed by artifact verification** (chain + SD JSON are committed; only the path string is stale; fixing (A) closes (B)).

**Everything the 3 working vendors flagged as ESSENTIAL/MAJOR is STALE, MISLABELED, OPINION, or OUT-OF-SCOPE.** The recurring root cause (pattern: reviewer re-flags an already-disclosed caveat because the abstract is dense): eROSITA non-reproducibility, NEOWISE geometry-QA, 8.98-vs-8.14, 388,493-vs-378,280, χ² over-interpretation, Cramér's V sqrt, "largest" hedge, and Eq-E1 ½-factor are ALL already in the current .tex. The OUT-OF-SCOPE set (Zenodo DOI, Gaia retrain, KDE-bandwidth sweep, jackknife-vs-bootstrap) is genuine future work, not arXiv-blocking.

Novelty: N3 (Claude-leg confirmed). 0 overfull, no `\mbox{-}` artifacts, dust p=0.35, Table IX rows, Cramér's V=0.0064 — all clean.

---

## Single closure action for v3.1.111 → arXiv

**File:** `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Line:** 1333
**Edit:** replace
`(GitHub: \texttt{Hubify-Projects/bigbounce}, path \texttt{reproducibility/nanograv\_mcmc/})`
with
`(GitHub: \texttt{Hubify-Projects/bigbounce}, path \artifact{pipelines/p3\_pta\_mcmc/free\_spectrum\_real\_2026-05-01/})`

Then recompile → `/latex-audit` → `/artifact-link-verify` (confirm the new path resolves on main; it is git-tracked) → restamp v3.1.111.

**No other change required for arXiv readiness.**
