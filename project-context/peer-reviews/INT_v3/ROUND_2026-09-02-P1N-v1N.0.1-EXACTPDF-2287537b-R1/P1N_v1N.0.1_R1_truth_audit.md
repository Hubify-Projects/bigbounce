# P1N v1N.0.1 — R1 truth audit (Opus, verdict-first)

**Round:** `ROUND_2026-09-02-P1N-v1N.0.1-EXACTPDF-2287537b-R1`
**Manuscript:** `arxiv/paper1bc_ech_note/main.tex` (596 lines) → `main.pdf`
**Exact-PDF binding:** sha256 `2287537b1cf2420b2aa043b6d07da1281fb2844a82e296e7658467c7362747ba` — **VERIFIED** by `shasum -a 256` in this audit. 6 pp, 4144 words (`pdftotext | wc -w`).
**Auditor stance:** skeptical in both directions; every verdict decided from the source `.tex`, the source manuscripts, the frozen theory-audit artifacts, and a ≥300-DPI render (`pdftoppm -r 300`, pp. 2, 4, 5) — never from a leg's verdict word (skill Rules 6/7/8).
**Date:** 2026-09-02

## Legs on this board

| Leg | Model | Verdict word (diagnostic only) | Tagged items in raw | Items dispositioned | Gap |
|---|---|---|---|---|---|
| Claude INT referee | claude-opus | major-revisions | 6 MAJOR + 10 MINOR = 16 | 16 | no |
| Grok API | grok-4.3 | REJECT | 5 ESSENTIAL + 4 MAJOR + 5 MINOR + 1 obs block = 15 | 15 | no |
| Gemini API | gemini-3.1-pro-preview | REJECT | 7 ESSENTIAL (E5 split in two) + 2 MAJOR + 1 MINOR = 11 | 11 | no |
| Perplexity | — | **ABSENT** (401 auth failure, `api_legs_run.log`) | — | — | recorded ABSENT, never as clean (Rule 4) |

**42 finding-rows audited. 0 BLOCKER-tagged items** (explicit observation, not assumption).

## Verdict-class counts

| Verdict | Count |
|---|---|
| REGRESSION (real; source manuscript had it right) | **3** |
| GENUINELY-NEW-REAL | **29** (29 rows → **16** distinct items after fingerprint dedup) |
| RE-FLAG-OF-DISCLOSED | **3** |
| FALSIFIED | **3** |
| OPINION/GENRE | **4** |
| OUT-OF-SCOPE | 0 |

**Canonical real items after dedup: 19** (3 regressions + 16 genuinely-new-real).

---

## Sources used for verification

- `arxiv/paper1c_nogo_survey/main.tex` — **P1C v1C.0.16** (`main.tex:417`)
- `arxiv/paper1a_ech_nogo.tex` — **P1A v1A.0.127** (`main.tex:100`)
- `research/theory_audit/ech_torsion_onshell_2026_08_08.md` (+ `.json`, `.py`)
- `research/theory_audit/operator_basis_adjudication_2026_08_07.md` (incl. 2026-08-08 ERRATUM ADDENDUM)
- `research/theory_audit/fierz_adjudication_2026_08_05.md` (+ `.json`, `.py`)
- `project-context/peer-reviews/INT_v3/ROUND_2026-08-08-P1C-v1C.0.15-EXACTPDF-f3e29c45-R13CONV/P1C_v1C.0.15_truth_audit.md`
- `project-context/SESSION_HANDOFF_2026-09-02.md:32` (CQG venue-form finding)
- 300-DPI renders of PDF pp. 2, 4, 5

---

## Per-finding table — Claude INT leg (16)

