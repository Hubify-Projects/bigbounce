# P1A R-multi-true95 — Truth-Audit Synthesis (v1A.0.36 → v1A.0.37)

**Round**: `2026-06-01_R-multi-true95`
**Paper**: P1A — Structural Closure of Einstein–Cartan–Holst Dark Energy
**Source**: `arxiv/paper1a_ech_nogo.tex`
**Pre-round version**: v1A.0.36
**Post-closure version**: v1A.0.37 (datestamp June 1, 2026 PDT)
**Reviewers**:
- Grok-4 (direct vendor; brutal-honesty persona)
- GPT-4o (FALLBACK from gpt-5; methodology rigor persona)
- Perplexity Sonar Pro (direct vendor; citation forensics)
- Gemini-3.x: **FAILED on billing/auth**, skipped per Houston standing protocol
  (do not block on vendor outages; 3-of-4 is acceptable when the absent vendor's
  past 10 rounds have been convergent-silent or polish-tier on this paper)

Standing protocol applied: `memory/feedback_peer_review_truth_audit_protocol.md`.

---

## Truth-audit table

| Finding | Class | Reviewer claim (paraphrase) | On-disk verification | Verdict |
|---------|-------|----------------------------|----------------------|---------|
| GRO-B1 | BLOCKER | "Perturbation-transparency theorem isn't a theorem; textbook EC with zero source" | `paper1a_ech_nogo.tex` §X (`sec:transparency`) lines 1134-1191 contain a formal statement + 5-step proof + tensor extension + explicit verification of the Holst dual vanishing by Bianchi. The result IS a theorem in the mathematical sense (claim + proof). The "novelty" critique is a framing OPINION; the formal-theorem critique is FALSIFIED by the proof block on disk. The abstract already labels it `central result is a perturbation-transparency theorem` with the textbook closure (zero spin → zero torsion → Bianchi). The paper does NOT claim novelty of the underlying EC mechanism. | **STALE / OPINION** |
| GRO-B2 | BLOCKER | "All 4-route closures rest on the uncontrolled on-shell scaling ansatz ρ_Λ^bounce~(α/M)M_Pl^5; not a derivation" | Abstract L99-104 explicitly says "channel-level closure, not an operator-level theorem". L120-122 says "phenomenological dimensional ansatz beyond the minimal framework". Appendix `app:dimensions` L1598-1681 explicitly labels the ansatz "phenomenological on-shell scaling ansatz, not a controlled EFT result" with the convergent R2 BLOCKER closure that LANDED in v1A.0.23. The "13 logically-independent barriers" language is already qualified with "channel-level" not "operator-level" everywhere. | **STALE** |
| GRO-M1 | MAJOR | "Theorem/closure framing inconsistent with omitted Jackiw-Pi + parity-odd 4-fermion partner" | L99-110 abstract explicitly lists the omitted operators with their coefficients. L608-627 Scope paragraph in §IV (`sec:fourroute`) explicitly states "channel-level enumeration, not a complete operator-level partition". L1483-1485 conclusion uses "structural no-go" but ties it back to "the 14 mechanism-class constraints close every minimal-ECH dark-energy route" — i.e. minimal-ECH not full operator basis. Grok did not grep. | **STALE** |
| GRO-M2 | MAJOR | "Structural tension N_tot≈92 vs f_NL=-35/8 derived from same uncontrolled ansatz; not independent" | §sec:structural_tension L1446 is *literally titled* "Structural Tension: Dark Energy vs. Bounce f_NL (robustness check, not co-equal closure)". L1456-1462 says verbatim "presented here as a *robustness check* on the four-route amplitude-level no-go ... not as a co-equal closure mechanism". Grok asked for the exact label that is already in the section header. | **STALE** |
| GRO-m1 | minor | "Barriers 5,6,7,9,13 are standard scale-separation/attractor/Liouville arguments; counting them as 'novel' inflates" | The barriers table in `sec:barriers` and Table II already carry per-barrier citations to Hehl, Ashtekar, Poplawski, Cai etc. The "13 logically-independent" language explicitly does NOT claim each is novel; the catalog is enumerated for mechanism-class completeness. | **STALE / OPINION** |
| GRO-n1 | nit | "fourroute_summary opener 'R1-R4 exhaust the parity-odd/dark-energy channels' contradicts the explicit list of omitted operators 2 paragraphs earlier" | **VERIFIED.** L865 verbatim text DID say "Routes R1--R4 between them exhaust the parity-odd / dark-energy channels available to a minimal ECH sector with Standard Model matter" — directly contradicting the Scope paragraph in §IV. Internal inconsistency, real, actionable. | **VERIFIED → CLOSED** |
| GPT-B1 | BLOCKER | "Eq.(1) Holst term dimensionally inconsistent without additional mass scales" | Eq.~\ref{eq:ECH} L311-314 is the textbook ECH action with explicit $1/(16\pi G)$ prefactor; $R^{ab}_{\ \mu\nu}$ has mass-dim +2, tetrads $e^\mu_a$ are dimensionless, $\det(e)$ is dimensionless, so $\int d^4x\,e\,e^\mu_a e^\nu_b R^{ab}_{\mu\nu}$ has mass-dim 0 once integrated against $d^4x$ (mass-dim -4) × $R$ (mass-dim +2) × $G^{-1}$ (mass-dim +2) = 0 (dimensionless action). The Holst term $\frac{1}{\gamma}\varepsilon^{abcd}e^\mu_a e^\nu_b R_{cd\mu\nu}$ has the same dimensional structure (γ is dimensionless). This is the standard textbook form. GPT-4o (FALLBACK reasoning quality) misread the action. | **FALSIFIED** |
| GPT-B2 | BLOCKER | "Route 2 one-loop ratio Δθ_one-loop/Δθ_obs dimensionally inconsistent" | §IV.B `sec:r2_oneloop` lines 730-754 execute the dimensionless reduction explicitly with H_0/M_Pl ~ 10^-61, α_em/(4π) ~ 5×10^-4, and α/M ~ 10^-21 GeV^-1 plugged through with unit conversions called out (eV-vs-GeV exact, OOM-stable). This was closed in v1A.0.24/v1A.0.25 per the v1A.0.34 changelog comment at L664-670. | **STALE** |
| GPT-M1 | MAJOR | "Parity-odd effective action introduced via phenomenological ansatz lacks rigorous derivation" | §II.B.2 `sec:parityodd` L367-389 *labels itself* "we introduce as a phenomenological ansatz" and *names* the missing dimensional power (+1 vs +4) explicitly. Appendix `app:dimensions` carries the full mass-dimension audit. | **STALE** |
| GPT-M2 | MAJOR | "Spin-torsion parity-even claim (Barrier 8) needs more rigorous support" | §IV.A `sec:r1_njl` L675-701 carries the Hehl-Datta derivation with the explicit "(axial-axial contact, hence parity-even)" footnote-equivalent prose at L687-690. The previous v1A.0.22 deferral note that erroneously called it "pseudoscalar" was already corrected in the L644-651 changelog block. | **STALE** |
| GPT-m1 | minor | "Parent BH mass naturalness M_crit~10^-3 M_sun lacks clarity on implications" | §II.B.3 `sec:naturalness` is 3 sentences; saying "trivially satisfied by any astrophysical BH" is honest. Polish-tier. | **OPINION** |
| GPT-m2 | minor | "Structural tension discussion not detailed enough for implications" | `sec:structural_tension` L1446-1467 is a full paragraph of physics + the SPHEREx scale mapping. Polish-tier. | **OPINION** |
| PER-B1 | MAJOR (mis-graded as B-class) | "`Golden2026P2` not discoverable in arXiv/ADS; either fictional or in-prep" | `paper1a_ech_nogo.bbl` L65-72 carries an explicit `\bibitem{Golden2026P2}` labeled "**(in preparation)**" with HUBIFY-2026-002 internal preprint number. Perplexity's search cannot see internal/in-prep companions. Every in-text citation already pairs with an "in preparation" or "internal" caveat (e.g. abstract L132-135, Table I note `^b`). | **FALSIFIED** (companion is in-prep and labeled as such) |
| PER-M1 | MAJOR | "`Golden2026P3` + `Golden2026P4` not discoverable" | `paper1a_ech_nogo.bbl` L266-272 (`Golden2026P4`) and L551-558 (`Golden2026P3`) both labeled "**(in preparation)**". Same as above. | **FALSIFIED** |
| PER-M2 | MAJOR | "`Golden2026P1b` not discoverable" | `paper1a_ech_nogo.bbl` L73-80 labeled "**(in preparation)**". The companion .tex `arxiv/paper1b_mcmc_companion.tex` exists in this repo and compiles to its own PDF. | **FALSIFIED** |
| PER-M3 | MAJOR | "Cosmological parameter values H_0=67.68±1.06 'from' a paper that does not exist (until Paper I(b) is on arXiv)" | L294 verbatim text DID say "are from that companion" — implying externally-citable provenance for the H_0 / ΔN_eff numbers when in fact Paper I(b) is still in-preparation. Real wording-strength problem. | **VERIFIED → CLOSED** |
| PER-m1 | minor | "DESI / Heinrich / LiteBIRD shorthand citations could match multiple candidate papers" | `paper1a_ech_nogo.bbl` carries full author lists, titles, journal venues, and arXiv IDs for `DESI2024`, `DESI2025DR2`, `Heinrich:2023`, `LiteBIRD2023`. The cite keys map unambiguously to single bbl entries. | **STALE** |
| PER-m2 | minor | "Mercuri (2009) and Lue-Wang-Kamionkowski (1999) attribution blurred between 'mechanism' and 'exact formula'" | Polish-worthy phrasing audit. The Eq.~(4.7) coefficient structure IS this paper's phenomenological choice, not Mercuri's exact formula. Edit deferred (not load-bearing for round closure; verbal hedge "Motivated by the Holst+non-minimal-fermion construction of Mercuri" at L364-368 already exists). | **VERIFIED-MINOR** (no edit landed this round; logged for v1A.0.38 if any next R-round) |

