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

## v2B.0.20 R3 — 2026-09-05 (exact PDF sha256 `cf57f485…5ee50cf`, 15 pp)

Active legs Grok API **REJECT** / Gemini API **MAJOR REVISIONS** / Claude INT Opus
**major-revisions**. Full audit: `INT_v3/P1B_v2B.0.20_R3_TRUTH_AUDIT_2026-09-05.md`.
Board: `INT_v3/P1B_v2B.0.20_R3_BOARD_2026-09-05.md`.
Receipt: `INT_v3/ROUND_2026-09-05-P1B-v2B.0.20-EXACTPDF-cf57f485-R3VERIFY/preflight_receipt.json`
(core `5af8959c…`, 9 rules, 0 findings).

**33 canonical · 27 genuinely-new REAL · 2 FALSIFIED · 3 OPINION · 1 OUT-OF-SCOPE disclosed.**
No fabricated number found. The genuinely-new count rose because the paper grew a batch
(12 → 15 pp): 22 of the 27 sit in text that did not exist at R2.

**The round's decisive finding — raised only by the INT leg, verified in code, then measured.**

- **D-R3-01** R7's spot rows are **prover-predictable**: `verify3.py:32–45` draws them as
  `sha256(mask_sha256 ‖ sha256(bandpowers) ‖ salt)` and `:57–58` feeds it two values the
  runner holds before publishing. `tex:573`'s "cannot be chosen by the runner" is the wrong
  property — unchoosable is not unpredictable — and an R7-aware S6 runner evades at **zero**
  marginal cost (it already built `M`). Fiat–Shamir applied to a prover-chosen commitment.
- **D-R3-02** R7 **fails open**: `verify3.py:48–56` returns `(False, nan)` on an absent or
  malformed `intermediates.pseudo_cl`, and no other rule requires the field — omitting it
  silently disables the only value-level rule.
- **Both confirmed empirically by batch 4**, pre-registered in `RULES_v4_FROZEN.md` (frozen
  before the scripts, the verifier-seed commitment and the seal, naming M1/M2/M3 as its
  reason). `public4/scorecard.json`: **S7** (R7-aware) `r7_fired 0/6, r7_residual_max 0.0,
  r8_fired 6/6`; **S8** (omit `pseudo_cl`) `r7_fired 0/6, r8_fired 6/6, suspect 6/6`;
  S1–S4/S6 R7+R8 6/6; S5 still escapes 0/6; honest FP **0/6**. R8's challenge randomness is
  a commit–reveal verifier seed (`efef74f2…` committed pre-seal, opened by `06e39b7a…` after
  every receipt digest), with a Bitcoin OTS blockhash declared as the drop-in upgrade.

**Canonical fingerprints registered for future re-flag matching (D-R3-nn = R3 canon):**

- **D-R3-03** batch-3 run-level Clopper–Pearson bounds (0.607 / 0.393 / 0.905) contradict
  batch 2's pre-declared refusal — REAL, a **recurrence of the D-R2-01/02 class in new text**,
  not a re-flag (`public3/scorecard.json::independence_caveat` contradicts its own bounds).
- **D-R3-04** "S1–S4b pool to **24/24**" — five arms × 6 = **30/30**; `0.05^(1/30)=0.905`
  proves n=30 was used. REAL, verified by recomputation; the slip runs against the authors.
- **D-R3-05 … D-R3-27** two-batch text, batch-3 trail + unpre-registered abort criterion,
  unarchived blind-test corpus, two dead cross-refs, "Both batches", title-page stamp +
  `p1b-` filenames, pymaster 3.0.1 vs 3.0, missing Freivalds/Fiat–Shamir, abstract
  value-level scope, uncomputed 6×10⁻¹⁶/"bias a fit", unquoted rule digests, §6 subsectioning,
  missing per-run tables, 500-word abstract, OTS verification mode, trust taxonomy third
  category, §9 single-angle σ, §8 placement, 0.1.7-has-no-R7, Rekor/S5, Q2 semantically-wrong
  case, mechanism recount, S4b source rule — all REAL, editorial (one recompute).
- **D-R3-28** Grok E1 "abstract has no independence caveat / quotes 0.473" — **FALSIFIED**:
  the caveat is in the abstract verbatim (`tex:179–182`, `:195`); `0.473` is not
  (only `tex:480`). Re-flag of D-R2-01, closed in v2B.0.19.
