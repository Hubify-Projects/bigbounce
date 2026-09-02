# P4′ v4P.0.2 — Claude INT referee leg, round R2

- **Reviewer:** Claude INT leg (independent, skeptical ApJS referee; not told any expected verdict)
- **Model:** `claude-opus-5[1m]`
- **Manuscript:** `pipelines/p4prime_chirality_test/paper/main.pdf`
- **sha256 (computed this session):** `78936e3610b2d9274e2ba19b8567207b7cd1cb99d9368585d6ff3d78ac9d1db1` — matches the round label
- **md5:** `413705f8cf6ce69da4fe6744b3014ea2` · **Pages:** 10 · **Version:** v4P.0.2, September 2, 2026
- **Source bound:** `pipelines/p4prime_chirality_test/paper/main.tex` (997 lines), `main.log`
- **Round:** `ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2`
- **Date:** 2026-09-02

**Verdict: major-revisions.** 3 MAJOR, 13 MINOR.

---

## Evidence actually inspected

Every assertion below was checked against a file on disk or a rendered page; nothing is
asserted from the R1 record alone.

- `main.tex` read in full; `main.log` (1 overfull hbox 5.88 pt, 0 undefined refs/citations,
  3 `A float is stuck` warnings at l.758/778/799).
- All 10 pages rendered at 100 DPI; pp. 4 and 6 (the figure pages) re-rendered at **300 DPI**
  per directive I6 and read visually.
- `pipelines/p2_chirality/chirality_catalog_paper.tex` (P4 v1.0.274) — ll. 1217, 1289, 1294–1302,
  1436, 1780–1815, 1980.