| # | Claim | Location | Verified against | Verdict | Sev | Closure instruction |
|---|---|---|---|---|---|---|
| C-M1 | "On the on-shell ECH branch the single-curvature pair (O1, O6) vanishes by the algebraic Bianchi identity on the torsion-free connection" reintroduces pre-erratum physics and self-contradicts within one paragraph | Note `main.tex:478–480`; **confirmed verbatim on the 300-DPI render of p. 4 right column** | `ech_torsion_onshell_2026_08_08.md` §6 `[L48]`–`[L50]`: `O1 + O2 = ½O4 ≠ 0` on six curved on-shell ECH configurations, so `O1 = O6 = −O2 + ½O4`, **not** zero; the ERRATUM ADDENDUM to `operator_basis_adjudication_2026_08_07.md` scopes the vanishing to γ→∞. **P1C v1C.0.16 `main.tex:2087–2098` states the correct branch-qualified version verbatim** ("That branch qualifier is essential: the identity used is the *torsion-free* first Bianchi identity, which a nonzero on-shell torsion violates… O1 and O6 are therefore not exact total derivatives on shell"), closed under R13 | **REGRESSION** | MAJOR | Restore P1C `main.tex:2087–2098` (branch split + `O1=O6=−O2+½O4`) into Note Sec. VI. No physics change: remainder is the same `(J⁵·J⁵)` at the same `MPl^{-2}` power. |
| C-M2 | Printed `O5^{[4]} = −(3/2)κ(J⁵·J⁵)` is the γ→∞ READING-II value while Eq. (2) is READING-I; two normalizations carried silently | Note `main.tex:476–478`, `186–189`; **render p. 4 confirms `O5^{[4]} = −(3/2)κ(J⁵·J⁵)` unqualified** | `ech_torsion_onshell_2026_08_08.md` §5 `[L27]`–`[L30]` (λ_I/λ_II = 2, "a real internal inconsistency in P1C") and §6 `[L33]`/`[L39]`. **P1C v1C.0.16 header `main.tex:351–358` records "CONVENTION FIXED … The survey now uses ONE normalization throughout — Eq. (E2)'s … Consequently O5 reduces to −3 kappa [gamma^2/(1+gamma^2)] (J5.J5)"** | **REGRESSION** | MAJOR | Adopt Eq. (E2)/READING-I once, stated in Sec. II; print `O5^{[4]} = −3κ[γ²/(1+γ²)](J⁵·J⁵)` as P1C v1C.0.16 does. Never carry both. |
| C-M3 | Operator-completeness claim drops the R13-M3 closure: `O5` is P-**even** off shell, and the ε-free P-odd density `T^a{}_{ab}J^{5b}` is neither enumerated nor disposed of | Note `main.tex:458–471` (construction rule), `539–541` (Conclusions), abstract `93–98` | R13 truth audit row M3: "GENUINELY-NEW-REAL … **CLOSED v1C.0.16 by scoping (option b)**". **P1C v1C.0.16 `main.tex:2106–2108`** carries the P-even clause; **`main.tex:2132–2136`** (`eq:vj5_onshell`) exhibits `T^a{}_{ab}J^{5b} = 3β(J⁵·J⁵)`, `β = κγ/[4(1+γ²)]`; **`main.tex:2231–2237`** states the trace-vector is not in the excluded set | **REGRESSION** | MAJOR | Restore P1C `main.tex:2106–2108` + `2132–2136` + `2231–2237`. Restate the rule as "one spacetime ε contraction" (drop "parity-odd" from the rule); the added density *strengthens* the disposal statement. |
| C-M4 | Popławski identification ("identical", "the same sign", "algebraically identical") holds only as γ→∞; no signature bridge | Note `133`, `190–196`, `66–73`, `527–531`, title | `ech_torsion_onshell_2026_08_08.md` §3 `[L17]` (pure axiality **is** the γ→∞ limit), `[L23]` (β/α = 2.1053 at γ = 0.2375 — the non-Popławski trace-vector piece is the **larger**). Note's own `main.tex:195–208` concedes purely-axial "holds only in the strict Einstein–Cartan limit". Coefficient γ²/(1+γ²) = 0.053 at γ = 0.2375 (~19× below EC). Popławski works in the opposite signature; no bridge is given, while a bridge **is** given for FMT (`main.tex:183–184`) | **GENUINELY-NEW-REAL** | MAJOR | See closure plan (2). Scope to γ→∞; state the finite-γ suppression and the trace-vector accompaniment; state the claim in signature-independent physical terms. |
| C-M5 | Eq. (2) is the Hehl–Datta term; Hehl uncited though `HehlDattaNJL1971` and `Hehl1976` are defined in the Note's own `.bib` | Note Eq. (2) attribution; `references.bib:43`, `:959` | Verified by key-set diff in this audit: **18 `\cite{}` keys vs 113 `@entry` keys**; `grep -i hehl` over the cited set returns **empty** | **GENUINELY-NEW-REAL** | MAJOR | Cite `HehlDattaNJL1971` + `Hehl1976` at Eq. (2); add Kibble/Sciama + a torsion-cosmology reference (Boehmer) + Shapiro's torsion review. |
| C-M6 | Secs. IV–V unverifiable from the Note + public sources; load-bearing refs are mutable `tree/main` / `blob/main` URLs and a self-declared non-refereed deposit | Note Secs. IV–V, `549–566`; refs [6],[7],[9],[15] | Note `main.tex:553–558` uses `\artifact{}` → `blob/main/...`; `main.tex:563–566` declares P1C "not independently resubmitted"; `main.tex:234–235`, `277–279` defer the regulated NJL derivation and the full transparency statement to [6]. R13 truth audit carries this as OPEN MINOR-6 + the "refereed-companion gate" checklist item, carried to R14, never closed. **The merge makes it load-bearing**: P1C at ~25 pp carried its own derivations; the Note at 6 pp carries none | **GENUINELY-NEW-REAL** (re-flag of an open, never-closed item, materially worsened by the merge) | MAJOR | See closure plan (4). Mint Zenodo version DOIs for P1C and both theory-audit artifacts; pin every GitHub URL to a commit SHA; bring the B1–B14 and Route-2/3 arithmetic in-paper. |
| C-m1 | As printed, `α ∝ γ²/(γ²+1)` and `β ∝ γ/(γ²+1)` divide to `1/γ`, not the stated `1/(2γ)` | Note `main.tex:198–203`; render p. 2 confirms both `∝` signs and `β/α = 1/(2γ)` | `ech_torsion_onshell_2026_08_08.md` §4: `α_E2 = −4πGγ²/(1+γ²)`, `β_E2 = −2πGγ/(1+γ²)` ⇒ `β/α = 1/(2γ)` `[L20]`. **Value correct; printed derivation not** | **GENUINELY-NEW-REAL** | minor | Print the constants, or give the ratio without the two `∝` statements. |
| C-m2 | `β/α` is Holst-sign-convention dependent; `s_H` never fixed | Note `main.tex:198–203` | Artifact `[L10]`,`[L13]`: `β/α = s_H/(2γ)`, computed under both `s_H = ±1` `[L46]`,`[L47]`. The Note fixes `η` and `ε_{0123}` only | **GENUINELY-NEW-REAL** | minor | One clause fixing `s_H = +1`. |
| C-m3 | The correction's size is understated: the trace-vector coefficient is 2.11× the axial one at γ = 0.2375 | Note `main.tex:198–208` | Artifact `[L23]` (40/19 = 2.1053), `[L24]` (1.8248 at γ = 0.274) | **GENUINELY-NEW-REAL** | minor | State the ratio at the programme's γ. |
| C-m4 | `3.6×10^{-69}` is inconsistent with the Note's own `ρ_Λ,obs ≈ (2.25 meV)⁴` | Note `main.tex:139–140`, `214–217`; render p. 2 | Recomputed independently in this audit (`M_Pl = 1.22089e28 eV`, `κ = 8π/M_Pl²`, `n = 100 cm^{-3}`): `κn² = 9.954e-80 eV⁴`; ratio **3.884e-69** at 2.25 meV, **3.620e-69** at 2.29 meV. Printed value corresponds to 2.29 meV | **GENUINELY-NEW-REAL** | minor | Use one `ρ_Λ` value; either print 3.9e-69 or state the 2.29 meV normalization. |
| C-m5 | `ρ_crit` never defined; unqualified it reads as the cosmological critical density, for which `(ρ_crit/ρ_Pl)² ~ 10^{-244}`, not 0.07–0.17 | Note `main.tex:370–374` | Intended object is the LQG **bounce** critical density; **P1A v1A.0.127 `main.tex:1527–1529`** gives `ρ_crit ≃ 0.27–0.41 ρ_Pl`; `0.27² = 0.073`, `0.41² = 0.168` — the printed endpoints. Defining window lost in the merge | **GENUINELY-NEW-REAL** | minor | Restore the `0.27–0.41 ρ_Pl` window inline (P1A `1527–1529`) or rename to `ρ_bounce`. |
| C-m6 | Table I "Src." column (`A…N/O`) has no legend anywhere in the Note; sequence skips I and K | Note `main.tex:302–331`, prose tags `333–388`; render p. 3 | Confirmed: no legend string in `main.tex`. Column is unreadable as printed | **GENUINELY-NEW-REAL** | minor | One caption clause naming the seven foundations and six branches, or drop the column. |
| C-m7 | "closed operator-level" for Route 2's DE leg contradicts the Note's own Table II ("(II) structural") and P1C's Tier-II record | Note `main.tex:396–399` vs `430–432` | P1C v1C.0.16 records the step as Tier-II because it inherits the unproved spanning assertion; the Note's own Table II says (II) | **GENUINELY-NEW-REAL** | minor | "closed at the operator level modulo the spanning assertion (Tier-II)". |
| C-m8 | The three `\artifact{}` links render as three identical "repository artifact" strings with no filename visible, in a floated `center` detached from its introducing colon | Note `main.tex:50`, `554–558`; **verified on the 300-DPI render of p. 5** | `\newcommand{\artifact}[1]{\href{...}{repository artifact}}` — link text is literal and constant | **GENUINELY-NEW-REAL** | minor | `\href{URL}{\texttt{filename}}`; place inline, not in a floating `center`. |
| C-m9 | `references.bib` ships ~95 unused entries inherited from the source manuscripts | `references.bib` | Key-set diff in this audit: **18 cited / 113 defined** | **GENUINELY-NEW-REAL** | minor | Prune for the arXiv tarball; ship the `.bbl`. |
| C-m10 | `β_obs` quoted without detection significance or the "indications not detections" caveat | Note `main.tex:404–406` | P1C `main.tex:1642` carries ≈3.6σ / 2.9σ and the caveat | **GENUINELY-NEW-REAL** | minor | Restore the significances + caveat. |

