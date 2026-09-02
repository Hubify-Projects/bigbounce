# P4′ v4P.0.1 — R1 truth audit (Opus, verdict-first, source-cited)

- **Round:** `ROUND_2026-09-02-P4P-v4P.0.1-EXACTPDF-a9cc2618-R1`
- **Manuscript:** `pipelines/p4prime_chirality_test/paper/main.tex` → `main.pdf`
- **sha256 (verified this session):** `a9cc26183c631ba88d021edc4b46f35a295832a9b1ceb7879aacf8d38253099f` — matches the round label and every leg header. 6 pages, AASTeX 7.0.2 twocolumn.
- **Auditor:** independent Opus truth-audit leg. Skeptical in both directions; every verdict below is decided from the on-disk source, never from a leg's verdict word (skill Rules 6/7/8).
- **Date:** 2026-09-02

## Legs in this round

| Leg | Model | Verdict word (diagnostic only) | Items in raw | Items dispositioned | Gap |
|---|---|---|---|---|---|
| Claude INT (`P4P_claude_r1_leg.md`) | claude-opus-5[1m] | major-revisions | 9 MAJOR + 11 MINOR = 20 | 20 | no |
| Grok API (`..._P4P_Grok_brutal.md`) | grok-4.3 | REJECT | 4 ESSENTIAL + 3 MAJOR + 3 MINOR/NIT = 10 | 10 | no |
| Gemini API (`..._P4P_Gemini_cosmology.md`) | gemini-3.1-pro-preview | REJECT | 3 ESSENTIAL + 2 MAJOR + 1 NIT = 6 | 6 | no |
| Perplexity (`..._P4P_Perplexity_citations.md`) | — | **ABSENT** | — | — | — |

**Perplexity leg = ABSENT, not clean** (skill Rule 4). `AuthenticationError 401 … insufficient_quota`; the file contains a `Reviewer call FAILED` traceback and a `[FALLBACK from sonar-pro]` tag. Optional leg; it does not degrade the round for the three active legs (directive M-AMENDED), but it may not be counted as a zero-finding review.

**0 BLOCKER-tagged items in any leg** (mechanical `grep -nE '\[(BLOCKER|MAJOR|MINOR)\]'` plus manual read of the ESSENTIAL/MAJOR/MINOR/NIT headings the API legs actually used — neither API leg uses bracket tags, so severity was read from the heading label).

## Evidence base actually inspected

