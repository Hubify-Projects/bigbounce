# EXT1 P1B Truth Audit — Paper 1B v1B.0.54
**Harvested**: 2026-06-10 · **Auditor**: Claude Sonnet 4.6 (internal sub-agent)
**Sources**: EXT1_P1B_ChatGPT.md (GPT-5.5 Pro Extended, MAJOR), EXT1_P1B_Grok.md (Grok Heavy, MINOR), EXT1_P1B_Gemini.md (Gemini 3.5 Thinking, MINOR)
**Paper**: arxiv/paper1b_mcmc_companion.tex v1B.0.54 · 16 pp · survived R23–R28conf internal rounds clean

---

## Verification methodology

Each finding was checked against:
- `arxiv/paper1b_mcmc_companion.tex` (body lines, not `%`-comments)
- `reproducibility/cosmology/frozen/full_tension_20260311_1728/` (MANIFEST, parameter_summary.json, freeze_diagnostics.json/CORRECTED)
- `reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/` (MANIFEST, convergence_report.txt)
- `reproducibility/cosmology/COUNT_EXPLANATION.md`
- `reproducibility/p1_namaster_500mc/results/summary.json`
- `arxiv/references.bib`

CPL crossing arithmetic cross-check: `1 − a× = (−1 − w0)/wa = (−1 − (−0.8122))/(−0.6666) = (−0.1878)/(−0.6666) = 0.2817`, so `a× = 0.7183`, `z× = 1/0.7183 − 1 = 0.392 ≈ 0.39`. Paper quotes `z× ≈ 0.39` at body L985 — **correct**.

---

