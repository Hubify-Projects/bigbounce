# P4′ v4P.0.3 — R3 (verification pass) truth audit

Manuscript: `pipelines/p4prime_chirality_test/paper/main.pdf`, 11 pp,
sha256 `e8b517d22f61ed733dca043ae2b8253eceffd856ffdfc09e65b422c90b3a8200`
(**verified this session** with `shasum -a 256`; matches all three leg headers).
Round dir: `project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P4P-v4P.0.3-EXACTPDF-e8b517d2-R3VERIFY/`.
Auditor: Opus, verdict-blind on the legs' recommendation words; every row decided from source.

## Legs

| Leg | Model | Verdict word (diagnostic only) | Tagged items in raw | Items dispositioned | Gap |
|---|---|---|---|---|---|
| Claude INT | claude-opus | minor-revisions | 0 MAJOR / 5 MINOR + 1 NIT | 6 | no |
| Grok API | grok-4.3 | REJECT | 0 BLOCKER / 3 ESSENTIAL / 3 MAJOR / 2 NIT | 8 | no |
| Gemini API | gemini-3.1-pro-preview | MINOR REVISIONS | 0 BLOCKER / 3 ESSENTIAL / 1 MAJOR / 1 MINOR | 5 | no |
| Perplexity | — | **ABSENT** (optional leg, 401 insufficient_quota) | — | — | recorded ABSENT, never as zero-findings (skill Rule 4) |

**`[BLOCKER]` count across the round: 0** (explicit observation, `grep -nEi '\[?(BLOCKER)'` on all three raws).
Per skill Rule 8, severity was taken from per-item tags, not from the verdict words:
Grok's REJECT and Gemini's MINOR REVISIONS were **not** used to filter which items were audited.
19 raw findings → **12 canonical** after cross-leg and cross-round fingerprint dedup.

## Part A — verification of the Claude leg's Part-A verification (R2 closures)

Independently spot-verified, not taken on trust:

- DP4P-21 monopole disclosure — `main.tex` ll.288–312 states all three monopoles
  (0.497353 / 0.496051 / 0.5126562 = 454,968/887,472) and the 14,776 CW / 44,739 CCW
  (75.2% CCW) quarantine, matching the R2 recomputation exactly; the by-construction
  and $A_p=m+\bm a\cdot\hat n_p$ absorption arguments are both present with the
  0.39σ generative check. **CLOSED** (unit defect → DP4P-44).
- DP4P-22 — Eq. 1 (l.455) explicitly "not itself a confidence-level bound"; the
  null's 95th percentile 0.669% explicitly relabelled a critical value tied to the
  $p=0.238$ rank; Eq. 2 (l.478) "full-amplitude, Neyman 95% CL", $A_{95}^{\rm CL}\simeq0.75\%$
  with the $[0.75\%,p_5{=}0.466\%]$–$[0.80\%,p_5{=}0.493\%]$ bracket. **CLOSED.**
  The Claude leg re-ran `research/bh_universe_dipole/a95_upper_limit_2026_09_02.py`
  (61.7 s, N_AXES=2000) and reproduced 0.7508188% plus the headline gate
  ($z_{\rm mom}=0.63465$, rank $p=0.237676$); the committed script's `N_AXES = 2000`
  at l.72 and `invert_p5` (ll.192–205, largest injected $A$ keeping $A_{\rm obs}$
  at or above the recovered-amplitude 5th percentile) were re-read here and are the
  standard one-sided Neyman construction. **Construction CORRECT.**
- DP4P-42 schema table — Table 1 (l.212) checked row-by-row against the released
  parquet read with pyarrow: `['object_id','ra_deg','dec_deg','class_eq','score_cw_eq',
  'score_ccw_eq','score_ns_eq','score_eq_max','is_spiral','primary_hc','raw_flip_qc_unsafe']`.
  Contents faithful; typesetting defective (→ DP4P-46).
