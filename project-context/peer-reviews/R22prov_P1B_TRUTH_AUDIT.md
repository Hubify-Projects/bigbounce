# R22prov P1B TRUTH AUDIT — v1B.0.49 (12pp), 2026-06-09

**Per-finding verdicts per `feedback_peer_review_truth_audit_protocol`.** All verdicts checked
against `arxiv/paper1b_mcmc_companion.tex` (v1B.0.49), the on-disk chain `.input.yaml`s,
`reproducibility/p1_namaster_500mc/` artifacts, `arxiv/references.bib`, and rendered figures
(pdftoppm). 185 raw findings (incl. Gemini duplicate blocks) → ~100 distinct findings audited.

**ROUND VERDICT: NOT CLEAN.** 6 VERIFIED ESSENTIAL/MAJOR-class clusters survive audit, including
two artifact-vs-prose contradictions the reviewers only partially saw (BAO dataset misattribution;
SNR-definition mismatch proven by the fsky-sweep JSON). A v1B.0.50 closure wave is required.

Verdict-class counts (distinct findings):
| VERIFIED | VERIFIED-LIKELY | PARTIAL | OPINION | STALE | FALSIFIED | HOUSTON-DECISION |
|---|---|---|---|---|---|---|
| 24 | 7 | 21 | 22 | 9 | 14 | 3 |

---

## (a) Consensus-group verdict table