- `main.tex` (569 lines), `main.log` (0 overfull/underfull, 0 undefined refs), `main.pdf` sha-verified.
- Rendered pages 2 and 3 at **300 DPI** (`pdftoppm -r 300`) — used to settle Fig. 1 and Fig. 2 disputes; `pdftotext -layout` for the reference list.
- P4 source: `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.274).
- P5 source: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.147).
- `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` + `outputs/poplawski_dipole_exclusion_2026_09_02.json`.
- md5 of `fig_sky_map.png` / `fig_p5_cw_by_env_bar.png` across all three trees.
- Live HTTP checks: GitHub repo, Zenodo DOI, HuggingFace mirror.
- Prior dispositions `DISPOSITIONS/P4.md`, `P5.md` (P4′ is a new manuscript; no prior P4′ fingerprints existed).

## Ten specific questions the round was asked to settle

| # | Question | Evidence | Answer |
|---|---|---|---|
| a | Fig. 1 provenance | `md5 = 7156f1af3c2ea3e6a0b7e47c6899802d` identical across `p4prime_chirality_test/paper/fig_sky_map.png`, `p2_chirality/fig_sky_map.png`, `p2_chirality/figs/fig_sky_map.png`. 300-DPI render of p. 2 shows baked-in title **"Galaxy Chirality Asymmetry Map (8.47M galaxies, equivariant)"** and colorbar $(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})$, range ±0.08. P4 caption (`chirality_catalog_paper.tex` l.1234–1244): "Equivariant (Catalog C) chirality asymmetry map of the 8.47 M-galaxy catalog … NSIDE=64 … $f_{\rm sky}=0.49005$ in the FSC support." | It is P4's **full-catalog FSC** map, not the 887,472-row HC supported-pixel sample the P4′ caption claims (tex l.202–205). Caption also says "CW-fraction" where the plotted quantity is the asymmetry $A_p = 2(f_{\rm CW}-\tfrac12)$. **Both defects real.** |
| b | κ=0.97 vs κ=0.40 | P4 l.1810: "*This $\kappa=0.9733$ figure is neither comparable to, nor a replacement for, the $\kappa=0.40$ / $69.91\%$ figure above*"; the 0.9733 is the **regenerable retrain checkpoint** on 3,000 confident held-out GZ1 spirals. P4 l.1054: the retrain "does *not* alter the released Catalog C labels, which remain the historical production outputs". P4 l.1807: released classifier's full GZ1 cross-match ($N=117{,}205$) gives **69.91% agreement, $\kappa=0.40$**. | The **released labels** are characterised by κ=0.40. P4′ l.179–181 quotes only κ=0.97, and it is the manuscript's only classifier-quality number. **Real.** |
| c | Sample-size arithmetic | $887{,}472/1{,}300{,}000 = 0.68$; $8{,}474{,}531/1{,}300{,}000 = 6.52$; $887{,}472/263 = 3{,}374$. Table 1 (tex l.348) lists Shamir 2022 at $N=1{,}300{,}000$. | The "6–3,400×" range (tex l.98, l.332) is produced by **two different numerators**. Against the stated denominator (supported-pixel sample) Shamir 2022 is *larger*, ratio 0.68. **Real.** |
| d | "More than an order of magnitude" | Table 1 Ratio column: 7.1, 5.1, 2.0, 2.0, 20.4 — four of five below 10. §6 (tex l.417) says "**2–20× tighter**". Abstract (l.96–98) and §5.3 (l.359) say "more than an order of magnitude". Abstract quotes literature as "~7–33%", dropping Table 1's 2–4% rows. | **Real.** The paper contradicts its own table and its own Discussion, in the abstract, §5.3 and Conclusions. |
| e | 95% CI arithmetic | P5 committed (`p5_desi_chirality.tex` l.1004–1006): $\Delta=+0.00145442$, SE $=0.00331502$, CI $[-0.00504290,+0.00795174]$. Recomputing $0.00145442 \pm 1.959964\times0.00331502 = [-0.00504302,+0.00795186]$ — implied multiplier 1.95996 (exact normal 0.975 quantile) to 6 s.f. P4′ prints $[-0.00504,+0.00795]$: correct 3-s.f. rounding. | Gemini re-derived from the *rounded* SE and got a $2\times10^{-5}$ difference. **FALSIFIED.** |
| f | Are [15]/[16] private paths? | `curl` anonymous: `https://github.com/Hubify-Projects/bigbounce` → **HTTP 200**; the `/blob/main/pipelines/p2_chirality/chirality_catalog_paper.tex` URL → **HTTP 200**. The `\artifact`/`\href` targets resolve. | The repository is **public** — "private repository" (Claude MAJOR-7, Gemini E1) is **FALSIFIED**. The real defect survives at full strength: [15]/[16] are working-tree `.tex` sources with **no journal, no arXiv id, no DOI, no publication status**, and every substantive deferral points at them. In print the reference renders as a bare path (`pipelines/p2 chirality/chirality catalog paper.tex`). Additionally [15] renders "**v4P.0.1** archived release" — a `\paperVersion{}` macro bug at tex l.554 stamping *this* manuscript's version onto the P4 reference. [14] (DESIVAST) carries no authors, arXiv id, DOI or URL. |
| g | Internal path in §1 | Rendered p. 2, lines 63–64: "(see project-context/PORTFOLIO_DECISION_2026-09-02.md, Track C1 Addendum)"; source tex l.140–141. Used as justification that the catalog "is an on-vision test … rather than a detached data product". | **Real.** A governance document cannot carry a manuscript's scientific motivation. |
| h | Does Popławski give any amplitude? | Exclusion script `finding` field (verbatim): arXiv:1910.10819 "states only that 'galaxies tend to align their axes of rotation with the preferred axis…' — a qualitative alignment tendency … not a derived dipole amplitude, alignment fraction, or timescale. The mechanism papers (1007.0587, 1111.4595, **1410.3881**) supply the torsion-repulsion bounce itself but likewise contain no galaxy-spin observable." `quantitative_amplitude_predicted: false` in the committed JSON. | **The paper's reading is correct and is the manuscript's genuine contribution.** No external fetch was needed to overturn it; the script's own note already covers 1410.3881 (= ApJ 832, 96) as a mechanism paper with no galaxy-spin observable, and the manuscript states the limitation of its own closure in italics (tex l.310–313). Grok E4 asks for exactly the rephrasing the paper already contains. |
| i | Mask robustness / covariance on the dipole fit | P4 tex l.179–187: the fourth channel is the **NaMaster MASTER-decoupled $\ell=1$ power** $C_1^{\rm master}$ (mode-coupling-matrix inverse, fixed canonical effective mask); "covariance now NaMaster-complete". P4 l.267: shared NSIDE=8 superpixel block bootstrap, $N=2000$, seed 42. 72 mask-related lines in P4. | The analysis **exists in P4** and is simply not carried into P4′. Grok M1 is therefore not a missing-analysis defect but an omitted-material defect — it folds into the self-containedness item, at MAJOR. |
| j | T-Web vs VoidFinder consistency | P5 l.1785–1806: three void definitions spanning two algorithmic families (VoidFinder, V2-REVOLVER, V2-VIDE) with the contrast reported for each (0.44 pp V2-REVOLVER sphere etc.); l.1010 contrasts the VoidFinder any-hole sample against the T-Web; l.2020 gives the clustering-robustness ladder (NSIDE 2/4/8 + 3,750 nearest-MAXIMALS 3-D clusters, point estimate $+0.00145442$ throughout, all intervals containing zero). | **Present in P5, omitted from P4′.** Same disposition as (i): folds into self-containedness at MAJOR. |

