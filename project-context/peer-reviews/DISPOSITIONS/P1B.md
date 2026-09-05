# P1B disposition ledger

**Canonical source:** `arxiv/paper1b_namaster_proof.tex`
**Current paper-local version:** `v2B.0.8` (2026-07-16 strict-validation closure)
**Claim policy:** exact-window and receipt software validation; no sky measurement,
foreground model, cosmological inference, or ECH/bounce evidence. The legacy
v1B computational-companion dispositions remain below as retained history.

| ID | Issue | Status | Evidence / residual scope |
|---|---|---|---|
| DP1B-01 | Computational analyses were framed as verification of the ECH program. | **CLOSED-BY-EDIT v1B.0.105** | New title, abstract, introduction, proxy scope, ALP caveat, and conclusion state that stock CAMB, synthetic NaMaster, and generic ALP fitting do not implement or test ECH. |
| DP1B-02 | P1B repeated the obsolete claim that P1A closed the complete minimal-ECH dark-energy parameter space. | **CLOSED-BY-EDIT v1B.0.105** | The imported 13-barrier/four-route summary is non-rendering; live prose describes P1A's contact-channel and narrow classical-transparency results only. |
| DP1B-03 | Stock-CAMB `Delta N_eff` posterior was interpreted as an ECH/bounce compatibility result. | **CLOSED-BY-EDIT v1B.0.105** | It is now a generic extra-radiation proxy. Agreement with the parametric contact scale is explicitly not evidence for a theory. |
| DP1B-04 | Synthetic NaMaster injection was at risk of being read as a sky measurement or systematic floor. | **CLOSED-DISCLOSURE** | CMB-only synthetic scope, absent foreground degeneracy breaking, injected-signal nature, and `-0.032` to `-0.040 deg` bias range remain explicit. |
| DP1B-05 | Spectator-ALP result was at risk of being read as an ECH prediction. | **CLOSED-DISCLOSURE** | The model is labeled generic GR+ALP, accommodation rather than prediction; prior-volume and spectator-safe subset costs remain explicit. |
| DP1B-06 | Model comparison is absent; Planck-only chain is not converged; ALP likelihood is a summary likelihood. | **OPEN / DISCLOSED** | No Bayes-factor claim is made; the nonconverged chain is excluded from headlines; full EB likelihood and calibration/foreground treatment remain outside this paper. |
| DP1B-07 | Submission metadata and archive immutability. | **OPEN-SUBMISSION** | Coordinated arXiv IDs and final DOI/archive identifiers remain placeholders. No upload/tag was performed in this paper-local closure. |
| DP1B-08 | Fresh referee verdict on the standalone v1B.0.105 artifact. | **OPEN-REVIEW** | Compile/layout QA does not replace a fresh scientific review. |
| DP1B-09 | JORS software-metapaper architecture and package release. | **CLOSED-BY-SPLIT v2B.0.0** | The active manuscript is the focused `namaster-proof` software paper; the legacy computational dossier remains retained rather than presented as a standalone novelty claim. |
| DP1B-10 | Silent spectrum padding/truncation and invalid recovery inputs. | **CLOSED-BY-CODE v2B.0.1 / package 0.1.1** | Exact harmonic support, finite inputs, non-negative weights, and band-count identity fail closed with regression coverage. |
| DP1B-11 | Overbroad result/receipt transaction and tamper guarantees. | **CLOSED-BY-EDIT v2B.0.1** | The manuscript and README state that the files are sequential per-file atomic replacements and coordinated replacement requires trusted expected metadata or an external anchor. |
| DP1B-12 | Real PyMaster integration was absent. | **CLOSED-BY-ARTIFACT v2B.0.2** | The retained PyMaster 2.6 example recovers 0.250°, records the 0.315° shortcut result, and verifies operator agreement at 6.78e-21; its JSON/receipt are regression-tested. |
| DP1B-13 | Receipt verification mixed payload and receipt generations during concurrent publication. | **CLOSED-BY-CODE v2B.0.3 / package 0.1.2** | Verification now hashes and parses the same immutable result-byte snapshot it returns; a race regression fails before the fix and passes after it. |
| DP1B-14 | Portability, receipt terminology, stale canonical documentation, malformed prose, and reference-page collision. | **CLOSED-BY-EDIT v2B.0.3** | Windows CI and POSIX-specific durability wording replace unsupported OS independence; “content-bound” replaces filename-inaccurate “content-addressed”; superseded recovery values are removed from the canonical README; grammar and rendered references are corrected. |
| DP1B-15 | Persistent archive identifier and final correspondence metadata. | **OPEN-SUBMISSION / HUMAN** | Package 0.1.3 must be bound to an immutable public archive before JORS submission; author-supplied contact metadata remains a human gate. |
| DP1B-16 | Concurrent same-path publishers could cross-bind one execution's metadata to another execution's bytes. | **CLOSED-BY-CODE v2B.0.4 / package 0.1.3** | Each publisher now derives byte count and SHA-256 from its own immutable serialized snapshot rather than re-reading the shared destination path; a deterministic publisher-interleaving regression requires the mismatched pair to fail validation. |
| DP1B-17 | JSON publication and verification accepted non-standard `NaN`/`Infinity` constants. | **CLOSED-BY-CODE v2B.0.5 / package 0.1.4** | Publication uses `allow_nan=False` for payload and receipt before either file is written; verification rejects non-standard constants; two deterministic regressions cover payload, metadata, and retained-file parsing. |
| DP1B-18 | Compatibility-helper edits could bypass package CI because workflow path filters covered only the package tree. | **CLOSED-BY-CI v2B.0.5** | The workflow now triggers on both imported production helpers as well as package and workflow changes. |
| DP1B-19 | The production README described two cuts as Galactic latitude plus declination although the executable applies both in one native HEALPix latitude frame. | **CLOSED-BY-DOC v2B.0.5** | The configuration now states the single-coordinate-frame window contract and explicitly disclaims a Galactic/equatorial or survey-footprint interpretation. |
| DP1B-20 | Adding Author Contributions stranded the sharded-validation paragraph under the wrong section. | **CLOSED-BY-LAYOUT v2B.0.6** | Sharded validation is restored to Worked Examples before the Author Contributions section; the closure regression is visually audited. |
| DP1B-21 | The printed minimal API call used nonexistent keyword `beta_deg` instead of `beta_rad`. | **CLOSED-BY-DOC v2B.0.6** | The manuscript now prints the executable `beta_rad=np.deg2rad(0.25)` call, matching `windows.py` and the retained example. |
| DP1B-22 | The Windows CI matrix executed a POSIX multiline example under the runner-default PowerShell shell. | **CLOSED-BY-CI be218ed7** | The independent-example step explicitly selects Bash; `verify_ci_shell_portability.py` and regression fixtures now fail future packet preflight on the same cross-platform escape. |
| DP1B-23 | Public multipole helpers accepted fractional harmonic limits and silently truncated integer bin edges. | **CLOSED-BY-CODE v2B.0.7 / package 0.1.5** | All integer-valued public multipole arguments now reject floats and booleans without coercion; seven boundary regressions cover field limits and bin construction. |
| DP1B-24 | Receipt metadata comparison used Python equality, allowing JSON boolean/integer and integer/float type substitutions. | **CLOSED-BY-CODE v2B.0.8 / package 0.1.6** | Metadata validation now uses recursive type-strict JSON equality; four regressions cover scalar and nested substitutions. |
| DP1B-25 | Window equivalence allowed a broadcastable malformed `decouple_cell()` result to produce a false zero residual. | **CLOSED-BY-CODE v2B.0.8 / package 0.1.6** | The operator result must exactly match the finite `[4,n_band]` window result before subtraction; shape and non-finite regressions fail closed. |

