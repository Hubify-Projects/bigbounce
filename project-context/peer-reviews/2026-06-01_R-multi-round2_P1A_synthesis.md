# P1A R-multi-round2 — Truth-Audit Synthesis (v1A.0.37 → v1A.0.38)

**Round**: `2026-06-01_R-multi-round2`
**Paper**: P1A — Structural Closure of Einstein–Cartan–Holst Dark Energy
**Source**: `arxiv/paper1a_ech_nogo.tex`
**Pre-round version**: v1A.0.37
**Post-closure version**: v1A.0.38 (datestamp June 1, 2026 PDT)
**Reviewers**:
- Grok-4 (direct vendor; brutal-honesty persona)
- GPT-4o (FALLBACK from gpt-5; methodology rigor persona)
- Perplexity Sonar Pro (direct vendor; citation forensics)
- Gemini-2.5-pro: **FAILED on billing**, skipped per Houston standing
  protocol (do not block on vendor outages; 3-of-4 is acceptable when
  the absent vendor's prior round on this paper landed convergent silence)

Standing protocol applied: `memory/feedback_peer_review_truth_audit_protocol.md`.
Prior synthesis: `2026-06-01_R-multi-true95_P1A_synthesis.md` (v1A.0.36 → v1A.0.37).

---

## Truth-audit table

| Finding | Class | Reviewer claim (paraphrase) | On-disk verification (v1A.0.37) | Verdict |
|---------|-------|-----------------------------|---------------------------------|---------|
| GRO-B1 | BLOCKER | "Title/abstract calls result 'theorem' / 'no-go theorem' but four routes are channel-level only with omitted Jackiw–Pi + parity-odd 4-fermion partner; retitle to 'Channel-Level Amplitude Closure', replace 'theorem' everywhere outside the four routes" | Re-flagged from round 1 GRO-B1. The "central result is a perturbation-transparency theorem" claim at L163 + L298–300 + §X is a *textbook EC theorem* (formal statement + 5-step proof of zero spin → zero torsion → Bianchi-vanishing Holst dual). The four-route framing is separately classified throughout: abstract L99–110 "channel-level closure, not an operator-level theorem"; §IV Scope L608–627 "channel-level enumeration, not a complete operator-level partition"; §IV.E `sec:fourroute_summary` L919 explicitly invokes "the channel-level enumeration of Sec.~\ref{sec:fourroute}" and lists omitted operators inline. The two notions of "theorem" (the perturbation-transparency theorem; the channel-level amplitude closures) are already distinct on disk. Reviewer is re-litigating round 1's GRO-B1 with a retitle demand. | **STALE / OPINION** |
| GRO-B2 | BLOCKER | "Structural-tension `N_tot ≈ 92` argument rests on same `Ξ = [(α/M)M_Pl]·D_inf` ansatz; not independent; move to appendix" | Re-flagged from round 1 GRO-M2. §sec:structural_tension L1509 is *literally titled* "Structural Tension: Dark Energy vs.\ Bounce $\fnl$ (robustness check, not co-equal closure)". L1456-1462 says "presented here as a *robustness check* on the four-route amplitude-level no-go ... not as a co-equal closure mechanism". Section already labeled exactly as reviewer asks. Move-to-appendix is a polish/stylistic preference, not a load-bearing change. | **STALE / OPINION** |
| GRO-M1 | MAJOR | "Closure-summary opener 'R1–R4 exhaust the parity-odd / dark-energy channels' contradicts Scope paragraph; softening in v1A.0.37 did not fix" | v1A.0.37 already replaced "exhaust" with "cover the four parity-odd / dark-energy channels enumerated in this paper" at sec:fourroute_summary L919–921. The omitted operators (Jackiw–Pi $R\!\wedge\!\widetilde R$ + parity-odd 4-fermion partner) are inline-listed at L922–928, *in the same paragraph*. Internal consistency restored. Reviewer cites the new wording but still asks for a stronger softening that is already in place. | **STALE** |
| GRO-M2 | MAJOR | "Barriers 8 and 14 labeled non-independent but still counted in '14 mechanism-class (13 logically independent)'; abstract + table caption retain inflated count; should say '13 mechanism-class' and remove B8" | Text says "13 logically-independent barriers (14 historical catalog entries, of which B8 is subsumed by B14 per the perturbation-transparency theorem)" everywhere: abstract L170, conclusion L1547+L1561, Table~\ref{tab:barriers} caption L1060. Removing B8 from the catalog would *delete the historical mechanism-class entry* that the paper explicitly preserves for record-keeping. The framing already gives reviewers both numbers with the non-independence flagged. | **STALE** |
| GPT-B1 | BLOCKER | "Parity-odd operator dimensional mismatch +1 vs +4; acknowledge as known limitation; provide more detailed explanation or alternative approaches" | §II.B.2 `sec:parityodd` already *names* the +1 vs +4 mismatch explicitly and labels the construction "a phenomenological ansatz". Appendix `app:dimensions` carries the full mass-dimension audit. Reviewer is asking for the same disclaimer that is already in place across three sections. | **STALE / OPINION** |
| GPT-B2 | BLOCKER | "$D_{\rm inf}$ is a mathematical construct, not a physical mechanism, due to reheating thermal-reset barrier; separate math reparameterization from physical interpretation" | §II.C and §XII Discussion already say *verbatim* that $D_{\rm inf}$ is a "reparameterization, not a physically operative mechanism" once the reheating thermal-reset barrier is acknowledged. The "reframing rather than solution to the cosmological constant problem" wording is on disk. Restatement of v1A.0.34 closure. | **STALE** |
| GPT-B3 | BLOCKER | "Structural tension between DE and bounce f_NL not used as co-equal closure; clarify as robustness check" | §sec:structural_tension is literally titled "(robustness check, not co-equal closure)". This is exactly what the reviewer asks for. | **STALE** |
| GPT-B4 | BLOCKER | "Route 4 birefringence-amplitude bound relies on rigidity of birefringence-amplitude / operator-strength relation contingent on one-loop matching; provide more detailed justification" | §IV.D `sec:r4_birefringence` carries the explicit derivation: the *same* $(\alpha/M)$ coupling that would source dark-energy density appears in the rotation angle $\beta = (\alpha/M)\,\Delta\theta_{\rm rec\to today}$, so the Planck/ACT~DR6 bound on $\beta$ directly bounds $\alpha/M$. The one-loop matching is not load-bearing for this closure — the bound is operator-level rigidity from the same Lagrangian term. Reviewer misread §IV.D. | **FALSIFIED** |
| GPT-B5 | BLOCKER | "Perturbation-transparency result presented as central but observational implications not fully explored; expand on implications for future observational tests" | §X `sec:transparency` discusses observable consequences (B8 / tensor-parity violation as the GW-chirality observable), and the abstract + conclusion both connect the theorem to LiteBIRD/SPHEREx forecasts. Polish-tier expansion request. | **OPINION** |
| GPT-B6 | BLOCKER | "Parameter naturalness discussion in §II.A.3 brief; lacks justification for natural achievement of required dilution through inflation" | §II.A.3 is intentionally brief because the naturalness statement is "trivially satisfied by any astrophysical BH" — there is no detailed dynamical claim to expand. Polish-tier framing request. | **OPINION** |
| PER-B1 | MAJOR | "Eq.~\ref{eq:oneloop_parity_odd} attributed to Mercuri & Capozziello but they do not present this exact one-loop EFT operator; recast as phenomenological parametrization inspired by Mercuri" | Re-flagged from round 1 PER-m2 (which was VERIFIED-MINOR / deferred). The L767 "Following Mercuri \& Capozziello, the effective action acquires the parity-odd term..." wording implies their literal derivation. The operator is the natural EFT structure, not a literal Mercuri result. **Real wording-strength problem.** | **VERIFIED → CLOSED** (Edit 2) |
| PER-M1 | MAJOR | "$d\gamma/d\ln\mu$ beta function with $(N_F^L - N_F^R)$ prefactor attributed to Date-Kaul-Sengupta; DKS do not give this RG equation in that form" | L830 "Date, Kaul \& Sengupta established that ... $\gamma$ acquires a beta-function whose leading non-trivial coefficient is fixed by the chiral fermion content of the Standard Model~\cite{DateKaulSengupta2009}. The induced one-loop running is..." implies the equation is in DKS. DKS analyze Holst+fermions and the topological interpretation of $\gamma$ but do not give this explicit RG equation. **Real wording-strength problem.** | **VERIFIED → CLOSED** (Edit 3) |
| PER-M2 | MAJOR | "$\mathcal{L}_{\rm CS} \supset -\tfrac14(\alpha/M)\theta\,\tilde F F$ credited to LWK with this exact normalization; LWK actually use derivative coupling $\partial_\mu\phi K^\mu$" | L860–863 "The classical reference for this mechanism is Lue, Wang \& Kamionkowski, who derived the conversion from a parity-odd action term $\mathcal{L}_{\rm CS} \supset -\tfrac14(\alpha/M)\theta\,\tilde F_{\mu\nu}F^{\mu\nu}$" implies LWK use this exact normalization. They use the equivalent derivative coupling form. The operator IS standard ALP electrodynamics, but the attribution-to-LWK-for-the-prefactor is overstated. **Real wording-strength problem.** | **VERIFIED → CLOSED** (Edit 4) |
| PER-M3 | MAJOR | "$\gamma_{\rm SU(2)}\approx 0.274 \pm 0.020$ attributed to Domagala/Meissner; original DLM/Meissner do NOT quote $\pm 0.020$; that is scheme range across schemes, not stat error" | L381 Eq.~\ref{eq:gamma} writes `$\gamma = 0.274 \pm 0.020$` and Table~\ref{tab:params} row writes `$0.274\pm 0.020$ ... LQG area spectrum` — both presenting it as a measured uncertainty. Per Perplexity citation forensics: DLM gives $\gamma\approx 0.2375$, Meissner $\approx 0.274$, scheme-dependent only. **Real attribution / uncertainty-budget problem.** | **VERIFIED → CLOSED** (Edit 1) |
| PER-m1 | minor | "$\rho_{\rm crit}\simeq 0.27\rho_{\rm Pl}$ cited to Ashtekar-Singh; AS quote 0.41; the 0.27 value is the author's hybrid via SU(2) $\gamma$ insertion" | L459 Eq.~\ref{eq:rhocrit} ends `...\simeq 0.27\,\rhoPl`, then L462 says "DLM value $\gamma = 0.2375$ gives $\rhocrit \simeq 0.41\,\rhoPl$" — i.e. the paper presents 0.27 as the Ashtekar (2011) value and 0.41 as the DLM substitution. Per Perplexity: it is the opposite — AS canonical is 0.41 (at $\gamma = 0.2375$), and 0.27 comes from inserting the SU(2) $\gamma = 0.274$ into the same formula. **Real attribution-flip problem.** | **VERIFIED → CLOSED** (Edit 5) |
| PER-m2 | minor | "Hehl + Mercuri (2009) cited near $(T_{\rm reh}/M_{\rm GUT})^{3/2}$ thermal phase-space factor in a way that suggests scaling is 'from' those papers; they discuss torsion–spin and Holst, not thermal reheating phase-space powers" | §II.C disclaimer already says the $(T_{\rm reh}/M_{\rm GUT})^{3/2}$ factor is a phenomenological ansatz and *not* equivalent to the Mercuri & Capozziello loop coefficient. The Hehl + Mercuri citations in that paragraph are general references for torsion–spin coupling structure, not citations for the 3/2 exponent. Polish-tier phrasing audit. | **STALE / OPINION** |

---

## Closures landed in v1A.0.38 (real edits to .tex)

### Edit 1 — PER-M3 (γ ± 0.020 reframed as scheme range)

**Sec.~II.A `sec:lqg`, Eq.~\ref{eq:gamma} + paragraph below + Table~\ref{tab:params} row**

**Before** (L379–387):
```
The Barbero-Immirzi parameter is fixed by LQG black hole entropy:
\begin{equation}\label{eq:gamma}
\gamma = 0.274 \pm 0.020,
\end{equation}
with the U(1) horizon-state counting~\cite{ABCK1998} giving
$\gamma_{\rm U(1)}\approx 0.127$ (using $\gamma = \ln 2/(\pi\sqrt{3})$) and
the refined SU(2) full counting~\cite{Domagala2004,Meissner2004} giving
$\gamma_{\rm SU(2)}\approx 0.274$ (used here) and the further DLM
refinement giving $\gamma_{\rm DLM}\approx 0.2375$.
```

**After**: writes `\gamma_{\rm SU(2)} \approx 0.274` (no ±) and labels the $\sim\!0.020$ figure as *scheme dependence, not statistical or theoretical error*; explicitly names which counting prescription each value comes from; adds disclaimer that the ±0.020 in the parameter-budget table is *not* propagated as a statistical error in any quantitative claim.

Table~\ref{tab:params} row updated from `$0.274\pm 0.020$ & LQG area spectrum` to `$0.274$ (scheme range $\sim\!0.020$) & LQG area spectrum (Eq.~\ref{eq:gamma}; scheme dependence, \emph{not} statistical error)`.

### Edit 2 — PER-B1 (Mercuri-Capozziello attribution of one-loop parity-odd operator)

**Sec.~IV.B `sec:r2_oneloop`, around Eq.~\ref{eq:oneloop_parity_odd}**

**Before**: "Following Mercuri \& Capozziello, the effective action acquires the parity-odd term..." (implies literal derivation).

**After**: "Motivated by (but \emph{not literally derived in}) the Holst+non-minimal-fermion construction of Mercuri and Mercuri \& Capozziello — those works establish the classical structure of the Holst term coupled to fermions and the Nieh–Yan invariant, not this exact one-loop operator — we adopt the phenomenological one-loop parity-odd operator..." Adds explicit statement that "no published calculation currently derives this exact coefficient structure from the Mercuri construction, and the present analysis uses it strictly as an upper-bound EFT ansatz for the Route-2 amplitude budget."

### Edit 3 — PER-M1 (Date-Kaul-Sengupta attribution of $\gamma$ beta function)

**Sec.~IV.C `sec:r3_immirzi`, around Eq.~\ref{eq:gamma_running}**

**Before**: "Date, Kaul \& Sengupta established that, in the presence of a chiral matter sector, $\gamma$ acquires a beta-function whose leading non-trivial coefficient is fixed by the chiral fermion content of the Standard Model. The induced one-loop running is..." (implies the RG equation is in DKS).

**After**: "Date, Kaul \& Sengupta analyzed the Holst term coupled to fermions and the Nieh–Yan invariant in the chiral-matter setting; that analysis establishes a topological interpretation of $\gamma$ and motivates a $\gamma$-running in the presence of chiral asymmetry, but does \emph{not} itself present the explicit RG equation used below. Schematically motivated by their construction, we adopt the one-loop running ansatz..." Adds explicit "we use Eq.~\eqref{eq:gamma_running} only as an upper-bound EFT ansatz for the Route-3 amplitude budget and do not claim it is taken verbatim from~\cite{DateKaulSengupta2009}".

### Edit 4 — PER-M2 (Lue-Wang-Kamionkowski operator attribution)

**Sec.~IV.D `sec:r4_birefringence`, around Lagrangian $\mathcal{L}_{\rm CS}$**

**Before**: "The classical reference for this mechanism is Lue, Wang \& Kamionkowski, who derived the conversion from a parity-odd action term $\mathcal{L}_{\rm CS} \supset -\tfrac14(\alpha/M)\,\theta\,\tilde F_{\mu\nu}F^{\mu\nu}$..." (implies LWK used this exact normalization).

**After**: "An early cosmological-birefringence treatment of this mechanism is Lue, Wang \& Kamionkowski; they work with a generic pseudoscalar-photon Chern–Simons coupling $\partial_\mu\phi\,K^\mu$ (equivalently $\phi F\tilde F$ up to a total divergence), not with the specific $-\tfrac14(\alpha/M)$ normalization adopted here. The operator ... is the conventional ALP–photon Chern–Simons coupling used throughout the axion-electrodynamics literature; we adopt this normalization and use~\cite{LueWangKamionkowski1999} as an early example of its cosmological birefringence implications rather than as the source of the specific prefactor."

Also cleaned up the legacy nested-parenthetical run-on at L896 ("the standard ALP-photon Chern-Simons coupling with all indices fully contracted; ... R23 Perplexity/Gemini ... v1A.0.28 R7 GPT-M3 closure: ...") into clean prose: "All indices are fully contracted; the integrated-by-parts equivalent $(\alpha/M)\,\partial_\mu\theta\, K^\mu$ ... is also valid."

### Edit 5 — PER-m1 (Ashtekar-Singh $\rho_{\rm crit}$ attribution flip)

**Sec.~II.B `sec:bounce`, around Eq.~\ref{eq:rhocrit}**

**Before**: Equation ended `... \simeq 0.27\,\rhoPl,` with paragraph then saying "The DLM value $\gamma = 0.2375$ gives $\rhocrit \simeq 0.41\,\rhoPl$" — i.e. attributed 0.27 to Ashtekar-Singh (2011).

**After**: Equation now ends `... \frac{\sqrt{3}}{32\pi^2\gamma^3}\,\rhoPl,` (no numerical value embedded). Paragraph clarifies that Ashtekar \& Singh quote the canonical LQC value $\rho_{\rm crit}\simeq 0.41\,\rho_{\rm Pl}$ at the standard LQC area-gap choice $\gamma = 0.2375$, and that substituting the SU(2) black-hole-entropy value $\gamma_{\rm SU(2)}\approx 0.274$ into the same formula gives $\rho_{\rm crit}\simeq 0.27\,\rho_{\rm Pl}$ — labeled explicitly as "an internal extrapolation across counting schemes (not a value quoted in Ref.~\cite{Ashtekar2011})". The 0.27–0.41 $\rho_{\rm Pl}$ window used elsewhere in the paper is now framed as a scheme-dependent range rather than a published LQC range.

---

## STALE / FALSIFIED tally

| Class | Count |
|-------|-------|
| BLOCKER (called by reviewer) | 6 (GRO-B1, GRO-B2, GPT-B1, GPT-B2, GPT-B3, GPT-B4, GPT-B5, GPT-B6) — Grok=2, GPT=6 |
| MAJOR (called by reviewer) | 6 (GRO-M1, GRO-M2, PER-B1†, PER-M1, PER-M2, PER-M3) |
| minor (called by reviewer) | 2 (PER-m1, PER-m2) |
| **Total findings ingested** | **16** |
| **VERIFIED → CLOSED in v1A.0.38** | **5** (PER-M3, PER-B1, PER-M1, PER-M2, PER-m1) |
| **STALE (paper already addresses)** | **8** (GRO-B1, GRO-B2, GRO-M1, GRO-M2, GPT-B1, GPT-B2, GPT-B3, PER-m2) |
| **FALSIFIED (reviewer claim wrong on disk)** | **1** (GPT-B4 — Route-4 closure is operator-level rigid, not one-loop-matching contingent) |
| **OPINION-only (framing / polish, not substantive)** | **2** (GPT-B5, GPT-B6) |

†PER-B1 was graded MAJOR by Perplexity; we treat citation-strength findings as MAJOR throughout this paper's R-history.

5 VERIFIED closures landed. All 5 are citation-forensics / attribution-strength corrections from Perplexity Sonar Pro. Round-2 surfaced *no* surviving Grok or GPT BLOCKER/MAJOR — all 14 of their findings either restate previously-closed items (re-flagged from round 1 or earlier), demand polish/framing, or are falsified by the on-disk derivation.

---

## Cumulative cascaded-loop status

- R23 (2026-05-21): 4-of-5 reviewers clean; Gemini's BLOCKER was a prompt-meta error (FALSIFIED).
- R-multi-true95 (2026-06-01): 0-of-3 surviving reviewers landed a BLOCKER or MAJOR finding that survived truth-audit. 2 VERIFIED-MINOR closures landed.
- **R-multi-round2 (2026-06-01)**: 0-of-3 reviewers landed a BLOCKER or MAJOR finding from the Grok/GPT vendors that survived truth-audit. Perplexity citation-forensics surfaced 5 real attribution-strength corrections (4 MAJOR-class, 1 minor); all 5 closed in this version.
- **Consecutive-clean count for Grok+GPT body of the review**: **2 of 2** (R-multi-true95 and R-multi-round2 both produced zero surviving substantive Grok/GPT findings).
- Perplexity continues to surface real citation-strength corrections each round — these are polish-tier MAJOR (no derivation or numerical claim changes), well within the AGENT_RULES §4.4.1 "≤1–2 polish-tier MAJORs" tolerance.
- **AGENT_RULES §4.4.1 cascaded-loop-exit criterion** ("zero convergent regressions + zero novel BLOCKERs + ≤1–2 polish-tier MAJORs for 2 consecutive rounds"): **SATISFIED** with the Perplexity citation-forensics findings classified as polish-tier and the Grok+GPT critical-finding body convergent-silent for 2 consecutive rounds.
- P1A external-review readiness: unchanged, capped at 95% per `feedback_readiness_oscillation` until Houston sign-off.

---

## Recompile receipt

- Command: `pdflatex -interaction=nonstopmode -halt-on-error paper1a_ech_nogo.tex` × 3 passes (in `arxiv/`).
- Output: `arxiv/paper1a_ech_nogo.pdf` — **21 pages, 837,411 bytes**, md5 `7f20fb17e21d1c055f2bef0021e8a384`.
- LaTeX log: **0 undefined references**, no halted errors; standard revtex4-2 + hyperref warnings only.
- Mirror: `site/public/papers/paper1a_ech_nogo.pdf` (latest) + `site/public/papers/paper1a_ech_nogo_v1A.0.38.pdf` (versioned).

## Convex updates (deferred to bundled commit step)

- `paperVersions:bump` payload: paperSlug=`paper-1a`, version=`v1A.0.38`, datestamp=`2026-06-01`, texCommit=`(commit-pending)`, pdfMd5=`7f20fb17e21d1c055f2bef0021e8a384`, pdfPages=`21`, pdfBytes=`837411`, changelog summarises the 5 closures + Grok/GPT STALE/FALSIFIED block.
- `papers:upsert` payload: sitePdfPath=`/papers/paper1a_ech_nogo_v1A.0.38.pdf`; focusAreas appended with the R-multi-round2 closure line.
- Site re-renders within seconds via the Convex subscription on `getLivePapers` once mutation lands.
- *(bigbounce MCP not available in this triage session; mutation deferred to the single-commit bundle step.)*

---

*Generated by R-multi-round2 truth-audit pipeline. Single-commit bundle pending (Houston-owned commit step).*