## Per-finding table

Severity column = severity **I** assign after verification.

### Leg 1 — Claude INT (20 findings)

| # | Claim | Cited location | Verified on disk | Verdict | Sev. | Closure instruction |
|---|---|---|---|---|---|---|
| C-1 | "6 to 3,400× smaller" is arithmetically false | tex l.98, l.332, l.414–415 | See (c). Two numerators; Shamir 2022 ratio 0.68 | **GENUINELY-NEW-REAL** | MAJOR | State all ratios against one named denominator; concede Shamir 2022 (same survey) is larger than the primary channel |
| C-2 | "More than an order of magnitude" contradicts Table 1 and §6 | tex l.96–97, l.359–361, l.446 vs l.417 | See (d) | **GENUINELY-NEW-REAL** | MAJOR | Use "2–20×" and "2–33%" uniformly in abstract, §5.3, Conclusions |
| C-3 | Fig. 1 is not the sample its caption claims | Fig. 1, p. 2 | See (a): md5 match + 300-DPI title + P4 caption l.1234 | **GENUINELY-NEW-REAL** | MAJOR | Regenerate from the 887,472-row HC supported-pixel sample, or retitle/recaption honestly as the full-catalog map and state the primary support is a subset |
| C-4 | κ=0.97 belongs to a model that did not produce the released labels | tex l.179–181 | See (b): P4 l.1807/l.1810/l.1054 | **GENUINELY-NEW-REAL** | MAJOR | Report the released classifier's GZ1 confusion / 69.91% / κ=0.40; carry over the training-provenance conflict and the CE-included honest negative in condensed form |
| C-5 | Not self-contained as an ApJS catalog paper | §2 (whole), Data Availability | P4 has all of it: completeness ~30% / purity ~70% (P4 l.563 comment block, body §data), NSIDE=64 + $N\ge10$ + 23,633-px HC-RI support + $f_{\rm sky}=0.49005$ (P4 l.1234ff, l.1505), injection–recovery curve (P4 l.1505), MASTER/covariance (i), P5 clustering ladder (j) | **GENUINELY-NEW-REAL** | MAJOR | See closure plan §"What must return" |
| C-6 | FSC $\ell=1$ $z=+6.923$ dropped; monopole caveat truncated | tex l.139–142, l.177–179 | P4 l.1073/l.1083/l.1124: $z=+6.923$, add-one rank $p=0.001996$, binomial-monopole $+6.983/+7.207$. P4 abstract l.996 (verbatim): monopole forward model "localizes its origin **upstream of the classifier, without resolving whether that origin is a true sky asymmetry or a DESI imaging systematic**" — P4′ l.177–179 stops before that clause | **GENUINELY-NEW-REAL** | MAJOR | State the FSC $\ell=1$ result and why it does not overturn the primary null (support/estimator/null differences); restore the unresolved-origin clause verbatim |
| C-7 | [15]/[16] unpublished paths; repo path in body; [14] bare | Refs p. 6; §1 | See (f), (g). Repo is **public** (200) — the privacy framing is falsified; the citability defect and the `v4P.0.1` stamp bug (tex l.554) are real | **GENUINELY-NEW-REAL** (severity partially over-called on the "private" premise) | MAJOR | Deposit P4/P5 as arXiv/Zenodo objects and cite the DOIs, or restore the material; fix l.554 macro; give [14] its DOI/URL |
| C-8 | Eq. 1 is a power threshold used as a CL exclusion | tex l.214–220, l.318–324, l.84–88 | Eq. 1 is defined as the amplitude at which "recovered detection probability crosses 95% coverage" (tex l.212–215; P4 l.1505 confirms: detection = one-sided add-one rank $p<0.05$ against the committed $10^4$ null). §5.2 verb is "excludes". No CL interval is quoted anywhere for $A_{\rm dip}=0.467\%$ | **GENUINELY-NEW-REAL** | MAJOR | Quote a 95% CL upper limit on $A_{\rm dip}$ from the committed null, and say plainly wherever "excludes" appears that this is a power/coverage statement |
| C-9 | Table 1 pools non-commensurable statistics; script's g-bridge contradicts | Table 1, assumption 2 | Script `label_type` fields: "physical (visual/algorithmic)", "algorithmic (Ganalyzer)" ×3, "algorithmic/visual" — four label spaces vs this paper's ViT-Small+TTA observed labels. JSON: `shamir2020` and `shamir2022desi` both `exceeds_A95_obs_face_value=true`, `exceeds_A95_obs_after_g_bridge=false` ($0.02\times0.398=0.00796<0.0098$) | **GENUINELY-NEW-REAL** | MAJOR | Add a cross-pipeline label-incommensurability caveat to assumption 2; report that under the paper's own illustrative bridge two rows (incl. same-survey Shamir 2022) fall below the floor |
| C-10 | Assumption 4 cites an N-scaling comparison Table 1 does not contain | tex l.382–385 | Table 1 columns are Source / Amplitude / N / Ratio; Ratio $=$ amplitude$/A_{95}$, no $1/\sqrt N$ quantity. `illustrative_sensitivity_floor_at_this_N` exists only in the JSON. (Claude quoted it as "√N-scaling"; the tex says "$N$-scaling" — immaterial) | **GENUINELY-NEW-REAL** | MINOR | Add the floor-at-N column or drop the assumption's Table-1 reference |
| C-11 | Assumption 3 is inverted — `fit_dipole` fits direction too | tex l.377–381 | `healpy.fit_dipole` returns monopole + dipole **vector**; a free-axis fit is the correct match to a free-direction model | **GENUINELY-NEW-REAL** | MINOR | Rewrite: the fit is direction-marginalised/free-axis, which is the right test for a free-axis model; state what is *not* done (no matched-axis template) |
| C-12 | Shamir 2025 "20–33%" conflates two encodings | tex l.97, l.349 | Script note: "~2:1 to 1.5:1 CW:CCW imbalance reported (small-N, high-z)"; `amplitude_frac_low/high = 0.20/0.33` | **GENUINELY-NEW-REAL** | MINOR | Define which encoding each endpoint is, or give both |
| C-13 | Longo ">5σ" vs script "~5 sigma" | tex l.113–114 vs script `amplitude_note` | Confirmed mismatch between manuscript and its own committed artifact | **GENUINELY-NEW-REAL** | MINOR | Reconcile against Longo 2011 and use one value in both |
| C-14 | Abstract "7–33%", §6 "2–33%", Table 1 2–33% | tex l.97, l.408 | Confirmed | **GENUINELY-NEW-REAL** — merged into C-2 | MINOR | (folded into R2) |
| C-15 | No Software / Acknowledgements / ORCID | whole paper | `grep -ci "software\|acknowledg\|orcid\|facilities" main.tex` → **0** | **GENUINELY-NEW-REAL** | MINOR | Add ApJS Software, Facilities, Acknowledgements, ORCID |
| C-16 | Fig. 2 legend "Paper IV global $\bar f_{\rm CW}=0.4974$" | Fig. 2, p. 3 | Confirmed at 300 DPI (crop of p. 3): red dotted legend entry reads exactly that. "Paper IV" appears nowhere in the manuscript | **GENUINELY-NEW-REAL** | MINOR | Regenerate the figure with a resolvable label (directive I6: the string is baked into the PNG, a tex grep cannot see it) |
| C-17 | Numeric citation style, not AASTeX author-year | preamble l.27, refs | `\setcitestyle{numbers,sort&compress}` + hand-rolled `thebibliography`; ApJS uses `aasjournal` author-year | **GENUINELY-NEW-REAL** | MINOR | Switch to `\bibliographystyle{aasjournal}` + a real `.bib` before submission |
| C-18 | No multiplicity statement across three tests | §3, §4 | Confirmed: dipole, void/non-void, T-Web reported; no multiplicity sentence anywhere | **GENUINELY-NEW-REAL** | MINOR | One sentence on multiplicity, alongside the existing post-hoc disclosure (tex l.254–257) |
| C-19 | Fig. 2 Filament/Cluster sub-parity offsets unmentioned | Fig. 2 | Confirmed at 300 DPI: Filament ≈0.4980 and Cluster ≈0.4958 sit below the parity line with small error bars; text says only "no significant CW-fraction trend" | **GENUINELY-NEW-REAL** | MINOR | One sentence connecting the offset to the residual monopole of C-6 |
| C-20 | Confirm Zenodo/HF resolve publicly; state format+size | Data Availability | `doi.org/10.5281/zenodo.21461899` → **200**; `huggingface.co/datasets/bamfai/galaxy-chirality-catalog` → **200**. Both public | **Partly FALSIFIED** (resolution verified) / real sliver: format+size absent | MINOR | State catalog file format, row/column count, and size |

