# P1A R-round adversarial review — GPT-5 (statistical-methodology, Gelman/Vehtari profile)

**Reviewer persona:** OpenAI GPT-5 in Gelman/Vehtari adversarial-statistician mode.
**Target:** `arxiv/paper1a_ech_nogo.tex`, v1A.0.19 (May 9, 2026), 1,425 lines.
**Scope:** four-route no-go theorem, ECH-specific dark-energy closure, cross-paper consistency.
**Prior context consulted:** `project-context/SSOT/paper-1/status.md` (R44 closures Wave 14-EEEE / IIII / JJJJ / NNNN; R45 BLOCKERs B1, B2 closures).

---

## Headline

**Total findings: 2 BLOCKER · 4 MAJOR · 6 minor · 3 nit.**

**Most concerning finding:** **P1A-R50-B1** — the §V Table II ‡-footnote (line 1075) makes a still-running computational claim that has gone stale: it asserts the new free-w0wa cobaya chain is "$\sim 109$ samples accepted as of 2026-05-08 18:27 PT, target $\hat R - 1 < 0.01$ still 1--3 days from publication-quality convergence." Per the standing project status this chain is actually at $\hat R - 1 \approx 0.095$ with a 5–15 day honest ETA after a pod IP rotation, and the chain has been running for over a week — the "1–3 days" promise in the footnote is the kind of stale, perishable promise that no published manuscript footnote should carry. This is fixable in ten lines of LaTeX but is BLOCKER-grade because the footnote is the load-bearing reconciliation between the abstract's no-w0wa claim and Paper I(b)'s in-flight chain, and it directly contradicts the lab's own honest R̂−1 trajectory.

The four-route theorem itself is structurally sound after the R45 B1/B2 fixes — the route 4 (R4) "$\sim 22$–$36$ orders of magnitude" framing now reconciles cleanly with the rigid $\rho_\theta \propto m_\theta^2$ relation, and the route 2 (R2) dimensional fix successfully replaced the bad $\dot\beta\,[\mathrm{eV}]$ vs $\sigma(\beta)\,[\mathrm{eV}]$ comparison with a clean dimensionless ratio. **The two R45 BLOCKERs are properly closed in v1A.0.19.** What remains is a layer of methodology issues that a Gelman-style referee would not let pass without explanation.

---

## BLOCKER (B) — must fix before submission

### P1A-R50-B1  Stale w0wa-chain status promise in the load-bearing reconciliation footnote

**Location:** §V Table II ‡-footnote, line 1075 (also abstract §I.A line 1067 row "Matter bounce ... not tested$^{\ddagger}$").

**Quote:**
> "A new DESI~DR2 + Planck~NPIPE + Pantheon$+$ + DES-SN5YR cobaya chain with the $w_0 w_a$ free-parameter extension is currently running on Pod~3 H200 ($\sim 109$ samples accepted as of 2026-05-08 18:27 PT, target $\hat R - 1 < 0.01$ still 1--3 days from publication-quality convergence; Paper~I(b) Table~IV row ``DESI DR2 w0wa (new)'')."

**Why this is a BLOCKER:** Published manuscript footnotes must not carry perishable run-state. The current honest project-level R̂−1 trajectory (per the SSOT, "Honest R-1 trajectory ... 5–15 more days") sits at $\hat R - 1 \approx 0.095$ on 5/11 — a *backward* step from 0.079 the day before. The "1–3 days" promise in the footnote was already a guess on 5/8, and at submission time will be wrong by orders of magnitude in either direction (chain still running, or chain converged but with different headline numbers). A statistician reading this footnote will immediately distrust every other quantitative claim in the table.

