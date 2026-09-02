# P4′ v4P.0.2 — R2 truth audit (Opus, verdict-blind, source-cited)

- **Round:** `ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2`
- **Manuscript:** `pipelines/p4prime_chirality_test/paper/main.pdf`, sha256 `78936e3610b2d9274e2ba19b8567207b7cd1cb99d9368585d6ff3d78ac9d1db1` — **verified this session** (`shasum -a 256`), 10 pp, v4P.0.2.
- **Legs audited:** Claude INT (major-revisions; 3 MAJOR / 13 MINOR), Grok API `grok-4.3` (REJECT; 10 items), Gemini API `gemini-3.1-pro-preview` (MAJOR REVISIONS; 7 items). **Perplexity ABSENT** — 401 `insufficient_quota`, optional leg, recorded absent, never as zero findings.
- **Findings audited:** 33. **Canonical GENUINELY-NEW-REAL: 21 (6 MAJOR, 15 MINOR).** RE-FLAG-OF-DISCLOSED: 8. FALSIFIED: 2. OPINION/GENRE: 2.
- The Claude leg's PART A closure verification (16/20 R1 items fully closed, R3/R9 partial, R5 page target and R17 open) was **spot-checked and stands**; no R1 closure claim in `SSOT/paper-4p/status.md` is overstated. No arithmetic or transcription error was found in the measurement layer by any leg or by this audit.

---

## Science resolution — the monopole question (Claude MAJOR-1)

**Settled here by direct recomputation from the committed catalog; no new inference needed.**

Recomputed from `pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet`
(8,474,531 rows), reproducing the committed selection `primary_hc && !raw_flip_qc_unsafe` and the
committed estimator support (NSIDE=64, `N_spiral(p) >= 10`):

| sample | N | N_CW | f_CW | monopole |
|---|---|---|---|---|
| Catalog C, all spirals (P4 Table `tab:cw_frac`, l.1283) | 3,201,160 | 1,592,107 | 0.497353 | −0.265% |
| HC, unsafe rows **included** (P4 l.1289; `g4_monopole_mechanism_injection.json` `observed`) | 948,428 (gal-mask) | — | 0.4960514 | −3.9486e−3 |
| HC **strict** selection (890,069 rows) | 890,069 | 456,273 | 0.512624 | +1.262e−2 |
| **Primary supported-pixel channel (887,472)** | 887,472 | **454,968** | **0.5126562** | **+1.2656e−2 (A_p = +2.53%)** |
| quarantined HC rows removed by the strict cut | 59,515 | 14,776 CW / **44,739 CCW** | 0.2483 | — |

**Cause identified:** the 59,515 `raw_flip_qc_unsafe` rows inside the HC selection are **75.2% CCW**.
Removing them — the review-mandated safe cut P4 adopted — moves the HC monopole from
0.496058 to 0.512656, i.e. it **flips the sign**. Both narrated monopoles (0.49735 catalog-wide,
0.49606 HC-with-unsafe) are therefore correct **for their own samples**; the primary channel's own
monopole is a third, unstated number, and it is +2.53% in A_p units — 2.6× A_95^obs = 0.98%.

**Claude's branch (ii) is FALSIFIED.** The Eq. 1 injection baseline is *not* wrong. The generator
(`a95_observed_label_upper_limit_v1_0_265.py` ll.128, 139–141) computes `p_cw_global` from the
**same** strict sample and support it injects into (`n_cw = cw[support].sum() / capacities.sum()`),
so injecting about 0.512656 is correct by construction; A_95^obs = 0.98% and everything downstream
of it (§5's confrontation, the abstract's 2–20×) is **unaffected**. Nor does the monopole bias the
dipole: the uniform-weight real-space estimator fits `A_p = m + a·n̂`, absorbing any constant
monopole into `m`, and P4 l.1289 shows generatively that binomial nulls at p = f_CW^global and at
p = 0.5 give statistically identical dipole-amplitude nulls (1.957e−3 vs 1.935e−3, 0.39σ).

**What survives is real and MAJOR as a disclosure defect** (DP4P-21): the paper reasons about "the
residual handedness monopole" in four places, never states the primary channel's own value, and the
one monopole a reader can extract (0.4974, Fig. 3) has the opposite sign from the sample carrying
the headline null. The parity-asymmetric quarantine (75% CCW) is itself a previously unstated,
checkable property of the released QC flag and belongs in §2. **No new computation is required** —
the table above is derived entirely from committed artifacts and can be transcribed.

