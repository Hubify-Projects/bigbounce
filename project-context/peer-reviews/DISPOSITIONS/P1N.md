# P1N disposition ledger

**Canonical source:** `arxiv/paper1bc_ech_note/main.tex`
**Current paper-local version:** `v1N.0.1` (2026-09-02; merge of P1A v1A.0.127 + P1C v1C.0.16 per `project-context/PORTFOLIO_DECISION_2026-09-02.md` Sec. 3 Track B)
**Claim policy:** channel-level closure of minimal-coupling ECH dark-energy routes only; **no** operator-level completeness theorem, no unrestricted no-go, no ECH dark-energy or birefringence prediction.
**Venue:** CQG — form is **Paper**, not Note (4144 words vs the ≤2500-word Note ceiling, `project-context/SESSION_HANDOFF_2026-09-02.md:32`).

## Round history

| Round | Exact PDF sha256 | Legs | Outcome |
|---|---|---|---|
| `ROUND_2026-09-02-P1N-v1N.0.1-EXACTPDF-2287537b-R1` | `2287537b1cf2420b2aa043b6d07da1281fb2844a82e296e7658467c7362747ba` | Claude INT (major-revisions), Grok API (REJECT), Gemini API (REJECT), **Perplexity ABSENT (401)** | 42 rows audited → 3 REGRESSION, 29 GENUINELY-NEW-REAL (16 distinct), 3 RE-FLAG-OF-DISCLOSED, 3 FALSIFIED, 4 OPINION/GENRE. **19 canonical real items open.** Clean-wave count **0**. Audit: `INT_v3/ROUND_2026-09-02-P1N-v1N.0.1-EXACTPDF-2287537b-R1/P1N_v1N.0.1_R1_truth_audit.md` |

## Open items (R1 board)

