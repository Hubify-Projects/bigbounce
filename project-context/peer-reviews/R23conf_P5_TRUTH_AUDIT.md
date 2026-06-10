# R23conf P5 — TRUTH AUDIT (META-REVIEW + remaining SYNTHESIS findings)

**Auditor**: Claude (in-session), 2026-06-09, against `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.52 working tree)
**Scope**: every P5-META-* finding + all SYNTHESIS findings not already closed in the R23conf_P5_Claude_brutal_INSESSION wave (M1 Bonferroni-4 crossing, M2 count ledger, M3 row-level z caveat, m1–m8, Table II row label = CLOSED-PRIOR; Claude_brutal duplicates = CLOSED-PRIOR).
**New artifacts this wave**: `pipelines/p5_desi_chirality/scripts/21_r23conf_meta_closures.py` + `outputs/21_r23conf_meta_closures.json` (unique-subset omnibus χ², weighted HEALPix correlation, Table IV density-definition proof, canonical interior-buffer excision).

## META-REVIEW findings

| ID | Sev | Claim | Verdict | Disposition |
|----|-----|-------|---------|-------------|
| META-E1 | ESS | R_s=10 Mpc/h cells under-resolved on 25.9 Mpc/h cells (256³); robustness claim invalid there | **VERIFIED** | Closed via reviewer option (a): §VII grid-resolution caveat added — R_s=10 cells below grid sampling, retained only as degenerate near-unsmoothed limit, **excluded from the robustness claim**; resolved-cell (R_s∈{25,50}) max residual 1.64σ, p_LEE 0.13–0.48 restated; abstract parenthetical added. 512³ rerun = pod work, queued. |
| META-M2 | MAJ | Zero-padded FFT Poisson on masked volume; canonical run has no boundary control | **VERIFIED→CLOSED by recompute** | Interior-buffer excision applied to canonical labels (boundary flag from z-shell geometry): 782,015/783,820 retained; per-class f_CW shifts ≤0.11 pp (void), ≤0.05 pp others; omnibus χ²=2.93 (p=0.40) — stable. Text added §IX.A; artifact `21_r23conf_meta_closures.json`. Full window-deconvolved Poisson re-solve queued (pod). |
| META-M3 | MAJ | "smoothed log-density" vs linear-density inconsistency in Table IV | **VERIFIED (sharper than reviewer)** | Exact recompute proves Table IV's ρ̄ column IS mean log₁₀(1+δ_smooth) (cluster 1.548/1.804/2.006/2.214 ≡ published 1.55/1.80/2.01/2.21; n and σ exact). Caption mislabeled it as linear density — caption + §IV.A step 12 fixed; monotone-invariance of quartile binning stated. Artifact block `META_M3_tableIV_density_definition`. |
| META-M4 | MAJ | Omnibus 4×2 χ² on duplicate-bearing parent violates independence | **VERIFIED→CLOSED by recompute** | Row-level χ²=3.5469/p=0.3147 reproduced exactly; unique-TARGETID subset (783,820): χ²=3.00, p=0.39; excluding 79 conflicted TARGETIDs: χ²=2.92, p=0.41. Both results now in §VI.A + abstract. Artifact `21_r23conf_meta_closures.json`. |
| META-m5 | MIN | Unweighted Pearson on heteroscedastic per-pixel σ misleading | **VERIFIED→CLOSED by recompute** | Reproduced r=+0.00568/p=0.879 (727 pixels) exactly, then N_pix-weighted r_w=+0.004 (p=0.91, n_eff≈683) and Spearman ρ=+0.020 (p=0.59) — conclusion unchanged; added §VIII.F. Artifact `21_r23conf_meta_closures.json`. |
| META-m6 | MIN | Convergence test (R_s=25 only) doesn't validate R_s=10 | **VERIFIED** | Sentence added to §IX.A "Grid-resolution convergence": R_s=10 cells below 256³ sampling, outside tested convergence regime, excluded from robustness claim. |
| META-m7 | MIN | Holes (max 24.5 Mpc/h) vs maximal voids (10–32 Mpc/h) not cross-walked | **VERIFIED** | Catalog-layer clarifier added §VIII.E: membership tests use hole-level spheres, not maximal-void effective spheres; distinct max radii noted. |
| META-N8 | NIT | FFT k units/normalization + CIC deconvolution unstated | **VERIFIED** | §IV.A step 9: k_i = 2πn_i/L (scipy fftfreq×2π/cell, physical h/Mpc), CIC window NOT deconvolved, classification uses eigenvalue order/sign only so λ_th defined on this normalization. Source: `env_finder/_compute_vweb_lib.py` L53–55. |

## Remaining SYNTHESIS findings (non-INSESSION)

| ID | Sev | Verdict | Disposition |
|----|-----|---------|-------------|
| Gemini E1 / Perp m3, n3 / OpenAI E2 (remove "earlier draft / withdrawn / version tag" language) | ESS | **HOUSTON-DECISION** | Deliberate disclosure policy — kept (standing rule). Consolidation option (Claude N2) also Houston's call. |
| Gemini M1 / Perp M2 (length/restructure, move §IX–X to appendix) | MAJ | **OPINION/HOUSTON-DECISION** | Structural editorial preference. |
| Gemini m1 (σ_from_half circular naming) | MIN | **VERIFIED** | §V now states it is the standard one-sample binomial z-score vs p=0.5, name kept to distinguish from σ_pred. |
| Gemini N1 (title length) | NIT | **HOUSTON-DECISION** | Title change is author prerogative. |
| Gemini N2 (abstract footnote placement) | NIT | **STALE** | Non-comparability now in abstract body text. |
| Grok E1 (Δf=0.0007 never recomputed in body) | ESS | **FALSIFIED** | Body §VIII.A/Table VII gives f 0.4964 vs 0.4971, Δ=+0.0007 with full method; committed driver artifact cited. |
| Grok E2 (four σ side-by-side without qualifier) | ESS | **STALE** | Abstract states σ_from_half scales as √n and is "not mutually comparable" immediately after the four values. |
| Grok E3 / bib audit (DESIVAST "ApJ 982, 38 (2025)" = future volume; Ref [3] no arXiv; Ref [11] preprint) | ESS | **FALSIFIED (date) / HOUSTON-DECISION (companions)** | 2025 is the past (it is June 2026) — auto-falsify. Companion-paper citability = publication-order decision. |
| Grok M1 / Perp E1, E3, M1 (load-bearing unpublished companions; catalog black box) | MAJ/ESS | **HOUSTON-DECISION** | Publication-order/strategy; P5 already labels them "not yet peer-reviewed" at first use. |
| Grok M2 (void bin n=428 powerless; flag in caption) | MAJ | **STALE** | Abstract + §VI.A declare the ±4.8 pp 2σ floor and survey-edge caveat; DESIVAST n=56,981 is the controlling void constraint. |
| Grok M3 (σ_pred covariance across classes) | MAJ | **OPINION/PARTIAL** | Monopole is a global offset applied per class; classes are disjoint partitions (multinomial covariance is second-order at f≈0.5). No false statement identified. |
| Grok N2 (Fig 1 "DESI z" ambiguity) | NIT | **OPINION** | DR1 redshifts are spectroscopic by construction (§III.B ZWARN=0 spectro sample). |
| Grok NIT1 ("canonical canonical", "V-Web V-Web") | NIT | **FALSIFIED** | grep: neither doubled phrase exists in source — PDF text-extraction artifact. |
| Claude N1 / OpenAI M5 / Perp n1 (title "T-Web" vs body reserving "T-Web" for external) | MIN | **VERIFIED** | §IV.A nomenclature reminder harmonized: "T-Web" = the recipe (as in the title) + external implementations; "V-Web" = our implementation. |
| Claude N2 (withdrawal-note density) | MIN | **HOUSTON-DECISION** | See Gemini E1 row. |
| Claude N3 (Table VIII Δf_CW sign convention undefined) | MIN | **VERIFIED** | Caption now defines Δf_CW ≡ f_non-void − f_void (verified against all three rows). |
| Claude N4 (31.7% twice in §X — copy slip?) | MIN | **VERIFIED (coincidence confirmed)** | Artifact `analysis_astra_per_object/summary.json`: ASTRA sheet 7,980/25,186 = 31.68%, V-Web filament 7,972/25,186 = 31.65% — genuine coincidence; clarifying parenthetical added. |
| OpenAI E1 (Eq. (1) algebra "∆fCW 0.5/√N") | ESS | **FALSIFIED** | Source is `\frac{\Delta f_{\rm CW}}{0.5/\sqrt{N}} = 2\Delta f_{\rm CW}\sqrt{N}` — correct identity; extraction flattening. |
| OpenAI E3 (mask dilation unspecified) | ESS | **VERIFIED** | §IV.A step 5: scipy binary_dilation, face-connected cross element, ⌈R_s/cell⌉+1 = 2 iterations (code: `01_compute_vweb.py` L291–292). |
| OpenAI E4 / Perp M3 (post-hoc primary path) | ESS/MAJ | **STALE/OPINION** | §V.B declares the post-hoc designation explicitly and bounds the forking-paths concern; all paths reported. |
| OpenAI E5 / m12 (SPECTYPE/z-window §III.B vs §IV.A) | MAJ | **STALE** | §III.B already carries the "SPECTYPE==GALAXY and the V-Web finder's tighter window" clarifier (v0.1.51 OAI-E3 closure). |
| OpenAI E6 (match-radius sweep 0.5″ n>baseline) | MAJ | **CLOSED-PRIOR** | INSESSION m5 (counting-convention caption). |
| OpenAI M1 ("RSD-immune" too strong) | MAJ | **VERIFIED** | §VIII.A reworded to "RSD-insensitive (rather than strictly immune)… membership flips for spirals near hole boundaries are not excluded, but the displacement scale argument bounds their rate". |
| OpenAI M2 (multiple-testing narrative scattered) | MAJ | **STALE** | §VII "Per-cell significance framework" subsection ties range→floor→σ_vs_monopole→LEE explicitly. |
| OpenAI M3 (≥0.7 row vs table 0.4/0.6/0.8) | MAJ | **CLOSED-PRIOR** | INSESSION m5. |
| OpenAI M4 (show explicit two-sample z for 0.29 pp pair) | MAJ | **VERIFIED** | §IX.B now gives \|z\| = 0.49 pooled two-proportion (pooled≈unpooled at p̂≈0.5); recomputed from C2 artifact counts (12,360/6,155 vs 16,701/8,365). |
| OpenAI M6 (Bonferroni-9 ≈2.77 not 3.02) | MAJ | **VERIFIED** | Both occurrences (§VII.A, §VII.B) corrected to 2.77 (= √2 erfc⁻¹(0.05/9), Eq. (3)); max residual 1.87 still below threshold so all claims survive. Line 1983's 3.02 is the correctly-labeled (0.01,4) value — untouched. |
| OpenAI M7 (free-shuffle p re-draw discrepancy vs fixed seed) | MAJ | **VERIFIED** | §VI.E clarifier: re-draws use RNG streams distinct from the deterministic-seed headline runs; differences within N_MC=1,000 permutation standard error. |
| OpenAI M8 (position-shuffle never reported) | MAJ | **VERIFIED** | §V now states label- and position-shuffle induce the identical permutation null for per-bin count statistics; all quoted p-values are label-shuffle; position-shuffle retained as pipeline cross-check. |
| OpenAI M9 ("agree to within ~10%" unsubstantiated) | MAJ | **VERIFIED** | Replaced with the verifiable statement: both approaches return the same verdict on every scan (no scan crosses either threshold). |
| OpenAI m1 (define NS in Table I) | MIN | **VERIFIED** | Table I row now glosses NS as Paper IV's `not_spiral` class (verified against P4 source `\newcommand{\NS}{\textsc{not\_spiral}}`). |
| OpenAI m2 (reiterate σ non-comparability at Table IV) | MIN | **VERIFIED** | Added to the rewritten Table IV caption. |
| OpenAI m3 (Table VI range dominated by void noise) | MIN | **VERIFIED** | Added to Table VI caption. |
| OpenAI m4 (no per-galaxy cross-match vs Ref. [11]) | MIN | **VERIFIED** | Sentence added §IX.C: comparison purely on volume fractions. |
| OpenAI m5 (HEALPix pixel area note) | MIN | **VERIFIED** | §VIII.E: NSIDE=16 equal-area ≈13.4 deg²/pixel (corrected from reviewer's 3.66, which is the NSIDE=32 value). |
| OpenAI m6 ("2563" notation) | MIN | **FALSIFIED** | Source uses $256^3$ throughout; extraction artifact. |
| OpenAI m7 (Table VII add n_CW) | MIN | **VERIFIED** | n_CW column added: 28,286 / 309,173 (exact from artifact fractions × n). |
| OpenAI m8 (RSD 5 vs 5–8 Mpc/h) | MIN | **VERIFIED (reconciled)** | The two numbers cover different z-ranges; §XIII now cross-references: ≲5 at z≲0.24, upper end at high z. |
| OpenAI m9 ("largest matched-sample" claim) | MIN | **STALE** | Already qualified "to our knowledge … on the chirality-relevant subsample defined here". |
| OpenAI m10 (ASTRA Table XII per-class n) | MIN | **VERIFIED** | Per-class n column added from `cw_fraction_by_env_astra.csv` (argmax counts; entropy-weighted n_eff). |
| OpenAI m11 (+0.18% denominator) | MIN | **VERIFIED** | §VIII.B: "+0.18% of the 56,981-galaxy void class". |
| OpenAI m13 (n_pix definition Table V) | MIN | **VERIFIED** | Caption: occupied (data-containing) pixels, not full sky. |
| OpenAI m14 (\|σ_void\|≤1.35 not tabulated) | MIN | **VERIFIED** | Nine per-cell \|σ_void\| values added to Table VI caption from `17_v0151_closure_recomputes.json` (max 1.35 confirmed). |
| OpenAI m15 (z-shell per-class counts for χ²=0.11) | MIN | **VERIFIED** | Per-class n already in §IX.A prose; per-class n_CW (2,164/76,777/234,990/90,180) added at the χ² sentence (artifact-exact). |
| OpenAI n1 (define pp) | NIT | **VERIFIED** | Abstract first use: "0.26 pp (percentage points…)". |
| OpenAI n2/n3/n4/n5 (primes, Mpc/h style, asides, "χ 2") | NIT | **FALSIFIED/OPINION** | Source uses $1''$, $\chi^2$ correctly (extraction artifacts); Mpc/h vs h⁻¹Mpc mixed usage = style preference; long asides = opinion. |
| Perp E2 / M9 / E7, E6 (σ mixing; σ map at n=428 wrong) | ESS/MAJ | **FALSIFIED (E6/E7) + PARTIAL (reminders)** | E6's −0.85 is arithmetically wrong: 2·0.0164·√428 = 0.679 ≈ the published −0.68 (also OpenAI's spot-check −0.676 and Claude's all-clear). Comparability reminders strengthened at Table IV (and pre-existing §V/§VI.A statements); further per-juxtaposition reminders = opinion-level. |
| Perp M4 (bright/dark overinterpretation) | MAJ | **STALE** | Abstract + §VI.D explicitly state the data "do not allow us to cleanly partition" the two hypotheses; no claim of detection. |
| Perp M5 (RSD quantitative treatment) | MAJ | **PARTIAL→QUEUED** | Qualitative scaling + displacement bound present; a reconstruction-based quantitative RSD rerun queued (pod). |
| Perp M6 (0/6 V-Web purity small-sample) | MAJ | **STALE/OPINION** | Text already labels it an n=6 supplement to the n=56,981 re-projection. |
| Perp M7 (abstract "~2σ" void wording) | MAJ | **VERIFIED** | Abstract rewritten: ±4.8 pp = 2σ binomial half-width at n=428; observed void offset −0.68σ stated inline — ambiguity removed. |
| Perp M8 (σ→p mapping for "no 3σ" claims) | MAJ | **STALE/PARTIAL** | §V.A LEE framework + per-cell significance section give the mapping; headline claims cite both thresholds. |
| Perp E4 / m5 (toy EFT segregation) | ESS/MIN | **STALE** | App A opens with "toy parametrization introduced in this work… not a quantitative ALP-coupling exclusion" (v0.1.40/41 closures). |
| Perp E5 (repo paths in data availability) | ESS | **HOUSTON-DECISION** | Internal-path artifact convention is the project's deliberate reproducibility scheme; DOI minting at release. |
| Perp m1 (walk-through arithmetic) | MIN | **STALE/OPINION** | σ_from_half and σ_pred formulas explicit in §V; abstract now defines pp. |
| Perp m2 (informal language) | MIN | **OPINION** | Style. |
| Perp m4 (abstract claims → table refs) | MIN | **OPINION** | All numbers present in body tables (V, VI, §VI.C). |
| Perp n2 (redundant phrasing) | NIT | **OPINION** | Style. |

**Counts**: 8 META audited (7 closed — 3 by local recompute, 4 by artifact-grounded edits; 1 with residual pod queue item) · 55 synthesis rows audited (24 VERIFIED-closed, 12 STALE, 6 FALSIFIED, 7 OPINION, 5 HOUSTON-DECISION, 2 QUEUED, 2 CLOSED-PRIOR refs).
