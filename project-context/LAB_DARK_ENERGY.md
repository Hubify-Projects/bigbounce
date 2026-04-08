# Lab Spec — Dark Energy Lab (Lab #3)

**Status:** SPEC ONLY — NOT seeded · Houston will create via the platform after Lab #1 ships
**Priority:** #3
**Slug:** `dark-energy-lab` (working name)
**Target repo:** `Hubify-Labs/dark-energy-lab`
**Target subdomain:** `darkenergy.hubify.app` or `de.hubify.app`
**Stress-test target:** **cross-lab sharing** — this lab inherits relevant content from Lab #1 (Bounce Cosmology) via the read-only cross-lab access pattern + comm gateway
**Author:** Houston Golden + Claude
**Date:** 2026-04-08
**Linked from:** PRD §40

---

## 0. Houston's framing (verbatim from 2026-04-08 batch)

> "#3: 'Dark Energy Lab' — high relevance kinda worth just including/starting in our bounce cosmology Lab honestly since that directly relates to the original failed** ambition of paper 1 and 14 barrier failures in the bounce cosmology — but still worth creating a dedicated Lab for Dark Energy specifically as well that we can share this initial part from bounce lab with to start etc...
>
> **What Is Dark Energy?**
>
> 73% of the universe is dark energy and we don't know what it is. Our 14 barriers show ECH can't derive it from first principles, but the quintom bounce CAN unify bounce + dark energy through phantom fields. DESI DR2 shows w-crossing at 2.8–4.2σ. Our MCMC confirms at 98%. If w truly crosses -1, dark energy is dynamical, not a cosmological constant — and the quintom bounce provides a theoretical home for it. **ACTIONABLE · w0-wa MCMC · DESI DR2 · Quintom**
>
> i'll also want to share the bounce cosmology lab with this lab for sure"

---

## 1. The thesis

**Dark energy is 73% of the universe and we still don't know what it is.** Two competing pictures:

1. **Cosmological constant Λ** — dark energy is the vacuum energy of empty space, w = -1 forever, perfectly constant.
2. **Dynamical dark energy** — w varies with time. Phantom fields, quintessence, quintom, etc.

**The current best evidence (DESI DR2, 2024-2025):** w0-wa parameter space shows w-crossing through -1 at 2.8-4.2σ depending on dataset combination. **If w truly crosses -1, the cosmological constant picture is dead.**

**The bounce connection:** the 14 ECH barriers from Paper 1 show that Einstein-Cartan-Holst gravity *cannot* produce dark energy from first principles via the routes Houston exhaustively closed. But the **quintom bounce** can — phantom fields naturally produce w-crossing as a feature, not a bug. The quintom bounce provides a *theoretical home* for dynamical dark energy.

**This lab's purpose:** push the quintom-bounce dark-energy connection from "theoretical possibility supported by 98% MCMC posterior" to a publishable paper with a falsifiable prediction.

---

## 2. Mission + North Star

**Mission:** "Determine whether dark energy is a cosmological constant or dynamical, and if dynamical, identify the bounce-cosmology mechanism that produces it."

**North Star:** **Statistical significance of dynamical dark energy detection (target: ≥ 5σ)** in a peer-reviewed publication. Currently the strongest signal is 4.2σ (DESI DR2 + CMB + SNIa combined). The lab's job is to push this to discovery-level (5σ) or definitively rule it out.

**Secondary metrics:**
- Quintom bounce model predictions vs DESI DR3 (when DR3 lands)
- Cross-survey consistency (DESI vs DES vs LSST)
- The number of alternative dynamical-dark-energy models ruled out by combined constraints

---

## 3. The 4 initial Projects

### Project 1: w0-wa MCMC v2 with DESI DR2

**Goal:** Recompute the w0-wa MCMC posterior using DESI DR2 (full dataset) instead of DR1, plus the latest CMB and SNIa likelihoods.

**Deliverable:** A peer-reviewable paper draft + the chains + a contribution at N3 if the result is novel.

**Measurable:** w-crossing significance σ (target: trend toward 5σ). P(quintom-B | data) (currently 98.6% with DR1 — target: > 99.9% with DR2).

**Source from Lab #1:** the existing quintom-B chains in `bigbounce-hubify/lab/projects/quintom-b-discrimination/datasets/chains/`. Read-only cross-lab access. Lab #3's agents can read these chains, run new analyses on them, and propose updates back to Lab #1 via the comm gateway.

### Project 2: Phantom Field Theoretical Framework

**Goal:** Build a clean derivation of the quintom-bounce phantom-field mechanism, showing how phantom + standard scalar produce w-crossing without unitarity violations.

