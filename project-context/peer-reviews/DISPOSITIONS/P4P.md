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

---

## R2 wave (2026-09-02) — `ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2`

PDF sha256 `78936e3610b2d9274e2ba19b8567207b7cd1cb99d9368585d6ff3d78ac9d1db1` (verified), 10 pp.
Legs: Claude INT (major-revisions, 3 MAJOR / 13 MINOR), Grok API `grok-4.3` (REJECT, 10),
Gemini API `gemini-3.1-pro-preview` (MAJOR REVISIONS, 7), **Perplexity ABSENT** (401
insufficient_quota — optional leg, recorded absent, never as zero findings).
33 findings audited. **21 canonical GENUINELY-NEW-REAL (6 MAJOR, 15 MINOR); 8
RE-FLAG-OF-DISCLOSED; 2 FALSIFIED; 2 OPINION/GENRE.** R1 status: 16/20 closed, R3 and R9
partial (→ DP4P-26, DP4P-22), R5 page target and R17 open (→ DP4P-42/43, DP4P-34).
Truth audit: `INT_v3/ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2/P4P_v4P.0.2_R2_truth_audit.md`.

### DP4P-21: primary channel's own monopole unreported; sign-flipped vs both narrated monopoles
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR, disclosure) — **science question RESOLVED in-audit**
- Recomputed from `pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet`
  under the committed selection + support: 454,968 / 887,472 = **0.5126562** (A_p = **+2.53%**).
  Cause: the 59,515 quarantined `raw_flip_qc_unsafe` HC rows are **75.2% CCW** (44,739 CCW /
  14,776 CW), so the safe cut flips HC 0.4960583 → 0.5126562. Catalog-wide 0.497353 (P4 l.1283)
  and HC-with-unsafe −3.9486e−3 (P4 l.1289, `g4_monopole_mechanism_injection.json`) are each
  correct for their own samples.
- **Eq. 1 baseline branch FALSIFIED:** the generator computes `p_cw_global` from the same strict
  sample/support it injects into (`a95_observed_label_upper_limit_v1_0_265.py` ll.128, 139–141),
  so A_95^obs = 0.98% and §5's confrontation are unaffected; the uniform-weight estimator absorbs
  a constant monopole into its fitted `m` (P4 l.1289 generative test, 0.39σ).
- **Closure:** state the primary channel's f_CW, its A_p, and the parity-asymmetric quarantine in
  §2.2. No new computation needed.
- **fingerprint:** p_cw_global, 0.512656, 454968, 887472, quarantine 59515 CCW, monopole sign flip, Eq.1 baseline

### DP4P-22: the "genuine 95% CL statement" is the null's 95th percentile, not an upper limit
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR, statistics) — R1 DP4P-09 partial-closure residue
- §3 l.377–384, cited as authoritative at §5.3 l.691–693. Null re-reduced: mean 0.00362029,
  sd 0.00164643, 95th pct 0.0066932 ✓ — a critical value of the no-signal law, equivalent to the
  reported rank p = 0.238, for a positive-definite estimator with null mean 0.362%.
- Correct construction = Neyman inversion of `per_amplitude`; only p16/p50/p84 are stored, so a
  true 95% limit is **not yet computable** (p16 inversion gives ≈0.58%, an ~84% limit).
- **Closure:** re-run the injection storing `recovered_amp` p5 and quote the inverted limit, **or**
  drop the CL claim and rest on detection power.
- **fingerprint:** 95th percentile, 0.669, critical value, upper limit, Neyman inversion, recovered_amp p5, 0.58

### DP4P-23: 4×4 bootstrap matrix imported without per-estimator z's; headline z = +2.21 withheld
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR) · §3 l.447–475
- P4 l.1436 verbatim: "z = +2.21 real-space dipole, +0.81 WLS dipole, −0.61 MASTER ℓ=1"; P4′
  prints only the monopole's −6.57 while headlining z_mom = +0.635 from the label-randomization null.
- **Closure:** print all four z's with P4's own one-sentence reconciliation.
- **fingerprint:** joint covariance, z=+2.21, +0.81, -0.61, -6.57, block bootstrap, selective import

### DP4P-24: abstract omits the g-bridge caveat the body says "should not go unstated"
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR) · abstract l.99–101 vs §5.3 l.652–659 (Gemini E1)
- **Closure:** one clause in the abstract noting the exclusion weakens on the two largest
  comparison samples under the illustrative bridge.
- **fingerprint:** abstract-body drift, g-bridge, 2-20x, should not go unstated, pattern-045

### DP4P-42 / DP4P-43: DP4P-05 residue — no column-by-column schema table (§2.1 l.170–209); completeness/purity only as two integrated scalars (l.185–188)
- **class:** OPEN — GENUINELY-NEW-REAL (MAJOR, venue). ≈1.0–1.25 pp → ~12–13 pp, inside the ≤15 pp allowance.
- **fingerprint:** schema table, dtype, flag semantics, completeness function, purity, magnitude, half-light radius

