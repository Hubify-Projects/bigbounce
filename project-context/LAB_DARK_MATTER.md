# Lab Spec — Dark Matter Lab (Lab #4)

**Status:** SPEC ONLY — NOT seeded · Houston will create via the platform after Lab #1 ships
**Priority:** #4
**Slug:** `dark-matter-lab` (working name)
**Target repo:** `Hubify-Labs/dark-matter-lab`
**Target subdomain:** `darkmatter.hubify.app` or `dm.hubify.app`
**Stress-test target:** **a cleanly separate domain** — tests platform domain-agnosticism with no shared content from Lab #1
**Author:** Houston Golden + Claude
**Date:** 2026-04-08
**Linked from:** PRD §40

---

## 0. Houston's framing

> "#4 'Dark Matter Lab'"

That's all Houston wrote. He's interested but didn't expand. This spec is therefore Claude's interpretation of what a useful Dark Matter Lab would do, framed in the same shape as the other labs. Houston will edit when he creates it via the platform.

---

## 1. The thesis

**Dark matter is 27% of the universe and we still don't know what it is.** The leading candidates have been searched for decades with no detection:

- **WIMPs** (Weakly Interacting Massive Particles) — XENONnT, LZ, PandaX-4T have ruled out most of the cross-section parameter space. Status: shrinking
- **Axions** — ADMX, HAYSTAC searching specific mass windows. Status: progress, no detection yet
- **Primordial black holes (PBHs)** — microlensing constraints rule out most mass windows but a 10^-12 to 10^-10 solar-mass window remains open
- **Modified gravity (MOND, TeVeS, Verlinde)** — explains rotation curves but fails for cluster scales

**The dark matter "crisis" is now ~50 years old.** New approaches are needed.

**The Hubify Labs angle:** anomaly detection on existing astrophysical data could surface dark-matter signatures the community isn't currently looking for. This is the same playbook as Lab #1's anomaly engine but pointed at different surveys with different physics targets.

---

## 2. Mission + North Star

**Mission:** "Use multi-survey anomaly detection to find dark-matter signatures that traditional searches haven't looked for, in particular: PBH microlensing events at unusual mass ranges, axion-like signals in stellar spectra, and rotation-curve anomalies that could discriminate modified-gravity from particle dark matter."

**North Star:** **Number of dark-matter candidate signals identified per quarter, weighted by significance.** A "candidate" must be flagged at ≥ 3σ and survive at least one round of cross-provider review.

---

## 3. The 4 initial Projects

### Project 1: PBH Microlensing Anomaly Search

**Goal:** Search Gaia DR3 + ZTF + LSST early data for microlensing events with light curves inconsistent with the standard PSPL (point source point lens) model. PBHs in the 10^-12 to 10^-10 solar-mass window would produce events with shorter durations and different spectral shapes than stellar-mass lenses.

**Deliverable:** A catalog of PBH candidate events + a paper.

**Measurable:** Number of candidates found. False-positive rate (estimate vs known PSPL events).

### Project 2: Axion Spectral Signatures in Stellar Spectra

**Goal:** Train an autoencoder on stellar spectra (SDSS, LAMOST) and look for anomalous absorption/emission lines that could correspond to axion-photon coupling at the predicted mass scales.

**Deliverable:** Anomaly catalog + paper.

**Measurable:** Number of anomalous spectra flagged. Cross-match with magnetic field surveys (axion signal should correlate with magnetic environment).

### Project 3: Rotation Curve Anomaly Detection

**Goal:** Apply anomaly detection to galaxy rotation curves (SPARC database, MaNGA) to find galaxies that don't fit either standard CDM or MOND predictions. Outliers in BOTH directions would be informative.

**Deliverable:** A paper + a public-facing rotation-curve outlier catalog.

**Measurable:** Number of outliers identified. Statistical significance of any systematic outlier population.

### Project 4: Dark Matter Discrimination Table

**Goal:** Same pattern as Lab #3's Project 4 — build a comprehensive comparison table of every viable dark matter candidate against the current data, with a clear ranking.

**Deliverable:** A "Dark Matter Discrimination Table" paper + a public-facing site page.

**Measurable:** Number of candidates ruled out at > 3σ. Number still viable.

---

## 4. Initial agent roster

