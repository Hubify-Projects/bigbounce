# PSU v1S.0.2 R2 — skeptical truth-audit (2026-09-04)

**Auditor:** independent Opus truth-audit leg; no expected outcome supplied.
**Exact artifact:** `arxiv/paper_su_criterion/main.pdf` sha256 `812dbaf1…aca31`, md5 `fcbecd03…`, 4 pp
(byte-identical to `site/public/papers/paper_su_criterion_v1S.0.2.pdf`).
**Inputs:** Grok_brutal + Gemini_cosmology R2VERIFY raws, `INT_v3/PSU_v1S.0.2_R2_claude_fable_2026-09-04.md`,
receipt `INT_v3/ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY/preflight_receipt.json`,
`DISPOSITIONS/PSU.md`, `INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md`,
`research/theory_audit/psu_gates_S1_S2_2026_09_04.{md,py,json}`,
`research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md`.

**Classes:** (a) genuinely-new real — must close; (b) re-flag of an already-closed/dispositioned
item; (c) honestly-disclosed out-of-scope/limitation; (d) FALSIFIED (contradicted by the artifact
or by re-derivation); (e) OPINION / venue-genre preference.

## PLAN (in progress — sections appended and committed one at a time)
1. Independent re-derivation gate (Eq. (4) sign, the −5 composition, the ×2 robustness arithmetic).
2. Canonical finding list with class + citation + closure action.
3. Per-leg counts + convergence note (R1 → R2 genuinely-new).
4. CLOSURE PLAN: (i) editorial for v1S.0.3, (ii) science items.
5. R2 statement + DISPOSITIONS/PSU.md update.

---

## 1. Independent re-derivation gate (auditor's own sympy, scratchpad `psu_check.py`)

With $\lambda=1-\eps/3$, $f^{\rm in\text{-}in}=\tfrac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ and the paper's
Eqs. (3)–(4):

| check | result | bearing |
|---|---|---|
| $f^{\rm fin}_{\rm map}-f^{\rm init}_{\rm map}$ | $=-\dfrac{5\eps}{4(3-\eps)}(1-3\mu^2)$ (residual with the printed $+$ sign is $\neq0$; with $-$ it is exactly $0$) | Eq. (4) as printed has the **wrong sign** |
| in-in monopole, general $\eps$ | $-\tfrac{5}{18}(\eps-3)(\eps-6)$; $=-15/8$ at $\eps=3/2$ | matches the paper |
| $f^{\rm in\text{-}in}/\lambda+f^{\rm init}_{\rm map}$ | $\equiv-5$ **identically in $\mu$**, all $\eps$ | Grok PSU-E4 falsified |
| $\langle f^{\rm init}_{\rm map}\rangle_\mu$ | $-5\eps/6=-5/4$ at $\eps=3/2$ (the value at $\mu=0$ is $-5/8$) | Grok used $\mu=0$, not the monopole |
| doubling the from-scratch shape | monopole $-15/4$, gap to $-5$ is $-5/4$, ratio $\mathbf{4/3}$ | the paper's "$8/7$" is wrong |
| $(-35/8)/(-15/8)$ | $7/3$, **not** $2$ | $-35/8$ is Cai's *isoceles* amplitude ($2\times(-35/16)$), not a monopole |

Independent sources: `psu_gates_S1_S2_2026_09_04.md` §S1.2 Eq. (S1.1) states
$f^{\rm init}_{\rm map}-f^{\rm fin}_{\rm map}=+\tfrac{5\eps}{4(3-\eps)}(1-3\mu^2)$ — i.e. the committed gate note
itself carries the opposite sign to the paper's Eq. (4). `fnl_matter_contraction_adjudication_2026_09_02.md`
l. 22–23 gives the shape $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ (isoceles $-35/16$, **angle-averaged monopole
$-15/8$**) and l. 26/32/101 the uniform factor 2 on Cai's *amplitudes*.

## 2. Canonical findings (32 items)

