# P5 R27conf — TRUTH AUDIT (final verdict of the six-paper campaign)

**Paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.58 (working tree, post-§IX.A severity-honest rewrite)
**Reviewed PDF**: v0.1.58 md5=6ffcd714, 27 pp
**Ground truth**: `outputs/25_completeness_weighted_rebuild.json` + 16/17/18/21/22/23/24-series artifacts
**Auditor**: Claude (in-session), 2026-06-10
**Round status note**: synthesis header marks the round DEGRADED (Perplexity leg ran on `sonar` fallback without web access and could not perform citation forensics; the original Claude API leg failed on credits and was replaced by the in-session leg). Per protocol the round cannot count toward any clean-round counter regardless of this audit.

## Verdict schema
VERIFIED (real, fix applied/queued) · STALE (already fixed in current tex) · FALSIFIED (claim wrong vs repo ground truth) · CALIBRATED (deliberate-disclosure detector hit) · EDITORIAL (style/scope judgment, no factual defect) · QUEUED (recompute-class, not closable in-session)

## In-session leg (Claude_brutal / Claude_brutal_INSESSION — byte-identical reports)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| M1 | MAJOR | §IX.A buries relabeling magnitude (26.6% spiral agreement, void 17.6→0.75%) | **STALE** | tex 2022–2036 now foregrounds: "rewrites the environment field wholesale", 17.6%→0.75% (≈23×), 21 pp, 44% cells / 26.6% spirals, per-class parity in BOTH builds with per-bin σ (0.475±0.023/−1.1σ; 0.502±0.003). All values re-verified against 25-series JSON ✓ |
| m1 | minor | ±4.8 pp not labeled 2σ | **STALE** | abstract line 145–146 now says "the 2σ binomial half-width of the n=428 V-Web void bin"; §IX.A quotes explicit ±1σ values ✓ |
| m2 | minor | z<0.5 scope caveat missing | **STALE** | tex 2038–2043 "Scope caveat: … z>0.5 is not probed here and is bounded separately…" ✓ |
| m3 | minor | cube-3 ≤3.1 pp loses sign/direction | **STALE** | tex 2044–2046 "(driven by the void fraction decreasing 24.4%→21.2%…)" ✓ |
| m4 | minor | §IV.A negative completeness claim lacks pivot | **STALE** | negative claim and randoms-rebuild pivot are now the same paragraph (2011–2022); no isolated instance elsewhere (grep "completeness") ✓ |
| E1 | all-clear | §IX.A numbers reconcile with JSON | **VERIFIED-CONFIRMED** | independently recomputed this session; one residual micro-error found and fixed: weighted void σ=0.547 was typeset "+0.6σ" → corrected to "+0.5σ" |
| E2 | all-clear | 5 deliberate disclosures correctly characterized | **CALIBRATED** ✓ | ZONEVOID, count ledger, stratified LEE, unique-parent rebuild, sample-ledger sentence all present |

