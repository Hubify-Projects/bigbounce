---
title: "Paper A3M SSOT — Multi-channel consistency of the matter-bounce prediction at f_NL = -35/16"
type: ssot
paper: A3M
last_updated: 2026-09-21 -- v3M.0.27. Ledger row 9 (D-A3-9) CLOSED 2026-09-19
(`research/cubic_bounce_transmission/row9_scheme_independence_2026_09_19/`) --
the intervening science decision directive R2 required after the R9+R10
rounds-stop. A scheme-independent Bardeen-potential argument, independently
blind-confirmed by a second construction, resolves the S1/S2 bounce-window
continuation ambiguity in favor of S2 on the Quintin-type background:
f_NL^after is now the single value -1.25 there (was the two-scheme band
[-1.25,-0.50]; S1's range is retained only for LQC/poly, where S2 is not yet
computed), and the tensor no-go strengthens (r_after~9.4e2, 2.6e4x BICEP/Keck,
superseding the S1 24.0/670x headline) -- both directions propagated together
per directive F. Propagated into `main.tex` in the same bundle as a
general-tilt (n_s=1) correction to Appendix A's monopole and squeezed-bispectrum
formulas (gate S12, `research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.md`);
no number this paper headlines changes, since this paper's construction is
exactly at eps=3/2 (dust), where the correction vanishes. Directive-G hygiene
complete. R11 INT board dispatched on this exact v3M.0.27 PDF -- see "R11"
section below for outcome. Readiness stays at the COMPUTED cap 75.
canonical_source: research/track_a3_multichannel/paper/main.tex
canonical_pdf: research/track_a3_multichannel/paper/main.pdf (21 pp / 0 undef refs / md5 ea6ebd918399650702ee5a9c81182ab2 / sha256 3e49f29bdc4bb21ea293db6a2174c4289f1308db2da9b3d96fa1e5192fbbdcef)
version: v3M.0.27 (2026-09-21, row-9 science-decision propagation + gate-S12 correction -- see "v3M.0.27" section below)
registry_id: A3M (project-context/draft_paper_registry.json)
review_profile: PRD-REGULAR
target_journal: Physical Review D (regular article)
headline_pct: 75 (COMPUTED by convex/papers.ts from open findings, capped at readinessCap=75). Directive-P gate status: science 25 done / evidence 25 partial (frozen-release DOI unminted; branch pointers untrue until the push lands) / automated-review convergence NOT MET (v3M.0.27 has not been reviewed by any board until R11) / packaging 20 partial (no P-round this round) / Houston's final 5 not sought. No cap-95 recommendation is made on this evidence.
submission_status: draft, readiness 75 -- row-9 science decision propagated 2026-09-21, unlocking the one board directive R2 permits after an intervening decision (R11). See "R11" section below for outcome.

## v3M.0.27 (2026-09-21) — row-9 (D-A3-9) science-decision propagation + gate-S12 correction; readiness held at 75

**What this bundle was.** Not a review round: the intervening science decision directive
R2 requires before another board can run. Ledger row 9 (D-A3-9) closed 2026-09-19 in
`research/cubic_bounce_transmission/row9_scheme_independence_2026_09_19/` (pre-registration
`117051bd`, result `8d7ede35`, manifest `a3-row9-scheme-independence`); this lane verified
the artifact, applied its printable sentences to `main.tex` exactly, and ran directive-G
hygiene.

**The science.** The Bardeen potential $\Phi$ obeys a second-order equation containing
neither a choice of linear variable $z$ nor any explicit $1/H$; it is regular at $H=0$ and
at the NEC crossing $\rho+p=0$. Written as the $\delta$-function-free first-order
$(\Phi,\Xi)$ system, its automatic continuity across the NEC boundaries is identically
scheme S2's junction condition ($[\zeta]=0$, $[z^2\zeta']=0$) -- no junction prescription
need be imposed. Propagated across the Quintin-type bounce: $|\lambda_\zeta|=0.9699$,
agreeing with S2 to $7\times10^{-8}$ and differing from S1's $6.06$ by 84%. Scheme S1's
$z=a$ is exact iff $\epsilon=-\dot H/H^2$ is constant (true in the matter contraction, false
in the bounce window, which is exactly where the schemes part company). An independent
blind adjudication (a different construction: the $(\Psi,D)$ system with Israel-matching
junctions, given neither this argument nor its conclusion) confirmed S2, $\lambda_\zeta=0.970$.

**Consequence, propagated in both directions together (directive F).** On the Quintin-type
background, $f_{\rm NL}^{\rm after}$ collapses from the two-scheme band $[-1.25,-0.50]$ to
the single value $-1.25$ (favorable to the survey-reach channel), while
$r_{\rm after}=24(\lambda_T/\lambda_\zeta)^2$ takes row-18a's S2 value $\approx9.4\times10^2$
rather than the S1 value $24.0$ (unfavorable -- $2.6\times10^4\times$ BICEP/Keck rather than
$670\times$); the tensor no-go is strengthened, not relieved.

**What is NOT claimed.** Adjudicates the linear MS-variable choice only (the cubic-action
choice -- raw-ADM vs. Maldacena-form -- is settled only indirectly). Computed on the
Quintin-type background only; the LQC and poly backgrounds have $\dot H=0$ crossings not yet
covered, so their rows in Table III/VI remain S1-only and are stated as such throughout.
No claim of refuting an LQC dressed-metric calculation.

**Paper edits (`research/track_a3_multichannel/paper/main.tex`).** Abstract; the
assumption-(A4) transfer-bound paragraph (Sec. III, now scoped to S1 and flagged
superseded on Quintin-type); Table III (`tab:s1_after`) caption relabeled per the
propagation note's option (a) -- S1 rows "superseded ... retained for comparison", S2 row
"this paper's selected result"; the Scheme-S2 closing paragraph replaced verbatim with the
Bardeen-potential argument and the blind-adjudication confirmation; the
"every use of f_NL^after carries its scheme qualifier" sentence rescoped (qualifier dropped
for the linear transfer on Quintin-type, retained for the cubic-action form and LQC/poly);
Sec. VII (tensor) and Sec. VIII (no-go) label S2 as the selected scheme on Quintin-type;
Table VI (`tab:reach`) caption and row labels updated, S2 row now "(selected)"; Discussion
Secs. "joint statement" and "where the consistency is weak" rewritten -- "which scheme's
linear variable is physical at H=0" is no longer stated as an open theory question on
Quintin-type; Next-steps item (i) rewritten from "settling which linear variable is
correct" (answered) to "extending the Bardeen argument to the LQC/poly $\dot H=0$
crossings" (the real remaining gap). Reproducibility statement gains two entries:
`row9_scheme_independence_2026_09_19/` and `psu_gate_S12_translation_trace_2026_09_19`.

**Gate-S12 correction (Appendix A).** `research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.md`
flagged that Appendix A2's printed "both with monopole $-5\epsilon/6$" and Appendix A4's
general-$\epsilon$ in-in bispectrum formula are both $n_s=1$-specific (a constant-$\epsilon$
background is scale-invariant only at $\epsilon=3/2$ and, on the dominant mode, as
$\epsilon\to0$), imported from the same derivation family as `paper_su_criterion`'s Appendix
A3. Both locations now state the $n_s=1$ scope and the general-$n_s$ correction; a
general-tilt gate (in the cited note) proves the correction cancels identically after the
$1/\lambda$ composition, so $f_{\delta N}^{\rm init}=-5$ for every constant $\epsilon$ and
every $n_s$ -- **no number in Sec. II, Sec. `crosscheck`, or Appendix A changes**, since
this paper's entire construction is at the dust value $\epsilon=3/2$, where the correction
vanishes exactly. Sec. II (`sec:parameter`) itself is entirely evaluated at $\epsilon=3/2$
and carried no $n_s=1$-specific general-$\epsilon$ claim; nothing to fix there.

**Directive I6 figure sweep.** Two `\includegraphics` in the whole paper:
`sigw_nhz_from_lab_spectrum_2026_09_04.png` (PTA/GW spectrum) and `pbh_compaction_fnl.png`
(PBH compaction). Neither renders $f_{\rm NL}^{\rm after}$, $r_{\rm after}$, or
$\lambda_\zeta$ -- confirmed by content, not by filename alone. No regeneration needed.

