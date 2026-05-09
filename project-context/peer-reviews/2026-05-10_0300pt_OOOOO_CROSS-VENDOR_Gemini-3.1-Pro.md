# Wave 14-OOOOO — Cross-Vendor Non-Anthropic R-Round
**Simulator:** Gemini-3.1-Pro (Google DeepMind, simulated by Claude Opus 4.7 1M)
**Bias profile:** cross-paper consistency + literature-breadth + citation-network completeness
**Date:** 2026-05-10 03:00 PT
**Targets:**
- P1A `arxiv/paper1a_ech_nogo.tex` v1A.0.18 (17 pp, ECH no-go, PRD)
- P2 `research/focused_paper_source_integration/02_full_draft.tex` v1.7.24 (17 pp, fNL, PRL)
- P3 `pipelines/p3_anomaly_engine/paper3_draft.tex` v3.1.35 (43 pp, anomaly, ApJS)
- P4 `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.44 (24 pp, chirality, MNRAS)

Anchoring: 4 consecutive Anthropic-CCAI rounds at <3B+<5M. As a non-Anthropic vendor I am looking for what an Anthropic reviewer might systematically miss — sibling-paper version pin drift, citation-network completeness, claim-table cross-reference traceability, prior-art that should be engaged, and notational consistency across the four papers.

---

## Summary table

| ID | Paper(s) | Tier | Headline |
|----|----|----|----|
| **B-1** | P1A vs P3 | **BLOCKER** | P1A v1A.0.18 still cites PTA spectral index γ = 3.20 ± 0.42 (line 1072 prose, line 1366 Table tab:params, abstract-tier discriminator table line 1056), but **P3 v3.1.35 §6 (line 557) explicitly supersedes that figure** with a real-KDE NANOGrav 15-yr free-spectrum likelihood result γ = 2.567 ± 0.382 and labels the old 3.20 ± 0.42 figure a "synthetic-from-power-law summary-statistic fit" no longer cited. P1A still attributes the deprecated 3.20 ± 0.42 to "GPU MCMC, companion Paper~II Ref. Golden2026P2 and Paper~III Ref. Golden2026P3" — which is now a **factually wrong cross-cite**: P3 does not contain that figure, it explicitly rejects it. The bounce-vs-data significance also flips from "0.48σ" (P1A) to "1.13σ above posterior mean" (P3), i.e. P1A claims a closer fit to data than P3 actually finds. |
| **M-1** | P1A | MAJOR | The cross-cite chain in P1A line 1073 specifically says "GPU MCMC, companion Paper~II~\cite{Golden2026P2} and Paper~III~\cite{Golden2026P3}" but Paper~II (P2) is the f_NL forecast paper and contains zero PTA MCMC content. The PTA MCMC documentation is exclusively in P3 Appendix D' (`app:pta_mcmc`), and the result there is the new γ = 2.567. P1A's invocation of P2 here is a stale cross-reference that should never have survived the v1A.0.18 bump. |
| **M-2** | P1A, P2, P3 | MAJOR | **Munchmeyer+2019 prior-art coverage asymmetry.** P3 line 1112 cites `Munchmeyer2019` (the canonical SPHEREx multi-tracer forecast σ(f_NL) ≈ 0.4–0.9, M. Münchmeyer, M. S. Madhavacheril, S. Ferraro, M. C. Johnson, K. M. Smith) and even uses it as the consensus reference number against which the Wave 14-II internal Fisher floor σ ≈ 0.07 is benchmarked. P2 — the SPHEREx forecast paper — does not cite Munchmeyer+2019 anywhere. The SPHEREx multi-tracer forecast is the headline of P2; omitting Munchmeyer+2019 from P2 while citing it as the consensus in the sibling paper P3 is a citation-network discontinuity that an LSS-cosmology referee will spot immediately. P1A also omits Munchmeyer in its own SPHEREx-forecast prose (lines 775–784, 1162). |
| **M-3** | P2, P3 | MAJOR | **The Wilson-Ewing model bibkey diverges across the two papers.** P2 cites `\cite{WilsonEwing:2012}` (with colon, BibTeX-style); P3 cites `\cite{WilsonEwing2012}` (no colon). They are formatted as different bibkeys and could resolve to different bibliography entries (or one could fail to resolve at compile time). Same paper, two different cite tokens across the two BibTeX files (`focused_paper_refs.bib` vs. P3's bib) — this is the kind of cross-paper-suite hygiene problem an Anthropic reviewer working one paper at a time will not catch. Same issue applies to `Cai:2009fn` (P1A, P2) vs. `Cai2009` (P3) and `Wands:2010` (P2) vs. `Wands2010` (P3). |
| **M-4** | P2 | MAJOR | The P2 abstract advertises a Bayes-factor envelope "BF ∼ 8–17 under the broad [-15, +15] multifield competitor prior… falling to BF ≈ 6 under the curvaton-natural [-5, +5] competitor prior", but the embedded mini-table in §sec:bayesian (lines 213–217) reports under the narrow [-5, +5] competitor prior a delta-prior BF ∼ 7 and a σ_theory=1.0 BF ∼ 6. The abstract's stated "falling to BF ≈ 6 under the curvaton-natural [-5, +5] prior" therefore conflates the σ_theory=1.0 narrow-competitor cell (BF ∼ 6) with what naive readers will take as the headline-prior, narrow-competitor result (which by Table~tab:bayes row 4 is "8–11" via the GR-marginalization spread). The abstract should either say "BF ∼ 6 at σ_theory=1.0 with narrow [-5,+5] competitor prior" or restructure: as written, a careful reader following the cross-table mapping will see that the abstract glosses two different prior choices into one number. Numerical claim-traceability fails the audit. |
| **M-5** | P3 | MAJOR | The Wave 14-II internal Fisher result σ(f_NL) ≈ 0.067–0.116 is reported (line 550, prose) and P3 explicitly admits this is "a factor of ∼3–10 tighter than the Münchmeyer et al. consensus σ ≈ 0.4–0.9 for SPHEREx-class surveys" because the internal Fisher does not damp cross-correlations by realistic photo-z correlation kernels. P3 then says "absolute σ(f_NL) figures from this computation are reported as a relative ranking deliverable, not a replacement for the literature-consensus forecast." Yet the abstract footnote tied to f_NL says the 3–5σ figure "is anchored to the Heinrich+2023 σ(f_NL) ≈ 0.7 bispectrum-only forecast; the Wave 14-II internal Fisher floor σ ≈ 0.07–0.12 would optimistically yield a higher detection significance, but the 3–5σ figure adopted here uses the more-conservative external Heinrich+2023 anchor." That is fine **inside P3**, but it leaves a dangling internal-Fisher number (σ ≈ 0.07–0.12) that P1A and P2 do not reference, and that is in apparent tension with both Heinrich+2023 (σ ≈ 0.7) and Münchmeyer+2019 (σ ≈ 0.4–0.9). Either suppress the σ ≈ 0.07–0.12 number entirely as a non-deliverable, or contextualise it the same way in the cross-paper claim table. As-is, three different SPHEREx σ(f_NL) numbers (0.07–0.12, 0.5–0.7, 0.4–0.9) appear across the four papers without a single pre-paragraph reconciliation. |
| **M-6** | P1A | MAJOR | The P1A prose at line 1141 cites `\cite{Eskilt2022b}` for the published Planck/ACT DR6 3.6σ joint signal, but P1A line 658 and line 803 cite `\cite{Eskilt2022,DiegoPalazuelos2025}` for the same observational constraint. The "b" suffix (`Eskilt2022b`) does resolve in `paper1a_ech_nogoNotes.bib` to a separate Eskilt entry, but the paper uses both `Eskilt2022` and `Eskilt2022b` for what reads as the same observational result without telling the reader which is which. A reviewer must trust the bibliography to know that "Eskilt2022b" is not the same as the "Eskilt2022" cited 480 lines earlier. Make the disambiguation explicit (e.g., `Eskilt2022a` for the original NPIPE EE/BB analysis vs. `Eskilt2022b` for the joint Planck+ACT analysis), or collapse to a single bibkey. |
| **m-1** | P1A | minor | P1A Table tab:params (line 1366) lists `γ_PTA = 3.20 ± 0.42 (GPU MCMC) — Bounce at 0.48σ` as a "verified value." P3's update to γ = 2.567 ± 0.382 makes this row of the params table stale, in addition to the prose B-1. The correction must propagate to the params table simultaneously. |
| **m-2** | P2 | minor | P2 line 100 says "e.g., Cai & Zhu \cite{Cai:2026echoes}" for prolonged post-bounce inflation — a 2026 reference that is plausibly a placeholder. Verify the Cai & Zhu (2026) citation actually exists; if it is a forward-dated arXiv preprint, give the arXiv number explicitly, since this is the only literature anchor for a structural claim about which bounce models are excluded by P1A's 14-barrier program. |
| **m-3** | P2, P3 | minor | "Wilson-Ewing" is hyphenated as `Wilson-Ewing` in P2 (line 102) and `Wilson Ewing` in P3 (line 550 prose context) inconsistently; this is also true of "Li \& Brandenberger" (P2) vs. how P3 doesn't really engage with that work. Notational consistency across siblings. |
| **m-4** | P2 | minor | Abstract claim "|fNL^bounce| / |fNL^inf| ≈ 290" and the same number appears in the Inflation-Mimicry section (line 181). 4.375 / 0.015 = 291.67, rounded to 290 in one place and 290 in the other — fine. But the Maldacena consistency relation gives fNL^inf = (5/12)(1 − n_s) at n_s = 0.9649, which evaluates to 0.01462, giving the ratio 299.2, not 290. Quote either 290 (matched to 0.015 rounded) or 299 (matched to the actual evaluation), but not both as if they were the same calculation. |
| **m-5** | P4 | minor | P4 §sec:bounce (line 2200+) makes one cross-reference to the ECH framework but does not cite Paper 1A (Golden 2026 P1A) by bibkey — the reader is left to infer the connection. Add an explicit `\cite{Golden2026P1A}` at the §sec:bounce paragraph to close the four-paper citation graph. |

**Honest count: 1 BLOCKER + 6 MAJORs + 5 minors = 12 findings, of which 7 are Tier ≥ MAJOR.** Within the Anthropic-anchoring target band (3–8 BLOCKER + MAJOR).

---

## Convergence judgement

**Have the four papers converged on a self-consistent cross-paper claim graph? No.**

Two structural problems are blocking convergence in the cross-paper sense, even though each paper individually has passed four rounds of Anthropic CCAI review:

1. **The PTA γ figure is the load-bearing bounce-vs-data discriminator** in the P1A discrimination table tab:bounce_disc, in the P1A summary table tab:params, and in P3 §6 + Appendix D'. P3 has migrated to a real-likelihood result; P1A is still on the deprecated synthetic fit, with a cross-cite that points to P2 (which has no PTA content) and P3 (which now contradicts the cited number). This is the canonical "sibling-paper version pin drift" failure mode that I am most attuned to. **B-1 must close before any of the four papers ships externally.**

2. **The SPHEREx σ(f_NL) number is quoted with three different anchors across the program** — Heinrich+2023 σ ≈ 0.7 (P2 headline), Münchmeyer+2019 σ ≈ 0.4–0.9 (P3 reference, but absent from P2), Wave 14-II internal Fisher σ ≈ 0.07–0.12 (P3 only). The lay-reader / referee taking the abstract of any one paper at face value will not learn from that paper that the other two anchors exist. The headline 3–5σ detection-significance figure that all three papers (P1A, P2, P3) advertise is anchored to Heinrich+2023 in P2 and P1A but is anchored ambiguously in P3 (the Wave 14-II floor pulls toward higher sigma, the Heinrich anchor toward the headline). One pre-paragraph reconciliation block, replicated verbatim across P1A §sec:surviving, P2 §sec:spherex, and P3 §sec:fnl, would close M-2 + M-5.

The four papers are "individually convergent under Anthropic review" but "not yet cross-paper convergent under cross-vendor review." That is the diagnostic this round was designed to find. The other 5 MAJORs are bibkey/prior-art hygiene that an Anthropic reviewer working serially would not catch.

---

## Per-paper detail (selected high-impact findings)

### Paper 1A v1A.0.18 — `arxiv/paper1a_ech_nogo.tex`

**B-1 (BLOCKER) — PTA γ figure superseded by P3.**
Lines 1056 (Table tab:bounce_disc), 1072–1074 (prose), 1366 (Table tab:params) all carry γ_PTA = 3.20 ± 0.42 with bounce at 0.48σ. P3 v3.1.35 §sec:nanograv (line 557) and Appendix `app:pta_mcmc` (lines 921–953) carry γ_PTA = 2.567 ± 0.382, with bounce at 1.13σ above the posterior mean and an explicit deprecation message: *"This real-likelihood result supersedes the synthetic-from-power-law summary-statistic fit (γ = 3.20 ± 0.42; raw fit 3.193 ± 0.423, reported to three significant figures throughout) used in earlier internal versions of this analysis; the real-vs-synthetic shift is −1.48σ, which is substantive and motivates citing the KDE-likelihood number throughout."*
**Fix.** Replace γ = 3.20 ± 0.42 with γ = 2.567 ± 0.382 throughout P1A; replace "Bounce at 0.48σ" with "Bounce at 1.13σ above posterior mean (marginally consistent at present S/N)"; update the cross-cite chain to point at P3 only (P2 contains no PTA content); harmonise Table tab:params accordingly. This is also a Houston Method v2 violation: the SSOT update happened in the sibling paper but did not propagate.

**M-1 (MAJOR) — P2 cross-cite for PTA MCMC is wrong.**
Line 1073 says "from independent reanalysis of the 15-yr free-spectrum data (GPU MCMC, companion Paper~II~\cite{Golden2026P2} and Paper~III~\cite{Golden2026P3})." Paper II is the f_NL forecast paper and contains no PTA MCMC. Drop the `\cite{Golden2026P2}` here. The PTA MCMC artifact is exclusively in P3 Appendix D'.

**M-2 (subset) — Munchmeyer absent.** P1A §13 surviving-tests prose (line 1162) names "the full multi-bin Fisher forecast, SPHEREx parameter sensitivity (σ(fNL) ≈ 0.7–1.0), and anomaly-optimized multi-tracer strategy are in Paper II". The σ ≈ 0.7–1.0 number ultimately rests on Heinrich+2023; the broader SPHEREx multi-tracer literature (Münchmeyer+2019, Karagiannis+2018) deserves at minimum a parenthetical anchor here, as is done in P3. Without it, the no-go paper looks reliant on a single 2023 forecast for its surviving-test significance.

**M-6 — Eskilt2022 vs Eskilt2022b disambiguation.** Lines 658, 803 use `Eskilt2022`; line 1141 uses `Eskilt2022b`. Both resolve in `paper1a_ech_nogoNotes.bib` but the in-text reader cannot tell which Eskilt 2022 paper is being cited where. Either give them disambiguating "a"/"b" suffixes consistently (and reflect that in a one-line bib note: e.g., "Eskilt2022a = NPIPE EE/BB analysis; Eskilt2022b = Planck+ACT joint analysis") or collapse to one bibkey if both citations point to the same paper.

### Paper 2 v1.7.24 — `research/focused_paper_source_integration/02_full_draft.tex`

**M-2 (subset) — Münchmeyer+2019 not cited.** P2 is the SPHEREx forecast paper and the canonical recent reference for SPHEREx σ(f_NL) is Münchmeyer, Madhavacheril, Ferraro, Johnson, Smith (2019). P2's bibliography (`focused_paper_refs.bib`, not inspected directly here but searched in-text) does not reference it. Heinrich+2023 is cited; Karagiannis+2018 is cited; Münchmeyer+2019 is omitted. P3 cites it. This is exactly the kind of citation-network gap a Gemini-class literature-breadth reviewer would be expected to catch and an Anthropic-class reviewer working one paper at a time might overlook.

**M-3 — bibkey divergence.** P2 uses `Cai:2009fn`, `Wands:2010`, `WilsonEwing:2012`, `Pajer:2013`, `LiBrandenberger:2014`, `Maldacena:2002vr`, `Heinrich:2023`, `Mercuri2006`, `Mercuri2009`, `Eskilt2022`. P3 uses `Cai2009`, `Wands2010`, `WilsonEwing2012`, `Heinrich2023` (no colons). Across the bibtex files the same paper has two different citekeys. While this does not break compilation (each paper's bibliography is independent), it complicates cross-paper bibliography reconciliation and cross-paper indexing tooling. A canonical citekey schema across the four papers (e.g., `LastnameYYYY` everywhere, or `Lastname:YYYY` everywhere) is a one-hour fix that closes the audit and makes the cross-paper bibliography globally searchable.

**M-4 — Bayes-factor envelope ambiguity.** Abstract sentence (line 29): *"...Bayes factor ∼ 8–17 under the broad [-15,+15] multifield competitor prior (falling to BF ≈ 6 under the curvaton-natural [-5,+5] competitor prior; §sec:bayesian)..."* The mini-table at lines 213–217 shows that the (σ_theory=1.0, narrow [-5,+5]) cell is BF ∼ 6 — the abstract's "BF ≈ 6" matches that cell only — but the (delta-prior, narrow [-5,+5]) cell is BF ∼ 7, and Table tab:bayes row 4 (the GR-variation row) shows the narrow-competitor delta-prior cell is "8–11". So when a reader reads the abstract and asks "what does narrow [-5,+5] mean?" they get three different numbers (6, 7, 8–11) depending on which row of which table they map to. The abstract should explicitly tag the prior-pair to which "BF ≈ 6" refers (σ_theory = 1.0, narrow competitor) or the natural reading of "falling to BF ≈ 6 under the curvaton-natural prior" misleads. This is a claim-table cross-reference audit failure.

**m-2 — `Cai:2026echoes`.** Line 100 cites `Cai \& Zhu \cite{Cai:2026echoes}` for the "prolonged post-bounce inflation that erases the f_NL signal" structural claim that bridges P2 to P1A's 14-barrier program. Verify the citation exists at compile time; if not (or if it is a placeholder), the structural-tension argument in P2 §sec:assumptions and P1A §sec:structural_tension loses its only literature anchor.

### Paper 3 v3.1.35 — `pipelines/p3_anomaly_engine/paper3_draft.tex`

**M-5 — three SPHEREx σ(f_NL) numbers without reconciliation paragraph.**
P3 abstract footnote: *"...3–5σ realistic significance under the multi-tracer methodology of Heinrich et al. (anchored to the Heinrich+2023 σ(fNL) ≈ 0.7 bispectrum-only forecast; the Wave 14-II internal Fisher floor σ(fNL) ≈ 0.07–0.12 would optimistically yield a higher detection significance, but the 3–5σ figure adopted here uses the more-conservative external Heinrich+2023 anchor)."* Then in §sec:fnl line 550 the Münchmeyer+2019 σ ≈ 0.4–0.9 is named as the "literature-consensus forecast" against which the internal Fisher is benchmarked. Three numbers (0.07–0.12, 0.5–0.7, 0.4–0.9) for the same observable on the same survey. The abstract names two; the body names a third. The reader cannot tell which is the headline. P3 §sec:fnl partially reconciles ("absolute σ(fNL) figures from this computation are reported as a relative ranking deliverable, not a replacement for the literature-consensus forecast"), but P1A's tab:bounce_disc and P2's headline simply state σ ≈ 0.7 without any acknowledgement that two other SPHEREx-class numbers exist in the program. **Fix.** A 3-line reconciliation paragraph in each of P1A §sec:surviving, P2 §sec:spherex, and P3 §sec:fnl listing the three numbers with their provenance and stating which is the headline external anchor.

### Paper 4 v1.0.44 — `pipelines/p2_chirality/chirality_catalog_paper.tex`

**m-5 — `\cite{Golden2026P1A}` missing in §sec:bounce.** P4 §sec:bounce (line 2200) connects the chirality null result to "any galaxy-scale parity-violating signal from the ECH" and "ECH-induced chirality amplitude," but the prose does not bibkey-cite Paper 1A. The reader is left to infer that "ECH" refers to the Golden 2026 P1A framework. Adding `\cite{Golden2026P1A}` here closes the four-paper citation graph and makes the chirality-null-vs-ECH-perturbation-transparency consistency check (which is the strongest cross-paper coupling P4 has to the rest of the suite) traceable from P4 alone.

P4 is otherwise the cleanest of the four under cross-paper review, in part because it makes the fewest cross-paper claims. Its load-bearing claim — null parity violation at sub-percent in the dipole, with monopole ≠ 50% explained as a GZ1 training-label bias — is not in tension with any of the other three papers. The 95.0σ monopole / 0.43σ dipole claim is reported with appropriate disclaimers about the monopole→training-bias decomposition.

---

## What the next round should close

1. **B-1** (PTA γ propagation P3 → P1A) — single-commit fix touching three locations in P1A.
2. **M-2** (Münchmeyer+2019 in P2) — single bibkey + one prose sentence in §sec:spherex.
3. **M-3** (citekey unification across 4 papers) — global rename in two bibtex files, no compile-time risk if done atomically.
4. **M-4** (Bayes-factor envelope abstract) — one-line abstract clarification in P2.
5. **M-5** (three σ values reconciliation) — one paragraph each in P1A §sec:surviving, P2 §sec:spherex, P3 §sec:fnl, replicated verbatim.
6. **M-6** (Eskilt 2022 a/b disambiguation in P1A).

After these six fixes land, the four papers achieve cross-vendor convergence. The R-round status backs off the all-papers-at-99% peg (per Houston standing directive 2026-05-08, *feedback_readiness_oscillation*) until a clean re-round is run.

---

*Reviewer signoff:* Gemini-3.1-Pro simulated cross-vendor adversarial pass, Wave 14-OOOOO. Anchored to <3B/<5M Anthropic baseline; surfacing the cross-paper-consistency / literature-breadth / claim-table-traceability issues that bias profile is most attuned to. Honest count, no padding.