**Fix:** Replace the run-state sentence with a non-perishable framing:
> "A free-$w_0 w_a$ cobaya chain (DESI~DR2 + Planck~NPIPE + Pantheon$+$ + DES-SN5YR likelihoods) is in production but has not converged to the publication-quality threshold $\hat R - 1 < 0.01$ as of this manuscript version; the asymmetry between the Quintom-B accommodation row and the others in Table II is therefore one of theoretical accommodation, not posterior preference. When that chain converges, Paper~I(b) Table~IV row ``DESI DR2 w0wa (new)'' will replace this footnote with the posterior-preference verdict for all five rows simultaneously."

This is honest, non-perishable, and survives any chain-convergence outcome.

### P1A-R50-B2  Logical redundancy between the structural-tension argument and the 14-barrier closure is never reconciled

**Location:** §I abstract (lines 81–88), §I.A.2 (lines 204–208), §XIII (line 1208), §XIV.4 (line 1264), and conclusions §XV (no acknowledgement).

**Quote (abstract, lines 81–86):**
> "A structural incompatibility ... exists between the dark-energy mechanism, which requires $N_{\rm tot}\approx 92$ post-bounce $e$-folds, and the matter-bounce $\fnl=-35/8$ signature, which would plausibly be erased ... by that many $e$-folds; ECH is therefore not internally consistent as both a dark-energy generator and a matter-bounce host."

**Why this is a BLOCKER:** The 14-barrier catalog (§IX) explicitly claims to close *every* minimal-ECH dark-energy route. If that closure is rigorous, then there is no surviving "dark-energy mechanism" left to be in structural tension with anything. The structural-tension argument requires the dark-energy mechanism to be *live enough* for its $N_{\rm tot}\approx 92$ requirement to bind on the bounce-$\fnl$ predictor. The paper presents both arguments as load-bearing without ever saying which is the primary closure and which is the backup, or whether they jointly close a single failure mode by independent means.

A Gelman-style reader will read this as either (a) the 14-barrier closure is not as airtight as claimed (so the structural tension is needed as a backstop), or (b) the structural tension is rhetorical padding on an already-closed result. Neither is acceptable. **Fix:** add one paragraph in §XIV.4 (`sec:structural_tension`) stating explicitly:
> "The structural tension between $N_{\rm tot}\approx 92$ and the matter-bounce $\fnl$ signature is *not* an independent closure of the dark-energy route — that route is already closed by Barriers 1–14 (Sec.~\ref{sec:barriers}). It is reported here as a *consistency-of-no-go* observation: even if one were to grant the phenomenological scaling ansatz of Eq.~\eqref{eq:Leff_full} despite Barriers 5, 10, and the dimensional-counting gap of Appendix~\ref{app:dimensions}, the resulting scenario would still fail to host both observables simultaneously. The structural tension is therefore a *robustness check* on the 14-barrier closure, not a co-equal closure mechanism."

This reframing also removes the abstract's implicit claim that ECH "is therefore not internally consistent" — which is a strictly stronger claim than the 14-barrier closure already supports.

---

## MAJOR (M)

### P1A-R50-M1  Four-route theorem never declares its statistical/inferential framework

**Location:** §IV (lines 495–743), throughout.

The four routes are closed by amplitude-bound arguments. Routes R1–R3 close by Planck-scale suppression (factors of $M_{\rm Pl}^{-1}$, $M_{\rm Pl}^{-2}$, plus running coefficients). Route R4 closes by the rigid $\rho_\theta \propto m_\theta^2$ relation between birefringence amplitude and operator strength. Nowhere does the paper state whether these are:

- Frequentist exclusions at some implicit $\alpha$ level (and against what null?);
- Bayesian rejections of an implicit prior on a free-parameter manifold;
- Pure structural/algebraic statements that need no statistical framing because they hold exactly;
- Or order-of-magnitude amplitude inequalities, which is what the prose actually argues.

The only place "frequentist" appears is line 1084, in the PTA $\gamma$ discussion. A reader expects a no-go theorem to have a clean inferential structure. **Fix:** add one paragraph at the start of §IV (around line 503, after "we collect those four routes here and close each with the standard published derivation"):

