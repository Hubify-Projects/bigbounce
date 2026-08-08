# Claude "AI for Science" — BigBounce Application (DRAFT)

**Program:** Anthropic AI for Science — up to 50 projects, **up to $30,000 in Claude/compute credits each**.
**Deadline:** applications close **2026-07-15**; award notifications by **2026-07-31**.

**Eligibility (researched 2026-07-01 — official rules at anthropic.com/ai-for-science-program-rules):**
- The rules **contemplate individual applicants**: "If you are an individual, you must be at least 18…; if you are employed by a legal entity or affiliated with a university or other research institution, then you must have obtained all consents." Independent application is not explicitly barred.
- However the program is **"designed for researchers attached to research institutions"** (academia/nonprofit), with a stated **biology/life-sciences focus** — though the Claude Science launch round explicitly extended hard sciences (physics, math, CS, chemistry). Expect the affiliation question; answer honestly (independent researcher, Hubify Labs as the operating platform, not a nonprofit). A collaborating academic co-applicant would materially strengthen the application if available.
- Evaluation criteria (stated): scientific merit, potential impact, technical feasibility, and **team credentials in both the subject area and AI** — lead with §4; the adversarial-review pipeline is itself a demonstrable AI-methods credential.
- ⚠️ **Data-use term Houston must accept before submitting:** Selected Researchers grant Anthropic a **perpetual, irrevocable license** to collect, analyze, and **train models on all data generated from use of the credits**. For BigBounce this covers credit-funded chains/retrains/forecasts (all destined for public release anyway, but confirm comfort).
- Applications undergo a biosecurity assessment (non-issue for cosmology).

> This is a DRAFT for Houston to review, tighten, and submit through the official form. Numbers below are drawn from real project artifacts (`SSOT/index.md`, `compute-queue.md`, `drive-to-100.md`) — keep them truthful; update any that have moved.

---

## 1. One-paragraph summary

BigBounce is a six-paper observational-cosmology program testing whether **bounce cosmology outperforms ΛCDM + inflation** across independent data channels — primordial non-Gaussianity (f_NL) forecasts, dark-energy evolution (DES-Y5 w0waCDM quintom-B), an **8.47M-galaxy chirality/parity catalog** (SDSS/LAMOST/DESI), and a **multi-survey anomaly engine (≥268,519 validated catalog-grade anomalies)**. All six papers currently sit at **96–98% readiness** after 50+ internal/external adversarial review rounds — every genuine scientific and reproducibility defect closed; the residual gate is structural (DOI/arXiv IDs mint at submission). The program is **model-agnostic** (goal: beat the standard model, not defend one bounce model) and runs an unusually rigorous **multi-vendor adversarial peer-review + provenance pipeline**. We are applying to move the compute-bound stages (MASTER/NaMaster Monte Carlo, referee-driven control chains and retrains, Cobaya MCMC, Fisher forecasts) onto Claude Science's HPC/Modal substrate and to author reusable astro-domain specialist agents.

## 2. Principal researcher

- **Houston Golden** — houston@hubify.com — independent researcher; site https://bigbounce.hubify.app; code https://github.com/Hubify-Projects/bigbounce.
- [VERIFY: institutional/nonprofit affiliation if applying under the academic track.]

## 3. Scientific goals (the six papers)

All six at **96–98% readiness** (50+ adversarial rounds; residual gate is the structural DOI/arXiv mint at submission, not quality):

| Paper | Topic | Open compute-bound stage |
|-------|-------|--------------------------|
| P1A/P1B | Spin–torsion bounce signatures; DES-Y5 w0waCDM quintom-B channel (direction confirmed robust in both independent SN samples) | ALP prior-predictive fraction; NaMaster β-injection/fsky sweeps |
| P2 | f_NL + n_fNL sensitivity recast (joint SDB Fisher computed: σ 1.53→3.08→7.06 with running) | deeper joint-constraint extensions (non-gating) |
| P3 | Multi-survey anomaly engine — **≥268,519 validated catalog-grade anomalies** (4 injection-recovery-PASS surveys) | held-out re-scores (Planck), multi-null 10⁴ reruns |
| P4 | **8.47M-galaxy chirality catalog**; dipole null confirmed pseudo-label-independent (GZ1-only retrain) | full-catalog GZ1-only re-inference; b/a cross-match; ≥200-axis injection battery |
| P5 | DESI void-parity; L-parity EFT (SO(3)-consistent reformulation) | LSS randoms acquisition + mask/randoms rebuilds |

## 4. Why AI / multi-agent is essential here (not incidental)

