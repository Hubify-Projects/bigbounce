# Canonical dispositions — P4′ (P4P)

Manuscript: `pipelines/p4prime_chirality_test/paper/main.tex` → `main.pdf`.
Sources it condenses: P4 `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.274)
and P5 `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.147).
Ledger opened 2026-09-02 at v4P.0.1. Line numbers below are verified against v4P.0.1.

---

## R1 wave (2026-09-02) — `ROUND_2026-09-02-P4P-v4P.0.1-EXACTPDF-a9cc2618-R1`

PDF sha256 `a9cc26183c631ba88d021edc4b46f35a295832a9b1ceb7879aacf8d38253099f` (verified).
Legs: Claude INT (major-revisions, 9 MAJOR / 11 MINOR), Grok API `grok-4.3` (REJECT, 10 items),
Gemini API `gemini-3.1-pro-preview` (REJECT, 6 items), **Perplexity ABSENT** (401 insufficient_quota —
optional leg, recorded absent per truth-audit skill Rule 4, never as zero-findings).
36 findings audited; 0 BLOCKER-tagged. Truth audit:
`project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P4P-v4P.0.1-EXACTPDF-a9cc2618-R1/P4P_v4P.0.1_R1_truth_audit.md`.
**Dedup: 20 canonical GENUINELY-NEW-REAL (10 MAJOR, 10 MINOR); 2 RE-FLAG-OF-DISCLOSED;
3 RE-FLAG-OF-DISCLOSED-IN-SOURCE (folded into DP4P-05); 4 FALSIFIED; 2 OPINION/GENRE.**
No leg found, and the audit found, **no arithmetic or transcription error in the measurement
layer** — every headline number traces correctly to P4/P5/the committed script.

### DP4P-01: Sample-size superiority claim mixes denominators; false vs Shamir 2022
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR)
- Abstract (tex l.98) "a sample 6–3,400× larger than the comparison catalogs"; §5.2 (l.332) "6 to 3,400 times smaller than the present catalog's **supported-pixel sample**"; §6 (l.414–415) "this is the largest single sample brought to the question".
- Verified: $887{,}472/1{,}300{,}000 = 0.68$ — Shamir 2022 (Table 1, l.348, $N=1.3$M, same survey) is *larger* than the primary channel. The "6" is $8{,}474{,}531/1{,}300{,}000=6.5$ (total catalog); the "3,400" is $887{,}472/263=3374$ (supported-pixel). No single denominator produces the range.
- Convergent across all three legs (Claude MAJOR-1, Gemini E2, Gemini M2).
- **Closure:** one named denominator throughout; concede Shamir 2022 exceeds the primary channel; restrict "largest" to the catalog release.
- **fingerprint:** sample-size, 6-3400, 887472, 1300000, Shamir 2022, denominator, largest single sample

### DP4P-02: "More than an order of magnitude" contradicts the paper's own Table 1 and §6
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR)
- Abstract l.96–97, §5.3 l.359–361, §7 l.445–446 say "more than an order of magnitude"; Table 1's own Ratio column is 7.1/5.1/2.0/2.0/20.4 (four of five below 10) and §6 l.417 says "2–20× tighter". Abstract's "~7–33%" silently drops Table 1's 2–4% rows, including same-survey Shamir 2022.
- **Closure:** "2–20×" and "2–33%" uniformly in abstract, §5.3, §7.
- **fingerprint:** order of magnitude, 2-20x, 7-33%, 2-33%, Table 1 ratio, abstract overstatement