> "*Inferential framework.*---The four route closures are amplitude-bound exclusions: each route generates a parity-odd or dark-energy contribution whose maximum amplitude, evaluated with the published one-loop or algebraic coefficients of the minimal ECH sector, is many orders of magnitude below the observed signal (R1, R2, R3) or rigidly tied to the birefringence amplitude in a way that forbids simultaneous dark-energy density and $\beta_{\rm obs}$ (R4). The closures are therefore not statistical hypothesis tests but operator-strength inequalities; the inferential question reduces to whether the operator coefficients can be enlarged within the minimal-ECH sector, and the answer is no because the coefficients are fixed by the LQG area spectrum (Barbero–Immirzi $\gamma$) and the Standard Model chiral content."

Without this, the paper looks like it is making a strong methodological claim ("no-go theorem") with no methodology.

### P1A-R50-M2  R4 closure number ambiguity: 22 OOM vs 36 OOM vs the "many orders of magnitude" abstract framing

**Location:** §IV.D (lines 690–695), abstract (no explicit number).

**Quote (lines 692–694):**
> "at $m_\theta \sim 10^{-22}$\,eV the overshoot is ${\sim}22$ orders of magnitude $(m_\theta/H_0)^2 \sim (10^{11})^2 \sim 10^{22}$, and at $m_\theta \sim 10^{-15}$\,eV the overshoot is ${\sim}36$ orders of magnitude $(m_\theta/H_0)^2 \sim (10^{18})^2 \sim 10^{36}$"

The R45-B1 fix correctly replaced the wrong "$\geq 8$ orders" claim with a range. Good. But: the abstract is now silent on the R4 closure amplitude, where it previously carried "the $\geq 8$ orders of magnitude" headline. A no-go theorem should carry the closure amplitude in the abstract. **Fix:** add one clause to the abstract (line 80, after "is closed by the 14 barriers of Sec.~\ref{sec:barriers}"):

> "The strongest amplitude bound comes from Route R4 (spectator-ALP birefringence): the same coupling that produces $\beta_{\rm obs}$ overshoots the dark-energy density by 22–36 orders of magnitude across the natural ALP mass range $m_a \in [10^{-22}, 10^{-15}]\,$eV, and matches $\rho_\Lambda$ only at the fine-tuned point $m_\theta \sim H_0$ — which re-imports the cosmological-constant problem rather than solving it."

This puts the closure verdict in the abstract where a referee can find it.

### P1A-R50-M3  R2 "factor-of-$\sim$100 ambiguity reflects $\varepsilon$-correction perturbative-order scaling alone" is a hand-wave

**Location:** §IV.B (lines 590–596).

**Quote:**
> "i.e.\ the one-loop induced $\beta$ is suppressed by $\sim 58$--$60$ orders of magnitude relative to the observed signal. (A complementary cross-check using $\alpha_{\rm em}/(4\pi\cdot M_{\rm Pl}\cdot(\alpha/M)\cdot\beta_{\rm obs})\cdot H_0$ as the dimensionless ordering yields a numerically distinct ratio of order $10^{-33}$; the two orderings differ in how the $H_0$ factor and the $M_{\rm Pl}\cdot(\alpha/M)$ product are contracted with the dimensionful coupling, but both land on the qualitative R2 closure ..."

A 27-order-of-magnitude discrepancy ($10^{-58}$ vs $10^{-33}$) between two "orderings" of the same dimensionless ratio is not "factor-of-$\sim$100 ambiguity." Either (a) one ordering is correct and the other is dimensionally wrong (in which case the paper should explain which and why), or (b) the two ratios are measuring different physical quantities (in which case naming them both "the R2 amplitude" is misleading). The current text reads as if the author tried two contractions, got wildly different numbers, and shrugged.

**Fix:** pick the dimensionally clean ordering, derive it once, and drop the other from the published text (it can live in a supplementary appendix if it has interpretive value). A statistician reading "two orderings differ by 25 orders of magnitude but both land on the qualitative closure" will mark the paper down.

