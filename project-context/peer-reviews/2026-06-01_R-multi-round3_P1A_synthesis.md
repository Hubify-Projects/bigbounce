# P1A R-multi-round3 — Truth-Audit Synthesis (v1A.0.38 → v1A.0.39)

**Round**: `2026-06-01_R-multi-round3`
**Paper**: P1A — Structural Closure of Einstein–Cartan–Holst Dark Energy
**Source**: `arxiv/paper1a_ech_nogo.tex`
**Pre-round version**: v1A.0.38
**Post-closure version**: v1A.0.39 (datestamp June 1, 2026 PDT)
**Reviewers**:
- Grok-4 (direct vendor; brutal-honesty persona)
- GPT-4o (FALLBACK from gpt-5; methodology rigor persona)
- Perplexity Sonar Pro (direct vendor; citation forensics)
- Gemini-2.5-pro: **FAILED on billing**, skipped per Houston standing protocol
  (3-of-4 acceptable when prior round on this paper was convergent-silent).

Standing protocol applied: `memory/feedback_peer_review_truth_audit_protocol.md`.
Prior syntheses:
- `2026-06-01_R-multi-true95_P1A_synthesis.md` (v1A.0.36 → v1A.0.37, 2 closures)
- `2026-06-01_R-multi-round2_P1A_synthesis.md` (v1A.0.37 → v1A.0.38, 5 closures)

---

## Truth-audit table

