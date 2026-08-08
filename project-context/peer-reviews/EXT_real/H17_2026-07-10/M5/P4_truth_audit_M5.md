# P4 M5-EXT truth-audit — v1.0.239 (2026-07-12) — STRICT ledger-first

**Raws audited (read verbatim, in full):**
- `EXT_real/H17_2026-07-10/M5/P4_grok_M5.md` — VERDICT: **MINOR REVISIONS** (4 MINOR)
- `EXT_real/H17_2026-07-10/M5/P4_chatgpt_M5.md` — VERDICT: **REJECT** (12 MAJOR + 1 MINOR)

**Version note:** the M5 raws were run on the served v1.0.238 PDF. The live `.tex` on disk
is now **v1.0.239** (L55 `\paperVersion{v1.0.239}`), whose only content delta over v1.0.238 is
the OpenAI-INT P4-E7 closure in the folded §VI B e2e paragraph (probability-level antisymmetry
vs. argmax flip-recovery rate; no number changed — ledger head + tex comment L58-71). No M5-EXT
finding touches that paragraph, so v1.0.238-vs-v1.0.239 drift is immaterial to this audit.

**Cross-check:** the M5-INT wave on this same v1.0.238→239 already found **1 genuinely-new
correctness item (OpenAI P4-E7, CLOSED-BY-EDIT)** and 0 others; every other INT finding a
source-cited standing re-flag (ledger head, L1-2). This M5-EXT audit is independent and lands
**0 genuinely-new EXT** — every Grok MINOR and every ChatGPT MAJOR/MINOR is a source-cited
re-flag of a standing D-id or an honestly-disclosed limitation, verified against the live `.tex`.

**ledger_match.py DRAFT** (conservative fingerprint pre-match, NOT authoritative) was
Opus-adjudicated below; every UNMATCHED finding independently source-verified against
`pipelines/p2_chirality/chirality_catalog_paper.tex` (grep evidence cited inline).

The Grok raw `ISSUES:` region and the ChatGPT `(2) ISSUES:` header are parse artifacts, not findings.

---

## RAW 1 — EXT Grok (MINOR REVISIONS)

| # | sev | verdict | D-id / .tex evidence | reason |
|---|-----|---------|----------------------|--------|
| 1 | — | HEADER ARTIFACT | — | `VERDICT: MINOR REVISIONS` / `ISSUES:` header lines — parse artifact, not a finding. |
| 2 | MINOR | RE-FLAG-DISCLOSED | **DP4-17** | "forward model accounts for only ~53% … ~47% open item; add a single consolidated paragraph quantifying the max allowed cosmological dipole fraction in the unmodeled remainder." The paper already discloses the 47% remainder AND bounds it a-fortiori below A50/A95: abstract L659 ("~47% of the post-MASTER amplitude an explicit open item that lies below A95 and does not affect the primary null"); §pseudolabel_independence L1104 explicit ceiling `|A_inh| ≲ A95 ≲ 1.5% (f_CW units; ≲3×10⁻² A_p units)`; §monopole_mask_null L1050. A *consolidated single-paragraph* joint real-space×harmonic likelihood is the standing OPEN-COMPUTE future-work item (DP4-17), not editable now. Presentation-preference re-flag on disclosed content. |
| 3 | MINOR | RE-FLAG-DISCLOSED | **DP4-01** (+DP4-11) | "amplitude-tension 1.7–4% stated clearly … 'disfavors a clean A_ref=0.017 dipole at z≈−7.6' could be misread as statistical confrontation; tighten to 'amplitude comparison under the present equivariant pipeline' vs 'statistical exclusion.'" The paper ALREADY does exactly this: abstract L676 "an amplitude-level comparison, not a frequentist exclusion of Shamir's distinct Ganalyzer estimator … a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion" (DP4-11); §methods L738/L1471 "template-model-disfavor statistic … not a calibrated detection significance … 'disfavors,' not 'excludes at 7.6σ'"; the factor-of-2 double-count is CLOSED-BY-EDIT (DP4-01, A_ref 0.034→0.017). The exact caveat Grok requests is verbatim in the paper. Referee-variance re-flag of disclosed language. |
| 4 | MINOR | RE-FLAG-DISCLOSED | **DP4-07** (+DP4-21) | "pre-specification via git commit hash is excellent; add explicit statement that the exact commit / frozen snapshot used for all quoted numbers, masks, null distributions is permanently archived alongside the public catalog release." Prospective-registration praise + an archival-freeze ask. §prereg L713 declares the a-priori primary sample (DP4-07); the immutable commit-hash / Zenodo-DOI minting is Houston-gated at journal submission (DP4-21, cannot fabricate a hash/DOI now). Disclosed + venue-gated, not editable now. |
| 5 | MINOR | RE-FLAG-DISCLOSED | **DP4-13** | "add a short 'reader's guide' paragraph immediately after the abstract stating in plain language that the cosmological conclusion rests solely on rows P1–P2 of Table I; all harmonic-channel σ values are systematics diagnostics." Pure presentation/accessibility preference. The paper ALREADY carries this exact primary-vs-diagnostic split: Table I decision-tree tags each row `PRIMARY`/`DIAGNOSTIC` (L746-769); L776 "The scientific verdict rests solely on the two rows tagged PRIMARY … every DIAGNOSTIC row is, by design, a systematics characterization"; §notation σ-not-comparable reader's note (L776/L822). The v1.0.237 directive-M overhaul already closed the presentation half of DP4-13. Adding one more boxed restatement = referee-taste OPINION on an already-foregrounded structure. Not a defect. |