---

## Per-finding table — Grok API leg (15)

| # | Claim | Location | Verified against | Verdict | Sev | Closure instruction |
|---|---|---|---|---|---|---|
| G-E1 | Abstract's "plausibly supports the bounce / cannot generate DE" is stronger than any calibrated statement; no quantitative `G_s ↔ ρ_Λ` map | abstract, p. 1 | The Note's claim is a **channel-level closure**, explicitly declared as such at `main.tex:107–109` and `157–160`; Eq. (3) `main.tex:214–222` **is** the calibration and is labelled a coefficient-one benchmark. "Plausibly" is already the hedge Grok asks for. The real remainder — that the *positive* half is asserted by citation — is C-M4 | **OPINION/GENRE** (real remainder folded into R4) | — | No separate action; R4 covers it. |
| G-E2 | Load-bearing results imported by citation to companions; a CQG Note must be standalone | pp. 1–2 and throughout | Same fingerprint as C-M6 | **GENUINELY-NEW-REAL (dup → R6)** | ESSENTIAL | R6. |
| G-E3 | The NJL "no nonzero solution" is truncation-dependent, not a theorem of Eq. (1) | p. 2 after Eq. (4) | **Disclosed verbatim** at `main.tex:230–235`: "This conditional-sign result does not exclude other truncations, species structures, non-minimal couplings, or propagating torsion"; abstract `78–81` says "declared … standard mean-field NJL scalar projection" | **RE-FLAG-OF-DISCLOSED** | — | None. |
| G-E4 | Table I functions as an index, not evidence; B8–B14 are one-sentence citations | p. 3, Sec. IV | Same fingerprint as C-M6 | **GENUINELY-NEW-REAL (dup → R6)** | ESSENTIAL | R6. |
| G-E5 | Dividing the two `∝` statements gives `β/α = 1/γ`, not `1/(2γ)` | p. 2 | Same fingerprint as C-m1; independently reached by two legs | **GENUINELY-NEW-REAL (dup → R10)** | ESSENTIAL | R10. |
| G-M1 | Manuscript carries internal-audit / version-history language ("supersedes", "earlier catalog draft", "theory-audit record", "merges two companion papers"), plus a version tag in `\date` | pp. 1, 2, 4, 5 | Verified in `main.tex`: `51–52` (`\paperVersion` printed in `\date` at `63`), `74–75`, `142–145`, `204–208`, `481–483`, `563–566`. Directly contrary to **directive Q1** (no mistake-narration in published works). *Partial confab:* Grok's cited example "R7/R8-style cross-references" does **not** occur in the Note (`grep` empty) — that sub-example is falsified; the rest is verified | **GENUINELY-NEW-REAL** | MAJOR | R8: strip meta/provenance language; drop `\paperVersion` from `\date`; move all of it to the internal record. |
| G-M2 | The rank-4/rank-2 claim and the relations `O1 = O6`, `O1 = ½O4 − O2` are given only by GitHub reference; unreproducible from the Note | p. 4, Sec. VI | Same fingerprint as C-M6 / Gem-E2 | **GENUINELY-NEW-REAL (dup → R6, R7)** | MAJOR | R6 + R7. |
| G-M3 | Eq. (3) omits the `3/16` and the γ factor present in Eq. (2) | p. 2, Eq. (3) | **Disclosed verbatim** at `main.tex:218–220`: "This coefficient-one benchmark omits the actual 3/16 and finite-γ factors" — confirmed on the render | **RE-FLAG-OF-DISCLOSED** | — | None. |
| G-M4 | (pass-2 restatement of M3) the benchmark cannot be reproduced from the displayed Lagrangian | p. 2 | Same; disclosed at `main.tex:218–222`, which also disclaims the composite/EoS mapping | **RE-FLAG-OF-DISCLOSED** | — | None. |
| G-N1 | "Future date … September 2, 2026" must be removed | p. 1 | **`date +%Y-%m-%d` = 2026-09-02.** The date is current, not future — skill auto-FALSIFY Rule 3 (training-cutoff artifact; 6+ consecutive prior rounds, 100% falsified) | **FALSIFIED** | — | None. (The separate `\paperVersion`-in-`\date` defect is R8.) |
| G-N2 | The two blue "repository artifact" strings are production artifacts and must be deleted | p. 5 | **MISLABELED**: they are the `\artifact{}` macro's link text (`main.tex:50`), live hyperlinks, not production leftovers — and there are three, not two. Real kernel (filenames invisible) is C-m8 | **GENUINELY-NEW-REAL (dup → R17), reviewer mislabel** | MINOR | R17 — fix by printing filenames, **not** by deleting the links. |
| G-N3 | Repeated "This Note …" self-reference should be trimmed | throughout | Style; overlaps the meta-language item | **OPINION/GENRE** (folded into R8) | — | R8. |
| G-N4 | Table I caption's "jointly close the four enumerated channels" is unsupported inside the Note | p. 3 caption | Same fingerprint as C-M6 | **GENUINELY-NEW-REAL (dup → R6)** | MINOR | R6. |
| G-N5 | Internal cross-references point at one-sentence summaries whose content is in the companions | throughout | Same fingerprint as C-M6 | **GENUINELY-NEW-REAL (dup → R6)** | MINOR | R6. |
| G-obs | No figures; bibliography carries preprint entries not load-bearing | — | No-figures is a legitimate choice for a theory Note; the unused-entry point is C-m9 | **OPINION/GENRE** (unused-entry half → R18) | — | R18. |

