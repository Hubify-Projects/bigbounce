# P1N v1N.0.2 — R2 truth audit (verdict-first, per-finding)

**Auditor:** Opus truth-auditor, independent of the review legs. No leg's verdict word
was used to triage; every finding was settled against source (`main.tex` line numbers,
the frozen theory-audit artifacts, P1C v1C.0.16 / P1A v1A.0.127) or against an
independent recomputation committed as
`research/theory_audit/p1n_r2_checks_2026_09_02.py`.

**Manuscript:** `arxiv/paper1bc_ech_note/main.tex` / `main.pdf`, v1N.0.2, 10 pp.
**Exact-PDF binding — sha256:** `790795fe3d0cd5c3ba68234ddf3a5336d11fbfa1d402c9bc9d4b3be3013f125d`
(re-verified this round with `shasum -a 256`; matches the round label).
**Round dir:** `INT_v3/ROUND_2026-09-02-P1N-v1N.0.2-EXACTPDF-790795fe-R2/`
**Date:** 2026-09-02.

## Legs

| Leg | Raw | Verdict word | Findings |
|---|---|---|---|
| Claude INT (opus, source+PDF) | `P1N_claude_r2_leg.md` | major-revisions | 7 MAJOR / 13 MINOR + 21 R1-verification rows |
| Grok API (`grok-4.3`, native PDF, brutal) | `../../ROUND_2026-09-02-P1N-v1N.0.2-EXACTPDF-790795fe-R2_P1N_Grok_brutal.md` | REJECT | 3 ESSENTIAL / 3 MAJOR / 2 minor-nit |
| Gemini API (`gemini-3.1-pro-preview`, native PDF) | `../../ROUND_2026-09-02-P1N-v1N.0.2-EXACTPDF-790795fe-R2_P1N_Gemini_cosmology.md` | MAJOR REVISIONS | 1 ESSENTIAL / 2 MAJOR / 5 minor-nit |
| Perplexity | — | **ABSENT** | not run; recorded absent, never back-filled |

Degraded-round check (skill Rule 4): no `[FALLBACK` tag and no failed-leg body in either
API raw; both carry a real wall time (112.2 s / 496.0 s) and a real packet hash. The round
is **not** degraded. Perplexity's absence is recorded, not counted as a clean leg.

## Independent recomputation

`research/theory_audit/p1n_r2_checks_2026_09_02.py` (committed with this audit) runs six
checks with printed intermediates and hard asserts; all pass:

- **C1** `-24 M_Pl^2 αβ` with the paper's own `α=κγ²/[2(1+γ²)]`, `β=κγ/[4(1+γ²)]`
  (`main.tex:198–199`) and its own `κ=8πG=8π/M_Pl²` (`main.tex:180`) gives
  `-24π κ γ³/(1+γ²)²`. Printed RHS of Eq. (13) is `-3κγ³/(1+γ²)²`.
  Ratio computed exactly: **`8π = 25.132741228718346`**.
- **C2** corrected ratio `O4/O5 = 8πγ/(1+γ²) = 5.650` at γ=0.2375 (printed: `γ/(1+γ²)=0.2248`).
  Bare invariant `κ→8πG`: `-192π²G γ³/(1+γ²)²` — **one** power of `G`, as dimensions require
  (`(J⁵·J⁵)` is mass-dim 6, a dim-4 density needs a dim-(−2) coefficient).
- **C3/C4** structural contractions from scratch in a flat mostly-plus frame with generic
  `α, β, J⁵`: `ε^{μνρσ}T^I{}_{μν}T_{Iρσ} = -24αβ(J⁵·J⁵)` and
  `ε^{μνρσ}T^I{}_{μν}e_{Iρ}J⁵_σ = -6α(J⁵·J⁵)` → `O5 = -3κ[γ²/(1+γ²)](J⁵·J⁵)`.
  **The tensor algebra of Eqs. (12) and (13) is correct; only the κ substitution fails.**