| ID | Issue | Status | Evidence / residual scope |
|---|---|---|---|
| DP1N-01 | Sec. VI asserts (O1, O6) vanish by the torsion-free Bianchi identity **on the on-shell ECH branch**; the ECH-branch statement is `O1 = O6 = −O2 + ½O4`. | **OPEN — REGRESSION** | Correct text exists verbatim in **P1C v1C.0.16 `main.tex:2087–2098`** (closed under R13). Artifact: `ech_torsion_onshell_2026_08_08.md` §6 `[L48]`–`[L50]`; ERRATUM ADDENDUM to `operator_basis_adjudication_2026_08_07.md`. Self-contradictory with the Note's own `O1 = ½O4 − O2` + `O4 ≠ 0`, 12 lines above. No physics change on fix. |
| DP1N-02 | `O5^{[4]} = −(3/2)κ(J⁵·J⁵)` (READING-II, γ→∞) printed alongside Eq. (2) in READING-I; two normalizations, no normalization statement. | **OPEN — REGRESSION** | **P1C v1C.0.16 `main.tex:351–358`** — "CONVENTION FIXED … ONE normalization throughout — Eq. (E2)'s … O5 reduces to −3 kappa [gamma^2/(1+gamma^2)] (J5.J5)". Artifact §5 `[L27]`–`[L30]`, §6 `[L33]`/`[L39]`. |
| DP1N-03 | Operator-completeness argument drops the R13-M3 closure: `O5` is parity-**even** off shell, and the ε-free parity-odd density `T^a{}_{ab}J^{5b}` is unenumerated. | **OPEN — REGRESSION** | R13 truth audit row M3 (GENUINELY-NEW-REAL, **CLOSED v1C.0.16 by scoping**). Restore **P1C `main.tex:2106–2108`**, **`2132–2136`** (`T^a{}_{ab}J^{5b} = 3β(J⁵·J⁵)`, `β = κγ/[4(1+γ²)]`), **`2231–2237`**. The added density lands in the same Fierz-closed class — it *strengthens* the disposal statement. |
| DP1N-04 | Popławski identification ("identical", "the same contact term", "the same sign", "algebraically identical") stated above evidential strength; exact only as γ→∞; no signature bridge; bounce asserted by citation. | **OPEN** | `ech_torsion_onshell_2026_08_08.md` `[L17]`, `[L20]`, `[L23]`: γ²/(1+γ²) = 0.053 and β/α = 2.11 at γ = 0.2375 — the non-Popławski trace-vector piece is the larger. Replacement sentence drafted in the R1 audit, closure plan (2). |
| DP1N-05 | Hehl–Datta attribution missing for Eq. (2); `HehlDattaNJL1971` and `Hehl1976` defined-but-uncited in the Note's own `.bib`; 18-reference list thin for the topic. | **OPEN** | Key-set diff: 18 cited / 113 defined; `grep -i hehl` over the cited set empty. Add Kibble/Sciama, a torsion-cosmology reference, and the Shapiro torsion review. |
| DP1N-06 | Standalone evaluability: B1–B14 and the Route-2/3 budgets are asserted, not derived; sole sources are mutable `tree/main` / `blob/main` URLs and a self-declared non-refereed, never-to-be-submitted companion; the sole Tier-I result defers its own proof to a non-peer-reviewed deposit. | **OPEN — carried from R13 MINOR-6 + the refereed-companion-gate checklist item; materially worsened by the merge** | P1C at ~25 pp carried its own derivations (deferrals supplementary); the Note at 6 pp carries none (deferrals load-bearing). Fix: Zenodo version DOIs for P1C v1C.0.16 and both theory-audit artifacts; commit-SHA pin in `\artifact` (`main.tex:50`); barrier/route arithmetic in-paper. Flagged by all three legs. |
| DP1N-07 | O1–O6 are never defined mathematically anywhere in the Note, yet their relations and rank are load-bearing. | **OPEN** | Verified in `main.tex` and on the 300-DPI render of p. 4. Restore the explicit densities from P1C Sec. V / Table III. |
| DP1N-08 | Version-history / internal-audit / provenance language throughout ("supersedes", "earlier catalog draft", "theory-audit record", "merges two companion papers"), plus `\paperVersion` printed in `\date`. | **OPEN — directive Q1** | Sites: `main.tex:51–52`, `63`, `74–75`, `142–145`, `204–208`, `481–483`, `563–566`. Grok M1 / Gemini E1. Published work presents the science in pure form; the merge/erratum history stays in this ledger and the audit trail. |
| DP1N-09 | Eq. (4) `G_s = −3κ/16` drops the `γ²/(1+γ²)` of Eq. (2) with no stated limit. | **OPEN** | Confirmed on the 300-DPI render of p. 2. Sign — hence the no-condensate conclusion — is γ-independent, so no result moves. Fix by printing the γ factor or stating the γ→∞ limit, plus P1A's declared-interaction clause (`paper1a_ech_nogo.tex:1786–1789`). |
| DP1N-10 | Printed `α ∝ γ²/(γ²+1)`, `β ∝ γ/(γ²+1)` divide to `1/γ`, not the stated (correct) `1/(2γ)`. | **OPEN** | Value correct per `[L20]` (`α_E2 = −4πGγ²/(1+γ²)`, `β_E2 = −2πGγ/(1+γ²)`); the printed derivation is not. Raised independently by Claude and Grok. |
| DP1N-11 | Holst sign convention `s_H` never fixed, though `β/α = s_H/(2γ)`. | **OPEN** | Artifact `[L10]`,`[L13]`,`[L46]`,`[L47]` (both conventions computed). One clause. |
| DP1N-12 | Size of the finite-γ correction understated: trace-vector coefficient is 2.11× the axial one at γ = 0.2375 (1.82× at γ = 0.274). | **OPEN** | `[L23]`, `[L24]`. |
| DP1N-13 | `3.6×10^{-69}` corresponds to `ρ_Λ = (2.29 meV)⁴`, not the Note's printed `(2.25 meV)⁴` (independently recomputed: 3.884e-69 vs 3.620e-69). | **OPEN** | Known P1C flag (`main.tex:95`). Use one `ρ_Λ` value. 8%; does not move "≈68 orders". |
| DP1N-14 | `ρ_crit` undefined and colliding with the cosmological critical density; the LQG window was lost in the merge. | **OPEN** | Restore `ρ_crit ≃ 0.27–0.41 ρ_Pl` from **P1A v1A.0.127 `main.tex:1527–1529`** (`0.27² = 0.073`, `0.41² = 0.168` — the printed endpoints), or rename to `ρ_bounce`. |
| DP1N-15 | Table I "Src." column (`A…N/O`, skipping I and K) has no legend anywhere in the Note. | **OPEN** | One caption clause, or drop the column. |
| DP1N-16 | "closed operator-level" for Route 2's dark-energy leg contradicts the Note's own Table II `(II)` and P1C's Tier-II record. | **OPEN** | Restate as "closed at the operator level modulo the spanning assertion (Tier-II)". |
| DP1N-17 | `\artifact{}` renders three identical "repository artifact" strings with no filename visible, floated away from the introducing sentence. | **OPEN** | `main.tex:50`, `554–558`; verified on the 300-DPI render of p. 5. Print filenames as link text; un-float. Mislabeled by Grok N2 ("production artifacts, delete") and Gemini E6 ("uncompiled placeholders") — the links are live; do **not** delete them. |
| DP1N-18 | `references.bib` ships ~95 unused entries (18 cited / 113 defined). | **OPEN** | Prune for the arXiv/CQG tarball; ship the `.bbl`. |
| DP1N-19 | `β_obs = 0.342° ± 0.094°` and ACT DR6 quoted without their ≈3.6σ / 2.9σ significances and the "indications rather than established detections" caveat. | **OPEN** | Restore from P1C `main.tex:1642`. |
| DP1N-20 | Page budget / venue form: 6 pp cannot carry the claims made; the budget is the mechanism that produced DP1N-01/02/03/06/07. | **OPEN — DECISION** | **Option A (recommended):** grow to ~12–16 pp and submit as a CQG **Paper** — no Note word budget exists to protect, since 4144 words already exceeds the ≤2500-word Note ceiling. **Option B:** cut to Secs. II+III at 6 pp and submit P1C separately — coherent, but reverses the Track-B consolidation; Houston/portfolio decision, not a referee call. |

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
