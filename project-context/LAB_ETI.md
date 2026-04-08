# Lab Spec — Extraterrestrial Intelligence Lab (Lab #5 / The Viral One)

**Status:** SPEC ONLY — NOT seeded · Houston will create via the platform after Lab #1 ships
**Priority:** **#5 — but Houston flagged HIGH PRIORITY for viral / press potential**, second after Lab #3 in his queue
**Slug:** `eti-lab` (working name)
**Target repo:** `Hubify-Labs/eti-lab`
**Target subdomain:** `seti.hubify.app` or `eti.hubify.app`
**Stress-test target:** **public-facing viral lab** — tests public sharing UX, the publish-loop's ability to ship press-ready content, and the platform's robustness against high-traffic spikes
**Author:** Houston Golden + Claude
**Date:** 2026-04-08
**Linked from:** PRD §40

---

## 0. Houston's framing (verbatim, full)

> "**#5 'Extraterrestrial Intelligence Lab'** : I LOVE THIS it has a lot of viral potential as aliens are super hot trending ALWAYS in pop culture and press will eat it upppppp — so honestly super interested high priority i want to tackle this one next after the dark energy quintom thing from #3 since that directly relates to the original failed** ambition of paper 1 and 14 barrier failures in the bounce cosmology
>
> **Search for Extraterrestrial Intelligence**
>
> ### Artificial Light from Exoplanets
>
> Loeb & Turner (2012) proposed that artificial illumination on the night side of tidally locked exoplanets could be detectable with next-generation telescopes. The signal would be a slight flux excess compared to what albedo alone predicts, with a specific spectral signature (LED/sodium lamp emission lines vs thermal blackbody). An autoencoder trained on 'normal' exoplanet phase curves would flag planets with anomalous night-side emission as candidates. JWST might already have the sensitivity for nearby systems.
>
> *Speculative but testable · JWST · Loeb & Turner (2012) · Phase curves*
>
> ### Anomalous Stellar Spectra: Dyson Spheres?
>
> A Dyson sphere (or swarm) would absorb starlight and re-emit in infrared, creating excess IR emission with no natural explanation. Searches have been done on small samples. Our autoencoder approach on Gaia + AllWISE photometry for billions of stars could flag candidates at scale. Suazo et al. (2022) found 7 candidates from 5 million stars. We could search 100x more.
>
> *ACTIONABLE · Gaia DR3 + AllWISE · IR excess anomaly detection*
>
> ### SETI at Scale: Anomaly Detection on Radio Surveys
>
> The Breakthrough Listen project has petabytes of radio telescope data. Traditional SETI searches for narrow-band signals. An unsupervised anomaly detector could find signals that don't match ANY known natural or artificial pattern — the signals we don't know to look for. This is philosophically identical to what we're doing with DESI spectra: find what doesn't fit.
>
> *Future · Breakthrough Listen · Radio anomaly detection*
>
> ### Interstellar Objects
>
> 'Oumuamua and Borisov were the first confirmed interstellar visitors. Rubin/LSST will detect more. Anomaly detection on their trajectories, spectra, and light curves could identify objects with properties inconsistent with natural comets or asteroids. This isn't necessarily 'aliens' — even purely natural interstellar chemistry would be a major discovery.
>
> *Future · Rubin/LSST ~2025-2035 · Trajectory anomalies*"

---

## 1. The thesis

**Houston's instinct on virality is correct.** Aliens are perpetually hot in pop culture and press. Any rigorous, well-instrumented search effort that produces public catalogs and forecast updates will get attention disproportionate to the science budget. This lab is therefore valuable on TWO axes:

1. **Real science** — anomaly detection on existing astrophysical surveys could surface SETI signals that traditional approaches miss. Worth doing on the merits.
2. **Platform validation + reach** — every press hit drives users to Hubify Labs. The lab's public site becomes a recruitment funnel for the platform itself. Aligns with the meta-lab's North Star ("verified novel scientific contributions per week, summed across labs").

**The four search axes** Houston identified (verbatim above) are all genuinely actionable:
- **Artificial light from exoplanets** — JWST data + Loeb & Turner 2012 framework
- **Dyson spheres** — Gaia DR3 + AllWISE IR excess (Suazo+ 2022 found 7/5M, we can do 100x more)
- **SETI radio anomaly detection** — Breakthrough Listen petabytes + unsupervised anomaly detection
- **Interstellar objects** — Rubin/LSST when it comes online (2025+), trajectory anomalies on 'Oumuamua-class objects