### DP4P-03: Figure 1 is P4's full-catalog map, mis-captioned by sample *and* by quantity
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR) — directive I6 (baked-into-PNG class)
- `md5 fig_sky_map.png = 7156f1af3c2ea3e6a0b7e47c6899802d`, byte-identical to `p2_chirality/fig_sky_map.png` and `p2_chirality/figs/fig_sky_map.png`. 300-DPI render of p. 2: baked-in title "Galaxy Chirality Asymmetry Map (**8.47M galaxies**, equivariant)", colorbar $(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})$, ±0.08. P4 caption (l.1234–1244): full-catalog **FSC** support, $f_{\rm sky}=0.49005$.
- P4′ caption (l.202–205) claims the **887,472-row HC supported-pixel** sample "used for the primary dipole fit" and calls it a "CW-fraction map". Two defects: wrong sample (HC-RI 23,633 px vs FSC 24,087 px) and wrong quantity (asymmetry $A_p=2(f_{\rm CW}-\tfrac12)$, not $f_{\rm CW}$).
- Claude MAJOR-3 (sample) + Gemini M1 (quantity) — same figure, one canonical item.
- **Closure:** regenerate from the 887,472-row sample, or retitle+recaption honestly as the full-catalog map and state the primary support is a subset. Text grep cannot see this — render-verify.
- **fingerprint:** fig_sky_map, 7156f1af, 8.47M, CW-fraction, asymmetry, colorbar, FSC, supported-pixel, I6

### DP4P-04: κ=0.97 is the retrain's, not the released classifier's; κ=0.40 omitted
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR)
- P4′ §2 l.179–181 quotes only "Cohen's $\kappa=0.97$" — the manuscript's *only* classifier-quality number.
- P4 l.1810 verbatim: "*This $\kappa=0.9733$ figure is neither comparable to, nor a replacement for, the $\kappa=0.40$ / $69.91\%$ figure above*"; P4 l.1054: the retrain "does *not* alter the released Catalog C labels"; P4 l.1807: released classifier, full GZ1 cross-match $N=117{,}205$ → 69.91% agreement, $\kappa=0.40$.
- Also omitted: irreproducible historical realization (26,616 vs 26,626; 826 vs 846 CE non-spirals), ~67.5–72% CE-ResNet dependence, and the CE-included retrain's collapse to chance (0.5617 three-class; 0.517 binary on clean held-out GZ1) — P4's own "honest negative".
- **Closure:** report the released classifier's GZ1 confusion / 69.91% / κ=0.40 in §2 and carry the provenance disclosure + honest negative in condensed form.
- **fingerprint:** kappa 0.97, kappa 0.40, 69.91, released classifier, retrain, GZ1, CE-ResNet, honest negative

### DP4P-05: Not self-contained as an ApJS catalog paper
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR) — venue/scope; absorbs three RE-FLAG-IN-SOURCE items
- §2 (l.165–169) and Data Availability (l.471–475) defer schema, selection function, completeness/purity, estimator spec, systematics, and the void secondary diagnostics to [15]/[16].
- All of it exists in the sources and is simply not carried over: completeness ~30% at $N_{\rm HC}=949{,}584$ / purity ~70%; NSIDE=64, $N_{\rm spiral}(p)\ge10$, 23,633-px HC-RI vs 24,087-px FSC, $f_{\rm sky}=0.49005$; the injection–recovery curve (P4 l.1505); **P4's NaMaster MASTER-decoupled $\ell=1$ + NSIDE=8 block-bootstrap joint covariance** (P4 l.179–187, l.267 — settles Grok M1); **P5's clustering-robustness ladder** (P5 l.2020: NSIDE 2/4/8 + 3,750 nearest-MAXIMALS clusters, point estimate $+0.00145442$ throughout, all intervals containing zero) and **void-definition sensitivity across VoidFinder / V2-REVOLVER / V2-VIDE** (P5 l.1785–1806 — settles Grok M2); P4's harmonic diagnostics (settles Grok N2).
- Convergent: Claude MAJOR-5, Grok E2/M1/M2/N2, Gemini E1. Both REJECT verdict words are driven by this item and DP4P-07, not by any defect in the science.
- **Closure:** Route A (restore ~7–9 pp; target 13–15 pp, inside the ≤15 pp allowance in `PORTFOLIO_DECISION_2026-09-02.md` l.78) or Route B (6-pp Letter, viable only once P4/P5 have DOIs — and that changes title and venue). Full restore list in the R1 truth audit.
- **fingerprint:** self-contained, standalone reader, ApJS catalog, schema, completeness, purity, selection function, NSIDE, f_sky, injection-recovery, MASTER, covariance, clustering ladder, void definitions

