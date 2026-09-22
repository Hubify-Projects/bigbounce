# Verdict: MAJOR REVISIONS

**Manuscript:** "namaster-proof: Content-bound execution receipts as a shortcut detector for pseudo-C_ell computations"
**Author:** Houston Golden (Independent researcher, ORCID 0009-0008-5616-5994)
**Stamp read:** September 5, 2026 — manuscript revision v2B.0.23 (2026-09-05 12:00 PT)
**File refereed:** `arxiv/paper1b_namaster_proof.pdf`, 16 pages, MD5 `60d1a18ab3ea499398106d6a92bc8a35`, 579,465 bytes, pdfTeX-1.40.29, CreationDate 2026-09-05 02:25:48 PDT
**Venue as given to me:** Journal of Open Research Software (JORS), Software Metapaper
**Referee stance:** cold, verdict-blind, adversarial. No repository access used; every check below is against what is printed in the PDF.

---

## Summary

### What the paper says it contributes

The manuscript describes `namaster-proof` v0.1.7, a small pure-Python (NumPy-only) layer with three modules:

1. **`windows`** — exact contraction of a caller-supplied NaMaster spin-2 bandpower-window tensor `W^{ij}_{b\ell}` with a uniformly rotated [EE, EB, BE, BB] spectrum, using a three-component (constant, cos 4β, sin 4β) precontraction so that repeated evaluation over a rotation-angle grid is cheap while the full window operator is retained; plus fixed-grid angle recovery and an equivalence check against `couple_cell()` → `decouple_cell()`.
2. **`Multipoles`** — deterministic harmonic-cutoff and bandpower-edge contracts.
3. **`receipts`** — atomic JSON publication with a SHA-256-bound sidecar receipt, fail-closed verification of content bindings, and JSON-type-strict validation of caller-asserted metadata, exposed as `namaster-proof verify` / `validate` CLI commands.

Layered on top of the software description is a substantially larger research contribution (§6, pp. 4–9): a pre-registered, sealed blind test of whether receipts extended into a *measured execution trace* (Wigner-3j evaluation count, evaluated ℓ-grid, coupling-matrix shape/support/hash, code hash, mask hash, wall time) can let a referee detect that an expensive pseudo-C_ell computation was silently shortcut. Four batches are reported:

- **Batch 1** (18 runs, 6 arms × 3) — explicitly relabelled a pilot/rule-development round because two rules were changed after outcomes were seen.
- **Batch 2** (35 runs, 7 arms × 5, rules R0–R6 frozen) — the primary structural result: honest 0/5 flagged; S1 (operator skipped), S2 (operator truncated), S3 (grid reduced), S4 (cache substituted) all 5/5; S5 (metadata forgery) escapes 5/5 as pre-declared; S6 (effective multipole) escapes 5/5 with no pre-declared outcome.
- **Batch 3** (48 runs, 8 arms × 6, adds value-level rule R7 and arms S4b, extended S5) — R7 catches S6 6/6 by recomputing K = 6 receipt-derived "spot rows" of the coupling operator and testing `|M C − p|` against TOL = 1e-6·‖p‖₂; the paper itself immediately discloses that R7's row draw is prover-predictable and that R7 fails open when the declared intermediate is omitted.
- **Batch 4** (54 runs, 9 arms × 6, adds post-commitment challenge rule R8 and adversary arms S7 = R7-aware, S8 = omit `pseudo_cl`) — R8 draws 32 random bytes σ, publishes only sha256(σ) before any run, binds each receipt as D, and reveals σ only after every D is committed; R8 catches S7 6/6 and S8 6/6 where R7 fires 0/6, with 0/6 honest false positives. Metadata forgery (S5) still escapes across all four batches and is stated as the primitive's limit.

Separately, §6 (pp. 9–10) reports a non-blind cross-check of the in-house spin-0 MASTER estimator against PyMaster 3.0 at N_side = 64, ℓ_max = 95, agreeing to 4.25e-13 (coupling matrix, 94×94) and 1.54e-12 (decoupled bandpowers) maximum relative difference.

### Referee's assessment of the contribution

The honest core of this manuscript is genuinely unusual and, in places, exemplary. The disclosure discipline is far above the norm: the author relabels batch 1 as a pilot rather than headlining its better-looking numbers; discloses that R7's challenge is prover-predictable *and then builds the adversary that exploits it*; discloses an aborted batch-3 attempt including a seeding defect that invalidated it; discloses that no abort criterion had been pre-registered; discloses that the wall-clock rule was removed only after it fired on honest runs; corrects an earlier draft's "24/24" to "30/30" in print; and states repeatedly that the seal establishes ordering, not an external witness, because the same party sealed, ran, and unsealed. Every arithmetic claim I could check independently is correct (details in Findings). The idea of a receipt field whose value is a *measured consequence of the numerical path* — a Wigner-3j counter — rather than an administrative assertion by the harness is a real and well-articulated delta against in-toto/SLSA/ReproZip/MLflow, and §7 argues it carefully.

But three problems are, in my judgement, disqualifying in their present form, and a dozen more are serious.

First, **this is not a JORS paper, and the manuscript says so itself**. §13 (p. 15) states that the manuscript "targets a venue for the measurement (e.g. ACM REP)" and that a "short software-description submission for the package itself (e.g. JOSS or JORS)" is a *separate* paper that should cross-cite it. I am being asked to referee, as a JORS Software Metapaper, a document whose own Reuse Potential section declares that JORS should receive a different, shorter manuscript. Roughly six of sixteen pages are a research measurement with a pre-registration, a confusion matrix, an adversary model, and an inferential statistic — material a metapaper is not the vehicle for.

Second, **the archive does not contain the work being described**. Both Zenodo deposits are dated July 21, 2026, and the software record is pinned to commit `0a587b58`. The batch-2 OpenTimestamps submission is dated 2026-09-04 19:31; the PyMaster cross-check manifest is named `...-2026-09-05.json`; the manuscript itself is stamped 2026-09-05. Batches 2, 3 and 4 — including `RULES_v3_FROZEN.md`, `RULES_v4_FROZEN.md`, `variants3.py`, `variants4.py`, `verify4.py`, `verifier_seed4.py`, and all sealed material — postdate the archive by six to seven weeks and therefore cannot be in it. The only stated location for the paper's headline artifacts is a mutable GitHub `main` branch.

Third, **the zero-false-positive result is a mathematical identity, not a measurement**. The paper states, correctly, that "rules R1–R5 compare seed-independent quantities against a fixed contract" (p. 5). Honest runs differ from one another only in the random input map. Therefore every honest run reproduces the reference contract's code hash, ℓ-grid, 3j count, operator shape/support and mask hash *by construction*, and R1–R5 cannot fire on an honest run under any seed. "Honest 0/5" and "honest 0/6" are entailments of the design, and the paper nonetheless converts one of them into a Clopper–Pearson upper bound of 0.393 (p. 8). The author applies the independence caveat scrupulously to the *detection* side and then does not apply the identical logic to the *false-positive* side. No honest-but-legitimately-different run — a different ℓ_max, a different mask, a refactored module, a different NumPy/BLAS build, a different platform — is ever tested, and R1, R2 and R5 would fire on every one of them. The detector as measured distinguishes "byte-identical configuration to one reference run" from "anything else", which is a much weaker and much less interesting claim than "shortcut vs. honest".

