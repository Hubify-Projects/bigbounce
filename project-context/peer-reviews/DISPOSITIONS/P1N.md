# P1N disposition ledger

**Canonical source:** `arxiv/paper1bc_ech_note/main.tex`
**Current paper-local version:** `v1N.0.2` (2026-09-02; R1 closure — 19 canonical items incl. 3 regressions closed; see `project-context/SSOT/paper-1n/status.md` for the full item→edit table)
**Claim policy:** channel-level closure of minimal-coupling ECH dark-energy routes only; **no** operator-level completeness theorem, no unrestricted no-go, no ECH dark-energy or birefringence prediction.
**Venue:** CQG — form is **Paper**, not Note (7725 words at v1N.0.2, 4144 words at v1N.0.1, both above the ≤2500-word Note ceiling, `project-context/SESSION_HANDOFF_2026-09-02.md:32`).

## Round history

| Round | Exact PDF sha256 | Legs | Outcome |
| R1 closure | v1N.0.2 sha256 `790795fe3d0cd5c3ba68234ddf3a5336d11fbfa1d402c9bc9d4b3be3013f125d` | — (closure round, no new review board run) | All 19 canonical R1 items (DP1N-01–DP1N-19) + the page/venue decision (DP1N-20) closed. 10 pp / 7725 words (short of the 12–16 pp upper recommendation — flagged as residual). 4-pass compile clean, 0 undef refs, `p1c_consistency_check.py` 4/4 PASS. |
|---|---|---|---|
| `ROUND_2026-09-02-P1N-v1N.0.1-EXACTPDF-2287537b-R1` | `2287537b1cf2420b2aa043b6d07da1281fb2844a82e296e7658467c7362747ba` | Claude INT (major-revisions), Grok API (REJECT), Gemini API (REJECT), **Perplexity ABSENT (401)** | 42 rows audited → 3 REGRESSION, 29 GENUINELY-NEW-REAL (16 distinct), 3 RE-FLAG-OF-DISCLOSED, 3 FALSIFIED, 4 OPINION/GENRE. **19 canonical real items open.** Clean-wave count **0**. Audit: `INT_v3/ROUND_2026-09-02-P1N-v1N.0.1-EXACTPDF-2287537b-R1/P1N_v1N.0.1_R1_truth_audit.md` |

## Open items (R1 board)

