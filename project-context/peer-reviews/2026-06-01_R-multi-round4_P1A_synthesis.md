# P1A R-multi-round4 — Truth-Audit Synthesis (no version bump; stands at v1A.0.39)

**Round**: `2026-06-01_R-multi-round4`
**Paper**: P1A — Structural Closure of Einstein–Cartan–Holst Dark Energy
**Source**: `arxiv/paper1a_ech_nogo.tex`
**Pre-round version**: v1A.0.39 (post-round-3 citation regression fix)
**Post-closure version**: **v1A.0.39 (unchanged; 0 VERIFIED findings)**
**Reviewers**:
- Grok-4 (direct vendor; brutal-honesty persona) — 1 polish + 3 OPINION
- GPT-4o (FALLBACK from gpt-5; methodology rigor persona) — 6 restatements
- Perplexity Sonar Pro (direct vendor; citation forensics) — 5 false-FABRICATION calls + 1 attribution polish
- Gemini-2.5-pro: skipped per Houston standing protocol (vendor billing failure; 3-of-4 acceptable with prior convergent silence)

Standing protocol applied: `memory/feedback_peer_review_truth_audit_protocol.md`.
Prior syntheses:
- `2026-06-01_R-multi-true95_P1A_synthesis.md` (v1A.0.36 → v1A.0.37, 2 closures)
- `2026-06-01_R-multi-round2_P1A_synthesis.md` (v1A.0.37 → v1A.0.38, 5 closures)
- `2026-06-01_R-multi-round3_P1A_synthesis.md` (v1A.0.38 → v1A.0.39, 1 closure)

---

## Truth-audit table

