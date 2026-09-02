# P1N — Claude Opus INT referee leg, round R3 (verification pass)

**Reviewer:** Claude INT leg (independent referee; CQG, article type **Paper**)
**Model:** `claude-opus`
**Manuscript:** `arxiv/paper1bc_ech_note/main.pdf` — v1N.0.3
**sha256:** `c758664b4485a45752cd79e2ab695c6b09d9f82f2b283dd8db5a2af6721f7027`
(recomputed with `shasum -a 256`; matches the round label)
**Pages:** 11 · 433,339 bytes · `pdftoppm` render at 300 DPI used for every
claim about printed content
**Source bound:** `arxiv/paper1bc_ech_note/main.tex` (1166 lines), `references.bib`
**Date:** 2026-09-02
**Stance:** independent, skeptical; no expected verdict was supplied to this leg.

Method: every assertion below is bound either to a `main.tex` line number, to a
300-DPI page render, or to an arithmetic recomputation printed inline. No finding
is asserted from memory of the R2 board.

---

## PART A — Verification of the 23 R2 canonical items (DP1N-21 … DP1N-43)

**Summary: 12 verified closed correctly · 9 closed with a residual defect ·
2 not closed.**

### A.1 The four headline items named in the work order

**DP1N-21 — the 8π correction. VERIFIED CLOSED, and independently re-derived.**
`main.tex:943–947` / PDF p. 8 Eq. (15) now prints
$\mathcal O_4^{[4]}=-24M_{\rm Pl}^2\alpha\beta(J^5\!\cdot\!J^5)
=-\frac{24\pi\kappa\gamma^3}{(1+\gamma^2)^2}(J^5\!\cdot\!J^5)
=-\frac{192\pi^2G\gamma^3}{(1+\gamma^2)^2}(J^5\!\cdot\!J^5)$.
Re-derived from scratch this round using only the paper's own
$\alpha=\kappa\gamma^2/[2(1+\gamma^2)]$, $\beta=\kappa\gamma/[4(1+\gamma^2)]$
(`main.tex:200–201`) and $\kappa=8\pi G=8\pi/M_{\rm Pl}^2$ (`main.tex:182`):
$\alpha\beta=\kappa^2\gamma^3/[8(1+\gamma^2)^2]$, so
$-24M_{\rm Pl}^2\alpha\beta=-3M_{\rm Pl}^2\kappa^2\gamma^3/(1+\gamma^2)^2$, and
$M_{\rm Pl}^2\kappa^2=8\pi\kappa$, giving $-24\pi\kappa\gamma^3/(1+\gamma^2)^2$
— **exactly as printed**. Dimensional check passes: one power of $G$, mass
dimension 4. The ordering is propagated correctly and completely: `main.tex:952`
prints $\mathcal O_4/\mathcal O_5=8\pi\gamma/(1+\gamma^2)\simeq5.65$
(recomputed at $\gamma=0.2375$: **5.65031**), and `main.tex:953–954` states
*"O4 is the larger of the two by a factor of $\sim$5.7"*. Grep confirms **no
surviving instance** of `0.22`, `-3\kappa\gamma^3`, or `192\pi^2 G^2` anywhere
in the source. The no-go conclusion is correctly stated as unaffected
(`main.tex:955–958`). This item is closed to a high standard.

**DP1N-22 — five distinct densities / rank 4. VERIFIED CLOSED.**
`main.tex:885–903` (PDF p. 8) restores P1C's clause in full and correctly: the
first null relation is identified as the tetrad conversion, *"$\mathcal O_1$ and
$\mathcal O_6$ … are the same density written twice"*, **"five distinct
densities"** in bold, rank four with one null direction being the duplication and
only $2\mathcal O_1+2\mathcal O_2-\mathcal O_4=0$ carrying independent content,
rank two modulo total derivatives, redundancy deliberate, O6 retained. Propagated
to the abstract (`main.tex:98–101`) and the Conclusions (`main.tex:1092–1095`).

**DP1N-23 — O5 parity. CLOSED WITH A RESIDUAL DEFECT (→ MINOR 3).**
`main.tex:930–936` now states O5 is parity-**even** *both off shell and on shell*,
admitted by the $\varepsilon$-**construction rule** rather than by being P-odd,
and calls the list *"a mixed-parity $\varepsilon$-contracted set, not a strictly
parity-odd one"*. Abstract line 99 agrees. The physics statement is now correct.
Residual: two later sentences still call the same objects parity-odd densities
— see MINOR 3.

