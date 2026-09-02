# P1N v1N.0.3 — R3 verification-round truth audit

**Auditor:** Opus truth-auditor, independent; skeptical both ways. Decided from source, never from verdict words.
**Manuscript:** `arxiv/paper1bc_ech_note/main.pdf`, 11 pp
**Exact sha256 (re-verified with `shasum -a 256`):** `c758664b4485a45752cd79e2ab695c6b09d9f82f2b283dd8db5a2af6721f7027` — matches the round label.
**Source bound:** `arxiv/paper1bc_ech_note/main.tex` (1166 lines), `references.bib`
**Cross-sources:** `arxiv/paper1c_nogo_survey/main.tex` (v1C.0.16), `arxiv/paper1a_ech_nogo.tex`, `research/theory_audit/*.md`, `research/theory_audit/p1n_r2_checks_2026_09_02.py`
**Date:** 2026-09-02

## Legs

| Leg | Model | Verdict word (diagnostic only) | Tagged items in raw | Dispositioned | Gap |
|---|---|---|---|---|---|
| Claude INT | claude-opus | major-revisions | 5 MAJOR / 9 MINOR = 14 | 14 | no |
| Grok API | grok-4.3 | REJECT | 6 ESSENTIAL / 3 MAJOR / 2 MINOR = 11 | 11 | no |
| Gemini API | gemini-3.1-pro-preview | MAJOR REVISIONS | 3 ESSENTIAL / 2 MAJOR / 2 NIT = 7 | 7 | no |
| Perplexity | — | **ABSENT** (401 insufficient_quota; `Reviewer call FAILED`) | — | — | recorded ABSENT, not clean |

**BLOCKER count: 0 across all legs** (explicit observation, mechanical grep of the raws).
Round is **not degraded**: three real legs with real wall times and packet hashes; the absent leg is recorded as absent per skill Rule 4.
Severity read from per-item tags, never from the verdict word (skill Rule 8). Grok's REJECT dispatch against a body whose surviving items are two sourcing/scope objections is skill Rule 6 / pattern-066 referee variance.

## Independent recomputation performed this round

All executed in this audit, not quoted from a leg:

| Quantity | Recomputed | Paper / claim | Result |
|---|---|---|---|
| `O4/O5 = 8πγ/(1+γ²)` at γ=0.2375 | **5.65031** | `main.tex:952` prints `≃5.65` | exact |
| `−24 M_Pl²αβ` from `α=κγ²/[2(1+γ²)]`, `β=κγ/[4(1+γ²)]`, `M_Pl²κ²=8πκ` | `−24πκγ³/(1+γ²)²` | `main.tex:943–947` | exact; dimension-4, one power of G |
| `1/(2γ)` | 2.10526 | abstract `main.tex:108–109` "evaluates to 2.11" | correct |
| `γ²/(1+γ²)` | 0.053394 | `main.tex:262` "0.053" | correct |
| Sign chain, κ=1, `(J⁵·J⁵)=+1` | `L₄ψ = −0.010011`; `ρ+3p = −L+3L = +2L = −0.020023` | paper prints `−2L` and `L>0` | **both printed steps wrong; product correct** |
| Eq. (11) central: `1.4e−6 × 3.9e−69` | `5.46e−75` → **74.26 orders** | window printed `61–67` | window excludes its own central value |
| Eq. (11) at `\|Δγ/γ\|→O(1)` | `3.9e−69` → **68.41 orders** | — | Eq. (11)'s honest window ≈68–74 |
| P1C `(Δγ/γ)(H₀/M_Pl)`, `H₀/M_Pl=1.18e−61`: `Δγ/γ=0.3` | `3.54e−62` → **61.45** | P1C `main.tex:1578–1583` "∼61 orders" | exact match |
| same, `Δγ/γ=1.4e−6` | `1.652e−67` → **66.78** | P1C same lines "∼67 orders" | exact match |
| Reduced Planck mass `1.22e19/√(8π)` | **2.4335e18 GeV** | `main.tex:721` calls `1.22e19 GeV` "reduced-Planck-mass convention" | label wrong |
| Abstract word count (LaTeX+math stripped) | **444 words** (Claude leg measured 433 with a stricter stripper; both ≫300) | SSOT records "435 → ~380" | not closed either way |
| `references.bib` `tree/main`/`blob/main` | 0 hits; 4 `ded46bc5…` pins | DP1N-31 | closed |
| doubled-word / "brauch" scan of `main.tex` | 0 hits; `main.tex:906` reads "branch" | Gemini N1 | extraction artifact |
| `main.log` | 0 undefined refs/citations; 1 overfull hbox @ 4.50 pt | — | under the 10 pt gate |