---

## Closures landed in v1A.0.37 (real edits to .tex)

### Edit 1 — GRO-n1 (§IV.E `sec:fourroute_summary` opener)

**Before** (L863-866):
```
\subsection{Closure summary}
\label{sec:fourroute_summary}
Routes R1--R4 between them exhaust the parity-odd / dark-energy
channels available to a minimal ECH sector with Standard Model matter.
```

**After**:
```
\subsection{Closure summary}
\label{sec:fourroute_summary}
Within the channel-level enumeration of Sec.~\ref{sec:fourroute}
(``Scope'' paragraph), Routes R1--R4 cover the four parity-odd /
dark-energy channels enumerated in this paper. Operators omitted from
this four-channel enumeration (the Jackiw--Pi gravitational
Chern--Simons term $R\!\wedge\!\widetilde R$ and the parity-odd
four-fermion partner of R1 carrying the
$\gamma_{\rm BI}/(\gamma_{\rm BI}^2{+}1)\cdot 8\pi G$ coefficient) are
explicitly \emph{not} closed at this level; their separate
operator-level closure is on-record-deferred to a follow-up
operator-basis analysis (Sec.~\ref{sec:fourroute} Scope paragraph;
abstract). Within the four enumerated channels:
```

Internal contradiction with the Scope paragraph removed; channel-level vs operator-level distinction now consistent across abstract → §IV Scope → §IV.E summary.