| ID | Issue | Status | Evidence / residual scope |
|---|---|---|---|
| DP1N-01 | Sec. VI asserts (O1, O6) vanish by the torsion-free Bianchi identity **on the on-shell ECH branch**; the ECH-branch statement is `O1 = O6 = −O2 + ½O4`. | **CLOSED v1N.0.2** — restored verbatim from P1C `main.tex:2087–2098` into Sec. VI of `arxiv/paper1bc_ech_note/main.tex`. | Correct text exists verbatim in **P1C v1C.0.16 `main.tex:2087–2098`** (closed under R13). Artifact: `ech_torsion_onshell_2026_08_08.md` §6 `[L48]`–`[L50]`; ERRATUM ADDENDUM to `operator_basis_adjudication_2026_08_07.md`. Self-contradictory with the Note's own `O1 = ½O4 − O2` + `O4 ≠ 0`, 12 lines above. No physics change on fix. |
| DP1N-02 | `O5^{[4]} = −(3/2)κ(J⁵·J⁵)` (READING-II, γ→∞) printed alongside Eq. (2) in READING-I; two normalizations, no normalization statement. | **CLOSED v1N.0.2** — single READING-I normalization stated once in Sec. II; `O5^{[4]}=−3κ[γ²/(1+γ²)](J⁵·J⁵)` used throughout. | **P1C v1C.0.16 `main.tex:351–358`** — "CONVENTION FIXED … ONE normalization throughout — Eq. (E2)'s … O5 reduces to −3 kappa [gamma^2/(1+gamma^2)] (J5.J5)". Artifact §5 `[L27]`–`[L30]`, §6 `[L33]`/`[L39]`. |
| DP1N-03 | Operator-completeness argument drops the R13-M3 closure: `O5` is parity-**even** off shell, and the ε-free parity-odd density `T^a{}_{ab}J^{5b}` is unenumerated. | **CLOSED v1N.0.2** — P-even-off-shell clause + `T^a{}_{ab}J^{5b}=3β(J⁵·J⁵)` restored in Sec. VI. | R13 truth audit row M3 (GENUINELY-NEW-REAL, **CLOSED v1C.0.16 by scoping**). Restore **P1C `main.tex:2106–2108`**, **`2132–2136`** (`T^a{}_{ab}J^{5b} = 3β(J⁵·J⁵)`, `β = κγ/[4(1+γ²)]`), **`2231–2237`**. The added density lands in the same Fierz-closed class — it *strengthens* the disposal statement. |
| DP1N-04 | Popławski identification ("identical", "the same contact term", "the same sign", "algebraically identical") stated above evidential strength; exact only as γ→∞; no signature bridge; bounce asserted by citation. | **CLOSED v1N.0.2** — audit's drafted γ→∞-scoped sentence installed (abstract, Intro, Sec. II, Discussion, Conclusions). | `ech_torsion_onshell_2026_08_08.md` `[L17]`, `[L20]`, `[L23]`: γ²/(1+γ²) = 0.053 and β/α = 2.11 at γ = 0.2375 — the non-Popławski trace-vector piece is the larger. Replacement sentence drafted in the R1 audit, closure plan (2). |
| DP1N-05 | Hehl–Datta attribution missing for Eq. (2); `HehlDattaNJL1971` and `Hehl1976` defined-but-uncited in the Note's own `.bib`; 18-reference list thin for the topic. | **CLOSED v1N.0.2** — Hehl–Datta cited at Eq. (3); Kibble1961/Sciama1964/Shapiro2002/BoehmerBurnett2008 added. | Key-set diff: 18 cited / 113 defined; `grep -i hehl` over the cited set empty. Add Kibble/Sciama, a torsion-cosmology reference, and the Shapiro torsion review. |
| DP1N-06 | Standalone evaluability: B1–B14 and the Route-2/3 budgets are asserted, not derived; sole sources are mutable `tree/main` / `blob/main` URLs and a self-declared non-refereed, never-to-be-submitted companion; the sole Tier-I result defers its own proof to a non-peer-reviewed deposit. | **CLOSED v1N.0.2 (SHA-pin fallback)** — Route-2/3 arithmetic, O1–O6 definitions, and Fierz row brought in-paper; `\artifact` links pinned to commit SHA `ded46bc5df8d39bbaac7bfbee16b07f0376bab34` (no Zenodo DOI existed for P1C to mint this session). | P1C at ~25 pp carried its own derivations (deferrals supplementary); the Note at 6 pp carries none (deferrals load-bearing). Fix: Zenodo version DOIs for P1C v1C.0.16 and both theory-audit artifacts; commit-SHA pin in `\artifact` (`main.tex:50`); barrier/route arithmetic in-paper. Flagged by all three legs. |
| DP1N-07 | O1–O6 are never defined mathematically anywhere in the Note, yet their relations and rank are load-bearing. | **CLOSED v1N.0.2** — Eq. (dim4\_defs) displays all six densities explicitly. | Verified in `main.tex` and on the 300-DPI render of p. 4. Restore the explicit densities from P1C Sec. V / Table III. |
| DP1N-08 | Version-history / internal-audit / provenance language throughout ("supersedes", "earlier catalog draft", "theory-audit record", "merges two companion papers"), plus `\paperVersion` printed in `\date`. | **CLOSED v1N.0.2** — meta/provenance language stripped; `\date` no longer prints `\paperVersion`; "this Note"→"this paper". | Sites: `main.tex:51–52`, `63`, `74–75`, `142–145`, `204–208`, `481–483`, `563–566`. Grok M1 / Gemini E1. Published work presents the science in pure form; the merge/erratum history stays in this ledger and the audit trail. |
| DP1N-09 | Eq. (4) `G_s = −3κ/16` drops the `γ²/(1+γ²)` of Eq. (2) with no stated limit. | **CLOSED v1N.0.2** — `G_s=−(3κ/16)[γ²/(1+γ²)]` (Eq. Gs) with explicit γ→∞ clause and P1A declared-interaction citation. | Confirmed on the 300-DPI render of p. 2. Sign — hence the no-condensate conclusion — is γ-independent, so no result moves. Fix by printing the γ factor or stating the γ→∞ limit, plus P1A's declared-interaction clause (`paper1a_ech_nogo.tex:1786–1789`). |
| DP1N-10 | Printed `α ∝ γ²/(γ²+1)`, `β ∝ γ/(γ²+1)` divide to `1/γ`, not the stated (correct) `1/(2γ)`. | **CLOSED v1N.0.2** — derivation clause added showing the two `∝` statements alone give `1/γ`; explicit constants needed for `1/(2γ)`. | Value correct per `[L20]` (`α_E2 = −4πGγ²/(1+γ²)`, `β_E2 = −2πGγ/(1+γ²)`); the printed derivation is not. Raised independently by Claude and Grok. |
| DP1N-11 | Holst sign convention `s_H` never fixed, though `β/α = s_H/(2γ)`. | **CLOSED v1N.0.2** — `s_H=+1` fixed explicitly. | Artifact `[L10]`,`[L13]`,`[L46]`,`[L47]` (both conventions computed). One clause. |
| DP1N-12 | Size of the finite-γ correction understated: trace-vector coefficient is 2.11× the axial one at γ = 0.2375 (1.82× at γ = 0.274). | **CLOSED v1N.0.2** — 2.11× ratio at γ=0.2375 stated in abstract, Sec. II, Discussion. | `[L23]`, `[L24]`. |
| DP1N-13 | `3.6×10^{-69}` corresponds to `ρ_Λ = (2.29 meV)⁴`, not the Note's printed `(2.25 meV)⁴` (independently recomputed: 3.884e-69 vs 3.620e-69). | **CLOSED v1N.0.2** — recomputed to `3.884e-69` with full arithmetic shown; old 2.29 meV value noted as not used. | Known P1C flag (`main.tex:95`). Use one `ρ_Λ` value. 8%; does not move "≈68 orders". |
| DP1N-14 | `ρ_crit` undefined and colliding with the cosmological critical density; the LQG window was lost in the merge. | **CLOSED v1N.0.2** — `0.27–0.41 ρ_Pl` window restored inline at B12. | Restore `ρ_crit ≃ 0.27–0.41 ρ_Pl` from **P1A v1A.0.127 `main.tex:1527–1529`** (`0.27² = 0.073`, `0.41² = 0.168` — the printed endpoints), or rename to `ρ_bounce`. |
| DP1N-15 | Table I "Src." column (`A…N/O`, skipping I and K) has no legend anywhere in the Note. | **CLOSED v1N.0.2** — Src legend added to Table I caption. | One caption clause, or drop the column. |
| DP1N-16 | "closed operator-level" for Route 2's dark-energy leg contradicts the Note's own Table II `(II)` and P1C's Tier-II record. | **CLOSED v1N.0.2** — restated "closed at the operator level modulo the spanning assertion (Tier-II)". | Restate as "closed at the operator level modulo the spanning assertion (Tier-II)". |
| DP1N-17 | `\artifact{}` renders three identical "repository artifact" strings with no filename visible, floated away from the introducing sentence. | **CLOSED v1N.0.2** — `\artifactbase` prints filenames as link text; un-floated into an itemize list. | `main.tex:50`, `554–558`; verified on the 300-DPI render of p. 5. Print filenames as link text; un-float. Mislabeled by Grok N2 ("production artifacts, delete") and Gemini E6 ("uncompiled placeholders") — the links are live; do **not** delete them. |
| DP1N-18 | `references.bib` ships ~95 unused entries (18 cited / 113 defined). | **CLOSED v1N.0.2** — `references.bib` pruned from 113 to 26 entries (exact cited set). | Prune for the arXiv/CQG tarball; ship the `.bbl`. |
| DP1N-19 | `β_obs = 0.342° ± 0.094°` and ACT DR6 quoted without their ≈3.6σ / 2.9σ significances and the "indications rather than established detections" caveat. | **CLOSED v1N.0.2** — ≈3.6σ/2.9σ + "indications not detections" caveat restored in Route 4. | Restore from P1C `main.tex:1642`. |
| DP1N-20 | Page budget / venue form: 6 pp cannot carry the claims made; the budget is the mechanism that produced DP1N-01/02/03/06/07. | **CLOSED v1N.0.2 (Option A adopted, partial)** — grew to 10 pp / 7725 words (from 6 pp / 4144 words); short of the 12–16 pp upper recommendation. Venue form recorded as CQG Paper in the registry. Residual: a future round may add further derivation detail if a referee still finds a step insufficiently self-contained. | **Option A (recommended):** grow to ~12–16 pp and submit as a CQG **Paper** — no Note word budget exists to protect, since 4144 words already exceeds the ≤2500-word Note ceiling. **Option B:** cut to Secs. II+III at 6 pp and submit P1C separately — coherent, but reverses the Track-B consolidation; Houston/portfolio decision, not a referee call. |