| Finding | Class | Reviewer claim (paraphrase) | On-disk verification (v1A.0.38) | Verdict |
|---------|-------|-----------------------------|---------------------------------|---------|
| GRO-SILENCE-1 | (none) | Grok explicitly returned: "No new blocker- or major-grade findings survive the convergent-silence filter." All load-bearing claims caveated as required by prior rounds. | n/a (convergent silence) | **CONVERGENT-SILENT** |
| GPT-B1 | BLOCKER | Eq.(1) parity-odd operator dim +1 vs required +4 — clarify as scaling ansatz | §II.B.2 `sec:parityodd` L491-494 already says verbatim "naive mass dimension $[\mathcal{L}_{\rm odd}] = +1$---three units short of the required $+4$ ... The identification $\rho_\Lambda = \Xi\,\MPl^4$ is therefore a \textit{scaling ansatz}, not a controlled EFT calculation." Reviewer is asking for the exact label already on disk. | **STALE / OPINION** |
| GPT-B2 | BLOCKER | Route 2 one-loop ratio Δθ_one-loop/Δθ_obs has units of mass; restore 1/M_Pl factors | §IV.B `sec:r2_oneloop` already executes the dimensionless reduction with explicit M_Pl·(α/M) ~ 10^{-2} prefactor at L864-869 and H_0/M_Pl ~ 10^{-61} at L868. Closed in v1A.0.24/v1A.0.25 per the v1A.0.34 changelog. Round-1 GPT-B2 = STALE; round-2 not raised; round-3 reflag = STALE. | **STALE** |
| GPT-B3 | BLOCKER | Route 4 rigidity tied to one-loop matching; if α/M is free, both β_obs and ρ_Λ can be matched by scaling α/M ∝ m_θ | L989 (§IV.D `sec:r4_birefringence`) carries verbatim: "this overshoot conclusion is conditional on the one-loop estimate $\alpha/M \sim 10^{-21}\,\text{GeV}^{-1}$ being rigidly bounded by the photon-Chern-Simons matching — if $\alpha/M$ is instead treated as a free phenomenological parameter, both $\beta_{\rm obs}$ and $\rho_\Lambda$ can be matched for arbitrary $m_\theta$ by scaling $\alpha/M \propto m_\theta$ (e.g.,\ requiring $\alpha/M \sim 10^{-10}\,\text{GeV}^{-1}$ at $m_\theta \sim 10^{-22}\,\text{eV}$), so the rigidity of the no-go is tied to the one-loop matching assumption rather than to ALP-mass kinematics alone." Reviewer reproduced the on-disk caveat almost verbatim and graded BLOCKER. GPT-4o (FALLBACK) did not grep. | **STALE** |
| GPT-B4 | BLOCKER | Barrier 12 GW bound Ω_GW^ECH|_bounce ≲ (ρ_crit/ρ_Pl)^2 not directly comparable to PTA; propagate through transfer function | §VI Barrier 12 already carries the bounce-frequency mapping comment and the broader paper defers the spectral-shape transfer function as out-of-scope for the *structural* no-go (the barrier is a parametric-amplitude bound, not a spectral prediction). Polish-tier framing; would only add words, not change the no-go content. | **OPINION** |
| GPT-B5 | BLOCKER | §14 Structural Tension framed as robustness check but could mislead readers; emphasize it is NOT a closure | §`sec:structural_tension` L1509 is *literally titled* "Structural Tension: Dark Energy vs.\ Bounce $\fnl$ (robustness check, not co-equal closure)" — same text the reviewer is asking for. Round-1 GRO-M2 = STALE, round-2 GRO-B2 = STALE, round-3 GPT-B5 same finding rephrased = STALE. | **STALE** |
| GPT-B6 | BLOCKER | Appendix B dim-status of parity-odd operator should be labeled phenomenological ansatz, not bookkeeping; controlled EFT deferred | Appendix `app:dimensions` already labels the construction "phenomenological on-shell scaling ansatz, not a controlled EFT result" with the convergent R2-closure prose. Reviewer is reproducing the on-disk label. | **STALE** |
| PER-B1 | MAJOR | `ShapiroTeixeira2014` citation appears fictional or metadata-fused; no Shapiro & Teixeira paper on torsion/anomaly with that result | **FALSIFIED.** Paper exists at arXiv:1402.4854, "Quantum Einstein-Cartan theory with the Holst term" by I.~L.~Shapiro & P.~M.~Teixeira, Class. Quantum Grav. 31:185002 (2014). DOI 10.1088/0264-9381/31/18/185002. Bbl L228-239 entry is correct (author names, title, journal, volume, pages, year, arXiv ID, DOI all verifiable). The paper is exactly the right context: one-loop renormalization of EC+Holst with fermions. Perplexity's search missed an existing publication. | **FALSIFIED** |
| PER-M1 | MAJOR | Mercuri / Mercuri-Capozziello attribution of one-loop parity-odd operator (Eq.~36) is over-attribution; they do not contain this exact EFT operator | **STALE** — already closed in v1A.0.38 as round-2 PER-B1. L767 (§IV.B `sec:r2_oneloop`) now reads "Motivated by (but *not literally derived in*) the Holst+non-minimal-fermion construction of Mercuri and Mercuri \& Capozziello — those works establish the classical structure of the Holst term coupled to fermions and the Nieh–Yan invariant, not this exact one-loop operator — we adopt the phenomenological one-loop parity-odd operator..." Reviewer re-flagged a closed finding without grep'ing the v1A.0.38 changelog block at L65-70. | **STALE** |
| PER-M2 | MAJOR | Sec. 2.1.3 Step 4 "the one-loop estimate is $\alpha/M \sim g^2/(32\pi^2)\,\gamma/M\,\ln(\Lambda_{\rm UV}^2/\mu^2) + \delta_{\rm NY}$" overstates as literal one-loop calculation from literature; recast as schematic EFT scaling | L501-502 already says verbatim: "motivating the order of magnitude $[(\alpha/M)\,\MPl]\sim 10^{-2}$. We treat $\alpha/M$ as a phenomenological parameter constrained by data." Reviewer's request is for the phenomenological framing that is already two lines below the equation. Polish-tier; the citation prefix "Following Freidel et al. and Shapiro & Teixeira" is supported by ShapiroTeixeira2014 (which IS a one-loop quantum-EC+Holst paper). | **STALE / OPINION** |
| PER-M3 | minor | `Golden2026P1b` / `P2` / `P3` / `P4` are "in preparation" companions and not externally verifiable; flag them so | **STALE** — closed in v1A.0.37 as round-1 PER-B1/M1/M2/M3. The bbl carries explicit `(in preparation)` labels on all four companion entries (`paper1a_ech_nogo.bbl` L65-80, L266-272, L551-558), and §I.D Companion-paper paragraph (L294-ish, post-v1A.0.37 edit) says "are drawn from the companion internal MCMC analysis (Paper~I(b), *in preparation*); they are documented internally rather than as externally citable arXiv-posted numbers". Reviewer re-flagged a closed finding. | **STALE** |
| PER-m1 | minor | "Planck/ACT~DR6 3.6σ joint signal" β = 0.342° ± 0.094° citing `[Minami2020, Eskilt2022b, DiegoPalazuelos2025]`: the 0.342° ± 0.094° at ~3.6σ is the WMAP+Planck Eskilt 2022 measurement (NOT joint ACT~DR6); DiegoPalazuelos2025 is the independent ACT~DR6 follow-up at β = 0.215° ± 0.074° (~2.9σ), not a co-measurement of 0.342° | **VERIFIED.** Direct check: arXiv:2205.13962 (Eskilt & Komatsu 2022) = Planck-only β=0.342°±0.094° at ~3.6σ. arXiv:2509.13654 (Diego-Palazuelos & Komatsu 2025) = ACT DR6 β=0.215°±0.074° at 2.9σ. The .tex framing "Planck/ACT~DR6 3.6σ joint signal" at L228-235, L963-965, L1490-1493 conflated the two distinct measurements. Real attribution-strength problem. **CLOSED in v1A.0.39 (Edit 1).** | **VERIFIED → CLOSED** |
| PER-m2 | minor | Ashtekar & Singh "0.27–0.41 ρ_Pl" range over-specific; AS quote 0.41 at γ=0.2375, 0.27 is internal extrapolation at γ=0.274 | **STALE** — closed in v1A.0.38 as round-2 PER-m1. §II.B `sec:bounce` Eq.~\ref{eq:rhocrit} now writes the formula without embedded numerical value, paragraph explicitly says "Ashtekar \& Singh quote the canonical LQC value $\rho_{\rm crit}\simeq 0.41\,\rho_{\rm Pl}$ at the standard LQC area-gap choice $\gamma = 0.2375$, and... substituting the SU(2) black-hole-entropy value $\gamma_{\rm SU(2)}\approx 0.274$ into the same formula gives $\rho_{\rm crit}\simeq 0.27\,\rho_{\rm Pl}$ — labeled explicitly as 'an internal extrapolation across counting schemes (not a value quoted in Ref.~\cite{Ashtekar2011})'." Reviewer re-flagged a closed finding. | **STALE** |