**DP1N-25 — Popławski's dark-energy claim. VERIFIED CLOSED, at correct
evidential strength.** New subsection `\label{sec:poplawski_de}`,
`main.tex:817–844`. It states the mechanism (cosmic fermion spin density),
**maps it explicitly onto Route 1**, closes it with both the amplitude argument
($\kappa n_\psi^2/\rho_{\Lambda,\rm obs}\simeq3.9\times10^{-69}$; recomputed
independently: $\kappa n_\psi^2=9.957\times10^{-80}$ eV⁴ against
$\rho_\Lambda=2.5629\times10^{-11}$ eV⁴ → $3.884\times10^{-69}$, agreeing to
3 s.f.) and the repulsive-sign/gap-equation argument, and correctly notes the
actual cosmic baryon density $n_b\sim0.25$ m⁻³ *widens* the gap. The strength
claim — *"a direct, quantitative rebuttal … in his own proposed channel at his
own order of magnitude"* — is supported by what precedes it and is not
overstated. Well done.

### A.2 Remaining items — verification table

| ID | Status | Evidence |
|---|---|---|
| DP1N-24 | **residual defect** | Citations added to B1–B6, B8, B10, B11, B13 (`main.tex:513,525,534,543,552,560,604,615,644`). But several do not support the stated proposition — see **MAJOR 4** |
| DP1N-26 | closed | B7 restated as a fixed parameter, `Ashtekar2011`+`GhoshMitra2005` cited, cross-ref repointed (`main.tex:569–580`) |
| DP1N-27 | **residual defect** | Eq. (11) `route3_scaling` displayed (`main.tex:729–733`), but its output does not reconcile with the retained 61–67 window — see **MAJOR 2** |
| DP1N-28 | **residual defect** | Gap equation + 3-line argument present and logically sound (`main.tex:313–331`); the displayed prefactor is unsourced — see MINOR 6 |
| DP1N-29 | **NOT CLOSED** | `main.tex:486` still reads *"the Barbero–Immirzi symbol $\kappa$"*. The SSOT closure table records this as fixed to "gravitational coupling κ". It was not. See **MINOR 1** |
| DP1N-30 | closed, defect class recurred | "chiral-count bound" is gone (grep: 0 hits); Table II's R3 row now names a *"mass-dimension lock"* appearing nowhere else — see MINOR 5 |
| DP1N-31 | closed | `references.bib` grep: **0** `tree/main`/`blob/main` URLs, **4** `ded46bc5…` SHA pins |
| DP1N-32 | **residual defect** | `READING-I` gone (0 hits). But `main.tex:627` still carries the internal tag `(P1A~\cite{...})`, and the closure *introduced* new provenance text — see **MAJOR 3** |
| DP1N-33 | **residual defect** | Fixed at `main.tex:692–695`; contradicted at `main.tex:1032–1033` — see MINOR 4 |
| DP1N-34 | closed | Shapiro–Teixeira result stated explicitly (`main.tex:666–673`) |
| DP1N-35 | **residual defect** | $\rho+3p<0$ argument now displayed (`main.tex:225–236`) — **and it contains two sign errors**. See **MAJOR 1** |
| DP1N-36 | closed | R1–R4 defined at head of Sec. IV (`main.tex:449–454`) |
| DP1N-37 | **NOT CLOSED** | Abstract measured this round at **433 words** (LaTeX stripped). SSOT records "435 → ~380". It did not shrink; still ~1.4× the CQG guidance |
| DP1N-38 | closed | Numbered `theorem` env with H1–H5 and an explicit excluded-cases list (`main.tex:351–367`) |
| DP1N-39 | closed | `Holst1996` cited with a positioning sentence (`main.tex:340–347`) |
| DP1N-40 | **residual defect** | `\paperVersion` is now used — but it prints internal version tracking into the published paper (`main.tex:1104`). See **MAJOR 3** |
| DP1N-41 | closed | `Ashtekar2011` cited at first abstract use of γ=0.2375 (`main.tex:109`) |
| DP1N-42 | **residual defect** | $G=1/M_{\rm Pl}^2$, $M_{\rm Pl}=1.22\times10^{19}$ GeV stated (`main.tex:720–722`) — **with a wrong convention label**. See **MAJOR 5** |
| DP1N-43 | closed | `main.tex:108` now reads "which evaluates to $2.11$" (recomputed $1/(2\gamma)=2.1053$) |