**Deliverable:** A theory paper draft (companion to Project 1's data paper).

**Measurable:** Internal consistency check (does the math work?), peer review verdicts from at least 3 cross-provider reviewers.

### Project 3: DESI DR3 Forecast

**Goal:** Forecast what DESI DR3 (expected 2026-2027) will tell us about w0-wa. Predict the σ levels and the parameter region where bounce-cosmology models will be confirmed or ruled out.

**Deliverable:** A short forecast note + a "tracking" page on the lab's site that updates as DR3 results come in.

**Measurable:** Forecast accuracy (compare predictions to actual DR3 once released).

### Project 4: Alternative Dark Energy Models — The Discrimination Table

**Goal:** Build a comprehensive comparison table of every viable dark-energy model (Λ, quintessence, quintom, phantom, k-essence, modified gravity, etc.) against the current data, with a clear ranking.

**Deliverable:** A "Discrimination Table" paper or contribution + a public-facing site page.

**Measurable:** Number of models ruled out at > 3σ. Number of models still viable at < 2σ.

---

## 4. Initial agent roster

| Agent | Role | Model | Tier |
|---|---|---|---|
| **dark-energy-orchestrator** | Top-level | claude-opus-4-6 | HIGH |
| **theory-lead** | Phantom field theoretical work | claude-sonnet-4-6 | MED-HIGH |
| **mcmc-lead** | DESI DR2 + DR3 analyses | claude-sonnet-4-6 | MED-HIGH |
| **paper-lead** | Manuscript authoring | claude-sonnet-4-6 | MED-HIGH |
| **mcmc-runner-worker** | Runs MCMC chains on H200 pod | claude-haiku-4-5 | LOW-MED |
| **literature-worker** | Watches arxiv for new dark-energy papers | claude-haiku-4-5 | LOW |
| **(shared) peer-review-gpt** | Cross-provider review | gpt-5 | HIGH |
| **(shared) peer-review-gemini** | Cross-provider review | gemini-2.5-pro | HIGH |

The cross-provider reviewers are SHARED with Labs #1 and #2 — same agent identities, billed against whichever lab requested the review.

---

## 5. Cross-lab sharing relationships

This is the lab that **stress-tests cross-lab sharing**.

**Reads from:**
- **Lab #1 (Bounce Cosmology)** — read-only access to the quintom-B project's chains, the 14 ECH barriers framework, and the related papers. The Dark Energy Lab inherits this content by reference, not by copy.

**Writes back to (via comm gateway only — not direct file edits):**
- **Lab #1 (Bounce Cosmology)** — when this lab discovers something relevant to Bounce Cosmology (e.g., "the new DR2 chains improve the quintom-B significance to 4.5σ — please update Paper 1 §5.2"), it sends a comm-event to the Bounce Cosmology orchestrator. The Bounce Cosmology orchestrator decides whether to apply the update.

**Public sharing:** `published-only`. Papers ship to `darkenergy.hubify.app`. Internal MCMC chains stay private until paper publication.

---

## 6. Initial datasets

- **DESI DR2 BAO + RSD** (downloaded from the public DESI release)
- **DES SN5YR** (Dark Energy Survey supernova sample)
- **Pantheon+ SNIa**
- **Planck 2018 CMB likelihoods**
- **Lab #1's quintom-B chains** (via cross-lab read access — referenced, not copied)

---

## 7. Bootstrap checklist

- [ ] Lab created via `/create lab dark-energy-lab` from the platform UI
- [ ] Mission + North Star + Director set
- [ ] 4 Projects created
- [ ] Agent roster bootstrapped (8 agents)
- [ ] Cross-lab read access requested from Lab #1 (Bounce Cosmology)
- [ ] First MCMC dispatch test (no-op chain) succeeds on H200
- [ ] First chat-to-project graduation works
- [ ] First standup runs successfully

---

## 8. What this lab stress-tests on the platform

| Feature | How |
|---|---|
| **Cross-lab sharing read access** | Lab #3 needs to read Lab #1's chains — tests the read-only cross-lab pattern |
| **Cross-lab comm gateway** | Lab #3 needs to send improvements back to Lab #1 — tests the suggestion-not-edit pattern |
| **Shared agents (peer reviewers)** | Same `peer-review-gpt` agent serves both Lab #1 and Lab #3 — tests multi-lab agent identity |
| **The Lab Sovereignty Rule** | Lab #3 cannot directly edit Lab #1's chains even if it has good reasons to — tests the hard invariant |
| **Real research, not synthetic** | This lab is doing real science (MCMC chains take real GPU time) — tests resource contention with Lab #1 on the same H200 pod |

---

## 9. Why this lab matters

Houston's framing: this is the lab that **redeems** the failed ambition of Paper 1. The 14 ECH barriers were a *negative* result — they showed that ECH can't derive dark energy. But the quintom bounce can. This lab takes the negative result from Paper 1 and turns it into the positive result that Paper 1 was originally aiming for.

If this lab succeeds, the bounce-cosmology research program has a complete narrative arc:
- **Paper 1 (Lab #1):** Here are the 14 things ECH cannot do.
- **Lab #3 first paper:** Here is what the quintom bounce CAN do — and the data already supports it at > 4σ.
- **Lab #3 second paper:** Here is the falsifiable prediction. DESI DR3 will confirm or rule it out.

That's a 3-paper arc that takes a negative result and converts it into a discovery (or definitive rule-out — both of which are publishable).

---

## 10. Open questions

1. **Compute budget** — does Lab #3 share Lab #1's H200 pod, or get its own? The pod can run multiple labs' work via separate tmux sessions. My recommendation: **share initially**, scale to dedicated pod if contention becomes a problem.
2. **Repo strategy** — separate repo from Lab #1, or subdirectory? Per the architecture lock (PRD §1 + §40.15), **separate repo** because each Lab gets its own.
3. **Subdomain** — `darkenergy.hubify.app` (verbose, clear) vs `de.hubify.app` (short, cryptic). Houston decides.
4. **Timing** — Houston wants to create this lab AFTER Lab #1 ships. Estimated: 2-4 weeks after migration completes, depending on stability.
