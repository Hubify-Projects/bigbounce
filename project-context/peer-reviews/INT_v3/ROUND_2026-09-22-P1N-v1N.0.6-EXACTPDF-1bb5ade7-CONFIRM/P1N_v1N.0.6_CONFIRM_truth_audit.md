# P1N exact-version CONFIRM board — truth audit

**Board:** `ROUND_2026-09-22-P1N-v1N.0.6-EXACTPDF-1bb5ade7-CONFIRM`
**Exact PDF audited:** `arxiv/paper1bc_ech_note/main.pdf` sha256
`1bb5ade7a9b7948c587a9f884ef7af8cc44d1a4eae0221a30a0bec63b2b0f223`, 11 pp,
md5 `b9ac109139b7d88aa0f798ee7ef80c8d` (v1N.0.6, 2026-09-18).
**Why this board ran:** P1N's last INT board audited exact v1N.0.3
(`ROUND_2026-09-02-P1N-v1N.0.3-EXACTPDF-c758664b-R3VERIFY`); the paper moved
v1N.0.3 → v1N.0.6 (D-round + P-round packaging, no science change recorded)
without a fresh exact-version board. HOUSTON_SIGNOFF_PACKET_2026-09-22.md §5
named this gap. Sibling confirmation boards on P1B and P2 each found a real
regression despite "no science change" packaging claims, so directive R2's
version-drift exception applies: exactly one confirmation round, then stop.

**Directive-G pre-check:** served PDF at every path (`arxiv/paper1bc_ech_note/main.pdf`,
`site/public/papers/paper1bc_ech_note_v1N.0.6.pdf`, `public/papers/paper1bc_ech_note_v1N.0.6.pdf`)
md5-identical (`b9ac109139b7d88aa0f798ee7ef80c8d`). A fresh isolated 4-pass
recompile in a scratch directory produced a *different* md5
(`da3b6d02d9c2e0ed11f176cc863f7651`) but **byte-identical `pdftotext` output**
(`diff` = 0 lines) — the divergence is pdflatex's non-deterministic embedded
`/CreationDate`/`/ID` metadata, not stale content. Content-level directive-G
intent (served == current source) holds. Convex arm UNAVAILABLE (spending
limit) — neither passed nor failed, per campaign state.

## Legs

| Leg | Model | Verdict | Essential/Major/Minor | Raw |
|---|---|---|---|---|
| Grok API | grok-4.3 | REJECT | 3E / 3M / 3N | `project-context/peer-reviews/ROUND_2026-09-22-P1N-v1N.0.6-EXACTPDF-1bb5ade7-CONFIRM_P1N_Grok_brutal.md` (sha256 `1bb5ade7a9b7948c587a9f884ef7af8cc44d1a4eae0221a30a0bec63b2b0f223`-bound; leg raw sha256 `3c8f281c431b1952cbf32ea282b1638724cf3c35587ee4fffdad6ea96f5cea15`) |
| Gemini API | gemini-3.1-pro-preview | MAJOR REVISIONS (pass 1) + 1 self-critique ESSENTIAL (pass 2) | 2E+1E(p2) / 1M / 1N | `project-context/peer-reviews/ROUND_2026-09-22-P1N-v1N.0.6-EXACTPDF-1bb5ade7-CONFIRM_P1N_Gemini_cosmology.md` (sha256 `03cbe1a1fc627551bfccd6acb36cf5668643748760c3035b529034d5ecd6cdc6`) |
| Claude opus sub-agent (verdict-blind cold read) | claude-opus-5 | MAJOR REVISIONS | 2E / 6M / 15 minor / 6 nit | `project-context/peer-reviews/ROUND_2026-09-22-P1N-v1N.0.6-EXACTPDF-1bb5ade7-CONFIRM_P1N_Claude_opus_coldread.md` |

Perplexity/OpenAI: not part of the active-legs criterion (directive N,
M-AMENDED) — not dispatched.

## Per-finding truth audit

### Grok_brutal