| # | Group (vendors) | Sev | Verdict | Evidence | Fix class |
|---|---|---|---|---|---|
| G1 | `companion` — cites Papers I(a)/II/III/IV "in preparation"; companion to unpublished paper (Claude E1, Gemini M3, Grok N1, OpenAI n4, Perplexity E1/N13) | ESS | **HOUSTON-DECISION** (core) + PARTIAL (sub-items) | Program-level submission logistics: P1A+P1B are bundled for simultaneous arXiv posting; "in preparation" labels become arXiv IDs at submission. Gemini-M3 sub-item (PR3 headline anchor vs PR4 code) is *explicitly disclosed* in fn:eskilt_pr3_pr4 (tex L603–614) — disclosed-choice, OPINION. Internal IDs `hUBIFY-2026-00x` (refs [1],[4]–[6]) are a VERIFIED submission-stage cleanup (swap to arXiv IDs at bundle). | Submission-stage; no v1B.0.50 body edit |
| G2 | `table_ii` — Table 1B cluster (Claude E9/M4-Gem/E11-OAI + META-E3/M1 + OAI E1 + Gem m2 + Per M2/M13) | ESS | **VERIFIED (split below)** | See rows G2a–G2f | Mixed |
| G2a | w_pivot footnote algebra (Claude E9, Gemini M4, OpenAI E11) | ESS | **VERIFIED — MAJOR** | tex L848 fn:wpivot prints σ²=(0.0436)²+(0.3320)²(0.1864)²=(0.0301)². Direct compute: 0.00190+0.00383=0.00573 → σ=0.0757 ≠ 0.0301. Printed formula provably does not reproduce printed value. Correct decorrelation identity is σ²_wp = σ²_w0 − Cov²/σ²_wa (minus sign); under it the quoted 0.0301 implies \|Cov\|=0.0059, inside the Cauchy bound 0.00813 → the *value* is plausibly the true chain readout, the *formula and a_p sign convention* are wrong. OpenAI's Cauchy-violation arithmetic confirms the printed combination is impossible. | Fix footnote: correct identity + recompute/state Cov from chain |
| G2b | §V.A dataset list "(2) +DESI 2024 DR1 BAO" (OpenAI E1) | ESS | **VERIFIED — ESSENTIAL (upgraded by artifact)** | tex L1124–1125 claims DESI DR1 BAO for the ΔNeff combinations. Frozen full-tension chain `reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/chain_01/spin_torsion.input.yaml` L15–20: `bao.sdss_dr16_baoplus_{lrg,qso,lyauto,lyxqso}` + `bao.sdss_dr7_mgs` + `bao.sixdf_2011_bao` — **SDSS DR16, no DESI likelihood present**. All 4 repo YAMLs (`cobaya_*.yaml`) match SDSS. Only iter2 (Table 1B) uses `bao.desi_dr2.desi_bao_all` (verified in its input.yaml) — that caption is correct. The §V.A prose misattributes the frozen-chain BAO dataset. | Rewrite §V.A dataset list to SDSS DR16+6dF+MGS w/ correct cites; add per-chain dataset table |
| G2c | Age = 13.763 ± 0.019 Gyr implausible (META-E3) | ESS | **FALSIFIED** | Planck 2018 publishes Age = 13.797 ± 0.023 Gyr alongside σ(H0)=0.54 (0.8%) — same order as quoted here with *more* data (BAO+SN). The reviewer's "≳0.09 Gyr from H0 alone" assumes uncorrelated parameters; CMB acoustic-scale degeneracies cancel exactly as in Planck's own published error. | None |
| G2d | χ²_BAO = 10.6 ± 1.8 anomalously low (META-M1, Claude m21) | MAJ | **PARTIAL** | DESI DR2 BAO ≈ 13 data points → χ²/ν ≈ 0.8, unremarkable. Not an error; but N_data is unstated, so the value is uninterpretable as printed — reviewer's clarity ask is legitimate. | Add "(13 BAO data points)" to table footnote |
| G2e | Text/table value drift: H0 67.69 (L919) vs 67.68 (Table I L804); ΔNeff ±0.169 vs ±0.17 (L594–595, L805) (Gemini m2, Claude m15) | MIN | **VERIFIED** | Direct read; same chain quoted two ways. | Unify (mechanical sweep) |
| G2f | 4.3σ marginal-tail caveat coverage (Perplexity M2) | MAJ | **PARTIAL** | Table cell carries fn:wcaveat (L845) and L873–875 references it, but L1157 "headline result is w0…+4.3σ" carries no fn ref. Mostly closed in v1B.0.26; one uncovered site remains. | Add `(fn.~\ref{fn:wcaveat})` at L1157 |
| G3 | `future_date` — "Dated: June 9, 2026" + arXiv 2509.xxxxx/2507.xxxxx "future-dated" (Grok E1, Perplexity M8, Gemini E1) | ESS | **FALSIFIED** | It **is** June 9, 2026. arXiv 2509 = Sept 2025 and 2507 = July 2025 are *past* dates. Classic reviewer training-cutoff artifact (auto-FALSIFY rule). The cited entries are real: references.bib L447+ (DiegoPalazuelos2025, 2509.13654), L574+ (Liu et al. EPJC 2025, 2507.04265) — the same entries FALSIFIED 5 consecutive prior rounds (v1B.0.31–0.39 preamble log). | None |
| G4 | `length` — 12pp too long / condense to 5–8pp (Claude M9, Grok NIT1, Perplexity N13) | MAJ | **OPINION** | Scope/style preference against the Technical Verification Companion format Houston chose. Standing push-back since R26/R28. | None (Houston owns format) |
| G5 | `sigma_mixing` — fsky-sweep σ_β does not scale (Claude M12/M5) + Liu cross-check unverifiable (Perplexity M12) | MAJ | **VERIFIED ×2 (distinct issues)** | (i) **SNR-definition mismatch, proven by artifact**: `c1_fsky_sweep.json` reports per-realization σ_β = 0.0292° (fsky 0.85), 0.0327° (0.65) and a separate field `snr_template_canonical_def` = 32.98 / 28.81. Check: 20.32×√(0.85/0.32)=33.1 ✓, 20.32×√(0.65/0.32)=29.0 ✓ — the canonical "20.32" is a **template-fit SNR** (summary.json key `snr_namaster`), *not* β̂√N/σ_β̂ as fn:snr_definition (L1068–1082) claims. Under the stated definition with artifact σ_β(0.32)≈0.048° (=0.029×1.63), SNR_SE would be ≈111 and SNR_real ≈ 5.0, not 0.91. The fn misdescribes both 20.32 and 0.91. Claude's factor-9 anomaly is real and this is its resolution. (ii) Liu et al. "0.5σ in H0, 0.4σ in σ8" (L970–973) gives no Liu central values — unverifiable as printed (also Claude M8, OpenAI M11). | (i) Rewrite fn:snr_definition to label 20.32/25.71 as template-fit SNR; state canonical per-realization σ_β ≈ 0.048° and true per-map SNR; fix "0.91/1.15". (ii) Quote Liu H0/σ8 ± σ + arithmetic |
| G6 | `table_ii,companion` — Eq. (4) 3.9σ null unspecified (Claude N5) + Table III internal-QA language (Perplexity N4) | MIN | **PARTIAL / HOUSTON-DECISION** | Eq. 4 (L1245): adding "significance vs β=0" is a one-line fix — PARTIAL. Table III (app:claims) is a deliberate transparency artifact retained across rounds — HOUSTON-DECISION (same as Claude E6, see (b)). | One-line Eq.4 clause |
| G7 | `companion,audit_artifact` — internal IDs, "this volume", Forward paragraph as status note (Perplexity E6) | ESS | **PARTIAL** | hUBIFY IDs → submission-stage (G1). The Conclusions "Forward.—…chain has converged…" (L1402) **is** process-log prose in the body — legitimate; merge into normal results language. | Rewrite Forward para; IDs at bundle stage |
| G8 | `sigma_mixing,table_ii` — w0wa posterior without model comparison (Claude E7) | ESS | **STALE/OPINION** | The deferral is explicitly disclosed at L889–904, L1139–1157, App. A L1459, Table III row "Omitted". Same critique STALE ×6 across GPT rounds (preamble log v1B.0.31–0.34). Reviewer asks the paper to stop disclosing and instead not report posteriors; the disclosed-deferral is by design. | None (nested-sampling ln B remains the standing queued item) |
| G9 | "Stock CAMB" repeated ~15× (Claude N10) | MIN | **OPINION** | In-cell-caveats-win-on-visibility cascade rule (v1B.0.27). | None |