Beyond these, R8 — the paper's newest and most heavily claimed result, and the one the abstract uses to say R7's two gaps are "fixed" — is the *least* evidenced result in the paper: no confusion table (batches 2 and 3 each get one), no commit-ordered audit trail (batches 2 and 3 each get one), no `seal_verified: true` statement (batches 2 and 3 each get one), no quoted pre-declared success criterion (batch 2 gets one), no per-run appendix (batch 2 gets one), and no OpenTimestamps anchor (batches 1–3 get one). And R8's soundness is asserted qualitatively but never bounded: with K = 6 challenged rows out of roughly 63, an adversary who computes 90% of the operator honestly and shortcuts the remaining 10% escapes with probability ≈ 0.9⁶ ≈ 0.53. That adversary is not built, not discussed, and not listed as a limitation.

There is also a conceptual error repeated three times: Sigstore/Rekor is described as supplying "exactly the externally witnessed anchor identified above as the missing ingredient for the metadata-forgery class" (§7, p. 10). It does not. A transparency log witnesses that a statement was signed at a time; it says nothing about whether the statement is true. An analyst who forges a trace signs the forgery and obtains a perfectly valid Rekor entry. The metadata-forgery gap is closed by a witnessed or attested *execution environment* (the paper's own SGX/TDX paragraph, or a third-party rerun) — not by a log.

I want to be explicit that none of this reads to me as dishonest. It reads as a careful author who has written two papers on top of each other and let the framing of the weaker halves drift out of sync with the stronger halves. The remedies are mostly editorial and structural rather than scientific. I therefore recommend **MAJOR REVISIONS**, with the explicit note that if the split (E1) and the archive (E2) are not resolved, the correct outcome at this venue is reject-and-resubmit-elsewhere rather than acceptance.

---

## Findings

### ESSENTIAL

**E1 — ESSENTIAL — Venue and scope: the manuscript disqualifies itself from JORS in its own text.**
*Location: §13 Reuse Potential, p. 15; §6 Blind Shortcut-Detection Test, pp. 4–9.*
Quote: "Accordingly this manuscript targets a venue for the measurement (e.g. ACM REP) with arXiv astro-ph.IM as primary category and cs.SE as secondary, alongside a short software-description submission for the package itself (e.g. JOSS or JORS) that cross-cites the measurement."
This is a direct statement that the document in front of me is not the one intended for JORS. Independently of the author's stated plan, the content confirms it: the blind-test measurement (§6) spans pp. 4–9 of a 16-page paper — roughly 40% of the body, plus Tables 2, 3, 4, and 6 and the whole of the Appendix — and constitutes new research results with a pre-registration, a sealed protocol, an adversary model, a confusion matrix, and inferential statistics. A JORS Software Metapaper is a description of released software and its reuse potential, not a venue for a new empirical result; the measurement would also be under-refereed here, since a JORS referee is not selected for competence in commit–reveal protocols or randomized verification.
Remedy: split. Submit the measurement (§§6, 7, the batch tables, the Appendix) to ACM REP or equivalent. Submit to JORS a short metapaper covering §§1–5, 8, 9, 11–13 that *cites* the measurement for the shortcut-detection claims and does not restate them. If the author prefers to keep one paper, it should not be at JORS.

**E2 — ESSENTIAL — The archive does not contain the described work; the Software Location requirement is unmet.**
*Location: §12 Availability → Archive, p. 14; cross-checked against §6 pp. 6, 9 and §12 p. 15.*
Quote: "the commit-pinned source tree (packages/namaster-proof at repository commit 0a587b58…), together with its license, citation metadata, and checksums, is published on Zenodo under doi:10.5281/zenodo.21481753 (deposited July 21, 2026). The manuscript itself … is separately archived under doi:10.5281/zenodo.21481842 (CC-BY-4.0, deposited July 21, 2026)."
Both deposits predate the work they are offered as the archive for:
- The batch-2 OpenTimestamps proof "was submitted 2026-09-04 19:31" (p. 6).
- The PyMaster cross-check manifest is `p1b-pymaster-crosscheck-2026-09-05.json` (p. 15).
- The manuscript is stamped September 5, 2026 (title page), so the July 21 manuscript deposit is demonstrably not this manuscript.
Consequently `RULES_v3_FROZEN.md`, `RULES_v4_FROZEN.md`, `variants3.py`, `variants4.py`, `seal3.py`, `seal4.py`, `verify4.py`, `reveal3.py`, `reveal4.py`, `verifier_seed4.py`, `sealed3/`, `sealed4/`, `public3_aborted/`, all four experiment manifests, and the cross-check script cannot be in the archived snapshot. The only location given for them is `https://github.com/.../tree/main/...` — a mutable branch that provides no persistent identifier and no immutability guarantee. For a paper whose entire thesis is that artifacts must be bound to the process that produced them, archiving the artifacts is not optional.
Remedy: mint a new Zenodo deposit containing the current package *and* the complete `pipelines/namaster_proof/blind_test/` tree and all four manifests; cite it by DOI with its deposit date; re-archive the manuscript at its current revision.

**E3 — ESSENTIAL — The zero-false-positive result is true by construction and is then given a confidence interval.**
*Location: §6 "Result (batch 2, primary)" and "Independence caveat", pp. 5–6; §6 "R7 catches S6, bounded three ways", p. 8; Tables 3 and 4.*
Quotes: "rules R1–R5 compare seed-independent quantities against a fixed contract, so the five replicates within an arm are seed-varied executions of one deterministic variant" (p. 5); "(2) 0/6 honest false positives bounds the false-positive rate above by 0.393; six runs cannot establish a small rate" (p. 8).
The author's own premise entails the conclusion. Honest runs are generated by the same code, on the same mask, on the same ℓ-grid, so their code hash, evaluated ℓ-list, 3j count, operator shape/support and mask hash are identical to the reference contract with probability exactly 1. R1–R5 therefore *cannot* fire on an honest run under any seed. "Honest 0/5" (Table 3) and "honest 0/6" (Table 4) are restatements of the design, not observations, and applying Clopper–Pearson to them is not meaningful — the upper bound of 0.393 is arithmetically correct (1 − 0.05^(1/6) = 0.3930) but models a sampling process that does not exist. The author applies exactly this reasoning to the detection side and then declines to apply it to the false-positive side; the asymmetry needs to go.
More importantly, the *interesting* false-positive question is never asked. Real honest analyses legitimately differ from a reference run: a different ℓ_max for a different science case, an updated apodization, a refactor that changes the module hash without changing the mathematics, a different NumPy/BLAS/platform, a rerun after a dependency bump. R1 fires on every honest refactor, R2 on every honest ℓ-grid change, R5 on every honest mask change. Under the design as measured, the rule set detects "this run's configuration is not byte-identical to the contract" — which is nearly a tautology — and the mapping from that to "this run took a shortcut" is entirely carried by the assumption that the analyst declared the right contract in the first place.
Remedy: (a) delete the Clopper–Pearson FP bound and state that 0 FPs on R1–R5 is deterministic; (b) add an honest-variation arm set — same science, legitimately different ℓ_max/mask/platform/module revision — and report how many rules fire, which will be the paper's most informative number; (c) reframe the contribution as *contract conformance detection* and state explicitly what operational discipline (who publishes the contract, and when) makes conformance equivalent to honesty.

**E4 — ESSENTIAL — Batch 4 / R8, the paper's headline new result, carries the least evidence of any batch.**
*Location: §6 "Batch 4: a post-commitment verifier challenge (R8)", pp. 7–8; compare §6 pp. 5–7 and §12 p. 15; Abstract p. 1.*
The abstract promotes R8 as the fix for both of R7's disclosed gaps ("A post-commitment verifier challenge (R8) fixes both gaps … and catches both the rule-aware evasion and the omission 6/6 with zero honest false positives"). Yet, measured against the evidential standard the author sets for batches 2 and 3, batch 4 is missing:
- **No confusion table.** Batch 2 gets Table 3; batch 3 gets Table 4; batch 4 gets a prose sentence. Nine arms × 6 = 54 runs are summarised in one line.
- **No commit-ordered audit trail.** Batch 2: `4451b135 → 28efa21c → 27300504 → 974e2859 → b3347c53`. Batch 3: a ten-commit chain `dcf96696 → … → bf7d26e3`. Batch 4: only "seal dbe6a713…" and "RULES_v4_FROZEN.md, sha256 a59caaf8…". The reader cannot check that the R8 rules were frozen before the σ commitment, that the σ commitment preceded the seal, or that the seal preceded any run output — which is the entire soundness argument for R8.
- **No `seal_verified: true`.** Stated for batch 2 ("seal_verified: true") and batch 3 ("seal abfe2793…, seal_verified: true"), absent for batch 4.
- **No quoted pre-declared success criterion.** Batch 2's is named and quoted (`BATCH2_PREREGISTRATION.md`, and the criterion itself on pp. 4–5). Batch 3's pre-registration commit is named (`d03fe376`) but its criterion is never stated. Batch 4 has neither.
- **No per-run verdict appendix.** The Appendix (p. 15, Table 6) covers batch 2 only.
- **No external anchor.** L2 (p. 12) reports OTS status for batches 1, 2 and 3; batch 4 is not mentioned, and neither is a timestamp on sha256(σ) — which, given that OTS is already in the author's toolkit and that σ's commitment time is the load-bearing fact for R8, is a conspicuous omission.
Remedy: give batch 4 a confusion table with the same columns as Tables 3 and 4 (including which of R0–R8 fired per arm), the full commit-ordered trail including the σ-commitment commit, `seal_verified`, the pre-declared criterion, a per-run appendix, and an OTS stamp on both the seal digest and sha256(σ).

---

### MAJOR

**M1 — MAJOR — R8's soundness is asserted, never bounded; the obvious partial-row adversary is neither built nor discussed.**
*Location: §6 "Batch 4", p. 7.*
Quote: "An honest run's residual is −10−12 C on every row at once, so it passes any challenge set without knowing σ; a shortcut with p ≠ M C on generic rows escapes only if all K post-commitment rows land in its agreeing set."
That last clause is correct and is precisely where a quantitative bound belongs, and none is given. With K = 6 challenged rows and an adversary that computes a fraction f of the operator's rows honestly (and shortcuts the rest), escape probability is ≈ f^K:

| f (fraction computed honestly) | build cost saved | escape probability f⁶ |
|---|---|---|
| 0.50 | 50% | 0.016 |
| 0.80 | 20% | 0.262 |
| 0.90 | 10% | 0.531 |
| 0.95 | 5% | 0.735 |

So R8 with K = 6 is only meaningful against adversaries who corrupt a large fraction of rows. The paper's own arms happen to be of that kind (S6 corrupts essentially every row, residuals 7.5e-2–1.5e-1), which is why the measured detection is 6/6 — but the *protocol-level* claim "made sound by a Fiat–Shamir-correct post-commitment challenge" (p. 8) is a claim about all adversaries. A "partial-operator" arm S9 that honestly builds 90% of rows is the natural continuation of the paper's own commendable build-the-predicted-adversary methodology, and it would presumably escape.
Also missing: the number of rows N is never stated (it must be inferred from "∼9% of a full build" for 6 rows, i.e. N ≈ 63); K = 6 is never justified; and whether the K rows are drawn with or without replacement is unspecified, which changes the bound.
Remedy: state N; derive the escape bound as a function of (f, K, N); choose K from a target soundness error and say what it is; either build the partial-operator adversary or list it as an explicit open class alongside S5.

**M2 — MAJOR — "Fiat–Shamir-correct" is a misnomer; R8 is the interactive predecessor of Fiat–Shamir, not an application of it, and §7's description of the transform is garbled.**
*Location: §6 p. 8 ("a row-sampled Freivalds test (§7) made sound by a Fiat–Shamir-correct post-commitment challenge"); §7 pp. 10–11.*
Quote (§7): "the Fiat–Shamir transform, which makes a randomized challenge sound only when the challenge is drawn after the prover's commitment rather than chosen or predictable by the prover".
That is not what Fiat–Shamir does. Fiat–Shamir removes interaction by replacing a verifier-drawn challenge with a hash of the prover's commitment, under a random-oracle assumption. The property the paper is invoking — the challenge must not be predictable to the prover before it commits — is the generic soundness condition of *interactive* proof systems, which Fiat–Shamir tries to preserve, not to establish. Concretely: **R7 is the Fiat–Shamir version** (challenge derived by hashing), and it is broken; **R8 abandons Fiat–Shamir** and returns to an interactive verifier-drawn challenge with a commitment. Calling R8 "Fiat–Shamir-correct" inverts the relationship.
Worse, the specific reason R7 fails has a name and a literature. R7 draws rows from `sha256(mask hash ‖ sha256(bandpowers))` — a hash of the *inputs* that omits the prover's actual claim `p`. That is the textbook "weak Fiat–Shamir" failure: the challenge is not bound to the full statement, so the prover computes the challenge first and crafts its claim second. This exact pitfall is documented (Bernhard, Pereira & Warinschi, "How not to prove yourself: pitfalls of the Fiat–Shamir heuristic", ASIACRYPT 2012; and the widely-reported 2023 "Frozen Heart" class of deployed instances). Citing it would *strengthen* the paper — it would show that R7's gap was a known trap rather than an idiosyncratic slip, and it would justify R8's design properly.
Note also that even a *strong* Fiat–Shamir fix (hashing `p` into the challenge, as R8's D in fact does) would not suffice here, because the prover can grind: with 6 precomputed exact rows out of ~63, each candidate perturbation of `p` hits the precomputed set with probability ≈ (6/63)⁶ ≈ 7e-7, so ~10⁷ trials suffice. This is a good argument *for* R8's verifier-drawn σ and should be in the paper; as written, the paper gives no reason why the hash-based route could not simply have been repaired.
Remedy: rewrite the R7/R8 framing in the correct vocabulary (commit-then-challenge / interactive vs. non-interactive; weak vs. strong Fiat–Shamir); add the grinding argument; cite the weak-FS literature.

**M3 — MAJOR — Sigstore/Rekor is repeatedly and incorrectly claimed to close the metadata-forgery gap.**
*Location: §7, p. 10 (twice); §6 "Scope limits", p. 9.*
Quotes: "Sigstore [7] with its Rekor transparency log supplies exactly the externally witnessed anchor identified above as the missing ingredient for the metadata-forgery class"; "anchoring such a predicate in a transparency log would close the metadata-forgery gap using existing infrastructure"; "The S5 metadata-forgery escape is structural, not a bug: closing it needs the same external anchor, or a witnessed execution environment, signed build/execution logs, or a third-party rerun."
A transparency log establishes that a given signed statement existed at a given time and has not been altered since. It establishes nothing about the statement's truth. The S5 adversary fabricates a well-formed honest trace at write time; signing that trace and logging it in Rekor yields a valid, verifiable, tamper-evident entry containing a lie. The same objection applies to the paper's OpenTimestamps anchors, and — to the author's credit — the paper states it correctly *for OTS* on p. 6 ("establishes that the digest existed before a given Bitcoin block time, not an external witness to the batch-2 execution itself") and p. 9 ("This is a genuine third-party time witness; it still does not witness execution"). The reasoning applied correctly to OTS is then abandoned for Sigstore.
What actually closes S5 is in the paper already: the SGX/TDX paragraph. An instrumented harness executing inside an attested enclave *does* prevent the analyst from fabricating the trace, because the attestation binds the measured harness binary and the harness, not the analyst, emits the trace.
Remedy: correct all three sentences. Say that transparency logs close backdating and post-hoc substitution, not fabrication-at-write-time; identify attested execution (or third-party rerun) as the mechanism that closes S5; and amend the list on p. 9 so that "the same external anchor" is not presented as sufficient.

**M4 — MAJOR — Three load-bearing references are given only inline and are absent from the bibliography.**
*Location: §7, pp. 10–11; bibliography [1]–[14], pp. 15–16.*
Freivalds (IFIP Congress 1977, pp. 839–842), Fiat & Shamir (CRYPTO '86, LNCS 263, pp. 186–194), and Klein & Roodman (Ann. Rev. Nucl. Part. Sci. 55, 141 (2005)) appear as parenthetical prose only. The bibliographic details are correct — I checked all three — but these are not incidental mentions: R7/R8's entire correctness argument is "Freivalds + commit-then-challenge", and the blind protocol's entire methodological justification is Klein & Roodman. Uncited-in-bibliography references are not indexed, not DOI-resolved, not counted, and not discoverable, and most journals (JORS included) will reject the manuscript at copy-edit for this alone.
Remedy: promote all three to numbered references with DOIs where available.

**M5 — MAJOR — Missing related work: the program-result-checking and algorithm-based-fault-tolerance literatures are the direct ancestors of R7/R8 and are absent.**
*Location: §7 Relation to Provenance and Attestation Tooling, pp. 10–11.*
§7 is good on the provenance/attestation side (in-toto, SLSA, Sigstore, ReproZip, Snakemake, Nextflow, RO-Crate, MLflow, SGX, SNARKs). It is silent on the literature that R7/R8 actually belongs to:
- **Blum & Kannan, "Designing programs that check their work" (JACM 42(1), 269–291, 1995)** and the program-checking/self-testing line (Blum, Luby, Rubinfeld). This is precisely the paradigm the paper reinvents: a cheap checker that verifies a program's output on the instance at hand without recomputing it.
- **Huang & Abraham, "Algorithm-Based Fault Tolerance for Matrix Operations" (IEEE Trans. Comput. C-33(6), 518–528, 1984)** and the ABFT line. Checksum/row-verification of matrix products is the standard technique here, and it is routinely applied at HPC scale to exactly the kind of `M C = p` product R7/R8 checks — including with *weighted* checksums that give far better detection per unit cost than uniform row sampling.
- **Bernhard, Pereira & Warinschi (ASIACRYPT 2012)** — see M2.
- **Public randomness beacons** — the abstract explicitly contrasts R8 with "a public randomness beacon" (p. 1) and §6 does the same, but no beacon is cited. NIST Randomness Beacon and drand / League of Entropy are the obvious candidates, and adopting one would remove the reliance on "the committing verifier's honesty" that the abstract concedes.
- **Reproducibility frameworks in astronomy** — Maneage (Akhlaghi et al., *Computing in Science & Engineering* 23(3), 2021) is the closest prior art in this field and is missing.
- **Artifact evaluation** — since the author targets ACM REP, the ACM artifact-badging literature (e.g. Krishnamurthi & Vitek) is the community context.
Remedy: add a paragraph positioning R7/R8 as a sampled ABFT/result-checker specialized to pseudo-C_ell, and cite a beacon. The ABFT comparison in particular is likely to improve the method (weighted checksums), not merely the citation list.

**M6 — MAJOR — The class-level Clopper–Pearson bound has no defensible sampling model and is refuted two sentences later by the author.**
*Location: §6 "Result (batch 2, primary)" and "Independence caveat", pp. 5–6.*
Quotes: "4/4 structural classes detected, 20/20 runs (one-sided 95% Clopper–Pearson lower bound 0.473 on the class-level detection rate, the only i.i.d. unit available …)"; then, on p. 6: "S1–S3 are all caught by the same trace-mismatch mechanism (rules R3 and R4); S4 is caught by R6. The evidence is therefore two deterministic mechanisms across four classes, not four independent mechanisms."
The arithmetic is right (0.05^(1/4) = 0.4729). The inference is not. A Clopper–Pearson interval requires n i.i.d. Bernoulli draws from a population. The four "classes" are four shortcut variants the author chose and wrote; they are not a random sample from any population of shortcuts, no such population is defined, and the paper states in the next breath that they reduce to two mechanisms — so even the author's own count of independent units is 2, not 4. Calling four self-selected classes "the only i.i.d. unit available" does not make them i.i.d.; scarcity of units is not evidence of exchangeability. The number 0.473 has no interpretation and invites exactly the misreading ("the detector works at least 47% of the time") that the surrounding careful prose is trying to prevent.
Remedy: delete the interval. Report "4 of 4 designed structural classes detected, 20 of 20 replicates, by 2 distinct mechanisms" and stop. The paper is stronger without a number that cannot be defended.

**M7 — MAJOR — The blanket claim that no run-level probability intervals are reported is contradicted three times in the same paper.**
*Location: Abstract p. 1; §6 batch-3 paragraph p. 7; §11 p. 12 — against §6 p. 6 and §6 p. 8.*
Claims: "All detection claims are reported as class-level counts, never as run-level probability intervals (§6)" (Abstract); "batches 1–4 uniformly report class-level detection counts and never a run-level Clopper–Pearson interval" (p. 7); "All detection rates in this paper (R1–R7) are class-level, not per-run, probabilities (§6)" (§11, p. 12).
Contradicted by:
- p. 6: "batch 1's own confusion counts (12/12 on S1–S4, **one-sided 95% lower bound 0.779**; 0/3 honest false positives, **upper bound 0.632**)". Both are run-level Clopper–Pearson intervals over 12 and 3 *runs* respectively. (Arithmetic checks: 0.05^(1/12) = 0.7791; 1 − 0.05^(1/3) = 0.6316.)
- p. 8: "0/6 honest false positives **bounds the false-positive rate above by 0.393**" — a run-level interval over 6 runs. (1 − 0.05^(1/6) = 0.3930.)
The p. 6 case is partially mitigated by the "rule-fitting numbers, not a blind-test result … not headlined" framing, and the p. 8 case is about false positives rather than detection, so the §11 wording ("detection rates") is technically survivable. The abstract's "All detection claims … never as run-level probability intervals" and p. 7's "batches 1–4 uniformly … never a run-level Clopper–Pearson interval" are not: the latter is a statement about the whole paper and is false of pages 6 and 8. A referee who spots this loses confidence in the other blanket assurances, which is a disproportionate cost for a fixable inconsistency.
Remedy: remove the run-level intervals entirely (see E3, M6) and keep the blanket claim, or weaken the blanket claim to match what is printed. The first is better.

**M8 — MAJOR — R0, R1 and R5 never fire in any tabulated run across 83 runs, and this is not disclosed, while a comparable gap (R6's cross-run disjunct) is disclosed.**
*Location: Table 3 p. 5; Table 4 p. 8; §11 L3 p. 12.*
Across the two per-arm tables (35 + 48 = 83 runs), the "Rule(s) fired" column contains only R2, R3, R4, R6 and R7. R0 (receipt verification failure), R1 (code hash mismatch) and R5 (mask hash mismatch) fire nowhere. The author is scrupulous about exactly this kind of coverage gap elsewhere — L3 (p. 12) is devoted to the fact that R6's cross-run disjunct fired 0/5 in batch 2 and was therefore untested, and batch 3's S4b arm was built specifically to exercise it. The same standard is not applied to R0/R1/R5, which are 3 of the 7 frozen rules and are entirely unexercised.
There is a sharper problem underneath. The trace records "sha256 of the compute module actually imported" (p. 4) and R1 fires when "code.sha256 disagrees with the contract". Arms S1, S2, S3, S6, S7 and S8 all alter the computation. If the alteration lives in the imported compute module, R1 should fire on every one of them, and Tables 3 and 4 say it does not. So either (a) the variants are injected without changing the hashed module (monkeypatching, a flag, a sibling module not covered by the hash) — in which case R1's coverage of the trace is narrower than the reader will assume, and the "unmodified-instrumented-harness" threat model is doing all the work; or (b) something in the accounting does not add up. Either way the paper must say which, because R1 is the rule that would otherwise make the whole exercise circular: if any change to the computation changes the code hash, shortcut detection reduces to "the code is not the declared code", and R2/R3/R4 are redundant.
Remedy: state explicitly how variants are injected relative to the hashed module; add an L5 limitation noting R0/R1/R5 are untested in all four batches; ideally add arms that exercise them (a corrupted receipt; a modified module; a substituted mask).

**M9 — MAJOR — The "Scope limits" paragraph is stale relative to batches 3–4 and its closing claim now contradicts the paper's own results.**
*Location: §6 "Scope limits", p. 9; Abstract p. 1.*
Three distinct staleness defects in one paragraph:
1. "The estimator exercised in **both batches** is this repository's own spin-0 MASTER implementation" — there are four batches.
2. "the sealed digest of each batch has been submitted to the OpenTimestamps Bitcoin calendar (`blind_test/public{,2}/sealed_digest.json.ots`)" — the brace expansion covers batches 1 and 2 only; batch 3's path is not given although its stamp is said to be pending, and batch 4 is not mentioned at all, contradicting "each batch".
3. Most seriously: "the tested claim is: receipts of this kind are a detector of structural shortcuts in instrumented steps, not of forged metadata **and not of value-level shortcuts taken downstream of a declared intermediate**." Batches 3 and 4 demonstrate the opposite: R7 catches S6 6/6 (Table 4) and R8 catches the rule-aware S7 and the omission S8 6/6 each (p. 8) — all value-level shortcuts downstream of a declared intermediate. §11 (p. 12) states the corrected position ("via R7/R8 …, of both rule-unaware and rule-aware value-level shortcuts and of omitted declared intermediates"). The **abstract carries the stale sentence too** ("not of forged metadata or of value-level shortcuts taken downstream of a declared intermediate"), so the paper's most-read sentence understates its own best result while §11 overstates it relative to §6. A reader cannot tell which is the author's position.
Remedy: rewrite the Scope-limits paragraph and the abstract's closing characterization against the four-batch state, and make abstract / §6 / §11 say the same thing. The correct statement is roughly: a detector of structural shortcuts, and — for value-level shortcuts — of those that leave the declared intermediate inconsistent with the operator, but not of fabrication of that intermediate.

**M10 — MAJOR — The frozen-rules digest pins the post-edit verifier, not the frozen state, and the rules file itself was edited post hoc; the "no rule edited" sentence is stronger than the evidence.**
*Location: §6 pp. 4, 6.*
Quotes: "the rule set was frozen and committed alone, in its own commit, before the seal commitment existed in the repository, and **no rule was added, removed, or edited between that freeze and the reveal**" (p. 4, emphasised in the original); versus "verify.py was edited once between freeze and seal (28efa21c) for non-rule plumbing (a one-line output-directory argument; the judge() function and the R6 block are unchanged), and its post-seal sha256 6a9acd70… is the digest pinned in public2/frozen_rules_digest.json" and "The R6 rule's stated behavior was corrected in RULES_v2_FROZEN.md as a documentation-only change … disclosed here as a third post-hoc change" (p. 6).
Two problems:
- The pinned digest `6a9acd70…` is the *post-edit* hash. It therefore attests the state of the verifier at seal time, not at freeze time. A reader who wants to confirm that the edit was confined to "a one-line output-directory argument" has nothing to diff against, because the freeze-commit digest of `verify.py` is never published. The author's assertion that `judge()` and the R6 block are unchanged is exactly the kind of claim this paper's own thesis says should not be taken on assertion.
- The emphasised sentence on p. 4 says no rule was edited between freeze and reveal; p. 6 says the rules *document* was edited post hoc and that S4's 5/5 "rests on the reference disjunct that description clarifies". These are reconcilable (code vs. documentation) but the reconciliation is two pages away from the emphasised claim, and the thing edited was the description of the rule whose behaviour the primary result depends on.
Remedy: publish the freeze-commit sha256 of `verify.py` alongside the post-seal one, and the diff; qualify the p. 4 sentence to "no rule *code* was added, removed, or edited" with a forward pointer to the p. 6 disclosure.

**M11 — MAJOR — S6/S7's cost model is never stated, and by the paper's own description these arms save nothing at the expensive step — undermining the threat model that motivates R7/R8.**
*Location: §6 p. 6 ("S6: the effective-multipole class escaped"); §6 p. 4 (threat model); §2 p. 2.*
Quote: "S6 builds the full mode-coupling operator genuinely — the real ℓ-grid, the real 3j-evaluation count, the real operator shape and support all match the contract — and takes the shortcut downstream, in the band evaluation."
The paper's motivating threat is a referee "who cannot afford to re-run an expensive exact computation" facing an analyst who "silently shortcut" it (p. 4). But in MASTER the expense is building M (the Wigner-3j sums), and S6 builds M in full. S6 therefore has no compute-saving motive under the stated threat model — it is a *methodological error* (or a deliberate misuse of a bin-centre approximation), not a shortcut in the cost sense. Likewise S7, described as evading R7 "at zero marginal cost, since the effective-multipole shortcut already builds the full operator honestly."
There *is* a real cost motive — §2 gestures at it ("A common shortcut is to evaluate a theory spectrum at a representative multipole for each bin"), and in an MCMC the per-likelihood-call band evaluation is repeated 10⁵–10⁶ times so that the savings are large in aggregate even though the one-time operator build is not avoided. That argument is never made, and without it the reader is left with the paper's headline contributions (R7, R8) aimed at a class whose members, by construction, decline the very savings the framework is built to detect.
Remedy: state the cost model per class explicitly — one-time operator build vs. per-evaluation band contraction — and quantify the aggregate saving S6 buys in a realistic inference (number of likelihood calls × per-call cost). This also repairs §2's motivation.

**M12 — MAJOR — The Statement of Need's motivating number is measured in the spin-0 sector, while the section is framed around the spin-2 tensor the package targets.**
*Location: §2 pp. 2 (opening and the N_side = 64 sentence); §6 pp. 9–10.*
§2 opens "For two spin-2 fields, NaMaster exposes a bandpower-window tensor with spectrum ordering [EE, EB, BE, BB]", then quantifies the shortcut: "On the synthetic N_side = 64, ℓ_max = 64 configuration used for the blind test below (Sec. 6), replacing the full band evaluation with a single effective-multipole transfer factor per 8-ℓ band produces order-unity fractional deviations in several bands." But the blind test's estimator is the in-house **spin-0** MASTER implementation (stated clearly on p. 9, and in the abstract), and the per-band numbers ("0.23–1.18 across the 8-wide bands", p. 9) come from that spin-0 path. The reader of §2 will take the order-unity deviation as a property of the spin-2 window operator that `windows` actually contracts. Spin-2 coupling has additional E/B-mixing structure and a different low-ℓ behaviour, so the magnitude does not transfer without argument.
Remedy: label the number as spin-0 at the point of use in §2, and either argue transferability to spin-2 or produce the spin-2 number directly — the machinery to do so exists, since the PyMaster cross-check (p. 9) shows PyMaster can be installed on demand and §9 describes a real PyMaster integration example.

---

### MINOR

**m1 — MINOR — Table 1 is not updated for R8.**
*Location: Table 1, p. 4.* The `intermediates.pseudo_cl` row reads "asserted, absent fails R7 open". R8 explicitly fails *closed* on absence (p. 7: "a missing, malformed, non-finite or wrong-length pseudo_cl … all fire"), and arm S8 exists to demonstrate it. The table is the reader's first summary of trust levels and currently states the superseded behaviour.

**m2 — MINOR — Paragraph heading "Protocol, two batches." contradicts its own text.**
*Location: §6, p. 4.* The same paragraph ends "The protocol was run four times: a pilot, a primary structural sweep, a value-level extension, and a post-commitment challenge."

**m3 — MINOR — "escapes X/6" is used with opposite meanings on the same page.**
*Location: §6, p. 7.* Batch 3: "S5 (metadata forgery, extended to forge p := M C) still **escapes 6/6**" (= escaped in 6 of 6). Batch 4: "S5 (metadata forgery) still **escapes 0/6**" (= flagged in 0 of 6). Tables 3 and 4 use the "Flagged" convention; the prose should too, throughout.

**m4 — MINOR — The abstract's stated reason for not testing against PyMaster is contradicted later.**
*Location: Abstract p. 1; §12 p. 15.* Abstract: "PyMaster is not installed in the test environment and exposes no Wigner-3j counter." §12: the cross-check was "run in a throwaway conda-forge pymaster 3.0 environment ($0, under one minute)." Installation is evidently not a constraint; only the absent 3j counter is. The abstract should drop the first conjunct.

**m5 — MINOR — R6's cross-run disjunct is order-dependent and the first run of a colliding group is structurally unflaggable.**
*Location: Table 2 p. 4; §6 p. 7.* R6's second disjunct fires when a bandpower digest "already occurred on an **earlier** run with a different input-map hash". The earliest run in any colliding set therefore never fires it, and which run is "earliest" depends on an arbitrary processing order. Batch 3's S4b result ("4/6 fired it, and the other 2 collapsed to the reference disjunct") is consistent with this but the order-dependence itself is never analysed, nor is the behaviour when the reference disjunct does not also apply.

**m6 — MINOR — The R7/R8 tolerance mixes a per-row absolute residual with a global vector norm, making sensitivity strongly ℓ-dependent and uncharacterised; "theory" is unspecified.**
*Location: §6, p. 7.* The rule fires iff `|Σ M_{ℓ1ℓ2} C_{ℓ2} − p_{ℓ1}| > 1e-6 ‖p‖₂` on a spot row. Since ‖p‖₂ is dominated by the largest (low-ℓ) entries, the effective *relative* sensitivity on high-ℓ rows, where p is small, is far coarser than 1e-6. The paper's arms have 23–118% errors so this is immaterial to the reported results, but the rule's stated sensitivity is not the sensitivity it has. Separately, "TOL = 1e-6 was fixed from theory plus non-blind calibration before the seal" does not say what the theory was; and the calibration used S6's own residuals ("S6 under the same seeds, 7.5e-2–1.5e-1") before sealing, i.e. it is adversary-informed — disclosed, and with an ~10.7-order gap it is not knife-edge, but it should be labelled as adversary-informed calibration rather than as pre-registration.

**m7 — MINOR — K = 6 and the row-draw mechanics are unspecified.**
*Location: §6, pp. 7–8.* The number of operator rows N is never printed (inferable only from "∼9% of a full build"); K = 6 is never justified; and whether the six indices from `sha256(σ‖run id‖D)` are drawn with or without replacement — which changes the soundness bound — is not said. See M1.

**m8 — MINOR — "Retained" is used inconsistently for the [4, 20, 4, 1025] workspace tensor.**
*Location: §8 p. 11; §12 p. 13.* §8: "Because the original workspace tensor was **not retained**, the scalar is not a self-contained reproducibility claim." §12: "the **largest retained arrays** are the [4, 20, 4, 1025]-shaped bandpower-window tensors in §8". The §12 sense is evidently "largest in-memory arrays"; the collision with §8's disclosure is confusing on a point the author has otherwise gone out of his way to be careful about. (The derived figures are right: 4·20·4·1025 = 328,000 entries ≈ 10⁵, 2.62 MB ≈ "a few MB".)

**m9 — MINOR — Batch 4 silently drops the S4b arm, and batch-3/batch-4 pre-declared criteria are never quoted.**
*Location: §6 pp. 7–8.* Batch 3 runs 8 arms including S4b (the arm introduced specifically to exercise R6's cross-run disjunct); batch 4's nine arms are honest/S1–S8 with S4b absent and no explanation. Batch 2's success criterion is quoted in full (pp. 4–5); batch 3's pre-registration is named by commit but never quoted; batch 4's is neither named nor quoted. See E4.

**m10 — MINOR — sha256(σ) is not externally timestamped although OpenTimestamps is used for every other digest in the paper.**
*Location: §6 pp. 6, 7–8; §11 L2 p. 12.* R8's whole soundness argument is that σ was fixed before any receipt was published. The paper already uses OTS for seal digests of batches 1–3 and discusses its limits carefully. Stamping sha256(σ) is free and would upgrade "the committing verifier's honesty" (abstract) to "the committing verifier's honesty plus a Bitcoin-anchored lower bound on the commitment time".

**m11 — MINOR — JORS metapaper structural requirements are not met.**
*Location: title page; §12 Availability, pp. 13–15.* No corresponding-author email or institutional statement beyond "Independent researcher" and an ORCID. The Availability section is missing the "List of contributors" and "Language" sub-headings a JORS metapaper requires, and "Software location → Archive" does not give the publisher, version published, and date published in the prescribed fields (the DOI and deposit date are present in prose). Section ordering also departs from the prescribed Overview → Implementation and architecture → Quality control sequence, with §§4–7 interposed.

**m12 — MINOR — No test-coverage figure for a software metapaper.**
*Location: §8, p. 11.* "no line- or branch-coverage tool is currently configured in that workflow, so a coverage percentage is not reported here rather than estimated." The honesty is appreciated, but for a JORS metapaper — where quality control is a required section and the thesis is verification rigour — adding `pytest-cov` to an existing CI workflow is a few lines and would let the paper report a real number rather than explain its absence.

**m13 — MINOR — §2 promises a figure; the paper contains none.**
*Location: §2, p. 2.* "a per-band deviation figure traceable to a committed script and output is discussed in §6 below." The manuscript has zero figures. If "figure" means "number" the wording should change; if a plot was intended, a per-band deviation plot would materially help §2 and §6 and is the single most useful visual the paper could carry.

**m14 — MINOR — Batch 1's S5 outcome is never reported, yet the abstract claims S5's escape is "unchanged across all four batches".**
*Location: Abstract p. 1; §6 p. 6.* Batch 1's reported counts are "12/12 on S1–S4 … 0/3 honest false positives"; the S5 arm (3 runs) has no printed outcome. The abstract's "unchanged across all four batches" and p. 8's "still escapes, unchanged across all four batches" therefore rest on an unreported batch-1 number.

**m15 — MINOR — Author Contributions claims funding acquisition; the Funding Statement says there was none.**
*Location: §10 p. 12; Funding Statement p. 15.* "conceptualization, …, project administration, and **funding acquisition**" vs. "No external funding supported this software release."

**m16 — MINOR — The attestation discussion over-hedges on enclaves.**
*Location: §7, p. 11.* "the two are complementary and neither substitutes for the other under an adversary who controls the harness itself." Under measured boot / SGX / TDX the adversary specifically *cannot* control the harness — the attestation binds the measured binary — so an instrumented harness inside an attested enclave does substitute for the missing anchor and does close S5. This matters because it is the paper's only correct answer to its own stated limit (see M3).

**m17 — MINOR — Internal cross-references are unusable.**
*Location: throughout §§1–13.* Because §6 has no numbered subsections, roughly fifteen references resolve to the same number: "(§6–6)" (four occurrences, e.g. pp. 7, 11, 12), "§6 presents R8" (p. 7), "the PyMaster cross-check (§6)" (p. 14), "batch 4 (§6)" (p. 14), "the pilot (batch 1, Sec. 6) … batch 2 (Sec. 6) … batch 3 (Sec. 6) … batch 4 (§6)" in one sentence (§12, p. 14), and L1's "(§6)" (p. 12). "(§6–6)" in particular reads as a production failure. Give §6 numbered subsections (6.1 Protocol, 6.2 Batch 1, 6.3 Batch 2, 6.4 Batch 3 / R7, 6.5 Batch 4 / R8, 6.6 Scope limits, 6.7 PyMaster cross-check) and repoint every reference.

---

### NIT

**n1 — NIT — Title-page revision stamp.** "v2B.0.23(2026-09-05 12:00 PT)" — missing space before the parenthesis; and the stamped time (12:00 PT) postdates the file's own creation timestamp (02:25:48 PDT), so the stamp is not generated at build time.

**n2 — NIT — Unexplained sign and missing norm in R8's honest-residual statement.** *p. 7:* "An honest run's residual is −10−12 C on every row at once". The leading minus is presumably a mangled "∼", and the quantity should carry an absolute value or a norm to match the rule statement, which uses |·| and ‖p‖₂. As printed it asserts a signed residual of −10⁻¹²·C.

**n3 — NIT — "bounds the false-positive rate above by 0.393"** (p. 8) should read "bounds … from above by" / "upper-bounds".

**n4 — NIT — "O(10–100%)" is not evidenced at the 10% end.** *p. 9:* the quoted range is "0.23–1.18 across the 8-wide bands", i.e. 23–118%. Either widen the evidence or write O(20–100%).

**n5 — NIT — Float placement.** Table 4 (batch 3) appears on p. 8, after the batch-4 paragraph that supersedes it, so the reader meets R8's results before the R7 table they build on.

**n6 — NIT — Reference formatting.** [6] "OpenSSF, 'Supply-chain Levels for Software Artifacts (SLSA),' slsa.dev" has no version or access date for a living specification. [14] MLflow is missing page numbers (IEEE Data Eng. Bull. 41(4), 39–45). All other entries [1]–[5], [7]–[13] check out against the literature.

**n7 — NIT — Gerrymandered novelty claim.** *p. 8:* "the first post-commitment challenge protocol for pseudo-C_ell execution receipts." The qualifier makes the reference class a singleton. Either drop the claim or state the novelty against the result-checking/ABFT literature (M5), where it is a genuine if narrower contribution.

**n8 — NIT — Unexplained timing disparity at point of use.** *§12 p. 15:* batch 1's 18 runs "take approximately one to two minutes" while batch 2's 36 runs "measured ∼11 s". The cold/warm cache explanation exists on p. 6 but is 9 pages away.

**n9 — NIT — Opaque sentence in Author Contributions.** *p. 12:* "Correspondence metadata remain author-supplied submission metadata and are not inferred by the software release process." I cannot determine what claim this makes or what it is guarding against.

**n10 — NIT — The Appendix is unnumbered** ("Appendix: Batch-2 Per-Run Verdicts", p. 15) and is referenced only implicitly; give it a letter and a forward reference from §6.

---

## Independent checks I performed (all from printed values only)

Recorded so the author can see which numbers I verified and which I could not.

**Arithmetic — all correct:**
- Clopper–Pearson one-sided 95% lower bound, 4/4: 0.05^(1/4) = 0.47287 → paper's 0.473 ✓
- Clopper–Pearson one-sided 95% lower bound, 12/12: 0.05^(1/12) = 0.77908 → paper's 0.779 ✓
- Clopper–Pearson one-sided 95% upper bound, 0/3: 1 − 0.05^(1/3) = 0.63160 → paper's 0.632 ✓
- Clopper–Pearson one-sided 95% upper bound, 0/6: 1 − 0.05^(1/6) = 0.39304 → paper's 0.393 ✓
(Arithmetically right; see E3, M6, M7 for why three of the four should not be in the paper.)

**Design arithmetic — all consistent:**
- Batch 1: 6 arms × 3 = 18 ✓; batch 2: 7 arms × 5 = 35 ✓ (+1 reference = "36 runs including the reference" ✓); batch 3: 8 arms × 6 = 48 ✓; batch 4: 9 arms × 6 = 54 ✓.
- Batch 3 "five arms × 6 = 30/30" for S1–S4 + S4b ✓ (and the paper's own correction of an earlier draft's "24/24" is right).
- Table 3 rows sum to 35 ✓; Table 4 rows sum to 48 ✓.

**Appendix Table 6 (p. 16) audited run-by-run against Table 3 — fully consistent.**
Run indices 0–34 = 35 runs. Arm tallies: honest {3,10,17,20,22} = 5; S1 {4,21,26,29,32} = 5; S2 {13,18,19,30,33} = 5; S3 {1,6,11,15,27} = 5; S4 {5,7,8,9,23} = 5; S5 {0,12,24,28,31} = 5; S6 {2,14,16,25,34} = 5. Rules fired per arm match Table 3 exactly in all 35 rows (S1/S2 → R3,R4; S3 → R2,R3,R4; S4 → R6; honest/S5/S6 → none). This is a clean, checkable appendix and I credit it.

**Physics / algebra — correct:**
- Eqs. (1)–(3), uniform rotation with vanishing intrinsic EB: C^EE(β) = C^EE cos²2β + C^BB sin²2β = ½(EE+BB) + ½(EE−BB)cos4β ✓; C^BB(β) symmetric with the sign flipped ✓; C^EB(β) = ½(EE−BB) sin4β ✓.
- Eqs. (4)–(5): the three-component precontraction is exact because W acts linearly on the spectrum vector, so R^{i,k} = Σ_{j,ℓ} W^{ij}_{bℓ} C^{j,k}_ℓ and C^i_b(β) = R^{i,0} + cos4β·R^{i,c} + sin4β·R^{i,s} reproduce the full contraction at every β ✓. This is a genuinely neat optimisation and the paper is right that it retains the full window tensor.
- Default recovery grid "2001 points spanning −1° to +1°" (§4, p. 3) ↔ the "declared 0.001° grid" (§9, p. 12): 2°/2000 = 0.001° ✓.

**§9 recovery campaign — internally consistent:**
- SEM = SD/√500: 0.0128/22.361 = 5.72e-4 → "± 0.0006" ✓; 0.0127/22.361 = 5.68e-4 → "± 0.0006" ✓.
- Recovery offsets 0.270→0.2699, 0.342→0.3419, 0.000→−0.0001 are all ≈0.2 SEM, i.e. no detectable bias ✓. The framing ("software-recovery checks under the stated simulation contract, not measurements, detection significances, or evidence for a physical birefringence model") is exactly right and I want to note it approvingly.

**§12 memory estimate:** 4·20·4·1025 = 328,000 entries → "order 10⁵" ✓; ×8 bytes = 2.62 MB → "a few MB" ✓.

**§6 magnitudes:** honest 1.4e-12 vs. S6 7.5e-2 is 10.73 orders → "an eleven-order gap" ✓. 6 rows at "∼9% of a full build" implies N ≈ 63 rows, consistent with ℓ = 2…64 ✓. Table 5's 4.25e-13 / 1.54e-12 are consistent with the abstract's "≲ 5 × 10⁻¹³ and ≲ 2 × 10⁻¹²" ✓. Coupling matrix 94×94 is consistent with ℓ = 2…95 ✓.

**Could not check from the paper alone:** every sha256/commit digest; `seal_verified` status; OTS attestation states; the 41-test count and CI matrix; the Zenodo record contents; whether `verify.py`'s freeze-commit and seal-commit versions differ only in plumbing (see M10); the sympy Wigner-3j agreement at 6e-16.

---

## Closing remarks

I want to separate two judgements, because they point in opposite directions and the author deserves both.

**On conduct, this manuscript is better than most of what I referee.** The author relabelled his own best-looking batch as a pilot because two rules moved after unblinding. He disclosed a third post-hoc change (the R6 documentation correction) that nobody would have found. He discovered that R7's challenge was prover-predictable, wrote it down in the abstract, and then *built the adversary that exploits it* rather than softening the prose — his own phrasing, "are answered by building the exact adversaries they predict rather than by softening the prose above", is the right instinct and I would like to see it imitated. He preserved and published an aborted batch, named the defect (`healpy.synfast` ignoring the seed argument through the global RNG), explained why the abort could not have been informed by the assignment, and volunteered that no stopping rule had been pre-registered. He corrected a "24/24" to "30/30" in print. He declined to report a pooled detection figure across arms because "its value is fixed by the arbitrary choice of how many escape classes are included". He states repeatedly that the seal proves ordering and not execution, and that the same party sealed, ran and unsealed. Several of my findings above (M6, M7, E3) exist only because the author *wrote down the caveat that refutes his own statistic* — a paper that had simply omitted the independence caveat would have been harder to referee and worse.

**On suitability and completeness, it is not ready.** It is two papers in one jacket, and by its own §13 the half that belongs at JORS is the half that is not written yet. Its archive predates its headline results by seven weeks. Its zero-false-positive claim, the load-bearing counterpart to its detection claim, is an identity rather than a measurement, and the paper does not run the experiment (honest-but-different runs) that would make it a measurement. Its newest and most-promoted result, R8, is supported by one sentence where its predecessors get tables, commit chains, seals and appendices. And its central soundness claim is qualitative where a two-line calculation would have shown that K = 6 challenged rows buy very little against an adversary who shortcuts 10% of the operator.

The good news is that essentially all of this is reparable without new science, and several repairs make the paper stronger rather than merely compliant: the ABFT/result-checking framing (M5) suggests a better rule than uniform row sampling; the weak-Fiat–Shamir literature (M2) shows R7's gap was a known trap rather than an idiosyncratic one; the honest-variation arm (E3) would convert the weakest number in the paper into the most informative; and a beacon or an OTS stamp on sha256(σ) (m10) removes the last dependence on the author's own honesty as verifier, which is the thing a sceptical reader will fix on.

**Recommendation: MAJOR REVISIONS**, contingent on E1 and E2. If the author elects to keep the measurement and the software description in a single manuscript, my recommendation converts to reject-and-resubmit at a venue that can referee the measurement (ACM REP, as the author himself proposes), with a separate short metapaper returned here.

**Finding counts:** ESSENTIAL 4 · MAJOR 12 · MINOR 17 · NIT 10 (43 total).