BigBounce's core method is a **model-, harness-, and vendor-agnostic adversarial review loop**: independent frontier models (Claude + cross-vendor) and an independent external browser-review leg *refute* each claim, verdict-first, with a separate skeptical integrity audit guarding against self-favoring bias. This has already **caught real errors** peers would have missed — e.g. de-biasing the referee prompt surfaced an overlap-inflated w0wa σ-distance (shared-SNe double-counting) and a mislabeled P3 "catalog-grade" tier that failed injection-recovery. In science the catastrophic failure is the *false positive* (a hallucinated derivation, a fabricated result), and cross-vendor adversarial verification is the only method that reliably decorrelates the shared-training-prior errors a single model repeats. Claude Science supplies the coordinating agent + reproducible-provenance substrate; our adversarial layer runs on top.

## 5. What the credits unlock

Current compute is self-funded and severely throttled — recent referee-driven runs launched with **~$7.86 of RunPod balance** on a $0.17/hr RTX A4000 while H200 pods sit EXITED with `INSUFFICIENT_BALANCE`. Even so, the pipeline converts compute directly into closed referee findings: the SN-overlap control chains (Pantheon+-only and DES-SN5YR-only Cobaya MCMC) **closed a reviewer MAJOR by showing the quintom-B direction survives in both independent SN samples**, and a GZ1-only classifier retrain **closed another MAJOR by proving the chirality dipole null is not inherited from pseudo-labels**. The open, referee-blocking compute queue (`SSOT/compute-to-accept-queue.md`) that **$30k in credits directly clears**:

1. **P4 chirality robustness battery**: full-catalog GZ1-only re-inference (the completed run was reduced-N) and the joint real-space×harmonic covariance likelihood / spatially-resolved confusion matrix (image-level compute, DP4-15/-17). The empirical b/a axis-ratio cross-match (a Gemini MAJOR) is **already closed** — real DR8 morphology pulled for all 3.2M spirals gave f_edge=15.8% and an edge-on-isolated dipole slice with per-leg |z|<1.4 (folded v1.0.218); the harmonic-injection amplitude sweep is likewise done to A=2%.
2. **P1B dark-energy accommodation test**: ALP prior-predictive fraction — quantify the prior-volume cost of the fit (the "tautological fit" referee concern).
3. **P3 anomaly-catalog reproducibility**: complete the held-out re-scores (Planck pending) and the remaining multi-null 10⁴ reruns.
4. **P5 DESI void-parity rebuilds**: LSS randoms acquisition + mask-dilation/randoms rebuilds.
5. Author + open-source reusable **astro-survey specialist agents** for Claude Science (DESI/SDSS/LAMOST/Gaia/CMB — the domain layer Anthropic's life-sciences connectors omit).

Every item above is a named referee finding with a machine-checkable closure criterion — the credits convert directly into review-verified science, not exploratory burn.

## 6. Open-science / reproducibility posture (differentiator)

- Every artifact is provenance-linked (`canonical_provenance/*.json`, `reviewTimeline.ts`); every review round is publicly timelined on https://bigbounce.hubify.app/reviews.
- Triple-redundant backups (local + HuggingFace + Backblaze B2) on every compute milestone.
- Papers are RevTeX, arXiv-ready, with a documented multi-vendor review trail — a natural, high-visibility showcase of Claude Science's auditable-provenance value.

## 7. Deliverables & timeline (if awarded)

- **Weeks 1–2:** port MASTER/NaMaster + anomaly-engine jobs to Claude Science HPC/Modal; provenance-parity check.
- **Weeks 3–6:** P3 native retrains + P2/P5 forecasts; drive papers past the 96→99 readiness ladder under the standing adversarial-review gates.
- **Ongoing:** publish astro specialist agents; public review timeline entries per round.

## 8. Pre-submission checklist

- [x] Eligibility researched (2026-07-01): individuals contemplated by the rules; program "designed for" institution-attached researchers — apply honestly as independent; academic co-applicant strengthens if available.
- [ ] **Houston decision:** accept the data-use term (perpetual, irrevocable Anthropic license to train on credit-generated data).
- [x] Quantitative figures refreshed against SSOT as of 2026-07-01 (readiness 96–98, ≥268,519 anomalies, 8.47M chirality catalog, SN-control-chain + GZ1-only closures, open queue items).
- [ ] Attach links: site, GitHub, a representative arXiv-ready PDF, the /reviews timeline.
- [ ] Tighten to the form's word limits; lead with §4 (why multi-agent is essential).
- [ ] Submit before 2026-07-15.

## Sources

- Anthropic — Claude Science / AI for Science (2026-06-30): https://www.anthropic.com/news/claude-science-ai-workbench
- Product page: https://claude.com/product/claude-science