**Directive G hygiene.** `\paperVersion` v3M.0.26 -> **v3M.0.27**, `\paperTimestamp` ->
September 21, 2026; 4-pass pdflatex, 0 errors, 0 undefined references or citations, 21 pp
(grew from 20 -- substantial new text), max overfull hbox 3.9pt (unchanged from v3M.0.26;
one intermediate 116pt table-row overflow from an over-long multicolumn label was caught by
`/latex-audit` and fixed by shortening the label, final residual 2.16pt, invisible). Pages
1, 6, 13, 18, 19 rendered and visually checked -- no column overflow, Table III/VI/Appendix-A
and the reproducibility statement's new entries all fit and wrap correctly. PDF mirrored
byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.27.pdf`,
`public/papers/a3_multichannel_arxiv_v3M.0.27.pdf` and the source dir: md5
`ea6ebd918399650702ee5a9c81182ab2`, sha256
`3e49f29bdc4bb21ea293db6a2174c4289f1308db2da9b3d96fa1e5192fbbdcef`, 21 pp. Convex
`paperVersions:bump` queued to `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`
(Convex disabled, spending limit).

**Open, for the director:** PUSH GATE (`origin/main` must carry the manuscript, this
propagation, and `row9_scheme_independence_2026_09_19/`/`psu_gate_S12_translation_trace_2026_09_19.*`
before the reproducibility statement's branch pointers are true); frozen-release DOI
unminted (P-round action); Fig. 1's ~5pt legend/tick labels (D-round item, unchanged from
v3M.0.26).

## v3M.0.26 (2026-09-19) — R10 confirmation board + closure; ROUNDS STOPPED (R2 budget spent); readiness held at 75

**What this round was.** Directive R2 allows one board plus one confirmation board when the
first closes real items. R9 closed 24. R10 was the confirmation board, run on the **exact
v3M.0.25 PDF** (sha256 `c5fe8889…`, md5 `d46166cb…`, 20 pp, verified byte-identical at both
served mirrors and against the Convex row before dispatch; preflight receipt PASS, 0 findings).
INT-only per Directive N + Portfolio Decision 2026-09-02 #6.

**Leg hygiene.** Only the Grok raw existed when this lane took over; the Gemini and Fable legs
had produced no raw and were therefore **FAILED and re-run on the same exact PDF**, not
back-filled and not recorded from a label. Verdicts: Grok `grok-4.3` **REJECT**; Gemini
`gemini-3.1-pro-preview` **MAJOR REVISIONS**; Claude Fable 5.1 INT referee (verdict-blind cold
read, no prior history) **MAJOR REVISIONS** — 0 ESSENTIAL / 4 MAJOR / 9 MINOR / 5 NIT / 6
verification requests.

**Outcome: the confirmation board did not confirm.** 17 genuinely-new-real (4 MAJOR, 1
MAJOR-lite, 12 minor/nit), 15 FALSIFIED each with a source citation, 5 re-flags-of-disclosed,
4 opinion/genre, 2 carried to D-round/proof. Clean-wave count 0. Full audit:
`peer-reviews/INT_v3/A3M_v3M.0.25_R10_TRUTH_AUDIT_2026-09-19.md`; canonical dispositions:
`peer-reviews/DISPOSITIONS/A3M.md` § "R10 CONFIRM".

**The four MAJORs, all closed in v3M.0.26 and all independently re-verified before closure:**

1. `DA3M-R10-06` — **Table V's `f_PBH` columns did not belong to their own row labels.** Rows 4–5
   carried `C_th = 0.5` values under `C_th = 0.6/0.4` labels (`pbh_compaction_fnl.py:417-427`
   computes the `gamma_cr_sensitivity` block at `C_TH_BASE = 0.5` for every point); row 1 carried
   the `calibrated_amplitude_comparison["C_th=0.4"]` pair, i.e. the (0.5, 1.0, 0.4) baseline.
   Re-evaluated at the labeled points with the committed functions unchanged
   (`research/track_a3_multichannel/r10_tableV_recompute/`, new): row 1 → 1.7e-11 / 1.0,
   row 4 → 9.5e5 / 6.6e9, row 5 → 1.9e-14 / 3.2e-3; rows 2–3 already correct. The **ratio column
   and the n = 27 footer are correct and untouched** (the required-amplitude ratio is not the
   calibrated-abundance quantity), and every qualitative claim survives. Per-row `A_*` now printed.

2. `DA3M-R10-07` — **the DBI "best case `r_min` = 12.6" was computed under an unstated criterion,
   on one background.** `row19_lambda.py:46,200` tests `|f_after| ≤ 5.1` (Planck 1σ) on the
   Quintin-type background alone; Table VII and the adjacent abstract number use the asymmetric
   95% upper edge 9.3 across three backgrounds. Two criteria and two Λ lines colliding at 12.6.
   Recomputed on a common criterion (`research/track_a3_multichannel/r10_window_criterion/`, new):
   the DBI line at Planck 95% gives **r_min = 10.3 (LQC, 286× BICEP/Keck)**, at 68% 11.9; the
   P∝X^n line at 95% gives 12.60, reproducing Table VII exactly, which confirms Table VII is
   internally consistent and localises the defect. **The correction moves the headline against the
   paper and is printed that way.** §VIII now names the criterion and the background set for every
   window number.

3. `DA3M-R10-08` — **the same tensor amplitude carried two incompatible shortfalls.** p. 8 said the
   r_after = 24 first-order tensor (1.7e-14) is "8–9 orders below" NANOGrav's 2.622e-8; p. 13 said
   10^6.2. log10(2.622e-8 / 1.70e-14) = 6.19; the 8–9 is the tensor-vs-*induced* ratio, given
   correctly as 9.1 decades in the same sentence. Fixed on p. 8.

4. `DA3M-R10-09` — **two reproducibility citations that cannot resolve for any reader.**
   `r9_perturbativity.log` is matched by `.gitignore: *.log` and has never been committed
   (citation dropped); `outputs/r11_pbh_residuals.json` exists on no branch — the real artifact is
   `row11_pbh_residuals/results/row11_gammacr_extension.json` (path corrected). A third
   sub-finding, that `origin/main` does not yet carry this manuscript, is a **PUSH GATE** for the
   director and is recorded open, not closed by an edit.

**MAJOR-lite** `DA3M-R10-01`: seven instances of drafting-history / self-referential revision prose
survived R9's closure of one such parenthetical (directive Q1) — the "S2 diverges" statement they
refer to is this lab's own earlier finding, not the literature, so nothing external is lost by
removing it. All rewritten to state the conclusion directly.

**Twelve minor/nit items** closed: raw artifact paths still in body text (`R10-02`, residual of
`DA3M-R9-05`, two of them introduced by the R9 closure itself); the reproducibility statement's
instruction-to-ourselves about minting the DOI (`R10-03`); the missing Li Eq. (A.19) citation for
`s = 39/16` (`R10-04`, value independently re-derived: Λ = 7/(16c_s²) ⇒ s = 39/16 exactly);
**the title's missing constant-sound-speed scope** (`R10-05`, same class as `DA3M-R9-02` at a new
location); the printed ratio slope 0.13 vs the measured OLS −0.20 (`R10-10`); the 144-point
subset's composition, 78 lognormal + 66 power-law (`R10-11`); the false "under 6 s total"
wall-clock claim, corrected to the real per-channel times (`R10-12`); the over-precise
factor-of-two attribution (`R10-13`); BBN decades (`R10-14`); the curvaton r-threshold band
(`R10-15`); Table IV's chain provenance (`R10-16`); the hardware string (`R10-17`).

**No physics error in either round.** Every scientific number re-checked across R10 reproduced:
the four committed sympy derivations (byte-identical re-runs), Cai et al.'s Eq. (37) re-derived
from the arXiv e-print (exactly half of each quoted amplitude), every Li/Cai/Quintin equation
attribution against the rendered PDFs, the transmission and tensor algebra, the perturbative
floor, the PTA channel end to end, the induced-GW and DESI numbers, and the curvaton algebra.

**Directive G hygiene (this bundle).** `\paperVersion` v3M.0.25 → **v3M.0.26**, `\paperTimestamp`
→ September 19, 2026; 4-pass pdflatex, 0 errors, **0 undefined references or citations**, 20 pp,
max overfull hbox 3.90 pt (unchanged from v3M.0.25); pages 10 and 14 rendered and visually
checked (no column overflow, tables and the rewritten §VIII fit). PDF mirrored **byte-identical**
to `site/public/papers/a3_multichannel_arxiv_v3M.0.26.pdf`, `public/papers/…v3M.0.26.pdf` and the
source dir: md5 `4dcb996e0a1252e9dca3c9414a33a213`, sha256 `2181fd270e78e1d3ac4bc86decd60daeaf786e16e2028d20eebc58105b98ff7b`,
20 pp. Convex `paperVersions:bump` posted with these real values.

**Directive R2 — budget SPENT, this lane STOPS.** R9 + R10 are two consecutive boards. No further
board runs on A3M without an intervening science or scope decision; that decision is the
director's. **Readiness stays at the COMPUTED cap 75, and no cap-95 recommendation is made** —
the automated-review-convergence gate of directive P is not met (the last board found 17 real
items; v3M.0.26 has been reviewed by nothing), and packaging is incomplete.

**Open, for the director:**
- **PUSH GATE** — `origin/main` must carry this manuscript and `r9_perturbativity/` before the
  reproducibility statement's branch-tree pointers are true for external readers.
- **Frozen-release DOI** — unminted; a P-round/maintainer action. The manuscript now promises it
  as a deposit at publication rather than instructing us to mint it.
- **D-round item** — Fig. 1's ~5 pt legend/tick labels need the figure regenerated.
- **Scope decision** — required before any further review board on this paper.

## v3M.0.25 (2026-09-18) — R9 board + closure; rounds RESUMED; readiness held at 75

**Stop lift.** `NEXT_SCIENCE_LEDGER.md` row 19 reads **"DONE 2026-09-04 — NO-GO
GENERALISED"** (decision `D-A3-14`, artifacts
`research/track_a3_multichannel/row19_lambda/`). That was the sole condition the
directive-R2 stop after v3M.0.18 named, so one board (R9) was authorized, plus one
confirmation board if R9 closed a real item. It did; the confirmation board is now the
remaining gate.

**R9 board (INT only; Directive N + Portfolio Decision 2026-09-02 #6).** Exact artifact
`main.pdf` sha256 `e0e923d6…`, md5 `b29ebb90…`, 19 pp, three-way-verified against both
served mirrors and the Convex row before dispatch; preflight receipt PASS. Legs:
Grok `grok-4.3` **REJECT**; Gemini `gemini-3.1-pro-preview` **MINOR REVISIONS**; Claude
Fable 5.1 INT referee **MAJOR REVISIONS**. No leg FAILED. Board:
`peer-reviews/INT_v3/A3M_v3M.0.24_R9_BOARD_2026-09-18.md`; truth-audit:
`…_R9_TRUTH_AUDIT_2026-09-18.md`; receipts:
`INT_v3/ROUND_2026-09-18-A3M-v3M.0.24-EXACTPDF-e0e923d6-R9VERIFY/`.

**Truth-audit outcome.** 24 genuinely-new-real (3 MAJOR, 1 MAJOR-lite, 17 minor, 3 nit),
14 FALSIFIED each with a source citation, 2 re-flags of disclosed, 2 opinion/genre.
Clean-wave count 0.

**The three MAJORs, all closed in v3M.0.25:**

1. `DA3M-R9-01` — the reproducibility statement pinned to commit `68309c8` (2026-09-02).
   `git cat-file -e 68309c8:<path>` over the full artifact list shows **none** of the ~12
   artifacts it names exists at that commit (`row19_lambda`, the A2 adjudication, all five
   `lane9*` dirs, `row10_r_ns`, `row11_pbh_residuals`, `row14_cs_window`, `row18a`,
   `row18b`, `desi_png_reproduction`, `fnl_monopole_adjudication_2026_09_03.md`). Both
   published tree URLs returned HTTP 200 — the parent directories do exist at that commit —
   which is exactly why no link check caught it. Closed by re-pointing the statement at the
   repository `main`-branch trees, stating why a branch pointer is used, and naming the
   frozen-release DOI as a required packaging-stage action rather than an aspiration.
2. `DA3M-R9-12` — Eq. (15) was attributed to Li *et al.* Eq. (4.19) but is their Eq. (5.1),
   the $P\propto X^n$ specialization that already carries $\lambda$ at
   $\Lambda=(1-c_s^2)/(6c_s^2)$ (verified symbolically: substituting that line into the
   general form reproduces $-165/16+65/(8c_s^2)$ exactly). The §VIII $\lambda$-scan
   measured from it therefore double-counted $\lambda$ on the matter-contraction line, and
   the $\lambda=0$ baseline its numbers actually come from was never printed. Closed by
   printing the general-$\lambda$ amplitude $-245/16+105/(8c_s^2)-30\Lambda$ as the primary
   equation, the $X^n$ line as its specialization citing Eq. (5.1)/(A.20), and stating that
   every scan number is measured from the $\Lambda=0$ baseline. `D-A3-14`'s conclusion is
   unchanged — this was a presentation defect that made the headline claim unverifiable
   from the PDF.
3. `DA3M-R9-13` — $f_{NL}^{after}=1.0$–$1.4\times10^{11}$ appeared in the abstract, §VIII
   and Table VII with no statement that the tree-level bispectrum has lost control. The
   paper's own §V B criterion ($1.2|f_{NL}|\sigma\le1$) applied at CMB scales with
   $\zeta_{rms}=\sqrt{A_s}=4.6\times10^{-5}$ gives $|f_{NL}|\le1.8\times10^4$ — the printed
   value is 6.9 decades past it. Closed by a new committed computation,
   `research/track_a3_multichannel/r9_perturbativity/` (`.py`, `results.json`, `.log`),
   which gives a floor $c_s\gtrsim0.073$–$0.079$ (where $r\gtrsim1.8$, already $49\times$
   BICEP/Keck) and independently reproduces the paper's own 68% boundary
   $c_s\ge0.624/0.632/0.627$ as a gate. Table VII and the abstract now rest the exclusion
   on $r=24c_s$ plus loss of perturbative control; the $10^{11}$ figure is retained only as
   an explicitly-labelled formal continuation.

**MAJOR-lite `DA3M-R9-02`.** v3M.0.19 dropped the whole "$\lambda=s=0$" qualifier when
`D-A3-14` had proved $\lambda$-independence **only**; `row19_lambda/results.json` still
records `scheme: "S1 geometric, eps_eff = 1/2, eta_sr = 0, s = 0, k eta_B = 1e-3"`. The
constant-sound-speed restriction is restored to the abstract and to the italicized claim
sentence, with time-dependent $c_s(\eta)$ stated as outside the present computation.

**Minors/nits closed (17 + 3).** Planck 95% edge added as the headline
($c_s\ge0.525$, $r\ge12.6$, disjointness $\sim350\times$) beside the 68% one; squeezed LQC
deficit corrected 2.1–4.4 → **3.1–4.4 dex** against `lane9c2` `abs_comparison/per_k`
(4.41/3.24/3.07 at $k\eta_B=0.1/0.3/1$); §IV D's $T_B$ / $k\eta_B$ pairing corrected
($3.8\times10^{-10}$, not the $T_B=10^8$ GeV value $2.3\times10^{-8}$); PTA injection test
disclosed as establishing bias but **not** coverage, with the $\sigma_\gamma\approx0.16$–$0.17$
recovered widths vs the real-data $0.382$ stated; the $\gamma$ marginal's left skew
($-1.10$, verified from the 320k-sample chain) noted so $\sigma$ exceeding the 68%
half-width no longer reads as an inconsistency; Table V caption re-cited to
`row11_pbh_residuals` (source of the headline $1.84\pm0.03$) rather than the 27-point grid;
bispectrum amplitude $\mathcal A$, $T_3$/$T_4$, sound-speed running $s$, and the quasar
response parameter $p$ all defined at first use; transmitted-amplitude tolerances stated
from `lane_b_numerical` (`step_convergence_rel` $\le1.5\times10^{-8}$); curvaton
"detectable for $r\gtrsim23$" reworded with its $1\sigma$ criterion and the
"tensor-viable $r<11.5$" misuse removed; $n_T$ "cheap discriminator" softened to
in-principle with the $\sigma(n_T)$ reality stated; a drafting-history parenthetical
removed (directive Q1); four internal ledger-row/lane labels removed from prose; nine raw
artifact paths moved out of body/captions into the reproducibility statement; Fig. 1
frequency identified as present-day observed; duplicated "and and" fixed (this one had been
provisionally falsified by a single-line grep and was re-verified as REAL — it spans a line
break); abstract re-trimmed 341 → **307 words**; four disclosed limitations added to §IX
covering the S1 prescription at $c_s\ne1$, the (A4) handoff, the $\delta N$ gradient
expansion, and bounce-window asymmetry.

**Defect found during closure, not by any leg.** The committed v3M.0.24 `main.tex` **did not
compile at all** on a clean toolchain — a raw Unicode `ρ` at line 1754 — under both TinyTeX
and Homebrew TeX Live. The served v3M.0.24 PDF therefore was not reproducible from its own
committed source. Fixed (`$\rho$`); the file is now pure ASCII. This is logged as
`DA3M-R9-25` and is the strongest argument yet for compiling from a clean checkout as part
of directive-G rather than trusting an incremental local build.

**Directive G.** `\paperVersion` v3M.0.25, `\paperTimestamp` September 18, 2026. 4-pass
pdflatex: **0 errors, 0 undefined references, 0 undefined citations**, 20 pp (grew from 19).
Overfull hboxes: max **3.9 pt**, none above 10 pt, none in a table row after Table VII was
narrowed (the first recompile put 8.7 pt into the new Table VII; fixed with footnote
markers). `/latex-audit` visual render of pages 1, 5, 13, 17 — no column escape, no margin
overflow, Table VII and Eqs. (15)/(16) render correctly. Three-way md5
`d46166cb88b32009cdc6be59bb620547` (fresh compile == `public/papers/` ==
`site/public/papers/`), sha256 `c5fe8889766be7f408b5e385f2826af85182ea50b00d4b8142f4db46422ca001`,
775 652 bytes. arXiv tarball rebuilt and standalone smoke-compiled clean (0 undef, 20 pp),
sha256 `403f6b1f…`.

**Readiness: 75, COMPUTED not chosen.** Convex `readinessCap` stays 75 and
`convex/papers.ts` computes `min(cap, cap − penalty)` from open findings. The
automated-review-convergence gate of directive P is **not** met until a board on the exact
v3M.0.25 PDF returns 0 genuinely-new-real. That confirmation board is the one remaining
round permitted under directive R2; after it, and only if clean, A3M becomes a candidate
for cap 95 on the same evidential basis P4′ used. The SSOT frontmatter's former
`headline_pct … ~95` is withdrawn as unsupported.

## v3M.0.19 (2026-09-04) — D-A3-14 (ledger row 19): no-go generalized to full P(X)

`research/track_a3_multichannel/row19_lambda/ROW19_LAMBDA_2026-09-04.md` answers
R8-01's open item: restoring the cubic-action coefficient `lambda` does not
open the window. `r=24c_s` and the bounce's own cubic term
`Delta_fnl^bounce(c_s)` are exactly `lambda`-independent
(`d(c_s^2)/d(P_XXX) = d(Sigma)/d(P_XXX) = 0`; the `lambda` vertex's S1
coefficient is odd about a symmetric bounce and cancels, verified to
`2.8e-7`). `fnl^pre(c_s, L) = -245/16 + 105/(8 c_s^2) - 30L` (`L =
lambda/Sigma`, squeezed) reproduces Li et al. 2016 on their line and
`-35/16` at `c_s=1, L=0`. No `L` in the physical range opens the window;
cancelling the `1/c_s^2` divergence needs `lambda/Sigma = 7/(16 c_s^2)`,
i.e. `s = 39/16`, far outside `|s| << 1`. The DBI line's best case gives
`r_min = 12.57` at `c_s = 0.524` (349x BICEP/Keck). The `lambda=s=0`
qualifier is dropped from the abstract, Sec. VIII, and Next steps; the
general-`lambda` open item is removed. Reproducibility statement now
cites `row19_lambda/row19_lambda.py`, `results.json`,
`row19_lambda.log`, and manifest `a3-row19-lambda.json`. Recompiled
18 pp, 0 undef refs, 0 overfull hboxes >10pt, md5
`fdbf93bfacc6cc644e103ff522d15381` (source dir == site/public/papers ==
public/papers). Readiness held at 75 — ROUNDS STOPPED (R2); row 19
answered — no lambda opens the window.

## v3M.0.18 (2026-09-04) — D-A3-13 (ledger row 19): R8 truth-audit closure, scope statement for the no-go

R8 truth-audit (`INT_v3/A3M_v3M.0.17_R8_TRUTH_AUDIT_2026-09-04.md`) closure
plan (i), 18 items, no new computation. **R8-01** (MAJOR): disclosed that
the `k`-essence no-go (Eq.~16, Table VII) assumes the Li *et al.* kinetic
sector `lambda=s=0`; general `lambda` is now an explicit open item (ledger
row 19, per decision D-A3-13). **R8-02** (MAJOR): Appendix A was printing
the final-label composition (`-25/4+(15/4)mu^2` at eps=3/2) under the
initial-label name (`-5`, isotropic); now prints both `f_map^init` and
`f_map^fin` correctly, transcribed from
`research/theory_audit/psu_gates_S1_S2_2026_09_04.md`. **R8-03**
(MAJOR-lite): defined `Upsilon` and `Delta t_B` where first used
(Quintin Eq. 79 evaluation). **DA3M-06** (residual MAJOR, open since R2):
removed the stale "unresolved r=0.84 matter-bounce scenario, open item"
passage in Sec. VI, replaced with the already-computed `r_after=24`
first-order tensor background (9.1 decades below NANOGrav, already excluded
at k* by BICEP/Keck) — closes the paper's last internal contradiction on its
headline quantity. **DA3M-08** (residual MAJOR, open since R2): swept 14
internal ledger/lane tags (`row18a`, `row18b`, `row14_`, "ledger row n",
`LEDGER4_RESULT_...`, `r5_15`, `r11_pbh`, `D-A3-9`, `lane9c2`) out of body
prose and captions into the reproducibility statement only. Also softened
"the conclusion is therefore scheme-independent ... no continuation rescues
it" to what S1+S2 actually support (S2 is defined only on the Quintin-type
background; LQC/poly have no exact S2 mode construction through their
`Hdot=0` crossings). 12 minors closed at the audit's cited lines: `[S]` row
suppression scaling `O(k_L^2/a^2H^2)`; explicit commit hash `68309c8`
replacing "current HEAD"; Eq. (12) headlines `1.84+-0.03` (144-pt,
`gamma_cr in [0.267,0.630]`), demotes `1.732+-0.050` (27-pt grid) to a
regime note; the Planck f_NL criterion recomputed against the correct 68%
interval `[-6.0,+4.2]` (not the symmetric `|f|<=5.1`) — `c_s_min` moves
`0.600->0.624`, `r_min` `14.4->15.0` (Quintin-type; LQC/poly `0.632/15.2`,
`0.627/15.0`), strengthening the no-go; Sec. V B/V C cross-reference and
`T_B` value fixed; the three distinct uses of `r` (tensor-to-scalar,
mode-mixing, bispectrum shape-overlap) renamed `r`, `r_mix`, `r_sh`; `r_dec`
lower bound `0.113` stated; Li *et al.* citation year unified to 2016;
Table IV's borrowed-`gamma=3` row relabelled; the duplicated Bianchi-I
argument kept once (Appendix A only, Sec. II D now points to it); Fig. 1
legend/axis fonts enlarged and the two predicted curves' legend labels
clarified (`sigw_nhz_from_lab_spectrum_2026_09_04.png` regenerated, no data
change); the `0.5-1.1sigma` vs `3.13sigma` LSS comparison tagged "not
directly comparable". Fable's Q1 (is the `1/(1-eps/3)=2` normalization
factor at eps=3/2 related to Cai *et al.*'s factor-of-two slip?) answered
in Sec. II D: numerically coincident but a different mechanism
(normalization convention vs. amplitude-conversion error). Abstract trimmed
39->0.18: net -20 words to 304 (was over the ~307 cap after R8-01/R8-07
additions). Directive-G hygiene: version bumped, recompiled 4-pass (0
undef refs, largest overfull hbox 3.9pt), three-way md5
`4ce035b9139cbb74d80e84037c43a5fa` (compile == site/public == public ==
source-dir), arXiv tarball rebuilt and smoke-tested (standalone re-extract
+ recompile, 0 undef refs), Convex `paperVersions:bump` +
`activityFeed:add` written. **R2 statement (from the audit): rounds STOP
on A3M after v3M.0.18** — R8 is the fifth consecutive verification round
with no physics or numerical error found; the only item that could license
a further round is the ledger-row-19 science/scope decision on general
`lambda`, which is Houston-gated, not a round trigger.

## v3M.0.17 (2026-09-04) — D-A3-12 (ledger row 18): scheme-independent tensor no-go + c_s-dependent bounce cubic term

Two computational items named by the R7 truth-audit (`row18a_s2_tensor/`,
`row18b_cs_bounce_cubic/`) are closed. §VII (tensor amplitude): the tensor
mode obeys `h''+2(a'/a)h'+k^2h=0` with no `1/H`, `eps`, `c_s`, or scalar
constraint variables, so the S1/S2 scalar-continuation ambiguity cannot act
on it; because the S1 scalar equation with `z=a` **is** the tensor equation,
`lambda_T = lambda_zeta^S1` identically (verified to `1.4e-14` on Quintin-type
at `k eta_B = 1e-3/3e-3/1e-2`, `8.5e-9` on poly/LQC). Hence `r_after^S1=24.0`
is an identity (unchanged from before the bounce) and `r_after^S2≈9.4e2`
(a `39x` bounce amplification in the fluid variable) — both excluded
(`670x`, `2.6e4x` above BICEP/Keck), so the tensor no-go's conclusion is
scheme-independent. §VIII (joint no-go): the bounce's own cubic term is
generalized to `Delta f_NL^bounce(c_s) = -(5/24) rho_B (6c_s^2-5)/c_s^4`
(V2-vertex-dominated, 99.97%; reproduces the `c_s=1` value to `4e-6`),
which changes sign at `c_s=sqrt(5/6)=0.913` and diverges as `1/c_s^4` —
faster than the transmitted term's `1/c_s^2`. Evaluating both terms at the
same `c_s` moves the Planck-viable boundary from `c_s>=0.444` (`r>=10.7`) to
`c_s>=0.600` (`r>=14.4`, `400x` BK18, up from `296x`); at the tensor-viable
`c_s=1.5e-3`, `f_NL^after` rises from `~7e5` to `~1e11`. The no-go is
strengthened, not relaxed. Abstract updated (302 words, `<=307` cap);
Table VII regenerated with the `c_s`-dependent bounce term. 4-pass, 0 undef
refs, 0 overfull hboxes >10pt (largest 3.9pt), 18 pp, md5
`b18aafd1288ffddeea2c3a1ee074a23b`, Convex bump `k5773fexyjhsy11m8gpd4j01xn8dt1fj`,
tarball sha256 `f37ff2e050c6b03349fe0e22c5871caeb2f5f05b3620bed5029fe5ba4c47eba4`
(standalone recompile smoke-tested, 0 errors). Readiness held at 75 —
D-A3-12 taken → one verification board (R8) permitted; recommended for the
next session.

## v3M.0.15 (2026-09-04) — D-A3-10/D-A3-11 science reframe: joint (r,f_NL) no-go

Not a review round; a science decision closing ledger rows 10 and 14
(`NEXT_SCIENCE_LEDGER.md`, decisions recorded in
`PAPER_LINEAGE_2026-08-05.md`'s last two sections). Sources: `row10_r_ns/`,
`row14_cs_window/`, `curvaton_matter_bounce_adjudication_2026_09_04.md`,
`row11_pbh_residuals/`, `threading_map_second_order_2026_09_04.md`,
`separate_universe_failure_criterion_2026_09_04.md` (row 16 candidate, not
yet integrated).

**Title/abstract:** reframed to "Multi-channel tests of the matter-bounce
prediction f_NL = -35/16 and a joint (r,f_NL) no-go for single-field matter
bounces"; abstract rewritten to the spine (exact amplitude → transmission →
r=24 → no c_s cures both → curvaton route → three nulls + DESI reproduction
as conditional checks), 294 words (detex count), under the 307-word
PRD-regular cap.

**New Sec. VII, "The tensor amplitude of the modelled background"
(D-A3-10):** r=16ε=24 exactly for the dust contraction, bounce-invariant to
8e-5 across all three A2 backgrounds, ~670× above BICEP/Keck r<0.036; n_s=1
exactly (0.9649 is an anchor); n_T=n_s-1=-0.035 the one falsifiable tilt
statement; first-order tensors at nHz give Ω_GW h²=1.7e-14, still 1e5.3
below NANOGrav (PTA null unaffected). The earlier tensor-sense "r=0.84" is
withdrawn — traced to the noise-weighted bispectrum shape-overlap
coefficient, not a tensor ratio.

**New Sec. VIII, "The joint (r,f_NL) no-go and the curvaton route"
(D-A3-11):** r=24c_s and f_NL^pre=-165/16+65/(8c_s²) (reproduces Li, Quintin,
Wang & Cai 2016 Eq. 3.18/4.19; c_s→1 limit matches this paper's own -35/16
exactly). r<0.036 needs c_s<1.5e-3 (f_NL^after 6e5-9e5, ~1e5σ over Planck);
|f_NL|≤5.1 needs c_s≥0.444 (r≥10.7); the two windows disjoint 296×; bounce
transfer c_s-independent to 5e-11; Quintin et al. 2015's amplification
route also fails (needs λ≥49, lab gives 4.0-6.1, zero net r suppression).
**Single-field matter bounce (canonical or k-essence) excluded jointly by r
and f_NL** — confirms and strengthens Li+2016's own no-go by 3.8×. Curvaton
route (Cai-Xue-Brandenberger 2011): r=24/[1+(4/3)r_dec²(M_pl/σ_*)²],
f_NL^curv=5/(4r_dec)-5/3-5r_dec/6 (+9.30 to -1.25); (r,n_s)-viable, but
dilutes -35/16 into the bispectrum by (r/24)², detectable only for r≳23;
CXB11's own -320/π⁴≈-3.29 flagged as arithmetic on their estimate, not
derived; converting to a checkable prediction needs an unmodelled entropy
sector (CXB11 Eqs. 62-64 remain un-re-derived).

**Appendix A wording fix:** the δN_c second-order monopole's numerical match
to the pure-translation coefficient (5/12)(3ε) is now stated as a
coincidence of the threading map (`threading_map_second_order_2026_09_04.md`
Appendix A: δN_c=ζ-(1/3)∫∂_iN^i dt along the fluid worldline; f_map=-5ε/4+
(5ε/4)μ²→isotropic -5 for every constant ε), not evidence that a pure
translation supplies the monopole — a rigid, isotropic translation cannot.

**Sec. V (PBH, D-A3-11 carries row 11's fix):** the sign disagreement with
Choudhury et al. below γ_cr≈0.85 is resolved — the apparent enhancement is
an IR-divergent O(ε²) artefact of the quadratic compaction map
(∝(6γ_cr²-1)σ_r², positive only below γ_cr=1/√6), not physical; Choudhury et
al. are right that negative f_NL suppresses throughout. In-coverage
amplitude ratio corrected: **1.84±0.03** (144 pts, γ_cr∈[0.267,0.630],
range [1.76,1.89]; full 255-pt scan 1.83±0.05, [1.61,1.91]); the narrower
1.732±0.050 (original 27-pt committed grid) is no longer quoted as
universal.

**Discussion/Next steps:** the joint-statement paragraph now leads with the
tensor no-go; two new next-steps items — (vi) curvaton-route entropy-sector
mechanism + CXB11 Eqs. 62-64, (vii) n_T=-0.035 as a dedicated forecast
target. Reproducibility statement lists the five new scripts/manifests
(row10_r_ns.py, row14_cs_window.py, curvaton_matter_bounce_adjudication_
2026_09_04.py, row11_pbh_residuals/, threading_map_second_order_2026_09_04.py).

**Directive G (PDF hygiene):** `\paperVersion` v3M.0.15, date unchanged
(2026-09-04, same day). 4-pass pdflatex, 0 undefined refs, 0 overfull hboxes
>10pt (largest 3.9pt, down from a 51pt overfull fixed by line-breaking two
long reproducibility-statement paths). **17 pp**, md5
`4f2bf5e8204021bf06cbe27e3b8932c9`, sha256
`909cf7893b89270f2a24d4a65a8750798b5bca7f6fa34e85acdb078a1bca6043`. Page 1
and the new Secs. VII/VIII (pages 11-13) rendered at 55 dpi and inspected —
clean, tables (VII: joint (r,f_NL) window) render correctly. Served
`site/public/papers/a3_multichannel_arxiv_v3M.0.15.pdf` +
`public/papers/a3_multichannel_arxiv_v3M.0.15.pdf` + source
`research/track_a3_multichannel/paper/main.pdf` — **three-way md5 PASS**
(all `4f2bf5e8204021bf06cbe27e3b8932c9`). arXiv tarball rebuilt
(`SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.15.tar.gz`, sha256
`bf94d9ded6ecd40027533a1468103bbf3ff38fe364383c923a00963012f73006`; main.tex
+ 2 figures; standalone smoke-compile 17 pp, 0 undef refs, only a benign
font-shape warning). Convex `paperVersions:bump` mutation id
`k570ykr8ywyxmbqxpkhc630ys58dvztk` (readback verified: version, md5, pages,
texCommit all match); `activityFeed:add` id
`j57d3z0140nthvhk7a8x3rwef98dtxbm`.

**Readiness held at 75.** D-A3-10/11 → one verification board permitted
(R7) on this reframed content per directive R2's convergence budget; site
data sync (papers.ts/live-status.ts/reviewTimeline.ts) pending in a separate
bundle (another lane owns `site/src` this session).

## v3M.0.14 (2026-09-04) — R6 truth-audit closure, 0 physics errors, rounds stopped (R2)

R6 verification board on the exact v3M.0.13 PDF (sha256 c6f9bb57..., 15 pp):
Claude Fable INT major-revisions (5M/15m), Grok API REJECT, Gemini API
major-revisions. Full audit:
`project-context/peer-reviews/INT_v3/A3M_v3M.0.13_R6_TRUTH_AUDIT_2026-09-04.md`.
41 findings canonicalized to 16 genuinely-new-real (1 MAJOR + 1 MAJOR-lite +
14 MINOR), 8 re-flags of already-disclosed items, 7 falsified against
committed source, 8 opinion/genre/venue. **Zero findings identified an
error in a derivation.**

**Closed (i list, all 20 items):**
1–3. R6-01 (MAJOR): §V C bounce-temperature condition recomputed from the
paper's own committed mapping `k_B≈1.71e7·T_B[GeV]`
(`outputs/inlab_delta2_zeta_2026-09-03.json`) — corrected 10^8–10^10 GeV /
eleven decades above BBN → 6×10^9–6×10^10 GeV / thirteen decades; §IV D's
"7.6 decades below" → 9.6; the §V C worked T_B=10^8 GeV point relabelled
below-validity. Error direction makes the null *stronger*.
4. R6-02 (MAJOR-lite): Channel I mixed the γ=13/3-fixed NANOGrav amplitude
(2.4e-15) against the free-γ slope (3.2); re-paired to the free-γ posterior
amplitude (~6.46e-15); `sigw_nhz_from_lab_spectrum_2026_09_04.py` rerun;
shortfall moves 10^14.3→10^15.2 (14.6 dust bracket); Fig. 1 regenerated.
5–6, 10–11. Abstract calibrated to body: P+B candidate separation
(0.5–1.1σ) vs. bare significance (1.0–1.3σ, Table VI); SMBH-seed FIRAS
exclusion (3 dex, model-independent) separated from this model's own
~7-dex shortfall; S1/S2 stated as two distinct scheme values, not a band;
PBH ratio carries its γ_cr-grid conditionality and the Choudhury
sign-disagreement caveat instead of "shape-robust." Abstract trimmed to
**304 words** (detex count), under the 307-word PRD-regular cap.
7. R6-05: DESI merger-response sign-of-comparison inverted text fixed
(prediction lies above, not below, the central value).
8. R6-06: version-history prose removed from §VII C.
9. R6-07: the 3162σ/3364σ/408σ excursion thresholds sourced with a
one-line derivation and labelled by mass scale, distinct from the
log₁₀β≈−1.7×10^9 number at M_H=10^20 g (n_σ=89,149).
12. R6-10: added the r=0.84 tensor-exclusion sentence after the Channel I
tensor comparison (already-excluded at k_* by the quoted BICEP/Keck bound,
if confirmed — open item A3-4).
13. R6-12: "largely excluded" replaced with the quantified three-orders
SMBH statement.
14. R6-14: S2's missing f_NL^after clarified as cubic-order-only (linear
S2/LQC transfer exists, T=0.409).
15. R6-15: sentence fragment after Eq. (7) repaired.
16. R6-16: Table VI caption states every entry is an upper bound.
17. R6-09: Ref. [8] (Papanikolaou, arXiv:2504.11641) author-list/identifier
flagged for pre-submission verification (not resolvable offline this pass).
18. R6-13: every printed PTA "σ" (abstract, §IV D, Fig. 1 caption,
Discussion) labelled a Gaussian-equivalent z-distance, consistent with the
paper's own Savage–Dickey stance.
19. RF9 (optional): §II D wording harmonized to "a computed identity, not
merely bounded," matching the Appendix's own framing.
20. Sec. VI gains the DESI DR1 v3 reproduction sentence: an independent
re-analysis of the public DESI DR1 QSO sample on DESI's own official
window matrix, full-randoms P_ℓ, and EZmock covariance
(z=0.8–2.1, k≤0.08 h Mpc⁻¹, 46 dof) returns f_NL=−2.2±25 (p=1.6),
0.06σ from the published −3.6⁺⁹·⁰₋₉.₁ — reproducing the published
constraint's sign and scale while showing DR1's power is an order of
magnitude too weak to separate −35/16 from −35/8, from zero, or from the
published value; the near-coincidence with −35/16 is a coincidence, not
evidence; mandatory caveat carried (σ=25 vs. published 9.0 because
wide-angle corrections are not applied and only 2/5 imaging-systematics
splits were run). Source:
`research/desi_png_reproduction/LEDGER4_RESULT_v3_2026-09-04.md`.

**(ii) SCIENCE items moved to `NEXT_SCIENCE_LEDGER.md`, not this review
round:** A3-4 (re-derive r for the three bounce backgrounds under S1 and
test against r<0.036 — the fourth-channel exclusion of item 12 stays
conditional until this is done); A3-1e (resolve the Choudhury et al.
γ_cr≲0.85 sign disagreement — blocked on their spectrum not being
reconstructible from the published paper; realistic route is analytic
diagnosis of the J(γ_cr) sign structure); A3-ns (evaluate Eq. (A3) at
n_s=0.9649 exactly, expected O(1%) shift); A3-dN (identify the second-order
δN mechanism — open theory question); DESI-4 (wide-angle corrections +
the 3 blocked imaging-systematics splits, blocked on locating the
DR9/Legacy pixweight VAC).

**PDF hygiene (directive G):** `\paperVersion` v3M.0.13→v3M.0.14,
`\paperTimestamp` unchanged (2026-09-04, same day). Recompiled 4-pass, 0
undefined references, 15 pp, md5 `de167ede0c3aa1ea31ded3fe9437fd82`, sha256
`9cffe9a8a33566afccf12614fe26e4f3a7fc79eb81b4ca2b284b10e06ecb1fb0`. Overfull
hboxes 2.7pt/2.2pt (both <10pt; a 74.9pt overfull introduced transiently by
the new DESI-sentence path was fixed with an `\allowbreak` before the final
compile). Page 1 and every edited page (bounce-temperature §V C, Fig. 1,
DESI §VI, Reproducibility statement) rendered at 55 dpi and visually
spot-checked — no overflow, all edits render as intended. Mirrored
byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.14.pdf`,
`public/papers/a3_multichannel_arxiv_v3M.0.14.pdf`, and the source-dir
`research/track_a3_multichannel/paper/main.pdf` (three-way md5 match
verified). arXiv tarball rebuilt at
`project-context/SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.14.tar.gz`,
sha256 `207d39f23ee3fcb521b49a6dba33b7b5a639a1dcf8319b15aee4d5e946bb2ba3`
(main.tex + 2 figures), standalone-smoke-tested (extract to a clean
directory, recompile 4-pass, 0 undefined refs, 15 pp). Convex
`paperVersions:bump` mutation id `k57571ypt0a7rz8zx3pfj0evk58dt0pd` (readback
verified); `activityFeed:add` id `j57ce544b5tqt8zzm8dd2vppp98dtpx6`.
`site/src/data/{papers,live-status,publish}.ts` updated to v3M.0.14
strings/pdfMeta/hrefs in the same bundle; `reviewTimeline.ts` gains a
`closure-wave` entry (`a3m-r6-closure-v3m-0-14-2026-09-04`). `cd site &&
npx tsc --noEmit` clean; `tools/site_freshness_check.sh` PASS.

**Readiness held at 75. ROUNDS STOPPED under directive R2 — this was the
third consecutive verification round on A3M, and its yield (0 physics
errors, all real items editorial/calibration/sourcing) confirms the
review-convergence floor. No further review round may be dispatched on
A3M until a science decision is taken on A3-4 and/or A3-1e.**

## v3M.0.13 (2026-09-04) — abstract to cap, 15 pp

Directive-G PDF hygiene wave. v3M.0.12's abstract had grown to ~415 words
against the PRD-REGULAR ≤307-word convention used since v3M.0.6. Rewritten
to exactly 307 words with no science change; every claim retained at its
evidential strength: the −35/16 in-in confirmation and the located Cai
et al. factor-of-2; the linear transfer bound scoped to scheme S1
(assumption A4); the two-scheme transmitted band f_NL^after ∈ [−1.25,−0.50]
with the S1/S2 distinction stated; the three honest nulls (PTA: γ_pred=5.07,
~10^14 below NANOGrav, first-order tensor 8–9 decades below either way;
PBH: ratio 1.7–1.9, 6.7–7.0 dex short, f_PBH=0 exactly, with the γ_cr
grid-coverage caveat carried in the body/table not the abstract; SMBH-seed
high-z: 3 dex short); and the LSS reach (S1 0.7–0.9σ, S2 1.78σ SPHEREx
bispectrum-only).

**PDF hygiene (directive G):** `\paperVersion` v3M.0.12→v3M.0.13,
`\paperTimestamp` unchanged (2026-09-04, same day). Recompiled 4-pass, 0
undefined references, 15 pp, md5 `02251c80882da4eda5fa07c92917c86d`, sha256
`c6f9bb57f9acb755dfe6a3bda12955038ffcf46c86a5cea9809dabff5031a34c`. Overfull
hboxes remain at 2.7pt/2.2pt (both pre-existing, under the `>10pt` gate).
Mirrored byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.13.pdf`,
`public/papers/a3_multichannel_arxiv_v3M.0.13.pdf`, and the source-dir
`research/track_a3_multichannel/paper/main.pdf` (three-way md5 match
verified). Page 1 rendered at 55 dpi and visually spot-checked — abstract
fits cleanly, no overflow. arXiv tarball rebuilt at
`project-context/SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.13.tar.gz`,
sha256 `e1a838dcc3a2b4823e227cc35348402ec39dcda629e4292d8b83463a5b3573ac`
(main.tex + 2 figures), standalone-smoke-tested (extract to a clean
directory, recompile 4-pass, 0 undefined refs, 15 pp). Convex
`paperVersions:bump` mutation id `k57akjqq9tz75xh8kd16tq6t058ds6m7`;
`activityFeed:add` id `j572mzpfrwfep32anbye451yzs8ds05m`.
`site/src/data/{papers,live-status,publish}.ts` updated to v3M.0.13
strings/pdfMeta/hrefs in the same bundle; `reviewTimeline.ts` gains a
`closure-wave` entry (`a3m-abstract-cap-v3m-0-13-2026-09-04`).

**Readiness held at 75. R6 verification board next — last round under the
directive-R2 convergence budget (2/2 will be consumed).**

## v3M.0.12 (2026-09-04) — R5 closure C1–C7 + DA3M-R5-15/18

**Round closed:** `A3M_v3M.0.11_R5_TRUTH_AUDIT_2026-09-04.md` (INT legs: Grok
API `grok-4.3` REJECT 3E/3M/2m/2N; Gemini API `gemini-3.1-pro-preview` MAJOR
REVISIONS 4E/3M/1m/1N; Claude Fable 5.1 INT subagent major-revisions 5
MAJOR/16 minor; OpenAI ABSENT per directive N; Perplexity ABSENT quota). 18
genuinely-new REAL findings closed (3 MAJOR + 15 MINOR), plus 2 real R4
residuals and 1 packaging item. **Readiness held at 75.** Directive R2 note:
this is A3M's **second consecutive** review round on this convergence cycle
— one verification round remains before the R2 convergence-budget (2
rounds) is exhausted; if that round finds 0 genuinely-new-real findings the
paper proceeds past the review-convergence gate, otherwise a science/scope
decision is required before any further review round.

**Closure plan (i) — editorial, no new science, all closed in v3M.0.12:**

| id | closure |
|---|---|
| C1 | Abstract + §III: tagged the `0≤T_fNL<1/2` bound as scheme S1, assumption (A4); stated S2's raw-ADM continuation transmits `T_fNL≈1.03` outside (A4); scoped "S2 has no computable f^after" to the LQC background specifically (S2 IS computed on Quintin-type); gave the per-background S1 table a caption+label (`tab:s1_after`) and added its S2/Quintin-type row (DA3M-R5-01, R5-04, R5-16, R5-08) |
| C2 | Scoped the exact-mode LQC bispectrum deficit (2.1–4.4 dex) to squeezed configuration at and below `k_LQC η_B≈1.06` (was advertised across the full `kη_B∈[0.1,10]`); added `tab:lane9c2` sourced directly from `lane9c2_lqc_modes/results.json` (DA3M-R5-02) |
| C3 | NANOGrav `Ω_GW h²(f_yr)`: `6.3e-10` → `3.6235e-9`, matching `outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json` `nanograv_reference` exactly (DA3M-R5-03) |
| C4 | Closed MINORs R5-05..17, R1, G4: body "under 1σ" → "0.5–1.1σ" (3 remaining sites); narrowed the from-scratch novelty claim to per-vertex attribution; defined `f_NL^ρ`/`f_NL^c` normalization + the δN_c factor-of-2; reconciled "all five" vertex pieces vs "all six cubic attachments"; reworded `O(1)`→factor `0.06–2.2`; "apparent tension"→"forecast detection significance"; fixed a stray mid-equation sentence break, "isoceles"→"isosceles", "Papanikolaou...derive"→"derives"; bounded the uncomputed shape-overlap-`r` claim; named `(T_B,k)` at the `kη_B≈3` PBH evaluation; added the official-vs-refit "not directly comparable" qualifier to Table II's caption (4th recurrence closed) |
| C5 | Regenerated Fig. 1 (`sigw_nhz_from_lab_spectrum_2026_09_04.png`) with publication-quality title/legend (no "A3-3", no `MB_anchored_ns0.9649`/`pure_dust_ns1` internal labels), verified numerically identical to the committed JSON, re-mirrored to `paper/`; closed the `Ω_DM=0.674` footnote residual with a quantified statement (factor `2.55` rescale, model's own f_PBH exactly zero regardless) (DA3M-R5-12, R4-12; directive I6) |
| C6 | Replaced 7 in-body "this lab's" occurrences with "this model's"/"this program's" (the 8th, inside the reproducibility statement's path list, is sanctioned); dropped the two internal-history clauses while keeping the physics (DA3M-R4-11 residual, C7 in the R4 audit) |
| C7 | Eliminated both `>10pt` overfull hboxes: split Eq. `gammapred` into a `gathered` two-line display (was 56.74pt, cascading to a 16.76pt paragraph overfull via a long `\texttt{}` path, now removed); narrowed the App. A.2 `[L]/[K]/[X]/[S]` table columns to `p{2.6cm}p{2.1cm}` (was 14.58pt) |

**Closure plan (ii) — science, computed by a concurrent lane during this
session, inserted in this closure:**

- **DA3M-R5-15** (first-order tensor `Ω_GW` at nHz): the model's own
  primordial tensor background dominates the induced (second-order)
  background by ~6 decades at the CMB bound `r<0.036` (BICEP/Keck,
  arXiv:2110.00483, added to the bibliography), but stays 8–9 orders of
  magnitude below NANOGrav either way, with `γ_pred^(1)=5.035` within `0.04`
  of the induced `γ_pred=5.070` — Channel I remains a null under either
  tensor order. Inserted into §IV D + Table IV's caption.
- **DA3M-R5-18** (`γ_cr` grid coverage): the 27-point grid's 9 distinct
  `γ_cr` values span `[0.766,0.968]` (9/27 points below the 0.85 sign-flip
  scale — the grid straddles it, not a one-branch artefact); the model's
  own spectrum shape sits at `γ_cr∈[0.27,0.63]`, outside that coverage,
  separately giving `1.85–1.89`. The abstract's `1.7–1.9` is the union of
  the scan and one out-of-coverage point, not itself a scan result over the
  full range. Inserted into Table V's caption.

**PDF hygiene (directive G):** `\paperVersion` v3M.0.11→v3M.0.12,
`\paperTimestamp` unchanged (2026-09-04, same day). Recompiled 4-pass, 0
undefined references, 15 pp, md5 `6c9a16d50efe17e16ac683fdb96807ca`, sha256
`ad63d5ee0d67946c34c610a0e9985fe10973f798bc344800c8de2241e58605af`. Mirrored
byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.12.pdf`,
`public/papers/a3_multichannel_arxiv_v3M.0.12.pdf`, and the source-dir
`research/track_a3_multichannel/paper/main.pdf` (three-way md5 match
verified). `/latex-audit`: 0 errors, 0 undefined refs, remaining overfull
hboxes are 2.7pt and 2.2pt (both pre-existing, under the `>10pt` gate).
Pages 1, 7, 8, 9, 13 visually spot-checked at low DPI — no overflow, Fig. 1
labels clean, all inserted tables/equations render inside the column.

**Known open item (flagged, not fixed in this closure):** the abstract is
~415–426 words by a raw word count of the rendered PDF text — this
pre-dates v3M.0.12 (confirmed identical at v3M.0.11 before this round's
edits) and was not flagged by the R5 truth audit's C1–C7 items. A
dedicated abstract-tightening pass to reach the project's ≤307-word
convention is recorded here as a real, not-yet-scheduled residual — it is
not a truth-audit finding and does not block this closure's readiness or
convergence bookkeeping.

## R2 closure (2026-09-02) — FINAL, rounds stop

**Round:** `ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY` (8 pp
v3M.0.4, sha256 `d86f484f5d4f83fb7b4a339cced6a9c4bf9482f5f5bc206a55bdbfe2270e277c`,
verified). **Verdicts (diagnostic only, per directive H/H-refined):**
Claude Fable INT — MINOR REVISIONS (0 MAJOR / 9 MINOR); Grok API `grok-4.3`
— REJECT (3 ESSENTIAL / 3 MAJOR / 2 MINOR / 1 NIT); Gemini API
`gemini-3.1-pro-preview` — MAJOR REVISIONS (4 ESSENTIAL / 4 MAJOR / 3
MINOR-NIT); Perplexity — ABSENT (not run). 0 BLOCKERs, all legs. **Audit
class counts:** 29 raw findings → 16 GENUINELY-NEW-REAL (1 MAJOR + 10 new
MINOR + 5 carried R1 minors: m04, m09, m11, m12, m15), 6
RE-FLAG-OF-DISCLOSED, 3 FALSIFIED, 6 OPINION/GENRE. R1 closure verification
on the exact PDF: 17/20 items CLOSED as specified, 1 PARTIAL (DA3M-02,
precision residual → DA3M-R2-04), 5 unaddressed (m04/m09/m11/m12/m15 —
omissions, not mis-closures); no closure introduced a new factual error; no
number failed recomputation.

**Orchestrator science decision for DA3M-R2-01 (recorded verbatim):** "Run a
real injection–recovery test at γ = 13/3 (and γ = 3) through the SAME 30-bin
free-spectrum pipeline used for the refit... with the same likelihood/bins/
priors as the refit, N ≥ 1 realization each (more if minutes allow), record
recovered γ ± σ and the pull, commit the script + JSON + a reproducibility
manifest, and restate §IV C truthfully with the real numbers." Executed as
option (b) — the stronger close: `research/track_a3_multichannel/pta_injection_30bin_2026_09_02.py`
reuses `model_log10rho`/`log_prior` and the 30-bin/T_obs=16.03yr/prior
geometry verbatim from `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py`;
the real NANOGrav KDE density grids (Zenodo 8060824) are not present on this
machine (they require the RunPod workspace), so a synthetic per-bin Gaussian
density (σ=0.22 dex) centered on a noisy injected observation is substituted
— disclosed explicitly in the paper and the manifest. Recovery is by exact
dense 2D grid (1200×900) posterior marginalization of the identical
log_prior+log_likelihood rather than emcee ensemble sampling: a preliminary
emcee run showed near-zero acceptance on this strongly-degenerate 2D ridge (a
known ensemble-sampler failure mode, not evidence of bias); the dense grid is
an exact, faster computation of the same posterior for 2 parameters. Results
(5 realizations each, `pta_injection_30bin_2026_09_02.json`): γ_true=13/3
(4.3333) → mean recovered 4.328, mean pull **−0.026σ**; γ_true=3.0 (control)
→ mean recovered 3.015, mean pull **+0.068σ**. Both consistent with unbiased
recovery at well under 0.1σ. §IV C rewritten to state these real numbers and
explicitly retract the prior claim that a different (6-bin, Gaussian-χ²,
γ=3.2-injected) validation was "the identical pipeline" injected at 13/3.

**Item → edit table:**

| Canonical item | Sev | Edit in v3M.0.5 |
|---|---|---|
| DA3M-R2-01 (§IV C misdescribes injection artifact) | MAJOR | §IV C (`\label{sec:pta_validity}`) rewritten with the real 30-bin injection-recovery result (γ=13/3: −0.026σ mean pull; γ=3 control: +0.068σ), script+JSON+manifest committed |
| DA3M-R2-02 (Eq. 8 σ² term dropped) | MINOR | Both occurrences (ceiling definition + non-monotonicity discussion) now state the leading-term-only numbers explicitly and give the full σ=0.1 values (0.1215/0.2036, ratio 1.68) |
| DA3M-R2-03 (Ω_DM=0.674 is Planck h) | MINOR | Footnote added: value as printed in Choudhury et al. Eq. (66), coincides with Planck h, cancels in the ratio / absorbed by calibration — no result changes |
| DA3M-R2-04 (13/3 Savage–Dickey precision) | MINOR | Table II 4.5e−4 → 5e−4; text 7.1e3/+3.85 → ≈7e3/+3.9±0.2, one-s.f. rule now consistent |
| DA3M-R2-05 (duplicated §VII C clause) | MINOR | Duplicate "settling the factor of two" clause removed |
| DA3M-R2-06 (undefined D1–D5 labels) | MINOR | "(deviation D1 above)" and "(D1–D5)" replaced with plain-prose descriptions |
| DA3M-R2-07 (refit 3.1–4.6σ mislabel) | MINOR | Split into explicit 3.1σ (official posterior) / 4.63σ (refit) with conditioning stated; L370 quadrature σ=0.53 now labelled |
| DA3M-R2-08 (bare/projected inversion) | MINOR | Reworded: bare significance does not depend on the (not-yet-derived) shape-overlap projection |
| DA3M-R2-09 (abstract DESI prior omission) | MINOR | Abstract now states both merger (−3.6, 0.16σ) and universality (+3.5, 0.77σ) priors with the not-directly-comparable caveat |
| DA3M-R2-10 (r=0.84 numeral unsourced) | MINOR | Numeral dropped (r<1, qualitative statement kept); no result depends on it |
| DA3M-R2-11 (no frozen-release DOI) | MINOR (packaging) | Reproducibility statement notes commit-pin pending Zenodo minting (Houston-only click-list action); P2 theory lineage cited at its archived Zenodo record 10.5281/zenodo.21461881 |
| DA3M-m04 (Table II "archived record" self-reproduction wording) | MINOR (carried) | Reworded: "self-reproduction run of the same script against the same chain," not an independent check |
| DA3M-m09 (Cai ×2 algebraic line unnamed) | MINOR (carried) | Localized to Cai et al.'s Eqs. (38)–(40), f_NL=(20/3)A/Σk³ |
| DA3M-m11 (ζ(∂ζ)² row leading-order qualifier) | MINOR (carried) | Table I footnote: "Zero at leading order O(k²S²)" |
| DA3M-m12 (r complex, text says \|r\|≫1) | MINOR (carried) | r=−9iA²I_∞/k³ stated explicitly (A2_TRANSMISSION_BRIEF_2026-09-02.md:94), complex in general |
| DA3M-m15 ("nested factor" undefined) | MINOR (carried) | Clarified: nested Savage–Dickey factors (point restrictions within the refit's free-γ model) vs. their model ratio |

**CONVERGENCE STATEMENT:** rounds stop after v3M.0.5 per directive R2 (2/2
convergence-budget rounds consumed); the remaining ledger is genre/length/
venue (abstract trim to PRD length, bibliography DOIs, AI-disclosure
placement, `.tex` header hygiene, optional Fig. 1 inset, Zenodo minting) and
belongs to the P-round, not a further review round.

**arXiv tarball (v3M.0.5):** `project-context/SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.5.tar.gz`,
sha256 `cd2ce1ef7c38746a9e8f59db371378bcc74b624a54406ca6f0c74611742522ab`. Contains
`main.tex` + `pbh_compaction_fnl.png` (inline `\bibitem` bibliography, no
separate .bbl). Smoke-tested: extracted standalone and recompiled 4-pass,
0 undefined refs, 9 pp, 544139 bytes — matches the served PDF.

## R1 closure (2026-09-02)

**Round:** `ROUND_2026-09-02-A3M-v3M.0.3-EXACTPDF-7e35caa0-R1` (7 pp v3M.0.3,
sha256 `7e35caa0...`). **Verdicts (diagnostic only, per directive H/H-refined):**
Fable INT — MAJOR REVISIONS (7 MAJOR / 16 MINOR); Grok API `grok-4.3` —
REJECT (3 ESSENTIAL / 3 MAJOR / 2 minor); Gemini API `gemini-3.1-pro-preview`
— MAJOR REVISIONS (2 ESSENTIAL / 1 MAJOR / 2 MINOR); Perplexity — ABSENT
(not run). **Audit class counts:** GENUINELY-NEW-REAL 20 (7 MAJOR/ESSENTIAL +
13 MINOR); RE-FLAG-OF-DISCLOSED 5; FALSIFIED 8 (incl. 2 sub-claims + 3
self-falsified by the Fable leg); OPINION/GENRE 3. No BLOCKERs, no fabricated
math found — the theory core (§II, −35/16, Table I) survived two independent
recomputations.

**Orchestrator science/scope decisions (recorded verbatim):**
- **D1 (PTA).** State NANOGrav's OFFICIAL 14-bin free-spectrum/HD posterior
  γ = 3.2 (+0.6/−0.6, 5–95% interval, arXiv:2306.16213) as the primary
  comparison; the lab's 30-bin refit (γ = 2.567 ± 0.382; synthetic-injection
  validation recovers γ = 3.19) is the secondary analysis. Both sets of
  tensions vs γ=3 and vs 13/3 are quoted (official-posterior SMBHB tension
  ≈ 3.1σ, matching NANOGrav's own "99% credible boundary" language, computed
  in `research/track_a3_multichannel/pta_gamma_reproduce.py`). Every Bayes
  factor/σ that extrapolates the KDE into the unsampled tail (B(γ=5),
  "6.37σ") is dropped from the abstract in favor of stating 0 of 320,000
  samples lie at γ ≥ 5.
- **D2 (transmission).** The transmission statement becomes a
  handoff-scheme-conditional bound: "under a handoff at the NEC boundary with
  cubic sourcing frozen thereafter, 0 < T ≤ 1/2" (assumption A4 explicit);
  "universal" is deleted; the honest note that the bounce's own cubic term is
  not computed is retained.
- **D3 (PBH).** The compaction-function ratio
  A(−35/16)/A(−35/8) = 1.732 [1.610, 1.809] is kept as a result (not demoted
  to illustration), with its regime of validity added (anti-correlated J>1
  branch; 1.2|f_NL|σ_r ≈ 0.7–1.5 non-perturbative excursion range) and an
  explicit one-sentence disclosure of the 55-decade non-monotonicity of
  f_PBH(f_NL).

**Item → edit table:**

| Canonical item | Sev | Disposition | Edit in v3M.0.4 |
|---|---|---|---|
| A3M-R1-01 (PTA official posterior undisclosed) | MAJOR | GENUINELY-NEW-REAL | §IV rewritten: official 14-bin posterior primary (new Table II columns z_official), 30-bin refit secondary with injection-validation subsection; abstract updated |
| A3M-R1-02 (γ=5 tail-extrapolated BF/6.37σ) | MAJOR | GENUINELY-NEW-REAL | Dropped B(γ=5)/"6.37σ" claim from abstract; Table II now reports "n/a" for γ=5 Bayes factor with 0-samples-at-tail note in caption/text |
| A3M-R1-03(b) ("universal" transmission bound) | MAJOR | GENUINELY-NEW-REAL (03a re-flag-of-disclosed) | §III: added explicit assumption (A4), removed "universal", added end-time-independence reconciliation sentence |
| A3M-R1-04(b,c) (PBH non-monotonicity/robust scope) | MAJOR | GENUINELY-NEW-REAL (04a re-flag-of-disclosed) | §V B: added "Regime of validity" + "Non-monotonicity" paragraphs; abstract/§VII scope "robust" to shape-only |
| A3M-R1-05 (4 contradictory factor-of-two statements) | MAJOR | GENUINELY-NEW-REAL | §II C/D rewritten to one consistent statement ("adjudicates within the in-in method"); "CLOSED" removed; §VII joint statement matches |
| A3M-R1-06 (r=0.84 unsourced) | MAJOR | GENUINELY-NEW-REAL | §VI B: r=0.84 now explicitly sourced to the P2 Fisher forecast (item A3-4 open); r-projected significances dropped from Table IV and abstract, bare significance only |
| A3M-R1-07 (Ref. [7] wrong ID+journal) | MAJOR | GENUINELY-NEW-REAL | Bibliography fixed: arXiv:1712.08148, Phys. Rev. D 97, 066021 (2018) |
| A3M-R1-08 (internal issue-tracker tags in body) | MAJOR | GENUINELY-NEW-REAL | All `item A3-N`/"CLOSED"/"flagged in the prior version" tags stripped from body prose (kept in this SSOT); in-body GitHub URLs/commit hash and long SHA-256 consolidated into the Reproducibility statement with line-break-safe formatting |
| R1-m01 (Fig. 1 caption "(top)/(bottom)" vs 1 panel) | MINOR | GENUINELY-NEW-REAL | Caption rewritten to describe the actual single f_PBH-vs-A panel |
| R1-m02 (1.14σ Gaussian-approx on bounded marginal) | MINOR | GENUINELY-NEW-REAL | Labelled Gaussian-approximate; P(γ>3)=8.97% quoted from chain |
| R1-m03 (ESS convention unstated) | MINOR | GENUINELY-NEW-REAL | τ=(58.1,58.0) and ESS=N/max(τ) convention stated |
| R1-m06 (perturbativity range not split per candidate) | MINOR | GENUINELY-NEW-REAL | Per-candidate ranges (0.54–1.01 at −35/16, 1.09–2.02 at −35/8) now quoted |
| R1-m07 (γ_cr discrepancy fiducial unnamed) | MINOR | RE-FLAG-OF-DISCLOSED | One clause naming the −35/8 fiducial added |
| R1-11/A3M-R1-11 (A* normalization missing) | MINOR | GENUINELY-NEW-REAL | A* = 0.131446 printed in §V B and figure caption |
| R1-12/A3M-R1-12 (DESI prior non-comparability) | MINOR | GENUINELY-NEW-REAL | Explicit non-comparability clause + asymmetric errors named in §VI A |
| R1-13 (Li 2016 vs 2017 year) | MINOR | GENUINELY-NEW-REAL (mislabelled MAJOR by Gemini) | Abstract now says Li et al. (2017), matching bibliography |
| A3M-R1-01a/01b (Fable sub-claims) | — | FALSIFIED | Not adopted (causal bin attribution, 1.9σ figure) |
| R1-09 (future-dated header) | — | FALSIFIED | No change (training-cutoff artifact) |
| R1-m19/m20 (arithmetic/formatting artifacts) | — | FALSIFIED | No change |
| A3-1b/c/d, A3-2, A3-3 | — | out-of-round (open science) | Unchanged; remain on next-steps list, not required for R1 closure per directive R2 |

# A3M status — current authoritative section

**Origin.** Executes the lineage decision recorded in
`project-context/PAPER_LINEAGE_2026-08-05.md`, "Decision record — 2026-09-02
(evening): P2′ Letter → theory section of the A3 multi-channel paper": the P2′
Letter's genuine contribution (an independent from-scratch in-in confirmation
of −35/16, not a new discovery) is folded into this paper's theory section
rather than standing as its own PRD Letter.