## PART 1 — Verification of the R2 closure record (DP1N-21 … DP1N-43)

The R3 Claude leg's PART A verification table was independently spot-checked at every point where it asserted a defect, and at the four headline science decisions.

- **DP1N-21 (8π) — CLOSED, and correct.** Re-derived here from the paper's own α, β, κ: `−24M_Pl²αβ = −3M_Pl²κ²γ³/(1+γ²)² = −24πκγ³/(1+γ²)²`, exactly as printed at `main.tex:943–947`. Grep confirms 0 surviving `0.22`, `-3\kappa\gamma^3`, `192\pi^2 G^2`. Ordering propagated (`main.tex:952–954`). **Closed to a high standard.**
- **DP1N-22 (five distinct densities / rank 4) — CLOSED.** `main.tex:885–903` restores P1C `2041–2043` in full; propagated to abstract `98–101` and Conclusions `1092–1095`; O6 retained as instructed.
- **DP1N-23 (O5 parity) — CLOSED in the operative statement** (`main.tex:930–936`: P-even off *and* on shell, ε-construction-rule-admitted, mixed-parity set), **with a residual** — see DP1N-51.
- **DP1N-25 (Popławski Λ) — CLOSED at correct evidential strength.** New `sec:poplawski_de` (`main.tex:817–844`) states the mechanism, maps it to Route 1, closes it on amplitude and sign, and notes the actual cosmic `n_b` widens the gap. The Route-1 arithmetic reproduces (`3.884e−69`).
- **Closed:** DP1N-26, 31, 34, 36, 38, 39, 41, 43 — each spot-verified at the cited lines.
- **NOT closed, recorded closed in SSOT:** DP1N-29 (`main.tex:486` still "the Barbero–Immirzi symbol κ") and DP1N-37 (abstract 444 words). **The SSOT closure record for this paper needs re-verification rather than trust.**
- **Closed with residual defect:** DP1N-24, 27, 28, 30, 32, 33, 35, 40, 42 — carried below as new IDs, not reopened.

## PART 2 — Per-finding audit table (all 32 leg findings)

Verdicts ∈ {GENUINELY-NEW-REAL, REGRESSION-FROM-CLOSURE, RE-FLAG-OF-DISCLOSED, FALSIFIED, OPINION/GENRE, OUT-OF-SCOPE}.