---

## Closures landed in v1A.0.39 (real edits to .tex)

### Edit 1 — PER-m1 (Planck/ACT DR6 birefringence attribution)

The .tex repeatedly framed β_obs = 0.342° ± 0.094° as a "Planck/ACT~DR6 3.6σ joint signal" citing `{Minami2020, Eskilt2022b, DiegoPalazuelos2025}`. Verification against arXiv:

- **Eskilt & Komatsu 2022** (arXiv:2205.13962, Phys. Rev. D 106:063503): WMAP+Planck *joint* analysis; reports β = 0.342° ± 0.094° at ~3.6σ. Title: "Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data." **Not ACT.**
- **Diego-Palazuelos & Komatsu 2025** (arXiv:2509.13654): independent ACT DR6 follow-up; reports β = 0.215° ± 0.074° at ~2.9σ. **Not joint with Planck and not the 0.342° measurement.**

The "Planck/ACT~DR6 joint 3.6σ" framing conflated two distinct measurements. Fix landed at three sites:

**1. Abstract / Results summary (around L233–236)**:
- *Before*: "spectator-ALP birefringence $\beta\approx 0.27^\circ$ consistent with the published Planck/ACT~DR6 $3.6\sigma$ signal arises in any GR+ALP setup"
- *After*: "spectator-ALP birefringence $\beta\approx 0.27^\circ$ consistent with the published Planck (WMAP+Planck joint) $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$ measurement (~3.6σ, Eskilt \& Komatsu~\cite{Eskilt2022b}; with an independent ACT~DR6 follow-up $\beta = 0.215^\circ\pm 0.074^\circ$ at ~2.9σ, Diego-Palazuelos \& Komatsu~\cite{DiegoPalazuelos2025}) arises in any GR+ALP setup"

**2. §IV.D `sec:r4_birefringence` (around L963–965)**:
- *Before*: "equal to the Planck/ACT~DR6 measurement $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$~\cite{Minami2020, Eskilt2022b, DiegoPalazuelos2025}"
- *After*: "equal to the published WMAP+Planck cosmological-birefringence measurement $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$ (~3.6σ from $\beta=0$; \cite{Minami2020,Eskilt2022b}; the independent ACT~DR6 follow-up of Diego-Palazuelos \& Komatsu~\cite{DiegoPalazuelos2025} reports $\beta = 0.215^\circ \pm 0.074^\circ$ at ~2.9σ, consistent within ~1.4σ)"

**3. §`sec:results` Spectator-ALP paragraph (around L1490–1493)**:
- *Before*: "consistent with the published Planck/ACT DR6 $3.6\sigma$ joint signal ($\beta=0.342^\circ\pm 0.094^\circ$, Eskilt~\etal~\cite{Eskilt2022b})"
- *After*: "consistent with the published WMAP+Planck cosmological-birefringence signal ($\beta=0.342^\circ\pm 0.094^\circ$, ~3.6σ from $\beta=0$, Eskilt \& Komatsu~\cite{Eskilt2022b}; an independent ACT~DR6 follow-up~\cite{DiegoPalazuelos2025} reports $\beta=0.215^\circ\pm 0.074^\circ$ at ~2.9σ)"

**4. Mechanical sed pass** on remaining loose "Planck/ACT~DR6 signal" / "Planck/ACT~DR6 sensitivity" / "Planck/ACT~DR6 central value" occurrences at L890–891, L1096, L1673 — all replaced with "WMAP+Planck birefringence signal (with ACT~DR6 follow-up)" / equivalent. Two surviving "Planck/ACT" mentions at L1083 ("published Planck/ACT measurements") and L1598 ("CMB birefringence from published Planck/ACT measurements") are deliberately left as generic survey-instrument references and are not measurement-specific.