## Falsified — do not re-litigate

| Finding | Leg | Verdict | Settled evidence |
|---|---|---|---|
| "Fatal physics sign error: Eq. (2) is attractive, not repulsive; flip the sign" (E4) | Gemini | **FALSIFIED** | (i) `research/theory_audit/ech_torsion_onshell_2026_08_08.md` §5 `[L27]` solves the ECH connection equation from scratch **in the Note's own mostly-plus conventions** and back-substitutes to `L_int = −3γ²κλ²/[16(γ²+s_H²)](J⁵·J⁵)` — the Note's Eq. (2) sign reproduced exactly, λ² > 0. (ii) Gemini's premise is inverted: Popławski's bounce is driven by a **negative** spin–spin correction to the effective energy density (gravitational repulsion in FRW is `ρ+3p < 0`); a positive correction would deepen the collapse. (iii) `T_{μν} = g_{μν}L_int` is invalid for a tetrad-contracted fermion bilinear. Also note "repulsive" at `main.tex:228–230` is the NJL-gap-equation sense of P1A's declared `+G_s(ψ̄ψ)²` (`paper1a_ech_nogo.tex:1786–1789`), not a gravitational energy density. **Gemini has flagged ECH signs incorrectly before; recorded here so no future round re-opens it.** Real remainder (no signature bridge; bounce asserted by citation) is **DP1N-04**. |
| "Fierz rearrangement coefficient error: A×A yields +2(ψ̄ψ)², so `G_s = −3κ/16` is wrong" (E5a) | Gemini | **FALSIFIED** | `research/theory_audit/fierz_adjudication_2026_08_05.md`: explicit 4×4 Dirac matrices in **both** signatures, full 5×5 Fierz matrix **solved** from the 256-component tensor identity, anticommuting map re-derived with an exact Grassmann engine. Operator row `[L08]`: `(J⁵·J⁵) → SS + ½VV + ½AA − PP` — **SS coefficient exactly +1**, unique, signature-independent `[L06]`,`[L09]`. Hence `G_s = −3κ/16` `[L16]`. Headline verdict: **"P1A-CORRECT — no published-P1A correction required."** Gemini's factor 2 matches no tested convention `[L17]`. The real remainder (unstated γ→∞ limit in Eq. (4)) is **DP1N-09**. |
| "Future date — September 2, 2026 must be removed" (N1) | Grok | **FALSIFIED** | `date` = 2026-09-02; the date is current, not future. Skill auto-FALSIFY Rule 3 (training-cutoff artifact; 6+ consecutive prior rounds, 100% falsified). The separate `\paperVersion`-in-`\date` defect is **DP1N-08**. |

## Re-flag of disclosed content — no action

| Finding | Leg | Disclosure site |
|---|---|---|
| "NJL no-go is truncation-dependent, not a theorem of Eq. (1)" (E3) | Grok | `main.tex:230–235` — "does not exclude other truncations, species structures, non-minimal couplings, or propagating torsion"; abstract `78–81` declares the convention. |
| "Eq. (3) omits the 3/16 and γ factors" (M3) | Grok | `main.tex:218–220` — "This coefficient-one benchmark omits the actual 3/16 and finite-γ factors". |
| "Eq. (3) cannot be reproduced from the displayed Lagrangian" (M4, pass-2) | Grok | Same, plus `main.tex:220–222` disclaiming the composite/stress-tensor/EoS mapping. |

## Opinion / genre — recorded, not defects

- Grok E1 (abstract stronger than any calibrated statement) — the Note declares a **channel-level**, not operator-level, closure at `main.tex:107–109`, `157–160`; real remainder is DP1N-04.
- Grok N3 ("This Note …" self-reference) — folded into DP1N-08.
- Grok observations (no figures; preprint entries in the bibliography) — a theory Note needs no figure; the unused-entry half is DP1N-18.
- Gemini N1 (transparency theorem is a standard Bianchi consequence) — the Note already derives it from the standard identity (`main.tex:263–267`) and claims only the all-orders classical statement with an explicit hypothesis list. Novelty weight is a referee judgment. Optional one-clause acknowledgement.

## Provenance