### P1A-R50-M4  $\gamma_{\rm BI}$ "Fixed: 0.274" prior with $\pm 0.020$ uncertainty is self-contradictory

**Location:** Appendix A, Table III (line 1382).

**Quote (table row):**
> "$\gamma$ & Barbero-Immirzi & Fixed: 0.274 & $0.274\pm 0.020$ & LQG area spectrum"

The "Prior" column says "Fixed: 0.274". The "Verified Value" column says "$0.274\pm 0.020$". A fixed value has no uncertainty. Either the parameter is fixed (no uncertainty, single value) or it carries a prior with width (in which case the prior column should reflect that — e.g., "Gaussian: $\mathcal{N}(0.274, 0.020^2)$, scheme-dependent"). The $\pm 0.020$ in v1A.0.19 is meant to capture the ABCK-vs-DLM scheme dependence (per §II.A.1 lines 271–273), but that should be reflected in the prior, not in a "verified" measurement. **Fix:** change the prior column to "Discrete: ABCK 0.274 / DLM 0.2375 (entropy-counting-scheme-dependent)" and the verified column to "0.274 (ABCK, fiducial)" with a footnote pointing to §II.A.1.

---

## minor (m)

### P1A-R50-m1  Free-floating `\label{sec:conjunctive}` at line 800

**Location:** Line 800 (between §VII and §VIII).

```latex
\section{Falsification Criteria}\label{sec:falsification}
...
framework rather than falsifying it (details in companion Paper~I(b)~\cite{Golden2026P1b}).

\label{sec:conjunctive}


%% ============================================================
%%  8. RELATED WORK
%% ============================================================
```

The `\label{sec:conjunctive}` is a free-floating label with no preceding `\section`/`\subsection`/`\subsubsection`. In compiled output it will silently bind to the previous counter (§VII Falsification Criteria), so any `\ref{sec:conjunctive}` elsewhere would resolve to "Sec. VII" — which is wrong. The Wave 14-NNNN M5 orphan-label sweep missed this one. **Fix:** delete line 800 (no `\ref{sec:conjunctive}` exists anywhere in the manuscript so it is safe to drop).

### P1A-R50-m2  Quadruple-stacked `\label{}` on §IV header is dead scaffolding

**Location:** Lines 495–497.

```latex
\section{Four-Route No-Go: Why Each Standard ECH Channel Closes}\label{sec:derivations}
\label{sec:fourroute}
\label{sec:oneloopfull}\label{sec:condensate}\label{sec:cosmo_derivation}
```

Five labels on one section header, of which four are orphans (`sec:derivations`, `sec:oneloopfull`, `sec:condensate`, `sec:cosmo_derivation` have zero `\ref` targets). This is dead scaffolding from prior versions where the section was structured differently. Only `sec:fourroute` is actually referenced (twice, lines 220, 503). **Fix:** drop the four orphan labels; keep only `\label{sec:fourroute}`.

### P1A-R50-m3  Figure labels `fig:theory_map` and `fig:derivation` are never referenced in body text

**Location:** Lines 176 (`\label{fig:theory_map}`), 278 (`\label{fig:derivation}`).

Neither figure is referenced via `\ref{fig:...}`. In compiled PDF the figures float without an explicit "see Fig. X" call-out. **Fix:** add `\ref{fig:theory_map}` at the end of §I (around line 184) and `\ref{fig:derivation}` at the end of §II.A (around line 282).

### P1A-R50-m4  Abstract claim "ECH is therefore not internally consistent as both a dark-energy generator and a matter-bounce host" is rhetorically stronger than the proof

**Location:** Abstract, lines 84–86.