**Grok closing one-sentence (raw l.10):** *"The central claim that the large-scale chirality
dipole is consistent with null at sub-percent sensitivity (with prior claims likely
systematics-driven under improved methodology) is robustly supported."*
→ Grok itself **affirms the central null holds**; MINOR REVISIONS = presentation polish only
(pattern-066 severity-on-presentation), zero editable science defect.

---

## RAW 2 — EXT ChatGPT (REJECT)

| # | sev | verdict | D-id / .tex evidence | reason |
|---|-----|---------|----------------------|--------|
| 1 | MAJOR | RE-FLAG-DISCLOSED | **DP4-07** (+DP4-13 title) | "p_eq>0.6 primary sample not demonstrably independent of the result; [0.5,0.6) bin excess; a code commit is not a timestamped preregistration; title misleading (uses <1M spirals not 8.5M)." Verbatim DP4-07: §prereg L713 declares HC 0.6 as the single a-priori primary sample; the [0.5,0.6) DECaLS-concentrated excess is disclosed as a footprint-correlated systematic (L1445); the GZ1-human-only cross-check with NO confidence model returns the same null z=−0.54 (L1104), so the result does not depend on the cut. Title "8.5 Million DESI Galaxies" (L649) is the catalog scale; the abstract L659 states the primary N≈9.5×10⁵ prominently and Table I distinguishes 8.47M/3.2M/9.5×10⁵ (DP4-13, presentation half CLOSED v1.0.237). Post-selection concern disclosed. |
| 2 | MAJOR | RE-FLAG-DISCLOSED | **DP4-09** (+DP4-01) | "claimed sensitivity to a physical 1.7% dipole contradicts the paper's own transfer calc; injections into the hard-label field not true chiralities; g=2a−1≃0.398 ⇒ a physical 1.7% appears at ~0.68% < A50; WLS-transfer ⇒ ~1.4σ not 7.6σ." This is the DP4-19 definitional re-frame built on the g-dilution: the paper states injections do NOT traverse ViT/triage/confidence (A50/A95 are thresholds on the *observed* f_CW field, explicitly "we do not claim them as physical morphology-dipole thresholds," §sensitivity L1078=DP4-09), and g=2a−1 is the *disclosed* single dilution bridge folded into the floors (L720/L874/L1104). The "1.4σ under g" arithmetic subsumes into the paper's own statement that z≈−7.6 is a template-*disfavor* statistic, NOT a detection significance (L676/L738/L1471=DP4-01/-14). No fabrication; injection scope + z-semantics disclosed. |
| 3 | MAJOR | RE-FLAG-DISCLOSED | **DP4-09** | "detection-efficiency thresholds misused as amplitude bounds; A95 is a 95%-recovery threshold not a confidence upper limit, yet the residual/pseudo-label/cosmological contribution is inferred to lie below A50/A95; failure to detect ≠ upper bound; needs a likelihood + coverage-validated upper limit." UNMATCHED by fingerprint → source-verified DP4-09. The paper states the A95 caveat VERBATIM in ChatGPT's own words: L676 "A95∈(1.0%,1.5%], a 95%-recovery threshold rather than a frequentist confidence upper limit." The a-fortiori bound is disclosed AS a recovery-efficiency argument, not claimed as a coverage-validated CL upper limit (§sensitivity L1078); the full likelihood/coverage construction is the standing OPEN-COMPUTE joint-nuisance likelihood (DP4-17). Statistical-philosophy re-flag of a caveat the paper already carries. |
| 4 | MAJOR | RE-FLAG-DISCLOSED | **DP4-16** | "primary null + injection distributions assume exchangeability the survey doesn't possess; pixel/label permutation ignores count-dependent variances, spatially varying confusion, clustering, survey-correlated errors; needs conditional randomization / validated spatial covariance / realistic isotropic mocks." Verbatim DP4-16: the paper discloses the exchangeability limit of shuffle nulls (L676 corollary; L1104 "cannot by themselves test independence from … inherited structure"), runs a density-stratified null (+3.80σ) and the template-agnostic block-bootstrap + injection floor which don't assume exchangeability; the full generative hierarchical null is genuine future work (DP4-16, OPEN-COMPUTE). Disclosed + partially mitigated. |
| 5 | MAJOR | RE-FLAG-DISCLOSED | **DP4-14** (+DP4-01/-07) | "Appendix-D block-bootstrap WLS is not a calibrated exclusion test and not on the primary sample; (A−0.017)/σ_boot centered on the observed estimate not sims under A=0.017; amplitude positive/nonlinear; WLS uses full Catalog C not p_eq>0.6; rank-deficient nuisance design; no validated confusion model." Verbatim DP4-14: the "not a calibrated frequentist exclusion significance" caveat is stated throughout (L676/L738/L1471/L1501 fig caption); the rank-deficiency IS disclosed and audited (L1471 "X^T W X is exactly rank-8, condition number 4.5×10¹⁶ … SVD-pseudoinverse / leg-drop / Gram-Schmidt refits all reproduce A_best=4.55×10⁻³"); the full-Catalog-C-vs-HC-sample distinction is the disclosed convention (WLS is the template-fit estimator; HC is the real-space estimator; both PRIMARY, Table I L746-767). Standing re-flag of a disclosed caveat. |
| 6 | MAJOR | RE-FLAG-DISCLOSED | **DP4-17** | "unresolved full-sample + harmonic signals can't be disposed by declaring an estimator hierarchy; full-sample real-space rejects the null, several harmonic analyses reject their nulls, ~47% ℓ=1 residual unexplained; different masks ≠ scientifically unrelated; a joint simulation must propagate one physical dipole + systematics through all channels; additive systematic can oppose/partially cancel a real signal." Verbatim DP4-17: the 47% remainder is disclosed (L659/L1050), harmonic is framed diagnostic-not-independent (L776), and the joint real-space×harmonic covariance/likelihood is the standing OPEN-COMPUTE future-work item. The vector-cancellation point is disclosed at L1104(ii) (bias direction argued toward-null for survey-correlated inheritance; the primary HC null is stated conservative against additive bias). Re-flag + OPEN-COMPUTE. |
| 7 | MAJOR | RE-FLAG-DISCLOSED | **DP4-15** (+DP4-08) | "classifier validation insufficient for sub-percent; 2/3 training labels are CE-ResNet pseudo-labels so 93.7% val-accuracy measures agreement with the pseudo-label source; GZ1 gives only 69.91% chirality accuracy; sky stratification too coarse to exclude RA/depth/morphology-dependent differential error; TTA guarantees flip-swap consistency not spatially unbiased hard labels." Verbatim DP4-15 (+DP4-08): 66.5% CE-ResNet pseudo-label fraction disclosed (L720 "validation metrics … partially reflect agreement with CE-ResNet"); 69.91% GZ1 accuracy / κ=0.40 disclosed and propagated as a conservative dilution floor (L720/L874); flip-TTA labeled flip-equivariance ONLY, explicitly not rotation/spatial-null (L838=DP4-08); the spatially-resolved confusion map is the standing OPEN-COMPUTE item (DP4-15). Disclosed limitation. |
| 8 | MAJOR | RE-FLAG-DISCLOSED | **DP4-13** (+DP4-10) | "LEE / tail-probability internally inconsistent: local max 3.05 moment-σ assigned direct-MC p_LEE≤10⁻⁴ while Bonferroni says <1σ; Bonferroni doesn't require independence; reporting +3.64σ when empirical p=0.030, or +7.93σ when rank-p=3×10⁻⁴, is misleading — call them moment-z." UNMATCHED → source-verified. The paper is NOT internally inconsistent: L1439 states the direct-MC max-statistic null (p_LEE≤10⁻⁴) IS the principled look-elsewhere control, and explicitly downgrades Bonferroni to "a qualitative cross-check … Bonferroni formally assumes independence, which the strongly correlated overlapping-hemisphere grid does not guarantee" — i.e. the paper ITSELF makes ChatGPT's Bonferroni point and does NOT rely on Bonferroni (L377 comment: "Bonferroni/BH layer dropped to heuristic cross-check only; direct-MC max-statistic null is the principled control"). moment-z is explicitly declared non-Gaussian (L822 §notation; DP4-10/-13). The σ-vs-empirical-p labeling is the disclosed σ-incommensurability reader's note (DP4-13, presentation half CLOSED v1.0.237). Re-flag of an already-downgraded heuristic + disclosed labeling. |
| 9 | MAJOR | RE-FLAG-DISCLOSED | **DP4-13** (+DP4-01) | "amplitude conventions not consistently applied: paper defines A=A_p=2(f_CW−½) and Table VIII uses that; §VI A describes A95≤1.5% as being in 'f_CW units' and converts to 3×10⁻² in A_p units — a factor-of-two inconsistency." UNMATCHED → **source-verified as INTERNALLY CONSISTENT, not a defect.** The §pseudolabel_independence ceiling (L1104) reads: `|A_inh| ≲ A95 ≲ 1.5% (f_CW units; ≲3×10⁻² in A_p units)`. With A_p=2(f_CW−½), an f_CW-*deviation* of 1.5% (f_CW−0.5=0.015) maps to A_p=0.03=3×10⁻² — the factor-of-2 is CORRECT and EXACTLY the paper's stated convention, not a contradiction. The distinct "no factor-of-two rescaling" statement (L676/L738/L1471) is about *Shamir's asymmetry already being a full-count (N_CW−N_CCW)/(N_CW+N_CCW)=A_p* quantity, a different object from an f_CW-deviation — no conflict. ChatGPT conflates a full-count asymmetry (=A_p) with an f_CW-deviation (=½A_p). Naming both "1.5%" without a units tag in one clause is at most a DP4-13 presentation nit; the arithmetic is right. NOT a genuinely-new reader-visible error. |
| 10 | MAJOR | RE-FLAG-DISCLOSED | **DP4-11** | "the '99.32% monopole–mask leakage reproduction' is overinterpreted; obtained for an un-monopole-subtracted field where a nonzero constant through a patchy mask necessarily produces deterministic pseudo-C_ℓ leakage; does not explain monopole-subtracted/MASTER-decoupled (only ~12%); can't criticize prior estimators without matched footprint/weighting; restrict or remove the broad conclusions." Verbatim DP4-11: the paper already restricts 99.32% to "the un-deconvolved pre-MASTER pseudo-C_ℓ" (L1050 bold), states the post-MASTER monopole-only null reproduces only ~12% (L1050), and hedges the literature attribution to "under our DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required" (L1050). Every restriction ChatGPT asks for is already in the text. Re-flag. |
| 11 | MAJOR | RE-FLAG-DISCLOSED | **DP4-12** | "§VI C connection to fundamental parity-violating models unsupported; no transfer function from birefringence / chiral GW / Chern-Simons to spiral-arm winding; statements that such mechanisms 'generically' align angular momenta or that this measurement constrains them must be deleted." Verbatim DP4-12: §parity_translation (~L1173) already states the transfer function "is not derived in this paper" and frames these as "in principle" / "pending a derived transfer function"; INT OpenAI-8 agreed it should be downgraded and the text already hedges. Existing hedge kept. Re-flag. |
| 12 | MAJOR | RE-FLAG-DISCLOSED | **DP4-21** | "numerical analysis not frozen in a reviewable archival record; mutable live branch; DOI + exact commit hashes 'supplied later'; internal artifact paths not in the paper; requires immutable tag/DOI + checksums + executable reproduction workflow before review." Verbatim DP4-21 (OPEN-VENUE / Houston-gated): the commit hash + Zenodo DOI are minted at journal submission (Data Availability ~L1441); cannot fabricate a hash/DOI now. The prereg sample is already declared a priori (§prereg L713). Venue-gated, not editable now. |
| 13 | MINOR | RE-FLAG-DISCLOSED | **DP4-13** | "requires substantial compression/restructuring; same caveats/results repeated; incompatible field/mask/weight conventions interleaved; internal-development language ('pod-deferred,' 'anchor battery,' 'operative ceiling') obscures the argument; state one primary sample, one likelihood, one amplitude convention, one systematic model, secondary diagnostics to a concise supplement." Verbatim DP4-13: the v1.0.237 directive-M overhaul already collapsed the 5-para abstract → one PRD paragraph, de-duplicated the σ-not-comparable caveat (33→canonical §notation cross-refs), and foregrounded one-primary narrative (ledger DP4-13 CLOSED-BY-EDIT presentation half). Residual = referee-taste on an already-tabulated/cross-ref'd structure (OPINION). Not a defect. |