---

## Per-finding table — Gemini API leg (11)

| # | Claim | Location | Verified against | Verdict | Sev | Closure instruction |
|---|---|---|---|---|---|---|
| Gem-E1 | Version-history language and internal audit tags throughout | abstract, Secs. I, II, VI, VIII | Same fingerprint as G-M1; every quoted string verified present in `main.tex` | **GENUINELY-NEW-REAL (dup → R8)** | ESSENTIAL | R8. |
| Gem-E2 | O1–O6 are **never defined mathematically anywhere in the text**, yet their relations and rank are asserted | Sec. VI, p. 4 | Verified: `grep -n 'O_1\|mathrm{O1}' main.tex` — the Note names `{O1–O6}` (`main.tex:463–470`) and identifies O2 (Nieh–Yan), O3 (Pontryagin), O4 ("ε-contracted torsion-square"), O5 (`O5^{[4]}` value only) **in words**, and gives **no defining expression for any of the six**. Confirmed on the 300-DPI render of p. 4 | **GENUINELY-NEW-REAL** | ESSENTIAL | R7: display the six densities explicitly (P1C Sec. V / Table III carries them). |
| Gem-E3 | "≳58 orders", "61–67 orders", "O(10^{-122}) at H_0" asserted with no derivation or inputs | Secs. IV–V, p. 4 | Same fingerprint as C-M6 | **GENUINELY-NEW-REAL (dup → R6)** | ESSENTIAL | R6. |
| **Gem-E4** | **"Fatal physics sign error": Eq. (2) with `−(3κ/16)γ²/(1+γ²)` in mostly-plus gives negative energy density ⇒ attractive, contradicting the Popławski bounce; the sign must be flipped** | Sec. II, Eq. (2), p. 2 | **FALSIFIED on three independent grounds.** (i) **The Note's Eq. (2) sign is the independently computed one.** `ech_torsion_onshell_2026_08_08.md` §5 `[L27]` solves the ECH connection equation from scratch **in the Note's own conventions** (mostly-plus `η = diag(−,+,+,+)`, `ε` normalization self-checked `[L01]`,`[L02]`) and back-substitutes: `L_int = −3γ²κλ²/[16(γ²+s_H²)](J⁵·J⁵)` — the same negative coefficient, with λ² > 0 so the sign is convention-independent. The artifact reproduces Eq. (2) exactly, sign included. (ii) **The physics premise is inverted.** Gemini asserts "Popławski's bounce requires a positive energy density (repulsion)". Gravitational repulsion in FRW is `ρ + 3p < 0`; Popławski's mechanism is precisely a **negative** spin–spin correction to the effective energy density, which cancels `ρ` at high spin density and drives `H² → 0` — a *positive* correction would deepen, not halt, the collapse. (iii) **The stress-tensor step is invalid here.** `T_{μν} = g_{μν}L_int` holds only for a Lagrangian whose sole metric dependence is `√−g`; `J_5^I J_{5I}` is built from tetrad-contracted fermion bilinears, so the tetrad variation contributes and the quoted `ρ = −L_int` does not follow. Separately, "repulsive" at `main.tex:228–230` is the **NJL-channel** sense fixed by P1A's declared interaction `+G_s(ψ̄ψ)²` (P1A v1A.0.127 `main.tex:1786–1789`), a statement about the gap equation, not about a gravitational energy density. **Gemini has been wrong on ECH signs before; it is wrong here, and the settled artifact is cited either way.** The real remainder — that the Note asserts the bounce by citation without exhibiting the negative effective-density correction, and gives no signature bridge to Popławski — is **C-M4/R4**, not a sign error | **FALSIFIED** | — | No sign change. Record the falsification in `DISPOSITIONS/P1N.md` so it is not re-litigated; address the real remainder under R4. |
| **Gem-E5a** | **"Fierz rearrangement coefficient error": A×A yields `+2(ψ̄ψ)²`, so `G_s = −3κ/16` is quantitatively wrong** | Sec. II A, Eq. (4), p. 2 | **FALSIFIED** by `research/theory_audit/fierz_adjudication_2026_08_05.md`, an independent adjudication that built explicit 4×4 Dirac matrices **in both signatures**, solved the full 5×5 Fierz matrix from the 256-component tensor identity, and re-derived the anticommuting-field map with an exact Grassmann engine (no remembered coefficient table). Result `[L08]`: the operator row is `(J⁵·J⁵) → SS + ½VV + ½AA − PP` — the **SS coefficient is exactly +1**, unique solution, signature-independent `[L06]`,`[L09]`, `F² = 𝟙` verified `[L02]`,`[L04]`. Hence `G_s = (−3κ/16)(+1) = −3κ/16` `[L16]`, and the adjudication's headline verdict is **"P1A-CORRECT — no published-P1A correction required."** Gemini's factor of 2 matches **no** tested convention among the 8 basis variants in either signature `[L17]`; the one historical error in this chain was the frozen monolith's spurious ¼ (`G_s = −3κ/64`), already retracted | **FALSIFIED** | — | No coefficient change. Cite the adjudication in the referee response. |
| **Gem-E5b** | The `γ²/(1+γ²)` factor present in Eq. (2) is dropped in Eq. (4) with no statement that the γ→∞ limit is being taken | Sec. II A, Eq. (4), p. 2 | **CONFIRMED on the 300-DPI render of p. 2**: Eq. (2) prints `−(3κ/16)[γ²/(1+γ²)]`, Eq. (4) prints `G_s = −3κ/16 < 0` with no limit statement anywhere between them. The Claude leg verified the *value* as "consistent with Eq. (2) at γ→∞" but did not flag the **unstated** limit. At γ = 0.2375 the factor is 0.053, so the printed `G_s` is ~19× the ECH value. The repulsive **sign** — hence the no-condensate conclusion — is γ-independent, so no result moves | **GENUINELY-NEW-REAL** | MAJOR (per skill Rule 8, dispositioned at the higher of tag/body) | R9: either print `G_s = −(3κ/16)γ²/(1+γ²)` or state "(Einstein–Cartan limit γ→∞; the sign, and hence the conclusion, is γ-independent)". |
| Gem-E6 | "Explicit placeholders in manuscript": the three "repository artifact" lines are uncompiled placeholder text | Data & Code, p. 5 | **MISLABELED** — they are the `\artifact{}` macro's link text (`main.tex:50`), compiled and hyperlinked, not placeholders. But the referee-visible symptom is real and is C-m8: no filename is visible in the rendered document | **GENUINELY-NEW-REAL (dup → R17), reviewer mislabel** | ESSENTIAL→minor | R17. |
| Gem-E7 | Load-bearing refs [7], [9], [15] point at the mutable `main` branch; not a frozen audit trail | bibliography, p. 6 | Verified: `main.tex:50` builds `blob/main/...`; `main.tex:553` prints the bare repo URL. Same fingerprint as C-M6 | **GENUINELY-NEW-REAL (dup → R6)** | ESSENTIAL | R6 (commit-pin / DOI sub-item). |
| Gem-M1 | The rank-4/rank-2 result is justified solely by an external GitHub markdown file | Sec. VI, p. 4 | Same fingerprint as C-M6 / Gem-E2 | **GENUINELY-NEW-REAL (dup → R6, R7)** | MAJOR | R6 + R7. |
| Gem-M2 | "the full regulated derivation is carried in the archived companion [6]" and the analogous transparency sentence fail the standalone test | Secs. II A, III | Verified at `main.tex:234–235` and `277–279`. Same fingerprint as C-M6 | **GENUINELY-NEW-REAL (dup → R6)** | MAJOR | R6. |
| Gem-N1 | The transparency theorem is a standard textbook consequence of the Bianchi identity; calling it a novel theorem overstates it | Sec. III | The Note does **not** claim the identity is new — `main.tex:263–267` explicitly derives it from the first algebraic Bianchi identity and distinguishes it from the two-curvature Pontryagin density. The contribution claimed is the **all-orders classical statement with an explicit hypothesis list**, which the Claude leg independently judged "a modest but genuine and cleanly-executed sharpening". Novelty weight is a referee judgment call, not a defect | **OPINION/GENRE** | — | Optional: one clause acknowledging the identity itself is standard. |