## Grok_brutal

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| P5-E1 | ESS | Abstract claims environmental test but rests on n=428 void bin; 0.26 pp is global | **FALSIFIED** | abstract already states the V-Web void bin is "sample-size limited… dominated by survey-edge artifacts" and "the controlling void constraint comes from the DESIVAST-anchored re-projection (n=56,981)"; 0.26 pp explicitly labeled a correctable classifier systematic, subtracted in monopole-referenced tests (lines 138–199). Reviewer's required fix is already implemented verbatim |
| P5-E2 | ESS | "Earlier draft" language throughout | **EDITORIAL/CALIBRATED** | provenance-transparency prose is a deliberate project convention pending journal-submission strip; several instances are the calibrated ZONEVOID/count-ledger disclosures. Submission-time cleanup tracked in SSOT, not a factual defect |
| P5-E3 | ESS | Pipeline paths/JSON names in body | **EDITORIAL** | `\artifact{}` reproducibility macro is deliberate (campaign-wide); journal-format strip is a submission-packaging step |
| P5-E4 | ESS | σ_from_half vs σ_pred lack "not comparable" qualifier at every juxtaposition | **STALE/PARTIAL** | qualifier present in abstract (161–163), §V (628–630), Table II caption (774), Table IV caption (1003–1006), and Table X caption explicitly contrasts comparability. Every caption mixing the two statistics defines both and states the baseline (Δf=−0.0026 Paper IV vs f^P5). Maximal per-sentence repetition not adopted — judgment call, no factual error |
| P5-M1 | MAJ | 27 pp too long; condense to ≤12 | **EDITORIAL** | length/venue judgment; consensus with Gemini M2 / OpenAI n3; noted for submission packaging, not a correctness defect |
| P5-M2 | MAJ | DESIVAST primary rests on artifact-dominated agreement | **FALSIFIED** | inverts the paper's logic: the artifact-dominated sample is the V-Web n=428 bin (secondary); DESIVAST n=56,981 is the independent catalog-anchored test, declared primary with reasons (§V.B, lines 695–710) |
| P5-M3 | MAJ | Density-quintile test mislabeled "local density" when it shows monopole | **FALSIFIED** | Fig./caption language is "Density-quintile null with Paper IV monopole-prediction overlay… tracks the monopole prediction"; the test probes density-dependence and reports a null vs monopole — correct framing (938–977) |
| P5-N1 | MIN | "largest … to date" unsupported superlative | **STALE** | already "to our knowledge, the largest matched-sample … in DESI DR1 to date" + "a null is not positive evidence" hedge (1633–1638), exactly the requested softening |
| P5-N2 | MIN | Figure typesetting pass | **QUEUED** (cosmetic) | production-pass item; no specific overlap reproduced |
| P5-NIT1 | NIT | "the the" typos, V-Web/T-Web caps | **FALSIFIED/PARTIAL** | grep "the the" → 0 hits; V-Web/T-Web nomenclature has a dedicated title footnote + §IV note |

## Gemini_cosmology

| ID | Sev | Claim | Verdict |
|---|---|---|---|
| E1 | ESS | Dependency on unpublished Paper IV | **EDITORIAL** — campaign-level: P4 is the companion submitted in the same wave; monopole derivation cited + value restated; condition resolves at co-submission |
| M1 | MAJ | "Earlier draft" prose | **EDITORIAL/CALIBRATED** (= Grok E2) |
| M2 | MAJ | Length | **EDITORIAL** (= Grok M1) |
| M3 | MAJ | Post-hoc primary designation | **STALE/PARTIAL** — explicitly declared + garden-of-forking-paths bound (§V.B); "move to intro" is structural preference |
| m1 | MIN | RSD caveat at first V-Web presentation | **VERIFIED-mitigated** — §VIII RSD paragraph now contrasts V-Web as "RSD-bounded only at the scalar-displacement level" with forward refs; further inline duplication editorial |
| m2 | MIN | Toy EFT appendix removable | **EDITORIAL** (consensus w/ OpenAI M5) — heavily caveated by design; kept per no-deferral of theory anchor |
| m3 | MIN | Ullah "future year… arXiv:2604.02463 should be 2404" | **AUTO-FALSIFIED** — today is 2026-06; 2604.xxxxx = April 2026, a valid current preprint ID |
| N1 | NIT | "Paper dated June 2026" | **AUTO-FALSIFIED** — date is real |
| N2 | NIT | V-Web/T-Web naming | **STALE** — title footnote + §IV note |

