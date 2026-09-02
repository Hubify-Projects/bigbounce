# P4′ v4P.0.3 — Claude INT referee leg, R3 (verification pass)

- **Reviewer:** Claude INT leg (independent ApJS referee, verdict-blind)
- **Model:** claude-opus
- **Manuscript:** `pipelines/p4prime_chirality_test/paper/main.pdf`
- **sha256:** `e8b517d22f61ed733dca043ae2b8253eceffd856ffdfc09e65b422c90b3a8200` (computed this session)
- **Pages:** 11 · **Version:** v4P.0.3 · **Date:** 2026-09-02
- **Round:** `ROUND_2026-09-02-P4P-v4P.0.3-EXACTPDF-e8b517d2-R3VERIFY`
- Line numbers are `main.tex` (the compiled source of the bound PDF); page numbers are the bound PDF.

---

## PART A — verification of the 21 canonical R2 items (DP4P-21 … DP4P-43)

**Result: 21/21 closed. 0 overstated closures. 3 closures carry residual quality caveats (noted).**

| ID | Verification | Status |
|---|---|---|
| DP4P-21 monopole disclosure | §2.2 ll.288–312: all three monopoles stated together — catalog-wide $f_{\rm CW}=0.497353$ (with $-9.47\sigma$), HC-with-unsafe $0.496051$, primary $0.5126562$ ($454{,}968/887{,}472$); quarantine $14{,}776$ CW / $44{,}739$ CCW = $75.2\%$ CCW stated as a previously unstated property of the QC flag. Values match the R2 recomputation exactly. | CLOSED (see MINOR-1 on units) |
| DP4P-21 non-propagation | ll.302–312: baseline-by-construction argument (generator draws $p_{\rm CW}$ from the same strict sample/support) and the $A_p=m+\bm a\cdot\hat n_p$ absorption argument, with the generative check ($1.957$ vs $1.935\times10^{-3}$, $0.39\sigma$). Both correct and correctly sourced. | CLOSED |
| DP4P-22 CL relabel + Neyman | ll.462–477: the null's own 95th percentile $0.669\%$ is now explicitly *not* a CL bound and is identified with the $p=0.238$ rank test. Eq. 1 (l.455, `eq:a95_obs`) is labelled "detection-power threshold … not itself a confidence-level bound"; Eq. 2 (l.478, `eq:a95_cl`) is labelled "full-amplitude, Neyman 95% CL". Both labelled exactly as required. | CLOSED |
| DP4P-22 CL value | **Re-run this session** of `research/bh_universe_dipole/a95_upper_limit_2026_09_02.py` (61.7 s, N_AXES=2000): headline reproduction gate passed ($A_{\rm obs}$, $z_{\rm mom}=0.63465$, rank $p=0.237676$ all reproduced), $A_{95}^{\rm CL}=0.7508188\%$, bracket $A=0.75\%\ (p_5=0.0046608)$ → $0.80\%\ (p_5=0.0049291)$, straddling $A_{\rm dip}=0.00466520$. Byte-identical to the committed JSON (deterministic seed); working tree restored with `git checkout --`. Paper's l.478–482 "$\simeq0.75\%$ … bracketed between $0.75\%$, $p_5=0.466\%$, and $0.80\%$, $p_5=0.493\%$" is exact. | CLOSED |
| DP4P-22 construction | Neyman inversion is correct in direction: `invert_p5` (ll.192–205) returns the largest injected $A$ whose recovered-amplitude distribution keeps $A_{\rm obs}$ at or above its 5th percentile — the standard one-sided upper limit for a positive-definite estimator. Injection model, estimator, support and null are imported verbatim from the committed `a95_observed_label_upper_limit_v1_0_265.py`. | CORRECT (see MINOR-5) |
| DP4P-23 bootstrap z's | ll.579–583 print $z=+2.21$ real-space, $+0.81$ WLS, $-0.61$ MASTER $\ell=1$ alongside the monopole's $-6.57$, and distinguish $+2.21$ from the primary null's $z_{\rm mom}=+0.635$. Verbatim match to P4 `chirality_catalog_paper.tex` l.1436. | CLOSED |
| DP4P-24 abstract g-bridge | Abstract ll.101–104: "though under an illustrative, not-adopted-for-strengthening observed-to-physical bridge the two largest comparison samples drop below this floor and that should not go unstated." | CLOSED |
| DP4P-42 schema table | New Table 1 (l.212, p.2). All 11 rows match the released parquet schema exactly (verified by reading `p4_catalog_primary_safe_v1.0.244.parquet` column names). | CLOSED (see MINOR-3) |
| DP4P-43 completeness/purity | New Table 2 (l.245). Faithful to the source: P4 `chirality_catalog_paper.tex` l.563 carries only the integrated scalars plus the $p_{\rm eq}>0.9$ halving, and P4 itself records the resolved curve as an uncomputed extension. The table's honest `$^\dagger$Not separately quoted in the archived release` is the correct disposition. | CLOSED as far as the source allows |
| DP4P-25 intro $N$ | l.154 now reads 887,472. | CLOSED |
| DP4P-26 Fig. 1 sentence | ll.428–431 now describe Fig. 1 as the full 8.47 M-galaxy FSC map with the HC support as a subset — consistent with caption ll.437–443. | CLOSED |
| DP4P-27 T5 | Table 4 l.383 carries an explicit "T5: removed (see caption)" row; caption ll.363–371 gives P4's circular-RA disposition and the superseding $Y_{\ell m}$ regression; "all seven tabulated tests pass". | CLOSED |
| DP4P-28 DOI sharing | ll.982–983 and bibliography ll.1120–1125 distinguish versioned (…899) from concept (…898) DOI and explain the shared record. | CLOSED |
| DP4P-29 "four rows" | l.786: "The table's five rows pool four non-commensurable statistic families". | CLOSED |
| DP4P-30 catalog monopole | l.290–291: value, and per-pixel-independent binomial significance $-9.47\sigma$, in one sentence. | CLOSED |
| DP4P-31 T-Web per-class N | l.642: Void 428, Wall 6,673, Filament 408,187, Cluster 397,505 (sums to 812,793 ✓), with the Void-bin power caveat. | CLOSED |
| DP4P-32 keywords | ll.113–114: UAT terms with identifiers (1560, 1882, 205, 902, 1857). | CLOSED |
| DP4P-35 hygiene | T5 row overfull fixed; the documented residual 5.9 pt hbox and one soft stuck-float warning remain, both under the hygiene gates and disclosed in SSOT. | CLOSED (documented residue) |
| DP4P-36 Popławski status | l.1082: "arXiv:1910.10819 (preprint, posted October 2019; no journal publication…)". | CLOSED |
| DP4P-37 949,584 rename | ll.554–555: "pre-support-cut HC sample $N=949{,}584$ — distinct from this paper's own $887{,}472$-galaxy…". | CLOSED |
| DP4P-38 "on-vision" | grep → 0 hits in body. | CLOSED |
| DP4P-39 "post-review" | grep → 0 hits; the legitimate exploratory/not-preregistered disclosure survives at l.627. | CLOSED |
| DP4P-40 revision pin | Data Availability ll.1005–1011: manuscript version + git-tracked source URL + versioned Zenodo DOI. | CLOSED |
| DP4P-41 title | Title ll.67–69 now reads "…and a Sensitivity Confrontation with the Rotating-Black-Hole-Universe Prediction". | CLOSED |