---

## Canonical real-item list (19; fingerprint-deduped)

| ID | Item | Class | Legs | Sev |
|---|---|---|---|---|
| **R1** | Sec. VI asserts (O1, O6) vanish by the torsion-free Bianchi identity **on the on-shell ECH branch**; correct statement is `O1 = O6 = −O2 + ½O4` | **REGRESSION** vs P1C v1C.0.16 `main.tex:2087–2098` | C | MAJOR |
| **R2** | `O5^{[4]} = −(3/2)κ(J⁵·J⁵)` is READING-II at γ→∞ while Eq. (2) is READING-I; two normalizations carried silently | **REGRESSION** vs P1C v1C.0.16 `main.tex:351–358` | C | MAJOR |
| **R3** | R13-M3 closure dropped: `O5` P-even off shell, and the ε-free P-odd density `T^a{}_{ab}J^{5b} = 3β(J⁵·J⁵)` unenumerated | **REGRESSION** vs P1C v1C.0.16 `main.tex:2106–2108`, `2132–2136`, `2231–2237` | C | MAJOR |
| **R4** | Popławski identification ("identical", "the same sign") stated above its evidential strength; exact only as γ→∞; no signature bridge; bounce asserted by citation | GENUINELY-NEW-REAL | C, Gem(E4 remainder), G(E1 remainder) | MAJOR |
| **R5** | Hehl–Datta attribution missing for Eq. (2); `Hehl1976`/`HehlDattaNJL1971` defined-but-uncited; 18-ref list thin for the topic | GENUINELY-NEW-REAL | C | MAJOR |
| **R6** | Standalone-evaluability: B1–B14 and Route-2/3 budgets asserted, not derived; sole sources are mutable `tree/main`/`blob/main` URLs and a self-declared non-refereed, never-to-be-submitted companion | GENUINELY-NEW-REAL (open R13 MINOR-6, worsened by the merge) | C, G×5, Gem×5 | MAJOR |
| **R7** | O1–O6 are never defined mathematically anywhere in the Note | GENUINELY-NEW-REAL | Gem, G | MAJOR |
| **R8** | Version-history / internal-audit / provenance language throughout, plus `\paperVersion` printed in `\date` — directive Q1 violation | GENUINELY-NEW-REAL | G, Gem | MAJOR |
| **R9** | Eq. (4) drops `γ²/(1+γ²)` with no stated limit | GENUINELY-NEW-REAL | Gem | MAJOR |
| **R10** | Printed `∝` pair divides to `β/α = 1/γ`, not the (correct) `1/(2γ)` | GENUINELY-NEW-REAL | C, G | minor |
| **R11** | Holst sign convention `s_H` never fixed, though `β/α = s_H/(2γ)` | GENUINELY-NEW-REAL | C | minor |
| **R12** | Trace-vector irrep is 2.11× the axial one at γ = 0.2375 — the correction's size is understated | GENUINELY-NEW-REAL | C | minor |
| **R13** | `3.6×10^{-69}` corresponds to 2.29 meV, not the Note's printed `(2.25 meV)⁴` (recomputed: 3.884e-69) | GENUINELY-NEW-REAL | C | minor |
| **R14** | `ρ_crit` undefined; the LQG window `0.27–0.41 ρ_Pl` (P1A `main.tex:1527–1529`) was lost in the merge | GENUINELY-NEW-REAL | C | minor |
| **R15** | Table I "Src." column has no legend anywhere | GENUINELY-NEW-REAL | C | minor |
| **R16** | "closed operator-level" contradicts Table II's `(II)` and P1C's Tier-II record | GENUINELY-NEW-REAL | C | minor |
| **R17** | `\artifact{}` renders three identical "repository artifact" strings, no filenames visible, floated away from the introducing sentence | GENUINELY-NEW-REAL | C, G, Gem | minor |
| **R18** | `references.bib`: 18 cited / 113 defined — ~95 unused entries shipped | GENUINELY-NEW-REAL | C, G | minor |
| **R19** | `β_obs` quoted without its ≈3.6σ / 2.9σ significances and the "indications not detections" caveat | GENUINELY-NEW-REAL | C | minor |

