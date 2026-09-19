# INT referee report — PSU (separate-universe criterion note) v1S.0.8, round R3VERIFY

- Reviewer: Claude (Opus 5) INT leg, independent skeptical PRD short-note referee
- Date: 2026-09-18
- Artifact reviewed: `arxiv/paper_su_criterion/main.tex` (ground truth) + `arxiv/paper_su_criterion/main.pdf`
- PDF SHA-256: `9f1fc41cce00b03f0cbbff80c709353e04958259925519984c87b9632bf0443d` (verified; byte-identical at `site/public/papers/paper_su_criterion_v1S.0.8.pdf`, `site/out/papers/…`, `public/papers/…` — directive-G mirror gate PASSES)
- `main.tex` SHA-256: `84d82bef6f359429751840732e33f0fb38caddb434c4fecf84a3bcf4e6231b9e`
- Pages: 6 (all read; text extracted with `pdftotext`, pages 1–4 rendered to PNG for figure/table inspection; `main.log` scanned)
- Method: `.tex` read in full, line by line. All load-bearing algebra re-derived by hand independently before any source note was consulted for it. Source notes (`a2_lapse_monopole_adjudication_2026_09_07.md`, `psu_gates_S1_S2`, `threading_map_second_order`) read for provenance and arithmetic-chain checking, not taken on trust. Prior R1/R2 audits and `DISPOSITIONS/PSU.md` read only at the end, to separate genuinely-new findings from re-flags. Not told an expected verdict.
- Venue bar: Physical Review D, short note / Brief Report.

---

## Summary

1. **The core science checks out.** I independently re-derived and confirm: the threading identity Eq. (1) from `NK = d/dt ln√h|_wl − ∂_iN^i`; `∂_iN^i = (ε/c_s²)ζ̇ − ∇²ζ/(a²H)` from `ψ = −ζ/H + χ`, `∂²χ = a²(ε/c_s²)ζ̇`; `I = ε` on a constant-ε pure growing mode; `λ = (1−w)/2`; both f_map monopoles `= −5ε/6` (so `−(5/4)(1+w)`); the second equality of Eq. (4) (**R2's C2 sign error is genuinely fixed**); `f_δN^init = f^in-in/λ + f_map^init ≡ −5` identically in *both* ε and μ; `f_δN^fin = −15(ε−4)/(4(ε−3)) + 15εμ²/(4(3−ε)) → −25/4 + (15/4)μ²` at ε=3/2; the in-in monopole `−(5/18)(ε−3)(ε−6) = −15/8`; the 25/8 gap and 8/3 ratio, and the 4/3 alternative (**R2's C4 arithmetic error is genuinely fixed**). I also derived `λ_USR` from scratch (`I = √(ε_sε_f) − ε_f`) and it matches the printed `1 + ε_f/3 − √(ε_sε_f)/3` exactly.
2. **The new Appendix A2 kernel table is right.** I summed the five listed contributions (`zlap`, `psi2`, `grad`, `wl_fin`, `lab_init`) and they reproduce Eq. (4)'s constant part `−5ε/4` and μ² part `+5ε/4` *exactly*, and each quoted per-contribution monopole (`5ε/(3−ε)²`, `5ε(−ε²+6ε−15)/(6(3−ε)²)`, `0`, `0`) is correct and they total `−5ε/6`. This is a strong internal consistency check and it passes.
3. **The v1S.0.8 closing amendment landed in the Appendix but NOT in the main text.** Sec. III (p.3) still prints `f^ρ_NL = (5/24)(2ε−15) = −5/2`; Appendix A5 (p.6) prints `f^ρ_NL = (5/8)(ε−7) = −55/16` *and explicitly states that the −5/2 figure is wrong and why*. The main text even cross-references the appendix that refutes it. Two contradictory values for the same headline quantity inside one manuscript.
4. **The manuscript does not compile cleanly.** `main.log:804` carries a hard `! LaTeX Error: Unicode character ρ (U+03C1) not set up for use with LaTeX` from a raw UTF-8 ρ at `main.tex:514`. The character is *silently dropped* from the output: p.6 reads "The uniform-density (-)slice question of Sec. II".
5. **The A5 amendment paragraph is not readable as written.** `λ′` and `A₂` each appear exactly once in the entire manuscript, both undefined; `f^ρ_NL` is quoted twice with no statement of what it is normalized by, even though the source adjudication establishes that `δN_{c,ρ} = λ′ζ₁ + 3λζ₂` with `λ′ = 2λ` — i.e. `−55/16` is not an f_NL of ζ.