**Compile hygiene (independent):** `main.log` — **0** undefined refs/citations;
**1** overfull hbox at 4.50 pt (under the >10 pt gate). Pages 8 and 9 rendered at
300 DPI and read: no column escape, both corrected equations legible.

---

## PART B — Fresh referee findings on v1N.0.3

Each finding is classified **SUBSTANTIVE** (error / unsupported claim / missing
derivation) or **GENRE** (length, house style, presentation convention), per the
R2 stop rule.

### MAJOR 1 — SUBSTANTIVE. The repulsive-sign derivation contains two sign errors that cancel.
**Location:** `main.tex:225–236`, PDF p. 2, Sec. II.
**Defect.** The paper writes: with $\rho_{4\psi}=-\mathcal L_{4\psi}$ and
$p_{4\psi}=\mathcal L_{4\psi}$, *"a repulsive … interaction requires
$\rho_{4\psi}+3p_{4\psi}<0$, i.e.\ $-2\mathcal L_{4\psi}<0$, i.e.\
$\mathcal L_{4\psi}>0$"*, and then that *"Eq. (3)'s coefficient
$-(3\kappa/16)\gamma^2/(1+\gamma^2)<0$ multiplying $(J_5^IJ_{5I})>0$ … gives
$\mathcal L_{4\psi}>0$"*.
**Evidence.** Two independent errors:
(i) From the paper's own $\rho=-\mathcal L$, $p=+\mathcal L$,
$\rho+3p=-\mathcal L+3\mathcal L=+2\mathcal L$, **not** $-2\mathcal L$. The
requirement is therefore $\mathcal L_{4\psi}<0$.
(ii) A negative coefficient multiplying a positive quantity is negative, so
Eq. (3) gives $\mathcal L_{4\psi}<0$, **not** $>0$. Recomputed at
$\gamma=0.2375$ with $(J^5\!\cdot\!J^5)=+1$: $\mathcal L_{4\psi}=-0.01001$.
The two errors cancel, so the physical conclusion (repulsive, $\rho+3p=2\mathcal
L=-0.0200<0$) is correct — but **every displayed step of the chain is wrong**,
and this chain was *added by the DP1N-35 closure*, i.e. it is a regression
introduced in v1N.0.3. A referee checking the sole displayed sign argument for
the paper's central positive claim will find it does not compute.
**Additional defect in the same sentence:** the conclusion is asserted
*"signature-independent"* while resting on the parenthetical assumption that
$J^5$ is *"spacelike-normalized"*. That assumption is load-bearing (it fixes the
sign of $(J^5\!\cdot\!J^5)$) and is neither justified nor tied to the
configurations of interest, where a spin-aligned axial current is naturally
timelike. Signature-independence cannot be claimed while conditioning on a
signature-dependent normalization.
**Required:** rewrite the three lines correctly and either justify or drop the
"spacelike-normalized" premise and the signature-independence claim.

### MAJOR 2 — SUBSTANTIVE. Route 3's new scaling relation does not produce the paper's own quoted 61–67-order window, and the stated origin of that window is not its actual origin.
**Location:** Eq. (11) `main.tex:729–733`; window `main.tex:743–754`; repeated
`main.tex:1032–1034`. PDF pp. 6, 9.
**Defect.** The DP1N-27 closure displayed a *new* scaling relation,
$\delta\rho_\Lambda^{(\rm R3)}/\rho_{\Lambda,\rm obs}\sim
|\Delta\gamma/\gamma|\times(\kappa n_\psi^2/\rho_{\Lambda,\rm obs})$, while
retaining the pre-existing "61–67 orders" figure and attributing the spread to
*"varying the reference fermion density $n_\psi$ and the sub-Planckian UV
boundary $\mu_{\rm UV}$"*. Neither the central value nor the window follows.
**Evidence.**
- The paper's own central inputs give
  $1.4\times10^{-6}\times3.9\times10^{-69}=5.46\times10^{-75}$ — recomputed —
  i.e. **74.3 orders** below $\rho_{\Lambda,\rm obs}$. The paper prints this value
  ("$\sim5\times10^{-75}$", `main.tex:741–742`) and then, two lines later, quotes
  a 61–67 window that **does not contain its own central estimate**.
- The stated $\mu_{\rm UV}$ variation cannot bridge the gap: pushing
  $\mu_{\rm UV}\to M_{\rm Pl}$ takes $|\Delta\gamma/\gamma|\to\mathcal O(1)$ and
  the ratio to $3.9\times10^{-69}$, i.e. 68 orders. Eq. (11)'s honest window is
  therefore ~68–74, not 61–67.