- **No fabricated result was found** in v1N.0.1. Every traced value (`3κ/16`, `γ²/(1+γ²)`, `G_s = −3κ/16`, `β/α = 1/(2γ)`, rank 4 / rank 2, `O1 = ½O4 − O2`, `f_NL = −35/16`, `3.6e-69`, `0.07–0.17`, `β_obs`) reproduces its cited source or frozen artifact.
- **The ECH dark-energy no-go conclusion survives all 19 open items unchanged** — every operator the corrections touch is the same Fierz-closed `(J⁵·J⁵)` structure at the same `MPl^{-2}` power (`ech_torsion_onshell_2026_08_08.md` §6).
- Clean-wave count for P1N: **0**. Not converged.

---

## R2 board — `ROUND_2026-09-02-P1N-v1N.0.2-EXACTPDF-790795fe-R2`

**Exact PDF sha256:** `790795fe3d0cd5c3ba68234ddf3a5336d11fbfa1d402c9bc9d4b3be3013f125d` (re-verified).
**Legs:** Claude INT `major-revisions` (7 MAJOR / 13 MINOR), Grok API `REJECT`,
Gemini API `MAJOR REVISIONS`, **Perplexity ABSENT** (not run; recorded absent).
Round not degraded (no FALLBACK tags; real wall times + packet hashes).
**Audit:** `INT_v3/ROUND_2026-09-02-P1N-v1N.0.2-EXACTPDF-790795fe-R2/P1N_v1N.0.2_R2_truth_audit.md`
**Independent recomputation:** `research/theory_audit/p1n_r2_checks_2026_09_02.py` (6 checks, all assert-pass).

35 leg findings audited → **21 GENUINELY-NEW-REAL, 2 INHERITED-ERROR, 2 RE-FLAG-OF-DISCLOSED,
6 FALSIFIED, 2 OPINION/GENRE, 0 OUT-OF-SCOPE.** **23 canonical real items opened**
(8 MAJOR, 14 MINOR, 1 NIT). R1's 19 items independently spot-verified as honestly closed;
the two closed-with-defect and two partial R1 items are carried forward as new IDs rather
than reopened. **No fabricated result found.** Clean-wave count for P1N: **0**.

### Open items (R2 board)