**What A3M contains:**
1. §II "The exact matter-contraction amplitude" — folded from
   `arxiv/paper2prime_fnl_letter/main.tex` v2L.0.2: setup + validation
   (de Sitter and ultra-slow-roll limits), the per-vertex table (Table I),
   the located ×2 discrepancy with Cai et al. 2009, consistency with
   Li et al. 2016 Eq. 4.19, and the δN/comoving reconciliation
   (ζ_ρ = 2ζ_c at linear order). Ledger item #1 (independent second-method
   adjudication of the factor of two) is CLOSED per NEXT_SCIENCE_LEDGER.md
   row 1 — the from-scratch in-in computation of Table I IS the independent
   route and reproduces −35/16; the δN cross-check reconciles a distinct
   uniform-density quantity, not a second adjudication. The one remaining
   open sub-item is a Bianchi-I separate-universe cross-check of the shear
   response (v3M.0.2 fix, 2026-09-02, corrects v3M.0.1's erroneous "OPEN"
   wording).
2. §III "Transmission through the bounce" — the linear bound
   0 < T_fNL ≤ 1/2 across three bounce backgrounds/two mode-function
   conventions, with the bounce's own (uncomputed) cubic term flagged via
   Agullo–Bolliet–Sreenath 2017.
3. §IV–VI — the A3 skeleton's real channel numbers: PTA slope
   (γ = 2.567 ± 0.382, reproduced from the committed NANOGrav chain); PBH
   abundance via the compaction-function formation criterion (item A3-1,
   CLOSED at ratio-level 2026-09-02) — the first-pass Press–Schechter result
   is kept as context but its ordering is explicitly reversed in-paper: at
   fixed curvature amplitude f_PBH(-35/16) < f_PBH(-35/8) at every point of a
   27-point (Δ, r_p, C_th) grid; the robust output is the required-amplitude
   ratio A(-35/16)/A(-35/8) = 1.732 [1.610, 1.809] (std 0.050), NOT a
   quotable f_PBH (it moves >100 dex with the unreconstructible spectrum
   shape, per PBH_COMPACTION_NOTE_2026-09-02.md); and LSS survey reach
   (DESI DR1 + SPHEREx, cited σ values).