---

## v2B.0.17 R1 — 2026-09-04 (exact PDF sha256 `0d0c92ab…4001fcac`, 8 pp)

Active legs Grok API / Gemini API / Claude INT Opus — all three **major-revisions**.
Full audit: `INT_v3/P1B_v2B.0.17_R1_TRUTH_AUDIT_2026-09-04.md`.
Board: `P1B_v2B.0.17_R1_BOARD_2026-09-04.md`.

**23 canonical · 21 genuinely-new REAL · 2 OPINION · 0 FALSIFIED · 0 re-flags.**

Canonical fingerprints registered for future re-flag matching:

- **C1** surrogate spin-0 estimator, not NaMaster; abstract unqualified — REAL, editorial.
- **C2** batch-1 rules amended post-unblinding; "pre-declared" overstated — REAL; **answered
  by pre-registered batch 2** (`4451b135` rules → `28efa21c` seal → `27300504` outputs →
  `974e2859` reveal → `b3347c53` manifest).
- **C3** seal not externally anchored / "independently verified" — REAL; ordering half
  answered by batch 2, external timestamp remains a SCIENCE item.
- **C4** R6 description ≠ implementation — REAL; answered by `RULES_v2_FROZEN.md`
  (batch 2: reference disjunct fired 5/5 on S4, cross-run 0/5).
- **C5** effective-multipole class missing — REAL; batch 2 added S6 and it **escaped 5/5**,
  no rule added afterwards. The paper must report the escape.
- **C6** n=3, bare percentages, no intervals — REAL; batch 2 gives 20/20 (lower 0.861) and
  0/5 (upper 0.451) plus the pre-declared independence caveat (effective n = 1 per class).
- **C7** no provenance/attestation related work — REAL; note `05b5940a` to be integrated.
- **C8** abstract overstates the threat-model guarantee — REAL, editorial.
- **C9** no uncertainty on the 0.270°/0.342°/0.000° recoveries — REAL, **not** answered by
  batch 2; the one item needing a fresh number.
- **C10, C12–C18, C20–C23** — REAL minors/trivia, all editorial.
- **C11** JORS length/scope opinion — **OPINION**, recorded not actioned.
- **C19** generalize the 54× cold/warm timing point — **OPINION** (enhancement).