- DP4P-23 (ll.579–583: +2.21 / +0.81 / −0.61 / −6.57 with the reconciliation
  sentence), DP4P-24 (abstract ll.101–104 g-bridge clause), DP4P-25 (l.154 = 887,472),
  DP4P-26 (ll.428–431 vs caption ll.437–443), DP4P-27 (Table 4 "T5: removed" row +
  caption), DP4P-29 (l.786 "five rows … four non-commensurable statistic families"),
  DP4P-30 (l.290 value + −9.47σ), DP4P-31 (l.642 per-class N summing to 812,793),
  DP4P-32 (UAT identifiers ll.113–114), DP4P-36 (l.1082), DP4P-37 (ll.554–555),
  DP4P-38/39 (`grep` → 0 hits, exploratory disclosure retained l.627), DP4P-41
  (title ll.67–69) — all **verified CLOSED** at the cited lines.

**Result: 21/21 canonical R2 items closed. 0 overstated closures found.** The Claude
leg's Part A is accurate; no closure was found to have been claimed without a
real edit.

## Part B — per-finding disposition table (all legs, deduped)

| # | Leg(s) | Claim · location | Verification | Verdict | Sev | Closure instruction |
|---|---|---|---|---|---|---|
| 1 | Claude MINOR-1 | Monopoles quoted as $f_{\rm CW}-\tfrac12$ ($-0.265$/$-0.395$/$+1.2656\%$) while every other amplitude in the paper is $A_p=2(f-\tfrac12)$ · ll.288–301 vs Fig.1 caption l.439 | Caption l.439 defines $A_p=(N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})=2(f_{{\rm CW},p}-\tfrac12)$; estimator l.~305–309 fits $A_p=m+\bm a\cdot\hat n_p$, so the fitted $m$ is in $A_p$ units. $2(0.5126562-0.5)=+0.0253124$. The primary monopole in the paper's own amplitude convention is **+2.53%**, $2.6\times$ the 0.98% floor quoted later; the text prints +1.2656% one sentence before referring to "$m$". | **GENUINELY-NEW-REAL** | MINOR (SUBSTANTIVE — disclosure) | State both conventions in the same sentence: "$f_{\rm CW}=0.5126562$, i.e. monopole $f_{\rm CW}-\tfrac12=+1.27\%$, equivalently $A_p=+2.53\%$ in the amplitude convention of Fig. 1 and Eqs. 1–2". No number or conclusion changes. |
| 2 | Claude MINOR-2 | Data Availability names a `dr8_id` column · l.1000 | `grep -n -i dr8 main.tex` → l.1000 `\texttt{dr8\_id}`; Table 1 l.221 says `object_id`; pyarrow schema of `pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet` has **no** `dr8_id`. Table 1 is right, l.1000 is wrong and self-contradicting. | **GENUINELY-NEW-REAL** | MINOR (factual) | l.1000 → `\texttt{object\_id}` (DR8 object identifier). |
| 3 | Claude MINOR-3 | Table 1 typesets one column as two rows · source ll.230–231 | Source verbatim: `\texttt{raw\_flip\_} & Release-safety QC flag: raw/eq \\` then `\texttt{qc\_unsafe} & pipeline-pass mismatch (boolean) \\`. The rendered schema therefore lists two non-existent columns in the one table whose purpose (DP4P-42) is exact schema specification. | **GENUINELY-NEW-REAL** | MINOR (factual) | Single row, `\texttt{raw\_flip\_qc\_unsafe}` with `\allowbreak`/smaller font in the `l` column; merge the two descriptions. |
| 4 | Claude MINOR-4 | Cited CL script's docstring contradicts its code · `research/bh_universe_dipole/a95_upper_limit_2026_09_02.py` ll.32–36, cited from l.480 | Docstring: "N_AXES is reduced from the committed 2000 to keep local wall time inside the ~60-minute closure budget (this is a statistical precision tradeoff…)". l.72: `N_AXES = 2000  # matches committed v1.0.265 N_AXES`. The tradeoff never happened. Directive Q2 makes the manifest/script documentation part of the deliverable. | **GENUINELY-NEW-REAL** | MINOR (reproducibility) | Delete the stale paragraph; keep the "no new physics / byte-identical machinery" sentence. |
| 5 | Claude MINOR-5 · Grok E1 · Gemini E1 | The abstract calls $A_{95}^{\rm obs}=0.98\%$ a "95% sensitivity upper limit" and omits $A_{95}^{\rm CL}=0.75\%$; and the CL limit lying *below* the sensitivity floor is unremarked · abstract ll.90–92 vs §3 ll.455–487 | Abstract l.90–92 verbatim: "with a coverage-calibrated observed-label $95\%$ sensitivity upper limit $A_{95}^{\rm obs}\simeq0.98\%$". Body l.462: "It is not itself a confidence-level bound on the measured value." $A_{95}^{\rm CL}$ appears nowhere in the abstract. Three independent legs converge on the same abstract-vs-body drift. | **GENUINELY-NEW-REAL** | MINOR-tagged by Claude/Gemini, ESSENTIAL by Grok → dispositioned at the **higher** reading (skill Rule 8.4): **MAJOR (disclosure)** | See the CL-vs-floor ruling below; abstract must drop "upper limit" for $A_{95}^{\rm obs}$ and must report $A_{95}^{\rm CL}$. |
| 6 | Gemini E2 | "DR1 companion" is undefined · l.599 | `grep -n DR1 main.tex` → only l.599 (body) and l.1111 (P5 reference title). §2 constructs a DESI Legacy **DR8** catalog; the DR1 cross-match that P5 performs is never defined in P4′. A standalone reader cannot evaluate the intersection. | **GENUINELY-NEW-REAL** | MINOR (self-containedness) | One clause in §4: the DESI DR1 spectroscopic TARGETID cross-match of the DR8 chirality catalog, as constructed in \cite{Golden:P5v147}, with the join key named. |
| 7 | Gemini M1 · Grok N2 | Table 1 caption says "release v1.0.244"; ref [15] says "v1.0.274 archived release" · l.213 vs l.1106 | Both strings are individually correct — v1.0.244 is the frozen **catalog release** (the parquet path is literally `apjs_release_v1.0.244/`), v1.0.274 is the **archived release paper's** version. The paper never says so, so a reader sees two version labels for "the archived release". | **GENUINELY-NEW-REAL** (as ambiguity; the "mismatch" premise is FALSIFIED) | MINOR (provenance) | One parenthetical: "catalog release v1.0.244, documented in the v1.0.274 archived release paper \cite{Golden:P4v274}". Do **not** renumber either. |
| 8 | Claude NIT | Ratio column computed from each row's lower amplitude endpoint, so "2–20× below" pairs with "2–33% amplitudes" (33% ↔ ~33×) · abstract l.100, §5.2 l.771, Table 5 caption | Table 5 Ratio 20.4 = 20%/0.98%. The convention is conservative and consistent, merely unstated. | **OPINION/GENRE** | NIT | Optional one clause in the Table 5 caption stating the ratio uses each row's lower endpoint. |
| 9 | Grok E2 | "Largest test" unqualified; no $N_{\rm eff}$ comparison | Abstract ll.106–110 verbatim concedes "except Shamir (2022)'s same-survey DESI Legacy sample ($N=1.3$ million), **which exceeds it**", and scopes "largest single catalog" to the 8,474,531-object release (l.876). This is the executed R1 DP4P-01 closure. The $N_{\rm eff}$-after-purity comparison Grok demands is a new cross-pipeline computation on other authors' masks. | **RE-FLAG-OF-DISCLOSED** (fingerprint: largest, Shamir 2022, denominator) + demand **OUT-OF-SCOPE** | — | None. |
| 10 | Grok E3 | §5 closure is an author-supplied auxiliary assumption; move to "Discussion" | ll.310–313 italic "Eq. 3 is *not* derived from Popławski's papers"; abstract l.96–97 "under the minimal closure needed to make the claim quantitative"; assumption 1. R1 Grok E4 same fingerprint. | **RE-FLAG-OF-DISCLOSED**; relocation is **OPINION/GENRE** | — | None. |
| 11 | Grok M1 | Programmatic first-person voice ("this research program", "our sensitivity floor") | `grep -i` → ll.147, 160, 162, 855, 916. Every hit is inside the **bounce-scope disclaimer** ("We make no bounce claim…", l.160) that directive R6 and the R1/R2 audits require to keep the paper's claim at its evidential strength. Excising it would weaken honest scoping, not the science. | **OPINION/GENRE** | — | None (a copy-edit at submission may de-emphasize, must not delete the disclaimer). |
| 12 | Grok M2 | No purity estimate for the 8.47 M parent or the 887k primary support | Table 2 gives completeness/purity vs $p_{\rm eq}$ against the GZ1 cross-match, with the honest "$^\dagger$Not separately quoted in the archived release"; P4 `chirality_catalog_paper.tex` l.563 carries only these and records the resolved curve as an uncomputed extension. An end-to-end purity for a sample with no external truth set for 8.47 M rows is not constructible from the released data. | **RE-FLAG-OF-DISCLOSED-IN-SOURCE** / demand **OUT-OF-SCOPE** | — | None. |
| 13 | Grok M3 | No "not directly comparable" warning between the primary and FSC/bootstrap statistics | ll.581–588 verbatim: "The block-bootstrap real-space $z=+2.21$ is a **distinct statistic** from the primary null's fixed-occupancy $z_{\rm mom}=+0.635$ … both are non-significant and **neither supersedes the other**"; ll.396–399 names the different support, estimator and null family. Same fingerprint as R2 Grok E4/Gemini E4. | **FALSIFIED** | — | None. |
| 14 | Gemini E3 | Table 4 caption's "supersedes" is version-history prose | Caption ll.363–371 explains a **methodological** supersession inside the archived release (circular-RA Pearson → low-$\ell$ $Y_{\ell m}$ regression, $|z|\le1.25$). This text is the executed DP4P-27 closure, which the R2 audit required in order not to hide the removed T5 row. | **RE-FLAG-OF-DISCLOSED** | NIT | Optional: lead with the methodological reason and drop "originally numbered"; the disposition itself must stay. |
| 15 | Gemini N1 | "in- jects" typographic anomaly, p. 3 | `main.tex` l.305 reads "sample and support it injects into" — no hyphen, no break. `pdftotext -layout main.pdf | grep injects` → no match, i.e. the word is split by ordinary justified-line hyphenation. Skill Rule 7 (extraction/typesetting artifact). | **FALSIFIED** | — | None. |
| 16 | Grok N1 | Draft header / version strings in a submitted manuscript | AASTeX draft header; date equals the actual current date (skill Rule 3); R1 and R2 precedent (DP4P-35). Mechanical at submission. | **OPINION/GENRE** (packaging) | NIT | Strip `linenumbers`/draft header in the submission build only. |