### DP4P-06: FSC $\ell=1$ dropped and the monopole caveat truncated mid-sentence
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR)
- (1) P4 l.1073/l.1083/l.1124: FSC support fixed-occupancy null gives $\ell=1$ moment $z=+6.923$, add-one rank $p=0.001996$ (binomial-monopole nulls $+6.983$/$+7.207$). P4′ l.139–142 disposes of the harmonic diagnostics in a subordinate clause.
- (2) P4 abstract l.996 (verbatim): the classifier-injection forward model "localizes its origin **upstream of the classifier, without resolving whether that origin is a true sky asymmetry or a DESI imaging systematic**". P4′ l.177–179 stops at "(0.0% of the observed value)", converting an unresolved systematic into a closed one.
- **Closure:** state the FSC $\ell=1$ result and why it does not overturn the primary null (support/estimator/null differences); restore the unresolved-origin clause verbatim.
- **fingerprint:** FSC l=1, 6.923, 0.001996, monopole, upstream of the classifier, unresolved origin, truncated caveat

### DP4P-07: Principal references are non-archival source paths; [15] carries the wrong version; [14] is bare
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR). **The "private repository" premise is FALSIFIED** — anonymous `curl` of `github.com/Hubify-Projects/bigbounce` and of the `/blob/main/…chirality_catalog_paper.tex` URL both return **HTTP 200**. The citability defect survives at full strength regardless.
- [15]/[16] are working-tree `.tex` sources with no journal, no arXiv id, no DOI, no publication status; every substantive deferral (DP4P-05, DP4P-06) points at them, and in print they render as bare paths.
- [15] renders "**v4P.0.1** archived release" — *this* manuscript's version stamped onto the P4 reference by a `\paperVersion{}` macro bug at **tex l.554**, while the same entry's path says v1.0.274.
- [14] DESIVAST: no authors, arXiv id, DOI or URL, and it is the entire basis of §4.
- **Closure:** deposit P4/P5 as arXiv/Zenodo objects and cite DOIs (or restore per DP4P-05); fix l.554; give [14] its DOI/URL.
- **fingerprint:** ref 15, ref 16, .tex path, no DOI, non-archival, paperVersion macro, l.554, v4P.0.1 stamp, DESIVAST citation, private repo FALSIFIED

### DP4P-08: Internal governance path cited in §1 body as scientific justification
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR)
- tex l.140–141, rendered p. 2 l.63–64: "(see project-context/PORTFOLIO\_DECISION\_2026-09-02.md, Track C1 Addendum)", supporting "which is why the present catalog is an on-vision test … rather than a detached data product".
- Convergent: Claude MAJOR-7, Grok E1, Gemini E3.
- **Closure:** delete the parenthetical; the scientific motivation stands on the Popławski citation alone.
- **fingerprint:** PORTFOLIO_DECISION, project-context, internal path, Track C1, on-vision, body text

### DP4P-09: Eq. 1 is a detection-power threshold used as a 95% CL exclusion
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR)
- Eq. 1 is defined operationally (l.212–215) as the amplitude at which recovered detection probability crosses 95% coverage (P4 l.1505: detection = one-sided add-one rank $p<0.05$ vs the committed $10^4$ null). The abstract (l.86–88) calls it a "95% sensitivity upper limit" and §5.2 (l.318–323) uses it to "exclude" $\eta>A_{95}^{\rm obs}$. A power statement and a CL upper limit are different objects.
- No confidence interval or upper limit is quoted anywhere for the measured $A_{\rm dip}=0.467\%$, though the committed $10^4$-draw null makes one directly constructible.
- **Closure:** quote a 95% CL upper limit on $A_{\rm dip}$ from the committed null alongside Eq. 1; state explicitly wherever "excludes" appears that it is a power/coverage statement.
- **fingerprint:** A95, power threshold, coverage, upper limit, excludes, no CL on A_dip, 0.467

