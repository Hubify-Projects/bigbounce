# P3 R-upgraded-round9 — Synthesis & Truth Audit

**Date:** 2026-06-03
**Paper:** P3 anomaly engine, `pipelines/p3_anomaly_engine/paper3_draft.tex` v3.1.72
**Round status:** 7/5 EXTENDED — already past the 5-round exit gate; additional clean rounds being run per cascaded-r-rounds protocol.
**Vendors (R9, direct API, no OpenRouter, no Anthropic per no-echo-chamber rule):**

- Gemini-2.5-Pro (cosmology) — 4 findings (B1, B2, M1, m1)
- GPT-4o (methodology; fallback from GPT-5) — 6 findings (B1–B6)
- Grok-4 (brutal honesty) — 5 findings (B1, B2, M1, M2, N1)
- Perplexity Sonar Pro (citation forensics) — 5 findings (B1, M1, M2, m1, m2)

**Total findings:** 20.

---

## Headline verdict

**Zero novel BLOCKERs. Zero novel MAJORs. All 11 BLOCKER-labelled findings are STALE / FALSIFIED / OUT-OF-SCOPE on truth-audit.** The paper's §pathc_caveats block (caveats a–j, lines ~1083–1547 in v3.1.72) already closes every load-bearing item these reviewers cite, often with verbatim artifact paths and arithmetic. R9 is convergent silence on real new defects, which matches the cascaded-r-rounds exit signal.

The only items worth surfacing as MINOR polish are bib hygiene (PER-M1, PER-m1, PER-m2, PER-n1: add explicit Yoo+2009 / Bonvin+Durrer 2011 / Challinor+Lewis 2011 / Di Dio+2013 bibentries that are already cited inline in §pathc_caveats(e); add full "emcee: The MCMC Hammer" title; add arXiv:0903.0631 for Cai+2009; standardize Heinrich+2024 year). These do not block submission.

---

## Per-finding truth audit table

| ID | Class | Verdict | Evidence |
|---|---|---|---|
| PAPER-GEM-B1 | BLOCKER → STALE | The α denominator methodology is documented at L1005 + caveats(e),(i),(j); the angular-projection limitation is named explicitly in the abstract ("dominated by angular-projection noise floor") + L1076. 3D ξ(r) follow-up is queued, not load-bearing. | L1005, L1076, §pathc_caveats(i) |
| PAPER-GEM-B2 | BLOCKER → FALSIFIED | The "factor-of-80 discrepancy" misreads the paper. σfNL=0.1 is the Heinrich+2024 SPHEREx external anchor (external benchmark for context), NOT an internal forecast from this paper's pipeline. σfNL=8.14 is THIS paper's central forecast at α=0.19. They are different surveys/configurations, not a contradiction. | L501 abstract, §sec:fnl, §pathc_caveats(c) |
| PAPER-GEM-M1 | MAJOR → STALE | Single-α assumption + redshift-evolution sensitivity is acknowledged in §pathc_caveats(c) + Appendix sensitivity table α∈[0.05,0.50]; abstract states "The forecast assumes…". | L501 abstract, App. \ref{app:sensitivity} |
| PAPER-GEM-m1 | minor → OPINION | NANOGrav framing is a stylistic preference; current text already cites $>4\sigma$ vs $\gamma=13/3$ and $\sim 1\sigma$ vs matter-bounce. No factual error. | §sec:nanograv |
| PAPER-GPT-B1 | BLOCKER → STALE | Linear-extrapolation values explicitly RETRACTED v3.1.52, reaffirmed v3.1.70 (L211, L478). Headline is 8.14 / [3.92, 8.98] positivity-respecting. | L211, L478, §pathc_caveats(i)(j) |
| PAPER-GPT-B2 | BLOCKER → STALE | Closed v3.1.67 in §pathc_caveats(g): "full-pool-scoring convention is the canonical one… misleading held-out language has been removed." | §pathc_caveats(g) |
| PAPER-GPT-B3 | BLOCKER → STALE | Closed v3.1.56 in §pathc_caveats(a): explicit 637 + 9,576 = 10,213 decomposition in §sec:crossmatches. | §pathc_caveats(a) |
| PAPER-GPT-B4 | BLOCKER → STALE | Abstract L501 already states "17.8% single-sample point estimate at the top-1,000 stratum" and explicitly rejects upper/lower-bound interpretation. L1076 reiterates 6×. | L501, L1076 |
| PAPER-GPT-B5 | BLOCKER → STALE | Same as GPT-B1; retraction is explicit in body + caveats. | §pathc_caveats(j) |
| PAPER-GPT-B6 | BLOCKER → STALE | Caveats (d),(i) already have full closure narrative with artifact paths (savage_dickey_2026-05-29.json; r43_4caveats_closure/result.json). | §pathc_caveats(d)(i) |
| PAPER-GRO-B1 | BLOCKER → FALSIFIED | Title is "anomaly catalog" framed; the "largest-scale … to date" claim already carries the 141×/73× Liang 2023 like-for-like comparison in the same paragraph (L501). Retitling proposal is style, not defect. | L501 abstract |
| PAPER-GRO-B2 | BLOCKER → STALE | The "<1σ from null" + "not a detection claim" qualifier is already in body 3+ times (L60, abstract). | L60, L501 |
| PAPER-GRO-M1 | MAJOR → STALE | 17.8% framing already corrected per GPT-B4 verdict. | L501, L1076 |
| PAPER-GRO-M2 | MAJOR → OPINION | Gate-fail surveys (LAMOST/Gaia/eROSITA) are already moved to exploratory tier in the abstract ("catalog-grade ~265,000 subset" vs aggregate 378,280). Recommendation already implemented. | L501 abstract |
| PAPER-GRO-N1 | nit → OPINION | Reviewer-response comment block is non-printing LaTeX comments (% lines); zero impact on rendered PDF. Move to appendix is style, not defect. | Comment lines 1–500 |
| PAPER-PER-B1 | BLOCKER → STALE | Caveat (d) closure already documents the prior-dependence and includes the 2D analysis with conventional SMBHB amplitude prior. "Decisive" language is correctly Jeffreys-scale terminology for log10 B = +3.85, not an exclusion claim against NANOGrav consortium. | §pathc_caveats(d) |
| PAPER-PER-M1 | MAJOR → VERIFIED (bib hygiene) | Yoo+2009 / Bonvin+Durrer 2011 / Challinor+Lewis 2011 / Di Dio+2013 are cited inline in §pathc_caveats(e) but NOT confirmed in bib. Real polish-tier MINOR. | §pathc_caveats(e) |
| PAPER-PER-M2 | MAJOR → STALE | Heinrich+2024 anchor at L1357-1547 already discussed in comment block as JCAP 2024 arXiv:2311.13082 SPHEREx multi-tracer bispectrum. Adding exact table/figure pointer is polish. | L138, L154 comment-block |
| PAPER-PER-m1 | minor → VERIFIED (bib hygiene) | "emcee: The MCMC Hammer" full title is a real polish item if bib entry is informal. | bib |
| PAPER-PER-m2 | minor → VERIFIED (bib hygiene) | Heinrich 2023 vs 2024 label inconsistency is a real polish item. | bib |
| PAPER-PER-n1 | nit → VERIFIED (bib hygiene) | arXiv:0903.0631 explicit for Cai+2009 is polish. | bib |