Legs: G = Grok, Ge = Gemini, F = Fable. Line numbers refer to `arxiv/paper_su_criterion/main.tex` at the
commit that produced sha256 `812dbaf1…`.

### (a) GENUINELY-NEW REAL — 20 items

| ID | Legs | Finding | Citation / verification | Closure action |
|---|---|---|---|---|
| C1 | F M1, Ge 1, G E3 | Abstract (l. 39–41) calls $-5$ "the in-in monopole"; $-5$ is the **separate-universe** value, the in-in monopole is $-15/8$ | body l. 229, Table I; composition verified §1 | reword abstract |
| C2 | F M2, Ge 2 | Eq. (4) second equality sign (l. 144–145) | §1 sympy; gates §S1.2 Eq. (S1.1) | flip $+\to-$ |
| C3 | Ge pass-2 E1, F min1 | l. 126 "$I=1-\lambda$ reduces to $\eps/3$" contradicts $\lambda\equiv1-I/3$ | Eq. (2) l. 118–121; Table I ($I=\eps$) | "$1-\lambda=I/3$ reduces to $\eps/3$, i.e. $I\to\eps$" |
| C4 | F M4b, Ge 6 | l. 88–90: "$8/7$" treats $-35/8$ as a monopole; a uniform $\times2$ gives monopole $-15/4$, gap $-5/4$, **ratio $4/3$**; also $(-35/8)/(-15/8)=7/3\neq2$ | §1; adjudication l. 22–26, 101 | rewrite the sentence with $4/3$; state that $-35/8$ is Cai's isoceles amplitude |
| C5 | F M4a | Li, Quintin, Wang & Cai (arXiv:1612.02036, JCAP 2017) load-bearing via the adjudication but absent from the bibliography | adjudication l. 26, 38, 90; `main.tex` bib l. 326–347 has no Li entry | cite and address |
| C6 | F M4c | l. 90 "the headline $O(1)$ statement rests on the from-scratch value" — false: $\lambda=1-\eps/3=1/2$ is bispectrum-independent | Eq. (2); only the second-order $-5$ composition uses the in-in input | separate the linear from the second-order claim |
| C7 | F M6 | Refs: [6] pairs arXiv:1504.00351 (DPS "On separate universes", JCAP 1510, 059) with JCAP 1511, 043 (that is Conformal Fermi Coordinates, arXiv:1502.02011); [11] initials (D. Artigas, J. Grain); [12] first author (J. H. P. Jackson) | `main.tex` l. 331, 336, 337 | correct all three **after** checking the arXiv listings |
| C8 | F M6 | §IV never engages DPS "On separate universes", the closest prior statement of when a long mode is a local FRW | §IV l. 248–276 | add a paragraph: which DPS assumption fails at $I=O(1)$ |
| C9 | Ge pass-2 N1 | Eq. (2)/abstract: additive $O(k_L^2/a^2H^2)$ should carry the $\zeta_L$ amplitude | l. 37, 118–121 | move inside the bracket |
| C10 | Ge 4 | §IV uses $\eps$ for both the gradient-expansion order and the slow-roll parameter in one sentence | l. 248–251 | use $\eps_{\rm grad}$ or $k/aH$ |
| C11 | F min4 | Second-order treatment assumes $\zeta_L(t_i)=0$ (pure growing mode); Eq. (2)'s "any history" is a linear-order statement | l. 122–130 | state the assumption |
| C12 | F min2 | "dust" labels a $w=0$, $c_s=1$ scalar; for true dust $c_s\to0$ and $I=\zeta^{-1}\!\int(\eps/c_s^2)\dot\zeta\,dt$ diverges | Eq. (2) | relabel row; say what the criterion predicts for genuine dust |
| C13 | F min3 | Abstract "exact, invertible change of variable" | Eq. (2) is linear order, super-Hubble | "exact at linear order on super-Hubble scales" |
| C14 | F min5 | "the two coincide only as $\eps\to0$" applies the growing-mode monopole outside its domain (attractor in-in is $\tfrac{5}{12}(1-n_s)$) | l. 165, 229 | delete or qualify |
| C15 | F min6 | Kination $\eps=3$: $m=3/\eps-1=0$ is the constant mode ($\dot\zeta_L=0$, $I=0$); $\lambda\to0$ is a formal limit of the $\eps$-formula | Fig. 1 caption, l. 165 | qualify or drop |
| C16 | F min9 | Final slice is uniform-$\phi$ ( = comoving) and differs from uniform-$\rho$ at $O(k^0)$ when $I=O(1)$ — so Lyth–Malik–Sasaki's $\delta N=\zeta_{ud}$ is not the compared object | Eq. (1); adjudication l. 34 | state explicitly (second $O(1)$ slice ambiguity) |
| C17 | F min10 | Table I ekpyrosis row: "attractor-like" is not a value | Table I | give the Creminelli–Nicolis–Zaldarriaga statement or "n/a" |
| C18 | F min11 | Abstract "USR: $I=O(\eps)$"; exact is $I=\sqrt{\eps_s\eps_f}-\eps_f$ | l. 127–129 ($\lambda_{\rm USR}$) | $O(\sqrt{\eps_s\eps_f})$ |
| C19 | F min13 | Eq. (1): $\partial_iN^i$ is the coordinate divergence of the contravariant shift; $u^\mu\!\parallel\!n^\mu$ presumes a single scalar (no vorticity) | Eq. (1) | one clarifying sentence |
| C20 | F M5 | "We validate on four backgrounds" (l. 42–44): attractor + ekpyrosis are $I=0$ by definition, the USR row is not computed here, leaving one nontrivial check | §V Limits; Table I; R1 PSU-21/27 | "one nontrivial check plus three consistency limits"; mark the USR entry as not computed here |