**ChatGPT closing (raw l.109):** *"No — the manuscript shows that one selected high-confidence
observed-label estimator is consistent with zero, but it does not support the broader physical null,
sub-percent sensitivity, or exclusion claims."* = the standing ChatGPT structural harsh-referee
REJECT floor (directive-H / pattern-066), identical to H17F / W1 / FR1b P4 ChatGPT REJECTs. Every
MAJOR is statistical-philosophy or scope on honestly-disclosed content — none a new editable defect.

---

## Summary

**P4 M5-EXT genuinely-new: 0**

- **Grok (MINOR REVISIONS):** 4 MINOR, all source-cited re-flags → **DP4-17, DP4-01(+DP4-11),
  DP4-07(+DP4-21), DP4-13**. Grok's closing sentence affirms the central null is *"robustly
  supported"*; MINOR = presentation polish (pattern-066), zero editable science defect.
- **ChatGPT (REJECT):** 12 MAJOR + 1 MINOR, all source-cited re-flags → **DP4-07, DP4-09, DP4-09,
  DP4-16, DP4-14, DP4-17, DP4-15, DP4-13, DP4-13, DP4-11, DP4-12, DP4-21, DP4-13**. Standing
  ChatGPT harsh-referee structural floor; every MAJOR is disclosed / OPEN-COMPUTE / OPEN-VENUE /
  definitional-reframe.