### Leg 2 — Grok API (10 findings)

| # | Claim | Verified on disk | Verdict | Sev. | Closure |
|---|---|---|---|---|---|
| G-E1 | Internal repo path in published text | Rendered p. 2 l.63–64; tex l.140–141. (Grok's OCR renders it `PORTFOLIO.DECISION`) | **GENUINELY-NEW-REAL** — dup of C-7/Ge-E3 | MAJOR | → R8 |
| G-E2 | Not self-contained; unusable without the companion | See (i)+(j)+C-5 | **GENUINELY-NEW-REAL** — dup of C-5 | MAJOR | → R5 |
| G-E3 | Abstract "mixes supported-pixel and quality-controlled totals without clarification" | Abstract tex l.84–85 reads "$N_{\rm support}=887{,}472$ **of** $890{,}069$ quality-controlled rows" — numerator and denominator are both named and the body (l.171–176) gives the full ladder 949,584 → −59,515 → 890,069 → 887,472 | **FALSIFIED** | — | None. (The undefined term "sufficient coverage", l.175, is real and folds into R5) |
| G-E4 | Exclusion presented without a numerical model→observable mapping | tex l.94–96 abstract: "under the minimal closure needed to make the claim quantitative"; l.310–313 in italics: Eq. 3 "is *not* derived from Popławski's papers"; l.365–369 assumption 1. Grok's own proposed fix is the manuscript's existing wording | **RE-FLAG-OF-DISCLOSED** (tex l.94–96, l.310–313, l.364–369) | — | None |
| G-M1 | No covariance / mask-induced-bias test on the dipole fit | See (i): P4 l.179–187 NaMaster MASTER-decoupled $\ell=1$, l.267 NSIDE=8 block bootstrap | **RE-FLAG-OF-DISCLOSED-IN-SOURCE**, omitted from P4′ | MAJOR (as omission) | → R5 |
| G-M2 | No T-Web/VoidFinder cross-consistency metric | See (j): P5 l.1785–1806, l.1010, l.2020 | **RE-FLAG-OF-DISCLOSED-IN-SOURCE**, omitted from P4′ | MAJOR (as omission) | → R5 |
| G-M3 | $1/\sqrt N$ ansatz is not an independent re-analysis; label "illustrative only" | tex l.382–385 says verbatim "it illustrates statistical reach and is **not a re-derivation of any other paper's estimator, mask, or null**" | **RE-FLAG-OF-DISCLOSED** | — | None (the Table-1 column sliver is R11) |
| G-N1 | "DRAFT VERSION SEPTEMBER 2, 2026" — update to submission date | AASTeX default draft header; date equals `date +%Y-%m-%d`. Skill Rule 3 territory | **OPINION/GENRE** | NIT | Remove `linenumbers`/draft header at submission |
| G-N2 | Fig. 1: no quadrupole / higher-multipole test | P4 carries the harmonic diagnostics (P4 l.179–187, l.1693) | **RE-FLAG-OF-DISCLOSED-IN-SOURCE** | MINOR | → R5 (one sentence on dipole-only adequacy) |
| G-N3 | Repetition of "qualitative alignment tendency" | Appears at l.93–94, l.297–298, l.442–443 — three sites, in abstract/§5.1/conclusions, which is normal structure | **OPINION/GENRE** | NIT | Optional trim |

### Leg 3 — Gemini API (6 findings)

| # | Claim | Verified on disk | Verdict | Sev. | Closure |
|---|---|---|---|---|---|
| Ge-E1 | Standalone-reader failure; [15]/[16] are repository `.tex` files | See (f) — public repo, but non-archival | **GENUINELY-NEW-REAL** — dup of C-5 + C-7 | MAJOR | → R5, R7 |
| Ge-E2 | Sample-size claim mathematically false; numerators cherry-picked | Gemini's arithmetic reproduced exactly ($8.47{\rm M}/1.3{\rm M}=6.5$; $887{,}472/263=3374$; $887{,}472/1{,}300{,}000=0.68$) | **GENUINELY-NEW-REAL** — dup of C-1 | MAJOR | → R1 |
| Ge-E3 | Internal bookkeeping: l.63 path; Fig. 2 "Paper IV"; refs carry version tags | Path **real** (g); "Paper IV" **real** (C-16); "[15]/[16] contain internal version tags v1.0.274/v0.1.147" is **FALSIFIED** — citing a source's version is normal practice. The real reference defect is different: [15] renders *this* paper's version, "v4P.0.1", via the l.554 macro bug | **GENUINELY-NEW-REAL in part / FALSIFIED in part** | MAJOR / — | → R8, R16, R7 |
| Ge-M1 | Fig. 1 caption says "CW-fraction"; colorbar is the asymmetry $(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})$ | Confirmed at 300 DPI. P4's own caption calls it $A_p = 2(f_{{\rm CW},p}-\tfrac12)$ | **GENUINELY-NEW-REAL** | MAJOR | → R3 (second sub-defect) |
| Ge-M2 | "Largest single sample brought to the question" is false for the tested sample | tex l.414–415; $887{,}472 < 1{,}300{,}000$ | **GENUINELY-NEW-REAL** — dup of C-1 | MAJOR | → R1 |
| Ge-N1 | 95% CI bounds slightly off | See (e): exact 1.95996 multiplier on the unrounded SE reproduces P5's committed bounds to 6 s.f.; P4′ rounds correctly. Gemini recomputed from the rounded SE | **FALSIFIED** | — | None |