| ID | Issue | Verdict | Sev | Closure instruction |
|---|---|---|---|---|
| DP1N-21 | Eq. (13) wrong by exactly `8π`: `-24 M_Pl²αβ = -24πκγ³/(1+γ²)²`, not the printed `-3κγ³/(1+γ²)²`; `O4/O5` inverts from `0.22` to `8πγ/(1+γ²) = 5.65` (O4 is the *larger*). `main.tex:796–804` | **INHERITED-ERROR** — verbatim in **P1C v1C.0.16 `main.tex:2118–2123`**, which also prints a dimensionally impossible `-192π²G²` (correct: `-192π²G`). Structural `-24αβ` independently confirmed correct; only the κ substitution fails. No-go conclusion unaffected | MAJOR | Correct Note **and P1C**; re-run/re-commit `dim4_parityodd_enumeration.py` + `operator_basis_adjudication_2026_08_07.*`; record in P1C's ledger. **Science decision.** |
| DP1N-22 | `O1 ≡ O6` identically for the metric-compatible ECH connection (tetrad conversion), so `O1-O6=0` is a tautology and "six-member spanning list, rank four" is partly presentational | **GENUINELY-NEW-REAL** (disclosure regression) — **P1C `main.tex:2041–2043` and `2690` state it openly** ("literally the same density"); the Note dropped the clause. Consistent with `operator_basis_adjudication_2026_08_07` (rank-4 spanning list) | MAJOR | Restore P1C's clause: five distinct densities, rank 4, one null direction is the duplication, only `2O1+2O2-O4=0` carries content, redundancy deliberate. Fix abstract + Conclusions. **Do not delete O6. Science decision.** |
| DP1N-23 | `O5` parity: the Note says "parity-even off shell" and advertises a strictly parity-odd list | **INHERITED-ERROR** — `O5` is P-even **both** off and on shell (ε odd × T even × e even × J⁵ odd). Gemini P1N-M2 **CORRECT**; Claude MINOR 1's "O5 is P-odd off shell" **FALSIFIED**. Wording inherited from P1C `2096–2100` | MAJOR | State the list is ε-construction-rule-admitted and mixed-parity; drop the "parity-odd label belongs to the pre-reduction density" claim in Note **and** P1C. No rank/closure change |
| DP1N-24 | Barrier catalog: **12 of 14** entries carry no citation and no derivation (only B12 sourced, only B14 derived; 4 `\cite` instances in Sec. IV, all in B12) | GENUINELY-NEW-REAL (Claude MAJOR 3 = Grok M1; residual of DP1N-06) | MAJOR | Citation or 2–4-line derivation per B1–B11, B13; demote unsupportable entries out of the "fourteen mechanism-class constraints" headline |
| DP1N-25 | Popławski's dark-energy claim (Ref. [10], GRG 44, 491) is never stated, quantified, mapped to R1–R4, or closed | GENUINELY-NEW-REAL — **yes, the Note must engage it** to be a "what ECH cannot do for dark energy" paper | MAJOR | ~0.5 pp: state the mechanism with its equation, map to R1–R4 (closest R1, where Sec. II already does the work), name closing barrier + tier — or weaken "the four enumerated channels". **Scope decision** |
| DP1N-26 | B7 ("γ fixed at a single universal value") contradicts B12 ("scheme-dependent"); B7's `Sec.~\ref{sec:theory}` cross-reference is empty ("area" occurs only at `515`, `561`) | GENUINELY-NEW-REAL | MAJOR | Cite `Ashtekar2011`/`GhoshMitra2005`; restate B7 as "fixed parameter, not a cycle-varying field"; repoint the cross-reference |
| DP1N-27 | Route 3's "mass-dimension scaling relation" never displayed; one input → a six-order-wide 61–67 output | GENUINELY-NEW-REAL (Claude MAJOR 6 = Gemini P1N-M1). Eq. (9) itself reproduces (`1.38e-6`) | MAJOR | Display the relation with inputs; state what varies across 61–67; label the tier |
| DP1N-28 | "No nonzero solution" asserted; gap equation, regulator, and argument deferred to a non-refereed deposit | GENUINELY-NEW-REAL (`G_s<0` **is** in-paper; the step from it is not) | MAJOR | Write `M = 2G_s M I(M,Λ)`, `I>0`; state the regulator; three-line no-solution argument |
| DP1N-29 | Table I caption calls `κ` "the Barbero–Immirzi symbol" (`435–439`) | GENUINELY-NEW-REAL (closes DP1N-15's residual defect) | MINOR | "…the gravitational coupling `κ`" |
| DP1N-30 | Table II R3 row cites a "chiral-count bound" appearing nowhere else (`696–698`) | GENUINELY-NEW-REAL | MINOR | Import or delete |
| DP1N-31 | SHA pin applied to `\artifactbase` but not the `.bib`: 4 entries still on mutable `tree/main`/`blob/main` (`references.bib:279,287,295,303`) | GENUINELY-NEW-REAL (residual of DP1N-06) | MINOR | Pin to `ded46bc5…`; mint Zenodo DOIs for P1C + the three artifacts |
| DP1N-32 | Provenance language survives in the `.bib` (ref. [26], `TorsionOnshell2026`) and as in-text tags "READING-I" (`202`) and "(P1A [15])" (`559`) | GENUINELY-NEW-REAL (residual of DP1N-08) | MINOR | Rewrite both `note` fields; drop the two tags |
| DP1N-33 | "≳58 orders relative to the observed birefringence amplitude" misdescribes Eq. (8)'s own normalization (`β_obs` **and** `M_Pl(α/M)`); Eq. (8) carries a common factor on both sides | GENUINELY-NEW-REAL (Claude MINOR 6 = Gemini P1N-N5) | MINOR | Say which ratio the count refers to; cancel the common factor |
| DP1N-34 | Eq. (8) "anchored in" Shapiro–Teixeira, but that result is never stated | GENUINELY-NEW-REAL | MINOR | One or two sentences quoting it |
| DP1N-35 | One sentence both asserts "signature-independent" and disclaims the signature bridge (`223–231`) | GENUINELY-NEW-REAL (refines DP1N-04) | MINOR | Show the `ρ+3p<0` line or end at the disclaimer |
| DP1N-36 | `[R1]`–`[R4]` used on p. 4 before Routes 1–4 are defined on p. 5 | GENUINELY-NEW-REAL (Claude MINOR 9 = Grok N1) | MINOR | One-line R1–R4 definition at the head of Sec. IV |
| DP1N-37 | Abstract 435 words (CQG ≈300) | GENUINELY-NEW-REAL | MINOR | Cut to ~250–300; lead with the structural dichotomy |
| DP1N-38 | Sole Tier-I result runs as prose with an italic "*Proof.*"; hypotheses unenumerated | GENUINELY-NEW-REAL (content re-checked **correct**) | MINOR | `Theorem` environment, (H1)–(H5), excluded cases |
| DP1N-39 | No novelty-positioning sentence vs the standard Holst statement; Holst (1996) absent from the bibliography | GENUINELY-NEW-REAL (the "standard result" half re-flags R1 Gemini N1) | MINOR | One sentence + add Holst 1996 |
| DP1N-40 | `\paperVersion` defined and never used (`main.tex:51`) | GENUINELY-NEW-REAL (residual of DP1N-08) | MINOR | Delete the dead macro |
| DP1N-41 | γ = 0.2375 load-bearing from the abstract but first cited only inside B12 on p. 5 | GENUINELY-NEW-REAL (Grok E1 — real, **severity mislabeled** ESSENTIAL→MINOR; the value *is* sourced in-paper) | MINOR | Cite `Ashtekar2011` at first use |
| DP1N-42 | Eq. (9)'s integration does not state the `G`/`M_Pl` normalization (an `8π` trap, cf. DP1N-21) | GENUINELY-NEW-REAL (Gemini P1N-N4) | MINOR | State `G = 1/M_Pl²`, `M_Pl = 1.22×10^19` GeV |
| DP1N-43 | Abstract `1/(2γ) -- 2.11` en-dash reads as a minus | GENUINELY-NEW-REAL (Gemini P1N-N3) | NIT | ", which evaluates to" |

### R2 additions to "Falsified — do not re-litigate"

| Finding | Leg | Settled evidence |
|---|---|---|
| "The `3.884e-69` coefficient is an uncomputed arithmetic step" (M2) | Grok | Full chain displayed at `main.tex:256–266`; independently reproduced (`3.885e-69`), including the `(2.29/2.25)⁴` cross-check. |
| "Dated September 2, 2026 — a future date" (M3) | Grok | Auto-FALSIFY **Rule 3**; identical claim already falsified at R1 (Grok N1). |
| "Duplicated phrasing ('the the', 'finite finite'); 'programme'/'program' alternate" (N2) | Grok | Perl doubled-word scan over `main.tex`: **zero** hits. `programme` 7×, bare `program` **0×**. Confabulated text. |
| "No frozen release hash; commit hashes pre-date the submission version" (E3) | Grok | `\repoSHA = ded46bc5…` printed at `main.tex:950`, all 8 `\artifactbase` targets resolve at it; immutable Zenodo deposit `doi:10.5281/zenodo.21481838` at `main.tex:975`. A pinned commit necessarily predates what it pins. Real remainder = DP1N-31. |
| "The transparency theorem's proof is deferred to the companion" (E2, first half) | Grok | Statement + `*Proof.*` in-paper at `main.tex:312–357`; key step re-checked correct. Real remainder (NJL) = DP1N-28. |
| "`O5` is parity-odd off shell; the 'off shell' qualifier is an introduced error" (MINOR 1 premise) | Claude | `O5` is parity-**even** off shell too. The sentence is defective for a different reason — carried as DP1N-23. |

### R2 additions to "Re-flag of disclosed" / "Opinion–genre"

- Grok M1 ("five barriers are only naturalness arguments") — the paper concedes exactly this at
  the head of Sec. IV; the non-disclosed remainder is DP1N-24.
- Gemini N2 (superseded draft carries load-bearing detail) — same substance as DP1N-24/31/32.
- Grok's **REJECT** dispatch word against a body whose surviving findings are one inherited
  coefficient error plus sourcing items — skill **Rule 6** (judge by the written findings).
  Two of three ESSENTIALs FALSIFIED, the third MINOR. Referee variance (pattern-066).
- Claude PART C's 13.5–14.5 pp recommendation — scope guidance under DP1N-20, not a finding.

### R2 budget note (directive R2)

Second consecutive review round with no intervening science or scope decision — the cap.
**A third board requires an intervening decision first.** Three are available and are
recorded as decisions, not findings: **DP1N-21** (the 8π correction — changes a printed
coefficient in two papers and inverts a stated size ordering), **DP1N-22** (the O1≡O6
restatement — changes what the operator enumeration claims), and **DP1N-25** (whether the
Note engages Popławski's Λ or narrows its channel claim). Take those, close the ledger,
then R3 is permitted. A board run before them would return the same findings: remaining
verdict movement on P1N is gated by content additions, not by more referee passes.

---

## R3 board — `ROUND_2026-09-02-P1N-v1N.0.3-EXACTPDF-c758664b-R3VERIFY` (verification round)

**Exact PDF sha256:** `c758664b4485a45752cd79e2ab695c6b09d9f82f2b283dd8db5a2af6721f7027` (re-verified, 11 pp).
**Legs:** Claude INT `major-revisions` (5 MAJOR / 9 MINOR), Grok API `REJECT` (6 ESSENTIAL / 3 MAJOR / 2 MINOR),
Gemini API `MAJOR REVISIONS` (3 ESSENTIAL / 2 MAJOR / 2 NIT), **Perplexity ABSENT** (401 insufficient_quota — recorded absent, not clean).
**BLOCKERs: 0** across all legs. Round not degraded. Completeness table: 32/32 tagged items dispositioned, gap `no` on every leg.
**Audit:** `INT_v3/ROUND_2026-09-02-P1N-v1N.0.3-EXACTPDF-c758664b-R3VERIFY/P1N_v1N.0.3_R3_truth_audit.md`
**Round permitted under directive R2** by the three intervening science decisions taken at R2 closure (DP1N-21, DP1N-22, DP1N-25) — all three independently re-verified closed and correct this round.

32 leg findings audited → **7 REGRESSION-FROM-CLOSURE, 11 GENUINELY-NEW-REAL, 5 RE-FLAG-OF-DISCLOSED,
7 FALSIFIED, 2 OPINION/GENRE, 0 OUT-OF-SCOPE.** **15 canonical real items opened (DP1N-44 … DP1N-58)**
— 6 MAJOR, 8 MINOR, 1 archival; **12 SUBSTANTIVE / 3 GENRE-LENGTH-VENUE**; **6 are regressions introduced by the R2 closure**.
**No fabricated result found.** Clean-wave count for P1N: **0**.

### R2 closure record — independent verification

The four headline R2 science decisions are **genuinely and correctly closed**:
**DP1N-21** (the 8π correction) re-derived from scratch from the paper's own α, β, κ → `−24πκγ³/(1+γ²)²` exactly as printed, with `O4/O5 = 8πγ/(1+γ²) = 5.65031` at γ=0.2375 and the ordering propagated completely;
**DP1N-22** (five distinct densities, rank 4, O6 retained) restored in full and propagated to abstract + Conclusions;
**DP1N-23** (O5 P-even off *and* on shell, ε-construction-rule-admitted) correct in the operative statement;
**DP1N-25** (Popławski's Λ mapped to Route 1 and closed on amplitude + sign) closed at correct evidential strength.
Also closed: DP1N-26, 31, 34, 36, 38, 39, 41, 43.
**Recorded closed in SSOT but NOT closed: DP1N-29** (Table I caption still "the Barbero–Immirzi symbol κ") **and DP1N-37** (abstract 444 words, SSOT records "~380"). The SSOT closure record for this paper requires line-level re-verification rather than trust.

### Open items (R3 board) — ★ = regression introduced by the R2 closure

| ID | Issue | Verdict | Sev | Class | Closure instruction |
|---|---|---|---|---|---|
| **DP1N-44** ★ | ρ+3p repulsion chain (`main.tex:225–236`): paper prints `ρ+3p = −2L` (its own `ρ=−L`, `p=+L` give `+2L`) and concludes `L>0` (a negative coefficient × positive `(J⁵·J⁵)` gives `L<0`). Recomputed κ=1: `L=−0.010011`, `ρ+3p=−0.020023<0` — conclusion correct, **every displayed step wrong**. Added by the DP1N-35 closure | REGRESSION-FROM-CLOSURE | MAJOR | SUBSTANTIVE | Rewrite three lines: `ρ+3p=2L`, requirement `L<0`, Eq. (3) supplies it |
| **DP1N-45** ★ | Eq. (11) (`729–733`) gives `1.4e−6 × 3.9e−69 = 5.46e−75` = **74.26 orders**, outside the retained `61–67` window (`743–754`, `1032–1034`) — which reproduces **exactly** from P1C's *different* relation `(Δγ/γ)(H₀/M_Pl)`, `H₀/M_Pl=1.18e−61` (`paper1c/main.tex:1563–1583`): `3.54e−62`→**61.45**, `1.652e−67`→**66.78**. `μ_UV→M_Pl` reaches only 68.41. Compounded by the DP1N-30 deletion of the chiral-count input that generates the 61 endpoint | REGRESSION-FROM-CLOSURE | MAJOR | SUBSTANTIVE — **scope decision** | **Decision:** restore P1C's `H₀/M_Pl` relation (keeps 61–67), or keep Eq. (11) and re-quote ≈68–74 everywhere. Not both |
| **DP1N-46** ★ | Directive-Q1 leaks printed in the PDF: "(SSOT)" erratum notice (`948–950`), "~4.5×" reference to a superseded draft (`953–954`), "This manuscript is internally tracked as v1N.0.3" (`1104`, **created by the DP1N-40 closure**), "(P1A)" tag (`627`). Claude MAJOR 3 = Gemini E1 + E2 | GENUINELY-NEW-REAL | MAJOR | GENRE (Q1 hard gate) | State Eq. (15) as the result; delete the comparison, `(SSOT)`, the version sentence (delete the macro instead of using it), the P1A tag |
| **DP1N-47** | B2 attaches `BlagojevicHehl2013`+`BoehmerBurnett2008` to a biconditional neither states; B5/B6/B10 each attach `Weinberg1989`, which contains nothing on the bounce density, the `N_tot≈92–94` transfer, or a UV→IR bridge — while the abstract (`92`) now asserts the barriers are "literature-sourced". B1/B3/B4/B11/B12/B13 *are* fairly supported. Residual of DP1N-24 | GENUINELY-NEW-REAL | MAJOR | SUBSTANTIVE — **scope decision** | **Decision:** supply the 2–4-line derivations for B2/B5/B6/B10, or downgrade the abstract wording and demote them out of the headline count |
| **DP1N-48** ★ | `main.tex:720–722` calls `M_Pl=1.22×10¹⁹ GeV` the "reduced-Planck-mass convention"; reduced = `1.22e19/√(8π) = 2.4335e18 GeV`. Numerics correct, label wrong — in the one sentence the DP1N-42 closure added to prevent an 8π ambiguity | REGRESSION-FROM-CLOSURE | MAJOR | SUBSTANTIVE | Delete "reduced-" |
| **DP1N-49** | Signature-independence (`225–236`) rests on an unjustified parenthetical "spacelike-normalized `J⁵`" premise that fixes the sign of `(J⁵·J⁵)`; a spin-aligned axial current is naturally timelike. Refines DP1N-04/DP1N-35 | GENUINELY-NEW-REAL | MAJOR | SUBSTANTIVE | Justify the premise for the configurations of interest, or drop the signature-independence claim |
| **DP1N-50** | Table I caption (`486`) still calls κ "the Barbero–Immirzi symbol" — **DP1N-29 not closed** | GENUINELY-NEW-REAL | MINOR | SUBSTANTIVE | "…the gravitational coupling κ" |
| **DP1N-51** | Residual "parity-odd" language at `850`, `852`, `909`, and the section's own summary at `978–979`, contradicting the mixed-parity statement established at `936`. Residual of DP1N-23 | GENUINELY-NEW-REAL | MINOR | SUBSTANTIVE | Use "ε-contracted"/"construction-rule-admitted" uniformly |
| **DP1N-52** ★ | Discussion `1032–1033` restates "≥58 orders of margin against the observed birefringence amplitude" — the exact misdescription DP1N-33 removed at `692–695`. Incomplete propagation | REGRESSION-FROM-CLOSURE | MINOR | SUBSTANTIVE | Fix the Discussion sentence to match `692–695` |
| **DP1N-53** ★ | Table II R3 row (`798–800`) credits a "mass-dimension lock" occurring exactly once in the manuscript; the argument is P1C's `H₀/M_Pl` dimension count (`paper1c/main.tex:1555–1560`), absent from the Note. Same defect class as the "chiral-count bound" removed under DP1N-30, recurring in the same table | REGRESSION-FROM-CLOSURE | MINOR | SUBSTANTIVE | Import the argument or rename the row's basis; resolves with DP1N-45 |
| **DP1N-54** | Gap-equation loop-integral prefactor `N_cN_f/(4π²)` (`313–317`) printed without derivation or citation; only `I>0` is load-bearing and the three-line argument is verified sound. Residual of DP1N-28 | GENUINELY-NEW-REAL | MINOR | SUBSTANTIVE | Derive/cite, or write `I ∝ ∫₀^Λ p²dp/√(p²+M²) > 0` and use positivity only |
| **DP1N-55** | `954–956`: "vanishes only in the γ→∞ limit" — `O4 ∝ γ³/(1+γ²)²` vanishes as γ→0 as well | GENUINELY-NEW-REAL | MINOR | SUBSTANTIVE | "…(and, degenerately, as γ→0)" |
| **DP1N-56** | `938–941`: "supported only by the **non-axial** torsion irreps … carried entirely by the **axial×trace-vector** cross term" — the cross term requires the axial irrep. Intended statement (needs both, vanishes on either alone) is correct | GENUINELY-NEW-REAL | MINOR | SUBSTANTIVE | Repair the "non-axial" clause |
| **DP1N-57** | Abstract measured at **444 words** (Claude leg: 433) vs CQG ≈300; SSOT records "435 → ~380". **DP1N-37 not closed** | GENUINELY-NEW-REAL | MINOR | **GENRE/LENGTH** | Cut to ~250–300; lead with the structural dichotomy |
| **DP1N-58** | Archival residual of DP1N-06/DP1N-31: P1C v1C.0.16 and the three theory-audit `.md` artifacts are commit-SHA-pinned only, no DOI (`Golden2026P1a` already carries Zenodo `10.5281/zenodo.21481838`). Gemini E3+M1+M2, Grok E1 | RE-FLAG-OF-DISCLOSED with real archival residual | MINOR | **VENUE/ARCHIVAL** | Mint Zenodo version DOIs for P1C + the three artifacts; cite the DOIs |

### R3 additions to "Falsified — do not re-litigate"

| Finding | Leg | Settled evidence |
|---|---|---|
| "Typo: 'brauch' for 'branch' (Sec. VI, p. 8)" (N1) | Gemini | `grep -n "brauch" main.tex` → **0 hits**; `main.tex:906` reads "ECH branch". PDF text-extraction mangling (skill **Rule 7**). |
| "Abstract quotes β/α = 2.11 with no finite-γ caveat — abstract–body drift" (E2) | Grok | `main.tex:108–109` reads "…evaluates to **2.11 at the programme's benchmark γ=0.2375** (Ref. [Ashtekar2011])". The benchmark and its citation are in the abstract itself. Premise false. |
| "The two operator relations are on-shell statements sold as an off-shell basis result" (E5) | Grok | `main.tex:~884`: "both relations hold identically **off shell and on shell**"; the first follows from the metric-compatible tetrad conversion (off-shell). Section is titled "Rank, **Not** Basis" and states the list is "*not* a linearly independent basis". |
| "Abstract's 'no ECH dark-energy or birefringence prediction is made' overstates the body, since R2/R3 are nonzero" (E6) | Grok | A claim-policy statement (the paper declines to *predict*), not an assertion that the contributions vanish; the body quantifies them as suppressed and says so. Consistent. |
| "`κn_ψ²/ρ_Λ ≃ 3.884e−69` is taken from the companion; neither `n_ψ=100 cm⁻³` nor the conversion is in-paper" (M2) | Grok | `main.tex:267` prints `M_Pl=1.22089e28 eV` **and** `n_ψ=100 cm⁻³`; `273` prints the result with its explicit `(n_ψ/100 cm⁻³)²` scaling; `737`, `828` repeat it. Independently recomputed → `3.884e−69`. Chain fully in-paper. |
| "'(Dated: September 2, 2026)' is an internal bookkeeping tag; remove" (N1) | Grok | `date` = 2026-09-02 — current, not future. Standard revtex front matter; the `\paperVersion`-in-`\date` defect closed at DP1N-08. **Third consecutive round**; auto-FALSIFY **Rule 3**. |
| "Self-citations carry future DOIs / non-peer-reviewed disclaimers" (N2) | Grok | Zenodo `10.5281/zenodo.21481838` deposited 2026-07-22 — past. Grok's own text concedes the entries are acceptable given the disclaimers. Self-withdrawn. |

### R3 additions to "Re-flag of disclosed" / "Opinion–genre"

- Grok E1 (all steps producing `−3κ/16` must be in main text) and Grok E4 (13 of 14 barriers are naturalness/single-branch) — both conceded in-paper (Sec. IV head; abstract tiering); real remainders are **DP1N-58** and **DP1N-47** respectively.
- Grok E3 (Theorem 1 conditional on H1–H5 ⇒ circular) — the claim policy is channel-level closure of **minimal-coupling** ECH routes; H1–H5 and the excluded-cases list (`351–367`, added under DP1N-38) state the scope openly. A theorem scoped to minimal ECH is not circular for not covering non-minimal ECH.
- Grok M1 (11 pp too long; 4–5 pp Letter) — directly opposes the R2 Claude leg's 13.5–14.5 pp Paper recommendation on unchanged content: pattern-066 referee variance on form, already settled by DP1N-20's adopted CQG-Paper decision.
- Grok M3 (no γ scan behind "trace-vector is larger") — the claim is analytic (`β/α = 1/(2γ)`, monotone); a scan would be presentational. Optional one clause noting `β/α>1` for all `γ<0.5`.
- Grok's **REJECT** dispatch word against a body whose surviving items are two sourcing/scope objections — skill **Rule 6**; four of its six ESSENTIALs FALSIFIED.

### R3 process finding (the one that most wants recording)

The R2 closure converted six "assert it" items into "display the derivation" items. **Three of the newly displayed derivations are wrong** (the sign chain DP1N-44, the substituted scaling relation DP1N-45, the convention label DP1N-48), two closures propagated incompletely (DP1N-52, DP1N-53), one closure *created* a directive-Q1 violation (DP1N-46 via DP1N-40), and two items were recorded closed in SSOT without being closed (DP1N-50, DP1N-57). **The remedy is arithmetic and grep verification of every newly displayed step and every SSOT closure claim before the next bump — not another review board.** Extend `research/theory_audit/p1n_r2_checks_2026_09_02.py` with assertions for the sign chain, the Eq. (11) order count, and the 61.45/66.78 endpoints so this class cannot recur silently.

### R3 convergence statement (directive R2)

**This round did not bottom out in genre/length/venue** — 12 of 15 canonical items are substantive and 6 are regressions the R2 closure introduced, so the round was productive rather than variance-driven and the convergence budget was correctly spent.

**After v1N.0.4 closes DP1N-44 … DP1N-58 — including taking both PART 4 decisions in that same version rather than deferring them — rounds stop.** What would remain is only: abstract length and the 11 pp-vs-Letter disagreement (opposing recommendations on unchanged content — pattern-066, settled by DP1N-20); Zenodo DOIs (packaging, closed by minting); and the standalone-reader objection, disclosed openly every round and structurally bounded by the companion architecture — a venue judgment, not a defect.

**No science decision would be outstanding after v1N.0.4.** The physics — Cartan elimination, the contact term, the transparency theorem, the operator rank/count, the Popławski mapping — is verified sound and correctly scoped at v1N.0.3; every remaining defect is in a displayed step, a label, or a cross-reference.

**Condition on stopping:** v1N.0.4 must ship machine-checkable assertions for the three regressed derivations and a line-level re-verification of every SSOT-recorded closure. Absent that, the closure record is not trustworthy enough to declare convergence on — and this round is the demonstration.