## Statistics resolution — the CL construction (Claude MAJOR-2)

Verified: `research/bh_universe_dipole/a95_null_cl_2026_09_02.py` outputs are arithmetically exact
(null mean 0.00362029, sd 0.00164643, 95th pct 0.0066932 = 0.669%, upper-tail 0.2376). The **label**
is wrong: the 95th percentile of the *no-signal* distribution is the acceptance boundary of the test
already reported as rank p = 0.238, not a confidence-level bound on A_dip. §3 l.377–384 calls it
"a genuine 95% confidence-level statement" and §5.3 l.691–693 cites it as such.

**Correct construction available on disk (Neyman inversion of the injection ladder):** the largest
injected A whose recovered-amplitude distribution keeps the observed A_dip = 0.4665% above its 5th
percentile. `per_amplitude` stores only `recovered_amp_p16_p50_p84`. Inverting the **p16** column
(p16 crosses 0.004665 between A = 0.0050 → 0.00384 and A = 0.0060 → 0.00486; linear interpolation
**A ≈ 0.58%**) gives an ~84% one-sided upper limit, **not** 95%. So the honest options are exactly
two: (a) re-run `a95_observed_label_upper_limit_v1_0_265.py` storing the 5th percentile of
`recovered_amp` per amplitude (same 18×2,000-axis grid, no new physics, cheap) and quote the
inverted 95% CL upper limit; or (b) delete the CL claim and rest §3/§5 on the detection-power
statement alone. The estimator is positive-definite with null mean 0.362%, which is why a naive
percentile is a particularly poor stand-in here.

---

## Canonical findings — R2

Severity: MAJOR = must close before convergence; MINOR = editorial/presentation.

### GENUINELY-NEW-REAL — MAJOR (6)

| ID | Claim · location | Verification on disk | Class |
|---|---|---|---|
| **DP4P-21** | Primary channel's own monopole never reported; conflicts in sign with the two narrated monopoles (Claude MAJOR-1) · §2.2 l.232–236, §3 l.340–346, Fig.3 caption, Appendix | Recomputed from the committed parquet: 454,968/887,472 = 0.5126562; quarantine 44,739 CCW / 14,776 CW; P4 l.1283/1289 for 0.497353 / −3.9486e−3. Baseline branch falsified (generator ll.128,139–141) | science (disclosure) |
| **DP4P-22** | "Genuine 95% CL statement" is a null critical value (Claude MAJOR-2) · §3 l.377–384; §5.3 l.691–693 | Null array re-reduced: 95th pct 0.0066932 ✓; `per_amplitude` has no p5 → a true 95% inversion is not yet computed; p16 inversion ≈ 0.58% | science (statistics) |
| **DP4P-23** | 4×4 bootstrap matrix imported without its per-estimator z's; headline real-space dipole z = +2.21 withheld while +0.635 is headlined (Claude MAJOR-3) · §3 l.447–475 | P4 l.1436 verbatim: "z = +2.21 real-space dipole, +0.81 WLS dipole, −0.61 MASTER ℓ=1"; P4′ prints only z = −6.57 | science (selective import) |
| **DP4P-24** | Abstract omits the g-bridge caveat the body says "should not go unstated" (Gemini E1) · abstract l.99–101 vs §5.3 l.652–659 | Abstract text read (l.99–101): "2–20× below the ~2–33% amplitudes", no bridge caveat; JSON `exceeds_A95_obs_after_g_bridge: false` for `shamir2020`, `shamir2022desi` | science communication |
| **DP4P-42** | No column-by-column catalog schema table (DP4P-05 residue; Claude "10 pp" item 1) · §2.1 l.170–209 | Schema is one prose clause; flag semantics (`raw_flip_qc_unsafe`, `primary_hc`, `class_eq`, `do_not_use_for_science`) never defined in-paper | venue/self-containedness |
| **DP4P-43** | Completeness/purity given only as two integrated scalars (~30%/~70%) (Claude item 2) · l.185–188 | Not usable for sample selection; P4 carries the resolved versions | venue/self-containedness |

### GENUINELY-NEW-REAL — MINOR (15)

