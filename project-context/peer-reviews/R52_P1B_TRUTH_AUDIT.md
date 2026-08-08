# R52 — P1B TRUTH AUDIT (Opus judgment leg)

**Paper:** P1B — "Technical Verification Companion to the ECH Spin-Torsion Program"
**Source audited:** `arxiv/paper1b_mcmc_companion.tex` (current head = v1B.0.76, June 20 2026)
**PDF reviewed by vendors:** md5 a29137f5, 21 pp (date-line "June 14" ⇒ vendors saw an
earlier ~v1B.0.74 build; **PDF/source drift noted** — all core sections below confirmed
present in current source, so findings still apply).
**Reviewers:** Claude (MINOR; 2 MAJOR), Grok_brutal (MAJOR outlier), OpenAI (accept→MAJOR list),
Gemini (MAJOR), Perplexity (FAILED — 401 quota; no citation leg this round).

**NET VERDICT: MINOR REVISIONS.** Zero blockers. Two MAJOR-tier presentation items, both
closeable DO-NOW by editorial demotion/scoping — neither requires new MCMC to close.
The three "MAJOR REVISIONS" vendor verdicts collapse to MINOR once falsified items are
removed: Gemini's headline (Eq.1 missing ½) is FALSIFIED, Grok's two ESSENTIALs (ΔNeff
truncation, ALP-as-ECH advertising) are FALSIFIED, and the shared "pending DOIs" item is
a deliberate submission-gated companion-placeholder.

## Verdict counts
- BLOCKERS: **0**
- VERIFIED MAJOR (presentation): **2** — both DO-NOW editorial (full fixes TRULY-BLOCKED but not closure-gating)
- VERIFIED MINOR/NIT (DO-NOW editorial): **18**
- VERIFIED-but-deferred/submission-gated: **2** (DOIs; full overlap-corrected re-fit)
- FALSIFIED: **5**
- STALE: **1**
- OPINION/deliberate-allowance: **5**

---

## Highest-risk adjudication — the w0wa Table II MAJOR (Claude MAJOR-1 / OpenAI E2+M5 / Gemini m1 / Grok E2-adjacency)

**VERDICT: VERIFIED as a presentation defect — NOT a blocker, NOT fabrication. Close DO-NOW
by editorial demotion. The overlap-corrected re-fit is TRULY-BLOCKED and legitimately deferred.**

Evidence from source:
- Table II cells already carry inline caveats: `$w_0=-0.8122\pm0.0436$ (marg.-tail, $+4.3\sigma$)`
  with `fn:wcaveat` (L1469) stating verbatim "**not** a Bayes-factor or $\ln B$ exclusion and
  **not** a frequentist tension"; `$w_a$` cell L1470 "(marg.-tail; fn.~wcaveat)"; `$w_0+w_a$`
  cell L1471 "phantom-crossing indicated (caveated; fn.~wcaveat)".
- Section title (L2142) is "$w_0w_a$ cross-check **with stated SN-overlap systematic**";
  §V.C front-loads caveat (e) before the numbers (L2144-2167); "**no** model-selection statement is claimed."
- caveat (e) (L1605) discloses the ~20% DES-SN5YR×Pantheon+ shared-SN overlap (cites Vincenzi 2025,
  arXiv:2501.06664), states the bias direction is toward the reported signal, and that joint-covariance
  robustness "**has not been demonstrated quantitatively**." Two control chains "are the subject of a
  separate follow-up note."

Judgment: the number is honestly disclosed at every point of use, so it is **not** a fabrication
or a misrepresented detection — hence not a blocker. BUT four independent reviewers converge on the
same risk (a σ-annotation in a *main-text table body* invites out-of-context citation), and the
**Table II caption itself (L1463) carries no overlap/diagnostic caveat at all** — a reader lifting
the table sees the likelihood stack (DES-Y5+Pantheon+) but no warning. That convergent signal +
the caption gap make this a real, cheap-to-close presentation defect. The cheapest robust fix needs
**no new compute**.

- **DO-NOW (closes the MAJOR):** (i) add a boldface line to the Table II caption — "Overlap-uncorrected
  DES-Y5×Pantheon+ product likelihood; the $\sigma$-distances are marginal-tail posterior-extrapolation
  distances, diagnostic only — not detection significances and not suitable for model selection (caveat (e),
  fn.~wcaveat)." (ii) Remove "phantom-crossing indicated" from the `$w_0+w_a$` *cell body*; retain it in the
  caption/footnote.