### (b) RE-FLAG of an R1-dispositioned item — 6 items

| ID | Legs | Finding | R1 item | Status |
|---|---|---|---|---|
| C21 | G E1, G E2, Ge 3, F M3 | Standalone-reader failure: Eqs. (3)–(5), the second-order kernels, the general-$\eps$ in-in shape and the factor-2 claim all live in unpublished GitHub notes [21],[22] | **PSU-5 → gate S4** | **OPEN** — still real; closed only by the appendix in the closure plan |
| C22 | Ge 5, G N1 (part) | GitHub commit hashes are not an archival record; mint a Zenodo DOI | **PSU-16 → E9** | OPEN |
| C23 | F min7 | $\Theta$ used at l. 262 without definition | **PSU-25 → E8** | OPEN (regression: not fixed in v1S.0.2) |
| C24 | F min12 | Reproducibility file paths break mid-word | **PSU-6 → E2** | OPEN (regression) |
| C25 | G M2 | "The four validations are known analytic limits; no new observable" | **PSU-15 (OPINION, CLOSED)** | re-flag; significance judgement, root shared with PSU-10/S3. Real residual is C20 |
| C26 | Ge pass-2 m1 | "Futuristic dates" (2026) in the affiliation block and refs | **PSU-17 / PSU-28 (FALSIFIED, CLOSED)** | re-flag; the dates are today's (`\paperTimestamp`), a reviewer knowledge-cutoff artifact |

### (c) OUT-OF-SCOPE / disclosed — 1 item

| ID | Legs | Finding | Disposition |
|---|---|---|---|
| C27 | G N2, Ge 7 | Version tag `v1S.0.2` in the `\preprint` header | Deliberate lab bookkeeping on the review artifact; stripped in the arXiv packaging (P-round) build, not in the science round. `main.tex` l. 16, 21 |

### (d) FALSIFIED — 2 items

