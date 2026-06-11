# EXT2 P1B — External Truth-Audit (Round EXT2, in-thread delta)

**Paper**: `arxiv/paper1b_mcmc_companion.tex` · v1B.0.56 (18 pp., PDF md5 4abcc0c6)
**Reports audited**:
- `EXT2_P1B_ChatGPT.md` — GPT-5.5 Pro Extended — **MAJOR REVISIONS** (was MAJOR @ EXT1) — 2 fresh BLOCKERS, 4 fresh MAJORS, 5 minors; closures incl. 2 REGRESSION calls
- `EXT2_P1B_Gemini.md` — Gemini 3.5 Thinking — **MAJOR REVISIONS** (**regressed from MINOR @ EXT1**) — 1 fresh MAJOR, 3 minors, 2 NOT-ADDRESSED calls
- `EXT2_P1B_Grok.md` — Grok Heavy — **ACCEPT after minors** (was MINOR @ EXT1) — 0 fresh majors, 4 minors, both prior majors CLOSED

**Audit date**: 2026-06-10 · **Protocol**: feedback_peer_review_truth_audit_protocol

---

## Verdict table — fresh findings + disputed closures

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| F1 | GPT F-B1 | BLOCKER | Data-availability section makes false/unverifiable release claims (tag, CHANGELOG SHA, README-pinned DOIs) | **VERIFIED** | tex L1995–2009: "tagged \texttt{\paperVersion}" (= v1B.0.56); "exact commit SHA is recorded in the repository's CHANGELOG.md under that tag"; "HuggingFace dataset DOIs … listed in the repository README at the \paperVersion tag". On-disk: `git tag` shows the paper1b series stops at **paper1b-v1B.0.41** (9 tags total; naming convention is `paper1b-v1B.0.XX`, not `v1B.0.56`); `git ls-remote --tags origin` confirms no v1B.0.5x tag exists remotely; **no CHANGELOG.md exists anywhere in the repo** (only node_modules). All three release claims are currently false — ChatGPT's 404 was a correct read of the live repo, not a stale view. Closure-introduced: the EXT1 A4 fix wrote the claim into the tex without creating the artifacts; R30conf checked the tex sentence (E7 "HOLDS") but never ran `git tag`. |
| F2 | GPT F-B2 | BLOCKER | Corrected MCMC diagnostics only partially propagated + new count mismatch | **VERIFIED (both parts; one part is a closure-introduced regression)** | (i) `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/freeze_diagnostics_CORRECTED.json` contains `total_accepted_samples: 176840` — the OLD wrong count. Paper body uses 176,240 throughout (tex L877, L900–905, L1000, L1219), and the v1B.0.23 R25a audit root-caused 176,240 as correct by direct chain line-count. The R29 "CORRECTED" artifact reintroduced the stale number. (ii) `frozen/planck_bao_sn_20260312_1954/diagnostics/` contains ONLY `convergence_report.txt` — no `parameter_summary_CORRECTED.json`, no README — and that report's "Parameter summary" (L83+) is still column-shifted (e.g. `nnu: 0.96644` is plainly n_s, not N_eff). Exactly the artifact class EXT1 F1 flagged; the fix wave corrected only the full-tension directory. |
| F3 | GPT F-M1 | MAJOR | SN-overlap caveat cites the wrong paper (DES-SN5YR cosmology paper, not the Vincenzi comparison paper) | **VERIFIED** | tex L1154: "refer to the DES Collaboration comparison analysis~\cite{DES2024SN5YR}". `arxiv/references.bib` L434–440: DES2024SN5YR = Abbott et al., "Cosmology results with ~1500 new high-redshift SNe Ia" (ApJL 973, L14) — the cosmology-results paper. Vincenzi et al. ("Comparing the DES-SN5YR and Pantheon+ SN cosmology analyses," the paper that actually quantifies the ~20% overlap and Malmquist-correction differences) is absent from the bib. Genuinely new — introduced with the EXT1 A3 overlap-disclosure closure. |
| F4 | GPT F-M2 + Gemini Fresh-M1 | MAJOR | w₀wₐ "quintom-B empirical anchor" rests on a knowingly non-independent DES-SN5YR×Pantheon+ product likelihood; disclosure ≠ fix; rerun/control chains demanded | **PARTIAL / HOUSTON-DECISION (consensus escalation of EXT1 F4)** | The overlap IS now disclosed (EXT1 A3 closure landed: §III caveat (e), ~20% shared SNe, no joint covariance, direction-of-bias statement). What is NOT done: any control chain. Per the recompute rule (SAMPLE+ESTIMATOR+NULL), neither reviewer ran numbers — Gemini's "artificially shrinks σ_w0, σ_wa / shifts best-fit" is direction-plausible but unquantified, so the severity is OPINION while the underlying gap (no overlap-robustness demonstration) is VERIFIED-by-construction. The honest fixes are exactly GPT's: (a) two control chains (DESI+Planck+Pantheon+ only; DESI+Planck+DES-SN5YR only) — real compute (~repeat of iter2, days on the MPI pod), or (b) demote "empirical anchor" → "exploratory cross-check" everywhere (§III, Table II, conclusion). Per /hardest-path-first: do (a). |
| F5 | GPT F-M3 | MAJOR | "Chains are not pre-computed" contradicts the committed frozen chain files | **VERIFIED** | tex L2067: "The ΛCDM+ΔN_eff proxy chains are not pre-computed (regenerate via reproduce_cosmology.sh…)". But the frozen artifact directories committed in-repo contain the chains themselves (`frozen/full_tension_20260311_1728/chains/chain_01…06/spin_torsion.1.txt` — read directly by the R29 E1 verification; `planck_bao_sn_20260312_1954/chains/` likewise). The corrected README even verifies values by loading those chain files. Wording contradiction is real; replace with the precise statement of what is committed (frozen diagnostics + chains) vs regenerable. |
| F6 | GPT F-M4 | MAJOR | "Natural parameter values" headline retained despite quantified tuning/coupling burden | **PARTIAL (re-raise of EXT1 F3 PARTIAL)** | tex L795, L1618, L1936 retain "natural parameters / natural parameter values", each immediately followed by the tuning disclosure parenthetical. The numbers ChatGPT cites (median m≃36H₀, θᵢ≤0.1 sliver 0.33%, Ω_a<0.01 mass 13%) are the paper's own — its proposed replacement sentence ("can accommodate the observed β, but the spectator-safe interpretation requires a tuned misalignment subspace and non-minimal photon coupling") is strictly more accurate than the current shorthand. Same verdict as EXT1: framing vulnerability, not fabrication; the residual fix is deleting the word "natural" at 3 sites. |
| F7 | Gemini M1 closure | MAJOR | Pairing-bias (PR4 high-ℓ + 2018 low-ℓ/lensing) swap test "NOT ADDRESSED" | **VERIFIED-UNCHANGED / dispute** | tex L869–874: the disclosure ("we have not run a release-pairing swap test … unquantified at the quoted precision") is verbatim unchanged since EXT1. Gemini's NOT-ADDRESSED is factually true; EXT1 truth-audit F27 ruled the disclosure adequate-PARTIAL for a companion paper and no patch was scheduled. Closure dispute, not a new error. Optional upgrade: cite a CamSpec/NPIPE consistency paper to bound the pairing shift. |
| F8 | Gemini M2 closure | MAJOR | Live Planck-only chain (114,992 samples, R̂−1∼0.05) still referenced across abstract/body/conclusions — "NOT ADDRESSED" | **VERIFIED-UNCHANGED / dispute** | tex L703 (abstract parenthetical), L874, L920–922, L1545–1546, L1574, L1953–1954. All sites explicitly exclude it from tables/headline. Factually unchanged since EXT1 (F28 PARTIAL: disclosure adequate). Deliberate non-action; same fix menu as EXT1 A16 (drop from abstract, keep one body mention). Note P1A carries the same class of live-chain content (EXT2 P1A F-M6) — fix both in one sweep. |
| F9 | GPT minor | MINOR | PR3/PR4 wording: §VI still calls the published headline "joint WMAP9 + Planck PR4/NPIPE" | **PARTIAL (re-raise of EXT1 F16 FALSIFIED, but with one real residual site)** | The disambiguation footnote (tex L726–732) is correct and was the basis of the EXT1 FALSIFIED verdict. However tex L1628 does read "…the published Eskilt–Komatsu joint WMAP9 + Planck PR4/NPIPE analysis" — for the published-paper headline this should be PR3+WMAP9 (the PR4/NPIPE label belongs to the repository rerun per the footnote's own taxonomy). One-site fix. |
| F10 | GPT minor | MINOR | CMB-S4 sentence says "spin-torsion ΔN_eff contribution" | **PARTIAL** | tex L1194 ties the CMB-S4 forecast to "the spin-torsion sector" phrasing; R29 M3 softened "first precision test" but not the sector attribution. Replace with "phenomenological ΔN_eff proxy" at both sites (L1194, L1961). |
| F11 | GPT minor | MINOR | PACS numbers remain | **OPINION (re-raise of EXT1 F14)** | Journal-dependent; defer to submission target. |
| F12 | GPT minor | MINOR | Table IV claims-classification says "Verified" for results whose public release is not cleanly versioned | **VERIFIED (minor, contingent on F1)** | tex L2102–2108. While the tag/DOI claims are false (F1), "Verified" overstates the public verifiability. Either create the tag (F1 fix) or relabel "internally verified / pending tagged artifact". |
| F13 | GPT minor | MINOR | App. C calls [9,51] the "full EOM-required band" while §VI says the natural-box requirement extends to ~160 | **VERIFIED (minor)** | tex L2169 ("covering the full EOM-required band [9,51]") vs L1789/L1810/L1978 (couplings up to ≈160 at the smallest displacement). Clarify: [9,51] is the posterior-supported band (69% mass, L1836), not the full kinematic requirement. |
| F14 | Gemini minor | MINOR | "Configuration (iii) — model-independent firee fit" typo | **FALSIFIED (extraction artifact)** | tex L2155: "Configuration (iii) --- model-independent $\beta_{\rm free}$ fit" — source clean; "firee" is the PDF text-extraction of the β subscript. |
| F15 | Gemini minor | MINOR | Table II row label mangled "H₀ I₀ [km s⁻¹ Mpc⁻¹]" | **FALSIFIED (extraction artifact)** | tex L1038: `$H_0$ [km\,s$^{-1}$\,Mpc$^{-1}$]` — clean (this exact header was the EXT1 A14 fix). |
| F16 | Gemini minor | MINOR | Table II "(marg.-tailfn; . a)" garble + footnote letters out of sequence (b, e, d; c absent) | **PARTIAL (needs one visual render check)** | Source is clean: `(marg.-tail; fn.~\ref{fn:wcaveat})` and `\footnote{\label{fn:wcaveat}…}` (tex L1032–1052) — the prose garble is extraction. The letter-sequence complaint is plausibly real, though: revtex `\footnote` inside `table*` + `\ref`-reuse can emit non-sequential markers. Action: pdftoppm the Table II page at next compile; if markers are non-sequential, convert to `\tablenotemark/\tablenotetext`. |
| F17 | Grok M1 closure | MAJOR (as CLOSED) | Grok credits "tagged v1B.0.56; SHA in CHANGELOG.md … version-pinned and machine-checkable" as CLOSED-complete | **FALSIFIED CLOSURE (over-credit)** | Direct contradiction with F1: the tag and CHANGELOG do not exist. Grok verified the SENTENCE, not the artifact — textbook pattern for the findings archive (reviewer credits a reproducibility claim without resolving it). Grok's ACCEPT rests partly on this over-credit. |
| F18 | Grok minor | MINOR | Burn-in note doesn't say which GetDist config produced 106,361 | **PARTIAL (minor)** | The reconciliation footnote exists (EXT1 A2 closure; `convergence_report.txt` now carries the post-hoc-readout NOTE); adding the one-parenthetical Grok requests is cheap and precise. |
| F19 | Grok minor | MINOR | Add explicit sentence that all Table I–II numbers were recomputed from raw chains/CORRECTED.json, not the buggy export | **VERIFIED (minor)** | True statement (R29 E1 recomputed from chains) not yet stated in the Data-Availability paragraph; one sentence. NB: fold in the F2 count fix first so the sentence is actually true of the artifacts. |
| F20 | Grok minor | MINOR | Consolidate artifact filenames/DOIs into one machine-checkable index table | **OPINION (re-raise of EXT1 F25)** | Reasonable polish; pairs naturally with the F1 tag work. |
| F21 | Grok minor | MINOR | Soften "qualitative quintom-B finding … unlikely to be reversed" | **PARTIAL (minor)** | Direction-of-bias claim is asserted, not demonstrated (same root as F4); Grok's softened sentence is the minimal honest fix if the control chains are not run. |

## Why Gemini regressed MINOR → MAJOR (driver-by-driver audit)

1. **Driver 1 — fresh SN product-likelihood MAJOR (F4).** Triggered BY the v1B.0.56 transparency fix: EXT1 A3 added the overlap disclosure, and Gemini (correctly) read a disclosed-but-unfixed independence violation under the +4.3σ/−3.6σ headline. No new on-disk error — a *transparency-induced escalation* (disclosure ≠ fix). The only closure Gemini will accept is a rerun/control chain.
2. **Driver 2 — M1 pairing-bias NOT ADDRESSED (F7).** True: text unchanged. Deliberate non-action per EXT1 truth-audit (disclosure ruled adequate). Closure dispute.
3. **Driver 3 — M2 live Planck-only chain NOT ADDRESSED (F8).** True: unchanged. Same deliberate non-action.

Net: zero of the three drivers is a new defect; one (F4) carries a real, hard fix (control chains) that would likely flip Gemini back to MINOR/ACCEPT, and incidentally satisfies GPT F-M2. The Grok ACCEPT ↔ Gemini MAJOR spread on the same PDF is reviewer-disposition variance plus Grok's F17 over-credit.

## Consensus findings (≥2 reviewers)

| # | Theme | Reviewers | Verdict |
|---|-------|-----------|---------|
| C1 | SN overlap: product likelihood must be demoted or control-chained | GPT F-M2, Gemini Fresh-M1, Grok minor-4 (softening) | PARTIAL → control chains |
| C2 | Release identity (tag/SHA/DOI) must actually exist | GPT F-B1/M9-REGRESSION; (Grok's CLOSED falsified) | VERIFIED |
| C3 | Artifact diagnostics propagation incomplete | GPT F-B2 + B1-PARTIAL | VERIFIED |

## Action plan (VERIFIED/PARTIAL, hardest first)

1. **[F4/C1] Run the two SN control chains** — `reproducibility/cosmology/` iter2 configs: (a) DESI DR2 + Planck NPIPE + Pantheon+ only, (b) DESI DR2 + Planck NPIPE + DES-SN5YR only; same priors/burn-in as iter2; report (w₀, wₐ) shifts vs the combined chain in §III + Table II. Until they finish, demote "quintom-B empirical anchor" → "exploratory w₀wₐ cross-check" (tex §III, Table II caption, conclusion) and soften L-"unlikely to be reversed" (F21).
2. **[F1/C2] Create the real release** — `git tag paper1b-v1B.0.56 <stamp-commit> && git push origin paper1b-v1B.0.56`; add a root `CHANGELOG.md` (or repoint the tex to the in-tex version log); put the three HF dataset DOI URLs directly in Appendix A; update tex L1995–2009 to the exact tag name `paper1b-v1B.0.56`. Add a `bigbounce-version-bump` gate: any tex sentence claiming a tag fails the bundle unless `git tag -l` confirms it.
3. **[F2/C3] Fix the corrected-diagnostics artifacts** — (a) `freeze_diagnostics_CORRECTED.json`: 176840 → 176240 (regenerate from chains, don't hand-edit); (b) add `parameter_summary_CORRECTED.json` + README to `planck_bao_sn_20260312_1954/diagnostics/` with the same column-permutation diagnosis; (c) add the machine-readable `table1_reproduction.json` + CI check GPT proposes (compare to tex Table I; fail on mismatch).
4. **[F5] Rewrite the "not pre-computed" sentence** — tex L2067: state precisely that the two frozen artifact directories include committed chains + diagnostics, while fresh proxy chains can be regenerated via `reproduce_cosmology.sh`.
5. **[F3] Add the Vincenzi et al. comparison-paper reference** — `arxiv/references.bib` (new entry) + cite at tex L1154; keep DES2024SN5YR for the likelihood itself.
6. **[F6] Delete "natural" at 3 sites** — tex L795, L1618, L1936 → GPT's replacement sentence.
7. **[F9/F10/F12/F13/F18/F19] Minor pass** — L1628 PR4→PR3 headline label; CMB-S4 "phenomenological ΔN_eff proxy" (L1194, L1961); Table IV "Verified" → "internally verified / pending tagged artifact" (until action 2 lands, then revert); App. C [9,51] = posterior-supported band; burn-in parenthetical; recomputed-from-chains sentence.
8. **[F16] Visual check** — pdftoppm the Table II page; fix footnote-marker sequence via `\tablenotemark` if non-sequential.
9. **[F8 + P1A F-M6] Live-chain sweep across both papers** — drop the Planck-only mention from the P1B abstract (keep one body site), delete the P1A Table III live-chain footnote.

## GAP METRIC

- **(a) Genuinely new (neither EXT1 nor R29/R30 caught): 4 substantive** — F1 (release claims false on-disk — R30conf verified the sentence, never the tag), F2 (176,840 regression in the CORRECTED artifact + planck_bao_sn non-propagation), F3 (Vincenzi mis-citation, introduced by the EXT1 A3 closure), F5 ("not pre-computed" contradiction). Plus 2 new minors (F12 Table-IV labels, F13 EOM-band naming). **3 of the 4 are closure-introduced** (F1 by EXT1-A4 text-without-artifact; F2 by the R29 CORRECTED-file generation; F3 by the EXT1-A3 caveat).
- **(b) Re-raises of audited-FALSIFIED items: 1** — F9 (PR3/PR4, EXT1 F16 FALSIFIED) — though this re-raise surfaced one genuinely mislabeled residual site (L1628), so it pays for itself.
- **(c) Closure-verification disputes: 7** — F4 (disclosed-vs-fixed escalation, 2 reviewers), F7, F8 (NOT-ADDRESSED on deliberately-parked items), F6 (natural-params residual), GPT B1-PARTIAL/REGRESSION + M9-REGRESSION (both audit as accurate), F17 (Grok CLOSED over-credit — falsified closure, the inverse failure mode).

## Deferred to compute-queue (EXT2 closure wave 2026-06-10)

The following actions are compute-bound and could not be closed in the
same-day source-edit wave; they are queued on the dedicated MPI pod
and will be closed in a follow-up wave when the chains converge.

- **F4/C1 — SN-overlap control chains (Gemini-regression drivers).**
  Two cobaya control chains queued: (i) DESI~DR2 + Planck~NPIPE +
  Pantheon$+$ only; (ii) DESI~DR2 + Planck~NPIPE + DES-SN5YR only.
  Same priors / burn-in as iter2. Manuscript prose at L1150 already
  softened from "unlikely to be reversed" to "plausibly robust …
  but this has not been demonstrated quantitatively in the present
  manuscript" pending the control-chain $(w_0, w_a)$ shifts.

## Post-audit recommendation

ChatGPT MAJOR REVISIONS is calibrated; Grok's ACCEPT is over-credited (F17); Gemini's MAJOR is severity-inflated on disclosed items but its core ask (control chains) is the right hard fix. Hold readiness at 94 until actions 1–3 land; actions 2–8 are same-day, action 1 is pod-compute.