- **TRULY-BLOCKED / legitimately deferred (NOT required to close):** the joint DES-SN5YR×Pantheon+
  covariance re-fit and the two SN-overlap control chains (need new MCMC). Do not gate closure on these.

---

## Grok MAJOR truth-audit (the harsh outlier — each reason individually)

| Grok ID | Claim | Verdict | Evidence |
|---|---|---|---|
| E1 | ΔNeff lead value −0.020±0.169 is a *truncated*-posterior mean with negative tail discarded, undisclosed | **FALSIFIED** | L1300: "results are two-sided posterior means." Truncation applies ONLY to the one-sided 95% UL (0.31/0.40), fully disclosed + justified L1304-1309. Grok conflates the two-sided central value with the one-sided limit. |
| E2 | Pipeline bias 0.040° juxtaposed with sky 3.6σ without "not directly comparable" at every use | **VERIFIED-mostly-satisfied** | Text states "not directly comparable" at L1116, L1640, L1890. Residual: propagate the one-liner into the Fig.3 caption + every downstream quote of 0.040°. MINOR DO-NOW. |
| E3 | Spectator-ALP advertised as part of "ECH Spin-Torsion Program" while disclaiming ECH derivation | **FALSIFIED/OPINION** | Title says "Birefringence **Consistency Check** with a Spectator-ALP Model"; L2195-2196 "not derived from minimal ECH … not a distinctive ECH prediction." The disclosure is exactly what Grok demands; framing is "verification companion," not prediction. |
| M1 | 21 pp too long; cut to 6-8 pp or withdraw | **OPINION** | Editorial length judgment; OpenAI logs it as a NIT. Not a defect. |
| M2 | ΔNeff one-sided UL uses ad-hoc renormalisation with no justification | **FALSIFIED** | L1299-1309: ΔNeff≥0 restriction is "physically motivated" (extra-species interpretation), conservatism for a mildly-negative mode explicitly noted. Two-sided interval also reported. |
| M3 | Pending DOIs; commit hashes pre-date v1B.0.74 | **VERIFIED-deferred (deliberate)** | Submission-gated companion-placeholder per calibration; DOIs minted at acceptance. Not a content defect; do not gate closure. |
| N1 | Axis labels omit units (Δφ/f_a) | **VERIFIED-NIT** | DO-NOW: add units. |
| N2 | Date "June 14 2026" is in the future | **STALE/FALSIFIED** | Source `\paperTimestamp` = June 20 2026; today = June 26 → past. |

**Grok net contribution:** 1 NIT (units) + reinforcement of the w0wa-caption item. Outlier verdict
driven entirely by falsified ESSENTIALs and an editorial length opinion.

---

## Full deduped findings ledger

### FALSIFIED (no fix)
- **Gemini M1 — Eq.(1) missing factor ½.** L1850 reads `\bigl[C_b^{EB,decoupled} - \tfrac{1}{2}\sin(4\beta)\,C_b^{EE,tmpl}\bigr]^2`. The ½ is present. Render/extraction artifact.
- **Gemini M4 — broken "fn. a"/"fn. b" cross-refs.** No such refs in source; caveats (a)-(e) are inline list labels (L1544-1610), footnote refs resolve via `\ref{fn:wcaveat}`/`\ref{fn:wpivot}`. Render artifact.
- **Grok E1, Grok M2** — see table above.

### OPINION / deliberate allowance
- **Gemini m2 / Gemini A1-dim — χ²(β) dimensionally inconsistent / abuse of notation.** Disclosed L1855-1858 (unweighted, no σ_b² divisor, matches canonical script). Optional relabel `S(β)`.
- **Gemini E1 — companion papers are placeholders / need joint submission.** Deliberate companion-placeholder per calibration; process item, not a content fix.
- **OpenAI E1 — pending DOIs / moving commit.** = Grok M3; submission-gated, deliberate.
- **OpenAI M7 / n5 — ℓ>2N_side bins "zero weight" wording.** Current "effectively restricted to ℓ≤1024" is correct for the minimiser (those bins add a β-independent constant). Optional wording polish.
- **Grok M1 / OpenAI n1 — length.** Editorial.