## Verdict

**MAJOR REVISIONS.** The physics is, as far as I can check it, correct and the note is worth publishing. But the manuscript currently prints a number its own appendix declares superseded, throws a LaTeX error that garbles the text of the paragraph carrying the corrected result, and states that corrected result in terms of two symbols it never defines. Those are not minor-revision items on a 6-page note whose entire content is a set of exact numbers.

---

## ESSENTIAL

**PSU-v8-E1 — Sec. III prints a value the paper's own Appendix declares wrong (`main.tex` l. 227–232; PDF p.3 col.1).**
Sec. III: *"continuing the fluid-congruence field $N_c$ onto the uniform-density surface $\rho=\bar\rho(t_f)$ (rather than uniform-$\phi$) to second order gives $f^{\rho}_{\rm NL}=\tfrac{5}{24}(2\eps-15)$, isotropic, i.e.\ $-\tfrac52$ at $\eps=\tfrac32$ (initial-position label) … (Appendix~\ref{app:kc})."*
Appendix A5 (`main.tex` l. 515–524; PDF p.6): *"continuing $N_c$ to second order on $\rho=\bar\rho(t_f)$ has squeezed monopole $f^{\rho}_{\rm NL}=\tfrac58(\eps-7)=-\tfrac{55}{16}$ at $\eps=\tfrac32$ … the earlier initial-label figure $\tfrac{5}{24}(2\eps-15)=-\tfrac52$ came from composing the map with the linear-mode weight $\lambda'=2\lambda$ where the $\rho$-surface time shift … instead carries weight $3\lambda$."*
Both are in the served PDF (verified by `pdftotext`: p.3 "= 5/24 (2ϵ − 15)"; p.6 "= 5/8 (ϵ − 7) = −55/16"). The main text directs the reader to the appendix *for* the number, and the appendix says that number is an artifact of a composition error. I independently checked the corrected chain and it is arithmetically exact: with `f^in-in_mono = (5/18)(3−ε)(ε−6)` and `λ′ = 2λ = 2(3−ε)/3`, `f^in-in/λ′ = 5(ε−6)/12`; `f^in-in/λ′ + f^ρ_map = 5(ε−6)/12 − 5/8 = 5(2ε−15)/24` (the printed Sec.-III value) and `(3/2)·f^in-in/λ′ + f^ρ_map = 5(ε−6)/8 − 5/8 = 5(ε−7)/8 = −55/16` at ε=3/2, with gap `5(ε−6)/24` — exactly as the adjudication note states. **The closing-amendment edit was applied to the Appendix and not propagated to Sec. III.**
*Required fix:* replace the Sec.-III value with `f^ρ_NL = (5/8)(ε−7) = −55/16` at ε=3/2, and grep the whole `.tex` for `2\eps-15` / `-\tfrac52` before recompiling. Keep the superseded form *only* inside the A5 sentence that explains it, and mark it there as superseded. (See also E2: the sentence in A5 that does this is currently garbled.)