---

## Closure plan

### (1) Passages to restore verbatim from the source manuscripts

| Target in Note | Restore from | Closes |
|---|---|---|
| Sec. VI ¶2, `main.tex:476–491` | **P1C v1C.0.16 `main.tex:2087–2098`** — the branch split, "That branch qualifier is essential", and `O1^{[4]} = O6^{[4]} = −O2^{[4]} + ½O4^{[4]}` with the disposal-class restatement | **R1** |
| Sec. VI ¶2 `O5^{[4]}` value; a new one-clause normalization statement in Sec. II | **P1C v1C.0.16 `main.tex:351–358`** (CONVENTION FIXED — Eq. (E2)/READING-I throughout) and **`main.tex:2100–2112`** (`O5 → −3κ[γ²/(1+γ²)](J⁵·J⁵)`) | **R2** |
| Sec. VI construction rule `main.tex:458–471` + one new equation | **P1C v1C.0.16 `main.tex:2106–2108`** (O5 is P-even; the parity-odd label belongs to the pre-reduction densities) + **`main.tex:2132–2136`** (`eq:vj5_onshell`: `T^a{}_{ab}J^{5b} = 3β(J⁵·J⁵)`, `β = κγ/[4(1+γ²)]`) + **`main.tex:2231–2237`** (the trace-vector irrep is *not* in the excluded set) | **R3** |
| Sec. VI, new display of the six densities | **P1C v1C.0.16 Sec. V construction rule + Table III** (the explicit `O1…O6` expressions) | **R7** |
| B12, `main.tex:370–374` | **P1A v1A.0.127 `main.tex:1527–1529`** (`ρ_crit ≃ 0.27–0.41 ρ_Pl`, entropy-scheme dependence) | **R14** |
| Sec. II A, around Eq. (4) | **P1A v1A.0.127 `main.tex:1786–1789`** (the declared interaction `+G_s(ψ̄ψ)²`, in which `G_s < 0` is repulsive) — one clause, which also pre-empts Gem-E4 on re-review | **R9**, prophylactic for Gem-E4 |
| Sec. V, Route 4 | **P1C `main.tex:1642`** (3.6σ / 2.9σ + "indications rather than established detections") | **R19** |