### DP4P-10: Table 1 pools non-commensurable statistics; the script's own g-bridge result is unreported
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR)
- The single "Amplitude" column pools Longo's dipole amplitude, Shamir 2012's per-bin asymmetry, Shamir 2020/2022's global asymmetry fraction, and Shamir 2025's CW:CCW count ratio (script `label_type` fields: "physical (visual/algorithmic)", "algorithmic (Ganalyzer)" ×3, "algorithmic/visual"), all compared to a floor on *this* paper's ViT-Small+TTA observed labels. Assumption 2 (l.370–376) addresses the observed→physical bridge but never cross-pipeline label incommensurability.
- Committed JSON: `shamir2020` and `shamir2022desi` are both `exceeds_A95_obs_face_value: true`, `exceeds_A95_obs_after_g_bridge: false` ($0.02\times0.398=0.00796<0.0098$). Under the paper's own illustrative bridge the two largest-$N$ rows — including same-survey Shamir 2022 — drop out. Assumption 2 correctly refuses to use $g$ to *strengthen* the claim; that it *weakens* it materially is unreported.
- **Closure:** add the incommensurability caveat; report the g-bridge exceedance flip.
- **fingerprint:** Table 1, incommensurable, Ganalyzer, label space, g=0.398, exceeds_A95_obs_after_g_bridge, shamir2020, shamir2022desi

### MINOR items (all GENUINELY-NEW-REAL, all OPEN)
| ID | Item | Evidence |
|---|---|---|
| DP4P-11 | Assumption 4 (l.382–385) cites an "$N$-scaling comparison in Table 1"; Table 1 has no such column (`illustrative_sensitivity_floor_at_this_N` exists only in the JSON) | Table 1 cols = Source/Amplitude/N/Ratio |
| DP4P-12 | Assumption 3 (l.377–381) is inverted — `healpy.fit_dipole` fits direction as well as amplitude, so a free-axis fit is the *correct* match to a free-axis model | estimator definition, l.192 |
| DP4P-13 | Shamir 2025 "20–33%" conflates asymmetry fraction with count ratio | script note "~2:1 to 1.5:1 CW:CCW imbalance" |
| DP4P-14 | Longo ">5σ" (l.113–114) vs the committed script's "~5 sigma" | script `amplitude_note` |
| DP4P-15 | No Software / Facilities / Acknowledgements / ORCID section (ApJS-required) | `grep -ci` → 0 |
| DP4P-16 | Fig. 2 legend "Paper IV global $\bar f_{\rm CW}=0.4974$" — undefined internal series label, baked into the PNG (directive I6) | 300-DPI crop of p. 3 |
| DP4P-17 | Numeric citation style + hand-rolled `thebibliography`, not AASTeX author-year | preamble l.27 |
| DP4P-18 | No multiplicity statement across the three reported tests (dipole, void/non-void, T-Web) | §3, §4 |
| DP4P-19 | Fig. 2's Filament (≈0.4980) / Cluster (≈0.4958) sub-parity offsets visible with small error bars but unmentioned; they are DP4P-06's residual monopole | 300-DPI crop of p. 3 |
| DP4P-20 | Catalog file format, row/column schema and size not stated | Data Availability. (DOI + HF mirror themselves verified public: both HTTP 200 — that half of the finding is FALSIFIED) |