- The 61–67 endpoints are traceable, and they come from a **different relation**.
  `arxiv/paper1c_nogo_survey/main.tex:1563–1583` gives
  $\rho_{\rm R3}/\rho_{\Lambda,\rm obs}\sim(\Delta\gamma/\gamma)(H_0/M_{\rm Pl})$
  with $H_0/M_{\rm Pl}=1.18\times10^{-61}$, and states the two endpoints
  explicitly: $\Delta\gamma/\gamma\sim0.3$ (the **chiral-count** input) gives
  $3\times10^{-62}$, *"$\sim$61 orders"*; $\Delta\gamma/\gamma=1.4\times10^{-6}$
  gives $1.7\times10^{-67}$, *"$\sim$67 orders"*. Recomputed this round:
  $3.54\times10^{-62}$ → **61.45**, $1.652\times10^{-67}$ → **66.78**. Exact match.
  The window's real variable is $\Delta\gamma/\gamma$ under P1C's $H_0/M_{\rm Pl}$
  relation — not $n_\psi$, and not the relation the Note now prints.
**Compounding.** The 61 endpoint is generated by precisely the "chiral-count"
input the DP1N-30 closure deleted, so the Note no longer contains anything that
could produce it. And Table II's R3 row still credits a *"mass-dimension lock"*
— P1C's $H_0/M_{\rm Pl}$ dimension argument — which the Note does not contain
(MINOR 5).
**Required:** either restore P1C's $H_0/M_{\rm Pl}$ relation as the one that
defines the quoted orders, or keep Eq. (11) and re-quote the window it actually
implies. The two cannot both stand.

### MAJOR 3 — GENRE (directive Q1), but a hard publication gate. The manuscript narrates its own internal draft errata and internal tracking state.
**Location:** `main.tex:948–950`, `953–954`, `1104`, `627`. Verified on the
300-DPI render of PDF p. 8 and p. 11.
**Defect.** The published text reads: *"the printed coefficient in an earlier
internal draft omitted this $8\pi$ substitution and is corrected here (SSOT)"*
(p. 8, right column) — an in-body erratum notice referencing an internal artifact
name meaningless to any reader. It is reinforced at `main.tex:953–954` by
*"not a $\sim$4.5×-smaller correction to O5"*, which quotes a number that appears
nowhere in this manuscript and exists only in the superseded draft. Sec. "Data and
Code Availability" opens *"This manuscript is internally tracked as v1N.0.3"*
(`main.tex:1104`). `main.tex:627` retains the internal project label
*"(P1A~\cite{Golden2026P1a})"*.
Ironically the DP1N-40 closure ("use the dead `\paperVersion` macro") created the
`1104` instance while DP1N-32 was supposed to be removing exactly this register.
**Required:** state Eq. (15) as the result, with no comparison to an unpublished
prior value and no `(SSOT)`; delete the internal version sentence and the `P1A`
tag. Errata belong in the internal record, not the manuscript.

### MAJOR 4 — SUBSTANTIVE. Several added barrier citations are topical pointers that do not support the proposition they are attached to, while the abstract now asserts the barriers are "literature-sourced".
**Location:** `main.tex:92` (abstract); B2 `524–529`, B5 `551–557`, B6 `559–567`,
B10 `603–610`.
**Defect.** The DP1N-24 closure raised the citation count from 4 to a citation on
almost every barrier, and the abstract was strengthened to say the barriers other
than the two derived ones *"are literature-sourced or self-labelled heuristics"*.
Checked individually, the mapping does not hold for several:
- **B2** attaches `BlagojevicHehl2013` (a gauge-theories-of-gravitation reader)
  and `BoehmerBurnett2008` to a **biconditional** — *"mass protection $\iff$ no
  geometric fingerprint"*. Neither source states this biconditional; it remains a
  proposition of this paper with no proof and no genuine reference.
- **B5, B6, B10** each attach `Weinberg1989`. Weinberg's review is the canonical
  statement of the cosmological-constant problem; it contains nothing about the
  bounce density, about transfer across "$N_{\rm tot}\approx92$–94 $e$-folds", or
  about a UV→IR bridge in minimal ECH. The citation establishes that a naturalness
  problem exists, not that these three specific ECH claims hold.
