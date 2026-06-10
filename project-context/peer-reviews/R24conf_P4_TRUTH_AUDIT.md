# R24conf P4 — TRUTH AUDIT (remaining findings after INSESSION wave)

**Auditor**: Claude (in-session), 2026-06-10, against `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.168 → v1.0.169 working tree)
**Scope**: all R24conf SYNTHESIS + META_REVIEW findings NOT already closed in the Claude_brutal_INSESSION wave.
**CLOSED-PRIOR (untouched, STALE here)**: INSESSION M1 (Table I "Reported statistic" relabel + "(moment z)"), M2 (axis-convention clause §VI), M3 (f_sky=0.4801 footnote, Table I row i), M4–M6 (self-resolved/no-action). Claude_brutal duplicates of the INSESSION items inherit the same verdicts.
**Ground truth anchors**: `outputs/dipole/catalog_c_summary.json` (0.41σ/p=0.31; shuffle 0.58σ/0.26), `outputs/canonical_provenance/c9/c9e_shot_noise.json`, `outputs/canonical_provenance/joint_nuisance_model_fit.json`, repaired `run_dipole_catalog_c.py`.

## ESSENTIAL findings

| ID | Sev | Claim | Verdict | Disposition |
|----|-----|-------|---------|-------------|
| META-E1 | ESS | "Analytic shot-noise floor 2.0×10⁻⁶ consistent with the null means above" — but canonical row ⟨C₁⟩=0.57×10⁻⁶ is 3.4× lower; field unspecified | **VERIFIED** | Artifact `c9e_shot_noise.json` proves the floor is computed for the apodized W_p=N_all convention (N_ℓ=1=2.006×10⁻⁶, matching that row's 1.93×10⁻⁶ null mean). Table III caption rewritten: floor tied to the apodized convention; canonical rows declared a different normalization with no analytic floor quoted. **CLOSED (textual, artifact-backed).** |
| META-E2 | ESS | ℓ=1 MASTER deconvolution conditioning/stability undemonstrated on patchy apodized mask | **VERIFIED→QUEUED** | Requires NaMaster coupling-matrix conditioning + apodization-length/jackknife stability runs. Queue #1 (R24CONF_COMPUTE_QUEUE.md). Paper already labels channel diagnostic-only, non-cosmological. |
| OpenAI-E1 (table_ii) | ESS | "+3.64σ canonical" vs Table III canonical row z=+7.93 = internal contradiction | **STALE/PARTIAL** | Table III caption already declares the +3.64σ a *distinct estimator* (500-MC direct single-mode vs 10⁴-perm full-39-band, galaxy-weighted subtraction) "superseded as a table entry but retained in the text." Reviewer recompute did not match SAMPLE+ESTIMATOR+NULL (R23conf dissolution rule). META-E1 caption rewrite further separates the conventions. |
| Grok-E1 | ESS | Abstract reports HC 0.41σ "without stating the selection" | **FALSIFIED** | Abstract states "(confidence >0.6; N≈9.5×10⁵ spirals)" inline, plus the unthresholded-sensitivity disposition. Selection is declared at first mention. |
| Grok-E2 | ESS | Remove withdrawn-result/provenance-audit language | **HOUSTON-DECISION** | Deliberate disclosure policy (standing rule). Not touched. |
| Grok-E3 (sigma_mixing) | ESS | "Not directly comparable" qualifier missing at every juxtaposition | **STALE** | Present in Results conventions paragraph + Table I/III/IV captions + §III C "not on the same statistical footing" passage. Per-paragraph repetition = opinion (OpenAI-N2 asks the opposite). |
| Grok-E4 | ESS | Factor 6–12 Shamir comparison apples-to-oranges | **STALE** | §I and §V already state "a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion"; claim is amplitude-level only. Matched reanalysis = external-data recompute, not queued (Shamir catalog not in repo). |
| OpenAI-E2 | ESS | Injection significances z≈68–218 lack in-paper table | **PARTIAL/HOUSTON** | Values + completeness P(≥3σ) are stated in Conclusions with artifact c9b. Full table = editorial format choice. |
| OpenAI-E3 | ESS | No formal 95% CL upper limit on A_dip | **VERIFIED→QUEUED** | `catalog_c_summary.json` stores null moments only, not the 10⁴ null array; rank-based UL needs regeneration. Queue #2. |
| OpenAI-E4 | ESS | σ definition for injection tests unspecified in §VI A | **PARTIAL→QUEUED** | Text states per-pixel-shuffle null + N_MC; the exact moment-z convention of the injection scorer needs script verification before asserting. Queue #3 (bundled with E5/M6 injection harmonization). |
| OpenAI-E5 | ESS | Mixed N_MC (200/500/10⁴) across displays | **PARTIAL/QUEUED** | 10⁴-perm Table III recompute exists; remaining 200/500-MC harmonization already declared queued in App E text. Queue #4. |
| OpenAI-E6 | ESS | Internal artifact paths in narrative | **HOUSTON-DECISION** | Deliberate `\artifact{}` reproducibility convention. |
| OpenAI-E7 | ESS | Fig 2 caption says production evaluates all eight D₄ transforms; §III C says 2-fold Z₂ | **VERIFIED** | Real caption/methods inconsistency. Fig 2 caption rewritten: production = 2-fold Z₂; D₄ = Appendix B hold-out validation. **CLOSED.** |
| OpenAI-E8 | ESS | Hemisphere LEE "double vs single correction" contradiction | **FALSIFIED** | The "applied once (no double correction)" sentence belongs to the 15-cell leg×confidence joint null (App C per-imaging-leg paragraph), not the 648-direction hemisphere scan. No contradiction; reviewer conflated two analyses. |
| OpenAI-E9/E10 | ESS | HC-broad A₅₀ floor used to dismiss full-sample 0.57% signal; no full-sample empirical floor | **VERIFIED** | True sample mismatch. §III C now states the floor is HC-broad-measured, comparison indicative, no unthresholded-sample floor exists. **CLOSED (textual)**; full-sample injection floor = Queue #5. |

## MAJOR findings

| ID | Sev | Verdict | Disposition |
|----|-----|---------|-------------|
| META-M1 | MAJ | **VERIFIED** | BH over 648 correlated directions assumes PRDS — App C now labels the BH/Bonferroni pass a conservative heuristic; direct-MC max-stat null declared the principled control. **CLOSED (textual).** |
| META-M2 | MAJ | **VERIFIED** | g=2a−1 symmetry unvalidated. §VI A now quantifies per-class GZ1 chirality accuracies from Table VIII (CW 39,011/57,900=67.4% vs CCW 42,928/59,305=72.4%; pooled 0.6991 ✓; NS triage 27,435/144,640≈19%), declares the 1.88% mapping approximate, observed-space A₅₀/A₉₅ operative. **CLOSED (textual, arithmetic shown).** |
| META-M3 | MAJ | **VERIFIED→QUEUED** | Equal-area slab rerun = recompute (Queue #6). Equal-count RA partition already in text. |
| META-M4 | MAJ | **VERIFIED** | CE-ResNet circularity: closed via reviewer option (iii) — explicit limitation sentence added §I (shuffle nulls don't test CE-ResNet-inherited gradients; Appendix D templates do). GZ1-only control model = Queue #7 (optional strengthening). |
| Grok-M1 | MAJ | **HOUSTON-DECISION** | Length (19pp; already condensed 54→19). |
| Grok-M2 (table_iv) | MAJ | **STALE** | +3.64σ already labeled non-headline, systematics-attributed, "not a positive detection" (App D operational conclusion). |
| Grok-M3 | MAJ | **STALE** | Fig captions carry explicit A_p vs f_CW unit conversions (Fig 3/sky-map and Fig 5/raw-vs-eq both state the ×2 relation). |
| OpenAI-M1 | MAJ | **VERIFIED→QUEUED** | Real-space robustness panel (uniform vs N-weighted fit; N≥10/20/50 threshold) — Queue #8. |
| OpenAI-M2 | MAJ | **STALE** | Conclusions explicitly segregate the two channels ("not interchangeable"). |
| OpenAI-M3 | MAJ | **PARTIAL→QUEUED** | Collinearity disclosed in Table IX caption; condition number = Queue #9. |
| OpenAI-M4 | MAJ | **VERIFIED→QUEUED** | A_dip vs p_eq curve — Queue #10. |
| OpenAI-M5 | MAJ | **STALE/PARTIAL** | Per-slab span, N, binomial σ quoted in §IV B prose; table format = editorial. |
| OpenAI-M6 | MAJ | **PARTIAL→QUEUED** | Area-uniform spot check already in §VI A; full area-uniform main curve = Queue #11. |
| OpenAI-M7 | MAJ | **CLOSED via META-E1** | App A monopole-subtraction statement consistent with the rewritten Table III caption. |
| OpenAI-M8 | MAJ | **VERIFIED** | Table I row (iv) f_sky=0.494 is geometric while row uses weights — footnote added: f_eff=0.452 (W_p=N_all, C² 2°; Table VI). **CLOSED.** |
| OpenAI-M9 | MAJ | **VERIFIED→QUEUED** | T7 flip-swap error split asserted, not quantified — Queue #12. |
| OpenAI-M10 | MAJ | **QUEUED** | 93.7% vs 94.9% augmentation ambiguity needs training-log verification before clarifying (never-fabricate rule). Queue #13. |
| OpenAI-M11 | MAJ | **STALE** | Table IV caption already declares the 768-dir grid distinct and non-comparable to the 648-dir scan. |
| OpenAI-M12 | MAJ | **VERIFIED** | "Does not introduce monopole–dipole coupling" over-strong — App A reworded (mean subtraction removes leading term; residual coupling governed by exact MASTER matrix). **CLOSED.** |

## MINOR/NIT findings

| ID | Verdict | Disposition |
|----|---------|-------------|
| META-m1 (T5 leakage test weak) | VERIFIED→QUEUED | Y_ℓm regression replacement = Queue #14. |
| META-m2 (f_eff normalization domain) | STALE | App A defines both normalizations + mask-restricted factors; artifact c11_meta_m3 cited. |
| META-m3 (dipole direction uncertainty) | VERIFIED | §III C now states the axis is unconstrained under the null. **CLOSED.** |
| META-m4 (constant vs multiplicative monopole) | VERIFIED | §IV A sentence added: generative test probes additive constant only; multiplicative handled by App D. **CLOSED.** |
| META-n1 (flip-swap 1.000 phrasing) | STALE | §III C + App B T1 already scope it as protocol check, raw network documented separately. |
| Gemini-M1 (consolidate ℓ=1 estimators) | STALE/OPINION | Declared hierarchy (§III A) + Table I + "same statistical footing" passage. |
| Gemini-M2 (Gaussian-equiv consistency) | STALE/PARTIAL | Abstract + Table III footer carry ≈1.9σ Gaussian-equivalent; Table III caption explains heavy-tail z vs rank-p. |
| Gemini-N1 (informal sub-heading) | VERIFIED | "Confidence-threshold sensitivity disclosure:" → "Sensitivity to the confidence threshold:". **CLOSED.** |
| Gemini-N2 ("uncommitted script") | VERIFIED | → "script that was not part of the version-controlled analysis pipeline". **CLOSED.** |
| Gemini-N3 ("dispositioned" ×2 in abstract) | VERIFIED | → "attributed to" / "characterized by". **CLOSED.** |
| Grok-N1 (no COI statement) | VERIFIED | COI + no-external-funding line added to acknowledgments. **CLOSED.** |
| Grok-N2/NIT1 ("canonical canonical-mask" typo; filenames in captions) | FALSIFIED / HOUSTON | grep: doubled phrase absent from source (extraction artifact). Artifact filenames = deliberate policy. |
| OpenAI-n1 (Catalog B 14.6σ rounding) | STALE | Table II caption: dev computed from unrounded calibrated fraction. |
| OpenAI-n2 (face-on = high inclination) | VERIFIED | → "(low-inclination)". **CLOSED.** |
| OpenAI-n3 (C² 2° spacing) | FALSIFIED | Source: `$C^2$ $2^\circ$` — extraction artifact. |
| OpenAI-n4 (Zenodo DOI) | HOUSTON-DECISION | Disclosed in Data Availability; minting at acceptance. |
| OpenAI-N1 ("evquivariant" etc.) | FALSIFIED | grep: no "evquivariant" in source. |
| OpenAI-n5 (row iv +7.28/+7.13 labels) | STALE | Null column "pp-sh./d-str." pairs positionally; caption spells it out. |
| OpenAI-n6 (σ_iso undefined) | VERIFIED | Definition added at first App C use. **CLOSED.** |
| OpenAI-n7 (sidedness convention) | VERIFIED | Default-sidedness sentence added to Results conventions paragraph. **CLOSED.** |
| OpenAI-n8 (Table IX z=−43.3 vs σ) | VERIFIED | Artifact `joint_nuisance_model_fit.json`: σ=1.0434×10⁻⁴, z=−43.285 — table now prints 1.04×10⁻⁴. **CLOSED.** |
| OpenAI-n9 (1.7% unit restating) | STALE/OPINION | A_ref=0.034 mapping given App D + multiple inline f_CW-unit tags. |
| OpenAI-n10 (−0.03σ estimator unnamed) | VERIFIED | §IV E names the confidence-stratified estimator + distinguishes from headline. **CLOSED.** |
| OpenAI-N2 (repetition) | OPINION | Conflicts with Grok-E3's demand for more repetition. |
| Claude_brutal P4-E1/M2/M4/M5/m1–m4/N1/N2, INSESSION twins | STALE | All-clears/verifications or CLOSED-PRIOR INSESSION items. |

## Verdict counts (P4, this wave)
- ESSENTIAL audited: 14 distinct → 2 VERIFIED-closed-textual (META-E1, OpenAI-E7), 1 VERIFIED-closed+queued (E9/E10), 3 VERIFIED→QUEUED (META-E2, E3, E4), 2 FALSIFIED (Grok-E1, OpenAI-E8), 3 STALE/PARTIAL, 2 HOUSTON, 1 PARTIAL/QUEUED (E5)
- MAJOR audited: 16 distinct → 5 closed textual (META-M1, M2, M4, OpenAI-M8, M12; +M7 via META-E1), 6 queued, 4 STALE, 1 HOUSTON
- MINOR/NIT: 10 closed textual, 4 FALSIFIED, 8 STALE/OPINION, 2 HOUSTON, 2 queued

**Pre-closure verified-and-open ESSENTIAL/MAJOR count: 16** (3 ESS + 13 MAJ requiring action), of which 9 closed textually this wave, 7+ queued as compute. **Not a clean round.**