| # | Leg · tag | Claim | Location | Verification | Verdict | Sev | Closure instruction |
|---|---|---|---|---|---|---|---|
| 1 | Claude MAJOR 1 | ρ+3p repulsion chain: two sign errors that cancel | `main.tex:225–236`, PDF p. 2 | From the paper's own `ρ=−L`, `p=+L`: `ρ+3p = −L+3L = +2L`, **not** the printed `−2L`; and a negative coefficient × positive `(J⁵·J⁵)` gives `L<0`, **not** the printed `L>0`. Recomputed κ=1: `L=−0.010011`, `ρ+3p=−0.020023<0`. Conclusion (repulsive) correct; **every displayed step wrong.** Chain was *added by the DP1N-35 closure*. | **REGRESSION-FROM-CLOSURE** | MAJOR | Rewrite the three lines: `ρ+3p=2L`, requirement `L<0`, Eq. (3)'s negative coefficient supplies it. |
| 2 | Claude MAJOR 1 (2nd half) | "signature-independent" asserted while conditioning on a "spacelike-normalized" `J⁵` | same lines | The parenthetical premise fixes the sign of `(J⁵·J⁵)` and is load-bearing; a spin-aligned axial current is naturally timelike. Signature-independence cannot rest on a signature-dependent normalization. Refines DP1N-04/DP1N-35. | GENUINELY-NEW-REAL | MAJOR | Justify the premise for the configurations of interest, or drop the signature-independence claim and end at the disclaimer. |
| 3 | Claude MAJOR 2 · Grok (implicit) | Eq. (11) does not produce the retained 61–67 window; the stated origin of the window is not its actual origin | Eq. (11) `729–733`; window `743–754`; repeat `1032–1034` | Central `1.4e−6 × 3.9e−69 = 5.46e−75` = **74.26 orders**, printed by the paper itself as `~5e−75` two lines above the 61–67 quote. `μ_UV→M_Pl` gives at best 68.41 orders. The 61/67 endpoints reproduce **exactly** from P1C's *different* relation `(Δγ/γ)(H₀/M_Pl)`, `H₀/M_Pl=1.18e−61` (`paper1c/main.tex:1563–1583`): 61.45 and 66.78. The Note no longer carries that relation. Introduced by the DP1N-27 closure. | **REGRESSION-FROM-CLOSURE** | MAJOR | **Decision required** (see PART 4): restore P1C's `H₀/M_Pl` relation as the one defining the quoted orders, or keep Eq. (11) and re-quote its own ≈68–74 window. Not both. |
| 4 | Claude MAJOR 2 (compounding) · Claude MINOR 5 | Table II R3 row credits a "mass-dimension lock" appearing nowhere else | `main.tex:798–800` | Grep: exactly 1 occurrence. The lock is P1C's `H₀/M_Pl` dimension argument (`paper1c/main.tex:1555–1560`), absent from the Note. Same defect class as the "chiral-count bound" the DP1N-30 closure deleted, recurring in the same table. | **REGRESSION-FROM-CLOSURE** | MINOR | Import the argument or rename the row's basis; resolves with item 3. |
| 5 | Claude MAJOR 3 · **Gemini E1** | In-body erratum notice: "the printed coefficient in an earlier internal draft omitted this 8π substitution and is corrected here (SSOT)" | `main.tex:948–950`, PDF p. 8 | Verified verbatim in source and on the p. 8 render. Directive-Q1 violation printed in the manuscript. | GENUINELY-NEW-REAL | MAJOR | State Eq. (15) as the result. Delete the comparison and `(SSOT)`. |
| 6 | Claude MAJOR 3 (2nd) | "not a ~4.5×-smaller correction to O5" quotes a number existing only in the superseded draft | `main.tex:953–954` | Grep: `4.5` appears only here; no other referent in the manuscript. | GENUINELY-NEW-REAL | MINOR | Delete the clause; keep "O4 is larger by ~5.7". |
| 7 | Claude MAJOR 3 (3rd) · **Gemini E2** | "This manuscript is internally tracked as v1N.0.3" printed in Data & Code Availability | `main.tex:1104`, PDF p. 11 | Verified. **Created by the DP1N-40 closure** ("use the dead `\paperVersion` macro") while DP1N-32 was removing exactly this register. | **REGRESSION-FROM-CLOSURE** | MAJOR | Delete the sentence; delete the macro instead of using it. |
| 8 | Claude MINOR 9 | Internal project label "(P1A~\cite{Golden2026P1a})" in the body | `main.tex:627` | Verified. Residual of DP1N-32. | GENUINELY-NEW-REAL | MINOR | Drop the tag, keep the citation. |
| 9 | Claude MAJOR 4 | Added barrier citations are topical pointers, not support; abstract now asserts "literature-sourced" | abstract `92`; B2 `524–529`, B5 `551–557`, B6 `559–567`, B10 `603–610` | Checked individually. B2 attaches `BlagojevicHehl2013` (a gauge-theories-of-gravitation reader) + `BoehmerBurnett2008` to a **biconditional** ("mass protection ⟺ no geometric fingerprint") stated in neither. B5/B6/B10 each attach `Weinberg1989`, the canonical Λ-problem review, which contains nothing on the bounce density, on transfer across `N_tot≈92–94` e-folds, or on a UV→IR bridge in minimal ECH. B1, B3, B4, B11, B12, B13 *are* fairly supported (B3 now carries a real in-paper argument) — targeted, not blanket. Residual of DP1N-24. | GENUINELY-NEW-REAL | MAJOR | **Scope decision:** supply the 2–4-line derivations R2 asked for for B2/B5/B6/B10, **or** downgrade the abstract's "literature-sourced" wording to what the citations establish. |
| 10 | Claude MAJOR 5 | "reduced-Planck-mass convention" mislabels `1.22e19 GeV` | `main.tex:720–722`, PDF p. 6 | `1.22e19 GeV` is the **non-reduced** Planck mass; reduced = `1.22e19/√(8π) = 2.4335e18 GeV` (recomputed). `G=1/M_Pl²` and `κ=8πG=8π/M_Pl²` (`main.tex:182`) are both non-reduced. Paper's numerics are internally correct (`M_Pl=1.22089e28 eV` reproduces `3.884e−69`); **only the label is wrong** — in the one sentence the DP1N-42 closure added to prevent an 8π ambiguity. | **REGRESSION-FROM-CLOSURE** | MAJOR | Delete "reduced-". One word. |
| 11 | Claude MINOR 1 · **Gemini N2** | Table I caption calls κ "the Barbero–Immirzi symbol" | `main.tex:486`, PDF p. 4 | Verified: text unchanged. γ is Barbero–Immirzi; `κ=8πG` per Eq. (1). **DP1N-29 recorded closed in SSOT and is not closed.** | GENUINELY-NEW-REAL (SSOT record defect) | MINOR | "…the gravitational coupling κ". |
| 12 | Claude MINOR 2 | Abstract length | abstract | Measured **444 words** here (Claude leg: 433). SSOT records "435 → ~380". Unchanged in substance; ~1.5× the CQG ≈300 guidance. **DP1N-37 recorded closed and is not closed.** | GENUINELY-NEW-REAL | MINOR **(GENRE)** | Cut to ~250–300; lead with the structural dichotomy. |
| 13 | Claude MINOR 3 | Residual "parity-odd" language contradicts the new mixed-parity statement | `850`, `852`, `909`, and decisively `978–979` | `main.tex:936` establishes "a mixed-parity ε-contracted set, not a strictly parity-odd one"; `main.tex:979` then concludes "every admissible local dimension-4 **parity-odd** density in minimal ECH is topological…" — the section's summary sentence reverts to the classification the section just corrected. Residual of DP1N-23. | GENUINELY-NEW-REAL | MINOR | Use "ε-contracted" / "construction-rule-admitted" uniformly at `850`, `852`, `909`, `979`. |
| 14 | Claude MINOR 4 | The DP1N-33 fix is contradicted in the Discussion | fix `692–695`; contradiction `1032–1033` | `692–695` correctly restricts "58 orders" to the doubly-normalized ratio of Eq. (7); `1033` then says "≥58 orders of margin **against the observed birefringence amplitude**" — the exact misdescription DP1N-33 was opened to remove. | **REGRESSION-FROM-CLOSURE** (incomplete propagation) | MINOR | Fix the Discussion sentence to match `692–695`. |
| 15 | Claude MINOR 6 | Gap-equation loop-integral prefactor `N_cN_f/(4π²)` is asserted | `main.tex:313–317` | The three-line argument is verified logically sound and only `I>0` is load-bearing; the prefactor is printed without derivation or citation. Residual of DP1N-28. | GENUINELY-NEW-REAL | MINOR | Derive/cite it, or write `I ∝ ∫₀^Λ p²dp/√(p²+M²) > 0` and state that only positivity is used. |
| 16 | Claude MINOR 7 | "vanishes only in the γ→∞ limit" is false as written | `main.tex:954–956` | `O4 ∝ γ³/(1+γ²)²` → 0 as γ→0 as well as γ→∞. "only" is wrong. | GENUINELY-NEW-REAL | MINOR | "vanishes in the γ→∞ Einstein–Cartan limit (and, degenerately, as γ→0)". |
| 17 | Claude MINOR 8 | Self-contradiction inside one sentence about O4's irrep support | `main.tex:938–941` | Text: "supported only by the **non-axial** torsion irreps — it vanishes on a pure axial or a pure trace-vector torsion alike and is carried entirely by the **axial×trace-vector** cross term". The cross term requires the axial irrep. Intended statement (needs both, vanishes on either alone) is correct and is what the γ→∞ behavior confirms; only the first clause is wrong. | GENUINELY-NEW-REAL | MINOR | Delete/repair the "non-axial" clause. |
| 18 | **Gemini E3** + **Gemini M2** · Grok E1 | Standalone-reader failure: the 14 barrier derivations and the core algebraic proofs (Refs [14],[15],[27],[30]) are outsourced to non-peer-reviewed repository `.md`/`.tex` files | `main.tex:1104ff`, `references.bib` | Verified: `Golden2026P1a` carries Zenodo `10.5281/zenodo.21481838`; the P1C survey and the three theory-audit `.md` artifacts are commit-SHA-pinned only, with no DOI. The paper discloses their non-refereed status openly. This is the standing DP1N-06 residual, narrowed by the DP1N-31 SHA pin. | RE-FLAG-OF-DISCLOSED **with a real archival residual** | MINOR (venue/archival) | Mint Zenodo version DOIs for P1C v1C.0.16 and the three theory-audit artifacts; cite the DOIs. Not a science change. |
| 19 | **Gemini M1** | GitHub commit pin is not a permanent academic archive | refs, PDF p. 11 | Same substance as #18. | RE-FLAG-OF-DISCLOSED (dup of #18) | — | Folded into #18. |
| 20 | **Gemini N1** | Typo "brauch" for "branch" | Sec. VI p. 8 | `grep -n "brauch"` on `main.tex`: **0 hits**; `main.tex:906` reads "ECH branch". PDF text-extraction mangling. | **FALSIFIED** (skill Rule 7 extraction artifact) | — | None. |
| 21 | **Grok E1** | All steps producing `−3κ/16` must be reproduced in main text, or reduce to a Letter | Sec. II p. 2 | Same standalone-reader substance as #18; the Fierz derivation is disclosed as carried by the frozen artifact (`fierz_adjudication_2026_08_05.md`, whose 5×5 Fierz matrix was independently solved and re-verified at R1). The "or reduce to a Letter" half is a length/venue opinion. | RE-FLAG-OF-DISCLOSED (→ #18) + OPINION/GENRE | — | None beyond #18. |
| 22 | **Grok E2** | Abstract quotes `β/α = 2.11` with no finite-γ caveat — abstract–body drift | abstract | `main.tex:108–109` reads "…which evaluates to **2.11 at the programme's benchmark γ=0.2375** (Ref. [Ashtekar2011])". The benchmark is named in the abstract itself, with its citation. Premise false. | **FALSIFIED** | — | None. |
| 23 | **Grok E3** | Theorem 1 is conditional on H1–H5, which exclude the very extensions the paper claims to close ⇒ circular | Sec. III | The paper's claim policy is channel-level closure of **minimal-coupling** ECH routes; H1–H5 and the explicit excluded-cases list (`main.tex:351–367`, added under DP1N-38) state the scope openly, and the abstract/Intro disclaim operator-level completeness and any unrestricted no-go. A theorem scoped to minimal ECH is not circular for not covering non-minimal ECH. | RE-FLAG-OF-DISCLOSED | — | None. |
| 24 | **Grok E4** | Table I over-claims: 13 of 14 barriers are naturalness or single-branch statements | Sec. IV, Table I | The paper concedes exactly this at the head of Sec. IV and in the abstract's tiering. The non-disclosed remainder — citations that do not support their propositions — is the real item, captured at #9. | RE-FLAG-OF-DISCLOSED (real remainder = #9) | — | None beyond #9. |
| 25 | **Grok E5** | The two operator relations are on-shell statements sold as an off-shell basis result | Sec. VI pp. 7–8 | `main.tex:~884`: "both relations hold identically **off shell and on shell**", and the first is derived from the metric-compatible tetrad conversion, which is off-shell. The section is titled "The Operator List: **Rank, Not Basis**" and states the list is "*not* a linearly independent basis". Premise contradicted by the text. | **FALSIFIED** | — | None. |
| 26 | **Grok E6** | Abstract's "no ECH dark-energy or birefringence prediction is made" is stronger than the body, since R2/R3 give tiny nonzero contributions | abstract, Sec. V | "No prediction is made" is a claim-policy statement (the paper declines to *predict*), not a claim that the contributions vanish; the body quantifies them as suppressed and says so. Consistent. | **FALSIFIED** | — | None. |
| 27 | **Grok M1** | 11 pp exceeds CQG length for a negative catalogue; a 4–5 pp Letter is appropriate | whole ms | Directly contradicts DP1N-20's adopted decision (CQG **Paper**, grow to 12–16 pp) and the R2 Claude leg's 13.5–14.5 pp recommendation. Referee variance on form (pattern-066); a portfolio decision already taken, not a defect. | OPINION/GENRE | — | Record only. |
| 28 | **Grok M2** | `κn_ψ²/ρ_Λ ≃ 3.884e−69` is taken from the companion; neither `n_ψ = 100 cm⁻³` nor the conversion is supplied | Sec. II p. 2 | `main.tex:267` prints `M_Pl=1.22089e28 eV` **and** `n_ψ=100 cm⁻³`; `273` prints the full result with its explicit `(n_ψ/100 cm⁻³)²` scaling; `737` and `828` repeat the benchmark. Independently recomputed here to `3.884e−69`. The chain is entirely in-paper. | **FALSIFIED** | — | None. |
| 29 | **Grok M3** | "Trace-vector is the larger piece" rests on a single ratio at one γ; no scan over `0.1 ≲ γ ≲ 1` | Sec. VII p. 9 | The claim is analytic — `β/α = 1/(2γ)`, monotone — so the benchmark value is representative rather than cherry-picked, and the γ-dependence is printed in closed form. A scan would be presentational. | OPINION/GENRE | — | Optional one clause noting `β/α>1` for all `γ<0.5`. |
| 30 | **Grok N1** | "(Dated: September 2, 2026)" is an internal bookkeeping tag; remove | p. 1 | `date` = 2026-09-02: current, not future. A revtex `\date` line is standard journal front matter, and the `\paperVersion`-in-`\date` defect was already closed under DP1N-08. Third consecutive round for this claim. | **FALSIFIED** (skill auto-FALSIFY Rule 3) | — | None. |
| 31 | **Grok N2** | Self-citations carry "future DOIs" and non-peer-reviewed disclaimers | references | Zenodo DOI `10.5281/zenodo.21481838` resolves and is dated 2026-07-22 — past. Grok's own text concedes the entries are "acceptable as long as the main text does not treat them as established literature", which the disclaimers ensure. Not a defect claim. | **FALSIFIED** / self-withdrawn | — | None. |
| 32 | Claude PART A | DP1N-30's "chiral-count bound" removal succeeded (grep 0 hits) but the removal deleted the input generating the 61-order endpoint | `main.tex`, P1C `1578–1580` | Verified: P1C's 61 endpoint comes from `Δγ/γ ∼ 0.3`, the chiral-count input. The Note now contains nothing that could produce it. | **REGRESSION-FROM-CLOSURE** (couples to #3/#4) | MAJOR | Resolves with the item-3 decision. |

### Verdict tally (32 rows)

| Class | Count |
|---|---|
| REGRESSION-FROM-CLOSURE | **7** (#1, #3, #4, #7, #10, #14, #32) |
| GENUINELY-NEW-REAL | **11** (#2, #5, #6, #8, #9, #11, #12, #13, #15, #16, #17) |
| RE-FLAG-OF-DISCLOSED | 5 (#18, #19, #21, #23, #24) |
| FALSIFIED | 6 (#20, #22, #25, #26, #28, #30) + #31 self-withdrawn = **7** |
| OPINION/GENRE | 2 (#27, #29) |
| OUT-OF-SCOPE | 0 |

**No fabricated result was found in v1N.0.3.** Every traced value (`−3κ/16`, `γ²/(1+γ²)`, `8πγ/(1+γ²)=5.65031`, `−24πκγ³/(1+γ²)²`, `1/(2γ)=2.105`, `3.884e−69`, `1.4e−6`, `61.45`/`66.78`) reproduces its cited source or my own recomputation. Where the paper is wrong it is wrong in a *displayed step or a label*, never in a result.

## PART 3 — Canonical real items for v1N.0.4 (fingerprint-deduped across legs and against R1/R2)

14 canonical items. **★ = regression introduced by the R2 closure.**

| ID | Item | Sev | Class | Rows |
|---|---|---|---|---|
| **DP1N-44** ★ | ρ+3p repulsion chain: `ρ+3p=+2L` not `−2L`, and Eq. (3) gives `L<0` not `L>0`. Two errors that cancel; conclusion correct, every displayed step wrong | MAJOR | SUBSTANTIVE | #1 |
| **DP1N-45** ★ | Eq. (11) yields 74.3 orders; retained window 61–67 comes from P1C's different `(Δγ/γ)(H₀/M_Pl)` relation (61.45 / 66.78 reproduced exactly). Compounded by DP1N-53 and by the DP1N-30 deletion of the chiral-count input | MAJOR | SUBSTANTIVE — **scope decision** | #3, #32 |
| **DP1N-46** ★ | Directive-Q1 leaks printed in the PDF: the "(SSOT)" erratum notice (`948–950`), the "~4.5×" reference to a superseded draft (`953–954`), "internally tracked as v1N.0.3" (`1104`, created by the DP1N-40 closure), "(P1A)" tag (`627`) | MAJOR | GENRE (directive-Q1 hard gate) | #5, #6, #7, #8 |
| **DP1N-47** | B2/B5/B6/B10 citations (`BlagojevicHehl2013`, `BoehmerBurnett2008`, `Weinberg1989`) establish topics, not the propositions attached; abstract asserts the barriers are "literature-sourced" | MAJOR | SUBSTANTIVE — **scope decision** | #9, #24 |
| **DP1N-48** ★ | "reduced-Planck-mass convention" mislabels `1.22e19 GeV` (reduced = `2.4335e18`) in the sentence added to prevent an 8π ambiguity | MAJOR | SUBSTANTIVE (one word) | #10 |
| **DP1N-49** | Signature-independence claim conditioned on an unjustified "spacelike-normalized `J⁵`" premise | MAJOR | SUBSTANTIVE | #2 |
| **DP1N-50** | Table I caption calls κ "the Barbero–Immirzi symbol". **DP1N-29 recorded closed in SSOT; not closed** | MINOR | SUBSTANTIVE | #11 |
| **DP1N-51** | Residual "parity-odd" language at `850`, `852`, `909`, and the section's own summary at `979`, contradicting the new mixed-parity statement at `936` | MINOR | SUBSTANTIVE | #13 |
| **DP1N-52** ★ | Discussion `1032–1033` restates the "≥58 orders against the observed birefringence amplitude" misdescription that DP1N-33 removed at `692–695` | MINOR | SUBSTANTIVE | #14 |
| **DP1N-53** ★ | Table II R3 row credits a "mass-dimension lock" occurring once and carried only by P1C | MINOR | SUBSTANTIVE | #4 |
| **DP1N-54** | Gap-equation prefactor `N_cN_f/(4π²)` printed without derivation or citation (only `I>0` is load-bearing) | MINOR | SUBSTANTIVE | #15 |
| **DP1N-55** | "vanishes only in the γ→∞ limit" — `O4 ∝ γ³/(1+γ²)²` also vanishes as γ→0 | MINOR | SUBSTANTIVE | #16 |
| **DP1N-56** | O4 irrep sentence contradicts itself: "supported only by the non-axial irreps … carried entirely by the axial×trace-vector cross term" | MINOR | SUBSTANTIVE | #17 |
| **DP1N-57** | Abstract 444 words vs CQG ≈300. **DP1N-37 recorded closed in SSOT; not closed** | MINOR | **GENRE/LENGTH** | #12 |
| **DP1N-58** | Archival residual: mint Zenodo version DOIs for P1C v1C.0.16 and the three theory-audit artifacts (currently commit-pin only) | MINOR | **VENUE/ARCHIVAL** (packaging) | #18, #19, #21 |

**SUBSTANTIVE: 12 · GENRE/LENGTH/VENUE: 3** (DP1N-46, DP1N-57, DP1N-58 — note DP1N-46 is genre in kind but a hard publication gate under directive Q1).
**Regressions from the R2 closure: 6** (DP1N-44, 45, 46, 48, 52, 53).

### The finding this round most wants recorded

The R2 closure converted six "assert it" items into "display the derivation" items. **Three of the newly displayed derivations are wrong** (the sign chain, the substituted scaling relation, the convention label) and two more closures propagated incompletely (DP1N-33 → `1033`, DP1N-30 → the deleted 61-order input). Two items are recorded closed in SSOT that a line check shows are untouched. The remedy is **arithmetic and grep verification of every newly displayed step and every SSOT closure claim before the next bump**, not another review board. `research/theory_audit/p1n_r2_checks_2026_09_02.py` should be extended to assert the sign chain, the Eq. (11) order count, and the 61/67 endpoints, so this class cannot recur silently.

## PART 4 — Science/scope decisions outstanding (directive R2)

Two of the fourteen are decisions rather than fixes; the other twelve are arithmetic, wording, or packaging, executable without judgment.

1. **DP1N-45 — which relation defines the quoted orders.** Option A: restore P1C's `(Δγ/γ)(H₀/M_Pl)` relation into the Note and keep "61–67" (the endpoints then reproduce exactly, and DP1N-53's Table II row becomes supported), which also requires restoring the chiral-count input the DP1N-30 closure deleted, in a form that survives its own objection. Option B: keep Eq. (11) and re-quote the window it actually implies, ≈68–74 orders, updating the abstract, Sec. V, Table II, and the Conclusions. **Option A is the smaller edit and the more defensible provenance; Option B is the more honest if the Note does not want to carry `H₀/M_Pl`.** Either strengthens the closure (68–74 ≫ 61–67). No new computation is required for either.
2. **DP1N-47 — derive or downgrade.** Either write the 2–4-line derivations for B2, B5, B6, B10 that R2's closure instruction already asked for, or downgrade the abstract's "literature-sourced" wording to what the citations establish and demote the four entries out of the headline count. **The downgrade is the honest minimum; the derivations are the stronger paper.**

Neither requires new compute, new data, or a change to any conclusion. Both are recorded as decisions, not findings, per directive R3.

## PART 5 — Convergence statement (directive R2)

**This round did not bottom out in genre/length/venue.** Twelve of fourteen canonical items are substantive, and six are regressions the R2 closure itself introduced — so R3 was a *productive* round, not a variance round, and the two-round convergence budget was correctly spent.

**After v1N.0.4 closes the fourteen items above — including taking the two decisions in PART 4 — rounds stop.** What would remain is exactly:

- **Length/format:** abstract to ≈300 words (DP1N-57) and the standing 11 pp vs Letter disagreement, on which Grok M1 (4–5 pp Letter) and the R2 Claude leg (13.5–14.5 pp Paper) point in opposite directions on unchanged content — textbook pattern-066 referee variance on form, already settled by DP1N-20's adopted CQG-Paper decision.
- **Venue/archival:** Zenodo DOIs (DP1N-58) — packaging, closed by minting, not by editing.
- **Standalone-reader:** raised by all three legs every round, disclosed openly in-paper every round, and structurally bounded by the companion architecture; it is a venue judgment, not a defect.

**No science decision would be outstanding after v1N.0.4**, provided both PART 4 decisions are taken *in* v1N.0.4 rather than deferred. The paper's physics — Cartan elimination, the contact term, the transparency theorem, the operator rank/count, the Popławski mapping — is verified sound and correctly scoped at v1N.0.3; every remaining defect is in a displayed step, a label, or a cross-reference.

**Condition on stopping:** v1N.0.4 must ship with a machine-checkable assertion for each of the three regressed derivations (sign chain, Eq. (11) order count, 61/67 endpoints) and a line-level re-verification of every SSOT-recorded closure. Absent that, the closure record is not trustworthy enough to declare convergence on, and this round demonstrated why. **Clean-wave count for P1N: 0.**