## Verdict counts

**Per finding (36 total across 3 legs; Perplexity ABSENT):**

| Verdict class | Count |
|---|---|
| GENUINELY-NEW-REAL | 25 (Claude 19 + 1 partial, Grok 2, Gemini 3 + 1 partial) |
| RE-FLAG-OF-DISCLOSED (in P4′ itself) | 2 (G-E4, G-M3) |
| RE-FLAG-OF-DISCLOSED-IN-SOURCE (in P4/P5, omitted from P4′) | 3 (G-M1, G-M2, G-N2) — each real *as an omission*, folded into R5 |
| FALSIFIED | 4 (G-E3, Ge-N1, C-20 resolution half, Ge-E3 version-tag half) |
| OPINION/GENRE | 2 (G-N1, G-N3) |
| OUT-OF-SCOPE | 0 |

**After cross-leg fingerprint dedup: 20 canonical GENUINELY-NEW-REAL items — 10 MAJOR, 10 MINOR.**

## Canonical real-item list (fingerprint-deduped)

| ID | Sev. | Item | Legs |
|---|---|---|---|
| R1 | MAJOR | Sample-size superiority claim mixes two denominators; false against Shamir 2022 ($N=1.3$M > 887,472) in abstract, §5.2 and §6 | C-1, Ge-E2, Ge-M2 |
| R2 | MAJOR | "More than an order of magnitude" contradicts the paper's own Table 1 (ratios 2.0–20.4) and §6 ("2–20×"); abstract's "~7–33%" drops Table 1's 2–4% rows | C-2, C-14 |
| R3 | MAJOR | Fig. 1 is byte-identical to P4's 8.47M full-catalog FSC asymmetry map (md5 7156f1af…), captioned as the 887,472-row HC supported-pixel sample, and labelled "CW-fraction" where the plotted quantity is the asymmetry | C-3, Ge-M1 |
| R4 | MAJOR | Sole classifier-quality number is κ=0.97 from the retrain that did **not** produce the released labels; released-classifier κ=0.40 / 69.91%, the training-provenance conflict, and the CE-included honest negative are omitted | C-4 |
| R5 | MAJOR | Not self-contained at ApJS: schema, selection function, completeness/purity, NSIDE=64 / $N\ge10$ / 23,633-px support / $f_{\rm sky}$, systematics audit, injection–recovery curve, P4's MASTER + joint covariance, P5's clustering-robustness ladder and void-definition sensitivity all deferred | C-5, G-E2, G-M1, G-M2, G-N2, Ge-E1 |
| R6 | MAJOR | Two omissions convert open questions into closed ones: P4's FSC $\ell=1$ $z=+6.923$ ($p=0.002$) is dropped, and the residual-monopole "unresolved origin" clause is truncated mid-sentence | C-6 |
| R7 | MAJOR | [15]/[16] are non-archival working-tree `.tex` sources (public repo, but no journal/arXiv/DOI) carrying every substantive deferral; [15] renders "v4P.0.1" via the `\paperVersion{}` bug at tex l.554; [14] DESIVAST has no authors/DOI/URL | C-7, Ge-E1, Ge-E3 |
| R8 | MAJOR | `project-context/PORTFOLIO_DECISION_2026-09-02.md, Track C1 Addendum` cited in §1 body as the paper's scientific justification | C-7, G-E1, Ge-E3 |
| R9 | MAJOR | Eq. 1 is a detection-power threshold used throughout as a 95% CL exclusion; no CL upper limit is quoted for $A_{\rm dip}=0.467\%$ despite the committed $10^4$-draw null | C-8 |
| R10 | MAJOR | Table 1 pools four non-commensurable statistics/label spaces; the committed script's own g-bridge output removes the two 2–4% rows (incl. same-survey Shamir 2022) from exceedance, unreported | C-9 |
| R11 | MINOR | Assumption 4 references an $N$-scaling comparison Table 1 does not contain | C-10, G-M3 sliver |
| R12 | MINOR | Assumption 3 inverted — `healpy.fit_dipole` fits direction as well as amplitude | C-11 |
| R13 | MINOR | Shamir 2025 "20–33%" conflates asymmetry fraction with count ratio | C-12 |
| R14 | MINOR | Longo ">5σ" vs the committed script's "~5 sigma" | C-13 |
| R15 | MINOR | No Software / Facilities / Acknowledgements / ORCID section | C-15 |
| R16 | MINOR | Fig. 2 legend "Paper IV global $\bar f_{\rm CW}=0.4974$" — undefined internal series label baked into the PNG (directive I6) | C-16, Ge-E3 |
| R17 | MINOR | Numeric citation style + hand-rolled bibliography, not AASTeX author-year | C-17 |
| R18 | MINOR | No multiplicity statement across the three reported tests | C-18 |
| R19 | MINOR | Fig. 2's Filament/Cluster sub-parity offsets visible but unmentioned; they are R6's residual monopole | C-19 |
| R20 | MINOR | Catalog file format, row/column schema and size not stated (DOI + HF mirror themselves verified public, HTTP 200) | C-20 |

