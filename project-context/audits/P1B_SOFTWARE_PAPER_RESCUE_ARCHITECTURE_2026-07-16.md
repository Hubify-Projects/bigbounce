# P1B software-paper rescue architecture — 2026-07-16

## Decision

Do not send the current v1B.0.112 manuscript through another incremental JCAP
review. Its exact-PDF board found no new computational defect, but both direct
providers still rejected the article because three bounded validation studies
do not constitute one standalone cosmology result. That is an article-
architecture failure, not a request for more wording polish.

The defensible durable contribution is the reusable software developed during
the closure campaign:

- exact NaMaster bandpower-window inference for uniform spin-2 rotation;
- deterministic multipole contracts;
- atomic checkpoint/results publication with tamper-evident receipts;
- content-addressed analysis manifests;
- fail-closed science contracts and exact-source provenance.

Package this contribution as **namaster-proof**. Treat the current CAMB,
NaMaster, and ALP studies as validation/use cases, not as three independent
physics discoveries.

## Target product

### Public software contract

The first release must provide:

1. an installable Python package with an OSI-compatible license;
2. a stable Python API for window response, bandpower evaluation, beta
   recovery, rotation, multipole limits, and checkpoint receipts;
3. a CLI for receipt publication/verification and deterministic contract
   checks;
4. tests that exercise numerical equivalence, invalid inputs, atomic receipt
   validation, and installation;
5. a versioned result/receipt schema and migration policy;
6. one minimal synthetic example that is not coupled to the BigBounce paper;
7. citation metadata and an explicit limitations statement;
8. compatibility for the existing production scripts until downstream users
   migrate.

The package must not claim to be a general cosmology inference engine. It is a
focused verification layer for exact pseudo-C_ell window inference and
tamper-evident computational provenance.

### Manuscript contract

Working title:

> **namaster-proof: Exact pseudo-C_ell window inference and tamper-evident
> provenance for reproducible spin-2 analyses**

Required sections:

1. Summary
2. Statement of need
3. Software architecture
4. Exact-window inference
5. Deterministic execution and provenance
6. Validation and tests
7. Worked cosmology examples
8. Limitations
9. Availability and archival record

The manuscript must remove or move to supplementary documentation:

- the broad cosmological-tensions review;
- standalone ECH/contact-operator interpretation;
- extended w0-wa posterior discussion;
- standalone ALP phenomenology and spectator-dark-energy interpretation;
- venue-level novelty claims about the three physics studies;
- historical review and closure narrative.

It may retain, as explicitly bounded validation examples:

- reproduction of the frozen stock-CAMB proxy summaries;
- 500-realization physical-spectrum beta recovery and robustness results;
- prior-predictive ALP frequencies, clearly conditional on the declared model
  and priors;
- manifest, source, checkpoint, and receipt guarantees;
- known limitations and failure modes discovered by the real production run.

## Venue decision

The current JCAP computational-research profile is not supported by the latest
review evidence. The preferred target is the **Journal of Open Research
Software** once the installable package, documentation, tests, public release,
and persistent archive exist. JOSS remains a secondary possibility if the
released package demonstrates sufficient reusable research functionality and
community scope.

Changing the registry is not authorized merely by this plan. It should occur
in the same release unit that produces the installable package and the first
software-paper manuscript, so the registry never advertises a venue contract
the repository cannot yet satisfy.

## Acceptance gates before the next external review

- [ ] `pip install` succeeds in a clean environment.
- [ ] Package API and CLI tests pass independently of repository-local import
      paths.
- [ ] Existing P1B production tests remain green.
- [ ] At least one repository production path consumes the package API or a
      compatibility proof demonstrates byte/numerical equivalence.
- [ ] README contains a runnable non-paper-specific example.
- [ ] LICENSE and CITATION metadata are present and consistent.
- [ ] The software manuscript compiles and passes the full PDF visual audit.
- [ ] Package version, manuscript version, release tag, source archive, and
      artifact manifest agree.
- [ ] The paper registry, SSOT, site, Convex, mirrors, and retained PDF are
      synchronized in the same release commit.
- [ ] One exact-PDF residual review is run under the software-paper rubric,
      with Codex subscription and direct Grok/Gemini only.

## Expected acceleration

This route stops spending review cycles defending an unsuitable three-study
JCAP narrative. It converts already-completed engineering and production
evidence into the article's central contribution, while preserving every
scientific limitation. The next review should test residual software-paper
quality and reuse—not rediscover that the current manuscript lacks a single
physics result.
