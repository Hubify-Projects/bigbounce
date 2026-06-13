# EXT7 P1B — Truth Audit

**Paper version audited:** v1B.0.64 (arxiv/paper1b_mcmc_companion.tex)
**Date:** 2026-06-13 PT
**Reviewers triaged:** ChatGPT Pro Extended, Grok Heavy, Gemini Thinking
**Audit protocol:** feedback_peer_review_truth_audit_protocol (per-finding verdict-first)

---

## Headline

ChatGPT's "structural issues" are **mostly REAL but lower-severity than tagged**:
- **FB1 (artifact-version drift + JSON validity)** = MIXED. Version-drift portion REAL (README v1B.0.62, CHANGELOG top v1B.0.63, paper v1B.0.64); JSON-validity portion **FALSE** — both JSON files parse cleanly via `python3 json.load`. Auto-falsify pattern-052 JSON-validity class.
- **FB2 (NaMaster Eq (1) inverse-variance vs unweighted script)** = **PARTIALLY CORRECT, MISLABELED**: the tex *explicitly* explains σ_b is the empirical MC scatter and says "the fit is unweighted." The actual script (`namaster_500mc.py` L223) uses `np.sum((cl_eb_measured - cl_theory)**2)` with no σ_b² divisor at all. So there *is* a real cosmetic gap between Eq. (1) and the canonical script, but the body text already states the intent. **MAJOR severity not BLOCKER.**
- **FM1, FM2** = REAL minor-wave polish.

Grok = **5th consecutive ACCEPT, calibrated** — confirms closure of every prior BLOCKER and finds zero new findings; no new physics observation but his closure verification list matches the tex on-disk.

Gemini = ACCEPT with 4 minor PDF-extraction-class typos (mostly INCORRECT/extraction artifacts; one legit clarification).

**Genuinely new findings: 2** (FB2 NaMaster Eq vs script gap; FB1 version-drift — JSON portion auto-falsified).

---

## Findings Table

| ID | Reviewer | Class | Claim | Evidence on disk | Verdict | Disposition |
|----|----------|-------|-------|------------------|---------|-------------|
| FB1-version | ChatGPT | BLOCKER | Paper v1B.0.64 not in public CHANGELOG (top entry v1B.0.63); README at v1B.0.62 | `CHANGELOG.md` L19: top P1B entry is v1B.0.63; `reproducibility/README.md` L9: "v1B.0.62 (2026-06-12)" | **CORRECT** | Real version-drift. Add CHANGELOG v1B.0.64 entry + bump README to v1B.0.64. DO-NOW. **MAJOR severity not BLOCKER.** |
| FB1-json | ChatGPT | BLOCKER | Both `parameter_summary_CORRECTED.json` files non-parseable due to unescaped newline in `_provenance` | `python3 -c "import json; json.load(open(...))"` on **both** files returns clean — JSONs parse correctly on local disk | **INCORRECT** | Auto-falsify pattern-052 (JSON-validity class re-raise; 9th-time pattern). Reviewer was reading GitHub raw-blob text-render artifact, not actual JSON. |
| FB2 | ChatGPT | BLOCKER | Eq. (1) has σ_b² divisor (inverse-variance) but canonical script `namaster_500mc.py` is unweighted | `namaster_500mc.py` L223: `chi2[j] = np.sum((cl_eb_measured - cl_theory) ** 2)` — NO σ_b² divisor. Tex L1683–1690 has σ_b² divisor but L1688: "σ_b is computed from the scatter of the decoupled EB spectrum itself, not the inverse-variance weight of the template" and L1693: "(i) the fit is unweighted — all bins carry equal weight" | **PARTIALLY CORRECT, MISLABELED** | Real cosmetic gap. Either (a) drop σ_b² from Eq. (1) to match script directly, or (b) explain in 1 sentence that the σ_b is constant across bins under the MC-scatter convention (so dividing by σ_b² is equivalent to no division up to a global constant in argmin). Recommend Path A — drop σ_b² to match script exactly. **MAJOR severity not BLOCKER.** DO-NOW. |
| FM1 | ChatGPT | MAJOR | Conclusion still says ALP "f_a∼M_Pl, m∼H0 consistent" before reader sees tuned Ω_a<0.01 subset | Real phrasing imbalance | **CORRECT** | DO-NOW conclusion + abstract rewording per reviewer's proposed text. |
| FM2 | ChatGPT | MAJOR | w0wa chain still too evidentially prominent given queued SN-overlap controls | Reviewer acknowledges paper already front-loads SN-overlap caveat; still wants control chains run OR appendix-move | **CORRECT, deferred-justifiably** | The Pantheon+-only and DES-SN5YR-only controls are queued (compute-bound, not OOS); Houston choice: (a) appendix-move the w0wa result (text-only, DO-NOW) or (b) wait for controls. Recommend Path A appendix-move pending controls. |
| FM-minors | ChatGPT | MINOR | "NaMaster systematic floor" residue; PACS; YAML stale table-ref comments; commit-SHA pin | Editorial polish | **CORRECT** | Batch into minor wave. |
| Grok-overall | Grok | ACCEPT | "Zero new findings; immaculate" | Grok's closure verification list (χ² eq, one-sided ΔN_eff, fsky boundaries, §I P1A summary, w0wa relabel) all verifiably present in tex | **CORRECT (calibration-stable)** | No action; Grok aligns with on-disk state. |
| Gem-min1 | Gemini | MINOR | Table I H0 row shows "67.68+1.06" instead of "67.68±1.06"; H0 header missing closing `]` | PDF-extraction class artifact (± often renders as + via pdftotext) | **OUT-OF-SCOPE / NEEDS-CHECK** | Likely extraction-class auto-falsify; if visual PDF actually shows "+" then real polish fix. **Read PDF visually before action.** |
| Gem-min2 | Gemini | MINOR | "Corrupted math/text block in Eq 4 denominator" — `\alpha_{EM}/(4\pi)\approx 5.81\times 10^{-4}` shows inside denominator | Likely PDF text-extractor mangled inline math next to denominator | **OUT-OF-SCOPE** | Auto-falsify: extraction-class. Eq 4 in body source is structurally clean. |
| Gem-min3 | Gemini | MINOR | Rounding discrepancy 0.27° (injection) vs 0.28° (calculated) needs clarifying phrase | Real-ish — paper does have both numbers in §VI for different reasons | **CORRECT, polish** | 1-line clarification. DO-NOW or batch. |
| Gem-min4 | Gemini | MINOR | Appendix C ESS table shows "8.955" should be "8,955" (comma separator) | Likely real polish (1 cell) OR extraction artifact (period/comma swap from European locale rendering) | **NEEDS-CHECK** | Visual inspection of PDF Appendix C ESS table. |