| ID | Item · location | Verification |
|---|---|---|
| DP4P-25 | §1 l.152 gives the primary N as 890,069, not 887,472 (Claude MINOR-1) | abstract l.87–88 and §3 l.341 both correct; l.151–152 read on disk |
| DP4P-26 | §3 l.345–346 still calls Fig. 1 "the per-pixel HC CW-fraction sky map underlying this fit", contradicting the corrected caption 3 lines later (R1 DP4P-03 **partial-closure residue**) | l.345–346 and caption l.351–358 read; PNG title "8.47M galaxies", colorbar is an asymmetry |
| DP4P-27 | Table 2 omits T5 from a numbered battery; caption says "all seven" (Claude MINOR-3, Gemini N1) | P4 l.1792/1794 gives the honest disposition (circular-coordinate Pearson removed, superseded) — carry it over |
| DP4P-28 | [15] (paper) and [17] (dataset) share DOI 10.5281/zenodo.21461899 (Claude MINOR-4) | bibliography p.10; §2.1 l.200–201; Data Availability l.863–864 |
| DP4P-29 | Table 3 caption "The four rows" — the table has five rows / four statistic families (Claude MINOR-5) | caption l.668 |
| DP4P-30 | Catalog-wide monopole value, its σ and its significance never appear together in body text (Claude MINOR-6) | only 0.4974 inside the Fig. 3 caption; P5 l.1037/1171 for ±0.000279 |
| DP4P-31 | T-Web corroboration rests on a 428-galaxy Void bin; per-class N absent from text (Claude MINOR-7) | 300-DPI Fig. 3: 428 + 6,673 + 408,187 + 397,505 = 812,793 ✓ |
| DP4P-32 | Keywords are MNRAS-style, not UAT terms with identifiers (Claude MINOR-8) | l.110–111 read |
| DP4P-35 | Draft-mode artifacts plus 3 `A float is stuck` warnings and one 5.88 pt overfull hbox (Claude MINOR-11) | `main.log` ll.758/778/799, l.767; `\documentclass[twocolumn,linenumbers]` l.12 |
| DP4P-36 | [11] Popławski (the paper's only source for the observational claim) has no publication status; year/identifier mismatch (Claude MINOR-12) | bibliography p.10; §5.1 l.602–613 rests wholly on it |
| DP4P-37 | "primary HC sample N = 949,584" at §3 l.450–451 collides with the paper's own definition of that phrase (887,472) (Claude MINOR-13) | correct for P4's bootstrap (P4 l.1436 block); rename "pre-QC HC sample" |
| DP4P-38 | Promotional/internal framing "an on-vision test of the model's one directly observable claim" survives at l.146 (Grok N2; DP4P-08 residue) | l.146 read; the internal path itself is gone (grep → 0 in body) |
| DP4P-39 | Internal audit prose "post-review 13-column linear nuisance basis" at l.505 (Gemini E2) | l.505 read; the exploratory disclosure at l.511–512 is fine and should stay |
| DP4P-40 | No frozen commit-hash/DOI pair pinning the manuscript's numbers to a revision (Grok M4; directive Q2) | Data Availability l.859–887 cites DOIs and script paths, no revision pin |
| DP4P-41 | Title asserts "an Exclusion of the Rotating-Black-Hole-Universe Dipole" for a model the paper itself shows has no computed amplitude (Grok E1) | title l.67; §5.1; abstract does carry the closure caveat, the title cannot |

### RE-FLAG-OF-DISCLOSED (8) — closure cited, do not re-open

| Finding | Basis |
|---|---|
| Grok E3 — "not standalone; withdraw the catalog claim" | R1 DP4P-05 Route A executed: schema/selection l.170–209, estimator+null §2.3 l.308–333, injection–recovery table, 4×4 covariance, P5 clustering ladder and five-way void family. Deferrals down to three sentences (l.208, 530, 878). Real residue is DP4P-42/43 only |
| Grok E4 / Gemini E4 — juxtaposed nulls need "not directly comparable" | l.396–399 states the different support, estimator (MASTER-decoupled vs real-space) and null family, and that it does not overturn the primary. Wording nit only |
| Grok M1 — relabel A_95^obs as an observed-label floor | Already so labelled at abstract l.90, §3 l.385–390, assumption list l.708; transfer-function gate disclosed. The CL half is DP4P-22 |
| Grok M2 — remove the ratio column / no calibrated conversion | R1 DP4P-10 closure: caption l.668–673 names the four label families and disclaims like-for-like comparison; g-bridge flip reported l.652–659 |
| Grok M3 — declare exploratory / preregistration | l.511–512 verbatim: "declared after review and inspection of the data and is exploratory, not preregistered"; multiplicity note l.572–578 |
| Gemini E3 — [16] cited by URL with no DOI | Paper states this plainly itself; R1 DP4P-07 partial closure. Submission blocker tracked under DP4P-28 |
| DP4P-33 (Claude MINOR-9) — no ORCID | R1 R15 residue, honestly recorded in SSOT, correctly not fabricated. Submission-kit blocker, not a manuscript defect |
| DP4P-34 (Claude MINOR-10) — numeric citation style | R1 DP4P-17, openly deferred (`\setcitestyle` l.27, hand-rolled bibliography l.901). Mechanical at submission |

### FALSIFIED (2)

| Finding | Verdict |
|---|---|
| Grok E2 — "abstract does not state the support size of the quoted z_mom/p" | **FALSIFIED.** Abstract l.87–89 verbatim: "(N_support = 887,472 of 890,069 quality-controlled rows) is null-consistent (z_mom = +0.635, one-sided p = 0.238)" |
| Gemini M1 — SE 0.00332 inconsistent with CI [−0.00504, +0.00795] | **FALSIFIED** (repeat of R1 Gemini N1). P5 l.1004–1006 committed: 0.00145442 ± 1.959964 × 0.00331502 → [−0.00504302, +0.00795186]; P4′ rounds correctly. Gemini re-derives from the rounded SE |

### OPINION/GENRE (2)

| Finding | Verdict |
|---|---|
| Grok N1 — remove AASTeX draft header / date | NIT, R1 precedent; the typographic half is folded into DP4P-35 |
| Gemini N2 — "brackets" is imprecise because detection fraction is 0.950 at A = 0.98% | NIT. Confirmed 0.9465 → 0.9500 across the 0.96%/0.98% rows; the crossing is attained at the upper endpoint, which is exactly why linear interpolation returns 0.0098. Optional one-word fix |

---

## Closure plan

**Wave 1 — science, no new inference (DP4P-21, 23, 24, 30, 31, 37):** transcribe the monopole
table above into §2.2 with the 75%-CCW quarantine sentence; print all four block-bootstrap z's with
P4's one-sentence reconciliation of +2.21 against +0.635; add the g-bridge clause to the abstract;
put the catalog-wide monopole with σ and significance in the body; add T-Web per-class N with the
Void-bin power caveat; rename the 949,584 sample.

**Wave 2 — one decision, then a small compute step (DP4P-22):** choose (a) re-run the injection
script storing `recovered_amp` p5 and quote the inverted 95% CL upper limit, or (b) drop the CL
claim. Do not ship the current wording either way.

**Wave 3 — venue/scope (DP4P-42, 43):** add the schema table and resolved completeness/purity
(≈1.0–1.25 pp), landing the paper at ~12–13 pp, inside the ≤15 pp allowance.

**Wave 4 — editorial sweep (DP4P-25, 26, 27, 28, 29, 32, 35, 36, 38, 39, 40, 41)** plus the
submission-kit residue (DP4P-33 ORCID, DP4P-34 citation style) at packaging.

## R2-budget note (directive R2)

This is the **second consecutive review round** on P4′. Per directive R2, a third round requires an
intervening **science or scope decision**, not another sweep. Two decisions are on the table and
either one satisfies R2:

1. **The monopole resolution (preferred, and already resolved here):** adopt the finding that the
   primary channel's monopole is +2.53% in A_p units, caused by a 75%-CCW quarantine, that it does
   not propagate to A_95^obs or to the dipole, and disclose it. This is a science decision with a
   settled answer and it removes the only R2 item that could have moved a headline number.
2. **The CL decision (DP4P-22):** re-run the injection for a genuine 95% inversion, or withdraw the
   CL claim — a methodological scope decision.

The remaining findings are presentation, venue-fit and packaging. Once waves 1–4 land, a third round
is justified **only** as a verification pass on the changed text; if it returns nothing but
genre/length/venue items, rounds stop under directive R2 and the paper moves to the publication
phase (directive P).

*Manuscript not edited by this audit.*
