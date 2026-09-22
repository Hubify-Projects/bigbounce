# PRE-REGISTRATION — the P1N Fierz-row scalar sign and the sign of `G_s`

**Lane** `bb-LS15-fierz-sign` · opened 2026-09-22 03:50 PDT
**Committed BEFORE any symbolic or numerical result is produced.**
**Repo state at pre-registration** `git rev-parse HEAD` = `27dd3143`
**Target (read-only)** `arxiv/paper1bc_ech_note/main.tex` @ `v1N.0.7`,
Eq. `eq:fierz_row` (l. 273–288) and Eq. `eq:Gs` (l. 289–296).

---

## 1. Why this lane exists

Lane `bb-LS13-p1n-essentials` closed DP1N-60 by derivation: the contact term's
equation of state is `w=+1` not `w=-1`, the repulsion-sign condition inverts,
and with the manuscript's own configuration the term is gravitationally
attractive (Kerlick 1975 / O'Connell 1977). That lane explicitly **flagged but
did not check** an adjacent sign — the scalar-channel coefficient of
`eq:fierz_row`, which is what makes `G_s < 0` and hence drives the NJL
no-condensate result — and recorded it as needing its own lane
(`research/ech_contact_term_2026_09_22/MANIFEST.md`, "Known limits" #2;
`PROPAGATION_NOTE.md` §6; `DERIVATION.md` §1.7 scope boundary).

One sign error has already been confirmed in the same section of the same
paper, and that lane's own first reading of §II was corrected by a blind
adjudicator. An unchecked sign in the adjacent equation must not be assumed
correct.

## 2. The claim under test (quoted from the manuscript)

`main.tex:276-281` —

```
(J_5^I J_{5I})  ->  (psibar psi)^2 + 1/2 (psibar gamma^mu psi)^2
                     + 1/2 (psibar gamma^mu gamma^5 psi)^2 - (psibar gamma^5 psi)^2
```

`main.tex:282-288` — "the scalar-channel coefficient is exactly `+1`, unique,
and signature-independent, with the single Grassmann exchange that maps the
ordering `(12)(34) -> (14)(32)` supplying the overall minus sign relative to the
c-number Nieves--Pal identity for the same index structure."

`main.tex:289-293` — inserting the scalar row into the declared interaction
`+G_s (psibar psi)^2` gives `G_s = -(3 kappa/16) gamma^2/(1+gamma^2) < 0`,
"repulsive", which is the sole input to the `eq:gap` three-line no-condensate
argument.

## 3. Pre-registered method (fixed before any result)

1. **State the manuscript's declared conventions and CHECK the paper actually
   uses them**: mostly-plus `eta = diag(-,+,+,+)` (`main.tex:167-168`),
   `eps_0123 = +1`, `kappa = 8 pi G`, the spin-aligned Dirac ensemble /
   spacelike `J^5` configuration (`main.tex:216-221`), and the sign convention
   of `gamma^5` and `psibar`. Any convention the paper states but does not use
   is itself a finding.
2. **Build the Fierz machinery from scratch**, numerically, from explicit
   4x4 Dirac matrices — no remembered coefficient table:
   * construct `gamma^mu` in BOTH signatures (mostly-plus and mostly-minus) in
     at least two representations (Dirac and Weyl), verify the Clifford algebra
     `{gamma^mu, gamma^nu} = 2 eta^{mu nu}` and `(gamma^5)^2 = 1` numerically;
   * form the five channel tensors `L^(X)_{abcd} = sum_idx (Gamma_X)_{ab}
     (Gamma^X)_{cd}` for X in {S, V, T, A, P} with the index contraction carried
     by `eta`;
   * form the AA tensor, apply the Fierz index exchange `b <-> d`, and solve the
     resulting 256-component linear system for the decomposition coefficients in
     the five-channel basis (exact rational / least-squares with a residual
     check, NOT a fit).
3. **Apply the Grassmann sign separately and explicitly**: derive the sign of
   the reordering `psibar_a psi_b psibar_c psi_d -> psibar_a psi_d psibar_c psi_b`
   from the anticommutation of four odd objects, and state it as its own step so
   the c-number row and the Grassmann row are both reported.
4. **Validate the machinery against a published answer BEFORE trusting it here.**
   Pre-declared validation set, all of which must pass or the machinery is
   rejected:
   * the full 5x5 c-number Fierz matrix must be reproduced and must satisfy
     `F^2 = 1` (the Fierz transform is an involution) — a self-consistency test
     the machinery cannot pass by accident;
   * the standard `V-A` identity `(psibar gamma^mu (1-gamma^5) psi)
     (psibar gamma_mu (1-gamma^5) psi)` must Fierz onto itself (the textbook
     Fierz self-conjugacy of the charged-current operator);
   * the Kerlick (PRD 12, 3004, 1975) / O'Connell (PRD 16, 1247, 1977)
     Dirac-field ECSK contact result used by the LS13 blind adjudicator must be
     reproduced from the same machinery;
   * Poplawski arXiv:1005.0893's vacuum-saturation chain (his Eqs. 9-10,
     `rho_Lambda = (kappa/3) <qbar q>^2 > 0`) must come out sign-consistent with
     whatever row this lane derives.