By contrast B1, B3, B4, B11, B12, B13 are fairly supported (B3 in particular now
carries a real in-paper argument from the algebraic torsion EOM), so this is a
targeted objection, not a blanket one.
**Required:** either downgrade the abstract's "literature-sourced" wording to
match what the citations actually establish, or supply the 2–4 line derivations
for B2, B5, B6, B10 that R2's closure instruction asked for. A citation that
establishes the *topic* is not a citation that establishes the *claim*.

### MAJOR 5 — SUBSTANTIVE. The Planck-mass convention added for DP1N-42 is mislabeled, and the label contradicts the paper's own $\kappa$.
**Location:** `main.tex:720–722`, PDF p. 6.
**Defect.** *"Throughout this integration $G=1/M_{\rm Pl}^2$ with
$M_{\rm Pl}=1.22\times10^{19}$ GeV (**reduced-Planck-mass convention**, as used
consistently elsewhere in this paper…)"*.
**Evidence.** $1.22\times10^{19}$ GeV is the **non-reduced** Planck mass;
the reduced Planck mass is $M_{\rm Pl}/\sqrt{8\pi}=2.435\times10^{18}$ GeV
(recomputed). The relations $G=1/M_{\rm Pl}^2$ and $\kappa=8\pi G=8\pi/M_{\rm
Pl}^2$ (`main.tex:182`) are both the non-reduced convention; in the reduced
convention one has $\kappa=1/\bar M_{\rm Pl}^2$ with no $8\pi$. The paper's
numerics are internally consistent and correct (Sec. II uses
$M_{\rm Pl}=1.22089\times10^{28}$ eV, verified above to reproduce
$3.884\times10^{-69}$) — **only the convention label is wrong**. But this is the
one sentence the R2 closure added specifically to protect the reader from an
$8\pi$ ambiguity, immediately after an $8\pi$ error was found (DP1N-21), and it
misnames the convention. Any referee who trusts the label will be off by
$\sqrt{8\pi}$.
**Required:** delete "reduced-".

### MINOR 1 — SUBSTANTIVE. DP1N-29 is recorded as closed but is not.
`main.tex:486`, Table I caption, PDF p. 4: *"to avoid confusion with the imaginary
unit and the Barbero–Immirzi symbol $\kappa$."* $\gamma$ is the Barbero–Immirzi
parameter; $\kappa=8\pi G$ is the gravitational coupling, as the paper's own
Eq. (1) states. Fix: "the gravitational coupling $\kappa$".

### MINOR 2 — GENRE. DP1N-37 is recorded as closed but is not.
Abstract measured this round at **433 words** (LaTeX macros and math stripped).
The SSOT closure table records "435 → ~380". It is essentially unchanged and
still runs ~1.4× the CQG guidance of ~300, filling p. 1.

### MINOR 3 — SUBSTANTIVE. Residual "parity-odd" language contradicts the new mixed-parity statement.
After `main.tex:930–936` establishes the list is *"a mixed-parity
$\varepsilon$-contracted set, not a strictly parity-odd one"*, the paper still
says at `main.tex:852` *"parity-odd $\varepsilon$ contraction"* as the construction
rule and, decisively, at `main.tex:978–979` concludes *"every admissible local
dimension-4 **parity-odd** density in minimal ECH is topological, …"* — the
summary sentence of the whole section reverts to the classification the section
just corrected. `main.tex:850` and `909` are the same slip. Fix: use
"$\varepsilon$-contracted" / "construction-rule-admitted" uniformly.

### MINOR 4 — SUBSTANTIVE. The DP1N-33 fix is contradicted in the Discussion.
`main.tex:692–695` correctly restricts the "58 orders" figure to the
*doubly-normalized* ratio of Eq. (7). `main.tex:1032–1033` then states *"Route 2
with $\approx$60 (conservatively $\geq58$) orders of margin **against the observed
birefringence amplitude**"* — the exact misdescription DP1N-33 was opened to
remove. Fix the Discussion sentence to match.

### MINOR 5 — SUBSTANTIVE. Table II names an argument that does not appear in the paper.
Table II, R3 row (`main.tex:798–800`, PDF p. 8): *"mass-dimension lock is
structural"*. Grep: "mass-dimension lock" occurs exactly once in the manuscript.
The lock is P1C's $H_0/M_{\rm Pl}$ dimension argument
(`paper1c_nogo_survey/main.tex:1555–1560`), which the Note does not carry. This is
the same defect class as the "chiral-count bound" removed under DP1N-30, recurring
in the same table. Fix: import the argument or rename the row's basis.

