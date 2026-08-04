# BigBounce publication architecture reset

**Decision draft for Houston · 2026-08-03**

## Blunt verdict

The current six-paper count is not a scientific result and should not govern
what gets submitted. It is the residue of earlier splits, rescue operations,
and downstream dependencies:

- the former broad Paper I was split into a narrow theory note (P1A) and a
  software paper (P1B);
- the anomaly paper was successively narrowed until the active P3 became a
  public-identifier recovery note;
- the chirality catalog (P4) produced a downstream environment analysis (P5).

Those are legitimate outputs, but they are not six equal chapters of one
scientific argument. Presenting them that way makes supporting machinery look
like the science and hides one of the strongest original projects: the DESI
anomaly-discovery survey.

The program should be organized by research question, with **primary research
articles** separated from **specialist publications**, **technical data
products**, and **optional companion analyses**. No current artifact is being
deleted. The six finished candidate packages remain preserved as evidence and
possible submission assets, but the six-at-once submission plan is on hold.

## The simple map

| Research program | Main question | Primary scientific output | Supporting or optional output |
|---|---|---|---|
| Bounce theory | Does matter-dominated contraction produce a distinctive, exactly reproducible primordial non-Gaussian amplitude? | **P2** | **P1A** narrow ECH boundary note; **P1B** software |
| Survey discovery | What unusual spectra are found by a full-scale DESI anomaly search, and which candidates survive scientific validation? | **Rebuilt anomaly-science paper** | Current **P3** integrated public-ID/provenance release |
| Galaxy chirality | Is there a large-scale observed-label chirality dipole in the released DESI imaging catalog? | **P4** | **P5** standalone AJ companion on environment dependence |

This is a portfolio of **three core scientific stories**, not a promise that
the final submission count must equal three or six.

## What each current paper actually is

### P1A — Algebraic Cartan elimination

**Plain-English reason it exists:** We began with a much broader attempt to
connect minimal Einstein--Cartan--Holst gravity to dark energy, a bounce, and
observable parity effects. The defensible result that survived review was
narrower: under clearly stated minimal assumptions, eliminate the
non-propagating connection and show what remains on spin-sourced and zero-spin
scalar branches.

**Actual contribution:** A convention-audited consolidation of standard
identities, an explicit contact-interaction coefficient and scale benchmark,
and sharply bounded statements about where minimal ECH does and does not
change the scalar/tensor dynamics.

**What it is not:** It is not a new dark-energy model, a complete no-go theorem
for torsion cosmology, or an empirical discovery. The manuscript says this
honestly.

**Disposition:** Keep as a narrow theory Note. It is scientifically coherent
but secondary to the main bounce result and should not be marketed as a
flagship breakthrough.

### P1B — `namaster-proof`

**Plain-English reason it exists:** A broad cosmology companion could not
support its original claims. The reusable, independently defensible part was
the software built to prevent two concrete analysis failures: replacing the
full pseudo-C_ell window operator with shortcuts and losing the binding
between numerical results and their execution evidence.

**Actual contribution:** A small verification library for exact NaMaster
window inference and tamper-evident, content-bound computational receipts.

**What it is not:** It is not a cosmological measurement or a second bounce
physics result.

**Disposition:** Keep as a separate software paper. List it under Research
Software, not as one of the core scientific papers.

### P2 — Exact matter-contraction non-Gaussianity

**Plain-English reason it exists:** This is the cleanest answer to the
program's original cosmology question: what observable theoretical signature
does a matter-dominated contracting phase predict?

**Actual contribution:** An exact four-vertex rederivation of
`f_NL^local = -35/16`, including the ordered polynomial coefficients and
independent cross-checks. The observational mapping is useful orientation but
is explicitly conditional on nonlinear transmission through a bounce and on
forecast assumptions.

**What it is not:** It is not a measured detection, a complete bounce model,
or an unconditional SPHEREx forecast.

**Disposition:** Keep and center as a primary theory paper. This is the
flagship paper in the bounce-theory track.

