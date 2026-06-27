# R56 P1B — Truth Audit (HARDENED / de-biased re-review)

Source: `arxiv/paper1b_mcmc_companion.tex` @ v1B.0.78
PDF: `/tmp/R56_P1B/paper1b_mcmc_companion.pdf` (22 pp, md5 f5f3c8ad), 0 undef, 0 overfull.
Vendors: OpenAI (MAJOR REV), Gemini (MAJOR REV), Grok (REJECT), Perplexity (quota-fail 401), + own Opus read.
Standard: same high PRD/MNRAS bar throughout; self-favoring reporting / unstated assumption / uncontrolled
systematic / internal inconsistency = real finding (MINOR min). Patterns 061-064 used to filter genuine
false-positives only.

## Verdict-first adjudication

| # | Vendor finding | Tier asked | Verdict | Evidence |
|---|----------------|-----------|---------|----------|
| 1 | w0wa σ-distances rest on overlap-uncorrected DES-SN5YR×Pantheon+ product likelihood; must be REMOVED from main text (OpenAI ESSENTIAL, Gemini ESSENTIAL) | ESSENTIAL | **VERIFIED-INTACT / already-closed; "remove entirely" = OPINION** | The systematic is fully DISCLOSED, not concealed: §sec:w0wa_crosscheck (L2166-2195) headlines it a "caveated overlap-uncorrected diagnostic"; every σ-distance labeled "marginal-tail posterior-extrapolation distances, diagnostic only — not detection significances and not suitable for model selection" (Table II caption L1468, fn:wcaveat L1474); "no model-selection claim is made". INTEGRITY_CLOSURE_2026-06-26 #5 promoted the caveat to the result headline TODAY. Directive: integrity-fix intact, do not reopen. The referees' "delete from main body" is a stronger PRD-acceptance editorial preference, not an integrity defect — the favorable number is reported stripped of inferential weight, the opposite of a hidden self-favoring choice. The overlap-aware joint-covariance refit is TRULY-BLOCKED (new MCMC) → correctly deferred. |
| 2 | -0.032/-0.040° "pipeline bias floor" mischaracterized as pipeline/MASTER bias despite being estimator-dependent and largely removed by proper weighting (OpenAI ESSENTIAL) | ESSENTIAL | **FALSIFIED** | Body §sec:data_cmb robustness battery EXPLICITLY discloses the estimator attribution: inverse-variance-weighted fit recovers β̂=0.264° (bias -0.006°), "removing ≈80% of the bias — the unweighted fit's equal weighting of noise-dominated high-ℓ bins is the dominant contribution" (L2023-2027); unweighted estimator deliberately retained only "to match the estimator configuration used in the public NaMaster driver scripts released by the published birefringence analyses" for comparability (L2060-2069). Abstract labels it "pipeline-recovery bias … not sky-measurement systematics" (L1115-1117). Headlining the LARGER bias is the conservative direction, not self-favoring. Disclosure adequate. |
| 3 | Abstract claims a 3.6σ Hubble-tension reduction, contradicted by body (Grok REJECT) | BLOCKER | **FALSIFIED (misread)** | Abstract states the OPPOSITE: "the ΔNeff extension does not reduce the residual ~3.6σ tension with the SH0ES … H0" (L1104-1106). Grok inverted an explicit negation. |
| 4 | Abstract makes an ECH-specific birefringence claim, contradicted by body (Grok REJECT) | BLOCKER | **FALSIFIED (misread)** | Abstract states "The same birefringence arises in standard GR with an identical ALP; it is not a distinctive ECH prediction" (L1141-1143). Grok inverted an explicit negation. The "not self-contained / relies on unpublished companion" point is an OPINION about companion-paper structure, disclosed in title/intro. Grok REJECT rests entirely on two falsified misreads. |
| 5 | βfree=0.344°±0.10° uses only 720 samples (ESS≈265), flagged marginal but used for consistency checks (OpenAI/Gemini MINOR) | MINOR | **STALE / already-disclosed** | Disclosed at every use: Table (App, L2973) prints ESS≈265; text "marginal … should be interpreted with the caveat that ~720 accepted samples provides limited ESS" (L2978-2981); consistency statement is explicitly internal ("all three are constrained by the same single published β_obs, not independent measurements", L2634-2635). No new action. |
| 6 | Add SE of the 500-MC mean per robustness config (OpenAI MAJOR) | MAJOR | **STALE / already in text** | σ_β/√500 ≈ 0.0013°/0.0015° quoted and the canonical-mask differences shown as 0.8×/1.4× the SE (L2000-2003); per-config β̂ tabulated in the battery (L2014-2052). The requested one-line aggregate is effectively present. |
| 7 | Permanent DOIs required for deposited artifacts (OpenAI) | MINOR | **OPINION (pre-submission state)** | "DOI assignment is pending (identifiers will be inserted at submission)" (L2761). Standard pre-arXiv state. |

## Recurring false-positives (held FALSIFIED, per directive)
- HEALPix 47.21 → correct; LiteBIRD √ extraction-artifact → extraction noise. Neither re-raised this round.

## Net result
- **NEW VERIFIED DO-NOW: NONE.** No finding survives the hardened truth-audit as a new closable defect.
- Self-favoring item under the hardened bar? **NONE survives.** The two candidate "favorable headline" sites
  (w0wa σ-distances; -0.040° bias floor) are each reported in the CONSERVATIVE/de-rated direction with full
  in-paper disclosure: w0wa stripped of inferential weight ("diagnostic only, not for model selection");
  bias floor headlines the larger value and the body attributes 80% to the retained estimator choice.
- TRULY-BLOCKED (skipped): overlap-aware DES-SN5YR×Pantheon+ joint-covariance w0wa refit (needs new MCMC).
- Integrity-fix (w0wa SN-overlap caveat): VERIFIED INTACT, not reopened.

## Convergence statement
P1B is a mature, exhaustively-caveated companion. R56 reproduces the standing external split (referees press
for editorial REMOVAL of the fully-caveated w0wa diagnostic and tighter abstract framing) but surfaces zero new
integrity defects: every ESSENTIAL/MAJOR is either an already-closed/disclosed item, a falsified misread, or a
pre-submission/editorial OPINION. The manuscript has CONVERGED at the truth-audit level; no closure wave warranted.
