# EXT6 P1B — Truth Audit

**Round**: EXT6 (external delta round 6 — 3-vendor: ChatGPT Pro Extended, Grok Heavy, Gemini Thinking)
**Paper**: 1B (`arxiv/paper1b_mcmc_companion.tex`)
**Version reviewed**: v1B.0.62 (PDF hash `e0066b42`, dated 12 June 2026 PDT)
**Audit date**: 2026-06-12 PT
**Reports**:
- `project-context/peer-reviews/EXT6_P1B_ChatGPT.md` — MAJOR REVISIONS (2 BLOCKERS, 4 MAJORS, 4 MINORS)
- `project-context/peer-reviews/EXT6_P1B_Grok.md` — ACCEPT (0/0/0 — zero findings)
- `project-context/peer-reviews/EXT6_P1B_Gemini.md` — ACCEPT (0/0/2 minors)

**Verdict schema**: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION
**Auto-falsify rules applied**: June 2026 current; HD-4 (Zenodo tagged release) and HD-11 (DOI placeholders) ruled; pattern-052 (prior-falsified re-raise must cite primary evidence to auto-rescue); w₀wₐ caveat-front-load is deliberate framing not a finding.

---

## Findings table

| # | Leg | Finding (severity) | Verdict | Evidence (tex lines / artifact paths) | Disposition |
|---|-----|--------------------|---------|---------------------------------------|-------------|
| 1 | ChatGPT FB1(a) | Public reproducibility README still labels Paper I(b) as v1B.0.61, not v1B.0.62 (BLOCKER, sub-claim) | **VERIFIED** | `reproducibility/README.md` L9: `**Paper I(b) version:** v1B.0.61 (2026-06-12)`. Tex `\paperVersion{v1B.0.62}` at L122. Real surface drift. | **FIX (cheap)**: bump README L9 to `v1B.0.62 (2026-06-12)` in next closure commit. Same-commit with version bump. |
| 2 | ChatGPT FB1(b) | Root `CHANGELOG.md` has no v1B.0.62 entry; current top entry is v1B.0.61 (BLOCKER, sub-claim) | **VERIFIED** | `CHANGELOG.md` L19 starts at `### v1B.0.61 (2026-06-12) — EXT5 external-round closure wave`. No v1B.0.62 block. Paper §Data and Code Availability L2331-2332 says URLs "are also recorded in the repository CHANGELOG.md under the entry for \paperVersion" — that entry is missing. Real cross-surface mismatch. | **FIX**: add v1B.0.62 changelog block citing the EXT5/R35conf closure-wave commit SHA, dataset URLs, and SHA-256 checksums of the two CORRECTED JSON artifacts. |
| 3 | ChatGPT FB1(c) | Both `parameter_summary_CORRECTED.json` files appear to be invalid JSON because the `_provenance` string spans a raw newline (BLOCKER, sub-claim) | **FALSIFIED** | `python3 -c "import json; json.load(open(...))"` on both `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/parameter_summary_CORRECTED.json` and `.../planck_bao_sn_20260312_1954/diagnostics/parameter_summary_CORRECTED.json` returns 0 errors. Both files parse cleanly. ChatGPT misread a multi-line rendered display as a raw-newline JSON. pattern-026 / GitHub-blob view artifact. | **NO ACTION**. |
| 4 | ChatGPT FB1(d) | Submission-day Zenodo DOI / tagged release pending | **HOUSTON-DECISION** | Tex §Data and Code Availability L2329-2330: `"DOI assignment is pending (identifiers will be inserted at submission)"`. HD-4 (Zenodo tagged release) + HD-11 (DOI placeholders) ruled this is a legitimate pre-submission state. | **DEFER**: insert DOI + tag at arXiv-submission moment. Not a same-commit blocker. |
| 5 | ChatGPT FB2 | Tex §III claims `bbn_predictor: 'PArthENoPE'` is explicitly declared in `theory.camb.extra_args` of each Cobaya YAML; flag is absent from public YAMLs (BLOCKER) | **VERIFIED** | Tex L1055-1058: `"CAMB uses its PArthENoPE-derived BBN-consistency module by default (explicit Cobaya/CAMB flag: \texttt{bbn\_predictor: 'PArthENoPE'}, declared at the \texttt{theory.camb.extra\_args} block of each \texttt{cobaya\_*.yaml}, pinning the BBN predictor for absolute reproducibility)"`. Grep over all 4 `reproducibility/cosmology/cobaya_*.yaml`: extra_args contains only `lens_potential_accuracy: 1`, `num_massive_neutrinos: 1`, `theta_H0_range: [40, 100]`. NO `bbn_predictor` key in any YAML. Real claim/artifact mismatch — exactly the failure mode the artifact-pinning standing pattern guards against. | **FIX (Path C — full hard fix)**: add `bbn_predictor: PArthENoPE` to `theory.camb.extra_args` in all 4 YAML files (`cobaya_planck.yaml`, `cobaya_planck_bao.yaml`, `cobaya_planck_bao_sn.yaml`, `cobaya_full_tension.yaml`). Re-run a short sanity chain to confirm no numerical change (BBN-consistent is CAMB default, so byte-identical expected). Note in CHANGELOG that the flag is now explicit. |
| 6 | ChatGPT FM1 | §V.B w₀wₐ paragraph still calls $w_0\!+\!w_a\!=\!-1.48\!\pm\!0.15$ "the canonical quintom signature" / "headline result" despite front-loaded overlap caveat in §III (MAJOR) | **PARTIAL / OPINION** | Tex L1863: `"The headline result is $w_0 = -0.812 \pm 0.044$ ... with $w_0+w_a = -1.48 \pm 0.15$ requiring phantom crossing (the canonical quintom signature)."` §III front-loads the SN-overlap caveat (per EXT5 closure). Whether to retain "canonical quintom signature" / "headline" in §V.B after the §III caveat is a stylistic-rhetorical call: ChatGPT's preferred "exploratory overlap-uncorrected w0wa cross-check" is fully defensible; the current phrasing is also defensible given that §III already caveats and L1228 fn:wcaveat says "marginal-tail posterior-extrapolation departure ... not a Bayes-factor or ln B exclusion." Soft-tier framing finding. | **FIX (cheap, partial)**: replace "the headline result" → "the central marginal-tail result" at L1863, and "the canonical quintom signature" → "the canonical quintom signature under the overlap-uncorrected likelihood (see §III caveat)". Section heading rename to HOUSTON-DECISION. |
| 7 | ChatGPT FM2 | ALP "at scan-prior midpoint values" phrasing misleading given fixed-$C_{a\gamma}\!=\!8$ posterior shifts to $m\!\simeq\!36H_0$ (MAJOR) | **VERIFIED** | Tex L963 (Sec. II), L1886, L2242 carry "scan-prior midpoint values". Detailed body (Eq.~3, Sec. VI) explicitly gives $m\!\simeq\!4 H_0$ to obtain $\beta\!\simeq\!0.28^\circ$ at $C_{a\gamma}\!=\!8,\theta_i\!=\!1$ — i.e. above the $m/H_0\!\in\![1,3]$ midpoint claim. Continuous-prior posterior has fixed-coupling median near $36H_0$. Real prose/calculation mismatch. | **FIX**: rephrase all three hits to "within the scan-prior envelope but near its upper-displacement/coupling edge; the posterior-supported fixed-$C_{a\gamma}\!=\!8$ fit shifts to $m\!\gg\!H_0$ (median $\simeq 36 H_0$)". One grep-and-replace pass. |
| 8 | ChatGPT FM3 | Table IV $\Omega_a\!<\!0.1$ and $\Omega_a\!<\!0.01$ rows carry qualitative placeholders ("post.-supported", "smaller-weighted", "broad") rather than weighted 16/50/84 percentiles (MAJOR) | **VERIFIED** | Tex L2179-2180: `"$\Omega_a<0.1$ ... $0.328\pm 0.100$ & post.-supported & broad & post.-supported & marginal-restricted"` and `"$\Omega_a<0.01$ (safe) ... $0.28\pm 0.10$ & post.-supported & smaller-weighted & post.-supported & marginal-restricted"`. The subset selections are real and well-defined; the table just under-reports. Legitimate audit-readability gap. | **FIX (Path C)**: compute weighted 16/50/84 percentiles for $m/H_0$, $\theta_i$, $C_{a\gamma}$ on each subset from the committed ALP chain. If subset ESS is too low for stable percentiles for a given column, replace the qualitative cell with "ESS=<n>, unreliable" not a vague adjective. One-pass post-process on existing chain. |
| 9 | ChatGPT FM4 | Public README still lists `χ²_eff | YES` while tex says χ²_eff is not reported (only Table II channel decomposition) (MAJOR) | **VERIFIED** | `reproducibility/README.md` L93: `"| χ²_eff | YES | From MCMC chain maximum likelihood; AIC/BIC/ln B NOT reported in manuscript (deferred to nested sampling) |"`. Tex L1863: `"The $\chi^2$ goodness-of-fit decomposition (BAO, CMB, SN, and total contributions) is reported in Table~\ref{tab:iter2_posterior}; the AIC, BIC, and $\ln B$ evidence metrics are \emph{not} reported there."` — the paper reports a per-channel $\chi^2$ decomposition, not a single $\chi^2_{\rm eff}$. README row label is slightly misleading. | **FIX (cheap)**: relabel README row to `"Table II channel χ² decomposition | YES"` and mark a new `χ²_eff / AIC / BIC / ln B | NO` row. Same closure commit as FB1(a). |
| 10 | ChatGPT minor — Appendix A table-reference drift (says "Table I and the Table III/Table IV reproducibility and claim-classification entries") | **VERIFIED** | Tex L2392: `"the chains and diagnostics that back Table~I and the Table~III/Table~IV reproducibility and claim-classification entries"`. Actual labels: Table I=verification, Table III=chain_datasets, Table IV=alp_restricted_subsets, Table V=claims. So Table IV is no longer a "reproducibility/claim-classification" entry — it's ALP subsets. Real drift after table inserted. | **FIX (cheap)**: rewrite to "back Table~I, Table~III, and the relevant Table~V claim-classification entries; the ALP $c5$ continuous chain backs Table~IV separately." |
| 11 | ChatGPT minor — PACS numbers remain | **HOUSTON-DECISION** | Tex L9 declares `showpacs`; L924 emits `\pacs{98.80.-k, 95.36.+x, 04.50.Kd}`. revtex4-2 PRD style retains PACS. MNRAS/JCAP would drop. HD at submission target. | **DEFER**. |
| 12 | ChatGPT minor — Abstract "pipeline systematic floor" easy to misread | **VERIFIED (cosmetic)** | Tex L891 abstract: `"forward as the pipeline systematic floor"`. Body uses both "systematic floor" and "pipeline-recovery bias floor". Reviewer wants "pipeline-recovery bias floor" everywhere — defensible polish. | **FIX (cheap)**: replace "pipeline systematic floor" → "pipeline-recovery bias floor" at L891, L1496, L1694, L1764. |
| 13 | ChatGPT minor — Version language: add commit SHA directly in §Data Availability at submission | **HOUSTON-DECISION** | Tex L2305-2316 already says version is identified by `\paperVersion` stamp + matching version-stamp commit in git log. Inserting explicit "commit: <SHA>" inline is a submission-moment decision. | **DEFER** to submission day (HD-4-adjacent). |
| 14 | Grok overall ACCEPT (0/0/0) | **MIS-CALIBRATED** | Grok says "the manuscript is flawless ... ready for immediate publication ... ZERO BLOCKERS, ZERO MAJORS, ZERO MINORS". This is a rubber-stamp ACCEPT. The audit above confirms FB1(a) README v1B.0.61 stale, FB1(b) CHANGELOG.md v1B.0.62 missing, FB2 BBN flag claim/YAML mismatch — three live, on-disk, cross-surface issues a "flawless" reading would catch. Grok's read of v1B.0.62 is artifact-blind: it only inspects the .tex body and accepts it as self-consistent without verifying against the public bundle. | **NOTE TO PATTERN CATALOG**: pattern-009 (vendor rubber-stamp) re-trigger. Grok's ACCEPT carries no audit weight on artifact-pinning class. |
| 15 | Gemini overall ACCEPT (0/0/2) | **WELL-CALIBRATED on body, ARTIFACT-BLIND on bundle** | Gemini correctly closed the 3 previous MAJORs (ALP ESS, SN overlap, Table I label corruption) and added 2 cosmetic minors. It does not look at the public bundle (README/CHANGELOG/YAMLs), so it misses FB1/FB2 — those are out-of-scope for a tex-only read. Within its scope, the ACCEPT is calibrated. ChatGPT correctly identifies the BLOCKER class because its scan extends to the GitHub repo state. | **NOTE**: Gemini's ACCEPT is real for the manuscript body. It does NOT clear the bundle. |
| 16 | Gemini minor — Add explicit caution that one-sided $\Delta N_{\rm eff}$ truncation overestimates the upper bound | **OPINION / PARTIAL** | Tex L1064-1074 already describes the renormalization procedure explicitly: `"discard the $\Delta\Neff < 0$ tail of weighted samples and rescale the surviving weights so $\int_0^\infty p \, d\Delta\Neff = 1$, then read the 95th percentile of the renormalised CDF"`. Reviewer wants a sentence calling this "highly conservative". Stylistic addition; the math is already shown. | **FIX (cheap, optional)**: add parenthetical "(this post-processing strategy is conservative when the unconstrained mode is mildly negative, as is the case here)" after L1074. |
| 17 | Gemini minor — Hubble constant units typeset as `kms^{-1}Mpc^{-1}` / `km~s^{-1}Mpc^{-1}` not MNRAS-style thin-space | **PARTIAL** | Grep finds 5 hits at L1327, L1337, L1339, L1433, L2202, all reading `km/s/Mpc`. Reviewer misquoted source. Cosmetic / journal-style choice. PRD accepts `km/s/Mpc`; MNRAS prefers `\mathrm{km\,s^{-1}\,Mpc^{-1}}$`. | **FIX at journal target lock-in**: replace per target style. HOUSTON-DECISION for now. |