### MINOR items (all GENUINELY-NEW-REAL, all OPEN)
| ID | Item | Evidence |
|---|---|---|
| DP4P-25 | §1 l.152 gives the primary N as 890,069, not 887,472 | abstract l.87–88, §3 l.341 correct |
| DP4P-26 | §3 l.345–346 still calls Fig. 1 the HC CW-fraction map, contradicting the corrected caption (R1 DP4P-03 residue) | l.345–346 vs caption l.351–358 |
| DP4P-27 | Table 2 omits T5; caption says "all seven" | P4 l.1792/1794 carries the honest disposition |
| DP4P-28 | [15] (paper) and [17] (dataset) share DOI 10.5281/zenodo.21461899 | p.10; l.200–201; l.863–864 |
| DP4P-29 | Table 3 caption "The four rows" — five rows, four statistic families | caption l.668 |
| DP4P-30 | Catalog-wide monopole value/σ/significance never together in body text | only in Fig. 3 caption; P5 l.1037/1171 |
| DP4P-31 | T-Web Void bin N = 428 (no power); per-class N absent from text | 300-DPI Fig. 3, sums to 812,793 ✓ |
| DP4P-32 | Keywords not UAT terms with identifiers | l.110–111 |
| DP4P-35 | Draft-mode artifacts; 3 stuck-float warnings + 5.88 pt overfull hbox | `main.log` ll.758/778/799/767 |
| DP4P-36 | [11] Popławski publication status unstated; year vs identifier | p.10; §5.1 l.602–613 |
| DP4P-37 | "primary HC sample N = 949,584" (§3 l.450–451) collides with the paper's own 887,472 | rename "pre-QC HC sample" |
| DP4P-38 | "on-vision test" promotional framing survives at l.146 (DP4P-08 residue) | l.146 |
| DP4P-39 | Internal audit prose "post-review 13-column basis" at l.505 | l.505 (keep the exploratory disclosure l.511–512) |
| DP4P-40 | No frozen commit-hash/DOI revision pin (directive Q2) | Data Availability l.859–887 |
| DP4P-41 | Title asserts "an Exclusion" of a model with no computed amplitude | title l.67 vs §5.1 |

### FALSIFIED / RE-FLAG / OPINION — do not re-open without new evidence
| Finding | Verdict | Source-cited basis |
|---|---|---|
| Grok E2 — abstract omits the support size of z_mom/p | **FALSIFIED** | abstract l.87–89 verbatim "(N_support = 887,472 of 890,069 …) … (z_mom = +0.635, one-sided p = 0.238)" |
| Gemini M1 — SE 0.00332 vs CI inconsistent | **FALSIFIED** (repeat of R1 Gemini N1) | P5 l.1004–1006: 0.00145442 ± 1.959964 × 0.00331502 → [−0.00504302, +0.00795186]; Gemini re-derived from the rounded SE |
| Grok E3 — not standalone / withdraw catalog claim | **RE-FLAG-OF-DISCLOSED** | R1 DP4P-05 Route A executed (l.170–209, §2.3 l.308–333, injection table, 4×4 covariance, P5 ladder + void family); residue is DP4P-42/43 only |
| Grok E4 / Gemini E4 — nulls juxtaposed without "not directly comparable" | **RE-FLAG-OF-DISCLOSED** | l.396–399 names the different support, estimator and null family |
| Grok M1 — relabel A_95^obs as observed-label floor | **RE-FLAG-OF-DISCLOSED** | abstract l.90, §3 l.385–390, assumption l.708; CL half → DP4P-22 |
| Grok M2 — remove the ratio column | **RE-FLAG-OF-DISCLOSED** | R1 DP4P-10 closure: caption l.668–673 + g-bridge flip l.652–659 |
| Grok M3 — declare exploratory / preregister | **RE-FLAG-OF-DISCLOSED** | l.511–512 "exploratory, not preregistered"; multiplicity l.572–578 |
| Gemini E3 — [16] has no DOI | **RE-FLAG-OF-DISCLOSED** | the paper states this itself; blocker tracked under DP4P-28 |
| DP4P-33 — no ORCID | **RE-FLAG-OF-DISCLOSED** (submission-kit) | R1 R15 residue, SSOT-recorded, correctly not fabricated |
| DP4P-34 — numeric citation style | **RE-FLAG-OF-DISCLOSED** (submission-kit) | R1 DP4P-17; l.27, l.901; mechanical at submission |
| Grok N1 — draft header/date | **OPINION/GENRE** (NIT) | R1 precedent; typographic half → DP4P-35 |
| Gemini N2 — "brackets" imprecise | **OPINION/GENRE** (NIT) | detection fraction 0.9465 → 0.9500 across the 0.96/0.98% rows; the crossing is attained at the endpoint, which is why linear interp returns 0.0098 |

### Verified-correct register (R2 additions)
Cohen's κ from both printed confusion matrices (0.3978 and 0.97333); three-class 58.7%; 69.91% on
117,205; all five Table 3 ratios; count ladders 949,584 − 59,515 = 890,069, 694,642 → 145,789 →
145,766 = 31,937 + 113,829, 812,793 = 428 + 6,673 + 408,187 + 397,505, 3,201,160 = 1,592,107 +
1,609,053; the twelve printed injection-recovery rows and both interpolations (0.0098 linear,
0.0095478 logistic); the null array's mean/sd/95th percentile; P5's four clustering-scale CIs and
five-way void family; f_sky 23,633/49,152 = 0.4808 and 24,087/49,152 = 0.49005; the Parquet byte
count and quarantine split. **No arithmetic or transcription error in the measurement layer.**
The §5.1 finding (Popławski supplies no computed amplitude) remains the paper's genuine
contribution, stated at its correct evidential strength; no bounce claim is smuggled in.

### R2-budget note (directive R2)
Second consecutive round. A third round requires an intervening science/scope decision. Satisfied
by either (1) **the monopole resolution** — adopt DP4P-21's settled answer (+2.53% A_p from a
75%-CCW quarantine; no propagation to A_95^obs or the dipole) and disclose it — or (2) **the CL
decision** (DP4P-22: re-run for a genuine 95% inversion, or withdraw the claim). Remaining items
are presentation/venue/packaging; if a verification pass returns only those, rounds stop and P4′
moves to the publication phase under directive P.