## What the legs got right that the manuscript did *not* get wrong

Recorded so the trail is symmetric. Every headline number in P4′ traces correctly to its source: 8,474,531; 949,584 − 59,515 = 890,069; 887,472; $A_{\rm dip}=0.467\%$, $z_{\rm mom}=+0.635$, $p=0.238$; $A_{95}^{\rm obs}=0.98\%$; 694,642 → 145,789 → 145,766 = 31,937 + 113,829; $\Delta f_{\rm CW}=+0.00145$, SE 0.00332, CI, $p=0.661$/0.673; 812,793 = 428 + 6,673 + 408,187 + 397,505; Table 1's ratio column against the JSON. `main.log` is clean (0 overfull, 0 undefined refs). I re-verified the CI to 6 s.f. and the Table-1 ratios against the JSON and found no transcription error. **No leg found an arithmetic or transcription error in the measurement layer, and neither did I.** The §5.1 finding — that Popławski's papers contain no computed amplitude — is correct, is the paper's real contribution, and is stated at the right evidential strength; the bounce-scope disclaimer is present in the abstract, §1, §5.2, §6 and §7 and smuggles in no bounce claim. Both REJECT verdict words are driven by venue self-containedness (R5/R7), not by a defect in the science.

## Closure plan

**Wave 1 — framing and honesty (R1, R2, R3, R4, R6, R8, R9, R10, R11–R20). ~1 day, no new computation.** These are the items that matter most for integrity, because eight of them are *selective presentation of material the author already computed correctly elsewhere*: the ratio range, the order-of-magnitude claim, the κ, the FSC $\ell=1$, the truncated monopole clause, the g-bridge exceedance flip. R3 and R16 require **figure regeneration**, not text edits — the offending strings are baked into the PNGs (directive I6); R3 additionally needs a map built from the 887,472-row HC supported-pixel sample, or an honest retitle. R9 needs one number computed from the committed $10^4$-draw null (a percentile), not a new run.

