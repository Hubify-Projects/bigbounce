# Claude "AI for Science" — BigBounce Application (DRAFT)

**Program:** Anthropic AI for Science — up to 50 projects, **up to $30,000 in Claude/compute credits each**.
**Deadline:** applications close **2026-07-15**; award notifications by **2026-07-31**.
**Eligibility (VERIFY before submitting):** the program targets scientific research; the *discounted Claude Team seats* are gated to academic institutions / nonprofit research orgs (hard sciences incl. physics explicitly listed). BigBounce is an **independent research program** — confirm whether the compute-credits track accepts independent/unaffiliated researchers, or apply via an affiliated institution/nonprofit. Do not overstate affiliation on the form.

> This is a DRAFT for Houston to review, tighten, and submit through the official form. Numbers below are drawn from real project artifacts (`SSOT/index.md`, `compute-queue.md`, `drive-to-100.md`) — keep them truthful; update any that have moved.

---

## 1. One-paragraph summary

BigBounce is a six-paper observational-cosmology program testing whether **bounce cosmology outperforms ΛCDM + inflation** across independent data channels — primordial non-Gaussianity (f_NL) forecasts, dark-energy evolution (DES-Y5 w0waCDM), galaxy-chirality/parity catalogs (SDSS/LAMOST/DESI, ≥268,519 validated galaxies), and a multi-survey cosmic-anomaly engine. The program is **model-agnostic** (goal: beat the standard model, not defend one bounce model) and runs an unusually rigorous **multi-vendor adversarial peer-review + provenance pipeline**. We are applying to move the compute-bound stages (MASTER/NaMaster Monte Carlo, native survey retrains, Cobaya MCMC, Fisher forecasts) onto Claude Science's HPC/Modal substrate and to author reusable astro-domain specialist agents.

## 2. Principal researcher

- **Houston Golden** — houston@hubify.com — independent researcher; site https://bigbounce.hubify.app; code https://github.com/Hubify-Projects/bigbounce.
- [VERIFY: institutional/nonprofit affiliation if applying under the academic track.]

## 3. Scientific goals (the six papers)

| Paper | Topic | Compute-bound stage |
|-------|-------|---------------------|
| P1A/P1B | Spin–torsion / bounce signatures; DES-Y5 w0wa dark-energy channel | NaMaster β-injection recovery, fsky sweeps |
| P2 | f_NL + n_fNL joint forecast (SDB Fisher) | Fisher forecasts, joint-constraint runs |
| P3 | Multi-survey anomaly catalog (Path C native retrains SDSS/LAMOST/CMB) | **GPU** survey retrains (highest credit need) |
| P4 | Galaxy chirality catalog (≥268,519 galaxies) | MASTER MC nulls, Wp invariance, fsky_eff |
| P5 | DESI chirality; L-parity EFT | MC + EFT operator validation |

## 4. Why AI / multi-agent is essential here (not incidental)

BigBounce's core method is a **model-, harness-, and vendor-agnostic adversarial review loop**: independent frontier models (Claude + cross-vendor) and an independent external browser-review leg *refute* each claim, verdict-first, with a separate skeptical integrity audit guarding against self-favoring bias. This has already **caught real errors** peers would have missed — e.g. de-biasing the referee prompt surfaced an overlap-inflated w0wa σ-distance (shared-SNe double-counting) and a mislabeled P3 "catalog-grade" tier that failed injection-recovery. In science the catastrophic failure is the *false positive* (a hallucinated derivation, a fabricated result), and cross-vendor adversarial verification is the only method that reliably decorrelates the shared-training-prior errors a single model repeats. Claude Science supplies the coordinating agent + reproducible-provenance substrate; our adversarial layer runs on top.

## 5. What the credits unlock

Current compute is self-funded and throttled — the account has run at/near $0 balance, forcing cheap CPU pods (RTX A4000 @ $0.17/hr) while the H200 pods ($4.39/hr) sit EXITED with `INSUFFICIENT_BALANCE`. Path C native retrains alone are budgeted at ~$300–500. **$30k credits would:**

1. Run the P3 Path-C **native GPU retrains** (SDSS/LAMOST/CMB) instead of the lower-quality cross-transfer stopgap.
2. Complete full-resolution NaMaster MC (NSIDE=512) and Cobaya MCMC chains without CPU-fallback compromises.
3. Fund the P2 f_NL joint Fisher forecasts and P3 PTA (NANOGrav/EPTA/SKA) σ(γ) forecasts.
4. Author + open-source reusable **astro-survey specialist agents** for Claude Science (the domain layer Anthropic's life-sciences connectors omit).

## 6. Open-science / reproducibility posture (differentiator)

- Every artifact is provenance-linked (`canonical_provenance/*.json`, `reviewTimeline.ts`); every review round is publicly timelined on https://bigbounce.hubify.app/reviews.
- Triple-redundant backups (local + HuggingFace + Backblaze B2) on every compute milestone.
- Papers are RevTeX, arXiv-ready, with a documented multi-vendor review trail — a natural, high-visibility showcase of Claude Science's auditable-provenance value.

## 7. Deliverables & timeline (if awarded)

- **Weeks 1–2:** port MASTER/NaMaster + anomaly-engine jobs to Claude Science HPC/Modal; provenance-parity check.
- **Weeks 3–6:** P3 native retrains + P2/P5 forecasts; drive papers past the 96→99 readiness ladder under the standing adversarial-review gates.
- **Ongoing:** publish astro specialist agents; public review timeline entries per round.

## 8. Pre-submission checklist

- [ ] Confirm eligibility track (independent vs academic/nonprofit affiliation).
- [ ] Refresh every quantitative figure against current `SSOT/index.md`.
- [ ] Attach links: site, GitHub, a representative arXiv-ready PDF, the /reviews timeline.
- [ ] Tighten to the form's word limits; lead with §4 (why multi-agent is essential).
- [ ] Submit before 2026-07-15.

## Sources

- Anthropic — Claude Science / AI for Science (2026-06-30): https://www.anthropic.com/news/claude-science-ai-workbench
- Product page: https://claude.com/product/claude-science