### Current P3 — Public-ID recovery for a historical anomaly list

**Plain-English reason it exists:** The old public anomaly catalog contained
mixed internal identifiers and could not be deterministically joined back to
public DESI spectra. This paper repairs that provenance problem and produces a
small, auditable follow-up list.

**Actual contribution:** Memory-bounded join and checkpoint machinery plus 181
warning-free public TARGETID associations, divided into a 170-row
high-coordinate-consistency core and 11 lower-confidence positional matches.

**What it is not:** It does not run or validate the anomaly detector, measure
an anomaly rate, demonstrate novelty or purity, classify the discoveries, or
publish the original full-survey science. Its use of the BigAE list is lineage
and coordinate provenance.

**Disposition:** Integrate it as the citable supporting data/provenance release
for the rebuilt anomaly paper. Do not submit it as an independent ApJS paper
and do not present it as the replacement for the anomaly-discovery paper. Its
public label is **Supporting Data Release · DESI Public-ID Recovery**.

### P4 — DESI observed-label chirality catalog and dipole null

**Plain-English reason it exists:** Test a controversial large-scale
chirality claim on a much larger catalog while documenting the classifier and
selection limitations honestly.

**Actual contribution:** An 8.47-million-row observed-label catalog, a
quality-controlled 890,069-object high-confidence sample, and a declared
primary dipole result consistent with zero. It also isolates unresolved
upstream label asymmetry and training-composition limitations instead of
hiding them.

**What it is not:** It is not a physical primordial-parity constraint; the
morphology transfer function and systematics needed for that inference remain
open.

**Disposition:** Keep as a primary catalog-and-observational-result paper. It
is the core paper in the chirality track.

### P5 — Chirality versus cosmic-web environment

**Plain-English reason it exists:** Once P4 created chirality labels, we asked
whether their frequency changes between released DESIVAST void and non-void
environments.

**Actual contribution:** A controlled, catalog-native comparison whose focal
contrast is consistent with zero, with extensive sensitivity analyses and
clear caveats.

**What it is not:** It is not independent of P4, preregistered, a physical
handedness measurement, or a cosmological constraint. It is exploratory and
post-hoc.

**Disposition:** Keep as a standalone AJ companion. Its environment-dependence
question, independent DESI/LSS joins, and systematics-controlled null are
distinct enough from P4 to justify a separate reader journey; merging it would
overload the catalog paper. Its dependence on P4 labels remains explicit. Its
public label is **Standalone Companion · Chirality–Environment Null Test**.

## What happened to the original anomaly paper

Houston's concern is correct: the active P3 did not merely improve the
original anomaly survey; it replaced its scope.

The deprecated manuscript `pipelines/p3_anomaly_engine/paper3_draft.tex`
describes a multi-survey autoencoder catalog with hundreds of thousands of
outliers and cosmological demonstrations. Commit `913f5033` first narrowed the
ApJS paper while retaining a large multi-survey catalog. Commit `3f5582c2`
then replaced 2,387 lines with the focused DESI public-ID manuscript that is
now P3.

Meanwhile, a separate surviving DESI line under
`pipelines/p1_highz_tracers/` and `projects/desi-dr1-anomalies/` contains the
actual discovery-oriented work: full-scale scoring, candidate taxonomies,
gold samples, line identification, photo-z experiments, NEOWISE matching,
and unusual-object follow-up.

That science cannot simply be restored by reviving an old TeX file. Its
recorded populations conflict across generations:

- an older outline reports 17,651,065 spectra and 195,829 thresholded
  anomalies;
- the deprecated multi-survey draft reports a different 37.3-million-input,
  roughly 268-thousand-candidate product;
- the current project README reports 22,504,897 DESI spectra, 2,145
  SNR-filtered anomalies, and 1,127 uncataloged objects;
- a surviving enhanced-catalog summary uses still other threshold and SNR
  definitions.

These may describe different valid stages or cuts, but they are not presently
one auditable scientific sample. The correct next move is a source-to-claim
reconciliation, not marketing the largest number.