The first two are ACTIONABLE NOW with existing public data. The second two are FUTURE work that becomes actionable as Breakthrough Listen and Rubin release more data.

---

## 2. Mission + North Star

**Mission:** "Search for technosignatures and natural-but-anomalous phenomena that could indicate extraterrestrial intelligence, by applying anomaly detection at scale to existing astronomical surveys."

**North Star:** **Number of high-quality candidate detections published, weighted by surprise.** A "high-quality candidate" must:
1. Be flagged at ≥ 4σ by the lab's anomaly detector
2. Survive 3 rounds of cross-provider peer review
3. Be reproducible from public data
4. Have a clear "what would falsify this" criterion

**Secondary metric (the viral one):** **Press mentions per quarter** — track Hubify Labs ETI mentions in major science outlets (NYT, Quanta, Nature News, Science News). Not a target, but a signal that the lab is reaching the audience.

**Anti-metric:** number of premature press claims. Houston is on record as wanting to **underrate**, not overclaim. A single false-positive aliens claim would torch the lab's credibility for years. The orchestrator must aggressively gatekeep against any "we found aliens" framing until the evidence is bulletproof.

---

## 3. The 4 initial Projects

### Project 1: Dyson Sphere IR Excess Search (ACTIONABLE NOW — first priority)

**Goal:** Apply autoencoder anomaly detection to the Gaia DR3 + AllWISE cross-match (~500M stars with both optical + IR photometry). Find stars with IR excess that can't be explained by dust, circumstellar disks, or normal stellar evolution.

**Deliverable:** A catalog of Dyson sphere candidates + a paper. Compare directly with Suazo+ 2022 (7 candidates from 5M stars).

**Measurable:**
- Candidates per million stars (target: comparable to or better than 7/5M = 1.4/M baseline)
- False positive rate (cross-check: how many of our candidates have known natural explanations on follow-up?)
- 100x scale: we want to search at least 500M stars (Suazo searched 5M)

**Why first:** existing public data, well-defined methodology (Suazo+ 2022), high signal-to-noise catalog work, immediate publishable result.

### Project 2: Exoplanet Night-Side Light Search

**Goal:** Apply anomaly detection to JWST exoplanet phase curves. Look for night-side flux excess that exceeds what albedo alone would predict, with spectral signatures consistent with artificial illumination (LED, sodium lamp).

**Deliverable:** A catalog of phase curve anomalies + a paper.

**Measurable:**
- Number of phase curve anomalies flagged
- Cross-match with known exoplanet properties (tidally locked? in habitable zone?)
- Spectral signature consistency with the Loeb & Turner (2012) prediction

**Why second:** JWST data is becoming available but the sample size is small (dozens, not millions). Lower signal but higher novelty.

### Project 3: SETI Radio Anomaly Detection (Future-ish — needs Breakthrough Listen access)

**Goal:** Run unsupervised anomaly detection on Breakthrough Listen radio data. Find signals that don't match ANY known natural or artificial template.

**Deliverable:** A catalog of radio anomalies + a paper.

**Measurable:**
- Anomaly count
- Cross-match with sky position (terrestrial RFI vs extraterrestrial origin)
- Reproducibility on independent observation runs

**Why third:** requires data partnership with Breakthrough Listen, which may take time to negotiate. Could be done with public BL data subsets.

### Project 4: Interstellar Object Trajectory Anomaly Detection (Future)