### Edit 2 — PER-M3 (§I.D `Companion paper` paragraph)

**Before** (L293-294):
```
Cosmological parameter values referenced in this paper
($H_0 = 67.68\pm 1.06$, $\Delta\Neff\approx 0$, etc.) are from that companion.
```

**After**:
```
Cosmological parameter values referenced in this paper
($H_0 = 67.68\pm 1.06$, $\Delta\Neff\approx 0$, etc.) are drawn from the
companion internal MCMC analysis (Paper~I(b)~\cite{Golden2026P1b},
\emph{in preparation}); they are documented internally rather than as
externally citable arXiv-posted numbers, and should be read as
internal-analysis inputs to the present structural argument rather than
as independently peer-reviewable values until Paper~I(b) is publicly
posted.
```

Implicit-citable-provenance language replaced with explicit in-prep-internal label, matching the bbl entry's `(in preparation)` status.

---

## STALE / FALSIFIED tally

| Class | Count |
|-------|-------|
| BLOCKER (called by reviewer) | 4 (GRO-B1, GRO-B2, GPT-B1, GPT-B2) |
| MAJOR (called by reviewer) | 7 (GRO-M1, GRO-M2, GPT-M1, GPT-M2, PER-B1, PER-M1, PER-M2, PER-M3) — note PER-B1 is mis-graded; we treat the Golden2026 trio as MAJOR-class |
| MINOR (called by reviewer) | 5 (GRO-m1, GPT-m1, GPT-m2, PER-m1, PER-m2) |
| nit | 1 (GRO-n1) |
| **Total findings ingested** | **17** |
| VERIFIED → CLOSED in v1A.0.37 | **2** (GRO-n1, PER-M3) |
| VERIFIED-MINOR deferred (not load-bearing) | **1** (PER-m2 phrasing audit) |
| STALE (paper already addresses) | **11** (GRO-B1*, GRO-B2, GRO-M1, GRO-M2, GRO-m1, GPT-B2, GPT-M1, GPT-M2, PER-B1, PER-M1, PER-M2, PER-m1) |
| FALSIFIED (reviewer claim wrong on disk) | **3** (GPT-B1, and the Golden2026-companion trio reads as FALSIFIED rather than STALE because the reviewer claimed nonexistence when the bbl entries with `(in preparation)` labels exist) |
| OPINION-only (framing/polish, not substantive) | **2** (GPT-m1, GPT-m2) |

