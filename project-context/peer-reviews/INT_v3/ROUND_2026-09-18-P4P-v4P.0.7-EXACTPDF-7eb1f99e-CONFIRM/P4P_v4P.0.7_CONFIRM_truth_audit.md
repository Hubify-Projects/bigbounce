# P4′ v4P.0.7 — exact-version confirmation board, truth audit (v4P.0.7 → v4P.0.8)

- **Round:** `ROUND_2026-09-18-P4P-v4P.0.7-EXACTPDF-7eb1f99e-CONFIRM`
- **Reviewed PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf`, v4P.0.7, sha256
  `7eb1f99ecc5e3d50a90457997e075873750eff0902ac95eadf9e430d27729a9d`, 13 pages.
- **Why this board ran:** R3 (2026-09-02) converged v4P.0.4 with 0 genuinely-new-real
  findings and rounds were declared stopped per directive-R2. v4P.0.5–v4P.0.7 then
  added three new disclosure results (pixel-level calibration, full-parent selection
  behavior, structure cross-correlations, row-16(iv-b) BGS external environment) across
  two version bumps with **no independent review**. This board is the first review of
  that content, per campaign 2026-09-18 lane L4, criterion A1′.
- **Legs run:** (1) Grok API (`grok-4.3`, rasterized-PNG native input), (2) Gemini API
  (`gemini-3.1-pro-preview`, native PDF + pass-2 self-critique), (3) Claude opus INT
  referee sub-agent (full repo/source access, verdict-blind). Codex/OpenAI paused
  (directive N); Anthropic/Claude leg here is the lab's own sub-agent per the
  2026-09-02 N-amendment, not the disabled Claude-Code-subscription-as-external-reviewer
  route.
- **Raw receipts:** `API_P4P_Grok_brutal.md`, `API_P4P_Gemini_cosmology.md`,
  `P4P_claude_confirm_leg.md` (all in this round directory).

## Verdict matrix (words are diagnostic, not the gate — directive P)

| Leg | Verdict | MAJOR/ESSENTIAL | MINOR | NIT |
|---|---|---|---|---|
| Grok (`grok-4.3`) | REJECT | 3 | 2 | 1 |
| Gemini (`gemini-3.1-pro-preview`) | MAJOR REVISIONS | 9 (5 pass-1 + 4 pass-2, one of which merges into MAJOR count) | 2 | 1 |
| Claude opus INT (verdict-blind) | major-revisions | 7 | 10 | 6 |

## Disposition method

Every MAJOR/ESSENTIAL finding was checked directly against the cited source document,
manifest, or paper text by the orchestrator (not just accepted from the reviewer),
per `/never-fabricate-derivation` and the campaign's standing truth-audit rule. Genre/
convention objections were checked against `project-context/peer-reviews/DISPOSITIONS/P4P.md`
fingerprints from R1/R2/R3 before being re-dispositioned.

## GENUINELY-NEW-REAL — closed in v4P.0.8

All seven independently confirmed against source; six are prose/attribution/pointer
defects closable without new computation, one (MAJ-1) is a science-honesty disclosure.

| ID | Finding | Verification | Fix in v4P.0.8 |
|---|---|---|---|
| **CONFIRM-1** (= Claude MAJ-2) | Full-parent QC attribution inverted: paper said removing `primary_hc` restores the null (z=+0.68); source (`ROW16IB_AXIS_SHIFT_2026-09-04.md` §A) shows z=+0.68 is C2 (raw-flip cut removed, `primary_hc` **retained**), and z=+9.13 is C1 (`primary_hc` **removed**) | Independently re-read source table lines 90-95: confirmed exact inversion | `main.tex` full-parent paragraph: swapped which cut is attributed to which z-value |
| **CONFIRM-2** (= Claude MAJ-3) | Source's per-imaging-leg table (§B) reports the primary C3 (887,472-galaxy) channel's own drop-one-leg fits reaching z=+4.19 (drop DECaLS, A=2.21%) and z=+4.26 (drop DES, A=1.39%), both above A₉₅ᵒᵇˢ=0.98%; paper quotes only the C0 (full-parent) leg rows | Independently re-read source table lines 104-116: confirmed exact C3 rows and values | Added disclosure sentence after the full-parent QC paragraph reporting the C3 leg instability, explicitly not subtracted from the primary result |
| **CONFIRM-3** (= Claude MAJ-4) | New BGS-projected channel and structure battery run on N=949,584 `primary_hc`-labelled sample (pre-raw-flip-QC-exclusion), not the 887,472 primary channel; mislabeled "photometric/no-redshift subset" when it is the full HC-labelled set nesting the 121,417 spec-z rows | Independently confirmed `ROW16IVB_BGS_ENVIRONMENT_2026-09-05.md` l.26/117 input = `primary_hc` + CW/CCW label, full sky, N=949,584 (not `!raw_flip_qc_unsafe`-restricted); confirmed 121,417 spec-z subset nests inside 949,584 | Rewrote structure-battery and BGS-paragraph openers to state the exact selection, its relation to the 887,472 primary channel, and the spec-z/projected nesting |
| **CONFIRM-4** (= Claude MAJ-5) | Appendix says "no low-z void catalog was available" while Sec. 4 of the same paper uses the DESIVAST low-z void catalog | Confirmed both passages in `main.tex`; DESIVAST title in the bibliography is literally "Catalogs of Low-redshift Voids" | Reworded to the true scope: no 3D void/filament *membership* product for this run's environment battery; DESIVAST (used in Sec. 4 for a different test) provides hole membership, not a continuous density field, and doesn't substitute here |
| **CONFIRM-5** (= Claude MAJ-6) | Paper states Shamir's axis isn't tested because "the sources this paper draws its quoted amplitudes from quote no explicit RA/Dec for it" — but the paper's own bibliography titles (Longo 2011 "and a dipole axis"; Shamir 2012 "Detection of a dipole...") contradict a blanket claim that the literature reports no axis | Confirmed bibliography entries in `main.tex`; source doc (`ROW16IV`) actually says only that *this manuscript* did not extract an axis from its own citation-only treatment | Reworded to the true, narrower scope: this manuscript's citation-only treatment did not extract an explicit axis, not a claim about what the cited literature contains |
| **CONFIRM-6** (= Claude MAJ-7) | Two of four Data-Availability manifest pointers are wrong: "pixel-level calibration" pointed at `row13-image-level-injection-pilot.json` (an explicitly superseded, inconclusive N=500 pilot), not the actual N=20,000 production manifest; "structure cross-correlations" pointed at `p4p-row16ib-axis-shift.json` (the QC-sweep manifest, actually used by the full-parent item), not `row16iv-chirality-structure.json` | Read both wrong and correct manifest files directly; confirmed titles/content match the claimed swap exactly | Fixed both pointers; full-parent item now cites both of its two real sources (`p4p-row16i-full-parent-dipole.json` + `p4p-row16ib-axis-shift.json`); registered the previously-unregistered `row16-image-level-injection-n20k.json` in `reproducibility/manifests/programs/galaxy-chirality.json` |
| **CONFIRM-7** (= Claude MAJ-1) | The new pixel-level injection slope (dA/df=+0.0167) implies an observed-to-physical transfer ratio (÷ naive identity +0.434) of ≈0.038, roughly 10× smaller than the illustrative bridge g=0.398 used in Assumption 2 of the Sec. 5 exclusion; propagated at face value this would move the physical floor to ≈26%, under which most Table 5 literature amplitudes would fall below rather than above the floor. The paper reported the pixel measurement but discussed only its benign (leakage-suppression) reading, never cross-referencing it against g=0.398 | Recomputed 0.0167/0.434=0.0385 and 0.98/0.0385=25.5% independently; confirmed g=0.398's location (Assumption 2, Sec. 5) and that no cross-reference existed pre-edit | **Science-honesty disclosure added**, not a new derivation: new paragraph after Table 6 states the arithmetic, the ~26% implied floor, and explicitly declines to adopt the propagation (pixel slope is a response to an injected mirror-flip fraction, not a validated on-sky amplitude transfer, and its sign relative to the mixture-corrected identity is itself unresolved — MIN-1 below). States plainly that resolving this requires a validated transfer function not attempted in this manuscript. No science conclusion is asserted either way; the tension is stated, not resolved and not hidden. |

**Directive R2 process note:** six of these seven are integration/attribution defects
of exactly the kind a review catches and self-review doesn't; they entered across two
version bumps with no independent pass after rounds were declared stopped. Any future
disclosure-only bump should still get a bounded confirmation pass on the new section,
regardless of standing convergence state on the rest of the paper.

## GENUINELY-NEW-REAL — closed, MINOR

| ID | Finding | Fix |
|---|---|---|
| Claude MIN-1 | "far below both" false for the mixture identity (opposite sign, larger magnitude, not smaller) | Reworded: "consistent in magnitude but sign-flipped at 2.9σ — an unresolved discrepancy" |
| Claude MIN-2 | Pixel test's own baseline (A₀=+0.59%) never reported; "consistent with the baseline residual" claim compares to a different, opposite-sign quantity (catalog HC monopole −0.265%) | Reported A₀=+0.59% explicitly and stated it is a different, opposite-sign quantity from the HC monopole |
| Claude MIN-3 | "4 randoms per cap" implies ~74.7M rows; estimator actually used 6.0×10⁶ after uniform sub-sampling | Stated both: 4/cap downloaded, sub-sampled to 6.0×10⁶ used |
| Claude MIN-4 | Projected χ² p-value transcribed as 0.084 (source: 0.083), creating a spurious coincidence with the unrelated Bonferroni-corrected p=0.084 four lines later | Corrected to 0.083 |
| Claude MIN-5 | "each tested against label-shuffle and sky-rotation nulls" is false for the axis/dipole-projection statistics, whose label-shuffle is degenerate and was replaced by rotation + permutation nulls | Reworded to name the substituted null for the degenerate case |
| Claude MIN-6 | "pre-registered battery of 15" undersells that 17 were pre-registered, 15 executed, ×17 Bonferroni retained (to the paper's credit) | Reworded to "15 of 17 ... ×17 correction retained" |
| Claude MIN-7(a) | BGS bins labelled void-like/wall/node by relative rank; every bin (including "void-like") is actually overdense vs. randoms in both subsets — the split never reaches genuinely underdense environments | Added explicit disclosure in the BGS paragraph |
| Claude MIN-7(b) | Projected subset's sky-rotation null ran only 10 realizations (45-min wall-clock guard), not 1,000; source states it is "not used as evidence" | Added explicit disclosure with the source's own caveat |
| Claude MIN-7(c) | Spec-z cut 231,549→121,417 by tracer redshift window not disclosed | Added: "cut from a 0.1<z<0.4 tracer-matched 231,549-spiral parent" |
| Claude MIN-8 | "the full 3,200,420-galaxy parent" silently introduces a second number distinct from Sec. 2.1's 3,201,160-spiral parent (a pixel-support-cut subset) | Added explicit clarification of the relationship between the two counts |
| Claude MIN-10 | Abstract parenthetical grammatically attaches "the floor used below" to the 0.75% Neyman limit; body (Sec. 5) uses the 0.98% floor | Rewrote the clause to attach unambiguously to the 0.98% floor |
| Gemini M1 (~= Claude's genre concern) | Table 4 caption narrates internal drafting history ("the former... row, was removed... supersedes it") | Reworded to a plain methods statement, no drafting-history language |

Not independently closed this wave (documented, not silently dropped):

- **Claude MIN-9** (two distinct z-values, +4.44 vs +4.33, for what could be read as
  "the same" C0 selection across two source documents/realizations) — genuinely low
  severity; the paper never actually restates the +4.33 figure, so no direct
  contradiction exists in-text. Deferred; flag for the next wave if the paper ever
  quotes both.
- **Gemini E4 / M2** (add per-statistic effect sizes to Table 7; expand Table 7 from
  7 representative rows to the full 15-of-17-statistic battery) — the underlying data
  exists in `ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md` (confirmed) and this is a real,
  closable-without-new-computation table-construction task, but is out of scope for
  this bounded confirmation pass given its size (the group-(b) angular cross-correlation
  alone is 8 sub-statistics). **OPEN, deferred to the next wave**, tracked here so it
  isn't silently lost.

## RE-FLAG-OF-DISCLOSED — no fix, already addressed by prior rounds

| Finding | Disposition |
|---|---|
| Grok E1 — remove "DRAFT VERSION" / dated title-block strings | **OPINION/GENRE.** AASTeX default draft header; matches actual current date. Precedent: `DISPOSITIONS/P4P.md` line 122 (R2 Grok N1, same finding, same disposition). Removed only at actual journal submission. |
| Grok E2 — internal script paths / `\artifact{}` links are "not acceptable in a journal submission" | **OPINION/GENRE.** `\artifact{}` links to committed reproducibility scripts are the lab's deliberate, standing convention (directive Q2, mandatory per-experiment manifests; CLAUDE.md: "`\artifact{}` macro for repo paths"). Not a defect — the disclosure the lab wants. |
| Grok E3 — "no independent verification of the 0.98%/0.75% numbers" | **RE-FLAG-OF-DISCLOSED.** The exact committed script + seed list + output JSON are already `\artifact{}`-linked in-paper (§Data Availability and inline); this is the same genre objection as E2. |
| Grok E4 / M1 — literature-ratio Table 5 asserts unquantified comparisons | **RE-FLAG-OF-DISCLOSED.** Closed in R1 (DP4P-10, `DISPOSITIONS/P4P.md` line 90-95) and reconfirmed R2 (DP4P-21/22); the g-bridge caveat and incommensurability disclosure are already in the table caption and body. `DISPOSITIONS/P4P.md` line 213: "Grok M2 — remove the ratio column → RE-FLAG-OF-DISCLOSED." |
| Grok M2 — z_mom / FSC harmonic juxtaposed without a "not comparable" caveat | **FALSIFIED.** Checked `main.tex`: "The distinct FSC harmonic diagnostic ... uses a different support" (twice, ll.406-407 and l.507 pre-edit) already states this explicitly, both times the two statistics are mentioned together. |
| Grok M3 — Fig. 1 "no coherent large-scale structure" claim lacks a quantitative ℓ>1 test | **OPINION/GENRE.** Caption already hedges as "visually apparent" (a qualitative caption claim, not a quantitative one), and quantitative ℓ=1 harmonic diagnostics exist elsewhere in the paper (Sec. 2.3, fixed-support multipole vector). |
| Gemini E1 — abstract/body sensitivity-floor contradiction | **GENUINELY-NEW-REAL**, same finding as Claude MIN-10 above; closed once, counted once. |
| Gemini E2 — Table 8 z-scores "mathematically irreconcilable" with $f_{\rm CW}$ direction; p=0.0060 should correspond to z≈2.75 not z=2.96 under a naive Gaussian two-sided test | **FALSIFIED.** Every Table 8 entry (N, $f_{\rm CW}$, σ, z) was independently confirmed byte-for-byte against `ROW16IVB_BGS_ENVIRONMENT_2026-09-05.md` §2 by the Claude leg (Part 0) and again here. The z-values are NOT naive $(f_{\rm CW}-\bar f)/\sigma$ against the 3-bin average — they are reported directly by the source's own null-testing procedure (label-shuffle / rotation permutation nulls per MIN-5 above, not a symmetric-Gaussian binomial null against a simple pooled mean), so a back-of-envelope Gaussian two-sided recomputation from the tabulated σ does not reproduce them and is not expected to. This is a reviewer assumption error about the null construction, not a transcription or arithmetic defect in the paper. |
| Gemini E3 — reliance on unarchived personal-domain URL (Ref. [16], P5) for load-bearing secondary material | **RE-FLAG-OF-DISCLOSED.** Closed in R1 (DP4P-07, `DISPOSITIONS/P4P.md` line 68-74) and reconfirmed (line 215: "Gemini E3 — [16] has no DOI → RE-FLAG-OF-DISCLOSED, the paper states this itself; blocker tracked under DP4P-28"). The paper already discloses the absent DOI and cites the archived manuscript at its served URL explicitly. |
| Gemini M3 — sample-size discrepancy 3,201,160 vs 3,200,420 | **GENUINELY-NEW-REAL**, same finding as Claude MIN-8 above; closed once, counted once. |
| Gemini M4 (pass-2) — "Largest Test" title/abstract claim contradicted by Shamir (2022)'s larger 1.3M sample | **RE-FLAG-OF-DISCLOSED.** Closed in R1 (DP4P-01): abstract already states, in the same sentence as the "largest" claim, "...4–3,400× larger than every comparison catalog in Table 5 **except Shamir's DESI Legacy sample (N=1.3 million)**." The tension is disclosed transparently in the same breath, not hidden. |
| Gemini N1 — misleading significance claim for Cluster bin (Fig. 3 caption) | Not re-verified this wave (Fig. 3 / T-Web content is pre-v4P.0.5, out of this board's charge, which is the v4P.0.5-v4P.0.7 additions); **not dispositioned, carried forward** for a future full R-round rather than fabricated a disposition here. |
| Gemini N2 — missing effect size for sample-purity-ladder excess | Same as above — pre-existing content, out of charge, carried forward undispositioned. |
| Gemini N3 — "typo" in HuggingFace URL (space in `huggingface.co`) | **FALSIFIED.** Source `main.tex` l.1209 (pre-edit numbering) reads `\url{https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog}` with no space. Artifact of the reviewer's PDF line-wrap reading (the `\url{}` macro breaks the URL across the column at render time). |

## Compile / hygiene (directive G)

- `\paperVersion` v4P.0.7 → **v4P.0.8**; `\paperTimestamp` September 5 → **September 18, 2026**.
- 4-pass `pdflatex`: 0 undefined references/citations; one pre-existing 5.88pt overfull
  hbox (below the 10pt hard gate, unchanged from all prior versions).
- Pages: 13 → **14** (new disclosure content).
- `main.pdf` sha256 `e8f1969e415777622561dde0f21a8ac7d6398c3b2ef55f69200ba50a89d91cd2`,
  md5 `b2399780320a50542279c35410b6b545`.
- `pdftoppm -r 110` full-page render, visually inspected pages 1, 4, 8, 10, 11, 12, 13
  (title/abstract, Table 4, Sec. 5 exclusion, pixel-calibration/full-parent
  disclosure, structure-cross-correlation table, BGS table + Data Availability): no
  column overflow, no overlap, all `\artifact{}` paths wrap inside the column.
- Mirrored byte-identical (md5-matched) to
  `pipelines/p4prime_chirality_test/paper/main.pdf`,
  `site/public/papers/paper4prime_chirality_test_v4P.0.8.pdf`,
  `public/papers/paper4prime_chirality_test_v4P.0.8.pdf`,
  `site/out/papers/paper4prime_chirality_test_v4P.0.8.pdf`.
- `reproducibility/manifests/programs/galaxy-chirality.json`: registered
  `row16-image-level-injection-n20k` (previously committed but unregistered).

## Convergence assessment

Zero genuinely-new-real findings remain open from this board (Gemini N1/N2 are
pre-existing content outside this board's charge, not new; Gemini E4/M2's Table 7
expansion is a real but bounded scope-add, not a correctness defect, deferred with
reason). The v4P.0.5–v4P.0.7 disclosure content is now independently reviewed for the
first time and closed to the same bar as the rest of the paper. SSOT's prior "no
science-conclusion change" claim is corrected by this board: it holds for the primary
null (confirmed, unaffected) but did not previously confront the exclusion-relevant
tension now disclosed in CONFIRM-7 — this board's fix makes that tension explicit
in-paper rather than leaving the prior claim overbroad.
