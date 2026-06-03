# P1A R-upgraded-round6 — Truth-Audit Synthesis

**Reviewed:** v1A.0.42
**Closure:** v1A.0.43 (bumped)
**Reviewers:** Grok-4 brutal, GPT-5 methodology (GPT-4o fallback), Perplexity Sonar Pro citations, Gemini-2.5-Pro cosmology
**Total findings:** 18 (1 VERIFIED, 14 STALE, 2 FALSIFIED, 1 OPINION)
**Counter:** RESET — prior 4-clean streak broken by GEM-M1; new counter 0/3 at v1A.0.43

---

## Verified closure

### GEM-M1 (MAJOR) — Bianchi vs Pontryagin justification bug — **VERIFIED**

Gemini correctly flagged that the perturbation-transparency section (Sec X) justified the vanishing of the Holst contribution to EOMs by claiming the dual $\tfrac12 \epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\mathring\Gamma)$ vanishes identically via the first Bianchi identity. This is mathematically false: that combination is the **Pontryagin density** ($\propto {}^*\!R\,R$), which is generically nonzero pointwise but is a **total derivative**, so it integrates to a boundary term and contributes nothing to the variational EOMs.

The headline conclusion (Holst sector decouples from perturbation observables; no GW birefringence; no $TB/EB$ parity from the ECH mechanism) **survives unchanged** — it now rests on the correct mathematical reason.

**Fix applied:** `arxiv/paper1a_ech_nogo.tex` L1460–1464 and L1488–1497 rewritten in v1A.0.43.

---

## Counter-evidence findings (17)

| ID | Class | Verdict | Reason |
|---|---|---|---|
| GRO-B1 | BLOCKER | STALE_OPINION | Channel-level framing already disclosed phenomenological + omitted operators |
| GRO-B2 | BLOCKER | STALE | N_tot=92 already labeled phenomenological-ansatz fit (Appendix B) |
| GRO-M1 | MAJOR | STALE_OPINION | "theorem" already scoped to canonical scalars; standard usage |
| GRO-M2 | MAJOR | STALE | Birefringence already class-scoped, not ECH-distinctive |
| GRO-n1 | nit | **FALSIFIED** | Review-log "in submission" claim — those lines are %-comments invisible in PDF |
| GRO-n2 | nit | STALE_OPINION | Novelty framing already explicit in intro |
| GPT-B1 | BLOCKER | STALE | +1 vs +4 dim ansatz already labeled phenomenological |
| GPT-B2 | MAJOR | STALE | Sensitivity table in Appendix B; full MCMC = P1B scope |
| GPT-B3 | MAJOR | STALE_OPINION | Reviewer misread — null result framed as class-scoped, not predictive |
| GPT-M1 | minor | STALE | P1A is no-go theorem, no Bayesian analysis (P1B) |
| GPT-M2 | minor | STALE | Systematic budget = P1B/P3 scope |
| GPT-n1 | nit | OPINION | Reviewer-taste, no specific citations |
| PER-B1 | BLOCKER | STALE | Attribution already "motivated by", not "derived in" |
| PER-M1 | MAJOR | STALE | Mercuri attribution already disambiguated in L1066+ |
| PER-M2 | MAJOR | STALE | LWK normalization already explicit own-mapping |
| PER-m1 | minor | STALE | Ashtekar-Singh window already disambiguated |
| PER-m2 | minor | STALE | f_NL=-35/8 already qualified to scalar w=0 sub-class |
| PER-n1 | nit | OPINION | "in prep" is standard companion-bundle practice |
| GEM-N1 | nit | OPINION | Phrasing tweak, not load-bearing |

---

## Decision

- **Bumped** v1A.0.42 → **v1A.0.43**
- **Recompiled** 4-pass pdflatex, 0 undef refs, 21 pages, page-1 stamp verified `v1A.0.43 / June 2, 2026 PDT`
- **Mirrored** PDF to `arxiv/`, `public/papers/`, `site/public/papers/`, `site/out/papers/`
- **Counter reset:** 0/3 clean rounds at v1A.0.43 (prior 4-of-3 EXIT_EXTENDED at v1A.0.42 broken by genuine novel VERIFIED catch)
- **Convex sync:** pending (no MCP closure mutation issued in this triage; will be issued in next fire)
- **No commit issued** per protocol scope

---

## New-pattern candidate

**pattern-035-math-justification-survives-conclusion** — class of findings where the stated mathematical reason for a result is wrong but the conclusion is correct via a different correct reason. Watch for 1–2 more occurrences across P1B/P3/P4 before promotion to formal catalog.

---

## Next gate

R-upgraded-round7 on v1A.0.43, targeting 1-of-3 clean rebuild toward fresh exit at 3-clean.
