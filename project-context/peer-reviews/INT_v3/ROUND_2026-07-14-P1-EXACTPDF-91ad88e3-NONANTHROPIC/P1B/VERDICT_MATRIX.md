# P1B exact-PDF truth-audit matrix

Frozen target: P1B v1B.0.105 at commit `91ad88e36121da128175415f55be44d5e458f9f1`.

This matrix adjudicates every labeled finding in the OpenAI, Gemini, and Grok reports. The Codex GPT-5.6-sol/high findings are added below as a separate complete block so raw reviewer identifiers remain traceable.

## Verified publication/reproducibility items

| Finding | Raw IDs | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| Companion arXiv placeholder | OpenAI E2; Gemini E1 | **KNOWN SUBMISSION BLOCKER** | Reference 1 and several mentions retain `arXiv:XXXX.XXXXX`. It must be replaced during coordinated posting; this is known metadata, not a new science defect. |
| Dataset DOIs pending | OpenAI E3 | **KNOWN SUBMISSION BLOCKER** | Data Availability and Appendix A explicitly say DOI assignment is pending and give live Hugging Face URLs. Final persistent identifiers remain a submission task; none was fabricated. |
| Claimed “current snapshot” hash is stale | Gemini E2 | **VERIFIED — REAL MAJOR** | Lines 3070–3076 and 3221–3222 say `b22f8cc9` matches the present paper version. At that commit P1B was v1B.0.47; frozen target `91ad88e3` is v1B.0.105. The hash must be replaced by a release/tag that actually freezes source and artifacts. |
| Prior-predictive protocol is under-described in rendered paper | OpenAI E1; Grok E2 | **VERIFIED — REAL MINOR** | The rendered paper states priors, `11.6%/6.1%`, summary-likelihood caveats, and that the script is archived, but not seed/tolerance/full counting protocol in one place. Commit-pinned `alp_prior_predictive.py` and `alp_prior_predictive_result.json` exactly contain 100,000 draws/config, 0 failures, 0.11597/0.06137, and integrator agreement `2.49e-8 deg`; the numbers are traceable, so “unverifiable” is overstated. |
| “Systematic floor” remains locally ambiguous | OpenAI M1 | **VERIFIED — REAL MINOR** | Lines 2210–2216 call 0.040° a NaMaster systematic floor, then immediately limit it to foreground-free synthetic deconvolution bias and deny a real-sky floor. The qualification saves the claim, but “pipeline-recovery bias” throughout would be safer. |
| c15 rerun is not below the declared 0.01 convergence threshold | OpenAI m4 | **VERIFIED — REAL MINOR** | Lines 2437–2458 disclose `R-1=0.0147` and call c15 an independent robustness rerun, not a headline chain. The number is honest but should not be described as fully converged under the paper's stricter `<0.01` convention. |
| “Propagating torsion” wording conflicts with minimal ECH | OpenAI M9 | **VERIFIED — REAL MINOR** | Lines 1831–1840 say the full Holst sector has propagating torsion above a heuristic strong scale. Minimal Einstein–Cartan–Holst torsion remains algebraic; a UV completion may add propagating modes, but that is different and should be named. |
| Natural/SI units and kappa notation can be clearer | OpenAI m9, m10; n2 | **VERIFIED — REAL MINOR** | The paper uses a `κ²=8πG` convention and inserts `(ℏc)²` during a mainly natural-unit estimate. The definitions are recoverable, but notation/capitalization should be standardized. |
| Angle-SNR definitions are easy to confuse | OpenAI M5, m11 | **VERIFIED — REAL MINOR** | Text distinguishes template SNR, per-realization angle SNR, and SE-of-mean calibration significance, but several nearby values use recovered versus injected beta. A single explicit definition table would prevent misreading. |
| Table IV quantile presentation and Appendix-C mean/median wording | OpenAI m13, m14 | **VERIFIED — REAL MINOR** | Full-chain and subset `m/H0` summaries use different formats, and lines 3344–3349 mix posterior “medians” with the datum's “mean.” Both are presentational/statistical wording defects. |
| Coupling-prior rationale could be more direct | OpenAI m8 | **VERIFIED — REAL MINOR** | The Figure 6 caption and Appendix C explain `[4,60]`, posterior support, and the omitted small-displacement tail, but the rationale is distributed rather than stated once at first use. |
| Repeated internal process/provenance prose | OpenAI m3, m6, n4; Grok N1, NIT1 | **OPINION/VENUE** | The “diagnostic/not headline,” bug history, file paths, repeated null wording, and burn-in hyphenation are transparent provenance. Compression is editorial, not a correctness defect. |

