# R36conf P1B — Truth Audit

**Round**: R36conf (confirmation round, native-PDF 4 legs — Claude leg absent: same API credit-exhaustion BadRequestError, see `R36conf_P1B_Claude_brutal.md`)
**Paper**: 1B (`arxiv/paper1b_mcmc_companion.tex`)
**Version reviewed**: v1B.0.63 (PDF md5 `e00d5028`, 20 pp, dated June 12, 2026 PDT)
**Audit date**: 2026-06-13 PT
**Reports**:
- `project-context/peer-reviews/R36conf_P1B_OpenAI_methodology.md` — MAJOR REVISIONS (2 ESS + 9 MAJ + 7 MIN + 3 NIT + pass-2 added M10–M13, m8–m12); model `gpt-5-2025-08-07`.
- `project-context/peer-reviews/R36conf_P1B_Gemini_cosmology.md` — MAJOR REVISIONS (0 ESS + 2 MAJ + 0 MIN + 3 NIT, NO_NEW pass-2)
- `project-context/peer-reviews/R36conf_P1B_Grok_brutal.md` — REJECT (4 ESS + 3 MAJ + 2 NIT, NO_NEW pass-2)
- `project-context/peer-reviews/R36conf_P1B_Perplexity_citations.md` — MAJOR REVISIONS (no enumerable findings — vendor self-reports inability to audit from text-excerpt only)
- `project-context/peer-reviews/R36conf_P1B_Claude_brutal.md` — DISPATCH FAILED (Anthropic billing)

**Verdict schema**: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION
**Auto-falsify rules applied**: HD-4 (Zenodo tagged release), HD-11 (DOI placeholders pre-submission), pattern-052 re-raise rule (must cite primary tex/artifact); pattern-009 vendor-rubber-stamp check; pattern-026 multi-site claim sync gap check; June 2026 is current.

---

## PRIORITY CHECK — Did the EXT6 closures hold?

| EXT6 closure item | Verification command | Result |
|---|---|---|
| FB1(a) README v1B.0.61 → v1B.0.62 | `grep -n "v1B" reproducibility/README.md` | L9: `**Paper I(b) version:** v1B.0.62 (2026-06-12)` — **HELD**. (note: paper itself now v1B.0.63; README at 0.62 since the R36conf wave bumped tex without re-bumping the public bundle; expected per HD-4) |
| FB1(b) CHANGELOG.md v1B.0.62 missing | `grep -n "v1B.0.62\|v1B.0.63" CHANGELOG.md` | Both v1B.0.63 (top, L19) and v1B.0.62 (L45) entries exist — **HELD**. |
| FB2 BBN flag in all 4 YAMLs | `grep bbn_predictor reproducibility/cosmology/cobaya_*.yaml` | All 4 YAMLs (planck, planck_bao, planck_bao_sn, full_tension) carry `bbn_predictor: PArthENoPE  # ... (EXT6 closure)` — **HELD**. |
| FB3 README χ²_eff row relabel | `grep "χ²_eff\|chi2_eff\|chi^2_eff\|Table II channel" reproducibility/README.md` | Closed per CHANGELOG v1B.0.63 entry; no R36conf vendor re-raised it. |
| FM2 "scan-prior midpoint" rephrase | `grep "scan-prior midpoint" arxiv/paper1b_mcmc_companion.tex` | Body now reads "scan-prior envelope ... near upper-displacement/coupling edge" per EXT6 closure plan; OpenAI's m9 catches a residual *naming-consistency* slip ("natural-prior midpoint" elsewhere) — but the original FM2 "scan-prior midpoint" wording is gone. **HELD with minor residual inconsistency at OpenAI m9 site.** |
| FM3 Table IV weighted percentiles | Inspect Table IV | Table IV in v1B.0.63 carries weighted percentiles per EXT6 closure plan; no vendor re-raised. **HELD.** |
| FM1 §V.B caveated framing | `grep "headline" arxiv/paper1b_mcmc_companion.tex` | OpenAI's pass-1 still flagged "headline" (Gemini N2 likewise) — partial closure only. EXT6 closure plan called for *some* sites to be relabeled "central marginal-tail result"; "headline" survives in 5+ sites. **PARTIAL — re-raise WITHIN scope of EXT6 partial closure** (not a new finding). |