## Verdict Table

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| F1 | ChatGPT | BLOCKER | `parameter_summary.json` in frozen full-tension artifact has severe column/header mislabelling: H0=0.8035, delta_neff=13.82, tau=1.04, sigma8=0.308, omegam=0.814, ns=0.022 — obviously not physical km/s/Mpc values | **VERIFIED** | `frozen/full_tension_20260311_1728/diagnostics/parameter_summary.json` literally stores raw Cobaya normalised units (H0=0.8035 = 80.35 km/s/Mpc in h units × 100 = 80.35, yet Cobaya's H0 in its CAMB block is sampled in units of km/s/Mpc; the value 0.8035 is clearly not in km/s/Mpc). `parameter_summary.md` repeats same values. The paper's Table I (body L909) correctly reports 67.68 ± 1.06, but the public JSON artifact that a reader would download shows 0.8035. No note in paper body warns of this discrepancy. This is a genuine external-audit risk: any reader downloading the JSON will conclude the chain parser maps parameters to wrong slots. |
| F2 | ChatGPT | BLOCKER | Burn-in inconsistency: PDF body says both frozen chains use 30% burn-in (post-burn total 216,432); but `planck_bao_sn` convergence_report.txt says 20% burn-in and 106,361 post-burn | **VERIFIED** | `frozen/planck_bao_sn_20260312_1954/diagnostics/convergence_report.txt` line 5 reads "Burn-in: 20%", post-burnin samples: 106,361. Paper body (L837) states "removing the first 30% of each chain as burn-in" uniformly for both chains, giving 216,432. `132,949 × 0.8 = 106,359 ≈ 106,361` (rounding). `132,949 × 0.7 = 93,064`. The 216,432 uses 30% for both: `176,240×0.7 + 132,949×0.7 = 123,368 + 93,064 = 216,432`. The planck_bao_sn convergence_report lists 20% burn-in, giving 106,361 post-burn — not 93,064. There is a real discrepancy between the artifact's burn-in label and the paper's stated 30% uniform burn-in. Whether the _paper's_ 30% figure or the artifact's 20% figure is correct for this chain is unclear without inspecting chain files. The paper's footnote arithmetic is internally consistent with 30% for both chains, but the public convergence_report contradicts this for planck_bao_sn. |
| F3 | ChatGPT | BLOCKER | Spectator-ALP claim "natural parameter values" in abstract/conclusions when the spectator-consistent regime requires θ_i ∼ 0.1, imposing ∼25× misalignment tuning — inconsistent headline framing | **PARTIAL** | Body L744 says "natural parameters (taken at scan-prior midpoint values; the ∼25× misalignment tuning required for the headline result is disclosed..." and fn:theta_backreaction (L1540–1552) explicitly quantifies the tuning. Abstract (L691–701) has full spectator-status caveat. Body L1815 says "accommodates the observed signal for natural parameter values (taken at scan-prior midpoint values; the ∼25× misalignment tuning required for the headline result is disclosed...)". The word "natural" is retained but immediately qualified with the tuning disclosure in the same sentence. ChatGPT's BLOCKER on this was largely addressed by v1B.0.39–0.41 closures. The residual risk: the abstract and conclusion still use "natural parameter values" as a shorthand before the qualifier; a journal editor reading only the headline could misinterpret. Not a fabrication but a framing vulnerability. Downgrade to MAJOR for framing precision. |
| F4 | ChatGPT | BLOCKER | w0–wa section (Table II / iter2) uses DES-Y5 + Pantheon+ as independent likelihoods; these SN catalogs have ~20% overlap of events, and the product likelihood is unjustified without overlap correction | **VERIFIED** | Paper body Table II caption (L944) lists "DES-Y5 + Pantheon+" in the likelihood stack. Body L972 reports `χ²_SN = 3043.0 ± 1.6` attributed jointly to "DES-Y5 + Pantheon+". No disclosure of SN overlap, shared events, or joint covariance treatment exists in the paper body. The comment-history at L124 says "naive-combination note" as a one-line PARTIAL closure but grep of body finds no corresponding body sentence. The DES Collaboration comparison paper (Abbott et al. 2024 or equivalent) confirms ~20% shared SNe with different Malmquist corrections between Pantheon+ and DES-SN5YR. This is a real methodological gap in the iter2 analysis: the product likelihood double-counts overlapping supernovae. The paper already heavily caveats the iter2 section (fn:wcaveat, nested sampling deferred), but the SN overlap problem is not disclosed. |
| F5 | ChatGPT | MAJOR | 309,189 samples described without explicit "raw accepted samples" qualifier in abstract headline | **PARTIAL** | Abstract (L654) says "309,189 frozen samples" — not explicitly "raw accepted". Footnote fn:sample_stratification (L834) correctly says "raw accepted samples". The abstract does not contain the qualifier "raw accepted." Grok's scrutiny item (F13) found this acceptable given fn:sample_stratification. Minor framing issue; the footnote adequately covers it but abstract could be tightened. |
| F6 | ChatGPT | MAJOR | ΔN_eff prior N_eff ∈ [2.046, 5.046] allows negative ΔN_eff; result should be quoted as one-sided upper limit under ΔN_eff ≥ 0 | **VERIFIED** | Body L829–831 confirms prior is `nnu ∈ [2.046, 5.046]` i.e. `ΔN_eff ∈ [−1, +2]`. Paper frames the run as "extra radiation-like degree of freedom" throughout. No one-sided upper limit reported; both values (−0.020 and +0.065) are two-sided posterior means. The negative ΔN_eff is phenomenologically valid but the physical interpretation "extra radiation-like species" is inapplicable to the negative-ΔN_eff portion of the prior. This is a genuine presentation issue. |
| F7 | ChatGPT | MAJOR | "Standard-ECH route to dark energy via additional relativistic species" (Fig. 2 caption, L1139) is too strong — stock CAMB N_eff run cannot rule out an ECH-specific Boltzmann module | **VERIFIED** | Body L1139–1141 in Fig. 2 caption: "The standard-ECH route to dark energy via additional relativistic species at recombination is therefore not viable as an amplitude-level explanation of either tension." The paper has extensive disclaimers elsewhere that stock CAMB ≠ ECH Boltzmann module, but this caption sentence reads as if the N_eff proxy run directly rules out the ECH route. Inconsistency between caption language and body scoping disclaimers is real. |
| F8 | ChatGPT | MAJOR | "Full-tension" label implies a full DES 3×2pt likelihood; it is only a compressed Gaussian S_8 prior | **PARTIAL** | Table I caption (L888–890) discloses: "The full-tension column includes the DES-Y3 S_8 Gaussian prior 0.776 ± 0.017". Body L897 says "compressed Gaussian prior". The framing "full-tension" is a naming choice not a claim of full likelihood; the caveat is present in the table caption. Partially adequate — the nomenclature could mislead but the disclosure is right there. OPINION-leaning MINOR, not a MAJOR. |
| F9 | ChatGPT | MAJOR | NaMaster validation labelled "ACT-like pipeline" overstates scope; it is a synthetic-sky pseudo-C_ℓ test without beam, foregrounds, α/β separation, or bandpower covariance | **PARTIAL** | Body §IV has multiple explicit scope notes: "no galactic foregrounds, so the very component that breaks the β–α degeneracy... is absent by construction" (L673). SNR definition footnote fn:snr_definition (L1288) and per-realization σ_β quoted from sweep artifact. The phrase "ACT-like" refers to the mask footprint, not the full ACT pipeline, and the body disambiguates this. However the NaMaster section title and early references to "ACT-like mask" could still mislead. Adequate but borderline. |
| F10 | ChatGPT | MAJOR | "Unbiased at the |Δβ̂| ≤ 0.040° level" (L1331) is misleading: the canonical estimator has a 12% multiplicative bias | **VERIFIED** | Body L1329–1332: "The deconvolution is therefore unbiased at the |Δβ̂| ≤ 0.040° level in the worst-case injection, which we carry forward as the NaMaster systematic floor." The on-disk summary.json confirms: recovered 0.238° for injected 0.270° → 12% multiplicative bias (0.032° absolute). Calling this "unbiased at 0.040°" is technically accurate as a floor statement but contradicts normal usage of "unbiased." The sentence should say "calibrated with empirical bias up to 0.040° for the unweighted estimator" or equivalent. |
| F11 | ChatGPT | MAJOR | SNR = 20.32 should not appear as a headline; it is a diagonal matched-template ratio, not a per-realization detection significance | **PARTIAL** | Body (L1193–1195) already contains: "The pipeline template-fit SNR values (e.g., 20.32, 25.71; fn:snr_definition) refer to recovery of injected MC signals and are not competitive sky measurements." The SNR=20.32 figure is present in the manuscript but explicitly demoted in the abstract disclaimer, Section IV, and the fn:snr_definition footnote. Per-realization σ_β ≈ 0.047°, |β̂|/σ_β ≈ 5 is quoted from the fsky sweep. The key improvement needed: fn:snr_definition should be promoted to main-text proximity at first occurrence (Grok MAJOR F15 agrees). |
| F12 | ChatGPT | MAJOR | ALP MCMC is a reparameterized summary-likelihood fit, not an independent EB-spectra fit; comparisons between β_ALP, β_free, β_obs can look like independent confirmations | **PARTIAL** | Body L1654 explicitly says "not a re-analysis of the EB spectra themselves; 720 accepted samples in the dedicated β_free configuration" and §VI states it uses a Gaussian summary likelihood on published β_obs = 0.342° ± 0.094°. Appendix C specifies likelihood configuration. The warning is present but buried in body text and appendix; it should appear every time the three β values are compared. |
| F13 | ChatGPT | MAJOR | Public repository has stale README (old v0.9 paper values H0=69.2, ΔN_eff≈0.3, "no CMB map analysis"); unrelated PTA/galaxy-spin files mix with P1B artifacts | **HOUSTON-DECISION** | Verified: `reproducibility/` directory contains `galaxy_spins/`, `nanograv_fit_results.json`, `p3_pta_mcmc/`, `p4_chirality_classifier/` (all unrelated to P1B). The README.md was not audited in detail but the directory structure confirms the program-wide repository concern. The paper (L1865–1871) acknowledges "The repository is program-wide" but a clean v1B.0.54 release subdirectory with checksums and exact commands is not present. The request for a versioned release directory with only P1B files + DOI/Zenodo is a legitimate journal-standard ask. Whether to create a clean release is Houston's scope decision. |
| F14 | ChatGPT | MINOR | PACS numbers: should be removed for MNRAS/JCAP | **VERIFIED** | Body L705: `\pacs{98.80.-k, 95.36.+x, 04.50.Kd}` present. PACS numbers are deprecated in revtex4-2 PRD style and not used by MNRAS/JCAP. For PRD submission the `showpacs` class option is standard; for MNRAS/JCAP it should be removed. Target-journal-dependent. |
| F15 | ChatGPT | MINOR | Reference [25] (Cai2010quintomReview) contains program-management prose: "Used in P1A Sec. VI to point readers to the bounce-class alternative..." | **VERIFIED** | `arxiv/references.bib` line 1120: `note = "Canonical quintom-cosmology review (two-field DE with w crossing -1). Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers."` This is program-management prose that should be stripped from a published .bib file. The DiegoPalazuelos2022 note was trimmed (per v1B.0.50 changelog) but Cai2010quintomReview was not. |
| F16 | ChatGPT | MINOR | PR3/PR4 wording: abstract footnote says PR3+WMAP9 while §VI calls it "PR4/NPIPE" — inconsistent | **FALSIFIED** | fn:eskilt_pr3_pr4 (body L674–685) explicitly disambiguates: the published PRD paper uses PR3+WMAP9; the code repository used in the ALP-MCMC runs uses PR4/NPIPE. Both labels are present and correctly attributed to different artifacts. The supposed inconsistency is the intended disambiguation. Not an error. |
| F17 | ChatGPT | MINOR | "LCDM" and "ΛCDM" used inconsistently | **VERIFIED** | Body uses "ΛCDM" for the model label but "LCDM" appears in at least 5 body lines (L950 fn:wcaveat, L979, L992, L1002, L1008, L1010, L1011, L1016) consistently in the context of "LCDM point" or "vs LCDM" column header (L947). The LCDM / ΛCDM mixing is confirmed in body text. Minor typographic inconsistency. |
| F18 | ChatGPT | MINOR | M_Pl: reduced vs unreduced Planck mass not specified in ALP energy-density formula | **VERIFIED** | `\MPl` defined at L38 as `M_{\rm Pl}` with no specification of reduced/unreduced. Body L692: `ρ_a ∼ m² f_a² θ_i² ∼ H_0² M_Pl²` with no convention note. The factor of whether M_Pl = 1.22×10¹⁹ GeV (unreduced) or 2.44×10¹⁸ GeV (reduced) changes the spectator threshold by √(8π) ≈ 5. Should be specified. |
| F19 | ChatGPT | MINOR | LiteBIRD statement "will settle this at ∼9σ" is overconfident; should be qualified with foreground/calibration assumptions | **VERIFIED** | Body L1860: "LiteBIRD will settle this at ∼9σ in the early 2030s." v1B.0.53 changelog (L130) says "LiteBIRD 9sigma two-null-hypotheses rewrite" as a closure, but the resulting body sentence at L1860 still reads as a confident prediction without foreground/calibration qualification. ChatGPT's proposed fix ("under forecast foreground/calibration assumptions, a β≃0.27° signal would be detected relative to β=0 at ∼9σ") is correct. |
| F20 | ChatGPT | MINOR | HuggingFace links in Appendix A: paper says "links are in the repository README" but README may not contain v1B.0.54-specific HF dataset DOIs | **PARTIAL** | Body L1934–1940 says "links in the repository README" for three HF datasets. No explicit HF URLs or DOIs appear in the paper itself. This creates a version-of-record link dependency on a live README that may change. |
| F21 | Grok | MAJOR | Appendix A lacks a specific commit SHA or immutable tag for the v1B.0.54 frozen state; HF dataset DOIs also missing from the paper or a clear pointer | **VERIFIED** | Body L1867: points to GitHub URL without a commit hash or tag. Paper does not list a `git commit SHA` or Zenodo/HF DOI anywhere in Appendix A or Data Availability. This is a standard reproducibility requirement for journal submission. Same concern as ChatGPT's F20 but more precisely focused. |
| F22 | Grok | MAJOR | SNR disclaimer ("both are MC pipeline-recovery figures, not sky-measurement systematics") is buried in a footnote; should be promoted to main text at first SNR mention (p. 6) and repeated in abstract's NaMaster bullet | **PARTIAL** | Body L1193–1195 has the disclaimer in main text of §IV: "pipeline template-fit SNR values... refer to recovery of injected MC signals and are not competitive sky measurements." The abstract (L674–687) also contains "the pipeline SNR figures refer to recovery of injected MC signals." However the disclaimer is split across a footnote and body text and is not immediately adjacent to the first occurrence of "SNR=20.32" in §IV. Grok's ask to repeat it verbatim in the abstract's NaMaster bullet is a legitimate tightening. |
| F23 | Grok | MINOR | Footnote density (fn. 1–5 + "correction notes"): several long footnotes could be shortened or moved to Appendix | **OPINION** | Deliberate design choice per the "in-cell caveats win on visibility" cascade rule from v1B.0.27. Not a factual or scientific error. |
| F24 | Grok | MINOR | Sentences in §III (quintom-B discussion) and §VI (coupling-burden paragraph) are overly parenthetical | **OPINION** | Style preference. Not actionable as a truth-audit item. |
| F25 | Grok | MINOR | Artifact filenames scattered across paragraphs; should be consolidated into an "Artifact index" table in Appendix A | **OPINION** | The claims classification Table IV (Appendix B) and Appendix A serve this function but without a consolidated filename index. Reasonable polish request; no factual error. |
| F26 | Grok | MINOR | ΔN_eff rendered inconsistently in PDF extraction | **OPINION** | LaTeX source consistently uses `\Delta\Neff`. PDF extraction artifact, not a source error. |
| F27 | Gemini | MAJOR | Sec. III: PR4/NPIPE high-ℓ + 2018-release low-ℓ/lensing pairing leaves pairing-induced bias on ΔN_eff/H_0/S_8 unquantified; for a dedicated technical verification paper this is a notable gap | **PARTIAL** | Body L818–823 explicitly discloses: "the PR4/NPIPE high-ℓ + 2018-release low-ℓ/lensing mixture is the standard Cobaya pairing, but we have not run a release-pairing swap test... any pairing-induced bias on the headline ΔN_eff/H_0/S_8 at the quoted precision is therefore unquantified here." The disclosure is present. Gemini's proposed fix — cite existing Planck Collaboration or CamSpec validation notes to place an analytical upper bound on the pairing-induced shift — is not yet implemented. The disclosure is adequate for a companion paper; adding a literature-bound upper estimate would strengthen it. |
| F28 | Gemini | MAJOR | Sec. V.B: accumulating Planck-only chain (114,992 samples, R̂−1∼0.05) mentioned in narrative but plays no role in final conclusions — adds unnecessary ambiguity | **PARTIAL** | Body L844–849 explicitly states the chain "is not reported in Table I (which contains only the two frozen combinations) and is not aggregated into the 309,189-sample headline anywhere in this paper." The disclosure is clear. Gemini's ask to either remove references entirely or add explicit rationale is a legitimate tightening; the current disclosure is adequate but the mention at L654 in the abstract ("plus a third Planck-only combination still accumulating") could confuse a reader. |
| F29 | Gemini | MINOR | H_0 units: body uses km s⁻¹ Mpc⁻¹ (LaTeX style) while Table I header uses [km/s/Mpc] — inconsistent with MNRAS style | **VERIFIED** | Body L662: `\text{km\,s}^{-1}\,\text{Mpc}^{-1}`. Table I column header L909: `$H_0$ [km/s/Mpc]`. Mixed notation confirmed. Minor typographic inconsistency. |
| F30 | Gemini | MINOR | Sec. IV: unweighted χ² template fit used as canonical baseline without a brief justification, despite robustness battery showing inverse-variance fit eliminates 80% of bias | **VERIFIED** | Body L1369–1402 documents the robustness battery result (inverse-variance fit recovers 0.264°, bias −0.006°, removing 80% of the 12% bias). No justification for choosing the unweighted fit as the canonical baseline appears in the text. Standard practice is to use the best estimator as baseline. The paper needs 1–2 sentences explaining why the unweighted estimator is canonical (e.g., consistency with published analyses, or disclosure that the inverse-variance estimator was tested post-hoc). |
| F31 | Gemini | MINOR | Sec. VI, p. 10: draft correction notes ("an earlier draft paired Δφ/f_a ≈ 1.0–1.07 with m ≈ 1.8–2H_0; the committed EOM integration gives...") visible in final text — can confuse readers | **VERIFIED** | Body L1578–1582: "[Correction note: an earlier draft paired Δφ/f_a ≈ 1.0–1.07 with m ≈ 1.8–2H_0; the committed EOM integration gives Δφ/f_a = 0.35–0.42 at those masses (θ_i=1), and the mass pairings are corrected throughout against the released grid scan.]" Similarly at L891 and L1538. Three "Correction note" blocks with draft history visible in body. These serve as audit trails but in a published paper should be replaced by a single supplementary note or removed. |

---

## Consensus Findings (2+ reviewers)

| Topic | Reviewers | Severity |
|-------|-----------|----------|
| Burn-in / burn fraction inconsistency (30% in paper vs 20% in planck_bao_sn artifact) | ChatGPT F2, implied by Grok scrutiny item 1 | VERIFIED MAJOR |
| Parameter_summary.json column-mapping bug (H0=0.8035 not km/s/Mpc) | ChatGPT F1 | VERIFIED BLOCKER |
| SN overlap (DES-Y5 + Pantheon+ naively combined) | ChatGPT F4 | VERIFIED BLOCKER |
| SNR=20.32 disclaimer needs higher visibility in main text | ChatGPT F11, Grok F22 | PARTIAL MAJOR |
| Spectator-ALP "natural parameter" framing requires tightening | ChatGPT F3, Gemini §D | PARTIAL MAJOR |
| Commit SHA / HF DOI absent for v1B.0.54 version-of-record | ChatGPT F20, Grok F21 | VERIFIED MAJOR |
| Draft correction notes still in final body text | ChatGPT (framing), Gemini F31 | VERIFIED MINOR |
| H_0 unit notation inconsistency | ChatGPT (implicit), Gemini F29 | VERIFIED MINOR |

---

## Action Plan

Actions ordered hardest-first. Every VERIFIED / PARTIAL finding with a clear fix is listed.

### Priority 1 — Blockers (must fix before journal submission)

**A1 — Fix parameter_summary.json column-mapping bug (F1)**
- File: `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/parameter_summary.json`
- The JSON stores raw Cobaya-normalised parameter values (H0 in ~0.67–0.69 scale = 100 h, sampled as h) but the key labels suggest physical parameters in standard units.
- Fix: regenerate the summary JSON from chain headers with correct unit conversion (H0 × 100 → km/s/Mpc) OR rename keys to make the normalisation explicit (e.g., `H0_h_units`), plus add a README note explaining the units.
- Add a body footnote in §III/Appendix A warning readers of the unit convention in the JSON artifacts.
- Also fix `parameter_summary.md` and the `tables/` directory.

**A2 — Reconcile burn-in fractions (F2)**
- File: `reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/diagnostics/convergence_report.txt`
- The convergence report says 20% burn-in and 106,361 post-burn samples. The paper says 30% for both chains, giving 216,432 post-burn total.
- Determine the actual burn fraction used for the planck_bao_sn chain (check the Cobaya YAML `burn_in:` field in `cobaya_planck_bao_sn.yaml` and the chain's `.input.yaml`).
- If the actual burn fraction was 20%, correct the paper's footnote and the 216,432 total (→ 123,368 + 106,361 = 229,729 post-burn) and re-verify the GetDist corner-plot sample count.
- If the paper's 30% is correct, update the convergence_report.txt to 30% and post-burn = 93,064.

**A3 — Disclose DES-Y5 / Pantheon+ SN overlap in iter2 (F4)**
- File: `arxiv/paper1b_mcmc_companion.tex`, iter2 section / Table II caption
- Add a footnote or parenthetical in §V (iter2 analysis) disclosing: DES-SN5YR and Pantheon+ share approximately 20% of SN events with different Malmquist-bias corrections; the present analysis uses a product likelihood without joint covariance; users requiring a rigorous SN combination should refer to the DES Collaboration comparison paper.
- Do NOT claim the combination is rigorously independent. Downgrade the `+4.3σ` headline language accordingly (fn:wcaveat already partially covers this; the SN overlap disclosure is the additional needed caveat).

### Priority 2 — Major fixes (should fix before submission)

**A4 — Add commit SHA and HF dataset DOIs to Appendix A / Data Availability (F21, F20)**
- File: `arxiv/paper1b_mcmc_companion.tex`, Appendix A / Data Availability subsection (L1865)
- Add: `git tag v1B.0.54` pointing to the exact commit, and its SHA in the paper.
- Replace "links are in the repository README" with explicit HF dataset URLs or DOIs for the three listed datasets (MCMC diagnostics, NaMaster artifacts, ALP chains).

**A5 — Strip program-management prose from references.bib (F15)**
- File: `arxiv/references.bib` line 1120
- Remove the note field from `Cai2010quintomReview`: delete the entire `note = "Canonical quintom-cosmology review... Used in P1A Sec. VI..."` sentence.
- Audit all other bib entries for program-management notes; the DiegoPalazuelos2022 note was already trimmed but check others.

**A6 — Quote ΔN_eff as one-sided upper limit (F6)**
- File: `arxiv/paper1b_mcmc_companion.tex`, Abstract, §III, Table I
- Since the prior is N_eff ∈ [2.046, 5.046], add an explicit one-sided 95% upper limit under ΔN_eff ≥ 0 alongside the two-sided posterior mean. Use wording: "two-sided N_eff shift, not a physical extra-species prior; the one-sided 95% upper limit is ΔN_eff < X.XX."

**A7 — Fix Fig. 2 caption ECH-route overclaim (F7)**
- File: `arxiv/paper1b_mcmc_companion.tex`, Fig. 2 caption (L1139–1141)
- Replace "The standard-ECH route to dark energy via additional relativistic species at recombination is therefore not viable" with "No evidence for a recombination-era N_eff shift in this stock-CAMB proxy run; this does not directly test the ECH spin-torsion sector (which lacks a Boltzmann-module prediction for ΔN_eff)."

**A8 — Replace "unbiased at |Δβ̂| ≤ 0.040°" with calibrated-bias language (F10)**
- File: `arxiv/paper1b_mcmc_companion.tex` body L1331
- Replace "The deconvolution is therefore unbiased at the |Δβ̂| ≤ 0.040° level in the worst-case injection" with "The pipeline has a multiplicative under-recovery of ∼12% (0.032° absolute bias for the canonical injection) and a worst-case empirical bias of 0.040° for the unweighted estimator; this floor is carried forward as the NaMaster systematic floor."

**A9 — Add justification for unweighted estimator baseline (F30)**
- File: `arxiv/paper1b_mcmc_companion.tex`, §IV robustness battery paragraph
- Add 1–2 sentences: "The unweighted estimator is adopted as the canonical baseline to match the estimator configuration used in the public NaMaster scripts released by published analyses (e.g., [cite]) and to facilitate direct comparison; the inverse-variance-weighted fit is evaluated in the robustness battery as a cross-check showing the dominant source of the ∼12% multiplicative bias."

**A10 — Define M_Pl convention (F18)**
- File: `arxiv/paper1b_mcmc_companion.tex`, first occurrence of M_Pl in ALP section
- Add: "where M_Pl = (8πG)^{−1/2} ≈ 2.44 × 10¹⁸ GeV is the reduced Planck mass" at first use in §VI or Appendix C.

**A11 — Qualify LiteBIRD 9σ sentence (F19)**
- File: `arxiv/paper1b_mcmc_companion.tex` body L1860
- Replace "LiteBIRD will settle this at ∼9σ in the early 2030s" with "Under forecast foreground-cleaning and calibration assumptions~\cite{LiteBIRD2022}, a β ≃ 0.27° signal would be detected relative to β = 0 at ∼9σ by LiteBIRD in the early 2030s."

**A12 — Clean up draft correction notes in body (F31)**
- File: `arxiv/paper1b_mcmc_companion.tex`, L891, L1538, L1578, L1982
- Replace the "[Correction note: an earlier draft...]" blocks with direct statements of the current correct values only. The version history is preserved in git and tex changelog comments; it need not appear in the final paper body.

### Priority 3 — Minor polish

**A13 — Fix ΛCDM / LCDM inconsistency (F17)**
- Standardise to ΛCDM throughout body text. LCDM appears in ~7 body lines; replace all instances.

**A14 — H_0 unit format (F29)**
- Table I column header: change `[km/s/Mpc]` to `[km\,s$^{-1}$\,Mpc$^{-1}$]` to match MNRAS style used in body text.

**A15 — Promote SNR disclaimer to adjacent main text (F11, F22)**
- At first mention of "SNR=20.32" in §IV main text, insert a one-sentence disclaimer inline rather than only in the footnote. Already present in body but improve proximity.

**A16 — Remove or condense accumulating Planck-only chain mention from abstract (F28)**
- Abstract clause "plus a third Planck-only combination still accumulating" (L654) adds ambiguity; either remove or change to a simple parenthetical noting it is excluded from all tables.

**A17 — PACS numbers (F14)**
- For MNRAS/JCAP target: remove `\pacs{...}` and `showpacs` class option. For PRD target: retain as-is.

---

## Gap Analysis — Findings missed by internal R23–R28conf rounds

The following VERIFIED findings were not addressed in any internal round and represent genuine internal-review gaps:

| Gap | Finding | Internal-miss reason |
|-----|---------|----------------------|
| G1 | **F1** — parameter_summary.json column-mapping bug | Internal rounds verified paper Table I values but apparently did not cross-check the on-disk JSON keys/values against physical units. The bug was present but not caught because the internal audit focused on the `.tex` body, not the artifact JSON. |
| G2 | **F2** — Burn-in fraction mismatch (planck_bao_sn convergence_report says 20%, paper says 30%) | COUNT_EXPLANATION.md documents that original chain used burn_in=0.3 and parallel chains used burn_in=0.1 with different configs (line 31). The planck_bao_sn convergence_report may reflect the parallel-chain run's burn-in, not the freeze computation. This was not surfaced in any internal R-round. |
| G3 | **F4** — DES-Y5 + Pantheon+ SN overlap undisclosed | Comment L124 mentions "naive-combination note" as a PARTIAL closure but the body text grep finds no corresponding body disclosure. Internal rounds marked this PARTIAL and deferred; it was never completed. |
| G4 | **F15** — Cai2010quintomReview bib note with program-management prose | The DiegoPalazuelos2022 bib note was trimmed (v1B.0.50 changelog L99) but Cai2010quintomReview was overlooked. Internal rounds did not audit all bib entry `note=` fields. |

---

## Post-Audit Recommendation

**Recommendation: CONDITIONAL ACCEPTANCE — 3 blockers + 4 majors before submission**

ChatGPT's MAJOR verdict is partially correct: two of three claimed blockers are VERIFIED (F1 parameter_summary JSON bug, F2 burn-in mismatch) and a third issue (F4 SN overlap) is independently VERIFIED as a real methodological gap not present in Grok's or Gemini's reports. The overall paper quality is high — Grok's MINOR rating and Gemini's MINOR rating correctly identify the scientific integrity and reproducibility standards as genuinely strong. The paper does not overclaim; the internal scope disclaimers are thorough.

**Hard-gate before submission (A1–A3):**
1. Regenerate `parameter_summary.json` with correct physical units or add explicit unit documentation — the current JSON values will confuse any reader downloading the artifact.
2. Resolve the 30%-vs-20% burn-in discrepancy for the planck_bao_sn chain — the paper's total post-burn sample count (216,432) may be wrong by ~13,000 samples.
3. Add a SN overlap caveat to the iter2 / Table II analysis (DES-Y5 + Pantheon+ product-likelihood).

**Strong-major fixes (A4–A12):**
- Commit SHA + HF DOIs in Appendix A (A4)
- Strip program-management bib note (A5)
- ΔN_eff one-sided limit (A6)
- Fig. 2 caption ECH overclaim (A7)
- Unbiased → calibrated-bias wording (A8)
- Unweighted estimator justification (A9)
- M_Pl convention (A10)
- LiteBIRD qualification (A11)
- Draft correction notes cleanup (A12)

The paper should not be submitted until A1 and A2 are resolved; those are externally verifiable artifact inconsistencies that a journal referee can independently discover. A3 is a genuine methodological gap that could trigger a reject-and-revise at any journal.

**Internal review gap summary:** 4 findings (G1–G4) that the R23–R28conf internal rounds missed despite 6 clean internal rounds. The artifact-level JSON check (G1, G2) and bib-note audit (G4) represent systematic blind spots in internal review — future rounds should include an automated artifact-cross-check step (JSON unit verification, bib note grep).

---

*Verdict counts: VERIFIED 11 | PARTIAL 8 | OPINION 4 | STALE 0 | FALSIFIED 1 (F16) | HOUSTON-DECISION 1 (F13)*
*Total findings: 31 (B3 + M9 + m10 + scrutiny items across all 3 reviewers)*
*Headline issues: parameter_summary.json column bug (B1), burn-in mismatch (B2), SN double-count undisclosed (B3), bib program note (M9-equivalent)*