| ID | Claim | Verdict | Source citation |
|---|---|---|---|
| E1 | Barrier catalog's negative result unsupported because majority of the 14 entries are heuristic/deferred | RE-FLAG-OF-DISCLOSED | `main.tex:87-88,1066-1071` abstract + Discussion explicitly tier the catalog ("two derived here, the rest argued or self-labelled heuristics"; "channel-level, not operator-level, closure"; "five entries ... are general naturalness or classification arguments ... not fourteen independently decisive theorems"). Same class as R3's Grok E4, previously dispositioned conceded-in-paper. |
| E2 | γ=0.2375, β/α≈2.11 asserted without in-paper derivation | RE-FLAG-OF-DISCLOSED | `main.tex:96-97,619,952` — cited to `Ashtekar2011` (published LQC area-gap literature value) at every occurrence; a literature-sourced constant with a real citation is not a standalone-reader defect. |
| E3 | Theorem 1's H1-H5 boundary-data hypotheses "stated to lie outside the present paper," proof not reproducible | **FALSIFIED** | `main.tex:341-352` states H1-H5 in full inline in the theorem statement; `main.tex:355-383` gives the complete 4-step proof plus the matched-data-hypothesis clarification, entirely in-paper. Same class as R3 Grok E3, previously falsified. |
| M1 | 7 barrier entries (B2,B5,B6,B7,B9,B10,B11,B13 per Grok's list) flagged non-rigorous, "jointly close" language unsupported | RE-FLAG-OF-DISCLOSED | Matches `DP1N-47`'s v1N.0.4 closure exactly: B2/B5/B6/B10 already downgraded to "argued in-paper (not literature-established)," unsupported citations removed (`main.tex:530,557,565,609` + abstract). |
| M2 | Route 2/3 amplitude closures rely on unreproduced companion-manuscript loop integrals | RE-FLAG-OF-DISCLOSED | `main.tex:1130-1136` discloses the companion manuscript (Zenodo DOI `10.5281/zenodo.21481838`) and the companion no-go survey (pinned commit) by name — the standalone-reader objection, structurally bounded by the disclosed companion architecture (R3 convergence-statement precedent). |
| M3 | Operator rank-4 claim's "only supporting evidence is a symbolic script whose output is not reproduced" | **FALSIFIED** | `main.tex:874-902` gives the full analytic derivation in-text: both null-space relations displayed, the tetrad-conversion identity for O1≡O6 shown step-by-step, rank-four/five-distinct-densities argued directly from the shown algebra. The cited symbolic script (`OperatorBasisAdj2026`) is independent supplementary verification, not the sole evidence. |
| N1 | Repeated "programme's benchmark γ=0.2375" phrase lacks a local definition | OPINION/GENRE | Each occurrence (`96,225,239,952`) carries or sits within one paragraph of the `Ashtekar2011` citation; a style preference, not a missing citation. |
| N2 | "No ECH dark-energy or birefringence prediction is made" is redundant | OPINION/GENRE | Same target sentence R3 already falsified once (as an "overstatement" framing); here reframed as "redundant" — still a style opinion on a claim-policy sentence, not a defect. |
| N3 | Some arXiv ids lack journal publication data despite having "subsequently appeared" | **FALSIFIED** | `references.bib` audited programmatically: every entry with an `eprint`/arXiv field but no `journal` field is a self-citation companion preprint (`Golden2026P1cArxiv` and similar) that is genuinely unpublished — there is no external citation missing its journal data. |

Grok's dispatch word REJECT does not survive: 2 of 3 ESSENTIALs FALSIFIED, the
third RE-FLAG; all MAJORs RE-FLAG-OF-DISCLOSED. Skill Rule 6 (judge by the
written findings, not the dispatch word); pattern-066 referee variance.

### Gemini_cosmology

| ID | Claim | Verdict | Source citation |
|---|---|---|---|
| P1N-E1 | Abstract's "exact total derivative **on the torsion-free branch**" misattaches the qualifier — body assigns "on the torsion-free branch only" to the *vanishing* category (O1,O6), not to the *total-derivative* category (O2,O3, which are total derivatives unconditionally, "on any connection") | **GENUINELY-NEW-REAL, MAJOR** | `main.tex:904-907` ("an exact total derivative (O2 ... O3...), identically vanishing on the torsion-free branch only (O1, O6...)") vs. the pre-fix abstract at `main.tex:92-94`. Confirmed by direct text comparison — not previously flagged in `DP1N-*`. **CLOSED v1N.0.7** (see below). |
| P1N-E2 | Barrier-catalog derivations outsourced to an unpublished GitHub `.tex` draft, violating standalone-reader test | RE-FLAG-OF-DISCLOSED | `main.tex:1133-1136` — same companion-architecture disclosure as Grok M2; R3 convergence-statement precedent ("disclosed openly every round ... a venue judgment, not a defect"). |
| P1N-M1 | Code artifacts (GitHub commit pin) lack a Zenodo DOI, unlike the companion manuscripts | Re-surfaces already-tracked open item | Matches `DP1N-58` exactly (open since R3, SSOT: "genuine open packaging item, not fabricated as closed" — minting requires an external Zenodo deposit action outside agent authorization). Not counted as a new item. |
| P1N-N1 | "well before the classical curvature singularity is reached" lacks a specific density scale | OPINION/GENRE | `main.tex:124-126` — Introduction background sentence describing the established (Poplawski-line) bounce mechanism, not this paper's own novel quantitative claim (the paper's actual quantitative content is the dark-energy no-go, stated with explicit numbers throughout). |
| P2N-E1 (pass 2) | "Catastrophic ~57-order unit-conversion error": claims `n_ψ=100 cm⁻³` must be **divided** by `(ħc)³` to reach eV³, giving `κn_ψ²/ρ_Λ≈1.1e-12` instead of the paper's `3.884e-69` | **FALSIFIED** | Independently re-derived from first principles: a number density (inverse length³) converts to natural units by **multiplying** by `(ħc)³` — standard convention (`1 fm⁻¹ = 197.3 MeV`, i.e. multiplying an inverse-length by ħc gives energy; nuclear saturation density `n₀≈0.16 fm⁻³` → `≈1.2×10⁻³ GeV³` this same way, the standard quoted QCD value). `100 cm⁻³ × (1.973e-5 eV·cm)³ = 7.68e-13 eV³`; squared `×κ=8π/M_Pl²` gives `9.94×10⁻⁸⁰ eV⁴` — matching `main.tex:254,726-727,826-827`'s printed `9.954×10⁻⁸⁰ eV⁴` to 3 significant figures. Gemini's proposed "fix" inverts the conversion direction; the paper's number is correct. This exact chain (`3.884e-69`) was independently re-derived and confirmed once before, at R3 (Grok M2, FALSIFIED then too). |

