# P4′ v4P.0.7 — Claude INT referee leg, exact-version confirmation board

- **Reviewer:** Claude INT leg (independent ApJS referee, verdict-blind)
- **Model:** claude-opus
- **Manuscript:** `pipelines/p4prime_chirality_test/paper/main.pdf`
- **sha256:** `7eb1f99ecc5e3d50a90457997e075873750eff0902ac95eadf9e430d27729a9d` (computed this session, `shasum -a 256`)
- **md5:** `1fc6b21ae07accb0b2a3441e4a31ebc1` (computed this session, `md5`)
- **Pages:** 13 (`pdfinfo`) · **Version:** v4P.0.7 · **Date:** September 5, 2026
- **Round:** `ROUND_2026-09-18-P4P-v4P.0.7-EXACTPDF-7eb1f99e-CONFIRM`
- Page 1 render confirms the bound title block reads "(Dated: September 5, 2026; Version v4P.0.7)" — the PDF is self-consistent with `\paperVersion`/`\paperTimestamp` in `main.tex` ll.61–62.
- Line numbers below are `main.tex` (the compiled source of this exact PDF); page numbers are the bound PDF.
- Focus of effort, per this board's charge: the v4P.0.5–v4P.0.7 additions — Sec. A.1 "Robustness and disclosure" (`sec:robustness_disclosure`, ll.982–1132, pp.10–12), i.e. the pixel-level calibration, full-parent selection behavior, structure cross-correlations, and the row-16(iv-b) DESI DR1 BGS external environment test. A fresh full read of the whole manuscript was also performed.

---

## PART 0 — What I verified as CORRECT before listing defects

I state these so the findings below are not read as a blanket rejection of the new material. Recomputed or source-matched this session:

| Claim (location) | Verification |
|---|---|
| Pixel slope $dA/df=+0.0167\pm0.0089$; naive identity $+0.434$, $47\sigma$; mixture identity $-0.0093$, $2.9\sigma$ (ll.985–993, Table 6 p.10) | Exact match to `injection_pilot/ROW13_PILOT_2026-09-04.md` §"Part A at N=20k" (+0.0167±0.0089; +0.4343; ~47σ/~35σ; −0.00934; ~2.9–3.0σ). Values are faithfully transcribed. |
| Full-parent $A=0.566\%$, $z=+4.44$, axis RA 278.6°/Dec +25.3° (ll.1019–1020) | Matches `ROW16I_FULL_PARENT_2026-09-04.md` §Result exactly (0.5660%, +4.440, 278.63°/+25.32°). |
| DES-leg removal $z=+0.48$; Galactic cuts do not remove it; axis shift 107.5°; mask-leakage floor 0.19% (ll.1024–1028) | Matches `ROW16IB_AXIS_SHIFT_2026-09-04.md` §B (C0 drop DES z=+0.48), §B (\|b\|>20° z=+4.09, \|b\|>30° z=+3.92), §D (107.5°), §C (0.191%). |
| Structure battery numbers: env $\chi^2$ $z=-0.38$, trend $+0.17$; anomaly $-2.37\sigma\to-1.05\sigma$; redshift trend $-1.63$; CMB axes $+0.21$, $-0.13$; free fit $0.44\%$ vs $0.38\%\pm0.16\%$, $z=+0.32$ (ll.1042–1049, Table 7 p.11) | All match `ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md` §2/§3 (0.437% vs 0.385%±0.162%). |
| BGS Table 8 (p.11): all six $N$, $f_{\rm CW}$, binomial $\sigma$, and $z$ entries | Exact match to `ROW16IVB_BGS_ENVIRONMENT_2026-09-05.md` §2. |
| BGS spec-z $\chi^2$: obs 1.872 vs null 1.984±1.841, $z=-0.06$, $p=0.952$; rotation null $z=-0.12$, $p=0.917$; per-bin dipoles $\vert z\vert\le2.15$; largest excursion $z=+2.96$, $p_{\rm local}=0.0060$, $p=0.084$ after ×14 (ll.1111–1121) | All match source §2/§3. I recomputed $0.0060\times14=0.084$ ✓. |
| Internal arithmetic (older content) | $1{,}592{,}107+1{,}609{,}053+5{,}273{,}371=8{,}474{,}531$ ✓; $949{,}584-59{,}515=890{,}069$ ✓; $454{,}968/887{,}472=0.5126562$ ✓; Table 3 row sums $=240{,}919$, three-class accuracy $58.71\%$ ✓, 2-class agreement $69.911\%$ ✓, and I independently recomputed Cohen's $\kappa=0.3978\approx0.40$ ✓; Fisher floor $\sqrt{3/3{,}201{,}160}=9.68\times10^{-4}$ ✓; Table 5 ratios 7.1/5.1/2.0/2.0/20.4 ✓; $g=0.398$ bridge does drop exactly the two $2$–$4\%$ rows below $0.98\%$ ✓; void cascade $31{,}937+113{,}829=145{,}766$ ✓; T-Web $428+6{,}673+408{,}187+397{,}505=812{,}793$ ✓; void CI $0.00145\pm1.96\times0.00332=[-0.00506,+0.00796]$ ✓ and two-sided $p=0.662$ ✓. |
| Compile hygiene | `main.log`: 0 undefined references, 0 undefined citations, exactly one overfull hbox (5.88 pt, l.757 → source ll.371–385). Renders of pp.1, 10, 11, 12 at 100 dpi show no column overflow, no overlap, no broken figure/table, and all `\artifact{}` paths wrapping inside the column. |
| Manifest existence | All four manifests cited in Data Availability (ll.1174–1181) exist on disk, as do `reproducibility/manifests/programs/galaxy-chirality.json`, `row16iv-chirality-structure.json`, `row16-image-level-injection-n20k.json`, and `row13-image-level-injection-scale.json`. |