| ID | Leg | Claim | Falsification |
|---|---|---|---|
| C28 | G E4 (ESSENTIAL) | "$f^{\rm in\text{-}in}/\lambda+f^{\rm init}_{\rm map}=-5$ is false; $\eps=3/2$ gives $-3.75-0.625=-4.375$" | §1: the composition is identically $-5$ **in $\mu$ and in $\eps$**. Grok used $f^{\rm init}_{\rm map}(\mu=0)=-5/8$ where the monopole is $\langle f^{\rm init}_{\rm map}\rangle=-5\eps/6=-5/4$ (his $-4.375=-35/16$ is the isoceles in-in value, not a composition). No paper change |
| C29 | G M3 (MAJOR) | "Eq. (2) is claimed exact with no error estimate or domain qualifier" | `main.tex` l. 122–125 prints the qualifier immediately after Eq. (2) ("exact on super-Hubble scales … from a flat, super-Hubble initial slice; the dropped gradient term is $O(k_L^2/a_iH_i^2)$ …"); constant $\eps$ is used only at second order. Real residual = C11 |

### (e) OPINION / venue-genre — 3 items

| ID | Legs | Finding | Disposition |
|---|---|---|---|
| C30 | G M1, F min8 | Fig. 1 plots two straight lines fixed by the caption's algebra | Presentation judgement, but both legs agree it is uninformative; optional editorial action (replace with $\lambda_{\rm USR}(\eps_s,\eps_f)$ or $I(t)$), tracked with R1 PSU-14 |
| C31 | G N1 | "Delete the Reproducibility and AI-usage sections" | Venue-genre preference; lab policy (directive Q2) requires reproducibility manifests. Archival-DOI part is real → C22 |
| C32 | G N3 | "'No discrepancy in the physics, only in which variable' is interpretive" | It is the S3-adjudicated conclusion of the composition ($f^{\rm in\text{-}in}/\lambda+f^{\rm init}_{\rm map}\equiv-5$), source-cited to `threading_map_second_order_2026_09_04.md` §4 and `psu_gates_S1_S2_2026_09_04.md` §S3. Keep |

## 3. Per-leg counts

| Leg | Raw findings | (a) new-real | (b) re-flag | (c) OOS | (d) falsified | (e) opinion |
|---|---|---|---|---|---|---|
| Grok (REJECT) | 10 | 1 (C1) | 3 (C21×2, C22, C25) | 1 (C27) | 2 (C28, C29) | 3 (C30–C32) |
| Gemini (MAJOR REVISIONS) | 10 | 7 (C1–C5, C9, C10) | 2 (C21, C22) | 1 (C27) | 1 (C26) | 0 |
| Fable INT (MAJOR REVISIONS) | 19 (6 MAJOR + 13 minor) | 18 | 3 (C21, C23, C24) | 0 | 0 | 1 (C30) |

**Canonical: 32 items — 20 genuinely-new real, 6 re-flags (4 still OPEN), 1 out-of-scope,
2 falsified, 3 opinion.**

## 4. Convergence note (R1 → R2)

R1 (v1S.0.1, sha `cc0dfb84…`): 38 raw → 28 canonical, **21 genuinely-new real**.
R2 (v1S.0.2, sha `812dbaf1…`): 39 raw → 32 canonical, **20 genuinely-new real**.
Clean-wave count stays **0** (directive K); the paper is not converged.

Two observations the count alone hides:

1. **The R2 new-real set is qualitatively different.** R1's items were load-bearing physics (label
   resolution, the criterion's normalisation, the framing) and were resolved by gates S1/S2/S3. R2's
   20 are one algebra sign (C2), one arithmetic error inherited from an R1 *disposition* (C4), the
   reference layer (C5, C7, C8), and 15 statement-precision items. The science core survived a
   second independent re-derivation (Fable re-derived Eq. (1) and the linear map from scratch; this
   audit re-derived the composition and both monopoles).
2. **Process finding (new).** C4 traces to R1's own PSU-4 disposition, which wrote "with $-35/8$ the
   gap is $-5/8$, factor $8/7$" and that sentence was transcribed into the manuscript. A number
   supplied by a truth-audit disposition entered the paper without an independent re-derivation, and
   it was wrong ($-35/8$ is Cai's isoceles amplitude, not a monopole; the correct counterfactual
   ratio is $4/3$). **Rule for this lab: any number a disposition hands to a manuscript gets the
   same independent re-derivation gate as a number in the manuscript.**

