# P-SU status — current authoritative section

**Current candidate:** v1S.0.2 · 2026-09-04 ·
`arxiv/paper_su_criterion/main.tex`

**Title:** "The separate universe computes a different variable: an exact
criterion for $\delta N=\zeta$ in non-attractor phases"

**Status: readiness 55 (up from 40). First R1 board closed under decision
D-PSU-1 (see `project-context/PAPER_LINEAGE_2026-08-05.md`, final section):
Claude Fable (INT), Grok API, Gemini API — 21 genuinely-new-real findings,
5 falsified, 1 opinion, 1 out-of-scope, per
`project-context/peer-reviews/INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md`.
All editorial items (E1–E10) closed and all three science gates resolved
(`research/theory_audit/psu_gates_S1_S2_2026_09_04.{md,py,json}`, S1/S2/S3
RESOLVED). Per directive R2, one verification round is permitted after
D-PSU-1; no further rounds beyond that without a new science or scope
decision.**

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

## Close-the-gap section (open items, as of v1S.0.2)

- Per directive R2, exactly one more verification round is permitted on this
  paper before another science/scope decision is required — the next INT/EXT
  round should target the closed E1–E10/S1–S3 items for re-audit, not open
  new science.
- S4 (self-containedness appendix reproducing the in-in kernel and
  second-order map derivation in-paper, or posting the companion notes as a
  citable preprint) and S5 (opus-tier confirmation that the literature
  positioning language in "What is new" is precise, beyond this bundle's
  WebFetch abstract check) remain open per the truth audit's ordering note.
- Venue/arXiv-category selection not yet made (candidate: gr-qc or
  astro-ph.CO, cross-list astro-ph.CO given the P2/P2L family).
- Site (`site/src/data/papers.ts` etc.) not yet updated — explicitly out of
  scope for this lane per the originating task (another lane owns
  `site/src`).

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