**Goal:** When Rubin/LSST starts producing transient detections at scale, look for interstellar objects ('Oumuamua, Borisov, and successors) with anomalous trajectories, spectra, or light curves.

**Deliverable:** Catalog + paper. Even purely natural interstellar chemistry anomalies are publishable.

**Measurable:** Number of interstellar objects detected + number with anomalous properties.

**Why fourth:** Rubin first light + first survey data is 2025+. This project becomes actionable as the data lands.

---

## 4. Initial agent roster

| Agent | Role | Model | Tier |
|---|---|---|---|
| **eti-orchestrator** | Top-level | claude-opus-4-6 | HIGH |
| **dyson-lead** | Project 1 (Dyson sphere search — first priority) | claude-sonnet-4-6 | MED-HIGH |
| **exoplanet-lead** | Project 2 (JWST phase curves) | claude-sonnet-4-6 | MED-HIGH |
| **radio-lead** | Project 3 (SETI radio) | claude-sonnet-4-6 | MED-HIGH |
| **trajectory-lead** | Project 4 (interstellar objects) | claude-sonnet-4-6 | MED-HIGH |
| **paper-lead** | Manuscript authoring (revtex4-2 like Lab #1) | claude-sonnet-4-6 | MED-HIGH |
| **outreach-lead** | Public-facing site content + press kit | claude-sonnet-4-6 | MED |
| **anomaly-worker** | Survey scans + autoencoder training | claude-haiku-4-5 | LOW |
| **photometry-worker** | IR/optical cross-match | claude-haiku-4-5 | LOW |
| **claim-gatekeeper** | **HARD-CODED skeptic** — blocks any "aliens" claim from publishing without ≥ 5 independent verifications | claude-sonnet-4-6 (skeptic mode) | HIGH |
| **(shared) peer-review-gpt** | Cross-provider | gpt-5 | HIGH |
| **(shared) peer-review-gemini** | Cross-provider | gemini-2.5-pro | HIGH |
| **(shared) peer-review-grok** | Contrarian cross-provider | grok-4 | MED-HIGH |

The **`claim-gatekeeper`** agent is unique to this lab. Its only job is to prevent premature alien-claim hype. Any contribution proposed for N3+ that mentions "extraterrestrial intelligence", "technosignature", or "alien" must pass this agent's sign-off in addition to the normal publish-ready loop.

---

## 5. Cross-lab sharing relationships

**Reads from:**
- **Lab #1 (Bounce Cosmology)** — read-only access to the anomaly-detection pipeline pattern (Pipeline 3) and the Gaia DR3 catalog work. Lab #5 inherits the technique.
- **Lab #4 (Dark Matter)** — shared anomaly-detection pattern, possibly shared Gaia DR3 cross-match catalog.

**Writes back:** None.

**Public sharing:** **`everything-but-internal-debate`**. The lab is public-facing by design. The catalog, the methodology, the candidates — all public. The internal debates between agents (which candidates are real vs noise, which framings are too strong) stay private. This is a NEW sharing mode that needs to be specced into PRD §40.11 — **call it `transparent`**.

**Why public-by-default:** the science wins by being open. Press wins by having something to write about. Recruitment wins by having a public face. The only thing that loses is competitive advantage on individual candidates — and Houston explicitly rejects competitive secrecy as an anti-pattern in independent research.

---

## 6. Initial datasets

- **Gaia DR3** (already in Lab #1)
- **AllWISE** (NEW — needs cross-match with Gaia at lab bootstrap)
- **JWST exoplanet phase curves** (public release, ~50 systems as of 2026)
- **Breakthrough Listen public subset** (initial — full access TBD)
- **(future) Rubin/LSST early transient catalogs**

---

## 7. The viral playbook (the press kit infrastructure)

The thing that makes this lab different from a normal research lab is that **press is explicitly part of the deliverable**. The lab needs infrastructure for:

1. **Public site** — `seti.hubify.app` (or final). Houston-quality design, mobile-first, fast.
2. **Live candidate counter** — homepage stat: "X Dyson sphere candidates detected, Y phase curve anomalies, Z radio signals under review". Updates in real time.
3. **Per-candidate detail page** — click any candidate, see its data, the analysis, the cross-checks, the current verdict. Auto-generated by the orchestrator.
4. **Press kit** — auto-maintained page with high-res images, fact sheets, quotes from Houston, and contact info. Updated weekly.
5. **The "How we're avoiding overclaim" page** — front and center. Explains the N0-N4 nomenclature. Explains the claim-gatekeeper agent. Explains why the lab will NEVER announce "aliens" until the evidence is overwhelming. This page is the credibility shield.
6. **Newsletter signup** — monthly update on new candidates, cross-checks, ruled-out cases. Drives recurring engagement without notification spam.

**The outreach-lead agent** is responsible for keeping all of this current.

---

## 8. Bootstrap checklist

- [ ] Lab created via `/create lab eti-lab` from the platform UI
- [ ] Mission + North Star + Director set
- [ ] 4 Projects created (Dyson spheres prioritized as Project 1)
- [ ] Agent roster bootstrapped (13 agents)
- [ ] **claim-gatekeeper agent installed and tested** — must reject any premature "aliens" claim
- [ ] Cross-lab read access requested from Lab #1 (anomaly pipeline)
- [ ] Public site bootstrapped at chosen subdomain
- [ ] Press kit infrastructure built
- [ ] First Dyson sphere search dispatched on H200
- [ ] First chat-to-project graduation works
- [ ] First standup runs successfully

---

## 9. What this lab stress-tests on the platform

| Feature | How |
|---|---|
| **Public sharing UX** | Lab is public-by-default — tests the public sharing settings end-to-end |
| **Press kit infrastructure** | Auto-maintained press materials — tests the writing-worker pattern at production quality |
| **Claim gatekeeping** | The `claim-gatekeeper` agent is a hard veto on the publish-loop — tests the "agent veto" pattern |
| **High-traffic spikes** | If a candidate goes viral, the public site needs to survive Hacker News + Reddit hugs of death — tests Vercel deploy + CDN behavior |
| **Multi-domain technique sharing** | Lab #5 borrows from Lab #1 + Lab #4's anomaly-detection patterns — tests multi-source pattern inheritance |
| **The N-score system in practice** | Every candidate gets an N-score and must NEVER be claimed as N4 without external corroboration — tests the underrate-not-overrate discipline |

---

## 10. The risk

This lab is the highest-risk lab in the platform's first 6 months. The risks:

1. **False positive that goes viral** — a candidate gets press attention, then turns out to be instrumental noise. Hubify Labs reputation takes a hit.
2. **Premature claim by an over-eager agent** — the claim-gatekeeper exists specifically to prevent this.
3. **Press spam** — if the lab posts too much, the press stops paying attention. Outreach-lead must be disciplined.
4. **Crackpot association** — the lab needs to clearly distinguish itself from the "I saw a UFO" crowd. The "How we're avoiding overclaim" page is the shield.

**Mitigation:** the entire lab is built around the claim-gatekeeper + N-score discipline + cross-provider peer review. If those break, the lab has to be paused. Houston signs off on all N3+ claims personally during the first year.

---

## 11. Why this lab matters

Houston's quote: *"I LOVE THIS it has a lot of viral potential as aliens are super hot trending ALWAYS in pop culture and press will eat it upppppp"*

He's right. The platform needs ONE lab that's fundamentally public-facing to test the public sharing infrastructure. SETI is the perfect test case because:
- The science is real and well-established (Loeb & Turner 2012, Suazo+ 2022 are peer-reviewed)
- The methodology (anomaly detection on existing surveys) maps cleanly onto Lab #1's existing pipelines
- The press hooks are obvious without being misleading
- There's a clear underrate-not-overrate discipline that prevents the lab from becoming a UFO blog

If this lab succeeds (real candidates, real catalogs, real papers, no embarrassments), it becomes the **public face of Hubify Labs**. Press writes about it, researchers join the platform because of it, the meta-lab's North Star (verified novel contributions per week) goes up.

**This is the lab that makes Hubify Labs famous. Built carefully, it's the platform's biggest growth engine. Built carelessly, it's the platform's biggest reputation risk.**

---

## 12. Open questions

1. **Subdomain** — `seti.hubify.app` (recognizable acronym) vs `eti.hubify.app` (matches the lab slug) vs `aliens.hubify.app` (most viral, least scientific). Houston decides — my recommendation: **`seti.hubify.app`** (recognizable + scientific).
2. **First public release timing** — when does the first Dyson sphere candidate catalog go public? Recommended: **after the first 3 candidates have survived cross-provider peer review AND a ≥ 30-day cooling period**. No rush.
3. **Press strategy** — does Houston want active media outreach, or passive (let press find us)? My recommendation: **passive for the first 3 months** (build the catalog, build the site, let the work speak), then active if catalog quality justifies it.
4. **Breakthrough Listen partnership** — does Houston have the contacts? If not, this might delay Project 3.
5. **The `transparent` sharing mode** — needs to be added to PRD §40.11 if Lab #5 uses it. Or is `published-only` sufficient with everything-but-debates published? My recommendation: extend §40.11 with `transparent` mode.