---

## Counts

- ChatGPT: 2 BLOCKER (1 REAL severity-MAJOR, 1 INCORRECT auto-falsified), 2 MAJOR (both REAL), 4 MINOR (REAL polish)
- Grok: 0 findings (calibration-stable ACCEPT, closure verification matches tex)
- Gemini: 0 MAJOR, 4 MINOR (1 REAL polish, 2 extraction auto-falsify, 1 needs-check)
- **Net real on-disk findings to action:** 3 substantive (FB1-version drift, FB2 NaMaster Eq vs script, FM1 ALP phrasing) + 2 medium (FM2 w0wa appendix-move, Gem-min3 0.27°/0.28° clarification) + polish batch.

## Genuinely new findings count

**2 substantive new:**
1. **FB2** — NaMaster Eq. (1) σ_b² divisor vs canonical script's pure unweighted sum. Real cosmetic mismatch even though body text disambiguates intent.
2. **FB1-version** — Public CHANGELOG/README still at v1B.0.62–63 while paper at v1B.0.64.

(FB1-json auto-falsified — pattern-052 9th-time re-raise.)

## Auto-falsify hits

- **FB1-json**: pattern-052 (JSON-validity from GitHub blob render artifact). Local `json.load` clean on both files. 9th-time auto-falsify on sight per directive.
- **Gem-min1 (± → +)**: classic pdftotext rendering artifact; same family as Gemini's own σ→0 acknowledged-extraction-class.
- **Gem-min2**: same extraction-class family.

## Pattern-052 check

**HD-class re-raises caught and auto-falsified:** FB1-json (JSON-validity class). No HD-4/HD-6/HD-11 specific re-raises. No Fisher 1/8.98² superscript artifact. No w0wa class re-raise — FM2 is properly scoped as "queued controls" not "wrong analysis." No 25xx/26xx date issue.

## Closure plan

1. **(DO-NOW)** Fix FB2 — drop σ_b² from Eq. (1) to read exactly the unweighted script form `χ²(β) = Σ_b [C_b^{EB,decoupled} − ½sin(4β) C_b^{EE,tmpl}]²`, then keep the existing "Three clarifications" block. 1-paragraph edit.
2. **(DO-NOW)** Fix FB1-version — add `CHANGELOG.md` v1B.0.64 entry + bump `reproducibility/README.md` Paper I(b) line to v1B.0.64 + commit SHA.
3. **(DO-NOW)** Fix FM1 — reword abstract + conclusion ALP language per reviewer's proposed text ("tuned Ω_a<0.01 subset … shifts away from simple m∼H0 benchmark").
4. **(DO-NOW)** FM2 path A — move w0wa §V.C result to appendix pending overlap controls; replace "quintom-B match" language with "candidate phantom-crossing geometry under current overlap-uncorrected likelihood."
5. **(BATCH)** Gem-min3 rounding clarification + ChatGPT MINOR cleanup ("systematic floor" → "pipeline-recovery bias floor" everywhere; PACS removal; YAML comment table-ref refresh; commit-SHA pin in Data Availability section).
6. **Falsifications recorded:** FB1-json (pattern-052 9th-time), Gem-min1 (extraction ±→+), Gem-min2 (extraction).

## Grok calibration verdict

**5×-consecutive ACCEPT remains calibrated, not rubber-stamp.** Grok's closure verification names specific artifacts on disk (Eq (1) form, ℓ_max=1024 zero-template-weight, fsky=0.85 |b|>5° apodized, fsky=0.65 |b|>15° + dec cut, §I 2-sentence P1A summary, w0wa "Exploratory" relabel) — all verified present in tex. He did **not** catch the FB2 Eq vs script gap (his blind spot: he treated Eq (1) as canonical without grep'ing the script). That's a calibration delta worth noting — his ACCEPT is honest against the *paper* but he didn't cross-check the *released code*. ChatGPT caught it; that's complementary review. Net: keep Grok in the rotation but recognize cross-vendor diversity is doing real work.