- `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (P5 v0.1.147) — ll. 1003–1006,
  1037, 1171, 1617, 1666, 1785–1840, 2020, 2118.
- `pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.json` (all 18
  `per_amplitude` rows, `sample`, `headline_reproduction_gate`, `interpretation_limits`) and its
  generator `a95_observed_label_upper_limit_v1_0_265.py` ll. 110–160.
- `pipelines/p2_chirality/apjs_release_v1.0.259_strict/primary_strict_fixed_occupancy_amps_10000.npy`
  — loaded and re-reduced (mean, std, percentiles, upper-tail rank).
- `research/bh_universe_dipole/a95_null_cl_2026_09_02.py` and both output JSONs.
- Arithmetic re-derived independently: Cohen's κ from both printed confusion matrices, three-class
  accuracy, every ratio in Table 3, every sample-size ratio, the count ladders in §2.1/§4, the
  Bonferroni-5 critical value.

---

## PART A — verification of the 20 canonical R1 items on v4P.0.2

**Summary: 16 fully closed · 2 partially closed (R3, R9) · 2 not closed (R5 page target, R17).**
R15 is closed except for ORCID. I found no item where the closure claim in
`project-context/SSOT/paper-4p/status.md` is untrue, and several where the closure is better
than the item required. Two closures introduced new defects (R7 → MINOR-4; R10 → MINOR-5),
and one restoration (R5) introduced MAJOR-3.

| ID | Sev. (R1) | Status in v4P.0.2 | Evidence I checked |
|---|---|---|---|
| **R1** sample-size denominator | MAJOR | **CLOSED** | One denominator (887,472) in abstract l.102, §5.2 l.648–651, §6 l.759–762; Shamir (2022, N=1.3M) explicitly conceded larger in all three. I recomputed 887,472/200,000 = 4.44, /263 = 3,374, /1,300,000 = 0.68 — the printed "4–3,400×" is now correct against the stated denominator, and the excluded row is named. "largest" is restricted to the catalog release (l.758). |
| **R2** "order of magnitude" | MAJOR | **CLOSED** | `grep -c "order of magnitude"` → 0. "2–20×" at abstract l.99–100, §5.3 l.695, §6 l.763; "2–33%" at abstract l.100, §6 l.752, §7 l.792 — matching Table 3's ratio column (2.0–20.4) and amplitude column (2–33%). The abstract's old "~7–33%" is gone. |
| **R3** Fig. 1 mislabel | MAJOR | **PARTIAL** | Caption (l.351–358) is now honest and, at 300 DPI on p. 4, agrees with the PNG's own baked-in title "Galaxy Chirality Asymmetry Map (8.47M galaxies, equivariant)" and its colorbar $(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})$; it names the 24,087-px FSC support and states this is *not* the HC-RI support. **But §3 l.345–346 still reads "Figure~\ref{fig:skymap} shows the per-pixel HC CW-fraction sky map underlying this fit"** — both halves of the original defect (wrong sample, "CW-fraction" for an asymmetry) survive in the body, now in direct contradiction with the corrected caption three lines later. See MINOR-2. |
| **R4** κ=0.97 vs κ=0.40 | MAJOR | **CLOSED (exemplary)** | Table 1 (l.238–256) prints the released classifier's full 3×3 GZ1 matrix. I summed it: 240,919 total ✓; diagonal 141,438 → 58.7% ✓; the CW/CCW block 117,205 ✓ with 81,939 agreements → 69.911% ✓; and I computed Cohen's κ on that block from scratch ($p_o=0.69911$, $p_e=0.50033$) → **κ = 0.3978 ≈ 0.40 ✓**. The retrain's $[[1460,10],[30,1500]]$ likewise gives accuracy 0.98667 and κ = 0.97333 ✓. The overlap-contamination caveat, P4's "neither comparable to, nor a replacement for" language, the CE-included collapse (0.5617/0.517), and the 26,616-vs-26,626 conflict are all restored (l.213–284). |
| **R5** self-containedness | MAJOR | **SUBSTANTIALLY CLOSED / page target not met** | Route A restoration is real, not nominal, and the imported numbers are accurate. Verified: schema + selection function + release contract (l.170–209); completeness ~30% / purity ~70% (l.185–188); estimator and null specification as a new §2.3 (l.308–333); a new injection–recovery figure **and** an 18-point table whose 12 printed rows I checked one-by-one against `per_amplitude` (0.5325→0.533, 0.6745→0.675, 0.8175→0.818, 0.9105→0.911, 0.9465→0.947, 0.9815→0.982, 0.9975→0.998 — all correctly rounded), plus the interpolation claims (linear 0.0098 ✓, logistic 0.0095478 ✓, "consistent to better than 0.03 pp" ✓ = 0.025 pp); the 4×4 estimator correlation matrix; P5's clustering ladder, which matches P5 l.2020 to the digit at all four scales; P5's five-way void-definition family, which matches P5 ll.1785–1840 (|z|≤1.25 ✓, Bonferroni-5 threshold 2.58 ✓, max half-width 0.75 pp ✓); the bias-hardening table; and a systematics appendix. Substantive deferrals to [15]/[16] are down to three sentences (l.208, l.530, l.878). **Page target 13–15 pp not met (10 pp).** See "Is 10 pages adequate?" below — and MAJOR-3, MINOR-3, MINOR-6, MINOR-7 for what the restoration still omits. |
| **R6** FSC ℓ=1 dropped / clause truncated | MAJOR | **CLOSED** | FSC ℓ=1 restored at l.394–398 with $z=+6.923$, rank $p=0.001996$ on 500 draws, and the binomial-monopole $+6.983$/$+7.207$ — matching P4. The non-overturning argument is given with its reasons (different support, estimator, null family). The truncated clause is restored verbatim at l.233–236: "without resolving whether that origin is a true sky asymmetry or a DESI imaging systematic, which remains an open attribution". |
| **R7** non-archival refs / macro bug | MAJOR | **CLOSED** (introduces MINOR-4) | Rendered p. 10: [14] now carries Rincón et al., ApJ 982, 38 (2025), DOI:10.3847/1538-4357/adb559, arXiv:2411.00148 ✓; [15] reads a literal "v1.0.274" — the `\paperVersion{}` stamp bug is gone ✓ — and cites a Zenodo DOI rather than a repo path ✓; [16] gives the served URL and states plainly that no DOI has been minted ✓. New defect: [15] and [17] now share one DOI for two different objects (MINOR-4). |
| **R8** internal governance path | MAJOR | **CLOSED** | `grep -c "PORTFOLIO_DECISION\|project-context"` over `main.tex` body → 0 (the string survives only in the `%`-comment header, ll. 5–6, which does not typeset). §1 l.144–147 now motivates the test from the program's own torsion mechanism, with no internal path. |
| **R9** Eq. 1 power-vs-CL | MAJOR | **PARTIAL** | The distinction itself is now stated correctly and prominently (l.374–377: "It is not itself a confidence-level bound on the measured value"), and §5.3 l.691–693 repeats it. That half is a genuine improvement. But the "genuine 95% confidence-level statement" supplied is the **95th percentile of the null**, which I reproduced exactly from the committed array (0.0066932 → 0.669% ✓). That is a critical value of the no-signal distribution, not a confidence-level upper limit on $A_{\rm dip}$ — which is what R1 asked for. See MAJOR-2. |
| **R10** Table pooling / g-bridge | MAJOR | **CLOSED** (introduces MINOR-5) | Table 3's caption now names the four label-space families explicitly and says "the ratio column is not a like-for-like statistical comparison across rows". The g-bridge flip is reported in the body (l.652–659) and I confirmed `exceeds_A95_obs_after_g_bridge: false` for `shamir2020` and `shamir2022desi` in the committed JSON, with the honest framing that it *weakens* the exclusion on the two largest comparison samples. Caption miscounts rows (MINOR-5). |
| **R11** assumption 4 / N-scaling | MINOR | **CLOSED** | l.722–726 now says the $1/\sqrt N$ ansatz "is not the basis of the Ratio column in Table~\ref{tab:bh_exclusion}"; no Table-1 reference remains. |
| **R12** assumption 3 inverted | MINOR | **CLOSED** | l.718–721 now reads "`healpy.fit_dipole` fits both amplitude and direction, which is the correct match to a model with no predicted axis", and states what is *not* done (no matched-axis search). Correct. |
| **R13** Shamir 2025 encoding | MINOR | **CLOSED** | Labelled a count ratio in three places (l.126 "~2:1", caption l.669–672, assumption 5 l.729–732) with the ~2:1→1.5:1 range given. |
| **R14** Longo >5σ vs ~5σ | MINOR | **CLOSED** | l.121 now "$\sim\!5\sigma$", matching the committed script's `amplitude_note`. |
| **R15** Software/Facilities/Ack/ORCID | MINOR | **CLOSED except ORCID** | New section at l.890–899 with Software, Facilities, and Acknowledgements. No ORCID (MINOR-9); SSOT records that none was fabricated, which is the right call. |
| **R16** Fig. 2 "Paper IV" legend | MINOR | **CLOSED** | Verified at **300 DPI on p. 6** (not by filename): the legend now reads "catalog global $\bar f_{\rm CW}=0.4974$". "Paper IV" appears nowhere in the regenerated PNG. Directive I6 satisfied. |
| **R17** citation style | MINOR | **NOT CLOSED** | Confirmed: `\setcitestyle{numbers,sort&compress}` at l.27 and a hand-rolled `\begin{thebibliography}` at l.901. Rendered p. 10 shows bracketed numerals. Deferral is honestly recorded in SSOT. |
| **R18** multiplicity | MINOR | **CLOSED** | l.572–578 gives a multiplicity note naming all three headline tests and observing none is significant even uncorrected. |
| **R19** Filament/Cluster offsets | MINOR | **CLOSED** | Fig. 3 caption (l.535–546) names both offsets with values and ties them to the §2.2 residual monopole rather than to environment. |
| **R20** format/schema/size | MINOR | **CLOSED** | Data Availability l.880–887: single Apache Parquet, 952,115,239 bytes, per-row columns, and the 249,066 / 59,515 quarantine split. I confirmed all three figures against P4 ll. 1217 and 1980. |

**Reported-as-deferred items independently confirmed:** the closure report says R17 and the R5
page target were not closed. Both statements are true, and no closure claim in the SSOT table
was overstated. This is an honest closure record.

---

## PART B — fresh referee read at ApJS catalog standard

### MAJOR findings

---

**MAJOR-1 — The primary channel's own CW fraction is never reported, and the committed
artifact behind Eq. 1 puts it in direct conflict with the monopole the paper does discuss.**

*Location:* §2.2 l.232–236; §3 l.340–346 and l.469–475; §4 Fig. 3 caption l.541–546;
Appendix l.838–846. Absent throughout.

*Defect.* The manuscript refers to "the residual handedness monopole" or "the catalog-wide
residual monopole" in four places and never gives its value in the text. The only monopole
number a reader can extract is `0.4974`, and it appears **only inside the Fig. 3 caption and
the Fig. 3 PNG**, as the catalog-wide global CW fraction ($A_p = -0.53\%$, a CCW excess).

Meanwhile the committed artifact that *produces Eq. 1* — the paper's central sensitivity
claim — reports the opposite. From
`pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.json`:

```
"sample": { "n_galaxies_in_support": 887472,
            "n_cw_in_support": 454968,
            "p_cw_global": 0.5126561739412624, ... }