- **D-R3-29** Grok E3 "rewrite out all review-process language" — **OPINION**, half refused:
  the pilot demotion, disclosed post-hoc changes and preserved abort **are** the required
  disclosure; stripping them would water down. Only D-R3-10 is actionable.
- **D-R3-30** Grok E4 "retract the production-library claim" — **OUT-OF-SCOPE, disclosed**;
  premise FALSIFIED (`tex:171–174` states PyMaster is not installed and has no 3j counter).
- **D-R3-31** Grok E5 JORS length/venue — **OPINION** → escalated to a **scope decision**
  (converges with the Opus venue section). Re-flag of D-R2-20.
- **D-R3-32** Grok M3 "commit predates the revision date" — **FALSIFIED** (§12 states the
  release line is deliberately independent). Archive half survives as D-R3-07.
- **D-R3-33** Grok N2 Table 1 caption vs header — **OPINION**, no contradiction.

**Guardrail (not a finding): no priority claim exists in v2B.0.20.** `grep` for
`first|novel|to our knowledge` returns only non-priority uses; D-R2-08's sentence was
deleted in v2B.0.19 and has not returned. If N3 language is ever added it may claim **only**
"first such measurement *for pseudo-C_ℓ execution receipts*", and only alongside the
Freivalds / Fiat–Shamir / Klein–Roodman / in-toto-SLSA / OpenTimestamps citations.

**Standing rules added for this lane:**
1. Every statistics fix must be applied as a **rule for all future batches**, not as a patch
   to the current one — D-R3-03 and D-R3-08 are both v2B.0.19 fixes that were not carried
   forward into newly written batch-3 prose. Class-level counts only; no run-level intervals.
2. A leg asserting the abstract lacks the independence caveat is a re-flag of **D-R3-28**;
   disposition by citing `tex:179–182` and `:195`.
3. A leg asserting the detector is claimed to work for production NaMaster is a re-flag of
   **D-R3-30**; disposition by citing `tex:171–174` and §11.
4. A leg demanding removal of the pilot/abort/post-hoc-change disclosures is a re-flag of
   **D-R3-29** and is **refused** on integrity grounds; only the title-page stamp and the
   `p1b-` filenames (D-R3-10) are actionable.
5. **Rounds STOP after v2B.0.21** (directive R2: R2+R3 are the two permitted consecutive
   rounds). The next P1B actions are the v2B.0.21 closure bundle, the batch-4 write-up, the
   Zenodo deposit of the blind-test corpus, and the venue decision — not another sweep.

## v2B.0.23 R-CONFIRM — 2026-09-22 (exact PDF sha256 `c7cac6c9f16c…`, 16 pp)

Directive-R2 exact-version confirmation board, triggered by version drift since R3 (v2B.0.20
to v2B.0.23, batch-4/R8 integrated) with no board run on the literal current PDF. Active legs
Grok API (`grok-4.3`) **REJECT** / Gemini API (`gemini-3.1-pro-preview`) **REJECT** / Claude
opus verdict-blind sub-agent referee **MAJOR REVISIONS** (43 findings: 4 ESSENTIAL, 12 MAJOR,
17 MINOR, 10 NIT; every printed arithmetic and design-count claim independently re-verified
and found correct; Appendix Table 6 audited run-by-run against Table 3, exact match).
Raws: `INT_v3/ROUND_2026-09-22-P1B-v2B.0.23-EXACTPDF-CONFIRM/` (Claude leg) and
`peer-reviews/R-CONFIRM-2026-09-22_P1B_{Grok_brutal,Gemini_cosmology}.md` (API legs).

**This was NOT a clean wave.** Genuinely-new-real findings existed and most were closed in
v2B.0.24 (below); this round does not itself confirm the paper. Canonical fingerprints:

- **D-CONF-01** abstract's "not of forged metadata or of value-level shortcuts taken
  downstream of a declared intermediate" is stale against R7/R8 (Grok E3; Gemini implicit;
  Opus M9-part-3) -- REAL, recurrence of D-R3-13 (the v2B.0.20/R3 remedy was applied to
  Sec.11 but never to the abstract or the "Scope limits" paragraph) -- CLOSED v2B.0.24:
  abstract and Scope-limits both restated to match Sec.11's already-correct framing.