### Claude opus sub-agent (verdict-blind cold read)

The opus leg independently re-derived roughly 20 of the paper's displayed
equations/numbers by hand before trusting any of them (Eq. 3's coefficient
from the Einstein+Holst sectors, the Fierz row against the standard Fierz
matrix, the O4/O5 ε-algebra, the Benedetti–Speziale β-function integration,
every unit conversion) and found all of them correct — including the exact
`9.954×10⁻⁸⁰ eV⁴` / `3.884×10⁻⁶⁹` benchmark independently re-verified for a
third time in this campaign's history (R3 Grok M2; this board's Gemini
pass-2). Two ESSENTIAL findings survive independent re-verification below.

| ID | Claim | Verdict | Source citation / independent check |
|---|---|---|---|
| E1 | The `main.tex:216-219` EOS assignment $\rho_{4\psi}=-\mathcal L_{4\psi}$, $p_{4\psi}=+\mathcal L_{4\psi}$ (i.e. $w=-1$, "for a term with no explicit time derivatives") is inconsistent with §II.A's own $\kappa n_\psi^2\propto n_\psi^2\propto a^{-6}$ parametrization, which under covariant conservation forces $w=+1$ (stiff), not $w=-1$; under the correct $w=+1$ the repulsion condition $\rho+3p<0$ inverts relative to what the paper derives. Consistent with the standard ECSK spin-fluid literature result ($\varepsilon_{\rm spin}=p_{\rm spin}<0$, $w=+1$, not $w=-1$) for the identical interaction. | **GENUINELY-NEW-REAL, ESSENTIAL — OPEN, not closeable by this lane** | Confirmed by re-reading `main.tex:216-236`: the paper's own text derives the EOS from "a term with no explicit time derivatives" (a vacuum-energy-like/potential-term heuristic), then two subsections later (`main.tex:250-251`) parametrizes the same term's magnitude by a density `$n_\psi$` explicitly invoked elsewhere as "the cosmic fermion number density" (`main.tex:822-823`), which the paper itself never states as constant-in-time. No prior `DP1N-*` disposition examined this question — DP1N-44/49 fixed an arithmetic/sign error *within* the assumed EOS, never the EOS assumption itself. This is a genuine, unresolved tension between two internally-inconsistent treatments of the same interaction term, not a false claim — it survives independent re-derivation and is NOT falsifiable against the source. |
| E2 | §VII.D's "direct, quantitative rebuttal" of Popławski's dark-energy proposal (cited to `Poplawski2012`) evaluates the wrong physical quantity: the cited paper (`references.bib`: "Cosmological constant from quarks and torsion," Annalen der Physik 523, 291) sets $\rho_\Lambda$ via the QCD quark chiral condensate $\langle\bar qq\rangle\sim-(235\,{\rm MeV})^3$, not a baryon/fermion number density as `main.tex:817-819` describes it; §VII.D then re-uses the §II.A ISM benchmark ($n_\psi\sim100\,{\rm cm^{-3}}$) instead, off from the cited paper's actual scale by roughly 74 orders of magnitude and in the wrong direction (the condensate-scale evaluation *over*-produces $\rho_\Lambda$ by $\sim2\times10^5$, not under-produces it) | **GENUINELY-NEW-REAL, ESSENTIAL — OPEN, not closeable by this lane** | Independently re-verified the arithmetic from scratch: $\kappa=8\pi/M_{\rm Pl}^2=1.686\times10^{-37}\,{\rm GeV^{-2}}$; $\langle\bar qq\rangle^2=(0.235\,{\rm GeV})^6=1.684\times10^{-4}\,{\rm GeV^6}$; $\tfrac{3}{16}\kappa\langle\bar qq\rangle^2=5.32\times10^{-42}\,{\rm GeV^4}$; $\rho_{\Lambda,\rm obs}=(2.25\,{\rm meV})^4=2.563\times10^{-47}\,{\rm GeV^4}$; ratio $=2.08\times10^5$ — independently reproduces the opus leg's number to 3 s.f. `references.bib:4-15` confirms `Poplawski2012` is indeed the quark-condensate paper (arXiv:1005.0893) — the mismatch between the paper's description ("average cosmic fermion (baryon) spin density") and the cited work's actual mechanism (quark chiral condensate) is a real misdescription of the source, not a truth-audit artifact. |