### R2 closure confirmation (v4P.0.2 → v4P.0.3, 2026-09-02)
All 21 canonical R2 items (DP4P-21–24, DP4P-25–41, DP4P-42/43) CLOSED in
`pipelines/p4prime_chirality_test/paper/main.tex` v4P.0.3
(SHA-256 `e8b517d22f61ed733dca043ae2b8253eceffd856ffdfc09e65b422c90b3a8200`).
Both R2-budget science decisions taken: (1) monopole disclosure —
$f_{\rm CW}=0.5126562$ on the primary channel stated with the 75.2%-CCW
quarantine cause, alongside both other narrated monopoles, non-propagation
to $A_{95}^{\rm obs}$/dipole stated; (2) CL decision — re-run executed
(`research/bh_universe_dipole/a95_upper_limit_2026_09_02.py`), genuine
95% CL upper limit $A_{95}^{\rm CL}\simeq0.75\%$ computed and reported as
Eq. 2, the prior mislabelled "genuine 95% CL" (null 95th pct) relabelled a
critical value. Full item→edit mapping in
`project-context/SSOT/paper-4p/status.md` §"R2 closure". Per directive
R2's third-round budget note above, a subsequent round on v4P.0.3 is
authorized only as a verification pass on this changed text.

---

## R3 wave (2026-09-02, VERIFICATION PASS) — `ROUND_2026-09-02-P4P-v4P.0.3-EXACTPDF-e8b517d2-R3VERIFY`

PDF sha256 `e8b517d22f61ed733dca043ae2b8253eceffd856ffdfc09e65b422c90b3a8200` (verified), 11 pp.
Legs: Claude INT (minor-revisions, 0 MAJOR / 5 MINOR + 1 NIT), Grok API `grok-4.3` (REJECT, 8 items),
Gemini API `gemini-3.1-pro-preview` (MINOR REVISIONS, 5 items), **Perplexity ABSENT** (401
insufficient_quota — optional leg, recorded absent per skill Rule 4, never as zero-findings).
**0 BLOCKERs across the round.** 19 raw findings → 12 canonical after dedup:
**7 GENUINELY-NEW-REAL (1 MAJOR-by-Rule-8.4, 6 MINOR); 4 RE-FLAG-OF-DISCLOSED; 2 FALSIFIED;
3 OPINION/GENRE.** Part A independently confirmed **21/21 R2 closures real, 0 overstated**;
the Neyman inversion was re-run and reproduced $A_{95}^{\rm CL}=0.7508188\%$ exactly.
No arithmetic, transcription or derivation error found. Truth audit:
`INT_v3/ROUND_2026-09-02-P4P-v4P.0.3-EXACTPDF-e8b517d2-R3VERIFY/P4P_v4P.0.3_R3_truth_audit.md`.

### Canonical items → v4P.0.4 (all SUBSTANTIVE, none requiring new computation)
| ID | Item | Evidence | Closure |
|---|---|---|---|
| DP4P-44 (MINOR) | Monopoles quoted as $f_{\rm CW}-\tfrac12$ (+1.2656% primary) while every other amplitude uses $A_p=2(f-\tfrac12)$; the primary monopole is $A_p=+2.53\%$, $2.6\times$ the 0.98% floor | ll.288–301 vs Fig. 1 caption l.439 and the estimator $A_p=m+\bm a\cdot\hat n_p$ (ll.305–309) | state both conventions in the same sentence |
| DP4P-45 (MINOR) | Data Availability names a `dr8_id` column | l.1000 vs Table 1 l.221 and the pyarrow schema of `apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet` (no `dr8_id`) | l.1000 → `object_id` |
| DP4P-46 (MINOR) | Table 1 typesets `raw_flip_qc_unsafe` as two rows (`raw_flip_` / `qc_unsafe`), misstating the schema | source ll.230–231 | one row, `\allowbreak` |
| DP4P-47 (MINOR) | Cited CL script's docstring claims N_AXES was reduced from 2000; code sets `N_AXES = 2000` and the JSON says no tradeoff (directive Q2) | `a95_upper_limit_2026_09_02.py` ll.32–36 vs l.72 | delete the stale paragraph |
| DP4P-48 (**MAJOR**, disclosure; 3-leg convergent) | Abstract calls $A_{95}^{\rm obs}=0.98\%$ a "95% sensitivity upper limit" and omits $A_{95}^{\rm CL}=0.75\%$; the CL limit sitting below the power floor is unremarked | abstract ll.90–92 vs §3 l.462 "not itself a confidence-level bound" | see CL ruling below |
| DP4P-49 (MINOR) | "DR1 companion" undefined — §2 builds a DR8 catalog; `grep DR1` → only l.599 and the P5 reference title | l.599 | define the DR1 TARGETID cross-match in one clause |
| DP4P-50 (MINOR) | Table 1 caption "release v1.0.244" vs ref [15] "v1.0.274 archived release" reads as a mismatch (both strings individually **correct** — catalog release vs release-paper version; the mismatch premise is FALSIFIED, the ambiguity is real) | l.213 vs l.1106; parquet path `apjs_release_v1.0.244/` | one clarifying parenthetical; renumber nothing |
| DP4P-51 (GENRE, optional) | Table 5 Ratio column uses each row's lower amplitude endpoint, so "2–20×" pairs with "2–33%" | abstract l.100, §5.2 l.771 | optional caption clause |