All seven restorations are **verbatim-or-near-verbatim reinstatements of already-reviewed source text**; none introduces new physics, and the no-go conclusion is unchanged by every one of them (the O1/O6/O4/`V·J⁵` remainders are all the same Fierz-closed `(J⁵·J⁵)` structure at the same `MPl^{-2}` power — `ech_torsion_onshell_2026_08_08.md` §6, "Why the no-go still holds").

### (2) What the Popławski identification can honestly claim (R4)

Established, with artifact backing:
- At **γ → ∞** (Einstein–Cartan; no Holst term) Eq. (2) reduces to the **Hehl–Datta** axial–axial contact term that underlies Popławski's torsion-avoided singularity, and the on-shell torsion is **purely axial** (`ech_torsion_onshell_2026_08_08.md` `[L17]`).
- At **finite γ**: the coefficient carries `γ²/(1+γ²)` — **0.053 at γ = 0.2375**, ~19× below the Einstein–Cartan magnitude; and the on-shell torsion carries a **trace-vector irrep Einstein–Cartan does not have**, with `β/α = s_H/(2γ)` = **2.11 at γ = 0.2375** `[L20]`,`[L23]`, i.e. the non-Popławski piece is the **larger** of the two. The tensor irrep vanishes identically `[L11]`.
- The **sign** of Eq. (2) is independently reproduced in the Note's own mostly-plus conventions `[L27]`; what is *not* established in the Note is a **signature/convention bridge to Popławski's papers**, and the Note nowhere exhibits the negative effective-energy-density correction that produces the bounce.