**PSU-v8-E2 — The manuscript does not compile cleanly; a raw UTF-8 ρ throws a LaTeX error and is dropped from the PDF (`main.tex` l. 514; `main.log` l. 804).**
`main.tex:514`: `The uniform-density (ρ-)slice question of Sec.~II is distinct from this admixture:` — a literal U+03C1, the only non-ASCII byte in the file. `main.log:804–805`:
```
! LaTeX Error: Unicode character ρ (U+03C1)
                not set up for use with LaTeX.
```
`pdftotext` on the shipped `main.pdf` returns `The uniform-density (-)slice question of Sec. II` — the ρ is gone, leaving `(-)slice`. This is the opening sentence of the paragraph that carries the corrected −55/16 result. arXiv's AutoTeX will reproduce the same error (and may hard-fail rather than continue).
*Required fix:* `(ρ-)` → `($\rho$-)`. Then re-run `pdflatex` and confirm `main.log` has zero `^!` lines. A zero-undefined-reference check is not sufficient — this error is not a reference error and the current log *does* have zero undefined refs.

---

## MAJOR

**PSU-v8-M1 — `f^ρ_NL` is quoted twice with no statement of its normalization; as printed, `−55/16` is not interpretable (`main.tex` l. 229–232, l. 515–517).**
`f_NL` is a ratio `B/P²`, so the value depends on which field's power spectrum normalizes it. The adjudication note the paragraph rests on establishes that on the uniform-density slice `δN_{c,ρ} = λ′ζ₁ + 3λζ₂` with `λ′ = 2λ = 2(3−ε)/3` — i.e. `δN_{c,ρ}` is *not* ζ even at linear order, and `−55/16` is the f_NL of `δN_{c,ρ}` normalized by its own spectrum. None of this is in the paper. A reader comparing `−55/16` to the in-in `−15/8` or to the comoving `−5` has no way to know they are three differently-normalized objects, which is precisely the confusion the paper's title claims to resolve.
*Required fix:* state the linear ρ-slice rescaling (`δN_{c,ρ} = λ′ζ_L` at linear order on the growing mode, `λ′ = 2λ`) in the same paragraph as the second-order value, and say explicitly that `f^ρ_NL` is normalized by `P_{δN_{c,ρ}}`.

**PSU-v8-M2 — `λ′` and `A₂` are each used exactly once and never defined (`main.tex` l. 519–523).**
Verified by grep: `\lambda'` occurs once (l. 522), `A_2` occurs once (l. 520). The sentence *"the second-order threading map's long$\times$short lapse monopole coefficient $A_2=\epsilon(3-\epsilon)^2/3$ is the correct constraint-solve value (not $2(3-\epsilon)^2$)"* presupposes a definition (`N = 1 + α₁ + α₂`, `α₂ ⊃ A₂ ζ_Lζ_S`, squeezed super-Hubble monopole) that appears nowhere in the manuscript; and `λ′ = 2λ` presupposes `λ′ ≡ λ + Hδt^(1)_S/ζ_S`, also absent. The paragraph is therefore unparseable to any reader who has not read `a2_lapse_monopole_adjudication_2026_09_07.md`, which the Appendix exists precisely to make unnecessary ("This appendix transcribes … the material a standalone reader needs", l. 396–398).
*Required fix:* define both symbols where they are first used, or recast the sentence so it does not depend on them.

**PSU-v8-M3 — The Reproducibility Statement omits the two scripts that produce the manuscript's newest results (`main.tex` l. 333–350 vs l. 512, l. 518).**
Every other load-bearing computation is listed with path + truncated SHA-256 + manifest, and I verified all four printed prefixes are correct (`21668ab6…`, `4e2a49be…`, `4f641022…`, `f4164019…` all match the on-disk files) and all cited paths exist on `main`, and both cited commits (`f3516042`, `a310bd90`) resolve. But:
- `psu_gates_S9_S10_2026_09_05.py` appears only as a bare `\texttt{}` filename at the end of A5 (l. 512) — no path, no link, no SHA, no manifest;
- `a2_lapse_monopole_adjudication_2026_09_07.md` appears only as a `\texttt{}` path at l. 518 — not a `\url{}` like every other artifact, no SHA, and neither its `.py` nor its manifest (`reproducibility/manifests/experiments/a2-lapse-monopole-adjudication.json`, which exists) is cited;
- the AI Usage Disclosure (l. 353–362) enumerates "the linear criterion, the second-order map for both worldline labels, and the four validations" and does not mention the ρ-slice/A₂ work at all.
The result is that the single newest number in the paper is the least reproducibly sourced.
*Required fix:* add both scripts + the a2 manifest to the Reproducibility Statement with SHA-256 prefixes and `\url{}` links matching the existing style; extend the AI Usage Disclosure to cover the ρ-slice continuation.