### CL-vs-floor ruling (DP4P-48) — binding
$A_{95}^{\rm CL}=0.75\%<A_{95}^{\rm obs}=0.98\%$ is **correct and requires no repair**: the
floor is a realization-independent 95%-*detection-power* amplitude, the CL limit is a Neyman
inversion conditioned on $A_{\rm dip}=0.4665\%$, a low draw of a positive-definite estimator
with null mean $0.362\%$. A median expected limit tracks the ~50%-power scale ($\sim0.6$–$0.7\%$
from the paper's own curve), so $0.75\%$ is ordinary, not pathological; no empty interval.
**Wording correction:** the one-sided Neyman construction does **not** undercover — it has exact
frequentist coverage; what it lacks is a *sensitivity* interpretation (a downward fluctuation can
make a classical limit stronger than the experiment's reach — the standard motivation for
unified/$\mathrm{CL_s}$). **Headline: keep the floor.** Grok E1's "make the Neyman limit the
primary bound" is REJECTED — §5's confrontation is a sensitivity argument, and headlining the
tighter fluctuation-dependent limit would strengthen the exclusion on a lucky draw (directive-F
self-favoring). Gemini E1's terminology half is ACCEPTED: the abstract drops "upper limit" for
$A_{95}^{\rm obs}$, calls it a detection-power sensitivity floor, and reports $A_{95}^{\rm CL}$
alongside with the "we confront with the more conservative floor" clause.

### FALSIFIED / RE-FLAG / OPINION — do not re-open without new evidence
| Finding | Verdict | Source-cited basis |
|---|---|---|
| Grok E2 — "largest" unqualified; supply $N_{\rm eff}$ comparison | **RE-FLAG-OF-DISCLOSED** (+ demand OUT-OF-SCOPE) | abstract ll.106–110 concedes Shamir 2022 "which exceeds it"; "largest single catalog" scoped at l.876 — the executed DP4P-01 closure |
| Grok E3 — §5 closure is an author-supplied assumption; relocate | **RE-FLAG-OF-DISCLOSED** (relocation OPINION) | ll.310–313 italic "Eq. 3 is *not* derived from Popławski's papers"; abstract l.96–97; R1 Grok E4 precedent |
| Grok M1 — programmatic first-person voice | **OPINION/GENRE** | every hit (ll.147/160/162/855/916) is inside the required bounce-scope disclaimer (directive R6); deleting it would weaken honest scoping |
| Grok M2 — end-to-end purity for the 8.47 M parent / 887k support | **RE-FLAG-OF-DISCLOSED-IN-SOURCE** / OUT-OF-SCOPE | Table 2 + P4 l.563; the resolved curve is recorded in P4 as an uncomputed extension; no external truth set exists at 8.47 M |
| Grok M3 — no "not directly comparable" qualifier | **FALSIFIED** | ll.581–588 verbatim "a **distinct statistic** … neither supersedes the other"; ll.396–399 names support/estimator/null |
| Gemini E3 — Table 4 caption "supersedes" is version-history prose | **RE-FLAG-OF-DISCLOSED** | ll.363–371 is a methodological supersession (circular-RA Pearson → $Y_{\ell m}$, $|z|\le1.25$) and is the executed DP4P-27 closure |
| Gemini N1 — "in- jects" typo p. 3 | **FALSIFIED** | l.305 has no hyphen; `pdftotext -layout | grep injects` → no match, i.e. ordinary justified-line hyphenation (skill Rule 7) |
| Grok N1 — draft header / version strings | **OPINION/GENRE** (packaging) | skill Rule 3; R1/R2 precedent (DP4P-35); mechanical at submission |

### R3 convergence statement (directive R2)
R3 was authorized only as a verification pass on changed text and behaved as one: 21/21 R2
closures verified real, the CL re-run byte-reproduced, **zero** genuinely-new findings touching a
number, derivation, selection or scope. All remaining items are presentation/terminology/
provenance/script-documentation. Directive R2's stopping rule is satisfied literally:
**rounds stop after v4P.0.4** — no further review round on P4′ is authorized. Once the v4P.0.4
bundle verifies (directive-G hygiene: version+date bump, 0 undef refs, `/latex-audit`,
byte-identical mirrors, Convex `paperVersions:bump`, three-way md5), P4′ moves to the publication
phase under directive P at readiness **95**, the final 5 reserved for Houston's explicit
per-paper sign-off; venue/submission/endorsement tracked separately and never subtracted.

## Exact-v4P.0.7 confirmation board (2026-09-18, campaign lane L4) — v4P.0.8 closure

R3's "rounds stop" statement applied to the v4P.0.4 content it reviewed. It did not
cover the three disclosure results added in v4P.0.5–v4P.0.7 (pixel-level calibration,
full-parent selection behavior, structure cross-correlations, row-16(iv-b) BGS
environment) — that content had never been independently reviewed. This board ran
Grok API + Gemini API + a Claude opus INT sub-agent against the exact v4P.0.7 PDF,
scoped to that new content (with a fresh full read of the rest of the paper). Full
audit: `project-context/peer-reviews/INT_v3/ROUND_2026-09-18-P4P-v4P.0.7-EXACTPDF-7eb1f99e-CONFIRM/P4P_v4P.0.7_CONFIRM_truth_audit.md`.

**7 GENUINELY-NEW-REAL MAJOR, all independently source-verified and closed in v4P.0.8:**
CONFIRM-1 (full-parent QC-cut attribution was inverted vs. source), CONFIRM-2 (primary
887,472-channel's own drop-one-leg fits reach z>4 above A₉₅ᵒᵇˢ, omitted from disclosure),
CONFIRM-3 (new BGS/structure channels silently ran on the pre-QC 949,584 sample, not the
887,472 primary channel, mislabeled), CONFIRM-4 (void-catalog-availability appendix
sentence contradicted Sec. 4's own use of DESIVAST), CONFIRM-5 (Shamir-axis-untested
justification misattributed a scope limitation of this manuscript to the cited
literature), CONFIRM-6 (two of four Data-Availability manifest pointers resolved to the
wrong experiment, one to a superseded "inconclusive" pilot), CONFIRM-7 (new pixel-level
calibration measurement implies an observed-to-physical transfer ~10× smaller than the
illustrative g=0.398 bridge the Sec. 5 exclusion carries; this tension is now disclosed
explicitly in-paper, not resolved by new derivation — see the truth audit for the exact
arithmetic and why it is not adopted as a repair).

12 MINOR items also closed (wording/disclosure fixes; see truth audit for the full list).
2 items — Claude MIN-9 (low-severity, no in-text contradiction) and Gemini E4/M2 (Table 7
effect-size + full-15-statistic expansion) — are OPEN, explicitly deferred with reason
(not silently dropped); the latter is a real, bounded table-construction task using data
already on disk, not a correctness defect.

### FALSIFIED / RE-FLAG / OPINION this board — do not re-open without new evidence
| Finding | Verdict | Source-cited basis |
|---|---|---|
| Grok E1 — remove DRAFT VERSION / dated header strings | **OPINION/GENRE** | precedent line 122 (R2 Grok N1); AASTeX default, removed at actual submission |
| Grok E2/E3 — internal `\artifact{}` script paths unacceptable in submission; no independent verification of 0.98%/0.75% | **OPINION/GENRE** | directive Q2 mandatory reproducibility manifests; scripts already `\artifact{}`-linked in-paper |
| Grok E4/M1 — literature-ratio Table 5 asserts unquantified factors | **RE-FLAG-OF-DISCLOSED** | closed R1 DP4P-10 (line 90-95), reconfirmed R2 (line 213) |
| Grok M2 — z_mom/FSC juxtaposed without "not comparable" caveat | **FALSIFIED** | `main.tex` states "uses a different support" at two separate mentions, pre-edit |
| Grok M3 — Fig. 1 "no coherent structure" lacks quantitative ℓ>1 test | **OPINION/GENRE** | caption already hedges "visually apparent"; quantitative ℓ=1 tests exist elsewhere (Sec. 2.3) |
| Gemini E2 — Table 8 z-scores "irreconcilable" with $f_{\rm CW}$/naive-Gaussian p | **FALSIFIED** | every Table 8 value byte-matches `ROW16IVB` §2; z-values come from the paper's own disclosed non-Gaussian permutation null (MIN-5), not a naive binomial vs. pooled mean |
| Gemini E3 — unarchived Ref. [16] URL for load-bearing material | **RE-FLAG-OF-DISCLOSED** | closed R1 DP4P-07 (line 68-74), reconfirmed (line 215) |
| Gemini M4 (pass-2) — "Largest Test" title contradicted by Shamir 2022's 1.3M sample | **RE-FLAG-OF-DISCLOSED** | closed R1 DP4P-01: abstract already discloses the Shamir-2022 exception in the same sentence |
| Gemini N3 — space in HuggingFace URL | **FALSIFIED** | `main.tex` l.1209 (pre-edit) has no space; PDF-render line-wrap artifact of the reviewer's native-PDF read |
| Gemini N1/N2 — Fig. 3 Cluster-bin significance claim; missing effect size, sample-purity ladder | **NOT DISPOSITIONED, carried forward** | pre-v4P.0.5 content, outside this board's charge (the v4P.0.5–v4P.0.7 additions); flag for the next full R-round rather than disposition without full-paper context |

### v4P.0.8 hygiene
`\paperVersion` v4P.0.7→v4P.0.8, `\paperTimestamp` Sept 5→Sept 18 2026; 4-pass compile,
0 undef refs, pre-existing 5.88pt hbox only; 13→14 pages; sha256
`e8f1969e415777622561dde0f21a8ac7d6398c3b2ef55f69200ba50a89d91cd2`, md5
`b2399780320a50542279c35410b6b545`; four-way byte-identical mirror verified;
`reproducibility/manifests/programs/galaxy-chirality.json` gained
`row16-image-level-injection-n20k` (previously committed, unregistered).

## Exact-v4P.0.8 re-verification board (2026-09-19, campaign lane L4b) — v4P.0.9 closure

Directive R2 permits exactly one consecutive verification round after the 2026-09-18
confirmation board without an intervening science/scope decision. This is that round
(lane `bb-L4b-p4p-reverify`), independently re-reviewing the v4P.0.7→v4P.0.8 closures
themselves. **No third consecutive round on this content is authorized.** Full audit:
`project-context/peer-reviews/INT_v3/ROUND_2026-09-19-P4P-v4P.0.8-EXACTPDF-e8f1969e-REVERIFY/P4P_v4P.0.8_REVERIFY_truth_audit.md`.

**6 GENUINELY-NEW-REAL MAJOR (Claude opus leg, verdict-blind, cold read — not shown
the prior closure list or this dispositions file before writing its report), all
independently re-derived by the orchestrator from underlying committed artifacts and
closed in v4P.0.9:** RVFY-A1 (pixel-injection baseline compared against the wrong
monopole sample, catalog-wide vs. HC-selected, and the wrong amplitude convention),
RVFY-A2 ("near-antipodal axis" is quantitatively false — max pairwise separation
among the four QC-sweep axes is 119.9°, not ~180°; the closest pair, 19.3° apart, was
omitted: the primary_hc-relaxed excess axis sits next to the primary channel's own
axis), RVFY-A3/A4 (the two most consequential §A.1 disclosures — the pixel-transfer
tension and the primary channel's own leg-instability — had zero forward reference
from the Abstract, §3, §5, §6, or §7; fixed with four targeted pointer insertions,
Abstract deliberately left untouched at its 250-word ApJS cap), RVFY-A5 ("tercile"
split is actually a 20/60/20 quintile split, contradicted by the paper's own Table 8
N's and the committed script's own docstring), RVFY-A6 (the "0.79 correlation"
justifying an FSC/monopole identification is misattributed — the matrix shows 0.79 is
real-space↔$C_1^{\rm master}$, not monopole-related, and the paper's own next
sentence says the monopole is nearly uncorrelated with the other three).

4 MINOR also closed with real, source-verified edits: RVFY-B1 ("15 of 17" structure
statistics does not reconcile, 17−1=16), RVFY-B4 (C3 leg-exceedance enumeration
incomplete: 5 of 6, not 2 of 6, single-leg fits exceed $A_{95}^{\rm obs}$), RVFY-B5
(Shamir 2025 low-end-amplitude convention inconsistency), RVFY-B6 (Data Availability
wrongly listed T-Web as unreproduced when §4 reproduces it), RVFY-B7 (0.1<z<0.4 BGS
window misattributed to the 231,549-spiral parent rather than the cut that produces
121,417 from it).

6 Claude-leg MINORs (B2, B3, B8, B9, B10, B11) and 6 NITs (C1, C2, C4–C7) explicitly
deferred with reason — real but lower-severity items requiring either a considered
rewrite (B2, B8, B10, B11) or cosmetic-only fixes (B3, B9, C1–C7) — not silently
dropped; see the truth audit for the full per-item reason. NIT C3 (undefined "C3"
jargon) was incidentally resolved by the B4 rewrite.

### FALSIFIED / RE-FLAG / OPINION this board — do not re-open without new evidence
| Finding | Verdict | Source-cited basis |
|---|---|---|
| Grok E1/E4 — g-bridge factor unestablished (abstract/Table 5) | **RE-FLAG-OF-DISCLOSED** | precedent DP4P-10, DP4P-24 |
| Grok E2 — Poplawski papers only qualitative, $A_{\rm pred}\approx\eta$ author-introduced | **RE-FLAG-OF-DISCLOSED** | main.tex l.93, 734, 827 already state this; Eq. 4 is a named Assumption |
| Grok E3 — $z_{\rm mom}$/FSC juxtaposed without "not comparable" | **FALSIFIED** | precedent (twice before); still states "different support" at both mentions |
| Grok M1 — manuscript overlength | **OPINION/GENRE** | subjective page-count preference |
| Grok M2 — DESIVAST test is post-hoc | **FALSIFIED** | main.tex §4 states this **verbatim** already |
| Grok M3 — "largest test" vs. Shamir (2022)'s larger $N$ | **RE-FLAG-OF-DISCLOSED** | precedent DP4P-01 |
| Grok M4 — released classifier's $\kappa=0.40$ disclosure | **RE-FLAG-OF-DISCLOSED** | precedent DP4P-04 |
| Grok M5 — Fig. 1 "no coherent structure" | **OPINION/GENRE** | precedent (Grok M3, prior round) |
| Grok m1/m2 — Table 1 column truncated / Neyman description incomplete | **FALSIFIED** | both already complete in main.tex, pre-edit |
| Grok m3 — "research program's own bounce papers" self-promotional | **OPINION/GENRE** | factual cross-reference, no superlative claim |
| Grok NITs — future date; one-sided/two-sided labeling; Table 8 null repeat | **FALSIFIED / OPINION** | 2026-09-18 is today, not future; every occurrence already labels its tail; caption cross-references adjacent text |
| Gemini M1 — three URLs contain spaces | **FALSIFIED** | no spaces in `main.tex` source at any of the three lines; PDF-render column-wrap artifact, same pattern as prior-round Gemini N3 |
| Gemini N1 — internal version string in journal date line | **OPINION/GENRE** | standard practice across this campaign's papers |

### v4P.0.9 hygiene
`\paperVersion` v4P.0.8→v4P.0.9, `\paperTimestamp` Sept 18→Sept 19 2026;
4-pass compile, 0 undef refs, pre-existing 5.88pt hbox only; 14→14 pages;
sha256 `0224d3b8e85c8a26fd8ed8e6a715ff571e3d6483cce4eadfbdf87acafd17a5bf`, md5
`e31da2ee9cc57fbf0344b8d5c3b9a330`; four-way byte-identical mirror verified; arXiv
tarball rebuilt and standalone-compile-verified.

## v4P.0.9 → v4P.0.10 — row-16(ii-b) science propagation (2026-09-21, lane `bb-L4d-p4p-row16-propagate`)

Not a review round — no board run, nothing here is a reviewer finding. This
is a **science-content update**: lanes `bb-LS-ledger16` / `bb-LS5-row16-finalize`
measured a direct, assumption-light bound on the observed-to-physical
transfer function ($D \le 0.717 \pm 0.005$, released `primary_hc`
preprocessing, from a PA-restoring handedness-reversal test) and left an
exact propagation note
(`pipelines/p4prime_chirality_test/row16_pa_parity_transfer/PROPAGATION_NOTE.md`,
sentences P-1..P-5d) rather than editing the paper themselves (per the
lane split, only lane L4/its descendants may write `main.tex`). This lane
applied every printable sentence in that note verbatim, and additionally
made the withdrawn claim's three other in-paper mentions (§2.3
forward-reference, Discussion, Conclusions) consistent with it, reusing only
numbers already given in the note (no new derivation, per
`/never-fabricate-derivation`).

**Superseded (withdrawn, not "reviewed away"):** the naive-identity
`+0.434`/`47σ` comparison, the `0.038` response ratio, the `≈26%`
propagated floor, and the "unresolved discrepancy"/"order of magnitude
tension" framing throughout — all four were comparisons between statistics
that do not share a normalization (P-1/P-2/P-3 of the propagation note), not
findings from any external reviewer.

**Adopted (new, measured):** $\bar\epsilon = 0.754 \pm 0.005$ (PA-restoring
reversal, `primary_hc`, released preprocessing, $51\sigma$ below unity);
dilution bound $D \le 0.717 \pm 0.005$; $A_{95}^{\rm phys} \ge 1.37\%$,
consistent with the illustrative $g=0.398$ bridge (source: `s1_pa_transfer_results.json`,
`s5b_nocrop_dilution.json`, `posthoc_nocrop_eps.json`, per the note's P-5d
citation table).

**Not yet done:** LS6's second propagation note
(`row16_tta_2026_09_21/PROPAGATION_NOTE.md`) did not exist when this lane
ran (checked, absent) — a future lane should check for and apply it before
the next review board. Directive R2's round budget is refreshed by this
science decision, but no board was run in this lane (out of scope; reserved
for whichever lane runs the next one).

### v4P.0.10 hygiene
`\paperVersion` v4P.0.9→v4P.0.10, `\paperTimestamp` Sept 19→Sept 21 2026;
4-pass compile (inline `thebibliography`, no `.bbl` dependency), 0 undef
refs, pre-existing 5.88pt hbox only (unchanged); 14→15 pages; sha256
`054b63f8a73902000a0e703da62229ee887f2fc77b0cc027533c2309985f9310`, md5
`d2d017145530e641ea491c4f5f0909de`; three-way byte-identical mirror verified
(source, `site/public/papers/`, `public/papers/`); arXiv tarball rebuilt
and standalone-compile-verified (0 undef refs on a clean extract).

## v4P.0.10 → v4P.0.11 — HOLD CORRECTION: out-of-domain dilution bound withdrawn (2026-09-22, lane `bb-L4e-p4p-hold-correction`)

Not a review round — a correction of a defect introduced by the immediately
preceding lane. `bb-LS6-row16-tta` (2026-09-21/22) found that the
`D ≤ 0.717 ± 0.005` / `A₉₅^phys ≥ 1.37%` bound v4P.0.10 had just printed
(propagated from `bb-L4d-p4p-row16-propagate`) was measured on **out-of-domain
images**: a pre-registered positive control required the released
preprocessing, run at the identity transform, to reproduce the released
catalog's own labels on ≥99.9% of galaxies; on the images that measurement
used it reproduces them for only 43.9% of 19,800 galaxies (42.4%/44.7% on two
further draws), while an identical check against the lane's own committed
forward passes on the same images agrees at 99.99% — proving the classifier
code and preprocessing were correct and the images were Legacy Survey display
cutouts (39.3″, upsampled to 224 px) rather than the `Smith42/galaxies` images
the released classifier ran inference on (224×224 px, 58.7″ native DR8,
`main.tex:171`). An out-of-domain instability bounds an in-domain one in
neither direction.

**DISP-HOLD-01 — dilution bound / physical-parity floor: WITHDRAWN, ON HOLD
(not a reviewer finding; a self-caught measurement-domain defect).** Removed
from every location it appeared (7 prose instances + 2 table rows) and
replaced with a named hold citing the exact positive-control numbers above;
the hold is lifted by re-running the identical PA-restoring test on the
correct, pinned `Smith42/galaxies` images (bounded, disk-only, no GPU). The
Q-1a architectural paragraph (why the transfer is not unity by construction)
is retained verbatim in Assumption 2 — that argument carries no image-domain
dependence and is unaffected.

**Unaffected (confirmed, re-verified this lane):** row-16(ii-b) items P-1–P-4
(pixel-injection error-bar correction, withdrawal of the invalid
`47σ`/`2.9σ`/`0.038`/`≈26%` comparisons, retirement of the mirror-injection
extension) — re-analyses of committed label-level quantities and of the exact
identity `eq_cw(MI)=eq_ccw(I)`, which holds for any image whatsoever. No
image enters them; v4P.0.10's text for these stands unchanged in v4P.0.11.

**DISP-HOLD-02 — sky-dependence systematic: ADOPTED (new disclosure, not a
reviewer finding).** Printed exactly as `bb-LS6-row16-tta` propagation note
item Q-3 gives it: an 11σ sky dipole in the classifier's parity-transfer
efficiency (`a_δ = 0.090 ± 0.010`, permutation-null `p ≤ 0.001`) projected
through the paper's own exact estimator imprints a spurious `0.23%` dipole on
the strict-887,472 support — 23% of the quoted `A₉₅ = 0.98%` limit, above the
note's pre-registered 10%-of-`A₉₅` disclosure threshold. Replaces the
superseded `0.036 ± 0.005` hemisphere-difference sentence (itself measured on
the same out-of-domain images and therefore carrying the same defect).

No new numbers introduced anywhere outside the two propagation notes'
committed JSON (`/never-fabricate-derivation`).

### v4P.0.11 hygiene
`\paperVersion` v4P.0.10→v4P.0.11, `\paperTimestamp` Sept 21→Sept 22 2026;
4-pass compile, 0 undef refs, pre-existing 5.88pt hbox only (unchanged);
15→15 pages (unchanged); sha256
`9f3822a2f1c97184c7d4beccd14294739816228b53ef8e59af02e6bc20b1528a`, md5
`c5944b14d0987d14bbe0d2a61953b1f6`; three-way byte-identical mirror verified
(source, `site/public/papers/`, `public/papers/` — Convex arm UNAVAILABLE,
spending limit, mutation queued in `CONVEX_BACKFILL_QUEUE_2026-09-21.md`);
arXiv tarball rebuilt and standalone-compile-verified (0 undef refs, 15 pp,
byte-identical size on a clean extract).

## v4P.0.11 → v4P.0.12 — HOLD LIFTED: in-domain dilution bound adopted (2026-09-22, lane `bb-L4f-p4p-indomain`)

Not a review round — the named lift of the DISP-HOLD-01 hold, by the exact
test that hold specified. Lane `bb-LS10-indomain-d180` (2026-09-22) re-ran the
identical PA-restoring rotation test directly on the classifier's own
`Smith42/galaxies` imaging (the pinned revision documented at
`main.tex:171-173`): $N=40{,}000$ galaxies streamed by HTTP range read (zero
image bytes to disk), 320,000 forward passes, local MPS, 47 min, \$0. Two
gates passed before the measurement was trusted: (1) catalogue-scale in-domain
agreement is 99.936% over all 8,474,531 galaxies and 100.000% over the
949,584 `primary_hc` galaxies (`c1_e2e_catalogue_agreement.json`), against
43.9% on the withdrawn out-of-domain viewer cutouts; (2) the domain gap is a
measured $3.41\times$ difference in angular field — the in-domain cutouts are
$512\times512$ px at $0.262''$/px (a $134.1''$ field, median pixel
correlation 0.992 at that scale, $\le 0.25$ at every other grid point tested;
`posthoc_pixel_scale.json`) against the withdrawn measurement's $39.3''$
viewer-cutout field.

**DISP-HOLD-01 — dilution bound / physical-parity floor: CLOSED, adopted
in-domain.** The withdrawn out-of-domain bound (`D ≤ 0.7166 ± 0.0047` /
`D ≤ 0.717 ± 0.005` cross-tabulation depending on selection, `A₉₅^phys ≥
1.37%`) is superseded, not averaged with, the in-domain measurement:
`primary_hc` (N=4,579) `D ≤ 0.5998 ± 0.0065` (`61σ` below unity;
`θ=180°`-only, assumption-free: `D ≤ 0.6599 ± 0.0075`), all spirals
(N=15,219) `D ≤ 0.5237 ± 0.0038`; `A₉₅^phys ≥ 1.63%` (`primary_hc`),
`≥ 1.87%` (all spirals). The in-domain classifier is **less** rotation-stable
than the withdrawn measurement suggested — `θ=180°` self-disagreement rose
from `21.1%` to `34.0%` — so the correction moves the physical-parity floor
upward, in the conservative direction, exactly as
`row16_indomain_d180_2026_09_22/PROPAGATION_NOTE.md` item R-1 characterizes
it. Applied verbatim per items R-1/R-1a/R-1b: Assumption 2 of §`sec:bh`, the
pre-`sec:bh` forward reference, the black-hole-section closing paragraph, the
Conclusions, the `sec:robustness_disclosure` narrative, and `tab:pixel_calib`
(9 prose locations + the table) all now state the in-domain result and record
the withdrawal explicitly (never a silent substitution) — a reader of
v4P.0.11 can see exactly what changed and why. Per R-3, the `$\bar\epsilon$`
(PA-restoring transfer efficiency) and TTA rotation-recovery-fraction clauses
are **cut**, not re-quoted, since they remain out-of-domain and the in-domain
instability being larger makes an out-of-domain recovery estimate optimistic
in the wrong direction.

**DISP-HOLD-02 — sky-dependence systematic: unchanged, still OUT-OF-DOMAIN.**
Not re-measured by this lane. The `0.090 ± 0.010` sky-dipole amplitude and its
propagated `0.23%` spurious-dipole figure remain measured on the same
withdrawn out-of-domain viewer cutouts; `main.tex` now says so explicitly
(new sentence: "This amplitude was measured on the same out-of-domain viewer
cutouts as the withdrawn dilution bound above and has not been re-measured on
the classifier's own imaging"). Do not read DISP-HOLD-01's closure as also
closing DISP-HOLD-02 — the two are independent measurements and only the
first was re-run in-domain.

**R-2 documentation fix (applied):** `main.tex:171-173` previously stated the
`Smith42/galaxies` parent cutouts are $224\times224$~px; they are
$512\times512$~px at $0.262''$/pixel (a $134''$ field), resampled to the
$224\times224$ network input. The same stale $224\times224$/`58.7''`
description was repeated at two further prose locations (Assumption 2,
`sec:robustness_disclosure`) and corrected in the same bundle. Verified: `grep
-n 224 main.tex` now returns only the one correct resize-target sentence plus
an unrelated journal-volume-number citation.

**No new numbers introduced anywhere outside `row16_indomain_d180_2026_09_22`'s
committed JSON** (`/never-fabricate-derivation`).

### v4P.0.12 hygiene
`\paperVersion` v4P.0.11→v4P.0.12, `\paperTimestamp` unchanged (September 22,
2026 — same day); 4-pass compile, 0 undef refs, pre-existing 5.88pt hbox only
(unchanged); 15→16 pages (grew by one page from the added in-domain content);
sha256 `025bec74e3b947e760c398f0eaaf5a82d6569207ed2769d9d355581906614768`, md5
`afff6bec7b78bac271104d89a3582bf9`; three-way byte-identical mirror verified
(source, `site/public/papers/`, `public/papers/` — Convex arm still
UNAVAILABLE, spending limit; mutation queued in
`CONVEX_BACKFILL_QUEUE_2026-09-21.md`); arXiv tarball rebuilt
(`paper4prime_chirality_test_arxiv_v4P.0.12.tar.gz`, sha256
`8e7fff95a9cc935fff37dd6f09049c220da324d78783e82363096c3e09cfdea5`) and
standalone-compile-verified on a clean extract (0 undef refs, 16 pp,
byte-identical 1,132,763 bytes to the source compile). New reproducibility
manifest registered: `reproducibility/manifests/experiments/row16-indomain-d180.json`,
linked into `reproducibility/manifests/programs/galaxy-chirality.json`.

**Sign-off hold status:** the co-director's SIGN-OFF HOLD on P4P, which
v4P.0.11 left standing on "the in-domain re-measurement that would let the
dilution bound itself be reinstated has not been done," is **RELEASABLE**:
that re-measurement is now done, verified against committed JSON, propagated
without a silent substitution, and the full directive-G bundle (compile,
audit, mirror, links, tarball) verifies clean except for the Convex arm
(unavailable, spending limit — queued). The one item still open is unchanged
from v4P.0.11: a fresh INT confirmation board on the exact v4P.0.12 PDF has
not been run (directive R2 budget already refreshed twice by the v4P.0.10/11
corrections). That is a review-convergence item, not a correctness defect,
and does not by itself justify continuing the hold — recommend RELEASE, with
the INT board scheduled as the next lane's task.