| Finding | Class | Reviewer claim (paraphrase) | On-disk verification (v1A.0.39) | Verdict |
|---------|-------|-----------------------------|---------------------------------|---------|
| GRO-B1 | polish | Drop redundant "Planck" parenthetical in Eskilt 2022 birefringence attribution | Round-3 edit already reads "WMAP+Planck joint" with Eskilt 2022 as the source; the parenthetical "Planck" inside "Planck (WMAP+Planck joint)" is a deliberate cross-reference to the survey instrument, not a duplicated claim of a separate Planck-only measurement. Polish-tier rephrase. | **STALE / OPINION** |
| GRO-M1 | polish | Title still says "No-Go Theorem" — should add "Channel-Level Amplitude No-Go (Not Operator-Basis)" | Title-vs-scope retitle is restated from round-1 GRO-B1 and round-2 GRO-B1. The abstract L237 already reads "channel-level closure, not an operator-level theorem"; §IV Scope paragraph and §IV.E summary inline-list the omitted Jackiw–Pi + parity-odd 4-fermion operators; §X `sec:transparency` is the formal perturbation-transparency theorem (claim + 5-step proof). The on-disk usage of "no-go" is *to the channel-level enumeration*; the formal theorem is separately labeled. Retitle is preference, not load-bearing. | **STALE / OPINION** |
| GRO-n1 | nit | §sec:structural_tension still reads as independent closure despite "robustness check" label | L1648 is *literally titled* "Structural Tension: Dark Energy vs.\ Bounce $\fnl$ (robustness check, not co-equal closure)". Round-1 GRO-M2, round-2 GRO-B2, round-3 GPT-B5 all reflagged the same; verdict on each was STALE. | **STALE** |
| GRO-n2 | nit | "ansatz-independent" wording on the 120-order hierarchy should soften to "robust to O(1) ansatz variations" | Appendix `app:dimensions` already says "robust to O(1) ansatz variations at the order-of-magnitude level" in framing the 120-order hierarchy. The "ansatz-independent" language Grok is critiquing does not appear verbatim in the v1A.0.39 appendix. | **STALE** |
| GPT-B1 | BLOCKER | Channel-level vs operator-level closure not sufficiently emphasized | Restatement of round-1 GRO-B1, round-2 GRO-B1, round-3 GPT-B1. Abstract L237 verbatim "channel-level closure, not an operator-level theorem". §IV Scope L608–627 explicit channel-level enumeration. §IV.E summary inline-lists Jackiw–Pi + parity-odd 4-fermion as explicitly NOT closed. 4 rounds, same finding, same on-disk caveat. | **STALE** |
| GPT-B2 | BLOCKER | Parity-odd Eq.(4.7) is phenomenological ansatz; expand limitation discussion | Restatement of round-1 GPT-B1, round-2 GPT-B1, round-3 GPT-B6. §II.B.2 `sec:parityodd` L536: "naive mass dimension $[\mathcal{L}_{\rm odd}] = +1$---three units short of the required $+4$ ... $\rho_\Lambda = \Xi\,\MPl^4$ is therefore a *scaling ansatz*, not a controlled EFT calculation." Appendix `app:dimensions` full audit. | **STALE** |
| GPT-B3 | BLOCKER | Route 2 one-loop graviton corrections dimensionally inconsistent | Restatement of round-1 GPT-B2 and round-3 GPT-B2. §IV.B `sec:r2_oneloop` carries the dimensionless reduction with H_0/M_Pl ~ 10^{-61} and (α/M)·M_Pl ~ 10^{-2} explicit. Closed in v1A.0.24/v1A.0.25 and re-anchored in v1A.0.34. | **STALE** |
| GPT-M1 | MAJOR | Null-galaxy-spin result needs more statistical detail | This is a forward-reference to Paper IV (chirality catalog) and is correctly labeled "consistent with null prediction; quantitative confidence interval is reported in Paper IV, not in this structural argument". The structural no-go is independent of the chirality numerical confidence; the citation is a consistency check. Asking for Paper IV's CI table inside Paper I(A) is out-of-scope. | **OPINION** |
| GPT-M2 | MAJOR | Barriers 8 and 14 not logically independent; merge | Restatement of round-1 GPT-M2 and round-2 GRO-M2. The paper *literally* says "13 logically-independent barriers (14 historical catalog entries, of which B8 is subsumed by B14)" at abstract L245, intro L259, §VII summary L317, conclusion L1551 + L1673, conclusion L1699. The merge is **already done in the count**; the catalog preserves B8 as a historical entry. | **STALE** |
| GPT-n1 | nit | Appendix B "phenomenological dimensional assignment" downplays the dimensional inconsistency | Appendix `app:dimensions` L1827 already says "*phenomenological dimensional assignment*, not a derivation". Round-3 GPT-B6 raised the same; STALE then, STALE now. | **STALE** |
| PER-BLOCKER-1 | BLOCKER | "Mis-cited Shapiro-Teixeira: arXiv:1402.4854 is not Shapiro-Teixeira" | **FALSIFIED.** Verified arXiv:1402.4854 is exactly "Quantum Einstein-Cartan theory with the Holst term" by I.L.~Shapiro and P.M.~Teixeira (2014), hep-th + gr-qc, published as CQG 31:185002 (DOI 10.1088/0264-9381/31/18/185002). The bbl entry (`paper1a_ech_nogo.bbl` `ShapiroTeixeira2014`) matches in author, title, journal, volume, pages, year, arXiv ID. Perplexity's web search returned a stale or wrong result; the same finding was raised and FALSIFIED in round 3 (PER-B1, same paper, same false alarm). | **FALSIFIED** |
| PER-MAJOR-1 | MAJOR | "Liu et al. EC torsion DESI / S8 paper doesn't exist as described" | **FALSIFIED.** Verified Liu, Li, Xu, Biesiada, Wang (2025), "Torsion cosmology in the light of DESI, supernovae and CMB observational constraints", *Eur. Phys. J. C* 85:1351, arXiv:2507.04265. The bbl key `ECTorsionDESI2025` resolves to this exact paper. Tension-related result (the paper analyzes DESI BAO + Pantheon+ SNe + CMB to constrain torsion cosmology) is correctly characterized. | **FALSIFIED** |
| PER-MAJOR-2 | MAJOR | "Legner et al. torsion condensation paper doesn't exist" | **FALSIFIED.** Verified Legner, Handley, Barker, Ormondroyd (2025), "Alleviating the Hubble tension with Torsion Condensation (TorC)", JCAP 03(2026)003, arXiv:2507.09228. Bbl key `Legner2025` resolves correctly. | **FALSIFIED** |
| PER-MAJOR-3 | MAJOR | "Alam et al. non-singular bounces in modified gravity uncited/unclear" | **FALSIFIED.** Verified Alam, Sen, Sengupta (2025), "Bouncing cosmologies in modified gravity with space time torsion", *Eur. Phys. J. C*, arXiv:2509.03508. Bbl key `Alam2025bounce` resolves correctly. | **FALSIFIED** |
| PER-MAJOR-4 | MAJOR | "Cai & Zhu 2026 echoes and Papanikolaou 2024 PBH look fabricated or misdated" | **FALSIFIED on both.** (a) Cai & Zhu 2026 echoes — verified Zhu & Cai (2026), "Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves", arXiv:2603.13924, astro-ph.CO. Bbl key `Cai:2026echoes` resolves correctly. (b) Papanikolaou et al. 2024 PBH — verified Papanikolaou, Banerjee, Cai, Capozziello, Saridakis (2024), "Primordial black holes and induced gravitational waves in non-singular matter bouncing cosmology", JCAP 06:066, arXiv:2404.03779, DOI 10.1088/1475-7516/2024/06/066. Bbl key `Papanikolaou:2024pbh` resolves correctly. | **FALSIFIED** |
| PER-minor-1 | minor | Heinrich+2024 σ(fNL)≈0.7 with downstream-degradation chain is attribution-blurred | Table~\ref{tab:summary} footnote `^b` L357–360 already says "3–5σ realistic after full systematic budget (GR-projection, $b_\phi$ uncertainty, photo-$z$ degradation) under Heinrich+2024 $\sigma(\fnl)\approx 0.7$" and routes it through Paper II's forecast pipeline ("Paper II forecast"). Heinrich is the σ baseline, the degradation chain is labeled Paper II. Already disambiguated. | **STALE / OPINION** |

---