This claim relies on the structural tension being independent of the 14-barrier closure (see B2 above). Even granting that, "internally inconsistent" is a strong word — the proper statement is "internally over-constrained" or "the two observables cannot both be hosted at the same operating point in parameter space." Internal inconsistency in physics has a specific meaning (the theory derives $0 = 1$ or similar). **Fix:** replace with "ECH cannot host both observables simultaneously" or "the parameter regions hosting the dark-energy ansatz and the matter-bounce $\fnl$ signature are non-overlapping within the minimal-ECH framework."

### P1A-R50-m5  "$3$--$5\sigma$ realistic significance" for SPHEREx repeated four times without a single in-paper derivation

**Location:** Abstract (line 93), Table I (line 165), §VII (line 785), §XIII (line 1192).

The four sites are consistent with each other, but the derivation of the $3$--$5\sigma$ range lives entirely in footnote 1 (`fn:spherex_range`, line 785) and in Paper II. A reader who lands on the abstract has no way to verify the headline significance without flipping to §VII or to a different paper. **Fix:** in the abstract (after "SPHEREx at $3$--$5\sigma$ realistic significance"), add a parenthetical: "(post-systematic-budget Fisher forecast; see §VII fn.~\ref{fn:spherex_range} and Paper~II~\cite{Golden2026P2})". This is a small change that lets the reader trace the headline number.

### P1A-R50-m6  "Many orders of magnitude" hedge in R1 closure is below the dimensional standard of the rest of §IV

**Location:** §IV.A (line 540).

**Quote:**
> "$\rho_{\rm NJL} \sim \kappa\,n_\psi^2/m^2 \sim n_\psi^2/(m^2 M_{\rm Pl}^2)$, which for the largest plausible cosmic fermion densities at recombination or post-recombination is many orders of magnitude below the present-day dark-energy density"

R2, R3, R4 all carry quantitative order-of-magnitude figures (58–60 OOM for R2, $10^{-63}$ for R3, 22–36 OOM for R4). R1 carries "many." This is the weakest closure number in the four-route theorem and looks like it was not redone in Wave 14-IIII to match the other three. **Fix:** plug in $n_\psi(z=1100) \sim n_b \sim 10^{-7}\,{\rm cm}^{-3} \sim (10^{-10}\,{\rm eV})^3$ and $m \sim m_e \sim 5\times 10^5\,$eV (lightest fermion that contributes to a non-relativistic NJL density), and report the resulting OOM ratio. The text should read something like "$\rho_{\rm NJL} \sim 10^{-(N)}\,{\rm eV}^4$, suppressed by $\sim N$ orders of magnitude below $\rho_\Lambda \sim 10^{-11}\,{\rm eV}^4$." This brings R1 to parity with R2–R4.

---

## nit (n)

### P1A-R50-n1  Mixed "matter bounce" vs "matter-bounce" capitalization
Throughout — line 90 "matter-bounce class", line 1187 "matter-bounce $\fnl$", but line 794 "matter-bounce from slow-roll inflation". Pick one (hyphenated reads cleaner in PRD style) and apply globally.

### P1A-R50-n2  `\paperVersion` is `v1A.0.19` but `\date` line 62 says "May 9, 2026, 22:30 PDT --- \paperVersion" while the file header comment (line 4) says "Houston Golden -- 2026" with no specific date. Bring the comment header into alignment with the `\paperVersion` macro.

### P1A-R50-n3  `\cite{Heinrich:2023}` uses a colon-separated key while every other Golden-paper cross-reference uses no separator (`Golden2026P2`, etc.). Cosmetic. The bib file should be checked for whether `Heinrich:2023` and `Heinrich2023` are the same entry or two entries (latter would produce a silent duplicate citation).

---

## Cross-paper consistency check (per prompt question 10)