- **C5** random tetrad × random `so(1,3)` curvature with pair antisymmetries:
  `ε^{μνρσ}e^I_μ e^J_ν R_{IJρσ} - ε^{μνρσ}R_{μνρσ} = 0` exactly. `O1 ≡ O6` identically.
- **C6** parity bookkeeping for `O5` off shell (see DP1N-23).

## (a) The 8π — settled

**Verdict: INHERITED-ERROR (real).** Eq. (13) at `main.tex:796–799` is wrong by exactly
`8π` under the paper's own conventions; the printed `O4/O5 ≃ 0.22` inverts to **5.65**, so
`O4` is ~5.7× *larger* than `O5` at the benchmark, not 4.5× smaller. The correct coefficient
is **`-24πκ γ³/(1+γ²)²`**, equivalently **`-192π²G γ³/(1+γ²)²`**.

The identical error is in the frozen restoration source **P1C v1C.0.16 `main.tex:2118–2123`**
(`\label{eq:o4_onshell}`), which additionally prints the bare invariant with `G²` — a second,
independent dimensional error not present in the Note. **This is a science decision for P1C's
own record as well as the Note's:** P1C's Eq. (o4_onshell), its `0.22` ratio sentence, and its
`-192π²G²` clause all require the same correction, and
`arxiv/scripts/dim4_parityodd_enumeration.py` /
`research/theory_audit/operator_basis_adjudication_2026_08_07.{py,json,md}` must be re-run and
re-committed against the corrected value so artifact and manuscript agree.

**The no-go conclusion is unaffected.** `O4` and `O5` remain the same Fierz-closed
`(J⁵·J⁵)` structure at the same `M_Pl^{-2}` power, and the corrected `O4` still scales as
`γ³/(1+γ²)² ~ 1/γ → 0` as `γ→∞`, so "O4 switches off in the Einstein–Cartan limit" survives.
What does **not** survive is the *sentence around it*: the Note currently reads as though `O4`
were a small correction to `O5`, and it is the larger of the two — the same size-ordering
mistake the paper elsewhere (correctly) makes a point of getting right for `β/α`.

## (b) O1 ≡ O6 — settled

**Verdict: GENUINELY-NEW-REAL (disclosure regression; presentation, not physics).**
The connection varied in Eq. (1) is a metric-compatible `so(1,3)` spin connection, so the
tetrad converts frame to coordinate indices exactly and
`ε^{μνρσ}e^I_μ e^J_ν R_{IJρσ} ≡ ε^{μνρσ}R_{μνρσ}` **identically, off shell and on shell,
torsion or no torsion** (C5). `O1^{[4]}` and `O6^{[4]}` as defined in Eq. (10)
(`main.tex:727–737`) are the same density written twice, so the first null-space relation
`O1 - O6 = 0` in Eq. (11) is a definitional identity, not a computational result.

Crucially this is **not** a defect of the underlying adjudication and **not** an overstatement
in P1C: **P1C v1C.0.16 `main.tex:2041–2043` says so in the open** — "the first is the tetrad
conversion `e^I_μ e^J_ν R_{IJρσ}=R_{μνρσ}` … so O1 and O6 are *literally the same density*" —
and **P1C `main.tex:2690`** (Table row O6) reads "`= O1 exactly (tetrad conversion)`". P1C
further states that the redundancy is *deliberate*, that the list is a spanning set of
recognizable invariants and not a basis, and names maximal-rank independent subsets
`{O2,O3,O4,O5}` and `{O1,O3,O4,O5}`. This is consistent with
`operator_basis_adjudication_2026_08_07` (rank-4 spanning list). **The Note dropped that
clause in the merge.**

The honest statement the Note should print is therefore P1C's, not Claude's option (a) or (b):
keep the six-member *deliberately redundant* generating list, and restore in one clause that
(i) `O1 - O6 = 0` **is** the tetrad conversion, so O1 and O6 are literally the same density,
(ii) the list contains **five distinct densities**, (iii) the rank is four with a
two-dimensional null space of which **one direction is that duplication and only
`2O1+2O2-O4=0` carries content**, and (iv) rank two modulo total derivatives is unchanged.
The abstract and Conclusions must not sell "six-member spanning list, rank four" as a
computational finding without that clause. No disposal statement in Sec. VI changes; removing
the duplicate makes the list smaller and opens no escape channel. **Grading this a science
decision** (it changes what the enumeration claims), not a copy-edit.