4. §VII discussion + reproducibility statement listing every manifest under
   `reproducibility/manifests/experiments/` (a3-*, including
   a3-pbh-compaction-fnl.json, p2-fnl-*, p2-a2-*).

**PBH gate status:** CLOSED as ratio-level result; abundance not quotable.
Real compaction-function computation supersedes the Press-Schechter first
pass; the amplitude ratio (Eq. 9 of the paper) is the one number this channel
supports until the primordial spectrum is predicted in-lab (open items below).

**Open items (not closed by this commit):**
- A3-1b — in-lab prediction of the matter-bounce contraction-phase curvature
  spectrum, to replace the lognormal stand-in and turn the PBH amplitude
  ratio into a quotable abundance.
- A3-1c — resolve the γ_cr ≲ 0.85 enhancement-branch discrepancy against
  Choudhury et al. 2025 (unresolved: depends on their unreconstructible
  spectrum shape).
- A3-1d — extend the PBH grid to a mass-integrated abundance (their Eq. 66)
  rather than the single M_H = 10^20 g point.
- A2 transmission second half — the bounce's own cubic self-interaction term
  is cited (Agullo–Bolliet–Sreenath 2017) but not computed; item on
  next-steps list.
- R1 review board (Fable INT + Grok API + Gemini API; Perplexity absent) ran
  on v3M.0.3 and is CLOSED as of v3M.0.4 (see "R1 closure" section above).
  R2 verification pass on the new exact PDF is authorized next; no EXT sweep
  yet. Readiness stays at the agent-gate composition (~70%) until R2 confirms
  0 genuinely-new-real findings.

