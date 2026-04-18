# Paper 4 — What's Actually Scientifically Interesting

**Purpose:** Distill the genuine scientific contributions of the Galaxy Chirality Catalog (8.47M galaxies) beyond "we built a big classifier" and "we measured a dipole."

**Canonical paper:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0, 1,099 lines, 19 MB PDF with 11 figures).
**SSOT:** [`project-context/SSOT/paper-4/status.md`](SSOT/paper-4/status.md).
**Last updated:** 2026-04-17.

---

## Novelty scale (used below)

- **N0 — Replication:** Standard reproduction of prior work with our pipeline.
- **N1 — Refinement:** Tightens or extends prior work — higher precision, bigger sample, systematic audit.
- **N2 — Substantive:** New application of known methods → actionable new result (catalog, diagnostic).
- **N3 — First-of-kind:** Novel methodology or first-of-kind observation, no prior analog in the literature.
- **N4 — Paradigm-shifting:** New physics claim or falsification that changes the consensus.

---

## The 7 Genuinely Novel Scientific Contributions

### 1. The largest bias-audited galaxy chirality catalog ever published — **N3**

**What:** 8,474,531 galaxies classified into CW / CCW / NOT_SPIRAL using a ViT-Small + 3-class head trained on 26,626 labels (6,637 Galaxy Zoo 1 + 17,153 CE-ResNet + 2,000 synthetic). Released publicly on HuggingFace (CC-BY-4.0) with three catalog tiers: raw (A), calibrated (B), equivariant (C).

**Why it matters:** Prior chirality catalogs topped out at ~1.6M galaxies (Shamir 2020). This is the first sample where the classifier survives a full 8-test bias hardening audit — flip-swap correlation 0.833, rotation stability 89.8 %, blank-sky control sane (v1 gave 100 % CW on blanks; v2 is calibrated). The explicit bias audit as a first-class gating step is what makes this catalog *usable* for cosmology.