## (c) Barrier sourcing — settled, per barrier

Machine-checked over `main.tex:463–589` (`\cite` extraction): **exactly four citation
instances, all inside B12** (`Golden2026P1a`, `Ashtekar2011` ×2, `GhoshMitra2005`). No
barrier entry contains a derivation.

| Barrier | Support in the Note | Support in the public P1A DOI record | Status |
|---|---|---|---|
| B1 (ultralight-torsion mass spectrum, `g_eff ~ 1/(M_Pl√|t_3|)`) | scaling ansatz, self-labelled "not a derived equality"; no citation | PGT parameter `t_3` provenance (Hayashi–Shirafuji, Yo–Nester, Blagojević–Hehl) is **not** in the Note's bibliography | **bare assertion** |
| B2 (mass protection ⟺ no geometric fingerprint) | none — a biconditional with neither proof nor reference | none cited | **bare assertion** |
| B3 (diff-invariance forces curvature coupling; "decouples precisely at the bounce density") | none | none cited | **bare assertion** |
| B4, B5, B6, B8 | none | none cited | **bare assertion** |
| B7 (γ uniquely fixed) | cross-reference to `Sec.~\ref{sec:theory}`, which contains no such content (verified: "area" occurs only at `main.tex:515` and `561`) | Ashtekar–Singh / Ghosh–Mitra are in the bibliography but not cited here | **bare assertion + empty cross-ref** → DP1N-26 |
| B9 (Liouville / no irreversible post-bounce selection) | self-labelled heuristic; measure not stated; no citation | none cited | **bare assertion (honestly tiered)** |
| B10, B11, B13 | none | none cited | **bare assertion** |
| B12 (`ρ_crit/ρ_Pl ≃ 0.27–0.41`) | `Golden2026P1a`, `Ashtekar2011` ×2, `GhoshMitra2005`; window + scheme-dependence explained in-paper | **P1A v1A.0.127 `main.tex:1527–1529`**; recomputed `√3/(32π²γ³)` → 0.4094 / 0.2666, squares 0.168 / 0.0711 | **sourced + derivable** |
| B14 (transparency theorem) | full statement + `*Proof.*` in Sec. III `main.tex:312–357` | the key step `½ε^{μνρσ}R_{μνρσ}(Γ̊)=0` from `R_{μ[νρσ]}=0` re-checked and correct | **derived in-paper** |

**2 of 14 supported; 12 of 14 bare assertions.** The abstract nevertheless calls them
"fourteen distinct mechanism-class constraints" that "jointly close" the four channels, and
routes the reader for derivations to `Golden2026P1cArxiv`, which the bibliography itself
labels a non-refereed, not-independently-submitted repository draft. Claude MAJOR 3 and
Grok M1 are the same finding at different resolution; Gemini N2 is the same defect seen from
the Data-Availability end.

## (d) Must the Note engage Popławski's dark-energy claim? — settled: **yes**