---

## (b) Single-vendor ESSENTIAL/MAJOR table

| Finding | Verdict | Evidence (file:line) | Fix class |
|---|---|---|---|
| **OpenAI E3** — Fig. 3 panel header "Planck SMICA" vs text "Commander" | **VERIFIED — ESSENTIAL** (and worse than reviewer saw) | Rendered `arxiv/figures/fig_namaster_beta_vs_nside.png`: title literally "…(NaMaster, Planck SMICA)". §IV text (L1031–1062) says Commander. **And** the canonical 500-MC script `reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py` L17: "Generate **synthetic ΛCDM** CMB Q/U maps" — the quoted 0.238/20.32/25.71 numbers come from synthetic-map MC (summary.json confirms), not from injections into the Commander map at all. Three-way provenance contradiction (text=Commander, figure=SMICA, artifact=synthetic ΛCDM + ACT-like dec-cut mask). | Regenerate Fig. 3 from 500-MC artifacts AND rewrite §IV map-provenance prose to match the executed pipeline (honesty-critical) |
| **Grok M4** — Fig. 3 Nside=512 point ≈0.15° vs quoted 0.238° | **VERIFIED — MAJOR** | Rendered figure: 512-point at ≈0.15°, 1024-point ("Lead result") ≈0.19°; nothing at 0.238. Figure is from a stale exploratory real-map run, inconsistent with every §IV number. | Same fix as OpenAI E3 (regenerate) |
| **Perplexity M14** — Fig. 3 caption "bias below 0.04°" contradicted | **VERIFIED — MAJOR** | Caption (tex L1006–1009) claims \|bias\|<0.04°; plotted 512-point implies bias ≈ −0.12° vs 0.27 injection. Also internal-junk annotations "Lead result"/"High-ℓ instability". | Same fix (regenerate) |
| Fig. 3 legend "Planck+ACT (Eskilt): 0.34±0.09°" | **VERIFIED — MAJOR** (caught via render; extends Gemini M1) | v1B.0.32 closure relabeled Eskilt to WMAP+Planck in all prose; the figure legend still says "Planck+ACT". | Same fix (regenerate) |
| **Gemini M1** — App. C likelihood stack: β_obs=0.342±0.094 labeled "joint Planck PR4 + ACT DR6" \cite{Eskilt2022,DiegoPalazuelos2025} | **VERIFIED — MAJOR** | tex L1537–1539. 0.342±0.094 is Eskilt WMAP+Planck (published PR3+WMAP9 headline per fn:eskilt_pr3_pr4); ACT DR6 is the *separate* 0.215±0.074 (so stated at L1181–1184). Also tex L1268–1270: "MCMC posterior, anchored to the Planck PR4 + ACT DR6 **EB-spectrum data**" directly contradicts the same paragraph's "Gaussian summary likelihood … not a re-analysis of the EB spectra" (L1277). Site-to-site inconsistency = VERIFIED per round context. | Relabel both sites to "published joint WMAP+Planck summary measurement [Eskilt2022]"; delete "EB-spectrum data" anchoring claim |
| **OpenAI E9** — Planck-only run "reported separately in Table I" but Table I has no Planck-only column | **VERIFIED — MAJOR** | fn L758–761 + Conclusions L1371–1374 both claim it; Table tab:verification (L795–819) has only Full-tension + Planck+BAO+SN columns. False cross-reference ×2. | Change to "not reported in Table \ref{tab:verification}" or add column |
| **OpenAI E12** — Conclusions cites "§VI body text" for the 0.040° bias; analysis is §IV | **VERIFIED — MINOR** | tex L1385 hardcoded "§VI"; pipeline section is sec:data_cmb = §IV. | s/§VI/§IV/ (use \ref) |
| **OpenAI E4 / Perplexity M9** — Ref [15] contains internal note "the value used at L256/L416 of P1B" | **VERIFIED — MAJOR** | references.bib L458 (`DiegoPalazuelos2022` note field). Renders into the PDF bibliography. | Trim note field to citable info |
| **Claude E3 / OpenAI M8, m6** — review-response/version prose in body | **VERIFIED — MAJOR (pattern-017)** | Five live sites: L881–884 ("An earlier count erroneously quoted '98.6% quintom-B'"), L898–900 ("note: prior caveat promised a Savage-Dickey ratio"), L927–934 ("This addresses earlier reviewer concerns"), L936–937 ("A concern was raised … claiming a Cobaya YAML alias failure"), L1396–1398 ("correcting the earlier C_aγθi product"). | Neutral-rephrase all 5 sites (keep scientific content) |
| **Claude E4 / OpenAI M4 / Perplexity M11, M3** — "corresponds exactly to the canonical 3.6σ" when computed 3.2σ | **VERIFIED — MAJOR (3-vendor)** | tex L946–949: 0.155/0.049 = 3.16σ; "exactly … 3.6σ" is false equivalence. | "is the same Hubble tension manifesting in the M_B axis (3.2σ in chain-σ units vs the canonical 3.6σ distance-ladder expression)" |
| **Claude M15 / Gemini m6 / Grok N2(part)** — Fig. 4 caption β=0.324° vs body 0.326° | **VERIFIED — MINOR** | Caption L1333 vs body L1314. Chain c5_continuous stats (verified by main session): 0.326±0.099 → caption stale. Grok N2's claim that caption uses "[1,30] run statistics" is wrong (0.324 is the [4,60] run, merely stale) → that part FALSIFIED. | Caption 0.324→0.326 |
| **Claude M16 / OpenAI m4** — Fig. 2 legend "Full tension (175 545 samples)" vs Table I 176,240 | **VERIFIED — MINOR** | Rendered fig_dneff_viability_two_frozen.pdf legend shows 175,545; Table L813 says 176,240; fn reconciliation never mentions 175,545. | Regenerate legend or footnote the count |
| Fig. 2 caption "four dataset combinations" but figure shows 2 | **VERIFIED — MINOR** (caught via render; adjacent to OpenAI E5) | tex L989–990 caption vs figure title "2 frozen datasets", 2 curves. | Fix caption |
| **OpenAI E5 / M9** — Fig. 2(a) overlays (WP4 reheating/decay, "BBN 2σ upper (0.41)", "ACT DR6 central (0.40)") uncited/unclear | **VERIFIED-LIKELY — MAJOR** | Overlays confirmed in render; no citation/definition in caption; "ACT DR6 central ΔNeff=0.40" is not a standard published value (ACT DR6 Neff=2.86±0.13 → ΔNeff≈−0.19). | Cite each overlay or strip them from the figure |
| **Claude M18 / Perplexity E4** — bias sign convention inconsistent (+0.032° canonical vs −0.033/−0.034° sweep) | **VERIFIED — MAJOR** | L1067/L1087–1090 (unsigned 0.032) vs L1107–1108 (signed −0.033/−0.034); both are β̂−β_inj<0. JSON: canonical bias_deg=+0.032 quoted unsigned; sweep bias_deg=−0.033. | Define bias=β̂−β_inj once; report −0.032° throughout |
| **Gemini M2** — "relative ~12% amplitude-dependent component" wrong/confusing | **PARTIAL** | L1090–1094. The bias *change* is 25% (0.032→0.040); "~12%" is the multiplicative under-recovery (0.238/0.27 = 0.88), correctly used at L1109. The sentence conflates the two. | Reword sentence |
| **Grok M1** — "statistically indistinguishable" without test | **PARTIAL** | −0.033 vs −0.032 with SE(mean)=0.029/√500≈0.0013 → claim true but arithmetic unstated. | Add SE arithmetic parenthetical |
| **Grok M2** — full R̂ table not published | **PARTIAL** | fn:rhat_csv gives worst row; full convergence CSVs exist (HF dataset + reproducibility/cosmology/convergence_latest.csv). Pointer absent from paper. | Add artifact pointer |
| **Grok M3** — β≈0.29 computed at C_aγ=8, "outside posterior support" | **FALSIFIED** | Continuous-prior posterior 16–84% = [7.3, 45.6] (chain-verified) **includes** 8. The [9,51] band assumes exact β=0.342; with 27% measurement σ, C_aγ=8 is comfortably inside support. | None |
| **Grok M5 / OpenAI E7, n1** — Eq. (3) missing rad→deg conversion | **PARTIAL — MINOR** | (α_EM/4π)×8×1.07 = 4.97×10⁻³ rad = 0.285° ≈ 0.29° — number correct, conversion implicit. Grok's "delete the equation" is overcall. | Add "×(180/π)" or a units sentence |
| **Grok E2/E3** — abstract headlines a null result / seven "NOT a…" disclaimers | **OPINION** | Title-declared scope; standing push-back (R26–R28, v1B.0.31 log). | None |
| **Grok E4** — abstract "3.6σ" contradicts pipeline-SNR disclaimer | **FALSIFIED** | The 3.6σ (L619) is the *published Eskilt* significance, explicitly attributed; the SNR disclaimer concerns the MC pipeline figures. No internal contradiction on direct read of L602–619. | None |
| **Claude M3 / OpenAI M1 / Perplexity E2** — 69%-in-band statement prior-dependent / under-specified | **PARTIAL** | Round context: it is a consistency statement; paper already says "posterior is broad, as expected for a single-amplitude constraint on a three-parameter degeneracy" (L1309–1311). Adding one prior-dependence sentence is cheap and fair. | One sentence |
| **Claude M13 / Gemini E2 / OpenAI M12 / Perplexity E8** — "spectator" banner vs sampled θi∈[0.5,2] (non-spectator regime) | **PARTIAL → one DO-NOW item** | Disclosure is extensive and repeated (abstract L620–630, fn:theta_backreaction L1205–1217, App. C fn L1514–1526). The *remaining* legitimate ask: report the spectator-restricted (θi≲0.1) posterior or the posterior fraction satisfying Ω_a≪1, so the "spectator-ALP consistency" headline has a number attached to its own regime. | Add spectator-subset readout from existing c5 chain (no new compute) |
| **Claude M14** — β_free σ=0.096 > input 0.094 implies "systematic floor" | **FALSIFIED** | Flat-prior+Gaussian-likelihood posterior σ should equal 0.094; the +2% excess is within MCMC sampling error of a σ estimate at N≈9,720 accepted (SE(σ)/σ ≈ 1/√(2N_eff) ≈ 2%). No floor is implied. | None |
| **Claude M6** — Λ_strong = M_Pl/√γ_BI not derived in Mercuri 2006 | **PARTIAL** | Citation-precision ask on a heuristic scale; cannot confirm an equation number from here. | Add pinpoint cite or soften to "cf." |
| **Claude M11** — DES-Y5 "~1500" SN count wrong (should be 1635) | **FALSIFIED** | references.bib L436: "~1500 new high-redshift Type Ia supernovae" is the **verbatim published DES title** (arXiv 2401.02929). Title text is not editable. | None |
| **Claude M2** — arXiv:2509.13654 unverifiable | **FALSIFIED** | Training-cutoff artifact; entry real; FALSIFIED 5 consecutive prior rounds (tex preamble log). | None |
| **Claude M1** — dataset footnote in abstract is a "red flag" | **OPINION** | The footnote *is* the deliberate v1B.0.34 disambiguation closure. Could move to §IV (Claude m1, batch) but its existence is by design. | Optional relocation |
| **Claude M4** — Fig. 4 "within 1σ" consistency tautological | **PARTIAL** | All three numbers are fits to the same β_obs; caption should say so. | Add "(all three constrained by the same β_obs)" |
| **Claude M7 / Perplexity M17/E3(part)** — footnote-1 reconciliation convoluted | **OPINION/HOUSTON** | Houston explicitly directed preserving the reconciliation (v1B.0.23 R25a closure, preamble log). The 175,545 figure-legend discrepancy *within* the cluster is VERIFIED (see above). | Keep fn; fix the 175,545 |
| **Claude M10** — remove §VI (heuristic-only ALP-ECH link) | **OPINION** | Scope; §VI repeatedly self-discloses non-distinctiveness. | None |
| **Claude M17 / Perplexity M15** — 3.9σ "upper bound" needs quantitative correlation | **PARTIAL** | Sign direction is correct (Claude concedes); a worked ρ-example would strengthen. | Optional 1-line ρ=0.3 example |
| **Perplexity M6** — SNR_real should be 9.1, not 0.91 | **PARTIAL** | Reviewer's arithmetic confuses σ_β̂ (SE of mean) with per-realization σ_β; 0.91=20.32/√500 follows the fn's own definition. **But** the artifact shows the printed 0.91 is wrong anyway (true per-realization SNR ≈ 5 at σ_β≈0.048°) — right smell, wrong derivation. Subsumed by G5(i). | Subsumed by G5 fix |
| **Perplexity M7** — which ALP results come from which chain | **PARTIAL** | 9,720 vs 8,955 bookkeeping is internally consistent (3×3,240=9,720 ✓; continuous run separate); attribution of each quoted number to its chain could be one explicit sentence. App. C already maps most. | One mapping sentence |
| **Perplexity M4** — [9,51] band derivation under-specified | **PARTIAL** | 10.3/1.1=9.4, 10.3/0.2=51.5 → "[~9, ~51]" with tildes is defensible rounding; showing the division explicitly is cheap. (Claude m18's *direction* point is the real error — see (c).) | Show division |
| **Perplexity M5** — "not a distinctive ECH prediction" unsupported | **OPINION** | The claim is a *negative* scope statement against self-interest; it weakens, not strengthens, the paper's claims. | None |
| **Perplexity M10** — results live only on GitHub/HF | **OPINION** | PRD permits repository-hosted supplementary material; fsky-sweep numbers also appear in the paper text. | None |
| **Perplexity M13** — σ8/S8 tension not quantified vs DES/KiDS | **PARTIAL** | Fair completeness ask; one sentence with DES-Y3 S8=0.776±0.017 vs chain 0.8245±0.0089 (≈2.5σ) suffices. | One sentence |
| **Perplexity E3** — sample-count accounting not uniquely reconstructible | **PARTIAL** | The fn arithmetic is self-consistent (verified v1B.0.25 against chains) *except* the 175,545 figure legend (VERIFIED above). "Both frozen" + "third ongoing" wording is awkward but accurate. | Fix 175,545; minor rewording |
| **Perplexity E5** — abstract "H0 consistent with ΛCDM" vs persistent 3.6σ tension | **FALSIFIED** | Both statements are simultaneously true and the mechanism is spelled out at L706–719 and L919–934 (posterior is Planck-dominated; tension persists vs SH0ES). No contradiction. | None |
| **META-E1 (Yp unstated) / META-E2 (Σmν unstated) / META-M3 (ΔNeff prior unstated)** | **VERIFIED-LIKELY — demoted to MINOR** | Real omissions, cheap fixes: full-tension YAML samples `nnu` flat [2.046, 5.046] (ΔNeff∈[−1,+2]) with no explicit mnu/YHe override → CAMB defaults (Σmν=0.06 eV one-massive, BBN-consistent Y_He). Constraints at σ(ΔNeff)≈0.17 are not "sensitively" conditioned on these defaults (META's ESSENTIAL severity is overcall), but PRD convention is to state them. | Add one config sentence to §V.A citing the YAML values |
| **META-M2 / OpenAI M5** — PR4 high-ℓ + 2018 low-ℓ/lensing mixing unjustified | **PARTIAL** | Legitimate-but-nonstandard combination; v1B.0.48 already unified the *naming*; a one-sentence justification is missing. | One sentence |
| **META-M4** — no negative-β / linearity injection test | **VERIFIED-LIKELY — actionable** | True: only β ∈ {0, +0.27, +0.342} tested (JSON+summary). A −0.27° injection run is ~30 min on-pod; closes the sign-symmetry hole for real. | Run −0.27° injection (eat-the-frog) or disclose |
| **META-M5 (purify_e=False) / META-M6 (Commander beam ≠ 5′@143GHz) / META-M8 (ℓ-range robustness) / META-m3 (noise model)** | **PARTIAL** | Legitimate methodology caveats — but note the audit finding above: the canonical run is on *synthetic ΛCDM maps*, so the Commander-beam critique (M6, also OpenAI M2) lands on prose that misdescribes the pipeline anyway. Fixing the §IV provenance rewrite (OpenAI E3 fix) largely moots M6; M5/M8 become one-sentence acknowledgments. | Fold into §IV rewrite |
| **META-M7** — Riess2020 Mb anchor vs Riess2022 cite | **STALE/PARTIAL** | `H0.riess2020Mb` is the Cobaya likelihood alias (addressed v1B.0.32 round log); paper quotes the Riess+2020 M_B value correctly at L916–918. Residual: §II calls it an "SH0ES H0 prior" when it enters as an M_B anchor — one-word clarification. | Clarify "M_B-anchor likelihood" |
| **OpenAI E13 / Perplexity E7** — β range 0.17–0.43° inconsistent with envelope | **STALE** | v1B.0.24 closure added the coupled-trajectory paragraph (L1234–1238) explicitly naming the naive [0.027, 0.44]° envelope and explaining the difference. Reviewers did not integrate it. | None |
| **OpenAI M3** — full-tension stack composition not enumerated in one place | **VERIFIED-LIKELY — MINOR** | True; merges into the G2b per-chain dataset table fix. | Same table |
| **OpenAI M6** — "Artifact:" path lines in main text | **OPINION/HOUSTON** | Deliberate reproducibility convention (\path artifacts), used across all 6 papers. | None |
| **OpenAI M7** — continuous-run prior log10(ma)∈[−35,−30] vs benchmark m/H0∈[1,3] unquantified | **VERIFIED-LIKELY — MINOR** | True: implied m/H0 spans ~[0.007, 670]; caption says "broadening" without numbers. | Add implied-range sentence |
| **OpenAI E10** — Fig. 1 axis "Neff" with τ-like ticks | **FALSIFIED** | Rendered corner plot: 6th axis labeled "τ" (0.04–0.07), 7th labeled "ΔN_eff" (−0.5…0.5). PDF text-layer flattening of Δ/subscripts (auto-FALSIFY rule). | None |
| **OpenAI E2** — Fig. 2(a) "SM (Neff = 0)" annotation false | **FALSIFIED** | Render shows "SM (ΔN_eff = 0)" — Δ present. Same text-layer artifact. | None |
| **OpenAI E8** — Fig. 2(b) garbled axis "(x xfull_tension)/full_tension" | **FALSIFIED** | Render shows "(x − x_full_tension) / σ_full_tension" — minus and σ present. Same artifact class. | None |
| **OpenAI E6** — canonical per-realization σ_β never stated | **VERIFIED** | Exactly the gap proven in G5(i). | Same fix |
| **Gemini E1** — placeholder citations [3],[11],[12] | **FALSIFIED** | Same as G3: real entries, training-cutoff artifact, 5-round FALSIFY streak. | None |
| **Gemini E2** — spectator framing | duplicate of Claude M13 group | see above | — |

---

## (c) Batched MINOR/NIT mechanical sweep (v1B.0.50 one-pass)

**VERIFIED minors — apply:**
1. Gemini m3: App. C scope statement still says "C_aγ∈[4,12] benchmark sweep" (L1548–1550) though headline is the [4,60] continuous run — update.
2. OpenAI m5: "References to 'k=7' elsewhere in this paper" (L814) — grep confirms **zero** other k=7 occurrences in body → delete the orphan sentence.
3. Claude m18: "(22% below, consistent with the **low**-Δφ/fa tail)" (L1313) — direction wrong: C_aγ<9 pairs with *high* Δφ/fa (or low-β draws), not low. Fix the parenthetical. (NB: the 22% itself is fine — see FALSIFIED m16.)
4. Claude m19: "Planck/ACT DR6 2.4–2.9σ" (L603, L667, L1028, L1388) — cited refs give 2.7σ (0.30/0.11) and 2.9σ (0.215/0.074); "2.4" untraceable → change to 2.7–2.9σ or cite the 2.4σ source.
5. Claude m13: (ω/H)₀ parenthetical duplicated verbatim (L700–705 ≈ L1129–1134) — deduplicate.
6. Claude m15 / Gemini m2: precision unification (0.169 vs 0.17; 67.68 vs 67.69) — sweep.
7. Claude N2: App. C footnote duplicates fn:theta_backreaction nearly verbatim (L1514–1526) — cross-reference instead.
8. Claude m6: "Eq.(1)-adjacent disclaimer" in fn:theta_backreaction points at eq:beta_namaster (§IV) but means the abstract restriction — fix the pointer.
9. Gemini m7: report the null-check number (β=0 → recovered 0.000, SNR 0.0 per summary.json) — one number, artifact in hand.
10. Gemini m5: Fig. 3 error-bar definition — folds into the Fig. 3 regeneration.
11. OpenAI n6: Data-availability list includes galaxy-spin code (L1446–1450) unrelated to P1B analyses — trim or label as program-wide repo.
12. Gemini m1 / Claude m8: "third Planck-only combination ongoing" in abstract (L589) + "still accumulating" (L1372) — either drop from abstract or keep both with identical wording; pick one.

**PARTIAL/OPINION nits — optional polish, no-action default:**
Claude m1–m5, m7, m9–m12, m14, N1, N3, N4, N6–N9; Gemini m4 ("disfavors" already carries fn:wcaveat qualifier at L873 — mostly STALE), N1; Grok N3 (FALSIFIED: "Esikilt" misspelling — grep returns 0 hits in tex; PDF artifact; \cite{Eskilt2022} resolves, bib entry exists); OpenAI n2, n3 (FALSIFIED: fn formula in tex is clean "β̂/SE(β̂)" — extraction garble), n5, n7; Perplexity N1–N3, N5–N13; META-m1, m2, N1 (typeset e^{2iβ} — tex L1054 already reads `e^{2i\beta}(Q+iU)` correctly → FALSIFIED).

---

## (d) FALSIFIED list (with evidence)

| Finding | Why false |
|---|---|
| Grok E1 + Perplexity M8 + Gemini E1 (future dates / placeholder arXiv IDs) | It IS 2026-06-09; arXiv 2509/2507 = Sept/Jul **2025**, past. Entries real in references.bib (L447+, L574+). 6th consecutive round this is falsified. |
| META-E3 (Age ±0.019 Gyr implausible) | Planck 2018 publishes 13.797±0.023 Gyr with comparable σ(H0); reviewer ignored parameter correlations. |
| Grok M3 (C_aγ=8 outside posterior support) | Chain 16–84% = [7.3, 45.6] includes 8. |
| Claude M14 (β_free σ 0.096 vs 0.094 ⇒ systematic floor) | +2% is within MC sampling error of a σ estimate at N≈9.7k. |
| Claude M11 (DES-Y5 "~1500" count) | "~1500" is the verbatim published DES-SN5YR title (bib L436). |
| Claude M2 (arXiv:2509.13654 unverifiable) | Real entry; training-cutoff artifact; multi-round streak. |
| Claude m16 (22% below 9 incompatible with 16th pct = 7.3) | Backwards: 16% lies below 7.3 < 9, so mass below 9 must *exceed* 16%; 22% is arithmetically consistent (and 69+22+9=100 ✓ with 84th pct 45.6 < 51). |
| Claude m20 (H200 not used for Cobaya) | namaster_500mc.py header: "as it ran on H200 pod pod1_namaster_umap_2026-04-29 … CPU-bound" — workloads genuinely ran on self-funded RunPod H200 instances. |
| Grok E4 (abstract self-contradiction 3.6σ) | 3.6σ is the attributed published Eskilt value; pipeline-SNR disclaimer refers to different figures. |
| OpenAI E10, E2, E8 (figure label errors: "Neff"=τ axis, "SM (Neff=0)", garbled axis) | Rendered figures show correct "τ", "ΔN_eff", "SM (ΔN_eff = 0)", "(x − x̄)/σ" labels. PDF text-layer flattening (auto-FALSIFY class). |
| OpenAI n3 (fn:snr_definition typo "β/ˆ SE") | tex L1071 is clean; extraction artifact. |
| Grok N3 ("Esikilt" misspelling + missing ref) | 0 occurrences of "Esikilt" in tex; Eskilt2022 bib entry present. |
| META-N1 (e2iβ typeset as product) | tex L1054: `e^{2i\beta}(Q + iU)` — correct in source/PDF. |
| Perplexity E5 (H0-consistent vs tension contradiction) | Both true; mechanism spelled out L706–719, L919–934. |
| Grok N2 (Fig. 4 caption quotes [1,30]-run stats) | Caption quotes the [4,60] continuous run (0.324 vs chain 0.326 — staleness, not wrong-chain). |

---

## (e) Disposition — v1B.0.50 closure wave

**ROUND IS NOT CLEAN** — VERIFIED MAJOR+ findings exist. Closure wave (ordered, hardest first):

**Wave A — load-bearing (ESSENTIAL/MAJOR, all VERIFIED):**
1. **§IV NaMaster provenance rewrite + Fig. 3 regeneration** (OpenAI E3, Grok M4, Perplexity M14, legend mislabel): describe the executed *synthetic-ΛCDM-map* MC pipeline honestly; regenerate Fig. 3 from `p1_namaster_500mc` + `c1_fsky_sweep.json` artifacts; kill SMICA/Commander/"Lead result" junk.
2. **SNR-definition repair** (G5(i), OpenAI E6, Perplexity M6 smell): relabel 20.32/25.71 as template-fit SNR; state σ_β(0.32)≈0.048°/realization; correct "SNR_real ≈ 0.91/1.15".
3. **§V.A BAO dataset correction** (OpenAI E1 upgraded): SDSS DR16+6dF+MGS for frozen chains, per `.input.yaml`; add consolidated per-chain dataset table (also closes OpenAI M3, part of META-M2).
4. **w_pivot footnote** (Claude E9/Gemini M4/OpenAI E11): correct decorrelation identity + chain Cov readout.
5. **ALP likelihood-stack attribution** (Gemini M1 + L1269 "EB-spectrum data"): WMAP+Planck summary-likelihood labels at both residual sites.
6. **Planck-only Table-I false cross-ref ×2** (OpenAI E9); **§VI→§IV** (OpenAI E12); **ref [15] internal note** (OpenAI E4/Per M9); **"exactly 3.6σ"** (Claude E4 group); **review-response prose ×5 sites** (Claude E3 group); **bias sign convention** (Claude M18/Per E4); **Liu et al. numbers** (G5(ii)); **Fig. 2 overlay citations + "four combinations" caption + 175,545 legend** (OpenAI E5/M9, Claude M16).
7. **Spectator-subset readout** (Claude M13 group DO-NOW): θi≲0.1 posterior fraction from existing c5 chain. **META-M4**: −0.27° injection run (~30 min pod) or explicit disclosure.

**Wave B — mechanical sweep:** the 12 VERIFIED minors in (c) + Fig. 4 caption 0.324→0.326 + Yp/Σmν/ΔNeff-prior config sentence (META-E1/E2/M3) + one-sentence PARTIAL closures (G2d, G2f, M2-Gem wording, Grok M1/M5 arithmetic/units, S8 comparison, 69% prior-dependence, App. C chain-attribution sentence).

**No-action:** all OPINION (scope/length/format — standing push-back), STALE (model-comparison deferral, 0.17–0.43 envelope, riess2020Mb alias), FALSIFIED (14, table (d)), HOUSTON-DECISION (companion-bundling logistics, Table III claims-classification retention, abstract-footnote placement).

**Readiness implication:** per `feedback_readiness_oscillation`, P1B must roll backward this round (VERIFIED ESSENTIAL-class provenance findings); next cross-vendor round fires on v1B.0.50 after Wave A+B closure.
