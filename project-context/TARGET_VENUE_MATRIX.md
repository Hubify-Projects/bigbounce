# BigBounce target-venue matrix

**Status:** active routing contract for the 2026-07 publication campaign  
**Purpose:** stop spending review cycles against a journal/article type whose
editorial bar does not match the manuscript's actual contribution.

Venue fit is not a substitute for scientific correctness. Every manuscript
must still close its exact-artifact truth-audited findings. A verdict from one
venue profile must never be relabeled as a verdict from another.

## Official editorial anchors

- [Physical Review D](https://journals.aps.org/prd/about) requires a high-quality,
  significant, authoritative, and substantive addition in particle physics,
  field theory, gravitation, cosmology, or astrophysics.
- [Classical and Quantum Gravity](https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-quantum-gravity/)
  covers gravitational physics and spacetime. Its **Notes** category is for a
  brief useful/novel clarification, short new result, or point that would not
  normally merit a full research paper.
- [JCAP](https://jcap.sissa.it/jcap/help/helpLoader.jsp?pgType=about) covers
  cosmology, particle astrophysics, gravitational physics, galaxies, and
  large-scale structure; acceptance is based on quality, originality, and
  relevance, with length appropriate to the contribution.
- [AAS journal scopes](https://journals.aas.org/scope-statements/) distinguish
  AJ's observation/method/software emphasis from ApJS's extensive catalogs and
  large reference data compilations.
- [MNRAS instructions](https://academic.oup.com/mnras/pages/General_Instructions)
  are the fallback reference for original astronomy/astrophysics research when
  the AAS framing is not selected.

## Per-paper routing

| Paper | Primary target | Article type | Fallback | Why this is the fastest honest route | Pre-review fit gate |
|---|---|---|---|---|---|
| P1A | **CQG** | **Note** | CQG Research Paper; PRD only if a substantive new physics result is added | The current short paper isolates contact benchmarks and corrects/clarifies scalar-sector and torsion misconceptions. That maps directly to CQG's Note definition and avoids forcing a seven-page clarification through PRD's authoritative-substantive-addition bar. | Keep one short point, explicit conventions/invertibility, no phenomenological overreach; review as `CQG-NOTE`, never as PRD by default. |
| P1B | **JCAP** | Research article / computational methods | PRD Research Article | The paper is a cosmological validation suite—stock-CAMB MCMC, exact synthetic NaMaster recovery, and a spectator-ALP fit—rather than a new torsion cosmology. JCAP's cosmology/particle-astrophysics scope is the cleaner primary fit, provided the three studies have one explicit validation thesis. | One central validation claim; every proxy separated from physical-model inference; exact-window robustness complete; article length justified. |
| P2 | **PRD** | Research Article | JCAP Research Article | The load-bearing contribution is a matter-bounce primordial non-Gaussianity derivation plus conditional forecast recast, squarely within PRD gravitation/cosmology. Its current venue-correct exact-PDF board is already the strongest of the six. | Preserve the exact derivation/convention evidence, distinguish conditional sensitivity from a survey prediction, and keep residual archive/external-covariance items as workflow gates. |
| P3 | **ApJS** | Catalog article | AJ methods/catalog article | The contribution is an extensive, reusable public-ID recovery catalog with machine-readable tables, dictionaries, manifests, and validation. ApJS explicitly publishes catalogs and large reference compilations. | Chance-association control; warned-population comparison; original-member sensitivity; one authoritative citable package. |
| P4 | **ApJS** | Catalog + methods article | AJ observational/methods article | The public 8.5-million-galaxy catalog and reproducible observed-label null battery are the durable contribution. ApJS gives the catalog—not a primordial parity claim—the correct editorial center. | Lead with catalog/reference utility and declared primary null; retain transfer-function and covariance limits; no primordial bound. |
| P5 | **AJ** | Observational research article | MNRAS Research Article | The paper is a DESI/DESIVAST observational environment analysis with selection/method controls. AJ explicitly emphasizes observational results, interpretation, astronomical software, and computing. A fresh AJ-profile board already moved two reviewers to MINOR while the unchanged PRD board remained REJECT/MAJOR/ACCEPT. | Official GALZONE OUT=0 adjusted estimator as primary; author-defined any-hole result as sensitivity; DESIVAST first; post-hoc hierarchy and Paper-IV dependency explicit; secondary T-Web material compressed. |

## Review-packet contract

Every new review packet must declare all of the following before dispatch:

```text
paper_id
paper_version
source_commit
source_path
pdf_path
pdf_sha256
page_count
target_journal
article_type
review_profile_id
prompt_sha256
allowed_context_sha256
```

The content-addressed cache key is:

```text
sha256(pdf_sha256 + review_profile_id + prompt_sha256 + model + effort)
```

An identical key is reused, not rerun. A changed PDF, journal/article type,
prompt, model, or effort creates a new immutable packet. Reviewers remain blind
to each other's reports until every declared leg has submitted or is recorded
as a typed failure.

## Wall-clock acceleration rules

1. Run independent vendor legs concurrently; total panel latency should be the
   slowest successful leg, not the sum.
2. Run focused delta review after a bounded closure, but require one full blind
   exact-PDF panel before declaring the paper ready.
3. Stop rerunning an unchanged PDF/profile/model key. Repeated verdict noise on
   identical content is evidence about reviewer variance, not new manuscript
   progress.
4. Separate **science gates** (derivation, control, reproducibility, claim) from
   **workflow gates** (DOI, archive publication, human sign-off, companion ID).
   Both stay visible, but workflow gates do not trigger fake science edits.
5. Site and SSOT entries record the exact venue profile. PRD, CQG Note, AJ,
   ApJS, JCAP, and MNRAS boards remain separate forever.

## Decision log

- **2026-07-14:** P1A routed from default PRD to a CQG Note fit test after its
  correctness closure; PRD remains an honest comparison board, not the primary.
- **2026-07-14:** P5 unchanged v0.1.129 AJ fit panel (OpenAI MAJOR / Gemini MINOR
  / Grok MINOR) demonstrated a material venue effect relative to its PRD panel
  (OpenAI REJECT / Gemini MAJOR / Grok ACCEPT). This is not an acceptance claim;
  it is evidence that venue selection belongs before the next edit/review loop.
- **2026-07-14:** P3 retained ApJS because the journal explicitly serves catalogs
  and large reference compilations; the new exact-PDF panel found real controls
  to close, so venue correction did not waive scientific work.