**Verdict: GENUINELY-NEW-REAL, MAJOR.** The title claims what ECH "cannot do for dark
energy"; the most prominent published contrary claim is Popławski, *Gen. Rel. Grav.* **44**,
491 (2012), "Cosmological constant from quarks and torsion" — Ref. [10] in this very
bibliography. It is cited twice (`main.tex:145–147` and the Acknowledgments), paraphrased in
one subordinate clause, and **never stated, never quantified, never mapped to R1–R4, never
closed.** The paper builds its entire positive half on identifying its contact term with
Popławski's *bounce* term at exact evidential strength (DP1N-04, re-verified closed this
round) and then declines to make the corresponding identification for the *dark-energy* half,
which is the half it claims to close. A referee cannot tell whether the manuscript refutes
Popławski's Λ or four routes of the author's own construction that may or may not contain it.
Half a page: state the mechanism with its own equation, map it onto the R1–R4 taxonomy (it is
closest to R1, where Sec. II's `G_s<0` result already does the work), and name the closing
barrier and its tier. If it does not map onto R1–R4, then "the four enumerated channels" is
incomplete and the abstract's closure claim is too strong — that is the honest alternative,
and it must be one or the other.

---

## Canonical finding table

Fingerprints deduped across the three legs and against the R1 board (`DISPOSITIONS/P1N.md`,
DP1N-01–20). New canonical IDs continue the sequence from DP1N-21.

| ID | Claim | Location | Verification | Verdict | Sev | Closure instruction |
|---|---|---|---|---|---|---|
| **DP1N-21** | Eq. (13) wrong by exactly `8π`; `O4/O5` ordering inverted | `main.tex:796–804`; PDF p. 7 | C1/C2 exact: ratio `= 8π`; structural `-24αβ` independently confirmed (C3). Present verbatim in **P1C v1C.0.16 `main.tex:2118–2123`**, which additionally prints `-192π²G²` (dimensionally impossible) | **INHERITED-ERROR** (Claude MAJOR 1 = Gemini P1N-E1) | MAJOR | Eq. (13) → `-24πκγ³/(1+γ²)²`; ratio → `8πγ/(1+γ²) ≃ 5.65`; rewrite the surrounding sentence (O4 is the *larger*); **same correction in P1C Eq. (o4_onshell) incl. `G²`→`G`**; re-run + re-commit `dim4_parityodd_enumeration.py` and `operator_basis_adjudication_2026_08_07.*` |
| **DP1N-22** | `O1 ≡ O6` as defined; first null relation is a tautology; "six-member spanning list, rank four" partly presentational | Eq. (10) `727–737`, Eq. (11) `749–751`, rank claim `744–748`, abstract `92–98`, Conclusions `937–941` | C5 exact. **P1C `main.tex:2041–2043` + `2690` disclose it explicitly**; the Note dropped the clause | **GENUINELY-NEW-REAL** (disclosure regression) | MAJOR | Restore P1C's clause: `O1-O6=0` *is* the tetrad conversion; five distinct densities; rank 4 with one null direction being the duplication and only `2O1+2O2-O4=0` carrying content; redundancy deliberate. Adjust abstract + Conclusions. Do **not** delete O6 |
| **DP1N-23** | `O5` parity classification: the Note says "parity-even off shell"; the list is advertised as strictly parity-odd | `786–789`; list intro `721–723` | C6: `ε`(odd)×`T`(even)×`e`(even)×`J⁵`(odd) = **even**. `O5` is P-even **both** off and on shell. Wording inherited from **P1C `2096–2100`**; the "off shell" qualifier was added in the Note | **INHERITED-ERROR** (Gemini P1N-M2 **CORRECT**; Claude MINOR 1's premise "O5 is P-odd off shell" **FALSIFIED**) | MAJOR | State that `O5` is admitted by the **ε-construction rule**, not by being P-odd, and that the list is a mixed-parity ε-contracted set; delete the "the parity-odd label belongs to the pre-reduction density" claim in both Note and P1C. No rank/closure change |
| **DP1N-24** | Barrier catalog: 12 of 14 entries carry no citation and no derivation | Sec. IV `463–589`; abstract `85–92`; Conclusions `934–936` | Table (c) above; `\cite` extraction gives 4 instances, all in B12 | **GENUINELY-NEW-REAL** (Claude MAJOR 3 = Grok M1; residual of DP1N-06) | MAJOR | Per barrier B1–B11, B13: a literature citation **or** 2–4 lines of derivation (appendix). Any barrier supportable by neither is demoted out of the "fourteen mechanism-class constraints" headline and presented as conjectural |
| **DP1N-25** | Popławski's dark-energy claim is never stated, mapped, or closed | `145–147` only | §(d) above; Ref. [10] in the bibliography | **GENUINELY-NEW-REAL** (Claude MAJOR 4) | MAJOR | ~0.5 pp subsection: state the mechanism with its equation, map to R1–R4, name closing barrier + tier — or weaken "the four enumerated channels" |
| **DP1N-26** | B7 ("γ fixed at a single universal value", `Sec.~\ref{sec:theory}`) contradicts B12 ("scheme-dependent"); the cross-reference is empty | B7 `511–517`; B12 `555–573` | grep: "area" occurs only at `515` and `561`; Sec. II introduces γ as "constant" and nothing more | **GENUINELY-NEW-REAL** (Claude MAJOR 5) | MAJOR | Cite the area-spectrum/entropy result (`Ashtekar2011`, `GhoshMitra2005`, both already in the bib); restate B7 as "γ is a fixed parameter of the theory, not a field with cycle-to-cycle dynamics"; note residual scheme-dependence (B12) supplies no landscape; repoint the cross-reference |
| **DP1N-27** | Route 3's "mass-dimension scaling relation" is never written down; one input maps to a six-order-wide 61–67 output | `645–652` | Eq. (9) integration independently reproduces `1.38e-6` vs the paper's `1.4e-6`; the propagation step is absent from the source | **GENUINELY-NEW-REAL** (Claude MAJOR 6 = Gemini P1N-M1) | MAJOR | Display the scaling relation as an equation with inputs; state what is varied to give 61–67; label the tier (Tier-III is admissible, but must be shown) |
| **DP1N-28** | Abstract item (i) ("no nonzero solution") is asserted; the gap equation, its regulator, and the argument are deferred to a non-refereed deposit | `300–307`; abstract `75–82` | `G_s<0` **is** established in-paper (Eq. 5 Fierz row + Eq. 7); the step to "no nonzero solution" is not | **GENUINELY-NEW-REAL** (Claude MAJOR 7; Grok E2 second half) | MAJOR | Write the mean-field gap equation `M = 2G_s M I(M,Λ)` with `I>0`, state the regulator, give the three-line no-solution argument; keep the deposit citation for the full regulated treatment |
| DP1N-29 | Table I caption calls `κ` "the Barbero–Immirzi symbol"; γ is the BI parameter, κ = 8πG | `435–439` | Eq. (1) `main.tex:180` | GENUINELY-NEW-REAL (Claude MINOR 2; closes DP1N-15's residual defect) | MINOR | "…and the gravitational coupling `κ`" |
| DP1N-30 | Table II R3 row cites a "chiral-count bound" that appears nowhere else | `696–698` | grep: single occurrence | GENUINELY-NEW-REAL (Claude MINOR 3) | MINOR | Import the bound or delete the clause |
| DP1N-31 | SHA pin applied to `\artifactbase` but not to the `.bib`: four entries still resolve through mutable `tree/main` / `blob/main` | `references.bib:279,287,295,303` | `\repoSHA` = `ded46bc5…` verified on `main` and `origin/main`; the four bib URLs are unpinned | GENUINELY-NEW-REAL (Claude MINOR 4; residual of DP1N-06) | MINOR | Pin to the same SHA; mint Zenodo version DOIs for P1C and the three theory-audit artifacts |
| DP1N-32 | Provenance/version-history language survives in the `.bib` (printed as ref. [26]) and as in-text tags "READING-I" and "(P1A [15])" | `references.bib:280` + `TorsionOnshell2026` note; `main.tex:202`, `559` | `main.tex` grep for `supersed*|earlier draft|this Note|merges` = 0 hits, so the body is clean; the bib and the two tags are not | GENUINELY-NEW-REAL (Claude MINOR 5 = Gemini P1N-N1; residual of DP1N-08) | MINOR | Rewrite both `note` fields to say what the artifact *is*; drop "READING-I" and the "(P1A …)" tag from the body |
| DP1N-33 | Route 2's "≳58 orders relative to the observed birefringence amplitude" misdescribes Eq. (8), whose LHS is normalized by `β_obs` **and** `M_Pl(α/M)`; Eq. (8) also carries the same factor on both sides | `598–621` | numeric chain `1.7e-60` reproduces; relative to `β_obs` alone the suppression is ~`1e-62` | GENUINELY-NEW-REAL (Claude MINOR 6 = Gemini P1N-N5) | MINOR | Say which ratio the order count refers to; simplify Eq. (8) by cancelling the common factor |
| DP1N-34 | Eq. (8) is "anchored in" Shapiro–Teixeira but that result is never stated | `598–607` | no statement of the one-loop result in the source | GENUINELY-NEW-REAL (Claude MINOR 7) | MINOR | One or two sentences quoting the renormalization result the ansatz rests on |
| DP1N-35 | One sentence asserts "signature-independent" and disclaims a signature bridge in the same breath | `223–231` | the supporting `ρ+3p<0` argument is gestured at, not shown | GENUINELY-NEW-REAL (Claude MINOR 8; refines DP1N-04) | MINOR | Display the one-line `ρ+3p<0` argument or end at the disclaimer |
| DP1N-36 | `[R1]`–`[R4]` tags used on p. 4 before Routes 1–4 are defined on p. 5 | `463` vs Sec. V | source order | GENUINELY-NEW-REAL (Claude MINOR 9 = Grok N1) | MINOR | One-line definition of R1–R4 at the head of Sec. IV |
| DP1N-37 | Abstract is 435 words and fills p. 1; CQG guidance ≈300 | abstract | word count from source | GENUINELY-NEW-REAL (Claude MINOR 10) | MINOR | Cut to ~250–300; lead with the structural dichotomy |
| DP1N-38 | The sole Tier-I result runs as prose with an italic "*Proof.*" and unenumerated hypotheses | Sec. III `312–357` | mathematical content re-checked and **correct** | GENUINELY-NEW-REAL (Claude MINOR 11; presentational) | MINOR | Numbered `Theorem` environment, hypotheses (H1)–(H5), excluded cases listed |
| DP1N-39 | No sentence positions the transparency theorem's novelty against the standard Holst statement; Holst (1996) is absent from the bibliography | Sec. III | bibliography grep | GENUINELY-NEW-REAL (Claude MINOR 12; the "standard result" half re-flags R1 Gemini N1, already dispositioned) | MINOR | One positioning sentence; add Holst 1996 |
| DP1N-40 | `\paperVersion` defined and never used | `main.tex:51` | grep | GENUINELY-NEW-REAL (Claude MINOR 13; residual of DP1N-08) | MINOR | Delete the dead macro |
| DP1N-41 | γ = 0.2375 is used as load-bearing from the abstract on but is first cited only inside B12 on p. 5 | `103`, `231`, `245` vs `561` | `Ashtekar2011` cited at `561` only | GENUINELY-NEW-REAL (Grok E1 — real, but **severity mislabeled** ESSENTIAL→MINOR: the value *is* sourced in-paper) | MINOR | Cite `Ashtekar2011` at first use in Sec. II |
| DP1N-42 | Eq. (9)'s integration does not state the `G`/`M_Pl` normalization used, so a reader could be off by `8π` | `632–652` | independent integration reproduces `1.38e-6` using `M_Pl = 1.22e19` GeV | GENUINELY-NEW-REAL (Gemini P1N-N4) | MINOR | State `G = 1/M_Pl²`, `M_Pl = 1.22×10^19` GeV explicitly — especially given DP1N-21 |
| DP1N-43 | Abstract's `1/(2γ) -- 2.11` en-dash reads as a minus sign | `102–104` | render | GENUINELY-NEW-REAL (Gemini P1N-N3) | NIT | Replace with ", which evaluates to" |

### FALSIFIED — do not re-litigate

| Finding | Leg | Settled evidence |
|---|---|---|
| "The 3.884×10⁻⁶⁹ coefficient is an uncomputed arithmetic step" (M2) | Grok | The full chain is displayed at `main.tex:256–266`: `M_Pl=1.22089e28 eV`, `n_ψ=100 cm⁻³`, `κn_ψ²=9.954e-80 eV⁴`, `ρ_Λ=(2.25 meV)⁴=2.563e-11 eV⁴`. Independently reproduced to 4 sf (`3.885e-69`), including the `(2.29/2.25)⁴` cross-check that explains the superseded `3.6e-69`. |
| "Dated September 2, 2026 — a future date" (M3) | Grok | `date` = 2026-09-02. Skill auto-FALSIFY **Rule 3** (training-cutoff artifact). Identical claim was FALSIFIED at R1 (Grok N1); this is a re-flag of an already-settled falsification. |
| "Duplicated phrasing ('the the', 'finite finite'); British 'programme' alternates with American 'program' in the same paragraph" (N2) | Grok | Perl doubled-word scan over `main.tex`: **zero** hits. `programme` occurs 7×, bare `program` **0×** — there is no alternation. Confabulated text. |
| "No frozen release hash; several commit hashes pre-date the stated submission version" (E3) | Grok | `\repoSHA = ded46bc5df8d39bbaac7bfbee16b07f0376bab34` is printed in the Data & Code section (`main.tex:950`) and all eight `\artifactbase` targets resolve at it; an immutable Zenodo deposit `doi:10.5281/zenodo.21481838` is cited at `main.tex:975`. A pinned commit *necessarily* predates the version it pins. The real remainder (unpinned `.bib` URLs) is **DP1N-31**. |
| "The perturbation-transparency theorem's proof is deferred to the companion" (E2, first half) | Grok | The statement and its `*Proof.*` are in-paper at `main.tex:312–357`; the key step (`½ε^{μνρσ}R_{μνρσ}(Γ̊)=0` from `R_{μ[νρσ]}=0`, order-independent) was re-checked and is correct. The real remainder — the **NJL** deferral — is **DP1N-28**. |
| "O5 is parity-odd off shell; the 'off shell' qualifier is an introduced error" (MINOR 1, premise) | Claude | C6: `O5` is parity-**even** off shell as well as on shell. The sentence *is* defective, but not for the stated reason; the correct repair is Gemini's and is carried as **DP1N-23**. |

### Re-flag of disclosed content — no action

| Finding | Leg | Disclosure site |
|---|---|---|
| "Five of the fourteen barriers are only naturalness/classification arguments, yet the abstract says they jointly close all four channels" (M1) | Grok | The paper concedes exactly this at the head of Sec. IV, and B9 is self-labelled heuristic. The real, non-disclosed remainder is the **absence of citation or derivation** for 12 of 14 — **DP1N-24**. |
| "Data Availability leans on a superseded, non-independently-submitted draft for load-bearing detail" (N2) | Gemini | Same substance as DP1N-24 (barrier sourcing) + DP1N-31 (mutable URLs) + DP1N-32 (supersession language in the bib). No separate item. |

### Opinion / genre — recorded, not defects

- Grok's **REJECT** dispatch word against a body whose findings are (after audit) one inherited
  coefficient error and a set of sourcing/self-containment items — skill **Rule 6**: judge by
  the written findings, not the verdict word. Two of Grok's three ESSENTIALs are FALSIFIED and
  the third is DP1N-41 at MINOR severity. Referee variance (pattern-066), recorded.
- Claude PART C's page-budget recommendation (13.5–14.5 pp) — scope guidance under DP1N-20,
  not a finding. It is consistent with the R1 audit's 12–16 pp.

---

## Counts

| Class | Count |
|---|---|
| Leg findings audited | **35** (Claude 20 fresh + Grok 8 + Gemini 8; plus Claude's 21 R1-verification rows cross-checked) |
| **GENUINELY-NEW-REAL** | **21** canonical (DP1N-22, 24–43) |
| **INHERITED-ERROR** | **2** canonical (DP1N-21, DP1N-23) |
| RE-FLAG-OF-DISCLOSED | 2 |
| FALSIFIED | 6 |
| OPINION/GENRE | 2 |
| OUT-OF-SCOPE | 0 |
| **Canonical real items opened** | **23** (8 MAJOR, 14 MINOR, 1 NIT) |
| Clean-wave count for P1N | **0** (unchanged; not converged) |

**R1 board re-verification (independent of the Claude leg's own tally):** spot-checked
DP1N-01 (`main.tex:764–778` vs P1C `2084–2098`), DP1N-07 (Eq. 10 present), DP1N-13 (chain
recomputed, `3.885e-69`), DP1N-14 (`√3/(32π²γ³)` → 0.409/0.267, squares 0.168/0.071),
DP1N-18 (27 cited = 27 defined), DP1N-19 (`0.342/0.094=3.64`, `0.215/0.074=2.91`). All
confirm the leg's verdicts. **No R1 item was closed dishonestly or by dismissal**; the two
"closed with defect" (DP1N-03 wording → now DP1N-23; DP1N-15 label → now DP1N-29) and the two
partials (DP1N-06 → DP1N-24/31; DP1N-08 → DP1N-32/40) are carried forward as new IDs rather
than being reopened.

**No fabricated result was found in v1N.0.2.** Every traced value reproduces its cited source
or frozen artifact; the single arithmetic failure (DP1N-21) is a substitution slip inherited
from a frozen source, and the paper's own disclosure practice (the `3.884` vs `3.6` note) is
exemplary.

---

## Closure plan

**Science / scope decisions (must be taken before any further review round — see budget note):**

1. **DP1N-21 — the 8π.** Correct Eq. (13), the ratio, and the surrounding size sentence in the
   Note; **and** correct P1C v1C.0.16 Eq. (o4_onshell) and its `-192π²G²` bare invariant; re-run
   and re-commit `arxiv/scripts/dim4_parityodd_enumeration.py` and
   `research/theory_audit/operator_basis_adjudication_2026_08_07.{py,json,md}`. Record the
   correction in P1C's own disposition ledger — it is a science decision for that paper's
   record, not a Note-local typo fix.
2. **DP1N-22 — the enumeration statement.** Restore P1C's tetrad-conversion clause and restate
   the rank/count honestly in Eq. (11)'s paragraph, the abstract, and the Conclusions.
3. **DP1N-23 — the parity statement.** Restate the list as ε-construction-rule-admitted and
   mixed-parity in both the Note and P1C.
4. **DP1N-25 — Popławski.** Decide: add the mapping subsection, or weaken "the four enumerated
   channels". Adding it is the recommended path; it is the paper's own strongest result.

**Content additions (~3.5–4.5 pp; takes the paper to ~14 pp, inside the R1 12–16 pp band):**

5. DP1N-24 — citation or 2–4-line derivation per barrier B1–B11, B13 (appendix), demoting any
   that survive neither.
6. DP1N-28 — the gap equation, regulator, and three-line no-solution argument (~0.25 pp).
7. DP1N-27 — display the Route-3 scaling relation and the source of the 61–67 spread (~0.25 pp).
8. DP1N-26 — B7 restatement + citations + repointed cross-reference.
9. DP1N-34, DP1N-38, DP1N-39 — Shapiro–Teixeira statement; Theorem environment; novelty sentence.

**Edits, no pages:** DP1N-29, 30, 31, 32, 33, 35, 36, 37, 40, 41, 42, 43.

**Then, in the same bundle (directive G):** bump `\paperVersion` + `\date`, 4-pass recompile
with 0 undef refs, `/latex-audit`, re-mirror the PDF byte-identical to every served path,
Convex `paperVersions:bump` with real md5/pages, three-way md5 check, SSOT + site sync.

## R2 budget note (directive R2)

This is the **second consecutive review round on P1N** (R1 board → R1 closure → R2 board) with
no intervening science or scope decision. Directive R2 caps that at two: **a third review
round requires an intervening science or scope decision first.** That condition is satisfiable
immediately and from this audit — **DP1N-21 (the 8π correction, which changes a printed
coefficient in two papers and inverts a stated size ordering) and DP1N-22 (the O1≡O6
restatement, which changes what the operator enumeration claims) are science decisions, not
review findings**, and DP1N-25 (whether the Note engages Popławski's Λ or narrows its channel
claim) is a scope decision. Take those three, close the ledger above, then R3 is permitted.

Running a third board *before* those decisions would be a directive-R2 violation and would
almost certainly return the same 8π and barrier-sourcing findings — the remaining verdict
movement on this paper is gated by content additions, not by more referee passes.