Net effect: the false impression of a "joint" 3.6σ Planck+ACT DR6 measurement is removed. The 3.6σ is now correctly attributed to the WMAP+Planck Eskilt 2022 analysis, and the ACT DR6 follow-up of Diego-Palazuelos 2025 is acknowledged separately at its actual β = 0.215° ± 0.074° / ~2.9σ.

---

## STALE / FALSIFIED tally

| Class | Count |
|-------|-------|
| Convergent silence (no findings raised) | 1 reviewer (Grok-4) |
| BLOCKER (called by reviewer) | 6 (GPT-B1, B2, B3, B4, B5, B6) |
| MAJOR (called by reviewer) | 3 (PER-B1, PER-M1, PER-M2) |
| minor (called by reviewer) | 3 (PER-M3, PER-m1, PER-m2) |
| **Total findings ingested** | **12** (1 reviewer + 6 GPT + 5 Perplexity = 12 surfaced; one PER-M3 graded MAJOR-class in the report, treated as minor here per its in-prep-companion nature already-closed) |
| **VERIFIED → CLOSED in v1A.0.39** | **1** (PER-m1) |
| **STALE (paper already addresses)** | **9** (GPT-B1, B2, B3, B5, B6, PER-M1, PER-M2, PER-M3, PER-m2) |
| **FALSIFIED (reviewer claim wrong)** | **1** (PER-B1 — Shapiro-Teixeira paper exists at arXiv:1402.4854) |
| **OPINION-only (framing / polish)** | **1** (GPT-B4 — PTA propagation polish-tier deferral) |

---

## Cumulative cascaded-loop status

- R23 (2026-05-21): 4-of-5 reviewers clean; Gemini's BLOCKER was prompt-meta error.
- R-multi-true95 (2026-06-01): 0 surviving BLOCKER/MAJOR; 2 VERIFIED-MINOR closures.
- R-multi-round2 (2026-06-01): 0 surviving Grok/GPT BLOCKER/MAJOR; 5 Perplexity citation-forensics closures.
- **R-multi-round3 (2026-06-01)**: Grok = convergent silence (explicit PAPER-GRO-SILENCE-1). GPT = 0 surviving BLOCKER/MAJOR (all 6 are restatements of round-1/round-2 findings already closed or labeled). Perplexity = 1 real attribution closure (PER-m1, the Planck/ACT~DR6 conflation), 1 FALSIFIED (PER-B1 ShapiroTeixeira), 3 STALE (closed in v1A.0.37 or v1A.0.38).
- **Consecutive-clean count for Grok+GPT body of the review**: **3 of 3** (R-multi-true95, R-multi-round2, R-multi-round3 all produced zero surviving substantive Grok/GPT findings).
- **Perplexity yield**: round 1 = 2 closures, round 2 = 5 closures, round 3 = 1 closure → monotonic decline, consistent with the citation-strength corrections converging.
- **AGENT_RULES §4.4.1 cascaded-loop-exit criterion** ("zero convergent regressions + zero novel BLOCKERs + ≤1–2 polish-tier MAJORs for 2 consecutive rounds"): **SATISFIED** for the 3rd consecutive round. P1A external-review readiness remains capped at 95% per `feedback_readiness_oscillation` until Houston sign-off.

---

## Recompile receipt

- Command: `pdflatex -interaction=nonstopmode -halt-on-error paper1a_ech_nogo.tex` × 3 passes (in `arxiv/`).
- Output: `arxiv/paper1a_ech_nogo.pdf` — **21 pages, 838,268 bytes**, md5 `4b290d111f03275c88bf5d147f8ad964`.
- LaTeX log: **0 undefined references**.
- Mirror: `site/public/papers/paper1a_ech_nogo.pdf` (latest) + `site/public/papers/paper1a_ech_nogo_v1A.0.39.pdf` (versioned).

## Convex updates

- `paperVersions:bump` → row `k57dbwygjy7hyg5qges7vr928d87x09r`
  (paperSlug=`paper-1a`, version=`v1A.0.39`, datestamp=`2026-06-01`,
  texCommit=`WIP-7097d75ebd1b`, pdfMd5=`4b290d111f03275c88bf5d147f8ad964`,
  pdfPages=`21`, pdfSizeBytes=`838268`, changelog summarises the 1 closure +
  STALE/FALSIFIED block).
- `papers:upsert` → row `k97bk3bj57gm567th3f3qc780d87v1sc`
  (sitePdfPath bumped to `/papers/paper1a_ech_nogo_v1A.0.39.pdf`; focusAreas
  updated with corrected Eskilt 2022 + DiegoPalazuelos 2025 attribution and
  the R-multi-round3 closure line).
- Site re-renders within seconds via Convex subscription on `getLivePapers`.

---

*Generated by R-multi-round3 truth-audit pipeline. Single-commit bundle pending (Houston-owned commit step).*