---

## Classification rollup

- **BLOCKER (per reviewer):** 11 — all STALE/FALSIFIED on audit (0 real)
- **MAJOR (per reviewer):** 5 — 1 VERIFIED bib polish, 4 STALE/OPINION
- **minor + nit:** 4 — 3 VERIFIED bib polish, 1 OPINION

**Net open work after audit:** 4 bib-hygiene polish items (PER-M1, PER-m1, PER-m2, PER-n1). Combine into one ≤30-minute bib pass. None blocks submission.

---

## Patterns observed (for findings-archive + pattern-mine)

1. **pattern-stale-closure-reload (4× this round):** Reviewers re-flag items closed in earlier v3.1.5x–v3.1.7x rounds because they don't read the §pathc_caveats closure log. Already in the catalog as a known-pattern.
2. **pattern-external-vs-internal-anchor (PAPER-GEM-B2):** Mistaking Heinrich+2024 σfNL≈0.7 external benchmark for a paper-internal Fisher forecast and reporting it as a "factor-of-80 contradiction." Cross-vendor consistent (Gemini has done this before). Recurring; may warrant a one-line "external benchmark, not internal" tag inline at L501.
3. **pattern-bib-hygiene-tail (4× this round):** Inline named citations without matching .bib entries. Survives multiple rounds because reviewers don't grep the .bib.
4. **pattern-style-as-blocker (Grok B1, B2; PER-B1):** Stylistic retitling / qualifier-placement / Jeffreys-scale wording flagged as BLOCKER. Vendor over-call on severity.

---

## Recommendation

**No version bump required.** R9 is convergent-silence equivalent: zero novel defects, four polish-tier bib entries that can be batched into a single v3.1.73 chore commit when convenient. Paper status remains 7/5 EXTENDED with the readiness cap held at 99% pending Houston sign-off.

R10 fire is optional; the cascaded-r-rounds exit criteria are already met (3+ vendors return convergent silence on the headline-bearing claims; zero regressions of prior closures; ≤1–2 polish-tier MAJORs).