**UNMATCHED-by-fingerprint resolved (all VERIFIED against live `chirality_catalog_paper.tex`):**
- ChatGPT #3 (thresholds-as-amplitude-bounds) → **DP4-09** (L676 verbatim "95%-recovery threshold
  rather than a frequentist confidence upper limit"; L1078 injection scope; full-likelihood ask = DP4-17).
- ChatGPT #8 (LEE/Bonferroni internal inconsistency) → **DP4-13** (+DP4-10) — the paper ITSELF
  downgrades Bonferroni to a non-principled cross-check and names the independence caveat (L1439/L377);
  direct-MC max-statistic p_LEE≤10⁻⁴ is the principled control; moment-z declared non-Gaussian (L822).
- ChatGPT #9 (A_p vs f_CW factor-2 convention) → **DP4-13** (+DP4-01) — **source-verified consistent,
  not a defect**: `1.5% f_CW-deviation → 3×10⁻² A_p` is exactly A_p=2(f_CW−½) (L1104); the "no
  rescaling" clause (L676/L1471) is about Shamir's full-count *asymmetry* being A_p directly, a
  distinct object. ChatGPT conflated the two. At most an untagged-units nit.
- ChatGPT #13 (organization) → **DP4-13** (presentation half CLOSED-BY-EDIT v1.0.237).
- Grok #1 header / ChatGPT `(2) ISSUES:` header = parse artifacts, noted not dispositioned.

