# A3M v3M.0.24 — R9 truth-audit (2026-09-18)

**Stop-lift basis.** Rounds were STOPPED on A3M after v3M.0.18 under directive R2,
"next board only after a science decision on row 19". `NEXT_SCIENCE_LEDGER.md` row 19
now reads **"DONE 2026-09-04 — NO-GO GENERALISED"** (decision `D-A3-14`,
`PAPER_LINEAGE_2026-08-05.md`; artifacts `research/track_a3_multichannel/row19_lambda/`).
The stop condition is met, so exactly one new board (R9) is authorized, plus one
confirmation board if R9 closes ≥1 real item.

**Exact artifact under review.** `research/track_a3_multichannel/paper/main.pdf`
sha256 `e0e923d6bdbc4eef7a1a57422e32e744c6f37c65258213166a579ec622d028c4`,
md5 `b29ebb90be09f8d0bbc3875647bb150a`, 19 pp.
Served copies `public/papers/a3_multichannel_arxiv_v3M.0.24.pdf` and
`site/public/papers/a3_multichannel_arxiv_v3M.0.24.pdf` — both md5-identical (verified).
Convex `paperVersions` current row md5 `b29ebb90be09f8d0bbc3875647bb150a` — identical.
Preflight receipt: `ROUND_.../preflight_receipt.json` (verdict PASS, core_sha256 `d7d4b7c5…`).