### VERIFIED MAJOR (presentation; DO-NOW closes, full fix deferred)
1. **w0wa Table II σ-figures / caption gap** — see adjudication above. Tier MAJOR; DO-NOW caption caveat + cell-body demotion.
2. **NaMaster MC scope — β–α / foreground separation not exercised** (Claude MAJOR-2). VERIFIED; disclosed strongly at L1116 (foreground-free skies, β–α degeneracy "absent by construction"). Residual gap: the 0.040° "systematic floor" is propagated downstream (§IV) without re-stating its foreground-free scope at each quote. **DO-NOW:** restrict every downstream use of 0.040° to "deconvolution-algebra bias on foreground-free skies — not a real-sky bias bound." A foreground/α-rotation injection MC is **TRULY-BLOCKED** (new compute) and not closure-gating.

### VERIFIED MINOR / NIT (all DO-NOW editorial)
- **OpenAI E3/M3 + Claude MINOR-4 — 0.040° floor quoted without uncertainty; Fig.3(b) no σβ bars.** σβ=0.046° at f_sky=0.32 measured (L1928); SE of 500-MC mean ≈ 0.046/√500 ≈ 0.0021°. Quote ±SE + add Fig.3(b) error bars + note rerun script/seed in caption.
- **OpenAI E4 — anharmonic correction in Ωa for θ_i≳O(1).** Partly addressed (v1B.0.74 O(θ²/6)→O(θ²/12)). Restrict Ωa fractions (13%/44%) to small-angle regime or state correction size. Recompute on existing chain ⇒ DO-NOW.
- **OpenAI E5 — tuning factor "~25×" vs ≳100× under cosθ prior.** Both slivers disclosed (0.33% flat-θ / 0.068% flat-cosθ). Harmonize headline: "≳100× under a cosθ_i prior (~25× vs the ad-hoc θ_i≈0.5 midpoint)."
- **OpenAI M1 — unweighted χ² "canonical estimator" uncited.** Add citation to the public driver, or adopt inverse-variance weighting as primary and keep unweighted as cross-check; note weighted is the efficient choice.
- **OpenAI M2 — release-pairing aux params not grouped.** One sentence listing H0/σ8/S8/Ωm deltas for c15-rerun vs frozen (numbers already exist).
- **OpenAI M4 — ACT footprint dec cuts (−65/+25 vs −60/+25).** Clarify by-design or harmonize; give f_sky to 3 dp.
- **OpenAI M6 / n4 — β radians-vs-degrees ambiguity in Eq.(1)/rotation.** State β in radians in equations/code; degree grid converted internally; give grid range/resolution.
- **OpenAI M8 — "effective weight 107,853" > 28,245 post-burn-in (L2123).** Nonstandard (ESS ≤ N_post). Relabel as GetDist sum-of-weights, or add true integrated-autocorrelation ESS.
- **OpenAI M9 / m-fn — per-realization SNR convention 8.1/7.2.** fn (L1922-1929) already defines it as |β̂|/σβ; state the convention once more prominently.
- **OpenAI M10 — "well below σ_obs" vs ACT DR6 0.074°.** Qualify to WMAP+Planck 0.094°; note 0.040° ≈ 0.5σ of ACT DR6 and remains a non-comparable pipeline quantity.
- **OpenAI M5** — folded into MAJOR #1.
- **Gemini M2 — w0wa "Physics interpretation" + caveats block sits in §III (ΛCDM+ΔNeff), duplicated at §V.C.** Structural-clarity. Consolidate/cross-reference; not load-bearing. Block at L1496-1610.
- **Gemini A1 — β_ALP vs β_obs combined-σ are not independent (β_ALP derived from β_obs).** Rephrase consistency as "model posterior mean 0.336° lies 0.06σ from the data central value" rather than σ_comb.
- **Gemini m1 / OpenAI E2-text — "σ" notation for marginal-tail distance.** Folded into MAJOR #1 (relabel/caption).
- **Claude MINOR-1 — sample-count footnote unfollowable.** Optional small table (raw/post-burn-in/GetDist-effective).
- **Claude MINOR-2/3 — β=0.27° vs 0.28° (Eq.4) and Eq.3 Δφ/f_a=0.42 vs fiducial 1.06.** Annotate canonical value once; flag Eq.3's 0.42 as one corner of the (m,θ_i) box.
- **Claude MINOR-5 — no model-selection statistic.** Legitimately scoped (caveat (a), fn:wcaveat). Add one abstract/§V sentence: "compatibility only; all model-preference inference deferred — not evidence for the bounce."
- **Grok N1 — figure-axis units.** Add units.