### MINOR 6 — SUBSTANTIVE (missing derivation). The gap-equation loop integral's prefactor is asserted.
`main.tex:313–317`. The logic is sound and correct — $M=0$ always solves it, a
nonzero root needs $1=2G_sI$, and $I>0$ with $G_s<0$ forbids it — and only $I>0$
is load-bearing. But the specific prefactor $N_cN_f/(4\pi^2)$ is printed without
derivation or citation and does not match the standard NJL normalization for
$\langle\bar\psi\psi\rangle$ in this convention. Either derive/cite it, or write
$I(M,\Lambda_{\rm cut})\propto\int_0^{\Lambda_{\rm cut}}p^2dp/\sqrt{p^2+M^2}>0$
and state that only positivity is used.

### MINOR 7 — SUBSTANTIVE. "Vanishes only in the $\gamma\to\infty$ limit" is false as written.
`main.tex:954–956`: $\mathcal O_4^{[4]}\propto\gamma^3/(1+\gamma^2)^2$ vanishes
as $\gamma\to0$ as well. Fix: "vanishes in the $\gamma\to\infty$ Einstein–Cartan
limit (and, degenerately, as $\gamma\to0$)".

### MINOR 8 — SUBSTANTIVE. Internal contradiction inside one sentence about O4.
`main.tex:938–941`: *"$T_I\wedge T^I$ is supported only by the **non-axial**
torsion irreps — it vanishes on a pure axial or a pure trace-vector torsion alike
and is carried entirely by the **axial×trace-vector** cross term"*. The cross term
requires the axial irrep, so "supported only by the non-axial irreps" contradicts
the clause that follows it. The intended statement — that O4 needs *both* irreps
and vanishes on either alone — is correct and is what the $\gamma\to\infty$
behavior confirms; only the first clause is wrong.

### MINOR 9 — GENRE. Internal project label in the body.
`main.tex:627`: *"(P1A~\cite{Golden2026P1a})"*. "P1A" is an internal identifier.
Cite the reference; drop the tag. (Residual of DP1N-32; see MAJOR 3.)

---

## Classification tally

**SUBSTANTIVE** (error, unsupported claim, or missing derivation): MAJOR 1,
MAJOR 2, MAJOR 4, MAJOR 5, MINOR 1, MINOR 3, MINOR 4, MINOR 5, MINOR 6,
MINOR 7, MINOR 8 — **11**.
**GENRE / LENGTH / VENUE**: MAJOR 3 (directive-Q1 presentation), MINOR 2
(abstract length), MINOR 9 (internal label) — **3**.

Note for directive R2: this round did **not** bottom out in genre/length/venue
items. Four of the five MAJORs are substantive, and three of them
(**MAJOR 1, MAJOR 2, MAJOR 5**) are *regressions introduced by the R2 closure
itself* — a displayed sign chain that does not compute, a substituted scaling
relation that does not reproduce the number it was attached to, and a mislabeled
Planck-mass convention. That pattern is the finding this round most wants
recorded: the R2 closure converted six "assert it" items into "display the
derivation" items, and three of the newly displayed derivations are wrong. The
remedy is arithmetic verification of each newly displayed step, not another
review board.

## Verdict

**major-revisions**

**Justification.** The four headline R2 science decisions are genuinely and
correctly closed, and the DP1N-21 coefficient correction in particular is
re-derived here from the paper's own conventions and confirmed exact — the
manuscript's central physics (Cartan elimination, the contact term, the
transparency theorem, the operator rank/count, the Popławski mapping) is sound,
honestly scoped, and now materially stronger than v1N.0.2. The paper is not far
from acceptable. But it cannot be accepted in this state: the sole displayed
derivation of the repulsive sign — the positive half of the title — is wrong in
two places (MAJOR 1); Route 3's headline "61–67 orders" is not what the paper's
own newly displayed equation produces, and its stated provenance is
demonstrably not its actual provenance (MAJOR 2); the Planck-mass convention
sentence added to prevent an $8\pi$ ambiguity misnames the convention (MAJOR 5);
several barrier citations do not support the claims they are attached to while
the abstract asserts they do (MAJOR 4); and the manuscript prints an internal
erratum notice and internal version-tracking string (MAJOR 3). Two R2 items
recorded as closed in SSOT are not closed at all (MINOR 1, MINOR 2), which means
the closure record itself needs re-verification rather than trust. All of these
are correctable by editing, none threatens the paper's conclusions, and none
requires new computation beyond checking arithmetic already in hand.

**Substantive findings remaining: 11**