**PSU-v8-M4 — The convention relating the kernel `𝓜` to `f_NL` is never stated, and the one contribution I could integrate by hand comes out a factor 2 from the quoted value (`main.tex` l. 421–426; l. 504–508).**
A2 defines `δN_c^{(2)} = 𝓜 ζ_Lζ_S` and quotes `zlap`'s "local kernel $2\eps/3$". Taking the definition literally: `∂_iN^i ⊃ −2ζ_L ∂²ψ_S/a² → −2εζ_Lζ̇_S` super-Hubble, so `δN_c^{(2)}|_zlap = −(1/3)∫(−2εζ_Lζ̇_S)dt = (2ε/3)∫ζ_Lζ̇_S dt = (ε/3)ζ_Lζ_S` for `ζ_L,ζ_S ∝ a^{−(3−ε)}` (the antisymmetric part of the integral vanishes for equal power laws) — i.e. `𝓜 = ε/3`, not `2ε/3`. A5's assembly formula `f_map = [5/(12λ_gλ₁)]·[𝓜(k_L,q)P(q)+𝓜(k_L,p)P(p)]/P_S` then returns `5ε/(3−ε)²` from `𝓜 = 2ε/3`, matching the quoted zlap contribution — so the manuscript is internally consistent and the discrepancy is almost certainly an unstated symmetrization (`𝓜[ζ_Lζ_S + ζ_Sζ_L]`). **I am flagging this as a stated-convention gap, not asserting an error**: the five contributions demonstrably sum to Eq. (4) exactly, which they could not do if the normalization were wrong. But a reader following the appendix's own definition gets the wrong answer on the first and simplest term, in the one section whose stated purpose is standalone verifiability.
*Required fix:* state the Fourier/symmetrization convention explicitly (`ζ^{(2)}(k) = ∫ 𝓜(k₁,k₂)ζ(k₁)ζ(k₂)`, symmetrized or not) and the `B → f_NL` conversion, so the quoted per-contribution numbers can be checked.