All four cross-paper cite keys (`Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`) are defined in `arxiv/references.bib` (lines 958, 966, 974, 982). All four are used in P1A. Cross-paper γ_PTA harmonization is clean: P1A line 1081 cites $\gamma = 2.567 \pm 0.382$ from real-KDE reanalysis, which matches the current canonical figure in `pipelines/p3_anomaly_engine/paper3_draft.tex`. The CLAUDE.md context block carries a stale γ = 3.20 ± 0.42 figure but the actual Paper 3 manuscript and Paper 1A both already use the real-KDE 2.567 ± 0.382 supersession — no cross-paper drift. **No finding here.**

## Question-by-question summary

1. **Mutual exclusivity of the four routes:** R1 (NJL contact, parity-even, $M_{\rm Pl}^{-2}$) and R2 (one-loop graviton, parity-odd, $M_{\rm Pl}^{-1}$) share the assumption that the gravitational sector is the only mediator. R3 (Immirzi running) shares with R2 the assumption that the Standard Model fermion content is the only chiral input. R4 (parity-odd CMB coupling) is structurally distinct — it requires an external spectator field. The union-of-routes argument is *not* rigorous in the sense that R1–R3 are not strictly disjoint; but the closure is *amplitude-bound*, so the routes do not need to be disjoint — each independently fails to deliver the required amplitude. **The paper should say this explicitly** (see M1).

2. **Route 4 amplitude bound:** R45-B1 fix is consistent — the 22–36 OOM range supersedes the old "≥ 8 OOM" claim. Abstract is silent on the number (see M2).

3. **Route 2 dimensional consistency:** R45-B2 fix is consistent — the dimensionless ratio replaces the bad eV-vs-eV comparison, and the author explicitly acknowledges the prior error (lines 608–612). But the "two orderings differ by 25 OOM" sentence (M3) is a remaining issue.

4. **M4 D_inf prefactor justification:** the Wave 14-NNNN insertion (lines 374–430) is dimensionally correct, walks through the $a^{-3}$ contorsion dilution + density-of-states matching + parity-odd phase-space factor. Author acknowledges the prefactor is "order-of-magnitude" rather than first-principles (lines 376–380, 1140–1154). This is honest. No finding.

5. **M5 orphan-label check:** Wave 14-NNNN did *not* fully land. `sec:conjunctive` (line 800) is a free-floating label, and `sec:oneloopfull` / `sec:condensate` / `sec:cosmo_derivation` are dead-scaffolding labels at line 497. See m1 + m2.

6. **6 vs 7 vs 8 branches:** all four sites (abstract line 67, §I.A.2 line 195, §IX line 829, §XV line 1302) consistently say "6 observational research branches (Branches H, J, L, M, N, O)". **Clean.**

7. **Frozen MCMC dataset combinations:** Table II ‡-footnote (line 1075) is the BLOCKER B1 above.

8. **Barbero-Immirzi $\gamma$ scope:** ABCK (fiducial 0.274) vs DLM (0.2375) is clearly stated in §II.A.1 (lines 271–273). Holst (1995) normalization is consistent with Mercuri (2006) and Freidel+(2005). But the Table III prior column is self-contradictory (see M4).

9. **Bayesian or frequentist?** Neither is declared. The four-route theorem is an amplitude-bound argument, not a hypothesis test. See M1.

10. **Cross-paper references:** clean (see cross-paper check above).

---

**Recommended waves:**
- **Wave 14-(next):** P1A v1A.0.19 → v1A.0.20 R50 BLOCKER B1 (stale w0wa footnote reframe) + B2 (structural-tension/14-barrier reconciliation paragraph) + MAJORs M1 (inferential framework declaration) + M2 (abstract R4 closure amplitude) + M3 (R2 ordering disambiguation) + M4 (Table III prior column fix). 1–2 hours of focused edits, no recompute or rerun required.
- **Wave 14-(next+1):** P1A v1A.0.20 → v1A.0.21 minors + nits sweep, recompile, mirror, SSOT update.

After both waves and a clean cross-vendor R-round, P1A is ready for arXiv submission pending Houston sign-off. Recommended readiness: **95 % until both waves + cross-vendor round clear; 99 % after that.**