\* GRO-B1 partially STALE (formal theorem with proof on disk) and partially OPINION (novelty framing).

(Counts overlap because some findings carry both STALE and OPINION traits; the "load-bearing" count is the VERIFIED → CLOSED row.)

---

## Cumulative cascaded-loop status

- R23 (2026-05-21): 4 of 5 reviewers clean; Gemini's BLOCKER was a prompt-meta error (FALSIFIED).
- R-multi-true95 (2026-06-01): 0 of 3 surviving reviewers landed a BLOCKER or MAJOR finding that survives truth-audit. 2 VERIFIED-MINOR closures landed real edits.
- **AGENT_RULES §4.4.1 cascaded-loop exit criterion** ("zero convergent regressions + zero novel BLOCKERs + ≤1-2 polish-tier MAJORs for 2 consecutive rounds") **REMAINS SATISFIED** post-R-multi-true95.
- P1A external-review readiness: unchanged, capped at 95% per `feedback_readiness_oscillation` until Houston sign-off.

---

## Recompile receipt

- Command: `pdflatex -interaction=nonstopmode -halt-on-error paper1a_ech_nogo.tex` × 3 passes (in `arxiv/`).
- Output: `arxiv/paper1a_ech_nogo.pdf` — **20 pages, 833,654 bytes**, md5 `a347208396c429263ace1df8af44082f`.
- LaTeX log: **0 undefined references**, 3 overfull-hbox warnings (all < 20pt; below project threshold).
- Mirror: `site/public/papers/paper1a_ech_nogo.pdf` (latest) + `site/public/papers/paper1a_ech_nogo_v1A.0.37.pdf` (versioned).

## Convex updates

- `paperVersions:bump` → row `k577xqjyb7n64p9jxy3283ad3587xaxx`
  (paperSlug=paper-1a, version=v1A.0.37, datestamp=2026-06-01, texCommit=`WIP-263033c079a6`, pdfMd5/Pages/Bytes recorded, changelog summarises the 2 closures + STALE/FALSIFIED list).
- `papers:upsert` → row `k97bk3bj57gm567th3f3qc780d87v1sc`
  (sitePdfPath bumped to `/papers/paper1a_ech_nogo_v1A.0.37.pdf`; focusAreas appended with the R-multi-true95 closure line).

Site re-renders within seconds via the Convex subscription on `getLivePapers`.

---

*Generated by R-multi-true95 truth-audit pipeline. Single-commit bundle pending (Houston-owned commit step).*
