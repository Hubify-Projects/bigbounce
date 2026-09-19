# A3M — R10 CONFIRMATION truth-audit — exact v3M.0.25

**Round label:** `ROUND_2026-09-18-A3M-v3M.0.25-EXACTPDF-c5fe8889-R10CONFIRM`
**Exact artifact:** `research/track_a3_multichannel/paper/main.pdf`
sha256 `c5fe8889766be7f408b5e385f2826af85182ea50b00d4b8142f4db46422ca001`,
md5 `d46166cb88b32009cdc6be59bb620547`, 20 pp — verified identical at
`site/public/papers/a3_multichannel_arxiv_v3M.0.25.pdf` and
`public/papers/a3_multichannel_arxiv_v3M.0.25.pdf` before dispatch.
**Preflight receipt:** `ROUND_2026-09-18-A3M-v3M.0.25-EXACTPDF-c5fe8889-R10CONFIRM/preflight_receipt.json` (PASS, 0 findings).
**Mode:** INT-only (Directive N + Portfolio Decision 2026-09-02 #6). No Codex, no OpenAI API, no browser EXT.
**Auditor stance:** verdict-first. No finding is closed on a reviewer's assertion; every
disposition below cites the file and line it was checked against.

## Legs

| Leg | Model | Verdict (verbatim) | Raw |
|---|---|---|---|
| Grok_brutal | `grok-4.3` | **REJECT** | `../ROUND_2026-09-18-A3M-v3M.0.25-EXACTPDF-c5fe8889-R10CONFIRM_A3M_Grok_brutal.md` |
| Gemini_cosmology | `gemini-3.1-pro-preview` | **MAJOR REVISIONS** | `../ROUND_2026-09-18-A3M-v3M.0.25-EXACTPDF-c5fe8889-R10CONFIRM_A3M_Gemini_cosmology.md` |
| Claude Fable 5.1 INT referee | `fable` sub-agent, verdict-blind, cold read | **MAJOR REVISIONS** (0 ESSENTIAL / 4 MAJOR / 9 MINOR / 5 NIT / 6 verification requests) | `A3M_v3M.0.25_R10_claude_fable_2026-09-19.md` |

The Grok raw was produced by lane L1 before its process ended; the Gemini and Fable legs
had **no raw on disk** and were therefore recorded FAILED and **re-run by this lane** on the
same exact PDF (Gemini wall time 126.5 s). No verdict in this file was recorded from a label.

---

## GENUINELY-NEW-REAL (closed in v3M.0.26)

All four are **residuals of incomplete R9 closures** or a defect at a location R9 did not
reach. None is a physics error: every number in the manuscript that was re-checked this
round reproduced.

### `DA3M-R10-01` — drafting-history / self-referential revision prose survives (directive Q1). MAJOR-lite.
- **Leg:** Gemini E1 (two instances quoted); confirmed independently in source, and **five more
  instances found by this audit that Gemini did not quote**.
- **Verified in source** (`research/track_a3_multichannel/paper/main.tex`, v3M.0.25):
  - `:572` "bounce-window integral, **previously reported divergent with no quoted number, is now
    shown to be finite**"
  - `:592-595` "and the paper's **own previously stated open item** -- whether the transmitted
    amplitude is scheme-independent -- **is answered negatively**"
  - `:615-620` "The nonlinear channel is therefore **no longer an unknown**… **rather than left open**"
  - `:1151` "and **this is no longer only a literature survey**" (+ `:1157` "**has now been** evaluated")
  - `:1537-1541` "**This sharpens, rather than contradicts, the paper's earlier statements**…"
  - `:1655-1659` "scheme-independence, **previously an open question, is now answered negatively
    rather than left unresolved**… **the earlier** ``S2 diverges'' **statement**"
  - `:1737` "The general-$P_{XXX}$ coefficient $\lambda$ **is no longer an open item**"
- **Attribution check (this matters):** the "S2 diverges" report being referred to is **this lab's
  own** earlier finding, not the literature — `research/cubic_bounce_transmission/lane9b_s2_regulation/LANE9B_S2_REGULATION_2026-09-04.md:12,139,153`
  ("Lane (a)/(b) found … a divergent"; "**Sentences the A3M paper should carry (replacing any
  'S2 diverges, a regulator is required' wording)**"). So this is internal revision history, and
  directive Q1 applies; no external attribution is lost by removing it.
- **Why R9 did not catch it:** `DA3M-R9-04` closed *one* drafting-history parenthetical. The
  closure was scoped to that parenthetical rather than to the pattern.
- **Closure (v3M.0.26):** every instance rewritten to state the conclusion directly, with no
  reference to what the manuscript formerly said. The physics content of each sentence is
  unchanged — e.g. `:592` now reads "and the transmitted amplitude is not scheme-independent",
  `:1657` "its apparent divergence in the integrated-by-parts form is a total-derivative
  artefact, not a physical pathology".
- **Fingerprint:** drafting history, previously reported, now shown, no longer an open item, earlier draft, S2 diverges statement, directive Q1, revision-log prose.

### `DA3M-R10-02` — raw repository paths and JSON field names still in the BODY text. MINOR.
- **Leg:** Gemini M1 (six locations quoted); all six confirmed, plus one more.
- **Verified in source** (all **before** the Reproducibility statement, which starts at `:1889`
  and legitimately lists artifacts): `:548-549` `\texttt{lane\_b\_numerical}, \texttt{results.json}
  field \texttt{step\_convergence\_rel}` (Table `tab:s1_after` caption) · `:1026`
  `\texttt{row11\_pbh\_residuals}` · `:1417` `\texttt{row19\_lambda}` · `:1474`
  `\texttt{r9\_perturbativity}` · `:1536` `\texttt{row19\_lambda}, \texttt{results.json} field
  \texttt{scheme}` · `:1740` `(row19\_lambda, …)` · `:1885`
  `\texttt{research/theory\_audit/}…\texttt{a2\_lapse\_monopole\_adjudication\_2026\_09\_07.md}`.
- **Why R9 did not catch it:** `DA3M-R9-05` closed "nine raw artifact paths in body/captions" —
  seven survived, including two introduced by the R9 closure itself (`r9_perturbativity` at
  `:1474` and the `row19_lambda` scheme pointer at `:1536`).
- **Closure (v3M.0.26):** all seven replaced by "(reproducibility statement below)". The
  artifacts remain fully named in the Reproducibility statement, so nothing becomes
  unreproducible; only the body prose is cleaned. Post-edit grep over everything before `:1889`
  returns **0** raw paths/JSON keys (the two remaining hits are a LaTeX comment on line 4 and the
  `tab:lane9c2` label, neither rendered).
- **Fingerprint:** raw artifact path in body, results.json field name, lane_b_numerical, row11_pbh_residuals, row19_lambda, r9_perturbativity, a2_lapse_monopole path, internal bookkeeping in prose.

### `DA3M-R10-03` — the Reproducibility statement contained an instruction to ourselves. MINOR.
- **Legs:** Gemini E2 (ESSENTIAL) and Grok E7 sub-claim (b), independently.
- **Verified in source** `:1988-1991`: "minting that DOI -- and re-pointing this statement at it --
  **is a maintainer action required at the packaging stage, before submission**"; and `:1914-1916`
  "the frozen-release DOI **to be minted at submission**… until then the branch tree is the
  pointer that is guaranteed to resolve."
- **Verdict on the two legs' framing:** Gemini's *characterisation* ("submitted with placeholder
  text") is accurate for the prose; Grok's "**DOIs that do not yet exist**" is **FALSIFIED as a
  hidden defect** — the manuscript states plainly that the DOI is not yet minted, so no reader is
  misled. The real defect is the maintainer-instruction register, not a false citation.
- **Closure (v3M.0.26):** rewritten as a standard data-availability sentence — "a frozen-release
  DOI covering them will be deposited at publication" — with the self-instruction removed. The
  **DOI minting itself remains an open packaging action** (see "Carried" below); it is not closed
  by this edit and is not claimed to be.
- **Fingerprint:** frozen-release DOI, maintainer action, packaging stage, placeholder DOI text, data-availability register.

### `DA3M-R10-04` — `s = 39/16` printed with no derivation and no citation. MINOR.
- **Leg:** Gemini M2, which called it "an uncomputed quantitative claim".
- **"Uncomputed" is FALSIFIED.** The value traces to a committed computation:
  `research/track_a3_multichannel/row19_lambda/row19_lambda.py:60`
  (`L_matter_s(cs, s)` = Li+2016 Eq. (A.19), sound-speed running retained) and
  `row19_lambda/ROW19_LAMBDA_2026-09-04.md:181-182` ("via Li's own Eq. (A.19) that value
  corresponds to a sound-speed running **s = 39/16 = 2.4375** (computed: `2.43750`)").
  **Independently re-derived by this audit** (not taken from the lab note): with
  $\Lambda=((1+c_s^2)(1+2s/3)/(2c_s^2)-1)/3$, setting $\Lambda = 7/(16c_s^2)$ and taking
  $c_s\to0$ gives $(1+2s/3)/6 = 7/16 \Rightarrow 2s/3 = 13/8 \Rightarrow s = 39/16$ exactly.
- **The residual REAL defect** is that `main.tex:1528-1529` joined the two with a bare "i.e.",
  so a referee reading only the PDF cannot verify the step. Same class as several R9 items:
  a correct number whose provenance was not printed.
- **Closure (v3M.0.26):** the sentence now reads "which by Li \textit{et al.}'s
  Eq.~(A.19)~\cite{Li2016} corresponds to a sound-speed running $s\equiv\dot c_s/(Hc_s)=39/16$".
  No new derivation was written into the paper (`/never-fabricate-derivation`); the citation
  points at the published equation the committed script implements.
- **Fingerprint:** s = 39/16, Lambda = 7/(16 cs^2), Li Eq. A.19, sound-speed running, missing citation for an i.e. step.

### `DA3M-R10-05` — the title claimed the no-go without the constant-sound-speed scope. MINOR.
- **Leg:** Grok E1 (raised as ESSENTIAL).
- **Verified in source:** title `:25-26` read "…and a joint $(r,\fnlloc)$ no-go for single-field
  matter bounces" with no qualifier, while the abstract's own italicised claim sentence `:52-56`
  is scoped — "for the full $P(X)$ $k$-essence class **at constant sound speed**" — and `:57`
  states "A time-dependent $c_s(\eta)$ is not covered". The body claim `:1531-1535` carries
  "at constant sound speed ($s=0$)".
- **Verdict: REAL, and the same defect class as `DA3M-R9-02`** (which restored the `λ = s = 0`
  qualifier to the abstract and the claim sentence but not to the title). Under directive R6
  ("every claim stated at exactly its evidential strength") the most-read sentence in the paper
  should not be the least-qualified one.
- **Closure (v3M.0.26):** title now ends "…no-go for single-field matter bounces **at constant
  sound speed**". No scientific content changed; the claim's stated strength now matches the body's.
- **Fingerprint:** title scope, constant sound speed qualifier, s = 0, time-dependent c_s not covered, over-claiming in the title.

---

## FALSIFIED this round — source-cited (do NOT re-open without new evidence)

| Leg item | Claim | Verdict + source |
|---|---|---|
| Grok E3 | The factor-of-two resolution is "a post-hoc normalization step… introduced solely to make the in-in result agree with Li et al."; the "from-scratch" claim is unsupported | **FALSIFIED.** `main.tex:223-232`: the paper introduces **no** normalization step of its own. It reads Cai et al.'s *own* printed shape function (their Eq. 37), finds Cai's *own* three quoted amplitudes are "each exactly twice the corresponding limits of their own printed polynomial, in all three configurations", and locates the slip in Cai's conversion — checked symbolically, uniform across their Eqs. (38)–(41) and Fig. 5. The "from-scratch" sub-claim is the `R9-E4` fingerprint, already falsified: novelty is explicitly narrowed at `:250-256` to the per-vertex attribution and the localization, *not* the amplitude number. |
| Grok E4 | The γ refit is juxtaposed with the NANOGrav posterior without saying they are not directly comparable | **FALSIFIED**, second time (`R9-E6` fingerprint). Table `tab:pta` caption `:699-700` reads verbatim "the official posterior is the primary comparison and the refit is a secondary, differently-conditioned cross-check, **not directly comparable to it**"; body `:700` the same. |
| Grok E5 | The 1.84±0.03 headline is stronger than the body's own calibration permits; the ratio runs 1.61–1.91 | **RE-FLAG-OF-DISCLOSED, not a defect.** The range Grok quotes is the paper's own printed 255-point scan range (`:1029` "$1.83\pm0.05$ overall (range $[1.61,1.91]$)"), and the same sentence Grok objects to already carries "must not be quoted as universal" (`:977`, `:982`, `:1034`) plus a "Regime of validity" paragraph (`:984-990`) and an explicit statement of which grid the headline comes from and why (`:1023-1038`). |
| Grok E7 (a) | Remove every URL, hash and the reproducibility statement from a journal submission | **OPINION/GENRE.** No PRD rule is cited and none exists; PRD carries data-availability statements, and directive Q2 mandates the manifest. |
| Grok E7 (b) | "frozen-release DOIs that do not yet exist" | **FALSIFIED as stated** — the manuscript says so itself (`:1914-1916`). The register defect that *is* real is `DA3M-R10-03`. |
| Grok E7 (c) | "commit hashes dated after the paper's own submission date" | **FALSIFIED.** `grep -nE "commit \`?[0-9a-f]{7,40}\|/commit/\|[0-9a-f]{40}"` over `main.tex` returns exactly one 40-hex token, `:1983-1984` — the **SHA-256 checksum of the NANOGrav-derived chain file**, split in two for line-breaking, not a commit hash. The R9 closure (`DA3M-R9-01`) removed the commit pin in favour of branch trees, and `:1911-1913` states why. |
| Grok M3 | The injection test uses 5 realizations with no coverage check, so "unbiased" is unsupported | **RE-FLAG-OF-DISCLOSED.** `:769-778` states Grok's objection in the paper's own words: "what this establishes is \emph{bias}, not \emph{coverage}: four of the five realizations at each injection are bootstrap bin-resamples of a single re-centred dataset rather than independent noise realizations", and names the per-realization scatter (0.10–0.12σ) as "comparable to, not smaller than" the threshold. Closed at R9 as `R9-21`. |
| Grok M4 | Fig. 1 plots γ = 5.07 while the text says γ = 5.00 — internally inconsistent | **FALSIFIED**, second time (`R9-M3` fingerprint). `:805-806` prints **both** as a labelled bracket ("$\gamma_{\rm pred}=5.070\ (n_s=0.9649)$", "$\gamma_{\rm pred}=5.000\ (n_s=1$ dust bracket$)$"), and the Fig. 1 caption `:871` prints "γ_pred = 5.07 (5.00, dust)". Two anchors of one quantity, not a contradiction. |
| Grok M5 | The FIRAS argument is "uncomputed" — the model's own spectrum is never folded through the FIRAS window | **FALSIFIED.** `:1170-1172`: "the lab's own prediction gives $\mu=1.65\times10^{-8}$, safely allowed at $1.8\times10^{-4}$ of the bound", computed in `inlab_delta2_zeta_2026-09-03.py`. The separate SMBH-seed statement is about the *required* amplitude and is stated two-part at `:1179-1184`. |
| Grok m1 | "Dated: September 18, 2026" is a future date | **FALSIFIED**, third time (`R8`, `R9-E1` fingerprint). It is the true compile date; the PDF was compiled 2026-09-18. |
| Grok m2 | "exactly" repeatedly precedes values that differ at the third digit | **FALSIFIED — no instance offered and none found.** All 23 uses of "exactly" in `main.tex` are exact-arithmetic claims (`:44` $n_s=1$ exactly for pure dust; `:111` "exactly one half"; `:227` "exactly twice"; `:322` "reproduces $-35/16$ exactly"), and where exactness fails the paper says so: `:900` "(ratio $1.68$, **not exactly** $2$)". |
| Grok m3 | Table II's S1/S2 columns never state that S2 is omitted because divergent | **FALSIFIED**, and misdescribed. The table is `tab:s1_after`, whose caption `:541-543` states the S2 row's scheme and that it "is not directly comparable to the S1 rows above it (different scheme, no separately regulated $\Delta\fnl^{\rm bounce}$)", and `:600-606` gives the actual reason no S2 bounce term is reported — the raw-form integral is **not bounce-localised** (an O(1) window-convention dependence), *not* divergence. |
| Grok n1 | "matter bounce" and "matter-contraction" used inconsistently in one paragraph | **FALSIFIED.** They are distinct defined objects: `:76-77` defines "the matter-bounce scenario — a dust-dominated contracting phase matched through a nonsingular bounce"; "matter contraction" names the contracting phase alone. |
| Grok n2 | Fig. 2's y-axis lacks units | **FALSIFIED / self-refuting.** The axis is `$f_{\rm PBH}$` (`pbh_compaction_fnl.py:608`), a dimensionless mass fraction; Grok's own text concedes it "is pure number". |
| Grok n3 | arXiv:1905.05697's journal citation is missing its volume number | **FALSIFIED.** `main.tex:2151` reads "Astron. Astrophys. \textbf{641}, A9 (2020)" — volume 641 is present. |
| Gemini N1 | "$r\simeq1.8$ is $49\times$ BICEP/Keck" — 1.8/0.036 = 50, so it should read 50× | **FALSIFIED.** Both numbers are roundings of the same computed quantity: `r9_perturbativity/results.json` → `backgrounds/lqc/r_at_floor = 1.7620247…` (the minimum across the three backgrounds; quintin 1.8911, poly 1.8472). 1.7620/0.036 = 48.9 → 49×. Gemini's own alternative ("leave as is if r = 1.764 was the intended exact value") is the correct reading. |
| Gemini M2 (framing) | The $s=39/16$ claim is "uncomputed" | **FALSIFIED** — see `DA3M-R10-04`; computed in `row19_lambda.py:60` and re-derived independently here. The citation gap is the real residual and is closed. |

## RE-FLAG-OF-DISCLOSED (no edit; already stated in the manuscript)

- **Grok E6** — "no first-principles argument selects S1 over S2; forecasts are scheme-dependent
  at the factor-of-two level." The paper's position is exactly this and says so: abstract `:40-42`
  "Transmission is **scheme-qualified**: $\fnl^{\rm after}\in[-0.65,-0.50]$ (S1) or $\approx-1.25$
  (S2)"; `:591-592` "S1 and S2 are therefore genuinely physically inequivalent continuations
  through $H=0$"; `:616-618` "every use of $\fnl^{\rm after}$ in this paper carries its scheme
  qualifier". Both values are reported; neither is presented as the robust one. (`DA3M-03` class.)
- **Grok M2** — "the no-go is derived only under constant $c_s$ and $k\eta_B\lesssim10^{-2}$, and
  the paper never quantifies what survives when these are relaxed." The window **is** quantified:
  `:431-444` is a dedicated paragraph ("*Direction of the $k\eta_B$ window*") stating the
  condition is an **upper** bound and what it excludes, and `:444-492` reports an explicit scan
  over $k\eta_B\in[0.1,10]$ on all three backgrounds with the excursion at
  $k\eta_B\approx0.6$–$0.8$ and the squeezed-LQC deficit (3.1–4.4 dex). The constant-$c_s$
  restriction is disclosed in the abstract and at the claim sentence (`DA3M-R9-02` closure) and
  cannot be quantified further without a new computation, which is not fabricated here.

## OPINION/GENRE (venue pass only, no edit)

- **Grok E2** — "no abstract claim may be phrased as an enumerated contribution list" (of the
  abstract's closing sentence). No such PRD rule; contribution sentences are ordinary in the
  journal. Recorded, not actioned.
- **Grok M1** — "20 pages is excessive; recommended maximum 12." PRD regular articles have no
  page cap (`R9-M4` fingerprint, second time).
- **Grok E7 (a)** — see FALSIFIED table.

## Carried as an open packaging action (NOT closed, NOT claimed closed)

- **Frozen-release DOI.** The Zenodo deposit for this work's own code and artifacts has not been
  minted. `DA3M-R10-03` removed the self-instruction from the prose; it did **not** create the
  DOI. This stays an open P-round/maintainer item and is recorded as such in
  `SSOT/paper-a3m/status.md`. Directive P: this is packaging, and it holds the packaging gate
  below complete.

---

## GENUINELY-NEW-REAL from the Fable INT leg (closed in v3M.0.26)

The Fable leg re-ran the four committed sympy derivations, re-derived Cai et al.'s printed
Eq. (37) from the arXiv e-print, checked every Li/Cai/Quintin equation attribution against the
rendered PDFs, and recomputed the transmission, tensor, window, curvaton, PTA, induced-GW,
DESI and survey-reach numbers. It found **no physics error** — and four defects that are
nonetheless real. **Every one was independently re-verified by this audit before closure; none
was accepted from the leg's text.**

### `DA3M-R10-06` — Table V's `f_PBH` columns were not evaluated at the rows' own labels. MAJOR.
- **Independent re-verification.** `research/track_a3_multichannel/r10_tableV_recompute/`
  (new, committed) re-evaluates each row at its labeled $(\Delta, r_pk_p, C_{\rm th})$ using the
  committed functions of `pbh_compaction_fnl.py` unchanged, with the per-row Gaussian
  calibration the caption describes. Result — this lane's own run, matching the leg to three
  significant figures:

  | row | $(\Delta, r_pk_p, C_{\rm th})$ | printed $f_{\rm PBH}(-35/16)$ | recomputed | printed $f_{\rm PBH}(-35/8)$ | recomputed |
  |---|---|---|---|---|---|
  | 1 | (0.35, 0.75, 0.5) | 5.8e-21 | **1.67e-11** | 4.5e-7 | **1.02** |
  | 2 | (0.35, 1.5, 0.5) | 5.3e-107 | 5.32e-107 ✓ | 7.0e-59 | 7.03e-59 ✓ |
  | 3 | (0.50, 1.0, 0.5) | 3.6e-14 | 3.62e-14 ✓ | 1.6e-2 | 1.57e-2 ✓ |
  | 4 | (0.80, 0.75, 0.6) | 3.5e3 | **9.45e5** | 2.2e8 | **6.63e9** |
  | 5 | (0.80, 1.5, 0.4) | 5.8e-9 | **1.91e-14** | 1.6e1 | **3.20e-3** |

- **Cause, traced to source (not inferred).** `pbh_compaction_fnl.py:417-427` computes the
  `gamma_cr_sensitivity` block at `C_TH_BASE = 0.5` for every $(\Delta, r_pk_p)$, so rows 4 and 5
  carry $C_{\rm th}=0.5$ values under $C_{\rm th}=0.6$ / $0.4$ labels; row 1's printed pair is
  `calibrated_amplitude_comparison["C_th=0.4"]` in `outputs/pbh_compaction_fnl.json`
  (`f_PBH` = 5.8246e-21 and 4.5004e-7 exactly), which is the $(\Delta, r_pk_p, C_{\rm th}) =
  (0.5, 1.0, 0.4)$ baseline, not row 1's point.
- **What is unaffected.** The **ratio column is correct in all five rows** (independently
  confirmed) and so is the $n=27$ footer, because the required-amplitude ratio (Eq. 13) is not
  the calibrated-abundance quantity. Every qualitative claim survives the correction:
  $f_{\rm PBH}(-35/16) < f_{\rm PBH}(-35/8)$ in all five rows, and row 4 stays
  non-perturbative with $f_{\rm PBH}\gg1$.
- **Closure (v3M.0.26):** the two columns replaced by the recomputed values, the per-row $A_*$
  ($0.1687$, $0.1054$, $0.1314$, $0.3790$, $0.0963$) added to the caption, and the
  "uncapped ratio" qualifier widened from "the $\gamma_{\rm cr}\lesssim0.8$ rows" to **any**
  entry with $f_{\rm PBH}>1$ (row 1's $1.02$ now needs it). New artifact committed with the paper.
- **Fingerprint:** Table V f_PBH columns, labeled grid point mismatch, C_TH_BASE 0.5, gamma_cr_sensitivity, calibrated_amplitude_comparison C_th=0.4, per-row A_star.

### `DA3M-R10-07` — the DBI "best case $r_{\rm min}=12.6$" used an undeclared criterion, on one background. MAJOR.
- **Independent re-verification.** `row19_lambda.py:46,200` fixes `PLANCK_1SIG = 5.1` and tests
  `abs(f_after(c, L)) <= PLANCK_1SIG`; `results.json → bounce.background` is
  `"Quintin+2015-type"` only. Table VII and the abstract's adjacent "Planck's 95% interval
  needs $c_s\ge0.525$ ($r\ge12.6$)" instead use the asymmetric 95% upper edge $9.3$ over three
  backgrounds. **Two different criteria, two different $\Lambda$ lines, colliding at 12.6.**
- **Recomputed here from the paper's own Eqs. (15)–(17) and Table III's $T_{\fnl}$**, in the
  new committed artifact `research/track_a3_multichannel/r10_window_criterion/` (reproduces the
  leg's numbers exactly):

  | criterion | DBI line | $P\propto X^n$ line | $\Lambda=0$ |
  |---|---|---|---|
  | Planck 95% ($\le9.3$) | **10.31 (LQC)** | 12.60 (Quintin) | 13.27 |
  | Planck 68% ($\le4.2$) | 11.85 (LQC) | 14.97 (Quintin) | 15.84 |
  | Planck $1\sigma$ ($\le5.1$) | 11.48 (LQC) | 14.39 (Quintin) | 15.21 |

  The $P\propto X^n$ 95% entry (12.604, $c_s=0.5251$) reproduces Table VII's own "$\ge0.525$,
  $r\ge12.6$", confirming Table VII is on that line and is internally consistent — the defect is
  confined to the $\Lambda$-scan sentence and the abstract's "best case" clause. A separate
  constant-$\Lambda$ scan over $[-1,1]$ reaches only $r_{\rm min}=11.66$ at 95%, so **DBI remains
  the best case** and the no-go is unchanged in substance.
- **Direction of the correction: against the paper.** The honest headline is *lower* —
  $r_{\rm min}=10.3$ ($286\times$ BK18), not 12.6 ($349\times$). It is quoted that way.
- **Closure (v3M.0.26):** §VIII now names the criterion ($|\fnl^{\rm after}|\le9.3$, as
  Table VII), the background set (all three of Table III), the best case
  ($r_{\rm min}=10.3$ at $c_s=0.430$, LQC-DBI), the 68% figure (11.9 at $c_s=0.494$) and the
  constant-$\Lambda$ best (11.7); the abstract's clause becomes "$r_{\rm min}=10.3$ on the same
  $95\%$ criterion". Fable **m6** (Quintin-only scan) closes with the same edit.
- **Fingerprint:** DBI best case, r_min 12.57 vs 10.3, PLANCK_1SIG 5.1 vs 95% edge 9.3, undeclared criterion, Quintin-only Lambda scan, 349x vs 286x.

### `DA3M-R10-08` — the same tensor amplitude given two incompatible shortfalls. MAJOR.
- **Verified in source and by arithmetic.** `main.tex:836-837` (p. 8): the $r_{\rm after}=24$
  first-order tensor background, $\OmGW^{(1)}h^2(f_{\rm yr})=1.7\times10^{-14}$, "remains
  $8$–$9$ orders of magnitude below NANOGrav's $2.622\times10^{-8}$". `main.tex:1342` (p. 13):
  the same number is "still $10^{6.2}$ below" the same NANOGrav value.
  $\log_{10}(2.622\times10^{-8}/1.70\times10^{-14}) = 6.188$ — p. 13 is right, p. 8 is wrong.
- **Cause.** The "$8$–$9$" is the tensor-vs-**induced** ratio, which the *same sentence* already
  gives correctly as "$9.1$ decades" ($1.70\times10^{-14}/1.45\times10^{-23}=10^{9.07}$); the
  comparator slipped from the induced background to NANOGrav mid-sentence.
- **Closure (v3M.0.26):** p. 8 now reads "$10^{6.2}$ below NANOGrav's $2.622\times10^{-8}$".
- **Fingerprint:** 8-9 orders vs 10^6.2, 1.7e-14, NANOGrav 2.622e-8, tensor-vs-induced comparator slip.

### `DA3M-R10-09` — reproducibility-statement citations that cannot resolve. MAJOR.
- **(c) `r9_perturbativity.log` — VERIFIED REAL.** Cited at `main.tex:1940`; `git ls-files
  research/track_a3_multichannel/r9_perturbativity/` returns only `r9_perturbativity.py` and
  `results.json`. `.gitignore` matches `*.log`, so the file has never been committed on any
  branch and the citation cannot resolve for any reader. **Closed:** citation dropped (the `.py`
  and `results.json` carry the reproduction).
- **(d) `outputs/r11_pbh_residuals.json` — VERIFIED REAL.** Cited at `main.tex:2001`;
  `ls research/track_a3_multichannel/outputs/ | grep r11` is empty and `git ls-files` finds no
  such path on any branch. The artifact that actually carries the 255/144-point scan is
  `row11_pbh_residuals/results/row11_gammacr_extension.json`. **Closed:** path corrected.
  (This is also why `DA3M-R9-20`'s "re-cite Table V to row11_pbh_residuals" landed on a name
  that does not exist — the R9 closure cited the directory's intended output, not its real one.)
- **(a) the public tree does not yet contain this PDF — REAL, but a PUSH GATE, not a paper edit.**
  `origin/main` is behind this lane's local HEAD, so the branch trees the statement names resolve
  to an older manuscript. Nothing in the manuscript can fix this; it is closed by the director's
  push. **Recorded as a hard pre-submission gate below, not as a closed item.**
- **Fingerprint:** r9_perturbativity.log gitignored, outputs/r11_pbh_residuals.json absent, row11_gammacr_extension.json, origin/main behind, branch-tree pointer resolves to an older PDF.

### Fable MINOR/NIT closed in v3M.0.26 (each re-verified here)
- **m1** — "decreases monotonically, slope $\sim0.13$ per unit $\gamma_{\rm cr}$". **REAL.** My own
  OLS over the 255 committed points gives **$-0.197$** ($-0.195$ over the 144 in-window points),
  and grouping the points by (family, $\Delta$, $r_pk_p$) gives **$+0.032$ per $+0.1$ in
  $C_{\rm th}$** (94 pairs, range $+0.017$ to $+0.064$) — so the union is not monotonic.
  Rewritten with the measured slopes and the correct scope.
- **m3** — the 144-point subset described as the model's own spectrum. **REAL (transparency).**
  The 144 points are **78 lognormal + 66 power-law** shapes whose $\gamma_{\rm cr}$ falls in the
  model's interval (counted here from `row11_gammacr_extension.json`); the power-law family alone
  gives $1.839\pm0.031$. Composition now stated in the text.
- **m4** — "the PTA/PBH/reach/injection channels ran in under $6\,$s total". **REAL and false as
  printed:** `outputs/pbh_compaction_fnl.json → wall_seconds = 214.98`,
  `inlab_delta2_zeta_2026-09-03.json → wall_clock_s = 48.70`,
  `ROW11_PBH_RESIDUALS_2026-09-04.md:159` = 1283 s. Replaced with the true per-channel
  wall-clock list (PTA 0.02 s, reach 0.002 s, SIGW 2.7 s, in-lab spectrum 49 s, PBH grid 215 s,
  $\gamma_{\rm cr}$ scan 1283 s).
- **m5** — "a uniform factor-2 slip **at** Cai et al.'s amplitude-conversion step". **REAL
  (over-precise attribution).** What print establishes is that their Eq. (37) under the printed
  normalization gives half of each of their Eqs. (38)–(41); whether the factor entered at the
  conversion or in an unprinted shape function used downstream cannot be decided from print
  (their own Fig. 5 is internally consistent with $-35/8$). Softened to "between their printed
  shape function and their quoted amplitudes", with the undecidability stated. The
  factor-of-two result itself is untouched and was independently re-derived by the leg.
- **m7** — "thirteen decades above the BBN scale" for $T_B\gtrsim6\times10^{9}$–$6\times10^{10}$ GeV.
  **REAL (under-reports the top):** $6\times10^{9}/10^{-3}=10^{12.78}$, $6\times10^{10}=10^{13.78}$.
  Now "thirteen to fourteen decades".
- **m8** — "$r>23$ after it". **REAL:** with the S1 band $\fnl^{\rm after}\in[-0.65,-0.50]$,
  $(r/24)^2|\fnl^{\rm after}|=0.5$ gives $r=21.0$–$24.0$; 23 is not any background's value.
  Now quoted as the band with its table reference.
- **m9** — Table IV's "reproduced from the committed chain". **REAL (provenance clarity):**
  caption now says the chain is this lab's own 2026-05-01 reduction of the NANOGrav 15-yr KDE
  free spectra, so "reproduced" means re-read, not re-sampled.
- **n3** — the hardware string ("Apple M5, 24 GB, macOS 26.5") in a PRD reproducibility
  statement. Replaced by "a single laptop CPU", in the same sentence as m4's fix.

### Fable items NOT closed — with reasons
- **m2 (Ω_DM = 0.674 is $h$, not $\Omega_{\rm DM}$) — RE-FLAG-OF-DISCLOSED.** Same fingerprint as
  the R9 Fable minor-13 re-flag of the R5 disposition. The paper carries a footnote stating the
  substitution, that $0.674/0.264\approx2.55$ rescales every tabulated $f_{\rm PBH}$ and Fig. 2,
  that the *ratio* conclusions are unaffected because $\Omega_{\rm DM}$ cancels, and that the
  model's predicted $f_{\rm PBH}$ is zero in double precision under either normalization. The
  value is retained deliberately for line-by-line comparability with Choudhury et al.'s printed
  Eq. (66). **Not silently kept: kept, disclosed, and quantified.**
- **n1 (Fig. 1's ~5 pt legend/tick labels)** — REAL but requires regenerating the figure;
  **carried to the D-round** (`/paper-design-round`), recorded here so it is not lost.
- **n2 (inline parenthetical inside a numbered display)** — OPINION/GENRE, PRD style preference.
- **n4 (check [19]/[20] for journal references at proof stage)** — carried to the P-round.
- **n5 ("write $0\le T<1/2$")** — **FALSIFIED:** `main.tex:392-393` already reads
  "$0\le T_{\fnl}<1/2$ since $\rho\in(0,1]$", exactly as requested.
- **The 6 verification requests** — recorded; none asserts a defect, and none is closed by an
  edit (`/never-fabricate-derivation`).

---

## Round tally

| class | count |
|---|---|
| GENUINELY-NEW-REAL (all closed in v3M.0.26) | **17** — 4 MAJOR, 1 MAJOR-lite, 12 minor/nit |
| FALSIFIED with a source citation | 15 |
| RE-FLAG-OF-DISCLOSED | 5 |
| OPINION/GENRE | 4 |
| Carried to D-round / proof stage | 2 |
| Open packaging actions (NOT closed) | 2 — frozen-release DOI; push gate |
| **Clean-wave count** | **0** |

## Convergence statement (R10) — NOT CONVERGED; directive R2 budget SPENT

**This confirmation board did not confirm.** R10 was the one board directive R2 permits after
R9 closed real items, and it surfaced **17 genuinely-new-real findings** — including four MAJOR
that no earlier round caught: a table whose numbers did not belong to its own row labels, a
headline window number computed under an unstated criterion on one background, a printed
order-of-magnitude that contradicted the same quantity thirteen pages away, and two
reproducibility citations that cannot resolve for any reader. All 17 are closed in **v3M.0.26**
by real edits backed by two new committed computations
(`r10_tableV_recompute/`, `r10_window_criterion/`).

**No physics error was found in either round.** Every scientific number re-checked across R10 —
the four sympy derivations (byte-identical re-runs), Cai et al.'s Eq. (37) re-derived from the
e-print, every Li/Cai/Quintin equation attribution, the transmission and tensor algebra, the
perturbative floor, the PTA channel end to end, the induced-GW and DESI numbers, the curvaton
algebra, the $s=39/16$ inversion of Li Eq. (A.19) — reproduced. The defects are presentation,
provenance and criterion-labelling; **one of them moved a headline number against the paper**
(DBI $r_{\rm min}$ 12.6 → 10.3) and that is how it is now printed.

**Directive R2: the budget is SPENT.** R9 (board 1) + R10 (the permitted confirmation board) =
two consecutive rounds. **No further board runs on A3M without an intervening science or scope
decision** — that decision is the director's, not this lane's. This lane stops here.

**Readiness stays COMPUTED (cap 75); no cap-95 recommendation is made.** The brief's cap-95
path was conditional on R10 returning zero genuinely-new-real findings. It returned seventeen,
so the automated-review-convergence gate of directive P is **not met** on any exact PDF: the
last board ran on v3M.0.25 and found real items, and nothing has been reviewed on v3M.0.26. The
packaging gate is also incomplete (no frozen-release DOI, no P-round tarball verification this
round). Claiming 95 on this evidence would be exactly the dishonest uplift `/readiness-cap-99`
and directive P forbid.

## Hard pre-submission gates for the director

1. **PUSH.** `origin/main` does not yet contain this manuscript or `r9_perturbativity/`. Until
   the push lands, the reproducibility statement's branch-tree pointers resolve to an older PDF
   for every external reader. This is `DA3M-R10-09(a)` and only the director can close it.
2. **Frozen-release DOI.** Still unminted; the manuscript now promises it as a deposit at
   publication rather than instructing us to mint it.