## Falsified, stale, or misread findings

| Finding | Raw IDs | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| NaMaster estimator uses `1/4 sin(4β)` | Gemini M1 | **STALE/MISREAD** | Frozen Eq. (4), rendered page 7 and source lines 2152–2163, uses `1/2 sin(4β)` and explicitly identifies it with `sin(2β)cos(2β)`. The reviewer read an obsolete version/extraction. |
| Figure 2 x-axis says `N_eff`, not `ΔN_eff` | OpenAI E4 | **STALE/MISREAD** | Direct visual inspection of frozen rendered page 7 shows `ΔN_eff` on panel (a); caption and source agree. |
| LiteBIRD uncertainty combination omits squares | OpenAI E5; n5 | **STALE/MISREAD** | Frozen source line 2968 and rendered PDF show `sqrt(0.03²+0.094²)`, yielding about 0.7 sigma. This was a PDF extraction misread. |
| One-sided Delta-Neff truncation is undocumented/ad hoc | Grok E3 | **STALE/MISREAD** | Rendered pages 3 and 6 define nonnegative-posterior renormalization, 95th percentile, the raw mildly negative mode, and both limits; Table II caption repeats the procedure. Whether to emphasize two-sided intervals is editorial, not missing methodology. |
| One-sided limits absent from Table II | OpenAI m1 | **STALE/MISREAD** | Table II caption explicitly reports 0.31 and 0.40 and defines the truncated CDF. |
| Headline estimator differs from the one applied to real data | Grok E4 | **STALE/MISREAD** | The manuscript never claims a real-sky reanalysis. It declares the unweighted estimator as its synthetic canonical baseline for comparison and reports inverse-variance weighting in the robustness battery; abstract explicitly says synthetic and not a real-sky systematic floor. |
| Tension anchors are not tested separately | Grok M3 | **STALE/MISREAD** | Table II compares full-tension with Planck+BAO+SN (anchors removed); both return Delta-Neff consistent with zero and nearly identical H0. |
| Companion derivation is load-bearing | Grok M2 | **STALE/MISREAD** | Sec. III derives the contact scaling needed for the proxy and repeatedly states no ECH likelihood module is implemented. P1B's numerical outputs stand on its own frozen chains/scripts; the companion supplies motivation. |
| Prior dependence is not disclosed | OpenAI M7 | **STALE/MISREAD** | Abstract calls it a prior-predictive prior-volume cost; Sec. VI begins with a bold prior-sensitivity disclaimer; Table IV and Appendix C state summary-likelihood/prior dependence. |
| Sample counts conflict | OpenAI m5 | **STALE/MISREAD** | Lines 1790–1805 reconcile 309,189 raw, 216,432 nominal 30% post-burn, 123,368 full-tension nominal, 123,129 chain-end-truncated, and 119,617 GetDist-weight-thinned. Fig. 1 correctly labels the last quantity. |
| Reduced Planck mass is undefined | OpenAI m2 | **STALE/MISREAD** | Table I and Sec. III define the reduced Planck convention used in P1B. This does not import P1A's separate unreduced-mass error. |
| Delta-Neff/H0 significance phrasing conflates datasets | OpenAI m7, n1 | **STALE/MISREAD** | Table II and surrounding text distinguish the two frozen stacks and quote their own uncertainties; “0.01 sigma agreement” is a transparent derived comparison, not a separate detection claim. |
| Spectator fractions lack small-angle boundary validation | OpenAI M8 | **OUT-OF-SCOPE/DISCLOSED** | The committed ALP forward model solves the nonlinear `sin(theta)` equation; the paper's analytic onset/scaling approximation is explicitly a classification aid and reports threshold dependence. A new full boundary-validation suite could strengthen robustness but is not evidence that the committed fractions are false. |
| Noise-level, l-binning, or identical-likelihood reruns are missing | OpenAI M2–M4 | **OUT-OF-SCOPE/DISCLOSED** | Secs. IV–V enumerate the completed robustness battery and explicitly disclose the single noise model/binning and PR4/2018 pairing. The c15 likelihood substitution is labeled a robustness rerun, not identical replication. These are requested new analyses. |
| SNR/angle units are wrong | OpenAI m12; n5 | **OPINION/VENUE** | Radians are dimensionless but labeling a numerical angle “rad” is conventional. Definitions can be polished; no numerical result changes. |
| Corner-plot parameter abbreviations are undefined | Grok N2 | **STALE/MISREAD** | Table I on the preceding page defines all seven parameters; standard `n_s`, `tau`, and related labels need not be repeated inside the small panel. |