## Closures landed in v1A.0.40

**None.** Zero VERIFIED findings in round 4. The paper stands at v1A.0.39.

Per the round-4 triage protocol:
- 0 VERIFIED → **no version bump, no recompile, no PDF re-mirror, no Convex bump.**
- Clean-count advances by 1.

---

## STALE / FALSIFIED tally

| Class | Count |
|-------|-------|
| Total reviewer findings ingested | 16 (4 Grok + 6 GPT + 5 Perplexity + 1 Perplexity minor) |
| **VERIFIED → CLOSED in v1A.0.40** | **0** |
| **STALE (paper already addresses, restatement of prior STALE finding)** | **10** (GRO-B1, GRO-M1, GRO-n1, GRO-n2, GPT-B1, GPT-B2, GPT-B3, GPT-M2, GPT-n1, PER-minor-1) |
| **FALSIFIED (reviewer claim wrong; arXiv ID + bbl checked)** | **5** (PER-BLOCKER-1, PER-MAJOR-1, PER-MAJOR-2, PER-MAJOR-3, PER-MAJOR-4) |
| **OPINION-only (framing / polish)** | **1** (GPT-M1 — Paper IV chirality CI cross-reference) |

---

## Citation-forensics false-FABRICATION pattern

Perplexity Sonar Pro raised **5 BLOCKER/MAJOR findings** in round 4 alleging citations were fabricated, fused metadata, or placeholders. All 5 were verified against arXiv directly (via WebFetch) and found to be real, correctly-attributed published or arXiv-posted papers:

| Bbl key | Verified arXiv | Verified venue |
|---------|----------------|----------------|
| `ShapiroTeixeira2014` | arXiv:1402.4854 | CQG 31:185002 (2014) |
| `ECTorsionDESI2025` (Liu et al.) | arXiv:2507.04265 | EPJC 85:1351 (2025) |
| `Legner2025` | arXiv:2507.09228 | JCAP 03(2026)003 |
| `Alam2025bounce` | arXiv:2509.03508 | EPJC (2025) |
| `Cai:2026echoes` (Zhu & Cai) | arXiv:2603.13924 | astro-ph.CO (2026) |
| `Papanikolaou:2024pbh` | arXiv:2404.03779 | JCAP 06:066 (2024) |

This is a **vendor reliability pattern**: Perplexity's low-context citation-forensics search rejects citations it doesn't surface in its own search index even when the bbl carries the correct arXiv ID. Three of the five (ShapiroTeixeira2014, ECTorsionDESI2025, Legner2025) were also falsely flagged in round 3 and verified there too — the same false alarms are recurring across rounds. Standing protocol `feedback_peer_review_truth_audit_protocol.md` (truth-audit before closure) is doing its job; without it these would have been false closures inflating the changelog.

---

## Cumulative cascaded-loop status

- R-multi-true95 (round 1, 2026-06-01): 2 VERIFIED closures
- R-multi-round2 (round 2, 2026-06-01): 5 VERIFIED closures
- R-multi-round3 (round 3, 2026-06-01): 1 VERIFIED closure
- **R-multi-round4 (round 4, 2026-06-01): 0 VERIFIED closures**
- Closure-yield trajectory: 2 → 5 → 1 → 0 (monotone decline as expected for a paper converging to clean-cross-vendor steady state).

### Clean-count for cross-vendor-r-round exit criterion

AGENT_RULES §4.4.1 ("zero convergent regressions + zero novel BLOCKERs + ≤1–2 polish-tier MAJORs for 2 consecutive rounds"):

- Round 3: ✅ satisfied (0 novel BLOCKER/MAJOR after truth-audit; 1 polish-tier MAJOR closed; rest STALE/FALSIFIED)
- Round 4: ✅ satisfied (0 novel BLOCKER/MAJOR after truth-audit; 0 closures needed; all 16 findings STALE/FALSIFIED/OPINION)

**Clean-count on v1A.0.39: 1 / 3.**

(Round 4 is the first clean round *on v1A.0.39 itself*; rounds 1–3 were on prior versions. Need 2 more clean rounds on v1A.0.39 — or any post-v1A.0.39 version with no new substantive edits — to satisfy the convergence exit criterion at the v1A.0.39 anchor.)

P1A external-review readiness remains capped at **95%** per `feedback_readiness_oscillation` until Houston sign-off + clean-count of 3.

---

## No recompile, no Convex bump

Per round-4 triage protocol: 0 VERIFIED → no .tex edit → no `\paperVersion` bump → no `pdflatex` 4-pass → no `papers.ts` mirror → no `paperVersions:bump` mutation → no commit.

The v1A.0.39 PDF (`arxiv/paper1a_ech_nogo.pdf`, 21 pages, md5 `4b290d111f03275c88bf5d147f8ad964`) and its site mirror (`site/public/papers/paper1a_ech_nogo.pdf` + `paper1a_ech_nogo_v1A.0.39.pdf`) remain canonical.

---

*Generated by R-multi-round4 truth-audit pipeline. No commit produced this round (per round-4 instruction "DO NOT git commit").*
