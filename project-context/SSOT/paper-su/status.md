# P-SU status — current authoritative section

**Current candidate:** v1S.0.8 · 2026-09-07 ·
`arxiv/paper_su_criterion/main.tex`

**Title:** "The separate universe computes a different variable: an exact
criterion for $\delta N=\zeta$ in non-attractor phases"

**Status: readiness 72 (up from 40). This header was frozen at v1S.0.2 while
five further science-only bundles (v1S.0.3–v1S.0.8) landed below — reconciled
2026-09-18 (campaign lane L2). First R1 board closed under decision D-PSU-1
(see `project-context/PAPER_LINEAGE_2026-08-05.md`, final section): Claude
Fable (INT), Grok API, Gemini API — 21 genuinely-new-real findings, 5
falsified, 1 opinion, 1 out-of-scope, per
`project-context/peer-reviews/INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md`.
R2 board (v1S.0.2, `PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md`) found 20 more
genuinely-new-real findings, closed in v1S.0.3; R1+R2 exhausted directive R2's
two-round convergence budget, so rounds stopped pending a science or scope
decision. That decision arrived as the S7/S9/S9b/S9c/A2-adjudication science
sequence (v1S.0.4–v1S.0.8, all editorial/science-only, no review round),
closing science gates S6/S7/S9/S10 and reconciling the -55/16 uniform-density
gap. Per directive R2, that intervening science decision re-opened the round
budget: campaign lane L2 (2026-09-18) ran the next permitted verification
board (R3VERIFY) on the exact v1S.0.8 artifact — see `## v1S.0.9 — R3VERIFY`
below for the outcome. R3VERIFY found and closed 2 ESSENTIAL + 3 MAJOR
genuinely-new-real defects (v1S.0.9) — most seriously, the v1S.0.8 A2 closing
amendment had landed in the Appendix but was never propagated to the main
text, leaving the served PDF with two contradictory values for the same
headline quantity for 11 days. **Exit decision: the R3VERIFY round is CLOSED
(no third board scheduled); the paper's status is OPEN pending a new science
gate S12** (Gemini's finding that the translation-term monopole's exact
vanishing was derived assuming $n_s=1$, not verified at general constant-$\eps$)
— see `project-context/peer-reviews/DISPOSITIONS/PSU.md` for the full
citation and required follow-up derivation. **S12 was RESOLVED on 2026-09-19
by campaign lane `bb-LS3-psu-s12`
(`research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.{py,md,json}`,
independently adjudicated): CLOSED-WITH-CORRECTION — the translation term does
carry a nonzero $(n_s-1)$ monopole, but an exactly compensating in-in term
cancels it, so $f_{\delta N}^{\rm init}\equiv-5$ holds for every constant
$\eps$ AND every $n_s$ (stronger than the paper states). S12 is therefore no
longer a science gate; what remains is a PRESENTATION correction to
Appendix A2/A3/A4 (sentences P1–P5 in the derivation note's §"Printable"),
owned by a separate manuscript lane — no `main.tex` edit, version bump, or
review board was done by the S12 lane. See the Close-the-gap section below.**

## v1S.0.2 closure summary (this bundle)

- Title/abstract reframed per D-PSU-1: an exact, invertible change-of-variable
  criterion, not a "failure" (PSU-10, S3 gate). Abstract 139 words.
- Sec. II: Eq. (1) threading identity restated from a flat super-Hubble
  initial slice with the worldline label explicit; Eq. (2) restores the
  dropped $O(k_L^2/a^2H^2)$ gradient term and defines $I$ (S2 gate, PSU-9);
  Eq. (3)/(4) give $f_{\rm map}$ for BOTH worldline labels — initial-label
  composition is exactly $-5$ for every constant $\eps$; final-label adds a
  zero-monopole translation term (S1 gate, PSU-1/PSU-8).
- Table I gains an $f^{\rm in\text{-}in}_{\rm mono}=-15/8$ column so the
  headline factor $8/3$ is traceable in-paper (PSU-3/PSU-7); ekpyrosis row
  marked a consistency check, USR row reworded (PSU-21/PSU-27).
- Cai, Xue, Brandenberger \& Zhang (2009) cited with the located factor-of-2
  and the gap's dependence on it (would be $8/7$, not $8/3$) stated (PSU-4).
  Takamizu-Mukohyama-Sasaki-Tanaka (arXiv:1004.1870) and Naruko-Takamizu-Sasaki
  (arXiv:1210.6525) added to "What is new" after WebFetch-verifying both
  abstracts confirm the NLO gradient-expansion term (PSU-11).
- Script/manifest strings removed from the body, confined to the
  reproducibility statement (PSU-6); AI-usage disclosure narrowed to what the
  scripts actually verify (PSU-24); unpublished notes labelled with commit
  hashes (PSU-23).
- Falsified/out-of-scope items (PSU-12, PSU-13, PSU-17, PSU-18, PSU-19,
  PSU-28) required no paper change beyond PSU-19's monopole-formula print.

## Provenance

Spun out as a standalone short note (revtex4-2, 4 pages) transcribing
`research/theory_audit/separate_universe_failure_criterion_2026_09_04.{md,py,json}`
verbatim, with support from
`research/theory_audit/threading_map_second_order_2026_09_04.md` and
`research/theory_audit/fnl_monopole_adjudication_2026_09_03.md`. No new math
was introduced beyond the source theory-audit note — see
`project-context/PAPER_LINEAGE_2026-08-05.md` for the disposition trail
(original claim vs new claim) recording this as a lift out of A3M Appendix A.

## Content summary

Derives the exact threading identity between Maldacena's comoving $\zeta$
and the separate universe's zero-shift variable $\delta N_c$, and states the
criterion: $\delta N$ (isotropic, with $N(\phi,\pi)$) reproduces the squeezed
bispectrum of $\zeta$ iff the $\zeta$-growth-weighted mean
$\langle\epsilon/c_s^2\rangle_\zeta$ vanishes. Validated on four backgrounds:
dust contraction ($O(1)$ failure, monopole gap $25/8$), ultra-slow-roll
inflation (agreement to $O(\epsilon)$, reproduces Namjoo-Firouzjahi-Sasaki
2013), attractor slow roll (identity map, Maldacena consistency relation
untouched), and ekpyrotic contraction (passes because $\zeta$ sits on its
constant mode, consistent with Creminelli-Nicolis-Zaldarriaga 2004).

## Compile receipts (v1S.0.2)

- 4-pass pdflatex, 0 undefined references, 0 overfull \hbox >10pt (2.6pt,
  2.2pt max) (`/latex-audit` clean)
- 4 pages, abstract 139 words
- PDF md5 `fcbecd03679fdc4ecae3956c35b9b08c`, three-way matched: fresh
  compile == `site/public/papers/paper_su_criterion_v1S.0.2.pdf` ==
  `public/papers/paper_su_criterion_v1S.0.2.pdf`
- arXiv tarball `project-context/SSOT/arxiv_tarballs/paper_su_arxiv_v1S.0.2.tar.gz`
  (sha256 `e8afdd83bf2e5aefe3c505b915fdb66199b4b6a27e34080be69d82872dedbba1`),
  smoke-tested: fresh extract + 2-pass pdflatex, 0 errors, 4 pages
- Convex `paperVersions:bump` id `k57fmgjrvbx4f72zsct0v1kgc98dt8mq`,
  `activityFeed:add` id `j57egqbn8ttkj33vphg8m3wgyh8dvck1`, both read back
  and confirmed current
- Figure `fig_lambda_fmap.png` unchanged from v1S.0.1 (the label-resolved
  fix only touches the quadrupole, not the label-independent monopole the
  figure plots, so no regeneration was required)

## Reproducibility manifest

`reproducibility/manifests/experiments/lift2-separate-universe-failure-criterion.json`
plus `reproducibility/manifests/experiments/psu-gates-s1-s2-label-composition-criterion.json`
(new in v1S.0.2, backs the label-resolved composition + restored gradient
term), both local CPU, \$0, under 5 seconds total compute.

## Close-the-gap section (open items, as of v1S.0.9 — superseded the v1S.0.2-era list below)

- **S12 (RESOLVED 2026-09-19, campaign lane `bb-LS3-psu-s12`) — CLOSED-WITH-CORRECTION;
  NO LONGER GATING.** The from-scratch derivation was done:
  `research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.{py,md,json}`
  (exact sympy; solves the linearised ADM constraints rather than assuming
  Maldacena's solution; rebuilds the label-change kernel from the displacement
  ξ alone and reproduces the committed `lab_init + wl_initextra` exactly; full
  n_s=1 validation battery against every committed and printed value passes
  before any general-tilt claim; finite-k_L numeric guard on the series
  extraction). Manifest
  `reproducibility/manifests/experiments/psu-gate-s12-translation-trace.json`
  (local CPU, 27 s, $0). **Gemini was right about the mechanism:** the trace
  never vanishes (∂_i ξ^i = ε ζ_L exactly) and
  T(ε,μ,n_s) = 5ε/(4(3−ε))·[1 − 3μ² + (n_s−1)μ²], monopole
  5ε(n_s−1)/(12(3−ε)) ≠ 0; the growing branch carries
  n_s − 1 = 2(2ε−3)/(ε−1), which vanishes only at ε=3/2. **But the paper's
  result survives unconditionally:** the in-in shape carries an exactly
  compensating −(5ε/12)(n_s−1)μ², so f_δN^init ≡ −5 for every constant ε AND
  every n_s — the residual vanishes identically before n_s(ε) is substituted,
  i.e. the −5 is *stronger* than the paper claims, not weaker. An independent
  blind `fable` adjudicator returned the same verdict and the same seven
  expressions (re-checked symbolically in script §S9) and caught two further
  n_s=1-specific printed statements (Appendix A2's "both with monopole −5ε/6";
  the printed in-in shape). **Carried forward as a PRESENTATION item, not a
  science gate:** Appendix A2/A3/A4 wording must be corrected and the −5 claim
  strengthened — ready-to-paste sentences P1–P5 are in the derivation note's
  §"Printable". That manuscript edit plus directive-G hygiene is a *separate
  lane's* job; this lane did not touch `main.tex`, did not bump the version,
  and ran no review board. See `DISPOSITIONS/PSU.md` §S12.
- S4 (self-containedness): partially open — Gemini's R3VERIFY MAJOR holds
  that the ADM constraint *solve* itself, not just its listed results, is
  not reproduced in-paper. Non-blocking per directive R2's genre exception.
- S8 (numerical USR validation) and S11 (Zenodo DOI for the cited scripts)
  remain open, unchanged since R2 — non-blocking, carried.
- Venue/arXiv-category selection not yet made (candidate: gr-qc or
  astro-ph.CO); the note is now 7 pp., over a strict PRD-Letter page limit —
  the venue-form decision (Letter vs. Brief Report) is also still open.
- Site (`site/src/data/papers.ts`, `live-status.ts`, `reviewTimeline.ts`)
  updated in the same commit bundle as this v1S.0.9 closure (lane L2, this
  round) — no longer deferred to another lane.

## v1S.0.3 — ROUNDS STOPPED (R2) pending S6–S11 / venue

R2 truth-audit (`project-context/peer-reviews/INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md`)
found 20 genuinely-new-real findings (32 canonical, 6 re-flags, 1 OOS, 2
falsified, 3 opinion) across Grok/Gemini/Fable INT legs. All 11 editorial
items (E-1..E-11) closed in v1S.0.3:

- E-1 abstract precision (linear-order label; in-in-bispectrum composition
  language; USR order $O(\sqrt{\eps_s\eps_f})$; validation count reworded to
  "one nontrivial check plus three consistency limits")
- E-2 Eq. (4) sign flip (sympy-verified independently by the audit)
- E-3 algebra statement corrected ($1-\lambda=I/3$, not $I=1-\lambda$)
- E-4 Cai 2009 counterfactual ratio corrected: **4/3, not 8/7** (R1's own
  PSU-4 disposition supplied a wrong number that had been transcribed
  unverified into the manuscript — see the audit's process finding)
- E-5 references fixed: split conflated [6] into Dai-Pajer-Schmidt CFC
  (arXiv:1502.02011) and DPS "On separate universes" (arXiv:1504.00351);
  Artigas2022/Jackson2023 initials corrected; added Li, Quintin, Wang & Cai
  2017 (arXiv:1612.02036)
- E-6 new paragraph engaging DPS "On separate universes"; gradient-expansion
  order renamed $\eps_{\rm grad}$
- E-7 gradient error term moved inside the $[1-I/3+O(\cdot)]$ bracket
  (abstract, Eq. (2), boxed summary)
- E-8 Eq. (1) caveats ($\partial_iN^i$ coordinate divergence, no-vorticity
  assumption), second-order $\zeta_L(t_i)=0$ assumption stated, uniform-$\phi$
  vs uniform-$\rho$ slice ambiguity noted (LMS $\delta N=\zeta_{ud}$ is not the
  compared object)
- E-9 Table I relabeled ($w{=}0$ scalar not "dust"; ekpyrosis "n/a" not
  "attractor-like"; USR marked not computed here, order corrected; kination
  $\lambda\to0$ and the $\eps\to0$ coincidence qualified as formal limits)
- E-10 $\Theta$ given an explicit name before its symbol; reproducibility
  paths switched from `\seqsplit` to `\url{}` (breaks at `/_-.` instead of
  mid-word)
- E-11 (**required**) new self-contained Appendix A transcribing the
  second-order lapse/shift setup, the five kernel contributions + totals,
  the two-label translation Eq. (S1.1) + per-label maps, and the general-$\eps$
  in-in shape + identity-vs-fit statement, from `threading_map_second_order_2026_09_04.md`
  and `psu_gates_S1_S2_2026_09_04.md` — no new math, transcription only

Post-closure hygiene: 4-pass pdflatex, 0 undefined references, 0 overfull
`\hbox` >10pt (two boxes introduced by the appendix were split/wrapped and
fixed in a follow-up commit), 6 pages (up from 4, driven by the required
appendix). PDF md5 `afeda89e03a7e0bc688d84c423d164fb`, sha256
`2c58f165af4398d6b0790643973867e97c4d9c9e8368a8ff0db8480bd47b28e4`,
three-way matched: fresh compile == `site/public/papers/paper_su_criterion_v1S.0.3.pdf`
== `public/papers/paper_su_criterion_v1S.0.3.pdf`. arXiv tarball
`project-context/SSOT/arxiv_tarballs/paper_su_arxiv_v1S.0.3.tar.gz` (sha256
`527808b57f057000c33b39c9237a55ec4b5708bfab74428b5138a522f7042f81`),
smoke-tested (fresh extract, 2-pass pdflatex, identical byte-size output).
Convex `paperVersions:bump` id `k572q3ewgfsmjb02ets0jyh9b58dvghn`,
`activityFeed:add` id `j572wqc5jm01efn9mr7yt8myz18dt2cj`,
`papers:setReadinessCap` → 65, all read back and confirmed current.

**Per the audit's R2 statement (directive R2 convergence budget: R1+R2 exhaust
it), review rounds on paper-su STOP here** until a science or venue decision
is taken on the remaining science items (not closable by editing):

- S6 — verify (not merely assert) the second-order map used no in-in/$\delta N$
  input; extend the sympy gate to assert the printed Eq. (4)
- S7 — the Cai 2009 factor-of-2 dispute: either an equation-level appendix
  locating the slip, or downgrade to "differs from [18]"; must engage Li,
  Quintin, Wang & Cai 2017
- S8 — turn the USR row into a real validation (exact numerical
  $\delta N(\phi,\pi)$ at finite $\eps_s$)
- S9 — which final slice ($\phi$ or $\rho$) the separate-universe $-5$ is
  computed on
- S10 — $f_{\rm map}^{\rm init}$ when $\zeta_L$ carries a constant piece as
  well as the growing mode
- S11 — Zenodo DOI for the exact script release (carried from R1 E9/C22)

Open Houston-gated decision: does the lab fund S7 (equation-level Cai
reconciliation) and S8 (numerical USR validation), or is the note rescoped
(Brief Report / comment, or held pending the Bianchi-I route)? Running R3 on
an editorially-patched v1S.0.3 would measure referee variance, not progress.

## v1S.0.4 — 2026-09-05 — S7 literature correction (rounds stay stopped)

Per `research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.md` (VERDICT:
LOCATED — equation and mechanism; unprinted step not individually
identifiable): Cai, Xue, Brandenberger & Zhang (2009) Eq. (37) is the correct
squeezed shape function (equals the sum of their Eqs. 27–32 and Li, Quintin,
Wang & Cai (2017) Eq. 4.19 at $c_s=1$); their quoted amplitudes Eqs. (38)–(41)
and Fig. 5 are uniformly twice Eq. (37) in every printed configuration, so the
correct isoceles amplitude is $-35/16$, not the printed $-35/8$. Li et al.'s
$-35/16$ (their Eq. 5.1 at $c_s=1$) evaluates the same Eq. (4.19); their rows
are an independent general-$(\epsilon,c_s)$ derivation coinciding with Cai's
at $\epsilon=3/2$, not a reuse of Cai's rows. Replaced the paper's Sec. I
Cai-comparison sentence with this equation-cited statement; the 4/3-vs-8/3
counterfactual arithmetic from v1S.0.3 is unchanged.

Recompiled: 4-pass pdflatex, 0 undefined refs, 0 overfull hboxes >10pt
(largest 8.31pt, a pre-existing table alignment overfull unrelated to this
edit). PDF md5 `32ef7a73c509eeb5cf4383f2e3ee00fe`, 6 pages, 438,804 bytes,
mirrored byte-identical to `site/public/papers/paper_su_criterion_v1S.0.4.pdf`
and `public/papers/paper_su_criterion_v1S.0.4.pdf`. Convex
`paperVersions:bump` id `k577w3x0yrqxp98jm9kxg9q6ss8dtcye`; readback via
`paperVersions:current` confirms version/md5/pages match. `activityFeed:add`
id `j5752bnpcs3h0egbb871zrer3s8dv8bq`.

This is a literature-statement correction, not a new review round — S7 is
now CLOSED per the audit. Readiness held at 65. Review rounds remain STOPPED
under directive R2; the open Houston-gated science/venue decision from
v1S.0.3 (fund S8 numerical USR validation and rescope, vs. hold) is
unchanged.

## v1S.0.5 (2026-09-05) — S9 resolved-negative, S10 resolved; rounds stopped; readiness 65

`research/theory_audit/psu_gates_S9_S10_2026_09_05.md` closes the remaining
science gates. S10 RESOLVED: the constant-mode kernel K_c is derived in
closed form (ADM constraints at (m_L,m_S)=(0,3/eps-1)), squeezing to -2eps/3,
exactly cancelling the constant-mode zlap term; corrected normalisation
f_map(g)=(g*lambda_1/lambda_g)*f_map(1), 1/(lambda_g*lambda_1); g=1
reproduces -5 / -25/4+(15/4)mu^2. S9 RESOLVED (equations) but the
composition is NEGATIVE: the second-order uniform-density (rho-slice) map
gives f^rho_NL=5(2eps-15)/24=-5/2 at dust, isotropic — this does NOT
reproduce the lab's uniform-density delta N value -55/16 (gap 15/16); the
missing step is the intrinsic flat-slice initial-data bispectrum in that
delta N lane (Namjoo-Firouzjahi-Sasaki caveat). Appendix A + Sec. II updated
accordingly; the paper no longer implies -55/16 is "the same physics in a
third variable." 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 6 pp, md5
`780b079e88e4ade112b35517edece020`. Readiness held at 65 — ROUNDS STOPPED
(R2), unchanged.

## v1S.0.6 (2026-09-05) — S9b: intrinsic term does not close the gap; open; rounds stopped; readiness 65

`research/theory_audit/psu_gate_S9b_intrinsic_term_2026_09_05.md` computes the
intrinsic flat-slice initial-data term named in v1S.0.5 directly:
f^intr_NL = 5*sqrt(3*eps)*(3-eps)/18 * r_i/(W-1) (= 5*sqrt(2)/8 * r_i/(W-1) at
eps=3/2). It VANISHES in the growing-mode-dominated limit that defines the
delta N value -55/16, for any t_f-independent r_i — it is not +-15/16, and
-55/16 + f^intr does not equal -5/2. The residual, 5(6-eps)/24, is unchanged
and does NOT arise in the initial data: it arises in the super-Hubble
evolution step between the flat slice at t_i and the uniform-density slice
at t_f (the separate-universe map versus the in-in evolution), with the
dropped shift term (1/3)*integral(d_i N^i dt) named as a candidate, not
asserted. The -55/16 sentence is replaced accordingly: NOT RECONCILED,
stated as an open item. 4-pass, 0 undef refs, 0 overfull hboxes >10pt, 6 pp,
md5 `13b2e4b0f935e7275fdde03e93c41f2c`, mirrored to
`public/papers/paper_su_criterion_v1S.0.6.pdf` and
`site/public/papers/paper_su_criterion_v1S.0.6.pdf`. Readiness held at 65 —
ROUNDS STOPPED (R2), unchanged.

## v1S.0.7 (2026-09-07) — S9c: dropped-evolution-term hypothesis NOT supported; A2 under adjudication; rounds stopped; readiness 65

`research/theory_audit/psu_gate_S9c_evolution_residual_2026_09_05.md` tests
the v1S.0.6 evolution-step hypothesis directly with an independent exact
separate-universe solution: it reproduces both -5 (comoving slice, all eps)
and -55/16 (uniform-density/rho slice, all eps) — the hypothesis that the
lane drops an evolution term is NOT SUPPORTED, and both delta N values are
well-defined variables, not artifacts. The 15/16 gap is relocated exactly to
the second-order threading map's long x short lapse monopole coefficient
A2 = eps*(3-eps)^2/3 (this map, = 9/8 at dust) versus the separate universe's
required 2*(3-eps)^2 (= 9/2 at dust); WHICH coefficient is correct is under
independent adjudication (a Fable lane), not yet resolved. The residual
sentence is replaced accordingly in both papers-su and A3M. 4-pass, 0 undef
refs, 0 overfull hboxes >10pt, 6 pp, md5 `89d7965b86fe1961c69b474d2764e54d`,
mirrored to `public/papers/paper_su_criterion_v1S.0.7.pdf` and
`site/public/papers/paper_su_criterion_v1S.0.7.pdf`. Readiness held at 65 —
ROUNDS STOPPED (R2), unchanged.

## v1S.0.8 (2026-09-07) — S9 fully reconciled (A2 adjudicated); all science gates closed; readiness 65 -> 70; rounds stopped; next: venue

`research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md`
(independent adjudicator) resolves v1S.0.7's open A2 dispute: S9's
constraint solve A2 = eps*(3-eps)^2/3 is correct (not the separate
universe's required 2*(3-eps)^2). The uniform-density-surface squeezed
monopole is f^rho_NL = 5*(eps-7)/8 = -55/16 at eps=3/2 — S9's earlier
-5/2 came from composing the threading map with the linear-mode weight
lambda' = 2*lambda where the rho-surface time shift, acting on the
second-order curvature perturbation, instead carries weight 3*lambda;
correcting the weight closes the 5*(6-eps)/24 gap exactly. In-in monopole
-15/8, comoving delta N -5, and uniform-density delta N -55/16 are now
three well-defined variables related by exact threading maps, not
competing claims. paper-su Appendix A composition step corrected in
place (v1S.0.8, no new math). 4-pass, 0 undef refs, max overfull hbox
8.3pt, 6 pp, md5 `87bda8d5faf08102b621a3ea1755d233`, mirrored to
`public/papers/paper_su_criterion_v1S.0.8.pdf` and
`site/public/papers/paper_su_criterion_v1S.0.8.pdf`; arXiv tarball
rebuilt and standalone smoke-compiled clean. Convex bumped
(`paperVersions:bump` k57b0pej..., `activityFeed:add` j577wamk...,
`papers:setReadinessCap` -> 70, readback confirmed). All S9 science
gates now closed. Readiness 65 -> 70 — ROUNDS STOPPED (R2); next step
is venue selection, not further review rounds.

## v1S.0.9 (2026-09-18) — R3VERIFY: the intervening-decision-permitted round; 2 ESSENTIAL + 3 MAJOR genuinely-new-real closed; new open item S12; rounds stopped again

Campaign lane L2 ran the one review round directive R2 permitted after the
S7–A2-adjudication science sequence, on the exact v1S.0.8 artifact (sha256
`9f1fc41c…443d`): Claude Opus 5 INT (full-repo context, independent
re-derivation), Grok API (native-PDF), Gemini API (native-PDF); OpenAI/ChatGPT
absent per directive N. Raws: `project-context/peer-reviews/INT_v3/PSU_v1S.0.8_R3VERIFY_claude_opus_2026-09-18.md`,
`project-context/peer-reviews/R3VERIFY_PSU_Grok_brutal.md`,
`project-context/peer-reviews/R3VERIFY_PSU_Gemini_cosmology.md`.

**Genuinely-new-real, closed in v1S.0.9:**
- **ESSENTIAL** — Sec. III still printed the pre-adjudication `f^ρ_NL=-5/2`
  while Appendix A5 printed the corrected `f^ρ_NL=5(ε-7)/8=-55/16` for the
  identical quantity: the v1S.0.8 closing amendment landed in the Appendix
  only and was never propagated to the main text, leaving a literal internal
  contradiction in the served PDF for 11 days. Fixed: Sec. III now prints
  `5(ε-7)/8`, `-55/16`.
- **ESSENTIAL** — a raw UTF-8 `ρ` at `main.tex:514` threw a hard
  `! LaTeX Error: Unicode character ρ (U+03C1) not set up for use with LaTeX`
  and was silently dropped from the rendered PDF (readable as "the
  uniform-density (-)slice question"). arXiv's AutoTeX would very likely
  reproduce or hard-fail on the same error. Fixed: `(ρ-)` → `($\rho$-)`.
- **MAJOR** — the Appendix A5 closing-amendment paragraph narrated internal
  review/adjudication process ("reconciled by an independent adjudication…",
  "the earlier initial-label figure … came from composing … correcting the
  weight closes the gap") and used undefined symbols `λ'`, `A_2` — a
  directive-G leak-gate violation (Gemini's two ESSENTIAL findings + Claude's
  M1/M2). Rewritten to state the physics directly, define `λ'≡2λ` and `A_2`
  in place, and state the `f^ρ_NL` normalization (`P_{δN_{c,ρ}}`, not `P_ζ`).
- **MAJOR** — footnote 1 miscounted `f_map^fin`'s geometric contributions,
  listing the initial-label translation as a fifth contribution to
  `f_map^fin` when Appendix A2/A3 establish it is the *difference* that
  distinguishes `f_map^init` (independently caught by both Gemini and Claude).
  Fixed: footnote now says four contributions to `f_map^fin`, translation is
  the separate fifth term for `f_map^init`.
- **MINOR** — Reproducibility Statement omitted the two newest scripts
  (`psu_gates_S9_S10_2026_09_05`, `a2_lapse_monopole_adjudication_2026_09_07`)
  and their manifests, making the single newest number in the paper the
  least reproducibly sourced. Fixed: both scripts + SHA-256 prefixes + both
  manifests added; AI Usage Disclosure extended to cover the ρ-slice/A₂ work.
- Nit: `isoceles` → `isosceles` (×2).

**Re-flagged, no action (already dispositioned):** future-date / version-string
/ AI-disclosure-genre complaints (PSU-17/28, C27, C31); self-containedness and
Zenodo-DOI complaints (PSU-5/S4, PSU-16/S11 — still OPEN, unchanged, carried
as non-blocking per directive R2's genre/length/venue exception).

**New open science item, NOT closed, NOT dismissed — S12:** Gemini's pass-2
finding that Appendix A3's derivation of the translation term's exact zero
monopole (`T(ε,μ)`, "monopole 0 (all ε)") implicitly assumes `n_s=1` to drop
a trace-part contribution `∝(n_s-1)`; for general constant-ε, `n_s≠1` except
at isolated points, so the exact monopole may carry an ε-dependent correction
that (if present) would break the exact, ε-independent `f_δN^init≡-5` result.
Claude's independent check (same round) confirms the five A2 contributions
sum exactly to Eq. (4) and to monopole `-5ε/6` — a strong internal-consistency
check, but it does not independently re-derive the trace-part computation
Gemini is questioning. Full citation and required follow-up derivation:
`project-context/peer-reviews/DISPOSITIONS/PSU.md` §S12.

**Directive-G hygiene:** `\paperVersion`/`\paperTimestamp` bumped to
v1S.0.9/September 18, 2026. 4-pass pdflatex, 0 `^!` errors, 0 undefined
references (only a benign `OMS/cmtt/m/n` font-shape substitution warning),
leak-gate grep clean, 0 overfull hboxes >10pt except the pre-existing 8.31pt
Table I alignment overflow (unchanged, tracked, cosmetic). 7 pages (up from
6 — the reproducibility additions pushed one paragraph to a new page; page 7
is mostly whitespace, a cosmetic byproduct, not a content defect). PDF md5
`fcc3383afa72efebd7e4cf888c5851e0`, sha256
`2b225d0b3ceaa42d9223cc5b54fb50e1c9a06875c8d6d1292610d85e00d94fb7`,
three-way matched: fresh compile == `site/public/papers/paper_su_criterion_v1S.0.9.pdf`
== `public/papers/paper_su_criterion_v1S.0.9.pdf`. arXiv tarball
`project-context/SSOT/arxiv_tarballs/paper_su_arxiv_v1S.0.9.tar.gz` (sha256
`f8dc10f1f526b216a610c40766f80ea9a2be192c0ed500d8d261fd1a48668d4c`),
standalone-compile-verified (0 errors, 0 undef, 7 pages) in an isolated temp
dir before packaging.

**Readiness 70 → 72.** Rationale: this round both fixed a genuine
science-integrity regression (a served PDF with two contradictory values for
its own headline second-order result, live for 11 days) and improved
reproducibility/self-containment (leak-gate cleanup, missing script
citations, footnote correction) — real, verified progress. Held below a
larger bump by: (a) this was not a "0 genuinely-new-real" clean wave — the
round found real defects, so it does not count toward directive-K's
clean-wave streak; (b) it surfaced a new, unresolved open science question
(S12) rather than closing the paper out. `DISPOSITIONS/PSU.md`'s "current
version" header, which had gone stale for six versions, is reconciled in the
same bundle as a process fix.

**Exit decision (per this lane's brief, D-PSU-1/R2 disposition):** the
R3VERIFY round is **CLOSED** — no third board is scheduled on unchanged
content. The paper's overall status is **OPEN**, gated on science item S12.
No further INT/EXT review round on `paper-su` until S12 is resolved by a
from-scratch derivation of the translation term's trace part at general
(non-scale-invariant) constant-ε, or Houston explicitly defers/descopes it.