The new material is therefore **numerically faithful at the level of individual transcribed values**. The defects below are about attribution, selection disclosure, internal consistency, and one substantive science implication — not about fabricated numbers. I found **no fabricated value and no invented derivation** anywhere in the new content.

---

## PART A — MAJOR findings

### MAJ-1 — The new pixel-level calibration measures an observed-to-physical parity transfer ~10× smaller than the bridge factor the exclusion depends on, and the paper does not confront it. This bears directly on the headline result.

**Location:** ll.985–997 + Table 6 (p.10); interacts with ll.493–501, ll.776–783, and Assumption 2 at ll.832–838.

The paper's central claim (Sec. 5, Abstract, Conclusions) is that $A_{95}^{\rm obs}\simeq0.98\%$ disfavors alignment-driven dipoles "a factor of $2$–$20$ below" the $2$–$33\%$ literature amplitudes. The paper is scrupulous that $A_{95}^{\rm obs}$ is an **observed-label** statement and that the observed-to-physical bridge is an open gate (Assumption 2), and it already discloses that under the illustrative bridge $g=0.398$ two of five rows fall below the floor.

The new pixel-level injection is the first *direct empirical measurement* bearing on exactly that bridge: a true mirror-flip of raw pixels pushed through the production equivariant classifier returns $dA/df=+0.0167$ where the label-identity model predicts $+0.4343$. The implied response ratio is

$$0.0167/0.4343 = 0.038\,,$$

i.e. **an order of magnitude smaller than the illustrative $g=0.398$** the paper carries. Propagating it naively, an observed-label floor of $0.98\%$ corresponds to a physical parity amplitude of $0.98\%/0.038 \approx 25\%$ — under which *every* row of Table 5 except Shamir (2025) falls below the floor and the exclusion statement of Sec. 5.3 does not survive.

Instead of confronting this, ll.994–997 read the same measurement in the reassuring direction: "The production pipeline suppresses pixel-level parity leakage well below what the label-level injection model alone would predict, consistent with the baseline residual already disclosed in Sec. [2.2]." Suppression of *leakage* (a systematic entering the labels) and suppression of *signal* (a true sky parity entering the labels) are the same transfer function read in two directions; the paper takes the benign reading only. A referee cannot let a paper whose headline is a sensitivity-based exclusion add a measurement of its own signal transfer function and then discuss only its systematics-suppression interpretation.