R1-era residue **R17** (numeric citation style) remains openly deferred to packaging, as recorded.

---

## PART B — fresh referee read of v4P.0.3

No MAJOR. Five MINOR, of which four are substantive and one is presentation.

**MINOR-1 (SUBSTANTIVE) — the monopole values are quoted in a different unit convention from every other amplitude in the paper, without saying so.**
Location: §2.2 ll.288–301 vs §2.3 ll.394–396 and Fig. 1 caption l.439.
Defect: the paper's own field convention is $A_p=(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})=2(f_{{\rm CW},p}-\tfrac12)$ (caption l.439), and the estimator fits $A_p=m+\bm a\cdot\hat n_p$ — so the fitted monopole $m$, like $A_{\rm dip}$, $A_{95}^{\rm obs}$ and $A_{95}^{\rm CL}$, lives in $A_p$ units. The three monopoles are instead quoted as $f_{\rm CW}-\tfrac12$: $-0.265\%$, $-0.395\%$, $+1.2656\%$ — a factor of two smaller than the $m$ the very next sentence ("absorbing any constant monopole into $m$", ll.307–309) refers to. In $A_p$ units the primary channel's monopole is $+2.53\%$, i.e. $2.6\times$ the $0.98\%$ detection floor quoted 150 lines later. A reader comparing "$+1.2656\%$ monopole" against "$A_{95}^{\rm obs}\simeq0.98\%$" is comparing mismatched units. No result changes — the non-propagation argument stands either way — but the disclosure that DP4P-21 was raised to obtain is stated in the one convention that under-reads it by 2×. Fix: state both, or state the convention explicitly in the same sentence.