- **D-CONF-02** abstract's "All detection claims...never as run-level probability intervals"
  is contradicted by batch 1's own printed 0.779/0.632 (12/12, 0/3) run-level bounds and by
  p.7's "batches 1-4 uniformly...never a run-level Clopper-Pearson interval" (Grok E2/E5;
  Gemini E2; Opus M7) -- REAL -- CLOSED v2B.0.24: scoped to "frozen rule sets
  (batches 2-4)"; batch-1 pilot exception stated explicitly wherever the blanket claim
  appears (abstract, Sec.6, Sec.11).
- **D-CONF-03** the class-level Clopper-Pearson bound (0.473, 4/4) and the false-positive
  CP bounds (0.393 at 0/6; 0.779/0.632 at batch-1's 12/12, 0/3) have no defensible i.i.d.
  sampling model: honest replicates are deterministic replicas of one fixed reference
  configuration by construction, and the paper's own text two sentences later says the four
  structural classes reduce to two mechanisms (Opus E3, M6) -- REAL, genuinely new --
  CLOSED v2B.0.24: every CP-interval claim removed from batches 1-4; replaced with
  "expected by construction" / descriptive counts, with the reasoning stated once and
  cross-referenced.
- **D-CONF-04** batch 4/R8 (the abstract's headline result) carried no confusion table and
  no quantitative soundness bound, while batches 2-3 get both (Opus E4, M1) -- REAL,
  genuinely new -- PARTIALLY CLOSED v2B.0.24: Table 5 (batch-4 confusion table) added,
  transcribed verbatim from the already-committed `public4/scorecard.json`; the
  escape-probability bound f^K added with N~63, K=6 stated explicitly and a
  partial-operator adversary named as an open arm. Remaining open (not closed this round):
  a full commit-ordered audit trail for batch 4 (needs git-log archaeology) and a per-run
  appendix for all 54 batch-4 runs.
- **D-CONF-05** "Protocol, two batches." heading contradicted the same paragraph's own "run
  four times" sentence (Gemini M1; Opus m2, independently) -- REAL, genuinely new --
  CLOSED v2B.0.24: heading reworded to "Protocol, common to every batch."
- **D-CONF-06** Sec.11 Limitations L1-L3 used literal reviewer-response-style status tags
  ("(closed for the estimator; open for the hook)", "(partially closed)", "(closed)")
  rather than standard prose (Gemini E1) -- REAL, genuinely new, distinct from D-R3-29
  (D-R3-29 protects the disclosure content -- pilot/abort/post-hoc-change narration --
  which stays; this finding is about formatting those items as a checklist, which does not
  need to stay) -- CLOSED v2B.0.24: reworded into prose, no disclosed content removed; new
  L5 added disclosing R0/R1/R5 never fire in any of the 83+54 tabulated runs (Opus M8,
  REAL, genuinely new, closed by disclosure only, no new arm built).
- **D-CONF-07** Sigstore/Rekor was twice claimed to close the metadata-forgery gap; a
  transparency log witnesses publication time, not truth (Opus M3) -- REAL, genuinely new
  -- CLOSED v2B.0.24: both sentences corrected; SGX/TDX enclave attestation (already in the
  paper) identified as the actual closing mechanism, removing the self-contradiction with
  the paper's own correct OTS-limitation language (Opus m16, same fix).
- **D-CONF-08** "Fiat-Shamir-correct" mislabeled R8, and Sec.7's description of the
  Fiat-Shamir transform was the generic interactive-soundness condition, not Fiat-Shamir
  itself (Opus M2) -- REAL, genuinely new -- CLOSED v2B.0.24 in the batch-4 paragraph and
  Sec.7: R7 now described as the hash-derived (Fiat-Shamir-style) version that is
  prover-predictable; R8 as the interactive, verifier-committed challenge that restores
  soundness. Freivalds, Fiat-Shamir, and Klein-Roodman promoted from inline-only prose
  citations to numbered bibliography entries (Opus M4).
- **D-CONF-09** the archive (Zenodo, both software and manuscript, deposited July 21, 2026)
  predates batches 2-4 (sealed 2026-09-04) and this manuscript revision (2026-09-05) by
  6-7 weeks, so neither deposit contains the described work (Opus E2) -- REAL, genuinely
  new, recurrence/completion of D-R3-23 (D-R3-23 flagged only "0.1.7 contains no R7/R8" and
  required a disclosure sentence that was never actually added) -- PARTIALLY CLOSED
  v2B.0.24: Archive paragraph now discloses the gap explicitly. Re-archiving is a
  Houston-gated irreversible action, not performed by this lane -- remains open.
- **D-CONF-10** venue: Sec.13 Reuse Potential states the manuscript should be split, with
  the measurement (Sec.6) targeting ACM REP and a short metapaper targeting JORS/JOSS (Opus
  E1; Grok E4/M1 length opinion) -- RE-FLAG of D-R3-31 (already escalated as a standing
  scope decision converging with "the Opus venue section" at R3-time) -- NOT closed, not
  actionable by this lane: standing Houston-gated decision, unchanged.
- **D-CONF-11** spin-0 vs spin-2 labeling in Sec.2's motivating deviation number; missing
  disclosure that S4b is dropped in batch 4; "retained" used in two inconsistent senses;
  Sec.2 promised a "figure" the paper doesn't have; Author Contributions claimed funding
  acquisition while the Funding Statement says none; title-page macro-spacing bug
  swallowing the space before "("; opaque Author Contributions sentence; two SLSA/MLflow
  bibliography formatting gaps; three range-reference pairs rendering as the literal glitch
  "6-6" because Sec.6 has no numbered subsections; Table 4 (batch 3) floating after the
  batch-4 paragraph that supersedes it (Opus M12, m9, m8, m13, m15, n1, n9, n6, m17-partial,
  n5) -- all REAL, genuinely new, editorial-only -- CLOSED v2B.0.24.
- **D-CONF-12** deferred, genuinely-real, NOT closed this round (flagged for a future lane,
  not fabricated toward): missing ABFT/program-result-checking/randomness-beacon related
  work (Opus M5); freeze-commit vs. post-seal `verify.py` digest not published separately
  (Opus M10); S6/S7 cost-model motivation not quantified against a realistic MCMC call
  count (Opus M11); R6 cross-run order-dependence not analyzed (Opus m5); TOL's
  per-row-absolute-vs-global-norm sensitivity not characterized (Opus m6); no coverage
  tool configured (Opus m12); JORS structural template (Overview to Implementation to QC
  ordering, contributor-list/language sub-headings) not fully conformed (Opus m11); full
  Sec.6 numbered-subsection restructuring beyond the 3 literal "6-6" instances (Opus m17);
  batch-4 commit trail and per-run appendix (D-CONF-04 residual).
- **D-CONF-13** Grok's "0.473 is the CP bound for 20/20, not 4/4" (E5) and its restatement
  (N4) -- FALSIFIED: the printed sentence explicitly scoped the bound "on the class-level
  detection rate," consistent with 0.05^(1/4)=0.4729; superseded in any case by D-CONF-03's
  removal of the interval entirely.
- Grok E1 (untested on production NaMaster) = re-flag of D-R3-30/C1, disclosed
  out-of-scope, unchanged. Grok M3/M5 (round-off number only shown at N_side=64, not the
  N_side=512 production config) = re-flag of D-R2-26, SCIENCE-tier, deferred, unchanged --
  the cross-check is explicitly scoped and manifest-linked, not concealed. Grok N2 (R0-R8
  vocabulary) = re-flag of D-R3-29, refused (these are the paper's own load-bearing rule
  names, not review-log bookkeeping). Gemini N1 (EB parity assumption) = already disclosed
  at point of use (tex:289) and in Limitations -- no action. Gemini M2/M3 (memory/speedup
  citation, cosmological effect-size quantification) = OPINION/SCIENCE, honestly disclosed
  already, deferred.

**Directive-G v2B.0.24**: 16 to 18 pp, 4-pass compile 0 undef refs / 0 overfull, sha256
`eec6e6d4792b2d8ecb17b05a4ee97d4ec2b5bd1c1f579f41b92bfc8746dc5bbd` / md5
`b94a18fbfbdece5949999354d6833864`, mirrored byte-identical to `arxiv/`,
`arxiv/jors_submission/`, `site/public/papers/` (bare + `_v2B.0.24` + `_arxiv_v2B.0.24`),
`public/papers/` (same three), tarball `paper1b_namaster_proof_arxiv_v2B.0.24.tar.gz`
rebuilt from the single `.tex` and standalone-recompiled clean. Visual audit: title page,
both new/moved confusion tables, Sec.7, Sec.11 Limitations, and the Archive paragraph
rendered and inspected -- no overflow, no broken tables. **Round CLOSED, not CONFIRMED**:
real items existed and were substantially (not entirely) closed; D-CONF-04/09/10/12 remain
open by design (Houston-gated or explicitly deferred, not silently dropped). No further
board this round per the no-re-board rule.