---

## CLOSURE PLAN (DO-NOW edits; all editorial, zero new compute)

| # | Tier | §/line | Current → Proposed | Class |
|---|---|---|---|---|
| 1 | MAJOR | Table II caption L1463 + cell L1471 | add boldface "overlap-uncorrected; marginal-tail distances diagnostic only, not detection-significance/model-selection (caveat (e), fn.~wcaveat)"; delete "phantom-crossing indicated" from `$w_0+w_a$` cell body (keep in footnote) | DO-NOW |
| 2 | MAJOR | §IV every quote of 0.040° (incl. Fig.3 caption L1718) | append "(deconvolution-algebra bias on foreground-free skies; not a real-sky bias bound)" at each downstream use | DO-NOW |
| 3 | MINOR | §IV / Fig.3(b) L1900-1928 | quote 0.040° ± SE (≈±0.002°); add σβ + SE bars to Fig.3(b); name rerun script/seed in caption | DO-NOW |
| 4 | MINOR | §VI Ωa (Eq.9) | restrict 13%/44% Ωa fractions to small-angle prior OR add anharmonic f(θ_i) + report correction size | DO-NOW |
| 5 | MINOR | §VI L2177 | "~25× tuning" → "≳100× under cosθ_i prior (~25× vs ad-hoc θ_i≈0.5 midpoint)" | DO-NOW |
| 6 | MINOR | §IV L1854 | add public-driver citation for unweighted estimator OR adopt inverse-variance as primary + note efficiency | DO-NOW |
| 7 | MINOR | §IV Eq.(1)/rotation | state β in radians in equations/code; degree grid converted internally; give grid range/resolution | DO-NOW |
| 8 | MINOR | §V.B L2123 | relabel "107,853 effective weight" as GetDist sum-of-weights OR add true ESS | DO-NOW |
| 9 | MINOR | §IV L1899-1901 / "well below σ_obs" | qualify to WMAP+Planck 0.094°; note ≈0.5σ vs ACT DR6 0.074° | DO-NOW |
| 10 | MINOR | §V (caveats) | one sentence grouping H0/σ8/S8/Ωm deltas for c15-rerun vs frozen | DO-NOW |
| 11 | MINOR | §IV masks | clarify −65/+25 vs −60/+25 dec cuts by-design; f_sky to 3 dp | DO-NOW |
| 12 | MINOR | §III L1496-1610 | consolidate/cross-ref the w0wa physics-interpretation block to §V.C | DO-NOW |
| 13 | MINOR | §VI ALP MCMC | rephrase β_ALP vs β_obs consistency as 0.06σ-from-central, drop σ_comb | DO-NOW |
| 14 | MINOR | abstract + §V | add "compatibility-only; model-preference inference deferred" sentence | DO-NOW |
| 15 | MINOR | Eq.3/Eq.4, fn | annotate canonical β (0.27° rounded vs 0.28° four-figure); flag Eq.3 0.42 as box corner | DO-NOW |
| 16 | NIT | Figs 1-4 | add missing axis units | DO-NOW |
| 17 | NIT | various | sample-count table (optional); micro-typography at proof | DO-NOW |

**TRULY-BLOCKED (deferred, NOT closure-gating, do not fabricate):**
- Joint DES-SN5YR×Pantheon+ covariance w0wa re-fit + the two SN-overlap control chains (new MCMC).
- Foreground/α-rotation (or beam-mismatch) NaMaster injection MC (new compute).
- Robust ln B / nested-sampling model comparison (new compute).
- DOI minting + immutable release tag (submission-gated).

**No FALSIFIED finding may be "fixed" into the paper** — Eq.(1) already has the ½; the ΔNeff central
value is correctly two-sided; the ALP section is correctly scoped as non-ECH; there are no broken
cross-refs. Editing these would introduce errors.