**MINOR-2 (SUBSTANTIVE) — Data Availability names a catalog column that does not exist.**
Location: l.1000 ("a `dr8_id` identifier") vs Table 1 l.221 (`object_id`).
Evidence: the released parquet `pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet` has columns `['object_id','ra_deg','dec_deg','class_eq','score_cw_eq','score_ccw_eq','score_ns_eq','score_eq_max','is_spiral','primary_hc','raw_flip_qc_unsafe']` — no `dr8_id`. Table 1 is right; Data Availability is wrong and contradicts it two pages later.

**MINOR-3 (SUBSTANTIVE) — Table 1 renders one column name as two schema rows.**
Location: Table 1, p. 2 (source ll.230–231).
Defect: `raw_flip_qc_unsafe` is typeset as a manual line break across two table rows, so the rendered table lists `raw_flip_` and `qc_unsafe` as two separate columns, neither of which exists. Verified by 300 DPI render of p. 2 and by `pdftotext -layout`. In a table whose sole purpose (DP4P-42) is self-contained schema specification, this misstates the schema. The same row set also breaks the `class_eq` description mid-line ("Equivariant-TTA        label:"). Fix: `\texttt{raw\_flip\_qc\_unsafe}` in a `p{}` column or `\allowbreak`.

**MINOR-4 (SUBSTANTIVE) — the cited CL artifact's own docstring contradicts its code.**
Location: `research/bh_universe_dipole/a95_upper_limit_2026_09_02.py` ll.34–37, cited from the paper at l.480.
Defect: the docstring states "N_AXES is reduced from the committed 2000 to keep local wall time inside the ~60-minute budget (this is a statistical precision tradeoff … stated explicitly in the output JSON)", while l.72 sets `N_AXES = 2000` and the output JSON's `n_axes_note` correctly says no tradeoff was needed. A reader auditing the paper's new headline equation reads the stale claim first. Under directive Q2 the manifest/script documentation is part of the deliverable. Fix: delete the stale paragraph.

**MINOR-5 (SUBSTANTIVE) — the genuine 95% CL limit lies below the sensitivity floor, and this is not remarked on.**
Location: §3 ll.478–487; §5.2 ll.764–772.
Defect: $A_{95}^{\rm CL}=0.75\%$ is *tighter* than the detection-power floor $A_{95}^{\rm obs}=0.98\%$, because $A_{\rm dip}=0.467\%$ is a downward fluctuation of a positive-definite estimator whose null mean is $0.362\%$. This is the classic regime in which a raw Neyman upper limit undercovers relative to the experiment's sensitivity (the standard motivation for a unified/Feldman–Cousins or CLs construction). The paper's science conclusion is unaffected and in fact conservative — §5 confronts the black-hole-universe claim with the weaker $0.98\%$ floor, not the tighter CL — but a referee will ask why the tighter limit is quoted and then not used, and whether the construction is protected against the empty-interval regime. One sentence stating that the CL limit falls below the sensitivity and that §5 therefore uses the power floor would close this.

**NIT (GENRE/PRESENTATION, not counted) —** the abstract (l.100) and §5.2 (l.771) pair "a factor of $2$–$20\times$ below" with "$\sim2$–$33\%$ amplitudes". The Ratio column of Table 5 is computed from each row's *lower* amplitude endpoint (e.g. Shamir 2025: $20\%/0.98\% = 20.4$), so the 33% endpoint corresponds to $\sim33\times$. The choice is conservative, but the convention should be stated in the caption.

---

## Verdict

**minor-revisions**

Justification: every one of the 21 canonical R2 items is closed with real, source-verifiable edits — I re-derived the monopole disclosure numbers against the R2 recomputation, matched the restored bootstrap $z$'s verbatim against P4 l.1436, matched Table 1 against the released parquet schema, and independently re-ran the Neyman inversion, which reproduces $A_{95}^{\rm CL}=0.7508\%$ and its $[0.75\%,0.80\%]$ bracket exactly, with the committed script's headline reproduction gate passing. Both new equations are labelled exactly as the R2 audit required, and the previously mislabelled "genuine 95% CL statement" is now correctly identified as the null's acceptance boundary rather than merely supplemented. Nothing found in this pass changes a number, a conclusion, or the paper's scope. What remains is a unit-convention disclosure defect on the monopole (MINOR-1), two factual/typesetting errors in the new self-containedness material (MINOR-2, MINOR-3), a stale docstring in a cited artifact (MINOR-4), and one missing sentence of statistical context on the new CL (MINOR-5) — all closable without new computation.

Substantive findings remaining: 5