I am **not** asserting the exclusion is wrong: $dA/df$ is a response to an injected *mirror-flip fraction* at a particular $A_0$, not a dipole-amplitude transfer on the sky, and the sign structure is genuinely unresolved (see MIN-1). That is precisely the point — the paper must either (a) derive and state the relation between the measured pixel-level response and the $g$ of Assumption 2, with the resulting bound on the exclusion, or (b) state explicitly and with an argument why the pixel slope does **not** constrain $g$. Silence with a one-sided gloss is not acceptable at ApJS. Note also that the two numbers sit ~250 lines apart in the same manuscript and are never cross-referenced.

**Required:** an explicit paragraph relating $dA/df=+0.0167$ to Assumption 2's $g$, and a statement of what the exclusion becomes if the implied transfer is taken at face value.

### MAJ-2 — The full-parent QC attribution is stated backwards; the two quality cuts are swapped relative to the committed source.

**Location:** ll.1021–1024, p.10 ll.707–709 of the render.

Paper: *"A graded QC sweep localizes this to a single cut: removing only the `primary_hc` confidence cut restores the null ($z=+0.68$), while removing only the raw-flip cut does not ($z=+9.13$, at a third, near-antipodal axis)."*

Source (`ROW16IB_AXIS_SHIFT_2026-09-04.md` §A):

| Selection | meaning | $z$ | axis |
|---|---|---|---|
| C1 relax `primary_hc` (`!unsafe` only) | `primary_hc` **removed** | **+9.13** | 168.5°, −73.2° |
| C2 relax raw-flip (`primary_hc` only) | raw-flip cut **removed** | **+0.68** | 294.3°, +16.0° |

and the source's own conclusion: *"The `primary_hc` confidence cut alone **removes the signal** (C2, z = +0.68), while the raw-flip QC cut alone does not (C1, z = +9.13...)"*.