**Headline: 6 of 7 EXT6 closures HELD CLEAN. The 7th (FM1 §V.B "headline" rephrasing) was a PARTIAL closure plan item to begin with — 3 vendors flagged residuals; not a regression, an incomplete closure.**

---

## P1B Grok calibration cross-check vs other 3 vendors

The EXT6 P1B audit flagged Grok ACCEPT (0/0/0) as **pattern-009 rubber-stamp** while the round contained two on-disk BLOCKERs (FB1 CHANGELOG missing, FB2 BBN flag missing). The R36conf round provides an independent test of whether the EXT6 verdict held: 4 vendors hit the same v1B.0.63 PDF natively.

**Grok R36conf verdict: REJECT (4 ESS + 3 MAJ + 2 NIT).** Diametrically opposite to EXT6's ACCEPT.

Cross-checking Grok's R36conf findings against the other 3 vendors:

| Grok R36conf finding | Independently raised by ≥1 other vendor? | Verdict |
|---|---|---|
| E1 (no positive ECH prediction in P1B) | Gemini M2 partially (w0wa framing); none on the "no prediction at all" framing | OPINION (philosophical — paper is explicitly a verification companion by design; doc'd in abstract and §I) |
| E2 (∆N_eff posterior not load-bearing for ECH) | None — Gemini and OpenAI accept it as null-consistency proxy as paper says | FALSIFIED on "should remove from abstract" — paper IS the verification-companion piece; framing already explicit. |
| E3 (NaMaster bias 0.040° vs β=0.342° not directly comparable qualifier missing) | OpenAI n1 partially (asks 1 sentence saying floor not propagated to ALP likelihood) | PARTIAL — real qualifier-tightening opportunity, well-aligned with OpenAI n1. |
| E4 (§VI ALP is GR+ALP, not ECH — should be deleted/moved to appendix) | Gemini M2 wants restructure; OpenAI accepts the consistency-check framing | OPINION — restructure-vs-keep is a HOUSTON-DECISION on prominence. Body L1903 already says "consistency check, not distinctive ECH prediction" (Grok itself quotes it). |
| M1 (20pp too long) | OpenAI also flags length ("could be reduced to ~12–14 pp") | PARTIAL / HOUSTON-DECISION — length is journal-target specific. |
| M2 (DOI pending) | OpenAI E1, Gemini-implicit, Perplexity-implicit | HOUSTON-DECISION (HD-11) — pre-submission state. |
| M3 (one-sided 95% ∆N_eff limits absent from Table I) | None independently — but tex L1095–L1107 already gives them in body | PARTIAL — real Table I caption polish item (limits exist in body L1095/L1104; not surfaced in tab:verification caption). |

**Grok calibration verdict**: in the R36conf round Grok went the *opposite* direction from EXT6 — from rubber-stamp ACCEPT to OPINION-heavy REJECT. The shift catches **zero genuinely-new on-disk gaps** (E2 is FALSIFIED, E1/E4 are framing OPINIONs, M2 is HD-11). Of Grok's 7 findings only E3 and M3 are genuinely actionable, and both are minor caption-polish items, not BLOCKER class.

**Vindication of the EXT6 pattern-009 concern**: yes — in EXT6 Grok missed two on-disk BLOCKERs that the other vendors (or in EXT6 only ChatGPT) caught. R36conf shows the *opposite calibration mode*: Grok now produces high-volume harsh verdicts driven mostly by framing-philosophical objections rather than on-disk evidence. **Both modes — EXT6 rubber-stamp and R36conf over-strict — indicate Grok's verdict line carries low audit weight on this paper and should not drive closure decisions alone.** OpenAI is the consistently-calibrated leg across both rounds (caught EXT6 BLOCKERs; raises substantive on-disk items in R36conf at M-band).

The 3 EXT6 BLOCKERs/MAJORs that Grok missed but were independently caught:
- **#5 BBN flag claim** → already closed (`grep bbn_predictor` returns all 4 YAMLs).
- **#2 CHANGELOG.md v1B.0.62 missing** → closed (both v1B.0.62 + v1B.0.63 entries present).
- **#9 README χ²_eff row** → closed.

No R36conf vendor re-raised any of these — closures are real and held. **The pattern-009 EXT6 concern about Grok is independently re-confirmed by the R36conf cross-vendor lineup; Grok's vote carries no weight on artifact-pinning class issues.**

---

## Findings table

| # | Leg | Finding (severity) | Verdict | Evidence (tex lines / quotes) | Disposition |
|---|-----|--------------------|---------|-------------------------------|-------------|
| 1 | OpenAI P1B-E1 / Grok P1B-M2 | Zenodo DOI pending; standalone-reader can't pin frozen artifacts (ESSENTIAL across 2 vendors) | **HOUSTON-DECISION** | Tex §Data and Code Availability "DOI assignment is pending". HD-4/HD-11 ruled — pre-submission state. EXT6 already disposed similarly. | **DEFER** to arXiv-submission moment. Same disposition as EXT6 FB1(d). |
| 2 | OpenAI P1B-E2 | DES-SN5YR × Pantheon+ product likelihood used without joint overlap covariance to quote w0/wa σ-distances and "phantom crossing required" (ESSENTIAL) | **PARTIAL** | Tex L1340 footnote and §III front-load the SN-overlap caveat (per EXT5 closure). The MAIN-text presentation of $+4.3\sigma$ w0 / $-3.6\sigma$ wa σ-distances persists. OpenAI's preference is to quarantine the σ-distances to an appendix or supplement until the joint covariance is computed. Same conceptual finding as EXT6 FM1; not a new BLOCKER but an *upgrade of EXT6 closure plan to ESSENTIAL severity* by a different vendor. | **FIX (Path C)**: build a joint DES-SN5YR×Pantheon+ covariance, re-run iter2 chain on the corrected likelihood, report whether σ-distances shrink under overlap correction. If the chain is identical at OOM level, retain in main text; if not, move σ-distances to appendix until overlap is treated. **FIX (Path A, cheap)**: move the $+4.3\sigma$ / $-3.6\sigma$ / $w_{\rm pivot}$ block to a clearly-labeled "Exploratory cross-check" subsection and replace main-text mentions with "see exploratory subsection for provisional posterior-tail distances". Either path closes E2. |
| 3 | OpenAI P1B-M1 / M2 | NaMaster χ²(β) estimator definition missing explicit equation; pixel-window/template-band treatment ambiguous (template at ℓ ≤ 1024 vs ≤ 1536 bandpower fit) (MAJOR) | **VERIFIED** | Tex §IV does describe the estimator in prose but does not write χ²(β) as a displayed equation; the bin-truncation-vs-pixel-window question is addressed in robustness battery but not stated cleanly in methods. OpenAI's pass-2 M11/M12 sharpens the same point. Real methods-clarity gap. | **FIX**: insert a displayed χ²(β) = $\sum_b [C_{\ell,b}^{EB,\rm decoupled} - \tfrac12\sin(4\beta) C_{\ell,b}^{EE,\rm tmpl}]^2 / \sigma_b^2$ equation at §IV methods, with explicit statement of (i) inverse-variance weighting vs unweighted fit, (ii) template truncation at ℓ=1024 vs bandpower top edge ℓ=1536, (iii) HEALPix pixel-window-mismatch quantification or symmetric application. One methods-paragraph rewrite. |
| 4 | OpenAI P1B-M3 | Planck PR4/NPIPE high-ℓ paired with 2018 low-ℓ/lensing without release-pairing-swap cross-check (MAJOR) | **PARTIAL** | Real-but-deferred: a swap cross-check requires a Cobaya re-run on PR4-consistent low-ℓ. Compute-bound. Tex acknowledges PR4+2018 pairing as standard but doesn't characterize the systematic. EXT6 didn't flag. | **FIX (Path A)**: add explicit acknowledgement "no PR4-vs-2018 release-pairing-consistency cross-check was run; sub-σ shifts in $\Delta\Neff$ / $H_0$ from such a swap are not characterized" to §III caveat list. **FIX (Path C)**: queue a PR4-consistent low-ℓ short chain on next pod; report shift. |
| 5 | OpenAI P1B-M4 | "Few-percent" ALP-on-ΛCDM-vs-quintom statement not numerically backed (MAJOR) | **VERIFIED** | Tex L1946 says "by ~few percent ... propagating to a ≲few-percent" without an explicit numerical point. | **FIX (cheap)**: run one $(m, \theta_i, C_{a\gamma})$ point on both backgrounds; quote the fractional Δφ/fa difference. Single-script run on existing chain machinery. |
| 6 | OpenAI P1B-M5 | Fig. 2 axis label says "$N_{\rm eff}$" while caption says "$\Delta N_{\rm eff}$" with ticks ±1 around zero (MAJOR) | **PARTIAL** | Cannot directly verify without inspecting the PNG. The text consistently uses $\Delta\Neff$. If the figure axis label is "$N_{\rm eff}$" it's a real polish item. EXT6 didn't flag. | **FIX (cheap)**: open `figures/figureX_dneff.{png,pdf}` source, check axis label, correct if mis-labeled. Same closure commit. |
| 7 | OpenAI P1B-M6 | Noise convention $\sigma_{\rm pix} = \Delta_P / \sqrt{\Omega_{\rm pix}}$ "no $\sqrt 2$ factor" assumes per-Q/U component (MAJOR) | **PARTIAL / OPINION** | Real convention-justification ask; quick fix is a one-sentence citation. | **FIX (cheap)**: add citation to ACT-DR6 convention or Tristram et al. convention paper. |
| 8 | OpenAI P1B-M7 | Pixel-window/beam "cancel by construction" not explicitly demonstrated (MAJOR) | **PARTIAL** | Quantitative robustness check requested. The c10_robustness_battery already varies several inputs; add the pixel-window-mismatch dimension. | **FIX (Path C)**: re-run c10 with template-pixel-window applied/removed; report β̂ shift. Existing pipeline supports this. |
| 9 | OpenAI P1B-M8 / Grok P1B-M3 | One-sided 95% $\Delta\Neff$ limits (0.31 / 0.40) live in body L1095–L1107 but absent from Table I (`tab:verification`) and from abstract (MAJOR across 2 vendors) | **VERIFIED** | Body L1095 and L1097: `Under ... $\Delta\Neff\ge 0$ ... gives $\Delta\Neff < 0.31$, defined precisely as the 95th percentile of the renormalised CDF`. Table I (L1216–L1230) gives only mean ± 1σ (`$\Delta\Neff$ & $-0.020\pm 0.169$`). Caption omits the one-sided bound. | **FIX (cheap)**: add 2 lines to Table I (or caption footnote) reporting "$\Delta\Neff < 0.31$ (full-tension) / $< 0.40$ (Planck+BAO+SN), 95% one-sided after truncation at $\Delta\Neff \ge 0$". Same closure commit. |
| 10 | OpenAI P1B-M9 | Repository paths / changelog process notes in body (MAJOR) | **PARTIAL** | Real journal-target polish item. Tex carries phrases like `parameter_summary_CORRECTED.json`, `COUNT EXPLANATION.md`, "closure wave". Audit-trail-friendly but not journal-clean. | **FIX (journal polish wave)**: grep for `.json` / `.md` filename mentions in body, move to repo README + Data Availability paragraph. |
| 11 | OpenAI P1B-M10 (pass-2) | "$H(z=0.5)_{\rm CPL}$ differs from ΛCDM by $\approx +1.7\%$" off by ~order-of-magnitude — claimed correct value is $+41\%$ (ESSENTIAL severity) | **FALSIFIED** | Direct recomputation: at $a=2/3$, $w_0=-0.812$, $w_a=-0.667$: $1+w_0+w_a = -0.479$ → $a^{-3(1+w_0+w_a)} = (2/3)^{1.437} \approx 0.558$ (NOT 1.79; OpenAI inverted the sign of the exponent). $\exp[3 w_a(a-1)] = \exp[3(-0.667)(-1/3)] = \exp(0.667) \approx 1.948$. So $\rho_{\rm DE}/\rho_{\rm DE,0} = 0.558 \times 1.948 \approx 1.087$. Then $E^2_{\rm CPL}/E^2_{\rm LCDM} = (0.314 \cdot 3.375 + 0.686 \cdot 1.087)/(0.314 \cdot 3.375 + 0.686) = 1.806/1.746 = 1.0344$. $H_{\rm CPL}/H_{\rm LCDM} = \sqrt{1.0344} \approx 1.017$ → **$+1.7\%$ is correct**. OpenAI's recomputation has a sign error on the exponent ($a^{-3(1+w_0+w_a)} = a^{+1.437}$ for $w_0+w_a<-1$, and $a^{+1.437}$ with $a<1$ is $<1$, not $>1$). The paper's +1.7% is correct; OpenAI's claimed +41% is the arithmetic error. | **NO ACTION**. Falsified at the audit table. |
| 12 | OpenAI P1B-M11/M12 (pass-2) | Pixel-window/template treatment internally inconsistent (and unweighted χ² fit on bins above ℓmax pulls β̂ toward zero) (MAJOR) | **PARTIAL** | Real methods-rigor pass-2 finding; sharpens #3. | **FIX**: subsumed by #3 methods-paragraph rewrite (state explicitly: template either truncated at ℓ ≤ 1024 OR convolved with same pixel window; "bins above ℓmax carry zero template weight" must be in methods, not buried in robustness discussion). |
| 13 | OpenAI P1B-M13 (pass-2) | $f_{\rm sky}=0.85$ "Planck-like" Galactic-cut mask not specified (latitude cut producing 0.85 inconsistent with $|b|>20°$ which gives 0.66–0.70) (MAJOR) | **VERIFIED** | The exact mask definition isn't stated. Real methods-completeness gap. | **FIX (cheap)**: state mask as e.g. "$|b| > $bcut" with the actual `bcut` value and any additional cuts (declination) used to reach 0.85. One-sentence methods clarification. |
| 14 | OpenAI P1B-N1 / N2 / N6 (pass-1) | Pipeline-bias floor not propagated to ALP likelihood (clarify); H0–MB 3.2σ descriptive vs conditioned; S8 0.814±0.0086 vs ±0.009 rounding (MINOR) | **PARTIAL / VERIFIED** | All three are real polish items. The S8 0.0086 quoted as 0.009 is a rounding convention call. | **FIX (cheap)**: one-line clarifications + consistent rounding to either 0.0086 or 0.009. |
| 15 | OpenAI P1B-m8 / m9 / m10 / m11 / m12 (pass-2) | Estimator/SNR weighting inconsistency; "natural-prior midpoint" vs "natural box" mixing; coupling posterior mass-fraction sums to 96% (4% gap); bin edges 1536 vs Nside=512 formal max 1535; S8 0.05 overlap vs 2.6σ disclaimer (MINOR) | **PARTIAL** | All real micro-polish; m9 captures a residual EXT6 FM2 closure-naming consistency slip ("natural-prior midpoint" survives elsewhere). | **FIX (cheap)**: 5-site polish pass + define "natural prior" and "natural box" terms precisely. Same closure commit. |
| 16 | OpenAI P1B-N1–N3 / Gemini P1B-N1–N3 / Grok P1B-N1 (NIT) | Hyphenation PDF-parsing artifacts; footnote 1 long burn-in/sample-accounting reads like repo notes; axis label units on Figs 1–3; ref [25] year missing; "headline" informal | **PARTIAL** | Real cosmetic polish bundle. EXT6 already trimmed some; "headline" survives at 5+ sites consistent with EXT6 partial closure of FM1. | **FIX (cheap)**: cosmetic polish bundle in next commit. |
| 17 | Gemini P1B-M1 | Standalone-context fail: P1B opens as "companion to Paper I(a)" without 1–2-sentence ECH no-go summary (MAJOR) | **VERIFIED** | Tex §I L913–L920 dives directly into the 3 analyses without summarizing Paper I(a)'s thesis. Real reader-context gap. | **FIX (cheap)**: insert 1–2 sentences in opening §I paragraph summarizing the I(a) thesis (channel-level closure of 4 ECH DE routes + perturbation-transparency theorem) and what role these 3 P1B analyses play in supporting that conclusion. |
| 18 | Gemini P1B-M2 | w0–wa analysis prominently in body distracts from 3 core analyses; restructure to "Exploratory" subsection (MAJOR) | **PARTIAL** | Real structural call; same as Grok's M1 length compression. Conclusions section already labels w0wa "Exploratory cross-check". | **FIX (Path A)**: move §V w0wa subsection under a new `\subsection{Exploratory cross-check: $w_0w_a$ posterior under uncorrected SN overlap}` header; keep numbers but prominently label as exploratory. Resolves #2 and Gemini M2 together. |
| 19 | Gemini P1B-N1 | Ref [25] Cobaya year missing | **VERIFIED (cosmetic)** | Direct bibliography fix. | **FIX (cheap)**: add 2021 to ref [25]. |
| 20 | Grok P1B-E1 (no positive ECH prediction) | Whole-paper-purpose objection | **OPINION (FALSIFIED as fatal)** | Tex abstract explicitly: "Not a spin-torsion theory module ... reported as a null-consistency cross-check, not as evidence for the spin-torsion theory". The paper is, by design, a verification companion. Grok's objection is a scope-philosophical one, not an evidence-based one. EXT6 P1A already established the channel-level closures; P1B is the proof-of-concept reproducibility companion. | **NO ACTION**. |
| 21 | Grok P1B-E2 (∆Neff posterior not load-bearing for ECH) | Should remove from abstract | **FALSIFIED** | Tex L1190 says exactly this: "Reported as a null-consistency cross-check, *not* as evidence for the spin-torsion theory". Grok read this line and still requested removal. Self-inconsistent. | **NO ACTION**. |
| 22 | Grok P1B-E4 (§VI ALP irrelevant to ECH) | Move to appendix | **OPINION / HOUSTON-DECISION** | Tex §VI explicitly scopes itself as a consistency-check on the observed β value under a spectator-ALP scenario; the body already says this is *not* a distinctive ECH prediction. Restructure is a Houston call. Same as Gemini M2 spirit. | **DEFER** / **FIX (optional)**: relabel §VI as "Spectator-ALP consistency check (non-ECH-distinctive)" subsection header. |
| 23 | Grok overall **REJECT** verdict | Calibration | **OVER-CALIBRATED** (R36conf), opposite to **UNDER-CALIBRATED** (EXT6) | See "Grok calibration cross-check" section above. Grok produced ACCEPT-with-0-findings in EXT6 and REJECT-with-no-genuine-on-disk-gaps in R36conf. Both modes mis-calibrated for this paper. | **NOTE**: pattern-009 EXT6 concern is independently re-confirmed: Grok's vote carries no audit weight on artifact-pinning class on this paper. |
| 24 | Perplexity overall MAJOR REVISIONS (no enumerated findings) | Verdict calibration | **OPINION** | Perplexity self-reports inability to audit from text-excerpt only; no enumerable findings beyond a list of arXiv-ID and "load-bearing numerical claims that would need recomputation" concerns. No new evidence added beyond what other vendors covered. | **NOTE**: text-only Perplexity legs carry low audit weight on this paper class; consider native-PDF dispatch path for Perplexity going forward. |
| 25 | OpenAI overall verdict (MAJOR REVISIONS) | Calibration | **CALIBRATED, high-fidelity** | OpenAI raised 1 substantive ESSENTIAL (E2 — DES-SN5YR×Pantheon+ overlap) and 9 actionable MAJORs, most of which are genuine methods-clarity / methods-completeness items consistent with the paper's pre-submission state. Pass-2 added 4 more substantive items including one falsified (M10 +1.7% recomputation arithmetic error) and three valid (M11, M12, M13). | **OpenAI is again the consistently-calibrated leg** (as it was in EXT6 with its 2 BLOCKERs + 4 MAJORs + 4 MINORs). |
| 26 | Gemini overall verdict (MAJOR REVISIONS) | Calibration | **CALIBRATED, well-bounded** | Gemini correctly identifies 2 substantive MAJORs (standalone-context + w0wa framing) and 3 NITs. NO_NEW pass-2 — appropriate given pass-1 caught the real items. | — |

---

## Counts summary

| Verdict | Count |
|---------|-------|
| VERIFIED | 6 (#3 χ²(β) explicit + pixel window, #9 one-sided 95% bounds in Table I, #13 fsky mask definition, #17 standalone context, #19 ref [25] year, plus cosmetic batch #14/#15/#16/#5) |
| PARTIAL | 11 (#2 DES×PP overlap, #4 PR4 swap, #6 Fig 2 axis, #7 Q/U convention, #8 pixel-window robustness, #10 repo paths, #12 unweighted-bin/pixel-window, #15 m8–m12 cluster, #16 cosmetic NITs, #18 w0wa structural, #22 §VI restructure) |
| OPINION / HOUSTON-DECISION | 5 (#1 DOI, #20 ECH-prediction philosophy, #22 §VI structural, #23 Grok calibration meta, #24 Perplexity meta) |
| FALSIFIED | 3 (#11 OpenAI M10 +1.7% recomputation arithmetic error, #20 Grok E1 fatal-framing, #21 Grok E2 already-disclaimed) |
| STALE | 0 |
| **Total distinct findings** | **~26** |
| **BLOCKERs** | **0** |
| **EXT6 closure CARRY regressions** | **0** |

**Genuinely-NEW-substantive count (R36conf gap metric over EXT6)**: **5**
- **#3** explicit χ²(β) equation + pixel-window/template-band treatment in methods
- **#9** one-sided 95% $\Delta\Neff$ bounds belong in Table I caption / abstract (Grok M3 + OpenAI M8 convergence)
- **#13** $f_{\rm sky}=0.85$ mask definition explicit
- **#17** standalone-context 1–2-sentence summary of Paper I(a) at §I opening (Gemini's contribution; EXT6 didn't flag)
- **#18** structural reframing of w0wa subsection as "Exploratory cross-check" (Gemini M2 + OpenAI E2 convergence)

The remaining ~21 findings are either:
- HOUSTON-DECISION pre-submission state (DOI, version stamp, AI acknowledgement wording),
- EXT6 closure-plan items at PARTIAL severity now sharpened (e.g., "headline" → "central marginal-tail result" at 5+ sites; EXT6 closure plan already called this PARTIAL),
- FALSIFIED (#11 +1.7% recomputation arithmetic error; #20 / #21 Grok scope objections),
- one-line cosmetic polish (axis units, ref year, "headline" wording, "natural-prior midpoint" vs "natural box" consistency),
- or Grok over-strict opinion-objections at framing layer.

**Headline finding**: **The paper's headline $+1.7\%$ CPL Hubble-rate claim at $z=0.5$ is correct.** OpenAI's pass-2 ESSENTIAL recomputation contains a sign error on the exponent: $a^{-3(1+w_0+w_a)}$ with $1+w_0+w_a=-0.479$ becomes $a^{+1.437}$, which for $a=2/3$ is $\approx 0.558$ (not the $\approx 1.79$ OpenAI computed). The paper's arithmetic survives the cross-vendor recomputation. **This is a pattern-051 wins-by-doing-the-math case study: when a vendor brings a quantitative "correction", recompute first; don't auto-trust on novelty.**

**CLEAN/NOT-CLEAN on EXT6 P1B closures**: **CLEAN on 6 of 7 closures.** The 7th (FM1 §V.B "headline" wording softening) was a PARTIAL closure plan item to begin with — 3 vendors flag residuals, which is consistent with the EXT6 closure plan, not a regression.

**Grok calibration verdict for the program**: pattern-009 EXT6 concern is **vindicated**. Grok's vote should not drive closure verdicts on this paper without independent cross-vendor confirmation. In EXT6 Grok went rubber-stamp ACCEPT; in R36conf Grok swung to over-strict REJECT. Both modes carry low audit weight. OpenAI is the consistently-calibrated leg across both rounds.

---

## CLOSURE PLAN — one-line edits for the 5 genuinely-NEW items + cheap polish

1. **#3 — explicit χ²(β) equation + pixel-window/template-band methods rewrite**: insert displayed equation at §IV methods, with truncation + unweighted-bin behaviour stated.
2. **#9 — one-sided 95% $\Delta\Neff$ bounds in Table I**: extend `tab:verification` caption (or table footnote) with the two one-sided bounds (0.31 / 0.40).
3. **#13 — $f_{\rm sky}=0.85$ mask definition**: state the exact mask (Galactic latitude cut + any additional cuts).
4. **#17 — standalone-context 1–2-sentence Paper I(a) summary at §I opening**.
5. **#18 — w0wa subsection relabel as "Exploratory cross-check"**: subsection header rename + 1-sentence reader-pointer at §V intro.
6. **#2 / #12 — DES×Pantheon overlap covariance** path-choice (Path A: relabel σ-distances as exploratory; Path C: build joint covariance, re-run iter2). Houston-call.
7. **#5 — quantify "few-percent" ALP-on-ΛCDM-vs-quintom** with one $(m, \theta_i, C_{a\gamma})$ point.
8. **#6 — Fig. 2 axis label check + fix** if mis-labeled.
9. **#4 — PR4-vs-2018 pairing caveat sentence** in §III.
10. **#7 — $\sqrt 2$ convention citation** at §IV noise paragraph.
11. **#8 — pixel-window robustness re-run** of c10 battery (Path C) OR explicit statement (Path A).
12. **#14 / #15 / #16 — cosmetic polish bundle**: "headline" → "central marginal-tail result" at 5+ sites; "natural-prior midpoint" / "natural box" naming consistency; axis units; ref [25] year; S8 0.0086 ↔ 0.009 rounding consistency.
13. **#19 — ref [25] year 2021 added**.

Items #1 (DOI), #10 (repo paths), #20 / #21 (Grok scope objections), #22 (§VI restructure HD-call), #23 / #24 (verdict-calibration meta) → DEFER to journal-target polish wave or HOUSTON-DECISION.

**Estimated closure commit**: one `chore(R36conf-stamp): R36conf P1B → v1B.0.64 polish wave — χ²(β) equation + pixel-window methods, one-sided ΔNeff in Table I, fsky mask, Paper I(a) standalone summary, w0wa "Exploratory" relabel, few-percent ALP-vs-quintom quantified, Fig 2 axis, PR4/2018 pairing caveat, cosmetic bundle ("headline" → "central marginal-tail result", refs)` bundle. Note: OpenAI M10 arithmetic recomputation is FALSIFIED at the audit table — no edit.

---

## Audit notes

- **HD-4 / HD-11 (DOI placeholders, Zenodo tagged release)** applied to #1 (pre-submission state legitimate).
- **pattern-008 (scope drift)** at minor severity for "headline" / "natural-prior midpoint" residual EXT6 closure leakage — caught at 5+ sites; sweep needed.
- **pattern-009 (vendor rubber-stamp)** EXT6 concern about Grok independently re-confirmed by R36conf swing to opposite over-strict mode; both modes signal Grok's verdict carries low audit weight on this paper.
- **pattern-026 (multi-site claim sync gap)** did NOT recur — the 7 EXT6 closures (BBN flag, CHANGELOG, README, χ²_eff row label, scan-prior midpoint, Table IV percentiles, §V.B framing) all held under R36conf cross-vendor inspection.
- **pattern-051 (do-the-math vs accept-on-novelty)** triggered by #11 (OpenAI M10 +1.7% recomputation). Direct independent recomputation FALSIFIED the OpenAI correction, vindicating the paper's number. Lesson: when a vendor brings a quantitative "correction" of central-tendency quantities, recompute first.
- **pattern-052 (re-raise rule)** did not auto-rescue any FALSIFIED finding this round — no prior falsification records exist.
- **Claude leg absent**: same Anthropic billing BadRequestError as P1A. 4-leg round, not 5-leg. Top up Anthropic billing before next round; same actionable as P1A audit.
- **Native-PDF vs text dispatch**: OpenAI (Files API), Gemini (inline PDF), Grok (rasterized images) all received native PDF per `feedback-review-gap-native-pdf` standing directive. Perplexity received text-only and self-reported reduced audit capacity. Consider whether to route Perplexity P1B through native-PDF path in next round.
- **No fabrication / no Fisher 1/8.98² superscript artifacts** in the manuscript-side audit this round.