**Scientific significance:** Every prior claim of large-scale parity violation in galaxy spins (notably Shamir's recurring 2–3 % asymmetry findings) has been plagued by uncalibrated classifier bias. A catalog that *can* be wrong but has been *shown not to be* unlocks the measurement, not just the data.

**Paper claim:** "We present the largest bias-audited galaxy chirality catalog to date: 8,474,531 galaxies, 8/8 bias tests passed, released under CC-BY-4.0 for community use."

---

### 2. Shamir 2020's 3 % asymmetry claim refuted 7× — **N3**

**What:** The raw (Catalog A) probability map shows a 94.6σ dipole signal. The equivariant (Catalog C) probability map, after test-time augmentation that averages each galaxy's prediction with its mirror image, collapses that same signal to **0.43σ (p = 0.33)**. The TTA operation is provably unbiased with respect to true parity — it zeros out any classifier-induced chirality preference. The 94.6σ → 0.43σ collapse proves the prior signal was classifier artifact, not sky.

**Why it matters:** Shamir (2020, 2022) claimed a ~3 % chirality asymmetry at > 2σ that has been cited as evidence for a preferred cosmic axis / large-scale parity violation. Our equivariant pipeline recovers an asymmetry *upper limit* of 0.47 % (max regional) — roughly 7× smaller than the Shamir claim — and rules out the claimed signal at high confidence.

**Scientific significance:** A cornerstone observational claim for anisotropic cosmology is retracted to null. The cosmological principle survives this stress test.

**Paper claim:** "The raw-catalog 94.6σ dipole is a classifier-systematic artifact; after equivariant test-time augmentation the signal collapses to 0.43σ (p = 0.33), ruling out Shamir (2020)'s ~3 % asymmetry claim at 7× below the detection threshold."

---

### 3. Equivariant test-time augmentation as a bias-removal primitive — **N3**

**What:** The explicit TTA operation p_eq(x) = ½ [p_CW(x) + (1 − p_CW(mirror(x)))] is applied per-galaxy. Because CW-in-original = CCW-in-mirror is a mathematical identity (parity flips handedness), any classifier bias toward either class cancels exactly. The per-galaxy cost is one extra forward pass.

**Why it matters:** CE-ResNet (Jia 2023) added per-model equivariance training; GZ1 (Lintott 2008) used human voting; SpArcFiRe (Hayes 2017) used symbolic fit. None of these impose exact per-galaxy parity symmetry as a post-processing step. Our equivariant post-processing is model-agnostic — it drops on top of any CW/CCW classifier and turns a biased estimator into an unbiased one at inference time.

**Scientific significance:** Any future chirality study can adopt this as a one-line wrapper, removing a class of systematic that has dogged the field for 15 years.

**Paper claim:** "We introduce equivariant post-processing as a model-agnostic TTA operation that provably cancels classifier chirality bias, converting any CW/CCW model into an unbiased chirality estimator."

---

### 4. Cross-classifier agreement at 91.5 % validates both pipelines — **N1**

**What:** On the 23 k DESI Legacy galaxy sample where both our ViT-Small v2 and the CE-ResNet (Jia 2023) report labels, the two independent classifiers agree on 91.5 % of calls. Probability correlation r = 0.753. Equivariant CW-fractions match to four decimals: 0.5012 (ours) vs 0.5013 (CE-ResNet).

**Why it matters:** Two architectures, two training labels, two preprocessing pipelines — both arriving at the *same* chirality fractions to part-in-10 ⁴ accuracy. This is the strongest external validation of the 0.43σ null: CE-ResNet, an independent group's work, recovers the same answer.

**Scientific significance:** Rules out "our specific architecture chose a specific wrong answer" — the null is robust across ML paradigms.

**Paper claim:** "Cross-classifier agreement with Jia et al. (2023) CE-ResNet reaches 91.5 % on 23 k common galaxies, with equivariant CW-fractions matching to four decimals (0.5012 vs 0.5013), providing independent validation of the null dipole result."

---

### 5. Catastrophic v1 bias is a cautionary tale in active learning — **N2**

**What:** The v1 baseline classifier (trained on only GZ1 + CE-ResNet without bias hardening) fell into a pathological local minimum: 92.8 % CW on real galaxies, 100 % CW on synthetic blank-sky images. Five of the six bias tests failed. v2 added: (i) 2,000 synthetic controls (blanks, obvious ellipticals), (ii) flip-augmented training, (iii) explicit non-spiral class, (iv) Platt calibration. v2 passes 8/8.

**Why it matters:** This is a recipe. The exact failure mode (classifier collapses to "everything is CW") has been implicit in older chirality work but never documented as a gating-level audit result. The step-by-step rescue (blanks as hard negatives, flip augmentation as the key single change, TTA as the safety net) is reproducible.

**Scientific significance:** Saves the next researcher the 3-month cycle we spent diagnosing v1. The bias-hardening suite is released with the catalog.

**Paper claim:** "An initial baseline classifier trained without bias hardening produced 92.8 % CW predictions on real data and 100 % CW on blank-sky controls — a pathological asymmetry driven by label-class priors in the training set. We document the exact pipeline that converts this pathology into an 8/8-passing classifier."

---

### 6. Minimum detectable dipole of 0.2 % at 3σ — **N2**

**What:** Given 3.3 M spiral galaxies, the equivariant pipeline's 3σ dipole floor is 0.2 % fractional asymmetry. Any genuine chirality signal larger than this would be detected.

**Why it matters:** This is the quantitative boundary for future bounce / anisotropic-cosmology claims — the threshold below which a claim cannot be made from this catalog. The number is derived from Poisson noise plus the dipole power-spectrum geometry (Landy–Szalay), not assumed.

**Scientific significance:** Any future cosmology scenario that predicts |f_CW − f_CCW| > 0.2 % is falsifiable today. Scenarios below this require a larger catalog (LSST Y1 should take it to ~20 M spirals → 0.08 % floor).

**Paper claim:** "The equivariant pipeline's 3σ detection floor for fractional chirality asymmetry is 0.2 % on 3.3 M spiral galaxies, setting a falsifiability threshold for future anisotropic-cosmology predictions."

---

### 7. Reusable equivariant dipole infrastructure — **N2**

**What:** The full pipeline (bias-hardening suite, equivariant TTA, Landy–Szalay dipole, spherical-harmonic multipoles, MC null test) is released as `pipelines/p2_chirality/*.py` with all 20+ scripts. The same code is being re-used for Paper 3 limitation G (empirical Landy-Szalay w(θ) bias calibration for anomaly subsamples).

**Why it matters:** Paper 4 produced a null; its lasting contribution is the framework. The ability to ask "is there a dipole in this sky-distributed sample?" at > 5 M source scale, with a *clean* answer that passes sanity checks, is itself an asset.

**Scientific significance:** One framework, two papers (Paper 3 anomaly bias calibration + Paper 4 chirality). Cross-paper synergy is how scientific infrastructure pays off.

**Paper claim:** "The equivariant chirality pipeline is released as community software; the same dipole infrastructure is adopted by Paper 3's anomaly bias calibration."

---

## Summary table: novelty classification

| # | Finding | N-tier | Why |
|---|---|:---:|---|
| 1 | 8.47 M bias-audited catalog | **N3** | Largest ever + first-of-kind 8-test bias audit gate |
| 2 | Shamir 2020 3 % claim refuted 7× | **N3** | Retraction of a cornerstone anisotropic-cosmology claim |
| 3 | Equivariant TTA as bias-removal primitive | **N3** | No prior per-galaxy parity-symmetric post-processing in the literature |
| 4 | 91.5 % cross-classifier agreement | **N1** | Refines earlier CE-ResNet validation with a ViT-based independent check |
| 5 | v1 pathology → v2 rescue recipe | **N2** | First documented recipe; bias-hardening suite released |
| 6 | 0.2 % 3σ asymmetry floor | **N2** | Quantitative falsifiability threshold for future claims |
| 7 | Reusable equivariant-dipole framework | **N2** | Cross-paper infrastructure (feeds Paper 3 limitation G) |

Count by tier: **N3 × 3, N2 × 3, N1 × 1, N0 × 0, N4 × 0.**

---

## What this paper contributes to science

1. **A new dataset** — the largest bias-audited chirality catalog ever, released under CC-BY-4.0.
2. **A null refutation** — Shamir (2020)'s ~3 % claim falls 7× below a higher-SNR measurement; the cosmological principle survives.
3. **A new primitive** — equivariant TTA as a model-agnostic bias-removal step, adoptable by any future chirality study.
4. **A cross-pipeline validation** — CE-ResNet independently recovers the same null at part-in-10 ⁴.
5. **A recipe** — documented rescue of a catastrophically biased baseline classifier.
6. **A falsifiability threshold** — 0.2 % 3σ floor for future anisotropic-cosmology predictions.
7. **Infrastructure** — dipole code feeds Paper 3 limitation G (empirical α calibration).

The paper is a **high-quality null** in the Higgs-hunt sense: a measurement precise enough to kill a prior claim, with infrastructure that outlives the specific result. Null results of this caliber are rarer than detections.

---

## Cross-references

- Dipole infrastructure re-used in Paper 3 §7.3 limitation G (empirical Landy-Szalay w(θ))
- Bias-hardening philosophy exported to Paper 3 LAMOST blue-excess audit (98 % artifact rate §7.1)
- Paper 2 companion section (`paper2_chirality_section.tex`) cross-references this as "Golden 2026c"