**Cross-check consistency:** the M5-INT wave on the same v1.0.238→239 found 1 genuinely-new
correctness item (OpenAI P4-E7, CLOSED-BY-EDIT in the v1.0.239 fold) + 0 others. This M5-EXT audit
independently lands **0 genuinely-new EXT**; the single genuinely-new item of the M5 wave (P4-E7) is
**already fixed in the v1.0.239 tex on disk** (ledger head L1-2). No further edit is triggered by
M5-EXT.

## Integrity statement

Both EXT raws read verbatim, in full, before any disposition (Grok l.1 `VERDICT: MINOR REVISIONS`;
ChatGPT l.1 `(1) VERDICT: REJECT`). No ACCEPT faked. No finding dismissed without a source-cited
verdict — every disposition cites a D-id AND/OR a specific `chirality_catalog_paper.tex` line
verified THIS session. No math fabricated. No hedging removed. Every UNMATCHED-by-fingerprint
finding was source-verified against the live `.tex`, not assumed (grep evidence inline). The
ChatGPT #9 "factor-of-two inconsistency" MAJOR was arithmetically checked (A_p=2(f_CW−½) ⇒
1.5% f_CW-dev = 3×10⁻² A_p) and found **correct/consistent**, not an error. The
Grok-MINOR / ChatGPT-REJECT verdict split is the documented LLM harsh-referee structural floor
on honestly-scoped, disclosed content (directive-H) — not editable defects.

**No further bump from M5-EXT; v1.0.239 stands** (the M5-wave genuinely-new item P4-E7 is already
closed in v1.0.239). `directive_g.sh` NOT re-run for M5-EXT (no EXT-triggered edit).