## OpenAI_methodology

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| E1 | ESS | se formula drops sqrt | **FALSIFIED** (extraction artifact) — tex 617 has `\sqrt{0.25/3.2\times10^6}`; radical present in source/PDF. Defensive parenthesization applied: `\sqrt{0.25/(3.2\times10^6)}` |
| E2 | ESS | "1 − 0.051/6" wrong Clopper–Pearson | **FALSIFIED** (extraction artifact) — tex 1561: `$1 - 0.05^{1/6} = 39\%$`, correct form and value (0.393) |
| E3 | ESS | Version-history prose | **EDITORIAL/CALIBRATED** (= Grok E2) |
| E4 | ESS | Post-hoc primary | **STALE/PARTIAL** (= Gemini M3) |
| E5 | ESS | Two monopole references not restated everywhere | **STALE/PARTIAL** (= Grok E4); §V 608–614 quantifies the denominator-convention difference (<0.01%) |
| E6 | ESS | §IX.A lacks per-class n/f_CW with uncertainties | **STALE** — the severity-honest rewrite now gives per-class f_CW, n, ±σ for both builds inline |
| E7 | ESS | "≈0.7" inconsistent with N=812,793 (should be 0.99) | **FALSIFIED** — 0.7 is the induced uncertainty at the N≈4×10⁵ class size with se=5.5e-4: 2·5.5e-4·√(4e5)=0.70 ✓. Antecedent clarified in tex: "for the same N≈4×10⁵ class" |
| E8 | ESS | Table IV ρ̄ log10(1+δ) values 1.55–2.21 implausible | **FALSIFIED** — under the documented global-mean convention low-z cells reach 1+δ~10–160 (in-mask mean δ=+62.3 in lowest shell, tex 2132–2134), so log10 values up to 2.2 are exactly right; caption cites exact-recompute artifact (21-series, key `META_M3_tableIV_density_definition`) |
| E9 | ESS | Eq. (1) missing parentheses | **FALSIFIED** — source is `\frac{\Delta f_{\rm CW}}{0.5/\sqrt{N}}`, unambiguous stacked fraction |
| M1 | MAJ | Abstract omnibus χ² lacks duplicate qualifier | **STALE** — abstract 166–169: "(χ²=3.00, p=0.39 on the 783,820 unique-spiral subset, so the 2.7% duplicate rows do not drive the verdict)" |
| M2 | MAJ | Promote global max-stat across Phase-2 cells | **STALE/PARTIAL** — Table VI caption carries p_global=0.36 (all nine)/0.27 with method; promotion to body sentence is placement preference |
| M3 | MAJ | Tempel low-n bins misreadable | **STALE/PARTIAL** — abstract/§IX.B label Tempel "supporting rather than load-bearing", filament-like bin the only quoted concordance |
| M4 | MAJ | Explicit footprint-mask split for Table IX | **QUEUED** — paper already carries the proxy caveat + "explicit footprint-mask re-tabulation is queued for the data release" (1788–1795) with the ≥1-void bound argument; recompute-class |
| M5 | MAJ | Toy EFT placement | **EDITORIAL** |
| M6 | MAJ | Dilation sensitivity table | **STALE** — cube-3 variant quantified in §IX.A (≤3.1 pp vol, 99.6% agreement, ≤0.77 pp) from 25-series artifact |
| m1–m7, n1–n3 | MIN/NIT | sig-figs, units phrasing, pp expansion, etc. | **QUEUED (cosmetic batch)** — no factual errors among them on spot-check; harmonization pass at submission packaging |
| M7 (pass-2) | MAJ | Across-NSIDE max-stat LEE | **QUEUED** (recompute: single-stream permutation across NSIDE 16/32/64; cheap on pod, not in-session — needs per-galaxy parent + shuffle harness) |
| M8 (pass-2) | MAJ | "per-shell table below" references a non-existent table | **VERIFIED → FIXED** — both occurrences rewritten to "per-shell statistics" (tex 2119, 2130); forward reference no longer promises a float |
| M9 (pass-2) | MAJ | Superlative justification | **STALE** (= Grok N1) |
| E7/E8/E9 (pass-2 dupes), m8–m10 | — | as numbered above | m8 (n=1/n=2 bins in Table XII range) **QUEUED-cosmetic**; m9 knot/cluster note **STALE** (title footnote); m10 units **QUEUED-cosmetic** |

## META_REVIEW (gpt-5-pro)