## Recommended portfolio hierarchy

### Core scientific papers

1. **P2 — exact matter-contraction amplitude**: primary theory result.
2. **Rebuilt DESI anomaly-science paper**: primary discovery/catalog result,
   contingent on a new evidence audit.
3. **P4 — chirality catalog and dipole null**: primary observational/catalog
   result.

### Specialist publications

4. **P1A — minimal ECH boundary Note**: coherent narrow theory result.
5. **P1B — `namaster-proof` software paper**: coherent software result.

### Standalone companion

6. **P5 — environment comparison**: a distinct AJ companion to P4.

### Supporting release, not a standalone paper

- **Current P3 — public-ID recovery**: integrated provenance/data release for
  the rebuilt anomaly flagship.

The provisional endpoint is therefore **six standalone works plus one
supporting data release**. That happens to total six papers only after replacing
the old standalone P3 with the rebuilt anomaly flagship; the number now follows
the scientific questions and venue fit rather than controlling them. The public
story remains three research programs with three clear lead results.

## Approved execution state — 2026-08-04

Houston approved executing the recommended next steps with: `continue all best
next steps`.

- The three-program public framing is approved.
- Current P3 is removed from the standalone submission queue and retained as
  the anomaly program's supporting data/provenance release.
- P5 remains a standalone AJ companion.
- The rebuilt anomaly flagship is the primary scientific reconstruction task;
  it is not yet submission-ready.
- Directive-P scores and finished candidate artifacts remain preserved as
  technical evidence, not as instructions to publish the old six-candidate
  lineup.

## Production truth audit

A read-only production check on 2026-08-03 found that the site loads normally,
reports no browser console errors, and serves the current six candidate PDFs.
Its scientific framing is nevertheless a stop-ship defect:

- the home and papers pages still lead with “six papers” and “two halves”;
- the site still describes P1B as an MCMC/cosmology companion even though the
  current P1B is a focused software metapaper;
- the publication command center says all six are science-complete and that
  endorsement is the sole remaining decision;
- the publication language treats technical candidate readiness as proof that
  every candidate should be an independent paper.

After the current deployment completed, P3 r17, P4 v1.0.274, and P5 v0.1.147
matched the Convex records and were served as real PDFs with the expected byte
lengths, alongside P1A v1A.0.127, P1B v2B.0.16, and P2 v1.7.130. The next
production change is therefore a content-architecture correction, not another
version bump: it must atomically ship the approved research-program framing,
honest status language, and any selected-paper decisions.

## Execution plan

1. **Anomaly evidence reconciliation.** Use the completed initial inventory at
   `project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`, then close
   its remaining restoration gates: recover the enhanced parent/model, bind
   hashes, and reconcile the `S>5` generations.
2. **Anomaly manuscript architecture.** From the reconciled inventory, choose
   one scientifically meaningful primary sample and rebuild the discovery
   paper around method validation, catalog characterization, candidate
   taxonomy, and genuinely supportable notable objects. Keep cosmology demos
   subordinate unless their estimators independently survive review.
3. **Current P3 editorial decision — complete.** Integrate it as the rebuilt
   anomaly paper's supporting data/provenance release; retire standalone ApJS
   routing.
4. **P5 editorial decision — complete.** Keep it as a standalone AJ companion
   to P4 with dependency and exploratory scope explicit.
5. **Public-site rewrite.** Replace “six papers” with Research Programs. Each
   program page should start with the question, result, limitation, lead paper,
   and linked supporting software/data. Readiness and review machinery move
   below the science story.
6. **Submission-board rebuild.** Only after those decisions, regenerate the
   approval board, venue order, archive plan, endorser plan, and exact served
   hashes. Then Houston reviews the actual selected portfolio.

## Decision record

The three-program hierarchy, anomaly rebuild priority, integrated-P3 role, and
standalone-P5 role are approved. The remaining human decisions concern the
actual selected manuscripts, final PDFs, archive actions, and submissions—not
the portfolio architecture.