**Wave 2 — self-containedness (R5, R7).** Two routes, and only these two:

- **Route A (recommended, and the only one that keeps the decision doc's ≤15 pp cap meaningful): restore the material.** What must come back:
  - *From P4* — (1) catalog schema and release contract: columns, dtypes, flag semantics, per-class counts (CW 1,592,107 / CCW 1,609,053 / NS 5,273,371), file format and size, quarantine definition; (2) selection function: inherited GZ-DESI cuts (REX/DEV/EXP/SER, $r\le19.0$, $r_{50}\ge3''$) and the three DR8 imaging campaigns; (3) completeness ~30% at $N_{\rm HC}=949{,}584$ and ~70% integrated chirality purity, with definitions; (4) the **released** classifier's GZ1 confusion matrix, 69.91% / κ=0.40 (R4); (5) training-provenance disclosure incl. the 26,616-vs-26,626 conflict, the ~67.5–72% CE-ResNet dependence, and the CE-included collapse-to-chance (0.5617 / 0.517); (6) estimator spec: NSIDE=64, $N_{\rm spiral}(p)\ge10$, the 23,633-px HC-RI vs 24,087-px FSC supports, $f_{\rm sky}=0.49005$, null construction; (7) the residual-monopole diagnosis with its unresolved origin **and** the FSC $\ell=1$ $z=+6.923$ result with the reason it does not overturn the primary null (R6); (8) the injection–recovery curve as a figure with the 2,000-axis scheme and amplitude grid; (9) a corrected Fig. 1 (R3); (10) the mask/MASTER-decoupled $\ell=1$ leg and the NSIDE=8 block-bootstrap joint covariance (settles G-M1 in-paper).
  - *From P5* — (11) the clustering-robustness ladder (NSIDE 2/4/8 and 3,750 nearest-MAXIMALS 3-D clusters; point estimate $+0.00145442$ throughout, all intervals containing zero) plus the 13-column nuisance-basis specification; (12) the void-definition sensitivity across VoidFinder / V2-REVOLVER / V2-VIDE and the T-Web-vs-VoidFinder distinction (settles G-M2 in-paper).
- **Route B: stay at 6 pp as a focused Letter on the Popławski test** — viable *only* if P4 and P5 are first deposited as arXiv or Zenodo objects with DOIs, so [15]/[16] become resolvable citations. Until then no deferral in the manuscript is resolvable and the paper fails self-containedness at any length. Note Route B also changes the venue and the title, since "We release an 8,474,531-object catalog" cannot survive as the framing of a paper that does not describe the catalog.

**Page target.** Route A lands at **13–15 pp** in AASTeX twocolumn: current 6 pp, plus ~4–5 pp of §2 catalog material (items 1–6), ~1 pp for the R6 diagnostics, ~1 pp for the injection–recovery figure plus the corrected Fig. 1, and ~1 pp for the P5 items (11)–(12), with items 5 and 10 compressible into an appendix if the cap binds. That is **inside the ≤15 pp allowance** in `PORTFOLIO_DECISION_2026-09-02.md` l.78 ("C1 · P4′ — catalog + dipole null, ≤15 pp, P5 folded in as one section"), but it consumes essentially all of it — the 6-pp draft was under-scoped against its own decision document, not over-scoped. Route A is therefore the on-plan route.

**Directive R note (R2 convergence budget).** This is round 1 on P4′ and every MAJOR is either a framing correction or a scope decision already written into the portfolio decision — no science is blocked. The next round should follow a *scope-and-restore* action, not another review sweep.