### Class counts (canonical, deduped)

- **GENUINELY-NEW-REAL: 7** — 1 MAJOR-by-Rule-8.4 (#5), 6 MINOR (#1,2,3,4,6,7). All closable without new computation.
- **RE-FLAG-OF-DISCLOSED (incl. -IN-SOURCE): 4** (#9, #10, #12, #14)
- **FALSIFIED: 2** (#13, #15)
- **OPINION/GENRE: 3** (#8, #11, #16); the out-of-scope demands inside #9 and #12 are noted in-row rather than double-counted.
- **BLOCKERs: 0.** No leg found, and this audit found, **any arithmetic, transcription or derivation error** in v4P.0.3. The unit-convention item (#1) is a disclosure defect, not an error: no printed number is wrong in its own stated convention.

### SUBSTANTIVE vs GENRE/LENGTH/VENUE

- **SUBSTANTIVE (must close in v4P.0.4):** #1 (unit disclosure), #2 (wrong column name), #3 (wrong rendered schema), #4 (stale reproducibility docstring), #5 (abstract/body CL drift + missing statistical remark), #6 (undefined dataset), #7 (provenance label ambiguity).
- **GENRE/LENGTH/VENUE (no closure required):** #8, #9's $N_{\rm eff}$ demand, #10's relocation demand, #11, #12, #14's wording, #16. Grok's REJECT rests entirely on this second bucket plus #5; nothing in it identifies a defect in the science.

## Ruling — the 95% CL limit below the detection-power floor (#5, Claude MINOR-5)

**Is presenting $A_{95}^{\rm CL}=0.75\%$ below $A_{95}^{\rm obs}=0.98\%$ correct?** Yes,
and it requires no repair of the construction. The two numbers answer different questions
and are not ordered a priori:

- $A_{95}^{\rm obs}=0.98\%$ is the injected amplitude at which the **detection**
  probability (one-sided add-one rank $p<0.05$ vs the committed $10^4$-draw null)
  reaches 95%. It is a property of the experiment alone — an ensemble sensitivity —
  and is independent of what was observed.
- $A_{95}^{\rm CL}=0.75\%$ is a Neyman one-sided upper limit: the largest true $A$
  whose recovered-amplitude distribution still keeps the **actual** observation
  $A_{\rm dip}=0.4665\%$ at or above its 5th percentile. It is conditioned on this
  particular realization.

The dipole amplitude is positive-definite with null mean $0.362\%$ and null 95th
percentile $0.669\%$; the observation $0.4665\%$ sits between the null mean and the
null's 95th percentile — a low-side realization relative to the amplitude scale the
95%-power floor describes. The *median expected* limit of an experiment is set by its
~50%-power amplitude, which is well below its 95%-power amplitude (the paper's own
curve: 0.24 detection probability at $A=0.40\%$, 0.91 at $0.90\%$, so 50% power lands
near $\sim0.6$–$0.7\%$). A limit of $0.75\%$ is therefore entirely ordinary — it sits
just above the 50%-power scale and below the 95%-power scale, exactly where a classical
limit from a slightly-low observation belongs. Nothing is broken, and the interval is
not empty.

**Correct wording — and a correction to the finding's own phrasing.** The Claude leg
calls this "the classic regime in which a raw Neyman upper limit **undercovers** relative
to the experiment's sensitivity". That phrasing is imprecise and must **not** be copied
into the paper: the one-sided Neyman construction here has *exact* frequentist coverage
by construction; what it lacks is a **sensitivity** interpretation. The real issue that
motivates unified/Feldman–Cousins or $\mathrm{CL_s}$ constructions is that a downward
fluctuation lets a classical limit come out *stronger than the experiment can actually
probe*, and (for a two-sided unified interval) can produce empty or unphysically small
intervals. Neither pathology is present at $0.75\%$, but the "limit stronger than
sensitivity" caveat is exactly the one that applies. Required sentence, in §3 after Eq. 2:

> Because $A_{\rm dip}$ is a low realization of a positive-definite estimator whose
> no-signal distribution has mean $0.362\%$, this classical one-sided limit falls below
> the $95\%$-detection sensitivity $A_{95}^{\rm obs}$. The limit retains exact
> frequentist coverage, but it is a statement about this realization, not about the
> experiment's reach; a downward fluctuation can make a classical limit stronger than
> the amplitude the experiment is guaranteed to detect (the standard motivation for
> unified/$\mathrm{CL_s}$ constructions). We therefore confront the model in Sec. 5
> with the realization-independent floor $A_{95}^{\rm obs}=0.98\%$, the more
> conservative of the two.

**Headline decision — the paper should headline the floor, not the CL limit, and must
say why.** Grok E1's "remove or subordinate 0.98% and make the Neyman limit the primary
bound" is **rejected** on the science: the model confrontation in §5 is a
sensitivity argument ("could we have seen an alignment-driven dipole of the literature's
size?"), which is properly answered by an ensemble-power quantity, and using the tighter,
fluctuation-dependent $0.75\%$ would make the exclusion look *stronger* on the strength
of a lucky low draw — the exact self-favoring move directive F's integrity audit
forbids. Gemini E1's terminology half is **accepted in full**: the abstract must stop
calling $A_{95}^{\rm obs}$ an "upper limit". Required abstract edit:

> …with a coverage-calibrated observed-label $95\%$ **detection-power sensitivity
> floor** $A_{95}^{\rm obs}\simeq0.98\%$ (full-amplitude; the corresponding Neyman
> $95\%$ CL upper limit on the measured amplitude is $A_{95}^{\rm CL}\simeq0.75\%$,
> and we confront the model with the more conservative floor).

Both numbers in the abstract, the confrontation still on $0.98\%$, and the word
"upper limit" attached only to the object that is one.

## Closure plan — v4P.0.4 (final)

Seven edits, no new computation, no figure regeneration (directive I6 sweep: none of
these values is baked into a PNG — the monopole is text-only; Fig. 1's caption already
carries the $A_p$ definition that item #1 must cite):

1. §2.2 ll.294–301 — add the $A_p$ equivalents (+2.53% primary; −0.53% catalog-wide;
   −0.79% HC-with-unsafe) or one convention sentence covering all three. (#1)
2. l.1000 — `dr8_id` → `object_id`. (#2)
3. Table 1 ll.230–231 — merge into one `raw_flip_qc_unsafe` row. (#3)
4. `a95_upper_limit_2026_09_02.py` ll.32–36 — delete the stale N_AXES paragraph. (#4)
5. Abstract ll.90–92 + §3 after Eq. 2 — the two blocks quoted in the ruling above. (#5)
6. §4 l.599 — define the DR1 companion cross-match. (#6)
7. l.213 — "catalog release v1.0.244, documented in the v1.0.274 archived release
   paper \cite{Golden:P4v274}". (#7)

Then directive-G hygiene in the same bundle: bump `\paperVersion` to v4P.0.4 and
`\paperTimestamp`; recompile (0 undefined refs); `/latex-audit`; re-mirror the PDF
byte-identical to every served path; Convex `paperVersions:bump` with the real new
md5/pages; three-way md5 check.

## Convergence statement (directive R2)

R3 was authorized as a **verification pass** on changed text, and it functioned as one:
21/21 R2 closures verified real, the independently re-run Neyman inversion reproduced
$0.7508\%$ exactly, and **zero** genuinely-new findings touch a number, a derivation, a
selection, or the paper's scope. All 7 remaining canonical items are presentation,
terminology, provenance-labelling, and script-documentation; the two REJECT-driving
arguments in the Grok leg are venue/voice preferences that this audit dispositions as
OPINION/GENRE and RE-FLAG against verbatim manuscript text.

**Rounds stop after v4P.0.4.** Directive R2's convergence budget is met — the intervening
science decisions (the monopole resolution and the CL construction) were taken at
v4P.0.3 and are now verified — and directive R2's own stopping rule ("if a verification
pass returns only presentation/venue/packaging items, rounds stop") is satisfied
literally. No further review round on P4′ is authorized. After the v4P.0.4 bundle
verifies, P4′ moves to the publication phase under directive P: agent gates complete →
publication readiness **95**, with the final 5 reserved for Houston's explicit per-paper
sign-off, and venue/submission/endorsement tracked separately and never subtracted from
the score.