## 5. CLOSURE PLAN

### (i) Editorial — `v1S.0.3` (exact lines in `arxiv/paper_su_criterion/main.tex`)

| # | Line(s) | Edit |
|---|---|---|
| E-1 | 39–41 | C1/C13/C18/C20 abstract rewrite: "…is an **exact linear-order, super-Hubble** change of variable…; at second order the initial-position label composes the in-in bispectrum back to **the isotropic separate-universe value, $-5$**, for every constant $\eps$… ultra-slow-roll ($I=O(\sqrt{\eps_s\eps_f})$)… **one nontrivial check (matter contraction) plus three consistency limits**" |
| E-2 | 144–145 | C2: `=f_{\rm map}^{\rm init}+` → `=f_{\rm map}^{\rm init}-`; re-run the sympy gate on the **printed** Eq. (4) (the current script asserts only the composed totals) |
| E-3 | 126 | C3: "$1-\lambda=I/3$ reduces to $\eps/3$ for constant $\eps$ (i.e. $I\to\eps$), so $\lambda\equiv1-I/3=1-\eps/3$" |
| E-4 | 88–90 | C4/C6: "Cai *et al.* quote a squeezed (isoceles) amplitude $-35/8$; the from-scratch shape is uniformly a factor of 2 smaller ($-35/16$, monopole $-15/8$). Were the from-scratch shape uniformly twice as large, the monopole would be $-15/4$ and the gap to $f_{\delta N}^{\rm init}=-5$ would be $-5/4$, **a ratio of $4/3$ rather than $8/3$**. The **linear** criterion $\lambda=1-\eps/3$ is independent of any bispectrum; only the second-order $-5$ composition uses the in-in input." |
| E-5 | 331, 336, 337 + new | C5/C7: verify against the arXiv listings, then fix [6] (split DPS "On separate universes" arXiv:1504.00351, JCAP **1510, 059** from Conformal Fermi Coordinates arXiv:1502.02011, JCAP 1511, 043), [11] "D.~Artigas, J.~Grain, V.~Vennin", [12] "J.~H.~P.~Jackson \etal"; add Li, Quintin, Wang & Cai, arXiv:1612.02036 |
| E-6 | §IV (248–276) | C8 paragraph on DPS "On separate universes" (which assumption fails at $I=O(1)$); C10 rename the gradient-expansion order to $\eps_{\rm grad}$ |
| E-7 | 37, 118–121 | C9: error term inside the bracket, $\zeta_{L,f}[1-I/3+O(k_L^2/a^2H^2)]$ |
| E-8 | 122–130 | C11 (state $\zeta_L(t_i)=0$ for the second-order map), C19 (Eq. (1) caveats), C16 (uniform-$\phi$ vs uniform-$\rho$; LMS $\delta N=\zeta_{ud}$ is not the compared object) |
| E-9 | Table I + 165 | C12 (relabel "dust" → "$w=0$ scalar, $c_s=1$"; note genuine dust $c_s\to0$), C17 (ekpyrosis row), C14, C15 (kination/attractor domain qualifiers), C20 (USR entry marked not computed here) |
| E-10 | Reproducibility | C23 ($\Theta$ definition), C24 (`\url`/breakable macro for paths), C22 (Zenodo DOI once minted) |
| E-11 | new Appendix A | **C21 — required.** See below |

**Appendix A (self-containedness) — the audit finds this REQUIRED for a standalone PRD note:**
three of four legs (Grok E1/E2, Gemini 3, Fable M3) independently judged the note unverifiable
without [21],[22], and this audit could verify the *composition* but not the *kernels*. Transcribe
from the committed notes:

1. `threading_map_second_order_2026_09_04.md` §2 — the second-order lapse/shift solution used
   (constant $\eps$, $c_s=1$) — and §3 "Totals" — the five kernel contributions `zlap`, `psi2`,
   `grad`, `wl_fin`, `lab_init` with their closed forms.
2. `psu_gates_S1_S2_2026_09_04.md` §S1.1–S1.3 — the two worldline labels, the translation
   $\xi^i=\int N_L^i dt$, Eq. (S1.1) $T=\tfrac{5\eps}{4(3-\eps)}(1-3\mu^2)$ (zero monopole), and the
   per-label maps.
3. `fnl_matter_contraction_adjudication_2026_09_02.md` l. 22–23 — the general-$\eps$ in-in **shape**
   $\tfrac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ (the note currently prints only its monopole), which
   the isotropy of $f_{\delta N}^{\rm init}$ depends on, with its source.
4. An explicit sentence (Fable Q4) that the map derivation takes **no in-in and no $\delta N$ input** —
   verify against the script before writing it. Without it a referee cannot separate an identity
   from a fit to the lab's own $-5$.

### (ii) SCIENCE items (not closable by editing)

| Gate | Item | Why it is science |
|---|---|---|
| **S6** | Verify (not assert) that the second-order map used no in-in/$\delta N$ input; add the printed-Eq. (4) assertion to the sympy gate | identity-vs-fit is the note's central credibility claim |
| **S7** | The Cai 2009 factor-2 dispute: either an equation-level appendix locating the slip, or downgrade to "differs from [18]"; must engage Li, Quintin, Wang & Cai 2017, which reproduces Cai's polynomial (adjudication l. 38) | contradicting a published result needs in-manuscript evidence |
| **S8** | Turn the USR row into a real validation: exact numerical $\delta N(\phi,\pi)$ at finite $\eps_s$ (e.g. $\eps_s=10^{-2},\eps_f=10^{-6}$, $\lambda-1\approx-3\times10^{-5}$) — Fable Q3 | the only route to more than one nontrivial check |
| **S9** | To which final slice (uniform $\phi$ or uniform $\rho$) is the separate-universe $-5$ computed, and is it the same on both? — Fable Q1 | a second $O(1)$ slice ambiguity of the same order as the effect |
| **S10** | $f^{\rm init}_{\rm map}$ when $\zeta_L$ carries a constant piece as well as the growing mode ($I<\eps$) — Fable Q2 | §III claims a general-history statement; kernels exist only for a constant-$\eps$ power law |
| **S11** | Zenodo DOI for the exact script release (carried from R1 E9) | archival record |
| — | Bianchi-I anisotropic separate-universe recovery of the in-in monopole/quadrupole (adjudication l. 40) | remains the open physics route; out of scope for this note |

## 6. R2 statement

Verdict board: Grok **REJECT**, Gemini **MAJOR REVISIONS**, Fable INT **MAJOR REVISIONS**. Verdict
words are diagnostic, not a gate (directives P, H-refined); the operative result is **20
genuinely-new real findings**, so `paper-su` is **not converged** and its clean-wave count is 0.

Per **directive R2** (convergence budget: at most two consecutive rounds without an intervening
science or scope decision), R1 and R2 exhaust the budget. **After `v1S.0.3` lands the E-1…E-11
closures, review rounds on `paper-su` STOP** until a science or venue decision is taken on S6–S10 —
specifically: does the lab fund S7 (equation-level Cai reconciliation) and S8 (numerical USR
validation), or is the note rescoped (e.g. Brief Report / comment, or held pending the Bianchi-I
route)? Running R3 on an editorially-patched v1S.0.3 would measure referee variance, not progress.

*Integrity note:* this audit consulted `DISPOSITIONS/PSU.md` and the R1 audit only to classify
re-flags; every physics disposition above was re-derived independently (§1) before being written,
and no finding was dispositioned non-real on assertion. No verdict was faked; the two FALSIFIED
items carry line-level citations to the artifact.