---

## Counts summary

| Verdict | Count |
|---------|-------|
| VERIFIED | 8 (#1, #2, #5, #7, #8, #9, #10, #12) |
| PARTIAL | 3 (#6, #16, #17) |
| OPINION | 1 (#6 same item also has framing-OPINION component) |
| FALSIFIED | 1 (#3 JSON invalidity claim) |
| HOUSTON-DECISION | 4 (#4 DOI, #11 PACS, #13 commit SHA inline, plus #14/#15 calibration notes) |
| STALE | 0 |
| MIS-CALIBRATED ACCEPT | 1 (#14 Grok) |
| **Total findings** | **17** |

**Genuinely-NEW-substantive count (EXT6 gap metric)**: **5**
- **#2 BLOCKER** — `CHANGELOG.md` v1B.0.62 entry missing (paper text claims it exists; pattern-026 multi-site sync gap)
- **#5 BLOCKER** — `bbn_predictor: 'PArthENoPE'` claim in tex vs absent in all 4 YAMLs (artifact-pinning class, exactly the failure mode this standing pattern guards against)
- **#7 MAJOR** — "scan-prior midpoint" phrasing vs fixed-$C_{a\gamma}$ posterior $m\!\simeq\!36 H_0$ (real prose/calculation mismatch at 3 sites)
- **#8 MAJOR** — Table IV qualitative cells where weighted percentiles are computable from the committed chain (audit-readability gap)
- **#10 MINOR** — Appendix A table-reference drift after Table IV insertion (Table IV no longer reproducibility; Table V is claims)

Findings **#1, #9** (README v1B.0.61 stale; README χ²_eff label) are real but smaller bundle-resync items, not new science.

**Headline finding**: ChatGPT's two BLOCKERs are **both real artifact-pinning failures**:
1. **#2 CHANGELOG.md v1B.0.62 missing** — the paper §Data Availability promises a CHANGELOG.md entry under `\paperVersion` that does not exist. This is the classic post-bump-full-sync miss the standing directive is supposed to prevent.
2. **#5 BBN flag claim vs YAML reality** — the tex makes a *quotable explicit-flag claim* about the YAMLs that the YAMLs do not back. Either the YAMLs get the flag added (Path C, byte-identical chains expected) or the tex gets rewritten to "CAMB's default BBN-consistency setting was used; no explicit override appears in the YAMLs."

The Path-C fix (add the flag to the YAMLs and re-run a short sanity chain) is the harder/honest one and matches the manuscript's stronger reproducibility claim. The Path-A fix (rewrite tex) is acceptable but weakens the artifact-pinning posture.

**Grok ACCEPT is mis-calibrated** (pattern-009 vendor rubber-stamp). **Gemini ACCEPT is calibrated on the manuscript body** but does not check the public bundle, so it misses both BLOCKERs by scope, not by error.

---

## CLOSURE PLAN — one-line edits per VERIFIED / PARTIAL

1. **#5 BLOCKER (BBN flag, Path C)** — add `bbn_predictor: PArthENoPE` to extra_args in `reproducibility/cosmology/cobaya_{planck,planck_bao,planck_bao_sn,full_tension}.yaml`. Run a short sanity chain to confirm byte-identical numerics. Update v1B.0.62 CHANGELOG entry to note flag is now explicit.
2. **#2 BLOCKER (CHANGELOG.md v1B.0.62)** — add a v1B.0.62 block to root `CHANGELOG.md` citing this closure-wave commit SHA, the two HuggingFace dataset URLs, and SHA-256 checksums of both `parameter_summary_CORRECTED.json` files.
3. **#1 BLOCKER-sub (README version)** — bump `reproducibility/README.md` L9 from `v1B.0.61 (2026-06-12)` to `v1B.0.62 (2026-06-12)` in same commit.
4. **#9 MAJOR (README χ²_eff row)** — relabel the row to `"Table II channel χ² decomposition | YES"` and add `χ²_eff / AIC / BIC / ln B | NO`. Same closure commit.
5. **#7 MAJOR ("scan-prior midpoint")** — three-site grep-and-replace at L963, L1886, L2242.
6. **#8 MAJOR (Table IV percentiles)** — post-process the committed ALP chain to weighted 16/50/84 percentiles for each subset row; replace qualitative cells.
7. **#6 PARTIAL (§V.B framing)** — replace "headline result" / "canonical quintom signature" with caveated phrasings; keep §V.B heading unchanged unless Houston elects rename.
8. **#10 MINOR (Appendix A table-ref drift)** — rewrite L2392 to "Table~I, Table~III, and the relevant Table~V claim-classification entries; the ALP $c5$ continuous chain backs Table~IV separately."
9. **#12 MINOR ("pipeline systematic floor")** — 4-site replace to "pipeline-recovery bias floor".
10. **#16 OPTIONAL (Gemini ΔNeff truncation note)** — one-sentence parenthetical at L1074.
11. **#4, #11, #13, #17** — HOUSTON-DECISION items (DOI, PACS, commit SHA inline, units style) — defer to journal-submission moment.

**Estimated closure commit**: `chore(R36conf-stamp): EXT6 P1B → v1B.0.63 closure wave — FB2 BBN flag added to all 4 YAMLs (Path C), FB1 CHANGELOG.md v1B.0.62 entry + README v1B.0.62 + χ²_eff row relabel, FM2 scan-prior midpoint rephrase, FM3 Table IV weighted percentiles, FM1 §V.B caveated framing, App A table-ref drift fix`. Single restamp bundle.

---

## Audit notes

- **HD-4 (Zenodo tagged release)** applied to FB1(d): pre-submission state is legitimate.
- **HD-11 (DOI placeholders)** applied to FB1(d): "DOI assignment is pending (identifiers will be inserted at submission)" is correct procedure.
- **pattern-026 (multi-site claim sync gap)** triggered by #2 and #5: paper §Data Availability promised CHANGELOG entry that wasn't written; tex promised an explicit YAML flag that isn't in the YAMLs. Both are exactly the post-bump-full-sync miss the standing directive is supposed to catch — escalate to `/bigbounce-post-bump-sync` audit hook.
- **pattern-009 (vendor rubber-stamp ACCEPT)** triggered by Grok's "flawless ... immediate publication" verdict that missed two on-disk artifact mismatches.
- **pattern-052 (re-raise of prior-falsified item)** does NOT apply to any FALSIFIED finding here: #3 (JSON invalidity) has no prior falsification record; ChatGPT misread a rendered display as raw newlines.
- **Review-gap-native-pdf compliance**: all 3 vendors received native PDF in EXT6 per the standing directive. ChatGPT additionally cross-referenced the public GitHub repo (this is what surfaced the artifact-layer BLOCKERs Gemini/Grok could not see by scope).
- **No fabrication / no Fisher 1/8.98² superscript artifact** in this round.