**Not edited by this commit (per lineage decision + task scope):** P2L
(`arxiv/paper2prime_fnl_letter/main.tex`), P2
(`research/focused_paper_source_integration/`), and the A3 brief
(`research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md`).

## Final review 2026-09-02 (orchestrator)
REVISE then DEFER submission; readiness cap 70 (Convex). See `SSOT/FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md`.

## REVISE executed 2026-09-02 → v3M.0.6

Both agent-doable items from `FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md`
§A3M were executed:

1. **Abstract cut to PRD length.** 450 words → 307 words. No quantitative
   claim or evidential-strength qualifier was dropped — every number
   (γ=2.567±0.382, 1.14σ/0.55σ, γ=13/3 at 3.1σ, γ=5 zero of 320,000 samples,
   A(-35/16)/A(-35/8)=1.732[1.610,1.809], the PBH non-monotonicity note, the
   DESI DR1 dual-prior numbers, SPHEREx 3.13σ at σ_fNL=0.7) and every
   qualifier ("not quotable", "not directly comparable", "pending... not yet
   re-derived", "no channel is in tension") survives verbatim or
   near-verbatim; explanatory framing (why the bounce is a testable
   alternative, grading conventions) was already present in the Introduction
   and was left there rather than duplicated in the abstract.
2. **30-bin injection on real NANOGrav KDE grids — NOT RESTORED.**
   `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py`
   loads the real grids from `/workspace/p3_realfreespec/kde/30f_fs{hd}_ceffyl/
   {freqs,log10rhogrid,density}.npy` (Zenodo 10.5281/zenodo.8060824), an
   ephemeral RunPod `/workspace` path — those exact files were never mirrored
   to a durable store. Searched: (a) local disk —
   `~/Desktop/CODE_YOU/bigbounce_datasets` and a repo-wide find for
   `ceffyl`/`30f_fs*` — zero hits; (b) HuggingFace `bamfai/*` datasets (7
   repos: bigbounce-mcmc, galaxy-chirality-catalog, bigbounce-anomaly-catalog,
   astra-desi-edr-mirror, p1b-mcmc-diagnostics, p1b-namaster-artifacts,
   p1b-alp-chains) — no file matching kde/ceffyl/freespec/pta/30f_fs in any
   repo's file list; (c) Backblaze B2 bucket `bigbounce`
   (`s3.us-west-004.backblazeb2.com`, 74,388 objects scanned) — zero keys
   matching kde/ceffyl/freespec/30f_fs; the only `mcmc/` prefix hits are the
   unrelated `w0wa_quintom` cosmological-parameter chains. **Conclusion: the
   real KDE grids are not restorable from any of the three checked stores**
   (they predate the 2026-06-26 ALWAYS-backup directive). §IV.C of the paper
   is left as-is (synthetic-per-bin-density injection, disclosed as such in
   the script and paper text); this is recorded as the missing artifact for
   ledger row A3-3. **Next action if this is to be closed:** re-download the
   Zenodo 8060824 KDE pack directly (no RunPod dependency needed — it is a
   public Zenodo record) to `pipelines/p3_pta_mcmc/kde_real/`, back it up to
   HF+B2 immediately per the ALWAYS-backup directive, then re-run
   `pta_injection_30bin_2026_09_02.py` against the real grids.

**Hygiene (this commit):** `\paperVersion` v3M.0.6, `\date`/`\paperTimestamp`
September 2, 2026 (unchanged, already current); 4-pass pdflatex, 0 undefined
refs, 0 overfull hboxes >10pt; pdftoppm -r 60 all 9 pages visually spot-checked
(pp. 1, 5) — clean two-column layout, no overflow; PDF md5
`3888085edc5c493fcd2a45c8c386576d` (sha256
`db87efa9fcc74f31e3dc8ae5aa3a6296f63536a5c2adaf59f7d28a133b3b2e20`), 9 pages,
mirrored byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.6.pdf`
and `public/papers/a3_multichannel_arxiv_v3M.0.6.pdf`; arXiv tarball
`SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.6.tar.gz` sha256
`c762345fbddd6c38844490c0d975536fc6d50cf4c53a258c5798398becc838b4`, standalone
extract+recompile smoke test PASS (0 undefined refs, 9 pages). Readiness
composition unchanged at this step (still capped by the open DEFER-submission
science gate per the 2026-09-02 final review; abstract/injection were
editorial-hygiene REVISE items, not science-gate closures).

## v3M.0.7 (2026-09-02) — REVISE item CLOSED: real-KDE injection validation

**Closure of the "30-bin injection on real NANOGrav KDE grids — NOT
RESTORED" item above.** The grids were never on an ephemeral RunPod path
alone — they are a public Zenodo data product. Queried
`https://zenodo.org/api/records/8060824`: one file,
`NANOGrav15yr_KDE-FreeSpectra_v1.0.0.zip` (6,571,028 bytes, sha256
`b461125ff9d384761ec4647756587c42067723c6980ef3c633b178012a4d91d8`),
containing five KDE variants; `30f_fs{hd}_ceffyl/` matches
`emcee_freespec.py`'s `ROOT` exactly (`freqs.npy`, `log10rhogrid.npy`,
`density.npy` shape `(1,30,10000)`, `bandwidths.npy`). Downloaded and
extracted to
`~/Desktop/CODE_YOU/bigbounce_datasets/nanograv15yr_kde_2026-09-02/`
(outside the repo); per-file sha256 recorded in
`outputs/pta_injection_30bin_realkde_2026_09_02.manifest.json`. Packed
cache uploaded to HuggingFace `bamfai/bigbounce-aug-011-clean-rerun` under
`external/nanograv15yr_kde/` (zip + sha256 manifest) so this artifact is
mirrored this time, closing the ALWAYS-backup gap that caused the original
loss:
<https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/external/nanograv15yr_kde/NANOGrav15yr_KDE-FreeSpectra_v1.0.0.zip>.