| ID | Sev | Claim | Verdict | Disposition |
|---|---|---|---|---|
| META-E1 | ESS | Phase-2 dilation iterations not scaled per Rs (Rs=50 needs 3, not 2) | **VERIFIED-QUEUED** | genuine blind spot; requires V-Web rebuild at Rs=50 w/ ⌈Rs/cell⌉+1=3 iterations + per-class shift table. Mitigation already in paper: cube-3 3-iteration variant at canonical Rs shifts f_CW ≤0.77 pp. Queued as R27conf-Q1 (pod recompute) |
| META-E2 | ESS | DESIVAST "RSD-insensitive" overstated; no membership-flip stability test | **VERIFIED → FIXED (textual leg) + QUEUED (recompute leg)** | language softened to "RSD-bounded" per reviewer's option (ii) + new empirical bound sentence: definition-variant reassigns 36,181/57,081 void spirals (≫ any RSD flip set) shifting Δf_CW by only 0.6 pp (24-series artifact). FoG-compressed rerun queued as R27conf-Q2 |
| META-M1 | MAJ | Permutation nulls run on 2.7%-duplicate parent | **PARTIAL-QUEUED** | χ²/per-pixel already reproduced on unique parent (22/23-series); TARGETID-level cluster-aware permutation rerun queued as R27conf-Q3 |
| META-M2 | MAJ | Logistic regression basis can't capture general dipole (no sin α; |sin δ| cusp) | **VERIFIED-QUEUED** | correct mathematical point; full ℓ=1 basis refit queued as R27conf-Q4 (cheap, needs per-galaxy table on pod) |
| META-M3 | MAJ | Fixed absolute λth across Rs conflates smoothing/threshold | **VERIFIED-QUEUED** | normalized-threshold sweep λ̃=λ/σλ(Rs) queued as R27conf-Q5 |
| META-M4 | MAJ | NN vs trilinear label assignment unchecked | **VERIFIED-QUEUED** | R27conf-Q6 (subset recompute) |
| META-M5 | MAJ | No mock-based classifier validation | **VERIFIED-QUEUED** | R27conf-Q7 (heaviest; mock suite w/ DR1 footprint) — alternatively limitation paragraph at submission |
| META-m1 | MIN | Residual null variance vs N(0,1) benchmark | **STALE/PARTIAL** | §V already propagates the 0.36–0.7 band and states no conclusion depends on finer thresholds; formal inflated-null benchmark folded into Q3 |
| META-m2 | MIN | Table IX at NSIDE=32/64 | **VERIFIED-QUEUED** | R27conf-Q8 (cheap re-binning) |
| META-N1 | NIT | "1.0″ fiber tolerance" framing | **STALE/PARTIAL** | §III.C already states "The 6.6-mas median … reflects shared coordinate provenance"; exact-phrase swap deferred to cosmetic batch |

## Score
33 synthesis findings → 11 STALE (incl. all 5 pre-closed in-session items, verified in tex), 9 FALSIFIED/AUTO-FALSIFIED, 2 CALIBRATED detector hits, 6 EDITORIAL, 2 VERIFIED-textual (fixed this session: OpenAI M8, META-E2 language) + 1 micro-fix (+0.6σ→+0.5σ), 8 VERIFIED-QUEUED recompute items (R27conf-Q1…Q8).

## Open recompute queue (carry to SSOT/queue.md)
Q1 per-Rs dilation Phase-2 rerun · Q2 FoG-compressed DESIVAST membership · Q3 TARGETID-level permutation + inflated-null residual benchmark · Q4 full-dipole logistic refit · Q5 normalized-λth sweep · Q6 trilinear label assignment · Q7 mock validation (or limitations paragraph) · Q8 Table IX NSIDE 32/64.

## Round verdict rationale
The two genuinely new ESSENTIAL findings (META-E1, META-E2) are recompute-class: E2's textual leg is closed this session with an artifact-backed empirical bound, but E1's per-Rs dilation rerun and the M1–M5 recompute family remain open, and the round is independently DEGRADED (Perplexity citation leg had no web access; counts as failed, not clean). NOT CLEAN.