**PSU-v8-M5 — The Lyth–Malik–Sasaki loop is left open, and it is the loop that decides the paper's thesis (`main.tex` l. 213–217).**
The paper concedes: *"The final slice used throughout is uniform-$\phi$ (comoving), which coincides with uniform-$\rho$ only at $I\to0$; at $I=O(1)$ the two differ already at $O(k^0)$, so Lyth--Malik--Sasaki's $\delta N=\zeta_{ud}$ … is not the object compared here, and this is a second, independent $O(1)$ slice ambiguity of the same order as the effect this note isolates."*
A skeptical referee reads this as the paper conceding the alternative explanation of its own headline result: that the "identification error" is the known comoving-vs-uniform-density slicing difference in a non-attractor, not a new statement about what the separate universe computes. The discriminating test is one line of the machinery already in A5 — compute (or cite) the in-in `ζ_ud` squeezed monopole at constant ε and compare it to the `δN_{c,ρ} = −55/16` the appendix now has. If they agree, LMS holds exactly and the paper's criterion is a clean slicing statement that should be framed that way; if they disagree, that is a much stronger result than the one currently claimed. Either outcome strengthens the paper; leaving it unstated is what a PRD referee will push back on hardest.
*Required fix:* compute the in-in `ζ_ud` monopole at constant ε (the paper already has `ζ_comoving`'s general-ε shape and the second-order time shift to the ρ-surface), compare to `5(ε−7)/8`, and state in Sec. III whether LMS's `δN = ζ_ud` survives at `I = O(1)`.

**PSU-v8-M6 — Footnote 1 mis-describes the decomposition its own Appendix gives (`main.tex` l. 165–168 vs l. 425–443).**
Footnote 1: *"Each of the five geometric contributions to $f_{\rm map}^{\rm fin}$ carries an overall factor of $\eps$: the lapse, the second-order metric perturbation, the gradient term, the final-position worldline displacement, and the initial-label translation."* Two errors against Appendix A2:
(a) the fifth item, `lab_init`, is by construction the *difference* between the two labels — it is exactly what `f_map^fin` does **not** contain (A2: "`lab_init` … the rigid translation $x_f\to x_i$ (initial-position label)"; A3: `T ≡ f_map^init − f_map^fin`). `f_map^fin` has four contributions, not five.
(b) the first item is called "the lapse", but A2 identifies it as `zlap`, *"the $-2\zeta\,\partial^2\psi$ term from $e^{-2\zeta}$ in $N^i=h^{ij}N_j$"* — a shift/spatial-metric term. Calling it "the lapse" is doubly confusing in v1S.0.8, where A5 now introduces a genuinely different quantity called the "lapse monopole coefficient `A₂`".
The ε-proportionality claim itself is correct (I verified all five listed closed forms carry an explicit ε).
*Required fix:* "the four geometric contributions to `f_map^fin` … plus the initial-label translation that distinguishes `f_map^init`"; rename "the lapse" to match A2's `zlap` description.

---

## Minor

**N1 — Inconsistent ε domain.** l. 258–259 says `f_δN^init = −5` *"for every constant $\eps\in(1,3)$"*; l. 153 and l. 469 say *"for every constant $\eps$"*. The restriction `(1,3)` is never justified. `ε < 3` is presumably the growing-mode condition (`ζ ∝ a^{−(3−ε)}`); the lower bound `ε > 1` is unexplained. State the domain once, with its reason, and use it consistently.

**N2 — Wrong cross-reference in A5 (l. 514).** *"The uniform-density (ρ-)slice question of Sec.~II"* — that question is raised in **Sec. III** (`The criterion`, l. 227–232), not Sec. II. Verified in the PDF (`of Sec. II`). Use `\label`/`\ref` rather than a hardcoded numeral.

**N3 — `\ref{app:kc}` renders as "Appendix A 5" (PDF p.3).** The label sits on a `\subsection`, so `\ref` returns a subsection number that revtex typesets with a space. Either label the appendix itself, or write "Appendix A, Sec. 5".

**N4 — "for all ε" attached to a dust-specific number (l. 526–528).** *"An independent exact separate-universe solution reproduces both $-\tfrac{55}{16}$ (uniform-density slice) and $-5$ (comoving slice) for all $\epsilon$."* `−5` is ε-independent; `−55/16` is `5(ε−7)/8` evaluated at ε=3/2 only. Write "reproduces both `5(ε−7)/8` (uniform-density) and `−5` (comoving) for all ε".

**N5 — Table I overflows its ruled width (`main.log` l. 569: `Overfull \hbox (8.31297pt too wide) in alignment at lines 242--249`).** Visible on PDF p.4: the ekpyrosis row's `result` cell runs past the right rule. Shorten the cell or widen/rebalance the columns.

**N6 — Eqs. (1) and (2) overfull (`main.log` l. 547: 2.63698pt at line 123; l. 557: 2.21017pt at line 135).** Small but real in a two-column layout; break or rescale.

**N7 — ~25 badness-10000 underfull lines in the Reproducibility Statement (`main.log` l. 584–714, paragraph at lines 334–351).** Visible as very ragged spacing on PDF p.4 col.2. The `\UrlBreaks` patch helps but the column is too narrow for these paths; consider a `\raggedright` block or a hash table.

**N8 — Abstract and Sec. I say "matter-dominated contraction"; Sec. III and Table I carefully say it is not (l. 44, l. 82–83 vs l. 254–257).** Sec. III: *"a $w=0$, $c_s=1$ field, not true dust: genuine dust has $c_s\to0$, where $I=\zeta^{-1}\int(\eps/c_s^2)\dot\zeta\,dt$ diverges and the criterion as stated does not apply"*. Carry that qualifier into the abstract — as written the abstract advertises a case the body excludes.

**N9 — `I → ε` stated without its condition (l. 138–140).** *"$1-\lambda=I/3$ reduces to $\eps/3$ for constant $\eps$ (i.e.\ $I\to\eps$)"*. With a constant admixture `I = ε(1 − ζ_{L,i}/ζ_{L,f}) = εg`, which A5 handles correctly (`λ_g = 1 − εg/3`). The pure-growing-mode condition is stated only for the *second-order* result (l. 143–144). State it for the linear reduction too, and forward-reference A5.

**N10 — Eq. (1) is called "the exact identity" but drops `ζ(t_i,x_i)` (l. 117–123; A1 l. 411).** Integrating `NK = d/dt ln√h|_wl − ∂_iN^i` with `ln√h = 3 ln a + 3ζ` gives `δN_c = ζ(t_f,x_f) − ζ(t_i,x_i) − (1/3)∫∂_iN^i dt`. Dropping the second term is legitimate on the flat `Σ_i` (which the surrounding prose does specify), but A1's one-line "this is Eq. (1)" derivation never mentions it — the exact point a standalone reader stumbles on.

**N11 — "Splitting the interval at the comoving slice through $x_i$ and integrating" (l. 130–131) is not explained.** It is the load-bearing step between Eq. (1) and Eq. (2). One sentence saying what is split and why.

**N12 — `ε → 0` is repeatedly called "the attractor limit" (Fig. 1 caption; l. 176–177; l. 261–263), but the USR row is an `ε → 0` *non*-attractor.** What `ε → 0` actually buys is `f_map → 0` and `λ → 1` on *either* mode. Relatedly, l. 261–263 (*"coincide only in the attractor limit $\eps\to0$, where both are computed on the constant mode ($I=0$) rather than by extrapolating this $\eps=3/2$ result"*) is self-undercutting: the `−5` coincidence at ε→0 *is* the extrapolation of the growing-mode formula. Rewrite to separate "ε→0 on the growing mode" (map→identity, `f^in-in_mono → −5 = f_δN`) from "the attractor" (`ζ̇=0`, `I=0`, Maldacena `(5/12)(1−n_s)`).

**N13 — Fig. 1 still plots two exactly-linear curves that coincide after dual-axis rescaling (PDF p.2).** The rendered figure shows the blue `λ(w)` and the red dashed `f_map^mono(w)` lying on top of each other; the figure carries no information beyond Eq. (5). This was raised at R2 (minor 8) and is unchanged in v1S.0.8. Either replace it with something the closed form does not already say (e.g. `I(t)` along the four histories, or `λ_USR(ε_s,ε_f)`), or drop the figure and keep Eq. (5).

**N14 — A5's title does not cover its second paragraph (l. 491–492).** The subsection is titled *"The general admixture: constant-mode kernel and the corrected normalisation"*; its second paragraph is the ρ-slice/A₂ amendment, which opens by saying it *"is distinct from this admixture"*. Split it into its own subsection — this is also the cleanest way to give `λ′` and `A₂` a home (M2).

**N15 — Table I floats to p.4 while its discussion is on p.3.** `[t]` on a `table*` in a 6-page note; consider `[!t]` or moving the discussion.

**N16 — Ref. [22] incomplete.** Naruko, Takamizu & Sasaki is given as `arXiv:1210.6525 (2012)` only; it is published (PTEP 2013, 043E01). Every other entry in the bibliography carries a journal reference.

**N17 — Dangling antecedent after Eq. (4) (l. 163–165).** *"giving $f_{\delta N}^{\rm fin}=\ldots$; $\mu=\hat k_L\!\cdot\!\hat k_S$. Both labels give the same, label-independent monopole $-5\eps/6$."* The immediately preceding object is `f_δN^fin`, whose monopole is `−5`, not `−5ε/6`; the intended subject is `f_map`. Name it.

**N18 — No Zenodo/archival DOI for the cited scripts (whole manuscript).** `grep -i "zenodo\|doi"` on `main.tex` returns nothing. All reproducibility anchors are GitHub paths + commit hashes on a repo the author controls. This is a standing item (R1 PSU-16, R2 C22) and I record it as unchanged in v1S.0.8 rather than as new; PRD will ask.

**N19 — Length/venue.** 6 pages. `DISPOSITIONS/PSU.md` records the target as "Physical Review D — Letter / short note" and the R1/R2 artifacts as 4 pp. If PRD Letter is still the target, the note is now over length; if it has become a Brief Report/regular article, the venue line should be updated and the framing checked against that format.

---

## Nits

- `isoceles` → `isosceles` (l. 89 and l. 90, twice).
- British `labelled` (×6), `labelling` (l. 165), `normalisation` (×2) against PRD's American house style.
- Abstract says *"a monopole gap of $25/8$"*; Sec. III says *"the identification error, $-5-(-15/8)=-25/8$"*. Same quantity, opposite sign convention.
- A5 says *"correcting the weight closes the gap $5(6-\epsilon)/24$"*; the two printed formulas differ by `5(ε−6)/24`. Sign convention again.
- Italic `$I$` in `1 − I/3` (Eq. 2, and throughout Sec. III) is hard to distinguish from `1` at body size in the rendered PDF. Consider `\mathcal{I}` or `\bar\epsilon`.
- Table I caption *"(constant $\eps$, $c_s=1$ except USR)"* — ambiguous whether "except USR" attaches to constant ε (intended) or to `c_s=1`.
- Table I's USR row is annotated *"(not computed here)"* yet carries five printed entries; move the annotation to the `result` cell or to a footnote.

---

## What I verified as CORRECT (do not re-flag next round)

Re-derived independently, by hand, before consulting any source note:

| Claim | Location | Status |
|---|---|---|
| `NK = d/dt ln√h\|_wl − ∂_iN^i` ⇒ Eq. (1) | A1 | ✅ (modulo N10) |
| `∂_iN^i = (ε/c_s²)ζ̇ − ∇²ζ/(a²H)` | l. 127–130 | ✅ from `ψ = −ζ/H+χ`, `∂²χ = a²(ε/c_s²)ζ̇` |
| `I = ε`, `λ = 1−ε/3 = 1/2` at ε=3/2 | Eq. (2), Table I | ✅ |
| `λ = (1−w)/2`; `f_map^fin = −(15/8)(1+w)(1−μ²)`; monopole `−(5/4)(1+w)` | Eq. (5) | ✅ |
| Eq. (4) second equality **sign** | l. 158–160 | ✅ **R2 C2 is genuinely fixed** |
| `f_map^init` monopole = `f_map^fin` monopole = `−5ε/6` | Eqs. (3)–(4) | ✅ |
| `f_δN^init = f^in-in/λ + f_map^init ≡ −5` identically in (ε, μ) | l. 153, A3 | ✅ exact cancellation verified |
| `f_δN^fin = −15(ε−4)/(4(ε−3)) + 15εμ²/(4(3−ε))`; `−25/4+(15/4)μ²` at ε=3/2 | l. 162–163 | ✅ |
| `f^in-in(μ,ε) = (5/12)(ε²μ²−ε²+6ε−12)` → `−35/16+(15/16)μ²` at ε=3/2 | A4 | ✅ |
| in-in monopole `−(5/18)(ε−3)(ε−6) = −15/8`; vanishes at ε=3 | l. 180–181, l. 260 | ✅ |
| gap `−25/8`, ratio `8/3`; the `×2` alternative → `−15/4`, gap `−5/4`, ratio `4/3` | l. 96–98, l. 260–262 | ✅ **R2 C4 is genuinely fixed** |
| `λ_USR = 1 + ε_f/3 − √(ε_sε_f)/3` | l. 140–142 | ✅ derived from scratch: `I = √(ε_sε_f) − ε_f` |
| Maldacena `(5/12)(1−n_s)` sign | Table I | ✅ |
| **A2's five contributions sum exactly to Eq. (4)** (const part `−5ε/4`, μ² part `+5ε/4`) and to monopole `−5ε/6`; each quoted per-contribution monopole correct | A2 | ✅ strongest single check in the paper |
| A5 admixture: `M(0)=0`, `f_map(g) = (gλ₁/λ_g)f_map(1)`, `f_map(0)=0` | A5 | ✅ internally consistent |
| Closing-amendment arithmetic chain `f^in-in/λ′ = 5(ε−6)/12` → `5(2ε−15)/24` / `5(ε−7)/8`, gap `5(ε−6)/24` | A5 + adjudication note | ✅ exact |
| `λ′ = 2λ` on the linear growing mode, `3λ` on `ζ₂ ∝ a^{−2(3−ε)}` | adjudication note §4 | ✅ self-consistent given `ζ₂`'s time dependence |
| All 4 printed SHA-256 prefixes match on-disk files | Reproducibility | ✅ `21668ab6`, `4e2a49be`, `4f641022`, `f4164019` |
| Both cited commits resolve; all cited artifact paths exist on `main` | Bib [23],[24] | ✅ |
| PDF byte-identical across `site/out/`, `site/public/`, `public/` | directive G | ✅ |
| Zero undefined references / citations | `main.log` | ✅ |
| Θ now defined (l. 295); five contributions now listed (A2); Fig. 1 caption now correct; Li–Quintin–Wang–Cai now cited [8]; refs [6]/[7]/[13]/[14] now correct; abstract no longer calls `−5` "the in-in monopole" | — | ✅ R1/R2 closures confirmed landed |

## Limitations of this review (stated, not hidden)

1. **I did not re-solve the second-order ADM constraints.** I verified that the five contributions A2 *lists* sum exactly to the printed Eq. (4) and to the `−5ε/6` monopole, and that the composition with the printed general-ε in-in shape is identically `−5`. I did not independently derive the non-local `psi2` kernel, which is the hardest of the five. A wrong `psi2` that happened to sum correctly is not excluded by my check.
2. **I did not independently derive `A₂ = ε(3−ε)²/3`.** I checked that the adjudication note's arithmetic chain is exact and that its `ε→0` exclusion argument for `2(3−ε)²` is sound in structure, and that the resulting `5(ε−7)/8` follows. I did not re-run the Hamiltonian-constraint solve. Consequently I can confirm the *internal contradiction* in E1 and that the appendix's value follows from the note's premises, but I cannot independently certify `−55/16` as physically correct.
3. **Journal/volume/page data** for the bibliography were checked against recall only; I had no network access to verify [8], [10], [11], [14] against INSPIRE. N16 is the only reference item I am confident about.
4. **I did not execute the sympy scripts.** File existence, SHA-256 prefixes, and commit hashes were verified on disk; script *output* was not re-run.
5. **M4's factor of 2** is reported as an undefined convention, not as an error, precisely because the totals check out. I could not resolve it from the manuscript, which is the finding.

## Integrity note

Every algebraic claim in the "verified as CORRECT" table above was derived by me from the paper's own stated premises before I opened the corresponding source note, and the source notes were then used only to check provenance and to trace E1's history. `DISPOSITIONS/PSU.md` and the R1/R2 truth audits were read **last**, solely to separate genuinely-new findings from re-flags (N13 and N18 are recorded as re-flags on that basis). I was not told an expected verdict and did not consult SSOT, the site, or the campaign status board. Where I could not verify a claim I have said so above rather than asserting a conclusion.

**Process observation (not a paper finding):** `project-context/peer-reviews/DISPOSITIONS/PSU.md` still records "Current paper-local version: `v1S.0.2`" with the v1S.0.2 SHA-256 and "4 pp." — six versions stale. E1 is exactly the class of defect a current ledger would have caught: a science amendment (S9/S9c/A2) landed in the appendix, and nothing cross-checked the main text for the value it superseded.