Six MAJOR + 15 minor + 6 nit findings from this leg (Theorem 1's novelty
relative to the 1996 Holst equivalence; a constructed counterexample to the
six-operator spanning claim; unargued/mistagged barrier-catalog entries; the
R4 "systematically, no" claim vs. §V.C's own naturalness-only concession;
companion-manuscript self-containment; the `Poplawski2011`/`Poplawski2012`
bib-key year swap; the PRD-class-for-a-CQG-submission formatting mismatch)
are recorded in the full raw and are real but lower-priority — logged as
open items for the science-closure lane below, not blocking this board's
headline verdict on their own.

## Genuinely-new-real tally

**Two (2) ESSENTIAL genuinely-new-real items that this board cannot close**
(opus E1, E2 — both target the paper's core physics claims, not wording) plus
**one (1) MAJOR genuinely-new-real item already closed** (Gemini P1N-E1,
abstract-body wording drift, DP1N-59, v1N.0.7) plus **6 MAJOR / 21 lower-tier
genuinely-new-real presentational items** from the opus leg, logged open but
not gating. `DP1N-58` (Zenodo DOI) re-surfaced but is already an open, tracked,
disclosed item (not new). All Grok findings and Gemini's pass-2 "catastrophic
error" claim are FALSIFIED, RE-FLAG-OF-DISCLOSED, or OPINION/GENRE (see above).

**This board cannot declare P1N CONFIRMED.** E1 and E2 are genuine,
independently-re-verified physics-reasoning gaps in the paper's two headline
claims (the "repulsive/bounce" sign argument, and the "direct quantitative
rebuttal" of Popławski's actual proposal) — not falsifiable against the
source, not previously dispositioned, and not closeable by a text edit
without either a real re-derivation of the contact term's stress tensor or a
substantive rewrite of §VII.D that may invert the paper's own Route-1
conclusion. Inventing either under this lane's scope and time budget would
violate `/never-fabricate-derivation`. Per directive R2 this board's one
permitted confirmation round is spent; per this lane's own instructions, a
finding this deep is reported, not silently authored around.

## Closure applied this board (v1N.0.6 → v1N.0.7)

- `main.tex:92-95` (abstract): reordered the branch/on-shell qualifiers to
  match the body's Sec. VI classification exactly — "is either an exact total
  derivative, a Fierz-closed M_Pl⁻²-suppressed contact term on-shell, or
  identically vanishing on the torsion-free branch only." No other text,
  equation, or numeric content changed.
- Directive-G hygiene: `\paperVersion` v1N.0.6→v1N.0.7, `\paperTimestamp`/`\date`
  September 18 → September 22, 2026. 4-pass recompile (pdflatex×2 + bibtex +
  pdflatex×2 via `bibtex` in the middle), 0 undefined refs/citations. One
  pre-existing 4.49666pt overfull hbox (line 868, unchanged from the D-round's
  recorded 4.5pt residual, well under the 10pt gate) — no new overflow. Page 1
  rendered at 150dpi and visually confirmed: corrected abstract text, no
  overflow, date reads "September 22, 2026." 11 pages (unchanged). PDF sha256
  `6f7851d6db2df0dc5f20b74fe7395280df6f75196f88ffb5ec9958c96d4e022e`, md5
  `8f073078c95ff587825e0a78397b13a3`. Mirrored byte-identical to
  `site/public/papers/paper1bc_ech_note_v1N.0.7.pdf` and
  `public/papers/paper1bc_ech_note_v1N.0.7.pdf` (md5-verified against source).

## Verdict

**P1N is NOT CONFIRMED on v1N.0.7. Readiness-99 must drop to a SIGN-OFF
HOLD pending real science closure of DP1N-60 and DP1N-61.** This board's own
three legs independently re-verified essentially every quantitative claim in
the paper as internally consistent and arithmetically correct (Grok's and
Gemini's adversarial attempts to find calculation errors — the H1-H5 scope
objection, the operator-rank-only-from-script objection, the "57-order unit
error" — all FALSIFIED under independent re-derivation), which is exactly why
the two findings that *did* survive independent re-verification carry weight:
they are not arithmetic slips but genuine gaps in what the paper's own
equations are used to assert (opus E1: an equation-of-state assumption that
contradicts the paper's own density parametrization and the standard ECSK
literature result for the same interaction; opus E2: a "direct quantitative
rebuttal" evaluated at the wrong physical scale against a misdescribed
source, off by ~74 orders of magnitude and in the wrong direction). Both
target the paper's title claims directly — what minimal ECH torsion "does for
the bounce" (E1) and "cannot do for dark energy" specifically against
Popławski's own proposal (E2) — and neither is closeable with a text edit: E1
needs a rigorous re-derivation of the contact term's stress tensor with the
fermion-fluid averaging made explicit; E2 needs either a correct evaluation
at Popławski's actual (condensate) scale — which the reviewer's own
arithmetic suggests would *invert* the Route-1 conclusion from
under-production to over-production, a different and non-trivial result — or
a withdrawal of the "direct, quantitative rebuttal" claim. Manufacturing
either resolution under this bounded lane would violate
`/never-fabricate-derivation`; this board's directive-R2 confirmation-round
budget is spent, so a fourth board is not the next step either. The next
step is a dedicated science-closure lane (same pattern as P4P's in-domain
remeasurement) that either produces the real derivations or narrows the
paper's title/abstract claims to what is actually established.

The v1N.0.7 wording fix (DP1N-59) stands — it is real, harmless, and
independent of DP1N-60/61. Directive-G hygiene on v1N.0.7 is clean. What
changes is the readiness-99 claim itself: the paper's D-round/P-round
packaging was never in question, but its science content now has two open
ESSENTIAL items that predate this lane and were never examined by any prior
`DP1N-*` round.

**Sentence for Houston's sign-off:** *"P1N's exact-version confirmation board
(Grok API + Gemini API + a verdict-blind Claude opus cold-read referee, exact
v1N.0.6→v1N.0.7 PDF) re-verified essentially every quantitative claim in the
paper as arithmetically correct, including successfully falsifying an
adversarial claim that the benchmark density calculation was off by 57
orders of magnitude — but the cold-read referee independently surfaced two
ESSENTIAL findings that were never examined by any prior review round: the
paper's sign argument for the repulsive/bounce mechanism rests on an
equation-of-state assumption that contradicts its own density parametrization
and the standard torsion-cosmology literature result for the same
interaction, and its claimed 'direct quantitative rebuttal' of Popławski's
actual dark-energy proposal evaluates the wrong physical quantity by roughly
74 orders of magnitude against a misdescribed source. Both target the title's
own claims directly, neither is a wording fix, and resolving the second
honestly may reverse the paper's Route-1 conclusion. Readiness-99 is placed
on SIGN-OFF HOLD pending real science closure — not a re-run of another
review board — of these two items."*