So $z=+0.68$ is the selection that **keeps** `primary_hc`, and $z=+9.13$ is the one that **removes** it. The paper has the two cuts exactly inverted. (That the trailing clause "at a third, near-antipodal axis" correctly describes C1's 168.5°/−73.2° confirms the $z$ values were taken from C1/C2 and only the cut labels were swapped.) As written, the manuscript tells the reader that discarding the confidence cut restores isotropy — the opposite of the measured behavior, and in direct tension with the paper's own next-sentence summary ("signal present only in the population the primary QC cuts are designed to exclude"). This is a factual inversion in a disclosure paragraph whose entire purpose is attribution.

### MAJ-3 — Selective disclosure of the imaging-leg table: the same committed table shows the *primary* (C3) selection failing drop-one-leg stability at $z>4$, and the paper quotes only the full-parent rows.

**Location:** ll.1024–1026 vs `ROW16IB_AXIS_SHIFT_2026-09-04.md` §B.

The paper cites §B for one fact only — that dropping DES removes the full-parent excess ($z=+0.48$). The same table reports drop-one-leg fits on **C3, i.e. the paper's own 887,472-galaxy primary channel**:

| Fit (C3 = primary selection) | $N$ | $A_{\rm obs}$ | $z$ | axis |
|---|---|---|---|---|
| C3 only BASS+MzLS | 208,269 | 3.916% | +2.00 | 248.7°, +56.3° |
| C3 drop BASS+MzLS | 678,781 | 0.658% | +1.02 | 121.0°, +22.2° |
| C3 only DECaLS | 462,750 | 1.657% | +2.20 | 122.2°, −47.1° |
| **C3 drop DECaLS** | 424,188 | **2.211%** | **+4.19** | 319.6°, +10.0° |
| C3 only DES | 215,919 | 5.830% | +2.49 | 359.5°, +0.5° |
| **C3 drop DES** | 671,441 | **1.389%** | **+4.26** | 157.5°, −68.9° |

Two drop-one-leg variants of the *primary* channel reach $z>4$ with amplitudes of $1.4$–$2.2\%$ — above $A_{95}^{\rm obs}=0.98\%$ — and the single-leg fits reach $5.83\%$. Whatever the correct interpretation (reduced $f_{\rm sky}$, mask leakage on a truncated footprint, 2,000-draw nulls), a paper whose result is "the primary channel is null and its floor is $0.98\%$" cannot cite this table for the parent rows and omit the rows that speak to the primary channel's own footprint stability. A reader of the current text would reasonably infer that leg-level instability is confined to the population the QC cuts exclude; the cited source says otherwise.

**Required:** disclose the C3 leg rows with their interpretation, or state on the record why drop-one-leg fits on the primary selection are not a meaningful robustness test (and then explain why the C0 rows *are*).

### MAJ-4 — The new BGS projected channel and the structure battery are run on the HC sample *including* the 59,515 `raw_flip_qc_unsafe` rows the paper excludes as release-unsafe. This is nowhere disclosed, and the sample is mischaracterized.

**Location:** ll.1084–1086 ("the 949,584-spiral photometric/no-redshift subset"), Table 8 lower block (p.11), and ll.1035–1049 (structure battery, whose source sample is also $N=949{,}584$).

Sec. 2.1 (ll.186–189) establishes: $N_{\rm HC}=949{,}584$; **59,515 rows are then excluded** as `raw_flip_qc_unsafe`, leaving 890,069 and thence the 887,472 primary sample. Sec. 2.2 (ll.284–298) states that the HC selection *including* those rows has $f_{\rm CW}=0.496051$, that the strict primary has $f_{\rm CW}=0.5126562$, and that the quarantined rows are **75.2% CCW** — "strongly parity-asymmetric", which is why their removal flips the monopole's sign.

The new BGS projected channel's $N$ is exactly 949,584 — the pre-exclusion number. I confirmed this is not a coincidence by recomputing the occupancy-weighted parity fraction of Table 8's lower block:

```
(189,917×0.49602 + 569,750×0.49680 + 189,917×0.49388) / 949,584 = 0.49606
```

against the paper's own HC-with-unsafe $f_{\rm CW}=0.496051$ and primary $f_{\rm CW}=0.5126562$. The projected channel is unambiguously run on the **contaminated** HC set, not on the paper's science sample. `ROW16IVB` §0.1 confirms the declared input is `primary_hc` + CW/CCW label with no raw-flip cut; `ROW16IV` §1 confirms the same 949,584 for the structure battery.

Three distinct problems follow:

1. **Undisclosed selection.** Two of the four new "robustness and disclosure" results are computed on a selection the manuscript elsewhere declares release-unsafe and strongly parity-asymmetric. The paper says nothing about this. The most consequential excursion in the new material — the projected node-like bin at $z=+2.96$ — sits in exactly the channel carrying a 75.2%-CCW contaminant population, and the reader is given no way to know.
2. **Mischaracterization.** "Photometric/no-redshift subset" is wrong twice: the set is the full HC labelled sample (it *contains* the 121,417 spec-z spirals, so the two rows of Table 8 are nested, not disjoint as the table's layout implies), and it is not defined by absence of a redshift at all.
3. **Unexplained $f_{\rm CW}$ discontinuity.** Every $f_{\rm CW}$ in Table 8 is below 0.5 (0.4939–0.4968) while the paper's primary sample has $f_{\rm CW}=0.5127$. A referee reading Table 8 against Sec. 2.2 sees an unexplained ~1.9-percentage-point jump. The explanation (different selection) is exactly the disclosure that is missing.

**Required:** state the selection explicitly for both new channels, state that the two Table 8 blocks are nested, and either re-run on the strict primary selection or justify not doing so and bound the contaminant's effect on the $z=+2.96$ excursion.

### MAJ-5 — Internal contradiction: the appendix asserts no low-redshift void catalog was available, while Sec. 4 of the same paper uses one and the very next paragraph uses the survey it is built from.

**Location:** ll.1050–1055 vs ll.604–610 and ll.1077–1086.

Appendix: *"...the DESI DR1 LSS products on disk are QSO-only at $z=0.8$–$2.1$ with no overlap with the $z\lesssim0.3$ spiral sample and **no low-$z$ void catalog was available**."*

Sec. 4 opens by testing chirality against "the released DESIVAST void catalog", cited as Rincón et al. (2025), whose title in this paper's own bibliography (l.1270) is *"DESIVAST: Catalogs of **Low-redshift Voids** Using Data from the DESI Data Release 1 **Bright Galaxy Survey**"* — and Eq. 3's headline result is built on VoidFinder hole membership from it. The paragraph immediately following the contradictory sentence then downloads and uses the DESI DR1 BGS clustering catalog.

The source document's scope was "on disk for that run"; the manuscript has flattened it to an unqualified availability claim that its own Sec. 4 falsifies. As written this is a self-contradiction on a data-availability question, and it also makes the item-(iv) environment fallback look unjustified when it was in fact justified (by *product type* — a void-membership catalog vs. a 3D density field with matching $z$ coverage — not by availability).

**Required:** rewrite to the true scope ("no low-$z$ 3D void/filament *membership* product covering this footprint was on disk at the time of that run; the DESIVAST void catalog used in Sec. 4 provides hole membership but not a continuous density field"), or delete the availability claim.

### MAJ-6 — The stated reason for not testing Shamir's axis is unsupported and is contradicted by this paper's own bibliography.

**Location:** ll.1053–1055: *"...and Shamir's claimed axis is not tested, as the sources this paper draws its quoted amplitudes from quote no explicit RA/Dec for it."*

The source document says something materially different (`ROW16IV` §1, §4.2): *"The **P4′ paper** cites Shamir 2012/2020/2022/2025 for **amplitudes only**... it quotes **no explicit RA/Dec** for a Shamir axis. Recorded UNAVAILABLE — not fabricated."* That is a correct statement about an internal provenance chain (the analyst worked from P4′'s quoted amplitudes and would not invent an axis). The manuscript has converted it into an assertion about **the Shamir/Longo literature itself**, which is (i) not what the source supports and (ii) very likely false on its face: the bibliography entry at l.1205 is *"Handedness asymmetry of spiral galaxies with $z<0.3$ shows cosmic parity violation **and a dipole axis**"*, and l.1200 is *"**Detection of a dipole** in the handedness of spiral galaxies..."*. Papers titled that way report axis directions.

This matters beyond wording: the untested axis is the single most directly relevant confirmatory test in the whole structure battery — the paper's thesis is that a preferred-axis claim is not reproduced, and the one axis the claimants actually name is skipped, on a stated ground that the paper's own reference list contradicts. Under the "never fabricate / never paper over a gap" standard this is the correct *handling* (the axis was recorded UNAVAILABLE rather than invented) reported with the *wrong justification*.

**Required:** either read the cited papers and test their published axes (the right answer), or restate the limitation truthfully as an internal-scope limitation of this manuscript's quoted-amplitude-only treatment, without asserting anything about what the sources contain.

### MAJ-7 — Both reproducibility pointers for the new material point at the wrong experiment; the correct manifests exist and are registered.

**Location:** ll.1173–1182 (Data Availability itemization, p.12).

| Paper bullet | Manifest cited | What that manifest actually is | Correct manifest (exists on disk) |
|---|---|---|---|
| pixel-level calibration ($N=20{,}000$, 10 seeds, $dA/df=+0.0167$) | `row13-image-level-injection-pilot.json` | *"Row 13 PILOT ... Status detail: pilot complete, **inconclusive** (raw single-pass model, **N=500**)"* — explicitly superseded in `ROW13_PILOT_2026-09-04.md`'s own header | `row16-image-level-injection-n20k.json` (title: "Row 16 Part A at **N=20,000** ... PRODUCTION equivariant ... resolving the slope comparison outside the noise floor") |
| structure cross-correlations (15-statistic battery) | `p4p-row16ib-axis-shift.json` | "Row 16(i-b) — is the **full-parent chirality dipole** a QC/footprint systematic? Graded QC sweep, per-imaging-leg table, monopole/mask-leakage null" | `row16iv-chirality-structure.json` (title: "Row 16 (iv) — chirality x structure: parity vs environment, anomaly positions, redshift, and preferred axes"), which **is** registered in `reproducibility/manifests/programs/galaxy-chirality.json` |

Consequences: (a) a reader following the paper's own stated reproduction route for the pixel-level calibration lands on the $N=500$, raw-single-pass pilot that the source describes as *"NOT apples-to-apples"* and *"did NOT recover a clean injected-vs-recovered curve"* — it cannot reproduce $dA/df=+0.0167\pm0.0089$; (b) the structure battery, the single largest block of new statistics (15 tests), has **no** correct manifest cited anywhere in the paper, while `p4p-row16ib-axis-shift.json` is double-counted for the full-parent item; (c) `p4p-row16i-full-parent-dipole.json` is cited alone for the full-parent bullet even though most of that paragraph's numbers (graded QC sweep, leg table, 0.19% mask leakage, 107.5° axis shift) come from `p4p-row16ib-axis-shift.json`.

Under directive Q2 (mandatory per-experiment reproducibility manifests) a wrong pointer is functionally equivalent to a missing one. I note this defect originates upstream in `project-context/SSOT/paper-4p/status.md` (the v4P.0.5→v4P.0.6 entry records the pilot manifest for the $N=20$k result), so the fix should be applied in both places.

---

## PART B — MINOR findings

**MIN-1 — "far below both" is arithmetically false for the mixture identity, and the source's own characterization is inverted.** ll.991–993: the measured $+0.0167$ is *not* "far below" $-0.0093$; it is larger in magnitude ($1.8\times$) and opposite in sign. `ROW13_PILOT` §"Part A at N=20k" states the honest reading: *"close in scale but sign-flipped relative to the NOT_SPIRAL-corrected mixture identity, a genuine (not noise-floor) discrepancy worth further modeling."* The paper should say "an order of magnitude below the naive label-identity slope and, against the mixture-corrected identity, consistent in magnitude but sign-flipped at $2.9\sigma$ — an unresolved discrepancy."

**MIN-2 — The pixel test's own baseline is never reported, so the stated consistency cannot be checked.** ll.994–997 claim consistency "with the baseline residual already disclosed in Sec. [2.2]" ($-0.265\%$). The source's baselines are $A_0=-21.72\%$ (full sample) and $+0.59\%$ (spiral-classified), the latter being *opposite in sign* to $-0.265\%$; the source explicitly flags these as "a DIFFERENT statistic than the paper's $-0.26\%$". Report $A_0$, say which statistic it is, and state the sign disagreement.

**MIN-3 — Random-catalog density overstated by ~12×.** ll.1080–1081 and ll.1128–1132 say "4 randoms per cap". `ROW16IVB` §1 and deviation 3: 4 randoms/cap were *downloaded* (~74.7M rows) then uniformly sub-sampled with a fixed seed to $3\times10^{6}$ per cap, $6.0\times10^{6}$ total — which is what the estimator used. The source's own authorized paragraph says "6.0e6 randoms". State the number actually used and the sub-sampling.

**MIN-4 — Transcription error on the projected $\chi^2$ $p$-value.** l.1114 gives $p=0.084$; `ROW16IVB` §2(2) gives $p=0.083$. Compounding the problem, the same paragraph uses 0.084 four lines later for the Bonferroni-corrected node-like excursion ($0.0060\times14$), so the error creates a spurious numerical coincidence between two unrelated quantities.

**MIN-5 — The null family is misdescribed for the axis statistics.** ll.1040–1042: "each tested against 1,000-realization label-shuffle and sky-rotation nulls". `ROW16IV` deviation 3 records that the pre-registered within-pixel label shuffle is *degenerate* for a pixel-level dipole (zero null variance) and was replaced, for the axis tests, by (i) random-axis rotation and (ii) permutation of per-pixel parity means. "Each" is therefore false; name the substituted null.

**MIN-6 — "A pre-registered battery of 15" understates the pre-registration.** 17 statistics were pre-registered; 15 were executed (the Shamir-axis slot being unavailable), and the source deliberately **kept** the $\times17$ Bonferroni threshold rather than loosening to $\times15$. Write "15 of 17 pre-registered statistics ... with the $\times17$ correction retained" — this is strictly to the paper's credit and is currently invisible.

**MIN-7 — The BGS environment bins are not what their names say, and two limitations are undisclosed.** (a) `ROW16IVB` §1 gives median $\delta_k$ per bin as 0.36 / 1.40 / 5.51 (spec-z) and 0.53 / 4.29 / 19.6 (projected): **every bin, including "void-like", is overdense relative to randoms.** The split spans >1 dex of density (real dynamic range) but never reaches underdense environments, so "no dependence of the parity fraction on environment" (l.1078) overstates the reach, and "void-like" invites confusion with Sec. 4's genuine DESIVAST voids. Report median $\delta_k$ per bin and rename to density quintiles. (b) Deviation 5: the projected subset's sky-rotation null ran **10** realizations, not 1,000 (45-min wall-clock guard), giving $p$-resolution ~0.09 — the source says it is "not used as evidence"; the paper should say so rather than be silent. (c) Deviation 2: the spec-z sample was cut 231,549 → 121,417 by the tracer redshift window $0.1<z<0.4$; disclose the cut, not just the final $N$.

**MIN-8 — "the full 3,200,420-galaxy parent" conflates two counts.** l.1019. `ROW16I`: $N_{\rm spiral}=3{,}201{,}160$; 3,200,420 is the subset falling in the $N_{\rm spiral}(p)\ge10$ support. The paper's own Sec. 2.1 uses 3,201,160 for the spiral parent, so the manuscript now carries both numbers for "the parent".

**MIN-9 — Two $z$ values for the identical C0 fit.** The sentence at ll.1019–1024 chains $z=+4.44$ (from `ROW16I`, seed 20260904, $10^4$ draws) to the graded QC sweep, where the same C0 selection gives $z=+4.33$ (`ROW16IB` §A, different null realization). Quote one with its null, or both with the seed difference stated.

**MIN-10 — Abstract parenthetical contradicts the body on which floor is used.** ll.87–89: "with a 95% sensitivity floor $A_{95}^{\rm obs}\simeq0.98\%$ (Neyman 95% CL limit $A_{95}^{\rm CL}\simeq0.75\%$, **the floor used below**)". The body (ll.490–493) is explicit that the confrontation uses $A_{95}^{\rm obs}=0.98\%$, "the more conservative of the two". As parsed, the parenthetical attributes "used below" to the 0.75% Neyman limit. Move the clause or rewrite. (Pre-existing, not new content, but a referee will read the abstract first.)

---

## PART C — NITs (not counted toward the verdict)

- **NIT-1** One residual overfull hbox, 5.88 pt, `main.log` l.757 → source ll.371–385 (bias-tests table region). Below the 10 pt hygiene gate and not visible as column overflow in the p.10/11/12 renders. 0 undefined refs, 13 pages, `\artifact{}` paths all wrap inside the column.
- **NIT-2** Table 2 (p.2) carries non-numeric cells ("lower", "higher$^\dagger$"). Honest, but a table row that quantifies nothing; consider folding into prose.
- **NIT-3** Table 8 (p.11) shows "$f_{\rm CW}\pm$" without the caption identifying the $\pm$ as the binomial $\sigma$ (it is); the caption defines only $z$.
- **NIT-4** l.626: "a declared 13-column linear nuisance basis" followed by nine named terms. Give the 13-column breakdown or say which terms expand to multiple columns.
- **NIT-5** ll.267–270: "no better than the $0.106$ \NS-only baseline plus chance on the CW/CCW split" set against "best three-class validation accuracy $0.5617$" is hard to parse; spell out the arithmetic.
- **NIT-6** ApJS house style would want the new Sec. A.1 material split — the pixel calibration and full-parent behavior are systematics, while the structure and BGS batteries are new null *results*. As one 150-line appendix subsection, four independent analyses read as an afterthought.

---

## PART D — Answers to this board's three specific questions

**Q: Are the new numbers verifiable against their cited sources?**
Yes, at the level of individual values — every quantitative entry in the new content matches `ROW13_PILOT`, `ROW16I`, `ROW16IB`, `ROW16IV`, and `ROW16IVB` (see Part 0), with one 0.083→0.084 transcription slip (MIN-4). All four cited manifests exist. What does **not** verify is the *attribution* layer: two cut labels are swapped (MAJ-2), two manifest pointers are wrong (MAJ-7), one leg-table block is omitted (MAJ-3), one selection is mischaracterized (MAJ-4), and one literature claim has no source (MAJ-6).

**Q: Is the new content internally consistent with the previously-converged v4P.0.4 text?**
Not entirely. MAJ-5 is a flat contradiction with Sec. 4's use of the DESIVAST low-$z$ void catalog. MAJ-4 creates an unexplained $f_{\rm CW}$ discontinuity (0.4939–0.4968 in Table 8 vs 0.5127 in Sec. 2.2) because the new channels silently use the selection Sec. 2.1 excludes. MIN-8 introduces a second number for "the parent". Units, estimator conventions ($A_p$ vs $f_{\rm CW}-\tfrac12$), $\nside$, and terminology are otherwise consistent, and the new material correctly refrains from mixing the \HCRI{}/\FSC{} supports.

**Q: Does the new content change, weaken, or overstate the primary null / science conclusion (SSOT claims "No science-conclusion change")?**
The **primary null itself** ($z_{\rm mom}=+0.635$, $p=0.238$) is untouched and correctly not adjusted — the full-parent excess is disclosed as a systematic and explicitly not subtracted, which is the right handling. So SSOT's claim is defensible *for the null*.

It is **not** defensible for the **exclusion**, which is the paper's headline. The pixel-level calibration is a new measurement of the paper's own signal transfer function whose face-value implication ($g\sim0.04$ vs the $g=0.398$ the paper carries) would move the physical floor to ~25% and nullify Sec. 5.3 (MAJ-1). Separately, the omitted C3 leg rows show the primary channel's own drop-one-leg fits at $z>4$ with amplitudes above $A_{95}^{\rm obs}$ (MAJ-3). Both are robustness-relevant facts introduced or made citable by the new material, and neither is confronted. "No science-conclusion change" was assessed against the null and not against the exclusion; on this board's evidence that assessment is incomplete.

I did not find the new content *overstating* any result in the sense of claiming more than the sources support — the verdict words ("null", "systematic", "consistent") are all source-backed. The failure mode here is one-sided framing and selective citation of sources that are themselves honest.

---

## VERDICT

**major-revisions**

Justification: 7 MAJOR findings, none of which is a fabrication but three of which a referee cannot pass. MAJ-2 is a factual inversion that tells the reader the opposite of the measured QC behavior. MAJ-4 means two of the four new analyses are computed on a selection the paper itself declares release-unsafe and 75.2%-parity-asymmetric, undisclosed and mislabeled (independently verified by recomputing the occupancy-weighted $f_{\rm CW}=0.49606$ against the paper's own 0.496051). MAJ-1 is the substantive one: the new pixel-level calibration is the paper's first direct handle on the observed-to-physical bridge that Assumption 2 leaves open, its implied transfer is ~10× smaller than the $g=0.398$ in use, and at face value it dissolves the Sec. 5.3 exclusion — the manuscript reports the measurement and discusses only its benign interpretation. MAJ-3 (omitted primary-channel leg rows), MAJ-5 (void-catalog self-contradiction), MAJ-6 (unsourced claim about the Shamir/Longo literature, contradicted by this paper's own reference titles), and MAJ-7 (both new reproducibility pointers resolve to the wrong experiment, one of them to a superseded "inconclusive" pilot) are each independently sufficient to require revision.

I want to be explicit about what this verdict is **not** saying. The underlying science in the new sections is real, pre-registered, honestly nulled, and the source documents are unusually candid — `ROW16IB` closes its own positive finding as a systematic under a pre-committed rule, `ROW13_PILOT` calls its own pilot inconclusive, `ROW16IVB` logs five deviations from pre-registration including one that cost it a null. Every number I could check, checked out. The defects are concentrated in the ~40 lines of manuscript prose that summarize those documents: the integration layer lost the direction of one attribution, the identity of one sample, the scope of one availability claim, the provenance of one literature claim, and the addresses of two manifests, and it declined to follow through on the one new measurement that cuts against the headline. Those are all fixable without new compute, except MAJ-1, which needs either a derivation relating the pixel slope to $g$ or a reasoned statement that it does not constrain $g$.

A note on process, not on the manuscript: this content entered the paper across two version bumps with no independent referee pass, after R3 declared convergence and rounds were stopped under directive R2. Six of the seven MAJOR findings are integration/attribution defects of exactly the kind a review pass catches and a self-review does not. Any future bump that adds a new results or disclosure section should re-enter review on the strength of that section alone, regardless of the standing convergence state.

**Recommended path to accept:** fix MAJ-2, MAJ-4, MAJ-5, MAJ-6, MAJ-7 and all ten MINORs as stated (all are text/pointer edits against sources already on disk); disclose the C3 leg rows for MAJ-3; and for MAJ-1 add the explicit $dA/df \to g$ discussion with its consequence for Table 5 stated honestly, even if the consequence is that the exclusion weakens. If MAJ-1 resolves as "the pixel slope does not constrain $g$, for reason X", say so in Assumption 2 where the reader will look for it.