| Agent | Role | Model | Tier |
|---|---|---|---|
| **dark-matter-orchestrator** | Top-level | claude-opus-4-6 | HIGH |
| **microlensing-lead** | Project 1 | claude-sonnet-4-6 | MED-HIGH |
| **spectra-lead** | Project 2 | claude-sonnet-4-6 | MED-HIGH |
| **rotation-lead** | Project 3 | claude-sonnet-4-6 | MED-HIGH |
| **paper-lead** | Project 4 + manuscript authoring | claude-sonnet-4-6 | MED-HIGH |
| **anomaly-worker** | Survey scans + autoencoder training | claude-haiku-4-5 | LOW |
| **lightcurve-worker** | Light curve fitting | claude-haiku-4-5 | LOW |
| **(shared) peer-review-gpt** | Cross-provider | gpt-5 | HIGH |
| **(shared) peer-review-gemini** | Cross-provider | gemini-2.5-pro | HIGH |

---

## 5. Cross-lab sharing relationships

**Reads from:**
- **Lab #1 (Bounce Cosmology)** — read-only access to Lab #1's anomaly-detection pipeline (Pipeline 3 in Lab #1) and the spectral autoencoder training methodology. Lab #4 inherits the *technique* without inheriting the *content*.

**Writes back:** None expected initially.

**Public sharing:** `published-only`.

**Note:** This lab has **no overlap with the cosmology research** in Lab #1 — it's a cleanly separate domain. The only thing borrowed is the anomaly-detection pipeline pattern. This is intentional: it tests whether the platform's pipeline patterns are reusable across domains.

---

## 6. Initial datasets

- **Gaia DR3** (cross-matched with Lab #1's Gaia anomaly catalog as the starting point)
- **ZTF DR21** (Zwicky Transient Facility light curves)
- **SDSS DR18 + LAMOST DR10** (stellar spectra — same as Lab #1 but used for axion-search not anomaly detection)
- **SPARC rotation curve database**
- **MaNGA IFU data**

---

## 7. Bootstrap checklist

- [ ] Lab created via `/create lab dark-matter-lab` from the platform UI
- [ ] Mission + North Star + Director set
- [ ] 4 Projects created
- [ ] Agent roster bootstrapped (9 agents)
- [ ] Cross-lab read access requested from Lab #1 (for the anomaly-detection technique)
- [ ] First MCMC dispatch test succeeds on H200 (or dedicated pod if scaling)
- [ ] First chat-to-project graduation works
- [ ] First standup runs successfully

---

## 8. What this lab stress-tests on the platform

| Feature | How |
|---|---|
| **Domain separation** | Lab #4 has zero scientific overlap with Lab #1 — proves the platform isn't biased toward bounce cosmology |
| **Pipeline pattern reuse** | The anomaly-detection pipeline from Lab #1 is reused as a *pattern*, not as *content* — tests the cross-lab pattern library (Lab #2's Project 5) |
| **Multi-survey ingestion** | New surveys (ZTF, MaNGA, SPARC) not used in Lab #1 — tests the dataset registration flow with novel inputs |
| **Long-tail survey support** | SPARC and MaNGA are smaller, more curated datasets than DESI — tests the platform's ability to handle small + niche data, not just big surveys |

---

## 9. Why this lab matters

Houston only wrote "#4 'Dark Matter Lab'", but this lab is the **negative control** for the Hubify Labs platform. If the platform is genuinely domain-agnostic, this lab should be just as easy to bootstrap and run as Lab #1, despite having no shared content.

If creating this lab is significantly harder than Lab #1, that's a signal the platform has accidentally hardcoded bounce-cosmology assumptions somewhere — and the meta-lab (Lab #2) should flag it as a friction point to fix.

**This lab is the test that the platform isn't secretly a bounce-cosmology-only tool.**

---

## 10. Open questions

1. **Houston's actual interest level** — he only wrote "#4 'Dark Matter Lab'" with no expansion. Is this a real research priority for him, or a placeholder for "test the platform with another physics domain"? My read: **placeholder**, lower priority than #3 or #5.
2. **Compute budget** — same question as Lab #3. Share H200 or dedicated?
3. **Should this lab actually run, or just exist as a spec?** Houston can decide. The spec stress-tests the platform even if no real research happens — just creating the lab structure tests the bootstrap flow.