Sentence at exactly that strength (replaces `main.tex:190–196`, with the abstract, Intro `133`, and Conclusions `527–531` brought into line):

> *In the Einstein–Cartan limit γ→∞, Eq. (2) reduces to the Hehl–Datta four-fermion contact term whose high-spin-density gravitational repulsion underlies Popławski's torsion-avoided singularity [Hehl–Datta 1971; Popławski 2010]. At finite γ the same elimination yields that term suppressed by γ²/(1+γ²) — 0.053 at γ = 0.2375 — and accompanied by a trace-vector torsion irrep, absent in Einstein–Cartan, whose coefficient exceeds the axial one by β/α = 1/(2γ) ≈ 2.11 at that γ. The physical content asserted here is signature-independent — the interaction is repulsive at high spin density — and the bounce itself is a result of the cited works, not derived in this Note.*

Delete "identical", "the same contact term", "the same sign", and "algebraically identical" wherever they stand unqualified. The **title** may stand: "what minimal ECH torsion does for the bounce" is defensible once the γ→∞ scoping is in the body.

### (3) Page target and venue form

**6 pp cannot stand.** Two independent reasons:
1. **Venue form is already settled.** The Note is **4144 words**, and the CQG "Note" ceiling is **≤2500 words** (`project-context/SESSION_HANDOFF_2026-09-02.md:32`). At 6 pp it is *already* a CQG **Paper**, so there is no Note word-budget to protect and no cost to growing it.
2. **The page budget is the mechanism that produced R1, R2, R3, R6 and R7** — three of them regressions against corrections the 25-pp source had already made, on precisely the technical points the merge exists to carry.

**Recommendation: Option A — grow to ~12–16 pp and submit as a CQG Paper.** Restore, in this order: the corrected on-shell disposal table with explicit `O1…O6` definitions under one normalization (R1/R2/R3/R7); a defining inequality or one-paragraph derivation for each of B1–B14 plus the foundation/branch legend (R6/R15); the Route-2/3 budget arithmetic and the LQG `ρ_crit` window (R6/R14); and the transparency theorem's boundary/falloff conditions and second-order Holst verification from P1A, so the Note's sole Tier-I result stops deferring its own proof (R6).

Option B (cut to Secs. II+III at 6 pp and submit P1C separately) is internally coherent and would also close R6, but it reverses the `PORTFOLIO_DECISION_2026-09-02.md` Track-B consolidation and forecloses the merged Note's stated contribution — a **Houston/portfolio decision, not a referee call**. Recorded, not recommended by this audit.

Under either option the manuscript must first strip the provenance/version-history language (R8) — under directive Q1 the published work presents the science in its pure form; the merge/erratum history stays in this audit trail.

### (4) Standalone-evaluability items (R6)

| Item | Action |
|---|---|
| Ref [7] — P1C survey, bare `tree/main` URL, declared never-to-be-submitted | Mint a **Zenodo version DOI** for P1C v1C.0.16 and cite the DOI. |
| Refs [9], [15] — `ech_torsion_onshell_2026_08_08` and `operator_basis_adjudication_2026_08_07`, `blob/main` URLs, the two most load-bearing citations in Sec. VI | Deposit both artifacts (`.md` + `.py` + `.json`) with a Zenodo DOI; **at minimum** pin every `\artifact{}` URL to a commit SHA (change `\newcommand{\artifact}` at `main.tex:50` from `/blob/main/` to `/blob/<sha>/`). |
| Ref [6] — P1A Zenodo deposit, `doi:10.5281/zenodo.21481838`, self-described "not an arXiv preprint and not peer reviewed" | The **Tier-I deferral is the sharp edge**: the Note's only rigorous theorem defers its full statement and its second-order verification to a non-refereed deposit. Bring the boundary/falloff hypotheses and the second-order Holst verification **in-paper** (Option A). The regulated-NJL deferral at `main.tex:234–235` may remain a pointer only if Eq. (4) is restated with its declared-interaction convention (R9). |
| Barrier and route arithmetic | Each of B1–B14 gets its defining inequality in-paper; the "≳58" and "61–67 orders" chains get their intermediate displays. |
| `\artifact{}` presentation | Print filenames as link text and un-float the block (R17); prune the `.bib` to the cited set for the tarball (R18). |

---

## Integrity statement

No verdict in this audit was taken from a leg's verdict word. Both REJECTs decompose into a large, genuinely-real, entirely **fixable** set (R6/R7/R8 dominate them) plus three falsifications; the major-revisions leg carried the three regressions the API legs could not see, because seeing them requires the source manuscripts. **No fabricated result was found in the manuscript** — every traced value (`3κ/16`, `γ²/(1+γ²)`, `G_s = −3κ/16`, `β/α = 1/(2γ)`, `rank 4 / rank 2`, `O1 = ½O4 − O2`, `f_NL = −35/16`, `3.6e-69`, `0.07–0.17`, `β_obs`) reproduces its cited source or artifact. The defects are branch, normalization, scope, attribution, presentation, and evaluability. **The ECH dark-energy no-go conclusion survives every one of the 19 items unchanged.**

**Genuinely-new-real items outstanding: 19. P1N is NOT converged.** Clean-wave count for P1N: **0**.