**Legs (INT only; no EXT browser round, no Codex — Directive N + Portfolio Decision 2026-09-02 #6).**

| leg | model | verdict (verbatim from raw) | raw findings | raw path |
|---|---|---|---|---|
| Grok_brutal | grok-4.3 | **REJECT** | 20 (9 E / 5 M / 4 m / 3 N, incl. pass-2) | `../ROUND_2026-09-18-A3M-v3M.0.24-EXACTPDF-e0e923d6-R9VERIFY_A3M_Grok_brutal.md` |
| Gemini_cosmology | gemini-3.1-pro-preview | **MINOR REVISIONS** | 8 (4 E / 3 M / 1 N, incl. pass-2) | `../ROUND_2026-09-18-A3M-v3M.0.24-EXACTPDF-e0e923d6-R9VERIFY_A3M_Gemini_cosmology.md` |
| Claude Fable 5.1 (INT referee) | fable-5.1 | *(see §Fable below)* | — | `A3M_v3M.0.24_R9_claude_fable_2026-09-18.md` |

No leg FAILED; both API raws carry a wall time, review-packet hashes and a
rendered-PDF confirmation. Verdict words are transcribed from each raw's own
recommendation line — never inferred, never softened.

---

## GENUINELY-NEW-REAL findings (must close before any convergence claim)

### `DA3M-R9-01` (MAJOR — reproducibility gate): the pinned commit contains none of the cited artifacts
- **Raised by:** Grok E7 (its verified kernel; its "units/masks inconsistent" sub-claim is falsified below).
- **Verified independently.** `main.tex:1782-1786` pins the reproducibility statement to commit
  `68309c8` and publishes two tree URLs at that commit. `68309c8` is
  `review(P1N,P4P): R3 verification …`, dated **2026-09-02**. Checked with
  `git cat-file -e 68309c8:<path>` for every artifact the statement names:

  | artifact cited in the statement | at `68309c8` |
  |---|---|
  | `research/theory_audit/fnl_monopole_adjudication_2026_09_03.md` | **MISSING** |
  | `research/cubic_bounce_transmission/lane9a_velocity_dip`, `lane9b_s2_regulation`, `lane9b2_s2_rawadm`, `lane9c_abs_operator`, `lane9c2_lqc_modes` | **MISSING** |
  | `research/cubic_bounce_transmission/row18a_s2_tensor`, `row18b_cs_bounce_cubic` | **MISSING** |
  | `research/track_a3_multichannel/row10_r_ns`, `row14_cs_window`, `row19_lambda`, `row11_pbh_residuals` | **MISSING** |
  | `research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md` | **MISSING** |
  | `research/desi_png_reproduction` | **MISSING** |

  All of them are present at `origin/main` = `50cccd95` (2026-09-18, verified with the same
  command). The pin simply predates the work it claims to pin: the paper's own §VIII cites
  `row19_lambda/` (created 2026-09-04) and Sec. II / App. A cite the A2 adjudication
  (2026-09-07). A referee following the paper's published reproducibility pointer today finds
  **nothing**. This is a hard directive-Q2 failure and blocks readiness uplift.
- **Closure:** re-pin to a commit that is on the public remote *and* contains every cited
  artifact (`50cccd95` or the commit that lands this bundle, once pushed), and state the pin
  once rather than twice. Verify afterwards with `git cat-file -e <pin>:<path>` over the full
  artifact list, not by eye.
- **Why a link check missed this.** Both published URLs return HTTP **200** (curl-verified
  2026-09-18) because the two *parent* directories do exist at `68309c8` — it is their
  contents that postdate the pin. `/artifact-link-verify`-style status checking is therefore
  insufficient here; the verification must be per-artifact (`git cat-file -e <pin>:<path>`).
  The replacement pin is live: `…/tree/50cccd95/research/track_a3_multichannel/row19_lambda`
  returns 200 **and** contains the artifact.
- **Fingerprint:** reproducibility pin, 68309c8, stale commit, tree URL, artifacts absent at pin.

### `DA3M-R9-02` (MAJOR-lite — scope): the no-go's constant-$c_s$ / $s=0$ restriction was dropped along with the $\lambda$ qualifier
- **Raised by:** Grok M1 + M5 (same item, raised twice).
- **Verified, and it is a REAL residual of an incomplete `DA3M-R8-01` closure — not a re-flag.**
  `DA3M-R8-01`'s own fingerprint was "the $k$-essence no-go silently assumes `λ (P_XXX) = 0`,
  **`s = 0`, `η_sr = 0`**". Decision `D-A3-14` proved **$\lambda$-independence only**
  (`row19_lambda/results.json`: `/bounce/lambda_vertex_is_odd_in_eta = True`,
  `max_abs_total_over_L0_minus_1 = 2.83e-07`), yet `v3M.0.19` dropped the **whole**
  "`lambda=s=0`" qualifier (SSOT v3M.0.19 section, verbatim: *"The `lambda=s=0` qualifier is
  dropped from the abstract, Sec. VIII, and Next steps"*). The $s=0$ half was never proved.
  The artifact still records the restriction: `row19_lambda/results.json` →
  `/bounce/scheme = "S1 geometric, eps_eff = 1/2, eta_sr = 0, s = 0, k eta_B = 1e-3"`.
- **What the manuscript actually says now.** The derivation is honestly scoped in the body —
  `main.tex:1322-1324` ("for the dust contraction with **constant** $c_s$") and `:1405-1407`
  ("no **constant-$c_s$** value keeps both … within current bounds"). But the summary claim
  sentence `:1443-1447` and the abstract `:60-64` state the exclusion "for the full $P(X)$
  $k$-essence class … independently of the cubic coefficient $\lambda$" with **no** constant-$c_s$
  / $|s|\ll1$ qualifier. The only place $s$ appears is inside the $\lambda$-cancellation argument
  (`:1442`). A generic $P(X)$ model has time-dependent $c_s$; the claim as worded is broader than
  the computation behind it.
- **Closure:** restore the restriction to the claim sentence and the abstract — the no-go is
  established for the full $P(X)$ class **at constant sound speed** ($s=\dot c_s/(Hc_s)=0$,
  $\eta_{\rm sr}=0$), $\lambda$-independently; a time-dependent $c_s(\eta)$ is outside the present
  computation. No number changes; this is a scope statement, not a science change.
- **Fingerprint:** constant c_s, sound-speed running s, eta_sr, full P(X) class, time-dependent c_s, no-go scope.

### `DA3M-R9-03` (minor — provenance/leak): internal ledger-row and lane labels in body prose
- **Raised by:** Gemini E3.
- **Verified:** `main.tex:1331` "row 10's $r=24$", `:1397` and `:1401` "row 14's …",
  `:1667` (Appendix A table) "comoving $\delta N$ (lanes A/B/C)". No such rows or lanes exist in
  the manuscript — they are `NEXT_SCIENCE_LEDGER` rows and internal lane names. Directive-G item 9
  (leak gate) forbids internal process language in paper prose. `DA3M-08` swept 14 ledger/round
  tags at v3M.0.18 but missed these four.
- **Closure:** replace with the in-paper cross-reference or the value itself.

### `DA3M-R9-04` (minor — directive Q1): drafting-history parenthetical in Appendix A.2
- **Raised by:** Gemini E2. **Verified:** `main.tex:1710` — *"(An earlier draft of this appendix
  printed …; both numbers above are correct, the label was mixed.)"* A published work must not
  narrate its own earlier error (directive Q1). The corrected physics stays; only the narration goes.
- **Closure:** delete the parenthetical, keep both labelled maps.

### `DA3M-R9-05` (minor — presentation): raw script/JSON paths inline in body prose and captions
- **Raised by:** Gemini E1. **Verified:** 12 occurrences outside the Reproducibility statement —
  `main.tex:329, 684, 747, 761, 843, 992, 1036, 1038, 1089, 1110, 1229, 1766`
  (e.g. `\texttt{outputs/pbh\_compaction\_fnl.json}`, `\texttt{pta\_gamma\_reproduce.py}`,
  `\texttt{research/theory\_audit/a2\_lapse\_monopole\_adjudication\_2026\_09\_07.md}`).
  PRD keeps artifact pointers in the reproducibility/data-availability section.
- **Closure:** move the pointers into the Reproducibility statement (which already names every one
  of them) and leave the body/captions referring to them by result, not by filename.

### `DA3M-R9-06` (minor — undefined symbols): $T_3$ and $T_4$ used without definition
- **Raised by:** Gemini E4. **Verified:** used at `main.tex:1662` ("cancels between varied legs of
  $T_4$"), `:1672` ("the $T_3$ bulk coupling"), `:1684` — never defined anywhere in the paper.
- **Closure:** define both at first use in Appendix A.2.

### `DA3M-R9-07` (minor — presentation): the PTA marginal's $\pm0.382$ vs its own $68\%$ interval
- **Raised by:** Gemini M3.
- **Verified against the committed chain, and both printed numbers are CORRECT** —
  `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy` (320 000 × 2):
  mean `2.5665`, std `0.3818`, percentiles 16/50/84 = `2.3041 / 2.5913 / 2.8822`
  (68 % half-width `0.2891`), skew `−1.099`, min `0.1501`. So there is **no arithmetic error**:
  the posterior is strongly left-skewed, which is exactly why the standard deviation exceeds the
  68 % half-width. But the paper prints `γ = 2.567 ± 0.382` and `68% interval [2.304, 2.882]` in
  adjacent clauses (`:657-663`) with nothing to reconcile them, so a referee reads it as an
  inconsistency — as this one did.
- **Closure:** one clause noting the low-$\gamma$ tail (skew $-1.10$) makes $\sigma>$ the 68 %
  half-width. Verified statement, no new computation.

### `DA3M-R9-08` (minor — numerical provenance): transmitted-amplitude numbers carry no stated tolerance
- **Raised by:** Grok E5 (its verified kernel; its "statistical significance of the S1/S2 0.035
  difference" sub-claim is a category error — schemes are not draws from a distribution — and is
  falsified).
- **Verified:** `T_{f_NL}` = 0.165 / 0.250 / 0.196 and $\Delta f^{\rm bounce}$ are quoted to 3 s.f.
  with no accuracy statement anywhere in §III (grep for tolerance/convergence/relative-error over
  `main.tex:350-610` returns nothing). The tolerances **do** exist in the committed artifacts:
  `row18b_cs_bounce_cubic/results.json` → `backgrounds/{quintin,lqc,poly}/gate_cs1/rel_diff` =
  `3.29e-06 / 3.16e-06 / 3.86e-06`; `row19_lambda/results.json` →
  `max_abs_total_over_L0_minus_1 = 2.83e-07`.
- **Closure:** state the measured agreement (≲4×10⁻⁶ on the $c_s=1$ gate, all three backgrounds)
  in §III. Cited from the artifacts — nothing newly computed.

### `DA3M-R9-09` (nit): Fig. 1 frequency axis does not say the frequency is the present-day observed one
- **Raised by:** Grok N2/N3. **Verified:** caption `main.tex:833-843` says only "$f$"; the
  generating script is explicit that it is today's frequency
  (`sigw_nhz_from_lab_spectrum_2026_09_04.py:38` "Today's amplitude", function
  `omega_gw_today_h2`). One-word caption fix.

### `DA3M-R9-10` (nit): "essentially the single-field value this section excludes"
- **Raised by:** Gemini M2. **Verified:** `main.tex:1474`. Replace the intensifier with the number
  ($r=24$).

### `DA3M-R9-11` (nit): `$p=1.6$` reads as a p-value beside a $\sigma$ distance
- **Raised by:** Gemini M1. **Verified:** `main.tex:1184`. Name the parameter at first use.

---

## FALSIFIED (source-cited; do not re-open without new evidence)

| id | claim | why it is false |
|---|---|---|
| Grok E1 | "Dated: September 7, 2026" is an anachronistic internal artifact | It is the true compile date of this exact PDF (`\paperTimestamp`, `main.tex:19`). Same fingerprint falsified at R8 ("the date is the true compile date"). |
| Grok E2 | PRD requires a labeled abstract; this paper has none | `main.tex:37` is `\begin{abstract}`; revtex4-2/PRD renders the abstract **unlabeled by design**. Rasterization artifact of the image-fed leg. |
| Grok E3 | abstract's no-go is stronger than the body because $\lambda$-independence is "an additional assumption" | Inverted: $\lambda$-independence is **proved**, not assumed (`row19_lambda`, `D-A3-14`; `lambda_vertex_is_odd_in_eta = True`, residual `2.83e-07`). The genuine scope gap is the **constant-$c_s$** one, tracked separately as `DA3M-R9-02`. |
| Grok E4 | "from-scratch"/"independent" unsupported because no new Feynman rules are derived | Category error: "from-scratch" denotes an independent recomputation, not a new formalism. The novelty claim was already narrowed at R5 to **per-vertex attribution** (Table I) plus locating the Cai et al. factor of two — neither is in Li+2016 or Quintin+2015. OPINION/GENRE at most. |
| Grok E6 | Table IV juxtaposes non-comparable $\sigma$ without the required qualifier | The Table IV caption carries it verbatim: `main.tex:675-681`, "…the refit is a secondary, differently-conditioned cross-check, **not directly comparable** to it." Also at `:531` and `:1535`. Same fingerprint falsified at R8. |
| Grok E8 | "ratio is 1.84 ± 0.03" is unsupported; Table V says 1.732 | The paper prints **both** and says which is which: `:938` (144-point shape-resolved grid, `1.84 [1.76,1.89]`, std 0.03) and `:944`, `:997-1002`, `:1022` (27-point committed grid, `1.732 ± 0.050`, range `[1.610,1.809]`), with `:999` stating the narrower one "**must not be quoted as**" the headline. Same fingerprint as `R8-06`, closed at v3M.0.18. |
| Grok E9 | $\sigma=0.53$ and $1.20\sigma$ are arithmetically inconsistent with 0.6 and 0.382 | Grok used 0.6 as a $1\sigma$ width. `main.tex:637-640` states the interval type explicitly — NANOGrav quote $3.2^{+0.6}_{-0.6}$ as a **5–95 %** interval, Gaussian-equivalent $1\sigma = 0.6/1.645 = 0.365$. Auditor's own arithmetic: $\sqrt{0.365^2+0.382^2}=0.5283$; $0.633/0.5283 = 1.198 \to 1.20\sigma$. The paper is right. |
| Grok M2 | 1.84 is a log-log artifact; true ratio varies 1.67–1.81 | Grok's own range contradicts the tabulated `[1.610, 1.809]` (`:1022`) and is sourced to nothing. The grid distinction is already disclosed (see E8). |
| Grok M3 | the $5.1\sigma$ headline is really $4.9\sigma$ once the asymmetric error is folded | The quoted error is symmetric ($\pm0.6$), so there is nothing to fold. Auditor's arithmetic: $(5.070-3.2)/0.365 = 5.12$. Moreover **$4.9\sigma$ is the paper's own dust-bracket value**, printed beside $5.1\sigma$ in the Fig. 1 caption (`:838-840`, "$5.1\sigma$ ($4.9\sigma$)"); Grok mistook the paper's second number for a correction to its first. |
| Grok m1 | Table I caption omits the configuration | The caption states it: "**Squeezed-limit** contribution of each cubic vertex … $\lim_{k_1\to0}$" (`:tab:vertices` caption). |
| Grok m2 | $r_{\rm mix}$ introduced without a defining equation | Defined in full at `main.tex:373`: $r_{\rm mix}=-9i\mathcal A^2 I_\infty/k^3=\beta_-I_\infty/\alpha_-$, with $\alpha_-,\beta_-$ named on the next line. |
| Grok m4 | no statement that the same $T_{f_{\rm NL}}$ normalization is used on all three backgrounds | `main.tex:374-377` fixes the vacuum normalization explicitly ($1+2r_{\rm mix}$; $C_1=\alpha_-(1+r_{\rm mix})$, $C_2=\beta_-$) inside the single $T_{f_{\rm NL}}(\eta_h)$ formula applied to all three. |
| Grok N1 | "the the" appears on p. 3 | `grep -n "the the" main.tex` → no match. |
| Grok E7 (sub-claim) | manifest lists files whose units/masks are inconsistent with the body | Unsupported; `row11_pbh_residuals` is cited coherently at `:1870-1873` for exactly the §V $\gamma_{\rm cr}$ scan Grok names. Only the **pin** is defective (`DA3M-R9-01`). |
| Gemini N1 | "and and (vii)" in §IX.C | `grep -n "and and" main.tex` → no match. |

## OPINION / GENRE (venue pass only, not review items)

- **Grok M4** — "19 pp is disproportionate; PRD regular articles are 8–12 pp." A length preference,
  not a defect; PRD regular articles have no such cap and the paper carries four channels, a no-go,
  and two appendices. Recorded, not actioned.
- **Grok m3** — "no sympy script is deposited". They are deposited and named in the Reproducibility
  statement; the real problem is that the pin makes them unreachable, which is `DA3M-R9-01`.

## Verdict-word note (integrity)

Grok returned **REJECT** while Gemini returned **MINOR REVISIONS** on the *same* exact PDF, and
Grok's rejection rests on E1/E2/E8/E9 — four items this audit falsified against the manuscript's own
text and the auditor's own arithmetic. That is pattern-066 referee variance, recorded, **not**
treated as either an exit condition or grounds for dismissing Grok: Grok's E5 and E7 kernels are two
of the three highest-value findings of this round, including the only MAJOR. Per directive P, verdict
words are diagnostic feedback; the gate is 0 genuinely-new-real findings outstanding.

---

# Fable leg (INT referee, fable-5.1) — **MAJOR REVISIONS**, 2 MAJOR / 14 minor / 6 questions

Raw: `A3M_v3M.0.24_R9_claude_fable_2026-09-18.md`. Integrity note in the raw confirms it opened no
prior review material, no SSOT, no dispositions and no ledger; it verified its numbers by its own
derivations, by executing/reading the named committed artifacts, and by fetching Li *et al.*
arXiv:1612.02036. This is the highest-yield leg of the round.

## GENUINELY-NEW-REAL (MAJOR)

### `DA3M-R9-12` (MAJOR — internal inconsistency): Eq. (15) is Li *et al.* Eq. (5.1), not Eq. (4.19), and already contains $\lambda$ on the matter-contraction line
- **Auditor's independent verification (sympy, this session), not taken on the leg's word:**
  the general-$\lambda$ squeezed amplitude recorded in the lab's own
  `row19_lambda/results.json` is
  `f_NL_squeezed_of_cs_L = -245/16 + 105/(8 c_s^2) - 30 L`. Substituting the matter-contraction
  line $L=\lambda/\Sigma=(1-c_s^2)/(6c_s^2)$ gives **exactly** $-165/16 + 65/(8c_s^2)$ — i.e.
  precisely the paper's Eq. (15). Verified symbolically: `simplify(gen.subs(L, li_line) - Eq15) == 0`.
  And the cancellation value the paper quotes, $\lambda/\Sigma = 7/(16c_s^2)$, is recovered only
  from the $\lambda=0$ baseline: `solve(105/(8 c_s^2) - 30 L, L) = [7/(16 c_s^2)]`
  ($7/16 = 105/(8\cdot30)$).
- **Therefore the printed chain in §VIII is inconsistent with itself:** Eq. (15) is presented as
  the $\lambda$-free baseline "from their Eq. (4.19)", and the next paragraph adds $-30\lambda/\Sigma$
  to it and scans "the matter-contraction line $\lambda/\Sigma=(1-c_s^2)/(6c_s^2)$" — which
  double-counts $\lambda$ on exactly that line. Two further printed statements are wrong as worded:
  $-30\lambda/\Sigma$ is called "**the constant** $-30\lambda/\Sigma$", but on both named lines
  $\lambda/\Sigma\propto1/c_s^2$ is not constant in $c_s$ (it is constant in *shape* — a purely
  local $\sum k_i^3$ term — which is what was meant); and the $\lambda=0$ form
  $-245/16+105/(8c_s^2)$, from which the DBI result $r_{\min}=12.57$ and the $7/(16c_s^2)$ value
  are actually measured, **appears nowhere in the paper**.
- **Status:** the *conclusion* is correct on the artifact ($\lambda$-independence of $r$ and of
  $\Delta f^{\rm bounce}$ is proved; no $\lambda$ opens the window) — this is **not** a science
  error and `D-A3-14` stands. It is a presentation/attribution defect that makes the headline
  no-go unverifiable from the PDF alone. **MAJOR because a referee cannot check the paper's
  central claim from the paper.**
- **Closure:** print the general-$\lambda$ form as the primary equation with its $\dot\zeta^3$-vertex
  origin (Li *et al.* Eq. 4.18), state that Eq. (15) is its specialization to the $P\propto X^n$
  line citing Eq. (5.1)/(A.20), re-word the scan so every number is measured from the $\lambda=0$
  baseline, and replace "constant" with "purely local-shaped ($\sum k_i^3$)".
- **Fingerprint:** Eq. 15 attribution, Li Eq. 4.19 vs 5.1, general-lambda form -245/16 + 105/(8cs^2) - 30L, double-counting lambda on the matter line, 7/(16 cs^2).

### `DA3M-R9-13` (MAJOR — claims at evidential strength, VISION R6): $f_{\rm NL}^{\rm after}=1.0$–$1.4\times10^{11}$ is printed without noting that perturbative control is long gone
- **Auditor's independent verification:** at $c_s=1.5\times10^{-3}$ the bounce term
  $\propto\rho_B/c_s^4$ evaluates to $1.38\times10^{11}$ — the paper's number **reproduces**, so
  there is no arithmetic error. But with $\zeta_{\rm rms}=\sqrt{A_s}=\sqrt{2.1\times10^{-9}}
  =4.58\times10^{-5}$, the tree-level expansion parameter $f_{\rm NL}\zeta$ reaches unity at
  $|f_{\rm NL}|\approx2.2\times10^{4}$ — about **seven decades below** the printed value. The
  manuscript already owns the tool: §V B applies a perturbativity criterion $1.2|f_{\rm NL}|\sigma$.
  It is simply never applied here.
- **Why this is real and not genre.** The number appears in the abstract, in §VIII and in Table VII
  row 2, and it is used to claim the no-go is "strengthened" ($6$–$9\times10^5 \to 1.0$–$1.4\times10^{11}$).
  That comparison is between two numbers neither of which comes from a controlled calculation.
  Directive Q1/VISION R6 require claims at exactly their evidential strength. The no-go itself is
  untouched — it is already secured by $r=24c_s$ alone and by the loss of perturbative control.
- **Closure:** state the perturbativity bound and the $c_s$ below which control is lost; recast the
  Table VII row and the abstract so the exclusion rests on (i) $r=24c_s$ and (ii) loss of
  perturbative control, not on a specific $10^{11}$ value; keep $c_s\ge0.624$ (where
  $|\Delta f^{\rm bounce}|\approx2.5$ and the expansion is controlled) as the one quantitatively
  meaningful edge. Drop the "$10^6\to10^{11}$ strengthening" framing.
- **Fingerprint:** perturbative control, f_NL zeta ~ 1, 1.0-1.4e11, Table VII row 2, tree-level validity, cs=1.5e-3.

## GENUINELY-NEW-REAL (minor) — Fable

| id | item | verification |
|---|---|---|
| `DA3M-R9-14` | "detectable only for $r\gtrsim23$" / "tensor-viable $r<11.5$" misuses "tensor-viable" (which means $r<0.036$ everywhere else in the paper) and reads as if $r$ were amplified through the bounce, contradicting §VII ($r_{\rm after}=r_{\rm before}$ in S1). Criterion behind "detectable" is an unstated $1\sigma$ crossing. | `main.tex:1470-1476`; §VII identity. REAL wording defect. |
| `DA3M-R9-15` | §IV D: "$T_B\gtrsim6\times10^9$–$6\times10^{10}$ GeV puts the whole NANOGrav band at $k\eta_B\le2.3\times10^{-8}$" — $2.3\times10^{-8}$ is the $T_B=10^8$ GeV value in `sigw_nhz…json`, not the value at the quoted temperature. | Conclusion unaffected (the true value is smaller, i.e. deeper inside validity); the printed pair is mismatched. REAL. |
| `DA3M-R9-16` | "$2.1$–$4.4$ dex" quoted for the **squeezed** LQC deficit at/below $k\eta_B\approx1.06$. | **Auditor checked `lane9c2_lqc_modes/results.json` → `abs_comparison/per_k`: the squeezed gaps at $k\eta_B=0.1/0.3/1$ are `4.413 / 3.235 / 3.075` dex.** 2.1 is not in that set. Quote **3.1–4.4 dex**. REAL. |
| `DA3M-R9-17` | Eq. (2): the bispectrum amplitude $\mathcal A(k_1,k_2,k_3)$ is never defined, though the whole §II C factor-of-two argument turns on its normalization. | Confirmed absent. REAL. |
| `DA3M-R9-18` | §VII calls $n_T=-0.035$ "a cheap, falsifiable discriminator"; no planned experiment reaches $\sigma(n_T)\sim0.03$ at tensor-viable $r$. | Overstatement. REAL — soften to "falsifiable in principle". |
| `DA3M-R9-19` | Table VII/abstract use Planck's **68%** interval as the exclusion boundary; the 95% edge is the referee-standard one. | `row14_cs_window/results.json` carries the 95% numbers. Adding them strengthens rigour and *weakens* the headline factor (∼416 → ∼240–265) — so it must be done, and the honest headline is the 95% one. REAL. |
| `DA3M-R9-20` | Table V caption cites `outputs/pbh_compaction_fnl.json` (27-point grid, 1.732) as the source of the headline $1.84\pm0.03$, which actually comes from `row11_pbh_residuals/results/row11_gammacr_extension.json` (144-point subset, 1.837 ± 0.031). | Auditor confirmed both files at R9. Mis-citation. REAL — and note it is the *citation*, not the number, that is wrong (cf. Grok E8, falsified). |
| `DA3M-R9-21` | §IV C injection test: recovered per-realization widths $\sigma_\gamma\approx0.16$–$0.17$ vs the real-data refit's $0.38$; four of five "realizations" are bin-bootstraps of one injection. It tests bias, not coverage, so it does not validate the $0.38$ that enters the $1.14\sigma/4.63\sigma$ statements. | Consistent with `pta_injection_30bin_realkde…json`. REAL — disclose the scope of what the test validates. |
| `DA3M-R9-22` | §III presents $T_{f_{\rm NL}}$ "ranges over $0.165$–$0.409$" in one sentence though $0.409$ is an S2 number, inviting an S1 reading. | REAL wording; Table III already separates them. |
| `DA3M-R9-23` | Abstract is **341 words** (auditor's own count on the `\begin{abstract}` block) — above the ≈300-word PRD-regular target the R6 closure trimmed it to (307). The no-go reframe re-inflated it. | REAL regression. |
| `DA3M-R9-24` | §VIII uses $s=39/16$ without ever defining $s\equiv\dot c_s/(Hc_s)$; Table VII header/row labelling. | REAL, trivial. |

## Carried as OPEN QUESTIONS (honest limitations, disclosed — not closed by edit)

Fable's Questions 1–6 and minors 9/10/13 are legitimate referee questions that the present
computation does not answer: the justification for the S1 dressed-metric prescription at
$c_s\ne1$ (Q1 — and this is the same object as `DA3M-R9-13`'s scheme caveat), the (A4) frozen-shape
handoff for a still-evolving non-attractor mode (Q2), the sense in which $f^c_{\rm NL}=-5$ is
"well-defined" given $N_i=O(1/k_L)$ (Q3), the injection-width question (Q4, same object as
`DA3M-R9-21`), the curvaton detectability criterion (Q5, same object as `DA3M-R9-14`), and the
window-asymmetry robustness of $\Delta f^{\rm bounce}$ (Q6). Minor 9 (showing Cai *et al.* Eq. (37)
under both readings) and minor 10 (Quintin *et al.*'s attribution) are verification requests the
leg explicitly flagged as *not verified*; minor 13 ($\Omega_{\rm DM}=0.674$) fingerprint-matches the
R5 disposition that closed it with a quantified factor-2.55 footnote — **RE-FLAG-OF-DISCLOSED**,
though Fable is right that a footnote is the wrong home and it should move into the main text.

These go to §IX C (the paper's own open-items list), not into fabricated answers. Per
`/never-fabricate-derivation`, no question above is to be "closed" by writing a derivation that
was not computed.

---

# R9 round tally (all three legs)

| class | count |
|---|---|
| **GENUINELY-NEW-REAL** | **24** — 3 MAJOR (`R9-01` repro pin, `R9-12` Eq. 15 chain, `R9-13` perturbativity), 1 MAJOR-lite (`R9-02` constant-$c_s$ scope), 17 minor, 3 nit |
| RE-FLAG-OF-DISCLOSED | 2 (Grok E8/E6 fingerprints closed at v3M.0.18; Fable minor 13 → R5) |
| FALSIFIED | 14 (table above, each source-cited) |
| OPINION/GENRE | 2 (Grok M4 length, Grok m3) |
| Carried open questions (disclosed limitations) | 6 + 2 verification requests |

**Clean-wave count: 0 — R9 is NOT a clean wave.** The R2 convergence budget permits one
confirmation board after these close; that board is the one authorized re-test, and it must run on
the exact v3M.0.25 PDF.

**Readiness consequence (directive P, computed not chosen).** With 3 MAJOR + 1 MAJOR-lite open on
the current exact PDF, the automated-review-convergence gate is **not** met, so A3M cannot sit at
95. The Convex cap stays **75** until the closure bundle lands and the confirmation board returns
0 genuinely-new-real. The SSOT frontmatter's `headline_pct … = ~95` was already wrong before this
round (it asserted gate completion while `submission_status` said "readiness 75 — ROUNDS STOPPED");
R9 settles the contradiction in favour of **75**, on evidence.