`research/track_a3_multichannel/pta_injection_30bin_realkde_2026_09_02.py`
reuses `model_log10rho`/`log_prior` verbatim from `emcee_freespec.py` and
builds the injection by re-centering each bin's REAL observed KDE curve
(shape/width/skew preserved exactly) along the log10_rho axis onto the
model prediction for a chosen injected `(gamma_true, log10_A_true)` — since
a real dataset's true signal is unknown, this re-centering is the only way
to get a ground-truth injection test out of the real KDE data without
simulating an entirely new PTA dataset from scratch. 5 realizations per
gamma_true (1 full 30-bin + 4 bootstrap bin-resamples), dense 2D grid
posterior marginalization (identical to the prior script's method).

**Results** (`outputs/pta_injection_30bin_realkde_2026_09_02.json`):
γ_true=13/3 (4.3333) → mean recovered 4.336, mean pull **+0.016σ**;
γ_true=3.0 (control) → mean recovered 3.005, mean pull **+0.033σ**. Both
well under 0.1σ, consistent with unbiased recovery, and tighter than the
prior synthetic-Gaussian-density result (−0.026σ / +0.068σ, retained as a
secondary cross-check line per Houston's science decision). §IV C
(`\label{sec:pta_validity}`) restated with the real-KDE numbers as the
primary line; the synthetic-density result is now the secondary
cross-check sentence.

**Hygiene (this commit):** `\paperVersion` v3M.0.7, `\date`/`\paperTimestamp`
September 2, 2026; 4-pass pdflatex, 0 undefined refs, 0 overfull hboxes
>10pt (one pre-existing 2.7pt hbox unrelated to this edit); pdftoppm all 9
pages rendered and pp. 4–5 (the edited section + neighboring page) visually
spot-checked — clean two-column layout, no overflow, real-Zenodo citation
and pull numbers render correctly. PDF md5 `f27a62098e5a673fa16b24d68e70da96`
(sha256 `b0f2ab22558b3c80a777362f8891c13e0af6ff6a7fb0190f90d47679f820e31f`), 9
pages, 543,764 bytes, mirrored byte-identical to
`site/public/papers/a3_multichannel_arxiv_v3M.0.7.pdf` and
`public/papers/a3_multichannel_arxiv_v3M.0.7.pdf`. Convex `paperVersions:bump`
+ `activityFeed:add` written for `paper-a3m`. Readiness raised 70 → 75
(science item genuinely closed with real data; still short of Houston's
final personal review for 100 per directive P).

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.7.tar.gz` sha256
`f4ecb9aec805527688961130ac41b35aaccbed02d62fea9cf25c5c9993ec2681`, rebuilt
from scratch in /tmp (main.tex + pbh_compaction_fnl.png, inline
`thebibliography` — no .bbl staleness risk), standalone extract+recompile
smoke test PASS (0 undefined refs, 9 pages).

## v3M.0.8 (2026-09-04) — three closed science-gate results integrated

**Sources (all committed, pre-existing to this bundle):**
`research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.md`,
`research/theory_audit/fnl_monopole_adjudication_2026_09_03.md`,
`research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md` §8
(+ `lane_a_vertex_table/`, `lane_b_numerical/`, `lane_c_comparison/`),
`research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.md`.

**(1) Method-independent squeezed-limit confirmation — Sec. II rewritten
("Cross-check by a different route: closed").** The classical $\mathcal
O(k^0)$ super-Hubble solution, organized by a shift decomposition
([L] local / [K] shear-curvature, cancels / [X] shift, carries the
quadrupole and $+5/4$ monopole / [S] sourced, suppressed), reproduces the
in-in $-35/16$ result exactly and independently of the in-in commutator
expansion. $\delta N_c=(1-\epsilon/3)\zeta$ (derived from the Friedmann
equation at fixed $\phi$) resolves the gap to every separate-universe
$\delta N$ value as an identity, not an open discrepancy. A companion
Bianchi-I check confirmed the shear alone gives identically zero monopole,
ruling that route out on its own and motivating the shift-decomposition
resolution. Eq. label `eq:deltaNc` added.

**(2) Bounce's own cubic term computed — new Sec. III.A.** Scheme S1
(geometric/dressed-metric): $\Delta f_{\rm NL}^{\rm bounce}=-(5/24)\rho_B$,
confirmed to $3\times10^{-4}$ by an independent finite-$k$ numerical in-in
evaluation. Combined with the pre-existing linear transmission bound:
$f_{\rm NL}^{\rm after}\in[-0.65,-0.50]$ across three backgrounds
(Quintin-type $-0.501$, LQC $-0.651$, poly $-0.555$), valid for
$k\eta_B\lesssim10^{-2}$ within scheme S1; scheme S2 does not regulate
(reported as a non-result). Literature comparison: no contradiction with
Quintin et al. 2015 (different term, same sign); not comparable as computed
with Agullo, Bolliet & Sreenath 2017 (scheme-limited, quantum-geometric
dressing not contained).

**(3) Lab's own predicted spectrum in the PBH channel — new Sec. IV.C.**
The lognormal stand-in of Sec. IV.B is supplemented (not replaced) with the
lab's own CMB-anchored $\Delta_\zeta^2(k)$ fed into the same compaction
machinery unmodified: a clean null, $f_{\rm PBH}=0$ exactly, $7.0$ orders of
magnitude short of the required amplitude at every mass scale
($10^{15}\,$g–$10^4\,M_\odot$). Required-amplitude ratio
$A(-35/16)/A(-35/8)$ widens from $1.732\pm0.050$ to $1.7$–$1.9$ for this
spectrum shape. FIRAS check: lab's own spectrum $\mu=1.65\times10^{-8}$
(safely allowed); required early-SMBH-seed amplitude FIRAS-excluded by
$\sim10^3$ if broadband, excluded even narrow for seeds $\ge10^4\,M_\odot$.

**What was deliberately NOT changed.** The Sec. VI (Channel III, LSS)
survey-reach table (`survey_reach_fnl.py` / `outputs/survey_reach_fnl.json`)
was NOT recomputed at $f_{\rm NL}^{\rm after}$: it never applied a
transmission factor (uses the pre-bounce $-35/16$ directly, as it did in
every prior version), and the new scheme-S1 transmission result is validated
only for $k\eta_B\lesssim10^{-2}$ — the PBH-scale regime — not for the
CMB/LSS pivot scale ($k\sim0.05\,{\rm Mpc}^{-1}$) Channel III uses, which
sits far outside that band. Applying $T_{\fnl}$ there without establishing
validity would be unsupported extrapolation, not a hygiene fix; this gap is
now explicit in the paper (Discussion, "Next steps" item (ii)) rather than
silent.

**Abstract.** Rewritten to state all three closures; 306 words (cap 307 per
this SSOT's prior v3M.0.6 trim).

**Hygiene (this commit).** `\paperVersion` v3M.0.8, `\date`/`\paperTimestamp`
September 4, 2026; 4-pass pdflatex, 0 undefined refs (one benign
`OMS/cmtt/m/n` font-shape warning, pre-existing pattern, not an undef ref);
0 overfull hboxes >10pt (one pre-existing 2.7pt hbox, unrelated to this
edit, carried from v3M.0.7); pdftoppm all 10 pages rendered at 55dpi and
visually spot-checked (pp. 1, 3, 4, 7, 8, 9 — abstract, new §II, new §III.A,
new §IV.C, Discussion) — clean two-column layout, no overflow, no path
overflow. Page count grew 9→10pp from the new content. PDF md5
`0c61d2ab760a14e0ff27ca560585bcbf` (sha256
`8cf429e002d44c97308ccc994c9378a93b066e094de865d48f850d5e72291b9a`), 10
pages, 564,544 bytes, mirrored byte-identical to
`site/public/papers/a3_multichannel_arxiv_v3M.0.8.pdf`,
`site/out/papers/a3_multichannel_arxiv_v3M.0.8.pdf`, and
`public/papers/a3_multichannel_arxiv_v3M.0.8.pdf` (three-way md5 check:
compile == served == Convex, all `0c61d2ab760a14e0ff27ca560585bcbf`).
Convex `paperVersions:bump` (paperSlug `paper-a3m`) + `activityFeed:add`
written; `sitePdfPath` confirmed updated on readback.
`site/src/data/papers.ts`, `site/src/data/live-status.ts`,
`site/src/data/publish.ts`, `site/src/data/reviewTimeline.ts` updated in the
same bundle. Readiness held at **75** (unchanged — this bundle closes
science items but the orchestrator sets readiness after a verification
board, per this SSOT's standing convention).

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.8.tar.gz`
sha256 `ad3680401e0c016965d5876d3148282d820369c3d075c3f518ac09082b09743e`,
rebuilt from scratch in `/tmp` (main.tex + pbh_compaction_fnl.png, inline
`thebibliography`, same convention as v3M.0.7), standalone extract+recompile
smoke test PASS (0 undefined refs, 10 pages).

**Not sourced from a committed file (disclosed).** None — every number
above traces to the four source files listed at the top of this section.

## R3 closure decision C1 (orchestrator, Fable 5.1, 2026-09-04)

**Decision C1 = (a) PROPAGATE.** Verbatim: "The scheme-S1 super-Hubble transfer (validity kη_B ≲ 1e−2, an upper bound on k) is satisfied most easily at the LSS/CMB pivot, so the transmitted amplitude f_NL^after = T·f_NL^pre + Δf_NL^bounce is the paper's observable prediction for every channel. Table IV carries f_NL^after rows for −35/16 and −35/8 on all three backgrounds with bare significances at σ = 0.7/0.5/1.0; the pre-bounce row stays as a clearly-labelled secondary ('assuming T_fNL = 1'). The abstract's 'this channel alone discriminates the two amplitudes, with SPHEREx reaching 3.13σ' is replaced by the transmitted statement (SPHEREx bare 0.7–0.9σ for −35/16, 1.2–1.7σ for −35/8 — no discrimination at current reach). The §VII A 'far outside that validated window' sentence is deleted as false. No exemption (b) is claimed: no physical IR cutoff on S1 exists in the lab's computation." Basis: A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md DA3M-R3-01 (Fable M1 ≡ Gemini E4); VISION.md R6 (claims at evidential strength). Consequence: the Track-A headline becomes a transmission-corrected prediction plus a multi-channel consistency map; the −35/16 vs −35/8 factor-two is not separable by SPHEREx at the transmitted amplitude. Closure C1–C10 → v3M.0.9.

## v3M.0.9 (2026-09-04) — R3 closure C1–C10

C1(a) PROPAGATE executed exactly as recorded in the section above. C2–C10
executed per `project-context/peer-reviews/INT_v3/A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md`
§5. Summary of what changed: §III states the true `kη_B` direction (upper
bound on k, satisfied most easily at large scales) and the false "far
outside that validated window" sentence is deleted; Table IV gains
`f_NL^after` rows (values re-derived by `survey_reach_fnl.py`, cross-checked
against the auditor's precomputed values exactly: 0.7–0.9σ / 1.2–1.7σ at
SPHEREx bispectrum-only); the bounce-energy condition is restated correctly
(`T_B ≳ 1e8–1e10 GeV` at the smallest PBH mass, with the 7-decade-shortfall
argument for why the null verdict is unaffected); a new Appendix A
transcribes the δN_c derivation, [L]/[K]/[X]/[S] table, general-ε formulas,
and Bianchi-I argument from `research/theory_audit/fnl_monopole_adjudication_2026_09_03.md`
§§1–4 (no new science); the induced-GW IR-slope claim is corrected (causal
floor is `f^3`/γ=2, Cai, Pi & Sasaki PRD 102, 083528 (2020), arXiv:1909.13728,
added to the bibliography; γ=3 here follows from the bounce's specific
source spectrum, Papanikolaou Eq. 30+8); three numeric corrections (19–39%,
`n_s−1=12w/(1+3w)`, `0≤T_fNL<1/2`); eight definitional/labelling fixes;
directive-Q1 revision-history sweep (verified: `grep -nE 'research/|earlier
draft|supersed|had to be redone|prior version' main.tex` returns hits only
in reproducibility-statement/appendix-attribution context); Cai bookkeeping
equation numbers added (Li et al. Eq. 4.19 shape function, Eq. 5.1
amplitude); abstract restores the PBH perturbativity/non-monotonicity
caveats dropped in v3M.0.8, trimmed to 304 words (≤307-word PRD cap).

**Script re-runs (committed).** `research/track_a3_multichannel/survey_reach_fnl.py`
extended with `f_NL^after` rows (`outputs/survey_reach_fnl.json` re-emitted);
`research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.py` fixed and
re-run (`outputs/inlab_delta2_zeta_2026-09-03.json` re-emitted, `w` moves
−0.00293→−0.00290 as predicted, all tabulated `Δ²_ζ` values unchanged at
quoted precision); `research/cubic_bounce_transmission/lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md`
corrected 28–39%→19–39% to match.

**Hygiene (directive G).** `\paperVersion` v3M.0.8→v3M.0.9, `\date`/
`\paperTimestamp` → September 4, 2026 (today). 4-pass `pdflatex`, 0 undefined
references, 0 overfull `\hbox` > 10pt (all four transient overfulls from the
new Table IV / Appendix A tables fixed with `\scriptsize` + narrower
`p{}`-columns and `\allowbreak` on one long path). Pages grew 10→12. Page 1
(abstract), page 2 (Cai bookkeeping), page 9 (Table IV / Discussion), and
page 10 (Appendix A) visually spot-checked at ~55 dpi — clean two-column
layout, no overflow, no path overflow. PDF md5
`925198c7ddc3485b9a6285a38995fe94` (sha256
`6c543e5e9885c6db58e07576482ed6f283b0307ad1499c6309a4651d3c26fb1a`), 12
pages, 605,681 bytes, mirrored byte-identical to
`site/public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` and
`public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` (three-way md5 check:
fresh compile == served == Convex, all `925198c7ddc3485b9a6285a38995fe94`).
Convex `paperVersions:bump` (paperSlug `paper-a3m`) written (mutation id
`k5784scqrpaftj6jgra8b22rjx8ds5v2`). `site/src/data/papers.ts`,
`site/src/data/live-status.ts`, `site/src/data/publish.ts`,
`site/src/data/reviewTimeline.ts` updated in the same bundle. Readiness held
at **75** (unchanged — this bundle is a science-decision closure; the
R2-budget allows one more verification round before the next readiness
decision).

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.9.tar.gz`
sha256 `d295ded8593acd723bfe560be6e7ae895feed1464c96fed8c3377b3d87574509`,
rebuilt from scratch in `/tmp` (main.tex + pbh_compaction_fnl.png, inline
`thebibliography`, same convention as v3M.0.8), standalone extract+recompile
smoke test PASS (0 undefined refs, 12 pages).

**Not sourced from a committed file (disclosed).** None — every number
above traces to the source files named above or to the R3 truth audit.

## v3M.0.10 — R4 verification board closed; PTA channel restated as a null; ROUNDS STOPPED (R2) — 2026-09-04

- **R4 board** (exact v3M.0.9 PDF, sha256 6c543e5e…, receipt bound to d8658cbf): Claude Fable major-revisions (5 MAJOR / 11 minor), Grok REJECT (4E/3M/3N), Gemini major-revisions (2E/1M/2N). Board `peer-reviews/INT_v3/A3M_v3M.0.9_R4_BOARD_2026-09-04.md` (2d009f09).
- **Truth-audit** `A3M_v3M.0.9_R4_TRUTH_AUDIT_2026-09-04.md` (1fd01443): 30 raw → 15 outstanding real (3 MAJOR / 12 minor; 13 genuinely-new), 5 re-flag, 8 falsified, 3 opinion. Clean-wave count 0.
- **Editorial closure** (5f1ae797, 194d18da, cbae7906, c1b0168a): S2-scheme exclusion stated beside the transmitted range with its reason; Eq. (6) defined; ref. [9] title corrected; abstract reach consistent with Table IV; decade counts / quadrupole wording; Appendix A domains; γ=2 causal-floor row (Table II, `pta_gamma_reproduce.py`); DESI error side; §VI A/B on one amplitude; Q1 sweep; Ω_DM footnote; Next-steps updated.
- **Science decision D-A3-3** (recorded in `PAPER_LINEAGE_2026-08-05.md` before editing; ledger A3-3 closed a68ac1ec…a638a02c): `research/track_a3_multichannel/SIGW_NHZ_NOTE_2026-09-04.md` — the lab's own spectrum at nHz through the validated Kohri–Terada kernel (benchmark 0.8225 vs 0.8222) gives γ_pred = 5.07 (n_s = 0.9649) / 5.00 (dust), Ω_GW h²(f_yr) = 1.45e−23, 14.3 dex below NANOGrav; kη_B deep inside the A2 domain for all T_B ≥ 1e8 GeV. Channel I restated as a NULL (4ba13ada, 7f57b68d, 1dd175b9, 8f643e06); γ=3 attribution withdrawn.
- **Directive G:** `\paperVersion` v3M.0.10, date 2026-09-04; 4-pass, 0 undefined refs/cites, 0 overfull >10pt, **13 pp**; pages 1/5/6/11/12/13 rendered and inspected; served `site/public/papers/a3_multichannel_arxiv_v3M.0.10.pdf` + `public/papers/…` byte-identical; **three-way md5 PASS** compile == served == Convex `d3981d8b5ed2cbf6b02bd771f784ee1c`; Convex `paperVersions:bump` id `k575ayh1ejerb184hvjjhjch598drgaf`, `activityFeed:add` id `j57104bpxp9pn22q32ygqrvw1h8dsdps`; tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.10.tar.gz` sha256 `b7265d810f11034f4e6cc743f800922b56f3aa71c1d1ff4c24f27330c1ebe077` (main.tex + 2 figures; standalone smoke compile 13 pp, only a font-shape warning).
- **Readiness 75, unchanged.** Publication readiness composition: evidence 25 + convergence (0 genuinely-new outstanding after this closure, but not yet re-verified) + packaging 20 + science: the three science-gate items are closed, and Track A now states three honest nulls + one unseparable channel. **ROUNDS STOPPED under directive R2:** two science decisions were taken this session (C1 propagate; D-A3-3 PTA null); the next board requires a new science decision first (the remaining route: bounce-scale enhancement at kη_B ~ 1, ledger A3-1e).
- Not sourced from a committed file: none.

## v3M.0.11 (2026-09-04) — science decision D-A3-9 (ledger row 9) integrated

**Science decision D-A3-9** recorded in `project-context/PAPER_LINEAGE_2026-08-05.md`
(2026-09-04 entry) before this edit. Sources (bounded reads, every number
traced to a committed file): `research/cubic_bounce_transmission/lane9b_s2_regulation/`,
`lane9b2_s2_rawadm/` (+ `results.json`), `lane9a_velocity_dip/`,
`lane9c_abs_operator/`, `lane9c2_lqc_modes/` (+ `results.json`).

**§III (Transmission).** The "S2 does not regulate" claim is replaced by a
two-scheme statement: the S2 apparent divergence is a total-derivative
artefact of the Maldacena/Chen integrated-by-parts cubic form (explicit
$1/H$ factors singular at the bounce); on the *raw* ADM cubic Lagrangian,
exact S2 mode functions give a comoving-gauge lapse/shift that is regular
at $H=0$ (residue cancellation), so the bounce-window integral is finite
and requires no cutoff. On the Quintin-type background (the only one
evaluated in S2), $\fnl^{\rm after}[{\rm S2}]=-1.249,-1.246,-1.244$ at
$k\eta_B=10^{-3},3\times10^{-3},10^{-2}$ against S1's $-0.501$ — a factor
$\approx2.5$, dominated by the linear Mukhanov–Sasaki variable choice
($|\lambda_\zeta|=0.97$ vs $6.06$) plus an $O(1)$ geometric-vs-lapse
cancellation in the cubic term, not a single operator. The earlier
statement that the Agullo–Bolliet–Sreenath (2017) LQC cubic operator is
"not contained in S1" is corrected: their $\mathcal H^{(3)}$ is, by their
own statement, the Legendre transform of the classical cubic action and
contains no quantum-geometric term; every one of its nine operators maps
onto S1's vertex table. Evaluated with exact LQC-dust modes across
$k\eta_B\in[0.1,10]$ and three initial states, the bispectrum shows no
counterpart of their order-$10^3$ enhancement (2.1–4.4 dex below their
plateau, state-dependence under 13%). A real, background-dependent,
sign-indefinite $O(1)$ transfer feature at $k\eta_B\approx0.6$–$0.8$ is
disclosed ($\Delta^2$ ratio $\times1.76$/$\times2.24$/$\times0.058$ on
Quintin/LQC/poly) and the Quintin *et al.* velocity-dip amplification
(their Eq. 79) is shown to evaluate to exactly 1 on all three backgrounds
(no matter-sector carrier exists on any of them). None of the three
row-9 mechanisms reopens the PTA or PBH nulls.

**Table IV.** Gains an S2 row block (Quintin-type only, $-35/16$):
SPHEREx bispectrum-only $1.78\sigma$, SPHEREx $P+B$ target $2.49\sigma$,
MegaMapper $1.25\sigma$ (`survey_reach_fnl.py`, extended to read
`lane9b2_s2_rawadm/results.json`; re-emitted
`outputs/survey_reach_fnl.json`). The $-35/8$ S2 row is explicitly **not
computed** — no window-convention-free $T_{\rm S2}$/$\Delta_{\rm S2}$
decomposition exists to scale from $-35/16$ without re-running the
raw-ADM in-in integral with the Cai normalization (per the task's
instruction not to scale without new physics).

**§V (PBH null) / §VII (Discussion).** §V now cites the exact-mode
$k\eta_B\approx3$ bispectrum result directly ($|\fnl|\approx0.9$–$1.9$,
worsening the required-excursion threshold to $3364\sigma$ from $3162\sigma$
Gaussian; even the largest number in the row-9 scan, $|\fnl|\approx1.2\times10^3$
equilateral, leaves $408\sigma$ against the 7.0-dex deficit) alongside the
pre-existing literature survey. §VII's "a second scheme (S2) does not
regulate at all, so scheme-independence remains open" is replaced: the
question is answered negatively (finite, factor $\approx2.5$ from S1),
not left open.

**Abstract.** Restates the transmitted amplitude as a two-scheme band,
$\fnl^{\rm after}\in[-1.25,-0.50]$ ($-35/16$, S1∪S2). Trimmed to stay at
or under the pre-edit raw-token length (365 vs 364 before), consistent
with the $\le307$-word PRD cap.

**Next steps.** Row-9 items replaced with what remains: (i) which linear
variable ($z=a$ vs the effective-fluid $z^2$) is the physically correct
continuation through $H=0$ — a theory question, since both schemes are
now finite and genuinely different; (ii) an evaluation-time (freeze-out)
prescription for $k\eta_B\gtrsim0.1$, where the model's lack of a
post-bounce inflationary phase leaves $\zeta$ unfrozen; (iii) shape-overlap
$r$ re-derivation; (iv) extending S2 to the LQC/poly backgrounds and to
$-35/8$; (v) the direct-collapse PBH channel (unchanged from v3M.0.10).

**Reproducibility statement.** Lists the five new lane9 script
directories (`lane9a_velocity_dip/`, `lane9b_s2_regulation/`,
`lane9b2_s2_rawadm/`, `lane9c_abs_operator/`, `lane9c2_lqc_modes/`), each
with its own manifest under `reproducibility/manifests/experiments/`.

**Hygiene (directive G).** `\paperVersion` v3M.0.10→v3M.0.11, date
unchanged (2026-09-04, today). 4-pass `pdflatex`, 0 undefined refs/cites
(one benign pre-existing `OMS/cmtt/m/n` font-shape warning). One overfull
`\hbox` (49.3pt, the reproducibility-statement filename now inside the
extended paragraph) fixed with `\allowbreak`. Two overfull hboxes remain
(56.7pt/16.8pt at the PTA $\gamma_{\rm pred}$ display equation; 14.6pt at
the Appendix `[L]/[K]/[X]/[S]` table) — confirmed **pre-existing**: a
standalone recompile of the unmodified v3M.0.10 baseline (commit
`1f895e9b`) reproduces the identical magnitudes at the identical
paragraphs, so they are unrelated to this edit and not introduced by it.
Pages grew 13→**14**. Pages 1 (abstract), 5 ("Scheme S2, resolved"), 9
(PBH null), 10 (Table IV), 11 (Discussion), and 13 (reproducibility
statement) rendered at 55 dpi and visually spot-checked — clean
two-column layout, no new overflow. PDF md5
`56ca90f1202595c8b7ee2f91932b3c65`, 14 pages, 707,384 bytes, mirrored
byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.11.pdf`
and `public/papers/a3_multichannel_arxiv_v3M.0.11.pdf` (three-way md5
PASS: fresh compile == served == Convex, all
`56ca90f1202595c8b7ee2f91932b3c65`). Convex `paperVersions:bump`
(paperSlug `paper-a3m`) mutation id `k57ag2aq3hs95mvqdkfp3jv9k18dszee`;
readback via `paperVersions:current` confirms version/md5/pages/tarball
path match. `activityFeed:add` id `j57c3yvjyeacafhwsfp58h2k3d8dsf6r`.

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.11.tar.gz`
sha256 `da60e774e78bc7aa8d8fb2567f98d1421802d8f5ad882f95ddd9ce3f5ac794b2`,
190,120 bytes, rebuilt from scratch (main.tex + 2 figures, inline
`thebibliography`, same convention as v3M.0.10), standalone
extract+recompile smoke test PASS (14 pages, 0 undefined refs).

**Readiness held at 75.** Science decision D-A3-9 taken → one
verification board permitted under directive R2 (two decisions were
already taken in this session's prior v3M.0.9/v3M.0.10 work; D-A3-9 is a
further science decision on the same paper, so the next board should be
the closing act before a readiness re-evaluation). **Site data sync
pending redesign**: per this task's scope boundary, `site/src/` was not
touched — five redesign lanes are editing it; the orchestrator syncs
`site/src/data/papers.ts`, `live-status.ts`, `publish.ts`, and
`reviewTimeline.ts` for this version in a later, separate bundle.

**Not sourced from a committed file (disclosed).** None — every number
above traces to the five lane9 files named at the top of this section.

- **R6-09 closed 2026-09-04 (orchestrator, arXiv fetched):** Ref. Papanikolaou2025 verified verbatim against arxiv.org/abs/2504.11641 — title "Gravitational wave signatures of non-singular matter bouncing cosmology in NANOGrav and beyond", sole author T. Papanikolaou, submitted 2025-04-15, Corfu Summer Institute 2024 proceedings contribution, no journal reference. No edit needed.

---

## v3M.0.16 — R7 truth-audit closure (2026-09-04)

Closed all 16 (i) items of `project-context/peer-reviews/INT_v3/A3M_v3M.0.15_R7_TRUTH_AUDIT_2026-09-04.md`
(16 genuinely-new-real findings across Grok_brutal REJECT / Gemini_cosmology
MAJOR REVISIONS / Claude Fable 5.1 INT major-revisions; 0 physics errors
beyond scoping and one stale figure). **R7-01** — `r=16ε=24` scoped to
transmission scheme: S1 (tensor/scalar share `z=a`) gives `r_after=24`
exactly as before; S2's raw-ADM continuation instead gives
`r_after≈9.4×10²` on the Quintin-type background (the tensor problem is
*worse*, not cured, in S2); the Sec. VIII `c_s`-window no-go is scoped to
S1, with S2 noted as strengthening the exclusion. **R7-02** (auditor-found,
directive I6) — Fig. 1's embedded PNG was stale: the paper's copy legended
the superseded NANOGrav free-`γ` amplitude `A=2.4×10⁻¹⁵` while the current
generator (post R6-02 fix) emits `A=6.46×10⁻¹⁵`; regenerated from the
committed script and re-mirrored byte-identical to `paper/` and `outputs/`;
**R7-16** fixed a colliding x-axis minor-tick-label collision in the same
regen. **R7-03** — the `c_s` sign-flip at `c_s=0.8876` disclosed: on
`c_s∈[0.444,0.888)` the k-essence `f_NL^pre` branch is positive, so the
flagship negative sign survives only for `c_s≳0.89`. **R7-04** — disclosed
the quoted window formula is `T×f_NL^pre(c_s)` only (no `Δf_NL^bounce`
term, itself derived at `c_s=1`; numerically `−0.14`, immaterial against
the `5.1` bound, but its `c_s`-dependence away from `c_s=1` is uncomputed —
ledger item `A3-cs-bounce`). **R7-05** — rebuilt the `CaiXue2011` bib entry
from arXiv:1101.0822 (Cai, Brandenberger & Zhang, *The Matter Bounce
Curvaton Scenario*, JCAP 03,003 2011), replacing an internally-inconsistent
prior citation; added Lyth–Ungarelli–Wands, Sasaki–Valiviita–Wands, and
Planck 2018 `f_NL` bib entries; dropped an unverifiable
Cai/Brandenberger/Zhang equation-number pointer rather than assert an
unchecked citation. **R7-06/07** — abstract `|f_NL|≤5.1` →
`|f_NL^after|≤5.1`; no-go statement scoped "on the backgrounds and channels
evaluated here". **R7-08** — Table V `γ_cr≲0.8` rows labelled
non-perturbative branch (`f_PBH>1` = uncapped ratio at the per-point
Gaussian-calibrated `A_*`, not a probability); "suppresses…throughout"
reworded to "suppresses at first order in `ε=(6/5)f_NLσ_r`"; ratio-vs-`γ_cr`
slope quantified (~0.13/unit). **R7-09** — reconciled a Sec. VII tensor-nHz
shortfall statement that silently used the pre-R6-02-fix stale NANOGrav
amplitude (`3.6235×10⁻⁹`, giving the stated `10^5.3`); corrected to `10^6.2`
against the same `2.622×10⁻⁸` free-`γ` posterior amplitude used
consistently elsewhere. **R7-10** — removed repo-path "imported from…"
framing for the LSS shape-overlap value; restated as an assumed `r=1`
pending an explicit shape-overlap projection, with Table VI (`tab:reach`)
explicitly an upper bound. **R7-11** (3rd recurrence, directive Q1) —
deleted remaining version-history/open-item prose ("appeared in earlier
drafts", "open item DESI-4"). **R7-13** — deleted a false claim that
`T_B≈2.3` GeV is below the QCD scale (it is above it) and the non-existent
baryogenesis-argument appeal. **R7-14/15** — Cai et al. shape-to-amplitude
conversion marked "effectively" converted (not exact); the second
`(37)=(4.19)` monomial-sum statement now repeats the distinct-monomial
qualifier and states the six-permutation alternative reading's difference
(`−(99/128)Σk³`, squeezed `−305/64`). **Appendix A** — replaced the
"translation coincidence" wording with the label-resolved statement from
`research/theory_audit/psu_gates_S1_S2_2026_09_04.md`: the initial-label
`δN_c` composition is exactly `−5` for every constant `ε` (not a
coincidence), and the gap to the in-in value is an exact, invertible change
of variable, with the `O(1)` effect an error only in the standard `δN`
formula's identification `δN_c=ζ` (arises iff the neglected integral
`I=O(1)`).

**Hygiene (directive G).** `\paperVersion` v3M.0.15→v3M.0.16, `\date`
held at September 4, 2026 (same day). 4-pass `pdflatex`, 0 undefined
references, 0 overfull `\hbox` >10pt (three pre-existing sub-10pt
overfulls unchanged, confirmed present before this round's edits). Pages
held at 17. Abstract 274/307 words. Page 1 (abstract) and the Fig. 1 page
(p. 8) rendered at 55/200 dpi and visually spot-checked — clean
two-column layout, no overflow; Fig. 1 legend confirmed reading
`A=6.46×10⁻¹⁵` and the x-axis minor-tick collision confirmed gone. PDF
md5 `5544bea1dba2db64f25e85d476489ce4`, 17 pages, 739,054 bytes, mirrored
byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.16.pdf`
and `public/papers/a3_multichannel_arxiv_v3M.0.16.pdf` (three-way md5
PASS: fresh compile == served == Convex, all
`5544bea1dba2db64f25e85d476489ce4`). Convex `paperVersions:bump`
(paperSlug `paper-a3m`) mutation id `k57421pb671psc0vbbxm8zkc698dt1ga`;
readback via `paperVersions:current` confirms version/md5/pages match.
`activityFeed:add` id `j576qgyvfas7whdv1ap4yggct58dvrzr`.

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.16.tar.gz`
sha256 `69d9178f24b6b8a3a292e3d579ec6c8a1c7834de574d31d9499b15c7e375914e`,
rebuilt from scratch (main.tex + 2 figures, inline `thebibliography`),
standalone extract+recompile smoke test PASS (17 pages, 0 undefined refs).

**Readiness held at 75. ROUNDS STOPPED (directive R2).** R7 is the fourth
consecutive verification round on A3M; both reviewer MAJORs (Grok's REJECT
rationale, Gemini's Fig. 1 finding) rested substantially on findings
falsified against committed artifacts (see the audit's (c) FALSIFIED
section). Per directive R2, no further round may be dispatched on A3M on
editorial grounds alone — the next board opens only after a science
decision on the (ii) ledger: `A3-S2r` (a committed lane evolving the tensor
mode under the S2 raw-ADM handoff convention to replace the current hand
ratio), `A3-cs-bounce` (the `c_s`-dependence of `Δf_NL^bounce`), and the
carried `A3-ns`, `A3-dN`, `DESI-4` items. Site data sync (`papers.ts`,
`live-status.ts`, `reviewTimeline.ts`) is out of this task's scope
boundary (`site/src/` not touched) and is deferred to a separate bundle.

## v3M.0.20 — 2026-09-05 — S7 literature correction; rounds still stopped

Same literature-statement correction as paper-su v1S.0.4, applied wherever
this paper's Sec. IV.B ("The Cai et al. factor of two") narrowly attributed
the factor-of-two slip to "specifically their Eqs. (38)–(40)". Per
`research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.md`, the slip is
uniform across Cai et al. (2009) Eqs. (38)–(41) and their Fig. 5 (all four
printed configurations), downstream of the correct Eq. (37). No other
"reuses Cai's rows" phrasing was present in this paper's text. This is a
literature-statement correction, not a new review round — ROUNDS STAY
STOPPED under directive R2; none of the open (ii)-ledger science items
(`A3-S2r`, `A3-cs-bounce`, `A3-ns`, `A3-dN`, `DESI-4`) are touched.

Recompiled: 4-pass pdflatex + bibtex, 0 undefined refs, 0 overfull hboxes
>10pt. PDF md5 `541a6b8a76c9cb2875c13dc15246bcce`, 18 pages, 762,230 bytes,
mirrored byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.20.pdf`
and `public/papers/a3_multichannel_arxiv_v3M.0.20.pdf`. arXiv tarball
`SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.20.tar.gz` sha256
`0dbe3064bb2802e3eabe58639104078280246ba2a6d456ee0f21484ceaa27fd6`, rebuilt
from scratch (main.tex + main.bbl + 2 figures), standalone extract+recompile
smoke test PASS (0 undefined refs). Convex `paperVersions:bump` id
`k573f5pzg2fdz11hwhnppasqax8dvsby`; readback via `paperVersions:current`
confirms version/md5/pages match. `activityFeed:add` id
`j57c2n5c3eq0d00mm346w5qm418dtc38`.

Readiness held at 75. ROUNDS STOPPED (directive R2), unchanged from v3M.0.19.
Site data sync (`papers.ts`, `live-status.ts`, `reviewTimeline.ts`) covered
in a separate task bundle.

## v3M.0.21 (2026-09-05) — literature/derivation correction; rounds still stopped

`research/theory_audit/psu_gates_S9_S10_2026_09_05.md` (S9) found the
second-order uniform-density (rho-slice) delta N map gives f_NL^rho=-5/2 at
dust, not -55/16 (gap 15/16). Sec. II's cross-check paragraph and Appendix A
(Bianchi-I subsection) no longer imply -55/16 is reconciled by the
threading-map identity; both now state the gap and attribute it to an
omitted intrinsic initial-data bispectrum, not a slice-labelling error. Only
the comoving-slice delta N value (-5) is fully reconciled; the flagship
in-in monopole -35/16 is unaffected. 4-pass, 0 undef refs, 0 overfull
hboxes >10pt, 18 pp, md5 `91d5a6511eb0169054855b5fae85960e`, mirrored to
`public/papers/a3_multichannel_arxiv_v3M.0.21.pdf` and
`site/public/papers/a3_multichannel_arxiv_v3M.0.21.pdf`. Readiness held at
75 — ROUNDS STOPPED (R2), unchanged.

## v3M.0.22 (2026-09-05) — S9b derivation-statement correction; rounds still stopped

Same S9b follow-up as paper-su v1S.0.6
(`research/theory_audit/psu_gate_S9b_intrinsic_term_2026_09_05.md`): the
intrinsic flat-slice initial-data term named in v3M.0.21 vanishes in the
growing-mode-dominated limit that defines -55/16, so it cannot be the
closure of the gap to f_NL^rho=-5/2. Sec. II's cross-check paragraph and
Appendix A (Bianchi-I subsection) are corrected: the residual, 5(6-eps)/24,
is now attributed to the super-Hubble evolution step between the flat and
uniform-density slices, not the initial data, and the -55/16 value is
stated as NOT RECONCILED, open. Only the comoving-slice delta N value (-5)
is fully reconciled; the flagship in-in monopole -35/16 is unaffected.
4-pass, 0 undef refs, 0 overfull hboxes >10pt, 18 pp, md5
`afae524cbc3b660978951ae5a675f2c4`, mirrored to
`public/papers/a3_multichannel_arxiv_v3M.0.22.pdf` and
`site/public/papers/a3_multichannel_arxiv_v3M.0.22.pdf`. Readiness held at
75 — ROUNDS STOPPED (R2), unchanged.

## v3M.0.23 (2026-09-07) — derivation-statement update; rounds still stopped

Same S9c follow-up as paper-su v1S.0.7
(`research/theory_audit/psu_gate_S9c_evolution_residual_2026_09_05.md`): the
v3M.0.22 "residual arises in the evolution step" hypothesis is NOT
supported — an independent exact separate-universe solution reproduces both
-5 (comoving) and -55/16 (uniform-density) for all eps, so both delta N
values are well-defined variables. Sec. II's cross-check paragraph and
Appendix A (Bianchi-I subsection) are corrected: the 15/16 gap is relocated
to the second-order threading map's long x short lapse monopole coefficient
A2 = eps*(3-eps)^2/3 versus the separate universe's required 2*(3-eps)^2;
which coefficient is correct is under independent adjudication, not yet
resolved. The flagship in-in monopole -35/16 is unaffected. 4-pass, 0 undef
refs, 0 overfull hboxes >10pt, 19 pp, md5
`52f438454b6227083b54eb8e9746dc79`, mirrored to
`public/papers/a3_multichannel_arxiv_v3M.0.23.pdf` and
`site/public/papers/a3_multichannel_arxiv_v3M.0.23.pdf`. Readiness held at
75 — ROUNDS STOPPED (R2), unchanged.

## v3M.0.24 (2026-09-07) — derivation reconciled; rounds still stopped; readiness 75

Follow-up to paper-su v1S.0.8: the independent adjudication
(`research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md`)
resolves v3M.0.23's open A2 dispute. A2 = eps*(3-eps)^2/3 (this map) stands
as the correct constraint-solve value, not the separate universe's required
2*(3-eps)^2. The v3M.0.23 initial-label figure f^rho=-5/2 came from
composing the threading map with the linear-mode weight lambda'=2*lambda;
the rho-surface time shift, acting on the second-order curvature
perturbation, instead carries weight 3*lambda, and correcting the weight
gives f^rho=5*(eps-7)/8=-55/16 at dust, closing the 15/16 gap exactly. Sec.
II's cross-check paragraph and Appendix A (Bianchi-I subsection) are
updated: the in-in monopole -15/8 (delta N_c normalization), the
comoving-slice delta N value -5, and the uniform-density delta N value
-55/16 are now stated as three well-defined variables related by exact
threading maps, not competing claims — the "not reconciled / open item"
wording is removed. The flagship in-in monopole -35/16 (Maldacena
normalization) is unaffected; no new math. 4-pass, 0 undef refs, max
overfull hbox 3.9pt, 19 pp, md5 `b29ebb90be09f8d0bbc3875647bb150a`,
mirrored to `public/papers/a3_multichannel_arxiv_v3M.0.24.pdf` and
`site/public/papers/a3_multichannel_arxiv_v3M.0.24.pdf`; arXiv tarball
rebuilt and standalone smoke-compiled clean (0 undef refs, 19 pp). Convex
bumped (`paperVersions:bump` k5790qqz..., `activityFeed:add` j5783hvb...).
Readiness held at 75 — ROUNDS STOPPED (R2), unchanged.