**Standing rule for this lane:** batch 1's 12/12 and 0/3 are **rule-development numbers**
and must never again be reported as a blind result. Any future leg quoting them against a
post-v2B.0.18 PDF is a re-flag of C2 and is dispositioned by citing batch 2.

---

## v2B.0.18 R2 — 2026-09-04 (exact PDF sha256 `354d63b2…5074f88d2`, 12 pp)

Active legs Grok API **REJECT** / Gemini API **MINOR REVISIONS** / Claude INT Opus
**major-revisions**. Full audit: `INT_v3/P1B_v2B.0.18_R2_TRUTH_AUDIT_2026-09-04.md`.
Board: `INT_v3/P1B_v2B.0.18_R2_BOARD_2026-09-04.md`.

**27 canonical · 19 genuinely-new REAL · 3 OPINION · 2 FALSIFIED-in-part · 1 OUT-OF-SCOPE
disclosed · 2 SCIENCE.** No fabricated number found. The batch-2 pre-registration was
independently re-derived by the INT leg (sealed digest `c96b5bf1…` reproduced from the
revealed key; seal commit `28efa21c` contains no run output; verifier sha256 `6a9acd70…`)
— **the seal holds**, and R1's C2/C3-ordering half stays closed.

Canonical fingerprints registered for future re-flag matching (D-R2-nn = R2 canon):

- **D-R2-01** abstract CP bounds contradict the pre-declared independence caveat — REAL, editorial.
- **D-R2-02** "95% interval [0.501,0.807]" is the **90%** two-sided CP interval (95% = [0.472,0.827]);
  pooled 20/30 is an arm-design artefact — REAL, verified by recomputation.
- **D-R2-03** abstract calls the window layer spin-0 (module contracts a **spin-2** \[4,n_b,4,n_l\]
  workspace) and says "not run against PyMaster" while §§8/9/12 report PyMaster 2.6 — REAL.
- **D-R2-04** S1–S3 share one mechanism (R3+R4); S4's R6 cross-run disjunct 0/5, untested — REAL.
- **D-R2-05** pre-registration verifiable but no reader recipe; digest is over canonical JSON — REAL.
- **D-R2-06** "(S3, open)"/"(S2, in progress)" dangling tags colliding with class names — REAL.
- **D-R2-07** §2's 1.66 / 0.17 deviations untraceable to any committed artefact — REAL.
- **D-R2-08** "to our knowledge this is the first" primacy claim — REAL, delete.
- **D-R2-09** "negligible memory footprint" unquantified — REAL.
- **D-R2-10 … D-R2-19** self-referential §6 refs, 34-s seal window / discard-and-retry gap,
  OTS not checkable, pre-registration criterion uncited, R6 description correction absent
  from the pilot disclosure, missing attestation/SNARK related work, implicit coverage
  abstention, Table 2 caption, spaced slash, title-page version stamp (deferred to the
  submission build per directive G) — all REAL, editorial.
- **D-R2-20** JORS scope/adoption/length (Grok E3) — **OPINION**, re-flag of **C11**; venue fit is
  a decision, not an edit.
- **D-R2-21** "no value-level rule; S6 evades" — framing half **FALSIFIED** (abstract states the
  primitive is not a detector of value-level shortcuts; §11 lists S6 as a limitation); re-flag of
  **C5**; the rule itself is batch-3 science.
- **D-R2-22** "no precise Wigner-3j count" — **FALSIFIED**: `public2/contract.json::n_wigner3j = 137345`,
  enforced by R3. Only the workspace-tensor-DOI request survives as an enhancement.
- **D-R2-23** "threat model incomplete (harness edit)" — **OUT-OF-SCOPE, DISCLOSED**: the abstract
  states the unmodified-instrumented-harness model and §11 states metadata forgery is undetectable
  in principle.
- **D-R2-24 / D-R2-25** physical-units bias for the 1.66 deviation; "no figures" — **OPINION**.
- **D-R2-26 / D-R2-27** regenerate the 1.41e-18 scalar under a live PyMaster; upstream-3j-counter
  feasibility — **SCIENCE**.

**Standing rules added for this lane:**
1. Any future leg quoting the pooled 20/30 or a run-level Clopper–Pearson interval against a
   post-v2B.0.19 PDF is a re-flag of D-R2-01/D-R2-02 once the class-level presentation lands.
2. Any leg asserting the 3j count or mask contract is unpublished is a re-flag of D-R2-22 and is
   dispositioned by citing `public2/contract.json`.
3. Any leg asserting the paper hides the value-level/metadata escapes is a re-flag of D-R2-21/23
   and is dispositioned by citing the abstract's threat-model sentence and §11.
4. **Rounds STOP after v2B.0.19** (directive R2: R1+R2 are the two permitted consecutive rounds).
   The next P1B action is a science/venue decision — batch 3 (value-level rule + cross-run cache
   variant) and the PyMaster/OTS confirmations — not another sweep.