### FALSIFIED / RE-FLAG / OPINION — do not re-open without new evidence
| Finding | Verdict | Source-cited basis |
|---|---|---|
| Grok E3 — "abstract mixes supported-pixel and quality-controlled totals without clarification" | **FALSIFIED** | Abstract l.84–85 reads "$N_{\rm support}=887{,}472$ **of** $890{,}069$ quality-controlled rows" — both named; body l.171–176 gives the full ladder 949,584 → −59,515 → 890,069 → 887,472. (The undefined term "sufficient coverage", l.175, is real and lives in DP4P-05.) |
| Grok E4 — "exclusion presented without a numerical model→observable mapping" | **RE-FLAG-OF-DISCLOSED** | l.94–96 "under the minimal closure needed to make the claim quantitative"; l.310–313 in italics "Eq. 3 is *not* derived from Popławski's papers"; l.364–369 assumption 1. Grok's proposed fix is the manuscript's existing wording. |
| Grok M3 — "$1/\sqrt N$ ansatz is not an independent re-analysis; label illustrative" | **RE-FLAG-OF-DISCLOSED** | Assumption 4, l.382–385 verbatim: "it illustrates statistical reach and is **not a re-derivation of any other paper's estimator, mask, or null**". (Table-column sliver → DP4P-11.) |
| Grok M1 / M2 / N2 — missing mask-robustness, T-Web/VoidFinder consistency, higher-multipole test | **RE-FLAG-OF-DISCLOSED-IN-SOURCE** | Present in P4 (l.179–187 NaMaster MASTER $\ell=1$; l.267 NSIDE=8 block bootstrap; l.1693 harmonic) and P5 (l.1785–1806, l.1010, l.2020). Real *as omissions* → folded into DP4P-05; **not** missing analyses. |
| Gemini N1 — "95% CI bounds slightly off" | **FALSIFIED** | P5 committed (l.1004–1006) $[-0.00504290,+0.00795174]$ from $0.00145442\pm1.959964\times0.00331502$ (recomputed: $[-0.00504302,+0.00795186]$, 6-s.f. agreement). P4′ rounds correctly to $[-0.00504,+0.00795]$. Gemini re-derived from the *rounded* SE. |
| Gemini E3 (part) — "[15]/[16] contain internal version tags v1.0.274 / v0.1.147" | **FALSIFIED** | Citing a source's version is normal practice. The real reference defect is different and is DP4P-07 (the "v4P.0.1" stamp from the l.554 macro bug). |
| Claude MAJOR-7 (premise) — "[15]/[16] are in a **private** repository" | **FALSIFIED** | Anonymous HTTP 200 on the repo root and on the `/blob/main/…` file URL. Substantive defect survives as DP4P-07. |
| Claude MINOR-20 (part) — "confirm the Zenodo DOIs and HF mirror resolve publicly" | **FALSIFIED** | `doi.org/10.5281/zenodo.21461899` → 200; `huggingface.co/datasets/bamfai/galaxy-chirality-catalog` → 200. Format/size sliver → DP4P-20. |
| Grok N1 — "DRAFT VERSION SEPTEMBER 2, 2026 — update to submission date" | **OPINION/GENRE** (NIT) | AASTeX default draft header; date equals the actual current date (skill Rule 3). Remove `linenumbers`/draft header at submission. |
| Grok N3 — repetition of "qualitative alignment tendency" | **OPINION/GENRE** (NIT) | Three sites (l.93–94 abstract, l.297–298 §5.1, l.442–443 §7) — normal abstract/body/conclusions structure. |

### Verified-correct register (no leg disputed these successfully, and the audit re-checked them)
8,474,531 catalog objects; 949,584 − 59,515 = 890,069; $N_{\rm support}=887{,}472$; $A_{\rm dip}=0.467\%$, $z_{\rm mom}=+0.635$, $p=0.238$; $A_{95}^{\rm obs}=0.98\%$; $10^4$-draw fixed-occupancy null; DESIVAST 694,642 → 145,789 → 145,766 = 31,937 + 113,829; $\Delta f_{\rm CW}=+0.00145$, SE $0.00332$, CI, $p=0.661$ / wild-cluster $0.673$ (matches P5 to 6 s.f.); 812,793 = 428 + 6,673 + 408,187 + 397,505; Table 1 ratios vs the committed JSON (7.143/5.102/2.041/2.041/20.408); Iye 2021 = arXiv:2011.00662, Patel & Desmond 2024 = arXiv:2404.06617. `main.log`: 0 overfull/underfull, 0 undefined refs.
**§5.1's central finding — that Popławski's papers (arXiv:1007.0587, 1111.4595, 1410.3881, 1910.10819) contain no computed dipole amplitude, alignment fraction or relaxation timescale — is confirmed against the committed script's `quantitative_amplitude_predicted: false` and its verbatim reading note, is the paper's genuine contribution, and is stated at the correct evidential strength.** The bounce-scope disclaimer appears in the abstract, §1, §5.2, §6 and §7; no bounce claim is smuggled in.