```

I confirmed the semantics in the generator rather than trusting the key name
(`a95_observed_label_upper_limit_v1_0_265.py` ll. 128, 139–141):

```python
is_cw = labels == "CW"
cw = np.bincount(pix[is_cw], minlength=npix)
n_cw = int(cw[support].sum());  n_gal = int(capacities.sum())
p_cw_global = n_cw / n_gal
```

454,968 / 887,472 = **0.512656**. So on the 887,472-galaxy HC-RI support that carries the
paper's headline null, $f_{\rm CW} = 0.5127$, i.e. an $A_p$ monopole of **+2.53%** — positive,
and **2.6× the quoted $A_{95}^{\rm obs} = 0.98\%$ floor**.

This cannot be reconciled with either monopole the paper narrates. P4 l.1289 states the
high-confidence monopole as $f_{\rm CW}-\tfrac12 = -3.95\times10^{-3}$, i.e.
$f_{\rm CW}^{\rm HC} = 0.49605$; the catalog-wide value is 0.49735. 0.51266 differs from
0.49605 by 1.66 percentage points **and flips sign about 0.5**. Both cannot describe the
primary channel.

*Why this is MAJOR, not bookkeeping.* Two readings, and the paper does not let a referee
distinguish them. (i) If 0.51266 is right, then the entire monopole discussion the paper
carries — §2.2's forward-model attribution, the appendix's slab ladder ($-0.110\%$ to
$-0.463\%$), Fig. 3's reference line — describes a *different* sample from the one carrying
the headline result, and the primary channel has an uncontrolled zeroth-order systematic
2.6× the sensitivity floor that §5 uses to exclude $\eta > 0.98\%$. (ii) If 0.49605 is right,
then the Eq. 1 injection model is baselined at the wrong $p_{\rm global}$ (it injects
$p_{\rm pix} = p_{\rm CW}^{\rm global} + (A/2)(\hat n\cdot u)$ about 0.5127), and
$A_{95}^{\rm obs} = 0.98\%$ — and with it §5's exclusion and the abstract's "$2$–$20\times$" —
is affected.

I am not asserting which is correct; I could not settle it from the manuscript, which is
precisely the problem. *Required:* state the primary channel's own $f_{\rm CW}$ and monopole
in §2 or §3 with its significance, reconcile it against the catalog-wide 0.4974 and P4's
HC $-3.95\times10^{-3}$ (a selection-induced shift of this size across the HC/QC/support cuts
needs its own sentence), and confirm that the Eq. 1 injection baseline is the intended one.

---

**MAJOR-2 — The "genuine 95% confidence-level statement" is a null critical value, not a
confidence-level bound; R9's actual request is unmet and the paper now claims something
stronger than it has.**

*Location:* §3 l.376–384; cross-referenced as authoritative at §5.3 l.691–693. Script:
`research/bh_universe_dipole/a95_null_cl_2026_09_02.py`.

*Evidence.* I loaded the committed null array and reproduced every number: mean 0.00362029,
std 0.00164643 (matching P4 l.1302 to 6 s.f.), 95th percentile **0.0066932 → 0.669% ✓**,
upper-tail fraction at $A_{\rm dip}$ = 0.2376 ✓. The arithmetic is correct. The *inference
label* is not.

The 95th percentile of the null is the acceptance boundary of the very test the paper already
reports as rank $p = 0.238$; it conveys no information beyond that $p$-value, and it is a
statement about the *no-signal* distribution, not a bound on the true amplitude. Calling it
"a genuine 95% confidence-level statement" (l.377–378) and then telling the reader in §5.3
that "a genuine 95% CL statement is given in Sec. 3" asserts a CL bound on $A_{\rm dip}$ that
has not been constructed. The script's own `statement` field makes the same slide, from the
defensible "null-consistent at 95% CL" to "a genuine confidence-level statement".

This matters more than usual here because the estimator is a **positive-definite amplitude with
a null mean of 0.362%** — the sampling distribution does not concentrate at zero under the
null, so a naive percentile is a particularly poor stand-in for an upper limit.

*Required, and cheap:* the committed machinery already supports the correct construction.
`per_amplitude` carries `recovered_amp_p16_p50_p84` at 18 injected amplitudes; inverting it for
the $A$ at which the observed 0.467% falls at the 5th percentile of the recovered distribution
gives a genuine 95% CL upper limit on the injected amplitude, from artifacts already on disk
and with no new inference. Alternatively, drop the CL claim entirely and rest §5 on the
detection-power statement, which the paper is otherwise careful about. What is not acceptable
is the current wording.

---

**MAJOR-3 — The R5 restoration imports P4's block-bootstrap correlation matrix but drops its
per-estimator significances, and the one dropped for the headline channel is 3.5× the one
reported.**

*Location:* §3 l.447–475 (the 4×4 correlation matrix and its three-sentence reading).

*Evidence.* P4 l.1436, describing the same shared $\nside=8$, $N_{\rm boot}=2{,}000$, seed-42
run that P4′ imports the matrix from, reports: "the monopole is the only $|z|>3$ mode
($z=-6.57$ …), while both dipole amplitudes and the MASTER-decoupled harmonic $\ell=1$ power
are non-significant (**$z=+2.21$ real-space dipole**, $+0.81$ WLS dipole, $-0.61$ MASTER
$\ell=1$)".

P4′ reproduces the correlation matrix in full and then reports exactly one of the four $z$
values — the monopole's — as "The monopole is the only channel with $|z|>3$ against its own
bootstrap scatter ($z=-6.57$)". The statement is true. But it withholds that in that same
resampling the paper's **primary real-space dipole sits at $z = +2.21$**, against a null that
propagates spatial coherence, while the abstract, §3, §6 and §7 headline $z_{\rm mom} = +0.635$
from the label-randomization null. A referee reading P4′ alone would not know the headline
channel has a 2.2σ reading under the more conservative of the paper's own two nulls.

I do not think +2.21 overturns the null — P4's own reading (non-significant, consistent with
the primary result) is defensible, and the block bootstrap and the label-randomization null
answer different questions. The defect is that the choice was made silently, in a paper whose
R1 round already had to restore two other omissions of exactly this shape (R6: the dropped FSC
$\ell=1$ and the truncated monopole clause). Selective import from a source the reader cannot
easily check is the specific failure mode this manuscript is most exposed to.

*Required:* print all four per-estimator $z$ values alongside the correlation matrix, with
P4's own reconciliation of $+2.21$ against $+0.635$ in one sentence.

---

### MINOR findings

**MINOR-1 — The Introduction states the wrong N for the primary result.** §1 l.152 reports the
primary null "on 890,069 quality-controlled high-confidence spirals". The abstract (l.87–88),
§2.1 (l.191–195) and §3 (l.341) all correctly have 890,069 as the *selection* and 887,472 as
the number entering the supported-pixel fit. R1 spent an entire MAJOR (R1) on denominator
discipline; this is the same error surviving in the Introduction. Fix to 887,472.

**MINOR-2 — R3 residue: body contradicts the corrected Fig. 1 caption.** §3 l.345–346 says
Fig. 1 is "the per-pixel HC CW-fraction sky map underlying this fit"; the caption on p. 4 says
it is the full-catalog FSC map and explicitly *not* the HC-RI support used for the fit, and
plots an asymmetry, not a CW fraction. As printed the paper contradicts itself across three
lines. One sentence: "Figure 1 shows the full-catalog asymmetry map; the primary fit is
performed on the narrower HC-RI support described in §2.1."

**MINOR-3 — Table 2 silently omits T5 from a numbered bias battery.** The table prints T1–T4,
T6–T8 and the caption says "All seven tabulated tests pass". A referee sees a gap at T5 and
must assume the worst. P4 handles this correctly (l.1794 caption and l.1792 text): the former
linear-Pearson-vs-RA row was *removed* because a linear Pearson $r$ is inappropriate for a
circular coordinate, and the map-level low-$\ell$ real-$Y_{\ell m}$ regression supersedes it.
That disposition is creditable and should be carried over — one clause in the caption. Omitting
it converts a good decision into an apparent suppression.

**MINOR-4 — Two different objects share one DOI in the bibliography (new, from R7's closure).**
[15] (the P4 release *paper*) and [17] (the *catalog dataset*) both resolve to
`doi:10.5281/zenodo.21461899`, and the same DOI is used for the catalog in §2.1 l.200–201 and
in Data Availability l.863–864. Either the deposit contains both — in which case [15] and [17]
are one reference and should be merged, with the text distinguishing paper from data — or the
DOI is wrong on one of them. As printed a reader following [15] lands on a dataset.

**MINOR-5 — Table 3 caption miscounts its own rows.** "The four rows pool non-commensurable
statistics" (l.668). The table has five rows; four *statistic families*. Reword to "the five
rows pool four non-commensurable statistic families".

**MINOR-6 — The residual monopole is discussed four times without a value in the text.** §2.2,
§3, the Fig. 3 caption and the Appendix all reason about "the residual handedness monopole",
but its value appears only inside a figure caption (0.4974) and nowhere in the body, and its
uncertainty ($\pm0.000279$, P5 l.1037/1171) and significance ($-9.47\sigma$ per-pixel binomial,
$z=-6.57$ block bootstrap) are not both given in one place. For an ApJS catalog paper this is
the single most important number a downstream user of the labels needs — P4 says so itself
(l.1289: any $\ell=0$ parity claim at or below this level is indistinguishable from the
artifact). State $f_{\rm CW}$, its uncertainty, its significance and the recommended
monopole-renormalization in §2.2. (Related to, but separable from, MAJOR-1.)

**MINOR-7 — The T-Web corroboration rests on a bin with 428 galaxies, and the per-class N are
not in the text.** l.526–528 offers the four-class T-Web run as showing "the same pattern — no
significant CW-fraction trend from void through wall, filament, to cluster". Reading Fig. 3 at
300 DPI, the per-class counts are Void 428, Wall 6,673, Filament 408,187, Cluster 397,505
(summing to the stated 812,793 ✓). The Void bin — the class most relevant to the void/non-void
question this diagnostic is offered to corroborate — has 428 objects and an error bar spanning
roughly 0.437–0.530. It has essentially no power, so "no significant trend" there is
uninformative rather than confirmatory. Put the per-class N in the text and state that the
T-Web run constrains Filament/Cluster and is uninformative in the Void class.

**MINOR-8 — Keywords are not AAS Unified Astronomy Thesaurus terms.** l.110–111 uses
MNRAS/A&A-style colon keywords ("galaxies: spiral, galaxies: statistics, …"). ApJS requires UAT
terms with their numeric identifiers (e.g. "Spiral galaxies (1560)", "Large-scale structure of
the universe (902)", "Astrostatistics (1882)").

**MINOR-9 — No ORCID.** AAS journals require an ORCID for the corresponding author. Correctly
not fabricated; still a submission blocker that must be resolved before the kit is final.

**MINOR-10 — R17 open: citation style.** `\setcitestyle{numbers,sort&compress}` (l.27) plus a
hand-rolled `thebibliography` (l.901) produce bracketed-numeral citations. ApJS is author-year
via `aasjournal`. A `references.bib` already sits beside the manuscript, so the conversion is
mechanical; the deferral is defensible for a review draft but not for submission.

**MINOR-11 — Draft-mode artifacts and float pressure.** `\documentclass[twocolumn,linenumbers]`
(l.12) still yields "Draft version September 2, 2026" and line numbers on every page. `main.log`
carries three `A float is stuck` warnings (l.758, 778, 799, for the floats at input lines 285,
370 and 579) and one 5.88 pt overfull hbox (l.767, the bias-hardening table). None affects
correctness; all should be cleared at submission, and the stuck-float warnings suggest the
`[t]`-only placement on five floats in a 10-page paper is over-constrained.

**MINOR-12 — The load-bearing citation's publication status is unstated.** [11]
(Popławski, "Universe in a rotating black hole and preferred axis") is given as
"arXiv:1910.10819 (2020)" with no journal reference, against an arXiv identifier from October
2019. This is the *only* source for the observational claim the entire paper is built to test
(§5.1 l.602–613 rests wholly on it). State explicitly whether it is published or remains a
preprint, and reconcile the year with the identifier — a referee will ask whether the paper's
central target has been peer reviewed.

**MINOR-13 — A third N is attached to "the primary HC sample".** §3 l.450–451 describes the
block bootstrap as run on "primary HC sample $N=949{,}584$", while §2.1 and §3 define the
primary channel as 887,472 (from a 890,069 selection). The 949,584 figure is correct for P4's
bootstrap, but calling it "the primary HC sample" in a paper that has just defined that phrase
differently invites confusion. Name it "the pre-QC HC sample (949,584)".

---

### What is right, recorded so the trail is symmetric

Every number I independently re-derived checked out. Cohen's κ from both printed confusion
matrices (0.3978 and 0.97333); three-class accuracy 58.7%; 69.91% on 117,205; all five ratios
in Table 3; all four count ladders (949,584 − 59,515 = 890,069; 694,642 → 145,789 → 145,766 =
31,937 + 113,829; 812,793 = 428 + 6,673 + 408,187 + 397,505; 3,201,160 = 1,592,107 + 1,609,053);
the twelve printed injection-recovery rows against the committed JSON, including both
interpolation methods and their agreement to 0.025 pp; the null array's mean, std and 95th
percentile; P5's four clustering-scale CIs to five decimals; P5's five-way sensitivity family
(|z|≤1.25, Bonferroni-5 = 2.58, max half-width 0.75 pp); $f_{\rm sky}$ = 23,633/49,152 = 0.4808
and 24,087/49,152 = 0.49005; the Parquet byte count and quarantine split against P4 l.1980.
**I found no arithmetic or transcription error anywhere in the measurement layer.**

The §5.1 finding — that Popławski's papers contain a qualitative alignment tendency and no
computed amplitude — is the manuscript's genuine and non-trivial contribution, it is stated at
exactly its evidential strength, and the closure $A_{\rm pred}\approx\eta$ is flagged as the
authors' own construction in the abstract, §5.1, §5.3 and the assumptions list. The
bounce-scope disclaimer is present in five places and no bounce claim is smuggled in. The
g-bridge disclosure (l.652–659) reports a result that *weakens* the paper's own exclusion on
the two largest comparison samples, unprompted by any reviewer beyond R10 — that is the right
instinct and should be preserved verbatim through revision. Data availability is genuinely
strong: I confirmed the Zenodo concept/version DOIs and the HuggingFace mirror are cited with
format, byte count, schema and quarantine.

None of my three MAJOR findings is a bounce claim, an overclaim of the exclusion, or a
fabricated number. Two are omissions of material the authors already computed correctly
(MAJOR-1, MAJOR-3) and one is a mislabeled inference (MAJOR-2).

---

## Is 10 pages adequate?

**No — but the deficit is specific missing material, not page count, and the closure worker was
right to refuse to pad.** The SSOT records 10 pp against R1's 13–15 pp estimate; page 10 holds
only 1,845 characters of bibliography, so the paper is ≈9.4 pp of content.

Judged as an ApJS *catalog* paper — can a reader evaluate and use this catalog from this paper
alone? — the following is still missing and is load-bearing:

1. **A real schema table.** §2.1 gives the schema as one prose clause ("each row carries
   `dr8_id`, sky coordinates, the observed chirality label, per-class probabilities, and
   quality-control flags"). ApJS catalog papers need a column-by-column table: name, dtype,
   unit, null convention, and the exact semantics of every flag — `raw_flip_qc_unsafe`,
   `primary_hc`, `class_eq`, `do_not_use_for_science`. ≈0.5–0.75 pp.
2. **Completeness and purity as functions, not two scalars.** "~30% completeness, ~70% purity"
   integrated over the whole catalog is not usable for sample selection. A user needs both
   against $r$ magnitude, half-light radius and $p_{\rm eq}$, at minimum as a small table.
   ≈0.5 pp.
3. **The primary channel's monopole and its reconciliation** (MAJOR-1) — ≈0.25 pp.
4. **The four per-estimator block-bootstrap $z$ values with P4's reconciliation** (MAJOR-3) —
   ≈0.15 pp.
5. **The correct 95% CL construction** (MAJOR-2) — ≈0.15 pp.
6. **T5's disposition** (MINOR-3) and **the T-Web per-class N with a power caveat**
   (MINOR-7) — ≈0.15 pp.

That is ≈1.7–2.0 pp of genuinely required material, landing the paper at **12–13 pp** — inside
the ≤15 pp allowance, and close enough to R1's 13–15 pp estimate that the estimate should be
read as having been approximately right about *content* while the closure was right that the
gap could not be filled by expansion for its own sake. I explicitly endorse the SSOT note that
"no content was padded to hit a page count"; padding would have been the worse failure. The
page-count miss is not itself a defect. Items 1 and 2 are.

---

## Verdict

**major-revisions.**

The R1 closure was real work, honestly reported, and in places (R4, R6, the P5 restoration)
better than the item required; 16 of 20 canonical items are fully closed and I could not find a
closure claim in the SSOT record that overstates what is in the file. The measurement layer is
arithmetically sound at every point I re-derived it, and the paper's actual contribution — that
the black-hole-universe model supplies no computed amplitude, and what happens when a minimal
closure is confronted with a real sensitivity floor — is sound, well-scoped, and honestly
qualified.

It is not yet acceptable because MAJOR-1 leaves an unresolved conflict about the monopole of the
very sample carrying the headline null, with a committed artifact putting it at 2.6× the
sensitivity floor the paper's §5 exclusion rests on; because MAJOR-2 asserts a
confidence-level bound that has not been constructed, in the one passage the previous round
specifically asked to be made precise; and because MAJOR-3 repeats the selective-omission
pattern R6 was raised to correct, in material newly imported by the R5 restoration.

None of these requires new computation. MAJOR-2 and MAJOR-3 are answerable from artifacts
already committed; MAJOR-1 requires reconciliation and a stated number, and only affects
$A_{95}^{\rm obs}$ in the branch where the Eq. 1 baseline turns out to be wrong. With those
three closed, the schema and completeness/purity material of items 1–2 above added, and the
thirteen minors swept, I would expect to recommend acceptance.

*Not reject:* nothing here is a fabricated result, an overclaim, or a scope violation, and the
science is not in question.
*Not minor-revisions:* MAJOR-1 could move the paper's headline sensitivity number, and MAJOR-2
is an incorrect statistical claim in the abstract's supporting chain.
