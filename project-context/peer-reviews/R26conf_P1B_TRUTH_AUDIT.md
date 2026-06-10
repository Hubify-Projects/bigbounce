# R26conf P1B — TRUTH AUDIT (v1B.0.53 → edits applied 2026-06-10)

Auditor: in-session Claude. Ground truth: `arxiv/paper1b_mcmc_companion.tex`, `.bbl`, committed chains (`reproducibility/cosmology/iter2_converged_2026-05-18/`, `research/branch_R_alp_birefringence/phase2_mcmc/`), `c10b_alp_envelope_scan.json`, `alp_ode.py`.

Independent recomputes performed this audit: (i) full iter2 chain readout (30% burn-in, weighted): σ8=0.8057±0.0083, Ωm=0.3142±0.0045, S8=0.8245±0.0089, χ²_tot=14037.4±5.61, channel χ² 10.6±1.79 / 10983.9±5.27 / 3043.0±1.59 — **every Table II number reproduces exactly**; ρ(σ8,Ωm)=−0.27; channel-χ² correlations −0.09/−0.03/+0.04. (ii) Independent fixed-step RK4 of the ALP EOM: Δφ/fa=1.0601 at (θi=1, m=3.9H0) — matches committed artifact to 4 s.f. (iii) CPL crossing arithmetic (below).

| Finding | Class | Verdict | Action |
|---|---|---|---|
| INSESSION M1 (marg.-tail caveat not on w_a row / prose) | presentation | VERIFIED-PARTIAL | CLOSED: fn:wcaveat ref added to w_a Table II row; §V.B prose sentence already carries "(in the marginal-tail sense; see fn)"; conclusions L1468 already refs fn at w0 |
| INSESSION M2 (χ² σ=5.6 vs quadrature 5.83 unexplained) | presentation | VERIFIED (premise corrected) | CLOSED with chain-verified text: channel correlations are weakly **negative** (−0.09/−0.03/+0.04), so σ_tot=5.61 sits *below* quadrature 5.79 — reviewer's "positive correlation" inference was backwards; footnote (c) now states the measured correlations |
| INSESSION M3 (phantom crossing at z*=−0.22, "outside data range") | claim-truth | **FALSIFIED — reviewer sign-slip** | Correct algebra: w(a)=w0+wa(1−a)=−1 ⇒ 1−a*=(−1−w0)/wa=(−1+0.8122)/(−0.6666)=+0.2817 ⇒ a*=0.7183 ⇒ **z*=+0.392, INSIDE the data range**. Reviewer computed a*=1−(1+w0)/wa=1.282 (sign error: a*=1+(1+w0)/wa). Trajectory is phantom at z>0.39, quintessence-like today — opposite of reviewer's "w<−1 today". Paper's L982 prose was CORRECT; strengthened with explicit z_×≈0.39 arithmetic so the claim is self-auditing |
| INSESSION M4 (σ_S8=0.0089 < uncorrelated 0.0103 unexplained) | presentation | VERIFIED | CLOSED: chain readout confirms ρ(σ8,Ωm)=−0.27; caption sentence added with the measured correlation |
| INSESSION M5 (Δφ/fa=1.06 lacks cross-check) | reproducibility | VERIFIED | CLOSED: independent RK4 re-integration actually run this audit (1.0601 to 4 s.f.); cross-check line added at Eq.(3) site |
| INSESSION m1 (−0.032° presented before worst case) | presentation | VERIFIED | CLOSED: §IV results paragraph now leads with worst-case ≤0.040° floor |
| INSESSION m2 (Fig 3 σ_β disclaimer missing in caption) | presentation | STALE | Caption already carries the fsky=0.32 σ_β disclaimer + 0.046° rerun |
| INSESSION m3 (28% truncation uncited to run2_extended) | presentation | VERIFIED | CLOSED: in-line "(run2_extended chain of Appendix C)" added |
| INSESSION m4 (5× "no torsion" repetition) | presentation | VERIFIED | CLOSED-PARTIAL: §I copy reduced to pointer; abstract + §III scope statement retained (load-bearing); brief conclusions/appendix mentions retained for self-containment |
| INSESSION m5 (Liu et al. implication unstated) | presentation | VERIFIED | CLOSED: parallel-null sentence was present; added AIC non-comparability sentence (model comparison deferred to nested sampling) |
| OpenAI E3 (caveat (c) H0=67.185 "wrong chain") | claim-truth | FALSIFIED-AS-STATED | Caveat block follows and refers to the iter2 w0wa chain — value is correct for its chain; ambiguity removed by adding explicit chain labels + the ΔNeff-chain 67.79±1.09 contrast |
| OpenAI E4 (missing exponent-2 in √(1.09²+0.32²)) | claim-truth | FALSIFIED | Source has `\sqrt{1.09^2+0.32^2}`; renders correctly — pdftotext artifact |
| OpenAI M6 (Fig 4 caption "EOM-required minimum 8.6" vs [4,60] prior) | presentation | VERIFIED | CLOSED: caption now states 8.6 is the minimum to reach the *central* β=0.342° at Δφ/fa=1.19, and why [4,8.6) stays supported |
| OpenAI M7 (0.33% vs 42/8955=0.47%) | claim-truth | VERIFIED (both numbers correct) | CLOSED: weighted-vs-count clarifier added |
| OpenAI M8 (Fig 1 caption vs fn sample counts) | presentation | STALE | fn:sample_stratification already reconciles 119,617 thinned vs 123,368 post-burnin |
| Gemini E3 (chains not available) | reproducibility | VERIFIED (appendix outdated) | CLOSED: Appendix A now states iter2 bundle + ALP chains ARE committed; only ΔNeff proxy chains regenerate-only |
| Gemini N1 (fn says SNR∝fsky) | claim-truth | FALSIFIED | fn:snr_definition uses 20.32√(fsky/0.32) — already √ scaling |
| Gemini E1/E2, Grok E2/N1, Perplexity E6/E8, OpenAI m2 (correction-notes / Table IV claims-classification removal) | presentation | HOUSTON-DECISION | Deliberate transparency artifacts; not auto-removed |
| Perplexity E1/E2/E5 (future-dated arXiv IDs, ACT DR6 2509.13654) | citations | AUTO-FALSIFIED | Project dating rule; `.bbl` entries verified incl. ECTorsionDESI2025 (Liu+ EPJC 2025, arXiv 2507.04265 — 6th re-flag) |
| Perplexity E3/E4 (companion papers unverifiable) | process | FALSIFIED/STALE | Companions in-repo, posted concurrently; multi-round prior adjudication |
| Grok E1/E3, M1/M2; Perplexity M1–M3, m1–m4; OpenAI M1–M5, m-series | scope/robustness/length | STALE/OPINION/QUEUED | Scope disclaimers already at every flagged site; length + AI-acknowledgment = editorial/Houston; Grok M1 amplitude-independence: paper states ~12% multiplicative (0.119 vs 0.117 — consistent) |
| META E1/E2, M1–M7, m1–m5 (bandpower covariance, visibility weighting, √2 noise, α-injection, 1/f, splits, ΔNeff prior, Yp, β-prior symmetry, TB, binning) | recompute/experiment | QUEUED | Method-extension robustness runs, not verified errors; none falsifies a committed number. Queue rows for the NaMaster c-series + ΔNeff prior-swap reruns |

**No substantive verified number/claim-truth/reproducibility error survived audit; all verified items were presentation/traceability and closed same-day. The lone substantive accusation (M3) is falsified with shown arithmetic.**
Recompile after closures: 16 pp, 0 errors, 0 undefined refs, 0 overfull hboxes.