5. **Answer the three questions**: (a) is the printed scalar sign correct?
   (b) what does `G_s` become under the correct sign? (c) which claims in the
   paper depend on `G_s` — enumerated BY LINE NUMBER against the pinned
   `v1N.0.7` text.
6. **One blind adjudicator sub-agent** (`fable` first; on HTTP 429 record
   FAILED-INFRA, never a verdict, and substitute `opus` with the label changed),
   told neither this lane's conclusion nor its method, and explicitly permitted
   to answer "undecidable".

## 4. Pre-registered outcome branches

Declared now so that neither outcome can be reverse-engineered later.

* **Branch A — sign as printed is CORRECT (`+1`).** Then `G_s < 0` stands, the
  `eq:gap` no-condensate argument stands, and §VII.D's `G_s`-sign leg is sound
  *as an internal statement* (it remains true, per LS13, that it does not rebut
  Poplawski, whose condensate is QCD-generated). Report plainly that the row is
  right, and record that P1N's remaining sign structure in §II.B is then
  verified — which is itself worth recording after DP1N-60.
  Readiness recommendation: **no further drop from 85** on this item.
* **Branch B — sign as printed is WRONG (`-1`).** Then
  `G_s = +(3 kappa/16) gamma^2/(1+gamma^2) > 0`, attractive; `eq:gap`'s step (2)
  ("the right-hand side is negative for `G_s<0`") fails, a nonzero `M` solution
  can exist, and the "this specific truncation admits no condensate" claim must
  be WITHDRAWN along with every downstream use. Report exactly what survives
  (the operator identification, the `alpha`/`beta` normalization, the
  transparency theorem) and what must be withdrawn.
  Readiness recommendation: a **further drop below 85**, quantified in the
  propagation note.
* **Branch C — UNDECIDABLE at this lane's resolution** (e.g. the coefficient is
  convention-dependent in a way the manuscript's declared conventions do not
  fix). Then the finding is that the manuscript's "unique and
  signature-independent" qualifier is unsupported, and the required closure is a
  convention-fixing sentence, not a sign flip. Report as such; do not
  manufacture a sign.

**What would invalidate this lane's own result:** failure of ANY item in the
§3.4 validation set, or a disagreement between the two signatures / two
representations that is not traced to a stated convention.

## 5. Scope boundaries (hard)

* This lane does **NOT** edit `main.tex`, `project-context/SSOT/`,
  `DISPOSITIONS/`, or `site/src/data/` — P1N is concurrently owned by lane
  `bb-L3d-p1n-withdrawals` landing `v1N.0.8`. Line numbers are pinned to
  `v1N.0.7` at commit `27dd3143` and will be reported as such.
* Output is confined to `research/fierz_row_sign_2026_09_22/`.
* This lane does not re-open DP1N-60 or DP1N-61; it checks one adjacent sign.
* `/never-fabricate-derivation` applies absolutely: a claim this lane cannot
  derive is not printed, and WITHDRAWAL is an acceptable outcome.

## 6. Reproducibility (directive Q2)

Compute venue: local workstation, CPU only, no GPU/RunPod, ~$0, deterministic
(exact rational arithmetic where possible; no RNG). Manifest at
`MANIFEST.md` on completion.