## Venue/editorial findings

| Finding | Raw IDs | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| Null/reproducibility studies lack PRD novelty | Grok E1 | **OPINION/VENUE** | The paper's contribution is reproducible quantitative scope control, not evidence for ECH. Journal novelty is a referee/editor judgment, not a technical falsification. |
| Manuscript should be at most eight pages | Grok M1 | **OPINION/VENUE** | No universal eight-page PRD technical-note limit was established. Length is an editorial choice; the detailed appendices support reproducibility. |
| Vendor-specific AI disclosure should be removed | OpenAI M6 | **OPINION/VENUE** | The disclosure assigns sole author responsibility and lists the actual workflow. Final journal policy controls format; transparency is not a methodological defect. |

## Codex GPT-5.6-sol/high independent findings

The initial subscription run reviewed all 21 rendered pages and exact commit artifacts, completed 66 evidence items, and produced a 1.5 MB raw event stream. It was interrupted only after a 12-minute post-tool final-synthesis stall. A bounded no-tool GPT-5.6-sol/high retry synthesized that frozen evidence; both the partial and retry event logs are retained.

| Finding | Raw ID | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| Surrogate ALP posterior is normalized over non-spectator points | Codex E1 | **VERIFIED — GENUINELY NEW BLOCKER** | The likelihood fixes the Lambda-CDM background and never feeds derived `Omega_a` into `H(z)`, although much of the full chain has `Omega_a~0.1–1`. The `<0.01` conditional subset is controlled, but 13.3818% is a survival fraction of the surrogate chain, not a physical posterior probability/prior cost because its denominator includes internally inconsistent points. Closure can be bounded: label it a surrogate validity diagnostic or rerun with background consistency. |
| NaMaster bandpower/theory-template mismatch | Codex E2 | **VERIFIED — GENUINELY NEW BLOCKER** | The code fits decoupled broad bandpowers against `C_ell^EE` sampled at bin effective centers instead of passing theory through the identical bin/window operator. Existing weighting, lmax, BB, mask, and apodization checks do not test this. The ~12% bias attribution and 0.040° “floor” require a correctly windowed-theory rerun; raw current-estimator outputs remain factual. |
| Stale snapshot hash | Codex M1 | **VERIFIED — REAL MAJOR** | Independently confirms Gemini E2: `b22f8cc9` is v1B.0.47, not reviewed v1B.0.105. |
| Table IV mixes stale beta values and unidentified ESS markers | Codex M2 | **VERIFIED — REAL MAJOR** | Exact c5 chain gives `Omega_a<0.1` beta mean/std 0.31471/0.10258 and median 0.31909, not manuscript 0.328±0.100. Full 0.32629±0.09899 and `<0.01` 0.27595±0.09880 check. Weight-expanded Sokal estimates show the 1989/461 ESS values do not use one declared marker; no committed generator reproduces them. |
| c15 threshold, propagating-torsion wording, statistical terminology | Codex m1–m3 | **VERIFIED — REAL MINOR** | Confirms the bounded issues already cataloged: `R-1=0.0147`, algebraic minimal-ECH torsion, and inconsistent mean/median/SNR/ESS/floor terminology. |
| Core null-chain arithmetic and prior-predictive numbers | Codex N1 | **STALE/MISREAD** for contrary reviewer findings | Independently confirms the frozen means/errors, truncation, counts, `1/2 sin(4 beta)`, LiteBIRD formula, Figure 2 label, and 11.597%/6.137% prior-predictive outputs. |
| Optional extra reruns, venue, AI disclosure | Codex N2–N3 | **OUT-OF-SCOPE/DISCLOSED** or **OPINION/VENUE** | Does not promote general requests or style preferences to technical blockers. Hugging Face links resolve. |

## Round disposition

The direct-vendor legs alone missed two consequential implementation/interpretation defects that the exact-artifact Codex leg exposed. P1B is **not publication-ready**. Its stock-CAMB null result, truncation/count arithmetic, prior-predictive calculation, and raw chain-cut fractions survive. The ALP 13% quantity must lose its physical posterior/prior-cost interpretation unless the background is made self-consistent; the NaMaster bias/floor needs a correctly binned-theory rerun; Table IV and the stale snapshot must be regenerated. Honest recommendation: major revision (or reject-and-resubmit if binary), not acceptance.
